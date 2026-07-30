"""Uji sebab_bangkit V1 — butir BERNOMOR agar dapat dicacah tangan (aturan 54).

Seluruh butir menguji fungsi murni: tidak ada jaringan, tidak ada berkas
laporan. Bentangan buatan sengaja memakai nama simbol yang BUKAN nama pasar
sungguhan (aturan 73: nama turunan tidak boleh menyelinap menjadi tetapan).
"""

from __future__ import annotations

from pathlib import Path

from lux_ai.serapan import kehidupan, sebab_bangkit

M = kehidupan.STATUS_MATI
H = kehidupan.STATUS_HIDUP
S = kehidupan.STATUS_SEPI

BENTANGAN_BANGKIT = {
    "2024-01": H,
    "2024-02": H,
    "2024-03": M,
    "2024-04": M,
    "2024-05": H,
}


def test_01_versi():
    assert sebab_bangkit.VERSI == 1


def test_02_nama_keluaran():
    assert sebab_bangkit.nama_keluaran() == "reports/sebab_bangkit.json"


def test_03_sidik_kode_bentuk():
    sidik = sebab_bangkit.sidik_kode()
    assert len(sidik) == 64 and set(sidik) <= set("0123456789abcdef")


def test_04_sidik_kode_stabil():
    assert sebab_bangkit.sidik_kode() == sebab_bangkit.sidik_kode()


def test_05_berkas_dicap_urut_dan_lengkap():
    assert sebab_bangkit.BERKAS_DICAP == sorted(sebab_bangkit.BERKAS_DICAP)
    assert "sebab_bangkit.py" in sebab_bangkit.BERKAS_DICAP
    assert "silang_funding.py" in sebab_bangkit.BERKAS_DICAP


def test_06_berkas_dicap_semuanya_ada():
    dasar = Path(sebab_bangkit.__file__).parent
    for nama in sebab_bangkit.BERKAS_DICAP:
        assert (dasar / nama).exists()


def test_07_pita_praregistrasi_tidak_berubah():
    assert sebab_bangkit.R304_PITA_MATI_DULU == (5, 8)
    assert sebab_bangkit.R304_PITA_HIDUP_BERLUBANG == (3, 8)


def test_08_angka_tercatat():
    assert sebab_bangkit.PENYEBUT_TERCATAT == 19586
    assert sebab_bangkit.SIMBOL_TERCATAT == 787
    assert sebab_bangkit.MATI_TERCATAT == 1401
    assert sebab_bangkit.BANGKIT_TERCATAT == 8
    assert sebab_bangkit.TERSISIP_TERCATAT == 88
    assert sebab_bangkit.LUBANG_DALAM_PENYEBUT_TERCATAT == 877


def test_09_indeks_bulan_sah():
    assert sebab_bangkit.indeks_bulan("2024-01") == 2024 * 12


def test_10_indeks_bulan_desember():
    assert sebab_bangkit.indeks_bulan("2023-12") == 2023 * 12 + 11


def test_11_indeks_bulan_tolak_bentuk_lain():
    for buruk in (None, "", "2024", "2024-1", "2024-13-01", "abcd-ef"):
        assert sebab_bangkit.indeks_bulan(buruk) is None


def test_12_jarak_bulan_maju():
    assert sebab_bangkit.jarak_bulan("2024-01", "2025-01") == 12


def test_13_jarak_bulan_mundur():
    assert sebab_bangkit.jarak_bulan("2024-06", "2024-01") == -5


def test_14_jarak_bulan_nol():
    assert sebab_bangkit.jarak_bulan("2024-06", "2024-06") == 0


def test_15_jarak_bulan_null_bila_tak_sah():
    assert sebab_bangkit.jarak_bulan("2024-06", None) is None
    assert sebab_bangkit.jarak_bulan("buruk", "2024-06") is None


def test_16_peta_status_memecah_per_simbol():
    peta = sebab_bangkit.peta_status(
        {("AAA", "2024-01"): H, ("AAA", "2024-02"): M, ("BBB", "2024-01"): H}
    )
    assert set(peta) == {"AAA", "BBB"}
    assert peta["AAA"]["2024-02"] == M


