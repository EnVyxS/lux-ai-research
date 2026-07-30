# STATE lampiran EKOR — bagian 2 dari STATE (v15, milik STATE v56)

**Mengapa berkas ini ada.** Dua push `STATE.md` berturut terpotong (v41, v42);
pemecahan ke tiga berkas berlaku sejak v43 (KC-42). Pembagian yang berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, 83, 84, 85, 86; KC-1..**KC-53**.
2. **`STATE_LAMPIRAN_EKOR.md`** (berkas ini, v15) — bagian 2: papan skor, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** — bagian 3: pengukuran, modul, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) dan **`PROMPT_KELANJUTAN.md`**
   (blob `35beed44`) — **arsip; BUKAN sumber** (ADR-A018 kep. 9).

Dasar v15: EKOR v14 (blob **`5d481f9b0fd6adca53e8ba145f3fbd6cfeca20a4`**), **dibaca
UTUH pada giliran yang sama sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43).

## KESERASIAN VERSI — dibaca apa adanya, termasuk yang belum serasi

Saat berkas ini didorong:

- `STATE.md` **v56** — blob **`3ac9c3698583b2e528015a5d36bfb9aa1cc3bd0c`**, commit
  **`019d16eaa7d2dbd1a97a2f10b2db6d9cae1d1bc7`**, dibaca ulang UTUH pada giliran yang
  sama ia didorong. **SERASI** dengan berkas ini.
- `STATE_LAMPIRAN_EKOR.md` **v15** — berkas ini.
- `STATE_LAMPIRAN_UKUR.md` masih **v14** — blob
  **`69d95bc490441ff19f74b4ac5a1b3e8258fdbacb`**, commit `6157586e`. **TERTINGGAL SATU
  VERSI.** Kepalanya berbunyi "milik STATE v55". Ia **tidak memuat**: ADR-A020, KC-53,
  aturan 86 butir (b), usulan aturan 87, adjudikasi R-314, H-A011 TERBUKTI, mustahilnya
  uji lubang tengah bagi H-A020/H-A021, jurnal 142 dan 143, serta aturan 38 ke-50, ke-51,
  ke-52. **Sampai UKUR v15 naik, sumber sah untuk seluruh butir itu adalah `STATE.md`
  v56, berkas ini, ADR-A020, dan jurnal 142–143** — bukan UKUR v14.

**Satu berkas per push tetap MENGIKAT** (KC-42, KC-43).

**Tentang push berkas ini:** ia di akar repo sehingga menyalakan `ci.yml`. Tidak satu
pun `tests/**` berubah, jadi cacah uji tetap **1377** — ramalan deterministik, **MUDAH**,
TIDAK diskor, TIDAK menambah beruntun aturan 57. **Laporannya WAJIB dibaca sebelum push
akar berikutnya**, atau ia hangus seperti run `30547842823`.

## KESALAHAN DOKUMEN SENDIRI — kini TIGA BELAS, dengan calon keempat belas

Daftar ini disalin dari STATE v56 dan berlaku identik di ketiga bagian. Sebab tetap
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
| 8 | STATE v53 aturan 45 | "empat push terakhir" lalu mendaftar ENAM | "enam push terakhir" | LUNAS di STATE v54 |
| 9 | STATE v53 aturan 52 | pembacaan ulang "tidak menangkap satu pun" | **satu dari delapan** | LUNAS di STATE v54 |
| 10 | jurnal 138 §5 butir 2 | "maka **839.842.134 yang keliru**" | kesimpulan **tidak sah dari premisnya**; kedua angka benar | LUNAS di jurnal 140 |
| 11 | jurnal 141 §6 | tuduhan atas EKOR v13 **dan ADR-A019** | tuduhan **terlalu luas**; diadili dari sumber | LUNAS di EKOR v14 |
| 12 | **ADR-A019 kep. 9** | poros identitas 12 karantina disebut **"termurah"**; gugus lubang tengah dilabeli `2022-05`/`2024-05` | manifes **20.533.802 B** → mustahil dibaca; bulan sebenarnya **BTCSTUSDT 2022-01** dan **LITUSDT 2025-07..2025-11** | LUNAS di ADR-A020 kep. 8 |
| 13 | **jurnal 142 §4** | angka **880 / 877 / 3** diumumkan sebagai temuan baru | ketiganya **sudah tertulis di STATE v55**; yang baru hanya **letak** selisih 3 di kelas AWAL | LUNAS di STATE v56 |
| **14 (calon)** | **STATE v56, keserasian nomor 2** | blob EKOR v14 ditulis berbelit: "blob `a722ec63…` salah; blob yang benar `5d481f9b…` (commit `a722ec63`)" | commit tertukar dengan blob lalu **dikoreksi di tempat**, bukan ditulis bersih | **AKTIF — dijadwalkan LUNAS di STATE v57** |

### Butir 13 — bentuk halus KC-19, dan mengapa ia layak masuk daftar

Jurnal 142 §4 menyajikan irisan **880 lubang funding semesta lawan 877 di dalam
penyebut, selisih 3 tak dikenal** sebagai temuan giliran itu. Pembacaan utuh STATE v55
menunjukkan bagian "Angka semesta yang mengikat" **sudah memuat ketiga angka itu**.
Maka yang benar-benar baru hanya satu hal: **seluruh selisih 3 duduk di kelas AWAL**
(48 − 45 = 3; ekor 826 − 826 = 0; tengah 6 − 6 = 0). Rumusan resmi STATE v56, dikutip
apa adanya:

> Ini kelas KC-19 dalam bentuk halus: mengumumkan sebagai baru apa yang sudah tertulis
> di dokumen sendiri.

**Penangkalnya sudah ada dan tidak dipakai:** aturan 52. Berkas sendiri dibaca ulang
berkali-kali, tetapi tidak dibaca **untuk mencari klaim tandingan**. Ini kembali
memperkuat batas kekuatan aturan 52 yang dirumuskan di v14: pembacaan ulang **dokumen
sendiri** lemah, pembacaan **kode** kuat.

### Batas kekuatan aturan 52 — rumusan yang berlaku

> Pembacaan ulang **dokumen sendiri** lemah terhadap penalaran cacat: ia membaca
> kalimat yang sudah diyakini benar. Pembacaan **kode** kuat terhadapnya: kode
> menyatakan identitas yang tidak dapat ditawar, dan ketidakcocokan antara docstring
> dan badan fungsi tampak begitu keduanya dibaca berdampingan.

