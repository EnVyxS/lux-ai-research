"""Uji modul kohort_ekor tanpa jaringan sama sekali.

Tujuh fungsi uji, TANPA `parametrize`, sehingga cacah fungsi sama dengan cacah
butir pytest (aturan 47).
"""

from __future__ import annotations

import hashlib
import io
import json
import zipfile
from pathlib import Path

from lux_ai.serapan import kohort_ekor


def _zip_klines(nama: str, baris: list) -> bytes:
    penyangga = io.BytesIO()
    with zipfile.ZipFile(penyangga, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(nama, "\n".join(baris) + "\n")
    return penyangga.getvalue()


def _lilin(waktu: int, volume: str, transaksi: str) -> str:
    return f"{waktu},1,1,1,1,{volume},{waktu + 59999},10,{transaksi},0,0,0"


def test_sidik_kode_mencakup_gerbang_dan_arsip():
    """Aturan 48: sidik menyempit diam-diam bila daftar berkasnya kurang."""
    akar = Path(kohort_ekor.__file__).parent

    def sidik(nama_berkas):
        h = hashlib.sha256()
        for nama in sorted(nama_berkas):
            h.update((akar / nama).read_bytes())
        return h.hexdigest()

    penuh = ["arsip.py", "gerbang_1m.py", "kohort_ekor.py", "resample.py"]
    assert kohort_ekor.sidik_kode() == sidik(penuh)
    # menghapus satu nama HARUS mengubah sidik, kalau tidak cakupannya semu
    assert kohort_ekor.sidik_kode() != sidik(["kohort_ekor.py", "arsip.py"])


def test_baca_zip_klines_mengenali_header_dari_isi():
    tanpa = _zip_klines(
        "X-1m-2026-06.csv", [_lilin(1750000000000, "1.5", "7"), _lilin(1750000060000, "0", "0")]
    )
    hasil = kohort_ekor.baca_zip_klines(tanpa)
    assert hasil["berheader"] is False
    assert hasil["cacah_baris"] == 2
    assert hasil["cap_waktu"] == [1750000000000, 1750000060000]

    dengan = _zip_klines(
        "X-1m-2026-06.csv",
        [
            "open_time,open,high,low,close,volume,close_time,quote_volume,count,a,b,c",
            _lilin(1750000000000, "2", "3"),
        ],
    )
    hasil2 = kohort_ekor.baca_zip_klines(dengan)
    assert hasil2["berheader"] is True
    assert hasil2["cacah_baris"] == 1


def test_baca_zip_klines_mencacah_baris_cacat_bukan_membuangnya_diam_diam():
    data = _zip_klines(
        "X-1m-2026-06.csv",
        [_lilin(1750000000000, "1", "1"), "1750000060000,1,1", "1750000120000,1,1,1,1,x,1,1,1,0,0,0"],
    )
    hasil = kohort_ekor.baca_zip_klines(data)
    assert hasil["cacah_baris"] == 1
    assert hasil["cacah_baris_cacat"] == 2


def test_ringkas_lilin_memisahkan_volume_nol_dari_transaksi_nol():
    """Volume nol dan transaksi nol bukan hal yang sama (aturan 46)."""
    terurai = {"volume": [0.0, 1.0, 0.0, 2.0], "transaksi": [0, 0, 0, 5]}
    r = kohort_ekor.ringkas_lilin(terurai)
    assert r["cacah_lilin"] == 4
    assert r["cacah_volume_nol"] == 2
    assert r["cacah_transaksi_nol"] == 3
    assert r["bagian_volume_nol"] == 0.5
    assert r["bagian_transaksi_nol"] == 0.75
    assert r["volume_total"] == 3.0
    assert r["transaksi_total"] == 5


def test_bagian_menolak_penyebut_nol():
    assert kohort_ekor.bagian(0, 0) is None
    assert kohort_ekor.ringkas_lilin({"volume": [], "transaksi": []})["bagian_volume_nol"] is None
    assert kohort_ekor.bagian(1, 4) == 0.25


def test_mundur_bulan_melintasi_pergantian_tahun():
    assert kohort_ekor.mundur_bulan("2025-07") == "2025-06"
    assert kohort_ekor.mundur_bulan("2025-01") == "2024-12"
    assert kohort_ekor.mundur_bulan("2025-01", 13) == "2023-12"
    assert kohort_ekor.mundur_bulan("bukan-bulan") is None
    assert kohort_ekor.mundur_bulan("2025-13") is None


def test_ringkas_menyalakan_penggugur_saat_kendali_gagal_atau_bulan_meleset():
    baris = [
        {"peran": "uji", "bulan": "2026-06", "bagian_volume_nol": 0.1, "lolos_gerbang": True},
        {"peran": "uji", "bulan": "2026-05", "bagian_volume_nol": 0.9, "lolos_gerbang": True},
        {"peran": "kendali", "bulan": "2025-06", "galat": "putus", "gagal_unduh": True},
    ]
    r = kohort_ekor.ringkas(baris)
    assert r["cacah_uji_diminta"] == 2
    assert r["cacah_uji_bagian_volume_nol_di_bawah_setengah"] == 1
    assert r["cacah_uji_bulan_bukan_diharapkan"] == 1
    assert r["cacah_gagal_unduh"] == 1
    assert r["kendali_sah"] is False
    # kendali yang utuh mensahkan pembandingnya
    baik = kohort_ekor.ringkas(
        baris[:1] + [{"peran": "kendali", "bulan": "2025-06", "bagian_volume_nol": 0.2}]
    )
    assert baik["kendali_sah"] is True
    assert baik["cacah_kendali_bagian_volume_nol_di_bawah_setengah"] == 1


def test_muat_kohort_melaporkan_galat_alih_alih_melempar(tmp_path):
    kosong = kohort_ekor.muat_kohort(str(tmp_path))
    assert kosong["simbol"] == []
    assert kosong["galat"]

    (tmp_path / "reports").mkdir()
    (tmp_path / "reports" / "funding_semesta.json").write_text(
        json.dumps({"kohort_puncak": {"bulan_mulai": "2025-07", "simbol": ["BBB", "AAA"]}}),
        encoding="utf-8",
    )
    ada = kohort_ekor.muat_kohort(str(tmp_path))
    assert ada["simbol"] == ["AAA", "BBB"]
    assert ada["bulan_mulai"] == "2025-07"
    assert ada["galat"] is None
