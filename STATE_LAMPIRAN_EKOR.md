# STATE lampiran EKOR — bagian 2 dari STATE (v14, milik STATE v55)

**Mengapa berkas ini ada.** Dua push `STATE.md` berturut terpotong (v41, v42);
pemecahan ke tiga berkas berlaku sejak v43 (KC-42). Pembagian yang berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, 83, 84, 85, **86**; KC-1..KC-52.
2. **`STATE_LAMPIRAN_EKOR.md`** (berkas ini, v14) — bagian 2: papan skor, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** — bagian 3: pengukuran, modul, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) dan **`PROMPT_KELANJUTAN.md`**
   (blob `35beed44`) — **arsip; BUKAN sumber** (ADR-A018 kep. 9).

Dasar v14: EKOR v13 (blob **`26ba6dc06fcaa358df3d0ac511996a9bb40a864f`**), **dibaca
UTUH pada giliran yang sama sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43).

## KESERASIAN VERSI — dibaca apa adanya, termasuk yang belum serasi

Saat berkas ini didorong:

- `STATE.md` **v55** — blob **`be6bc6524e4209d370a4a5795a00bfe6c561d24d`**, commit
  **`cd209f3ed75a86470afa611ad6f2b97cb89e592e`**, dibaca ulang UTUH pada giliran yang
  sama ia didorong. **SERASI** dengan berkas ini.
- `STATE_LAMPIRAN_EKOR.md` **v14** — berkas ini.
- `STATE_LAMPIRAN_UKUR.md` masih **v13** — blob
  **`9e71c1ee9667c4b06389c87e0c77d4cefaca5b96`**, commit `2bdd8233`. **TERTINGGAL SATU
  VERSI.** Kepalanya berbunyi "milik STATE v54". Ia **tidak memuat**: aturan 86 resmi,
  ADR-A019, ketiga blob trio, temuan arah selisih R-312, dan aturan 38 ke-47/48/49.
  **Sampai UKUR v14 naik, sumber sah untuk seluruh butir itu adalah `STATE.md` v55,
  berkas ini, ADR-A019, dan jurnal 141** — bukan UKUR v13.

**Satu berkas per push tetap MENGIKAT** (KC-42, KC-43).

**Tentang push berkas ini:** ia di akar repo sehingga menyalakan `ci.yml`. Tidak satu
pun `tests/**` berubah, jadi cacah uji tetap **1377** — ramalan deterministik, **MUDAH**,
TIDAK diskor, TIDAK menambah beruntun aturan 57. **Laporannya WAJIB dibaca sebelum push
akar berikutnya**, atau ia hangus seperti run `30547842823`.

## KESALAHAN DOKUMEN SENDIRI — kini SEBELAS

Daftar ini disalin dari STATE v55 dan berlaku identik di ketiga bagian. Sebab tetap
sama setiap kali: `push_files` menulis ulang SELURUH berkas, sehingga memperbaiki satu
karakter berarti menyusun ulang berkas besar dari konteks terpakai — persis yang
dicatat KC-42 sebagai cara paling pasti merusaknya. Perbaikan selalu menumpang pada
penulisan ulang yang memang sudah dijadwalkan.

| # | berkas | tertulis | seharusnya | status |
| --- | --- | --- | --- | --- |
| 1 | jurnal 132 §3 | "beruntun 2/1" | 2/2 | LUNAS di STATE v50 |
| 2 | EKOR v10 | `terisi ≉49,7%` | `≈49,7%` | LUNAS di EKOR v11 |
| 3 | jurnal 135 §13.3 | "hendan dirumuskan" | "hendak" | LUNAS di STATE v51 |
| 4 | EKOR v11 kepala | "deretministik" | "deterministik" | LUNAS di EKOR v12 |
| 5 | UKUR v11 kepala | "KESERAIAN VERSI" | "KESERASIAN VERSI" | LUNAS di UKUR v12 |
| 6 | UKUR v11 daftar uji | penanda `**` tak berpasangan | berpasangan | LUNAS di UKUR v12 |
| 7 | STATE v52 | "Empat salah ketik" padahal tabelnya enam | "Enam" | LUNAS di STATE v53 |
| 8 | STATE v53 aturan 45 | "empat push terakhir" lalu mendaftar **ENAM** | "enam push terakhir" | LUNAS di STATE v54 |
| 9 | STATE v53 aturan 52 | pembacaan ulang "tidak menangkap satu pun" | **satu dari delapan** | LUNAS di STATE v54 |
| 10 | jurnal 138 §5 butir 2 | "maka **839.842.134 yang keliru**" | kesimpulan **tidak sah dari premisnya**; kedua angka benar | LUNAS di jurnal 140 |
| 11 | **jurnal 141 §6** | larangan R-312 nomor 5 "disajikan di EKOR v13 **dan ADR-A019** seolah diresmikan sesudah adjudikasi" | tuduhan **terlalu luas**; diadili dari sumber di bawah | **LUNAS di berkas ini** |

### Butir 11 — tuduhan diadili dari sumber, dan ia mengecil

STATE v55 mencabut tuduhan jurnal 141 terhadap EKOR v13 karena berkas itu belum dibaca
ulang. **Pada giliran ini EKOR v13 dibaca UTUH, dan vonisnya kini dapat dijatuhkan atas
bukti, bukan ingatan:**

| tertuduh | bunyi sebenarnya | vonis |
| --- | --- | --- |
| **STATE v54** | larangan 5 ditutup **"(syarat gugur nomor 3, jurnal 136)"** | **BEBAS** — atribusinya tepat sejak semula |
| **EKOR v13** | larangan 5 berbunyi lengkap tanpa satu kata pun tentang asal-usulnya | **kelalaian atribusi**, BUKAN misrepresentasi |
| **ADR-A019** | mendaftar kelima larangan di bawah kepala "DIRESMIKAN" | **bersalah ringan** — kalimatnya benar, konteksnya menyesatkan |

**Yang penting dan sering terlewat:** EKOR v13 tidak pernah **mengklaim** larangan itu
lahir dari adjudikasi. Ia hanya **diam** soal asal-usulnya. Jurnal 141 membaca kesunyian
sebagai klaim — kekeliruan yang bentuknya sama persis dengan butir 10 (kesimpulan tidak
sah dari premis yang benar), hanya berskala kecil. **Kredit atas larangan nomor 5 tetap
milik praregistrasi**, dan itulah inti jurnal 141 yang benar dan bertahan.

