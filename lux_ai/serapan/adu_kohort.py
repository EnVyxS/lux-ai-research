"""Adu keanggotaan kohort 38 funding lawan kohort 38 kehidupan.

Utang ukur 38. Modul ini TIDAK menghitung ulang apa pun dan TIDAK menulis ke
manifes mana pun. Ia hanya MEMBACA daftar anggota yang sudah tertulis di
laporan yang ada, lalu mengadukan keanggotaannya sebagai himpunan.

Aturan yang ditegakkan:
- aturan 7  : keluaran selalu lahir, walau bahan tidak lengkap.
- aturan 16 : sebab kegagalan ditulis, bukan disembunyikan.
- aturan 20 : tidak ada pernyataan tentang apa pun di luar yang dibaca.
- aturan 21 : absen dibedakan dari null dan dari himpunan kosong.
- aturan 24 : penggugur ditulis tersurat.
- aturan 30 : tidak ada pembagian oleh nol.
- aturan 32 : sidik kode modul ikut diterbitkan.
- aturan 36 : nama kunci sumber TIDAK dikarang; kunci puncak dilaporkan apa
              adanya dan daftar kandidat ditemukan dari BENTUK nilainya.
- aturan 46 : batas tafsir ditulis di dalam laporan.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import os
from typing import Any

VERSI = 1

KELUARAN = "reports/adu_kohort.json"

SUMBER_FUNDING = "reports/funding_semesta.json"
SUMBER_KEHIDUPAN = "reports/kehidupan.json"
SUMBER_EKOR = "reports/kohort_ekor.json"

BERKAS_DICAP = ("adu_kohort.py",)

# Batas cetak daftar mentah supaya laporan tetap terbaca alat.
BATAS_DAFTAR = 64

# Sebuah nilai dianggap KANDIDAT daftar kohort bila ia larik berisi hanya
# string, dan setidaknya satu di antaranya berakhiran akhiran pasar berikut.
AKHIRAN = ("USDT",)


def sidik_kode() -> str:
    akar = os.path.dirname(os.path.abspath(__file__))
    cerna = hashlib.sha256()
    for nama in sorted(BERKAS_DICAP):
        jalan = os.path.join(akar, nama)
        with open(jalan, "rb") as f:
            cerna.update(f.read())
    return cerna.hexdigest()


def baca_json(jalan: str) -> tuple[Any, str | None, int]:
    try:
        byte = os.path.getsize(jalan)
    except OSError as galat:
        return None, f"tidak ada: {galat}", 0
    try:
        with open(jalan, "r", encoding="utf-8") as f:
            return json.load(f), None, byte
    except Exception as galat:  # noqa: BLE001 - sebab wajib terbaca
        return None, f"rusak: {type(galat).__name__}: {galat}", byte


def daftar_kandidat(muatan: Any) -> dict[str, list[str]]:
    """Temukan daftar simbol di puncak dokumen tanpa mengarang nama kunci."""
    hasil: dict[str, list[str]] = {}
    if not isinstance(muatan, dict):
        return hasil
    for kunci, nilai in muatan.items():
        if not isinstance(nilai, list) or not nilai:
            continue
        if not all(isinstance(x, str) for x in nilai):
            continue
        if any(x.endswith(AKHIRAN) for x in nilai):
            hasil[kunci] = list(nilai)
    return hasil


def adu(kiri: list[str], kanan: list[str]) -> dict[str, Any]:
    a, b = set(kiri), set(kanan)
    hanya_kiri = sorted(a - b)
    hanya_kanan = sorted(b - a)
    irisan = sorted(a & b)
    return {
        "cacah_kiri": len(kiri),
        "cacah_kiri_unik": len(a),
        "cacah_kanan": len(kanan),
        "cacah_kanan_unik": len(b),
        "cacah_irisan": len(irisan),
        "cacah_hanya_kiri": len(hanya_kiri),
        "cacah_hanya_kanan": len(hanya_kanan),
        "himpunan_identik": (not hanya_kiri) and (not hanya_kanan) and bool(a),
        "kiri_bagian_kanan": (not hanya_kiri) and bool(a),
        "kanan_bagian_kiri": (not hanya_kanan) and bool(b),
        "hanya_kiri": hanya_kiri[:BATAS_DAFTAR],
        "hanya_kanan": hanya_kanan[:BATAS_DAFTAR],
        "irisan": irisan[:BATAS_DAFTAR],
        "urutan_sama": list(kiri) == list(kanan),
    }


def jalankan() -> dict[str, Any]:
    funding, galat_funding, byte_funding = baca_json(SUMBER_FUNDING)
    kehidupan, galat_kehidupan, byte_kehidupan = baca_json(SUMBER_KEHIDUPAN)
    ekor, galat_ekor, byte_ekor = baca_json(SUMBER_EKOR)

    kandidat_funding = daftar_kandidat(funding)
    kandidat_kehidupan = daftar_kandidat(kehidupan)
    kandidat_ekor = daftar_kandidat(ekor)

    # Sisi kanan adu: daftar anggota kohort yang SUDAH terukur di kehidupan.
    kanan = kandidat_kehidupan.get("simbol_diukur")
    kanan_absen = kanan is None
    kanan = list(kanan or [])

    aduan = {
        nama: adu(daftar, kanan)
        for nama, daftar in sorted(kandidat_funding.items())
        if not kanan_absen
    }

    aduan_ekor = {}
    for nama, daftar in sorted(kandidat_ekor.items()):
        if not kanan_absen:
            aduan_ekor[nama] = adu(daftar, kanan)

    cocok_penuh = sorted(n for n, h in aduan.items() if h["himpunan_identik"])

    def cacah(muatan: Any, kunci: str) -> Any:
        if isinstance(muatan, dict) and kunci in muatan:
            return muatan[kunci]
        return None

    laporan: dict[str, Any] = {
        "versi_adu_kohort": VERSI,
        "waktu_utc": datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        "sidik_kode": sidik_kode(),
        "bukan_bukti": False,
        "sumber": {
            "funding": {
                "jalan": SUMBER_FUNDING,
                "byte": byte_funding,
                "galat": galat_funding,
            },
            "kehidupan": {
                "jalan": SUMBER_KEHIDUPAN,
                "byte": byte_kehidupan,
                "galat": galat_kehidupan,
            },
            "ekor": {
                "jalan": SUMBER_EKOR,
                "byte": byte_ekor,
                "galat": galat_ekor,
            },
        },
        "kunci_atas_funding": sorted(funding.keys())
        if isinstance(funding, dict)
        else None,
        "kunci_atas_kehidupan": sorted(kehidupan.keys())
        if isinstance(kehidupan, dict)
        else None,
        "kunci_atas_ekor": sorted(ekor.keys()) if isinstance(ekor, dict) else None,
        "nama_kandidat_funding": sorted(kandidat_funding),
        "nama_kandidat_kehidupan": sorted(kandidat_kehidupan),
        "nama_kandidat_ekor": sorted(kandidat_ekor),
        "cacah_kandidat_funding": {
            n: len(v) for n, v in sorted(kandidat_funding.items())
        },
        "kanan_absen": kanan_absen,
        "kanan_nama": None if kanan_absen else "kehidupan.simbol_diukur",
        "kanan_cacah": len(kanan),
        "kanan_daftar": sorted(kanan)[:BATAS_DAFTAR],
        "cacah_simbol_kohort_funding": cacah(funding, "cacah_simbol_kohort"),
        "cacah_simbol_kohort_kehidupan": cacah(kehidupan, "cacah_simbol_kohort"),
        "cacah_simbol_kohort_ekor": cacah(ekor, "cacah_simbol_kohort"),
        "sumber_kohort_kehidupan": cacah(kehidupan, "sumber_kohort"),
        "sumber_kohort_ekor": cacah(ekor, "sumber_kohort"),
        "adu_funding_lawan_kehidupan": aduan,
        "adu_ekor_lawan_kehidupan": aduan_ekor,
        "nama_yang_identik": cocok_penuh,
        "ada_yang_identik": bool(cocok_penuh),
        "catatan_bukan_bukti": (
            "laporan ini membaca daftar anggota yang sudah tertulis; ia TIDAK "
            "mengunduh apa pun, TIDAK menjatuhkan simbol-bulan, dan TIDAK "
            "menulis ke manifes"
        ),
        "catatan_penggugur": (
            "galat != null pada sumber mana pun berarti aduan atas sumber itu "
            "TIDAK terukur dan DILARANG dibaca sebagai perbedaan; kanan_absen "
            "true berarti tidak ada aduan sama sekali; nama_kandidat kosong "
            "berarti daftar anggota tidak tersimpan di puncak dokumen dan "
            "harus dicari di tempat lain, bukan disimpulkan"
        ),
        "catatan_tafsir": (
            "himpunan_identik hanya menyatakan bahwa DAFTAR NAMA-nya sama. Ia "
            "TIDAK membuktikan bahwa kedua laporan mengukur hal yang sama, dan "
            "TIDAK membuat keduanya menjadi dua saksi bebas"
        ),
    }
    return laporan


def main() -> int:
    os.makedirs(os.path.dirname(KELUARAN), exist_ok=True)
    laporan = jalankan()
    with open(KELUARAN, "w", encoding="utf-8") as f:
        json.dump(laporan, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    galat = [
        nama
        for nama, isi in laporan["sumber"].items()
        if isi["galat"] is not None
    ]
    print(f"adu_kohort v{VERSI}: kanan={laporan['kanan_cacah']} "
          f"identik={laporan['nama_yang_identik']} galat={galat}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
