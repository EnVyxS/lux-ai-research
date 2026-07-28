"""Uji pilot serapan. Tidak menyentuh jaringan (aturan 14)."""

from lux_ai.serapan import serap


def test_nama_aman_menyelamatkan_simbol_tionghoa():
    # KC-9: nama non-ASCII tidak boleh hilang, hanya diubah bentuknya.
    hasil = serap.nama_aman("\u5e01\u5b89\u4eba\u751fUSDT")
    assert hasil == "u5E01u5B89u4EBAu751FUSDT"
    assert serap.nama_aman("BTCUSDT") == "BTCUSDT"
    assert serap.nama_aman("BTCUSDT_260327") == "BTCUSDT_260327"
    assert "/" not in serap.nama_aman("A/B")


def test_pilih_pilot_hanya_perpetual_usdt_dan_deterministik():
    rentang = {
        "BTCUSDT": {"bulan_pertama": "2020-01", "bulan_terakhir": "2026-06"},
        "ETHUSDC": {"bulan_pertama": "2023-01", "bulan_terakhir": "2026-06"},
        "AAVEUSDT": {"bulan_pertama": "2020-10", "bulan_terakhir": "2026-06"},
    }

    def jenis(simbol):
        return "perpetual_usdt" if simbol.endswith("USDT") else "perpetual_usdc"

    a = serap.pilih_pilot(rentang, jenis, cacah_simbol=2)
    b = serap.pilih_pilot(rentang, jenis, cacah_simbol=2)
    assert a == b
    assert all(s.endswith("USDT") for s, _ in a)
    assert ("AAVEUSDT", "2020-10") in a
    assert ("BTCUSDT", "2020-01") in a
    # Bulan tengah masa hidup ikut terpilih sebagai kendali.
    assert ("BTCUSDT", "2023-03") in a


def test_ringkas_melaporkan_medan_penggugur_walau_nol():
    manifes = [
        {
            "simbol": "BTCUSDT",
            "bulan": "2020-01",
            "jenis_instrumen": "perpetual_usdt",
            "baris": 44640,
            "baris_dibuang": 0,
            "byte_zip": 1000,
            "byte_parquet": 1500,
            "_putusan": {"lolos": True, "pelanggaran": [], "ukuran": {"baris": 44640, "slot_dalam_rentang": 44640}},
        }
    ]
    hasil = serap.ringkas(manifes)
    assert hasil["status"] == "TERUKUR"
    assert hasil["cacah_simbol_bulan_dengan_baris_dibuang"] == 0
    assert hasil["jumlah_baris_dibuang"] == 0
    assert hasil["cacah_gagal_unduh"] == 0
    assert hasil["nisbah_parquet_per_zip"] == 1.5
    assert hasil["gerbang"]["simbol_bulan_gagal"] == 0
    assert hasil["jenis_instrumen_unik"] == ["perpetual_usdt"]


def test_ringkas_menghitung_baris_dibuang_yang_tidak_nol():
    manifes = [
        {"baris": 10, "baris_dibuang": 2, "byte_zip": 10, "byte_parquet": 10, "jenis_instrumen": "perpetual_usdt"},
        {"baris": 10, "baris_dibuang": 0, "byte_zip": 10, "byte_parquet": 10, "jenis_instrumen": "perpetual_usdt"},
        {"gagal_unduh": True, "gagal_checksum": True, "jenis_instrumen": "perpetual_usdt"},
    ]
    hasil = serap.ringkas(manifes)
    assert hasil["cacah_simbol_bulan_dengan_baris_dibuang"] == 1
    assert hasil["jumlah_baris_dibuang"] == 2
    assert hasil["cacah_gagal_unduh"] == 1
    assert hasil["cacah_gagal_checksum"] == 1
    assert hasil["penyebut"]["simbol_bulan_terunduh"] == 2


def test_penyebut_nol_berstatus_tidak_mengukur():
    hasil = serap.ringkas([])
    assert hasil["status"] == "TIDAK MENGUKUR"
    assert hasil["penyebut"]["simbol_bulan_diminta"] == 0
    assert hasil["nisbah_parquet_per_zip"] is None
