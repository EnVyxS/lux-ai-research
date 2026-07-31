# STATE lampiran UKUR — bagian 3 dari STATE (v18, milik STATE v59)

**Kedudukan berkas ini.** STATE dipecah tiga sejak v43 (KC-42). Pembagian berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, 83, 84, 85, 86 (a) dan (b), **87**;
   KC-1..**KC-55** resmi, **KC-56 diusulkan**.
2. **`STATE_LAMPIRAN_EKOR.md`** v18 (blob **`217beaeebd367309ea1a4a4d5ea3234887788b2b`**)
   — bagian 2: papan skor, ADR, catatan kejujuran.
3. **`STATE_LAMPIRAN_UKUR.md`** (berkas ini, v18) — bagian 3: pengukuran, modul,
   workflow, uji, API, hipotesis, koreksi bernomor.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) dan **`PROMPT_KELANJUTAN.md`** (blob
   `35beed44`) — **arsip; BUKAN sumber** (ADR-A018 kep. 9).

Dasar v18: UKUR v17 (blob **`94be0d2863a1a0972311cec9fd8ecb06d5720261`**, commit
**`72fe177c352f94f340574d0a0eaf0291a6408fda`**), dibaca UTUH pada giliran yang sama
sebelum berkas ini ditulis (aturan 52, pencegahan KC-43).

**Apa yang v18 bawa, disebut di muka.** v17 membawa angka **51** yang membatalkan
gambaran yang baru saja tersusun. **v18 membawa sesuatu yang lebih tajam: sebuah medan
yang selama satu giliran penuh hampir dibaca salah, dan yang menyelamatkannya bukan
kepandaian melainkan memeriksa simbol kedua.** `cacah_bulan` pada
`reports/semesta_rentang.json` **bukan** bentangan kalender — dan bila hanya BNXUSDT
yang diperiksa (51 = 51), kesimpulan sebaliknya akan lahir dan terdengar meyakinkan.
v18 juga membawa **pencabutan SEBAGIAN** sebuah larangan, **Koreksi 15**, dan
**pengakuan bahwa utang ukur 20 tidak terbayar** — hanya dipertajam.

## KESERASIAN VERSI — PULIH PENUH pada v59 / v18 / v18

- `STATE.md` **v59** — blob **`8f5bc472b81865bdabcb5be7c16bbdbac6505ec1`**, commit
  **`05f6f72e3bde9dd634ad6494eca0bc397bc0c7f1`**.
- `STATE_LAMPIRAN_EKOR.md` **v18** — blob **`217beaeebd367309ea1a4a4d5ea3234887788b2b`**,
  commit **`bb565f4cb2bc0ef8d7b2c72ece8f835c74613422`**.
- `STATE_LAMPIRAN_UKUR.md` **v18** — berkas ini.

Keserasian **PECAH** begitu STATE v59 naik (v59/v17/v17 lalu v59/v18/v17) dan
**dipulihkan oleh berkas ini**. Ketertinggalan yang dicatat STATE v59 dan EKOR v18 —
bahwa berkas ini masih berkepala "milik STATE v58" dan **tidak memuat** pembacaan
`semesta_rentang.json`, definisi terukur `cacah_bulan`, BNXUSDT kontinu **51**, TLMUSDT
kontinu **60**, **Koreksi 15**, usulan **KC-56**, kesalahan dokumen butir **17**, status
baru H-A023, maupun aturan 38 ke-60..ke-62 — **LUNAS oleh berkas ini**. **Satu berkas
per push tetap MENGIKAT** (KC-42, KC-43).

**Tentang push berkas ini:** ia di akar repo sehingga menyalakan `ci.yml`. Tidak satu
pun `tests/**` berubah, jadi cacah uji tetap **1377** — ramalan **deterministik**,
**MUDAH**, TIDAK masuk papan skor, TIDAK menambah beruntun aturan 57. **Laporannya
WAJIB dibaca sebelum push akar berikutnya** (aturan 38 **ke-63**).

**Angka yang TIDAK berubah dari v44/v45/v6/v7** (tidak diulang): taksonomi 9 kelas,
bulan ABSEN 11, H-A013..H-A015, terhenti, SETTLED. Rinciannya di v44 (blob
`d302caff`), v45 (`eb826817`), v6 (`27e59a79`), v7 (`4e7fb65b`).

## KOREKSI KC-41 — BACA SEBELUM MENGUTIP BERKAS INI

Kelima belas koreksi **tetap dicantumkan** karena semuanya soal dokumen kami sendiri,
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
**[v18] Pencabutan itu kini punya penyangkalan TERUKUR, bukan sekadar penalaran:**
ketiga bulan itu **ADA** pada `semesta_rentang.json`, di dalam rentang kontinu
2022-04..2026-06.

**Koreksi 14 [v17] — `bulan_per_simbol` dibaca sebagai DAFTAR, isinya CACAH.**
Praregistrasi R-316 menanyakan kehadiran dua bulan **bernama**; berkasnya **tidak
memuat satu nama bulan pun**. **KC-54 kejadian KETIGA.**

