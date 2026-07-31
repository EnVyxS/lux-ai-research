# STATE lampiran UKUR — bagian 3 dari STATE (v19, milik STATE v60)

**Kedudukan berkas ini.** STATE dipecah tiga sejak v43 (KC-42). Pembagian berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, 83, 84, 85, 86 (a) dan (b), 87,
   **90**; KC-1..**KC-55** resmi, **KC-56 dan KC-57 diusulkan**.
2. **`STATE_LAMPIRAN_EKOR.md`** v19 (blob **`e19c5573966d835e9d40eadcb55165ab7d79f0de`**,
   commit **`b8877a2710544723ce81fc44ad505fa08fb7828b`**) — bagian 2: papan skor, ADR,
   catatan kejujuran, utang verifikasi.
3. **`STATE_LAMPIRAN_UKUR.md`** (berkas ini, v19) — bagian 3: pengukuran, modul,
   workflow, uji, API, hipotesis, koreksi bernomor, utang ukur.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) dan **`PROMPT_KELANJUTAN.md`** (blob
   `35beed44`) — **arsip; BUKAN sumber** (ADR-A018 kep. 9).

Dasar v19: UKUR v18 (blob **`11b14975a7ee2b00ca5e25ca19fc4e16ad5c1deb`**, commit
**`51c65e2afea4364a855e68c8f84465d1a2efcac9`**), dibaca UTUH pada giliran yang sama
sebelum berkas ini ditulis (aturan 52, pencegahan KC-43).

**Apa yang v19 bawa, disebut di muka.** v17 membawa angka **51** yang membatalkan
gambaran yang baru tersusun. v18 membawa medan yang nyaris dibaca salah
(`cacah_bulan`). **v19 membawa dua hal yang lebih keras daripada keduanya:**

1. **Sebuah KELAS BATAS BARU.** Sebuah laporan dapat terbaca **UTUH menurut alat** dan
   tetap **tidak lengkap**, karena **modulnya sendiri** memotongnya. `lubang_awal.json`
   melaporkan 42.449 byte tanpa satu pun peringatan, dan di dalamnya tertulis bahwa
   **58 dari 118 baris tidak pernah ditulis**. Kelas ini **lebih berbahaya** daripada
   pemotongan alat: tidak ada peringatan sama sekali.
2. **Jembatan 51 − 48 = 3 TERTUTUP TANPA SISA, dan ketiga bulannya BERNAMA.** Utang ukur
   20 dan 23 — yang v18 akui **tidak terbayar, hanya dipertajam** — kini **LUNAS**.

v19 juga membawa **kesalahan dokumen butir 18** (konvensi batas tabel H-A010),
**pelunasan utang ukur 24**, dan **satu utang ukur baru bernomor 25** yang kini menjadi
**poros riset peringkat pertama**.

## KESERASIAN VERSI — PULIH PADA ATURAN, BELUM PADA PAPAN SKOR

- `STATE.md` **v60** — blob **`d3f1448fad4ead804be59b1bbb1562b460f01621`**, commit
  **`8345668e9a8f0e01bcbe86fd9d0f60f4709fd834`**.
- `STATE_LAMPIRAN_EKOR.md` **v19** — blob **`e19c5573966d835e9d40eadcb55165ab7d79f0de`**,
  commit **`b8877a2710544723ce81fc44ad505fa08fb7828b`**.
- `STATE_LAMPIRAN_UKUR.md` **v19** — berkas ini.

Ketertinggalan **dua versi isi** yang dicatat EKOR v19 terhadap berkas ini — pembacaan
`lubang_awal.json`, kelas batas pemotongan oleh MODUL, tabel `baris_penyebut_butir_2`,
penanda **EKSKLUSIF** pada tabel H-A010, aritmetika 50 − 48 = 2 dan 9 − 7 = 2,
pembacaan `bulan_absen.py`, dan seluruh isi `bulan_absen_ringkas.json` — **LUNAS oleh
berkas ini**.

**SATU KETIDAKSERASIAN TETAP TERBUKA, dan ia disebut apa adanya:** `STATE.md` v60 memuat
papan skor **325**; EKOR v19 memuat dan **mengesahkan 329**. Sebabnya tersurat: R-318
diadjudikasi di jurnal 151, **sesudah** STATE v60 didorong. **Sumber sah untuk papan skor
adalah EKOR v19** (aturan 29). Berkas ini **tidak** memuat papan skor dan **tidak
berwenang** mengesahkannya. **Pemulihan penuh menuntut `STATE.md` v61.**

**Satu berkas per push tetap MENGIKAT** (KC-42, KC-43).

**Tentang push berkas ini:** ia di akar repo sehingga menyalakan `ci.yml`. Tidak satu
pun `tests/**` berubah, jadi cacah uji tetap **1377** — ramalan **deterministik**,
**MUDAH**, TIDAK masuk papan skor, TIDAK menambah beruntun aturan 57. **Laporannya
WAJIB dibaca sebelum push akar berikutnya** (aturan 38 **ke-66**) dan **WAJIB DITOLAK
bila medan `commit` tidak cocok** (**aturan 90**, kini RESMI).

**Angka yang TIDAK berubah dari v44/v45/v6/v7** (tidak diulang): taksonomi 9 kelas,
H-A013..H-A015, terhenti, SETTLED. Rinciannya di v44 (blob `d302caff`), v45
(`eb826817`), v6 (`27e59a79`), v7 (`4e7fb65b`).

## KOREKSI KC-41 — BACA SEBELUM MENGUTIP BERKAS INI

Keenam belas koreksi **tetap dicantumkan** karena semuanya soal dokumen kami sendiri,
bukan soal data — menghapusnya berarti menghapus jejak cacat.

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
**[v18] Pencabutan itu punya penyangkalan TERUKUR:** ketiga bulan itu **ADA** pada
`semesta_rentang.json`, di dalam rentang kontinu 2022-04..2026-06.
**[v19] Kini penyangkalan itu BERLAPIS DUA:** kedua bulan yang di dalam rentang terukur
**`gagal_gerbang`** — sebabnya **gerbang**, bukan **kelahiran simbol**. Tafsir yang
dicabut itu tidak sekadar tak terbukti; **sebab sejatinya kini bernama.**

**Koreksi 14 [v17] — `bulan_per_simbol` dibaca sebagai DAFTAR, isinya CACAH.**
Praregistrasi R-316 menanyakan kehadiran dua bulan **bernama**; berkasnya **tidak
memuat satu nama bulan pun**. **KC-54 kejadian KETIGA.**

| kejadian | medan | dibaca sebagai | sebenarnya |
| --- | --- | --- | --- |
| 1 (Koreksi 11 butir 2) | label gugus `2022-05` / `2024-05` | bulan lubang tengah | `bulan_klines_pertama` BNXUSDT |
| 2 (Koreksi 13) | `lubang_tak_dikenal` | posisi **waktu** lubang | kegagalan pasangan terhadap penyebut 19.586 |
| 3 (Koreksi 14) | `bulan_per_simbol` | daftar bulan | **cacah** bulan |

**[v19] KC-54 TETAP TIGA KEJADIAN.** Ia ditangkal **preventif** untuk kedua kalinya
berturut: definisi `bulan_absen`, `pembeda_absen`, `rentang`, dan `kendali` **disalin
verbatim** dari medan `definisi` laporan sebelum satu pun angkanya ditafsirkan.

### Koreksi 15 [v18] — `cacah_bulan` nyaris dibaca sebagai BENTANGAN KALENDER

`reports/semesta_rentang.json` memberi tiap simbol tiga medan: `bulan_pertama`,
`bulan_terakhir`, `cacah_bulan`. **Definisi `cacah_bulan` tidak tertulis di berkas itu,
dan tidak ada modul yang diketahui menulisnya** (utang ukur 22, masih hidup).

Untuk **BNXUSDT** angkanya cocok sempurna dengan bentangan: 2022-04..2026-06 →
(2026−2022)×12 = 48; +(6−4) = 50; +1 = **51**, dan `cacah_bulan` juga **51**. Bila
pemeriksaan berhenti di situ, kesimpulan "`cacah_bulan` = bentangan kalender" akan
ditulis, terdengar masuk akal, dan **salah**.

| simbol | bentangan (tangan) | `cacah_bulan` | selisih |
| --- | --- | --- | --- |
| BNXUSDTSETTLED | 2022-04..2023-02 → **11** | **6** | **5** |
| TLMUSDTSETTLED | 2022-01..2023-03 → **15** | **9** | **6** |

**Maka `cacah_bulan` mencacah bulan yang BENAR-BENAR ADA, bukan panjang rentang.**
Karena medan ini **mampu** menunjukkan selisih, selisih **nol** pada BNXUSDT adalah
**pengukuran, bukan ketiadaan alat** — aturan 50 dengan **kendali positif tertulis**.

**Bukan KC-54:** nama `cacah_bulan` sudah jujur menyebut dirinya "cacah". Yang hampir
menipu adalah **kemiripan angka pada satu simbol**. Kelasnya kerabat **KC-47**.
**Penangkal yang bekerja:** memeriksa simbol kedua **sebelum** menulis definisi.

