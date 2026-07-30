"""Ukur BYTE PARQUET atas seluruh semesta 19.586 simbol-bulan - arah R-307.

Poros: H-A018, bukan H-A017. H-A017 adalah hipotesis ARAH SEBAB (LITUSDT) yang
sudah dicabut sebagai pola oleh ADR-A012 dan dibatasi lebih jauh oleh ADR-A013.
Besar byte parquet dulu hanya PENGAMATAN di ekor H-A017 (LITUSDT: bulan MATI
~390-434 ribu byte lawan bulan HIDUP ~1,6-1,9 juta), dan kini dinaikkan menjadi
hipotesis tersendiri agar dua hal berbeda tidak tercampur (KC-36, KC-41).

H-A018: besar `byte_parquet` per simbol-bulan berkorelasi dengan status
kehidupan; bulan MATI menempati bagian KECIL dari total byte semesta. Belum
pernah dijumlahkan sekali pun atas 19.586 simbol-bulan - itulah pekerjaan modul
ini.

## Mengapa poros ini dipilih sekarang

R-304, R-305, dan R-306 semuanya berujung pada satu peristiwa yang sama: tebing
funding `2025-07`. R-306 MENANG 3/3 namun klaim ilmiahnya hampir kosong karena
39 dari 40 anggota numerator berbagi bulan itu (KC-47, aturan 81). Poros
lubang/funding karena itu sudah kehabisan kejutan. Byte parquet adalah besaran
yang SAMA SEKALI LAIN: ia diukur dari berkas data, bukan dari daftar tanggal
funding, sehingga tidak dapat runtuh menjadi artefak `2025-07` yang itu-itu juga.

## Tanpa jaringan

Seluruh bahannya sudah di-commit. `byte_parquet` TIDAK dibaca dengan pembaca
baru: ia sudah dikembalikan oleh `silang_funding.baca_laporan_kehidupan`, yang
mengembalikan TIGA nilai (status, byte_parquet, meta). Berkas itu dan
`lubang_awal.py` DIBACA UTUH dari main pada giliran yang sama sebelum modul ini
ditulis (KC-43); tidak ada tanda tangan yang ditulis dari ingatan.

## Definisi yang dipakai (tersurat, aturan 47)

- `total_byte` = jumlah `byte_parquet` seluruh simbol-bulan DI DALAM penyebut
  19.586. Simbol-bulan di luar penyebut tidak ikut, dan tidak diam-diam dibuang:
  ia tidak pernah masuk karena penyebutnya memang laporan kehidupan itu sendiri.
- kelas ukur: `MATI` bila status MATI; `TERUKUR` bila HIDUP atau SEPI; `LAIN`
  untuk sisanya (mis. TAK_TERUKUR). Kelas `LAIN` DILARANG ikut butir 2.
- byte kecil: `byte_parquet` < `R307_AMBANG_BYTE_KECIL` (10.000), perbandingan
  STRIKT. Byte tepat 10.000 TIDAK dihitung kecil.

## Kendali positif dua lapis (aturan 50, KC-21)

Butir 2 dapat berujung pada cacah kecil atau nol, dan nol yang buta bukan
pengukuran. Karena itu:

1. kendali DATA: `silang_funding.kendali_silang` - tiga simbol-bulan berparquet
   terbesar, yang wajib HIDUP dan wajib punya funding.
2. kendali DETEKTOR: satu bentangan BUATAN berisi lima simbol-bulan dengan byte
   yang sudah diketahui jawabannya, termasuk satu baris tepat DI AMBANG (wajib
   tidak terhitung) dan satu baris kelas LAIN berbyte kecil (wajib TIDAK masuk
   butir 2). Bila detektor gagal memisahkan keduanya, `kendali_deteksi_sah`
   false dan kode keluar 2.

## Laporan sengaja RINGKAS (dasar usulan aturan 78)

`reports/lubang_tebing.json` terpotong saat dibaca (batas ~30.000 token) karena
daftar barisnya panjang, dan laporan yang tak terbaca utuh setara dengan laporan
yang tidak ada (aturan 52). Modul ini TIDAK menerbitkan 19.586 baris: hanya
agregat, sebaran per status, dan paling banyak `BATAS_BARIS_LAPORAN` (40) contoh
baris berbyte kecil. Daftar yang terpotong DILARANG dipakai sebagai daftar
lengkap (aturan 62, KC-24).

## Praregistrasi R-307 - DITULIS SEBELUM MODUL INI ADA (aturan 79)

Dikunci di `journal/2026-07-30-127.md` bagian 7, disalin apa adanya:

- butir 1 (BERISIKO): bagian byte parquet milik simbol-bulan MATI atas TOTAL
  byte seluruh 19.586, pita **0.02 .. 0.15**. Bila total byte 0, butir ini TIDAK
  TERADJUDIKASI (aturan 41).
- butir 2 (BERISIKO): cacah simbol-bulan TERUKUR (HIDUP atau SEPI) dengan
  `byte_parquet` < 10.000, pita **20 .. 400**.
- butir 3 (MUDAH): sembilan invarian penggugur tetap nol, kedua kendali sah,
  kode keluar 0, dan cacah uji CI diukur bukan diklaim.

Sembilan invarian penggugur: 19.586 penyebut, 787 simbol, 1.401 MATI, 8 bangkit,
877 lubang dalam penyebut, 880 lubang semesta, 122 ada_lubang, 5 lubang_awal,
118 lubang_bukan_awal.

Irisan BUKAN sebab (aturan 10): byte kecil yang berbarengan dengan status MATI
TIDAK membuktikan salah satu menyebabkan yang lain. Keduanya dapat lahir dari
satu delisting yang sama, dan besar berkas juga dipengaruhi pemadatan parquet.

Aturan yang mengikat: 10, 20, 21, 22, 24, 29, 36, 41, 44, 45, 46, 47, 50, 52,
54, 57, 62, 66, 74, 79, 80, 81.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from . import kehidupan, kehidupan_arsip, lubang_awal, silang_funding

VERSI = 1
KELUARAN = "reports/byte_semesta.json"
TOTAL_PECAHAN = kehidupan_arsip.TOTAL_PECAHAN

# Sembilan invarian yang SUDAH diterbitkan; penggugur, bukan masukan (aturan 24).
PENYEBUT_TERCATAT = 19586
SIMBOL_TERCATAT = 787
MATI_TERCATAT = 1401
BANGKIT_TERCATAT = 8
LUBANG_DALAM_PENYEBUT_TERCATAT = 877
LUBANG_SEMESTA_TERCATAT = 880
ADA_LUBANG_TERCATAT = 122
LUBANG_AWAL_TERCATAT = 5
LUBANG_BUKAN_AWAL_TERCATAT = 118

R307_PITA_BUTIR_1 = (0.02, 0.15)
R307_AMBANG_BYTE_KECIL = 10000
R307_PITA_BUTIR_2_CACAH = (20, 400)

KELAS_MATI = "MATI"
KELAS_TERUKUR = "TERUKUR"
KELAS_LAIN = "LAIN"
KELAS_UKUR = (KELAS_MATI, KELAS_TERUKUR, KELAS_LAIN)

BATAS_BARIS_LAPORAN = 40

MEDAN_SELISIH = (
    "selisih_penyebut",
    "selisih_simbol",
    "selisih_mati",
    "selisih_bangkit",
    "selisih_lubang_dalam_penyebut",
    "selisih_lubang_semesta",
    "selisih_ada_lubang",
    "selisih_lubang_awal",
    "selisih_lubang_bukan_awal",
)

BERKAS_DICAP = [
    "byte_semesta.py",
    "kehidupan.py",
    "kehidupan_arsip.py",
    "lubang_awal.py",
    "silang_funding.py",
]

Kunci = Tuple[str, str]


def nama_keluaran() -> str:
    return KELUARAN


def sidik_kode() -> str:
    """Aturan 22: cap tiap berkas yang ikut menentukan angka ini."""
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(BERKAS_DICAP):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def _bagian(a: int, b: int) -> Optional[float]:
    """Aturan 41/46: penyebut nol menghasilkan null, bukan nol."""
    return (a / b) if b else None


def kelas_ukur(status: str) -> str:
    """MATI, TERUKUR (HIDUP atau SEPI), atau LAIN. Kelas LAIN dilarang di butir 2."""
    if status == kehidupan.STATUS_MATI:
        return KELAS_MATI
    if status in (kehidupan.STATUS_HIDUP, kehidupan.STATUS_SEPI):
        return KELAS_TERUKUR
    return KELAS_LAIN


def himpun_byte(
    status: Dict[Kunci, str],
    byte_parquet: Dict[Kunci, int],
    ambang: int = R307_AMBANG_BYTE_KECIL,
) -> Dict[str, Any]:
    """Agregat byte parquet per kelas ukur; tiap cacah punya penyebut tersurat."""
    byte_kelas: Dict[str, int] = {k: 0 for k in KELAS_UKUR}
    cacah_kelas: Dict[str, int] = {k: 0 for k in KELAS_UKUR}
    kecil_kelas: Dict[str, int] = {k: 0 for k in KELAS_UKUR}
    cacah_nol = 0
    for k, st in status.items():
        kelas = kelas_ukur(str(st))
        b = int(byte_parquet.get(k) or 0)
        byte_kelas[kelas] = byte_kelas.get(kelas, 0) + b
        cacah_kelas[kelas] = cacah_kelas.get(kelas, 0) + 1
        if b < int(ambang):
            kecil_kelas[kelas] = kecil_kelas.get(kelas, 0) + 1
        if b == 0:
            cacah_nol += 1
    total = sum(byte_kelas.values())
    return {
        "total_byte": total,
        "byte_mati": byte_kelas[KELAS_MATI],
        "byte_terukur": byte_kelas[KELAS_TERUKUR],
        "byte_lain": byte_kelas[KELAS_LAIN],
        "bagian_byte_mati": _bagian(byte_kelas[KELAS_MATI], total),
        "bagian_byte_terukur": _bagian(byte_kelas[KELAS_TERUKUR], total),
        "cacah_mati": cacah_kelas[KELAS_MATI],
        "cacah_terukur": cacah_kelas[KELAS_TERUKUR],
        "cacah_lain": cacah_kelas[KELAS_LAIN],
        "cacah_terukur_byte_kecil": kecil_kelas[KELAS_TERUKUR],
        "cacah_mati_byte_kecil": kecil_kelas[KELAS_MATI],
        "cacah_lain_byte_kecil": kecil_kelas[KELAS_LAIN],
        "ambang_byte_kecil": int(ambang),
        "cacah_byte_nol": cacah_nol,
        "cacah_baris": len(status),
    }


def daftar_terukur_byte_kecil(
    status: Dict[Kunci, str],
    byte_parquet: Dict[Kunci, int],
    ambang: int = R307_AMBANG_BYTE_KECIL,
) -> List[Dict[str, Any]]:
    """Baris TERUKUR berbyte kecil, urut byte menaik lalu simbol-bulan."""
    baris: List[Dict[str, Any]] = []
    for k, st in status.items():
        if kelas_ukur(str(st)) != KELAS_TERUKUR:
            continue
        b = int(byte_parquet.get(k) or 0)
        if b >= int(ambang):
            continue
        baris.append(
            {"simbol": k[0], "bulan": k[1], "status": str(st), "byte_parquet": b}
        )
    baris.sort(key=lambda r: (int(r["byte_parquet"]), r["simbol"], r["bulan"]))
    return baris


def sebaran_byte_per_status(
    status: Dict[Kunci, str], byte_parquet: Dict[Kunci, int]
) -> Dict[str, Dict[str, Any]]:
    """Byte dan cacah per status APA ADANYA, agar kelas tak tersamar (aturan 62)."""
    keluar: Dict[str, Dict[str, Any]] = {}
    for k, st in status.items():
        sel = keluar.setdefault(
            str(st), {"cacah": 0, "byte": 0, "byte_min": None, "byte_maks": None}
        )
        b = int(byte_parquet.get(k) or 0)
        sel["cacah"] += 1
        sel["byte"] += b
        sel["byte_min"] = b if sel["byte_min"] is None else min(int(sel["byte_min"]), b)
        sel["byte_maks"] = b if sel["byte_maks"] is None else max(int(sel["byte_maks"]), b)
    for st in keluar:
        keluar[st]["byte_rata"] = _bagian(keluar[st]["byte"], keluar[st]["cacah"])
    return keluar


def kendali_deteksi(ambang: int = 50) -> Dict[str, Any]:
    """Kendali positif detektor: bentangan BUATAN yang jawabannya sudah diketahui.

    Dua perangkap dipasang dengan sengaja: satu baris tepat DI AMBANG (wajib
    TIDAK terhitung kecil, sebab perbandingannya strikt) dan satu baris kelas
    LAIN berbyte kecil (wajib TIDAK masuk butir 2).
    """
    m = kehidupan.STATUS_MATI
    h = kehidupan.STATUS_HIDUP
    s = kehidupan.STATUS_SEPI
    t = kehidupan.STATUS_TAK_TERUKUR
    status: Dict[Kunci, str] = {
        ("KENDALI_MATI", "2024-01"): m,
        ("KENDALI_HIDUP", "2024-01"): h,
        ("KENDALI_KECIL", "2024-01"): h,
        ("KENDALI_SEPI", "2024-01"): s,
        ("KENDALI_AMBANG", "2024-01"): h,
        ("KENDALI_LAIN", "2024-01"): t,
    }
    byte_parquet: Dict[Kunci, int] = {
        ("KENDALI_MATI", "2024-01"): 100,
        ("KENDALI_HIDUP", "2024-01"): 900,
        ("KENDALI_KECIL", "2024-01"): 10,
        ("KENDALI_SEPI", "2024-01"): 5,
        ("KENDALI_AMBANG", "2024-01"): int(ambang),
        ("KENDALI_LAIN", "2024-01"): 3,
    }
    agregat = himpun_byte(status, byte_parquet, ambang=ambang)
    kecil = daftar_terukur_byte_kecil(status, byte_parquet, ambang=ambang)
    nama_kecil = sorted(r["simbol"] for r in kecil)
    sah = bool(
        agregat["cacah_mati"] == 1
        and agregat["cacah_terukur"] == 4
        and agregat["cacah_lain"] == 1
        and agregat["byte_mati"] == 100
        and agregat["total_byte"] == 1018 + int(ambang)
        and agregat["cacah_terukur_byte_kecil"] == 2
        and agregat["cacah_lain_byte_kecil"] == 1
        and agregat["bagian_byte_mati"] is not None
        and nama_kecil == ["KENDALI_KECIL", "KENDALI_SEPI"]
    )
    return {
        "ambang_kendali": int(ambang),
        "agregat_kendali": agregat,
        "baris_kendali_kecil": kecil,
        "kendali_deteksi_sah": sah,
        "catatan": (
            "baris tepat di ambang wajib tidak terhitung kecil (perbandingan "
            "strikt) dan baris kelas LAIN berbyte kecil wajib tidak masuk butir 2"
        ),
    }


def dalam_pita(nilai: Optional[float], pita: Tuple[float, float]) -> bool:
    if nilai is None:
        return False
    return pita[0] <= nilai <= pita[1]


def uji_r307(agregat: Dict[str, Any], ringkasan: Dict[str, Any]) -> Dict[str, Any]:
    """Adjudikasi mesin terhadap pita praregistrasi jurnal 127 bagian 7."""
    total = int(agregat.get("total_byte") or 0)
    bagian = agregat.get("bagian_byte_mati")
    if total <= 0:
        butir_1 = "TIDAK_TERADJUDIKASI"
    elif dalam_pita(bagian, R307_PITA_BUTIR_1):
        butir_1 = "MENANG"
    else:
        butir_1 = "KALAH"
    cacah = int(agregat.get("cacah_terukur_byte_kecil") or 0)
    butir_2 = (
        "MENANG"
        if dalam_pita(
            float(cacah),
            (float(R307_PITA_BUTIR_2_CACAH[0]), float(R307_PITA_BUTIR_2_CACAH[1])),
        )
        else "KALAH"
    )
    butir_3 = bool(
        all(int(ringkasan.get(medan) or 0) == 0 for medan in MEDAN_SELISIH)
        and ringkasan.get("kendali_sah")
        and ringkasan.get("kendali_deteksi_sah")
    )
    return {
        "butir_1": butir_1,
        "butir_1_bagian": bagian,
        "butir_1_total_byte": total,
        "butir_1_pita": list(R307_PITA_BUTIR_1),
        "butir_2": butir_2,
        "butir_2_cacah": cacah,
        "butir_2_pita_cacah": list(R307_PITA_BUTIR_2_CACAH),
        "butir_2_ambang_byte": R307_AMBANG_BYTE_KECIL,
        "butir_3": butir_3,
        "catatan_butir_3": "MUDAH: hanya menyalin angka yang sudah terverifikasi",
        "catatan_butir_1": (
            "total byte 0 berarti TIDAK TERADJUDIKASI, bukan KALAH (aturan 41)"
        ),
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
    if not ringkasan.get("kendali_deteksi_sah"):
        return 2
    for medan in MEDAN_SELISIH:
        if int(ringkasan.get(medan) or 0) != 0:
            return 2
    return 0


def jalankan(akar: str = ".", total: Optional[int] = None) -> Dict[str, Any]:
    total = TOTAL_PECAHAN if total is None else total
    status, byte_parquet, meta = silang_funding.baca_laporan_kehidupan(
        akar=akar, total=total
    )
    mentah = (Path(akar) / silang_funding.SUMBER_FUNDING).read_bytes()
    funding = json.loads(mentah.decode("utf-8"))
    lubang, meta_lubang = silang_funding.lubang_funding(funding)

    berlubang: Dict[str, Set[str]] = {}
    for simbol, bulan in lubang:
        berlubang.setdefault(str(simbol), set()).add(str(bulan))

    peta = lubang_awal.peta_status(status)
    baris_simbol = [
        lubang_awal.ringkas(simbol, peta[simbol], berlubang.get(simbol, set()))
        for simbol in sorted(peta)
    ]
    agregat_lubang = lubang_awal.himpun(baris_simbol)

    agregat = himpun_byte(status, byte_parquet)
    kecil = daftar_terukur_byte_kecil(status, byte_parquet)
    kendali = silang_funding.kendali_silang(byte_parquet, status, lubang)
    kd = kendali_deteksi()

    cacah_mati = sum(1 for st in status.values() if st == kehidupan.STATUS_MATI)
    lubang_dalam = len(lubang & set(status))
    lubang_semesta = len(lubang)

    ringkasan: Dict[str, Any] = {
        "penyebut_kehidupan": len(status),
        "cacah_simbol": len(peta),
        "cacah_mati": cacah_mati,
        "cacah_bangkit": agregat_lubang["cacah_bangkit"],
        "cacah_lubang_dalam_penyebut": lubang_dalam,
        "cacah_lubang_semesta": lubang_semesta,
        "cacah_simbol_ada_lubang": agregat_lubang["cacah_simbol_ada_lubang"],
        "cacah_simbol_lubang_awal": agregat_lubang["cacah_simbol_lubang_awal"],
        "cacah_simbol_lubang_bukan_awal": agregat_lubang[
            "cacah_simbol_lubang_bukan_awal"
        ],
        "selisih_penyebut": len(status) - PENYEBUT_TERCATAT,
        "selisih_simbol": len(peta) - SIMBOL_TERCATAT,
        "selisih_mati": cacah_mati - MATI_TERCATAT,
        "selisih_bangkit": agregat_lubang["cacah_bangkit"] - BANGKIT_TERCATAT,
        "selisih_lubang_dalam_penyebut": lubang_dalam
        - LUBANG_DALAM_PENYEBUT_TERCATAT,
        "selisih_lubang_semesta": lubang_semesta - LUBANG_SEMESTA_TERCATAT,
        "selisih_ada_lubang": agregat_lubang["cacah_simbol_ada_lubang"]
        - ADA_LUBANG_TERCATAT,
        "selisih_lubang_awal": agregat_lubang["cacah_simbol_lubang_awal"]
        - LUBANG_AWAL_TERCATAT,
        "selisih_lubang_bukan_awal": agregat_lubang["cacah_simbol_lubang_bukan_awal"]
        - LUBANG_BUKAN_AWAL_TERCATAT,
        "sebaran_byte_per_status": sebaran_byte_per_status(status, byte_parquet),
        "kendali": kendali,
        "kendali_sah": silang_funding.kendali_sah(kendali),
        "kendali_deteksi_sah": kd["kendali_deteksi_sah"],
    }
    ringkasan.update(meta)
    ringkasan.update(meta_lubang)
    ringkasan.update(agregat)

    return {
        "bukan_bukti": False,
        "versi_byte_semesta": VERSI,
        "sidik_kode": sidik_kode(),
        "sidik_kode_silang_funding": silang_funding.sidik_kode(),
        "sidik_kode_lubang_awal": lubang_awal.sidik_kode(),
        "sidik_data_funding": hashlib.sha256(mentah).hexdigest(),
        "sumber": [silang_funding.SUMBER_FUNDING]
        + [kehidupan_arsip.nama_keluaran(i) for i in range(total)],
        "hipotesis": "H-A018",
        "definisi": {
            "total_byte": "jumlah byte_parquet seluruh simbol-bulan di dalam penyebut",
            "kelas_MATI": "status MATI",
            "kelas_TERUKUR": "status HIDUP atau SEPI",
            "kelas_LAIN": "sisanya, dilarang ikut butir 2",
            "byte_kecil": "byte_parquet < 10000, perbandingan STRIKT",
        },
        "praregistrasi_r307": {
            "jurnal": "journal/2026-07-30-127.md",
            "hipotesis": "H-A018",
            "pita_butir_1": list(R307_PITA_BUTIR_1),
            "pita_butir_2_cacah": list(R307_PITA_BUTIR_2_CACAH),
            "ambang_byte_kecil": R307_AMBANG_BYTE_KECIL,
            "butir_3": "MUDAH",
        },
        "baris_terukur_byte_kecil": kecil[:BATAS_BARIS_LAPORAN],
        "cacah_baris_terukur_byte_kecil_dilapor": len(kecil[:BATAS_BARIS_LAPORAN]),
        "cacah_baris_terukur_byte_kecil_seluruhnya": len(kecil),
        "kendali_deteksi": kd,
        "uji_r307": uji_r307(agregat, ringkasan),
        "ringkasan": ringkasan,
        "catatan_tafsir": (
            "irisan BUKAN sebab (aturan 10): byte kecil yang berbarengan dengan "
            "status MATI tidak membuktikan salah satu menyebabkan yang lain; "
            "besar berkas juga dipengaruhi pemadatan parquet, bukan hanya cacah lilin"
        ),
        "catatan_daftar": (
            "baris_terukur_byte_kecil dibatasi BATAS_BARIS_LAPORAN dan BUKAN daftar "
            "lengkap; pakai cacah_baris_terukur_byte_kecil_seluruhnya untuk cacah "
            "(aturan 62, KC-24)"
        ),
        "catatan_penggugur": (
            "sidik_seragam false, laporan pecahan kurang, kunci ganda, kendali data "
            "atau kendali detektor tidak sah, atau salah satu dari sembilan selisih "
            "bukan nol membatalkan seluruh angka (aturan 24)"
        ),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def main() -> int:
    laporan = jalankan()
    teks = json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    Path(KELUARAN).parent.mkdir(parents=True, exist_ok=True)
    Path(KELUARAN).write_text(teks, encoding="utf-8")
    print(teks)
    return kode_keluar(laporan["ringkasan"])


if __name__ == "__main__":
    raise SystemExit(main())
