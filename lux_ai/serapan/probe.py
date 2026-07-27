"""Pengukuran 12 simbol probe. Ukur dulu, ekstrapolasi, baru serapan penuh.

Keluaran: `reports/probe_serapan.json`. Angka di dalamnya adalah PENGUKURAN
INFRASTRUKTUR, bukan bukti tentang strategi apa pun. Serapan penuh tidak boleh
dijalankan sebelum angka-angka ini masuk ke ADR-A002 bagian 7.

Dijalankan sebagai `python -m lux_ai.serapan.probe` dari workflow.
"""
from __future__ import annotations

import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path

from . import arsip, klines

AKAR_REPO = Path(__file__).resolve().parents[2]
LAPORAN = AKAR_REPO / "reports" / "probe_serapan.json"
PROGRES = AKAR_REPO / "reports" / "probe_serapan_progres.json"

# Dipilih di muka, sebelum melihat data apa pun.
PROBE_LIKUID = [
    "BTCUSDT",
    "ETHUSDT",
    "BNBUSDT",
    "SOLUSDT",
    "XRPUSDT",
    "ADAUSDT",
    "DOGEUSDT",
    "LINKUSDT",
]

# Klaim: keempatnya sudah delisting dari USDS-M. Klaim ini DIUJI oleh run ini.
# Simbol yang tidak ada di indeks arsip dicatat sebagai klaim yang dibantah.
PROBE_DELISTING_KLAIM = ["FTTUSDT", "SRMUSDT", "COCOSUSDT", "BTSUSDT"]


def sidik_kode() -> str:
    """Hash modul serapan yang terlibat, agar laporan dapat direproduksi."""
    h = hashlib.sha256()
    for nama in sorted(["arsip.py", "klines.py", "probe.py"]):
        h.update((Path(__file__).parent / nama).read_bytes())
    return h.hexdigest()


def tulis(path: Path, isi: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(isi, indent=2, ensure_ascii=False, sort_keys=True) + "\n")


def sekarang() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def ukur_simbol(simbol: str) -> dict:
    """Ukur satu simbol probe: cakupan bulan, ukuran zip, baris, ukuran parquet."""
    hasil = {"simbol": simbol}
    bulan = arsip.bulan_tersedia(simbol, "1m")
    hasil["jumlah_bulan_1m"] = len(bulan)
    hasil["bulan_pertama"] = bulan[0] if bulan else None
    hasil["bulan_terakhir"] = bulan[-1] if bulan else None
    if not bulan:
        hasil["galat"] = "tidak ada berkas bulanan 1m di arsip"
        return hasil

    sasaran = bulan[-1]
    url = arsip.url_klines(simbol, "1m", sasaran)
    mulai = time.time()
    data = arsip.unduh_terverifikasi(url)
    hasil["bulan_diukur"] = sasaran
    hasil["byte_zip"] = len(data)
    hasil["detik_unduh"] = round(time.time() - mulai, 2)
    hasil["checksum_cocok"] = True

    df = klines.baca_zip(data)
    df, dibuang = klines.rapikan(df)
    hasil["baris"] = int(len(df))
    hasil["baris_dibuang"] = int(dibuang)

    tujuan = f"/tmp/{simbol}-1m-{sasaran}.parquet"
    hasil["byte_parquet_zstd"] = int(klines.tulis_parquet(df, tujuan))
    Path(tujuan).unlink(missing_ok=True)

    # Menit penuh dalam sebulan berkisar 40.320-44.640. Celah adalah fakta yang
    # harus tercatat, bukan disembunyikan.
    if len(df) > 1:
        beda = df["open_time"].astype("int64").diff().dropna()
        hasil["celah_bukan_60_detik"] = int((beda != 60000).sum())

    try:
        f_data = arsip.unduh_terverifikasi(arsip.url_funding(simbol, sasaran))
        hasil["funding_byte_zip"] = len(f_data)
        hasil["funding_ada"] = True
    except Exception as exc:  # noqa: BLE001
        hasil["funding_ada"] = False
        hasil["funding_galat"] = str(exc)[:200]

    return hasil


