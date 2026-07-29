"""Uji pelapor ringkas. Tiga fungsi uji, tanpa parametrize (aturan 47)."""

from __future__ import annotations

import hashlib
import json

from lux_ai.serapan import kohort_ringkas


def _laporan():
    return {
        "versi_kohort_ekor": 3,
        "ringkasan": {"cacah_uji_sepi": 10, "parser_terbukti": True},
        "riwayat": [{"simbol": "AAA", "bulan_hidup_terakhir": "2025-04"}],
        "catatan_penggugur": "jangan hilang",
        "baris": [{"simbol": "AAA", "bulan": "2025-04"}, {"simbol": "AAA", "bulan": "2025-05"}],
    }


def test_ringkas_membuang_baris_tetapi_menahan_ringkasan_dan_riwayat():
    hasil = kohort_ringkas.ringkas_laporan(_laporan())
    assert "baris" not in hasil
    assert hasil["cacah_baris_penuh"] == 2
    assert hasil["medan_dibuang"] == ["baris"]
    # medan yang menentukan tafsir TIDAK boleh ikut terbuang
    assert hasil["ringkasan"] == {"cacah_uji_sepi": 10, "parser_terbukti": True}
    assert hasil["riwayat"][0]["bulan_hidup_terakhir"] == "2025-04"
    assert hasil["catatan_penggugur"] == "jangan hilang"
    assert hasil["versi_kohort_ekor"] == 3


def test_sidik_sumber_mengikat_ringkasan_pada_berkas_yang_itu_juga(tmp_path):
    (tmp_path / "reports").mkdir()
    jalur = tmp_path / "reports" / "kohort_ekor.json"
    jalur.write_text(json.dumps(_laporan()), encoding="utf-8")
    hasil = kohort_ringkas.jalankan(str(tmp_path))
    assert hasil["galat_ringkas"] is None
    assert hasil["sidik_sumber"] == hashlib.sha256(jalur.read_bytes()).hexdigest()

    # berkas berubah satu byte -> sidik WAJIB berubah
    jalur.write_text(json.dumps(_laporan()) + " ", encoding="utf-8")
    assert kohort_ringkas.jalankan(str(tmp_path))["sidik_sumber"] != hasil["sidik_sumber"]


def test_sumber_hilang_atau_rusak_melaporkan_galat_bukan_melempar(tmp_path):
    hilang = kohort_ringkas.jalankan(str(tmp_path))
    assert hilang["galat_ringkas"]
    assert "ringkasan" not in hilang

    (tmp_path / "reports").mkdir()
    (tmp_path / "reports" / "kohort_ekor.json").write_text("{bukan json", encoding="utf-8")
    rusak = kohort_ringkas.jalankan(str(tmp_path))
    assert rusak["galat_ringkas"]
    # bahkan saat rusak, sidik sumber tetap dicatat supaya dapat dilacak
    assert rusak["sidik_sumber"]
