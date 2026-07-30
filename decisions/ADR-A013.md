# ADR-A013 — Klaim arah waktu wajib dipilah tebing lawan bukan-tebing

Status: **DITERIMA** (2026-07-30, jurnal 127)
Menggantikan sebagian: ADR-A012 (yang mencabut arah sebab A009)
Berkaitan: aturan 10, 24, 44, 46, 47, 50

## Konteks

R-305 mengukur bagian `mati_tidak_setelah_lubang_bukan_awal` = **1.0 (118/118)**
dengan perbandingan LEMAH (`<=`). ADR-A012 menyatakan angka itu artefak
tautologis dan mencabut klaim arah sebab.

R-306 menguji ulang dengan perbandingan **STRIKT** (`<`) di atas penyebut yang
sama (118 simbol). Hasil terukur (run 30524631435, kode 0):

| kelas | cacah |
| --- | --- |
| `mati_dulu` (MATI < lubang) | 40 |
| `serempak` (bulan sama) | 78 |
| `lubang_dulu` (MATI > lubang) | 0 |

Bagian strikt = **0.339**, di dalam pita praregistrasi 0.25..0.60 → R-306 butir 1
MENANG. Namun pemilahan lanjutan menunjukkan: **39 dari 40** simbol `mati_dulu`
ber-`bulan_lubang_bukan_awal_pertama` TEPAT `2025-07`, yaitu bulan tebing
`kohort_ekor.TEBING`. Satu-satunya pengecualian adalah **BTCSTUSDT** (lubang
`2022-01`, MATI `2021-04`).

## Masalah

Angka 0.339 secara aritmetika benar, tetapi bila dibaca sebagai bukti bahwa
"kematian mendahului lubang funding pada 40 simbol", ia menyesatkan. Yang
sebenarnya terjadi adalah SATU peristiwa penerbitan (funding berhenti serempak
pada 2025-07) yang menimpa 39 simbol yang sudah mati lebih dulu. Derajat
kebebasan efektif klaim itu bukan 40, melainkan mendekati 1.

Ini bukan kasus irisan-dianggap-sebab (aturan 10) dalam bentuk lamanya. Ini
bentuk yang lebih halus: **satu peristiwa yang menyamar sebagai banyak
pengamatan bebas**. Kekeliruan semacam ini tidak tertangkap oleh penyebut yang
benar, oleh kendali positif, maupun oleh perbandingan strikt — ketiganya sudah
diterapkan dan tetap lolos.

## Keputusan

1. Setiap klaim arah waktu antara kematian dan lubang funding WAJIB dilapor dalam
   dua kolom terpisah: **di-tebing** (`bulan_lubang_bukan_awal_pertama` ==
   `kohort_ekor.TEBING`) dan **bukan-tebing**. Angka gabungan saja tidak cukup
   dan tidak boleh dikutip sendirian.
2. Kelas `serempak` TIDAK PERNAH masuk numerator klaim arah. Perbandingan tanggal
   dalam uji arah wajib STRIKT.
3. Kekuatan bukti arah waktu yang lepas dari tebing dinyatakan APA ADANYA:
   **satu simbol (BTCSTUSDT)** atas penyebut 118. Selama cacah bukan-tebing masih
   satuan, tidak ada klaim arah sebab yang boleh dinaikkan derajatnya.
4. Klaim apa pun di masa depan yang numeratornya dikuasai satu bulan kalender
   (≥ 1/4) wajib dilapor bersama cacah per bulan dan ditandai sebagai kemungkinan
   artefak satu peristiwa. (Dirumuskan sebagai calon aturan B di jurnal 127 §9;
   penomoran resmi ditunda sampai `STATE_LAMPIRAN.md` dibaca utuh, agar tidak
   mengulang KC-41.)
5. ADR-A012 TETAP berlaku: arah sebab A009 tetap tercabut untuk seluruh semesta.
   R-306 tidak memulihkannya; ia hanya mengukur seberapa kecil sisa buktinya.

## Akibat

- Poros lubang/funding dinyatakan hampir habis sebagai sumber pertanyaan
  berisiko: R-304, R-305, dan R-306 semuanya berujung pada peristiwa 2025-07 yang
  sama. R-307 karena itu dipindah ke H-A017 (byte parquet atas 19.586
  simbol-bulan), poros yang belum pernah diukur.
- `lubang_tebing` V1 tetap sah sebagai pengukuran (sembilan penggugur nol, kedua
  kendali sah, kode 0) dan menjadi rujukan angka 40/78/0 serta 39.
- Taksonomi lubang tiga kelas (awal / delisting / tebing) naik prioritas: tanpa
  itu, setiap cacah lubang akan terus mencampur satu peristiwa penerbitan dengan
  peristiwa per-simbol.

## Bukti

- `reports/lubang_tebing.json` (run 30524631435, commit `84b11164`), sidik kode
  `4a5c2e4279eb1554dc119b48d6a8db61f6ea4ee11b7539efd70ee71d1ae18bf3`.
- `reports/lubang_tebing_status.json` — kode_keluar 0.
- `reports/ci_terakhir.json` — run 30524631516, 1044 butir, kode 0.
- Jurnal 127 §4–§6.
