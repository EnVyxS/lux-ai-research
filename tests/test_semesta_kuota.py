"""Uji semesta_kuota V2.

DAFTAR BERNOMOR fungsi uji (aturan 54, 57) - dasar ramalan R-264:
1 versi_dua · 2 sumber_sama_dengan_semesta_silang · 3 dua_berkas_keluaran ·
4 sidik_kode_heksadesimal · 5 pisah_settled_tanpa_garis_bawah ·
6 pisah_settled_dengan_garis_bawah · 7 pisah_settled_nama_biasa ·
8 kuota_usdt · 9 kuota_busd · 10 kuota_usdc · 11 kuota_btc ·
12 kuota_tak_dikenal · 13 kuota_usdt_menang_atas_usd ·
14 kuota_nama_settled_tetap_usdt · 15 akhiran_usdt_false_pada_settled ·
16 klasifikasi_mempertahankan_cacah · 17 klasifikasi_mempertahankan_bulan ·
18 klasifikasi_terurut · 19 ringkas_kuota_menjumlah · 20 ringkas_kuota_settled ·
21 jumlah_bulan_usdt_bukan_settled · 22 jumlah_bulan_seluruhnya ·
23 cacah_nama_saringan · 24 nama_bukan_akhiran_usdt · 25 pemegang_tunggal ·
26 pemegang_seri · 27 pemegang_tanpa_kandidat · 28 kendali_sah ·
29 kendali_kurang · 30 kendali_hilang · 31 kode_keluar_bersih ·
32 kode_keluar_penggugur.

Tambahan V2, bernomor 33..46 (14 fungsi baru, dasar 584 + 14 = 598):
33 berkas_dicap_memuat_sumber_penyebut · 34 total_pecahan_dari_semesta_silang ·
35 cacah_lolos_per_simbol · 36 himpunan_hanya_arsip ·
37 himpunan_hanya_arsip_kosong · 38 per_kuota_himpunan_menyaring ·
39 per_kuota_himpunan_kosong · 40 urai_selisih_identitas ·
41 urai_selisih_nama_hanya_arsip · 42 urai_selisih_abai_settled ·
43 nama_berkuota · 44 kode_keluar_penggugur_penyebut ·
45 kode_keluar_penggugur_lolos · 46 ringkas_memuat_daftar_baru.

Cacah: 46 fungsi, tanpa parametrize.
"""

from __future__ import annotations

from lux_ai.serapan import semesta_kuota as sk
from lux_ai.serapan import semesta_silang


def peta_contoh():
    """Peta sintetis; angkanya dipilih agar tiap jumlah dapat dihitung tangan."""
    return {
        "BTCUSDT": 78,
        "ETHUSDT": 70,
        "BTCDOMUSDT": 30,
        "ADABUSD": 20,
        "1000SHIBBUSD": 5,
        "ADAUSDC": 10,
        "CTKUSDTSETTLED": 1,
        "ICPUSDT_SETTLED": 9,
        "ETHBTC": 4,
    }


def ringkasan_bersih():
    return {
        "kendali_sah": True,
        "cacah_nama_arsip": sk.CACAH_NAMA_TERCATAT,
        "jumlah_bulan_arsip": sk.JUMLAH_BULAN_TERCATAT,
        "cacah_nama_settled": sk.CACAH_SETTLED_TERCATAT,
        "cacah_penyebut_simbol": sk.PENYEBUT_SIMBOL_TERCATAT,
        "bulan_lolos_gerbang": sk.PENYEBUT_BULAN_TERCATAT,
        "penyebut_bagian_arsip": True,
    }


def test_versi_dua():
    assert sk.VERSI == 2


def test_sumber_sama_dengan_semesta_silang():
    assert sk.SUMBER == semesta_silang.SUMBER_ARSIP


def test_dua_berkas_keluaran():
    assert sk.nama_keluaran() == "reports/semesta_kuota.json"
    assert sk.nama_ringkas() == "reports/semesta_kuota_ringkas.json"


def test_sidik_kode_heksadesimal():
    sidik = sk.sidik_kode()
    assert len(sidik) == 64
    assert set(sidik) <= set("0123456789abcdef")


def test_pisah_settled_tanpa_garis_bawah():
    assert sk.pisah_settled("CTKUSDTSETTLED") == ("CTKUSDT", True)


