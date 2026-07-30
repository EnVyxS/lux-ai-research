"""Uji keterisian_lilin V1 — 64 butir bernomor, satu nama per nomor.

Aturan 57: cacah butir diramalkan SEBELUM push dengan DAFTAR bernomor, bukan
rentang. Rentang "56-62" adalah yang memutus beruntun pada giliran ke-27.
Tidak ada `parametrize` di berkas ini; setiap fungsi tepat satu butir.
"""

from __future__ import annotations

import pytest

from lux_ai.serapan import kehidupan
from lux_ai.serapan import keterisian_lilin as kl


def _ringkasan_sehat():
    return {
        "sidik_seragam": True,
        "cacah_laporan_dibaca": kl.TOTAL_PECAHAN,
        "total_pecahan": kl.TOTAL_PECAHAN,
        "cacah_kunci_ganda": 0,
        "selisih_invarian": {k: 0 for k in kl.INVARIAN},
        "cacah_defisit_negatif": 0,
        "cacah_baris_tanpa_lilin": 0,
        "kendali_data_sah": True,
        "kendali_deteksi_lolos": True,
        "kendali_negatif_terdeteksi": True,
    }


def _selisih_nol():
    return {k: 0 for k in kl.INVARIAN}


def test_01_versi():
    assert kl.VERSI == 1


def test_02_nama_keluaran():
    assert kl.nama_keluaran() == "reports/keterisian_lilin.json"


def test_03_nama_ringkas():
    assert kl.nama_ringkas() == "reports/keterisian_lilin_ringkas.json"


def test_04_batas_baris_laporan():
    assert kl.BATAS_BARIS_LAPORAN == 40


def test_05_berkas_dicap():
    assert kl.BERKAS_DICAP == [
        "kehidupan.py",
        "kehidupan_arsip.py",
        "keterisian_lilin.py",
        "silang_funding.py",
    ]


def test_06_sidik_kode_panjang():
    assert len(kl.sidik_kode()) == 64


def test_07_sidik_kode_stabil():
    assert kl.sidik_kode() == kl.sidik_kode()


def test_08_hari_januari():
    assert kl.hari_dalam_bulan("2024-01") == 31


def test_09_hari_februari_biasa():
    assert kl.hari_dalam_bulan("2023-02") == 28


def test_10_hari_februari_kabisat():
    assert kl.hari_dalam_bulan("2024-02") == 29


def test_11_hari_februari_2000():
    assert kl.hari_dalam_bulan("2000-02") == 29


def test_12_hari_februari_1900():
    assert kl.hari_dalam_bulan("1900-02") == 28


def test_13_hari_april():
    assert kl.hari_dalam_bulan("2025-04") == 30


def test_14_hari_desember():
    assert kl.hari_dalam_bulan("2026-12") == 31


def test_15_hari_bulan_cacat():
    with pytest.raises(ValueError):
        kl.hari_dalam_bulan("2024-13")


def test_16_lilin_penuh_januari():
    assert kl.lilin_penuh("2024-01") == 44640


def test_17_lilin_penuh_februari_kabisat():
    assert kl.lilin_penuh("2024-02") == 41760


def test_18_lilin_penuh_april():
    assert kl.lilin_penuh("2025-04") == 43200


def test_19_defisit_nol():
    assert kl.defisit(44640, "2024-01") == 0


def test_20_defisit_positif():
    assert kl.defisit(40000, "2023-02") == 320


def test_21_defisit_negatif():
    assert kl.defisit(44641, "2024-03") == -1


def test_22_defisit_lilin_none():
    assert kl.defisit(None, "2024-01") is None


def test_23_peta_pertama_satu_simbol():
    status = {("AAA", "2024-03"): "HIDUP", ("AAA", "2024-01"): "HIDUP"}
    assert kl.peta_bulan_pertama(status) == {"AAA": "2024-01"}


def test_24_peta_pertama_dua_simbol():
    status = {
        ("AAA", "2024-03"): "HIDUP",
        ("BBB", "2020-07"): "HIDUP",
        ("BBB", "2021-01"): "HIDUP",
    }
    assert kl.peta_bulan_pertama(status) == {"AAA": "2024-03", "BBB": "2020-07"}


def test_25_kumpulkan_cacah_baris():
    status, lilin = kl.semesta_kendali()
    assert len(kl.kumpulkan(status, lilin)) == 5


def test_26_kumpulkan_medan_lengkap():
    status, lilin = kl.semesta_kendali()
    baris = kl.kumpulkan(status, lilin)[0]
    assert set(baris) == {
        "simbol",
        "bulan",
        "status",
        "cacah_lilin",
        "lilin_penuh",
        "defisit",
        "pertama",
    }


