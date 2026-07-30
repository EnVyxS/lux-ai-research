"""bulan_pertama V1 — R-309.

Poros H-A019. R-308 mengukur bahwa di zona 22.440–97.634 byte ada 38 baris
HIDUP dan NOL baris MATI. Tafsir "berkas kecil = pasar mati" TERBALIK di zona
itu, dan besar berkas DILARANG dipakai sebagai detektor status ke arah mana pun
(ADR-A015 kep. 5). Yang belum diukur: apakah berkas kecil menandai bulan
SEBAGIAN — bulan pertama pencatatan sebuah simbol, atau bulan tepi jendela
(BULAN_TEPI = 2026-06) yang belum lengkap.

H-A019 lahir dari MEMBACA hasil R-308, jadi ia wajib diuji atas semesta penuh,
bukan atas daftar 38 yang melahirkannya. Karena itu butir 2 mengukur nisbah
rata byte bulan PERTAMA terhadap bulan BUKAN-pertama atas seluruh 19.586 baris,
bukan atas ekor kecilnya saja.

DILARANG menyimpulkan sebab dari modul ini. Bulan pertama yang kecil tidak
membuktikan bahwa kekecilan itu DISEBABKAN oleh ketidaklengkapan bulan; ia
hanya mengukur bentuk irisannya (aturan 10).

## Delapan medan selisih, semuanya jalur bebas

Cacat irisan_byte yang wajib diteruskan: di sana `total_byte` dihitung dari
jumlah byte per kelas, sehingga `selisih_total_byte` TURUNAN — sembilan medan
selisihnya sesungguhnya delapan pemeriksaan bebas ditambah satu turunan.

Di modul ini `total_byte` dihitung LANGSUNG oleh `total_byte_langsung`, yakni
menjumlah byte seluruh kunci penyebut tanpa melewati pengelompokan kelas. Tidak
ada medan invarian di sini yang dihitung dari medan invarian lain. Yang tetap
wajib dikatakan apa adanya: `byte_hidup` dan `total_byte` berbagi bahan baku
yang sama, jadi keduanya bebas sebagai JALUR HITUNG, bukan sebagai bukti yang
saling merdeka. Delapan, bukan sembilan, dan bukan pula delapan yang setara.

## Praregistrasi R-309 — TERKUNCI sebelum run (teks sama di jurnal 129 §10)

- butir 1 BERISIKO: dari baris HIDUP ber-byte < 97.634 (penyebut terukur 38),
  cacah yang merupakan bulan PERTAMA simbol ATAU bulan `2026-06`. Pita 22..38.
  Penyebut nol berarti TIDAK TERADJUDIKASI, bukan menang.
- butir 2 BERISIKO: nisbah rata byte bulan PERTAMA terhadap rata byte bulan
  BUKAN-pertama, atas 19.586 baris. Pita 0.10..0.60.
- butir 3 MUDAH: kedelapan selisih invarian nol, dua kendali sah, kode 0, CI
  diukur.

Aturan yang mengikat: 10, 21, 22, 24, 29, 38, 41, 45, 46, 47, 50, 52, 53, 57,
66, KC-42, KC-43, KC-49.
"""

from __future__ import annotations

import hashlib
import json
import os
from typing import Any, Dict, List, Mapping, Optional, Tuple

from lux_ai.serapan import kehidupan_arsip
from lux_ai.serapan import silang_funding

VERSI = 1
KELUARAN = "reports/bulan_pertama.json"
BATAS_BARIS_LAPORAN = 40

KELAS_HIDUP = "HIDUP"
KELAS_SEPI = "SEPI"
KELAS_MATI = "MATI"
KELAS_LAIN = "LAIN"

# Ambang R-308 apa adanya: byte_min kelas MATI hasil ukur R-307.
AMBANG_HIDUP_KECIL = 97634
# Tepi jendela kehidupan; bulan ini belum tentu lengkap saat arsip dibuat.
BULAN_TEPI = "2026-06"

R309_PITA_BUTIR_1: Tuple[int, int] = (22, 38)
R309_PITA_BUTIR_2: Tuple[float, float] = (0.10, 0.60)

# Delapan invarian, semuanya angka TERUKUR R-307/R-308.
INVARIAN: Dict[str, int] = {
    "penyebut": 19586,
    "simbol": 787,
    "cacah_hidup": 18087,
    "cacah_sepi": 98,
    "cacah_mati": 1401,
    "total_byte": 32706262375,
    "byte_hidup": 32049492952,
    "cacah_hidup_byte_kecil": 38,
}
MEDAN_SELISIH: Tuple[str, ...] = tuple("selisih_" + nama for nama in INVARIAN)

