"""Uji `anatomi_tengah` V1 — daftar BERNOMOR (aturan 54, 56, 57).

Tidak ada `parametrize` di berkas ini, sehingga cacah fungsi sama dengan cacah
butir. Seluruh uji berjalan atas data sintetis; tidak ada laporan yang dibaca dan
tidak ada jaringan yang disentuh.

1. versi modul adalah 1
2. nama keluaran menunjuk reports/anatomi_tengah.json
3. daftar simbol datang dari lubang_tengah.SIMBOL_TENGAH_TERCATAT
4. daftar simbol memuat dua nama
5. total pecahan diwarisi dari kehidupan_arsip
6. sumber funding diwarisi dari silang_funding
7. medan lilin diwarisi dari silang_funding
8. praregistrasi cacah bulan adalah 64 bagi kedua simbol
9. praregistrasi simbol dan bulan lubang adalah BTCSTUSDT 2022-01
10. praregistrasi tetangga adalah 2021-12 dan 2022-02
11. praregistrasi pita hidup adalah 8..30
12. berkas yang dicap sidik_kode berjumlah lima dan memuat modul ini sendiri
13. sidik_kode stabil pada dua pemanggilan
14. sidik_kode berupa 64 huruf heksadesimal
15. bulan_simbol mengembalikan bulan urut naik
16. bulan_simbol menyaring simbol lain
17. bentangan mengembalikan satu baris per bulan
18. bentangan memuat keenam medan yang dijanjikan
19. funding_ada true bila simbol-bulan bukan lubang
20. funding_ada false bila simbol-bulan adalah lubang
21. status_bulan mengembalikan None bila bulan di luar penyebut
22. tetangga_status membaca kedua sisi dan terukur true
23. tetangga_status pada bulan paling awal berbunyi terukur false
24. tetangga_status pada bulan paling akhir berbunyi terukur false
25. mati_tersisip mengenali MATI di antara dua HIDUP
26. mati_tersisip tidak menghitung bulan tepi
27. mati_tersisip kosong bila tetangganya MATI
28. rentetan_terpanjang menghitung rentetan MATI terpanjang
29. rentetan_terpanjang nol bila status itu tidak ada
30. ringkas_simbol melaporkan keempat kelas status walau nol
31. ringkas_simbol mencacah lubang funding dan byte parquet
32. uji_r300 butir 1 menang bila kedua cacah bulan 64
33. uji_r300 butir 1 kalah bila salah satu bukan 64
34. uji_r300 butir 2 menang bila kedua tetangga HIDUP
35. uji_r300 butir 2 kalah bila satu tetangga MATI
36. uji_r300 butir 2 tak terukur bila bulan lubang di luar penyebut
37. uji_r300 butir 3 menang di dalam pita dengan MATI melampaui HIDUP
38. uji_r300 butir 3 kalah bila cacah hidup di luar pita
39. uji_r300 butir 3 kalah bila MATI tidak melampaui HIDUP
40. pembatal_a008_menyala mengikuti butir 2 saja
41. butir 1 ditandai MUDAH sedangkan butir 2 dan 3 tidak
42. kode_keluar nol bila ringkasan sehat
43. kode_keluar dua bila sidik tidak seragam
44. kode_keluar dua bila laporan pecahan kurang
45. kode_keluar dua bila ada kunci ganda
46. kode_keluar dua bila kendali tidak sah
47. kode_keluar tidak memeriksa hasil R-300
"""

from lux_ai.serapan import anatomi_tengah as at
from lux_ai.serapan import kehidupan, kehidupan_arsip, lubang_tengah, silang_funding

HIDUP = kehidupan.STATUS_HIDUP
MATI = kehidupan.STATUS_MATI
SEPI = kehidupan.STATUS_SEPI


def _status_sederhana():
    return {
        ("AAAUSDT", "2021-11"): HIDUP,
        ("AAAUSDT", "2021-12"): HIDUP,
        ("AAAUSDT", "2022-01"): MATI,
        ("AAAUSDT", "2022-02"): HIDUP,
        ("AAAUSDT", "2022-03"): MATI,
        ("BBBUSDT", "2022-01"): HIDUP,
    }


