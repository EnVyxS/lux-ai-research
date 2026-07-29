"""Uji bentangan_kohort V1.

Butir bernomor, tanpa parametrize (aturan 54/56/57). Seluruh butir bekerja atas
data sintetis; tidak ada butir yang menuntut laporan nyata.
"""

from lux_ai.serapan import bentangan_kohort as bk
from lux_ai.serapan import kehidupan

H = kehidupan.STATUS_HIDUP
M = kehidupan.STATUS_MATI
S = kehidupan.STATUS_SEPI
T = kehidupan.STATUS_TAK_TERUKUR


# --- 1..6 pisah_kunci ---

def test_01_pisah_kunci_pemisah_pipa():
    assert bk.pisah_kunci("BNXUSDT|2022-04") == ("BNXUSDT", "2022-04")


def test_02_pisah_kunci_pemisah_garis_bawah():
    assert bk.pisah_kunci("BNXUSDT_2022-04") == ("BNXUSDT", "2022-04")


def test_03_pisah_kunci_pemisah_hubung():
    assert bk.pisah_kunci("LITUSDT-2025-12") == ("LITUSDT", "2025-12")


def test_04_pisah_kunci_tanpa_pemisah():
    assert bk.pisah_kunci("LITUSDT2025-12") == ("LITUSDT", "2025-12")


def test_05_pisah_kunci_nama_non_ascii():
    assert bk.pisah_kunci("\u5e01\u5b89\u4eba\u751fUSDT/2023-05") == (
        "\u5e01\u5b89\u4eba\u751fUSDT",
        "2023-05",
    )


def test_06_pisah_kunci_tolak_tanpa_bulan():
    assert bk.pisah_kunci("BTCUSDT") is None
    assert bk.pisah_kunci("2026-06") is None


# --- 7..9 kelompokkan ---

def test_07_kelompokkan_membentuk_peta_dua_tingkat():
    per, gagal = bk.kelompokkan({"AUSDT|2025-01": H, "AUSDT|2025-02": M, "BUSDT|2025-01": S})
    assert gagal == 0
    assert per == {"AUSDT": {"2025-01": H, "2025-02": M}, "BUSDT": {"2025-01": S}}


def test_08_kelompokkan_mencacah_kunci_gagal():
    per, gagal = bk.kelompokkan({"AUSDT|2025-01": H, "rusak": M})
    assert gagal == 1
    assert list(per) == ["AUSDT"]


def test_09_kelompokkan_peta_kosong():
    assert bk.kelompokkan({}) == ({}, 0)


# --- 10..12 bulan_berstatus ---

def test_10_bulan_berstatus_terurut():
    peta = {"2025-03": H, "2025-01": H, "2025-02": M}
    assert bk.bulan_berstatus(peta, H) == ["2025-01", "2025-03"]


def test_11_bulan_berstatus_kosong_bukan_galat():
    assert bk.bulan_berstatus({"2025-01": M}, H) == []


def test_12_bulan_berstatus_tak_terukur_terpisah():
    peta = {"2025-01": T, "2025-02": M}
    assert bk.bulan_berstatus(peta, T) == ["2025-01"]


# --- 13..17 mati_tersisip ---

def test_13_mati_tersisip_satu_sisipan():
    peta = {"2025-01": H, "2025-02": M, "2025-03": H}
    assert bk.mati_tersisip(peta) == 1


def test_14_mati_tersisip_ekor_bukan_sisipan():
    peta = {"2025-01": H, "2025-02": M, "2025-03": M}
    assert bk.mati_tersisip(peta) == 0


def test_15_mati_tersisip_sepi_tidak_mengapit():
    peta = {"2025-01": S, "2025-02": M, "2025-03": H}
    assert bk.mati_tersisip(peta) == 0


def test_16_mati_tersisip_dua_sisipan():
    peta = {"2025-01": H, "2025-02": M, "2025-03": H, "2025-04": M, "2025-05": H}
    assert bk.mati_tersisip(peta) == 2