### **Koreksi 16 [BARU v19] — KONVENSI BATAS TABEL SENDIRI BERGESER SATU BULAN**

Ini **kesalahan dokumen butir 18** dalam daftar bersama, diresmikan di STATE v60 dan
disalin ke sini karena tabelnya **hidup di lampiran ini**.

Tabel H-A010 di bagian LUBANG TENGAH menuliskan kolom "rentang lubang awal" dengan batas
kanan **EKSKLUSIF** — yaitu bulan pertama yang **TIDAK** lagi berlubang. Medan sumbernya,
`akhir_lubang_awal` pada `reports/lubang_awal.json`, **INKLUSIF** — bulan terakhir yang
**MASIH** berlubang. Selisihnya tepat **+1**, pada **lima dari lima** baris:

| simbol | tabel H-A010 lama (EKSKLUSIF) | `akhir_lubang_awal` sejati (INKLUSIF) |
| --- | --- | --- |
| BNXUSDT | 2023-02 | **2023-01** |
| ICPUSDT | 2022-09 | **2022-08** |
| JUPUSDT | 2024-02 | **2024-01** |
| QTUMUSDT | 2020-03 | **2020-02** |
| TLMUSDT | 2023-03 | **2023-02** |

**Akibat terukur:** butir 3 R-317 mengutip **2023-02** dari tabel cacat ini dan **KALAH**
terhadap **2023-01**. **Kekalahan itu TIDAK dibatalkan** (aturan 29, ADR-A016); yang
ditambahkan hanya **sebabnya**.

**Mengapa ia lolos begitu lama:** **setiap angkanya benar**. Yang salah hanya
**konvensi**, dan konvensi tidak pernah dibaca ulang. Tidak ada aritmetika yang keliru,
sehingga penangkal butir 17 (aritmetika terbuka) **tidak dapat menangkapnya sama sekali**.

**Pola koreksi resmi bertambah satu bentuk:** *kolom ringkasan buatan sendiri yang
batasnya bergeser satu satuan dari medan sumbernya.*

**Yang DILARANG:** mengutip tabel H-A010 di lampiran ini sebagai nilai
`akhir_lubang_awal`. **Sumber sah hanya `reports/lubang_awal.json`.**

**KC-57 [DIUSULKAN, DITAHAN].** *Tabel ringkasan yang disusun tangan dapat memakai
konvensi batas yang berbeda dari medan sumbernya; kecocokan angka tidak menjamin
kecocokan konvensi.* **Penangkal:** setiap kolom tabel buatan sendiri WAJIB menyebut
nama medan sumbernya **dan konvensinya** di kepala kolom. **TIDAK diresmikan:** lima
baris itu berasal dari **satu kolom pada satu tabel** — satu cacat tampak lima kali,
bukan lima pengamatan bebas. Meresmikannya adalah **KC-47 persis**.

**Bacaan jujur atas Koreksi 4, 9, 10, 11, 12, 13, 14, 15, dan 16 bersama-sama:** cacat
yang bertahan paling lama di riset ini bukan salah hitung, melainkan **tafsir yang
terdengar masuk akal atas angka yang benar**; sejak v15 bertambah **label yang masuk
akal atas medan yang benar**; sejak v18 bertambah **kecocokan angka pada satu contoh
yang terdengar seperti definisi**; dan **sejak v19 bertambah konvensi batas yang
bergeser satu satuan tanpa satu pun angka salah.**

## BATAS KEKUATAN ATURAN 52 — DIPERSEMPIT, BUKAN DICABUT

> Pembacaan ulang **dokumen sendiri** lemah terhadap penalaran cacat: ia membaca
> kalimat yang sudah diyakini benar. Pembacaan **kode** kuat terhadapnya.

**[v16] Bukti ketiga:** bacaan `lubang_tak_dikenal` bertahan melewati **empat** berkas
akar dan runtuh dalam **satu** pembacaan laporan.
**[v17] Bukti keempat:** R-316 butir 1 tidak dapat diadili sama sekali.
**[v18] Bukti kelima:** kalimat "Tujuh belas pembacaan berturut (ke-42..ke-57)" lolos
dari **dua puluh empat** pembacaan ulang, padahal 57 − 42 = 15; 15 + 1 = **enam belas**.
Yang menangkapnya **aritmetika tangan**, bukan pembacaan.
**[v19] Bukti keenam, dan ia paling tajam:** butir 18 lolos dari **seluruh** pembacaan
ulang sejak tabel H-A010 disusun, karena **setiap angkanya benar**. Ia **tidak dapat**
ditangkap oleh aritmetika. **Yang menangkapnya hanya SUMBER DI LUAR DOKUMEN** —
pembacaan `reports/lubang_awal.json`.

**[v19] Bukti balik yang jujur, dan ini yang paling berharga.** Pada giliran R-318,
aturan 86 (b) dipakai lebih dulu: `lux_ai/serapan/bulan_absen.py` dibaca UTUH **sebelum**
laporannya dibuka. Satu pembacaan kode menghasilkan **tiga penangkal sekaligus**:

1. kepastian bahwa modul itu **tanpa pembatas baris**, sehingga `baris_berabsen` lengkap
   — pengetahuan yang **mustahil** diperoleh dari laporan;
2. definisi resmi tiap medan **disalin** sebelum ditafsirkan (KC-54 ditangkal);
3. pengetahuan bahwa **tepi tidak pernah absen menurut definisi**, sehingga 2022-04
   mustahil muncul — dan pita ramalan dikunci dengan sadar atas dasar itu.

**DILARANG** menulis bahwa aturan 52 menjaga mutu penalaran **atas dokumen**; yang
dijaganya **kesetiaan salinan**, dan ia **kuat atas kode**.

**Penangkal wajib sejak v59:** setiap panjang deret ditulis bersama aritmetika
`akhir − awal + 1` secara terbuka. Diterapkan di seluruh berkas ini.

## [BARU v19] KELAS BATAS BARU — PEMOTONGAN OLEH MODUL, BUKAN OLEH ALAT

Sampai v18, satu-satunya kelas ketidaklengkapan yang dikenal adalah **pemotongan alat**,
yang **selalu** mengumumkan dirinya secara verbatim:
`This result has been truncated (showing NN% of full).`

**v19 menemukan kelas kedua, dan ia tidak mengumumkan dirinya sama sekali.**

`reports/lubang_awal.json` terbaca **42.449 byte, UTUH, tanpa satu pun peringatan alat**.
Di dalamnya:

| medan | nilai |
| --- | --- |
| `penyebut_butir_1` | **118** |
| `cacah_baris_penyebut_butir_1_dilapor` | **60** |
| **selisih** | **58 baris tidak pernah ditulis** |

Sebabnya terukur dari kode, bukan diduga: `lux_ai/serapan/lubang_awal.py` (blob
**`8c36943da222dfa262b3b9f2117bf72dc801681d`**, dibaca UTUH) memuat
**`BATAS_BARIS_LAPORAN = 60`**.

> **Kelas ini LEBIH BERBAHAYA daripada pemotongan alat.** Pemotongan alat berteriak;
> pemotongan modul diam. Satu-satunya pendeteksinya adalah **membaca kode sebelum
> laporan** (aturan 86 b) — atau, secara kebetulan, sebuah medan yang jujur melaporkan
> cacah barisnya sendiri.

**LARANGAN PERMANEN.** **DILARANG** menarik **cacah, sebaran, daftar, minimum, maksimum,
atau kesimpulan apa pun** dari larik `baris_penyebut_butir_1`. Yang boleh dipakai hanya
medan agregat yang dihitung modul atas **seluruh** 118, bukan atas 60 yang tertulis.

**Pemeriksaan yang dilakukan atas modul kedua, PREVENTIF:**
`lux_ai/serapan/bulan_absen.py` (blob **`10279d721d66a86b6d265badf81ada3204648f69`**)
dibaca UTUH **sebelum** laporannya dibuka. **Ia TIDAK memiliki pembatas baris apa pun.**
Maka `baris_berabsen` pada `bulan_absen_ringkas.json` **LENGKAP** — dan itu **terukur**,
bukan diasumsikan.

**Konsekuensi prosedural:** aturan 86 (b) naik dari "disiplin baik" menjadi
**satu-satunya penangkal yang diketahui** untuk kelas batas ini. Setiap laporan yang
dikutip sesudah v19 wajib disertai jawaban atas pertanyaan: **apakah modul penulisnya
sudah dibaca, dan apakah ia punya pembatas baris?**

## [BARU v19] `reports/lubang_awal.json` — bahan R-317

Blob **`3da15a11c3cd949fb2741f919beb2b515a51d70f`**, **42.449 B**, dibaca pada ref
`1ba0a007421182d22584a1d22fac546ff7951b7d`. `waktu_utc` **2026-07-30T07:23:11Z** ·
`sidik_kode` **`156499ce9d6e822bb7f57786e8e308955441996699c1fd53d0e8814e1f8f2362`**.
**Tanpa pemotongan ALAT; DIPOTONG MODUL** (lihat bagian di atas).

