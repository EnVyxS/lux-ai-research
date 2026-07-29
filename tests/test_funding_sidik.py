"""Uji bahwa pemecahan modul tidak menyempitkan sidik kode (aturan 48).

VERSI 6 memindahkan blok CDN keluar dari `funding.py`. Bahaya pemecahan
semacam itu halus: kode berpindah KELUAR dari cap `sidik_kode`, sehingga dua
versi kode yang berbeda dapat menghasilkan sidik yang sama, dan laporan run
lama tidak lagi dapat dibedakan dari yang baru. Uji ini mengunci ketiga berkas
yang ikut menentukan isi laporan, dan sekaligus membuktikan bahwa berkas yang
baru benar-benar ikut dicap.
"""
import hashlib
from pathlib import Path

from lux_ai.serapan import funding

DASAR = Path(funding.__file__).parent
BERKAS_DICAP = ["arsip.py", "funding.py", "funding_cdn.py"]


def _sidik(nama):
    h = hashlib.sha256()
    for n in sorted(nama):
        h.update((DASAR / n).read_bytes())
    return h.hexdigest()


def test_sidik_kode_mencakup_funding_cdn():
    assert funding.sidik_kode() == _sidik(BERKAS_DICAP)
    # Penggugur: bila funding_cdn.py TIDAK ikut dicap, sidik dua-berkas akan
    # sama dengan sidik modul, dan pemecahan tadi menyembunyikan perubahan.
    assert funding.sidik_kode() != _sidik(["arsip.py", "funding.py"])
