"""Uji lubang_awal V1 - butir BERNOMOR agar dapat dicacah tangan (aturan 54).

Seluruh butir menguji fungsi murni: tanpa jaringan, tanpa berkas laporan.
Bentangan buatan memakai nama simbol yang BUKAN nama pasar sungguhan (aturan 73).
"""

from __future__ import annotations

from pathlib import Path

from lux_ai.serapan import kehidupan, lubang_awal, silang_funding

M = kehidupan.STATUS_MATI
H = kehidupan.STATUS_HIDUP
S = kehidupan.STATUS_SEPI

AWAL = {"2024-01": H, "2024-02": H, "2024-03": M, "2024-04": H}
LUB_AWAL = {"2024-01", "2024-02"}

BUKAN = {"2024-01": H, "2024-02": M, "2024-03": M, "2024-04": H}
LUB_BUKAN = {"2024-03"}

BUKAN_MATI_AKHIR = {"2024-01": H, "2024-02": H, "2024-03": M}
LUB_BUKAN_MATI_AKHIR = {"2024-02"}

SELURUH = {"2024-01": M, "2024-02": M}
LUB_SELURUH = {"2024-01", "2024-02"}


def _ringkasan_sah():
    return {
        "sidik_seragam": True,
        "cacah_laporan_dibaca": lubang_awal.TOTAL_PECAHAN,
        "total_pecahan": lubang_awal.TOTAL_PECAHAN,
        "cacah_kunci_ganda": 0,
        "kendali_sah": True,
        "kendali_deteksi_sah": True,
        "selisih_penyebut": 0,
        "selisih_simbol": 0,
        "selisih_mati": 0,
        "selisih_bangkit": 0,
        "selisih_lubang_dalam_penyebut": 0,
        "selisih_lubang_semesta": 0,
    }


def test_01_versi():
    assert lubang_awal.VERSI == 1


def test_02_nama_keluaran():
    assert lubang_awal.nama_keluaran() == "reports/lubang_awal.json"


def test_03_sidik_kode_bentuk():
    sidik = lubang_awal.sidik_kode()
    assert len(sidik) == 64 and set(sidik) <= set("0123456789abcdef")


def test_04_sidik_kode_stabil():
    assert lubang_awal.sidik_kode() == lubang_awal.sidik_kode()


def test_05_berkas_dicap_urut_dan_lengkap():
    assert lubang_awal.BERKAS_DICAP == sorted(lubang_awal.BERKAS_DICAP)
    assert "lubang_awal.py" in lubang_awal.BERKAS_DICAP
    assert "silang_funding.py" in lubang_awal.BERKAS_DICAP


def test_06_berkas_dicap_semuanya_ada():
    dasar = Path(lubang_awal.__file__).parent
    for nama in lubang_awal.BERKAS_DICAP:
        assert (dasar / nama).exists()


def test_07_pita_praregistrasi_tidak_berubah():
    assert lubang_awal.R305_PITA_BUTIR_1 == (0.55, 0.95)
    assert lubang_awal.R305_MINIMAL_PENYEBUT_BUTIR_1 == 100
    assert lubang_awal.R305_PITA_BUTIR_2_CACAH == (20, 120)
    assert lubang_awal.R305_MINIMAL_BAGIAN_BUTIR_2 == 0.80


def test_08_angka_tercatat():
    assert lubang_awal.PENYEBUT_TERCATAT == 19586
    assert lubang_awal.SIMBOL_TERCATAT == 787
    assert lubang_awal.MATI_TERCATAT == 1401
    assert lubang_awal.BANGKIT_TERCATAT == 8
    assert lubang_awal.LUBANG_DALAM_PENYEBUT_TERCATAT == 877
    assert lubang_awal.LUBANG_SEMESTA_TERCATAT == 880


def test_09_bulan_urut_membuang_bukan_bulan():
    assert lubang_awal.bulan_urut({"2024-02": H, "2024-01": M, "sampah": H}) == [
        "2024-01",
        "2024-02",
    ]


def test_10_bangkit_lokal_benar():
    assert lubang_awal.bangkit_lokal({"2024-01": H, "2024-02": M, "2024-03": H}) is True


def test_11_bangkit_lokal_salah_tanpa_mati():
    assert lubang_awal.bangkit_lokal({"2024-01": H, "2024-02": H}) is False


def test_12_bangkit_lokal_salah_mati_ekor():
    assert (
        lubang_awal.bangkit_lokal({"2024-01": H, "2024-02": M, "2024-03": M}) is False
    )


def test_13_ringkas_awal_bentuk():
    r = lubang_awal.ringkas("A", AWAL, LUB_AWAL)
    assert r["cacah_lubang_awal"] == 2
    assert r["cacah_lubang_bukan_awal"] == 0