| medan | nilai |
| --- | --- |
| `cacah_simbol_ada_lubang` | **122** |
| `cacah_simbol_lubang_awal` | **5** |
| `cacah_simbol_lubang_bukan_awal` | **118** |
| `cacah_bangkit` | **8** |
| `penyebut_butir_1` / `bagian_butir_1` | **118** / **1.0** |
| `penyebut_butir_2` / `numerator_butir_2` / `bagian_butir_2` | **5** / **3** / **0.6** |
| semua `selisih_*` | **0** |

**`baris_penyebut_butir_2` — 5 dari 5, LENGKAP** (larik ini **tidak** kena batas 60):

| simbol | `bulan_pertama` | `bulan_terakhir` | `cacah_bulan` | `cacah_lubang` | `cacah_lubang_awal` | `cacah_lubang_bukan_awal` | **`akhir_lubang_awal` (INKLUSIF)** | `cacah_mati` | `bangkit` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **BNXUSDT** | **2022-05** | 2026-06 | **48** | 19 | **7** | 12 | **2023-01** | 15 | false |
| ICPUSDT | 2021-05 | 2026-06 | 62 | 16 | 16 | 0 | **2022-08** | 2 | true |
| JUPUSDT | 2024-01 | 2026-06 | 30 | 1 | 1 | 0 | **2024-01** | 0 | false |
| QTUMUSDT | 2020-02 | 2026-06 | 77 | 1 | 1 | 0 | **2020-02** | 0 | false |
| TLMUSDT | 2021-07 | 2026-06 | 60 | 20 | 20 | 0 | **2023-02** | 8 | true |

Baris lain yang terbaca di `baris_penyebut_butir_1` (**DILARANG dicacah** — 58 hilang):
BTCSTUSDT (2021-03..2026-06, 64, `cacah_mati` **63**) · DARUSDT (2022-04..2026-06, 51) ·
FTTUSDT (2022-04..2026-06, 51, `cacah_mati` 43) · LENDUSDT (2020-07..2020-11, 5).

**Temuan struktural:** **empat dari lima** simbol lubang-awal **kontigu sempurna**
(16=16, 20=20, 1=1, 1=1). **Hanya BNXUSDT tidak:** 7 dari 19. Rentetan kalender
2022-05..2023-01 = **9** bulan; 9 − 7 = **2**. **Selang itu sama besarnya dengan
50 − 48 = 2** — dan v19 kini tahu keduanya adalah **selang yang sama**, bernama
**2022-06** dan **2022-08**. ✅

**Blok `uji_r305` — VONIS ALAT, BUKAN ADJUDIKASI (KC-49).** Ia menyatakan sendiri
butir 1 KALAH (`bagian` **1.0** di luar pita 0.55–0.95; penyebut **118** ≥ minimal 100)
dan butir 2 KALAH (`bagian` **0.6** < 0.80; cacah **5** di bawah pita 20–120).
**Papan skor TIDAK disentuh** (aturan 29). R-305 tetap menunggu **adjudikasi tangan**
atas `journal/2026-07-30-125.md`, yang **belum dibaca**.

**Catatan atas `bagian_butir_1` = 1.0.** Nilai itu **tautologis**: modul menghitung
`cacah_bulan` sebagai `len(urut)` atas penyebut 19.586, sehingga pembilang dan penyebut
butir itu tidak bebas. **DILARANG** dibaca sebagai temuan empiris.

**Tetapan R-305 yang tertanam di modul:** `R305_PITA_BUTIR_1=(0.55,0.95)` ·
`R305_MINIMAL_PENYEBUT_BUTIR_1=100` · `R305_PITA_BUTIR_2_CACAH=(20,120)` ·
`R305_MINIMAL_BAGIAN_BUTIR_2=0.80`. Docstring modul memuat **praregistrasi R-305**.

## [BARU v19] `reports/bulan_absen_ringkas.json` — bahan R-318, TERBACA UTUH

Blob **`e450d9f95e9bca0dc28a0e01c6aad6594c4fa3d6`**, dibaca pada ref
`6894b02f36b6c1a0ee27ad0a90f9c7f1f4697d75`. **TANPA PEMOTONGAN ALAT, dan modulnya
terukur TANPA PEMBATAS BARIS.**

| medan | nilai |
| --- | --- |
| `waktu_utc` | **2026-07-29T17:50:29Z** |
| `versi_bulan_absen` | **1** |
| `sidik_kode` | **`0294eb3a2fca6354b495148fc87d564f649d545a81314f21ef432775cf163088`** |
| `berkas_sumber` | `reports/bulan_absen.json` |
| `byte_sumber` | **249.992** |
| `sidik_sumber` | **`d2fc3bfb362f834225faab76d6bf87b8f334d1ee26638a8112fb9b546614a3bd`** |

**Definisi resmi, DISALIN VERBATIM dari medan `definisi` sebelum ditafsirkan (KC-54):**

> `bulan_absen` — *"bulan kalender di antara bulan_pertama dan bulan_terakhir sebuah
> simbol yang TIDAK ada di penyebut 19.586; BUKAN lubang funding dan BUKAN lubang
> tengah"*.

> `pembeda_absen` — *`gagal_gerbang` bila bulan itu ADA di manifes arsip;
> `tak_diterbitkan_arsip` bila tidak ada di manifes; `tak_terukur` bila manifes tidak
> lengkap terbaca*.

**Konsekuensi definisi yang WAJIB dicatat:** karena batasnya *"di antara bulan_pertama
dan bulan_terakhir"*, **bulan tepi tidak pernah dapat absen**. Maka **2022-04 mustahil
muncul** di medan ini — dan itu diketahui **sebelum** pita R-318 dikunci.

**`ringkasan` — penggugur dan kendali, diperiksa LEBIH DULU:**

| medan | nilai |
| --- | --- |
| `kendali_sah` | **true** (BTCUSDT **78**/0 · ETHUSDT **78**/0, ambang 60) |
| `penggugur_menyala` | **false** |
| `sidik_seragam` | **true** |
| `cacah_laporan_dibaca` / `cacah_manifes_dibaca` / `total_pecahan` | **8** / **8** / **8** |
| `cacah_kunci_ganda` | **0** |
| `laporan_hilang` / `manifes_hilang` | **[]** / **[]** |
| `selisih_penyebut` / `selisih_nama_penyebut` | **0** / **0** |
| `cacah_nama_tak_konsisten_rentang` | **0** |
| `penyebut_kehidupan` | **19.586** |
| `cacah_nama_penyebut` / `cacah_nama_didaftar` | **787** / **787** |
| `sidik_kode_laporan` | **[`24b6bb26…c8595`]** |

**`ringkasan` — besaran pokok:**

| medan | nilai |
| --- | --- |
| `cacah_nama_berabsen` | **10** dari 787 |
| `jumlah_bulan_absen` | **11** |
| `jumlah_bulan_absen_pasangan` | **11** |
| `jumlah_bulan_absen_luar_pasangan` | **0** |
| `cacah_pasangan` | **15** |
| **`sebaran_pembeda`** | **`gagal_gerbang` 11 · `tak_diterbitkan_arsip` 0 · `tak_terukur` 0** |
| `selisih_absen_pasangan_jurnal_113` | **−1** (12 tercatat vs **11** terukur) |

**`baris_berabsen` — sepuluh nama, LENGKAP:**

| simbol | `bulan_absen` | `bulan_pertama` | `bulan_terakhir` | `rentang` | `cacah_bulan_lolos` | pembeda |
| --- | --- | --- | --- | --- | --- | --- |
| AERGOUSDT | 2025-04 | 2024-09 | 2026-06 | 22 | 21 | gagal_gerbang |
| AIAUSDT | 2026-01 | 2025-09 | 2026-06 | 10 | 9 | gagal_gerbang |
| **BNXUSDT** | **2022-06, 2022-08** | **2022-05** | 2026-06 | **50** | **48** | gagal_gerbang ×2 |
| CTKUSDT | 2025-04 | 2020-11 | 2026-06 | 68 | 67 | gagal_gerbang |
| CVCUSDT | 2025-05 | 2020-11 | 2026-06 | 68 | 67 | gagal_gerbang |
| CVXUSDT | 2025-07 | 2022-09 | 2026-06 | 46 | 45 | gagal_gerbang |
| LITUSDT | 2025-12 | 2021-02 | 2026-06 | 65 | 64 | gagal_gerbang |
| MAVIAUSDT | 2025-03 | 2024-02 | 2026-06 | 29 | 28 | gagal_gerbang |
| PUMPUSDT | 2025-07 | 2025-04 | 2026-06 | 15 | 14 | gagal_gerbang |
| SLPUSDT | 2025-07 | 2023-10 | 2026-06 | 33 | 32 | gagal_gerbang |

**`baris_pasangan_settled` (15).** `absen_sama_dengan_settled` **true** untuk kesembilan
simbol berabsen tunggal. **false** untuk **BNXUSDT** (`bulan_settled_terakhir`
**2023-02**, `settled_ada_di_absen` **false**). Lima pasangan berabsen **nol**: BDXNUSDT
(settled 2026-04, 10/10) · ICPUSDT (2022-09, 62/62) · MINAUSDT (2023-02, 41/41) ·
SXPUSDT (2026-06, 71/71) · TLMUSDT (2023-03, 60/60).

