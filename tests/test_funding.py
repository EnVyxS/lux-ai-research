"""Uji jalur funding tanpa jaringan sama sekali.

Delapan belas fungsi uji, TANPA `parametrize`, sehingga cacah fungsi sama dengan
cacah butir yang dikumpulkan pytest. Ini disengaja: kekeliruan R-148 lahir dari
mencacah fungsi padahal pytest mencacah butir (aturan 47).

Sejak VERSI 6 blok CDN pindah ke `funding_cdn.py` dan `funding.py` hanya
mengekspor ulang namanya. Re-export memindahkan FUNGSI, bukan MODUL: setelah
pemecahan, `funding.urllib` tidak ada lagi dan uji yang menambalnya gugur dengan
AttributeError (run 30412188737). Karena itu tambalan di bawah menunjuk
`funding_cdn.urllib.request`, yaitu modul yang benar-benar memiliki kodenya,
sementara pemanggilannya tetap lewat `funding.periksa_url`. Susunan itu disengaja:
ia sekaligus membuktikan re-export menyalurkan panggilan ke kode yang ditambal,
bukan ke salinan lain.
"""

from __future__ import annotations

import io
import urllib.error
import zipfile

from lux_ai.serapan import funding, funding_cdn


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


def test_ringkas_sampel_mempertahankan_null_berheader():
    """null dan false adalah dua keadaan berbeda (aturan 46)."""
    ringkas = funding.ringkas_sampel(
        [
            {"simbol": "AAA", "bulan": "2021-03", "berheader": None, "byte_zip": 0},
            {"simbol": "BBB", "bulan": "2025-03", "berheader": False, "byte_zip": 500},
        ]
    )
    assert ringkas[0]["berheader"] is None
    assert ringkas[1]["berheader"] is False
    assert ringkas[0]["gagal_unduh"] is None  # medan absen tetap hadir sebagai null
    assert set(ringkas[0]) == set(funding.MEDAN_SAMPEL_RINGKAS)


def test_klasifikasi_lubang_membedakan_awal_ekor_tengah():
    bulan = ["2024-01", "2024-02", "2024-03", "2024-04", "2024-05", "2024-06"]
    hasil = funding.klasifikasi_lubang(bulan, ["2024-01", "2024-03", "2024-05", "2024-06"])
    assert hasil["awal"] == 1
    assert hasil["ekor"] == 2
    assert hasil["tengah"] == 1
    assert hasil["hilang"] == 4
    assert hasil["awal"] + hasil["ekor"] + hasil["tengah"] == hasil["hilang"]


def test_klasifikasi_lubang_seluruh_bulan_hilang_tidak_dicacah_ganda():
    bulan = ["2024-01", "2024-02", "2024-03"]
    hasil = funding.klasifikasi_lubang(bulan, bulan)
    assert hasil["awal"] == 3
    assert hasil["ekor"] == 0
    assert hasil["tengah"] == 0
    assert hasil["hilang"] == 3
    # bulan di luar riwayat klines diabaikan, bukan menambah cacah
    lain = funding.klasifikasi_lubang(bulan, bulan + ["2030-01"])
    assert lain["hilang"] == 3


def test_mulai_lubang_ekor_bulan_pertama_akhiran():
    bulan = ["2025-05", "2025-06", "2025-07", "2025-08"]
    assert funding.mulai_lubang_ekor(bulan, ["2025-07", "2025-08"]) == "2025-07"
    # lubang di tengah bukan lubang ekor
    assert funding.mulai_lubang_ekor(bulan, ["2025-06"]) is None
    # tanpa lubang sama sekali
    assert funding.mulai_lubang_ekor(bulan, []) is None
    # seluruh bulan hilang dihitung sebagai awal, jadi ekornya kosong
    assert funding.mulai_lubang_ekor(bulan, bulan) is None


