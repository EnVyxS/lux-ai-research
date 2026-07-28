"""Pengemasan parquet menjadi aset rilis: tar terbelah + SHA256SUMS.

Menjalankan ADR-A006 Keputusan 3. Masalahnya konkret: aset rilis GitHub
berbatas 2 GB per berkas, sementara satu pecahan menghasilkan ±4,1 GB parquet
(semesta penuh 32,71 GB). Tanpa modul ini setiap serapan membakar ±1,5 jam
runner untuk menghasilkan ANGKA lalu menghapus datanya.

Rancangan:

- **Aliran, bukan tumpuk.** Berkas ditambahkan satu per satu dan sumbernya
  dihapus segera setelah masuk tar, sehingga puncak pemakaian cakram ≈ satu
  bagian tar, bukan dua kali ukuran pecahan. Runner hanya punya ±14 GB.
- **Tar tanpa gzip.** Parquet sudah terkompresi; gzip di atasnya membakar CPU
  untuk penghematan yang mendekati nol.
- **Batas 1,8 GB**, bukan 2 GB, menyisakan ruang bagi kepala tar dan bantalan.
- **Berkas tunggal yang lebih besar dari batas tidak dipecah byte-nya.** Ia
  ditempatkan di bagiannya sendiri dan dicatat di `cacah_berkas_melebihi_batas`.
  Memecah satu berkas parquet akan membuat bagian tar tak bisa dibaca sendiri.

## Ukuran tar: tiga lapis, dua di antaranya mahal dipelajari

1. **Isi tiap anggota** dibulatkan ke blok 512 byte.
2. **Kepala tiap anggota = 3 blok, bukan 1.** Sejak Python 3.8 `tarfile` memakai
   format **PAX** sebagai baku, dan pax menulis header tambahan (satu blok
   kepala + satu blok isi = 1.024 byte) untuk anggota yang butuh field
   diperluas — di sini `mtime` berpecahan detik, yang dimiliki hampir semua
   parquet yang baru ditulis. Terukur pada run **`30376241019`**: bagian dengan
   1.055 anggota meleset 1.054.720 byte dari taksiran, 1.044 anggota meleset
   1.044.480, dan 366 anggota meleset 348.160 — semuanya ≈ 1.024 byte per
   anggota. Taksiran + 1.055 × 1.024 cocok dengan tar nyata sampai sisa 512 byte.
3. **Seluruh arsip** dibulatkan ke `tarfile.RECORDSIZE` = 10.240 byte, dan
   `MARGIN_REKAM` (2 rekam) ditambahkan sebagai bantalan sisa.

Sejarah yang wajib diingat: lapis 2 sempat muncul sebagai "tar selalu satu rekam
lebih besar" (jurnal 54), karena pada uji sintetis 6 anggota galat 6 × 1.024
masih lebih kecil daripada satu rekam. **Margin tetap menyembunyikan galat yang
menskala** — lihat aturan 43. Karena itu uji regresi modul ini memakai 120
anggota, bukan 6.

## Dua pengemas dalam satu direktori (KC-17)

Semula `tutup()` selalu menulis `data/rilis/SHA256SUMS`. Begitu pengemas KEDUA
dipakai untuk parquet karantina di direktori yang sama, berkas itu akan tertimpa
dan sidik bagian utama lenyap tanpa satu pun medan penggugur menyala. Karena itu
nama berkas sidik kini dapat dipilih lewat `nama_sums`, dan pengemas karantina
memakai `NAMA_SUMS_KARANTINA`. Keduanya tetap di `data/rilis` supaya satu glob
unggahan cukup, dan nama asetnya tidak pernah bertabrakan di satu tag rilis.

Semua keputusan pembelahan lewat SATU fungsi, `taksir_bagian()`, supaya model
ukuran tidak bisa berbeda antara `rencana_belah` dan `PengemasBerbelah`
(aturan 9).

Medan penggugur (aturan 24): `cacah_bagian_melebihi_batas`,
`cacah_berkas_melebihi_batas`, `cacah_bagian_taksiran_terlampaui`, dan
`verifikasi()` yang membaca ulang tiap tar lalu mencocokkan cacah anggota dan
sha256. Bila salah satu tidak nol atau tidak cocok, rilisnya TIDAK sah dan tidak
boleh dianggap persistensi. Medan itulah yang menangkap cacat pax pada skala
nyata setelah 16 uji sintetis lolos; ia tidak boleh dilunakkan.

Aturan yang ditegakkan: 7, 8, 9, 16, 21, 23, 24, 30, 32, 39, 43.
"""

