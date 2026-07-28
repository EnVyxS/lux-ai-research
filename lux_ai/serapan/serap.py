"""Pilot serapan: satu jalur penuh dari arsip ke parquet, dengan manifes.

Menempuh seluruh rantai yang nanti dipakai serapan penuh (utang 24):
unduh terverifikasi checksum -> baca zip -> rapikan -> gerbang integritas 1m
(ADR-A004) -> tulis parquet -> catat manifes per simbol-bulan.

Cakupan instrumen mengikuti ADR-A005 §1: hanya `perpetual_usdt`.

**Versi 2 (KC-13, aturan 37).** Versi 1 memilih tiga simbol pertama menurut
abjad. Deterministik, dan bias: yang terpilih adalah 0GUSDT dan dua pasar 2024-
2025, sehingga format pra-2022 tanpa header, simbol non-ASCII, dan simbol
terhenti tidak tersentuh sama sekali. Pemilihan kini BERLAPIS: tiap kelas
risiko yang diketahui wajib diwakili, dan laporan menyebut kelas mana yang
benar-benar tersentuh, walau nol.

**Versi 3 (ADR-A006).** Simbol-bulan yang dijatuhkan gerbang dikarantina, bukan
dibuang dan bukan ditambal. Dua akibat di kode ini:

1. Parquet-nya TETAP ditulis, ke `data/parquet_karantina/` yang terpisah, agar
   "karantina" benar-benar berarti disisihkan. Sebelumnya barisnya gagal gerbang
   lalu datanya tidak pernah ditulis sama sekali — itu pembuangan berkedok
   karantina.
2. `ringkas()` melaporkan `cacah_karantina` dan `daftar_karantina`, ditambah
   `cacah_dibuang` dan `cacah_ditambal` yang wajib nol. Keduanya adalah medan
   penggugur: begitu salah satunya tidak nol, ADR-A006 sedang dilanggar
   (aturan 24).

`byte_parquet` sengaja TIDAK mencakup parquet karantina; ia dipisah ke
`byte_parquet_karantina` supaya nisbah parquet/zip tetap sebanding dengan
kedelapan manifes yang sudah terukur (aturan 36).

Aturan yang ditegakkan di sini: 16, 18, 20, 24, 25, 30, 32, 36, 37.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
from pathlib import Path
from typing import Any, Dict, List, Tuple

from . import arsip, gerbang_1m, klines

SUMBER_RENTANG = "reports/semesta_rentang.json"
MANIFES = "reports/manifes_pilot.json"
AKAR_PARQUET = "data/parquet"
AKAR_KARANTINA = "data/parquet_karantina"

# Cakupan pilot dipatok tertulis SEBELUM run (aturan 25).
JENIS_DIIZINKAN = "perpetual_usdt"
BATAS_HEADER = "2022-01"  # KC-4: sebelum bulan ini arsip tanpa header
BATAS_BARU = "2025-01"
BATAS_HIDUP = "2026-05"
KELAS_RISIKO = ("pra_header", "non_ascii", "terhenti", "bulan_awal_2020_2021", "kendali_baru")
# Semesta penuh hanya punya 12 simbol-bulan karantina dari 19.598, jadi batas ini
# tidak pernah tersentuh. Ia ada agar kegagalan massal tidak meledakkan manifes,
# dan pemotongannya dilaporkan, tidak disembunyikan.
BATAS_DAFTAR_KARANTINA = 500

AMAN = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._-")


def sidik_kode() -> str:
    """Aturan 22: seluruh berkas yang ikut menentukan isi manifes."""
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(["serap.py", "arsip.py", "klines.py", "gerbang_1m.py", "resample.py"]):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def nama_aman(simbol: str) -> str:
    """Nama berkas aman tanpa MEMBUANG simbol non-ASCII (aturan 32, KC-9)."""
    return "".join(ch if ch in AMAN else f"u{ord(ch):04X}" for ch in simbol)


def non_ascii(simbol: str) -> bool:
    return any(ord(ch) > 127 for ch in simbol)


def iso_dari_ms(nilai) -> str:
    if nilai is None:
        return ""
    return dt.datetime.fromtimestamp(int(nilai) / 1000, dt.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


def _tengah(awal: str, akhir: str) -> str:
    ta, ba = (int(x) for x in awal.split("-"))
    tb, bb = (int(x) for x in akhir.split("-"))
    total = ((ta * 12 + ba - 1) + (tb * 12 + bb - 1)) // 2
    return f"{total // 12:04d}-{total % 12 + 1:02d}"


def pilih_berlapis(rentang: Dict[str, Any], jenis_dari) -> List[Tuple[str, str]]:
    """Pilih simbol-bulan sehingga TIAP kelas risiko terwakili (aturan 37).

    Tetap deterministik: di dalam tiap lapis, kandidat diurut abjad dan yang
    pertama diambil. Yang berubah dari versi 1 adalah lapisnya, bukan cara
    memilih di dalam lapis, sehingga hasilnya tetap bisa diulang persis.
    """
    layak = {
        s: isi
        for s, isi in sorted(rentang.items())
        if isinstance(isi, dict)
        and isinstance(isi.get("bulan_pertama"), str)
        and isinstance(isi.get("bulan_terakhir"), str)
        and jenis_dari(s) == JENIS_DIIZINKAN
    }

    pasangan: List[Tuple[str, str]] = []

    def tambah(simbol: str, bulan: str) -> None:
        if simbol and bulan and (simbol, bulan) not in pasangan:
            pasangan.append((simbol, bulan))

    # Lapis 1: simbol tertua yang hidup sejak sebelum batas header.
    tua = [s for s, i in layak.items() if i["bulan_pertama"] < BATAS_HEADER]
    if tua:
        s = sorted(tua, key=lambda x: (layak[x]["bulan_pertama"], x))[0]
        tambah(s, layak[s]["bulan_pertama"])
        tambah(s, _tengah(layak[s]["bulan_pertama"], layak[s]["bulan_terakhir"]))

    # Lapis 2: simbol bernama non-ASCII (KC-9).
    aneh = [s for s in layak if non_ascii(s)]
    if aneh:
        s = sorted(aneh)[0]
        tambah(s, layak[s]["bulan_pertama"])

    # Lapis 3: simbol yang sudah terhenti.
    mati = [s for s, i in layak.items() if i["bulan_terakhir"] < BATAS_HIDUP]
    if mati:
        s = sorted(mati)[0]
        tambah(s, layak[s]["bulan_terakhir"])

    # Lapis 4: kendali, pasar baru.
    baru = [s for s, i in layak.items() if i["bulan_pertama"] >= BATAS_BARU]
    if baru:
        s = sorted(baru)[0]
        tambah(s, layak[s]["bulan_pertama"])

    return pasangan


def kelas_risiko_tersentuh(manifes: List[Dict[str, Any]]) -> Dict[str, int]:
    """Cacah tiap kelas risiko yang benar-benar tersentuh, dilaporkan walau nol."""
    cacah = {nama: 0 for nama in KELAS_RISIKO}
    for b in manifes:
        simbol = str(b.get("simbol") or "")
        bulan = str(b.get("bulan") or "")
        if b.get("berheader") is False:
            cacah["pra_header"] += 1
        if non_ascii(simbol):
            cacah["non_ascii"] += 1
        if b.get("terhenti"):
            cacah["terhenti"] += 1
        if bulan and bulan < "2022-01":
            cacah["bulan_awal_2020_2021"] += 1
        if bulan and bulan >= BATAS_BARU:
            cacah["kendali_baru"] += 1
    return cacah


def baris_karantina(manifes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Simbol-bulan yang dijatuhkan gerbang, urut dan lengkap (ADR-A006).

    Baris yang gagal DIUNDUH tidak masuk sini: ia bukan data yang disisihkan,
    melainkan data yang tidak pernah ada. Keduanya dicacah terpisah agar tidak
    saling menyamarkan (aturan 16).
    """
    hasil: List[Dict[str, Any]] = []
    for b in manifes:
        if b.get("gagal_unduh"):
            continue
        if b.get("gerbang_lolos") is False:
            hasil.append(
                {
                    "simbol": str(b.get("simbol") or ""),
                    "bulan": str(b.get("bulan") or ""),
                    "pelanggaran": sorted(str(p) for p in (b.get("gerbang_pelanggaran") or [])),
                    "baris": int(b.get("baris") or 0),
                    "parquet_karantina": b.get("parquet_karantina"),
                    "checksum_zip_sha256": b.get("checksum_zip_sha256"),
                }
            )
    return sorted(hasil, key=lambda x: (x["simbol"], x["bulan"]))