def test_pisah_settled_dengan_garis_bawah():
    assert sk.pisah_settled("ICPUSDT_SETTLED") == ("ICPUSDT", True)


def test_pisah_settled_nama_biasa():
    assert sk.pisah_settled("BTCUSDT") == ("BTCUSDT", False)


def test_kuota_usdt():
    assert sk.kuota_dasar("BTCUSDT") == "USDT"


def test_kuota_busd():
    assert sk.kuota_dasar("ADABUSD") == "BUSD"


def test_kuota_usdc():
    assert sk.kuota_dasar("ADAUSDC") == "USDC"


def test_kuota_btc():
    assert sk.kuota_dasar("ETHBTC") == "BTC"


def test_kuota_tak_dikenal():
    assert sk.kuota_dasar("USDT") == sk.KUOTA_TAK_DIKENAL
    assert sk.kuota_dasar("ABCXYZ") == sk.KUOTA_TAK_DIKENAL


def test_kuota_usdt_menang_atas_usd():
    """Urutan KUOTA_URUT wajib menahan USDT agar tidak terbaca sebagai USD."""
    assert sk.KUOTA_URUT.index("USDT") < sk.KUOTA_URUT.index("USD")
    assert sk.KUOTA_URUT.index("BUSD") < sk.KUOTA_URUT.index("USD")


def test_kuota_nama_settled_tetap_usdt():
    info = sk.kuota_nama("CTKUSDTSETTLED")
    assert info["kuota"] == "USDT"
    assert info["settled"] is True
    assert info["dasar"] == "CTKUSDT"


def test_akhiran_usdt_false_pada_settled():
    assert sk.kuota_nama("CTKUSDTSETTLED")["akhiran_usdt"] is False
    assert sk.kuota_nama("BTCUSDT")["akhiran_usdt"] is True


def test_klasifikasi_mempertahankan_cacah():
    baris = sk.klasifikasi(peta_contoh())
    assert len(baris) == 9


def test_klasifikasi_mempertahankan_bulan():
    baris = sk.klasifikasi(peta_contoh())
    assert sk.jumlah_bulan(baris) == 227


def test_klasifikasi_terurut():
    baris = sk.klasifikasi(peta_contoh())
    nama = [b["nama"] for b in baris]
    assert nama == sorted(nama)


def test_ringkas_kuota_menjumlah():
    per = sk.ringkas_kuota(sk.klasifikasi(peta_contoh()))
    assert per["USDT"]["cacah_nama"] == 5
    assert per["USDT"]["jumlah_bulan"] == 188
    assert per["BUSD"]["cacah_nama"] == 2
    assert per["BUSD"]["jumlah_bulan"] == 25
    assert per["USDC"]["cacah_nama"] == 1
    assert per["BTC"]["cacah_nama"] == 1


def test_ringkas_kuota_settled():
    per = sk.ringkas_kuota(sk.klasifikasi(peta_contoh()))
    assert per["USDT"]["cacah_settled"] == 2
    assert per["BUSD"]["cacah_settled"] == 0


def test_jumlah_bulan_usdt_bukan_settled():
    baris = sk.klasifikasi(peta_contoh())
    assert sk.jumlah_bulan(baris, kuota="USDT", settled=False) == 178
    assert sk.jumlah_bulan(baris, kuota="USDT", settled=True) == 10


def test_jumlah_bulan_seluruhnya():
    baris = sk.klasifikasi(peta_contoh())
    assert sk.jumlah_bulan(baris, settled=True) == 10
    assert sk.jumlah_bulan(baris, settled=False) == 217


def test_cacah_nama_saringan():
    baris = sk.klasifikasi(peta_contoh())
    assert sk.cacah_nama(baris) == 9
    assert sk.cacah_nama(baris, kuota="USDT") == 5
    assert sk.cacah_nama(baris, kuota="USDT", settled=False) == 3
    assert sk.cacah_nama(baris, settled=True) == 2


def test_nama_bukan_akhiran_usdt():
    baris = sk.klasifikasi(peta_contoh())
    bukan = sk.nama_bukan_akhiran_usdt(baris)
    assert bukan == [
        "1000SHIBBUSD",
        "ADABUSD",
        "ADAUSDC",
        "CTKUSDTSETTLED",
        "ETHBTC",
        "ICPUSDT_SETTLED",
    ]