**Pelajaran yang sudah jadi larangan di STATE v55:** dilarang menuduh isi sebuah berkas
tanpa membacanya ulang.

### Batas kekuatan aturan 52 — rumusan v13 DIPERSEMPIT

EKOR v13 menulis bahwa pembacaan ulang aturan 52 "tidak berdaya sama sekali terhadap
penalaran yang cacat". **Rumusan itu terlalu luas dan dikoreksi di STATE v55:**

> Pembacaan ulang **dokumen sendiri** lemah terhadap penalaran cacat: ia membaca
> kalimat yang sudah diyakini benar. Pembacaan **kode** kuat terhadapnya: kode
> menyatakan identitas yang tidak dapat ditawar, dan ketidakcocokan antara docstring
> dan badan fungsi tampak begitu keduanya dibaca berdampingan.

Buktinya giliran lalu: pembacaan ulang trio `c1dc0009` **menangkap** cacat penalaran
terbesar yang tersisa — arah selisih R-312 yang mustahil positif. **DILARANG** menulis
bahwa aturan 52 menjaga mutu penalaran **atas dokumen**; **DIIZINKAN** mencatat bahwa
ia melakukannya **atas kode**, dengan satu kejadian terukur.

## KC-43..KC-52 (teks lengkap KC-43..KC-47 di STATE v47, KC-49 di v48, KC-50 di v50, KC-51 di v52, KC-52 di v54)

- **KC-43** — tanda tangan fungsi dari INGATAN. Penangkal: baca modul yang diimpor
  UTUH pada giliran yang sama.
- **KC-44** — semua laporan di-commit satu langkah.
- **KC-45 [RESMI v45]** — satuan "bulan tanpa funding" vs "bulan MATI" dicampur.
- **KC-46 [RESMI v45]** — lubang bentuk AWAL dibaca sebagai "funding berhenti".
- **KC-47 [RESMI v46]** — satu peristiwa menyamar sebagai banyak pengamatan bebas.
  Kasus kuat: TUJUH dari sembilan baris MATI tak penuh R-310 berbulan `2024-05` dalam
  jendela **9 lilin**. Diperiksa untuk R-311 dan TIDAK terpicu (ADR-A018 kep. 4).
  Diperiksa untuk R-313 dan TIDAK terpicu: dua belas parquet karantina tersebar di
  **enam pecahan berbeda** dengan cacah 3/3/1/1/3/1.
- **KC-48 [RESMI v47]** — ambang absolut pada besaran yang sebarannya belum diukur.
- **KC-49 [RESMI v8 lampiran ini]** — pita dikunci tanpa aritmetika implikasi.
  Penangkalnya berlaku sebagai aturan 83. **[v14] Tercatat ditaati DI DALAM KODE**
  R-312: lantai aritmetis 12 diturunkan tertulis dari 516.135 / 44.640 = 11,56…
  dibulatkan ke atas — terbaca dari docstring, bukan dari klaim.
- **KC-50 [RESMI di STATE v50]** — agregat lewat jalan memutar, sehingga selisih
  terhadap sumber lain mustahil terlihat. **Cacat kelas ini tidak menghasilkan galat;
  ia menghasilkan kesunyian.** Kasus 839.842.134 lawan 839.325.999 SELESAI, tetapi
  tidak dengan cara yang KC-50 ramalkan: jalur langsung memang memperlihatkan
  selisihnya; yang tidak dilihat siapa pun adalah bahwa selisih itu **sah**. Kasus
  `total_byte` `irisan_byte` dan tautologi 712.925 tetap berlaku penuh.
- **KC-51 [RESMI v52]** — **bias taksiran pemusatan**: besaran yang belum pernah diukur
  sebarannya secara sistematis ditaksir **lebih menyebar** daripada kenyataannya.
  **Empat kejadian berturut tanpa satu pun pembalikan arah:** R-308 butir 2 (pita
  10..300 → **2**); R-310 butir 2 (0,073; pita 0,02..0,25 → **0,0445**); R-311 butir 1
  (3.000; pita 200..12.000 → **114**, faktor **26,3**); R-311 butir 2 (0,15; pita
  0,02..0,45 → **0,4087**, **+172%**). **[v14] TIDAK mendapat kejadian kelima.**
  **DILARANG:** membaca kemenangan tipis mana pun — termasuk R-313 — sebagai bukti
  kalibrasi membaik. **Penangkalnya aturan 85**, berlaku mulai R-312, dan **masih belum
  punya satu pun adjudikasi**.
- **KC-52 [RESMI di STATE v54, DITUTUP pada giliran yang sama]** — **dua penyebut
  berbeda diperlakukan sebagai satu.** Rumusan resmi: ketika dua angka besar atas
  "semesta yang sama" tidak cocok, kemungkinan pertama yang wajib diperiksa bukanlah
  bahwa salah satunya keliru, melainkan bahwa keduanya **mencacah himpunan yang
  berbeda**. Selisih tak terjelaskan adalah dugaan tentang **batas himpunan**, bukan
  tentang mutu pengukuran. **[v14] Sebab strukturalnya terukur:**
  `kehidupan_arsip.peta_parquet` **melewatkan baris `parquet_karantina`**, sehingga
  kedua belas parquet tidak pernah masuk penyebut mana pun — benar secara kode, dan
  tidak pernah disebut di dokumen mana pun sebelum jurnal 140. **[v14] Kemunculan kedua
  tercatat: KC-52 hidup DI DALAM KODE**, pada docstring `selisih_lilin.py`. Kelas ini
  **DITUTUP sebagai teka-teki, TETAP HIDUP sebagai pola** — 19.586 lawan 19.598, **880
  lawan 877**, 18.799 lawan 17.398. Kerabat: KC-25, KC-36, KC-39, aturan 44.
- **KC berikutnya yang bebas: KC-53.**

## Papan skor prediksi — lengkap R-300..R-313 (R-199..R-299 di v4, blob `67dda29e`)

