"""Pindai SELURUH semesta untuk KEBANGKITAN — satu run, tiga pertanyaan.

LITUSDT membuktikan sebuah simbol dapat MATI lima bulan lalu HIDUP kembali
(H-A011 MENANG 6-0, run 30440471508). Sebelum itu repo ini berulang kali menulis
"tidak ada kebangkitan" dengan dasar `bangkit_kembali` = 0 pada `kohort_ekor` V4
- padahal laporan yang sama menulis `cacah_simbol_bangkit_dapat_diuji` = **0**,
yang berarti alat ukurnya tidak pernah mampu membedakan. Dari kekeliruan itu
lahir aturan 59 dan KC-21. Modul ini menutupnya dengan PENGUKURAN, bukan dengan
tafsir.

Tenggat riset maju ke 2 Agustus 2026, jadi satu run atomik ini sengaja menjawab
TIGA pertanyaan yang bahan bakunya sudah di-commit dan tidak menyentuh jaringan:

1. **H-A012** - berapa banyak simbol di semesta 787 yang punya bulan MATI lalu
   bulan HIDUP sesudahnya. Penyebutnya kini terbukti TIDAK kosong (LITUSDT ada
   di dalamnya), jadi pertanyaan ini bermakna.
2. **BTCSTUSDT 2022-02..2026-06** - pemilik lubang funding TENGAH yang satu lagi.
   Apakah rentetan satu bulannya juga kebangkitan, atau bentuk lain sama sekali.
   Diuji dengan MEMAKAI ULANG `lubang_tengah.uji_h_a011` beserta rentang yang
   berbeda; definisi "menang" karena itu tetap SATU (aturan 36).
3. **Sebaran 1.401 MATI menurut TAHUN dan menurut SIMBOL**, plus
   `bulan_hidup_terakhir` bagi SELURUH 787 simbol - superset dari 28 anggota
   kohort yang belum disampel `kohort_ekor` V4.

## Mengapa modul BARU

`funding.py` dan `silang_funding.py` sama-sama **705 baris**; aturan 48 melarang
menambah fungsi ke keduanya sebelum dipecah. `lubang_tengah.py` V2 belum diukur
cacah barisnya, jadi menumpuk di sana melanggar semangat aturan yang sama.
Seluruh pembaca laporan yang dibutuhkan sudah ada dan sudah diuji
(`silang_funding.baca_laporan_kehidupan`, `lubang_funding`, `kendali_silang`,
`lubang_tengah.uji_h_a011`), jadi modul ini MEMAKAINYA, tidak menyalinnya.

## Definisi yang dipakai - tersurat, supaya dapat digugurkan

- `rentetan_status` menggabungkan bulan berstatus sama HANYA bila bulannya
  bersambung menurut kalender. Jurang bulan (simbol tidak terdaftar) MEMUTUS
  rentetan; ia tidak diam-diam dijembatani.
- **kebangkitan** = sebuah bulan MATI yang mengakhiri rentetan MATI dan diikuti,
  kapan pun sesudahnya, oleh sekurang-kurangnya satu bulan HIDUP. Bulan SEPI di
  antaranya TIDAK membatalkan; jaraknya dilaporkan pada `cacah_bulan_antara`.
- `ada_hidup_sebelum` memisahkan dua hal yang mudah tertukar: pasar yang pernah
  hidup lalu mati lalu hidup lagi (**bangkit penuh**, seperti LITUSDT), dan pasar
  yang bulan-bulan awalnya mati lalu mulai hidup (itu bukan kebangkitan
  melainkan permulaan yang lambat). Keduanya dicacah terpisah.
- `bulan_hidup_terakhir` = bulan HIDUP terbesar simbol itu di dalam penyebut
  19.586. Ini BUKAN definisi `kohort_ekor` V4, yang memindai MUNDUR dari 2025-07
  dan karena itu tidak pernah memeriksa bulan sesudah jendelanya. Keduanya
  dibandingkan berdampingan (aturan 36) lewat `cocokkan_kohort_ekor`; selisih
  adalah TEMUAN tentang jendela, bukan cacat.

## Penggugur (aturan 24)

`selisih_penyebut` terhadap **19.586** dan `selisih_mati` terhadap **1.401**
harus nol; bukan nol berarti bahan bakunya berubah dan seluruh laporan batal
(kode 2). Ditambah `sidik_seragam`, kelengkapan kedelapan laporan pecahan,
ketiadaan kunci ganda, dan kendali positif `silang_funding.kendali_silang`
(aturan 50). H-A012 yang KALAH bukan penggugur - hipotesis yang kalah adalah
hasil.

Laporan penuh berpasangan dengan `reports/kebangkitan_ringkas.json` yang kecil
supaya selalu terbaca utuh dari luar runner (aturan 52).

## Praregistrasi ramalan - ditulis SEBELUM run

- **R-232** - CI pada commit BERIKUTNYA yang menyentuh
  `tests/test_kebangkitan.py` (aturan 56), yakni commit yang memuat berkas ini,
  mengumpulkan **450 butir** dengan kode keluar **0**. Dasar (aturan 38, 54, 57):
  396 butir terverifikasi pada run 30440471598, berkas uji baru menyumbang
  **54** butir, tidak ada berkas uji lain disentuh, 396 + 54 = **450**. Kelima
  puluh empat nama ditulis BERNOMOR di docstring berkas uji pada commit yang
  sama; tidak ada `parametrize` di sana.
- **R-233 (H-A012, ditulis di bawah aturan 59)** - penyebutnya **787 simbol**,
  dan cacah kasus kebangkitan yang pernah benar-benar diperiksa sebelum ini
  adalah **satu** (LITUSDT), sehingga saya DILARANG menegaskan ketiadaan maupun
  kelangkaan. Ramalan berbentuk pita: `cacah_simbol_bangkit` jatuh pada
  **2..80** simbol, `cacah_peristiwa` tidak kurang daripada
  `cacah_simbol_bangkit`, dan `menang` **true**. Ramalan ini GUGUR bila hasilnya
  1 (kebangkitan benar-benar tunggal) atau lebih besar daripada 80. Alasan pita:
  826 dari 877 lubang funding berbentuk EKOR, yang menandai kematian terminal,
  sehingga sebagian besar dari 1.401 MATI tidak akan berbalik; tetapi 559
  simbol-bulan MATI tetap berfunding, dan justru di sanalah kebangkitan mungkin
  bersembunyi.
- **R-234 (BTCSTUSDT, berkepala dua)** - `cacah_bulan` pada rentang
  2022-02..2026-06 tepat **53** (hitungan kalender: 11 + 12 + 12 + 12 + 6), dan
  `cacah_hidup` **sekurang-kurangnya 1**. Dasar kepala kedua: BTCSTUSDT punya 64
  bulan klines dengan hanya SATU lubang funding, jadi funding terbit pada 63
  bulan lainnya; bila tafsir LITUSDT berlaku umum, perdagangan pulih bersama
  funding. Kepala kedua GUGUR bila keenam puluh tiga bulan itu ternyata MATI
  seluruhnya - dan bila itu terjadi, KC-18 justru menang: funding dapat terbit
  tanpa perdagangan.
- **R-235 (cocok kohort_ekor)** - kesepuluh simbol `kohort_ekor` V4 HADIR di
  penyebut (`cacah_hilang` = **0**) dan `cacah_cocok` jatuh pada **6..10** dari
  10. Pita itu lebar dengan sengaja: `kohort_ekor` memindai MUNDUR dari 2025-07,
  sehingga bulan HIDUP sesudah jendelanya tidak pernah diperiksa, dan tiap
  simbol yang bangkit sesudah 2025-07 akan berbeda. Selisih semacam itu bukan
  kekalahan alat ukur mana pun; ia keterangan tentang jendela (aturan 51).

Aturan yang mengikat: 10, 20, 21, 22, 24, 30, 36, 37, 41, 44, 45, 46, 47, 48,
50, 51, 52, 53, 54, 56, 57, 58, 59. Cacah baris berkas ini SENGAJA tidak
diramalkan (aturan 58, pilihan c): ia diukur `ukur_baris`, bukan ditaksir.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from . import kehidupan, kehidupan_arsip, lubang_tengah, silang_funding

VERSI = 1
TOTAL_PECAHAN = kehidupan_arsip.TOTAL_PECAHAN
SUMBER_FUNDING = silang_funding.SUMBER_FUNDING
KELUARAN = "reports/kebangkitan.json"
KELUARAN_RINGKAS = "reports/kebangkitan_ringkas.json"

# Angka terverifikasi yang dipakai sebagai PENGGUGUR (aturan 24).
# Penyebut 19.586 dan 1.401 MATI: kedelapan run pecahan pada commit 0929643c.
PENYEBUT_TERCATAT = 19586
MATI_TERCATAT = 1401

# Pemilik lubang funding TENGAH yang satu lagi (laporan lubang_tengah V1/V2).
SIMBOL_TENGAH_LAIN = "BTCSTUSDT"
RENTANG_BTCST = ("2022-02", "2026-06")

# kohort_ekor V4, run 30416845475: bulan_hidup_terakhir 10 anggota abjad awal.
# Dipakai HANYA untuk perbandingan berdampingan (aturan 36), bukan sebagai
# kebenaran yang menggugurkan.
KOHORT_EKOR_TERCATAT = {
    "AGIXUSDT": "2024-06",
    "ALPACAUSDT": "2025-04",
    "AMBUSDT": "2025-02",
    "BADGERUSDT": "2025-03",
    "BALUSDT": "2025-03",
    "BLZUSDT": "2024-12",
    "BNXUSDT": "2025-03",
    "BONDUSDT": "2024-11",
    "COMBOUSDT": "2025-03",
    "DARUSDT": "2024-12",
}

TERATAS = 20

BERKAS_DICAP = [
    "kebangkitan.py",
    "kehidupan.py",
    "kehidupan_arsip.py",
    "lubang_tengah.py",
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


def bulan_setelah(bulan: str) -> str:
    """Bulan kalender berikutnya, dalam bentuk YYYY-MM."""
    tahun = int(str(bulan)[:4])
    bln = int(str(bulan)[5:7])
    if bln >= 12:
        return "%04d-01" % (tahun + 1)
    return "%04d-%02d" % (tahun, bln + 1)


def cacah_bulan_rentang(mulai: str, sampai: str) -> int:
    """Cacah bulan pada rentang tertutup; rentang terbalik berbunyi 0."""
    a = int(str(mulai)[:4]) * 12 + int(str(mulai)[5:7])
    b = int(str(sampai)[:4]) * 12 + int(str(sampai)[5:7])
    return b - a + 1 if b >= a else 0


def peta_status(status: Dict[Kunci, str]) -> Dict[str, Dict[str, str]]:
    """Status per simbol per bulan, seluruhnya sebagai string."""
    keluar: Dict[str, Dict[str, str]] = {}
    for (simbol, bulan), st in status.items():
        keluar.setdefault(str(simbol), {})[str(bulan)] = str(st)
    return keluar


def rentetan_status(st_map: Dict[str, str]) -> List[Dict[str, Any]]:
    """Rentetan bulan berstatus sama; jurang kalender MEMUTUS rentetan."""
    keluar: List[Dict[str, Any]] = []
    berikut: Optional[str] = None
    for bulan in sorted(st_map):
        st = st_map[bulan]
        if keluar and keluar[-1]["status"] == st and berikut == bulan:
            keluar[-1]["sampai"] = bulan
            keluar[-1]["panjang"] += 1
        else:
            keluar.append(
                {"status": st, "mulai": bulan, "sampai": bulan, "panjang": 1}
            )
        berikut = bulan_setelah(bulan)
    return keluar


def kebangkitan_simbol(st_map: Dict[str, str]) -> List[Dict[str, Any]]:
    """Peristiwa MATI -> HIDUP pada satu simbol.

    Sebuah peristiwa dicatat pada bulan MATI yang MENGAKHIRI rentetan MATI dan
    diikuti, kapan pun sesudahnya, oleh bulan HIDUP. Bulan SEPI di antaranya
    tidak membatalkan; jaraknya dilaporkan apa adanya (aturan 10).
    """
    urut = sorted(st_map)
    keluar: List[Dict[str, Any]] = []
    for i, bulan in enumerate(urut):
        if st_map[bulan] != kehidupan.STATUS_MATI:
            continue
        if i + 1 < len(urut) and st_map[urut[i + 1]] == kehidupan.STATUS_MATI:
            continue
        sesudah = [b for b in urut[i + 1 :] if st_map[b] == kehidupan.STATUS_HIDUP]
        if not sesudah:
            continue
        hidup = sesudah[0]
        j = i
        while j - 1 >= 0 and st_map[urut[j - 1]] == kehidupan.STATUS_MATI:
            j -= 1
        keluar.append(
            {
                "bulan_mati_mulai": urut[j],
                "bulan_mati_terakhir": bulan,
                "panjang_mati": i - j + 1,
                "bulan_hidup_pertama_sesudah": hidup,
                "cacah_bulan_antara": urut.index(hidup) - i - 1,
                "ada_hidup_sebelum": any(
                    st_map[b] == kehidupan.STATUS_HIDUP for b in urut[:j]
                ),
            }
        )
    return keluar


def daftar_kebangkitan(status: Dict[Kunci, str]) -> List[Dict[str, Any]]:
    """Baris bernama bagi setiap simbol yang punya sekurangnya satu peristiwa."""
    peta = peta_status(status)
    baris: List[Dict[str, Any]] = []
    for simbol in sorted(peta):
        st_map = peta[simbol]
        peristiwa = kebangkitan_simbol(st_map)
        if not peristiwa:
            continue
        urut = sorted(st_map)
        baris.append(
            {
                "simbol": simbol,
                "cacah_peristiwa": len(peristiwa),
                "peristiwa": peristiwa,
                "cacah_bulan": len(urut),
                "bulan_pertama": urut[0],
                "bulan_terakhir": urut[-1],
                "bangkit_penuh": any(p["ada_hidup_sebelum"] for p in peristiwa),
            }
        )
    return baris


def uji_h_a012(
    baris: List[Dict[str, Any]], penyebut_simbol: int
) -> Dict[str, Any]:
    """H-A012: kebangkitan bukan peristiwa tunggal.

    MENANG hanya bila LEBIH DARI SATU simbol punya peristiwa; penyebut nol
    berbunyi `terukur` false, bukan kekalahan (aturan 41, 46).
    """
    penuh = [r["simbol"] for r in baris if r.get("bangkit_penuh")]
    return {
        "cacah_simbol_bangkit": len(baris),
        "cacah_peristiwa": sum(int(r.get("cacah_peristiwa") or 0) for r in baris),
        "cacah_simbol_bangkit_penuh": len(penuh),
        "simbol_bangkit_penuh": sorted(penuh),
        "penyebut_simbol": int(penyebut_simbol),
        "terukur": int(penyebut_simbol) > 0,
        "menang": int(penyebut_simbol) > 0 and len(baris) > 1,
    }


def bulan_hidup_terakhir(status: Dict[Kunci, str]) -> Dict[str, Optional[str]]:
    """Bulan HIDUP terbesar per simbol; null bila simbol itu tak pernah HIDUP."""
    keluar: Dict[str, Optional[str]] = {}
    for simbol, st_map in peta_status(status).items():
        hidup = [b for b in sorted(st_map) if st_map[b] == kehidupan.STATUS_HIDUP]
        keluar[simbol] = hidup[-1] if hidup else None
    return keluar


def cocokkan_kohort_ekor(
    peta_terakhir: Dict[str, Optional[str]],
    tercatat: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Dua definisi berdampingan (aturan 36), tanpa satu pun dianggap benar."""
    ref = tercatat if tercatat is not None else KOHORT_EKOR_TERCATAT
    baris: List[Dict[str, Any]] = []
    cocok = beda = hilang = 0
    for simbol in sorted(ref):
        ada = simbol in peta_terakhir
        nilai = peta_terakhir.get(simbol)
        sama = ada and nilai == ref[simbol]
        if not ada:
            hilang += 1
        elif sama:
            cocok += 1
        else:
            beda += 1
        baris.append(
            {
                "simbol": simbol,
                "kohort_ekor_v4": ref[simbol],
                "kebangkitan_v1": nilai,
                "ada_di_penyebut": ada,
                "sama": sama,
            }
        )
    return {
        "baris": baris,
        "cacah_simbol": len(baris),
        "cacah_cocok": cocok,
        "cacah_beda": beda,
        "cacah_hilang": hilang,
        "seluruhnya_cocok": bool(baris) and cocok == len(baris),
    }


