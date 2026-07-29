"""Uji `lubang_tengah` V2.

Aturan 57 (penangkal KC-19): nama setiap fungsi uji ditulis BERNOMOR di sini
SEBELUM cacahnya diramalkan. Tidak ada `parametrize` di berkas ini, sehingga
cacah fungsi sama dengan cacah butir pytest.

1. test_versi_dua
2. test_nama_keluaran_tetap
3. test_sidik_kode_hex_dan_stabil
4. test_sidik_kode_beda_dari_silang_funding
5. test_berkas_dicap_empat_nama
6. test_tengah_tercatat_enam
7. test_simbol_h_a010_lima_nama
8. test_medan_per_simbol_melaporkan_nama_medan
9. test_medan_per_simbol_kosong_aman
10. test_bulan_berfunding_membuang_lubang
11. test_bulan_berfunding_urut
12. test_bulan_berfunding_kosong_bila_semua_lubang
13. test_tetangga_berfunding_mengapit_lubang
14. test_tetangga_berfunding_null_di_ujung
15. test_panjang_rentetan_lubang_berurutan
16. test_panjang_rentetan_nol_bila_bukan_lubang
17. test_daftar_lubang_tengah_hanya_bentuk_tengah
18. test_daftar_lubang_tengah_urut
19. test_daftar_lubang_tengah_memuat_tetangga
20. test_daftar_lubang_tengah_memuat_panjang_rentetan
21. test_daftar_lubang_tengah_lilin_null_bila_tak_ada
22. test_daftar_lubang_tengah_byte_parquet_nol_bila_tak_ada
23. test_daftar_lubang_tengah_abai_lubang_luar_penyebut
24. test_daftar_lubang_tengah_memuat_cacah_bulan_dan_lubang
25. test_sebaran_status_mencacah_empat_status
26. test_sebaran_status_kosong_nol
27. test_uji_h_a010_menang_bila_funding_menyusul
28. test_uji_h_a010_gugur_bila_funding_lebih_dulu
29. test_uji_h_a010_simbol_tak_dikenal_tak_terukur
30. test_uji_h_a010_menang_wajib_semua_simbol
31. test_uji_h_a010_cacah_konsisten
32. test_kode_keluar_nol_pada_ringkasan_sehat
33. test_kode_keluar_dua_bila_sidik_tak_seragam
34. test_kode_keluar_dua_bila_laporan_kurang
35. test_kode_keluar_dua_bila_selisih_tengah_bukan_nol
36. test_kode_keluar_dua_bila_kendali_tak_sah
37. test_kode_keluar_dua_bila_kunci_ganda
38. test_jalankan_atas_repo_tiruan
39. test_jalankan_menyertakan_definisi_dan_catatan
40. test_jalankan_menyertakan_sumber_lengkap
41. test_jalankan_bukan_bukti_false
42. test_main_menulis_berkas_dan_kode_bulat
43. test_simbol_h_a011_dan_rentang
44. test_simbol_tengah_tercatat_dua
45. test_medan_funding_tanpa_klines_bernama
46. test_funding_tanpa_klines_kosong_seluruhnya
47. test_funding_tanpa_klines_berisi_dilaporkan
48. test_funding_tanpa_klines_simbol_tak_ada_bukan_kosong
49. test_funding_tanpa_klines_medan_hilang_tak_terukur
50. test_funding_tanpa_klines_bulan_urut
51. test_status_rentang_menyaring_bulan
52. test_status_rentang_simbol_lain_diabaikan
53. test_uji_h_a011_menang_bila_ada_hidup
54. test_uji_h_a011_gugur_bila_semua_mati
55. test_uji_h_a011_rentang_kosong_tak_terukur
56. test_jalankan_memuat_h_a011_dan_funding_tanpa_klines

Cacah: 56 fungsi, 0 parametrize tambahan, maka **56 butir**. Berkas ini
sebelumnya menyumbang 42 butir; selisihnya +14, dan itulah dasar R-228
(382 − 42 + 56 = 396).
"""

