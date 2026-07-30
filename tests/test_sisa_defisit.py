"""Uji `sisa_defisit` V1 — R-311.

DAFTAR BERNOMOR LENGKAP (aturan 57, satu nama per nomor, tanpa rentang):

01 test_01_versi_dan_nama_keluaran
02 test_02_nama_ringkas
03 test_03_pita_butir_1_terkunci
04 test_04_pita_butir_2_terkunci
05 test_05_cacah_teratas_dan_batas_laporan
06 test_06_berkas_dicap_tepat_lima
07 test_07_sidik_kode_bentuk_heksa
08 test_08_sidik_kode_stabil
09 test_09_invarian_sepuluh_kunci
10 test_10_invarian_nilai_terbitan
11 test_11_sisa_tercatat_konsisten
12 test_12_calon_baris_menyaring
13 test_13_calon_baris_membuang_pertama
14 test_14_calon_baris_membuang_mati
15 test_15_berdefisit_hanya_positif
16 test_16_berdefisit_membuang_null
17 test_17_teratas_urut_menurun
18 test_18_teratas_seri_deterministik
19 test_19_teratas_memotong
20 test_20_jumlah_defisit_langsung
21 test_21_bagian_teratas_hitung_tangan
22 test_22_bagian_teratas_null_bila_kurang
23 test_23_bagian_teratas_null_bila_penyebut_nol
24 test_24_bagian_bulat_empat_desimal
25 test_25_invarian_terukur_semesta_kendali
26 test_26_selisih_invarian_nol
27 test_27_selisih_invarian_bukan_nol
28 test_28_kendali_negatif_lolos
29 test_29_kendali_negatif_memuat_penuh_dan_berdefisit
30 test_30_kendali_nol_lolos
31 test_31_defisit_negatif_tertangkap
32 test_32_baris_tanpa_lilin_tertangkap
33 test_33_dalam_pita_batas
34 test_34_dalam_pita_pecahan_batas
35 test_35_butir_1_menang
36 test_36_butir_1_kalah
37 test_37_butir_1_tidak_teradjudikasi
38 test_38_butir_2_menang
39 test_39_butir_2_tidak_teradjudikasi
40 test_40_butir_3_menuntut_bersih
41 test_41_kode_keluar_nol
42 test_42_kode_keluar_sidik_tidak_seragam
43 test_43_kode_keluar_defisit_negatif
44 test_44_kode_keluar_selisih_invarian

Cacah butir: 44. Tanpa `parametrize`. Helper berawalan garis bawah.
"""

from __future__ import annotations

from lux_ai.serapan import kehidupan, sisa_defisit


def _baris(simbol, bulan, status, defisit, pertama=False, lilin=1):
    return {
        "simbol": simbol,
        "bulan": bulan,
        "status": status,
        "cacah_lilin": lilin,
        "lilin_penuh": 44640,
        "defisit": defisit,
        "pertama": pertama,
    }


def _ringkasan_bersih():
    return {
        "sidik_seragam": True,
        "cacah_laporan_dibaca": sisa_defisit.TOTAL_PECAHAN,
        "total_pecahan": sisa_defisit.TOTAL_PECAHAN,
        "cacah_kunci_ganda": 0,
        "cacah_defisit_negatif": 0,
        "cacah_baris_tanpa_lilin": 0,
        "selisih_invarian": {k: 0 for k in sisa_defisit.INVARIAN},
        "kendali_data_sah": True,
        "kendali_negatif_lolos": True,
        "kendali_nol_lolos": True,
    }


def test_01_versi_dan_nama_keluaran():
    assert sisa_defisit.VERSI == 1
    assert sisa_defisit.nama_keluaran() == "reports/sisa_defisit.json"


def test_02_nama_ringkas():
    assert sisa_defisit.nama_ringkas() == "reports/sisa_defisit_ringkas.json"


def test_03_pita_butir_1_terkunci():
    assert sisa_defisit.R311_PITA_BUTIR_1 == (200, 12000)


def test_04_pita_butir_2_terkunci():
    assert sisa_defisit.R311_PITA_BUTIR_2 == (0.02, 0.45)