**Ketertutupan yang diperiksa tangan:** 9 absen tunggal + 2 milik BNXUSDT = **11** =
`jumlah_bulan_absen` ✅ · 11 + 0 + 0 = **11** = sebaran pembeda ✅ · 10 berabsen +
5 berabsen nol = **15** pasangan ✅

### Tiga kesimpulan TERUKUR

1. **Bulan absen adalah gejala GERBANG, bukan gejala PENERBITAN.** Sebelas dari sebelas
   **ADA di manifes arsip** lalu **ditolak gerbang**. Ini pertama kalinya sebuah kelas
   lubang di riset ini disertai **mekanisme bernama**, bukan sekadar bentuk.
2. **BNXUSDT satu-satunya simbol dengan lebih dari satu bulan absen** di seluruh 787.
3. **BNXUSDT satu-satunya yang bulan absennya BUKAN bulan settled terakhirnya.**

**KC-53 ditangkal preventif:** `tak_diterbitkan_arsip` **0** dan `tak_terukur` **0**
**TIDAK** dibaca sebagai "arsip selalu menerbitkan". Yang terukur hanya: **dari 11 bulan
absen, tak satu pun bersebab itu.**

### Yang DILARANG disimpulkan

1. **DILARANG** menyebut **klausa mana** dari `gerbang_1m.py` yang menjatuhkan bulan-bulan
   itu. Yang terukur hanya **bahwa** pembedanya `gagal_gerbang`. → **utang ukur 25**.
2. **DILARANG** menyamakan "tidak ada di penyebut" dengan "dijatuhkan gerbang" **secara
   umum**, di luar apa yang dilaporkan medan `pembeda_absen` untuk 11 bulan itu.
3. **DILARANG** menyimpulkan bahwa hanya simbol berpasangan settled yang berabsen:
   seluruh 11 memang milik pasangan settled, **tetapi 5 dari 15 pasangan berabsen nol** —
   "berpasangan settled" **bukan syarat cukup**.
4. **DILARANG** memakai blok `uji_r288` sebagai adjudikasi (KC-49).
5. **DILARANG** mengutip selisih **3 lawan 2** sebagai bukti KC-52. Angka 3 adalah
   `R288_BNX_ABSEN`, sebuah **tetapan ramalan di dalam kode**, bukan pengukuran laporan
   kedua. **Ramalan yang kalah bukan dua penyebut yang berselisih.**

## [BARU v19] JEMBATAN 48 / 50 / 51 — TERTUTUP TANPA SISA

Sejak v17 riset ini memegang tiga angka bersaing untuk satu simbol. v18 menambah sumber
keempat dan tetap menyebutnya **tidak terdamaikan**. **v19 menutupnya secara aritmetis:**

| angka | medan / asal | arti terukur |
| --- | --- | --- |
| **48** | `cacah_bulan_lolos` (`bulan_absen_ringkas`); `cacah_bulan` (`lubang_awal`); `cacah_bulan_klines_simbol` (`silang_funding`) | bulan BNXUSDT yang **ADA di penyebut 19.586** |
| **50** | `rentang` (`bulan_absen_ringkas`) | **bentangan kalender** 2022-05..2026-06 |
| **51** | `cacah_bulan` (`semesta_rentang`); `bulan_per_simbol` (`semesta_bulan_1m`) | bulan berberkas, bentangan 2022-04..2026-06 |

**Aritmetika terbuka, tiga baris:**

- **51 − 50 = 1** → satu bulan **di tepi**: **2022-04** (di luar penyebut karena
  `bulan_pertama` penyebut adalah 2022-05).
- **50 − 48 = 2** → dua bulan **di dalam**: **2022-06** dan **2022-08**, keduanya
  terukur **`gagal_gerbang`**.
- **51 − 48 = 3** = 2 + 1 ✅ — dan `cacah_lubang_tak_dikenal` juga **3**, dengan
  **nama yang sama persis**: 2022-04, 2022-06, 2022-08.

**Silang kedua yang menutup mandiri:** rentetan lubang awal 2022-05..2023-01 = **9**;
`cacah_lubang_awal` = **7**; 9 − 7 = **2** — **selang yang sama**, dari laporan yang
**berbeda**.

**Apa yang ini SUNGGUH buktikan, dan apa yang TIDAK.**

- **TERBUKTI:** untuk **BNXUSDT**, ketiga angka itu konsisten dan ketiga bulan selisihnya
  **bernama**. **KC-52 SEBAGIAN TERDAMAIKAN** — untuk pertama kalinya sejak lahir.
- **TIDAK TERBUKTI:** apakah himpunan **787** simbol pada kedua laporan itu himpunan yang
  sama. **KC-52 TIDAK DICABUT.**
- **TIDAK TERBUKTI:** keanggotaan penyebut untuk **786 simbol lain**. Yang diukur satu
  simbol. **DILARANG** digeneralkan (KC-47).

## SEMESTA BULAN 1M (dari v17, tidak berubah)

Blob **`a1a6d3f0f13dd7100a91853cadfcaa9a5620fee3`**, **18.884 B**, `waktu_utc`
**2026-07-28T09:44:48Z**, TERBACA UTUH. Dua kunci: `bulan_per_simbol` (peta simbol →
**satu bilangan bulat**) dan `waktu_utc`. **Tidak ada nama bulan.** Cacah entri peta
**DILARANG dikutip terukur** (aturan 66). `bulan_per_simbol["BNXUSDT"]` **51** ·
`["BNXUSDTSETTLED"]` **6**.

**CATATAN KESERAMPAKAN yang WAJIB disebut:** semesta 1m lahir 2026-07-28T09:44:48Z ·
`silang_funding.json` 2026-07-29T08:17:55Z · **`bulan_absen_ringkas.json`
2026-07-29T17:50:29Z** · `lubang_awal.json` 2026-07-30T07:23:11Z · semesta rentang
**tak bertanggal**. **Bukan pengukuran serempak** (KC-56).

**Aturan 36 TETAP TIDAK diberi kasus keempat** oleh kecocokan 3 = 3, 6 = 6, maupun
51 = 51. **[v19] Bahkan sesudah jembatan tertutup, ini tetap berlaku:** yang menutup
adalah **aritmetika di dalam satu simbol**, bukan **sebaran lintas simbol**.

## SEMESTA RENTANG — tak bertanggal, terbaca 95% (dari v18)

Blob **`8d5bd06ca4073dac8a8ef7841d81824427cc8e63`**, **110.662 B**, dibaca pada ref
`24b53ba5d1bab273c0ac457c3ee8f65b94915ecb`.

**BATAS ALAT YANG WAJIB DISEBUT SETIAP KALI BERKAS INI DIKUTIP.** Verbatim:
`This result has been truncated (showing 95% of full).` Potongan hilang di **tengah**,
abjad **P–R** (antara `PLTRUSDT` dan `ROBOUSDT`). **Cacah entri `rentang` DILARANG
diklaim terukur** (aturan 66).

Satu kunci akar `rentang`; tiga medan per simbol. Entri terakhir terbaca `"龙虾USDT"`.
**TANPA `waktu_utc`. TANPA medan sidik apa pun** — terukur, sebab ekor berkas terbaca.

| simbol | `bulan_pertama` | `bulan_terakhir` | `cacah_bulan` | bentangan (TURUNAN) | lubang |
| --- | --- | --- | --- | --- | --- |
| **BNXUSDT** | **2022-04** | **2026-06** | **51** | **51** | **0** |
| BNXUSDTSETTLED | 2022-04 | 2023-02 | **6** | 11 | **5** |
| TLMUSDT | 2021-07 | 2026-06 | **60** | 60 | **0** |
| TLMUSDTSETTLED | 2022-01 | 2023-03 | **9** | 15 | **6** |
| MATICUSDT | 2020-10 | 2024-09 | 48 | 48 | 0 |
| BTCSTUSDT | 2021-03 | 2026-06 | 64 | 64 | 0 |
| SXPUSDT | 2020-07 | 2026-05 | 71 | 71 | 0 |
| FTTUSDT | 2022-04 | 2026-06 | 51 | 51 | 0 |
| 1000LUNCBUSD | 2022-05 | 2023-12 | 20 | 20 | 0 |
| ICPUSDT_SETTLED | 2022-01 | 2022-09 | 9 | 9 | 0 |

**Larangan yang tetap berlaku penuh:** (1) DILARANG menyebutnya mengukur "semesta 1m";
(2) DILARANG menyimpulkan hanya simbol SETTLED yang berlubang; (3) DILARANG mengklaim
berapa banyak simbol berlubang; (4) DILARANG membandingkan secara keserempakan — ia tak
bertanggal (**KC-56**); (5) DILARANG memindahkan sifat `cacah_bulan` ↔ `bulan_per_simbol`;
(6) DILARANG menyatakan gerbang menjatuhkan bulan mana pun **atas dasar berkas ini**;
(7) DILARANG menyamakan "ada di semesta rentang" dengan "ada di penyebut 19.586".