def _ringkas_palsu(hidup, mati, cacah_bulan):
    return {
        "cacah_bulan": cacah_bulan,
        "cacah_hidup": hidup,
        "cacah_mati": mati,
    }


def _ringkasan_sehat():
    return {
        "sidik_seragam": True,
        "cacah_laporan_dibaca": at.TOTAL_PECAHAN,
        "total_pecahan": at.TOTAL_PECAHAN,
        "cacah_kunci_ganda": 0,
        "kendali_sah": True,
    }


def test_1_versi():
    assert at.VERSI == 1


def test_2_nama_keluaran():
    assert at.nama_keluaran() == "reports/anatomi_tengah.json"


def test_3_simbol_dari_lubang_tengah():
    assert at.SIMBOL == list(lubang_tengah.SIMBOL_TENGAH_TERCATAT)


def test_4_simbol_dua_nama():
    assert len(at.SIMBOL) == 2


def test_5_total_pecahan_diwarisi():
    assert at.TOTAL_PECAHAN == kehidupan_arsip.TOTAL_PECAHAN


def test_6_sumber_funding_diwarisi():
    assert at.SUMBER_FUNDING == silang_funding.SUMBER_FUNDING


def test_7_medan_lilin_diwarisi():
    assert at.MEDAN_LILIN == silang_funding.MEDAN_LILIN


def test_8_praregistrasi_cacah_bulan():
    assert at.R300_BULAN_TERCATAT == {"BTCSTUSDT": 64, "LITUSDT": 64}


def test_9_praregistrasi_lubang():
    assert at.R300_SIMBOL_LUBANG == "BTCSTUSDT"
    assert at.R300_BULAN_LUBANG == "2022-01"


def test_10_praregistrasi_tetangga():
    assert at.R300_TETANGGA == ("2021-12", "2022-02")


def test_11_praregistrasi_pita():
    assert at.R300_PITA_HIDUP == (8, 30)


def test_12_berkas_dicap():
    assert len(at.BERKAS_DICAP) == 5
    assert "anatomi_tengah.py" in at.BERKAS_DICAP


def test_13_sidik_kode_stabil():
    assert at.sidik_kode() == at.sidik_kode()


def test_14_sidik_kode_heks():
    sidik = at.sidik_kode()
    assert len(sidik) == 64
    assert all(h in "0123456789abcdef" for h in sidik)


def test_15_bulan_simbol_urut():
    assert at.bulan_simbol(_status_sederhana(), "AAAUSDT") == [
        "2021-11",
        "2021-12",
        "2022-01",
        "2022-02",
        "2022-03",
    ]


def test_16_bulan_simbol_menyaring():
    assert at.bulan_simbol(_status_sederhana(), "BBBUSDT") == ["2022-01"]


def test_17_bentangan_satu_baris_per_bulan():
    baris = at.bentangan(_status_sederhana(), "AAAUSDT")
    assert len(baris) == 5


def test_18_bentangan_medan():
    baris = at.bentangan(_status_sederhana(), "AAAUSDT")[0]
    for medan in (
        "simbol",
        "bulan",
        "status",
        "byte_parquet",
        "cacah_lilin",
        "funding_ada",
    ):
        assert medan in baris


def test_19_funding_ada_true():
    baris = at.bentangan(_status_sederhana(), "AAAUSDT", lubang=set())
    assert all(r["funding_ada"] for r in baris)


def test_20_funding_ada_false_pada_lubang():
    lubang = {("AAAUSDT", "2022-01")}
    baris = at.bentangan(_status_sederhana(), "AAAUSDT", lubang=lubang)
    per_bulan = {r["bulan"]: r["funding_ada"] for r in baris}
    assert per_bulan["2022-01"] is False
    assert per_bulan["2021-12"] is True


def test_21_status_bulan_none():
    assert at.status_bulan(_status_sederhana(), "AAAUSDT", "2030-01") is None


def test_22_tetangga_dua_sisi():
    hasil = at.tetangga_status(_status_sederhana(), "AAAUSDT", "2022-01")
    assert hasil["status_sebelum"] == HIDUP
    assert hasil["status_sesudah"] == HIDUP
    assert hasil["terukur"] is True


