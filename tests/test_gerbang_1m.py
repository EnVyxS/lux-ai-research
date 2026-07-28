"""Uji gerbang integritas 1m. Tanpa jaringan (aturan 14).

Setiap klausa diuji dengan kasus POSITIF dan NEGATIF (semangat aturan 12):
gerbang yang hanya pernah melihat data bersih tidak diketahui bisa menolak.
"""
from __future__ import annotations

from lux_ai.serapan import diagnosa_kc6, gerbang_1m as g

AWAL = 1_577_836_800_000  # 2020-01-01T00:00:00Z
M = g.MS_MENIT


def deret(n: int, mulai: int = AWAL):
    return [mulai + i * M for i in range(n)]


def test_deret_bersih_lolos():
    hasil = g.nilai_deret(deret(60), "BTCUSDT", "2020-01")
    assert hasil["lolos"] is True
    assert hasil["pelanggaran"] == []
    assert hasil["ukuran"]["baris"] == 60
    assert hasil["ukuran"]["slot_dalam_rentang"] == 60


def test_deret_kosong_gagal():
    hasil = g.nilai_deret([], "BTCUSDT", "2020-01")
    assert hasil["lolos"] is False
    assert "deret_tidak_kosong" in hasil["pelanggaran"]
    assert "satuan_milidetik" in hasil["pelanggaran"]
    assert hasil["ukuran"]["menit_pertama"] is None


def test_duplikat_gagal():
    hasil = g.nilai_deret(deret(10) + [AWAL + 3 * M], "ETHUSDT", "2020-01")
    assert hasil["lolos"] is False
    assert hasil["pelanggaran"] == ["tanpa_duplikat"]
    assert hasil["ukuran"]["duplikat"] == 1
    assert hasil["ukuran"]["baris"] == 11


def test_menit_hilang_gagal_pada_dua_klausa():
    cap = [t for t in deret(10) if t != AWAL + 4 * M]
    hasil = g.nilai_deret(cap, "DOGEUSDT", "2020-01")
    assert hasil["lolos"] is False
    assert "tanpa_menit_hilang" in hasil["pelanggaran"]
    assert "jarak_60_detik" in hasil["pelanggaran"]
    assert hasil["ukuran"]["menit_hilang_dalam_rentang"] == 1
    assert hasil["ukuran"]["jarak_bukan_60_detik"] == 1


def test_cap_tidak_selaras_gagal():
    hasil = g.nilai_deret(deret(5) + [AWAL + 5 * M + 1234], "BTSUSDT", "2020-01")
    assert hasil["lolos"] is False
    assert "selaras_menit" in hasil["pelanggaran"]
    assert hasil["ukuran"]["cap_tidak_selaras_menit"] == 1


def test_satuan_detik_gagal():
    cap = [1_577_836_800 + i * 60 for i in range(10)]
    hasil = g.nilai_deret(cap, "XRPUSDT", "2020-01")
    assert hasil["lolos"] is False
    assert "satuan_milidetik" in hasil["pelanggaran"]
    assert (
        hasil["ukuran"]["satuan_stempel_dari_besaran"]
        == "bukan_milidetik_terlalu_kecil"
    )


def test_satuan_mikrodetik_gagal():
    cap = [1_577_836_800_000_000 + i * 60_000_000 for i in range(10)]
    hasil = g.nilai_deret(cap, "XRPUSDT", "2020-01")
    assert "satuan_milidetik" in hasil["pelanggaran"]
    assert (
        hasil["ukuran"]["satuan_stempel_dari_besaran"]
        == "bukan_milidetik_terlalu_besar"
    )


def test_satuan_campuran_gagal():
    cap = deret(3) + [1_577_836_800]
    assert g.satuan_stempel_dari_besaran(cap) == "campuran"
    assert "satuan_milidetik" in g.nilai_deret(cap)["pelanggaran"]


def test_mulai_tengah_bulan_bukan_pelanggaran():
    """Bulan pertama sebuah simbol mulai di tengah bulan; itu bukan celah."""
    hasil = g.nilai_deret(deret(120, AWAL + 15 * 1440 * M), "SOLUSDT", "2020-09")
    assert hasil["lolos"] is True


def test_ukur_deret_sepakat_dengan_diagnosa():
    kasus = [
        deret(30),
        deret(30) + [AWAL + 2 * M],
        [t for t in deret(30) if t != AWAL + 7 * M],
        [],
    ]
    for cap in kasus:
        kiri = g.ukur_deret(cap)
        kanan = diagnosa_kc6.celah_menit(cap)
        for medan in kanan:
            assert kiri[medan] == kanan[medan], (medan, cap[:3])


def test_klausa_berjumlah_enam_dan_dinilai_semua():
    hasil = g.nilai_deret(deret(5))
    assert len(g.KLAUSA) == 6
    assert set(hasil["klausa"]) == set(g.KLAUSA)


def test_ringkas_menghitung_lolos_dan_gagal():
    hasil = [
        g.nilai_deret(deret(10), "BTCUSDT", "2020-01"),
        g.nilai_deret(deret(10) + [AWAL], "ETHUSDT", "2020-01"),
    ]
    ringkas = g.ringkas_gerbang(hasil)
    assert ringkas["simbol_bulan_dinilai"] == 2
    assert ringkas["simbol_bulan_lolos"] == 1
    assert ringkas["simbol_bulan_gagal"] == 1
    assert ringkas["persen_lolos"] == 50.0
    assert ringkas["pelanggaran_per_klausa"]["tanpa_duplikat"] == 1
    assert ringkas["pelanggaran_per_klausa"]["selaras_menit"] == 0
    assert ringkas["baris_diperiksa"] == 21
    assert ringkas["slot_diperiksa"] == 20


def test_ringkas_kosong_tidak_mengaku_seratus_persen():
    ringkas = g.ringkas_gerbang([])
    assert ringkas["simbol_bulan_dinilai"] == 0
    assert ringkas["persen_lolos"] is None


def test_ringkas_contoh_gagal_maksimal_sepuluh():
    hasil = [g.nilai_deret([], f"S{i}", "2020-01") for i in range(14)]
    ringkas = g.ringkas_gerbang(hasil)
    assert ringkas["simbol_bulan_gagal"] == 14
    assert len(ringkas["contoh_gagal"]) == 10


def test_persen_menolak_penyebut_nol():
    assert g.persen(0, 0) is None
    assert g.persen(1, 3) == 33.33


def test_sidik_kode_hex_dan_stabil():
    satu = g.sidik_kode()
    assert len(satu) == 64
    assert satu == g.sidik_kode()
    assert satu != diagnosa_kc6.sidik_kode()
