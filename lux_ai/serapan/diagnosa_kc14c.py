"""Diagnosa KC-14c — sembilan lubang baru: masih sepakat dengan berkas harian?

Pecahan 1..7 menambah **9** simbol-bulan yang dijatuhkan gerbang, sehingga
seluruh populasi gagal di 19.598 simbol-bulan menjadi **12**. Diagnosa KC-14b
sudah menggugurkan H-A003 pada tiga tersangka pertama, tetapi aturan 20 melarang
saya memindahkan kesimpulan dari 3 kasus ke 12.

Bedanya dengan KC-14b: di sana letak lubang saya SALIN dari laporan sebelumnya.
Di sini letak lubang tidak diketahui, jadi modul ini menemukannya sendiri dari
berkas BULANAN (memakai `diagnosa_kc14.menit_hilang` dan `.blok`, bukan salinan
logika baru), lalu mengelompokkannya per TANGGAL UTC dan mengunduh berkas
HARIAN untuk tiap tanggal terdampak.

Dua hal yang diukur sekaligus:

1. **Kesepakatan harian vs bulanan.** `menit_hadir_di_harian_saat_bulanan_hilang`
   > 0 berarti berkas harian memuat menit yang absen dari berkas bulanan: arsip
   bulanan cacat, **KC-15** dinamai, dan seluruh serapan berbasis berkas bulanan
   wajib ditinjau (aturan 24). Medan ini dilaporkan walau nol.
2. **Bentuk pola.** `blok_mulai_00_utc` dan `total_kelipatan_15` menguji apakah
   keselarasan tengah malam UTC dan kelipatan 15 menit — satu-satunya petunjuk
   yang belum terjelaskan pada KC-14 — bertahan di luar tiga kasus pertama.

Catatan kejujuran yang harus tetap terbaca di kode: hasil apa pun di sini TIDAK
bisa memisahkan jeda pasar dari cacat di HULU arsip (H-A004), karena harian dan
bulanan bisa dirakit dari sumber yang sama. `fapi` memberi 451 dari runner, jadi
pemisah non-arsip tidak tersedia. Sebab lubang tetap "tidak diketahui"; ADR-A006
mengarantina tanpa menunggu sebab.

Aturan yang ditegakkan: 20, 21, 24, 25, 26, 30, 32, 37.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

from . import arsip, klines
from . import diagnosa_kc14 as k14
from .diagnosa_kc14b import url_harian

KELUARAN = "reports/diagnosa_kc14c.json"
MS_MENIT = 60_000
MS_HARI = 86_400_000
MENIT_SEHARI = 1440
BATAS_CONTOH = 20
# Batas unduhan harian per simbol-bulan. Bila terlampaui, tanggal sisanya
# DILEWATI dan dilaporkan di `hari_dilewati`, tidak dianggap kosong.
BATAS_HARI = 12

# Kesembilan simbol-bulan yang GAGAL gerbang di pecahan 1..7. Disalin dari
# `contoh_gagal` di reports/pecahan_<i>.log, dan pada tiap pecahan panjang
# `contoh_gagal` sama dengan `simbol_bulan_gagal`, jadi daftar ini lengkap.
TERSANGKA: Tuple[Tuple[str, str, int], ...] = (
    ("CVXUSDT", "2025-07", 1),
    ("MAVIAUSDT", "2025-03", 1),
    ("PUMPUSDT", "2025-07", 1),
    ("CTKUSDT", "2025-04", 3),
    ("LITUSDT", "2025-12", 4),
    ("BNXUSDT", "2022-04", 6),
    ("BNXUSDT", "2022-06", 6),
    ("BNXUSDT", "2022-08", 6),
    ("AIAUSDT", "2026-01", 7),
)

# slot_diperiksa - baris_diperiksa per pecahan, dari reports/pecahan_<i>.log.
# Dipakai sebagai uji silang aritmetika, bukan sebagai sumber kebenaran.
MENIT_HILANG_GERBANG: Dict[int, int] = {1: 2160, 3: 615, 4: 1050, 6: 7200, 7: 675}


def sidik_kode() -> str:
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(
        [
            "diagnosa_kc14c.py",
            "diagnosa_kc14b.py",
            "diagnosa_kc14.py",
            "arsip.py",
            "klines.py",
        ]
    ):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def tanggal_dari_ms(ms: int) -> str:
    """TANGGAL UTC dari stempel milidetik, tanpa aritmetika pecahan."""
    dasar = dt.datetime(1970, 1, 1, tzinfo=dt.timezone.utc)
    return (dasar + dt.timedelta(milliseconds=int(ms))).strftime("%Y-%m-%d")


def kelompok_per_tanggal(menit: Sequence[int]) -> Dict[str, List[int]]:
    hasil: Dict[str, List[int]] = {}
    for t in sorted(int(x) for x in menit):
        hasil.setdefault(tanggal_dari_ms(t), []).append(t)
    return hasil


def cacah_blok_mulai_batas_hari(daftar_blok: Sequence[Dict[str, int]]) -> int:
    return sum(1 for b in daftar_blok if int(b["mulai_ms"]) % MS_HARI == 0)


def kelipatan_15(panjang: int) -> bool:
    return int(panjang) % 15 == 0


def putusan_dari(hadir: int, terukur: int) -> str:
    if terukur == 0:
        return "TIDAK MENGUKUR"
    return "MENDUKUNG_H-A003" if hadir > 0 else "H-A003_GUGUR"


def periksa_hari(simbol: str, tanggal: str, menit_dicari: Sequence[int]) -> Dict[str, Any]:
    catatan: Dict[str, Any] = {
        "tanggal": tanggal,
        "menit_hilang_di_bulanan": len(menit_dicari),
    }
    url = url_harian(simbol, "1m", tanggal)
    catatan["url"] = url
    try:
        data = arsip.unduh_terverifikasi(url)
    except Exception as exc:  # noqa: BLE001
        catatan["tersedia"] = False
        catatan["sebab"] = str(exc)[:200]
        return catatan

    catatan["tersedia"] = True
    catatan["checksum"] = arsip.sha256_bytes(data)
    df = klines.baca_zip(data)
    df, dibuang = klines.rapikan(df)
    stempel = set(int(x) for x in df["open_time"].tolist())
    hadir = sorted(int(t) for t in menit_dicari if int(t) in stempel)
    catatan["cacah_baris_harian"] = len(stempel)
    catatan["baris_dibuang"] = int(dibuang)
    catatan["stempel_pertama_ms"] = min(stempel) if stempel else None
    catatan["stempel_terakhir_ms"] = max(stempel) if stempel else None
    catatan["menit_hadir_di_harian_saat_bulanan_hilang"] = len(hadir)
    catatan["contoh_menit_hadir"] = hadir[:BATAS_CONTOH]
    return catatan


def periksa_satu(simbol: str, bulan: str, pecahan: int) -> Dict[str, Any]:
    catatan: Dict[str, Any] = {"simbol": simbol, "bulan": bulan, "pecahan": pecahan}
    url = arsip.url_klines(simbol, "1m", bulan)
    catatan["url_bulanan"] = url
    try:
        data = arsip.unduh_terverifikasi(url)
    except Exception as exc:  # noqa: BLE001
        catatan["bulanan_tersedia"] = False
        catatan["sebab"] = str(exc)[:200]
        catatan["putusan"] = "TIDAK MENGUKUR"
        return catatan

    catatan["bulanan_tersedia"] = True
    catatan["checksum_bulanan"] = arsip.sha256_bytes(data)
    stempel = k14.stempel_dari_zip(data)
    hilang = k14.menit_hilang(stempel)
    daftar_blok = k14.blok(hilang)

    catatan["cacah_baris_1m"] = len(stempel)
    catatan["cacah_menit_hilang"] = len(hilang)
    catatan["cacah_blok"] = len(daftar_blok)
    catatan["blok_terpanjang_menit"] = max(
        (int(b["panjang_menit"]) for b in daftar_blok), default=0
    )
    catatan["blok_tunggal_menit"] = sum(
        1 for b in daftar_blok if int(b["panjang_menit"]) == 1
    )
    catatan["blok_mulai_00_utc"] = cacah_blok_mulai_batas_hari(daftar_blok)
    catatan["semua_blok_mulai_00_utc"] = bool(daftar_blok) and catatan[
        "blok_mulai_00_utc"
    ] == len(daftar_blok)
    catatan["total_kelipatan_15"] = kelipatan_15(len(hilang))
    catatan["contoh_blok"] = daftar_blok[:BATAS_CONTOH]

    per_tanggal = kelompok_per_tanggal(hilang)
    tanggal_urut = sorted(per_tanggal)
    dipakai = tanggal_urut[:BATAS_HARI]
    catatan["cacah_tanggal_terdampak"] = len(tanggal_urut)
    catatan["hari_dilewati"] = len(tanggal_urut) - len(dipakai)
    catatan["tanggal_terdampak"] = tanggal_urut

    rincian_hari = [periksa_hari(simbol, t, per_tanggal[t]) for t in dipakai]
    catatan["harian"] = rincian_hari
    terukur = [h for h in rincian_hari if h.get("tersedia")]
    hadir = sum(
        int(h.get("menit_hadir_di_harian_saat_bulanan_hilang", 0)) for h in terukur
    )
    catatan["hari_diperiksa"] = len(terukur)
    catatan["hari_tidak_tersedia"] = sum(
        1 for h in rincian_hari if h.get("tersedia") is False
    )
    catatan["menit_hadir_di_harian_saat_bulanan_hilang"] = hadir
    catatan["putusan"] = putusan_dari(hadir, len(terukur))
    return catatan


def ringkas(catatan: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    diperiksa = [c for c in catatan if c.get("bulanan_tersedia")]
    putusan = [c.get("putusan") for c in catatan]
    per_pecahan: Dict[str, int] = {}
    for c in diperiksa:
        kunci = str(c.get("pecahan"))
        per_pecahan[kunci] = per_pecahan.get(kunci, 0) + int(
            c.get("cacah_menit_hilang", 0)
        )
    banding_gerbang = {
        kunci: {
            "gerbang": MENIT_HILANG_GERBANG.get(int(kunci)),
            "dihitung_ulang": nilai,
            "cocok": MENIT_HILANG_GERBANG.get(int(kunci)) == nilai,
        }
        for kunci, nilai in sorted(per_pecahan.items())
    }
    return {
        "simbol_bulan_diminta": len(catatan),
        "simbol_bulan_diperiksa": len(diperiksa),
        "total_menit_hilang": sum(int(c.get("cacah_menit_hilang", 0)) for c in diperiksa),
        "menit_hilang_per_pecahan": per_pecahan,
        "banding_menit_hilang_gerbang": banding_gerbang,
        "cacah_pecahan_tak_cocok": sum(
            1 for v in banding_gerbang.values() if not v["cocok"]
        ),
        "menit_hadir_di_harian_saat_bulanan_hilang": sum(
            int(c.get("menit_hadir_di_harian_saat_bulanan_hilang", 0)) for c in diperiksa
        ),
        "hari_diperiksa": sum(int(c.get("hari_diperiksa", 0)) for c in diperiksa),
        "cacah_hari_tidak_tersedia": sum(
            int(c.get("hari_tidak_tersedia", 0)) for c in diperiksa
        ),
        "cacah_hari_dilewati": sum(int(c.get("hari_dilewati", 0)) for c in diperiksa),
        "cacah_semua_blok_mulai_00_utc": sum(
            1 for c in diperiksa if c.get("semua_blok_mulai_00_utc")
        ),
        "cacah_total_kelipatan_15": sum(
            1 for c in diperiksa if c.get("total_kelipatan_15")
        ),
        "cacah_mendukung_h_a003": putusan.count("MENDUKUNG_H-A003"),
        "cacah_h_a003_gugur": putusan.count("H-A003_GUGUR"),
        "cacah_tidak_mengukur": putusan.count("TIDAK MENGUKUR"),
        "status": "TERUKUR" if diperiksa else "TIDAK MENGUKUR",
        "catatan_penggugur": (
            "menit_hadir_di_harian_saat_bulanan_hilang > 0 berarti berkas HARIAN memuat "
            "menit yang absen dari berkas BULANAN: arsip bulanan cacat, KC-15 dinamai, "
            "dan seluruh serapan berbasis berkas bulanan wajib ditinjau (aturan 24)"
        ),
        "catatan_rentang": (
            "9 simbol-bulan yang GAGAL gerbang di pecahan 1..7; bersama 3 dari pecahan 0 "
            "itulah SELURUH populasi gagal dari 19.598 simbol-bulan. Bukan sampel dari "
            "19.586 yang LOLOS, jadi tidak berlaku bagi mereka (aturan 20)"
        ),
        "catatan_kelas_risiko": (
            "kelas non_ascii KOSONG di antara kedua belas tersangka; kelas pra_header, "
            "terhenti, bulan_awal_2020_2021, kendali_baru belum dipetakan per tersangka "
            "dan tidak boleh dianggap nol (aturan 37)"
        ),
        "catatan_batas_uji": (
            "uji ini TIDAK bisa memisahkan jeda pasar dari cacat di HULU arsip (H-A004), "
            "karena harian dan bulanan mungkin dirakit dari sumber yang sama; fapi 451 "
            "dari runner sehingga pemisah non-arsip tidak tersedia"
        ),
    }


def jalankan(akar: str = ".") -> Dict[str, Any]:
    catatan = [periksa_satu(s, b, p) for s, b, p in TERSANGKA]
    laporan = ringkas(catatan)
    laporan["bukan_bukti"] = False
    laporan["tersangka"] = [f"{s} {b} (pecahan {p})" for s, b, p in TERSANGKA]
    laporan["rincian"] = catatan
    laporan["sidik_kode"] = sidik_kode()
    laporan["waktu_utc"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    tujuan = Path(akar) / KELUARAN
    tujuan.parent.mkdir(parents=True, exist_ok=True)
    tujuan.write_text(
        json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return laporan


def main() -> None:
    print(json.dumps(jalankan(), ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
