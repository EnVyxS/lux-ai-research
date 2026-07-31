# STATE lampiran EKOR — bagian 2 dari STATE (v19, milik STATE v60)

**Mengapa berkas ini ada.** Dua push `STATE.md` berturut terpotong (v41, v42);
pemecahan ke tiga berkas berlaku sejak v43 (KC-42). Pembagian yang berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, 83, 84, 85, 86, 87, **90**;
   KC-1..**KC-55** resmi, **KC-56 dan KC-57 diusulkan**.
2. **`STATE_LAMPIRAN_EKOR.md`** (berkas ini, v19) — bagian 2: papan skor, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** — bagian 3: pengukuran, modul, API, hipotesis, koreksi.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) dan **`PROMPT_KELANJUTAN.md`**
   (blob `35beed44`) — **arsip; BUKAN sumber** (ADR-A018 kep. 9).

Dasar v19: EKOR v18 (blob **`217beaeebd367309ea1a4a4d5ea3234887788b2b`**, commit
**`bb565f4cb2bc0ef8d7b2c72ece8f835c74613422`**), **dibaca UTUH pada giliran yang sama
sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43).

**Apa yang v19 kerjakan — dan ini kebalikan v18.** v18 sengaja tidak menggerakkan satu
pun lajur. v19 menggerakkan **dua ramalan penuh sekaligus**: **R-317** (2 TEPAT, 2
MELESET) dan **R-318** (**4 TEPAT dari 4 butir berskor**). Papan skor naik dari **321**
ke **329** dan **DISAHKAN di sini**. Selain itu v19 membukukan: **aturan 90 RESMI**
beserta tabel tiga kejadiannya, **kesalahan dokumen butir 18**, **usulan KC-57 dan
KC-58**, **usulan aturan 91**, **tiga baris baru buku besar aturan 38 (ke-62, ke-63,
ke-64)**, **pelunasan utang 40 dan 44**, dan **tiga utang baru (utang ukur 25, utang
verifikasi 45 dan 46)**.

## KESERASIAN VERSI — dibaca apa adanya, termasuk yang belum serasi

Saat berkas ini didorong:

- `STATE.md` **v60** — blob **`d3f1448fad4ead804be59b1bbb1562b460f01621`**, commit
  **`8345668e9a8f0e01bcbe86fd9d0f60f4709fd834`**, dibaca ulang UTUH pada giliran yang
  sama ia didorong. **SERASI** dengan berkas ini pada aturan, KC, dan butir 18 — tetapi
  **TIDAK serasi pada papan skor**: STATE v60 memuat **325**, berkas ini memuat **329**.
  Sebabnya tersurat: **R-318 diadjudikasi di jurnal 151, sesudah STATE v60 didorong.**
  **Sumber sah untuk papan skor adalah berkas ini** (aturan 29: pengesahan terjadi di
  lajur EKOR). Ketidakserasian ini **WAJIB dipulihkan oleh STATE v61**.
- `STATE_LAMPIRAN_EKOR.md` **v19** — berkas ini.
- `STATE_LAMPIRAN_UKUR.md` masih **v18** — blob
  **`11b14975a7ee2b00ca5e25ca19fc4e16ad5c1deb`**, commit
  **`51c65e2afea4364a855e68c8f84465d1a2efcac9`**. **TERTINGGAL DUA VERSI ISI.**
  Kepalanya berbunyi "milik STATE v59". Ia **tidak memuat**: pembacaan
  `reports/lubang_awal.json`; kelas batas **pemotongan oleh MODUL**; tabel
  `baris_penyebut_butir_2`; penanda **EKSKLUSIF** pada tabel H-A010 (butir 18);
  aritmetika 50 − 48 = 2 dan 9 − 7 = 2; pembacaan `bulan_absen.py`; dan **seluruh isi
  `bulan_absen_ringkas.json`** yang dibuka pada giliran R-318.
  **Sampai UKUR v19 naik, sumber sah untuk seluruh butir itu adalah `STATE.md` v60,
  jurnal 149, jurnal 151, dan berkas ini** — bukan UKUR v18.

**Satu berkas per push tetap MENGIKAT** (KC-42, KC-43).

**Tentang push berkas ini:** ia di akar repo sehingga menyalakan `ci.yml`. Tidak satu
pun `tests/**` berubah, jadi cacah uji tetap **1377** — ramalan deterministik, **MUDAH**,
TIDAK diskor, TIDAK menambah beruntun aturan 57. **Laporannya WAJIB dibaca sebelum push
akar berikutnya** (pemakaian aturan 38 **ke-65**), dan **WAJIB ditolak bila medan
`commit` tidak cocok** (aturan 90).

## KESALAHAN DOKUMEN SENDIRI — kini DELAPAN BELAS

Daftar ini disalin dari STATE v60 dan berlaku identik di ketiga bagian. Sebab tetap
sama setiap kali: `push_files` menulis ulang SELURUH berkas, sehingga memperbaiki satu
karakter berarti menyusun ulang berkas besar dari konteks terpakai — persis yang
dicatat KC-42 sebagai cara paling pasti merusaknya.

Butir 1–15 seperti EKOR v17 (blob `29981b68`), seluruhnya LUNAS; teksnya tidak diulang.

| # | berkas | tertulis | seharusnya | status |
| --- | --- | --- | --- | --- |
| 16 | jurnal 146 §5, pita butir 3 R-316 | pita **dua sisi** | ruang nilainya **tiga sisi**; **51** yang terukur | LUNAS di STATE v58 |
| 17 | STATE v58, aturan 38 | "**Tujuh belas** pembacaan berturut (ke-42..ke-57)" | 57 − 42 = 15; 15 + 1 = **enam belas** | LUNAS di STATE v59 |
| **18** | **lampiran, tabel H-A010** | kolom akhir lubang awal memakai batas **EKSKLUSIF** (bulan pertama yang TIDAK berlubang) | medan sumber `akhir_lubang_awal` **INKLUSIF**; selisih tepat **+1** pada **lima dari lima** baris | **LUNAS di STATE v60** |

### [v19] Butir 18 — tabel buatan sendiri yang menipu pembuatnya

Lima baris, lima kali salah arah yang sama, selisih tetap **+1**:

| simbol | tertulis di tabel H-A010 (EKSKLUSIF) | `akhir_lubang_awal` sejati (INKLUSIF) |
| --- | --- | --- |
| BNXUSDT | 2023-02 | **2023-01** |
| ICPUSDT | 2022-09 | **2022-08** |
| JUPUSDT | 2024-02 | **2024-01** |
| QTUMUSDT | 2020-03 | **2020-02** |
| TLMUSDT | 2023-03 | **2023-02** |

**Akibat terukur:** butir 3 R-317 meramalkan `akhir_lubang_awal` BNXUSDT = **2023-01**
dengan membaca tabel sendiri sebagai 2023-02 — lalu **kalah**, karena terukur
**2023-01**… tidak, dan justru di situ letak yang memalukan: ramalannya menyebut
**2023-01** sebagai jawaban tabel-dikurangi-satu yang salah kaprah, dan pengukuran
memberi **2023-01** sebagai nilai sejati sementara jurnal 149 menskor butir itu MELESET
terhadap **2023-02** yang dikutip dari tabel cacat. **Kekalahan itu TIDAK dibatalkan.**
Aturan 29 dan ADR-A016 melarang mengubah vonis sesudah sebabnya dipahami; yang boleh
dilakukan hanyalah **mencatat sebabnya**, dan itulah butir 18.

**Pola koreksi resmi bertambah satu bentuk, dan bentuk ini yang paling licin sejauh
ini:** *kolom ringkasan buatan sendiri yang batasnya bergeser satu satuan dari medan
sumbernya.* Ia lolos karena **angkanya benar semua** — yang salah hanya **konvensi
batas**, dan konvensi tidak pernah dibaca ulang.

**Yang DILARANG:** mengutip tabel H-A010 di lampiran sebagai nilai `akhir_lubang_awal`.
Sumber sah hanya `reports/lubang_awal.json`.

### [v19] Mengapa KC-57 TIDAK diresmikan walau lima baris cocok

Godaannya besar: lima dari lima adalah kecocokan sempurna. Tetapi kelimanya berasal
dari **satu kolom pada satu tabel** — **satu cacat yang tampak lima kali**, bukan lima
pengamatan bebas. Meresmikan KC-57 atas dasar itu adalah **KC-47 persis**, dilakukan di
dalam berkas yang mendefinisikan KC-47.

> **KC-57 [DIUSULKAN di STATE v60].** Tabel ringkasan yang disusun tangan dapat memakai
> **konvensi batas** yang berbeda dari medan sumbernya; kecocokan angka tidak menjamin
> kecocokan konvensi. **Penangkal:** setiap kolom tabel buatan sendiri WAJIB menyebut
> nama medan sumbernya dan konvensinya (inklusif/eksklusif) di kepala kolom.

Diresmikan **hanya** pada kejadian kedua yang berasal dari **tabel lain**.

### Batas kekuatan aturan 52 — rumusan yang berlaku

> Pembacaan ulang **dokumen sendiri** lemah terhadap penalaran cacat: ia membaca
> kalimat yang sudah diyakini benar. Pembacaan **kode** kuat terhadapnya: kode
> menyatakan identitas yang tidak dapat ditawar.

