"""Uji KC-9: nama pasar non-ASCII pada penyusunan URL arsip.

Aturan 12 menuntut kasus POSITIF dan NEGATIF. Kasus positif memakai tiga nama
sungguhan yang ditemukan di arsip pada sesi 25; kasus negatif memakai nama ASCII
biasa yang TIDAK boleh berubah bentuk.

Aturan 32: nama pasar tidak boleh dianggap ASCII.
Aturan 14: uji ini tidak menyentuh jaringan sama sekali.

Uji ini sengaja TIDAK menghitung ulang hasil dengan `quote`, sebab itu hanya
akan menyalin implementasi. Yang diperiksa adalah sifat yang harus benar apa pun
implementasinya: hasil ASCII murni, aksara mentah tidak bocor ke URL, dan nama
aslinya pulih utuh saat di-unquote.
"""
from urllib.parse import unquote

from lux_ai.serapan.arsip import AKAR, CDN, segmen, url_funding, url_klines

# Kasus POSITIF: ditemukan di indeks arsip, memikul 19 berkas-bulan (jurnal 25).
NON_ASCII = ("\u5e01\u5b89\u4eba\u751fUSDT", "\u6211\u8e0f\u9a6c\u6765\u4e86USDT", "\u9f99\u867eUSDT")
# Kasus NEGATIF: nama biasa yang harus lewat tanpa perubahan.
ASCII_KONTROL = ("BTCUSDT", "ADAUSDT", "1000SHIBUSDT")


def test_segmen_mengubah_nama_non_ascii():
    for nama in NON_ASCII:
        hasil = segmen(nama)
        assert hasil.isascii(), nama
        assert "%" in hasil, nama
        assert unquote(hasil) == nama, nama


def test_segmen_membiarkan_nama_ascii_apa_adanya():
    for nama in ASCII_KONTROL:
        assert segmen(nama) == nama, nama


def test_segmen_mengencode_pemisah_path():
    # safe="" wajib: satu nama yang memuat "/" tidak boleh memecah path arsip.
    assert segmen("A/B") == "A%2FB"
    assert segmen("../rahasia") == "..%2Frahasia"


def test_url_klines_tidak_membocorkan_aksara_mentah():
    for nama in NON_ASCII:
        url = url_klines(nama, "1m", "2024-05")
        assert url.isascii(), nama
        assert nama not in url, nama
        assert url.startswith(f"{CDN}/{AKAR}/monthly/klines/"), nama
        assert url.endswith("-1m-2024-05.zip"), nama
        # Nama muncul dua kali: sebagai folder dan di dalam nama berkas.
        assert unquote(url).count(nama) == 2, nama


def test_url_funding_tidak_membocorkan_aksara_mentah():
    for nama in NON_ASCII:
        url = url_funding(nama, "2024-05")
        assert url.isascii(), nama
        assert nama not in url, nama
        assert url.startswith(f"{CDN}/{AKAR}/monthly/fundingRate/"), nama
        assert url.endswith("-fundingRate-2024-05.zip"), nama
        assert unquote(url).count(nama) == 2, nama


def test_url_nama_ascii_tetap_persis_sama():
    assert url_klines("BTCUSDT", "1m", "2020-01") == (
        f"{CDN}/{AKAR}/monthly/klines/BTCUSDT/1m/BTCUSDT-1m-2020-01.zip"
    )
    assert url_funding("BTCUSDT", "2020-01") == (
        f"{CDN}/{AKAR}/monthly/fundingRate/BTCUSDT/BTCUSDT-fundingRate-2020-01.zip"
    )