def test_jarak_bulan_melintasi_pergantian_tahun():
    assert funding.jarak_bulan("2025-07", "2026-06") == 11
    assert funding.jarak_bulan("2026-06", "2026-06") == 0
    assert funding.jarak_bulan("2026-06", "2025-07") == -11
    assert funding.jarak_bulan("bukan-bulan", "2026-06") is None


def test_histogram_menyaring_none_dan_melaporkan_seri():
    h = funding.histogram(["2025-07", "2025-07", "2024-01", None])
    assert h == {"2024-01": 1, "2025-07": 2}
    puncak = funding.puncak_histogram(h)
    assert puncak["kunci"] == "2025-07"
    assert puncak["cacah"] == 2
    assert puncak["seri"] is False
    # seri dimenangkan kunci terkecil, tetapi keseriannya dilaporkan
    seri = funding.puncak_histogram({"2024-01": 2, "2025-07": 2})
    assert seri["kunci"] == "2024-01"
    assert seri["seri"] is True
    assert funding.puncak_histogram({}) == {"kunci": None, "cacah": 0, "seri": False}


def test_periksa_url_membedakan_404_dari_galat_jaringan(monkeypatch):
    """Server menjawab 'tidak ada' bukan hal yang sama dengan server bisu.

    Tambalan dipasang pada `funding_cdn` (pemilik kode sejak VERSI 6) sedangkan
    panggilan dilakukan lewat `funding` (yang mengekspor ulang). Bila suatu saat
    re-export putus atau menunjuk salinan lain, tambalan tidak akan terpakai dan
    uji ini gagal, bukan lulus diam-diam.
    """

    def tolak(*_args, **_kwargs):
        raise urllib.error.HTTPError("http://x", 404, "Not Found", None, None)

    monkeypatch.setattr(funding_cdn.urllib.request, "urlopen", tolak)
    empat_nol_empat = funding.periksa_url("http://x")
    assert empat_nol_empat["kode_http"] == 404
    assert empat_nol_empat["galat"] is None

    def bisu(*_args, **_kwargs):
        raise urllib.error.URLError("nama tidak dapat diselesaikan")

    monkeypatch.setattr(funding_cdn.urllib.request, "urlopen", bisu)
    galat = funding.periksa_url("http://x")
    assert galat["kode_http"] is None
    assert galat["galat"]


def test_uji_cdn_kohort_dan_kendali_berpasangan():
    """Kendali wajib simbol yang sama pada bulan berbeda: satu variabel saja."""
    assert len(funding.UJI_KOHORT) == len(funding.UJI_KENDALI) == 3
    kohort = dict(funding.UJI_KOHORT)
    kendali = dict(funding.UJI_KENDALI)
    assert set(kohort) == set(kendali)
    for simbol in kohort:
        assert kohort[simbol] != kendali[simbol]
    # tidak ada pasangan yang sama persis di kedua daftar
    assert not set(funding.UJI_KOHORT) & set(funding.UJI_KENDALI)


def test_ringkas_uji_cdn_gugur_saat_kendali_gagal():
    kohort = [{"kode_http": 404}, {"kode_http": 404}, {"kode_http": None, "galat": "putus"}]
    kendali_baik = [{"kode_http": 200, "checksum_cocok": True}] * 2
    hasil = funding.ringkas_uji_cdn(kohort, kendali_baik)
    assert hasil["cacah_kohort_404"] == 2
    assert hasil["cacah_kohort_galat"] == 1
    assert hasil["kendali_sah"] is True

    # kendali yang terambil tetapi checksumnya tidak cocok TIDAK mensahkan
    hasil_cacat = funding.ringkas_uji_cdn(
        kohort, [{"kode_http": 200, "checksum_cocok": None}]
    )
    assert hasil_cacat["kendali_sah"] is False
    # kendali kosong juga tidak mensahkan apa pun
    assert funding.ringkas_uji_cdn(kohort, [])["kendali_sah"] is False