| # | Prediksi | Status |
|---|---|---|
| R-300 | (1) cacah_bulan 64; (2) tetangga BTCST HIDUP; (3) cacah_hidup 8..30 dan MATI>HIDUP | **SEPARUH** |
| R-301 | (1) tebing==0; (2) mati_tersisip ≥1; (3) bangkit==0 | **TIDAK TERADJUDIKASI** |
| R-302 | (1) simbol tersisip 1..10; (2) simbol-bulan 1..50; (3) penyebut 19.586/787 | **SEPARUH** (butir 2 MELESET 88>50) |
| R-303 | (1) simbol tersisip 1..60; (2) simbol-bulan 1..300; (3) penyebut/kendali/kode 0 | **TEPAT (3/3)** |
| R-304 | (1) mati_dulu 5..8; (2) hidup_berlubang 3..8; (3) penyebut/kendali/kode 0 | **MELESET** (1 dan 2 kalah) |
| R-305 | (1) bagian mati-tak-setelah-lubang dari ≥100 dalam 0.55..0.95; (2) cacah lubang-awal 20..120; (3) invarian + kendali + kode 0 + CI | **MELESET** — butir 1 KALAH (penyebut 118, bagian **1.0**, tautologis); butir 2 KALAH (**5**); butir 3 TEPAT (MUDAH) |
| R-306 | (1) bagian arah STRIKT dari penyebut ≥100 dalam 0.25..0.60; (2) cacah tebing 2025-07 dalam 20..90; (3) sembilan invarian + dua kendali + kode 0 + CI | **TEPAT (3/3)** — **0.339** (penyebut **118**); **39**; MUDAH |
| R-307 | (1) bagian byte MATI dalam 0.02..0.15; (2) cacah simbol-bulan ber-`byte_parquet` < 10.000 dalam 20..400; (3) sembilan invarian nol + dua kendali + kode 0 + CI | **MELESET** — **0.017704** tipis di bawah pita; **0** (ambang MUSTAHIL, KC-48); butir 3 MUDAH |
| R-308 | (1) cacah HIDUP ber-byte < 97.634 dari 18.087 dalam **20..600**; (2) cacah MATI ber-byte < 150.000 dari 1.401 dalam **10..300**; (3) invarian + kendali + kode 0 + CI | **SEPARUH** — **38** MENANG; **2** KALAH (KC-49, kasus pertama KC-51); butir 3 MUDAH |
| R-309 | (1) cacah baris HIDUP-kecil bulan PERTAMA atau tepi `2026-06`, dari 38, dalam **22..38**; (2) nisbah rata byte dalam **0.10..0.60**; (3) delapan invarian nol + dua kendali + kode 0 + CI | **TEPAT (3/3)** — **37** (0,973684); **0,527179**; MUDAH |
| R-310 | (1) cacah baris MATI berdefisit lilin, dari 1.401, dalam **1..120**; (2) bagian defisit bukan-pertama dalam **0.02..0.25**; (3) delapan invarian nol + tiga kendali + lima penggugur + kode 0 + CI | **TEPAT** — **9** (tipis ke tepi BAWAH); **0,0445** (tipis ke tepi BAWAH); MUDAH |
| R-311 | (1) cacah baris bukan-pertama bukan-MATI berdefisit, dari **17.398**, dalam **200 .. 12.000**; (2) bagian sisa 712.925 yang ditanggung SEPULUH teratas, dalam **0,02 .. 0,45**; (3) sepuluh invarian nol + tiga kendali + penggugur + kode 0 + CI | **SEPARUH** — butir 1 **KALAH** (**114**, lantai aritmetis 16); butir 2 **MENANG** (**0,4087**, tipis ke tepi ATAS, sisa 0,0413); butir 3 MUDAH |
| **R-312** | (1) cacah baris berselisih antara `cacah_lilin` dan `cacah_lilin_terbaca`, dari 19.586, dalam **12 .. 120**; (2) bagian selisih yang ditanggung baris teratas dalam **0,50 .. 0,865**; (3) penggugur + kendali + kode 0 + CI | **TIDAK TERADJUDIKASI** — `cacah_berselisih` **0**, penyebut butir 2 NOL (aturan 41). **[v14] Vonis DIPERBERAT:** butir 2 **mustahil dimenangkan secara struktural** — lihat di bawah. |
| **R-313** | (1) Σ `baris_karantina` atas delapan `reports/pulihkan_pecahan_<i>.json` = **516.135** (titik tunggal, selisih nol); (2) Σ parquet karantina = **12** (titik tunggal) | **TEPAT (2/2)** — **516.135** dan **12**, keduanya selisih **0**, dengan **cacat aturan 79 melekat permanen** |

**Total R-1..R-313** (dihitung tangan, aturan 21):

- TEPAT **218**
- MELESET **57**
- SEPARUH **22**
- TIDAK TERADJUDIKASI **9**
- MENUNGGU **7** (R-7, R-19, R-20, R-28, R-36, R-37, R-199)

218 + 57 = 275; 275 + 22 = 297; 297 + 9 = 306; 306 + 7 = **313** ✅ Nomor terpakai
R-1..R-313. N_percobaan = 0. **ADJUDIKASI RISET TETAP TERKUNCI.**
**[v14] Lajur TIDAK bergerak sejak v13** — tidak ada ramalan baru diadjudikasi.

**Nisbah papan skor, dihitung tangan dan disebut apa adanya:** dari 297 ramalan yang
beradjudikasi penuh (218 + 57 + 22), TEPAT **73,4%**, MELESET **19,2%**, SEPARUH
**7,4%**. Angka itu **DILARANG dibaca sebagai mutu ramalan**: sebagian besar butir
ketiga tiap ramalan berlabel MUDAH dan tidak berisiko. **R-312 DILARANG masuk pembilang
maupun penyebut nisbah ini.**

**Utang papan skor:** rincian R-236..R-247 masih di jurnal 92–94; R-229 TEPAT dan
R-230 MELESET (dari docstring) menunggu pemeriksaan R-224..R-235.

### [v14] R-312 — arah selisihnya mustahil, dan itu memperberat vonis

Docstring `selisih_lilin.py` (blob `d19bdb5f…`) mendefinisikan
`selisih = cacah_lilin_terbaca - cacah_lilin` dan menyatakan arah itu dipilih supaya
selisih bertanda **POSITIF** bila jumlah terbaca lebih besar. Tetapi
`kehidupan_arsip.ukur_kolom` memaksa **`cacah_lilin` = `cacah_lilin_terbaca` +
`cacah_baris_cacat`** dengan `cacah_baris_cacat` ≥ 0. Maka **selisih itu tidak akan
pernah positif pada baris mana pun**.

Akibatnya butir 2 — yang menimbang sepuluh baris berselisih **positif** terbesar —
**tidak dapat dimenangkan secara struktural**, dan itu benar **sejak sebelum pita
dikunci**. Rumusan lama ("kedua medan bukan pengukuran bebas") benar tetapi **kurang
keras**.

