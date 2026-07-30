"""Uji irisan_byte V1 (R-308). Semuanya sintetis: tidak menyentuh data nyata."""

import json
import re

import pytest

from lux_ai.serapan import irisan_byte as ib


def _kendali_benar():
    byte = {
        ("BTCUSDT", "2021-05"): 2770666,
        ("BTCUSDT", "2021-08"): 2730341,
        ("BTCUSDT", "2021-01"): 2722266,
    }
    status = {kunci: "HIDUP" for kunci in byte}
    return status, byte


def _contoh():
    status = {
        ("AAA", "2024-01"): "HIDUP",
        ("AAA", "2024-02"): "HIDUP",
        ("BBB", "2024-01"): "MATI",
        ("BBB", "2024-02"): "SEPI",
    }
    byte = {
        ("AAA", "2024-01"): 100,
        ("AAA", "2024-02"): 300,
        ("BBB", "2024-01"): 50,
        ("BBB", "2024-02"): 70,
    }
    return status, byte


def test_versi():
    assert ib.VERSI == 1


def test_keluaran_nama():
    assert ib.KELUARAN == "reports/irisan_byte.json"


def test_batas_baris():
    assert ib.BATAS_BARIS_LAPORAN == 40


def test_nama_keluaran_akar():
    assert ib.nama_keluaran("/tmp").endswith("reports/irisan_byte.json")


def test_ambang_hidup_sama_dengan_byte_min_mati():
    assert ib.AMBANG_HIDUP_KECIL == 97634


def test_ambang_mati():
    assert ib.AMBANG_MATI_KECIL == 150000


def test_pita_butir_1():
    assert ib.R308_PITA_BUTIR_1 == (20, 600)


def test_pita_butir_2():
    assert ib.R308_PITA_BUTIR_2 == (10, 300)


def test_penyebut_hidup():
    assert ib.PENYEBUT_HIDUP_TERCATAT == 18087


def test_penyebut_mati():
    assert ib.PENYEBUT_MATI_TERCATAT == 1401


def test_invarian_sembilan():
    assert len(ib.INVARIAN) == 9


def test_medan_selisih_sembilan():
    assert len(ib.MEDAN_SELISIH) == 9


def test_medan_berawalan():
    assert all(m.startswith("selisih_") for m in ib.MEDAN_SELISIH)


def test_byte_menjumlah_total():
    jumlah = (
        ib.INVARIAN["byte_hidup"]
        + ib.INVARIAN["byte_sepi"]
        + ib.INVARIAN["byte_mati"]
    )
    assert jumlah == ib.INVARIAN["total_byte"]


def test_cacah_menjumlah_penyebut():
    jumlah = (
        ib.INVARIAN["cacah_hidup"]
        + ib.INVARIAN["cacah_sepi"]
        + ib.INVARIAN["cacah_mati"]
    )
    assert jumlah == ib.INVARIAN["penyebut"]


def test_kelas_urut():
    assert ib.KELAS_URUT == ("HIDUP", "SEPI", "MATI")


def test_kendali_data_tiga_butir():
    assert len(ib.KENDALI_DATA) == 3


def test_sidik_panjang():
    assert len(ib.sidik_kode()) == 64


def test_sidik_hex():
    assert re.fullmatch(r"[0-9a-f]{64}", ib.sidik_kode())


def test_sidik_stabil():
    assert ib.sidik_kode() == ib.sidik_kode()


def test_bagian_tuple():
    assert ib._bagian(("BTCUSDT", "2021-05")) == ("BTCUSDT", "2021-05")


def test_bagian_pipa():
    assert ib._bagian("BTCUSDT|2021-05") == ("BTCUSDT", "2021-05")


def test_bagian_titik_dua():
    assert ib._bagian("BTCUSDT::2021-05") == ("BTCUSDT", "2021-05")


def test_bagian_miring():
    assert ib._bagian("BTCUSDT/2021-05") == ("BTCUSDT", "2021-05")


def test_bagian_tanpa_pemisah():
    assert ib._bagian("BTCUSDT") == ("BTCUSDT", "")


def test_kelas_status_hidup():
    assert ib.kelas_status("HIDUP") == "HIDUP"


def test_kelas_status_huruf_kecil():
    assert ib.kelas_status("mati") == "MATI"


def test_kelas_status_spasi():
    assert ib.kelas_status("  sepi ") == "SEPI"


