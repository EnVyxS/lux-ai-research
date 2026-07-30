# STATE lampiran UKUR — bagian 3 dari STATE (v16, milik STATE v57)

**Kedudukan berkas ini.** STATE dipecah tiga sejak v43 (KC-42). Pembagian berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, 83, 84, 85, 86 (a) dan (b), **87**;
   KC-1..**KC-54**.
2. **`STATE_LAMPIRAN_EKOR.md`** v16 (blob **`1afefb8f99aeaf5a6529a246cffa354341ee9ec2`**)
   — bagian 2: papan skor, ADR, catatan kejujuran.
3. **`STATE_LAMPIRAN_UKUR.md`** (berkas ini, v16) — bagian 3: pengukuran, modul,
   workflow, uji, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) dan **`PROMPT_KELANJUTAN.md`** (blob
   `35beed44`) — **arsip; BUKAN sumber** (ADR-A018 kep. 9).

Dasar v16: UKUR v15 (blob **`0768d497812e6e39269ebc74cca75ee0fb89fe25`**, commit
**`d551f4712aa8719de87188ed4a33dd89914a20cb`**), dibaca UTUH pada giliran yang sama
sebelum berkas ini ditulis (aturan 52, pencegahan KC-43).

**Apa yang v16 bawa, disebut di muka:** v15 membawa pembacaan laporan yang menuntaskan
poros lubang tengah. **v16 membawa PEMBACAAN `reports/silang_funding.json` yang mengubah
lubang tak dikenal dari angka menjadi tiga baris bernama** — dan, dalam gerak yang sama,
**mencabut tafsir yang selama tiga versi terdengar paling masuk akal tentang apa lubang
itu.** Ia juga mencatat batas alat secara terbuka: **laporan sumbernya hanya terbaca
54%**.

## KESERASIAN VERSI — PULIH PENUH pada v57 / v16 / v16

- `STATE.md` **v57** — blob **`a542b4b12c556fa0a0180ccdbc09bc3d620d12a1`**, commit
  **`ebe6f373b585bca00ac68c0f8bde9f32c97938ac`**.
- `STATE_LAMPIRAN_EKOR.md` **v16** — blob **`1afefb8f99aeaf5a6529a246cffa354341ee9ec2`**,
  commit **`3241393513750ca823d86e86808c88af9132491e`**.
- `STATE_LAMPIRAN_UKUR.md` **v16** — berkas ini.

Keserasian **PECAH** begitu STATE v57 naik (v57/v15/v15 lalu v57/v16/v15) dan
**dipulihkan oleh berkas ini**. Ketertinggalan yang dicatat STATE v57 dan EKOR v16 —
bahwa berkas ini masih berkepala "milik STATE v56" dan **tidak memuat** ADR-A021,
KC-54, aturan 87 resmi, usulan aturan 88, adjudikasi R-315, pencabutan bacaan
`lubang_tak_dikenal`, `sidik_kode_funding` baru, jurnal 144 dan 145, maupun aturan 38
ke-54..ke-56 — **LUNAS oleh berkas ini**. **Satu berkas per push tetap MENGIKAT**
(KC-42, KC-43).

**Tentang push berkas ini:** ia di akar repo sehingga menyalakan `ci.yml`. Tidak satu
pun `tests/**` berubah, jadi cacah uji tetap **1377** — ramalan **deterministik**,
**MUDAH**, TIDAK masuk papan skor, TIDAK menambah beruntun aturan 57. **Laporannya
WAJIB dibaca sebelum push akar berikutnya** (aturan 38 ke-57), atau ia hangus seperti
run `30547842823`.

**Angka yang TIDAK berubah dari v44/v45/v6/v7** (tidak diulang): taksonomi 9 kelas,
bulan ABSEN 11, H-A013..H-A015, terhenti, SETTLED. Rinciannya di v44 (blob
`d302caff`), v45 (`eb826817`), v6 (`27e59a79`), v7 (`4e7fb65b`).

## KOREKSI KC-41 — BACA SEBELUM MENGUTIP BERKAS INI

Ketiga belas koreksi di bawah **tetap dicantumkan** karena semuanya soal dokumen kami
sendiri, bukan soal data — menghapusnya berarti menghapus jejak cacat.

**Koreksi 1 (v5).** UKUR v5 menulis `lubang_awal.yml` ber-`paths` tiga entri. **SALAH**
— berkas asli (blob `3134bc9f6f91c83ed39ff8424506ac253317edee`) memuat **SATU** entri.
Bila bagian STATE bertentangan dengan berkas sumber, **berkas sumber menang**.

**Koreksi 2 (PROMPT v49).** Poros R-307 disebut "H-A017"; yang benar **H-A018**. LUNAS
di PROMPT v50.

**Koreksi 3 [v9].** Tiga dari empat simbol yang disebut "tampak bulan tengah" ternyata
bulan **PERTAMA**; yang benar-benar melawan H-A019 hanya **TLMUSDT 2023-03**. Kalimat
v8 **DICABUT** (ADR-A016 kep. 4).

**Koreksi 4 [v10, dikoreksi sendiri di v13 oleh KC-52]. BACA UTUH SEBELUM MENGUTIP.**
Rumusan v10–v12 berbunyi: *"Angka 839.842.134 BUKAN jumlah lilin"*, dan menyiratkan
angka itu bermasalah sedangkan 839.325.999 yang benar. **Sirat itu SALAH dan DICABUT.**
Yang terukur:

| angka | arti | himpunan | satuan |
| --- | --- | --- | --- |
| **839.325.999** | Σ baris parquet **lolos gerbang** | **19.586** simbol-bulan | baris parquet |
| **516.135** | Σ baris **12 parquet karantina** | **12** simbol-bulan | baris parquet |
| **839.842.134** | Σ **seluruh** baris parquet rilis | **19.598** simbol-bulan | baris parquet |

**839.325.999 + 516.135 = 839.842.134** ✅ dan **19.586 + 12 = 19.598** ✅

**Ketiganya BENAR, ketiganya satu satuan yang sama, dan tak satu pun keliru.**
**DILARANG** memakai salah satu dari ketiga angka itu **tanpa menyebut penyebutnya**.
Rata-rata 516.135 / 12 = **43.011** turunan yang boleh dikutip, **bukan bukti**;
sebarannya sangat tidak rata (42.585 sampai 131.760).

**Koreksi 5 [v10, LUNAS di EKOR v11].** EKOR v10 menulis `terisi ≉49,7%`; yang benar
**≈49,7%**.

**Koreksi 6 [v11, LUNAS di EKOR v12].** "ramalan deretministik" → "deterministik".

**Koreksi 7 [v12, LUNAS di UKUR v12].** "KESERAIAN VERSI" → "KESERASIAN VERSI".

**Koreksi 8 [v12, LUNAS di UKUR v12].** Penanda tebal tak berpasangan di daftar cacah
berkas uji. Tidak ada angka yang berubah.

**Koreksi 9 [v13] — SALAH NALAR, bukan salah ketik.** Jurnal 138 §5 butir 2 menulis
verbatim: *"Keduanya ditulis dari dua ekspresi berbeda yang kebetulan selalu bertemu —
maka 839.325.999 adalah cacah baris parquet yang sebenarnya, dan **839.842.134 yang
keliru**, bukan sebaliknya."* **Premisnya benar; kesimpulannya tidak sah.** ADR-A019
kep. 2 mengangkatnya menjadi **kelas cacat TANPA PENANGKAL**: dari delapan kesalahan
dokumen yang diperiksa, pembacaan ulang menangkap **satu**.

**Koreksi 10 [v14] — TUDUHAN TERLALU LUAS, diadili dari sumber.** Jurnal 141 §6
menuduh EKOR v13 **dan** ADR-A019 menyajikan larangan R-312 nomor 5 seolah diresmikan
sesudah adjudikasi. Vonis dari sumber: **STATE v54 BEBAS**; **EKOR v13 lalai atribusi,
bukan misrepresentasi**; **ADR-A019 bersalah ringan**.

**Koreksi 11 [v15, DIPERKUAT v16 — kini berinduk pada KC-54] — DUA CACAT DALAM SATU
KEPUTUSAN, dicabut ADR-A020 kep. 8.** ADR-A019 kep. 9 (disalin utuh ke UKUR v14) memuat
dua kekeliruan:

1. Poros identitas dua belas simbol-bulan karantina disebut **"kandidat termurah"**.
   **SALAH.** Kedelapan manifes berjumlah **20.533.802 B** — mustahil dibaca lewat alat
   (batas baca ±30.000 token). Ini **kejadian keempat** taksiran biaya yang keliru, dan
   **yang pertama berarah terlalu murah**.
2. Poros lubang tengah dilabeli **"gugus `2022-05` dan `2024-05`"**. **SALAH.** Keenam
   lubang tengah yang terukur berbulan **2022-01** (BTCSTUSDT) dan **2025-07..2025-11**
   (LITUSDT). Label `2022-05` sebenarnya adalah **`bulan_klines_pertama` BNXUSDT** pada
   tabel H-A010 — satu medan yang berpindah tempat menjadi nama poros.

**[v16] Butir 2 kini dikenali sebagai kejadian PERTAMA dari kelas yang diresmikan
sebagai KC-54** (*nama medan bukan definisi medan*): sebuah medan dibaca dari namanya,
lalu namanya dipakai sebagai kesimpulan tentang isinya. Kejadian keduanya adalah
pencabutan bacaan `lubang_tak_dikenal` di bawah. **Bagaimana perpindahan label itu
terjadi TIDAK diukur, karena itu TIDAK diklaim** (aturan 21).

