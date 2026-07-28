"""Uji regresi `lux_ai.serapan.pulihkan`.

Delapan uji, semuanya memakai parquet nyata (pyarrow) dan tar nyata yang dikemas
oleh `rilis.PengemasBerbelah` — bukan tar sintetis buatan uji — supaya jalur yang
diuji adalah jalur produksi.

Dua uji sengaja MERUSAK aset: satu byte diubah, satu bagian dihapus. Uji yang
hanya menunjukkan jalur bahagia tidak membuktikan medan penggugurnya menyala
(aturan 24).
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq
import pytest

from lux_ai.serapan import pulihkan, rilis

INDEKS_UJI = 9
RUN_UJI = "11112222"


def _tulis_parquet(jalur: Path, baris: int) -> None:
    jalur.parent.mkdir(parents=True, exist_ok=True)
    tabel = pa.table({"waktu": list(range(baris)), "harga": [1.0] * baris})
    pq.write_table(tabel, str(jalur))


def _siapkan(
    tmp_path: Path, cacah: int = 40, baris: int = 7, cacah_karantina: int = 0
) -> dict:
    """Bangun parquet, kemas dengan pengemas produksi, tulis manifes + status."""
    akar = tmp_path
    baris_utama = 0
    pengemas = rilis.PengemasBerbelah(
        akar=str(akar), nama_dasar=f"pecahan_{INDEKS_UJI}"
    )
    for i in range(cacah):
        rel = f"data/parquet/SIM{i:03d}/SIM{i:03d}-1m-2025-01.parquet"
        _tulis_parquet(akar / rel, baris)
        baris_utama += baris
        pengemas.tambah(rel)
    laporan_utama = pengemas.tutup()

    laporan_kar = None
    baris_kar = 0
    if cacah_karantina:
        pengemas_kar = rilis.PengemasBerbelah(
            akar=str(akar),
            nama_dasar=f"pecahan_{INDEKS_UJI}_karantina",
            nama_sums=rilis.NAMA_SUMS_KARANTINA,
        )
        for i in range(cacah_karantina):
            rel = f"data/parquet_karantina/KAR{i:03d}/KAR{i:03d}-1m-2025-02.parquet"
            _tulis_parquet(akar / rel, baris + 1)
            baris_kar += baris + 1
            pengemas_kar.tambah(rel)
        laporan_kar = pengemas_kar.tutup()

    manifes = {
        "jumlah_baris": baris_utama,
        "rilis": laporan_utama,
        "rilis_karantina": laporan_kar,
        "sidik_kode": "kode-uji",
    }
    (akar / "reports").mkdir(parents=True, exist_ok=True)
    (akar / pulihkan.nama_manifes(INDEKS_UJI)).write_text(
        json.dumps(manifes), encoding="utf-8"
    )
    (akar / pulihkan.nama_status_serapan(INDEKS_UJI)).write_text(
        json.dumps({"run_id": RUN_UJI, "indeks": str(INDEKS_UJI)}), encoding="utf-8"
    )

    # Tirukan `gh release download`: aset pindah ke direktori unduhan.
    unduh = akar / pulihkan.AKAR_UNDUH
    unduh.mkdir(parents=True, exist_ok=True)
    for tar in sorted((akar / rilis.AKAR_RILIS).glob("*.tar")):
        shutil.move(str(tar), str(unduh / tar.name))

    return {
        "akar": akar,
        "unduh": unduh,
        "baris_utama": baris_utama,
        "baris_karantina": baris_kar,
        "cacah": cacah,
        "cacah_karantina": cacah_karantina,
    }


def test_sidik_kode_heksadesimal_dan_stabil():
    a = pulihkan.sidik_kode()
    assert a == pulihkan.sidik_kode()
    assert len(a) == 64
    int(a, 16)


def test_nama_tag_dan_keluaran_mengikuti_pola_rilis():
    assert pulihkan.nama_tag(3, "30396803601") == "serapan-pecahan-3-30396803601"
    assert pulihkan.nama_keluaran(3) == "reports/pulihkan_pecahan_3.json"
    assert pulihkan.nama_manifes(3) == "reports/manifes_pecahan_3.json"


@pytest.mark.parametrize(
    "nama, aman",
    [
        ("data/parquet/BTCUSDT/x.parquet", True),
        ("/etc/passwd", False),
        ("../../keluar.parquet", False),
        ("data/../data/x.parquet", False),
    ],
)
def test_anggota_aman_menolak_jalur_berbahaya(nama, aman):
    assert pulihkan.anggota_aman(nama) is aman


def test_alur_penuh_sah_dan_baris_cocok(tmp_path):
    s = _siapkan(tmp_path, cacah=40, baris=7)
    hasil = pulihkan.jalankan(INDEKS_UJI, akar=str(s["akar"]))
    assert hasil["pulih_sah"] is True
    assert hasil["utama"]["cacah_sha_tak_cocok"] == 0
    assert hasil["utama"]["cacah_bagian_hilang"] == 0
    assert hasil["utama"]["cacah_anggota_terbaca"] == 40
    assert hasil["utama"]["cacah_anggota_kurang"] == 0
    assert hasil["utama"]["cacah_anggota_tak_aman"] == 0
    assert hasil["baris_utama"] == s["baris_utama"]
    assert hasil["selisih_baris_utama"] == 0
    assert hasil["baris_terverifikasi"] is True
    assert hasil["run_id_sumber"] == RUN_UJI
    # Cakram dibersihkan: tar dan hasil bongkar tidak boleh tertinggal.
    assert not list((s["unduh"]).glob("*.tar"))


def test_satu_byte_berubah_menggugurkan(tmp_path):
    s = _siapkan(tmp_path, cacah=12, baris=5)
    tar = sorted(s["unduh"].glob("*.tar"))[0]
    isi = bytearray(tar.read_bytes())
    isi[len(isi) // 2] ^= 0xFF
    tar.write_bytes(bytes(isi))
    hasil = pulihkan.jalankan(INDEKS_UJI, akar=str(s["akar"]))
    assert hasil["utama"]["cacah_sha_tak_cocok"] == 1
    assert hasil["pulih_sah"] is False


def test_bagian_hilang_menggugurkan(tmp_path):
    s = _siapkan(tmp_path, cacah=12, baris=5)
    sorted(s["unduh"].glob("*.tar"))[0].unlink()
    hasil = pulihkan.jalankan(INDEKS_UJI, akar=str(s["akar"]))
    assert hasil["utama"]["cacah_bagian_hilang"] == 1
    assert hasil["utama"]["cacah_anggota_kurang"] > 0
    assert hasil["pulih_sah"] is False


def test_selisih_baris_tidak_membatalkan_keutuhan(tmp_path):
    """Pertanyaan definisi dan pertanyaan keutuhan wajib terpisah."""
    s = _siapkan(tmp_path, cacah=10, baris=6)
    jalur = s["akar"] / pulihkan.nama_manifes(INDEKS_UJI)
    manifes = json.loads(jalur.read_text(encoding="utf-8"))
    manifes["jumlah_baris"] = int(manifes["jumlah_baris"]) + 13
    jalur.write_text(json.dumps(manifes), encoding="utf-8")
    hasil = pulihkan.jalankan(INDEKS_UJI, akar=str(s["akar"]))
    assert hasil["pulih_sah"] is True
    assert hasil["selisih_baris_utama"] == -13
    assert hasil["baris_terverifikasi"] is False
    assert hasil["definisi_jumlah_baris"] == "tidak ada definisi yang cocok"


def test_karantina_dihitung_terpisah(tmp_path):
    s = _siapkan(tmp_path, cacah=8, baris=4, cacah_karantina=3)
    hasil = pulihkan.jalankan(INDEKS_UJI, akar=str(s["akar"]))
    assert hasil["pulih_sah"] is True
    assert hasil["karantina"]["cacah_anggota_terbaca"] == 3
    assert hasil["karantina"]["cacah_sha_tak_cocok"] == 0
    assert hasil["baris_karantina"] == s["baris_karantina"]
    assert hasil["baris_total"] == s["baris_utama"] + s["baris_karantina"]
    assert hasil["selisih_baris_utama"] == 0
