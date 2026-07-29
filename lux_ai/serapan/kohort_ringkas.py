"""Ringkasan kohort ekor yang cukup kecil untuk dibaca utuh.

`reports/kohort_ekor.json` VERSI 3 memuat satu baris per simbol-bulan yang
dipindai (10 simbol × 15 bulan + 4 kendali hidup = 154 baris) dan menjadi terlalu
besar untuk dibaca seluruhnya. Pelajaran yang sama pernah didapat dari manifes
pecahan: laporan yang tidak terbaca sama saja dengan laporan yang tidak ada.

Modul ini TIDAK mengukur apa pun. Ia menyalin `ringkasan`, `riwayat`, dan seluruh
medan catatan dari laporan penuh, membuang medan `baris`, lalu mencatat
`sidik_sumber` — SHA256 atas byte berkas sumber — supaya ringkasan ini dapat
dibuktikan berasal dari laporan penuh yang itu juga, bukan dari sisa run lama.

Karena tak satu angka pun lahir di sini, modul ini tidak masuk `BERKAS_DICAP`
milik `kohort_ekor.py`; yang menjaganya adalah `sidik_sumber` dan uji kesamaan
medan.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

VERSI = 1
SUMBER = "reports/kohort_ekor.json"
KELUARAN = "reports/kohort_ekor_ringkas.json"

# Medan yang dibuang justru karena besarnya. Hanya ini yang boleh hilang.
BUANG = ("baris",)


def sidik_byte(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def ringkas_laporan(laporan: dict) -> dict:
    """Salin laporan tanpa medan besar, dan catat apa yang dibuang.

    Cacah baris yang dibuang tetap dilaporkan supaya penyusutan berkas tidak
    menyamarkan run yang gagal mengukur sebagian simbol.
    """
    keluar = {k: v for k, v in laporan.items() if k not in BUANG}
    baris = laporan.get("baris")
    keluar["cacah_baris_penuh"] = len(baris) if isinstance(baris, list) else None
    keluar["medan_dibuang"] = [k for k in BUANG if k in laporan]
    keluar["versi_kohort_ringkas"] = VERSI
    return keluar


def jalankan(akar: str = ".") -> dict:
    jalur = Path(akar) / SUMBER
    if not jalur.exists():
        return {"galat_ringkas": f"{SUMBER} tidak ada", "versi_kohort_ringkas": VERSI}
    data = jalur.read_bytes()
    try:
        laporan = json.loads(data.decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as exc:
        return {
            "galat_ringkas": f"{SUMBER} tidak terbaca: {exc}",
            "sidik_sumber": sidik_byte(data),
            "versi_kohort_ringkas": VERSI,
        }
    keluar = ringkas_laporan(laporan)
    keluar["galat_ringkas"] = None
    keluar["sidik_sumber"] = sidik_byte(data)
    keluar["sumber_ringkas"] = SUMBER
    return keluar


def main() -> int:
    hasil = jalankan(".")
    Path(KELUARAN).parent.mkdir(parents=True, exist_ok=True)
    with open(KELUARAN, "w", encoding="utf-8") as f:
        json.dump(hasil, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    if hasil.get("galat_ringkas"):
        print(hasil["galat_ringkas"])
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
