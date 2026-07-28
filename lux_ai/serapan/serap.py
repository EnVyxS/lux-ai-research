"""Pilot serapan: satu jalur penuh dari arsip ke parquet, dengan manifes.

Menempuh seluruh rantai yang nanti dipakai serapan penuh (utang 24):
unduh terverifikasi checksum -> baca zip -> rapikan -> gerbang integritas 1m
(ADR-A004) -> tulis parquet -> catat manifes per simbol-bulan.

Dijalankan lebih dulu atas SEDIKIT simbol-bulan. Serapan penuh yang gagal di
jam keempat jauh lebih mahal daripada pilot yang gagal di menit kedua.

Cakupan instrumen mengikuti ADR-A005 §1: hanya `perpetual_usdt`.

Aturan yang ditegakkan di sini:
- 16: tiap medan dinamai menurut apa yang benar-benar diukurnya.
- 18: cacah yang benar-benar diperiksa selalu dilaporkan.
- 20: laporan menyebut simbol-bulan yang benar-benar disampel.
- 24: `baris_dibuang` dan `cacah_simbol_bulan_dengan_baris_dibuang` dilaporkan
  walau nol; keduanya dapat menggugurkan premis "arsip 1m utuh".
- 30: penyebut eksplisit; penyebut nol berarti `TIDAK MENGUKUR`.
- 32: nama simbol non-ASCII diamankan untuk sistem berkas tanpa dibuang.
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

# Cakupan pilot dipatok tertulis SEBELUM run (aturan 25).
PILOT_CACAH_SIMBOL = 3
PILOT_BULAN_PER_SIMBOL = 2
JENIS_DIIZINKAN = "perpetual_usdt"

AMAN = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._-")


def sidik_kode() -> str:
    """Aturan 22: seluruh berkas yang ikut menentukan isi manifes."""
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(["serap.py", "arsip.py", "klines.py", "gerbang_1m.py", "resample.py"]):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def nama_aman(simbol: str) -> str:
    """Nama berkas yang aman tanpa MEMBUANG simbol non-ASCII (aturan 32).

    币安人生USDT tidak boleh hilang diam-diam seperti pada KC-9; ia diubah
    menjadi bentuk yang dapat dipulihkan.
    """
    keluar = []
    for ch in simbol:
        keluar.append(ch if ch in AMAN else f"u{ord(ch):04X}")
    return "".join(keluar)


def iso_dari_ms(nilai) -> str:
    if nilai is None:
        return ""
    detik = int(nilai) / 1000
    return dt.datetime.fromtimestamp(detik, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def pilih_pilot(
    rentang: Dict[str, Any],
    jenis_dari,
    cacah_simbol: int = PILOT_CACAH_SIMBOL,
    bulan_per_simbol: int = PILOT_BULAN_PER_SIMBOL,
) -> List[Tuple[str, str]]:
    """Pilih simbol-bulan pilot secara DETERMINISTIK.

    Deterministik supaya pilot bisa diulang persis; urut abjad supaya pilihannya
    tidak bisa saya sesuaikan setelah melihat hasil (aturan 25).
    Tiap simbol menyumbang bulan PERTAMA-nya (paling berisiko, format lama tanpa
    header) dan bulan TENGAH masa hidupnya (kendali).
    """
    layak = []
    for simbol in sorted(rentang):
        isi = rentang[simbol]
        if not isinstance(isi, dict):
            continue
        if jenis_dari(simbol) != JENIS_DIIZINKAN:
            continue
        awal = isi.get("bulan_pertama")
        akhir = isi.get("bulan_terakhir")
        if not isinstance(awal, str) or not isinstance(akhir, str):
            continue
        layak.append((simbol, awal, akhir))
        if len(layak) >= cacah_simbol:
            break

    pasangan: List[Tuple[str, str]] = []
    for simbol, awal, akhir in layak:
        bulan = [awal]
        if bulan_per_simbol > 1 and akhir != awal:
            ta, ba = (int(x) for x in awal.split("-"))
            tb, bb = (int(x) for x in akhir.split("-"))
            total = ((ta * 12 + ba - 1) + (tb * 12 + bb - 1)) // 2
            tengah = f"{total // 12:04d}-{total % 12 + 1:02d}"
            if tengah not in bulan:
                bulan.append(tengah)
        for b in bulan[:bulan_per_simbol]:
            pasangan.append((simbol, b))
    return pasangan


def serap_satu(simbol: str, bulan: str, akar: str = ".") -> Dict[str, Any]:
    """Serap satu simbol-bulan dan kembalikan satu baris manifes."""
    url = arsip.url_klines(simbol, "1m", bulan)
    baris: Dict[str, Any] = {
        "simbol": simbol,
        "bulan": bulan,
        "jenis_instrumen": JENIS_DIIZINKAN,
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

    cap = [int(t) for t in df["open_time"].tolist()]
    putusan = gerbang_1m.nilai_deret(cap, simbol, bulan)
    baris["gerbang_lolos"] = bool(putusan["lolos"])
    baris["gerbang_pelanggaran"] = list(putusan["pelanggaran"])
    baris["satuan_stempel"] = putusan["ukuran"]["satuan_stempel_dari_besaran"]
    baris["awal_sejati"] = putusan["ukuran"]["menit_pertama"]
    baris["akhir_sejati"] = putusan["ukuran"]["menit_terakhir"]
    baris["awal_sejati_utc"] = iso_dari_ms(putusan["ukuran"]["menit_pertama"])
    baris["akhir_sejati_utc"] = iso_dari_ms(putusan["ukuran"]["menit_terakhir"])
    # Funding TIDAK diambil pada pilot. Ditulis apa adanya, bukan diisi nol.
    baris["funding_ada"] = None

    if putusan["lolos"]:
        nama = f"{nama_aman(simbol)}-1m-{bulan}.parquet"
        tujuan = Path(akar) / AKAR_PARQUET / nama_aman(simbol) / nama
        tujuan.parent.mkdir(parents=True, exist_ok=True)
        klines.tulis_parquet(df, str(tujuan))
        baris["parquet"] = str(Path(AKAR_PARQUET) / nama_aman(simbol) / nama)
        baris["byte_parquet"] = int(tujuan.stat().st_size)
    else:
        baris["parquet"] = None
        baris["byte_parquet"] = 0

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
        }
    gagal_unduh = sum(1 for b in manifes if b.get("gagal_unduh"))
    gagal_checksum = sum(1 for b in manifes if b.get("gagal_checksum"))
    dibuang = [int(b.get("baris_dibuang") or 0) for b in manifes]
    byte_zip = sum(int(b.get("byte_zip") or 0) for b in manifes)
    byte_parquet = sum(int(b.get("byte_parquet") or 0) for b in manifes)
    putusan = [b["_putusan"] for b in manifes if isinstance(b.get("_putusan"), dict)]
    jenis = sorted({str(b.get("jenis_instrumen")) for b in manifes})
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
        "nisbah_parquet_per_zip": round(byte_parquet / byte_zip, 4) if byte_zip else None,
        "jenis_instrumen_unik": jenis,
        "gerbang": gerbang_1m.ringkas_gerbang(putusan),
    }


def jalankan(akar: str = ".") -> Dict[str, Any]:
    from ..semesta import taksonomi

    basis = Path(akar)
    mentah = (basis / SUMBER_RENTANG).read_bytes()
    rentang = json.loads(mentah.decode("utf-8")).get("rentang", {})
    if not isinstance(rentang, dict):
        rentang = {}

    batas = int(os.environ.get("PILOT_CACAH_SIMBOL", PILOT_CACAH_SIMBOL))
    pasangan = pilih_pilot(rentang, taksonomi.jenis_instrumen, cacah_simbol=batas)

    manifes = [serap_satu(s, b, akar=akar) for s, b in pasangan]
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
    ringkasan = {k: v for k, v in hasil.items() if k != "manifes"}
    print(json.dumps(ringkasan, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