**Koreksi 12 [v15] — KLAIM KEBARUAN DIPERSEMPIT.** Jurnal 142 §4 mengumumkan
**880 / 877 / 3** sebagai temuan giliran itu. Ketiga angka **sudah tertulis di STATE
v55**. Yang benar-benar baru hanya **letak** selisih 3: seluruhnya di kelas **AWAL**
(48 − 45 = 3; ekor 826 − 826 = 0; tengah 6 − 6 = 0). Rumusan resmi STATE v56: *"Ini
kelas KC-19 dalam bentuk halus: mengumumkan sebagai baru apa yang sudah tertulis di
dokumen sendiri."*

**Koreksi 13 [BARU v16] — TAFSIR `lubang_tak_dikenal` DICABUT (ADR-A021 kep. 2).**
STATE v55, v56, EKOR v15, dan UKUR v15 sama-sama membiarkan berdiri bacaan bahwa
**"lubang di luar penyebut = bulan sebelum simbol lahir"** — yakni bahwa ketiga lubang
tak dikenal pasti mendahului `bulan_klines_pertama`. Pembacaan
`reports/silang_funding.json` **membantahnya dengan angka telanjang**: dari tiga lubang
BNXUSDT, **hanya 2022-04 yang mendahului** `bulan_klines_pertama` 2022-05; **2022-06 dan
2022-08 duduk DI DALAM rentang klines** 2022-05..2026-06. Bacaan itu **DICABUT** dan
**DILARANG dipulihkan tanpa pengukuran baru**. Tidak ada sebab yang diklaim menggantikan
nya (aturan 21).

**Bacaan jujur atas Koreksi 4, 9, 10, 11, 12, dan 13 bersama-sama:** cacat yang bertahan
paling lama di riset ini bukan salah hitung, melainkan **tafsir yang terdengar masuk
akal atas angka yang benar** — dan, sejak v15–v16, **label yang terdengar masuk akal
atas medan yang benar**. Dua kejadian terakhir (Koreksi 11 butir 2 dan Koreksi 13)
satu keluarga, dan keluarga itu kini bernama **KC-54**.

## BATAS KEKUATAN ATURAN 52 — DIPERSEMPIT, BUKAN DICABUT

> Pembacaan ulang **dokumen sendiri** lemah terhadap penalaran cacat: ia membaca
> kalimat yang sudah diyakini benar. Pembacaan **kode** kuat terhadapnya: kode
> menyatakan identitas yang tidak dapat ditawar.

**[v15] Bukti kedua dari sisi kelemahan:** Koreksi 11 dan 12 lolos dari berkali-kali
pembacaan ulang dokumen, dan runtuh hanya ketika **laporan** dibuka.
**[v16] Bukti ketiga, kini paling tajam:** bacaan `lubang_tak_dikenal` bertahan melewati
**empat** berkas akar berturut, dan runtuh dalam **satu** pembacaan laporan. **DILARANG**
menulis bahwa aturan 52 menjaga mutu penalaran **atas dokumen**; yang dijaganya adalah
**kesetiaan salinan**.

## [BARU v16] SILANG FUNDING — TIGA LUBANG TAK DIKENAL, DISEBUT DENGAN NAMA

Sumber: **`reports/silang_funding.json`**, blob
**`b61fe8b3bcabbfce435dd5e5f78fc367f6bef617`**. `waktu_utc` **2026-07-29T08:17:55Z** —
**kejadian keempat aturan 86 (a)**: laporan sudah ada sebelum pertanyaannya dirumuskan.

**BATAS ALAT YANG WAJIB DISEBUT SETIAP KALI LAPORAN INI DIKUTIP.** Alat mengembalikan
verbatim: `This result has been truncated (showing 54% of full).` Bagian tengah larik
**`baris_mati`** TIDAK TERLIHAT. Maka **cacah total `baris_mati` DILARANG diklaim
terukur**; utang ini terdaftar sebagai **utang verifikasi 39** di EKOR v16. Seluruh medan
agregat di bawah terbaca penuh dan sah dikutip.

### Ketiga lubang tak dikenal, LENGKAP

Seluruhnya **BNXUSDT**; tidak ada simbol lain.

| # | simbol | bulan | di dalam rentang klines? |
| --- | --- | --- | --- |
| 1 | **BNXUSDT** | **2022-04** | **TIDAK** — mendahului `bulan_klines_pertama` |
| 2 | **BNXUSDT** | **2022-06** | **YA** |
| 3 | **BNXUSDT** | **2022-08** | **YA** |

Medan pendamping: `bulan_klines_pertama` **2022-05** · `bulan_klines_terakhir`
**2026-06** · `cacah_bulan_klines_simbol` **48**.

**Aritmetika kalender, dihitung TANGAN dan ditandai TURUNAN (aturan 87):** 2022-05
sampai 2026-06 = **50** bulan kalender; `cacah_bulan_klines_simbol` = **48**; selisih
**2**, dan kedua bulan yang hilang **tepat** 2022-06 dan 2022-08. **Sebabnya BELUM
diukur, karena itu TIDAK diklaim** (aturan 21). Inilah poros peringkat pertama sekarang.

### Jembatan penyebut — dua jalur, ditandai TURUNAN

| jalur | susunan | jumlah |
| --- | --- | --- |
| bentuk | 45 awal + 826 ekor + 0 seluruh + 6 tengah | **877** |
| tabel silang | 33 HIDUP + 842 MATI + 2 SEPI + 0 TAK_TERUKUR | **877** |
| terbitan funding | 48 awal + 826 ekor + 6 tengah | **880** |

**877 + 3 = 880** ✅ — ketiga butir tambahan itu **persis** ketiga baris BNXUSDT di atas.
Kedua jalur menuju 877 bertemu; **itu aturan 36, bukan dua pengukuran bebas** — keduanya
lahir dari laporan yang sama.

### Angka terukur yang sah dikutip dari laporan ini

| medan | nilai |
| --- | --- |
| `penyebut_kehidupan` | **19.586** |
| `cacah_baris_dengan_medan` | **19.586** |
| `bulan_klines_funding` | **19.598** |
| `cacah_lubang_funding` | **880** |
| `cacah_lubang_tak_dikenal` | **3** |
| `cacah_mati` | **1.401** (kohort **456** + luar kohort **945**) |
| luar kohort berlubang / berfunding | **386** / **559** |
| `bagian_mati_luar_kohort_dengan_lubang_funding` | **0,4085** |
| `cacah_hidup_tanpa_funding` | **33** |
| `sebaran_bentuk_semua_lubang` | 45 / 826 / 0 / 6 = **877** |
| `bentuk_terbitan_funding` | 48 / 826 / 6 = **880** |
| `tabel_silang` | HIDUP 18.054 / 33 · MATI 559 / 842 · SEPI 96 / 2 · TAK_TERUKUR 0 / 0 |
| semua `selisih_*` | **0** |
| `kendali_sah` · `sidik_seragam` · `laporan_hilang` | **true** · **true** · **[]** |

**Kelima simbol `cacah_hidup_tanpa_funding` 33, LENGKAP, semuanya kelas AWAL:**
BNXUSDT **7** · ICPUSDT **13** · JUPUSDT **1** · QTUMUSDT **1** · TLMUSDT **11**.
7 + 13 + 1 + 1 + 11 = **33** ✅

**Ketertutupan tabel silang, dihitung tangan:** 18.054 + 33 = **18.087** HIDUP ✅ ·
559 + 842 = **1.401** MATI ✅ · 96 + 2 = **98** SEPI ✅ · jumlah **19.586** ✅

Sidik: `sidik_kode` **`8a9b859c09cd64e30e203e6f8dc53411b8e341c44f112805b3041e5d4d3231b1`**
· `sidik_data_funding`
**`2c9fbd1b04f74c9c844bc223a99a103d12220b88d08667b3792720e5b9608d24`** ·
**`sidik_kode_funding`
`d38548236f03314eaa648f64f73be5af2f682207be750a2c2fa413fad581513a`** — **BARU, dicatat
pertama kali di STATE v57 dan disalin ke sini** · `sidik_kode_laporan`
**`24b6bb265525e81c2e571b46e401f36903383f1e3738c487850861adc3e8c595`**.

### Adjudikasi R-315 — FINAL, DILARANG DIADILI ULANG

| butir | ramalan | terukur | vonis |
| --- | --- | --- | --- |
| 1 | ketiga lubang tak dikenal milik **satu** simbol | **1** (BNXUSDT) | **TEPAT** |
| 2 | ketiganya mendahului `bulan_klines_pertama` | **1 dari 3** | **MELESET** |
| 3 (MUDAH) | — | — | **tidak diskor, tidak masuk lajur** |

**Butir 2 DILARANG ditulis ulang sebagai SEPARUH** — 1 dari 3 bukan separuh, dan aturan
84 menuntut satu klausa per butir dinilai utuh. **Syarat gugur (e) MENYALA.**

### KC-54 — diresmikan dari kekalahan ini

> **Nama medan bukan definisi medan.** `lubang_tak_dikenal` menamai hubungan baris itu
> dengan **penyebut**, bukan hubungannya dengan **waktu lahir simbol**. Membaca arah
> waktu dari sebuah nama adalah menebak, bukan mengukur.

**Konsekuensi mengikat:** sebelum sebuah medan dipakai dalam ramalan, **definisinya
wajib disalin dari laporan atau kode lebih dulu**, pada kalimat yang sama dengan
angkanya (bersambung ke KC-53).

## KC-18 — semesta kehidupan (dikonfirmasi ulang oleh R-307..R-315)