from __future__ import annotations

import json
from pathlib import Path

from lux_ai.serapan import kehidupan, kehidupan_arsip, lubang_tengah, silang_funding

HIDUP = kehidupan.STATUS_HIDUP
MATI = kehidupan.STATUS_MATI
SEPI = kehidupan.STATUS_SEPI

BULAN_AAA = ["2021-01", "2021-02", "2021-03", "2021-04", "2021-05"]


def _status():
    status = {("AAA", b): HIDUP for b in BULAN_AAA}
    status[("AAA", "2021-03")] = MATI
    status[("BBB", "2021-01")] = HIDUP
    status[("BBB", "2021-02")] = HIDUP
    status[("BBB", "2021-03")] = HIDUP
    return status


def _byte():
    return {k: 100 + i for i, k in enumerate(sorted(_status()))}


def _lubang():
    # AAA 2021-03 = tengah; BBB 2021-01 = awal; ZZZ di luar penyebut.
    return {("AAA", "2021-03"), ("BBB", "2021-01"), ("ZZZ", "2020-01")}


def _funding():
    return {
        "versi_funding": 6,
        "sidik_kode": "funding-palsu",
        "penyebut": {"bulan_klines": 8},
        "kohort_puncak": {"simbol": []},
        "per_simbol": [
            {
                "simbol": "AAA",
                "klines_tanpa_funding": ["2021-03"],
                "mulai_lubang_ekor": None,
                "funding_tanpa_klines": [],
            },
            {
                "simbol": "BBB",
                "klines_tanpa_funding": ["2021-01"],
                "mulai_lubang_ekor": None,
                "funding_tanpa_klines": [],
            },
            {
                "simbol": "ZZZ",
                "klines_tanpa_funding": ["2020-01"],
                "mulai_lubang_ekor": None,
                "funding_tanpa_klines": ["2019-12", "2019-11"],
            },
        ],
    }


def _tulis_repo(akar: Path, total: int = 1, lilin: bool = True) -> None:
    (akar / "reports").mkdir(parents=True, exist_ok=True)
    baris = []
    for (simbol, bulan), st in sorted(_status().items()):
        b = {
            "simbol": simbol,
            "bulan": bulan,
            "status": st,
            "byte_parquet": 1000 if (simbol, bulan) == ("AAA", "2021-01") else 10,
        }
        if lilin:
            b["cacah_lilin"] = 43200
        baris.append(b)
    for i in range(total):
        isi = {"sidik_kode": "sama", "baris": baris if i == 0 else []}
        (akar / kehidupan_arsip.nama_keluaran(i)).write_text(
            json.dumps(isi, ensure_ascii=False), encoding="utf-8"
        )
    (akar / lubang_tengah.SUMBER_FUNDING).write_text(
        json.dumps(_funding(), ensure_ascii=False), encoding="utf-8"
    )


def _ringkasan_sehat():
    return {
        "sidik_seragam": True,
        "cacah_laporan_dibaca": lubang_tengah.TOTAL_PECAHAN,
        "total_pecahan": lubang_tengah.TOTAL_PECAHAN,
        "cacah_kunci_ganda": 0,
        "kendali_sah": True,
        "selisih_lubang_tengah": 0,
    }


def test_versi_dua():
    assert lubang_tengah.VERSI == 2


def test_nama_keluaran_tetap():
    assert lubang_tengah.nama_keluaran() == "reports/lubang_tengah.json"


def test_sidik_kode_hex_dan_stabil():
    s = lubang_tengah.sidik_kode()
    assert len(s) == 64 and s == lubang_tengah.sidik_kode()
    int(s, 16)


def test_sidik_kode_beda_dari_silang_funding():
    assert lubang_tengah.sidik_kode() != silang_funding.sidik_kode()


def test_berkas_dicap_empat_nama():
    assert lubang_tengah.BERKAS_DICAP == sorted(lubang_tengah.BERKAS_DICAP)
    assert len(lubang_tengah.BERKAS_DICAP) == 4
    assert "lubang_tengah.py" in lubang_tengah.BERKAS_DICAP


