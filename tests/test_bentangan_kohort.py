"""Butir uji bentangan_kohort V2.

Perbedaan pokok dengan V1: data sintetis di sini memakai BENTUK NYATA sumbernya
— kunci TUPLE `(simbol, bulan)` dan kembalian PASANGAN dari `silang_funding` —
sebab data sintetis yang bentuknya dikarang sendiri hanya menguji karangan itu
(penangkal KC-43). Butir 47 memanggil `silang_funding` yang asli untuk memeriksa
bentuk kembaliannya, bukan mengandaikannya.
"""
from __future__ import annotations

from pathlib import Path

from lux_ai.serapan import (
    bentangan_kohort as bk,
    kehidupan,
    kohort_ekor,
    silang_funding,
)

HIDUP = kehidupan.STATUS_HIDUP
MATI = kehidupan.STATUS_MATI
SEPI = kehidupan.STATUS_SEPI


def peta(**bulan):
    """Peta {bulan: status} dengan bulan bertanda garis bawah, mis. b2025_07."""
    return {k[1:].replace("_", "-"): v for k, v in bulan.items()}


# --- pisah_kunci (bentuk kanon TUPLE) ---------------------------------------


def test_01_pisah_kunci_tuple_kanon():
    assert bk.pisah_kunci(("AAAUSDT", "2026-06")) == ("AAAUSDT", "2026-06")


def test_02_pisah_kunci_daftar_dua_unsur_diterima():
    assert bk.pisah_kunci(["AAAUSDT", "2025-07"]) == ("AAAUSDT", "2025-07")


def test_03_pisah_kunci_tuple_panjang_salah_ditolak():
    assert bk.pisah_kunci(("AAAUSDT", "2026-06", "1m")) is None


def test_04_pisah_kunci_tuple_bulan_bukan_bulan_ditolak():
    assert bk.pisah_kunci(("AAAUSDT", "Juni")) is None


def test_05_pisah_kunci_tuple_simbol_kosong_ditolak():
    assert bk.pisah_kunci(("", "2026-06")) is None


def test_06_pisah_kunci_string_gabungan():
    assert bk.pisah_kunci("AAAUSDT2026-06") == ("AAAUSDT", "2026-06")


def test_07_pisah_kunci_string_berpemisah():
    assert bk.pisah_kunci("AAAUSDT|2026-06") == ("AAAUSDT", "2026-06")


def test_08_pisah_kunci_bukan_string_bukan_tuple_ditolak():
    assert bk.pisah_kunci(2026) is None


def test_09_pisah_kunci_string_tuple_dicetak_ditolak():
    """Inilah cacat V1: str(tuple) berakhir dengan tanda kurung dan wajib ditolak."""
    assert bk.pisah_kunci(str(("AAAUSDT", "2026-06"))) is None


# --- kelompokkan ------------------------------------------------------------


def test_10_kelompokkan_kunci_tuple():
    status = {("A", "2026-05"): HIDUP, ("A", "2026-06"): MATI, ("B", "2026-06"): HIDUP}
    hasil, gagal = bk.kelompokkan(status)
    assert gagal == []
    assert hasil == {"A": {"2026-05": HIDUP, "2026-06": MATI}, "B": {"2026-06": HIDUP}}


def test_11_kelompokkan_melaporkan_kunci_gagal():
    hasil, gagal = bk.kelompokkan({("A", "2026-06"): HIDUP, 7: MATI})
    assert list(hasil) == ["A"]
    assert gagal == ["7"]


def test_12_kelompokkan_status_dijadikan_string():
    hasil, _ = bk.kelompokkan({("A", "2026-06"): HIDUP})
    assert hasil["A"]["2026-06"] == HIDUP


# --- bulan_berstatus --------------------------------------------------------


def test_13_bulan_berstatus_urut_menaik():
    p = peta(b2026_06=HIDUP, b2026_04=HIDUP, b2026_05=MATI)
    assert bk.bulan_berstatus(p, HIDUP) == ["2026-04", "2026-06"]


def test_14_bulan_berstatus_kosong_bila_tak_ada():
    assert bk.bulan_berstatus(peta(b2026_06=HIDUP), MATI) == []


def test_15_bulan_berstatus_sepi_terpisah_dari_mati():
    p = peta(b2026_05=SEPI, b2026_06=MATI)
    assert bk.bulan_berstatus(p, SEPI) == ["2026-05"]