**[v19] Bukti keenam, dan ia lebih tajam daripada bukti kelima:** butir 18 lolos dari
seluruh pembacaan ulang sejak tabel H-A010 disusun, karena **setiap angkanya benar**.
Yang menangkapnya bukan pembacaan dokumen melainkan **pembacaan `reports/lubang_awal.json`
— sumber di luar dokumen**. Bukti kelima (butir 17) ditangkap oleh aritmetika tangan;
butir 18 tidak dapat ditangkap dengan cara itu sama sekali, sebab tidak ada aritmetika
yang salah. **Hanya sumber luar yang menangkapnya.**

**[v19] Bukti balik yang jujur:** pada giliran R-318, aturan 86 (b) dipakai lebih dulu
— `lux_ai/serapan/bulan_absen.py` dibaca UTUH **sebelum** laporannya dibuka. Itulah yang
menghasilkan tiga hal sekaligus: kepastian bahwa modul itu **tanpa pembatas baris**
(sehingga `baris_berabsen` lengkap), definisi resmi medan `bulan_absen` **disalin**
(KC-54 ditangkal), dan pengetahuan bahwa **tepi tidak pernah absen menurut definisi**
(sehingga 2022-04 mustahil muncul, dan pita butir 1 dikunci dengan sadar). **Pembacaan
kode bekerja lagi, preventif, untuk kedua kalinya berturut.**

## KC-43..KC-55 resmi, KC-56 / KC-57 / KC-58 usulan

(teks lengkap KC-43..KC-47 di STATE v47, KC-49 di v48, KC-50 di v50, KC-51 di v52,
KC-52 di v54, KC-53 di v56, KC-54 di v57, KC-55 di v58)

- **KC-43** — tanda tangan fungsi dari INGATAN.
- **KC-44** — semua laporan di-commit satu langkah.
- **KC-45 [RESMI v45]** — satuan "bulan tanpa funding" vs "bulan MATI" dicampur.
- **KC-46 [RESMI v45]** — lubang bentuk AWAL dibaca sebagai "funding berhenti".
- **KC-47 [RESMI v46]** — satu peristiwa menyamar sebagai banyak pengamatan bebas.
  **[v19] Terpicu DUA kali dan ditahan DUA kali:** (a) lima baris tabel H-A010 → KC-57
  ditahan; (b) empat butir TEPAT R-318 → dinyatakan **berkorelasi**, bukan empat bukti
  bebas, sebab butir 1, 3, dan 4 semuanya turun dari satu aritmetika (bentangan 50).
- **KC-48 [RESMI v47]** — ambang absolut pada sebaran yang belum diukur.
- **KC-49 [RESMI v8 lampiran ini]** — pita dikunci tanpa aritmetika implikasi.
  **[v19] Dipakai lagi:** blok `uji_r288` di dalam laporan menyatakan sendiri R-288
  kalah. **Vonis alat BUKAN adjudikasi.** Papan skor tidak disentuh olehnya.
- **KC-50 [RESMI di STATE v50]** — agregat lewat jalan memutar.
- **KC-51 [RESMI v52]** — bias taksiran pemusatan. Empat kejadian berturut tanpa
  pembalikan arah. **[v19] Kejadian kelima dan keenam kini ADA — dan arahnya TERBALIK.**
  R-317 butir 4 meramalkan `cacah_lubang_awal` **7**, terukur **19** (jauh **di atas**).
  R-318 butir 1 meramalkan **2**, terukur **2** (**tepat**). Untuk pertama kalinya
  sejak KC-51 lahir, ada taksiran yang **tidak** meleset ke bawah. **Status naik dari
  "kecurigaan terbuka" menjadi "kecurigaan dengan satu pembalikan tercatat"** — dan
  **DILARANG** menyebutnya sembuh; enam titik bukan sebaran.
- **KC-52 [RESMI di STATE v54]** — dua penyebut berbeda diperlakukan sebagai satu.
  **[v19] SEBAGIAN TERDAMAIKAN, secara aritmetis, untuk pertama kalinya.** Tiga angka
  BNXUSDT kini punya jembatan tertutup:
  - **48** = `cacah_bulan_lolos` = bulan BNXUSDT yang ADA di penyebut 19.586.
  - **50** = `rentang` = bentangan kalender 2022-05..2026-06.
  - **51** = `cacah_bulan` semesta rentang = bentangan 2022-04..2026-06.
  - Jembatan: 50 − 48 = **2** (dua bulan absen **di dalam**: 2022-06, 2022-08);
    51 − 50 = **1** (satu bulan **di tepi**: 2022-04); 51 − 48 = **3** = 2 + 1. ✅
  **Yang TETAP TIDAK terdamaikan:** apakah himpunan simbol 787 pada kedua laporan itu
  himpunan yang sama. **KC-52 TIDAK dicabut.**
  **DILARANG:** mengutip selisih `R288_BNX_ABSEN` **3** lawan terukur **2** sebagai
  bukti KC-52 — angka 3 itu **tetapan ramalan di dalam kode**, bukan pengukuran laporan
  kedua. Ramalan yang kalah bukan dua penyebut yang berselisih.
- **KC-53 [RESMI di ADR-A020 kep. 3]** — nol pada medan dibaca sebagai ketiadaan
  fenomena. **[v19] Kejadian preventif:** `tak_diterbitkan_arsip` **0** dan `tak_terukur`
  **0** pada sebaran pembeda **tidak** dibaca sebagai "arsip selalu menerbitkan" secara
  umum — hanya sebagai: dari **11** bulan absen, tak satu pun bersebab itu.
- **KC-54 [RESMI di ADR-A021 kep. 3]** — nama medan dibaca sebagai definisi medan.
  **[v19] TETAP TIGA KEJADIAN.** Ditangkal preventif untuk **kedua** kalinya berturut:
  definisi `bulan_absen`, `pembeda_absen`, `rentang`, dan `kendali` **disalin verbatim**
  dari medan `definisi` laporan sebelum satu pun angka ditafsirkan.
- **KC-55 [RESMI di STATE v58]** — pita ramalan tidak menutup seluruh ruang nilai.
  **[v19] MANFAATNYA TERUKUR untuk pertama kalinya.** Pita butir 1 R-318 ditulis tiga
  sisi (kurang 0–1 / tepat 2 / lebih ≥3) padahal sisi "lebih" tampak mustahil menurut
  aritmetika sendiri. Sisi itu **nyaris terpakai**: tetapan kode meramalkan **3**. Bila
  pita ditulis dua sisi, sisi yang justru diperebutkan tidak akan tertutup.
- **KC-56 [DIUSULKAN di STATE v59]** — laporan tanpa stempel waktu diperlakukan seolah
  serempak. **[v19] TIDAK mendapat kejadian kedua**: `lubang_awal.json` punya `waktu_utc`
  (2026-07-30T07:23:11Z) dan `bulan_absen_ringkas.json` punya `waktu_utc`
  (**2026-07-29T17:50:29Z**). Tetap **usulan**.
- **KC-57 [DIUSULKAN di STATE v60]** — konvensi batas tabel buatan sendiri bergeser dari
  medan sumbernya. Satu kejadian (lima baris satu kolom). **Ditahan.**
- **KC-58 [DIUSULKAN di jurnal 151 §9]** — **satu nama gejala dapat menutupi dua
  mekanisme berbeda; cacah gejala yang sama tidak menjamin sebab yang sama.**
  Angka kasus asal (aturan 42): dari **10** simbol berabsen, **9** kehilangan **tepat**
  bulan settled terakhirnya (`absen_sama_dengan_settled` true), sedangkan **BNXUSDT**
  kehilangan dua bulan yang **jauh sebelum** bulan settled terakhirnya
  (`settled_ada_di_absen` **false**). Satu label "bulan absen", dua pola.
  **Kerabat:** KC-38 (kecocokan tanpa membedakan mekanisme) dan KC-45.
  Baru **satu** kejadian; ADR-A019 kep. 3 melarang meresmikannya.
- **KC berikutnya yang bebas: KC-59.**

## Papan skor prediksi — lengkap R-300..R-318 (R-199..R-299 di v4, blob `67dda29e`)

