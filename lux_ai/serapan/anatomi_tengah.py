"""Bentangan status bulanan kedua pemilik lubang funding TENGAH.

Menjawab prasyarat tersurat Keputusan 7 ADR-A008 pada cabang **BTCSTUSDT**, dan
melengkapi cabang **LITUSDT** yang sudah punya bukti kebangkitan.

## Apa yang BELUM terukur sebelum modul ini

`lubang_tengah` V2 sudah menerbitkan anatomi tingkat-BULAN keenam lubang tengah:
tetangga berfunding, panjang rentetan, cacah lilin, byte parquet, status bulan
lubang itu sendiri. Yang TIDAK ada di sana adalah **bentangan status seluruh bulan
simbolnya**. Tanpa itu satu pertanyaan yang menentukan arah ADR tidak dapat
dijawab: apakah lubang funding tengah jatuh di dalam wilayah pasar yang sudah
mati, atau **menyisip di tengah pasar yang masih hidup**?

Yang kedua adalah pembatal pertama yang tersurat di ADR-A008 §6: "bila
simbol-bulan MATI ... tersebar di TENGAH sejarah simbol yang aktif — bukan hanya
di ekor — maka label saja tidak cukup dan kebijakan penyebut harus dinaikkan
menjadi gerbang riset tersendiri". Modul ini mengukur apakah pembatal itu menyala.

## Mengapa modul BARU, bukan `lubang_tengah` V3

`ukur_baris` V5 mengukur `lubang_tengah.py` V2 pada 560 baris dan
`silang_funding.py` pada 705 baris; pagar 800 dan aturan 48 melarang menumpuk
fungsi baru pada berkas yang sudah besar. Seluruh pembacaan yang dibutuhkan sudah
ada dan sudah diuji di `silang_funding` (`baca_laporan_kehidupan`,
`baca_medan_baris`, `lubang_funding`, `kendali_silang`), jadi modul ini
MEMAKAINYA, tidak menyalinnya. Daftar simbolnya pun diambil dari
`lubang_tengah.SIMBOL_TENGAH_TERCATAT`, bukan ditulis ulang — definisi tetap SATU
(aturan 36).

## Tidak ada unduhan

Bahannya `reports/kehidupan_arsip_<0..7>.json` dan `reports/funding_semesta.json`,
keduanya sudah di-commit (aturan 13). Satu job ringan.

## Definisi yang dilahirkan di sini, dan hanya satu

**`mati_tersisip`**: bulan berstatus MATI yang tetangga langsungnya — bulan
sebelumnya DAN bulan sesudahnya di dalam penyebut kehidupan — keduanya HIDUP.
Bulan di ujung riwayat TIDAK PERNAH tersisip, sebab salah satu tetangganya tidak
ada; itu bukan kekalahan, itu ketiadaan pengukuran (aturan 46). Definisi ini
sengaja memakai tetangga di dalam PENYEBUT, bukan bulan kalender: bulan yang
dikarantina tidak ada di penyebut, sehingga ia tidak dapat menyamar sebagai
tetangga.

## Praregistrasi R-300 — ditulis di jurnal 119 SEBELUM modul ini ada

Jurnal 119 didorong lebih dahulu justru supaya ramalan ini tidak dapat disunting
sesudah angkanya terlihat; `journal/**` ada di `paths-ignore` sehingga push itu
tidak menyalakan run apa pun (calon aturan 79).

1. **Penyebut.** `cacah_bulan` = **64** bagi BTCSTUSDT DAN 64 bagi LITUSDT. Butir
   ini **MUDAH** dan disebut MUDAH: kedua angka sudah terbaca di
   `reports/lubang_tengah.json`.
2. **Tetangga lubang — BERISIKO.** Status BTCSTUSDT **2021-12 = HIDUP** dan
   **2022-02 = HIDUP**, sehingga 2022-01 adalah bulan MATI yang TERSISIP di antara
   dua bulan hidup. KALAH bila salah satu tetangga MATI atau SEPI.
3. **Bentangan hidup BTCSTUSDT — BERISIKO.** `cacah_hidup` sepanjang 64 bulan
   berada di dalam pita **8..30** inklusif, DAN `cacah_mati` lebih besar daripada
   `cacah_hidup`. KALAH bila di luar pita, atau bila MATI tidak melampaui HIDUP.

**Akibat yang dinyatakan lebih dahulu:** bila butir 2 MENANG, pembatal pertama §6
ADR-A008 MENYALA dan Keputusan 7 tidak boleh diambil sebelum kebijakan penyebut
ditinjau. Bila butir 2 KALAH, pembatal itu tidak menyala dan cabang BTCSTUSDT
menjadi kembar cabang LITUSDT.

## Penggugur (aturan 24)

`sidik_seragam` false, laporan pecahan kurang dari delapan, kunci ganda, atau
`kendali_sah` false membatalkan seluruh angka (kode 2). Kendali positif dipakai
apa adanya dari `silang_funding.kendali_silang` (aturan 50). **Ketiga butir R-300
BOLEH kalah tanpa membatalkan pengukuran:** ramalan yang kalah adalah hasil, bukan
cacat. `kode_keluar` karena itu sengaja TIDAK memeriksa `uji_r300`.

Cacah baris berkas ini dan cacah butir uji CI SENGAJA tidak diramalkan (aturan 58
pilihan c, dan keputusan jurnal 118 untuk berhenti mengumpulkan kemenangan MUDAH).

Aturan yang mengikat: 7, 10, 13, 18, 20, 21, 22, 24, 29, 30, 36, 41, 44, 45, 46,
47, 48, 50, 52, 54, 56, 57, 58, 66, 71, 73, 74.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from . import kehidupan, kehidupan_arsip, lubang_tengah, silang_funding

VERSI = 1
TOTAL_PECAHAN = kehidupan_arsip.TOTAL_PECAHAN
SUMBER_FUNDING = silang_funding.SUMBER_FUNDING
MEDAN_LILIN = silang_funding.MEDAN_LILIN
KELUARAN = "reports/anatomi_tengah.json"

# Definisi TUNGGAL: daftar pemilik lubang tengah datang dari lubang_tengah V2,
# tidak ditulis ulang di sini (aturan 36).
SIMBOL = list(lubang_tengah.SIMBOL_TENGAH_TERCATAT)

# Praregistrasi R-300, jurnal 119. Angka-angka ini DILARANG disunting sesudah run.
R300_BULAN_TERCATAT: Dict[str, int] = {"BTCSTUSDT": 64, "LITUSDT": 64}
R300_SIMBOL_LUBANG = "BTCSTUSDT"
R300_BULAN_LUBANG = "2022-01"
R300_TETANGGA = ("2021-12", "2022-02")
R300_PITA_HIDUP = (8, 30)

BERKAS_DICAP = [
    "anatomi_tengah.py",
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


def bulan_simbol(status: Dict[Kunci, str], simbol: str) -> List[str]:
    """Bulan sebuah simbol yang ADA di dalam penyebut kehidupan, urut naik."""
    return sorted(str(b) for (s, b) in status if str(s) == simbol)


def bentangan(
    status: Dict[Kunci, str],
    simbol: str,
    byte_parquet: Optional[Dict[Kunci, int]] = None,
    lilin: Optional[Dict[Kunci, Any]] = None,
    lubang: Optional[Set[Kunci]] = None,
) -> List[Dict[str, Any]]:
    """Satu baris per bulan simbol itu, apa adanya."""
    byte_parquet = byte_parquet or {}
    lilin = lilin or {}
    lubang = lubang or set()
    baris: List[Dict[str, Any]] = []
    for b in bulan_simbol(status, simbol):
        k = (simbol, b)
        baris.append(
            {
                "simbol": simbol,
                "bulan": b,
                "status": status.get(k),
                "byte_parquet": int(byte_parquet.get(k) or 0),
                "cacah_lilin": lilin.get(k),
                "funding_ada": k not in lubang,
            }
        )
    return baris


def status_bulan(
    status: Dict[Kunci, str], simbol: str, bulan: str
) -> Optional[str]:
    """Status satu simbol-bulan; None bila ia tidak ada di penyebut (aturan 46)."""
    return status.get((simbol, bulan))


def tetangga_status(
    status: Dict[Kunci, str], simbol: str, bulan: str
) -> Dict[str, Any]:
    """Status bulan itu beserta tetangga langsungnya di dalam PENYEBUT.

    Ujung riwayat menghasilkan None dan `terukur` false, bukan bulan palsu.
    """
    urut = bulan_simbol(status, simbol)
    sebelum = [b for b in urut if b < bulan]
    sesudah = [b for b in urut if b > bulan]
    nb = sebelum[-1] if sebelum else None
    na = sesudah[0] if sesudah else None
    return {
        "simbol": simbol,
        "bulan": bulan,
        "status_bulan": status.get((simbol, bulan)),
        "bulan_sebelum": nb,
        "status_sebelum": status.get((simbol, nb)) if nb is not None else None,
        "bulan_sesudah": na,
        "status_sesudah": status.get((simbol, na)) if na is not None else None,
        "terukur": bulan in urut and nb is not None and na is not None,
    }


def mati_tersisip(baris: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Bulan MATI yang KEDUA tetangganya HIDUP. Tepi riwayat tidak dihitung."""
    urut = sorted(baris, key=lambda r: str(r.get("bulan")))
    daftar: List[str] = []
    for i in range(1, len(urut) - 1):
        if urut[i].get("status") != kehidupan.STATUS_MATI:
            continue
        if (
            urut[i - 1].get("status") == kehidupan.STATUS_HIDUP
            and urut[i + 1].get("status") == kehidupan.STATUS_HIDUP
        ):
            daftar.append(str(urut[i].get("bulan")))
    return {"bulan": daftar, "cacah": len(daftar)}


