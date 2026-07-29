"""Sebaran KUOTA dan JENIS semesta arsip - V3: taksonomi kanonik dipakai.

Riwayat singkat. V1 (`f5cebf04`) mencacah kuota 937 nama arsip: R-249 TEPAT,
R-257 dan R-258 MELESET, klaim lama "150 hanya-arsip hampir seluruhnya BUSD/USDC"
DICABUT. V2 (`3a3e85e1`) menyilangkan penyebut kehidupan yang sebenarnya: R-261
dan R-262 TEPAT, R-263 MELESET dengan arah terbalik, dan selisih 163 terurai
menjadi 12 (di dalam penyebut) + 151 (tiga nama di luar penyebut).

## Mengapa V3 ada: KC-29

V1 dan V2 mengarang klasifikasinya sendiri - `kuota_dasar`, `KUOTA_URUT`,
`TAK_DIKENAL` - padahal taksonomi **kanonik** sudah ada di repo sebagai
`lux_ai/semesta/taksonomi.py` dan sudah dipakai gerbang serapan lewat
`pecahan.simbol_pecahan`. Akibatnya terukur: kategori `TAK_DIKENAL` 51 nama yang
saya perlakukan sebagai misteri sebenarnya 50 `futures_kedaluwarsa` (`BTCUSDT_*`
24, `ETHUSDT_*` 24, `BTCBUSD_*` 2) ditambah 1 `perpetual_usd1` (`BTCUSD1`), sebab
`taksonomi.KUTIPAN` memuat `USD1` dan `POLA_EKSPIRASI` menangkap nama bertanggal.
Itulah KC-29: taksonomi paralel yang melahirkan kategori sisa palsu.

V3 mengimpor `taksonomi.jenis_instrumen` dan memakainya apa adanya (aturan 36).
Klasifikasi kuota buatan sendiri TIDAK dihapus - ia dipertahankan berdampingan
agar penyimpangan kedua taksonomi terlihat, bukan tersembunyi. Menghapusnya akan
menghilangkan jejak cacatnya sendiri.

## Hipotesis TIDAK dijadikan penggugur

R-266 memperkirakan `cacah_perpetual_usdt` = 787 dan
`cacah_perpetual_usdt_luar_penyebut` = 0. Godaan besarnya adalah menjadikan
keduanya penggugur seperti kendali BTCUSDT. Itu ditolak dengan sengaja: penggugur
adalah premis yang saya percayai dan bersedia batalkan seluruh laporan untuknya,
sedangkan R-266 adalah **hipotesis yang sedang diuji**. Menjadikan hipotesis
sebagai penggugur berarti laporan menolak melahirkan angka yang membantah saya -
bentuk paling halus dari kecurangan. Karena itu keduanya dilaporkan sebagai medan
biasa, dan kode keluar tetap 0 walau R-266 gugur.

Penggugur tetap yang lama: kendali BTCUSDT >= 60 bulan, cacah nama 937, jumlah
bulan 21.789, cacah SETTLED 15, cacah penyebut 787, bulan lolos 19.586, dan
penyebut wajib himpunan bagian arsip.

## Batas yang tetap berlaku

Kuota masih DUGAAN dari nama, dan taksonomi kanonik pun mengakui batasnya sendiri:
`taksonomi.CATATAN_BATAS` menyatakan token saham dan komoditas (`AAPLUSDT`,
`XAUUSDT`) tidak dapat dibedakan dari perpetual koin lewat bentuk nama, sehingga
keduanya IKUT masuk `perpetual_usdt` - yakni ikut masuk penyebut 787. Setiap
tafsir kadar kematian sebagai sifat "pasar kripto" wajib menyebut batas ini.
Simbol-bulan di sini tetap bulan yang arsip TERBITKAN, kecuali
`bulan_lolos_gerbang` yang berasal dari penyebut kehidupan.

## Praregistrasi - sudah ditulis di jurnal 100 SEBELUM run ini

- **R-265** - `per_jenis_hanya_arsip` berbunyi `futures_kedaluwarsa` **50**,
  `sisa_settled` **15**, `indeks` **3**, `perpetual_busd` **41**, `perpetual_usdc`
  **39**, `perpetual_usd1` **1**, `basis_non_fiat` **1**, `perpetual_usdt` **0**,
  `tak_tergolong` **0**. Suku yang paling diragukan: `tak_tergolong`, sebab nama
  non-ASCII yang tidak berakhiran kutipan mana pun akan mendarat di situ.
- **R-266** - `cacah_perpetual_usdt` = **787** dan
  `cacah_perpetual_usdt_luar_penyebut` = **0**. Bila gugur, ada perpetual USDT yang
  hilang dari serapan - temuan yang lebih besar daripada seluruh modul ini.
- **R-267** - CI mengumpulkan **610 butir** dengan kode keluar 0. Dasar (aturan 54,
  56, 57): 598 terverifikasi pada run 30455491991 ditambah **12** fungsi `def
  test_` baru bernomor 47..58 di `tests/test_semesta_kuota.py`, tanpa
  `parametrize`; fungsi 1 hanya berubah nama menjadi `test_versi_tiga` sehingga
  tidak menambah cacah. 598 + 12 = 610.

Aturan yang mengikat: 10, 16, 20, 21, 22, 24, 29, 30, 36, 38, 44, 45, 46, 50, 52,
54, 56, 57, 58, 59, 62, 63, 64, 65, 66.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from ..semesta import taksonomi
from . import semesta_silang, silang_funding

VERSI = 3
SUMBER = semesta_silang.SUMBER_ARSIP
TOTAL_PECAHAN = semesta_silang.TOTAL_PECAHAN
KELUARAN = "reports/semesta_kuota.json"
KELUARAN_RINGKAS = "reports/semesta_kuota_ringkas.json"

TANDA_SETTLED: Tuple[str, ...] = ("_SETTLED", "SETTLED")

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

# Jenis kanonik yang menjadi semesta riset (pecahan.JENIS_DIIZINKAN).
JENIS_PENYEBUT = "perpetual_usdt"

SIMBOL_KENDALI = "BTCUSDT"
AMBANG_KENDALI = 60

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
# Berkas di luar paket serapan yang ikut menentukan angka (KC-29, aturan 22).
BERKAS_DICAP_LUAR = [("semesta", "taksonomi.py")]


def nama_keluaran() -> str:
    return KELUARAN


def nama_ringkas() -> str:
    return KELUARAN_RINGKAS


def berkas_dicap_penuh() -> List[Path]:
    """Jalur seluruh berkas yang dicap, termasuk yang di luar paket ini."""
    dasar = Path(__file__).parent
    jalur = [dasar / nama for nama in BERKAS_DICAP]
    for bagian in BERKAS_DICAP_LUAR:
        jalur.append(dasar.parent.joinpath(*bagian))
    return sorted(jalur, key=lambda p: (p.parent.name, p.name))


def sidik_kode() -> str:
    """Aturan 22: cap setiap berkas yang ikut menentukan angka ini."""
    h = hashlib.sha256()
    for jalur in berkas_dicap_penuh():
        h.update(jalur.read_bytes())
    return h.hexdigest()


def pisah_settled(nama: str) -> Tuple[str, bool]:
    teks = str(nama)
    for tanda in TANDA_SETTLED:
        if teks.endswith(tanda) and len(teks) > len(tanda):
            return teks[: -len(tanda)], True
    return teks, False


def kuota_dasar(dasar: str) -> str:
    teks = str(dasar)
    for kuota in KUOTA_URUT:
        if teks.endswith(kuota) and len(teks) > len(kuota):
            return kuota
    return KUOTA_TAK_DIKENAL


def jenis_nama(nama: str) -> str:
    """Jenis instrumen menurut taksonomi KANONIK - didelegasikan, tidak disalin.

    Penawar KC-29. Fungsi ini sengaja tipis: satu baris delegasi. Menambahkan
    logika apa pun di sini akan melahirkan taksonomi paralel yang kedua.
    """
    return taksonomi.jenis_instrumen(str(nama))


def kuota_nama(nama: str) -> Dict[str, Any]:
    dasar, settled = pisah_settled(nama)
    return {
        "nama": str(nama),
        "dasar": dasar,
        "settled": bool(settled),
        "kuota": kuota_dasar(dasar),
        "jenis": jenis_nama(nama),
        "akhiran_usdt": str(nama).endswith(KUOTA_UTAMA),
    }


def klasifikasi(peta: Dict[str, int]) -> List[Dict[str, Any]]:
    baris: List[Dict[str, Any]] = []
    for nama in sorted(peta):
        info = kuota_nama(nama)
        info["cacah_bulan"] = int(peta[nama])
        baris.append(info)
    return baris


def _ringkas_medan(
    baris: Sequence[Dict[str, Any]], medan: str
) -> Dict[str, Dict[str, int]]:
    hasil: Dict[str, Dict[str, int]] = {}
    for b in baris:
        sel = hasil.setdefault(
            str(b[medan]),
            {"cacah_nama": 0, "jumlah_bulan": 0, "cacah_settled": 0},
        )
        sel["cacah_nama"] += 1
        sel["jumlah_bulan"] += int(b["cacah_bulan"])
        if b["settled"]:
            sel["cacah_settled"] += 1
    return hasil


def ringkas_kuota(baris: Sequence[Dict[str, Any]]) -> Dict[str, Dict[str, int]]:
    return _ringkas_medan(baris, "kuota")


def ringkas_jenis(baris: Sequence[Dict[str, Any]]) -> Dict[str, Dict[str, int]]:
    """Sebaran menurut taksonomi kanonik; seluruh JENIS dilaporkan walau nol.

    Aturan 18 dan 24: kelas yang bernilai nol adalah bagian dari temuan. Bila
    `perpetual_usdt` bernilai 0 pada himpunan hanya-arsip, justru itulah isi
    R-265 - dan ia harus terbaca, bukan lenyap karena kuncinya tidak ada.
    """
    hasil = {
        nama: {"cacah_nama": 0, "jumlah_bulan": 0, "cacah_settled": 0}
        for nama in taksonomi.JENIS
    }
    hasil.update(_ringkas_medan(baris, "jenis"))
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
    return sorted(str(b["nama"]) for b in baris if not b["akhiran_usdt"])


def nama_berkuota(baris: Sequence[Dict[str, Any]], kuota: str) -> List[str]:
    return sorted(str(b["nama"]) for b in baris if str(b["kuota"]) == str(kuota))


def nama_berjenis(baris: Sequence[Dict[str, Any]], jenis: str) -> List[str]:
    return sorted(str(b["nama"]) for b in baris if str(b["jenis"]) == str(jenis))


def baca_penyebut(
    akar: str = ".", total: int = TOTAL_PECAHAN
) -> Tuple[List[str], Dict[str, int], int]:
    """Penyebut kehidupan apa adanya (aturan 36), lewat jalur yang sudah terbukti."""
    status, _byte_parquet, _meta = silang_funding.baca_laporan_kehidupan(
        akar=akar, total=total
    )
    return (
        semesta_silang.simbol_penyebut(status),
        cacah_lolos_per_simbol(status),
        len(status),
    )


def cacah_lolos_per_simbol(status: Dict[Tuple[str, str], Any]) -> Dict[str, int]:
    hasil: Dict[str, int] = {}
    for kunci in status:
        simbol = str(kunci[0])
        hasil[simbol] = hasil.get(simbol, 0) + 1
    return hasil


def himpunan_hanya_arsip(
    baris: Sequence[Dict[str, Any]], penyebut: Iterable[str]
) -> List[str]:
    p = {str(x) for x in penyebut}
    return sorted(str(b["nama"]) for b in baris if str(b["nama"]) not in p)


def per_kuota_himpunan(
    baris: Sequence[Dict[str, Any]], terpilih: Iterable[str]
) -> Dict[str, Dict[str, int]]:
    pilih = {str(x) for x in terpilih}
    return ringkas_kuota([b for b in baris if str(b["nama"]) in pilih])


def per_jenis_himpunan(
    baris: Sequence[Dict[str, Any]], terpilih: Iterable[str]
) -> Dict[str, Dict[str, int]]:
    """Sebaran JENIS kanonik atas subhimpunan nama - inti R-265."""
    pilih = {str(x) for x in terpilih}
    return ringkas_jenis([b for b in baris if str(b["nama"]) in pilih])


def perpetual_usdt_luar_penyebut(
    baris: Sequence[Dict[str, Any]], penyebut: Iterable[str]
) -> List[str]:
    """Nama bergolongan `perpetual_usdt` yang tidak ada di penyebut - inti R-266.

    Bila daftar ini tidak kosong, ada perpetual USDT yang arsip terbitkan tetapi
    serapan lewatkan. Itu BUKAN penggugur laporan: ia hipotesis yang sedang diuji.
    """
    p = {str(x) for x in penyebut}
    return sorted(
        str(b["nama"])
        for b in baris
        if str(b["jenis"]) == JENIS_PENYEBUT and str(b["nama"]) not in p
    )


def penyebut_luar_jenis(
    baris: Sequence[Dict[str, Any]], penyebut: Iterable[str]
) -> List[str]:
    """Simbol penyebut yang taksonomi kanonik TIDAK golongkan perpetual_usdt.

    Arah kebalikan dari `perpetual_usdt_luar_penyebut`; keduanya bersama menguji
    kesepadanan dua himpunan, bukan hanya satu arah (aturan 62).
    """
    jenis = {str(b["nama"]): str(b["jenis"]) for b in baris}
    return sorted(
        str(s) for s in penyebut if jenis.get(str(s), "tak_ada_di_arsip") != JENIS_PENYEBUT
    )


def urai_selisih(
    baris: Sequence[Dict[str, Any]],
    penyebut: Iterable[str],
    cacah_lolos: Dict[str, int],
) -> Dict[str, Any]:
    """Pecah selisih 19.749 lawan 19.586 menjadi dua sumbangan yang menutup."""
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
    """Kode 2 hanya untuk PREMIS yang gugur, bukan untuk hipotesis yang kalah."""
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
    per_jenis = ringkas_jenis(baris)
    bukan_usdt = nama_bukan_akhiran_usdt(baris)
    terbanyak = pemegang_terbanyak(per_kuota)
    kend = kendali(peta)

    penyebut, lolos_per_simbol, cacah_lolos = baca_penyebut(akar=akar, total=total)
    hanya_arsip = himpunan_hanya_arsip(baris, penyebut)
    per_kuota_hanya_arsip = per_kuota_himpunan(baris, hanya_arsip)
    per_jenis_hanya_arsip = per_jenis_himpunan(baris, hanya_arsip)
    urai = urai_selisih(baris, penyebut, lolos_per_simbol)
    pu_luar = perpetual_usdt_luar_penyebut(baris, penyebut)
    penyebut_bukan_jenis = penyebut_luar_jenis(baris, penyebut)
    penyebut_bukan_usdt = sorted(
        n for n in penyebut if not str(n).endswith(KUOTA_UTAMA)
    )
    penyebut_luar_arsip = sorted(n for n in penyebut if str(n) not in peta)

    bulan_usdt_bukan_settled = jumlah_bulan(baris, kuota=KUOTA_UTAMA, settled=False)
    cacah_busd = int((per_kuota.get("BUSD") or {}).get("cacah_nama") or 0)
    cacah_usdc = int((per_kuota.get("USDC") or {}).get("cacah_nama") or 0)
    ha_busd = int((per_kuota_hanya_arsip.get("BUSD") or {}).get("cacah_nama") or 0)
    ha_usdc = int((per_kuota_hanya_arsip.get("USDC") or {}).get("cacah_nama") or 0)
    cacah_pu = int((per_jenis.get(JENIS_PENYEBUT) or {}).get("cacah_nama") or 0)

    harapan_r265 = {
        "futures_kedaluwarsa": 50,
        "sisa_settled": 15,
        "indeks": 3,
        "perpetual_usdt": 0,
        "perpetual_usdc": 39,
        "perpetual_busd": 41,
        "perpetual_usd1": 1,
        "basis_non_fiat": 1,
        "tak_tergolong": 0,
    }
    r265 = all(
        int((per_jenis_hanya_arsip.get(k) or {}).get("cacah_nama") or 0) == v
        for k, v in harapan_r265.items()
    )

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
        "cacah_jenis_terpakai": sum(
            1 for v in per_jenis.values() if int(v.get("cacah_nama") or 0) > 0
        ),
        "cacah_perpetual_usdt": cacah_pu,
        "cacah_perpetual_usdt_luar_penyebut": len(pu_luar),
        "perpetual_usdt_luar_penyebut": pu_luar,
        "cacah_penyebut_bukan_perpetual_usdt": len(penyebut_bukan_jenis),
        "penyebut_bukan_perpetual_usdt": penyebut_bukan_jenis,
        "cacah_indeks": int((per_jenis.get("indeks") or {}).get("cacah_nama") or 0),
        "cacah_futures_kedaluwarsa": int(
            (per_jenis.get("futures_kedaluwarsa") or {}).get("cacah_nama") or 0
        ),
        "cacah_tak_tergolong": int(
            (per_jenis.get("tak_tergolong") or {}).get("cacah_nama") or 0
        ),
        "r_249_menang": bulan_usdt_bukan_settled > PENYEBUT_BULAN_TERCATAT,
        "r_261_menang": (
            len(penyebut_bukan_usdt) == 0
            and int(urai["cacah_nama_usdt_hanya_arsip"]) == 3
            and len(hanya_arsip) == CACAH_NAMA_TERCATAT - PENYEBUT_SIMBOL_TERCATAT
        ),
        "r_263_menang": int(urai["selisih_dari_hanya_arsip"]) <= 60,
        "r_265_menang": bool(r265),
        "r_266_menang": cacah_pu == PENYEBUT_SIMBOL_TERCATAT and len(pu_luar) == 0,
        "kendali": kend,
        "kendali_sah": kend["sah"],
    }

    return {
        "bukan_bukti": False,
        "versi_semesta_kuota": VERSI,
        "sidik_kode": sidik_kode(),
        "sidik_data": hashlib.sha256(mentah).hexdigest(),
        "sumber": [SUMBER],
        "berkas_dicap": [
            f"{p.parent.name}/{p.name}" for p in berkas_dicap_penuh()
        ],
        "definisi": {
            "kuota": (
                "DUGAAN kuota dari akhiran nama, taksonomi LOKAL modul ini; "
                "dipertahankan berdampingan dengan taksonomi kanonik agar "
                "penyimpangannya terlihat (KC-29)"
            ),
            "jenis": (
                "taksonomi KANONIK lux_ai/semesta/taksonomi.py, sama dengan yang "
                "dipakai gerbang serapan lewat pecahan.simbol_pecahan"
            ),
            "semesta_riset": (
                "perpetual_usdt; token saham dan komoditas IKUT masuk kelas ini "
                "sebab tidak dapat dibedakan lewat bentuk nama "
                "(taksonomi.CATATAN_BATAS)"
            ),
            "hanya_arsip": (
                "nama arsip yang tidak punya satu pun bulan LOLOS gerbang, "
                "dihitung dari penyebut kehidupan"
            ),
            "hipotesis_bukan_penggugur": (
                "R-265 dan R-266 dilaporkan sebagai medan biasa; kode keluar tetap "
                "0 walau keduanya gugur, sebab hipotesis yang dijadikan penggugur "
                "akan menolak melahirkan angka yang membantah peramalnya"
            ),
        },
        "per_kuota": per_kuota,
        "per_jenis": per_jenis,
        "per_kuota_hanya_arsip": per_kuota_hanya_arsip,
        "per_jenis_hanya_arsip": per_jenis_hanya_arsip,
        "terbanyak_bukan_usdt": terbanyak,
        "urai_selisih": urai,
        "nama_indeks": nama_berjenis(baris, "indeks"),
        "nama_tak_tergolong": nama_berjenis(baris, "tak_tergolong"),
        "nama_tak_dikenal": nama_berkuota(baris, KUOTA_TAK_DIKENAL),
        "nama_bukan_akhiran_usdt": bukan_usdt,
        "nama_hanya_arsip": hanya_arsip,
        "baris": baris,
        "ringkasan": ringkasan,
        "catatan_batas": (
            "kuota LOKAL disimpulkan dari NAMA; kategori TAK_DIKENAL 51 nama pada "
            "V1/V2 adalah artefak taksonomi paralel (KC-29), bukan sifat data - "
            "menurut taksonomi kanonik ia 50 futures_kedaluwarsa + 1 perpetual_usd1"
        ),
        "catatan_penggugur": (
            "kendali BTCUSDT di bawah ambang, cacah nama bukan 937, jumlah bulan "
            "bukan 21.789, cacah SETTLED bukan 15, cacah penyebut bukan 787, "
            "bulan lolos bukan 19.586, atau penyebut bukan himpunan bagian arsip "
            "membatalkan seluruh angka (aturan 24, 50). R-265 dan R-266 SENGAJA "
            "bukan penggugur"
        ),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def ringkas(laporan: Dict[str, Any]) -> Dict[str, Any]:
    """Berkas kecil pendamping (aturan 52): seluruh daftar yang wajib dibaca utuh."""
    return {
        "bukan_bukti": False,
        "versi_semesta_kuota": laporan.get("versi_semesta_kuota"),
        "sidik_kode": laporan.get("sidik_kode"),
        "sidik_data": laporan.get("sidik_data"),
        "berkas_dicap": laporan.get("berkas_dicap"),
        "per_kuota": laporan.get("per_kuota"),
        "per_jenis": laporan.get("per_jenis"),
        "per_kuota_hanya_arsip": laporan.get("per_kuota_hanya_arsip"),
        "per_jenis_hanya_arsip": laporan.get("per_jenis_hanya_arsip"),
        "terbanyak_bukan_usdt": laporan.get("terbanyak_bukan_usdt"),
        "urai_selisih": laporan.get("urai_selisih"),
        "nama_indeks": laporan.get("nama_indeks"),
        "nama_tak_tergolong": laporan.get("nama_tak_tergolong"),
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
