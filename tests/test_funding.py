"""Uji jalur funding tanpa jaringan sama sekali.

Sembilan fungsi uji, TANPA `parametrize`, sehingga cacah fungsi sama dengan
cacah butir yang dikumpulkan pytest. Ini disengaja: kekeliruan R-148 lahir dari
mencacah fungsi padahal pytest mencacah butir.
"""

from __future__ import annotations

import io
import zipfile

from lux_ai.serapan import funding


def _zip(nama: str, isi: str) -> bytes:
    penyangga = io.BytesIO()
    with zipfile.ZipFile(penyangga, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(nama, isi)
    return penyangga.getvalue()


def test_sidik_kode_heksadesimal_dan_stabil():
    a = funding.sidik_kode()
    b = funding.sidik_kode()
    assert a == b
    assert len(a) == 64
    assert all(ch in "0123456789abcdef" for ch in a)


def test_nama_keluaran_di_reports():
    assert funding.nama_keluaran() == "reports/funding_semesta.json"
    assert funding.nama_keluaran().startswith("reports/")


def test_selisih_bulan_melaporkan_dua_arah():
    beda = funding.selisih_bulan(["2024-01", "2024-02", "2024-03"], ["2024-02", "2024-09"])
    assert beda["klines_tanpa_funding"] == ["2024-01", "2024-03"]
    assert beda["funding_tanpa_klines"] == ["2024-09"]


def test_kelas_bulan_menandai_awal_dan_kendali():
    assert "bulan_awal_2020_2021" in funding.kelas_bulan("BTCUSDT", "2020-05", "2026-06")
    assert "kendali_baru" in funding.kelas_bulan("BTCUSDT", "2025-03", "2026-06")
    assert funding.kelas_bulan("BTCUSDT", "2023-07", "2026-06") == []


def test_kelas_bulan_menandai_non_ascii_dan_terhenti():
    kelas = funding.kelas_bulan("1000\u00d7USDT", "2023-07", "2024-05")
    assert "non_ascii" in kelas
    assert "terhenti" in kelas


def test_pilih_sampel_satu_wakil_tiap_kelas():
    kandidat = [
        {"simbol": "BBB", "bulan": "2021-01", "kelas": ["bulan_awal_2020_2021"]},
        {"simbol": "AAA", "bulan": "2021-02", "kelas": ["bulan_awal_2020_2021"]},
        {"simbol": "CCC", "bulan": "2025-06", "kelas": ["kendali_baru"]},
    ]
    dipilih = funding.pilih_sampel(kandidat)
    kelas = [d["kelas_terpilih"] for d in dipilih]
    assert kelas == ["bulan_awal_2020_2021", "kendali_baru"]
    # deterministik: yang terpilih adalah kandidat terkecil menurut abjad
    assert dipilih[0]["simbol"] == "AAA"
    # kelas tanpa kandidat tidak memaksa wakil
    assert "non_ascii" not in kelas


def test_baca_zip_funding_tanpa_header():
    isi = "1609459200000,8,0.00010000\n1609488000000,8,0.00012000\n"
    hasil = funding.baca_zip_funding(_zip("X-fundingRate-2021-01.csv", isi))
    assert hasil["berheader"] is False
    assert hasil["cacah_baris"] == 2


def test_baca_zip_funding_berheader():
    isi = (
        "calc_time,funding_interval_hours,last_funding_rate\n"
        "1735689600000,8,0.00005000\n"
    )
    hasil = funding.baca_zip_funding(_zip("X-fundingRate-2025-01.csv", isi))
    assert hasil["berheader"] is True
    assert hasil["cacah_baris"] == 1
    assert hasil["baris_pertama"].startswith("calc_time")


def test_ringkas_selisih_memotong_daftar_dan_melaporkannya():
    per_simbol = [
        {"simbol": "AAA", "klines_tanpa_funding": ["2024-01", "2024-02"], "funding_tanpa_klines": []},
        {"simbol": "BBB", "klines_tanpa_funding": ["2024-03"], "funding_tanpa_klines": ["2024-04"]},
    ]
    hasil = funding.ringkas_selisih(per_simbol, batas=2)
    assert hasil["cacah_bulan_klines_tanpa_funding"] == 3
    assert hasil["cacah_bulan_funding_tanpa_klines"] == 1
    assert len(hasil["daftar_klines_tanpa_funding"]) == 2
    assert hasil["daftar_terpotong"] is True
    assert hasil["batas_daftar"] == 2
