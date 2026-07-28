"""Uji murni atas klien arsip dan pembaca klines. Tidak menyentuh jaringan.

Uji jaringan tidak boleh ada di CI: kegagalan jaringan akan menyamar sebagai
kegagalan logika, dan CI yang merah karena sebab luar akan berhenti dipercaya.
"""
import io
import pathlib
import zipfile

import pandas as pd

from lux_ai.serapan import arsip, klines, probe, survei


def test_url_klines_memakai_prefix_data():
    u = arsip.url_klines("BTCUSDT", "1m", "2024-01")
    assert u == (
        "https://data.binance.vision/data/futures/um/monthly/klines/"
        "BTCUSDT/1m/BTCUSDT-1m-2024-01.zip"
    )


def test_url_menangani_simbol_non_ascii():
    u = arsip.url_klines("\u9f99\u867eUSDT", "1m", "2021-05")
    assert u.isascii(), "karakter non-ASCII harus dienkode"
    assert "%" in u


def test_url_funding_terpisah_dari_klines():
    u = arsip.url_funding("ETHUSDT", "2023-07")
    assert u.endswith("/fundingRate/ETHUSDT/ETHUSDT-fundingRate-2023-07.zip")


def test_deteksi_header_mengukur_isi():
    assert klines.punya_header("open_time,open,high,low,close,volume")
    assert not klines.punya_header("1704067200000,42000.0,42010.0,41990.0,42005.0,12.3")
    assert not klines.punya_header('"1704067200000",42000.0')


def _zip_csv(teks):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("BTCUSDT-1m-2024-01.csv", teks)
    return buf.getvalue()


BARIS = "{t},1,2,0.5,1.5,10,{c},100,5,4,40,0"


def test_baca_zip_tanpa_header_tidak_kehilangan_baris():
    isi = "\n".join(
        BARIS.format(t=1704067200000 + i * 60000, c=1704067259999 + i * 60000)
        for i in range(3)
    )
    df = klines.baca_zip(_zip_csv(isi))
    assert len(df) == 3
    assert list(df.columns)[:6] == klines.KOLOM[:6]


def test_baca_zip_dengan_header_tidak_menelan_header_sebagai_data():
    isi = ",".join(klines.KOLOM) + "\n" + BARIS.format(t=1704067200000, c=1704067259999)
    df = klines.baca_zip(_zip_csv(isi))
    assert len(df) == 1
    assert int(df["open_time"].iloc[0]) == 1704067200000


def test_rapikan_mengurutkan_dan_membuang_duplikat():
    df = pd.DataFrame(
        {
            "open_time": [300, 100, 200, 100],
            "open": [3.0, 1.0, 2.0, 1.0],
            "high": [3, 1, 2, 1],
            "low": [3, 1, 2, 1],
            "close": [3, 1, 2, 1],
            "volume": [1, 1, 1, 1],
            "close_time": [359, 159, 259, 159],
            "quote_volume": [1, 1, 1, 1],
            "trades": [1, 1, 1, 1],
            "taker_buy_base": [1, 1, 1, 1],
            "taker_buy_quote": [1, 1, 1, 1],
        }
    )
    rapi, dibuang = klines.rapikan(df)
    assert list(rapi["open_time"]) == [100, 200, 300]
    assert dibuang == 1


def test_semesta_simbol_tidak_menyaring_pair_aktif():
    """Penegakan anti bias keselamatan-hidup di level kode.

    Fungsi semesta hanya boleh membaca indeks arsip. Bila kelak ada yang
    menambahkan penyaringan status pair, uji ini memaksa perubahan itu disadari.
    """
    sumber = pathlib.Path(arsip.__file__).read_text(encoding="utf-8")
    potongan = sumber.split("def semesta_simbol", 1)[1].split("\ndef ", 1)[0]
    for terlarang in ("exchangeInfo", "fapi", "TRADING"):
        assert terlarang not in potongan


# --- KC-5: cara probe mengukur klaim delisting -------------------------------
# Aturan 12: yang diuji di sini adalah CARA MENGUKUR, dengan kasus positif
# (simbol yang memang berhenti) dan kasus negatif (simbol yang masih terbit
# padahal ada di daftar klaim).


def test_klaim_delisting_tidak_memakai_kehadiran_di_indeks():
    """Kasus yang menjatuhkan versi lama: FTTUSDT ada di indeks TAPI masih terbit."""
    baris = probe.nilai_klaim_delisting(
        ["FTTUSDT", "SRMUSDT"],
        {"FTTUSDT": "2026-06", "SRMUSDT": "2024-05"},
        "2026-06",
    )
    per_simbol = {b["simbol"]: b for b in baris}
    assert per_simbol["FTTUSDT"]["ada_di_indeks"] is True
    assert per_simbol["FTTUSDT"]["terhenti"] is False
    assert per_simbol["FTTUSDT"]["selisih_bulan"] == 0
    assert per_simbol["SRMUSDT"]["terhenti"] is True
    assert per_simbol["SRMUSDT"]["selisih_bulan"] == 25


def test_klaim_delisting_tanpa_bulan_terakhir_tidak_diputuskan():
    """Tanpa bulan terakhir tidak ada yang bisa diukur; jangan menebak."""
    (baris,) = probe.nilai_klaim_delisting(["HANTUUSDT"], {}, "2026-06")
    assert baris["ada_di_indeks"] is False
    assert baris["bulan_terakhir"] is None
    assert baris["selisih_bulan"] is None
    assert baris["terhenti"] is None


def test_klaim_delisting_memakai_definisi_tunggal_dari_survei():
    """Probe dilarang punya ambang delisting sendiri.

    Bila kelak ada yang menyalin ulang ambangnya ke probe.py dan mengubahnya,
    perbandingan ini akan gagal untuk salah satu jarak bulan.
    """
    bulan = ["2026-06", "2026-05", "2026-04", "2026-03", "2025-12", "2024-05"]
    baris = probe.nilai_klaim_delisting(
        [f"S{i}" for i in range(len(bulan))],
        {f"S{i}": b for i, b in enumerate(bulan)},
        "2026-06",
    )
    for b in baris:
        assert b["terhenti"] == survei.terhenti(b["bulan_terakhir"], "2026-06")
        assert b["selisih_bulan"] == survei.selisih_bulan(b["bulan_terakhir"], "2026-06")


def test_klaim_delisting_mencatat_bulan_acuannya():
    """Aturan 20: putusan tanpa rentang acuan tidak bisa ditafsirkan.

    Simbol yang sama bisa terhenti terhadap satu acuan dan hidup terhadap acuan
    lain, jadi acuannya wajib ikut tercatat di tiap baris.
    """
    (jauh,) = probe.nilai_klaim_delisting(["X"], {"X": "2024-05"}, "2026-06")
    (dekat,) = probe.nilai_klaim_delisting(["X"], {"X": "2024-05"}, "2024-05")
    assert jauh["bulan_acuan"] == "2026-06" and dekat["bulan_acuan"] == "2024-05"
    assert jauh["terhenti"] is True
    assert dekat["terhenti"] is False