| kejadian | medan | dibaca sebagai | sebenarnya |
| --- | --- | --- | --- |
| 1 (Koreksi 11 butir 2) | label gugus `2022-05` / `2024-05` | bulan lubang tengah | `bulan_klines_pertama` BNXUSDT |
| 2 (Koreksi 13) | `lubang_tak_dikenal` | posisi **waktu** lubang | kegagalan pasangan terhadap penyebut 19.586 |
| 3 (Koreksi 14) | `bulan_per_simbol` | daftar bulan | **cacah** bulan |

### **Koreksi 15 [BARU v18] — `cacah_bulan` nyaris dibaca sebagai BENTANGAN KALENDER**

`reports/semesta_rentang.json` memberi tiap simbol tiga medan: `bulan_pertama`,
`bulan_terakhir`, `cacah_bulan`. **Definisi `cacah_bulan` tidak tertulis di berkas itu,
dan tidak ada modul yang diketahui menulisnya** (utang ukur 22 baru).

Untuk **BNXUSDT** angkanya cocok sempurna dengan bentangan: 2022-04..2026-06 →
(2026−2022)×12 = 48; +(6−4) = 50; +1 = **51**, dan `cacah_bulan` juga **51**. Bila
pemeriksaan berhenti di situ, kesimpulan "`cacah_bulan` = bentangan kalender" akan
ditulis, terdengar masuk akal, dan **salah**.

**Dua tandingan hitung tangan membatalkannya:**

| simbol | bentangan (tangan) | `cacah_bulan` | selisih |
| --- | --- | --- | --- |
| BNXUSDTSETTLED | 2022-04..2023-02 → **11** | **6** | **5** |
| TLMUSDTSETTLED | 2022-01..2023-03 → **15** | **9** | **6** |

**Maka `cacah_bulan` mencacah bulan yang BENAR-BENAR ADA, bukan panjang rentang.**
Konsekuensinya justru menguatkan: karena medan ini **mampu** menunjukkan selisih, maka
selisih **nol** pada BNXUSDT adalah **pengukuran, bukan ketiadaan alat** — penerapan
aturan 50 dengan **kendali positif tertulis**.

**Beda dengan Koreksi 11, 13, dan 14:** ketiganya cacat **nama medan** (KC-54). Koreksi
15 bukan itu — nama `cacah_bulan` sudah jujur menyebut dirinya "cacah". Yang hampir
menipu adalah **kemiripan angka pada satu simbol**. Karena itu ia **TIDAK** dihitung
sebagai KC-54 kejadian keempat, dan pencatatan itu disengaja agar cacah kejadian KC-54
tidak digelembungkan demi kesan pola.

**Kelas cacatnya:** kerabat **KC-47** (satu simbol menyamar sebagai bukti umum).
**Penangkal yang bekerja:** memeriksa simbol kedua **sebelum** menulis definisi.

**Bacaan jujur atas Koreksi 4, 9, 10, 11, 12, 13, 14, dan 15 bersama-sama:** cacat yang
bertahan paling lama di riset ini bukan salah hitung, melainkan **tafsir yang terdengar
masuk akal atas angka yang benar**; sejak v15 bertambah **label yang terdengar masuk
akal atas medan yang benar**; dan sejak v18 bertambah lagi **kecocokan angka pada satu
contoh yang terdengar seperti definisi**.

## BATAS KEKUATAN ATURAN 52 — DIPERSEMPIT, BUKAN DICABUT

> Pembacaan ulang **dokumen sendiri** lemah terhadap penalaran cacat: ia membaca
> kalimat yang sudah diyakini benar. Pembacaan **kode** kuat terhadapnya.

**[v16] Bukti ketiga:** bacaan `lubang_tak_dikenal` bertahan melewati **empat** berkas
akar dan runtuh dalam **satu** pembacaan laporan.
**[v17] Bukti keempat:** R-316 butir 1 tidak dapat diadili sama sekali.
**[v18] Bukti kelima, dan yang paling telanjang:** kalimat "Tujuh belas pembacaan
berturut (ke-42..ke-57)" lolos dari **dua puluh empat** pembacaan ulang berturut,
padahal 57 − 42 = 15; 15 + 1 = **enam belas**. Angkanya dikutip benar; yang salah
aritmetika di antaranya. **Yang menangkapnya bukan pembacaan melainkan aritmetika
tangan yang dipaksakan atas angka yang sudah ada di kalimat itu sendiri.**
**DILARANG** menulis bahwa aturan 52 menjaga mutu penalaran **atas dokumen**; yang
dijaganya **kesetiaan salinan**.

**Penangkal wajib sejak v59:** setiap panjang deret ditulis bersama aritmetika
`akhir − awal + 1` secara terbuka. Diterapkan di seluruh berkas ini.

## [BARU v18] SEMESTA RENTANG — bahan baru, terbaca 95%

Sumber: **`reports/semesta_rentang.json`**, blob
**`8d5bd06ca4073dac8a8ef7841d81824427cc8e63`**, **110.662 B**, dibaca pada ref
**`24b53ba5d1bab273c0ac457c3ee8f65b94915ecb`**.

**BATAS ALAT YANG WAJIB DISEBUT SETIAP KALI BERKAS INI DIKUTIP.** Verbatim:
`This result has been truncated (showing 95% of full).` Potongan hilang di **tengah**,
kira-kira abjad **P–R** (antara `PLTRUSDT` dan `ROBOUSDT`). **Cacah entri `rentang`
DILARANG diklaim terukur** dan tidak dihitung (aturan 66).

