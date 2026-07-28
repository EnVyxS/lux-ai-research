"""Uji pengemas rilis terbelah. Tanpa jaringan; berkas sintetis kecil.

Tiga putaran membuktikan model ukuran tar saya terlalu kecil: bantalan
`RECORDSIZE`, lalu "satu rekam misterius", lalu — pada 1.055 anggota nyata di
run `30376241019` — sebabnya yang sebenarnya: header **pax** 1.024 byte per
anggota.

Pelajaran yang dibakukan di sini (aturan 43): galat yang menskala per item TIDAK
boleh diuji dengan segelintir item, karena margin tetap akan menelannya. Karena
itu `test_taksiran_tahan_pada_banyak_anggota` memakai 120 anggota; dengan model
lama uji itu gagal telak, dengan model 6 anggota ia lolos padahal cacat.

Tidak satu pun tuntutan dilonggarkan: `cacah_bagian_melebihi_batas == 0`,
`cacah_bagian_taksiran_terlampaui == 0`, dan `byte <= byte_taksir_dibulatkan`
tetap berlaku.
"""

import tarfile

import pytest

from lux_ai.serapan import rilis

REKAM = rilis.REKAM_TAR
MARGIN = rilis.MARGIN_REKAM
KEPALA = rilis.KEPALA_ANGGOTA


def test_perkiraan_byte_anggota_membulat_ke_blok():
    assert KEPALA == 1536  # kepala tar 512 + pax 1.024
    assert rilis.perkiraan_byte_anggota(0) == KEPALA
    assert rilis.perkiraan_byte_anggota(1) == KEPALA + 512
    assert rilis.perkiraan_byte_anggota(512) == KEPALA + 512
    assert rilis.perkiraan_byte_anggota(513) == KEPALA + 1024


def test_perkiraan_byte_anggota_menolak_negatif():
    with pytest.raises(ValueError):
        rilis.perkiraan_byte_anggota(-1)


def test_bulatkan_rekam_mengikuti_recordsize_tarfile():
    assert REKAM == tarfile.RECORDSIZE == 10240
    assert rilis.bulatkan_rekam(0) == 0
    assert rilis.bulatkan_rekam(1) == REKAM
    assert rilis.bulatkan_rekam(REKAM) == REKAM
    assert rilis.bulatkan_rekam(REKAM + 1) == 2 * REKAM
    with pytest.raises(ValueError):
        rilis.bulatkan_rekam(-1)


def test_taksir_bagian_selalu_menambah_margin():
    assert MARGIN == 2 * REKAM
    assert rilis.taksir_bagian(0) == MARGIN
    assert rilis.taksir_bagian(1) == REKAM + MARGIN
    assert rilis.taksir_bagian(REKAM) == REKAM + MARGIN
    assert rilis.taksir_bagian(REKAM + 1) == 2 * REKAM + MARGIN


def test_rencana_belah_tidak_melewati_batas():
    batas = 6 * REKAM
    ukuran = [10_000] * 8
    bagian = rilis.rencana_belah(ukuran, batas=batas)
    assert sum(len(b) for b in bagian) == 8
    assert [i for b in bagian for i in b] == list(range(8))
    assert len(bagian) > 1
    for b in bagian:
        pakai = rilis.taksir_bagian(
            rilis.BYTE_AKHIR_TAR
            + sum(rilis.perkiraan_byte_anggota(ukuran[i]) for i in b)
        )
        assert pakai <= batas


def test_rencana_belah_berkas_raksasa_sendirian():
    bagian = rilis.rencana_belah([100, 100_000, 100], batas=6 * REKAM)
    assert [len(b) for b in bagian] == [1, 1, 1]


def test_rencana_belah_menolak_batas_mustahil():
    with pytest.raises(ValueError):
        rilis.rencana_belah([1], batas=512)
    with pytest.raises(ValueError):
        rilis.rencana_belah([1], batas=REKAM + MARGIN - 1)


def _buat(tmp_path, nama, byte_isi):
    jalur = tmp_path / nama
    jalur.parent.mkdir(parents=True, exist_ok=True)
    jalur.write_bytes(b"x" * byte_isi)
    return nama