# Kendali data: tiga baris terbesar semesta, semuanya HIDUP (R-307).
KENDALI_DATA: Dict[Tuple[str, str], int] = {
    ("BTCUSDT", "2021-05"): 2770666,
    ("BTCUSDT", "2021-08"): 2730341,
    ("BTCUSDT", "2021-01"): 2722266,
}

# Kendali deteksi: semesta buatan, angka dipisah dari fungsi yang diuji.
DETEKSI_AMBANG = 250
DETEKSI_PERTAMA = 2
DETEKSI_HIDUP_KECIL = 2
DETEKSI_SEBAGIAN = 2
DETEKSI_NISBAH = 0.75
DETEKSI_TOTAL_BYTE = 1500


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


def peta_bulan_pertama(status: Mapping[Any, Any]) -> Dict[str, str]:
    """Bulan terkecil per simbol menurut penyebut kehidupan itu sendiri."""
    peta: Dict[str, str] = {}
    for kunci in status:
        simbol, bulan = _bagian(kunci)
        ada = peta.get(simbol)
        if ada is None or bulan < ada:
            peta[simbol] = bulan
    return peta


def penanda_baris(
    simbol: Any,
    bulan: Any,
    peta: Mapping[str, str],
    bulan_tepi: str = BULAN_TEPI,
) -> Dict[str, bool]:
    pertama = peta.get(str(simbol)) == str(bulan)
    tepi = str(bulan) == str(bulan_tepi)
    return {
        "pertama": bool(pertama),
        "tepi": bool(tepi),
        "sebagian": bool(pertama or tepi),
    }


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


def total_byte_langsung(
    status: Mapping[Any, Any], byte_parquet: Mapping[Any, Any]
) -> int:
    """Jumlah byte seluruh penyebut TANPA melewati pengelompokan kelas."""
    total = 0
    for kunci in status:
        byte = byte_parquet.get(kunci)
        if byte is None:
            continue
        total += int(byte)
    return total


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


def cacah_sebagian(
    status: Mapping[Any, Any],
    byte_parquet: Mapping[Any, Any],
    kelas: str,
    ambang: int,
    peta: Optional[Mapping[str, str]] = None,
    bulan_tepi: str = BULAN_TEPI,
) -> int:
    """Butir 1: baris berkelas `kelas` di bawah ambang yang bulan PERTAMA
    simbolnya ATAU bulan tepi. Dihitung penuh, BUKAN dari daftar terpotong."""
    acuan = peta_bulan_pertama(status) if peta is None else peta
    batas = int(ambang)
    cacah = 0
    for kunci, nilai in status.items():
        if kelas_status(nilai) != kelas:
            continue
        byte = byte_parquet.get(kunci)
        if byte is None:
            continue
        if int(byte) >= batas:
            continue
        simbol, bulan = _bagian(kunci)
        if penanda_baris(simbol, bulan, acuan, bulan_tepi)["sebagian"]:
            cacah += 1
    return cacah


def daftar_kecil_bertanda(
    status: Mapping[Any, Any],
    byte_parquet: Mapping[Any, Any],
    kelas: str,
    ambang: int,
    peta: Optional[Mapping[str, str]] = None,
    bulan_tepi: str = BULAN_TEPI,
    batas: int = BATAS_BARIS_LAPORAN,
) -> List[Dict[str, Any]]:
    acuan = peta_bulan_pertama(status) if peta is None else peta
    ambang_int = int(ambang)
    baris: List[Dict[str, Any]] = []
    for kunci, nilai in status.items():
        if kelas_status(nilai) != kelas:
            continue
        byte = byte_parquet.get(kunci)
        if byte is None:
            continue
        angka = int(byte)
        if angka >= ambang_int:
            continue
        simbol, bulan = _bagian(kunci)
        tanda = penanda_baris(simbol, bulan, acuan, bulan_tepi)
        baris.append(
            {
                "simbol": simbol,
                "bulan": bulan,
                "byte": angka,
                "pertama": tanda["pertama"],
                "tepi": tanda["tepi"],
                "sebagian": tanda["sebagian"],
            }
        )
    baris.sort(key=lambda r: (r["byte"], r["simbol"], r["bulan"]))
    return baris[: int(batas)]


