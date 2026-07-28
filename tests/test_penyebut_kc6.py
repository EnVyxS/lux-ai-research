"""Uji modul penyebut KC-6. Tanpa jaringan (aturan 14)."""
from __future__ import annotations

from lux_ai.serapan import penyebut_kc6 as p


def simpul(dibandingkan: int, open_beda: int, ohlc_beda: int = 0) -> dict:
    return {
        "bucket_dibandingkan": dibandingkan,
        "bucket_open_beda": open_beda,
        "bucket_ohlc_beda": ohlc_beda,
    }


def test_kumpulkan_menemukan_simpul_bersarang_sedalam_apa_pun():
    data = {
        "pengukuran": [
            {"simbol": "BTCUSDT", "bulan": {"5m": simpul(100, 1), "15m": simpul(50, 0)}},
            {"simbol": "ETHUSDT", "lain": {"dalam": {"5m": simpul(10, 2)}}},
        ],
        "ringkas": {"tanpa_medan": 1},
    }
    hasil = p.kumpulkan(data)
    assert len(hasil) == 3
    assert sum(s["bucket_dibandingkan"] for s in hasil) == 160
    assert sum(s["bucket_open_beda"] for s in hasil) == 3


def test_penanda_kelompok_diwariskan_ke_anak_dan_tak_dikenal_tetap_terlihat():
    data = {
        "a": {"peran": "kendali", "5m": simpul(10, 1)},
        "b": {"peran": "awal", "5m": simpul(20, 2)},
        "c": {"5m": simpul(30, 3)},
    }
    ringkas = p.ringkas(p.kumpulkan(data))
    kelompok = ringkas["per_kelompok"]
    assert kelompok["kendali"]["bucket_dibandingkan"] == 10
    assert kelompok["awal"]["bucket_dibandingkan"] == 20
    assert kelompok["tak_dikenal"]["bucket_dibandingkan"] == 30
    assert ringkas["total"]["simpul"] == 3
    assert ringkas["total"]["bucket_dibandingkan"] == 60


def test_laju_dihitung_dan_penyebut_nol_menolak_berbohong():
    ringkas = p.ringkas(p.kumpulkan({"x": {"peran": "awal", "5m": simpul(200, 1)}}))
    assert ringkas["total"]["laju_open_beda_persen"] == 0.5
    assert p.persen(0, 0) is None
    kosong = p.ringkas([])
    assert kosong["total"]["laju_open_beda_persen"] is None
