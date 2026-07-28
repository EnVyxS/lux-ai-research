"""Uji pilot serapan. Tidak menyentuh jaringan (aturan 14)."""

from lux_ai.serapan import serap


def jenis_usdt(simbol):
    return "perpetual_usdt" if simbol.endswith("USDT") else "perpetual_usdc"


RENTANG = {
    "BTCUSDT": {"bulan_pertama": "2020-01", "bulan_terakhir": "2026-06"},
    "ETHUSDC": {"bulan_pertama": "2023-01", "bulan_terakhir": "2026-06"},
    "0GUSDT": {"bulan_pertama": "2025-09", "bulan_terakhir": "2026-06"},
    "BTSUSDT": {"bulan_pertama": "2020-03", "bulan_terakhir": "2023-04"},
    "\u5e01\u5b89\u4eba\u751fUSDT": {"bulan_pertama": "2024-02", "bulan_terakhir": "2026-06"},
}


def test_nama_aman_menyelamatkan_simbol_tionghoa():
    assert serap.nama_aman("\u5e01\u5b89\u4eba\u751fUSDT") == "u5E01u5B89u4EBAu751FUSDT"
    assert serap.nama_aman("BTCUSDT") == "BTCUSDT"
    assert serap.nama_aman("BTCUSDT_260327") == "BTCUSDT_260327"
    assert "/" not in serap.nama_aman("A/B")


def test_pilih_berlapis_mewakili_tiap_kelas_risiko():
    hasil = serap.pilih_berlapis(RENTANG, jenis_usdt)
    simbol = {s for s, _ in hasil}
    assert hasil == serap.pilih_berlapis(RENTANG, jenis_usdt)  # deterministik
    assert "ETHUSDC" not in simbol  # ADR-A005: hanya perpetual_usdt
    assert ("BTCUSDT", "2020-01") in hasil  # pra-header
    assert ("\u5e01\u5b89\u4eba\u751fUSDT", "2024-02") in hasil  # non-ASCII
    assert ("BTSUSDT", "2023-04") in hasil  # terhenti
    assert ("0GUSDT", "2025-09") in hasil  # kendali baru


def test_pilih_berlapis_tanpa_kandidat_tidak_meledak():
    assert serap.pilih_berlapis({}, jenis_usdt) == []
    hanya_usdc = {"ETHUSDC": {"bulan_pertama": "2023-01", "bulan_terakhir": "2026-06"}}
    assert serap.pilih_berlapis(hanya_usdc, jenis_usdt) == []


def test_kelas_risiko_dilaporkan_walau_nol():
    manifes = [
        {"simbol": "0GUSDT", "bulan": "2025-09", "berheader": True, "terhenti": False},
    ]
    kelas = serap.kelas_risiko_tersentuh(manifes)
    assert set(kelas) == set(serap.KELAS_RISIKO)
    assert kelas["pra_header"] == 0
    assert kelas["non_ascii"] == 0
    assert kelas["terhenti"] == 0
    assert kelas["bulan_awal_2020_2021"] == 0
    assert kelas["kendali_baru"] == 1


def test_kelas_risiko_menghitung_yang_tersentuh():
    manifes = [
        {"simbol": "BTCUSDT", "bulan": "2020-01", "berheader": False, "terhenti": False},
        {"simbol": "\u5e01\u5b89\u4eba\u751fUSDT", "bulan": "2024-02", "berheader": True, "terhenti": False},
        {"simbol": "BTSUSDT", "bulan": "2023-04", "berheader": True, "terhenti": True},
    ]
    kelas = serap.kelas_risiko_tersentuh(manifes)
    assert kelas["pra_header"] == 1
    assert kelas["non_ascii"] == 1
    assert kelas["terhenti"] == 1
    assert kelas["bulan_awal_2020_2021"] == 1


def test_ringkas_melaporkan_medan_penggugur_walau_nol():
    manifes = [
        {
            "simbol": "BTCUSDT",
            "bulan": "2020-01",
            "jenis_instrumen": "perpetual_usdt",
            "baris": 44640,
            "baris_dibuang": 0,
            "berheader": False,
            "byte_zip": 1000,
            "byte_parquet": 1500,
            "_putusan": {"lolos": True, "pelanggaran": [], "ukuran": {"baris": 44640, "slot_dalam_rentang": 44640}},
        }
    ]
    hasil = serap.ringkas(manifes)
    assert hasil["status"] == "TERUKUR"
    assert hasil["cacah_simbol_bulan_dengan_baris_dibuang"] == 0
    assert hasil["jumlah_baris_dibuang"] == 0
    assert hasil["nisbah_parquet_per_zip"] == 1.5
    assert hasil["gerbang"]["simbol_bulan_gagal"] == 0
    assert hasil["kelas_risiko_tersentuh"]["pra_header"] == 1
    assert "non_ascii" in hasil["kelas_risiko_kosong"]


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
    assert hasil["kelas_risiko_kosong"] == list(serap.KELAS_RISIKO)
