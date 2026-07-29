"""Uji kohort puncak dan pemilihan pasangan uji CDN (FUNDING VERSI 5).

Berkas terpisah dari `test_funding.py` dengan sengaja: `push_files` menulis
ulang seluruh isi berkas, dan menulis ulang berkas panjang hanya untuk
menambah tiga fungsi adalah risiko ekor-terpotong yang tidak perlu dibayar.

Tiga fungsi uji. Tidak memakai `parametrize`, sehingga satu fungsi = satu butir
CI dan cacah butir dapat diramalkan (aturan 47).
"""

from lux_ai.serapan import funding


def _baris(simbol, mulai, ekor, klines_terakhir, funding_terakhir):
    """Baris per-simbol seperti yang dihasilkan `jalankan`, seperlunya saja."""
    return {
        "simbol": simbol,
        "mulai_lubang_ekor": mulai,
        "bentuk_lubang": {"awal": 0, "ekor": ekor, "tengah": 0, "hilang": ekor},
        "bulan_klines_terakhir": klines_terakhir,
        "bulan_funding_terakhir": funding_terakhir,
    }


def test_kumpulkan_kohort_memisahkan_satuan_simbol_dan_simbol_bulan():
    """Dua satuan yang berbeda tidak boleh menghasilkan satu angka."""
    per_simbol = [
        _baris("BUSDT", "2025-07", 12, "2026-06", "2025-06"),
        _baris("AUSDT", "2025-07", 12, "2026-06", "2025-06"),
        _baris("CUSDT", "2026-01", 6, "2026-06", "2025-12"),
        _baris("DUSDT", None, 0, "2026-06", "2026-06"),
    ]
    hasil = funding.kumpulkan_kohort(per_simbol, "2025-07")
    assert hasil["cacah_simbol"] == 2
    assert hasil["cacah_simbol_bulan"] == 24
    assert hasil["cacah_simbol"] != hasil["cacah_simbol_bulan"]
    assert hasil["simbol"] == ["AUSDT", "BUSDT"]
    assert hasil["seragam_bulan_klines_terakhir"] is True
    assert hasil["histogram_bulan_klines_terakhir"] == {"2026-06": 2}


def test_kumpulkan_kohort_tidak_mengaku_seragam_saat_bulan_terakhir_hilang():
    """Histogram menyaring None; tanpa medan penggugur ia tampak seragam."""
    per_simbol = [
        _baris("AUSDT", "2025-07", 12, "2026-06", "2025-06"),
        _baris("BUSDT", "2025-07", 12, None, "2025-06"),
    ]
    hasil = funding.kumpulkan_kohort(per_simbol, "2025-07")
    assert hasil["cacah_simbol"] == 2
    assert hasil["cacah_tanpa_bulan_terakhir"] == 1
    assert hasil["histogram_bulan_klines_terakhir"] == {"2026-06": 1}
    assert hasil["seragam_bulan_klines_terakhir"] is False
    beda = [
        _baris("AUSDT", "2025-07", 12, "2026-06", "2025-06"),
        _baris("BUSDT", "2025-07", 12, "2026-01", "2025-06"),
    ]
    assert funding.kumpulkan_kohort(beda, "2025-07")["seragam_bulan_klines_terakhir"] is False


def test_pasangan_uji_memakai_bulan_funding_terakhir_dan_membatasi_cacah():
    """Kendali harus bulan yang menurut listing ada, dan cacahnya dibatasi."""
    per_simbol = [
        _baris("AUSDT", "2025-07", 12, "2026-06", "2025-06"),
        _baris("BUSDT", "2025-07", 12, "2026-06", "2025-06"),
        _baris("CUSDT", "2025-07", 12, "2026-06", None),
        _baris("DUSDT", "2026-01", 6, "2026-06", "2025-12"),
    ]
    pasang = funding.pasangan_uji(per_simbol, "2025-07")
    assert pasang == [
        ("AUSDT", "2025-07", "2025-06"),
        ("BUSDT", "2025-07", "2025-06"),
    ]
    assert funding.pasangan_uji(per_simbol, "2025-07", batas=1) == [
        ("AUSDT", "2025-07", "2025-06")
    ]
    assert funding.pasangan_uji(per_simbol, None) == []