### Lima larangan permanen yang menempel pada R-312

1. **DILARANG** mengatakan pita butir 1 (12..120) "tidak terbantah". Ia tidak diuji.
2. **DILARANG** mengatakan kalibrasi membaik atau memburuk karena R-312.
3. **DILARANG** menghitungnya di pembilang maupun penyebut nisbah kemenangan.
4. **DILARANG** menghidupkannya kembali dengan alasan penjelasannya kini ditemukan.
5. Angka **12** di R-313 adalah cacah **parquet karantina** — arti berbeda dari 12 di
   R-312 butir 1. **Kesamaan itu DILARANG dibaca sebagai konfirmasi apa pun.**
   **[v14] ATRIBUSI DILENGKAPI — inilah kelalaian v13 yang diperbaiki:** larangan ini
   **berasal dari praregistrasi**, yaitu **syarat gugur nomor 3** di docstring modul dan
   jurnal 136, **bukan** dari adjudikasi.

### [v14] Kredit yang wajib diberikan kepada praregistrasi R-312

Docstring memuat **empat syarat gugur yang dikunci di muka**. Syarat 1 berbunyi bahwa
medan identik di seluruh baris menghasilkan **TIDAK TERADJUDIKASI (aturan 41), bukan
MELESET**. Maka vonis atas R-312 **bukan rasionalisasi pasca-hoc** — ia syarat gugur
yang terpicu persis sebagaimana dirumuskan. Disiplin proseduralnya hampir seluruhnya
benar: pita terkunci, lantai aritmetis dihitung, tiga tautologi dibuang tertulis, butir
MUDAH ditandai di muka. **Yang gagal satu hal saja: tidak ada yang memeriksa apakah
besaran yang diramalkan bisa ada.**

## Catatan kejujuran [v14]

1. **Aturan 79 TIDAK dilemahkan — catatan kejujuran v13 nomor 3 DICABUT.** v13 menulis
   "aturan 79 dilemahkan oleh R-313, dan itu diakui". ADR-A019 kep. 7 dan STATE v55
   membatalkan rumusan itu: **aturan yang dilanggar lalu disebut "lemah" adalah aturan
   yang sedang dihapus diam-diam.** Rumusan yang berlaku: aturan 79 **tetap PENUH**;
   praregistrasi di luar `journal/**` **tidak sah sebagai praregistrasi**; hasilnya tetap
   dicatat demi kejujuran riwayat, **cacatnya melekat permanen**, dan **penolakan pihak
   ketiga atas R-313 sah**. Yang lemah bukan aturannya, melainkan **kepatuhan kami** pada
   satu kejadian. **DILARANG** menyebut aturan 79 lemah, longgar, atau opsional.
2. **Tuduhan sendiri diperiksa dan diringankan.** Jurnal 141 menuduh EKOR v13 salah
   menyajikan larangan R-312 nomor 5. Dibaca dari sumber pada giliran ini, yang terjadi
   adalah **kelalaian atribusi**, bukan misrepresentasi — v13 diam soal asal-usul, tidak
   pernah mengklaim yang keliru. Membaca kesunyian sebagai klaim adalah bentuk kecil
   dari kesalahan butir 10.
3. **Utang aturan 52 terbesar LUNAS.** Ketiga berkas trio `c1dc0009` dibaca UTUH,
   **blob dicatat untuk pertama kalinya**: `selisih_lilin.yml`
   **`de2fd4fd346c9e13213fcc9a410d4aea8460d67a`** · `test_selisih_lilin.py`
   **`2d903a4a6f544eacd26b82bdb177680fa78bdffd`** · `selisih_lilin.py`
   **`d19bdb5fe67e0bd9c1b141d7fb7cc6dcd089c5f2`**. Cacah **36** butir `test_01`..`test_36`
   **terverifikasi dari sumber**; turunan **1341 + 36 = 1377** kini berdiri di atas
   pembacaan, bukan ingatan.
4. **Aturan 86 kini RESMI**, atas dua kejadian yang keduanya kerugian kami sendiri:
   biaya uji pemisah ditaksir empat langkah padahal **satu pembacaan** (jurnal 138 §4);
   dan `selisih_lilin` + 36 uji + satu workflow ditulis untuk angka yang **sudah
   tersimpan** di `reports/` sejak 29 Juli, **dua hari sebelum** pertanyaannya
   dirumuskan (jurnal 140 §7).
5. **Aturan 57 beruntun 4 dari 4, dan tidak bertambah.** Tidak ada berkas uji baru sejak
   trio. Lajur ini satu-satunya yang belum pernah kalah sejak putus di 26/27, dan
   satu-satunya alasan ia tidak dibanggakan adalah ia **mencacah, bukan menaksir**.
6. **Aturan 36 tetap memegang kasus terkuatnya:** `selisih_lilin` dan `pulihkan`
   bertemu di **839.325.999** sampai satuan terakhir, lewat dua jalur, dua modul, dua
   run, dengan jarak tiga hari.
7. **Kekalahan poros terbesar sesi ini, disebut telanjang:** R-312 berdiri di atas
   anggapan **tak terperiksa** bahwa dua medan bernama berbeda adalah dua pengukuran
   bebas. Tidak ada satu pun baris kode dibaca sebelum pita dikunci. Modul, 36 butir
   uji, dan satu workflow ditulis di atas anggapan itu — dan arah ramalannya ternyata
   **mustahil** sejak awal.
8. **`PROMPT_KELANJUTAN.md` tetap belum diberi kepala "ARSIP — BUKAN SUMBER"** dan
   `PROMPT.md` **v55 belum didorong**. Sampai itu dikerjakan, satu-satunya penjaga
   adalah larangan tertulis di STATE v52–v55 dan di berkas ini.
9. **Pemeriksaan silang yang menutup tanpa sisa** (terbitan, TIDAK diskor):
   18.799 − 1.401 = **17.398**; 18.087 − 17.318 = **769**; 98 − 80 = **18**;
   769 + 18 = **787** = `cacah_simbol`; **19.586 + 12 = 19.598**;
   **839.325.999 + 516.135 = 839.842.134**.

