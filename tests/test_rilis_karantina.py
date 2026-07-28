"""Uji pengemas kedua untuk parquet karantina (KC-17).

Berkas uji terpisah dari `tests/test_rilis.py` supaya 17 uji yang sudah
terverifikasi CI tidak perlu ditulis ulang — `push_files` menimpa seluruh isi
berkas, dan menulis ulang uji yang sudah hijau dari ingatan adalah cara termurah
merusaknya.

Yang diuji di sini justru dua hal yang hampir lolos tanpa terlihat:
1. dua pengemas di SATU direktori saling menimpa berkas sidiknya;
2. pengemas tanpa satu pun anggota — keadaan nyata pecahan 2 dan 5 yang tidak
   punya karantina — menghasilkan `sah` = false, sehingga pemanggilnya WAJIB
   memperlakukan "nol karantina" secara terpisah, bukan sebagai kegagalan.
"""

from __future__ import annotations

import tarfile
from pathlib import Path

from lux_ai.serapan import rilis


def _buat(akar: Path, rel: str, byte_isi: int) -> str:
    jalur = akar / rel
    jalur.parent.mkdir(parents=True, exist_ok=True)
    jalur.write_bytes(b"x" * byte_isi)
    return rel


def test_dua_pengemas_satu_direktori_tidak_saling_menimpa_sums(tmp_path):
    utama_rel = _buat(tmp_path, "data/parquet/AAA/AAA-1m-2025-01.parquet", 5000)
    kar_rel = _buat(
        tmp_path, "data/parquet_karantina/BBB/BBB-1m-2025-02.parquet", 3000
    )

    utama = rilis.PengemasBerbelah(akar=str(tmp_path), nama_dasar="pecahan_9")
    utama.tambah(utama_rel)
    lap_utama = utama.tutup()

    karantina = rilis.PengemasBerbelah(
        akar=str(tmp_path),
        nama_dasar="pecahan_9_karantina",
        nama_sums=rilis.NAMA_SUMS_KARANTINA,
    )
    karantina.tambah(kar_rel)
    lap_kar = karantina.tutup()

    assert lap_utama["berkas_sums"].endswith(rilis.NAMA_SUMS)
    assert lap_kar["berkas_sums"].endswith(rilis.NAMA_SUMS_KARANTINA)
    assert lap_utama["berkas_sums"] != lap_kar["berkas_sums"]

    isi_utama = (tmp_path / lap_utama["berkas_sums"]).read_text(encoding="utf-8")
    isi_kar = (tmp_path / lap_kar["berkas_sums"]).read_text(encoding="utf-8")
    assert "pecahan_9.part01.tar" in isi_utama
    assert "karantina" not in isi_utama
    assert "pecahan_9_karantina.part01.tar" in isi_kar

    assert rilis.verifikasi(str(tmp_path), lap_utama)["sah"] is True
    assert rilis.verifikasi(str(tmp_path), lap_kar)["sah"] is True


def test_pengemas_karantina_kosong_tidak_menulis_sums_dan_tidak_sah(tmp_path):
    kosong = rilis.PengemasBerbelah(
        akar=str(tmp_path),
        nama_dasar="pecahan_9_karantina",
        nama_sums=rilis.NAMA_SUMS_KARANTINA,
    )
    laporan = kosong.tutup()

    assert laporan["status"] == "TIDAK MENGEMAS"
    assert laporan["cacah_bagian"] == 0
    assert laporan["cacah_berkas"] == 0
    assert laporan["berkas_sums"] is None
    assert not (tmp_path / rilis.AKAR_RILIS / rilis.NAMA_SUMS_KARANTINA).exists()
    # Penting bagi pecahan.py: nol anggota BUKAN persistensi yang sah, jadi
    # keadaan "pecahan ini memang tidak punya karantina" wajib dibedakan.
    assert rilis.verifikasi(str(tmp_path), laporan)["sah"] is False


def test_karantina_dikemas_dengan_jalur_asli_dan_sumber_dihapus(tmp_path):
    rel = _buat(tmp_path, "data/parquet_karantina/BBB/BBB-1m-2025-02.parquet", 1500)
    karantina = rilis.PengemasBerbelah(
        akar=str(tmp_path),
        nama_dasar="pecahan_9_karantina",
        nama_sums=rilis.NAMA_SUMS_KARANTINA,
    )
    karantina.tambah(rel)
    laporan = karantina.tutup()

    assert not (tmp_path / rel).exists()
    jalur_tar = tmp_path / laporan["bagian"][0]["jalur"]
    with tarfile.open(jalur_tar, "r") as tar:
        nama = [m.name for m in tar.getmembers() if m.isfile()]
    assert nama == [rel]
