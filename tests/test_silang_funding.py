"""Uji `silang_funding`: pembacaan laporan, irisan, kendali, dan kode keluar.

Seluruh uji memakai laporan tiruan di `tmp_path`; tidak ada jaringan dan tidak
ada aset rilis. Yang dijaga di sini adalah bagian yang bila salah akan membuat
laporan irisan terbaca meyakinkan namun keliru: penyebut yang bocor, laporan
pecahan yang hilang diam-diam, dan kendali yang tidak menggugurkan apa pun.

Cacah butir (aturan 54, dicacah dari berkas ini setelah selesai ditulis): 42
fungsi `def test_`, satu di antaranya `parametrize` tiga kasus, sehingga
41 + 3 = **44 butir**.

V2 menambah uji bagi definisi `bentuk_lubang_lokal`, kedua daftar bernama, dan
dua penggugur baru.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from lux_ai.serapan import kehidupan, silang_funding as sf


def _tulis_pecahan(akar: Path, indeks: int, baris, sidik: str = "sidik-a") -> None:
    tujuan = akar / "reports"
    tujuan.mkdir(parents=True, exist_ok=True)
    (tujuan / f"kehidupan_arsip_{indeks}.json").write_text(
        json.dumps({"sidik_kode": sidik, "baris": baris}, ensure_ascii=False),
        encoding="utf-8",
    )


def _baris(simbol: str, bulan: str, status: str, byte_parquet: int = 10):
    return {
        "simbol": simbol,
        "bulan": bulan,
        "status": status,
        "byte_parquet": byte_parquet,
    }


def test_status_terbaca_dari_kedua_pecahan(tmp_path):
    _tulis_pecahan(tmp_path, 0, [_baris("A", "2024-01", kehidupan.STATUS_MATI)])
    _tulis_pecahan(tmp_path, 1, [_baris("B", "2024-01", kehidupan.STATUS_HIDUP)])
    status, byte_parquet, meta = sf.baca_laporan_kehidupan(akar=str(tmp_path), total=2)
    assert status[("A", "2024-01")] == kehidupan.STATUS_MATI
    assert byte_parquet[("B", "2024-01")] == 10
    assert meta["sidik_seragam"] is True


def test_laporan_pecahan_hilang_dicatat_bukan_dianggap_kosong(tmp_path):
    _tulis_pecahan(tmp_path, 0, [_baris("A", "2024-01", kehidupan.STATUS_MATI)])
    _, _, meta = sf.baca_laporan_kehidupan(akar=str(tmp_path), total=2)
    assert meta["cacah_laporan_dibaca"] == 1
    assert meta["laporan_hilang"] == ["reports/kehidupan_arsip_1.json"]
    assert meta["sidik_seragam"] is False


def test_sidik_kode_berbeda_membatalkan_penjumlahan(tmp_path):
    _tulis_pecahan(tmp_path, 0, [_baris("A", "2024-01", kehidupan.STATUS_MATI)])
    _tulis_pecahan(
        tmp_path, 1, [_baris("B", "2024-01", kehidupan.STATUS_HIDUP)], sidik="sidik-b"
    )
    _, _, meta = sf.baca_laporan_kehidupan(akar=str(tmp_path), total=2)
    assert meta["sidik_seragam"] is False
    assert sf.kode_keluar(dict(meta, kendali_sah=True)) == 2


def test_kunci_ganda_dicacah_bukan_ditimpa(tmp_path):
    _tulis_pecahan(tmp_path, 0, [_baris("A", "2024-01", kehidupan.STATUS_MATI)])
    _tulis_pecahan(tmp_path, 1, [_baris("A", "2024-01", kehidupan.STATUS_HIDUP)])
    status, _, meta = sf.baca_laporan_kehidupan(akar=str(tmp_path), total=2)
    assert meta["cacah_kunci_ganda"] == 1
    assert status[("A", "2024-01")] == kehidupan.STATUS_MATI


def _funding(per_simbol, kohort=None):
    return {"per_simbol": per_simbol, "kohort_puncak": kohort or {}}


def test_lubang_funding_dibaca_dari_per_simbol():
    lubang, meta = sf.lubang_funding(
        _funding(
            [
                {"simbol": "A", "klines_tanpa_funding": ["2024-01", "2024-02"]},
                {"simbol": "B", "klines_tanpa_funding": []},
            ]
        )
    )
    assert lubang == {("A", "2024-01"), ("A", "2024-02")}
    assert meta["cacah_lubang_funding"] == 2
    assert meta["cacah_lubang_ganda"] == 0


def test_kohort_hanya_memuat_bulan_ekor():
    funding = _funding(
        [
            {
                "simbol": "A",
                "klines_tanpa_funding": ["2021-01", "2025-07", "2025-08"],
                "mulai_lubang_ekor": "2025-07",
            }
        ],
        kohort={"simbol": ["A"], "bulan_mulai": "2025-07"},
    )
    assert sf.kohort_simbol_bulan(funding) == {("A", "2025-07"), ("A", "2025-08")}


def test_kohort_melewati_anggota_tanpa_bulan_mulai():
    funding = _funding(
        [{"simbol": "A", "klines_tanpa_funding": ["2025-07"], "mulai_lubang_ekor": None}],
        kohort={"simbol": ["A"]},
    )
    assert sf.kohort_simbol_bulan(funding) == set()


def test_kohort_melewati_simbol_bukan_anggota():
    funding = _funding(
        [
            {
                "simbol": "Z",
                "klines_tanpa_funding": ["2025-07"],
                "mulai_lubang_ekor": "2025-07",
            }
        ],
        kohort={"simbol": ["A"]},
    )
    assert sf.kohort_simbol_bulan(funding) == set()


def test_silang_melaporkan_keempat_status_walau_nol():
    tabel = sf.silang({}, set())
    assert set(tabel) == {
        kehidupan.STATUS_MATI,
        kehidupan.STATUS_SEPI,
        kehidupan.STATUS_HIDUP,
        kehidupan.STATUS_TAK_TERUKUR,
    }
    assert tabel[kehidupan.STATUS_MATI] == {"funding_hilang": 0, "funding_ada": 0}


def test_silang_menempatkan_lubang_pada_kolom_benar():
    status = {
        ("A", "2024-01"): kehidupan.STATUS_MATI,
        ("B", "2024-01"): kehidupan.STATUS_MATI,
        ("C", "2024-01"): kehidupan.STATUS_HIDUP,
    }
    tabel = sf.silang(status, {("A", "2024-01")})
    assert tabel[kehidupan.STATUS_MATI] == {"funding_hilang": 1, "funding_ada": 1}
    assert tabel[kehidupan.STATUS_HIDUP] == {"funding_hilang": 0, "funding_ada": 1}


@pytest.mark.parametrize(
    "status_baris,kolom",
    [
        (kehidupan.STATUS_MATI, "funding_hilang"),
        (kehidupan.STATUS_SEPI, "funding_hilang"),
        (kehidupan.STATUS_HIDUP, "funding_hilang"),
    ],
)
def test_silang_setiap_status_dapat_berlubang(status_baris, kolom):
    tabel = sf.silang({("A", "2024-01"): status_baris}, {("A", "2024-01")})
    assert tabel[status_baris][kolom] == 1


def test_rincian_mati_memisahkan_dalam_dan_luar_kohort():
    status = {
        ("A", "2025-07"): kehidupan.STATUS_MATI,
        ("B", "2024-01"): kehidupan.STATUS_MATI,
        ("C", "2024-01"): kehidupan.STATUS_MATI,
        ("D", "2024-01"): kehidupan.STATUS_HIDUP,
    }
    hasil = sf.rincian_mati(
        status, {("A", "2025-07"), ("B", "2024-01")}, {("A", "2025-07")}
    )
    assert hasil["cacah_mati"] == 3
    assert hasil["cacah_mati_di_kohort"] == 1
    assert hasil["cacah_mati_luar_kohort"] == 2
    assert hasil["cacah_mati_luar_kohort_dengan_lubang_funding"] == 1
    assert hasil["cacah_mati_luar_kohort_funding_ada"] == 1


def test_rincian_mati_bagian_membulat_empat_desimal():
    status = {
        ("A", "2024-01"): kehidupan.STATUS_MATI,
        ("B", "2024-01"): kehidupan.STATUS_MATI,
        ("C", "2024-01"): kehidupan.STATUS_MATI,
    }
    hasil = sf.rincian_mati(status, {("A", "2024-01"), ("B", "2024-01")}, set())
    # kohort_ekor.bagian MEMBULATKAN ke empat desimal (aturan 53).
    assert hasil["bagian_mati_luar_kohort_dengan_lubang_funding"] == 0.6667


def test_rincian_mati_penyebut_nol_menghasilkan_null():
    hasil = sf.rincian_mati({("A", "2024-01"): kehidupan.STATUS_HIDUP}, set(), set())
    assert hasil["cacah_mati"] == 0
    assert hasil["bagian_mati_luar_kohort_dengan_lubang_funding"] is None


def test_kendali_dipilih_dari_parquet_terbesar():
    byte_parquet = {("A", "2024-01"): 5, ("B", "2024-01"): 900, ("C", "2024-01"): 40}
    status = {k: kehidupan.STATUS_HIDUP for k in byte_parquet}
    kendali = sf.kendali_silang(byte_parquet, status, set(), cacah=2)
    assert [k["simbol"] for k in kendali] == ["B", "C"]
    assert sf.kendali_sah(kendali) is True


def test_kendali_gagal_bila_kendali_terbaca_mati():
    byte_parquet = {("A", "2024-01"): 900}
    kendali = sf.kendali_silang(
        byte_parquet, {("A", "2024-01"): kehidupan.STATUS_MATI}, set()
    )
    assert sf.kendali_sah(kendali) is False


def test_kendali_gagal_bila_kendali_kehilangan_funding():
    byte_parquet = {("A", "2024-01"): 900}
    kendali = sf.kendali_silang(
        byte_parquet, {("A", "2024-01"): kehidupan.STATUS_HIDUP}, {("A", "2024-01")}
    )
    assert sf.kendali_sah(kendali) is False


def _ringkasan_bersih(**ganti):
    dasar = {
        "sidik_seragam": True,
        "cacah_laporan_dibaca": sf.TOTAL_PECAHAN,
        "total_pecahan": sf.TOTAL_PECAHAN,
        "cacah_kunci_ganda": 0,
        "kendali_sah": True,
        "selisih_penyebut": 0,
        "selisih_mati": 0,
        "selisih_kohort": 0,
    }
    dasar.update(ganti)
    return dasar


def test_kode_keluar_nol_saat_bersih():
    assert sf.kode_keluar(_ringkasan_bersih()) == 0


def test_kode_keluar_dua_bila_penyebut_bergeser():
    assert sf.kode_keluar(_ringkasan_bersih(selisih_penyebut=-12)) == 2


def test_kode_keluar_dua_bila_cacah_mati_bergeser():
    assert sf.kode_keluar(_ringkasan_bersih(selisih_mati=5)) == 2


def test_lubang_tak_dikenal_bukan_penggugur():
    ringkasan = _ringkasan_bersih(cacah_lubang_tak_dikenal=12)
    assert sf.kode_keluar(ringkasan) == 0


def test_sidik_kode_heks_64_dan_stabil():
    sidik = sf.sidik_kode()
    assert len(sidik) == 64
    assert sidik == sf.sidik_kode()


def test_nama_keluaran_dan_ringkas():
    assert sf.nama_keluaran() == "reports/silang_funding.json"
    assert sf.nama_ringkas() == "reports/silang_funding_ringkas.json"


# --------------------------------------------------------------------------
# V2
# --------------------------------------------------------------------------

URUT = ["2024-01", "2024-02", "2024-03"]


def test_versi_dua():
    assert sf.VERSI == 2


def test_nama_daftar():
    assert sf.nama_daftar() == "reports/hidup_tanpa_funding.json"


def test_bulan_per_simbol_terurut():
    status = {
        ("A", "2024-03"): kehidupan.STATUS_HIDUP,
        ("A", "2024-01"): kehidupan.STATUS_MATI,
        ("B", "2024-02"): kehidupan.STATUS_HIDUP,
    }
    assert sf.bulan_per_simbol(status) == {
        "A": ["2024-01", "2024-03"],
        "B": ["2024-02"],
    }


def test_bentuk_lubang_lokal_awal():
    assert sf.bentuk_lubang_lokal(URUT, {"2024-01"}, "2024-01") == "awal"


def test_bentuk_lubang_lokal_ekor():
    assert sf.bentuk_lubang_lokal(URUT, {"2024-03"}, "2024-03") == "ekor"


def test_bentuk_lubang_lokal_tengah():
    assert sf.bentuk_lubang_lokal(URUT, {"2024-02"}, "2024-02") == "tengah"


def test_bentuk_lubang_lokal_seluruh():
    assert sf.bentuk_lubang_lokal(URUT, set(URUT), "2024-02") == "seluruh"


def test_bentuk_lubang_lokal_awal_dua_bulan_berurutan():
    assert sf.bentuk_lubang_lokal(URUT, {"2024-01", "2024-02"}, "2024-02") == "awal"


def test_bentuk_lubang_lokal_bukan_lubang():
    assert sf.bentuk_lubang_lokal(URUT, {"2024-01"}, "2024-02") == "bukan_lubang"


def test_daftar_hidup_tanpa_funding_hanya_hidup_yang_berlubang():
    status = {
        ("A", "2024-01"): kehidupan.STATUS_HIDUP,
        ("B", "2024-01"): kehidupan.STATUS_MATI,
        ("C", "2024-01"): kehidupan.STATUS_HIDUP,
    }
    baris = sf.daftar_hidup_tanpa_funding(
        status, {}, {("A", "2024-01"), ("B", "2024-01")}
    )
    assert [(r["simbol"], r["bulan"]) for r in baris] == [("A", "2024-01")]
    assert baris[0]["status"] == kehidupan.STATUS_HIDUP


def test_daftar_hidup_tanpa_funding_terurut_deterministik():
    status = {
        ("B", "2024-01"): kehidupan.STATUS_HIDUP,
        ("A", "2024-02"): kehidupan.STATUS_HIDUP,
        ("A", "2024-01"): kehidupan.STATUS_HIDUP,
    }
    baris = sf.daftar_hidup_tanpa_funding(status, {}, set(status))
    assert [(r["simbol"], r["bulan"]) for r in baris] == [
        ("A", "2024-01"),
        ("A", "2024-02"),
        ("B", "2024-01"),
    ]


def test_daftar_hidup_tanpa_funding_membawa_bentuk_byte_dan_lilin():
    status = {
        ("A", "2024-01"): kehidupan.STATUS_HIDUP,
        ("A", "2024-02"): kehidupan.STATUS_HIDUP,
    }
    baris = sf.daftar_hidup_tanpa_funding(
        status, {("A", "2024-01"): 77}, {("A", "2024-01")}, {("A", "2024-01"): 5}
    )
    assert baris[0]["bentuk_lubang_lokal"] == "awal"
    assert baris[0]["byte_parquet"] == 77
    assert baris[0]["cacah_lilin"] == 5
    assert baris[0]["cacah_bulan_klines_simbol"] == 2
    assert baris[0]["cacah_lubang_simbol"] == 1


def test_cacah_lilin_null_bila_tidak_tersedia():
    status = {("A", "2024-01"): kehidupan.STATUS_HIDUP}
    baris = sf.daftar_hidup_tanpa_funding(status, {}, {("A", "2024-01")})
    assert baris[0]["cacah_lilin"] is None


def test_daftar_lubang_tak_dikenal_menandai_simbol_dikenal():
    status = {("A", "2024-01"): kehidupan.STATUS_HIDUP}
    baris = sf.daftar_lubang_tak_dikenal(
        status, {("A", "2024-09"), ("Z", "2024-01")}
    )
    assert [(r["simbol"], r["simbol_dikenal"]) for r in baris] == [
        ("A", True),
        ("Z", False),
    ]
    assert baris[0]["bulan_klines_terakhir"] == "2024-01"
    assert baris[1]["cacah_bulan_klines_simbol"] == 0


def test_daftar_lubang_tak_dikenal_kosong_bila_semua_dikenal():
    status = {("A", "2024-01"): kehidupan.STATUS_HIDUP}
    assert sf.daftar_lubang_tak_dikenal(status, {("A", "2024-01")}) == []


def test_sebaran_bentuk_mencacah_empat_kelas():
    baris = [
        {"bentuk_lubang_lokal": "awal"},
        {"bentuk_lubang_lokal": "awal"},
        {"bentuk_lubang_lokal": "ekor"},
    ]
    assert sf.sebaran_bentuk(baris) == {
        "awal": 2,
        "ekor": 1,
        "tengah": 0,
        "seluruh": 0,
    }


def test_sebaran_bentuk_semua_hanya_lubang_dalam_penyebut():
    status = {
        ("A", "2024-01"): kehidupan.STATUS_HIDUP,
        ("A", "2024-02"): kehidupan.STATUS_MATI,
    }
    sebaran = sf.sebaran_bentuk_semua(status, {("A", "2024-02"), ("Z", "2024-01")})
    assert sebaran == {"awal": 0, "ekor": 1, "tengah": 0, "seluruh": 0}


def test_kode_keluar_dua_bila_hidup_tanpa_funding_bergeser():
    assert sf.kode_keluar(_ringkasan_bersih(selisih_hidup_tanpa_funding=-1)) == 2


def test_kode_keluar_dua_bila_lubang_tak_dikenal_bergeser():
    assert sf.kode_keluar(_ringkasan_bersih(selisih_lubang_tak_dikenal=2)) == 2


def test_medan_baris_terlihat_dicatat_apa_adanya(tmp_path):
    _tulis_pecahan(tmp_path, 0, [_baris("A", "2024-01", kehidupan.STATUS_HIDUP)])
    nilai, meta = sf.baca_medan_baris(akar=str(tmp_path), total=1)
    assert nilai == {}
    assert meta["medan_baris_terlihat"] == [
        "bulan",
        "byte_parquet",
        "simbol",
        "status",
    ]
    assert meta["cacah_baris_dengan_medan"] == 0


def test_baca_medan_baris_mengambil_nilai_yang_ada(tmp_path):
    baris = _baris("A", "2024-01", kehidupan.STATUS_HIDUP)
    baris["cacah_lilin"] = 44
    _tulis_pecahan(tmp_path, 0, [baris])
    nilai, meta = sf.baca_medan_baris(akar=str(tmp_path), total=1)
    assert nilai == {("A", "2024-01"): 44}
    assert meta["cacah_baris_dengan_medan"] == 1
    assert meta["medan_diminta"] == "cacah_lilin"


def test_berkas_daftar_memuat_kedua_daftar():
    laporan = {
        "versi_silang_funding": 2,
        "sidik_kode": "x",
        "definisi": {"bentuk_lubang_lokal": "definisi"},
        "baris_hidup_tanpa_funding": [{"simbol": "A"}],
        "lubang_tak_dikenal": [{"simbol": "Z"}],
        "ringkasan": {"cacah_hidup_tanpa_funding": 1},
    }
    daftar = sf.berkas_daftar(laporan)
    assert daftar["baris_hidup_tanpa_funding"] == [{"simbol": "A"}]
    assert daftar["lubang_tak_dikenal"] == [{"simbol": "Z"}]
    assert daftar["cacah_hidup_tanpa_funding"] == 1
    assert daftar["definisi_bentuk_lubang_lokal"] == "definisi"


def test_bentuk_terbitan_funding_hanya_pembanding():
    assert sf.BENTUK_TERBITAN_FUNDING == {"awal": 48, "ekor": 826, "tengah": 6}


def test_angka_tercatat_v1_dipakai_sebagai_penggugur():
    assert sf.HIDUP_TANPA_FUNDING_TERCATAT == 33
    assert sf.LUBANG_TAK_DIKENAL_TERCATAT == 3