**Dua bukti sekarang, bukan satu:** pembacaan ulang trio `c1dc0009` menangkap arah
selisih R-312 yang mustahil positif (kekuatan atas kode); dan butir 13 di atas adalah
kegagalan pembacaan ulang dokumen menangkap klaim kebaruan yang keliru (kelemahan atas
dokumen). **DILARANG** menulis bahwa aturan 52 menjaga mutu penalaran **atas dokumen**.

## KC-43..KC-53 (teks lengkap KC-43..KC-47 di STATE v47, KC-49 di v48, KC-50 di v50, KC-51 di v52, KC-52 di v54, **KC-53 di v56**)

- **KC-43** — tanda tangan fungsi dari INGATAN. Penangkal: baca modul yang diimpor
  UTUH pada giliran yang sama.
- **KC-44** — semua laporan di-commit satu langkah.
- **KC-45 [RESMI v45]** — satuan "bulan tanpa funding" vs "bulan MATI" dicampur.
- **KC-46 [RESMI v45]** — lubang bentuk AWAL dibaca sebagai "funding berhenti".
- **KC-47 [RESMI v46]** — satu peristiwa menyamar sebagai banyak pengamatan bebas.
  Kasus kuat: TUJUH dari sembilan baris MATI tak penuh R-310 berbulan `2024-05` dalam
  jendela **9 lilin**. Diperiksa untuk R-311 dan TIDAK terpicu (ADR-A018 kep. 4).
  Diperiksa untuk R-313 dan TIDAK terpicu: dua belas parquet karantina tersebar di
  **enam pecahan berbeda** dengan cacah 3/3/1/1/3/1. **[v15] Terpicu KUAT pada H-A011:**
  keenam bulan HIDUP LITUSDT 2026-01..2026-06 adalah **satu simbol, satu rentetan
  berturut** — bukan enam pengamatan bebas. Inilah dasar larangan generalisasi
  ADR-A020 kep. 1.
- **KC-48 [RESMI v47]** — ambang absolut pada besaran yang sebarannya belum diukur.
- **KC-49 [RESMI v8 lampiran ini]** — pita dikunci tanpa aritmetika implikasi.
  Penangkalnya berlaku sebagai aturan 83. Tercatat ditaati DI DALAM KODE R-312: lantai
  aritmetis 12 diturunkan tertulis dari 516.135 / 44.640 = 11,56… dibulatkan ke atas.
  **[v15] Ditaati lagi pada R-314 butir 1:** pita [747, 827] dikunci mengelilingi
  penyebut simbol yang sudah tercatat, dan kena di **787**.
- **KC-50 [RESMI di STATE v50]** — agregat lewat jalan memutar, sehingga selisih
  terhadap sumber lain mustahil terlihat. **Cacat kelas ini tidak menghasilkan galat;
  ia menghasilkan kesunyian.** Kasus 839.842.134 lawan 839.325.999 SELESAI, tetapi
  tidak dengan cara yang KC-50 ramalkan. Kasus `total_byte` `irisan_byte` dan tautologi
  712.925 tetap berlaku penuh.
- **KC-51 [RESMI v52]** — **bias taksiran pemusatan**: besaran yang belum pernah diukur
  sebarannya secara sistematis ditaksir **lebih menyebar** daripada kenyataannya.
  Empat kejadian berturut tanpa satu pun pembalikan arah: R-308 butir 2 (10..300 → **2**);
  R-310 butir 2 (pita 0,02..0,25 → **0,0445**); R-311 butir 1 (pita 200..12.000 → **114**,
  faktor **26,3**); R-311 butir 2 (pita 0,02..0,45 → **0,4087**). **[v15] TIDAK mendapat
  kejadian kelima, dan sekali ini karena alasan yang sehat:** R-314 butir 1 memakai pita
  **sempit** [747, 827] yang diturunkan dari penyebut tercatat, dan menang. Itu **bukan**
  bukti kalibrasi membaik — lihat larangan di bawah papan skor.
- **KC-52 [RESMI di STATE v54, DITUTUP pada giliran yang sama]** — **dua penyebut
  berbeda diperlakukan sebagai satu.** Ketika dua angka besar atas "semesta yang sama"
  tidak cocok, kemungkinan pertama yang wajib diperiksa bukanlah bahwa salah satunya
  keliru, melainkan bahwa keduanya **mencacah himpunan yang berbeda**. Sebab
  strukturalnya terukur: `kehidupan_arsip.peta_parquet` **melewatkan baris
  `parquet_karantina`**. Kelas ini **DITUTUP sebagai teka-teki, TETAP HIDUP sebagai
  pola** — 19.586 lawan 19.598, **880 lawan 877**, 18.799 lawan 17.398. **[v15] Pasangan
  penyebut mirip yang paling berbahaya kini tercatat: 787 simbol klines lawan 787 simbol
  funding.** Keduanya **sama besar**, sehingga tidak ada selisih yang menyalakan alarm;
  kesamaan angka **DILARANG** dibaca sebagai kesamaan himpunan sampai irisannya diukur.
  Kerabat: KC-25, KC-36, KC-39, aturan 44.
- **KC-53 [RESMI di ADR-A020 kep. 3, diserap STATE v56]** — **nol pada sebuah medan
  dibaca sebagai ketiadaan fenomena.** Kasus asal: `cacah_simbol_bangkit_dapat_diuji`
  = 0 pada `kohort_ekor` V4 dibaca sebagai "tidak ada kebangkitan di semesta". Yang
  benar: tidak ada kebangkitan **yang dapat diuji menurut definisi kohort ekor**. Enam
  bulan HIDUP LITUSDT membuktikan fenomenanya ada. Kelas sama dengan Koreksi 10:
  kesimpulan tidak sah dari premis yang benar. **Mengutip nol itu sebagai bukti
  ketiadaan kebangkitan DILARANG.** Penangkal: **penyebut dan definisi medan wajib
  ditulis pada kalimat yang sama dengan angkanya.** Kerabat: KC-21, KC-37, KC-41,
  aturan 46, aturan 59.
- **KC berikutnya yang bebas: KC-54.**