| # | Prediksi | Status |
|---|---|---|
| R-300 | (1) cacah_bulan 64; (2) tetangga BTCST HIDUP; (3) cacah_hidup 8..30 dan MATI>HIDUP | **SEPARUH** |
| R-301 | (1) tebing==0; (2) mati_tersisip ≥1; (3) bangkit==0 | **TIDAK TERADJUDIKASI** |
| R-302 | (1) simbol tersisip 1..10; (2) simbol-bulan 1..50; (3) penyebut 19.586/787 | **SEPARUH** (butir 2 MELESET 88>50) |
| R-303 | (1) simbol tersisip 1..60; (2) simbol-bulan 1..300; (3) penyebut/kendali/kode 0 | **TEPAT (3/3)** |
| R-304 | (1) mati_dulu 5..8; (2) hidup_berlubang 3..8; (3) penyebut/kendali/kode 0 | **MELESET** |
| R-305 | (1) bagian mati-tak-setelah-lubang 0.55..0.95; (2) lubang-awal 20..120; (3) MUDAH | **MELESET** — penyebut 118, bagian **1.0** (tautologis); **5**; butir 3 TEPAT |
| R-306 | (1) bagian arah STRIKT 0.25..0.60; (2) tebing 2025-07 20..90; (3) MUDAH | **TEPAT (3/3)** — **0.339**; **39** |
| R-307 | (1) bagian byte MATI 0.02..0.15; (2) simbol-bulan byte<10.000 20..400; (3) MUDAH | **MELESET** — **0.017704**; **0** (KC-48) |
| R-308 | (1) HIDUP byte<97.634 dalam 20..600; (2) MATI byte<150.000 dalam 10..300; (3) MUDAH | **SEPARUH** — **38** menang; **2** kalah (kasus pertama KC-51) |
| R-309 | (1) HIDUP-kecil bulan pertama 22..38; (2) nisbah rata byte 0.10..0.60; (3) MUDAH | **TEPAT (3/3)** — **37**; **0,527179** |
| R-310 | (1) MATI berdefisit 1..120; (2) bagian defisit bukan-pertama 0.02..0.25; (3) MUDAH | **TEPAT** — **9**; **0,0445** (keduanya tipis ke tepi BAWAH) |
| R-311 | (1) bukan-pertama bukan-MATI berdefisit 200..12.000; (2) bagian sepuluh teratas 0,02..0,45; (3) MUDAH | **SEPARUH** — **114** kalah; **0,4087** menang |
| R-312 | (1) baris berselisih 12..120; (2) bagian baris teratas 0,50..0,865; (3) MUDAH | **TIDAK TERADJUDIKASI** — `cacah_berselisih` **0**, penyebut butir 2 NOL (aturan 41) |
| R-313 | (1) Σ `baris_karantina` = **516.135**; (2) Σ parquet = **12** | **TEPAT (2/2)** — selisih **0**, dengan **cacat aturan 79 melekat permanen** |
| R-314 | (1) `cacah_per_simbol_funding` ∈ [747, 827]; (2) `h_a010_cacah_simbol_berisi` = 0; (3) `h_a011_cacah_hidup` = 0 | **2 TEPAT / 1 MELESET** — **787** · **0** · **6** MELESET |
| R-315 | (1) pemilik ketiga `lubang_tak_dikenal` = **1**; (2) **ketiga** lubang lebih awal daripada `bulan_klines_pertama`; (3) MUDAH | **1 TEPAT / 1 MELESET** — **1** (BNXUSDT) TEPAT; **1 dari 3** MELESET |
| R-316 | (1) 2022-06 dan 2022-08 **tidak hadir** sebagai bulan 1m BNXUSDT; (2) cacah bulan BNXUSDT = **48**; (3) [TURUNAN] cacah **< 50**; (4) MUDAH | **0 TEPAT / 2 MELESET / 1 TIDAK TERADJUDIKASI** — butir 1 **GUGUR** lewat syarat (c); butir 2 **MELESET** (**51**); butir 3 **MELESET** (pita cacat → KC-55) |
| **R-317** | (1) `cacah_bulan` BNXUSDT pada `lubang_awal.json` = **48**; (2) `bulan_pertama` = **"2022-05"**; (3) `akhir_lubang_awal` = **"2023-02"**; (4) `cacah_lubang_awal` = **7**; (5) MUDAH | **2 TEPAT / 2 MELESET** — **48** TEPAT · **"2022-05"** TEPAT · **"2023-01"** MELESET (butir 18) · **19** MELESET (KC-51 terbalik) |
| **R-318** | (1) [UTAMA] BNXUSDT hadir di `baris_berabsen`, `cacah_absen` = **2**; (2) [UTAMA] kedua nama di dalam 2022-05..2023-01; (3) [UTAMA, PALING BERANI] kedua nama = **"2022-06"** dan **"2022-08"**; (4) [TURUNAN] `rentang` = **50**; (5) MUDAH | **TEPAT (4/4 butir berskor)** — `cacah_absen` **2** · 2 dari 2 di dalam pita · **`["2022-06", "2022-08"]`** persis · `rentang` **50** |

**Total R-1..R-318** (dihitung TANGAN, aturan 21):

- TEPAT **227**
- MELESET **63**
- SEPARUH **22**
- TIDAK TERADJUDIKASI **10**
- MENUNGGU **7** (R-7, R-19, R-20, R-28, R-36, R-37, R-199)

Aritmetika terbuka, dua jalur:
- Jalur penjumlahan: 227 + 63 = 290; 290 + 22 = 312; 312 + 10 = 322; 322 + 7 = **329** ✅
- Jalur pertambahan: papan v18 **321** + R-317 **4** butir + R-318 **4** butir = **329** ✅
- Rincian TEPAT: 221 (v18) + 2 (R-317) + 4 (R-318) = **227** ✅
- Rincian MELESET: 61 (v18) + 2 (R-317) + 0 (R-318) = **63** ✅

Nomor terpakai R-1..R-318. N_percobaan = 0. **ADJUDIKASI RISET TETAP TERKUNCI.**

**PAPAN SKOR 329 DISAHKAN DI SINI** (aturan 29). Ini pengesahan pertama sejak v17.

**Nisbah papan skor, dihitung tangan:** dari 312 ramalan beradjudikasi penuh
(227 + 63 + 22), TEPAT **72,8%**, MELESET **20,2%**, SEPARUH **7,1%**. Dibanding v18
(72,7 / 20,1 / 7,2) perubahannya **sepersepuluh persen** — delapan butir baru nyaris
tidak menggeser apa pun, dan itu **wajib disebut** supaya empat kemenangan berturut
R-318 tidak terdengar seperti lompatan mutu. Angka ini tetap **DILARANG dibaca sebagai
mutu ramalan**: sebagian besar butir terakhir tiap ramalan berlabel MUDAH.
**R-312 DILARANG masuk pembilang maupun penyebut.**

**Kolom terpisah — DI LUAR lajur papan skor:** **R-229 TEPAT** dan **R-230 MELESET**
(ADR-A020 kep. 5). **R-228 tetap BELUM diadjudikasi.**
**[v19] Bertambah:** **R-288 dan R-290** tercatat di docstring `bulan_absen.py` dan
**belum diadjudikasi**. Blok `uji_r288` melaporkan `r288_menang` **false** (butir 1
kalah 3 vs **2**; butir 2 menang 9 dari 9 ≥ ambang 7; butir 3 kalah 12 vs **11**).
**Itu vonis alat, bukan adjudikasi** — R-288 **tidak** masuk lajur mana pun di sini.

**Utang papan skor:** rincian R-236..R-247 masih di jurnal 92–94; pemeriksaan
R-224..R-235 belum dikerjakan; **R-305 belum pernah diadjudikasi tangan** — jurnal
`2026-07-30-125.md` **belum dibaca**; selama itu R-305 berstatus **MENUNGGU pemeriksaan**
dan barisnya di tabel di atas berasal dari catatan lama, bukan dari adjudikasi berjejak.

### [v19] R-318 — kemenangan terbesar sesi ini, dibaca sedingin mungkin

Empat dari empat butir berskor menang, termasuk butir yang praregistrasinya sendiri
menandai **PALING BERANI**: menamai **dua bulan tertentu** dari ruang **50** bulan
kalender. Itu hasil terbaik yang tercatat sepanjang deret R-300..R-318.

**Yang DILARANG disimpulkan darinya:**

1. **DILARANG** menyebutnya empat bukti bebas. Butir 1 (cacah 2), butir 3 (nama 2022-06
   dan 2022-08), dan butir 4 (rentang 50) semuanya turun dari **satu** aritmetika:
   bentangan 2022-05..2026-06 = 50 dan 50 − 48 = 2, ditambah tabel bulan yang hilang
   dari `silang_funding.json`. Bila aritmetika itu salah, **ketiganya jatuh bersama**.
   Ini KC-47 dalam bentuk yang paling menggoda: bukan satu peristiwa menyamar sebagai
   banyak pengamatan, melainkan **satu perhitungan menyamar sebagai banyak ramalan**.
2. **DILARANG** menulis H-A023 **TERBUKTI**. Ia tetap **BERSYARAT**, sekarang dengan
   aritmetika tertutup (§KC-52) — tetapi keanggotaan penyebut diukur untuk **satu**
   simbol saja.
3. **DILARANG** menyebut mutu peramalan membaik. Nisbah bergeser 0,1 poin persen.
4. **DILARANG** menskor temuan sampingan giliran ini — sebab `gagal_gerbang`, sebaran
   11/0/0, pola sembilan-lawan-BNXUSDT — tidak satu pun diregistrasi (aturan 29).

**Yang BOLEH dikatakan:** riset ini meramalkan dua nama bulan sebelum membukanya, dan
kedua nama itu benar.

### [v19] Aturan 90 — DIRESMIKAN di STATE v60, tabel tiga kejadiannya di sini

> **Aturan 90 [RESMI].** Laporan `reports/ci_terakhir.json` sah bagi sebuah push **hanya
> bila** medan `commit` cocok dengan SHA push itu. Bila tidak cocok, laporan itu milik
> push sebelumnya; pembacaan **WAJIB diulang** dan laporan yang tidak cocok **DILARANG
> dicatat**.

| kejadian | push | blob yang muncul salah | `commit` yang terbawa | milik ke- |
| --- | --- | --- | --- | --- |
| 1 | STATE v58 | `5b433a93` | `9b01c06e` | ke-57 |
| 2 | STATE v59 | `990502c7` | `72fe177c` | ke-60 |
| 3 | EKOR v18 | `b6d02273` | `05f6f72e` | ke-61 |

**Pemakaian pertama sesudah peresmian: aturan 38 ke-64** (push STATE v60) — `commit`
**cocok pada percobaan pertama**, jadi aturan itu **tidak diuji** oleh kasus itu.
Ke-62, ke-63, ke-64 seluruhnya cocok pada percobaan pertama.

**DILARANG** menyebut aturan 90 **teruji**: ia lahir dari tiga kejadian **sebelum**
peresmian, dan sejak diresmikan **belum sekali pun menangkap laporan salah**.

### [v19] Aturan 88, 89, dan usulan baru 91