def test_17_bulan_urut_membuang_bentuk_bukan_bulan():
    urut = sebab_bangkit.bulan_urut({"2024-02": H, "2024-01": M, "sampah": H})
    assert urut == ["2024-01", "2024-02"]


def test_18_bangkit_lokal_benar():
    assert sebab_bangkit.bangkit_lokal(BENTANGAN_BANGKIT) is True


def test_19_bangkit_lokal_salah_tanpa_mati():
    assert sebab_bangkit.bangkit_lokal({"2024-01": H, "2024-02": H}) is False


def test_20_bangkit_lokal_salah_bila_mati_di_ekor():
    assert (
        sebab_bangkit.bangkit_lokal({"2024-01": H, "2024-02": M, "2024-03": M})
        is False
    )


def test_21_bangkit_lokal_sepi_bukan_hidup():
    assert (
        sebab_bangkit.bangkit_lokal({"2024-01": H, "2024-02": M, "2024-03": S})
        is False
    )


def test_22_tersisip_lokal_mencacah_blok():
    assert sebab_bangkit.tersisip_lokal(BENTANGAN_BANGKIT) == [
        "2024-03",
        "2024-04",
    ]


def test_23_tersisip_lokal_kosong_bila_mati_di_ekor():
    assert sebab_bangkit.tersisip_lokal({"2024-01": H, "2024-02": M}) == []


def test_24_tersisip_lokal_kosong_tanpa_hidup():
    assert sebab_bangkit.tersisip_lokal({"2024-01": M, "2024-02": M}) == []


def test_25_ringkas_cacah_dasar():
    r = sebab_bangkit.ringkas("AAA", BENTANGAN_BANGKIT, set())
    assert r["cacah_bulan"] == 5
    assert r["cacah_mati"] == 2
    assert r["cacah_hidup"] == 3


def test_26_ringkas_bulan_tepi():
    r = sebab_bangkit.ringkas("AAA", BENTANGAN_BANGKIT, set())
    assert r["bulan_pertama"] == "2024-01"
    assert r["bulan_terakhir"] == "2024-05"
    assert r["bulan_mati_pertama"] == "2024-03"
    assert r["bulan_hidup_terakhir"] == "2024-05"


def test_27_ringkas_tanpa_lubang():
    r = sebab_bangkit.ringkas("AAA", BENTANGAN_BANGKIT, set())
    assert r["tanpa_lubang"] is True
    assert r["bulan_berlubang_pertama"] is None
    assert r["mati_dulu"] is False
    assert r["lubang_dulu"] is False
    assert r["selisih_bulan_mati_ke_lubang"] is None


def test_28_ringkas_mati_dulu():
    r = sebab_bangkit.ringkas("AAA", BENTANGAN_BANGKIT, {"2024-04", "2024-05"})
    assert r["mati_dulu"] is True
    assert r["lubang_dulu"] is False
    assert r["selisih_bulan_mati_ke_lubang"] == 1


def test_29_ringkas_lubang_dulu():
    r = sebab_bangkit.ringkas("AAA", BENTANGAN_BANGKIT, {"2024-01", "2024-02"})
    assert r["lubang_dulu"] is True
    assert r["mati_dulu"] is False
    assert r["selisih_bulan_mati_ke_lubang"] == -2


def test_30_ringkas_serentak():
    r = sebab_bangkit.ringkas("AAA", BENTANGAN_BANGKIT, {"2024-03"})
    assert r["serentak"] is True
    assert r["mati_dulu"] is False and r["lubang_dulu"] is False
    assert r["selisih_bulan_mati_ke_lubang"] == 0


def test_31_ringkas_hidup_berlubang():
    r = sebab_bangkit.ringkas("AAA", BENTANGAN_BANGKIT, {"2024-05"})
    assert r["cacah_hidup_berlubang"] == 1
    assert r["ada_hidup_berlubang"] is True
    assert r["cacah_mati_berlubang"] == 0


