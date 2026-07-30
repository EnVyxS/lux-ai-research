"""Butir uji tersisip_semesta V1 — 47 butir bernomor test_01..test_47.

Cacah butir dibaca dari daftar bernomor ini, bukan dari ingatan (aturan 54/57).
Tiga butir memanggil modul sumber ASLI untuk memeriksa BENTUK kembalian dan
tanda tangan, sebab data sintetis yang bentuknya dikarang sendiri hanya menguji
karangan itu (penangkal KC-43).
"""
from __future__ import annotations

import inspect
from pathlib import Path

from lux_ai.serapan import (
    bentangan_kohort,
    kehidupan,
    silang_funding,
    tersisip_semesta as ts,
)

HIDUP = kehidupan.STATUS_HIDUP
MATI = kehidupan.STATUS_MATI
SEPI = kehidupan.STATUS_SEPI

SISIP = {"2024-01": HIDUP, "2024-02": MATI, "2024-03": HIDUP}
MONOTON = {"2024-01": HIDUP, "2024-02": HIDUP, "2024-03": MATI}


def test_01_versi():
    assert ts.VERSI == 1


def test_02_keluaran():
    assert ts.KELUARAN == "reports/tersisip_semesta.json"


def test_03_penyebut_tercatat():
    assert ts.PENYEBUT_TERCATAT == 19586


def test_04_simbol_tercatat():
    assert ts.SIMBOL_TERCATAT == 787


def test_05_mati_tercatat():
    assert ts.MATI_TERCATAT == 1401


def test_06_pita_butir_1():
    assert ts.R303_PITA_SIMBOL == (1, 60)


def test_07_pita_butir_2():
    assert ts.R303_PITA_SIMBOL_BULAN == (1, 300)


def test_08_berkas_dicap_ada():
    dasar = Path(ts.__file__).parent
    assert ts.BERKAS_DICAP == sorted(ts.BERKAS_DICAP)
    assert len(ts.BERKAS_DICAP) == 5
    for nama in ts.BERKAS_DICAP:
        assert (dasar / nama).exists()


def test_09_sidik_kode_stabil():
    a = ts.sidik_kode()
    assert len(a) == 64
    assert a == ts.sidik_kode()


def test_10_sisip_dasar():
    assert ts.bulan_tersisip(SISIP) == ["2024-02"]


def test_11_monoton_nol():
    assert ts.bulan_tersisip(MONOTON) == []


def test_12_tanpa_hidup_nol():
    assert ts.bulan_tersisip({"2024-01": MATI, "2024-02": MATI}) == []


def test_13_satu_hidup_nol():
    assert ts.bulan_tersisip({"2024-01": HIDUP, "2024-02": MATI}) == []


def test_14_dua_tersisip():
    peta = {
        "2024-01": HIDUP,
        "2024-02": MATI,
        "2024-03": MATI,
        "2024-04": HIDUP,
    }
    assert ts.bulan_tersisip(peta) == ["2024-02", "2024-03"]


def test_15_mati_sesudah_hidup_terakhir_tidak_dihitung():
    peta = {"2024-01": HIDUP, "2024-02": HIDUP, "2024-03": MATI, "2024-04": MATI}
    assert ts.bulan_tersisip(peta) == []


def test_16_mati_sebelum_hidup_pertama_tidak_dihitung():
    peta = {"2024-01": MATI, "2024-02": HIDUP, "2024-03": HIDUP}
    assert ts.bulan_tersisip(peta) == []


def test_17_sepi_bukan_mati():
    peta = {"2024-01": HIDUP, "2024-02": SEPI, "2024-03": HIDUP}
    assert ts.bulan_tersisip(peta) == []


def test_18_sepakat_dengan_bentangan_kohort():
    for peta in (
        SISIP,
        MONOTON,
        {"2024-01": HIDUP, "2024-02": MATI, "2024-03": MATI, "2024-04": HIDUP},
        {"2024-01": MATI, "2024-02": HIDUP},
        {"2024-01": HIDUP, "2024-02": SEPI, "2024-03": HIDUP},
    ):
        assert len(ts.bulan_tersisip(peta)) == bentangan_kohort.mati_tersisip(peta)


def test_19_rapat_dasar():
    assert ts.bulan_tersisip_rapat(SISIP) == ["2024-02"]


