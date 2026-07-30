"""Uji byte_semesta V1 (R-307, poros H-A018).

Butir dinamai test_01..test_56 tanpa parametrize agar cacahnya dapat
diverifikasi dengan mata (aturan 54, 57). Tidak satu pun butir menyentuh
jaringan atau laporan nyata: semuanya bentangan buatan.
"""

from __future__ import annotations

from lux_ai.serapan import byte_semesta, kehidupan


def _status_buatan():
    m = kehidupan.STATUS_MATI
    h = kehidupan.STATUS_HIDUP
    s = kehidupan.STATUS_SEPI
    t = kehidupan.STATUS_TAK_TERUKUR
    status = {
        ("A", "2024-01"): m,
        ("B", "2024-01"): h,
        ("C", "2024-01"): s,
        ("D", "2024-01"): t,
    }
    byte_parquet = {
        ("A", "2024-01"): 100,
        ("B", "2024-01"): 900,
        ("C", "2024-01"): 5,
        ("D", "2024-01"): 3,
    }
    return status, byte_parquet


def _ringkasan_sehat():
    r = {
        "sidik_seragam": True,
        "cacah_laporan_dibaca": byte_semesta.TOTAL_PECAHAN,
        "total_pecahan": byte_semesta.TOTAL_PECAHAN,
        "cacah_kunci_ganda": 0,
        "kendali_sah": True,
        "kendali_deteksi_sah": True,
    }
    for medan in byte_semesta.MEDAN_SELISIH:
        r[medan] = 0
    return r


def test_01():
    assert byte_semesta.VERSI == 1


def test_02():
    assert byte_semesta.KELUARAN == "reports/byte_semesta.json"


def test_03():
    assert byte_semesta.TOTAL_PECAHAN == 8


def test_04():
    assert byte_semesta.nama_keluaran() == byte_semesta.KELUARAN


def test_05():
    assert byte_semesta.sidik_kode() == byte_semesta.sidik_kode()


def test_06():
    assert len(byte_semesta.sidik_kode()) == 64


def test_07():
    assert len(byte_semesta.BERKAS_DICAP) == 5


def test_08():
    assert "byte_semesta.py" in byte_semesta.BERKAS_DICAP


def test_09():
    assert "silang_funding.py" in byte_semesta.BERKAS_DICAP


def test_10():
    assert byte_semesta.R307_PITA_BUTIR_1 == (0.02, 0.15)


def test_11():
    assert byte_semesta.R307_AMBANG_BYTE_KECIL == 10000


def test_12():
    assert byte_semesta.R307_PITA_BUTIR_2_CACAH == (20, 400)


def test_13():
    assert byte_semesta.PENYEBUT_TERCATAT == 19586


def test_14():
    assert byte_semesta.SIMBOL_TERCATAT == 787


def test_15():
    assert byte_semesta.MATI_TERCATAT == 1401


def test_16():
    assert byte_semesta.BANGKIT_TERCATAT == 8


def test_17():
    assert byte_semesta.LUBANG_DALAM_PENYEBUT_TERCATAT == 877


def test_18():
    assert byte_semesta.LUBANG_SEMESTA_TERCATAT == 880


def test_19():
    assert byte_semesta.ADA_LUBANG_TERCATAT == 122


def test_20():
    assert byte_semesta.LUBANG_AWAL_TERCATAT == 5


def test_21():
    assert byte_semesta.LUBANG_BUKAN_AWAL_TERCATAT == 118


def test_22():
    assert len(byte_semesta.MEDAN_SELISIH) == 9


def test_23():
    assert byte_semesta.BATAS_BARIS_LAPORAN == 40


def test_24():
    assert byte_semesta._bagian(1, 4) == 0.25


def test_25():
    assert byte_semesta._bagian(5, 0) is None


def test_26():
    assert byte_semesta.kelas_ukur(kehidupan.STATUS_MATI) == byte_semesta.KELAS_MATI


def test_27():
    assert byte_semesta.kelas_ukur(kehidupan.STATUS_HIDUP) == byte_semesta.KELAS_TERUKUR


def test_28():
    assert byte_semesta.kelas_ukur(kehidupan.STATUS_SEPI) == byte_semesta.KELAS_TERUKUR


def test_29():
    assert (
        byte_semesta.kelas_ukur(kehidupan.STATUS_TAK_TERUKUR)
        == byte_semesta.KELAS_LAIN
    )


def test_30():
    status, byte_parquet = _status_buatan()
    assert byte_semesta.himpun_byte(status, byte_parquet)["total_byte"] == 1008


def test_31():
    status, byte_parquet = _status_buatan()
    assert byte_semesta.himpun_byte(status, byte_parquet)["byte_mati"] == 100


def test_32():
    status, byte_parquet = _status_buatan()
    assert byte_semesta.himpun_byte(status, byte_parquet)["byte_terukur"] == 905


def test_33():
    status, byte_parquet = _status_buatan()
    assert byte_semesta.himpun_byte(status, byte_parquet)["byte_lain"] == 3


def test_34():
    status, byte_parquet = _status_buatan()
    a = byte_semesta.himpun_byte(status, byte_parquet)
    assert a["bagian_byte_mati"] == 100 / 1008


def test_35():
    status, _ = _status_buatan()
    a = byte_semesta.himpun_byte(status, {})
    assert a["total_byte"] == 0 and a["bagian_byte_mati"] is None