def test_14_ringkas_awal_bulan_pertama_berlubang():
    assert lubang_awal.ringkas("A", AWAL, LUB_AWAL)["bulan_pertama_berlubang"] is True


def test_15_ringkas_awal_akhir_lubang_awal():
    assert lubang_awal.ringkas("A", AWAL, LUB_AWAL)["akhir_lubang_awal"] == "2024-02"


def test_16_ringkas_awal_berakhir_sebelum_mati():
    assert (
        lubang_awal.ringkas("A", AWAL, LUB_AWAL)["lubang_awal_berakhir_sebelum_mati"]
        is True
    )


def test_17_ringkas_awal_tidak_masuk_penyebut_1():
    assert lubang_awal.ringkas("A", AWAL, LUB_AWAL)["masuk_penyebut_butir_1"] is False


def test_18_ringkas_bukan_awal_bentuk():
    r = lubang_awal.ringkas("A", BUKAN, LUB_BUKAN)
    assert r["cacah_lubang_bukan_awal"] == 1
    assert r["cacah_lubang_awal"] == 0


def test_19_ringkas_bukan_awal_bulan_pertama_tidak_berlubang():
    assert (
        lubang_awal.ringkas("A", BUKAN, LUB_BUKAN)["bulan_pertama_berlubang"] is False
    )


def test_20_ringkas_bukan_awal_masuk_penyebut_1():
    assert lubang_awal.ringkas("A", BUKAN, LUB_BUKAN)["masuk_penyebut_butir_1"] is True


def test_21_ringkas_bukan_awal_mati_tidak_setelah_true():
    assert (
        lubang_awal.ringkas("A", BUKAN, LUB_BUKAN)[
            "mati_tidak_setelah_lubang_bukan_awal"
        ]
        is True
    )


def test_22_ringkas_bukan_awal_mati_setelah_false():
    r = lubang_awal.ringkas("A", BUKAN_MATI_AKHIR, LUB_BUKAN_MATI_AKHIR)
    assert r["mati_tidak_setelah_lubang_bukan_awal"] is False
    assert r["masuk_penyebut_butir_1"] is True


def test_23_ringkas_tanpa_lubang():
    r = lubang_awal.ringkas("A", AWAL, set())
    assert r["cacah_lubang"] == 0
    assert r["masuk_penyebut_butir_1"] is False
    assert r["bulan_pertama_berlubang"] is False


def test_24_ringkas_seluruh_dihitung_awal():
    r = lubang_awal.ringkas("A", SELURUH, LUB_SELURUH)
    assert r["cacah_lubang_awal"] == 2
    assert r["cacah_lubang_bukan_awal"] == 0


def test_25_himpun_penyebut_butir_1():
    baris = [
        lubang_awal.ringkas("A", BUKAN, LUB_BUKAN),
        lubang_awal.ringkas("B", BUKAN_MATI_AKHIR, LUB_BUKAN_MATI_AKHIR),
        lubang_awal.ringkas("C", AWAL, LUB_AWAL),
    ]
    ag = lubang_awal.himpun(baris)
    assert ag["penyebut_butir_1"] == 2
    assert ag["numerator_butir_1"] == 1


def test_26_himpun_bagian_butir_1():
    baris = [
        lubang_awal.ringkas("A", BUKAN, LUB_BUKAN),
        lubang_awal.ringkas("B", BUKAN_MATI_AKHIR, LUB_BUKAN_MATI_AKHIR),
    ]
    assert lubang_awal.himpun(baris)["bagian_butir_1"] == 0.5


def test_27_himpun_penyebut_butir_2():
    baris = [
        lubang_awal.ringkas("A", AWAL, LUB_AWAL),
        lubang_awal.ringkas("B", SELURUH, LUB_SELURUH),
        lubang_awal.ringkas("C", BUKAN, LUB_BUKAN),
    ]
    ag = lubang_awal.himpun(baris)
    assert ag["penyebut_butir_2"] == 2
    assert ag["numerator_butir_2"] == 1
    assert ag["bagian_butir_2"] == 0.5


def test_28_himpun_cacah_bangkit():
    baris = [
        lubang_awal.ringkas("A", AWAL, LUB_AWAL),
        lubang_awal.ringkas("B", SELURUH, LUB_SELURUH),
    ]
    assert lubang_awal.himpun(baris)["cacah_bangkit"] == 1


def test_29_dalam_pita_inklusif():
    assert lubang_awal.dalam_pita(0.55, (0.55, 0.95)) is True
    assert lubang_awal.dalam_pita(0.95, (0.55, 0.95)) is True
    assert lubang_awal.dalam_pita(0.54, (0.55, 0.95)) is False
    assert lubang_awal.dalam_pita(None, (0.55, 0.95)) is False


def test_30_kendali_deteksi_sah():
    assert lubang_awal.kendali_deteksi()["kendali_deteksi_sah"] is True


