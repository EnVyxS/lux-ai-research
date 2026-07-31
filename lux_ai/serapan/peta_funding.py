"""peta_funding.py — peringkas KEDUA atas kedelapan manifes pecahan.

Sasaran: membayar utang **Lapis A** (ADR-A024), yang dilarang ditutup paksa:

  (a) **blokir 4** — medan `funding_ada`. Ia tercatat sebagai salah satu dari 28
      kunci entri manifes, namun TIDAK muncul pada lajur boolean maupun teks di
      `reports/peta_manifes.json`. Modul ini mencacah nilainya apa adanya,
      termasuk `null` dan kunci yang hilang, tanpa penggolongan lebih dulu.

  (b) **utang ukur 32** — arti `terhenti` = 587. Modul ini tidak menebak artinya;
      ia menyilangkan `terhenti` terhadap `gerbang_lolos`, `karantina`,
      `berheader`, `dikemas`, terhadap sebaran `baris`, terhadap bulan, dan
      terhadap pertanyaan apakah entri terhenti selalu bulan TERAKHIR simbolnya.

  (c) **utang verifikasi 50** — apakah simbol non-Latin ikut dalam 787, dan
      apakah ada simbol lain yang gagal `POLA_SIMBOL`.

KOREKSI 19 DIPERBAIKI: modul ini tidak memakai ambang kardinalitas sama sekali.
Setiap sebaran digabung lintas kedelapan pecahan. Bila suatu daftar dipotong,
pemotongan itu ditulis eksplisit lewat pasangan kunci `*_dipotong` dan
`*_penyebut` — tidak ada pemotongan diam-diam (aturan 86 (b)).

Modul ini BUKAN bukti sampai laporannya lahir dari GitHub Actions dan dibaca
pada ref runner (aturan 38).
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

from lux_ai.serapan import pulihkan

VERSI = 1
KELUARAN = "reports/peta_funding.json"

# Angka tercatat yang WAJIB didamaikan, bukan diasumsikan.
PENYEBUT_SEMESTA = 19598
PENYEBUT_LOLOS = 19586
CACAH_SIMBOL_TERCATAT = 787
CACAH_TERHENTI_TERCATAT = 587
CACAH_HIDUP_TANPA_FUNDING_TERCATAT = 33
SIMBOL_LIMA = ("BNXUSDT", "ICPUSDT", "JUPUSDT", "QTUMUSDT", "TLMUSDT")
KENDALI_NAMA = ("BTCUSDT", "ETHUSDT")
KENDALI_BULAN = 78

POLA_SIMBOL = re.compile(r"^[A-Z0-9]{2,20}USDT$")
POLA_BULAN = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")

BATAS_DAFTAR = 60

AKAR = pathlib.Path(__file__).resolve().parents[2]


def sidik_kode() -> str:
    """sha256 atas kode sumber modul ini sendiri."""
    return hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()


def _jalur_manifes(indeks: int) -> pathlib.Path:
    nama = str(pulihkan.nama_manifes(indeks))
    jalur = pathlib.Path(nama)
    if not jalur.exists():
        jalur = AKAR / nama
    return jalur


def _entri_dari(muatan) -> list:
    """Ambil daftar entri manifes tanpa mengandaikan bentuknya."""
    if not isinstance(muatan, dict):
        return []
    jalur = muatan.get("manifes")
    if isinstance(jalur, list):
        return [e for e in jalur if isinstance(e, dict)]
    if isinstance(jalur, dict):
        keluar = []
        for kunci, nilai in jalur.items():
            if isinstance(nilai, dict):
                salin = dict(nilai)
                salin.setdefault("__kunci", kunci)
                keluar.append(salin)
        return keluar
    return []


def _kunci_nilai(nilai) -> str:
    """Penanda nilai yang membedakan null, boolean, angka, dan teks."""
    if nilai is None:
        return "null"
    if isinstance(nilai, bool):
        return "boolean:true" if nilai else "boolean:false"
    if isinstance(nilai, int):
        return "angka:%d" % nilai
    if isinstance(nilai, float):
        return "angka:%r" % nilai
    if isinstance(nilai, str):
        return "teks:%s" % nilai
    if isinstance(nilai, list):
        return "larik:%d" % len(nilai)
    if isinstance(nilai, dict):
        return "peta:%d" % len(nilai)
    return "lain:%s" % type(nilai).__name__


def _potong(pasangan, batas=BATAS_DAFTAR):
    """Potong daftar SECARA TERBUKA. Kembalikan (daftar, dipotong, penyebut)."""
    penyebut = len(pasangan)
    return list(pasangan[:batas]), bool(penyebut > batas), penyebut


def _statistik(angka):
    bersih = [a for a in angka if isinstance(a, (int, float)) and not isinstance(a, bool)]
    if not bersih:
        return {"cacah": 0, "jumlah": 0, "min": None, "maks": None}
    return {
        "cacah": len(bersih),
        "jumlah": sum(bersih),
        "min": min(bersih),
        "maks": max(bersih),
    }


def jalankan() -> dict:
    entri_semua = []
    per_pecahan = {}
    manifes_hilang = []

    for indeks in range(pulihkan.TOTAL_PECAHAN):
        jalur = _jalur_manifes(indeks)
        if not jalur.exists():
            manifes_hilang.append(str(jalur))
            continue
        muatan = json.loads(jalur.read_text())
        entri = _entri_dari(muatan)
        per_pecahan[str(indeks)] = len(entri)
        for satu in entri:
            satu["__pecahan"] = indeks
        entri_semua.extend(entri)

    cacah_entri = len(entri_semua)

    # ---- kerangka per simbol ------------------------------------------------
    bulan_per_simbol = defaultdict(set)
    for satu in entri_semua:
        simbol = satu.get("simbol")
        bulan = satu.get("bulan")
        if isinstance(simbol, str) and isinstance(bulan, str):
            bulan_per_simbol[simbol].add(bulan)

    bulan_terakhir = {s: max(b) for s, b in bulan_per_simbol.items() if b}
    cacah_simbol_unik = len(bulan_per_simbol)

    # ---- (a) funding_ada ----------------------------------------------------
    funding_nilai = Counter()
    funding_per_pecahan = defaultdict(Counter)
    funding_hilang = 0
    simbol_funding = defaultdict(Counter)

    for satu in entri_semua:
        pecahan = satu.get("__pecahan")
        simbol = satu.get("simbol")
        if "funding_ada" not in satu:
            funding_hilang += 1
            kunci = "KUNCI_HILANG"
        else:
            kunci = _kunci_nilai(satu.get("funding_ada"))
        funding_nilai[kunci] += 1
        funding_per_pecahan[str(pecahan)][kunci] += 1
        if isinstance(simbol, str):
            simbol_funding[simbol][kunci] += 1

    simbol_funding_benar = sorted(
        s for s, c in simbol_funding.items() if c.get("boolean:true", 0) > 0
    )
    bulan_funding_benar = sum(
        c.get("boolean:true", 0) for c in simbol_funding.values()
    )
    daftar_fb, fb_dipotong, fb_penyebut = _potong(
        [{"simbol": s, "cacah_true": simbol_funding[s]["boolean:true"]} for s in simbol_funding_benar]
    )

    lima_terperiksa = {
        nama: dict(simbol_funding.get(nama, Counter())) for nama in SIMBOL_LIMA
    }

    funding = {
        "sebaran_nilai": dict(funding_nilai),
        "cacah_kunci_hilang": funding_hilang,
        "sebaran_per_pecahan": {k: dict(v) for k, v in sorted(funding_per_pecahan.items())},
        "cacah_simbol_funding_true": len(simbol_funding_benar),
        "cacah_bulan_funding_true": bulan_funding_benar,
        "simbol_funding_true": daftar_fb,
        "simbol_funding_true_dipotong": fb_dipotong,
        "simbol_funding_true_penyebut": fb_penyebut,
        "lima_simbol_tercatat": lima_terperiksa,
        "cocok_33": bulan_funding_benar == CACAH_HIDUP_TANPA_FUNDING_TERCATAT,
        "cocok_lima_simbol": sorted(SIMBOL_LIMA) == simbol_funding_benar,
    }

    # ---- (b) terhenti -------------------------------------------------------
    silang = defaultdict(Counter)
    baris_terhenti = []
    baris_tak_terhenti = []
    bulan_terhenti = Counter()
    simbol_terhenti = Counter()
    terhenti_bulan_terakhir = 0
    terhenti_bukan_terakhir = 0
    cacah_terhenti = 0
    terhenti_hilang = 0

    for satu in entri_semua:
        if "terhenti" not in satu:
            terhenti_hilang += 1
            continue
        nyala = bool(satu.get("terhenti"))
        baris = satu.get("baris")
        if nyala:
            cacah_terhenti += 1
            baris_terhenti.append(baris)
            simbol = satu.get("simbol")
            bulan = satu.get("bulan")
            if isinstance(bulan, str):
                bulan_terhenti[bulan] += 1
            if isinstance(simbol, str):
                simbol_terhenti[simbol] += 1
                if bulan_terakhir.get(simbol) == bulan:
                    terhenti_bulan_terakhir += 1
                else:
                    terhenti_bukan_terakhir += 1
        else:
            baris_tak_terhenti.append(baris)
        for lawan in ("gerbang_lolos", "karantina", "berheader", "dikemas", "gagal_unduh"):
            if lawan in satu:
                sel = "%s=%s" % (lawan, bool(satu.get(lawan)))
                silang["terhenti=%s" % nyala][sel] += 1

    daftar_st, st_dipotong, st_penyebut = _potong(
        [
            {"simbol": s, "cacah": n, "bulan_simbol": len(bulan_per_simbol.get(s, ()))}
            for s, n in simbol_terhenti.most_common()
        ]
    )

    terhenti = {
        "cacah_terhenti_true": cacah_terhenti,
        "cacah_kunci_hilang": terhenti_hilang,
        "cocok_587": cacah_terhenti == CACAH_TERHENTI_TERCATAT,
        "silang": {k: dict(v) for k, v in sorted(silang.items())},
        "baris_saat_terhenti": _statistik(baris_terhenti),
        "baris_saat_tidak_terhenti": _statistik(baris_tak_terhenti),
        "sebaran_bulan": dict(sorted(bulan_terhenti.items())),
        "cacah_simbol_terhenti": len(simbol_terhenti),
        "simbol_terhenti": daftar_st,
        "simbol_terhenti_dipotong": st_dipotong,
        "simbol_terhenti_penyebut": st_penyebut,
        "terhenti_pada_bulan_terakhir": terhenti_bulan_terakhir,
        "terhenti_bukan_bulan_terakhir": terhenti_bukan_terakhir,
    }

    # ---- (c) keanggotaan simbol --------------------------------------------
    tak_berpola = sorted(
        (s for s in bulan_per_simbol if not POLA_SIMBOL.match(s)),
        key=lambda s: (-len(bulan_per_simbol[s]), s),
    )
    daftar_tb, tb_dipotong, tb_penyebut = _potong(
        [{"simbol": s, "cacah_bulan": len(bulan_per_simbol[s])} for s in tak_berpola]
    )
    bulan_tak_berpola = sum(len(bulan_per_simbol[s]) for s in tak_berpola)

    bulan_cacat = sorted(
        {b for bs in bulan_per_simbol.values() for b in bs if not POLA_BULAN.match(b)}
    )

    keanggotaan = {
        "cacah_simbol_unik": cacah_simbol_unik,
        "cocok_787": cacah_simbol_unik == CACAH_SIMBOL_TERCATAT,
        "cacah_simbol_tak_berpola": len(tak_berpola),
        "cacah_bulan_pada_simbol_tak_berpola": bulan_tak_berpola,
        "simbol_tak_berpola": daftar_tb,
        "simbol_tak_berpola_dipotong": tb_dipotong,
        "simbol_tak_berpola_penyebut": tb_penyebut,
        "bulan_tak_berpola": bulan_cacat,
        "simbol_berpola_ikut_dalam_cacah": cacah_simbol_unik - len(tak_berpola),
    }

    # ---- kendali ------------------------------------------------------------
    kendali = {
        nama: len(bulan_per_simbol.get(nama, ()))
        for nama in KENDALI_NAMA
    }
    kendali_sah = all(v == KENDALI_BULAN for v in kendali.values())

    return {
        "versi_peta_funding": VERSI,
        "bukan_bukti": False,
        "waktu_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "sidik_kode": sidik_kode(),
        "cacah_entri": cacah_entri,
        "cacah_entri_per_pecahan": dict(sorted(per_pecahan.items())),
        "manifes_hilang": manifes_hilang,
        "selisih_penyebut_semesta": cacah_entri - PENYEBUT_SEMESTA,
        "selisih_penyebut_lolos": cacah_entri - PENYEBUT_LOLOS,
        "kendali": kendali,
        "kendali_sah": kendali_sah,
        "funding": funding,
        "terhenti": terhenti,
        "keanggotaan": keanggotaan,
    }


def kode_keluar(hasil: dict) -> int:
    """0 hanya bila kendali sah, tidak ada manifes hilang, dan penyebut cocok."""
    if hasil.get("manifes_hilang"):
        return 2
    if not hasil.get("kendali_sah"):
        return 3
    if hasil.get("selisih_penyebut_semesta") != 0:
        return 4
    return 0


def main() -> int:
    hasil = jalankan()
    keluaran = pathlib.Path(KELUARAN)
    keluaran.parent.mkdir(parents=True, exist_ok=True)
    keluaran.write_text(json.dumps(hasil, indent=2, sort_keys=True, ensure_ascii=False) + "\n")

    print("cacah_entri=%s" % hasil["cacah_entri"])
    print("cacah_simbol_unik=%s" % hasil["keanggotaan"]["cacah_simbol_unik"])
    print("funding.sebaran_nilai=%s" % json.dumps(hasil["funding"]["sebaran_nilai"], sort_keys=True))
    print("funding.cacah_simbol_funding_true=%s" % hasil["funding"]["cacah_simbol_funding_true"])
    print("funding.cacah_bulan_funding_true=%s" % hasil["funding"]["cacah_bulan_funding_true"])
    print("terhenti.cacah_terhenti_true=%s" % hasil["terhenti"]["cacah_terhenti_true"])
    print("terhenti.pada_bulan_terakhir=%s" % hasil["terhenti"]["terhenti_pada_bulan_terakhir"])
    print("keanggotaan.cacah_simbol_tak_berpola=%s" % hasil["keanggotaan"]["cacah_simbol_tak_berpola"])
    print("byte_laporan=%s" % keluaran.stat().st_size)

    kode = kode_keluar(hasil)
    print("kode_keluar=%s" % kode)
    return kode


if __name__ == "__main__":
    sys.exit(main())
