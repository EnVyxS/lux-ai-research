"""Peta manifes pecahan: sensus simbol-bulan dibaca langsung dari kedelapan manifes.

Modul ini dibuat untuk membongkar EMPAT blokir klasifikasi sekaligus, yang
keempatnya bermuara pada satu sebab tunggal: `reports/manifes_pecahan_*.json`
berjumlah 20.533.802 byte dan **alat baca agen menolak** berkas sebesar itu
(aturan 78 § 3.2 (a); yang terkecil, pecahan 3, sudah 2.257.314 B). Preseden
jalan keluarnya sudah ada dan sudah sah: `karantina_semesta.py` menempuhnya
lebih dulu — kode di-commit, Actions menjalankannya, laporan kecil dibaca pada
ref runner (aturan 38, aturan 52).

Blokir yang disasar:

- **Blokir 2** — 786 simbol selain BNXUSDT belum pernah diperiksa keanggotaan
  penyebutnya.
- **Blokir 3** — cacah `baris_mati` hanya pernah terbaca 54% (aturan 78 § 3.2
  (b)); di sini setiap medan ANGKA dijumlahkan di runner, jadi tak ada yang
  terpotong.
- **Blokir 4** — kelas positif 33 hanya datang dari lima simbol (KC-47).
- **Blokir 5** — 787 lawan 787 baru didamaikan untuk BNXUSDT (0,127%).

## ATURAN 71 DITEGAKKAN DENGAN CARA YANG TIDAK BIASA

Penulis modul ini **belum pernah membaca isi manifes** — justru itu perkaranya.
Menuliskan nama medan dari ingatan atau dugaan adalah persis yang aturan 71
larang. Karena itu modul ini **TIDAK menyebut satu pun nama medan manifes**.
Ia **menemukan** nama medan dari **bentuk nilainya**:

- medan simbol = medan yang nilainya cocok `^[A-Z0-9]{2,20}USDT$` pada mayoritas
  entri;
- medan bulan = medan yang nilainya cocok `^\\d{4}-(0[1-9]|1[0-2])$`.

Nama yang ditemukan **dilaporkan apa adanya** di medan `medan_simbol` dan
`medan_bulan`, sehingga giliran berikutnya boleh mengutipnya sebagai nama
terbaca, bukan nama tertebak. Satu-satunya nama yang dipinjam dari kode yang
SUDAH dibaca utuh adalah `pulihkan.nama_manifes` dan `pulihkan.TOTAL_PECAHAN`,
keduanya dikutip lewat `karantina_semesta.py` (blob 46e7c46b…).

## Yang dilaporkan, dan mengapa kecil

Laporan sengaja dijaga jauh di bawah 110.662 B — titik pemotongan terukur
terendah (aturan 78 § 3.2 (c)). Karena itu **tidak ada satu pun baris entri
mentah yang disalin**. Yang keluar hanya: skema tiap manifes, jumlah tiap medan
angka, sebaran tiap medan berkardinalitas rendah, dan cacah bulan per simbol
(787 baris pendek). Contoh nilai dibatasi `BATAS_CONTOH`.

## Medan penggugur (aturan 24)

`manifes_hilang`, `sidik_seragam` false, `cacah_simbol_bulan_ganda` bukan nol,
`cacah_simbol_lintas_pecahan` bukan nol (round-robin `i%8` melarang satu simbol
muncul di dua pecahan), dan `daftar_utama_hilang`.

Selisih terhadap 19.598 / 19.586 / 787 **TIDAK menggugurkan apa pun**: ramalan
yang kalah wajib dicatat MELESET, bukan membatalkan laporannya sendiri (aturan
24, 72; preseden `karantina_semesta.py`).

Kendali positif (aturan 50): BTCUSDT dan ETHUSDT wajib HADIR dengan cacah bulan
lebih dari nol — kebalikan kendali `karantina_semesta.py`, sebab di sini
penyebutnya seluruh semesta, bukan daftar karantina.

**Laporan ini BUKAN adjudikasi.** Ia tidak memuat satu pun blok `uji_*`; vonis
alat bukan adjudikasi (KC-49), dan ramalan atasnya diregistrasi di jurnal
SEBELUM laporan ini dibaca (aturan 21).

Aturan yang ditegakkan: 21, 22, 24, 36, 38, 50, 52, 71, 72, 74, 76, 78, 93.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from . import pulihkan

VERSI = 1
KELUARAN = "reports/peta_manifes.json"

POLA_SIMBOL = re.compile(r"^[A-Z0-9]{2,20}USDT$")
POLA_BULAN = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")

PENYEBUT_SEMESTA = 19598
PENYEBUT_LOLOS = 19586
CACAH_SIMBOL_TERCATAT = 787
KENDALI_NAMA: Tuple[str, ...] = ("BTCUSDT", "ETHUSDT")

BATAS_CONTOH = 8
BATAS_KARDINALITAS = 24
BATAS_JALUR = 40


def sidik_kode() -> str:
    """Aturan 22: modul ini beserta modul yang namanya dipinjam."""
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(["peta_manifes.py", "pulihkan.py"]):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def _daftar_dict(obj: Any, jalur: str, keluar: List[Tuple[str, List[Dict[str, Any]]]],
                 kedalaman: int = 0) -> None:
    """Kumpulkan setiap daftar berisi dict, beserta jalurnya."""
    if kedalaman > 3 or len(keluar) >= BATAS_JALUR:
        return
    if isinstance(obj, list):
        isi = [e for e in obj if isinstance(e, dict)]
        if isi:
            keluar.append((jalur or "(akar)", isi))
        return
    if isinstance(obj, dict):
        for k in sorted(obj.keys()):
            _daftar_dict(obj[k], f"{jalur}.{k}" if jalur else str(k), keluar,
                         kedalaman + 1)


def _medan_berpola(entri: List[Dict[str, Any]], pola: re.Pattern) -> Optional[str]:
    """Nama medan yang nilainya cocok pola pada mayoritas entri."""
    if not entri:
        return None
    contoh = entri[: min(len(entri), 500)]
    terbaik: Optional[str] = None
    skor_terbaik = 0.0
    kunci: set = set()
    for e in contoh:
        kunci.update(k for k in e.keys() if isinstance(k, str))
    for k in sorted(kunci):
        cocok = sum(
            1 for e in contoh
            if isinstance(e.get(k), str) and pola.match(e.get(k) or "")
        )
        skor = cocok / len(contoh)
        if skor > skor_terbaik:
            skor_terbaik = skor
            terbaik = k
    return terbaik if skor_terbaik >= 0.9 else None


def _ringkas_medan(entri: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Jumlah tiap medan angka; sebaran tiap medan berkardinalitas rendah."""
    angka: Dict[str, Dict[str, Any]] = {}
    boolean: Dict[str, int] = {}
    teks: Dict[str, Dict[str, Any]] = {}
    kunci: set = set()
    for e in entri:
        kunci.update(k for k in e.keys() if isinstance(k, str))
    for k in sorted(kunci):
        nilai = [e.get(k) for e in entri if k in e]
        angka_k = [v for v in nilai if isinstance(v, (int, float))
                   and not isinstance(v, bool)]
        bool_k = [v for v in nilai if isinstance(v, bool)]
        teks_k = [v for v in nilai if isinstance(v, str)]
        if angka_k and len(angka_k) >= len(nilai) * 0.5:
            angka[k] = {
                "cacah": len(angka_k),
                "jumlah": sum(angka_k),
                "minimum": min(angka_k),
                "maksimum": max(angka_k),
                "cacah_nol": sum(1 for v in angka_k if v == 0),
            }
        elif bool_k and len(bool_k) >= len(nilai) * 0.5:
            boolean[k] = sum(1 for v in bool_k if v)
        elif teks_k:
            unik = sorted(set(teks_k))
            if len(unik) <= BATAS_KARDINALITAS:
                teks[k] = {
                    "kardinalitas": len(unik),
                    "sebaran": {u: teks_k.count(u) for u in unik},
                }
            else:
                teks[k] = {
                    "kardinalitas": len(unik),
                    "contoh": unik[:BATAS_CONTOH],
                }
    return {"medan_angka": angka, "medan_boolean": boolean, "medan_teks": teks}