def test_17_mati_tersisip_rentetan_dua_bulan_bukan_sisipan_tunggal():
    peta = {"2025-01": H, "2025-02": M, "2025-03": M, "2025-04": H}
    assert bk.mati_tersisip(peta) == 0


# --- 18..21 bangkit ---

def test_18_bangkit_hidup_sesudah_mati():
    peta = {"2025-01": H, "2025-02": M, "2025-03": M, "2025-04": H}
    assert bk.bangkit(peta) is True


def test_19_bangkit_tanpa_hidup_awal_bukan_kebangkitan():
    peta = {"2025-01": M, "2025-02": M, "2025-03": H}
    assert bk.bangkit(peta) is False


def test_20_bangkit_peralihan_bersih_false():
    peta = {"2025-01": H, "2025-02": H, "2025-03": M, "2025-04": M}
    assert bk.bangkit(peta) is False


def test_21_bangkit_peta_kosong_false():
    assert bk.bangkit({}) is False


# --- 22..24 rentetan_terpanjang ---

def test_22_rentetan_hidup_terpanjang():
    peta = {"2025-01": H, "2025-02": H, "2025-03": M, "2025-04": H}
    assert bk.rentetan_terpanjang(peta, H) == 2


def test_23_rentetan_mati_terpanjang():
    peta = {"2025-01": M, "2025-02": M, "2025-03": M, "2025-04": H}
    assert bk.rentetan_terpanjang(peta, M) == 3


def test_24_rentetan_nol_bila_status_absen():
    assert bk.rentetan_terpanjang({"2025-01": M}, H) == 0


# --- 25..29 ringkas_simbol ---

def test_25_ringkas_simbol_medan_dasar():
    peta = {"2025-01": H, "2025-02": M, "2025-03": H}
    r = bk.ringkas_simbol("AUSDT", peta, {}, {}, {})
    assert r["cacah_bulan_berlabel"] == 3
    assert r["bulan_hidup_pertama"] == "2025-01"
    assert r["bulan_hidup_terakhir"] == "2025-03"
    assert r["cacah_mati"] == 1


def test_26_ringkas_simbol_tanpa_label_bukan_nol_palsu():
    r = bk.ringkas_simbol("AUSDT", {}, {}, {}, {})
    assert r["cacah_bulan_berlabel"] == 0
    assert r["bulan_hidup_terakhir"] is None
    assert r["cacah_hidup_sesudah_tebing"] == 0


def test_27_ringkas_simbol_hidup_sesudah_tebing_terdeteksi():
    peta = {"2025-06": H, bk.TEBING: H}
    r = bk.ringkas_simbol("AUSDT", peta, {}, {}, {})
    assert r["cacah_hidup_sesudah_tebing"] == 1
    assert r["bulan_hidup_sesudah_tebing"] == [bk.TEBING]


def test_28_ringkas_simbol_byte_parquet_dijumlah():
    peta = {"2025-01": H, "2025-02": M}
    byte = {"AUSDT2025-01": 1000, "AUSDT2025-02": 500, "BUSDT2025-01": 99}
    r = bk.ringkas_simbol("AUSDT", peta, byte, {}, {})
    assert r["byte_parquet_total"] == 1500


def test_29_ringkas_simbol_lubang_funding_terurut():
    r = bk.ringkas_simbol("AUSDT", {"2025-01": H}, {}, {}, {"AUSDT": ["2025-09", "2025-08"]})
    assert r["lubang_funding"] == ["2025-08", "2025-09"]


# --- 30..35 uji_r301 ---

def _bentangan(simbol, hidup_sesudah=0, tersisip=0, bangkit=False):
    return {
        "simbol": simbol,
        "cacah_hidup_sesudah_tebing": hidup_sesudah,
        "cacah_mati_tersisip": tersisip,
        "bangkit": bangkit,
    }


def test_30_r301_butir_1_menang_bila_nol_hidup_sesudah_tebing():
    hasil = bk.uji_r301([_bentangan("A"), _bentangan("B")])
    assert hasil["butir_1"] is True