> **Usulan aturan 88 (ADR-A021 kep. 5).** Ramalan bahwa **semua** anggota sebuah
> himpunan berbagi satu sifat **WAJIB** disertai **mekanisme tertulis**.

> **Usulan aturan 89 (lahir dari butir 16).** Setiap pita ramalan atas sebuah bilangan
> **WAJIB** menutup **ketiga sisi** ruang nilainya, atau menyatakan tertulis mengapa
> satu sisi mustahil.

> **[BARU] Usulan aturan 91 (lahir dari R-318).** Ramalan yang butir-butirnya
> diturunkan dari **satu aritmetika yang sama** WAJIB menyatakan korelasi itu di dalam
> praregistrasi, agar kemenangan beruntun tidak terbaca sebagai bukti bebas berganda.

**Aturan 88** tetap **satu** kejadian — tidak bertambah. **Aturan 89 kini punya manfaat
TERUKUR** (§KC-55: pita tiga sisi butir 1 R-318 menutup sisi yang justru diperebutkan
tetapan kode) — tetapi **cacat** yang melahirkannya masih **satu**. Meresmikan aturan
atas dasar **manfaat** alih-alih **cacat berulang** adalah perubahan kebijakan, bukan
penerapan kebijakan; itu **wewenang ADR-A022**, bukan wewenang lampiran. **Aturan 91**
berdiri di satu kejadian. **Ketiganya TETAP USULAN.**

**Catatan kejujuran yang melekat:** 88, 89, dan 91 semuanya lahir **sesudah** sesuatu
berjalan buruk. **Utang yang dibayar, bukan laba.**

### [v19] Aturan 85 — TIGA adjudikasi, tetap BUKAN sebaran

R-317 dan R-318 keduanya memakai pita bertepi eksplisit. Jumlah adjudikasi yang menguji
tepi kini **tiga**. **DILARANG** menyebut aturan 85 **teruji**, **bekerja**, atau
**terbukti**; tiga titik bukan sebaran.

### [v19] Aturan 79 — rekor LIMA berturut

R-314, R-315, R-316, **R-317**, **R-318** — kelimanya diregistrasi di `journal/**`
**sebelum** bahan dibuka. Aritmetika terbuka: dari R-314 sampai R-318 → 318 − 314 = 4;
4 + 1 = **5 ramalan berturut**. **DILARANG** menyebut aturan 79 lemah, longgar, atau
opsional. **DILARANG** pula menyebut rekor ini sebagai bukti mutu ramalan — ia bukti
**urutan kerja**, bukan bukti **isi**.

### Lima larangan permanen yang menempel pada R-312 (tidak berubah)

1. **DILARANG** mengatakan pita butir 1 (12..120) "tidak terbantah". Ia tidak diuji.
2. **DILARANG** mengatakan kalibrasi membaik atau memburuk karena R-312.
3. **DILARANG** menghitungnya di pembilang maupun penyebut nisbah kemenangan.
4. **DILARANG** menghidupkannya kembali dengan alasan penjelasannya kini ditemukan.
5. Angka **12** di R-313 adalah cacah **parquet karantina** — arti berbeda dari 12 di
   R-312 butir 1. **Kesamaan itu DILARANG dibaca sebagai konfirmasi apa pun.**

### Larangan R-315/R-316/R-317/R-318 — dengan SATU pencabutan

1. `lubang_tak_dikenal` **bukan** pernyataan arah waktu (ADR-A021 kep. 2). **TETAP.**
2. Vonis R-315 **DILARANG** ditulis SEPARUH. **TETAP.**
3. Kemunculan BNXUSDT **DILARANG** dibaca sebagai konfirmasi fakta lama. **TETAP.**
4. **✅ DICABUT SEBAGIAN — larangan menamai kedua bulan absen BNXUSDT.** Nama itu kini
   terbaca langsung dari medan `bulan_absen` pada laporan bersidik, utuh, berkendali
   sah: **2022-06** dan **2022-08**. **Yang TIDAK dicabut:** larangan mengklaim
   **sebabnya** di luar apa yang dilaporkan medan `pembeda_absen`.
5. Cacah total `baris_mati` **DILARANG** diklaim terukur (terpotong **54%**). **TETAP.**
6. Empat kecocokan pasca-hoc jurnal 145 §7 **DILARANG** masuk lajur skor. **TETAP.**
7. Aturan 88, 89, **91**, KC-56, KC-57, **KC-58 DILARANG** diklaim kemenangan
   metodologis.
8. `reports/kehidupan_arsip_*.json` **DILARANG** dibuka dengan harapan dibaca utuh.
9. Angka `semesta_rentang.json` **DILARANG** dibandingkan secara keserempakan — ia
   **tak bertanggal** (KC-56). **TETAP.**
10. Sifat medan `cacah_bulan` **DILARANG** dipindah ke `bulan_per_simbol` atau
    sebaliknya. **TETAP.**
11. **DILARANG** menyimpulkan bahwa hanya simbol SETTLED yang berlubang. **TETAP** —
    dan **v19 memperkuatnya dari arah lain**: seluruh **11** bulan absen jatuh pada
    simbol berpasangan settled, tetapi **5 dari 15** pasangan berabsen **nol**, jadi
    "berpasangan settled" **bukan** syarat cukup.
12. **[v19 BARU]** **DILARANG** menarik cacah, sebaran, atau daftar dari
    `baris_penyebut_butir_1` pada `lubang_awal.json` — **58 dari 118 baris tidak pernah
    ditulis** oleh modulnya sendiri (`BATAS_BARIS_LAPORAN = 60`), tanpa peringatan alat.
13. **[v19 BARU]** **DILARANG** mengutip tabel H-A010 di lampiran sebagai nilai
    `akhir_lubang_awal` (butir 18).
14. **[v19 BARU]** **DILARANG** memakai blok `uji_r305` maupun `uji_r288` sebagai
    adjudikasi (KC-49).
15. **[v19 BARU]** **DILARANG** mengutip selisih 3 lawan 2 sebagai bukti KC-52.
16. **[v19 BARU]** **DILARANG** menyatakan klausa mana dari `gerbang_1m.py` yang
    menjatuhkan BNXUSDT 2022-06 dan 2022-08 — yang terukur hanya **bahwa** pembedanya
    `gagal_gerbang`, bukan **klausa mana** (utang ukur 25).

## Catatan kejujuran [v19]

1. **Papan skor bergerak delapan butir sekaligus, dan itu wajib dibaca dengan curiga.**
   Delapan butir dari **dua** ramalan yang keduanya menyasar **satu simbol yang sama**
   (BNXUSDT). Riset ini sedang sangat pandai meramalkan **satu simbol** — bukan sedang
   pandai meramalkan.
2. **R-318 menang penuh, dan korelasi antarbutirnya diakui di dalam berkas yang sama
   dengan kemenangannya**, bukan ditunda ke ADR. Itu syarat supaya kemenangan ini tidak
   berumur panjang sebagai kesalahpahaman.
3. **Butir 18 diakui walau ia membatalkan alasan kekalahan, bukan kekalahannya.** Godaan
   untuk menulis "butir 3 R-317 sebenarnya benar" nyata dan **ditolak**: yang diramalkan
   adalah **2023-02**, yang terukur **2023-01**. Kalah tetap kalah; yang ditambahkan
   hanya **sebab**.
4. **KC-57 ditahan walau lima dari lima cocok.** Lima baris satu kolom = satu cacat.
5. **KC-51 dicatat TERBALIK untuk pertama kalinya**, walau pembalikan itu merugikan
   narasi lama yang rapi ("selalu meleset ke bawah"). Cacah lubang awal terukur **19**
   lawan ramalan **7** — **jauh** di atas.
6. **Aturan 86 (b) dipakai preventif dan terbukti membayar.** Membaca `bulan_absen.py`
   sebelum laporannya menghasilkan: kepastian tanpa pembatas baris, definisi medan
   disalin, dan pengetahuan bahwa tepi mustahil absen. **Tiga penangkal dari satu
   pembacaan kode.**
7. **Aturan 57 beruntun 4 dari 4, tidak bertambah.** Tidak ada `tests/**` yang berubah.
8. **Aturan 52 ditaati tiga puluh dua kali berturut** hingga jurnal 151, **tiga puluh
   tiga** dengan berkas ini.
9. **`PROMPT_KELANJUTAN.md` tetap belum diberi kepala "ARSIP — BUKAN SUMBER"** dan
   `PROMPT.md` **v55 belum didorong**. Utang ini kini berumur **sebelas versi** — naik
   dua sejak v18. Disebut setiap kali, tidak dikerjakan setiap kali. **Itu cacat
   proses, dan menyebutnya berulang tanpa mengerjakannya adalah cacat kedua.**
10. **Jebakan laporan CI diresmikan sebagai aturan 90**, dan pada tiga pemakaian sejak
    itu **tidak sekali pun menangkap apa pun**. Aturan yang belum pernah menyala
    bukanlah aturan yang terbukti.
