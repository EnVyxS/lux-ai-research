"""Uji bulan_pertama V1 (R-309).

DAFTAR BUTIR BERNOMOR — ditulis SEBELUM push (aturan 57). 65 fungsi `def test_`,
tidak satu pun memakai `parametrize`, sehingga cacah butir = cacah fungsi.

 1 versi_satu                      34 nisbah_cacah_pertama
 2 nama_keluaran_default           35 nisbah_nilai
 3 nama_keluaran_dengan_akar       36 nisbah_null_tanpa_bukan_pertama
 4 sidik_kode_panjang              37 selisih_invarian_nol
 5 sidik_kode_stabil               38 selisih_invarian_tanda
 6 bagian_dari_tuple               39 medan_selisih_delapan
 7 bagian_dari_teks_pipa           40 dalam_pita_batas_bawah
 8 bagian_dari_teks_titik_dua      41 dalam_pita_batas_atas
 9 bagian_tanpa_pemisah            42 dalam_pita_luar
10 kelas_status_hidup              43 dalam_pita_pecahan_batas
11 kelas_status_sepi               44 dalam_pita_pecahan_luar
12 kelas_status_mati               45 kendali_data_sah
13 kelas_status_huruf_kecil        46 kendali_data_gagal_byte_beda
14 kelas_status_asing_jadi_lain    47 kendali_data_gagal_bukan_hidup
15 peta_pertama_dua_simbol         48 kendali_deteksi_sah
16 peta_pertama_urutan_bebas       49 kendali_deteksi_angka_terkunci
17 peta_pertama_kosong             50 ringkaskan_medan_pokok
18 penanda_pertama                 51 ringkaskan_daftar_dan_nisbah
19 penanda_tepi                    52 uji_butir1_menang
20 penanda_bukan_sebagian          53 uji_butir1_kalah
21 penanda_pertama_sekaligus_tepi  54 uji_butir1_penyebut_nol
22 sebaran_cacah_per_kelas         55 uji_butir2_menang
23 sebaran_jumlah_byte             56 uji_butir2_kalah
24 sebaran_min_maks                57 uji_butir2_null_tidak_teradjudikasi
25 total_byte_langsung             58 uji_butir3_menang
26 total_byte_abai_tanpa_byte      59 uji_butir3_kalah_bila_selisih
27 cacah_di_bawah_strikt           60 kode_keluar_nol
28 cacah_di_bawah_kelas_terpisah   61 kode_keluar_satu
29 cacah_sebagian_hidup_kecil      62 tetapan_terkunci_pita
30 cacah_sebagian_nol              63 tetapan_terkunci_ambang_dan_tepi
31 daftar_kecil_urut_byte          64 tetapan_terkunci_invarian
32 daftar_kecil_medan_tanda        65 batas_baris_laporan
33 daftar_kecil_hormati_batas

Seluruh uji memakai semesta buatan; tidak ada jaringan, tidak ada berkas laporan.
"""

from lux_ai.serapan import bulan_pertama as bp


def semesta():
    status = {
        ("AAA", "2024-01"): "HIDUP",
        ("AAA", "2024-02"): "HIDUP",
        ("AAA", "2024-03"): "HIDUP",
        ("BBB", "2026-05"): "MATI",
        ("BBB", "2026-06"): "HIDUP",
    }
    byte_parquet = {
        ("AAA", "2024-01"): 100,
        ("AAA", "2024-02"): 300,
        ("AAA", "2024-03"): 500,
        ("BBB", "2026-05"): 400,
        ("BBB", "2026-06"): 200,
    }
    return status, byte_parquet


def ringkas_lulus():
    ringkas = {medan: 0 for medan in bp.MEDAN_SELISIH}
    ringkas.update(
        {
            "cacah_hidup_byte_kecil": 38,
            "cacah_hidup_kecil_sebagian": 30,
            "nisbah_rata": 0.3,
            "cacah_pertama": 787,
            "cacah_bukan_pertama": 18799,
            "kendali_data_sah": True,
            "kendali_deteksi_sah": True,
        }
    )
    return ringkas


def test_versi_satu():
    assert bp.VERSI == 1


def test_nama_keluaran_default():
    assert bp.nama_keluaran().endswith("reports/bulan_pertama.json")


def test_nama_keluaran_dengan_akar():
    assert bp.nama_keluaran("/tmp") == "/tmp/reports/bulan_pertama.json"