**Kesalahan proses [v14] — klaim v13 dikoreksi.** EKOR v13 menulis "tidak ada satu pun
kegagalan konektor". Itu tidak lagi benar: pada giliran push STATE v55, satu panggilan
`push_files` **ditolak** karena bungkus argumen tidak dipakai. **Ia bukan galat alat
maupun galat GitHub, melainkan kesalahan bentuk panggilan.** Tidak ada yang tertulis ke
repo, tip tidak bergerak, dan panggilan ulang berhasil — tetapi klaim "nol kegagalan"
tidak boleh dipertahankan hanya karena kerugiannya nol. Kerugian lain yang tetap
tercatat berasal dari urutan kerja: laporan CI run `30547842823` hangus, dan blob
laporan ke-38 tidak dapat dipulihkan.

## Jumlah uji

**1377 TERUKUR, kini LIMA bacaan berjejak.**

1. blob **`cdfdee2559201306a49bc9b01f1185d7aa36eebe`**: run **30559145901**, commit
   **`c1dc0009`** (trio `selisih_lilin`), 15:57:01Z, kode 0, `1377 tests collected in 0.58s`.
2. blob **`effb3a46bc20cda5c6c5910ee926aa16c195bb68`**: run **30575123865**, commit
   **`8368ca1f`** (STATE v54), 19:30:52Z, kode 0, `… in 0.54s`.
3. **[v14]** blob **`8cbbd4ce7b85d9e1f217a9cefbdacfb9318dec78`**: run **30576963781**,
   commit **`6642ed68`** (EKOR v13), 19:56:30Z, kode 0, `… in 0.67s`.
4. **[v14]** blob **`8ec97de5af8b528276174f635e3bda9e6cc2d7ef`**: run **30577779309**,
   commit **`2bdd8233`** (UKUR v13), 20:07:50Z, kode 0, `… in 0.62s`.
5. **[v14]** blob **`94d270e7065218f87bd5a26c5113ed8346cf6abf`**: run **30579348728**,
   commit **`cd209f3e`** (STATE v55), 20:29:25Z, kode 0, `… in 0.61s`.

Turunan: 1341 + **36** butir `tests/test_selisih_lilin.py` = **1377** ✅ (aturan 21),
**kini terverifikasi dari sumber**, bukan dari ingatan.

Riwayat panjang: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 →
984 → 1044 → 1100 → 1168 → 1233 → 1297 → 1341 (enam run) → **1377** (lima run berjejak).

Cacah per berkas uji (**milik repo riset ini — bukan repo warisan**):
`test_irisan_byte.py` **68** · `test_bulan_pertama.py` **65** ·
`test_keterisian_lilin.py` **64** · `test_bentangan_kohort.py` V2 **63** (dicacah
TANGAN, `test_01`..`test_63`) · `test_lubang_tebing.py` **60** ·
`test_sebab_bangkit.py` **57** · `test_byte_semesta.py` **56** ·
`test_lubang_awal.py` **48** · `test_tersisip_semesta.py` **47** ·
`test_anatomi_tengah.py` **47** · `test_sisa_defisit.py` **44** (dicacah TANGAN) ·
**`test_selisih_lilin.py` 36** (dicacah TANGAN dari sumber, `test_01`..`test_36`;
dua helper berawalan garis bawah TIDAK dikumpulkan pytest) · `test_terhenti.py` V4
**33** · `test_bulan_absen.py` **32** · `test_karantina_semesta.py` **28** ·
`test_silang_settled.py` **24** · `test_ukur_baris.py` **3**.

**Aturan 57: beruntun 4 dari 4** sesudah putus di 26/27. Hanya push yang menyentuh
`tests/**` yang dihitung.

### ORDINAL ATURAN 38 — buku besar, kini sampai ke-49

**Definisi yang berlaku (ADR-A018 kep. 8):** pemakaian dihitung **hanya** untuk
pembacaan `reports/ci_terakhir.json` yang meninggalkan **jejak tertulis** berupa nomor
run + commit + blob di STATE, lampiran, atau jurnal. Pembacaan tanpa jejak tidak masuk
buku besar dan karena itu tidak boleh dihitung.

| ke- | CI | run | commit | blob | jejak |
|---|---|---|---|---|---|
| 43 | 1341 | 30550547017 | `1247a5a3` | `fdb7c668` | STATE v53 |
| 44 | 1341 | 30551789395 | `33a4ab37` | `5b16417b` | jurnal 136 |
| 45 | 1377 | 30559145901 | `c1dc0009` | `cdfdee25` | jurnal 137, STATE v54 |
| 46 | 1377 | 30575123865 | `8368ca1f` | `effb3a46` | EKOR v13 |
| 47 | 1377 | 30576963781 | `6642ed68` | `8cbbd4ce` | jurnal 141, STATE v55 |
| 48 | 1377 | 30577779309 | `2bdd8233` | `8ec97de5` | jurnal 141, STATE v55 |
| **49** | **1377** | **30579348728** | **`cd209f3e`** | **`94d270e7`** | **berkas ini** |

**Pemakaian berjalan = ke-empat puluh sembilan.** Pemakaian ke-49 dibaca
**2026-07-30T20:29:25Z**, kode keluar **0**, atas push STATE v55 — **dibaca sebelum
tertimpa**, sehingga ramalan "CI tetap 1377" untuk push itu **TERUKUR dan TEPAT**,
tetap **MUDAH**, tetap tidak diskor.

**[v14] Delapan pembacaan berturut (ke-42..ke-49) tanpa satu pun laporan hangus.**

**Dua cacat tetap disebut apa adanya:** baris ke-**38** (run `30541051907`, CI 1297,
commit `5d7d8b96`) **tanpa blob**, tidak dapat dipulihkan — ordinal ini karena itu sah
**relatif terhadap definisi di atas**, bukan sebagai pencacahan mutlak; dan run
**30547842823** (bot `de2fc03d`) **tidak pernah dibaca**, sudah tertimpa, **DILARANG
dihitung**, ramalannya **DILARANG diklaim menang**. Bila jejak pembacaan lain ditemukan
di jurnal 133–134, nomor ini **WAJIB dikoreksi, bukan dipertahankan**.

**Calon aturan** — dua push akar berturut tanpa membaca laporan di antaranya pasti
menghanguskan yang pertama — **DITOLAK diresmikan** oleh ADR-A019 kep. 3: masih **satu**
kejadian.

## Utang verifikasi

1-5, 11 menunggu tahap juri. 6-23, 25-29, 31 LUNAS. **Nomor utang BUKAN nomor ramalan
— KC-32.**

