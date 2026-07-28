"""Diagnostik KC-6 lanjutan: SEJAUH MANA ketidaksepakatan itu bertahan.

`diagnosa_kc6.py` hanya menyampel bulan PERTAMA tiap simbol. Aturan 20 melarang
menyimpulkan di luar rentang yang disampel, jadi kalimat "gejala terbatas pada
awal hidup simbol" masih klaim, bukan ukuran. Modul ini memperluas sampel ke
K bulan pertama tiap simbol ditambah satu bulan KENDALI di tengah hidup simbol.

K dan cara memilih bulan kendali dipatok di muka (jurnal 2026-07-28-15) dan
tidak boleh disetel ulang setelah melihat hasil; menyetelnya kemudian adalah
KC-1 dalam bentuk lain.

Aturan 24: laporan SELALU memuat `menit_hilang_total`, `duplikat_total`,
`total_bucket_beda_kendali`, dan `simbol_kendali_beda`, walau nilainya nol.
Dua yang pertama dapat menghidupkan kembali H1 yang saya anggap mati; dua yang
terakhir dapat menggugurkan keyakinan bahwa gejala terbatas pada bulan awal.

Aturan 10: keluaran bertanda `"bukan_bukti": true`, tidak menyentuh gerbang,
dan proses selalu keluar dengan kode 0.

Dijalankan sebagai `python -m lux_ai.serapan.rentang_kc6`.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from . import arsip, resample as rs
from .diagnosa_kc6 import (
    PROBE,
    celah_menit,
    muat,
    periksa_bucket,
    persen,
    sekarang,
    tulis,
)

AKAR_REPO = Path(__file__).resolve().parents[2]
LAPORAN = AKAR_REPO / "reports" / "rentang_kc6.json"
PROGRES = AKAR_REPO / "reports" / "rentang_kc6_progres.json"

#: Cacah bulan awal yang disampel. DIPATOK DI MUKA.
K_AWAL = 6
#: Bulan kendali hanya dipilih bila simbol punya minimal sebanyak ini bulan.
MIN_BULAN_KENDALI = K_AWAL + 3


def sidik_kode() -> str:
    """Aturan 22: seluruh berkas yang ikut menentukan isi laporan."""
    h = hashlib.sha256()
    berkas = sorted(
        ["arsip.py", "klines.py", "resample.py", "diagnosa_kc6.py", "rentang_kc6.py"]
    )
    for nama in berkas:
        h.update((Path(__file__).parent / nama).read_bytes())
    return h.hexdigest()


def pilih_bulan(bersama, k: int = K_AWAL) -> dict:
    """Pilih K bulan pertama dan satu bulan kendali di tengah hidup simbol.

    Bulan kendali sengaja dijepit agar tidak jatuh di dalam K bulan pertama dan
    tidak di bulan terakhir: keduanya rentan pada gejala tepi yang justru sedang
    diukur, dan bulan kendali harus bebas darinya untuk berguna.
    """
    bersama = list(bersama)
    awal = bersama[:k]
    kendali = None
    if len(bersama) >= MIN_BULAN_KENDALI:
        indeks = len(bersama) // 2
        if indeks < k:
            indeks = k
        if indeks > len(bersama) - 2:
            indeks = len(bersama) - 2
        if k <= indeks <= len(bersama) - 2:
            kendali = bersama[indeks]
    return {"bulan_bersama": len(bersama), "awal": awal, "kendali": kendali}


def beda_satuan(satuan) -> tuple:
    """Jumlahkan cacah beda 5m dan 15m untuk satu simbol-bulan."""
    beda = 0
    tak_terjelaskan = 0
    for nama in ("5m", "15m"):
        bagian = satuan.get(nama) or {}
        beda += int(bagian.get("bucket_open_beda") or 0)
        tak_terjelaskan += int(bagian.get("beda_tak_terjelaskan_h1") or 0)
    return beda, tak_terjelaskan


def ukur_bulan(simbol: str, bulan: str, peran: str, indeks: int) -> dict:
    """Ukur satu simbol-bulan: kelengkapan 1m dan pemilahan bucket 5m/15m."""
    hasil = {
        "simbol": simbol,
        "bulan": bulan,
        "peran": peran,
        "indeks_bulan": indeks,
    }
    df1, dibuang = muat(simbol, "1m", bulan)
    rekaman = df1.to_dict("records")
    cap = [int(r["open_time"]) for r in rekaman]
    hasil["baris_1m_dibuang"] = int(dibuang)
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


def ringkas_rentang(pengukuran) -> dict:
    """Cacah lintas bulan, dengan medan penggugur dilaporkan walau nol."""
    per_simbol: dict = {}
    total_awal = 0
    total_kendali = 0
    menit_hilang_total = 0
    duplikat_total = 0
    bulan_diukur = 0
    galat = []

    for satuan in pengukuran:
        if satuan.get("galat"):
            galat.append(
                {
                    "simbol": satuan.get("simbol"),
                    "bulan": satuan.get("bulan"),
                    "galat": satuan.get("galat"),
                }
            )
            continue
        bulan_diukur += 1
        celah = satuan.get("celah") or {}
        menit_hilang_total += int(celah.get("menit_hilang_dalam_rentang") or 0)
        duplikat_total += int(celah.get("duplikat") or 0)

        beda, tak_terjelaskan = beda_satuan(satuan)
        peran = satuan.get("peran") or "awal"
        catatan = per_simbol.setdefault(
            satuan.get("simbol"), {"awal": [], "kendali": []}
        )
        catatan.setdefault(peran, []).append(
            {
                "bulan": satuan.get("bulan"),
                "indeks_bulan": satuan.get("indeks_bulan"),
                "bucket_open_beda": beda,
                "beda_tak_terjelaskan_h1": tak_terjelaskan,
            }
        )
        if peran == "kendali":
            total_kendali += beda
        else:
            total_awal += beda

    simbol_kendali_beda = sorted(
        s for s, c in per_simbol.items() if any(x["bucket_open_beda"] for x in c["kendali"])
    )
    simbol_masih_beda_di_bulan_terakhir_awal = []
    simbol_reda_di_dalam_k = []
    simbol_menurun = []
    for simbol in sorted(per_simbol):
        baris = sorted(per_simbol[simbol]["awal"], key=lambda x: x["indeks_bulan"])
        if not baris:
            continue
        pertama = baris[0]["bucket_open_beda"]
        terakhir = baris[-1]["bucket_open_beda"]
        if terakhir:
            simbol_masih_beda_di_bulan_terakhir_awal.append(simbol)
        elif pertama:
            simbol_reda_di_dalam_k.append(simbol)
        if pertama and terakhir < pertama:
            simbol_menurun.append(simbol)

    return {
        "k_awal": K_AWAL,
        "bulan_diukur": bulan_diukur,
        "total_bucket_beda_awal": total_awal,
        "total_bucket_beda_kendali": total_kendali,
        "persen_kendali_atas_awal": persen(total_kendali, total_awal),
        "menit_hilang_total": menit_hilang_total,
        "duplikat_total": duplikat_total,
        "simbol_kendali_beda": simbol_kendali_beda,
        "simbol_masih_beda_di_bulan_terakhir_awal": simbol_masih_beda_di_bulan_terakhir_awal,
        "simbol_reda_di_dalam_k": simbol_reda_di_dalam_k,
        "simbol_menurun": simbol_menurun,
        "galat": galat,
        "per_simbol": per_simbol,
    }


def rencana_simbol(simbol: str) -> dict:
    """Bulan yang akan disampel untuk satu simbol."""
    bersama = sorted(
        set(arsip.bulan_tersedia(simbol, "1m"))
        & set(arsip.bulan_tersedia(simbol, "5m"))
        & set(arsip.bulan_tersedia(simbol, "15m"))
    )
    rencana = pilih_bulan(bersama)
    rencana["simbol"] = simbol
    return rencana


def jalankan() -> dict:
    catatan = {"mulai_utc": sekarang(), "tahap": "mulai"}
    tulis(PROGRES, catatan)

    rencana = []
    for simbol in PROBE:
        try:
            rencana.append(rencana_simbol(simbol))
        except Exception as exc:  # noqa: BLE001
            rencana.append({"simbol": simbol, "galat": str(exc)[:300]})
    catatan["tahap"] = "rencana selesai"
    tulis(PROGRES, catatan)

    pengukuran = []
    for r in rencana:
        simbol = r.get("simbol")
        if r.get("galat"):
            pengukuran.append({"simbol": simbol, "galat": r["galat"]})
            continue
        tugas = [(b, "awal", i + 1) for i, b in enumerate(r.get("awal") or [])]
        if r.get("kendali"):
            tugas.append((r["kendali"], "kendali", 0))
        for bulan, peran, indeks in tugas:
            try:
                pengukuran.append(ukur_bulan(simbol, bulan, peran, indeks))
            except Exception as exc:  # noqa: BLE001
                pengukuran.append(
                    {
                        "simbol": simbol,
                        "bulan": bulan,
                        "peran": peran,
                        "indeks_bulan": indeks,
                        "galat": str(exc)[:300],
                    }
                )
            catatan["terakhir"] = f"{simbol} {bulan} ({peran})"
            catatan["selesai"] = len(pengukuran)
            tulis(PROGRES, catatan)

    laporan = {
        "nama": "rentang_kc6",
        "bukan_bukti": True,
        "waktu_utc": sekarang(),
        "sidik_kode": sidik_kode(),
        "sumber_arsip": arsip.S3,
        "simbol_diukur": PROBE,
        "rencana": rencana,
        "pengukuran": pengukuran,
        "ringkas": ringkas_rentang(pengukuran),
    }
    tulis(LAPORAN, laporan)
    catatan["tahap"] = "selesai"
    tulis(PROGRES, catatan)
    return laporan


if __name__ == "__main__":
    hasil = jalankan()
    print(
        json.dumps(
            {k: v for k, v in hasil.items() if k != "pengukuran"},
            indent=2,
            ensure_ascii=False,
        )
    )
    sys.exit(0)
