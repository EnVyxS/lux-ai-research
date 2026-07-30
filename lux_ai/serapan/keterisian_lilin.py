"""Ukur KETERISIAN lilin per simbol-bulan — berapa lilin yang benar-benar ada.

ADR-A016 kep. 7 memindahkan prioritas ke pertanyaan yang tiga giliran berturut
tidak terjawab: **apa ISI berkas bulan MATI**. Bulan MATI bukan bulan KOSONG;
yang sudah terukur hanyalah bahwa transaksinya nol dan berkasnya besar
(579.041.399 byte atas 1.401 simbol-bulan). Apa yang mengisi byte itu belum
pernah dilihat.

`kehidupan_arsip.ukur_kolom` ternyata sudah menulis `cacah_lilin` untuk SETIAP
simbol-bulan ke `reports/kehidupan_arsip_<0..7>.json`. Artinya keterisian dapat
diukur dari laporan yang SUDAH di-commit — tanpa unduhan, tanpa aset rilis,
tanpa menyentuh parquet. Satu job ringan cukup.

## Batas yang wajib disebut di muka

Laporan kehidupan menyimpan CACAH lilin, cacah volume nol, dan transaksi. Ia
TIDAK menyimpan harga. Karena itu dugaan "harga beku" atau "lilin datar" TIDAK
dapat diuji oleh modul ini dan DILARANG disimpulkan darinya.

Besar berkas tetap DILARANG dipakai sebagai detektor status ke arah mana pun
(ADR-A015 kep. 5). Modul ini mengukur lilin, bukan membalik larangan itu.

## Aritmetika implikasi yang membunuh rancangan pertama (aturan 83)

Rancangan pertama adalah "cacah baris MATI berlilin PENUH berada dalam pita
1.150..1.401". Sebelum dikunci, implikasinya dihitung:

- rata lilin sebulan kalender = 365,25 / 12 x 1440 = 43.830;
- bila seluruh 19.586 simbol-bulan penuh: 858.454.380 lilin;
- total baris parquet semesta yang TERUKUR: 839.842.134;
- defisit seluruh semesta: 18.612.246 lilin;
- bila 787 bulan pertama rata-rata terisi separuh (nisbah byte 0,527179 dari
  R-309), sumbangannya sendiri 17.247.105 lilin, yakni 92,7% defisit semesta;
- sisa untuk 18.799 baris bukan-pertama hanya 1.365.141 lilin.

Dengan sisa sekecil itu, cacah baris MATI berlilin penuh sudah tertentu di
1.370..1.401. Pita itu bukan ramalan berisiko, jadi porosnya dipindahkan. Dua
butir lain ikut dibuang karena sebab yang sama: "cacah baris MATI ber-cacah_lilin
< 1440" (byte minimum MATI 97.634 dibagi 9,43 byte/lilin sudah memaksa jawabnya
nol) dan "nisbah byte per lilin MATI:HIDUP" (tersirat 0,233 bila butir lilin
penuh benar, jadi tidak bebas).

Angka 9,43 dan 40,43 byte per lilin adalah TAKSIRAN turunan dari anggapan
keterisian penuh, BUKAN pengukuran. Bila modul ini mengukurnya, yang berlaku
adalah angka modul.

## Tautologi yang dihindari (aturan 82, KC-48)

1. "Bulan MATI bertransaksi nol" mengulang definisi `transaksi_total == 0`.
2. "Setiap lilin di bulan MATI bertrades nol" dipaksa aritmetika: trades tak
   pernah negatif, jadi jumlah nol memaksa setiap suku nol.
3. "Bulan MATI punya sedikitnya satu lilin" dipaksa `klasifikasi`, yang melempar
   TAK_TERUKUR bila `cacah_lilin` kosong.

Ketiganya dibuang sebelum menjadi butir.

## Definisi, ditulis SEBELUM pengukuran

- `lilin_penuh(bulan)` = jumlah hari kalender bulan itu x 1440. Februari kabisat
  dihitung benar lewat `calendar.monthrange`, bukan lewat rata-rata 43.830.
- `defisit(baris)` = `lilin_penuh(bulan)` - `cacah_lilin`.
- `penuh(baris)` bila defisitnya tepat nol, tanpa toleransi.
- Defisit negatif TIDAK dijumlahkan; ia dicacah tersendiri sebagai
  `cacah_defisit_negatif` dan menggugurkan laporan, sebab bulan dengan lilin
  lebih banyak daripada kalendernya berarti definisi ini salah, bukan temuan.
- Penyebut eksplisit: 19.586 simbol-bulan yang LOLOS gerbang, BUKAN 19.598
  (aturan 30, 44).

## Praregistrasi R-310 — pita TERKUNCI di jurnal 131 sebelum modul ini ada

- **Butir 1 (BERISIKO)** — di antara 1.401 simbol-bulan MATI, cacah baris yang
  TIDAK penuh berada dalam pita **1..120** inklusif. Satuan: SIMBOL-BULAN.
  Batas defisit di atas membatasi TOTAL lilin yang hilang, bukan JUMLAH BARIS
  yang kehilangannya: 1.365.141 lilin dapat berwujud 3 baris nyaris kosong, 31
  baris kosong penuh, atau 500 baris yang masing-masing kurang 2.700 lilin.
  Gugur ke bawah bila hasilnya 0, gugur ke atas bila lebih dari 120.
- **Butir 2 (BERISIKO, bebas dari butir 1)** — `defisit_bukan_pertama` dibagi
  `defisit_total` berada dalam pita **0,02..0,25**. Satuan: BAGIAN antara 0 dan
  1, bukan persen (aturan 47). Taksiran 0,073 berdiri di atas anggapan yang
  BELUM diukur, yakni bahwa bulan pertama terisi separuh; anggapan itulah yang
  butir ini uji. Butir 1 mencacah BARIS di kelas MATI, butir 2 menimbang LILIN
  di seluruh semesta menurut pembelahan pertama/bukan-pertama.
- **Butir 3 (MUDAH, dinyatakan mudah di muka)** — kedelapan invarian semesta
  terbaca ulang identik. Deterministik, TIDAK masuk papan skor.

Tidak satu pun butir memakai klausa ATAU (usulan aturan 84). Pita tidak boleh
disentuh sesudah laporan dibaca (aturan 29).

## Jalur LANGSUNG (calon KC-50)

`total_byte` dan `jumlah_lilin_langsung` dijumlah LANGSUNG dari baris, bukan
dijumlah dari byte per kelas status. Ini pelajaran dari cacat `irisan_byte`,
yang melaporkan sembilan medan selisih padahal satu di antaranya turunan dari
delapan lainnya sehingga tidak bebas.

Aturan yang mengikat: 21, 22, 24, 29, 30, 38, 41, 44, 46, 47, 50, 52, 53, 57,
66, 79, 82, 83.
"""

