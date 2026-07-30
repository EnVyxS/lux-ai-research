"""Ukur lubang funding bentuk AWAL atas SELURUH semesta - arah R-305.

R-304 MELESET: arah sebab 'kematian mendahului hilangnya funding' (ADR-A009)
GUGUR pada delapan simbol bangkit. Lima dari delapan tidak punya satu pun lubang
funding, dan dua yang tampak 'lubang dulu' ternyata berlubang tepat di BULAN
PERTAMA riwayatnya - bukan 'funding berhenti', melainkan 'funding belum mulai'
(calon KC-46). ADR-A011 membatasi H-A017 pada satu simbol saja.

Modul ini menegakkan pertanyaan itu pada penyebut BESAR, bukan delapan: apakah
arah sebab gugur juga di seluruh semesta, dan apakah lubang bentuk AWAL memang
gejala 'penerbitan belum mulai'?

Tanpa jaringan: seluruh bahannya sudah di-commit (laporan pecahan kehidupan dan
reports/funding_semesta.json). Dibaca lewat tanda tangan
silang_funding.baca_laporan_kehidupan dan silang_funding.lubang_funding yang
SUDAH dibaca utuh dari main pada giliran yang sama sebelum modul ini ditulis
(KC-43). Bentuk lubang memakai silang_funding.bentuk_lubang_lokal apa adanya
(aturan 36, KC-46): TIDAK ditulis ulang.

Definisi LOKAL (aturan 36), sama dengan praregistrasi:
- lubang awal: bentuk lokal 'awal' atau 'seluruh' - seluruh bulan klines simbol
  yang tidak lebih besar darinya juga berlubang.
- lubang bukan-awal: bentuk 'ekor' atau 'tengah' - didahului sekurangnya satu
  bulan klines yang PUNYA funding.
- bulan_pertama_berlubang: bulan klines PERTAMA simbol itu berlubang funding.
- akhir_lubang_awal: bulan terakhir rentetan berlubang yang menempel di awal.

Kendali positif dua lapis (aturan 50): kendali data
(silang_funding.kendali_silang, tiga simbol-bulan berparquet terbesar) dan
kendali detektor (dua bentangan BUATAN yang wajib terpisah). Medan penggugur
(aturan 24): selisih_penyebut 19586, selisih_simbol 787, selisih_mati 1401,
selisih_bangkit 8, selisih_lubang_dalam_penyebut 877, selisih_lubang_semesta 880.

Praregistrasi R-305 ditulis di jurnal 125 SEBELUM modul ini dibuat (aturan 79).
Irisan BUKAN sebab (aturan 10).

Aturan yang mengikat: 10, 20, 21, 22, 24, 29, 36, 41, 46, 50, 52, 54, 66, 73,
74, 79.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from . import kehidupan, kehidupan_arsip, silang_funding

VERSI = 1
KELUARAN = "reports/lubang_awal.json"
TOTAL_PECAHAN = kehidupan_arsip.TOTAL_PECAHAN

PENYEBUT_TERCATAT = 19586
SIMBOL_TERCATAT = 787
MATI_TERCATAT = 1401
BANGKIT_TERCATAT = 8
LUBANG_DALAM_PENYEBUT_TERCATAT = 877
LUBANG_SEMESTA_TERCATAT = 880

R305_PITA_BUTIR_1 = (0.55, 0.95)
R305_MINIMAL_PENYEBUT_BUTIR_1 = 100
R305_PITA_BUTIR_2_CACAH = (20, 120)
R305_MINIMAL_BAGIAN_BUTIR_2 = 0.80

POLA_BULAN = re.compile(r"^\d{4}-\d{2}$")
BATAS_BARIS_LAPORAN = 60

BERKAS_DICAP = [
    "kehidupan.py",
    "kehidupan_arsip.py",
    "lubang_awal.py",
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
    return (a / b) if b else None


def bulan_urut(peta_bulan: Dict[str, str]) -> List[str]:
    return sorted(b for b in peta_bulan if POLA_BULAN.match(str(b)))


def peta_status(status: Dict[Kunci, str]) -> Dict[str, Dict[str, str]]:
    """Susun status per simbol: {simbol: {bulan: status}}."""
    keluar: Dict[str, Dict[str, str]] = {}
    for (simbol, bulan), st in status.items():
        keluar.setdefault(str(simbol), {})[str(bulan)] = str(st)
    return keluar


def bangkit_lokal(peta_bulan: Dict[str, str]) -> bool:
    """Ada bulan HIDUP yang lebih besar daripada bulan MATI pertama."""
    urut = bulan_urut(peta_bulan)
    mati = [b for b in urut if peta_bulan[b] == kehidupan.STATUS_MATI]
    if not mati:
        return False
    return any(peta_bulan[b] == kehidupan.STATUS_HIDUP for b in urut if b > mati[0])


def ringkas(
    simbol: str, peta_bulan: Dict[str, str], berlubang: Set[str]
) -> Dict[str, Any]:
    """Satu baris: bentuk lubang funding satu simbol dipasangkan dengan kematian."""
    urut = bulan_urut(peta_bulan)
    mati = [b for b in urut if peta_bulan[b] == kehidupan.STATUS_MATI]
    mati_pertama = mati[0] if mati else None
    lubang_dalam_urut = [b for b in urut if b in berlubang]
    bentuk = {
        b: silang_funding.bentuk_lubang_lokal(urut, berlubang, b)
        for b in lubang_dalam_urut
    }
    lubang_awal = [b for b in lubang_dalam_urut if bentuk[b] in ("awal", "seluruh")]
    lubang_bukan_awal = [
        b for b in lubang_dalam_urut if bentuk[b] in ("ekor", "tengah")
    ]
    bukan_awal_pertama = lubang_bukan_awal[0] if lubang_bukan_awal else None

    akhir_awal: Optional[str] = None
    for b in urut:
        if b in berlubang:
            akhir_awal = b
        else:
            break

    bulan_pertama_berlubang = bool(urut) and urut[0] in berlubang
    masuk_1 = bool(mati) and bool(lubang_bukan_awal)
    mati_tidak_setelah = bool(masuk_1 and mati_pertama <= bukan_awal_pertama)
    if bulan_pertama_berlubang:
        berakhir: Optional[bool] = (mati_pertama is None) or (
            akhir_awal is not None and akhir_awal < mati_pertama
        )
    else:
        berakhir = None

    return {
        "simbol": simbol,
        "cacah_bulan": len(urut),
        "bulan_pertama": urut[0] if urut else None,
        "bulan_terakhir": urut[-1] if urut else None,
        "cacah_mati": len(mati),
        "bulan_mati_pertama": mati_pertama,
        "cacah_lubang": len(lubang_dalam_urut),
        "cacah_lubang_awal": len(lubang_awal),
        "cacah_lubang_bukan_awal": len(lubang_bukan_awal),
        "bulan_lubang_bukan_awal_pertama": bukan_awal_pertama,
        "bulan_pertama_berlubang": bulan_pertama_berlubang,
        "akhir_lubang_awal": akhir_awal if bulan_pertama_berlubang else None,
        "masuk_penyebut_butir_1": masuk_1,
        "mati_tidak_setelah_lubang_bukan_awal": mati_tidak_setelah,
        "lubang_awal_berakhir_sebelum_mati": berakhir,
        "bangkit": bangkit_lokal(peta_bulan),
    }


def himpun(baris: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Agregat dua butir R-305; tiap cacah punya penyebut yang tersurat."""
    p1 = [r for r in baris if r.get("masuk_penyebut_butir_1")]
    n1 = sum(1 for r in p1 if r.get("mati_tidak_setelah_lubang_bukan_awal"))
    p2 = [r for r in baris if r.get("bulan_pertama_berlubang")]
    n2 = sum(1 for r in p2 if r.get("lubang_awal_berakhir_sebelum_mati"))
    return {
        "cacah_simbol": len(baris),
        "cacah_bangkit": sum(1 for r in baris if r.get("bangkit")),
        "cacah_simbol_ada_lubang": sum(1 for r in baris if r.get("cacah_lubang")),
        "cacah_simbol_lubang_awal": sum(
            1 for r in baris if r.get("cacah_lubang_awal")
        ),
        "cacah_simbol_lubang_bukan_awal": sum(
            1 for r in baris if r.get("cacah_lubang_bukan_awal")
        ),
        "penyebut_butir_1": len(p1),
        "numerator_butir_1": n1,
        "bagian_butir_1": _bagian(n1, len(p1)),
        "penyebut_butir_2": len(p2),
        "numerator_butir_2": n2,
        "bagian_butir_2": _bagian(n2, len(p2)),
    }