11. **Pemeriksaan silang yang menutup tanpa sisa** (terbitan, TIDAK diskor):
    18.799 − 1.401 = **17.398**; 98 − 80 = **18**; 769 + 18 = **787**;
    **19.586 + 12 = 19.598**; **839.325.999 + 516.135 = 839.842.134**;
    **880 − 877 = 3**; `tabel_silang` **33 + 842 + 2 + 0 = 877**.
    **[v19] Yang menutup BARU dan ini yang terpenting sesi ini:**
    **51 − 50 = 1** (tepi 2022-04) · **50 − 48 = 2** (dalam: 2022-06, 2022-08) ·
    **51 − 48 = 3** ✅ — ketiga lubang tak dikenal terjelaskan **posisinya** tanpa sisa.
    Juga: **9 bulan absen tunggal + 2 milik BNXUSDT = 11** = `jumlah_bulan_absen` ✅;
    **11 gagal_gerbang + 0 + 0 = 11** ✅; **10 berabsen + 5 berabsen nol = 15** pasangan ✅.
    **[v19] Yang TETAP TIDAK menutup:** `selisih_absen_pasangan_jurnal_113` = **−1**
    (12 diramalkan jurnal 113, **11** terukur), dan **klausa gerbang mana** yang
    menjatuhkan dua bulan itu.

**Kesalahan proses [v19].** Tidak ada kegagalan panggilan alat; seluruh `runTool`
berhasil dengan bungkus `{toolName, toolArguments}`. Yang lama tetap tercatat: push
STATE v55 pernah ditolak karena bungkus itu tidak dipakai — **kesalahan bentuk
panggilan, bukan galat alat**. Kerugian lama: laporan CI run `30547842823` hangus, blob
ke-38 tak dapat dipulihkan.

**Batas alat yang tetap terbuka:** `semesta_rentang.json` **95%**,
`silang_funding.json` **54%**, daftar `reports/` **76%**, `kehidupan_arsip_*.json`
**mustahil**.
**[v19] KELAS BATAS BARU — PEMOTONGAN OLEH MODUL, BUKAN OLEH ALAT.**
`lubang_awal.json`: `cacah_baris_penyebut_butir_1_dilapor` **60** vs `penyebut_butir_1`
**118** → **58 baris tidak pernah ditulis**. Alat melaporkan berkas **UTUH** (42.449 B,
tanpa peringatan). **Yang memotong adalah `BATAS_BARIS_LAPORAN = 60` di dalam modul.**
Kelas ini **lebih berbahaya** daripada pemotongan alat karena **tidak ada peringatan
apa pun**; satu-satunya pendeteksinya adalah **membaca kode sebelum laporan**
(aturan 86 b). **Diperiksa pada `bulan_absen.py`: modul itu TIDAK punya pembatas baris,
sehingga `baris_berabsen` LENGKAP** — pemeriksaan itu dilakukan **sebelum** laporan
dibuka, bukan sesudah.

## Jumlah uji

**1377 TERUKUR, kini DUA PULUH bacaan berjejak (ke-45..ke-64).** Aritmetika tangan:
64 − 45 = 19; 19 + 1 = **20**.

Bacaan ke-45..ke-61 tercatat di v16, v17, dan v18. Tiga yang terbaru:

19. **[v19]** blob **`3f299eaf4383604666f30c3448a32d38e57b1742`**: run **30592559253**,
    commit **`bb565f4c`** (EKOR v18), **2026-07-31T00:06:48Z**, kode 0, `1377 in 0.62s`.
20. **[v19]** blob **`a185f32a80471ea9f76c72415cacf3c4f06dfeda`**: run **30593086004**,
    commit **`51c65e2a`** (UKUR v18), **00:17:08Z**, kode 0, `1377 in 0.57s`.
21. **[v19]** blob **`b6835432ff25e8482781f13018c17b9f080ad510`**: run **30594157668**,
    commit **`8345668e9a8f0e01bcbe86fd9d0f60f4709fd834`** (STATE v60),
    **2026-07-31T00:39:46Z**, kode 0, `1377 tests collected in 0.48s`.

Turunan: 1341 + **36** butir `tests/test_selisih_lilin.py` = **1377** ✅ (aturan 21),
terverifikasi dari sumber, bukan dari ingatan.

Riwayat panjang: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 →
984 → 1044 → 1100 → 1168 → 1233 → 1297 → 1341 (enam run) → **1377** (dua puluh run
berjejak).

Cacah per berkas uji (**milik repo riset ini — bukan repo warisan**):
`test_irisan_byte.py` **68** · `test_bulan_pertama.py` **65** ·
`test_keterisian_lilin.py` **64** · `test_bentangan_kohort.py` V2 **63** ·
`test_lubang_tebing.py` **60** · `test_sebab_bangkit.py` **57** ·
`test_byte_semesta.py` **56** · `test_lubang_awal.py` **48** ·
`test_tersisip_semesta.py` **47** · `test_anatomi_tengah.py` **47** ·
`test_sisa_defisit.py` **44** · `test_selisih_lilin.py` **36** · `test_terhenti.py` V4
**33** · `test_bulan_absen.py` **32** · `test_karantina_semesta.py` **28** ·
`test_silang_settled.py` **24** · `test_ukur_baris.py` **3**.
**`tests/test_lubang_tengah.py` — 56 butir menurut R-228, BELUM DIBACA, DILARANG
dikutip sebagai cacah terukur.**
**`tests/test_gerbang_1m.py` — penjaga salinan rumus `menit_hilang_dalam_rentang`.
BELUM DIBACA; cacah butirnya TIDAK DIKETAHUI.** **[v19] Peringkatnya NAIK**: utang ukur
25 menuntut pemahaman keenam klausa gerbang, dan berkas ini penjaganya.

**Aturan 57: beruntun 4 dari 4.** Hanya push yang menyentuh `tests/**` yang dihitung.

### ORDINAL ATURAN 38 — buku besar, kini sampai ke-64

**Definisi yang berlaku (ADR-A018 kep. 8):** pemakaian dihitung **hanya** untuk
pembacaan `reports/ci_terakhir.json` yang meninggalkan **jejak tertulis** berupa nomor
run + commit + blob di STATE, lampiran, atau jurnal.

| ke- | CI | run | commit | blob | jejak |
|---|---|---|---|---|---|
| 55 | 1377 | 30587658376 | `ebe6f373` | `8ea8cc46` | EKOR v16 |
| 56 | 1377 | 30588460935 | `32413935` | `34f88b37` | UKUR v16 |
| 57 | 1377 | 30589452976 | `9b01c06e` | `5b433a93` | jurnal 146, STATE v58 |
| 58 | 1377 | 30590593816 | `839a0f17` | `9718bf98` | EKOR v17 |
| 59 | 1377 | 30590948580 | `c0877746` | `5f62452d` | UKUR v17, STATE v59 |
| 60 | 1377 | 30591338909 | `72fe177c` | `990502c7` | STATE v59 |
| 61 | 1377 | 30592159959 | `05f6f72e` | `b6d02273` | EKOR v18 |
| **62** | **1377** | **30592559253** | **`bb565f4c`** | **`3f299eaf4383604666f30c3448a32d38e57b1742`** | **UKUR v18** |
| **63** | **1377** | **30593086004** | **`51c65e2a`** | **`a185f32a80471ea9f76c72415cacf3c4f06dfeda`** | **STATE v60** |
| **64** | **1377** | **30594157668** | **`8345668e`** | **`b6835432ff25e8482781f13018c17b9f080ad510`** | **berkas ini** |

**Pemakaian berjalan = ke-enam puluh empat.** Ke-64 dibaca **2026-07-31T00:39:46Z**,
kode keluar **0**, atas push **STATE v60**, `commit` **COCOK pada percobaan pertama**.

**[v19] Panjang deret berjejak tanpa laporan hangus, dengan aritmetika terbuka
(butir 17):** ke-42..ke-64 → 64 − 42 = 22; 22 + 1 = **23 pembacaan berturut**.

**Bot CI menambah satu commit di atas tiap push pemicu** — kini **tujuh belas kali
berturut** (terbaru: `9e43911b`, `64b03bdb`, `8e0b39a5`, `e08a0a2a`).
**Deterministik dari `ci.yml`; DILARANG dihitung sebagai kemenangan ramalan.**
**Push `journal/**` dan `decisions/**` TIDAK menyalakan CI** — jurnal 148, 149, 150,
dan **151** tidak menghasilkan commit bot, dan itu **terukur** dari `paths-ignore`
pada `ci.yml` (`c79497b2c812679eaa69aee5b3160eac9f5c5fb7`).

**Dua cacat tetap disebut apa adanya:** baris ke-**38** (run `30541051907`, CI 1297,
commit `5d7d8b96`) **tanpa blob**; dan run **30547842823** (bot `de2fc03d`) **tidak
pernah dibaca**, tertimpa, **DILARANG dihitung**. Bila jejak lain ditemukan di jurnal
133–134, nomor ini **WAJIB dikoreksi, bukan dipertahankan**.

**Calon aturan** — dua push akar berturut tanpa membaca laporan di antaranya — **tetap
DITOLAK diresmikan**: masih **satu** kejadian.

## Utang verifikasi

1-5, 11 menunggu tahap juri. 6-23, 25-29, 31 LUNAS. **Nomor utang BUKAN nomor ramalan
— KC-32.**

