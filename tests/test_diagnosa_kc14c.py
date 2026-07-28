"""Uji fungsi murni diagnosa KC-14c. Tanpa jaringan (aturan 13-14)."""

from lux_ai.serapan import diagnosa_kc14 as k14
from lux_ai.serapan import diagnosa_kc14c as k14c

MS_MENIT = 60_000
MS_HARI = 86_400_000


def test_tanggal_dari_ms_batas_hari():
    assert k14c.tanggal_dari_ms(1744761600000) == "2025-04-16"
    assert k14c.tanggal_dari_ms(1744761600000 + 86_399_000) == "2025-04-16"
    assert k14c.tanggal_dari_ms(1744761600000 + MS_HARI) == "2025-04-17"


def test_kelompok_per_tanggal_memecah_lintas_hari():
    mulai = 1744761600000 - 2 * MS_MENIT
    menit = [mulai + i * MS_MENIT for i in range(5)]
    kelompok = k14c.kelompok_per_tanggal(menit)
    assert sorted(kelompok) == ["2025-04-15", "2025-04-16"]
    assert len(kelompok["2025-04-15"]) == 2
    assert len(kelompok["2025-04-16"]) == 3


def test_blok_mulai_batas_hari_dihitung_benar():
    daftar = k14.blok([1744761600000 + i * MS_MENIT for i in range(3)])
    assert k14c.cacah_blok_mulai_batas_hari(daftar) == 1
    geser = k14.blok([1744761600000 + MS_MENIT + i * MS_MENIT for i in range(3)])
    assert k14c.cacah_blok_mulai_batas_hari(geser) == 0


def test_kelipatan_15():
    assert k14c.kelipatan_15(660)
    assert k14c.kelipatan_15(705)
    assert not k14c.kelipatan_15(661)


def test_putusan_dari_tiga_cabang():
    assert k14c.putusan_dari(0, 0) == "TIDAK MENGUKUR"
    assert k14c.putusan_dari(0, 2) == "H-A003_GUGUR"
    assert k14c.putusan_dari(1, 2) == "MENDUKUNG_H-A003"


def test_tersangka_lengkap_sembilan_dan_unik():
    assert len(k14c.TERSANGKA) == 9
    assert len({(s, b) for s, b, _ in k14c.TERSANGKA}) == 9
    assert sum(k14c.MENIT_HILANG_GERBANG.values()) == 11700


def test_ringkas_menandai_ketidakcocokan_gerbang():
    catatan = [
        {
            "simbol": "XUSDT",
            "bulan": "2025-07",
            "pecahan": 1,
            "bulanan_tersedia": True,
            "cacah_menit_hilang": 5,
            "menit_hadir_di_harian_saat_bulanan_hilang": 0,
            "hari_diperiksa": 1,
            "hari_tidak_tersedia": 0,
            "hari_dilewati": 0,
            "putusan": "H-A003_GUGUR",
        }
    ]
    hasil = k14c.ringkas(catatan)
    assert hasil["status"] == "TERUKUR"
    assert hasil["total_menit_hilang"] == 5
    assert hasil["cacah_pecahan_tak_cocok"] == 1
    assert hasil["cacah_h_a003_gugur"] == 1


def test_ringkas_tanpa_bulanan_tidak_mengukur():
    hasil = k14c.ringkas([{"putusan": "TIDAK MENGUKUR", "bulanan_tersedia": False}])
    assert hasil["status"] == "TIDAK MENGUKUR"
    assert hasil["simbol_bulan_diperiksa"] == 0
