# STATE lampiran UKUR — bagian 3 dari STATE (v17, milik STATE v58)

**Kedudukan berkas ini.** STATE dipecah tiga sejak v43 (KC-42). Pembagian berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, 83, 84, 85, 86 (a) dan (b), **87**;
   KC-1..**KC-55**.
2. **`STATE_LAMPIRAN_EKOR.md`** v17 (blob **`29981b68314264f7897408f31b08bad91e32d4d8`**)
   — bagian 2: papan skor, ADR, catatan kejujuran.
3. **`STATE_LAMPIRAN_UKUR.md`** (berkas ini, v17) — bagian 3: pengukuran, modul,
   workflow, uji, API, hipotesis, koreksi bernomor.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) dan **`PROMPT_KELANJUTAN.md`** (blob
   `35beed44`) — **arsip; BUKAN sumber** (ADR-A018 kep. 9).

Dasar v17: UKUR v16 (blob **`510addd24bdd7dc04205b622fdda252e69c284f2`**, commit
**`9b01c06ec5f2a58e0c083f4a924515c92475356b`**), dibaca UTUH pada giliran yang sama
sebelum berkas ini ditulis (aturan 52, pencegahan KC-43).

**Apa yang v17 bawa, disebut di muka:** v16 mengubah lubang tak dikenal dari angka
menjadi tiga baris bernama. **v17 membawa angka yang membatalkan gambaran yang baru
saja tersusun itu: `bulan_per_simbol["BNXUSDT"] = 51.`** Bukan 48, bukan 50 — **51**,
lebih besar daripada rentang kalender klines simbol itu sendiri. Ia juga membawa
**pembacaan utuh `gerbang_1m.py`** (utang ukur 18 LUNAS) yang menutup satu jalan riset
sekaligus: modul itu **tidak berkeluaran**.

## KESERASIAN VERSI — PULIH PENUH pada v58 / v17 / v17

- `STATE.md` **v58** — blob **`986b138f400bfcd1fcd9f3592f50bef1b12f867c`**, commit
  **`839a0f17b558a6359c9746944c70bcbf9c33e61e`**.
- `STATE_LAMPIRAN_EKOR.md` **v17** — blob **`29981b68314264f7897408f31b08bad91e32d4d8`**,
  commit **`c0877746c3193d1a7ae708d2015d9d1093452627`**.
- `STATE_LAMPIRAN_UKUR.md` **v17** — berkas ini.

Keserasian **PECAH** begitu STATE v58 naik (v58/v16/v16 lalu v58/v17/v16) dan
**dipulihkan oleh berkas ini**. Ketertinggalan yang dicatat STATE v58 dan EKOR v17 —
bahwa berkas ini masih berkepala "milik STATE v57" dan **tidak memuat** R-316, papan
skor **321**, KC-55, usulan aturan 89, kesalahan dokumen butir 16, angka **51** dan
**6**, temuan `gerbang_1m.py` pustaka murni, **Koreksi 14**, maupun aturan 38
ke-57..ke-59 — **LUNAS oleh berkas ini**. **Satu berkas per push tetap MENGIKAT**
(KC-42, KC-43).

**Tentang push berkas ini:** ia di akar repo sehingga menyalakan `ci.yml`. Tidak satu
pun `tests/**` berubah, jadi cacah uji tetap **1377** — ramalan **deterministik**,
**MUDAH**, TIDAK masuk papan skor, TIDAK menambah beruntun aturan 57. **Laporannya
WAJIB dibaca sebelum push akar berikutnya** (aturan 38 ke-60).

**Angka yang TIDAK berubah dari v44/v45/v6/v7** (tidak diulang): taksonomi 9 kelas,
bulan ABSEN 11, H-A013..H-A015, terhenti, SETTLED. Rinciannya di v44 (blob
`d302caff`), v45 (`eb826817`), v6 (`27e59a79`), v7 (`4e7fb65b`).

## KOREKSI KC-41 — BACA SEBELUM MENGUTIP BERKAS INI

Keempat belas koreksi di bawah **tetap dicantumkan** karena semuanya soal dokumen kami
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
Rumusan v10–v12 menyiratkan 839.842.134 bermasalah. **Sirat itu SALAH dan DICABUT.**

| angka | arti | himpunan | satuan |
| --- | --- | --- | --- |
| **839.325.999** | Σ baris parquet **lolos gerbang** | **19.586** simbol-bulan | baris parquet |
| **516.135** | Σ baris **12 parquet karantina** | **12** simbol-bulan | baris parquet |
| **839.842.134** | Σ **seluruh** baris parquet rilis | **19.598** simbol-bulan | baris parquet |

**839.325.999 + 516.135 = 839.842.134** ✅ dan **19.586 + 12 = 19.598** ✅
**Ketiganya BENAR.** **DILARANG** memakai salah satunya **tanpa menyebut penyebutnya**.
Rata 516.135 / 12 = **43.011** turunan, **bukan bukti**; sebaran 42.585–131.760.

**Koreksi 5 [v10, LUNAS di EKOR v11].** `terisi ≉ 49,7%` → **≈ 49,7%**.

**Koreksi 6 [v11, LUNAS di EKOR v12].** "deretministik" → "deterministik".

**Koreksi 7 [v12, LUNAS di UKUR v12].** "KESERAIAN VERSI" → "KESERASIAN VERSI".

**Koreksi 8 [v12, LUNAS di UKUR v12].** Penanda tebal tak berpasangan. Tidak ada angka
yang berubah.

**Koreksi 9 [v13] — SALAH NALAR, bukan salah ketik.** Jurnal 138 §5 butir 2:
*"… maka 839.325.999 adalah cacah baris parquet yang sebenarnya, dan **839.842.134 yang
keliru**…"* **Premisnya benar; kesimpulannya tidak sah.** ADR-A019 kep. 2 mengangkatnya
menjadi **kelas cacat TANPA PENANGKAL**: dari delapan kesalahan dokumen yang diperiksa,
pembacaan ulang menangkap **satu**.

**Koreksi 10 [v14] — TUDUHAN TERLALU LUAS.** Vonis dari sumber: **STATE v54 BEBAS**;
**EKOR v13 lalai atribusi**; **ADR-A019 bersalah ringan**.

**Koreksi 11 [v15, DIPERKUAT v16 — berinduk pada KC-54].** ADR-A019 kep. 9 memuat dua
kekeliruan: (1) poros karantina disebut **"termurah"** padahal manifes **20.533.802 B**;
(2) poros lubang tengah dilabeli **"gugus `2022-05`/`2024-05`"** padahal keenam lubang
tengah berbulan **2022-01** (BTCSTUSDT) dan **2025-07..2025-11** (LITUSDT). Label
`2022-05` sebenarnya **`bulan_klines_pertama` BNXUSDT**. **Butir 2 = KC-54 kejadian
PERTAMA.**

**Koreksi 12 [v15] — KLAIM KEBARUAN DIPERSEMPIT.** **880 / 877 / 3** sudah tertulis di
STATE v55; yang baru hanya **letak** selisih 3 (seluruhnya kelas AWAL). *"KC-19 dalam
bentuk halus: mengumumkan sebagai baru apa yang sudah tertulis di dokumen sendiri."*

**Koreksi 13 [v16] — TAFSIR `lubang_tak_dikenal` DICABUT (ADR-A021 kep. 2).** Bacaan
"lubang di luar penyebut = bulan sebelum simbol lahir" **DICABUT**: dari tiga lubang
BNXUSDT, hanya **2022-04** yang mendahului `bulan_klines_pertama`; **2022-06 dan
2022-08 duduk DI DALAM** rentang klines. **KC-54 kejadian KEDUA.**

### **Koreksi 14 [BARU v17] — `bulan_per_simbol` dibaca sebagai DAFTAR, isinya CACAH**

