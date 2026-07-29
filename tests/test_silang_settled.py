"""Uji silang_settled V1 — 24 butir bernomor (aturan 54, 57).

1. versi satu
2. nama keluaran
3. sidik kode stabil
4. lima belas pasangan
5. pasangan memuat kohort banyak
6. kohort banyak tiga nama
7. lima kendali terbitan
8. funding pertama tanpa lubang
9. funding pertama melewati lubang awal
10. seluruh bulan berlubang menghasilkan None
11. lubang tengah tidak mengubah funding pertama
12. tanpa bulan menghasilkan None
13. arah sama
14. arah lebih awal
15. arah lebih lambat
16. arah tak terukur bila None
17. baris pasangan tetap lima belas walau tanpa data
18. baris pasangan mencacah lubang
19. kendali definisi selisih nol bila cocok
20. kendali definisi selisih bukan nol bila beda
21. butir 1 menang pada tiga cocok
22. butir 1 gugur pada lima cocok
23. butir 2 dan butir 3 memakai penyebut sendiri
24. kode keluar 2 bila kendali tak sah
"""

from __future__ import annotations

from lux_ai.serapan import silang_settled as ss


def _status_kendali():
    """Status buatan agar kelima kendali cocok dengan terbitan V2."""
    pasang = {
        "BNXUSDT": ("2022-05", "2023-02"),
        "ICPUSDT": ("2021-05", "2022-09"),
        "JUPUSDT": ("2024-01", "2024-02"),
        "QTUMUSDT": ("2020-02", "2020-03"),
        "TLMUSDT": ("2021-07", "2023-03"),
    }
    status = {}
    lubang = set()
    for simbol, (awal, terbit) in pasang.items():
        status[(simbol, awal)] = "HIDUP"
        status[(simbol, terbit)] = "HIDUP"
        lubang.add((simbol, awal))
    return status, lubang


def _baris_sintetis(cocok_tambahan: int = 0):
    """15 baris: tiga kohort cocok, sisanya lebih awal kecuali yang diminta."""
    baris = []
    lubang_kohort = {"BNXUSDT": 19, "ICPUSDT": 16, "TLMUSDT": 20}
    lain = [s for s in sorted(ss.PASANGAN_SETTLED) if s not in ss.KOHORT_BANYAK]
    for simbol in ss.KOHORT_BANYAK:
        baris.append(
            {
                "simbol": simbol,
                "arah": ss.SAMA,
                "cacah_lubang": lubang_kohort[simbol],
                "kohort_banyak": True,
            }
        )
    for i, simbol in enumerate(lain):
        baris.append(
            {
                "simbol": simbol,
                "arah": ss.SAMA if i < cocok_tambahan else ss.LEBIH_AWAL,
                "cacah_lubang": 1,
                "kohort_banyak": False,
            }
        )
    return baris


def test_versi_satu():
    assert ss.VERSI == 1


def test_nama_keluaran():
    assert ss.nama_keluaran() == "reports/silang_settled.json"


def test_sidik_kode_stabil():
    a = ss.sidik_kode()
    assert a == ss.sidik_kode() and len(a) == 64


def test_lima_belas_pasangan():
    assert len(ss.PASANGAN_SETTLED) == 15


def test_pasangan_memuat_kohort_banyak():
    assert all(s in ss.PASANGAN_SETTLED for s in ss.KOHORT_BANYAK)


def test_kohort_banyak_tiga_nama():
    assert ss.KOHORT_BANYAK == ("BNXUSDT", "ICPUSDT", "TLMUSDT")


def test_lima_kendali_terbitan():
    assert len(ss.FUNDING_PERTAMA_TERBITAN) == 5


def test_funding_pertama_tanpa_lubang():
    assert (
        ss.bulan_berfunding_pertama_lokal(["2021-03", "2021-01"], set()) == "2021-01"
    )


def test_funding_pertama_melewati_lubang_awal():
    hasil = ss.bulan_berfunding_pertama_lokal(
        ["2021-01", "2021-02", "2021-03"], {"2021-01", "2021-02"}
    )
    assert hasil == "2021-03"


