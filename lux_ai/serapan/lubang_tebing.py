"""Arah waktu TANPA tautologi, dan berapa banyak lubang lahir di tebing 2025-07.

R-305 MELESET dua arah, dan kekalahan butir 1 adalah yang paling mengajar:
bagian `mati_tidak_setelah_lubang_bukan_awal` terukur **1.0 (118/118)**, di atas
pita 0.55..0.95. Kemenangan arah sebab tampak makin kuat, tetapi ADR-A012
menyatakannya ARTEFAK TAUTOLOGIS: uji itu memakai perbandingan LEMAH (`<=`),
sehingga simbol yang bulan MATI pertamanya SAMA DENGAN bulan lubang bukan-awal
pertamanya ikut dihitung sebagai kemenangan. Padahal kesamaan itu justru tanda
keduanya satu peristiwa (delisting), bukan tanda yang satu mendahului yang lain.
Irisan bukan sebab (aturan 10).

Modul ini memisahkan yang dulu tercampur itu menjadi TIGA kelas arah yang saling
lepas, di atas penyebut yang sama persis (`masuk_penyebut_butir_1` milik
`lubang_awal` V1, terukur 118):

- **mati_dulu** — `bulan_mati_pertama` < `bulan_lubang_bukan_awal_pertama`,
  STRIKT. Hanya kelas INI yang berhak disebut bukti arah waktu.
- **serempak** — keduanya bulan yang SAMA. Ini kelas tautologis; ia TIDAK
  dihitung sebagai kemenangan arah, dan justru diduga menguasai penyebut.
- **lubang_dulu** — `bulan_mati_pertama` > lubang bukan-awal pertama. Kelas ini
  wajib tetap dilapor walau nol (aturan 46, KC-21): nol yang tak pernah dicacah
  bukan nol yang terukur.

Pertanyaan kedua: tebing. `kohort_ekor.TEBING` = "2025-07" adalah bulan ketika 38
simbol berhenti menerbitkan funding serempak. Bila banyak
`bulan_lubang_bukan_awal_pertama` jatuh TEPAT di bulan itu, maka sebagian besar
"lubang" bukanlah peristiwa per-simbol melainkan satu peristiwa penerbitan yang
diulang 118 kali. TEBING diimpor APA ADANYA dari `kohort_ekor`, tidak ditulis
ulang sebagai harfiah (aturan 36).

Tanpa jaringan: seluruh bahan sudah di-commit. Bacaan memakai
`silang_funding.baca_laporan_kehidupan` dan `silang_funding.lubang_funding`, dan
baris per simbol dibangun oleh `lubang_awal.ringkas` APA ADANYA — modul ini TIDAK
menulis ulang satu pun definisi bentuk lubang (aturan 36, KC-22). Keenam modul
yang ikut menentukan angka dibaca UTUH dari main pada giliran yang sama sebelum
berkas ini ditulis (KC-43).

Kendali positif dua lapis (aturan 50): kendali data
(`silang_funding.kendali_silang`, tiga simbol-bulan berparquet terbesar) dan
kendali detektor — empat bentangan BUATAN yang wajib terpisah menjadi mati_dulu,
serempak, lubang_dulu, dan tebing. Bila detektor tidak sanggup memisahkan
ketiga kelas arah pada data buatan, seluruh cacah di laporan ini batal.

Medan penggugur (aturan 24), sembilan invarian: selisih_penyebut 19586,
selisih_simbol 787, selisih_mati 1401, selisih_bangkit 8,
selisih_lubang_dalam_penyebut 877, selisih_lubang_semesta 880,
selisih_ada_lubang 122, selisih_lubang_awal 5, selisih_lubang_bukan_awal 118.
Ketiga yang terakhir mengikat laporan ini pada agregat `lubang_awal` V1 yang
sudah diterbitkan, supaya ia tidak diam-diam mengukur semesta lain.

Praregistrasi R-306 ditulis di jurnal 126 §7 SEBELUM modul ini dibuat
(aturan 79). Pitanya disalin ke tetapan di bawah dan dilapor di berkas keluaran.

Aturan yang mengikat: 10, 20, 21, 22, 24, 29, 36, 41, 44, 46, 47, 50, 52, 54,
57, 66, 73, 74, 79.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from . import kohort_ekor, lubang_awal, silang_funding

VERSI = 1
KELUARAN = "reports/lubang_tebing.json"
TOTAL_PECAHAN = lubang_awal.TOTAL_PECAHAN

# Aturan 36: bulan tebing diimpor apa adanya, TIDAK ditulis ulang harfiah.
TEBING = kohort_ekor.TEBING

# Angka yang sudah diterbitkan; penggugur, BUKAN masukan (aturan 21, 24).
PENYEBUT_TERCATAT = 19586
SIMBOL_TERCATAT = 787
MATI_TERCATAT = 1401
BANGKIT_TERCATAT = 8
LUBANG_DALAM_PENYEBUT_TERCATAT = 877
LUBANG_SEMESTA_TERCATAT = 880
ADA_LUBANG_TERCATAT = 122
LUBANG_AWAL_TERCATAT = 5
LUBANG_BUKAN_AWAL_TERCATAT = 118

# Praregistrasi R-306, jurnal 126 §7.
R306_PITA_BUTIR_1 = (0.25, 0.60)
R306_MINIMAL_PENYEBUT_BUTIR_1 = 100
R306_PITA_BUTIR_2_CACAH = (20, 90)

KELAS_MATI_DULU = "mati_dulu"
KELAS_SEREMPAK = "serempak"
KELAS_LUBANG_DULU = "lubang_dulu"
KELAS_ARAH = (KELAS_MATI_DULU, KELAS_SEREMPAK, KELAS_LUBANG_DULU)

BATAS_BARIS_LAPORAN = 60

BERKAS_DICAP = [
    "kehidupan.py",
    "kehidupan_arsip.py",
    "kohort_ekor.py",
    "lubang_awal.py",
    "lubang_tebing.py",
    "silang_funding.py",
]

Kunci = Tuple[str, str]


def nama_keluaran() -> str:
    return KELUARAN


def sidik_kode() -> str:
    """Aturan 22: cap tiap berkas yang ikut menentukan angka ini."""
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(BERKAS_DICAP):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def _bagian(a: int, b: int) -> Optional[float]:
    """Aturan 41/46: penyebut nol menghasilkan null, bukan nol."""
    return kohort_ekor.bagian(a, b) if b else None


def kelas_arah(baris: Dict[str, Any]) -> Optional[str]:
    """Kelas arah waktu satu simbol; None bila ia di luar penyebut butir 1.

    Tiga kelas saling LEPAS dan menutupi seluruh penyebut. Kesamaan bulan
    mendapat namanya sendiri (`serempak`) alih-alih ikut dihitung sebagai
    kemenangan arah seperti pada R-305 (aturan 10, ADR-A012).
    """
    if not baris.get("masuk_penyebut_butir_1"):
        return None
    mati = baris.get("bulan_mati_pertama")
    lubang = baris.get("bulan_lubang_bukan_awal_pertama")
    if not mati or not lubang:
        return None
    if mati < lubang:
        return KELAS_MATI_DULU
    if mati == lubang:
        return KELAS_SEREMPAK
    return KELAS_LUBANG_DULU


def di_tebing(baris: Dict[str, Any]) -> bool:
    """Benar bila lubang bukan-awal PERTAMA simbol ini tepat bulan tebing."""
    return str(baris.get("bulan_lubang_bukan_awal_pertama") or "") == TEBING


def perkaya(baris: Dict[str, Any]) -> Dict[str, Any]:
    """Tambahkan medan arah pada satu baris `lubang_awal` tanpa mengubah asalnya."""
    keluar = dict(baris)
    kelas = kelas_arah(baris)
    keluar["kelas_arah"] = kelas
    keluar["mati_sebelum_lubang_strikt"] = kelas == KELAS_MATI_DULU
    keluar["lubang_bukan_awal_pertama_di_tebing"] = di_tebing(baris)
    keluar["bulan_tebing"] = TEBING
    return keluar


def sebaran_arah(baris: List[Dict[str, Any]]) -> Dict[str, int]:
    """Cacah tiap kelas arah; ketiganya dilapor walau nol (aturan 46, KC-21)."""
    keluar: Dict[str, int] = {k: 0 for k in KELAS_ARAH}
    for r in baris:
        kelas = r.get("kelas_arah") if "kelas_arah" in r else kelas_arah(r)
        if kelas in keluar:
            keluar[kelas] += 1
    return keluar


def himpun(baris: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Agregat dua butir R-306; tiap cacah menyebut penyebutnya (aturan 44)."""
    kaya = [perkaya(r) for r in baris]
    p1 = [r for r in kaya if r.get("masuk_penyebut_butir_1")]
    n1 = sum(1 for r in p1 if r.get("mati_sebelum_lubang_strikt"))
    p2 = [r for r in kaya if r.get("bulan_lubang_bukan_awal_pertama")]
    n2 = sum(1 for r in p2 if r.get("lubang_bukan_awal_pertama_di_tebing"))
    return {
        "cacah_simbol": len(kaya),
        "cacah_bangkit": sum(1 for r in kaya if r.get("bangkit")),
        "cacah_mati_simbol_bulan": sum(int(r.get("cacah_mati") or 0) for r in kaya),
        "cacah_simbol_ada_lubang": sum(1 for r in kaya if r.get("cacah_lubang")),
        "cacah_simbol_lubang_awal": sum(
            1 for r in kaya if r.get("cacah_lubang_awal")
        ),
        "cacah_simbol_lubang_bukan_awal": sum(
            1 for r in kaya if r.get("cacah_lubang_bukan_awal")
        ),
        "penyebut_butir_1": len(p1),
        "numerator_butir_1": n1,
        "bagian_butir_1": _bagian(n1, len(p1)),
        "sebaran_arah": sebaran_arah(p1),
        "penyebut_butir_2": len(p2),
        "cacah_tebing_butir_2": n2,
        "bagian_tebing_butir_2": _bagian(n2, len(p2)),
    }