def test_20_rapat_nol_saat_celah():
    peta = {"2024-01": HIDUP, "2024-02": MATI, "2024-04": HIDUP}
    assert ts.bulan_tersisip(peta) == ["2024-02"]
    assert ts.bulan_tersisip_rapat(peta) == []


def test_21_tetangga_maju():
    assert ts.tetangga_maju(SISIP, "2024-01") == "2024-02"
    assert ts.tetangga_maju(SISIP, "2024-03") is None


def test_22_kendali_deteksi_sah():
    assert ts.kendali_deteksi()["sah"] is True


def test_23_kendali_deteksi_angka():
    k = ts.kendali_deteksi()
    assert k["cacah_sisip_pada_kendali_sisip"] == 1
    assert k["cacah_sisip_pada_kendali_monoton"] == 0
    assert k["cacah_rapat_pada_kendali_sisip"] == 1


def test_24_ringkas_cacah():
    r = ts.ringkas_simbol("AAA", {"2024-01": HIDUP, "2024-02": MATI, "2024-03": SEPI})
    assert r["cacah_bulan"] == 3
    assert r["cacah_hidup"] == 1
    assert r["cacah_mati"] == 1
    assert r["cacah_sepi"] == 1


def test_25_ringkas_batas_bulan():
    r = ts.ringkas_simbol("AAA", SISIP)
    assert r["bulan_pertama"] == "2024-01"
    assert r["bulan_terakhir"] == "2024-03"
    assert r["bulan_hidup_terakhir"] == "2024-03"
    assert r["bulan_mati_pertama"] == "2024-02"


def test_26_ringkas_bangkit():
    assert ts.ringkas_simbol("AAA", SISIP)["bangkit"] is True
    assert ts.ringkas_simbol("AAA", MONOTON)["bangkit"] is False


def test_27_ringkas_rentetan():
    peta = {"2024-01": HIDUP, "2024-02": HIDUP, "2024-04": HIDUP}
    assert ts.ringkas_simbol("AAA", peta)["rentetan_hidup_terpanjang"] == 2


def test_28_ringkas_pangkas_daftar():
    peta = {"2020-01": HIDUP, "2030-01": HIDUP}
    for i in range(1, 13):
        peta["2024-%02d" % i] = MATI
    peta["2025-01"] = MATI
    r = ts.ringkas_simbol("AAA", peta)
    assert r["cacah_tersisip"] == 13
    assert len(r["bulan_tersisip"]) == ts.BATAS_BULAN_DICATAT


def test_29_himpun_jumlah():
    baris = [
        ts.ringkas_simbol("AAA", SISIP),
        ts.ringkas_simbol("BBB", MONOTON),
    ]
    a = ts.himpun(baris)
    assert a["cacah_simbol"] == 2
    assert a["penyebut_simbol_bulan"] == 6
    assert a["cacah_mati"] == 2
    assert a["cacah_hidup"] == 4


def test_30_himpun_cacah_simbol_tersisip():
    baris = [
        ts.ringkas_simbol("AAA", SISIP),
        ts.ringkas_simbol("BBB", MONOTON),
    ]
    a = ts.himpun(baris)
    assert a["cacah_simbol_tersisip"] == 1
    assert a["cacah_simbol_bulan_tersisip"] == 1
    assert a["cacah_simbol_tersisip_rapat"] == 1


def test_31_himpun_distribusi():
    baris = [
        ts.ringkas_simbol("AAA", SISIP),
        ts.ringkas_simbol("BBB", MONOTON),
    ]
    d = ts.himpun(baris)["distribusi_tersisip"]
    assert d["0"] == 1
    assert d["1"] == 1


def test_32_ember():
    assert ts.ember(0) == "0"
    assert ts.ember(1) == "1"
    assert ts.ember(2) == "2"
    assert ts.ember(5) == "3-5"
    assert ts.ember(12) == "6-12"
    assert ts.ember(13) == "13+"


def test_33_dalam_pita_tertutup():
    assert ts.dalam_pita(1, (1, 60)) is True
    assert ts.dalam_pita(60, (1, 60)) is True
    assert ts.dalam_pita(0, (1, 60)) is False
    assert ts.dalam_pita(61, (1, 60)) is False


