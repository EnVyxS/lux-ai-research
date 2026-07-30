"""Mati tersisip atas SELURUH semesta simbol-bulan — penguji R-303.

Ramalan R-303 sudah DIPRAREGISTRASI di journal/2026-07-30-123.md §5, ditulis
SEBELUM modul ini ada (aturan 79). Bunyinya TIDAK boleh diubah oleh modul ini;
yang boleh dilakukan modul ini hanya MENGUKUR.

## Mengapa modul ini ada

R-302 mengukur `mati_tersisip` pada 38 anggota kohort puncak dan mendapat 0 dari
38 — butir BERISIKO-nya KALAH. Sebelumnya dua lubang tengah juga memberi 0.
Jadi pembatal pertama §6 ADR-A008 belum pernah menyala pada dua semesta kecil.
Dua nol pada dua sampel kecil BUKAN pernyataan tentang semesta (aturan 20), dan
ketiadaan pengukuran bukan ketiadaan gejala (aturan 59). Modul ini memperluas
pengukuran yang sama ke SELURUH penyebut kehidupan, sekali, tanpa sampel.

## Bentuk masukan — DIKUTIP, bukan diingat (penangkal KC-43)

`silang_funding` (blob 42c3aa9d):

    Kunci = Tuple[str, str]                      # (simbol, bulan) — TUPLE
    baca_laporan_kehidupan(akar, total)
        -> Tuple[Dict[Kunci, str], Dict[Kunci, int], Dict[str, Any]]

KC-43 lahir karena V1 `bentangan_kohort` menyusun modul atas NAMA fungsi tanpa
membaca bentuk kembaliannya. Karena itu modul ini tidak menulis ulang pemisah
kunci, pengelompok, penghitung rentetan, dan kendali positif: ia MEMAKAI ULANG
fungsi `bentangan_kohort` yang sudah terbukti menghasilkan laporan berjejak
(run 30509071237). Nama turunan hidup bersama asalnya (aturan 69).

## Definisi yang diukur

`bulan_tersisip`: bulan MATI yang punya bulan HIDUP di KEDUA sisinya pada sumbu
waktu — persis definisi `bentangan_kohort.mati_tersisip`, dan butir uji memaksa
keduanya sepakat. `bulan_tersisip_rapat`: bagian yang lebih ketat, yaitu bulan
MATI yang tetangga kalender LANGSUNG di kedua sisinya berstatus HIDUP; celah
bulan memutus kerapatan. Yang kedua selalu himpunan bagian yang pertama.

Tanpa dua bulan HIDUP, jawabannya 0 dan itu pernyataan tentang ketiadaan
pengapit, bukan tentang dunia (aturan 74). Karena itu penyebut ikut ditulis di
setiap tempat angka nol muncul.

## Penggugur (aturan 24)

`penyebut_kehidupan` 0, `cacah_kunci_gagal_pisah` > 0, `kendali_sah` false,
`deteksi_sah` false, `sidik_seragam` false, `cacah_simbol` 0, atau `cacah_mati`
0 — masing-masing membatalkan SELURUH angka laporan ini dan menghasilkan kode
keluar 2.

## Kendali (aturan 50)

Dua lapis. Pertama kendali pasar: simbol yang pasti diperdagangkan wajib terbaca
HIDUP pada bulan yang diharapkan (diwarisi `kohort_ekor.KENDALI_HIDUP`). Kedua,
yang khusus bagi ramalan ini, KENDALI DETEKTOR: bentangan buatan yang pasti
memuat satu bulan tersisip wajib terbaca 1, dan bentangan monoton wajib terbaca
0. Bila detektor tidak menyala pada kasus yang pasti menyala, angka nol pada
semesta tidak berarti apa-apa — ia hanya mengukur detektor yang mati.

## Keluaran sengaja RINGKAS

Laporan per-simbol penuh untuk 787 simbol mustahil dibaca utuh oleh agen
(batas baca ±30.000 token; aturan 52 menyatakan laporan yang tak terbaca utuh
sama dengan tidak ada). Karena itu laporan menyimpan agregat, distribusi, dan
baris rinci HANYA bagi simbol yang bulan tersisipnya > 0, dipagari
`BATAS_BARIS_LAPORAN`. Batas alat adalah bagian desain, bukan kecelakaan
(calon aturan 78).

Aturan yang mengikat modul ini: 10, 20, 21, 22, 24, 29, 41, 44, 46, 47, 50, 52,
59, 69, 71, 73, 74, 79.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from . import bentangan_kohort, kehidupan, kehidupan_arsip, kohort_ekor, silang_funding

VERSI = 1
KELUARAN = "reports/tersisip_semesta.json"

# Angka terbitan STATE, dipakai sebagai PEMBANDING, bukan masukan (aturan 21).
PENYEBUT_TERCATAT = 19586
SIMBOL_TERCATAT = 787
MATI_TERCATAT = 1401
SEPI_TERCATAT = 98
HIDUP_TERCATAT = 18087

# Tetapan praregistrasi R-303 (jurnal 123 §5). Pita tertutup, kedua ujung ikut.
# Butir 1 bersatuan SIMBOL, butir 2 bersatuan SIMBOL-BULAN. Nol KALAH pada
# keduanya, dan itu memang maksudnya: ramalan ini bisa kalah.
R303_PITA_SIMBOL = (1, 60)
R303_PITA_SIMBOL_BULAN = (1, 300)

# Diwarisi, tidak disalin (aturan 69, 73).
BULAN_DIHARAPKAN = kohort_ekor.BULAN_DIHARAPKAN
KENDALI_HIDUP = kohort_ekor.KENDALI_HIDUP

BERKAS_DICAP = [
    "bentangan_kohort.py",
    "kehidupan.py",
    "kehidupan_arsip.py",
    "silang_funding.py",
    "tersisip_semesta.py",
]

BATAS_BARIS_LAPORAN = 200
BATAS_BULAN_DICATAT = 12

Kunci = Tuple[str, str]


def sidik_kode() -> str:
    """Aturan 22: cap setiap berkas yang ikut menentukan angka laporan ini."""
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(BERKAS_DICAP):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def bulan_tersisip(peta_bulan: Dict[str, str]) -> List[str]:
    """Bulan MATI yang diapit bulan HIDUP di KEDUA sisi, urut menaik.

    Definisi ini WAJIB sepakat dengan `bentangan_kohort.mati_tersisip`; butir uji
    memaksanya. Bila pengapit tidak ada, hasilnya kosong — itu pernyataan tentang
    ketiadaan pengapit, bukan tentang dunia (aturan 74).
    """
    hidup = bentangan_kohort.bulan_berstatus(peta_bulan, kehidupan.STATUS_HIDUP)
    if len(hidup) < 2:
        return []
    awal, akhir = hidup[0], hidup[-1]
    return [
        b
        for b in bentangan_kohort.bulan_berstatus(peta_bulan, kehidupan.STATUS_MATI)
        if awal < b < akhir
    ]


def tetangga_maju(peta_bulan: Dict[str, str], bulan: str) -> Optional[str]:
    """Bulan berikutnya menurut KALENDER yang benar-benar ada di bentangan.

    Dicari lewat `kohort_ekor.mundur_bulan(kandidat, 1) == bulan` supaya tidak
    menebak perilaku langkah negatif yang belum pernah diukur.
    """
    for kandidat in dict(peta_bulan):
        if kohort_ekor.mundur_bulan(str(kandidat), 1) == str(bulan):
            return str(kandidat)
    return None


def bulan_tersisip_rapat(peta_bulan: Dict[str, str]) -> List[str]:
    """Bagian ketat: bulan MATI yang tetangga kalender LANGSUNGnya HIDUP di dua sisi."""
    peta = {str(b): str(st) for b, st in dict(peta_bulan).items()}
    hasil: List[str] = []
    for b in bulan_tersisip(peta):
        sebelum = kohort_ekor.mundur_bulan(b, 1)
        sesudah = tetangga_maju(peta, b)
        if peta.get(sebelum) != kehidupan.STATUS_HIDUP:
            continue
        if sesudah is None or peta.get(sesudah) != kehidupan.STATUS_HIDUP:
            continue
        hasil.append(b)
    return hasil


def ringkas_simbol(simbol: str, peta_bulan: Dict[str, str]) -> Dict[str, Any]:
    """Ringkasan satu simbol. Satuan tiap cacah di sini: BULAN (aturan 47)."""
    bulan = sorted(dict(peta_bulan))
    hidup = bentangan_kohort.bulan_berstatus(peta_bulan, kehidupan.STATUS_HIDUP)
    mati = bentangan_kohort.bulan_berstatus(peta_bulan, kehidupan.STATUS_MATI)
    sepi = bentangan_kohort.bulan_berstatus(peta_bulan, kehidupan.STATUS_SEPI)
    tersisip = bulan_tersisip(peta_bulan)
    rapat = bulan_tersisip_rapat(peta_bulan)
    return {
        "simbol": simbol,
        "cacah_bulan": len(bulan),
        "bulan_pertama": bulan[0] if bulan else None,
        "bulan_terakhir": bulan[-1] if bulan else None,
        "cacah_hidup": len(hidup),
        "cacah_mati": len(mati),
        "cacah_sepi": len(sepi),
        "bulan_hidup_terakhir": hidup[-1] if hidup else None,
        "bulan_mati_pertama": mati[0] if mati else None,
        "cacah_tersisip": len(tersisip),
        "bulan_tersisip": tersisip[:BATAS_BULAN_DICATAT],
        "cacah_tersisip_rapat": len(rapat),
        "bulan_tersisip_rapat": rapat[:BATAS_BULAN_DICATAT],
        "bangkit": bentangan_kohort.bangkit(peta_bulan),
        "rentetan_hidup_terpanjang": bentangan_kohort.rentetan_terpanjang(hidup),
        "rentetan_mati_terpanjang": bentangan_kohort.rentetan_terpanjang(mati),
    }


def ember(cacah: int) -> str:
    """Ember distribusi. Nol diberi ember sendiri supaya tidak menyamar sebagai kecil."""
    n = int(cacah)
    if n <= 0:
        return "0"
    if n == 1:
        return "1"
    if n == 2:
        return "2"
    if n <= 5:
        return "3-5"
    if n <= 12:
        return "6-12"
    return "13+"


def himpun(baris: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    """Agregat semesta. `cacah_simbol_*` bersatuan SIMBOL, sisanya SIMBOL-BULAN."""
    daftar = list(baris)
    distribusi: Dict[str, int] = {}
    for r in daftar:
        kunci = ember(int(r.get("cacah_tersisip") or 0))
        distribusi[kunci] = distribusi.get(kunci, 0) + 1
    return {
        "cacah_simbol": len(daftar),
        "cacah_simbol_berlabel": sum(
            1 for r in daftar if int(r.get("cacah_bulan") or 0) > 0
        ),
        "cacah_simbol_tersisip": sum(
            1 for r in daftar if int(r.get("cacah_tersisip") or 0) > 0
        ),
        "cacah_simbol_bulan_tersisip": sum(
            int(r.get("cacah_tersisip") or 0) for r in daftar
        ),
        "cacah_simbol_tersisip_rapat": sum(
            1 for r in daftar if int(r.get("cacah_tersisip_rapat") or 0) > 0
        ),
        "cacah_simbol_bulan_tersisip_rapat": sum(
            int(r.get("cacah_tersisip_rapat") or 0) for r in daftar
        ),
        "cacah_simbol_bangkit": sum(1 for r in daftar if r.get("bangkit")),
        "penyebut_simbol_bulan": sum(int(r.get("cacah_bulan") or 0) for r in daftar),
        "cacah_hidup": sum(int(r.get("cacah_hidup") or 0) for r in daftar),
        "cacah_mati": sum(int(r.get("cacah_mati") or 0) for r in daftar),
        "cacah_sepi": sum(int(r.get("cacah_sepi") or 0) for r in daftar),
        "distribusi_tersisip": distribusi,
    }


def kendali_deteksi() -> Dict[str, Any]:
    """Aturan 50 lapis kedua: detektor wajib menyala pada kasus yang pasti menyala."""
    sisip = {
        "2024-01": kehidupan.STATUS_HIDUP,
        "2024-02": kehidupan.STATUS_MATI,
        "2024-03": kehidupan.STATUS_HIDUP,
    }
    monoton = {
        "2024-01": kehidupan.STATUS_HIDUP,
        "2024-02": kehidupan.STATUS_HIDUP,
        "2024-03": kehidupan.STATUS_MATI,
    }
    hasil = {
        "cacah_sisip_pada_kendali_sisip": len(bulan_tersisip(sisip)),
        "diharapkan_sisip": 1,
        "cacah_sisip_pada_kendali_monoton": len(bulan_tersisip(monoton)),
        "diharapkan_monoton": 0,
        "cacah_rapat_pada_kendali_sisip": len(bulan_tersisip_rapat(sisip)),
        "diharapkan_rapat": 1,
    }
    hasil["sah"] = (
        hasil["cacah_sisip_pada_kendali_sisip"] == 1
        and hasil["cacah_sisip_pada_kendali_monoton"] == 0
        and hasil["cacah_rapat_pada_kendali_sisip"] == 1
    )
    return hasil


def dalam_pita(nilai: int, pita: Tuple[int, int]) -> bool:
    """Pita TERTUTUP: kedua ujung ikut menang."""
    return int(pita[0]) <= int(nilai) <= int(pita[1])


def uji_r303(agregat: Dict[str, Any]) -> Dict[str, Any]:
    """Adjudikasi mesin atas ketiga butir praregistrasi R-303 (jurnal 123 §5).

    Butir 1 dan 2 BERISIKO: nol kalah, dan angka besar juga kalah. Butir 3 MUDAH
    dan disebut MUDAH: ia hanya mengulang angka yang sudah terverifikasi.
    """
    a = dict(agregat)
    simbol_tersisip = int(a.get("cacah_simbol_tersisip") or 0)
    bulan_tersisip_total = int(a.get("cacah_simbol_bulan_tersisip") or 0)
    butir_1 = dalam_pita(simbol_tersisip, R303_PITA_SIMBOL)
    butir_2 = dalam_pita(bulan_tersisip_total, R303_PITA_SIMBOL_BULAN)
    butir_3 = (
        int(a.get("penyebut_simbol_bulan") or 0) == PENYEBUT_TERCATAT
        and int(a.get("cacah_simbol") or 0) == SIMBOL_TERCATAT
        and int(a.get("cacah_mati") or 0) == MATI_TERCATAT
        and bool(a.get("kendali_sah"))
        and bool(a.get("deteksi_sah"))
    )
    return {
        "pita_butir_1_simbol": list(R303_PITA_SIMBOL),
        "pita_butir_2_simbol_bulan": list(R303_PITA_SIMBOL_BULAN),
        "cacah_simbol_tersisip": simbol_tersisip,
        "cacah_simbol_bulan_tersisip": bulan_tersisip_total,
        "butir_1": butir_1,
        "butir_2": butir_2,
        "butir_3_mudah": butir_3,
        "cacah_butir_menang": sum((butir_1, butir_2, butir_3)),
        "pembatal_a008_menyala": bulan_tersisip_total > 0,
        "catatan_butir_3": "butir 3 MUDAH: ia hanya menyalin angka terverifikasi",
    }


def kode_keluar(laporan: Dict[str, Any]) -> int:
    """Kode 2 bila laporan ini tidak berhak diklaim sebagai pengukuran."""
    r = dict(laporan.get("ringkasan") or {})
    if not r.get("sidik_seragam"):
        return 2
    if not r.get("kendali_sah"):
        return 2
    if not r.get("deteksi_sah"):
        return 2
    if int(r.get("penyebut_kehidupan") or 0) <= 0:
        return 2
    if int(r.get("cacah_kunci_gagal_pisah") or 0) > 0:
        return 2
    if int(r.get("cacah_simbol") or 0) <= 0:
        return 2
    if int(r.get("cacah_mati") or 0) <= 0:
        return 2
    return 0


def jalankan(akar: str = ".", total: Optional[int] = None) -> Dict[str, Any]:
    jumlah = kehidupan_arsip.TOTAL_PECAHAN if total is None else int(total)
    status, byte_parquet, meta = silang_funding.baca_laporan_kehidupan(akar, jumlah)

    peta, gagal = bentangan_kohort.kelompokkan(status)
    baris = [ringkas_simbol(simbol, peta[simbol]) for simbol in sorted(peta)]
    agregat = himpun(baris)

    kendali = bentangan_kohort.kendali_positif(status)
    deteksi = kendali_deteksi()
    agregat["kendali_sah"] = bentangan_kohort.kendali_sah(kendali)
    agregat["deteksi_sah"] = bool(deteksi.get("sah"))
    r303 = uji_r303(agregat)

    bertersisip = sorted(
        (r for r in baris if int(r.get("cacah_tersisip") or 0) > 0),
        key=lambda r: (-int(r.get("cacah_tersisip") or 0), str(r.get("simbol"))),
    )
    terbanyak_mati = sorted(
        baris, key=lambda r: (-int(r.get("cacah_mati") or 0), str(r.get("simbol")))
    )[:20]

    ringkasan: Dict[str, Any] = {
        "versi_tersisip_semesta": VERSI,
        "penyebut_kehidupan": len(status),
        "selisih_penyebut": len(status) - PENYEBUT_TERCATAT,
        "selisih_simbol": agregat["cacah_simbol"] - SIMBOL_TERCATAT,
        "selisih_mati": agregat["cacah_mati"] - MATI_TERCATAT,
        "selisih_sepi": agregat["cacah_sepi"] - SEPI_TERCATAT,
        "selisih_hidup": agregat["cacah_hidup"] - HIDUP_TERCATAT,
        "cacah_kunci_gagal_pisah": len(gagal),
        "bulan_diharapkan": BULAN_DIHARAPKAN,
        "kendali": kendali,
        "deteksi": deteksi,
        "cacah_baris_tersisip_dicatat": min(len(bertersisip), BATAS_BARIS_LAPORAN),
        "r303": r303,
    }
    ringkasan.update(agregat)
    ringkasan.update(meta)

    return {
        "bukan_bukti": False,
        "versi_tersisip_semesta": VERSI,
        "sidik_kode": sidik_kode(),
        "kunci_gagal_pisah_contoh": gagal[:10],
        "baris_tersisip": bertersisip[:BATAS_BARIS_LAPORAN],
        "baris_terbanyak_mati": terbanyak_mati,
        "ringkasan": ringkasan,
        "catatan_bukan_bukti": (
            "laporan ini diagnostik: ia TIDAK menjatuhkan simbol-bulan mana pun dan "
            "TIDAK menulis funding_ada di manifes mana pun"
        ),
        "catatan_keluaran_ringkas": (
            "baris rinci hanya bagi simbol dengan bulan tersisip > 0, dipagari "
            "BATAS_BARIS_LAPORAN, supaya laporan ini TERBACA UTUH oleh agen "
            "(aturan 52); 787 baris penuh mustahil dibaca"
        ),
        "catatan_penggugur": (
            "sidik_seragam false, kendali_sah false, deteksi_sah false, "
            "penyebut_kehidupan 0, cacah_kunci_gagal_pisah > 0, cacah_simbol 0, "
            "atau cacah_mati 0 masing-masing membatalkan SELURUH angka laporan ini "
            "dan menghasilkan kode keluar 2 (aturan 24)"
        ),
        "catatan_satuan": (
            "cacah_simbol_* bersatuan SIMBOL; cacah_bulan, cacah_hidup, cacah_mati, "
            "cacah_sepi, cacah_tersisip bersatuan BULAN pada satu simbol; "
            "penyebut_kehidupan dan penyebut_simbol_bulan bersatuan SIMBOL-BULAN "
            "(aturan 47)"
        ),
        "catatan_nol": (
            "setiap nol dibaca bersama penyebutnya; simbol tanpa dua bulan HIDUP "
            "tidak punya pengapit, sehingga nolnya adalah pernyataan tentang "
            "ketiadaan pengapit, bukan tentang dunia (aturan 74)"
        ),
        "catatan_praregistrasi": (
            "bunyi R-303 ditulis di journal/2026-07-30-123.md paragraf 5 SEBELUM "
            "modul ini ada; modul ini hanya mengukur (aturan 29, 79)"
        ),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def main() -> int:
    laporan = jalankan(".")
    Path(KELUARAN).parent.mkdir(parents=True, exist_ok=True)
    with open(KELUARAN, "w", encoding="utf-8") as f:
        json.dump(laporan, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(laporan["ringkasan"], ensure_ascii=False, indent=2, sort_keys=True))
    return kode_keluar(laporan)


if __name__ == "__main__":
    raise SystemExit(main())
