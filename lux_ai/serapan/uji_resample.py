"""Uji integritas resample atas 12 simbol probe, dijalankan di runner.

Membandingkan bar 5m dan 15m yang DITURUNKAN dari 1m dengan berkas 5m dan 15m
ASLI dari arsip. Berkas asli itu dipakai HANYA di sini; ADR-A002 bagian 3
melarang memakainya untuk backtest mana pun.

Versi kedua menguji DUA bulan per simbol: bulan bersama PERTAMA dan bulan
bersama TERAKHIR. Versi pertama hanya menguji bulan terakhir, yang seluruhnya
jatuh di era berheader, sehingga era tanpa header (s.d. 2021-12) belum pernah
diuji resample-nya sama sekali — itu utang 12 dan ramalan R-12.

Era tiap bulan yang diuji DITENTUKAN DARI ISI BERKAS lewat
`klines.punya_header`, bukan dari tanggalnya. Tanggal hanya dipakai sebagai
pembanding, karena yang hendak diuji justru apakah tanggal dan isi sepakat.

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

# Batas era menurut survei semesta: bulan pertama yang berheader adalah 2022-01.
# Dipakai HANYA untuk membandingkan dugaan tanggal dengan isi berkas.
BATAS_HEADER = "2022-01"


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


def pilih_bulan_uji(bersama: list) -> list:
    """Pilih bulan bersama PERTAMA dan TERAKHIR, tanpa menguji satu bulan dua kali.

    Bila hanya ada satu bulan bersama, bulan itu memikul kedua peran sekaligus
    dan dilaporkan apa adanya, bukan digandakan menjadi dua pengukuran semu.
    """
    if not bersama:
        return []
    urut = sorted(bersama)
    if len(urut) == 1:
        return [{"bulan": urut[0], "peran": "awal+akhir"}]
    return [{"bulan": urut[0], "peran": "awal"}, {"bulan": urut[-1], "peran": "akhir"}]


def ringkas_era(pengukuran: list) -> dict:
    """Cacah bulan yang benar-benar diuji, dipilah menurut era HASIL PENGUKURAN.

    Aturan 18: gerbang wajib melaporkan cacah hal yang benar-benar dibandingkan.
    Bulan yang eranya tidak terukur (`berheader` bukan True/False) TIDAK boleh
    dihitung sebagai era mana pun; ia dihitung terpisah supaya ketidaktahuan
    tetap kelihatan.
    """
    total = era_lama = era_baru = tak_terukur = 0
    simbol_era_lama = []
    tanggal_tak_sepakat = []
    for s in pengukuran:
        for u in s.get("uji_bulan") or []:
            total += 1
            bh = u.get("berheader")
            bulan = u.get("bulan")
            if bh is False:
                era_lama += 1
                if s.get("simbol") not in simbol_era_lama:
                    simbol_era_lama.append(s.get("simbol"))
            elif bh is True:
                era_baru += 1
            else:
                tak_terukur += 1
                continue
            if bulan and (bulan >= BATAS_HEADER) != bool(bh):
                tanggal_tak_sepakat.append({"simbol": s.get("simbol"), "bulan": bulan})
    return {
        "bulan_diuji_total": total,
        "bulan_era_tanpa_header": era_lama,
        "bulan_era_berheader": era_baru,
        "bulan_era_tak_terukur": tak_terukur,
        "simbol_dengan_bulan_era_tanpa_header": simbol_era_lama,
        "batas_header_dipakai": BATAS_HEADER,
        "tanggal_tak_sepakat_dengan_isi": tanggal_tak_sepakat,
    }


def muat(simbol: str, interval: str, bulan: str):
    """Unduh terverifikasi lalu baca sebagai teks apa adanya."""
    data = arsip.unduh_terverifikasi(arsip.url_klines(simbol, interval, bulan))
    df, dibuang = klines.rapikan(klines.baca_zip(data, teks=True))
    return data, df, int(dibuang)


def uji_bulan(simbol: str, bulan: str, peran: str) -> dict:
    """Bandingkan 5m dan 15m turunan dengan aslinya untuk satu simbol-bulan."""
    keluar = {"bulan": bulan, "peran": peran}
    data1, df1, dibuang = muat(simbol, "1m", bulan)
    keluar["baris_1m"] = int(len(df1))
    keluar["baris_1m_dibuang"] = dibuang
    keluar["berheader"] = klines.punya_header(klines.baris_pertama(data1))

    rekaman = df1.to_dict("records")
    for menit, nama in ((5, "5m"), (15, "15m")):
        try:
            _, dfn, dibuang_n = muat(simbol, nama, bulan)
            banding = rs.bandingkan(rs.resample(rekaman, menit), dfn.to_dict("records"))
            banding["baris_asli"] = int(len(dfn))
            banding["baris_asli_dibuang"] = dibuang_n
            keluar[nama] = banding
        except Exception as exc:  # noqa: BLE001
            keluar[nama] = {"galat": str(exc)[:300]}
    return keluar


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
    hasil["bulan_bersama_pertama"] = bersama[0] if bersama else None
    hasil["bulan_bersama_terakhir"] = bersama[-1] if bersama else None
    if not bersama:
        hasil["galat"] = "tidak ada bulan yang punya 1m, 5m, dan 15m sekaligus"
        return hasil

    # Bila 5m atau 15m mulai belakangan, bulan awal yang diuji BUKAN bulan 1m
    # pertama. Selisih itu dicatat supaya klaim cakupan tidak dibesar-besarkan.
    hasil["bulan_awal_tertinggal_dari_1m"] = bersama[0] != bulan_1m[0]

    hasil["uji_bulan"] = [
        uji_bulan(simbol, p["bulan"], p["peran"]) for p in pilih_bulan_uji(bersama)
    ]
    return hasil


def lolos_gerbang(pengukuran) -> bool:
    """Gerbang keras: OHLC wajib cocok persis dan himpunan bar wajib sama.

    Simbol tanpa satu pun bulan teruji dianggap GAGAL, bukan lolos. Gerbang yang
    hijau karena tidak menguji apa pun adalah gerbang yang berbohong.
    """
    for simbol in pengukuran:
        if "galat" in simbol:
            return False
        bulan_diuji = simbol.get("uji_bulan") or []
        if not bulan_diuji:
            return False
        for u in bulan_diuji:
            for nama in ("5m", "15m"):
                banding = u.get(nama)
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
    bar_dibandingkan = 0
    for simbol in pengukuran:
        for u in simbol.get("uji_bulan") or []:
            for nama in ("5m", "15m"):
                banding = u.get(nama) or {}
                bar_dibandingkan += int(banding.get("baris_asli") or 0)
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
        "ringkas_era": ringkas_era(pengukuran),
        "total_bar_asli_dibandingkan": bar_dibandingkan,
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
