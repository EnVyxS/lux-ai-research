"""Uji fungsi murni diagnosa KC-14 (tanpa jaringan)."""

from lux_ai.serapan import diagnosa_kc14 as d

M = d.MS_MENIT


def test_menit_hilang_kosong_saat_rapat():
    assert d.menit_hilang([0, M, 2 * M]) == []


def test_menit_hilang_hanya_di_dalam_rentang():
    # lubang di menit 1 dan 3; menit sebelum awal dan sesudah akhir bukan lubang
    assert d.menit_hilang([0, 2 * M, 4 * M]) == [M, 3 * M]


def test_menit_hilang_deret_pendek():
    assert d.menit_hilang([]) == []
    assert d.menit_hilang([5 * M]) == []


def test_blok_menyambung_yang_bersebelahan():
    hasil = d.blok([M, 2 * M, 3 * M])
    assert len(hasil) == 1
    assert hasil[0]["panjang_menit"] == 3
    assert hasil[0]["mulai_ms"] == M and hasil[0]["akhir_ms"] == 3 * M


def test_blok_memisah_yang_terpencar():
    hasil = d.blok([M, 5 * M])
    assert [b["panjang_menit"] for b in hasil] == [1, 1]


def test_slot_naungan_membulat_ke_bawah():
    assert d.slot_naungan(7 * M, "5m") == 5 * M
    assert d.slot_naungan(7 * M, "15m") == 0
    assert d.slot_naungan(15 * M, "15m") == 15 * M


def test_ringkas_tanpa_catatan_tidak_mengukur():
    r = d.ringkas([])
    assert r["status"] == "TIDAK MENGUKUR"
    assert r["simbol_bulan_diperiksa"] == 0


def test_ringkas_menghitung_medan_penggugur():
    catatan = [
        {
            "cacah_menit_hilang": 10,
            "putusan": "MENDUKUNG_H-A002b",
            "checksum_stabil": True,
            "banding": {"5m": {"slot_hadir_saat_1m_hilang": 2}},
        },
        {
            "cacah_menit_hilang": 5,
            "putusan": "MENDUKUNG_H-A002a",
            "checksum_stabil": False,
            "banding": {"5m": {"slot_hadir_saat_1m_hilang": 0}},
        },
    ]
    r = d.ringkas(catatan)
    assert r["total_menit_hilang"] == 15
    assert r["slot_5m_hadir_saat_1m_hilang"] == 2
    assert r["cacah_mendukung_h_a002b"] == 1
    assert r["cacah_mendukung_h_a002a"] == 1
    assert r["cacah_checksum_tak_stabil"] == 1
