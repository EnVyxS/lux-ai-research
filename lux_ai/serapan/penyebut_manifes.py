"""penyebut_manifes.py - pembaca NILAI medan BERSARANG pada manifes pecahan.

VERSI 2. VERSI 1 melunasi UTANG UKUR 41 (penyebut.simbol_bulan_diminta dan
penyebut.simbol_bulan_terunduh terbaca lewat log runner), tetapi laporan
penuhnya 116.538 B dengan badan `pecahan` mendahului `ringkasan` secara
alfabetis, sehingga bagian yang paling dibutuhkan justru berisiko terpotong
saat dibaca alat. VERSI 2 menambah keluaran KEDUA yang ramping:
`reports/penyebut_manifes_ringkas.json`, berisi HANYA ringkasan lintas pecahan
(tanpa badan per-pecahan). Laporan penuh tetap ditulis dan tidak dikurangi.

SASARAN UTAMA (utang ukur 41, sudah terbaca pada VERSI 1):
  penyebut.simbol_bulan_diminta
  penyebut.simbol_bulan_terunduh
SASARAN VERSI 2 (menyentuh penghalang baris 6):
  gerbang.pelanggaran_per_klausa  -> NAMA klausa dan cacah pelanggarannya
  gerbang.simbol_bulan_dinilai / _lolos / _gagal / persen_lolos
  gerbang.baris_diperiksa / slot_diperiksa
  selisih_cacah_bulan.cacah_simbol_berselisih

BATAS YANG DITULIS DI MUKA (aturan 21, 24, 30):
- Modul ini MENYALIN nilai apa adanya. Ia TIDAK menghitung ulang isi manifes.
- Medan yang absen dilaporkan absen. ABSEN BUKAN NOL. Null BUKAN nol.
- Penjumlahan lintas pecahan hanya dilakukan bila KEDELAPAN nilai adalah
  bilangan bulat. Bila ada satu saja yang bukan, hasilnya null.
- DILARANG memakai angka `reports/peta_manifes.json` sebagai pengganti medan
  puncak manifes. Akibat bukan medan.
- DILARANG menulis "gerbang punya N klausa" dari cacah kunci saja; yang sah
  hanyalah NAMA klausa yang benar-benar terbaca di pelanggaran_per_klausa,
  dan itu pun adalah klausa yang DILAPORKAN, belum tentu seluruh klausa yang
  DIPERIKSA. Perbedaan itu wajib diuji terpisah, bukan disimpulkan di sini.
- Laporan ini TIDAK mengubah vonis ramalan mana pun yang sudah sah, termasuk
  R-324 (MELESET, final sejak jurnal 182 bagian 4).

Medan `manifes` dan `daftar_karantina` SENGAJA tidak dirambah: keduanya badan
data raksasa, bukan kunci atas.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import os
import sys

VERSI = 2
KELUARAN = "reports/penyebut_manifes.json"
KELUARAN_RINGKAS = "reports/penyebut_manifes_ringkas.json"
POLA_MANIFES = "reports/manifes_pecahan_{}.json"
TOTAL_PECAHAN = 8

# Pagar ukuran laporan.
KEDALAMAN = 4
BATAS_LARIK = 16
BATAS_KUNCI = 64
BATAS_TEKS = 240

MEDAN_BERSARANG = (
    "penyebut",
    "gerbang",
    "selisih_cacah_bulan",
    "pecahan",
    "mengemas",
    "rilis",
    "rilis_karantina",
    "karantina",
    "sumber_rentang",
    "kelas_risiko_tersentuh",
    "kelas_risiko_kosong",
)

MEDAN_SKALAR = (
    "versi_pecahan",
    "status",
    "jumlah_baris",
    "jumlah_baris_dibuang",
    "byte_parquet_total",
    "byte_parquet_karantina_total",
    "byte_zip_total",
    "cacah_gagal_unduh",
    "cacah_gagal_checksum",
    "cacah_simbol_bulan_dengan_baris_dibuang",
    "jenis_instrumen_unik",
    "nisbah_parquet_per_zip",
    "sidik_data",
    "sidik_kode",
    "waktu_utc",
)

MEDAN_DILARANG = ("manifes", "daftar_karantina")

SASARAN_UTANG_41 = (
    "penyebut.simbol_bulan_diminta",
    "penyebut.simbol_bulan_terunduh",
)

# Awalan daun yang wajib ikut dicetak ke log VERSI 2.
AWALAN_SOROT = ("penyebut.", "gerbang.", "selisih_cacah_bulan.")


def sidik_kode() -> str:
    try:
        with open(os.path.abspath(__file__), "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except OSError:
        return ""


def sekarang() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


def potong(teks: str) -> str:
    if len(teks) <= BATAS_TEKS:
        return teks
    return teks[:BATAS_TEKS] + "...[dipotong " + str(len(teks)) + " aksara]"


def skalar(nilai) -> bool:
    return nilai is None or isinstance(nilai, (bool, int, float, str))


def ratakan(nilai, awalan: str, keluar: dict, sisa: int) -> None:
    """Ratakan objek bersarang menjadi daun berjalur titik."""
    if skalar(nilai):
        keluar[awalan] = potong(nilai) if isinstance(nilai, str) else nilai
        return

    if isinstance(nilai, dict):
        keluar[awalan + ".__cacah_kunci"] = len(nilai)
        if sisa <= 0 or len(nilai) > BATAS_KUNCI:
            keluar[awalan + ".__kunci"] = sorted(str(k) for k in nilai)[:32]
            keluar[awalan + ".__dirambah"] = False
            return
        keluar[awalan + ".__dirambah"] = True
        for kunci in sorted(nilai, key=str):
            ratakan(nilai[kunci], awalan + "." + str(kunci), keluar, sisa - 1)
        return

    if isinstance(nilai, list):
        keluar[awalan + ".__cacah"] = len(nilai)
        semua_skalar = all(skalar(x) for x in nilai)
        if semua_skalar and len(nilai) <= BATAS_LARIK:
            keluar[awalan] = [
                potong(x) if isinstance(x, str) else x for x in nilai
            ]
        elif semua_skalar:
            keluar[awalan + ".__contoh"] = [
                potong(x) if isinstance(x, str) else x
                for x in nilai[:BATAS_LARIK]
            ]
        elif sisa > 0 and nilai and isinstance(nilai[0], dict):
            kunci = set()
            for x in nilai[:200]:
                if isinstance(x, dict):
                    kunci.update(str(k) for k in x)
            keluar[awalan + ".__kunci_anggota"] = sorted(kunci)[:32]
        return

    keluar[awalan] = "[jenis lain: " + type(nilai).__name__ + "]"


def baca_pecahan(indeks: int) -> dict:
    jalur = POLA_MANIFES.format(indeks)
    hasil = {
        "pecahan": indeks,
        "jalur": jalur,
        "ada": False,
        "byte": 0,
        "rusak": False,
        "sebab_rusak": None,
        "daun": {},
        "medan_absen": [],
    }

    if not os.path.exists(jalur):
        return hasil

    hasil["ada"] = True
    try:
        hasil["byte"] = os.path.getsize(jalur)
    except OSError:
        hasil["byte"] = 0

    try:
        with open(jalur, "r", encoding="utf-8") as f:
            dokumen = json.load(f)
    except Exception as galat:  # noqa: BLE001 - sebab rusak wajib tercatat
        hasil["rusak"] = True
        hasil["sebab_rusak"] = potong(repr(galat))
        return hasil

    if not isinstance(dokumen, dict):
        hasil["rusak"] = True
        hasil["sebab_rusak"] = "puncak dokumen bukan pemetaan"
        return hasil

    daun: dict = {}
    absen: list = []

    for medan in MEDAN_SKALAR:
        if medan in dokumen:
            nilai = dokumen[medan]
            daun[medan] = potong(nilai) if isinstance(nilai, str) else nilai
        else:
            absen.append(medan)

    for medan in MEDAN_BERSARANG:
        if medan not in dokumen:
            absen.append(medan)
            continue
        ratakan(dokumen[medan], medan, daun, KEDALAMAN)

    for medan in MEDAN_DILARANG:
        daun["__ada_" + medan] = medan in dokumen

    hasil["daun"] = daun
    hasil["medan_absen"] = absen
    return hasil


def rangkum(pecahan: list) -> dict:
    kunci = set()
    for satu in pecahan:
        kunci.update(satu["daun"])

    ringkas: dict = {}
    for k in sorted(kunci):
        deret = [satu["daun"].get(k, None) for satu in pecahan]
        absen = [
            satu["pecahan"] for satu in pecahan if k not in satu["daun"]
        ]
        catatan = {"nilai": deret}
        if absen:
            catatan["pecahan_absen"] = absen

        bilangan = [
            x for x in deret if isinstance(x, int) and not isinstance(x, bool)
        ]
        if len(bilangan) == len(deret) and deret:
            catatan["jumlah"] = sum(bilangan)
            catatan["unik"] = sorted(set(bilangan))
            catatan["seragam"] = len(set(bilangan)) == 1
        elif all(skalar(x) for x in deret):
            catatan["unik"] = sorted({repr(x) for x in deret})
            catatan["seragam"] = len({repr(x) for x in deret}) == 1
            catatan["jumlah"] = None
        ringkas[k] = catatan

    return ringkas


def jalankan() -> dict:
    pecahan = [baca_pecahan(i) for i in range(TOTAL_PECAHAN)]
    ringkas = rangkum(pecahan)

    sasaran = {}
    for jalur in SASARAN_UTANG_41:
        if jalur in ringkas:
            sasaran[jalur] = ringkas[jalur]
        else:
            sasaran[jalur] = {
                "nilai": None,
                "terbaca": False,
                "catatan": (
                    "medan tidak muncul sebagai daun skalar; periksa "
                    "penyebut.__kunci dan penyebut.__dirambah"
                ),
            }

    laporan = {
        "bukan_bukti": False,
        "versi_penyebut_manifes": VERSI,
        "waktu_utc": sekarang(),
        "sidik_kode": sidik_kode(),
        "total_pecahan_diminta": TOTAL_PECAHAN,
        "cacah_pecahan_dibaca": sum(1 for p in pecahan if p["ada"]),
        "pecahan_hilang": [p["pecahan"] for p in pecahan if not p["ada"]],
        "pecahan_rusak": [p["pecahan"] for p in pecahan if p["rusak"]],
        "byte_manifes_total": sum(p["byte"] for p in pecahan),
        "medan_bersarang_dirambah": list(MEDAN_BERSARANG),
        "medan_dilarang_dirambah": list(MEDAN_DILARANG),
        "sasaran_utang_41": sasaran,
        "ringkasan": ringkas,
        "pecahan": pecahan,
        "catatan_batas": (
            "nilai disalin apa adanya; modul ini tidak menghitung ulang isi "
            "manifes dan tidak menambal medan absen. Absen BUKAN nol."
        ),
        "catatan_penggugur": (
            "pecahan_hilang atau pecahan_rusak tidak kosong berarti laporan "
            "ini TIDAK cukup untuk memutuskan apa pun (aturan 24)."
        ),
        "catatan_vonis": (
            "laporan ini TIDAK mengubah vonis R-324; MELESET sudah sah dan "
            "final atas butir 1 dan butir 3 sejak jurnal 182 bagian 4."
        ),
        "catatan_penyebut": (
            "simbol_bulan_diminta dan simbol_bulan_terunduh adalah penyebut "
            "UNDUHAN per pecahan, BUKAN penyebut semesta 787 maupun 937. "
            "Menyamakannya tanpa uji adalah mengarang."
        ),
        "catatan_gerbang": (
            "nama klausa yang muncul di pelanggaran_per_klausa adalah klausa "
            "yang DILAPORKAN, belum tentu seluruh klausa yang DIPERIKSA. "
            "DILARANG menyimpulkan cacah klausa gerbang dari sini saja."
        ),
    }
    return laporan


def ringkaskan(laporan: dict) -> dict:
    """Salinan laporan tanpa badan per-pecahan, supaya terbaca utuh oleh alat."""
    kurus = {k: v for k, v in laporan.items() if k != "pecahan"}
    kurus["catatan_ringkas"] = (
        "berkas ini adalah laporan yang SAMA tanpa badan per-pecahan; "
        "badan penuh ada di " + KELUARAN + ". Tidak ada nilai yang diubah."
    )
    kurus["jalur_penuh"] = KELUARAN
    kurus["cacah_daun_ringkasan"] = len(laporan.get("ringkasan", {}))
    return kurus


def main() -> int:
    laporan = jalankan()
    os.makedirs(os.path.dirname(KELUARAN), exist_ok=True)
    with open(KELUARAN, "w", encoding="utf-8") as f:
        json.dump(laporan, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")

    with open(KELUARAN_RINGKAS, "w", encoding="utf-8") as f:
        json.dump(
            ringkaskan(laporan), f, ensure_ascii=False, indent=2, sort_keys=True
        )
        f.write("\n")

    print("keluaran:", KELUARAN, os.path.getsize(KELUARAN), "B")
    print("ringkas:", KELUARAN_RINGKAS, os.path.getsize(KELUARAN_RINGKAS), "B")
    print("pecahan dibaca:", laporan["cacah_pecahan_dibaca"])
    print("hilang:", laporan["pecahan_hilang"], "rusak:", laporan["pecahan_rusak"])
    for jalur, catatan in sorted(laporan["ringkasan"].items()):
        if jalur.startswith(AWALAN_SOROT):
            print(jalur, "=>", json.dumps(catatan, ensure_ascii=False)[:400])
    return 0


if __name__ == "__main__":
    sys.exit(main())
