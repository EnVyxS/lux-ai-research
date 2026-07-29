"""Uji regresi `lux_ai.serapan.pulihkan`.

Tiga belas fungsi uji, dihitung satu per satu: `sidik_kode_heksadesimal`,
`nama_tag_dan_keluaran`, `anggota_aman` (berparameter empat kasus),
`alur_penuh_sah`, `satu_byte_berubah`, `bagian_hilang`,
`selisih_baris_tidak_membatalkan_keutuhan`, `karantina_dihitung_terpisah`,
`definisi_tidak_dapat_dibedakan_tanpa_karantina`,
`definisi_lolos_saja_saat_karantina_ada`, `definisi_lolos_plus_karantina`,
`definisi_null_saat_jumlah_baris_manifes_hilang`, dan `putuskan_definisi_tabel`
(berparameter lima kasus). Butir yang dikumpulkan pytest: 20, bukan 13
(aturan 38).

Semuanya memakai parquet nyata (pyarrow) dan tar nyata yang dikemas oleh
`rilis.PengemasBerbelah` — bukan tar sintetis buatan uji — supaya jalur yang
diuji adalah jalur produksi.

Dua uji sengaja MERUSAK aset: satu byte diubah, satu bagian dihapus. Uji yang
hanya menunjukkan jalur bahagia tidak membuktikan medan penggugurnya menyala
(aturan 24).

Empat uji terakhir menegakkan aturan 46: kode dilarang menyebut salah satu
definisi `jumlah_baris` ketika kasusnya tidak mampu membedakan keduanya.
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


def _tulis_jumlah_baris(akar: Path, nilai) -> None:
    """Ganti `jumlah_baris` di manifes uji; `None` berarti medannya dihapus."""
    jalur = akar / pulihkan.nama_manifes(INDEKS_UJI)
    manifes = json.loads(jalur.read_text(encoding="utf-8"))
    if nilai is None:
        manifes.pop("jumlah_baris", None)
    else:
        manifes["jumlah_baris"] = int(nilai)
    jalur.write_text(json.dumps(manifes), encoding="utf-8")


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
    _tulis_jumlah_baris(s["akar"], s["baris_utama"] + 13)
    hasil = pulihkan.jalankan(INDEKS_UJI, akar=str(s["akar"]))
    assert hasil["pulih_sah"] is True
    assert hasil["selisih_baris_utama"] == -13
    assert hasil["baris_terverifikasi"] is False
    assert hasil["definisi_jumlah_baris"] == pulihkan.DEF_TAK_COCOK


def test_karantina_dihitung_terpisah(tmp_path):
    s = _siapkan(tmp_path, cacah=8, baris=4, cacah_karantina=3)
    hasil = pulihkan.jalankan(INDEKS_UJI, akar=str(s["akar"]))
    assert hasil["pulih_sah"] is True
    assert hasil["karantina"]["cacah_anggota_terbaca"] == 3
    assert hasil["karantina"]["cacah_sha_tak_cocok"] == 0
    assert hasil["baris_karantina"] == s["baris_karantina"]
    assert hasil["baris_total"] == s["baris_utama"] + s["baris_karantina"]
    assert hasil["selisih_baris_utama"] == 0


def test_definisi_tidak_dapat_dibedakan_tanpa_karantina(tmp_path):
    """Aturan 46: inilah cacat VERSI 1 pada pecahan 2 dan 5."""
    s = _siapkan(tmp_path, cacah=6, baris=5, cacah_karantina=0)
    hasil = pulihkan.jalankan(INDEKS_UJI, akar=str(s["akar"]))
    assert hasil["baris_karantina"] == 0
    assert hasil["selisih_baris_utama"] == 0
    assert hasil["selisih_baris_total"] == 0
    assert hasil["definisi_dapat_dibedakan"] is False
    assert hasil["definisi_jumlah_baris"] == pulihkan.DEF_TAK_TERBEDAKAN
    assert hasil["baris_terverifikasi"] is True


def test_definisi_lolos_saja_saat_karantina_ada(tmp_path):
    s = _siapkan(tmp_path, cacah=6, baris=5, cacah_karantina=2)
    hasil = pulihkan.jalankan(INDEKS_UJI, akar=str(s["akar"]))
    assert hasil["baris_karantina"] > 0
    assert hasil["definisi_dapat_dibedakan"] is True
    assert hasil["definisi_jumlah_baris"] == pulihkan.DEF_LOLOS_SAJA


def test_definisi_lolos_plus_karantina(tmp_path):
    s = _siapkan(tmp_path, cacah=6, baris=5, cacah_karantina=2)
    _tulis_jumlah_baris(s["akar"], s["baris_utama"] + s["baris_karantina"])
    hasil = pulihkan.jalankan(INDEKS_UJI, akar=str(s["akar"]))
    assert hasil["selisih_baris_total"] == 0
    assert hasil["selisih_baris_utama"] != 0
    assert hasil["definisi_dapat_dibedakan"] is True
    assert hasil["definisi_jumlah_baris"] == pulihkan.DEF_LOLOS_PLUS_KARANTINA


def test_definisi_null_saat_jumlah_baris_manifes_hilang(tmp_path):
    s = _siapkan(tmp_path, cacah=5, baris=4, cacah_karantina=2)
    _tulis_jumlah_baris(s["akar"], None)
    hasil = pulihkan.jalankan(INDEKS_UJI, akar=str(s["akar"]))
    assert hasil["jumlah_baris_manifes"] is None
    assert hasil["selisih_baris_utama"] is None
    assert hasil["selisih_baris_total"] is None
    assert hasil["definisi_dapat_dibedakan"] is False
    assert hasil["definisi_jumlah_baris"] == pulihkan.DEF_TAK_ADA_MANIFES
    assert hasil["baris_terverifikasi"] is False
    assert hasil["pulih_sah"] is True


@pytest.mark.parametrize(
    "selisih_utama, selisih_total, baris_karantina, harap, dapat",
    [
        (None, None, 0, pulihkan.DEF_TAK_ADA_MANIFES, False),
        (0, 0, 0, pulihkan.DEF_TAK_TERBEDAKAN, False),
        (0, 9, 9, pulihkan.DEF_LOLOS_SAJA, True),
        (-9, 0, 9, pulihkan.DEF_LOLOS_PLUS_KARANTINA, True),
        (5, 14, 9, pulihkan.DEF_TAK_COCOK, True),
    ],
)
def test_putuskan_definisi_tabel(
    selisih_utama, selisih_total, baris_karantina, harap, dapat
):
    kesimpulan, dapat_dibedakan = pulihkan.putuskan_definisi(
        selisih_utama, selisih_total, baris_karantina
    )
    assert kesimpulan == harap
    assert dapat_dibedakan is dapat