24. **AKTIF. LUNAS BARU [v14]:**
    - **Ketiga berkas trio `c1dc0009` dibaca UTUH** pada ref `e6007ba5`, blob dicatat
      (lihat catatan kejujuran 3). **Utang (a) v13 LUNAS PENUH.**
    - **`decisions/ADR-A019.md` dibaca UTUH** sesudah push — blob
      **`9cd7d25e7a61207343e60233887d06b441aa3cbf`**, commit `e6007ba5`.
    - **`journal/2026-07-30-141.md` dibaca UTUH** — blob
      **`bde76db952f587f4df4529e49f0015c13a29919b`**, commit `1b970da5`.
    - **`STATE.md` v55 dibaca UTUH** — blob **`be6bc652…`**, commit `cd209f3e`.
    - **EKOR v13 dibaca UTUH** pada giliran ini — blob `26ba6dc0…`.
    - `reports/ci_terakhir.json` (`8cbbd4ce`, `8ec97de5`, `94d270e7`) dibaca utuh,
      blob DICATAT.
    **TETAP BELUM:** `decisions/ADR-A002`, **A004**, **A006**, **A007**, **A008**;
    `.github/workflows/karantina_semesta.yml` (`de40fa4e`); `tests/test_pulihkan.py`
    (`11c43533`); `tests/test_rilis_karantina.py` (`739c8da9`);
    `tests/test_karantina_a006.py` (`a5a3d82f`). **BARU:** UKUR v13 belum dibaca ulang
    sesudah ADR-A019 — wajib dibaca utuh sebelum UKUR v14 ditulis.
30. **AKTIF — UTANG HIDUP, dan ADR-A019 kep. 8 MENOLAK menutupnya.** Angka
    **50 / 54 / 45** tetap **TURUNAN** dan **DILARANG dikutip sebagai terukur** sampai
    dicacah satu per satu bernomor (aturan 66, KC-33). Yang sah tetap
    **49 / 53 / 44 / 18** pada ref `3196fd98` dan `8a614567`. Alasan penolakan:
    menuliskannya sebagai "cacah baru" berarti mengarang pengukuran di dalam dokumen
    yang justru meresmikan larangan mengarang.
32. **AKTIF — tiga butir "memerlukan verifikasi" `PETA_MODUL.md`** (repo **WARISAN**),
    utang terbuka, bukan fakta: (a) `enable_hs` tidak ditemukan di `config.py` padahal
    dipakai `strategy.py`; (b) klaim "30 pair dipilih alfabetis"; (c) klaim "kendala
    mengikat = kapasitas margin".
33. **AKTIF LAGI [v14]** — daftar kesalahan dokumen bertambah menjadi **sebelas**;
    butir 11 lunas di STATE v55 dan diadili dari sumber di berkas ini.
34. **AKTIF — `PROMPT_KELANJUTAN.md` belum diberi kepala "ARSIP — BUKAN SUMBER"**, dan
    **`PROMPT.md` v55 belum didorong.**
35. **LUNAS [v14]** — UKUR v13 sudah naik (commit `2bdd8233`, blob `9e71c1ee…`).
    **Digantikan utang baru:** UKUR **v14** belum naik; sampai itu, UKUR v13 tertinggal
    satu versi (lihat keserasian di kepala).
36. **AKTIF — identitas dua belas simbol-bulan karantina belum pernah didaftar.**
    Cacah dan barisnya terukur (12 parquet, 516.135 baris), tetapi **nama simbol dan
    bulannya tidak diketahui**. Selama itu, kalimat apa pun tentang *jenis* instrumen
    yang dikarantina **DILARANG**.
37. **BARU [v14] — `ukur_baris.py` V6 belum ditulis.** `BERKAS_DIUKUR` masih **21** nama
    atas ~50 modul dan ~54 berkas uji; pagar 800 baris belum pernah diuji atas ~29
    modul yang lebih baru.

## Daftar ADR

- **ADR-A001** aturan dasar. DITERIMA.
- **ADR-A002** serapan. Kondisi v3 berlaku; §10 tetap tidak boleh diubah.
- **ADR-A003** taksonomi rezim. BELUM ADA.
- **ADR-A004** kebijakan KC-6. DITERIMA.
- **ADR-A005** jenis instrumen. DITERIMA.
- **ADR-A006** karantina + persistensi. DITERIMA, TERVERIFIKASI.
- **ADR-A007** serapan hibrida. DIUSULKAN, belum diterima.
- **ADR-A008** akibat KC-18. Keputusan 1–6 DITERIMA. **Keputusan 7 DITANGGUHKAN.**
- **ADR-A009** (`17a594b6`). **DICABUT PENUH oleh ADR-A012.**
- **ADR-A010** (`c4bccf21`) — klaim "kebangkitan tunggal" DICABUT. DITERIMA.
- **ADR-A011** (`645fd5df`) — arah sebab A009 dicabut untuk kelas bangkit. DITERIMA.
- **ADR-A012** (`f9f564d1`) — arah sebab dicabut untuk SELURUH semesta. DITERIMA.
- **ADR-A013** (`8ba4f989`) — (2) dan (4) kini aturan **80** dan **81**. DITERIMA.
- **ADR-A014** (blob `6d77c2cd`) — byte parquet; (5) melahirkan KC-48. DITERIMA.
- **ADR-A015** (blob `387d5510`) — delapan keputusan; (5) besar berkas bukan detektor
  status ke arah mana pun — **TIDAK dibalik oleh R-310, R-311, R-313, A018, maupun
  A019**. DITERIMA.
- **ADR-A016** (blob `209802d7`) — H-A019 diterima TERBATAS; kep. 4 **DIKOREKSI oleh
  A018 kep. 6**. DITERIMA.
- **ADR-A017** (blob `1be570f2`) — sebelas keputusan; kep. 4 mencatat selisih
  **516.135** sebagai koreksi resmi. Kep. 4 **TERJAWAB PENUH oleh R-313**: selisih itu
  bukan cacat, melainkan batas himpunan. Rumusan A017 kep. 4 tetap benar sebagai
  peringatan; tafsirnya yang menyiratkan salah satu angka bermasalah **gugur**.
  DITERIMA.
- **ADR-A018** (blob `3fba599e`) — dua belas keputusan; (1) KC-51 diresmikan;
  (2) aturan 85 berlaku mulai R-312; (3) rumusan resmi R-311; (4) aturan 81 tidak
  terpicu; (5) H-A021 diusulkan; (6) A016 kep. 4 dikoreksi; (7) koreksi aturan 38;
  (8) definisi ordinal; (9) `PROMPT_KELANJUTAN.md` arsip; (10) dua cacah `tests/`;
  (11) cacah tangan 49/53/44/18; (12) poros R-312 ditetapkan. DITERIMA.
  Kep. 12 **SELESAI**: poros (b) dijawab tuntas lewat R-313.
