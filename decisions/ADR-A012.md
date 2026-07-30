# ADR-A012 — Arah sebab A009 dicabut untuk SELURUH semesta; lubang awal langka; tebing data dicurigai

- Status: DITERIMA
- Tanggal: 30 Juli 2026
- Ramalan penentu: **R-305** (MELESET), diadjudikasi di jurnal 126 §3.
- Menggantikan sebagian: ADR-A009 (arah sebab), ADR-A011 (yang hanya membatasi
  A009 pada kelas bangkit).

## Konteks

ADR-A009 mengajukan arah sebab "kematian pasar mendahului berhentinya funding".
R-304 menggugurkannya pada delapan simbol bangkit, dan ADR-A011 membatasi
pencabutan itu hanya pada kelas bangkit sambil menunggu R-305 pada penyebut besar.

R-305 mengukur penyebut besar (`lubang_awal` V1, run 30522785043, commit
`d304d3eb`, kode 0, kedua kendali sah, enam selisih nol). Hasilnya, dengan pita
dikunci di jurnal 125 §7 sebelum angka terlihat:

- **Butir 1:** penyebut 118 (≥100, teradjudikasi), bagian **1.0** — di ATAS pita
  55–95% → KALAH.
- **Butir 2:** cacah simbol bulan-pertama-berlubang **5** — di BAWAH pita 20–120
  → KALAH.

## Keputusan

Mengikuti akibat yang dipraregistrasi di jurnal 125 §7:

1. **Arah sebab A009 DICABUT untuk SELURUH semesta**, bukan hanya kelas bangkit.
   Butir 1 yang mencapai 100% BUKAN penguat arah sebab: pemeriksaan baris
   menunjukkan angka itu tautologis (lubang bukan-awal sering ADALAH bulan
   delisting, atau muncul di tebing data 2025-07 jauh sesudah kematian). Aturan 10
   (irisan bukan sebab) berlaku penuh. Tidak ada klaim arah sebab yang boleh
   dibangun dari urutan bulan lubang-vs-mati tanpa memisahkan delisting dan tebing
   lebih dulu.
2. **Dugaan "lubang awal = kelas penerbitan-belum-mulai yang besar" GUGUR.**
   Hanya 5 dari 787 simbol berlubang di bulan klines pertama. Lubang awal tetap
   dicatat sebagai kelas tersendiri (KC-46), tetapi LANGKA (0,6%), bukan tulang
   punggung taksonomi. Ia wajib diukur ulang tanpa praduga.
3. **Tebing data 2025-07 dicurigai sebagai sumber lubang funding semu.** Banyak
   `bulan_lubang_bukan_awal_pertama` bernilai tepat `kohort_ekor.TEBING`. R-306
   dipraregistrasi untuk menakar besarnya (jurnal 126 §7). Sampai R-306
   teradjudikasi, angka lubang bukan-awal TIDAK boleh dipakai sebagai kejadian
   pasar tanpa memangkas tebing.
4. **KC-45 (satuan bulan wajib tersurat) dan KC-46 (periksa bentuk lubang sebelum
   tafsir arah waktu) terbukti berguna** dan wajib diangkat menjadi KC resmi di
   STATE v45.

## Konsekuensi

- H-A017 tetap dibatasi pada LITUSDT (1 dari 8), sesuai ADR-A011.
- Modul `lubang_awal` V1 tetap sah sebagai alat ukur; medannya dipakai kembali
  oleh R-306. Definisi lubang memakai `silang_funding.bentuk_lubang_lokal` apa
  adanya (aturan 36).
- Setiap pengukuran lubang funding berikutnya wajib memisahkan tiga kelas:
  lubang-awal (belum mulai), lubang-delisting (bulan mati), dan lubang-tebing
  (artefak 2025-07). Menyatukannya menghasilkan tafsir sebab yang salah, seperti
  R-304 dan R-305 membuktikan.

## Sidik kode penentu

- `lubang_awal` V1 = `156499ce9d6e822bb7f57786e8e308955441996699c1fd53d0e8814e1f8f2362`
- `silang_funding` V2 = `8a9b859c09cd64e30e203e6f8dc53411b8e341c44f112805b3041e5d4d3231b1`