Praregistrasi R-316 (jurnal 146 §5) memilih `reports/semesta_bulan_1m.json` sebagai
bahan dan menulis butir 1 yang menanyakan **kehadiran dua bulan bernama**. Pembacaan
utuh membuktikan berkas itu **tidak memuat satu nama bulan pun**, untuk simbol mana
pun: nilai `bulan_per_simbol` adalah **satu bilangan bulat per simbol**.

**KC-54 kejadian KETIGA — tiga kejadian dalam tiga giliran akar berturut.**

| kejadian | medan | dibaca sebagai | sebenarnya |
| --- | --- | --- | --- |
| 1 (Koreksi 11 butir 2) | label gugus `2022-05` / `2024-05` | bulan lubang tengah | `bulan_klines_pertama` BNXUSDT |
| 2 (Koreksi 13) | `lubang_tak_dikenal` | posisi **waktu** lubang | kegagalan pasangan terhadap penyebut 19.586 |
| **3 (Koreksi 14)** | **`bulan_per_simbol`** | **daftar bulan** | **cacah bulan** |

**Yang menyelamatkan giliran itu bukan kepandaian melainkan syarat gugur (c) yang
ditulis sebelum berkas dibuka.** Tanpa syarat itu, butir 1 akan disulap menjadi SEPARUH.
**Konsekuensi mengikat:** bila definisi sebuah medan **tidak dapat ditemukan** sebelum
pita dikunci, ramalan atas medan itu **WAJIB** disertai syarat gugur tersurat.

**Bacaan jujur atas Koreksi 4, 9, 10, 11, 12, 13, dan 14 bersama-sama:** cacat yang
bertahan paling lama di riset ini bukan salah hitung, melainkan **tafsir yang terdengar
masuk akal atas angka yang benar** — dan, sejak v15, **label yang terdengar masuk akal
atas medan yang benar**. Tiga kejadian terakhir satu keluarga, dan keluarga itu bernama
**KC-54**.

## BATAS KEKUATAN ATURAN 52 — DIPERSEMPIT, BUKAN DICABUT

> Pembacaan ulang **dokumen sendiri** lemah terhadap penalaran cacat: ia membaca
> kalimat yang sudah diyakini benar. Pembacaan **kode** kuat terhadapnya.

**[v16] Bukti ketiga:** bacaan `lubang_tak_dikenal` bertahan melewati **empat** berkas
akar dan runtuh dalam **satu** pembacaan laporan.
**[v17] Bukti keempat, bentuk baru:** R-316 butir 1 **tidak dapat diadili sama sekali**,
sebab bahannya tidak memuat jenis informasi yang diramalkan. **DILARANG** menulis bahwa
aturan 52 menjaga mutu penalaran **atas dokumen**; yang dijaganya **kesetiaan salinan**.

## [BARU v17] SEMESTA BULAN 1M — angka 51 dan apa yang TIDAK dikatakannya

Sumber: **`reports/semesta_bulan_1m.json`**, blob
**`a1a6d3f0f13dd7100a91853cadfcaa9a5620fee3`**, **18.884 B**, `waktu_utc`
**2026-07-28T09:44:48Z**. **TERBACA UTUH, tanpa pemotongan alat.**

**Struktur, disalin apa adanya:** dua kunci tingkat atas — `bulan_per_simbol` (peta nama
simbol → **satu bilangan bulat**) dan `waktu_utc`. Tidak ada kunci lain, **tidak ada nama
bulan**. **Cacah entri peta TIDAK dihitung tangan; DILARANG dikutip terukur** (aturan 66).

| medan | nilai |
| --- | --- |
| `bulan_per_simbol["BNXUSDT"]` | **51** |
| `bulan_per_simbol["BNXUSDTSETTLED"]` | **6** |

### Tiga angka bersaing untuk satu simbol — semuanya benar (KC-52 termurni)

| angka | medan / asal | satuan |
| --- | --- | --- |
| **48** | `cacah_bulan_klines_simbol`, `silang_funding.json` | bulan klines di penyebut |
| **50** | rentang kalender 2022-05..2026-06 (**TURUNAN**) | bulan kalender |
| **51** | `bulan_per_simbol`, semesta 1m | bulan berberkas 1m |

**51 − 48 = 3**, dan `cacah_lubang_tak_dikenal` juga **3**.

**CATATAN KESERAMPAKAN yang WAJIB disebut setiap kali kedua angka dibandingkan:** bahan
ini lahir **2026-07-28T09:44:48Z**, `silang_funding.json` lahir **2026-07-29T08:17:55Z**
— selisih hampir **23 jam**. **Keduanya bukan pengukuran serempak.**

### Yang DILARANG disimpulkan

1. **DILARANG** menyatakan tiga bulan selisih itu **adalah** 2022-04 / 2022-06 /
   2022-08. **Kesamaan cacah bukan kesamaan identitas** — berbentuk sama persis dengan
   bacaan yang dicabut Koreksi 13.
2. **DILARANG** menyatakan gerbang menjatuhkan bulan mana pun (lihat bagian berikut).
3. **DILARANG** menyatakan 51 mencakup 2022-04. Belum diukur.
4. **DILARANG** menyamakan "tidak ada di penyebut" dengan "dijatuhkan gerbang".
5. **Aturan 36 TIDAK diberi kasus keempat** oleh kesamaan 3 = 3: dua laporan berjarak
   23 jam yang belum terbukti mengukur himpunan sama. Memasukkannya = KC-38.

### Adjudikasi R-316 — FINAL

| butir | ramalan | terukur | vonis |
| --- | --- | --- | --- |
| 1 | 2022-06 dan 2022-08 tidak hadir | **mustahil dinilai** | **TIDAK TERADJUDIKASI** (syarat gugur (c)) |
| 2 | cacah bulan BNXUSDT = **48** | **51** | **MELESET** (+3) |
| 3 [TURUNAN] | cacah **< 50** | **51** | **MELESET** (pita cacat → KC-55) |
| 4 (MUDAH) | berkas terbaca utuh | terbaca utuh | tidak masuk lajur |

Papan skor **321**, disahkan di EKOR v17. **Kemenangan harfiah butir 3 DITOLAK sendiri**
di jurnal 147; penolakan itu **FINAL**.

## [BARU v17] `gerbang_1m.py` — DIBACA UTUH, utang ukur 18 LUNAS

Blob **`c8cc54c84a57173ef2e426c317d6ac50734e9b4a`**. Modul menyatakan dirinya penerapan
**ADR-A004 §2**.

**Enam klausa `KLAUSA`:** `deret_tidak_kosong` (baris > 0) · `tanpa_duplikat`
(duplikat == 0) · `tanpa_menit_hilang` (`menit_hilang_dalam_rentang` == 0) ·
`jarak_60_detik` · `selaras_menit` · `satuan_milidetik`.
`nilai_deret` → `lolos = not pelanggaran` — **satu klausa gagal cukup menjatuhkan**.

Tetapan: `MS_BAWAH=1_000_000_000_000`, `MS_ATAS=100_000_000_000_000`.
`sidik_kode()` mencap **dua** berkas: `gerbang_1m.py` + `resample.py` (`66a4b177`).

Rumus yang wajib dikutip persis:
`rentang = (unik[-1] - unik[0]) // MS_MENIT + 1`;
`menit_hilang_dalam_rentang = rentang - len(unik)`
— dihitung **dari rentang yang ada di berkas**, **bukan** dari panjang bulan kalender.
Rumus itu **DISALIN**, bukan diimpor dari `diagnosa_kc6.celah_menit` (aturan 10);
penjaganya `tests/test_gerbang_1m.py`. Docstring **mengaku nilainya dapat negatif** dan
sengaja tidak ditambal.

Fungsi lain: `persen` · `satuan_stempel_dari_besaran` · `ukur_deret` · `nilai_klausa` ·
`ringkas_gerbang` (medan `simbol_bulan_dinilai`/`lolos`/`gagal`, `persen_lolos`,
`pelanggaran_per_klausa`, `baris_diperiksa`, `slot_diperiksa`, `contoh_gagal` maks 10).

