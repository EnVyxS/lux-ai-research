"""Uji `lux_ai.serapan.kebangkitan` V1 — 54 fungsi, tanpa `parametrize`.

Aturan 57 dan penangkal KC-19: nama setiap fungsi ditulis BERNOMOR di sini
SEBELUM push, dan nomor terakhirnya dipakai sebagai cacahan ramalan R-232
(396 + 54 = 450 butir). Tidak ada `parametrize` di berkas ini, sehingga cacah
fungsi sama dengan cacah butir.

 1 nama_keluaran_menyebut_reports_kebangkitan
 2 nama_ringkas_berbeda_dan_berakhiran_ringkas
 3 sidik_kode_stabil_dua_pemanggilan
 4 sidik_kode_enam_puluh_empat_heksadesimal
 5 berkas_dicap_lima_dan_memuat_dirinya
 6 versi_satu
 7 angka_tercatat_sesuai_run_terverifikasi
 8 bulan_setelah_menyeberang_tahun
 9 bulan_setelah_di_tengah_tahun
10 bulan_setelah_januari
11 peta_status_mengelompokkan_per_simbol
12 peta_status_menghasilkan_string
13 rentetan_status_menggabungkan_bulan_bersambung
14 rentetan_status_memutus_pada_jurang_kalender
15 rentetan_status_memutus_pada_perubahan_status
16 rentetan_status_kosong_pada_peta_kosong
17 kebangkitan_simbol_menemukan_mati_lalu_hidup
18 kebangkitan_simbol_mencacah_panjang_mati
19 kebangkitan_simbol_menandai_ada_hidup_sebelum
20 kebangkitan_simbol_tanpa_hidup_sesudah_kosong
21 kebangkitan_simbol_melewati_sepi_di_antara
22 kebangkitan_simbol_tanpa_hidup_sebelum_tetap_tercatat
23 kebangkitan_simbol_dua_peristiwa
24 kebangkitan_simbol_hanya_hidup_kosong
25 daftar_kebangkitan_hanya_simbol_yang_bangkit
26 daftar_kebangkitan_urut_abjad
27 daftar_kebangkitan_mencacah_peristiwa_dan_bulan
28 uji_h_a012_menang_dengan_dua_simbol
29 uji_h_a012_satu_simbol_belum_menang
30 uji_h_a012_penyebut_nol_tidak_terukur
31 uji_h_a012_mencacah_bangkit_penuh
32 bulan_hidup_terakhir_memakai_hidup_terakhir
33 bulan_hidup_terakhir_null_bila_tak_pernah_hidup
34 cocokkan_kohort_ekor_seluruhnya_cocok
35 cocokkan_kohort_ekor_menandai_beda
36 cocokkan_kohort_ekor_menandai_hilang
37 kohort_ekor_tercatat_sepuluh_nama
38 sebaran_mati_tahun_mencacah_per_tahun
39 sebaran_mati_tahun_mengabaikan_bukan_mati
40 sebaran_mati_simbol_urut_menurun
41 sebaran_mati_simbol_membatasi_teratas
42 sebaran_mati_simbol_mencacah_total
43 kode_keluar_nol_pada_ringkasan_bersih
44 kode_keluar_dua_bila_sidik_tak_seragam
45 kode_keluar_dua_bila_laporan_kurang
46 kode_keluar_dua_bila_kunci_ganda
47 kode_keluar_dua_bila_kendali_tak_sah
48 kode_keluar_dua_bila_selisih_penyebut_bukan_nol
49 kode_keluar_dua_bila_selisih_mati_bukan_nol
50 kode_keluar_nol_walau_h_a012_kalah
51 cacah_bulan_rentang_satu_bulan
52 cacah_bulan_rentang_btcst_lima_puluh_tiga
53 cacah_bulan_rentang_terbalik_nol
54 uji_h_a011_dipakai_ulang_untuk_btcst
"""

from __future__ import annotations

from lux_ai.serapan import kebangkitan, kehidupan, lubang_tengah

MATI = kehidupan.STATUS_MATI
SEPI = kehidupan.STATUS_SEPI
HIDUP = kehidupan.STATUS_HIDUP