def test_05_cacah_teratas_dan_batas_laporan():
    assert sisa_defisit.CACAH_TERATAS == 10
    assert sisa_defisit.BATAS_BARIS_LAPORAN == 40


def test_06_berkas_dicap_tepat_lima():
    assert sisa_defisit.BERKAS_DICAP == [
        "kehidupan.py",
        "kehidupan_arsip.py",
        "keterisian_lilin.py",
        "silang_funding.py",
        "sisa_defisit.py",
    ]


def test_07_sidik_kode_bentuk_heksa():
    s = sisa_defisit.sidik_kode()
    assert len(s) == 64
    assert all(c in "0123456789abcdef" for c in s)


def test_08_sidik_kode_stabil():
    assert sisa_defisit.sidik_kode() == sisa_defisit.sidik_kode()


def test_09_invarian_sepuluh_kunci():
    assert len(sisa_defisit.INVARIAN) == 10
    assert "defisit_bukan_pertama" in sisa_defisit.INVARIAN
    assert "defisit_sembilan" in sisa_defisit.INVARIAN


def test_10_invarian_nilai_terbitan():
    inv = sisa_defisit.INVARIAN
    assert inv["penyebut"] == 19586
    assert inv["cacah_simbol"] == 787
    assert inv["cacah_bukan_pertama"] == 18799
    assert inv["cacah_hidup"] == 18087
    assert inv["cacah_sepi"] == 98
    assert inv["cacah_mati"] == 1401
    assert inv["cacah_mati_penuh"] == 1392
    assert inv["cacah_mati_tak_penuh"] == 9
    assert inv["defisit_bukan_pertama"] == 808162
    assert inv["defisit_sembilan"] == 95237


def test_11_sisa_tercatat_konsisten():
    inv = sisa_defisit.INVARIAN
    selisih = inv["defisit_bukan_pertama"] - inv["defisit_sembilan"]
    assert sisa_defisit.SISA_TERCATAT == 712925
    assert selisih == sisa_defisit.SISA_TERCATAT


def test_12_calon_baris_menyaring():
    baris = [
        _baris("A", "2024-01", kehidupan.STATUS_HIDUP, 0, pertama=True),
        _baris("A", "2024-02", kehidupan.STATUS_HIDUP, 10),
        _baris("B", "2024-02", kehidupan.STATUS_SEPI, 20),
    ]
    calon = sisa_defisit.calon_baris(baris)
    assert len(calon) == 2


def test_13_calon_baris_membuang_pertama():
    baris = [_baris("A", "2024-01", kehidupan.STATUS_HIDUP, 99, pertama=True)]
    assert sisa_defisit.calon_baris(baris) == []


def test_14_calon_baris_membuang_mati():
    baris = [_baris("A", "2024-02", kehidupan.STATUS_MATI, 99)]
    assert sisa_defisit.calon_baris(baris) == []


def test_15_berdefisit_hanya_positif():
    baris = [
        _baris("A", "2024-02", kehidupan.STATUS_HIDUP, 0),
        _baris("B", "2024-02", kehidupan.STATUS_HIDUP, 5),
    ]
    hasil = sisa_defisit.baris_berdefisit(baris)
    assert len(hasil) == 1
    assert hasil[0]["simbol"] == "B"


def test_16_berdefisit_membuang_null():
    baris = [_baris("A", "2024-02", kehidupan.STATUS_HIDUP, None)]
    assert sisa_defisit.baris_berdefisit(baris) == []


def test_17_teratas_urut_menurun():
    baris = [
        _baris("A", "2024-02", kehidupan.STATUS_HIDUP, 5),
        _baris("B", "2024-02", kehidupan.STATUS_HIDUP, 50),
        _baris("C", "2024-02", kehidupan.STATUS_HIDUP, 500),
    ]
    urut = sisa_defisit.teratas(baris, 3)
    assert [r["simbol"] for r in urut] == ["C", "B", "A"]


def test_18_teratas_seri_deterministik():
    baris = [
        _baris("B", "2024-02", kehidupan.STATUS_HIDUP, 7),
        _baris("A", "2024-03", kehidupan.STATUS_HIDUP, 7),
        _baris("A", "2024-01", kehidupan.STATUS_HIDUP, 7),
    ]
    urut = sisa_defisit.teratas(baris, 3)
    assert [(r["simbol"], r["bulan"]) for r in urut] == [
        ("A", "2024-01"),
        ("A", "2024-03"),
        ("B", "2024-02"),
    ]