**TEMUAN STRUKTURAL YANG MENGIKAT.** Modul ini **PUSTAKA MURNI** — tanpa `KELUARAN`,
tanpa `jalankan`/`main`, **tidak menulis laporan apa pun**, tidak menyentuh jaringan
(aturan 13). Maka:

> **Pertanyaan poros tentang gerbang TIDAK dapat dijawab dari keluaran gerbang, sebab
> tidak ada keluaran.** Ia harus lewat laporan **modul pemanggil**.

**Tidak ada satu medan pun di repo yang saat ini menamai klausa pelanggaran per
simbol-bulan.** Menyebut salah satu dari enam klausa sebagai penyebab hilangnya sebuah
bulan adalah **KC-54 yang diulang**.

**Catatan pembeda:** `gerbang_1m.py` **tidak memuat praregistrasi R apa pun** di
docstring-nya — berbeda dari `lubang_tengah.py` yang memuat enam. Aturan 86 (b) karena
itu tidak menghasilkan apa-apa untuk poros ini.

## SILANG FUNDING — tiga lubang tak dikenal (tidak berubah dari v16)

Sumber: **`reports/silang_funding.json`**, blob
**`b61fe8b3bcabbfce435dd5e5f78fc367f6bef617`**, `waktu_utc` **2026-07-29T08:17:55Z**.

**BATAS ALAT YANG WAJIB DISEBUT SETIAP KALI LAPORAN INI DIKUTIP.** Verbatim:
`This result has been truncated (showing 54% of full).` Bagian tengah larik
**`baris_mati`** TIDAK TERLIHAT → **cacah total `baris_mati` DILARANG diklaim terukur**
(utang verifikasi 39, utang ukur 17). Medan agregat di bawah terbaca penuh.

| # | simbol | bulan | di dalam rentang klines? |
| --- | --- | --- | --- |
| 1 | **BNXUSDT** | **2022-04** | **TIDAK** |
| 2 | **BNXUSDT** | **2022-06** | **YA** |
| 3 | **BNXUSDT** | **2022-08** | **YA** |

`bulan_klines_pertama` **2022-05** · `bulan_klines_terakhir` **2026-06** ·
`cacah_bulan_klines_simbol` **48**.

| jalur | susunan | jumlah |
| --- | --- | --- |
| bentuk | 45 awal + 826 ekor + 0 seluruh + 6 tengah | **877** |
| tabel silang | 33 HIDUP + 842 MATI + 2 SEPI + 0 TAK_TERUKUR | **877** |
| terbitan funding | 48 awal + 826 ekor + 6 tengah | **880** |

**877 + 3 = 880** ✅ Kedua jalur menuju 877 lahir dari laporan yang sama — **aturan 36,
bukan dua pengukuran bebas**.

| medan | nilai |
| --- | --- |
| `penyebut_kehidupan` / `cacah_baris_dengan_medan` | **19.586** / **19.586** |
| `bulan_klines_funding` | **19.598** |
| `cacah_lubang_funding` / `cacah_lubang_tak_dikenal` | **880** / **3** |
| `cacah_mati` | **1.401** (kohort **456** + luar kohort **945**) |
| luar kohort berlubang / berfunding | **386** / **559** |
| `bagian_mati_luar_kohort_dengan_lubang_funding` | **0,4085** |
| `cacah_hidup_tanpa_funding` | **33** |
| `tabel_silang` | HIDUP 18.054 / 33 · MATI 559 / 842 · SEPI 96 / 2 · TAK_TERUKUR 0 / 0 |
| semua `selisih_*` · `kendali_sah` · `sidik_seragam` · `laporan_hilang` | **0** · true · true · [] |

**Kelima simbol `cacah_hidup_tanpa_funding` 33, semuanya kelas AWAL:** BNXUSDT **7** ·
ICPUSDT **13** · JUPUSDT **1** · QTUMUSDT **1** · TLMUSDT **11**. 7+13+1+1+11 = **33** ✅

**Ketertutupan tabel silang:** 18.054 + 33 = **18.087** ✅ · 559 + 842 = **1.401** ✅ ·
96 + 2 = **98** ✅ · jumlah **19.586** ✅

Sidik: `sidik_kode` **`8a9b859c09cd64e30e203e6f8dc53411b8e341c44f112805b3041e5d4d3231b1`** ·
`sidik_data_funding` **`2c9fbd1b04f74c9c844bc223a99a103d12220b88d08667b3792720e5b9608d24`** ·
**`sidik_kode_funding` `d38548236f03314eaa648f64f73be5af2f682207be750a2c2fa413fad581513a`** ·
`sidik_kode_laporan` **`24b6bb265525e81c2e571b46e401f36903383f1e3738c487850861adc3e8c595`**.

### Adjudikasi R-315 — FINAL, DILARANG DIADILI ULANG

Butir 1 **TEPAT** (**1**, BNXUSDT) · butir 2 **MELESET** (**1 dari 3**) · butir 3 MUDAH,
tidak diskor. **DILARANG ditulis ulang sebagai SEPARUH.** Syarat gugur (e) MENYALA.

## KC-18 — semesta kehidupan (dikonfirmasi ulang oleh R-307..R-316)

Atas **19.586** simbol-bulan lolos gerbang: **1.401 MATI** (7,153%), **98 SEPI**,
**18.087 HIDUP**. Dari 1.401 MATI: 842 kehilangan funding, 559 tetap berfunding.
`cacah_simbol_tanpa_hidup` **18**. `cacah_lain` = 0 pada kelima modul.
18.087 + 98 = 18.185, + 1.401 = **19.586** ✅

**Pembelahan [v9]:** **787** bulan PERTAMA + **18.799** bukan-pertama = 19.586 ✅
**Pembelahan MATI [v10]:** 1.392 penuh + **9** tak penuh = 1.401 ✅
**Pembelahan [v11]:** 18.799 − 1.401 = **17.398**; 17.284 penuh + **114** berdefisit ✅
(114 = HIDUP 111 · SEPI 3 · MATI 0)
**Pembelahan [v13]:** rilis parquet **19.598** = 19.586 lolos + **12** karantina;
sebabnya terukur dari kode: `kehidupan_arsip.peta_parquet` **melewatkan baris
`parquet_karantina`**.

**Pembelahan ketiga atas lubang funding:**

| kelas bentuk | seluruh semesta | di dalam penyebut | selisih |
| --- | --- | --- | --- |
| awal | **48** | **45** | **3** |
| ekor | **826** | **826** | 0 |
| tengah | **6** | **6** | 0 |
| **jumlah** | **880** | **877** | **3** |

Seluruh selisih 3 di kelas **AWAL**, ketiganya BNXUSDT dan bernama.

**[v17] PERINGATAN BARU atas seluruh bagian ini:** angka **19.586** adalah penyebut
**lolos gerbang**. Semesta 1m **bukan** himpunan yang sama — BNXUSDT sendiri punya
**51** bulan 1m lawan **48** di penyebut. **Berapa besar selisih itu untuk simbol lain
BELUM DIUKUR dan DILARANG DITAKSIR.**

## LUBANG TENGAH — POROS TUNTAS (tidak berubah)

Sumber: **`reports/lubang_tengah.json`**, blob
**`39cd1caacedc4d49ba23c91c80f553bb9fb135a6`**, **11.014 B**, dibaca UTUH.
`waktu_utc` **2026-07-29T09:38:52Z**. `versi_lubang_tengah` **2** · `versi_funding` **6**.

