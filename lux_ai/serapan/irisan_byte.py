"""irisan_byte V1 — R-308.

Poros H-A018. R-307 mengukur bahwa kelas MATI memegang 0,0177 dari byte
semesta dan rata-ratanya kira-kira 4,3 kali lebih kecil daripada HIDUP.
R-307 JUGA mengukur bahwa berkas TERKECIL di seluruh semesta (22.440 byte)
adalah berkas HIDUP, sedangkan berkas MATI terkecil 97.634 byte. Dua sebaran
itu BERIRISAN. Modul ini mengukur LEBAR irisan tersebut.

Ambang di modul ini RELATIF terhadap sebaran terukur R-307, bukan angka bulat
yang dikarang. Itu jawaban langsung atas KC-48: ambang 10.000 byte pada R-307
mustahil dilewati sehingga butir keduanya tidak pernah menguji alam.

DILARANG menyimpulkan "berkas kecil = mati" dari modul ini. Modul ini justru
dibangun untuk mengukur seberapa lebar zona tempat kesimpulan itu SALAH.
"""

from __future__ import annotations

import hashlib
import json
import os
from typing import Any, Dict, List, Mapping, Optional, Tuple

from lux_ai.serapan import kehidupan_arsip
from lux_ai.serapan import silang_funding

VERSI = 1
KELUARAN = "reports/irisan_byte.json"
BATAS_BARIS_LAPORAN = 40

KELAS_HIDUP = "HIDUP"
KELAS_SEPI = "SEPI"
KELAS_MATI = "MATI"
KELAS_LAIN = "LAIN"
KELAS_URUT = (KELAS_HIDUP, KELAS_SEPI, KELAS_MATI)

# Ambang butir 1: byte_min kelas MATI hasil ukur R-307.
AMBANG_HIDUP_KECIL = 97634
# Ambang butir 2: di bawah rata-rata MATI (413.306) tetapi di atas byte_min-nya.
AMBANG_MATI_KECIL = 150000

R308_PITA_BUTIR_1 = (20, 600)
R308_PITA_BUTIR_2 = (10, 300)

PENYEBUT_HIDUP_TERCATAT = 18087
PENYEBUT_MATI_TERCATAT = 1401

# Sembilan invarian. Berbeda isi dari sembilan milik byte_semesta: enam angka
# cacah/penyebut ditambah tiga jumlah byte per kelas. Tiga yang terakhir
# memeriksa ulang angka R-307 lewat jalur baca yang sama tetapi kode berbeda.
INVARIAN: Dict[str, int] = {
    "penyebut": 19586,
    "simbol": 787,
    "cacah_hidup": 18087,
    "cacah_sepi": 98,
    "cacah_mati": 1401,
    "total_byte": 32706262375,
    "byte_hidup": 32049492952,
    "byte_sepi": 77728024,
    "byte_mati": 579041399,
}
MEDAN_SELISIH: Tuple[str, ...] = tuple("selisih_" + nama for nama in INVARIAN)

# Kendali data: tiga baris terbesar semesta, semuanya HIDUP (R-307).
KENDALI_DATA: Dict[Tuple[str, str], int] = {
    ("BTCUSDT", "2021-05"): 2770666,
    ("BTCUSDT", "2021-08"): 2730341,
    ("BTCUSDT", "2021-01"): 2722266,
}

# Kendali deteksi: angka buatan, dipisah dari fungsi yang diuji.
DETEKSI_HIDUP = (5, 10, 1000)
DETEKSI_MATI = (7, 900)
DETEKSI_TOTAL = 1922


def nama_keluaran(akar: str = ".") -> str:
    return os.path.join(akar, KELUARAN)


def sidik_kode() -> str:
    with open(os.path.abspath(__file__), "rb") as berkas:
        return hashlib.sha256(berkas.read()).hexdigest()


def _bagian(kunci: Any) -> Tuple[str, str]:
    if isinstance(kunci, (tuple, list)) and len(kunci) >= 2:
        return str(kunci[0]).strip(), str(kunci[1]).strip()
    teks = str(kunci)
    for pemisah in ("|", "::", "#", "/", ":"):
        if pemisah in teks:
            kiri, kanan = teks.split(pemisah, 1)
            return kiri.strip(), kanan.strip()
    return teks.strip(), ""


