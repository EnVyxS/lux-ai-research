"""Uji pengemas rilis terbelah. Tanpa jaringan; berkas sintetis kecil."""

import tarfile

import pytest

from lux_ai.serapan import rilis


def test_perkiraan_byte_anggota_membulat_ke_blok():
    assert rilis.perkiraan_byte_anggota(0) == 512
    assert rilis.perkiraan_byte_anggota(1) == 1024
    assert rilis.perkiraan_byte_anggota(512) == 1024
    assert rilis.perkiraan_byte_anggota(513) == 1536


def test_perkiraan_byte_anggota_menolak_negatif():
    with pytest.raises(ValueError):
        rilis.perkiraan_byte_anggota(-1)


def test_rencana_belah_tidak_melewati_batas():
    batas = 10 * 512
    ukuran = [512] * 12  # tiap anggota memakai 1024 byte
    bagian = rilis.rencana_belah(ukuran, batas=batas)
    assert sum(len(b) for b in bagian) == 12
    assert [i for b in bagian for i in b] == list(range(12))
    for b in bagian:
        pakai = rilis.BYTE_AKHIR_TAR + sum(
            rilis.perkiraan_byte_anggota(ukuran[i]) for i in b
        )
        assert pakai <= batas


def test_rencana_belah_berkas_raksasa_sendirian():
    batas = 4 * 512
    bagian = rilis.rencana_belah([100, 100_000, 100], batas=batas)
    assert [len(b) for b in bagian] == [1, 1, 1]


def test_rencana_belah_menolak_batas_mustahil():
    with pytest.raises(ValueError):
        rilis.rencana_belah([1], batas=512)


def _buat(tmp_path, nama, byte_isi):
    jalur = tmp_path / nama
    jalur.parent.mkdir(parents=True, exist_ok=True)
    jalur.write_bytes(b"x" * byte_isi)
    return nama


def test_pengemas_membelah_menghapus_sumber_dan_menulis_sums(tmp_path):
    nama = [
        _buat(tmp_path, f"data/parquet/AUSDT/A-1m-2025-0{i}.parquet", 900)
        for i in range(1, 7)
    ]
    kemas = rilis.PengemasBerbelah(
        akar=str(tmp_path), nama_dasar="pecahan_9", batas=6 * 512
    )
    for n in nama:
        assert kemas.tambah(n)["ditambahkan"] is True
    laporan = kemas.tutup()

    assert laporan["status"] == "TERKEMAS"
    assert laporan["cacah_berkas"] == 6
    assert laporan["cacah_bagian"] >= 3
    assert laporan["cacah_bagian_melebihi_batas"] == 0
    assert laporan["cacah_berkas_hilang"] == 0
    assert laporan["byte_anggota_total"] == 6 * 900
    # sumber dihapus supaya puncak cakram tetap ≈ satu bagian
    for n in nama:
        assert not (tmp_path / n).exists()
    sums = tmp_path / "data/rilis/SHA256SUMS"
    assert sums.exists()
    assert len(sums.read_text(encoding="utf-8").strip().splitlines()) == laporan[
        "cacah_bagian"
    ]


def test_pengemas_memulihkan_jalur_asli(tmp_path):
    n = _buat(tmp_path, "data/parquet/u4E2DUSDT/x-1m-2024-01.parquet", 64)
    kemas = rilis.PengemasBerbelah(akar=str(tmp_path), nama_dasar="p0")
    kemas.tambah(n)
    laporan = kemas.tutup()
    jalur = tmp_path / laporan["bagian"][0]["jalur"]
    with tarfile.open(jalur, "r") as tar:
        assert [m.name for m in tar.getmembers()] == [n]


def test_pengemas_mencatat_berkas_hilang(tmp_path):
    kemas = rilis.PengemasBerbelah(akar=str(tmp_path), nama_dasar="p0")
    hasil = kemas.tambah("data/parquet/tidak/ada.parquet")
    assert hasil["ditambahkan"] is False
    laporan = kemas.tutup()
    assert laporan["status"] == "TIDAK MENGEMAS"
    assert laporan["cacah_berkas_hilang"] == 1
    assert laporan["berkas_sums"] is None


def test_verifikasi_sah_lalu_gugur_saat_tar_dirusak(tmp_path):
    for i in range(3):
        _buat(tmp_path, f"data/parquet/AUSDT/A-1m-2025-0{i}.parquet", 700)
    kemas = rilis.PengemasBerbelah(akar=str(tmp_path), nama_dasar="p1", batas=4 * 512)
    for i in range(3):
        kemas.tambah(f"data/parquet/AUSDT/A-1m-2025-0{i}.parquet")
    laporan = kemas.tutup()

    baik = rilis.verifikasi(str(tmp_path), laporan)
    assert baik["sah"] is True
    assert baik["cacah_anggota_terbaca"] == 3
    assert baik["cacah_sha_tak_cocok"] == 0

    laporan["bagian"][0]["sha256"] = "0" * 64
    rusak = rilis.verifikasi(str(tmp_path), laporan)
    assert rusak["sah"] is False
    assert rusak["cacah_sha_tak_cocok"] == 1


def test_verifikasi_menangkap_bagian_hilang(tmp_path):
    _buat(tmp_path, "data/parquet/AUSDT/A-1m-2025-01.parquet", 100)
    kemas = rilis.PengemasBerbelah(akar=str(tmp_path), nama_dasar="p2")
    kemas.tambah("data/parquet/AUSDT/A-1m-2025-01.parquet")
    laporan = kemas.tutup()
    (tmp_path / laporan["bagian"][0]["jalur"]).unlink()
    hasil = rilis.verifikasi(str(tmp_path), laporan)
    assert hasil["sah"] is False
    assert hasil["cacah_bagian_hilang"] == 1


def test_baris_sums_format_sha256sum():
    teks = rilis.baris_sums([{"sha256": "a" * 64, "nama": "p.part01.tar"}])
    assert teks == "a" * 64 + "  p.part01.tar\n"