def nisbah_pertama(
    status: Mapping[Any, Any],
    byte_parquet: Mapping[Any, Any],
    peta: Optional[Mapping[str, str]] = None,
) -> Dict[str, Any]:
    """Butir 2: rata byte bulan pertama lawan bulan bukan-pertama.

    Penyebut nol menghasilkan null, bukan 0 (aturan 41, 46).
    """
    acuan = peta_bulan_pertama(status) if peta is None else peta
    cacah_p = 0
    cacah_b = 0
    jumlah_p = 0
    jumlah_b = 0
    for kunci in status:
        byte = byte_parquet.get(kunci)
        if byte is None:
            continue
        simbol, bulan = _bagian(kunci)
        angka = int(byte)
        if acuan.get(simbol) == bulan:
            cacah_p += 1
            jumlah_p += angka
        else:
            cacah_b += 1
            jumlah_b += angka
    rata_p = jumlah_p / cacah_p if cacah_p else None
    rata_b = jumlah_b / cacah_b if cacah_b else None
    nisbah = round(rata_p / rata_b, 6) if rata_p is not None and rata_b else None
    return {
        "cacah_pertama": cacah_p,
        "cacah_bukan_pertama": cacah_b,
        "jumlah_byte_pertama": jumlah_p,
        "jumlah_byte_bukan_pertama": jumlah_b,
        "rata_byte_pertama": round(rata_p, 3) if rata_p is not None else None,
        "rata_byte_bukan_pertama": round(rata_b, 3) if rata_b is not None else None,
        "nisbah_rata": nisbah,
    }


def selisih_invarian(ringkas: Mapping[str, Any]) -> Dict[str, int]:
    return {
        "selisih_" + nama: int(ringkas.get(nama, 0)) - int(harap)
        for nama, harap in INVARIAN.items()
    }


def dalam_pita(nilai: Any, pita: Tuple[int, int]) -> bool:
    return int(pita[0]) <= int(nilai) <= int(pita[1])


def dalam_pita_pecahan(nilai: Any, pita: Tuple[float, float]) -> bool:
    if nilai is None:
        return False
    return float(pita[0]) <= float(nilai) <= float(pita[1])


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


def kendali_deteksi(ambang: int = DETEKSI_AMBANG) -> Tuple[bool, Dict[str, Any]]:
    """Semesta buatan: dua simbol, lima baris, jawaban dihitung tangan.

    AAA 2024-01 100 HIDUP · AAA 2024-02 300 HIDUP · AAA 2024-03 500 HIDUP
    BBB 2026-05 400 MATI · BBB 2026-06 200 HIDUP
    Bulan pertama: AAA 2024-01, BBB 2026-05 (2 simbol).
    HIDUP di bawah 250: AAA 2024-01 dan BBB 2026-06 (2 baris).
    Keduanya sebagian: yang satu bulan pertama, yang lain bulan tepi (2).
    Nisbah: (100+400)/2 = 250 dibagi (300+500+200)/3 = 333,333… → 0,75.
    """
    batas = int(ambang)
    status = {
        ("AAA", "2024-01"): "HIDUP",
        ("AAA", "2024-02"): "HIDUP",
        ("AAA", "2024-03"): "HIDUP",
        ("BBB", "2026-05"): "MATI",
        ("BBB", "2026-06"): "HIDUP",
    }
    byte_parquet = {
        ("AAA", "2024-01"): 100,
        ("AAA", "2024-02"): 300,
        ("AAA", "2024-03"): 500,
        ("BBB", "2026-05"): 400,
        ("BBB", "2026-06"): 200,
    }
    peta = peta_bulan_pertama(status)
    hidup_kecil = cacah_di_bawah(status, byte_parquet, KELAS_HIDUP, batas)
    sebagian = cacah_sebagian(status, byte_parquet, KELAS_HIDUP, batas, peta)
    nisbah = nisbah_pertama(status, byte_parquet, peta)
    total = total_byte_langsung(status, byte_parquet)
    sah = (
        len(peta) == DETEKSI_PERTAMA
        and hidup_kecil == DETEKSI_HIDUP_KECIL
        and sebagian == DETEKSI_SEBAGIAN
        and nisbah["nisbah_rata"] == DETEKSI_NISBAH
        and total == DETEKSI_TOTAL_BYTE
    )
    return bool(sah), {
        "ambang": batas,
        "cacah_simbol": len(peta),
        "hidup_kecil": hidup_kecil,
        "sebagian": sebagian,
        "nisbah_rata": nisbah["nisbah_rata"],
        "total_byte": total,
        "harap_cacah_simbol": DETEKSI_PERTAMA,
        "harap_hidup_kecil": DETEKSI_HIDUP_KECIL,
        "harap_sebagian": DETEKSI_SEBAGIAN,
        "harap_nisbah_rata": DETEKSI_NISBAH,
        "harap_total_byte": DETEKSI_TOTAL_BYTE,
    }