def test_27_kumpulkan_tandai_pertama():
    status, lilin = kl.semesta_kendali()
    baris = kl.kumpulkan(status, lilin)
    pertama = {(r["simbol"], r["bulan"]) for r in baris if r["pertama"]}
    assert pertama == {("AAA", "2024-01"), ("BBB", "2023-02"), ("CCC", "2025-04")}


def test_28_kumpulkan_lilin_hilang_null():
    status = {("AAA", "2024-01"): kehidupan.STATUS_MATI}
    baris = kl.kumpulkan(status, {})[0]
    assert baris["cacah_lilin"] is None and baris["defisit"] is None


def test_29_ringkas_defisit_total():
    status, lilin = kl.semesta_kendali()
    assert kl.ringkas_defisit(kl.kumpulkan(status, lilin))["defisit_total"] == 1160


def test_30_ringkas_defisit_pertama():
    status, lilin = kl.semesta_kendali()
    assert kl.ringkas_defisit(kl.kumpulkan(status, lilin))["defisit_pertama"] == 520


def test_31_ringkas_defisit_bukan_pertama():
    status, lilin = kl.semesta_kendali()
    r = kl.ringkas_defisit(kl.kumpulkan(status, lilin))
    assert r["defisit_bukan_pertama"] == 640


def test_32_ringkas_jumlah_lilin_langsung():
    status, lilin = kl.semesta_kendali()
    r = kl.ringkas_defisit(kl.kumpulkan(status, lilin))
    assert r["jumlah_lilin_langsung"] == 213400


def test_33_ringkas_cacah_defisit_negatif():
    status = {("DDD", "2024-03"): kehidupan.STATUS_MATI}
    r = kl.ringkas_defisit(kl.kumpulkan(status, {("DDD", "2024-03"): 44641}))
    assert r["cacah_defisit_negatif"] == 1


def test_34_cacah_mati_tak_penuh():
    status, lilin = kl.semesta_kendali()
    assert kl.cacah_mati_tak_penuh(kl.kumpulkan(status, lilin)) == 3


def test_35_cacah_mati_penuh():
    status, lilin = kl.semesta_kendali()
    assert kl.cacah_mati_penuh(kl.kumpulkan(status, lilin)) == 1


def test_36_bagian_defisit_bukan_pertama():
    status, lilin = kl.semesta_kendali()
    r = kl.ringkas_defisit(kl.kumpulkan(status, lilin))
    assert kl.bagian_defisit_bukan_pertama(r) == 0.5517


def test_37_bagian_penyebut_nol_null():
    kosong = {"defisit_total": 0, "defisit_bukan_pertama": 0}
    assert kl.bagian_defisit_bukan_pertama(kosong) is None


def test_38_dalam_pita_batas_bawah():
    assert kl.dalam_pita(1, kl.R310_PITA_BUTIR_1)


def test_39_dalam_pita_batas_atas():
    assert kl.dalam_pita(120, kl.R310_PITA_BUTIR_1)


def test_40_dalam_pita_luar():
    assert not kl.dalam_pita(121, kl.R310_PITA_BUTIR_1)


def test_41_dalam_pita_pecahan_batas():
    assert kl.dalam_pita_pecahan(0.02, kl.R310_PITA_BUTIR_2)


def test_42_dalam_pita_pecahan_null():
    assert not kl.dalam_pita_pecahan(None, kl.R310_PITA_BUTIR_2)


def test_43_pita_butir_1_terkunci():
    assert kl.R310_PITA_BUTIR_1 == (1, 120)


def test_44_pita_butir_2_terkunci():
    assert kl.R310_PITA_BUTIR_2 == (0.02, 0.25)


def test_45_invarian_delapan_kunci():
    assert set(kl.INVARIAN) == {
        "penyebut",
        "cacah_simbol",
        "cacah_hidup",
        "cacah_sepi",
        "cacah_mati",
        "total_byte",
        "byte_hidup",
        "cacah_hidup_byte_kecil",
    }


def test_46_invarian_terukur_cocok():
    status = {
        ("AAA", "2024-01"): kehidupan.STATUS_HIDUP,
        ("AAA", "2024-02"): kehidupan.STATUS_MATI,
        ("BBB", "2023-02"): kehidupan.STATUS_SEPI,
    }
    byte_parquet = {
        ("AAA", "2024-01"): 100,
        ("AAA", "2024-02"): 50,
        ("BBB", "2023-02"): 7,
    }
    assert kl.invarian_terukur(status, byte_parquet) == {
        "penyebut": 3,
        "cacah_simbol": 2,
        "cacah_hidup": 1,
        "cacah_sepi": 1,
        "cacah_mati": 1,
        "total_byte": 157,
        "byte_hidup": 100,
        "cacah_hidup_byte_kecil": 1,
    }


