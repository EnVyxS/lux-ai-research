"""Uji fungsi murni diagnosa KC-15 tepi bulan. Tanpa jaringan."""

import datetime as dt

from lux_ai.serapan import diagnosa_kc15 as k15
from lux_ai.serapan import serap

MS_MENIT = 60_000


def test_menit_kalender_termasuk_tahun_kabisat():
    assert k15.menit_kalender("2025-04") == 43_200
    assert k15.menit_kalender("2025-07") == 44_640
    assert k15.menit_kalender("2025-02") == 40_320
    assert k15.menit_kalender("2024-02") == 41_760


def test_awal_bulan_ms_cocok_dengan_utc():
    diharap = int(dt.datetime(2022, 4, 1, tzinfo=dt.timezone.utc).timestamp() * 1000)
    assert k15.awal_bulan_ms("2022-04") == diharap


def test_tanggal_tepi():
    assert k15.tanggal_tepi("2022-04") == ("2022-04-01", "2022-04-30")
    assert k15.tanggal_tepi("2025-02") == ("2025-02-01", "2025-02-28")


def test_ukur_tepi_bulan_utuh_nol():
    awal = k15.awal_bulan_ms("2022-04")
    akhir = awal + (k15.menit_kalender("2022-04") - 1) * MS_MENIT
    tepi = k15.ukur_tepi("2022-04", awal, akhir)
    assert tepi == {"tepi_awal": 0, "tepi_akhir": 0, "tepi_total": 0}


def test_ukur_tepi_menangkap_210_menit():
    awal = k15.awal_bulan_ms("2022-04")
    mulai = awal + 210 * MS_MENIT
    akhir = awal + (k15.menit_kalender("2022-04") - 1) * MS_MENIT
    tepi = k15.ukur_tepi("2022-04", mulai, akhir)
    assert tepi["tepi_awal"] == 210
    assert tepi["tepi_akhir"] == 0
    assert tepi["tepi_total"] == 210


def test_ukur_tepi_kedua_sisi():
    awal = k15.awal_bulan_ms("2025-07")
    mulai = awal + 30 * MS_MENIT
    akhir = awal + (k15.menit_kalender("2025-07") - 1 - 45) * MS_MENIT
    tepi = k15.ukur_tepi("2025-07", mulai, akhir)
    assert tepi == {"tepi_awal": 30, "tepi_akhir": 45, "tepi_total": 75}


def test_posisi_bulan():
    daftar = ["2022-01", "2022-02", "2022-03"]
    assert k15.posisi_bulan("2022-01", daftar) == "pertama"
    assert k15.posisi_bulan("2022-02", daftar) == "tengah"
    assert k15.posisi_bulan("2022-03", daftar) == "terakhir"
    assert k15.posisi_bulan("2021-12", daftar) == "tak_dikenal"


def test_bulan_tengah_terpilih_deterministik():
    assert k15.bulan_tengah_terpilih(["2022-01", "2022-02", "2022-03"]) == "2022-02"
    assert k15.bulan_tengah_terpilih(["2022-01", "2022-02"]) == ""
    assert k15.bulan_tengah_terpilih(["2022-01"]) == ""
    lima = ["2024-01", "2024-02", "2024-03", "2024-04", "2024-05"]
    assert k15.bulan_tengah_terpilih(lima) == "2024-03"


def test_kelas_simbol_menandai_lapis():
    kelas = k15.kelas_simbol(
        {"bulan_pertama": "2021-05", "bulan_terakhir": "2023-01"}, "BNXUSDT"
    )
    assert "pra_header" in kelas and "terhenti" in kelas
    baru = k15.kelas_simbol(
        {"bulan_pertama": "2025-06", "bulan_terakhir": "2026-07"}, "AIAUSDT"
    )
    assert baru == ["kendali_baru"]


def test_kelas_dengan_bulan_menandai_bulan_pra_2022():
    assert k15.kelas_dengan_bulan(["pra_header"], "2021-06") == [
        "pra_header",
        "bulan_awal_2020_2021",
    ]
    assert k15.kelas_dengan_bulan(["pra_header"], "2022-04") == ["pra_header"]
    # idempoten
    sekali = k15.kelas_dengan_bulan(["pra_header"], "2020-12")
    assert k15.kelas_dengan_bulan(sekali, "2020-12") == sekali