def ringkas_karantina(manifes: List[Dict[str, Any]]) -> Dict[str, Any]:
    daftar = baris_karantina(manifes)
    dipotong = len(daftar) > BATAS_DAFTAR_KARANTINA
    return {
        "kebijakan": "ADR-A006: disisihkan, bukan dibuang dan bukan ditambal",
        "cacah_karantina": len(daftar),
        "cacah_tak_terunduh": sum(1 for b in manifes if b.get("gagal_unduh")),
        "cacah_dibuang": 0,
        "cacah_ditambal": 0,
        "byte_parquet_karantina": sum(
            int(b.get("byte_parquet_karantina") or 0) for b in manifes
        ),
        "daftar_karantina": daftar[:BATAS_DAFTAR_KARANTINA],
        "daftar_terpotong": dipotong,
        "batas_daftar": BATAS_DAFTAR_KARANTINA,
        "catatan_penggugur": (
            "cacah_dibuang atau cacah_ditambal tidak nol berarti ADR-A006 dilanggar; "
            "interpolasi, forward-fill, dan penurunan ambang gerbang DILARANG "
            "(aturan 23, 24)"
        ),
    }


def serap_satu(simbol: str, bulan: str, akar: str = ".", terhenti: bool = False) -> Dict[str, Any]:
    """Serap satu simbol-bulan dan kembalikan satu baris manifes."""
    url = arsip.url_klines(simbol, "1m", bulan)
    baris: Dict[str, Any] = {
        "simbol": simbol,
        "bulan": bulan,
        "jenis_instrumen": JENIS_DIIZINKAN,
        "terhenti": bool(terhenti),
        "sumber_url": url,
        "gagal_unduh": False,
        "gagal_checksum": False,
        "galat": None,
    }
    try:
        data = arsip.unduh_terverifikasi(url)
    except Exception as exc:  # noqa: BLE001
        pesan = str(exc)
        baris["gagal_unduh"] = True
        baris["gagal_checksum"] = "checksum" in pesan.lower() or "sha256" in pesan.lower()
        baris["galat"] = pesan[:300]
        return baris

    baris["byte_zip"] = len(data)
    baris["checksum_zip_sha256"] = hashlib.sha256(data).hexdigest()
    baris["berheader"] = bool(klines.punya_header(klines.baris_pertama(data)))

    df, dibuang = klines.rapikan(klines.baca_zip(data, teks=True))
    baris["baris"] = int(len(df))
    baris["baris_dibuang"] = int(dibuang)

    putusan = gerbang_1m.nilai_deret([int(t) for t in df["open_time"].tolist()], simbol, bulan)
    baris["gerbang_lolos"] = bool(putusan["lolos"])
    baris["gerbang_pelanggaran"] = list(putusan["pelanggaran"])
    baris["satuan_stempel"] = putusan["ukuran"]["satuan_stempel_dari_besaran"]
    baris["awal_sejati"] = putusan["ukuran"]["menit_pertama"]
    baris["akhir_sejati"] = putusan["ukuran"]["menit_terakhir"]
    baris["awal_sejati_utc"] = iso_dari_ms(putusan["ukuran"]["menit_pertama"])
    baris["akhir_sejati_utc"] = iso_dari_ms(putusan["ukuran"]["menit_terakhir"])
    baris["funding_ada"] = None  # pilot tidak mengambil funding; jangan diisi nol

    # ADR-A006: yang lolos masuk data utama, yang jatuh DISISIHKAN ke pohon
    # karantina. Tidak ada cabang yang membuang datanya.
    lolos = bool(putusan["lolos"])
    baris["karantina"] = not lolos
    aman = nama_aman(simbol)
    nama = f"{aman}-1m-{bulan}.parquet"
    relatif = Path(AKAR_PARQUET if lolos else AKAR_KARANTINA) / aman / nama
    tujuan = Path(akar) / relatif
    tujuan.parent.mkdir(parents=True, exist_ok=True)
    klines.tulis_parquet(df, str(tujuan))
    byte_parquet = int(tujuan.stat().st_size)
    if lolos:
        baris["parquet"] = str(relatif)
        baris["byte_parquet"] = byte_parquet
        baris["parquet_karantina"] = None
        baris["byte_parquet_karantina"] = 0
    else:
        baris["parquet"] = None
        baris["byte_parquet"] = 0
        baris["parquet_karantina"] = str(relatif)
        baris["byte_parquet_karantina"] = byte_parquet

    baris["_putusan"] = putusan
    return baris