Atas **19.586** simbol-bulan lolos gerbang: **1.401 MATI** (7,153%), **98 SEPI**,
**18.087 HIDUP**. Dari 1.401 MATI: 842 kehilangan funding, 559 tetap berfunding.
`cacah_simbol_tanpa_hidup` **18**.

`cacah_lain` = 0 pada kelima modul → seluruh 19.586 berstatus MATI/SEPI/HIDUP.
18.087 + 98 = 18.185 TERUKUR, + 1.401 = 19.586 ✅

**Pembelahan [v9]:** **787** baris bulan PERTAMA (tepat satu per simbol — identitas),
**18.799** bukan-pertama. 787 + 18.799 = **19.586** ✅

**Pembelahan atas kelas MATI [v10]:** 1.392 berlilin PENUH + **9** tidak penuh =
**1.401** ✅

**Pembelahan [v11] — penyebut kerja R-311:** 18.799 − 1.401 = **17.398**. Dari 17.398:
**17.284** penuh + **114** berdefisit ✅ Rincian 114: HIDUP 111, SEPI 3, MATI 0.

**Pembelahan [v13] — lapis di luar penyebut.** Rilis parquet memuat **19.598**:
**19.586 lolos + 12 karantina**. Sebab strukturalnya terukur dari kode:
`kehidupan_arsip.peta_parquet` **melewatkan baris `parquet_karantina`**.

**Pembelahan ketiga atas lubang funding [v15, kini lengkap dengan identitas v16]:**

| kelas bentuk | seluruh semesta | di dalam penyebut | selisih |
| --- | --- | --- | --- |
| awal | **48** | **45** | **3** |
| ekor | **826** | **826** | 0 |
| tengah | **6** | **6** | 0 |
| **jumlah** | **880** | **877** | **3** |

Seluruh selisih 3 duduk di kelas **AWAL**, dan **[v16] ketiganya kini bernama**:
BNXUSDT 2022-04, 2022-06, 2022-08. **Utang ukur 5 UKUR v15 LUNAS.**

## LUBANG TENGAH — POROS TUNTAS OLEH SATU PEMBACAAN [v15, tetap]

Sumber: **`reports/lubang_tengah.json`**, blob
**`39cd1caacedc4d49ba23c91c80f553bb9fb135a6`**, **11.014 B**, dibaca UTUH pada ref
`ae867f2e`. `waktu_utc` **2026-07-29T09:38:52Z**. `versi_lubang_tengah` **2** ·
`versi_funding` **6**.

| medan | nilai |
| --- | --- |
| `penyebut_kehidupan` | **19.586** |
| `cacah_baris_dengan_medan` | **19.586** |
| `cacah_lubang_funding` | **880** |
| `cacah_lubang_tengah` | **6** |
| `selisih_lubang_tengah` | **0** |
| `cacah_lubang_ganda` / `cacah_kunci_ganda` | **0** / **0** |
| `cacah_laporan_dibaca` | **8** (= `total_pecahan` 8) |
| `cacah_per_simbol_funding` | **787** |
| `sebaran_status_lubang_tengah` | HIDUP 0 · MATI **6** · SEPI 0 · TAK_TERUKUR 0 |
| `h_a010_menang` | **true** (5–0) |
| `h_a011_menang` / `h_a011_cacah_bulan` / `h_a011_cacah_hidup` | **true** / **6** / **6** |
| `kendali_sah` · `sidik_seragam` · `laporan_hilang` | true · true · [] |

Sidik `lubang_tengah`:
**`c9372bd763b86cfeb2adcf0a0c0c43dae8d9aa9a6508e9c32f7671d5ec7b3f4e`**.

### Keenam lubang tengah, LENGKAP

| # | simbol | bulan | status | byte_parquet | `cacah_lilin` |
| --- | --- | --- | --- | --- | --- |
| 1 | **BTCSTUSDT** | **2022-01** | MATI | 399.757 | 44.640 |
| 2 | **LITUSDT** | **2025-07** | MATI | 427.922 | 44.640 |
| 3 | **LITUSDT** | **2025-08** | MATI | 427.505 | 44.640 |
| 4 | **LITUSDT** | **2025-09** | MATI | 392.233 | 43.200 |
| 5 | **LITUSDT** | **2025-10** | MATI | 434.201 | 44.640 |
| 6 | **LITUSDT** | **2025-11** | MATI | 389.479 | 43.200 |

- BTCSTUSDT: rentetan **1**, tetangga 2021-12 → 2022-02, `bulan_klines_pertama`
  **2021-03**, `cacah_bulan_klines` **64**, `cacah_lubang` **1**.
- LITUSDT: rentetan **5**, tetangga 2025-06 → 2026-01, `bulan_klines_pertama`
  **2021-02**, `cacah_bulan_klines` **64**, `cacah_lubang` **5**.
- **TIDAK SATU PUN berbulan `2022-05` atau `2024-05`.** Lubangnya di **funding**, bukan
  di klines.

### H-A011 — kebangkitan pertama yang terukur

LITUSDT **2026-01..2026-06**: keenam bulan HIDUP sesudah lima bulan MATI berturut.
**Batas tafsir MENGIKAT (ADR-A020 kep. 1):** DILARANG menggeneralisasi (KC-47 terpicu
kuat: enam bulan berturut bukan enam pengamatan bebas); DILARANG menyebut sebab;
DIIZINKAN: *fenomena kebangkitan ADA, dan terukur sekali.*

### H-A010 — MENANG 5–0

| simbol | rentang lubang awal | `cacah_bulan_klines` | `cacah_lubang` |
| --- | --- | --- | --- |
| BNXUSDT | 2022-05 → 2023-02 | 48 | 19 |
| ICPUSDT | 2021-05 → 2022-09 | 62 | 16 |
| JUPUSDT | 2024-01 → 2024-02 | 30 | 1 |
| QTUMUSDT | 2020-02 → 2020-03 | 77 | 1 |
| TLMUSDT | 2021-07 → 2023-03 | 60 | 20 |

`funding_tanpa_klines`: kelima simbol `ada_medan` **true**, `bulan` **[]**,
`kosong_seluruhnya` **true**. **Aturan 46 kasus ketiga.**

**[v16] CATATAN SILANG YANG WAJIB DITAHAN.** Baris BNXUSDT pada tabel ini —
`cacah_bulan_klines` **48**, rentang lubang awal mulai **2022-05** — adalah **medan yang
sama** yang di UKUR v15 berpindah tempat menjadi nama poros "gugus 2022-05" (Koreksi 11
butir 2), dan **medan yang sama** yang kini menutup jembatan 50 lawan 48 di bagian silang
funding. Satu medan, tiga pemakaian, **dua di antaranya keliru sebelum diukur**. Itulah
KC-54 dalam satu baris tabel.

### Kendali dan sumber

`kendali`: tiga baris **BTCUSDT** (2021-05, 2021-08, 2021-01), semuanya HIDUP dengan
`funding_ada` true → `kendali_sah` true. `sumber`: `reports/funding_semesta.json` +
`reports/kehidupan_arsip_0..7.json`. `medan_per_simbol_funding_terlihat` **10** medan;
`medan_baris_terlihat` **14** medan.

### Konsekuensi pahit: uji H-A020 dan H-A021 MUSTAHIL

> Uji yang direncanakan bagi H-A020 dan H-A021 **MUSTAHIL** — bukan mahal, bukan
> tertunda, melainkan **tidak ada bahannya**.

Keduanya berstatus **DIUSULKAN, BELUM DIUJI, TANPA JALAN UJI YANG DIKETAHUI**.

### Aturan 36 — kasus kedua

`lubang_tengah` **memakai** `silang_funding.bentuk_lubang_lokal` alih-alih menyalin
definisinya. Kasus terkuat tetap yang pertama: `selisih_lilin` dan `pulihkan` bertemu di
**839.325.999** lewat dua jalur, dua modul, dua run, berjarak tiga hari.

## VONIS `ukur_kolom` [v13] — dasar runtuhnya R-312

Dibaca langsung dari `kehidupan_arsip.py` (blob `318a5cb1`):

- **`cacah_lilin` = `n`** = cacah baris parquet, dari `pq.ParquetFile(...).metadata.num_rows`.
- **`cacah_lilin_terbaca`** = cacah baris yang **KEDUA** kolomnya (`volume`, `trades`)
  berhasil terurai.
- **Identitas paksa:** `cacah_lilin` = `cacah_lilin_terbaca` + `cacah_baris_cacat`.

**Kedua medan BUKAN dua pengukuran bebas.** Turunan cuma-cuma: `cacah_berselisih` = 0
pada 19.586 dari 19.586 memaksa **`cacah_baris_cacat` = 0 di seluruh semesta**.

## ARAH SELISIH R-312 MUSTAHIL — vonis diperberat [v14, tetap]

Docstring `selisih_lilin.py` mendefinisikan `selisih = cacah_lilin_terbaca − cacah_lilin`
dan menyatakan arah itu dipilih supaya selisih **POSITIF**. Identitas `ukur_kolom`
memaksa `cacah_lilin_terbaca` ≤ `cacah_lilin` **pada setiap baris**. Maka **butir 2
R-312 tidak dapat dimenangkan secara struktural**. Kalimat "sesuai dua angka di atas"
adalah **KC-52 yang ditulis ulang ke dalam kode**.

## SISA DEFISIT [v11, tetap berlaku]

Sumber: `sisa_defisit.py` V1 run **30542217951** (commit `b1c7941d`, kode 0), ringkas
blob **`91a05c0528050d0d37e4cf7711b6556f13fc8d16`**.