def test_32_ringkas_mati_berlubang():
    r = sebab_bangkit.ringkas("AAA", BENTANGAN_BANGKIT, {"2024-03", "2024-04"})
    assert r["cacah_mati_berlubang"] == 2
    assert r["ada_hidup_berlubang"] is False


def test_33_ringkas_lubang_di_luar_bentangan_diabaikan():
    r = sebab_bangkit.ringkas("AAA", BENTANGAN_BANGKIT, {"2030-01"})
    assert r["cacah_bulan_berlubang"] == 0
    assert r["tanpa_lubang"] is True


def test_34_ringkas_silang_tersisip_dua_jalan():
    r = sebab_bangkit.ringkas("AAA", BENTANGAN_BANGKIT, set())
    assert r["cacah_tersisip_lokal"] == 2
    assert isinstance(r["cacah_tersisip_alat"], int)
    assert r["tersisip_sepakat"] == (
        r["cacah_tersisip_lokal"] == r["cacah_tersisip_alat"]
    )


def test_35_ringkas_bangkit_ikut_terlapor():
    r = sebab_bangkit.ringkas("AAA", BENTANGAN_BANGKIT, set())
    assert r["bangkit"] is True


def test_36_ember_kelas():
    assert sebab_bangkit.ember(None) == "null"
    assert sebab_bangkit.ember(-1) == "<0"
    assert sebab_bangkit.ember(0) == "0"
    assert sebab_bangkit.ember(3) == "1-3"
    assert sebab_bangkit.ember(12) == "4-12"
    assert sebab_bangkit.ember(13) == "13+"


def test_37_himpun_cacah():
    baris = [
        sebab_bangkit.ringkas("AAA", BENTANGAN_BANGKIT, {"2024-04"}),
        sebab_bangkit.ringkas("BBB", BENTANGAN_BANGKIT, {"2024-01"}),
        sebab_bangkit.ringkas("CCC", BENTANGAN_BANGKIT, set()),
    ]
    ag = sebab_bangkit.himpun(baris)
    assert ag["cacah_simbol_bangkit"] == 3
    assert ag["cacah_mati_dulu"] == 1
    assert ag["cacah_lubang_dulu"] == 1
    assert ag["cacah_tanpa_lubang"] == 1


def test_38_himpun_tersisip_dijumlah():
    baris = [sebab_bangkit.ringkas("AAA", BENTANGAN_BANGKIT, set())] * 2
    assert sebab_bangkit.himpun(baris)["cacah_simbol_bulan_tersisip"] == 4


def test_39_himpun_sebaran_lengkap():
    ag = sebab_bangkit.himpun([])
    assert set(ag["sebaran_selisih_bulan"]) == {
        "null",
        "<0",
        "0",
        "1-3",
        "4-12",
        "13+",
    }
    assert sum(ag["sebaran_selisih_bulan"].values()) == 0


def test_40_himpun_hidup_berlubang():
    baris = [sebab_bangkit.ringkas("AAA", BENTANGAN_BANGKIT, {"2024-05"})]
    assert sebab_bangkit.himpun(baris)["cacah_simbol_hidup_berlubang"] == 1


def test_41_kendali_deteksi_sah():
    kd = sebab_bangkit.kendali_deteksi()
    assert kd["kendali_deteksi_sah"] is True


def test_42_kendali_deteksi_dua_arah():
    baris = sebab_bangkit.kendali_deteksi()["baris_kendali_deteksi"]
    assert len(baris) == 2
    assert baris[0]["mati_dulu"] is True
    assert baris[1]["lubang_dulu"] is True


def test_43_dalam_pita_inklusif():
    assert sebab_bangkit.dalam_pita(5, (5, 8)) is True
    assert sebab_bangkit.dalam_pita(8, (5, 8)) is True
    assert sebab_bangkit.dalam_pita(4, (5, 8)) is False
    assert sebab_bangkit.dalam_pita(9, (5, 8)) is False
    assert sebab_bangkit.dalam_pita(None, (5, 8)) is False