## Papan skor prediksi — lengkap R-300..R-314 (R-199..R-299 di v4, blob `67dda29e`)

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
| R-311 | (1) cacah baris bukan-pertama bukan-MATI berdefisit, dari **17.398**, dalam **200 .. 12.000**; (2) bagian sisa 712.925 yang ditanggung SEPULUH teratas, dalam **0,02 .. 0,45**; (3) sepuluh invarian nol + tiga kendali + penggugur + kode 0 + CI | **SEPARUH** — butir 1 **KALAH** (**114**, lantai aritmetis 16); butir 2 **MENANG** (**0,4087**, tipis ke tepi ATAS); butir 3 MUDAH |
| R-312 | (1) cacah baris berselisih antara `cacah_lilin` dan `cacah_lilin_terbaca`, dari 19.586, dalam **12 .. 120**; (2) bagian selisih yang ditanggung baris teratas dalam **0,50 .. 0,865**; (3) penggugur + kendali + kode 0 + CI | **TIDAK TERADJUDIKASI** — `cacah_berselisih` **0**, penyebut butir 2 NOL (aturan 41). Vonis DIPERBERAT di v14: butir 2 **mustahil dimenangkan secara struktural**. |
| R-313 | (1) Σ `baris_karantina` atas delapan `reports/pulihkan_pecahan_<i>.json` = **516.135**; (2) Σ parquet karantina = **12** | **TEPAT (2/2)** — keduanya selisih **0**, dengan **cacat aturan 79 melekat permanen** |
| **R-314** | (1) `cacah_per_simbol_funding` ∈ **[747, 827]**; (2) `h_a010_cacah_simbol_berisi` = **0**; (3) `h_a011_cacah_hidup` = **0** | **2 TEPAT / 1 MELESET** — **787** TEPAT · **0** TEPAT · **6** **MELESET**. Kelima penggugur lolos; **syarat gugur 5 MENYALA**. Butir 2 dan 3 **TURUNAN dari docstring** (lihat catatan kejujuran 1). |

**Total R-1..R-314** (dihitung TANGAN dari rincian v14, aturan 21):

- TEPAT **220**
- MELESET **58**
- SEPARUH **22**
- TIDAK TERADJUDIKASI **9**
- MENUNGGU **7** (R-7, R-19, R-20, R-28, R-36, R-37, R-199)

220 + 58 = 278; 278 + 22 = 300; 300 + 9 = 309; 309 + 7 = **316** ✅ Nomor terpakai
R-1..R-314. N_percobaan = 0. **ADJUDIKASI RISET TETAP TERKUNCI.**
**Pertambahan dari 313:** TEPAT **+2**, MELESET **+1**, seluruhnya dari **R-314**;
lajur lain tidak bergerak.

**Kolom terpisah — DI LUAR lajur papan skor:** **R-229 TEPAT** dan **R-230 MELESET**,
keduanya terbaca dari docstring `lubang_tengah.py` V2 dan dikonfirmasi oleh laporan
(ADR-A020 kep. 5). Keduanya **TIDAK dimasukkan ke lajur** karena pemeriksaan berurutan
R-224..R-235 belum dilakukan; memasukkan dua butir dari tengah blok yang belum diperiksa
akan membuat papan skor mencacah himpunan yang tidak jelas batasnya (KC-52 dalam bentuk
papan skor). **R-228 tetap BELUM diadjudikasi** — ia menuntut laporan CI atas commit V2
`lubang_tengah` (run 30436915256 atau berikutnya).

**Nisbah papan skor, dihitung tangan dan disebut apa adanya:** dari 300 ramalan yang
beradjudikasi penuh (220 + 58 + 22), TEPAT **73,3%**, MELESET **19,3%**, SEPARUH
**7,3%**. Angka itu **DILARANG dibaca sebagai mutu ramalan**: sebagian besar butir
ketiga tiap ramalan berlabel MUDAH dan tidak berisiko. **R-312 DILARANG masuk pembilang
maupun penyebut nisbah ini.**

**Utang papan skor:** rincian R-236..R-247 masih di jurnal 92–94; pemeriksaan
R-224..R-235 belum dikerjakan.

### [v15] R-314 — kemenangan yang wajib diperkecil sendiri

Tiga butir, dua menang. Tetapi **hanya butir 1 yang murni**: pita [747, 827] dikunci
dari penalaran sendiri atas penyebut simbol, dan kena di **787**.

**Butir 2 dan 3 TURUNAN dari docstring `lubang_tengah.py` V2**, yang sudah menuliskan
harapan penulis modulnya. Maka:

- Kemenangan butir 2 **bukan kemenangan penalaran baru** — ia menyalin harapan orang
  lain yang kebetulan benar.
- Kekalahan butir 3 adalah **kekalahan karena mempercayai penalaran orang lain tanpa
  memeriksanya**. Kodenya ada di repo; ia tidak dibaca ulang untuk butir ini.

Inilah dasar **usulan aturan 87**: ramalan yang diturunkan dari praregistrasi orang lain
(termasuk docstring modul) **wajib ditandai TURUNAN di muka**, dan **DILARANG dihitung
sebagai bukti kalibrasi** ke arah mana pun. Aturan 87 **DIUSULKAN, BELUM RESMI** —
ADR-A020 kep. 7 menolak meresmikannya karena kejadiannya masih **satu**.

### [v15] Aturan 85 mendapat adjudikasi pertamanya

Aturan 85 berlaku sejak R-312 dan sampai v14 **belum pernah punya satu pun adjudikasi**.
R-314 memberinya yang pertama. **Yang DIIZINKAN dikatakan:** aturan 85 **pernah teruji
sekali**. **Yang DILARANG:** menyebutnya **teruji**, **bekerja**, atau **terbukti**. Satu
adjudikasi bukan pengujian; ia titik data pertama.

### Lima larangan permanen yang menempel pada R-312 (tidak berubah di v15)

1. **DILARANG** mengatakan pita butir 1 (12..120) "tidak terbantah". Ia tidak diuji.
2. **DILARANG** mengatakan kalibrasi membaik atau memburuk karena R-312.
3. **DILARANG** menghitungnya di pembilang maupun penyebut nisbah kemenangan.
4. **DILARANG** menghidupkannya kembali dengan alasan penjelasannya kini ditemukan.
5. Angka **12** di R-313 adalah cacah **parquet karantina** — arti berbeda dari 12 di
   R-312 butir 1. **Kesamaan itu DILARANG dibaca sebagai konfirmasi apa pun.** Larangan
   ini **berasal dari praregistrasi** (syarat gugur nomor 3 di docstring modul dan
   jurnal 136), **bukan** dari adjudikasi.

