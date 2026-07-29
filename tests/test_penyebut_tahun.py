"""Uji `penyebut_tahun` V1 - 44 butir, seluruhnya atas data sintetis.

Daftar BERNOMOR (aturan 57); tidak ada `parametrize`, jadi cacah butir = cacah
fungsi = **44**. Bersama 450 butir terverifikasi pada run 30444539002, CI pada
commit yang memuat berkas ini diramalkan **494** (R-238).

1. test_01_nama_keluaran_tetap
2. test_02_nama_ringkas_berbeda
3. test_03_sidik_kode_panjang
4. test_04_sidik_kode_stabil
5. test_05_tahun_dari_bulan
6. test_06_tahun_dari_bulan_desember
7. test_07_penyebut_per_tahun_kosong
8. test_08_penyebut_per_tahun_cacah
9. test_09_penyebut_per_tahun_terurut
10. test_10_penyebut_per_tahun_jumlah_sama
11. test_11_mati_per_tahun_hanya_mati
12. test_12_mati_per_tahun_definisi_satu
13. test_13_bagian_baris_lengkap
14. test_14_bagian_tahun_tanpa_mati_tetap_didaftar
15. test_15_bagian_nilai_benar
16. test_16_bagian_terukur_true
17. test_17_bagian_tahun_tertinggi
18. test_18_bagian_jumlah_penyebut
19. test_19_bagian_kosong_tanpa_tahun_tertinggi
20. test_20_nama_settled_dua_bentuk
21. test_21_nama_settled_tanpa_ganda
22. test_22_bulan_simbol_terurut
23. test_23_bulan_simbol_asing_kosong
24. test_24_h_a013_baris_enam
25. test_25_h_a013_hadir_di_penyebut
26. test_26_h_a013_hadir_false
27. test_27_h_a013_saudara_ditemukan
28. test_28_h_a013_saudara_bentuk_garis_bawah
29. test_29_h_a013_cocok_bulan_true
30. test_30_h_a013_cocok_bulan_false_bulan_lain
31. test_31_h_a013_hadir_mengalahkan_cocok
32. test_32_h_a013_sebab_membedakan
33. test_33_h_a013_sebab_tak_pernah_kosong
34. test_34_h_a013_menang_pada_ambang
35. test_35_h_a013_menang_false_di_bawah_ambang
36. test_36_h_a013_terukur_false_bila_kosong
37. test_37_rinci_bersambung_dua_baris
38. test_38_rinci_bnx_bulan
39. test_39_rinci_bnx_lubang
40. test_40_rinci_bnx_tanpa_klaim_kc15
41. test_41_bulan_hidup_terakhir_penuh
42. test_42_kode_keluar_nol
43. test_43_kode_keluar_dua_bila_selisih_jumlah_tahun
44. test_44_ringkas_tanpa_peta_penuh
"""

from __future__ import annotations

from lux_ai.serapan import kehidupan, penyebut_tahun

MATI = kehidupan.STATUS_MATI
HIDUP = kehidupan.STATUS_HIDUP
SEPI = kehidupan.STATUS_SEPI


def contoh():
    return {
        ("AUSDT", "2025-01"): HIDUP,
        ("AUSDT", "2025-02"): MATI,
        ("AUSDT", "2025-03"): HIDUP,
        ("BUSDT", "2026-01"): MATI,
        ("BUSDT", "2026-02"): HIDUP,
    }


def sehat():
    return {
        "sidik_seragam": True,
        "cacah_laporan_dibaca": penyebut_tahun.TOTAL_PECAHAN,
        "total_pecahan": penyebut_tahun.TOTAL_PECAHAN,
        "cacah_kunci_ganda": 0,
        "kendali_sah": True,
        "selisih_penyebut": 0,
        "selisih_mati": 0,
        "selisih_jumlah_tahun": 0,
    }


def test_01_nama_keluaran_tetap():
    assert penyebut_tahun.nama_keluaran() == "reports/penyebut_tahun.json"


