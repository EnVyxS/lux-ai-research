"""Sebut NAMA keenam lubang funding berbentuk TENGAH — tanpa menyentuh jaringan.

Tiga bentuk lubang funding sudah terjelaskan, satu belum. `silang_funding` V2
menerbitkan sebaran bentuk lokal atas 877 lubang yang jatuh di dalam penyebut
19.586: **awal 45, ekor 826, tengah 6, seluruh 0**. Bentuk *ekor* terjelaskan
oleh kematian pasar (lubang -> mati 96,0%); bentuk *awal* terjelaskan oleh
penerbitan funding yang menyusul penerbitan klines (33 simbol-bulan HIDUP tanpa
funding SEMUANYA berbentuk awal). Yang **tengah** tidak terjelaskan oleh
keduanya: pasar itu punya funding sebelumnya DAN punya funding sesudahnya,
namun bolong di tengah.

Enam simbol-bulan bukan angka besar, tetapi Keputusan 7 ADR-A008 tidak boleh
diambil selagi ada bentuk cacat yang belum bernama. Modul ini menyebut namanya.

## Mengapa modul BARU, bukan `silang_funding` V3

`silang_funding.py` sudah 396 baris pada V1 dan belum diukur ulang pada V2;
pagar baris 800 dan aturan 48 melarang menumpuk fungsi pada berkas yang sudah
besar. Seluruh alat yang dibutuhkan sudah ada dan sudah diuji di sana
(`baca_laporan_kehidupan`, `baca_medan_baris`, `lubang_funding`,
`bulan_per_simbol`, `bentuk_lubang_lokal`, `kendali_silang`), jadi modul ini
MEMAKAINYA, tidak menyalinnya. Definisi bentuk karena itu tetap SATU (aturan
36); tidak ada definisi kedua yang bisa diam-diam menyimpang.

## Tidak ada unduhan

Bahannya `reports/kehidupan_arsip_<0..7>.json` dan
`reports/funding_semesta.json`, keduanya sudah di-commit. Satu job ringan.

## Uji H-A010 — dan batas yang jujur

H-A010: "arsip funding menyusul arsip klines" — funding sebuah simbol mulai
diterbitkan SESUDAH klines-nya. Ujinya di sini memakai definisi LOKAL:
`bulan_berfunding_pertama` adalah bulan klines paling awal simbol itu yang TIDAK
berlubang. H-A010 MENANG hanya bila kelima simbol pemilik 33 lubang HIDUP
(ICPUSDT, TLMUSDT, BNXUSDT, JUPUSDT, QTUMUSDT) punya
`bulan_berfunding_pertama` yang lebih besar daripada `bulan_klines_pertama`.
Satu simbol saja yang tidak, hipotesis itu gugur.

**Batasnya wajib disebut:** definisi ini tidak dapat melihat bulan funding yang
ada SEBELUM klines pertama, sebab penyebutnya adalah bulan klines. Karena itu
laporan ini juga menerbitkan `medan_per_simbol_funding_terlihat` apa adanya —
bila kelak terbukti ada medan yang memuat bulan funding pertama sesungguhnya,
uji ini wajib diulang dengan medan itu. Yang dilaporkan sekarang adalah bentuk
irisannya, bukan tanggal penerbitan arsip Binance (aturan 20).

## Penggugur (aturan 24)

`selisih_lubang_tengah` membandingkan cacah yang baru dibangun dengan **6** yang
sudah diterbitkan `silang_funding` V2 pada run 30434948267. Bukan nol berarti
bahan bakunya berubah dan seluruh laporan batal (kode 2). Kendali positif
`silang_funding.kendali_silang` dipakai apa adanya: tiga simbol-bulan
berparquet terbesar wajib HIDUP dan wajib berfunding (aturan 50).

## Praregistrasi ramalan — ditulis SEBELUM run

- **R-221** — CI pada commit yang menambahkan `tests/test_lubang_tengah.py`
  (sasaran dinyatakan menurut aturan 56) mengumpulkan **382 butir** dengan kode
  keluar **0**. Dasar: 340 butir terverifikasi pada run 30435672616, ditambah
  **42** butir dari berkas uji baru. Keempat puluh dua nama itu ditulis
  BERNOMOR di docstring `tests/test_lubang_tengah.py` pada commit yang sama
  (aturan 57, penangkal KC-19); tidak ada `parametrize` di berkas itu, sehingga
  cacah fungsi sama dengan cacah butir. 340 + 42 = **382**.
- **R-222** — `cacah_lubang_tengah` = **6** persis (`selisih_lubang_tengah` = 0)
  dan keenamnya berstatus **MATI**, yakni `sebaran_status_lubang_tengah` memuat
  MATI 6, SEPI 0, HIDUP 0, TAK_TERUKUR 0. Dasar: 33 lubang pada simbol-bulan
  HIDUP semuanya berbentuk awal, jadi tengah tidak mungkin HIDUP; SEPI hanya
  menyumbang 2 lubang dari 98 simbol-bulan. Ramalan ini GUGUR bila satu saja
  lubang tengah berstatus SEPI — dan bila itu terjadi, tafsir "lubang tengah
  adalah jeda perdagangan" justru menguat, bukan melemah.
- **R-223** — H-A010 **MENANG**: kelima simbol punya
  `bulan_berfunding_pertama` lebih besar daripada `bulan_klines_pertama`,
  yakni `cacah_menang` = 5 dan `cacah_gugur` = 0. Dasar: ke-33 lubang HIDUP
  seluruhnya berbentuk awal, dan bentuk awal menurut definisinya menuntut
  seluruh bulan terawal berlubang. Ramalan ini gugur bila ada simbol yang
  bulan pertamanya justru BERFUNDING — itu berarti lubang awalnya bukan sejak
  bulan pertama dan bentuk "awal" punya tafsir lain.

Aturan yang mengikat: 10, 20, 21, 22, 24, 30, 36, 41, 44, 45, 46, 47, 48, 50,
52, 53, 54, 56, 57.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from . import kehidupan, kehidupan_arsip, silang_funding

VERSI = 1
TOTAL_PECAHAN = kehidupan_arsip.TOTAL_PECAHAN
SUMBER_FUNDING = silang_funding.SUMBER_FUNDING
KELUARAN = "reports/lubang_tengah.json"
KENDALI_CACAH = silang_funding.KENDALI_CACAH
MEDAN_LILIN = silang_funding.MEDAN_LILIN

# Diterbitkan silang_funding V2 (run 30434948267): sebaran_bentuk_semua_lubang
# = {awal 45, ekor 826, tengah 6, seluruh 0}. Dipakai sebagai PENGGUGUR.
TENGAH_TERCATAT = 6

# Pemilik ke-33 lubang pada simbol-bulan HIDUP, menurut daftar terbitan V2.
SIMBOL_H_A010 = ["BNXUSDT", "ICPUSDT", "JUPUSDT", "QTUMUSDT", "TLMUSDT"]

BERKAS_DICAP = [
    "kehidupan.py",
    "kehidupan_arsip.py",
    "lubang_tengah.py",
    "silang_funding.py",
]

Kunci = Tuple[str, str]


def nama_keluaran() -> str:
    return KELUARAN


def sidik_kode() -> str:
    """Aturan 22: cap setiap berkas yang ikut menentukan angka ini."""
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(BERKAS_DICAP):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def medan_per_simbol(funding: Dict[str, Any]) -> Tuple[List[str], int]:
    """Medan yang benar-benar ada pada `per_simbol` — dilapor, tidak ditebak."""
    terlihat: Set[str] = set()
    cacah = 0
    for baris in funding.get("per_simbol") or []:
        cacah += 1
        terlihat.update(str(m) for m in baris.keys())
    return sorted(terlihat), cacah


def _berlubang_per_simbol(lubang: Set[Kunci]) -> Dict[str, Set[str]]:
    keluar: Dict[str, Set[str]] = {}
    for simbol, bulan in lubang:
        keluar.setdefault(str(simbol), set()).add(str(bulan))
    return keluar


def bulan_berfunding(bulan_urut: List[str], bulan_berlubang: Set[str]) -> List[str]:
    """Bulan klines yang PUNYA funding, urut naik."""
    return [b for b in sorted(bulan_urut) if b not in bulan_berlubang]


def tetangga_berfunding(
    bulan_urut: List[str], bulan_berlubang: Set[str], bulan: str
) -> Tuple[Optional[str], Optional[str]]:
    """Bulan berfunding terdekat sebelum dan sesudah sebuah bulan.

    Ujung riwayat menghasilkan null, bukan bulan palsu (aturan 46).
    """
    berfunding = bulan_berfunding(bulan_urut, bulan_berlubang)
    sebelum = [b for b in berfunding if b < bulan]
    sesudah = [b for b in berfunding if b > bulan]
    return (sebelum[-1] if sebelum else None, sesudah[0] if sesudah else None)


def panjang_rentetan(
    bulan_urut: List[str], bulan_berlubang: Set[str], bulan: str
) -> int:
    """Panjang rentetan lubang berurutan yang memuat `bulan`; 0 bila bukan lubang."""
    urut = sorted(bulan_urut)
    if bulan not in urut or bulan not in bulan_berlubang:
        return 0
    i = urut.index(bulan)
    kiri = kanan = i
    while kiri - 1 >= 0 and urut[kiri - 1] in bulan_berlubang:
        kiri -= 1
    while kanan + 1 < len(urut) and urut[kanan + 1] in bulan_berlubang:
        kanan += 1
    return kanan - kiri + 1


def daftar_lubang_tengah(
    status: Dict[Kunci, str],
    byte_parquet: Dict[Kunci, int],
    lubang: Set[Kunci],
    lilin: Optional[Dict[Kunci, Any]] = None,
) -> List[Dict[str, Any]]:
    """Daftar bernama lubang berbentuk TENGAH, memakai definisi silang_funding."""
    lilin = lilin or {}
    per_simbol = silang_funding.bulan_per_simbol(status)
    berlubang = _berlubang_per_simbol(lubang)
    baris: List[Dict[str, Any]] = []
    for k in sorted(lubang & set(status)):
        simbol, bulan = k
        urut = per_simbol.get(simbol, [])
        bl = berlubang.get(simbol, set())
        if silang_funding.bentuk_lubang_lokal(urut, bl, bulan) != "tengah":
            continue
        sebelum, sesudah = tetangga_berfunding(urut, bl, bulan)
        baris.append(
            {
                "simbol": simbol,
                "bulan": bulan,
                "status": status.get(k),
                "bentuk_lubang_lokal": "tengah",
                "bulan_berfunding_sebelum": sebelum,
                "bulan_berfunding_sesudah": sesudah,
                "panjang_rentetan_lubang": panjang_rentetan(urut, bl, bulan),
                "byte_parquet": int(byte_parquet.get(k) or 0),
                "cacah_lilin": lilin.get(k),
                "cacah_bulan_klines_simbol": len(urut),
                "cacah_lubang_simbol": len(bl & set(urut)),
                "bulan_klines_pertama": urut[0] if urut else None,
                "bulan_klines_terakhir": urut[-1] if urut else None,
            }
        )
    return baris


def sebaran_status(baris: List[Dict[str, Any]]) -> Dict[str, int]:
    """Cacah status; keempat kelas dilapor walau nol."""
    keluar: Dict[str, int] = {
        st: 0
        for st in (
            kehidupan.STATUS_MATI,
            kehidupan.STATUS_SEPI,
            kehidupan.STATUS_HIDUP,
            kehidupan.STATUS_TAK_TERUKUR,
        )
    }
    for r in baris:
        nama = str(r.get("status"))
        keluar[nama] = keluar.get(nama, 0) + 1
    return keluar


def uji_h_a010(
    status: Dict[Kunci, str],
    lubang: Set[Kunci],
    simbol: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """H-A010: funding menyusul klines. MENANG hanya bila SEMUA simbol setuju."""
    daftar = sorted(simbol if simbol is not None else SIMBOL_H_A010)
    per_simbol = silang_funding.bulan_per_simbol(status)
    berlubang = _berlubang_per_simbol(lubang)
    baris: List[Dict[str, Any]] = []
    menang = gugur = tak_terukur = 0
    for s in daftar:
        urut = per_simbol.get(s, [])
        berfunding = bulan_berfunding(urut, berlubang.get(s, set())) if urut else []
        pertama = berfunding[0] if berfunding else None
        if not urut or pertama is None:
            menyusul: Optional[bool] = None
            tak_terukur += 1
        else:
            menyusul = pertama > urut[0]
            if menyusul:
                menang += 1
            else:
                gugur += 1
        baris.append(
            {
                "simbol": s,
                "bulan_klines_pertama": urut[0] if urut else None,
                "bulan_berfunding_pertama": pertama,
                "funding_menyusul": menyusul,
                "cacah_bulan_klines_simbol": len(urut),
                "cacah_lubang_simbol": len(berlubang.get(s, set()) & set(urut)),
            }
        )
    return {
        "baris": baris,
        "cacah_simbol": len(baris),
        "cacah_menang": menang,
        "cacah_gugur": gugur,
        "cacah_tak_terukur": tak_terukur,
        "menang": bool(baris) and menang == len(baris),
    }


def kode_keluar(ringkasan: Dict[str, Any]) -> int:
    """Kode 2 bila laporan ini tidak berhak diklaim sebagai pengukuran."""
    if not ringkasan.get("sidik_seragam"):
        return 2
    if int(ringkasan.get("cacah_laporan_dibaca") or 0) != int(
        ringkasan.get("total_pecahan") or TOTAL_PECAHAN
    ):
        return 2
    if int(ringkasan.get("cacah_kunci_ganda") or 0) > 0:
        return 2
    if not ringkasan.get("kendali_sah"):
        return 2
    if int(ringkasan.get("selisih_lubang_tengah") or 0) != 0:
        return 2
    return 0


def jalankan(akar: str = ".", total: int = TOTAL_PECAHAN) -> Dict[str, Any]:
    status, byte_parquet, meta = silang_funding.baca_laporan_kehidupan(
        akar=akar, total=total
    )
    lilin, meta_lilin = silang_funding.baca_medan_baris(
        akar=akar, total=total, medan=MEDAN_LILIN
    )
    mentah = (Path(akar) / SUMBER_FUNDING).read_bytes()
    funding = json.loads(mentah.decode("utf-8"))

    lubang, meta_lubang = silang_funding.lubang_funding(funding)
    medan_funding, cacah_per_simbol = medan_per_simbol(funding)
    tengah = daftar_lubang_tengah(status, byte_parquet, lubang, lilin)
    h_a010 = uji_h_a010(status, lubang)
    kendali = silang_funding.kendali_silang(byte_parquet, status, lubang)

    ringkasan: Dict[str, Any] = {
        "penyebut_kehidupan": len(status),
        "cacah_lubang_tengah": len(tengah),
        "selisih_lubang_tengah": len(tengah) - TENGAH_TERCATAT,
        "sebaran_status_lubang_tengah": sebaran_status(tengah),
        "medan_per_simbol_funding_terlihat": medan_funding,
        "cacah_per_simbol_funding": cacah_per_simbol,
        "h_a010_menang": h_a010["menang"],
        "h_a010_cacah_menang": h_a010["cacah_menang"],
        "h_a010_cacah_gugur": h_a010["cacah_gugur"],
        "h_a010_cacah_tak_terukur": h_a010["cacah_tak_terukur"],
        "kendali": kendali,
        "kendali_sah": silang_funding.kendali_sah(kendali),
    }
    ringkasan.update(meta)
    ringkasan.update(meta_lilin)
    ringkasan.update(meta_lubang)

    return {
        "bukan_bukti": False,
        "versi_lubang_tengah": VERSI,
        "sidik_kode": sidik_kode(),
        "sidik_kode_silang_funding": silang_funding.sidik_kode(),
        "sidik_data_funding": hashlib.sha256(mentah).hexdigest(),
        "versi_funding": funding.get("versi_funding"),
        "sumber": [SUMBER_FUNDING]
        + [kehidupan_arsip.nama_keluaran(i) for i in range(total)],
        "definisi": {
            "bentuk_lubang_lokal": (
                "dipakai apa adanya dari silang_funding.bentuk_lubang_lokal: "
                "tengah berarti ada bulan klines berfunding sebelum DAN sesudah "
                "lubang itu; definisinya SATU, tidak disalin ulang (aturan 36)"
            ),
            "bulan_berfunding_pertama": (
                "bulan klines paling awal simbol itu yang TIDAK berlubang; ini "
                "BUKAN tanggal penerbitan arsip funding Binance"
            ),
            "h_a010_menang": (
                "benar hanya bila SELURUH simbal yang diuji punya "
                "bulan_berfunding_pertama lebih besar daripada "
                "bulan_klines_pertama"
            ),
        },
        "baris_lubang_tengah": tengah,
        "h_a010": h_a010,
        "ringkasan": ringkasan,
        "catatan_batas_h_a010": (
            "penyebut uji ini adalah bulan KLINES, sehingga bulan funding yang "
            "ada sebelum klines pertama tidak terlihat; bila kelak terbukti ada "
            "medan yang memuat bulan funding pertama sesungguhnya, uji ini wajib "
            "diulang dengan medan itu (aturan 20)"
        ),
        "catatan_tafsir": (
            "lubang tengah yang berdampingan dengan bulan berfunding TIDAK "
            "membuktikan sebab apa pun; ia hanya menunjukkan bahwa ketiadaan "
            "funding di bulan itu tidak dapat dijelaskan oleh awal maupun akhir "
            "riwayat simbol (aturan 10)"
        ),
        "catatan_penggugur": (
            "sidik_seragam false, laporan pecahan kurang, kunci ganda, "
            "kendali_sah false, atau selisih_lubang_tengah bukan nol "
            "membatalkan seluruh angka (aturan 24)"
        ),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def main() -> int:
    laporan = jalankan()
    Path(KELUARAN).parent.mkdir(parents=True, exist_ok=True)
    teks = json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    Path(KELUARAN).write_text(teks, encoding="utf-8")
    print(teks)
    return kode_keluar(laporan["ringkasan"])


if __name__ == "__main__":
    raise SystemExit(main())