def ringkasan_bersih() -> dict:
    return {
        "sidik_seragam": True,
        "cacah_laporan_dibaca": 8,
        "total_pecahan": 8,
        "cacah_kunci_ganda": 0,
        "kendali_sah": True,
        "selisih_penyebut": 0,
        "selisih_mati": 0,
    }


def test_nama_keluaran_menyebut_reports_kebangkitan() -> None:
    assert kebangkitan.nama_keluaran() == "reports/kebangkitan.json"


def test_nama_ringkas_berbeda_dan_berakhiran_ringkas() -> None:
    assert kebangkitan.nama_ringkas() != kebangkitan.nama_keluaran()
    assert kebangkitan.nama_ringkas().endswith("_ringkas.json")


def test_sidik_kode_stabil_dua_pemanggilan() -> None:
    assert kebangkitan.sidik_kode() == kebangkitan.sidik_kode()


def test_sidik_kode_enam_puluh_empat_heksadesimal() -> None:
    sidik = kebangkitan.sidik_kode()
    assert len(sidik) == 64
    int(sidik, 16)


def test_berkas_dicap_lima_dan_memuat_dirinya() -> None:
    assert len(kebangkitan.BERKAS_DICAP) == 5
    assert "kebangkitan.py" in kebangkitan.BERKAS_DICAP


def test_versi_satu() -> None:
    assert kebangkitan.VERSI == 1


def test_angka_tercatat_sesuai_run_terverifikasi() -> None:
    assert kebangkitan.PENYEBUT_TERCATAT == 19586
    assert kebangkitan.MATI_TERCATAT == 1401


def test_bulan_setelah_menyeberang_tahun() -> None:
    assert kebangkitan.bulan_setelah("2025-12") == "2026-01"


def test_bulan_setelah_di_tengah_tahun() -> None:
    assert kebangkitan.bulan_setelah("2025-07") == "2025-08"


def test_bulan_setelah_januari() -> None:
    assert kebangkitan.bulan_setelah("2020-01") == "2020-02"


def test_peta_status_mengelompokkan_per_simbol() -> None:
    peta = kebangkitan.peta_status(
        {("A", "2025-01"): HIDUP, ("A", "2025-02"): MATI, ("B", "2025-01"): MATI}
    )
    assert sorted(peta) == ["A", "B"]
    assert peta["A"] == {"2025-01": HIDUP, "2025-02": MATI}


def test_peta_status_menghasilkan_string() -> None:
    peta = kebangkitan.peta_status({("A", "2025-01"): HIDUP})
    assert isinstance(list(peta["A"])[0], str)
    assert isinstance(peta["A"]["2025-01"], str)


def test_rentetan_status_menggabungkan_bulan_bersambung() -> None:
    rentetan = kebangkitan.rentetan_status(
        {"2025-01": MATI, "2025-02": MATI, "2025-03": MATI}
    )
    assert len(rentetan) == 1
    assert rentetan[0]["panjang"] == 3
    assert rentetan[0]["mulai"] == "2025-01"
    assert rentetan[0]["sampai"] == "2025-03"


def test_rentetan_status_memutus_pada_jurang_kalender() -> None:
    rentetan = kebangkitan.rentetan_status({"2025-01": MATI, "2025-03": MATI})
    assert len(rentetan) == 2
    assert [r["panjang"] for r in rentetan] == [1, 1]


def test_rentetan_status_memutus_pada_perubahan_status() -> None:
    rentetan = kebangkitan.rentetan_status({"2025-01": MATI, "2025-02": HIDUP})
    assert [r["status"] for r in rentetan] == [MATI, HIDUP]


def test_rentetan_status_kosong_pada_peta_kosong() -> None:
    assert kebangkitan.rentetan_status({}) == []


def test_kebangkitan_simbol_menemukan_mati_lalu_hidup() -> None:
    peristiwa = kebangkitan.kebangkitan_simbol(
        {"2025-01": HIDUP, "2025-02": MATI, "2025-03": HIDUP}
    )
    assert len(peristiwa) == 1
    assert peristiwa[0]["bulan_mati_terakhir"] == "2025-02"
    assert peristiwa[0]["bulan_hidup_pertama_sesudah"] == "2025-03"