**Pencabutan sebagian (v18) tetap berlaku:** larangan "51 mencakup 2022-04" **DICABUT**
untuk medan `cacah_bulan` (terukur kontinu), **TETAP BERLAKU PENUH** untuk medan
`bulan_per_simbol` (berkasnya tanpa nama bulan). **Kedua angka kebetulan sama-sama 51;
kesamaan itu DILARANG memindahkan pencabutan.**

### KC-56 [DIUSULKAN, TIDAK BERTAMBAH]

Laporan tanpa `waktu_utc` diperlakukan seolah serempak. **[v19] TIDAK mendapat kejadian
kedua:** `lubang_awal.json` **dan** `bulan_absen_ringkas.json` keduanya **bertanggal**.
Tetap **usulan** (ADR-A019 kep. 3). **KC berikutnya KC-59.**

## `gerbang_1m.py` — DIBACA UTUH; kini POROS PERINGKAT PERTAMA

Blob **`c8cc54c84a57173ef2e426c317d6ac50734e9b4a`**. Modul menyatakan dirinya penerapan
**ADR-A004 §2**.

**Enam klausa `KLAUSA`:** `deret_tidak_kosong` · `tanpa_duplikat` ·
`tanpa_menit_hilang` · `jarak_60_detik` · `selaras_menit` · `satuan_milidetik`.
`nilai_deret` → `lolos = not pelanggaran` — **satu klausa gagal cukup menjatuhkan**.
Tetapan `MS_BAWAH=1_000_000_000_000`, `MS_ATAS=100_000_000_000_000`. `sidik_kode()`
mencap **dua** berkas: `gerbang_1m.py` + `resample.py` (`66a4b177`).

Rumus yang wajib dikutip persis:
`rentang = (unik[-1] - unik[0]) // MS_MENIT + 1`;
`menit_hilang_dalam_rentang = rentang - len(unik)`
— dihitung **dari rentang yang ada di berkas**, **bukan** dari panjang bulan kalender.
Rumus itu **DISALIN**, bukan diimpor dari `diagnosa_kc6.celah_menit` (aturan 10);
penjaganya `tests/test_gerbang_1m.py`. Docstring **mengaku nilainya dapat negatif**.

Fungsi lain: `persen` · `satuan_stempel_dari_besaran` · `ukur_deret` · `nilai_klausa` ·
`ringkas_gerbang`.

**TEMUAN STRUKTURAL YANG MENGIKAT.** Modul ini **PUSTAKA MURNI** — tanpa `KELUARAN`,
tanpa `jalankan`/`main`, **tidak menulis laporan apa pun**.

> **Pertanyaan poros tentang gerbang TIDAK dapat dijawab dari keluaran gerbang, sebab
> tidak ada keluaran.** Ia harus lewat laporan **modul pemanggil**.

**[v19] Inilah yang membuat utang ukur 25 mahal.** Kini terukur bahwa **11 bulan absen
dijatuhkan gerbang** — tetapi **tidak ada satu medan pun di seluruh repo yang menamai
klausa pelanggaran per simbol-bulan**. Jawabannya menuntut **pemanggil ditelusuri**,
bukan laporan dibaca. **ADR-A004 §2 naik menjadi utang bacaan berperingkat tertinggi.**

## SILANG FUNDING — tiga lubang tak dikenal, kini BERNAMA dan TERJELASKAN POSISINYA

Blob **`b61fe8b3bcabbfce435dd5e5f78fc367f6bef617`**, `waktu_utc`
**2026-07-29T08:17:55Z**.

**BATAS ALAT YANG WAJIB DISEBUT SETIAP KALI.** Verbatim:
`This result has been truncated (showing 54% of full).` Bagian tengah larik
**`baris_mati`** TIDAK TERLIHAT → **cacah total `baris_mati` DILARANG diklaim terukur**
(utang verifikasi 39, utang ukur 17).

| # | simbol | bulan | di dalam rentang klines? | ada di semesta rentang? | **[v19] posisi terhadap penyebut** | **[v19] pembeda** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **BNXUSDT** | **2022-04** | **TIDAK** | **YA** | **tepi** (sebelum `bulan_pertama` penyebut 2022-05) | — |
| 2 | **BNXUSDT** | **2022-06** | **YA** | **YA** | **di dalam** | **`gagal_gerbang`** |
| 3 | **BNXUSDT** | **2022-08** | **YA** | **YA** | **di dalam** | **`gagal_gerbang`** |

`bulan_klines_pertama` **2022-05** · `bulan_klines_terakhir` **2026-06** ·
`cacah_bulan_klines_simbol` **48**.

**Ketiganya kini terjelaskan POSISINYA tanpa sisa. SEBAB KLAUSANYA tetap BELUM DIUKUR.**

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

Butir 1 **TEPAT** (**1**, BNXUSDT) · butir 2 **MELESET** (**1 dari 3**) · butir 3 MUDAH.
**DILARANG ditulis ulang sebagai SEPARUH.** Syarat gugur (e) MENYALA.

**[v19] Catatan yang wajib melekat:** butir 2 R-315 meramalkan **ketiga** lubang lebih
awal daripada `bulan_klines_pertama`; terukur **satu dari tiga**. Kekalahan itu kini
**dijelaskan sepenuhnya**: dua lubang lainnya duduk **di dalam** rentang dan gugur
karena **gerbang**, bukan karena kelahiran simbol. **Vonisnya tidak berubah.**

## KC-18 — semesta kehidupan

Atas **19.586** simbol-bulan lolos gerbang: **1.401 MATI** (7,153%), **98 SEPI**,
**18.087 HIDUP**. Dari 1.401 MATI: 842 kehilangan funding, 559 tetap berfunding.
`cacah_simbol_tanpa_hidup` **18**. 18.087 + 98 = 18.185, + 1.401 = **19.586** ✅

**Pembelahan [v9]:** **787** bulan PERTAMA + **18.799** bukan-pertama = 19.586 ✅
**Pembelahan MATI [v10]:** 1.392 penuh + **9** tak penuh = 1.401 ✅
**Pembelahan [v11]:** 18.799 − 1.401 = **17.398**; 17.284 penuh + **114** berdefisit ✅
**Pembelahan [v13]:** rilis parquet **19.598** = 19.586 lolos + **12** karantina.

**Pembelahan ketiga atas lubang funding:**

| kelas bentuk | seluruh semesta | di dalam penyebut | selisih |
| --- | --- | --- | --- |
| awal | **48** | **45** | **3** |
| ekor | **826** | **826** | 0 |
| tengah | **6** | **6** | 0 |
| **jumlah** | **880** | **877** | **3** |

**[v19] PERINGATAN YANG BERUBAH BENTUK.** **19.586** adalah penyebut **lolos gerbang**.
Semesta 1m dan semesta rentang **bukan** himpunan yang sama. Untuk **BNXUSDT** selisih
itu kini **terukur dan bernama** (51 / 51 / 48; tiga bulan: 2022-04 tepi, 2022-06 dan
2022-08 `gagal_gerbang`). **Untuk 786 simbol lain selisihnya BELUM DIUKUR dan DILARANG
DITAKSIR.** Yang berubah dari v18: pertanyaannya bukan lagi "apakah dapat didamaikan"
melainkan "apakah pola satu simbol ini berlaku umum" — dan itu **belum diukur**.

**[v19] Yang kini terukur secara semesta, dan ini besar:** dari **787** simbol, hanya
**10** punya bulan absen, seluruhnya berjumlah **11** bulan, **seluruhnya
`gagal_gerbang`**. Maka jarak antara "bulan berberkas" dan "bulan di penyebut" **bukan
fenomena luas** — ia terpusat pada sepuluh simbol.

## LUBANG TENGAH — POROS TUNTAS

Blob **`39cd1caacedc4d49ba23c91c80f553bb9fb135a6`**, **11.014 B**, dibaca UTUH.
`waktu_utc` **2026-07-29T09:38:52Z**. `versi_lubang_tengah` **2** · `versi_funding` **6**.

`cacah_lubang_tengah` **6** · `selisih_lubang_tengah` **0** · `cacah_lubang_ganda` /
`cacah_kunci_ganda` **0** / **0** · `cacah_laporan_dibaca` **8** ·
`cacah_per_simbol_funding` **787** · sebaran {HIDUP 0 · MATI **6** · SEPI 0} ·
`h_a010_menang` true (5–0) · `h_a011_menang` true. Sidik
**`c9372bd763b86cfeb2adcf0a0c0c43dae8d9aa9a6508e9c32f7671d5ec7b3f4e`**.

| # | simbol | bulan | status | byte_parquet | `cacah_lilin` |
| --- | --- | --- | --- | --- | --- |
| 1 | **BTCSTUSDT** | **2022-01** | MATI | 399.757 | 44.640 |
| 2 | **LITUSDT** | **2025-07** | MATI | 427.922 | 44.640 |
| 3 | **LITUSDT** | **2025-08** | MATI | 427.505 | 44.640 |
| 4 | **LITUSDT** | **2025-09** | MATI | 392.233 | 43.200 |
| 5 | **LITUSDT** | **2025-10** | MATI | 434.201 | 44.640 |
| 6 | **LITUSDT** | **2025-11** | MATI | 389.479 | 43.200 |

