"""Ukur SISA defisit lilin pada baris bukan-pertama di luar baris MATI tak penuh.

ADR-A017 kep. 10 menetapkan pertanyaan terbuka nomor satu sesudah R-310:
**sisa 712.925 lilin**. Angka itu lahir dari pengurangan
808.162 (defisit bukan-pertama) - 95.237 (defisit kesembilan baris MATI tak penuh).
Sampai sekarang tidak diketahui berapa BARIS yang menanggungnya, apalagi baris mana.

Modul ini menjawab bentuk sebarannya, bukan sebabnya.

## Batas yang wajib disebut di muka

- Laporan kehidupan menyimpan CACAH lilin, bukan HARGA. Dugaan "harga beku",
  "lilin datar", atau "jeda pemeliharaan bursa" TIDAK dapat diuji di sini dan
  DILARANG disimpulkan dari laporan ini.
- Besar berkas tetap DILARANG dipakai sebagai detektor status ke arah mana pun
  (ADR-A015 kep. 5, ditegaskan ulang ADR-A017). Modul ini tidak menyentuh byte
  sama sekali kecuali untuk kendali positif BTCUSDT.
- Nama modul sengaja `sisa_defisit`, bukan `lubang_hidup`, `hari_hilang`, atau
  `jeda_bursa`. Ketiga nama itu DITOLAK karena masing-masing sudah menyiratkan
  sebab yang belum diukur — pelajaran `byte_kecil` dan `lubang_tengah`.

## Penyebut kerja, ditulis SEBELUM pengukuran

Baris bukan-pertama yang berstatus BUKAN MATI. Alasannya tersurat:

- baris pertama dikeluarkan karena defisitnya sudah dijelaskan R-310 (bulan
  pertama simbol terisi sebagian, 92,7% defisit semesta ada di sana);
- baris MATI dikeluarkan karena kesembilan baris MATI tak penuh sudah dikenal
  namanya dan defisitnya sudah dijumlah (95.237), sedangkan baris MATI berlilin
  penuh berdefisit nol MENURUT DEFINISI sehingga tidak mungkin menanggung sisa.

## Aritmetika implikasi (aturan 83) — sudah ditulis di jurnal 134 §3

Cacah baris berdefisit dijamin berada di **16 .. 18.790**: batas bawah dari
712.925 / 44.639 (satu baris paling banyak menanggung sebulan penuh kurang satu
lilin, sebab `cacah_baris_tanpa_lilin` = 0), batas atas dari 18.799 baris
bukan-pertama dikurangi kesembilan baris MATI tak penuh. Tiga tingkat besaran;
aritmetika ini TIDAK menentukan jawabannya.

Tiga calon butir dibuang karena tautologi: "ada baris berdefisit?" (pasti YA,
sebab 712.925 > 0), "cacahnya >= 16?" (sudah dibuktikan di atas), dan "defisit
terbesar < 44.640?" (dipaksa definisi `lilin_penuh`).

## KC-50 — penyebut butir 2 sengaja BUKAN 712.925

712.925 adalah angka TURUNAN dari pengurangan. KC-50 melarangnya menjadi
penyebut pemeriksaan. Penyebut `bagian_teratas` dihitung LANGSUNG dari baris
yang sama yang menghasilkan numeratornya, yakni jumlah defisit seluruh baris
berdefisit di dalam penyebut kerja.

Selisih terhadap 808.162 dan 95.237 tetap dilaporkan meski nol, dan
`selisih_sisa` terhadap 712.925 dilapor sebagai KETERANGAN — bukan sebagai
penyebut apa pun.

## Pembulatan (aturan 53)

`_bagian` membulatkan ke EMPAT desimal dengan `round` bawaan Python. Modul ini
sengaja TIDAK memakai `kohort_ekor.bagian` walau perilakunya serupa, sebab
`kohort_ekor.py` tidak dibaca utuh pada giliran penulisan ini (KC-43); memakai
fungsi yang belum dibaca berarti menebak. Penyebut nol menghasilkan null, bukan
nol (aturan 41, 46).

## PRAREGISTRASI R-311 — TERKUNCI di jurnal 134 §5, dilarang disentuh (aturan 29)

- **Butir 1 (BERISIKO)** — cacah baris bukan-pertama berstatus bukan-MATI yang
  `cacah_lilin` kurang dari lilin penuh bulannya, berada dalam pita
  **200 .. 12.000** inklusif. Satuan: BARIS simbol-bulan. Kalah bila defisit
  terpusat pada puluhan baris; kalah pula bila hampir setiap baris bukan-pertama
  berdefisit. Penyebut nol menghasilkan TIDAK TERADJUDIKASI (aturan 41).
- **Butir 2 (BERISIKO)** — bagian sisa defisit yang ditanggung SEPULUH baris
  berdefisit terbesar, dengan penyebut jumlah defisit baris-baris berdefisit itu
  sendiri, berada dalam pita **0,02 .. 0,45** inklusif. Satuan: BAGIAN antara 0
  dan 1, bukan persen (aturan 47). Kalah bila satu peristiwa besar menguasai;
  kalah pula bila sebarannya nyaris seragam sempurna. Bila baris berdefisit
  kurang dari sepuluh, TIDAK TERADJUDIKASI.
- **Butir 3 (MUDAH, dinyatakan mudah di muka)** — seluruh selisih invarian nol,
  ketiga kendali lolos, `cacah_defisit_negatif` nol, sidik laporan seragam.
  Deterministik, TIDAK masuk papan skor.

Seluruh butir berisiko berklausa TUNGGAL (aturan 84). Tidak satu pun memakai
klausa ATAU.

## Jalur LANGSUNG (KC-50)

Seluruh agregat dijumlah LANGSUNG dari baris, bukan dijumlah dari total per
kelas. Pembangun baris `keterisian_lilin.kumpulkan` memang dipakai bersama,
sehingga jalur ini BUKAN sepenuhnya bebas dari R-310 — itu disebut di sini apa
adanya, bukan disembunyikan.

Aturan yang mengikat: 10, 21, 22, 24, 29, 30, 38, 41, 44, 45, 46, 47, 50, 52,
53, 57, 66, 79, 82, 83, 84. Kunci cacat: KC-41, KC-43, KC-48, KC-50.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from . import kehidupan, kehidupan_arsip, keterisian_lilin, silang_funding

VERSI = 1
TOTAL_PECAHAN = kehidupan_arsip.TOTAL_PECAHAN
KELUARAN = "reports/sisa_defisit.json"
KELUARAN_RINGKAS = "reports/sisa_defisit_ringkas.json"

# Aturan 52: laporan yang tak terbaca utuh sama dengan tidak ada.
BATAS_BARIS_LAPORAN = 40

MEDAN_LILIN = keterisian_lilin.MEDAN_LILIN
CACAH_TERATAS = 10
CACAH_TERATAS_KENDALI = 2

# Pita R-311, TERKUNCI di jurnal 134 (aturan 29). Dilarang disentuh.
R311_PITA_BUTIR_1 = (200, 12000)
R311_PITA_BUTIR_2 = (0.02, 0.45)

# Sepuluh invarian yang sudah diterbitkan. Pembanding, BUKAN masukan.
INVARIAN = {
    "penyebut": 19586,
    "cacah_simbol": 787,
    "cacah_bukan_pertama": 18799,
    "cacah_hidup": 18087,
    "cacah_sepi": 98,
    "cacah_mati": 1401,
    "cacah_mati_penuh": 1392,
    "cacah_mati_tak_penuh": 9,
    "defisit_bukan_pertama": 808162,
    "defisit_sembilan": 95237,
}

# Angka TURUNAN. Dilapor sebagai keterangan, DILARANG jadi penyebut (KC-50).
SISA_TERCATAT = 712925

BERKAS_DICAP = [
    "kehidupan.py",
    "kehidupan_arsip.py",
    "keterisian_lilin.py",
    "silang_funding.py",
    "sisa_defisit.py",
]

Kunci = Tuple[str, str]


def nama_keluaran() -> str:
    return KELUARAN


def nama_ringkas() -> str:
    return KELUARAN_RINGKAS


def daftar_sumber(total: int = TOTAL_PECAHAN) -> List[str]:
    return [kehidupan_arsip.nama_keluaran(i) for i in range(int(total))]


def sidik_kode() -> str:
    """Aturan 22: cap setiap berkas yang ikut menentukan angka ini."""
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(BERKAS_DICAP):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def _bagian(a: int, b: int) -> Optional[float]:
    """Aturan 41/46/53: penyebut nol menghasilkan null; bulat empat desimal."""
    if not b:
        return None
    return round(float(a) / float(b), 4)


def calon_baris(baris: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Penyebut kerja: bukan-pertama DAN berstatus bukan MATI."""
    return [
        r
        for r in baris
        if not r.get("pertama") and r.get("status") != kehidupan.STATUS_MATI
    ]