# --- mati_tersisip ----------------------------------------------------------


def test_16_mati_tersisip_terapit_dicacah():
    p = peta(b2025_01=HIDUP, b2025_02=MATI, b2025_03=HIDUP)
    assert bk.mati_tersisip(p) == 1


def test_17_mati_tersisip_dua_bulan_terapit():
    p = peta(b2025_01=HIDUP, b2025_02=MATI, b2025_03=MATI, b2025_04=HIDUP)
    assert bk.mati_tersisip(p) == 2


def test_18_mati_tersisip_ekor_tidak_dicacah():
    p = peta(b2025_01=HIDUP, b2025_02=HIDUP, b2025_03=MATI)
    assert bk.mati_tersisip(p) == 0


def test_19_mati_tersisip_awal_tidak_dicacah():
    p = peta(b2025_01=MATI, b2025_02=HIDUP, b2025_03=HIDUP)
    assert bk.mati_tersisip(p) == 0


def test_20_mati_tersisip_tanpa_hidup_nol():
    assert bk.mati_tersisip(peta(b2025_01=MATI, b2025_02=MATI)) == 0


def test_21_mati_tersisip_satu_hidup_saja_nol():
    assert bk.mati_tersisip(peta(b2025_01=HIDUP, b2025_02=MATI)) == 0


# --- bangkit ----------------------------------------------------------------


def test_22_bangkit_benar_bila_hidup_sesudah_mati():
    p = peta(b2025_02=MATI, b2026_01=HIDUP)
    assert bk.bangkit(p) is True


def test_23_bangkit_salah_bila_mati_di_ekor():
    p = peta(b2025_02=HIDUP, b2026_01=MATI)
    assert bk.bangkit(p) is False


def test_24_bangkit_salah_tanpa_mati():
    assert bk.bangkit(peta(b2025_02=HIDUP, b2026_01=HIDUP)) is False


def test_25_bangkit_salah_tanpa_hidup():
    assert bk.bangkit(peta(b2025_02=MATI)) is False


# --- rentetan_terpanjang ----------------------------------------------------


def test_26_rentetan_berurutan_kalender():
    assert bk.rentetan_terpanjang(["2025-11", "2025-12", "2026-01"]) == 3


def test_27_rentetan_diputus_celah():
    assert bk.rentetan_terpanjang(["2025-01", "2025-02", "2025-05"]) == 2


def test_28_rentetan_kosong_nol():
    assert bk.rentetan_terpanjang([]) == 0


def test_29_rentetan_bulan_cacat_diabaikan():
    assert bk.rentetan_terpanjang(["2025-01", "bukan-bulan"]) == 1


# --- ringkas_simbol ---------------------------------------------------------


def test_30_ringkas_simbol_cacah_dasar():
    p = peta(b2025_01=HIDUP, b2025_02=MATI, b2025_03=SEPI)
    r = bk.ringkas_simbol("A", p)
    assert (r["cacah_bulan"], r["cacah_hidup"], r["cacah_mati"], r["cacah_sepi"]) == (
        3,
        1,
        1,
        1,
    )


def test_31_ringkas_simbol_bulan_tepi():
    p = peta(b2025_01=HIDUP, b2025_03=MATI)
    r = bk.ringkas_simbol("A", p)
    assert r["bulan_pertama"] == "2025-01" and r["bulan_terakhir"] == "2025-03"


def test_32_ringkas_simbol_hidup_sesudah_tebing_termasuk_tebing():
    p = {bk.TEBING: HIDUP, "2020-01": HIDUP}
    r = bk.ringkas_simbol("A", p)
    assert r["cacah_hidup_sesudah_tebing"] == 1
    assert r["bulan_hidup_sesudah_tebing"] == [bk.TEBING]


def test_33_ringkas_simbol_hidup_sebelum_tebing_tidak_dicacah():
    r = bk.ringkas_simbol("A", {"2020-01": HIDUP})
    assert r["cacah_hidup_sesudah_tebing"] == 0


def test_34_ringkas_simbol_byte_dan_lilin_berkunci_tuple():
    p = peta(b2025_01=HIDUP, b2025_02=HIDUP)
    r = bk.ringkas_simbol(
        "A",
        p,
        byte_parquet={("A", "2025-01"): 100, ("A", "2025-02"): 5, ("B", "2025-01"): 999},
        lilin={("A", "2025-01"): 7, ("A", "2025-02"): 3},
    )
    assert r["byte_parquet_total"] == 105
    assert r["cacah_lilin_total"] == 10


