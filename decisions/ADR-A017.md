# ADR-A017 — Keputusan sesudah R-310 (isi bulan MATI)

- Tanggal: 2026-07-30
- Status: DITERIMA
- Sumber ukur: `reports/keterisian_lilin.json` blob
  `14f1772070789dad603b132ece034ea4c19c6e3d` (6.588 B, terbaca utuh) dan
  `reports/keterisian_lilin_ringkas.json` blob
  `f33714eda66e77d37a7024b52c433ead070b16c7`, run 30535202643, kode 0,
  commit `924b0d7afcf1f9e17965dff931d36489ad27f01b`.
  Sidik kode modul `1cd98f4fa22c24b30f31f5b36dac0ea0bb3fa9de44e5e15ae73cbf11cdca08bb`.
  CI 1297 butir, kode 0, blob `3c07c9093d5232ce3852b2ac509fd9e9875f0f33`.
- Jurnal terkait: 131 (blob `cae9ab53641f7e0b984e6fb1a439f4720ffa5e88`, praregistrasi),
  132 (blob `35c5400ea2a6fb6191c26bd5d7f7dbc3f630b2f0`, adjudikasi),
  133 (blob `ee0ed4cde76bf7054bf64dd1d991396208303577`, penutup).
- ADR sebelumnya yang bersambung: A015 (kep. 5, larangan besar berkas sebagai
  detektor status) dan A016 (kep. 5 → calon KC-50; kep. 7 → pertanyaan yang
  dijawab R-310).

## Konteks

ADR-A016 kep. 7 menetapkan pertanyaan terbuka nomor satu: **apa isi berkas bulan
MATI**, yang byte minimumnya 97.634 dan rata-ratanya 413.305,781 tetapi tak satu
pun jatuh ke zona kecil. Pertanyaan itu tiga giliran berturut tidak terjawab.
R-310 menjawabnya dan menang bulat: butir 1 = 9 (pita 1..120), butir 2 = 0,0445
(pita 0.02..0.25), butir 3 seluruh kendali sah.

ADR ini dituntut bukan oleh kemenangannya, melainkan oleh sesuatu yang ditemukan
sambil lalu: dua angka yang selama berpuluh kutipan diperlakukan setara ternyata
berbeda 516.135. Itu temuan terpenting giliran tersebut, dan ia bukan bagian dari
ramalan mana pun.

## Keputusan

**1. Temuan pokok R-310 DITERIMA, dengan rumusan yang dibatasi.** Rumusan resmi
yang boleh dikutip: *dari 1.401 baris MATI, 1.392 (99,4%) memuat lilin sebanyak
lilin penuh bulannya, dan 9 tidak penuh; bulan MATI karena itu bukan bulan yang
datanya berhenti, melainkan bulan yang transaksinya nol sementara lilinnya tetap
dicetak.* Ini menutup A016 kep. 7.

**2. DILARANG melanjutkan temuan itu ke pernyataan tentang HARGA.** `medan_baris_terlihat`
berisi empat belas medan — `ada_di_arsip`, `bagian_volume_nol`, `bulan`,
`byte_parquet`, `cacah_baris_cacat`, `cacah_lilin`, `cacah_lilin_terbaca`,
`cacah_volume_nol`, `galat`, `gerbang_lolos`, `jalur`, `simbol`, `status`,
`transaksi_total` — dan tak satu pun harga. Ungkapan "harga beku", "lilin datar",
atau "lilin berulang" DILARANG ditulis sebagai temuan sampai ada pengukuran yang
menyentuh kolom harga (aturan 10).

**3. KC-50 DIRESMIKAN** (resmi sejak STATE v50): *agregat semesta yang diperoleh
lewat jalan memutar — dijumlahkan dari kelas, disalin dari angka tercatat, atau
diwarisi dari laporan lain — tidak boleh diperlakukan sebagai pemeriksaan bebas,
dan bila dua angka seharusnya setara, keduanya wajib diadu dan selisihnya
dilaporkan termasuk bila nol.* Dua kasusnya: `total_byte` turunan pada
`irisan_byte` (delapan bebas + satu turunan), dan 839.842.134 lawan 839.325.999.
Cacat kelas ini tidak menghasilkan galat; ia menghasilkan kesunyian.