| besaran | nilai |
| --- | --- |
| `cacah_calon` (bukan-pertama, bukan-MATI) | **17.398** |
| `cacah_calon_penuh` | **17.284** |
| **`cacah_berdefisit`** | **114** (0,66%) |
| `defisit_calon` | **712.925** |
| rata-rata defisit per baris berdefisit | **6.254** |
| `defisit_teratas` (sepuluh baris) | **291.379** |
| **`bagian_teratas`** | **0,4087** |
| `defisit_terbesar` (satu baris) | **42.510** |
| `selisih_sisa` | **0** |
| kelas 114 | HIDUP **111** · SEPI **3** · MATI **0** |

- **Baris terbesar: TLMUSDT `2023-03`, HIDUP, 2.130 dari 44.640 lilin — 95,2% KOSONG.**
- **Sepuluh teratas tersebar di TUJUH bulan** → **aturan 81 TIDAK terpicu**.
- **ANCUSDT `2022-05` defisit 26.959** lawan **LUNAUSDT `2022-05` defisit 26.950** —
  selisih **sembilan lilin**; dasar **H-A021**; **kebetulan angka, bukan bukti**.
  Tidak ada lubang tengah di `2022-05` → jalan uji tertutup.
- **712.925 DILARANG DISEBUT PENGUKURAN BEBAS** — tautologi dari 808.162 − 95.237.
- Kendali: `JAWABAN_KENDALI` **17 medan**, `bagian_teratas` **0,9677** = 600/620
  dihitung TANGAN lebih dulu dan cocok.

**Adjudikasi R-311: SEPARUH.** Dasar **KC-51**.

**Sidik `sisa_defisit` V1 =**
`6211624ba9514d604d4dc510abca2e40386775c7aaa1279135f0baf666f044b0`

## KETERISIAN LILIN [v10, tetap berlaku]

Sumber: `keterisian_lilin.py` V1 run **30535202643** (commit `924b0d7a`, kode 0),
laporan blob `14f17720`, ringkas blob `f33714ed`.

| besaran | nilai |
| --- | --- |
| `cacah_mati_penuh` / `cacah_mati_tak_penuh` | **1.392** / **9** |
| `jumlah_lilin_langsung` (19.586 baris) | **839.325.999** |
| `defisit_total` | **18.143.601** |
| `defisit_pertama` | **17.335.439** (95,5%) |
| `defisit_bukan_pertama` | **808.162** (bagian **0,0445**) |
| `cacah_baris_tanpa_lilin` / negatif / kunci ganda | **0** / **0** / **0** |
| `cacah_laporan_dibaca` | **8** dari 8 · `sidik_seragam` **true** |

- **BULAN MATI PENUH DATANYA; YANG NOL ADALAH TRANSAKSINYA** — 1.392 dari 1.401 (99,4%).
- **DILARANG melanjutkan ke "harga beku" atau "lilin datar".** `medan_baris_terlihat`
  berisi **14** medan dan **tak satu pun harga**.
- Defisit menumpuk di bulan pertama: rata **22.027** lilin hilang, keterisian
  **≈49,7%**, bersesuaian dengan nisbah byte 0,527179 dari R-309.
- **Kesembilan baris MATI tak penuh, LENGKAP** (semuanya `pertama: false`):

| # | simbol | bulan | `cacah_lilin` | penuh | defisit |
| --- | --- | --- | --- | --- | --- |
| 1 | LENDUSDT | 2020-11 | 13.475 | 43.200 | 29.725 |
| 2 | FRONTUSDT | 2024-09 | 14.986 | 43.200 | 28.214 |
| 3 | FOOTBALLUSDT | 2024-05 | 39.308 | 44.640 | 5.332 |
| 4 | ANTUSDT | 2024-05 | 39.309 | 44.640 | 5.331 |
| 5 | BTSUSDT | 2024-05 | 39.310 | 44.640 | 5.330 |
| 6 | SRMUSDT | 2024-05 | 39.311 | 44.640 | 5.329 |
| 7 | HNTUSDT | 2024-05 | 39.312 | 44.640 | 5.328 |
| 8 | TOMOUSDT | 2024-05 | 39.315 | 44.640 | 5.325 |
| 9 | COCOSUSDT | 2024-05 | 39.317 | 44.640 | 5.323 |

  Jumlah defisit kesembilan **95.237** = **0,1178** dari 808.162.
  808.162 − 95.237 = **712.925**.
- **TUJUH dari sembilan berbulan `2024-05`, jendela hanya SEMBILAN lilin** → KC-47,
  aturan 81, **H-A020**. **Kalimat "tujuh simbol didelisting 28 Mei 2024" DILARANG
  ditulis sebagai temuan.** Tidak ada lubang tengah di `2024-05` → jalan uji tertutup.
- **Larangan ADR-A015 kep. 5 TIDAK dibalik** oleh R-310..R-315 maupun A018..A021.
- **Adjudikasi R-310: TEPAT** — kedua kemenangan **tipis ke tepi BAWAH**, gejala KC-51.

**Sidik `keterisian_lilin` V1 =**
`1cd98f4fa22c24b30f31f5b36dac0ea0bb3fa9de44e5e15ae73cbf11cdca08bb`

## IRISAN BULAN PERTAMA [v9, tetap berlaku]

Sumber: `bulan_pertama.py` V1 run **30532058657** (commit `09ce9853`, kode 0), laporan
blob `0a2aa6ae`. Definisi "bulan pertama": bulan TERKECIL milik simbol itu **di dalam
penyebut 19.586** — bukan bulan pertama simbol itu di bursa. Perbedaan keduanya BELUM
diukur (ADR-A016 kep. 6).

| besaran | nilai |
| --- | --- |
| `cacah_hidup_kecil_sebagian` (dari 38) | **37** (0,973684) |
| `cacah_pertama` / `cacah_bukan_pertama` | **787** / **18.799** |
| `rata_byte_pertama` / `rata_byte_bukan_pertama` | **897.374,517** / **1.702.219,726** |
| `nisbah_rata` | **0,527179** |

- **Irisan NYATA tetapi ASIMETRIS TAJAM:** 37 dari 38 berkas kecil adalah bulan pertama
  (**97,4%**); hanya 37 dari 787 bulan pertama yang berkas kecil (**±4,7%**). Rumusan
  resmi satu-satunya di **ADR-A016 kep. 1**.
- Klausa tepi `2026-06` menyumbang NOL secara bebas — DICABUT (ADR-A016 kep. 2),
  melahirkan aturan 84.
- **Satu lawan tersisa: TLMUSDT 2023-03 (80.394 byte)**; tafsir pengganti **TIDAK
  ditegakkan** (ADR-A018 kep. 6).

**`daftar_kecil_bertanda` (38, LENGKAP, urut byte menaik):** JUPUSDT 2024-01 22.440 ·
TIAUSDT 2023-10 24.551 · REZUSDT 2024-04 32.164 · SLPUSDT 2023-10 33.257 · PORTALUSDT
2024-02 34.175 · NAORISUSDT 2025-07 34.673 · TROYUSDT 2024-10 35.511 · MDTUSDT 2023-06
36.580 · COSUSDT 2024-09 36.742 · GUNUSDT 2025-03 36.768 · CCUSDT 2025-10 37.116 ·
MAGMAUSDT 2025-12 37.327 · COLLECTUSDT 2025-12 38.486 · CKBUSDT 2023-02 39.079 ·
EDUUSDT 2023-04 39.749 · AIOTUSDT 2025-04 41.514 · PUNDIXUSDT 2025-04 42.561 · ADAUSDT
2020-01 42.678 · VFYUSDT 2025-09 44.460 · PLAYUSDT 2025-07 44.508 · COMPUSDT 2020-06
44.898 · MLNUSDT 2025-03 45.246 · EDENUSDT 2025-09 45.883 · RLCUSDT 2020-07 46.447 ·
FUNUSDT 2025-03 47.831 · MTLUSDT 2021-03 51.322 · YFIUSDT 2020-08 54.929 · ATAUSDT
2021-08 58.161 · ENSUSDT 2021-11 62.845 · ROSEUSDT 2021-12 63.592 · **SQQQUSDT 2026-06
72.819 (tepi)** · **TLMUSDT 2023-03 80.394 (pertama:false, tepi:false, sebagian:false)**
· AMBUSDT 2023-03 81.419 · **TQQQUSDT 2026-06 82.330 (tepi)** · **MVLLUSDT 2026-06
86.126 (tepi)** · LEVERUSDT 2023-03 89.724 · INXUSDT 2026-01 94.575 · ENJUSDT 2020-09
94.658.

**Sidik `bulan_pertama` V1 =**
`0d3530f69ad51a22e038c17616411b56e4518698ff14c9b635131ec1e2a66562`

## LEBAR ZONA IRISAN BYTE [v8, tetap berlaku]

Sumber: `irisan_byte.py` V1 run **30529294165** (commit `d22364b9`, kode 0), laporan
blob `4c13bf6a`.

| besaran | nilai |
| --- | --- |
| `cacah_hidup_byte_kecil` (< **97.634**, STRIKT) | **38** (0,0021009564880853653) |
| `cacah_mati_byte_kecil` (< **150.000**, STRIKT) | **2** (0,0014275517487508922) |

- **Zona 22.440–97.634 byte berisi 38 baris HIDUP dan NOL baris MATI.**
- **Sebaran per kelas IDENTIK dari TIGA modul berbeda** (aturan 36):

| kelas | cacah | byte | byte_min | byte_maks | byte_rata |
| --- | --- | --- | --- | --- | --- |
| HIDUP | 18.087 | 32.049.492.952 | **22.440** | 2.770.666 | 1.771.962,899 |
| SEPI | 98 | 77.728.024 | 259.327 | 1.231.408 | 793.143,102 |
| MATI | 1.401 | 579.041.399 | **97.634** | 451.875 | 413.305,781 |

  `cacah_lain` 0 · `byte_lain` 0 · `total_byte` **32.706.262.375**.
