"""Uji taksonomi instrumen (utang 27, syarat (h) utang 24).

Setiap uji memuat kasus positif DAN negatif (aturan 12).
"""

from lux_ai.semesta import taksonomi as T


def test_ekspirasi_dikenali_dan_tidak_kelebihan():
    assert T.jenis_instrumen("BTCUSDT_210326") == "futures_kedaluwarsa"
    assert T.jenis_instrumen("ETHUSDT_261225") == "futures_kedaluwarsa"
    assert T.jenis_instrumen("BTCBUSD_210129") == "futures_kedaluwarsa"
    # Negatif: angka di tengah nama bukan ekspirasi.
    assert T.jenis_instrumen("1000PEPEUSDT") == "perpetual_usdt"


def test_settled_dua_ejaan():
    assert T.jenis_instrumen("CTKUSDTSETTLED") == "sisa_settled"
    assert T.jenis_instrumen("ICPUSDT_SETTLED") == "sisa_settled"
    # Negatif: nama biasa yang memuat huruf serupa tidak ikut tertangkap.
    assert T.jenis_instrumen("SETTLEDUSDT") == "perpetual_usdt"


def test_indeks_hanya_dari_daftar():
    assert T.jenis_instrumen("DEFIUSDT") == "indeks"
    assert T.jenis_instrumen("BTCDOMUSDT") == "indeks"
    # Negatif: pasar biasa tidak boleh dianggap indeks.
    assert T.jenis_instrumen("BTCUSDT") == "perpetual_usdt"


def test_mata_uang_kutipan():
    assert T.jenis_instrumen("BTCUSDT") == "perpetual_usdt"
    assert T.jenis_instrumen("ADABUSD") == "perpetual_busd"
    assert T.jenis_instrumen("BTCUSDC") == "perpetual_usdc"
    assert T.jenis_instrumen("BTCUSD1") == "perpetual_usd1"


def test_basis_non_fiat_dan_tak_tergolong():
    assert T.jenis_instrumen("ETHBTC") == "basis_non_fiat"
    # Negatif: nama tanpa kutipan dikenal harus JATUH ke tak_tergolong,
    # bukan dipaksa masuk golongan mana pun.
    assert T.jenis_instrumen("ETHUP") == "tak_tergolong"
    assert T.jenis_instrumen("USDT") == "tak_tergolong"


def test_nama_non_ascii_tidak_dibuang():
    nama = "\u5e01\u5b89\u4eba\u751fUSDT"
    assert T.non_ascii(nama) is True
    assert T.non_ascii("BTCUSDT") is False
    assert T.jenis_instrumen(nama) == "perpetual_usdt"
    laporan = T.ringkas({nama: {"bulan_pertama": "2025-10", "bulan_terakhir": "2026-06", "cacah_bulan": 9}})
    assert laporan["non_ascii"]["cacah"] == 1
    assert laporan["non_ascii"]["jumlah_bulan"] == 9
    assert laporan["non_ascii"]["contoh"] == [nama]


def test_penyebut_nol_berstatus_tidak_mengukur():
    laporan = T.ringkas({})
    assert laporan["status"] == "TIDAK MENGUKUR"
    assert laporan["penyebut"]["cacah_simbol"] == 0
    # Setiap golongan tetap hadir walau nol (aturan 24).
    for nama in T.JENIS:
        assert laporan["cacah_per_jenis"][nama] == 0
    assert laporan["bulan_paling_awal"] is None


def test_ringkas_menghitung_dan_menolak_entri_cacat():
    rentang = {
        "BTCUSDT": {"bulan_pertama": "2020-01", "bulan_terakhir": "2026-06", "cacah_bulan": 78},
        "SRMUSDT": {"bulan_pertama": "2020-09", "bulan_terakhir": "2024-05", "cacah_bulan": 45},
        "RUSAK": {"bulan_pertama": "bukan-bulan", "bulan_terakhir": "2026-06", "cacah_bulan": 1},
        "BUKAN_PETA": 7,
    }
    laporan = T.ringkas(rentang)
    assert laporan["penyebut"]["entri_dibaca"] == 4
    assert laporan["penyebut"]["cacah_simbol"] == 2
    assert laporan["penyebut"]["cacah_entri_cacat"] == 2
    assert laporan["jumlah_bulan_total"] == 123
    assert laporan["bulan_paling_awal"] == "2020-01"
    assert laporan["bulan_paling_akhir"] == "2026-06"
    assert laporan["cacah_terhenti"] == 1
    assert laporan["cacah_hidup"] == 1
