"""Diagnosa KC-14b — apakah lubang 1m itu jeda pasar atau cacat perakitan?

Diagnosa KC-14 menutup H-A002b (kerusakan satu interval): 5m dan 15m ikut
kosong persis di tempat 1m kosong. Tetapi ia TIDAK bisa memisahkan dua sebab
yang tersisa, karena semua interval bulanan mungkin dirakit dari sumber harian
yang sama:

- **jeda pasar** — bursa berhenti mengutip;
- **H-A003** — satu segmen HARIAN hilang saat arsip bulanan dirakit.

Yang menerbitkan kecurigaan: ketiga lubang mulai **tepat 00:00 UTC** dan
panjangnya kelipatan 15 menit (660, 510, 705). Sepinya pasar tidak tahu jam
berapa tengah malam UTC.

Arsip juga menerbitkan berkas HARIAN, dan itulah pemisahnya. Bila berkas harian
tanggal yang sama memuat menit yang absen dari berkas bulanan, arsip bulanan
cacat (**KC-15**) dan seluruh serapan yang memakainya wajib ditinjau. Bila
harian ikut kosong, H-A003 gugur.

Medan penggugur wajib (aturan 24): `menit_hadir_di_harian_saat_bulanan_hilang`
dilaporkan walau nol, beserta `cacah_baris_harian` mentahnya, supaya angka itu
bisa diperiksa tanpa memercayai putusan modul ini.

URL harian disusun di sini, bukan di `arsip.py`, agar `sidik_kode` rantai
serapan tidak berubah dan manifes lama tetap sebanding (aturan 22).

Aturan yang ditegakkan: 20, 21, 24, 25, 26, 30, 32.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

from . import arsip, klines

KELUARAN = "reports/diagnosa_kc14b.json"
MS_MENIT = 60_000
MENIT_SEHARI = 1440
BATAS_CONTOH = 20

# (simbol, tanggal, stempel awal lubang ms, panjang lubang menit)
# Keempat angka diambil dari reports/diagnosa_kc14.json, bukan dikarang.
TERSANGKA: Tuple[Tuple[str, str, int, int], ...] = (
    ("AERGOUSDT", "2025-04-16", 1744761600000, 660),
    ("CVCUSDT", "2025-05-16", 1747353600000, 510),
    ("SLPUSDT", "2025-07-23", 1753228800000, 705),
)


def sidik_kode() -> str:
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(["diagnosa_kc14b.py", "arsip.py", "klines.py"]):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def url_harian(simbol: str, interval: str, tanggal: str) -> str:
    """URL arsip HARIAN; bentuknya sejajar url_klines bulanan."""
    s = arsip.segmen(simbol)
    return f"{arsip.CDN}/{arsip.AKAR}/daily/klines/{s}/{interval}/{s}-{interval}-{tanggal}.zip"


def menit_lubang(mulai_ms: int, panjang: int) -> List[int]:
    return [mulai_ms + i * MS_MENIT for i in range(panjang)]


def periksa_satu(simbol: str, tanggal: str, mulai_ms: int, panjang: int) -> Dict[str, Any]:
    catatan: Dict[str, Any] = {
        "simbol": simbol,
        "tanggal": tanggal,
        "panjang_lubang_menit": panjang,
        "mulai_lubang_ms": mulai_ms,
    }
    url = url_harian(simbol, "1m", tanggal)
    catatan["url"] = url
    try:
        data = arsip.unduh_terverifikasi(url)
    except Exception as exc:  # noqa: BLE001
        catatan["tersedia"] = False
        catatan["sebab"] = str(exc)[:200]
        catatan["putusan"] = "TIDAK MENGUKUR"
        return catatan

    catatan["tersedia"] = True
    catatan["checksum"] = arsip.sha256_bytes(data)
    df = klines.baca_zip(data)
    df, dibuang = klines.rapikan(df)
    stempel = set(int(x) for x in df["open_time"].tolist())
    lubang = menit_lubang(mulai_ms, panjang)
    hadir = sorted(t for t in lubang if t in stempel)

    catatan["cacah_baris_harian"] = len(stempel)
    catatan["baris_dibuang"] = int(dibuang)
    catatan["stempel_pertama_ms"] = min(stempel) if stempel else None
    catatan["stempel_terakhir_ms"] = max(stempel) if stempel else None
    catatan["menit_hadir_di_harian_saat_bulanan_hilang"] = len(hadir)
    catatan["contoh_menit_hadir"] = hadir[:BATAS_CONTOH]
    catatan["cacah_baris_harian_diharap_bila_jeda_pasar"] = MENIT_SEHARI - panjang
    catatan["putusan"] = "MENDUKUNG_H-A003" if hadir else "H-A003_GUGUR"
    return catatan


def ringkas(catatan: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    diperiksa = [c for c in catatan if c.get("tersedia")]
    putusan = [c.get("putusan") for c in catatan]
    return {
        "hari_diminta": len(catatan),
        "hari_diperiksa": len(diperiksa),
        "cacah_hari_tersedia": len(diperiksa),
        "cacah_hari_tidak_tersedia": sum(1 for c in catatan if c.get("tersedia") is False),
        "menit_hadir_di_harian_saat_bulanan_hilang": sum(
            int(c.get("menit_hadir_di_harian_saat_bulanan_hilang", 0)) for c in diperiksa
        ),
        "cacah_mendukung_h_a003": putusan.count("MENDUKUNG_H-A003"),
        "cacah_h_a003_gugur": putusan.count("H-A003_GUGUR"),
        "cacah_tidak_mengukur": putusan.count("TIDAK MENGUKUR"),
        "status": "TERUKUR" if diperiksa else "TIDAK MENGUKUR",
        "catatan_penggugur": (
            "menit_hadir_di_harian_saat_bulanan_hilang > 0 berarti berkas HARIAN memuat "
            "menit yang absen dari berkas BULANAN: arsip bulanan cacat (KC-15) dan "
            "seluruh serapan yang memakainya wajib ditinjau (aturan 24)"
        ),
        "catatan_rentang": (
            "3 tanggal dari 3 simbol-bulan yang gagal di pecahan 0; bukan sampel semesta "
            "(aturan 20)"
        ),
    }


def jalankan(akar: str = ".") -> Dict[str, Any]:
    catatan = [periksa_satu(*t) for t in TERSANGKA]
    laporan = ringkas(catatan)
    laporan["bukan_bukti"] = False
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
