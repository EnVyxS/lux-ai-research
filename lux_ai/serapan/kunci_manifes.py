"""Pembaca NILAI medan penentu di kunci atas manifes pecahan.

Mengapa modul ini ada. `reports/peta_manifes.json` melaporkan NAMA kunci atas
kedelapan manifes pecahan, bukan NILAINYA. Empat medan penentu -
`versi_pecahan`, `verifikasi_rilis`, `cacah_parquet_tak_terkemas`,
`cacah_karantina_tak_terkemas` - karena itu tetap tak terbaca, dan selama ia tak
terbaca, klaim "manifes terverifikasi" DILARANG dan adjudikasi ikut terlarang
(blokir ketujuh).

Dua jalan pembacaan langsung sudah dicoba dan buntu, keduanya terukur:

1. Alat GitHub menolak `reports/manifes_pecahan_0.json` dengan sebab ukuran
   (2.530.465 byte) - penolakan berbatas, bukan galat.
2. Pengambilan lewat `raw.githubusercontent.com` menjawab "Content not
   available".

Jalan ketiga adalah modul ini: runner membaca kedelapan manifes dari cakram -
berkas itu ADA di git - lalu menulis NILAI skalarnya ke laporan kecil yang muat
dibaca alat.

## Batas kejujuran yang ditegakkan modul ini

- Ia **tidak menghitung ulang apa pun**. Ia menyalin nilai apa adanya. Bila
  sebuah medan tidak ada, ia menulis `null` DAN mencatat namanya di
  `medan_absen`, sebab "absen" dan "bernilai null" adalah dua hal berbeda
  (aturan 24).
- Ia **tidak menyimpulkan versi** dari akibat. `dikemas_karantina` yang terisi
  BUKAN `versi_pecahan`. Hanya medan yang benar-benar terbaca yang dilaporkan.
- `verifikasi_rilis` dan `verifikasi_rilis_karantina` adalah objek. Modul ini
  menyalin sub-medan skalarnya saja dan MEMOTONG daftar nama, supaya laporan
  tetap kecil. Arti `sah` didefinisikan di `rilis.verifikasi()`: ada bagian,
  nol sha tak cocok, nol bagian hilang, cacah anggota terbaca sama dengan
  cacah berkas, nol bagian melebihi batas, nol bagian taksiran terlampaui.
- `bukan_bukti: false`. Laporan ini MENGIKAT: ia salinan langsung dari manifes
  yang sama yang dipakai serapan, bukan diagnostik turunan.

Medan penggugur (aturan 24): `cacah_manifes_hilang`, `cacah_manifes_rusak`, dan
`medan_absen`. Bila salah satu tidak kosong, laporan ini TIDAK boleh dipakai
untuk memutuskan blokir ketujuh.

Aturan yang ditegakkan: 7, 16, 20, 21, 22, 24, 30, 32, 36, 37, 46.
"""

from __future__ import annotations

import datetime
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

VERSI = 1
TOTAL_PECAHAN = 8
POLA_MANIFES = "reports/manifes_pecahan_{i}.json"
KELUARAN = "reports/kunci_manifes.json"
BERKAS_DICAP = ("kunci_manifes.py",)
BATAS_DAFTAR = 20

# Empat medan penentu blokir ketujuh, ditulis tersurat supaya tidak bergeser.
MEDAN_PENENTU = (
    "versi_pecahan",
    "verifikasi_rilis",
    "cacah_parquet_tak_terkemas",
    "cacah_karantina_tak_terkemas",
)

# Medan pendamping: bukan penentu, tetapi menerangkan keempatnya.
MEDAN_PENDAMPING = (
    "verifikasi_rilis_karantina",
    "karantina_dipersistenkan",
    "parquet_dipersistenkan",
    "selisih_cacah_bulan",
    "nisbah_parquet_per_zip",
    "cacah_entri",
    "sidik_kode",
    "pecahan",
    "total_pecahan",
)


def sidik_kode() -> str:
    """sha256 gabungan berkas sumber modul ini (aturan 32)."""
    h = hashlib.sha256()
    akar = Path(__file__).resolve().parent
    for nama in BERKAS_DICAP:
        jalur = akar / nama
        h.update(nama.encode("utf-8"))
        h.update(jalur.read_bytes() if jalur.exists() else b"")
    return h.hexdigest()