def kelas_status(nilai: Any) -> str:
    teks = str(nilai).strip().upper()
    if teks in (KELAS_HIDUP, KELAS_SEPI, KELAS_MATI):
        return teks
    return KELAS_LAIN


def sebaran_per_kelas(
    status: Mapping[Any, Any], byte_parquet: Mapping[Any, Any]
) -> Dict[str, Dict[str, Any]]:
    hasil: Dict[str, Dict[str, Any]] = {}
    for kunci, nilai in status.items():
        byte = byte_parquet.get(kunci)
        if byte is None:
            continue
        angka = int(byte)
        kelas = kelas_status(nilai)
        simpul = hasil.setdefault(
            kelas, {"cacah": 0, "jumlah": 0, "min": None, "maks": None}
        )
        simpul["cacah"] += 1
        simpul["jumlah"] += angka
        simpul["min"] = angka if simpul["min"] is None else min(simpul["min"], angka)
        simpul["maks"] = angka if simpul["maks"] is None else max(simpul["maks"], angka)
    for simpul in hasil.values():
        cacah = simpul["cacah"]
        simpul["rata"] = round(simpul["jumlah"] / cacah, 3) if cacah else 0.0
    return hasil


def cacah_di_bawah(
    status: Mapping[Any, Any],
    byte_parquet: Mapping[Any, Any],
    kelas: str,
    ambang: int,
) -> int:
    batas = int(ambang)
    cacah = 0
    for kunci, nilai in status.items():
        if kelas_status(nilai) != kelas:
            continue
        byte = byte_parquet.get(kunci)
        if byte is None:
            continue
        if int(byte) < batas:
            cacah += 1
    return cacah


def daftar_kecil(
    status: Mapping[Any, Any],
    byte_parquet: Mapping[Any, Any],
    kelas: str,
    ambang: int,
    batas: int = BATAS_BARIS_LAPORAN,
) -> List[Dict[str, Any]]:
    baris: List[Dict[str, Any]] = []
    ambang_int = int(ambang)
    for kunci, nilai in status.items():
        if kelas_status(nilai) != kelas:
            continue
        byte = byte_parquet.get(kunci)
        if byte is None:
            continue
        angka = int(byte)
        if angka < ambang_int:
            simbol, bulan = _bagian(kunci)
            baris.append({"simbol": simbol, "bulan": bulan, "byte": angka})
    baris.sort(key=lambda r: (r["byte"], r["simbol"], r["bulan"]))
    return baris[: int(batas)]


def kendali_data(
    byte_parquet: Mapping[Any, Any],
    status: Optional[Mapping[Any, Any]] = None,
    harapan: Optional[Mapping[Tuple[str, str], int]] = None,
) -> Tuple[bool, List[Dict[str, Any]]]:
    acuan = KENDALI_DATA if harapan is None else harapan
    peta: Dict[Tuple[str, str], Any] = {}
    for kunci in byte_parquet:
        peta[_bagian(kunci)] = kunci
    sah = True
    rinci: List[Dict[str, Any]] = []
    for (simbol, bulan), harap in sorted(acuan.items()):
        kunci = peta.get((simbol, bulan))
        terukur = None if kunci is None else int(byte_parquet[kunci])
        kelas = None
        if kunci is not None and status is not None:
            kelas = kelas_status(status.get(kunci))
        cocok = terukur == int(harap) and (kelas is None or kelas == KELAS_HIDUP)
        sah = sah and cocok
        rinci.append(
            {
                "simbol": simbol,
                "bulan": bulan,
                "harap": int(harap),
                "terukur": terukur,
                "kelas": kelas,
                "cocok": bool(cocok),
            }
        )
    return bool(sah), rinci