### [v15] Enam larangan baru yang lahir bersama STATE v56

1. **DILARANG** mengutip `cacah_simbol_bangkit_dapat_diuji` = 0 sebagai ketiadaan
   kebangkitan (KC-53).
2. **DILARANG** menyebut poros identitas 12 karantina "termurah" (manifes 20.533.802 B).
3. **DILARANG** menyebut adanya lubang tengah di gugus `2022-05` atau `2024-05` — tidak
   ada satu pun di sana.
4. **DILARANG** menyamakan **787 simbol funding** dengan **787 simbol klines** sebelum
   irisannya diukur.
5. **DILARANG** menyebut aturan 85 "teruji".
6. **DILARANG** menggeneralisasi kebangkitan LITUSDT ke semesta — satu simbol, satu
   rentetan (KC-47).

## Catatan kejujuran [v15]

1. **Kekalahan ramalan disebut telanjang.** R-314 butir 3 meramalkan
   `h_a011_cacah_hidup` = **0**; terukur **6**. H-A011 **MENANG**, dan ini **kebangkitan
   pertama yang terukur di repo ini**. Ramalan itu diturunkan dari docstring, bukan dari
   pemeriksaan sendiri atas kode — kekalahannya karena itu **layak**.
2. **Poros yang dikira menjawab dua hipotesis ternyata menjawab NOL.** STATE v55
   menetapkan uji H-A020 dan H-A021 sebagai "lubang tengah pada gugus `2022-05` dan
   `2024-05`". Keenam lubang tengah yang terukur — BTCSTUSDT **2022-01** dan LITUSDT
   **2025-07..2025-11** — **tidak menyentuh satu pun bulan itu**. Rumusan resmi STATE v56:

   > Uji yang direncanakan bagi H-A020 dan H-A021 **MUSTAHIL** — bukan mahal, bukan
   > tertunda, melainkan **tidak ada bahannya**.

   Keduanya kini berstatus **DIUSULKAN, BELUM DIUJI, TANPA JALAN UJI YANG DIKETAHUI**.
   Label `2022-05` sendiri ternyata **`bulan_klines_pertama` BNXUSDT** pada tabel H-A010;
   bagaimana ia berpindah menjadi label poros **tidak diukur**, karena itu **tidak
   diklaim** (aturan 21).
3. **Aturan 79 DITAATI SEPENUHNYA pada R-314 — pertama kali sejak R-313 melanggarnya.**
   Praregistrasi R-314 ditulis di `journal/2026-07-30-142.md` **sebelum** laporan dibuka.
   Aturan 79 **tetap PENUH**; cacat R-313 tetap melekat permanen. **DILARANG** menyebut
   aturan 79 lemah, longgar, atau opsional.
4. **Aturan 86 kini punya empat kejadian, dan yang keempat berlawanan arah.** Tiga
   kejadian pertama semuanya "pekerjaan sudah ada, kami tidak memeriksa": biaya uji
   pemisah ditaksir empat langkah padahal satu pembacaan (jurnal 138 §4); `selisih_lilin`
   + 36 uji + satu workflow ditulis untuk angka yang **sudah tersimpan** (jurnal 140 §7);
   `reports/lubang_tengah.json` **sudah ada sejak 2026-07-29T09:38:52Z**, dua hari sebelum
   pertanyaannya dirumuskan (jurnal 143 §5). **Kejadian keempat berarah sebaliknya:**
   poros karantina ditaksir **terlalu murah** ("termurah") padahal mustahil. **Aturan 86
   butir (b) diresmikan** karena ini: sebelum menulis modul atau ramalan, **praregistrasi
   docstring modul terkait wajib diperiksa**.
5. **Aturan 57 beruntun 4 dari 4, dan tidak bertambah.** Tidak ada berkas uji baru sejak
   trio `c1dc0009`. Ia satu-satunya lajur yang belum pernah kalah sejak putus di 26/27,
   dan satu-satunya alasan ia tidak dibanggakan adalah ia **mencacah, bukan menaksir**.
6. **Aturan 36 mendapat kasus kedua [v15]:** `lubang_tengah` **memakai**
   `silang_funding.bentuk_lubang_lokal` alih-alih menyalin definisinya, sehingga sebaran
   bentuk tidak dapat menyimpang diam-diam antar modul. Kasus terkuat tetap yang pertama:
   `selisih_lilin` dan `pulihkan` bertemu di **839.325.999** sampai satuan terakhir, lewat
   dua jalur, dua modul, dua run, berjarak tiga hari.
7. **Aturan 46 mendapat kasus ketiga [v15]:** `funding_tanpa_klines` menolak menyatakan
   `kosong_seluruhnya` **true** bila ada baris tanpa medan — ia menolak menyimpulkan dari
   ketiadaan pengukuran.
8. **Aturan 52 ditaati sebelas kali berturut**, dan utang bacanya bertambah satu:
   **`tests/test_lubang_tengah.py`** (56 butir menurut R-228) **belum pernah dibaca**.
9. **`PROMPT_KELANJUTAN.md` tetap belum diberi kepala "ARSIP — BUKAN SUMBER"** dan
   `PROMPT.md` **v55 belum didorong**. Sampai itu dikerjakan, satu-satunya penjaga adalah
   larangan tertulis di STATE v52–v56 dan di berkas ini.
10. **Pemeriksaan silang yang menutup tanpa sisa** (terbitan, TIDAK diskor):
    18.799 − 1.401 = **17.398**; 18.087 − 17.318 = **769**; 98 − 80 = **18**;
    769 + 18 = **787** = `cacah_simbol`; **19.586 + 12 = 19.598**;
    **839.325.999 + 516.135 = 839.842.134**; **880 − 877 = 3**, seluruhnya di kelas AWAL
    (48 − 45); **6 − 6 = 0** untuk kelas tengah; `selisih_lubang_tengah` **0**.

**Kesalahan proses [v15].** Satu-satunya kegagalan panggilan alat sepanjang sesi tetap
tercatat: pada giliran push STATE v55, `push_files` **ditolak** karena bungkus
`toolName`/`toolArguments` tidak dipakai. **Bukan galat alat, bukan galat GitHub,
melainkan kesalahan bentuk panggilan.** Tidak ada yang tertulis ke repo dan tip tidak
bergerak. Kerugian lain yang tetap tercatat berasal dari urutan kerja: laporan CI run
`30547842823` hangus, dan blob laporan ke-38 tidak dapat dipulihkan.

