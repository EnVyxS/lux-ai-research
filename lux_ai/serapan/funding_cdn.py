"""Permintaan langsung ke CDN untuk berkas funding.

Dipisahkan dari `funding.py` pada VERSI 6 karena berkas itu menembus pagar 800
baris dan menjatuhkan CI (818 baris, run 30410773363). Pemisahan ini murni
struktural: tidak satu pun perilaku di bawah ini berubah. Seluruh nama tetap
dapat dipanggil lewat modul `funding`, sehingga pemanggil dan uji lama tidak
perlu ditulis ulang.

Yang diukur di sini BUKAN ketersediaan menurut listing S3, melainkan jawaban
server atas permintaan berkas yang sesungguhnya. Keduanya bisa berbeda, dan
perbedaan itulah alasan blok ini ada.

Setiap permintaan kohort wajib berpasangan dengan permintaan kendali. Tanpa
kendali, kode 404 tidak dapat dibedakan dari jalur unduh yang rusak, dan
seluruh cacah kohort menjadi tak bermakna (aturan 24).

Aturan yang ditegakkan: 20, 22, 24, 46, 48.
"""

from __future__ import annotations

import hashlib
import urllib.error
import urllib.request
from typing import Any, Dict, List, Optional, Sequence, Tuple

from . import arsip

# Banyaknya pasang kohort-kendali yang diminta langsung ke CDN. Tiap pasang
# adalah dua permintaan, jadi sepuluh pasang = dua puluh permintaan; masih jauh
# di bawah biaya listing dan tidak mendekati batas waktu job 300 detik.
BATAS_UJI_CDN = 10

# Daftar cadangan, dipakai HANYA bila kohort terukur kosong (mis. saat modul
# dijalankan dengan FUNDING_BATAS_SIMBOL kecil). Ketiga pasang inilah yang
# diuji VERSI 4; dipertahankan supaya hasil lama tetap dapat direproduksi.
UJI_KOHORT: Tuple[Tuple[str, str], ...] = (
    ("FTMUSDT", "2025-07"),
    ("KLAYUSDT", "2025-07"),
    ("LOOMUSDT", "2025-07"),
)
UJI_KENDALI: Tuple[Tuple[str, str], ...] = (
    ("FTMUSDT", "2025-06"),
    ("KLAYUSDT", "2025-06"),
    ("LOOMUSDT", "2025-06"),
)


def periksa_url(url: str, timeout: int = 60) -> Dict[str, Any]:
    """Minta satu URL dan laporkan kode HTTP apa adanya.

    404 (server menjawab: tidak ada) dan galat jaringan (server tidak menjawab)
    adalah dua keadaan yang berbeda. Menyamakan keduanya persis kesalahan yang
    dilarang aturan 46, maka `kode_http` tetap None saat yang terjadi adalah
    galat, dan `galat` tetap None saat yang terjadi adalah 404.
    """
    baris: Dict[str, Any] = {
        "url": url,
        "kode_http": None,
        "byte": None,
        "checksum_sha256": None,
        "teks_awal": None,
        "galat": None,
    }
    try:
        with urllib.request.urlopen(url, timeout=timeout) as jawab:
            data = jawab.read()
            baris["kode_http"] = int(getattr(jawab, "status", 200) or 200)
            baris["byte"] = len(data)
            baris["checksum_sha256"] = hashlib.sha256(data).hexdigest()
            baris["teks_awal"] = data[:200].decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        baris["kode_http"] = int(exc.code)
    except Exception as exc:  # noqa: BLE001
        baris["galat"] = str(exc)[:200]
    return baris


def periksa_berkas_funding(simbol: str, bulan: str, peran: str) -> Dict[str, Any]:
    """Minta satu berkas funding langsung ke CDN, lalu cocokkan checksum resmi.

    `checksum_cocok` bernilai None bila berkas tidak terambil; None berarti
    "tidak dapat diperiksa", bukan "tidak cocok".
    """
    url = arsip.url_funding(simbol, bulan)
    baris = periksa_url(url)
    baris["simbol"] = simbol
    baris["bulan"] = bulan
    baris["peran"] = peran
    baris["checksum_cocok"] = None
    if baris["kode_http"] == 200 and baris["checksum_sha256"]:
        sidik = periksa_url(url + ".CHECKSUM")
        baris["kode_http_checksum"] = sidik["kode_http"]
        teks = sidik.get("teks_awal") or ""
        if sidik["kode_http"] == 200 and teks:
            baris["checksum_cocok"] = baris["checksum_sha256"] in teks.split()
    return baris


def ringkas_uji_cdn(
    kohort: List[Dict[str, Any]], kendali: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """Cacah hasil uji CDN, dengan kendali sebagai medan penggugur.

    Bila kendali tidak seluruhnya 200 dan cocok checksum, jalur unduh sendiri
    yang tidak dapat dipercaya, dan seluruh angka kohort di blok ini batal.
    """
    kendali_200 = sum(1 for b in kendali if b.get("kode_http") == 200)
    kendali_cocok = sum(1 for b in kendali if b.get("checksum_cocok") is True)
    sah = bool(kendali) and kendali_200 == len(kendali) and kendali_cocok == len(kendali)
    return {
        "cacah_kohort_diminta": len(kohort),
        "cacah_kohort_404": sum(1 for b in kohort if b.get("kode_http") == 404),
        "cacah_kohort_200": sum(1 for b in kohort if b.get("kode_http") == 200),
        "cacah_kohort_galat": sum(1 for b in kohort if b.get("galat")),
        "cacah_kendali_diminta": len(kendali),
        "cacah_kendali_200": kendali_200,
        "cacah_kendali_checksum_cocok": kendali_cocok,
        "kendali_sah": sah,
        "catatan": (
            "bila kendali_sah false, jalur unduh tidak terbukti bekerja dan "
            "seluruh cacah kohort di blok ini BATAL (aturan 24); 404 berarti "
            "server menjawab tidak ada, galat berarti server tidak menjawab, "
            "dan keduanya tidak boleh disamakan (aturan 46)"
        ),
    }


def jalankan_uji_cdn(
    pasangan: Optional[Sequence[Tuple[str, str, str]]] = None
) -> Dict[str, Any]:
    """Uji kohort dan kendali berdampingan; keduanya selalu dijalankan.

    Pasangan yang terpilih dari data lebih disukai daripada daftar tetap,
    karena daftar tetap dipilih tangan dan itu bias pilihan yang diakui.
    """
    if pasangan:
        kohort = [periksa_berkas_funding(s, bk, "kohort") for s, bk, _ in pasangan]
        kendali = [periksa_berkas_funding(s, bn, "kendali") for s, _, bn in pasangan]
        sumber = "kohort terukur"
    else:
        kohort = [periksa_berkas_funding(s, b, "kohort") for s, b in UJI_KOHORT]
        kendali = [periksa_berkas_funding(s, b, "kendali") for s, b in UJI_KENDALI]
        sumber = "daftar tetap"
    hasil = ringkas_uji_cdn(kohort, kendali)
    hasil["sumber_pasangan"] = sumber
    hasil["baris"] = [
        {
            m: b.get(m)
            for m in (
                "peran",
                "simbol",
                "bulan",
                "kode_http",
                "byte",
                "checksum_cocok",
                "galat",
            )
        }
        for b in kohort + kendali
    ]
    return hasil
