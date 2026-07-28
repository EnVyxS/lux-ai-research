"""Uji selisih definisi terhenti (utang 28)."""

from lux_ai.semesta import terhenti as H
from lux_ai.serapan import survei


def test_salinan_selisih_bulan_sepakat_dengan_survei():
    kasus = [
        ("2026-05", "2026-06"),
        ("2026-04", "2026-06"),
        ("2020-01", "2026-06"),
        ("2026-06", "2026-06"),
        ("2026-07", "2026-06"),
    ]
    for lebih_tua, acuan in kasus:
        assert H.selisih_bulan(lebih_tua, acuan) == survei.selisih_bulan(lebih_tua, acuan)


def test_definisi_survei_sama_dengan_fungsi_asli():
    for bulan in ("2026-06", "2026-05", "2026-04", "2024-05"):
        assert H.terhenti_survei(bulan, "2026-06") == survei.terhenti(bulan, "2026-06")


def test_mundur_bulan_melewati_pergantian_tahun():
    assert H.mundur_bulan("2026-06", 0) == "2026-06"
    assert H.mundur_bulan("2026-06", 1) == "2026-05"
    assert H.mundur_bulan("2026-01", 1) == "2025-12"
    assert H.mundur_bulan("2026-01", 13) == "2024-12"


def test_selisih_himpunan_menyebut_nama_dan_arah():
    rentang = {
        "HIDUP": {"bulan_pertama": "2020-01", "bulan_terakhir": "2026-06", "cacah_bulan": 78},
        "BATAS": {"bulan_pertama": "2020-01", "bulan_terakhir": "2026-05", "cacah_bulan": 77},
        "MATI": {"bulan_pertama": "2020-01", "bulan_terakhir": "2024-05", "cacah_bulan": 53},
    }
    laporan = H.bandingkan(rentang)
    assert laporan["bulan_tutup_terakhir"] == "2026-06"
    assert laporan["ambang_survei"] == "2026-04"
    assert laporan["ambang_taksonomi"] == "2026-05"
    assert laporan["cacah_terhenti_survei"] == 1
    assert laporan["cacah_terhenti_taksonomi"] == 2
    assert laporan["hanya_taksonomi"] == ["BATAS"]
    # Medan penggugur: arah sebaliknya harus KOSONG bila sebabnya cuma ambang.
    assert laporan["hanya_survei"] == []
    assert laporan["cacah_per_bulan_terakhir_ekor"]["2026-05"] == 1
    assert laporan["cacah_per_bulan_terakhir_ekor"]["2026-04"] == 0


def test_penyebut_nol_berstatus_tidak_mengukur():
    laporan = H.bandingkan({})
    assert laporan["status"] == "TIDAK MENGUKUR"
    assert laporan["penyebut"]["cacah_simbol"] == 0
    assert laporan["hanya_survei"] == []
    assert laporan["bulan_tutup_terakhir"] is None