def test_tengah_tercatat_enam():
    assert lubang_tengah.TENGAH_TERCATAT == 6


def test_simbol_h_a010_lima_nama():
    assert lubang_tengah.SIMBOL_H_A010 == [
        "BNXUSDT",
        "ICPUSDT",
        "JUPUSDT",
        "QTUMUSDT",
        "TLMUSDT",
    ]


def test_medan_per_simbol_melaporkan_nama_medan():
    medan, cacah = lubang_tengah.medan_per_simbol(_funding())
    assert cacah == 3
    assert medan == [
        "funding_tanpa_klines",
        "klines_tanpa_funding",
        "mulai_lubang_ekor",
        "simbol",
    ]


def test_medan_per_simbol_kosong_aman():
    assert lubang_tengah.medan_per_simbol({}) == ([], 0)


def test_bulan_berfunding_membuang_lubang():
    assert lubang_tengah.bulan_berfunding(BULAN_AAA, {"2021-03"}) == [
        "2021-01",
        "2021-02",
        "2021-04",
        "2021-05",
    ]


def test_bulan_berfunding_urut():
    acak = ["2021-05", "2021-01", "2021-03"]
    assert lubang_tengah.bulan_berfunding(acak, set()) == [
        "2021-01",
        "2021-03",
        "2021-05",
    ]


def test_bulan_berfunding_kosong_bila_semua_lubang():
    assert lubang_tengah.bulan_berfunding(BULAN_AAA, set(BULAN_AAA)) == []


def test_tetangga_berfunding_mengapit_lubang():
    assert lubang_tengah.tetangga_berfunding(BULAN_AAA, {"2021-03"}, "2021-03") == (
        "2021-02",
        "2021-04",
    )


def test_tetangga_berfunding_null_di_ujung():
    assert lubang_tengah.tetangga_berfunding(BULAN_AAA, {"2021-01"}, "2021-01")[0] is None
    assert lubang_tengah.tetangga_berfunding(BULAN_AAA, {"2021-05"}, "2021-05")[1] is None


def test_panjang_rentetan_lubang_berurutan():
    assert (
        lubang_tengah.panjang_rentetan(
            BULAN_AAA, {"2021-02", "2021-03"}, "2021-03"
        )
        == 2
    )


def test_panjang_rentetan_nol_bila_bukan_lubang():
    assert lubang_tengah.panjang_rentetan(BULAN_AAA, {"2021-03"}, "2021-04") == 0


def test_daftar_lubang_tengah_hanya_bentuk_tengah():
    baris = lubang_tengah.daftar_lubang_tengah(_status(), _byte(), _lubang())
    assert [(r["simbol"], r["bulan"]) for r in baris] == [("AAA", "2021-03")]
    assert baris[0]["bentuk_lubang_lokal"] == "tengah"
    assert baris[0]["status"] == MATI


def test_daftar_lubang_tengah_urut():
    status = _status()
    status[("AAB", "2021-01")] = HIDUP
    status[("AAB", "2021-02")] = HIDUP
    status[("AAB", "2021-03")] = HIDUP
    lubang = set(_lubang()) | {("AAB", "2021-02")}
    baris = lubang_tengah.daftar_lubang_tengah(status, {}, lubang)
    assert [r["simbol"] for r in baris] == ["AAA", "AAB"]


def test_daftar_lubang_tengah_memuat_tetangga():
    baris = lubang_tengah.daftar_lubang_tengah(_status(), _byte(), _lubang())[0]
    assert baris["bulan_berfunding_sebelum"] == "2021-02"
    assert baris["bulan_berfunding_sesudah"] == "2021-04"


def test_daftar_lubang_tengah_memuat_panjang_rentetan():
    baris = lubang_tengah.daftar_lubang_tengah(_status(), _byte(), _lubang())[0]
    assert baris["panjang_rentetan_lubang"] == 1


