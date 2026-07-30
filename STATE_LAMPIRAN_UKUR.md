# STATE lampiran UKUR — bagian 3 dari STATE (v15, milik STATE v56)

**Kedudukan berkas ini.** STATE dipecah tiga sejak v43 (KC-42). Pembagian berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, 83, 84, 85, **86 (a) dan (b)**;
   KC-1..**KC-53**.
2. **`STATE_LAMPIRAN_EKOR.md`** v15 (blob **`e3fd04c267b702b308e50110b5b7f697b6bbf80d`**)
   — bagian 2: papan skor, ADR, catatan kejujuran.
3. **`STATE_LAMPIRAN_UKUR.md`** (berkas ini, v15) — bagian 3: pengukuran, modul,
   workflow, uji, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) dan **`PROMPT_KELANJUTAN.md`** (blob
   `35beed44`) — **arsip; BUKAN sumber** (ADR-A018 kep. 9).

Dasar v15: UKUR v14 (blob **`69d95bc490441ff19f74b4ac5a1b3e8258fdbacb`**), dibaca UTUH
pada giliran yang sama sebelum berkas ini ditulis (aturan 52, pencegahan KC-43).

**Apa yang v15 bawa, disebut di muka:** v14 membawa pembacaan kode yang menutup utang
aturan 52 terbesar. **v15 membawa PEMBACAAN LAPORAN yang menuntaskan satu poros dan
membunuh dua hipotesis sekaligus** — bukan dengan menyangkalnya, melainkan dengan
menunjukkan bahwa **bahan ujinya tidak ada**.

## KESERASIAN VERSI — SERASI PENUH pada v56 / v15 / v15

- `STATE.md` **v56** — blob **`3ac9c3698583b2e528015a5d36bfb9aa1cc3bd0c`**, commit
  **`019d16eaa7d2dbd1a97a2f10b2db6d9cae1d1bc7`**.
- `STATE_LAMPIRAN_EKOR.md` **v15** — blob
  **`e3fd04c267b702b308e50110b5b7f697b6bbf80d`**, commit
  **`94c7d9da8babdf586ae3f821a13781321a7fd40d`**.
- `STATE_LAMPIRAN_UKUR.md` **v15** — berkas ini.

Ketertinggalan satu versi yang dicatat EKOR v15 — bahwa berkas ini masih berkepala
"milik STATE v55" dan **tidak memuat** ADR-A020, KC-53, aturan 86 butir (b), usulan
aturan 87, adjudikasi R-314, H-A011 TERBUKTI, mustahilnya uji H-A020/H-A021, jurnal 142
dan 143, maupun aturan 38 ke-51..ke-53 — **LUNAS oleh berkas ini**. Ketiga bagian serasi
kembali. **Satu berkas per push tetap MENGIKAT** (KC-42, KC-43).

**Tentang push berkas ini:** ia di akar repo sehingga menyalakan `ci.yml`. Tidak satu
pun `tests/**` berubah, jadi cacah uji tetap **1377** — ramalan **deterministik**,
**MUDAH**, TIDAK masuk papan skor, TIDAK menambah beruntun aturan 57. **Laporannya
WAJIB dibaca sebelum push akar berikutnya**, atau ia hangus seperti run `30547842823`.

**Angka yang TIDAK berubah dari v44/v45/v6/v7** (tidak diulang): taksonomi 9 kelas,
bulan ABSEN 11, H-A013..H-A015, terhenti, SETTLED. Rinciannya di v44 (blob
`d302caff`), v45 (`eb826817`), v6 (`27e59a79`), v7 (`4e7fb65b`).

## KOREKSI KC-41 — BACA SEBELUM MENGUTIP BERKAS INI

Kedua belas koreksi di bawah **tetap dicantumkan** karena semuanya soal dokumen kami
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

**Koreksi 11 [BARU v15] — DUA CACAT DALAM SATU KEPUTUSAN, dicabut ADR-A020 kep. 8.**
ADR-A019 kep. 9 (disalin utuh ke UKUR v14, bagian "Praregistrasi R-314") memuat dua
kekeliruan:

1. Poros identitas dua belas simbol-bulan karantina disebut **"kandidat termurah"**.
   **SALAH.** Kedelapan manifes berjumlah **20.533.802 B** — mustahil dibaca lewat alat
   (batas baca ±30.000 token). Ini **kejadian keempat** taksiran biaya yang keliru, dan
   **yang pertama berarah terlalu murah**.
2. Poros lubang tengah dilabeli **"gugus `2022-05` dan `2024-05`"**. **SALAH.** Keenam
   lubang tengah yang terukur berbulan **2022-01** (BTCSTUSDT) dan **2025-07..2025-11**
   (LITUSDT). Label `2022-05` sebenarnya adalah **`bulan_klines_pertama` BNXUSDT** pada
   tabel H-A010 — satu medan yang berpindah tempat menjadi nama poros. **Bagaimana
   perpindahan itu terjadi TIDAK diukur, karena itu TIDAK diklaim** (aturan 21).

**Koreksi 12 [BARU v15] — KLAIM KEBARUAN DIPERSEMPIT.** Jurnal 142 §4 mengumumkan
**880 / 877 / 3** sebagai temuan giliran itu. Ketiga angka **sudah tertulis di STATE
v55**. Yang benar-benar baru hanya **letak** selisih 3: seluruhnya di kelas **AWAL**
(48 − 45 = 3; ekor 826 − 826 = 0; tengah 6 − 6 = 0). Rumusan resmi STATE v56: *"Ini
kelas KC-19 dalam bentuk halus: mengumumkan sebagai baru apa yang sudah tertulis di
dokumen sendiri."*

**Bacaan jujur atas Koreksi 4, 9, 10, 11, dan 12 bersama-sama:** cacat yang bertahan
paling lama di riset ini bukan salah hitung, melainkan **tafsir yang terdengar masuk
akal atas angka yang benar** — dan, sejak v15, **label yang terdengar masuk akal atas
medan yang benar**.

