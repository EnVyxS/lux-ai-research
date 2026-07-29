"""Uji selisih definisi terhenti (utang 28) dan penguraian per jenis (V2).

Daftar bernomor agar cacah butirnya dapat diramalkan, bukan ditaksir
(aturan 54, 56, 57). Delapan belas butir:

1. test_salinan_selisih_bulan_sepakat_dengan_survei
2. test_definisi_survei_sama_dengan_fungsi_asli
3. test_mundur_bulan_melewati_pergantian_tahun
4. test_selisih_himpunan_menyebut_nama_dan_arah
5. test_penyebut_nol_berstatus_tidak_mengukur
6. test_versi_dua
7. test_sidik_kode_mencakup_taksonomi
8. test_berkas_dicap_terurut_dan_memuat_dua_berkas
9. test_terhenti_per_jenis_menjumlah_penyebut
10. test_identitas_per_jenis_utuh
11. test_jenis_tanpa_anggota_dilaporkan
12. test_hidup_luar_penyebut_menyebut_nama
13. test_contoh_hidup_luar_penyebut_dibatasi
14. test_kendali_positif_sah_saat_btcusdt_hidup
15. test_kendali_gugur_saat_kendali_tak_ada
16. test_definisi_dapat_dibedakan_terlaporkan
17. test_medan_hipotesis_ada_walau_penyebut_nol
18. test_semua_jenis_kanonik_hadir_sebagai_kunci
"""

import hashlib
from pathlib import Path

from lux_ai.semesta import taksonomi
from lux_ai.semesta import terhenti as H
from lux_ai.serapan import survei


def _isi(bulan_terakhir, bulan_pertama="2020-01", cacah=10):
    return {
        "bulan_pertama": bulan_pertama,
        "bulan_terakhir": bulan_terakhir,
        "cacah_bulan": cacah,
    }


def _rentang_contoh():
    """Tujuh nama yang sengaja menjangkau enam kelas kanonik.

    `SXPUSDT` meniru selisih nyata: terhenti menurut taksonomi (2026-05 <
    2026-06) tetapi TIDAK menurut survei (jeda 1 < 2).
    """
    return {
        "BTCUSDT": _isi("2026-06"),
        "SXPUSDT": _isi("2026-05"),
        "ADABUSD": _isi("2023-12"),
        "AAVEUSDC": _isi("2026-06"),
        "ICPUSDT_SETTLED": _isi("2023-01"),
        "BTCUSDT_261225": _isi("2026-06"),
        "DEFIUSDT": _isi("2026-06"),
    }


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
        "HIDUP": _isi("2026-06", cacah=78),
        "BATAS": _isi("2026-05", cacah=77),
        "MATI": _isi("2024-05", cacah=53),
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


def test_versi_dua():
    assert H.VERSI == 2
    assert H.bandingkan(_rentang_contoh())["versi_terhenti"] == 2
    assert H.bandingkan({})["versi_terhenti"] == 2


def test_sidik_kode_mencakup_taksonomi():
    """Pelajaran KC-29: berkas yang menentukan isi laporan wajib ikut dicap."""
    dasar = Path(H.__file__).parent
    harap = hashlib.sha256()
    for nama in sorted(H.BERKAS_DICAP):
        harap.update((dasar / nama).read_bytes())
    assert H.sidik_kode() == harap.hexdigest()
    # Sidik berkas sendiri saja TIDAK boleh cukup.
    sendiri = hashlib.sha256(Path(H.__file__).read_bytes()).hexdigest()
    assert H.sidik_kode() != sendiri


def test_berkas_dicap_terurut_dan_memuat_dua_berkas():
    assert sorted(H.BERKAS_DICAP) == ["taksonomi.py", "terhenti.py"]
    for nama in H.BERKAS_DICAP:
        assert (Path(H.__file__).parent / nama).exists()


def test_terhenti_per_jenis_menjumlah_penyebut():
    laporan = H.bandingkan(_rentang_contoh())
    assert laporan["penyebut"]["cacah_simbol"] == 7
    assert sum(laporan["cacah_per_jenis"].values()) == 7
    assert sum(laporan["terhenti_per_jenis"].values()) == laporan["cacah_terhenti_taksonomi"]
    assert sum(laporan["hidup_per_jenis"].values()) == laporan["cacah_hidup"]
    assert laporan["cacah_terhenti_taksonomi"] + laporan["cacah_hidup"] == 7