def test_daftar_lubang_tengah_lilin_null_bila_tak_ada():
    baris = lubang_tengah.daftar_lubang_tengah(_status(), _byte(), _lubang())[0]
    assert baris["cacah_lilin"] is None
    berlilin = lubang_tengah.daftar_lubang_tengah(
        _status(), _byte(), _lubang(), {("AAA", "2021-03"): 7}
    )[0]
    assert berlilin["cacah_lilin"] == 7


def test_daftar_lubang_tengah_byte_parquet_nol_bila_tak_ada():
    baris = lubang_tengah.daftar_lubang_tengah(_status(), {}, _lubang())[0]
    assert baris["byte_parquet"] == 0


def test_daftar_lubang_tengah_abai_lubang_luar_penyebut():
    baris = lubang_tengah.daftar_lubang_tengah(_status(), _byte(), _lubang())
    assert all(r["simbol"] != "ZZZ" for r in baris)


def test_daftar_lubang_tengah_memuat_cacah_bulan_dan_lubang():
    baris = lubang_tengah.daftar_lubang_tengah(_status(), _byte(), _lubang())[0]
    assert baris["cacah_bulan_klines_simbol"] == 5
    assert baris["cacah_lubang_simbol"] == 1
    assert baris["bulan_klines_pertama"] == "2021-01"
    assert baris["bulan_klines_terakhir"] == "2021-05"


def test_sebaran_status_mencacah_empat_status():
    sebaran = lubang_tengah.sebaran_status(
        [{"status": MATI}, {"status": MATI}, {"status": SEPI}]
    )
    assert sebaran[MATI] == 2 and sebaran[SEPI] == 1
    assert sebaran[HIDUP] == 0
    assert len(sebaran) == 4


def test_sebaran_status_kosong_nol():
    assert set(lubang_tengah.sebaran_status([]).values()) == {0}


def test_uji_h_a010_menang_bila_funding_menyusul():
    hasil = lubang_tengah.uji_h_a010(_status(), {("AAA", "2021-01")}, ["AAA"])
    assert hasil["menang"] is True
    assert hasil["baris"][0]["bulan_berfunding_pertama"] == "2021-02"


def test_uji_h_a010_gugur_bila_funding_lebih_dulu():
    hasil = lubang_tengah.uji_h_a010(_status(), {("AAA", "2021-03")}, ["AAA"])
    assert hasil["menang"] is False
    assert hasil["cacah_gugur"] == 1


def test_uji_h_a010_simbol_tak_dikenal_tak_terukur():
    hasil = lubang_tengah.uji_h_a010(_status(), set(), ["TIDAKADA"])
    assert hasil["cacah_tak_terukur"] == 1
    assert hasil["baris"][0]["funding_menyusul"] is None
    assert hasil["menang"] is False


def test_uji_h_a010_menang_wajib_semua_simbol():
    hasil = lubang_tengah.uji_h_a010(
        _status(), {("AAA", "2021-01")}, ["AAA", "BBB"]
    )
    assert hasil["cacah_menang"] == 1
    assert hasil["menang"] is False


def test_uji_h_a010_cacah_konsisten():
    hasil = lubang_tengah.uji_h_a010(_status(), _lubang())
    jumlah = (
        hasil["cacah_menang"] + hasil["cacah_gugur"] + hasil["cacah_tak_terukur"]
    )
    assert jumlah == hasil["cacah_simbol"] == 5


def test_kode_keluar_nol_pada_ringkasan_sehat():
    assert lubang_tengah.kode_keluar(_ringkasan_sehat()) == 0


def test_kode_keluar_dua_bila_sidik_tak_seragam():
    r = _ringkasan_sehat()
    r["sidik_seragam"] = False
    assert lubang_tengah.kode_keluar(r) == 2


def test_kode_keluar_dua_bila_laporan_kurang():
    r = _ringkasan_sehat()
    r["cacah_laporan_dibaca"] = lubang_tengah.TOTAL_PECAHAN - 1
    assert lubang_tengah.kode_keluar(r) == 2