- **Sembilan medan selisih semuanya 0 — tetapi hanya DELAPAN bebas** (`total_byte`
  turunan). Menyebut "sembilan pemeriksaan bebas" **DILARANG** (KC-50).

**Sidik `irisan_byte` V1 =**
`0e7103ef46a37d1e442d8e7fc5b9771b1ef7cdc3956ea57d584d84f6f73ea2c6`

## BYTE PARQUET ATAS SELURUH SEMESTA [v7, tetap]

`byte_semesta.py` V1 run **30526358811** (commit `d3bc2039`, kode 0), laporan blob
`8b7f2077`. **Total byte parquet = 32.706.262.375** atas 19.586 simbol-bulan.
`bagian_byte_mati` **0,017704297493883234**; `cacah_terukur_byte_kecil` (< 10.000) 0;
`cacah_byte_nol` 0 → **dasar keras ≈22 KB**, sebab langsung KC-48. Adjudikasi R-307:
**MELESET**. Sidik `e02aca2b3967069b500b01d27a1d2d1553f47b912ea41ddbecd9e4e6c33883c7`

## Arah waktu kematian lawan lubang funding [v6, tetap]

`lubang_tebing` V1 run **30524631435** (commit `84b11164`, kode 0), laporan blob
`7d8883f5`. Penyebut **118**.

| kelas arah (STRIKT, aturan 80) | cacah | bagian |
| --- | --- | --- |
| `mati_dulu` | **40** | **0,339** |
| `serempak` (DILARANG di numerator) | **78** | 0,661 |
| `lubang_dulu` | **0** | 0,000 |

`cacah_tebing_butir_2` **39** (`2025-07`); **39 dari 40** `mati_dulu` ada di tebing
(0,975); satu-satunya bukan-tebing **BTCSTUSDT** → KC-47, aturan 81. Adjudikasi R-306:
TEPAT 3/3.
**Catatan yang WAJIB ditahan:** BTCSTUSDT muncul lagi sebagai satu-satunya lubang tengah
di luar LITUSDT, dan LITUSDT berlubang mulai **`2025-07`** — bulan tebing itu juga.
**Keserian itu BELUM diukur dan DILARANG diklaim** (aturan 21); ia poros nomor 3.
Sidik `4a5c2e4279eb1554dc119b48d6a8db61f6ea4ee11b7539efd70ee71d1ae18bf3`

## Lubang funding — agregat semesta (tetap)

- `cacah_simbol_ada_lubang` **122** dari 787 · awal **5** · bukan-awal **118**.
- BNXUSDT punya lubang AWAL dan bukan-awal sekaligus.
- Lima bentuk AWAL: BNXUSDT, ICPUSDT, JUPUSDT, QTUMUSDT, TLMUSDT. ICP dan TLM lubang
  awalnya melewati kematian (sumber salah-baca R-304, KC-46).
- Lubang funding **880** semesta / **877** dalam penyebut / **3** tak dikenal;
  ketiganya di kelas AWAL, **[v16] ketiganya BNXUSDT dan bernama**.
- Dari 945 MATI di luar kohort: **386** kehilangan funding, **559** berfunding;
  `bagian_mati_luar_kohort_dengan_lubang_funding` **0,4085**.

## Jumlah uji — terukur

**1377, kini DUA BELAS bacaan berjejak di berkas ini.**

1. blob **`cdfdee2559201306a49bc9b01f1185d7aa36eebe`**, run **30559145901**, commit
   **`c1dc0009`**, 15:57:01Z, kode 0, `1377 tests collected in 0.58s`.
2. blob **`effb3a46bc20cda5c6c5910ee926aa16c195bb68`**, run **30575123865**, commit
   **`8368ca1f`**, 19:30:52Z, kode 0, `… in 0.54s`.
3. blob **`8cbbd4ce7b85d9e1f217a9cefbdacfb9318dec78`**, run **30576963781**, commit
   **`6642ed68`**, 19:56:30Z, kode 0, `… in 0.67s`.
4. blob **`8ec97de5af8b528276174f635e3bda9e6cc2d7ef`**, run **30577779309**, commit
   **`2bdd8233`**, 20:07:50Z, kode 0, `… in 0.62s`.
5. blob **`94d270e7065218f87bd5a26c5113ed8346cf6abf`**, run **30579348728**, commit
   **`cd209f3e`**, 20:29:25Z, kode 0, `… in 0.61s`.
6. blob **`04bfa2ed5fb43f128f8ee2351f41722314685a03`**, run **30580133552**, commit
   **`a722ec63`**, 20:40:02Z, kode 0, `… in 0.46s`.
7. blob **`aeb4315ad73806b61f734f9c1d92b27b1ae2727b`**, run **30581703827**, commit
   **`6157586e`** (UKUR v14), 21:02:01Z, kode 0, `… in 0.61s`.
8. blob **`19785af1d96fdc1fabec2dfa9f7c3dbaf60b3708`**, run **30583686515**, commit
   **`019d16ea`** (STATE v56), 21:31:10Z, kode 0, `… in 0.61s`.
9. blob **`5f4282f6d8f21cae7c2f6786ea29072ab4175973`**, run **30584737431**, commit
   **`94c7d9da`** (EKOR v15), 21:47:25Z, kode 0, `… in 0.60s`.
10. **[v16]** blob **`340c3c7f425d49859e6ae659cca38d0ee7770aaa`**, run **30585269231**,
    commit **`d551f471`** (UKUR v15), 21:55:58Z, kode 0, `… in 0.60s`.
11. **[v16]** blob **`8ea8cc463ff58246b363e47458e9355d26a5ea79`**, run **30587658376**,
    commit **`ebe6f373`** (STATE v57), 22:36:15Z, kode 0, **`… in 0.40s`** — tercepat
    yang pernah tercatat.
12. **[v16]** blob **`34f88b3744e4d9733a731f3f97056584344ddc33`**, run **30588460935**,
    commit **`3241393513750ca823d86e86808c88af9132491e`** (EKOR v16), **22:49:39Z**,
    kode 0, `… in 0.61s`.

Turunan: 1341 + **36** butir `tests/test_selisih_lilin.py` = **1377** ✅ (aturan 21),
terverifikasi dari sumber. **Rentang waktu kutip 0,40s–0,67s DILARANG dibaca sebagai
pengukuran apa pun tentang repo** — ia keadaan mesin CI, bukan besaran riset.

Riwayat: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 → 984 →
1044 → 1100 → 1168 → 1233 → 1297 → 1341 (enam run) → **1377** (dua belas run berjejak).

**Aturan 57: beruntun 4 dari 4** sesudah PUTUS di 26/27. Tidak bertambah sejak trio.
Ia **mencacah, bukan menaksir**.

### Aturan 38 — ordinal, kini sampai ke-56

Definisi yang berlaku (ADR-A018 kep. 8): pemakaian dihitung **hanya** untuk pembacaan
`reports/ci_terakhir.json` yang meninggalkan **jejak tertulis** berupa nomor run,
commit, dan blob.

| ke- | CI | run | commit | blob | jejak |
| --- | --- | --- | --- | --- | --- |
| 49 | 1377 | 30579348728 | `cd209f3e` | `94d270e7` | EKOR v14, STATE v56 |
| 50 | 1377 | 30580133552 | `a722ec63` | `04bfa2ed` | UKUR v14, STATE v56 |
| 51 | 1377 | 30581703827 | `6157586e` | `aeb4315a` | jurnal 142, STATE v56 |
| 52 | 1377 | 30583686515 | `019d16ea` | `19785af1` | EKOR v15 |
| 53 | 1377 | 30584737431 | `94c7d9da` | `5f4282f6` | UKUR v15 |
| 54 | 1377 | 30585269231 | `d551f471` | `340c3c7f425d49859e6ae659cca38d0ee7770aaa` | jurnal 144, STATE v57 |
| 55 | 1377 | 30587658376 | `ebe6f373` | `8ea8cc463ff58246b363e47458e9355d26a5ea79` | EKOR v16 |
| **56** | **1377** | **30588460935** | **`3241393513750ca823d86e86808c88af9132491e`** | **`34f88b3744e4d9733a731f3f97056584344ddc33`** | **berkas ini** |

**Pemakaian berjalan = ke-lima puluh enam.** Pemakaian ke-56 dibaca
**2026-07-30T22:49:39Z**, kode keluar **0**, atas push EKOR v16 — **dibaca sebelum
tertimpa** dan **sebelum push berkas ini**, sehingga tidak hangus.

**[v16] LIMA BELAS pembacaan berturut (ke-42..ke-56) tanpa satu pun laporan hangus.**

**Bot CI:** setiap push yang menyalakan `ci.yml` diikuti **satu** commit bot di atasnya —
deterministik, **DILARANG dihitung kemenangan**. Commit bot yang terlihat pada giliran
ini: **`ff89f688c5f8090c679a0cae73d4e71ea80cf939`** (atas STATE v57) dan
**`47769b1805d19ae53a2b5c91d9bc72dd88e7e68d`** (atas EKOR v16).

**Dua cacat tetap disebut, tidak dihaluskan:** baris ke-**38** (run `30541051907`,
commit `5d7d8b96`) **tanpa blob**, tidak dapat dipulihkan — ordinal ini sah **relatif
terhadap definisi di atas**, bukan sebagai pencacahan mutlak; dan run **30547842823**
(bot `de2fc03d`) **tidak pernah dibaca**, sudah tertimpa, **DILARANG dihitung**,
ramalannya **DILARANG diklaim menang**.