## Jumlah uji

**1377 TERUKUR, kini DELAPAN bacaan berjejak (ke-45..ke-52).**

1. blob **`cdfdee2559201306a49bc9b01f1185d7aa36eebe`**: run **30559145901**, commit
   **`c1dc0009`** (trio `selisih_lilin`), 15:57:01Z, kode 0, `1377 tests collected in 0.58s`.
2. blob **`effb3a46bc20cda5c6c5910ee926aa16c195bb68`**: run **30575123865**, commit
   **`8368ca1f`** (STATE v54), 19:30:52Z, kode 0, `… in 0.54s`.
3. blob **`8cbbd4ce7b85d9e1f217a9cefbdacfb9318dec78`**: run **30576963781**, commit
   **`6642ed68`** (EKOR v13), 19:56:30Z, kode 0, `… in 0.67s`.
4. blob **`8ec97de5af8b528276174f635e3bda9e6cc2d7ef`**: run **30577779309**, commit
   **`2bdd8233`** (UKUR v13), 20:07:50Z, kode 0, `… in 0.62s`.
5. blob **`94d270e7065218f87bd5a26c5113ed8346cf6abf`**: run **30579348728**, commit
   **`cd209f3e`** (STATE v55), 20:29:25Z, kode 0, `… in 0.61s`.
6. **[v15]** blob **`04bfa2ed5fb43f128f8ee2351f41722314685a03`**: run **30580133552**,
   commit **`a722ec63`** (EKOR v14), kode 0, `… in 0.46s` — **tercepat yang pernah
   tercatat**.
7. **[v15]** blob **`aeb4315ad73806b61f734f9c1d92b27b1ae2727b`**: run **30581703827**,
   commit **`6157586e`** (UKUR v14), 21:02:01Z, kode 0, `… in 0.61s`.
8. **[v15]** blob **`19785af1d96fdc1fabec2dfa9f7c3dbaf60b3708`**: run **30583686515**,
   commit **`019d16ea`** (STATE v56), 21:31:10Z, kode 0, `… in 0.61s`.

Turunan: 1341 + **36** butir `tests/test_selisih_lilin.py` = **1377** ✅ (aturan 21),
terverifikasi dari sumber, bukan dari ingatan.

Riwayat panjang: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 →
984 → 1044 → 1100 → 1168 → 1233 → 1297 → 1341 (enam run) → **1377** (delapan run berjejak).

Cacah per berkas uji (**milik repo riset ini — bukan repo warisan**):
`test_irisan_byte.py` **68** · `test_bulan_pertama.py` **65** ·
`test_keterisian_lilin.py` **64** · `test_bentangan_kohort.py` V2 **63** (dicacah
TANGAN, `test_01`..`test_63`) · `test_lubang_tebing.py` **60** ·
`test_sebab_bangkit.py` **57** · `test_byte_semesta.py` **56** ·
`test_lubang_awal.py` **48** · `test_tersisip_semesta.py` **47** ·
`test_anatomi_tengah.py` **47** · `test_sisa_defisit.py` **44** (dicacah TANGAN) ·
`test_selisih_lilin.py` **36** (dicacah TANGAN dari sumber) · `test_terhenti.py` V4
**33** · `test_bulan_absen.py` **32** · `test_karantina_semesta.py` **28** ·
`test_silang_settled.py` **24** · `test_ukur_baris.py` **3**.
**`tests/test_lubang_tengah.py` — 56 butir menurut R-228, BELUM DIBACA, karena itu
DILARANG dikutip sebagai cacah terukur.**

**Aturan 57: beruntun 4 dari 4** sesudah putus di 26/27. Hanya push yang menyentuh
`tests/**` yang dihitung.

### ORDINAL ATURAN 38 — buku besar, kini sampai ke-52

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
| 49 | 1377 | 30579348728 | `cd209f3e` | `94d270e7` | EKOR v14, STATE v56 |
| 50 | 1377 | 30580133552 | `a722ec63` | `04bfa2ed` | jurnal 142, STATE v56 |
| 51 | 1377 | 30581703827 | `6157586e` | `aeb4315a` | jurnal 142, STATE v56 |
| **52** | **1377** | **30583686515** | **`019d16ea`** | **`19785af1d96fdc1fabec2dfa9f7c3dbaf60b3708`** | **berkas ini** |

**Pemakaian berjalan = ke-lima puluh dua.** Pemakaian ke-52 dibaca
**2026-07-30T21:31:10Z**, kode keluar **0**, atas push STATE v56 — **dibaca sebelum
tertimpa**, sehingga ramalan "CI tetap 1377" untuk push itu **TERUKUR dan TEPAT**, tetap
**MUDAH**, tetap tidak diskor, tetap tidak menambah beruntun aturan 57.

**[v15] Sebelas pembacaan berturut (ke-42..ke-52) tanpa satu pun laporan hangus.**

**Dua cacat tetap disebut apa adanya:** baris ke-**38** (run `30541051907`, CI 1297,
commit `5d7d8b96`) **tanpa blob**, tidak dapat dipulihkan — ordinal ini karena itu sah
**relatif terhadap definisi di atas**, bukan sebagai pencacahan mutlak; dan run
**30547842823** (bot `de2fc03d`) **tidak pernah dibaca**, sudah tertimpa, **DILARANG
dihitung**, ramalannya **DILARANG diklaim menang**. Bila jejak pembacaan lain ditemukan
di jurnal 133–134, nomor ini **WAJIB dikoreksi, bukan dipertahankan**.

**Calon aturan** — dua push akar berturut tanpa membaca laporan di antaranya pasti
menghanguskan yang pertama — **tetap DITOLAK diresmikan** (ADR-A019 kep. 3): masih
**satu** kejadian.

## Utang verifikasi

1-5, 11 menunggu tahap juri. 6-23, 25-29, 31 LUNAS. **Nomor utang BUKAN nomor ramalan
— KC-32.**

