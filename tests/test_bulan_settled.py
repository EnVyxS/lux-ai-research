"""Uji `bulan_settled` V1 - 26 butir, seluruhnya sintetis dan TANPA jaringan.

Daftar BERNOMOR (aturan 57); tidak ada `parametrize`, jadi cacah butir = cacah
fungsi = **26**. Bersama 526 butir terverifikasi pada run 30447917282, CI pada
commit yang memuat berkas ini diramalkan **552** (R-250).

Pendaftaran arsip disuntikkan lewat `pengambil`, jadi tidak satu pun butir
menyentuh jaringan.

1. test_01_nama_keluaran_tetap
2. test_02_nama_ringkas_berbeda
3. test_03_sidik_kode_panjang
4. test_04_sidik_kode_stabil
5. test_05_daftar_settled_tercatat
6. test_06_daftar_settled_kosong
7. test_07_nama_didaftar_memuat_dasar
8. test_08_nama_didaftar_tanpa_ganda
9. test_09_kumpulkan_bulan_terurut
10. test_10_kumpulkan_bulan_tanpa_ganda
11. test_11_kumpulkan_bulan_galat_dicatat
12. test_12_bulan_saudara_dua_bentuk
13. test_13_bulan_saudara_abai_tak_terukur
14. test_14_h_a013_cocok_true
15. test_15_h_a013_cocok_false_bulan_lain
16. test_16_h_a013_tanpa_saudara
17. test_17_h_a013_enam_baris
18. test_18_h_a013_menang_pada_ambang
19. test_19_h_a013_menang_false_di_bawah_ambang
20. test_20_h_a013_terukur_false
21. test_21_silang_cacah_cocok
22. test_22_silang_cacah_tak_cocok
23. test_23_silang_cacah_tanpa_laporan_lama
24. test_24_kendali_sah
25. test_25_kendali_tak_sah_di_bawah_ambang
26. test_26_kode_keluar
"""

from __future__ import annotations

from lux_ai.serapan import bulan_settled


def peta(bulan_per_nama, gagal=()):
    hasil = {}
    for nama, bulan in bulan_per_nama.items():
        hasil[nama] = {
            "bulan": list(bulan),
            "cacah_bulan": len(bulan),
            "terukur": True,
            "galat": None,
        }
    for nama in gagal:
        hasil[nama] = {
            "bulan": [],
            "cacah_bulan": 0,
            "terukur": False,
            "galat": "gagal",
        }
    return hasil


def sehat():
    return {
        "kendali_sah": True,
        "cacah_gagal_daftar": 0,
        "cacah_settled_tercatat": bulan_settled.SETTLED_TERCATAT,
    }


def test_01_nama_keluaran_tetap():
    assert bulan_settled.nama_keluaran() == "reports/bulan_settled.json"


def test_02_nama_ringkas_berbeda():
    assert bulan_settled.nama_ringkas() != bulan_settled.nama_keluaran()


def test_03_sidik_kode_panjang():
    assert len(bulan_settled.sidik_kode()) == 64


def test_04_sidik_kode_stabil():
    assert bulan_settled.sidik_kode() == bulan_settled.sidik_kode()


def test_05_daftar_settled_tercatat():
    dok = {"settled": {"daftar_settled_arsip": ["BUSDTSETTLED", "AUSDTSETTLED"]}}
    assert bulan_settled.daftar_settled_tercatat(dok) == [
        "AUSDTSETTLED",
        "BUSDTSETTLED",
    ]


def test_06_daftar_settled_kosong():
    assert bulan_settled.daftar_settled_tercatat({}) == []


def test_07_nama_didaftar_memuat_dasar():
    nama = bulan_settled.nama_didaftar([])
    for simbol, _bulan in bulan_settled.PERALIHAN:
        assert simbol in nama
    for simbol in bulan_settled.DASAR_LAIN:
        assert simbol in nama


def test_08_nama_didaftar_tanpa_ganda():
    nama = bulan_settled.nama_didaftar(["ICPUSDT", "ZUSDTSETTLED"])
    assert len(nama) == len(set(nama))
    assert "ZUSDTSETTLED" in nama


def test_09_kumpulkan_bulan_terurut():
    hasil = bulan_settled.kumpulkan_bulan(
        ["AUSDT"], pengambil=lambda n: ["2025-03", "2025-01"]
    )
    assert hasil["AUSDT"]["bulan"] == ["2025-01", "2025-03"]
    assert hasil["AUSDT"]["terukur"] is True


def test_10_kumpulkan_bulan_tanpa_ganda():
    hasil = bulan_settled.kumpulkan_bulan(
        ["AUSDT"], pengambil=lambda n: ["2025-01", "2025-01"]
    )
    assert hasil["AUSDT"]["cacah_bulan"] == 1


def test_11_kumpulkan_bulan_galat_dicatat():
    def rusak(_nama):
        raise RuntimeError("451")

    hasil = bulan_settled.kumpulkan_bulan(["AUSDT"], pengambil=rusak)
    assert hasil["AUSDT"]["terukur"] is False
    assert "451" in hasil["AUSDT"]["galat"]
    assert hasil["AUSDT"]["bulan"] == []