def _ringkasan_sah():
    return {
        "sidik_seragam": True,
        "cacah_laporan_dibaca": sebab_bangkit.TOTAL_PECAHAN,
        "total_pecahan": sebab_bangkit.TOTAL_PECAHAN,
        "cacah_kunci_ganda": 0,
        "kendali_sah": True,
        "kendali_deteksi_sah": True,
        "selisih_penyebut": 0,
        "selisih_simbol": 0,
        "selisih_mati": 0,
        "selisih_bangkit": 0,
        "selisih_tersisip": 0,
        "selisih_lubang_dalam_penyebut": 0,
    }


def test_44_uji_r304_butir_1_menang():
    hasil = sebab_bangkit.uji_r304({"cacah_mati_dulu": 6}, _ringkasan_sah())
    assert hasil["butir_1_mati_dulu_dalam_pita"] is True


def test_45_uji_r304_butir_1_kalah_pada_nol():
    hasil = sebab_bangkit.uji_r304({"cacah_mati_dulu": 0}, _ringkasan_sah())
    assert hasil["butir_1_mati_dulu_dalam_pita"] is False


def test_46_uji_r304_butir_2():
    hasil = sebab_bangkit.uji_r304(
        {"cacah_simbol_hidup_berlubang": 3}, _ringkasan_sah()
    )
    assert hasil["butir_2_hidup_berlubang_dalam_pita"] is True
    hasil2 = sebab_bangkit.uji_r304(
        {"cacah_simbol_hidup_berlubang": 2}, _ringkasan_sah()
    )
    assert hasil2["butir_2_hidup_berlubang_dalam_pita"] is False


def test_47_uji_r304_butir_3_menuntut_kendali():
    ringkasan = _ringkasan_sah()
    assert sebab_bangkit.uji_r304({}, ringkasan)["butir_3_mudah_cocok"] is True
    ringkasan["kendali_deteksi_sah"] = False
    assert sebab_bangkit.uji_r304({}, ringkasan)["butir_3_mudah_cocok"] is False


def test_48_uji_r304_butir_3_disebut_mudah():
    hasil = sebab_bangkit.uji_r304({}, _ringkasan_sah())
    assert "MUDAH" in hasil["catatan_butir_3"]


def test_49_kode_keluar_nol_pada_laporan_sah():
    assert sebab_bangkit.kode_keluar(_ringkasan_sah()) == 0


def test_50_kode_keluar_dua_bila_sidik_tak_seragam():
    r = _ringkasan_sah()
    r["sidik_seragam"] = False
    assert sebab_bangkit.kode_keluar(r) == 2


def test_51_kode_keluar_dua_bila_laporan_kurang():
    r = _ringkasan_sah()
    r["cacah_laporan_dibaca"] = sebab_bangkit.TOTAL_PECAHAN - 1
    assert sebab_bangkit.kode_keluar(r) == 2


def test_52_kode_keluar_dua_bila_kunci_ganda():
    r = _ringkasan_sah()
    r["cacah_kunci_ganda"] = 1
    assert sebab_bangkit.kode_keluar(r) == 2


def test_53_kode_keluar_dua_bila_kendali_data_gagal():
    r = _ringkasan_sah()
    r["kendali_sah"] = False
    assert sebab_bangkit.kode_keluar(r) == 2


def test_54_kode_keluar_dua_bila_kendali_detektor_gagal():
    r = _ringkasan_sah()
    r["kendali_deteksi_sah"] = False
    assert sebab_bangkit.kode_keluar(r) == 2


def test_55_kode_keluar_dua_pada_tiap_selisih():
    for medan in (
        "selisih_penyebut",
        "selisih_simbol",
        "selisih_mati",
        "selisih_bangkit",
        "selisih_tersisip",
        "selisih_lubang_dalam_penyebut",
    ):
        r = _ringkasan_sah()
        r[medan] = 1
        assert sebab_bangkit.kode_keluar(r) == 2, medan


def test_56_modul_tidak_memuat_nama_pasar():
    sumber = Path(sebab_bangkit.__file__).read_text(encoding="utf-8")
    assert "USDT" not in sumber


def test_57_batas_baris_laporan_cukup_untuk_delapan():
    assert sebab_bangkit.BATAS_BARIS_LAPORAN >= sebab_bangkit.BANGKIT_TERCATAT
