"""Sebaran KUOTA semesta arsip - V2: silang penyebut dan penguraian selisih.

V1 (commit `f5cebf04`, run 30454633506) mencacah kuota seluruh 937 nama arsip dan
menghasilkan tiga hal: R-249 TEPAT (19.749 simbol-bulan USDT bukan SETTLED, di
atas penyebut 19.586), R-257 MELESET (nama berakhiran USDT **790**, bukan 787;
bukan-USDT **147**, bukan 150), dan R-258 MELESET (pemegang terbanyak
`TAK_DIKENAL` 51 nama, sementara BUSD 41 + USDC 39 = 80 saja - klaim "150
hanya-arsip hampir seluruhnya BUSD/USDC" DICABUT, lihat jurnal 98, aturan 65,
KC-27).

V1 sengaja tidak menyentuh penyebut: ia bekerja dari satu laporan saja. Akibatnya
tiga utang lahir sekaligus, dan ketiganya dilunasi di sini.

## Yang ditambahkan V2

1. **Himpunan hanya-arsip yang SEBENARNYA.** V1 memakai "tidak berakhiran USDT"
   sebagai pengganti hanya-arsip, dan R-257 membuktikan pengganti itu keliru.
   V2 membaca penyebut kehidupan langsung lewat
   `silang_funding.baca_laporan_kehidupan` dan `semesta_silang.simbol_penyebut`
   (aturan 36: definisi dipakai apa adanya, tidak disalin ulang), lalu menyilangkan
   himpunan - persis alat yang dipakai `semesta_silang` untuk R-247.
2. **Identitas nama berkuota USDT yang hanya ada di arsip.** 790 - 787 = 3 adalah
   ARITMETIKA, dan hanya sah bila seluruh 787 penyebut memang berakhiran USDT.
   V2 tidak mengandaikannya: ia mendaftar nama-namanya dan mencacah penyebut yang
   TIDAK berakhiran USDT. Bila cacah itu bukan nol, R-261 gugur dan seluruh
   penguraian 150 = 147 + 3 di jurnal 98 harus ditulis ulang.
3. **Penguraian selisih 163.** Jurnal 98 mengakui bahwa alasan R-249 hanya
   menjelaskan 12 dari 163. V2 memecahnya menjadi dua sumbangan yang saling
   melengkapi secara identitas: bulan arsip milik simbol penyebut yang TIDAK lolos
   gerbang, dan bulan arsip milik nama USDT yang tidak pernah masuk penyebut.
4. **Daftar `TAK_DIKENAL` naik ke berkas RINGKAS** (aturan 52). V1 menaruhnya di
   laporan penuh yang terlalu besar untuk dibaca utuh, sehingga 51 nama itu
   terukur tetapi tidak terbaca - dan angka yang tidak terbaca utuh sama dengan
   tidak ada.

## Aturan 64 tetap dipatuhi

`pemegang_terbanyak` tidak diubah: ia selalu mengembalikan DAFTAR pemegang beserta
medan `seri` (KC-26).

## Kendali positif dan penggugur (aturan 24, 50)

BTCUSDT >= 60 bulan tetap kendali pertama. V2 menambah tiga penggugur: cacah
simbol penyebut wajib **787**, cacah simbol-bulan lolos gerbang wajib **19.586**,
dan penyebut wajib himpunan bagian arsip (`penyebut_bagian_arsip`). Bila salah
satu gugur, kode keluar 2 dan seluruh angka batal - sebab ketiganya adalah angka
yang sudah diverifikasi berulang kali, dan pergeserannya berarti artefak berubah,
bukan berarti temuan baru.

## Batas yang tetap berlaku

Kuota masih DUGAAN dari nama. Simbol-bulan di sini masih bulan yang DITERBITKAN
arsip, bukan yang lolos gerbang; hanya medan `bulan_lolos_gerbang` yang berasal
dari penyebut kehidupan. Angka apa pun dari modul ini tetap DILARANG dipakai
sebagai penyebut kematian (aturan 30, 63), dan seluruhnya tetap terbatas pada apa
yang arsip terbitkan.

## Praregistrasi ramalan - ditulis SEBELUM run

- **R-261** - seluruh 787 simbol penyebut berakhiran `USDT`
  (`cacah_penyebut_bukan_akhiran_usdt` = **0**), sehingga nama berkuota USDT bukan
  SETTLED yang hanya ada di arsip berjumlah **tepat 3** dan himpunan hanya-arsip
  berjumlah **150**. GUGUR bila salah satu berbeda. Ini menguji penguraian
  150 = 147 + 3 yang ditulis di jurnal 98; bila gugur, penguraian itu batal.
- **R-262** - sebaran kuota himpunan hanya-arsip berbunyi USDT **18** (15 SETTLED
  + 3), BUSD **41**, USDC **39**, `TAK_DIKENAL` **51**, BTC **1**. Ramalan MUDAH:
  ia hanya menjumlahkan angka V1 yang sudah terverifikasi, jadi ia menguji jalur
  penyaringan modul ini, bukan pemahaman saya. GUGUR bila satu angka berbeda.
- **R-263** - dari selisih 163, sumbangan nama USDT hanya-arsip
  (`selisih_dari_hanya_arsip`) berjumlah **paling banyak 60**, sehingga mayoritas
  selisih - sekurang-kurangnya 103 - berasal dari bulan yang arsip terbitkan bagi
  simbol penyebut tetapi TIDAK lolos gerbang kehidupan. GUGUR bila sumbangan nama
  hanya-arsip lebih dari 60. Ramalan ini benar-benar tidak saya ketahui: ketiga
  nama itu bisa saja berumur panjang.
- **R-264** - CI pada commit yang memuat berkas ini mengumpulkan **598 butir**
  dengan kode keluar 0. Dasar (aturan 54, 56, 57): 584 terverifikasi pada run
  30454633453 ditambah **14** fungsi `def test_` baru bernomor 33..46 di
  `tests/test_semesta_kuota.py`, tanpa `parametrize`; fungsi 1 hanya berubah nama
  menjadi `test_versi_dua` sehingga tidak menambah cacah. 584 + 14 = 598.

Cacah baris berkas ini SENGAJA tidak diramalkan (aturan 58, pilihan c).

Aturan yang mengikat: 10, 16, 20, 21, 22, 24, 30, 36, 38, 44, 45, 46, 50, 52, 54,
56, 57, 58, 59, 62, 63, 64, 65.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from . import semesta_silang, silang_funding

VERSI = 2
SUMBER = semesta_silang.SUMBER_ARSIP
TOTAL_PECAHAN = semesta_silang.TOTAL_PECAHAN
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
    "kehidupan_arsip.py",
    "semesta_kuota.py",
    "semesta_silang.py",
    "silang_funding.py",
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
    """Kuota dari akhiran nama dasar; TAK_DIKENAL bila tak ada yang cocok."""
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
    """Aturan 64 dan KC-26: pemegang nilai ekstrem dilaporkan sebagai DAFTAR."""
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
    """DAFTAR nama yang tidak berakhiran USDT - BUKAN himpunan hanya-arsip."""
    return sorted(str(b["nama"]) for b in baris if not b["akhiran_usdt"])


def nama_berkuota(baris: Sequence[Dict[str, Any]], kuota: str) -> List[str]:
    return sorted(str(b["nama"]) for b in baris if str(b["kuota"]) == str(kuota))


# --- V2: silang terhadap penyebut kehidupan -------------------------------


def baca_penyebut(
    akar: str = ".", total: int = TOTAL_PECAHAN
) -> Tuple[List[str], Dict[str, int], int]:
    """Penyebut kehidupan apa adanya (aturan 36), lewat jalur yang sudah terbukti.

    Mengembalikan daftar simbol penyebut, cacah bulan LOLOS per simbol, dan cacah
    seluruh simbol-bulan yang lolos gerbang.
    """
    status, _byte_parquet, _meta = silang_funding.baca_laporan_kehidupan(
        akar=akar, total=total
    )
    return (
        semesta_silang.simbol_penyebut(status),
        cacah_lolos_per_simbol(status),
        len(status),
    )


def cacah_lolos_per_simbol(status: Dict[Tuple[str, str], Any]) -> Dict[str, int]:
    """Cacah bulan yang LOLOS gerbang per simbol, dari kunci (simbol, bulan)."""
    hasil: Dict[str, int] = {}
    for kunci in status:
        simbol = str(kunci[0])
        hasil[simbol] = hasil.get(simbol, 0) + 1
    return hasil


def himpunan_hanya_arsip(
    baris: Sequence[Dict[str, Any]], penyebut: Iterable[str]
) -> List[str]:
    """Nama arsip yang tidak ada di penyebut - himpunan hanya-arsip SEBENARNYA."""
    p = {str(x) for x in penyebut}
    return sorted(str(b["nama"]) for b in baris if str(b["nama"]) not in p)


def per_kuota_himpunan(
    baris: Sequence[Dict[str, Any]], terpilih: Iterable[str]
) -> Dict[str, Dict[str, int]]:
    """Sebaran kuota atas subhimpunan nama - penawar KC-27."""
    pilih = {str(x) for x in terpilih}
    return ringkas_kuota([b for b in baris if str(b["nama"]) in pilih])


def urai_selisih(
    baris: Sequence[Dict[str, Any]],
    penyebut: Iterable[str],
    cacah_lolos: Dict[str, int],
) -> Dict[str, Any]:
    """Pecah selisih 19.749 lawan 19.586 menjadi dua sumbangan yang menutup.

    Identitas yang ditegakkan:
        (bulan arsip milik penyebut - bulan lolos) + bulan arsip milik nama USDT
        hanya-arsip = bulan USDT bukan SETTLED - bulan lolos
    """
    p = {str(x) for x in penyebut}
    bulan_penyebut = 0
    bulan_hanya_arsip = 0
    nama_hanya_arsip: List[str] = []
    for b in baris:
        if str(b["kuota"]) != KUOTA_UTAMA or bool(b["settled"]):
            continue
        if str(b["nama"]) in p:
            bulan_penyebut += int(b["cacah_bulan"])
        else:
            bulan_hanya_arsip += int(b["cacah_bulan"])
            nama_hanya_arsip.append(str(b["nama"]))
    lolos = sum(int(v) for v in cacah_lolos.values())
    total = bulan_penyebut + bulan_hanya_arsip
    dalam = bulan_penyebut - lolos
    return {
        "bulan_usdt_bukan_settled": total,
        "bulan_arsip_milik_penyebut": bulan_penyebut,
        "bulan_arsip_milik_hanya_arsip": bulan_hanya_arsip,
        "nama_usdt_hanya_arsip": sorted(nama_hanya_arsip),
        "cacah_nama_usdt_hanya_arsip": len(nama_hanya_arsip),
        "bulan_lolos_gerbang": lolos,
        "selisih_total": total - lolos,
        "selisih_dalam_penyebut": dalam,
        "selisih_dari_hanya_arsip": bulan_hanya_arsip,
        "identitas_utuh": dalam + bulan_hanya_arsip == total - lolos,
    }


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
    if int(ringkasan.get("cacah_penyebut_simbol") or 0) != PENYEBUT_SIMBOL_TERCATAT:
        return 2
    if int(ringkasan.get("bulan_lolos_gerbang") or 0) != PENYEBUT_BULAN_TERCATAT:
        return 2
    if not ringkasan.get("penyebut_bagian_arsip"):
        return 2
    return 0


def jalankan(akar: str = ".", total: int = TOTAL_PECAHAN) -> Dict[str, Any]:
    basis = Path(akar)
    mentah = (basis / SUMBER).read_bytes()
    dok = json.loads(mentah.decode("utf-8"))
    peta = {str(k): int(v) for k, v in semesta_silang.cacah_bulan_arsip(dok).items()}

    baris = klasifikasi(peta)
    per_kuota = ringkas_kuota(baris)
    bukan_usdt = nama_bukan_akhiran_usdt(baris)
    terbanyak = pemegang_terbanyak(per_kuota)
    kend = kendali(peta)

    penyebut, lolos_per_simbol, cacah_lolos = baca_penyebut(akar=akar, total=total)
    hanya_arsip = himpunan_hanya_arsip(baris, penyebut)
    per_kuota_hanya_arsip = per_kuota_himpunan(baris, hanya_arsip)
    urai = urai_selisih(baris, penyebut, lolos_per_simbol)
    penyebut_bukan_usdt = sorted(
        n for n in penyebut if not str(n).endswith(KUOTA_UTAMA)
    )
    penyebut_luar_arsip = sorted(n for n in penyebut if str(n) not in peta)

    bulan_usdt_bukan_settled = jumlah_bulan(baris, kuota=KUOTA_UTAMA, settled=False)
    cacah_busd = int((per_kuota.get("BUSD") or {}).get("cacah_nama") or 0)
    cacah_usdc = int((per_kuota.get("USDC") or {}).get("cacah_nama") or 0)
    ha_busd = int((per_kuota_hanya_arsip.get("BUSD") or {}).get("cacah_nama") or 0)
    ha_usdc = int((per_kuota_hanya_arsip.get("USDC") or {}).get("cacah_nama") or 0)

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
        "cacah_penyebut_simbol": len(penyebut),
        "cacah_penyebut_bukan_akhiran_usdt": len(penyebut_bukan_usdt),
        "penyebut_bukan_akhiran_usdt": penyebut_bukan_usdt,
        "cacah_penyebut_luar_arsip": len(penyebut_luar_arsip),
        "penyebut_bagian_arsip": len(penyebut_luar_arsip) == 0,
        "bulan_lolos_gerbang": cacah_lolos,
        "cacah_hanya_arsip": len(hanya_arsip),
        "cacah_hanya_arsip_busd_usdc": ha_busd + ha_usdc,
        "r_249_menang": bulan_usdt_bukan_settled > PENYEBUT_BULAN_TERCATAT,
        "r_261_menang": (
            len(penyebut_bukan_usdt) == 0
            and int(urai["cacah_nama_usdt_hanya_arsip"]) == 3
            and len(hanya_arsip) == CACAH_NAMA_TERCATAT - PENYEBUT_SIMBOL_TERCATAT
        ),
        "r_263_menang": int(urai["selisih_dari_hanya_arsip"]) <= 60,
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
                "bulan yang arsip TERBITKAN pada interval 1m; hanya medan "
                "bulan_lolos_gerbang berasal dari penyebut kehidupan"
            ),
            "hanya_arsip": (
                "nama arsip yang tidak punya satu pun bulan LOLOS gerbang, "
                "dihitung dari penyebut kehidupan - bukan dari akhiran nama"
            ),
            "pemegang_terbanyak": (
                "DAFTAR seluruh kuota pemegang nilai ekstrem beserta medan seri "
                "(aturan 64, KC-26)"
            ),
        },
        "per_kuota": per_kuota,
        "per_kuota_hanya_arsip": per_kuota_hanya_arsip,
        "terbanyak_bukan_usdt": terbanyak,
        "urai_selisih": urai,
        "nama_tak_dikenal": nama_berkuota(baris, KUOTA_TAK_DIKENAL),
        "nama_bukan_akhiran_usdt": bukan_usdt,
        "nama_hanya_arsip": hanya_arsip,
        "baris": baris,
        "ringkasan": ringkasan,
        "catatan_batas": (
            "kuota disimpulkan dari NAMA; nama adalah petunjuk kuat tetapi tetap "
            "petunjuk. V1 memakai 'tidak berakhiran USDT' sebagai pengganti "
            "hanya-arsip dan R-257 membuktikan pengganti itu keliru; V2 memakai "
            "penyebut kehidupan yang sebenarnya (aturan 62)"
        ),
        "catatan_penggugur": (
            "kendali BTCUSDT di bawah ambang, cacah nama bukan 937, jumlah bulan "
            "bukan 21.789, cacah SETTLED bukan 15, cacah penyebut bukan 787, "
            "bulan lolos bukan 19.586, atau penyebut bukan himpunan bagian arsip "
            "membatalkan seluruh angka (aturan 24, 50)"
        ),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def ringkas(laporan: Dict[str, Any]) -> Dict[str, Any]:
    """Berkas kecil pendamping (aturan 52).

    V2 MENAIKKAN daftar TAK_DIKENAL, daftar hanya-arsip berkuota USDT, dan sebaran
    kuota hanya-arsip ke berkas ini, sebab V1 menaruhnya di laporan penuh yang
    terlalu besar untuk dibaca utuh - dan angka yang tidak terbaca utuh tidak ada.
    Daftar 937 baris tetap tinggal di laporan penuh.
    """
    return {
        "bukan_bukti": False,
        "versi_semesta_kuota": laporan.get("versi_semesta_kuota"),
        "sidik_kode": laporan.get("sidik_kode"),
        "sidik_data": laporan.get("sidik_data"),
        "per_kuota": laporan.get("per_kuota"),
        "per_kuota_hanya_arsip": laporan.get("per_kuota_hanya_arsip"),
        "terbanyak_bukan_usdt": laporan.get("terbanyak_bukan_usdt"),
        "urai_selisih": laporan.get("urai_selisih"),
        "nama_tak_dikenal": laporan.get("nama_tak_dikenal"),
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
