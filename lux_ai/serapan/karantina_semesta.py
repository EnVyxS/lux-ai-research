"""Daftar karantina TERUKUR: siapa yang benar-benar ada di tar karantina.

Alat uji R-291. Sampai jurnal 115, kedua belas simbol-bulan karantina hanya
dikenal lewat dua jalan tak langsung: aritmetika penyebut (19.598 − 19.586 = 12)
dan bulan ABSEN yang diukur `bulan_absen.py` (11 dalam rentang + 1 tepi). Daftar
karantina itu sendiri **belum pernah dibaca**. Modul ini membacanya.

## Mengapa harus di runner, bukan di agen

`reports/manifes_pecahan_2.json` berukuran 2.446.093 byte; alat baca agen menolak
berkas sebesar itu. Aturan 52 berlaku: yang tak terbaca utuh dianggap TIDAK ADA.
Satu-satunya jalan sah adalah kode yang di-commit lalu dijalankan Actions, dan
laporannya dibaca pada ref runner (aturan 38).

## Sumber medan — dibaca, bukan ditebak (aturan 71)

`pecahan.py` VERSI 6 menyusun manifes lewat `serap.ringkas`, yang memanggil
`serap.ringkas_karantina`. Dari sana datang blok `karantina` dengan
`daftar_karantina`, dan tiap entrinya membawa `simbol`, `bulan`, `pelanggaran`,
`baris`, `parquet_karantina`, dan `checksum_zip_sha256`. Nama-nama itu dikutip
dari kode yang menulisnya, bukan dari ingatan. `rilis.py` sengaja TIDAK dipakai
sebagai sumber nama: laporan pengemas hanya menyimpan bagian tar beserta
`cacah_berkas`, jadi ia tahu BERAPA berkas karantina, tidak tahu SIAPA.

## Praregistrasi (ditulis sebelum run)

- **R-291** sudah terkunci di jurnal 115 §7 dan TIDAK diubah di sini: daftar
  karantina memuat tepat 12 simbol-bulan, himpunannya sama persis dengan
  `R291_HIMPUNAN`. GUGUR bila cacahnya bukan 12 atau ada nama-bulan lain.
- **R-294 (MUDAH)** — CI mengumpulkan **722 butir**, kode keluar 0. Dasar: 694
  butir terverifikasi pada run 30479093362, ditambah 28 fungsi `def test_` di
  `tests/test_karantina_semesta.py` tanpa satu pun `parametrize` (aturan
  54/56/57). Satuan: BUTIR yang dikumpulkan pytest.

## Yang diukur di luar ramalan

`pelanggaran` tiap entri dan `nisbah_lilin` = `baris` / menit kalender bulan itu.
Keduanya menjawab pertanyaan murah yang tercatat di PROMPT v43 butir 4: apakah
bulan peralihan kontrak berlilin SEBAGIAN. Preseden BNXUSDT 2022-04: 41.550 dari
43.200. Ini pengukuran, bukan ramalan — tidak ada bilangan yang dipraregistrasi
untuknya, dan karena itu ia tidak boleh dihitung sebagai kemenangan.

## Medan penggugur (aturan 24)

`manifes_hilang`, `cacah_kunci_ganda`, `jumlah_selisih_cacah_daftar`,
`cacah_daftar_terpotong`, `jumlah_cacah_dibuang`, `jumlah_cacah_ditambal`,
`sidik_seragam` false, `kendali_sah` false, `selisih_ditulis_terdaftar` bukan
nol, `jumlah_karantina_tak_terkemas` bukan nol.

`selisih_penyebut`, `selisih_byte_tercatat`, dan `uji_r291` sengaja TIDAK
menggugurkan apa pun: ramalan yang kalah wajib dicatat MELESET, bukan
membatalkan laporannya sendiri (preseden `bulan_absen.py`, aturan 24 dan 72).

Kendali positif (aturan 50): BTCUSDT dan ETHUSDT wajib TIDAK muncul sekali pun
di daftar karantina; keduanya terukur 78 bulan lolos tanpa absen.

Aturan yang ditegakkan: 16, 20, 21, 22, 24, 36, 38, 44, 50, 52, 54, 69, 71, 72,
74, 76.
"""

from __future__ import annotations

import calendar
import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from . import pulihkan

VERSI = 1
KELUARAN = "reports/karantina_semesta.json"
KELUARAN_RINGKAS = "reports/karantina_semesta_ringkas.json"

