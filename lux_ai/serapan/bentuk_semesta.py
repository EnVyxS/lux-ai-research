"""Cetak KERANGKA reports/semesta_bulan_1m.json (pra-registrasi R-48, R-49).

`ringkas_semesta` gagal mengenali skema berkas ini (jurnal 22). Modul ini tidak
mengukur apa pun tentang data; ia hanya memaparkan bentuknya supaya pengumpul
berikutnya disusun dari fakta, bukan tebakan. Berkas TIDAK dibaca utuh oleh
agen: hanya kerangka terpotong yang di-commit.

Aturan 30: penyebut (`cacah_kunci_tingkat_atas`) dicetak eksplisit, dan bila nol
laporan menuliskan status TIDAK MENGUKUR.
"""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

AKAR_REPO = Path(__file__).resolve().parents[2]
SUMBER = AKAR_REPO / "reports" / "semesta_bulan_1m.json"
LAPORAN = AKAR_REPO / "reports" / "bentuk_semesta.json"

BATAS_KUNCI = 40
BATAS_CONTOH = 200
BATAS_DALAM = 8
TIDAK_MENGUKUR = "TIDAK MENGUKUR"
MENGUKUR = "MENGUKUR"


def sidik_kode() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def sidik_data(mentah: str) -> str:
    return hashlib.sha256(mentah.encode("utf-8")).hexdigest()


def sekarang() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def tulis(path: Path, isi: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(isi, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def tipe_dari(nilai) -> str:
    if isinstance(nilai, dict):
        return "objek"
    if isinstance(nilai, list):
        return "daftar"
    if isinstance(nilai, bool):
        return "bool"
    if isinstance(nilai, (int, float)):
        return "angka"
    if isinstance(nilai, str):
        return "teks"
    return "kosong"


def potong(nilai, batas: int = BATAS_CONTOH) -> str:
    teks = json.dumps(nilai, ensure_ascii=False, sort_keys=True)
    return teks if len(teks) <= batas else teks[:batas] + "..."


def cabang_pertama(simpul, batas_dalam: int = BATAS_DALAM) -> dict:
    """Turuni cabang pertama sampai nilai bukan wadah atau batas kedalaman."""
    jejak = []
    kini = simpul
    for _ in range(batas_dalam):
        if isinstance(kini, dict) and kini:
            kunci = next(iter(kini))
            jejak.append(str(kunci))
            kini = kini[kunci]
        elif isinstance(kini, list) and kini:
            jejak.append("[0]")
            kini = kini[0]
        else:
            break
    return {"jejak": jejak, "contoh": potong(kini), "tipe": tipe_dari(kini)}


def kerangka(akar) -> dict:
    kunci = list(akar) if isinstance(akar, dict) else []
    terpakai = [str(k) for k in kunci[:BATAS_KUNCI]]
    tipe_nilai = {}
    cacah_elemen = {}
    for satu in terpakai:
        nilai = akar[satu]
        tipe_nilai[satu] = tipe_dari(nilai)
        if isinstance(nilai, (dict, list)):
            cacah_elemen[satu] = len(nilai)
    return {
        "tipe_akar": tipe_dari(akar),
        "cacah_kunci_tingkat_atas": len(kunci),
        "kunci_tingkat_atas": terpakai,
        "kunci_dipotong": len(kunci) > BATAS_KUNCI,
        "tipe_nilai": tipe_nilai,
        "cacah_elemen_nilai": cacah_elemen,
        "cabang_pertama": cabang_pertama(akar),
        "status": TIDAK_MENGUKUR if not kunci else MENGUKUR,
    }


def jalankan() -> int:
    isi = {
        "nama": "bentuk_semesta",
        "bukan_bukti": True,
        "sumber": "reports/semesta_bulan_1m.json",
        "sidik_kode": sidik_kode(),
        "waktu_utc": sekarang(),
        "catatan_metode": (
            "Hanya kerangka: tipe akar, kunci tingkat atas (maks 40), tipe dan "
            "cacah elemen tiap nilai, serta satu cabang pertama terpotong 200 "
            "aksara. Tidak ada klaim tentang isi data."
        ),
    }
    if not SUMBER.exists():
        isi["status"] = TIDAK_MENGUKUR
        isi["galat"] = "berkas sumber tidak ada"
        tulis(LAPORAN, isi)
        return 1
    mentah = SUMBER.read_text(encoding="utf-8")
    isi["byte_sumber"] = len(mentah.encode("utf-8"))
    isi["sidik_data"] = sidik_data(mentah)
    try:
        akar = json.loads(mentah)
    except json.JSONDecodeError as galat:
        isi["status"] = TIDAK_MENGUKUR
        isi["galat"] = "json tidak sah: " + str(galat)
        tulis(LAPORAN, isi)
        return 1
    hasil = kerangka(akar)
    isi["kerangka"] = hasil
    isi["status"] = hasil["status"]
    tulis(LAPORAN, isi)
    return 0


if __name__ == "__main__":
    sys.exit(jalankan())
