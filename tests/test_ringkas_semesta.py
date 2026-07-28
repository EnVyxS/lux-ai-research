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
    assert bersih["status"] == rs.MENGUKUR

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

    # Aturan 30: penyebut nol tidak boleh tampak bersih (KC-7).
    assert rs.ringkas({})["status"] == rs.TIDAK_MENGUKUR


def test_jalur_cacah_menerima_simbol_ke_angka_dan_menolak_yang_bukan_angka():
    terkumpul = rs.kumpulkan_cacah(
        {
            "bulan_per_simbol": {
                "0GUSDT": 10,
                "BTCUSDT": 78,
                "XXXUSDT": "sepuluh",
                "YYYUSDT": True,
            },
            "waktu_utc": "2026-07-28T09:09:38Z",
        }
    )
    # bool BUKAN angka di sini; kalau lolos, cacah akan terhitung 1 secara diam-diam.
    assert terkumpul["peta"] == {"0GUSDT": 10, "BTCUSDT": 78}
    assert terkumpul["cacah_nilai_bukan_angka"] == 2

    hasil = rs.ringkas_cacah(terkumpul["peta"])
    assert hasil["cacah_simbol"] == 2
    assert hasil["total_berkas_bulan"] == 88
    assert hasil["cacah_minimum"] == 10
    assert hasil["cacah_maksimum"] == 78
    assert hasil["simbol_minimum"] == ["0GUSDT"]
    assert hasil["cacah_nilai_negatif"] == 0
    assert hasil["cacah_nilai_melebihi_78"] == 0
    assert hasil["status"] == rs.MENGUKUR

    aneh = rs.ringkas_cacah({"XUSDT": -1, "YUSDT": 100})
    assert aneh["cacah_nilai_negatif"] == 1
    assert aneh["cacah_nilai_melebihi_78"] == 1
    assert rs.ringkas_cacah({})["status"] == rs.TIDAK_MENGUKUR


def test_kunci_ditolak_pola_dihitung_bukan_dibuang_diam_diam():
    # Nama 21 aksara: melebihi batas POLA_SIMBOL, nilainya tetap angka.
    panjang = "AERGOUSDTSETTLEDXTRAA"
    assert len(panjang) == 21
    terkumpul = rs.kumpulkan_cacah(
        {
            "bulan_per_simbol": {
                "BTCUSDT": 78,
                panjang: 5,
                "huruf kecil": 7,
            },
            "waktu_utc": "2026-07-28T09:23:59Z",
        }
    )
    assert terkumpul["peta"] == {"BTCUSDT": 78}
    assert terkumpul["cacah_kunci_ditolak_pola"] == 2
    assert panjang in terkumpul["contoh_kunci_ditolak"]
    assert terkumpul["panjang_nama_terpanjang"] == 21
    assert terkumpul["cacah_nilai_bukan_angka"] == 0

    # Kasus negatif: tanpa kunci menyimpang, penggugur wajib tetap ada dan nol.
    rapi = rs.kumpulkan_cacah({"bulan_per_simbol": {"BTCUSDT": 78}})
    assert rapi["cacah_kunci_ditolak_pola"] == 0
    assert rapi["contoh_kunci_ditolak"] == []


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
    assert isi["status"] == rs.TIDAK_MENGUKUR
    assert "ringkas" not in isi

    # Jalur daftar bulan.
    sumber.write_text('{"per_simbol": {"BTCUSDT": ["2020-01"]}}', encoding="utf-8")
    assert rs.jalankan() == 0
    isi = _json.loads(laporan.read_text(encoding="utf-8"))
    assert isi["jalur"] == "daftar_bulan"
    assert isi["bentuk_tak_dikenali"] is False
    assert isi["ringkas"]["cacah_simbol"] == 1
    assert isi["ringkas"]["entri_simbol_bulan"] == 1
    assert isi["sidik_data"]

    # Jalur cacah bulan, bentuk sebenarnya berkas semesta.
    sumber.write_text(
        '{"bulan_per_simbol": {"0GUSDT": 10, "BTCUSDT": 78, "nama_panjang_sekali_x": 1},'
        ' "waktu_utc": "x"}',
        encoding="utf-8",
    )
    assert rs.jalankan() == 0
    isi = _json.loads(laporan.read_text(encoding="utf-8"))
    assert isi["jalur"] == "cacah_bulan"
    assert isi["bentuk_tak_dikenali"] is False
    assert isi["ringkas_cacah"]["total_berkas_bulan"] == 88
    assert isi["cacah_kunci_ditolak_pola"] == 1
    assert isi["jumlah_diterima_dan_ditolak"] == 3
    assert isi["status"] == rs.MENGUKUR
