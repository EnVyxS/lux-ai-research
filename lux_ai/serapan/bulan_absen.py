"""Bulan ABSEN — rentang riwayat lawan cacah bulan yang benar-benar lolos.

Jurnal 113 §6 menemukan gejala yang belum pernah diukur atas semesta: bagi
sebagian nama, `bulan_terakhir - bulan_pertama + 1` (rentang kalender) LEBIH
BESAR daripada `cacah_bulan_lolos`. Selisihnya adalah bulan yang berada DI
DALAM riwayat sebuah simbol namun tidak ada di penyebut 19.586. Bulan itu
saya sebut **bulan ABSEN**, dan namanya sengaja dibedakan dari dua homonim yang
sudah dipakai di repo ini (aturan 69, KC-36):

- **lubang funding** — bulan punya klines tetapi tidak punya fundingRate
  (`silang_funding.lubang_funding`). Bulan itu ADA di penyebut.
- **lubang tengah** — lubang funding yang bentuknya bukan awal maupun ekor
  (`silang_funding.bentuk_lubang_lokal`). Bulan itu juga ADA di penyebut.
- **bulan ABSEN** — bulan yang TIDAK ADA di penyebut sama sekali, padahal
  terletak di antara bulan pertama dan bulan terakhir simbol itu. Ini yang
  diukur modul ini, dan ia bukan salah satu dari dua yang di atas.

Tabel jurnal 113 §6 dihitung dengan tangan atas 15 pasangan SETTLED saja, dari
medan `baris` laporan `silang_settled.json`. Jumlahnya 12. Yang BELUM pernah
diukur adalah jumlah bulan absen atas SELURUH nama penyebut — dan tepat itulah
yang diramalkan R-288 butir 3. Modul ini adalah alat ukurnya.

## Mengapa modul ini MENGIMPOR, bukan memecah (preseden jurnal 111 §5)

`silang_funding.py` sudah 705 baris dan `sidik_kode`-nya tertanam di banyak
laporan yang sudah di-commit; memindahkan fungsi keluar darinya akan mengubah
sidik itu dan membatalkan pembandingan dengan laporan lama. Modul ini karena itu
mengimpor `baca_laporan_kehidupan` dan `bulan_per_simbol` apa adanya, mengimpor
`PASANGAN_SETTLED` dari `silang_settled`, dan tidak menyalin satu pun
definisinya (aturan 36).

## Modul ini tidak menyentuh jaringan

Seluruh bahannya sudah di-commit: `reports/kehidupan_arsip_<0..7>.json`. Tidak
ada unduhan, tidak ada aset rilis, tidak ada listing baru. Satu job ringan cukup.

## Medan pembeda: "tak diterbitkan arsip" lawan "gagal gerbang"

Bulan ABSEN dapat lahir dari dua sebab yang sangat berbeda:

1. **gagal_gerbang** — bulan itu ADA di manifes (arsip menerbitkannya) tetapi
   tidak lolos gerbang 1m, sehingga ia masuk karantina dan bukan penyebut. Dua
   belas simbol-bulan karantina semesta adalah kandidat kelas ini.
2. **tak_diterbitkan_arsip** — bulan itu tidak ada di manifes sama sekali; arsip
   tidak pernah menerbitkan bulan itu bagi simbol tersebut.

Pembeda ini dibaca dari manifes lewat `pulihkan.nama_manifes(i)`, dan
STRUKTURNYA tidak ditebak: medan `manifes[].simbol` dan `manifes[].bulan` sudah
terbaca di `kehidupan_arsip.peta_parquet`. Bila manifes tidak lengkap di pohon
kerja, seluruh pembeda menjadi `tak_terukur` dan itu BUKAN penggugur —
ketiadaan pengukuran bukan ketiadaan gejala (aturan 59). Yang gugur hanyalah hak
menyebut sebabnya, bukan cacah absennya.

## Kendali positif (aturan 50)

Kesimpulan di sini bersandar pada KETIADAAN bulan di penyebut. Tanpa kendali,
penyebut yang terbaca separuh akan tampak sebagai "absen di mana-mana".
Kendalinya dipilih sebelum satu angka pun dilihat: **BTCUSDT dan ETHUSDT wajib
ada, wajib berbulan >= 60, dan wajib berabsen 0**. Bila satu saja gagal,
`kendali_sah` false, kode keluar 2, dan seluruh angka absen batal.

## Ramalan yang MELESET tidak boleh membatalkan laporan

`kode_keluar` sengaja TIDAK memeriksa satu pun medan `uji_r288`. Laporan yang
menggugurkan dirinya ketika ramalannya kalah adalah laporan yang tidak dapat
mengalahkan penulisnya. Yang menggugurkan hanyalah cacat bahan baku:
`sidik_seragam`, laporan pecahan kurang, kunci ganda, `kendali_sah`,
`selisih_penyebut`, dan `cacah_pasangan` (aturan 24).

Demikian pula `selisih_absen_pasangan_jurnal_113` — selisih jumlah absen 15
pasangan terhadap 12 yang dihitung tangan di jurnal 113 — dilapor sebagai
KETERANGAN, bukan penggugur, sebab justru itulah yang sedang diuji (aturan 72).

## Praregistrasi ramalan

- **R-288** (sudah dipraregistrasi di jurnal 113 §8; disalin apa adanya, bunyinya
  DILARANG diubah oleh modul ini):
  1. tepat **9** dari 15 pasangan berbulan-absen SATU, dan persisnya AERGOUSDT,
     AIAUSDT, CTKUSDT, CVCUSDT, CVXUSDT, LITUSDT, MAVIAUSDT, PUMPUSDT, SLPUSDT;
     BNXUSDT berabsen **3**; lima sisanya (BDXNUSDT, ICPUSDT, MINAUSDT,
     SXPUSDT, TLMUSDT) berabsen **0**. Butir ini **MUDAH** — ia hanya menyalin
     tabel jurnal 113 §6 yang sudah dihitung dari laporan yang sama.
  2. bagi **>= 7 dari 9** pasangan berabsen-satu, bulan absennya SAMA PERSIS
     dengan `bulan_settled_terakhir`. **BERISIKO.** GUGUR bila <= 6.
  3. jumlah bulan absen atas SELURUH nama penyebut = **12**, yakni tidak ada
     satu pun bulan absen di luar 15 pasangan SETTLED. **BERISIKO BESAR** — 787
     nama belum pernah diukur dengan definisi ini, dan aturan 74 mengikat: nol
     di luar pasangan adalah dugaan, bukan angka terbitan.
- **R-290** — CI pada commit yang menyentuh `tests/test_bulan_absen.py`
  mengumpulkan **694 butir** dengan kode keluar **0**. Dasar (aturan 54, 56, 57;
  dicacah dari berkas uji yang sudah SELESAI ditulis): 662 butir terverifikasi
  tiga kali berturut-turut pada `reports/ci_terakhir.json` (commit `3d113d49`,
  `9e4226ca`, `57bac8ae`), ditambah **32** fungsi `def test_` baru tanpa satu pun
  `parametrize`. 662 + 32 = 694. Satuan: BUTIR yang dikumpulkan pytest. Ramalan
  ini **MUDAH** dan saya menyebutnya begitu.

Aturan yang mengikat: 10, 16, 20, 21, 22, 24, 30, 36, 44, 45, 46, 50, 52, 53,
54, 56, 57, 59, 66, 69, 70, 72, 73, 74, 75.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from . import kehidupan_arsip, pulihkan, silang_funding, silang_settled

VERSI = 1
TOTAL_PECAHAN = kehidupan_arsip.TOTAL_PECAHAN
KELUARAN = "reports/bulan_absen.json"
KELUARAN_RINGKAS = "reports/bulan_absen_ringkas.json"

# Angka terbitan yang dipakai sebagai penggugur, BUKAN sebagai masukan.
PENYEBUT_TERCATAT = 19586

# Angka terbitan yang dipakai sebagai KETERANGAN saja (aturan 72): jumlah bulan
# absen 15 pasangan SETTLED menurut hitungan tangan jurnal 113 §6.
ABSEN_PASANGAN_JURNAL_113 = 12

# Nama penyebut menurut STATE v39; keterangan, bukan penggugur (aturan 21, 59).
NAMA_PENYEBUT_TERCATAT = 787

GAGAL_GERBANG = "gagal_gerbang"
TAK_DITERBITKAN = "tak_diterbitkan_arsip"
TAK_TERUKUR = "tak_terukur"
PEMBEDA = (GAGAL_GERBANG, TAK_DITERBITKAN, TAK_TERUKUR)

# Kendali positif, dipilih sebelum satu angka pun dilihat (aturan 50).
KENDALI_NAMA: Tuple[str, ...] = ("BTCUSDT", "ETHUSDT")
KENDALI_BULAN_MIN = 60

# Pita ramalan R-288, ditulis sebagai TETAPAN agar tidak bergeser diam-diam.
R288_TUNGGAL: Tuple[str, ...] = (
    "AERGOUSDT",
    "AIAUSDT",
    "CTKUSDT",
    "CVCUSDT",
    "CVXUSDT",
    "LITUSDT",
    "MAVIAUSDT",
    "PUMPUSDT",
    "SLPUSDT",
)
R288_NOL: Tuple[str, ...] = (
    "BDXNUSDT",
    "ICPUSDT",
    "MINAUSDT",
    "SXPUSDT",
    "TLMUSDT",
)
R288_BNX = "BNXUSDT"
R288_BNX_ABSEN = 3
R288_SAMA_MIN = 7
R288_JUMLAH_SEMESTA = 12

BERKAS_DICAP = [
    "bulan_absen.py",
    "kehidupan.py",
    "kehidupan_arsip.py",
    "silang_funding.py",
    "silang_settled.py",
]

Kunci = Tuple[str, str]


def nama_keluaran() -> str:
    return KELUARAN


def nama_ringkas() -> str:
    return KELUARAN_RINGKAS


def sidik_kode() -> str:
    """Aturan 22: cap setiap berkas yang ikut menentukan angka ini."""
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(BERKAS_DICAP):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def bulan_ke_indeks(bulan: Any) -> Optional[int]:
    """'YYYY-MM' menjadi indeks bulan mutlak; bentuk cacat menghasilkan None.

    Bulan yang tak terurai TIDAK dibaca sebagai nol dan tidak diam-diam dibuang
    (aturan 16, 46); pemanggilnya wajib memutuskan apa yang dilakukan atasnya.
    """
    teks = str(bulan or "")
    if len(teks) != 7 or teks[4] != "-":
        return None
    try:
        tahun = int(teks[:4])
        bln = int(teks[5:7])
    except ValueError:
        return None
    if bln < 1 or bln > 12:
        return None
    return tahun * 12 + (bln - 1)


def indeks_ke_bulan(indeks: int) -> str:
    tahun, bln = divmod(int(indeks), 12)
    return f"{tahun:04d}-{bln + 1:02d}"


def rentang_bulan(pertama: Any, terakhir: Any) -> List[str]:
    """Seluruh bulan kalender dari `pertama` sampai `terakhir`, inklusif."""
    a = bulan_ke_indeks(pertama)
    b = bulan_ke_indeks(terakhir)
    if a is None or b is None or b < a:
        return []
    return [indeks_ke_bulan(i) for i in range(a, b + 1)]


def bulan_sah(bulan_urut: Any) -> List[str]:
    return sorted({str(b) for b in (bulan_urut or []) if bulan_ke_indeks(b) is not None})


def bulan_absen(bulan_urut: Any) -> List[str]:
    """Bulan di DALAM rentang simbol yang tidak ada di penyebut.

    Tepi tidak pernah absen menurut definisi: bulan sebelum `bulan_pertama` dan
    sesudah `bulan_terakhir` bukan bagian rentang, sehingga ketiadaannya bukan
    gejala (aturan 20).
    """
    sah = bulan_sah(bulan_urut)
    if len(sah) < 2:
        return []
    ada = set(sah)
    return [b for b in rentang_bulan(sah[0], sah[-1]) if b not in ada]


def pembeda_absen(
    simbol: Any,
    bulan: Any,
    didaftar: Optional[Dict[str, Set[str]]] = None,
    ada_manifes: bool = False,
) -> str:
    """Sebab bulan absen, bila manifes memang terbaca; bila tidak, tak_terukur."""
    if not ada_manifes or didaftar is None:
        return TAK_TERUKUR
    bulan_didaftar = didaftar.get(str(simbol)) or set()
    return GAGAL_GERBANG if str(bulan) in bulan_didaftar else TAK_DITERBITKAN


def baris_simbol(
    simbol: Any,
    bulan_urut: Any,
    didaftar: Optional[Dict[str, Set[str]]] = None,
    ada_manifes: bool = False,
) -> Dict[str, Any]:
    """Satu baris per nama; simbol tanpa bulan sah menghasilkan null, bukan nol."""
    sah = bulan_sah(bulan_urut)
    absen = bulan_absen(sah)
    pertama = sah[0] if sah else None
    terakhir = sah[-1] if sah else None
    rentang = len(rentang_bulan(pertama, terakhir)) if sah else None
    return {
        "simbol": str(simbol),
        "bulan_pertama": pertama,
        "bulan_terakhir": terakhir,
        "rentang": rentang,
        "cacah_bulan_lolos": len(sah),
        "cacah_absen": len(absen),
        "bulan_absen": absen,
        "pembeda_absen": [
            {
                "bulan": b,
                "pembeda": pembeda_absen(simbol, b, didaftar, ada_manifes),
            }
            for b in absen
        ],
        "selisih_rentang": (rentang - len(sah)) if rentang is not None else None,
        "konsisten_rentang": (
            (rentang - len(sah)) == len(absen) if rentang is not None else None
        ),
    }


def jumlah_absen(baris: List[Dict[str, Any]]) -> int:
    return sum(int(r.get("cacah_absen") or 0) for r in baris)


def sebaran_pembeda(baris: List[Dict[str, Any]]) -> Dict[str, int]:
    """Ketiga kelas pembeda dilapor walau nol (aturan 45)."""
    keluar: Dict[str, int] = {p: 0 for p in PEMBEDA}
    for r in baris:
        for x in r.get("pembeda_absen") or []:
            nama = str(x.get("pembeda"))
            keluar[nama] = keluar.get(nama, 0) + 1
    return keluar


def peta_didaftar(
    akar: str = ".", total: int = TOTAL_PECAHAN
) -> Tuple[Dict[str, Set[str]], Dict[str, Any]]:
    """Bulan yang DIDAFTAR arsip per simbol, dari manifes pecahan bila ada.

    Manifes yang tidak ada TIDAK dianggap kosong: namanya dicatat dan
    `sumber_pembeda_ada` menjadi false. Itu bukan penggugur (aturan 59).
    """
    didaftar: Dict[str, Set[str]] = {}
    hilang: List[str] = []
    dibaca = 0
    for i in range(total):
        nama = pulihkan.nama_manifes(i)
        jalur = Path(akar) / nama
        if not jalur.exists():
            hilang.append(nama)
            continue
        dibaca += 1
        isi = json.loads(jalur.read_text(encoding="utf-8"))
        for baris in isi.get("manifes") or []:
            simbol = str(baris.get("simbol") or "")
            bulan = str(baris.get("bulan") or "")
            if not simbol or not bulan:
                continue
            didaftar.setdefault(simbol, set()).add(bulan)
    meta = {
        "cacah_manifes_dibaca": dibaca,
        "manifes_hilang": hilang,
        "sumber_pembeda_ada": dibaca == total and not hilang,
        "cacah_nama_didaftar": len(didaftar),
    }
    return didaftar, meta


def baris_pasangan_settled(
    per_baris: Dict[str, Dict[str, Any]],
    pasangan: Optional[Dict[str, str]] = None,
) -> List[Dict[str, Any]]:
    """Satu baris per pasangan SETTLED; pasangan tanpa data TIDAK dibuang."""
    pasangan = dict(
        pasangan if pasangan is not None else silang_settled.PASANGAN_SETTLED
    )
    keluar: List[Dict[str, Any]] = []
    for simbol in sorted(pasangan):
        b = per_baris.get(simbol) or {}
        absen = [str(x) for x in (b.get("bulan_absen") or [])]
        bulan_settled = str(pasangan[simbol])
        keluar.append(
            {
                "simbol": simbol,
                "bulan_settled_terakhir": bulan_settled,
                "ada_di_penyebut": bool(b),
                "cacah_bulan_lolos": b.get("cacah_bulan_lolos"),
                "rentang": b.get("rentang"),
                "cacah_absen": len(absen),
                "bulan_absen": absen,
                "absen_tunggal": len(absen) == 1,
                "absen_sama_dengan_settled": bool(
                    len(absen) == 1 and absen[0] == bulan_settled
                ),
                "settled_ada_di_absen": bulan_settled in absen,
            }
        )
    return keluar


def uji_r288(
    baris_pasangan: List[Dict[str, Any]], jumlah_semesta: int
) -> Dict[str, Any]:
    """Ketiga butir R-288, masing-masing dengan penyebutnya sendiri (aturan 74)."""
    tunggal = sorted(
        str(r.get("simbol"))
        for r in baris_pasangan
        if int(r.get("cacah_absen") or 0) == 1
    )
    nol = sorted(
        str(r.get("simbol"))
        for r in baris_pasangan
        if int(r.get("cacah_absen") or 0) == 0
    )
    bnx = next(
        (
            int(r.get("cacah_absen") or 0)
            for r in baris_pasangan
            if str(r.get("simbol")) == R288_BNX
        ),
        None,
    )
    sama = sorted(
        str(r.get("simbol"))
        for r in baris_pasangan
        if r.get("absen_sama_dengan_settled")
    )
    sama_tunggal = sorted(set(sama) & set(tunggal))
    butir_1 = {
        "cacah_absen_tunggal": len(tunggal),
        "simbol_absen_tunggal": tunggal,
        "diramalkan_tunggal": sorted(R288_TUNGGAL),
        "cacah_absen_bnx": bnx,
        "diramalkan_bnx": R288_BNX_ABSEN,
        "simbol_absen_nol": nol,
        "diramalkan_nol": sorted(R288_NOL),
        "mudah": True,
        "menang": bool(
            tunggal == sorted(R288_TUNGGAL)
            and bnx == R288_BNX_ABSEN
            and nol == sorted(R288_NOL)
        ),
    }
    butir_2 = {
        "penyebut": len(tunggal),
        "cacah_sama_dengan_settled": len(sama_tunggal),
        "simbol_sama_dengan_settled": sama_tunggal,
        "ambang": R288_SAMA_MIN,
        "menang": len(sama_tunggal) >= R288_SAMA_MIN,
    }
    butir_3 = {
        "jumlah_bulan_absen_semesta": int(jumlah_semesta),
        "jumlah_bulan_absen_pasangan": sum(
            int(r.get("cacah_absen") or 0) for r in baris_pasangan
        ),
        "diramalkan": R288_JUMLAH_SEMESTA,
        "menang": int(jumlah_semesta) == R288_JUMLAH_SEMESTA,
    }
    return {
        "butir_1": butir_1,
        "butir_2": butir_2,
        "butir_3": butir_3,
        "penggugur_menyala": not butir_2["menang"],
        "r288_menang": bool(
            butir_1["menang"] and butir_2["menang"] and butir_3["menang"]
        ),
        "catatan": (
            "butir 1 MUDAH: ia menyalin tabel jurnal 113 §6 yang dihitung dari "
            "laporan yang sama; kemenangannya bukan bukti mutu ramalan"
        ),
    }


def kendali_absen(
    per_baris: Dict[str, Dict[str, Any]],
    nama: Tuple[str, ...] = KENDALI_NAMA,
    bulan_min: int = KENDALI_BULAN_MIN,
) -> List[Dict[str, Any]]:
    """Kendali positif: nama yang jelas hidup penuh wajib berabsen 0."""
    keluar: List[Dict[str, Any]] = []
    for simbol in nama:
        b = per_baris.get(simbol) or {}
        ada = bool(b)
        lolos = int(b.get("cacah_bulan_lolos") or 0) if ada else 0
        absen = int(b.get("cacah_absen") or 0) if ada else None
        keluar.append(
            {
                "simbol": simbol,
                "ada": ada,
                "cacah_bulan_lolos": lolos if ada else None,
                "cacah_absen": absen,
                "bulan_min": bulan_min,
                "sah": bool(ada and lolos >= bulan_min and absen == 0),
            }
        )
    return keluar


def kendali_sah(kendali: List[Dict[str, Any]]) -> bool:
    return bool(kendali) and all(k.get("sah") for k in kendali)


def kode_keluar(ringkasan: Dict[str, Any]) -> int:
    """Kode 2 hanya untuk cacat BAHAN BAKU; ramalan yang kalah tidak menggugurkan."""
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
    if int(ringkasan.get("selisih_penyebut") or 0) != 0:
        return 2
    if int(ringkasan.get("cacah_pasangan") or 0) != len(
        silang_settled.PASANGAN_SETTLED
    ):
        return 2
    return 0


def jalankan(akar: str = ".", total: int = TOTAL_PECAHAN) -> Dict[str, Any]:
    status, _byte_parquet, meta = silang_funding.baca_laporan_kehidupan(
        akar=akar, total=total
    )
    per_simbol = silang_funding.bulan_per_simbol(status)
    didaftar, meta_manifes = peta_didaftar(akar=akar, total=total)
    ada_manifes = bool(meta_manifes.get("sumber_pembeda_ada"))

    baris = [
        baris_simbol(simbol, per_simbol[simbol], didaftar, ada_manifes)
        for simbol in sorted(per_simbol)
    ]
    per_baris = {str(r["simbol"]): r for r in baris}
    berabsen = [r for r in baris if int(r.get("cacah_absen") or 0) > 0]
    pasangan = baris_pasangan_settled(per_baris)
    kendali = kendali_absen(per_baris)
    total_absen = jumlah_absen(baris)
    absen_pasangan = sum(int(r.get("cacah_absen") or 0) for r in pasangan)

    ringkasan: Dict[str, Any] = {
        "penyebut_kehidupan": len(status),
        "selisih_penyebut": len(status) - PENYEBUT_TERCATAT,
        "cacah_nama_penyebut": len(baris),
        "selisih_nama_penyebut": len(baris) - NAMA_PENYEBUT_TERCATAT,
        "jumlah_bulan_absen": total_absen,
        "cacah_nama_berabsen": len(berabsen),
        "jumlah_bulan_absen_pasangan": absen_pasangan,
        "selisih_absen_pasangan_jurnal_113": absen_pasangan
        - ABSEN_PASANGAN_JURNAL_113,
        "jumlah_bulan_absen_luar_pasangan": total_absen - absen_pasangan,
        "cacah_nama_tak_konsisten_rentang": sum(
            1 for r in baris if r.get("konsisten_rentang") is False
        ),
        "sebaran_pembeda": sebaran_pembeda(baris),
        "cacah_pasangan": len(pasangan),
        "kendali": kendali,
        "kendali_sah": kendali_sah(kendali),
        "uji_r288": uji_r288(pasangan, total_absen),
    }
    ringkasan.update(meta)
    ringkasan.update(meta_manifes)

    return {
        "bukan_bukti": False,
        "versi_bulan_absen": VERSI,
        "sidik_kode": sidik_kode(),
        "sidik_kode_silang_funding": silang_funding.sidik_kode(),
        "sidik_kode_silang_settled": silang_settled.sidik_kode(),
        "sumber": [kehidupan_arsip.nama_keluaran(i) for i in range(total)],
        "definisi": {
            "bulan_absen": (
                "bulan kalender di antara bulan_pertama dan bulan_terakhir "
                "sebuah simbol yang TIDAK ada di penyebut 19.586; BUKAN lubang "
                "funding dan BUKAN lubang tengah, yang keduanya ADA di "
                "penyebut (aturan 69, KC-36)"
            ),
            "rentang": "cacah bulan kalender dari bulan_pertama sampai bulan_terakhir",
            "pembeda_absen": (
                "gagal_gerbang bila bulan itu ada di manifes arsip; "
                "tak_diterbitkan_arsip bila tidak ada di manifes; tak_terukur "
                "bila manifes tidak lengkap terbaca — dan ketiadaan pengukuran "
                "BUKAN ketiadaan gejala (aturan 59)"
            ),
            "kendali": (
                "BTCUSDT dan ETHUSDT wajib ada, berbulan >= 60, dan berabsen 0"
            ),
        },
        "baris_berabsen": berabsen,
        "baris_pasangan_settled": pasangan,
        "baris": baris,
        "ringkasan": ringkasan,
        "catatan_tafsir": (
            "bulan absen membuktikan bulan itu tidak ada di penyebut, BUKAN "
            "bahwa pasarnya berhenti diperdagangkan; sebabnya baru terbedakan "
            "bila manifes terbaca, dan kecocokan dengan bulan SETTLED tetap "
            "membuktikan PENAMAAN, bukan perdagangan (KC-18, aturan 10)"
        ),
        "catatan_penggugur": (
            "yang menggugurkan hanyalah cacat bahan baku: sidik_seragam false, "
            "laporan pecahan kurang, kunci ganda, kendali_sah false, "
            "selisih_penyebut bukan nol, atau cacah_pasangan bukan 15. "
            "uji_r288 dan selisih_absen_pasangan_jurnal_113 TIDAK menggugurkan "
            "apa pun: ramalan yang kalah wajib dicatat MELESET, bukan "
            "membatalkan laporannya sendiri (aturan 24, 72)"
        ),
        "catatan_rentang": (
            "hasil berlaku bagi nama yang punya sekurang-kurangnya dua bulan "
            "lolos; nama berbulan tunggal tidak dapat berabsen menurut definisi, "
            "dan itu bukan bukti ketiadaan gejala pada nama itu (aturan 20, 59)"
        ),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def berkas_ringkas(laporan: Dict[str, Any], teks_sumber: str) -> Dict[str, Any]:
    """Aturan 52: berkas kecil yang dapat dibaca UTUH dalam satu bacaan."""
    byte_sumber = teks_sumber.encode("utf-8")
    return {
        "versi_bulan_absen": laporan.get("versi_bulan_absen"),
        "sidik_kode": laporan.get("sidik_kode"),
        "berkas_sumber": KELUARAN,
        "byte_sumber": len(byte_sumber),
        "sidik_sumber": hashlib.sha256(byte_sumber).hexdigest(),
        "definisi": laporan.get("definisi"),
        "baris_berabsen": laporan.get("baris_berabsen"),
        "baris_pasangan_settled": laporan.get("baris_pasangan_settled"),
        "ringkasan": laporan.get("ringkasan"),
        "catatan_penggugur": laporan.get("catatan_penggugur"),
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