def test_kebangkitan_simbol_mencacah_panjang_mati() -> None:
    peristiwa = kebangkitan.kebangkitan_simbol(
        {
            "2025-01": HIDUP,
            "2025-02": MATI,
            "2025-03": MATI,
            "2025-04": MATI,
            "2025-05": HIDUP,
        }
    )
    assert len(peristiwa) == 1
    assert peristiwa[0]["panjang_mati"] == 3
    assert peristiwa[0]["bulan_mati_mulai"] == "2025-02"


def test_kebangkitan_simbol_menandai_ada_hidup_sebelum() -> None:
    peristiwa = kebangkitan.kebangkitan_simbol(
        {"2025-01": HIDUP, "2025-02": MATI, "2025-03": HIDUP}
    )
    assert peristiwa[0]["ada_hidup_sebelum"] is True


def test_kebangkitan_simbol_tanpa_hidup_sesudah_kosong() -> None:
    assert (
        kebangkitan.kebangkitan_simbol(
            {"2025-01": HIDUP, "2025-02": MATI, "2025-03": MATI}
        )
        == []
    )


def test_kebangkitan_simbol_melewati_sepi_di_antara() -> None:
    peristiwa = kebangkitan.kebangkitan_simbol(
        {"2025-01": HIDUP, "2025-02": MATI, "2025-03": SEPI, "2025-04": HIDUP}
    )
    assert len(peristiwa) == 1
    assert peristiwa[0]["cacah_bulan_antara"] == 1


def test_kebangkitan_simbol_tanpa_hidup_sebelum_tetap_tercatat() -> None:
    peristiwa = kebangkitan.kebangkitan_simbol({"2025-01": MATI, "2025-02": HIDUP})
    assert len(peristiwa) == 1
    assert peristiwa[0]["ada_hidup_sebelum"] is False


def test_kebangkitan_simbol_dua_peristiwa() -> None:
    peristiwa = kebangkitan.kebangkitan_simbol(
        {
            "2025-01": HIDUP,
            "2025-02": MATI,
            "2025-03": HIDUP,
            "2025-04": MATI,
            "2025-05": HIDUP,
        }
    )
    assert len(peristiwa) == 2


def test_kebangkitan_simbol_hanya_hidup_kosong() -> None:
    assert kebangkitan.kebangkitan_simbol({"2025-01": HIDUP, "2025-02": HIDUP}) == []


def test_daftar_kebangkitan_hanya_simbol_yang_bangkit() -> None:
    baris = kebangkitan.daftar_kebangkitan(
        {
            ("A", "2025-01"): HIDUP,
            ("A", "2025-02"): MATI,
            ("A", "2025-03"): HIDUP,
            ("B", "2025-01"): HIDUP,
            ("B", "2025-02"): MATI,
        }
    )
    assert [r["simbol"] for r in baris] == ["A"]


def test_daftar_kebangkitan_urut_abjad() -> None:
    baris = kebangkitan.daftar_kebangkitan(
        {
            ("Z", "2025-01"): MATI,
            ("Z", "2025-02"): HIDUP,
            ("A", "2025-01"): MATI,
            ("A", "2025-02"): HIDUP,
        }
    )
    assert [r["simbol"] for r in baris] == ["A", "Z"]


def test_daftar_kebangkitan_mencacah_peristiwa_dan_bulan() -> None:
    baris = kebangkitan.daftar_kebangkitan(
        {
            ("A", "2025-01"): HIDUP,
            ("A", "2025-02"): MATI,
            ("A", "2025-03"): HIDUP,
        }
    )
    assert baris[0]["cacah_peristiwa"] == 1
    assert baris[0]["cacah_bulan"] == 3
    assert baris[0]["bulan_pertama"] == "2025-01"
    assert baris[0]["bulan_terakhir"] == "2025-03"
    assert baris[0]["bangkit_penuh"] is True


def test_uji_h_a012_menang_dengan_dua_simbol() -> None:
    baris = kebangkitan.daftar_kebangkitan(
        {
            ("A", "2025-01"): HIDUP,
            ("A", "2025-02"): MATI,
            ("A", "2025-03"): HIDUP,
            ("B", "2025-01"): HIDUP,
            ("B", "2025-02"): MATI,
            ("B", "2025-03"): HIDUP,
        }
    )
    hasil = kebangkitan.uji_h_a012(baris, 2)
    assert hasil["menang"] is True
    assert hasil["cacah_simbol_bangkit"] == 2