**4. Koreksi resmi: 839.842.134 BUKAN jumlah lilin.** Angka itu adalah total baris
parquet semesta dari run rilis 30404071324. Jumlah lilin yang dihitung LANGSUNG
dari medan `cacah_lilin` atas 19.586 baris adalah **839.325.999**. **Selisih
516.135.** Seluruh aritmetika implikasi jurnal 131 §6 dibangun di atas penyamaan
itu dan karena itu cacat sebagai turunan; R-310 sendiri tetap sah karena pitanya
dikunci sebelum pengukuran (aturan 29). Dugaan penyebab — 19.598 − 19.586 = 12
simbol-bulan karantina, 516.135 / 12 = 43.011 ≈ sebulan penuh — **BELUM DIUJI dan
DILARANG dikutip sebagai penjelasan.**

**5. Aturan 84 DIRESMIKAN** (resmi sejak STATE v50): *butir praregistrasi yang
memakai klausa ATAU wajib melaporkan sumbangan BEBAS setiap klausa secara
terpisah; bila laporan tidak dapat memisahkannya, klausa ATAU DILARANG dan butir
harus dipecah.* Usulannya lahir di A016 kep. 3 dari cacat butir 1 R-309. R-310
mematuhinya secara preventif: kedua butir berisikonya berklausa TUNGGAL.

**6. Numerator 9 BUKAN sembilan pengamatan bebas.** Tujuh dari sembilan baris MATI
tak penuh berbulan `2024-05` dengan `cacah_lilin` 39.308..39.317 — jendela selebar
sembilan lilin. Ini kasus baru KC-47 dan penerapan aturan 81. Cacah pengamatan
bebas paling banter **tiga**: gugus `2024-05`, LENDUSDT 2020-11, FRONTUSDT 2024-09.
Setiap kutipan angka 9 wajib menyertakan batas ini.

**7. H-A020 DIUSULKAN, belum diuji:** *ketujuh baris `2024-05` adalah satu
peristiwa, bukan tujuh pengamatan bebas.* Bersamanya berlaku larangan tersurat:
**kalimat "tujuh simbol didelisting 28 Mei 2024" DILARANG ditulis sebagai temuan.**
Tanggal itu tidak terukur; yang terukur hanya lebar jendela. Cara menguji yang
disarankan: `lubang_tengah` atas gugus `2024-05`, untuk melihat apakah lilin yang
hilang menempati posisi yang sama pada ketujuh simbol.

**8. Larangan ADR-A015 kep. 5 TIDAK DIBALIK.** R-310 memang menjelaskan kedua
berkas MATI terkecil — LENDUSDT 2020-11 (97.634 byte, 13.475 lilin) dan FRONTUSDT
2024-09 (109.120 byte, 14.986 lilin) — sebagai baris dengan lilin paling sedikit di
seluruh semesta. Menjelaskan dua kasus bukan membangun detektor. Besar berkas tetap
DILARANG dipakai sebagai penanda status ke arah mana pun.

**9. H-A019 DIKUATKAN dari jalur ukur kedua, tanpa perubahan rumusan.** Bulan
pertama menanggung 17.335.439 dari 18.143.601 defisit (95,5%) dan terisi
rata-rata **≈49,7%** — sebangun dengan nisbah byte 0,527179 dari R-309. Rumusan
resmi H-A019 tetap persis seperti A016 kep. 1; penguatan ini tidak memperluasnya.
**TLMUSDT 2023-03 tetap melawan** dan TIDAK dijelaskan oleh R-310, sebab baris itu
berstatus HIDUP sehingga mustahil muncul di daftar MATI tak penuh.

