"""Serapan penuh berpecahan atas semesta tahap pertama (ADR-A005).

Semesta: 787 simbol `perpetual_usdt`, 19.598 simbol-bulan. Dibagi 8 pecahan
per ADR-A002 §9.

**Pembagian round-robin atas DAFTAR SIMBOL urut abjad** (`indeks % total`),
bukan potong blok dan bukan atas simbol-bulan:
- seluruh riwayat satu simbol selalu jatuh di pecahan yang sama, sehingga
  penggabungan tidak perlu melintasi pecahan;
- potong blok akan menumpuk simbol berawalan angka di pecahan 0 dan berawalan
  Z di pecahan 7, membuat umur dan ukuran berkas timpang. Itu pelajaran
  langsung dari KC-13.

**Daftar bulan DITANYAKAN ke arsip** lewat `arsip.bulan_tersedia`, tidak
diturunkan dari `bulan_pertama..bulan_terakhir`: `semesta_rentang.json` hanya
menyimpan ujung dan `cacah_bulan`, sehingga simbol yang pernah jeda akan
menghasilkan bulan hantu bila rentangnya sekadar dibentangkan. Selisihnya nol
pada kedelapan pecahan sejauh ini; itu tetap dilaporkan, tidak diasumsikan
(aturan 36).

**Persistensi (ADR-A006 bagian 2/2).** Dulu parquet ditulis, diukur, lalu
dihapus — ±1,5 jam runner terbakar untuk menghasilkan angka saja. Kini, bila
`PECAHAN_KEMAS=1`, tiap parquet dialirkan ke `rilis.PengemasBerbelah` yang
menghapus sumbernya segera setelah masuk tar, sehingga puncak cakram tetap
≈ satu ukuran pecahan pada runner yang hanya punya ±14 GB. Tar terbelah ≤1,8 GB
+ `SHA256SUMS` diunggah workflow sebagai aset rilis — di luar git, karena 32,71
GB tidak boleh masuk riwayat repo.

`parquet_dipersistenkan` bernilai `true` HANYA bila `verifikasi()` membaca ulang
setiap tar, sha256-nya cocok, dan cacah anggotanya sama dengan cacah berkas yang
dikemas. Klaim persistensi diikat pada pembacaan ulang, bukan pada niat
mengunggah (aturan 24).

Riwayat VERSI:

- **3** — pengemas dinyalakan. Run `30376241019` hijau, tetapi medan
  penggugurnya menolak klaimnya sendiri: model ukuran tar mengabaikan header
  **pax** 1.024 byte per anggota.
- **4** — model diperbaiki (kepala anggota 3 blok). Run `30383278359`:
  `verifikasi_rilis.sah` = `true` di ketujuh pecahan, 17.178 parquet
  terpersistensi, 20 bagian tar, nol taksiran terlampaui.
- **5** — matriks diperluas ke `0..7`. Run `30389402113`: kedelapan pecahan sah,
  **19.586 parquet, 23 bagian, 32.706.262.375 byte**, seluruhnya di bawah SATU
  `run_id` dan SATU `sidik_kode`.
- **6** — **KC-17.** Sampai VERSI 5, pengemas hanya menerima `baris["parquet"]`.
  Baris karantina menaruh jalurnya di `baris["parquet_karantina"]`, sehingga
  **12 berkas (13.247.705 byte) diukur, didaftar, lalu lenyap bersama runner** —
  padahal ADR-A006 berbunyi "disisihkan, bukan dibuang". Ukurannya 0,04% semesta,
  tetapi justru berkas itulah bahan bukti KC-14 dan KC-15 dan bahan baku
  pemulihan ADR-A007. VERSI 6 mengemasnya ke tar kedua dengan berkas sidik
  sendiri, dan menambah medan penggugur `cacah_karantina_tak_terkemas`.

  Dua jebakan yang sudah diperiksa sebelum run, bukan sesudah:
  - `tutup()` semula selalu menulis `data/rilis/SHA256SUMS`, jadi pengemas kedua
    akan MENIMPA sidik bagian utama tanpa satu pun medan penggugur menyala;
    karena itu `rilis.py` kini menerima `nama_sums`;
  - pengemas tanpa anggota menghasilkan `sah` = false. Pecahan 2 dan 5 memang
    nol karantina, jadi pengemas karantina dibuat MALAS — hanya begitu baris
    karantina pertama muncul — dan "nol karantina" tidak boleh dibaca sebagai
    kegagalan persistensi.

**VERSI** dinaikkan setiap kali pecahan perlu dijalankan ulang. Pemicu-diri
workflow sudah dicabut (aturan 33), dan modul inilah satu-satunya pemicu run,
sehingga menaikkan VERSI adalah cara sengaja untuk menyalakannya.

Aturan yang ditegakkan: 18, 20, 22, 24, 25, 28, 30, 32, 33, 36, 37, 43, 44.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

from . import arsip, rilis, serap

VERSI = 6
SUMBER_RENTANG = serap.SUMBER_RENTANG
TOTAL_PECAHAN = 8
JENIS_DIIZINKAN = serap.JENIS_DIIZINKAN


def nama_keluaran(indeks: int) -> str:
    return f"reports/manifes_pecahan_{indeks}.json"


def nama_dasar_rilis(indeks: int) -> str:
    return f"pecahan_{indeks}"


def nama_dasar_karantina(indeks: int) -> str:
    return f"pecahan_{indeks}_karantina"


def sidik_kode() -> str:
    """Aturan 22: modul ini ditambah seluruh rantai yang dipakainya.

    `rilis.py` masuk sejak VERSI 3: bila pengemas berubah, sidiknya berubah,
    sehingga manifes lama tidak bisa disalahartikan sebagai hasil kode baru.
    """
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(
        [
            "pecahan.py",
            "serap.py",
            "arsip.py",
            "klines.py",
            "gerbang_1m.py",
            "resample.py",
            "rilis.py",
        ]
    ):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def simbol_pecahan(
    rentang: Dict[str, Any], jenis_dari, indeks: int, total: int = TOTAL_PECAHAN
) -> List[str]:
    """Simbol milik satu pecahan, round-robin atas daftar urut abjad."""
    if total <= 0:
        raise ValueError("total pecahan wajib positif")
    if not 0 <= indeks < total:
        raise ValueError(f"indeks pecahan {indeks} di luar 0..{total - 1}")
    layak = [
        s
        for s, isi in sorted(rentang.items())
        if isinstance(isi, dict) and jenis_dari(s) == JENIS_DIIZINKAN
    ]
    return [s for i, s in enumerate(layak) if i % total == indeks]


def kemas_diminta(kemas: Optional[bool] = None) -> bool:
    """Gerbang env `PECAHAN_KEMAS`; argumen eksplisit selalu menang."""
    if kemas is not None:
        return bool(kemas)
    return str(os.environ.get("PECAHAN_KEMAS", "0") or "0").strip() == "1"


def jalankan(
    indeks: int,
    total: int = TOTAL_PECAHAN,
    akar: str = ".",
    hapus_parquet: bool = True,
    kemas: Optional[bool] = None,
) -> Dict[str, Any]:
    from ..semesta import taksonomi

    basis = Path(akar)
    mentah = (basis / SUMBER_RENTANG).read_bytes()
    rentang = json.loads(mentah.decode("utf-8")).get("rentang", {})
    if not isinstance(rentang, dict):
        rentang = {}

    simbol = simbol_pecahan(rentang, taksonomi.jenis_instrumen, indeks, total)
    batas = int(os.environ.get("PECAHAN_BATAS_SIMBOL", "0") or 0)
    if batas > 0:
        simbol = simbol[:batas]

    mengemas = kemas_diminta(kemas)
    pengemas = (
        rilis.PengemasBerbelah(akar=akar, nama_dasar=nama_dasar_rilis(indeks))
        if mengemas
        else None
    )
    # Dibuat MALAS: pecahan tanpa karantina tidak boleh menghasilkan pengemas
    # kosong, karena laporan pengemas kosong berstatus tidak sah.
    pengemas_kar: Optional[rilis.PengemasBerbelah] = None

    manifes: List[Dict[str, Any]] = []
    selisih_bulan: List[Dict[str, Any]] = []
    gagal_daftar: List[str] = []
    cacah_parquet_ditulis = 0
    cacah_parquet_karantina_ditulis = 0

    for nama in simbol:
        isi = rentang.get(nama) or {}
        try:
            bulan = sorted(arsip.bulan_tersedia(nama))
        except Exception as exc:  # noqa: BLE001
            gagal_daftar.append(f"{nama}: {str(exc)[:120]}")
            continue

        diharap = isi.get("cacah_bulan")
        if isinstance(diharap, int) and diharap != len(bulan):
            selisih_bulan.append(
                {
                    "simbol": nama,
                    "cacah_bulan_rentang": diharap,
                    "cacah_bulan_arsip": len(bulan),
                }
            )

        mati = bool(str(isi.get("bulan_terakhir") or "") < serap.BATAS_HIDUP)
        for b in bulan:
            baris = serap.serap_satu(nama, b, akar=akar, terhenti=mati)
            jalur_rel = baris.get("parquet")
            jalur_kar = baris.get("parquet_karantina")
            if jalur_rel:
                cacah_parquet_ditulis += 1
                if pengemas is not None:
                    hasil = pengemas.tambah(str(jalur_rel))
                    baris["dikemas"] = bool(hasil.get("ditambahkan"))
                elif hapus_parquet:
                    jalur = basis / str(jalur_rel)
                    if jalur.exists():
                        jalur.unlink()
            elif jalur_kar:
                # KC-17: karantina dikemas, TIDAK PERNAH dihapus tanpa dikemas.
                cacah_parquet_karantina_ditulis += 1
                if mengemas:
                    if pengemas_kar is None:
                        pengemas_kar = rilis.PengemasBerbelah(
                            akar=akar,
                            nama_dasar=nama_dasar_karantina(indeks),
                            nama_sums=rilis.NAMA_SUMS_KARANTINA,
                        )
                    hasil = pengemas_kar.tambah(str(jalur_kar))
                    baris["dikemas_karantina"] = bool(hasil.get("ditambahkan"))
            manifes.append(baris)

    laporan_rilis: Optional[Dict[str, Any]] = None
    periksa_rilis: Optional[Dict[str, Any]] = None
    if pengemas is not None:
        laporan_rilis = pengemas.tutup()
        periksa_rilis = rilis.verifikasi(akar, laporan_rilis)

    laporan_kar: Optional[Dict[str, Any]] = None
    periksa_kar: Optional[Dict[str, Any]] = None
    if pengemas_kar is not None:
        laporan_kar = pengemas_kar.tutup()
        periksa_kar = rilis.verifikasi(akar, laporan_kar)

    if mengemas:
        tak_terkemas: Optional[int] = cacah_parquet_ditulis - int(
            (laporan_rilis or {}).get("cacah_berkas") or 0
        )
        kar_tak_terkemas: Optional[int] = cacah_parquet_karantina_ditulis - int(
            (laporan_kar or {}).get("cacah_berkas") or 0
        )
        karantina_sah = (
            True
            if cacah_parquet_karantina_ditulis == 0
            else bool(periksa_kar and periksa_kar.get("sah") is True)
        )
        dipersistenkan = (
            bool(periksa_rilis and periksa_rilis.get("sah") is True)
            and tak_terkemas == 0
            and kar_tak_terkemas == 0
            and karantina_sah
        )
    else:
        tak_terkemas = None
        kar_tak_terkemas = None
        karantina_sah = False
        dipersistenkan = False

    laporan = serap.ringkas(manifes)
    laporan["bukan_bukti"] = False
    laporan["versi_pecahan"] = VERSI
    laporan["pecahan"] = {
        "indeks": indeks,
        "total": total,
        "cacah_simbol": len(simbol),
        "cacah_simbol_gagal_daftar": len(gagal_daftar),
        "contoh_gagal_daftar": gagal_daftar[:10],
    }
    laporan["selisih_cacah_bulan"] = {
        "cacah_simbol_berselisih": len(selisih_bulan),
        "contoh": selisih_bulan[:10],
        "catatan": (
            "daftar bulan diambil dari arsip; cacah_bulan di semesta_rentang.json "
            "berasal dari survei terdahulu. Selisih dicatat, tidak dibulatkan hilang "
            "(aturan 36)."
        ),
    }
    laporan["cacah_parquet_ditulis"] = cacah_parquet_ditulis
    laporan["cacah_parquet_karantina_ditulis"] = cacah_parquet_karantina_ditulis
    laporan["mengemas"] = mengemas
    laporan["rilis"] = laporan_rilis
    laporan["verifikasi_rilis"] = periksa_rilis
    laporan["rilis_karantina"] = laporan_kar
    laporan["verifikasi_rilis_karantina"] = periksa_kar
    laporan["cacah_parquet_tak_terkemas"] = tak_terkemas
    laporan["cacah_karantina_tak_terkemas"] = kar_tak_terkemas
    laporan["karantina_dipersistenkan"] = bool(mengemas and karantina_sah)
    laporan["parquet_dipersistenkan"] = bool(dipersistenkan)
    laporan["catatan_parquet"] = (
        "parquet dialirkan ke tar terbelah <=1,8 GB lalu diunggah sebagai aset "
        "rilis; parquet_dipersistenkan true HANYA bila tiap tar dibaca ulang, "
        "sha256-nya cocok, dan cacah anggotanya sama dengan cacah berkas yang "
        "dikemas (aturan 24). cacah_parquet_tak_terkemas != 0 berarti ada parquet "
        "yang lenyap antara penulisan dan pengemasan"
        if mengemas
        else "PECAHAN_KEMAS tidak aktif: parquet ditulis, diukur, lalu dihapus"
    )
    laporan["catatan_karantina_persistensi"] = (
        "KC-17: sampai VERSI 5 parquet karantina diukur lalu lenyap bersama "
        "runner. Sejak VERSI 6 ia dikemas ke tar terpisah dengan berkas sidik "
        "SHA256SUMS_KARANTINA. cacah_karantina_tak_terkemas != 0 berarti cacat "
        "itu kambuh. Pecahan tanpa karantina melaporkan rilis_karantina null dan "
        "karantina_dipersistenkan true dengan penyebut nol — itu BUKAN bukti "
        "pengemas karantina bekerja (aturan 30, 41)"
    )
    laporan["catatan_rentang"] = (
        f"hasil berlaku untuk pecahan {indeks} dari {total} saja, bukan untuk "
        "19.598 bulan perpetual_usdt (aturan 20)"
    )
    laporan["catatan_bulan_parsial"] = (
        "bulan pertama dan terakhir tiap simbol PARSIAL; rerata baris per bulan "
        "dilarang dikalikan begitu saja (aturan 28)"
    )
    laporan["manifes"] = [
        {k: v for k, v in b.items() if not k.startswith("_")} for b in manifes
    ]
    laporan["sumber_rentang"] = SUMBER_RENTANG
    laporan["sidik_data"] = hashlib.sha256(mentah).hexdigest()
    laporan["sidik_kode"] = sidik_kode()
    laporan["waktu_utc"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    tujuan = basis / nama_keluaran(indeks)
    tujuan.parent.mkdir(parents=True, exist_ok=True)
    tujuan.write_text(
        json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return laporan


def main() -> None:
    indeks = int(os.environ.get("PECAHAN_INDEKS", "0") or 0)
    total = int(os.environ.get("PECAHAN_TOTAL", str(TOTAL_PECAHAN)) or TOTAL_PECAHAN)
    hasil = jalankan(indeks, total)
    print(
        json.dumps(
            {k: v for k, v in hasil.items() if k != "manifes"},
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