BTCSTUSDT rentetan **1**, klines pertama **2021-03**, **64** bulan. LITUSDT rentetan
**5**, klines pertama **2021-02**, **64** bulan. **TIDAK SATU PUN berbulan `2022-05`
atau `2024-05`.** BTCSTUSDT terukur **KONTIGU 64** pada semesta rentang; **keserian
dengan tebing tetap BELUM diukur dan DILARANG diklaim.**

### H-A010 MENANG 5–0 — TABEL DIPERBAIKI, KONVENSI DINYATAKAN (butir 18)

**Kepala kolom kini menyebut medan sumber DAN konvensinya**, sesuai penangkal KC-57:

| simbol | awal lubang awal | **`akhir_lubang_awal` (medan sumber, INKLUSIF)** | `cacah_bulan_klines` | `cacah_lubang` |
| --- | --- | --- | --- | --- |
| BNXUSDT | 2022-05 | **2023-01** | 48 | 19 |
| ICPUSDT | 2021-05 | **2022-08** | 62 | 16 |
| JUPUSDT | 2024-01 | **2024-01** | 30 | 1 |
| QTUMUSDT | 2020-02 | **2020-02** | 77 | 1 |
| TLMUSDT | 2021-07 | **2023-02** | 60 | 20 |

**Vonis H-A010 MENANG 5–0 TIDAK BERUBAH** — yang cacat adalah konvensi kolom ringkasan,
bukan hasil ujinya.

**CATATAN SILANG YANG WAJIB DITAHAN, kini BERLIPAT ENAM.** Baris BNXUSDT —
`cacah_bulan_klines` **48**, mulai **2022-05** — adalah medan yang sama yang: (a) di v15
berpindah menjadi nama poros "gugus 2022-05" (Koreksi 11); (b) di v16 menutup jembatan
50 lawan 48; (c) di v17 dibantah oleh **51** dari semesta 1m; (d) di v18 dibantah lagi
oleh semesta rentang yang mulai **2022-04**; **(e) di v19 akhirnya TERDAMAIKAN — 2022-04
adalah bulan tepi, dan selisih 2022-05 lawan 2022-04 itu terukur, bukan cacat;**
**(f) di v19 pula, kolom tetangganya terbukti bergeser satu bulan (butir 18).**
**Satu medan, enam pemakaian, dua di antaranya keliru sebelum diukur.**

Kendali: tiga baris **BTCUSDT** semuanya HIDUP dengan `funding_ada` true.

**Uji H-A020 dan H-A021 MUSTAHIL** — bukan mahal, **tidak ada bahannya**.

## VONIS `ukur_kolom` [v13] — dasar runtuhnya R-312

Dari `kehidupan_arsip.py` (`318a5cb1`): **`cacah_lilin` = `n`** dari
`pq.ParquetFile(...).metadata.num_rows`; **`cacah_lilin_terbaca`** = baris yang KEDUA
kolomnya terurai; identitas paksa
`cacah_lilin = cacah_lilin_terbaca + cacah_baris_cacat`. **Bukan dua pengukuran bebas.**
`cacah_berselisih` = 0 memaksa **`cacah_baris_cacat` = 0 di seluruh semesta**.

## ARAH SELISIH R-312 MUSTAHIL [v14, tetap]

`selisih = cacah_lilin_terbaca − cacah_lilin`, dipilih agar POSITIF; identitas
`ukur_kolom` memaksa `cacah_lilin_terbaca` ≤ `cacah_lilin` → **butir 2 R-312 tidak dapat
dimenangkan secara struktural**.

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
  Bulannya terukur **ADA** pada semesta rentang (TLMUSDT kontinu 60) **dan** TLMUSDT
  terukur **berabsen NOL** pada `bulan_absen_ringkas.json`. **[v19] Maka kekosongan itu
  DIPASTIKAN soal ISI, dari dua sumber bebas.** Utang ukur 7 menyempit lagi; tetap hidup.
- Sepuluh teratas tersebar di **TUJUH** bulan → aturan 81 **TIDAK** terpicu.
- ANCUSDT `2022-05` **26.959** lawan LUNAUSDT `2022-05` **26.950** — selisih **sembilan
  lilin**; dasar **H-A021**; **kebetulan angka, bukan bukti**.
- **712.925 DILARANG DISEBUT PENGUKURAN BEBAS** (tautologi, KC-50).

Sidik `6211624ba9514d604d4dc510abca2e40386775c7aaa1279135f0baf666f044b0`.

## KETERISIAN LILIN [v10, tetap]

`cacah_mati_penuh` / tak penuh **1.392** / **9** · `jumlah_lilin_langsung`
**839.325.999** · `defisit_total` **18.143.601** · `defisit_pertama` **17.335.439**
(95,5%) · `defisit_bukan_pertama` **808.162** (**0,0445**) · baris tanpa lilin / negatif
/ kunci ganda **0** / **0** / **0**.

- **BULAN MATI PENUH DATANYA; YANG NOL ADALAH TRANSAKSINYA** — 1.392 dari 1.401 (99,4%).
- **DILARANG** melanjutkan ke "harga beku": `medan_baris_terlihat` **14** medan, **tak
  satu pun harga**.
- Bulan pertama rata kehilangan **22.027** lilin; keterisian **≈ 49,7%**.

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
**bukan** bulan pertama simbol itu di bursa. **[v19] Perbedaan keduanya kini punya
contoh TERUKUR PENUH:** BNXUSDT mulai **2022-04** di semesta rentang, **2022-05** di
penyebut, dan selisih satu bulan itu **bukan cacat** melainkan bulan tepi yang tidak
lolos ke penyebut. Utang ukur 6 **menyempit tajam pada satu simbol**; **tetap hidup**
untuk 786 lainnya.

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

**[v19] Catatan silang baru yang WAJIB ditahan:** **LITUSDT** muncul di **tiga** tempat
sekaligus — lima lubang tengah 2025-07..2025-11, tebing funding 2025-07, dan **bulan
absen 2025-12** (`gagal_gerbang`). **Keseriannya DILARANG diklaim**: tiga kemunculan
satu simbol pada tiga laporan **bukan** tiga pengamatan bebas (KC-47), dan tak satu pun
diregistrasi lebih dulu (aturan 29).

## Lubang funding — agregat semesta (tetap)

`cacah_simbol_ada_lubang` **122** dari 787 · awal **5** · bukan-awal **118**. BNXUSDT
punya lubang AWAL dan bukan-awal sekaligus. Lima bentuk AWAL: BNXUSDT, ICPUSDT,
JUPUSDT, QTUMUSDT, TLMUSDT. Lubang **880** semesta / **877** dalam penyebut / **3** tak
dikenal. Dari 945 MATI di luar kohort: **386** kehilangan funding, **559** berfunding.

## Jumlah uji — terukur

**1377, kini DUA PULUH SATU bacaan berjejak di berkas ini.** Bacaan 1–15 tercatat di
v16 dan v17 dan tidak diulang; yang terbaru:

16. blob **`990502c707237fa0ef8e5314471ea5277dac19c5`**, run **30591338909**, commit
    **`72fe177c`** (UKUR v17), **23:42:47Z**, kode 0, `… in 0.56s`.
17. blob **`b6d02273aa15ebee7736f79883283f4906c447b7`**, run **30592159959**, commit
    **`05f6f72e`** (STATE v59), **2026-07-30T23:59:10Z**, kode 0, `… in 0.52s`.
18. blob **`3f299eaf4383604666f30c3448a32d38e57b1742`**, run **30592559253**, commit
    **`bb565f4c`** (EKOR v18), **2026-07-31T00:06:48Z**, kode 0, `… in 0.62s`.
19. **[v19]** blob **`a185f32a80471ea9f76c72415cacf3c4f06dfeda`**, run **30593086004**,
    commit **`51c65e2a`** (UKUR v18), **00:17:08Z**, kode 0, `… in 0.57s`.
20. **[v19]** blob **`b6835432ff25e8482781f13018c17b9f080ad510`**, run **30594157668**,
    commit **`8345668e9a8f0e01bcbe86fd9d0f60f4709fd834`** (STATE v60), **00:39:46Z**,
    kode 0, `1377 tests collected in 0.48s`.
21. **[v19]** blob **`87677ef656439ff30eb0c1a6788a5c324fdca702`**, run **30595169680**,
    commit **`b8877a2710544723ce81fc44ad505fa08fb7828b`** (EKOR v19),
    **2026-07-31T01:01:01Z**, kode 0, `1377 tests collected in 0.47s`.

Turunan: 1341 + **36** butir `tests/test_selisih_lilin.py` = **1377** ✅
**Rentang waktu kutip 0,40s–0,67s DILARANG dibaca sebagai pengukuran apa pun tentang
repo** — ia keadaan mesin CI, bukan besaran riset.

Riwayat: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 → 984 →
1044 → 1100 → 1168 → 1233 → 1297 → 1341 (enam run) → **1377** (dua puluh satu run
berjejak di berkas ini).

**Aturan 57: beruntun 4 dari 4** sesudah PUTUS di 26/27. Ia **mencacah, bukan menaksir**.

