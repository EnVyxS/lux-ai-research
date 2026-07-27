"""Uji integritas resample atas 12 simbol probe, dijalankan di runner.

Membandingkan bar 5m dan 15m yang DITURUNKAN dari 1m dengan berkas 5m dan 15m
ASLI dari arsip. Berkas asli itu dipakai HANYA di sini; ADR-A002 bagian 3
melarang memakainya untuk backtest mana pun.

Sekalian mengukur ada tidaknya baris header pada bulan pertama dan bulan
terakhir tiap simbol, karena ramalan R-5 belum bisa diadjudikasi tanpa itu.

Gerbang: ketidakcocokan open/high/low/close, atau bar yang hanya ada di satu
sisi, MENGHENTIKAN pipeline (keluar dengan kode 1). Beda volume tidak
menjatuhkan gerbang tetapi tetap dicatat.

Dijalankan sebagai `python -m lux_ai.serapan.uji_resample`.
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from . import arsip, klines, resample as rs

AKAR_REPO = Path(__file__).resolve().parents[2]
LAPORAN = AKAR_REPO / "reports" / "uji_resample.json"
PROGRES = AKAR_REPO / "reports" / "uji_resample_progres.json"

PROBE = [
    "BTCUSDT",
    "ETHUSDT",
    "BNBUSDT",
    "SOLUSDT",
    "XRPUSDT",
    "ADAUSDT",
    "DOGEUSDT",
    "LINKUSDT",
    "FTTUSDT",
    "SRMUSDT",
    "COCOSUSDT",
    "BTSUSDT",
]

OHLC = ["open", "high", "low", "close"]


def sidik_kode() -> str:
    h = hashlib.sha256()
    for nama in sorted(["arsip.py", "klines.py", "resample.py", "uji_resample.py"]):
        h.update((Path(__file__).parent / nama).read_bytes())
    return h.hexdigest()


def tulis(path: Path, isi: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(isi, indent=2, ensure_ascii=False, sort_keys=True) + "\n")


def sekarang() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def muat(simbol: str, interval: str, bulan: str):
    """Unduh terverifikasi lalu baca sebagai teks apa adanya."""
    data = arsip.unduh_terverifikasi(arsip.url_klines(simbol, interval, bulan))
    df, dibuang = klines.rapikan(klines.baca_zip(data, teks=True))
    return data, df, int(dibuang)


def uji_simbol(simbol: str) -> dict:
    hasil = {"simbol": simbol}
    bulan_1m = arsip.bulan_tersedia(simbol, "1m")
    hasil["bulan_1m_pertama"] = bulan_1m[0] if bulan_1m else None
    hasil["bulan_1m_terakhir"] = bulan_1m[-1] if bulan_1m else None
    if not bulan_1m:
        hasil["galat"] = "tidak ada berkas bulanan 1m"
        return hasil

    bersama = sorted(
        set(bulan_1m)
        & set(arsip.bulan_tersedia(simbol, "5m"))
        & set(arsip.bulan_tersedia(simbol, "15m"))
    )
    hasil["jumlah_bulan_bersama"] = len(bersama)
    if not bersama:
        hasil["galat"] = "tidak ada bulan yang punya 1m, 5m, dan 15m sekaligus"
        return hasil

    bulan = bersama[-1]
    hasil["bulan_diuji"] = bulan

    data1, df1, dibuang = muat(simbol, "1m", bulan)
    hasil["baris_1m"] = int(len(df1))
    hasil["baris_1m_dibuang"] = dibuang
    hasil["berheader_bulan_diuji"] = klines.punya_header(klines.baris_pertama(data1))

    if bulan_1m[0] != bulan:
        awal = arsip.unduh_terverifikasi(arsip.url_klines(simbol, "1m", bulan_1m[0]))
        hasil["berheader_bulan_pertama"] = klines.punya_header(klines.baris_pertama(awal))

    rekaman = df1.to_dict("records")
    for menit, nama in ((5, "5m"), (15, "15m")):
        try:
            _, dfn, dibuang_n = muat(simbol, nama, bulan)
            banding = rs.bandingkan(rs.resample(rekaman, menit), dfn.to_dict("records"))
            banding["baris_asli"] = int(len(dfn))
            banding["baris_asli_dibuang"] = dibuang_n
            hasil[nama] = banding
        except Exception as exc:  # noqa: BLE001
            hasil[nama] = {"galat": str(exc)[:300]}
    return hasil


def lolos_gerbang(pengukuran) -> bool:
    """Gerbang keras: OHLC wajib cocok persis dan himpunan bar wajib sama."""
    for simbol in pengukuran:
        if "galat" in simbol:
            return False
        for nama in ("5m", "15m"):
            banding = simbol.get(nama)
            if not banding or "galat" in banding:
                return False
            if banding["jumlah_hanya_di_resample"] or banding["jumlah_hanya_di_asli"]:
                return False
            if any(banding["beda_per_kolom"].get(k, 0) for k in OHLC):
                return False
    return True


def jalankan() -> dict:
    catatan = {"mulai_utc": sekarang(), "tahap": "mulai"}
    tulis(PROGRES, catatan)

    pengukuran = []
    for i, simbol in enumerate(PROBE, 1):
        try:
            pengukuran.append(uji_simbol(simbol))
        except Exception as exc:  # noqa: BLE001
            pengukuran.append({"simbol": simbol, "galat": str(exc)[:300]})
        catatan["selesai"] = f"{i}/{len(PROBE)}"
        catatan["terakhir"] = simbol
        tulis(PROGRES, catatan)

    beda_volume = 0
    for simbol in pengukuran:
        for nama in ("5m", "15m"):
            banding = simbol.get(nama) or {}
            for kolom, cacah in (banding.get("beda_per_kolom") or {}).items():
                if kolom not in OHLC:
                    beda_volume += cacah

    laporan = {
        "nama": "uji_resample",
        "waktu_utc": sekarang(),
        "sidik_kode": sidik_kode(),
        "sumber_arsip": arsip.S3,
        "simbol_diuji": PROBE,
        "pengukuran": pengukuran,
        "total_beda_kolom_jumlah": beda_volume,
        "lolos": lolos_gerbang(pengukuran),
    }
    tulis(LAPORAN, laporan)
    catatan["tahap"] = "selesai"
    tulis(PROGRES, catatan)
    return laporan


if __name__ == "__main__":
    ringkas = jalankan()
    print(
        json.dumps(
            {k: v for k, v in ringkas.items() if k != "pengukuran"},
            indent=2,
            ensure_ascii=False,
        )
    )
    sys.exit(0 if ringkas["lolos"] else 1)