def test_12_bulan_saudara_dua_bentuk():
    p = peta({"XUSDTSETTLED": ["2025-04"], "XUSDT_SETTLED": ["2025-05"]})
    info = bulan_settled.bulan_saudara(p, "XUSDT")
    assert info["saudara_ditemukan"] == ["XUSDTSETTLED", "XUSDT_SETTLED"]
    assert info["bulan_saudara"] == ["2025-04", "2025-05"]


def test_13_bulan_saudara_abai_tak_terukur():
    p = peta({}, gagal=["XUSDTSETTLED"])
    info = bulan_settled.bulan_saudara(p, "XUSDT")
    assert info["saudara_ditemukan"] == []
    assert info["cacah_bulan_saudara"] == 0


def test_14_h_a013_cocok_true():
    p = peta({"CTKUSDTSETTLED": ["2025-04"]})
    hasil = bulan_settled.uji_h_a013_bulan(p, peralihan=(("CTKUSDT", "2025-04"),))
    assert hasil["baris"][0]["cocok_bulan"] is True
    assert hasil["baris"][0]["sebab"] == bulan_settled.SEBAB_COCOK


def test_15_h_a013_cocok_false_bulan_lain():
    p = peta({"CTKUSDTSETTLED": ["2024-01"]})
    hasil = bulan_settled.uji_h_a013_bulan(p, peralihan=(("CTKUSDT", "2025-04"),))
    assert hasil["baris"][0]["cocok_bulan"] is False
    assert hasil["baris"][0]["sebab"] == bulan_settled.SEBAB_LAIN


def test_16_h_a013_tanpa_saudara():
    hasil = bulan_settled.uji_h_a013_bulan({}, peralihan=(("CTKUSDT", "2025-04"),))
    assert hasil["baris"][0]["sebab"] == bulan_settled.SEBAB_TANPA
    assert hasil["cacah_terukur"] == 0


def test_17_h_a013_enam_baris():
    hasil = bulan_settled.uji_h_a013_bulan({})
    assert hasil["cacah_peralihan"] == 6
    assert len(hasil["baris"]) == 6


def test_18_h_a013_menang_pada_ambang():
    isi = {}
    for simbol, bulan in bulan_settled.PERALIHAN[: bulan_settled.AMBANG_MENANG]:
        isi[simbol + "SETTLED"] = [bulan]
    hasil = bulan_settled.uji_h_a013_bulan(peta(isi))
    assert hasil["cacah_cocok_bulan"] == bulan_settled.AMBANG_MENANG
    assert hasil["menang"] is True


def test_19_h_a013_menang_false_di_bawah_ambang():
    simbol, bulan = bulan_settled.PERALIHAN[0]
    hasil = bulan_settled.uji_h_a013_bulan(peta({simbol + "SETTLED": [bulan]}))
    assert hasil["cacah_cocok_bulan"] == 1
    assert hasil["menang"] is False


def test_20_h_a013_terukur_false():
    hasil = bulan_settled.uji_h_a013_bulan({})
    assert hasil["terukur"] is False
    assert hasil["menang"] is False


def test_21_silang_cacah_cocok():
    hasil = bulan_settled.silang_cacah(
        peta({"AUSDT": ["2025-01", "2025-02"]}), {"AUSDT": 2}
    )
    assert hasil["cacah_cocok_cacah"] == 1
    assert hasil["seluruhnya_cocok"] is True


def test_22_silang_cacah_tak_cocok():
    hasil = bulan_settled.silang_cacah(peta({"AUSDT": ["2025-01"]}), {"AUSDT": 2})
    assert hasil["cacah_cocok_cacah"] == 0
    assert hasil["seluruhnya_cocok"] is False


def test_23_silang_cacah_tanpa_laporan_lama():
    hasil = bulan_settled.silang_cacah(peta({"AUSDT": ["2025-01"]}), {})
    assert hasil["cacah_tak_ada_di_laporan_lama"] == 1
    assert hasil["baris"][0]["cacah_tercatat"] is None


def test_24_kendali_sah():
    bulan = ["2020-%02d" % (i + 1) for i in range(12)]
    p = peta({bulan_settled.SIMBOL_KENDALI: bulan})
    hasil = bulan_settled.kendali(p, ambang=12)
    assert hasil["sah"] is True
    assert hasil["cacah_bulan"] == 12


def test_25_kendali_tak_sah_di_bawah_ambang():
    p = peta({bulan_settled.SIMBOL_KENDALI: ["2020-01"]})
    assert bulan_settled.kendali(p)["sah"] is False
    assert bulan_settled.kendali({})["sah"] is False


def test_26_kode_keluar():
    assert bulan_settled.kode_keluar(sehat()) == 0
    buruk = sehat()
    buruk["kendali_sah"] = False
    assert bulan_settled.kode_keluar(buruk) == 2
    lain = sehat()
    lain["cacah_gagal_daftar"] = 1
    assert bulan_settled.kode_keluar(lain) == 2
