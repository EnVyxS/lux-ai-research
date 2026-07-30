"""Uji `selisih_lilin` V1. Seluruhnya murni: tanpa jaringan, tanpa berkas data.

Cacah butir dicacah TANGAN dan dinomori test_01..test_36 (aturan 57).
"""

from __future__ import annotations

import pytest

from lux_ai.serapan import kehidupan, selisih_lilin as sl


def _baris_kendali():
    status, klaim, terbaca = sl.semesta_kendali()
    return sl.kumpulkan(status, klaim, terbaca)


def _ringkasan_sehat():
    return {
        "sidik_seragam": True,
        "cacah_laporan_dibaca": sl.TOTAL_PECAHAN,
        "total_pecahan": sl.TOTAL_PECAHAN,
        "cacah_kunci_ganda": 0,
        "selisih_invarian": {k: 0 for k in sl.INVARIAN},
        "cacah_baris_tanpa_klaim": 0,
        "cacah_baris_tanpa_terbaca": 0,
        "cacah_berselisih": 37,
        "dua_jalur_bertemu": True,
        "kendali_deteksi_lolos": True,
        "kendali_nol_lolos": True,
        "kendali_negatif_terdeteksi": True,
        "kendali_teratas_lolos": True,
    }


def test_01_versi_satu():
    assert sl.VERSI == 1


def test_02_nama_keluaran():
    assert sl.nama_keluaran() == "reports/selisih_lilin.json"


def test_03_nama_ringkas():
    assert sl.nama_ringkas() == "reports/selisih_lilin_ringkas.json"


def test_04_daftar_sumber_delapan():
    sumber = sl.daftar_sumber()
    assert len(sumber) == sl.TOTAL_PECAHAN
    assert len(set(sumber)) == len(sumber)


def test_05_sidik_kode_stabil():
    assert sl.sidik_kode() == sl.sidik_kode()


def test_06_sidik_kode_enam_puluh_empat_heks():
    s = sl.sidik_kode()
    assert len(s) == 64
    assert all(c in "0123456789abcdef" for c in s)


def test_07_pita_butir_1_terkunci():
    assert sl.R312_PITA_BUTIR_1 == (12, 120)


def test_08_pita_butir_2_terkunci():
    assert sl.R312_PITA_BUTIR_2 == (0.50, 0.865)


def test_09_dua_medan_berbeda():
    assert sl.MEDAN_KLAIM == "cacah_lilin"
    assert sl.MEDAN_TERBACA == "cacah_lilin_terbaca"
    assert sl.MEDAN_KLAIM != sl.MEDAN_TERBACA


def test_10_arah_selisih_terbaca_dikurangi_klaim():
    assert sl.selisih(100, 140) == 40
    assert sl.selisih(140, 100) == -40


def test_11_selisih_null_bila_medan_hilang():
    assert sl.selisih(None, 100) is None
    assert sl.selisih(100, None) is None
    assert sl.selisih(None, None) is None


def test_12_kumpulkan_urut_deterministik():
    baris = _baris_kendali()
    kunci = [(r["simbol"], r["bulan"]) for r in baris]
    assert kunci == sorted(kunci)


def test_13_kumpulkan_cacah_baris_sama_dengan_status():
    assert len(_baris_kendali()) == 5


def test_14_jumlah_selisih_positif_kendali():
    assert sl.ringkas_selisih(_baris_kendali())["jumlah_selisih_positif"] == 1080


def test_15_bersih_sama_dengan_positif_kurang_negatif():
    r = sl.ringkas_selisih(_baris_kendali())
    assert r["jumlah_selisih_bersih"] == (
        r["jumlah_selisih_positif"] - r["jumlah_selisih_negatif"]
    )


def test_16_dua_jalur_bertemu_pada_kendali():
    assert sl.dua_jalur_bertemu(sl.ringkas_selisih(_baris_kendali()))


def test_17_baris_berselisih_hanya_bukan_nol():
    beda = sl.baris_berselisih(_baris_kendali())
    assert len(beda) == 3
    assert all(int(r["selisih"]) != 0 for r in beda)


def test_18_baris_berselisih_urut_menurun():
    nilai = [int(r["selisih"]) for r in sl.baris_berselisih(_baris_kendali())]
    assert nilai == sorted(nilai, reverse=True)


def test_19_teratas_none_bila_kurang_sepuluh():
    assert sl.teratas(_baris_kendali()) is None