def test_23_tetangga_ujung_awal():
    hasil = at.tetangga_status(_status_sederhana(), "AAAUSDT", "2021-11")
    assert hasil["bulan_sebelum"] is None
    assert hasil["terukur"] is False


def test_24_tetangga_ujung_akhir():
    hasil = at.tetangga_status(_status_sederhana(), "AAAUSDT", "2022-03")
    assert hasil["bulan_sesudah"] is None
    assert hasil["terukur"] is False


def test_25_mati_tersisip_dikenali():
    baris = at.bentangan(_status_sederhana(), "AAAUSDT")
    assert at.mati_tersisip(baris) == {"bulan": ["2022-01"], "cacah": 1}


def test_26_mati_tersisip_tanpa_tepi():
    baris = at.bentangan(_status_sederhana(), "AAAUSDT")
    assert "2022-03" not in at.mati_tersisip(baris)["bulan"]


def test_27_mati_tersisip_kosong():
    status = {
        ("CCCUSDT", "2022-01"): MATI,
        ("CCCUSDT", "2022-02"): MATI,
        ("CCCUSDT", "2022-03"): MATI,
    }
    baris = at.bentangan(status, "CCCUSDT")
    assert at.mati_tersisip(baris)["cacah"] == 0


def test_28_rentetan_mati():
    status = {
        ("DDDUSDT", "2022-01"): MATI,
        ("DDDUSDT", "2022-02"): MATI,
        ("DDDUSDT", "2022-03"): HIDUP,
        ("DDDUSDT", "2022-04"): MATI,
    }
    baris = at.bentangan(status, "DDDUSDT")
    assert at.rentetan_terpanjang(baris, MATI) == 2


def test_29_rentetan_nol():
    baris = at.bentangan(_status_sederhana(), "BBBUSDT")
    assert at.rentetan_terpanjang(baris, SEPI) == 0


def test_30_ringkas_empat_kelas():
    baris = at.bentangan(_status_sederhana(), "AAAUSDT")
    sebaran = at.ringkas_simbol(baris)["sebaran_status"]
    for nama in (HIDUP, MATI, SEPI, kehidupan.STATUS_TAK_TERUKUR):
        assert nama in sebaran


def test_31_ringkas_lubang_dan_byte():
    lubang = {("AAAUSDT", "2022-01")}
    byte_parquet = {("AAAUSDT", "2021-11"): 100, ("AAAUSDT", "2021-12"): 50}
    baris = at.bentangan(
        _status_sederhana(), "AAAUSDT", byte_parquet=byte_parquet, lubang=lubang
    )
    ringkas = at.ringkas_simbol(baris)
    assert ringkas["cacah_lubang_funding"] == 1
    assert ringkas["byte_parquet_total"] == 150


def test_32_butir1_menang():
    ringkas = {
        "BTCSTUSDT": _ringkas_palsu(10, 54, 64),
        "LITUSDT": _ringkas_palsu(20, 44, 64),
    }
    tetangga = {"terukur": True, "status_sebelum": HIDUP, "status_sesudah": HIDUP}
    assert at.uji_r300(ringkas, tetangga)["butir_1"]["menang"] is True


def test_33_butir1_kalah():
    ringkas = {
        "BTCSTUSDT": _ringkas_palsu(10, 54, 63),
        "LITUSDT": _ringkas_palsu(20, 44, 64),
    }
    tetangga = {"terukur": True, "status_sebelum": HIDUP, "status_sesudah": HIDUP}
    assert at.uji_r300(ringkas, tetangga)["butir_1"]["menang"] is False


def test_34_butir2_menang():
    ringkas = {
        "BTCSTUSDT": _ringkas_palsu(10, 54, 64),
        "LITUSDT": _ringkas_palsu(20, 44, 64),
    }
    tetangga = {"terukur": True, "status_sebelum": HIDUP, "status_sesudah": HIDUP}
    assert at.uji_r300(ringkas, tetangga)["butir_2"]["menang"] is True


def test_35_butir2_kalah():
    ringkas = {
        "BTCSTUSDT": _ringkas_palsu(10, 54, 64),
        "LITUSDT": _ringkas_palsu(20, 44, 64),
    }
    tetangga = {"terukur": True, "status_sebelum": MATI, "status_sesudah": HIDUP}
    assert at.uji_r300(ringkas, tetangga)["butir_2"]["menang"] is False