- **ADR-A019 — ADA [v14]** (blob **`9cd7d25e7a61207343e60233887d06b441aa3cbf`**, commit
  **`e6007ba5`**, dibaca ulang UTUH pada giliran yang sama). **Sepuluh keputusan:**
  (1) **KC-52 DIRESMIKAN** dengan rumusan tunggal dan tabel tiga angka berpenyebut;
  sebab strukturalnya `peta_parquet` melewatkan `parquet_karantina`; mencabut sirat
  A017 kep. 4 **dan** pemisahan satuan STATE v53;
  (2) **Koreksi 9 diakui sebagai kelas cacat TANPA PENANGKAL** — satu-satunya butir
  yang bukan salah ketik; aturan 52 menangkap **satu dari delapan**;
  (3) **Aturan 86 DIRESMIKAN**; calon aturan "dua berkas akar berturut" **DITOLAK**
  karena kejadiannya masih satu;
  (4) **R-312 TIDAK TERADJUDIKASI selamanya** + lima larangan permanen; aturan 85
  dinyatakan belum terbukti bekerja maupun gagal; syarat praregistrasi baru: kebebasan
  medan wajib diperiksa terhadap kode;
  (5) **R-313 TEPAT (2/2)** dengan cacat aturan 79 melekat permanen dan penolakan pihak
  ketiga dinyatakan sah;
  (6) **H-A022 TERBUKTI** dengan batas tafsir; turunan `cacah_baris_cacat` = 0 di
  seluruh semesta; aturan 36 kasus terkuat;
  (7) **Aturan 79 DIRUMUSKAN ULANG, bukan dilemahkan**;
  (8) **utang cacah tangan aturan 66 DITOLAK ditutup**; `ukur_baris` V6 tetap utang;
  (9) urutan poros resmi + tujuh syarat kumulatif praregistrasi R-314;
  (10) utang aturan 52 atas trio `c1dc0009` ditetapkan **peringkat pertama** — dan
  **sudah dilunasi** pada giliran yang sama. DITERIMA.
- **ADR-A020 [BELUM ADA]** — calon isinya: hasil poros lubang tengah `2022-05` /
  `2024-05` (H-A020 dan H-A021), atau identitas dua belas simbol-bulan karantina.
  **DILARANG disusun pada giliran yang sama dengan adjudikasi** (ADR-A016).

## Temuan sampingan

**Karantina, terukur penuh** (kedelapan `reports/pulihkan_pecahan_<i>.json`, ref
`a2c4b83c`; `pulihkan` VERSI 2, `run_id_sumber` **30396803601**, ditulis
2026-07-29T02:48Z):

| pecahan | `baris_karantina` | parquet | blob laporan |
| --- | --- | --- | --- |
| 0 | 130.605 | 3 | `2e738ea33cf6b00544e685ca8137b215b2f301ae` |
| 1 | 131.760 | 3 | `9ddfb994eee11a81024dca97a4a0b0ab6785b098` |
| 2 | **0** (`karantina: null`) | 0 | `6f83de7e0f0b9e455cb5d66692074dcb9d2cd1a4` |
| 3 | 42.585 | 1 | `ce5d47b5ca99d56b5758a7f18cb64836221e0947` |
| 4 | 43.590 | 1 | `6b50a6571b560d2c96338898a8e859d01fc48e81` |
| 5 | **0** (`karantina: null`) | 0 | `b09913fd73e07ee293927b82a621b12589cce8e5` |
| 6 | 123.630 | 3 | `5d3f29ccb8181028030bed9e2fcc6f0d789a4150` |
| 7 | 43.965 | 1 | `dcd891af10b782c7c9fa2787403865097abc8856` |
| **jumlah** | **516.135** | **12** | — |

- **Mutu bukti:** kedelapan `pulih_sah` **true**; `cacah_sha_tak_cocok`,
  `cacah_bagian_hilang`, `cacah_anggota_kurang`, `cacah_anggota_tak_aman`,
  `selisih_baris_total` seluruhnya **0**; `baris_terverifikasi` true.
- **Sidik kode seragam** `76c27e3ce5d6edb13bb998b6ec65b538fb3d25205d4469bd4d186a95fa62d700`;
  **sidik kode manifes seragam** `237ccf427faf9d48e9c0904433a56e8902de64de6552daee5d3053093bfba601`
  → penjumlahan lintas pecahan **sah** (aturan 22).
- **Aturan 46 terbukti bekerja:** pecahan 2 dan 5 melaporkan
  `definisi_dapat_dibedakan` **false** dan menolak memilih definisi, alih-alih
  mengarang. Enam pecahan lain melaporkan `definisi_jumlah_baris` = "baris lolos +
  baris karantina".
- **Sebaran sangat tidak rata** — 42.585 sampai 131.760 baris per tar. Rata-rata
  **43.011** boleh dikutip sebagai turunan, **bukan sebagai bukti**.
- **Nama tar karantina:** `pecahan_<i>_karantina.part01.tar`.

**[v14] `selisih_lilin` V1 — kini dibaca dari sumber** (blob `d19bdb5f…`, commit
`c1dc0009`; laporan ringkas blob `e5cc64011030cfb8e1a8edf3699dd01b3caafab7`, sidik kode
`e6c77965…257e7`, `byte_sumber` 6.834): `cacah_baris` **19586** · `cacah_berselisih`
**0** · `jumlah_klaim_langsung` = `jumlah_terbaca_langsung` = **839325999** ·
`dua_jalur_bertemu` **true** · `selisih_terhadap_warisan` = {klaim 0, terbaca −516135,
bersih −516135} · `uji_r312.teradjudikasi` **false** · `bagian_teratas` null ·
`sebaran_kelas` `{}` · kode keluar alur modul **2** — **dirancang**, sebab `kode_keluar`
mengembalikan 2 bila `cacah_berselisih <= 0`.
**Empat kendali terbaca dari kode dan seluruhnya lolos:** `kendali_deteksi` (jawaban
dihitung TANGAN, 11 medan: klaim langsung 213.480 · terbaca 214.360 · bersih 880 ·
positif 1.080 · negatif 200 · berselisih 3), `kendali_nol`, `kendali_negatif` (menuntut
bersih **−250**), `kendali_teratas` (bagian **0,9615** = 7.500/7.800). Tetapan lain:
`BATAS_BARIS_LAPORAN` 40 · `CACAH_TERATAS` 10 · `AMBANG_HIDUP_KECIL` 97.634 ·
`INVARIAN` 8 kunci · `BERKAS_DICAP` **4** nama.