def test_kode_keluar_dua_bila_selisih_tengah_bukan_nol():
    r = _ringkasan_sehat()
    r["selisih_lubang_tengah"] = -1
    assert lubang_tengah.kode_keluar(r) == 2


def test_kode_keluar_dua_bila_kendali_tak_sah():
    r = _ringkasan_sehat()
    r["kendali_sah"] = False
    assert lubang_tengah.kode_keluar(r) == 2


def test_kode_keluar_dua_bila_kunci_ganda():
    r = _ringkasan_sehat()
    r["cacah_kunci_ganda"] = 1
    assert lubang_tengah.kode_keluar(r) == 2


def test_jalankan_atas_repo_tiruan(tmp_path):
    _tulis_repo(tmp_path, total=1)
    laporan = lubang_tengah.jalankan(akar=str(tmp_path), total=1)
    ringkasan = laporan["ringkasan"]
    assert ringkasan["penyebut_kehidupan"] == 8
    assert ringkasan["cacah_lubang_tengah"] == 1
    assert ringkasan["selisih_lubang_tengah"] == 1 - lubang_tengah.TENGAH_TERCATAT
    assert ringkasan["sebaran_status_lubang_tengah"][MATI] == 1
    assert ringkasan["cacah_per_simbol_funding"] == 3


def test_jalankan_menyertakan_definisi_dan_catatan(tmp_path):
    _tulis_repo(tmp_path, total=1)
    laporan = lubang_tengah.jalankan(akar=str(tmp_path), total=1)
    assert "tengah" in laporan["definisi"]["bentuk_lubang_lokal"]
    assert laporan["catatan_batas_h_a010"]
    assert laporan["catatan_batas_h_a011"]
    assert laporan["catatan_penggugur"]


def test_jalankan_menyertakan_sumber_lengkap(tmp_path):
    _tulis_repo(tmp_path, total=1)
    laporan = lubang_tengah.jalankan(akar=str(tmp_path), total=1)
    assert laporan["sumber"] == [
        lubang_tengah.SUMBER_FUNDING,
        kehidupan_arsip.nama_keluaran(0),
    ]


def test_jalankan_bukan_bukti_false(tmp_path):
    _tulis_repo(tmp_path, total=1)
    laporan = lubang_tengah.jalankan(akar=str(tmp_path), total=1)
    assert laporan["bukan_bukti"] is False
    assert laporan["versi_lubang_tengah"] == 2


def test_main_menulis_berkas_dan_kode_bulat(tmp_path, monkeypatch):
    _tulis_repo(tmp_path, total=lubang_tengah.TOTAL_PECAHAN)
    monkeypatch.chdir(tmp_path)
    kode = lubang_tengah.main()
    assert isinstance(kode, int)
    isi = json.loads(Path(lubang_tengah.KELUARAN).read_text(encoding="utf-8"))
    assert isi["ringkasan"]["cacah_lubang_tengah"] == 1


def test_simbol_h_a011_dan_rentang():
    assert lubang_tengah.SIMBOL_H_A011 == "LITUSDT"
    assert lubang_tengah.RENTANG_H_A011 == ("2026-01", "2026-06")


def test_simbol_tengah_tercatat_dua():
    assert lubang_tengah.SIMBOL_TENGAH_TERCATAT == ["BTCSTUSDT", "LITUSDT"]


def test_medan_funding_tanpa_klines_bernama():
    assert lubang_tengah.MEDAN_FUNDING_TANPA_KLINES == "funding_tanpa_klines"


def test_funding_tanpa_klines_kosong_seluruhnya():
    hasil = lubang_tengah.funding_tanpa_klines(_funding(), ["AAA", "BBB"])
    assert hasil["cacah_simbol"] == 2
    assert hasil["cacah_berisi"] == 0
    assert hasil["cacah_tak_terukur"] == 0
    assert hasil["kosong_seluruhnya"] is True