def rentetan_terpanjang(baris: List[Dict[str, Any]], nama_status: str) -> int:
    """Panjang rentetan berurutan terpanjang berstatus `nama_status`; 0 bila tak ada."""
    urut = sorted(baris, key=lambda r: str(r.get("bulan")))
    terbaik = sekarang = 0
    for r in urut:
        if r.get("status") == nama_status:
            sekarang += 1
            terbaik = max(terbaik, sekarang)
        else:
            sekarang = 0
    return terbaik


def bulan_berstatus(baris: List[Dict[str, Any]], nama_status: str) -> List[str]:
    return [
        str(r.get("bulan"))
        for r in sorted(baris, key=lambda r: str(r.get("bulan")))
        if r.get("status") == nama_status
    ]


def ringkas_simbol(baris: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Ringkasan satu simbol; keempat kelas status dilapor walau nol (aturan 18)."""
    sebaran = lubang_tengah.sebaran_status(baris)
    hidup = bulan_berstatus(baris, kehidupan.STATUS_HIDUP)
    mati = bulan_berstatus(baris, kehidupan.STATUS_MATI)
    urut = [str(r.get("bulan")) for r in sorted(baris, key=lambda r: str(r.get("bulan")))]
    tersisip = mati_tersisip(baris)
    return {
        "cacah_bulan": len(baris),
        "sebaran_status": sebaran,
        "cacah_hidup": len(hidup),
        "cacah_mati": len(mati),
        "cacah_sepi": int(sebaran.get(kehidupan.STATUS_SEPI) or 0),
        "cacah_tak_terukur": int(sebaran.get(kehidupan.STATUS_TAK_TERUKUR) or 0),
        "bulan_pertama": urut[0] if urut else None,
        "bulan_terakhir": urut[-1] if urut else None,
        "bulan_hidup_pertama": hidup[0] if hidup else None,
        "bulan_hidup_terakhir": hidup[-1] if hidup else None,
        "bulan_mati_pertama": mati[0] if mati else None,
        "bulan_mati_terakhir": mati[-1] if mati else None,
        "rentetan_mati_terpanjang": rentetan_terpanjang(baris, kehidupan.STATUS_MATI),
        "rentetan_hidup_terpanjang": rentetan_terpanjang(baris, kehidupan.STATUS_HIDUP),
        "mati_tersisip": tersisip,
        "cacah_mati_tersisip": tersisip["cacah"],
        "cacah_lubang_funding": sum(1 for r in baris if r.get("funding_ada") is False),
        "byte_parquet_total": sum(int(r.get("byte_parquet") or 0) for r in baris),
    }


def uji_r300(
    ringkas: Dict[str, Dict[str, Any]], tetangga: Dict[str, Any]
) -> Dict[str, Any]:
    """Adjudikasi ketiga butir R-300, masing-masing dapat kalah sendiri."""
    baris1: List[Dict[str, Any]] = []
    menang1 = bool(R300_BULAN_TERCATAT)
    for s in sorted(R300_BULAN_TERCATAT):
        diramalkan = int(R300_BULAN_TERCATAT[s])
        ada = s in ringkas
        terukur = int((ringkas.get(s) or {}).get("cacah_bulan") or 0)
        cocok = ada and terukur == diramalkan
        menang1 = menang1 and cocok
        baris1.append(
            {
                "simbol": s,
                "diramalkan": diramalkan,
                "terukur": terukur,
                "ada_di_penyebut": ada,
                "cocok": cocok,
            }
        )

    hidup_kiri = tetangga.get("status_sebelum")
    hidup_kanan = tetangga.get("status_sesudah")
    butir2_terukur = bool(tetangga.get("terukur"))
    menang2 = (
        butir2_terukur
        and hidup_kiri == kehidupan.STATUS_HIDUP
        and hidup_kanan == kehidupan.STATUS_HIDUP
    )

    r = ringkas.get(R300_SIMBOL_LUBANG) or {}
    hidup = int(r.get("cacah_hidup") or 0)
    mati = int(r.get("cacah_mati") or 0)
    bawah, atas = R300_PITA_HIDUP
    butir3_terukur = R300_SIMBOL_LUBANG in ringkas
    dalam_pita = butir3_terukur and bawah <= hidup <= atas
    mati_melampaui = butir3_terukur and mati > hidup
    menang3 = bool(dalam_pita and mati_melampaui)

    return {
        "butir_1": {
            "nama": "cacah_bulan 64 bagi kedua simbol",
            "mudah": True,
            "baris": baris1,
            "menang": bool(menang1),
        },
        "butir_2": {
            "nama": "kedua tetangga bulan lubang BTCSTUSDT berstatus HIDUP",
            "mudah": False,
            "tetangga": tetangga,
            "tetangga_diramalkan": list(R300_TETANGGA),
            "terukur": butir2_terukur,
            "menang": bool(menang2),
        },
        "butir_3": {
            "nama": "cacah_hidup BTCSTUSDT di dalam pita dan MATI melampaui HIDUP",
            "mudah": False,
            "pita": list(R300_PITA_HIDUP),
            "cacah_hidup": hidup,
            "cacah_mati": mati,
            "dalam_pita": bool(dalam_pita),
            "mati_melampaui_hidup": bool(mati_melampaui),
            "terukur": butir3_terukur,
            "menang": menang3,
        },
        "cacah_butir_menang": int(menang1) + int(menang2) + int(menang3),
        "menang_seluruhnya": bool(menang1 and menang2 and menang3),
        "pembatal_a008_menyala": bool(menang2),
        "catatan_pembatal": (
            "pembatal_a008_menyala mengikuti butir 2 saja: bulan MATI yang "
            "tersisip di antara dua bulan HIDUP adalah kematian di TENGAH "
            "sejarah pasar aktif, yakni keadaan yang ADR-A008 §6 sebut sebagai "
            "pembatal pertama; satu kasus TIDAK boleh digeneralkan ke 19.586 "
            "(aturan 20)"
        ),
    }


def kode_keluar(ringkasan: Dict[str, Any]) -> int:
    """Kode 2 bila laporan ini tidak berhak diklaim sebagai pengukuran.

    Sengaja TIDAK memeriksa `uji_r300`: ramalan yang kalah adalah hasil.
    """
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

    baris_per_simbol: Dict[str, List[Dict[str, Any]]] = {}
    ringkas: Dict[str, Dict[str, Any]] = {}
    for s in SIMBOL:
        baris = bentangan(status, s, byte_parquet, lilin, lubang)
        baris_per_simbol[s] = baris
        ringkas[s] = ringkas_simbol(baris)

    tetangga = tetangga_status(status, R300_SIMBOL_LUBANG, R300_BULAN_LUBANG)
    r300 = uji_r300(ringkas, tetangga)
    kendali = silang_funding.kendali_silang(byte_parquet, status, lubang)

    ringkasan: Dict[str, Any] = {
        "penyebut_kehidupan": len(status),
        "cacah_simbol_diperiksa": len(SIMBOL),
        "simbol_diperiksa": sorted(SIMBOL),
        "cacah_bulan_per_simbol": {
            s: int(ringkas[s]["cacah_bulan"]) for s in sorted(ringkas)
        },
        "cacah_mati_tersisip_per_simbol": {
            s: int(ringkas[s]["cacah_mati_tersisip"]) for s in sorted(ringkas)
        },
        "r300_cacah_butir_menang": r300["cacah_butir_menang"],
        "r300_menang_seluruhnya": r300["menang_seluruhnya"],
        "pembatal_a008_menyala": r300["pembatal_a008_menyala"],
        "kendali": kendali,
        "kendali_sah": silang_funding.kendali_sah(kendali),
    }
    ringkasan.update(meta)
    ringkasan.update(meta_lilin)
    ringkasan.update(meta_lubang)

    return {
        "bukan_bukti": False,
        "versi_anatomi_tengah": VERSI,
        "sidik_kode": sidik_kode(),
        "sidik_kode_silang_funding": silang_funding.sidik_kode(),
        "sidik_kode_lubang_tengah": lubang_tengah.sidik_kode(),
        "sidik_data_funding": hashlib.sha256(mentah).hexdigest(),
        "versi_funding": funding.get("versi_funding"),
        "sumber": [SUMBER_FUNDING]
        + [kehidupan_arsip.nama_keluaran(i) for i in range(total)],
        "definisi": {
            "mati_tersisip": (
                "bulan berstatus MATI yang tetangga langsungnya DI DALAM "
                "penyebut kehidupan — bulan sebelum dan bulan sesudah — keduanya "
                "HIDUP; bulan di ujung riwayat tidak pernah tersisip sebab satu "
                "tetangganya tidak ada (aturan 46)"
            ),
            "status": (
                "dipakai apa adanya dari kehidupan.py lewat kehidupan_arsip: "
                "MATI berarti transaksi_total nol, SEPI berarti "
                "bagian_volume_nol di atas ambang; keduanya per SIMBOL-BULAN, "
                "tidak pernah per simbol (ADR-A008 Keputusan 2 dan 6)"
            ),
            "funding_ada": (
                "kebalikan keanggotaan himpunan lubang terbitan "
                "silang_funding.lubang_funding; definisinya SATU (aturan 36)"
            ),
        },
        "bentangan": {s: baris_per_simbol[s] for s in sorted(baris_per_simbol)},
        "ringkas_per_simbol": ringkas,
        "tetangga_lubang": tetangga,
        "r300": r300,
        "ringkasan": ringkasan,
        "catatan_tafsir": (
            "bentangan status TIDAK membuktikan sebab apa pun; ia hanya "
            "menunjukkan bulan mana yang tidak diperdagangkan menurut arsip. "
            "Bulan MATI yang tersisip di antara dua bulan HIDUP tetap dapat "
            "lahir dari kegagalan penerbitan arsip, bukan dari berhentinya "
            "perdagangan (aturan 10, KC-18)"
        ),
        "catatan_batas": (
            "dua simbol bukan sampel; tidak satu pun angka di sini boleh "
            "digeneralkan ke 19.586 simbol-bulan maupun ke 38 anggota kohort "
            "(aturan 20). Bentangan kehidupan kohort adalah prasyarat KEDUA "
            "Keputusan 7 dan BELUM diukur."
        ),
        "catatan_penggugur": (
            "sidik_seragam false, laporan pecahan kurang, kunci ganda, atau "
            "kendali_sah false membatalkan seluruh angka (aturan 24); ketiga "
            "butir R-300 yang kalah BUKAN penggugur"
        ),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
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