## BATAS KEKUATAN ATURAN 52 — DIPERSEMPIT, BUKAN DICABUT

> Pembacaan ulang **dokumen sendiri** lemah terhadap penalaran cacat: ia membaca
> kalimat yang sudah diyakini benar. Pembacaan **kode** kuat terhadapnya: kode
> menyatakan identitas yang tidak dapat ditawar, dan ketidakcocokan antara docstring
> dan badan fungsi tampak begitu keduanya dibaca berdampingan.

**[v15] Bukti kedua, kali ini dari sisi kelemahan:** Koreksi 11 dan 12 keduanya lolos
dari berkali-kali pembacaan ulang dokumen, dan runtuh hanya ketika **laporan** dibuka.
**DILARANG** menulis bahwa aturan 52 menjaga mutu penalaran **atas dokumen**.

## Semesta riset = `perpetual_usdt` = penyebut 787 — tidak berubah

- `cacah_perpetual_usdt` **787** = `cacah_penyebut_simbol` **787**
- `cacah_perpetual_usdt_luar_penyebut` 0, `cacah_penyebut_bukan_perpetual_usdt` 0
- Batas wajib disebut: token saham/ETF/komoditas ikut di dalam 787.
- **[v15] PERINGATAN KC-52 BARU:** `lubang_tengah` melaporkan
  `cacah_per_simbol_funding` = **787**, angka yang **sama besar** dengan cacah simbol
  klines. **Kesamaan angka DILARANG dibaca sebagai kesamaan himpunan** sampai irisannya
  diukur; justru pasangan penyebut yang sama besar paling berbahaya, sebab tidak ada
  selisih yang menyalakan alarm. Penguat kewaspadaan: docstring `funding.py` V6
  mencacah **87** simbol "funding tanpa klines" atas 787 simbol itu.

## KC-18 — semesta kehidupan (dikonfirmasi ulang oleh R-307..R-314)

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

**[v15] Pembelahan ketiga atas lubang funding — kini dengan kelas bentuk:**

| kelas bentuk | seluruh semesta | di dalam penyebut | selisih |
| --- | --- | --- | --- |
| awal | **48** | **45** | **3** |
| ekor | **826** | **826** | 0 |
| tengah | **6** | **6** | 0 |
| **jumlah** | **880** | **877** | **3** |

Seluruh selisih 3 duduk di kelas **AWAL**. **Irisan per simbol-bulan BELUM diukur** —
itulah poros peringkat pertama sekarang (`reports/silang_funding.json`, blob
**`b61fe8b3bcabbfce435dd5e5f78fc367f6bef617`**).

## [BARU v15] LUBANG TENGAH — POROS TUNTAS OLEH SATU PEMBACAAN

Sumber: **`reports/lubang_tengah.json`**, blob
**`39cd1caacedc4d49ba23c91c80f553bb9fb135a6`**, **11.014 B**, dibaca UTUH pada ref
`ae867f2e`. `waktu_utc` **2026-07-29T09:38:52Z** — **dua hari sebelum pertanyaannya
dirumuskan** (kejadian ketiga aturan 86 (a), TERKONFIRMASI PENUH).
`versi_lubang_tengah` **2** · `versi_funding` **6**.

### Ringkasan, medan demi medan

| medan | nilai |
| --- | --- |
| `penyebut_kehidupan` | **19.586** |
| `cacah_baris_dengan_medan` | **19.586** |
| `cacah_lubang_funding` | **880** |
| `cacah_lubang_tengah` | **6** |
| `selisih_lubang_tengah` | **0** |
| `cacah_lubang_ganda` | **0** |
| `cacah_kunci_ganda` | **0** |
| `cacah_laporan_dibaca` | **8** (= `total_pecahan` 8) |
| `cacah_per_simbol_funding` | **787** |
| `sebaran_status_lubang_tengah` | HIDUP **0** · MATI **6** · SEPI 0 · TAK_TERUKUR 0 |
| `h_a010_menang` | **true** (5–0) |
| `h_a010_funding_tanpa_klines_kosong` | **true** |
| `h_a010_cacah_simbol_berisi` | **0** |
| `h_a010_cacah_simbol_tak_terukur` | **0** |
| `h_a011_menang` | **true** |
| `h_a011_terukur` | **true** |
| `h_a011_cacah_bulan` | **6** |
| `h_a011_cacah_hidup` | **6** |
| `kendali_sah` | **true** |
| `sidik_seragam` | **true** |
| `laporan_hilang` | **[]** |
| `medan_diminta` | `"cacah_lilin"` |

Sidik: `sidik_kode`
**`c9372bd763b86cfeb2adcf0a0c0c43dae8d9aa9a6508e9c32f7671d5ec7b3f4e`** ·
`sidik_kode_silang_funding`
**`8a9b859c09cd64e30e203e6f8dc53411b8e341c44f112805b3041e5d4d3231b1`** ·
`sidik_data_funding`
**`2c9fbd1b04f74c9c844bc223a99a103d12220b88d08667b3792720e5b9608d24`** ·
`sidik_kode_laporan`
**`24b6bb265525e81c2e571b46e401f36903383f1e3738c487850861adc3e8c595`**.

### Keenam lubang tengah, LENGKAP dan disebut dengan nama

| # | simbol | bulan | status | byte_parquet | `cacah_lilin` |
| --- | --- | --- | --- | --- | --- |
| 1 | **BTCSTUSDT** | **2022-01** | MATI | 399.757 | 44.640 |
| 2 | **LITUSDT** | **2025-07** | MATI | 427.922 | 44.640 |
| 3 | **LITUSDT** | **2025-08** | MATI | 427.505 | 44.640 |
| 4 | **LITUSDT** | **2025-09** | MATI | 392.233 | 43.200 |
| 5 | **LITUSDT** | **2025-10** | MATI | 434.201 | 44.640 |
| 6 | **LITUSDT** | **2025-11** | MATI | 389.479 | 43.200 |