def kendali_deteksi(ambang: int = 50) -> Tuple[bool, Dict[str, Any]]:
    batas = int(ambang)
    status = {
        ("AAA", "2024-01"): "HIDUP",
        ("AAA", "2024-02"): "HIDUP",
        ("AAA", "2024-03"): "HIDUP",
        ("BBB", "2024-01"): "MATI",
        ("BBB", "2024-02"): "MATI",
    }
    byte_parquet = {
        ("AAA", "2024-01"): DETEKSI_HIDUP[0],
        ("AAA", "2024-02"): DETEKSI_HIDUP[1],
        ("AAA", "2024-03"): DETEKSI_HIDUP[2],
        ("BBB", "2024-01"): DETEKSI_MATI[0],
        ("BBB", "2024-02"): DETEKSI_MATI[1],
    }
    hidup_kecil = cacah_di_bawah(status, byte_parquet, KELAS_HIDUP, batas)
    mati_kecil = cacah_di_bawah(status, byte_parquet, KELAS_MATI, batas)
    total = sum(int(nilai) for nilai in byte_parquet.values())
    harap_hidup = len([n for n in DETEKSI_HIDUP if n < batas])
    harap_mati = len([n for n in DETEKSI_MATI if n < batas])
    sah = (
        hidup_kecil == harap_hidup
        and mati_kecil == harap_mati
        and total == DETEKSI_TOTAL
    )
    return bool(sah), {
        "ambang": batas,
        "hidup_kecil": hidup_kecil,
        "mati_kecil": mati_kecil,
        "harap_hidup": harap_hidup,
        "harap_mati": harap_mati,
        "total_byte": total,
        "harap_total_byte": DETEKSI_TOTAL,
    }


def selisih_invarian(ringkas: Mapping[str, Any]) -> Dict[str, int]:
    return {
        "selisih_" + nama: int(ringkas.get(nama, 0)) - int(harap)
        for nama, harap in INVARIAN.items()
    }


def dalam_pita(nilai: Any, pita: Tuple[int, int]) -> bool:
    return int(pita[0]) <= int(nilai) <= int(pita[1])


def ringkaskan(
    status: Mapping[Any, Any],
    byte_parquet: Mapping[Any, Any],
    ambang_hidup: int = AMBANG_HIDUP_KECIL,
    ambang_mati: int = AMBANG_MATI_KECIL,
) -> Dict[str, Any]:
    sebaran = sebaran_per_kelas(status, byte_parquet)

    def ambil(kelas: str, medan: str) -> int:
        return int(sebaran.get(kelas, {}).get(medan, 0) or 0)

    hilang = [list(_bagian(k)) for k in status if byte_parquet.get(k) is None]
    hilang.sort()
    ringkas: Dict[str, Any] = {
        "versi": VERSI,
        "sidik_kode": sidik_kode(),
        "ambang_hidup_kecil": int(ambang_hidup),
        "ambang_mati_kecil": int(ambang_mati),
        "penyebut": len(status),
        "simbol": len({_bagian(k)[0] for k in status}),
        "cacah_hidup": ambil(KELAS_HIDUP, "cacah"),
        "cacah_sepi": ambil(KELAS_SEPI, "cacah"),
        "cacah_mati": ambil(KELAS_MATI, "cacah"),
        "cacah_lain": ambil(KELAS_LAIN, "cacah"),
        "byte_hidup": ambil(KELAS_HIDUP, "jumlah"),
        "byte_sepi": ambil(KELAS_SEPI, "jumlah"),
        "byte_mati": ambil(KELAS_MATI, "jumlah"),
        "byte_lain": ambil(KELAS_LAIN, "jumlah"),
        "sebaran": sebaran,
        "laporan_hilang": hilang[:BATAS_BARIS_LAPORAN],
        "cacah_laporan_hilang": len(hilang),
    }
    ringkas["total_byte"] = (
        ringkas["byte_hidup"]
        + ringkas["byte_sepi"]
        + ringkas["byte_mati"]
        + ringkas["byte_lain"]
    )
    ringkas["cacah_hidup_byte_kecil"] = cacah_di_bawah(
        status, byte_parquet, KELAS_HIDUP, ambang_hidup
    )
    ringkas["cacah_mati_byte_kecil"] = cacah_di_bawah(
        status, byte_parquet, KELAS_MATI, ambang_mati
    )
    ringkas["bagian_hidup_byte_kecil"] = (
        ringkas["cacah_hidup_byte_kecil"] / ringkas["cacah_hidup"]
        if ringkas["cacah_hidup"]
        else 0.0
    )
    ringkas["bagian_mati_byte_kecil"] = (
        ringkas["cacah_mati_byte_kecil"] / ringkas["cacah_mati"]
        if ringkas["cacah_mati"]
        else 0.0
    )
    ringkas["daftar_hidup_kecil"] = daftar_kecil(
        status, byte_parquet, KELAS_HIDUP, ambang_hidup
    )
    ringkas["daftar_mati_kecil"] = daftar_kecil(
        status, byte_parquet, KELAS_MATI, ambang_mati
    )
    ringkas.update(selisih_invarian(ringkas))
    sah_data, rinci_data = kendali_data(byte_parquet, status)
    sah_deteksi, rinci_deteksi = kendali_deteksi()
    ringkas["kendali_data_sah"] = sah_data
    ringkas["kendali_data"] = rinci_data
    ringkas["kendali_deteksi_sah"] = sah_deteksi
    ringkas["kendali_deteksi"] = rinci_deteksi
    return ringkas