def baca_manifes(indeks: int, akar: str = ".") -> Tuple[Optional[Dict[str, Any]], int]:
    jalur = Path(akar) / pulihkan.nama_manifes(indeks)
    if not jalur.exists():
        return None, 0
    byte = jalur.stat().st_size
    isi = json.loads(jalur.read_text(encoding="utf-8"))
    return (isi if isinstance(isi, dict) else None), byte


def jalankan(akar: str = ".", total: int = pulihkan.TOTAL_PECAHAN) -> Dict[str, Any]:
    hilang: List[int] = []
    skema: List[Dict[str, Any]] = []
    sidik: List[str] = []
    byte_total = 0

    # (jalur) -> daftar pasangan (simbol, bulan, indeks_pecahan)
    pasangan: Dict[str, List[Tuple[str, str, int]]] = {}
    medan_ditemukan: Dict[str, Dict[str, Any]] = {}
    ringkas_jalur: Dict[str, Dict[str, Any]] = {}
    cacah_entri_jalur: Dict[str, int] = {}

    for i in range(int(total)):
        manifes, byte = baca_manifes(i, akar=akar)
        if manifes is None:
            hilang.append(i)
            continue
        byte_total += byte
        kode = manifes.get("sidik_kode")
        if isinstance(kode, str) and kode:
            sidik.append(kode)

        daftar: List[Tuple[str, List[Dict[str, Any]]]] = []
        _daftar_dict(manifes, "", daftar)

        per_jalur = []
        for jalur, entri in daftar:
            cacah_entri_jalur[jalur] = cacah_entri_jalur.get(jalur, 0) + len(entri)
            ms = _medan_berpola(entri, POLA_SIMBOL)
            mb = _medan_berpola(entri, POLA_BULAN)
            if jalur not in medan_ditemukan:
                medan_ditemukan[jalur] = {"medan_simbol": ms, "medan_bulan": mb}
            if ms and mb:
                simpan = pasangan.setdefault(jalur, [])
                for e in entri:
                    s, b = e.get(ms), e.get(mb)
                    if isinstance(s, str) and isinstance(b, str):
                        simpan.append((s, b, i))
            kunci_entri: set = set()
            for e in entri[: min(len(entri), 500)]:
                kunci_entri.update(k for k in e.keys() if isinstance(k, str))
            per_jalur.append({
                "jalur": jalur,
                "cacah_entri": len(entri),
                "kunci_entri": sorted(kunci_entri),
                "medan_simbol": ms,
                "medan_bulan": mb,
            })
            sebelum = ringkas_jalur.get(jalur)
            if sebelum is None:
                ringkas_jalur[jalur] = _ringkas_medan(entri)
            else:
                tambahan = _ringkas_medan(entri)
                for k, v in tambahan["medan_angka"].items():
                    lama = sebelum["medan_angka"].get(k)
                    if lama is None:
                        sebelum["medan_angka"][k] = v
                    else:
                        lama["cacah"] += v["cacah"]
                        lama["jumlah"] += v["jumlah"]
                        lama["minimum"] = min(lama["minimum"], v["minimum"])
                        lama["maksimum"] = max(lama["maksimum"], v["maksimum"])
                        lama["cacah_nol"] += v["cacah_nol"]
                for k, v in tambahan["medan_boolean"].items():
                    sebelum["medan_boolean"][k] = (
                        sebelum["medan_boolean"].get(k, 0) + v
                    )
                for k, v in tambahan["medan_teks"].items():
                    lama_t = sebelum["medan_teks"].get(k)
                    if lama_t is None or "sebaran" not in lama_t or "sebaran" not in v:
                        sebelum["medan_teks"].setdefault(k, v)
                    else:
                        for u, c in v["sebaran"].items():
                            lama_t["sebaran"][u] = lama_t["sebaran"].get(u, 0) + c
                        lama_t["kardinalitas"] = len(lama_t["sebaran"])

        skema.append({
            "indeks": i,
            "byte": byte,
            "kunci_atas": sorted(k for k in manifes.keys() if isinstance(k, str)),
            "daftar": per_jalur,
        })

    # Jalur utama = jalur berpasangan simbol-bulan dengan entri terbanyak.
    jalur_utama = None
    if pasangan:
        jalur_utama = max(pasangan.keys(), key=lambda j: len(pasangan[j]))

    sensus: Dict[str, Any] = {"jalur_utama": jalur_utama}
    per_simbol: Dict[str, int] = {}
    if jalur_utama is not None:
        semua = pasangan[jalur_utama]
        kunci_sb = [(s, b) for s, b, _ in semua]
        unik_sb = set(kunci_sb)
        simbol_unik = sorted({s for s, _ in kunci_sb})
        pecahan_per_simbol: Dict[str, set] = {}
        for s, _b, i in semua:
            pecahan_per_simbol.setdefault(s, set()).add(i)
            per_simbol[s] = per_simbol.get(s, 0) + 1
        lintas = sorted(s for s, p in pecahan_per_simbol.items() if len(p) > 1)
        sensus.update({
            "medan_simbol": medan_ditemukan.get(jalur_utama, {}).get("medan_simbol"),
            "medan_bulan": medan_ditemukan.get(jalur_utama, {}).get("medan_bulan"),
            "cacah_entri": len(semua),
            "cacah_simbol_bulan_unik": len(unik_sb),
            "cacah_simbol_bulan_ganda": len(kunci_sb) - len(unik_sb),
            "cacah_simbol_unik": len(simbol_unik),
            "cacah_simbol_lintas_pecahan": len(lintas),
            "simbol_lintas_pecahan": lintas[:BATAS_CONTOH],
            "selisih_terhadap_penyebut_semesta": len(unik_sb) - PENYEBUT_SEMESTA,
            "selisih_terhadap_penyebut_lolos": len(unik_sb) - PENYEBUT_LOLOS,
            "selisih_terhadap_cacah_simbol": len(simbol_unik) - CACAH_SIMBOL_TERCATAT,
            "bulan_paling_awal": min((b for _s, b in kunci_sb), default=None),
            "bulan_paling_akhir": max((b for _s, b in kunci_sb), default=None),
        })

    kendali = []
    for nama in KENDALI_NAMA:
        cacah = int(per_simbol.get(nama, 0))
        kendali.append({"simbol": nama, "cacah_bulan": cacah, "sah": cacah > 0})

    ringkasan: Dict[str, Any] = {
        "cacah_manifes_diminta": int(total),
        "cacah_manifes_dibaca": len(skema),
        "manifes_hilang": hilang,
        "byte_manifes_total": byte_total,
        "sidik_kode_manifes": sorted(set(sidik)),
        "sidik_seragam": bool(len(set(sidik)) == 1),
        "daftar_utama_hilang": bool(jalur_utama is None),
        "jalur_berpasangan": sorted(pasangan.keys()),
        "cacah_entri_per_jalur": dict(sorted(cacah_entri_jalur.items())),
        "sensus": sensus,
        "kendali": kendali,
        "kendali_sah": bool(all(k["sah"] for k in kendali) and not hilang),
        "catatan_penyebut": (
            "cacah_simbol_bulan_unik adalah cacah entri simbol-bulan yang TERDAFTAR "
            "di manifes, bukan cacah parquet yang LOLOS gerbang; keduanya penyebut "
            "berbeda dan angkanya dilarang dipertukarkan (aturan 76, KC-39)"
        ),
        "catatan_medan": (
            "medan_simbol dan medan_bulan DITEMUKAN dari bentuk nilai, bukan "
            "ditebak dari nama; nama yang dilaporkan di sini sah dikutip sebagai "
            "nama terbaca (aturan 71)"
        ),
        "catatan_penggugur": (
            "yang menggugurkan hanya cacat bahan baku: manifes hilang, sidik tak "
            "seragam, simbol-bulan ganda, simbol muncul lintas pecahan, atau "
            "daftar utama tidak ditemukan. Selisih terhadap 19.598, 19.586, dan "
            "787 TIDAK menggugurkan apa pun (aturan 24, 72)"
        ),
        "bukan_adjudikasi": (
            "laporan ini tidak memuat blok uji apa pun; vonis alat bukan "
            "adjudikasi (KC-49)"
        ),
    }

    laporan: Dict[str, Any] = {
        "bukan_bukti": False,
        "versi_peta_manifes": VERSI,
        "ringkasan": ringkasan,
        "skema": skema,
        "ringkas_medan_per_jalur": ringkas_jalur,
        "cacah_bulan_per_simbol": dict(sorted(per_simbol.items())),
        "sidik_kode": sidik_kode(),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    tujuan = Path(akar) / KELUARAN
    tujuan.parent.mkdir(parents=True, exist_ok=True)
    tujuan.write_text(
        json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return laporan


def kode_keluar(ringkasan: Dict[str, Any]) -> int:
    sensus = ringkasan.get("sensus") or {}
    gugur = (
        bool(ringkasan.get("manifes_hilang"))
        or not bool(ringkasan.get("sidik_seragam"))
        or bool(ringkasan.get("daftar_utama_hilang"))
        or int(sensus.get("cacah_simbol_bulan_ganda") or 0) != 0
        or int(sensus.get("cacah_simbol_lintas_pecahan") or 0) != 0
        or not bool(ringkasan.get("kendali_sah"))
    )
    return 2 if gugur else 0


def main() -> int:
    hasil = jalankan()
    ringkasan = hasil["ringkasan"]
    print(json.dumps({"ringkasan": ringkasan}, ensure_ascii=False, indent=2,
                     sort_keys=True))
    print("byte_laporan=%d" % Path(KELUARAN).stat().st_size)
    return kode_keluar(ringkasan)


if __name__ == "__main__":
    raise SystemExit(main())
