"""Klien arsip publik data.binance.vision untuk USDS-M futures.

Ditulis untuk repo ini (bukan pengangkatan tier A). Empat sifat arsip di bawah
DIKLAIM berdasarkan pembacaan klien serupa di jalur riset lain dan WAJIB
terbukti sendiri saat workflow probe berjalan; laporan probe mencatat hasilnya:

1. Prefix `data/` wajib; tanpa itu S3 menjawab NoSuchKey.
2. Nama berkas harus dipertahankan apa adanya, karena berkas `.CHECKSUM`
   memuat nama berkas.
3. `fapi.binance.com` menjawab 451 dari runner GitHub; hanya arsip S3 yang dipakai.
4. Nama simbol wajib di-percent-encode saat menyusun URL CDN; arsip pernah
   memuat simbol non-ASCII, dan listing bisa lolos sementara unduhannya gagal.

Hanya pustaka baku yang dipakai: runner tidak punya `requests`.
"""
from __future__ import annotations

import hashlib
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

S3 = "https://s3-ap-northeast-1.amazonaws.com/data.binance.vision"
CDN = "https://data.binance.vision"
AKAR = "data/futures/um"
NS = {"s3": "http://s3.amazonaws.com/doc/2006-03-01/"}
UA = {"User-Agent": "lux-ai-research/0.1 (riset kuantitatif, arsip publik)"}


def segmen(teks: str) -> str:
    """Percent-encode satu segmen path URL; simbol tidak boleh memuat pemisah path."""
    return urllib.parse.quote(teks, safe="")


def ambil(url: str, timeout: int = 90, ulang: int = 5) -> bytes:
    """Ambil URL dengan backoff eksponensial; kegagalan permanen dilempar.

    Kegagalan TIDAK BOLEH diam-diam menghasilkan data tidak lengkap.
    """
    jeda = 1.0
    terakhir: Exception | None = None
    for _ in range(ulang):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except Exception as exc:  # noqa: BLE001
            terakhir = exc
            time.sleep(jeda)
            jeda = min(jeda * 2, 30.0)
    raise RuntimeError(f"gagal mengambil {url}: {terakhir}")


def _halaman(prefix: str, pemisah: str = "/"):
    """Iterasi seluruh halaman listing S3 sampai pagination habis."""
    token = None
    while True:
        q = {
            "list-type": "2",
            "max-keys": "1000",
            "prefix": prefix,
            "delimiter": pemisah,
        }
        if token:
            q["continuation-token"] = token
        akar = ET.fromstring(ambil(S3 + "?" + urllib.parse.urlencode(q)))
        yield akar
        if akar.findtext("s3:IsTruncated", "false", NS) != "true":
            return
        token = akar.findtext("s3:NextContinuationToken", None, NS)
        if not token:
            return


def daftar_prefix(prefix: str) -> list:
    hasil = []
    for akar in _halaman(prefix):
        hasil += [e.text for e in akar.findall("s3:CommonPrefixes/s3:Prefix", NS)]
    return hasil


def daftar_kunci(prefix: str) -> list:
    hasil = []
    for akar in _halaman(prefix, pemisah=""):
        hasil += [e.text for e in akar.findall("s3:Contents/s3:Key", NS)]
    return hasil


def semesta_simbol(jenis: str = "klines") -> list:
    """Semua simbol yang PERNAH ada di arsip bulanan, termasuk yang delisting.

    Inilah satu-satunya sumber daftar simbol yang sah di repo ini. Mengambil
    daftar pair aktif akan memasukkan bias keselamatan-hidup.
    """
    basis = f"{AKAR}/monthly/{jenis}/"
    return sorted(p[len(basis):].strip("/") for p in daftar_prefix(basis))


def bulan_tersedia(simbol: str, interval: str = "1m", jenis: str = "klines") -> list:
    """Bulan yang tersedia untuk satu simbol, format YYYY-MM."""
    if jenis == "klines":
        basis = f"{AKAR}/monthly/klines/{simbol}/{interval}/"
    else:
        basis = f"{AKAR}/monthly/{jenis}/{simbol}/"
    bulan = set()
    for kunci in daftar_kunci(basis):
        nama = kunci.rsplit("/", 1)[-1]
        if not nama.endswith(".zip"):
            continue
        bagian = nama[:-4].split("-")
        if len(bagian) >= 2:
            bulan.add(f"{bagian[-2]}-{bagian[-1]}")
    return sorted(bulan)


def url_klines(simbol: str, interval: str, bulan: str) -> str:
    s = segmen(simbol)
    return f"{CDN}/{AKAR}/monthly/klines/{s}/{interval}/{s}-{interval}-{bulan}.zip"


def url_funding(simbol: str, bulan: str) -> str:
    s = segmen(simbol)
    return f"{CDN}/{AKAR}/monthly/fundingRate/{s}/{s}-fundingRate-{bulan}.zip"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def checksum_arsip(url: str) -> str:
    """sha256 resmi dari berkas `.CHECKSUM` milik arsip."""
    return ambil(url + ".CHECKSUM", timeout=60).decode().split()[0].strip()


def unduh_terverifikasi(url: str) -> bytes:
    """Unduh ke memori dan cocokkan dengan checksum resmi arsip.

    Pecahan yang checksum-nya tidak cocok dianggap TIDAK ADA (aturan T1).
    """
    data = ambil(url, timeout=300)
    diharapkan = checksum_arsip(url)
    nyata = sha256_bytes(data)
    if nyata != diharapkan:
        raise RuntimeError(f"checksum tidak cocok untuk {url}: {nyata} != {diharapkan}")
    return data


def simpan(data: bytes, tujuan: str) -> Path:
    p = Path(tujuan)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data)
    return p