24. **AKTIF. LUNAS BARU [v15]:**
    - **`lux_ai/serapan/lubang_tengah.py` V2 dibaca UTUH** — blob
      **`4d3beaf18c070d2931044c50dd5a354d75eaceb8`**, 23.745 B.
    - **`reports/lubang_tengah.json` dibaca UTUH** — blob
      **`39cd1caacedc4d49ba23c91c80f553bb9fb135a6`**, 11.014 B.
    - **`journal/2026-07-30-142.md` dibaca UTUH** — blob `af11d8a2…`, commit `ae867f2e`.
    - **`journal/2026-07-30-143.md` dibaca UTUH** — blob `fb4ec5ad…`, commit `d92ba0f1`.
    - **`decisions/ADR-A020.md` dibaca UTUH** — blob `200c7e7d…`, commit `d8335be1`.
    - **`STATE.md` v56 dibaca UTUH** — blob `3ac9c369…`, commit `019d16ea`.
    - **EKOR v14 dibaca UTUH** pada giliran ini — blob `5d481f9b…`.
    - `reports/ci_terakhir.json` (`04bfa2ed`, `aeb4315a`, `19785af1`) dibaca utuh, blob
      DICATAT.
    **TETAP BELUM:** `decisions/ADR-A002`, **A004**, **A006**, **A007**, **A008**;
    `.github/workflows/karantina_semesta.yml` (`de40fa4e`); `tests/test_pulihkan.py`
    (`11c43533`); `tests/test_rilis_karantina.py` (`739c8da9`);
    `tests/test_karantina_a006.py` (`a5a3d82f`); **BARU [v15]:
    `tests/test_lubang_tengah.py`**; **`reports/silang_funding.json`** (`b61fe8b3`).
30. **AKTIF — UTANG HIDUP, dan ADR-A019 kep. 8 MENOLAK menutupnya.** Angka
    **50 / 54 / 45** tetap **TURUNAN** dan **DILARANG dikutip sebagai terukur** sampai
    dicacah satu per satu bernomor (aturan 66, KC-33). Yang sah tetap
    **49 / 53 / 44 / 18** pada ref `3196fd98` dan `8a614567`.
32. **AKTIF — tiga butir "memerlukan verifikasi" `PETA_MODUL.md`** (repo **WARISAN**),
    utang terbuka, bukan fakta: (a) `enable_hs` tidak ditemukan di `config.py` padahal
    dipakai `strategy.py`; (b) klaim "30 pair dipilih alfabetis"; (c) klaim "kendala
    mengikat = kapasitas margin".
33. **AKTIF LAGI [v15]** — daftar kesalahan dokumen bertambah menjadi **tiga belas**;
    butir 12 dan 13 lunas di ADR-A020 dan STATE v56. **Calon butir 14 sudah
    teridentifikasi** (blob EKOR v14 ditulis berbelit di STATE v56) dan dijadwalkan lunas
    di STATE v57.
34. **AKTIF — `PROMPT_KELANJUTAN.md` belum diberi kepala "ARSIP — BUKAN SUMBER"**, dan
    **`PROMPT.md` v55 belum didorong.**
35. **LUNAS [v15]** — UKUR v14 sudah naik (commit `6157586e`, blob `69d95bc4…`).
    **Digantikan utang baru:** UKUR **v15** belum naik; sampai itu, UKUR v14 tertinggal
    satu versi (lihat keserasian di kepala).
36. **AKTIF — identitas dua belas simbol-bulan karantina belum pernah didaftar.**
    Cacah dan barisnya terukur (12 parquet, 516.135 baris), tetapi **nama simbol dan
    bulannya tidak diketahui**. Selama itu, kalimat apa pun tentang *jenis* instrumen
    yang dikarantina **DILARANG**. **[v15] Biayanya kini terukur, bukan ditaksir:**
    manifes berjumlah **20.533.802 B** — mustahil dibaca lewat alat; jalan satu-satunya
    adalah **modul CI**.
37. **AKTIF — `ukur_baris.py` V6 belum ditulis.** `BERKAS_DIUKUR` masih **21** nama atas
    ~50 modul dan ~54 berkas uji; pagar 800 baris belum pernah diuji atas ~29 modul yang
    lebih baru. `silang_funding.py` V2 kini **705 baris** — jarak ke pagar tinggal 95.
38. **BARU [v15] — R-228 belum diadjudikasi.** Ia meramalkan cacah butir CI pada commit
    V2 `lubang_tengah` (396). Menuntut laporan CI run **30436915256** atau berikutnya yang
    belum pernah dibuka. Selama itu, cacah 56 butir `test_lubang_tengah.py` **DILARANG**
    dikutip sebagai terukur.

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
  status ke arah mana pun — **TIDAK dibalik oleh R-310, R-311, R-313, R-314, A018, A019,
  maupun A020**. DITERIMA.
- **ADR-A016** (blob `209802d7`) — H-A019 diterima TERBATAS; kep. 4 **DIKOREKSI oleh
  A018 kep. 6**. DITERIMA.
- **ADR-A017** (blob `1be570f2`) — sebelas keputusan; kep. 4 **TERJAWAB PENUH oleh
  R-313**: selisih 516.135 bukan cacat, melainkan batas himpunan. DITERIMA.
- **ADR-A018** (blob `3fba599e`) — dua belas keputusan; (1) KC-51 diresmikan;
  (2) aturan 85 berlaku mulai R-312; (3) rumusan resmi R-311; (4) aturan 81 tidak
  terpicu; (5) H-A021 diusulkan; (6) A016 kep. 4 dikoreksi; (7) koreksi aturan 38;
  (8) definisi ordinal; (9) `PROMPT_KELANJUTAN.md` arsip; (10) dua cacah `tests/`;
  (11) cacah tangan 49/53/44/18; (12) poros R-312 ditetapkan. DITERIMA.
- **ADR-A019** (blob **`9cd7d25e7a61207343e60233887d06b441aa3cbf`**, commit `e6007ba5`).
  **Sepuluh keputusan:** (1) KC-52 DIRESMIKAN; (2) Koreksi 9 diakui sebagai kelas cacat
  TANPA PENANGKAL; (3) aturan 86 DIRESMIKAN; (4) R-312 TIDAK TERADJUDIKASI selamanya +
  lima larangan permanen; (5) R-313 TEPAT (2/2) dengan cacat aturan 79 melekat;
  (6) H-A022 TERBUKTI dengan batas tafsir; (7) aturan 79 DIRUMUSKAN ULANG, bukan
  dilemahkan; (8) utang cacah tangan aturan 66 DITOLAK ditutup; (9) urutan poros +
  tujuh syarat praregistrasi R-314; (10) utang aturan 52 atas trio `c1dc0009`.
  **DITERIMA — kep. 9 DIKOREKSI DUA KALI oleh A020 kep. 8.**
