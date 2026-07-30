"""Pasangkan kematian pertama dengan lubang funding pertama pada simbol BANGKIT.

R-303 mengukur delapan simbol yang MATI lalu HIDUP kembali (88 simbol-bulan
tersisip dari penyebut 19.586 / 787 simbol). ADR-A009 mengajukan arah sebab:
kematian pasar MENDAHULUI berhentinya funding. Sampai sekarang arah itu hanya
terukur pada SATU simbol (H-A017, kematian mendahului funding 5 bulan), dan satu
simbol bukan pola (aturan 20).

Modul ini memasangkan, bagi tiap simbol bangkit, bulan MATI pertamanya dengan
bulan berlubang funding pertamanya, lalu mencacah berapa simbol yang kematiannya
DATANG LEBIH DAHULU. Delapan adalah penyebut yang kecil dan disebut apa adanya.

## Mengapa modul ini tidak menyentuh jaringan

Seluruh bahannya sudah di-commit: `reports/kehidupan_arsip_<0..7>.json` (status
per simbol-bulan) dan `reports/funding_semesta.json` (bulan klines tanpa
funding). Keduanya dibaca lewat `silang_funding.baca_laporan_kehidupan` dan
`silang_funding.lubang_funding`, yakni tanda tangan yang SUDAH dibaca utuh dari
main sebelum modul ini ditulis (pelajaran KC-43: tanda tangan tidak ditebak).

## Definisi LOKAL — ditulis tersurat (aturan 36)

- **bangkit**: ada bulan HIDUP yang lebih besar daripada bulan MATI pertama.
- **tersisip**: bulan MATI yang berada di antara bulan HIDUP pertama dan bulan
  HIDUP terakhir simbol itu.
- **mati_dulu**: `bulan_mati_pertama` < `bulan_berlubang_pertama`.
- **lubang_dulu**: kebalikannya. **serentak**: keduanya sama bulan.
- **tanpa_lubang**: simbol itu tidak punya satu pun bulan berlubang funding.

`cacah_tersisip_alat` memanggil `tersisip_semesta.bulan_tersisip` dan
dibandingkan dengan hitungan lokal (aturan 21: hitung ulang dengan jalan lain).
Ketidaksepakatan DILAPORKAN sebagai `tersisip_sepakat` false dan BUKAN penggugur
kendali — ia temuan tentang dua definisi, bukan kegagalan alat ukur.

## Kendali positif dua lapis (aturan 50)

1. **Kendali data** — `silang_funding.kendali_silang`: tiga simbol-bulan dengan
   `byte_parquet` terbesar wajib HIDUP dan wajib punya funding.
2. **Kendali detektor** — dua bentangan BUATAN: satu yang kematiannya mendahului
   lubang, satu yang lubangnya mendahului kematian. Detektor wajib memisahkan
   keduanya. Bila tidak, `mati_dulu` tidak berhak dipercaya sama sekali.

## Medan penggugur (aturan 24)

`selisih_penyebut` (19.586), `selisih_simbol` (787), `selisih_mati` (1.401),
`selisih_bangkit` (8), `selisih_tersisip` (88), dan `selisih_lubang_dalam_penyebut`
(877). Semuanya membandingkan yang terbaca sekarang dengan angka yang SUDAH
diterbitkan. Bukan nol berarti bahan bakunya berubah dan seluruh angka batal.

Catatan penyebut: 88 simbol-bulan tersisip semesta seluruhnya berasal dari
delapan simbol bangkit itu, sehingga total tersisip atas kedelapan simbol WAJIB
88 — bukan angka baru, melainkan silang terhadap R-303.

## Praregistrasi ramalan R-304 — DITULIS DI JURNAL 124 §8 SEBELUM RUN

- **Butir 1 (BERISIKO)** — dari 8 simbol bangkit, yang `bulan_mati_pertama`-nya
  jatuh SEBELUM bulan berlubang funding pertamanya berjumlah dalam pita **5..8**.
  Nol atau di bawah 5 berarti KALAH.
- **Butir 2 (BERISIKO)** — dari 8 simbol itu, yang punya sekurangnya satu bulan
  HIDUP berlubang funding berjumlah dalam pita **3..8**.
- **Butir 3 (MUDAH, dan disebut MUDAH karena hanya menyalin angka terverifikasi)**
  — penyebut 19.586 / 787 simbol, bangkit 8, tersisip 88, kedua kendali sah,
  kode keluar 0.

Akibat yang dinyatakan lebih dahulu (aturan 29 melarang menawar sesudah angka
terlihat): butir 1 menang -> ADR-A009 boleh ditutup dengan bunyi diperluas ke
delapan simbol; butir 1 kalah -> arah sebab A009 DICABUT dan pertanyaannya
dinyatakan BELUM TERJAWAB. Butir 2 menang -> '33 HIDUP tanpa funding' adalah
ciri kebangkitan dan taksonomi wajib memuat kelasnya; butir 2 kalah -> H-A017
dirumuskan ulang.

Irisan bukan sebab (aturan 10): urutan bulan tidak membuktikan sebab, hanya
menyingkirkan salah satu arah bila urutannya seragam.

Aturan yang mengikat: 10, 20, 21, 22, 24, 29, 36, 41, 46, 50, 52, 54, 66, 73,
74, 79.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from . import kehidupan, kehidupan_arsip, silang_funding, tersisip_semesta

VERSI = 1
KELUARAN = "reports/sebab_bangkit.json"
TOTAL_PECAHAN = kehidupan_arsip.TOTAL_PECAHAN

# Angka yang SUDAH diterbitkan; penggugur, bukan masukan (aturan 21, 24).
PENYEBUT_TERCATAT = 19586
SIMBOL_TERCATAT = 787
MATI_TERCATAT = 1401
BANGKIT_TERCATAT = 8
TERSISIP_TERCATAT = 88
LUBANG_DALAM_PENYEBUT_TERCATAT = 877

# Pita praregistrasi R-304 (jurnal 124 §8) — TIDAK boleh diubah sesudah run.
R304_PITA_MATI_DULU = (5, 8)
R304_PITA_HIDUP_BERLUBANG = (3, 8)

POLA_BULAN = re.compile(r"^\d{4}-\d{2}$")
BATAS_BARIS_LAPORAN = 60

BERKAS_DICAP = [
    "kehidupan.py",
    "kehidupan_arsip.py",
    "sebab_bangkit.py",
    "silang_funding.py",
    "tersisip_semesta.py",
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


def indeks_bulan(bulan: Optional[str]) -> Optional[int]:
    """Ubah 'YYYY-MM' menjadi indeks bulan mutlak; bentuk lain menghasilkan None."""
    if bulan is None or not POLA_BULAN.match(str(bulan)):
        return None
    tahun, bln = str(bulan).split("-")
    return int(tahun) * 12 + (int(bln) - 1)


def jarak_bulan(awal: Optional[str], akhir: Optional[str]) -> Optional[int]:
    """Selisih bulan akhir - awal; None bila salah satu bukan bulan sah."""
    a, b = indeks_bulan(awal), indeks_bulan(akhir)
    if a is None or b is None:
        return None
    return b - a


def peta_status(status: Dict[Kunci, str]) -> Dict[str, Dict[str, str]]:
    """Susun status per simbol: {simbol: {bulan: status}}."""
    keluar: Dict[str, Dict[str, str]] = {}
    for (simbol, bulan), st in status.items():
        keluar.setdefault(str(simbol), {})[str(bulan)] = str(st)
    return keluar


def bulan_urut(peta_bulan: Dict[str, str]) -> List[str]:
    return sorted(b for b in peta_bulan if POLA_BULAN.match(str(b)))


def bangkit_lokal(peta_bulan: Dict[str, str]) -> bool:
    """Ada bulan HIDUP yang lebih besar daripada bulan MATI pertama."""
    urut = bulan_urut(peta_bulan)
    mati = [b for b in urut if peta_bulan[b] == kehidupan.STATUS_MATI]
    if not mati:
        return False
    return any(
        peta_bulan[b] == kehidupan.STATUS_HIDUP for b in urut if b > mati[0]
    )


def tersisip_lokal(peta_bulan: Dict[str, str]) -> List[str]:
    """Bulan MATI yang terkurung di antara bulan HIDUP pertama dan terakhir."""
    urut = bulan_urut(peta_bulan)
    hidup = [b for b in urut if peta_bulan[b] == kehidupan.STATUS_HIDUP]
    if not hidup:
        return []
    awal, akhir = hidup[0], hidup[-1]
    return [
        b
        for b in urut
        if peta_bulan[b] == kehidupan.STATUS_MATI and awal < b < akhir
    ]


def ringkas(
    simbol: str, peta_bulan: Dict[str, str], berlubang: Set[str]
) -> Dict[str, Any]:
    """Satu baris: bentangan sebuah simbol berpasangan dengan lubang funding."""
    urut = bulan_urut(peta_bulan)
    mati = [b for b in urut if peta_bulan[b] == kehidupan.STATUS_MATI]
    hidup = [b for b in urut if peta_bulan[b] == kehidupan.STATUS_HIDUP]
    lubang = [b for b in urut if b in berlubang]
    lokal = tersisip_lokal(peta_bulan)
    alat = list(tersisip_semesta.bulan_tersisip(peta_bulan))
    mati_pertama = mati[0] if mati else None
    lubang_pertama = lubang[0] if lubang else None
    berpasangan = bool(mati_pertama and lubang_pertama)
    return {
        "simbol": simbol,
        "cacah_bulan": len(urut),
        "bulan_pertama": urut[0] if urut else None,
        "bulan_terakhir": urut[-1] if urut else None,
        "cacah_mati": len(mati),
        "cacah_hidup": len(hidup),
        "bulan_mati_pertama": mati_pertama,
        "bulan_hidup_terakhir": hidup[-1] if hidup else None,
        "cacah_tersisip_lokal": len(lokal),
        "cacah_tersisip_alat": len(alat),
        "tersisip_sepakat": len(lokal) == len(alat),
        "cacah_bulan_berlubang": len(lubang),
        "bulan_berlubang_pertama": lubang_pertama,
        "cacah_mati_berlubang": sum(1 for b in mati if b in berlubang),
        "cacah_hidup_berlubang": sum(1 for b in hidup if b in berlubang),
        "ada_hidup_berlubang": any(b in berlubang for b in hidup),
        "mati_dulu": bool(berpasangan and mati_pertama < lubang_pertama),
        "lubang_dulu": bool(berpasangan and lubang_pertama < mati_pertama),
        "serentak": bool(berpasangan and mati_pertama == lubang_pertama),
        "tanpa_lubang": lubang_pertama is None,
        "selisih_bulan_mati_ke_lubang": jarak_bulan(mati_pertama, lubang_pertama)
        if berpasangan
        else None,
        "bangkit": bangkit_lokal(peta_bulan),
    }


def ember(nilai: Optional[int]) -> str:
    """Kelas selisih bulan; null disebut sebagai kelas tersendiri (aturan 74)."""
    if nilai is None:
        return "null"
    if nilai < 0:
        return "<0"
    if nilai == 0:
        return "0"
    if nilai <= 3:
        return "1-3"
    if nilai <= 12:
        return "4-12"
    return "13+"


def himpun(baris: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Agregat atas baris simbol bangkit; setiap cacah punya penyebut yang sama."""
    sebaran: Dict[str, int] = {
        k: 0 for k in ("null", "<0", "0", "1-3", "4-12", "13+")
    }
    for r in baris:
        kelas = ember(r.get("selisih_bulan_mati_ke_lubang"))
        sebaran[kelas] = sebaran.get(kelas, 0) + 1
    return {
        "cacah_simbol_bangkit": len(baris),
        "cacah_mati_dulu": sum(1 for r in baris if r.get("mati_dulu")),
        "cacah_lubang_dulu": sum(1 for r in baris if r.get("lubang_dulu")),
        "cacah_serentak": sum(1 for r in baris if r.get("serentak")),
        "cacah_tanpa_lubang": sum(1 for r in baris if r.get("tanpa_lubang")),
        "cacah_simbol_hidup_berlubang": sum(
            1 for r in baris if r.get("ada_hidup_berlubang")
        ),
        "cacah_simbol_bulan_tersisip": sum(
            int(r.get("cacah_tersisip_lokal") or 0) for r in baris
        ),
        "cacah_simbol_tersisip_tak_sepakat": sum(
            1 for r in baris if not r.get("tersisip_sepakat")
        ),
        "sebaran_selisih_bulan": sebaran,
    }


