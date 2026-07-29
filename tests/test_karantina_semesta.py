"""Uji karantina_semesta V1.

Daftar bernomor (aturan 54/56/57): **28** fungsi `def test_`, tanpa satu pun
`parametrize`, sehingga 28 butir. Dasar CI 694 (run 30479093362) -> ramalan
R-294 = 722 butir.

 1 test_versi_modul_satu
 2 test_nama_keluaran_tetap
 3 test_r291_himpunan_dua_belas
 4 test_bulan_menit_31_hari
 5 test_bulan_menit_februari_kabisat
 6 test_bulan_menit_februari_biasa
 7 test_bulan_menit_rusak_nol
 8 test_kunci_entri
 9 test_perkaya_selisih_menit
10 test_perkaya_nisbah_lilin
11 test_perkaya_tanpa_parquet
12 test_entri_karantina_dari_blok
13 test_entri_karantina_dari_kunci_atas
14 test_entri_karantina_kosong
15 test_baca_manifes_hilang_none
16 test_jalankan_bersih_kode_nol
17 test_jalankan_r291_menang
18 test_jalankan_r291_kalah_tidak_menggugurkan
19 test_jalankan_manifes_hilang_menggugurkan
20 test_jalankan_kunci_ganda_menggugurkan
21 test_jalankan_selisih_cacah_daftar_menggugurkan
22 test_jalankan_daftar_terpotong_menggugurkan
23 test_jalankan_dibuang_menggugurkan
24 test_jalankan_ditambal_menggugurkan
25 test_jalankan_sidik_tak_seragam_menggugurkan
26 test_jalankan_kendali_btc_menggugurkan
27 test_jalankan_selisih_ditulis_terdaftar_menggugurkan
28 test_jalankan_menulis_dua_berkas_dan_sebaran
"""

from __future__ import annotations

import json
from pathlib import Path

from lux_ai.serapan import karantina_semesta as ks
from lux_ai.serapan import pulihkan


def _entri(simbol, bulan, baris=1000, pelanggaran=("menit_kurang",), parquet=True):
    return {
        "simbol": simbol,
        "bulan": bulan,
        "baris": baris,
        "pelanggaran": list(pelanggaran),
        "parquet_karantina": (
            f"data/parquet_karantina/{simbol}/{simbol}-1m-{bulan}.parquet"
            if parquet
            else None
        ),
        "checksum_zip_sha256": "0" * 64,
    }


def _manifes(entri, sidik="sidik-a", ditulis=None, **ubah):
    blok = {
        "cacah_karantina": len(entri),
        "daftar_karantina": list(entri),
        "daftar_terpotong": False,
        "cacah_dibuang": 0,
        "cacah_ditambal": 0,
        "byte_parquet_karantina": 100 * len(entri),
    }
    blok.update(ubah)
    return {
        "sidik_kode": sidik,
        "versi_pecahan": 6,
        "karantina_dipersistenkan": True,
        "cacah_parquet_karantina_ditulis": len(entri) if ditulis is None else ditulis,
        "cacah_karantina_tak_terkemas": 0,
        "karantina": blok,
    }


def _tulis(akar: Path, daftar_manifes):
    for i, isi in enumerate(daftar_manifes):
        if isi is None:
            continue
        jalur = akar / pulihkan.nama_manifes(i)
        jalur.parent.mkdir(parents=True, exist_ok=True)
        jalur.write_text(json.dumps(isi, ensure_ascii=False), encoding="utf-8")


def _dua_belas():
    """Kedua belas entri R-291 dibagi ke dua manifes palsu."""
    semua = [_entri(s, b) for s, b in ks.R291_HIMPUNAN]
    return [_manifes(semua[:7]), _manifes(semua[7:])]


def test_versi_modul_satu():
    assert ks.VERSI == 1


def test_nama_keluaran_tetap():
    assert ks.KELUARAN == "reports/karantina_semesta.json"
    assert ks.KELUARAN_RINGKAS == "reports/karantina_semesta_ringkas.json"


def test_r291_himpunan_dua_belas():
    assert len(ks.R291_HIMPUNAN) == ks.R291_CACAH == 12
    assert len(set(ks.R291_HIMPUNAN)) == 12


def test_bulan_menit_31_hari():
    assert ks.bulan_menit("2022-08") == 31 * 1440


def test_bulan_menit_februari_kabisat():
    assert ks.bulan_menit("2024-02") == 29 * 1440