**Struktur, disalin apa adanya sebelum ditafsirkan:** satu kunci akar `rentang`; tiap
simbol → tiga medan `bulan_pertama`, `bulan_terakhir`, `cacah_bulan`. Entri terakhir
yang terbaca: `"龙虾USDT"`.

**TANPA `waktu_utc`. TANPA medan sidik apa pun.** Ketiadaan itu **terukur**, sebab ekor
berkas terbaca utuh — bukan dugaan dari bagian yang hilang.

| simbol | `bulan_pertama` | `bulan_terakhir` | `cacah_bulan` | bentangan (TURUNAN, tangan) | lubang |
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

**Tiga temuan terukur:**

1. **`cacah_bulan` bukan bentangan** (Koreksi 15) — dua tandingan SETTLED.
2. **BNXUSDT KONTINU, nol lubang.** Aritmetika tangan: (2026−2022)×12 = 48; +(6−4) =
   50; +1 = **51** = `cacah_bulan`. Maka **2022-04, 2022-06, dan 2022-08 SEMUANYA ADA**
   pada semesta rentang.
3. **TLMUSDT KONTINU 60 bulan**, sehingga kekosongan **2023-03** **bukan** absennya
   bulan melainkan **kekosongan isi**. Utang ukur 7 **menyempit, tidak lunas**.

**Kecocokan silang dengan semesta 1m:** `bulan_per_simbol` = `cacah_bulan` pada **dua**
simbol — BNXUSDT **51 = 51**, BNXUSDTSETTLED **6 = 6**. **PETUNJUK, BUKAN BUKTI
identitas medan** (KC-23, KC-52 tetap terbuka). Dua titik bukan sebaran, dan salah satu
berkas tak bertanggal.

### Yang DILARANG disimpulkan dari berkas ini

1. **DILARANG** menyebutnya mengukur "semesta 1m"; hubungannya dengan
   `semesta_bulan_1m.json` **belum diukur**.
2. **DILARANG** menyimpulkan hanya simbol SETTLED yang berlubang — empat simbol
   dihitung tangan, tidak ada pemindaian, dan 5% berkas tak terbaca (KC-47).
3. **DILARANG** mengklaim berapa banyak simbol berlubang.
4. **DILARANG** membandingkan angkanya secara keserempakan dengan laporan lain — ia
   **tak bertanggal** (**KC-56**).
5. **DILARANG** memindahkan sifat `cacah_bulan` ke `bulan_per_simbol` atau sebaliknya.
6. **DILARANG** menyatakan gerbang menjatuhkan bulan mana pun.
7. **DILARANG** menyamakan "ada di semesta rentang" dengan "ada di penyebut 19.586".

### PENCABUTAN SEBAGIAN — larangan "51 mencakup 2022-04"

UKUR v17 melarang menyatakan bahwa **51 mencakup 2022-04** dengan alasan "belum
diukur". **Larangan itu kini DICABUT SEBAGIAN:**

- **DICABUT** untuk medan **`cacah_bulan` pada `semesta_rentang.json`**: di sana 51
  terbukti kontinu 2022-04..2026-06, sehingga **2022-04 termasuk**. Ini **terukur**.
- **TETAP BERLAKU PENUH** untuk medan **`bulan_per_simbol` pada
  `semesta_bulan_1m.json`**: berkas itu **tidak memuat satu nama bulan pun**, sehingga
  cakupan 51-nya **tidak dapat diperiksa** dan **DILARANG diklaim**.

**Kedua angka kebetulan sama-sama 51. Kesamaan itu DILARANG dipakai untuk memindahkan
pencabutan dari medan pertama ke medan kedua.**

### [BARU v18] KC-56 [DIUSULKAN] — laporan tak bertanggal dianggap serempak

