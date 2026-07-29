"""Uji `silang_funding`: pembacaan laporan, irisan, kendali, dan kode keluar.

Seluruh uji memakai laporan tiruan di `tmp_path`; tidak ada jaringan dan tidak
ada aset rilis. Yang dijaga di sini adalah bagian yang bila salah akan membuat
laporan irisan terbaca meyakinkan namun keliru: penyebut yang bocor, laporan
pecahan yang hilang diam-diam, dan kendali yang tidak menggugurkan apa pun.

Cacah butir: 18 fungsi berbutir tunggal + 1 fungsi berparameter tiga kasus = 21
butir (aturan 38, 47).
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
