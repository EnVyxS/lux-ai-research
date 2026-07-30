"""Uji lubang_tebing V1 — 60 butir, dicacah satu per satu (aturan 54, 57).

Penomoran test_01..test_60 sengaja tersurat supaya cacah butir dapat
diperiksa dengan mata, bukan ditebak. Tidak ada parametrize, sehingga satu
fungsi = satu butir.
"""
from __future__ import annotations

from lux_ai.serapan import kehidupan, kohort_ekor, lubang_awal, lubang_tebing

H = kehidupan.STATUS_HIDUP
M = kehidupan.STATUS_MATI


def b_mati_dulu():
    """MATI 2024-02 mendahului lubang tengah 2024-04 secara STRIKT."""
    peta = {"2024-01": H, "2024-02": M, "2024-03": H, "2024-04": H, "2024-05": H}
    return lubang_awal.ringkas("A", peta, {"2024-04"})


def b_serempak():
    """MATI dan lubang bukan-awal pada bulan yang SAMA (kelas tautologis)."""
    peta = {"2024-01": H, "2024-02": H, "2024-03": M, "2024-04": H}
    return lubang_awal.ringkas("B", peta, {"2024-03"})


def b_lubang_dulu():
    """Lubang 2024-02 mendahului MATI 2024-04."""
    peta = {"2024-01": H, "2024-02": H, "2024-03": H, "2024-04": M}
    return lubang_awal.ringkas("C", peta, {"2024-02"})


def b_tebing():
    """Lubang bukan-awal pertama tepat di bulan tebing."""
    peta = {"2025-05": H, "2025-06": H, "2025-07": M, "2025-08": M}
    return lubang_awal.ringkas("D", peta, {"2025-07", "2025-08"})


def b_tanpa_mati():
    """Punya lubang bukan-awal tetapi tak pernah MATI: luar penyebut butir 1."""
    peta = {"2024-01": H, "2024-02": H, "2024-03": H}
    return lubang_awal.ringkas("E", peta, {"2024-02"})


def ringkasan_bersih():
    return {
        "sidik_seragam": True,
        "cacah_laporan_dibaca": lubang_tebing.TOTAL_PECAHAN,
        "total_pecahan": lubang_tebing.TOTAL_PECAHAN,
        "cacah_kunci_ganda": 0,
        "kendali_sah": True,
        "kendali_deteksi_sah": True,
        "selisih_penyebut": 0,
        "selisih_simbol": 0,
        "selisih_mati": 0,
        "selisih_bangkit": 0,
        "selisih_lubang_dalam_penyebut": 0,
        "selisih_lubang_semesta": 0,
        "selisih_ada_lubang": 0,
        "selisih_lubang_awal": 0,
        "selisih_lubang_bukan_awal": 0,
    }


def agregat_palsu(penyebut_1, bagian_1, cacah_tebing):
    return {
        "penyebut_butir_1": penyebut_1,
        "bagian_butir_1": bagian_1,
        "sebaran_arah": {k: 0 for k in lubang_tebing.KELAS_ARAH},
        "penyebut_butir_2": 118,
        "cacah_tebing_butir_2": cacah_tebing,
    }


def test_01():
    assert lubang_tebing.VERSI == 1


def test_02():
    assert lubang_tebing.nama_keluaran() == "reports/lubang_tebing.json"


def test_03():
    assert lubang_tebing.TEBING == kohort_ekor.TEBING


def test_04():
    assert lubang_tebing.TEBING == "2025-07"


def test_05():
    assert lubang_tebing.TOTAL_PECAHAN == lubang_awal.TOTAL_PECAHAN


def test_06():
    assert len(lubang_tebing.sidik_kode()) == 64


def test_07():
    assert lubang_tebing.sidik_kode() == lubang_tebing.sidik_kode()


def test_08():
    assert "lubang_tebing.py" in lubang_tebing.BERKAS_DICAP


def test_09():
    assert "lubang_awal.py" in lubang_tebing.BERKAS_DICAP


def test_10():
    assert "kohort_ekor.py" in lubang_tebing.BERKAS_DICAP


def test_11():
    assert "silang_funding.py" in lubang_tebing.BERKAS_DICAP


def test_12():
    assert lubang_tebing.BERKAS_DICAP == sorted(set(lubang_tebing.BERKAS_DICAP))


def test_13():
    assert lubang_tebing._bagian(1, 2) == 0.5


def test_14():
    assert lubang_tebing._bagian(1, 0) is None


def test_15():
    assert lubang_tebing._bagian(0, 5) == 0.0


def test_16():
    assert lubang_tebing.R306_PITA_BUTIR_1 == (0.25, 0.60)


def test_17():
    assert lubang_tebing.R306_MINIMAL_PENYEBUT_BUTIR_1 == 100


def test_18():
    assert lubang_tebing.R306_PITA_BUTIR_2_CACAH == (20, 90)


def test_19():
    assert lubang_tebing.dalam_pita(0.4, (0.25, 0.60))


def test_20():
    assert lubang_tebing.dalam_pita(0.25, (0.25, 0.60))


def test_21():
    assert lubang_tebing.dalam_pita(0.60, (0.25, 0.60))


def test_22():
    assert not lubang_tebing.dalam_pita(None, (0.25, 0.60))


def test_23():
    assert not lubang_tebing.dalam_pita(0.99, (0.25, 0.60))


def test_24():
    assert len(lubang_tebing.KELAS_ARAH) == 3


def test_25():
    assert len(set(lubang_tebing.KELAS_ARAH)) == 3