`cacah_lubang_tengah` **6** · `selisih_lubang_tengah` **0** · `cacah_lubang_ganda` /
`cacah_kunci_ganda` **0** / **0** · `cacah_laporan_dibaca` **8** ·
`cacah_per_simbol_funding` **787** · sebaran {HIDUP 0 · MATI **6** · SEPI 0 ·
TAK_TERUKUR 0} · `h_a010_menang` true (5–0) · `h_a011_menang` true, `cacah_bulan` **6**,
`cacah_hidup` **6**. Sidik
**`c9372bd763b86cfeb2adcf0a0c0c43dae8d9aa9a6508e9c32f7671d5ec7b3f4e`**.

| # | simbol | bulan | status | byte_parquet | `cacah_lilin` |
| --- | --- | --- | --- | --- | --- |
| 1 | **BTCSTUSDT** | **2022-01** | MATI | 399.757 | 44.640 |
| 2 | **LITUSDT** | **2025-07** | MATI | 427.922 | 44.640 |
| 3 | **LITUSDT** | **2025-08** | MATI | 427.505 | 44.640 |
| 4 | **LITUSDT** | **2025-09** | MATI | 392.233 | 43.200 |
| 5 | **LITUSDT** | **2025-10** | MATI | 434.201 | 44.640 |
| 6 | **LITUSDT** | **2025-11** | MATI | 389.479 | 43.200 |

BTCSTUSDT rentetan **1**, tetangga 2021-12 → 2022-02, klines pertama **2021-03**, **64**
bulan. LITUSDT rentetan **5**, tetangga 2025-06 → 2026-01, klines pertama **2021-02**,
**64** bulan. **TIDAK SATU PUN berbulan `2022-05` atau `2024-05`.**

**H-A011** — LITUSDT 2026-01..2026-06 keenamnya HIDUP sesudah lima bulan MATI.
Generalisasi **DILARANG** (KC-47); sebab **DILARANG**.

**H-A010 MENANG 5–0:**

| simbol | rentang lubang awal | `cacah_bulan_klines` | `cacah_lubang` |
| --- | --- | --- | --- |
| BNXUSDT | 2022-05 → 2023-02 | 48 | 19 |
| ICPUSDT | 2021-05 → 2022-09 | 62 | 16 |
| JUPUSDT | 2024-01 → 2024-02 | 30 | 1 |
| QTUMUSDT | 2020-02 → 2020-03 | 77 | 1 |
| TLMUSDT | 2021-07 → 2023-03 | 60 | 20 |

**[v17] CATATAN SILANG YANG WAJIB DITAHAN, kini BERLIPAT.** Baris BNXUSDT pada tabel ini
— `cacah_bulan_klines` **48**, rentang mulai **2022-05** — adalah medan yang **sama**
yang: (a) di UKUR v15 berpindah menjadi nama poros "gugus 2022-05" (Koreksi 11 butir 2);
(b) di v16 menutup jembatan 50 lawan 48; **(c) di v17 dibantah oleh angka 51 dari semesta
1m.** Satu medan, **empat** pemakaian, **dua** di antaranya keliru sebelum diukur, dan
yang keempat memperlihatkan medan itu **tidak pernah mengukur seluruh bulan simbolnya**.

Kendali: tiga baris **BTCUSDT** (2021-05, 2021-08, 2021-01) semuanya HIDUP dengan
`funding_ada` true. Sumber: `reports/funding_semesta.json` +
`reports/kehidupan_arsip_0..7.json`.

**Uji H-A020 dan H-A021 MUSTAHIL** — bukan mahal, bukan tertunda, **tidak ada bahannya**.

## VONIS `ukur_kolom` [v13] — dasar runtuhnya R-312

Dari `kehidupan_arsip.py` (blob `318a5cb1`): **`cacah_lilin` = `n`** dari
`pq.ParquetFile(...).metadata.num_rows`; **`cacah_lilin_terbaca`** = baris yang KEDUA
kolomnya (`volume`, `trades`) terurai; identitas paksa
`cacah_lilin = cacah_lilin_terbaca + cacah_baris_cacat`. **Bukan dua pengukuran bebas.**
`cacah_berselisih` = 0 pada 19.586 memaksa **`cacah_baris_cacat` = 0 di seluruh semesta**.

## ARAH SELISIH R-312 MUSTAHIL [v14, tetap]

Docstring `selisih_lilin.py`: `selisih = cacah_lilin_terbaca − cacah_lilin`, dipilih agar
POSITIF. Identitas `ukur_kolom` memaksa `cacah_lilin_terbaca` ≤ `cacah_lilin` pada setiap
baris → **butir 2 R-312 tidak dapat dimenangkan secara struktural**.

## SISA DEFISIT [v11, tetap]

| besaran | nilai |
| --- | --- |
| `cacah_calon` | **17.398** |
| `cacah_calon_penuh` | **17.284** |
| **`cacah_berdefisit`** | **114** (0,66%) |
| `defisit_calon` | **712.925** |
| rata per baris berdefisit | **6.254** |
| `defisit_teratas` (sepuluh) | **291.379** |
| **`bagian_teratas`** | **0,4087** |
| `defisit_terbesar` | **42.510** |
| `selisih_sisa` | **0** |

- **Terbesar: TLMUSDT `2023-03`, HIDUP, 2.130 dari 44.640 lilin — 95,2% KOSONG.**
- Sepuluh teratas tersebar di **TUJUH** bulan → aturan 81 **TIDAK** terpicu.
- ANCUSDT `2022-05` **26.959** lawan LUNAUSDT `2022-05` **26.950** — selisih **sembilan
  lilin**; dasar **H-A021**; **kebetulan angka, bukan bukti**.
- **712.925 DILARANG DISEBUT PENGUKURAN BEBAS** (tautologi 808.162 − 95.237, KC-50).

Sidik `6211624ba9514d604d4dc510abca2e40386775c7aaa1279135f0baf666f044b0`.

## KETERISIAN LILIN [v10, tetap]

`cacah_mati_penuh` / tak penuh **1.392** / **9** · `jumlah_lilin_langsung`
**839.325.999** · `defisit_total` **18.143.601** · `defisit_pertama` **17.335.439**
(95,5%) · `defisit_bukan_pertama` **808.162** (**0,0445**) · baris tanpa lilin / negatif
/ kunci ganda **0** / **0** / **0**.

- **BULAN MATI PENUH DATANYA; YANG NOL ADALAH TRANSAKSINYA** — 1.392 dari 1.401 (99,4%).
- **DILARANG** melanjutkan ke "harga beku" / "lilin datar": `medan_baris_terlihat` **14**
  medan, **tak satu pun harga**.
- Bulan pertama rata kehilangan **22.027** lilin; keterisian **≈49,7%**, bersesuaian
  dengan nisbah byte 0,527179.

**Kesembilan baris MATI tak penuh, LENGKAP** (semuanya `pertama: false`):

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

Jumlah **95.237** = **0,1178** dari 808.162; 808.162 − 95.237 = **712.925**.
**TUJUH dari sembilan berbulan `2024-05`, jendela SEMBILAN lilin** → KC-47, aturan 81,
**H-A020**. **Kalimat "tujuh simbol didelisting 28 Mei 2024" DILARANG.**

Sidik `1cd98f4fa22c24b30f31f5b36dac0ea0bb3fa9de44e5e15ae73cbf11cdca08bb`.

## IRISAN BULAN PERTAMA [v9, tetap]

Definisi "bulan pertama": bulan TERKECIL milik simbol **di dalam penyebut 19.586** —
**bukan** bulan pertama simbol itu di bursa. Perbedaan keduanya BELUM diukur (ADR-A016
kep. 6). **[v17] Angka 51 memperkuat mengapa utang ini penting.**

`cacah_hidup_kecil_sebagian` **37** dari 38 (0,973684) · `cacah_pertama` /
`cacah_bukan_pertama` **787** / **18.799** · `rata_byte_pertama` **897.374,517** ·
`rata_byte_bukan_pertama` **1.702.219,726** · `nisbah_rata` **0,527179**.

