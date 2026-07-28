"""Uji fungsi murni diagnosa KC-14b (tanpa jaringan)."""

from lux_ai.serapan import diagnosa_kc14b as d

M = d.MS_MENIT


def test_url_harian_memakai_jalur_daily():
    u = d.url_harian("AERGOUSDT", "1m", "2025-04-16")
    assert "/daily/klines/AERGOUSDT/1m/AERGOUSDT-1m-2025-04-16.zip" in u
    assert "/monthly/" not in u


def test_url_harian_meng_encode_non_ascii():
    u = d.url_harian("\u5e01\u5b89\u4eba\u751fUSDT", "1m", "2025-10-01")
    assert "%E5%B8%81" in u
    assert "\u5e01" not in u


def test_menit_lubang_panjang_dan_ujung():
    lubang = d.menit_lubang(1000, 3)
    assert lubang == [1000, 1000 + M, 1000 + 2 * M]


def test_menit_lubang_kosong():
    assert d.menit_lubang(1000, 0) == []


def test_ringkas_tanpa_hari_tersedia_tidak_mengukur():
    r = d.ringkas([{"tersedia": False, "putusan": "TIDAK MENGUKUR"}])
    assert r["status"] == "TIDAK MENGUKUR"
    assert r["cacah_hari_tidak_tersedia"] == 1
    assert r["hari_diperiksa"] == 0


def test_ringkas_menjumlahkan_medan_penggugur():
    catatan = [
        {
            "tersedia": True,
            "putusan": "MENDUKUNG_H-A003",
            "menit_hadir_di_harian_saat_bulanan_hilang": 660,
        },
        {
            "tersedia": True,
            "putusan": "H-A003_GUGUR",
            "menit_hadir_di_harian_saat_bulanan_hilang": 0,
        },
    ]
    r = d.ringkas(catatan)
    assert r["menit_hadir_di_harian_saat_bulanan_hilang"] == 660
    assert r["cacah_mendukung_h_a003"] == 1
    assert r["cacah_h_a003_gugur"] == 1
    assert r["status"] == "TERUKUR"
