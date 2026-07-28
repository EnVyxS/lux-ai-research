"""Penyebut KC-6 (utang 21): mengubah cacah mutlak menjadi laju.

`reports/rentang_kc6.json` memuat 2.530 bucket `open` beda, tetapi tanpa
penyebutnya angka itu tidak berarti apa-apa (aturan 18). Berkas sumbernya 177 KB
dan terlalu besar untuk dibaca agen, jadi penjumlahannya dikerjakan runner dan
hasilnya ditulis sebagai laporan kecil.

Modul ini TIDAK menyentuh jaringan: masukannya berkas yang sudah ada di repo.
Keluarannya diagnostik (aturan 10) dan tidak boleh menyentuh gerbang mana pun.

Dijalankan sebagai `python -m lux_ai.serapan.penyebut_kc6`.
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

AKAR_REPO = Path(__file__).resolve().parents[2]
SUMBER = AKAR_REPO / "reports" / "rentang_kc6.json"
LAPORAN = AKAR_REPO / "reports" / "penyebut_kc6.json"

MEDAN = ("bucket_dibandingkan", "bucket_ohlc_beda", "bucket_open_beda")
PENANDA = ("awal", "kendali")


def sidik_kode() -> str:
    """Aturan 22. Modul ini tidak memanggil modul lain, jadi cakupannya satu berkas."""
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def sidik_data(mentah: bytes) -> str:
    return hashlib.sha256(mentah).hexdigest()


def sekarang() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def tulis(path: Path, isi: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(isi, indent=2, ensure_ascii=False, sort_keys=True) + "\n")


def persen(bagian: int, total: int):
    """Persentase yang menolak berbohong saat penyebutnya nol."""
    if not total:
        return None
    return round(100.0 * bagian / total, 4)


def penanda_dari(simpul: dict, warisan: str) -> str:
    """Cari penanda kelompok di antara nilai teks simpul.

    Ini heuristik atas teks, bukan medan resmi; penamaan medan hasilnya
    menyebutkannya secara eksplisit (aturan 16).
    """
    for nilai in simpul.values():
        if isinstance(nilai, str) and nilai in PENANDA:
            return nilai
    return warisan


def kumpulkan(simpul, warisan: str = "tak_dikenal", keluar=None) -> list:
    """Kumpulkan setiap simpul yang punya `bucket_dibandingkan`, sedalam apa pun.

    Sengaja tidak mengandalkan bentuk sarang laporan sumber: menebak skema
    masukan adalah cara termurah menghasilkan angka palsu.
    """
    if keluar is None:
        keluar = []
    if isinstance(simpul, dict):
        peran = penanda_dari(simpul, warisan)
        if "bucket_dibandingkan" in simpul:
            catatan = {"kelompok_dari_penanda_teks": peran}
            for medan in MEDAN:
                catatan[medan] = int(simpul.get(medan) or 0)
            keluar.append(catatan)
        for nilai in simpul.values():
            kumpulkan(nilai, peran, keluar)
    elif isinstance(simpul, list):
        for nilai in simpul:
            kumpulkan(nilai, warisan, keluar)
    return keluar


def ringkas(terkumpul) -> dict:
    """Cacah per kelompok plus total, dengan lajunya."""
    kelompok = {}
    total = {"simpul": 0}
    for medan in MEDAN:
        total[medan] = 0
    for catatan in terkumpul:
        nama = catatan["kelompok_dari_penanda_teks"]
        bagian = kelompok.get(nama)
        if bagian is None:
            bagian = {"simpul": 0}
            for medan in MEDAN:
                bagian[medan] = 0
            kelompok[nama] = bagian
        bagian["simpul"] += 1
        total["simpul"] += 1
        for medan in MEDAN:
            bagian[medan] += catatan[medan]
            total[medan] += catatan[medan]
    for bagian in list(kelompok.values()) + [total]:
        bagian["laju_open_beda_persen"] = persen(
            bagian["bucket_open_beda"], bagian["bucket_dibandingkan"]
        )
        bagian["laju_ohlc_beda_persen"] = persen(
            bagian["bucket_ohlc_beda"], bagian["bucket_dibandingkan"]
        )
    return {"per_kelompok": kelompok, "total": total}


def jalankan() -> dict:
    mentah = SUMBER.read_bytes()
    data = json.loads(mentah)
    laporan = {
        "nama": "penyebut_kc6",
        "bukan_bukti": True,
        "waktu_utc": sekarang(),
        "sidik_kode": sidik_kode(),
        "sidik_data": sidik_data(mentah),
        "sumber": "reports/rentang_kc6.json",
        "byte_sumber": len(mentah),
        "catatan_metode": (
            "Simpul dikumpulkan rekursif dari setiap dict yang punya medan "
            "bucket_dibandingkan. Kelompok awal/kendali disimpulkan dari penanda "
            "teks di laporan sumber, bukan dari medan khusus; karena itu namanya "
            "kelompok_dari_penanda_teks (aturan 16)."
        ),
        "ringkas": ringkas(kumpulkan(data)),
    }
    tulis(LAPORAN, laporan)
    return laporan


if __name__ == "__main__":
    print(json.dumps(jalankan(), indent=2, ensure_ascii=False))
    sys.exit(0)
