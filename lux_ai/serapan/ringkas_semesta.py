"""Ringkas reports/semesta_bulan_1m.json DI RUNNER (utang 19).

Agen tidak boleh membaca berkas sumber utuh; modul ini membacanya di runner dan
menulis laporan kecil. Skema sumber BELUM pernah dilihat saat modul ini ditulis,
jadi pengumpulan dibuat rekursif dan bentuk yang tidak dikenali DITANDAI, bukan
ditebak. Keluaran diagnostik (aturan 10): "bukan_bukti": true.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

AKAR_REPO = Path(__file__).resolve().parents[2]
SUMBER = AKAR_REPO / "reports" / "semesta_bulan_1m.json"
LAPORAN = AKAR_REPO / "reports" / "ringkas_semesta.json"

POLA_BULAN = re.compile(r"^\d{4}-\d{2}$")
POLA_SIMBOL = re.compile(r"^[A-Z0-9_]{2,20}$")
KUNCI_BULAN = ("bulan", "month", "bulan_1m")
BATAS_AWAL = "2020-01"
BATAS_AKHIR = "2026-06"


def sidik_kode() -> str:
    """sha256 atas berkas modul ini sendiri (aturan 22)."""
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def sidik_data(mentah: str) -> str:
    return hashlib.sha256(mentah.encode("utf-8")).hexdigest()


def sekarang() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def tulis(path: Path, isi: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(isi, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def bulan_dari(nilai) -> list:
    """Ambil daftar bulan 'YYYY-MM' dari sebuah nilai, tanpa menebak."""
    if isinstance(nilai, str):
        return [nilai] if POLA_BULAN.match(nilai) else []
    if isinstance(nilai, list):
        keluar = []
        for item in nilai:
            if isinstance(item, str) and POLA_BULAN.match(item):
                keluar.append(item)
            elif isinstance(item, dict):
                for kunci in KUNCI_BULAN:
                    dalam = item.get(kunci)
                    if isinstance(dalam, str) and POLA_BULAN.match(dalam):
                        keluar.append(dalam)
                        break
        return keluar
    return []


def kumpulkan(simpul, keluar=None) -> dict:
    """Kumpulkan peta simbol -> daftar bulan dari struktur sedalam apa pun."""
    if keluar is None:
        keluar = {}
    if isinstance(simpul, dict):
        for kunci, nilai in simpul.items():
            bulan = bulan_dari(nilai)
            if bulan and POLA_SIMBOL.match(str(kunci)):
                keluar.setdefault(str(kunci), []).extend(bulan)
            else:
                kumpulkan(nilai, keluar)
    elif isinstance(simpul, list):
        for item in simpul:
            kumpulkan(item, keluar)
    return keluar


def ringkas(peta: dict) -> dict:
    """Ringkas peta simbol -> bulan, termasuk medan penggugur (aturan 24)."""
    simbol_tanpa_bulan = sorted(s for s, b in peta.items() if not b)
    bulan_duplikat = 0
    bulan_tidak_terurut = 0
    bulan_di_luar_rentang_survei = []
    entri_simbol_bulan = 0
    paling_awal = None
    paling_akhir = None
    simbol_akhir_2024_05 = 0
    for simbol in sorted(peta):
        bulan = peta[simbol]
        entri_simbol_bulan += len(bulan)
        bulan_duplikat += len(bulan) - len(set(bulan))
        if list(bulan) != sorted(bulan):
            bulan_tidak_terurut += 1
        for satu in bulan:
            if satu < BATAS_AWAL or satu > BATAS_AKHIR:
                bulan_di_luar_rentang_survei.append(simbol + ":" + satu)
        if bulan:
            awal = min(bulan)
            akhir = max(bulan)
            if paling_awal is None or awal < paling_awal:
                paling_awal = awal
            if paling_akhir is None or akhir > paling_akhir:
                paling_akhir = akhir
            if akhir == "2024-05":
                simbol_akhir_2024_05 += 1
    return {
        "cacah_simbol": len(peta),
        "entri_simbol_bulan": entri_simbol_bulan,
        "bulan_paling_awal": paling_awal,
        "bulan_paling_akhir": paling_akhir,
        "simbol_akhir_2024_05": simbol_akhir_2024_05,
        "simbol_tanpa_bulan": simbol_tanpa_bulan,
        "cacah_simbol_tanpa_bulan": len(simbol_tanpa_bulan),
        "bulan_duplikat": bulan_duplikat,
        "bulan_tidak_terurut": bulan_tidak_terurut,
        "bulan_di_luar_rentang_survei": bulan_di_luar_rentang_survei[:20],
        "cacah_bulan_di_luar_rentang_survei": len(bulan_di_luar_rentang_survei),
    }


def jalankan() -> int:
    isi = {
        "nama": "ringkas_semesta",
        "bukan_bukti": True,
        "sumber": "reports/semesta_bulan_1m.json",
        "sidik_kode": sidik_kode(),
        "waktu_utc": sekarang(),
        "catatan_metode": (
            "Peta simbol->bulan dikumpulkan rekursif; kunci diterima sebagai "
            "simbol hanya bila nilainya memuat bulan berpola YYYY-MM. Bentuk "
            "yang tidak menghasilkan satu pun simbol ditandai "
            "bentuk_tak_dikenali, bukan ditebak (aturan 16)."
        ),
    }
    if not SUMBER.exists():
        isi["bentuk_tak_dikenali"] = True
        isi["galat"] = "berkas sumber tidak ada"
        tulis(LAPORAN, isi)
        return 1
    mentah = SUMBER.read_text(encoding="utf-8")
    isi["byte_sumber"] = len(mentah.encode("utf-8"))
    isi["sidik_data"] = sidik_data(mentah)
    try:
        akar = json.loads(mentah)
    except json.JSONDecodeError as galat:
        isi["bentuk_tak_dikenali"] = True
        isi["galat"] = "json tidak sah: " + str(galat)
        tulis(LAPORAN, isi)
        return 1
    peta = kumpulkan(akar)
    isi["bentuk_tak_dikenali"] = not peta
    isi["ringkas"] = ringkas(peta)
    tulis(LAPORAN, isi)
    return 0


if __name__ == "__main__":
    sys.exit(jalankan())
