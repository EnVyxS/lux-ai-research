"""Adu keanggotaan kohort 38 funding lawan kohort 38 kehidupan.

Utang ukur 38. Modul ini TIDAK menghitung ulang apa pun dan TIDAK menulis ke
manifes mana pun. Ia hanya MEMBACA daftar anggota yang sudah tertulis di
laporan yang ada, lalu mengadukan keanggotaannya sebagai himpunan.

VERSI 2. Versi 1 gagal terukur pada sisi funding: ia hanya melihat larik
string di PUNCAK dokumen, sedangkan funding_semesta.json menyimpan anggota di
dalam struktur bersarang (mis. kohort_puncak, per_simbol, selisih_kohort).
Kegagalan itu ditulis, bukan ditutupi. Versi ini menelusuri dokumen sampai
kedalaman terbatas dan mengumpulkan nama simbol dari TIGA bentuk yang benar
benar ditemui, tanpa mengarang nama kunci mana pun.

Aturan yang ditegakkan:
- aturan 7  : keluaran selalu lahir, walau bahan tidak lengkap.
- aturan 16 : sebab kegagalan ditulis, bukan disembunyikan.
- aturan 20 : tidak ada pernyataan tentang apa pun di luar yang dibaca.
- aturan 21 : absen dibedakan dari null dan dari himpunan kosong.
- aturan 24 : penggugur ditulis tersurat.
- aturan 30 : tidak ada pembagian oleh nol.
- aturan 32 : sidik kode modul ikut diterbitkan.
- aturan 36 : nama kunci sumber TIDAK dikarang; jalur temuan dilaporkan apa
              adanya bersama bentuk yang membuatnya terkumpul.
- aturan 46 : batas tafsir ditulis di dalam laporan.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import os
from typing import Any

VERSI = 2

KELUARAN = "reports/adu_kohort.json"

SUMBER_FUNDING = "reports/funding_semesta.json"
SUMBER_KEHIDUPAN = "reports/kehidupan.json"
SUMBER_EKOR = "reports/kohort_ekor.json"

BERKAS_DICAP = ("adu_kohort.py",)

# Batas cetak daftar mentah supaya laporan tetap terbaca alat.
BATAS_DAFTAR = 64

# Jalur dengan anggota lebih banyak daripada ini tetap DICATAT cacahnya,
# tetapi tidak diadu satu per satu supaya laporan tidak meledak.
BATAS_ADU = 200

KEDALAMAN = 4

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


def simbol_ish(teks: Any) -> bool:
    return isinstance(teks, str) and teks.endswith(AKHIRAN)


def kumpulkan(
    simpul: Any,
    jalur: str,
    dalam: int,
    hasil: dict[str, dict[str, Any]],
) -> None:
    """Kumpulkan daftar nama simbol dari tiga bentuk yang benar benar ada."""
    if dalam > KEDALAMAN:
        return

    if isinstance(simpul, list) and simpul:
        # bentuk 1: larik string simbol
        if all(isinstance(x, str) for x in simpul) and any(
            simbol_ish(x) for x in simpul
        ):
            hasil[jalur] = {"bentuk": "larik_string", "nama": list(simpul)}
            return
        # bentuk 2: larik objek yang punya medan simbol
        if all(isinstance(x, dict) for x in simpul):
            for medan in ("simbol", "symbol"):
                nama = [x[medan] for x in simpul if simbol_ish(x.get(medan))]
                if nama:
                    hasil[f"{jalur}[].{medan}"] = {
                        "bentuk": "larik_objek",
                        "nama": nama,
                    }
                    break
        for i, anak in enumerate(simpul[:8]):
            kumpulkan(anak, f"{jalur}[{i}]", dalam + 1, hasil)
        return

    if isinstance(simpul, dict) and simpul:
        # bentuk 3: pemetaan yang KUNCInya adalah simbol
        kunci_simbol = [k for k in simpul if simbol_ish(k)]
        if kunci_simbol:
            hasil[f"{jalur}{{}}"] = {
                "bentuk": "kunci_pemetaan",
                "nama": list(kunci_simbol),
            }
            return
        for kunci, anak in simpul.items():
            kumpulkan(anak, f"{jalur}.{kunci}" if jalur else str(kunci), dalam + 1, hasil)


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
    }


def jalankan() -> dict[str, Any]:
    funding, galat_funding, byte_funding = baca_json(SUMBER_FUNDING)
    kehidupan, galat_kehidupan, byte_kehidupan = baca_json(SUMBER_KEHIDUPAN)
    ekor, galat_ekor, byte_ekor = baca_json(SUMBER_EKOR)

    temuan_funding: dict[str, dict[str, Any]] = {}
    temuan_kehidupan: dict[str, dict[str, Any]] = {}
    temuan_ekor: dict[str, dict[str, Any]] = {}
    kumpulkan(funding, "", 0, temuan_funding)
    kumpulkan(kehidupan, "", 0, temuan_kehidupan)
    kumpulkan(ekor, "", 0, temuan_ekor)

    sisi_kanan = temuan_kehidupan.get("simbol_diukur")
    kanan_absen = sisi_kanan is None
    kanan = list(sisi_kanan["nama"]) if sisi_kanan else []

    def adu_semua(temuan: dict[str, dict[str, Any]]) -> dict[str, Any]:
        keluar: dict[str, Any] = {}
        if kanan_absen:
            return keluar
        for jalur, isi in sorted(temuan.items()):
            nama = isi["nama"]
            if len(set(nama)) > BATAS_ADU:
                keluar[jalur] = {
                    "bentuk": isi["bentuk"],
                    "cacah_kiri_unik": len(set(nama)),
                    "tidak_diadu": True,
                    "sebab": f"lebih dari {BATAS_ADU} anggota",
                    "cacah_irisan": len(set(nama) & set(kanan)),
                    "cacah_hanya_kanan": len(set(kanan) - set(nama)),
                    "kanan_bagian_kiri": not (set(kanan) - set(nama)),
                }
                continue
            hasil = adu(nama, kanan)
            hasil["bentuk"] = isi["bentuk"]
            keluar[jalur] = hasil
        return keluar

    aduan_funding = adu_semua(temuan_funding)
    aduan_ekor = adu_semua(temuan_ekor)

    identik = sorted(
        j for j, h in aduan_funding.items() if h.get("himpunan_identik")
    )

    def ambil(muatan: Any, kunci: str) -> Any:
        if isinstance(muatan, dict) and kunci in muatan:
            nilai = muatan[kunci]
            if isinstance(nilai, (str, int, float, bool)) or nilai is None:
                return nilai
            return f"<{type(nilai).__name__}>"
        return None

    laporan: dict[str, Any] = {
        "versi_adu_kohort": VERSI,
        "waktu_utc": datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        "sidik_kode": sidik_kode(),
        "bukan_bukti": False,
        "kedalaman_telusur": KEDALAMAN,
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
        "jalur_funding": {
            j: {"bentuk": i["bentuk"], "cacah_unik": len(set(i["nama"]))}
            for j, i in sorted(temuan_funding.items())
        },
        "jalur_kehidupan": {
            j: {"bentuk": i["bentuk"], "cacah_unik": len(set(i["nama"]))}
            for j, i in sorted(temuan_kehidupan.items())
        },
        "jalur_ekor": {
            j: {"bentuk": i["bentuk"], "cacah_unik": len(set(i["nama"]))}
            for j, i in sorted(temuan_ekor.items())
        },
        "kanan_absen": kanan_absen,
        "kanan_nama": None if kanan_absen else "kehidupan.simbol_diukur",
        "kanan_cacah": len(kanan),
        "kanan_daftar": sorted(kanan)[:BATAS_DAFTAR],
        "cacah_simbol_kohort_funding": ambil(funding, "cacah_simbol_kohort"),
        "cacah_simbol_kohort_kehidupan": ambil(kehidupan, "cacah_simbol_kohort"),
        "cacah_simbol_kohort_ekor": ambil(ekor, "cacah_simbol_kohort"),
        "sumber_kohort_kehidupan": ambil(kehidupan, "sumber_kohort"),
        "sumber_kohort_ekor": ambil(ekor, "sumber_kohort"),
        "versi_funding": ambil(funding, "versi_funding"),
        "adu_funding_lawan_kehidupan": aduan_funding,
        "adu_ekor_lawan_kehidupan": aduan_ekor,
        "jalur_yang_identik": identik,
        "ada_yang_identik": bool(identik),
        "catatan_bukan_bukti": (
            "laporan ini membaca daftar anggota yang sudah tertulis; ia TIDAK "
            "mengunduh apa pun, TIDAK menjatuhkan simbol-bulan, dan TIDAK "
            "menulis ke manifes"
        ),
        "catatan_penggugur": (
            "galat != null pada sumber mana pun berarti aduan atas sumber itu "
            "TIDAK terukur dan DILARANG dibaca sebagai perbedaan; kanan_absen "
            "true berarti tidak ada aduan sama sekali; jalur_funding kosong "
            "berarti penelusuran sedalam kedalaman_telusur tidak menemukan "
            "daftar nama, sehingga adu TETAP BELUM TERUKUR dan DILARANG "
            "dibaca sebagai bukti perbedaan maupun kesamaan"
        ),
        "catatan_tafsir": (
            "himpunan_identik hanya menyatakan bahwa DAFTAR NAMA-nya sama. Ia "
            "TIDAK membuktikan bahwa kedua laporan mengukur hal yang sama, dan "
            "TIDAK membuat keduanya menjadi dua saksi bebas. Kesamaan yang "
            "lahir karena satu laporan MEMBACA laporan lain sebagai sumber "
            "kohort adalah kesamaan turunan, bukan kesaksian kedua"
        ),
    }
    return laporan


def main() -> int:
    os.makedirs(os.path.dirname(KELUARAN), exist_ok=True)
    laporan = jalankan()
    with open(KELUARAN, "w", encoding="utf-8") as f:
        json.dump(laporan, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    print(
        f"adu_kohort v{VERSI}: kanan={laporan['kanan_cacah']} "
        f"jalur_funding={list(laporan['jalur_funding'])} "
        f"identik={laporan['jalur_yang_identik']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
