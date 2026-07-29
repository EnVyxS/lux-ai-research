"""Uji `kehidupan_arsip`: fungsi murni, plus dua parquet nyata di tmp_path.

Tidak ada uji yang menyentuh jaringan atau aset rilis. Yang diuji di sini adalah
pengurai, pemilih kendali, penyebut ganda, dan kode keluar — bagian yang bila
salah akan membuat laporan run terbaca meyakinkan namun keliru.

## Perbaikan sesudah run `30419770312` (291 butir, 1 gagal)

`test_ukur_kolom_menghitung_transaksi_dan_nol` menuntut `bagian_volume_nol`
sama dengan 2/3 penuh, padahal `kohort_ekor.bagian` MEMBULATKAN ke empat
desimal dan mengembalikan 0,6667. Yang salah adalah harapan uji, bukan modul:
pembulatan itu sudah dipakai seluruh papan kehidupan sejak kohort puncak, dan
mengubahnya sekarang akan mengubah angka yang sudah diterbitkan (aturan 29).
Harapan uji karena itu diberi toleransi yang sesuai, dan pembulatannya diuji
secara tersurat di dalam fungsi yang sama agar tidak diam-diam hilang.

Saya seharusnya membaca `kohort_ekor.bagian` sebelum meramalkan kode keluar 0;
ini kegagalan membaca, bukan kegagalan rancangan.

## Praregistrasi ramalan — ditulis SEBELUM run

- **R-208** — CI pada commit ini mengumpulkan **291 butir** dengan kode keluar
  **0**. Cacahnya tidak berubah sebab tidak ada fungsi uji baru yang
  ditambahkan; hanya harapan di dalam satu fungsi yang diperbaiki. Satuan:
  BUTIR yang dikumpulkan pytest.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from lux_ai.serapan import kehidupan, kehidupan_arsip as ka


def _manifes(baris):
    return {"manifes": baris}


def test_peta_parquet_memetakan_jalur():
    peta = ka.peta_parquet(
        _manifes(
            [
                {
                    "simbol": "BTCUSDT",
                    "bulan": "2024-01",
                    "parquet": "data/parquet/BTCUSDT/BTCUSDT-1m-2024-01.parquet",
                    "byte_parquet": 99,
                    "gerbang_lolos": True,
                    "baris": 44640,
                }
            ]
        )
    )
    kunci = "data/parquet/BTCUSDT/BTCUSDT-1m-2024-01.parquet"
    assert peta[kunci]["simbol"] == "BTCUSDT"
    assert peta[kunci]["bulan"] == "2024-01"
    assert peta[kunci]["byte_parquet"] == 99


def test_peta_parquet_melewati_baris_tanpa_parquet():
    peta = ka.peta_parquet(
        _manifes(
            [
                {"simbol": "X", "bulan": "2024-01", "parquet": None},
                {
                    "simbol": "Y",
                    "bulan": "2024-02",
                    "parquet": None,
                    "parquet_karantina": "data/parquet_karantina/Y/Y-1m-2024-02.parquet",
                },
            ]
        )
    )
    assert peta == {}


def test_ukur_kolom_menghitung_transaksi_dan_nol():
    hasil = ka.ukur_kolom(["0.0", "1.5", "0"], ["0", "7", "0"])
    assert hasil["cacah_lilin"] == 3
    assert hasil["transaksi_total"] == 7
    assert hasil["cacah_volume_nol"] == 2
    # kohort_ekor.bagian membulatkan ke empat desimal: 2/3 menjadi 0,6667.
    assert hasil["bagian_volume_nol"] == 0.6667
    assert hasil["bagian_volume_nol"] == pytest.approx(2 / 3, abs=1e-4)


def test_ukur_kolom_menandai_baris_cacat():
    hasil = ka.ukur_kolom(["1.0", "bukan angka"], ["3", "4"])
    assert hasil["cacah_baris_cacat"] == 1
    assert hasil["cacah_lilin_terbaca"] == 1
    assert hasil["transaksi_total"] == 3


def test_ukur_kolom_tanpa_baris_terbaca_menolak_menyimpulkan():
    hasil = ka.ukur_kolom(["", None], ["", None])
    assert hasil["transaksi_total"] is None
    assert hasil["cacah_lilin_terbaca"] == 0
    assert kehidupan.klasifikasi(dict(hasil, ada_di_arsip=True)) == kehidupan.STATUS_TAK_TERUKUR


@pytest.mark.parametrize(
    "volume,transaksi,harapan",
    [
        (["0", "0"], ["0", "0"], kehidupan.STATUS_MATI),
        (["0", "0", "1", "2"], ["0", "0", "1", "2"], kehidupan.STATUS_SEPI),
        (["1", "2", "3", "0"], ["5", "6", "7", "0"], kehidupan.STATUS_HIDUP),
        ([], [], kehidupan.STATUS_TAK_TERUKUR),
    ],
)
def test_status_dari_ukuran(volume, transaksi, harapan):
    info = {"simbol": "S", "bulan": "2024-01", "jalur": "j", "byte_parquet": 1}
    baris = ka.baris_kehidupan(info, ka.ukur_kolom(volume, transaksi))
    assert baris["status"] == harapan


def test_kendali_dipilih_dari_parquet_terbesar():
    peta = {
        "a": {"simbol": "A", "bulan": "2024-01", "byte_parquet": 10},
        "b": {"simbol": "B", "bulan": "2024-01", "byte_parquet": 900},
        "c": {"simbol": "C", "bulan": "2024-01", "byte_parquet": 500},
        "d": {"simbol": "D", "bulan": "2024-01", "byte_parquet": 1},
    }
    assert ka.kendali_pecahan(peta) == [
        ("B", "2024-01"),
        ("C", "2024-01"),
        ("A", "2024-01"),
    ]


def test_kendali_urutan_stabil_saat_byte_sama():
    peta = {
        "x": {"simbol": "Z", "bulan": "2024-01", "byte_parquet": 5},
        "y": {"simbol": "A", "bulan": "2024-02", "byte_parquet": 5},
    }
    assert ka.kendali_pecahan(peta, cacah=2) == [("A", "2024-02"), ("Z", "2024-01")]


def _baris(simbol, bulan, status, lilin=10, lolos=True):
    return {
        "simbol": simbol,
        "bulan": bulan,
        "status": status,
        "cacah_lilin": lilin,
        "gerbang_lolos": lolos,
        "cacah_baris_cacat": 0,
    }


def test_ringkas_menerbitkan_penyebut_ganda():
    baris = [
        _baris("A", "2024-01", kehidupan.STATUS_MATI),
        _baris("B", "2024-01", kehidupan.STATUS_HIDUP),
    ]
    r = ka.ringkas_pecahan(baris, [("B", "2024-01")], {"cacah_parquet_diminta": 2})
    assert r["penyebut_penuh"] == 2
    assert r["penyebut_tanpa_mati"] == 1
    assert r["cacah_mati"] == 1
    assert r["cacah_mati_lolos_gerbang"] == 1
    assert r["parser_terbukti"] is True


def test_ringkas_penyebut_tanpa_mati_kosong():
    baris = [_baris("A", "2024-01", kehidupan.STATUS_MATI)]
    r = ka.ringkas_pecahan(baris, [("A", "2024-01")], {})
    assert r["penyebut_tanpa_mati"] == 0
    assert r["penyebut_tanpa_mati_kosong"] is True


def test_parser_terbukti_false_bila_satu_kendali_tidak_hidup():
    baris = [
        _baris("A", "2024-01", kehidupan.STATUS_HIDUP),
        _baris("B", "2024-01", kehidupan.STATUS_MATI),
    ]
    r = ka.ringkas_pecahan(baris, [("A", "2024-01"), ("B", "2024-01")], {})
    assert r["cacah_kendali_hidup"] == 1
    assert r["parser_terbukti"] is False


def test_kode_keluar_dua_bila_parser_tak_terbukti():
    assert ka.kode_keluar({"parser_terbukti": False}) == 2


def test_kode_keluar_dua_bila_sha_tak_cocok():
    assert ka.kode_keluar({"parser_terbukti": True, "cacah_sha_tak_cocok": 1}) == 2


def test_kode_keluar_nol_saat_bersih():
    assert (
        ka.kode_keluar(
            {
                "parser_terbukti": True,
                "cacah_sha_tak_cocok": 0,
                "cacah_bagian_hilang": 0,
                "cacah_parquet_hilang": 0,
                "cacah_anggota_tak_aman": 0,
            }
        )
        == 0
    )


def test_nama_keluaran_sesuai_indeks():
    assert ka.nama_keluaran(5) == "reports/kehidupan_arsip_5.json"
    assert ka.nama_ringkas(5) == "reports/kehidupan_arsip_5_ringkas.json"


def test_sidik_kode_heks_64():
    sidik = ka.sidik_kode()
    assert len(sidik) == 64
    assert sidik == ka.sidik_kode()


def test_anggota_parquet_tak_aman_ditolak():
    from lux_ai.serapan import pulihkan

    assert pulihkan.anggota_aman("data/parquet/A/A-1m-2024-01.parquet") is True
    assert pulihkan.anggota_aman("../luar.parquet") is False


def _tulis_parquet(tujuan: Path, kolom):
    import pandas as pd

    tujuan.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(kolom).to_parquet(tujuan, engine="pyarrow", index=False)


def test_ukur_parquet_membaca_berkas_nyata(tmp_path):
    jalur = tmp_path / "a.parquet"
    _tulis_parquet(
        jalur,
        {"open_time": ["1", "2", "3"], "volume": ["0", "0", "4.5"], "trades": ["0", "0", "9"]},
    )
    hasil = ka.ukur_parquet(jalur)
    assert hasil["cacah_lilin"] == 3
    assert hasil["transaksi_total"] == 9
    assert hasil["cacah_volume_nol"] == 2
    assert hasil["galat"] is None


def test_ukur_parquet_kolom_hilang_menghasilkan_galat(tmp_path):
    jalur = tmp_path / "b.parquet"
    _tulis_parquet(jalur, {"open_time": ["1", "2"], "volume": ["1", "2"]})
    hasil = ka.ukur_parquet(jalur)
    assert hasil["transaksi_total"] is None
    assert "trades" in str(hasil["galat"])