**Calon aturan** — dua berkas akar berturut tanpa membaca laporan di antaranya pasti
menghanguskan yang pertama — **tetap DITOLAK diresmikan** (ADR-A019 kep. 3): masih
**satu** kejadian terukur.

## Modul, workflow, dan berkas uji

**CACAH TANGAN yang sah** (aturan 66), pada ref **`3196fd98`** dan dikonfirmasi ulang
pada ref **`8a614567`**:

| direktori | cacah TANGAN |
| --- | --- |
| `lux_ai/serapan/` (berkas `.py`) | **49** |
| `tests/` | **53** |
| `.github/workflows/` | **44** |
| akar repo | **18** entri (6 direktori + 12 berkas) |

**UTANG ATURAN 66 HIDUP.** **50 / 54 / 45** adalah **TURUNAN dan DILARANG dikutip
sebagai terukur** sampai dicacah satu per satu bernomor (KC-33, ADR-A019 kep. 8).

**PERINGATAN DUA CACAH `tests/` (ADR-A018 kep. 10).** `PETA_MODUL_BERKAS.md`
(`3abe95f6`) mencatat **34** berkas uji milik repo **WARISAN `bot_v8`**; repo riset ini
punya **53**. **Menyebut "cacah uji" tanpa menyebut repo-nya DILARANG.**

**Peringatan dini aturan 48:** tiga modul terbesar `lux_ai/serapan/` menurut byte —
`silang_funding.py` **29.873** (**705 baris**, pagar 800 → sisa **95**) · `funding.py`
**28.121** · `sisa_defisit.py` **25.949**. **`lubang_tengah.py` V2 23.745 B.**

**BLOB TRIO R-312 — DIBACA UTUH, aturan 52 LUNAS PENUH:**

| berkas | blob |
| --- | --- |
| `.github/workflows/selisih_lilin.yml` | **`de2fd4fd346c9e13213fcc9a410d4aea8460d67a`** |
| `tests/test_selisih_lilin.py` (**36** butir) | **`2d903a4a6f544eacd26b82bdb177680fa78bdffd`** |
| `lux_ai/serapan/selisih_lilin.py` | **`d19bdb5fe67e0bd9c1b141d7fb7cc6dcd089c5f2`** |

Blob trio R-311 tetap: `sisa_defisit.py` **`7aa0e6d7003902e50806570ad112aae7f0345b07`**
· `test_sisa_defisit.py` **`7004115acffd9c03c9ba4f9873bef40cb6b1375f`** (**44** butir) ·
`sisa_defisit.yml` **`645112075e104a74d43f3e3d2185cfbd48b0b513`**.
Blob trio R-310: `keterisian_lilin.py` `3f80ffa7` · `test_keterisian_lilin.py`
`f58912d0` (64) · `keterisian_lilin.yml` `d821c63a`. Trio v9: `bulan_pertama.py`
`b9bd00ac` · `test_bulan_pertama.py` `75d87ba2` (65) · `bulan_pertama.yml` `2242e3e4`.
Lainnya identik: `irisan_byte.py` `2dbe3d55`, `test_irisan_byte.py` `b6389051` (68),
`irisan_byte.yml` `7d98a267`, `kehidupan.py` `f49abb2b`, **`kehidupan_arsip.py`
`318a5cb187406d16cfd3385d653bed905f632934` (19.281 B, DIBACA UTUH)**, **`pulihkan.py`
`a9e6eab7cc47555dfed919ac63044ff2eadc4893` (14.839 B, DIBACA UTUH)**,
**`silang_funding.py` V2 `42c3aa9dc2c16220b79cf9c9e46979dd000fd393` (29.873 B, DIBACA
UTUH)**, **`ukur_baris.py` V5 `3ebaa9f9` (17.442 B, DIBACA UTUH)**, **`lubang_tengah.py`
V2 `4d3beaf18c070d2931044c50dd5a354d75eaceb8` (23.745 B, DIBACA UTUH)**,
`kohort_ekor.py` `c9b63bbe`, `lubang_awal.py` `8c36943d`, `lubang_tebing.py` `575e777e`,
`sebab_bangkit.py` `fd5a1dc4`, `tersisip_semesta.py` `8a648838`, `bentangan_kohort.py`
V2 `f4eae57a`, `byte_semesta.py` `ff68e4be`, `funding.py` `8d4b1f82`, `rilis.py`
`2e44530c`, `karantina_semesta.py` `46e7c46b`, `arsip.py` `0104958b`, **`gerbang_1m.py`
`c8cc54c8` (BELUM DIBACA UTUH — poros berikutnya)**, `resample.py` `66a4b177`,
`semesta_kuota.py` `7288b030`, `bulan_absen.py` `10279d72`, `kebangkitan.py` `446321ee`,
`penyebut_tahun.py` `265aad00`, `anatomi_tengah.py` `04279335`, `__init__.py`
`64d85584`. `ci.yml` = **`c79497b2c812679eaa69aee5b3160eac9f5c5fb7`** (paths-ignore
`journal/**`, `decisions/**`, `hipotesis/**`, `reports/**`; push ke `lux_ai/**`,
`tests/**`, `STATE*`, `PROMPT*` MENYALAKAN CI — **terkonfirmasi delapan kali berturut**).
`karantina_semesta.yml` = `de40fa4e` (**belum dibaca utuh**).

Cacah per berkas uji — **milik repo riset ini, bukan repo warisan**:
`test_irisan_byte.py` **68** · `test_bulan_pertama.py` **65** ·
`test_keterisian_lilin.py` **64** · `test_bentangan_kohort.py` V2 **63** (blob
`9f850ecdb25466d38c839004b36ff221db2cf7f8`, dicacah TANGAN) · `test_lubang_tebing.py`
**60** · `test_sebab_bangkit.py` **57** · `test_byte_semesta.py` **56** ·
`test_lubang_awal.py` **48** · `test_tersisip_semesta.py` **47** ·
`test_anatomi_tengah.py` **47** · `test_sisa_defisit.py` **44** ·
**`test_selisih_lilin.py` 36** · `test_terhenti.py` V4 **33** · `test_bulan_absen.py`
**32** · `test_karantina_semesta.py` **28** · `test_silang_settled.py` **24** ·
**`test_ukur_baris.py` 3**.
**`tests/test_lubang_tengah.py` — 56 butir menurut praregistrasi R-228, BELUM DIBACA.
DILARANG dikutip sebagai cacah terukur; R-228 belum diadjudikasi.**

**POLA WORKFLOW TRIO — TERVERIFIKASI DARI SUMBER** (`selisih_lilin.yml`, blob
`de2fd4fd…`): `name`, `on.push.paths` **SATU** entri, `permissions: contents: write`,
job `ukur` di `ubuntu-latest`, checkout@v4 + setup-python@v5 (3.11),
`pip install numpy pandas pyarrow pyyaml`, langkah `jalan` id=`jalan` dengan `set +e` →
`KODE=$?` → `echo "kode=$KODE" >> "$GITHUB_OUTPUT"` → `exit 0`, langkah `catat status`,
langkah `dorong laporan` (`[skip ci]`, `git pull --rebase`), penutup
`exit ${{ steps.jalan.outputs.kode }}`. **Aturan 55 LUNAS untuk berkas ini.**

## API terverifikasi

API lama (v37–v12) tetap berlaku. Tambahan v13–v15 **seluruhnya dibaca UTUH dari kode**
(KC-43). v16 **tidak menambah pembacaan kode baru** — ia menambah pembacaan **laporan**.

**`lubang_tengah` V2** (blob **`4d3beaf18c070d2931044c50dd5a354d75eaceb8`**, 23.745 B,
DIBACA UTUH). Tetapan: `VERSI=2` · `KELUARAN="reports/lubang_tengah.json"` ·
`TENGAH_TERCATAT=6` · `SIMBOL_H_A010=["BNXUSDT","ICPUSDT","JUPUSDT","QTUMUSDT","TLMUSDT"]`
· `SIMBOL_TENGAH_TERCATAT=["BTCSTUSDT","LITUSDT"]` · `SIMBOL_H_A011="LITUSDT"` ·
`RENTANG_H_A011=("2026-01","2026-06")` ·
`BERKAS_DICAP=["kehidupan.py","kehidupan_arsip.py","lubang_tengah.py","silang_funding.py"]`.
**Enam belas fungsi**; **lima penggugur** dikunci di muka; **enam praregistrasi di
docstring** (R-221, R-222, R-223 TEPAT; **R-229 TEPAT**, **R-230 MELESET**; R-228 belum
diadjudikasi). **Aturan 36 ditegakkan di dalam kode**; **aturan 46 ditegakkan di dalam
kode**. Angka docstring (**TURUNAN**): `funding.py` V6 mencacah **87** "funding tanpa
klines" atas **787** simbol; `silang_funding.py` V2 = **705 baris**.

**`pulihkan` V2** (blob `a9e6eab7cc47555dfed919ac63044ff2eadc4893`, 14.839 B).
Tetapan: `VERSI=2`, `TOTAL_PECAHAN=8`, `AKAR_UNDUH="data/unduh"`,
`AKAR_PULIH="data/pulih"`. Fungsi: `nama_manifes(i)` · `nama_status_serapan(i)` ·
`nama_keluaran(i)="reports/pulihkan_pecahan_<i>.json"` · `nama_tag(i,run_id)` ·
`sidik_kode()` mencap `["pulihkan.py","rilis.py"]` · `run_id_sumber` ·
`putuskan_definisi(...)` → `(kesimpulan, dapat_dibedakan)` · `anggota_aman` ·
**`cacah_baris_parquet(jalur)` = `pq.ParquetFile(...).metadata.num_rows`** ·
`periksa_bagian` · **`periksa_keluarga`** dipanggil **dua kali**, atas `manifes["rilis"]`
dan **`manifes["rilis_karantina"]`** · `_utuh` · `jalankan` · `main` (env
`PULIH_INDEKS`). Praregistrasi historis **R-198**.