from __future__ import annotations

import calendar
import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from . import kehidupan, kehidupan_arsip, kohort_ekor, silang_funding

VERSI = 1
TOTAL_PECAHAN = kehidupan_arsip.TOTAL_PECAHAN
KELUARAN = "reports/keterisian_lilin.json"
KELUARAN_RINGKAS = "reports/keterisian_lilin_ringkas.json"

# Aturan 52: laporan yang tak terbaca utuh sama dengan tidak ada.
BATAS_BARIS_LAPORAN = 40

MENIT_PER_HARI = 1440
MEDAN_LILIN = "cacah_lilin"
KENDALI_SIMBOL = "BTCUSDT"
KENDALI_CACAH = 3

# Ambang yang sudah diterbitkan R-308/R-309; dipakai apa adanya, tidak diubah.
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

# Pita R-310, TERKUNCI di jurnal 131 (aturan 29). Dilarang disentuh.
R310_PITA_BUTIR_1 = (1, 120)
R310_PITA_BUTIR_2 = (0.02, 0.25)

BERKAS_DICAP = [
    "kehidupan.py",
    "kehidupan_arsip.py",
    "keterisian_lilin.py",
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


def hari_dalam_bulan(bulan: str) -> int:
    """Hari kalender sebenarnya, termasuk Februari kabisat."""
    teks = str(bulan)
    if len(teks) != 7 or teks[4] != "-":
        raise ValueError("bulan cacat: %r" % (bulan,))
    tahun = int(teks[:4])
    bln = int(teks[5:])
    if not 1 <= bln <= 12:
        raise ValueError("bulan cacat: %r" % (bulan,))
    return int(calendar.monthrange(tahun, bln)[1])


def lilin_penuh(bulan: str) -> int:
    return hari_dalam_bulan(bulan) * MENIT_PER_HARI


def defisit(cacah_lilin: Optional[int], bulan: str) -> Optional[int]:
    """Null bila cacah lilin tidak ada; ketiadaan TIDAK ditebak sebagai nol."""
    if cacah_lilin is None:
        return None
    return lilin_penuh(bulan) - int(cacah_lilin)


def peta_bulan_pertama(status: Dict[Kunci, str]) -> Dict[str, str]:
    """Bulan terkecil DI DALAM penyebut, bukan bulan pertama di bursa.

    Batas tafsir ini diputuskan di ADR-A016 kep. 6 dan tidak boleh dilebarkan.
    """
    per_simbol = silang_funding.bulan_per_simbol(status)
    return {s: b[0] for s, b in per_simbol.items() if b}


def kumpulkan(
    status: Dict[Kunci, str], lilin: Dict[Kunci, Any]
) -> List[Dict[str, Any]]:
    """Satu baris per simbol-bulan, urutan deterministik."""
    pertama = peta_bulan_pertama(status)
    baris: List[Dict[str, Any]] = []
    for k in sorted(status):
        simbol, bulan = k
        n = lilin.get(k)
        baris.append(
            {
                "simbol": simbol,
                "bulan": bulan,
                "status": str(status[k]),
                "cacah_lilin": None if n is None else int(n),
                "lilin_penuh": lilin_penuh(bulan),
                "defisit": defisit(n, bulan),
                "pertama": pertama.get(simbol) == bulan,
            }
        )
    return baris


def ringkas_defisit(baris: List[Dict[str, Any]]) -> Dict[str, int]:
    """Jalur LANGSUNG: dijumlah dari baris, bukan dari total per kelas."""
    total = pertama = bukan_pertama = 0
    negatif = tanpa_lilin = 0
    lilin_langsung = 0
    for r in baris:
        n = r.get("cacah_lilin")
        if n is None:
            tanpa_lilin += 1
            continue
        lilin_langsung += int(n)
        d = r.get("defisit")
        d = 0 if d is None else int(d)
        if d < 0:
            negatif += 1
            continue
        total += d
        if r.get("pertama"):
            pertama += d
        else:
            bukan_pertama += d
    return {
        "defisit_total": total,
        "defisit_pertama": pertama,
        "defisit_bukan_pertama": bukan_pertama,
        "jumlah_lilin_langsung": lilin_langsung,
        "cacah_defisit_negatif": negatif,
        "cacah_baris_tanpa_lilin": tanpa_lilin,
    }


def baris_mati_tak_penuh(baris: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    keluar = [
        r
        for r in baris
        if r.get("status") == kehidupan.STATUS_MATI
        and r.get("defisit") is not None
        and int(r["defisit"]) != 0
    ]
    keluar.sort(key=lambda r: (-int(r["defisit"]), r["simbol"], r["bulan"]))
    return keluar


def cacah_mati_tak_penuh(baris: List[Dict[str, Any]]) -> int:
    return len(baris_mati_tak_penuh(baris))


def cacah_mati_penuh(baris: List[Dict[str, Any]]) -> int:
    return sum(
        1
        for r in baris
        if r.get("status") == kehidupan.STATUS_MATI
        and r.get("defisit") is not None
        and int(r["defisit"]) == 0
    )


def bagian_defisit_bukan_pertama(ringkas: Dict[str, int]) -> Optional[float]:
    """Aturan 41/46: penyebut nol menghasilkan null, bukan nol."""
    total = int(ringkas.get("defisit_total") or 0)
    if not total:
        return None
    return kohort_ekor.bagian(int(ringkas.get("defisit_bukan_pertama") or 0), total)


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


def kendali_data(
    status: Dict[Kunci, str],
    byte_parquet: Dict[Kunci, int],
    cacah: int = KENDALI_CACAH,
) -> List[Dict[str, Any]]:
    """Kendali positif (aturan 50): tiga bulan BTCUSDT berparquet terbesar."""
    calon = sorted(
        ((k, int(byte_parquet.get(k) or 0)) for k in status if k[0] == KENDALI_SIMBOL),
        key=lambda kv: (-kv[1], kv[0][1]),
    )
    return [
        {
            "simbol": k[0],
            "bulan": k[1],
            "byte_parquet": b,
            "status": status.get(k),
            "cacah_lilin": None,
        }
        for k, b in calon[: int(cacah)]
    ]


def kendali_data_sah(kendali: List[Dict[str, Any]]) -> bool:
    return len(kendali) == KENDALI_CACAH and all(
        r.get("status") == kehidupan.STATUS_HIDUP for r in kendali
    )


def semesta_kendali() -> Tuple[Dict[Kunci, str], Dict[Kunci, int]]:
    """Semesta buatan kecil yang jawabannya sudah dihitung TANGAN."""
    status = {
        ("AAA", "2024-01"): kehidupan.STATUS_HIDUP,
        ("AAA", "2024-02"): kehidupan.STATUS_MATI,
        ("BBB", "2023-02"): kehidupan.STATUS_MATI,
        ("CCC", "2025-04"): kehidupan.STATUS_MATI,
        ("CCC", "2025-05"): kehidupan.STATUS_MATI,
    }
    lilin = {
        ("AAA", "2024-01"): 44640,
        ("AAA", "2024-02"): 41760,
        ("BBB", "2023-02"): 40000,
        ("CCC", "2025-04"): 43000,
        ("CCC", "2025-05"): 44000,
    }
    return status, lilin


# Dihitung tangan: Jan 2024 penuh 44.640 (defisit 0); Feb 2024 kabisat penuh
# 41.760 (defisit 0); Feb 2023 penuh 40.320 (defisit 320, pertama); Apr 2025
# penuh 43.200 (defisit 200, pertama); Mei 2025 penuh 44.640 (defisit 640,
# bukan pertama). Total defisit 1.160; pertama 520; bukan pertama 640;
# bagian 640/1.160 = 0,5517; lilin langsung 213.400; MATI tak penuh 3.
JAWABAN_KENDALI = {
    "cacah_mati_tak_penuh": 3,
    "cacah_mati_penuh": 1,
    "defisit_total": 1160,
    "defisit_pertama": 520,
    "defisit_bukan_pertama": 640,
    "jumlah_lilin_langsung": 213400,
    "cacah_defisit_negatif": 0,
    "bagian_defisit_bukan_pertama": 0.5517,
}


def kendali_deteksi() -> Dict[str, Any]:
    status, lilin = semesta_kendali()
    baris = kumpulkan(status, lilin)
    r = ringkas_defisit(baris)
    terukur = {
        "cacah_mati_tak_penuh": cacah_mati_tak_penuh(baris),
        "cacah_mati_penuh": cacah_mati_penuh(baris),
        "defisit_total": r["defisit_total"],
        "defisit_pertama": r["defisit_pertama"],
        "defisit_bukan_pertama": r["defisit_bukan_pertama"],
        "jumlah_lilin_langsung": r["jumlah_lilin_langsung"],
        "cacah_defisit_negatif": r["cacah_defisit_negatif"],
        "bagian_defisit_bukan_pertama": bagian_defisit_bukan_pertama(r),
    }
    return {
        "terukur": terukur,
        "diharapkan": dict(JAWABAN_KENDALI),
        "lolos": terukur == JAWABAN_KENDALI,
    }


def kendali_negatif() -> Dict[str, Any]:
    """Kendali bahwa defisit negatif benar-benar TERTANGKAP, bukan tersembunyi."""
    status = {("DDD", "2024-03"): kehidupan.STATUS_MATI}
    lilin = {("DDD", "2024-03"): 44641}
    r = ringkas_defisit(kumpulkan(status, lilin))
    return {
        "cacah_defisit_negatif": r["cacah_defisit_negatif"],
        "terdeteksi": r["cacah_defisit_negatif"] == 1,
    }


def uji_r310(
    cacah_tak_penuh: Optional[int],
    bagian_bukan_pertama: Optional[float],
    selisih: Dict[str, int],
) -> Dict[str, Any]:
    """Adjudikasi ketiga butir terhadap pita yang dikunci di jurnal 131."""
    b1 = dalam_pita(cacah_tak_penuh, R310_PITA_BUTIR_1)
    b2 = dalam_pita_pecahan(bagian_bukan_pertama, R310_PITA_BUTIR_2)
    b3 = len(selisih) == len(INVARIAN) and all(int(v) == 0 for v in selisih.values())
    return {
        "butir_1": {
            "pertanyaan": "cacah simbol-bulan MATI yang lilinnya TIDAK penuh",
            "satuan": "simbol-bulan",
            "pita": list(R310_PITA_BUTIR_1),
            "terukur": cacah_tak_penuh,
            "berisiko": True,
            "menang": b1,
        },
        "butir_2": {
            "pertanyaan": "defisit_bukan_pertama dibagi defisit_total",
            "satuan": "bagian antara 0 dan 1",
            "pita": list(R310_PITA_BUTIR_2),
            "terukur": bagian_bukan_pertama,
            "berisiko": True,
            "menang": b2,
        },
        "butir_3": {
            "pertanyaan": "kedelapan invarian semesta terbaca ulang identik",
            "satuan": "cocok atau tidak",
            "berisiko": False,
            "mudah": True,
            "menang": b3,
        },
        "cacah_menang_berisiko": int(b1) + int(b2),
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
    selisih = ringkasan.get("selisih_invarian") or {}
    if len(selisih) != len(INVARIAN):
        return 2
    if any(int(v) != 0 for v in selisih.values()):
        return 2
    if int(ringkasan.get("cacah_defisit_negatif") or 0) > 0:
        return 2
    if int(ringkasan.get("cacah_baris_tanpa_lilin") or 0) > 0:
        return 2
    if not ringkasan.get("kendali_data_sah"):
        return 2
    if not ringkasan.get("kendali_deteksi_lolos"):
        return 2
    if not ringkasan.get("kendali_negatif_terdeteksi"):
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

    baris = kumpulkan(status, lilin)
    r = ringkas_defisit(baris)
    tak_penuh = baris_mati_tak_penuh(baris)
    terukur = invarian_terukur(status, byte_parquet)
    selisih = selisih_invarian(terukur)
    bagian = bagian_defisit_bukan_pertama(r)
    kd = kendali_data(status, byte_parquet)
    for baris_kendali in kd:
        baris_kendali["cacah_lilin"] = lilin.get(
            (baris_kendali["simbol"], baris_kendali["bulan"])
        )
    det = kendali_deteksi()
    neg = kendali_negatif()

    ringkasan: Dict[str, Any] = {
        "invarian_terukur": terukur,
        "invarian_tercatat": dict(INVARIAN),
        "selisih_invarian": selisih,
        "cacah_mati_tak_penuh": len(tak_penuh),
        "cacah_mati_penuh": cacah_mati_penuh(baris),
        "bagian_defisit_bukan_pertama": bagian,
        "kendali_data": kd,
        "kendali_data_sah": kendali_data_sah(kd),
        "kendali_deteksi_lolos": bool(det.get("lolos")),
        "kendali_negatif_terdeteksi": bool(neg.get("terdeteksi")),
    }
    ringkasan.update(r)
    ringkasan.update(meta)
    ringkasan.update(meta_lilin)
    ringkasan["uji_r310"] = uji_r310(len(tak_penuh), bagian, selisih)

    return {
        "bukan_bukti": False,
        "versi_keterisian_lilin": VERSI,
        "sidik_kode": sidik_kode(),
        "sumber": daftar_sumber(total),
        "definisi": {
            "lilin_penuh": "hari kalender bulan itu dikali 1440 menit",
            "defisit": "lilin_penuh dikurangi cacah_lilin; null bila lilin tak ada",
            "penuh": "defisit tepat nol, tanpa toleransi",
            "pertama": "bulan terkecil simbol itu DI DALAM penyebut 19.586",
            "jumlah_lilin_langsung": (
                "dijumlah LANGSUNG dari baris, bukan dari total per kelas status"
            ),
        },
        "baris_mati_tak_penuh": potong(tak_penuh),
        "cacah_baris_mati_tak_penuh_penuh": len(tak_penuh),
        "batas_baris_laporan": BATAS_BARIS_LAPORAN,
        "ringkasan": ringkasan,
        "catatan_harga": (
            "laporan kehidupan TIDAK menyimpan harga; dugaan harga beku atau "
            "lilin datar TIDAK diuji di sini dan dilarang disimpulkan"
        ),
        "catatan_byte": (
            "besar berkas tetap dilarang dipakai sebagai detektor status ke arah "
            "mana pun (ADR-A015 kep. 5); modul ini mengukur lilin, bukan "
            "membalik larangan itu"
        ),
        "catatan_taksiran": (
            "angka 9,43 dan 40,43 byte per lilin di jurnal 131 adalah TAKSIRAN "
            "turunan dari anggapan keterisian penuh, bukan pengukuran"
        ),
        "catatan_penggugur": (
            "selisih invarian bukan nol, defisit negatif, baris tanpa cacah_lilin, "
            "atau salah satu kendali gagal membatalkan seluruh angka; ketiga "
            "butir lalu dicatat TIDAK TERADJUDIKASI, bukan MELESET (aturan 24)"
        ),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def berkas_ringkas(laporan: Dict[str, Any], teks_sumber: str) -> Dict[str, Any]:
    """Aturan 52: ringkasan yang terbaca UTUH dalam satu bacaan."""
    byte_sumber = teks_sumber.encode("utf-8")
    return {
        "versi_keterisian_lilin": laporan.get("versi_keterisian_lilin"),
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
