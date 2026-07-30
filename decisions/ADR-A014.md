# ADR-A014 — Byte parquet: arah H-A018 didukung, pita gugur, dan "kecil" BUKAN penanda mati

Status: **DITERIMA** · Tanggal: 2026-07-30 (sesi 59) · Ramalan terkait: **R-307
MELESET** · Menggantikan: tidak ada · Dibatasi oleh: tidak ada

## Konteks

R-307 adalah pengukuran PERTAMA yang menjumlahkan `byte_parquet` atas seluruh
19.586 simbol-bulan. Poros H-A018 (byte parquet sebagai gejala kehidupan) baru
dipisahkan dari H-A017 pada STATE v46, sesudah label salah tertangkap sebagai
KC-41. Sebelum hari ini, seluruh dasar H-A018 hanyalah satu simbol: LITUSDT.

Hasilnya (`reports/byte_semesta.json`, blob `8b7f2077`, run `30526358811`, kode 0):
total **32.706.262.375** byte; MATI **579.041.399** (bagian **0,017704**); rata
MATI **413.306** lawan HIDUP **1.771.963**; HIDUP `byte_min` **22.440** lawan MATI
`byte_min` **97.634**; tidak satu pun simbol-bulan ber-byte < 10.000.

## Masalah

R-307 MELESET pada kedua butir berisiko, tetapi kedua kekalahan itu berbeda
jenis, dan menyamakannya akan menyesatkan penerus:

1. Butir 1 kalah karena PITA saya keliru (0.0177 lawan pita 0.02–0.15), padahal
   ARAH yang diramalkan justru terbukti kuat.
2. Butir 2 kalah karena AMBANG-nya mustahil (10.000 byte, sementara dasar semesta
   22.440), jadi ia tidak pernah menguji alam sama sekali.

Sekaligus muncul satu angka yang melawan tafsir mudah: berkas TERKECIL di semesta
milik bulan HIDUP, lebih kecil daripada SETIAP bulan MATI.

## Keputusan

1. **R-307 dicatat MELESET** (dua butir berisiko KALAH). Dilarang dibaca sebagai
   kemenangan, dan dilarang "diselamatkan" dengan melebarkan pita sesudah
   pengukuran (aturan 29). Papan skor menjadi 307 dengan MELESET 57.
2. **H-A018 TIDAK dicabut; ia dipertajam dan dibatasi.** Bunyi yang BOLEH dipakai:
   "bulan MATI menempati bagian kecil dari byte semesta (0,0177) dan rata-rata
   sekitar 4,3 kali lebih kecil daripada bulan HIDUP (413.306 lawan 1.771.963)".
   Bunyi yang DILARANG: "berkas kecil berarti pasar mati" — kedua kelas beririsan,
   dan HIDUP `byte_min` 22.440 < MATI `byte_min` 97.634 membuktikan arah irisan
   itu justru berlawanan dengan dugaan. Besar berkas DILARANG dipakai sebagai
   detektor status kehidupan (kerabat KC-38).
3. **Nol pada butir 2 sah disebut TERUKUR**, bukan buta, karena
   `kendali_deteksi_sah` true: bentangan buatan memisahkan baris berbyte kecil,
   baris tepat di ambang, dan baris kelas LAIN. Yang tidak ada adalah datanya,
   bukan kemampuan detektornya (aturan 50, KC-21).
4. **Bulan MATI bukan bulan KOSONG.** `byte_min` MATI 97.634 dan `cacah_byte_nol`
   0 atas seluruh semesta: setiap simbol-bulan punya berkas berisi. Apa isi
   berkas bulan MATI (lilin berulang, volume nol, atau lainnya) BELUM diukur dan
   dilarang ditebak.
5. **Ambang absolut wajib bersandar pada sebaran terukur.** KC-48 diresmikan dan
   aturan 82 diusulkan. Praregistrasi R-308 sudah menaatinya: kedua ambangnya
   (97.634 dan 150.000) diambil dari sebaran yang diukur hari ini, bukan dari
   angka bulat yang enak dibaca.
6. **ADR-A012 dan ADR-A013 TETAP berlaku.** R-307 tidak menyentuh soal arah sebab
   sama sekali; ia sengaja pindah poros justru agar tidak lagi bergantung pada
   tebing `2025-07`. Dan itu berhasil: tidak satu pun angka R-307 dapat runtuh
   menjadi artefak satu bulan (KC-47 tidak berlaku di sini).

## Akibat

- Papan skor: **307** (TEPAT 215 / MELESET 57 / SEPARUH 20 / TT 8 / MENUNGGU 7).
- **KC-48 RESMI**; **aturan 82 DIUSULKAN** (bersama 77 dan 78 yang masih menunggu).
- H-A018 tetap terbuka dengan bunyi terbatas seperti keputusan 2.
- Pertanyaan baru yang naik prioritas: berapa lebar zona irisan HIDUP-berbyte-kecil
  (butir 1 R-308), dan apa ISI berkas bulan MATI.
- Taksonomi lubang tiga kelas (awal/delisting/tebing) dari ADR-A013 TETAP menunggu.

## Bukti

- `reports/byte_semesta.json` blob **`8b7f207750c1c458c5e1150f5f413150a1011996`**
- `reports/byte_semesta_status.json` blob **`2cbcbc1b…`** (run `30526358811`, kode 0)
- `reports/ci_terakhir.json` blob **`0765ce7b…`** — CI **1100**, run `30526358010`
- `lux_ai/serapan/byte_semesta.py` V1 blob **`ff68e4be…`**, sidik kode
  **`e02aca2b3967069b500b01d27a1d2d1553f47b912ea41ddbecd9e4e6c33883c7`**
- `tests/test_byte_semesta.py` blob **`0e1e3ab2…`** (56 butir, `test_01`..`test_56`)
- `.github/workflows/byte_semesta.yml` blob **`45650ff9…`**
- Sidik semesta COCOK dengan run sebelumnya (aturan 36): laporan kehidupan
  `24b6bb26…`, `sidik_data_funding` `2c9fbd1b…`, `silang_funding` `8a9b859c…`,
  `lubang_awal` `156499ce…` — semesta yang diukur sama.
- Praregistrasi R-307 di `journal/2026-07-30-127.md` §7, dikunci sebelum modul ada.