- **ADR-A020 — ADA [v15]** (blob **`200c7e7d737fdfa0b8d689e35482d9ae249b90ee`**, commit
  **`d8335be1198b50d8df7168a494d4f4a286617e1b`**, dibaca ulang UTUH pada giliran yang
  sama ia didorong). **Sepuluh keputusan:**
  (1) **H-A011 TERBUKTI** — LITUSDT 2026-01..2026-06 keenamnya HIDUP; kebangkitan
  **pertama yang terukur** di repo; **larangan generalisasi melekat** (KC-47: satu simbol,
  satu rentetan);
  (2) bacaan `cacah_simbol_bangkit_dapat_diuji` = 0 sebagai "tidak ada kebangkitan"
  **DICABUT**;
  (3) **KC-53 DIRESMIKAN** — nol pada medan dibaca sebagai ketiadaan fenomena;
  (4) **R-314 2 TEPAT / 1 MELESET**, papan skor **316**, dan **aturan 85 memperoleh
  adjudikasi pertamanya** (tetap DILARANG disebut teruji);
  (5) **R-229 TEPAT dan R-230 MELESET** dicatat di **kolom terpisah**, di luar lajur;
  (6) **aturan 86 diperluas butir (b)** — praregistrasi docstring wajib diperiksa;
  (7) **aturan 87 DIUSULKAN** (ramalan turunan wajib ditandai) — **ditolak diresmikan**,
  satu kejadian belum cukup;
  (8) **dua pencabutan atas ADR-A019 kep. 9** — sebutan "termurah" dan label gugus
  `2022-05`/`2024-05`;
  (9) **urutan poros diperbarui**, lubang tengah **dikeluarkan karena TUNTAS**;
  (10) utang aturan 52 dicatat dan penomoran **A021** ditetapkan. DITERIMA.
- **ADR-A021 [BELUM ADA]** — calon isinya: hasil pemisahan **880 lawan 877** lubang
  funding per kelas bentuk (`reports/silang_funding.json`, blob `b61fe8b3`), atau sebab
  kekosongan **TLMUSDT 2023-03**. **DILARANG disusun pada giliran yang sama dengan
  adjudikasi** (ADR-A016).

## Temuan sampingan

### [v15] Lubang tengah — poros TUNTAS, dan hasilnya membalik dua harapan

Sumber: `reports/lubang_tengah.json`, blob
**`39cd1caacedc4d49ba23c91c80f553bb9fb135a6`**, 11.014 B, ditulis
**2026-07-29T09:38:52Z**, `versi_lubang_tengah` **2**, `versi_funding` **6**.

**Ringkasan terukur:** `penyebut_kehidupan` **19.586** · `cacah_baris_dengan_medan`
**19.586** · `cacah_lubang_funding` **880** · `cacah_lubang_tengah` **6** ·
`selisih_lubang_tengah` **0** · `cacah_lubang_ganda` **0** · `cacah_kunci_ganda` **0** ·
`cacah_laporan_dibaca` **8** = `total_pecahan` **8** · `cacah_per_simbol_funding`
**787** · `sebaran_status_lubang_tengah` {HIDUP **0**, MATI **6**, SEPI 0, TAK_TERUKUR 0}
· `kendali_sah` **true** · `sidik_seragam` **true** · `laporan_hilang` **[]** ·
`medan_diminta` `"cacah_lilin"`.

**Keenam lubang tengah, disebut dengan nama:**

| simbol | bulan | status | rentetan | tetangga |
| --- | --- | --- | --- | --- |
| **BTCSTUSDT** | **2022-01** | MATI | 1 | 2021-12 → 2022-02 |
| **LITUSDT** | **2025-07 .. 2025-11** | MATI (kelimanya) | 5 | 2025-06 → 2026-01 |

Klines pertama BTCSTUSDT **2021-03**, LITUSDT **2021-02**; terakhir keduanya **2026-06**;
keduanya **64 bulan** klines. **Tidak satu pun berbulan `2022-05` atau `2024-05`.**

**H-A011 — MENANG, dan inilah kebangkitan pertama yang terukur:** LITUSDT
**2026-01..2026-06**, keenam bulan **HIDUP**; `h_a011_menang` true, `h_a011_terukur`
true, `h_a011_cacah_bulan` 6, `h_a011_cacah_hidup` **6**. **Generalisasi DILARANG.**

**H-A010 — MENANG 5–0:** kelima simbol (BNXUSDT 2022-05→2023-02, 48 bulan/19 lubang ·
ICPUSDT 2021-05→2022-09, 62/16 · JUPUSDT 2024-01→2024-02, 30/1 · QTUMUSDT
2020-02→2020-03, 77/1 · TLMUSDT 2021-07→2023-03, 60/20) seluruhnya `ada_medan` **true**,
`bulan` **[]**, `cacah_bulan` **0**; `h_a010_cacah_simbol_berisi` **0**;
`kosong_seluruhnya` **true**.

**Kendali:** tiga baris BTCUSDT (2021-05, 2021-08, 2021-01) semuanya HIDUP dengan
`funding_ada` true. **Sumber:** `funding_semesta.json` + `kehidupan_arsip_0..7.json`.
**Sidik kode** `c9372bd7…b3f4e` · **silang_funding** `8a9b859c…3231b1` · **data funding**
`2c9fbd1b…608d24` · **sidik kode laporan** `24b6bb26…3e8c595`.

### [v15] Angka semesta yang bertambah

- Sebaran **bentuk lubang funding, seluruh semesta**: awal **48** · ekor **826** ·
  tengah **6** = **880**.
- Sebaran **di dalam penyebut**: awal **45** · ekor **826** · tengah **6** = **877**.
- Selisih **3** seluruhnya di kelas **AWAL**; kelas ekor dan tengah **nol selisih**.
- `funding.py` V6 mencacah **87** simbol "funding tanpa klines" atas **787** simbol.

### Karantina, terukur penuh

(kedelapan `reports/pulihkan_pecahan_<i>.json`, ref `a2c4b83c`; `pulihkan` VERSI 2,
`run_id_sumber` **30396803601**, ditulis 2026-07-29T02:48Z)

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
- **Sidik kode seragam** `76c27e3c…62d700`; **sidik kode manifes seragam**
  `237ccf42…ba601` → penjumlahan lintas pecahan **sah** (aturan 22).
