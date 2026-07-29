"""Uji `lux_ai.serapan.bulan_absen` — 32 butir, tanpa satu pun parametrize.

Daftar bernomor (aturan 54, 56, 57); dasar praregistrasi R-290 = 662 + 32 = 694.

 1. test_bulan_ke_indeks_bulan_sah
 2. test_bulan_ke_indeks_bentuk_cacat_menghasilkan_none
 3. test_indeks_ke_bulan_pulang_pergi
 4. test_rentang_bulan_lintas_tahun
 5. test_rentang_bulan_satu_bulan
 6. test_rentang_bulan_terbalik_kosong
 7. test_bulan_sah_membuang_bentuk_cacat
 8. test_bulan_absen_tanpa_lubang
 9. test_bulan_absen_satu_lubang
10. test_bulan_absen_lubang_berurutan
11. test_bulan_absen_daftar_pendek
12. test_bulan_absen_tidak_menghitung_tepi
13. test_baris_simbol_medan_pokok
14. test_baris_simbol_tanpa_bulan_menghasilkan_null
15. test_baris_simbol_konsisten_rentang
16. test_pembeda_gagal_gerbang
17. test_pembeda_tak_diterbitkan_arsip
18. test_pembeda_tanpa_manifes_tak_terukur
19. test_sebaran_pembeda_melapor_kelas_nol
20. test_jumlah_absen_menjumlahkan_baris
21. test_baris_pasangan_settled_lima_belas
22. test_pasangan_absen_sama_dengan_settled
23. test_pasangan_absen_beda_dengan_settled
24. test_pasangan_di_luar_penyebut_tidak_dibuang
25. test_uji_r288_butir_1_menang
26. test_uji_r288_butir_1_gugur_bila_daftar_lain
27. test_uji_r288_butir_2_gugur_di_bawah_ambang
28. test_uji_r288_butir_3_menuntut_dua_belas
29. test_kendali_absen_sah
30. test_kendali_absen_gugur_bila_absen_bukan_nol
31. test_kode_keluar_penggugur_bahan_baku
32. test_kode_keluar_tidak_gugur_bila_ramalan_meleset
"""

from __future__ import annotations

from lux_ai.serapan import bulan_absen as ba
from lux_ai.serapan import silang_settled


def _ringkasan_bersih(**tambahan):
    dasar = {
        "sidik_seragam": True,
        "cacah_laporan_dibaca": ba.TOTAL_PECAHAN,
        "total_pecahan": ba.TOTAL_PECAHAN,
        "cacah_kunci_ganda": 0,
        "kendali_sah": True,
        "selisih_penyebut": 0,
        "cacah_pasangan": len(silang_settled.PASANGAN_SETTLED),
    }
    dasar.update(tambahan)
    return dasar


def _per_baris_ramalan(bnx_absen=3, tunggal_sama=None):
    """Bangun per_baris tiruan yang menaati tabel jurnal 113 §6."""
    tunggal_sama = ba.R288_TUNGGAL if tunggal_sama is None else tunggal_sama
    per_baris = {}
    for simbol in ba.R288_TUNGGAL:
        bulan_settled = silang_settled.PASANGAN_SETTLED[simbol]
        absen = bulan_settled if simbol in tunggal_sama else "1999-01"
        per_baris[simbol] = {
            "simbol": simbol,
            "cacah_bulan_lolos": 20,
            "rentang": 21,
            "bulan_absen": [absen],
            "cacah_absen": 1,
        }
    per_baris[ba.R288_BNX] = {
        "simbol": ba.R288_BNX,
        "cacah_bulan_lolos": 48,
        "rentang": 50,
        "bulan_absen": [f"2022-{i:02d}" for i in range(1, bnx_absen + 1)],
        "cacah_absen": bnx_absen,
    }
    for simbol in ba.R288_NOL:
        per_baris[simbol] = {
            "simbol": simbol,
            "cacah_bulan_lolos": 60,
            "rentang": 60,
            "bulan_absen": [],
            "cacah_absen": 0,
        }
    return per_baris


def test_bulan_ke_indeks_bulan_sah():
    assert ba.bulan_ke_indeks("2021-02") - ba.bulan_ke_indeks("2021-01") == 1
    assert ba.bulan_ke_indeks("2022-01") - ba.bulan_ke_indeks("2021-12") == 1


def test_bulan_ke_indeks_bentuk_cacat_menghasilkan_none():
    for cacat in ("", None, "2021-13", "2021-00", "2021/01", "abcd-ef", "2021-1"):
        assert ba.bulan_ke_indeks(cacat) is None


def test_indeks_ke_bulan_pulang_pergi():
    for bulan in ("2020-01", "2022-12", "2026-06"):
        assert ba.indeks_ke_bulan(ba.bulan_ke_indeks(bulan)) == bulan


def test_rentang_bulan_lintas_tahun():
    assert ba.rentang_bulan("2021-11", "2022-02") == [
        "2021-11",
        "2021-12",
        "2022-01",
        "2022-02",
    ]


