"""Resample 1m ke N menit, eksak dengan Decimal, tanpa jaringan.

Seluruh interval selain 1m di repo ini DITURUNKAN dari 1m (ADR-A002 bagian 3).
Itu hanya sah bila penurunannya terbukti cocok dengan berkas asli arsip, jadi
modul ini sengaja memisahkan dua hal: cara menurunkan bar, dan cara MENGUKUR
kecocokannya. Keduanya diuji terpisah.

Aritmetika memakai Decimal atas teks asli arsip. Dengan float, penjumlahan
volume tidak eksak, dan setiap ketidakcocokan menjadi tidak bisa dibedakan
antara kesalahan agregasi dan kesalahan pembulatan.
"""
from __future__ import annotations

from decimal import Decimal

MS_MENIT = 60_000

KOLOM_HARGA = ["open", "high", "low", "close"]
KOLOM_JUMLAH = [
    "volume",
    "quote_volume",
    "trades",
    "taker_buy_base",
    "taker_buy_quote",
]
KOLOM_BANDING = KOLOM_HARGA + KOLOM_JUMLAH


def desimal(nilai) -> Decimal:
    """Ubah satu sel menjadi Decimal tanpa melewati float."""
    if isinstance(nilai, Decimal):
        return nilai
    return Decimal(str(nilai).strip())


def ke_baris(rekaman: dict) -> dict:
    """Normalkan satu rekaman mentah menjadi bar bertipe pasti."""
    bar = {
        "open_time": int(rekaman["open_time"]),
        "close_time": int(rekaman["close_time"]),
    }
    for kolom in KOLOM_BANDING:
        bar[kolom] = desimal(rekaman[kolom])
    return bar


def resample(rekaman, menit: int) -> list:
    """Turunkan bar N menit dari bar 1m.

    Ember diselaraskan ke kelipatan N menit sejak epoch, sama seperti arsip.
    Bar dengan menit tidak lengkap tetap dihasilkan, dan cacah menit yang
    benar-benar ada dicatat di `menit_terisi`; menyembunyikannya akan membuat
    lubang data terlihat seperti bar normal.
    """
    if menit < 1:
        raise ValueError("menit harus >= 1")
    lebar = menit * MS_MENIT
    ember: dict = {}
    for rekam in sorted((ke_baris(r) for r in rekaman), key=lambda b: b["open_time"]):
        kunci = (rekam["open_time"] // lebar) * lebar
        agregat = ember.get(kunci)
        if agregat is None:
            agregat = {
                "open_time": kunci,
                "open": rekam["open"],
                "high": rekam["high"],
                "low": rekam["low"],
                "close": rekam["close"],
                "close_time": rekam["close_time"],
                "menit_terisi": 0,
            }
            for kolom in KOLOM_JUMLAH:
                agregat[kolom] = Decimal(0)
            ember[kunci] = agregat
        if rekam["high"] > agregat["high"]:
            agregat["high"] = rekam["high"]
        if rekam["low"] < agregat["low"]:
            agregat["low"] = rekam["low"]
        agregat["close"] = rekam["close"]
        agregat["close_time"] = rekam["close_time"]
        agregat["menit_terisi"] += 1
        for kolom in KOLOM_JUMLAH:
            agregat[kolom] = agregat[kolom] + rekam[kolom]
    return [ember[k] for k in sorted(ember)]


def bandingkan(hasil, asli, kolom=None) -> dict:
    """Bandingkan bar turunan dengan bar asli arsip, per waktu dan per kolom.

    Keluarannya sengaja memuat cacah dan contoh, bukan sekadar lulus/gagal:
    putusan gerbang dibuat di tempat lain, atas angka ini.
    """
    kolom = list(kolom or KOLOM_BANDING)
    kiri = {b["open_time"]: b for b in hasil}
    kanan = {}
    for rekam in asli:
        bar = ke_baris(rekam)
        kanan[bar["open_time"]] = bar

    sama = sorted(set(kiri) & set(kanan))
    hanya_kiri = sorted(set(kiri) - set(kanan))
    hanya_kanan = sorted(set(kanan) - set(kiri))

    beda = {k: 0 for k in kolom}
    contoh = []
    for waktu in sama:
        for k in kolom:
            if kiri[waktu][k] != kanan[waktu][k]:
                beda[k] += 1
                if len(contoh) < 5:
                    contoh.append(
                        {
                            "open_time": waktu,
                            "kolom": k,
                            "resample": str(kiri[waktu][k]),
                            "asli": str(kanan[waktu][k]),
                        }
                    )
    return {
        "bar_cocok_waktu": len(sama),
        "jumlah_hanya_di_resample": len(hanya_kiri),
        "jumlah_hanya_di_asli": len(hanya_kanan),
        "contoh_hanya_di_resample": hanya_kiri[:5],
        "contoh_hanya_di_asli": hanya_kanan[:5],
        "beda_per_kolom": beda,
        "contoh_beda": contoh,
    }
