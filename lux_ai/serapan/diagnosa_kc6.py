"""Diagnostik KC-6: mencari SEBAB beda OHLC di bulan awal, bukan memutuskan.

Gerbang `uji_resample` menemukan 609 sel OHLC berbeda, seluruhnya di bulan awal
tiap simbol, didominasi `open`. Dua hipotesis bersaing:

- H1 celah menit: berkas 1m kehilangan sebagian menit, sehingga `open` turunan
  diambil dari menit yang salah.
- H2 sumber berbeda: berkas 1m dan 5m/15m dibangun dari agregasi yang berbeda,
  sehingga beda tetap muncul walau tidak ada menit yang hilang.

Modul ini mengukur mana yang benar dengan memeriksa, untuk setiap bucket yang
OHLC-nya berbeda, apakah menit PERTAMA bucket itu ada di berkas 1m dan apakah
bucket itu terisi penuh. Bucket yang PENUH dan menit pertamanya ADA namun tetap
berbeda tidak dapat dijelaskan H1; itulah yang dicacah sebagai
`beda_tak_terjelaskan_h1`.

Aturan 10: seluruh keluaran modul ini bertanda `"bukan_bukti": true`, tidak
menyentuh gerbang mana pun, dan proses selalu keluar dengan kode 0. Diagnostik
yang bisa menjatuhkan pipeline akan berubah diam-diam menjadi gerbang.

Dijalankan sebagai `python -m lux_ai.serapan.diagnosa_kc6`.
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from . import arsip, klines, resample as rs

AKAR_REPO = Path(__file__).resolve().parents[2]
LAPORAN = AKAR_REPO / "reports" / "diagnosa_kc6.json"
PROGRES = AKAR_REPO / "reports" / "diagnosa_kc6_progres.json"

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


def sidik_kode() -> str:
    """Aturan 22: cakup seluruh berkas yang ikut menentukan isi laporan."""
    h = hashlib.sha256()
    for nama in sorted(["arsip.py", "klines.py", "resample.py", "diagnosa_kc6.py"]):
        h.update((Path(__file__).parent / nama).read_bytes())
    return h.hexdigest()


def tulis(path: Path, isi: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(isi, indent=2, ensure_ascii=False, sort_keys=True) + "\n")


def sekarang() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def persen(bagian: int, total: int):
    """Persentase yang menolak berbohong saat penyebutnya nol."""
    if not total:
        return None
    return round(100.0 * bagian / total, 2)


def celah_menit(cap_waktu) -> dict:
    """Ukur kelengkapan deret menit 1m apa adanya.

    `menit_hilang_dalam_rentang` sengaja dihitung dari rentang yang benar-benar
    ada di berkas, bukan dari panjang bulan kalender: bulan pertama sebuah
    simbol memang mulai di tengah bulan, dan itu bukan celah.
    """
    urut = sorted(int(t) for t in cap_waktu)
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
        }
    unik = sorted(set(urut))
    rentang = (unik[-1] - unik[0]) // rs.MS_MENIT + 1
    return {
        "baris": len(urut),
        "cap_unik": len(unik),
        "duplikat": len(urut) - len(unik),
        "menit_pertama": unik[0],
        "menit_terakhir": unik[-1],
        "slot_dalam_rentang": rentang,
        "menit_hilang_dalam_rentang": rentang - len(unik),
        "jarak_bukan_60_detik": sum(
            1 for a, b in zip(unik, unik[1:]) if b - a != rs.MS_MENIT
        ),
        "cap_tidak_selaras_menit": sum(1 for t in unik if t % rs.MS_MENIT),
    }


def periksa_bucket(hasil, asli, cap_ada, menit: int) -> dict:
    """Pilah bucket yang OHLC-nya beda menurut apa yang bisa menjelaskannya.

    Bucket dihitung `beda_tak_terjelaskan_h1` bila ia terisi penuh `menit` menit
    DAN menit pertamanya hadir, namun OHLC-nya tetap berbeda. Bucket seperti itu
    adalah bukti melawan H1, dan itulah yang paling ingin saya temukan.
    """
    ada = {int(t) for t in cap_ada}
    kiri = {b["open_time"]: b for b in hasil}
    kanan = {}
    for rekam in asli:
        bar = rs.ke_baris(rekam)
        kanan[bar["open_time"]] = bar

    keluar = {
        "bucket_dibandingkan": 0,
        "bucket_ohlc_beda": 0,
        "bucket_open_beda": 0,
        "open_beda_menit_pertama_hilang": 0,
        "open_beda_menit_pertama_ada": 0,
        "open_beda_bucket_menit_penuh": 0,
        "beda_tak_terjelaskan_h1": 0,
        "contoh_tak_terjelaskan": [],
    }

    for waktu in sorted(set(kiri) & set(kanan)):
        keluar["bucket_dibandingkan"] += 1
        turunan = kiri[waktu]
        asal = kanan[waktu]
        beda = [k for k in rs.KOLOM_HARGA if turunan[k] != asal[k]]
        if not beda:
            continue
        keluar["bucket_ohlc_beda"] += 1
        penuh = int(turunan.get("menit_terisi") or 0) == menit
        pertama_ada = waktu in ada
        if "open" in beda:
            keluar["bucket_open_beda"] += 1
            if pertama_ada:
                keluar["open_beda_menit_pertama_ada"] += 1
            else:
                keluar["open_beda_menit_pertama_hilang"] += 1
            if penuh:
                keluar["open_beda_bucket_menit_penuh"] += 1
        if penuh and pertama_ada:
            keluar["beda_tak_terjelaskan_h1"] += 1
            if len(keluar["contoh_tak_terjelaskan"]) < 5:
                keluar["contoh_tak_terjelaskan"].append(
                    {
                        "open_time": waktu,
                        "kolom_beda": beda,
                        "menit_terisi": int(turunan.get("menit_terisi") or 0),
                        "resample_open": str(turunan["open"]),
                        "asli_open": str(asal["open"]),
                    }
                )
    return keluar


def ringkas(pengukuran) -> dict:
    """Cacah lintas bulan, plus persentase per simbol untuk R-26."""
    total = {
        "bucket_open_beda": 0,
        "open_beda_menit_pertama_hilang": 0,
        "bucket_ohlc_beda": 0,
        "beda_tak_terjelaskan_h1": 0,
    }
    per_simbol = {}
    bulan_tanpa_celah = []
    bulan_diukur = 0

    for satuan in pengukuran:
        if satuan.get("galat"):
            continue
        bulan_diukur += 1
        celah = satuan.get("celah") or {}
        if not celah.get("menit_hilang_dalam_rentang") and not celah.get("duplikat"):
            bulan_tanpa_celah.append(
                {"simbol": satuan.get("simbol"), "bulan": satuan.get("bulan")}
            )
        beda_simbol = 0
        hilang_simbol = 0
        for nama in ("5m", "15m"):
            bagian = satuan.get(nama) or {}
            for kunci in total:
                total[kunci] += int(bagian.get(kunci) or 0)
            beda_simbol += int(bagian.get("bucket_open_beda") or 0)
            hilang_simbol += int(bagian.get("open_beda_menit_pertama_hilang") or 0)
        per_simbol[satuan.get("simbol")] = {
            "bucket_open_beda": beda_simbol,
            "open_beda_menit_pertama_hilang": hilang_simbol,
            "persen_terjelaskan_h1": persen(hilang_simbol, beda_simbol),
        }

    return {
        "bulan_diukur": bulan_diukur,
        "bucket_ohlc_beda_total": total["bucket_ohlc_beda"],
        "bucket_open_beda_total": total["bucket_open_beda"],
        "open_beda_menit_pertama_hilang_total": total["open_beda_menit_pertama_hilang"],
        "persen_terjelaskan_h1": persen(
            total["open_beda_menit_pertama_hilang"], total["bucket_open_beda"]
        ),
        "beda_tak_terjelaskan_h1_total": total["beda_tak_terjelaskan_h1"],
        "bulan_tanpa_celah": bulan_tanpa_celah,
        "per_simbol": per_simbol,
    }


def muat(simbol: str, interval: str, bulan: str):
    data = arsip.unduh_terverifikasi(arsip.url_klines(simbol, interval, bulan))
    df, dibuang = klines.rapikan(klines.baca_zip(data, teks=True))
    return df, int(dibuang)


def ukur_simbol(simbol: str) -> dict:
    hasil = {"simbol": simbol}
    bulan_1m = arsip.bulan_tersedia(simbol, "1m")
    bersama = sorted(
        set(bulan_1m)
        & set(arsip.bulan_tersedia(simbol, "5m"))
        & set(arsip.bulan_tersedia(simbol, "15m"))
    )
    if not bersama:
        hasil["galat"] = "tidak ada bulan yang punya 1m, 5m, dan 15m sekaligus"
        return hasil

    bulan = bersama[0]
    hasil["bulan"] = bulan
    df1, dibuang = muat(simbol, "1m", bulan)
    rekaman = df1.to_dict("records")
    cap = [int(r["open_time"]) for r in rekaman]
    hasil["baris_1m_dibuang"] = dibuang
    hasil["celah"] = celah_menit(cap)

    for menit, nama in ((5, "5m"), (15, "15m")):
        try:
            dfn, _ = muat(simbol, nama, bulan)
            hasil[nama] = periksa_bucket(
                rs.resample(rekaman, menit), dfn.to_dict("records"), cap, menit
            )
        except Exception as exc:  # noqa: BLE001
            hasil[nama] = {"galat": str(exc)[:300]}
    return hasil


def jalankan() -> dict:
    catatan = {"mulai_utc": sekarang(), "tahap": "mulai"}
    tulis(PROGRES, catatan)

    pengukuran = []
    for i, simbol in enumerate(PROBE, 1):
        try:
            pengukuran.append(ukur_simbol(simbol))
        except Exception as exc:  # noqa: BLE001
            pengukuran.append({"simbol": simbol, "galat": str(exc)[:300]})
        catatan["selesai"] = f"{i}/{len(PROBE)}"
        catatan["terakhir"] = simbol
        tulis(PROGRES, catatan)

    laporan = {
        "nama": "diagnosa_kc6",
        "bukan_bukti": True,
        "waktu_utc": sekarang(),
        "sidik_kode": sidik_kode(),
        "sumber_arsip": arsip.S3,
        "simbol_diukur": PROBE,
        "pengukuran": pengukuran,
        "ringkas": ringkas(pengukuran),
    }
    tulis(LAPORAN, laporan)
    catatan["tahap"] = "selesai"
    tulis(PROGRES, catatan)
    return laporan


if __name__ == "__main__":
    ringkasan = jalankan()
    print(
        json.dumps(
            {k: v for k, v in ringkasan.items() if k != "pengukuran"},
            indent=2,
            ensure_ascii=False,
        )
    )
    sys.exit(0)