def test_02_nama_ringkas_berbeda():
    assert penyebut_tahun.nama_ringkas() != penyebut_tahun.nama_keluaran()


def test_03_sidik_kode_panjang():
    assert len(penyebut_tahun.sidik_kode()) == 64


def test_04_sidik_kode_stabil():
    assert penyebut_tahun.sidik_kode() == penyebut_tahun.sidik_kode()


def test_05_tahun_dari_bulan():
    assert penyebut_tahun.tahun_dari_bulan("2025-07") == "2025"


def test_06_tahun_dari_bulan_desember():
    assert penyebut_tahun.tahun_dari_bulan("2026-12") == "2026"


def test_07_penyebut_per_tahun_kosong():
    assert penyebut_tahun.penyebut_per_tahun({}) == {}


def test_08_penyebut_per_tahun_cacah():
    assert penyebut_tahun.penyebut_per_tahun(contoh()) == {"2025": 3, "2026": 2}


def test_09_penyebut_per_tahun_terurut():
    kunci = list(penyebut_tahun.penyebut_per_tahun(contoh()))
    assert kunci == sorted(kunci)


def test_10_penyebut_per_tahun_jumlah_sama():
    st = contoh()
    assert sum(penyebut_tahun.penyebut_per_tahun(st).values()) == len(st)


def test_11_mati_per_tahun_hanya_mati():
    assert penyebut_tahun.mati_per_tahun(contoh()) == {"2025": 1, "2026": 1}


def test_12_mati_per_tahun_definisi_satu():
    from lux_ai.serapan import kebangkitan

    st = contoh()
    assert penyebut_tahun.mati_per_tahun(st) == kebangkitan.sebaran_mati_tahun(st)


def test_13_bagian_baris_lengkap():
    tabel = penyebut_tahun.bagian_mati_per_tahun(contoh())
    assert tabel["cacah_tahun"] == 2
    assert [b["tahun"] for b in tabel["baris"]] == ["2025", "2026"]


def test_14_bagian_tahun_tanpa_mati_tetap_didaftar():
    st = {("AUSDT", "2024-01"): HIDUP}
    tabel = penyebut_tahun.bagian_mati_per_tahun(st)
    assert tabel["baris"][0]["mati"] == 0
    assert tabel["baris"][0]["bagian"] == 0.0


def test_15_bagian_nilai_benar():
    tabel = penyebut_tahun.bagian_mati_per_tahun(contoh())
    peta = {b["tahun"]: b["bagian"] for b in tabel["baris"]}
    assert peta["2025"] == round(1 / 3, 6)
    assert peta["2026"] == 0.5


def test_16_bagian_terukur_true():
    tabel = penyebut_tahun.bagian_mati_per_tahun(contoh())
    assert all(b["terukur"] for b in tabel["baris"])


def test_17_bagian_tahun_tertinggi():
    tabel = penyebut_tahun.bagian_mati_per_tahun(contoh())
    assert tabel["tahun_tertinggi"] == "2026"
    assert tabel["bagian_tertinggi"] == 0.5


def test_18_bagian_jumlah_penyebut():
    st = contoh()
    tabel = penyebut_tahun.bagian_mati_per_tahun(st)
    assert tabel["jumlah_penyebut"] == len(st)
    assert tabel["jumlah_mati"] == 2


def test_19_bagian_kosong_tanpa_tahun_tertinggi():
    tabel = penyebut_tahun.bagian_mati_per_tahun({})
    assert tabel["tahun_tertinggi"] is None
    assert tabel["bagian_tertinggi"] is None


def test_20_nama_settled_dua_bentuk():
    assert penyebut_tahun.nama_settled("CTKUSDT") == [
        "CTKUSDTSETTLED",
        "CTKUSDT_SETTLED",
    ]


def test_21_nama_settled_tanpa_ganda():
    nama = penyebut_tahun.nama_settled("XUSDT")
    assert len(nama) == len(set(nama))


def test_22_bulan_simbol_terurut():
    assert penyebut_tahun.bulan_simbol(contoh(), "AUSDT") == [
        "2025-01",
        "2025-02",
        "2025-03",
    ]