def test_seluruh_bulan_berlubang_none():
    assert (
        ss.bulan_berfunding_pertama_lokal(["2021-01"], {"2021-01"}) is None
    )


def test_lubang_tengah_tidak_mengubah_funding_pertama():
    hasil = ss.bulan_berfunding_pertama_lokal(
        ["2021-01", "2021-02", "2021-03"], {"2021-02"}
    )
    assert hasil == "2021-01"


def test_tanpa_bulan_none():
    assert ss.bulan_berfunding_pertama_lokal([], set()) is None


def test_arah_sama():
    assert ss.arah("2023-02", "2023-02") == ss.SAMA


def test_arah_lebih_awal():
    assert ss.arah("2022-01", "2023-02") == ss.LEBIH_AWAL


def test_arah_lebih_lambat():
    assert ss.arah("2024-01", "2023-02") == ss.LEBIH_LAMBAT


def test_arah_tak_terukur_bila_none():
    assert ss.arah(None, "2023-02") == ss.TAK_TERUKUR


def test_baris_pasangan_tetap_lima_belas():
    baris = ss.baris_pasangan({}, set())
    assert len(baris) == 15
    assert ss.sebaran_arah(baris)[ss.TAK_TERUKUR] == 15


def test_baris_pasangan_mencacah_lubang():
    status = {("BNXUSDT", "2022-05"): "MATI", ("BNXUSDT", "2023-02"): "HIDUP"}
    lubang = {("BNXUSDT", "2022-05")}
    baris = {r["simbol"]: r for r in ss.baris_pasangan(status, lubang)}
    bnx = baris["BNXUSDT"]
    assert bnx["cacah_lubang"] == 1
    assert bnx["bulan_berfunding_pertama"] == "2023-02"
    assert bnx["arah"] == ss.SAMA


def test_kendali_definisi_selisih_nol_bila_cocok():
    status, lubang = _status_kendali()
    baris, selisih = ss.kendali_funding_pertama(status, lubang)
    assert selisih == 0 and len(baris) == 5


def test_kendali_definisi_selisih_bukan_nol_bila_beda():
    status, lubang = _status_kendali()
    lubang.discard(("BNXUSDT", "2022-05"))
    _, selisih = ss.kendali_funding_pertama(status, lubang)
    assert selisih == 1


def test_butir_1_menang_pada_tiga_cocok():
    uji = ss.uji_h_a015(_baris_sintetis(0))
    assert uji["butir_1"]["cacah_cocok"] == 3
    assert uji["butir_1"]["menang"] is True
    assert uji["penggugur_menyala"] is False


def test_butir_1_gugur_pada_lima_cocok():
    uji = ss.uji_h_a015(_baris_sintetis(2))
    assert uji["butir_1"]["cacah_cocok"] == 5
    assert uji["butir_1"]["menang"] is False
    assert uji["h_a015_menang"] is False


def test_butir_2_dan_3_memakai_penyebut_sendiri():
    uji = ss.uji_h_a015(_baris_sintetis(0))
    assert uji["butir_2"]["penyebut"] == 12
    assert uji["butir_2"]["cacah_lebih_awal"] == 12
    assert uji["butir_3"]["cacah_kohort_lubang_lebih_dari_10"] == 3
    assert uji["butir_3"]["cacah_satu_bulan_lubang_kurang_dari_10"] == 12
    assert uji["butir_3"]["menang"] is True


def test_kode_keluar_dua_bila_kendali_tak_sah():
    ringkasan = {
        "sidik_seragam": True,
        "cacah_laporan_dibaca": ss.TOTAL_PECAHAN,
        "total_pecahan": ss.TOTAL_PECAHAN,
        "cacah_kunci_ganda": 0,
        "kendali_sah": False,
        "selisih_penyebut": 0,
        "selisih_kendali_funding_pertama": 0,
        "cacah_pasangan": 15,
    }
    assert ss.kode_keluar(ringkasan) == 2
    ringkasan["kendali_sah"] = True
    assert ss.kode_keluar(ringkasan) == 0