def test_35_ringkas_simbol_lubang_funding_dicacah():
    p = peta(b2025_01=HIDUP, b2025_02=MATI)
    r = bk.ringkas_simbol("A", p, bulan_berlubang={"2025-02", "2099-01"})
    assert r["cacah_bulan_berlubang_funding"] == 1


def test_36_ringkas_simbol_bulan_terakhir_diharapkan():
    r = bk.ringkas_simbol("A", {bk.BULAN_DIHARAPKAN: HIDUP})
    assert r["bulan_terakhir_sama_diharapkan"] is True


def test_37_ringkas_simbol_tanpa_bulan_bukan_nol_melainkan_null():
    r = bk.ringkas_simbol("A", {})
    assert r["cacah_bulan"] == 0
    assert r["bulan_terakhir"] is None
    assert r["bulan_terakhir_sama_diharapkan"] is None


# --- uji_r301 ---------------------------------------------------------------


def baris_uji(hidup_sesudah=0, tersisip=0, bangkit=False):
    return {
        "cacah_hidup_sesudah_tebing": hidup_sesudah,
        "cacah_mati_tersisip": tersisip,
        "bangkit": bangkit,
    }


def test_38_uji_r301_ketiga_butir_menang():
    hasil = bk.uji_r301([baris_uji(tersisip=1), baris_uji()])
    assert (hasil["butir_1"], hasil["butir_2"], hasil["butir_3"]) == (True, True, True)
    assert hasil["cacah_butir_menang"] == 3


def test_39_uji_r301_butir_1_kalah():
    hasil = bk.uji_r301([baris_uji(hidup_sesudah=2, tersisip=1)])
    assert hasil["butir_1"] is False
    assert hasil["cacah_simbol_hidup_sesudah_tebing"] == 1


def test_40_uji_r301_butir_2_kalah():
    hasil = bk.uji_r301([baris_uji(), baris_uji()])
    assert hasil["butir_2"] is False
    assert hasil["pembatal_a008_menyala"] is False


def test_41_uji_r301_butir_3_kalah():
    hasil = bk.uji_r301([baris_uji(tersisip=1, bangkit=True)])
    assert hasil["butir_3"] is False
    assert hasil["cacah_simbol_bangkit"] == 1


def test_42_uji_r301_penyebut_dilapor():
    assert bk.uji_r301([baris_uji(), baris_uji(), baris_uji()])["penyebut_simbol"] == 3


# --- kendali positif --------------------------------------------------------


def test_43_kendali_sah_bila_semua_hidup():
    status = {(s, bk.BULAN_DIHARAPKAN): HIDUP for s in bk.KENDALI_HIDUP}
    kendali = bk.kendali_positif(status)
    assert len(kendali) == len(bk.KENDALI_HIDUP)
    assert bk.kendali_sah(kendali) is True


def test_44_kendali_tidak_sah_bila_satu_hilang():
    status = {(bk.KENDALI_HIDUP[0], bk.BULAN_DIHARAPKAN): HIDUP}
    kendali = bk.kendali_positif(status)
    assert bk.kendali_sah(kendali) is False
    assert kendali[1]["status"] is None


def test_45_kendali_tidak_sah_bila_mati():
    status = {(s, bk.BULAN_DIHARAPKAN): MATI for s in bk.KENDALI_HIDUP}
    assert bk.kendali_sah(bk.kendali_positif(status)) is False


# --- kode_keluar ------------------------------------------------------------


def laporan_bersih(**ubah):
    ringkasan = {
        "sidik_seragam": True,
        "kendali_sah": True,
        "penyebut_kehidupan": 19586,
        "cacah_kunci_gagal_pisah": 0,
        "cacah_simbol_kohort": 38,
    }
    ringkasan.update(ubah.pop("ringkasan", {}))
    laporan = {"galat_kohort": None, "ringkasan": ringkasan}
    laporan.update(ubah)
    return laporan


def test_46_kode_keluar_nol_bila_bersih():
    assert bk.kode_keluar(laporan_bersih()) == 0


def test_47_kode_keluar_dua_bila_galat_kohort():
    assert bk.kode_keluar(laporan_bersih(galat_kohort="sumber tidak ada")) == 2


