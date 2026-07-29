"""Sebaran KUOTA semesta arsip - identitas nama hanya-arsip dan adjudikasi R-249.

Aturan 63 lahir dari satu pengakuan: penyebut 787 simbol adalah pasangan berkuota
USDT SAJA, sementara arsip memuat 937 nama dan 21.789 simbol-bulan. Selisih 150
nama disebut "hampir seluruhnya BUSD/USDC" atas dasar delapan belas CONTOH yang
terbaca di jurnal 94 - bukan atas dasar cacahan. Modul ini mengubah contoh menjadi
cacahan, tanpa jaringan, dari laporan yang sudah di-commit.

## Yang diukur

1. KUOTA setiap nama di `reports/semesta_bulan_1m.json`, diturunkan dari akhiran
   namanya sesudah tanda SETTLED dipisahkan, beserta cacah nama dan jumlah
   simbol-bulan per kuota.
2. **R-249, yang sejak jurnal 94 MENUNGGU:** jumlah simbol-bulan bagi nama
   berkuota USDT dan BUKAN nama SETTLED, dibandingkan dengan penyebut 19.586.
   Jurnal 94 menulis "manifes arsip" sebagai sumbernya; itu KELIRU dengan alasan
   yang sama seperti dikoreksi di `bulan_settled.py` - manifes pecahan hanya
   memuat parquet yang benar-benar diunduh, yakni penyebut itu sendiri, sehingga
   membacanya akan menjawab pertanyaan dengan angkanya sendiri. Isi ramalan tidak
   diubah sedikit pun; hanya alat pengukurnya dikoreksi ke pendaftaran arsip.
3. DAFTAR nama yang tidak berakhiran `USDT`, yakni calon anggota himpunan
   hanya-arsip. Bahwa keduanya identik adalah HIPOTESIS yang diuji di sini oleh
   R-257, bukan anggapan.
4. Silang balik terhadap angka yang sudah tercatat (aturan 21): cacah nama arsip
   WAJIB 937 dan jumlah bulan arsip WAJIB 21.789. Bila berbeda, arsip berubah dan
   seluruh perbandingan lama harus dibaca ulang - itu temuan, bukan gangguan.

## Aturan 64 diterapkan pada kesempatan pertama

R-255 SEPARUH karena medan `berkas_terpanjang` menamai satu pemegang dari dua yang
seri (KC-26). Modul ini karena itu TIDAK PERNAH menamai pemegang tunggal:
`pemegang_terbanyak` selalu mengembalikan DAFTAR beserta medan `seri`. Aturan yang
lahir dari kekeliruan wajib dipakai, bukan sekadar dicatat.

## Kendali positif (aturan 50)

BTCUSDT dibaca dari peta yang sama. Bila laporan sumber kosong atau salah bentuk,
ia berbunyi nol; BTCUSDT di bawah `AMBANG_KENDALI` membuat `kendali_sah` false dan
kode keluar 2, sehingga sebaran kuota yang sepi tidak boleh dibaca sebagai bukti
apa pun (aturan 59).

## Batas yang tetap berlaku

Kuota disimpulkan dari NAMA, bukan dari metadata bursa; nama adalah petunjuk kuat
tetapi tetap petunjuk (bandingkan KC-18: bentuk bukan kehidupan). Simbol-bulan di
sini adalah bulan yang arsip TERBITKAN, bukan yang lolos gerbang kehidupan, jadi
angka apa pun dari modul ini DILARANG dipakai sebagai penyebut kematian (aturan
30, 63). Modul ini tidak menyentuh satu pun berkas data dan tidak mengunduh
apa pun.

## Praregistrasi ramalan - ditulis SEBELUM run

- **R-249 (dipraregistrasi jurnal 94, alat dikoreksi di sini)** - jumlah
  simbol-bulan bagi nama berkuota USDT dan bukan SETTLED **lebih besar dari
  19.586**. Dasarnya: 12 simbol-bulan gagal gerbang 1m dan karantina tidak masuk
  penyebut, jadi arsip wajib memuat sekurang-kurangnya 19.598. GUGUR bila sama
  atau lebih kecil.
- **R-257** - cacah nama arsip yang TIDAK berakhiran `USDT` berjumlah **tepat
  150**, yakni sama dengan cacah hanya-arsip, dan karena itu cacah nama
  berakhiran `USDT` berjumlah **787**. GUGUR bila salah satu berbeda. Ramalan ini
  BERISIKO: bila ada satu saja simbol berkuota USDT yang tidak pernah masuk
  penyebut, kedua angka bergeser sekaligus.
- **R-258** - di antara nama yang bukan berkuota USDT, kuota terbanyak menurut
  cacah nama adalah **BUSD atau USDC**, dan keduanya bersama menguasai
  **sekurang-kurangnya 130 dari 150**. Perlakuan SERI disebut di muka (aturan
  64): bila BUSD dan USDC seri, ramalan tetap TEPAT sebab keduanya sudah
  disebutkan bersama, dan medan `pemegang` akan memuat keduanya.
- **R-259** - jumlah simbol-bulan seluruh nama arsip tetap **21.789** dan cacah
  nama tetap **937**, sehingga `kode_keluar` 0. GUGUR bila salah satu berbeda -
  dan bila gugur, seluruh angka lama wajib dibaca ulang.
- **R-260** - CI pada commit yang memuat berkas ini mengumpulkan **584 butir**
  dengan kode keluar 0. Dasar (aturan 54, 56, 57): 552 terverifikasi pada run
  30452311150 ditambah **32** fungsi `def test_` yang dicacah BERNOMOR di
  `tests/test_semesta_kuota.py`, tanpa `parametrize`. 552 + 32 = 584.

Cacah baris berkas ini SENGAJA tidak diramalkan (aturan 58, pilihan c).

Aturan yang mengikat: 10, 16, 20, 21, 22, 24, 30, 36, 44, 45, 46, 50, 52, 54, 56,
57, 58, 59, 62, 63, 64.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from . import semesta_silang

VERSI = 1
SUMBER = semesta_silang.SUMBER_ARSIP
KELUARAN = "reports/semesta_kuota.json"
KELUARAN_RINGKAS = "reports/semesta_kuota_ringkas.json"

# Urutan penting: bentuk bergaris bawah diperiksa lebih dulu, sebab keduanya
# hidup berdampingan di arsip (ICPUSDT_SETTLED lawan TLMUSDTSETTLED, R-246).
TANDA_SETTLED: Tuple[str, ...] = ("_SETTLED", "SETTLED")

# Urutan penting: USDT sebelum USD, BUSD dan USDC sebelum USD.
KUOTA_URUT: Tuple[str, ...] = (
    "USDT",
    "BUSD",
    "USDC",
    "TUSD",
    "FDUSD",
    "USD",
    "BTC",
    "ETH",
    "BNB",
)
KUOTA_TAK_DIKENAL = "TAK_DIKENAL"
KUOTA_UTAMA = "USDT"

SIMBOL_KENDALI = "BTCUSDT"
AMBANG_KENDALI = 60

# Angka yang sudah tercatat dan dipakai sebagai penggugur (aturan 21, 24).
CACAH_NAMA_TERCATAT = 937
JUMLAH_BULAN_TERCATAT = 21789
CACAH_SETTLED_TERCATAT = 15
PENYEBUT_SIMBOL_TERCATAT = 787
PENYEBUT_BULAN_TERCATAT = 19586
SIMBOL_BULAN_DISERAP = 19598
AMBANG_BUSD_USDC = 130

BERKAS_DICAP = [
    "semesta_kuota.py",
    "semesta_silang.py",
]


def nama_keluaran() -> str:
    return KELUARAN


def nama_ringkas() -> str:
    return KELUARAN_RINGKAS


def sidik_kode() -> str:
    """Aturan 22: cap setiap berkas yang ikut menentukan angka ini."""
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(BERKAS_DICAP):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def pisah_settled(nama: str) -> Tuple[str, bool]:
    """Pisahkan tanda SETTLED dari nama; KEDUA konvensi diperiksa (R-246)."""
    teks = str(nama)
    for tanda in TANDA_SETTLED:
        if teks.endswith(tanda) and len(teks) > len(tanda):
            return teks[: -len(tanda)], True
    return teks, False


def kuota_dasar(dasar: str) -> str:
    """Kuota dari akhiran nama dasar; TAK_DIKENAL bila tak ada yang cocok.

    Aturan 16: medan ini menamai DUGAAN dari nama, bukan kuota yang dibaca dari
    metadata bursa. Nama yang tidak dikenali TIDAK dipaksa masuk kuota mana pun.
    """
    teks = str(dasar)
    for kuota in KUOTA_URUT:
        if teks.endswith(kuota) and len(teks) > len(kuota):
            return kuota
    return KUOTA_TAK_DIKENAL


def kuota_nama(nama: str) -> Dict[str, Any]:
    dasar, settled = pisah_settled(nama)
    return {
        "nama": str(nama),
        "dasar": dasar,
        "settled": bool(settled),
        "kuota": kuota_dasar(dasar),
        "akhiran_usdt": str(nama).endswith(KUOTA_UTAMA),
    }


def klasifikasi(peta: Dict[str, int]) -> List[Dict[str, Any]]:
    """Satu baris per nama arsip, dengan cacah bulan yang dibawa apa adanya."""
    baris: List[Dict[str, Any]] = []
    for nama in sorted(peta):
        info = kuota_nama(nama)
        info["cacah_bulan"] = int(peta[nama])
        baris.append(info)
    return baris


def ringkas_kuota(baris: Sequence[Dict[str, Any]]) -> Dict[str, Dict[str, int]]:
    hasil: Dict[str, Dict[str, int]] = {}
    for b in baris:
        sel = hasil.setdefault(
            str(b["kuota"]),
            {"cacah_nama": 0, "jumlah_bulan": 0, "cacah_settled": 0},
        )
        sel["cacah_nama"] += 1
        sel["jumlah_bulan"] += int(b["cacah_bulan"])
        if b["settled"]:
            sel["cacah_settled"] += 1
    return hasil


def pemegang_terbanyak(
    ringkasan_kuota: Dict[str, Dict[str, int]],
    medan: str = "cacah_nama",
    abaikan: Iterable[str] = (KUOTA_UTAMA,),
) -> Dict[str, Any]:
    """Aturan 64 dan KC-26: pemegang nilai ekstrem dilaporkan sebagai DAFTAR.

    Medan `berkas_terpanjang` pada `ukur_baris` V5 menamai satu dari dua pemegang
    yang seri, dan pemenangnya ditentukan urutan daftar. Medan ini tidak boleh
    mengulanginya: ia menyebut nilainya, seluruh pemegangnya, dan apakah seri.
    """
    kandidat = {k: v for k, v in ringkasan_kuota.items() if k not in set(abaikan)}
    if not kandidat:
        return {
            "medan": str(medan),
            "nilai": None,
            "pemegang": [],
            "cacah_pemegang": 0,
            "seri": False,
            "terukur": False,
        }
    nilai = max(int(v.get(medan) or 0) for v in kandidat.values())
    pemegang = sorted(k for k, v in kandidat.items() if int(v.get(medan) or 0) == nilai)
    return {
        "medan": str(medan),
        "nilai": int(nilai),
        "pemegang": pemegang,
        "cacah_pemegang": len(pemegang),
        "seri": len(pemegang) > 1,
        "terukur": True,
    }


def jumlah_bulan(
    baris: Sequence[Dict[str, Any]],
    kuota: Optional[str] = None,
    settled: Optional[bool] = None,
) -> int:
    """Jumlah simbol-bulan dengan saringan kuota dan/atau tanda SETTLED."""
    total = 0
    for b in baris:
        if kuota is not None and str(b["kuota"]) != str(kuota):
            continue
        if settled is not None and bool(b["settled"]) is not bool(settled):
            continue
        total += int(b["cacah_bulan"])
    return total


def cacah_nama(
    baris: Sequence[Dict[str, Any]],
    kuota: Optional[str] = None,
    settled: Optional[bool] = None,
) -> int:
    n = 0
    for b in baris:
        if kuota is not None and str(b["kuota"]) != str(kuota):
            continue
        if settled is not None and bool(b["settled"]) is not bool(settled):
            continue
        n += 1
    return n


def nama_bukan_akhiran_usdt(baris: Sequence[Dict[str, Any]]) -> List[str]:
    """DAFTAR nama yang tidak berakhiran USDT - calon anggota hanya-arsip."""
    return sorted(str(b["nama"]) for b in baris if not b["akhiran_usdt"])


def kendali(
    peta: Dict[str, int],
    simbol: str = SIMBOL_KENDALI,
    ambang: int = AMBANG_KENDALI,
) -> Dict[str, Any]:
    """Kendali positif: laporan sumber terbukti terbaca (aturan 50)."""
    ada = str(simbol) in peta
    cacah = int(peta.get(str(simbol)) or 0)
    return {
        "simbol": str(simbol),
        "cacah_bulan": cacah,
        "ambang": int(ambang),
        "ada": bool(ada),
        "sah": bool(ada) and cacah >= int(ambang),
    }


def kode_keluar(ringkasan: Dict[str, Any]) -> int:
    """Kode 2 bila laporan ini tidak berhak diklaim sebagai pengukuran."""
    if not ringkasan.get("kendali_sah"):
        return 2
    if int(ringkasan.get("cacah_nama_arsip") or 0) != CACAH_NAMA_TERCATAT:
        return 2
    if int(ringkasan.get("jumlah_bulan_arsip") or 0) != JUMLAH_BULAN_TERCATAT:
        return 2
    if int(ringkasan.get("cacah_nama_settled") or 0) != CACAH_SETTLED_TERCATAT:
        return 2
    return 0


def jalankan(akar: str = ".") -> Dict[str, Any]:
    basis = Path(akar)
    mentah = (basis / SUMBER).read_bytes()
    dok = json.loads(mentah.decode("utf-8"))
    peta = {str(k): int(v) for k, v in semesta_silang.cacah_bulan_arsip(dok).items()}

    baris = klasifikasi(peta)
    per_kuota = ringkas_kuota(baris)
    bukan_usdt = nama_bukan_akhiran_usdt(baris)
    terbanyak = pemegang_terbanyak(per_kuota)
    kend = kendali(peta)

    bulan_usdt_bukan_settled = jumlah_bulan(baris, kuota=KUOTA_UTAMA, settled=False)
    cacah_busd = int((per_kuota.get("BUSD") or {}).get("cacah_nama") or 0)
    cacah_usdc = int((per_kuota.get("USDC") or {}).get("cacah_nama") or 0)

    ringkasan: Dict[str, Any] = {
        "cacah_nama_arsip": len(baris),
        "jumlah_bulan_arsip": jumlah_bulan(baris),
        "cacah_nama_settled": cacah_nama(baris, settled=True),
        "jumlah_bulan_settled": jumlah_bulan(baris, settled=True),
        "cacah_nama_akhiran_usdt": len(baris) - len(bukan_usdt),
        "cacah_nama_bukan_akhiran_usdt": len(bukan_usdt),
        "cacah_nama_kuota_usdt": cacah_nama(baris, kuota=KUOTA_UTAMA),
        "cacah_nama_kuota_usdt_bukan_settled": cacah_nama(
            baris, kuota=KUOTA_UTAMA, settled=False
        ),
        "jumlah_bulan_usdt_bukan_settled": bulan_usdt_bukan_settled,
        "cacah_kuota_terpakai": len(per_kuota),
        "cacah_nama_tak_dikenal": int(
            (per_kuota.get(KUOTA_TAK_DIKENAL) or {}).get("cacah_nama") or 0
        ),
        "cacah_busd": cacah_busd,
        "cacah_usdc": cacah_usdc,
        "cacah_busd_usdc": cacah_busd + cacah_usdc,
        "terbanyak_bukan_usdt": terbanyak,
        "selisih_bulan_terhadap_penyebut": bulan_usdt_bukan_settled
        - PENYEBUT_BULAN_TERCATAT,
        "selisih_bulan_terhadap_serapan": bulan_usdt_bukan_settled
        - SIMBOL_BULAN_DISERAP,
        "r_249_menang": bulan_usdt_bukan_settled > PENYEBUT_BULAN_TERCATAT,
        "r_257_menang": (
            len(bukan_usdt) == CACAH_NAMA_TERCATAT - PENYEBUT_SIMBOL_TERCATAT
            and (len(baris) - len(bukan_usdt)) == PENYEBUT_SIMBOL_TERCATAT
        ),
        "r_258_menang": (
            bool(set(terbanyak.get("pemegang") or []) & {"BUSD", "USDC"})
            and (cacah_busd + cacah_usdc) >= AMBANG_BUSD_USDC
        ),
        "kendali": kend,
        "kendali_sah": kend["sah"],
    }

    return {
        "bukan_bukti": False,
        "versi_semesta_kuota": VERSI,
        "sidik_kode": sidik_kode(),
        "sidik_data": hashlib.sha256(mentah).hexdigest(),
        "sumber": [SUMBER],
        "definisi": {
            "kuota": (
                "DUGAAN kuota dari akhiran nama sesudah tanda SETTLED dipisahkan; "
                "bukan kuota yang dibaca dari metadata bursa"
            ),
            "simbol_bulan": (
                "bulan yang arsip TERBITKAN pada interval 1m, bukan bulan yang "
                "lolos gerbang kehidupan; dilarang dipakai sebagai penyebut "
                "kematian (aturan 30, 63)"
            ),
            "pemegang_terbanyak": (
                "DAFTAR seluruh kuota pemegang nilai ekstrem beserta medan seri "
                "(aturan 64, KC-26)"
            ),
        },
        "per_kuota": per_kuota,
        "terbanyak_bukan_usdt": terbanyak,
        "nama_bukan_akhiran_usdt": bukan_usdt,
        "baris": baris,
        "ringkasan": ringkasan,
        "catatan_batas": (
            "kuota disimpulkan dari NAMA; nama adalah petunjuk kuat tetapi tetap "
            "petunjuk. Himpunan 'tidak berakhiran USDT' dan himpunan 'hanya-arsip' "
            "tidak boleh dianggap identik tanpa R-257 menang (aturan 62)"
        ),
        "catatan_penggugur": (
            "kendali BTCUSDT di bawah ambang, cacah nama bukan 937, jumlah bulan "
            "bukan 21.789, atau cacah nama SETTLED bukan 15 membatalkan seluruh "
            "angka (aturan 24, 50)"
        ),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def ringkas(laporan: Dict[str, Any]) -> Dict[str, Any]:
    """Berkas kecil pendamping (aturan 52): tanpa daftar baris penuh."""
    return {
        "bukan_bukti": False,
        "versi_semesta_kuota": laporan.get("versi_semesta_kuota"),
        "sidik_kode": laporan.get("sidik_kode"),
        "sidik_data": laporan.get("sidik_data"),
        "per_kuota": laporan.get("per_kuota"),
        "terbanyak_bukan_usdt": laporan.get("terbanyak_bukan_usdt"),
        "ringkasan": laporan.get("ringkasan"),
        "waktu_utc": laporan.get("waktu_utc"),
    }


def main() -> int:
    laporan = jalankan()
    Path(KELUARAN).parent.mkdir(parents=True, exist_ok=True)
    Path(KELUARAN).write_text(
        json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    teks = (
        json.dumps(ringkas(laporan), ensure_ascii=False, indent=2, sort_keys=True)
        + "\n"
    )
    Path(KELUARAN_RINGKAS).write_text(teks, encoding="utf-8")
    print(teks)
    return kode_keluar(laporan["ringkasan"])


if __name__ == "__main__":
    raise SystemExit(main())