def test_23_bulan_simbol_asing_kosong():
    assert penyebut_tahun.bulan_simbol(contoh(), "TIDAKADAUSDT") == []


def test_24_h_a013_baris_enam():
    hasil = penyebut_tahun.uji_h_a013({})
    assert hasil["cacah_peralihan"] == 6
    assert len(hasil["baris"]) == 6


def test_25_h_a013_hadir_di_penyebut():
    st = {("CTKUSDT", "2025-04"): HIDUP}
    hasil = penyebut_tahun.uji_h_a013(st, peralihan=(("CTKUSDT", "2025-04"),))
    assert hasil["baris"][0]["hadir_di_penyebut"] is True
    assert hasil["cacah_hadir_di_penyebut"] == 1


def test_26_h_a013_hadir_false():
    st = {("CTKUSDT", "2025-01"): MATI}
    hasil = penyebut_tahun.uji_h_a013(st, peralihan=(("CTKUSDT", "2025-04"),))
    assert hasil["baris"][0]["hadir_di_penyebut"] is False


def test_27_h_a013_saudara_ditemukan():
    st = {("CTKUSDTSETTLED", "2025-04"): SEPI}
    hasil = penyebut_tahun.uji_h_a013(st, peralihan=(("CTKUSDT", "2025-04"),))
    assert hasil["baris"][0]["saudara_ditemukan"] == ["CTKUSDTSETTLED"]
    assert hasil["cacah_saudara_ditemukan"] == 1


def test_28_h_a013_saudara_bentuk_garis_bawah():
    st = {("CVCUSDT_SETTLED", "2025-05"): SEPI}
    hasil = penyebut_tahun.uji_h_a013(st, peralihan=(("CVCUSDT", "2025-05"),))
    assert hasil["baris"][0]["saudara_ditemukan"] == ["CVCUSDT_SETTLED"]


def test_29_h_a013_cocok_bulan_true():
    st = {("SLPUSDTSETTLED", "2025-07"): MATI}
    hasil = penyebut_tahun.uji_h_a013(st, peralihan=(("SLPUSDT", "2025-07"),))
    assert hasil["baris"][0]["cocok_bulan"] is True
    assert hasil["baris"][0]["sebab"] == penyebut_tahun.SEBAB_SAUDARA_COCOK


def test_30_h_a013_cocok_bulan_false_bulan_lain():
    st = {("SLPUSDTSETTLED", "2024-01"): MATI}
    hasil = penyebut_tahun.uji_h_a013(st, peralihan=(("SLPUSDT", "2025-07"),))
    assert hasil["baris"][0]["cocok_bulan"] is False
    assert hasil["baris"][0]["sebab"] == penyebut_tahun.SEBAB_SAUDARA_LAIN


def test_31_h_a013_hadir_mengalahkan_cocok():
    st = {
        ("LITUSDT", "2025-12"): HIDUP,
        ("LITUSDTSETTLED", "2025-12"): MATI,
    }
    hasil = penyebut_tahun.uji_h_a013(st, peralihan=(("LITUSDT", "2025-12"),))
    assert hasil["baris"][0]["sebab"] == penyebut_tahun.SEBAB_HADIR
    assert hasil["cacah_cocok_bulan"] == 0


def test_32_h_a013_sebab_membedakan():
    st = {
        ("CTKUSDT", "2025-04"): HIDUP,
        ("CVCUSDTSETTLED", "2025-05"): MATI,
        ("CVXUSDTSETTLED", "2020-01"): MATI,
    }
    peralihan = (
        ("CTKUSDT", "2025-04"),
        ("CVCUSDT", "2025-05"),
        ("CVXUSDT", "2025-07"),
        ("MAVIAUSDT", "2025-03"),
    )
    hasil = penyebut_tahun.uji_h_a013(st, peralihan=peralihan)
    assert len(hasil["sebab_terpakai"]) == 4
    assert hasil["definisi_dapat_dibedakan"] is True


