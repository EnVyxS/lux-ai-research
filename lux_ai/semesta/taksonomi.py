"""Taksonomi instrumen semesta arsip.

Membayar utang 27 dan menyiapkan syarat (h) utang 24.

Masukan: `reports/semesta_rentang.json`, laporan yang TIDAK bersidik (KC-12).
Keluaran: `reports/taksonomi_semesta.json`, yang BERSIDIK (aturan 7, 31, 35),
ditandai `bukan_bukti` (aturan 10), memuat penyebut eksplisit (aturan 30),
cacah yang dilaporkan walau nol (aturan 18, 24), serta cacah dan contoh nama
yang tidak tergolong (aturan 32).

Tidak menyentuh jaringan (aturan 13).
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any, Dict, List

SUMBER = "reports/semesta_rentang.json"
KELUARAN = "reports/taksonomi_semesta.json"

# Bulan terakhir semesta menurut survei. Simbol yang berhenti lebih awal
# dihitung sebagai terhenti.
AKHIR_SEMESTA = "2026-06"

# Akhiran tanggal ekspirasi gaya Binance: _YYMMDD (mis. BTCUSDT_210326).
POLA_EKSPIRASI = re.compile(r"_\d{6}$")

# Urutan PENTING: diperiksa dari kiri ke kanan.
KUTIPAN = ("USDT", "USDC", "BUSD", "USD1", "BTC")

# Kutipan yang bukan mata uang fiat/stabil.
KUTIPAN_NON_FIAT = frozenset({"BTC"})

# Indeks TIDAK bisa dikenali dari bentuk namanya; daftar ini eksplisit dan
# wajib ditinjau bila semesta bertambah. Ini memerlukan verifikasi.
INDEKS = frozenset({"DEFIUSDT", "BTCDOMUSDT", "BLUEBIRDUSDT"})

JENIS = (
    "futures_kedaluwarsa",
    "sisa_settled",
    "indeks",
    "perpetual_usdt",
    "perpetual_usdc",
    "perpetual_busd",
    "perpetual_usd1",
    "basis_non_fiat",
    "tak_tergolong",
)

CATATAN_BATAS = (
    "Saham, ETF, dan komoditas yang di-token-kan (mis. AAPLUSDT, XAUUSDT) "
    "TIDAK dapat dibedakan dari perpetual koin lewat bentuk nama, sehingga di "
    "sini mereka masuk perpetual_usdt. Memisahkannya menuntut daftar instrumen "
    "dari bursa. Ini memerlukan verifikasi."
)

BATAS_CONTOH = 10


def sidik_kode() -> str:
    """sha256 berkas modul ini sendiri (aturan 7, 22)."""
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def sidik_data(data: bytes) -> str:
    """sha256 byte masukan apa adanya (aturan 31)."""
    return hashlib.sha256(data).hexdigest()


def non_ascii(nama: str) -> bool:
    return any(ord(huruf) > 127 for huruf in nama)


def jenis_instrumen(nama: str) -> str:
    """Golongkan satu nama pasar.

    Urutan pemeriksaan mengikat: ekspirasi, lalu sisa penyelesaian, lalu daftar
    indeks, baru mata uang kutipan. Membalik urutan ini salah, sebab
    `BTCUSDT_210326` juga berakhiran angka dan `ICPUSDT_SETTLED` juga memuat
    `USDT`.
    """
    if POLA_EKSPIRASI.search(nama):
        return "futures_kedaluwarsa"
    if nama.endswith("SETTLED"):
        return "sisa_settled"
    if nama in INDEKS:
        return "indeks"
    for kutipan in KUTIPAN:
        if nama.endswith(kutipan) and len(nama) > len(kutipan):
            if kutipan in KUTIPAN_NON_FIAT:
                return "basis_non_fiat"
            return "perpetual_" + kutipan.lower()
    return "tak_tergolong"


def _bulan_valid(nilai: Any) -> bool:
    return isinstance(nilai, str) and re.fullmatch(r"\d{4}-\d{2}", nilai) is not None


def ringkas(rentang: Dict[str, Any]) -> Dict[str, Any]:
    """Susun ringkasan dari peta simbol -> rentang.

    Penyebutnya adalah cacah entri di `rentang`. Bila nol, statusnya
    `TIDAK MENGUKUR` (aturan 30).
    """
    cacah_per_jenis: Dict[str, int] = {nama: 0 for nama in JENIS}
    bulan_per_jenis: Dict[str, int] = {nama: 0 for nama in JENIS}
    contoh_tak_tergolong: List[str] = []
    contoh_non_ascii: List[str] = []
    entri_cacat: List[str] = []

    jumlah_bulan = 0
    cacah_non_ascii = 0
    bulan_non_ascii = 0
    cacah_terhenti = 0
    paling_awal: str | None = None
    paling_akhir: str | None = None

    for simbol, isi in rentang.items():
        if not isinstance(isi, dict):
            entri_cacat.append(simbol)
            continue
        awal = isi.get("bulan_pertama")
        akhir = isi.get("bulan_terakhir")
        cacah = isi.get("cacah_bulan")
        if not _bulan_valid(awal) or not _bulan_valid(akhir) or not isinstance(cacah, int):
            entri_cacat.append(simbol)
            continue

        jenis = jenis_instrumen(simbol)
        cacah_per_jenis[jenis] += 1
        bulan_per_jenis[jenis] += cacah
        jumlah_bulan += cacah

        if jenis == "tak_tergolong" and len(contoh_tak_tergolong) < BATAS_CONTOH:
            contoh_tak_tergolong.append(simbol)

        if non_ascii(simbol):
            cacah_non_ascii += 1
            bulan_non_ascii += cacah
            if len(contoh_non_ascii) < BATAS_CONTOH:
                contoh_non_ascii.append(simbol)

        if akhir < AKHIR_SEMESTA:
            cacah_terhenti += 1

        if paling_awal is None or awal < paling_awal:
            paling_awal = awal
        if paling_akhir is None or akhir > paling_akhir:
            paling_akhir = akhir

    cacah_simbol = sum(cacah_per_jenis.values())
    status = "TERUKUR" if cacah_simbol > 0 else "TIDAK MENGUKUR"

    return {
        "bukan_bukti": True,
        "status": status,
        "penyebut": {
            "entri_dibaca": len(rentang),
            "cacah_simbol": cacah_simbol,
            "cacah_entri_cacat": len(entri_cacat),
            "contoh_entri_cacat": entri_cacat[:BATAS_CONTOH],
        },
        "cacah_per_jenis": cacah_per_jenis,
        "bulan_per_jenis": bulan_per_jenis,
        "jumlah_bulan_total": jumlah_bulan,
        "bulan_paling_awal": paling_awal,
        "bulan_paling_akhir": paling_akhir,
        "cacah_terhenti": cacah_terhenti,
        "cacah_hidup": cacah_simbol - cacah_terhenti,
        "non_ascii": {
            "cacah": cacah_non_ascii,
            "jumlah_bulan": bulan_non_ascii,
            "contoh": contoh_non_ascii,
        },
        "cacah_tak_tergolong": cacah_per_jenis["tak_tergolong"],
        "contoh_tak_tergolong": contoh_tak_tergolong,
        "catatan_batas": CATATAN_BATAS,
        "akhir_semesta_diasumsikan": AKHIR_SEMESTA,
        "daftar_indeks_eksplisit": sorted(INDEKS),
    }


def jalankan(akar: str = ".") -> Dict[str, Any]:
    """Baca sumber, susun ringkasan bersidik, tulis keluaran."""
    basis = Path(akar)
    sumber = basis / SUMBER
    mentah = sumber.read_bytes()
    muatan = json.loads(mentah.decode("utf-8"))
    rentang = muatan.get("rentang", {})
    if not isinstance(rentang, dict):
        rentang = {}

    laporan = ringkas(rentang)
    laporan["sumber"] = SUMBER
    laporan["sumber_byte"] = len(mentah)
    laporan["sumber_kunci_tingkat_atas"] = sorted(muatan.keys())
    laporan["sumber_bersidik"] = "sidik_kode" in muatan
    laporan["sidik_data"] = sidik_data(mentah)
    laporan["sidik_kode"] = sidik_kode()

    tujuan = basis / KELUARAN
    tujuan.parent.mkdir(parents=True, exist_ok=True)
    tujuan.write_text(
        json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return laporan


def main() -> None:
    laporan = jalankan()
    print(json.dumps(laporan, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