def test_uji_h_a012_satu_simbol_belum_menang() -> None:
    baris = kebangkitan.daftar_kebangkitan(
        {
            ("A", "2025-01"): HIDUP,
            ("A", "2025-02"): MATI,
            ("A", "2025-03"): HIDUP,
        }
    )
    hasil = kebangkitan.uji_h_a012(baris, 787)
    assert hasil["cacah_simbol_bangkit"] == 1
    assert hasil["menang"] is False
    assert hasil["terukur"] is True


def test_uji_h_a012_penyebut_nol_tidak_terukur() -> None:
    hasil = kebangkitan.uji_h_a012([], 0)
    assert hasil["terukur"] is False
    assert hasil["menang"] is False


def test_uji_h_a012_mencacah_bangkit_penuh() -> None:
    baris = kebangkitan.daftar_kebangkitan(
        {
            ("A", "2025-01"): HIDUP,
            ("A", "2025-02"): MATI,
            ("A", "2025-03"): HIDUP,
            ("B", "2025-01"): MATI,
            ("B", "2025-02"): HIDUP,
        }
    )
    hasil = kebangkitan.uji_h_a012(baris, 2)
    assert hasil["cacah_simbol_bangkit"] == 2
    assert hasil["cacah_simbol_bangkit_penuh"] == 1
    assert hasil["simbol_bangkit_penuh"] == ["A"]


def test_bulan_hidup_terakhir_memakai_hidup_terakhir() -> None:
    peta = kebangkitan.bulan_hidup_terakhir(
        {
            ("A", "2025-01"): HIDUP,
            ("A", "2025-02"): HIDUP,
            ("A", "2025-03"): MATI,
        }
    )
    assert peta["A"] == "2025-02"


def test_bulan_hidup_terakhir_null_bila_tak_pernah_hidup() -> None:
    peta = kebangkitan.bulan_hidup_terakhir({("A", "2025-01"): MATI})
    assert peta["A"] is None


def test_cocokkan_kohort_ekor_seluruhnya_cocok() -> None:
    peta = dict(kebangkitan.KOHORT_EKOR_TERCATAT)
    hasil = kebangkitan.cocokkan_kohort_ekor(peta)
    assert hasil["cacah_cocok"] == 10
    assert hasil["seluruhnya_cocok"] is True


def test_cocokkan_kohort_ekor_menandai_beda() -> None:
    peta = dict(kebangkitan.KOHORT_EKOR_TERCATAT)
    peta["AGIXUSDT"] = "2026-01"
    hasil = kebangkitan.cocokkan_kohort_ekor(peta)
    assert hasil["cacah_beda"] == 1
    assert hasil["cacah_cocok"] == 9
    assert hasil["seluruhnya_cocok"] is False


def test_cocokkan_kohort_ekor_menandai_hilang() -> None:
    peta = dict(kebangkitan.KOHORT_EKOR_TERCATAT)
    del peta["DARUSDT"]
    hasil = kebangkitan.cocokkan_kohort_ekor(peta)
    assert hasil["cacah_hilang"] == 1
    assert hasil["cacah_cocok"] == 9


def test_kohort_ekor_tercatat_sepuluh_nama() -> None:
    assert len(kebangkitan.KOHORT_EKOR_TERCATAT) == 10
    assert all(len(b) == 7 for b in kebangkitan.KOHORT_EKOR_TERCATAT.values())


def test_sebaran_mati_tahun_mencacah_per_tahun() -> None:
    sebaran = kebangkitan.sebaran_mati_tahun(
        {
            ("A", "2024-01"): MATI,
            ("A", "2024-02"): MATI,
            ("B", "2025-01"): MATI,
        }
    )
    assert sebaran == {"2024": 2, "2025": 1}


def test_sebaran_mati_tahun_mengabaikan_bukan_mati() -> None:
    sebaran = kebangkitan.sebaran_mati_tahun(
        {("A", "2024-01"): HIDUP, ("A", "2024-02"): SEPI}
    )
    assert sebaran == {}