- **Aturan 46 terbukti bekerja:** pecahan 2 dan 5 melaporkan
  `definisi_dapat_dibedakan` **false** dan menolak memilih definisi.
- **Sebaran sangat tidak rata** — 42.585 sampai 131.760 baris per tar. Rata-rata
  **43.011** boleh dikutip sebagai turunan, **bukan sebagai bukti**.
- **Nama tar karantina:** `pecahan_<i>_karantina.part01.tar`.
- **Manifes:** delapan berkas `reports/manifes_pecahan_<i>`, jumlah **20.533.802 B**.

### `selisih_lilin` V1 — dibaca dari sumber

(blob `d19bdb5f…`, commit `c1dc0009`; laporan ringkas blob `e5cc6401…`): `cacah_baris`
**19586** · `cacah_berselisih` **0** · `jumlah_klaim_langsung` = `jumlah_terbaca_langsung`
= **839325999** · `dua_jalur_bertemu` **true** · `selisih_terhadap_warisan` bersih
**−516135** · `uji_r312.teradjudikasi` **false** · kode keluar alur modul **2**
(**dirancang**). Empat kendali lolos; `kendali_deteksi` 11 medan (klaim 213.480 · terbaca
214.360 · bersih 880 · positif 1.080 · negatif 200 · berselisih 3); `kendali_teratas`
**0,9615** = 7.500/7.800.

### Modul dan laporan lain (tetap berlaku)

- **`sisa_defisit` V1:** penyebut kerja **17.398** · `cacah_berdefisit` **114** (0,66%) ·
  `defisit_calon` **712.925** (tautologis, KC-50) · `bagian_teratas` **0,4087** ·
  `defisit_terbesar` **42.510** = **TLMUSDT 2023-03**, HIDUP, 2.130 dari 44.640 lilin
  (**95,2% kosong**) · pasangan `2022-05`: ANCUSDT **26.959** dan LUNAUSDT **26.950**,
  berselisih **sembilan lilin** (dasar **H-A021**; kalimat sebab apa pun **DILARANG**).
- **`keterisian_lilin` V1:** lilin semesta LANGSUNG **839.325.999** · MATI penuh **1.392**,
  tak penuh **9** · defisit semesta **18.143.601**, **17.335.439 (95,5%)** di bulan pertama
  dan **808.162** di bukan-pertama (bagian **0,0445**) · bulan pertama rata terisi
  **≈49,7%** · harga TIDAK tersimpan (**14** medan).
- **`bulan_pertama` V1:** 37 dari 38 baris HIDUP-kecil adalah bulan pertama (0,973684);
  satu-satunya yang bukan **TLMUSDT 2023-03**; nisbah rata byte **0,527179**.
- **`irisan_byte` V1:** zona 22.440–97.634 byte berisi **38 HIDUP dan 0 MATI**; total byte
  **32.706.262.375**; HIDUP 32.049.492.952 · SEPI 77.728.024 · MATI 579.041.399.
- **`lubang_tebing` V1:** `mati_dulu` **40** (0.339) · `serempak` **78** (0.661) ·
  `lubang_dulu` **0**; tebing `2025-07` menguasai 39 dari 40 `mati_dulu`, satu-satunya
  bukan-tebing **BTCSTUSDT** (KC-47); **122** dari 787 simbol pernah berlubang funding.

### Belum diukur, urut prioritas resmi (ADR-A020 kep. 9)

**Poros lubang tengah DIKELUARKAN dari daftar — TUNTAS oleh satu pembacaan.**

1. **Irisan 880 lawan 877 lubang funding per kelas bentuk** —
   `reports/silang_funding.json` (blob **`b61fe8b3bcabbfce435dd5e5f78fc367f6bef617`**);
   satu pembacaan, kandidat KC-52 berikutnya. **PERINGKAT PERTAMA.**
2. **Sebab kekosongan TLMUSDT 2023-03** (95,2% kosong, HIDUP).
3. Apakah **"bulan pertama di penyebut" = "bulan pertama di bursa"**.
4. **Tebing funding `2025-07`** (39 simbol) dan **BTCSTUSDT** — keserian dengan LITUSDT
   2025-07 **BELUM diukur** dan **DILARANG diklaim**.
5. **Identitas dua belas simbol-bulan karantina** — menuntut **modul CI**; manifes
   **20.533.802 B**. **Bukan kandidat murah** (koreksi A020 kep. 8).
6. Sisanya: selisih 40−38 `diagnosa_kc15`; hari hilang BNXUSDT 2022-04/06/08; bentangan
   38 kohort; H-A016; mati_tersisip atas 19.586; **`ukur_baris` V6**; R-7/19/20/28/36/37
   dan R-199; R-236..R-247 dari jurnal 92–94; taksonomi lubang tiga kelas.

## Penomoran berikutnya

Aturan resmi **1–81, 83, 84, 85, 86 (a) dan (b)** · usulan **77**, **78**, **82**,
**87** · **aturan berikutnya yang bebas 88** · KC resmi sampai **KC-53** (KC-16 kosong
selamanya) · **KC berikutnya KC-54** · Hipotesis: H-A016 (belum diuji), H-A017
(dilemahkan R-306), H-A018 (tafsir dibatasi A014/A015), H-A019 (DITERIMA TERBATAS,
dilemahkan A018 kep. 6), **H-A020 (DIUSULKAN, BELUM DIUJI, TANPA JALAN UJI YANG
DIKETAHUI)**, **H-A021 (idem)**, H-A022 (TERBUKTI lewat R-313), **H-A011 (TERBUKTI lewat
R-314, dengan larangan generalisasi)** · Hipotesis berikutnya **H-A023** · Jurnal
berikutnya **144** · `STATE.md` berikutnya **v57** · EKOR berikutnya **v16** · **UKUR
berikutnya v15 (utang hidup, tertinggal satu versi)** · PROMPT berikutnya **v55 (belum
didorong)** · ADR berikutnya **A021** · Ramalan berikutnya **R-315** · papan skor **316**.

**Syarat praregistrasi R-315 — SEPULUH syarat kumulatif** (naik dari sembilan): aturan
**79** (di `journal/**`, sebelum laporan dibuka) · aturan **83** · aturan **84** · aturan
**85** · aturan **86 (a) dan (b)** · pemeriksaan **kebebasan medan terhadap kode** ·
**KC-50** · **KC-52** · **KC-53** · aturan **66**.
