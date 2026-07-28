"""Uji CARA MENGUKUR diagnostik KC-6, bukan hasilnya (aturan 12).

Setiap fungsi di sini diberi kasus yang jawabannya sudah saya ketahui lebih
dulu, termasuk kasus yang HARUS membuat H1 gugur. Alat yang hanya diuji dengan
kasus yang mendukung dugaan saya tidak menguji apa pun.
"""
from __future__ import annotations

from decimal import Decimal

from lux_ai.serapan import diagnosa_kc6 as dk
from lux_ai.serapan import resample as rs

MENIT = rs.MS_MENIT


def bar(waktu, o, h, l, c, terisi):
    hasil = {
        "open_time": waktu,
        "close_time": waktu + 5 * MENIT - 1,
        "menit_terisi": terisi,
        "open": Decimal(o),
        "high": Decimal(h),
        "low": Decimal(l),
        "close": Decimal(c),
    }
    for kolom in rs.KOLOM_JUMLAH:
        hasil[kolom] = Decimal(0)
    return hasil


def mentah(waktu, o, h, l, c):
    hasil = {
        "open_time": waktu,
        "close_time": waktu + 5 * MENIT - 1,
        "open": o,
        "high": h,
        "low": l,
        "close": c,
    }
    for kolom in rs.KOLOM_JUMLAH:
        hasil[kolom] = "0"
    return hasil


def test_celah_menit_menghitung_duplikat_dan_menit_hilang():
    cap = [0, MENIT, MENIT, 4 * MENIT]
    ukur = dk.celah_menit(cap)
    assert ukur["baris"] == 4
    assert ukur["cap_unik"] == 3
    assert ukur["duplikat"] == 1
    assert ukur["slot_dalam_rentang"] == 5
    assert ukur["menit_hilang_dalam_rentang"] == 2
    assert ukur["jarak_bukan_60_detik"] == 1


def test_celah_menit_pada_deret_penuh_tidak_menemukan_celah():
    cap = [i * MENIT for i in range(60)]
    ukur = dk.celah_menit(cap)
    assert ukur["menit_hilang_dalam_rentang"] == 0
    assert ukur["duplikat"] == 0
    assert ukur["jarak_bukan_60_detik"] == 0
    assert ukur["cap_tidak_selaras_menit"] == 0


def test_celah_menit_kosong_tidak_menebak():
    ukur = dk.celah_menit([])
    assert ukur["menit_pertama"] is None
    assert ukur["menit_hilang_dalam_rentang"] == 0


def test_periksa_bucket_menandai_menit_pertama_yang_hilang():
    hasil = [bar(0, "10", "12", "10", "11", 4)]
    asli = [mentah(0, "9", "12", "9", "11")]
    ukur = dk.periksa_bucket(hasil, asli, cap_ada=[MENIT, 2 * MENIT], menit=5)
    assert ukur["bucket_open_beda"] == 1
    assert ukur["open_beda_menit_pertama_hilang"] == 1
    assert ukur["open_beda_menit_pertama_ada"] == 0
    assert ukur["beda_tak_terjelaskan_h1"] == 0


def test_periksa_bucket_mengabaikan_bucket_yang_cocok():
    hasil = [bar(0, "10", "12", "9", "11", 5)]
    asli = [mentah(0, "10", "12", "9", "11")]
    ukur = dk.periksa_bucket(hasil, asli, cap_ada=[0], menit=5)
    assert ukur["bucket_dibandingkan"] == 1
    assert ukur["bucket_ohlc_beda"] == 0
    assert ukur["beda_tak_terjelaskan_h1"] == 0


def test_periksa_bucket_mencatat_beda_yang_h1_tidak_bisa_jelaskan():
    hasil = [bar(0, "10", "12", "9", "11", 5)]
    asli = [mentah(0, "10.5", "12", "9", "11")]
    ukur = dk.periksa_bucket(hasil, asli, cap_ada=[0], menit=5)
    assert ukur["open_beda_menit_pertama_ada"] == 1
    assert ukur["open_beda_bucket_menit_penuh"] == 1
    assert ukur["beda_tak_terjelaskan_h1"] == 1
    assert ukur["contoh_tak_terjelaskan"][0]["kolom_beda"] == ["open"]


def test_persen_menolak_membagi_nol():
    assert dk.persen(0, 0) is None
    assert dk.persen(1, 4) == 25.0


def test_ringkas_menjumlahkan_lintas_bulan_dan_mendaftar_bulan_tanpa_celah():
    pengukuran = [
        {
            "simbol": "AAAUSDT",
            "bulan": "2020-01",
            "celah": {"menit_hilang_dalam_rentang": 0, "duplikat": 0},
            "5m": {
                "bucket_open_beda": 4,
                "open_beda_menit_pertama_hilang": 1,
                "bucket_ohlc_beda": 4,
                "beda_tak_terjelaskan_h1": 3,
            },
            "15m": {
                "bucket_open_beda": 0,
                "open_beda_menit_pertama_hilang": 0,
                "bucket_ohlc_beda": 0,
                "beda_tak_terjelaskan_h1": 0,
            },
        },
        {
            "simbol": "BBBUSDT",
            "bulan": "2020-02",
            "celah": {"menit_hilang_dalam_rentang": 7, "duplikat": 0},
            "5m": {
                "bucket_open_beda": 6,
                "open_beda_menit_pertama_hilang": 6,
                "bucket_ohlc_beda": 6,
                "beda_tak_terjelaskan_h1": 0,
            },
        },
        {"simbol": "CCCUSDT", "galat": "tidak ada bulan bersama"},
    ]
    hasil = dk.ringkas(pengukuran)
    assert hasil["bulan_diukur"] == 2
    assert hasil["bucket_open_beda_total"] == 10
    assert hasil["open_beda_menit_pertama_hilang_total"] == 7
    assert hasil["persen_terjelaskan_h1"] == 70.0
    assert hasil["beda_tak_terjelaskan_h1_total"] == 3
    assert hasil["bulan_tanpa_celah"] == [{"simbol": "AAAUSDT", "bulan": "2020-01"}]
    assert hasil["per_simbol"]["AAAUSDT"]["persen_terjelaskan_h1"] == 25.0
    assert hasil["per_simbol"]["BBBUSDT"]["persen_terjelaskan_h1"] == 100.0
