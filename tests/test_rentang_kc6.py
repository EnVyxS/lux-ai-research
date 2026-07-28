"""Uji modul rentang_kc6. Tanpa jaringan (aturan 14).

Yang diuji di sini bukan angka arsipnya, melainkan CARA memilih bulan dan CARA
mencacah. Pemilihan bulan yang salah akan membuat bulan kendali jatuh di dalam
rentang yang sedang diukur, dan cacah yang salah akan membuat laporan berbohong
tanpa satu pun galat.
"""
from __future__ import annotations

from lux_ai.serapan import rentang_kc6 as rk


def bulan_deret(n: int) -> list:
    keluar = []
    tahun, bulan = 2020, 1
    for _ in range(n):
        keluar.append(f"{tahun:04d}-{bulan:02d}")
        bulan += 1
        if bulan > 12:
            bulan = 1
            tahun += 1
    return keluar


def test_pilih_bulan_mengambil_k_bulan_pertama():
    deret = bulan_deret(24)
    pilih = rk.pilih_bulan(deret, k=6)
    assert pilih["awal"] == deret[:6]
    assert pilih["bulan_bersama"] == 24


def test_bulan_kendali_di_tengah_dan_di_luar_k():
    deret = bulan_deret(24)
    pilih = rk.pilih_bulan(deret, k=6)
    assert pilih["kendali"] == deret[12]
    assert pilih["kendali"] not in pilih["awal"]
    assert pilih["kendali"] != deret[-1]


def test_simbol_pendek_tidak_punya_bulan_kendali():
    deret = bulan_deret(7)
    pilih = rk.pilih_bulan(deret, k=6)
    assert pilih["kendali"] is None
    assert pilih["awal"] == deret[:6]


def test_bulan_kendali_tidak_pernah_bulan_terakhir():
    for n in range(rk.MIN_BULAN_KENDALI, 40):
        pilih = rk.pilih_bulan(bulan_deret(n), k=6)
        if pilih["kendali"] is not None:
            assert pilih["kendali"] != bulan_deret(n)[-1]
            assert pilih["kendali"] not in pilih["awal"]


def satuan(simbol, bulan, peran, indeks, beda5, beda15, hilang=0, duplikat=0):
    return {
        "simbol": simbol,
        "bulan": bulan,
        "peran": peran,
        "indeks_bulan": indeks,
        "celah": {"menit_hilang_dalam_rentang": hilang, "duplikat": duplikat},
        "5m": {"bucket_open_beda": beda5, "beda_tak_terjelaskan_h1": beda5},
        "15m": {"bucket_open_beda": beda15, "beda_tak_terjelaskan_h1": beda15},
    }


def test_beda_satuan_menjumlahkan_kedua_interval():
    assert rk.beda_satuan(satuan("X", "2020-01", "awal", 1, 3, 4)) == (7, 7)


def test_ringkas_memisahkan_awal_dan_kendali():
    pengukuran = [
        satuan("AAA", "2020-01", "awal", 1, 10, 5),
        satuan("AAA", "2020-06", "awal", 6, 0, 0),
        satuan("AAA", "2021-06", "kendali", 0, 0, 0),
    ]
    r = rk.ringkas_rentang(pengukuran)
    assert r["total_bucket_beda_awal"] == 15
    assert r["total_bucket_beda_kendali"] == 0
    assert r["simbol_reda_di_dalam_k"] == ["AAA"]
    assert r["simbol_masih_beda_di_bulan_terakhir_awal"] == []
    assert r["simbol_menurun"] == ["AAA"]


def test_medan_penggugur_selalu_hadir_walau_nol():
    r = rk.ringkas_rentang([satuan("AAA", "2020-01", "awal", 1, 0, 0)])
    for medan in (
        "menit_hilang_total",
        "duplikat_total",
        "total_bucket_beda_kendali",
        "simbol_kendali_beda",
    ):
        assert medan in r
    assert r["menit_hilang_total"] == 0
    assert r["simbol_kendali_beda"] == []


def test_kendali_yang_beda_tertangkap():
    pengukuran = [
        satuan("AAA", "2020-01", "awal", 1, 4, 0),
        satuan("AAA", "2021-06", "kendali", 0, 2, 1),
    ]
    r = rk.ringkas_rentang(pengukuran)
    assert r["simbol_kendali_beda"] == ["AAA"]
    assert r["total_bucket_beda_kendali"] == 3
    assert r["persen_kendali_atas_awal"] == 75.0


def test_celah_positif_terlaporkan():
    r = rk.ringkas_rentang(
        [satuan("AAA", "2020-01", "awal", 1, 0, 0, hilang=3, duplikat=2)]
    )
    assert r["menit_hilang_total"] == 3
    assert r["duplikat_total"] == 2


def test_galat_tidak_dihitung_sebagai_bulan_diukur():
    r = rk.ringkas_rentang(
        [
            satuan("AAA", "2020-01", "awal", 1, 1, 1),
            {"simbol": "BBB", "bulan": "2020-01", "galat": "unduhan gagal"},
        ]
    )
    assert r["bulan_diukur"] == 1
    assert len(r["galat"]) == 1