def test_rentang_bulan_satu_bulan():
    assert ba.rentang_bulan("2022-05", "2022-05") == ["2022-05"]


def test_rentang_bulan_terbalik_kosong():
    assert ba.rentang_bulan("2022-05", "2022-04") == []
    assert ba.rentang_bulan("2022-05", None) == []


def test_bulan_sah_membuang_bentuk_cacat():
    assert ba.bulan_sah(["2021-03", "cacat", "2021-01", ""]) == ["2021-01", "2021-03"]


def test_bulan_absen_tanpa_lubang():
    assert ba.bulan_absen(["2021-01", "2021-02", "2021-03"]) == []


def test_bulan_absen_satu_lubang():
    assert ba.bulan_absen(["2021-01", "2021-03"]) == ["2021-02"]


def test_bulan_absen_lubang_berurutan():
    assert ba.bulan_absen(["2021-11", "2022-03"]) == ["2021-12", "2022-01", "2022-02"]


def test_bulan_absen_daftar_pendek():
    assert ba.bulan_absen([]) == []
    assert ba.bulan_absen(["2021-01"]) == []


def test_bulan_absen_tidak_menghitung_tepi():
    hasil = ba.bulan_absen(["2021-03", "2021-05"])
    assert hasil == ["2021-04"]
    assert "2021-02" not in hasil
    assert "2021-06" not in hasil


def test_baris_simbol_medan_pokok():
    baris = ba.baris_simbol("LITUSDT", ["2021-01", "2021-03"])
    assert baris["simbol"] == "LITUSDT"
    assert baris["bulan_pertama"] == "2021-01"
    assert baris["bulan_terakhir"] == "2021-03"
    assert baris["rentang"] == 3
    assert baris["cacah_bulan_lolos"] == 2
    assert baris["cacah_absen"] == 1
    assert baris["bulan_absen"] == ["2021-02"]


def test_baris_simbol_tanpa_bulan_menghasilkan_null():
    baris = ba.baris_simbol("XUSDT", [])
    assert baris["rentang"] is None
    assert baris["bulan_pertama"] is None
    assert baris["selisih_rentang"] is None
    assert baris["konsisten_rentang"] is None
    assert baris["cacah_absen"] == 0


def test_baris_simbol_konsisten_rentang():
    baris = ba.baris_simbol("BNXUSDT", ["2022-01", "2022-04", "2022-05"])
    assert baris["selisih_rentang"] == baris["cacah_absen"]
    assert baris["konsisten_rentang"] is True


def test_pembeda_gagal_gerbang():
    assert (
        ba.pembeda_absen("AUSDT", "2022-01", {"AUSDT": {"2022-01"}}, True)
        == ba.GAGAL_GERBANG
    )


def test_pembeda_tak_diterbitkan_arsip():
    assert (
        ba.pembeda_absen("AUSDT", "2022-01", {"AUSDT": {"2021-12"}}, True)
        == ba.TAK_DITERBITKAN
    )
    assert ba.pembeda_absen("BUSDT", "2022-01", {"AUSDT": set()}, True) == (
        ba.TAK_DITERBITKAN
    )


def test_pembeda_tanpa_manifes_tak_terukur():
    assert ba.pembeda_absen("AUSDT", "2022-01", None, False) == ba.TAK_TERUKUR
    assert (
        ba.pembeda_absen("AUSDT", "2022-01", {"AUSDT": {"2022-01"}}, False)
        == ba.TAK_TERUKUR
    )


def test_sebaran_pembeda_melapor_kelas_nol():
    baris = [
        {"pembeda_absen": [{"bulan": "2022-01", "pembeda": ba.GAGAL_GERBANG}]},
        {"pembeda_absen": [{"bulan": "2022-02", "pembeda": ba.GAGAL_GERBANG}]},
    ]
    hasil = ba.sebaran_pembeda(baris)
    assert set(hasil) == set(ba.PEMBEDA)
    assert hasil[ba.GAGAL_GERBANG] == 2
    assert hasil[ba.TAK_DITERBITKAN] == 0
    assert hasil[ba.TAK_TERUKUR] == 0


def test_jumlah_absen_menjumlahkan_baris():
    assert ba.jumlah_absen([{"cacah_absen": 1}, {"cacah_absen": 3}]) == 4
    assert ba.jumlah_absen([]) == 0


def test_baris_pasangan_settled_lima_belas():
    hasil = ba.baris_pasangan_settled(_per_baris_ramalan())
    assert len(hasil) == len(silang_settled.PASANGAN_SETTLED) == 15
    assert sorted(r["simbol"] for r in hasil) == sorted(
        silang_settled.PASANGAN_SETTLED
    )