**Irisan NYATA tetapi ASIMETRIS TAJAM:** 37 dari 38 berkas kecil adalah bulan pertama
(**97,4%**); hanya 37 dari 787 bulan pertama yang berkas kecil (**±4,7%**). Satu lawan
tersisa: **TLMUSDT 2023-03 (80.394 byte)**.

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
72.819 (tepi)** · **TLMUSDT 2023-03 80.394** · AMBUSDT 2023-03 81.419 · **TQQQUSDT
2026-06 82.330 (tepi)** · **MVLLUSDT 2026-06 86.126 (tepi)** · LEVERUSDT 2023-03
89.724 · INXUSDT 2026-01 94.575 · ENJUSDT 2020-09 94.658.

Sidik `0d3530f69ad51a22e038c17616411b56e4518698ff14c9b635131ec1e2a66562`.

## LEBAR ZONA IRISAN BYTE [v8, tetap]

`cacah_hidup_byte_kecil` (< **97.634**) **38** · `cacah_mati_byte_kecil` (< **150.000**)
**2**. **Zona 22.440–97.634 byte berisi 38 HIDUP dan NOL MATI.**

| kelas | cacah | byte | byte_min | byte_maks | byte_rata |
| --- | --- | --- | --- | --- | --- |
| HIDUP | 18.087 | 32.049.492.952 | **22.440** | 2.770.666 | 1.771.962,899 |
| SEPI | 98 | 77.728.024 | 259.327 | 1.231.408 | 793.143,102 |
| MATI | 1.401 | 579.041.399 | **97.634** | 451.875 | 413.305,781 |

`total_byte` **32.706.262.375**. Sembilan medan selisih nol tetapi hanya **DELAPAN
bebas** — "sembilan pemeriksaan bebas" **DILARANG** (KC-50).
Sidik `0e7103ef46a37d1e442d8e7fc5b9771b1ef7cdc3956ea57d584d84f6f73ea2c6`.

## BYTE PARQUET SEMESTA [v7] dan ARAH WAKTU KEMATIAN [v6]

Total byte **32.706.262.375**; `bagian_byte_mati` **0,017704297493883234**;
`cacah_terukur_byte_kecil` (< 10.000) **0**; `cacah_byte_nol` **0** → **dasar keras
≈22 KB** (KC-48). Sidik `e02aca2b…883c7`.

`lubang_tebing` V1, penyebut **118**: `mati_dulu` **40** (**0,339**) · `serempak` **78**
(DILARANG di numerator) · `lubang_dulu` **0**. `cacah_tebing_butir_2` **39** (`2025-07`);
**39 dari 40** `mati_dulu` di tebing; satu-satunya bukan-tebing **BTCSTUSDT** → KC-47.
**Keserian tebing `2025-07` dengan lubang LITUSDT BELUM diukur dan DILARANG diklaim.**
Sidik `4a5c2e42…18bf3`.

## Lubang funding — agregat semesta (tetap)

`cacah_simbol_ada_lubang` **122** dari 787 · awal **5** · bukan-awal **118**. BNXUSDT
punya lubang AWAL dan bukan-awal sekaligus. Lima bentuk AWAL: BNXUSDT, ICPUSDT,
JUPUSDT, QTUMUSDT, TLMUSDT. Lubang **880** semesta / **877** dalam penyebut / **3** tak
dikenal. Dari 945 MATI di luar kohort: **386** kehilangan funding, **559** berfunding.

## Jumlah uji — terukur

**1377, kini LIMA BELAS bacaan berjejak di berkas ini.** Sembilan pertama tercatat di
v16 dan tidak diulang; yang terbaru:

10. blob **`340c3c7f425d49859e6ae659cca38d0ee7770aaa`**, run **30585269231**, commit
    **`d551f471`** (UKUR v15), 21:55:58Z, kode 0, `… in 0.60s`.
11. blob **`8ea8cc463ff58246b363e47458e9355d26a5ea79`**, run **30587658376**, commit
    **`ebe6f373`** (STATE v57), 22:36:15Z, kode 0, **`… in 0.40s`** — tercepat.
12. blob **`34f88b3744e4d9733a731f3f97056584344ddc33`**, run **30588460935**, commit
    **`32413935`** (EKOR v16), 22:49:39Z, kode 0, `… in 0.61s`.
13. **[v17]** blob **`5b433a93a3f0d3bb2cded75a5c0379c4a557ae3d`**, run **30589452976**,
    commit **`9b01c06e`** (UKUR v16), **23:07:02Z**, kode 0, `… in 0.55s`.
14. **[v17]** blob **`9718bf98caafc59349465ff55b9755e4ea309ac3`**, run **30590593816**,
    commit **`839a0f17`** (STATE v58), **23:28:30Z**, kode 0, `… in 0.61s`.
15. **[v17]** blob **`5f62452da6ba9e52f1324f796b2dbb552332c8bc`**, run **30590948580**,
    commit **`c0877746c3193d1a7ae708d2015d9d1093452627`** (EKOR v17),
    **2026-07-30T23:35:07Z**, kode 0, `1377 tests collected in 0.49s`.

Turunan: 1341 + **36** butir `tests/test_selisih_lilin.py` = **1377** ✅
**Rentang waktu kutip 0,40s–0,67s DILARANG dibaca sebagai pengukuran apa pun tentang
repo** — ia keadaan mesin CI, bukan besaran riset.

Riwayat: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 → 984 →
1044 → 1100 → 1168 → 1233 → 1297 → 1341 (enam run) → **1377** (lima belas run berjejak).

**Aturan 57: beruntun 4 dari 4** sesudah PUTUS di 26/27. Ia **mencacah, bukan menaksir**.

### Aturan 38 — ordinal, kini sampai ke-59

| ke- | CI | run | commit | blob | jejak |
| --- | --- | --- | --- | --- | --- |
| 53 | 1377 | 30584737431 | `94c7d9da` | `5f4282f6` | UKUR v15 |
| 54 | 1377 | 30585269231 | `d551f471` | `340c3c7f` | jurnal 144, STATE v57 |
| 55 | 1377 | 30587658376 | `ebe6f373` | `8ea8cc46` | EKOR v16 |
| 56 | 1377 | 30588460935 | `32413935` | `34f88b37` | UKUR v16 |
| 57 | 1377 | 30589452976 | `9b01c06e` | `5b433a93` | jurnal 146, STATE v58 |
| 58 | 1377 | 30590593816 | `839a0f17` | `9718bf98` | EKOR v17 |
| **59** | **1377** | **30590948580** | **`c0877746c3193d1a7ae708d2015d9d1093452627`** | **`5f62452da6ba9e52f1324f796b2dbb552332c8bc`** | **berkas ini** |

**Pemakaian berjalan = ke-lima puluh sembilan.** Ke-59 dibaca **2026-07-30T23:35:07Z**,
kode keluar **0**, atas push EKOR v17 — **dibaca sebelum tertimpa**.

**[v17] SEMBILAN BELAS pembacaan berturut (ke-42..ke-59) tanpa satu pun laporan hangus.**

**[v17] JEBAKAN YANG TERBUKTI NYATA.** Sesudah push STATE v58, pembacaan pertama
mengembalikan blob `5b433a93` dengan `commit` `9b01c06e` — **laporan ke-57 yang lama**,
karena bot belum menerbitkan. Ia **tidak dicatat** sebagai ke-58. **Laporan sah hanya
bila medan `commit` cocok dengan commit push yang baru.**

**Bot CI** menambah satu commit di atas tiap push pemicu — deterministik, **DILARANG
dihitung kemenangan**. Yang terlihat pada rangkaian ini: `ff89f688` (STATE v57) ·
`47769b18` (EKOR v16) · `e271a711` (STATE v58) · `14f3316e` (EKOR v17).

