"""Gerbang integritas struktural deret 1m — penerapan ADR-A004 §2.

ADR-A004 memutuskan berkas 1m sebagai satu-satunya sumber kebenaran dan
memindahkan gerbang serapan yang MENGIKAT dari "sama dengan berkas 5m/15m
terbitan" ke integritas struktural deret 1m itu sendiri. Modul ini adalah
gerbang tersebut dalam kode.

Berbeda dengan `diagnosa_kc6` dan `rentang_kc6`, keluaran modul ini BUKAN
diagnostik: ia boleh menjatuhkan sebuah simbol-bulan. Karena itu ia sengaja
tidak mengimpor apa pun dari modul diagnostik (aturan 10), dan tidak menyentuh
jaringan sama sekali (aturan 13): masukannya hanya deret stempel waktu.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

from . import resample as rs

MS_MENIT = rs.MS_MENIT

# Batas besaran untuk menilai satuan stempel. 1e12 ms = 2001-09-09 dan
# 1e14 ms = 5138-11-16; seluruh arsip Binance futures jatuh di antaranya,
# sementara stempel detik (1e9) dan mikrodetik (1e15) jatuh di luarnya.
MS_BAWAH = 1_000_000_000_000
MS_ATAS = 100_000_000_000_000

KLAUSA = (
    "deret_tidak_kosong",
    "tanpa_duplikat",
    "tanpa_menit_hilang",
    "jarak_60_detik",
    "selaras_menit",
    "satuan_milidetik",
)


def sidik_kode() -> str:
    """Aturan 22: cakup seluruh berkas yang ikut menentukan putusan gerbang."""
    h = hashlib.sha256()
    for nama in sorted(["gerbang_1m.py", "resample.py"]):
        h.update((Path(__file__).parent / nama).read_bytes())
    return h.hexdigest()


def persen(bagian: int, total: int):
    """Persentase yang menolak berbohong saat penyebutnya nol."""
    if not total:
        return None
    return round(100.0 * bagian / total, 2)


def satuan_stempel_dari_besaran(cap) -> str:
    """Nilai satuan stempel dari BESARAN angkanya.

    Namanya menyebut `dari_besaran` karena itulah yang benar-benar diukur
    (aturan 16): berkas arsip tidak menyatakan satuan stempelnya di mana pun,
    sehingga satuan hanya bisa disimpulkan dari rentang nilainya.
    """
    nilai = [abs(int(t)) for t in cap]
    if not nilai:
        return "tak_ada_data"
    if all(MS_BAWAH <= v < MS_ATAS for v in nilai):
        return "milidetik"
    if all(v < MS_BAWAH for v in nilai):
        return "bukan_milidetik_terlalu_kecil"
    if all(v >= MS_ATAS for v in nilai):
        return "bukan_milidetik_terlalu_besar"
    return "campuran"


def ukur_deret(cap_waktu) -> dict:
    """Ukur struktur deret menit apa adanya, tanpa memutuskan apa pun.

    `menit_hilang_dalam_rentang` dihitung dari rentang yang benar-benar ada di
    berkas, bukan dari panjang bulan kalender: bulan pertama sebuah simbol
    memang mulai di tengah bulan, dan itu bukan celah.

    Rumusnya identik dengan `diagnosa_kc6.celah_menit` dan sengaja DISALIN,
    bukan diimpor: modul diagnostik tidak boleh menjadi bagian dari gerbang
    yang mengikat (aturan 10). Agar kedua salinan tidak menyimpang diam-diam,
    `tests/test_gerbang_1m.py` membandingkan seluruh medan bersamanya.

    Catatan: bila stempel tidak selaras menit, `menit_hilang_dalam_rentang`
    dapat bernilai negatif. Rumus tidak ditambal agar tetap identik; klausa
    `selaras_menit` yang menangkap kasus itu.
    """
    urut = sorted(int(t) for t in cap_waktu)
    satuan = satuan_stempel_dari_besaran(urut)
    if not urut:
        return {
            "baris": 0,
            "cap_unik": 0,
            "duplikat": 0,
            "menit_pertama": None,
            "menit_terakhir": None,
            "slot_dalam_rentang": 0,
            "menit_hilang_dalam_rentang": 0,
            "jarak_bukan_60_detik": 0,
            "cap_tidak_selaras_menit": 0,
            "satuan_stempel_dari_besaran": satuan,
        }
    unik = sorted(set(urut))
    rentang = (unik[-1] - unik[0]) // MS_MENIT + 1
    return {
        "baris": len(urut),
        "cap_unik": len(unik),
        "duplikat": len(urut) - len(unik),
        "menit_pertama": unik[0],
        "menit_terakhir": unik[-1],
        "slot_dalam_rentang": rentang,
        "menit_hilang_dalam_rentang": rentang - len(unik),
        "jarak_bukan_60_detik": sum(
            1 for a, b in zip(unik, unik[1:]) if b - a != MS_MENIT
        ),
        "cap_tidak_selaras_menit": sum(1 for t in unik if t % MS_MENIT),
        "satuan_stempel_dari_besaran": satuan,
    }


def nilai_klausa(ukuran: dict) -> dict:
    """Terjemahkan hasil ukur menjadi enam klausa ADR-A004 §2."""
    return {
        "deret_tidak_kosong": int(ukuran.get("baris") or 0) > 0,
        "tanpa_duplikat": int(ukuran.get("duplikat") or 0) == 0,
        "tanpa_menit_hilang": int(ukuran.get("menit_hilang_dalam_rentang") or 0) == 0,
        "jarak_60_detik": int(ukuran.get("jarak_bukan_60_detik") or 0) == 0,
        "selaras_menit": int(ukuran.get("cap_tidak_selaras_menit") or 0) == 0,
        "satuan_milidetik": ukuran.get("satuan_stempel_dari_besaran") == "milidetik",
    }


def nilai_deret(cap_waktu, simbol: str = "", bulan: str = "") -> dict:
    """Putusan gerbang untuk satu simbol-bulan."""
    ukuran = ukur_deret(cap_waktu)
    klausa = nilai_klausa(ukuran)
    pelanggaran = [nama for nama in KLAUSA if not klausa[nama]]
    return {
        "simbol": simbol,
        "bulan": bulan,
        "lolos": not pelanggaran,
        "klausa": klausa,
        "pelanggaran": pelanggaran,
        "ukuran": ukuran,
    }


def ringkas_gerbang(hasil) -> dict:
    """Cacah lintas simbol-bulan.

    Aturan 18: gerbang yang lolos wajib melaporkan CACAH hal yang benar-benar
    diperiksa, karena itu `baris_diperiksa` dan `slot_diperiksa` selalu ada.
    Aturan 24: `simbol_bulan_gagal` dan `pelanggaran_per_klausa` dilaporkan
    walau nilainya nol, sebab keduanyalah yang dapat menggugurkan premis
    "arsip 1m utuh" yang saat ini saya percayai.
    """
    daftar = list(hasil)
    lolos = [h for h in daftar if h.get("lolos")]
    gagal = [h for h in daftar if not h.get("lolos")]
    per_klausa = {nama: 0 for nama in KLAUSA}
    for h in gagal:
        for nama in h.get("pelanggaran") or []:
            per_klausa[nama] = per_klausa.get(nama, 0) + 1
    return {
        "simbol_bulan_dinilai": len(daftar),
        "simbol_bulan_lolos": len(lolos),
        "simbol_bulan_gagal": len(gagal),
        "persen_lolos": persen(len(lolos), len(daftar)),
        "pelanggaran_per_klausa": per_klausa,
        "baris_diperiksa": sum(
            int((h.get("ukuran") or {}).get("baris") or 0) for h in daftar
        ),
        "slot_diperiksa": sum(
            int((h.get("ukuran") or {}).get("slot_dalam_rentang") or 0) for h in daftar
        ),
        "contoh_gagal": [
            {
                "simbol": h.get("simbol"),
                "bulan": h.get("bulan"),
                "pelanggaran": h.get("pelanggaran"),
            }
            for h in gagal[:10]
        ],
    }