def jalankan() -> dict:
    catatan = {"mulai_utc": sekarang(), "tahap": "indeks arsip"}
    tulis(PROGRES, catatan)

    semesta = arsip.semesta_simbol()
    catatan["jumlah_simbol_semesta"] = len(semesta)
    catatan["tahap"] = "probe simbol"
    tulis(PROGRES, catatan)

    ada = set(semesta)
    delisting_terbukti = [s for s in PROBE_DELISTING_KLAIM if s in ada]
    delisting_dibantah = [s for s in PROBE_DELISTING_KLAIM if s not in ada]
    probe = [s for s in PROBE_LIKUID if s in ada] + delisting_terbukti

    pengukuran = []
    for i, simbol in enumerate(probe, 1):
        try:
            pengukuran.append(ukur_simbol(simbol))
        except Exception as exc:  # noqa: BLE001
            pengukuran.append({"simbol": simbol, "galat": str(exc)[:300]})
        catatan["probe_selesai"] = f"{i}/{len(probe)}"
        catatan["terakhir"] = simbol
        tulis(PROGRES, catatan)

    catatan["tahap"] = "cacah bulan seluruh semesta"
    tulis(PROGRES, catatan)

    bulan_per_simbol = {}
    for i, simbol in enumerate(semesta, 1):
        try:
            bulan_per_simbol[simbol] = len(arsip.bulan_tersedia(simbol, "1m"))
        except Exception:  # noqa: BLE001
            bulan_per_simbol[simbol] = -1
        if i % 25 == 0:
            catatan["semesta_selesai"] = f"{i}/{len(semesta)}"
            tulis(PROGRES, catatan)

    total_bulan = sum(v for v in bulan_per_simbol.values() if v > 0)
    gagal_listing = [s for s, v in bulan_per_simbol.items() if v < 0]
    berhasil = [p for p in pengukuran if p.get("byte_zip")]
    rerata_zip = sum(p["byte_zip"] for p in berhasil) / len(berhasil) if berhasil else 0
    rerata_parquet = (
        sum(p["byte_parquet_zstd"] for p in berhasil) / len(berhasil) if berhasil else 0
    )

    laporan = {
        "nama": "probe_serapan",
        "waktu_utc": sekarang(),
        "sidik_kode": sidik_kode(),
        "sumber_arsip": arsip.S3,
        "akar_prefix": arsip.AKAR,
        "jumlah_simbol_semesta": len(semesta),
        "total_berkas_bulanan_1m": total_bulan,
        "simbol_gagal_listing": gagal_listing,
        "probe_dipakai": probe,
        "delisting_klaim_terbukti": delisting_terbukti,
        "delisting_klaim_dibantah": delisting_dibantah,
        "pengukuran": pengukuran,
        "rerata_byte_zip_per_simbol_bulan": round(rerata_zip),
        "rerata_byte_parquet_per_simbol_bulan": round(rerata_parquet),
        "estimasi_total_zip_gb": round(total_bulan * rerata_zip / 1e9, 2),
        "estimasi_total_parquet_gb": round(total_bulan * rerata_parquet / 1e9, 2),
        "catatan_estimasi": (
            "Ekstrapolasi memakai rerata simbol probe yang condong LIKUID, jadi "
            "estimasi ini kemungkinan besar TERLALU TINGGI untuk semesta penuh "
            "yang banyak memuat simbol tipis. Perlakukan sebagai batas atas kasar."
        ),
    }
    tulis(LAPORAN, laporan)
    tulis(
        AKAR_REPO / "reports" / "semesta_bulan_1m.json",
        {"waktu_utc": sekarang(), "bulan_per_simbol": bulan_per_simbol},
    )
    catatan["tahap"] = "selesai"
    tulis(PROGRES, catatan)
    return laporan


if __name__ == "__main__":
    ringkas = jalankan()
    print(json.dumps({k: v for k, v in ringkas.items() if k != "pengukuran"}, indent=2))