def ringkas_verifikasi(nilai: Any) -> Any:
    """Salin sub-medan skalar objek verifikasi; potong daftar namanya."""
    if not isinstance(nilai, dict):
        return nilai
    keluar: Dict[str, Any] = {}
    for k, v in nilai.items():
        if isinstance(v, list):
            keluar[k + "__cacah"] = len(v)
            keluar[k] = v[:BATAS_DAFTAR]
        elif isinstance(v, dict):
            keluar[k + "__kunci"] = sorted(v.keys())[:BATAS_DAFTAR]
        else:
            keluar[k] = v
    return keluar


def baca_satu(akar: Path, i: int) -> Dict[str, Any]:
    """Baca satu manifes pecahan; kembalikan NILAI medan yang diminta."""
    jalur = akar / POLA_MANIFES.format(i=i)
    hasil: Dict[str, Any] = {
        "pecahan": i,
        "jalur": str(POLA_MANIFES.format(i=i)),
        "ada": jalur.exists(),
        "byte": int(jalur.stat().st_size) if jalur.exists() else 0,
        "rusak": False,
        "sebab_rusak": None,
        "medan_absen": [],
        "nilai": {},
        "kunci_atas": [],
    }
    if not jalur.exists():
        return hasil
    try:
        with open(jalur, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:  # noqa: BLE001 - sebab wajib tercatat, bukan bisu
        hasil["rusak"] = True
        hasil["sebab_rusak"] = f"{type(e).__name__}: {e}"[:300]
        return hasil
    if not isinstance(data, dict):
        hasil["rusak"] = True
        hasil["sebab_rusak"] = f"puncak bukan objek melainkan {type(data).__name__}"
        return hasil

    hasil["kunci_atas"] = sorted(data.keys())
    for medan in MEDAN_PENENTU + MEDAN_PENDAMPING:
        if medan not in data:
            hasil["medan_absen"].append(medan)
            hasil["nilai"][medan] = None
            continue
        nilai = data[medan]
        if medan.startswith("verifikasi_rilis"):
            nilai = ringkas_verifikasi(nilai)
        elif isinstance(nilai, list):
            nilai = {"__cacah": len(nilai)}
        elif isinstance(nilai, dict):
            nilai = {"__kunci": sorted(nilai.keys())[:BATAS_DAFTAR]}
        hasil["nilai"][medan] = nilai
    return hasil


def himpun(pecahan: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Ringkas lintas pecahan TANPA menghitung ulang isi manifes."""

    def kumpul(medan: str) -> List[Any]:
        return [p["nilai"].get(medan) for p in pecahan if not p["rusak"] and p["ada"]]

    versi = kumpul("versi_pecahan")
    tak_terkemas_parquet = kumpul("cacah_parquet_tak_terkemas")
    tak_terkemas_karantina = kumpul("cacah_karantina_tak_terkemas")

    def jumlah_aman(nilai: List[Any]) -> Optional[int]:
        angka = [v for v in nilai if isinstance(v, int) and not isinstance(v, bool)]
        if len(angka) != len(nilai) or not nilai:
            return None
        return sum(angka)

    sah_rilis = []
    for p in pecahan:
        v = p["nilai"].get("verifikasi_rilis")
        sah_rilis.append(v.get("sah") if isinstance(v, dict) else None)
    sah_karantina = []
    for p in pecahan:
        v = p["nilai"].get("verifikasi_rilis_karantina")
        sah_karantina.append(v.get("sah") if isinstance(v, dict) else None)

    return {
        "versi_pecahan_nilai": versi,
        "versi_pecahan_unik": sorted({str(v) for v in versi}),
        "versi_pecahan_seragam": len({str(v) for v in versi}) == 1 and bool(versi),
        "verifikasi_rilis_sah": sah_rilis,
        "verifikasi_rilis_sah_semua": bool(sah_rilis) and all(v is True for v in sah_rilis),
        "verifikasi_rilis_karantina_sah": sah_karantina,
        "cacah_parquet_tak_terkemas_nilai": tak_terkemas_parquet,
        "cacah_parquet_tak_terkemas_jumlah": jumlah_aman(tak_terkemas_parquet),
        "cacah_karantina_tak_terkemas_nilai": tak_terkemas_karantina,
        "cacah_karantina_tak_terkemas_jumlah": jumlah_aman(tak_terkemas_karantina),
        "parquet_dipersistenkan_nilai": kumpul("parquet_dipersistenkan"),
        "karantina_dipersistenkan_nilai": kumpul("karantina_dipersistenkan"),
        "selisih_cacah_bulan_nilai": kumpul("selisih_cacah_bulan"),
        "cacah_entri_nilai": kumpul("cacah_entri"),
        "sidik_kode_manifes_unik": sorted({str(v) for v in kumpul("sidik_kode")}),
    }


def jalankan(akar: str = ".") -> Dict[str, Any]:
    dasar = Path(akar)
    pecahan = [baca_satu(dasar, i) for i in range(TOTAL_PECAHAN)]
    hilang = [p["pecahan"] for p in pecahan if not p["ada"]]
    rusak = [p["pecahan"] for p in pecahan if p["rusak"]]
    absen: Dict[str, List[int]] = {}
    for p in pecahan:
        for medan in p["medan_absen"]:
            absen.setdefault(medan, []).append(p["pecahan"])

    laporan = {
        "versi_kunci_manifes": VERSI,
        "sidik_kode": sidik_kode(),
        "waktu_utc": datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        "bukan_bukti": False,
        "total_pecahan_diminta": TOTAL_PECAHAN,
        "cacah_manifes_dibaca": sum(1 for p in pecahan if p["ada"] and not p["rusak"]),
        "cacah_manifes_hilang": len(hilang),
        "pecahan_hilang": hilang,
        "cacah_manifes_rusak": len(rusak),
        "pecahan_rusak": rusak,
        "medan_absen": absen,
        "byte_manifes_total": sum(int(p["byte"]) for p in pecahan),
        "medan_penentu": list(MEDAN_PENENTU),
        "ringkasan": himpun(pecahan),
        "pecahan": pecahan,
        "catatan_penggugur": (
            "cacah_manifes_hilang > 0, cacah_manifes_rusak > 0, atau medan_absen "
            "tidak kosong berarti laporan ini TIDAK cukup untuk memutuskan blokir "
            "ketujuh (aturan 24)"
        ),
        "catatan_arti_sah": (
            "verifikasi_rilis.sah didefinisikan di rilis.verifikasi(): ada bagian, "
            "nol sha tak cocok, nol bagian hilang, cacah_anggota_terbaca sama "
            "dengan cacah_berkas, cacah_bagian_melebihi_batas nol, dan "
            "cacah_bagian_taksiran_terlampaui nol"
        ),
        "catatan_batas": (
            "modul ini menyalin nilai apa adanya dan TIDAK menghitung ulang isi "
            "manifes; akibat seperti dikemas_karantina BUKAN pengganti medan "
            "versi_pecahan"
        ),
    }
    return laporan


def main() -> int:
    laporan = jalankan(".")
    Path("reports").mkdir(parents=True, exist_ok=True)
    with open(KELUARAN, "w", encoding="utf-8") as f:
        json.dump(laporan, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    r = laporan["ringkasan"]
    print("kunci_manifes VERSI", VERSI)
    print("dibaca:", laporan["cacah_manifes_dibaca"], "hilang:", laporan["cacah_manifes_hilang"], "rusak:", laporan["cacah_manifes_rusak"])
    print("versi_pecahan:", r["versi_pecahan_nilai"])
    print("verifikasi_rilis.sah:", r["verifikasi_rilis_sah"])
    print("verifikasi_rilis_karantina.sah:", r["verifikasi_rilis_karantina_sah"])
    print("cacah_parquet_tak_terkemas:", r["cacah_parquet_tak_terkemas_nilai"])
    print("cacah_karantina_tak_terkemas:", r["cacah_karantina_tak_terkemas_nilai"])
    print("medan_absen:", laporan["medan_absen"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