- BTCSTUSDT: rentetan **1**, tetangga **2021-12 → 2022-02**, `bulan_klines_pertama`
  **2021-03**, `cacah_bulan_klines` **64**, `cacah_lubang` **1**.
- LITUSDT: rentetan **5**, tetangga **2025-06 → 2026-01**, `bulan_klines_pertama`
  **2021-02**, `cacah_bulan_klines` **64**, `cacah_lubang` **5**. Bulan klines terakhir
  keduanya **2026-06**.
- **TIDAK SATU PUN berbulan `2022-05` atau `2024-05`.** Keenamnya **penuh lilin** atau
  hampir penuh — lubangnya di **funding**, bukan di klines.

### H-A011 — MENANG, dan inilah kebangkitan pertama yang terukur di repo

LITUSDT **2026-01..2026-06**: **keenam bulan HIDUP**. Sesudah lima bulan berturut tanpa
funding dan berstatus MATI, simbol yang sama kembali HIDUP dan bertahan enam bulan
sampai tepi rentang.

**Batas tafsir yang MENGIKAT (ADR-A020 kep. 1):**
- **DILARANG** menggeneralisasi ke semesta. Ini **satu simbol, satu rentetan** — KC-47
  terpicu KUAT: enam bulan HIDUP berturut bukan enam pengamatan bebas.
- **DILARANG** menyebut sebab. Tidak ada satu pun medan sebab yang diukur.
- **DIIZINKAN** dikatakan: *fenomena kebangkitan ADA, dan terukur sekali.*

### H-A010 — MENANG 5–0

Kelima simbol berlubang funding bentuk AWAL diperiksa apakah punya medan klines di
bulan-bulan lubangnya:

| simbol | rentang lubang awal | `cacah_bulan_klines` | `cacah_lubang` |
| --- | --- | --- | --- |
| BNXUSDT | 2022-05 → 2023-02 | 48 | 19 |
| ICPUSDT | 2021-05 → 2022-09 | 62 | 16 |
| JUPUSDT | 2024-01 → 2024-02 | 30 | 1 |
| QTUMUSDT | 2020-02 → 2020-03 | 77 | 1 |
| TLMUSDT | 2021-07 → 2023-03 | 60 | 20 |

`funding_tanpa_klines`: kelima simbol `ada_medan` **true**, `bulan` **[]**,
`cacah_bulan` **0**; `cacah_berisi` **0**, `cacah_tak_terukur` **0**,
`kosong_seluruhnya` **true**.

**Aturan 46 kasus ketiga [v15]:** modul menolak menyatakan `kosong_seluruhnya` **true**
bila ada baris tanpa medan — ia menolak menyimpulkan dari ketiadaan pengukuran.

### Kendali dan sumber

`kendali`: tiga baris **BTCUSDT** (2021-05, 2021-08, 2021-01), semuanya **HIDUP** dengan
`funding_ada` **true** → `kendali_sah` true. `sumber`: `reports/funding_semesta.json` +
`reports/kehidupan_arsip_0..7.json`. `medan_per_simbol_funding_terlihat` **10** medan;
`medan_baris_terlihat` **14** medan.

### Konsekuensi pahit: uji H-A020 dan H-A021 MUSTAHIL

STATE v55 dan ADR-A019 kep. 9 menetapkan uji kedua hipotesis itu sebagai "lubang tengah
pada gugus `2022-05` dan `2024-05`". Keenam lubang tengah yang ada **tidak menyentuh
satu pun bulan itu**. Rumusan resmi STATE v56, dikutip apa adanya:

> Uji yang direncanakan bagi H-A020 dan H-A021 **MUSTAHIL** — bukan mahal, bukan
> tertunda, melainkan **tidak ada bahannya**.

**Poros yang dikira menjawab dua hipotesis sekaligus ternyata menjawab NOL.** Keduanya
kini berstatus **DIUSULKAN, BELUM DIUJI, TANPA JALAN UJI YANG DIKETAHUI**.

### Aturan 36 — kasus kedua [v15]

`lubang_tengah` **memakai** `silang_funding.bentuk_lubang_lokal` alih-alih menyalin
definisinya. Akibatnya sebaran bentuk 48/826/6 tidak dapat menyimpang diam-diam antar
modul. Kasus terkuat tetap yang pertama: `selisih_lilin` dan `pulihkan` bertemu di
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
R-312 tidak dapat dimenangkan secara struktural**, dan itu benar **sejak sebelum pita
dikunci**. Kalimat "sesuai dua angka di atas" adalah **KC-52 yang ditulis ulang ke dalam
kode**.

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
  selisih **sembilan lilin**. Ini dan hanya ini dasar **H-A021**; **kebetulan angka,
  bukan bukti**. **[v15] Tidak ada lubang tengah di `2022-05`**, sehingga jalan uji yang
  direncanakan tertutup.
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
  ditulis sebagai temuan.** **[v15] Tidak ada lubang tengah di `2024-05`** → jalan uji
  tertutup.
- **Larangan ADR-A015 kep. 5 TIDAK dibalik** oleh R-310, R-311, R-313, R-314, A018,
  A019, maupun A020.
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
| `cacah_hidup_byte_kecil` (< **97.634**, STRIKT) | **38** (0.0021009564880853653) |
| `cacah_mati_byte_kecil` (< **150.000**, STRIKT) | **2** (0.0014275517487508922) |

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
`bagian_byte_mati` **0.017704297493883234**; `cacah_terukur_byte_kecil` (< 10.000) 0;
`cacah_byte_nol` 0 → **dasar keras ≈22 KB**, sebab langsung KC-48. Adjudikasi R-307:
**MELESET**. Sidik `e02aca2b3967069b500b01d27a1d2d1553f47b912ea41ddbecd9e4e6c33883c7`