def test_20_teratas_sepuluh_bila_cukup():
    status, klaim, terbaca = sl.semesta_teratas()
    puncak = sl.teratas(sl.kumpulkan(status, klaim, terbaca))
    assert puncak is not None
    assert len(puncak) == 10


def test_21_bagian_teratas_kendali_tangan():
    status, klaim, terbaca = sl.semesta_teratas()
    assert sl.bagian_teratas(sl.kumpulkan(status, klaim, terbaca)) == 0.9615


def test_22_bagian_teratas_none_bila_tak_ada_positif():
    status, klaim, _ = sl.semesta_kendali()
    assert sl.bagian_teratas(sl.kumpulkan(status, klaim, dict(klaim))) is None


def test_23_kendali_deteksi_lolos():
    assert sl.kendali_deteksi()["lolos"] is True


def test_24_kendali_nol_lolos():
    nol = sl.kendali_nol()
    assert nol["lolos"] is True
    assert nol["cacah_berselisih"] == 0


def test_25_kendali_negatif_terdeteksi():
    neg = sl.kendali_negatif()
    assert neg["terdeteksi"] is True
    assert neg["jumlah_selisih_bersih"] == -250


def test_26_kendali_teratas_lolos():
    assert sl.kendali_teratas()["lolos"] is True


def test_27_invarian_delapan_kunci():
    assert len(sl.INVARIAN) == 8
    assert sl.INVARIAN["penyebut"] == 19586


def test_28_selisih_invarian_nol_bila_cocok():
    s = sl.selisih_invarian(dict(sl.INVARIAN))
    assert set(s) == set(sl.INVARIAN)
    assert all(v == 0 for v in s.values())


def test_29_dalam_pita_batas_inklusif():
    assert sl.dalam_pita(12, sl.R312_PITA_BUTIR_1)
    assert sl.dalam_pita(120, sl.R312_PITA_BUTIR_1)
    assert not sl.dalam_pita(11, sl.R312_PITA_BUTIR_1)
    assert not sl.dalam_pita(121, sl.R312_PITA_BUTIR_1)
    assert not sl.dalam_pita(None, sl.R312_PITA_BUTIR_1)


def test_30_dalam_pita_pecahan_batas_inklusif():
    assert sl.dalam_pita_pecahan(0.50, sl.R312_PITA_BUTIR_2)
    assert sl.dalam_pita_pecahan(0.865, sl.R312_PITA_BUTIR_2)
    assert not sl.dalam_pita_pecahan(0.49, sl.R312_PITA_BUTIR_2)
    assert not sl.dalam_pita_pecahan(None, sl.R312_PITA_BUTIR_2)


def test_31_butir_3_ditandai_mudah_dan_tak_berisiko():
    u = sl.uji_r312(20, 0.7, {k: 0 for k in sl.INVARIAN})
    assert u["butir_3"]["mudah"] is True
    assert u["butir_3"]["berisiko"] is False
    assert u["butir_1"]["berisiko"] is True
    assert u["butir_2"]["berisiko"] is True


def test_32_tidak_teradjudikasi_bila_medan_identik():
    u = sl.uji_r312(0, None, {k: 0 for k in sl.INVARIAN})
    assert u["teradjudikasi"] is False
    assert u["butir_1"]["menang"] is False
    assert u["butir_2"]["menang"] is False
    assert u["cacah_menang_berisiko"] == 0


def test_33_kode_keluar_nol_pada_ringkasan_sehat():
    assert sl.kode_keluar(_ringkasan_sehat()) == 0


def test_34_kode_keluar_dua_bila_invarian_meleset():
    r = _ringkasan_sehat()
    r["selisih_invarian"] = dict(r["selisih_invarian"], penyebut=1)
    assert sl.kode_keluar(r) == 2


def test_35_kode_keluar_dua_bila_medan_identik_atau_baris_tanpa_medan():
    r = _ringkasan_sehat()
    r["cacah_berselisih"] = 0
    assert sl.kode_keluar(r) == 2
    r2 = _ringkasan_sehat()
    r2["cacah_baris_tanpa_terbaca"] = 1
    assert sl.kode_keluar(r2) == 2


def test_36_aritmetika_warisan_konsisten():
    assert sl.BARIS_PARQUET_TERCATAT - sl.LILIN_LANGSUNG_TERCATAT == sl.SELISIH_TERCATAT
    assert sl.SELISIH_TERCATAT == 516135