def test_26():
    assert lubang_tebing.kelas_arah(b_mati_dulu()) == lubang_tebing.KELAS_MATI_DULU


def test_27():
    assert lubang_tebing.kelas_arah(b_serempak()) == lubang_tebing.KELAS_SEREMPAK


def test_28():
    assert lubang_tebing.kelas_arah(b_lubang_dulu()) == lubang_tebing.KELAS_LUBANG_DULU


def test_29():
    assert lubang_tebing.kelas_arah(b_tanpa_mati()) is None


def test_30():
    assert lubang_tebing.kelas_arah({"masuk_penyebut_butir_1": False}) is None


def test_31():
    kosong = {
        "masuk_penyebut_butir_1": True,
        "bulan_mati_pertama": None,
        "bulan_lubang_bukan_awal_pertama": "2025-07",
    }
    assert lubang_tebing.kelas_arah(kosong) is None


def test_32():
    assert lubang_tebing.kelas_arah(b_tebing()) == lubang_tebing.KELAS_SEREMPAK


def test_33():
    assert lubang_tebing.di_tebing(b_tebing())


def test_34():
    assert not lubang_tebing.di_tebing(b_mati_dulu())


def test_35():
    assert not lubang_tebing.di_tebing({"bulan_lubang_bukan_awal_pertama": None})


def test_36():
    assert "kelas_arah" in lubang_tebing.perkaya(b_mati_dulu())


def test_37():
    assert lubang_tebing.perkaya(b_mati_dulu())["mati_sebelum_lubang_strikt"]


def test_38():
    assert not lubang_tebing.perkaya(b_serempak())["mati_sebelum_lubang_strikt"]


def test_39():
    assert not lubang_tebing.perkaya(b_lubang_dulu())["mati_sebelum_lubang_strikt"]


def test_40():
    kaya = lubang_tebing.perkaya(b_tebing())
    assert kaya["lubang_bukan_awal_pertama_di_tebing"]


def test_41():
    kaya = lubang_tebing.perkaya(b_mati_dulu())
    assert kaya["simbol"] == "A" and kaya["bulan_tebing"] == "2025-07"


def test_42():
    asli = b_mati_dulu()
    lubang_tebing.perkaya(asli)
    assert "kelas_arah" not in asli


def test_43():
    sebaran = lubang_tebing.sebaran_arah([])
    assert sebaran == {k: 0 for k in lubang_tebing.KELAS_ARAH}


def test_44():
    sebaran = lubang_tebing.sebaran_arah([b_mati_dulu(), b_serempak()])
    assert sebaran[lubang_tebing.KELAS_MATI_DULU] == 1


def test_45():
    sebaran = lubang_tebing.sebaran_arah([b_serempak(), b_tebing()])
    assert sebaran[lubang_tebing.KELAS_SEREMPAK] == 2


def test_46():
    sebaran = lubang_tebing.sebaran_arah([b_lubang_dulu()])
    assert sebaran[lubang_tebing.KELAS_LUBANG_DULU] == 1


def test_47():
    agregat = lubang_tebing.himpun([b_mati_dulu(), b_serempak(), b_tanpa_mati()])
    assert agregat["penyebut_butir_1"] == 2


def test_48():
    agregat = lubang_tebing.himpun([b_mati_dulu(), b_serempak()])
    assert agregat["numerator_butir_1"] == 1


def test_49():
    agregat = lubang_tebing.himpun([b_mati_dulu(), b_serempak()])
    assert agregat["bagian_butir_1"] == 0.5


def test_50():
    agregat = lubang_tebing.himpun([b_tanpa_mati()])
    assert agregat["penyebut_butir_1"] == 0


def test_51():
    agregat = lubang_tebing.himpun([b_tanpa_mati()])
    assert agregat["bagian_butir_1"] is None


def test_52():
    agregat = lubang_tebing.himpun([b_mati_dulu(), b_tanpa_mati()])
    assert agregat["penyebut_butir_2"] == 2


def test_53():
    agregat = lubang_tebing.himpun([b_tebing(), b_mati_dulu()])
    assert agregat["cacah_tebing_butir_2"] == 1


def test_54():
    agregat = lubang_tebing.himpun([b_mati_dulu(), b_serempak()])
    assert agregat["cacah_simbol"] == 2


def test_55():
    kd = lubang_tebing.kendali_deteksi()
    assert kd["kendali_deteksi_sah"]


def test_56():
    kd = lubang_tebing.kendali_deteksi()
    assert len(kd["baris_kendali_deteksi"]) == 4


def test_57():
    hasil = lubang_tebing.uji_r306(agregat_palsu(99, 0.4, 50), ringkasan_bersih())
    assert hasil["butir_1"] == "TIDAK_TERADJUDIKASI"


def test_58():
    hasil = lubang_tebing.uji_r306(agregat_palsu(118, 0.4, 50), ringkasan_bersih())
    assert hasil["butir_1"] == "MENANG" and hasil["butir_2"] == "MENANG"


def test_59():
    hasil = lubang_tebing.uji_r306(agregat_palsu(118, 1.0, 5), ringkasan_bersih())
    assert hasil["butir_1"] == "KALAH" and hasil["butir_2"] == "KALAH"


def test_60():
    bersih = ringkasan_bersih()
    assert lubang_tebing.kode_keluar(bersih) == 0
    for medan in ("selisih_ada_lubang", "selisih_lubang_awal", "kendali_deteksi_sah"):
        rusak = ringkasan_bersih()
        rusak[medan] = 3 if medan.startswith("selisih") else False
        assert lubang_tebing.kode_keluar(rusak) == 2