def test_kelas_status_lain():
    assert ib.kelas_status(None) == "LAIN"


def test_sebaran_cacah():
    status, byte = _contoh()
    sebaran = ib.sebaran_per_kelas(status, byte)
    assert sebaran["HIDUP"]["cacah"] == 2


def test_sebaran_jumlah():
    status, byte = _contoh()
    sebaran = ib.sebaran_per_kelas(status, byte)
    assert sebaran["HIDUP"]["jumlah"] == 400


def test_sebaran_min_maks():
    status, byte = _contoh()
    sebaran = ib.sebaran_per_kelas(status, byte)
    assert (sebaran["HIDUP"]["min"], sebaran["HIDUP"]["maks"]) == (100, 300)


def test_sebaran_rata():
    status, byte = _contoh()
    sebaran = ib.sebaran_per_kelas(status, byte)
    assert sebaran["HIDUP"]["rata"] == 200.0


def test_sebaran_lewati_byte_hilang():
    status, byte = _contoh()
    byte.pop(("AAA", "2024-02"))
    sebaran = ib.sebaran_per_kelas(status, byte)
    assert sebaran["HIDUP"]["cacah"] == 1


def test_sebaran_kelas_kosong_tidak_muncul():
    status = {("AAA", "2024-01"): "HIDUP"}
    byte = {("AAA", "2024-01"): 10}
    assert "MATI" not in ib.sebaran_per_kelas(status, byte)


def test_cacah_di_bawah_ketat():
    status, byte = _contoh()
    assert ib.cacah_di_bawah(status, byte, "HIDUP", 200) == 1


def test_cacah_di_bawah_batas_persis():
    status, byte = _contoh()
    assert ib.cacah_di_bawah(status, byte, "HIDUP", 100) == 0


def test_cacah_di_bawah_saring_kelas():
    status, byte = _contoh()
    assert ib.cacah_di_bawah(status, byte, "MATI", 200) == 1


def test_cacah_di_bawah_nol():
    status, byte = _contoh()
    assert ib.cacah_di_bawah(status, byte, "HIDUP", 1) == 0


def test_daftar_kecil_terurut():
    status = {("AAA", "2024-01"): "HIDUP", ("AAA", "2024-02"): "HIDUP"}
    byte = {("AAA", "2024-01"): 300, ("AAA", "2024-02"): 100}
    daftar = ib.daftar_kecil(status, byte, "HIDUP", 1000)
    assert [b["byte"] for b in daftar] == [100, 300]


def test_daftar_kecil_dipotong():
    status = {("S%03d" % n, "2024-01"): "HIDUP" for n in range(45)}
    byte = {kunci: 10 for kunci in status}
    assert len(ib.daftar_kecil(status, byte, "HIDUP", 1000)) == 40


def test_daftar_kecil_medan():
    status, byte = _contoh()
    daftar = ib.daftar_kecil(status, byte, "MATI", 1000)
    assert set(daftar[0]) == {"simbol", "bulan", "byte"}


def test_daftar_kecil_kosong():
    status, byte = _contoh()
    assert ib.daftar_kecil(status, byte, "MATI", 1) == []


def test_kendali_data_sah():
    status, byte = _kendali_benar()
    sah, _rinci = ib.kendali_data(byte, status)
    assert sah is True


def test_kendali_data_byte_salah():
    status, byte = _kendali_benar()
    byte[("BTCUSDT", "2021-05")] = 1
    sah, _rinci = ib.kendali_data(byte, status)
    assert sah is False


def test_kendali_data_kunci_hilang():
    status, byte = _kendali_benar()
    byte.pop(("BTCUSDT", "2021-01"))
    sah, _rinci = ib.kendali_data(byte, status)
    assert sah is False


def test_kendali_data_kelas_bukan_hidup():
    status, byte = _kendali_benar()
    status[("BTCUSDT", "2021-05")] = "MATI"
    sah, _rinci = ib.kendali_data(byte, status)
    assert sah is False


def test_kendali_deteksi_sah():
    sah, _rinci = ib.kendali_deteksi()
    assert sah is True


def test_kendali_deteksi_rinci():
    _sah, rinci = ib.kendali_deteksi()
    assert (rinci["hidup_kecil"], rinci["mati_kecil"]) == (2, 1)


def test_kendali_deteksi_ambang_lain():
    sah, rinci = ib.kendali_deteksi(ambang=8)
    assert sah is True and rinci["hidup_kecil"] == 1


