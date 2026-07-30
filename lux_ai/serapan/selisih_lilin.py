"""Ukur SELISIH per baris antara `cacah_lilin` dan `cacah_lilin_terbaca`.

Dua angka semesta sudah terbit dan TIDAK sama:

- `jumlah_lilin_langsung` = **839.325.999**, dijumlah LANGSUNG dari medan
  `cacah_lilin` oleh `keterisian_lilin` atas penyebut 19.586;
- baris parquet semesta = **839.842.134**, terbit dari run rilis parquet.

Selisihnya **516.135**. Yang belum pernah diukur adalah BENTUK SEBARAN selisih
itu: apakah ia terkumpul di segelintir simbol-bulan, atau tersebar tipis atas
ribuan baris. Modul ini menjawab pertanyaan itu dan hanya pertanyaan itu.

## Apa yang dibandingkan, ditulis SEBELUM pengukuran

Laporan kehidupan menulis DUA medan cacah per simbol-bulan: `cacah_lilin`
(klaim) dan `cacah_lilin_terbaca` (terbaca). Keduanya sudah tercatat dalam
daftar 14 medan `medan_baris_terlihat`. Modul ini mengambil keduanya lewat
`silang_funding.baca_medan_baris`, satu panggilan per medan, lalu mengurangkan
per BARIS -- bukan mengurangkan dua total yang sudah jadi.

    selisih(baris) = cacah_lilin_terbaca - cacah_lilin

Arah itu dipilih supaya selisih semesta bertanda POSITIF bila jumlah terbaca
memang lebih besar, sesuai dua angka di atas. Arah TIDAK boleh dibalik sesudah
laporan dibaca (aturan 29).

## Jalur LANGSUNG wajib (KC-50)

`jumlah_klaim_langsung` dan `jumlah_terbaca_langsung` dijumlah dari baris, bukan
dari total per kelas status. `jumlah_selisih_bersih` juga dijumlah dari baris,
lalu DIPERIKSA sama dengan selisih kedua jumlah langsung. Bila dua jalur itu
tidak bertemu, kesalahannya ada pada kode ini, bukan pada data.

Angka 712.925 DILARANG dipakai sebagai penyebut apa pun di sini (KC-50).

## Yang TIDAK dapat dijawab modul ini

Laporan kehidupan tidak menyimpan harga dan tidak menyimpan cap waktu per
menit. Karena itu modul ini TIDAK dapat mengatakan lilin MANA yang hilang, di
menit ke berapa, atau apakah lubangnya di awal, tengah, atau ekor bulan. Ia
hanya mencacah BERAPA dan DI BARIS MANA. Dugaan "harga beku", "lilin datar",
dan "jeda pemeliharaan bursa" tetap DILARANG disimpulkan (KC-41).

Besar berkas tetap DILARANG dipakai sebagai detektor status (ADR-A015 kep. 5).

## Tautologi yang dibuang sebelum menjadi butir (aturan 82, KC-48)

1. "Jumlah selisih sama dengan 516.135" mengulang aritmetika dua angka yang
   sudah terbit; ia dicatat sebagai PEMERIKSAAN, bukan ramalan.
2. "Selisih tidak pernah melampaui lilin penuh sebulan" dipaksa definisi cacah.
3. "Baris tanpa medan tidak punya selisih" mengulang definisi null.

## Praregistrasi R-312 -- pita TERKUNCI di jurnal 136 sebelum modul ini ada

- **Butir 1 (BERISIKO)** -- cacah simbol-bulan yang selisihnya BUKAN nol berada
  dalam pita **12..120** inklusif. Satuan: SIMBOL-BULAN. Lantai aritmetis 12
  berasal dari 516.135 dibagi 44.640 (lilin terbanyak sebulan) = 11,56...,
  dibulatkan ke atas. Rentang implikasi sebenarnya 12..19.586, jadi pita ini
  menutup kurang dari satu persen ruang jawab. Gugur ke atas bila lebih dari
  120.
- **Butir 2 (BERISIKO, bebas dari butir 1)** -- bagian jumlah selisih yang
  disumbang SEPULUH baris berselisih positif terbesar, dibagi jumlah seluruh
  selisih positif, berada dalam pita **0,50..0,865**. Satuan: BAGIAN antara 0
  dan 1, bukan persen (aturan 47). Langit-langit 0,865 = 10 x 44.640 / 516.135
  adalah batas fisik, bukan tebakan. Taksiran titik 0,833 = 10/12 berlaku hanya
  bila butir 1 mendarat tepat di lantainya. Butir 1 mencacah BARIS, butir 2
  menimbang LILIN; keduanya dapat menang atau kalah sendiri-sendiri.
- **Butir 3 (MUDAH, dinyatakan mudah di muka)** -- kedelapan invarian semesta
  terbaca ulang identik. Deterministik, TIDAK masuk papan skor.

Tidak satu pun butir memakai klausa ATAU (aturan 84).

## Empat syarat gugur, dikunci di muka

1. Medan `cacah_lilin_terbaca` tidak ada, atau identik dengan `cacah_lilin` di
   SELURUH baris: laporan TIDAK TERADJUDIKASI (aturan 41), bukan MELESET.
2. Jumlah selisih bersih tidak sama dengan 516.135: ketiga butir TETAP
   diadjudikasi, dan kesenjangannya dicatat sebagai KC baru. Angka modul yang
   berlaku, bukan angka warisan.
3. Bila butir 1 mendarat tepat di 12, kesamaannya dengan dugaan 12 bulan
   karantina DILARANG dibaca sebagai konfirmasi apa pun.
4. Kemenangan yang menempel tepi pita DILARANG dibaca sebagai kalibrasi yang
   membaik (KC-51).

Aturan yang mengikat: 21, 22, 24, 29, 30, 38, 41, 44, 46, 47, 50, 52, 53, 57,
66, 79, 82, 83, 84, 85.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from . import kehidupan, kehidupan_arsip, kohort_ekor, silang_funding

VERSI = 1
TOTAL_PECAHAN = kehidupan_arsip.TOTAL_PECAHAN
KELUARAN = "reports/selisih_lilin.json"
KELUARAN_RINGKAS = "reports/selisih_lilin_ringkas.json"

# Aturan 52: laporan yang tak terbaca utuh sama dengan tidak ada.
BATAS_BARIS_LAPORAN = 40

MEDAN_KLAIM = "cacah_lilin"
MEDAN_TERBACA = "cacah_lilin_terbaca"
CACAH_TERATAS = 10

# Angka warisan, dipakai sebagai PEMBANDING, bukan sebagai masukan.
LILIN_LANGSUNG_TERCATAT = 839325999
BARIS_PARQUET_TERCATAT = 839842134
SELISIH_TERCATAT = 516135

AMBANG_HIDUP_KECIL = 97634

# Delapan invarian semesta yang sudah diterbitkan. Pembanding, BUKAN masukan.
INVARIAN = {
    "penyebut": 19586,
    "cacah_simbol": 787,
    "cacah_hidup": 18087,
    "cacah_sepi": 98,
    "cacah_mati": 1401,
    "total_byte": 32706262375,
    "byte_hidup": 32049492952,
    "cacah_hidup_byte_kecil": 38,
}

# Pita R-312, TERKUNCI di jurnal 136 (aturan 29). Dilarang disentuh.
R312_PITA_BUTIR_1 = (12, 120)
R312_PITA_BUTIR_2 = (0.50, 0.865)

BERKAS_DICAP = [
    "kehidupan.py",
    "kehidupan_arsip.py",
    "selisih_lilin.py",
    "silang_funding.py",
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


def selisih(klaim: Optional[int], terbaca: Optional[int]) -> Optional[int]:
    """Null bila salah satu medan tak ada; ketiadaan TIDAK ditebak sebagai nol."""
    if klaim is None or terbaca is None:
        return None
    return int(terbaca) - int(klaim)


def kumpulkan(
    status: Dict[Kunci, str],
    klaim: Dict[Kunci, Any],
    terbaca: Dict[Kunci, Any],
) -> List[Dict[str, Any]]:
    """Satu baris per simbol-bulan, urutan deterministik."""
    baris: List[Dict[str, Any]] = []
    for k in sorted(status):
        simbol, bulan = k
        a = klaim.get(k)
        b = terbaca.get(k)
        a = None if a is None else int(a)
        b = None if b is None else int(b)
        baris.append(
            {
                "simbol": simbol,
                "bulan": bulan,
                "status": str(status[k]),
                "cacah_lilin": a,
                "cacah_lilin_terbaca": b,
                "selisih": selisih(a, b),
            }
        )
    return baris


def ringkas_selisih(baris: List[Dict[str, Any]]) -> Dict[str, int]:
    """Jalur LANGSUNG: seluruhnya dijumlah dari baris (KC-50)."""
    cacah_baris = len(baris)
    berselisih = positif = negatif = 0
    jumlah_positif = jumlah_negatif = 0
    jumlah_klaim = jumlah_terbaca = 0
    tanpa_klaim = tanpa_terbaca = 0
    for r in baris:
        a = r.get("cacah_lilin")
        b = r.get("cacah_lilin_terbaca")
        if a is None:
            tanpa_klaim += 1
        else:
            jumlah_klaim += int(a)
        if b is None:
            tanpa_terbaca += 1
        else:
            jumlah_terbaca += int(b)
        d = r.get("selisih")
        if d is None:
            continue
        d = int(d)
        if d == 0:
            continue
        berselisih += 1
        if d > 0:
            positif += 1
            jumlah_positif += d
        else:
            negatif += 1
            jumlah_negatif += -d
    return {
        "cacah_baris": cacah_baris,
        "cacah_berselisih": berselisih,
        "cacah_selisih_positif": positif,
        "cacah_selisih_negatif": negatif,
        "jumlah_selisih_positif": jumlah_positif,
        "jumlah_selisih_negatif": jumlah_negatif,
        "jumlah_selisih_bersih": jumlah_positif - jumlah_negatif,
        "jumlah_klaim_langsung": jumlah_klaim,
        "jumlah_terbaca_langsung": jumlah_terbaca,
        "cacah_baris_tanpa_klaim": tanpa_klaim,
        "cacah_baris_tanpa_terbaca": tanpa_terbaca,
    }


def baris_berselisih(baris: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    keluar = [
        r for r in baris if r.get("selisih") is not None and int(r["selisih"]) != 0
    ]
    keluar.sort(key=lambda r: (-int(r["selisih"]), r["simbol"], r["bulan"]))
    return keluar


def baris_positif(baris: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [r for r in baris_berselisih(baris) if int(r["selisih"]) > 0]


def teratas(
    baris: List[Dict[str, Any]], cacah: int = CACAH_TERATAS
) -> Optional[List[Dict[str, Any]]]:
    """Null bila baris berselisih positif kurang dari `cacah` (aturan 46)."""
    positif = baris_positif(baris)
    if len(positif) < int(cacah):
        return None
    return positif[: int(cacah)]


def bagian_teratas(
    baris: List[Dict[str, Any]], cacah: int = CACAH_TERATAS
) -> Optional[float]:
    """Aturan 41/46: penyebut nol atau contoh kurang menghasilkan null."""
    puncak = teratas(baris, cacah)
    if puncak is None:
        return None
    penyebut = sum(int(r["selisih"]) for r in baris_positif(baris))
    if not penyebut:
        return None
    return kohort_ekor.bagian(sum(int(r["selisih"]) for r in puncak), penyebut)


def sebaran_kelas(baris: List[Dict[str, Any]]) -> Dict[str, Dict[str, int]]:
    """Cacah dan bobot selisih per kelas status, dijumlah LANGSUNG."""
    keluar: Dict[str, Dict[str, int]] = {}
    for r in baris_berselisih(baris):
        kelas = str(r.get("status"))
        pos = keluar.setdefault(kelas, {"cacah": 0, "jumlah_selisih": 0})
        pos["cacah"] += 1
        pos["jumlah_selisih"] += int(r["selisih"])
    return keluar


def potong(
    baris: List[Dict[str, Any]], batas: int = BATAS_BARIS_LAPORAN
) -> List[Dict[str, Any]]:
    return list(baris)[: int(batas)]


def dalam_pita(nilai: Optional[int], pita: Tuple[int, int]) -> bool:
    if nilai is None:
        return False
    return int(pita[0]) <= int(nilai) <= int(pita[1])


def dalam_pita_pecahan(nilai: Optional[float], pita: Tuple[float, float]) -> bool:
    if nilai is None:
        return False
    return float(pita[0]) <= float(nilai) <= float(pita[1])


def invarian_terukur(
    status: Dict[Kunci, str], byte_parquet: Dict[Kunci, int]
) -> Dict[str, int]:
    """Kedelapan invarian dihitung LANGSUNG dari baris, saling bebas."""
    hidup = [k for k, v in status.items() if v == kehidupan.STATUS_HIDUP]
    return {
        "penyebut": len(status),
        "cacah_simbol": len({s for s, _ in status}),
        "cacah_hidup": len(hidup),
        "cacah_sepi": sum(1 for v in status.values() if v == kehidupan.STATUS_SEPI),
        "cacah_mati": sum(1 for v in status.values() if v == kehidupan.STATUS_MATI),
        "total_byte": sum(int(b or 0) for b in byte_parquet.values()),
        "byte_hidup": sum(int(byte_parquet.get(k) or 0) for k in hidup),
        "cacah_hidup_byte_kecil": sum(
            1 for k in hidup if int(byte_parquet.get(k) or 0) <= AMBANG_HIDUP_KECIL
        ),
    }


def selisih_invarian(terukur: Dict[str, int]) -> Dict[str, int]:
    return {k: int(terukur.get(k) or 0) - int(v) for k, v in INVARIAN.items()}


def semesta_kendali() -> Tuple[Dict[Kunci, str], Dict[Kunci, int], Dict[Kunci, int]]:
    """Semesta buatan kecil yang jawabannya sudah dihitung TANGAN."""
    status = {
        ("AAA", "2024-01"): kehidupan.STATUS_HIDUP,
        ("AAA", "2024-02"): kehidupan.STATUS_MATI,
        ("BBB", "2023-02"): kehidupan.STATUS_MATI,
        ("CCC", "2025-04"): kehidupan.STATUS_HIDUP,
        ("CCC", "2025-05"): kehidupan.STATUS_HIDUP,
    }
    klaim = {
        ("AAA", "2024-01"): 44640,
        ("AAA", "2024-02"): 41000,
        ("BBB", "2023-02"): 40000,
        ("CCC", "2025-04"): 43200,
        ("CCC", "2025-05"): 44640,
    }
    terbaca = {
        ("AAA", "2024-01"): 44640,
        ("AAA", "2024-02"): 41760,
        ("BBB", "2023-02"): 40320,
        ("CCC", "2025-04"): 43000,
        ("CCC", "2025-05"): 44640,
    }
    return status, klaim, terbaca


# Dihitung tangan: selisih per baris 0, +760, +320, -200, 0. Berselisih 3
# (positif 2, negatif 1). Jumlah positif 1.080; besaran negatif 200; bersih 880.
# Klaim langsung 44.640+41.000+40.000+43.200+44.640 = 213.480. Terbaca langsung
# 44.640+41.760+40.320+43.000+44.640 = 214.360. Selisih dua jumlah = 880, sama
# dengan bersih. Tidak ada baris tanpa medan.
JAWABAN_KENDALI = {
    "cacah_baris": 5,
    "cacah_berselisih": 3,
    "cacah_selisih_positif": 2,
    "cacah_selisih_negatif": 1,
    "jumlah_selisih_positif": 1080,
    "jumlah_selisih_negatif": 200,
    "jumlah_selisih_bersih": 880,
    "jumlah_klaim_langsung": 213480,
    "jumlah_terbaca_langsung": 214360,
    "cacah_baris_tanpa_klaim": 0,
    "cacah_baris_tanpa_terbaca": 0,
}


def semesta_teratas() -> Tuple[Dict[Kunci, str], Dict[Kunci, int], Dict[Kunci, int]]:
    """Dua belas baris berselisih 100..1200, dipakai menguji butir 2."""
    status: Dict[Kunci, str] = {}
    klaim: Dict[Kunci, int] = {}
    terbaca: Dict[Kunci, int] = {}
    for i in range(1, 13):
        k = ("T%02d" % i, "2024-01")
        status[k] = kehidupan.STATUS_HIDUP
        klaim[k] = 1000
        terbaca[k] = 1000 + 100 * i
    return status, klaim, terbaca


# Dihitung tangan: jumlah seluruh selisih positif 100 x (1+..+12) = 7.800;
# sepuluh terbesar 100 x (3+..+12) = 7.500; bagian 7.500/7.800 = 0,9615.
JAWABAN_TERATAS = {
    "cacah_teratas": 10,
    "jumlah_teratas": 7500,
    "jumlah_positif": 7800,
    "bagian": 0.9615,
}


def kendali_deteksi() -> Dict[str, Any]:
    """Kendali positif: selisih yang ADA memang tertangkap dengan angka benar."""
    status, klaim, terbaca = semesta_kendali()
    terukur = ringkas_selisih(kumpulkan(status, klaim, terbaca))
    return {
        "terukur": terukur,
        "diharapkan": dict(JAWABAN_KENDALI),
        "lolos": terukur == JAWABAN_KENDALI,
    }


def kendali_nol() -> Dict[str, Any]:
    """Kendali NOL wajib: medan identik harus menghasilkan selisih nol bersih."""
    status, klaim, _ = semesta_kendali()
    baris = kumpulkan(status, klaim, dict(klaim))
    r = ringkas_selisih(baris)
    bagian = bagian_teratas(baris)
    return {
        "cacah_berselisih": r["cacah_berselisih"],
        "jumlah_selisih_bersih": r["jumlah_selisih_bersih"],
        "bagian_teratas": bagian,
        "lolos": (
            r["cacah_berselisih"] == 0
            and r["jumlah_selisih_bersih"] == 0
            and bagian is None
        ),
    }


def kendali_negatif() -> Dict[str, Any]:
    """Kendali bahwa arah negatif TERTANGKAP, bukan dibulatkan menjadi nol."""
    status = {("DDD", "2024-03"): kehidupan.STATUS_MATI}
    klaim = {("DDD", "2024-03"): 44890}
    terbaca = {("DDD", "2024-03"): 44640}
    r = ringkas_selisih(kumpulkan(status, klaim, terbaca))
    return {
        "cacah_selisih_negatif": r["cacah_selisih_negatif"],
        "jumlah_selisih_negatif": r["jumlah_selisih_negatif"],
        "jumlah_selisih_bersih": r["jumlah_selisih_bersih"],
        "terdeteksi": (
            r["cacah_selisih_negatif"] == 1
            and r["jumlah_selisih_negatif"] == 250
            and r["jumlah_selisih_bersih"] == -250
        ),
    }


def kendali_teratas() -> Dict[str, Any]:
    """Kendali bahwa penimbang butir 2 memang menimbang sepuluh terbesar."""
    status, klaim, terbaca = semesta_teratas()
    baris = kumpulkan(status, klaim, terbaca)
    puncak = teratas(baris)
    terukur = {
        "cacah_teratas": 0 if puncak is None else len(puncak),
        "jumlah_teratas": 0 if puncak is None else sum(int(r["selisih"]) for r in puncak),
        "jumlah_positif": ringkas_selisih(baris)["jumlah_selisih_positif"],
        "bagian": bagian_teratas(baris),
    }
    return {
        "terukur": terukur,
        "diharapkan": dict(JAWABAN_TERATAS),
        "lolos": terukur == JAWABAN_TERATAS,
    }


def selisih_terhadap_warisan(ringkas: Dict[str, int]) -> Dict[str, int]:
    """Pemeriksaan, BUKAN ramalan: kesenjangan terhadap dua angka terbit."""
    return {
        "klaim_dikurangi_tercatat": int(ringkas.get("jumlah_klaim_langsung") or 0)
        - LILIN_LANGSUNG_TERCATAT,
        "terbaca_dikurangi_tercatat": int(ringkas.get("jumlah_terbaca_langsung") or 0)
        - BARIS_PARQUET_TERCATAT,
        "bersih_dikurangi_tercatat": int(ringkas.get("jumlah_selisih_bersih") or 0)
        - SELISIH_TERCATAT,
    }


def dua_jalur_bertemu(ringkas: Dict[str, int]) -> bool:
    """Bersih per baris WAJIB sama dengan selisih dua jumlah langsung."""
    kiri = int(ringkas.get("jumlah_selisih_bersih") or 0)
    kanan = int(ringkas.get("jumlah_terbaca_langsung") or 0) - int(
        ringkas.get("jumlah_klaim_langsung") or 0
    )
    return kiri == kanan


def uji_r312(
    cacah_berselisih: Optional[int],
    bagian: Optional[float],
    selisih_inv: Dict[str, int],
) -> Dict[str, Any]:
    """Adjudikasi ketiga butir terhadap pita yang dikunci di jurnal 136."""
    teradjudikasi = cacah_berselisih is not None and int(cacah_berselisih) > 0
    b1 = teradjudikasi and dalam_pita(cacah_berselisih, R312_PITA_BUTIR_1)
    b2 = teradjudikasi and dalam_pita_pecahan(bagian, R312_PITA_BUTIR_2)
    b3 = len(selisih_inv) == len(INVARIAN) and all(
        int(v) == 0 for v in selisih_inv.values()
    )
    return {
        "teradjudikasi": bool(teradjudikasi),
        "butir_1": {
            "pertanyaan": "cacah simbol-bulan yang selisihnya bukan nol",
            "satuan": "simbol-bulan",
            "pita": list(R312_PITA_BUTIR_1),
            "terukur": cacah_berselisih,
            "berisiko": True,
            "menang": bool(b1),
        },
        "butir_2": {
            "pertanyaan": (
                "bagian sepuluh baris berselisih positif terbesar terhadap "
                "jumlah seluruh selisih positif"
            ),
            "satuan": "bagian antara 0 dan 1",
            "pita": list(R312_PITA_BUTIR_2),
            "terukur": bagian,
            "berisiko": True,
            "menang": bool(b2),
        },
        "butir_3": {
            "pertanyaan": "kedelapan invarian semesta terbaca ulang identik",
            "satuan": "cocok atau tidak",
            "berisiko": False,
            "mudah": True,
            "menang": bool(b3),
        },
        "cacah_menang_berisiko": int(bool(b1)) + int(bool(b2)),
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
    selisih_inv = ringkasan.get("selisih_invarian") or {}
    if len(selisih_inv) != len(INVARIAN):
        return 2
    if any(int(v) != 0 for v in selisih_inv.values()):
        return 2
    if int(ringkasan.get("cacah_baris_tanpa_klaim") or 0) > 0:
        return 2
    if int(ringkasan.get("cacah_baris_tanpa_terbaca") or 0) > 0:
        return 2
    if int(ringkasan.get("cacah_berselisih") or 0) <= 0:
        return 2
    if not ringkasan.get("dua_jalur_bertemu"):
        return 2
    if not ringkasan.get("kendali_deteksi_lolos"):
        return 2
    if not ringkasan.get("kendali_nol_lolos"):
        return 2
    if not ringkasan.get("kendali_negatif_terdeteksi"):
        return 2
    if not ringkasan.get("kendali_teratas_lolos"):
        return 2
    return 0


def jalankan(akar: str = ".", total: Optional[int] = None) -> Dict[str, Any]:
    total = TOTAL_PECAHAN if total is None else int(total)
    status, byte_parquet, meta = silang_funding.baca_laporan_kehidupan(
        akar=akar, total=total
    )
    klaim, meta_klaim = silang_funding.baca_medan_baris(
        akar=akar, total=total, medan=MEDAN_KLAIM
    )
    galat_medan = None
    try:
        terbaca, meta_terbaca = silang_funding.baca_medan_baris(
            akar=akar, total=total, medan=MEDAN_TERBACA
        )
    except Exception as e:  # syarat gugur 1: medan tidak ada
        terbaca, meta_terbaca = {}, {}
        galat_medan = "%s: %s" % (type(e).__name__, e)

    baris = kumpulkan(status, klaim, terbaca)
    r = ringkas_selisih(baris)
    beda = baris_berselisih(baris)
    bagian = bagian_teratas(baris)
    terukur = invarian_terukur(status, byte_parquet)
    selisih_inv = selisih_invarian(terukur)
    det = kendali_deteksi()
    nol = kendali_nol()
    neg = kendali_negatif()
    tas = kendali_teratas()

    ringkasan: Dict[str, Any] = {
        "invarian_terukur": terukur,
        "invarian_tercatat": dict(INVARIAN),
        "selisih_invarian": selisih_inv,
        "bagian_teratas": bagian,
        "sebaran_kelas": sebaran_kelas(baris),
        "selisih_terhadap_warisan": selisih_terhadap_warisan(r),
        "galat_medan_terbaca": galat_medan,
        "meta_medan_terbaca": meta_terbaca,
        "kendali_deteksi_lolos": bool(det.get("lolos")),
        "kendali_nol_lolos": bool(nol.get("lolos")),
        "kendali_negatif_terdeteksi": bool(neg.get("terdeteksi")),
        "kendali_teratas_lolos": bool(tas.get("lolos")),
    }
    ringkasan.update(r)
    ringkasan.update(meta)
    ringkasan.update(meta_klaim)
    ringkasan["dua_jalur_bertemu"] = dua_jalur_bertemu(r)
    ringkasan["uji_r312"] = uji_r312(r["cacah_berselisih"], bagian, selisih_inv)

    return {
        "bukan_bukti": False,
        "versi_selisih_lilin": VERSI,
        "sidik_kode": sidik_kode(),
        "sumber": daftar_sumber(total),
        "definisi": {
            "selisih": "cacah_lilin_terbaca dikurangi cacah_lilin; null bila salah satu tak ada",
            "berselisih": "selisih bukan nol, arah mana pun",
            "jumlah_selisih_negatif": "jumlah BESARAN selisih negatif, bertanda positif",
            "bagian_teratas": (
                "jumlah sepuluh selisih positif terbesar dibagi jumlah seluruh "
                "selisih positif; null bila baris positif kurang dari sepuluh"
            ),
            "jalur_langsung": (
                "seluruh jumlah dihitung dari baris, bukan dari total per kelas status"
            ),
        },
        "baris_berselisih": potong(beda),
        "cacah_baris_berselisih_penuh": len(beda),
        "batas_baris_laporan": BATAS_BARIS_LAPORAN,
        "kendali_deteksi": det,
        "kendali_nol": nol,
        "kendali_negatif": neg,
        "kendali_teratas": tas,
        "ringkasan": ringkasan,
        "catatan_harga": (
            "laporan kehidupan TIDAK menyimpan harga maupun cap waktu per menit; "
            "modul ini tidak dapat mengatakan lilin MANA yang hilang, hanya "
            "berapa dan di baris mana"
        ),
        "catatan_lantai": (
            "bila cacah berselisih mendarat tepat di 12, kesamaannya dengan dugaan "
            "12 bulan karantina DILARANG dibaca sebagai konfirmasi"
        ),
        "catatan_tepi": (
            "kemenangan yang menempel tepi pita DILARANG dibaca sebagai kalibrasi "
            "yang membaik (KC-51)"
        ),
        "catatan_penggugur": (
            "selisih invarian bukan nol, baris tanpa medan, medan identik di seluruh "
            "baris, dua jalur tidak bertemu, atau salah satu kendali gagal "
            "membatalkan seluruh angka; butir lalu dicatat TIDAK TERADJUDIKASI, "
            "bukan MELESET (aturan 24, 41)"
        ),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def berkas_ringkas(laporan: Dict[str, Any], teks_sumber: str) -> Dict[str, Any]:
    """Aturan 52: ringkasan yang terbaca UTUH dalam satu bacaan."""
    byte_sumber = teks_sumber.encode("utf-8")
    return {
        "versi_selisih_lilin": laporan.get("versi_selisih_lilin"),
        "sidik_kode": laporan.get("sidik_kode"),
        "berkas_sumber": KELUARAN,
        "byte_sumber": len(byte_sumber),
        "sidik_sumber": hashlib.sha256(byte_sumber).hexdigest(),
        "definisi": laporan.get("definisi"),
        "ringkasan": laporan.get("ringkasan"),
        "catatan_harga": laporan.get("catatan_harga"),
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
