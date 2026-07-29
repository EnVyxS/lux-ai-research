"""Uji `semesta_silang` V1 - 32 butir, seluruhnya atas data sintetis.

Daftar BERNOMOR (aturan 57); tidak ada `parametrize`, jadi cacah butir = cacah
fungsi = **32**. Bersama 494 butir terverifikasi pada run 30446932599, CI pada
commit yang memuat berkas ini diramalkan **526** (R-244).

1. test_01_nama_keluaran_tetap
2. test_02_nama_ringkas_berbeda
3. test_03_sidik_kode_panjang
4. test_04_sidik_kode_stabil
5. test_05_cacah_bulan_arsip_int
6. test_06_cacah_bulan_arsip_tanpa_medan
7. test_07_simbol_arsip_terurut
8. test_08_simbol_penyebut_unik
9. test_09_berakhiran_settled_tanpa_garis
10. test_10_berakhiran_settled_garis_bawah
11. test_11_berakhiran_settled_false
12. test_12_daftar_settled_terurut_tanpa_ganda
13. test_13_silang_cacah_dasar
14. test_14_silang_irisan
15. test_15_silang_hanya_arsip
16. test_16_silang_arsip_lebih_banyak
17. test_17_silang_arsip_tidak_lebih_banyak_bila_sama
18. test_18_silang_semesta_sama
19. test_19_silang_penyebut_bukan_bagian
20. test_20_silang_contoh_dibatasi
21. test_21_settled_di_penyebut_nol
22. test_22_settled_di_penyebut_ada
23. test_23_settled_terukur_false_bila_kosong
24. test_24_saudara_arsip_dua_bentuk
25. test_25_h_a013_arsip_enam_baris
26. test_26_h_a013_arsip_saudara_dan_bulan
27. test_27_h_a013_arsip_satu_bulan
28. test_28_h_a013_arsip_tak_berlaku
29. test_29_rinci_bersambung_arsip
30. test_30_kode_keluar_nol
31. test_31_kode_keluar_dua_bila_simbol_salah
32. test_32_kode_keluar_dua_bila_arsip_kosong
"""

from __future__ import annotations

from lux_ai.serapan import semesta_silang


def dok():
    return {
        "bulan_per_simbol": {
            "AUSDT": 3,
            "AUSDTSETTLED": 1,
            "BUSDT": "5",
        }
    }


def sehat():
    return {
        "sidik_seragam": True,
        "cacah_laporan_dibaca": semesta_silang.TOTAL_PECAHAN,
        "total_pecahan": semesta_silang.TOTAL_PECAHAN,
        "cacah_kunci_ganda": 0,
        "kendali_sah": True,
        "selisih_penyebut": 0,
        "cacah_penyebut_simbol": semesta_silang.SIMBOL_TERCATAT,
        "cacah_arsip": 800,
    }


def test_01_nama_keluaran_tetap():
    assert semesta_silang.nama_keluaran() == "reports/semesta_silang.json"


def test_02_nama_ringkas_berbeda():
    assert semesta_silang.nama_ringkas() != semesta_silang.nama_keluaran()


def test_03_sidik_kode_panjang():
    assert len(semesta_silang.sidik_kode()) == 64


def test_04_sidik_kode_stabil():
    assert semesta_silang.sidik_kode() == semesta_silang.sidik_kode()


def test_05_cacah_bulan_arsip_int():
    cacah = semesta_silang.cacah_bulan_arsip(dok())
    assert cacah["AUSDT"] == 3
    assert cacah["BUSDT"] == 5


def test_06_cacah_bulan_arsip_tanpa_medan():
    assert semesta_silang.cacah_bulan_arsip({}) == {}


def test_07_simbol_arsip_terurut():
    assert semesta_silang.simbol_arsip(dok()) == [
        "AUSDT",
        "AUSDTSETTLED",
        "BUSDT",
    ]


def test_08_simbol_penyebut_unik():
    status = {("AUSDT", "2025-01"): "HIDUP", ("AUSDT", "2025-02"): "MATI"}
    assert semesta_silang.simbol_penyebut(status) == ["AUSDT"]


def test_09_berakhiran_settled_tanpa_garis():
    assert semesta_silang.berakhiran_settled("CTKUSDTSETTLED") is True


def test_10_berakhiran_settled_garis_bawah():
    assert semesta_silang.berakhiran_settled("ICPUSDT_SETTLED") is True


def test_11_berakhiran_settled_false():
    assert semesta_silang.berakhiran_settled("BTCUSDT") is False


def test_12_daftar_settled_terurut_tanpa_ganda():
    daftar = semesta_silang.daftar_settled(
        ["BUSDT", "AUSDTSETTLED", "AUSDTSETTLED", "C_SETTLED"]
    )
    assert daftar == ["AUSDTSETTLED", "C_SETTLED"]


def test_13_silang_cacah_dasar():
    s = semesta_silang.silang_semesta(["A", "B", "C"], ["B", "C"])
    assert s["cacah_arsip"] == 3
    assert s["cacah_penyebut"] == 2


def test_14_silang_irisan():
    s = semesta_silang.silang_semesta(["A", "B", "C"], ["B", "C"])
    assert s["cacah_irisan"] == 2