def test_sidik_kode_panjang():
    assert len(bp.sidik_kode()) == 64


def test_sidik_kode_stabil():
    assert bp.sidik_kode() == bp.sidik_kode()


def test_bagian_dari_tuple():
    assert bp._bagian(("AAA", "2024-01")) == ("AAA", "2024-01")


def test_bagian_dari_teks_pipa():
    assert bp._bagian("AAA|2024-01") == ("AAA", "2024-01")


def test_bagian_dari_teks_titik_dua():
    assert bp._bagian("AAA:2024-01") == ("AAA", "2024-01")


def test_bagian_tanpa_pemisah():
    assert bp._bagian("AAA") == ("AAA", "")


def test_kelas_status_hidup():
    assert bp.kelas_status("HIDUP") == bp.KELAS_HIDUP


def test_kelas_status_sepi():
    assert bp.kelas_status("SEPI") == bp.KELAS_SEPI


def test_kelas_status_mati():
    assert bp.kelas_status("MATI") == bp.KELAS_MATI


def test_kelas_status_huruf_kecil():
    assert bp.kelas_status(" hidup ") == bp.KELAS_HIDUP


def test_kelas_status_asing_jadi_lain():
    assert bp.kelas_status("ENTAH") == bp.KELAS_LAIN


def test_peta_pertama_dua_simbol():
    status, _ = semesta()
    assert bp.peta_bulan_pertama(status) == {"AAA": "2024-01", "BBB": "2026-05"}


def test_peta_pertama_urutan_bebas():
    terbalik = {
        ("AAA", "2024-03"): "HIDUP",
        ("AAA", "2024-01"): "HIDUP",
    }
    assert bp.peta_bulan_pertama(terbalik) == {"AAA": "2024-01"}


def test_peta_pertama_kosong():
    assert bp.peta_bulan_pertama({}) == {}


def test_penanda_pertama():
    peta = {"AAA": "2024-01"}
    tanda = bp.penanda_baris("AAA", "2024-01", peta)
    assert tanda["pertama"] and tanda["sebagian"] and not tanda["tepi"]


def test_penanda_tepi():
    peta = {"BBB": "2026-05"}
    tanda = bp.penanda_baris("BBB", "2026-06", peta)
    assert tanda["tepi"] and tanda["sebagian"] and not tanda["pertama"]


def test_penanda_bukan_sebagian():
    peta = {"AAA": "2024-01"}
    tanda = bp.penanda_baris("AAA", "2024-02", peta)
    assert not tanda["sebagian"]


def test_penanda_pertama_sekaligus_tepi():
    peta = {"CCC": "2026-06"}
    tanda = bp.penanda_baris("CCC", "2026-06", peta)
    assert tanda["pertama"] and tanda["tepi"] and tanda["sebagian"]


def test_sebaran_cacah_per_kelas():
    status, byte_parquet = semesta()
    sebaran = bp.sebaran_per_kelas(status, byte_parquet)
    assert sebaran[bp.KELAS_HIDUP]["cacah"] == 4
    assert sebaran[bp.KELAS_MATI]["cacah"] == 1


def test_sebaran_jumlah_byte():
    status, byte_parquet = semesta()
    sebaran = bp.sebaran_per_kelas(status, byte_parquet)
    assert sebaran[bp.KELAS_HIDUP]["jumlah"] == 1100


def test_sebaran_min_maks():
    status, byte_parquet = semesta()
    sebaran = bp.sebaran_per_kelas(status, byte_parquet)
    assert sebaran[bp.KELAS_HIDUP]["min"] == 100
    assert sebaran[bp.KELAS_HIDUP]["maks"] == 500


def test_total_byte_langsung():
    status, byte_parquet = semesta()
    assert bp.total_byte_langsung(status, byte_parquet) == 1500


def test_total_byte_abai_tanpa_byte():
    status, byte_parquet = semesta()
    status[("CCC", "2025-01")] = "HIDUP"
    assert bp.total_byte_langsung(status, byte_parquet) == 1500


def test_cacah_di_bawah_strikt():
    status, byte_parquet = semesta()
    assert bp.cacah_di_bawah(status, byte_parquet, bp.KELAS_HIDUP, 100) == 0


def test_cacah_di_bawah_kelas_terpisah():
    status, byte_parquet = semesta()
    assert bp.cacah_di_bawah(status, byte_parquet, bp.KELAS_MATI, 450) == 1


