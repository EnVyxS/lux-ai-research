"""Silangkan kehidupan semesta dengan lubang funding — tanpa menyentuh jaringan.

STATE v30 meninggalkan satu pertanyaan yang menentukan nasib ADR-A002 §10: dari
1.401 simbol-bulan MATI, 456 berada di kohort puncak funding 2025-07, sedangkan
**945 lainnya berada di luarnya**. Apakah yang 945 itu juga kehilangan funding?

- Bila hampir semuanya kehilangan funding, maka lubang funding dan kematian
  pasar adalah satu gejala, dan tafsir "perubahan rezim penerbitan" melemah.
- Bila banyak di antaranya MATI sementara funding-nya ADA, maka arsip funding
  menerbitkan funding bagi pasar yang tidak diperdagangkan, dan kedua gejala itu
  BERBEDA — tebing funding tidak dapat dijelaskan oleh kematian pasar.

Keduanya adalah kesimpulan besar, dan keduanya dapat gugur. Karena itu modul ini
dibuat sebelum tafsir apa pun ditulis.

## Mengapa modul ini tidak mengunduh apa pun

Seluruh bahannya sudah di-commit: `reports/kehidupan_arsip_<0..7>.json` (status
per simbol-bulan bagi 19.586 simbol-bulan lolos gerbang) dan
`reports/funding_semesta.json` (`per_simbol[].klines_tanpa_funding`, yakni bulan
klines yang tidak punya funding). Tidak ada listing baru, tidak ada unduhan,
tidak ada aset rilis. Satu job ringan cukup.

## Yang TIDAK boleh disimpulkan dari laporan ini

Irisan bukan sebab (aturan 10). Simbol-bulan yang MATI dan sekaligus kehilangan
funding tidak membuktikan salah satu menyebabkan yang lain; keduanya bisa lahir
dari satu delisting. Yang diukur di sini hanyalah BENTUK irisannya.

Penyebutnya juga wajib disebut: 19.586 simbol-bulan yang LOLOS gerbang dan
terkemas di tar utama, BUKAN 19.598 (aturan 30, 44). Lubang funding yang jatuh
pada simbol-bulan di luar penyebut itu — misalnya dua belas simbol-bulan
karantina — dicacah tersendiri sebagai `cacah_lubang_tak_dikenal` dan TIDAK
diam-diam dibuang.

## Kendali positif (aturan 50)

Kesimpulan di sini bersandar pada KETIADAAN nama bulan di daftar funding. Tanpa
kendali, daftar yang gagal terbaca akan tampak sebagai "semua funding hilang".
Kendalinya dipilih dari data SEBELUM tafsir apa pun: tiga simbol-bulan dengan
`byte_parquet` terbesar di seluruh semesta. Ketiganya WAJIB terbaca HIDUP dan
WAJIB punya funding. Bila satu saja gagal, `kendali_sah` false, kode keluar 2,
dan seluruh angka irisan batal.

Medan penggugur lain (aturan 24): `selisih_penyebut`, `selisih_mati`, dan
`selisih_kohort` membandingkan apa yang terbaca sekarang dengan angka yang sudah
diterbitkan di STATE v30 (19.586 / 1.401 / 456). Bila salah satunya bukan nol,
yang terbaca bukan laporan yang sama, dan kode keluar 2 — ini penangkal langsung
terhadap laporan basi yang berulang kali hampir menipu saya.

## Pembulatan (aturan 53)

`kohort_ekor.bagian` MEMBULATKAN ke empat desimal. Itu dipakai apa adanya di
sini, dan tidak satu pun bagian dihitung atas penyebut nol — penyebut nol
menghasilkan null, bukan 0 (aturan 41, 46).

## Praregistrasi ramalan — ditulis SEBELUM run

- **R-210** — dari **945** simbol-bulan MATI di luar kohort puncak, yang juga
  kehilangan funding berjumlah dalam pita **150..400**. Satuan: SIMBOL-BULAN.
  Penyebut eksplisit: 945 = 1.401 MATI semesta dikurangi 456 MATI kohort puncak.
  Dasar pita: seluruh lubang funding semesta 880, dan 456 di antaranya sudah
  terpakai kohort puncak, sehingga sisa lubang yang mungkin beririsan paling
  banyak 424; batas bawah 150 dipasang agar ramalan ini gugur bila irisannya
  ternyata kecil. Bila hasilnya di bawah 150, tafsir "dua gejala berbeda" menang
  dan saya wajib mencatatnya MELESET, bukan membenarkannya belakangan.
- **R-211** — CI pada commit ini mengumpulkan **312 butir** dengan kode keluar
  **0**. Dasar: 291 butir terverifikasi pada run `30420236800`, ditambah 21 butir
  baru dari `tests/test_silang_funding.py` (18 fungsi berbutir tunggal + 1 fungsi
  berparameter tiga kasus). Satuan: BUTIR yang dikumpulkan pytest (aturan 38, 47,
  53 — perilaku setiap fungsi yang diuji sudah dibaca lebih dulu).

Aturan yang mengikat: 10, 16, 20, 21, 22, 24, 29, 30, 41, 44, 45, 46, 47, 50,
52, 53.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from . import kehidupan, kehidupan_arsip, kohort_ekor

VERSI = 1
TOTAL_PECAHAN = kehidupan_arsip.TOTAL_PECAHAN
SUMBER_FUNDING = "reports/funding_semesta.json"
KELUARAN = "reports/silang_funding.json"
KELUARAN_RINGKAS = "reports/silang_funding_ringkas.json"
KENDALI_CACAH = 3

# Angka yang sudah diterbitkan di STATE v30; dipakai sebagai penggugur, BUKAN
# sebagai masukan perhitungan (aturan 21, 24).
PENYEBUT_TERCATAT = 19586
MATI_TERCATAT = 1401
KOHORT_TERCATAT = 456

BERKAS_DICAP = ["kehidupan.py", "kehidupan_arsip.py", "silang_funding.py"]

Kunci = Tuple[str, str]


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


def baca_laporan_kehidupan(
    akar: str = ".", total: int = TOTAL_PECAHAN
) -> Tuple[Dict[Kunci, str], Dict[Kunci, int], Dict[str, Any]]:
    """Status dan byte parquet per simbol-bulan dari laporan pecahan yang ada.

    Laporan yang tidak ada TIDAK dianggap kosong: namanya dicatat dan
    `sidik_seragam` menjadi false, sehingga kode keluar 2 (aturan 52).
    """
    status: Dict[Kunci, str] = {}
    byte_parquet: Dict[Kunci, int] = {}
    sidik: List[str] = []
    hilang: List[str] = []
    ganda = 0
    for i in range(total):
        nama = kehidupan_arsip.nama_keluaran(i)
        jalur = Path(akar) / nama
        if not jalur.exists():
            hilang.append(nama)
            continue
        isi = json.loads(jalur.read_text(encoding="utf-8"))
        sidik.append(str(isi.get("sidik_kode")))
        for baris in isi.get("baris") or []:
            k = (str(baris.get("simbol")), str(baris.get("bulan")))
            if k in status:
                ganda += 1
                continue
            status[k] = str(baris.get("status"))
            byte_parquet[k] = int(baris.get("byte_parquet") or 0)
    meta = {
        "total_pecahan": total,
        "cacah_laporan_dibaca": total - len(hilang),
        "laporan_hilang": hilang,
        "sidik_kode_laporan": sorted(set(sidik)),
        "sidik_seragam": bool(sidik) and len(set(sidik)) == 1 and not hilang,
        "cacah_kunci_ganda": ganda,
    }
    return status, byte_parquet, meta


def lubang_funding(funding: Dict[str, Any]) -> Tuple[Set[Kunci], Dict[str, Any]]:
    """Himpunan simbol-bulan yang punya klines tetapi TIDAK punya funding."""
    hilang: Set[Kunci] = set()
    ganda = 0
    for baris in funding.get("per_simbol") or []:
        simbol = str(baris.get("simbol") or "")
        for bulan in baris.get("klines_tanpa_funding") or []:
            k = (simbol, str(bulan))
            if k in hilang:
                ganda += 1
            hilang.add(k)
    return hilang, {"cacah_lubang_funding": len(hilang), "cacah_lubang_ganda": ganda}


def kohort_simbol_bulan(funding: Dict[str, Any]) -> Set[Kunci]:
    """Simbol-bulan EKOR milik anggota kohort puncak.

    Lubang ekor bersifat berurutan sampai bulan terakhir, sehingga bulan hilang
    yang tidak lebih kecil daripada `mulai_lubang_ekor` tepat membentuk ekornya.
    Anggota tanpa bulan-mulai TIDAK menyumbang apa pun (aturan 46).
    """
    kohort = funding.get("kohort_puncak") or {}
    anggota = {str(s) for s in (kohort.get("simbol") or [])}
    keluar: Set[Kunci] = set()
    for baris in funding.get("per_simbol") or []:
        simbol = str(baris.get("simbol") or "")
        if simbol not in anggota:
            continue
        mulai = baris.get("mulai_lubang_ekor")
        if not mulai:
            continue
        for bulan in baris.get("klines_tanpa_funding") or []:
            if str(bulan) >= str(mulai):
                keluar.add((simbol, str(bulan)))
    return keluar


def silang(status: Dict[Kunci, str], lubang: Set[Kunci]) -> Dict[str, Dict[str, int]]:
    """Tabel status x ketersediaan funding; keempat status dilapor walau nol."""
    tabel: Dict[str, Dict[str, int]] = {
        st: {"funding_hilang": 0, "funding_ada": 0}
        for st in (
            kehidupan.STATUS_MATI,
            kehidupan.STATUS_SEPI,
            kehidupan.STATUS_HIDUP,
            kehidupan.STATUS_TAK_TERUKUR,
        )
    }
    for k, st in status.items():
        sel = tabel.setdefault(str(st), {"funding_hilang": 0, "funding_ada": 0})
        sel["funding_hilang" if k in lubang else "funding_ada"] += 1
    return tabel


def _bagian(a: int, b: int) -> Optional[float]:
    """Aturan 41/46: penyebut nol menghasilkan null, bukan nol."""
    return kohort_ekor.bagian(a, b) if b else None


def rincian_mati(
    status: Dict[Kunci, str], lubang: Set[Kunci], kohort: Set[Kunci]
) -> Dict[str, Any]:
    """Pisahkan simbol-bulan MATI menurut kohort puncak dan lubang funding."""
    baris: List[Dict[str, Any]] = []
    dalam = luar = dalam_lubang = luar_lubang = 0
    for k in sorted(k for k, st in status.items() if st == kehidupan.STATUS_MATI):
        di_kohort = k in kohort
        ada_lubang = k in lubang
        if di_kohort:
            dalam += 1
            dalam_lubang += 1 if ada_lubang else 0
        else:
            luar += 1
            luar_lubang += 1 if ada_lubang else 0
        baris.append(
            {
                "simbol": k[0],
                "bulan": k[1],
                "di_kohort_puncak": di_kohort,
                "lubang_funding": ada_lubang,
            }
        )
    return {
        "baris_mati": baris,
        "cacah_mati": len(baris),
        "cacah_mati_di_kohort": dalam,
        "cacah_mati_luar_kohort": luar,
        "cacah_mati_di_kohort_dengan_lubang_funding": dalam_lubang,
        "cacah_mati_luar_kohort_dengan_lubang_funding": luar_lubang,
        "cacah_mati_luar_kohort_funding_ada": luar - luar_lubang,
        "bagian_mati_luar_kohort_dengan_lubang_funding": _bagian(luar_lubang, luar),
    }


def kendali_silang(
    byte_parquet: Dict[Kunci, int],
    status: Dict[Kunci, str],
    lubang: Set[Kunci],
    cacah: int = KENDALI_CACAH,
) -> List[Dict[str, Any]]:
    """Kendali positif: simbol-bulan berparquet terbesar, dipilih tanpa melihat
    status maupun funding. Urutan kunci deterministik (aturan 50)."""
    urut = sorted(byte_parquet.items(), key=lambda kv: (-int(kv[1]), kv[0][0], kv[0][1]))
    return [
        {
            "simbol": k[0],
            "bulan": k[1],
            "byte_parquet": int(b),
            "status": status.get(k),
            "funding_ada": k not in lubang,
        }
        for k, b in urut[:cacah]
    ]


def kendali_sah(kendali: List[Dict[str, Any]]) -> bool:
    return bool(kendali) and all(
        k.get("status") == kehidupan.STATUS_HIDUP and k.get("funding_ada")
        for k in kendali
    )


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
    for medan in ("selisih_penyebut", "selisih_mati", "selisih_kohort"):
        if int(ringkasan.get(medan) or 0) != 0:
            return 2
    return 0


def jalankan(akar: str = ".", total: int = TOTAL_PECAHAN) -> Dict[str, Any]:
    status, byte_parquet, meta = baca_laporan_kehidupan(akar=akar, total=total)
    mentah = (Path(akar) / SUMBER_FUNDING).read_bytes()
    funding = json.loads(mentah.decode("utf-8"))

    lubang, meta_lubang = lubang_funding(funding)
    kohort = kohort_simbol_bulan(funding)
    tabel = silang(status, lubang)
    rincian = rincian_mati(status, lubang, kohort)
    kendali = kendali_silang(byte_parquet, status, lubang)

    ringkasan: Dict[str, Any] = {
        "penyebut_kehidupan": len(status),
        "cacah_kohort_puncak": len(kohort),
        "cacah_lubang_tak_dikenal": len(lubang - set(status)),
        "selisih_penyebut": len(status) - PENYEBUT_TERCATAT,
        "selisih_mati": int(rincian["cacah_mati"]) - MATI_TERCATAT,
        "selisih_kohort": len(kohort) - KOHORT_TERCATAT,
        "tabel_silang": tabel,
        "kendali": kendali,
        "kendali_sah": kendali_sah(kendali),
        "bulan_klines_funding": int(
            ((funding.get("penyebut") or {}).get("bulan_klines")) or 0
        ),
    }
    ringkasan.update(meta)
    ringkasan.update(meta_lubang)
    ringkasan.update({k: v for k, v in rincian.items() if k != "baris_mati"})

    return {
        "bukan_bukti": False,
        "versi_silang_funding": VERSI,
        "sidik_kode": sidik_kode(),
        "sidik_data_funding": hashlib.sha256(mentah).hexdigest(),
        "sidik_kode_funding": funding.get("sidik_kode"),
        "versi_funding": funding.get("versi_funding"),
        "sumber": [SUMBER_FUNDING]
        + [kehidupan_arsip.nama_keluaran(i) for i in range(total)],
        "definisi": {
            "lubang_funding": "bulan punya klines tetapi tidak punya fundingRate",
            "di_kohort_puncak": "simbol-bulan EKOR milik anggota kohort_puncak",
            "status": "dibaca apa adanya dari laporan kehidupan_arsip",
        },
        "baris_mati": rincian["baris_mati"],
        "ringkasan": ringkasan,
        "catatan_tafsir": (
            "irisan BUKAN sebab: simbol-bulan yang MATI sekaligus kehilangan "
            "funding tidak membuktikan salah satu menyebabkan yang lain; "
            "keduanya dapat lahir dari satu delisting (aturan 10)"
        ),
        "catatan_penyebut": (
            "penyebut kehidupan adalah 19.586 simbol-bulan LOLOS gerbang, bukan "
            "19.598; lubang funding yang jatuh di luar penyebut itu dicacah "
            "sebagai cacah_lubang_tak_dikenal dan tidak dibuang (aturan 30, 44)"
        ),
        "catatan_penggugur": (
            "sidik_seragam false, laporan pecahan kurang, kunci ganda, atau "
            "kendali_sah false membatalkan seluruh angka; selisih_penyebut, "
            "selisih_mati, dan selisih_kohort bukan nol berarti yang terbaca "
            "bukan laporan yang sudah diterbitkan di STATE v30 (aturan 24)"
        ),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def berkas_ringkas(laporan: Dict[str, Any], teks_sumber: str) -> Dict[str, Any]:
    """Aturan 52: ringkasan terbaca utuh yang menyebut sidik laporan penuhnya."""
    byte_sumber = teks_sumber.encode("utf-8")
    return {
        "versi_silang_funding": laporan.get("versi_silang_funding"),
        "sidik_kode": laporan.get("sidik_kode"),
        "sidik_data_funding": laporan.get("sidik_data_funding"),
        "berkas_sumber": KELUARAN,
        "byte_sumber": len(byte_sumber),
        "sidik_sumber": hashlib.sha256(byte_sumber).hexdigest(),
        "definisi": laporan.get("definisi"),
        "ringkasan": laporan.get("ringkasan"),
    }


def main() -> int:
    laporan = jalankan()
    teks = json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    Path(KELUARAN).parent.mkdir(parents=True, exist_ok=True)
    Path(KELUARAN).write_text(teks, encoding="utf-8")
    ringkas = berkas_ringkas(laporan, teks)
    Path(KELUARAN_RINGKAS).write_text(
        json.dumps(ringkas, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(ringkas, ensure_ascii=False, indent=2, sort_keys=True))
    return kode_keluar(laporan["ringkasan"])


if __name__ == "__main__":
    raise SystemExit(main())