def uji_r308(ringkas: Mapping[str, Any]) -> Dict[str, Any]:
    penyebut_1 = int(ringkas.get("cacah_hidup", 0))
    nilai_1 = int(ringkas.get("cacah_hidup_byte_kecil", 0))
    butir1 = {
        "nilai": nilai_1,
        "penyebut": penyebut_1,
        "pita": list(R308_PITA_BUTIR_1),
        "teradjudikasi": penyebut_1 > 0,
        "menang": penyebut_1 > 0 and dalam_pita(nilai_1, R308_PITA_BUTIR_1),
    }
    penyebut_2 = int(ringkas.get("cacah_mati", 0))
    nilai_2 = int(ringkas.get("cacah_mati_byte_kecil", 0))
    butir2 = {
        "nilai": nilai_2,
        "penyebut": penyebut_2,
        "pita": list(R308_PITA_BUTIR_2),
        "teradjudikasi": penyebut_2 > 0,
        "menang": penyebut_2 > 0 and dalam_pita(nilai_2, R308_PITA_BUTIR_2),
    }
    semua_nol = all(int(ringkas.get(medan, 1)) == 0 for medan in MEDAN_SELISIH)
    butir3 = {
        "selisih_semua_nol": bool(semua_nol),
        "kendali_data_sah": bool(ringkas.get("kendali_data_sah", False)),
        "kendali_deteksi_sah": bool(ringkas.get("kendali_deteksi_sah", False)),
        "teradjudikasi": True,
    }
    butir3["menang"] = bool(
        butir3["selisih_semua_nol"]
        and butir3["kendali_data_sah"]
        and butir3["kendali_deteksi_sah"]
    )
    return {
        "butir1": butir1,
        "butir2": butir2,
        "butir3": butir3,
        "butir3_menang": butir3["menang"],
        "menang_semua": bool(
            butir1["menang"] and butir2["menang"] and butir3["menang"]
        ),
    }


def kode_keluar(hasil: Mapping[str, Any]) -> int:
    return 0 if bool(hasil.get("butir3_menang", False)) else 1


def jalankan(akar: str = ".", total: Optional[int] = None) -> Dict[str, Any]:
    if total is None:
        total = int(getattr(kehidupan_arsip, "TOTAL_PECAHAN", 8))
    status, byte_parquet, _meta = silang_funding.baca_laporan_kehidupan(akar, total)
    ringkas = ringkaskan(status, byte_parquet)
    ringkas["hasil"] = uji_r308(ringkas)
    tujuan = nama_keluaran(akar)
    induk = os.path.dirname(tujuan)
    if induk:
        os.makedirs(induk, exist_ok=True)
    with open(tujuan, "w", encoding="utf-8") as berkas:
        json.dump(ringkas, berkas, ensure_ascii=False, indent=2, sort_keys=True)
        berkas.write("\n")
    return ringkas


def main() -> int:
    ringkas = jalankan(".")
    ikhtisar = {
        "cacah_hidup_byte_kecil": ringkas["cacah_hidup_byte_kecil"],
        "cacah_mati_byte_kecil": ringkas["cacah_mati_byte_kecil"],
        "kendali_data_sah": ringkas["kendali_data_sah"],
        "kendali_deteksi_sah": ringkas["kendali_deteksi_sah"],
        "butir3_menang": ringkas["hasil"]["butir3_menang"],
    }
    print(json.dumps(ikhtisar, ensure_ascii=False, sort_keys=True))
    return kode_keluar(ringkas["hasil"])


if __name__ == "__main__":
    raise SystemExit(main())