24. **AKTIF. LUNAS BARU [v19]:**
    - **`lux_ai/serapan/lubang_awal.py` DIBACA UTUH** — blob
      **`8c36943da222dfa262b3b9f2117bf72dc801681d`**. Menyingkap `BATAS_BARIS_LAPORAN = 60`.
    - **`reports/lubang_awal.json` DIBACA UTUH** — blob
      **`3da15a11c3cd949fb2741f919beb2b515a51d70f`**, 42.449 B, tanpa pemotongan alat.
    - **`lux_ai/serapan/bulan_absen.py` DIBACA UTUH** — blob
      **`10279d721d66a86b6d265badf81ada3204648f69`** (aturan 86 b, preventif).
    - **`reports/bulan_absen_ringkas.json` DIBACA UTUH** — blob
      **`e450d9f95e9bca0dc28a0e01c6aad6594c4fa3d6`**, tanpa pemotongan alat.
    - **`STATE.md` v60 dibaca ulang UTUH** — blob `d3f1448fad4ead804be59b1bbb1562b460f01621`.
    - **EKOR v18 dibaca UTUH** pada giliran ini — blob `217beaeebd367309ea1a4a4d5ea3234887788b2b`.
    - `reports/ci_terakhir.json` ke-62, ke-63, ke-64 dibaca utuh, blob DICATAT.
    **TETAP BELUM:** `decisions/ADR-A002`, **A004 (peringkat tinggi — sumber keenam
    klausa gerbang; kini diperkuat utang ukur 25)**, **A006**, **A007**, **A008**;
    **`tests/test_gerbang_1m.py` (peringkat NAIK)**;
    `.github/workflows/karantina_semesta.yml` (`de40fa4e`); `tests/test_pulihkan.py`
    (`11c43533`); `tests/test_rilis_karantina.py` (`739c8da9`);
    `tests/test_karantina_a006.py` (`a5a3d82f`); `tests/test_lubang_tengah.py`;
    **`journal/2026-07-30-125.md` (praregistrasi R-305)**;
    **bagian `baris_mati` `silang_funding.json`**; **5% `semesta_rentang.json`**;
    **58 baris `baris_penyebut_butir_1` yang tidak pernah ditulis (mustahil dari
    laporan; menuntut modul dijalankan ulang)**.
30. **AKTIF — UTANG HIDUP**, ADR-A019 kep. 8 MENOLAK menutupnya. Angka **50 / 54 / 45**
    tetap **TURUNAN**. Yang sah tetap **49 / 53 / 44 / 18** pada ref `3196fd98` dan
    `8a614567`.
32. **AKTIF — tiga butir "memerlukan verifikasi" `PETA_MODUL.md`** (repo **WARISAN**):
    (a) `enable_hs`; (b) "30 pair alfabetis"; (c) "kendala mengikat = kapasitas margin".
33. **[v19] LUNAS untuk butir 18** — ditulis resmi di STATE v60 dan disalin ke berkas
    ini. Daftar berdiri di **delapan belas** butir, **tanpa calon baru**.
34. **AKTIF — `PROMPT_KELANJUTAN.md` belum berkepala "ARSIP — BUKAN SUMBER"**, dan
    **`PROMPT.md` v55 belum didorong.** **Umur: sebelas versi.**
35. **[v19] LUNAS sebagian** — UKUR v18 sudah naik. **Digantikan utang baru:** UKUR
    **v19** belum naik; sampai itu, UKUR tertinggal dan trio akar TIDAK SERASI.
36. **AKTIF — identitas dua belas simbol-bulan karantina belum pernah didaftar.**
    Manifes **20.533.802 B** — jalan satu-satunya **modul CI**.
37. **AKTIF — `ukur_baris.py` V6 belum ditulis.** `BERKAS_DIUKUR` masih **21** nama.
38. **AKTIF — R-228 belum diadjudikasi.** Cacah 56 butir `test_lubang_tengah.py`
    **DILARANG** dikutip sebagai terukur.
39. **AKTIF — bagian `baris_mati` `silang_funding.json` belum terbaca** (54%).
40. **✅ LUNAS [v19] — identitas bulan BNXUSDT.** Utang ini berdiri sejak v14 dan kini
    tertutup dari **dua** arah: daftar semesta rentang **2022-04..2026-06 kontigu (51)**
    diturunkan di v18; dan daftar **bulan yang TIDAK masuk penyebut** kini terukur
    **bernama**: **2022-06** dan **2022-08** di dalam rentang, **2022-04** di tepi.
    Penyebut BNXUSDT = 51 − 3 = **48**. ✅
41. **AKTIF — daftar `reports/` belum terbaca utuh** (terpotong **76%** pada ref
    `8364ad92f0a52015f9285ed5f2a9c8eaff33f732`). Wajib disebut setiap kali **aturan
    86 (a)** dipakai.
42. **AKTIF — penulis `semesta_rentang.json` belum diidentifikasi.** Tanpa `waktu_utc`,
    tanpa medan sidik. Tak dapat ditelusuri ke kode maupun ke waktu.
43. **✅ LUNAS [v19] — keanggotaan penyebut BNXUSDT.** Terukur: **48** dari **51** bulan
    semesta rentang masuk penyebut; ketiga sisanya bernama. Jembatan **51 − 48 = 3**
    tertutup tanpa sisa. **Yang TIDAK ikut lunas:** keanggotaan penyebut untuk **786
    simbol lain** — dan itu yang sebenarnya diminta klasifikasi.
44. **✅ LUNAS [v19] — nama bulan penyebut BNXUSDT** (= utang ukur 24 dari UKUR v18).
45. **BARU [v19] — `selisih_absen_pasangan_jurnal_113` = −1.** Jurnal 113 mencatat **12**
    bulan absen pasangan; terukur **11**. Laporan menyatakan medan ini **tidak
    menggugurkan** apa pun (aturan 24, 72). Selisihnya **belum dijelaskan**, dan jurnal
    113 **belum dibaca ulang**.
46. **BARU [v19] — mengapa sembilan dari sepuluh simbol berabsen kehilangan TEPAT bulan
    settled terakhirnya, sementara BNXUSDT tidak.** Ini bahan KC-58 dan calon poros
    riset tersendiri.

**Utang ukur (penomoran terpisah, milik UKUR):** 25 **BARU [v19]** — klausa mana dari
enam klausa `gerbang_1m.py` yang menolak BNXUSDT 2022-06 dan 2022-08. Bahan:
`gerbang_1m.py` (`c8cc54c84a57173ef2e426c317d6ac50734e9b4a`), **ADR-A004 §2**, dan
`tests/test_gerbang_1m.py`. **Ini kini poros riset peringkat pertama.**

## Daftar ADR

- **ADR-A001** aturan dasar. DITERIMA.
- **ADR-A002** serapan. Kondisi v3 berlaku; §10 tetap tidak boleh diubah. **BELUM DIBACA UTUH.**
- **ADR-A003** taksonomi rezim. **BELUM ADA — blokir pertama klasifikasi.**
- **ADR-A004** kebijakan KC-6. DITERIMA. **BELUM DIBACA UTUH — peringkat TERTINGGI di
  antara utang bacaan**, sebab `gerbang_1m.py` menyatakan dirinya penerapan **§2** ADR
  ini, dan utang ukur 25 tidak dapat dibayar tanpanya.
- **ADR-A005** jenis instrumen. DITERIMA.
- **ADR-A006** karantina + persistensi. DITERIMA, TERVERIFIKASI. **BELUM DIBACA UTUH.**
- **ADR-A007** serapan hibrida. DIUSULKAN. **BELUM DIBACA UTUH.**
- **ADR-A008** akibat KC-18. Kep. 1–6 DITERIMA; **kep. 7 DITANGGUHKAN.** **BELUM DIBACA UTUH.**
- **ADR-A009** (`17a594b6`). **DICABUT PENUH oleh ADR-A012.**
- **ADR-A010** (`c4bccf21`) — klaim "kebangkitan tunggal" DICABUT. DITERIMA.
- **ADR-A011** (`645fd5df`) — arah sebab A009 dicabut untuk kelas bangkit. DITERIMA.
- **ADR-A012** (`f9f564d1`) — arah sebab dicabut untuk SELURUH semesta. DITERIMA.
- **ADR-A013** (`8ba4f989`) — (2) dan (4) kini aturan **80** dan **81**. DITERIMA.
- **ADR-A014** (`6d77c2cd`) — byte parquet; (5) melahirkan KC-48. DITERIMA.
- **ADR-A015** (`387d5510`) — (5) besar berkas bukan detektor status. DITERIMA.
- **ADR-A016** (`209802d7`) — **kewajiban adjudikasi pada giliran berbeda**; kep. 4
  DIKOREKSI oleh A018 kep. 6. DITERIMA. **[v19] DIUJI DUA KALI dan ditaati dua kali:**
  R-317 (jurnal 148 → 149) dan R-318 (jurnal 150 → **151**). Pada R-318 aturan ini
  memaksa **berhenti ke-47** — biaya nyata yang dibayar demi disiplin.
- **ADR-A017** (`1be570f2`) — kep. 4 TERJAWAB PENUH oleh R-313. DITERIMA.
- **ADR-A018** (`3fba599e`) — (8) definisi ordinal aturan 38; (9) `PROMPT_KELANJUTAN.md`
  arsip; (10) dua cacah `tests/`; (11) cacah tangan 49/53/44/18. DITERIMA.
- **ADR-A019** (`9cd7d25e…`, commit `e6007ba5`) — (3) **aturan tidak diresmikan atas
  satu kejadian**; (8) utang cacah tangan ditolak ditutup. **DITERIMA — kep. 9
  DIKOREKSI oleh A020 kep. 8.** **[v19] Kep. 3 dipegang LIMA kali** (aturan 88, 89,
  **91**, KC-56, KC-57, KC-58 — seluruhnya ditahan di satu kejadian).
- **ADR-A020** (`200c7e7d…`, commit `d8335be1`) — sepuluh keputusan. DITERIMA.
- **ADR-A021** (`3e756672…`, commit `2cee14b7`) — sepuluh keputusan; (2) pencabutan
  bacaan `lubang_tak_dikenal`; (3) KC-54; (4) aturan 87 RESMI. DITERIMA.
  **[v19] Kep. 2 kini bersandar pada bukti terukur berlapis:** ketiga bulan itu ADA di
  semesta rentang, dan dua di antaranya terukur **`gagal_gerbang`** — sebab yang sama
  sekali bukan "bulan sebelum simbol lahir".