## Arah waktu kematian lawan lubang funding [v6, tetap]

`lubang_tebing` V1 run **30524631435** (commit `84b11164`, kode 0), laporan blob
`7d8883f5`. Penyebut **118**.

| kelas arah (STRIKT, aturan 80) | cacah | bagian |
| --- | --- | --- |
| `mati_dulu` | **40** | **0.339** |
| `serempak` (DILARANG di numerator) | **78** | 0.661 |
| `lubang_dulu` | **0** | 0.000 |

`cacah_tebing_butir_2` **39** (`2025-07`); **39 dari 40** `mati_dulu` ada di tebing
(0.975); satu-satunya bukan-tebing **BTCSTUSDT** → KC-47, aturan 81. Adjudikasi R-306:
TEPAT 3/3.
**[v15] Catatan yang WAJIB ditahan:** BTCSTUSDT muncul lagi sebagai satu-satunya lubang
tengah di luar LITUSDT, dan LITUSDT berlubang mulai **`2025-07`** — bulan tebing itu
juga. **Keserian itu BELUM diukur dan DILARANG diklaim** (aturan 21); ia poros nomor 4.
Sidik `4a5c2e4279eb1554dc119b48d6a8db61f6ea4ee11b7539efd70ee71d1ae18bf3`

## Lubang funding — agregat semesta (tetap)

- `cacah_simbol_ada_lubang` **122** dari 787 · awal **5** · bukan-awal **118**.
- BNXUSDT punya lubang AWAL dan bukan-awal sekaligus.
- Lima bentuk AWAL: BNXUSDT, ICPUSDT, JUPUSDT, QTUMUSDT, TLMUSDT. ICP dan TLM lubang
  awalnya melewati kematian (sumber salah-baca R-304, KC-46).
- Lubang funding **880** semesta / **877** dalam penyebut / **3** tak dikenal;
  **[v15] ketiganya di kelas AWAL**. **Irisan per simbol-bulan BELUM diukur.**
- Dari 945 MATI di luar kohort: **386** kehilangan funding, **559** berfunding.

## Jumlah uji — terukur

**1377, kini SEMBILAN bacaan berjejak.**

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
7. **[v15]** blob **`aeb4315ad73806b61f734f9c1d92b27b1ae2727b`**, run **30581703827**,
   commit **`6157586e`** (UKUR v14), 21:02:01Z, kode 0, `… in 0.61s`.
8. **[v15]** blob **`19785af1d96fdc1fabec2dfa9f7c3dbaf60b3708`**, run **30583686515**,
   commit **`019d16ea`** (STATE v56), 21:31:10Z, kode 0, `… in 0.61s`.
9. **[v15]** blob **`5f4282f6d8f21cae7c2f6786ea29072ab4175973`**, run **30584737431**,
   commit **`94c7d9da`** (EKOR v15), 21:47:25Z, kode 0, `… in 0.60s`.

Turunan: 1341 + **36** butir `tests/test_selisih_lilin.py` = **1377** ✅ (aturan 21),
terverifikasi dari sumber.

Riwayat: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 → 984 →
1044 → 1100 → 1168 → 1233 → 1297 → 1341 (enam run) → **1377** (sembilan run berjejak).

**Aturan 57: beruntun 4 dari 4** sesudah PUTUS di 26/27. Tidak bertambah sejak trio.
Ia **mencacah, bukan menaksir**.

### Aturan 38 — ordinal, kini sampai ke-53

Definisi yang berlaku (ADR-A018 kep. 8): pemakaian dihitung **hanya** untuk pembacaan
`reports/ci_terakhir.json` yang meninggalkan **jejak tertulis** berupa nomor run,
commit, dan blob.

| ke- | CI | run | commit | blob | jejak |
| --- | --- | --- | --- | --- | --- |
| 47 | 1377 | 30576963781 | `6642ed68` | `8cbbd4ce` | jurnal 141, STATE v55 |
| 48 | 1377 | 30577779309 | `2bdd8233` | `8ec97de5` | jurnal 141, STATE v55 |
| 49 | 1377 | 30579348728 | `cd209f3e` | `94d270e7` | EKOR v14, STATE v56 |
| 50 | 1377 | 30580133552 | `a722ec63` | `04bfa2ed` | UKUR v14, STATE v56 |
| 51 | 1377 | 30581703827 | `6157586e` | `aeb4315a` | jurnal 142, STATE v56 |
| 52 | 1377 | 30583686515 | `019d16ea` | `19785af1` | EKOR v15 |
| **53** | **1377** | **30584737431** | **`94c7d9da`** | **`5f4282f6d8f21cae7c2f6786ea29072ab4175973`** | **berkas ini** |

**Pemakaian berjalan = ke-lima puluh tiga.** Pemakaian ke-53 dibaca
**2026-07-30T21:47:25Z**, kode keluar **0**, atas push EKOR v15 — **dibaca sebelum
tertimpa**, sehingga ramalan "CI tetap 1377" untuk push itu **TERUKUR dan TEPAT**, tetap
**MUDAH**, tetap tidak diskor.

