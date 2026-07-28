"""Ringkas reports/semesta_bulan_1m.json DI RUNNER (utang 19).

Agen tidak boleh membaca berkas sumber utuh; modul ini membacanya di runner dan
menulis laporan kecil. Skema sumber terungkap pada sesi 23 lewat
`bentuk_semesta`: akar objek dengan dua kunci, `bulan_per_simbol` (peta simbol ->
CACAH bulan, bertipe angka) dan `waktu_utc`. Jalur lama untuk peta simbol ->
DAFTAR bulan sengaja DIPERTAHANKAN, sebab berkas survei lain memakai bentuk itu.
Bentuk yang tidak dikenali tetap DITANDAI, bukan ditebak.

Sesi 24: pengukuran memberi 934 simbol, bukan 937. Karena itu kunci yang GAGAL
`POLA_SIMBOL` padahal nilainya angka kini dihitung sebagai
`cacah_kunci_ditolak_pola`, lengkap dengan contohnya. Sebelumnya kunci semacam
itu lenyap tanpa jejak, dan penyaring saya sendiri bisa mencuri simbol.

Aturan 10: keluaran diagnostik menandai "bukan_bukti": true.
Aturan 30: penyebut dicetak eksplisit; bila nol, status TIDAK MENGUKUR.
Aturan 31: `sidik_data` sumber selalu dicatat.
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
BATAS_BULAN = 78  # 2020-01..2026-06 inklusif
BATAS_CONTOH_KUNCI = 10
TIDAK_MENGUKUR = "TIDAK MENGUKUR"
MENGUKUR = "MENGUKUR"


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


def penggugur_kosong() -> dict:
    return {
        "cacah_nilai_bukan_angka": 0,
        "cacah_kunci_ditolak_pola": 0,
        "contoh_kunci_ditolak": [],
        "panjang_nama_terpanjang": 0,
    }


def kumpulkan_cacah(simpul, keluar=None, penggugur=None) -> dict:
    """Kumpulkan peta simbol -> CACAH bulan (angka bulat, bukan bool).

    Tiga nasib sebuah kunci dicatat, tidak ada yang dibuang diam-diam:
    diterima; lolos pola tetapi nilainya bukan angka; atau ditolak pola padahal
    nilainya angka (`cacah_kunci_ditolak_pola`).
    """
    if keluar is None:
        keluar = {}
    if penggugur is None:
        penggugur = penggugur_kosong()
    if isinstance(simpul, dict):
        for kunci, nilai in simpul.items():
            teks = str(kunci)
            simbol = POLA_SIMBOL.match(teks)
            angka = isinstance(nilai, int) and not isinstance(nilai, bool)
            if isinstance(nilai, (dict, list)):
                kumpulkan_cacah(nilai, keluar, penggugur)
                continue
            if simbol and angka:
                keluar[teks] = nilai
            elif simbol:
                penggugur["cacah_nilai_bukan_angka"] += 1
            elif angka:
                penggugur["cacah_kunci_ditolak_pola"] += 1
                if len(penggugur["contoh_kunci_ditolak"]) < BATAS_CONTOH_KUNCI:
                    penggugur["contoh_kunci_ditolak"].append(teks)
            else:
                continue
            if len(teks) > penggugur["panjang_nama_terpanjang"]:
                penggugur["panjang_nama_terpanjang"] = len(teks)
    elif isinstance(simpul, list):
        for item in simpul:
            kumpulkan_cacah(item, keluar, penggugur)
    return {"peta": keluar, **penggugur}


def ringkas_cacah(peta: dict) -> dict:
    """Ringkas peta simbol -> cacah bulan, dengan penyebut eksplisit."""
    nilai = [peta[s] for s in sorted(peta)]
    negatif = sum(1 for n in nilai if n < 0)
    melebihi = sum(1 for n in nilai if n > BATAS_BULAN)
    terkecil = min(nilai) if nilai else None
    terbesar = max(nilai) if nilai else None
    return {
        "cacah_simbol": len(peta),
        "total_berkas_bulan": sum(nilai),
        "cacah_minimum": terkecil,
        "cacah_maksimum": terbesar,
        "simbol_minimum": sorted(s for s in peta if peta[s] == terkecil)[:5],
        "simbol_maksimum": sorted(s for s in peta if peta[s] == terbesar)[:5],
        "cacah_nilai_negatif": negatif,
        "cacah_nilai_melebihi_78": melebihi,
        "status": TIDAK_MENGUKUR if not peta else MENGUKUR,
    }


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
        "status": TIDAK_MENGUKUR if not peta else MENGUKUR,
    }


def jalankan() -> int:
    isi = {
        "nama": "ringkas_semesta",
        "bukan_bukti": True,
        "sumber": "reports/semesta_bulan_1m.json",
        "sidik_kode": sidik_kode(),
        "waktu_utc": sekarang(),
        "catatan_metode": (
            "Dua jalur: peta simbol->daftar bulan, atau peta simbol->cacah "
            "bulan (bentuk sebenarnya berkas ini, lihat jurnal 23). Kunci yang "
            "ditolak POLA_SIMBOL padahal nilainya angka dihitung terpisah, "
            "tidak dibuang diam-diam (jurnal 24). Bila tak ada jalur yang "
            "cocok, laporan menandai bentuk_tak_dikenali, bukan menebak."
        ),
    }
    if not SUMBER.exists():
        isi["bentuk_tak_dikenali"] = True
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
        isi["bentuk_tak_dikenali"] = True
        isi["status"] = TIDAK_MENGUKUR
        isi["galat"] = "json tidak sah: " + str(galat)
        tulis(LAPORAN, isi)
        return 1
    peta_bulan = kumpulkan(akar)
    if peta_bulan:
        isi["jalur"] = "daftar_bulan"
        isi["bentuk_tak_dikenali"] = False
        isi["ringkas"] = ringkas(peta_bulan)
        isi["status"] = isi["ringkas"]["status"]
        tulis(LAPORAN, isi)
        return 0
    terkumpul = kumpulkan_cacah(akar)
    peta_cacah = terkumpul.pop("peta")
    isi["jalur"] = "cacah_bulan" if peta_cacah else "tidak ada"
    isi["bentuk_tak_dikenali"] = not peta_cacah
    isi.update(terkumpul)
    isi["ringkas_cacah"] = ringkas_cacah(peta_cacah)
    isi["jumlah_diterima_dan_ditolak"] = (
        isi["ringkas_cacah"]["cacah_simbol"] + terkumpul["cacah_kunci_ditolak_pola"]
    )
    isi["status"] = isi["ringkas_cacah"]["status"]
    tulis(LAPORAN, isi)
    return 0


if __name__ == "__main__":
    sys.exit(jalankan())