from __future__ import annotations

import hashlib
import tarfile
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence

# 1,8 GB desimal. Aset rilis GitHub berbatas 2 GB; sisanya bantalan tar.
BATAS_BAGIAN = 1_800_000_000
BLOK_TAR = 512
BLOK_PAX = 2 * BLOK_TAR  # header pax: satu blok kepala + satu blok isi
KEPALA_ANGGOTA = BLOK_TAR + BLOK_PAX  # 1.536 byte per anggota
BYTE_AKHIR_TAR = 2 * BLOK_TAR  # dua blok nol penutup arsip
REKAM_TAR = tarfile.RECORDSIZE  # 10.240 byte; ukuran tar selalu kelipatan ini
MARGIN_REKAM = 2 * REKAM_TAR  # bantalan sisa pembulatan
NAMA_SUMS = "SHA256SUMS"
NAMA_SUMS_KARANTINA = "SHA256SUMS_KARANTINA"
AKAR_RILIS = "data/rilis"
POTONG_BACA = 1024 * 1024


def perkiraan_byte_anggota(ukuran: int) -> int:
    """Byte yang dipakai satu anggota tar: kepala 3 blok + isi berbantalan.

    Tiga blok, bukan satu: format pax menambahkan 1.024 byte per anggota. Galat
    ini menskala dengan cacah anggota, jadi ia TIDAK boleh diserahkan kepada
    margin (aturan 43).
    """
    ukuran = int(ukuran)
    if ukuran < 0:
        raise ValueError("ukuran anggota tidak boleh negatif")
    blok_isi = (ukuran + BLOK_TAR - 1) // BLOK_TAR
    return KEPALA_ANGGOTA + blok_isi * BLOK_TAR


def bulatkan_rekam(byte: int) -> int:
    """Bulatkan ke atas ke kelipatan `REKAM_TAR`, seperti yang `tarfile` tulis."""
    byte = int(byte)
    if byte < 0:
        raise ValueError("byte tidak boleh negatif")
    rekam = (byte + REKAM_TAR - 1) // REKAM_TAR
    return rekam * REKAM_TAR


def taksir_bagian(byte_anggota_berbantalan: int) -> int:
    """Taksiran ATAS ukuran satu bagian tar; satu-satunya model yang dipakai."""
    return bulatkan_rekam(byte_anggota_berbantalan) + MARGIN_REKAM


def batas_terlalu_kecil(batas: int) -> bool:
    """Batas mustahil: tak sanggup memuat satu rekam beserta marginnya."""
    return int(batas) < REKAM_TAR + MARGIN_REKAM


def rencana_belah(ukuran: Sequence[int], batas: int = BATAS_BAGIAN) -> List[List[int]]:
    """Bagi indeks berkas ke bagian-bagian tar, tanpa menyentuh cakram."""
    if batas_terlalu_kecil(batas):
        raise ValueError("batas terlalu kecil untuk memuat satu rekam beserta margin")
    bagian: List[List[int]] = []
    kini: List[int] = []
    byte_kini = BYTE_AKHIR_TAR
    for i, u in enumerate(ukuran):
        tambahan = perkiraan_byte_anggota(u)
        if kini and taksir_bagian(byte_kini + tambahan) > batas:
            bagian.append(kini)
            kini = []
            byte_kini = BYTE_AKHIR_TAR
        kini.append(i)
        byte_kini += tambahan
    if kini:
        bagian.append(kini)
    return bagian


def sha256_berkas(jalur: Path) -> str:
    h = hashlib.sha256()
    with open(jalur, "rb") as f:
        for bongkah in iter(lambda: f.read(POTONG_BACA), b""):
            h.update(bongkah)
    return h.hexdigest()


def baris_sums(bagian: Iterable[Dict[str, Any]]) -> str:
    """Format baku `sha256sum`: sidik, dua spasi, nama berkas."""
    return "".join(f"{b['sha256']}  {b['nama']}\n" for b in bagian)