def kendali_deteksi() -> Dict[str, Any]:
    """Kendali positif detektor: dua bentangan BUATAN yang wajib terpisah."""
    m, h = kehidupan.STATUS_MATI, kehidupan.STATUS_HIDUP
    peta_awal = {"2024-01": h, "2024-02": h, "2024-03": m, "2024-04": h}
    a = ringkas("KENDALI_AWAL", peta_awal, {"2024-01", "2024-02"})
    peta_bukan = {"2024-01": h, "2024-02": m, "2024-03": m, "2024-04": h}
    b = ringkas("KENDALI_BUKAN_AWAL", peta_bukan, {"2024-03"})
    sah = bool(
        a["bulan_pertama_berlubang"]
        and a["cacah_lubang_awal"] == 2
        and a["cacah_lubang_bukan_awal"] == 0
        and a["lubang_awal_berakhir_sebelum_mati"]
        and not b["bulan_pertama_berlubang"]
        and b["cacah_lubang_bukan_awal"] == 1
        and b["cacah_lubang_awal"] == 0
        and b["masuk_penyebut_butir_1"]
        and b["mati_tidak_setelah_lubang_bukan_awal"]
    )
    return {"baris_kendali_deteksi": [a, b], "kendali_deteksi_sah": sah}


def dalam_pita(nilai: Optional[float], pita: Tuple[float, float]) -> bool:
    if nilai is None:
        return False
    return pita[0] <= nilai <= pita[1]


