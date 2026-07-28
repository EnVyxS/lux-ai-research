"""Selisih dua definisi "simbol terhenti" (utang 28, aturan 36).

`survei.py` menghitung terhenti sebagai `selisih_bulan(bulan_terakhir,
bulan_tutup) >= 2`, sedangkan `taksonomi.py` memakai `bulan_terakhir <
"2026-06"`. Keduanya memberi angka berbeda (128 lawan 129), dan aturan 36
melarang selisih itu dibiarkan tanpa nama.

Modul ini menghitung KEDUA definisi atas sumber yang sama lalu menyebut nama
simbol pada selisih himpunan KEDUA ARAH. Arah kedua (`hanya_survei`) adalah
medan penggugur (aturan 24): bila ia tidak kosong, dugaan "selisihnya semata
soal ambang bulan" salah.

`selisih_bulan` DISALIN dari `survei.py`, bukan diimpor, agar modul ini tidak
menarik paket serapan. Uji `test_terhenti.py` memaksa kedua salinan sepakat.

Tidak menyentuh jaringan (aturan 13).
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

SUMBER = "reports/semesta_rentang.json"
KELUARAN = "reports/terhenti_semesta.json"

# Nilai yang dipakai survei.py saat laporan 128/809 dibuat.
JEDA_MATI_BULAN = 2

# Berapa bulan terakhir yang cacahnya dilaporkan walau nol (aturan 24).
EKOR_BULAN = 4

BATAS_CONTOH = 20


def sidik_kode() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def sidik_data(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _pecah(bulan: str) -> Tuple[int, int]:
    tahun, bln = bulan.split("-")
    return int(tahun), int(bln)


def selisih_bulan(lebih_tua: str, acuan: str) -> int:
    """Berapa bulan `lebih_tua` tertinggal di belakang `acuan`.

    DISALIN dari `lux_ai/serapan/survei.py`. Bila salinan ini menyimpang, uji
    kesepakatan akan pecah.
    """
    ta, ba = _pecah(lebih_tua)
    tb, bb = _pecah(acuan)
    return (tb - ta) * 12 + (bb - ba)


def mundur_bulan(bulan: str, langkah: int) -> str:
    """Bulan YYYY-MM sekian langkah sebelum `bulan`."""
    tahun, bln = _pecah(bulan)
    total = tahun * 12 + (bln - 1) - langkah
    return f"{total // 12:04d}-{total % 12 + 1:02d}"


def terhenti_survei(bulan_terakhir: str, acuan: str, jeda: int = JEDA_MATI_BULAN) -> bool:
    return selisih_bulan(bulan_terakhir, acuan) >= jeda


def terhenti_taksonomi(bulan_terakhir: str, acuan: str) -> bool:
    return bulan_terakhir < acuan


def bandingkan(rentang: Dict[str, Any]) -> Dict[str, Any]:
    """Bandingkan kedua definisi atas peta simbol -> rentang."""
    sah = {
        simbol: isi["bulan_terakhir"]
        for simbol, isi in rentang.items()
        if isinstance(isi, dict) and isinstance(isi.get("bulan_terakhir"), str)
    }
    if not sah:
        return {
            "bukan_bukti": True,
            "status": "TIDAK MENGUKUR",
            "penyebut": {"entri_dibaca": len(rentang), "cacah_simbol": 0},
            "bulan_tutup_terakhir": None,
            "cacah_terhenti_survei": 0,
            "cacah_terhenti_taksonomi": 0,
            "hanya_taksonomi": [],
            "hanya_survei": [],
            "cacah_per_bulan_terakhir_ekor": {},
            "jeda_mati_bulan": JEDA_MATI_BULAN,
        }

    acuan = max(sah.values())

    set_survei = {s for s, b in sah.items() if terhenti_survei(b, acuan)}
    set_taksonomi = {s for s, b in sah.items() if terhenti_taksonomi(b, acuan)}

    hanya_taksonomi = sorted(set_taksonomi - set_survei)
    hanya_survei = sorted(set_survei - set_taksonomi)

    ekor: Dict[str, int] = {}
    for langkah in range(EKOR_BULAN):
        bulan = mundur_bulan(acuan, langkah)
        ekor[bulan] = sum(1 for b in sah.values() if b == bulan)

    rincian: List[Dict[str, str]] = [
        {"simbol": s, "bulan_terakhir": sah[s]}
        for s in (hanya_taksonomi + hanya_survei)[:BATAS_CONTOH]
    ]

    return {
        "bukan_bukti": True,
        "status": "TERUKUR",
        "penyebut": {"entri_dibaca": len(rentang), "cacah_simbol": len(sah)},
        "bulan_tutup_terakhir": acuan,
        "jeda_mati_bulan": JEDA_MATI_BULAN,
        "ambang_survei": mundur_bulan(acuan, JEDA_MATI_BULAN),
        "ambang_taksonomi": mundur_bulan(acuan, 1),
        "cacah_terhenti_survei": len(set_survei),
        "cacah_terhenti_taksonomi": len(set_taksonomi),
        "cacah_hanya_taksonomi": len(hanya_taksonomi),
        "cacah_hanya_survei": len(hanya_survei),
        "hanya_taksonomi": hanya_taksonomi[:BATAS_CONTOH],
        "hanya_survei": hanya_survei[:BATAS_CONTOH],
        "rincian_selisih": rincian,
        "cacah_per_bulan_terakhir_ekor": ekor,
    }


def jalankan(akar: str = ".") -> Dict[str, Any]:
    basis = Path(akar)
    mentah = (basis / SUMBER).read_bytes()
    muatan = json.loads(mentah.decode("utf-8"))
    rentang = muatan.get("rentang", {})
    if not isinstance(rentang, dict):
        rentang = {}

    laporan = bandingkan(rentang)
    laporan["sumber"] = SUMBER
    laporan["sumber_byte"] = len(mentah)
    laporan["sidik_data"] = sidik_data(mentah)
    laporan["sidik_kode"] = sidik_kode()

    tujuan = basis / KELUARAN
    tujuan.parent.mkdir(parents=True, exist_ok=True)
    tujuan.write_text(
        json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return laporan


def main() -> None:
    print(json.dumps(jalankan(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
