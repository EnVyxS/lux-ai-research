"""Uji selisih definisi terhenti (utang 28), penguraian per jenis (V2),
penyebutan nama (V3), dan pemasangan SETTLED dengan nama dasarnya (V4).

Daftar bernomor agar cacah butirnya dapat diramalkan, bukan ditaksir
(aturan 54, 56, 57). Tiga puluh tiga butir — delapan terakhir baru di V4:

1. test_salinan_selisih_bulan_sepakat_dengan_survei
2. test_definisi_survei_sama_dengan_fungsi_asli
3. test_mundur_bulan_melewati_pergantian_tahun
4. test_selisih_himpunan_menyebut_nama_dan_arah
5. test_penyebut_nol_berstatus_tidak_mengukur
6. test_versi_empat
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
19. test_nama_terhenti_per_jenis_menyebut_nama
20. test_nama_terhenti_per_jenis_konsisten_dengan_cacahnya
21. test_nama_hidup_luar_penyebut_lengkap_dan_terurut
22. test_settled_hidup_menyebut_cacah_bulan
23. test_peralihan_h_a013_dilaporkan_walau_tak_hadir
24. test_peralihan_h_a013_menang_hanya_bila_keenam_terhenti
25. test_daftar_nama_terpotong_menyala_dan_cacah_tetap_penuh
26. test_nama_dasar_membuang_kedua_konvensi
27. test_nama_dasar_menolak_nama_bukan_settled
28. test_pasangan_settled_memuat_bulan_kedua_nama
29. test_pasangan_settled_menandai_dasar_terhenti
30. test_pasangan_tanpa_nama_dasar_dilaporkan
31. test_identitas_pasangan_utuh
32. test_kendali_pasangan_sah_bahkan_tanpa_data
33. test_r_278_menang_hanya_pada_pola_yang_diramalkan
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


def test_versi_empat():
    assert H.VERSI == 4
    assert H.bandingkan(_rentang_contoh())["versi_terhenti"] == 4
    assert H.bandingkan({})["versi_terhenti"] == 4


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
    for medan in ("r_272_menang", "r_273_menang", "r_275_menang", "r_276_menang", "r_278_menang"):
        assert kosong[medan] is False
    assert kosong["status"] == "TIDAK MENGUKUR"
    contoh = H.bandingkan(_rentang_contoh())
    assert contoh["r_272_menang"] is True
    assert contoh["r_273_menang"] is False
    assert contoh["status"] == "TERUKUR"


def test_semua_jenis_kanonik_hadir_sebagai_kunci():
    laporan = H.bandingkan(_rentang_contoh())
    for medan in ("cacah_per_jenis", "terhenti_per_jenis", "hidup_per_jenis"):
        assert sorted(laporan[medan]) == sorted(taksonomi.JENIS)
        assert len(laporan[medan]) == 9
    assert sorted(laporan["nama_terhenti_per_jenis"]) == sorted(taksonomi.JENIS)


def test_nama_terhenti_per_jenis_menyebut_nama():
    laporan = H.bandingkan(_rentang_contoh())
    nama = laporan["nama_terhenti_per_jenis"]
    assert nama["perpetual_busd"] == ["ADABUSD"]
    assert nama["sisa_settled"] == ["ICPUSDT_SETTLED"]
    assert nama["perpetual_usdt"] == ["SXPUSDT"]
    assert nama["perpetual_usdc"] == []
    assert nama["futures_kedaluwarsa"] == []


def test_nama_terhenti_per_jenis_konsisten_dengan_cacahnya():
    laporan = H.bandingkan(_rentang_contoh())
    for jenis, daftar in laporan["nama_terhenti_per_jenis"].items():
        assert len(daftar) == laporan["terhenti_per_jenis"][jenis]
        assert daftar == sorted(daftar)
    assert laporan["daftar_nama_terpotong"] is False


def test_nama_hidup_luar_penyebut_lengkap_dan_terurut():
    laporan = H.bandingkan(_rentang_contoh())
    daftar = laporan["nama_hidup_luar_penyebut"]
    assert daftar == ["AAVEUSDC", "BTCUSDT_261225", "DEFIUSDT"]
    assert daftar == sorted(daftar)
    assert len(daftar) == laporan["cacah_hidup_luar_penyebut"]


def test_settled_hidup_menyebut_cacah_bulan():
    """R-275 hanya bisa diadjudikasi bila cacah_bulan-nya ikut disebut."""
    rentang = _rentang_contoh()
    assert H.bandingkan(rentang)["settled_hidup"] == []
    rentang["PUMPUSDTSETTLED"] = _isi("2026-06", bulan_pertama="2026-05", cacah=2)
    laporan = H.bandingkan(rentang)
    assert laporan["settled_hidup"] == [
        {"simbol": "PUMPUSDTSETTLED", "bulan_terakhir": "2026-06", "cacah_bulan": 2}
    ]
    assert laporan["hidup_per_jenis"]["sisa_settled"] == 1
    assert laporan["r_275_menang"] is True
    # Kontrak SETTLED berumur panjang yang masih terbit menggugurkan R-275.
    rentang["PUMPUSDTSETTLED"] = _isi("2026-06", cacah=12)
    assert H.bandingkan(rentang)["r_275_menang"] is False


def test_peralihan_h_a013_dilaporkan_walau_tak_hadir():
    """Aturan 59: nama yang hilang bukan nama yang terhenti."""
    laporan = H.bandingkan(_rentang_contoh())
    peralihan = laporan["peralihan_h_a013"]
    assert sorted(peralihan) == sorted(H.PERALIHAN_H_A013)
    for simbol, isi in peralihan.items():
        assert isi["ada"] is False
        assert isi["terhenti"] is False
        assert isi["bulan_terakhir"] is None
    assert laporan["cacah_peralihan_terhenti"] == 0
    assert laporan["r_276_menang"] is False


def test_peralihan_h_a013_menang_hanya_bila_keenam_terhenti():
    rentang = {"BTCUSDT": _isi("2026-06")}
    for simbol in H.PERALIHAN_H_A013:
        rentang[simbol] = _isi("2025-06")
    laporan = H.bandingkan(rentang)
    assert laporan["cacah_peralihan_terhenti"] == 6
    assert laporan["r_276_menang"] is True
    # Satu nama masih terbit sudah cukup menggugurkan.
    rentang["LITUSDT"] = _isi("2026-06")
    gugur = H.bandingkan(rentang)
    assert gugur["cacah_peralihan_terhenti"] == 5
    assert gugur["peralihan_h_a013"]["LITUSDT"]["terhenti"] is False
    assert gugur["r_276_menang"] is False


def test_daftar_nama_terpotong_menyala_dan_cacah_tetap_penuh():
    """KC-13: daftar terpotong wajib mengaku, dan cacah penuh tetap terbaca."""
    besar = H.BATAS_NAMA + 7
    rentang = {f"N{i:03d}USDC": _isi("2026-06") for i in range(besar)}
    rentang["BTCUSDT"] = _isi("2026-06")
    laporan = H.bandingkan(rentang)
    assert laporan["cacah_hidup_luar_penyebut"] == besar
    assert len(laporan["nama_hidup_luar_penyebut"]) == H.BATAS_NAMA
    assert laporan["daftar_nama_terpotong"] is True


def test_nama_dasar_membuang_kedua_konvensi():
    """Dua konvensi hidup berdampingan; yang bergaris bawah wajib menang dulu."""
    assert H.nama_dasar("ICPUSDT_SETTLED") == "ICPUSDT"
    assert H.nama_dasar("TLMUSDTSETTLED") == "TLMUSDT"
    assert H.nama_dasar("SXPUSDTSETTLED") == "SXPUSDT"
    assert H.AKHIRAN_SETTLED[0] == "_SETTLED"


def test_nama_dasar_menolak_nama_bukan_settled():
    """Nama biasa TIDAK boleh terpasang, dan sisa kosong bukan nama dasar."""
    assert H.nama_dasar("BTCUSDT") is None
    assert H.nama_dasar("SETTLEDUSDT") is None
    assert H.nama_dasar("SETTLED") is None
    assert H.nama_dasar("_SETTLED") is None


def test_pasangan_settled_memuat_bulan_kedua_nama():
    """Aturan 68: bulan terakhir nama turunan dan nama asal wajib berpasangan."""
    rentang = _rentang_contoh()
    rentang["ICPUSDT"] = _isi("2026-06")
    laporan = H.bandingkan(rentang)
    assert laporan["cacah_settled"] == 1
    pasangan = laporan["pasangan_settled"][0]
    assert pasangan["settled"] == "ICPUSDT_SETTLED"
    assert pasangan["dasar"] == "ICPUSDT"
    assert pasangan["dasar_ada"] is True
    assert pasangan["dasar_hidup"] is True
    assert pasangan["bulan_terakhir_settled"] == "2023-01"
    assert pasangan["bulan_terakhir_dasar"] == "2026-06"
    assert pasangan["settled_mendahului_tutup"] is True
    assert laporan["cacah_dasar_hidup"] == 1
    assert laporan["cacah_settled_mendahului"] == 1


def test_pasangan_settled_menandai_dasar_terhenti():
    """Pola SXPUSDT: nama dasar berhenti, nama SETTLED meneruskan."""
    rentang = {
        "BTCUSDT": _isi("2026-06"),
        "SXPUSDT": _isi("2026-05"),
        "SXPUSDTSETTLED": _isi("2026-06", bulan_pertama="2026-06", cacah=1),
    }
    laporan = H.bandingkan(rentang)
    pasangan = laporan["pasangan_settled"][0]
    assert pasangan["settled"] == "SXPUSDTSETTLED"
    assert pasangan["dasar"] == "SXPUSDT"
    assert pasangan["dasar_ada"] is True
    assert pasangan["dasar_hidup"] is False
    assert pasangan["bulan_terakhir_dasar"] == "2026-05"
    assert pasangan["settled_mendahului_tutup"] is False
    assert laporan["cacah_dasar_terhenti"] == 1
    assert laporan["cacah_dasar_hidup"] == 0


def test_pasangan_tanpa_nama_dasar_dilaporkan():
    """KC-13 dan aturan 59: pemasangan yang gagal dicacah, bukan dibuang."""
    laporan = H.bandingkan(_rentang_contoh())
    assert laporan["cacah_settled"] == 1
    assert laporan["cacah_dasar_tak_ada"] == 1
    pasangan = laporan["pasangan_settled"][0]
    assert pasangan["dasar"] == "ICPUSDT"
    assert pasangan["dasar_ada"] is False
    assert pasangan["dasar_hidup"] is False
    assert pasangan["bulan_terakhir_dasar"] is None
    assert laporan["r_278_menang"] is False


def test_identitas_pasangan_utuh():
    rentang = _rentang_contoh()
    rentang["TLMUSDTSETTLED"] = _isi("2023-03")
    rentang["TLMUSDT"] = _isi("2026-06")
    laporan = H.bandingkan(rentang)
    assert laporan["cacah_settled"] == 2
    jumlah = (
        laporan["cacah_dasar_hidup"]
        + laporan["cacah_dasar_terhenti"]
        + laporan["cacah_dasar_tak_ada"]
    )
    assert jumlah == laporan["cacah_settled"]
    assert laporan["identitas_pasangan_utuh"] is True
    assert H.bandingkan({})["identitas_pasangan_utuh"] is True


def test_kendali_pasangan_sah_bahkan_tanpa_data():
    """Kendali positif atas KODE pemasangan, bukan atas data (aturan 50)."""
    assert H.bandingkan(_rentang_contoh())["kendali_pasangan_sah"] is True
    assert H.bandingkan({})["kendali_pasangan_sah"] is True


def test_r_278_menang_hanya_pada_pola_yang_diramalkan():
    """13 dasar hidup, 2 dasar terhenti, >=11 SETTLED mendahului bulan tutup."""
    rentang = {"BTCUSDT": _isi("2026-06")}
    for i in range(H.R278_DASAR_HIDUP):
        rentang[f"A{i:02d}USDT"] = _isi("2026-06")
        rentang[f"A{i:02d}USDTSETTLED"] = _isi("2025-01")
    for j in range(H.R278_DASAR_TERHENTI):
        rentang[f"B{j}USDT"] = _isi("2024-01")
        rentang[f"B{j}USDTSETTLED"] = _isi("2025-06")
    laporan = H.bandingkan(rentang)
    assert laporan["cacah_settled"] == 15
    assert laporan["cacah_dasar_hidup"] == 13
    assert laporan["cacah_dasar_terhenti"] == 2
    assert laporan["cacah_dasar_tak_ada"] == 0
    assert laporan["cacah_settled_mendahului"] == 15
    assert laporan["r_278_menang"] is True
    # Satu pasangan tambahan dengan dasar hidup sudah menggugurkan pola.
    rentang["C0USDT"] = _isi("2026-06")
    rentang["C0USDTSETTLED"] = _isi("2025-02")
    gugur = H.bandingkan(rentang)
    assert gugur["cacah_dasar_hidup"] == 14
    assert gugur["r_278_menang"] is False