def test_bulan_menit_februari_biasa():
    assert ks.bulan_menit("2023-02") == 28 * 1440


def test_bulan_menit_rusak_nol():
    assert ks.bulan_menit("bukan-bulan") == 0
    assert ks.bulan_menit("") == 0


def test_kunci_entri():
    assert ks.kunci(_entri("LITUSDT", "2025-12")) == ("LITUSDT", "2025-12")
    assert ks.kunci({}) == ("", "")


def test_perkaya_selisih_menit():
    r = ks.perkaya(_entri("BNXUSDT", "2022-04", baris=41550), 3)
    assert r["menit_kalender"] == 43200
    assert r["selisih_menit"] == 43200 - 41550
    assert r["indeks_pecahan"] == 3


def test_perkaya_nisbah_lilin():
    r = ks.perkaya(_entri("XUSDT", "2022-04", baris=21600), 0)
    assert r["nisbah_lilin"] == 0.5
    rusak = ks.perkaya(_entri("XUSDT", "tak-terbaca", baris=10), 0)
    assert rusak["nisbah_lilin"] is None
    assert rusak["selisih_menit"] is None


def test_perkaya_tanpa_parquet():
    r = ks.perkaya(_entri("XUSDT", "2025-01", parquet=False), 1)
    assert r["ada_parquet_karantina"] is False
    assert r["ada_checksum_zip"] is True


def test_entri_karantina_dari_blok():
    m = _manifes([_entri("AUSDT", "2025-01")])
    assert len(ks.entri_karantina(m)) == 1


def test_entri_karantina_dari_kunci_atas():
    m = {"daftar_karantina": [_entri("AUSDT", "2025-01")]}
    assert len(ks.entri_karantina(m)) == 1


def test_entri_karantina_kosong():
    assert ks.entri_karantina({}) == []
    assert ks.entri_karantina({"karantina": {"daftar_karantina": None}}) == []


def test_baca_manifes_hilang_none(tmp_path):
    assert ks.baca_manifes(0, akar=str(tmp_path)) is None


def test_jalankan_bersih_kode_nol(tmp_path):
    _tulis(tmp_path, _dua_belas())
    hasil = ks.jalankan(akar=str(tmp_path), total=2)
    ringkas = hasil["ringkasan"]
    assert ringkas["cacah_manifes_dibaca"] == 2
    assert ringkas["cacah_karantina_semesta"] == 12
    assert ringkas["selisih_penyebut"] == 0
    assert ringkas["kendali_sah"] is True
    assert ks.kode_keluar(ringkas) == 0


def test_jalankan_r291_menang(tmp_path):
    _tulis(tmp_path, _dua_belas())
    ringkas = ks.jalankan(akar=str(tmp_path), total=2)["ringkasan"]
    uji = ringkas["uji_r291"]
    assert uji["menang"] is True
    assert uji["mudah"] is False
    assert uji["diramalkan_hilang"] == []
    assert uji["terukur_tak_diramalkan"] == []


def test_jalankan_r291_kalah_tidak_menggugurkan(tmp_path):
    manifes = _dua_belas()
    manifes.append(_manifes([_entri("ZZZUSDT", "2026-06")]))
    _tulis(tmp_path, manifes)
    ringkas = ks.jalankan(akar=str(tmp_path), total=3)["ringkasan"]
    assert ringkas["cacah_karantina_semesta"] == 13
    assert ringkas["uji_r291"]["menang"] is False
    assert ringkas["uji_r291"]["terukur_tak_diramalkan"] == [["ZZZUSDT", "2026-06"]]
    assert ringkas["selisih_penyebut"] == -1
    assert ks.kode_keluar(ringkas) == 0


def test_jalankan_manifes_hilang_menggugurkan(tmp_path):
    _tulis(tmp_path, [_manifes([_entri("AUSDT", "2025-01")])])
    ringkas = ks.jalankan(akar=str(tmp_path), total=2)["ringkasan"]
    assert ringkas["manifes_hilang"] == [1]
    assert ringkas["kendali_sah"] is False
    assert ks.kode_keluar(ringkas) == 2


def test_jalankan_kunci_ganda_menggugurkan(tmp_path):
    sama = _entri("AUSDT", "2025-01")
    _tulis(tmp_path, [_manifes([sama]), _manifes([dict(sama)])])
    ringkas = ks.jalankan(akar=str(tmp_path), total=2)["ringkasan"]
    assert ringkas["cacah_kunci_ganda"] == 1
    assert ks.kode_keluar(ringkas) == 2