**[v14] Pola workflow trio TERVERIFIKASI dari `selisih_lilin.yml`** (blob
`de2fd4fd…`): `on.push.paths` **satu entri**, `permissions: contents: write`, job
`ukur` di `ubuntu-latest`, checkout@v4 + setup-python@v5 (3.11),
`pip install numpy pandas pyarrow pyyaml`, langkah `jalan` dengan `set +e` → `KODE=$?`
→ `echo "kode=$KODE" >> "$GITHUB_OUTPUT"` → `exit 0`, langkah `catat status`, langkah
`dorong laporan` (`[skip ci]`, `git pull --rebase`), penutup
`exit ${{ steps.jalan.outputs.kode }}`. **Aturan 55 LUNAS untuk berkas ini.**

**[tetap berlaku] `sisa_defisit` V1** (run 30542217951, laporan ringkas blob
`91a05c05`, sidik kode `6211624b…f044b0`): penyebut kerja **17.398** (HIDUP 17.318 +
SEPI 80) · `cacah_berdefisit` **114** (HIDUP 111, SEPI 3, MATI 0; **0,66%**) ·
`cacah_calon_penuh` **17.284** · `defisit_calon` **712.925** (tautologis, KC-50) ·
`defisit_teratas` **291.379**, `bagian_teratas` **0,4087** · `defisit_terbesar`
**42.510** = **TLMUSDT 2023-03**, HIDUP, 2.130 dari 44.640 lilin (**95,2% kosong**) ·
sepuluh teratas tersebar di **tujuh bulan** → aturan 81 TIDAK terpicu · pasangan
`2022-05`: ANCUSDT **26.959** dan LUNAUSDT **26.950**, berselisih **sembilan lilin**
(dasar **H-A021**; kalimat sebab apa pun **DILARANG**).

**`keterisian_lilin` V1:** jumlah lilin semesta LANGSUNG **839.325.999** ·
`cacah_baris_tanpa_lilin` 0 dari 19.586 · MATI penuh **1.392**, tak penuh **9** ·
defisit semesta **18.143.601** dengan **17.335.439 (95,5%)** di bulan pertama dan
**808.162** di bukan-pertama (bagian **0,0445**) · bulan pertama rata terisi
**≈49,7%** · kesembilan baris MATI tak penuh (LENDUSDT 2020-11 13.475 · FRONTUSDT
2024-09 14.986 · FOOTBALLUSDT 2024-05 39.308 · ANTUSDT 39.309 · BTSUSDT 39.310 ·
SRMUSDT 39.311 · HNTUSDT 39.312 · TOMOUSDT 39.315 · COCOSUSDT 39.317; jumlah
**95.237** = 0,1178 dari 808.162) · harga TIDAK tersimpan (**14** medan).

**`bulan_pertama` V1:** 37 dari 38 baris HIDUP-kecil adalah bulan pertama (0,973684);
satu-satunya yang bukan **TLMUSDT 2023-03**; nisbah rata byte **0,527179**.

**`irisan_byte` V1:** di zona 22.440–97.634 byte ada **38 HIDUP dan 0 MATI**; total
byte **32.706.262.375**; HIDUP 32.049.492.952 · SEPI 77.728.024 · MATI 579.041.399 ·
`cacah_lain` 0.

**`lubang_tebing` V1:** `mati_dulu` **40** (0.339) · `serempak` **78** (0.661) ·
`lubang_dulu` **0**; tebing `2025-07` menguasai 39 dari 40 `mati_dulu`, satu-satunya
bukan-tebing **BTCSTUSDT** (KC-47); **122** dari 787 simbol pernah berlubang funding;
delapan simbol bangkit berjumlah 88.

**Belum diukur, urut prioritas resmi (ADR-A019 kep. 9):**
(1) **lubang tengah gugus `2022-05` dan `2024-05`** — menguji **H-A020 dan H-A021
sekaligus**; poros tunggal berprioritas tertinggi;
(2) **identitas dua belas simbol-bulan karantina** — kandidat **termurah**, manifesnya
sudah ada di repo; **aturan 86 berlaku penuh di sini**;
(3) **irisan 880 lawan 877 lubang funding** — kandidat KC-52 berikutnya;
(4) **sebab kekosongan TLMUSDT 2023-03** (95,2% kosong, HIDUP);
(5) apakah "bulan pertama di penyebut" = "bulan pertama di bursa";
(6) tebing funding `2025-07` (39 simbol) dan BTCSTUSDT;
(7) selisih 40−38 `diagnosa_kc15`; hari hilang BNXUSDT 2022-04/06/08; bentangan 38
kohort; H-A016; mati_tersisip atas 19.586; **`ukur_baris` V6**; R-7/19/20/28/36/37 dan
R-199; R-236..R-247 dari jurnal 92–94; taksonomi lubang tiga kelas.

## Penomoran berikutnya

Aturan resmi **1–81, 83, 84, 85, 86** · usulan **77**, **78**, **82** · **aturan
berikutnya yang bebas 87** · KC resmi sampai **KC-52** (KC-16 kosong selamanya; KC-52
ditutup pada giliran ia diresmikan) · **KC berikutnya KC-53** · Hipotesis terbuka
H-A016 (belum diuji), H-A017 (dilemahkan R-306), H-A018 (tafsir dibatasi A014/A015),
H-A019 (DITERIMA TERBATAS, DILEMAHKAN A018 kep. 6 tanpa pengganti), **H-A020
(DIUSULKAN, belum diuji)**, **H-A021 (DIUSULKAN, belum diuji)**, **H-A022 (TERBUKTI
lewat R-313, dengan batas tafsir A019 kep. 6)** · Hipotesis berikutnya **H-A023** ·
Jurnal berikutnya **142** · `STATE.md` berikutnya **v56** · EKOR berikutnya **v15** ·
**UKUR berikutnya v14 (utang hidup, tertinggal satu versi)** · PROMPT berikutnya **v55
(belum didorong)** · ADR berikutnya **A020** · Ramalan berikutnya **R-314** · papan skor
**313**.
