"""Silang semesta ARSIP lawan penyebut KEHIDUPAN - menegakkan aturan 62.

Jurnal 93 mencatat KC-24: saya menguji H-A013 dengan menyilangkan dua laporan
yang semestanya BERBEDA seolah satu. `reports/semesta_bulan_1m.json` memuat nama
berakhiran SETTLED (`CTKUSDTSETTLED` 1, `ICPUSDT_SETTLED` 9, `BNXUSDTSETTLED` 6,
dan lain-lain); penyebut kehidupan 19.586 simbol-bulan atas 787 simbol tidak
memuat satu pun. Akibatnya R-239 dan R-240 MELESET bukan karena hipotesisnya
salah, melainkan karena ujinya dijalankan di semesta yang salah.

Aturan 62 kini menuntut perbandingan semesta ditulis TERSURAT sebelum hipotesis
lintas-laporan diuji. Modul ini melakukan tepat itu, dan tidak lebih.

## Yang diukur

1. Cacah simbol pada semesta arsip lawan 787 simbol penyebut, beserta ketiga
   himpunan selisihnya: hanya-arsip, hanya-penyebut, irisan. Bila ada simbol
   hanya-penyebut, maka penyebut BUKAN himpunan bagian arsip, dan itu sendiri
   temuan yang harus dijelaskan.
2. Seluruh nama berakhiran SETTLED di semesta arsip, dan berapa di antaranya ada
   di penyebut.
3. H-A013 sejauh yang BOLEH diuji dari artefak yang sudah di-commit: keberadaan
   saudara SETTLED bagi keenam simbol peralihan, dan CACAH bulannya.

## Yang SENGAJA tidak diukur

`semesta_bulan_1m.json` memuat `bulan_per_simbol` sebagai CACAH, bukan DAFTAR
bulan (dibaca utuh, blob a1a6d3f0). Karena itu pertanyaan inti H-A013 - apakah
bulan tunggal saudara SETTLED SAMA dengan bulan peralihan yang hilang - TIDAK
dapat dijawab dari artefak yang ada. Medan `bulan_cocok_terukur` karena itu
selalu false dan `menang` selalu null: uji itu dinyatakan **TAK BERLAKU**, bukan
kalah (aturan 62). Menjawabnya menuntut daftar bulan per simbol yang belum
pernah diterbitkan; itu pekerjaan run lain, bukan run ini.

Definisi `saudara SETTLED` dipakai apa adanya dari `penyebut_tahun.nama_settled`
dan daftar `PERALIHAN` dari modul yang sama (aturan 36); tidak ada yang disalin
ulang.

## Penggugur (aturan 24)

`selisih_penyebut` terhadap 19.586, `cacah_penyebut_simbol` terhadap 787,
`sidik_seragam`, kelengkapan kedelapan laporan pecahan, ketiadaan kunci ganda,
kendali positif `silang_funding.kendali_silang` (aturan 50), dan `cacah_arsip`
yang bukan nol - sebab semesta arsip kosong berarti berkasnya salah dibaca, dan
seluruh perbandingan menjadi hampa (aturan 59: ketiadaan pengukuran bukan
ketiadaan gejala).

## Praregistrasi ramalan - ditulis SEBELUM run

R-242 dan R-243 sudah dipraregistrasi di jurnal 93 dan diadili oleh run ini.

- **R-244** - CI pada commit yang memuat berkas ini mengumpulkan **526 butir**
  dengan kode keluar **0**. Dasar (aturan 54, 56, 57): 494 butir terverifikasi
  pada run 30446932599 (commit d95c35a5) ditambah **32** fungsi `def test_`
  bernomor di berkas uji baru, tanpa `parametrize`, tanpa menyentuh berkas uji
  lain. 494 + 32 = 526. Aturan 57 kini empat dari empat.
- **R-245** - `cacah_saudara_arsip` bagi keenam simbol peralihan = **6 dari 6**,
  dan `cacah_saudara_satu_bulan` = **6**. Ramalan MUDAH: ia menyalin angka dari
  blob a1a6d3f0 yang sudah dibaca utuh, jadi ia menguji jalur pembacaan modul
  ini, bukan pemahaman saya tentang pasar. GUGUR bila salah satu bukan 6.
- **R-246** - `ICPUSDT_SETTLED` dan `TLMUSDT_SETTLED` masing-masing bercacah
  bulan **9** di semesta arsip. GUGUR bila salah satu bukan 9.
- **R-247** - `penyebut_bagian_arsip` **true**: seluruh 787 simbol penyebut ada di
  semesta arsip, sehingga `cacah_hanya_penyebut` = 0. Ini ramalan yang benar-benar
  TIDAK saya ketahui: bila ada simbol yang lolos gerbang kehidupan tetapi tidak
  terdaftar di semesta bulan 1m, maka salah satu dari kedua laporan itu cacat, dan
  temuan itu lebih penting daripada seluruh sisa run ini. GUGUR bila
  `cacah_hanya_penyebut` lebih dari nol.

Cacah baris berkas ini SENGAJA tidak diramalkan (aturan 58, pilihan c).

Aturan yang mengikat: 10, 20, 21, 22, 24, 30, 36, 37, 41, 45, 46, 50, 52, 53, 54,
56, 57, 58, 59, 62.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from . import kebangkitan, kehidupan_arsip, penyebut_tahun, silang_funding

VERSI = 1
TOTAL_PECAHAN = kehidupan_arsip.TOTAL_PECAHAN
SUMBER_FUNDING = silang_funding.SUMBER_FUNDING
SUMBER_ARSIP = "reports/semesta_bulan_1m.json"
KELUARAN = "reports/semesta_silang.json"
KELUARAN_RINGKAS = "reports/semesta_silang_ringkas.json"

PENYEBUT_TERCATAT = kebangkitan.PENYEBUT_TERCATAT
SIMBOL_TERCATAT = 787
TERATAS = 20

MEDAN_ARSIP = "bulan_per_simbol"
AKHIRAN_SETTLED = penyebut_tahun.AKHIRAN_SETTLED
PERALIHAN = penyebut_tahun.PERALIHAN
BERSAMBUNG = penyebut_tahun.BERSAMBUNG

SEBAB_TAK_BERLAKU = (
    "laporan arsip memuat CACAH bulan, bukan DAFTAR bulan, jadi kecocokan bulan "
    "peralihan tidak dapat diuji dari artefak yang ada (aturan 62)"
)

BERKAS_DICAP = [
    "kebangkitan.py",
    "kehidupan.py",
    "kehidupan_arsip.py",
    "penyebut_tahun.py",
    "semesta_silang.py",
    "silang_funding.py",
]

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


def cacah_bulan_arsip(dok: Dict[str, Any]) -> Dict[str, int]:
    """Peta simbol ke CACAH bulan; medan yang tidak ada berbunyi kosong."""
    peta = dok.get(MEDAN_ARSIP) or {}
    return {str(k): int(v) for k, v in peta.items()}


def simbol_arsip(dok: Dict[str, Any]) -> List[str]:
    return sorted(cacah_bulan_arsip(dok))


def simbol_penyebut(status: Dict[Kunci, str]) -> List[str]:
    """Simbol yang punya sekurang-kurangnya satu bulan LOLOS gerbang."""
    return sorted({str(simbol) for (simbol, _bulan) in status})


def berakhiran_settled(nama: str) -> bool:
    return any(str(nama).endswith(a) for a in AKHIRAN_SETTLED)


def daftar_settled(nama: Iterable[str]) -> List[str]:
    return sorted({str(n) for n in nama if berakhiran_settled(n)})


def silang_semesta(arsip: Iterable[str], penyebut: Iterable[str]) -> Dict[str, Any]:
    """Ketiga himpunan selisih, tersurat - inilah inti aturan 62."""
    a = {str(x) for x in arsip}
    p = {str(x) for x in penyebut}
    hanya_a = sorted(a - p)
    hanya_p = sorted(p - a)
    return {
        "cacah_arsip": len(a),
        "cacah_penyebut": len(p),
        "cacah_irisan": len(a & p),
        "cacah_hanya_arsip": len(hanya_a),
        "cacah_hanya_penyebut": len(hanya_p),
        "contoh_hanya_arsip": hanya_a[:TERATAS],
        "contoh_hanya_penyebut": hanya_p[:TERATAS],
        "arsip_lebih_banyak": len(a) > len(p),
        "penyebut_bagian_arsip": len(hanya_p) == 0,
        "semesta_sama": a == p,
    }


def settled_di_penyebut(
    arsip: Iterable[str], penyebut: Iterable[str]
) -> Dict[str, Any]:
    """Berapa nama SETTLED arsip yang benar-benar lolos ke penyebut."""
    daftar = daftar_settled(arsip)
    p = {str(x) for x in penyebut}
    ada = [n for n in daftar if n in p]
    return {
        "cacah_settled_arsip": len(daftar),
        "daftar_settled_arsip": daftar,
        "cacah_settled_di_penyebut": len(ada),
        "daftar_settled_di_penyebut": ada,
        "terukur": len(daftar) > 0,
    }


def saudara_arsip(
    cacah: Dict[str, int], simbol: str
) -> List[Dict[str, Any]]:
    """Saudara SETTLED satu simbol beserta CACAH bulannya di semesta arsip."""
    return [
        {"nama": n, "cacah_bulan": int(cacah[n])}
        for n in penyebut_tahun.nama_settled(simbol)
        if n in cacah
    ]


def uji_h_a013_arsip(
    cacah: Dict[str, int],
    peralihan: Sequence[Tuple[str, str]] = PERALIHAN,
) -> Dict[str, Any]:
    """H-A013 di semesta yang BENAR, sejauh artefak mengizinkan.

    `menang` selalu null: kecocokan bulan tidak dapat diuji dari cacah bulan.
    Yang diukur hanyalah keberadaan saudara dan cacah bulannya.
    """
    baris: List[Dict[str, Any]] = []
    ada = satu = 0
    for simbol, bulan in peralihan:
        saudara = saudara_arsip(cacah, simbol)
        total = sum(int(s["cacah_bulan"]) for s in saudara)
        if saudara:
            ada += 1
        if total == 1:
            satu += 1
        baris.append(
            {
                "simbol": str(simbol),
                "bulan_peralihan": str(bulan),
                "simbol_di_arsip": str(simbol) in cacah,
                "cacah_bulan_simbol": int(cacah.get(str(simbol), 0)),
                "saudara": saudara,
                "cacah_bulan_saudara": total,
                "saudara_satu_bulan": total == 1,
                "bulan_cocok_terukur": False,
            }
        )
    return {
        "baris": baris,
        "cacah_peralihan": len(baris),
        "cacah_saudara_arsip": ada,
        "cacah_saudara_satu_bulan": satu,
        "bulan_cocok_terukur": False,
        "berlaku": False,
        "menang": None,
        "sebab_tak_berlaku": SEBAB_TAK_BERLAKU,
    }


def rinci_bersambung_arsip(
    cacah: Dict[str, int], simbol: Sequence[str] = BERSAMBUNG
) -> List[Dict[str, Any]]:
    """Kedua peristiwa bersambung, diperiksa dengan alat yang SAMA."""
    keluar: List[Dict[str, Any]] = []
    for s in simbol:
        saudara = saudara_arsip(cacah, s)
        keluar.append(
            {
                "simbol": str(s),
                "cacah_bulan_simbol": int(cacah.get(str(s), 0)),
                "saudara": saudara,
                "cacah_bulan_saudara": sum(
                    int(x["cacah_bulan"]) for x in saudara
                ),
            }
        )
    return keluar


def kode_keluar(ringkasan: Dict[str, Any]) -> int:
    """Kode 2 bila perbandingan ini tidak berhak diklaim sebagai pengukuran."""
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
    if int(ringkasan.get("selisih_penyebut") or 0) != 0:
        return 2
    if int(ringkasan.get("cacah_penyebut_simbol") or 0) != SIMBOL_TERCATAT:
        return 2
    if int(ringkasan.get("cacah_arsip") or 0) <= 0:
        return 2
    return 0


def jalankan(akar: str = ".", total: int = TOTAL_PECAHAN) -> Dict[str, Any]:
    status, byte_parquet, meta = silang_funding.baca_laporan_kehidupan(
        akar=akar, total=total
    )
    mentah_funding = (Path(akar) / SUMBER_FUNDING).read_bytes()
    funding = json.loads(mentah_funding.decode("utf-8"))
    lubang, meta_lubang = silang_funding.lubang_funding(funding)
    kendali = silang_funding.kendali_silang(byte_parquet, status, lubang)

    mentah_arsip = (Path(akar) / SUMBER_ARSIP).read_bytes()
    dok = json.loads(mentah_arsip.decode("utf-8"))
    cacah = cacah_bulan_arsip(dok)

    arsip = sorted(cacah)
    penyebut = simbol_penyebut(status)
    silang = silang_semesta(arsip, penyebut)
    settled = settled_di_penyebut(arsip, penyebut)
    h_a013 = uji_h_a013_arsip(cacah)
    bersambung = rinci_bersambung_arsip(cacah)

    ringkasan: Dict[str, Any] = {
        "penyebut_kehidupan": len(status),
        "selisih_penyebut": len(status) - PENYEBUT_TERCATAT,
        "cacah_penyebut_simbol": len(penyebut),
        "cacah_arsip": silang["cacah_arsip"],
        "jumlah_bulan_arsip": sum(int(v) for v in cacah.values()),
        "cacah_irisan": silang["cacah_irisan"],
        "cacah_hanya_arsip": silang["cacah_hanya_arsip"],
        "cacah_hanya_penyebut": silang["cacah_hanya_penyebut"],
        "arsip_lebih_banyak": silang["arsip_lebih_banyak"],
        "penyebut_bagian_arsip": silang["penyebut_bagian_arsip"],
        "semesta_sama": silang["semesta_sama"],
        "cacah_settled_arsip": settled["cacah_settled_arsip"],
        "cacah_settled_di_penyebut": settled["cacah_settled_di_penyebut"],
        "cacah_saudara_arsip": h_a013["cacah_saudara_arsip"],
        "cacah_saudara_satu_bulan": h_a013["cacah_saudara_satu_bulan"],
        "h_a013_berlaku": h_a013["berlaku"],
        "kendali": kendali,
        "kendali_sah": silang_funding.kendali_sah(kendali),
    }
    ringkasan.update(meta)
    ringkasan.update(meta_lubang)

    definisi = {
        "semesta_arsip": (
            "simbol yang terdaftar pada medan bulan_per_simbol di "
            "reports/semesta_bulan_1m.json; nilainya CACAH bulan, bukan daftar"
        ),
        "semesta_penyebut": (
            "simbol yang punya sekurang-kurangnya satu bulan LOLOS gerbang "
            "kehidupan; inilah semesta 19.586 simbol-bulan"
        ),
        "saudara_settled": (
            "nama simbol yang sama ditambah akhiran SETTLED atau _SETTLED, "
            "dipakai apa adanya dari penyebut_tahun.nama_settled"
        ),
        "h_a013_berlaku": (
            "selalu false pada run ini; kecocokan bulan peralihan TIDAK dapat "
            "diuji dari cacah bulan, jadi hipotesisnya TAK BERLAKU, bukan kalah"
        ),
    }

    return {
        "bukan_bukti": False,
        "versi_semesta_silang": VERSI,
        "sidik_kode": sidik_kode(),
        "sidik_kode_penyebut_tahun": penyebut_tahun.sidik_kode(),
        "sidik_kode_silang_funding": silang_funding.sidik_kode(),
        "sidik_data_arsip": hashlib.sha256(mentah_arsip).hexdigest(),
        "sidik_data_funding": hashlib.sha256(mentah_funding).hexdigest(),
        "sumber": [SUMBER_ARSIP, SUMBER_FUNDING]
        + [kehidupan_arsip.nama_keluaran(i) for i in range(total)],
        "definisi": definisi,
        "silang": silang,
        "settled": settled,
        "h_a013_arsip": h_a013,
        "bersambung": bersambung,
        "ringkasan": ringkasan,
        "catatan_batas": (
            "semesta arsip adalah bulan 1m yang DITERBITKAN, bukan yang LOLOS "
            "gerbang; simbol hanya-arsip karena itu bukan bukti pasar mati, dan "
            "nama SETTLED yang absen dari penyebut bukan bukti ia tak "
            "diperdagangkan (aturan 30, 59)"
        ),
        "catatan_tafsir": (
            "KC-24 lahir dari menyilangkan kedua semesta ini seolah satu; run "
            "ini hanya MENGUKUR jaraknya dan tidak menghidupkan kembali satu pun "
            "klaim yang gugur bersama R-239 dan R-240"
        ),
        "catatan_penggugur": (
            "sidik_seragam false, laporan pecahan kurang, kunci ganda, "
            "kendali_sah false, selisih_penyebut bukan nol, "
            "cacah_penyebut_simbol bukan 787, atau cacah_arsip nol membatalkan "
            "seluruh angka (aturan 24)"
        ),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def ringkas(laporan: Dict[str, Any]) -> Dict[str, Any]:
    """Berkas kecil pendamping (aturan 52): tanpa daftar simbol penuh."""
    settled = laporan.get("settled") or {}
    return {
        "bukan_bukti": False,
        "versi_semesta_silang": laporan.get("versi_semesta_silang"),
        "sidik_kode": laporan.get("sidik_kode"),
        "sidik_data_arsip": laporan.get("sidik_data_arsip"),
        "ringkasan": laporan.get("ringkasan"),
        "silang": laporan.get("silang"),
        "settled": {
            k: v for k, v in settled.items() if k != "daftar_settled_arsip"
        },
        "h_a013_arsip": laporan.get("h_a013_arsip"),
        "bersambung": laporan.get("bersambung"),
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
