"""Uji atas CARA gerbang resample memilih bulan dan mencacah era.

Tidak menyentuh jaringan. Yang diuji di sini bukan hasil perbandingan bar,
melainkan alat ukurnya: pemilihan bulan, pencacahan era, dan syarat gagal.
"""
from lux_ai.serapan import uji_resample as ur


def test_pilih_bulan_uji_mengambil_ujung_dan_tidak_menggandakan():
    assert ur.pilih_bulan_uji([]) == []
    satu = ur.pilih_bulan_uji(["2024-03"])
    assert len(satu) == 1 and satu[0]["peran"] == "awal+akhir"
    banyak = ur.pilih_bulan_uji(["2021-05", "2020-01", "2026-06"])
    assert [p["bulan"] for p in banyak] == ["2020-01", "2026-06"]
    assert [p["peran"] for p in banyak] == ["awal", "akhir"]


def test_ringkas_era_memilah_dari_isi_bukan_dari_tanggal():
    pengukuran = [
        {
            "simbol": "BTCUSDT",
            "uji_bulan": [
                {"bulan": "2020-01", "berheader": False},
                {"bulan": "2026-06", "berheader": True},
            ],
        },
        {"simbol": "COCOSUSDT", "uji_bulan": [{"bulan": "2023-02", "berheader": True}]},
    ]
    r = ur.ringkas_era(pengukuran)
    assert r["bulan_diuji_total"] == 3
    assert r["bulan_era_tanpa_header"] == 1
    assert r["bulan_era_berheader"] == 2
    assert r["simbol_dengan_bulan_era_tanpa_header"] == ["BTCUSDT"]
    assert r["tanggal_tak_sepakat_dengan_isi"] == []


def test_ringkas_era_menandai_tanggal_yang_tidak_sepakat_dengan_isi():
    """Bulan 2023-05 tanpa header melanggar dugaan batas 2022-01; harus terlihat."""
    r = ur.ringkas_era(
        [{"simbol": "XUSDT", "uji_bulan": [{"bulan": "2023-05", "berheader": False}]}]
    )
    assert r["bulan_era_tanpa_header"] == 1
    assert r["tanggal_tak_sepakat_dengan_isi"] == [{"simbol": "XUSDT", "bulan": "2023-05"}]


def test_ringkas_era_tidak_menebak_era_yang_tak_terukur():
    r = ur.ringkas_era(
        [{"simbol": "YUSDT", "uji_bulan": [{"bulan": "2020-01", "berheader": None}]}]
    )
    assert r["bulan_era_tak_terukur"] == 1
    assert r["bulan_era_tanpa_header"] == 0
    assert r["bulan_era_berheader"] == 0
    assert r["simbol_dengan_bulan_era_tanpa_header"] == []


def _banding_bersih():
    return {
        "jumlah_hanya_di_resample": 0,
        "jumlah_hanya_di_asli": 0,
        "beda_per_kolom": {"open": 0, "high": 0, "low": 0, "close": 0, "volume": 3},
    }


def test_gerbang_lolos_bila_ohlc_cocok_walau_volume_beda():
    pengukuran = [
        {
            "simbol": "BTCUSDT",
            "uji_bulan": [
                {"bulan": "2020-01", "5m": _banding_bersih(), "15m": _banding_bersih()}
            ],
        }
    ]
    assert ur.lolos_gerbang(pengukuran) is True


def test_gerbang_gagal_bila_simbol_tidak_menguji_bulan_apa_pun():
    """Gerbang hijau tanpa pengukuran adalah gerbang yang berbohong (aturan 18)."""
    assert ur.lolos_gerbang([{"simbol": "BTCUSDT", "uji_bulan": []}]) is False
    assert ur.lolos_gerbang([{"simbol": "BTCUSDT"}]) is False


def test_gerbang_gagal_bila_ohlc_beda_atau_bar_sepihak():
    beda_ohlc = _banding_bersih()
    beda_ohlc["beda_per_kolom"]["high"] = 1
    assert (
        ur.lolos_gerbang(
            [
                {
                    "simbol": "X",
                    "uji_bulan": [
                        {"bulan": "2020-01", "5m": beda_ohlc, "15m": _banding_bersih()}
                    ],
                }
            ]
        )
        is False
    )
    sepihak = _banding_bersih()
    sepihak["jumlah_hanya_di_asli"] = 2
    assert (
        ur.lolos_gerbang(
            [
                {
                    "simbol": "X",
                    "uji_bulan": [
                        {"bulan": "2020-01", "5m": _banding_bersih(), "15m": sepihak}
                    ],
                }
            ]
        )
        is False
    )