def test_36_butir2_tak_terukur():
    ringkas = {
        "BTCSTUSDT": _ringkas_palsu(10, 54, 64),
        "LITUSDT": _ringkas_palsu(20, 44, 64),
    }
    tetangga = {"terukur": False, "status_sebelum": None, "status_sesudah": None}
    hasil = at.uji_r300(ringkas, tetangga)
    assert hasil["butir_2"]["terukur"] is False
    assert hasil["butir_2"]["menang"] is False


def test_37_butir3_menang():
    ringkas = {
        "BTCSTUSDT": _ringkas_palsu(10, 54, 64),
        "LITUSDT": _ringkas_palsu(20, 44, 64),
    }
    tetangga = {"terukur": True, "status_sebelum": HIDUP, "status_sesudah": HIDUP}
    assert at.uji_r300(ringkas, tetangga)["butir_3"]["menang"] is True


def test_38_butir3_kalah_di_luar_pita():
    ringkas = {
        "BTCSTUSDT": _ringkas_palsu(2, 62, 64),
        "LITUSDT": _ringkas_palsu(20, 44, 64),
    }
    tetangga = {"terukur": True, "status_sebelum": HIDUP, "status_sesudah": HIDUP}
    hasil = at.uji_r300(ringkas, tetangga)
    assert hasil["butir_3"]["dalam_pita"] is False
    assert hasil["butir_3"]["menang"] is False


def test_39_butir3_kalah_mati_tak_melampaui():
    ringkas = {
        "BTCSTUSDT": _ringkas_palsu(30, 20, 64),
        "LITUSDT": _ringkas_palsu(20, 44, 64),
    }
    tetangga = {"terukur": True, "status_sebelum": HIDUP, "status_sesudah": HIDUP}
    hasil = at.uji_r300(ringkas, tetangga)
    assert hasil["butir_3"]["mati_melampaui_hidup"] is False
    assert hasil["butir_3"]["menang"] is False


def test_40_pembatal_mengikuti_butir2():
    ringkas = {
        "BTCSTUSDT": _ringkas_palsu(10, 54, 64),
        "LITUSDT": _ringkas_palsu(20, 44, 64),
    }
    menyala = at.uji_r300(
        ringkas,
        {"terukur": True, "status_sebelum": HIDUP, "status_sesudah": HIDUP},
    )
    mati = at.uji_r300(
        ringkas,
        {"terukur": True, "status_sebelum": MATI, "status_sesudah": MATI},
    )
    assert menyala["pembatal_a008_menyala"] is True
    assert mati["pembatal_a008_menyala"] is False


def test_41_penandaan_mudah():
    ringkas = {
        "BTCSTUSDT": _ringkas_palsu(10, 54, 64),
        "LITUSDT": _ringkas_palsu(20, 44, 64),
    }
    hasil = at.uji_r300(
        ringkas,
        {"terukur": True, "status_sebelum": HIDUP, "status_sesudah": HIDUP},
    )
    assert hasil["butir_1"]["mudah"] is True
    assert hasil["butir_2"]["mudah"] is False
    assert hasil["butir_3"]["mudah"] is False


def test_42_kode_keluar_nol():
    assert at.kode_keluar(_ringkasan_sehat()) == 0


def test_43_kode_dua_sidik():
    r = _ringkasan_sehat()
    r["sidik_seragam"] = False
    assert at.kode_keluar(r) == 2


def test_44_kode_dua_pecahan_kurang():
    r = _ringkasan_sehat()
    r["cacah_laporan_dibaca"] = at.TOTAL_PECAHAN - 1
    assert at.kode_keluar(r) == 2


def test_45_kode_dua_kunci_ganda():
    r = _ringkasan_sehat()
    r["cacah_kunci_ganda"] = 1
    assert at.kode_keluar(r) == 2


def test_46_kode_dua_kendali():
    r = _ringkasan_sehat()
    r["kendali_sah"] = False
    assert at.kode_keluar(r) == 2


def test_47_kode_tidak_memeriksa_r300():
    r = _ringkasan_sehat()
    r["r300_menang_seluruhnya"] = False
    r["r300_cacah_butir_menang"] = 0
    assert at.kode_keluar(r) == 0