**`kehidupan_arsip` V1** (blob `318a5cb187406d16cfd3385d653bed905f632934`, 19.281 B).
Tetapan: `VERSI=1`, `TOTAL_PECAHAN=8`, `AKAR_BONGKAR="data/kehidupan_arsip"`,
`KENDALI_CACAH=3`, `KOLOM_VOLUME="volume"`, `KOLOM_TRANSAKSI="trades"`,
`BERKAS_DICAP` 5 nama, `nama_keluaran(i)="reports/kehidupan_arsip_<i>.json"`.
Fungsi: `peta_parquet` (**melewatkan baris `parquet_karantina`**), `_angka`,
**`ukur_kolom`**, `ukur_parquet`, `baris_kehidupan`, `kendali_pecahan`, `ringkas_pecahan`,
`kode_keluar`, `_cocokkan`, `periksa_bagian`, `jalankan`, `berkas_ringkas`, `main`.

**`selisih_lilin` V1** (blob `d19bdb5fe67e0bd9c1b141d7fb7cc6dcd089c5f2`). Tetapan:
`VERSI=1` · `KELUARAN` + `KELUARAN_RINGKAS` · `BATAS_BARIS_LAPORAN=40` ·
`MEDAN_KLAIM="cacah_lilin"` · `MEDAN_TERBACA="cacah_lilin_terbaca"` · `CACAH_TERATAS=10`
· `LILIN_LANGSUNG_TERCATAT=839325999` · `BARIS_PARQUET_TERCATAT=839842134` ·
`SELISIH_TERCATAT=516135` · `AMBANG_HIDUP_KECIL=97634` · `INVARIAN` **8** kunci ·
`R312_PITA_BUTIR_1=(12,120)` · `R312_PITA_BUTIR_2=(0.50,0.865)` · `BERKAS_DICAP` **4**
nama. **Empat kendali lolos**; `kendali_deteksi` **11 medan**; `kendali_teratas`
**0,9615** = 7.500/7.800. `kode_keluar` mengembalikan **2** bila `cacah_berselisih <= 0`
— **dirancang**. Laporan ringkas blob **`e5cc64011030cfb8e1a8edf3699dd01b3caafab7`**:
`cacah_baris` **19586** · `cacah_berselisih` **0** · kedua jumlah **839325999** ·
`dua_jalur_bertemu` **true** · `uji_r312.teradjudikasi` **false**.

**`ukur_baris` V5** (blob `3ebaa9f9`, 17.442 B): `PAGAR_BARIS=800`, `BERKAS_DIUKUR`
**21 nama**, uji `test_ukur_baris.py` (`7975bf88`) **3** fungsi. **Utang V6 hidup.**

**`silang_funding` V2** (blob `42c3aa9d`, DIBACA UTUH): `baca_laporan_kehidupan(akar,
total)` → **TIGA** nilai, kunci tuple `(simbol, bulan)`; `baca_medan_baris(akar, total,
medan)` → `(nilai, meta)`. Tetapan: `PENYEBUT_TERCATAT=19586`, `MATI_TERCATAT=1401`,
`KOHORT_TERCATAT=456`, `HIDUP_TANPA_FUNDING_TERCATAT=33`,
**`LUBANG_TAK_DIKENAL_TERCATAT=3`**, `BENTUK_TERBITAN_FUNDING={"awal":48,"ekor":826,
"tengah":6}`, `MEDAN_LILIN="cacah_lilin"`, `SUMBER_FUNDING="reports/funding_semesta.json"`,
`KENDALI_CACAH=3`.
**[v16] PERINGATAN KC-54 atas tetapan ini:** `LUBANG_TAK_DIKENAL_TERCATAT=3` memuat
**cacah**, bukan **identitas** dan bukan **arah waktu**. Kode tidak pernah menjanjikan
bahwa ketiganya mendahului kelahiran simbol; **dokumenlah yang menambahkannya**.

**`keterisian_lilin` V1** (blob `3f80ffa7`): `INVARIAN` =
`{penyebut:19586, cacah_simbol:787, cacah_hidup:18087, cacah_sepi:98, cacah_mati:1401,
total_byte:32706262375, byte_hidup:32049492952, cacah_hidup_byte_kecil:38}` ·
`AMBANG_HIDUP_KECIL=97634` · `MENIT_PER_HARI=1440` · `KENDALI_SIMBOL="BTCUSDT"` ·
`R310_PITA_BUTIR_1=(1,120)` · `R310_PITA_BUTIR_2=(0.02,0.25)`.

**`sisa_defisit` V1** (blob `7aa0e6d7`): `R311_PITA_BUTIR_1=(200,12000)`,
`R311_PITA_BUTIR_2=(0.02,0.45)`, `DEFISIT_SEMBILAN_TERCATAT=95237`,
`DEFISIT_BUKAN_PERTAMA_TERCATAT=808162`, `SISA_TERCATAT=712925`, `INVARIAN` delapan
kunci BEBAS, `JAWABAN_KENDALI` **17 medan**, `teratas` mengembalikan **None** bila baris
berdefisit < 10.

**`bulan_pertama` V1** (`b9bd00ac`): `R309_PITA_BUTIR_1=(22,38)`,
`R309_PITA_BUTIR_2=(0.10,0.60)`, `BULAN_TEPI="2026-06"`.
**`irisan_byte` V1** (`2dbe3d55`): `AMBANG_HIDUP_KECIL=97634`,
`AMBANG_MATI_KECIL=150000`, `MEDAN_SELISIH` **9** (delapan bebas + satu turunan).
**`bentangan_kohort` V2** (`f4eae57a`, uji `9f850ecd`): butir 09 menolak `str(tuple)`
sebagai kunci; butir 59–61 memanggil `silang_funding` asli; butir 63 melarang nama
kohort tertulis di dalam modul (aturan 73); butir 37 menuntut `None`, bukan nol.
**`lubang_awal` V1** (`8c36943d`): medan `mati_tidak_setelah_lubang_bukan_awal` memakai
`<=` — **DILARANG dipakai untuk klaim arah** (aturan 80).
**`kohort_ekor` V4** (`c9b63bbe`): `TEBING="2025-07"`, `BULAN_DIHARAPKAN="2026-06"`,
`BATAS_SIMBOL=10`, `PAGU_MUNDUR=60`, `AMBANG_SEPI=0.5`,
`KENDALI_HIDUP=("BTCUSDT","ETHUSDT")`. **Medan `cacah_simbol_bangkit_dapat_diuji` = 0
DILARANG dibaca sebagai ketiadaan kebangkitan (KC-53).**
**`kehidupan`** (`f49abb2b`): `AMBANG_SEPI=0.5`, `BULAN_MULAI="2025-07"`,
`BULAN_AKHIR="2026-06"`.

Sidik lain: `sebab_bangkit` V1 `bafe4359…221a` · `tersisip_semesta` V1 `9618fd19…c537c` ·
`bentangan_kohort` V2 `8ca6ebbe…f32c` · `lubang_awal` V1 `156499ce…f2362`. Sidik manifes
per pecahan: `_0` `88d5704c` · `_1` `64311545` · `_2` `6bbc9990` · `_3` `b6f5f27e` ·
`_4` `d204f353` · `_5` `3b0e2d22` · `_6` `356ae3d6` · `_7` `2abc9c73`.

## Hipotesis

- H-A001 belum diuji · H-A002b GUGUR · H-A003 MENANG pada 3, GUGUR pada 9 · H-A004 tak
  dapat diuji · H-A005 GUGUR · H-A006 MENANG enam run · H-A008 MENANG dua kali ·
  H-A009 GUGUR · **H-A010 MENANG 5–0** · **H-A011 TERBUKTI** · H-A012 MENANG ·
  H-A013 MENANG 6–0, TAFSIR DICABUT · H-A014 BENTUK BARU MENANG 9 dari 9 · H-A015
  MENANG sebagai angka, DIBATASI sebagai tafsir (KC-45) · H-A016 PENGAMATAN, BELUM
  DIUJI.
- **H-A011 [TERBUKTI lewat R-314, ADR-A020 kep. 1].** LITUSDT 2026-01..2026-06,
  `h_a011_cacah_bulan` **6**, `h_a011_cacah_hidup` **6**. **Batas tafsir MENGIKAT:** satu
  simbol, satu rentetan (KC-47) → generalisasi DILARANG; kalimat sebab DILARANG.
- **H-A017** DICABUT sebagai pola semesta (ADR-A011/A012, dilemahkan R-306): bukti
  lepas-tebing tinggal **1** simbol.
- **H-A018 — byte parquet sebagai gejala kehidupan.** **BOLEH:** "bulan MATI menempati
  bagian KECIL dari byte semesta (**0,0177** dari 32,7 GB) dan rata-rata sekitar **4,3×**
  lebih kecil daripada bulan HIDUP". **DILARANG:** "berkas kecil berarti pasar mati".
- **H-A019 [DIUJI R-309 — DITERIMA TERBATAS, ADR-A016 kep. 1].** Irisan asimetris, bukan
  sebab. **DILEMAHKAN oleh ADR-A018 kep. 6 tanpa tafsir pengganti.**
- **H-A020 [DIUSULKAN, BELUM DIUJI, TANPA JALAN UJI YANG DIKETAHUI].** *Ketujuh baris
  MATI tak penuh berbulan `2024-05` adalah SATU peristiwa.* Uji yang direncanakan
  MUSTAHIL.