**10. Pertanyaan terbuka nomor satu berpindah ke sisa 712.925 lilin.**
808.162 − 95.237 = 712.925 lilin defisit pada baris bukan-pertama yang BUKAN baris
MATI tak penuh. Baris mana yang menanggungnya belum diukur. Poros ini didahulukan
di atas selisih 516.135 justru karena angkanya belum tersirat sama sekali.

**11. Cacah tangan pasca-trio dicatat sebagai TERHITUNG** pada ref
`5d7d8b96508e0885bb1ced60811de3fe69e66007`: `lux_ai/serapan/` = **48**,
`tests/` = **52**, `.github/workflows/` = **43**. Ketiganya dicacah satu per satu
dan bernomor, tanpa rentang, dan cocok dengan ramalan turunannya. Kecocokan itu
bukan alasan untuk melewatkan pencacahan berikutnya (aturan 66, KC-33).

## Alternatif yang DITOLAK

- **Membacakan R-310 sebagai konfirmasi kuat.** Ditolak: kedua butir berisiko
  menang **tipis ke tepi BAWAH** pitanya (9 pada 1..120; 0,0445 pada 0.02..0.25).
  Pita yang lebar di sisi atas membuat kemenangan lebih murah daripada tampaknya.
- **Menyatakan bahwa bulan MATI "harganya beku".** Ditolak: harga tidak tersimpan
  di laporan kehidupan. Lihat kep. 2.
- **Menjelaskan selisih 516.135 dengan karantina 12 simbol-bulan.** Ditolak sebagai
  penjelasan; diterima hanya sebagai dugaan yang menunggu pengukuran. Aritmetikanya
  rapi, dan justru kerapian itu yang membuatnya berbahaya bila dikutip lebih awal.
- **Menghitung sembilan baris MATI tak penuh sebagai sembilan bukti.** Ditolak,
  lihat kep. 6.
- **Membalik ADR-A015 kep. 5 karena dua anomalinya kini terjelaskan.** Ditolak,
  lihat kep. 8.
- **Memperluas H-A019 menjadi "bulan pertama menyebabkan defisit lilin".** Ditolak:
  yang terukur adalah dua besaran yang bersesuaian dari dua jalur, bukan arah sebab
  (aturan 10). Bersesuaian bukan menyebabkan.
- **Menyusun R-311 pada giliran yang sama dengan adjudikasi.** Ditolak, meneruskan
  A016 alternatif terakhir: aturan 83 menuntut paragraf aritmetika implikasi lebih
  dulu, dan konteks giliran adjudikasi selalu sudah terpakai berat.
- **Mendorong ulang EKOR v10 hanya untuk memperbaiki satu karakter `≉`.** Ditolak
  (KC-42): koreksinya ditulis di UKUR v10 §Koreksi 5 dan PROMPT v54, dan perbaikan
  berkasnya menunggu EKOR v11.

## Konsekuensi

- STATE v50 sudah memuat KC-50 dan aturan 84 sebagai RESMI, papan skor 310, dan
  koreksi 516.135. ADR ini tidak menambah kewajiban baru pada STATE v50; ia
  memformalkan dasarnya.
- STATE v51 wajib memuat: cacah tangan **48 / 52 / 43** pada ref `5d7d8b96` sebagai
  TERUKUR, aturan 57 beruntun **3/3** dengan catatan bahwa beruntun itu murah, dan
  status ADR ini.
- Rumusan kep. 1 adalah satu-satunya bentuk temuan R-310 yang boleh dikutip modul
  atau dokumen berikutnya.
- Aturan resmi menjadi **1–81, 83, 84**; 77, 78, dan 82 tetap usulan; nomor bebas
  berikutnya **85**. KC resmi sampai **KC-50**; berikutnya **KC-51**.
- Hipotesis berikutnya **H-A021**. **H-A020 DIUSULKAN dan belum diuji.**
- ADR berikutnya **A018**. Utang lama tetap berlaku: **A003 wajib memuat koreksi
  A011, A012, A013, A014, A015, dan A016** — dan sejak ADR ini, juga **A017**.