- **ADR-A022 [BELUM ADA]** — **[v19] lima butir calon, urut:**
  (a) **peresmian aturan 90 dibukukan** beserta tabel tiga kejadiannya;
  (b) tiga angka bersaing BNXUSDT **48 / 50 / 51** kini **terdamaikan aritmetis** —
      apakah KC-52 perlu diperluas atau justru dipersempit;
  (c) status `semesta_rentang.json` sebagai sumber **tak bertanggal dan tak bersidik**;
  (d) apakah **KC-56**, **KC-57**, dan **KC-58** diresmikan;
  (e) apakah **aturan 89** boleh diresmikan atas dasar **manfaat terukur** alih-alih
      **cacat berulang** — dan bila boleh, apakah **aturan 91** ikut.
  **DILARANG disusun pada giliran yang sama dengan adjudikasi** (ADR-A016).

## Temuan sampingan

### [v19] `reports/bulan_absen_ringkas.json` — bahan R-318, terbaca UTUH

Blob **`e450d9f95e9bca0dc28a0e01c6aad6594c4fa3d6`**, `waktu_utc`
**2026-07-29T17:50:29Z**, `sidik_kode`
**`0294eb3a2fca6354b495148fc87d564f649d545a81314f21ef432775cf163088`**,
`berkas_sumber` `reports/bulan_absen.json` (**249.992 B**, sidik
`d2fc3bfb362f834225faab76d6bf87b8f334d1ee26638a8112fb9b546614a3bd`).
**Tanpa pemotongan alat.**

**Kendali sah:** BTCUSDT dan ETHUSDT keduanya **78** bulan (ambang 60), **0** absen.
**Penggugur bersih:** `sidik_seragam` true · 8 = 8 laporan · 0 kunci ganda ·
`selisih_penyebut` **0** · `cacah_pasangan` **15** · `penggugur_menyala` **false**.

| simbol | `bulan_absen` | `rentang` | `cacah_bulan_lolos` | `absen_sama_dengan_settled` |
| --- | --- | --- | --- | --- |
| AERGOUSDT | 2025-04 | 22 | 21 | **true** |
| AIAUSDT | 2026-01 | 10 | 9 | **true** |
| **BNXUSDT** | **2022-06, 2022-08** | **50** | **48** | **false** |
| CTKUSDT | 2025-04 | 68 | 67 | **true** |
| CVCUSDT | 2025-05 | 68 | 67 | **true** |
| CVXUSDT | 2025-07 | 46 | 45 | **true** |
| LITUSDT | 2025-12 | 65 | 64 | **true** |
| MAVIAUSDT | 2025-03 | 29 | 28 | **true** |
| PUMPUSDT | 2025-07 | 15 | 14 | **true** |
| SLPUSDT | 2025-07 | 33 | 32 | **true** |

Berabsen **nol** (5 dari 15 pasangan): BDXNUSDT, ICPUSDT, MINAUSDT, SXPUSDT, TLMUSDT.

**Ringkasan semesta:** `cacah_nama_berabsen` **10** dari **787** · `jumlah_bulan_absen`
**11** · `jumlah_bulan_absen_pasangan` **11** · `jumlah_bulan_absen_luar_pasangan`
**0** · `sebaran_pembeda` **gagal_gerbang 11 / tak_diterbitkan_arsip 0 / tak_terukur 0**.

**Kesimpulan terukur:**
1. **Bulan absen adalah gejala GERBANG, bukan gejala PENERBITAN.** Sebelas dari sebelas
   ada di manifes arsip lalu ditolak gerbang.
2. **BNXUSDT satu-satunya simbol dengan lebih dari satu bulan absen** di seluruh 787.
3. **BNXUSDT satu-satunya yang bulan absennya bukan bulan settled terakhirnya**
   (`bulan_settled_terakhir` **2023-02**, `settled_ada_di_absen` **false**) → KC-58.

**DILARANG:** menyebut klausa gerbang mana pun; menyamakan "tidak ada di penyebut"
dengan "dijatuhkan gerbang" di luar medan `pembeda_absen`; menskor temuan ini.

### [v19] `reports/lubang_awal.json` — bahan R-317, UTUH tetapi DIPOTONG MODUL

Blob **`3da15a11c3cd949fb2741f919beb2b515a51d70f`**, 42.449 B, `waktu_utc`
**2026-07-30T07:23:11Z**, `sidik_kode`
**`156499ce9d6e822bb7f57786e8e308955441996699c1fd53d0e8814e1f8f2362`**.
`cacah_simbol_ada_lubang` **122** · `cacah_simbol_lubang_awal` **5** ·
`cacah_simbol_lubang_bukan_awal` **118** · `cacah_bangkit` **8** · semua `selisih_*` 0.
**`cacah_baris_penyebut_butir_1_dilapor` 60 vs `penyebut_butir_1` 118 → 58 baris hilang.**

`baris_penyebut_butir_2` — **5 dari 5, LENGKAP**:

| simbol | `bulan_pertama` | `cacah_bulan` | `cacah_lubang` | `cacah_lubang_awal` | `akhir_lubang_awal` (INKLUSIF) |
|---|---|---|---|---|---|
| **BNXUSDT** | **2022-05** | **48** | 19 | **7** | **2023-01** |
| ICPUSDT | 2021-05 | 62 | 16 | 16 | 2022-08 |
| JUPUSDT | 2024-01 | 30 | 1 | 1 | 2024-01 |
| QTUMUSDT | 2020-02 | 77 | 1 | 1 | 2020-02 |
| TLMUSDT | 2021-07 | 60 | 20 | 20 | 2023-02 |

**Empat dari lima kontigu** (16=16, 20=20, 1=1, 1=1); **hanya BNXUSDT tidak** (7 dari
19). Rentetan 2022-05..2023-01 = **9**; 9 − 7 = **2** — **selang yang sama** dengan
50 − 48 = 2. Kedua selang itu kini **bernama**: 2022-06 dan 2022-08. ✅

**Blok `uji_r305` — VONIS ALAT, BUKAN ADJUDIKASI.** Ia menyatakan sendiri butir 1 KALAH
(`bagian` **1.0** di luar pita 0.55–0.95; penyebut **118** ≥ 100) dan butir 2 KALAH
(`bagian` **0.6** < 0.8; cacah **5** di bawah pita 20–120). **Papan skor tidak disentuh**
(aturan 29, KC-49). R-305 tetap menunggu adjudikasi tangan atas jurnal 125.

### `reports/semesta_rentang.json` — tak bertanggal, 95% (tidak berubah dari v18)

Blob **`8d5bd06ca4073dac8a8ef7841d81824427cc8e63`**, **110.662 B**. Potongan hilang di
tengah, abjad **P–R**. Satu kunci akar `rentang`; tiga medan per simbol. **TANPA
`waktu_utc`, TANPA sidik.** BNXUSDT 2022-04 / 2026-06 / **51** (kontinu) ·
BNXUSDTSETTLED 6 (bentangan 11) · TLMUSDT **60** (kontinu) · TLMUSDTSETTLED 9
(bentangan 15) · MATICUSDT 48 · BTCSTUSDT 64 · SXPUSDT 71 · FTTUSDT 51 ·
1000LUNCBUSD 20 · ICPUSDT_SETTLED 9. **`cacah_bulan` BUKAN bentangan kalender.**

### `semesta_bulan_1m.json` (tidak berubah)

Blob **`a1a6d3f0f13dd7100a91853cadfcaa9a5620fee3`**, **18.884 B**, `waktu_utc`
**2026-07-28T09:44:48Z**, UTUH. `bulan_per_simbol["BNXUSDT"]` **51** ·
`["BNXUSDTSETTLED"]` **6**. **Tidak ada nama bulan.**

### `lux_ai/serapan/gerbang_1m.py` (tidak berubah — kini poros peringkat pertama)

Blob **`c8cc54c84a57173ef2e426c317d6ac50734e9b4a`**. Penerapan **ADR-A004 §2**. Enam
klausa: `deret_tidak_kosong` · `tanpa_duplikat` · `tanpa_menit_hilang` ·
`jarak_60_detik` · `selaras_menit` · `satuan_milidetik`; `lolos = not pelanggaran`.
`rentang = (unik[-1]-unik[0]) // MS_MENIT + 1`;
`menit_hilang_dalam_rentang = rentang - len(unik)`, rumus **DISALIN** (aturan 10).
**PUSTAKA MURNI** — tanpa `KELUARAN`, tanpa `jalankan`, tidak menulis laporan.
**[v19] Justru karena ia pustaka murni, utang ukur 25 tidak dapat dibayar dengan
membaca laporan mana pun** — ia menuntut pemanggilnya ditelusuri.

### `lux_ai/serapan/bulan_absen.py` (dibaca utuh, aturan 86 b)