def test_31_kendali_deteksi_dua_baris():
    baris = lubang_awal.kendali_deteksi()["baris_kendali_deteksi"]
    assert len(baris) == 2
    assert baris[0]["bulan_pertama_berlubang"] is True
    assert baris[1]["masuk_penyebut_butir_1"] is True


def test_32_uji_r305_butir_1_menang():
    ag = {
        "penyebut_butir_1": 120,
        "bagian_butir_1": 0.7,
        "penyebut_butir_2": 50,
        "bagian_butir_2": 0.9,
    }
    assert lubang_awal.uji_r305(ag, _ringkasan_sah())["butir_1"] == "MENANG"


def test_33_uji_r305_butir_1_tidak_teradjudikasi():
    ag = {"penyebut_butir_1": 50, "bagian_butir_1": 0.7}
    assert (
        lubang_awal.uji_r305(ag, _ringkasan_sah())["butir_1"] == "TIDAK_TERADJUDIKASI"
    )


def test_34_uji_r305_butir_1_kalah():
    ag = {"penyebut_butir_1": 120, "bagian_butir_1": 0.3}
    assert lubang_awal.uji_r305(ag, _ringkasan_sah())["butir_1"] == "KALAH"


def test_35_uji_r305_butir_2_menang():
    ag = {"penyebut_butir_2": 50, "bagian_butir_2": 0.9}
    assert lubang_awal.uji_r305(ag, _ringkasan_sah())["butir_2"] == "MENANG"


def test_36_uji_r305_butir_2_kalah_luar_pita():
    ag = {"penyebut_butir_2": 10, "bagian_butir_2": 0.9}
    assert lubang_awal.uji_r305(ag, _ringkasan_sah())["butir_2"] == "KALAH"


def test_37_uji_r305_butir_2_kalah_bagian():
    ag = {"penyebut_butir_2": 50, "bagian_butir_2": 0.5}
    assert lubang_awal.uji_r305(ag, _ringkasan_sah())["butir_2"] == "KALAH"


def test_38_uji_r305_butir_3_menuntut_kendali():
    ag = {"penyebut_butir_1": 120, "bagian_butir_1": 0.7, "penyebut_butir_2": 50, "bagian_butir_2": 0.9}
    assert lubang_awal.uji_r305(ag, _ringkasan_sah())["butir_3"] is True
    r = _ringkasan_sah()
    r["kendali_deteksi_sah"] = False
    assert lubang_awal.uji_r305(ag, r)["butir_3"] is False


def test_39_kode_keluar_nol():
    assert lubang_awal.kode_keluar(_ringkasan_sah()) == 0


def test_40_kode_keluar_dua_sidik():
    r = _ringkasan_sah()
    r["sidik_seragam"] = False
    assert lubang_awal.kode_keluar(r) == 2


def test_41_kode_keluar_dua_laporan_kurang():
    r = _ringkasan_sah()
    r["cacah_laporan_dibaca"] = lubang_awal.TOTAL_PECAHAN - 1
    assert lubang_awal.kode_keluar(r) == 2


def test_42_kode_keluar_dua_kunci_ganda():
    r = _ringkasan_sah()
    r["cacah_kunci_ganda"] = 1
    assert lubang_awal.kode_keluar(r) == 2


def test_43_kode_keluar_dua_kendali_data():
    r = _ringkasan_sah()
    r["kendali_sah"] = False
    assert lubang_awal.kode_keluar(r) == 2


def test_44_kode_keluar_dua_kendali_detektor():
    r = _ringkasan_sah()
    r["kendali_deteksi_sah"] = False
    assert lubang_awal.kode_keluar(r) == 2


def test_45_kode_keluar_dua_tiap_selisih():
    for medan in (
        "selisih_penyebut",
        "selisih_simbol",
        "selisih_mati",
        "selisih_bangkit",
        "selisih_lubang_dalam_penyebut",
        "selisih_lubang_semesta",
    ):
        r = _ringkasan_sah()
        r[medan] = 1
        assert lubang_awal.kode_keluar(r) == 2, medan


def test_46_modul_tidak_memuat_nama_pasar():
    sumber = Path(lubang_awal.__file__).read_text(encoding="utf-8")
    assert "USDT" not in sumber


def test_47_batas_baris_laporan():
    assert lubang_awal.BATAS_BARIS_LAPORAN >= 1


def test_48_bentuk_lubang_lokal_dari_silang():
    assert (
        silang_funding.bentuk_lubang_lokal(["2024-01", "2024-02"], {"2024-01"}, "2024-01")
        == "awal"
    )
    assert (
        silang_funding.bentuk_lubang_lokal(
            ["2024-01", "2024-02"], {"2024-01", "2024-02"}, "2024-01"
        )
        == "seluruh"
    )