def test_jalankan_selisih_cacah_daftar_menggugurkan(tmp_path):
    m = _manifes([_entri("AUSDT", "2025-01")], cacah_karantina=5)
    _tulis(tmp_path, [m])
    ringkas = ks.jalankan(akar=str(tmp_path), total=1)["ringkasan"]
    assert ringkas["jumlah_selisih_cacah_daftar"] == 4
    assert ks.kode_keluar(ringkas) == 2


def test_jalankan_daftar_terpotong_menggugurkan(tmp_path):
    m = _manifes([_entri("AUSDT", "2025-01")], daftar_terpotong=True)
    _tulis(tmp_path, [m])
    ringkas = ks.jalankan(akar=str(tmp_path), total=1)["ringkasan"]
    assert ringkas["cacah_daftar_terpotong"] == 1
    assert ks.kode_keluar(ringkas) == 2


def test_jalankan_dibuang_menggugurkan(tmp_path):
    m = _manifes([_entri("AUSDT", "2025-01")], cacah_dibuang=1)
    _tulis(tmp_path, [m])
    ringkas = ks.jalankan(akar=str(tmp_path), total=1)["ringkasan"]
    assert ringkas["jumlah_cacah_dibuang"] == 1
    assert ks.kode_keluar(ringkas) == 2


def test_jalankan_ditambal_menggugurkan(tmp_path):
    m = _manifes([_entri("AUSDT", "2025-01")], cacah_ditambal=3)
    _tulis(tmp_path, [m])
    ringkas = ks.jalankan(akar=str(tmp_path), total=1)["ringkasan"]
    assert ringkas["jumlah_cacah_ditambal"] == 3
    assert ks.kode_keluar(ringkas) == 2


def test_jalankan_sidik_tak_seragam_menggugurkan(tmp_path):
    _tulis(
        tmp_path,
        [
            _manifes([_entri("AUSDT", "2025-01")], sidik="sidik-a"),
            _manifes([_entri("BUSDT", "2025-02")], sidik="sidik-b"),
        ],
    )
    ringkas = ks.jalankan(akar=str(tmp_path), total=2)["ringkasan"]
    assert ringkas["sidik_seragam"] is False
    assert len(ringkas["sidik_kode_manifes"]) == 2
    assert ks.kode_keluar(ringkas) == 2


def test_jalankan_kendali_btc_menggugurkan(tmp_path):
    _tulis(tmp_path, [_manifes([_entri("BTCUSDT", "2022-01")])])
    ringkas = ks.jalankan(akar=str(tmp_path), total=1)["ringkasan"]
    assert ringkas["kendali"][0] == {"simbol": "BTCUSDT", "cacah": 1, "sah": False}
    assert ringkas["kendali_sah"] is False
    assert ks.kode_keluar(ringkas) == 2


def test_jalankan_selisih_ditulis_terdaftar_menggugurkan(tmp_path):
    _tulis(tmp_path, [_manifes([_entri("AUSDT", "2025-01")], ditulis=4)])
    ringkas = ks.jalankan(akar=str(tmp_path), total=1)["ringkasan"]
    assert ringkas["selisih_ditulis_terdaftar"] == 3
    assert ks.kode_keluar(ringkas) == 2


def test_jalankan_menulis_dua_berkas_dan_sebaran(tmp_path):
    _tulis(
        tmp_path,
        [
            _manifes([_entri("AUSDT", "2025-01", pelanggaran=("menit_kurang",))]),
            _manifes(
                [_entri("BUSDT", "2025-02", pelanggaran=("menit_kurang", "tepi"))]
            ),
        ],
    )
    hasil = ks.jalankan(akar=str(tmp_path), total=2)
    assert (tmp_path / ks.KELUARAN).exists()
    assert (tmp_path / ks.KELUARAN_RINGKAS).exists()
    assert hasil["ringkasan"]["sebaran_pelanggaran"] == {"menit_kurang": 2, "tepi": 1}
    assert hasil["ringkasan"]["cacah_pecahan_berkarantina"] == 2
    assert hasil["ringkasan"]["pecahan_tanpa_karantina"] == []
    assert [r["simbol"] for r in hasil["baris"]] == ["AUSDT", "BUSDT"]