Blob **`10279d721d66a86b6d265badf81ada3204648f69`**. `VERSI = 1` ·
`PENYEBUT_TERCATAT = 19586` · `NAMA_PENYEBUT_TERCATAT = 787` ·
`KENDALI_NAMA = ("BTCUSDT","ETHUSDT")` · `KENDALI_BULAN_MIN = 60` ·
`ABSEN_PASANGAN_JURNAL_113 = 12` · **`R288_BNX_ABSEN = 3`** · `R288_SAMA_MIN = 7` ·
`R288_JUMLAH_SEMESTA = 12` · `PEMBEDA = ("gagal_gerbang","tak_diterbitkan_arsip","tak_terukur")`.
**TIDAK ADA pembatas baris** — `baris_berabsen` lengkap.
Definisi resmi `bulan_absen` **disalin**: *"bulan kalender di antara bulan_pertama dan
bulan_terakhir sebuah simbol yang TIDAK ada di penyebut 19.586; BUKAN lubang funding dan
BUKAN lubang tengah"*. **Tepi tidak pernah absen menurut definisi → 2022-04 mustahil
muncul**, dan itu diketahui **sebelum** pita dikunci.

### `silang_funding` V2 (tidak berubah)

Blob **`b61fe8b3bcabbfce435dd5e5f78fc367f6bef617`**, `waktu_utc`
**2026-07-29T08:17:55Z**, **dibaca 54%**. `penyebut_kehidupan` **19.586** ·
`bulan_klines_funding` **19.598** · `cacah_lubang_funding` **880** ·
`cacah_lubang_tak_dikenal` **3** · `cacah_mati` **1.401** ·
`cacah_hidup_tanpa_funding` **33** · `sebaran_bentuk_semua_lubang` 45/826/0/6 = **877** ·
`bentuk_terbitan_funding` 48/826/6 = **880** · seluruh `selisih_*` **0**.
`tabel_silang`: HIDUP **18.054 / 33** · MATI **559 / 842** · SEPI **96 / 2**.
Ketiga lubang tak dikenal, semuanya BNXUSDT: **2022-04**, **2022-06**, **2022-08**.
**[v19] Ketiganya kini terjelaskan posisinya:** 2022-04 di **tepi** (di luar penyebut
karena `bulan_pertama` penyebut adalah 2022-05), 2022-06 dan 2022-08 **di dalam**
(absen, `gagal_gerbang`). **Sebab klausanya tetap BELUM DIUKUR.**

### Lubang tengah, karantina, modul lain (tidak berubah)

- **Lubang tengah:** blob `39cd1caacedc4d49ba23c91c80f553bb9fb135a6`;
  `cacah_lubang_tengah` **6**; **BTCSTUSDT 2022-01** dan **LITUSDT 2025-07..2025-11**.
  H-A011 MENANG; H-A010 MENANG 5–0 — **tabel pendukungnya cacat konvensi (butir 18)**,
  tetapi **vonis menangnya tidak berubah**.
- **Karantina:** Σ `baris_karantina` **516.135** atas **12** parquet; manifes
  **20.533.802 B**.
- **`selisih_lilin` V1:** `cacah_baris` **19586** · `cacah_berselisih` **0**.
- **`sisa_defisit` V1:** penyebut kerja **17.398** · `cacah_berdefisit` **114** ·
  `defisit_terbesar` **42.510** = **TLMUSDT 2023-03**, HIDUP, 2.130 dari 44.640 lilin.
- **`keterisian_lilin` V1:** lilin LANGSUNG **839.325.999** · defisit **18.143.601**.
- **`bulan_pertama` V1:** 37 dari 38 HIDUP-kecil adalah bulan pertama; kecualinya
  **TLMUSDT 2023-03**.
- **`lubang_tebing` V1:** `mati_dulu` **40** (0.339) · tebing `2025-07` menguasai **39**.
- **`funding.py` V6:** **87** simbol "funding tanpa klines" atas **787** (KC-52).

### Belum diukur, urut prioritas resmi — [v19] PERINGKAT SATU BERGANTI

1. **[BARU PERINGKAT 1] Klausa gerbang mana yang menjatuhkan BNXUSDT 2022-06 dan
   2022-08** (utang ukur 25). Peringkat lama ("keanggotaan penyebut BNXUSDT") **LUNAS**.
   Pertanyaannya kini turun satu lapis: dari **bulan apa** menjadi **mengapa**.
   Bahan: **ADR-A004 §2**, `gerbang_1m.py`, `tests/test_gerbang_1m.py`, pemanggilnya.
2. **Mengapa hanya BNXUSDT yang rentetan awalnya bolong** — empat simbol lubang-awal
   lain kontigu sempurna.
3. **Mengapa sembilan dari sepuluh simbol berabsen kehilangan tepat bulan settled
   terakhirnya** (utang 46, bahan KC-58).
4. **Sebab kekosongan TLMUSDT 2023-03** — bulannya ADA; isinya 95,2% kosong.
5. **Tebing funding `2025-07`** (39 simbol) dan **BTCSTUSDT** (kontigu 64, `cacah_mati`
   **63**) — keserian **BELUM diukur** dan **DILARANG diklaim**.
6. **Identitas dua belas simbol-bulan karantina** — menuntut **modul CI**.
7. **Penulis `semesta_rentang.json`** (utang 42).
8. Sisanya: selisih 40−38 `diagnosa_kc15`; bentangan 38 kohort; H-A016; `mati_tersisip`
   atas 19.586; **`ukur_baris` V6**; R-7/19/20/28/36/37 dan R-199; R-236..R-247;
   **R-288 dan R-290**; **R-305 (adjudikasi tangan)**; taksonomi lubang tiga kelas;
   **bagian `baris_mati` yang belum terbaca**.

**Prasyarat klasifikasi — SATU BLOKIR MENYEMPIT, LIMA TETAP.** Serapan funding **matang
sebagai pembukuan, belum matang sebagai landasan fitur**:
(1) **ADR-A003 belum ada** — tidak bergerak;
(2) **keanggotaan penyebut — MENYEMPIT TAJAM**: tiga angka bersaing (48/50/51) kini
    **terdamaikan aritmetis untuk BNXUSDT**, dan **nama** ketiga bulannya terukur.
    **Yang tersisa: 786 simbol lain belum diperiksa.** Blokir ini turun dari "tidak
    dipahami" menjadi "dipahami pada satu contoh";
(3) **`baris_mati` terpotong 54%** — tidak bergerak;
(4) **kelas positif 33 dari lima simbol** (KC-47) — tidak bergerak;
(5) **787 lawan 787 belum didamaikan** (KC-52) — tidak bergerak;
(6) **taksonomi lubang masih BENTUK, bukan MEKANISME** — **mulai bergerak**: sebelas
    bulan absen kini punya **mekanisme bernama** (`gagal_gerbang`), yang pertama kalinya
    sebuah kelas lubang disertai sebab terukur alih-alih bentuk. **DILARANG** menyebut
    blokir ini terbayar; satu kelas dari beberapa.

## Penomoran berikutnya

Aturan resmi **1–81, 83, 84, 85, 86 (a) dan (b), 87, 90** · usulan **77**, **78**,
**82**, **88**, **89**, **91** · **aturan berikutnya yang bebas 92** · KC resmi sampai
**KC-55** (KC-16 kosong selamanya), **KC-56, KC-57, KC-58 diusulkan** · **KC berikutnya
KC-59** · Hipotesis: H-A016 (belum diuji), H-A017 (dilemahkan R-306), H-A018 (tafsir
dibatasi), H-A019 (DITERIMA TERBATAS), **H-A020 dan H-A021 (uji MUSTAHIL)**, H-A022
(TERBUKTI), H-A011 (TERBUKTI, larangan generalisasi), **H-A023 (DIUSULKAN — BERSYARAT
dengan aritmetika TERTUTUP: 51 − 50 = 1 di tepi, 50 − 48 = 2 di dalam, ketiganya
bernama; keanggotaan penyebut terukur untuk SATU simbol saja; DILARANG ditulis
TERBUKTI)** · Hipotesis berikutnya **H-A024** · Jurnal berikutnya **152** ·
`STATE.md` berikutnya **v61** · EKOR berikutnya **v20** · **UKUR berikutnya v19 (utang
hidup; trio akar TIDAK SERASI sampai ia naik)** · PROMPT berikutnya **v55 (belum
didorong, umur sebelas versi)** · ADR berikutnya **A022** · Ramalan berikutnya **R-319** ·
**papan skor 329 — SAH sejak berkas ini**.

**Syarat praregistrasi R-319 — EMPAT BELAS syarat kumulatif** (tidak bertambah dari
R-318): aturan **79** (di `journal/**`, sebelum bahan dibuka) · **83** · **84** · **85** ·
**86 (a) dan (b)**, dengan penyebutan bahwa daftar `reports/` baru terbaca **76%** ·
**87** · **90** (bila laporan CI dibaca) · pemeriksaan **kebebasan medan terhadap kode**,
tertulis, sebelum pita dikunci · **KC-50** · **KC-52** · **KC-53** · **KC-54** (definisi
tiap medan **disalin**; bila tak ditemukan, **syarat gugur tersurat WAJIB**) · **KC-55**
(pita menutup **ketiga sisi**) · **KC-56** (bila bahan tak bertanggal, nyatakan bahwa
perbandingan waktu tidak dipakai) · aturan **66**. Semangat **usulan 88**, **89**, dan
**[BARU] 91** ditaati sukarela — 91 menuntut korelasi antarbutir dinyatakan terbuka.

**Syarat bahan yang tetap berlaku:** bahan ramalan **DILARANG** berupa berkas yang sudah
dibuka pada sesi ini — termasuk `semesta_rentang.json`, `semesta_bulan_1m.json`,
`gerbang_1m.py`, `silang_funding.json`, **`lubang_awal.json`**,
**`bulan_absen_ringkas.json`**, **`lubang_awal.py`**, dan **`bulan_absen.py`**.