def test_pemegang_tunggal():
    per = sk.ringkas_kuota(sk.klasifikasi(peta_contoh()))
    hasil = sk.pemegang_terbanyak(per)
    assert hasil["pemegang"] == ["BUSD"]
    assert hasil["nilai"] == 2
    assert hasil["seri"] is False
    assert hasil["terukur"] is True


def test_pemegang_seri():
    """KC-26: seri WAJIB melaporkan seluruh pemegang, bukan yang pertama."""
    per = {
        "USDT": {"cacah_nama": 99, "jumlah_bulan": 1, "cacah_settled": 0},
        "BUSD": {"cacah_nama": 7, "jumlah_bulan": 1, "cacah_settled": 0},
        "USDC": {"cacah_nama": 7, "jumlah_bulan": 1, "cacah_settled": 0},
        "BTC": {"cacah_nama": 2, "jumlah_bulan": 1, "cacah_settled": 0},
    }
    hasil = sk.pemegang_terbanyak(per)
    assert hasil["pemegang"] == ["BUSD", "USDC"]
    assert hasil["cacah_pemegang"] == 2
    assert hasil["seri"] is True


def test_pemegang_tanpa_kandidat():
    hasil = sk.pemegang_terbanyak({"USDT": {"cacah_nama": 5}})
    assert hasil["terukur"] is False
    assert hasil["pemegang"] == []
    assert hasil["nilai"] is None


def test_kendali_sah():
    kend = sk.kendali(peta_contoh())
    assert kend["simbol"] == "BTCUSDT"
    assert kend["cacah_bulan"] == 78
    assert kend["ada"] is True
    assert kend["sah"] is True


def test_kendali_kurang():
    kend = sk.kendali({"BTCUSDT": 12})
    assert kend["ada"] is True
    assert kend["sah"] is False


def test_kendali_hilang():
    kend = sk.kendali({"ETHUSDT": 70})
    assert kend["ada"] is False
    assert kend["cacah_bulan"] == 0
    assert kend["sah"] is False


def test_kode_keluar_bersih():
    assert sk.kode_keluar(ringkasan_bersih()) == 0


def test_kode_keluar_penggugur():
    r = ringkasan_bersih()
    r["kendali_sah"] = False
    assert sk.kode_keluar(r) == 2
    r = ringkasan_bersih()
    r["cacah_nama_arsip"] = 936
    assert sk.kode_keluar(r) == 2
    r = ringkasan_bersih()
    r["jumlah_bulan_arsip"] = 21788
    assert sk.kode_keluar(r) == 2
    r = ringkasan_bersih()
    r["cacah_nama_settled"] = 14
    assert sk.kode_keluar(r) == 2


# --- V2, fungsi 33..46 ----------------------------------------------------


def test_berkas_dicap_memuat_sumber_penyebut():
    """Aturan 22: berkas yang menentukan penyebut WAJIB ikut dicap."""
    assert "silang_funding.py" in sk.BERKAS_DICAP
    assert "kehidupan_arsip.py" in sk.BERKAS_DICAP
    assert "semesta_silang.py" in sk.BERKAS_DICAP
    assert "semesta_kuota.py" in sk.BERKAS_DICAP


def test_total_pecahan_dari_semesta_silang():
    assert sk.TOTAL_PECAHAN == semesta_silang.TOTAL_PECAHAN


def test_cacah_lolos_per_simbol():
    status = {
        ("BTCUSDT", "2020-01"): "HIDUP",
        ("BTCUSDT", "2020-02"): "HIDUP",
        ("ETHUSDT", "2020-01"): "MATI",
    }
    hasil = sk.cacah_lolos_per_simbol(status)
    assert hasil == {"BTCUSDT": 2, "ETHUSDT": 1}


def test_himpunan_hanya_arsip():
    baris = sk.klasifikasi(peta_contoh())
    hanya = sk.himpunan_hanya_arsip(baris, ["BTCUSDT", "ETHUSDT", "BTCDOMUSDT"])
    assert hanya == [
        "1000SHIBBUSD",
        "ADABUSD",
        "ADAUSDC",
        "CTKUSDTSETTLED",
        "ETHBTC",
        "ICPUSDT_SETTLED",
    ]


def test_himpunan_hanya_arsip_kosong():
    baris = sk.klasifikasi({"BTCUSDT": 78})
    assert sk.himpunan_hanya_arsip(baris, ["BTCUSDT"]) == []