**Dua cacat tetap disebut:** ke-**38** (run `30541051907`, commit `5d7d8b96`) **tanpa
blob**; run **30547842823** (bot `de2fc03d`) **tidak pernah dibaca**, tertimpa,
**DILARANG dihitung**.

## Modul, workflow, dan berkas uji

**CACAH TANGAN yang sah** (aturan 66), ref **`3196fd98`** dan **`8a614567`**:
`lux_ai/serapan/` **49** · `tests/` **53** · `.github/workflows/` **44** · akar **18**
(6 direktori + 12 berkas). **50 / 54 / 45 TURUNAN dan DILARANG dikutip terukur.**

**PERINGATAN DUA CACAH `tests/`:** repo WARISAN **34**, repo riset ini **53**.
**Menyebut "cacah uji" tanpa menyebut repo-nya DILARANG.**

**Peringatan dini aturan 48:** `silang_funding.py` **29.873 B / 705 baris** (sisa **95**)
· `funding.py` **28.121** · `sisa_defisit.py` **25.949** · `semesta_kuota.py` **24.987**
· `lubang_tengah.py` V2 **23.745**.

**Blob modul — [v17] `gerbang_1m.py` kini DIBACA UTUH:**
`gerbang_1m.py` **`c8cc54c84a57173ef2e426c317d6ac50734e9b4a` (DIBACA UTUH, pustaka
murni)** · `resample.py` `66a4b177` (ikut dicap `sidik_kode` gerbang) ·
`silang_funding.py` V2 `42c3aa9dc2c16220b79cf9c9e46979dd000fd393` (DIBACA UTUH) ·
`lubang_tengah.py` V2 `4d3beaf18c070d2931044c50dd5a354d75eaceb8` (DIBACA UTUH) ·
`kehidupan_arsip.py` `318a5cb187406d16cfd3385d653bed905f632934` (DIBACA UTUH) ·
`pulihkan.py` `a9e6eab7cc47555dfed919ac63044ff2eadc4893` (DIBACA UTUH) ·
`ukur_baris.py` V5 `3ebaa9f9` (DIBACA UTUH) · `selisih_lilin.py`
`d19bdb5fe67e0bd9c1b141d7fb7cc6dcd089c5f2` · `sisa_defisit.py` `7aa0e6d7` ·
`keterisian_lilin.py` `3f80ffa7` · `bulan_pertama.py` `b9bd00ac` · `irisan_byte.py`
`2dbe3d55` · `byte_semesta.py` `ff68e4be` · `lubang_tebing.py` `575e777e` ·
`lubang_awal.py` `8c36943d` · `kohort_ekor.py` V4 `c9b63bbe` · `bentangan_kohort.py` V2
`f4eae57a` · `sebab_bangkit.py` `fd5a1dc4` · `tersisip_semesta.py` `8a648838` ·
`kehidupan.py` `f49abb2b` · `funding.py` `8d4b1f82` · `rilis.py` `2e44530c` ·
`karantina_semesta.py` `46e7c46b` · `arsip.py` `0104958b` · `semesta_kuota.py`
`7288b030` · `bulan_absen.py` `10279d72` · `kebangkitan.py` `446321ee` ·
`penyebut_tahun.py` `265aad00` · `anatomi_tengah.py` `04279335` · `__init__.py`
`64d85584`.

`ci.yml` = **`c79497b2c812679eaa69aee5b3160eac9f5c5fb7`** (paths-ignore `journal/**`,
`decisions/**`, `hipotesis/**`, `reports/**`; push ke `lux_ai/**`, `tests/**`, `STATE*`,
`PROMPT*` MENYALAKAN CI — **terkonfirmasi sebelas kali berturut**).
`karantina_semesta.yml` = `de40fa4e` (**belum dibaca utuh**).
Trio R-312: `selisih_lilin.yml` `de2fd4fd346c9e13213fcc9a410d4aea8460d67a` ·
`test_selisih_lilin.py` `2d903a4a6f544eacd26b82bdb177680fa78bdffd` (**36** butir).
Trio R-311: `sisa_defisit.py` `7aa0e6d7…` · `test_sisa_defisit.py` `7004115a…` (**44**) ·
`sisa_defisit.yml` `64511207…`. Trio R-310: `test_keterisian_lilin.py` `f58912d0` (64) ·
`keterisian_lilin.yml` `d821c63a`. Trio v9: `test_bulan_pertama.py` `75d87ba2` (65) ·
`bulan_pertama.yml` `2242e3e4`. `test_irisan_byte.py` `b6389051` (68) · `irisan_byte.yml`
`7d98a267`.

Cacah per berkas uji — **repo riset ini**: `test_irisan_byte.py` **68** ·
`test_bulan_pertama.py` **65** · `test_keterisian_lilin.py` **64** ·
`test_bentangan_kohort.py` V2 **63** · `test_lubang_tebing.py` **60** ·
`test_sebab_bangkit.py` **57** · `test_byte_semesta.py` **56** · `test_lubang_awal.py`
**48** · `test_tersisip_semesta.py` **47** · `test_anatomi_tengah.py` **47** ·
`test_sisa_defisit.py` **44** · `test_selisih_lilin.py` **36** · `test_terhenti.py` V4
**33** · `test_bulan_absen.py` **32** · `test_karantina_semesta.py` **28** ·
`test_silang_settled.py` **24** · `test_ukur_baris.py` **3**.
**`tests/test_lubang_tengah.py` — 56 butir menurut R-228, BELUM DIBACA, DILARANG dikutip
terukur.**
**[v17] `tests/test_gerbang_1m.py` — penjaga penyimpangan salinan rumus
`menit_hilang_dalam_rentang`. BELUM DIBACA; cacah butirnya TIDAK DIKETAHUI.**

**POLA WORKFLOW TRIO — TERVERIFIKASI DARI SUMBER** (`selisih_lilin.yml`): `name`,
`on.push.paths` **SATU** entri, `permissions: contents: write`, job `ukur` di
`ubuntu-latest`, checkout@v4 + setup-python@v5 (3.11),
`pip install numpy pandas pyarrow pyyaml`, langkah `jalan` dengan `set +e` → `KODE=$?` →
`echo "kode=$KODE" >> "$GITHUB_OUTPUT"` → `exit 0`, langkah `catat status`, langkah
`dorong laporan` (`[skip ci]`, `git pull --rebase`), penutup
`exit ${{ steps.jalan.outputs.kode }}`. **Aturan 55 LUNAS untuk berkas itu.**

## API terverifikasi

API lama (v37–v12) tetap berlaku. **[v17] Tambahan: `gerbang_1m` (lihat bagian
tersendiri di atas) — satu-satunya pembacaan kode baru pada versi ini.**

**`lubang_tengah` V2** (`4d3beaf1…`, 23.745 B): `VERSI=2` ·
`KELUARAN="reports/lubang_tengah.json"` · `TENGAH_TERCATAT=6` · `SIMBOL_H_A010` lima
nama · `SIMBOL_TENGAH_TERCATAT=["BTCSTUSDT","LITUSDT"]` · `SIMBOL_H_A011="LITUSDT"` ·
`RENTANG_H_A011=("2026-01","2026-06")` · `BERKAS_DICAP` empat nama. **Enam belas
fungsi**; **lima penggugur**; **enam praregistrasi di docstring** (R-221/222/223 TEPAT;
R-229 TEPAT; R-230 MELESET; R-228 belum diadjudikasi).

**`pulihkan` V2** (`a9e6eab7…`, 14.839 B): `VERSI=2`, `TOTAL_PECAHAN=8`,
`AKAR_UNDUH="data/unduh"`, `AKAR_PULIH="data/pulih"`; `sidik_kode()` mencap
`["pulihkan.py","rilis.py"]`; **`cacah_baris_parquet` = `metadata.num_rows`**;
`periksa_keluarga` dipanggil **dua kali** (`rilis` dan **`rilis_karantina`**).