def test_cacah_sebagian_hidup_kecil():
    status, byte_parquet = semesta()
    assert bp.cacah_sebagian(status, byte_parquet, bp.KELAS_HIDUP, 250) == 2


def test_cacah_sebagian_nol():
    status, byte_parquet = semesta()
    assert bp.cacah_sebagian(status, byte_parquet, bp.KELAS_HIDUP, 50) == 0


def test_daftar_kecil_urut_byte():
    status, byte_parquet = semesta()
    daftar = bp.daftar_kecil_bertanda(status, byte_parquet, bp.KELAS_HIDUP, 400)
    assert [r["byte"] for r in daftar] == [100, 200, 300]


def test_daftar_kecil_medan_tanda():
    status, byte_parquet = semesta()
    daftar = bp.daftar_kecil_bertanda(status, byte_parquet, bp.KELAS_HIDUP, 400)
    assert daftar[0]["pertama"] is True
    assert daftar[1]["tepi"] is True
    assert daftar[2]["sebagian"] is False


def test_daftar_kecil_hormati_batas():
    status, byte_parquet = semesta()
    daftar = bp.daftar_kecil_bertanda(
        status, byte_parquet, bp.KELAS_HIDUP, 400, batas=2
    )
    assert len(daftar) == 2


def test_nisbah_cacah_pertama():
    status, byte_parquet = semesta()
    hasil = bp.nisbah_pertama(status, byte_parquet)
    assert hasil["cacah_pertama"] == 2
    assert hasil["cacah_bukan_pertama"] == 3


def test_nisbah_nilai():
    status, byte_parquet = semesta()
    hasil = bp.nisbah_pertama(status, byte_parquet)
    assert hasil["rata_byte_pertama"] == 250.0
    assert hasil["nisbah_rata"] == 0.75


def test_nisbah_null_tanpa_bukan_pertama():
    status = {("AAA", "2024-01"): "HIDUP"}
    byte_parquet = {("AAA", "2024-01"): 100}
    hasil = bp.nisbah_pertama(status, byte_parquet)
    assert hasil["nisbah_rata"] is None
    assert hasil["rata_byte_bukan_pertama"] is None


def test_selisih_invarian_nol():
    selisih = bp.selisih_invarian(dict(bp.INVARIAN))
    assert set(selisih.values()) == {0}


def test_selisih_invarian_tanda():
    ringkas = dict(bp.INVARIAN)
    ringkas["cacah_mati"] = ringkas["cacah_mati"] - 3
    assert bp.selisih_invarian(ringkas)["selisih_cacah_mati"] == -3


def test_medan_selisih_delapan():
    assert len(bp.MEDAN_SELISIH) == 8
    assert len(bp.INVARIAN) == 8


def test_dalam_pita_batas_bawah():
    assert bp.dalam_pita(22, bp.R309_PITA_BUTIR_1)


def test_dalam_pita_batas_atas():
    assert bp.dalam_pita(38, bp.R309_PITA_BUTIR_1)


def test_dalam_pita_luar():
    assert not bp.dalam_pita(21, bp.R309_PITA_BUTIR_1)


def test_dalam_pita_pecahan_batas():
    assert bp.dalam_pita_pecahan(0.10, bp.R309_PITA_BUTIR_2)
    assert bp.dalam_pita_pecahan(0.60, bp.R309_PITA_BUTIR_2)


def test_dalam_pita_pecahan_luar():
    assert not bp.dalam_pita_pecahan(0.61, bp.R309_PITA_BUTIR_2)
    assert not bp.dalam_pita_pecahan(None, bp.R309_PITA_BUTIR_2)


def test_kendali_data_sah():
    status, byte_parquet = semesta()
    sah, rinci = bp.kendali_data(
        byte_parquet, status, {("AAA", "2024-01"): 100}
    )
    assert sah is True
    assert rinci[0]["cocok"] is True


def test_kendali_data_gagal_byte_beda():
    status, byte_parquet = semesta()
    sah, _ = bp.kendali_data(byte_parquet, status, {("AAA", "2024-01"): 999})
    assert sah is False


def test_kendali_data_gagal_bukan_hidup():
    status, byte_parquet = semesta()
    sah, _ = bp.kendali_data(byte_parquet, status, {("BBB", "2026-05"): 400})
    assert sah is False