def test_19_teratas_memotong():
    baris = [
        _baris("A", "2024-0%d" % i, kehidupan.STATUS_HIDUP, i) for i in range(1, 6)
    ]
    assert len(sisa_defisit.teratas(baris, 2)) == 2


def test_20_jumlah_defisit_langsung():
    baris = [
        _baris("A", "2024-02", kehidupan.STATUS_HIDUP, 100),
        _baris("B", "2024-02", kehidupan.STATUS_HIDUP, 500),
        _baris("C", "2024-02", kehidupan.STATUS_HIDUP, 20),
    ]
    assert sisa_defisit.jumlah_defisit(baris) == 620


def test_21_bagian_teratas_hitung_tangan():
    baris = [
        _baris("A", "2024-02", kehidupan.STATUS_HIDUP, 100),
        _baris("B", "2024-02", kehidupan.STATUS_HIDUP, 500),
        _baris("C", "2024-02", kehidupan.STATUS_HIDUP, 20),
    ]
    assert sisa_defisit.bagian_teratas(baris, 2) == 0.9677


def test_22_bagian_teratas_null_bila_kurang():
    baris = [_baris("A", "2024-02", kehidupan.STATUS_HIDUP, 100)]
    assert sisa_defisit.bagian_teratas(baris, 10) is None


def test_23_bagian_teratas_null_bila_penyebut_nol():
    baris = [
        _baris("A", "2024-02", kehidupan.STATUS_HIDUP, 0),
        _baris("B", "2024-02", kehidupan.STATUS_HIDUP, 0),
    ]
    assert sisa_defisit.bagian_teratas(baris, 2) is None


def test_24_bagian_bulat_empat_desimal():
    assert sisa_defisit._bagian(1, 3) == 0.3333
    assert sisa_defisit._bagian(1, 0) is None


def test_25_invarian_terukur_semesta_kendali():
    terukur = sisa_defisit.invarian_terukur(sisa_defisit.baris_kendali())
    assert terukur["penyebut"] == 11
    assert terukur["cacah_simbol"] == 5
    assert terukur["cacah_bukan_pertama"] == 6
    assert terukur["cacah_mati_penuh"] == 2
    assert terukur["cacah_mati_tak_penuh"] == 2
    assert terukur["defisit_sembilan"] == 300
    assert terukur["defisit_bukan_pertama"] == 720


def test_26_selisih_invarian_nol():
    selisih = sisa_defisit.selisih_invarian(dict(sisa_defisit.INVARIAN))
    assert set(selisih) == set(sisa_defisit.INVARIAN)
    assert all(v == 0 for v in selisih.values())


def test_27_selisih_invarian_bukan_nol():
    terukur = dict(sisa_defisit.INVARIAN)
    terukur["defisit_bukan_pertama"] = 808163
    selisih = sisa_defisit.selisih_invarian(terukur)
    assert selisih["defisit_bukan_pertama"] == 1


def test_28_kendali_negatif_lolos():
    hasil = sisa_defisit.kendali_negatif()
    assert hasil["lolos"] is True
    assert hasil["terukur"] == sisa_defisit.JAWABAN_KENDALI


def test_29_kendali_negatif_memuat_penuh_dan_berdefisit():
    baris = sisa_defisit.baris_kendali()
    calon = sisa_defisit.calon_baris(baris)
    berdefisit = sisa_defisit.baris_berdefisit(calon)
    assert len(berdefisit) == 3
    assert len(calon) - len(berdefisit) == 1


def test_30_kendali_nol_lolos():
    hasil = sisa_defisit.kendali_nol()
    assert hasil["lolos"] is True
    assert hasil["cacah_berdefisit"] == 0
    assert hasil["bagian_teratas"] is None


def test_31_defisit_negatif_tertangkap():
    baris = [_baris("A", "2024-02", kehidupan.STATUS_HIDUP, -1)]
    r = sisa_defisit.ringkas_bukan_pertama(baris)
    assert r["cacah_defisit_negatif"] == 1
    assert r["defisit_bukan_pertama"] == 0