**[v15] DUA BELAS pembacaan berturut (ke-42..ke-53) tanpa satu pun laporan hangus.**

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
V2 `4d3beaf18c070d2931044c50dd5a354d75eaceb8` (23.745 B, DIBACA UTUH [v15])**,
`kohort_ekor.py` `c9b63bbe`, `lubang_awal.py` `8c36943d`, `lubang_tebing.py` `575e777e`,
`sebab_bangkit.py` `fd5a1dc4`, `tersisip_semesta.py` `8a648838`, `bentangan_kohort.py`
V2 `f4eae57a`, `byte_semesta.py` `ff68e4be`, `funding.py` `8d4b1f82`, `rilis.py`
`2e44530c`, `karantina_semesta.py` `46e7c46b`, `arsip.py` `0104958b`, `gerbang_1m.py`
`c8cc54c8`, `resample.py` `66a4b177`, `semesta_kuota.py` `7288b030`, `bulan_absen.py`
`10279d72`, `kebangkitan.py` `446321ee`, `penyebut_tahun.py` `265aad00`,
`anatomi_tengah.py` `04279335`, `__init__.py` `64d85584`. `ci.yml` =
**`c79497b2c812679eaa69aee5b3160eac9f5c5fb7`** (paths-ignore `journal/**`,
`decisions/**`, `hipotesis/**`, `reports/**`; push ke `lux_ai/**`, `tests/**`, `STATE*`,
`PROMPT*` MENYALAKAN CI — **terkonfirmasi lima kali berturut**). `karantina_semesta.yml`
= `de40fa4e` (**belum dibaca utuh**).

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
**[v15] `tests/test_lubang_tengah.py` — 56 butir menurut praregistrasi R-228, BELUM
DIBACA. DILARANG dikutip sebagai cacah terukur; R-228 belum diadjudikasi.**

**POLA WORKFLOW TRIO — TERVERIFIKASI DARI SUMBER** (`selisih_lilin.yml`, blob
`de2fd4fd…`): `name`, `on.push.paths` **SATU** entri, `permissions: contents: write`,
job `ukur` di `ubuntu-latest`, checkout@v4 + setup-python@v5 (3.11),
`pip install numpy pandas pyarrow pyyaml`, langkah `jalan` id=`jalan` dengan `set +e` →
`KODE=$?` → `echo "kode=$KODE" >> "$GITHUB_OUTPUT"` → `exit 0`, langkah `catat status`,
langkah `dorong laporan` (`[skip ci]`, `git pull --rebase`), penutup
`exit ${{ steps.jalan.outputs.kode }}`. **Aturan 55 LUNAS untuk berkas ini.**

## API terverifikasi

API lama (v37–v12) tetap berlaku. Tambahan v13–v15 **seluruhnya dibaca UTUH dari kode**
(KC-43).

**[BARU v15] `lubang_tengah` V2** (blob
**`4d3beaf18c070d2931044c50dd5a354d75eaceb8`**, 23.745 B, DIBACA UTUH).
Tetapan: `VERSI=2` · `KELUARAN="reports/lubang_tengah.json"` · `TENGAH_TERCATAT=6` ·
`SIMBOL_H_A010=["BNXUSDT","ICPUSDT","JUPUSDT","QTUMUSDT","TLMUSDT"]` ·
`SIMBOL_TENGAH_TERCATAT=["BTCSTUSDT","LITUSDT"]` · `SIMBOL_H_A011="LITUSDT"` ·
`RENTANG_H_A011=("2026-01","2026-06")` ·
`BERKAS_DICAP=["kehidupan.py","kehidupan_arsip.py","lubang_tengah.py","silang_funding.py"]`.
**Enam belas fungsi**; **lima penggugur** dikunci di muka; **enam praregistrasi di
docstring** (R-221, R-222, R-223 TEPAT; **R-229 TEPAT**, **R-230 MELESET**; R-228 belum
diadjudikasi).
**Aturan 36 ditegakkan di dalam kode:** modul **memakai**
`silang_funding.bentuk_lubang_lokal`, tidak menyalinnya.
**Aturan 46 ditegakkan di dalam kode:** `funding_tanpa_klines` menolak
`kosong_seluruhnya` true bila ada baris tanpa medan.
Angka yang terbaca dari docstring (**TURUNAN, bukan pengukuran berkas ini**):
`funding.py` V6 mencacah **87** "funding tanpa klines" atas **787** simbol;
`silang_funding.py` V2 = **705 baris**; sebaran dalam penyebut awal **45** / ekor **826**
/ tengah **6** / seluruh **0**.

**`pulihkan` V2** (blob `a9e6eab7cc47555dfed919ac63044ff2eadc4893`, 14.839 B).
Tetapan: `VERSI=2`, `TOTAL_PECAHAN=8`, `AKAR_UNDUH="data/unduh"`,
`AKAR_PULIH="data/pulih"`. Fungsi: **`nama_manifes(i)`** · **`nama_status_serapan(i)`** ·
**`nama_keluaran(i)="reports/pulihkan_pecahan_<i>.json"`** · `nama_tag(i,run_id)` ·
`sidik_kode()` mencap `["pulihkan.py","rilis.py"]` · `run_id_sumber` ·
**`putuskan_definisi(...)`** → `(kesimpulan, dapat_dibedakan)` · `anggota_aman` ·
**`cacah_baris_parquet(jalur)` = `pq.ParquetFile(...).metadata.num_rows`** ·
`periksa_bagian` · **`periksa_keluarga`** dipanggil **dua kali**, atas `manifes["rilis"]`
dan **`manifes["rilis_karantina"]`** — tempat karantina dicacah terpisah · `_utuh` ·
`jalankan` · `main` (env `PULIH_INDEKS`). Praregistrasi historis **R-198**.

**`kehidupan_arsip` V1** (blob `318a5cb187406d16cfd3385d653bed905f632934`, 19.281 B).
Tetapan: `VERSI=1`, `TOTAL_PECAHAN=8`, `AKAR_BONGKAR="data/kehidupan_arsip"`,
`KENDALI_CACAH=3`, `KOLOM_VOLUME="volume"`, `KOLOM_TRANSAKSI="trades"`,
`BERKAS_DICAP` 5 nama, `nama_keluaran(i)="reports/kehidupan_arsip_<i>.json"`.
Fungsi: `peta_parquet` (**melewatkan baris `parquet_karantina`**), `_angka`,
**`ukur_kolom`** → `{cacah_lilin, cacah_lilin_terbaca, cacah_baris_cacat,
transaksi_total, cacah_volume_nol, bagian_volume_nol}`, `ukur_parquet`,
`baris_kehidupan`, **`kendali_pecahan`**, `ringkas_pecahan`, `kode_keluar`, `_cocokkan`,
`periksa_bagian`, `jalankan`, `berkas_ringkas`, `main`.

