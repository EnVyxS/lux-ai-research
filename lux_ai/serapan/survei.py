"""Survei semesta arsip: rentang hidup tiap simbol dan sifat format berkas.

Satu run membayar empat utang verifikasi sekaligus, dan tiap medan dinamai
menurut apa yang benar-benar diukurnya (aturan 16).

1. Rentang bulan 1m tiap simbol dari indeks arsip.
2. Ukuran delisting yang BENAR: jarak bulan terakhir sebuah simbol terhadap
   bulan tutup terakhir semesta. Kehadiran di indeks bukan ukuran delisting,
   karena arsip menyimpan simbol mati selamanya (KC-5).
3. Stempel waktu bar terakhir simbol yang sudah mati, diukur dari isi berkas.
4. Bulan persis arsip berpindah dari format tanpa header ke format berheader,
   diukur bulan demi bulan tanpa mengandaikan peralihannya monoton.

Sekalian diukur PANJANG DIGIT stempel waktu tiap bulan yang diunduh. Arsip
Binance pernah berpindah dari milidetik ke mikrodetik, dan kode yang mengandaikan
satu satuan akan salah menyusun ember waktu tanpa memberi tanda apa pun.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path

from . import arsip, klines

LAPORAN = "reports/survei_semesta.json"
RENTANG = "reports/semesta_rentang.json"
PROGRES = "reports/survei_progres.json"

JEDA_MATI_BULAN = 2
BATAS_R8 = "2026-01"
SIMBOL_AKHIR = ["SRMUSDT", "COCOSUSDT", "BTSUSDT"]
SIMBOL_HEADER = ["BTCUSDT", "ETHUSDT", "LINKUSDT"]
AWAL_HEADER = "2020-01"
AKHIR_HEADER = "2023-12"


def sidik_kode() -> str:
    h = hashlib.sha256()
    for nama in ("arsip.py", "klines.py", "survei.py"):
        h.update(Path(__file__).with_name(nama).read_bytes())
    return h.hexdigest()


def _pecah(bulan: str):
    tahun, bln = bulan.split("-")
    return int(tahun), int(bln)


def bulan_dalam_rentang(awal: str, akhir: str) -> list:
    """Deret bulan YYYY-MM inklusif dari awal sampai akhir."""
    ta, ba = _pecah(awal)
    tb, bb = _pecah(akhir)
    keluar = []
    t, b = ta, ba
    while (t, b) <= (tb, bb):
        keluar.append(f"{t:04d}-{b:02d}")
        b += 1
        if b == 13:
            t, b = t + 1, 1
    return keluar


def selisih_bulan(lebih_tua: str, acuan: str) -> int:
    """Berapa bulan `lebih_tua` tertinggal di belakang `acuan`."""
    ta, ba = _pecah(lebih_tua)
    tb, bb = _pecah(acuan)
    return (tb - ta) * 12 + (bb - ba)


def terhenti(bulan_terakhir: str, bulan_acuan: str, jeda: int = JEDA_MATI_BULAN) -> bool:
    """True bila simbol berhenti terbit jauh sebelum semesta berhenti terbit.

    Inilah ukuran delisting yang sah. Kehadiran simbol di indeks arsip TIDAK
    mengukur apa pun tentang delisting.
    """
    return selisih_bulan(bulan_terakhir, bulan_acuan) >= jeda


def cacah_lebih_tua(rentang: dict, batas: str) -> int:
    """Cacah simbol yang bulan terakhirnya lebih tua daripada `batas`."""
    return sum(1 for r in rentang.values() if r["bulan_terakhir"] < batas)


def ringkas_header(peta: dict) -> dict:
    """Ringkas peta {bulan: berheader} menjadi batas peralihan format.

    `monoton` bernilai False bila pernah ada bulan berheader yang diikuti bulan
    tanpa header. Bila itu terjadi, gagasan "satu bulan peralihan" salah dan
    tidak boleh dipakai.
    """
    urut = sorted(peta)
    berheader = [b for b in urut if peta[b]]
    tanpa = [b for b in urut if not peta[b]]
    monoton = True
    if berheader and tanpa:
        monoton = max(tanpa) < min(berheader)
    return {
        "bulan_diperiksa": len(urut),
        "bulan_tanpa_header_terakhir": max(tanpa) if tanpa else None,
        "bulan_berheader_pertama": min(berheader) if berheader else None,
        "monoton": monoton,
    }


def satuan_stempel(nilai: int) -> str:
    """Tebak satuan stempel dari besarannya, dan katakan bila tak dikenali."""
    if 10**12 <= nilai < 10**13:
        return "milidetik"
    if 10**15 <= nilai < 10**16:
        return "mikrodetik"
    return "tidak_dikenali"


def iso_dari_stempel(nilai: int) -> str:
    satuan = satuan_stempel(nilai)
    if satuan == "mikrodetik":
        detik = nilai / 1_000_000
    elif satuan == "milidetik":
        detik = nilai / 1000
    else:
        return "tidak_dikenali"
    return dt.datetime.fromtimestamp(detik, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _tulis(path: str, obj) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n")


def _progres(**kv) -> None:
    _tulis(PROGRES, kv)


def survei_rentang() -> dict:
    """Bulan pertama, bulan terakhir, dan cacah bulan 1m untuk seluruh simbol."""
    simbol = arsip.semesta_simbol()
    rentang = {}
    gagal = []
    for i, s in enumerate(simbol, 1):
        try:
            bulan = arsip.bulan_tersedia(s, "1m")
        except Exception as exc:  # noqa: BLE001
            gagal.append({"simbol": s, "galat": str(exc)})
            continue
        if not bulan:
            gagal.append({"simbol": s, "galat": "tidak ada bulan 1m"})
            continue
        rentang[s] = {
            "bulan_pertama": bulan[0],
            "bulan_terakhir": bulan[-1],
            "cacah_bulan": len(bulan),
        }
        if i % 25 == 0:
            _progres(tahap="rentang", selesai=f"{i}/{len(simbol)}", terakhir=s)
    _progres(tahap="rentang_selesai", selesai=f"{len(rentang)}/{len(simbol)}")
    return {"rentang": rentang, "gagal_listing": gagal, "cacah_simbol": len(simbol)}


def ukur_bar_terakhir(simbol: str, bulan: str) -> dict:
    """Stempel waktu bar terakhir sebuah simbol, dari isi berkas bulan itu."""
    data = arsip.unduh_terverifikasi(arsip.url_klines(simbol, "1m", bulan))
    df, dibuang = klines.rapikan(klines.baca_zip(data, teks=True))
    akhir = int(df["open_time"].iloc[-1])
    awal = int(df["open_time"].iloc[0])
    return {
        "simbol": simbol,
        "bulan": bulan,
        "baris": int(len(df)),
        "baris_dibuang": int(dibuang),
        "stempel_bar_pertama": awal,
        "stempel_bar_terakhir": akhir,
        "panjang_digit_stempel": len(str(akhir)),
        "satuan_stempel": satuan_stempel(akhir),
        "bar_pertama_utc": iso_dari_stempel(awal),
        "bar_terakhir_utc": iso_dari_stempel(akhir),
    }


def ukur_header(simbol: str, bulan_tersedia: list) -> dict:
    """Ada tidaknya header, bulan demi bulan, tanpa mengandaikan monoton."""
    diminta = set(bulan_dalam_rentang(AWAL_HEADER, AKHIR_HEADER))
    peta = {}
    digit = {}
    for bulan in sorted(diminta & set(bulan_tersedia)):
        data = arsip.unduh_terverifikasi(arsip.url_klines(simbol, "1m", bulan))
        baris = klines.baris_pertama(data)
        peta[bulan] = klines.punya_header(baris)
        df, _ = klines.rapikan(klines.baca_zip(data, teks=True))
        digit[bulan] = len(str(int(df["open_time"].iloc[0])))
        _progres(tahap="header", simbol=simbol, terakhir=bulan)
    hasil = ringkas_header(peta)
    hasil["simbol"] = simbol
    hasil["berheader_per_bulan"] = peta
    hasil["panjang_digit_stempel_per_bulan"] = digit
    return hasil


def jalankan() -> int:
    _progres(tahap="mulai", mulai_utc=dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
    dasar = survei_rentang()
    rentang = dasar["rentang"]
    _tulis(RENTANG, {"rentang": rentang})

    bulan_tutup = max(r["bulan_terakhir"] for r in rentang.values())
    mati = sorted(s for s, r in rentang.items() if terhenti(r["bulan_terakhir"], bulan_tutup))

    akhir = []
    for s in SIMBOL_AKHIR:
        if s in rentang:
            akhir.append(ukur_bar_terakhir(s, rentang[s]["bulan_terakhir"]))

    header = []
    for s in SIMBOL_HEADER:
        if s in rentang:
            bulan = arsip.bulan_tersedia(s, "1m")
            header.append(ukur_header(s, bulan))

    laporan = {
        "nama": "survei_semesta",
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "sidik_kode": sidik_kode(),
        "sumber_arsip": arsip.S3,
        "cacah_simbol_indeks": dasar["cacah_simbol"],
        "cacah_simbol_dengan_1m": len(rentang),
        "gagal_listing": dasar["gagal_listing"],
        "bulan_tutup_terakhir_semesta": bulan_tutup,
        "jeda_mati_bulan": JEDA_MATI_BULAN,
        "cacah_simbol_terhenti": len(mati),
        "cacah_simbol_masih_terbit": len(rentang) - len(mati),
        "batas_r8": BATAS_R8,
        "cacah_bulan_terakhir_lebih_tua_dari_batas_r8": cacah_lebih_tua(rentang, BATAS_R8),
        "bulan_pertama_paling_awal": min(r["bulan_pertama"] for r in rentang.values()),
        "bar_terakhir_simbol_mati": akhir,
        "peralihan_header": header,
        "catatan": "cacah_simbol_terhenti mengukur jarak bulan terakhir simbol terhadap bulan tutup semesta, BUKAN kehadiran di indeks arsip",
    }
    _tulis(LAPORAN, laporan)
    _progres(tahap="selesai", cacah_simbol=len(rentang))
    print(json.dumps({k: v for k, v in laporan.items() if k not in ("peralihan_header",)}, indent=2, ensure_ascii=False))
    for h in header:
        print(json.dumps({k: v for k, v in h.items() if k != "berheader_per_bulan"}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(jalankan())