def test_33_h_a013_sebab_tak_pernah_kosong():
    hasil = penyebut_tahun.uji_h_a013({})
    assert all(str(b["sebab"]) for b in hasil["baris"])


def test_34_h_a013_menang_pada_ambang():
    st = {}
    for simbol, bulan in penyebut_tahun.PERALIHAN[: penyebut_tahun.AMBANG_MENANG]:
        st[(simbol + "SETTLED", bulan)] = MATI
    hasil = penyebut_tahun.uji_h_a013(st)
    assert hasil["cacah_cocok_bulan"] == penyebut_tahun.AMBANG_MENANG
    assert hasil["menang"] is True


def test_35_h_a013_menang_false_di_bawah_ambang():
    simbol, bulan = penyebut_tahun.PERALIHAN[0]
    hasil = penyebut_tahun.uji_h_a013({(simbol + "SETTLED", bulan): MATI})
    assert hasil["cacah_cocok_bulan"] == 1
    assert hasil["menang"] is False


def test_36_h_a013_terukur_false_bila_kosong():
    hasil = penyebut_tahun.uji_h_a013({})
    assert hasil["terukur"] is False
    assert hasil["menang"] is False


def test_37_rinci_bersambung_dua_baris():
    st = {
        ("ICPUSDT", "2022-09"): HIDUP,
        ("ICPUSDT_SETTLED", "2022-09"): MATI,
    }
    baris = penyebut_tahun.rinci_bersambung(st)
    assert [b["simbol"] for b in baris] == ["ICPUSDT", "TLMUSDT"]
    assert baris[0]["saudara_ditemukan"] == ["ICPUSDT_SETTLED"]
    assert baris[1]["cacah_bulan"] == 0


def test_38_rinci_bnx_bulan():
    st = {
        ("BNXUSDT", "2022-04"): MATI,
        ("BNXUSDT", "2022-05"): HIDUP,
        ("BNXUSDTSETTLED", "2023-02"): MATI,
    }
    hasil = penyebut_tahun.rinci_bnx(st)
    assert hasil["cacah_bulan"] == 2
    assert hasil["bulan_saudara"] == ["2023-02"]


def test_39_rinci_bnx_lubang():
    st = {("BNXUSDT", "2022-04"): MATI}
    hasil = penyebut_tahun.rinci_bnx(st)
    assert hasil["cacah_lubang"] == 3
    assert hasil["cacah_lubang_ada_di_penyebut"] == 1
    assert hasil["lubang"][0]["status"] == MATI
    assert hasil["lubang"][1]["status"] is None


def test_40_rinci_bnx_tanpa_klaim_kc15():
    assert penyebut_tahun.rinci_bnx({})["klaim_kc15"] is False


def test_41_bulan_hidup_terakhir_penuh():
    st = dict(contoh())
    st[("CUSDT", "2024-01")] = MATI
    peta = penyebut_tahun.bulan_hidup_terakhir_penuh(st)
    assert peta["AUSDT"] == "2025-03"
    assert peta["CUSDT"] is None


def test_42_kode_keluar_nol():
    assert penyebut_tahun.kode_keluar(sehat()) == 0


def test_43_kode_keluar_dua_bila_selisih_jumlah_tahun():
    buruk = sehat()
    buruk["selisih_jumlah_tahun"] = 1
    assert penyebut_tahun.kode_keluar(buruk) == 2


def test_44_ringkas_tanpa_peta_penuh():
    laporan = {
        "versi_penyebut_tahun": 1,
        "h_a013": {"baris": [{"simbol": "CTKUSDT"}], "menang": True},
        "bulan_hidup_terakhir": {"AUSDT": "2025-03"},
        "ringkasan": {"penyebut_kehidupan": 5},
    }
    kecil = penyebut_tahun.ringkas(laporan)
    assert "bulan_hidup_terakhir" not in kecil
    assert "baris" not in kecil["h_a013"]
    assert kecil["h_a013_baris"] == [{"simbol": "CTKUSDT"}]