- **H-A021 [DIUSULKAN, BELUM DIUJI, TANPA JALAN UJI YANG DIKETAHUI].** *Kekosongan
  ANCUSDT dan LUNAUSDT `2022-05` adalah SATU peristiwa.* Dasarnya hanya selisih sembilan
  lilin. Uji MUSTAHIL. Bila kelak DITERIMA, cacah pengamatan bebas dalam sepuluh teratas
  turun dari 10 ke 9, dan `bagian_teratas` **tidak berubah**.
- **H-A022 [TERBUKTI lewat R-313].** *Selisih 516.135 adalah tepat jumlah baris pada 12
  parquet karantina di luar penyebut 19.586.* **Batas tafsir (ADR-A019 kep. 6):** yang
  terbukti **identitas himpunan**, bukan sebab karantina.
- Hipotesis berikutnya **H-A023** — calon isinya poros gerbang BNXUSDT, **belum
  dirumuskan**.

## Aturan 87 RESMI dan usulan 88

**Aturan 87 [RESMI, STATE v57].** Ramalan yang **turunan** — yakni yang angkanya berasal
dari docstring, laporan yang sudah ada, atau penalaran orang lain — **wajib ditandai
TURUNAN pada saat praregistrasi**, sebelum bahan dibuka. Kemenangannya **tidak dihitung
sebagai kemenangan penalaran baru**; kekalahannya **tetap dihitung penuh**.
Dasarnya: R-314 butir 2 dan 3 (ADR-A020 kep. 4 dan 7).

**Usulan aturan 88 [DIUSULKAN, BELUM RESMI].** Setiap bacaan tafsir yang berdiri di atas
**nama medan** wajib diberi tanggal kedaluwarsa: ia gugur sendiri bila definisi medannya
belum disalin dari sumber dalam dua versi berkas akar. **Catatan kejujuran yang melekat:**
bila kelak diresmikan, ia **utang yang dibayar, bukan laba** — ia hanya menutup lubang
yang sudah dua kali kami jatuhi (Koreksi 11 butir 2 dan Koreksi 13).

## Praregistrasi R-316 — BELUM ADA

Porosnya **wajib ditulis di jurnal lebih dulu** (aturan 79), pada giliran yang BERBEDA
dari adjudikasi (ADR-A016). Urutan resmi poros (ADR-A021 kep. 7):

1. **BNXUSDT 2022-06 dan 2022-08 lawan gerbang** — mengapa dua bulan **di dalam** rentang
   klines tidak lolos. Bahan calon: `reports/kehidupan_arsip_*.json` dan
   **`lux_ai/serapan/gerbang_1m.py`** (`c8cc54c8`, belum dibaca utuh). **PERINGKAT
   PERTAMA.**
2. **Sebab kekosongan TLMUSDT 2023-03** (2.130/44.640, 95,2% kosong, HIDUP).
3. **Tebing funding `2025-07`** (39 simbol) **dan BTCSTUSDT** — keserian dengan lubang
   LITUSDT yang juga mulai `2025-07` **BELUM diukur, DILARANG diklaim**.
4. **Identitas dua belas simbol-bulan karantina** — menuntut **modul CI**; manifes
   **20.533.802 B**. **BUKAN kandidat murah** (Koreksi 11).
5. **"Bulan pertama di penyebut" lawan "bulan pertama di bursa"**.
6. Sisanya: selisih 40−38 `diagnosa_kc15`; bentangan 38 kohort; H-A016; `mati_tersisip`;
   R-7/19/20/28/36/37; R-199; R-236..R-247; **taksonomi lubang tiga kelas**; bagian
   `baris_mati`.

**SEBELAS SYARAT KUMULATIF sebelum pita R-316 dikunci** (naik dari sepuluh, UKUR v15):
aturan **79** (di `journal/**`, giliran berbeda, sebelum laporan dibuka) · aturan **83**
(aritmetika implikasi tertulis) · aturan **84** (satu klausa per butir) · aturan **85**
(tepi terpusat di lantai aritmetis atau paling banyak satu orde di atasnya) ·
**aturan 86 (a)** (`reports/` diperiksa lebih dulu) · **aturan 86 (b)** (praregistrasi
docstring modul terkait diperiksa lebih dulu) · **aturan 87** (butir TURUNAN ditandai di
muka) · **kebebasan tiap medan diperiksa terhadap kode** · **KC-50** · **KC-52** ·
**KC-53** · **KC-54** (definisi medan disalin dari sumber sebelum dipakai) · aturan
**66**.

## Utang ukur yang masih hidup

1. **LUNAS [v14]** — aturan 52 atas trio `c1dc0009`.
2. **`karantina_semesta.yml`** (`de40fa4e`) belum dibaca utuh; begitu pula
   `test_pulihkan.py` (`11c43533`), `test_rilis_karantina.py` (`739c8da9`),
   `test_karantina_a006.py` (`a5a3d82f`), dan `tests/test_lubang_tengah.py`.
3. **Lima ADR belum dibaca utuh:** A002, A004, A006, A007, A008.
4. **Identitas dua belas simbol-bulan karantina** belum didaftar; biayanya **terukur**
   (20.533.802 B) dan menuntut modul CI.
5. **LUNAS [v16]** — irisan 880 lawan 877 diukur; ketiga lubang tak dikenal bernama
   (BNXUSDT 2022-04 / 2022-06 / 2022-08).
6. **Perbedaan "bulan pertama di penyebut" lawan "bulan pertama di bursa"** belum
   diukur (ADR-A016 kep. 6).
7. **Sebab kekosongan TLMUSDT 2023-03** belum diukur.
8. **Cacah tangan aturan 66 ulang** — 50/54/45 TURUNAN, DILARANG dikutip terukur.
9. **`ukur_baris` V6** — `BERKAS_DIUKUR` 21 nama; `silang_funding.py` V2 sudah **705**
   baris dari pagar 800 (jarak **95**).
10. **Tiga butir `PETA_MODUL.md` bertanda "memerlukan verifikasi"** (repo WARISAN).
11. **`PROMPT_KELANJUTAN.md`** belum diberi kepala "ARSIP — BUKAN SUMBER";
    **`PROMPT.md` v55** belum didorong.
12. **LUNAS [v15]** — ADR-A020 ada. **[v16] ADR-A021** ada pula (blob
    `3e756672ca355ea976bf2931d278e37fe9057d0d`, commit `2cee14b7`, sepuluh keputusan,
    dibaca utuh).
13. **LUNAS [v16]** — jurnal 144 (`fcc93745…`, commit `1146b96a`, praregistrasi R-315)
    dan jurnal 145 (`d9b63433…`, commit `526e41e8`, adjudikasi R-315) ada dan dibaca
    utuh. **Digantikan:** **jurnal 146 + praregistrasi R-316** belum ditulis — pekerjaan
    ukur berikutnya. **Nama jurnal wajib memakai tanggal UTC** (kesalahan dokumen butir
    15, LUNAS di STATE v57).
14. **BARU [v16]** — laporan CI atas push berkas ini (**aturan 38 ke-57**) wajib dibaca
    sebelum push akar berikutnya.
15. **R-228 belum diadjudikasi**; cacah 56 butir `tests/test_lubang_tengah.py` DILARANG
    dikutip terukur sampai berkasnya dibaca.
16. **Keserian tebing `2025-07`** antara 39 simbol tebing funding dan lubang LITUSDT
    belum diukur; **DILARANG diklaim**.
17. **BARU [v16] — bagian `baris_mati` `reports/silang_funding.json` belum terbaca**
    (alat terpotong pada **54%**). Cacah total `baris_mati` **DILARANG diklaim terukur**;
    TLMUSDT **20** lawan **19** tetap **utang bacaan**, bukan pertentangan terukur.
    Terdaftar sebagai **utang verifikasi 39** di EKOR v16. Penyelesaian menuntut **modul
    CI** atau **pembacaan berpotong terancang**.
18. **BARU [v16] — `gerbang_1m.py` (`c8cc54c8`) belum dibaca utuh**, padahal ia bahan
    poros peringkat pertama.
19. **BARU [v16] — prasyarat klasifikasi belum dipenuhi.** Serapan funding **matang
    sebagai pembukuan, belum matang sebagai landasan fitur**: ADR-A003 (taksonomi rezim)
    **belum ada**; irisan 787 simbol funding lawan 787 simbol klines **belum diukur**
    (KC-52); 87 "funding tanpa klines" atas 787 **belum didamaikan**; kelas positif
    `cacah_hidup_tanpa_funding` **33** hanya dari **lima** simbol (KC-47 menyala);
    taksonomi lubang tiga kelas masih **BENTUK, bukan MEKANISME** (KC-54, usulan 88).

## Penomoran berikutnya

Aturan resmi **1–81, 83, 84, 85, 86 (a) dan (b), 87** · usulan tersisa **77**, **78**,
**82**, **88** · **aturan berikutnya yang bebas 89** · KC resmi sampai **KC-54** (KC-16
kosong selamanya) · **KC berikutnya KC-55** · Hipotesis berikutnya **H-A023** · Jurnal
berikutnya **146** (tanggal **UTC**) · `STATE.md` berikutnya **v58** · EKOR berikutnya
**v17** · UKUR berikutnya **v17** · PROMPT berikutnya **v55 (belum didorong)** · ADR
berikutnya **A022** · Ramalan berikutnya **R-316** · papan skor **318 SAH** (TEPAT
**221** · MELESET **59** · SEPARUH **22** · TIDAK TERADJUDIKASI **9** · MENUNGGU **7**).
