from lux_ai.serapan import ringkas_semesta as rs


def test_kumpulkan_menemukan_peta_simbol_bulan_sedalam_apa_pun():
    akar = {
        "meta": {"dibuat": "2026-07-28", "versi": 3},
        "per_simbol": {
            "BTCUSDT": ["2020-01", "2020-02"],
            "ETHUSDT": [{"bulan": "2021-05"}, {"bulan": "2021-06"}],
        },
        "lain": [{"dalam": {"BTSUSDT": ["2024-05"]}}],
    }
    peta = rs.kumpulkan(akar)
    assert peta == {
        "BTCUSDT": ["2020-01", "2020-02"],
        "ETHUSDT": ["2021-05", "2021-06"],
        "BTSUSDT": ["2024-05"],
    }
    # Kasus negatif: kunci yang bukan simbol dan nilai yang bukan bulan diabaikan.
    assert rs.kumpulkan({"catatan": "bukan bulan", "versi": 3}) == {}


def test_medan_penggugur_dilaporkan_walau_nol_dan_menangkap_pelanggaran():
    bersih = rs.ringkas({"BTCUSDT": ["2020-01", "2020-02"]})
    assert bersih["cacah_simbol"] == 1
    assert bersih["entri_simbol_bulan"] == 2
    assert bersih["bulan_duplikat"] == 0
    assert bersih["bulan_tidak_terurut"] == 0
    assert bersih["cacah_bulan_di_luar_rentang_survei"] == 0
    assert bersih["cacah_simbol_tanpa_bulan"] == 0
    assert bersih["bulan_paling_awal"] == "2020-01"
    assert bersih["bulan_paling_akhir"] == "2020-02"

    kotor = rs.ringkas(
        {
            "AAAUSDT": ["2020-02", "2020-01"],
            "BBBUSDT": ["2021-03", "2021-03"],
            "CCCUSDT": ["2019-12", "2027-01"],
            "DDDUSDT": [],
            "EEEUSDT": ["2024-04", "2024-05"],
        }
    )
    assert kotor["bulan_tidak_terurut"] == 1
    assert kotor["bulan_duplikat"] == 1
    assert kotor["cacah_bulan_di_luar_rentang_survei"] == 2
    assert kotor["simbol_tanpa_bulan"] == ["DDDUSDT"]
    assert kotor["simbol_akhir_2024_05"] == 1
    assert kotor["entri_simbol_bulan"] == 8


def test_bentuk_tak_dikenali_ditandai_bukan_ditebak(tmp_path, monkeypatch):
    sumber = tmp_path / "semesta_bulan_1m.json"
    laporan = tmp_path / "ringkas_semesta.json"
    monkeypatch.setattr(rs, "SUMBER", sumber)
    monkeypatch.setattr(rs, "LAPORAN", laporan)

    # Sumber tidak ada: menolak berbohong, menandai bentuk_tak_dikenali.
    assert rs.jalankan() == 1
    import json as _json

    isi = _json.loads(laporan.read_text(encoding="utf-8"))
    assert isi["bentuk_tak_dikenali"] is True
    assert isi["bukan_bukti"] is True
    assert "ringkas" not in isi

    # Sumber ada dan dikenali: melaporkan angka, bukan menandai tak dikenali.
    sumber.write_text('{"per_simbol": {"BTCUSDT": ["2020-01"]}}', encoding="utf-8")
    assert rs.jalankan() == 0
    isi = _json.loads(laporan.read_text(encoding="utf-8"))
    assert isi["bentuk_tak_dikenali"] is False
    assert isi["ringkas"]["cacah_simbol"] == 1
    assert isi["ringkas"]["entri_simbol_bulan"] == 1
    assert isi["sidik_data"]
