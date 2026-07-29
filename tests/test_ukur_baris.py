"""Uji modul ukur_baris.

Tiga fungsi uji, TANPA `parametrize`, dihitung dengan menyebut satu per satu:
(1) definisi_sama_dengan_pagar, (2) berkas_hilang_dilaporkan,
(3) pilahan_kosong_komentar_kode.
"""

from __future__ import annotations

import pathlib

from lux_ai.serapan import ukur_baris

AKAR = pathlib.Path(__file__).resolve().parents[1]


def test_definisi_cacah_baris_sama_dengan_pagar_800(tmp_path):
    """Kalau definisinya menyimpang dari pagar, pita R-175 dan R-179 tak bermakna."""
    p = tmp_path / "a.py"
    p.write_text("satu\ndua\ntiga\n", encoding="utf-8")
    h = ukur_baris.ukur_berkas(p)
    assert h["cacah_baris"] == len(p.read_text(encoding="utf-8").splitlines()) == 3
    assert h["cacah_newline"] == 3
    assert h["berakhir_newline"] is True
    assert h["melebihi_pagar"] is False

    # tanpa baris baru di ekor, kedua definisi berbeda tepat satu
    q = tmp_path / "b.py"
    q.write_text("satu\ndua", encoding="utf-8")
    hq = ukur_baris.ukur_berkas(q)
    assert hq["cacah_baris"] == 2
    assert hq["cacah_newline"] == 1
    assert hq["berakhir_newline"] is False

    # berkas nyata: definisi modul ini harus sepadan dengan cara pagar mengukur
    nyata = AKAR / "lux_ai" / "serapan" / "ukur_baris.py"
    hn = ukur_baris.ukur_berkas(nyata)
    assert hn["cacah_baris"] == len(nyata.read_text(encoding="utf-8").splitlines())


def test_berkas_hilang_dilaporkan_bukan_dilempar(tmp_path):
    hilang = ukur_baris.ukur_berkas(tmp_path / "tidak_ada.py")
    assert hilang["ada"] is False
    assert hilang["cacah_baris"] is None
    assert hilang["melebihi_pagar"] is None

    (tmp_path / "c.py").write_text("x = 1\n", encoding="utf-8")
    ada = ukur_baris.ukur_berkas(tmp_path / "c.py")
    r = ukur_baris.ringkas([ada, hilang])
    assert r["cacah_berkas_diminta"] == 2
    assert r["cacah_berkas_ada"] == 1
    assert r["cacah_berkas_hilang"] == 1
    assert r["cacah_baris_total"] == 1
    assert r["cacah_berkas_melebihi_pagar"] == 0

    # seluruh berkas yang didaftar modul harus benar-benar ada di repo
    laporan = ukur_baris.jalankan(str(AKAR))
    assert laporan["ringkasan"]["cacah_berkas_hilang"] == 0


def test_pilahan_baris_kosong_komentar_dan_kode(tmp_path):
    p = tmp_path / "d.py"
    p.write_text(
        "# komentar\n\n    # komentar menjorok\nx = 1  # bukan baris komentar\n",
        encoding="utf-8",
    )
    h = ukur_baris.ukur_berkas(p)
    assert h["cacah_baris"] == 4
    assert h["cacah_baris_kosong"] == 1
    assert h["cacah_baris_komentar"] == 2
    assert h["cacah_baris_kode"] == 1