def _agregat(**ganti):
    dasar = {
        "cacah_simbol_tersisip": 30,
        "cacah_simbol_bulan_tersisip": 120,
        "penyebut_simbol_bulan": ts.PENYEBUT_TERCATAT,
        "cacah_simbol": ts.SIMBOL_TERCATAT,
        "cacah_mati": ts.MATI_TERCATAT,
        "kendali_sah": True,
        "deteksi_sah": True,
    }
    dasar.update(ganti)
    return dasar


def test_34_butir_1_menang():
    assert ts.uji_r303(_agregat())["butir_1"] is True


def test_35_butir_1_kalah_pada_nol():
    assert ts.uji_r303(_agregat(cacah_simbol_tersisip=0))["butir_1"] is False


def test_36_butir_1_kalah_di_atas_pita():
    assert ts.uji_r303(_agregat(cacah_simbol_tersisip=61))["butir_1"] is False


def test_37_butir_2_batas_pita():
    assert ts.uji_r303(_agregat(cacah_simbol_bulan_tersisip=300))["butir_2"] is True
    assert ts.uji_r303(_agregat(cacah_simbol_bulan_tersisip=301))["butir_2"] is False
    assert ts.uji_r303(_agregat(cacah_simbol_bulan_tersisip=0))["butir_2"] is False


def test_38_butir_3_menang():
    assert ts.uji_r303(_agregat())["butir_3_mudah"] is True


def test_39_butir_3_kalah_bila_penyebut_beda():
    assert ts.uji_r303(_agregat(penyebut_simbol_bulan=19585))["butir_3_mudah"] is False
    assert ts.uji_r303(_agregat(cacah_simbol=786))["butir_3_mudah"] is False
    assert ts.uji_r303(_agregat(deteksi_sah=False))["butir_3_mudah"] is False


def test_40_pembatal_a008():
    assert ts.uji_r303(_agregat())["pembatal_a008_menyala"] is True
    assert (
        ts.uji_r303(_agregat(cacah_simbol_bulan_tersisip=0))["pembatal_a008_menyala"]
        is False
    )


def _laporan(**ganti):
    ringkasan = {
        "sidik_seragam": True,
        "kendali_sah": True,
        "deteksi_sah": True,
        "penyebut_kehidupan": ts.PENYEBUT_TERCATAT,
        "cacah_kunci_gagal_pisah": 0,
        "cacah_simbol": ts.SIMBOL_TERCATAT,
        "cacah_mati": ts.MATI_TERCATAT,
    }
    ringkasan.update(ganti)
    return {"ringkasan": ringkasan}


def test_41_kode_nol_pada_laporan_sehat():
    assert ts.kode_keluar(_laporan()) == 0


def test_42_kode_dua_pada_penyebut_nol():
    assert ts.kode_keluar(_laporan(penyebut_kehidupan=0)) == 2


def test_43_kode_dua_pada_kunci_gagal_pisah():
    assert ts.kode_keluar(_laporan(cacah_kunci_gagal_pisah=1)) == 2


def test_44_kode_dua_pada_kendali_dan_deteksi():
    assert ts.kode_keluar(_laporan(kendali_sah=False)) == 2
    assert ts.kode_keluar(_laporan(deteksi_sah=False)) == 2
    assert ts.kode_keluar(_laporan(sidik_seragam=False)) == 2


def test_45_kode_dua_pada_mati_nol():
    assert ts.kode_keluar(_laporan(cacah_mati=0)) == 2
    assert ts.kode_keluar(_laporan(cacah_simbol=0)) == 2


def test_46_bentuk_sumber_asli():
    """Penangkal KC-43: tanda tangan sumber diperiksa, bukan diingat."""
    tanda = inspect.signature(silang_funding.baca_laporan_kehidupan)
    assert list(tanda.parameters) == ["akar", "total"]
    assert ts.bulan_tersisip.__module__.endswith("tersisip_semesta")
    kunci = ("AAA", "2024-01")
    peta, gagal = bentangan_kohort.kelompokkan({kunci: HIDUP})
    assert gagal == []
    assert peta == {"AAA": {"2024-01": HIDUP}}


def test_47_nama_simbol_bukan_tetapan():
    """Aturan 73: daftar nama simbol TIDAK boleh menjadi tetapan modul."""
    sumber = Path(ts.__file__).read_text(encoding="utf-8")
    assert "USDT" not in sumber
