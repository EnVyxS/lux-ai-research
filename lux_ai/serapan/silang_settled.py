"""Uji H-A015 — bulan `...SETTLED` sebagai batas antara dua kontrak.

Jurnal 112 menemukan, dari medan `h_a010.baris` laporan `lubang_tengah.json` V2,
bahwa bulan berfunding PERTAMA nama dasar sama PERSIS dengan bulan `...SETTLED`
TERAKHIR pasangannya pada tiga simbol: BNXUSDT 2023-02, ICPUSDT 2022-09, dan
TLMUSDT 2023-03. Ketiganya justru ketiga pasangan yang berkohort banyak bulan
(6, 9, 9). Dua simbol H-A010 sisanya (JUPUSDT, QTUMUSDT) tidak berpasangan
SETTLED dan lubangnya hanya satu bulan.

H-A015: bulan `...SETTLED` menandai batas antara dua kontrak pada nama dasar
yang sama; ia jatuh pada atau tepat sebelum bulan berfunding pertama kontrak
berikutnya. Modul ini mengujinya atas SELURUH 15 pasangan, bukan atas tiga yang
melahirkan dugaannya.

## Mengapa modul ini MENGIMPOR, bukan memecah (preseden jurnal 111 §5)

`silang_funding.py` sudah 705 baris dan `sidik_kode`-nya tertanam di banyak
laporan yang sudah di-commit. Memindahkan fungsi keluar darinya akan mengubah
sidik itu dan membatalkan pembandingan dengan laporan lama. Modul ini karena itu
mengimpor `baca_laporan_kehidupan`, `lubang_funding`, `bulan_per_simbol`,
`_berlubang_per_simbol`, `kendali_silang`, dan `kendali_sah` apa adanya, dan
tidak menyalin satu pun definisinya (aturan 36).

## Kesetaraan definisi TIDAK diasumsikan — ia diuji (KC-9, aturan 24)

`bulan_berfunding_pertama` yang saya pakai di sini dihitung LOKAL: bulan klines
pertama simbol yang TIDAK berlubang funding. `lubang_tengah.py` V2 sudah
menerbitkan angka yang seharusnya setara bagi kelima simbol H-A010. Alih-alih
menganggap keduanya sama, modul ini membandingkannya sebagai KENDALI:
`selisih_kendali_funding_pertama` wajib 0, dan bila bukan nol kode keluar 2 dan
seluruh angka batal. Menyamakan dua definisi tanpa memeriksanya adalah cacat yang
sudah pernah terjadi (KC-9).

Angka terbitan yang dipakai sebagai kendali diambil dari `lubang_tengah.json` V2
runner `e2a37ff7` (run 30440471508): BNXUSDT 2023-02, ICPUSDT 2022-09, JUPUSDT
2024-02, QTUMUSDT 2020-03, TLMUSDT 2023-03.

## Yang TIDAK boleh disimpulkan

Kecocokan bulan membuktikan PENAMAAN kontrak, bukan perdagangan (KC-18).
Sekalipun ke-15 pasangan cocok, laporan ini tidak berhak menyimpulkan bahwa
kontrak lama diperdagangkan sampai bulan itu; yang terbukti hanyalah bahwa
penerbitan funding di bawah nama dasar mulai pada bulan itu (aturan 10).

Penyebutnya juga wajib disebut: 19.586 simbol-bulan yang LOLOS gerbang, bukan
19.598 (aturan 30, 44). Bulan SETTLED sendiri TIDAK ada di penyebut itu — 15 nama
SETTLED tidak satu pun masuk penyebut, jadi bulan SETTLED di sini adalah TETAPAN
terbitan `bulan_settled.json`, bukan hasil pembacaan ulang.

## Praregistrasi ramalan — ditulis SEBELUM run

- **R-286** (sudah dipraregistrasi di jurnal 112 §10, disalin apa adanya):
  1. cacah pasangan yang bulan berfunding pertamanya SAMA PERSIS dengan bulan
     SETTLED terakhirnya adalah **3 atau 4**, dan ketiga yang cocok wajib memuat
     BNXUSDT, ICPUSDT, TLMUSDT. GUGUR bila cacah cocok >= 5 atau <= 2.
  2. bagi sekurang-kurangnya **10 dari 12** pasangan bersatu-bulan, funding
     pertama nama dasar jatuh LEBIH AWAL daripada bulan SETTLED-nya.
  3. ketiga pasangan berkohort banyak punya lubang funding **> 10** (19/16/20),
     dan sekurang-kurangnya 10 dari 12 sisanya punya **< 10** lubang.
- **R-287** — CI pada commit yang menyentuh `tests/test_silang_settled.py`
  mengumpulkan **662 butir** dengan kode keluar **0**. Dasar (aturan 54, 56, 57;
  dicacah dari berkas uji yang sudah SELESAI ditulis): 638 butir terverifikasi
  pada run terakhir yang tercatat di `reports/ci_terakhir.json`, ditambah 24
  fungsi `def test_` baru tanpa satu pun `parametrize`. 638 + 24 = 662. Satuan:
  BUTIR yang dikumpulkan pytest.

Aturan yang mengikat: 10, 16, 20, 21, 22, 24, 30, 36, 44, 45, 46, 50, 52, 53,
54, 56, 57, 70, 72, 73, 74.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from . import kehidupan_arsip, silang_funding

VERSI = 1
TOTAL_PECAHAN = kehidupan_arsip.TOTAL_PECAHAN
SUMBER_FUNDING = silang_funding.SUMBER_FUNDING
KELUARAN = "reports/silang_settled.json"
PENYEBUT_TERCATAT = 19586

# Tetapan terbitan reports/bulan_settled.json (jurnal 107): bulan SETTLED
# TERAKHIR bagi tiap nama dasar. 15 pasangan, tidak lebih dan tidak kurang.
PASANGAN_SETTLED: Dict[str, str] = {
    "AERGOUSDT": "2025-04",
    "AIAUSDT": "2026-01",
    "BDXNUSDT": "2026-04",
    "BNXUSDT": "2023-02",
    "CTKUSDT": "2025-04",
    "CVCUSDT": "2025-05",
    "CVXUSDT": "2025-07",
    "ICPUSDT": "2022-09",
    "LITUSDT": "2025-12",
    "MAVIAUSDT": "2025-03",
    "MINAUSDT": "2023-02",
    "PUMPUSDT": "2025-07",
    "SLPUSDT": "2025-07",
    "SXPUSDT": "2026-06",
    "TLMUSDT": "2023-03",
}

# Pasangan berkohort banyak bulan (6, 9, 9); sisanya bersatu-bulan.
KOHORT_BANYAK: Tuple[str, ...] = ("BNXUSDT", "ICPUSDT", "TLMUSDT")

# Kendali kesetaraan definisi: terbitan lubang_tengah.json V2 runner e2a37ff7.
FUNDING_PERTAMA_TERBITAN: Dict[str, str] = {
    "BNXUSDT": "2023-02",
    "ICPUSDT": "2022-09",
    "JUPUSDT": "2024-02",
    "QTUMUSDT": "2020-03",
    "TLMUSDT": "2023-03",
}

# Pita ramalan R-286, ditulis sebagai TETAPAN agar tidak bergeser diam-diam.
R286_COCOK_MIN = 3
R286_COCOK_MAKS = 4
R286_LEBIH_AWAL_MIN = 10
R286_LUBANG_BANYAK_MIN = 10
R286_SATU_BULAN_KURANG_MIN = 10

SAMA = "sama"
LEBIH_AWAL = "lebih_awal"
LEBIH_LAMBAT = "lebih_lambat"
TAK_TERUKUR = "tak_terukur"
ARAH = (SAMA, LEBIH_AWAL, LEBIH_LAMBAT, TAK_TERUKUR)

BERKAS_DICAP = [
    "kehidupan.py",
    "kehidupan_arsip.py",
    "silang_funding.py",
    "silang_settled.py",
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


def bulan_berfunding_pertama_lokal(
    bulan_urut: List[str], bulan_berlubang: Set[str]
) -> Optional[str]:
    """Bulan klines pertama yang TIDAK berlubang funding.

    DEFINISI LOKAL, dinyatakan tersurat: tanpa bulan klines sama sekali, atau
    bila seluruh bulannya berlubang, hasilnya None dan BUKAN nol (aturan 46).
    """
    for bulan in sorted(str(b) for b in bulan_urut):
        if bulan not in bulan_berlubang:
            return bulan
    return None


def arah(funding_pertama: Optional[str], bulan_settled: Optional[str]) -> str:
    """Arah bulan funding pertama terhadap bulan SETTLED terakhir."""
    if not funding_pertama or not bulan_settled:
        return TAK_TERUKUR
    if funding_pertama == bulan_settled:
        return SAMA
    return LEBIH_AWAL if funding_pertama < bulan_settled else LEBIH_LAMBAT


def baris_pasangan(
    status: Dict[Kunci, str],
    lubang: Set[Kunci],
    pasangan: Optional[Dict[str, str]] = None,
) -> List[Dict[str, Any]]:
    """Satu baris per pasangan SETTLED; pasangan tanpa data TIDAK dibuang."""
    pasangan = dict(pasangan if pasangan is not None else PASANGAN_SETTLED)
    per_simbol = silang_funding.bulan_per_simbol(status)
    berlubang = silang_funding._berlubang_per_simbol(lubang)
    baris: List[Dict[str, Any]] = []
    for simbol in sorted(pasangan):
        urut = per_simbol.get(simbol, [])
        bl = berlubang.get(simbol, set())
        pertama = bulan_berfunding_pertama_lokal(urut, bl)
        bulan_settled = pasangan[simbol]
        baris.append(
            {
                "simbol": simbol,
                "bulan_settled_terakhir": bulan_settled,
                "cacah_bulan_klines": len(urut),
                "bulan_klines_pertama": urut[0] if urut else None,
                "bulan_klines_terakhir": urut[-1] if urut else None,
                "bulan_berfunding_pertama": pertama,
                "cacah_lubang": len(bl & set(urut)),
                "arah": arah(pertama, bulan_settled),
                "kohort_banyak": simbol in KOHORT_BANYAK,
            }
        )
    return baris


def sebaran_arah(baris: List[Dict[str, Any]]) -> Dict[str, int]:
    """Keempat kelas arah dilapor walau nol (aturan 45)."""
    keluar: Dict[str, int] = {a: 0 for a in ARAH}
    for r in baris:
        nama = str(r.get("arah"))
        keluar[nama] = keluar.get(nama, 0) + 1
    return keluar


def kendali_funding_pertama(
    status: Dict[Kunci, str],
    lubang: Set[Kunci],
    terbitan: Optional[Dict[str, str]] = None,
) -> Tuple[List[Dict[str, Any]], int]:
    """Bandingkan definisi LOKAL dengan angka terbitan lubang_tengah V2.

    Selisih bukan nol berarti kedua definisi TIDAK setara; itu penggugur, dan
    bukan sesuatu yang boleh dijelaskan belakangan (KC-9, aturan 24).
    """
    terbitan = dict(terbitan if terbitan is not None else FUNDING_PERTAMA_TERBITAN)
    per_simbol = silang_funding.bulan_per_simbol(status)
    berlubang = silang_funding._berlubang_per_simbol(lubang)
    baris: List[Dict[str, Any]] = []
    selisih = 0
    for simbol in sorted(terbitan):
        lokal = bulan_berfunding_pertama_lokal(
            per_simbol.get(simbol, []), berlubang.get(simbol, set())
        )
        cocok = lokal == terbitan[simbol]
        if not cocok:
            selisih += 1
        baris.append(
            {
                "simbol": simbol,
                "terbitan": terbitan[simbol],
                "lokal": lokal,
                "cocok": cocok,
            }
        )
    return baris, selisih


def uji_h_a015(baris: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Ketiga butir R-286, masing-masing dengan penyebutnya sendiri."""
    cocok = sorted(str(r.get("simbol")) for r in baris if r.get("arah") == SAMA)
    kohort = [r for r in baris if r.get("kohort_banyak")]
    satu_bulan = [r for r in baris if not r.get("kohort_banyak")]
    kohort_cocok = bool(kohort) and all(r.get("arah") == SAMA for r in kohort)
    lebih_awal = [r for r in satu_bulan if r.get("arah") == LEBIH_AWAL]
    kohort_banyak_lubang = [
        r for r in kohort if int(r.get("cacah_lubang") or 0) > R286_LUBANG_BANYAK_MIN
    ]
    satu_bulan_sedikit = [
        r
        for r in satu_bulan
        if int(r.get("cacah_lubang") or 0) < R286_LUBANG_BANYAK_MIN
    ]
    butir_1 = {
        "cacah_cocok": len(cocok),
        "simbol_cocok": cocok,
        "kohort_banyak_seluruhnya_cocok": kohort_cocok,
        "pita": [R286_COCOK_MIN, R286_COCOK_MAKS],
        "menang": (R286_COCOK_MIN <= len(cocok) <= R286_COCOK_MAKS) and kohort_cocok,
    }
    butir_2 = {
        "penyebut": len(satu_bulan),
        "cacah_lebih_awal": len(lebih_awal),
        "ambang": R286_LEBIH_AWAL_MIN,
        "menang": len(lebih_awal) >= R286_LEBIH_AWAL_MIN,
    }
    butir_3 = {
        "penyebut_kohort": len(kohort),
        "cacah_kohort_lubang_lebih_dari_10": len(kohort_banyak_lubang),
        "penyebut_satu_bulan": len(satu_bulan),
        "cacah_satu_bulan_lubang_kurang_dari_10": len(satu_bulan_sedikit),
        "menang": len(kohort_banyak_lubang) == len(kohort)
        and len(satu_bulan_sedikit) >= R286_SATU_BULAN_KURANG_MIN,
    }
    return {
        "butir_1": butir_1,
        "butir_2": butir_2,
        "butir_3": butir_3,
        "penggugur_menyala": not butir_1["menang"],
        "h_a015_menang": bool(
            butir_1["menang"] and butir_2["menang"] and butir_3["menang"]
        ),
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
    for medan in ("selisih_penyebut", "selisih_kendali_funding_pertama"):
        if int(ringkasan.get(medan) or 0) != 0:
            return 2
    if int(ringkasan.get("cacah_pasangan") or 0) != len(PASANGAN_SETTLED):
        return 2
    return 0


def jalankan(akar: str = ".", total: int = TOTAL_PECAHAN) -> Dict[str, Any]:
    status, byte_parquet, meta = silang_funding.baca_laporan_kehidupan(
        akar=akar, total=total
    )
    mentah = (Path(akar) / SUMBER_FUNDING).read_bytes()
    funding = json.loads(mentah.decode("utf-8"))
    lubang, meta_lubang = silang_funding.lubang_funding(funding)

    baris = baris_pasangan(status, lubang)
    kendali = silang_funding.kendali_silang(byte_parquet, status, lubang)
    kendali_definisi, selisih_definisi = kendali_funding_pertama(status, lubang)
    uji = uji_h_a015(baris)

    ringkasan: Dict[str, Any] = {
        "penyebut_kehidupan": len(status),
        "selisih_penyebut": len(status) - PENYEBUT_TERCATAT,
        "cacah_pasangan": len(baris),
        "sebaran_arah": sebaran_arah(baris),
        "kendali": kendali,
        "kendali_sah": silang_funding.kendali_sah(kendali),
        "kendali_funding_pertama": kendali_definisi,
        "selisih_kendali_funding_pertama": selisih_definisi,
        "uji_h_a015": uji,
    }
    ringkasan.update(meta)
    ringkasan.update(meta_lubang)

    return {
        "bukan_bukti": False,
        "versi_silang_settled": VERSI,
        "sidik_kode": sidik_kode(),
        "sidik_kode_silang_funding": silang_funding.sidik_kode(),
        "sidik_data_funding": hashlib.sha256(mentah).hexdigest(),
        "sidik_kode_funding": funding.get("sidik_kode"),
        "versi_funding": funding.get("versi_funding"),
        "sumber": [SUMBER_FUNDING]
        + [kehidupan_arsip.nama_keluaran(i) for i in range(total)],
        "definisi": {
            "bulan_berfunding_pertama": (
                "bulan klines pertama simbol yang TIDAK berlubang funding; "
                "DEFINISI LOKAL, kesetaraannya dengan terbitan lubang_tengah "
                "V2 diuji sebagai kendali, bukan diasumsikan (KC-9)"
            ),
            "bulan_settled_terakhir": (
                "TETAPAN terbitan reports/bulan_settled.json; 15 nama SETTLED "
                "tidak satu pun ada di penyebut 19.586, jadi bulan ini tidak "
                "dibaca ulang di sini"
            ),
            "kohort_banyak": "pasangan berkohort 6, 9, 9 bulan: BNX, ICP, TLM",
        },
        "baris": baris,
        "ringkasan": ringkasan,
        "catatan_tafsir": (
            "kecocokan bulan membuktikan PENAMAAN kontrak, bukan perdagangan "
            "(KC-18); sekalipun seluruh pasangan cocok, laporan ini tidak "
            "berhak menyimpulkan kontrak lama masih diperdagangkan (aturan 10)"
        ),
        "catatan_penggugur": (
            "sidik_seragam false, laporan pecahan kurang, kunci ganda, "
            "kendali_sah false, selisih_penyebut bukan nol, "
            "selisih_kendali_funding_pertama bukan nol, atau cacah_pasangan "
            "bukan 15 membatalkan seluruh angka (aturan 24)"
        ),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def main() -> int:
    laporan = jalankan()
    teks = json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    Path(KELUARAN).parent.mkdir(parents=True, exist_ok=True)
    Path(KELUARAN).write_text(teks, encoding="utf-8")
    print(teks)
    return kode_keluar(laporan["ringkasan"])


if __name__ == "__main__":
    raise SystemExit(main())