def test_pengemas_membelah_menghapus_sumber_dan_menulis_sums(tmp_path):
    nama = [
        _buat(tmp_path, f"data/parquet/AUSDT/A-1m-2025-{i:02d}.parquet", 9_000)
        for i in range(1, 9)
    ]
    kemas = rilis.PengemasBerbelah(
        akar=str(tmp_path), nama_dasar="pecahan_9", batas=8 * REKAM
    )
    for n in nama:
        assert kemas.tambah(n)["ditambahkan"] is True
    laporan = kemas.tutup()

    assert laporan["status"] == "TERKEMAS"
    assert laporan["cacah_berkas"] == 8
    assert laporan["cacah_bagian"] > 1
    assert laporan["cacah_bagian_melebihi_batas"] == 0
    assert laporan["cacah_bagian_taksiran_terlampaui"] == 0
    assert laporan["cacah_berkas_melebihi_batas"] == 0
    assert laporan["cacah_berkas_hilang"] == 0
    assert laporan["byte_anggota_total"] == 8 * 9_000
    assert sum(b["cacah_berkas"] for b in laporan["bagian"]) == 8
    for n in nama:
        assert not (tmp_path / n).exists()
    sums = tmp_path / "data/rilis/SHA256SUMS"
    assert sums.exists()
    assert len(sums.read_text(encoding="utf-8").strip().splitlines()) == laporan[
        "cacah_bagian"
    ]


def test_tar_nyata_tidak_pernah_melebihi_taksiran_dibulatkan(tmp_path):
    """Model wajib >= kenyataan, pada berbagai ukuran isi."""
    for i, isi in enumerate([1, 511, 512, 513, 4_096, 20_000]):
        _buat(tmp_path, f"data/parquet/BUSDT/B-{i}.parquet", isi)
    kemas = rilis.PengemasBerbelah(
        akar=str(tmp_path), nama_dasar="p_taksir", batas=6 * REKAM
    )
    for i in range(6):
        kemas.tambah(f"data/parquet/BUSDT/B-{i}.parquet")
    laporan = kemas.tutup()

    assert laporan["cacah_berkas"] == 6
    for b in laporan["bagian"]:
        assert b["byte"] <= b["byte_taksir_dibulatkan"]
        assert b["byte"] % REKAM == 0
        assert b["byte"] <= laporan["batas_byte"]
    assert laporan["cacah_bagian_taksiran_terlampaui"] == 0
    assert laporan["cacah_bagian_melebihi_batas"] == 0


def test_taksiran_tahan_pada_banyak_anggota(tmp_path):
    """Aturan 43: galat per anggota wajib diuji pada cacah anggota yang besar.

    120 anggota × 1.024 byte pax = 122.880 byte, jauh melampaui margin 20.480.
    Dengan model lama (kepala satu blok) uji ini gagal telak; dengan enam anggota
    ia lolos meski modelnya cacat — persis cara cacat pax lolos ke produksi.
    """
    for i in range(120):
        _buat(tmp_path, f"data/parquet/CUSDT/C-{i:03d}.parquet", 100)
    kemas = rilis.PengemasBerbelah(akar=str(tmp_path), nama_dasar="p_banyak")
    for i in range(120):
        kemas.tambah(f"data/parquet/CUSDT/C-{i:03d}.parquet")
    laporan = kemas.tutup()

    assert laporan["cacah_berkas"] == 120
    assert laporan["cacah_bagian"] == 1
    bagian = laporan["bagian"][0]
    assert bagian["cacah_berkas"] == 120
    assert bagian["byte"] <= bagian["byte_taksir_dibulatkan"]
    # rapat, bukan sekadar longgar: sisa di luar margin < satu rekam
    assert bagian["byte_taksir_dibulatkan"] - MARGIN - bagian["byte"] < REKAM
    assert laporan["cacah_bagian_taksiran_terlampaui"] == 0


def test_pengemas_memulihkan_jalur_asli(tmp_path):
    n = _buat(tmp_path, "data/parquet/u4E2DUSDT/x-1m-2024-01.parquet", 64)
    kemas = rilis.PengemasBerbelah(akar=str(tmp_path), nama_dasar="p0")
    kemas.tambah(n)
    laporan = kemas.tutup()
    jalur = tmp_path / laporan["bagian"][0]["jalur"]
    with tarfile.open(jalur, "r") as tar:
        assert [m.name for m in tar.getmembers()] == [n]


def test_pengemas_menolak_batas_mustahil(tmp_path):
    with pytest.raises(ValueError):
        rilis.PengemasBerbelah(akar=str(tmp_path), batas=REKAM)


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
    kemas = rilis.PengemasBerbelah(
        akar=str(tmp_path), nama_dasar="p1", batas=4 * REKAM
    )
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


def test_verifikasi_gugur_saat_taksiran_terlampaui(tmp_path):
    """Medan penggugur wajib MEMBATALKAN kesahihan, bukan sekadar dicatat."""
    _buat(tmp_path, "data/parquet/AUSDT/A-1m-2025-01.parquet", 100)
    kemas = rilis.PengemasBerbelah(akar=str(tmp_path), nama_dasar="p3")
    kemas.tambah("data/parquet/AUSDT/A-1m-2025-01.parquet")
    laporan = kemas.tutup()
    assert rilis.verifikasi(str(tmp_path), laporan)["sah"] is True
    laporan["cacah_bagian_taksiran_terlampaui"] = 1
    assert rilis.verifikasi(str(tmp_path), laporan)["sah"] is False


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
