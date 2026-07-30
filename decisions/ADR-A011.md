# ADR-A011 — Arah sebab "kematian mendahului berhentinya funding" DICABUT pada kelas bangkit

- Tanggal: 30 Juli 2026
- Status: **DITERIMA**
- Bahan: `reports/sebab_bangkit.json` blob
  `9d654428c755319af3ea4dc34e87e3b90ba74af0`, run **30517682958**, commit
  `3913a0546c8db08b83ec22051459fdb24c4baf2d`, kode keluar 0, laporan TERBACA
  UTUH. Sidik kode `bafe4359e8f36f0402d4be4a4e4aef4a28f224f6419f06f701fb3a5bf696221a`.
- Ramalan yang mendasari: **R-304**, dipraregistrasi di jurnal 124 §8,
  diadjudikasi **MELESET** di jurnal 125 §3.

## 1. Keputusan

1. **Arah sebab ADR-A009 DICABUT untuk kelas simbol bangkit.** Bunyi "kematian
   pasar mendahului berhentinya funding" hanya terukur pada **1 dari 8** simbol
   bangkit (pita praregistrasi 5..8). Pertanyaan arah sebab dinyatakan **BELUM
   TERJAWAB**, sesuai akibat yang sudah dinyatakan sebelum angka terlihat.
2. **H-A017 diturunkan derajat dan dirumuskan ulang.** Bunyi lama memperlakukan
   selisih 5 bulan pada LITUSDT sebagai pola. Bunyi baru: "pada LITUSDT, dan
   sejauh ini HANYA pada LITUSDT di antara delapan simbol bangkit, bulan MATI
   pertama mendahului bulan berlubang funding pertama sebanyak 5 bulan."
   Penyebutnya wajib ikut disebut setiap kali angka itu dipakai (aturan 74).
3. **Kematian pasar dan lubang funding dinyatakan DUA GEJALA BERBEDA.** Lima dari
   delapan simbol bangkit MATI 11–29 bulan tanpa satu pun lubang funding.
4. **Lubang funding di bulan klines PERTAMA tidak boleh dibaca sebagai "funding
   berhenti".** ICPUSDT (bulan pertama 2021-05) dan TLMUSDT (bulan pertama
   2021-07) berlubang tepat sejak bulan pertama riwayatnya; selisih −14 dan −12
   bulan itu adalah gejala penerbitan yang BELUM MULAI. Setiap tafsir arah waktu
   wajib memeriksa bentuk lubang lebih dahulu.
5. **ADR-A003 wajib memuat koreksi ini** berdampingan dengan delapan simbol
   bangkit yang sudah diwajibkan ADR-A010 §3.4.

## 2. Yang TIDAK diputuskan

- Tidak diputuskan bahwa funding menyebabkan apa pun. Urutan bulan bukan sebab
  (aturan 10); yang gugur hanyalah satu arah tafsir.
- Tidak diputuskan apa pun tentang 779 simbol non-bangkit. Penyebut keputusan ini
  adalah **8 simbol**, dan itu penyebut yang kecil (aturan 20).
- Tidak diputuskan bahwa "33 HIDUP tanpa funding" bukan ciri kebangkitan dalam
  satuan simbol-bulan; 24 dari 33 memang berada pada dua simbol bangkit, tetapi
  itu pengamatan PASCA-HOC dan tidak dipakai membatalkan kekalahan butir 2.

## 3. Pembatal (aturan 24)

Keputusan ini gugur bila salah satu terjadi:

1. R-305 butir 1 menang pada penyebut ≥ 100 simbol, yang berarti arah sebab
   berlaku di luar kelas bangkit dan ADR ini wajib dibatasi ulang.
2. Ditemukan pengukuran yang menunjukkan `cacah_mati_dulu` > 1 pada delapan
   simbol itu dengan definisi lubang yang sama.
3. `selisih_bangkit`, `selisih_tersisip`, `selisih_penyebut`, `selisih_simbol`,
   `selisih_mati`, atau `selisih_lubang_dalam_penyebut` ternyata bukan nol pada
   pengukuran ulang.
4. Kendali detektor arah waktu gagal memisahkan dua bentangan buatan pada versi
   modul berikutnya.

## 4. Kendali yang menyertai keputusan ini

- Kendali data: tiga simbol-bulan berparquet terbesar (BTCUSDT 2021-05,
  2021-08, 2021-01) HIDUP dan berfunding → sah.
- Kendali detektor: dua bentangan buatan terpisah dengan selisih +1 dan −1 → sah.
- Silang dua jalan: cacah tersisip lokal == cacah tersisip `tersisip_semesta`
  pada 8/8 simbol, total 88 — cocok dengan R-303.