**`selisih_lilin` V1** (blob `d19bdb5fe67e0bd9c1b141d7fb7cc6dcd089c5f2`). Tetapan:
`VERSI=1` · `KELUARAN` + `KELUARAN_RINGKAS` · `BATAS_BARIS_LAPORAN=40` ·
`MEDAN_KLAIM="cacah_lilin"` · `MEDAN_TERBACA="cacah_lilin_terbaca"` · `CACAH_TERATAS=10`
· `LILIN_LANGSUNG_TERCATAT=839325999` · `BARIS_PARQUET_TERCATAT=839842134` ·
`SELISIH_TERCATAT=516135` · `AMBANG_HIDUP_KECIL=97634` · `INVARIAN` **8** kunci ·
`R312_PITA_BUTIR_1=(12,120)` · `R312_PITA_BUTIR_2=(0.50,0.865)` · `BERKAS_DICAP` **4**
nama. **Empat kendali lolos**; `kendali_deteksi` **11 medan** (klaim 213.480 · terbaca
214.360 · bersih 880 · positif 1.080 · negatif 200 · berselisih 3); `kendali_negatif`
menuntut bersih **−250**; `kendali_teratas` **0,9615** = 7.500/7.800. `kode_keluar`
mengembalikan **2** bila `cacah_berselisih <= 0` — **dirancang**.
**Empat syarat gugur DIKUNCI DI MUKA.** Syarat 1 verbatim: *"Medan
`cacah_lilin_terbaca` tidak ada, atau identik dengan `cacah_lilin` di SELURUH baris:
laporan TIDAK TERADJUDIKASI (aturan 41), bukan MELESET."*
Laporan ringkas blob **`e5cc64011030cfb8e1a8edf3699dd01b3caafab7`**: `cacah_baris`
**19586** · `cacah_berselisih` **0** · kedua jumlah **839325999** · `dua_jalur_bertemu`
**true** · `uji_r312.teradjudikasi` **false**.

**`ukur_baris` V5** (blob `3ebaa9f9`, 17.442 B): `PAGAR_BARIS=800`, `BERKAS_DIUKUR`
**21 nama**, uji `test_ukur_baris.py` (`7975bf88`) **3** fungsi. **Utang V6 hidup.**

**`silang_funding` V2** (blob `42c3aa9d`, DIBACA UTUH): `baca_laporan_kehidupan(akar,
total)` → **TIGA** nilai, kunci tuple `(simbol, bulan)`; **`baca_medan_baris(akar, total,
medan)` → `(nilai, meta)`** dengan peta berkunci `(simbol, bulan)`. Tetapan:
`PENYEBUT_TERCATAT=19586`, `MATI_TERCATAT=1401`, `KOHORT_TERCATAT=456`,
`HIDUP_TANPA_FUNDING_TERCATAT=33`, `LUBANG_TAK_DIKENAL_TERCATAT=3`,
`BENTUK_TERBITAN_FUNDING={"awal":48,"ekor":826,"tengah":6}`, `MEDAN_LILIN="cacah_lilin"`,
`SUMBER_FUNDING="reports/funding_semesta.json"`, `KENDALI_CACAH=3`.

**`keterisian_lilin` V1** (blob `3f80ffa7`): `INVARIAN` =
`{penyebut:19586, cacah_simbol:787, cacah_hidup:18087, cacah_sepi:98, cacah_mati:1401,
total_byte:32706262375, byte_hidup:32049492952, cacah_hidup_byte_kecil:38}` ·
`AMBANG_HIDUP_KECIL=97634` · `MENIT_PER_HARI=1440` · `KENDALI_SIMBOL="BTCUSDT"` ·
`R310_PITA_BUTIR_1=(1,120)` · `R310_PITA_BUTIR_2=(0.02,0.25)`.

**`sisa_defisit` V1** (blob `7aa0e6d7`): `R311_PITA_BUTIR_1=(200,12000)`,
`R311_PITA_BUTIR_2=(0.02,0.45)`, `DEFISIT_SEMBILAN_TERCATAT=95237`,
`DEFISIT_BUKAN_PERTAMA_TERCATAT=808162`, `SISA_TERCATAT=712925`, `INVARIAN` delapan
kunci BEBAS, `JAWABAN_KENDALI` **17 medan**, **`teratas`** mengembalikan **None** bila
baris berdefisit < 10.

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
`KENDALI_HIDUP=("BTCUSDT","ETHUSDT")`. **[v15] Medan
`cacah_simbol_bangkit_dapat_diuji` = 0 DILARANG dibaca sebagai ketiadaan kebangkitan
(KC-53).**
**`kehidupan`** (`f49abb2b`): `AMBANG_SEPI=0.5`, `BULAN_MULAI="2025-07"`,
`BULAN_AKHIR="2026-06"`.

Sidik lain: `sebab_bangkit` V1 `bafe4359…221a` · `tersisip_semesta` V1 `9618fd19…c537c` ·
`bentangan_kohort` V2 `8ca6ebbe…f32c` · `lubang_awal` V1 `156499ce…f2362`. Sidik manifes
per pecahan: `_0` `88d5704c` · `_1` `64311545` · `_2` `6bbc9990` · `_3` `b6f5f27e` ·
`_4` `d204f353` · `_5` `3b0e2d22` · `_6` `356ae3d6` · `_7` `2abc9c73`.

## Hipotesis

- H-A001 belum diuji · H-A002b GUGUR · H-A003 MENANG pada 3, GUGUR pada 9 · H-A004 tak
  dapat diuji · H-A005 GUGUR · H-A006 MENANG enam run · H-A008 MENANG dua kali ·
  H-A009 GUGUR · **H-A010 MENANG 5–0 [dikonfirmasi ulang v15 dari laporan]** ·
  **H-A011 — lihat di bawah** · H-A012 MENANG · H-A013 MENANG 6–0, TAFSIR DICABUT ·
  H-A014 BENTUK BARU MENANG 9 dari 9 · H-A015 MENANG sebagai angka, DIBATASI sebagai
  tafsir (KC-45) · H-A016 PENGAMATAN, BELUM DIUJI.