def test_identitas_per_jenis_utuh():
    laporan = H.bandingkan(_rentang_contoh())
    assert laporan["identitas_per_jenis_utuh"] is True
    for jenis, cacah in laporan["cacah_per_jenis"].items():
        assert cacah == laporan["terhenti_per_jenis"][jenis] + laporan["hidup_per_jenis"][jenis]
    # ADABUSD dan ICPUSDT_SETTLED terhenti; SXPUSDT terhenti menurut taksonomi.
    assert laporan["terhenti_per_jenis"]["perpetual_busd"] == 1
    assert laporan["terhenti_per_jenis"]["sisa_settled"] == 1
    assert laporan["terhenti_per_jenis"]["perpetual_usdt"] == 1
    assert laporan["hidup_per_jenis"]["perpetual_usdt"] == 1


def test_jenis_tanpa_anggota_dilaporkan():
    laporan = H.bandingkan(_rentang_contoh())
    assert laporan["jenis_tanpa_anggota"] == ["basis_non_fiat", "perpetual_usd1", "tak_tergolong"]
    assert H.bandingkan({})["jenis_tanpa_anggota"] == sorted(taksonomi.JENIS)


def test_hidup_luar_penyebut_menyebut_nama():
    """Aturan 67: masih terbit tidak berarti ikut dihitung."""
    laporan = H.bandingkan(_rentang_contoh())
    assert laporan["cacah_hidup_luar_penyebut"] == 3
    assert laporan["contoh_hidup_luar_penyebut"] == [
        "AAVEUSDC",
        "BTCUSDT_261225",
        "DEFIUSDT",
    ]


def test_contoh_hidup_luar_penyebut_dibatasi():
    rentang = {f"NAMA{i:03d}USDC": _isi("2026-06") for i in range(H.BATAS_CONTOH + 5)}
    laporan = H.bandingkan(rentang)
    assert laporan["cacah_hidup_luar_penyebut"] == H.BATAS_CONTOH + 5
    assert len(laporan["contoh_hidup_luar_penyebut"]) == H.BATAS_CONTOH


def test_kendali_positif_sah_saat_btcusdt_hidup():
    laporan = H.bandingkan(_rentang_contoh())
    assert laporan["kendali"]["ada"] is True
    assert laporan["kendali"]["hidup"] is True
    assert laporan["kendali"]["jenis"] == "perpetual_usdt"
    assert laporan["kendali_sah"] is True


def test_kendali_gugur_saat_kendali_tak_ada():
    rentang = _rentang_contoh()
    del rentang["BTCUSDT"]
    laporan = H.bandingkan(rentang)
    assert laporan["kendali"]["ada"] is False
    assert laporan["kendali_sah"] is False
    assert H.bandingkan({})["kendali_sah"] is False


def test_definisi_dapat_dibedakan_terlaporkan():
    """Aturan 46: laporan harus mengatakan apakah kedua definisi terpisahkan."""
    laporan = H.bandingkan(_rentang_contoh())
    assert laporan["definisi_dapat_dibedakan"] is True
    seragam = {"BTCUSDT": _isi("2026-06"), "ETHUSDT": _isi("2026-06")}
    assert H.bandingkan(seragam)["definisi_dapat_dibedakan"] is False


def test_medan_hipotesis_ada_walau_penyebut_nol():
    """Hipotesis dilaporkan, tetapi TIDAK dipakai sebagai penggugur."""
    kosong = H.bandingkan({})
    assert kosong["r_272_menang"] is False
    assert kosong["r_273_menang"] is False
    assert kosong["status"] == "TIDAK MENGUKUR"
    contoh = H.bandingkan(_rentang_contoh())
    # Pada contoh kecil, R-272 menang sedangkan R-273 kalah; keduanya tetap
    # dilaporkan dan laporan tetap TERUKUR.
    assert contoh["r_272_menang"] is True
    assert contoh["r_273_menang"] is False
    assert contoh["status"] == "TERUKUR"


def test_semua_jenis_kanonik_hadir_sebagai_kunci():
    laporan = H.bandingkan(_rentang_contoh())
    for medan in ("cacah_per_jenis", "terhenti_per_jenis", "hidup_per_jenis"):
        assert sorted(laporan[medan]) == sorted(taksonomi.JENIS)
        assert len(laporan[medan]) == 9
