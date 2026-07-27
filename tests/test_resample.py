"""Uji resample dan pembacaan teks. Murni, tanpa jaringan.

Setengah berkas ini menguji CARA MENGUKUR, bukan hanya hasilnya: pengukur impor
jaringan diuji dengan kasus positif dan negatif, sesuai aturan 12 di STATE.
"""
from __future__ import annotations

import ast
import io
import zipfile
from decimal import Decimal
from pathlib import Path

from lux_ai.serapan import klines
from lux_ai.serapan import resample as rs

AKAR = Path(__file__).resolve().parents[1]
MS = 60_000


def bar(waktu, o, h, l, c, volume="1", trades="2"):
    return {
        "open_time": waktu,
        "open": o,
        "high": h,
        "low": l,
        "close": c,
        "volume": volume,
        "close_time": waktu + 59_999,
        "quote_volume": "10",
        "trades": trades,
        "taker_buy_base": "0.5",
        "taker_buy_quote": "5",
    }


def zip_csv(teks: str) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("contoh.csv", teks)
    return buf.getvalue()


def modul_diimpor(sumber: str) -> set:
    """Kumpulkan modul yang benar-benar DIIMPOR, diukur lewat AST."""
    pohon = ast.parse(sumber)
    hasil = set()
    for simpul in ast.walk(pohon):
        if isinstance(simpul, ast.Import):
            hasil |= {a.name.split(".")[0] for a in simpul.names}
        elif isinstance(simpul, ast.ImportFrom) and simpul.level == 0 and simpul.module:
            hasil.add(simpul.module.split(".")[0])
    return hasil


def test_lima_bar_menjadi_satu_bar_5m():
    baris = [
        bar(0 * MS, "100", "105", "99", "101"),
        bar(1 * MS, "101", "110", "98", "102"),
        bar(2 * MS, "102", "103", "97", "103"),
        bar(3 * MS, "103", "104", "96", "104"),
        bar(4 * MS, "104", "106", "95", "105"),
    ]
    hasil = rs.resample(baris, 5)
    assert len(hasil) == 1
    satu = hasil[0]
    assert satu["open_time"] == 0
    assert satu["open"] == Decimal("100")
    assert satu["high"] == Decimal("110")
    assert satu["low"] == Decimal("95")
    assert satu["close"] == Decimal("105")
    assert satu["menit_terisi"] == 5
    assert satu["volume"] == Decimal("5")
    assert satu["trades"] == Decimal("10")


def test_ember_selaras_dengan_kelipatan_lima_menit():
    baris = [bar(4 * MS, "1", "1", "1", "1"), bar(5 * MS, "2", "2", "2", "2")]
    hasil = rs.resample(baris, 5)
    assert [b["open_time"] for b in hasil] == [0, 5 * MS]
    assert hasil[1]["open"] == Decimal("2")


def test_menit_hilang_tetap_menghasilkan_bar_dan_tercatat():
    baris = [bar(0, "1", "1", "1", "1"), bar(3 * MS, "2", "3", "0.5", "2")]
    hasil = rs.resample(baris, 5)
    assert len(hasil) == 1
    assert hasil[0]["menit_terisi"] == 2
    assert hasil[0]["high"] == Decimal("3")
    assert hasil[0]["low"] == Decimal("0.5")


def test_penjumlahan_volume_eksak_bukan_float():
    baris = [
        bar(0, "1", "1", "1", "1", volume="0.1"),
        bar(MS, "1", "1", "1", "1", volume="0.2"),
    ]
    hasil = rs.resample(baris, 5)
    assert hasil[0]["volume"] == Decimal("0.3")
    assert str(hasil[0]["volume"]) == "0.3"


def test_urutan_masukan_tidak_mengubah_hasil():
    baris = [
        bar(2 * MS, "3", "3", "3", "3"),
        bar(0, "1", "5", "0", "2"),
        bar(1 * MS, "2", "2", "2", "2"),
    ]
    hasil = rs.resample(baris, 5)
    assert hasil[0]["open"] == Decimal("1")
    assert hasil[0]["close"] == Decimal("3")
    assert hasil[0]["high"] == Decimal("5")


def test_bandingkan_menemukan_kolom_yang_berbeda():
    hasil = rs.resample([bar(0, "1", "2", "0.5", "1.5")], 5)
    asli = [bar(0, "1", "9", "0.5", "1.5")]
    banding = rs.bandingkan(hasil, asli)
    assert banding["beda_per_kolom"]["high"] == 1
    assert banding["beda_per_kolom"]["open"] == 0
    assert banding["contoh_beda"][0]["kolom"] == "high"
    assert banding["contoh_beda"][0]["asli"] == "9"


def test_bandingkan_menghitung_bar_yang_hanya_ada_di_satu_sisi():
    hasil = rs.resample([bar(0, "1", "1", "1", "1")], 5)
    asli = [bar(5 * MS, "1", "1", "1", "1")]
    banding = rs.bandingkan(hasil, asli)
    assert banding["bar_cocok_waktu"] == 0
    assert banding["jumlah_hanya_di_resample"] == 1
    assert banding["jumlah_hanya_di_asli"] == 1


def test_baca_zip_teks_mempertahankan_desimal_apa_adanya():
    baris = (
        "0,100.10000000,100.20000000,100.00000000,100.15000000,0.10000000,"
        "59999,10.50000000,2,0.05000000,5.25000000,0\n"
    )
    df = klines.baca_zip(zip_csv(baris), teks=True)
    assert df.loc[0, "open"] == "100.10000000"
    rapi, dibuang = klines.rapikan(df)
    assert dibuang == 0
    assert rapi.loc[0, "volume"] == "0.10000000"
    assert "ignore" not in rapi.columns


def test_baris_pertama_membedakan_header_dari_data():
    berheader = (
        "open_time,open,high,low,close,volume,close_time,quote_volume,"
        "trades,taker_buy_base,taker_buy_quote,ignore\n"
        "0,1,1,1,1,1,59999,1,1,1,1,0\n"
    )
    tanpa = "0,1,1,1,1,1,59999,1,1,1,1,0\n"
    assert klines.punya_header(klines.baris_pertama(zip_csv(berheader))) is True
    assert klines.punya_header(klines.baris_pertama(zip_csv(tanpa))) is False


def test_pengukur_impor_membedakan_impor_dari_sekadar_sebutan():
    assert "urllib" in modul_diimpor("import urllib.request\n")
    assert "urllib" in modul_diimpor("from urllib import request\n")
    assert "urllib" not in modul_diimpor('"""dilarang mengimpor urllib"""\nx = "urllib"\n')


def test_resample_tidak_mengimpor_jaringan():
    sumber = (AKAR / "lux_ai" / "serapan" / "resample.py").read_text(encoding="utf-8")
    assert not (modul_diimpor(sumber) & {"urllib", "http", "socket", "requests"})