def test_47_selisih_invarian_bukan_nol():
    terukur = dict(kl.INVARIAN)
    terukur["penyebut"] = 19585
    assert kl.selisih_invarian(terukur)["penyebut"] == -1


def test_48_kendali_deteksi_lolos():
    assert kl.kendali_deteksi()["lolos"] is True


def test_49_kendali_negatif_terdeteksi():
    assert kl.kendali_negatif()["terdeteksi"] is True


def test_50_kendali_data_sah():
    status = {
        ("BTCUSDT", "2021-05"): kehidupan.STATUS_HIDUP,
        ("BTCUSDT", "2021-08"): kehidupan.STATUS_HIDUP,
        ("BTCUSDT", "2021-01"): kehidupan.STATUS_HIDUP,
        ("AAAUSDT", "2021-01"): kehidupan.STATUS_MATI,
    }
    byte_parquet = {
        ("BTCUSDT", "2021-05"): 2770666,
        ("BTCUSDT", "2021-08"): 2730341,
        ("BTCUSDT", "2021-01"): 2722266,
        ("AAAUSDT", "2021-01"): 9,
    }
    assert kl.kendali_data_sah(kl.kendali_data(status, byte_parquet))


def test_51_kendali_data_gagal():
    status = {
        ("BTCUSDT", "2021-05"): kehidupan.STATUS_HIDUP,
        ("BTCUSDT", "2021-08"): kehidupan.STATUS_MATI,
        ("BTCUSDT", "2021-01"): kehidupan.STATUS_HIDUP,
    }
    byte_parquet = {
        ("BTCUSDT", "2021-05"): 2770666,
        ("BTCUSDT", "2021-08"): 2730341,
        ("BTCUSDT", "2021-01"): 2722266,
    }
    assert not kl.kendali_data_sah(kl.kendali_data(status, byte_parquet))


def test_52_butir_1_menang():
    hasil = kl.uji_r310(50, 0.07, _selisih_nol())
    assert hasil["butir_1"]["menang"] is True


def test_53_butir_1_kalah_nol():
    hasil = kl.uji_r310(0, 0.07, _selisih_nol())
    assert hasil["butir_1"]["menang"] is False


def test_54_butir_1_kalah_atas():
    hasil = kl.uji_r310(121, 0.07, _selisih_nol())
    assert hasil["butir_1"]["menang"] is False


def test_55_butir_2_menang():
    hasil = kl.uji_r310(50, 0.073, _selisih_nol())
    assert hasil["butir_2"]["menang"] is True


def test_56_butir_2_kalah():
    hasil = kl.uji_r310(50, 0.3, _selisih_nol())
    assert hasil["butir_2"]["menang"] is False


def test_57_butir_3_mudah():
    hasil = kl.uji_r310(50, 0.07, _selisih_nol())
    assert hasil["butir_3"]["mudah"] is True
    assert hasil["butir_3"]["berisiko"] is False


def test_58_kode_keluar_nol():
    assert kl.kode_keluar(_ringkasan_sehat()) == 0


def test_59_kode_keluar_invarian_gagal():
    r = _ringkasan_sehat()
    r["selisih_invarian"]["cacah_mati"] = 1
    assert kl.kode_keluar(r) == 2


def test_60_kode_keluar_defisit_negatif():
    r = _ringkasan_sehat()
    r["cacah_defisit_negatif"] = 1
    assert kl.kode_keluar(r) == 2


def test_61_kode_keluar_lilin_kurang():
    r = _ringkasan_sehat()
    r["cacah_baris_tanpa_lilin"] = 3
    assert kl.kode_keluar(r) == 2


def test_62_kode_keluar_kendali_gagal():
    r = _ringkasan_sehat()
    r["kendali_deteksi_lolos"] = False
    assert kl.kode_keluar(r) == 2


def test_63_potong_batas():
    banyak = [{"n": i} for i in range(100)]
    assert len(kl.potong(banyak)) == kl.BATAS_BARIS_LAPORAN


def test_64_sumber_delapan_pecahan():
    sumber = kl.daftar_sumber()
    assert len(sumber) == 8 and sumber[0] == "reports/kehidupan_arsip_0.json"