**`kehidupan_arsip` V1** (`318a5cb1…`, 19.281 B): `VERSI=1`, `TOTAL_PECAHAN=8`,
`KENDALI_CACAH=3`, `KOLOM_VOLUME="volume"`, `KOLOM_TRANSAKSI="trades"`;
`peta_parquet` **melewatkan baris `parquet_karantina`**.
**[v17] Keluarannya `reports/kehidupan_arsip_<i>.json` berukuran 991.422–1.261.637 B —
MUSTAHIL dibaca utuh lewat alat. DICORET dari daftar bahan ramalan.**

**`selisih_lilin` V1** (`d19bdb5f…`): `LILIN_LANGSUNG_TERCATAT=839325999` ·
`BARIS_PARQUET_TERCATAT=839842134` · `SELISIH_TERCATAT=516135` ·
`AMBANG_HIDUP_KECIL=97634` · `INVARIAN` **8** kunci · `R312_PITA_BUTIR_1=(12,120)` ·
`R312_PITA_BUTIR_2=(0.50,0.865)`. `kode_keluar` mengembalikan **2** bila
`cacah_berselisih <= 0` — **dirancang**.

**`silang_funding` V2** (`42c3aa9d`): `PENYEBUT_TERCATAT=19586`, `MATI_TERCATAT=1401`,
`KOHORT_TERCATAT=456`, `HIDUP_TANPA_FUNDING_TERCATAT=33`,
**`LUBANG_TAK_DIKENAL_TERCATAT=3`**,
`BENTUK_TERBITAN_FUNDING={"awal":48,"ekor":826,"tengah":6}`, `KENDALI_CACAH=3`.
**PERINGATAN KC-54:** `LUBANG_TAK_DIKENAL_TERCATAT=3` memuat **cacah**, bukan identitas
dan bukan arah waktu. **Kode tidak pernah menjanjikan apa pun tentang waktu;
dokumenlah yang menambahkannya.**

**`keterisian_lilin` V1** (`3f80ffa7`): `INVARIAN` delapan kunci ·
`AMBANG_HIDUP_KECIL=97634` · `MENIT_PER_HARI=1440` · `KENDALI_SIMBOL="BTCUSDT"` ·
`R310_PITA_BUTIR_1=(1,120)` · `R310_PITA_BUTIR_2=(0.02,0.25)`.
**`sisa_defisit` V1** (`7aa0e6d7`): `R311_PITA_BUTIR_1=(200,12000)`,
`R311_PITA_BUTIR_2=(0.02,0.45)`, `DEFISIT_SEMBILAN_TERCATAT=95237`,
`DEFISIT_BUKAN_PERTAMA_TERCATAT=808162`, `SISA_TERCATAT=712925`, `JAWABAN_KENDALI` **17**
medan, `teratas` → **None** bila baris berdefisit < 10.
**`bulan_pertama` V1** (`b9bd00ac`): `R309_PITA_BUTIR_1=(22,38)`,
`R309_PITA_BUTIR_2=(0.10,0.60)`, `BULAN_TEPI="2026-06"`.
**`irisan_byte` V1** (`2dbe3d55`): `AMBANG_HIDUP_KECIL=97634`,
`AMBANG_MATI_KECIL=150000`, `MEDAN_SELISIH` **9** (delapan bebas + satu turunan).
**`bentangan_kohort` V2** (`f4eae57a`): butir 09 menolak `str(tuple)` sebagai kunci;
butir 59–61 memanggil `silang_funding` asli; butir 63 melarang nama kohort tertulis di
dalam modul (aturan 73); butir 37 menuntut `None`, bukan nol.
**`lubang_awal` V1** (`8c36943d`): medan `mati_tidak_setelah_lubang_bukan_awal` memakai
`<=` — **DILARANG dipakai untuk klaim arah** (aturan 80).
**`kohort_ekor` V4** (`c9b63bbe`): `TEBING="2025-07"`, `BULAN_DIHARAPKAN="2026-06"`,
`BATAS_SIMBOL=10`, `PAGU_MUNDUR=60`, `AMBANG_SEPI=0.5`. **Medan
`cacah_simbol_bangkit_dapat_diuji` = 0 DILARANG dibaca sebagai ketiadaan kebangkitan
(KC-53).**
**`ukur_baris` V5** (`3ebaa9f9`): `PAGAR_BARIS=800`, `BERKAS_DIUKUR` **21 nama**.
**Utang V6 hidup.**
**`kehidupan`** (`f49abb2b`): `AMBANG_SEPI=0.5`, `BULAN_MULAI="2025-07"`,
`BULAN_AKHIR="2026-06"`.

Sidik lain: `sebab_bangkit` `bafe4359…221a` · `tersisip_semesta` `9618fd19…c537c` ·
`bentangan_kohort` V2 `8ca6ebbe…f32c` · `lubang_awal` `156499ce…f2362` · `pulihkan` kode
seragam `76c27e3c…62d700`, manifes seragam `237ccf42…ba601`. Sidik manifes per pecahan:
`_0` `88d5704c` · `_1` `64311545` · `_2` `6bbc9990` · `_3` `b6f5f27e` · `_4` `d204f353` ·
`_5` `3b0e2d22` · `_6` `356ae3d6` · `_7` `2abc9c73`.

## Hipotesis

- H-A001 belum diuji · H-A002b GUGUR · H-A003 MENANG pada 3, GUGUR pada 9 · H-A004 tak
  dapat diuji · H-A005 GUGUR · H-A006 MENANG enam run · H-A008 MENANG dua kali · H-A009
  GUGUR · **H-A010 MENANG 5–0** · **H-A011 TERBUKTI** · H-A012 MENANG · H-A013 MENANG
  6–0 TAFSIR DICABUT · H-A014 MENANG 9 dari 9 · H-A015 DIBATASI sebagai tafsir (KC-45) ·
  H-A016 PENGAMATAN, BELUM DIUJI.
- **H-A017** DICABUT sebagai pola semesta; bukti lepas-tebing tinggal **1** simbol.
- **H-A018** — **BOLEH:** "bulan MATI menempati bagian KECIL byte semesta (**0,0177**)
  dan rata sekitar **4,3×** lebih kecil". **DILARANG:** "berkas kecil berarti pasar mati".
- **H-A019** DITERIMA TERBATAS; DILEMAHKAN oleh ADR-A018 kep. 6 tanpa tafsir pengganti.
- **H-A020, H-A021 [DIUSULKAN]** — uji **MUSTAHIL**, tidak ada bahannya.
- **H-A022 [TERBUKTI lewat R-313]** — yang terbukti **identitas himpunan**, bukan sebab
  karantina.
- **[v17] H-A023 [DIUSULKAN, BELUM DIREGISTRASI, TIDAK DISKOR]** — *selisih 51 − 48 = 3
  pada BNXUSDT dan `cacah_lubang_tak_dikenal` = 3 menunjuk himpunan simbol-bulan yang
  sama.* Ujinya menuntut sumber yang menyebut **nama bulan** per simbol; sumber itu
  **belum ditemukan**. Calon: `reports/semesta_rentang.json`
  (`8d5bd06ca4073dac8a8ef7841d81824427cc8e63`, 110.662 B), **belum dibuka**. **Bila
  kelak terbukti, ia TIDAK membuktikan sebab** — ia hanya memindahkan pertanyaan dari
  "bulan mana" ke "mengapa". Hipotesis berikutnya **H-A024**.

## Aturan 87 RESMI; usulan 88 dan 89

**Aturan 87 [RESMI].** Butir ramalan **turunan** wajib ditandai **TURUNAN** pada
praregistrasi; kemenangannya wajib diperkecil sendiri secara tertulis; kekalahannya
dihitung penuh. **[v17] Ditaati:** butir 3 R-316 ditandai TURUNAN di muka dan kalah.