def test_48_kode_keluar_dua_bila_sidik_tidak_seragam():
    assert bk.kode_keluar(laporan_bersih(ringkasan={"sidik_seragam": False})) == 2


def test_49_kode_keluar_dua_bila_kendali_tidak_sah():
    assert bk.kode_keluar(laporan_bersih(ringkasan={"kendali_sah": False})) == 2


def test_50_kode_keluar_dua_bila_penyebut_nol():
    assert bk.kode_keluar(laporan_bersih(ringkasan={"penyebut_kehidupan": 0})) == 2


def test_51_kode_keluar_dua_bila_ada_kunci_gagal_pisah():
    assert bk.kode_keluar(laporan_bersih(ringkasan={"cacah_kunci_gagal_pisah": 3})) == 2


def test_52_kode_keluar_dua_bila_kohort_kosong():
    assert bk.kode_keluar(laporan_bersih(ringkasan={"cacah_simbol_kohort": 0})) == 2


# --- tetapan dan warisan ----------------------------------------------------


def test_53_versi_dua():
    assert bk.VERSI == 2


def test_54_tetapan_diwarisi_kohort_ekor():
    assert bk.TEBING == kohort_ekor.TEBING == "2025-07"
    assert bk.BULAN_DIHARAPKAN == kohort_ekor.BULAN_DIHARAPKAN == "2026-06"
    assert bk.KENDALI_HIDUP == kohort_ekor.KENDALI_HIDUP


def test_55_medan_lilin_diwarisi_silang_funding():
    assert bk.MEDAN_LILIN == silang_funding.MEDAN_LILIN
    assert bk.SUMBER_FUNDING == silang_funding.SUMBER_FUNDING


def test_56_tetapan_praregistrasi_tidak_bergeser():
    assert bk.R301_BUTIR_1_HIDUP_SESUDAH_TEBING == 0
    assert bk.R301_BUTIR_2_MINIMAL_SATU_TERSISIP == 1
    assert bk.R301_BUTIR_3_BANGKIT == 0


def test_57_berkas_dicap_empat_nama_dan_ada():
    assert len(bk.BERKAS_DICAP) == 4
    dasar = Path(bk.__file__).parent
    for nama in bk.BERKAS_DICAP:
        assert (dasar / nama).exists()


def test_58_sidik_kode_stabil_dan_heksa():
    sidik = bk.sidik_kode()
    assert sidik == bk.sidik_kode()
    assert len(sidik) == 64


# --- penangkal KC-43: bentuk kembalian sumber diperiksa, bukan diandaikan ---


def test_59_lubang_funding_mengembalikan_pasangan_himpunan_dan_meta():
    hasil = silang_funding.lubang_funding({"per_simbol": []})
    assert isinstance(hasil, tuple) and len(hasil) == 2
    assert isinstance(hasil[0], set) and isinstance(hasil[1], dict)


def test_60_baca_medan_baris_mengembalikan_pasangan(tmp_path):
    hasil = silang_funding.baca_medan_baris(str(tmp_path), 1, silang_funding.MEDAN_LILIN)
    assert isinstance(hasil, tuple) and len(hasil) == 2
    assert isinstance(hasil[0], dict) and isinstance(hasil[1], dict)


def test_61_baca_laporan_kehidupan_mengembalikan_tiga_unsur(tmp_path):
    hasil = silang_funding.baca_laporan_kehidupan(str(tmp_path), 1)
    assert isinstance(hasil, tuple) and len(hasil) == 3
    assert hasil[2]["sidik_seragam"] is False


def test_62_jalankan_tanpa_bahan_menggugurkan_dirinya(tmp_path):
    laporan = bk.jalankan(str(tmp_path), total=1)
    assert laporan["galat_kohort"]
    assert laporan["ringkasan"]["penyebut_kehidupan"] == 0
    assert laporan["ringkasan"]["cacah_kunci_gagal_pisah"] == 0
    assert bk.kode_keluar(laporan) == 2


def test_63_modul_tidak_memuat_daftar_nama_kohort():
    """Aturan 73: nama anggota kohort dibaca di runner, tidak pernah ditetapkan."""
    sumber = Path(bk.__file__).read_text(encoding="utf-8")
    for nama in ("BTCSTUSDT", "LITUSDT", "BNXUSDT", "TLMUSDT", "ICPUSDT"):
        assert nama not in sumber