def test_funding_tanpa_klines_berisi_dilaporkan():
    hasil = lubang_tengah.funding_tanpa_klines(_funding(), ["ZZZ"])
    assert hasil["cacah_berisi"] == 1
    assert hasil["kosong_seluruhnya"] is False
    assert hasil["baris"][0]["cacah_bulan"] == 2


def test_funding_tanpa_klines_simbol_tak_ada_bukan_kosong():
    hasil = lubang_tengah.funding_tanpa_klines(_funding(), ["TIDAKADA"])
    assert hasil["baris"][0]["ada_di_per_simbol"] is False
    assert hasil["cacah_tak_terukur"] == 1
    assert hasil["kosong_seluruhnya"] is False


def test_funding_tanpa_klines_medan_hilang_tak_terukur():
    hasil = lubang_tengah.funding_tanpa_klines(
        {"per_simbol": [{"simbol": "CCC"}]}, ["CCC"]
    )
    assert hasil["baris"][0]["ada_di_per_simbol"] is True
    assert hasil["baris"][0]["ada_medan"] is False
    assert hasil["cacah_tak_terukur"] == 1
    assert hasil["kosong_seluruhnya"] is False


def test_funding_tanpa_klines_bulan_urut():
    hasil = lubang_tengah.funding_tanpa_klines(_funding(), ["ZZZ"])
    assert hasil["baris"][0]["bulan"] == ["2019-11", "2019-12"]


def test_status_rentang_menyaring_bulan():
    baris = lubang_tengah.status_rentang(_status(), "AAA", "2021-02", "2021-04")
    assert [r["bulan"] for r in baris] == ["2021-02", "2021-03", "2021-04"]
    assert baris[1]["status"] == MATI


def test_status_rentang_simbol_lain_diabaikan():
    baris = lubang_tengah.status_rentang(_status(), "BBB", "2021-01", "2021-05")
    assert len(baris) == 3
    assert all(r["simbol"] == "BBB" for r in baris)
    assert lubang_tengah.status_rentang(_status(), "LITUSDT", "2026-01", "2026-06") == []


def test_uji_h_a011_menang_bila_ada_hidup():
    status = {("LITUSDT", "2026-01"): MATI, ("LITUSDT", "2026-02"): HIDUP}
    hasil = lubang_tengah.uji_h_a011(status)
    assert hasil["terukur"] is True
    assert hasil["cacah_bulan"] == 2
    assert hasil["cacah_hidup"] == 1
    assert hasil["menang"] is True


def test_uji_h_a011_gugur_bila_semua_mati():
    status = {("LITUSDT", b): MATI for b in ("2026-01", "2026-02", "2026-03")}
    hasil = lubang_tengah.uji_h_a011(status)
    assert hasil["terukur"] is True
    assert hasil["cacah_hidup"] == 0
    assert hasil["menang"] is False
    assert hasil["sebaran_status"][MATI] == 3


def test_uji_h_a011_rentang_kosong_tak_terukur():
    hasil = lubang_tengah.uji_h_a011(_status())
    assert hasil["cacah_bulan"] == 0
    assert hasil["terukur"] is False
    assert hasil["menang"] is False


def test_jalankan_memuat_h_a011_dan_funding_tanpa_klines(tmp_path):
    _tulis_repo(tmp_path, total=1)
    laporan = lubang_tengah.jalankan(akar=str(tmp_path), total=1)
    assert "simbal" not in json.dumps(laporan["definisi"], ensure_ascii=False)
    assert "simbol" in laporan["definisi"]["h_a010_menang"]
    assert laporan["funding_tanpa_klines"]["cacah_simbol"] == 5
    assert laporan["h_a011"]["simbol"] == "LITUSDT"
    ringkasan = laporan["ringkasan"]
    assert ringkasan["h_a011_terukur"] is False
    assert ringkasan["h_a010_cacah_simbol_tak_terukur"] == 5
    assert ringkasan["h_a010_funding_tanpa_klines_kosong"] is False