def kendali_deteksi() -> Dict[str, Any]:
    """Kendali positif detektor: dua bentangan BUATAN yang wajib terpisah."""
    m, h = kehidupan.STATUS_MATI, kehidupan.STATUS_HIDUP
    peta = {"2024-01": h, "2024-02": m, "2024-03": m, "2024-04": h}
    a = ringkas("KENDALI_MATI_DULU", peta, {"2024-03", "2024-04"})
    b = ringkas("KENDALI_LUBANG_DULU", peta, {"2024-01", "2024-02", "2024-03"})
    sah = bool(
        a["mati_dulu"]
        and not a["lubang_dulu"]
        and a["bangkit"]
        and b["lubang_dulu"]
        and not b["mati_dulu"]
        and a["selisih_bulan_mati_ke_lubang"] == 1
        and b["selisih_bulan_mati_ke_lubang"] == -1
    )
    return {"baris_kendali_deteksi": [a, b], "kendali_deteksi_sah": sah}


def dalam_pita(nilai: Optional[int], pita: Tuple[int, int]) -> bool:
    if nilai is None:
        return False
    return int(pita[0]) <= int(nilai) <= int(pita[1])


def uji_r304(agregat: Dict[str, Any], ringkasan: Dict[str, Any]) -> Dict[str, Any]:
    """Adjudikasi mesin terhadap pita yang sudah dipraregistrasi di jurnal 124."""
    butir_1 = dalam_pita(agregat.get("cacah_mati_dulu"), R304_PITA_MATI_DULU)
    butir_2 = dalam_pita(
        agregat.get("cacah_simbol_hidup_berlubang"), R304_PITA_HIDUP_BERLUBANG
    )
    butir_3 = bool(
        int(ringkasan.get("selisih_penyebut") or 0) == 0
        and int(ringkasan.get("selisih_simbol") or 0) == 0
        and int(ringkasan.get("selisih_bangkit") or 0) == 0
        and int(ringkasan.get("selisih_tersisip") or 0) == 0
        and ringkasan.get("kendali_sah")
        and ringkasan.get("kendali_deteksi_sah")
    )
    return {
        "butir_1_mati_dulu_dalam_pita": butir_1,
        "butir_1_pita": list(R304_PITA_MATI_DULU),
        "butir_1_nilai": agregat.get("cacah_mati_dulu"),
        "butir_2_hidup_berlubang_dalam_pita": butir_2,
        "butir_2_pita": list(R304_PITA_HIDUP_BERLUBANG),
        "butir_2_nilai": agregat.get("cacah_simbol_hidup_berlubang"),
        "butir_3_mudah_cocok": butir_3,
        "catatan_butir_3": "MUDAH: hanya menyalin angka yang sudah terverifikasi",
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
    for medan in (
        "selisih_penyebut",
        "selisih_simbol",
        "selisih_mati",
        "selisih_bangkit",
        "selisih_tersisip",
        "selisih_lubang_dalam_penyebut",
    ):
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

    peta = peta_status(status)
    baris: List[Dict[str, Any]] = []
    for simbol in sorted(peta):
        if not bangkit_lokal(peta[simbol]):
            continue
        baris.append(ringkas(simbol, peta[simbol], berlubang.get(simbol, set())))

    agregat = himpun(baris)
    kendali = silang_funding.kendali_silang(byte_parquet, status, lubang)
    kd = kendali_deteksi()
    cacah_mati = sum(1 for st in status.values() if st == kehidupan.STATUS_MATI)
    lubang_dalam = len(lubang & set(status))

    ringkasan: Dict[str, Any] = {
        "penyebut_kehidupan": len(status),
        "cacah_simbol": len(peta),
        "cacah_mati": cacah_mati,
        "cacah_lubang_dalam_penyebut": lubang_dalam,
        "selisih_penyebut": len(status) - PENYEBUT_TERCATAT,
        "selisih_simbol": len(peta) - SIMBOL_TERCATAT,
        "selisih_mati": cacah_mati - MATI_TERCATAT,
        "selisih_bangkit": len(baris) - BANGKIT_TERCATAT,
        "selisih_tersisip": int(agregat["cacah_simbol_bulan_tersisip"])
        - TERSISIP_TERCATAT,
        "selisih_lubang_dalam_penyebut": lubang_dalam
        - LUBANG_DALAM_PENYEBUT_TERCATAT,
        "kendali": kendali,
        "kendali_sah": silang_funding.kendali_sah(kendali),
        "kendali_deteksi_sah": kd["kendali_deteksi_sah"],
    }
    ringkasan.update(meta)
    ringkasan.update(meta_lubang)
    ringkasan.update(agregat)

    return {
        "bukan_bukti": False,
        "versi_sebab_bangkit": VERSI,
        "sidik_kode": sidik_kode(),
        "sidik_kode_silang_funding": silang_funding.sidik_kode(),
        "sidik_kode_tersisip_semesta": tersisip_semesta.sidik_kode(),
        "sidik_data_funding": hashlib.sha256(mentah).hexdigest(),
        "sumber": [silang_funding.SUMBER_FUNDING]
        + [kehidupan_arsip.nama_keluaran(i) for i in range(total)],
        "definisi": {
            "bangkit": "ada bulan HIDUP lebih besar daripada bulan MATI pertama",
            "tersisip": "bulan MATI di antara bulan HIDUP pertama dan terakhir",
            "mati_dulu": "bulan_mati_pertama < bulan_berlubang_pertama",
            "lubang_funding": "bulan punya klines tetapi tidak punya fundingRate",
        },
        "praregistrasi_r304": {
            "jurnal": "journal/2026-07-30-124.md",
            "pita_butir_1": list(R304_PITA_MATI_DULU),
            "pita_butir_2": list(R304_PITA_HIDUP_BERLUBANG),
            "butir_3": "MUDAH",
        },
        "baris_simbol_bangkit": baris[:BATAS_BARIS_LAPORAN],
        "cacah_baris_dilapor": len(baris[:BATAS_BARIS_LAPORAN]),
        "baris_kendali_deteksi": kd["baris_kendali_deteksi"],
        "uji_r304": uji_r304(agregat, ringkasan),
        "ringkasan": ringkasan,
        "catatan_tafsir": (
            "urutan bulan BUKAN sebab (aturan 10); yang diukur hanya urutan "
            "kejadian, dan penyebutnya delapan simbol — kecil, dan disebut kecil "
            "(aturan 20, 74)"
        ),
        "catatan_penggugur": (
            "sidik_seragam false, laporan pecahan kurang, kunci ganda, kendali "
            "data atau kendali detektor tidak sah, atau salah satu selisih bukan "
            "nol membatalkan seluruh angka (aturan 24)"
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