def ringkaskan(
    status: Mapping[Any, Any],
    byte_parquet: Mapping[Any, Any],
    ambang_hidup: int = AMBANG_HIDUP_KECIL,
    bulan_tepi: str = BULAN_TEPI,
) -> Dict[str, Any]:
    peta = peta_bulan_pertama(status)
    sebaran = sebaran_per_kelas(status, byte_parquet)

    def ambil(kelas: str, medan: str) -> int:
        return int(sebaran.get(kelas, {}).get(medan, 0) or 0)

    hilang = [list(_bagian(k)) for k in status if byte_parquet.get(k) is None]
    hilang.sort()
    ringkas: Dict[str, Any] = {
        "versi": VERSI,
        "sidik_kode": sidik_kode(),
        "ambang_hidup_kecil": int(ambang_hidup),
        "bulan_tepi": str(bulan_tepi),
        "penyebut": len(status),
        "simbol": len(peta),
        "cacah_hidup": ambil(KELAS_HIDUP, "cacah"),
        "cacah_sepi": ambil(KELAS_SEPI, "cacah"),
        "cacah_mati": ambil(KELAS_MATI, "cacah"),
        "cacah_lain": ambil(KELAS_LAIN, "cacah"),
        "byte_hidup": ambil(KELAS_HIDUP, "jumlah"),
        "byte_sepi": ambil(KELAS_SEPI, "jumlah"),
        "byte_mati": ambil(KELAS_MATI, "jumlah"),
        "byte_lain": ambil(KELAS_LAIN, "jumlah"),
        "total_byte": total_byte_langsung(status, byte_parquet),
        "sebaran": sebaran,
        "laporan_hilang": hilang[:BATAS_BARIS_LAPORAN],
        "cacah_laporan_hilang": len(hilang),
    }
    ringkas["cacah_hidup_byte_kecil"] = cacah_di_bawah(
        status, byte_parquet, KELAS_HIDUP, ambang_hidup
    )
    ringkas["cacah_hidup_kecil_sebagian"] = cacah_sebagian(
        status, byte_parquet, KELAS_HIDUP, ambang_hidup, peta, bulan_tepi
    )
    ringkas["bagian_hidup_kecil_sebagian"] = (
        round(
            ringkas["cacah_hidup_kecil_sebagian"] / ringkas["cacah_hidup_byte_kecil"],
            6,
        )
        if ringkas["cacah_hidup_byte_kecil"]
        else None
    )
    ringkas["daftar_hidup_kecil"] = daftar_kecil_bertanda(
        status, byte_parquet, KELAS_HIDUP, ambang_hidup, peta, bulan_tepi
    )
    ringkas.update(nisbah_pertama(status, byte_parquet, peta))
    ringkas.update(selisih_invarian(ringkas))
    sah_data, rinci_data = kendali_data(byte_parquet, status)
    sah_deteksi, rinci_deteksi = kendali_deteksi()
    ringkas["kendali_data_sah"] = sah_data
    ringkas["kendali_data"] = rinci_data
    ringkas["kendali_deteksi_sah"] = sah_deteksi
    ringkas["kendali_deteksi"] = rinci_deteksi
    return ringkas


def uji_r309(ringkas: Mapping[str, Any]) -> Dict[str, Any]:
    penyebut_1 = int(ringkas.get("cacah_hidup_byte_kecil", 0))
    nilai_1 = int(ringkas.get("cacah_hidup_kecil_sebagian", 0))
    butir1 = {
        "nilai": nilai_1,
        "penyebut": penyebut_1,
        "pita": list(R309_PITA_BUTIR_1),
        "teradjudikasi": penyebut_1 > 0,
        "menang": penyebut_1 > 0 and dalam_pita(nilai_1, R309_PITA_BUTIR_1),
    }
    nilai_2 = ringkas.get("nisbah_rata")
    butir2 = {
        "nilai": nilai_2,
        "cacah_pertama": int(ringkas.get("cacah_pertama", 0)),
        "cacah_bukan_pertama": int(ringkas.get("cacah_bukan_pertama", 0)),
        "pita": list(R309_PITA_BUTIR_2),
        "teradjudikasi": nilai_2 is not None,
        "menang": dalam_pita_pecahan(nilai_2, R309_PITA_BUTIR_2),
    }
    semua_nol = all(int(ringkas.get(medan, 1)) == 0 for medan in MEDAN_SELISIH)
    butir3 = {
        "selisih_semua_nol": bool(semua_nol),
        "cacah_medan_selisih": len(MEDAN_SELISIH),
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
    ringkas["hasil"] = uji_r309(ringkas)
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
        "cacah_hidup_kecil_sebagian": ringkas["cacah_hidup_kecil_sebagian"],
        "nisbah_rata": ringkas["nisbah_rata"],
        "rata_byte_pertama": ringkas["rata_byte_pertama"],
        "rata_byte_bukan_pertama": ringkas["rata_byte_bukan_pertama"],
        "kendali_data_sah": ringkas["kendali_data_sah"],
        "kendali_deteksi_sah": ringkas["kendali_deteksi_sah"],
        "butir3_menang": ringkas["hasil"]["butir3_menang"],
    }
    print(json.dumps(ikhtisar, ensure_ascii=False, sort_keys=True))
    return kode_keluar(ringkas["hasil"])


if __name__ == "__main__":
    raise SystemExit(main())