def test_selisih_nol():
    selisih = ib.selisih_invarian(dict(ib.INVARIAN))
    assert set(selisih.values()) == {0}


def test_selisih_bukan_nol():
    ringkas = dict(ib.INVARIAN)
    ringkas["penyebut"] = ringkas["penyebut"] + 3
    assert ib.selisih_invarian(ringkas)["selisih_penyebut"] == 3


def test_dalam_pita_tepi_bawah():
    assert ib.dalam_pita(20, (20, 600)) is True


def test_dalam_pita_tepi_atas():
    assert ib.dalam_pita(600, (20, 600)) is True


def test_dalam_pita_luar():
    assert ib.dalam_pita(19, (20, 600)) is False


def _ringkas_bohong(**ganti):
    ringkas = dict(ib.INVARIAN)
    ringkas.update(
        {
            "cacah_hidup_byte_kecil": 100,
            "cacah_mati_byte_kecil": 50,
            "kendali_data_sah": True,
            "kendali_deteksi_sah": True,
        }
    )
    ringkas.update(ib.selisih_invarian(ringkas))
    ringkas.update(ganti)
    return ringkas


def test_uji_butir1_menang():
    assert ib.uji_r308(_ringkas_bohong())["butir1"]["menang"] is True


def test_uji_butir1_kalah():
    ringkas = _ringkas_bohong(cacah_hidup_byte_kecil=5000)
    assert ib.uji_r308(ringkas)["butir1"]["menang"] is False


def test_uji_butir2_menang():
    assert ib.uji_r308(_ringkas_bohong())["butir2"]["menang"] is True


def test_uji_butir2_kalah():
    ringkas = _ringkas_bohong(cacah_mati_byte_kecil=0)
    assert ib.uji_r308(ringkas)["butir2"]["menang"] is False


def test_uji_penyebut_nol_tidak_teradjudikasi():
    ringkas = _ringkas_bohong(cacah_hidup=0)
    assert ib.uji_r308(ringkas)["butir1"]["teradjudikasi"] is False


def test_uji_butir3_menang():
    assert ib.uji_r308(_ringkas_bohong())["butir3"]["menang"] is True


def test_uji_butir3_kalah_selisih():
    ringkas = _ringkas_bohong(selisih_penyebut=1)
    assert ib.uji_r308(ringkas)["butir3"]["menang"] is False


def test_uji_butir3_kalah_kendali():
    ringkas = _ringkas_bohong(kendali_deteksi_sah=False)
    assert ib.uji_r308(ringkas)["butir3"]["menang"] is False


def test_kode_keluar_nol():
    assert ib.kode_keluar(ib.uji_r308(_ringkas_bohong())) == 0


def test_kode_keluar_satu():
    ringkas = _ringkas_bohong(kendali_data_sah=False)
    assert ib.kode_keluar(ib.uji_r308(ringkas)) == 1


def _tambal(monkeypatch):
    status, byte = _kendali_benar()
    status[("CCC", "2024-01")] = "MATI"
    byte[("CCC", "2024-01")] = 120000

    def palsu(akar, total):
        return status, byte, {"akar": akar, "total": total}

    monkeypatch.setattr(ib.silang_funding, "baca_laporan_kehidupan", palsu)


def test_jalankan_menulis_berkas(tmp_path, monkeypatch):
    _tambal(monkeypatch)
    ib.jalankan(str(tmp_path))
    assert (tmp_path / "reports" / "irisan_byte.json").exists()


def test_jalankan_medan_lengkap(tmp_path, monkeypatch):
    _tambal(monkeypatch)
    ringkas = ib.jalankan(str(tmp_path))
    assert ringkas["cacah_mati_byte_kecil"] == 1
    assert ringkas["kendali_data_sah"] is True
    assert ringkas["hasil"]["butir1"]["teradjudikasi"] is True


def test_jalankan_laporan_tidak_melebihi_batas(tmp_path, monkeypatch):
    _tambal(monkeypatch)
    ib.jalankan(str(tmp_path))
    isi = json.loads((tmp_path / "reports" / "irisan_byte.json").read_text())
    assert len(isi["daftar_hidup_kecil"]) <= ib.BATAS_BARIS_LAPORAN
    assert len(isi["daftar_mati_kecil"]) <= ib.BATAS_BARIS_LAPORAN
