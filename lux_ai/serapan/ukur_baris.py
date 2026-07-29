"""Cacah baris berkas kode yang benar-benar DIHITUNG, bukan ditaksir.

Alasan modul ini ada: R-175 dan R-179 sudah menunggu dua jurnal karena satu-
satunya angka yang saya punya adalah UKURAN BYTE. Membagi byte dengan panjang
baris rata-rata adalah taksiran, dan menutup ramalan dengan taksiran melanggar
aturan 21. Modul ini menghitung, lalu menerbitkan hasilnya sebagai artefak yang
di-commit.

DEFINISI (aturan 16 dan 47). `cacah_baris` memakai definisi yang PERSIS SAMA
dengan pagar 800 baris di `tests/test_kontinuitas.py`, yaitu
`len(teks.splitlines())`. Pita R-175 (500..680) dan R-179 (640..700) mengacu ke
definisi itu, sebab pita-pita itu lahir dari pagar yang sama. Definisi lain ikut
diterbitkan supaya perbedaannya tidak pernah menjadi perdebatan diam-diam:

- `cacah_baris` — `len(splitlines())`; INI yang mengadjudikasi R-175 dan R-179.
- `cacah_newline` — cacah karakter "\\n". Berbeda satu dari `cacah_baris` bila
  berkas tidak berakhir dengan baris baru.
- `cacah_baris_kosong`, `cacah_baris_komentar`, `cacah_baris_kode` — pilahan
  kasar; komentar dihitung dari baris yang setelah dipangkas dimulai dengan "#".
  Docstring TIDAK dihitung sebagai komentar, ia terhitung kode.

PRAREGISTRASI (ditulis sebelum run, aturan kebiasaan):

- **R-197** — CI melaporkan **244 butir** dan **kode 0**. Satuan: BUTIR. Basis
  241 butir terverifikasi pada run 30416845496 (commit 387037a9), ditambah tepat
  tiga fungsi uji baru di `tests/test_ukur_baris.py`.

R-175 dan R-179 TIDAK ditulis ulang di sini dan pitanya TIDAK disetel ulang;
keduanya diadjudikasi apa adanya oleh angka yang terbit.

Penggugur (aturan 24): `cacah_berkas_hilang` != 0 berarti daftar yang diukur
tidak lengkap, sehingga seluruh cacah di laporan ini batal dipakai untuk menutup
ramalan.

---

## V2 (29 Juli 2026) — amandemen, bukan penghapusan (aturan 29)

Teks V1 di atas dibiarkan utuh, termasuk praregistrasi R-197 yang sudah
diadjudikasi TEPAT. Yang berubah pada V2 hanya SATU hal: daftar `BERKAS_DIUKUR`
bertambah dua nama, `lux_ai/serapan/kehidupan.py` dan `lux_ai/serapan/ukur_baris.py`
sendiri. Mekanika pengukuran, definisi `cacah_baris`, pagar 800, dan medan
penggugur TIDAK disentuh.

Alasan V2 dijalankan sekarang: `pulihkan.py` sudah naik ke V2 dan cacah barisnya
BELUM PERNAH diukur. Angka 318 yang tercatat di STATE adalah angka `pulihkan.py`
V1, dan STATE v28 sudah menandainya kedaluwarsa parsial. Menaksirnya dari 14.839
byte adalah persis kesalahan yang menjatuhkan R-175 dan R-179; karena itu ia
dihitung ulang, bukan ditaksir.

PRAREGISTRASI V2 (ditulis SEBELUM run ini):

- **R-202** — `cacah_baris` `lux_ai/serapan/pulihkan.py` berada dalam pita
  **340..420**. Satuan: BARIS menurut `len(splitlines())`. Penyebut tidak berlaku
  (ini pengukuran tunggal, bukan bagian). Pita dipakai karena satu-satunya
  petunjuk yang saya punya adalah ukuran byte, dan byte BUKAN baris; pita ini
  sengaja lebar supaya kegagalannya bermakna. Penggugur: `cacah_berkas_hilang`
  != 0 → TIDAK TERADJUDIKASI.
- **R-203** — `cacah_baris` `lux_ai/serapan/kehidupan.py` berada dalam pita
  **300..400** BARIS, dan `cacah_berkas_melebihi_pagar` = **0** atas kesepuluh
  berkas. Saya menulis berkas itu sendiri dan tetap tidak tahu cacah barisnya;
  ini ramalan, bukan pengetahuan.
- **R-204** — CI melaporkan **269 butir** dan **kode 0**. Satuan: BUTIR. Basis
  269 terverifikasi pada run 30418471386 (commit d4a2f60a); V2 tidak menambah
  satu pun fungsi uji, jadi angkanya harus DIAM. Penggugur: bila cacahnya
  bergerak tanpa uji baru, ada uji yang hilang atau gagal terkumpul dan itu
  MELESET, bukan kebetulan.

---

## V3 (29 Juli 2026) — dua berkas baru masuk daftar (aturan 29)

Seluruh teks V1 dan V2 di atas dibiarkan utuh, termasuk R-203 yang diadjudikasi
MELESET (kehidupan.py ternyata 417 baris, di luar pita 300..400). Yang berubah
pada V3 tetap hanya SATU hal: `BERKAS_DIUKUR` bertambah
`lux_ai/serapan/kehidupan_arsip.py` dan `lux_ai/serapan/silang_funding.py`.
Mekanika, definisi `cacah_baris`, pagar 800, dan medan penggugur TIDAK disentuh.

Alasan: kedua berkas itu sudah menerbitkan angka yang dipakai STATE (kehidupan
semesta dan silang funding), namun cacah barisnya belum pernah dihitung, sehingga
pagar 800 belum pernah benar-benar diuji atas keduanya. Menaksir dari byte adalah
kesalahan yang sudah tiga kali menjatuhkan ramalan saya (R-175, R-179, R-203).

Sebelum berkas ini diubah, `tests/test_ukur_baris.py` dibaca utuh: tidak ada uji
yang mengunci PANJANG `BERKAS_DIUKUR`; satu-satunya kewajiban adalah setiap nama
yang didaftar harus benar-benar ada di repo (`cacah_berkas_hilang` == 0). Kedua
nama baru sudah ada di `main`. Karena itu cacah butir uji TIDAK berubah.

PRAREGISTRASI V3 (ditulis SEBELUM run ini):

- **R-213** — `cacah_baris` `lux_ai/serapan/kehidupan_arsip.py` berada dalam pita
  **250..500** BARIS. Pita ini lebar dan saya mengakui sebabnya: saya tidak
  menyimpan ukuran byte berkas itu sama sekali, jadi dasarnya hanya ingatan
  struktur modulnya. Pita lebar yang jujur lebih baik daripada pita sempit yang
  dikarang. Penggugur: `cacah_berkas_hilang` != 0 → TIDAK TERADJUDIKASI.
- **R-214** — `cacah_baris` `lux_ai/serapan/silang_funding.py` berada dalam pita
  **330..430** BARIS. Dasar: saya menulisnya beberapa jam lalu dan membacanya
  ulang utuh; docstring praregistrasinya panjang. Tetap ramalan, bukan
  pengetahuan.
- **R-215** — CI melaporkan **316 butir** dan **kode 0**. Satuan: BUTIR yang
  dikumpulkan pytest. Basis: 316 terverifikasi pada run 30431610324 (commit
  1b0e8d8e); V3 tidak menambah maupun menghapus satu pun fungsi uji, jadi
  angkanya harus DIAM (aturan 54: dicacah dari berkas uji yang sudah ada, bukan
  dari ingatan). Commit ini menyentuh `lux_ai/**`, sehingga CI PASTI menyala —
  berbeda dari R-209 dan R-212 yang batal karena `ci.yml` mengabaikan `journal/**`.
- Cacah baris `ukur_baris.py` sendiri SENGAJA tidak diramalkan pada V3, sebab
  berkas inilah yang sedang saya sunting dan angkanya berubah oleh suntingan ini;
  meramalkannya hanya akan menambah ramalan murah.

---

## V4 (29 Juli 2026) — satu berkas baru, dan satu angka kedaluwarsa ditebus

Seluruh teks V1..V3 dibiarkan utuh, termasuk R-213 dan R-214 yang keduanya
diadjudikasi TEPAT (kehidupan_arsip.py 496 baris dalam pita 250..500;
silang_funding.py V1 396 baris dalam pita 330..430). Yang berubah pada V4 tetap
hanya SATU hal: `BERKAS_DIUKUR` bertambah `lux_ai/serapan/lubang_tengah.py`.
Mekanika, definisi `cacah_baris`, pagar 800, dan medan penggugur TIDAK disentuh.

Dua alasan, dan keduanya utang yang sudah tercatat di STATE:

1. `lubang_tengah.py` lahir pada commit `680d04b4` dan sama sekali belum masuk
   daftar ukur, sehingga pagar 800 belum pernah diuji atasnya.
2. Angka **396 baris** untuk `silang_funding.py` adalah angka **V1**. Modul itu
   sudah naik ke V2 (tujuh fungsi baru dan satu bagian docstring baru), jadi 396
   resmi KEDALUWARSA dan dilarang ditaksir dari byte — itu pola yang sudah
   menjatuhkan R-175, R-179, dan R-203. Nama `silang_funding.py` sudah ada di
   daftar sejak V3, jadi run ini menebusnya tanpa perubahan daftar.

Sebelum berkas ini disunting, `tests/test_ukur_baris.py` dibaca utuh SEKALI LAGI
(blob `7975bf88`): ketiga fungsi ujinya tidak mengunci panjang `BERKAS_DIUKUR`
maupun nama-namanya; yang dikunci hanya `cacah_berkas_hilang == 0` atas repo
nyata. `lubang_tengah.py` sudah ada di `main`. Karena itu cacah butir uji TIDAK
berubah oleh V4.

PRAREGISTRASI V4 (ditulis SEBELUM run ini):

- **R-224** — `cacah_baris` `lux_ai/serapan/lubang_tengah.py` berada dalam pita
  **350..470** BARIS. Dasar: saya menulis dan membaca ulang berkas itu beberapa
  menit lalu; docstring praregistrasinya panjang (kira-kira seratus baris) dan
  badan kodenya sebelas fungsi. Tetap ramalan, bukan pengetahuan — saya tidak
  pernah mencacahnya, dan mencacah dari ingatan adalah KC-19.
- **R-225** — `cacah_baris` `lux_ai/serapan/silang_funding.py` **V2** berada
  dalam pita **470..620** BARIS, dan `cacah_berkas_melebihi_pagar` = **0** atas
  ketiga belas berkas. Dasar: V1 terukur 396 baris; V2 menambah tujuh fungsi
  (`nama_daftar`, `baca_medan_baris`, `bulan_per_simbol`, `bentuk_lubang_lokal`,
  `daftar_hidup_tanpa_funding`, `daftar_lubang_tak_dikenal`, `sebaran_bentuk`,
  `sebaran_bentuk_semua`, `berkas_daftar` — sembilan, dicacah dari berkas yang
  sudah dibaca ulang utuh) serta satu bagian docstring. Bila hasilnya melampaui
  620, aturan 48 langsung berlaku atas berkas itu dan ia wajib dipecah sebelum
  fungsi berikutnya ditambahkan.
- **R-226** — CI melaporkan **382 butir** dan **kode 0**. Satuan: BUTIR yang
  dikumpulkan pytest. Basis: 382 terverifikasi pada run 30436334383 (commit
  680d04b4); V4 tidak menambah maupun menghapus satu pun fungsi uji, jadi
  angkanya harus DIAM. Bila ia bergerak tanpa uji baru, ada uji yang hilang atau
  gagal terkumpul, dan itu MELESET.

Catatan jujur: cacah baris `ukur_baris.py` sendiri kembali TIDAK diramalkan,
sebab berkas inilah yang sedang disunting.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

VERSI = 4
KELUARAN = "reports/ukur_baris.json"
PAGAR_BARIS = 800

BERKAS_DIUKUR = [
    "lux_ai/serapan/funding.py",
    "lux_ai/serapan/funding_cdn.py",
    "lux_ai/serapan/arsip.py",
    "lux_ai/serapan/gerbang_1m.py",
    "lux_ai/serapan/kehidupan.py",
    "lux_ai/serapan/kehidupan_arsip.py",
    "lux_ai/serapan/kohort_ekor.py",
    "lux_ai/serapan/kohort_ringkas.py",
    "lux_ai/serapan/lubang_tengah.py",
    "lux_ai/serapan/pulihkan.py",
    "lux_ai/serapan/resample.py",
    "lux_ai/serapan/silang_funding.py",
    "lux_ai/serapan/ukur_baris.py",
]


def ukur_berkas(jalur: Path) -> dict:
    """Ukur satu berkas. Berkas hilang DILAPORKAN, bukan melempar."""
    p = Path(jalur)
    if not p.is_file():
        return {
            "berkas": str(jalur),
            "ada": False,
            "byte": None,
            "sha256": None,
            "cacah_baris": None,
            "cacah_newline": None,
            "berakhir_newline": None,
            "cacah_baris_kosong": None,
            "cacah_baris_komentar": None,
            "cacah_baris_kode": None,
            "melebihi_pagar": None,
        }
    data = p.read_bytes()
    teks = data.decode("utf-8", "replace")
    baris = teks.splitlines()
    kosong = sum(1 for b in baris if not b.strip())
    komentar = sum(1 for b in baris if b.strip().startswith("#"))
    return {
        "berkas": str(jalur),
        "ada": True,
        "byte": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "cacah_baris": len(baris),
        "cacah_newline": teks.count("\n"),
        "berakhir_newline": teks.endswith("\n"),
        "cacah_baris_kosong": kosong,
        "cacah_baris_komentar": komentar,
        "cacah_baris_kode": len(baris) - kosong - komentar,
        "melebihi_pagar": len(baris) > PAGAR_BARIS,
    }


def ringkas(hasil) -> dict:
    """Cacah lintas berkas beserta penggugurnya."""
    daftar = list(hasil)
    ada = [h for h in daftar if h.get("ada")]
    return {
        "cacah_berkas_diminta": len(daftar),
        "cacah_berkas_ada": len(ada),
        "cacah_berkas_hilang": len(daftar) - len(ada),
        "cacah_berkas_melebihi_pagar": sum(1 for h in ada if h.get("melebihi_pagar")),
        "cacah_baris_total": sum(int(h.get("cacah_baris") or 0) for h in ada),
        "cacah_baris_terbesar": max((int(h.get("cacah_baris") or 0) for h in ada), default=0),
    }


def jalankan(akar: str = ".") -> dict:
    hasil = [ukur_berkas(Path(akar) / nama) for nama in BERKAS_DIUKUR]
    for h, nama in zip(hasil, BERKAS_DIUKUR):
        h["berkas"] = nama
    return {
        "versi_ukur_baris": VERSI,
        "pagar_baris": PAGAR_BARIS,
        "definisi_cacah_baris": (
            "len(teks.splitlines()), definisi yang sama dengan pagar 800 baris di "
            "tests/test_kontinuitas.py; inilah definisi yang mengadjudikasi R-175 "
            "dan R-179"
        ),
        "berkas": hasil,
        "ringkasan": ringkas(hasil),
        "catatan_penggugur": (
            "cacah_berkas_hilang != 0 berarti daftar yang diukur tidak lengkap dan "
            "seluruh cacah di laporan ini batal dipakai menutup ramalan (aturan 24)"
        ),
        "catatan_satuan": "cacah_baris bersatuan BARIS; byte bersatuan BYTE (aturan 47)",
        "catatan_versi": (
            "V2 hanya menambah kehidupan.py dan ukur_baris.py ke daftar; V3 menambah "
            "kehidupan_arsip.py dan silang_funding.py; V4 menambah lubang_tengah.py. "
            "Mekanika, definisi, dan pagar tidak berubah sejak V1 (aturan 29). Angka "
            "318 baris pulihkan.py yang tercatat di STATE adalah angka V1 dan "
            "digantikan oleh laporan ini; angka 396 baris silang_funding.py adalah "
            "angka V1 dan digantikan oleh laporan V4 ini"
        ),
    }


def main() -> int:
    laporan = jalankan(".")
    Path(KELUARAN).parent.mkdir(parents=True, exist_ok=True)
    with open(KELUARAN, "w", encoding="utf-8") as f:
        json.dump(laporan, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True))
    return 2 if laporan["ringkasan"]["cacah_berkas_hilang"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