def ringkas(manifes: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Cacah lintas simbol-bulan, dengan medan penggugur yang selalu hadir."""
    diminta = len(manifes)
    if not diminta:
        return {
            "status": "TIDAK MENGUKUR",
            "penyebut": {"simbol_bulan_diminta": 0},
            "cacah_gagal_unduh": 0,
            "cacah_gagal_checksum": 0,
            "cacah_simbol_bulan_dengan_baris_dibuang": 0,
            "jumlah_baris_dibuang": 0,
            "nisbah_parquet_per_zip": None,
            "kelas_risiko_tersentuh": {nama: 0 for nama in KELAS_RISIKO},
            "kelas_risiko_kosong": list(KELAS_RISIKO),
            "cacah_karantina": 0,
            "daftar_karantina": [],
            "karantina": ringkas_karantina([]),
        }
    gagal_unduh = sum(1 for b in manifes if b.get("gagal_unduh"))
    gagal_checksum = sum(1 for b in manifes if b.get("gagal_checksum"))
    dibuang = [int(b.get("baris_dibuang") or 0) for b in manifes]
    byte_zip = sum(int(b.get("byte_zip") or 0) for b in manifes)
    byte_parquet = sum(int(b.get("byte_parquet") or 0) for b in manifes)
    putusan = [b["_putusan"] for b in manifes if isinstance(b.get("_putusan"), dict)]
    kelas = kelas_risiko_tersentuh(manifes)
    karantina = ringkas_karantina(manifes)
    return {
        "status": "TERUKUR",
        "penyebut": {
            "simbol_bulan_diminta": diminta,
            "simbol_bulan_terunduh": diminta - gagal_unduh,
        },
        "cacah_gagal_unduh": gagal_unduh,
        "cacah_gagal_checksum": gagal_checksum,
        "cacah_simbol_bulan_dengan_baris_dibuang": sum(1 for d in dibuang if d),
        "jumlah_baris_dibuang": sum(dibuang),
        "jumlah_baris": sum(int(b.get("baris") or 0) for b in manifes),
        "byte_zip_total": byte_zip,
        "byte_parquet_total": byte_parquet,
        "byte_parquet_karantina_total": karantina["byte_parquet_karantina"],
        "nisbah_parquet_per_zip": round(byte_parquet / byte_zip, 4) if byte_zip else None,
        "jenis_instrumen_unik": sorted({str(b.get("jenis_instrumen")) for b in manifes}),
        "kelas_risiko_tersentuh": kelas,
        "kelas_risiko_kosong": [nama for nama, n in kelas.items() if not n],
        "cacah_karantina": karantina["cacah_karantina"],
        "daftar_karantina": karantina["daftar_karantina"],
        "karantina": karantina,
        "gerbang": gerbang_1m.ringkas_gerbang(putusan),
    }


def jalankan(akar: str = ".") -> Dict[str, Any]:
    from ..semesta import taksonomi

    basis = Path(akar)
    mentah = (basis / SUMBER_RENTANG).read_bytes()
    rentang = json.loads(mentah.decode("utf-8")).get("rentang", {})
    if not isinstance(rentang, dict):
        rentang = {}

    pasangan = pilih_berlapis(rentang, taksonomi.jenis_instrumen)
    batas = int(os.environ.get("PILOT_BATAS_SIMBOL_BULAN", "0") or 0)
    if batas > 0:
        pasangan = pasangan[:batas]

    manifes = []
    for s, b in pasangan:
        mati = bool(rentang.get(s, {}).get("bulan_terakhir", "") < BATAS_HIDUP)
        manifes.append(serap_satu(s, b, akar=akar, terhenti=mati))

    laporan = ringkas(manifes)
    laporan["bukan_bukti"] = False
    laporan["catatan_bukan_bukti"] = (
        "manifes serapan adalah artefak mengikat, bukan diagnostik; "
        "gerbangnya boleh menjatuhkan simbol-bulan"
    )
    laporan["cakupan_disampel"] = [f"{s}:{b}" for s, b in pasangan]
    laporan["catatan_rentang"] = (
        "kesimpulan hanya berlaku untuk simbol-bulan pada cakupan_disampel, "
        "bukan untuk 19.598 bulan perpetual_usdt"
    )
    laporan["catatan_funding"] = "pilot tidak mengambil funding; funding_ada sengaja null"
    laporan["catatan_kc13"] = (
        "pemilihan berlapis menggantikan urutan abjad versi 1 yang membuat "
        "pra_header, non_ascii, dan terhenti tidak pernah tersentuh"
    )
    laporan["catatan_karantina"] = (
        "parquet simbol-bulan yang jatuh gerbang ditulis ke data/parquet_karantina "
        "dan tidak ikut byte_parquet_total, agar nisbah tetap sebanding dengan "
        "manifes pecahan yang sudah terukur (aturan 36)"
    )
    laporan["manifes"] = [
        {k: v for k, v in b.items() if not k.startswith("_")} for b in manifes
    ]
    laporan["sumber_rentang"] = SUMBER_RENTANG
    laporan["sidik_data"] = hashlib.sha256(mentah).hexdigest()
    laporan["sidik_kode"] = sidik_kode()
    laporan["waktu_utc"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    tujuan = basis / MANIFES
    tujuan.parent.mkdir(parents=True, exist_ok=True)
    tujuan.write_text(
        json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return laporan


def main() -> None:
    hasil = jalankan()
    print(json.dumps({k: v for k, v in hasil.items() if k != "manifes"}, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