class PengemasBerbelah:
    """Kemas berkas ke deret tar `<dasar>.part<NN>.tar` dengan batas ukuran."""

    def __init__(
        self,
        akar: str = ".",
        nama_dasar: str = "parquet",
        tujuan: str = AKAR_RILIS,
        batas: int = BATAS_BAGIAN,
        nama_sums: str = NAMA_SUMS,
    ) -> None:
        if batas_terlalu_kecil(batas):
            raise ValueError(
                "batas terlalu kecil untuk memuat satu rekam beserta margin"
            )
        self.akar = Path(akar)
        self.nama_dasar = nama_dasar
        self.tujuan = self.akar / tujuan
        self.rel_tujuan = tujuan
        self.batas = int(batas)
        self.nama_sums = nama_sums
        self.tujuan.mkdir(parents=True, exist_ok=True)
        self._tar: Optional[tarfile.TarFile] = None
        self._jalur_kini: Optional[Path] = None
        self._byte_taksir = 0
        self._cacah_kini = 0
        self.bagian: List[Dict[str, Any]] = []
        self.cacah_berkas = 0
        self.byte_anggota_total = 0
        self.cacah_berkas_melebihi_batas = 0
        self.cacah_berkas_hilang = 0

    # —— bagian dalam ——

    def _nama_bagian(self, nomor: int) -> str:
        return f"{self.nama_dasar}.part{nomor:02d}.tar"

    def _buka(self) -> None:
        nomor = len(self.bagian) + 1
        self._jalur_kini = self.tujuan / self._nama_bagian(nomor)
        self._tar = tarfile.open(self._jalur_kini, "w")
        self._byte_taksir = BYTE_AKHIR_TAR
        self._cacah_kini = 0

    def _tutup_bagian(self) -> None:
        if self._tar is None or self._jalur_kini is None:
            return
        self._tar.close()
        self._tar = None
        jalur = self._jalur_kini
        byte_nyata = int(jalur.stat().st_size)
        taksir = taksir_bagian(self._byte_taksir)
        self.bagian.append(
            {
                "nama": jalur.name,
                "jalur": str(Path(self.rel_tujuan) / jalur.name),
                "byte": byte_nyata,
                "byte_taksir": self._byte_taksir,
                "byte_taksir_dibulatkan": taksir,
                "cacah_berkas": self._cacah_kini,
                "sha256": sha256_berkas(jalur),
                "melebihi_batas": byte_nyata > self.batas,
                "taksiran_terlampaui": byte_nyata > taksir,
            }
        )
        self._jalur_kini = None
        self._byte_taksir = 0
        self._cacah_kini = 0

    # —— antarmuka ——

    def tambah(self, jalur_relatif: str, hapus: bool = True) -> Dict[str, Any]:
        """Masukkan satu berkas ke tar; sumbernya dihapus bila `hapus`."""
        sumber = self.akar / jalur_relatif
        if not sumber.exists():
            self.cacah_berkas_hilang += 1
            return {"jalur": jalur_relatif, "ditambahkan": False, "sebab": "tidak ada"}

        ukuran = int(sumber.stat().st_size)
        tambahan = perkiraan_byte_anggota(ukuran)
        if taksir_bagian(BYTE_AKHIR_TAR + tambahan) > self.batas:
            self.cacah_berkas_melebihi_batas += 1

        if self._tar is None:
            self._buka()
        elif (
            self._cacah_kini
            and taksir_bagian(self._byte_taksir + tambahan) > self.batas
        ):
            self._tutup_bagian()
            self._buka()

        assert self._tar is not None
        self._tar.add(str(sumber), arcname=str(jalur_relatif))
        self._byte_taksir += tambahan
        self._cacah_kini += 1
        self.cacah_berkas += 1
        self.byte_anggota_total += ukuran
        if hapus:
            sumber.unlink()
        return {
            "jalur": jalur_relatif,
            "ditambahkan": True,
            "byte": ukuran,
            "bagian": len(self.bagian) + 1,
        }

    def tutup(self) -> Dict[str, Any]:
        """Tutup bagian terakhir, tulis berkas sidik, kembalikan laporan."""
        self._tutup_bagian()
        jalur_sums: Optional[str] = None
        if self.bagian:
            berkas_sums = self.tujuan / self.nama_sums
            berkas_sums.write_text(baris_sums(self.bagian), encoding="utf-8")
            jalur_sums = str(Path(self.rel_tujuan) / self.nama_sums)
        return self.laporan(jalur_sums)

    def laporan(self, jalur_sums: Optional[str] = None) -> Dict[str, Any]:
        byte_bagian = sum(int(b["byte"]) for b in self.bagian)
        return {
            "status": "TERKEMAS" if self.bagian else "TIDAK MENGEMAS",
            "nama_dasar": self.nama_dasar,
            "nama_sums": self.nama_sums,
            "batas_byte": self.batas,
            "rekam_tar": REKAM_TAR,
            "margin_rekam": MARGIN_REKAM,
            "kepala_anggota": KEPALA_ANGGOTA,
            "cacah_bagian": len(self.bagian),
            "cacah_berkas": self.cacah_berkas,
            "byte_anggota_total": self.byte_anggota_total,
            "byte_bagian_total": byte_bagian,
            "nisbah_bagian_per_anggota": (
                round(byte_bagian / self.byte_anggota_total, 6)
                if self.byte_anggota_total
                else None
            ),
            "cacah_bagian_melebihi_batas": sum(
                1 for b in self.bagian if b["melebihi_batas"]
            ),
            "cacah_bagian_taksiran_terlampaui": sum(
                1 for b in self.bagian if b["taksiran_terlampaui"]
            ),
            "cacah_berkas_melebihi_batas": self.cacah_berkas_melebihi_batas,
            "cacah_berkas_hilang": self.cacah_berkas_hilang,
            "bagian": self.bagian,
            "berkas_sums": jalur_sums,
            "catatan_penggugur": (
                "cacah_bagian_melebihi_batas > 0 berarti ada aset yang akan ditolak "
                "batas 2 GB rilis GitHub; cacah_bagian_taksiran_terlampaui > 0 "
                "berarti model ukuran lebih kecil daripada tar nyata dan tidak boleh "
                "dipercaya; cacah_berkas_hilang > 0 berarti manifes menyebut parquet "
                "yang tidak ada di cakram. Ketiganya membatalkan klaim persistensi "
                "(aturan 24)"
            ),
            "catatan_kompresi": (
                "tar tanpa gzip: parquet sudah terkompresi, jadi nisbah bagian per "
                "anggota mendekati 1 dan selisihnya adalah kepala 1.536 byte per "
                "anggota (termasuk pax 1.024), pembulatan rekam 10.240 byte, dan "
                "margin 20.480 byte"
            ),
        }