def kendali_deteksi() -> Dict[str, Any]:
    """Kendali positif detektor: empat bentangan BUATAN yang wajib terpisah.

    Tanpa lapis ini, `lubang_dulu` = 0 pada data nyata tidak dapat dibedakan
    dari detektor yang memang tak mampu melihatnya (aturan 50, KC-21).
    """
    h = "HIDUP"
    m = "MATI"
    peta_a = {"2024-01": h, "2024-02": m, "2024-03": h, "2024-04": h, "2024-05": h}
    a = perkaya(lubang_awal.ringkas("KENDALI_MATI_DULU", peta_a, {"2024-04"}))
    peta_b = {"2024-01": h, "2024-02": h, "2024-03": m, "2024-04": h}
    b = perkaya(lubang_awal.ringkas("KENDALI_SEREMPAK", peta_b, {"2024-03"}))
    peta_c = {"2024-01": h, "2024-02": h, "2024-03": h, "2024-04": m}
    c = perkaya(lubang_awal.ringkas("KENDALI_LUBANG_DULU", peta_c, {"2024-02"}))
    peta_d = {"2025-05": h, "2025-06": h, "2025-07": m, "2025-08": m}
    d = perkaya(
        lubang_awal.ringkas("KENDALI_TEBING", peta_d, {"2025-07", "2025-08"})
    )
    sah = bool(
        a["kelas_arah"] == KELAS_MATI_DULU
        and a["mati_sebelum_lubang_strikt"]
        and not a["lubang_bukan_awal_pertama_di_tebing"]
        and b["kelas_arah"] == KELAS_SEREMPAK
        and not b["mati_sebelum_lubang_strikt"]
        and c["kelas_arah"] == KELAS_LUBANG_DULU
        and not c["mati_sebelum_lubang_strikt"]
        and d["lubang_bukan_awal_pertama_di_tebing"]
        and d["kelas_arah"] == KELAS_SEREMPAK
        and sebaran_arah([a, b, c, d])
        == {KELAS_MATI_DULU: 1, KELAS_SEREMPAK: 2, KELAS_LUBANG_DULU: 1}
    )
    return {"baris_kendali_deteksi": [a, b, c, d], "kendali_deteksi_sah": sah}