### Aturan 38 — ordinal, kini sampai ke-65

| ke- | CI | run | commit | blob | jejak |
| --- | --- | --- | --- | --- | --- |
| 59 | 1377 | 30590948580 | `c0877746` | `5f62452d` | UKUR v17, STATE v59 |
| 60 | 1377 | 30591338909 | `72fe177c` | `990502c7` | STATE v59, EKOR v18 |
| 61 | 1377 | 30592159959 | `05f6f72e` | `b6d02273` | EKOR v18 |
| 62 | 1377 | 30592559253 | `bb565f4c` | `3f299eaf` | UKUR v18 |
| **63** | **1377** | **30593086004** | **`51c65e2a`** | **`a185f32a80471ea9f76c72415cacf3c4f06dfeda`** | **STATE v60, EKOR v19** |
| **64** | **1377** | **30594157668** | **`8345668e`** | **`b6835432ff25e8482781f13018c17b9f080ad510`** | **EKOR v19** |
| **65** | **1377** | **30595169680** | **`b8877a2710544723ce81fc44ad505fa08fb7828b`** | **`87677ef656439ff30eb0c1a6788a5c324fdca702`** | **berkas ini** |

**Pemakaian berjalan = ke-enam puluh lima.** Ke-65 dibaca **2026-07-31T01:01:01Z**, kode
keluar **0**, atas push **EKOR v19** — `commit` **COCOK pada percobaan pertama**.

**[v19] Panjang deret berjejak tanpa laporan hangus, dengan aritmetika terbuka
(kesalahan dokumen butir 17):** ke-42..ke-65 → 65 − 42 = 23; 23 + 1 = **24 pembacaan
berturut**.

### ATURAN 90 — RESMI (diresmikan di STATE v60)

> **Aturan 90.** Laporan `reports/ci_terakhir.json` sah bagi sebuah push **hanya bila**
> medan `commit` cocok dengan SHA push itu. Bila tidak cocok, laporan itu milik push
> sebelumnya; pembacaan **WAJIB diulang** dan laporan yang tidak cocok **DILARANG
> dicatat**.

| kejadian | push | blob salah yang muncul | `commit` terbawa | milik ke- |
| --- | --- | --- | --- | --- |
| 1 | STATE v58 | `5b433a93` | `9b01c06e` | ke-57 |
| 2 | STATE v59 | `990502c7` | `72fe177c` | ke-60 |
| 3 | EKOR v18 | `b6d02273` | `05f6f72e` | ke-61 |

**Sejak diresmikan, aturan 90 dipakai EMPAT kali** (ke-62, ke-63, ke-64, ke-65) dan
**tidak sekali pun menangkap laporan salah** — keempatnya cocok pada percobaan pertama.
**DILARANG menyebut aturan 90 "teruji".** Aturan yang belum pernah menyala bukanlah
aturan yang terbukti; ia hanya aturan yang belum diuji.

**Bot CI** menambah satu commit di atas tiap push pemicu — deterministik, **DILARANG
dihitung kemenangan**. Terbaru: `9e43911b` (STATE v59) · `64b03bdb` (EKOR v18) ·
`8e0b39a5` (UKUR v18) · `e08a0a2a` (STATE v60) · **`4bf883c433d492fa76f84707dec6320162ec61c0`**
(EKOR v19). **Push `journal/**` dan `decisions/**` TIDAK menyalakan CI** — jurnal 148,
149, 150, 151 tidak menghasilkan commit bot, terukur dari `paths-ignore` pada `ci.yml`.

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

**Blob modul:** `gerbang_1m.py` **`c8cc54c84a57173ef2e426c317d6ac50734e9b4a` (DIBACA
UTUH, pustaka murni)** · `resample.py` `66a4b177` · `silang_funding.py` V2
`42c3aa9dc2c16220b79cf9c9e46979dd000fd393` (DIBACA UTUH) · `lubang_tengah.py` V2
`4d3beaf18c070d2931044c50dd5a354d75eaceb8` (DIBACA UTUH) · `kehidupan_arsip.py`
`318a5cb187406d16cfd3385d653bed905f632934` (DIBACA UTUH) · `pulihkan.py`
`a9e6eab7cc47555dfed919ac63044ff2eadc4893` (DIBACA UTUH) ·
**`lubang_awal.py` `8c36943da222dfa262b3b9f2117bf72dc801681d` (DIBACA UTUH [v19] —
`BATAS_BARIS_LAPORAN = 60`)** ·
**`bulan_absen.py` `10279d721d66a86b6d265badf81ada3204648f69` (DIBACA UTUH [v19] —
TANPA pembatas baris)** · `ukur_baris.py` V5 `3ebaa9f9` (DIBACA UTUH) ·
`selisih_lilin.py` `d19bdb5fe67e0bd9c1b141d7fb7cc6dcd089c5f2` · `sisa_defisit.py`
`7aa0e6d7` · `keterisian_lilin.py` `3f80ffa7` · `bulan_pertama.py` `b9bd00ac` ·
`irisan_byte.py` `2dbe3d55` · `byte_semesta.py` `ff68e4be` · `lubang_tebing.py`
`575e777e` · `kohort_ekor.py` V4 `c9b63bbe` · `bentangan_kohort.py` V2 `f4eae57a` ·
`sebab_bangkit.py` `fd5a1dc4` · `tersisip_semesta.py` `8a648838` · `kehidupan.py`
`f49abb2b` · `funding.py` `8d4b1f82` · `rilis.py` `2e44530c` · `karantina_semesta.py`
`46e7c46b` · `arsip.py` `0104958b` · `semesta_kuota.py` `7288b030` · `kebangkitan.py`
`446321ee` · `penyebut_tahun.py` `265aad00` · `anatomi_tengah.py` `04279335` ·
`__init__.py` `64d85584`.

**TIDAK ADA modul yang diketahui menulis `reports/semesta_rentang.json`** (utang ukur 22).

`ci.yml` = **`c79497b2c812679eaa69aee5b3160eac9f5c5fb7`** (paths-ignore `journal/**`,
`decisions/**`, `hipotesis/**`, `reports/**`; push ke `lux_ai/**`, `tests/**`, `STATE*`,
`PROMPT*` MENYALAKAN CI — **terkonfirmasi delapan belas kali berturut**).
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
terukur.** **`tests/test_gerbang_1m.py` — BELUM DIBACA; cacah butirnya TIDAK DIKETAHUI.
[v19] PERINGKATNYA NAIK KE ATAS:** ia penjaga salinan rumus gerbang, dan utang ukur 25
tidak dapat dibayar tanpanya.

**POLA WORKFLOW TRIO — TERVERIFIKASI DARI SUMBER** (`selisih_lilin.yml`): `name`,
`on.push.paths` **SATU** entri, `permissions: contents: write`, job `ukur` di
`ubuntu-latest`, checkout@v4 + setup-python@v5 (3.11),
`pip install numpy pandas pyarrow pyyaml`, langkah `jalan` dengan `set +e` → `KODE=$?` →
`echo "kode=$KODE" >> "$GITHUB_OUTPUT"` → `exit 0`, langkah `catat status`, langkah
`dorong laporan` (`[skip ci]`, `git pull --rebase`), penutup
`exit ${{ steps.jalan.outputs.kode }}`. **Aturan 55 LUNAS untuk berkas itu.**

## API terverifikasi

API lama (v37–v12) tetap berlaku. `gerbang_1m` diuraikan di bagiannya sendiri di atas.

**[BARU v19] `bulan_absen` V1** (`10279d72…`, DIBACA UTUH): `VERSI = 1` ·
`KELUARAN = "reports/bulan_absen.json"` ·
`KELUARAN_RINGKAS = "reports/bulan_absen_ringkas.json"` · `PENYEBUT_TERCATAT = 19586` ·
`NAMA_PENYEBUT_TERCATAT = 787` · `KENDALI_NAMA = ("BTCUSDT","ETHUSDT")` ·
`KENDALI_BULAN_MIN = 60` · `ABSEN_PASANGAN_JURNAL_113 = 12` · **`R288_BNX_ABSEN = 3`** ·
`R288_SAMA_MIN = 7` · `R288_JUMLAH_SEMESTA = 12` ·
`PEMBEDA = ("gagal_gerbang","tak_diterbitkan_arsip","tak_terukur")`.
**TIDAK ADA pembatas baris** — `baris_berabsen` LENGKAP. Docstring memuat praregistrasi
**R-288** dan menyebut **R-290**; keduanya **belum diadjudikasi**.
**PERINGATAN:** `R288_BNX_ABSEN = 3` adalah **tetapan ramalan**, bukan pengukuran.

**[BARU v19] `lubang_awal` V1** (`8c36943d…`, DIBACA UTUH):
**`BATAS_BARIS_LAPORAN = 60`** · `R305_PITA_BUTIR_1=(0.55,0.95)` ·
`R305_MINIMAL_PENYEBUT_BUTIR_1=100` · `R305_PITA_BUTIR_2_CACAH=(20,120)` ·
`R305_MINIMAL_BAGIAN_BUTIR_2=0.80`. `cacah_bulan` dihitung sebagai `len(urut)` atas
penyebut 19.586 — **itulah sebab `bagian_butir_1` tautologis 1.0**. Medan
`mati_tidak_setelah_lubang_bukan_awal` memakai `<=` — **DILARANG dipakai untuk klaim
arah** (aturan 80). Docstring memuat **praregistrasi R-305**.