- **H-A011 [TERBUKTI lewat R-314, ADR-A020 kep. 1].** Terukur: LITUSDT 2026-01..2026-06,
  `h_a011_cacah_bulan` **6**, `h_a011_cacah_hidup` **6**, `h_a011_menang` **true**.
  **Kebangkitan pertama yang terukur di repo ini.** **Batas tafsir MENGIKAT:** satu
  simbol, satu rentetan berturut (KC-47) → **generalisasi ke semesta DILARANG**;
  **kalimat sebab DILARANG**.
- **H-A017** DICABUT sebagai pola semesta (ADR-A011/A012, dilemahkan R-306): bukti
  lepas-tebing tinggal **1** simbol. TIDAK dipulihkan oleh R-307..R-314.
- **H-A018 — byte parquet sebagai gejala kehidupan. DIUKUR DUA KALI (R-307, R-308).**
  **BOLEH:** "bulan MATI menempati bagian KECIL dari byte semesta (**0,0177** dari
  32,7 GB) dan rata-rata sekitar **4,3×** lebih kecil daripada bulan HIDUP".
  **DILARANG:** "berkas kecil berarti pasar mati".
- **H-A019 [DIUJI R-309 — DITERIMA TERBATAS, ADR-A016 kep. 1].** Irisan asimetris, bukan
  sebab. **DILEMAHKAN oleh ADR-A018 kep. 6 tanpa tafsir pengganti.**
- **H-A020 [DIUSULKAN, BELUM DIUJI, TANPA JALAN UJI YANG DIKETAHUI — v15].** *Ketujuh
  baris MATI tak penuh berbulan `2024-05` adalah SATU peristiwa, bukan tujuh pengamatan
  bebas.* **Uji yang direncanakan (lubang tengah atas gugus 2024-05) MUSTAHIL: tidak ada
  satu pun lubang tengah di bulan itu.** Jalan uji baru **belum ditemukan**.
- **H-A021 [DIUSULKAN, BELUM DIUJI, TANPA JALAN UJI YANG DIKETAHUI — v15].**
  *Kekosongan ANCUSDT `2022-05` dan LUNAUSDT `2022-05` adalah SATU peristiwa.* Dasarnya
  hanya selisih **sembilan lilin**. **Uji yang direncanakan MUSTAHIL** dengan alasan
  yang sama. Bila kelak DITERIMA, cacah pengamatan bebas dalam sepuluh teratas turun
  dari 10 ke 9, dan `bagian_teratas` **tidak berubah**.
- **H-A022 [TERBUKTI lewat R-313].** *Selisih 516.135 adalah tepat jumlah baris pada 12
  parquet karantina di luar penyebut 19.586.* **Batas tafsir (ADR-A019 kep. 6):** yang
  terbukti **identitas himpunan**, bukan sebab karantina. Turunan cuma-cuma:
  **`cacah_baris_cacat` = 0 di seluruh semesta**.
- Hipotesis berikutnya **H-A023**.

## Praregistrasi R-314 — TERADJUDIKASI: 2 TEPAT / 1 MELESET

Disimpan apa adanya sebagai jejak (aturan 29). Ditulis di
**`journal/2026-07-30-142.md`** (blob `af11d8a2…`, commit `ae867f2e`) **sebelum**
`reports/lubang_tengah.json` dibuka — **aturan 79 DITAATI SEPENUHNYA, pertama kali sejak
R-313 melanggarnya**.

| butir | ramalan | terukur | vonis |
| --- | --- | --- | --- |
| 1 (BERISIKO, MURNI) | `cacah_per_simbol_funding` ∈ **[747, 827]** | **787** | **TEPAT** |
| 2 (TURUNAN docstring) | `h_a010_cacah_simbol_berisi` = **0** | **0** | **TEPAT** |
| 3 (TURUNAN docstring) | `h_a011_cacah_hidup` = **0** | **6** | **MELESET** |

**Kelima penggugur lolos:** `sidik_seragam` true · `cacah_laporan_dibaca` 8 =
`total_pecahan` 8 · `cacah_kunci_ganda` 0 · `kendali_sah` true ·
`selisih_lubang_tengah` 0. Syarat gugur 3 dan 4 **tidak menyala**; **syarat gugur 5
MENYALA**.

**Pengakuan kejujuran yang melekat permanen (ADR-A020 kep. 4 dan 7):** hanya butir 1
yang **murni**. Butir 2 dan 3 **TURUNAN dari docstring `lubang_tengah.py` V2** —
kemenangan butir 2 bukan kemenangan penalaran baru, dan kekalahan butir 3 adalah
**kekalahan karena mempercayai penalaran orang lain tanpa memeriksanya**. Dari sinilah
**usulan aturan 87** lahir (ramalan turunan wajib ditandai di muka); ia **DIUSULKAN,
BELUM RESMI** karena kejadiannya baru satu.

**Aturan 85 memperoleh adjudikasi pertamanya di sini.** **DIIZINKAN:** "pernah teruji
sekali". **DILARANG:** "teruji", "bekerja", "terbukti".

**R-229 TEPAT dan R-230 MELESET** dicatat di **kolom terpisah, DI LUAR lajur papan
skor** (ADR-A020 kep. 5), sebab pemeriksaan berurutan R-224..R-235 belum dilakukan.
**R-228 BELUM diadjudikasi** — ia menuntut laporan CI atas commit V2 `lubang_tengah`
(run 30436915256 atau berikutnya).

## Praregistrasi R-315 — BELUM ADA