def dalam_pita(nilai: Optional[float], pita: Tuple[float, float]) -> bool:
    if nilai is None:
        return False
    return pita[0] <= nilai <= pita[1]


def uji_r306(agregat: Dict[str, Any], ringkasan: Dict[str, Any]) -> Dict[str, Any]:
    """Adjudikasi mesin terhadap pita praregistrasi jurnal 126 §7."""
    p1 = int(agregat.get("penyebut_butir_1") or 0)
    bagian_1 = agregat.get("bagian_butir_1")
    if p1 < R306_MINIMAL_PENYEBUT_BUTIR_1:
        butir_1 = "TIDAK_TERADJUDIKASI"
    elif dalam_pita(bagian_1, R306_PITA_BUTIR_1):
        butir_1 = "MENANG"
    else:
        butir_1 = "KALAH"
    cacah_2 = int(agregat.get("cacah_tebing_butir_2") or 0)
    butir_2 = (
        "MENANG"
        if dalam_pita(
            float(cacah_2),
            (float(R306_PITA_BUTIR_2_CACAH[0]), float(R306_PITA_BUTIR_2_CACAH[1])),
        )
        else "KALAH"
    )
    butir_3 = bool(
        int(ringkasan.get("selisih_penyebut") or 0) == 0
        and int(ringkasan.get("selisih_simbol") or 0) == 0
        and int(ringkasan.get("selisih_mati") or 0) == 0
        and int(ringkasan.get("selisih_bangkit") or 0) == 0
        and int(ringkasan.get("selisih_lubang_dalam_penyebut") or 0) == 0
        and int(ringkasan.get("selisih_lubang_semesta") or 0) == 0
        and int(ringkasan.get("selisih_ada_lubang") or 0) == 0
        and int(ringkasan.get("selisih_lubang_awal") or 0) == 0
        and int(ringkasan.get("selisih_lubang_bukan_awal") or 0) == 0
        and ringkasan.get("kendali_sah")
        and ringkasan.get("kendali_deteksi_sah")
    )
    return {
        "butir_1": butir_1,
        "butir_1_penyebut": p1,
        "butir_1_bagian": bagian_1,
        "butir_1_pita": list(R306_PITA_BUTIR_1),
        "butir_1_minimal_penyebut": R306_MINIMAL_PENYEBUT_BUTIR_1,
        "butir_1_sebaran_arah": agregat.get("sebaran_arah"),
        "butir_2": butir_2,
        "butir_2_cacah": cacah_2,
        "butir_2_penyebut": agregat.get("penyebut_butir_2"),
        "butir_2_pita_cacah": list(R306_PITA_BUTIR_2_CACAH),
        "butir_3": butir_3,
        "catatan_butir_3": "MUDAH: hanya menyalin angka yang sudah terverifikasi",
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
    if not ringkasan.get("kendali_deteksi_sah"):
        return 2
    for medan in (
        "selisih_penyebut",
        "selisih_simbol",
        "selisih_mati",
        "selisih_bangkit",
        "selisih_lubang_dalam_penyebut",
        "selisih_lubang_semesta",
        "selisih_ada_lubang",
        "selisih_lubang_awal",
        "selisih_lubang_bukan_awal",
    ):
        if int(ringkasan.get(medan) or 0) != 0:
            return 2
    return 0


def jalankan(akar: str = ".", total: Optional[int] = None) -> Dict[str, Any]:
    total = TOTAL_PECAHAN if total is None else total
    status, byte_parquet, meta = silang_funding.baca_laporan_kehidupan(
        akar=akar, total=total
    )
    mentah = (Path(akar) / silang_funding.SUMBER_FUNDING).read_bytes()
    funding = json.loads(mentah.decode("utf-8"))
    lubang, meta_lubang = silang_funding.lubang_funding(funding)

    berlubang: Dict[str, Set[str]] = {}
    for simbol, bulan in lubang:
        berlubang.setdefault(str(simbol), set()).add(str(bulan))

    peta = lubang_awal.peta_status(status)
    baris: List[Dict[str, Any]] = [
        perkaya(
            lubang_awal.ringkas(simbol, peta[simbol], berlubang.get(simbol, set()))
        )
        for simbol in sorted(peta)
    ]

    agregat = himpun(baris)
    kendali = silang_funding.kendali_silang(byte_parquet, status, lubang)
    kd = kendali_deteksi()
    lubang_dalam = len(lubang & set(status))
    lubang_semesta = len(lubang)

    p1_baris = [r for r in baris if r["masuk_penyebut_butir_1"]]
    tebing_baris = [r for r in baris if r["lubang_bukan_awal_pertama_di_tebing"]]
    mati_dulu_baris = [r for r in baris if r["mati_sebelum_lubang_strikt"]]
    lubang_dulu_baris = [
        r for r in baris if r["kelas_arah"] == KELAS_LUBANG_DULU
    ]

    ringkasan: Dict[str, Any] = {
        "penyebut_kehidupan": len(status),
        "cacah_simbol": len(peta),
        "cacah_mati": agregat["cacah_mati_simbol_bulan"],
        "cacah_bangkit": agregat["cacah_bangkit"],
        "cacah_lubang_dalam_penyebut": lubang_dalam,
        "cacah_lubang_semesta": lubang_semesta,
        "bulan_tebing": TEBING,
        "selisih_penyebut": len(status) - PENYEBUT_TERCATAT,
        "selisih_simbol": len(peta) - SIMBOL_TERCATAT,
        "selisih_mati": agregat["cacah_mati_simbol_bulan"] - MATI_TERCATAT,
        "selisih_bangkit": agregat["cacah_bangkit"] - BANGKIT_TERCATAT,
        "selisih_lubang_dalam_penyebut": lubang_dalam
        - LUBANG_DALAM_PENYEBUT_TERCATAT,
        "selisih_lubang_semesta": lubang_semesta - LUBANG_SEMESTA_TERCATAT,
        "selisih_ada_lubang": agregat["cacah_simbol_ada_lubang"]
        - ADA_LUBANG_TERCATAT,
        "selisih_lubang_awal": agregat["cacah_simbol_lubang_awal"]
        - LUBANG_AWAL_TERCATAT,
        "selisih_lubang_bukan_awal": agregat["cacah_simbol_lubang_bukan_awal"]
        - LUBANG_BUKAN_AWAL_TERCATAT,
        "kendali": kendali,
        "kendali_sah": silang_funding.kendali_sah(kendali),
        "kendali_deteksi_sah": kd["kendali_deteksi_sah"],
    }
    ringkasan.update(meta)
    ringkasan.update(meta_lubang)
    ringkasan.update(agregat)

    return {
        "bukan_bukti": False,
        "versi_lubang_tebing": VERSI,
        "sidik_kode": sidik_kode(),
        "sidik_kode_lubang_awal": lubang_awal.sidik_kode(),
        "sidik_kode_silang_funding": silang_funding.sidik_kode(),
        "sidik_data_funding": hashlib.sha256(mentah).hexdigest(),
        "sumber": [silang_funding.SUMBER_FUNDING]
        + [lubang_awal.kehidupan_arsip.nama_keluaran(i) for i in range(total)],
        "definisi": {
            "mati_dulu": "bulan_mati_pertama < bulan_lubang_bukan_awal_pertama (STRIKT)",
            "serempak": "kedua bulan SAMA; kelas tautologis, bukan bukti arah",
            "lubang_dulu": "bulan_mati_pertama > lubang bukan-awal pertama",
            "di_tebing": "lubang bukan-awal pertama TEPAT bulan tebing kohort",
            "bulan_tebing": "diimpor dari kohort_ekor.TEBING apa adanya (aturan 36)",
        },
        "praregistrasi_r306": {
            "jurnal": "journal/2026-07-30-126.md",
            "bagian": "7",
            "pita_butir_1": list(R306_PITA_BUTIR_1),
            "minimal_penyebut_butir_1": R306_MINIMAL_PENYEBUT_BUTIR_1,
            "pita_butir_2_cacah": list(R306_PITA_BUTIR_2_CACAH),
            "butir_3": "MUDAH",
        },
        "baris_penyebut_butir_1": p1_baris[:BATAS_BARIS_LAPORAN],
        "cacah_baris_penyebut_butir_1_dilapor": len(p1_baris[:BATAS_BARIS_LAPORAN]),
        "baris_mati_dulu": mati_dulu_baris[:BATAS_BARIS_LAPORAN],
        "cacah_baris_mati_dulu_dilapor": len(mati_dulu_baris[:BATAS_BARIS_LAPORAN]),
        "baris_lubang_dulu": lubang_dulu_baris[:BATAS_BARIS_LAPORAN],
        "cacah_baris_lubang_dulu_dilapor": len(
            lubang_dulu_baris[:BATAS_BARIS_LAPORAN]
        ),
        "baris_tebing": tebing_baris[:BATAS_BARIS_LAPORAN],
        "cacah_baris_tebing_dilapor": len(tebing_baris[:BATAS_BARIS_LAPORAN]),
        "baris_kendali_deteksi": kd["baris_kendali_deteksi"],
        "uji_r306": uji_r306(agregat, ringkasan),
        "ringkasan": ringkasan,
        "catatan_tafsir": (
            "irisan BUKAN sebab (aturan 10). Hanya kelas mati_dulu yang berhak "
            "disebut bukti arah waktu; kelas serempak adalah tanda kedua gejala "
            "satu peristiwa, dan R-305 dulu keliru menghitungnya sebagai "
            "kemenangan karena memakai perbandingan lemah (ADR-A012)"
        ),
        "catatan_satuan": (
            "cacah_simbol_* dan penyebut_butir_* bersatuan SIMBOL; cacah_mati dan "
            "penyebut_kehidupan bersatuan SIMBOL-BULAN; bagian_* adalah BAGIAN "
            "antara 0 dan 1, bukan persen (aturan 47, KC-45)"
        ),
        "catatan_penggugur": (
            "sidik_seragam false, laporan pecahan kurang, kunci ganda, kendali data "
            "atau kendali detektor tidak sah, atau salah satu dari sembilan selisih "
            "bukan nol membatalkan SELURUH angka laporan ini (aturan 24)"
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
