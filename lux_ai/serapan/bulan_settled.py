"""DAFTAR bulan arsip bagi nama SETTLED - uji H-A013 yang sebenarnya.

Jurnal 94 menutup `semesta_silang` dengan satu simpulan tajam: keenam simbol
peralihan punya saudara berakhiran SETTLED yang bercacah TEPAT satu bulan, tetapi
laporan arsip hanya memuat CACAH bulan, bukan DAFTAR bulan, sehingga pertanyaan
inti H-A013 - apakah bulan tunggal itu SAMA dengan bulan peralihan yang hilang -
dinyatakan TAK BERLAKU, bukan kalah (aturan 62).

Jurnal 94 juga menyebut `bulan_arsip` dari kedelapan manifes pecahan sebagai
jalan keluar. Itu KELIRU, dan koreksinya ditulis di sini sebelum satu baris pun
dijalankan: manifes pecahan hanya memuat parquet yang benar-benar DIUNDUH, yakni
787 simbol berkuota USDT, dan nama SETTLED tidak pernah ada di dalamnya. Membaca
manifes karena itu akan mengulang KC-24 dalam bentuk baru. Yang dibutuhkan adalah
pendaftaran arsip itu sendiri, dan `arsip.bulan_tersedia` sudah menyediakannya.

R-248 karena itu diadili oleh run INI, bukan oleh modul manifes. Isi ramalannya
tidak diubah sedikit pun; hanya alat pengukurnya yang dikoreksi.

## Yang diukur

1. DAFTAR bulan 1m untuk kelima belas nama berakhiran SETTLED yang tercatat di
   `reports/semesta_silang.json`, dan untuk kesembilan nama dasarnya (keenam
   simbol peralihan ditambah ICPUSDT, TLMUSDT, BNXUSDT).
2. H-A013: apakah bulan peralihan yang HILANG dari penyebut ada di dalam daftar
   bulan saudara SETTLED-nya. Inilah uji yang selama dua run tertunda.
3. Silang cacah terhadap `reports/semesta_bulan_1m.json` (aturan 62): cacah bulan
   yang didaftar hari ini WAJIB sama dengan cacah yang tercatat di laporan itu.
   Bila berbeda, arsip berubah sejak 28 Juli dan seluruh perbandingan lama harus
   dibaca ulang - itu temuan, bukan gangguan.

## Kendali positif (aturan 50)

BTCUSDT didaftar dengan alat yang sama. Bila pendaftaran arsip rusak atau diblokir,
ia akan berbunyi kosong; BTCUSDT yang bercacah kurang dari `AMBANG_KENDALI` bulan
membuat `kendali_sah` false dan kode keluar 2, sehingga ketiadaan bulan SETTLED
tidak boleh disalahbaca sebagai bukti apa pun (aturan 59).

## Batas yang tetap berlaku

Daftar bulan ini adalah bulan yang DITERBITKAN arsip, bukan yang lolos gerbang
kehidupan. Kecocokan bulan peralihan dengan bulan saudara SETTLED membuktikan
PENAMAAN, bukan perdagangan: KC-18 sudah menunjukkan arsip menerbitkan klines 1m
sempurna secara bentuk bagi pasar yang tidak diperdagangkan. Karena itu H-A013
yang MENANG melemahkan tafsir kebangkitan tanpa membuktikan pasarnya hidup
(aturan 10, 20, 63).

## Praregistrasi ramalan - ditulis SEBELUM run

- **R-248 (H-A013, uji sebenarnya; dipraregistrasi di jurnal 94, alat dikoreksi
  di sini)** - dari keenam bulan peralihan, yang SAMA dengan salah satu bulan
  saudara SETTLED-nya berjumlah **4..6**. GUGUR bila 3 atau kurang. Bila menang,
  tafsir "delapan kebangkitan" wajib dilemahkan menjadi "dua bersambung dan enam
  peralihan nama".
- **R-250** - CI pada commit yang memuat berkas ini mengumpulkan **552 butir**
  dengan kode keluar 0. Dasar (aturan 54, 56, 57): 526 terverifikasi pada run
  30447917282 (commit 474fa23c) ditambah **26** fungsi `def test_` bernomor,
  tanpa `parametrize`. 526 + 26 = 552. Aturan 57 kini lima dari lima.
- **R-251** - `cacah_cocok_cacah` = **24 dari 24** nama yang didaftar: cacah bulan
  hari ini sama dengan cacah di `semesta_bulan_1m.json` (28 Juli). GUGUR bila satu
  saja berbeda; bila gugur, sebabnya wajib diperiksa sebelum angka lain dipakai.
- **R-252** - kendali BTCUSDT mendaftar **sekurang-kurangnya 60** bulan 1m. GUGUR
  bila kurang, dan bila gugur seluruh laporan ini batal.

Cacah baris berkas ini SENGAJA tidak diramalkan (aturan 58, pilihan c).

Aturan yang mengikat: 10, 16, 20, 21, 22, 24, 30, 36, 41, 45, 46, 50, 52, 54, 56,
57, 58, 59, 62, 63.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Tuple

from . import arsip, penyebut_tahun, semesta_silang

VERSI = 1
SUMBER_SILANG = "reports/semesta_silang.json"
SUMBER_ARSIP = semesta_silang.SUMBER_ARSIP
KELUARAN = "reports/bulan_settled.json"
KELUARAN_RINGKAS = "reports/bulan_settled_ringkas.json"

INTERVAL = "1m"
PERALIHAN = penyebut_tahun.PERALIHAN
DASAR_LAIN: Tuple[str, ...] = ("ICPUSDT", "TLMUSDT", "BNXUSDT")
SIMBOL_KENDALI = "BTCUSDT"
AMBANG_KENDALI = 60
AMBANG_MENANG = penyebut_tahun.AMBANG_MENANG
SETTLED_TERCATAT = 15

SEBAB_COCOK = penyebut_tahun.SEBAB_SAUDARA_COCOK
SEBAB_LAIN = penyebut_tahun.SEBAB_SAUDARA_LAIN
SEBAB_TANPA = penyebut_tahun.SEBAB_TANPA_SAUDARA

BERKAS_DICAP = [
    "arsip.py",
    "bulan_settled.py",
    "penyebut_tahun.py",
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


def daftar_settled_tercatat(dok: Dict[str, Any]) -> List[str]:
    """Kelima belas nama SETTLED dari laporan semesta_silang yang sudah di-commit."""
    settled = dok.get("settled") or {}
    return sorted(str(n) for n in (settled.get("daftar_settled_arsip") or []))


def nama_didaftar(settled: Iterable[str]) -> List[str]:
    """Nama SETTLED ditambah kesembilan nama dasar, tanpa penggandaan."""
    kumpulan = {str(n) for n in settled}
    for simbol, _bulan in PERALIHAN:
        kumpulan.add(str(simbol))
    for simbol in DASAR_LAIN:
        kumpulan.add(str(simbol))
    return sorted(kumpulan)


def kumpulkan_bulan(
    nama: Iterable[str],
    pengambil: Optional[Callable[[str], List[str]]] = None,
) -> Dict[str, Dict[str, Any]]:
    """Daftar bulan tiap nama; galat dicatat, TIDAK diam-diam jadi daftar kosong.

    Aturan 16 dan 41: nama yang gagal didaftar berbunyi `terukur` false dengan
    `galat` tertulis, sebab daftar kosong karena galat bukan daftar kosong karena
    arsip tidak memuatnya.
    """
    ambil = pengambil or (lambda n: arsip.bulan_tersedia(n, interval=INTERVAL))
    hasil: Dict[str, Dict[str, Any]] = {}
    for n in sorted({str(x) for x in nama}):
        try:
            bulan = sorted({str(b) for b in ambil(n)})
            hasil[n] = {
                "bulan": bulan,
                "cacah_bulan": len(bulan),
                "terukur": True,
                "galat": None,
            }
        except Exception as exc:  # noqa: BLE001
            hasil[n] = {
                "bulan": [],
                "cacah_bulan": 0,
                "terukur": False,
                "galat": str(exc)[:300],
            }
    return hasil


def bulan_saudara(peta: Dict[str, Dict[str, Any]], simbol: str) -> Dict[str, Any]:
    """Saudara SETTLED satu simbol beserta DAFTAR bulannya."""
    ditemukan = [
        n for n in penyebut_tahun.nama_settled(simbol) if n in peta and peta[n]["terukur"]
    ]
    bulan = sorted({b for n in ditemukan for b in peta[n]["bulan"]})
    return {
        "saudara_diperiksa": penyebut_tahun.nama_settled(simbol),
        "saudara_ditemukan": ditemukan,
        "bulan_saudara": bulan,
        "cacah_bulan_saudara": len(bulan),
    }


def uji_h_a013_bulan(
    peta: Dict[str, Dict[str, Any]],
    peralihan: Sequence[Tuple[str, str]] = PERALIHAN,
) -> Dict[str, Any]:
    """H-A013 sebagaimana mestinya: bulan peralihan ADA di daftar bulan saudara."""
    baris: List[Dict[str, Any]] = []
    cocok = 0
    terukur = 0
    for simbol, bulan in peralihan:
        info = bulan_saudara(peta, simbol)
        ada = str(bulan) in info["bulan_saudara"]
        if info["saudara_ditemukan"]:
            terukur += 1
            sebab = SEBAB_COCOK if ada else SEBAB_LAIN
        else:
            sebab = SEBAB_TANPA
        if ada:
            cocok += 1
        baris.append(
            {
                "simbol": str(simbol),
                "bulan_peralihan": str(bulan),
                "cocok_bulan": ada,
                "sebab": sebab,
                "bulan_simbol_dasar": (peta.get(str(simbol)) or {}).get("bulan") or [],
                **info,
            }
        )
    return {
        "baris": baris,
        "cacah_peralihan": len(baris),
        "cacah_terukur": terukur,
        "cacah_cocok_bulan": cocok,
        "ambang_menang": AMBANG_MENANG,
        "sebab_terpakai": sorted({str(b["sebab"]) for b in baris}),
        "definisi_dapat_dibedakan": len({str(b["sebab"]) for b in baris}) > 1,
        "terukur": terukur > 0,
        "menang": terukur > 0 and cocok >= AMBANG_MENANG,
    }


def silang_cacah(
    peta: Dict[str, Dict[str, Any]], tercatat: Dict[str, int]
) -> Dict[str, Any]:
    """Aturan 62: cacah hari ini WAJIB sama dengan cacah 28 Juli, per nama."""
    baris: List[Dict[str, Any]] = []
    for nama in sorted(peta):
        kini = int(peta[nama]["cacah_bulan"])
        lalu = tercatat.get(nama)
        baris.append(
            {
                "nama": nama,
                "cacah_kini": kini,
                "cacah_tercatat": (int(lalu) if lalu is not None else None),
                "ada_di_laporan_lama": lalu is not None,
                "cocok": (lalu is not None and int(lalu) == kini),
            }
        )
    return {
        "baris": baris,
        "cacah_nama": len(baris),
        "cacah_cocok_cacah": sum(1 for b in baris if b["cocok"]),
        "cacah_tak_ada_di_laporan_lama": sum(
            1 for b in baris if not b["ada_di_laporan_lama"]
        ),
        "seluruhnya_cocok": all(b["cocok"] for b in baris) if baris else False,
    }


def kendali(
    peta: Dict[str, Dict[str, Any]],
    simbol: str = SIMBOL_KENDALI,
    ambang: int = AMBANG_KENDALI,
) -> Dict[str, Any]:
    """Kendali positif: pendaftaran arsip terbukti bekerja (aturan 50)."""
    info = peta.get(str(simbol)) or {}
    cacah = int(info.get("cacah_bulan") or 0)
    return {
        "simbol": str(simbol),
        "cacah_bulan": cacah,
        "ambang": int(ambang),
        "terukur": bool(info.get("terukur")),
        "sah": bool(info.get("terukur")) and cacah >= int(ambang),
    }


def kode_keluar(ringkasan: Dict[str, Any]) -> int:
    """Kode 2 bila laporan ini tidak berhak diklaim sebagai pengukuran."""
    if not ringkasan.get("kendali_sah"):
        return 2
    if int(ringkasan.get("cacah_gagal_daftar") or 0) > 0:
        return 2
    if int(ringkasan.get("cacah_settled_tercatat") or 0) != SETTLED_TERCATAT:
        return 2
    return 0


def jalankan(akar: str = ".") -> Dict[str, Any]:
    basis = Path(akar)
    mentah_silang = (basis / SUMBER_SILANG).read_bytes()
    dok_silang = json.loads(mentah_silang.decode("utf-8"))
    mentah_arsip = (basis / SUMBER_ARSIP).read_bytes()
    dok_arsip = json.loads(mentah_arsip.decode("utf-8"))
    tercatat = semesta_silang.cacah_bulan_arsip(dok_arsip)

    settled = daftar_settled_tercatat(dok_silang)
    nama = nama_didaftar(settled)
    peta = kumpulkan_bulan(nama + [SIMBOL_KENDALI])

    h_a013 = uji_h_a013_bulan(peta)
    silang = silang_cacah({k: v for k, v in peta.items() if k in set(nama)}, tercatat)
    kend = kendali(peta)

    ringkasan: Dict[str, Any] = {
        "cacah_settled_tercatat": len(settled),
        "cacah_nama_didaftar": len(nama),
        "cacah_gagal_daftar": sum(1 for v in peta.values() if not v["terukur"]),
        "jumlah_bulan_didaftar": sum(
            int(v["cacah_bulan"]) for k, v in peta.items() if k in set(nama)
        ),
        "cacah_cocok_bulan": h_a013["cacah_cocok_bulan"],
        "h_a013_menang": h_a013["menang"],
        "h_a013_terukur": h_a013["terukur"],
        "h_a013_dapat_dibedakan": h_a013["definisi_dapat_dibedakan"],
        "cacah_nama_silang": silang["cacah_nama"],
        "cacah_cocok_cacah": silang["cacah_cocok_cacah"],
        "seluruhnya_cocok": silang["seluruhnya_cocok"],
        "kendali": kend,
        "kendali_sah": kend["sah"],
    }

    return {
        "bukan_bukti": False,
        "versi_bulan_settled": VERSI,
        "sidik_kode": sidik_kode(),
        "sidik_data_silang": hashlib.sha256(mentah_silang).hexdigest(),
        "sidik_data_arsip": hashlib.sha256(mentah_arsip).hexdigest(),
        "sumber": [SUMBER_SILANG, SUMBER_ARSIP],
        "interval": INTERVAL,
        "definisi": {
            "bulan_didaftar": (
                "bulan yang arsip TERBITKAN untuk nama itu pada interval 1m, dari "
                "arsip.bulan_tersedia; bukan bulan yang lolos gerbang kehidupan"
            ),
            "cocok_bulan": (
                "bulan peralihan yang hilang dari penyebut ADA di dalam daftar "
                "bulan saudara SETTLED-nya"
            ),
            "menang": (
                "sekurang-kurangnya empat dari enam bulan peralihan cocok; "
                "kemenangan MELEMAHKAN tafsir kebangkitan, bukan menguatkannya"
            ),
        },
        "h_a013": h_a013,
        "silang_cacah": silang,
        "bulan": peta,
        "ringkasan": ringkasan,
        "catatan_batas": (
            "KC-18: arsip menerbitkan klines 1m sempurna secara bentuk bagi pasar "
            "yang tidak diperdagangkan, jadi kecocokan bulan membuktikan PENAMAAN "
            "kontrak, bukan perdagangan; seluruh angka tetap terbatas pada "
            "pasangan berkuota USDT (aturan 63)"
        ),
        "catatan_penggugur": (
            "kendali BTCUSDT di bawah ambang, ada nama yang gagal didaftar, atau "
            "cacah nama SETTLED bukan 15 membatalkan seluruh angka (aturan 24, 50)"
        ),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def ringkas(laporan: Dict[str, Any]) -> Dict[str, Any]:
    """Berkas kecil pendamping (aturan 52): tanpa daftar bulan penuh."""
    return {
        "bukan_bukti": False,
        "versi_bulan_settled": laporan.get("versi_bulan_settled"),
        "sidik_kode": laporan.get("sidik_kode"),
        "sidik_data_silang": laporan.get("sidik_data_silang"),
        "ringkasan": laporan.get("ringkasan"),
        "h_a013": laporan.get("h_a013"),
        "silang_cacah": laporan.get("silang_cacah"),
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