# Bunyi R-291, disalin apa adanya dari jurnal 115 §7.
R291_HIMPUNAN: Tuple[Tuple[str, str], ...] = (
    ("AERGOUSDT", "2025-04"),
    ("AIAUSDT", "2026-01"),
    ("BNXUSDT", "2022-04"),
    ("BNXUSDT", "2022-06"),
    ("BNXUSDT", "2022-08"),
    ("CTKUSDT", "2025-04"),
    ("CVCUSDT", "2025-05"),
    ("CVXUSDT", "2025-07"),
    ("LITUSDT", "2025-12"),
    ("MAVIAUSDT", "2025-03"),
    ("PUMPUSDT", "2025-07"),
    ("SLPUSDT", "2025-07"),
)
R291_CACAH = 12

PENYEBUT_SEMESTA = 19598
PENYEBUT_LOLOS = 19586
BYTE_KARANTINA_TERCATAT = 13247705  # pecahan.py VERSI 6, KC-17
KENDALI_NAMA: Tuple[str, ...] = ("BTCUSDT", "ETHUSDT")
MENIT_PER_HARI = 1440


def sidik_kode() -> str:
    """Aturan 22: modul ini beserta modul yang nama berkasnya dipinjam."""
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(["karantina_semesta.py", "pulihkan.py"]):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def bulan_menit(bulan: str) -> int:
    """Menit kalender satu bulan; 0 bila bulannya tidak terbaca.

    Nol di sini berarti TAK TERUKUR, bukan bulan tanpa menit (aturan 74).
    """
    try:
        tahun, bln = (int(x) for x in str(bulan).split("-"))
        return int(calendar.monthrange(tahun, bln)[1]) * MENIT_PER_HARI
    except Exception:  # noqa: BLE001
        return 0


def kunci(entri: Dict[str, Any]) -> Tuple[str, str]:
    return (str(entri.get("simbol") or ""), str(entri.get("bulan") or ""))