def test_15_silang_hanya_arsip():
    s = semesta_silang.silang_semesta(["A", "B"], ["B"])
    assert s["cacah_hanya_arsip"] == 1
    assert s["contoh_hanya_arsip"] == ["A"]
    assert s["cacah_hanya_penyebut"] == 0


def test_16_silang_arsip_lebih_banyak():
    s = semesta_silang.silang_semesta(["A", "B"], ["B"])
    assert s["arsip_lebih_banyak"] is True
    assert s["penyebut_bagian_arsip"] is True


def test_17_silang_arsip_tidak_lebih_banyak_bila_sama():
    s = semesta_silang.silang_semesta(["A"], ["A"])
    assert s["arsip_lebih_banyak"] is False


def test_18_silang_semesta_sama():
    s = semesta_silang.silang_semesta(["A", "B"], ["B", "A"])
    assert s["semesta_sama"] is True
    assert s["cacah_hanya_arsip"] == 0


def test_19_silang_penyebut_bukan_bagian():
    s = semesta_silang.silang_semesta(["A"], ["A", "Z"])
    assert s["penyebut_bagian_arsip"] is False
    assert s["contoh_hanya_penyebut"] == ["Z"]


def test_20_silang_contoh_dibatasi():
    banyak = ["S%03d" % i for i in range(semesta_silang.TERATAS + 5)]
    s = semesta_silang.silang_semesta(banyak, [])
    assert s["cacah_hanya_arsip"] == semesta_silang.TERATAS + 5
    assert len(s["contoh_hanya_arsip"]) == semesta_silang.TERATAS


def test_21_settled_di_penyebut_nol():
    hasil = semesta_silang.settled_di_penyebut(["AUSDTSETTLED"], ["AUSDT"])
    assert hasil["cacah_settled_arsip"] == 1
    assert hasil["cacah_settled_di_penyebut"] == 0


def test_22_settled_di_penyebut_ada():
    hasil = semesta_silang.settled_di_penyebut(
        ["AUSDTSETTLED"], ["AUSDTSETTLED"]
    )
    assert hasil["daftar_settled_di_penyebut"] == ["AUSDTSETTLED"]


def test_23_settled_terukur_false_bila_kosong():
    assert semesta_silang.settled_di_penyebut(["AUSDT"], [])["terukur"] is False


def test_24_saudara_arsip_dua_bentuk():
    cacah = {"XUSDTSETTLED": 1, "XUSDT_SETTLED": 9, "YUSDT": 4}
    saudara = semesta_silang.saudara_arsip(cacah, "XUSDT")
    assert [s["nama"] for s in saudara] == ["XUSDTSETTLED", "XUSDT_SETTLED"]
    assert semesta_silang.saudara_arsip(cacah, "YUSDT") == []


def test_25_h_a013_arsip_enam_baris():
    hasil = semesta_silang.uji_h_a013_arsip({})
    assert hasil["cacah_peralihan"] == 6
    assert hasil["cacah_saudara_arsip"] == 0


def test_26_h_a013_arsip_saudara_dan_bulan():
    simbol, _bulan = semesta_silang.PERALIHAN[0]
    cacah = {simbol: 11, simbol + "SETTLED": 1}
    hasil = semesta_silang.uji_h_a013_arsip(cacah, peralihan=((simbol, "2025-04"),))
    baris = hasil["baris"][0]
    assert baris["simbol_di_arsip"] is True
    assert baris["cacah_bulan_simbol"] == 11
    assert baris["cacah_bulan_saudara"] == 1


def test_27_h_a013_arsip_satu_bulan():
    cacah = {}
    for simbol, _bulan in semesta_silang.PERALIHAN:
        cacah[simbol + "SETTLED"] = 1
    hasil = semesta_silang.uji_h_a013_arsip(cacah)
    assert hasil["cacah_saudara_arsip"] == 6
    assert hasil["cacah_saudara_satu_bulan"] == 6


def test_28_h_a013_arsip_tak_berlaku():
    hasil = semesta_silang.uji_h_a013_arsip({"CTKUSDTSETTLED": 1})
    assert hasil["berlaku"] is False
    assert hasil["menang"] is None
    assert hasil["bulan_cocok_terukur"] is False
    assert all(not b["bulan_cocok_terukur"] for b in hasil["baris"])


def test_29_rinci_bersambung_arsip():
    cacah = {"ICPUSDT": 62, "ICPUSDT_SETTLED": 9}
    baris = semesta_silang.rinci_bersambung_arsip(cacah)
    assert [b["simbol"] for b in baris] == ["ICPUSDT", "TLMUSDT"]
    assert baris[0]["cacah_bulan_saudara"] == 9
    assert baris[1]["cacah_bulan_saudara"] == 0


def test_30_kode_keluar_nol():
    assert semesta_silang.kode_keluar(sehat()) == 0


def test_31_kode_keluar_dua_bila_simbol_salah():
    buruk = sehat()
    buruk["cacah_penyebut_simbol"] = 786
    assert semesta_silang.kode_keluar(buruk) == 2


def test_32_kode_keluar_dua_bila_arsip_kosong():
    buruk = sehat()
    buruk["cacah_arsip"] = 0
    assert semesta_silang.kode_keluar(buruk) == 2