def verifikasi(akar: str, laporan: Dict[str, Any]) -> Dict[str, Any]:
    """Baca ulang tiap bagian tar: cocokkan sha256 dan cacah anggotanya."""
    basis = Path(akar)
    cocok = 0
    tak_cocok: List[str] = []
    anggota = 0
    hilang: List[str] = []
    for b in laporan.get("bagian") or []:
        jalur = basis / str(b["jalur"])
        if not jalur.exists():
            hilang.append(str(b["nama"]))
            continue
        if sha256_berkas(jalur) == b["sha256"]:
            cocok += 1
        else:
            tak_cocok.append(str(b["nama"]))
        with tarfile.open(jalur, "r") as tar:
            anggota += sum(1 for m in tar.getmembers() if m.isfile())
    diharap = int(laporan.get("cacah_berkas") or 0)
    return {
        "cacah_sha_cocok": cocok,
        "cacah_sha_tak_cocok": len(tak_cocok),
        "nama_sha_tak_cocok": tak_cocok[:20],
        "cacah_bagian_hilang": len(hilang),
        "nama_bagian_hilang": hilang[:20],
        "cacah_anggota_terbaca": anggota,
        "cacah_anggota_diharap": diharap,
        "anggota_cocok": anggota == diharap,
        "sah": (
            bool(laporan.get("bagian"))
            and not tak_cocok
            and not hilang
            and anggota == diharap
            and int(laporan.get("cacah_bagian_melebihi_batas") or 0) == 0
            and int(laporan.get("cacah_bagian_taksiran_terlampaui") or 0) == 0
        ),
    }