Porosnya **wajib ditulis di jurnal lebih dulu** (aturan 79), pada giliran yang BERBEDA
dari adjudikasi (ADR-A016). Urutan resmi poros (ADR-A020 kep. 9) — **lubang tengah
DIKELUARKAN karena TUNTAS**:

1. **Irisan 880 lawan 877 lubang funding per kelas bentuk** —
   `reports/silang_funding.json` (blob **`b61fe8b3bcabbfce435dd5e5f78fc367f6bef617`**).
   Satu pembacaan; kandidat KC-52 berikutnya. **PERINGKAT PERTAMA.**
2. **Sebab kekosongan TLMUSDT 2023-03** (95,2% kosong, HIDUP).
3. **"Bulan pertama di penyebut" lawan "bulan pertama di bursa"**.
4. **Tebing funding `2025-07`** (39 simbol) **dan BTCSTUSDT** — keserian dengan lubang
   LITUSDT yang juga mulai `2025-07` **BELUM diukur, DILARANG diklaim**.
5. **Identitas dua belas simbol-bulan karantina** — menuntut **modul CI**; manifes
   **20.533.802 B**. **BUKAN kandidat murah** (Koreksi 11).
6. Sisanya: selisih 40−38 `diagnosa_kc15`; BNXUSDT 2022-04/06/08; bentangan 38 kohort;
   H-A016; mati_tersisip; R-7/19/20/28/36/37; R-199; R-236..R-247; taksonomi lubang tiga
   kelas.

**SEPULUH SYARAT KUMULATIF sebelum pita R-315 dikunci** (naik dari sembilan, STATE v56):
aturan **79** (di `journal/**`, giliran berbeda, sebelum laporan dibuka) · aturan **83**
(aritmetika implikasi tertulis) · aturan **84** (satu klausa per butir) · aturan **85**
(tepi terpusat di lantai aritmetis atau paling banyak satu orde di atasnya, dengan
alasan tertulis) · **aturan 86 (a)** (`reports/` diperiksa lebih dulu) · **aturan 86 (b)**
(**praregistrasi docstring modul terkait diperiksa lebih dulu**) · **kebebasan tiap medan
diperiksa terhadap kode** · **KC-50** · **KC-52** · **KC-53** (penyebut dan definisi medan
ditulis pada kalimat yang sama dengan angkanya) · aturan **66**.

## Utang ukur yang masih hidup

1. **LUNAS [v14]** — aturan 52 atas trio `c1dc0009`.
2. **`karantina_semesta.yml`** (`de40fa4e`) belum dibaca utuh; begitu pula
   `test_pulihkan.py` (`11c43533`), `test_rilis_karantina.py` (`739c8da9`),
   `test_karantina_a006.py` (`a5a3d82f`), dan **[v15] `tests/test_lubang_tengah.py`**.
3. **Lima ADR belum dibaca utuh:** A002, A004, A006, A007, A008.
4. **Identitas dua belas simbol-bulan karantina** belum didaftar; biayanya kini
   **terukur** (20.533.802 B) dan menuntut modul CI.
5. **Irisan 880 lawan 877 lubang funding per simbol-bulan** belum diukur — **poros
   peringkat pertama**.
6. **Perbedaan "bulan pertama di penyebut" lawan "bulan pertama di bursa"** belum
   diukur (ADR-A016 kep. 6).
7. **Sebab kekosongan TLMUSDT 2023-03** belum diukur.
8. **Cacah tangan aturan 66 ulang** — 50/54/45 TURUNAN, DILARANG dikutip terukur.
9. **`ukur_baris` V6** — `BERKAS_DIUKUR` 21 nama atas ~50 modul dan ~54 uji;
   `silang_funding.py` V2 sudah **705** baris dari pagar 800.
10. **Tiga butir `PETA_MODUL.md` bertanda "memerlukan verifikasi"** (repo WARISAN).
11. **`PROMPT_KELANJUTAN.md`** belum diberi kepala "ARSIP — BUKAN SUMBER";
    **`PROMPT.md` v55** belum didorong.
12. **LUNAS [v15]** — ADR-A020 ada (blob `200c7e7d737fdfa0b8d689e35482d9ae249b90ee`,
    commit `d8335be1`, sepuluh keputusan, dibaca ulang utuh pada giliran yang sama).
13. **LUNAS [v15]** — jurnal 142 (blob `af11d8a2…`, commit `ae867f2e`) dan jurnal 143
    (blob `fb4ec5ad…`, commit `d92ba0f1`) ada dan dibaca ulang utuh.
    **Digantikan:** **jurnal 144 + praregistrasi R-315** belum ditulis — pekerjaan ukur
    berikutnya.
14. **BARU [v15]** — laporan CI atas push berkas ini (**aturan 38 ke-54**) wajib dibaca
    sebelum push akar berikutnya.
15. **BARU [v15]** — **R-228 belum diadjudikasi**; cacah 56 butir
    `tests/test_lubang_tengah.py` DILARANG dikutip terukur sampai berkasnya dibaca.
16. **BARU [v15]** — **keserian tebing `2025-07`** antara 39 simbol tebing funding dan
    lubang LITUSDT belum diukur; **DILARANG diklaim**.

## Penomoran berikutnya

Aturan resmi **1–81, 83, 84, 85, 86 (a) dan (b)** · usulan tersisa **77**, **78**,
**82**, **87** · **aturan berikutnya yang bebas 88** · KC resmi sampai **KC-53** (KC-16
kosong selamanya) · **KC berikutnya KC-54** · Hipotesis berikutnya **H-A023** · Jurnal
berikutnya **144** · `STATE.md` berikutnya **v57** · EKOR berikutnya **v16** · UKUR
berikutnya **v16** · PROMPT berikutnya **v55 (belum didorong)** · ADR berikutnya **A021**
· Ramalan berikutnya **R-315** · papan skor **316** (TEPAT **220** · MELESET **58** ·
SEPARUH **22** · TIDAK TERADJUDIKASI **9** · MENUNGGU **7**).