def entri_karantina(manifes: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Daftar karantina satu manifes, dari blok `karantina` lalu kunci atas."""
    blok = manifes.get("karantina")
    if isinstance(blok, dict) and isinstance(blok.get("daftar_karantina"), list):
        return [e for e in blok["daftar_karantina"] if isinstance(e, dict)]
    atas = manifes.get("daftar_karantina")
    if isinstance(atas, list):
        return [e for e in atas if isinstance(e, dict)]
    return []


def _medan(manifes: Dict[str, Any], nama: str, baku: Any = 0) -> Any:
    blok = manifes.get("karantina")
    if isinstance(blok, dict) and nama in blok:
        return blok.get(nama)
    if nama in manifes:
        return manifes.get(nama)
    return baku


def perkaya(entri: Dict[str, Any], indeks: int) -> Dict[str, Any]:
    """Satu baris karantina beserta ukuran lilinnya."""
    bulan = str(entri.get("bulan") or "")
    baris = int(entri.get("baris") or 0)
    menit = bulan_menit(bulan)
    return {
        "indeks_pecahan": int(indeks),
        "simbol": str(entri.get("simbol") or ""),
        "bulan": bulan,
        "pelanggaran": sorted(str(p) for p in (entri.get("pelanggaran") or [])),
        "baris": baris,
        "menit_kalender": menit,
        "selisih_menit": (menit - baris) if menit else None,
        "nisbah_lilin": round(baris / menit, 6) if menit else None,
        "ada_parquet_karantina": bool(entri.get("parquet_karantina")),
        "parquet_karantina": entri.get("parquet_karantina"),
        "ada_checksum_zip": bool(entri.get("checksum_zip_sha256")),
    }


def baca_manifes(indeks: int, akar: str = ".") -> Optional[Dict[str, Any]]:
    """Manifes satu pecahan, atau None bila berkasnya tidak ada."""
    jalur = Path(akar) / pulihkan.nama_manifes(indeks)
    if not jalur.exists():
        return None
    isi = json.loads(jalur.read_text(encoding="utf-8"))
    return isi if isinstance(isi, dict) else None


def jalankan(akar: str = ".", total: int = pulihkan.TOTAL_PECAHAN) -> Dict[str, Any]:
    baris: List[Dict[str, Any]] = []
    hilang: List[int] = []
    per_pecahan: List[Dict[str, Any]] = []
    sidik: List[str] = []
    selisih_daftar = 0
    terpotong = 0
    dibuang = 0
    ditambal = 0
    ditulis = 0
    tak_terkemas = 0
    byte_kar = 0

    for i in range(int(total)):
        manifes = baca_manifes(i, akar=akar)
        if manifes is None:
            hilang.append(i)
            continue
        entri = entri_karantina(manifes)
        cacah_medan = int(_medan(manifes, "cacah_karantina", 0) or 0)
        selisih_daftar += abs(cacah_medan - len(entri))
        if bool(_medan(manifes, "daftar_terpotong", False)):
            terpotong += 1
        dibuang += int(_medan(manifes, "cacah_dibuang", 0) or 0)
        ditambal += int(_medan(manifes, "cacah_ditambal", 0) or 0)
        byte_kar += int(_medan(manifes, "byte_parquet_karantina", 0) or 0)
        ditulis += int(manifes.get("cacah_parquet_karantina_ditulis") or 0)
        tak_terkemas += int(manifes.get("cacah_karantina_tak_terkemas") or 0)
        kode = manifes.get("sidik_kode")
        if isinstance(kode, str) and kode:
            sidik.append(kode)
        for e in entri:
            baris.append(perkaya(e, i))
        per_pecahan.append(
            {
                "indeks": i,
                "cacah_karantina": cacah_medan,
                "cacah_daftar_terbaca": len(entri),
                "cacah_parquet_karantina_ditulis": int(
                    manifes.get("cacah_parquet_karantina_ditulis") or 0
                ),
                "versi_pecahan": manifes.get("versi_pecahan"),
                "karantina_dipersistenkan": manifes.get("karantina_dipersistenkan"),
            }
        )

    baris.sort(key=lambda r: (r["simbol"], r["bulan"]))
    kunci_semua = [(r["simbol"], r["bulan"]) for r in baris]
    kunci_unik = sorted(set(kunci_semua))

    sebaran: Dict[str, int] = {}
    for r in baris:
        for p in r["pelanggaran"]:
            sebaran[p] = sebaran.get(p, 0) + 1

    kendali = []
    for nama in KENDALI_NAMA:
        cacah = sum(1 for r in baris if r["simbol"] == nama)
        kendali.append({"simbol": nama, "cacah": cacah, "sah": cacah == 0})
    kendali_sah = bool(
        all(k["sah"] for k in kendali) and len(hilang) == 0 and len(per_pecahan) == int(total)
    )

    diramalkan = set(R291_HIMPUNAN)
    terukur = set(kunci_unik)
    hilang_r291 = sorted(diramalkan - terukur)
    tambahan_r291 = sorted(terukur - diramalkan)

    ringkasan: Dict[str, Any] = {
        "cacah_manifes_diminta": int(total),
        "cacah_manifes_dibaca": len(per_pecahan),
        "manifes_hilang": hilang,
        "cacah_karantina_semesta": len(baris),
        "cacah_kunci_unik": len(kunci_unik),
        "cacah_kunci_ganda": len(kunci_semua) - len(kunci_unik),
        "jumlah_selisih_cacah_daftar": selisih_daftar,
        "cacah_daftar_terpotong": terpotong,
        "jumlah_cacah_dibuang": dibuang,
        "jumlah_cacah_ditambal": ditambal,
        "jumlah_parquet_karantina_ditulis": ditulis,
        "selisih_ditulis_terdaftar": ditulis - len(baris),
        "jumlah_karantina_tak_terkemas": tak_terkemas,
        "byte_parquet_karantina_semesta": byte_kar,
        "selisih_byte_tercatat": byte_kar - BYTE_KARANTINA_TERCATAT,
        "penyebut_semesta": PENYEBUT_SEMESTA,
        "penyebut_lolos": PENYEBUT_LOLOS,
        "selisih_penyebut": (PENYEBUT_SEMESTA - PENYEBUT_LOLOS) - len(baris),
        "sidik_kode_manifes": sorted(set(sidik)),
        "sidik_seragam": bool(len(set(sidik)) == 1),
        "cacah_pecahan_berkarantina": sum(
            1 for p in per_pecahan if int(p["cacah_daftar_terbaca"]) > 0
        ),
        "pecahan_tanpa_karantina": [
            int(p["indeks"]) for p in per_pecahan if int(p["cacah_daftar_terbaca"]) == 0
        ],
        "cacah_tanpa_parquet_karantina": sum(
            1 for r in baris if not r["ada_parquet_karantina"]
        ),
        "sebaran_pelanggaran": dict(sorted(sebaran.items())),
        "kendali": kendali,
        "kendali_sah": kendali_sah,
        "uji_r291": {
            "diramalkan_cacah": R291_CACAH,
            "cacah_terukur": len(kunci_unik),
            "diramalkan_hilang": [list(k) for k in hilang_r291],
            "terukur_tak_diramalkan": [list(k) for k in tambahan_r291],
            "menang": bool(
                len(kunci_unik) == R291_CACAH and not hilang_r291 and not tambahan_r291
            ),
            "mudah": False,
            "catatan": (
                "R-291 BERISIKO: daftar karantina belum pernah dibaca ketika ia "
                "dipraregistrasi; ia bersandar pada aritmetika penyebut dan bulan "
                "ABSEN, bukan pada isi daftar ini"
            ),
        },
        "catatan_penggugur": (
            "yang menggugurkan hanyalah cacat bahan baku: manifes hilang, kunci "
            "ganda, selisih cacah daftar, daftar terpotong, cacah_dibuang atau "
            "cacah_ditambal bukan nol, sidik kode tak seragam, kendali tidak sah, "
            "selisih ditulis lawan terdaftar bukan nol, atau karantina tak "
            "terkemas. uji_r291, selisih_penyebut, dan selisih_byte_tercatat TIDAK "
            "menggugurkan apa pun (aturan 24, 72)"
        ),
        "catatan_lilin": (
            "nisbah_lilin = baris / menit kalender bulan itu; ia mengukur apakah "
            "bulan karantina berlilin SEBAGIAN, dan tidak ada bilangan yang "
            "dipraregistrasi untuknya"
        ),
        "catatan_rentang": (
            "daftar ini adalah simbol-bulan yang DIKARANTINA gerbang 1m, bukan "
            "bulan ABSEN dari rentang lolos; keduanya penyebut berbeda dan "
            "angkanya dilarang dipertukarkan (aturan 76, KC-39)"
        ),
    }

    laporan: Dict[str, Any] = {
        "bukan_bukti": False,
        "versi_karantina_semesta": VERSI,
        "ringkasan": ringkasan,
        "per_pecahan": per_pecahan,
        "baris": baris,
        "sidik_kode": sidik_kode(),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    basis = Path(akar)
    for nama_berkas, isi in (
        (KELUARAN, laporan),
        (
            KELUARAN_RINGKAS,
            {
                "bukan_bukti": False,
                "versi_karantina_semesta": VERSI,
                "ringkasan": ringkasan,
                "per_pecahan": per_pecahan,
                "baris": baris,
                "berkas_sumber": KELUARAN,
                "sidik_kode": laporan["sidik_kode"],
                "waktu_utc": laporan["waktu_utc"],
            },
        ),
    ):
        tujuan = basis / nama_berkas
        tujuan.parent.mkdir(parents=True, exist_ok=True)
        tujuan.write_text(
            json.dumps(isi, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    return laporan


def kode_keluar(ringkasan: Dict[str, Any]) -> int:
    """2 bila ada cacat bahan baku; ramalan yang kalah TIDAK menggugurkan."""
    gugur = (
        bool(ringkasan.get("manifes_hilang"))
        or int(ringkasan.get("cacah_kunci_ganda") or 0) != 0
        or int(ringkasan.get("jumlah_selisih_cacah_daftar") or 0) != 0
        or int(ringkasan.get("cacah_daftar_terpotong") or 0) != 0
        or int(ringkasan.get("jumlah_cacah_dibuang") or 0) != 0
        or int(ringkasan.get("jumlah_cacah_ditambal") or 0) != 0
        or not bool(ringkasan.get("sidik_seragam"))
        or not bool(ringkasan.get("kendali_sah"))
        or int(ringkasan.get("selisih_ditulis_terdaftar") or 0) != 0
        or int(ringkasan.get("jumlah_karantina_tak_terkemas") or 0) != 0
    )
    return 2 if gugur else 0


def main() -> int:
    hasil = jalankan()
    ringkasan = hasil["ringkasan"]
    print(
        json.dumps(
            {
                "ringkasan": ringkasan,
                "per_pecahan": hasil["per_pecahan"],
                "baris": hasil["baris"],
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    return kode_keluar(ringkasan)


if __name__ == "__main__":
    raise SystemExit(main())