def test_32_baris_tanpa_lilin_tertangkap():
    baris = [_baris("A", "2024-02", kehidupan.STATUS_HIDUP, None, lilin=None)]
    r = sisa_defisit.ringkas_bukan_pertama(baris)
    assert r["cacah_baris_tanpa_lilin"] == 1


def test_33_dalam_pita_batas():
    pita = sisa_defisit.R311_PITA_BUTIR_1
    assert sisa_defisit.dalam_pita(200, pita) is True
    assert sisa_defisit.dalam_pita(12000, pita) is True
    assert sisa_defisit.dalam_pita(199, pita) is False
    assert sisa_defisit.dalam_pita(12001, pita) is False
    assert sisa_defisit.dalam_pita(None, pita) is False


def test_34_dalam_pita_pecahan_batas():
    pita = sisa_defisit.R311_PITA_BUTIR_2
    assert sisa_defisit.dalam_pita_pecahan(0.02, pita) is True
    assert sisa_defisit.dalam_pita_pecahan(0.45, pita) is True
    assert sisa_defisit.dalam_pita_pecahan(0.019, pita) is False
    assert sisa_defisit.dalam_pita_pecahan(0.46, pita) is False
    assert sisa_defisit.dalam_pita_pecahan(None, pita) is False


def test_35_butir_1_menang():
    nol = {k: 0 for k in sisa_defisit.INVARIAN}
    hasil = sisa_defisit.uji_r311(1000, 3000, 0.2, nol, True)
    assert hasil["butir_1"]["hasil"] == "menang"


def test_36_butir_1_kalah():
    nol = {k: 0 for k in sisa_defisit.INVARIAN}
    hasil = sisa_defisit.uji_r311(1000, 18000, 0.2, nol, True)
    assert hasil["butir_1"]["hasil"] == "kalah"


def test_37_butir_1_tidak_teradjudikasi():
    nol = {k: 0 for k in sisa_defisit.INVARIAN}
    hasil = sisa_defisit.uji_r311(0, 0, None, nol, True)
    assert hasil["butir_1"]["hasil"] == "tidak_teradjudikasi"


def test_38_butir_2_menang():
    nol = {k: 0 for k in sisa_defisit.INVARIAN}
    hasil = sisa_defisit.uji_r311(1000, 3000, 0.2, nol, True)
    assert hasil["butir_2"]["hasil"] == "menang"
    assert hasil["cacah_menang_berisiko"] == 2


def test_39_butir_2_tidak_teradjudikasi():
    nol = {k: 0 for k in sisa_defisit.INVARIAN}
    hasil = sisa_defisit.uji_r311(1000, 4, 0.2, nol, True)
    assert hasil["butir_2"]["hasil"] == "tidak_teradjudikasi"


def test_40_butir_3_menuntut_bersih():
    nol = {k: 0 for k in sisa_defisit.INVARIAN}
    assert sisa_defisit.uji_r311(1, 1, None, nol, True)["butir_3"]["hasil"] == "menang"
    assert sisa_defisit.uji_r311(1, 1, None, nol, False)["butir_3"]["hasil"] == "kalah"
    rusak = dict(nol)
    rusak["cacah_sepi"] = 1
    assert sisa_defisit.uji_r311(1, 1, None, rusak, True)["butir_3"]["hasil"] == "kalah"


def test_41_kode_keluar_nol():
    assert sisa_defisit.kode_keluar(_ringkasan_bersih()) == 0


def test_42_kode_keluar_sidik_tidak_seragam():
    r = _ringkasan_bersih()
    r["sidik_seragam"] = False
    assert sisa_defisit.kode_keluar(r) == 2


def test_43_kode_keluar_defisit_negatif():
    r = _ringkasan_bersih()
    r["cacah_defisit_negatif"] = 1
    assert sisa_defisit.kode_keluar(r) == 2


def test_44_kode_keluar_selisih_invarian():
    r = _ringkasan_bersih()
    r["selisih_invarian"] = dict(r["selisih_invarian"])
    r["selisih_invarian"]["defisit_sembilan"] = -3
    assert sisa_defisit.kode_keluar(r) == 2