def sebaran_mati_tahun(status: Dict[Kunci, str]) -> Dict[str, int]:
    """Cacah simbol-bulan MATI menurut TAHUN."""
    keluar: Dict[str, int] = {}
    for (_simbol, bulan), st in status.items():
        if str(st) != kehidupan.STATUS_MATI:
            continue
        tahun = str(bulan)[:4]
        keluar[tahun] = keluar.get(tahun, 0) + 1
    return dict(sorted(keluar.items()))


def sebaran_mati_simbol(
    status: Dict[Kunci, str], teratas: int = TERATAS
) -> Dict[str, Any]:
    """Cacah simbol-bulan MATI menurut SIMBOL; hanya puncaknya didaftar."""
    per: Dict[str, int] = {}
    for (simbol, _bulan), st in status.items():
        if str(st) != kehidupan.STATUS_MATI:
            continue
        per[str(simbol)] = per.get(str(simbol), 0) + 1
    urut = sorted(per.items(), key=lambda kv: (-kv[1], kv[0]))
    return {
        "cacah_simbol_bermati": len(per),
        "cacah_mati_total": sum(per.values()),
        "teratas": [
            {"simbol": s, "cacah_bulan_mati": n} for s, n in urut[: max(teratas, 0)]
        ],
        "cacah_teratas": len(urut[: max(teratas, 0)]),
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
    if int(ringkasan.get("selisih_penyebut") or 0) != 0:
        return 2
    if int(ringkasan.get("selisih_mati") or 0) != 0:
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

    baris = daftar_kebangkitan(status)
    peta_terakhir = bulan_hidup_terakhir(status)
    h_a012 = uji_h_a012(baris, len(peta_terakhir))
    btcst = lubang_tengah.uji_h_a011(
        status, simbol=SIMBOL_TENGAH_LAIN, rentang=RENTANG_BTCST
    )
    mati_tahun = sebaran_mati_tahun(status)
    mati_simbol = sebaran_mati_simbol(status)
    cocok = cocokkan_kohort_ekor(peta_terakhir)

    ringkasan: Dict[str, Any] = {
        "penyebut_kehidupan": len(status),
        "selisih_penyebut": len(status) - PENYEBUT_TERCATAT,
        "penyebut_simbol": len(peta_terakhir),
        "cacah_mati_total": mati_simbol["cacah_mati_total"],
        "selisih_mati": mati_simbol["cacah_mati_total"] - MATI_TERCATAT,
        "cacah_simbol_bermati": mati_simbol["cacah_simbol_bermati"],
        "cacah_tahun_bermati": len(mati_tahun),
        "h_a012_menang": h_a012["menang"],
        "h_a012_terukur": h_a012["terukur"],
        "cacah_simbol_bangkit": h_a012["cacah_simbol_bangkit"],
        "cacah_peristiwa_bangkit": h_a012["cacah_peristiwa"],
        "cacah_simbol_bangkit_penuh": h_a012["cacah_simbol_bangkit_penuh"],
        "btcst_cacah_bulan": btcst["cacah_bulan"],
        "btcst_cacah_bulan_kalender": cacah_bulan_rentang(*RENTANG_BTCST),
        "btcst_cacah_hidup": btcst["cacah_hidup"],
        "btcst_terukur": btcst["terukur"],
        "btcst_menang": btcst["menang"],
        "cacah_cocok_kohort": cocok["cacah_cocok"],
        "cacah_beda_kohort": cocok["cacah_beda"],
        "cacah_hilang_kohort": cocok["cacah_hilang"],
        "kendali": kendali,
        "kendali_sah": silang_funding.kendali_sah(kendali),
    }
    ringkasan.update(meta)
    ringkasan.update(meta_lubang)

    definisi = {
        "kebangkitan": (
            "bulan MATI yang mengakhiri rentetan MATI dan diikuti kapan pun "
            "sesudahnya oleh bulan HIDUP; bulan SEPI di antaranya tidak "
            "membatalkan dan jaraknya dilaporkan"
        ),
        "bangkit_penuh": (
            "kebangkitan yang didahului sekurang-kurangnya satu bulan HIDUP "
            "sebelum rentetan MATI; tanpa itu yang terjadi adalah permulaan "
            "yang lambat, BUKAN kebangkitan"
        ),
        "rentetan_status": (
            "bulan berstatus sama digabung HANYA bila bersambung menurut "
            "kalender; jurang bulan memutus rentetan, tidak dijembatani"
        ),
        "bulan_hidup_terakhir": (
            "bulan HIDUP terbesar di dalam penyebut 19.586; BUKAN definisi "
            "kohort_ekor V4 yang memindai MUNDUR dari 2025-07 dan tidak pernah "
            "memeriksa bulan sesudah jendelanya"
        ),
        "h_a012_menang": (
            "benar hanya bila LEBIH DARI SATU simbol punya peristiwa "
            "kebangkitan; satu simbol saja berarti LITUSDT tetap tunggal"
        ),
        "btcst_menang": (
            "dipakai apa adanya dari lubang_tengah.uji_h_a011 dengan rentang "
            "2022-02..2026-06; definisinya SATU, tidak disalin ulang (aturan 36)"
        ),
    }

    return {
        "bukan_bukti": False,
        "versi_kebangkitan": VERSI,
        "sidik_kode": sidik_kode(),
        "sidik_kode_silang_funding": silang_funding.sidik_kode(),
        "sidik_kode_lubang_tengah": lubang_tengah.sidik_kode(),
        "sidik_data_funding": hashlib.sha256(mentah).hexdigest(),
        "versi_funding": funding.get("versi_funding"),
        "sumber": [SUMBER_FUNDING]
        + [kehidupan_arsip.nama_keluaran(i) for i in range(total)],
        "definisi": definisi,
        "h_a012": h_a012,
        "baris_kebangkitan": baris,
        "btcst": btcst,
        "sebaran_mati_tahun": mati_tahun,
        "sebaran_mati_simbol": mati_simbol,
        "cocok_kohort_ekor": cocok,
        "ringkasan": ringkasan,
        "catatan_batas": (
            "cacah kebangkitan ini terbatas pada 19.586 simbol-bulan yang LOLOS "
            "gerbang; 12 simbol-bulan karantina tidak ada di dalamnya, dan bulan "
            "yang tidak terdaftar di arsip bukan bulan MATI melainkan bulan yang "
            "tidak ada (aturan 30, 46)"
        ),
        "catatan_tafsir": (
            "kebangkitan yang terukur TIDAK membuktikan sebabnya: pendaftaran "
            "ulang, perubahan rezim penerbitan arsip, maupun pemulihan minat "
            "pasar sama-sama menghasilkan pola MATI lalu HIDUP (aturan 10)"
        ),
        "catatan_penggugur": (
            "sidik_seragam false, laporan pecahan kurang, kunci ganda, "
            "kendali_sah false, selisih_penyebut bukan nol, atau selisih_mati "
            "bukan nol membatalkan seluruh angka (aturan 24); H-A012 yang gugur "
            "BUKAN penggugur"
        ),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def ringkas(laporan: Dict[str, Any]) -> Dict[str, Any]:
    """Berkas kecil pendamping (aturan 52): tanpa daftar peristiwa penuh."""
    return {
        "bukan_bukti": False,
        "versi_kebangkitan": laporan.get("versi_kebangkitan"),
        "sidik_kode": laporan.get("sidik_kode"),
        "sidik_data_funding": laporan.get("sidik_data_funding"),
        "ringkasan": laporan.get("ringkasan"),
        "h_a012": {
            k: v for k, v in (laporan.get("h_a012") or {}).items() if k != "baris"
        },
        "btcst_sebaran_status": (laporan.get("btcst") or {}).get("sebaran_status"),
        "sebaran_mati_tahun": laporan.get("sebaran_mati_tahun"),
        "sebaran_mati_simbol": laporan.get("sebaran_mati_simbol"),
        "cocok_kohort_ekor": laporan.get("cocok_kohort_ekor"),
        "simbol_bangkit": [
            {
                "simbol": r.get("simbol"),
                "cacah_peristiwa": r.get("cacah_peristiwa"),
                "bangkit_penuh": r.get("bangkit_penuh"),
            }
            for r in (laporan.get("baris_kebangkitan") or [])
        ],
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
