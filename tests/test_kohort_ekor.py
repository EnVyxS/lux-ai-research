"""Uji modul kohort_ekor tanpa jaringan sama sekali.

Lima belas fungsi uji, TANPA `parametrize`, sehingga cacah fungsi sama dengan
cacah butir pytest (aturan 47). Cacahnya dihitung dengan menyebut satu per satu,
bukan ditaksir dengan menatap: (1) sidik_kode, (2) header, (3) indeks_kolom,
(4) baris_cacat, (5) ringkas_lilin, (6) bagian, (7) mundur_bulan,
(8) penggugur_kendali, (9) parser_terbukti, (10) kendali_hidup, (11) riwayat,
(12) jendela_dan_peran, (13) muat_kohort, (14) pindai_adaptif_berhenti,
(15) pindai_adaptif_pagu_lawan_arsip.
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


def _baris(bulan: str, bagian_nol: float, transaksi: int) -> dict:
    return {
        "bulan": bulan,
        "bagian_volume_nol": bagian_nol,
        "transaksi_total": transaksi,
    }


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
    assert kohort_ekor.sidik_kode() != sidik(["kohort_ekor.py", "arsip.py"])


def test_baca_zip_klines_mengenali_header_dari_isi():
    tanpa = _zip_klines(
        "X-1m-2026-06.csv", [_lilin(1750000000000, "1.5", "7"), _lilin(1750000060000, "0", "0")]
    )
    hasil = kohort_ekor.baca_zip_klines(tanpa)
    assert hasil["berheader"] is False
    assert hasil["kepala"] is None
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
    assert hasil2["kepala"][kohort_ekor.IDX_VOLUME] == "volume"
    assert hasil2["kepala"][kohort_ekor.IDX_TRANSAKSI] == "count"


def test_kolom_volume_dan_transaksi_terbaca_dari_posisi_yang_benar():
    """Penjaga langsung atas kekeliruan yang paling mungkin: salah indeks kolom."""
    data = _zip_klines("X-1m-2026-06.csv", [_lilin(1750000000000, "12.5", "9")])
    hasil = kohort_ekor.baca_zip_klines(data)
    assert hasil["volume"] == [12.5]
    assert hasil["transaksi"] == [9]


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
        {"peran": "uji", "bulan": "2026-06", "bagian_volume_nol": 1.0, "lolos_gerbang": True},
        {"peran": "uji", "bulan": "2026-05", "bagian_volume_nol": 0.1, "lolos_gerbang": True},
        {"peran": "kendali", "bulan": "2025-06", "galat": "putus", "gagal_unduh": True},
    ]
    r = kohort_ekor.ringkas(baris)
    assert r["cacah_uji_diminta"] == 2
    assert r["cacah_uji_sepi"] == 1
    assert r["cacah_uji_bulan_bukan_diharapkan"] == 1
    assert r["cacah_gagal_unduh"] == 1
    assert r["kendali_sah"] is False
    baik = kohort_ekor.ringkas(
        baris[:1] + [{"peran": "kendali", "bulan": "2025-06", "bagian_volume_nol": 1.0}]
    )
    assert baik["kendali_sah"] is True
    assert baik["cacah_kendali_sepi"] == 1


def test_parser_terbukti_gugur_saat_kendali_hidup_ikut_kosong():
    """Bila simbol yang pasti hidup terbaca kosong, yang cacat adalah kode."""
    kosong = [
        {"peran": "kendali_hidup", "bagian_volume_nol": 1.0, "transaksi_total": 0},
        {"peran": "kendali_hidup", "bagian_volume_nol": 0.02, "transaksi_total": 900},
    ]
    assert kohort_ekor.ringkas(kosong)["parser_terbukti"] is False

    ramai = [
        {"peran": "kendali_hidup", "bagian_volume_nol": 0.01, "transaksi_total": 1000},
        {"peran": "kendali_hidup", "bagian_volume_nol": 0.02, "transaksi_total": 900},
    ]
    hasil = kohort_ekor.ringkas(ramai)
    assert hasil["parser_terbukti"] is True
    assert hasil["cacah_kendali_hidup_ramai"] == 2
    assert kohort_ekor.ringkas([])["parser_terbukti"] is False


def test_baris_kendali_hidup_memasangkan_simbol_dengan_kedua_bulan():
    dipanggil = []

    def palsu(simbol, bulan, peran):
        dipanggil.append((simbol, bulan, peran))
        return {"simbol": simbol, "bulan": bulan, "peran": peran}

    hasil = kohort_ekor.baris_kendali_hidup("2026-06", "2025-06", ukur=palsu)
    assert len(hasil) == 2 * len(kohort_ekor.KENDALI_HIDUP)
    assert all(b["peran"] == "kendali_hidup" for b in hasil)
    assert ("BTCUSDT", "2026-06", "kendali_hidup") in dipanggil
    assert ("BTCUSDT", "2025-06", "kendali_hidup") in dipanggil
    hanya_satu = kohort_ekor.baris_kendali_hidup("2026-06", None, ukur=palsu)
    assert len(hanya_satu) == len(kohort_ekor.KENDALI_HIDUP)


def test_nilai_riwayat_membedakan_mati_kebangkitan_dan_tak_terukur():
    """Tiga keadaan yang mudah tertukar bila hanya dilihat sekilas."""
    mati = kohort_ekor.nilai_riwayat(
        "AAA",
        [
            _baris("2025-04", 0.02, 500),
            _baris("2025-05", 1.0, 0),
            _baris("2026-06", 1.0, 0),
        ],
    )
    assert mati["bulan_hidup_terakhir"] == "2025-04"
    assert mati["bulan_sepi_paling_awal"] == "2025-05"
    assert mati["cacah_bulan_ramai"] == 1
    assert mati["cacah_bulan_sepi"] == 2
    assert mati["bangkit_kembali"] is False
    assert mati["batas_tercapai"] is False
    assert mati["hidup_terakhir_sebelum_tebing"] is True

    bangkit = kohort_ekor.nilai_riwayat(
        "BBB", [_baris("2025-05", 1.0, 0), _baris("2025-09", 0.01, 900)]
    )
    assert bangkit["bangkit_kembali"] is True
    assert bangkit["bangkit_dapat_diuji"] is True
    assert bangkit["bulan_hidup_terakhir"] == "2025-09"
    assert bangkit["hidup_terakhir_sebelum_tebing"] is False

    # seluruh rentang sepi: TAK TERUKUR, bukan "tidak pernah hidup" (aturan 41)
    buta = kohort_ekor.nilai_riwayat("CCC", [_baris("2026-05", 1.0, 0), _baris("2026-06", 1.0, 0)])
    assert buta["batas_tercapai"] is True
    assert buta["bulan_hidup_terakhir"] is None
    assert buta["hidup_terakhir_sebelum_tebing"] is None

    # baris bergalat tidak boleh ikut dihitung sebagai bulan sepi
    bergalat = kohort_ekor.nilai_riwayat(
        "DDD", [{"bulan": "2026-06", "galat": "putus"}, _baris("2026-05", 0.01, 10)]
    )
    assert bergalat["cacah_bulan_dipindai"] == 1
    assert bergalat["bulan_hidup_terakhir"] == "2026-05"


def test_jendela_bulan_dan_peran_bulan():
    tersedia = ["2025-03", "2025-04", "2025-05", "2025-06", "2025-07"]
    assert kohort_ekor.jendela_bulan(tersedia, 3) == ["2025-05", "2025-06", "2025-07"]
    assert kohort_ekor.jendela_bulan(tersedia, 99) == tersedia
    assert kohort_ekor.jendela_bulan([], 3) == []
    # urutan masukan tidak boleh menentukan isi jendela
    assert kohort_ekor.jendela_bulan(list(reversed(tersedia)), 2) == ["2025-06", "2025-07"]

    assert kohort_ekor.peran_bulan("2026-06", "2026-06", "2025-06") == "uji"
    assert kohort_ekor.peran_bulan("2025-06", "2026-06", "2025-06") == "kendali"
    assert kohort_ekor.peran_bulan("2025-11", "2026-06", "2025-06") == "pindai"
    assert kohort_ekor.peran_bulan("2025-06", "2026-06", None) == "pindai"


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


def test_pindai_adaptif_berhenti_pada_bulan_ramai_pertama():
    """Aturan 51: jendela adaptif berhenti pada peristiwanya, bukan pada angka tetap."""
    dipanggil = []

    def palsu(simbol, bulan, peran):
        dipanggil.append(bulan)
        hidup = bulan == "2024-03"
        return {
            "simbol": simbol,
            "bulan": bulan,
            "peran": peran,
            "bagian_volume_nol": 0.01 if hidup else 1.0,
            "transaksi_total": 900 if hidup else 0,
        }

    tersedia = ["2024-01", "2024-02", "2024-03", "2024-04", "2024-05"]
    hasil = kohort_ekor.pindai_adaptif("AAA", tersedia, None, ukur=palsu)
    # mundur dari yang terbaru, lalu BERHENTI; dua bulan tertua tak pernah diunduh
    assert dipanggil == ["2024-05", "2024-04", "2024-03"]
    assert hasil["cacah_bulan_diunduh"] == 3
    assert hasil["cacah_bulan_tersedia"] == 5
    # keluaran tetap urut menaik walau pindaiannya mundur
    assert [b["bulan"] for b in hasil["baris"]] == ["2024-03", "2024-04", "2024-05"]
    assert hasil["bulan_terakhir"] == "2024-05"
    assert hasil["pagu_habis"] is False
    assert hasil["arsip_habis"] is False

    riwayat = kohort_ekor.nilai_riwayat("AAA", hasil["baris"], hasil)
    assert riwayat["bulan_hidup_terakhir"] == "2024-03"
    assert riwayat["batas_tercapai"] is False
    assert riwayat["hidup_terakhir_sebelum_tebing"] is True
    # kejujuran rancangan: kebangkitan TIDAK dapat digugurkan oleh mode ini
    assert riwayat["bangkit_dapat_diuji"] is False
    assert kohort_ekor.ringkas(hasil["baris"], [riwayat])[
        "cacah_simbol_bangkit_dapat_diuji"
    ] == 0


def test_pindai_adaptif_membedakan_pagu_habis_dari_arsip_habis():
    """Dua sebab berbeda di balik satu batas_tercapai (aturan 46)."""

    def sepi_selalu(simbol, bulan, peran):
        return {
            "simbol": simbol,
            "bulan": bulan,
            "peran": peran,
            "bagian_volume_nol": 1.0,
            "transaksi_total": 0,
        }

    tersedia = ["2024-01", "2024-02", "2024-03", "2024-04"]
    kena_pagu = kohort_ekor.pindai_adaptif("BBB", tersedia, None, ukur=sepi_selalu, pagu=2)
    assert [b["bulan"] for b in kena_pagu["baris"]] == ["2024-03", "2024-04"]
    assert kena_pagu["pagu_habis"] is True
    assert kena_pagu["arsip_habis"] is False

    habis = kohort_ekor.pindai_adaptif("CCC", tersedia, None, ukur=sepi_selalu, pagu=60)
    assert habis["cacah_bulan_diunduh"] == 4
    assert habis["pagu_habis"] is False
    assert habis["arsip_habis"] is True

    kosong = kohort_ekor.pindai_adaptif("DDD", [], None, ukur=sepi_selalu, pagu=60)
    assert kosong["baris"] == []
    assert kosong["bulan_terakhir"] is None
    assert kosong["arsip_habis"] is True

    riwayat = [
        kohort_ekor.nilai_riwayat("BBB", kena_pagu["baris"], kena_pagu),
        kohort_ekor.nilai_riwayat("CCC", habis["baris"], habis),
    ]
    assert all(r["batas_tercapai"] for r in riwayat)
    assert all(r["bulan_hidup_terakhir"] is None for r in riwayat)
    r = kohort_ekor.ringkas(kena_pagu["baris"] + habis["baris"], riwayat)
    assert r["cacah_simbol_batas_tercapai"] == 2
    assert r["cacah_simbol_pagu_habis"] == 1
    assert r["cacah_simbol_arsip_habis"] == 1
    assert r["cacah_bulan_diunduh"] == 6