def test_pasangan_absen_sama_dengan_settled():
    hasil = ba.baris_pasangan_settled(_per_baris_ramalan())
    lit = next(r for r in hasil if r["simbol"] == "LITUSDT")
    assert lit["bulan_settled_terakhir"] == "2025-12"
    assert lit["absen_tunggal"] is True
    assert lit["absen_sama_dengan_settled"] is True
    assert lit["settled_ada_di_absen"] is True


def test_pasangan_absen_beda_dengan_settled():
    per_baris = _per_baris_ramalan(tunggal_sama=())
    hasil = ba.baris_pasangan_settled(per_baris)
    lit = next(r for r in hasil if r["simbol"] == "LITUSDT")
    assert lit["absen_tunggal"] is True
    assert lit["absen_sama_dengan_settled"] is False
    assert lit["settled_ada_di_absen"] is False


def test_pasangan_di_luar_penyebut_tidak_dibuang():
    hasil = ba.baris_pasangan_settled({})
    assert len(hasil) == 15
    assert all(r["ada_di_penyebut"] is False for r in hasil)
    assert all(r["cacah_absen"] == 0 for r in hasil)


def test_uji_r288_butir_1_menang():
    pasangan = ba.baris_pasangan_settled(_per_baris_ramalan())
    uji = ba.uji_r288(pasangan, 12)
    assert uji["butir_1"]["menang"] is True
    assert uji["butir_1"]["mudah"] is True
    assert uji["butir_1"]["cacah_absen_tunggal"] == 9
    assert uji["butir_1"]["cacah_absen_bnx"] == 3
    assert uji["r288_menang"] is True


def test_uji_r288_butir_1_gugur_bila_daftar_lain():
    per_baris = _per_baris_ramalan()
    per_baris["SXPUSDT"] = {
        "simbol": "SXPUSDT",
        "bulan_absen": ["2024-01"],
        "cacah_absen": 1,
    }
    uji = ba.uji_r288(ba.baris_pasangan_settled(per_baris), 13)
    assert uji["butir_1"]["menang"] is False
    assert uji["r288_menang"] is False


def test_uji_r288_butir_2_gugur_di_bawah_ambang():
    sedikit = ba.R288_TUNGGAL[:6]
    pasangan = ba.baris_pasangan_settled(_per_baris_ramalan(tunggal_sama=sedikit))
    uji = ba.uji_r288(pasangan, 12)
    assert uji["butir_2"]["cacah_sama_dengan_settled"] == 6
    assert uji["butir_2"]["ambang"] == 7
    assert uji["butir_2"]["menang"] is False
    assert uji["penggugur_menyala"] is True


def test_uji_r288_butir_3_menuntut_dua_belas():
    pasangan = ba.baris_pasangan_settled(_per_baris_ramalan())
    assert ba.uji_r288(pasangan, 12)["butir_3"]["menang"] is True
    kalah = ba.uji_r288(pasangan, 13)
    assert kalah["butir_3"]["menang"] is False
    assert kalah["butir_3"]["jumlah_bulan_absen_pasangan"] == 12


def test_kendali_absen_sah():
    per_baris = {
        "BTCUSDT": {"cacah_bulan_lolos": 70, "cacah_absen": 0},
        "ETHUSDT": {"cacah_bulan_lolos": 70, "cacah_absen": 0},
    }
    kendali = ba.kendali_absen(per_baris)
    assert len(kendali) == 2
    assert ba.kendali_sah(kendali) is True


def test_kendali_absen_gugur_bila_absen_bukan_nol():
    per_baris = {
        "BTCUSDT": {"cacah_bulan_lolos": 70, "cacah_absen": 1},
        "ETHUSDT": {"cacah_bulan_lolos": 70, "cacah_absen": 0},
    }
    assert ba.kendali_sah(ba.kendali_absen(per_baris)) is False
    assert ba.kendali_sah(ba.kendali_absen({})) is False
    assert ba.kendali_sah([]) is False


def test_kode_keluar_penggugur_bahan_baku():
    assert ba.kode_keluar(_ringkasan_bersih()) == 0
    assert ba.kode_keluar(_ringkasan_bersih(sidik_seragam=False)) == 2
    assert ba.kode_keluar(_ringkasan_bersih(cacah_laporan_dibaca=7)) == 2
    assert ba.kode_keluar(_ringkasan_bersih(cacah_kunci_ganda=1)) == 2
    assert ba.kode_keluar(_ringkasan_bersih(kendali_sah=False)) == 2
    assert ba.kode_keluar(_ringkasan_bersih(selisih_penyebut=-12)) == 2
    assert ba.kode_keluar(_ringkasan_bersih(cacah_pasangan=14)) == 2


def test_kode_keluar_tidak_gugur_bila_ramalan_meleset():
    ringkasan = _ringkasan_bersih(
        jumlah_bulan_absen=99,
        selisih_absen_pasangan_jurnal_113=87,
        uji_r288={"r288_menang": False, "penggugur_menyala": True},
    )
    assert ba.kode_keluar(ringkasan) == 0