Bila sebuah laporan tidak memuat `waktu_utc`, jaraknya terhadap laporan lain **tidak
diketahui — bukan nol**. **Angka kasus asal (aturan 42):** `semesta_rentang.json`
**tanpa** `waktu_utc`; `semesta_bulan_1m.json` **2026-07-28T09:44:48Z`**;
`silang_funding.json` **2026-07-29T08:17:55Z** — dua yang bertanggal saja berjarak
hampir **23 jam**. **Penangkal:** cari `waktu_utc` sebelum membandingkan; bila tidak
ada, tulis **"tak bertanggal"** di sebelah setiap angka yang dikutip. Baru **satu**
kejadian — ADR-A019 kep. 3 melarang meresmikannya. **KC berikutnya KC-57.**

## SEMESTA BULAN 1M — angka 51 dan apa yang TIDAK dikatakannya (dari v17)

Sumber: **`reports/semesta_bulan_1m.json`**, blob
**`a1a6d3f0f13dd7100a91853cadfcaa9a5620fee3`**, **18.884 B**, `waktu_utc`
**2026-07-28T09:44:48Z**. **TERBACA UTUH.** Dua kunci tingkat atas: `bulan_per_simbol`
(peta simbol → **satu bilangan bulat**) dan `waktu_utc`. **Tidak ada nama bulan.**
Cacah entri peta **TIDAK dihitung tangan; DILARANG dikutip terukur** (aturan 66).

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

**[v18] Sumber KEEMPAT kini setuju dengan 51** (`cacah_bulan`, tak bertanggal) — tetapi
**kesepakatan dua sumber BUKAN pendamaian**: keduanya mengukur himpunan yang belum
terbukti sama dengan penyebut 19.586, dan **48 tetap tidak terdamaikan**.

**CATATAN KESERAMPAKAN yang WAJIB disebut:** semesta 1m lahir 2026-07-28T09:44:48Z,
`silang_funding.json` lahir 2026-07-29T08:17:55Z — selisih hampir **23 jam**; semesta
rentang **tak bertanggal**. **Ketiganya bukan pengukuran serempak.**

### Yang DILARANG disimpulkan

1. **DILARANG** menyatakan tiga bulan selisih itu **adalah** 2022-04 / 2022-06 /
   2022-08. **Kesamaan cacah bukan kesamaan identitas.**
2. **DILARANG** menyatakan gerbang menjatuhkan bulan mana pun.
3. **DILARANG** menyamakan "tidak ada di penyebut" dengan "dijatuhkan gerbang".
4. **Aturan 36 TIDAK diberi kasus keempat** oleh kesamaan 3 = 3, **maupun** oleh
   kecocokan 6 = 6 dan 51 = 51: satu berkas tak bertanggal, dua titik bukan sebaran.
   Memasukkannya = KC-38.

### Adjudikasi R-316 — FINAL

| butir | ramalan | terukur | vonis |
| --- | --- | --- | --- |
| 1 | 2022-06 dan 2022-08 tidak hadir | **mustahil dinilai** | **TIDAK TERADJUDIKASI** (syarat gugur (c)) |
| 2 | cacah bulan BNXUSDT = **48** | **51** | **MELESET** (+3) |
| 3 [TURUNAN] | cacah **< 50** | **51** | **MELESET** (pita cacat → KC-55) |
| 4 (MUDAH) | berkas terbaca utuh | terbaca utuh | tidak masuk lajur |

Papan skor **321**, disahkan di EKOR v17, **tidak bergerak di v18** — tidak ada
adjudikasi, sebab bahan dibuka tanpa praregistrasi (aturan 29).

## `gerbang_1m.py` — DIBACA UTUH, utang ukur 18 LUNAS (dari v17)

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

**[v18] Catatan yang menguat:** karena `semesta_rentang.json` **tanpa sidik kode**, ia
**tidak dapat** dipastikan sebagai keluaran modul pemanggil gerbang — atau modul mana
pun. **Tidak ada satu medan pun di repo yang menamai klausa pelanggaran per
simbol-bulan.**

## SILANG FUNDING — tiga lubang tak dikenal (tidak berubah)

Sumber: **`reports/silang_funding.json`**, blob
**`b61fe8b3bcabbfce435dd5e5f78fc367f6bef617`**, `waktu_utc` **2026-07-29T08:17:55Z**.

**BATAS ALAT YANG WAJIB DISEBUT SETIAP KALI.** Verbatim:
`This result has been truncated (showing 54% of full).` Bagian tengah larik
**`baris_mati`** TIDAK TERLIHAT → **cacah total `baris_mati` DILARANG diklaim terukur**
(utang verifikasi 39, utang ukur 17).

| # | simbol | bulan | di dalam rentang klines? | **[v18] ada di semesta rentang?** |
| --- | --- | --- | --- | --- |
| 1 | **BNXUSDT** | **2022-04** | **TIDAK** | **YA** |
| 2 | **BNXUSDT** | **2022-06** | **YA** | **YA** |
| 3 | **BNXUSDT** | **2022-08** | **YA** | **YA** |

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

Butir 1 **TEPAT** (**1**, BNXUSDT) · butir 2 **MELESET** (**1 dari 3**) · butir 3 MUDAH.
**DILARANG ditulis ulang sebagai SEPARUH.** Syarat gugur (e) MENYALA.

## KC-18 — semesta kehidupan

Atas **19.586** simbol-bulan lolos gerbang: **1.401 MATI** (7,153%), **98 SEPI**,
**18.087 HIDUP**. Dari 1.401 MATI: 842 kehilangan funding, 559 tetap berfunding.
`cacah_simbol_tanpa_hidup` **18**. 18.087 + 98 = 18.185, + 1.401 = **19.586** ✅

**Pembelahan [v9]:** **787** bulan PERTAMA + **18.799** bukan-pertama = 19.586 ✅
**Pembelahan MATI [v10]:** 1.392 penuh + **9** tak penuh = 1.401 ✅
**Pembelahan [v11]:** 18.799 − 1.401 = **17.398**; 17.284 penuh + **114** berdefisit ✅
**Pembelahan [v13]:** rilis parquet **19.598** = 19.586 lolos + **12** karantina;
`kehidupan_arsip.peta_parquet` **melewatkan baris `parquet_karantina`**.

**Pembelahan ketiga atas lubang funding:**

| kelas bentuk | seluruh semesta | di dalam penyebut | selisih |
| --- | --- | --- | --- |
| awal | **48** | **45** | **3** |
| ekor | **826** | **826** | 0 |
| tengah | **6** | **6** | 0 |
| **jumlah** | **880** | **877** | **3** |

**[v18] PERINGATAN YANG MENGERAS.** **19.586** adalah penyebut **lolos gerbang**.
Semesta 1m **bukan** himpunan yang sama, dan semesta rentang **juga belum terbukti**
sama dengan keduanya. BNXUSDT: **51** (rentang, tak bertanggal) · **51** (1m) · **48**
(penyebut). **Selisih untuk simbol lain BELUM DIUKUR dan DILARANG DITAKSIR.**
**Yang belum diperiksa dan menjadi utang baru:** apakah setiap bulan penyebut BNXUSDT
termuat di dalam semesta rentang (utang ukur 23).

## LUBANG TENGAH — POROS TUNTAS

Sumber: **`reports/lubang_tengah.json`**, blob
**`39cd1caacedc4d49ba23c91c80f553bb9fb135a6`**, **11.014 B**, dibaca UTUH.
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
atau `2024-05`.**

**[v18] BTCSTUSDT terukur KONTIGU 64 bulan pada semesta rentang** (2021-03..2026-06 →
bentangan 64 = `cacah_bulan` 64). **Keserian dengan tebing tetap BELUM diukur dan
DILARANG diklaim.**

**H-A010 MENANG 5–0:**

| simbol | rentang lubang awal | `cacah_bulan_klines` | `cacah_lubang` |
| --- | --- | --- | --- |
| BNXUSDT | 2022-05 → 2023-02 | 48 | 19 |
| ICPUSDT | 2021-05 → 2022-09 | 62 | 16 |
| JUPUSDT | 2024-01 → 2024-02 | 30 | 1 |
| QTUMUSDT | 2020-02 → 2020-03 | 77 | 1 |
| TLMUSDT | 2021-07 → 2023-03 | 60 | 20 |

**[v18] CATATAN SILANG YANG WAJIB DITAHAN, kini BERLIPAT LIMA.** Baris BNXUSDT —
`cacah_bulan_klines` **48**, mulai **2022-05** — adalah medan yang sama yang: (a) di v15
berpindah menjadi nama poros "gugus 2022-05" (Koreksi 11); (b) di v16 menutup jembatan
50 lawan 48; (c) di v17 dibantah oleh **51** dari semesta 1m; **(d) di v18 dibantah lagi
oleh semesta rentang yang mulai 2022-04, bukan 2022-05.** Satu medan, lima pemakaian,
dua di antaranya keliru sebelum diukur.
**Perhatikan bulan mulanya:** semesta rentang **2022-04**, klines penyebut **2022-05**.
**Selisih satu bulan itu terukur, dan sebabnya DILARANG diklaim.**

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
  **[v18] Bulannya terukur ADA** pada semesta rentang (TLMUSDT kontinu 60);
  **kekosongan itu soal ISI, bukan soal keberadaan bulan.**
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
**bukan** bulan pertama simbol itu di bursa. Perbedaan keduanya BELUM diukur (ADR-A016
kep. 6). **[v18] Utang ini NAIK NILAI LAGI dan kini punya contoh terukur:** BNXUSDT
mulai **2022-04** pada semesta rentang tetapi **2022-05** pada klines penyebut.

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

**1377, kini DELAPAN BELAS bacaan berjejak di berkas ini.** Bacaan 1–12 tercatat di v16
dan v17 dan tidak diulang; yang terbaru:

13. blob **`5b433a93a3f0d3bb2cded75a5c0379c4a557ae3d`**, run **30589452976**, commit
    **`9b01c06e`** (UKUR v16), **23:07:02Z**, kode 0, `… in 0.55s`.
14. blob **`9718bf98caafc59349465ff55b9755e4ea309ac3`**, run **30590593816**, commit
    **`839a0f17`** (STATE v58), **23:28:30Z**, kode 0, `… in 0.61s`.
15. blob **`5f62452da6ba9e52f1324f796b2dbb552332c8bc`**, run **30590948580**, commit
    **`c0877746`** (EKOR v17), **23:35:07Z**, kode 0, `… in 0.49s`.
16. **[v18]** blob **`990502c707237fa0ef8e5314471ea5277dac19c5`**, run **30591338909**,
    commit **`72fe177c`** (UKUR v17), **23:42:47Z**, kode 0, `… in 0.56s`.
17. **[v18]** blob **`b6d02273aa15ebee7736f79883283f4906c447b7`**, run **30592159959**,
    commit **`05f6f72e`** (STATE v59), **2026-07-30T23:59:10Z**, kode 0, `… in 0.52s`.
18. **[v18]** blob **`3f299eaf4383604666f30c3448a32d38e57b1742`**, run **30592559253**,
    commit **`bb565f4cb2bc0ef8d7b2c72ece8f835c74613422`** (EKOR v18),
    **2026-07-31T00:06:48Z**, kode 0, `1377 tests collected in 0.62s`.

Turunan: 1341 + **36** butir `tests/test_selisih_lilin.py` = **1377** ✅
**Rentang waktu kutip 0,40s–0,67s DILARANG dibaca sebagai pengukuran apa pun tentang
repo** — ia keadaan mesin CI, bukan besaran riset.

Riwayat: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 → 984 →
1044 → 1100 → 1168 → 1233 → 1297 → 1341 (enam run) → **1377** (delapan belas run
berjejak di berkas ini).

**Aturan 57: beruntun 4 dari 4** sesudah PUTUS di 26/27. Ia **mencacah, bukan menaksir**.

### Aturan 38 — ordinal, kini sampai ke-62

| ke- | CI | run | commit | blob | jejak |
| --- | --- | --- | --- | --- | --- |
| 56 | 1377 | 30588460935 | `32413935` | `34f88b37` | UKUR v16 |
| 57 | 1377 | 30589452976 | `9b01c06e` | `5b433a93` | jurnal 146, STATE v58 |
| 58 | 1377 | 30590593816 | `839a0f17` | `9718bf98` | EKOR v17 |
| 59 | 1377 | 30590948580 | `c0877746` | `5f62452d` | UKUR v17, STATE v59 |
| **60** | **1377** | **30591338909** | **`72fe177c`** | **`990502c707237fa0ef8e5314471ea5277dac19c5`** | **STATE v59, EKOR v18** |
| **61** | **1377** | **30592159959** | **`05f6f72e`** | **`b6d02273aa15ebee7736f79883283f4906c447b7`** | **EKOR v18** |
| **62** | **1377** | **30592559253** | **`bb565f4cb2bc0ef8d7b2c72ece8f835c74613422`** | **`3f299eaf4383604666f30c3448a32d38e57b1742`** | **berkas ini** |

**Pemakaian berjalan = ke-enam puluh dua.** Ke-62 dibaca **2026-07-31T00:06:48Z**, kode
keluar **0**, atas push **EKOR v18** — `commit` **COCOK**.

**[v18] Panjang deret berjejak tanpa laporan hangus, dengan aritmetika terbuka
(kesalahan dokumen butir 17):** ke-42..ke-62 → 62 − 42 = 20; 20 + 1 = **21 pembacaan
berturut**.

**[v18] JEBAKAN CI — KINI TIGA KEJADIAN.** Sesudah push STATE v58, pembacaan pertama
mengembalikan blob `5b433a93` (commit `9b01c06e`) — laporan ke-57 lama. Sesudah push
STATE v59, mengembalikan `990502c7` (commit `72fe177c`) — laporan ke-60 lama. Sesudah
push EKOR v18, mengembalikan `b6d02273` (commit `05f6f72e`) — laporan ke-61 lama.
**Ketiganya dikenali dan TIDAK dicatat.** **Laporan sah hanya bila medan `commit` cocok
dengan commit push yang baru.** Dengan tiga kejadian, ADR-A019 kep. 3 **terpenuhi**:
ini layak diajukan sebagai **aturan resmi** pada ADR-A022, dan **belum** diresmikan di
berkas ini karena peresmian aturan bukan wewenang lampiran UKUR.

**Bot CI** menambah satu commit di atas tiap push pemicu — deterministik, **DILARANG
dihitung kemenangan**. Yang terlihat pada rangkaian ini: `e271a711` (STATE v58) ·
`14f3316e` (EKOR v17) · `24b53ba5` (UKUR v17) · `9e43911b` (STATE v59) · `64b03bdb`
(EKOR v18).

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
`a9e6eab7cc47555dfed919ac63044ff2eadc4893` (DIBACA UTUH) · `ukur_baris.py` V5
`3ebaa9f9` (DIBACA UTUH) · `selisih_lilin.py`
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

**[v18] TIDAK ADA modul yang diketahui menulis `reports/semesta_rentang.json`.** Tidak
satu pun nama di daftar di atas terbukti sebagai penulisnya, dan berkas itu tanpa sidik
kode. **Utang ukur 22.**

`ci.yml` = **`c79497b2c812679eaa69aee5b3160eac9f5c5fb7`** (paths-ignore `journal/**`,
`decisions/**`, `hipotesis/**`, `reports/**`; push ke `lux_ai/**`, `tests/**`, `STATE*`,
`PROMPT*` MENYALAKAN CI — **terkonfirmasi lima belas kali berturut**).
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
terukur.** **`tests/test_gerbang_1m.py` — BELUM DIBACA; cacah butirnya TIDAK DIKETAHUI.**

**POLA WORKFLOW TRIO — TERVERIFIKASI DARI SUMBER** (`selisih_lilin.yml`): `name`,
`on.push.paths` **SATU** entri, `permissions: contents: write`, job `ukur` di
`ubuntu-latest`, checkout@v4 + setup-python@v5 (3.11),
`pip install numpy pandas pyarrow pyyaml`, langkah `jalan` dengan `set +e` → `KODE=$?` →
`echo "kode=$KODE" >> "$GITHUB_OUTPUT"` → `exit 0`, langkah `catat status`, langkah
`dorong laporan` (`[skip ci]`, `git pull --rebase`), penutup
`exit ${{ steps.jalan.outputs.kode }}`. **Aturan 55 LUNAS untuk berkas itu.**

## API terverifikasi

API lama (v37–v12) tetap berlaku. `gerbang_1m` diuraikan di bagiannya sendiri di atas.

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
- **H-A022 [TERBUKTI lewat R-313]** — yang terbukti **identitas himpunan**, bukan sebab.
- **[v18] H-A023 [DIUSULKAN, BELUM DIREGISTRASI, TIDAK DISKOR — status BERUBAH menjadi
  BERSYARAT]** — *selisih 51 − 48 = 3 pada BNXUSDT dan `cacah_lubang_tak_dikenal` = 3
  menunjuk himpunan simbol-bulan yang sama.*
  **Yang kini TERUKUR:** ketiga bulan (2022-04, 2022-06, 2022-08) **ADA** pada semesta
  rentang, dan **tidak ada** di penyebut 19.586. Arahnya konsisten dengan hipotesis.
  **Yang BELUM terukur, dan karenanya bukti bersifat BERSYARAT:** apakah **seluruh** 48
  bulan penyebut BNXUSDT termuat di dalam 51 bulan semesta rentang. Bila ada satu bulan
  penyebut yang tidak termuat, selisih 3 **tidak** sama dengan ketiga bulan itu.
  **DILARANG ditulis TERBUKTI.** Ujinya menuntut sumber yang menyebut **nama bulan
  penyebut** per simbol — sumber itu **masih belum ditemukan**.
  Hipotesis berikutnya **H-A024**.

## Aturan 87 RESMI; usulan 88 dan 89

**Aturan 87 [RESMI].** Butir ramalan **turunan** wajib ditandai **TURUNAN**;
kemenangannya wajib diperkecil sendiri; kekalahannya dihitung penuh.
**[v18] Ditaati:** seluruh bentangan kalender di berkas ini ditandai **TURUNAN**.

**Usulan aturan 88 [BELUM RESMI].** Ramalan keseragaman tanpa mekanisme tertulis wajib
ditulis sebagai **sebaran**. **[v18] TIDAK mendapat kejadian kedua** — tidak ada ramalan
baru.

**Usulan aturan 89 [BELUM RESMI].** Setiap pita ramalan wajib menutup **ketiga sisi**
ruang nilainya, atau menyatakan mengapa satu sisi mustahil. **[v18] TIDAK bertambah.**

**Catatan kejujuran melekat:** keduanya lahir **sesudah** kekalahan. **Utang yang
dibayar, bukan laba.** Hal yang sama berlaku untuk **KC-56**.

## Praregistrasi R-317 — BELUM ADA, BAHAN LAMA BATAL

**[v18] `reports/semesta_rentang.json` sudah dibuka, maka ia TIDAK BOLEH lagi menjadi
bahan R-317** (aturan 29). Bahan penggantinya **belum dipilih**, dan **dilarang** berupa
berkas yang sudah dibuka pada sesi ini. Porosnya **wajib ditulis di jurnal lebih dulu**
(aturan 79), pada giliran BERBEDA dari adjudikasi (ADR-A016).

Urutan poros:

1. **BNXUSDT — keanggotaan PENYEBUT.** **[v18] Pertanyaan BERUBAH BENTUK LAGI:** daftar
   bulan semesta rentang kini **diketahui seluruhnya** (2022-04..2026-06, kontigu; boleh
   diturunkan karena bentangan = cacah). Yang **tidak** diketahui: **bulan mana saja yang
   masuk penyebut 19.586**. **PERINGKAT PERTAMA.**
2. **Sebab kekosongan TLMUSDT 2023-03** — bulannya terukur ADA; isinya 95,2% kosong.
3. **Tebing funding `2025-07`** (39 simbol) **dan BTCSTUSDT** (terukur kontigu 64).
4. **Identitas dua belas simbol-bulan karantina** — menuntut **modul CI**; **BUKAN
   kandidat murah**.
5. **"Bulan pertama di penyebut" lawan "bulan pertama di bursa"** — **[v18] naik nilai
   lagi**, kini dengan contoh terukur (2022-04 lawan 2022-05 pada BNXUSDT).
6. **[BARU] Penulis `semesta_rentang.json`** — tanpa itu, medannya tak tertelusur.
7. Sisanya: selisih 40−38 `diagnosa_kc15`; bentangan 38 kohort; H-A016; `mati_tersisip`;
   R-7/19/20/28/36/37; R-199; R-236..R-247; taksonomi lubang tiga kelas; bagian
   `baris_mati`.

**TIGA BELAS SYARAT KUMULATIF sebelum pita R-317 dikunci** (naik dari dua belas):
aturan **79** · **83** · **84** · **85** · **86 (a)** — dengan penyebutan bahwa daftar
`reports/` baru terbaca **76%** · **86 (b)** · **87** · **kebebasan tiap medan diperiksa
terhadap kode** · **KC-50** · **KC-52** · **KC-53** · **KC-54** (definisi medan disalin;
bila tak ditemukan, **syarat gugur tersurat WAJIB**) · **KC-55** (pita menutup ketiga
sisi) · **[BARU] KC-56** (bila bahan tak bertanggal, praregistrasi wajib menyatakan
perbandingan waktu tidak dipakai) · aturan **66**.

## Utang ukur yang masih hidup

1. **LUNAS [v14]** — aturan 52 atas trio `c1dc0009`.
2. **`karantina_semesta.yml`** (`de40fa4e`), `test_pulihkan.py` (`11c43533`),
   `test_rilis_karantina.py` (`739c8da9`), `test_karantina_a006.py` (`a5a3d82f`),
   `tests/test_lubang_tengah.py`, **`tests/test_gerbang_1m.py`** belum dibaca utuh.
3. **Lima ADR belum dibaca utuh:** A002, **A004 (peringkat tinggi — sumber keenam klausa
   gerbang)**, A006, A007, A008.
4. **Identitas dua belas simbol-bulan karantina** belum didaftar; **20.533.802 B**.
5. **LUNAS [v16]** — irisan 880 lawan 877 diukur; ketiga lubang bernama.
6. **"Bulan pertama di penyebut" lawan "di bursa"** belum diukur — **[v18] kini punya
   contoh terukur**: BNXUSDT 2022-04 (rentang) lawan 2022-05 (klines penyebut).
7. **Sebab kekosongan TLMUSDT 2023-03** belum diukur — **[v18] MENYEMPIT**: bulannya
   terukur ADA dan kontinu, sehingga yang dicari **sebab kekosongan isi**, bukan sebab
   hilangnya bulan. **Tidak lunas.**
8. **Cacah tangan aturan 66 ulang** — 50/54/45 TURUNAN. **[v18] Bertambah beban:** cacah
   entri `rentang` tidak dapat dihitung selama pemotongan 95% berdiri.
9. **`ukur_baris` V6** — `BERKAS_DIUKUR` 21 nama; `silang_funding.py` **705** baris.
10. **Tiga butir `PETA_MODUL.md`** bertanda "memerlukan verifikasi" (repo WARISAN).
11. **`PROMPT_KELANJUTAN.md`** belum berkepala "ARSIP — BUKAN SUMBER"; **`PROMPT.md`
    v55** belum didorong. **[v18] Utang berumur SEMBILAN versi.**
12. **LUNAS** — ADR-A020 dan ADR-A021 ada dan dibaca utuh.
13. **LUNAS [v17]** — jurnal 146 dan 147 dibaca utuh. **Digantikan:** jurnal **148**
    belum ditulis, dan **R-317 wajib dirancang ulang atas bahan lain**.
14. **LUNAS [v18]** — aturan 38 ke-60, ke-61, ke-62 dibaca, blob dicatat, ketiga jebakan
    CI dikenali. **Digantikan:** laporan atas push berkas ini (**ke-63**) wajib dibaca
    sebelum push akar berikutnya.
15. **R-228 belum diadjudikasi**; cacah 56 butir `test_lubang_tengah.py` DILARANG dikutip
    terukur.
16. **Keserian tebing `2025-07`** belum diukur; **DILARANG diklaim**.
17. **Bagian `baris_mati` `silang_funding.json` belum terbaca** (54%). Utang verifikasi
    **39**.
18. **LUNAS [v17]** — `gerbang_1m.py` dibaca utuh; modul **tidak berkeluaran**.
19. **Prasyarat klasifikasi belum dipenuhi.** Serapan funding **matang sebagai
    pembukuan, belum matang sebagai landasan fitur**: ADR-A003 **belum ada**; irisan 787
    lawan 787 belum diukur (KC-52); **87** "funding tanpa klines" belum didamaikan; kelas
    positif **33** dari **lima** simbol (KC-47); taksonomi lubang masih **BENTUK, bukan
    MEKANISME**. **[v18] Blokir kedua TIDAK membaik:** sumber keempat menguatkan **51**,
    tetapi **48 tetap tidak terdamaikan**, dan sumber baru itu tak bertanggal.
20. **TIDAK TERBAYAR [v18] — identitas bulan BNXUSDT.** Cacahnya kini terukur dari dua
    sumber (51 dan 51); **nama bulan PENYEBUT tetap tidak diketahui**. Yang berubah:
    daftar bulan **semesta rentang** dapat diturunkan seluruhnya. Yang tidak: daftar
    bulan **penyebut**. **Utang dipertajam, bukan lunas.** Utang verifikasi **40**.
21. **Daftar `reports/` baru terbaca 76%** (ref `8364ad92…`). **Melemahkan aturan 86 (a)**
    dan wajib disebut setiap kali (a) dipakai. Utang verifikasi **41**.
22. **BARU [v18] — penulis `reports/semesta_rentang.json` belum diidentifikasi.** Tanpa
    `waktu_utc` dan tanpa sidik; **tak tertelusur ke kode maupun ke waktu**. Selama
    terbuka, definisi medannya hanya dapat disimpulkan dari **bentuk data** — keadaan
    yang tepat memicu KC-54. Utang verifikasi **42**.
23. **BARU [v18] — keanggotaan penyebut BNXUSDT belum diukur.** Belum diperiksa apakah
    seluruh 48 bulan penyebut termuat di dalam 51 bulan semesta rentang. **Ini yang
    membuat H-A023 bersyarat** dan memblokir poros peringkat pertama. Utang verifikasi
    **43**.

## Penomoran berikutnya

Aturan resmi **1–81, 83, 84, 85, 86 (a) dan (b), 87** · usulan tersisa **77**, **78**,
**82**, **88**, **89** · **aturan berikutnya yang bebas 90** · KC resmi sampai **KC-55**
(KC-16 kosong selamanya), **KC-56 DIUSULKAN** · **KC berikutnya KC-57** · Hipotesis
berikutnya **H-A024** · Jurnal berikutnya **148** (tanggal **UTC**) · `STATE.md`
berikutnya **v60** · EKOR berikutnya **v19** · UKUR berikutnya **v19** · PROMPT
berikutnya **v55 (belum didorong)** · ADR berikutnya **A022** · Ramalan berikutnya
**R-317 (bahan lama BATAL)** · papan skor **321 SAH dan TIDAK BERGERAK** (TEPAT **221** ·
MELESET **61** · SEPARUH **22** · TIDAK TERADJUDIKASI **10** · MENUNGGU **7**).