def test_31_r301_butir_1_kalah_bila_satu_masih_hidup():
    hasil = bk.uji_r301([_bentangan("A", hidup_sesudah=1), _bentangan("B")])
    assert hasil["butir_1"] is False
    assert hasil["simbol_hidup_sesudah_tebing"] == ["A"]


def test_32_r301_butir_2_menang_bila_ada_sisipan():
    hasil = bk.uji_r301([_bentangan("A", tersisip=2)])
    assert hasil["butir_2"] is True
    assert hasil["pembatal_a008_menyala"] is True


def test_33_r301_butir_2_kalah_bila_tanpa_sisipan():
    hasil = bk.uji_r301([_bentangan("A"), _bentangan("B")])
    assert hasil["butir_2"] is False
    assert hasil["pembatal_a008_menyala"] is False


def test_34_r301_butir_3_kalah_bila_ada_kebangkitan():
    hasil = bk.uji_r301([_bentangan("A", bangkit=True)])
    assert hasil["butir_3"] is False
    assert hasil["simbol_bangkit"] == ["A"]


def test_35_r301_cacah_butir_menang_dijumlah_benar():
    hasil = bk.uji_r301([_bentangan("A", tersisip=1)])
    assert hasil["cacah_butir_menang"] == 3
    hasil2 = bk.uji_r301([_bentangan("A")])
    assert hasil2["cacah_butir_menang"] == 2


# --- 36..38 kendali_positif ---

def test_36_kendali_positif_sah():
    per = {s: {bk.BULAN_DIHARAPKAN: H} for s in bk.KENDALI_HIDUP}
    assert bk.kendali_positif(per)["kendali_sah"] is True


def test_37_kendali_positif_gagal_bila_mati():
    per = {s: {bk.BULAN_DIHARAPKAN: M} for s in bk.KENDALI_HIDUP}
    assert bk.kendali_positif(per)["kendali_sah"] is False


def test_38_kendali_positif_gagal_bila_absen():
    assert bk.kendali_positif({})["kendali_sah"] is False


# --- 39..44 kode_keluar dan tetapan ---

def _ringkasan(**ganti):
    dasar = {
        "galat_kohort": None,
        "kendali_sah": True,
        "penyebut_kehidupan": 19586,
        "cacah_kunci_gagal_pisah": 0,
        "cacah_simbol_kohort": 38,
    }
    dasar.update(ganti)
    return dasar


def test_39_kode_keluar_nol_bila_sah():
    assert bk.kode_keluar(_ringkasan()) == 0


def test_40_kode_keluar_dua_bila_galat_kohort():
    assert bk.kode_keluar(_ringkasan(galat_kohort="laporan hilang")) == 2


def test_41_kode_keluar_dua_bila_kendali_gagal():
    assert bk.kode_keluar(_ringkasan(kendali_sah=False)) == 2


def test_42_kode_keluar_dua_bila_kunci_gagal_pisah():
    assert bk.kode_keluar(_ringkasan(cacah_kunci_gagal_pisah=3)) == 2


def test_43_kode_keluar_dua_bila_kohort_kosong():
    assert bk.kode_keluar(_ringkasan(cacah_simbol_kohort=0)) == 2


def test_44_tetapan_praregistrasi_tidak_bergeser():
    assert bk.VERSI == 1
    assert bk.TEBING == "2025-07"
    assert bk.R301_BUTIR_1_HIDUP_SESUDAH_TEBING == 0
    assert bk.R301_BUTIR_2_MINIMAL_SATU_TERSISIP == 1
    assert bk.R301_BUTIR_3_BANGKIT == 0


def test_45_modul_tidak_memuat_daftar_nama_kohort():
    """Aturan 73: daftar 38 nama wajib dibaca saat jalan, bukan tetapan."""
    import inspect

    sumber = inspect.getsource(bk)
    for nama in ("AGIXUSDT", "ALPACAUSDT", "WAVESUSDT", "XEMUSDT"):
        assert nama not in sumber