def baris_berdefisit(baris: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Defisit yang benar-benar positif; null TIDAK ditebak sebagai nol."""
    return [
        r
        for r in baris
        if r.get("defisit") is not None and int(r["defisit"]) > 0
    ]


def teratas(
    baris: List[Dict[str, Any]], cacah: int = CACAH_TERATAS
) -> List[Dict[str, Any]]:
    """Urutan deterministik walau defisitnya seri (aturan 50)."""
    urut = sorted(
        baris,
        key=lambda r: (-int(r.get("defisit") or 0), str(r.get("simbol")), str(r.get("bulan"))),
    )
    return urut[: int(cacah)]


def jumlah_defisit(baris: List[Dict[str, Any]]) -> int:
    """Jalur LANGSUNG: dijumlah dari baris, bukan dari total per kelas."""
    return sum(int(r.get("defisit") or 0) for r in baris)


def bagian_teratas(
    berdefisit: List[Dict[str, Any]], cacah: int = CACAH_TERATAS
) -> Optional[float]:
    """Butir 2. Penyebut dihitung LANGSUNG dari baris yang sama (KC-50).

    Kurang dari `cacah` baris berdefisit menghasilkan null, yang di adjudikasi
    dibaca sebagai TIDAK TERADJUDIKASI, bukan sebagai kekalahan (aturan 41).
    """
    if len(berdefisit) < int(cacah):
        return None
    penyebut = jumlah_defisit(berdefisit)
    if not penyebut:
        return None
    return _bagian(jumlah_defisit(teratas(berdefisit, cacah)), penyebut)


def sebaran_status(baris: List[Dict[str, Any]]) -> Dict[str, int]:
    """KETERANGAN, bukan butir yang diadjudikasi (jurnal 134 §8)."""
    keluar: Dict[str, int] = {
        kehidupan.STATUS_HIDUP: 0,
        kehidupan.STATUS_SEPI: 0,
        kehidupan.STATUS_MATI: 0,
        kehidupan.STATUS_TAK_TERUKUR: 0,
    }
    for r in baris:
        nama = str(r.get("status"))
        keluar[nama] = keluar.get(nama, 0) + 1
    return keluar


def baris_mati_tak_penuh(baris: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [
        r
        for r in baris
        if r.get("status") == kehidupan.STATUS_MATI
        and r.get("defisit") is not None
        and int(r["defisit"]) != 0
    ]


def ringkas_bukan_pertama(baris: List[Dict[str, Any]]) -> Dict[str, int]:
    """Hitung ulang LANGSUNG agregat yang akan diadu dengan angka terbitan."""
    bukan_pertama = negatif = tanpa_lilin = 0
    for r in baris:
        if r.get("cacah_lilin") is None:
            tanpa_lilin += 1
            continue
        d = r.get("defisit")
        d = 0 if d is None else int(d)
        if d < 0:
            negatif += 1
            continue
        if not r.get("pertama"):
            bukan_pertama += d
    return {
        "defisit_bukan_pertama": bukan_pertama,
        "cacah_defisit_negatif": negatif,
        "cacah_baris_tanpa_lilin": tanpa_lilin,
    }


def invarian_terukur(baris: List[Dict[str, Any]]) -> Dict[str, int]:
    """Kesepuluh invarian dihitung LANGSUNG dari baris."""
    tak_penuh = baris_mati_tak_penuh(baris)
    r = ringkas_bukan_pertama(baris)
    return {
        "penyebut": len(baris),
        "cacah_simbol": len({str(x.get("simbol")) for x in baris}),
        "cacah_bukan_pertama": sum(1 for x in baris if not x.get("pertama")),
        "cacah_hidup": sum(
            1 for x in baris if x.get("status") == kehidupan.STATUS_HIDUP
        ),
        "cacah_sepi": sum(
            1 for x in baris if x.get("status") == kehidupan.STATUS_SEPI
        ),
        "cacah_mati": sum(
            1 for x in baris if x.get("status") == kehidupan.STATUS_MATI
        ),
        "cacah_mati_penuh": sum(
            1
            for x in baris
            if x.get("status") == kehidupan.STATUS_MATI
            and x.get("defisit") is not None
            and int(x["defisit"]) == 0
        ),
        "cacah_mati_tak_penuh": len(tak_penuh),
        "defisit_bukan_pertama": int(r["defisit_bukan_pertama"]),
        "defisit_sembilan": jumlah_defisit(tak_penuh),
    }


def selisih_invarian(terukur: Dict[str, int]) -> Dict[str, int]:
    return {k: int(terukur.get(k) or 0) - int(v) for k, v in INVARIAN.items()}


def dalam_pita(nilai: Optional[int], pita: Tuple[int, int]) -> bool:
    if nilai is None:
        return False
    return int(pita[0]) <= int(nilai) <= int(pita[1])


def dalam_pita_pecahan(nilai: Optional[float], pita: Tuple[float, float]) -> bool:
    if nilai is None:
        return False
    return float(pita[0]) <= float(nilai) <= float(pita[1])


def potong(
    baris: List[Dict[str, Any]], batas: int = BATAS_BARIS_LAPORAN
) -> List[Dict[str, Any]]:
    return list(baris)[: int(batas)]


def semesta_kendali() -> Tuple[Dict[Kunci, str], Dict[Kunci, int]]:
    """Semesta buatan yang memuat baris BERDEFISIT dan baris BERLILIN PENUH.

    Aturan 50 menuntut kendali membuktikan modul dapat MEMBEDAKAN keduanya,
    bukan sekadar menghasilkan angka. Jawabannya dihitung TANGAN di bawah.
    """
    status = {
        ("AAA", "2024-01"): kehidupan.STATUS_HIDUP,
        ("AAA", "2024-02"): kehidupan.STATUS_HIDUP,
        ("AAA", "2024-03"): kehidupan.STATUS_HIDUP,
        ("BBB", "2023-06"): kehidupan.STATUS_SEPI,
        ("BBB", "2023-07"): kehidupan.STATUS_SEPI,
        ("CCC", "2025-04"): kehidupan.STATUS_MATI,
        ("CCC", "2025-05"): kehidupan.STATUS_MATI,
        ("DDD", "2022-01"): kehidupan.STATUS_HIDUP,
        ("DDD", "2022-02"): kehidupan.STATUS_HIDUP,
        ("EEE", "2021-08"): kehidupan.STATUS_MATI,
        ("EEE", "2021-09"): kehidupan.STATUS_MATI,
    }
    lilin = {
        ("AAA", "2024-01"): 44640,
        ("AAA", "2024-02"): 41660,
        ("AAA", "2024-03"): 44140,
        ("BBB", "2023-06"): 43200,
        ("BBB", "2023-07"): 44620,
        ("CCC", "2025-04"): 43000,
        ("CCC", "2025-05"): 44540,
        ("DDD", "2022-01"): 44640,
        ("DDD", "2022-02"): 40320,
        ("EEE", "2021-08"): 44640,
        ("EEE", "2021-09"): 43200,
    }
    return status, lilin


# Dihitung TANGAN sebelum modul dijalankan sekali pun.
# Lilin penuh: 2024-01 = 31x1440 = 44.640; 2024-02 kabisat = 29x1440 = 41.760;
# 2024-03 = 44.640; 2023-06 = 30x1440 = 43.200; 2023-07 = 44.640;
# 2025-04 = 43.200; 2025-05 = 44.640; 2022-01 = 44.640; 2022-02 = 28x1440 =
# 40.320; 2021-08 = 44.640; 2021-09 = 43.200.
# Defisit: AAA-01 0 (pertama); AAA-02 100; AAA-03 500; BBB-06 0 (pertama);
# BBB-07 20; CCC-04 200 (pertama, MATI); CCC-05 100 (MATI); DDD-01 0 (pertama);
# DDD-02 0; EEE-08 0 (pertama, MATI penuh); EEE-09 0 (MATI penuh).
# Baris 11; simbol 5; bukan-pertama 6; HIDUP 5, SEPI 2, MATI 4.
# MATI penuh 2 (EEE keduanya); MATI tak penuh 2 (CCC keduanya), defisitnya 300.
# defisit_bukan_pertama = 100+500+20+100+0+0 = 720.
# Calon (bukan-pertama, bukan MATI) = AAA-02, AAA-03, BBB-07, DDD-02 = 4.
# Berdefisit di antara calon = AAA-02, AAA-03, BBB-07 = 3, jumlahnya 620.
# Dua teratas = 500 + 100 = 600. Bagian = 600/620 = 0,967741... -> 0,9677.
JAWABAN_KENDALI = {
    "penyebut": 11,
    "cacah_simbol": 5,
    "cacah_bukan_pertama": 6,
    "cacah_hidup": 5,
    "cacah_sepi": 2,
    "cacah_mati": 4,
    "cacah_mati_penuh": 2,
    "cacah_mati_tak_penuh": 2,
    "defisit_sembilan": 300,
    "defisit_bukan_pertama": 720,
    "cacah_calon": 4,
    "cacah_berdefisit": 3,
    "defisit_calon": 620,
    "defisit_teratas": 600,
    "bagian_teratas": 0.9677,
    "cacah_defisit_negatif": 0,
    "cacah_baris_tanpa_lilin": 0,
}


def baris_kendali() -> List[Dict[str, Any]]:
    status, lilin = semesta_kendali()
    return keterisian_lilin.kumpulkan(status, lilin)


def kendali_negatif() -> Dict[str, Any]:
    """Aturan 50: buktikan modul melihat baris berdefisit DAN baris penuh."""
    baris = baris_kendali()
    calon = calon_baris(baris)
    berdefisit = baris_berdefisit(calon)
    terukur = dict(invarian_terukur(baris))
    terukur.update(
        {
            "cacah_calon": len(calon),
            "cacah_berdefisit": len(berdefisit),
            "defisit_calon": jumlah_defisit(berdefisit),
            "defisit_teratas": jumlah_defisit(
                teratas(berdefisit, CACAH_TERATAS_KENDALI)
            ),
            "bagian_teratas": bagian_teratas(berdefisit, CACAH_TERATAS_KENDALI),
        }
    )
    terukur.update(ringkas_bukan_pertama(baris))
    return {
        "terukur": terukur,
        "diharapkan": dict(JAWABAN_KENDALI),
        "lolos": terukur == JAWABAN_KENDALI,
    }


def semesta_nol() -> Tuple[Dict[Kunci, str], Dict[Kunci, int]]:
    status = {
        ("FFF", "2024-01"): kehidupan.STATUS_HIDUP,
        ("FFF", "2024-02"): kehidupan.STATUS_HIDUP,
    }
    lilin = {("FFF", "2024-01"): 44640, ("FFF", "2024-02"): 41760}
    return status, lilin


def kendali_nol() -> Dict[str, Any]:
    """Kendali bahwa detektor sanggup menjawab NOL, bukan mengarang defisit."""
    status, lilin = semesta_nol()
    calon = calon_baris(keterisian_lilin.kumpulkan(status, lilin))
    berdefisit = baris_berdefisit(calon)
    bagian = bagian_teratas(berdefisit, CACAH_TERATAS_KENDALI)
    return {
        "cacah_calon": len(calon),
        "cacah_berdefisit": len(berdefisit),
        "bagian_teratas": bagian,
        "lolos": len(calon) == 1 and len(berdefisit) == 0 and bagian is None,
    }


def uji_r311(
    cacah_calon: int,
    cacah_berdefisit: Optional[int],
    bagian: Optional[float],
    selisih: Dict[str, int],
    bersih: bool,
) -> Dict[str, Any]:
    """Adjudikasi ketiga butir terhadap pita yang dikunci di jurnal 134."""
    if int(cacah_calon) == 0:
        s1 = "tidak_teradjudikasi"
    else:
        s1 = "menang" if dalam_pita(cacah_berdefisit, R311_PITA_BUTIR_1) else "kalah"
    if bagian is None or int(cacah_berdefisit or 0) < CACAH_TERATAS:
        s2 = "tidak_teradjudikasi"
    else:
        s2 = (
            "menang"
            if dalam_pita_pecahan(bagian, R311_PITA_BUTIR_2)
            else "kalah"
        )
    b3 = (
        bool(bersih)
        and len(selisih) == len(INVARIAN)
        and all(int(v) == 0 for v in selisih.values())
    )
    return {
        "butir_1": {
            "pertanyaan": (
                "cacah baris bukan-pertama bukan-MATI yang cacah_lilin kurang "
                "dari lilin penuh bulannya"
            ),
            "satuan": "baris simbol-bulan",
            "pita": list(R311_PITA_BUTIR_1),
            "terukur": cacah_berdefisit,
            "berisiko": True,
            "hasil": s1,
        },
        "butir_2": {
            "pertanyaan": (
                "bagian defisit yang ditanggung sepuluh baris berdefisit "
                "terbesar, atas penyebut jumlah defisit baris berdefisit itu "
                "sendiri"
            ),
            "satuan": "bagian antara 0 dan 1",
            "pita": list(R311_PITA_BUTIR_2),
            "terukur": bagian,
            "berisiko": True,
            "hasil": s2,
        },
        "butir_3": {
            "pertanyaan": "seluruh selisih invarian nol dan ketiga kendali lolos",
            "satuan": "cocok atau tidak",
            "berisiko": False,
            "mudah": True,
            "hasil": "menang" if b3 else "kalah",
        },
        "cacah_menang_berisiko": int(s1 == "menang") + int(s2 == "menang"),
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
    if int(ringkasan.get("cacah_defisit_negatif") or 0) > 0:
        return 2
    if int(ringkasan.get("cacah_baris_tanpa_lilin") or 0) > 0:
        return 2
    selisih = ringkasan.get("selisih_invarian") or {}
    if len(selisih) != len(INVARIAN):
        return 2
    if any(int(v) != 0 for v in selisih.values()):
        return 2
    if not ringkasan.get("kendali_data_sah"):
        return 2
    if not ringkasan.get("kendali_negatif_lolos"):
        return 2
    if not ringkasan.get("kendali_nol_lolos"):
        return 2
    return 0


def jalankan(akar: str = ".", total: Optional[int] = None) -> Dict[str, Any]:
    total = TOTAL_PECAHAN if total is None else int(total)
    status, byte_parquet, meta = silang_funding.baca_laporan_kehidupan(
        akar=akar, total=total
    )
    lilin, meta_lilin = silang_funding.baca_medan_baris(
        akar=akar, total=total, medan=MEDAN_LILIN
    )

    baris = keterisian_lilin.kumpulkan(status, lilin)
    calon = calon_baris(baris)
    berdefisit = baris_berdefisit(calon)
    atas = teratas(berdefisit, CACAH_TERATAS)
    terukur = invarian_terukur(baris)
    selisih = selisih_invarian(terukur)
    r = ringkas_bukan_pertama(baris)
    bagian = bagian_teratas(berdefisit, CACAH_TERATAS)

    kd = keterisian_lilin.kendali_data(status, byte_parquet)
    for baris_kd in kd:
        baris_kd["cacah_lilin"] = lilin.get((baris_kd["simbol"], baris_kd["bulan"]))
    neg = kendali_negatif()
    nol = kendali_nol()

    defisit_calon = jumlah_defisit(berdefisit)
    sisa_terukur = int(terukur["defisit_bukan_pertama"]) - int(
        terukur["defisit_sembilan"]
    )

    ringkasan: Dict[str, Any] = {
        "invarian_terukur": terukur,
        "invarian_tercatat": dict(INVARIAN),
        "selisih_invarian": selisih,
        "selisih_defisit_bukan_pertama": int(selisih["defisit_bukan_pertama"]),
        "selisih_defisit_sembilan": int(selisih["defisit_sembilan"]),
        "cacah_calon": len(calon),
        "cacah_berdefisit": len(berdefisit),
        "cacah_calon_penuh": len(calon) - len(berdefisit),
        "defisit_calon": defisit_calon,
        "defisit_teratas": jumlah_defisit(atas),
        "bagian_teratas": bagian,
        "cacah_teratas": CACAH_TERATAS,
        "defisit_terbesar": int(atas[0]["defisit"]) if atas else None,
        "sisa_terukur": sisa_terukur,
        "sisa_tercatat": SISA_TERCATAT,
        "selisih_sisa": sisa_terukur - SISA_TERCATAT,
        "selisih_defisit_calon_lawan_sisa": defisit_calon - sisa_terukur,
        "sebaran_status_berdefisit": sebaran_status(berdefisit),
        "sebaran_status_calon": sebaran_status(calon),
        "kendali_data": kd,
        "kendali_data_sah": keterisian_lilin.kendali_data_sah(kd),
        "kendali_negatif_lolos": bool(neg.get("lolos")),
        "kendali_nol_lolos": bool(nol.get("lolos")),
    }
    ringkasan.update(r)
    ringkasan.update(meta)
    ringkasan.update(meta_lilin)

    bersih = (
        bool(ringkasan.get("sidik_seragam"))
        and int(ringkasan.get("cacah_defisit_negatif") or 0) == 0
        and int(ringkasan.get("cacah_baris_tanpa_lilin") or 0) == 0
        and bool(ringkasan.get("kendali_data_sah"))
        and bool(ringkasan.get("kendali_negatif_lolos"))
        and bool(ringkasan.get("kendali_nol_lolos"))
    )
    ringkasan["uji_r311"] = uji_r311(
        len(calon), len(berdefisit), bagian, selisih, bersih
    )

    return {
        "bukan_bukti": False,
        "versi_sisa_defisit": VERSI,
        "sidik_kode": sidik_kode(),
        "sumber": daftar_sumber(total),
        "definisi": {
            "penyebut_kerja": (
                "baris bukan-pertama yang berstatus BUKAN MATI"
            ),
            "berdefisit": "defisit positif; null tidak ditebak sebagai nol",
            "bagian_teratas": (
                "jumlah defisit sepuluh baris terbesar dibagi jumlah defisit "
                "SELURUH baris berdefisit di penyebut kerja; penyebutnya "
                "dihitung LANGSUNG, bukan angka turunan 712.925 (KC-50)"
            ),
            "pertama": "bulan terkecil simbol itu DI DALAM penyebut 19.586",
            "defisit_sembilan": (
                "jumlah defisit seluruh baris MATI yang lilinnya tidak penuh"
            ),
        },
        "baris_teratas": potong(atas),
        "baris_mati_tak_penuh": potong(baris_mati_tak_penuh(baris)),
        "batas_baris_laporan": BATAS_BARIS_LAPORAN,
        "kendali_negatif": neg,
        "kendali_nol": nol,
        "ringkasan": ringkasan,
        "catatan_harga": (
            "laporan kehidupan TIDAK menyimpan harga; dugaan harga beku, lilin "
            "datar, atau jeda pemeliharaan bursa TIDAK diuji di sini dan "
            "dilarang disimpulkan dari laporan ini"
        ),
        "catatan_byte": (
            "besar berkas tetap dilarang dipakai sebagai detektor status ke "
            "arah mana pun (ADR-A015 kep. 5); modul ini tidak memakai byte "
            "kecuali untuk kendali positif BTCUSDT"
        ),
        "catatan_turunan": (
            "712.925 adalah angka TURUNAN dari pengurangan dan DILARANG jadi "
            "penyebut pemeriksaan (KC-50); ia hanya dilapor sebagai keterangan "
            "lewat sisa_terukur dan selisih_sisa"
        ),
        "catatan_kebebasan": (
            "pembangun baris keterisian_lilin.kumpulkan dipakai bersama dengan "
            "R-310, sehingga hitung ulang ini BUKAN jalur yang sepenuhnya "
            "bebas; ia menangkap salah kutip dan laporan basi, bukan cacat "
            "pada pembangun barisnya sendiri"
        ),
        "catatan_penggugur": (
            "sidik tidak seragam, laporan pecahan kurang, kunci ganda, defisit "
            "negatif, baris tanpa cacah_lilin, selisih invarian bukan nol, "
            "atau salah satu dari ketiga kendali gagal membatalkan seluruh "
            "angka; ketiga butir lalu dicatat TIDAK TERADJUDIKASI, bukan "
            "MELESET (aturan 24)"
        ),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def berkas_ringkas(laporan: Dict[str, Any], teks_sumber: str) -> Dict[str, Any]:
    """Aturan 52: ringkasan yang terbaca UTUH dalam satu bacaan."""
    byte_sumber = teks_sumber.encode("utf-8")
    return {
        "versi_sisa_defisit": laporan.get("versi_sisa_defisit"),
        "sidik_kode": laporan.get("sidik_kode"),
        "berkas_sumber": KELUARAN,
        "byte_sumber": len(byte_sumber),
        "sidik_sumber": hashlib.sha256(byte_sumber).hexdigest(),
        "definisi": laporan.get("definisi"),
        "baris_teratas": laporan.get("baris_teratas"),
        "ringkasan": laporan.get("ringkasan"),
        "catatan_turunan": laporan.get("catatan_turunan"),
        "catatan_kebebasan": laporan.get("catatan_kebebasan"),
        "waktu_utc": laporan.get("waktu_utc"),
    }


def main() -> int:
    laporan = jalankan()
    teks = json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    Path(KELUARAN).parent.mkdir(parents=True, exist_ok=True)
    Path(KELUARAN).write_text(teks, encoding="utf-8")
    ringkas = berkas_ringkas(laporan, teks)
    Path(KELUARAN_RINGKAS).write_text(
        json.dumps(ringkas, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(ringkas, ensure_ascii=False, indent=2, sort_keys=True))
    return kode_keluar(laporan["ringkasan"])


if __name__ == "__main__":
    raise SystemExit(main())