def test_sebaran_mati_simbol_urut_menurun() -> None:
    hasil = kebangkitan.sebaran_mati_simbol(
        {
            ("A", "2024-01"): MATI,
            ("B", "2024-01"): MATI,
            ("B", "2024-02"): MATI,
        }
    )
    assert [r["simbol"] for r in hasil["teratas"]] == ["B", "A"]


def test_sebaran_mati_simbol_membatasi_teratas() -> None:
    hasil = kebangkitan.sebaran_mati_simbol(
        {("A", "2024-01"): MATI, ("B", "2024-01"): MATI}, teratas=1
    )
    assert hasil["cacah_teratas"] == 1
    assert len(hasil["teratas"]) == 1
    assert hasil["cacah_simbol_bermati"] == 2


def test_sebaran_mati_simbol_mencacah_total() -> None:
    hasil = kebangkitan.sebaran_mati_simbol(
        {
            ("A", "2024-01"): MATI,
            ("A", "2024-02"): MATI,
            ("B", "2024-01"): HIDUP,
        }
    )
    assert hasil["cacah_mati_total"] == 2
    assert hasil["cacah_simbol_bermati"] == 1


def test_kode_keluar_nol_pada_ringkasan_bersih() -> None:
    assert kebangkitan.kode_keluar(ringkasan_bersih()) == 0


def test_kode_keluar_dua_bila_sidik_tak_seragam() -> None:
    r = ringkasan_bersih()
    r["sidik_seragam"] = False
    assert kebangkitan.kode_keluar(r) == 2


def test_kode_keluar_dua_bila_laporan_kurang() -> None:
    r = ringkasan_bersih()
    r["cacah_laporan_dibaca"] = 7
    assert kebangkitan.kode_keluar(r) == 2


def test_kode_keluar_dua_bila_kunci_ganda() -> None:
    r = ringkasan_bersih()
    r["cacah_kunci_ganda"] = 1
    assert kebangkitan.kode_keluar(r) == 2


def test_kode_keluar_dua_bila_kendali_tak_sah() -> None:
    r = ringkasan_bersih()
    r["kendali_sah"] = False
    assert kebangkitan.kode_keluar(r) == 2


def test_kode_keluar_dua_bila_selisih_penyebut_bukan_nol() -> None:
    r = ringkasan_bersih()
    r["selisih_penyebut"] = -12
    assert kebangkitan.kode_keluar(r) == 2


def test_kode_keluar_dua_bila_selisih_mati_bukan_nol() -> None:
    r = ringkasan_bersih()
    r["selisih_mati"] = 3
    assert kebangkitan.kode_keluar(r) == 2


def test_kode_keluar_nol_walau_h_a012_kalah() -> None:
    r = ringkasan_bersih()
    r["h_a012_menang"] = False
    r["cacah_simbol_bangkit"] = 1
    assert kebangkitan.kode_keluar(r) == 0


def test_cacah_bulan_rentang_satu_bulan() -> None:
    assert kebangkitan.cacah_bulan_rentang("2026-01", "2026-01") == 1


def test_cacah_bulan_rentang_btcst_lima_puluh_tiga() -> None:
    assert kebangkitan.cacah_bulan_rentang("2022-02", "2026-06") == 53
    assert kebangkitan.cacah_bulan_rentang(*kebangkitan.RENTANG_BTCST) == 53


def test_cacah_bulan_rentang_terbalik_nol() -> None:
    assert kebangkitan.cacah_bulan_rentang("2026-06", "2026-01") == 0


def test_uji_h_a011_dipakai_ulang_untuk_btcst() -> None:
    status = {
        ("BTCSTUSDT", "2022-01"): MATI,
        ("BTCSTUSDT", "2022-02"): HIDUP,
        ("BTCSTUSDT", "2022-03"): MATI,
    }
    hasil = lubang_tengah.uji_h_a011(
        status,
        simbol=kebangkitan.SIMBOL_TENGAH_LAIN,
        rentang=kebangkitan.RENTANG_BTCST,
    )
    assert hasil["simbol"] == "BTCSTUSDT"
    assert hasil["cacah_bulan"] == 2
    assert hasil["cacah_hidup"] == 1
    assert hasil["menang"] is True
