"""Diagnosa KC-14 — menit hilang di arsip 1m: jeda pasar atau arsip cacat?

Dipicu oleh pecahan 0 (run `30353584831`): 3 dari 2.411 simbol-bulan
dijatuhkan gerbang pada klausa `tanpa_menit_hilang` dan `jarak_60_detik`,
total 1.875 menit hilang.

ADR-A006 Keputusan 2 mewajibkan uji pemisah, BUKAN tebakan:

- **H-A002a** bursa berhenti mengutip → arsipnya benar, lubang itu fakta pasar.
- **H-A002b** berkas arsip cacat → premis "arsip 1m adalah kebenaran", dasar
  seluruh ADR-A002, retak.

Tiga medan pemisahnya:

1. **Banding lintas interval.** Slot 5m dan 15m ASLI yang menaungi menit hilang
   diperiksa. Bila 5m juga kosong di sana → mendukung H-A002a. Bila 5m HADIR
   sementara 1m kosong → mendukung **H-A002b**, dan itu menggugurkan hipotesis
   yang saya sukai. Medan `slot_5m_hadir_saat_1m_hilang` sengaja dibuat
   menonjol karena inilah yang bisa menjatuhkan seluruh ADR-A002 (aturan 24).
2. **Bentuk lubang.** Satu blok panjang cocok dengan jeda bursa; sebaran acak
   satu-satu cocok dengan berkas cacat.
3. **Ulang unduh.** Checksum unduhan kedua dibandingkan dengan yang pertama.
   Berbeda → kerusakan transportasi, bukan kedua hipotesis di atas.

Aturan yang ditegakkan: 20, 21, 24, 25, 26, 30, 32.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

from . import arsip, klines

KELUARAN = "reports/diagnosa_kc14.json"
MS_MENIT = 60_000
BATAS_CONTOH = 20

# Terukur pada pecahan 0; bukan pilihan, melainkan seluruh populasi yang gagal.
TERSANGKA: Tuple[Tuple[str, str], ...] = (
    ("AERGOUSDT", "2025-04"),
    ("CVCUSDT", "2025-05"),
    ("SLPUSDT", "2025-07"),
)
INTERVAL_BANDING = ("5m", "15m")
MENIT_PER = {"5m": 5, "15m": 15}


def sidik_kode() -> str:
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(["diagnosa_kc14.py", "arsip.py", "klines.py"]):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def menit_hilang(stempel: Sequence[int]) -> List[int]:
    """Menit yang absen di antara stempel pertama dan terakhir."""
    if len(stempel) < 2:
        return []
    ada = set(int(x) for x in stempel)
    awal, akhir = min(ada), max(ada)
    return [t for t in range(awal, akhir + MS_MENIT, MS_MENIT) if t not in ada]


def blok(hilang: Sequence[int]) -> List[Dict[str, int]]:
    """Kelompokkan menit hilang yang bersebelahan menjadi blok."""
    hasil: List[Dict[str, int]] = []
    for t in sorted(int(x) for x in hilang):
        if hasil and t == hasil[-1]["akhir_ms"] + MS_MENIT:
            hasil[-1]["akhir_ms"] = t
            hasil[-1]["panjang_menit"] += 1
        else:
            hasil.append({"mulai_ms": t, "akhir_ms": t, "panjang_menit": 1})
    return hasil


def slot_naungan(menit_ms: int, interval: str) -> int:
    """Stempel awal slot interval yang menaungi satu menit."""
    lebar = MENIT_PER[interval] * MS_MENIT
    return (menit_ms // lebar) * lebar


def stempel_dari_zip(data: bytes) -> List[int]:
    df = klines.baca_zip(data)
    df, _dibuang = klines.rapikan(df)
    return [int(x) for x in df["open_time"].tolist()]


def periksa_satu(simbol: str, bulan: str) -> Dict[str, Any]:
    catatan: Dict[str, Any] = {"simbol": simbol, "bulan": bulan}

    url1 = arsip.url_klines(simbol, "1m", bulan)
    data1 = arsip.unduh_terverifikasi(url1)
    catatan["checksum_1m"] = arsip.sha256_bytes(data1)
    ulang = arsip.unduh_terverifikasi(url1)
    catatan["checksum_1m_ulang"] = arsip.sha256_bytes(ulang)
    catatan["checksum_stabil"] = catatan["checksum_1m"] == catatan["checksum_1m_ulang"]

    stempel = stempel_dari_zip(data1)
    hilang = menit_hilang(stempel)
    daftar_blok = blok(hilang)
    catatan["cacah_baris_1m"] = len(stempel)
    catatan["cacah_menit_hilang"] = len(hilang)
    catatan["cacah_blok"] = len(daftar_blok)
    catatan["blok_terpanjang_menit"] = max((b["panjang_menit"] for b in daftar_blok), default=0)
    catatan["blok_tunggal_menit"] = sum(1 for b in daftar_blok if b["panjang_menit"] == 1)
    catatan["contoh_blok"] = daftar_blok[:BATAS_CONTOH]

    banding: Dict[str, Any] = {}
    for interval in INTERVAL_BANDING:
        try:
            data_lain = arsip.unduh_terverifikasi(arsip.url_klines(simbol, interval, bulan))
        except Exception as exc:  # noqa: BLE001
            banding[interval] = {"tersedia": False, "sebab": str(exc)[:160]}
            continue
        ada = set(stempel_dari_zip(data_lain))
        naungan = {slot_naungan(t, interval) for t in hilang}
        hadir = sorted(s for s in naungan if s in ada)
        banding[interval] = {
            "tersedia": True,
            "cacah_baris": len(ada),
            "slot_menaungi_menit_hilang": len(naungan),
            "slot_hadir_saat_1m_hilang": len(hadir),
            "slot_kosong_saat_1m_hilang": len(naungan) - len(hadir),
            "contoh_slot_hadir": hadir[:BATAS_CONTOH],
        }
    catatan["banding"] = banding

    lima = banding.get("5m", {})
    if not lima.get("tersedia"):
        catatan["putusan"] = "TIDAK MENGUKUR"
    elif lima.get("slot_menaungi_menit_hilang", 0) == 0:
        catatan["putusan"] = "TIDAK MENGUKUR"
    elif lima.get("slot_hadir_saat_1m_hilang", 0) > 0:
        catatan["putusan"] = "MENDUKUNG_H-A002b"
    else:
        catatan["putusan"] = "MENDUKUNG_H-A002a"
    return catatan


def ringkas(catatan: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    penyebut = len(catatan)
    total_hilang = sum(int(c.get("cacah_menit_hilang", 0)) for c in catatan)
    hadir_5m = sum(
        int((c.get("banding", {}).get("5m", {}) or {}).get("slot_hadir_saat_1m_hilang", 0))
        for c in catatan
    )
    putusan = [c.get("putusan") for c in catatan]
    return {
        "simbol_bulan_diperiksa": penyebut,
        "total_menit_hilang": total_hilang,
        "slot_5m_hadir_saat_1m_hilang": hadir_5m,
        "cacah_mendukung_h_a002a": putusan.count("MENDUKUNG_H-A002a"),
        "cacah_mendukung_h_a002b": putusan.count("MENDUKUNG_H-A002b"),
        "cacah_tidak_mengukur": putusan.count("TIDAK MENGUKUR"),
        "cacah_checksum_tak_stabil": sum(1 for c in catatan if c.get("checksum_stabil") is False),
        "status": "TERUKUR" if penyebut else "TIDAK MENGUKUR",
        "catatan_rentang": (
            "berlaku untuk 3 simbol-bulan yang GAGAL di pecahan 0 saja; pecahan 1..7 "
            "belum diperiksa, jadi dilarang menyimpulkan untuk seluruh semesta (aturan 20)"
        ),
        "catatan_penggugur": (
            "slot_5m_hadir_saat_1m_hilang > 0 berarti 5m punya data ketika 1m tidak; "
            "itu MENGGUGURKAN premis 'arsip 1m adalah kebenaran' dan ADR-A002 wajib "
            "ditinjau ulang (aturan 24)"
        ),
    }


def jalankan(akar: str = ".") -> Dict[str, Any]:
    catatan = [periksa_satu(s, b) for s, b in TERSANGKA]
    laporan = ringkas(catatan)
    laporan["bukan_bukti"] = False
    laporan["tersangka"] = [f"{s} {b}" for s, b in TERSANGKA]
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