def test_per_kuota_himpunan_menyaring():
    baris = sk.klasifikasi(peta_contoh())
    per = sk.per_kuota_himpunan(baris, ["ADABUSD", "ADAUSDC", "ETHBTC"])
    assert per["BUSD"]["cacah_nama"] == 1
    assert per["USDC"]["cacah_nama"] == 1
    assert per["BTC"]["cacah_nama"] == 1
    assert "USDT" not in per


def test_per_kuota_himpunan_kosong():
    baris = sk.klasifikasi(peta_contoh())
    assert sk.per_kuota_himpunan(baris, []) == {}


def test_urai_selisih_identitas():
    baris = sk.klasifikasi(peta_contoh())
    urai = sk.urai_selisih(
        baris,
        ["BTCUSDT", "ETHUSDT"],
        {"BTCUSDT": 70, "ETHUSDT": 60},
    )
    assert urai["bulan_usdt_bukan_settled"] == 178
    assert urai["bulan_arsip_milik_penyebut"] == 148
    assert urai["bulan_arsip_milik_hanya_arsip"] == 30
    assert urai["bulan_lolos_gerbang"] == 130
    assert urai["selisih_total"] == 48
    assert urai["selisih_dalam_penyebut"] == 18
    assert urai["selisih_dari_hanya_arsip"] == 30
    assert urai["identitas_utuh"] is True


def test_urai_selisih_nama_hanya_arsip():
    baris = sk.klasifikasi(peta_contoh())
    urai = sk.urai_selisih(baris, ["BTCUSDT", "ETHUSDT"], {"BTCUSDT": 78})
    assert urai["nama_usdt_hanya_arsip"] == ["BTCDOMUSDT"]
    assert urai["cacah_nama_usdt_hanya_arsip"] == 1


def test_urai_selisih_abai_settled():
    """Nama SETTLED tidak boleh masuk penguraian penyebut USDT."""
    baris = sk.klasifikasi(peta_contoh())
    urai = sk.urai_selisih(baris, [], {})
    assert urai["bulan_usdt_bukan_settled"] == 178
    assert "CTKUSDTSETTLED" not in urai["nama_usdt_hanya_arsip"]
    assert "ICPUSDT_SETTLED" not in urai["nama_usdt_hanya_arsip"]


def test_nama_berkuota():
    baris = sk.klasifikasi(peta_contoh())
    assert sk.nama_berkuota(baris, "BTC") == ["ETHBTC"]
    assert sk.nama_berkuota(baris, sk.KUOTA_TAK_DIKENAL) == []


def test_kode_keluar_penggugur_penyebut():
    r = ringkasan_bersih()
    r["cacah_penyebut_simbol"] = 786
    assert sk.kode_keluar(r) == 2
    r = ringkasan_bersih()
    r["penyebut_bagian_arsip"] = False
    assert sk.kode_keluar(r) == 2


def test_kode_keluar_penggugur_lolos():
    r = ringkasan_bersih()
    r["bulan_lolos_gerbang"] = 19585
    assert sk.kode_keluar(r) == 2


def test_ringkas_memuat_daftar_baru():
    """Aturan 52: daftar yang wajib dibaca utuh harus ada di berkas ringkas."""
    laporan = {
        "versi_semesta_kuota": 2,
        "sidik_kode": "a" * 64,
        "sidik_data": "b" * 64,
        "per_kuota": {"USDT": {"cacah_nama": 1}},
        "per_kuota_hanya_arsip": {"BUSD": {"cacah_nama": 1}},
        "terbanyak_bukan_usdt": {"pemegang": ["BUSD"]},
        "urai_selisih": {"selisih_total": 163},
        "nama_tak_dikenal": ["ABCXYZ"],
        "nama_hanya_arsip": ["ABCXYZ"],
        "baris": [{"nama": "ABCXYZ"}],
        "ringkasan": {"cacah_nama_arsip": 937},
        "waktu_utc": "2026-07-29T00:00:00Z",
    }
    kecil = sk.ringkas(laporan)
    assert kecil["nama_tak_dikenal"] == ["ABCXYZ"]
    assert kecil["per_kuota_hanya_arsip"] == {"BUSD": {"cacah_nama": 1}}
    assert kecil["urai_selisih"] == {"selisih_total": 163}
    assert "baris" not in kecil
    assert "nama_hanya_arsip" not in kecil