**Usulan aturan 88 [BELUM RESMI].** Ramalan keseragaman tanpa mekanisme tertulis wajib
ditulis sebagai **sebaran**. **[v17] TIDAK mendapat kejadian kedua** — butir 1 R-316
gugur karena bahan, bukan kalah karena keseragaman.

**Usulan aturan 89 [BARU v17, BELUM RESMI].** Setiap pita ramalan atas bilangan wajib
menutup **ketiga sisi** ruang nilainya, atau menyatakan tertulis mengapa satu sisi
mustahil. Satu kejadian (R-316 butir 3 → **KC-55**).

**Catatan kejujuran melekat pada 88 dan 89:** keduanya lahir **sesudah** kekalahan.
**Utang yang dibayar, bukan laba.**

## Praregistrasi R-317 — BELUM ADA

Porosnya **wajib ditulis di jurnal lebih dulu** (aturan 79), pada giliran BERBEDA dari
adjudikasi (ADR-A016). Urutan poros:

1. **BNXUSDT — identitas bulan.** **[v17] Pertanyaan BERUBAH BENTUK:** bukan "mengapa
   dua bulan hilang", melainkan **"bulan mana saja yang dimiliki BNXUSDT pada semesta 1m
   (51), dan mana yang tidak sampai ke penyebut (48)"**. Bahan calon
   `reports/semesta_rentang.json`. **`kehidupan_arsip_*.json` DICORET.** **PERINGKAT
   PERTAMA.**
2. **Sebab kekosongan TLMUSDT 2023-03** (2.130/44.640, 95,2% kosong, HIDUP).
3. **Tebing funding `2025-07`** (39 simbol) **dan BTCSTUSDT**.
4. **Identitas dua belas simbol-bulan karantina** — menuntut **modul CI**; **BUKAN
   kandidat murah**.
5. **"Bulan pertama di penyebut" lawan "bulan pertama di bursa"** — **[v17] naik nilai**
   karena angka 51.
6. Sisanya: selisih 40−38 `diagnosa_kc15`; bentangan 38 kohort; H-A016; `mati_tersisip`;
   R-7/19/20/28/36/37; R-199; R-236..R-247; taksonomi lubang tiga kelas; bagian
   `baris_mati`.

**DUA BELAS SYARAT KUMULATIF sebelum pita R-317 dikunci** (naik dari sebelas): aturan
**79** · **83** · **84** · **85** · **86 (a)** — dengan penyebutan bahwa daftar `reports/`
baru terbaca **76%** · **86 (b)** · **87** · **kebebasan tiap medan diperiksa terhadap
kode** · **KC-50** · **KC-52** · **KC-53** · **KC-54** (definisi medan disalin dari
sumber; bila tak ditemukan, **syarat gugur tersurat WAJIB**) · **KC-55** (pita menutup
ketiga sisi) · aturan **66**.

## Utang ukur yang masih hidup

1. **LUNAS [v14]** — aturan 52 atas trio `c1dc0009`.
2. **`karantina_semesta.yml`** (`de40fa4e`), `test_pulihkan.py` (`11c43533`),
   `test_rilis_karantina.py` (`739c8da9`), `test_karantina_a006.py` (`a5a3d82f`),
   `tests/test_lubang_tengah.py` belum dibaca utuh. **[v17] Ditambah
   `tests/test_gerbang_1m.py`.**
3. **Lima ADR belum dibaca utuh:** A002, **A004 (NAIK PERINGKAT — sumber keenam klausa
   gerbang)**, A006, A007, A008.
4. **Identitas dua belas simbol-bulan karantina** belum didaftar; **20.533.802 B**;
   menuntut modul CI.
5. **LUNAS [v16]** — irisan 880 lawan 877 diukur; ketiga lubang bernama.
6. **"Bulan pertama di penyebut" lawan "bulan pertama di bursa"** belum diukur —
   **[v17] naik nilai** oleh angka 51.
7. **Sebab kekosongan TLMUSDT 2023-03** belum diukur.
8. **Cacah tangan aturan 66 ulang** — 50/54/45 TURUNAN.
9. **`ukur_baris` V6** — `BERKAS_DIUKUR` 21 nama; `silang_funding.py` **705** baris.
10. **Tiga butir `PETA_MODUL.md`** bertanda "memerlukan verifikasi" (repo WARISAN).
11. **`PROMPT_KELANJUTAN.md`** belum berkepala "ARSIP — BUKAN SUMBER"; **`PROMPT.md`
    v55** belum didorong. **Utang berumur delapan versi.**
12. **LUNAS** — ADR-A020 dan ADR-A021 ada dan dibaca utuh.
13. **LUNAS [v17]** — jurnal **146** (`1992c8ef…`, commit `440fe8ba`, praregistrasi
    R-316) dan jurnal **147** (`eaf941f6…`, commit `e429e4fb`, adjudikasi R-316) ada dan
    dibaca utuh. **Digantikan:** jurnal **148** belum ditulis.
14. **LUNAS [v17]** — aturan 38 ke-57, ke-58, dan ke-59 dibaca, blob dicatat.
    **Digantikan:** laporan atas push berkas ini (**ke-60**) wajib dibaca sebelum push
    akar berikutnya.
15. **R-228 belum diadjudikasi**; cacah 56 butir `test_lubang_tengah.py` DILARANG dikutip
    terukur.
16. **Keserian tebing `2025-07`** belum diukur; **DILARANG diklaim**.
17. **Bagian `baris_mati` `silang_funding.json` belum terbaca** (54%). Menuntut **modul
    CI** atau **pembacaan berpotong terancang**. Utang verifikasi **39**.
18. **LUNAS [v17]** — **`gerbang_1m.py` DIBACA UTUH** (`c8cc54c8…`). Hasilnya menutup
    satu jalan: modul itu **tidak berkeluaran**, sehingga poros gerbang **tidak dapat
    dijawab dari keluarannya**.
19. **Prasyarat klasifikasi belum dipenuhi.** Serapan funding **matang sebagai
    pembukuan, belum matang sebagai landasan fitur**: ADR-A003 **belum ada**; irisan 787
    lawan 787 belum diukur (KC-52); **87** "funding tanpa klines" atas 787 belum
    didamaikan; kelas positif **33** dari **lima** simbol (KC-47); taksonomi lubang masih
    **BENTUK, bukan MEKANISME**. **[v17] Blokir kedua MEMBURUK:** kini ada **tiga** angka
    bersaing untuk satu simbol (48 / 50 / 51).
20. **BARU [v17] — identitas 51 bulan 1m BNXUSDT belum diketahui.** Cacahnya terukur,
    nama bulannya tidak. **Memblokir H-A023 dan poros peringkat pertama sekaligus.**
    Utang verifikasi **40**.
21. **BARU [v17] — daftar `reports/` baru terbaca 76%** (ref `8364ad92…`). Keputusan
    bahan diambil hanya dari bagian yang terlihat; **melemahkan aturan 86 (a)** dan wajib
    disebut setiap kali (a) dipakai. Utang verifikasi **41**.

## Penomoran berikutnya

Aturan resmi **1–81, 83, 84, 85, 86 (a) dan (b), 87** · usulan tersisa **77**, **78**,
**82**, **88**, **89** · **aturan berikutnya yang bebas 90** · KC resmi sampai **KC-55**
(KC-16 kosong selamanya) · **KC berikutnya KC-56** · Hipotesis berikutnya **H-A024** ·
Jurnal berikutnya **148** (tanggal **UTC**) · `STATE.md` berikutnya **v59** · EKOR
berikutnya **v18** · UKUR berikutnya **v18** · PROMPT berikutnya **v55 (belum didorong)**
· ADR berikutnya **A022** · Ramalan berikutnya **R-317** · papan skor **321 SAH** (TEPAT
**221** · MELESET **61** · SEPARUH **22** · TIDAK TERADJUDIKASI **10** · MENUNGGU **7**).
