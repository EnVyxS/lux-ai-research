"""Uji CARA MENGUKUR survei semesta. Tidak ada satu pun sentuhan jaringan."""
from __future__ import annotations

from lux_ai.serapan import survei


def test_deret_bulan_melintasi_tahun():
    assert survei.bulan_dalam_rentang("2021-11", "2022-02") == [
        "2021-11",
        "2021-12",
        "2022-01",
        "2022-02",
    ]


def test_deret_bulan_satu_bulan():
    assert survei.bulan_dalam_rentang("2024-05", "2024-05") == ["2024-05"]


def test_selisih_bulan_melintasi_tahun():
    assert survei.selisih_bulan("2024-05", "2026-06") == 25
    assert survei.selisih_bulan("2026-06", "2026-06") == 0


def test_terhenti_membedakan_simbol_mati_dari_simbol_hidup():
    # kasus positif: berhenti 25 bulan sebelum semesta
    assert survei.terhenti("2024-05", "2026-06") is True
    # kasus negatif: masih terbit di bulan tutup semesta
    assert survei.terhenti("2026-06", "2026-06") is False
    # kasus negatif: tertinggal satu bulan saja, itu jeda terbit biasa
    assert survei.terhenti("2026-05", "2026-06") is False


def test_terhenti_tidak_bergantung_pada_kehadiran_di_indeks():
    """KC-5: dua simbol sama-sama ada di indeks, putusannya harus berbeda."""
    rentang = {
        "MATIUSDT": {"bulan_terakhir": "2024-05"},
        "HIDUPUSDT": {"bulan_terakhir": "2026-06"},
    }
    putusan = {s: survei.terhenti(r["bulan_terakhir"], "2026-06") for s, r in rentang.items()}
    assert putusan == {"MATIUSDT": True, "HIDUPUSDT": False}


def test_cacah_lebih_tua():
    rentang = {
        "A": {"bulan_terakhir": "2025-12"},
        "B": {"bulan_terakhir": "2026-01"},
        "C": {"bulan_terakhir": "2026-06"},
    }
    assert survei.cacah_lebih_tua(rentang, "2026-01") == 1


def test_ringkas_header_menemukan_batas():
    peta = {"2021-01": False, "2021-02": False, "2021-03": True, "2021-04": True}
    hasil = survei.ringkas_header(peta)
    assert hasil["bulan_tanpa_header_terakhir"] == "2021-02"
    assert hasil["bulan_berheader_pertama"] == "2021-03"
    assert hasil["monoton"] is True
    assert hasil["bulan_diperiksa"] == 4


def test_ringkas_header_menandai_peralihan_yang_tidak_monoton():
    """Bila format bolak-balik, gagasan satu bulan peralihan harus ditolak."""
    peta = {"2021-01": False, "2021-02": True, "2021-03": False, "2021-04": True}
    hasil = survei.ringkas_header(peta)
    assert hasil["monoton"] is False


def test_ringkas_header_seluruhnya_satu_format():
    assert survei.ringkas_header({"2026-06": True})["bulan_tanpa_header_terakhir"] is None
    assert survei.ringkas_header({"2020-01": False})["bulan_berheader_pertama"] is None


def test_satuan_stempel_membedakan_mili_dan_mikro():
    assert survei.satuan_stempel(1717200000000) == "milidetik"
    assert survei.satuan_stempel(1717200000000000) == "mikrodetik"
    assert survei.satuan_stempel(1717200000) == "tidak_dikenali"


def test_iso_dari_stempel_sama_untuk_kedua_satuan():
    mili = survei.iso_dari_stempel(1717200000000)
    mikro = survei.iso_dari_stempel(1717200000000000)
    assert mili == mikro == "2024-06-01T00:00:00Z"


def test_ringkas_satuan_seragam():
    peta = {"2020-01": "milidetik", "2026-06": "milidetik"}
    hasil = survei.ringkas_satuan(peta)
    assert hasil["seragam"] is True
    assert hasil["satuan_unik"] == ["milidetik"]
    assert hasil["bulan_satuan_berubah"] is None
    assert hasil["bulan_disampel"] == 2


def test_ringkas_satuan_menunjuk_bulan_peralihan():
    """Kasus positif R-18 gagal: satuan berpindah di tengah sejarah."""
    peta = {
        "2024-04": "milidetik",
        "2024-05": "milidetik",
        "2024-06": "mikrodetik",
        "2024-07": "mikrodetik",
    }
    hasil = survei.ringkas_satuan(peta)
    assert hasil["seragam"] is False
    assert hasil["bulan_satuan_berubah"] == "2024-06"
    assert hasil["satuan_unik"] == ["mikrodetik", "milidetik"]


def test_ringkas_satuan_peta_kosong_bukan_bukti_keseragaman():
    """Aturan 18: tidak mengukur apa pun tidak boleh terbaca sebagai lolos."""
    hasil = survei.ringkas_satuan({})
    assert hasil["seragam"] is False
    assert hasil["bulan_disampel"] == 0
    assert hasil["satuan_unik"] == []


def test_ringkas_satuan_menahan_satuan_tak_dikenali():
    peta = {"2020-01": "milidetik", "2020-02": "tidak_dikenali"}
    hasil = survei.ringkas_satuan(peta)
    assert hasil["seragam"] is False
    assert "tidak_dikenali" in hasil["satuan_unik"]


def test_survei_tidak_memakai_jaringan_langsung():
    """Menguji CARA MENGUKUR: survei hanya boleh lewat modul arsip."""
    import ast
    from pathlib import Path

    berkas = Path(survei.__file__)
    pohon = ast.parse(berkas.read_text())
    diimpor = set()
    for simpul in ast.walk(pohon):
        if isinstance(simpul, ast.Import):
            diimpor.update(a.name.split(".")[0] for a in simpul.names)
        elif isinstance(simpul, ast.ImportFrom) and simpul.module and simpul.level == 0:
            diimpor.add(simpul.module.split(".")[0])
    assert "urllib" not in diimpor
    assert "http" not in diimpor
    assert "socket" not in diimpor
