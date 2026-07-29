"""Penyebut PER TAHUN, dan nasib keenam bulan peralihan - satu run, empat soal.

`kebangkitan` V1 (run 30443289476) memberi sebaran 1.401 MATI menurut tahun:
2020 **1** - 2021 **9** - 2022 **34** - 2023 **103** - 2024 **192** - 2025 **506**
- 2026 **556**. Angka itu PEMBILANG tanpa penyebut. Tanpa penyebut per tahun,
kalimat seperti "kematian memuncak pada 2026" tidak berhak diucapkan: 2026 boleh
jadi hanya punya lebih banyak simbol-bulan, atau justru lebih sedikit. Aturan 20
melarang menyimpulkan di luar rentang yang terukur; modul ini mengukur
penyebutnya supaya kalimat itu boleh diadili.

Soal kedua lahir dari lubang di laporan yang sama. Pada ENAM dari delapan
peristiwa kebangkitan, bulan PERALIHAN - bulan tepat antara bulan MATI terakhir
dan bulan HIDUP pertama - TIDAK ADA di dalam penyebut 19.586: CTKUSDT 2025-04,
CVCUSDT 2025-05, CVXUSDT 2025-07, LITUSDT 2025-12, MAVIAUSDT 2025-03, SLPUSDT
2025-07. Dua sisanya (ICPUSDT, TLMUSDT) bersambung. "Tidak ada di penyebut"
bukan sebab; ia gejala. Aturan 46 menuntut medan yang MEMBEDAKAN sebab-sebab
yang mungkin, bukan satu bendera yang mengaburkannya.

**H-A013** karena itu dirumuskan tajam: bulan peralihan yang hilang itu tidak
lenyap, ia terbit di bawah NAMA LAIN. `reports/semesta_bulan_1m.json` (dibaca
utuh, blob a1a6d3f0) memuat `CTKUSDTSETTLED` 1, `CVCUSDTSETTLED` 1,
`CVXUSDTSETTLED` 1, `LITUSDTSETTLED` 1, `MAVIAUSDTSETTLED` 1, `SLPUSDTSETTLED` 1
- keenam simbol peralihan punya saudara berakhiran SETTLED dengan TEPAT SATU
bulan. Dan kedua simbol yang BERSAMBUNG punya bentuk berbeda: `ICPUSDT_SETTLED`
9 dan `TLMUSDT_SETTLED` 9. Bila bulan tunggal saudara itu sama dengan bulan
peralihan yang hilang, maka "kebangkitan" pada keenam simbol itu sebagian adalah
perkara PENAMAAN kontrak yang diselesaikan, bukan pasar yang mati lalu hidup.
Itu akan MELEMAHKAN tafsir kebangkitan, bukan menguatkannya - dan itulah sebabnya
ia wajib diuji (aturan 24, medan penggugur).

Soal ketiga: BNXUSDT punya TIGA lubang funding tengah tercatat (2022-04, 2022-06,
2022-08) dan saudara `BNXUSDTSETTLED` dengan ENAM bulan. Ketiga bulan itu
diperiksa apa adanya terhadap penyebut. Modul ini TIDAK mengklaim mencocokkannya
dengan ketiga simbol-bulan KC-15: `reports/diagnosa_kc15.json` belum dibaca utuh,
dan menuduh kecocokan tanpa membacanya adalah tepat cacat yang melahirkan KC-23.

Soal keempat: `bulan_hidup_terakhir` bagi SELURUH simbol ditulis penuh ke
laporan. `kebangkitan` V1 menghitungnya untuk 787 simbol tetapi hanya menuliskan
sepuluh perbandingan, sehingga ke-28 anggota kohort di luar sampel abjad tetap
tak terbaca. Menulis petanya penuh melunasi utang itu tanpa pengukuran baru.

## Mengapa modul BARU

`funding.py` dan `silang_funding.py` sama-sama 705 baris (aturan 48, terkunci).
`kebangkitan.py` dan `lubang_tengah.py` V2 belum diukur cacah barisnya. Seluruh
pembaca yang dibutuhkan sudah ada dan sudah diuji, jadi modul ini MEMAKAINYA:
`silang_funding.baca_laporan_kehidupan`, `lubang_funding`, `kendali_silang`,
`kendali_sah`, `kebangkitan.peta_status`, `kebangkitan.sebaran_mati_tahun`,
`kebangkitan.bulan_hidup_terakhir`. Tidak ada satu pun definisi disalin ulang
(aturan 36).

## Definisi tersurat

- `penyebut_per_tahun` = cacah simbol-bulan yang LOLOS gerbang pada tahun itu.
  Bulan yang tidak terdaftar bukan bulan MATI, melainkan bulan yang TIDAK ADA
  (aturan 30); ia tidak masuk penyebut mana pun.
- `bagian_mati` = mati tahun itu dibagi penyebut tahun itu. Penyebut nol berbunyi
  `terukur` false dan `bagian` null - BUKAN nol (aturan 41).
- `saudara_settled` = nama simbol yang sama ditambah akhiran `SETTLED` atau
  `_SETTLED`. Kedua bentuk ada di semesta; keduanya diperiksa.
- `sebab` pada H-A013 mengambil EMPAT nilai yang saling membedakan (aturan 46):
  `hadir_di_penyebut` (bulan peralihan ternyata ada, jadi tidak ada yang hilang),
  `saudara_settled_memuat_bulan` (terbit di bawah nama SETTLED),
  `saudara_settled_bulan_lain` (saudara ada tetapi bulannya bukan itu), dan
  `tanpa_saudara_settled` (sebab masih BELUM terukur - jujur, bukan nol).

## Penggugur (aturan 24)

`selisih_penyebut` terhadap 19.586, `selisih_mati` terhadap 1.401, dan
`selisih_jumlah_tahun` (jumlah penyebut per tahun dikurangi penyebut) harus nol.
Ditambah `sidik_seragam`, kelengkapan kedelapan laporan pecahan, ketiadaan kunci
ganda, dan kendali positif `silang_funding.kendali_silang` (aturan 50). H-A013
yang KALAH bukan penggugur.

## Praregistrasi ramalan - ditulis SEBELUM run

- **R-238** - CI pada commit yang memuat berkas ini mengumpulkan **494 butir**
  dengan kode keluar **0**. Dasar (aturan 54, 56, 57): 450 butir terverifikasi
  pada run 30444539002 (commit 34ff496b), berkas uji baru menyumbang **44**
  butir, tidak ada berkas uji lain disentuh, 450 + 44 = **494**. Keempat puluh
  empat nama ditulis BERNOMOR di docstring berkas uji; tidak ada `parametrize`.
  Aturan 57 mencatat tiga dari tiga ramalan cacah butir sebelumnya TEPAT.
- **R-239** - `cacah_saudara_ditemukan` pada keenam bulan peralihan jatuh pada
  **4..6** dari 6. Dasar: `semesta_bulan_1m.json` memuat keenam nama berakhiran
  SETTLED, tetapi keberadaan di sana TIDAK menjamin lolos gerbang 1m - dua belas
  simbol-bulan gagal gerbang dan masuk karantina. Ramalan GUGUR bila 3 atau
  kurang.
- **R-240 (H-A013)** - `cacah_cocok_bulan` jatuh pada **4..6** dari 6 dan
  `menang` **true**. Dasar: keenam saudara SETTLED punya TEPAT SATU bulan, dan
  bulan yang hilang dari penyebut tepat satu pula. Ramalan GUGUR bila 3 atau
  kurang cocok. Bila ia MENANG, tafsir "delapan kebangkitan" wajib dilemahkan di
  STATE berikutnya menjadi "dua kebangkitan bersambung dan enam peralihan nama";
  itu konsekuensi yang saya terima sebelum melihat hasilnya.
- **R-241** - tahun dengan `bagian_mati` TERTINGGI adalah **2026**. Dasar: 556
  MATI pada 2026 hanya mencakup enam bulan kalender (sampai 2026-06), sedangkan
  506 MATI pada 2025 tersebar atas dua belas bulan. Ramalan GUGUR bila tahun
  tertinggi adalah tahun lain mana pun.

Aturan yang mengikat: 10, 20, 21, 22, 24, 30, 36, 37, 41, 44, 45, 46, 47, 48,
50, 51, 52, 53, 54, 56, 57, 58, 59, 60, 61. Cacah baris berkas ini SENGAJA tidak
diramalkan (aturan 58, pilihan c): ia diukur `ukur_baris`, bukan ditaksir.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from . import kebangkitan, kehidupan, kehidupan_arsip, silang_funding

VERSI = 1
TOTAL_PECAHAN = kehidupan_arsip.TOTAL_PECAHAN
SUMBER_FUNDING = silang_funding.SUMBER_FUNDING
KELUARAN = "reports/penyebut_tahun.json"
KELUARAN_RINGKAS = "reports/penyebut_tahun_ringkas.json"

PENYEBUT_TERCATAT = kebangkitan.PENYEBUT_TERCATAT
MATI_TERCATAT = kebangkitan.MATI_TERCATAT

# Keenam bulan peralihan yang HILANG dari penyebut, dari reports/kebangkitan.json
# (blob 43b70e24, dibaca utuh). Bulan peralihan = bulan tepat sesudah bulan MATI
# terakhir dan tepat sebelum bulan HIDUP pertama.
PERALIHAN: Tuple[Tuple[str, str], ...] = (
    ("CTKUSDT", "2025-04"),
    ("CVCUSDT", "2025-05"),
    ("CVXUSDT", "2025-07"),
    ("LITUSDT", "2025-12"),
    ("MAVIAUSDT", "2025-03"),
    ("SLPUSDT", "2025-07"),
)

# Kedua peristiwa yang BERSAMBUNG; didaftar supaya perbandingannya tersurat.
BERSAMBUNG: Tuple[str, ...] = ("ICPUSDT", "TLMUSDT")

AKHIRAN_SETTLED: Tuple[str, ...] = ("SETTLED", "_SETTLED")

SEBAB_HADIR = "hadir_di_penyebut"
SEBAB_SAUDARA_COCOK = "saudara_settled_memuat_bulan"
SEBAB_SAUDARA_LAIN = "saudara_settled_bulan_lain"
SEBAB_TANPA_SAUDARA = "tanpa_saudara_settled"

AMBANG_MENANG = 4

# BNXUSDT: tiga lubang funding TENGAH tercatat pada reports/silang_funding.json.
SIMBOL_BNX = "BNXUSDT"
LUBANG_BNX_TERCATAT: Tuple[str, ...] = ("2022-04", "2022-06", "2022-08")

BERKAS_DICAP = [
    "kebangkitan.py",
    "kehidupan.py",
    "kehidupan_arsip.py",
    "penyebut_tahun.py",
    "silang_funding.py",
]

Kunci = Tuple[str, str]


def nama_keluaran() -> str:
    return KELUARAN


def nama_ringkas() -> str:
    """Aturan 52: laporan penuh wajib berpasangan dengan berkas kecil."""
    return KELUARAN_RINGKAS


def sidik_kode() -> str:
    """Aturan 22: cap setiap berkas yang ikut menentukan angka ini."""
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(BERKAS_DICAP):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def tahun_dari_bulan(bulan: str) -> str:
    """Empat aksara pertama; bentuk masukan selalu YYYY-MM."""
    return str(bulan)[:4]


def penyebut_per_tahun(status: Dict[Kunci, str]) -> Dict[str, int]:
    """Cacah simbol-bulan yang LOLOS gerbang, menurut tahun."""
    keluar: Dict[str, int] = {}
    for (_simbol, bulan), _st in status.items():
        tahun = tahun_dari_bulan(bulan)
        keluar[tahun] = keluar.get(tahun, 0) + 1
    return dict(sorted(keluar.items()))


def mati_per_tahun(status: Dict[Kunci, str]) -> Dict[str, int]:
    """Dipakai apa adanya dari kebangkitan V1; definisinya SATU (aturan 36)."""
    return kebangkitan.sebaran_mati_tahun(status)


def bagian_mati_per_tahun(status: Dict[Kunci, str]) -> Dict[str, Any]:
    """Pembilang dan penyebut berdampingan, per tahun.

    Penyebut nol berbunyi `terukur` false dan `bagian` null (aturan 41); tahun
    tanpa MATI tetap didaftar dengan pembilang 0 supaya tidak hilang diam-diam.
    """
    penyebut = penyebut_per_tahun(status)
    mati = mati_per_tahun(status)
    baris: List[Dict[str, Any]] = []
    for tahun in sorted(penyebut):
        n = int(penyebut[tahun])
        m = int(mati.get(tahun, 0))
        baris.append(
            {
                "tahun": tahun,
                "penyebut": n,
                "mati": m,
                "bagian": (round(m / n, 6) if n > 0 else None),
                "terukur": n > 0,
            }
        )
    terukur = [b for b in baris if b["terukur"]]
    tertinggi = max(terukur, key=lambda b: (b["bagian"], b["tahun"])) if terukur else None
    return {
        "baris": baris,
        "cacah_tahun": len(baris),
        "jumlah_penyebut": sum(int(b["penyebut"]) for b in baris),
        "jumlah_mati": sum(int(b["mati"]) for b in baris),
        "tahun_tertinggi": (tertinggi["tahun"] if tertinggi else None),
        "bagian_tertinggi": (tertinggi["bagian"] if tertinggi else None),
    }


def nama_settled(simbol: str) -> List[str]:
    """Kedua bentuk saudara yang ada di semesta, tanpa penggandaan."""
    keluar: List[str] = []
    for akhiran in AKHIRAN_SETTLED:
        nama = "%s%s" % (str(simbol), akhiran)
        if nama not in keluar:
            keluar.append(nama)
    return keluar


def bulan_simbol(status: Dict[Kunci, str], simbol: str) -> List[str]:
    """Bulan yang terdaftar bagi satu simbol, terurut; asing berbunyi kosong."""
    return sorted(kebangkitan.peta_status(status).get(str(simbol), {}))


def uji_h_a013(
    status: Dict[Kunci, str],
    peralihan: Sequence[Tuple[str, str]] = PERALIHAN,
) -> Dict[str, Any]:
    """H-A013: bulan peralihan yang hilang terbit di bawah nama SETTLED.

    MENANG hanya bila sekurang-kurangnya `AMBANG_MENANG` dari bulan peralihan
    benar-benar ditemukan pada saudara SETTLED. Penyebut kosong berbunyi
    `terukur` false, bukan kekalahan (aturan 41, 46).
    """
    peta = kebangkitan.peta_status(status)
    baris: List[Dict[str, Any]] = []
    hadir = saudara = cocok = 0
    for simbol, bulan in peralihan:
        st_map = peta.get(str(simbol), {})
        ada = str(bulan) in st_map
        ditemukan = [n for n in nama_settled(simbol) if n in peta]
        bulan_saudara = sorted({b for n in ditemukan for b in peta[n]})
        memuat = str(bulan) in bulan_saudara
        if ada:
            sebab = SEBAB_HADIR
        elif memuat:
            sebab = SEBAB_SAUDARA_COCOK
        elif ditemukan:
            sebab = SEBAB_SAUDARA_LAIN
        else:
            sebab = SEBAB_TANPA_SAUDARA
        if ada:
            hadir += 1
        if ditemukan:
            saudara += 1
        if memuat and not ada:
            cocok += 1
        baris.append(
            {
                "simbol": str(simbol),
                "bulan_peralihan": str(bulan),
                "hadir_di_penyebut": ada,
                "saudara_diperiksa": nama_settled(simbol),
                "saudara_ditemukan": ditemukan,
                "bulan_saudara": bulan_saudara,
                "cacah_bulan_saudara": len(bulan_saudara),
                "cocok_bulan": bool(memuat and not ada),
                "sebab": sebab,
            }
        )
    return {
        "baris": baris,
        "cacah_peralihan": len(baris),
        "cacah_hadir_di_penyebut": hadir,
        "cacah_saudara_ditemukan": saudara,
        "cacah_cocok_bulan": cocok,
        "ambang_menang": AMBANG_MENANG,
        "sebab_terpakai": sorted({str(b["sebab"]) for b in baris}),
        "definisi_dapat_dibedakan": len({str(b["sebab"]) for b in baris}) > 1,
        "terukur": len(status) > 0,
        "menang": len(status) > 0 and cocok >= AMBANG_MENANG,
    }


def rinci_bersambung(
    status: Dict[Kunci, str], simbol: Sequence[str] = BERSAMBUNG
) -> List[Dict[str, Any]]:
    """Kedua peristiwa bersambung, diperiksa dengan alat yang SAMA."""
    peta = kebangkitan.peta_status(status)
    keluar: List[Dict[str, Any]] = []
    for s in simbol:
        ditemukan = [n for n in nama_settled(s) if n in peta]
        keluar.append(
            {
                "simbol": str(s),
                "cacah_bulan": len(peta.get(str(s), {})),
                "saudara_ditemukan": ditemukan,
                "cacah_bulan_saudara": sum(len(peta[n]) for n in ditemukan),
            }
        )
    return keluar


def rinci_bnx(
    status: Dict[Kunci, str],
    simbol: str = SIMBOL_BNX,
    bulan_lubang: Iterable[str] = LUBANG_BNX_TERCATAT,
) -> Dict[str, Any]:
    """Ketiga lubang funding tengah BNXUSDT, apa adanya terhadap penyebut.

    Bulan lubang datang sebagai KONSTANTA tercatat dari laporan yang sudah
    di-commit; modul ini tidak menurunkannya ulang dan tidak mengklaim kecocokan
    dengan KC-15 (laporan KC-15 belum dibaca utuh).
    """
    peta = kebangkitan.peta_status(status)
    st_map = peta.get(str(simbol), {})
    ditemukan = [n for n in nama_settled(simbol) if n in peta]
    baris = [
        {
            "bulan": str(b),
            "ada_di_penyebut": str(b) in st_map,
            "status": st_map.get(str(b)),
        }
        for b in bulan_lubang
    ]
    return {
        "simbol": str(simbol),
        "cacah_bulan": len(st_map),
        "bulan": sorted(st_map),
        "saudara_ditemukan": ditemukan,
        "bulan_saudara": sorted({b for n in ditemukan for b in peta[n]}),
        "lubang": baris,
        "cacah_lubang": len(baris),
        "cacah_lubang_ada_di_penyebut": sum(1 for b in baris if b["ada_di_penyebut"]),
        "klaim_kc15": False,
    }


def bulan_hidup_terakhir_penuh(
    status: Dict[Kunci, str]
) -> Dict[str, Optional[str]]:
    """Peta penuh; definisinya dipakai apa adanya dari kebangkitan V1."""
    return kebangkitan.bulan_hidup_terakhir(status)


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
    if int(ringkasan.get("selisih_penyebut") or 0) != 0:
        return 2
    if int(ringkasan.get("selisih_mati") or 0) != 0:
        return 2
    if int(ringkasan.get("selisih_jumlah_tahun") or 0) != 0:
        return 2
    return 0


def jalankan(akar: str = ".", total: int = TOTAL_PECAHAN) -> Dict[str, Any]:
    status, byte_parquet, meta = silang_funding.baca_laporan_kehidupan(
        akar=akar, total=total
    )
    mentah = (Path(akar) / SUMBER_FUNDING).read_bytes()
    funding = json.loads(mentah.decode("utf-8"))
    lubang, meta_lubang = silang_funding.lubang_funding(funding)
    kendali = silang_funding.kendali_silang(byte_parquet, status, lubang)

    tabel = bagian_mati_per_tahun(status)
    h_a013 = uji_h_a013(status)
    bersambung = rinci_bersambung(status)
    bnx = rinci_bnx(status)
    terakhir = bulan_hidup_terakhir_penuh(status)

    ringkasan: Dict[str, Any] = {
        "penyebut_kehidupan": len(status),
        "selisih_penyebut": len(status) - PENYEBUT_TERCATAT,
        "penyebut_simbol": len(terakhir),
        "jumlah_penyebut_tahun": tabel["jumlah_penyebut"],
        "selisih_jumlah_tahun": tabel["jumlah_penyebut"] - len(status),
        "jumlah_mati_tahun": tabel["jumlah_mati"],
        "selisih_mati": tabel["jumlah_mati"] - MATI_TERCATAT,
        "cacah_tahun": tabel["cacah_tahun"],
        "tahun_tertinggi": tabel["tahun_tertinggi"],
        "bagian_tertinggi": tabel["bagian_tertinggi"],
        "h_a013_menang": h_a013["menang"],
        "h_a013_terukur": h_a013["terukur"],
        "h_a013_dapat_dibedakan": h_a013["definisi_dapat_dibedakan"],
        "cacah_hadir_di_penyebut": h_a013["cacah_hadir_di_penyebut"],
        "cacah_saudara_ditemukan": h_a013["cacah_saudara_ditemukan"],
        "cacah_cocok_bulan": h_a013["cacah_cocok_bulan"],
        "bnx_cacah_lubang_ada_di_penyebut": bnx["cacah_lubang_ada_di_penyebut"],
        "cacah_simbol_tanpa_hidup": sum(1 for v in terakhir.values() if v is None),
        "kendali": kendali,
        "kendali_sah": silang_funding.kendali_sah(kendali),
    }
    ringkasan.update(meta)
    ringkasan.update(meta_lubang)

    definisi = {
        "penyebut_per_tahun": (
            "cacah simbol-bulan yang LOLOS gerbang pada tahun itu; bulan yang "
            "tidak terdaftar bukan bulan MATI melainkan bulan yang TIDAK ADA"
        ),
        "bagian_mati": (
            "mati tahun itu dibagi penyebut tahun itu; penyebut nol berbunyi "
            "terukur false dan bagian null, BUKAN nol"
        ),
        "saudara_settled": (
            "nama simbol yang sama ditambah akhiran SETTLED atau _SETTLED; kedua "
            "bentuk ada di semesta dan keduanya diperiksa"
        ),
        "sebab": (
            "empat nilai yang saling membedakan: hadir_di_penyebut, "
            "saudara_settled_memuat_bulan, saudara_settled_bulan_lain, "
            "tanpa_saudara_settled (sebab BELUM terukur, bukan nol)"
        ),
        "h_a013_menang": (
            "benar hanya bila sekurang-kurangnya empat dari enam bulan peralihan "
            "ditemukan pada saudara SETTLED"
        ),
    }

    return {
        "bukan_bukti": False,
        "versi_penyebut_tahun": VERSI,
        "sidik_kode": sidik_kode(),
        "sidik_kode_kebangkitan": kebangkitan.sidik_kode(),
        "sidik_kode_silang_funding": silang_funding.sidik_kode(),
        "sidik_data_funding": hashlib.sha256(mentah).hexdigest(),
        "versi_funding": funding.get("versi_funding"),
        "sumber": [SUMBER_FUNDING]
        + [kehidupan_arsip.nama_keluaran(i) for i in range(total)],
        "definisi": definisi,
        "tabel_tahun": tabel,
        "h_a013": h_a013,
        "bersambung": bersambung,
        "bnx": bnx,
        "bulan_hidup_terakhir": terakhir,
        "ringkasan": ringkasan,
        "catatan_batas": (
            "seluruh angka terbatas pada 19.586 simbol-bulan yang LOLOS gerbang; "
            "12 simbol-bulan karantina tidak ada di dalamnya, jadi "
            "tanpa_saudara_settled BUKAN bukti saudara itu tidak diterbitkan "
            "(aturan 30, 46, 59)"
        ),
        "catatan_tafsir": (
            "bila H-A013 MENANG, keenam peristiwa itu sebagian perkara PENAMAAN "
            "kontrak yang diselesaikan, sehingga tafsir kebangkitan wajib "
            "DILEMAHKAN, bukan diperkuat; bagian_mati per tahun tidak mengukur "
            "sebab kematian mana pun (aturan 10, 20)"
        ),
        "catatan_penggugur": (
            "sidik_seragam false, laporan pecahan kurang, kunci ganda, "
            "kendali_sah false, atau salah satu dari selisih_penyebut, "
            "selisih_mati, selisih_jumlah_tahun bukan nol membatalkan seluruh "
            "angka (aturan 24); H-A013 yang gugur BUKAN penggugur"
        ),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def ringkas(laporan: Dict[str, Any]) -> Dict[str, Any]:
    """Berkas kecil pendamping (aturan 52): tanpa peta 787 simbol."""
    h = laporan.get("h_a013") or {}
    return {
        "bukan_bukti": False,
        "versi_penyebut_tahun": laporan.get("versi_penyebut_tahun"),
        "sidik_kode": laporan.get("sidik_kode"),
        "sidik_data_funding": laporan.get("sidik_data_funding"),
        "ringkasan": laporan.get("ringkasan"),
        "tabel_tahun": laporan.get("tabel_tahun"),
        "h_a013": {k: v for k, v in h.items() if k != "baris"},
        "h_a013_baris": h.get("baris"),
        "bersambung": laporan.get("bersambung"),
        "bnx": laporan.get("bnx"),
        "waktu_utc": laporan.get("waktu_utc"),
    }


def main() -> int:
    laporan = jalankan()
    Path(KELUARAN).parent.mkdir(parents=True, exist_ok=True)
    Path(KELUARAN).write_text(
        json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    teks = (
        json.dumps(ringkas(laporan), ensure_ascii=False, indent=2, sort_keys=True)
        + "\n"
    )
    Path(KELUARAN_RINGKAS).write_text(teks, encoding="utf-8")
    print(teks)
    return kode_keluar(laporan["ringkasan"])


if __name__ == "__main__":
    raise SystemExit(main())