def test_36():
    status, byte_parquet = _status_buatan()
    a = byte_semesta.himpun_byte(status, byte_parquet)
    assert (a["cacah_mati"], a["cacah_terukur"], a["cacah_lain"]) == (1, 2, 1)


def test_37():
    status, byte_parquet = _status_buatan()
    a = byte_semesta.himpun_byte(status, byte_parquet, ambang=50)
    assert a["cacah_terukur_byte_kecil"] == 1


def test_38():
    status, byte_parquet = _status_buatan()
    byte_parquet[("C", "2024-01")] = 50
    a = byte_semesta.himpun_byte(status, byte_parquet, ambang=50)
    assert a["cacah_terukur_byte_kecil"] == 0


def test_39():
    status, byte_parquet = _status_buatan()
    byte_parquet[("A", "2024-01")] = 1
    a = byte_semesta.himpun_byte(status, byte_parquet, ambang=50)
    assert a["cacah_terukur_byte_kecil"] == 1 and a["cacah_mati_byte_kecil"] == 1


def test_40():
    status, byte_parquet = _status_buatan()
    a = byte_semesta.himpun_byte(status, byte_parquet, ambang=50)
    assert a["cacah_lain_byte_kecil"] == 1


def test_41():
    status, byte_parquet = _status_buatan()
    byte_parquet[("B", "2024-01")] = 0
    a = byte_semesta.himpun_byte(status, byte_parquet)
    assert a["cacah_byte_nol"] == 1


def test_42():
    status, byte_parquet = _status_buatan()
    a = byte_semesta.himpun_byte(status, byte_parquet)
    assert a["cacah_baris"] == 4 and a["ambang_byte_kecil"] == 10000


def test_43():
    status, byte_parquet = _status_buatan()
    baris = byte_semesta.daftar_terukur_byte_kecil(status, byte_parquet, ambang=50)
    assert [r["simbol"] for r in baris] == ["C"]


def test_44():
    status, byte_parquet = _status_buatan()
    baris = byte_semesta.daftar_terukur_byte_kecil(status, byte_parquet, ambang=1000)
    assert [r["simbol"] for r in baris] == ["C", "B"]


def test_45():
    status, byte_parquet = _status_buatan()
    s = byte_semesta.sebaran_byte_per_status(status, byte_parquet)
    assert s[kehidupan.STATUS_MATI]["byte"] == 100


def test_46():
    status, byte_parquet = _status_buatan()
    s = byte_semesta.sebaran_byte_per_status(status, byte_parquet)
    assert s[kehidupan.STATUS_HIDUP]["byte_min"] == 900


def test_47():
    kd = byte_semesta.kendali_deteksi()
    assert kd["kendali_deteksi_sah"] is True


def test_48():
    kd = byte_semesta.kendali_deteksi()
    assert kd["agregat_kendali"]["cacah_terukur_byte_kecil"] == 2


def test_49():
    kd = byte_semesta.kendali_deteksi()
    assert [r["simbol"] for r in kd["baris_kendali_kecil"]] == [
        "KENDALI_SEPI",
        "KENDALI_KECIL",
    ]


def test_50():
    assert byte_semesta.dalam_pita(0.05, byte_semesta.R307_PITA_BUTIR_1)


def test_51():
    assert byte_semesta.dalam_pita(0.02, byte_semesta.R307_PITA_BUTIR_1)
    assert byte_semesta.dalam_pita(0.15, byte_semesta.R307_PITA_BUTIR_1)


def test_52():
    assert not byte_semesta.dalam_pita(None, byte_semesta.R307_PITA_BUTIR_1)
    assert not byte_semesta.dalam_pita(0.4, byte_semesta.R307_PITA_BUTIR_1)


def test_53():
    agregat = {"total_byte": 1000, "bagian_byte_mati": 0.05, "cacah_terukur_byte_kecil": 50}
    u = byte_semesta.uji_r307(agregat, _ringkasan_sehat())
    assert u["butir_1"] == "MENANG" and u["butir_2"] == "MENANG" and u["butir_3"]


def test_54():
    agregat = {"total_byte": 1000, "bagian_byte_mati": 0.9, "cacah_terukur_byte_kecil": 5}
    u = byte_semesta.uji_r307(agregat, _ringkasan_sehat())
    assert u["butir_1"] == "KALAH" and u["butir_2"] == "KALAH"


def test_55():
    agregat = {"total_byte": 0, "bagian_byte_mati": None, "cacah_terukur_byte_kecil": 0}
    u = byte_semesta.uji_r307(agregat, _ringkasan_sehat())
    assert u["butir_1"] == "TIDAK_TERADJUDIKASI"


def test_56():
    assert byte_semesta.kode_keluar(_ringkasan_sehat()) == 0
    for medan in byte_semesta.MEDAN_SELISIH:
        r = _ringkasan_sehat()
        r[medan] = 1
        assert byte_semesta.kode_keluar(r) == 2
    for medan in ("kendali_sah", "kendali_deteksi_sah", "sidik_seragam"):
        r = _ringkasan_sehat()
        r[medan] = False
        assert byte_semesta.kode_keluar(r) == 2
    r = _ringkasan_sehat()
    r["cacah_kunci_ganda"] = 1
    assert byte_semesta.kode_keluar(r) == 2
    r = _ringkasan_sehat()
    r["cacah_laporan_dibaca"] = 7
    assert byte_semesta.kode_keluar(r) == 2
