"""Pemulihan aset rilis oleh proses yang TIDAK menulisnya.

Seluruh klaim persistensi sampai STATE v25 berasal dari runner yang menulis tar
itu, membacanya ulang dari cakramnya sendiri beberapa detik kemudian. Tiga tahap
belum pernah tersentuh sekalipun: unggahan `gh`, penyimpanan aset GitHub, dan
unduhan kembali. `kode_unggah: 0` hanya berarti perintah `gh` pulang tanpa galat.

## Mengapa TIDAK memakai `sha256sum -c SHA256SUMS`

Berkas sidik itu adalah aset rilis juga: diunggah oleh proses yang sama, dari
cakram yang sama, dalam perintah yang sama. Memeriksa tar rilis dengan sidik
rilis hanya membuktikan rilis konsisten dengan dirinya sendiri. Untuk karantina
ia bahkan tidak ada — `SHA256SUMS_KARANTINA` gagal terunggah pada run
`30396803601` (aturan 45).

Sumber kebenaran di sini adalah **`reports/manifes_pecahan_<i>.json` di git**:
`rilis.bagian[].sha256` ditulis sebelum unggahan lalu di-commit. Membandingkan
tar hasil unduhan terhadap sidik di riwayat repo adalah perbandingan
lintas-jalur yang sesungguhnya. Tag pun tidak diketik dari ingatan; ia disusun
dari `run_id` di `reports/pecahan_<i>_status.json`.

## Medan penggugur (aturan 24)

- `cacah_bagian_hilang` — aset yang tidak terunduh.
- `cacah_sha_tak_cocok` — byte berubah antara ditulis dan diunduh.
- `cacah_anggota_kurang` — anggota tar hasil unduhan lawan `cacah_berkas`.
- `cacah_anggota_tak_aman` — anggota berjalur mutlak atau `..`. Tar ini ditulis
  kode sendiri, tetapi ia melewati penyimpanan pihak lain sebelum kembali;
  membongkarnya tanpa memeriksa nama anggota berarti mempercayai persis hal yang
  sedang diuji.
- `selisih_baris_utama` / `selisih_baris_total` — baris yang dibaca pyarrow dari
  parquet hasil BONGKAR, lawan `jumlah_baris` di manifes.

`pulih_sah` sengaja HANYA mencakup keutuhan pengangkutan (empat medan pertama).
Kecocokan baris dilaporkan terpisah sebagai `baris_terverifikasi`, karena
pertanyaan "apakah `jumlah_baris` mencakup karantina" adalah pertanyaan
DEFINISI, bukan pertanyaan keutuhan; mencampurnya akan membuat satu angka
membatalkan kesimpulan tentang angka lain (aturan 16, 36).

## Cakram

Runner ±14 GB; pecahan terbesar 4,57 GB tar. Karena itu tiap bagian dibongkar,
dihitung, lalu bagian DAN hasil bongkarnya dihapus sebelum bagian berikutnya
dibuka. Puncak ≈ satu unduhan pecahan + satu bagian terbongkar.

Aturan yang ditegakkan: 7, 8, 9, 16, 21, 22, 24, 30, 33, 34, 36, 44, 45.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import tarfile
from pathlib import Path
from typing import Any, Dict, List, Optional

from . import rilis

VERSI = 1
TOTAL_PECAHAN = 8
AKAR_UNDUH = "data/unduh"
AKAR_PULIH = "data/pulih"


def nama_manifes(indeks: int) -> str:
    return f"reports/manifes_pecahan_{indeks}.json"


def nama_status_serapan(indeks: int) -> str:
    return f"reports/pecahan_{indeks}_status.json"


def nama_keluaran(indeks: int) -> str:
    return f"reports/pulihkan_pecahan_{indeks}.json"


def nama_tag(indeks: int, run_id: str) -> str:
    return f"serapan-pecahan-{indeks}-{run_id}"


def sidik_kode() -> str:
    """Aturan 22: modul ini beserta modul yang putusannya bergantung padanya."""
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(["pulihkan.py", "rilis.py"]):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def run_id_sumber(indeks: int, akar: str = ".") -> str:
    """run_id diambil dari berkas status di git, bukan dari ingatan agen."""
    jalur = Path(akar) / nama_status_serapan(indeks)
    isi = json.loads(jalur.read_text(encoding="utf-8"))
    return str(isi.get("run_id") or "")


def anggota_aman(nama: str) -> bool:
    """Tolak jalur mutlak dan komponen `..` sebelum membongkar."""
    teks = str(nama)
    if teks.startswith("/") or teks.startswith("\\"):
        return False
    p = Path(teks)
    if p.is_absolute():
        return False
    return ".." not in p.parts


def cacah_baris_parquet(jalur: Path) -> int:
    """Baca cacah baris dari kaki parquet; tidak memuat datanya."""
    import pyarrow.parquet as pq

    return int(pq.ParquetFile(str(jalur)).metadata.num_rows)


def periksa_bagian(
    jalur_tar: Path, sha_harap: str, tujuan: Path, hapus: bool = True
) -> Dict[str, Any]:
    """Satu bagian tar: cocokkan sidik, bongkar, hitung baris, lalu bersihkan."""
    hasil: Dict[str, Any] = {
        "nama": jalur_tar.name,
        "ada": jalur_tar.exists(),
        "sha256": None,
        "sha256_diharap": sha_harap,
        "sha_cocok": False,
        "byte": 0,
        "cacah_anggota": 0,
        "cacah_anggota_tak_aman": 0,
        "cacah_parquet_terbaca": 0,
        "cacah_baris": 0,
    }
    if not hasil["ada"]:
        return hasil

    hasil["byte"] = int(jalur_tar.stat().st_size)
    hasil["sha256"] = rilis.sha256_berkas(jalur_tar)
    hasil["sha_cocok"] = bool(hasil["sha256"] == sha_harap)

    tujuan.mkdir(parents=True, exist_ok=True)
    dibongkar: List[Path] = []
    with tarfile.open(jalur_tar, "r") as tar:
        for anggota in tar.getmembers():
            if not anggota.isfile():
                continue
            if not anggota_aman(anggota.name):
                hasil["cacah_anggota_tak_aman"] += 1
                continue
            tar.extract(anggota, path=str(tujuan))
            hasil["cacah_anggota"] += 1
            dibongkar.append(tujuan / anggota.name)

    for jalur in dibongkar:
        if jalur.suffix == ".parquet" and jalur.exists():
            hasil["cacah_baris"] += cacah_baris_parquet(jalur)
            hasil["cacah_parquet_terbaca"] += 1
        if hapus and jalur.exists():
            jalur.unlink()

    if hapus and jalur_tar.exists():
        jalur_tar.unlink()
    return hasil


def periksa_keluarga(
    laporan_kemas: Optional[Dict[str, Any]],
    dir_unduh: Path,
    tujuan: Path,
    hapus: bool = True,
) -> Optional[Dict[str, Any]]:
    """Seluruh bagian satu keluarga tar (utama atau karantina)."""
    if not laporan_kemas:
        return None
    bagian_harap = laporan_kemas.get("bagian") or []
    rincian = [
        periksa_bagian(
            dir_unduh / str(b["nama"]), str(b["sha256"]), tujuan, hapus=hapus
        )
        for b in bagian_harap
    ]
    anggota = sum(int(r["cacah_anggota"]) for r in rincian)
    diharap = int(laporan_kemas.get("cacah_berkas") or 0)
    return {
        "nama_dasar": laporan_kemas.get("nama_dasar"),
        "cacah_bagian_diharap": len(bagian_harap),
        "cacah_bagian_hilang": sum(1 for r in rincian if not r["ada"]),
        "nama_bagian_hilang": [r["nama"] for r in rincian if not r["ada"]][:20],
        "cacah_sha_cocok": sum(1 for r in rincian if r["sha_cocok"]),
        "cacah_sha_tak_cocok": sum(1 for r in rincian if r["ada"] and not r["sha_cocok"]),
        "nama_sha_tak_cocok": [
            r["nama"] for r in rincian if r["ada"] and not r["sha_cocok"]
        ][:20],
        "cacah_anggota_terbaca": anggota,
        "cacah_anggota_diharap": diharap,
        "cacah_anggota_kurang": diharap - anggota,
        "cacah_anggota_tak_aman": sum(int(r["cacah_anggota_tak_aman"]) for r in rincian),
        "cacah_parquet_terbaca": sum(int(r["cacah_parquet_terbaca"]) for r in rincian),
        "cacah_baris": sum(int(r["cacah_baris"]) for r in rincian),
        "byte_bagian_terunduh": sum(int(r["byte"]) for r in rincian),
        "bagian": rincian,
    }


def _utuh(ringkas: Optional[Dict[str, Any]]) -> bool:
    """Keluarga yang tidak ada (penyebut nol) tidak menggugurkan apa pun."""
    if ringkas is None:
        return True
    return (
        int(ringkas["cacah_bagian_hilang"]) == 0
        and int(ringkas["cacah_sha_tak_cocok"]) == 0
        and int(ringkas["cacah_anggota_kurang"]) == 0
        and int(ringkas["cacah_anggota_tak_aman"]) == 0
        and int(ringkas["cacah_bagian_diharap"]) > 0
    )


def jalankan(
    indeks: int,
    akar: str = ".",
    dir_unduh: str = AKAR_UNDUH,
    dir_pulih: str = AKAR_PULIH,
    hapus: bool = True,
) -> Dict[str, Any]:
    basis = Path(akar)
    mentah = (basis / nama_manifes(indeks)).read_bytes()
    manifes = json.loads(mentah.decode("utf-8"))

    utama = periksa_keluarga(
        manifes.get("rilis"), basis / dir_unduh, basis / dir_pulih, hapus=hapus
    )
    karantina = periksa_keluarga(
        manifes.get("rilis_karantina"), basis / dir_unduh, basis / dir_pulih, hapus=hapus
    )

    baris_utama = int((utama or {}).get("cacah_baris") or 0)
    baris_karantina = int((karantina or {}).get("cacah_baris") or 0)
    baris_total = baris_utama + baris_karantina
    baris_manifes = manifes.get("jumlah_baris")
    baris_manifes = int(baris_manifes) if isinstance(baris_manifes, int) else None

    selisih_utama = None if baris_manifes is None else baris_utama - baris_manifes
    selisih_total = None if baris_manifes is None else baris_total - baris_manifes
    if selisih_utama == 0:
        definisi = "jumlah_baris = baris parquet lolos gerbang saja"
    elif selisih_total == 0:
        definisi = "jumlah_baris = baris lolos + baris karantina"
    else:
        definisi = "tidak ada definisi yang cocok"

    pulih_sah = bool(utama is not None and _utuh(utama) and _utuh(karantina))

    laporan: Dict[str, Any] = {
        "bukan_bukti": False,
        "versi_pulihkan": VERSI,
        "indeks": indeks,
        "run_id_sumber": run_id_sumber(indeks, akar=akar),
        "utama": utama,
        "karantina": karantina,
        "jumlah_baris_manifes": baris_manifes,
        "baris_utama": baris_utama,
        "baris_karantina": baris_karantina,
        "baris_total": baris_total,
        "selisih_baris_utama": selisih_utama,
        "selisih_baris_total": selisih_total,
        "definisi_jumlah_baris": definisi,
        "baris_terverifikasi": bool(selisih_utama == 0 or selisih_total == 0),
        "pulih_sah": pulih_sah,
        "catatan_penggugur": (
            "pulih_sah HANYA mencakup keutuhan pengangkutan: bagian hilang, sha "
            "tak cocok, anggota kurang, anggota tak aman. Kecocokan baris "
            "dilaporkan terpisah karena ia pertanyaan definisi, bukan keutuhan "
            "(aturan 16, 36)"
        ),
        "catatan_sumber_sidik": (
            "sidik pembanding diambil dari manifes di git, BUKAN dari berkas "
            "SHA256SUMS di rilis; berkas itu diunggah proses yang sama dari "
            "cakram yang sama, jadi memakainya hanya membuktikan rilis "
            "konsisten dengan dirinya sendiri"
        ),
        "catatan_rentang": (
            f"berlaku untuk pecahan {indeks} dari {TOTAL_PECAHAN} saja, dan untuk "
            "satu kali unduhan pada satu waktu; ia tidak mengatakan apa pun "
            "tentang ketahanan aset dalam jangka panjang (aturan 20)"
        ),
    }
    laporan["sidik_manifes"] = hashlib.sha256(mentah).hexdigest()
    laporan["sidik_kode"] = sidik_kode()
    laporan["sidik_kode_manifes"] = manifes.get("sidik_kode")
    laporan["waktu_utc"] = dt.datetime.now(dt.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )

    tujuan = basis / nama_keluaran(indeks)
    tujuan.parent.mkdir(parents=True, exist_ok=True)
    tujuan.write_text(
        json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return laporan


def main() -> None:
    indeks = int(os.environ.get("PULIH_INDEKS", "0") or 0)
    hasil = jalankan(indeks)
    ringkas = {
        k: v
        for k, v in hasil.items()
        if k not in ("utama", "karantina")
    }
    for nama in ("utama", "karantina"):
        isi = hasil.get(nama)
        if isi:
            ringkas[nama] = {k: v for k, v in isi.items() if k != "bagian"}
    print(json.dumps(ringkas, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
