"""Kehidupan per simbol-bulan: pelabelan MATI / SEPI / HIDUP menurut ADR-A008.

Latar. KC-18 menyatakan arsip menerbitkan klines 1m yang sempurna secara BENTUK
(43.200 lilin, cap waktu rapat, checksum cocok) untuk pasar yang tidak
diperdagangkan. Gerbang 1m meloloskannya karena ia menilai bentuk deret, bukan
kehidupan pasar. ADR-A008 memutuskan lilin datar TIDAK dijatuhkan, melainkan
DILABELI, dan bahwa setiap penyebut diterbitkan berpasangan supaya baris mati
tidak pernah diam-diam ikut menjadi penyebut.

Modul ini menjalankan Keputusan 2, 3, dan 4 ADR-A008 pada bentangan yang belum
pernah diukur: SELURUH 456 simbol-bulan kohort funding 2025-07 (38 simbol x 12
bulan, 2025-07..2026-06). Sebelum ini kehidupan hanya terukur pada 10 simbol
lewat `kohort_ekor` V4, dan aturan 20 melarang menyimpulkan tentang 28 sisanya.

Definisi, persis seperti ADR-A008 dan tanpa istilah ketiga yang kabur:

- **MATI** bila `transaksi_total` = 0 pada simbol-bulan itu.
- **SEPI** bila bukan MATI dan `bagian_volume_nol` >= `AMBANG_SEPI` (0,5).
- **HIDUP** selain keduanya.
- **TAK_TERUKUR** bila berkasnya gagal diunduh, gagal checksum, tidak pernah
  diterbitkan arsip, atau tidak memuat satu lilin pun. TAK_TERUKUR BUKAN nol dan
  tidak pernah ikut ke dalam penyebut mana pun (aturan 41).

Penyebut ganda (Keputusan 3). `penyebut_penuh` mencacah simbol-bulan terukur apa
adanya; `penyebut_tanpa_mati` mencacah yang sama dikurangi yang MATI. Keduanya
diterbitkan berdampingan, selalu, walau selisihnya nol. Bila seluruhnya MATI,
`penyebut_tanpa_mati` = 0 dan `penyebut_tanpa_mati_kosong` menyala, supaya nol
itu tak pernah dipakai membagi diam-diam.

Kendali positif (aturan 50). BTCUSDT dan ETHUSDT diukur pada bulan pertama dan
terakhir jendela yang sama. Bila salah satu tidak terbaca HIDUP, `parser_terbukti`
false dan SELURUH klaim kematian di laporan ini batal, bukan sekadar lemah.

DIAGNOSTIK, bukan gerbang. Modul ini tidak menjatuhkan satu simbol-bulan pun,
tidak menulis apa pun ke manifes, dan tidak menulis ulang 839.842.134
(aturan 29). Ia hanya menerbitkan label dan penyebut kedua.

Praregistrasi ramalan, ditulis SEBELUM run mana pun.

- **R-200** — CI mengumpulkan **269 butir** dengan kode keluar 0. Satuan: BUTIR
  yang dikumpulkan pytest, bukan fungsi uji (aturan 38, 47). Dasar: 244 + 9 = 253
  terverifikasi pada run 30417800419, ditambah 16 butir baru dari
  `tests/test_kehidupan.py` (12 fungsi berbutir tunggal + 1 fungsi berparameter
  empat kasus).
- **R-201** — pada jendela 2025-07..2026-06 atas seluruh anggota kohort,
  simbol-bulan berstatus MATI berjumlah dalam pita **350..456**, dan
  `cacah_hidup` = **0**. Satuan: SIMBOL-BULAN. Penyebut disebut eksplisit
  (aturan 44): 456 simbol-bulan kohort yang diminta, bukan 19.598 semesta.
  Pita dipakai, bukan angka tunggal, karena keseragaman hanya terukur pada 10
  dari 38 anggota (aturan 39). Penggugur: bila `parser_terbukti` false, R-201
  dicatat TIDAK TERADJUDIKASI, bukan TEPAT (aturan 41); bila
  `cacah_simbol_bulan_tak_terukur` melampaui 106 sehingga terukur kurang dari
  350, pita atasnya tak dapat dicapai dan ramalan ini MELESET apa adanya.

Aturan yang mengikat modul ini: 10, 16, 20, 21, 22, 24, 29, 30, 37, 41, 44, 46,
47, 48, 50, 52.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

from . import arsip, gerbang_1m, kohort_ekor

VERSI = 1
SUMBER = "reports/funding_semesta.json"
KELUARAN = "reports/kehidupan.json"
KELUARAN_RINGKAS = "reports/kehidupan_ringkas.json"
INTERVAL = "1m"

# Jendela pengukuran: bulan tebing funding sampai bulan klines terakhir yang
# diketahui seragam pada ke-38 anggota. 12 bulan x 38 simbol = 456 simbol-bulan.
BULAN_MULAI = "2025-07"
BULAN_AKHIR = "2026-06"

# Kendali positif: penguji pembaca modul ini sendiri, bukan pembanding pasar.
KENDALI_HIDUP = ("BTCUSDT", "ETHUSDT")

STATUS_MATI = "MATI"
STATUS_SEPI = "SEPI"
STATUS_HIDUP = "HIDUP"
STATUS_TAK_TERUKUR = "TAK_TERUKUR"
STATUS_TERUKUR = (STATUS_MATI, STATUS_SEPI, STATUS_HIDUP)

BERKAS_DICAP = [
    "arsip.py",
    "gerbang_1m.py",
    "kehidupan.py",
    "kohort_ekor.py",
]


def sidik_kode() -> str:
    """Aturan 22 dan 48: cap seluruh berkas yang ikut menentukan angka ini."""
    h = hashlib.sha256()
    for nama in sorted(BERKAS_DICAP):
        h.update((Path(__file__).parent / nama).read_bytes())
    return h.hexdigest()


def _indeks_bulan(bulan):
    potong = str(bulan).split("-")
    if len(potong) != 2:
        return None
    try:
        tahun = int(potong[0])
        bln = int(potong[1])
    except ValueError:
        return None
    if not 1 <= bln <= 12:
        return None
    return tahun * 12 + (bln - 1)


def _bulan_dari_indeks(i: int) -> str:
    return f"{i // 12:04d}-{i % 12 + 1:02d}"


def deret_bulan(mulai: str, akhir: str) -> list:
    """Bulan dari `mulai` sampai `akhir` inklusif, menaik; [] bila tak masuk akal."""
    a = _indeks_bulan(mulai)
    b = _indeks_bulan(akhir)
    if a is None or b is None or b < a:
        return []
    return [_bulan_dari_indeks(i) for i in range(a, b + 1)]


def klasifikasi(baris) -> str:
    """Label satu simbol-bulan menurut definisi ADR-A008.

    Urutan sengaja: ketakterukuran dinilai LEBIH DULU daripada kematian, sebab
    berkas yang tidak ada tidak boleh terbaca sebagai pasar yang mati
    (aturan 41, 46).
    """
    if baris.get("galat"):
        return STATUS_TAK_TERUKUR
    if not baris.get("ada_di_arsip", True):
        return STATUS_TAK_TERUKUR
    if not baris.get("cacah_lilin"):
        return STATUS_TAK_TERUKUR
    transaksi = baris.get("transaksi_total")
    if transaksi is None:
        return STATUS_TAK_TERUKUR
    if int(transaksi) == 0:
        return STATUS_MATI
    bagian_nol = baris.get("bagian_volume_nol")
    if bagian_nol is not None and bagian_nol >= kohort_ekor.AMBANG_SEPI:
        return STATUS_SEPI
    return STATUS_HIDUP


def ukur_satu(simbol: str, bulan: str, peran: str = "kohort") -> dict:
    """Unduh satu simbol-bulan dan labeli isinya. Kegagalan dilaporkan, bukan ditelan."""
    baris = {
        "simbol": simbol,
        "bulan": bulan,
        "peran": peran,
        "ada_di_arsip": True,
        "gagal_unduh": False,
        "gagal_checksum": False,
        "galat": None,
        "byte_zip": None,
        "lolos_gerbang": None,
        "pelanggaran": None,
    }
    try:
        data = arsip.unduh_terverifikasi(arsip.url_klines(simbol, INTERVAL, bulan))
    except Exception as exc:  # noqa: BLE001
        pesan = str(exc)
        baris["galat"] = pesan
        baris["gagal_checksum"] = "checksum tidak cocok" in pesan
        baris["gagal_unduh"] = not baris["gagal_checksum"]
        baris["status"] = STATUS_TAK_TERUKUR
        return baris
    terurai = kohort_ekor.baca_zip_klines(data)
    putusan = gerbang_1m.nilai_deret(terurai["cap_waktu"], simbol, bulan)
    baris.update(kohort_ekor.ringkas_lilin(terurai))
    baris["berheader"] = terurai["berheader"]
    baris["byte_zip"] = len(data)
    baris["cacah_baris_cacat"] = terurai["cacah_baris_cacat"]
    baris["lolos_gerbang"] = putusan["lolos"]
    baris["pelanggaran"] = putusan["pelanggaran"]
    baris["menit_hilang"] = putusan["ukuran"]["menit_hilang_dalam_rentang"]
    baris["status"] = klasifikasi(baris)
    return baris


def ukur_simbol(simbol: str, bulan_diminta, ukur=None, daftar=None) -> list:
    """Ukur satu simbol pada seluruh bulan yang diminta.

    Bulan yang tidak pernah diterbitkan arsip TIDAK diunduh dan TIDAK dianggap
    mati; ia ditandai `ada_di_arsip` false dan berstatus TAK_TERUKUR.
    """
    jalan = ukur or ukur_satu
    lister = daftar or (lambda s: arsip.bulan_tersedia(s, INTERVAL, "klines"))
    try:
        tersedia = set(lister(simbol) or [])
        galat_daftar = None
    except Exception as exc:  # noqa: BLE001
        tersedia = set()
        galat_daftar = f"gagal mendaftar bulan: {exc}"
    hasil = []
    for bulan in bulan_diminta:
        if galat_daftar:
            hasil.append(
                {
                    "simbol": simbol,
                    "bulan": bulan,
                    "peran": "kohort",
                    "ada_di_arsip": None,
                    "gagal_unduh": True,
                    "gagal_checksum": False,
                    "galat": galat_daftar,
                    "status": STATUS_TAK_TERUKUR,
                }
            )
            continue
        if bulan not in tersedia:
            hasil.append(
                {
                    "simbol": simbol,
                    "bulan": bulan,
                    "peran": "kohort",
                    "ada_di_arsip": False,
                    "gagal_unduh": False,
                    "gagal_checksum": False,
                    "galat": None,
                    "status": STATUS_TAK_TERUKUR,
                }
            )
            continue
        hasil.append(jalan(simbol, bulan, "kohort"))
    return hasil


def penyebut_ganda(baris) -> dict:
    """Keputusan 3 ADR-A008: dua penyebut berdampingan, selalu."""
    terukur = [b for b in baris if b.get("status") in STATUS_TERUKUR]
    mati = [b for b in terukur if b.get("status") == STATUS_MATI]
    penuh = len(terukur)
    tanpa_mati = penuh - len(mati)
    return {
        "penyebut_penuh": penuh,
        "penyebut_tanpa_mati": tanpa_mati,
        "penyebut_tanpa_mati_kosong": tanpa_mati == 0,
        "cacah_mati": len(mati),
        "cacah_sepi": sum(1 for b in terukur if b.get("status") == STATUS_SEPI),
        "cacah_hidup": sum(1 for b in terukur if b.get("status") == STATUS_HIDUP),
        "bagian_mati": kohort_ekor.bagian(len(mati), penuh),
        "lilin_penuh": sum(int(b.get("cacah_lilin") or 0) for b in terukur),
        "lilin_tanpa_mati": sum(
            int(b.get("cacah_lilin") or 0)
            for b in terukur
            if b.get("status") != STATUS_MATI
        ),
        "lilin_mati": sum(int(b.get("cacah_lilin") or 0) for b in mati),
    }


def ringkas(baris, kendali) -> dict:
    """Cacah lintas simbol-bulan beserta medan penggugurnya (aturan 24)."""
    semua = list(baris)
    kend = list(kendali)
    angka = penyebut_ganda(semua)
    kendali_terambil = [b for b in kend if not b.get("galat")]
    ringkasan = {
        "cacah_simbol_bulan_diminta": len(semua),
        "cacah_simbol_bulan_terukur": angka["penyebut_penuh"],
        "cacah_simbol_bulan_tak_terukur": sum(
            1 for b in semua if b.get("status") == STATUS_TAK_TERUKUR
        ),
        "cacah_bulan_tidak_ada_di_arsip": sum(
            1 for b in semua if b.get("ada_di_arsip") is False
        ),
        "cacah_gagal_unduh": sum(1 for b in semua if b.get("gagal_unduh")),
        "cacah_gagal_checksum": sum(1 for b in semua if b.get("gagal_checksum")),
        "cacah_baris_cacat": sum(int(b.get("cacah_baris_cacat") or 0) for b in semua),
        "cacah_lolos_gerbang": sum(1 for b in semua if b.get("lolos_gerbang")),
        "cacah_mati_lolos_gerbang": sum(
            1
            for b in semua
            if b.get("status") == STATUS_MATI and b.get("lolos_gerbang")
        ),
        "cacah_kendali_diminta": len(kend),
        "cacah_kendali_terambil": len(kendali_terambil),
        "cacah_kendali_hidup": sum(
            1 for b in kend if b.get("status") == STATUS_HIDUP
        ),
        "parser_terbukti": bool(kend)
        and all(b.get("status") == STATUS_HIDUP for b in kend),
    }
    ringkasan.update(angka)
    return ringkasan


def berkas_ringkas(laporan: dict, teks_sumber: str) -> dict:
    """Aturan 52: ringkasan yang membuktikan berasal dari laporan penuh yang ini."""
    byte_sumber = teks_sumber.encode("utf-8")
    return {
        "versi_kehidupan": laporan.get("versi_kehidupan"),
        "sidik_kode": laporan.get("sidik_kode"),
        "berkas_sumber": KELUARAN,
        "byte_sumber": len(byte_sumber),
        "sidik_sumber": hashlib.sha256(byte_sumber).hexdigest(),
        "bulan_mulai": laporan.get("bulan_mulai"),
        "bulan_akhir": laporan.get("bulan_akhir"),
        "cacah_simbol_diukur": len(laporan.get("simbol_diukur") or []),
        "galat_kohort": laporan.get("galat_kohort"),
        "definisi": laporan.get("definisi"),
        "ringkasan": laporan.get("ringkasan"),
    }


def jalankan(akar: str = ".") -> dict:
    kohort = kohort_ekor.muat_kohort(akar)
    batas = int(os.environ.get("KEHIDUPAN_BATAS_SIMBOL", "0") or 0)
    mulai = os.environ.get("KEHIDUPAN_BULAN_MULAI") or BULAN_MULAI
    akhir = os.environ.get("KEHIDUPAN_BULAN_AKHIR") or BULAN_AKHIR
    bulan = deret_bulan(mulai, akhir)
    tersedia_simbol = list(kohort.get("simbol") or [])
    dipilih = tersedia_simbol[:batas] if batas > 0 else tersedia_simbol

    baris = []
    kendali = []
    if not kohort.get("galat") and bulan:
        for simbol in dipilih:
            baris += ukur_simbol(simbol, bulan)
        bulan_kendali = list(dict.fromkeys([bulan[0], bulan[-1]]))
        for simbol in KENDALI_HIDUP:
            for b in bulan_kendali:
                kendali.append(ukur_satu(simbol, b, "kendali_hidup"))

    return {
        "versi_kehidupan": VERSI,
        "sidik_kode": sidik_kode(),
        "sumber_kohort": SUMBER,
        "galat_kohort": kohort.get("galat"),
        "cacah_simbol_kohort": kohort.get("cacah_simbol_kohort"),
        "simbol_diukur": dipilih,
        "simbol_kendali_hidup": list(KENDALI_HIDUP),
        "bulan_mulai": mulai,
        "bulan_akhir": akhir,
        "bulan_diminta": bulan,
        "cacah_bulan_per_simbol": len(bulan),
        "ambang_sepi": kohort_ekor.AMBANG_SEPI,
        "definisi": {
            "MATI": "transaksi_total == 0",
            "SEPI": "bukan MATI dan bagian_volume_nol >= ambang_sepi",
            "HIDUP": "selain keduanya",
            "TAK_TERUKUR": (
                "gagal unduh, gagal checksum, tidak diterbitkan arsip, atau tanpa "
                "satu lilin pun; BUKAN nol dan tidak masuk penyebut mana pun"
            ),
        },
        "baris": baris,
        "kendali": kendali,
        "ringkasan": ringkas(baris, kendali),
        "catatan_bukan_bukti": (
            "laporan ini diagnostik: ia TIDAK menjatuhkan simbol-bulan mana pun, "
            "TIDAK menulis apa pun ke manifes, dan TIDAK menulis ulang angka semesta "
            "839.842.134 (aturan 29)"
        ),
        "catatan_penggugur": (
            "parser_terbukti == false berarti pembaca modul ini tidak terbukti melihat "
            "kehidupan pada pasar yang pasti hidup, sehingga SELURUH klaim kematian di "
            "laporan ini batal (aturan 50); cacah_gagal_checksum != 0 berarti berkas "
            "yang diukur tidak terbukti asli; cacah_simbol_bulan_tak_terukur > 0 "
            "berarti penyebut menyusut dan tidak boleh diam-diam dibaca sebagai 456; "
            "galat_kohort != null berarti daftar anggota tidak terbaca (aturan 24)"
        ),
        "catatan_penyebut": (
            "penyebut_penuh mencacah simbol-bulan TERUKUR, bukan yang diminta; "
            "penyebut_tanpa_mati adalah penyebut kedua yang diwajibkan ADR-A008 "
            "Keputusan 3 dan diterbitkan walau selisihnya nol; bila "
            "penyebut_tanpa_mati_kosong true, nol itu DILARANG dipakai membagi "
            "(aturan 30, 41)"
        ),
        "catatan_satuan": (
            "cacah_simbol_bulan_*, cacah_mati, cacah_sepi, cacah_hidup, dan kedua "
            "penyebut bersatuan SIMBOL-BULAN; lilin_* bersatuan LILIN; bagian_mati "
            "adalah BAGIAN antara 0 dan 1, bukan persen (aturan 47)"
        ),
        "catatan_rentang": (
            "yang diukur hanya jendela bulan_mulai..bulan_akhir pada anggota kohort "
            "funding 2025-07. Tidak ada pernyataan apa pun tentang bulan di luar "
            "jendela itu, tentang 19.598 simbol-bulan semesta, atau tentang simbol di "
            "luar kohort (aturan 20)"
        ),
    }


def main() -> int:
    laporan = jalankan(".")
    Path(KELUARAN).parent.mkdir(parents=True, exist_ok=True)
    teks = json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    Path(KELUARAN).write_text(teks, encoding="utf-8")
    ringkasan_berkas = berkas_ringkas(laporan, teks)
    Path(KELUARAN_RINGKAS).write_text(
        json.dumps(ringkasan_berkas, ensure_ascii=False, indent=2, sort_keys=True)
        + "\n",
        encoding="utf-8",
    )
    print(json.dumps(ringkasan_berkas, ensure_ascii=False, indent=2, sort_keys=True))
    r = laporan["ringkasan"]
    if (
        laporan["galat_kohort"]
        or not r["parser_terbukti"]
        or r["cacah_gagal_checksum"]
    ):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