**`lubang_tengah` V2** (`4d3beaf1…`, 23.745 B): `VERSI=2` ·
`KELUARAN="reports/lubang_tengah.json"` · `TENGAH_TERCATAT=6` · `SIMBOL_H_A010` lima
nama · `SIMBOL_TENGAH_TERCATAT=["BTCSTUSDT","LITUSDT"]` · `SIMBOL_H_A011="LITUSDT"` ·
`RENTANG_H_A011=("2026-01","2026-06")` · `BERKAS_DICAP` empat nama. **Enam belas
fungsi**; **lima penggugur**; **enam praregistrasi di docstring**.

**`pulihkan` V2** (`a9e6eab7…`, 14.839 B): `VERSI=2`, `TOTAL_PECAHAN=8`,
`AKAR_UNDUH="data/unduh"`, `AKAR_PULIH="data/pulih"`; `sidik_kode()` mencap
`["pulihkan.py","rilis.py"]`; **`cacah_baris_parquet` = `metadata.num_rows`**;
`periksa_keluarga` dipanggil **dua kali**.

**`kehidupan_arsip` V1** (`318a5cb1…`, 19.281 B): `VERSI=1`, `TOTAL_PECAHAN=8`,
`KENDALI_CACAH=3`, `KOLOM_VOLUME="volume"`, `KOLOM_TRANSAKSI="trades"`;
`peta_parquet` **melewatkan baris `parquet_karantina`**. Keluarannya
`reports/kehidupan_arsip_<i>.json` **991.422–1.261.637 B — MUSTAHIL dibaca utuh lewat
alat. DICORET dari daftar bahan ramalan.**

**`selisih_lilin` V1** (`d19bdb5f…`): `LILIN_LANGSUNG_TERCATAT=839325999` ·
`BARIS_PARQUET_TERCATAT=839842134` · `SELISIH_TERCATAT=516135` ·
`AMBANG_HIDUP_KECIL=97634` · `INVARIAN` **8** kunci · `R312_PITA_BUTIR_1=(12,120)` ·
`R312_PITA_BUTIR_2=(0.50,0.865)`. `kode_keluar` **2** bila `cacah_berselisih <= 0`.

**`silang_funding` V2** (`42c3aa9d`): `PENYEBUT_TERCATAT=19586`, `MATI_TERCATAT=1401`,
`KOHORT_TERCATAT=456`, `HIDUP_TANPA_FUNDING_TERCATAT=33`,
**`LUBANG_TAK_DIKENAL_TERCATAT=3`**,
`BENTUK_TERBITAN_FUNDING={"awal":48,"ekor":826,"tengah":6}`, `KENDALI_CACAH=3`.
**PERINGATAN KC-54:** medan itu memuat **cacah**, bukan identitas dan bukan arah waktu.
**Kode tidak pernah menjanjikan apa pun tentang waktu; dokumenlah yang menambahkannya.**

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
**`kohort_ekor` V4** (`c9b63bbe`): `TEBING="2025-07"`, `BULAN_DIHARAPKAN="2026-06"`,
`BATAS_SIMBOL=10`, `PAGU_MUNDUR=60`, `AMBANG_SEPI=0.5`. **Medan
`cacah_simbol_bangkit_dapat_diuji` = 0 DILARANG dibaca sebagai ketiadaan kebangkitan
(KC-53).**
**`ukur_baris` V5** (`3ebaa9f9`): `PAGAR_BARIS=800`, `BERKAS_DIUKUR` **21 nama**.
**Utang V6 hidup.**
**`kehidupan`** (`f49abb2b`): `AMBANG_SEPI=0.5`, `BULAN_MULAI="2025-07"`,
`BULAN_AKHIR="2026-06"`.

Sidik lain: `sebab_bangkit` `bafe4359…221a` · `tersisip_semesta` `9618fd19…c537c` ·
`bentangan_kohort` V2 `8ca6ebbe…f32c` · **`lubang_awal` `156499ce…f2362`** ·
**`bulan_absen` kode `0294eb3a…163088`, sumber `d2fc3bfb…14a3bd`** · `pulihkan` kode
seragam `76c27e3c…62d700`, manifes seragam `237ccf42…ba601`. Sidik manifes per pecahan:
`_0` `88d5704c` · `_1` `64311545` · `_2` `6bbc9990` · `_3` `b6f5f27e` · `_4` `d204f353` ·
`_5` `3b0e2d22` · `_6` `356ae3d6` · `_7` `2abc9c73`.

## Hipotesis

- H-A001 belum diuji · H-A002b GUGUR · H-A003 MENANG pada 3, GUGUR pada 9 · H-A004 tak
  dapat diuji · H-A005 GUGUR · H-A006 MENANG enam run · H-A008 MENANG dua kali · H-A009
  GUGUR · **H-A010 MENANG 5–0 (tabel pendukung dikoreksi konvensinya, vonis tetap)** ·
  **H-A011 TERBUKTI** · H-A012 MENANG · H-A013 MENANG 6–0 TAFSIR DICABUT · H-A014 MENANG
  9 dari 9 · H-A015 DIBATASI sebagai tafsir (KC-45) · H-A016 PENGAMATAN, BELUM DIUJI.
- **H-A017** DICABUT sebagai pola semesta; bukti lepas-tebing tinggal **1** simbol.
- **H-A018** — **BOLEH:** "bulan MATI menempati bagian KECIL byte semesta (**0,0177**)
  dan rata sekitar **4,3×** lebih kecil". **DILARANG:** "berkas kecil berarti pasar mati".
- **H-A019** DITERIMA TERBATAS; DILEMAHKAN oleh ADR-A018 kep. 6 tanpa tafsir pengganti.
- **H-A020, H-A021 [DIUSULKAN]** — uji **MUSTAHIL**, tidak ada bahannya.
- **H-A022 [TERBUKTI lewat R-313]** — yang terbukti **identitas himpunan**, bukan sebab.
- **[v19] H-A023 [DIUSULKAN — BERSYARAT dengan ARITMETIKA TERTUTUP]** — *selisih
  51 − 48 = 3 pada BNXUSDT dan `cacah_lubang_tak_dikenal` = 3 menunjuk himpunan
  simbol-bulan yang sama.*
  **Yang kini TERUKUR dan menutup:** ketiga bulan **BERNAMA** — 2022-04 (tepi),
  2022-06 dan 2022-08 (di dalam, `gagal_gerbang`); 51 − 50 = 1 dan 50 − 48 = 2;
  1 + 2 = 3 ✅. Nama itu **sama persis** dengan ketiga `lubang_tak_dikenal` pada
  `silang_funding.json`.
  **Yang membuatnya TETAP BERSYARAT:** keanggotaan penyebut diukur untuk **SATU** simbol.
  Untuk 786 simbol lain, kesamaan cacah **belum** terbukti kesamaan identitas.
  **DILARANG ditulis TERBUKTI.** Naiknya status v18→v19 adalah dari "arah konsisten"
  menjadi "aritmetika tertutup pada satu simbol" — **bukan** menjadi terbukti.
  Hipotesis berikutnya **H-A024**.

## Aturan 87 dan 90 RESMI; usulan 88, 89, 91

**Aturan 87 [RESMI].** Butir ramalan **turunan** wajib ditandai **TURUNAN**;
kemenangannya wajib diperkecil sendiri; kekalahannya dihitung penuh.
**[v19] Ditaati:** butir 4 R-318 (`rentang` = 50) ditandai TURUNAN di praregistrasinya,
dan kemenangannya **diperkecil sendiri** di jurnal 151 dan EKOR v19.

**Aturan 90 [RESMI di STATE v60].** Diuraikan penuh di bagian aturan 38 di atas.

**Usulan aturan 88 [BELUM RESMI].** Ramalan keseragaman tanpa mekanisme tertulis wajib
ditulis sebagai **sebaran**. **[v19] TIDAK bertambah** — tetap satu kejadian.

**Usulan aturan 89 [BELUM RESMI].** Setiap pita ramalan wajib menutup **ketiga sisi**
ruang nilainya, atau menyatakan mengapa satu sisi mustahil.
**[v19] MANFAATNYA kini TERUKUR** — pita butir 1 R-318 ditulis tiga sisi (kurang 0–1 /
tepat 2 / lebih ≥3) padahal sisi "lebih" tampak mustahil menurut aritmetika sendiri, dan
sisi itu **nyaris terpakai** (tetapan kode meramalkan 3). **Tetapi CACAT yang
melahirkannya masih SATU.** Meresmikan aturan atas dasar **manfaat** alih-alih **cacat
berulang** adalah **perubahan kebijakan**, bukan penerapan kebijakan — **wewenang
ADR-A022**, bukan wewenang lampiran ini.

**[BARU v19] Usulan aturan 91 [BELUM RESMI].** Ramalan yang butir-butirnya diturunkan
dari **satu arit