def uji_r305(agregat: Dict[str, Any], ringkasan: Dict[str, Any]) -> Dict[str, Any]:
    """Adjudikasi mesin terhadap pita praregistrasi jurnal 125."""
    p1 = int(agregat.get("penyebut_butir_1") or 0)
    bagian_1 = agregat.get("bagian_butir_1")
    if p1 < R305_MINIMAL_PENYEBUT_BUTIR_1:
        butir_1 = "TIDAK_TERADJUDIKASI"
    elif dalam_pita(bagian_1, R305_PITA_BUTIR_1):
        butir_1 = "MENANG"
    else:
        butir_1 = "KALAH"
    cacah_2 = int(agregat.get("penyebut_butir_2") or 0)
    bagian_2 = agregat.get("bagian_butir_2")
    b2_pita = dalam_pita(float(cacah_2), (float(R305_PITA_BUTIR_2_CACAH[0]), float(R305_PITA_BUTIR_2_CACAH[1])))
    b2_bagian = bagian_2 is not None and bagian_2 >= R305_MINIMAL_BAGIAN_BUTIR_2
    butir_2 = "MENANG" if (b2_pita and b2_bagian) else "KALAH"
    butir_3 = bool(
        int(ringkasan.get("selisih_penyebut") or 0) == 0
        and int(ringkasan.get("selisih_simbol") or 0) == 0
        and int(ringkasan.get("selisih_mati") or 0) == 0
        and int(ringkasan.get("selisih_bangkit") or 0) == 0
        and int(ringkasan.get("selisih_lubang_dalam_penyebut") or 0) == 0
        and int(ringkasan.get("selisih_lubang_semesta") or 0) == 0
        and ringkasan.get("kendali_sah")
        and ringkasan.get("kendali_deteksi_sah")
    )
    return {
        "butir_1": butir_1,
        "butir_1_penyebut": p1,
        "butir_1_bagian": bagian_1,
        "butir_1_pita": list(R305_PITA_BUTIR_1),
        "butir_1_minimal_penyebut": R305_MINIMAL_PENYEBUT_BUTIR_1,
        "butir_2": butir_2,
        "butir_2_cacah": cacah_2,
        "butir_2_pita_cacah": list(R305_PITA_BUTIR_2_CACAH),
        "butir_2_bagian": bagian_2,
        "butir_2_minimal_bagian": R305_MINIMAL_BAGIAN_BUTIR_2,
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

    peta = peta_status(status)
    baris: List[Dict[str, Any]] = [
        ringkas(simbol, peta[simbol], berlubang.get(simbol, set()))
        for simbol in sorted(peta)
    ]

    agregat = himpun(baris)
    kendali = silang_funding.kendali_silang(byte_parquet, status, lubang)
    kd = kendali_deteksi()
    cacah_mati = sum(1 for st in status.values() if st == kehidupan.STATUS_MATI)
    lubang_dalam = len(lubang & set(status))
    lubang_semesta = len(lubang)

    p1_baris = [r for r in baris if r["masuk_penyebut_butir_1"]]
    p2_baris = [r for r in baris if r["bulan_pertama_berlubang"]]

    ringkasan: Dict[str, Any] = {
        "penyebut_kehidupan": len(status),
        "cacah_simbol": len(peta),
        "cacah_mati": cacah_mati,
        "cacah_bangkit": agregat["cacah_bangkit"],
        "cacah_lubang_dalam_penyebut": lubang_dalam,
        "cacah_lubang_semesta": lubang_semesta,
        "selisih_penyebut": len(status) - PENYEBUT_TERCATAT,
        "selisih_simbol": len(peta) - SIMBOL_TERCATAT,
        "selisih_mati": cacah_mati - MATI_TERCATAT,
        "selisih_bangkit": agregat["cacah_bangkit"] - BANGKIT_TERCATAT,
        "selisih_lubang_dalam_penyebut": lubang_dalam - LUBANG_DALAM_PENYEBUT_TERCATAT,
        "selisih_lubang_semesta": lubang_semesta - LUBANG_SEMESTA_TERCATAT,
        "kendali": kendali,
        "kendali_sah": silang_funding.kendali_sah(kendali),
        "kendali_deteksi_sah": kd["kendali_deteksi_sah"],
    }
    ringkasan.update(meta)
    ringkasan.update(meta_lubang)
    ringkasan.update(agregat)

    return {
        "bukan_bukti": False,
        "versi_lubang_awal": VERSI,
        "sidik_kode": sidik_kode(),
        "sidik_kode_silang_funding": silang_funding.sidik_kode(),
        "sidik_data_funding": hashlib.sha256(mentah).hexdigest(),
        "sumber": [silang_funding.SUMBER_FUNDING]
        + [kehidupan_arsip.nama_keluaran(i) for i in range(total)],
        "definisi": {
            "lubang_awal": "bentuk lokal awal atau seluruh (silang_funding.bentuk_lubang_lokal)",
            "lubang_bukan_awal": "bentuk lokal ekor atau tengah",
            "bulan_pertama_berlubang": "bulan klines pertama simbol berlubang funding",
            "lubang_funding": "bulan punya klines tetapi tidak punya fundingRate",
        },
        "praregistrasi_r305": {
            "jurnal": "journal/2026-07-30-125.md",
            "pita_butir_1": list(R305_PITA_BUTIR_1),
            "minimal_penyebut_butir_1": R305_MINIMAL_PENYEBUT_BUTIR_1,
            "pita_butir_2_cacah": list(R305_PITA_BUTIR_2_CACAH),
            "minimal_bagian_butir_2": R305_MINIMAL_BAGIAN_BUTIR_2,
            "butir_3": "MUDAH",
        },
        "baris_penyebut_butir_1": p1_baris[:BATAS_BARIS_LAPORAN],
        "cacah_baris_penyebut_butir_1_dilapor": len(p1_baris[:BATAS_BARIS_LAPORAN]),
        "baris_penyebut_butir_2": p2_baris[:BATAS_BARIS_LAPORAN],
        "cacah_baris_penyebut_butir_2_dilapor": len(p2_baris[:BATAS_BARIS_LAPORAN]),
        "baris_kendali_deteksi": kd["baris_kendali_deteksi"],
        "uji_r305": uji_r305(agregat, ringkasan),
        "ringkasan": ringkasan,
        "catatan_tafsir": (
            "irisan BUKAN sebab (aturan 10): urutan bulan hanya menyingkirkan satu "
            "arah bila seragam; penyebut butir 1 wajib >=100 atau TIDAK TERADJUDIKASI"
        ),
        "catatan_penggugur": (
            "sidik_seragam false, laporan pecahan kurang, kunci ganda, kendali data "
            "atau kendali detektor tidak sah, atau salah satu selisih bukan nol "
            "membatalkan seluruh angka (aturan 24)"
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
