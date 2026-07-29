"""Sebut NAMA keenam lubang funding berbentuk TENGAH — tanpa menyentuh jaringan.

Tiga bentuk lubang funding sudah terjelaskan, satu belum. `silang_funding` V2
menerbitkan sebaran bentuk lokal atas 877 lubang yang jatuh di dalam penyebut
19.586: **awal 45, ekor 826, tengah 6, seluruh 0**. Bentuk *ekor* terjelaskan
oleh kematian pasar (lubang -> mati 96,0%); bentuk *awal* terjelaskan oleh
penerbitan funding yang menyusul penerbitan klines (33 simbol-bulan HIDUP tanpa
funding SEMUANYA berbentuk awal). Yang **tengah** tidak terjelaskan oleh
keduanya: pasar itu punya funding sebelumnya DAN punya funding sesudahnya,
namun bolong di tengah.

Enam simbol-bulan bukan angka besar, tetapi Keputusan 7 ADR-A008 tidak boleh
diambil selagi ada bentuk cacat yang belum bernama. Modul ini menyebut namanya.

## Mengapa modul BARU, bukan `silang_funding` V3

`silang_funding.py` sudah 396 baris pada V1 dan belum diukur ulang pada V2;
pagar baris 800 dan aturan 48 melarang menumpuk fungsi pada berkas yang sudah
besar. Seluruh alat yang dibutuhkan sudah ada dan sudah diuji di sana
(`baca_laporan_kehidupan`, `baca_medan_baris`, `lubang_funding`,
`bulan_per_simbol`, `bentuk_lubang_lokal`, `kendali_silang`), jadi modul ini
MEMAKAINYA, tidak menyalinnya. Definisi bentuk karena itu tetap SATU (aturan
36); tidak ada definisi kedua yang bisa diam-diam menyimpang.

**Terbukti benar oleh angka [V2]:** `ukur_baris` V4 mengukur
`silang_funding.py` V2 = **705 baris**, seri dengan `funding.py`. Bila jalur V3
ditempuh, berkas itu sudah menembus pagar 800 sekarang.

## Tidak ada unduhan

Bahannya `reports/kehidupan_arsip_<0..7>.json` dan
`reports/funding_semesta.json`, keduanya sudah di-commit. Satu job ringan.

## Uji H-A010 — dan batas yang jujur

H-A010: "arsip funding menyusul arsip klines" — funding sebuah simbol mulai
diterbitkan SESUDAH klines-nya. Ujinya di sini memakai definisi LOKAL:
`bulan_berfunding_pertama` adalah bulan klines paling awal simbol itu yang TIDAK
berlubang. H-A010 MENANG hanya bila kelima simbol pemilik 33 lubang HIDUP
(ICPUSDT, TLMUSDT, BNXUSDT, JUPUSDT, QTUMUSDT) punya
`bulan_berfunding_pertama` yang lebih besar daripada `bulan_klines_pertama`.
Satu simbol saja yang tidak, hipotesis itu gugur.

**Batasnya wajib disebut:** definisi ini tidak dapat melihat bulan funding yang
ada SEBELUM klines pertama, sebab penyebutnya adalah bulan klines. Karena itu
laporan ini juga menerbitkan `medan_per_simbol_funding_terlihat` apa adanya —
bila kelak terbukti ada medan yang memuat bulan funding pertama sesungguhnya,
uji ini wajib diulang dengan medan itu. Yang dilaporkan sekarang adalah bentuk
irisannya, bukan tanggal penerbitan arsip Binance (aturan 20).

## Perubahan V2 — menutup batas itu, dan menguji jeda LITUSDT

V1 menang pada R-223 tetapi mengakui sendiri bahwa definisinya TURUNAN. Medan
`funding_tanpa_klines` ternyata ADA di `funding_semesta.json.per_simbol` (satu
dari 10 medan) dan belum pernah dipakai. Medan itulah satu-satunya jalan di
dalam repo untuk melihat bulan funding yang mendahului klines. V2 menambah
**tiga** fungsi — `funding_tanpa_klines`, `status_rentang`, `uji_h_a011` — dan
tidak menyentuh satu pun fungsi V1.

1. **Penguji R-223.** Bila kelima simbol H-A010 punya `funding_tanpa_klines`
   KOSONG, tidak ada bulan funding sebelum klines pertama, sehingga definisi
   turunan V1 bukan hanya memadai melainkan TEPAT. Bila salah satunya berisi,
   kemenangan R-223 wajib ditinjau ulang — dan laporan ini akan menyebutnya,
   bukan menyembunyikannya. Aturan 46 ditaati: bila medannya TIDAK ADA pada
   sebuah baris, hasilnya `ada_medan` false dan `kosong_seluruhnya` TIDAK boleh
   berbunyi true.
2. **H-A011 (lahir di STATE v33).** LITUSDT kehilangan funding 2025-07..2025-11
   lalu memperolehnya kembali 2026-01, sementara klines terbit penuh dan status
   kehidupannya MATI. Bila pasar itu benar-benar diperdagangkan kembali,
   sekurang-kurangnya satu bulan pada 2026-01..2026-06 wajib berstatus HIDUP.
   Bila keenamnya MATI, H-A011 GUGUR dan yang tersisa hanyalah pernyataan
   tentang PENERBITAN arsip, bukan tentang perdagangan.

## Penggugur (aturan 24)

`selisih_lubang_tengah` membandingkan cacah yang baru dibangun dengan **6** yang
sudah diterbitkan `silang_funding` V2 pada run 30434948267. Bukan nol berarti
bahan bakunya berubah dan seluruh laporan batal (kode 2). Kendali positif
`silang_funding.kendali_silang` dipakai apa adanya: tiga simbol-bulan
berparquet terbesar wajib HIDUP dan wajib berfunding (aturan 50). V2 TIDAK
menambah penggugur: kedua uji baru boleh kalah tanpa membatalkan pengukuran,
sebab hipotesis yang gugur adalah hasil, bukan cacat.

## Praregistrasi ramalan V1 — ditulis SEBELUM run (TIDAK disunting)

- **R-221** — CI pada commit yang menambahkan `tests/test_lubang_tengah.py`
  (sasaran dinyatakan menurut aturan 56) mengumpulkan **382 butir** dengan kode
  keluar **0**. Dasar: 340 butir terverifikasi pada run 30435672616, ditambah
  **42** butir dari berkas uji baru. Keempat puluh dua nama itu ditulis
  BERNOMOR di docstring `tests/test_lubang_tengah.py` pada commit yang sama
  (aturan 57, penangkal KC-19); tidak ada `parametrize` di berkas itu, sehingga
  cacah fungsi sama dengan cacah butir. 340 + 42 = **382**. → TEPAT (run
  30436334383).
- **R-222** — `cacah_lubang_tengah` = **6** persis (`selisih_lubang_tengah` = 0)
  dan keenamnya berstatus **MATI**. → TEPAT (MATI 6, SEPI 0, HIDUP 0).
- **R-223** — H-A010 **MENANG**: `cacah_menang` = 5 dan `cacah_gugur` = 0. →
  TEPAT 5–0, dengan batas yang kini diuji V2.

## Praregistrasi ramalan V2 — ditulis SEBELUM run

- **R-228** — CI pada commit BERIKUTNYA yang menyentuh
  `tests/test_lubang_tengah.py` (aturan 56), yakni commit yang memuat V2 ini,
  mengumpulkan **396 butir** dengan kode keluar **0**. Dasar (aturan 38, 54,
  57): 382 butir terverifikasi pada run 30436915256, berkas uji ini turun dari
  42 menjadi **56** butir, dan tidak ada berkas uji lain yang disentuh, maka
  382 − 42 + 56 = **396**. Kelima puluh enam nama ditulis BERNOMOR di docstring
  berkas uji pada commit yang sama; tidak ada `parametrize` di sana.
- **R-229** — `funding_tanpa_klines` KOSONG bagi kelima simbol H-A010:
  `kosong_seluruhnya` **true**, `cacah_berisi` **0**, `cacah_tak_terukur` **0**.
  Dasar: ke-33 lubang HIDUP seluruhnya berbentuk AWAL, dan `funding.py` V6
  mencacah 87 "funding tanpa klines" atas SELURUH 787 simbol — tidak ada alasan
  memperkirakan kelima simbol ini termasuk di dalamnya. Ramalan ini GUGUR bila
  satu bulan saja terdaftar; bila itu terjadi, kemenangan R-223 wajib ditinjau
  ulang dan definisi turunan V1 dinyatakan tidak tepat.
- **R-230** — **H-A011 GUGUR**: keenam bulan LITUSDT 2026-01..2026-06 HADIR di
  penyebut kehidupan (`cacah_bulan` = 6, `terukur` true) dan `cacah_hidup` =
  **0**, sehingga `h_a011_menang` false. Dasar: sepanjang jeda funding
  2025-07..2025-11 klines LITUSDT terbit penuh secara bentuk namun statusnya
  MATI (KC-18), dan tidak ada satu pun kasus kebangkitan terukur di repo ini
  (`cacah_simbol_bangkit_dapat_diuji` = 0 pada kohort_ekor V4). Ramalan ini
  GUGUR bila ada satu bulan HIDUP — dan bila itu terjadi, tafsir
  "delisting lalu terdaftar ulang" justru MENANG, yang lebih berharga daripada
  ramalan saya yang tepat.

Aturan yang mengikat: 10, 20, 21, 22, 24, 30, 36, 41, 44, 45, 46, 47, 48, 50,
52, 53, 54, 56, 57, 58. Cacah baris berkas ini SENGAJA tidak diramalkan
(aturan 58, pilihan c): ia diukur `ukur_baris`, bukan ditaksir.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from . import kehidupan, kehidupan_arsip, silang_funding

VERSI = 2
TOTAL_PECAHAN = kehidupan_arsip.TOTAL_PECAHAN
SUMBER_FUNDING = silang_funding.SUMBER_FUNDING
KELUARAN = "reports/lubang_tengah.json"
KENDALI_CACAH = silang_funding.KENDALI_CACAH
MEDAN_LILIN = silang_funding.MEDAN_LILIN

# Diterbitkan silang_funding V2 (run 30434948267): sebaran_bentuk_semua_lubang
# = {awal 45, ekor 826, tengah 6, seluruh 0}. Dipakai sebagai PENGGUGUR.
TENGAH_TERCATAT = 6

# Pemilik ke-33 lubang pada simbol-bulan HIDUP, menurut daftar terbitan V2.
SIMBOL_H_A010 = ["BNXUSDT", "ICPUSDT", "JUPUSDT", "QTUMUSDT", "TLMUSDT"]

# Pemilik keenam lubang TENGAH, menurut laporan V1 run 30436334434.
SIMBOL_TENGAH_TERCATAT = ["BTCSTUSDT", "LITUSDT"]

# H-A011: funding LITUSDT berhenti 2025-06 lalu kembali 2026-01.
SIMBOL_H_A011 = "LITUSDT"
RENTANG_H_A011 = ("2026-01", "2026-06")
MEDAN_FUNDING_TANPA_KLINES = "funding_tanpa_klines"

BERKAS_DICAP = [
    "kehidupan.py",
    "kehidupan_arsip.py",
    "lubang_tengah.py",
    "silang_funding.py",
]

Kunci = Tuple[str, str]


def nama_keluaran() -> str:
    return KELUARAN


def sidik_kode() -> str:
    """Aturan 22: cap setiap berkas yang ikut menentukan angka ini."""
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(BERKAS_DICAP):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def medan_per_simbol(funding: Dict[str, Any]) -> Tuple[List[str], int]:
    """Medan yang benar-benar ada pada `per_simbol` — dilapor, tidak ditebak."""
    terlihat: Set[str] = set()
    cacah = 0
    for baris in funding.get("per_simbol") or []:
        cacah += 1
        terlihat.update(str(m) for m in baris.keys())
    return sorted(terlihat), cacah


def funding_tanpa_klines(
    funding: Dict[str, Any], daftar: Optional[List[str]] = None
) -> Dict[str, Any]:
    """Bulan funding yang MENDAHULUI klines, bagi simbol yang diminta.

    Ini penguji batas R-223. Aturan 46: bila medannya tidak ada pada sebuah
    baris, hasilnya `ada_medan` false dan `kosong_seluruhnya` TIDAK berbunyi
    true — tidak adanya medan bukan bukti tidak adanya bulan.
    """
    minta = sorted(daftar if daftar is not None else SIMBOL_H_A010)
    per: Dict[str, Dict[str, Any]] = {}
    for baris in funding.get("per_simbol") or []:
        per[str(baris.get("simbol"))] = baris
    keluar: List[Dict[str, Any]] = []
    berisi = 0
    tak_terukur = 0
    for s in minta:
        baris = per.get(s)
        ada_medan = bool(baris) and MEDAN_FUNDING_TANPA_KLINES in baris
        nilai = (baris or {}).get(MEDAN_FUNDING_TANPA_KLINES)
        bulan = sorted(str(b) for b in nilai) if isinstance(nilai, list) else []
        if not ada_medan:
            tak_terukur += 1
        elif bulan:
            berisi += 1
        keluar.append(
            {
                "simbol": s,
                "ada_di_per_simbol": baris is not None,
                "ada_medan": ada_medan,
                "cacah_bulan": len(bulan),
                "bulan": bulan,
            }
        )
    return {
        "baris": keluar,
        "cacah_simbol": len(keluar),
        "cacah_berisi": berisi,
        "cacah_tak_terukur": tak_terukur,
        "kosong_seluruhnya": bool(keluar) and tak_terukur == 0 and berisi == 0,
    }


def _berlubang_per_simbol(lubang: Set[Kunci]) -> Dict[str, Set[str]]:
    keluar: Dict[str, Set[str]] = {}
    for simbol, bulan in lubang:
        keluar.setdefault(str(simbol), set()).add(str(bulan))
    return keluar


def bulan_berfunding(bulan_urut: List[str], bulan_berlubang: Set[str]) -> List[str]:
    """Bulan klines yang PUNYA funding, urut naik."""
    return [b for b in sorted(bulan_urut) if b not in bulan_berlubang]


def tetangga_berfunding(
    bulan_urut: List[str], bulan_berlubang: Set[str], bulan: str
) -> Tuple[Optional[str], Optional[str]]:
    """Bulan berfunding terdekat sebelum dan sesudah sebuah bulan.

    Ujung riwayat menghasilkan null, bukan bulan palsu (aturan 46).
    """
    berfunding = bulan_berfunding(bulan_urut, bulan_berlubang)
    sebelum = [b for b in berfunding if b < bulan]
    sesudah = [b for b in berfunding if b > bulan]
    return (sebelum[-1] if sebelum else None, sesudah[0] if sesudah else None)


def panjang_rentetan(
    bulan_urut: List[str], bulan_berlubang: Set[str], bulan: str
) -> int:
    """Panjang rentetan lubang berurutan yang memuat `bulan`; 0 bila bukan lubang."""
    urut = sorted(bulan_urut)
    if bulan not in urut or bulan not in bulan_berlubang:
        return 0
    i = urut.index(bulan)
    kiri = kanan = i
    while kiri - 1 >= 0 and urut[kiri - 1] in bulan_berlubang:
        kiri -= 1
    while kanan + 1 < len(urut) and urut[kanan + 1] in bulan_berlubang:
        kanan += 1
    return kanan - kiri + 1


def daftar_lubang_tengah(
    status: Dict[Kunci, str],
    byte_parquet: Dict[Kunci, int],
    lubang: Set[Kunci],
    lilin: Optional[Dict[Kunci, Any]] = None,
) -> List[Dict[str, Any]]:
    """Daftar bernama lubang berbentuk TENGAH, memakai definisi silang_funding."""
    lilin = lilin or {}
    per_simbol = silang_funding.bulan_per_simbol(status)
    berlubang = _berlubang_per_simbol(lubang)
    baris: List[Dict[str, Any]] = []
    for k in sorted(lubang & set(status)):
        simbol, bulan = k
        urut = per_simbol.get(simbol, [])
        bl = berlubang.get(simbol, set())
        if silang_funding.bentuk_lubang_lokal(urut, bl, bulan) != "tengah":
            continue
        sebelum, sesudah = tetangga_berfunding(urut, bl, bulan)
        baris.append(
            {
                "simbol": simbol,
                "bulan": bulan,
                "status": status.get(k),
                "bentuk_lubang_lokal": "tengah",
                "bulan_berfunding_sebelum": sebelum,
                "bulan_berfunding_sesudah": sesudah,
                "panjang_rentetan_lubang": panjang_rentetan(urut, bl, bulan),
                "byte_parquet": int(byte_parquet.get(k) or 0),
                "cacah_lilin": lilin.get(k),
                "cacah_bulan_klines_simbol": len(urut),
                "cacah_lubang_simbol": len(bl & set(urut)),
                "bulan_klines_pertama": urut[0] if urut else None,
                "bulan_klines_terakhir": urut[-1] if urut else None,
            }
        )
    return baris


def sebaran_status(baris: List[Dict[str, Any]]) -> Dict[str, int]:
    """Cacah status; keempat kelas dilapor walau nol."""
    keluar: Dict[str, int] = {
        st: 0
        for st in (
            kehidupan.STATUS_MATI,
            kehidupan.STATUS_SEPI,
            kehidupan.STATUS_HIDUP,
            kehidupan.STATUS_TAK_TERUKUR,
        )
    }
    for r in baris:
        nama = str(r.get("status"))
        keluar[nama] = keluar.get(nama, 0) + 1
    return keluar


def status_rentang(
    status: Dict[Kunci, str], simbol: str, mulai: str, sampai: str
) -> List[Dict[str, Any]]:
    """Baris status sebuah simbol pada rentang bulan tertutup [mulai, sampai]."""
    baris: List[Dict[str, Any]] = []
    for (s, b), st in sorted(status.items()):
        if str(s) != simbol:
            continue
        if not (mulai <= str(b) <= sampai):
            continue
        baris.append({"simbol": simbol, "bulan": str(b), "status": st})
    return baris


def uji_h_a011(
    status: Dict[Kunci, str],
    simbol: Optional[str] = None,
    rentang: Optional[Tuple[str, str]] = None,
) -> Dict[str, Any]:
    """H-A011: kembalinya funding menandai pasar yang diperdagangkan ulang.

    MENANG hanya bila sekurang-kurangnya satu bulan pada rentang itu HIDUP.
    Rentang yang kosong menghasilkan `terukur` false, BUKAN kekalahan yang
    diklaim sebagai pengukuran (aturan 41, 46).
    """
    nama = simbol or SIMBOL_H_A011
    mulai, sampai = rentang or RENTANG_H_A011
    baris = status_rentang(status, nama, mulai, sampai)
    sebaran = sebaran_status(baris)
    hidup = int(sebaran.get(kehidupan.STATUS_HIDUP) or 0)
    return {
        "simbol": nama,
        "mulai": mulai,
        "sampai": sampai,
        "baris": baris,
        "cacah_bulan": len(baris),
        "sebaran_status": sebaran,
        "cacah_hidup": hidup,
        "terukur": bool(baris),
        "menang": bool(baris) and hidup > 0,
    }


def kode_keluar(ringkasan: Dict[str, Any]) -> int:
    """Kode 2 bila laporan ini tidak berhak diklaim sebagai pengukuran."""
    if not ringkasan.get("sidik_seragam"):
        return 2
    if int(ringkasan.get("cacah_laporan_dibaca") or 0) != int(
        ringkasan.get("total_pecahan") or TOTAL_PECAHAN
    ):
        return 2
    if int(ringkasan.get("cacah_kunci_ganda") or 0) > 0:
        return 2
    if not ringkasan.get("kendali_sah"):
        return 2
    if int(ringkasan.get("selisih_lubang_tengah") or 0) != 0:
        return 2
    return 0


def jalankan(akar: str = ".", total: int = TOTAL_PECAHAN) -> Dict[str, Any]:
    status, byte_parquet, meta = silang_funding.baca_laporan_kehidupan(
        akar=akar, total=total
    )
    lilin, meta_lilin = silang_funding.baca_medan_baris(
        akar=akar, total=total, medan=MEDAN_LILIN
    )
    mentah = (Path(akar) / SUMBER_FUNDING).read_bytes()
    funding = json.loads(mentah.decode("utf-8"))

    lubang, meta_lubang = silang_funding.lubang_funding(funding)
    medan_funding, cacah_per_simbol = medan_per_simbol(funding)
    tengah = daftar_lubang_tengah(status, byte_parquet, lubang, lilin)
    h_a010 = uji_h_a010(status, lubang)
    tanpa_klines = funding_tanpa_klines(funding)
    h_a011 = uji_h_a011(status)
    kendali = silang_funding.kendali_silang(byte_parquet, status, lubang)

    ringkasan: Dict[str, Any] = {
        "penyebut_kehidupan": len(status),
        "cacah_lubang_tengah": len(tengah),
        "selisih_lubang_tengah": len(tengah) - TENGAH_TERCATAT,
        "sebaran_status_lubang_tengah": sebaran_status(tengah),
        "medan_per_simbol_funding_terlihat": medan_funding,
        "cacah_per_simbol_funding": cacah_per_simbol,
        "h_a010_menang": h_a010["menang"],
        "h_a010_cacah_menang": h_a010["cacah_menang"],
        "h_a010_cacah_gugur": h_a010["cacah_gugur"],
        "h_a010_cacah_tak_terukur": h_a010["cacah_tak_terukur"],
        "h_a010_funding_tanpa_klines_kosong": tanpa_klines["kosong_seluruhnya"],
        "h_a010_cacah_simbol_berisi": tanpa_klines["cacah_berisi"],
        "h_a010_cacah_simbol_tak_terukur": tanpa_klines["cacah_tak_terukur"],
        "h_a011_menang": h_a011["menang"],
        "h_a011_terukur": h_a011["terukur"],
        "h_a011_cacah_bulan": h_a011["cacah_bulan"],
        "h_a011_cacah_hidup": h_a011["cacah_hidup"],
        "kendali": kendali,
        "kendali_sah": silang_funding.kendali_sah(kendali),
    }
    ringkasan.update(meta)
    ringkasan.update(meta_lilin)
    ringkasan.update(meta_lubang)

    return {
        "bukan_bukti": False,
        "versi_lubang_tengah": VERSI,
        "sidik_kode": sidik_kode(),
        "sidik_kode_silang_funding": silang_funding.sidik_kode(),
        "sidik_data_funding": hashlib.sha256(mentah).hexdigest(),
        "versi_funding": funding.get("versi_funding"),
        "sumber": [SUMBER_FUNDING]
        + [kehidupan_arsip.nama_keluaran(i) for i in range(total)],
        "definisi": {
            "bentuk_lubang_lokal": (
                "dipakai apa adanya dari silang_funding.bentuk_lubang_lokal: "
                "tengah berarti ada bulan klines berfunding sebelum DAN sesudah "
                "lubang itu; definisinya SATU, tidak disalin ulang (aturan 36)"
            ),
            "bulan_berfunding_pertama": (
                "bulan klines paling awal simbol itu yang TIDAK berlubang; ini "
                "BUKAN tanggal penerbitan arsip funding Binance"
            ),
            "h_a010_menang": (
                "benar hanya bila SELURUH simbol yang diuji punya "
                "bulan_berfunding_pertama lebih besar daripada "
                "bulan_klines_pertama"
            ),
            "funding_tanpa_klines": (
                "medan terbitan funding.py V6 apa adanya: bulan yang punya "
                "funding namun tidak punya klines; kosong pada kelima simbol "
                "H-A010 berarti definisi bulan_berfunding_pertama TEPAT, "
                "berisi berarti kemenangan R-223 wajib ditinjau ulang"
            ),
            "h_a011_menang": (
                "benar hanya bila sekurang-kurangnya SATU bulan pada rentang "
                "yang diuji berstatus HIDUP; rentang kosong berbunyi "
                "terukur false, bukan gugur (aturan 41, 46)"
            ),
        },
        "baris_lubang_tengah": tengah,
        "h_a010": h_a010,
        "funding_tanpa_klines": tanpa_klines,
        "h_a011": h_a011,
        "ringkasan": ringkasan,
        "catatan_batas_h_a010": (
            "penyebut uji ini adalah bulan KLINES, sehingga bulan funding yang "
            "ada sebelum klines pertama tidak terlihat; V2 memeriksa batas itu "
            "lewat medan funding_tanpa_klines, dan bila medan itu berisi maka "
            "uji H-A010 wajib diulang dengan medan itu (aturan 20)"
        ),
        "catatan_batas_h_a011": (
            "status HIDUP pada 2026-01..2026-06 tidak akan membuktikan SEBAB "
            "kembalinya funding, hanya bahwa perdagangan dan penerbitan pulih "
            "bersama; sebaliknya status MATI seluruhnya menunjukkan penerbitan "
            "funding dapat pulih tanpa perdagangan (aturan 10)"
        ),
        "catatan_tafsir": (
            "lubang tengah yang berdampingan dengan bulan berfunding TIDAK "
            "membuktikan sebab apa pun; ia hanya menunjukkan bahwa ketiadaan "
            "funding di bulan itu tidak dapat dijelaskan oleh awal maupun akhir "
            "riwayat simbol (aturan 10)"
        ),
        "catatan_penggugur": (
            "sidik_seragam false, laporan pecahan kurang, kunci ganda, "
            "kendali_sah false, atau selisih_lubang_tengah bukan nol "
            "membatalkan seluruh angka (aturan 24); H-A010 dan H-A011 yang "
            "gugur BUKAN penggugur — hipotesis yang kalah adalah hasil"
        ),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def uji_h_a010(
    status: Dict[Kunci, str],
    lubang: Set[Kunci],
    simbol: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """H-A010: funding menyusul klines. MENANG hanya bila SEMUA simbol setuju."""
    daftar = sorted(simbol if simbol is not None else SIMBOL_H_A010)
    per_simbol = silang_funding.bulan_per_simbol(status)
    berlubang = _berlubang_per_simbol(lubang)
    baris: List[Dict[str, Any]] = []
    menang = gugur = tak_terukur = 0
    for s in daftar:
        urut = per_simbol.get(s, [])
        berfunding = bulan_berfunding(urut, berlubang.get(s, set())) if urut else []
        pertama = berfunding[0] if berfunding else None
        if not urut or pertama is None:
            menyusul: Optional[bool] = None
            tak_terukur += 1
        else:
            menyusul = pertama > urut[0]
            if menyusul:
                menang += 1
            else:
                gugur += 1
        baris.append(
            {
                "simbol": s,
                "bulan_klines_pertama": urut[0] if urut else None,
                "bulan_berfunding_pertama": pertama,
                "funding_menyusul": menyusul,
                "cacah_bulan_klines_simbol": len(urut),
                "cacah_lubang_simbol": len(berlubang.get(s, set()) & set(urut)),
            }
        )
    return {
        "baris": baris,
        "cacah_simbol": len(baris),
        "cacah_menang": menang,
        "cacah_gugur": gugur,
        "cacah_tak_terukur": tak_terukur,
        "menang": bool(baris) and menang == len(baris),
    }


def main() -> int:
    laporan = jalankan()
    Path(KELUARAN).parent.mkdir(parents=True, exist_ok=True)
    teks = json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    Path(KELUARAN).write_text(teks, encoding="utf-8")
    print(teks)
    return kode_keluar(laporan["ringkasan"])


if __name__ == "__main__":
    raise SystemExit(main())