def test_kendali_deteksi_sah():
    sah, _ = bp.kendali_deteksi()
    assert sah is True


def test_kendali_deteksi_angka_terkunci():
    _, rinci = bp.kendali_deteksi()
    assert rinci["hidup_kecil"] == bp.DETEKSI_HIDUP_KECIL
    assert rinci["sebagian"] == bp.DETEKSI_SEBAGIAN
    assert rinci["nisbah_rata"] == bp.DETEKSI_NISBAH
    assert rinci["total_byte"] == bp.DETEKSI_TOTAL_BYTE


def test_ringkaskan_medan_pokok():
    status, byte_parquet = semesta()
    ringkas = bp.ringkaskan(status, byte_parquet, ambang_hidup=250)
    assert ringkas["penyebut"] == 5
    assert ringkas["simbol"] == 2
    assert ringkas["total_byte"] == 1500
    assert ringkas["cacah_hidup_byte_kecil"] == 2
    assert ringkas["cacah_hidup_kecil_sebagian"] == 2


def test_ringkaskan_daftar_dan_nisbah():
    status, byte_parquet = semesta()
    ringkas = bp.ringkaskan(status, byte_parquet, ambang_hidup=250)
    assert len(ringkas["daftar_hidup_kecil"]) == 2
    assert ringkas["nisbah_rata"] == 0.75
    assert ringkas["bagian_hidup_kecil_sebagian"] == 1.0


def test_uji_butir1_menang():
    hasil = bp.uji_r309(ringkas_lulus())
    assert hasil["butir1"]["menang"] is True
    assert hasil["butir1"]["teradjudikasi"] is True


def test_uji_butir1_kalah():
    ringkas = ringkas_lulus()
    ringkas["cacah_hidup_kecil_sebagian"] = 21
    assert bp.uji_r309(ringkas)["butir1"]["menang"] is False


def test_uji_butir1_penyebut_nol():
    ringkas = ringkas_lulus()
    ringkas["cacah_hidup_byte_kecil"] = 0
    butir1 = bp.uji_r309(ringkas)["butir1"]
    assert butir1["teradjudikasi"] is False
    assert butir1["menang"] is False


def test_uji_butir2_menang():
    hasil = bp.uji_r309(ringkas_lulus())
    assert hasil["butir2"]["menang"] is True


def test_uji_butir2_kalah():
    ringkas = ringkas_lulus()
    ringkas["nisbah_rata"] = 0.9
    assert bp.uji_r309(ringkas)["butir2"]["menang"] is False


def test_uji_butir2_null_tidak_teradjudikasi():
    ringkas = ringkas_lulus()
    ringkas["nisbah_rata"] = None
    butir2 = bp.uji_r309(ringkas)["butir2"]
    assert butir2["teradjudikasi"] is False
    assert butir2["menang"] is False


def test_uji_butir3_menang():
    hasil = bp.uji_r309(ringkas_lulus())
    assert hasil["butir3_menang"] is True
    assert hasil["butir3"]["cacah_medan_selisih"] == 8


def test_uji_butir3_kalah_bila_selisih():
    ringkas = ringkas_lulus()
    ringkas["selisih_cacah_mati"] = 1
    assert bp.uji_r309(ringkas)["butir3_menang"] is False


def test_kode_keluar_nol():
    assert bp.kode_keluar(bp.uji_r309(ringkas_lulus())) == 0


def test_kode_keluar_satu():
    ringkas = ringkas_lulus()
    ringkas["kendali_data_sah"] = False
    assert bp.kode_keluar(bp.uji_r309(ringkas)) == 1


def test_tetapan_terkunci_pita():
    assert bp.R309_PITA_BUTIR_1 == (22, 38)
    assert bp.R309_PITA_BUTIR_2 == (0.10, 0.60)


def test_tetapan_terkunci_ambang_dan_tepi():
    assert bp.AMBANG_HIDUP_KECIL == 97634
    assert bp.BULAN_TEPI == "2026-06"


def test_tetapan_terkunci_invarian():
    assert bp.INVARIAN["penyebut"] == 19586
    assert bp.INVARIAN["simbol"] == 787
    assert bp.INVARIAN["cacah_hidup_byte_kecil"] == 38
    assert bp.INVARIAN["total_byte"] == 32706262375


def test_batas_baris_laporan():
    assert bp.BATAS_BARIS_LAPORAN == 40
