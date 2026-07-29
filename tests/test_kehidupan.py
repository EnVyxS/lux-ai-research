"""Uji pengukur kehidupan per simbol-bulan (ADR-A008 Keputusan 2-4).

Tiga belas fungsi uji, enam belas butir pytest: dua belas fungsi berbutir
tunggal ditambah satu fungsi berparameter empat kasus atas tabel klasifikasi.

Tidak satu pun uji di berkas ini menyentuh jaringan: pengukur dan pendaftar
bulan selalu disuntikkan.
"""
from __future__ import annotations

import pytest

from lux_ai.serapan import arsip, kehidupan


def _baris(**ubah):
    dasar = {
        "simbol": "XUSDT",
        "bulan": "2025-08",
        "peran": "kohort",
        "ada_di_arsip": True,
        "galat": None,
        "cacah_lilin": 43200,
        "transaksi_total": 0,
        "bagian_volume_nol": 1.0,
    }
    dasar.update(ubah)
    dasar["status"] = kehidupan.klasifikasi(dasar)
    return dasar


def test_deret_bulan_inklusif_dan_menaik():
    assert kehidupan.deret_bulan("2025-11", "2026-02") == [
        "2025-11",
        "2025-12",
        "2026-01",
        "2026-02",
    ]


def test_deret_bulan_kosong_saat_akhir_mendahului_mulai():
    assert kehidupan.deret_bulan("2026-06", "2025-07") == []
    assert kehidupan.deret_bulan("2025-13", "2026-01") == []


def test_klasifikasi_mati_saat_transaksi_nol():
    baris = _baris(transaksi_total=0, bagian_volume_nol=1.0)
    assert baris["status"] == kehidupan.STATUS_MATI


def test_klasifikasi_tak_terukur_saat_galat():
    baris = _baris(galat="checksum tidak cocok", transaksi_total=99)
    assert baris["status"] == kehidupan.STATUS_TAK_TERUKUR


def test_klasifikasi_tak_terukur_saat_tanpa_lilin():
    baris = _baris(cacah_lilin=0, transaksi_total=0)
    assert baris["status"] == kehidupan.STATUS_TAK_TERUKUR


@pytest.mark.parametrize(
    "transaksi,bagian_nol,harapan",
    [
        (0, 1.0, kehidupan.STATUS_MATI),
        (5, 0.9, kehidupan.STATUS_SEPI),
        (5, 0.5, kehidupan.STATUS_SEPI),
        (5, 0.1, kehidupan.STATUS_HIDUP),
    ],
)
def test_tabel_klasifikasi(transaksi, bagian_nol, harapan):
    baris = _baris(transaksi_total=transaksi, bagian_volume_nol=bagian_nol)
    assert baris["status"] == harapan


def test_ukur_simbol_menandai_bulan_tak_ada_di_arsip():
    dipanggil = []

    def ukur(simbol, bulan, peran):
        dipanggil.append(bulan)
        return _baris(simbol=simbol, bulan=bulan, transaksi_total=0)

    hasil = kehidupan.ukur_simbol(
        "AGIXUSDT",
        ["2025-07", "2025-08"],
        ukur=ukur,
        daftar=lambda s: ["2025-07"],
    )
    assert dipanggil == ["2025-07"]
    assert hasil[1]["ada_di_arsip"] is False
    assert hasil[1]["status"] == kehidupan.STATUS_TAK_TERUKUR


def test_ukur_simbol_melaporkan_galat_daftar():
    def daftar(simbol):
        raise RuntimeError("listing gagal")

    def ukur(simbol, bulan, peran):  # pragma: no cover - tidak boleh terpanggil
        raise AssertionError("tidak boleh mengunduh saat listing gagal")

    hasil = kehidupan.ukur_simbol("AMBUSDT", ["2025-07"], ukur=ukur, daftar=daftar)
    assert hasil[0]["gagal_unduh"] is True
    assert "listing gagal" in hasil[0]["galat"]
    assert hasil[0]["status"] == kehidupan.STATUS_TAK_TERUKUR


def test_penyebut_ganda_menerbitkan_dua_penyebut():
    baris = [
        _baris(transaksi_total=0),
        _baris(transaksi_total=0),
        _baris(transaksi_total=7, bagian_volume_nol=0.9),
        _baris(transaksi_total=7, bagian_volume_nol=0.1),
        _baris(ada_di_arsip=False),
    ]
    angka = kehidupan.penyebut_ganda(baris)
    assert angka["penyebut_penuh"] == 4
    assert angka["penyebut_tanpa_mati"] == 2
    assert angka["cacah_mati"] == 2
    assert angka["cacah_sepi"] == 1
    assert angka["cacah_hidup"] == 1
    assert angka["penyebut_tanpa_mati_kosong"] is False


def test_penyebut_tanpa_mati_kosong_saat_semua_mati():
    baris = [_baris(transaksi_total=0) for _ in range(3)]
    angka = kehidupan.penyebut_ganda(baris)
    assert angka["penyebut_penuh"] == 3
    assert angka["penyebut_tanpa_mati"] == 0
    assert angka["penyebut_tanpa_mati_kosong"] is True
    assert angka["bagian_mati"] == 1.0
    assert angka["lilin_tanpa_mati"] == 0


def test_ringkas_parser_terbukti_false_saat_kendali_tidak_hidup():
    baris = [_baris(transaksi_total=0)]
    kendali_mati = [_baris(simbol="BTCUSDT", peran="kendali_hidup", transaksi_total=0)]
    kendali_hidup = [
        _baris(
            simbol="BTCUSDT",
            peran="kendali_hidup",
            transaksi_total=1000,
            bagian_volume_nol=0.0,
        )
    ]
    assert kehidupan.ringkas(baris, kendali_mati)["parser_terbukti"] is False
    assert kehidupan.ringkas(baris, kendali_hidup)["parser_terbukti"] is True
    assert kehidupan.ringkas(baris, [])["parser_terbukti"] is False


def test_ringkas_mencacah_gagal_checksum():
    baris = [
        _baris(galat="checksum tidak cocok", gagal_checksum=True),
        _baris(transaksi_total=0),
    ]
    ringkasan = kehidupan.ringkas(baris, [])
    assert ringkasan["cacah_gagal_checksum"] == 1
    assert ringkasan["cacah_simbol_bulan_diminta"] == 2
    assert ringkasan["cacah_simbol_bulan_terukur"] == 1
    assert ringkasan["cacah_simbol_bulan_tak_terukur"] == 1


def test_jalankan_tanpa_sumber_tidak_mengunduh_apa_pun(tmp_path, monkeypatch):
    def jangan(*args, **kwargs):  # pragma: no cover - tidak boleh terpanggil
        raise AssertionError("jalankan tidak boleh menyentuh jaringan tanpa kohort")

    monkeypatch.setattr(arsip, "unduh_terverifikasi", jangan)
    monkeypatch.setattr(arsip, "bulan_tersedia", jangan)
    laporan = kehidupan.jalankan(str(tmp_path))
    assert laporan["galat_kohort"]
    assert laporan["baris"] == []
    assert laporan["ringkasan"]["parser_terbukti"] is False
    assert laporan["ringkasan"]["cacah_simbol_bulan_diminta"] == 0