def test_seluruh_kelas_risiko_dapat_ditandai():
    """Aturan 37: tiap kelas di serap.KELAS_RISIKO harus bisa muncul."""
    kelas = k15.kelas_dengan_bulan(
        k15.kelas_simbol(
            {"bulan_pertama": "2021-01", "bulan_terakhir": "2023-01"}, "AB\u00c7USDT"
        ),
        "2021-06",
    )
    assert set(kelas) >= {"pra_header", "terhenti", "non_ascii", "bulan_awal_2020_2021"}
    assert set(serap.KELAS_RISIKO) - set(kelas) == {"kendali_baru"}


def test_pilih_simbol_mewakili_kelas_dan_deterministik():
    rentang = {
        "AUSDT": {"bulan_pertama": "2025-06", "bulan_terakhir": "2026-07"},
        "BUSDT": {"bulan_pertama": "2020-09", "bulan_terakhir": "2026-07"},
        "CUSDT": {"bulan_pertama": "2023-01", "bulan_terakhir": "2024-02"},
        "DUSDT": {"bulan_pertama": "2023-05", "bulan_terakhir": "2026-07"},
    }
    hasil = k15.pilih_simbol(rentang, list(rentang), banyak=3)
    assert len(hasil) == 3
    assert "BUSDT" in hasil  # pra_header
    assert "CUSDT" in hasil  # terhenti
    assert hasil == k15.pilih_simbol(rentang, list(reversed(list(rentang))), banyak=3)


def test_putusan_tepi_empat_cabang():
    assert k15.putusan_tepi(0, 0, 0) == "TEPI_BERSIH"
    assert k15.putusan_tepi(210, 0, 0) == "TIDAK MENGUKUR"
    assert k15.putusan_tepi(210, 210, 1) == "TEPI_TERPOTONG"
    assert k15.putusan_tepi(210, 0, 1) == "TEPI_TAK_TERJELASKAN"


def test_ringkas_menghitung_gerbang_buta():
    catatan = [
        {
            "simbol": "BNXUSDT",
            "bulan": "2022-04",
            "posisi": "tengah",
            "bulanan_tersedia": True,
            "cacah_baris_1m": 41550,
            "kelas": ["pra_header", "terhenti"],
            "tepi_total": 210,
            "menit_tepi_hadir_di_harian": 210,
            "gerbang_lolos": True,
            "hari_tepi_diperiksa": 1,
            "hari_tepi_tidak_tersedia": 0,
            "selisih_tak_terjelaskan": 0,
            "putusan": "TEPI_TERPOTONG",
        },
        {
            "simbol": "AUSDT",
            "bulan": "2025-03",
            "posisi": "pertama",
            "bulanan_tersedia": True,
            "cacah_baris_1m": 1000,
            "kelas": ["kendali_baru"],
            "tepi_total": 500,
            "menit_tepi_hadir_di_harian": 0,
            "gerbang_lolos": True,
            "hari_tepi_diperiksa": 1,
            "hari_tepi_tidak_tersedia": 0,
            "selisih_tak_terjelaskan": 0,
            "putusan": "TEPI_TAK_TERJELASKAN",
        },
    ]
    hasil = k15.ringkas(catatan)
    assert hasil["status"] == "TERUKUR"
    assert hasil["bulan_tengah_diperiksa"] == 1
    assert hasil["cacah_bulan_pertama_dikecualikan"] == 1
    # bulan pertama TIDAK ikut menghitung tepi
    assert hasil["total_menit_tepi"] == 210
    assert hasil["cacah_gerbang_lolos_padahal_tepi_terpotong"] == 1
    assert hasil["kelas_risiko_kosong"] == ["non_ascii", "bulan_awal_2020_2021"]


def test_ringkas_tanpa_bulan_tengah_tidak_mengukur():
    hasil = k15.ringkas(
        [{"posisi": "pertama", "bulanan_tersedia": True, "cacah_baris_1m": 5, "putusan": "TEPI_BERSIH"}]
    )
    assert hasil["status"] == "TIDAK MENGUKUR"
    assert hasil["bulan_tengah_diperiksa"] == 0
