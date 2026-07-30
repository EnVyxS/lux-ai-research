# STATE lampiran UKUR — bagian 3 dari STATE (v14, milik STATE v55)

**Kedudukan berkas ini.** STATE dipecah tiga sejak v43 (KC-42). Pembagian berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, 83, 84, 85, **86**; KC-1..**KC-52**.
2. **`STATE_LAMPIRAN_EKOR.md`** v14 (blob **`5d481f9b0fd6adca53e8ba145f3fbd6cfeca20a4`**)
   — bagian 2: papan skor, ADR, catatan kejujuran.
3. **`STATE_LAMPIRAN_UKUR.md`** (berkas ini, v14) — bagian 3: pengukuran, modul,
   workflow, uji, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) dan **`PROMPT_KELANJUTAN.md`** (blob
   `35beed44`) — **arsip; BUKAN sumber** (ADR-A018 kep. 9).

Dasar v14: UKUR v13 (blob **`9e71c1ee9667c4b06389c87e0c77d4cefaca5b96`**), dibaca UTUH
pada giliran yang sama sebelum berkas ini ditulis (aturan 52, pencegahan KC-43).

**Apa yang v14 bawa, disebut di muka:** v13 membawa pengukuran karantina dan satu
koreksi yang membalik tafsir berkas ini sendiri. **v14 membawa PEMBACAAN KODE yang
menutup utang aturan 52 terbesar**, dan bersamanya satu temuan yang memperberat vonis
R-312: arah selisih yang diramalkan **mustahil ada**.

## KESERASIAN VERSI — SERASI PENUH pada v55 / v14 / v14

- `STATE.md` **v55** — blob **`be6bc6524e4209d370a4a5795a00bfe6c561d24d`**, commit
  **`cd209f3ed75a86470afa611ad6f2b97cb89e592e`**.
- `STATE_LAMPIRAN_EKOR.md` **v14** — blob
  **`5d481f9b0fd6adca53e8ba145f3fbd6cfeca20a4`**, commit
  **`a722ec632b3ee6f144e6e90c615db2480e946837`**.
- `STATE_LAMPIRAN_UKUR.md` **v14** — berkas ini.

Ketertinggalan satu versi yang dicatat EKOR v14 — bahwa berkas ini masih berkepala
"milik STATE v54" dan **tidak memuat** aturan 86 resmi, ADR-A019, ketiga blob trio,
temuan arah selisih R-312, maupun aturan 38 ke-47..ke-50 — **LUNAS oleh berkas ini**.
Ketiga bagian serasi kembali. **Satu berkas per push tetap MENGIKAT** (KC-42, KC-43).

**Tentang push berkas ini:** ia di akar repo sehingga menyalakan `ci.yml`. Tidak satu
pun `tests/**` berubah, jadi cacah uji tetap **1377** — ramalan **deterministik**,
**MUDAH**, TIDAK masuk papan skor, TIDAK menambah beruntun aturan 57. **Laporannya
WAJIB dibaca sebelum push akar berikutnya**, atau ia hangus seperti run `30547842823`.

**Angka yang TIDAK berubah dari v44/v45/v6/v7** (tidak diulang): taksonomi 9 kelas,
bulan ABSEN 11, H-A013..H-A015, terhenti, SETTLED. Rinciannya di v44 (blob
`d302caff`), v45 (`eb826817`), v6 (`27e59a79`), v7 (`4e7fb65b`).

## KOREKSI KC-41 — BACA SEBELUM MENGUTIP BERKAS INI

Kesepuluh koreksi di bawah **tetap dicantumkan** karena semuanya soal dokumen kami
sendiri, bukan soal data — menghapusnya berarti menghapus jejak cacat.

**Koreksi 1 (v5).** UKUR v5 menulis `lubang_awal.yml` ber-`paths` tiga entri. **SALAH**
— berkas asli (blob `3134bc9f6f91c83ed39ff8424506ac253317edee`) memuat **SATU** entri.
Bila bagian STATE bertentangan dengan berkas sumber, **berkas sumber menang**.

**Koreksi 2 (PROMPT v49).** Poros R-307 disebut "H-A017"; yang benar **H-A018**. LUNAS
di PROMPT v50.

**Koreksi 3 [v9].** Tiga dari empat simbol yang disebut "tampak bulan tengah" ternyata
bulan **PERTAMA**; yang benar-benar melawan H-A019 hanya **TLMUSDT 2023-03**. Kalimat
v8 **DICABUT** (ADR-A016 kep. 4). Pelajaran: membaca daftar dengan mata lalu menyebutnya
"tampak" adalah tebakan.

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

**Ketiganya BENAR, ketiganya satu satuan yang sama, dan tak satu pun keliru.** Yang
keliru adalah menyamakan penyebutnya. v53 sempat memberi dua angka pertama satuan
"lilin menit" tetapi yang ketiga "baris parquet" — **pemisahan satuan itu sendiri
adalah penyangga yang membuat kekeliruan bertahan berpuluh giliran** (ADR-A019 kep. 1
mencabutnya). **DILARANG** memakai salah satu dari ketiga angka itu **tanpa menyebut
penyebutnya**.

Dugaan lama **516.135 / 12 = 43.011 ≈ sebulan penuh**: pembagiannya sah secara
aritmetis, tetapi **sebarannya sangat tidak rata** (42.585 sampai 131.760 baris per
tar). Rata-rata 43.011 **turunan yang boleh dikutip, bukan bukti**; tafsir "tiap
karantina kira-kira sebulan penuh" **TIDAK ditegakkan**.

**Koreksi 5 [v10, LUNAS di EKOR v11].** EKOR v10 menulis `terisi ≉49,7%`; yang benar
**≈49,7%**.

**Koreksi 6 [v11, LUNAS di EKOR v12].** "ramalan deretministik" → "deterministik".

**Koreksi 7 [v12, LUNAS di UKUR v12].** Kepala berkas ini pernah berbunyi "KESERAIAN
VERSI"; yang benar "KESERASIAN VERSI".

**Koreksi 8 [v12, LUNAS di UKUR v12].** Penanda tebal tak berpasangan di daftar cacah
berkas uji. Tidak ada angka yang berubah.

**Koreksi 9 [v13] — SALAH NALAR, bukan salah ketik.** Jurnal 138 §5 butir 2 menulis
verbatim: *"Keduanya ditulis dari dua ekspresi berbeda yang kebetulan selalu bertemu —
maka 839.325.999 adalah cacah baris parquet yang sebenarnya, dan **839.842.134 yang
keliru**, bukan sebaliknya."* **Premisnya benar; kesimpulannya tidak sah.** Ia bertahan
dua giliran penuh, **lolos dari pembacaan ulang aturan 52**, dan runtuh hanya karena
data baru dibuka. **[v14] ADR-A019 kep. 2 mengangkatnya menjadi KELAS CACAT TANPA
PENANGKAL:** dari delapan kesalahan dokumen yang diperiksa, pembacaan ulang menangkap
**satu**. Ini butir ke-**10** daftar kesalahan dokumen dan satu-satunya yang **bukan**
salah ketik.

**Koreksi 10 [BARU v14] — TUDUHAN TERLALU LUAS, diadili dari sumber.** Jurnal 141 §6
menuduh EKOR v13 **dan** ADR-A019 menyajikan larangan R-312 nomor 5 seolah diresmikan
sesudah adjudikasi. Sesudah ketiga berkas dibaca dari sumber: **STATE v54 BEBAS** (ia
sudah menulis "(syarat gugur nomor 3, jurnal 136)"); **EKOR v13 lalai atribusi, bukan
misrepresentasi** — ia **diam** soal asal-usul, tidak pernah mengklaim yang keliru;
**ADR-A019 bersalah ringan** — kalimatnya benar, konteksnya menyesatkan. Membaca
kesunyian sebagai klaim adalah bentuk kecil dari Koreksi 9. Ini butir ke-**11**.

**Bacaan jujur atas Koreksi 4, 9, dan 10 bersama-sama:** cacat yang bertahan paling
lama di riset ini bukan salah hitung, melainkan **tafsir yang terdengar masuk akal atas
angka yang benar**. Itulah isi KC-52.

## [v14] BATAS KEKUATAN ATURAN 52 — DIPERSEMPIT, BUKAN DICABUT

EKOR v13 menulis bahwa pembacaan ulang aturan 52 "tidak berdaya sama sekali terhadap
penalaran yang cacat". **Rumusan itu terlalu luas.** Rumusan resmi STATE v55:

> Pembacaan ulang **dokumen sendiri** lemah terhadap penalaran cacat: ia membaca
> kalimat yang sudah diyakini benar. Pembacaan **kode** kuat terhadapnya: kode
> menyatakan identitas yang tidak dapat ditawar, dan ketidakcocokan antara docstring
> dan badan fungsi tampak begitu keduanya dibaca berdampingan.

Buktinya ada di berkas ini: pembacaan ulang trio `c1dc0009` **menangkap** cacat
penalaran terbesar yang tersisa (arah selisih R-312). **DILARANG** menulis bahwa aturan
52 menjaga mutu penalaran **atas dokumen**; **DIIZINKAN** mencatat bahwa ia melakukannya
**atas kode**, dengan **satu** kejadian terukur.

## Semesta riset = `perpetual_usdt` = penyebut 787 — tidak berubah

- `cacah_perpetual_usdt` **787** = `cacah_penyebut_simbol` **787**
- `cacah_perpetual_usdt_luar_penyebut` 0, `cacah_penyebut_bukan_perpetual_usdt` 0
- Batas wajib disebut: token saham/ETF/komoditas ikut di dalam 787.

## KC-18 — semesta kehidupan (dikonfirmasi ulang oleh R-307..R-313)

Atas **19.586** simbol-bulan lolos gerbang: **1.401 MATI** (7,153%), **98 SEPI**,
**18.087 HIDUP**. Dari 1.401 MATI: 842 kehilangan funding, 559 tetap berfunding.
`cacah_simbol_tanpa_hidup` **18**.

`cacah_lain` = 0 pada kelima modul → seluruh 19.586 berstatus MATI/SEPI/HIDUP.
18.087 + 98 = 18.185 TERUKUR, + 1.401 = 19.586 ✅

**Pembelahan [v9]:** **787** baris bulan PERTAMA (tepat satu per simbol — identitas),
**18.799** bukan-pertama. 787 + 18.799 = **19.586** ✅

**Pembelahan atas kelas MATI [v10]:** 1.392 berlilin PENUH + **9** tidak penuh =
**1.401** ✅

**Pembelahan [v11] — penyebut kerja R-311:** 18.799 − 1.401 = **17.398** (seluruh 1.401
baris MATI ternyata bukan bulan pertama). Dari 17.398: **17.284** penuh + **114**
berdefisit ✅ Rincian 114: HIDUP 111, SEPI 3, MATI 0.

**Pembelahan [v13] — lapis di luar penyebut.** Rilis parquet memuat **19.598**:
**19.586 lolos + 12 karantina**. Kedua belas baris karantina **TIDAK PERNAH** masuk
hitungan mana pun sebelum v13 — benar, tetapi **tidak pernah disebut**, dan itulah yang
menciptakan kesunyian KC-52. **[v14] Sebab strukturalnya terukur dari kode:**
`kehidupan_arsip.peta_parquet` **melewatkan baris `parquet_karantina`**.

## KARANTINA — TERUKUR PENUH [v13, tetap]

Sumber: kedelapan `reports/pulihkan_pecahan_<i>.json` dibaca UTUH pada ref
**`a2c4b83cb3a39647a912139cb45696ceea5efa71`**. `pulihkan` **VERSI 2**,
`run_id_sumber` **30396803601**, ditulis **2026-07-29T02:48Z** — **dua hari sebelum
pertanyaannya dirumuskan** (dasar kejadian kedua aturan 86).

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

`baris_total` per pecahan: 103.264.917 · 105.765.980 · 100.058.416 · 91.884.319 ·
106.865.397 · 117.671.896 · 114.013.851 · 100.317.358 → **839.842.134**.
`baris_utama` per pecahan: 103.134.312 · 105.634.220 · 100.058.416 · 91.841.734 ·
106.821.807 · 117.671.896 · 113.890.221 · 100.273.393 → **839.325.999**.

- **Mutu bukti:** kedelapan `pulih_sah` **true**; `cacah_sha_tak_cocok`,
  `cacah_bagian_hilang`, `cacah_anggota_kurang`, `cacah_anggota_tak_aman`,
  `selisih_baris_total` seluruhnya **0**; `baris_terverifikasi` **true**.
- **Sidik kode seragam** `76c27e3ce5d6edb13bb998b6ec65b538fb3d25205d4469bd4d186a95fa62d700`
  dan **sidik kode manifes seragam**
  `237ccf427faf9d48e9c0904433a56e8902de64de6552daee5d3053093bfba601` → penjumlahan
  lintas pecahan **sah** (aturan 22).
- **Aturan 46 terbukti bekerja secara positif:** pecahan 2 dan 5 melaporkan
  `definisi_dapat_dibedakan` **false** dan **menolak memilih**, alih-alih mengarang.
- **KC-47 diperiksa dan TIDAK terpicu:** 12 parquet tersebar di **enam** pecahan
  (3/3/1/1/3/1), bukan satu peristiwa.
- Nama tar karantina: `pecahan_<i>_karantina.part01.tar`.
- **BELUM DIUKUR:** **identitas** kedua belas simbol-bulan itu. Nama simbol dan
  bulannya **tidak diketahui**; kalimat apa pun tentang *jenis* instrumen yang
  dikarantina **DILARANG**.

**Adjudikasi R-313: TEPAT (2/2)** — selisih 0 pada kedua butir. **H-A022 TERBUKTI.**
**Cacat aturan 79 melekat permanen** (praregistrasi ditulis di chat, bukan
`journal/**`); **penolakan pihak ketiga atas R-313 sah**. **DILARANG** membacanya
sebagai bukti kalibrasi membaik (KC-51).

## VONIS `ukur_kolom` [v13] — dasar runtuhnya R-312

Dibaca langsung dari `kehidupan_arsip.py` (blob `318a5cb1`), bukan dari ingatan:

- **`cacah_lilin` = `n`** = cacah baris parquet, dari `pq.ParquetFile(...).metadata.num_rows`.
- **`cacah_lilin_terbaca`** = cacah baris yang **KEDUA** kolomnya (`volume`, `trades`)
  berhasil terurai.
- **Identitas paksa:** `cacah_lilin` = `cacah_lilin_terbaca` + `cacah_baris_cacat`.

**Kedua medan BUKAN dua pengukuran bebas** — mereka dua sisi dari satu identitas. R-312
berdiri di atas anggapan bahwa keduanya bebas, dan anggapan itu **tidak pernah
diperiksa terhadap kode** sebelum pitanya dikunci.

**Turunan cuma-cuma:** `cacah_berselisih` = **0** pada 19.586 dari 19.586, digabung
dengan identitas di atas, memaksa **`cacah_baris_cacat` = 0 di seluruh semesta** —
tidak satu pun dari 839.325.999 baris gagal diurai. Didapat tanpa run tambahan.

## [BARU v14] ARAH SELISIH R-312 MUSTAHIL — vonis diperberat

Docstring `selisih_lilin.py` (blob `d19bdb5f…`), **dibaca dari sumber**, mendefinisikan
`selisih = cacah_lilin_terbaca − cacah_lilin` dan menyatakan verbatim: *"Arah itu
dipilih supaya selisih semesta bertanda POSITIF bila jumlah terbaca memang lebih besar,
sesuai dua angka di atas."*

Tetapi identitas `ukur_kolom` memaksa `cacah_lilin` = `cacah_lilin_terbaca` +
`cacah_baris_cacat` dengan `cacah_baris_cacat` ≥ 0. Maka `cacah_lilin_terbaca` ≤
`cacah_lilin` **pada setiap baris**, dan **selisih itu tidak akan pernah positif**.

Akibatnya **butir 2 R-312 — yang menimbang sepuluh baris berselisih positif terbesar —
tidak dapat dimenangkan secara struktural**, dan itu benar **sejak sebelum pita
dikunci**. Kalimat "sesuai dua angka di atas" adalah **KC-52 yang ditulis ulang ke
dalam kode**: 839.325.999 dan 839.842.134 dianggap dua bacaan atas himpunan yang sama,
padahal berbeda penyebut. Rumusan v13 ("kedua medan bukan pengukuran bebas") **benar
tetapi kurang keras**.

## SISA DEFISIT [v11, tetap berlaku]

Sumber: `sisa_defisit.py` V1 run modul **30542217951** (commit `b1c7941d`, kode 0),
ringkas blob **`91a05c0528050d0d37e4cf7711b6556f13fc8d16`**.

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
  Bukan bulan tepi, bukan bulan pertama (ADR-A018 kep. 6).
- **Sepuluh teratas tersebar di TUJUH bulan** → **aturan 81 TIDAK terpicu**, sehingga
  114 sah diperlakukan sebagai cacah baris.
- **ANCUSDT `2022-05` defisit 26.959** lawan **LUNAUSDT `2022-05` defisit 26.950** —
  selisih **sembilan lilin**. Ini dan hanya ini dasar **H-A021**; **kebetulan angka,
  bukan bukti**. Setiap kalimat sebab untuk gugus `2022-05` **DILARANG**.
- **712.925 DILARANG DISEBUT PENGUKURAN BEBAS** — tautologi dari 808.162 − 95.237
  (KC-50, KC-37, ADR-A018 kep. 3). **DILARANG dipakai sebagai penyebut.**
- **114 baris seluruhnya HIDUP/SEPI dan NOL MATI DILARANG disebut temuan** — dipaksa
  oleh definisi penyebut kerja.
- Kendali: `kendali_nol` membuktikan modul bisa mengembalikan nol (aturan 50);
  `JAWABAN_KENDALI` **17 medan**, `bagian_teratas` **0,9677** = 600/620 dihitung TANGAN
  lebih dulu dan cocok; `bagian_teratas` **null** bila baris berdefisit < 10.

**Adjudikasi R-311: SEPARUH** — butir 1 **KALAH** (114; pita 200..12.000; meleset 26,3
kali dari taksiran 3.000); butir 2 MENANG (0,4087; sisa 0,0413 ke tepi ATAS); butir 3
MUDAH. Kedua butir meleset ke arah fisik yang SAMA. Dasar **KC-51**.

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

- **BULAN MATI PENUH DATANYA; YANG NOL ADALAH TRANSAKSINYA** — 1.392 dari 1.401
  (**99,4%**).
- **DILARANG melanjutkan ke "harga beku" atau "lilin datar".** `medan_baris_terlihat`
  berisi **14** medan — `ada_di_arsip`, `bagian_volume_nol`, `bulan`, `byte_parquet`,
  `cacah_baris_cacat`, `cacah_lilin`, `cacah_lilin_terbaca`, `cacah_volume_nol`,
  `galat`, `gerbang_lolos`, `jalur`, `simbol`, `status`, `transaksi_total` — dan **tak
  satu pun harga**.
- Defisit menumpuk di bulan pertama: rata **22.027** lilin hilang per bulan pertama,
  keterisian **≈49,7%**, bersesuaian dengan nisbah byte 0,527179 dari R-309.
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
- **DUA ANOMALI LAMA LUNAS** — baris 1 dan 2 adalah tepat kedua `cacah_mati_byte_kecil`
  R-308. **Larangan ADR-A015 kep. 5 TIDAK dibalik**: besar berkas tetap DILARANG dipakai
  sebagai penanda status ke arah mana pun. R-310, R-311, R-313, A018, dan **A019** tidak
  membaliknya.
- **TUJUH dari sembilan berbulan `2024-05`, jendela hanya SEMBILAN lilin**
  (39.308..39.317) → KC-47, aturan 81, **H-A020**. **Kalimat "tujuh simbol didelisting
  28 Mei 2024" DILARANG ditulis sebagai temuan.**
- Kendali data sah: tiga kendali BTCUSDT (2021-05, 2021-08, 2021-01) semuanya
  `cacah_lilin` **44.640** dan HIDUP.
- **Adjudikasi R-310: TEPAT** — kedua kemenangan **tipis ke tepi BAWAH**, kini terbaca
  sebagai gejala KC-51, bukan kalibrasi baik.

**Sidik `keterisian_lilin` V1 =**
`1cd98f4fa22c24b30f31f5b36dac0ea0bb3fa9de44e5e15ae73cbf11cdca08bb`
**Sidik laporan (`sidik_kode_laporan`) =**
`24b6bb265525e81c2e571b46e401f36903383f1e3738c487850861adc3e8c595`

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
- **Satu lawan tersisa: TLMUSDT 2023-03 (80.394 byte)** — sifatnya terukur oleh R-311
  (baris berdefisit terbesar semesta, HIDUP, 95,2% kosong). Tafsir "byte kecil = bulan
  sebagian di tepi rentang" **MELEMAH**; tafsir pengganti **TIDAK ditegakkan**
  (ADR-A018 kep. 6).
- Kendali dua lapis sah: tiga parquet terbesar seluruhnya BTCUSDT (2.770.666 /
  2.730.341 / 2.722.266, semuanya HIDUP); semesta buatan dengan jawaban dihitung TANGAN
  — `DETEKSI_PERTAMA` 2, `DETEKSI_HIDUP_KECIL` 2, `DETEKSI_SEBAGIAN` 2,
  `DETEKSI_NISBAH` 0,75, `DETEKSI_TOTAL_BYTE` 1.500 — cocok.

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

- **Zona 22.440–97.634 byte berisi 38 baris HIDUP dan NOL baris MATI.** Tafsir
  "kecil = mati" di zona itu **TERBALIK** (ADR-A015 kep. 5).
- **Sebaran per kelas IDENTIK dari TIGA modul berbeda** (aturan 36; kini **lima** run
  berturut bila `keterisian_lilin` dan `sisa_defisit` dihitung):

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
`8b7f2077`. **Total byte parquet = 32.706.262.375** (≈32,7 GB) atas 19.586 simbol-bulan.
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
TEPAT 3/3 — kemenangan sah, klaim ilmiah hampir kosong.
Sidik `4a5c2e4279eb1554dc119b48d6a8db61f6ea4ee11b7539efd70ee71d1ae18bf3`

## Lubang funding — agregat semesta (tetap)

- `cacah_simbol_ada_lubang` **122** dari 787 · awal **5** · bukan-awal **118**.
- BNXUSDT punya lubang AWAL dan bukan-awal sekaligus.
- Lima bentuk AWAL: BNXUSDT, ICPUSDT, JUPUSDT, QTUMUSDT, TLMUSDT. ICP dan TLM lubang
  awalnya melewati kematian (sumber salah-baca R-304, KC-46).
- Lubang funding **880** semesta / **877** dalam penyebut / **3** tak dikenal.
  **Irisan 880 lawan 877 BELUM diukur** — kandidat KC-52 berikutnya: dua penyebut mirip
  yang belum pernah dijajarkan.
- Dari 945 MATI di luar kohort: **386** kehilangan funding, **559** berfunding.

## Jumlah uji — terukur

**1377, kini ENAM bacaan berjejak.**

1. blob **`cdfdee2559201306a49bc9b01f1185d7aa36eebe`**, run **30559145901**, commit
   **`c1dc0009`** (trio `selisih_lilin`), 15:57:01Z, kode 0, `1377 tests collected in 0.58s`.
2. blob **`effb3a46bc20cda5c6c5910ee926aa16c195bb68`**, run **30575123865**, commit
   **`8368ca1f`** (STATE v54), 19:30:52Z, kode 0, `… in 0.54s`.
3. blob **`8cbbd4ce7b85d9e1f217a9cefbdacfb9318dec78`**, run **30576963781**, commit
   **`6642ed68`** (EKOR v13), 19:56:30Z, kode 0, `… in 0.67s`.
4. **[v14]** blob **`8ec97de5af8b528276174f635e3bda9e6cc2d7ef`**, run **30577779309**,
   commit **`2bdd8233`** (UKUR v13), 20:07:50Z, kode 0, `… in 0.62s`.
5. **[v14]** blob **`94d270e7065218f87bd5a26c5113ed8346cf6abf`**, run **30579348728**,
   commit **`cd209f3e`** (STATE v55), 20:29:25Z, kode 0, `… in 0.61s`.
6. **[v14]** blob **`04bfa2ed5fb43f128f8ee2351f41722314685a03`**, run **30580133552**,
   commit **`a722ec63`** (EKOR v14), 20:40:02Z, kode 0, `… in 0.46s`.

Turunan: 1341 + **36** butir `tests/test_selisih_lilin.py` = **1377** ✅ (aturan 21),
**[v14] kini terverifikasi dari sumber** — 36 butir `test_01`..`test_36` dicacah TANGAN
dari blob `2d903a4a…`, bukan dari ingatan.

Riwayat: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 → 984 →
1044 → 1100 → 1168 → 1233 → 1297 → 1341 (enam run) → **1377** (enam run berjejak).

**Aturan 57: beruntun 4 dari 4** sesudah PUTUS di 26/27. Tidak bertambah sejak trio —
tidak ada berkas uji baru. Ia **mencacah, bukan menaksir**; itulah sebabnya lajur ini
belum pernah kalah, dan sebabnya ia tidak dibanggakan.

### Aturan 38 — ordinal, kini sampai ke-50

Definisi yang berlaku (ADR-A018 kep. 8): pemakaian dihitung **hanya** untuk pembacaan
`reports/ci_terakhir.json` yang meninggalkan **jejak tertulis** berupa nomor run,
commit, dan blob.

| ke- | CI | run | commit | blob | jejak |
| --- | --- | --- | --- | --- | --- |
| 45 | 1377 | 30559145901 | `c1dc0009` | `cdfdee25` | jurnal 137, STATE v54 |
| 46 | 1377 | 30575123865 | `8368ca1f` | `effb3a46` | EKOR v13 |
| 47 | 1377 | 30576963781 | `6642ed68` | `8cbbd4ce` | jurnal 141, STATE v55 |
| 48 | 1377 | 30577779309 | `2bdd8233` | `8ec97de5` | jurnal 141, STATE v55 |
| 49 | 1377 | 30579348728 | `cd209f3e` | `94d270e7` | EKOR v14 |
| **50** | **1377** | **30580133552** | **`a722ec63`** | **`04bfa2ed`** | **berkas ini** |

**Pemakaian berjalan = ke-lima puluh.** Pemakaian ke-50 dibaca
**2026-07-30T20:40:02Z**, kode keluar **0**, atas push EKOR v14 — **dibaca sebelum
tertimpa**, sehingga ramalan "CI tetap 1377" untuk push itu **TERUKUR dan TEPAT**, tetap
**MUDAH**, tetap tidak diskor.

**[v14] Sembilan pembacaan berturut (ke-42..ke-50) tanpa satu pun laporan hangus.**

**Dua cacat tetap disebut, tidak dihaluskan:** baris ke-**38** (run `30541051907`,
commit `5d7d8b96`) **tanpa blob**, tidak dapat dipulihkan — ordinal ini sah **relatif
terhadap definisi di atas**, bukan sebagai pencacahan mutlak; dan run **30547842823**
(bot `de2fc03d`) **tidak pernah dibaca**, sudah tertimpa, **DILARANG dihitung**,
ramalannya **DILARANG diklaim menang**.

**Calon aturan** — dua berkas akar berturut tanpa membaca laporan di antaranya pasti
menghanguskan yang pertama — **DITOLAK diresmikan** oleh ADR-A019 kep. 3: masih **satu**
kejadian terukur. Mengangkatnya sekarang mengulang KC-48.

## Modul, workflow, dan berkas uji

**CACAH TANGAN yang sah** (aturan 66), pada ref **`3196fd98`** dan dikonfirmasi ulang
pada ref **`8a614567`**:

| direktori | cacah TANGAN |
| --- | --- |
| `lux_ai/serapan/` (berkas `.py`) | **49** |
| `tests/` | **53** |
| `.github/workflows/` | **44** |
| akar repo | **18** entri (6 direktori + 12 berkas) |

**UTANG ATURAN 66 HIDUP, dan ADR-A019 kep. 8 MENOLAK menutupnya.** Trio `selisih_lilin`
didorong sesudah ref itu, sehingga **50 / 54 / 45** adalah **TURUNAN dan DILARANG
dikutip sebagai terukur** sampai dicacah satu per satu bernomor (KC-33). Alasan
penolakan: menuliskannya sebagai "cacah baru" berarti mengarang pengukuran. Angka lama
47/51/42 (ref `07a69d39`) dan 48/52/43 (ref `5d7d8b96`) tetap sah **untuk ref
masing-masing**.

**PERINGATAN DUA CACAH `tests/` (ADR-A018 kep. 10).** `PETA_MODUL_BERKAS.md`
(`3abe95f6`) mencatat **34** berkas uji milik repo **WARISAN `bot_v8`**; repo riset ini
punya **53**. Keduanya benar untuk repo masing-masing; **menyebut "cacah uji" tanpa
menyebut repo-nya DILARANG**.

**Peringatan dini aturan 48:** tiga modul terbesar `lux_ai/serapan/` menurut byte —
`silang_funding.py` **29.873** · `funding.py` **28.121** · `sisa_defisit.py` **25.949**.

**[v14] BLOB TRIO R-312 — DIBACA UTUH, aturan 52 LUNAS PENUH.** Ketiganya dibaca pada
ref `e6007ba5`, blob dicatat untuk pertama kalinya:

| berkas | blob |
| --- | --- |
| `.github/workflows/selisih_lilin.yml` | **`de2fd4fd346c9e13213fcc9a410d4aea8460d67a`** |
| `tests/test_selisih_lilin.py` (**36** butir) | **`2d903a4a6f544eacd26b82bdb177680fa78bdffd`** |
| `lux_ai/serapan/selisih_lilin.py` | **`d19bdb5fe67e0bd9c1b141d7fb7cc6dcd089c5f2`** |

Cacah 36 **terverifikasi dari sumber** (`test_01`..`test_36`); dua helper
`_baris_kendali` dan `_ringkasan_sehat` berawalan garis bawah → **tidak dikumpulkan
pytest**. **CI 1377 bukan pengganti pembacaan ini** (ADR-A019 kep. 10).

Blob trio R-311 tetap: `sisa_defisit.py` **`7aa0e6d7003902e50806570ad112aae7f0345b07`**
(25.949 B) · `test_sisa_defisit.py` **`7004115acffd9c03c9ba4f9873bef40cb6b1375f`**
(12.640 B, **44** butir) · `sisa_defisit.yml` **`645112075e104a74d43f3e3d2185cfbd48b0b513`**.
Blob trio R-310 tetap: `keterisian_lilin.py` `3f80ffa7` · `test_keterisian_lilin.py`
`f58912d0` (64) · `keterisian_lilin.yml` `d821c63a`. Trio v9: `bulan_pertama.py`
`b9bd00ac` · `test_bulan_pertama.py` `75d87ba2` (65) · `bulan_pertama.yml` `2242e3e4`.
Lainnya identik: `irisan_byte.py` `2dbe3d55`, `test_irisan_byte.py` `b6389051` (68),
`irisan_byte.yml` `7d98a267`, `kehidupan.py` `f49abb2b`, **`kehidupan_arsip.py`
`318a5cb187406d16cfd3385d653bed905f632934` (19.281 B, DIBACA UTUH)**, **`pulihkan.py`
`a9e6eab7cc47555dfed919ac63044ff2eadc4893` (14.839 B, DIBACA UTUH)**,
**`silang_funding.py` V2 `42c3aa9dc2c16220b79cf9c9e46979dd000fd393` (29.873 B, DIBACA
UTUH)**, **`ukur_baris.py` V5 `3ebaa9f9` (17.442 B, DIBACA UTUH)**, `kohort_ekor.py`
`c9b63bbe`, `lubang_awal.py` `8c36943d`, `lubang_tebing.py` `575e777e`,
`lubang_tengah.py` `4d3beaf1`, `sebab_bangkit.py` `fd5a1dc4`, `tersisip_semesta.py`
`8a648838`, `bentangan_kohort.py` V2 `f4eae57a`, `byte_semesta.py` `ff68e4be`,
`funding.py` `8d4b1f82`, `rilis.py` `2e44530c`, `karantina_semesta.py` `46e7c46b`,
`arsip.py` `0104958b`, `gerbang_1m.py` `c8cc54c8`, `resample.py` `66a4b177`,
`semesta_kuota.py` `7288b030`, `bulan_absen.py` `10279d72`, `kebangkitan.py` `446321ee`,
`penyebut_tahun.py` `265aad00`, `anatomi_tengah.py` `04279335`, `__init__.py`
`64d85584`. `ci.yml` = **`c79497b2c812679eaa69aee5b3160eac9f5c5fb7`** (paths-ignore
`journal/**`, `decisions/**`, `hipotesis/**`, `reports/**`; push ke `lux_ai/**`,
`tests/**`, `STATE*`, `PROMPT*` MENYALAKAN CI). `karantina_semesta.yml` = `de40fa4e`
(**belum dibaca utuh**).

Cacah per berkas uji — **milik repo riset ini, bukan repo warisan**:
`test_irisan_byte.py` **68** · `test_bulan_pertama.py` **65** ·
`test_keterisian_lilin.py` **64** · `test_bentangan_kohort.py` V2 **63** (blob
`9f850ecdb25466d38c839004b36ff221db2cf7f8`, dicacah TANGAN `test_01`..`test_63`) ·
`test_lubang_tebing.py` **60** · `test_sebab_bangkit.py` **57** · `test_byte_semesta.py`
**56** · `test_lubang_awal.py` **48** · `test_tersisip_semesta.py` **47** ·
`test_anatomi_tengah.py` **47** · `test_sisa_defisit.py` **44** ·
**`test_selisih_lilin.py` 36** · `test_terhenti.py` V4 **33** · `test_bulan_absen.py`
**32** · `test_karantina_semesta.py` **28** · `test_silang_settled.py` **24** ·
**`test_ukur_baris.py` 3**.

**[v14] POLA WORKFLOW TRIO — TERVERIFIKASI DARI SUMBER** (`selisih_lilin.yml`, blob
`de2fd4fd…`), bukan lagi dari ingatan: `name`, `on.push.paths` **SATU** entri,
`permissions: contents: write`, job `ukur` di `ubuntu-latest`, checkout@v4 +
setup-python@v5 (3.11), `pip install numpy pandas pyarrow pyyaml`, langkah `jalan`
id=`jalan` dengan `set +e` → `KODE=$?` → `echo "kode=$KODE" >> "$GITHUB_OUTPUT"` →
`exit 0`, langkah `catat status` (`reports/<nama>_status.json`), langkah `dorong laporan`
(`[skip ci]`, `git pull --rebase`, push), langkah akhir
`exit ${{ steps.jalan.outputs.kode }}`. **Aturan 55 LUNAS untuk berkas ini.**

## API terverifikasi

API lama (v37–v12) tetap berlaku. Tambahan v13–v14 **seluruhnya dibaca UTUH dari kode**
(KC-43):

**`pulihkan` V2** (blob `a9e6eab7cc47555dfed919ac63044ff2eadc4893`, 14.839 B).
Tetapan: `VERSI=2`, `TOTAL_PECAHAN=8`, `AKAR_UNDUH="data/unduh"`,
`AKAR_PULIH="data/pulih"`. Tetapan teks: `DEF_TAK_ADA_MANIFES`,
`DEF_TAK_TERBEDAKAN`, `DEF_LOLOS_SAJA`, `DEF_LOLOS_PLUS_KARANTINA`, `DEF_TAK_COCOK`.
Fungsi: **`nama_manifes(i)="reports/manifes_pecahan_<i>.json"`** ·
**`nama_status_serapan(i)="reports/pecahan_<i>_status.json"`** ·
**`nama_keluaran(i)="reports/pulihkan_pecahan_<i>.json"`** ·
`nama_tag(i,run_id)="serapan-pecahan-<i>-<run_id>"` · `sidik_kode()` mencap
`["pulihkan.py","rilis.py"]` · `run_id_sumber` ·
**`putuskan_definisi(selisih_utama, selisih_total, baris_karantina)`** →
`(kesimpulan, dapat_dibedakan)` · `anggota_aman` ·
**`cacah_baris_parquet(jalur)` = `pq.ParquetFile(...).metadata.num_rows`** ·
`periksa_bagian` · **`periksa_keluarga`** dipanggil **dua kali**, atas
`manifes.get("rilis")` dan **`manifes.get("rilis_karantina")`** — inilah tempat karantina
dicacah terpisah · `_utuh` · `jalankan` · `main` (env `PULIH_INDEKS`). Praregistrasi
historis **R-198**. Aturan ditegakkan: 7, 8, 9, 16, 21, 22, 24, 30, 33, 34, 36, 44, 45, 46.

**`kehidupan_arsip` V1** (blob `318a5cb187406d16cfd3385d653bed905f632934`, 19.281 B).
Tetapan: `VERSI=1`, `TOTAL_PECAHAN=8`, `AKAR_BONGKAR="data/kehidupan_arsip"`,
`KENDALI_CACAH=3`, `KOLOM_VOLUME="volume"`, `KOLOM_TRANSAKSI="trades"`,
`BERKAS_DICAP=["kehidupan.py","kehidupan_arsip.py","kohort_ekor.py","pulihkan.py","rilis.py"]`,
`nama_keluaran(i)="reports/kehidupan_arsip_<i>.json"`.
Fungsi: `peta_parquet` (**melewatkan baris `parquet_karantina`** — sebab struktural
KC-52), `_angka`, **`ukur_kolom`** → `{cacah_lilin, cacah_lilin_terbaca,
cacah_baris_cacat, transaksi_total, cacah_volume_nol, bagian_volume_nol}`,
`ukur_parquet`, `baris_kehidupan`, **`kendali_pecahan`** (tiga `byte_parquet` terbesar),
`ringkas_pecahan`, `kode_keluar`, `_cocokkan`, `periksa_bagian`, `jalankan`,
`berkas_ringkas`, `main` (env `KEHIDUPAN_ARSIP_INDEKS`). Praregistrasi historis R-205,
R-206, R-207.

**[v14] `selisih_lilin` V1 — KINI DIBACA UTUH DARI SUMBER** (blob
`d19bdb5fe67e0bd9c1b141d7fb7cc6dcd089c5f2`, commit `c1dc0009`). Tetapan: `VERSI=1` ·
`TOTAL_PECAHAN` diwarisi `kehidupan_arsip` · `KELUARAN="reports/selisih_lilin.json"` ·
`KELUARAN_RINGKAS="reports/selisih_lilin_ringkas.json"` · `BATAS_BARIS_LAPORAN=40` ·
`MEDAN_KLAIM="cacah_lilin"` · `MEDAN_TERBACA="cacah_lilin_terbaca"` · `CACAH_TERATAS=10` ·
`LILIN_LANGSUNG_TERCATAT=839325999` · `BARIS_PARQUET_TERCATAT=839842134` ·
`SELISIH_TERCATAT=516135` · `AMBANG_HIDUP_KECIL=97634` · `INVARIAN` **8** kunci ·
`R312_PITA_BUTIR_1=(12,120)` · `R312_PITA_BUTIR_2=(0.50,0.865)` · `BERKAS_DICAP` **4**
nama. Fungsi: `nama_keluaran`, `nama_ringkas`, `daftar_sumber`, `sidik_kode`, `selisih`,
`kumpulkan`, `ringkas_selisih` (11 medan), `baris_berselisih`, `baris_positif`,
`teratas`, `bagian_teratas`, `sebaran_kelas`, `potong`, `dalam_pita`,
`dalam_pita_pecahan`, `invarian_terukur`, `selisih_invarian`, `semesta_kendali`,
`semesta_teratas`, `kendali_deteksi`, `kendali_nol`, `kendali_negatif`,
`kendali_teratas`, `selisih_terhadap_warisan`, `dua_jalur_bertemu`, `uji_r312`,
`kode_keluar`, `jalankan`, `berkas_ringkas`, `main`.
**Empat kendali terbaca dari kode dan seluruhnya lolos:** `kendali_deteksi`
(`JAWABAN_KENDALI` **11 medan**, dihitung TANGAN: klaim langsung 213.480 · terbaca
214.360 · bersih 880 · positif 1.080 · negatif 200 · berselisih 3), `kendali_nol`,
`kendali_negatif` (menuntut bersih **−250**), `kendali_teratas` (bagian **0,9615** =
7.500/7.800). `kode_keluar` mengembalikan **2** bila `cacah_berselisih <= 0` —
**dirancang**, bukan galat.
**Empat syarat gugur DIKUNCI DI MUKA** di docstring. Syarat 1 verbatim: *"Medan
`cacah_lilin_terbaca` tidak ada, atau identik dengan `cacah_lilin` di SELURUH baris:
laporan TIDAK TERADJUDIKASI (aturan 41), bukan MELESET."* Syarat 3 verbatim: *"Bila
butir 1 mendarat tepat di 12, kesamaannya dengan dugaan 12 bulan karantina DILARANG
dibaca sebagai konfirmasi apa pun."* → **vonis TIDAK TERADJUDIKASI bukan rasionalisasi
pasca-hoc**, dan **kredit larangan nomor 5 milik praregistrasi**, bukan adjudikasi.
**KC-49 tercatat ditaati DI DALAM KODE:** lantai aritmetis 12 diturunkan tertulis dari
516.135 / 44.640 = 11,56… dibulatkan ke atas.
Laporan `reports/selisih_lilin_ringkas.json` blob
**`e5cc64011030cfb8e1a8edf3699dd01b3caafab7`**, `byte_sumber` 6.834, sidik kode
`e6c77965cc40f40ae5a11c3af3422d5939bb580ca005cf55df7c7d7bb96257e7`, sidik sumber
`53ff54b2fc3dced38229c9729e09a9b4365cf2b98c1ca722698d838d8157b2f9`. Terukur:
`cacah_baris` **19586** · `cacah_berselisih` **0** · `jumlah_klaim_langsung` =
`jumlah_terbaca_langsung` = **839325999** · `dua_jalur_bertemu` **true** ·
`selisih_terhadap_warisan` {klaim 0, terbaca −516135, bersih −516135} ·
`uji_r312.teradjudikasi` **false** · `bagian_teratas` **null** · `sebaran_kelas` `{}`.

**`ukur_baris` V5** (blob `3ebaa9f9`, 17.442 B): `PAGAR_BARIS=800`, `BERKAS_DIUKUR`
**21 nama**, uji `test_ukur_baris.py` (`7975bf88`) **3** fungsi. **Utang V6 hidup**
(ADR-A019 kep. 8): 21 nama jauh tertinggal dari ~50 modul dan ~54 uji; pagar 800 belum
diuji atas ≈29 modul yang lebih baru.

**`silang_funding` V2** (blob `42c3aa9d`, DIBACA UTUH): `baca_laporan_kehidupan(akar,
total)` → **TIGA** nilai `(status, byte_parquet, meta)`, kunci tuple `(simbol, bulan)`;
**`baca_medan_baris(akar, total, medan)` → `(nilai, meta)`** — **TIDAK cacat**, dan
bentuk kembaliannya **peta berkunci `(simbol, bulan)`, bukan daftar** (dugaan lama
DIKOREKSI OLEH PENGUKURAN). Melewati baris ber-medan `None`. Dipakai `keterisian_lilin`
dan `sisa_defisit` dengan `medan="cacah_lilin"`. Tetapan: `PENYEBUT_TERCATAT=19586`,
`MATI_TERCATAT=1401`, `KOHORT_TERCATAT=456`, `HIDUP_TANPA_FUNDING_TERCATAT=33`,
`LUBANG_TAK_DIKENAL_TERCATAT=3`,
`BENTUK_TERBITAN_FUNDING={"awal":48,"ekor":826,"tengah":6}`, `MEDAN_LILIN="cacah_lilin"`,
`SUMBER_FUNDING="reports/funding_semesta.json"`, `KENDALI_CACAH=3`.

**`keterisian_lilin` V1** (blob `3f80ffa7`): `INVARIAN` =
`{penyebut:19586, cacah_simbol:787, cacah_hidup:18087, cacah_sepi:98, cacah_mati:1401,
total_byte:32706262375, byte_hidup:32049492952, cacah_hidup_byte_kecil:38}` ·
`AMBANG_HIDUP_KECIL=97634` · `MENIT_PER_HARI=1440` · `KENDALI_SIMBOL="BTCUSDT"` ·
`KENDALI_CACAH=3` · `R310_PITA_BUTIR_1=(1,120)` · `R310_PITA_BUTIR_2=(0.02,0.25)`.

**`sisa_defisit` V1** (blob `7aa0e6d7`): `KELUARAN="reports/sisa_defisit.json"`,
`BATAS_BARIS_LAPORAN=40`, `CACAH_TERATAS=10`, `R311_PITA_BUTIR_1=(200,12000)`,
`R311_PITA_BUTIR_2=(0.02,0.45)`, `DEFISIT_SEMBILAN_TERCATAT=95237`,
`DEFISIT_BUKAN_PERTAMA_TERCATAT=808162`, `SISA_TERCATAT=712925`, `INVARIAN` delapan
kunci seluruhnya BEBAS, `JAWABAN_KENDALI` **17 medan**. Fungsi kunci: `baris_calon`,
`baris_berdefisit`, **`teratas`** (mengembalikan **None** bila baris berdefisit < 10 —
bukan 0, bukan galat), `kendali_nol`, `uji_r311`, `jalankan(akar=".", total=None)`.

**`bulan_pertama` V1** (`b9bd00ac`): `R309_PITA_BUTIR_1=(22,38)`,
`R309_PITA_BUTIR_2=(0.10,0.60)`, `BULAN_TEPI="2026-06"`, `nisbah_pertama` (penyebut
kosong → **None**), `total_byte_langsung`.
**`irisan_byte` V1** (`2dbe3d55`): `AMBANG_HIDUP_KECIL=97634`,
`AMBANG_MATI_KECIL=150000`, `MEDAN_SELISIH` **9** (delapan bebas + satu turunan).
**`bentangan_kohort` V2** (`f4eae57a`, uji `9f850ecd`): butir 09 menolak `str(tuple)`
sebagai kunci; butir 59–61 memanggil `silang_funding` asli untuk memeriksa BENTUK
kembalian; butir 63 melarang nama kohort tertulis di dalam modul (aturan 73); butir 37
menuntut `None`, bukan nol.
**`lubang_awal` V1** (`8c36943d`): medan `mati_tidak_setelah_lubang_bukan_awal` memakai
`<=` — **DILARANG dipakai untuk klaim arah** (aturan 80).
**`kohort_ekor` V4** (`c9b63bbe`): `TEBING="2025-07"`, `BULAN_DIHARAPKAN="2026-06"`,
`BATAS_SIMBOL=10`, `PAGU_MUNDUR=60`, `AMBANG_SEPI=0.5`,
`KENDALI_HIDUP=("BTCUSDT","ETHUSDT")`.
**`kehidupan`** (`f49abb2b`): `AMBANG_SEPI=0.5`, `BULAN_MULAI="2025-07"`,
`BULAN_AKHIR="2026-06"`, `deret_bulan`, `klasifikasi`, `penyebut_ganda`.

Sidik lain: `sebab_bangkit` V1 `bafe4359e8f36f0402d4be4a4e4aef4a28f224f6419f06f701fb3a5bf696221a` ·
`tersisip_semesta` V1 `9618fd19e4ab2e7b5279177db600f6176afd914ab1e94576e54197f70ebc537c` ·
`bentangan_kohort` V2 `8ca6ebbefc3606464ebd7f94c6b51b1fdf500c62779cdcb5700ec2ee4ea9f32c` ·
`lubang_awal` V1 `156499ce…f2362` · `sidik_data_funding`
`2c9fbd1b04f74c9c844bc223a99a103d12220b88d08667b3792720e5b9608d24` ·
`sidik_kode_silang_funding` seragam
`8a9b859c09cd64e30e203e6f8dc53411b8e341c44f112805b3041e5d4d3231b1` · laporan kehidupan
seragam `24b6bb265525e81c2e571b46e401f36903383f1e3738c487850861adc3e8c595`. Sidik
manifes per pecahan: `_0` `88d5704c` · `_1` `64311545` · `_2` `6bbc9990` · `_3`
`b6f5f27e` · `_4` `d204f353` · `_5` `3b0e2d22` · `_6` `356ae3d6` · `_7` `2abc9c73`.

**[v13] ATURAN 36 — KASUS TERKUAT SAMPAI KINI.** `selisih_lilin` menjumlahkan medan
`cacah_lilin` atas 19.586 baris laporan kehidupan; `pulihkan` mencacah kaki parquet
lewat jalur unduh–bongkar–verifikasi yang sama sekali berbeda, pada run yang berbeda,
tiga hari lebih awal. Keduanya **839.325.999**, sampai satuan terakhir. **Dua jalur,
dua modul, dua run, satu angka.**

## Hipotesis

- H-A001 belum diuji · H-A002b GUGUR · H-A003 MENANG pada 3, GUGUR pada 9 · H-A004 tak
  dapat diuji · H-A005 GUGUR · H-A006 MENANG enam run · H-A008 MENANG dua kali ·
  H-A009 GUGUR · H-A010 MENANG 5–0 · H-A011 MENANG · H-A012 MENANG · H-A013 MENANG 6–0,
  TAFSIR DICABUT · H-A014 BENTUK BARU MENANG 9 dari 9 · H-A015 MENANG sebagai angka,
  DIBATASI sebagai tafsir (KC-45) · H-A016 PENGAMATAN, BELUM DIUJI.
- **H-A017** DICABUT sebagai pola semesta (ADR-A011/A012, dilemahkan R-306): bukti
  lepas-tebing tinggal **1** simbol. TIDAK dipulihkan oleh R-307..R-313.
- **H-A018 — byte parquet sebagai gejala kehidupan. DIUKUR DUA KALI (R-307, R-308).**
  **BOLEH:** "bulan MATI menempati bagian KECIL dari byte semesta (**0,0177** dari
  32,7 GB) dan rata-rata sekitar **4,3×** lebih kecil daripada bulan HIDUP".
  **DILARANG:** "berkas kecil berarti pasar mati" — di zona 22.440–97.634 byte ada
  **38 HIDUP dan 0 MATI**, dan baris paling kosong di seluruh semesta (TLMUSDT 2023-03,
  95,2% kosong) berstatus **HIDUP**.
- **H-A019 [DIUJI R-309 — DITERIMA TERBATAS, ADR-A016 kep. 1].** Rumusan resmi
  satu-satunya: *hampir setiap baris HIDUP di zona byte kecil adalah bulan pertama
  simbol itu di dalam penyebut (**37 dari 38**), sementara hampir setiap bulan pertama
  BUKAN berkas kecil (**37 dari 787, ±4,7%**).* Irisan asimetris, bukan sebab.
  **DILEMAHKAN oleh ADR-A018 kep. 6 tanpa tafsir pengganti.**
- **H-A020 [DIUSULKAN, BELUM DIUJI].** *Ketujuh baris MATI tak penuh berbulan `2024-05`
  adalah SATU peristiwa, bukan tujuh pengamatan bebas: jendelanya hanya sembilan lilin
  (39.308..39.317).* DILARANG menulis "tujuh simbol didelisting 28 Mei 2024" sebagai
  temuan. Cara mengujinya: `lubang_tengah` atas gugus 2024-05.
- **H-A021 [DIUSULKAN, BELUM DIUJI].** *Kekosongan ANCUSDT `2022-05` (defisit 26.959)
  dan LUNAUSDT `2022-05` (defisit 26.950) adalah SATU peristiwa yang sama.* Dasarnya
  hanya selisih **sembilan lilin** — **kebetulan angka, bukan bukti**. Bila kelak
  DITERIMA, cacah pengamatan bebas dalam sepuluh teratas turun dari 10 ke 9, dan
  `bagian_teratas` **tidak berubah** karena dihitung atas lilin, bukan atas baris.
- **H-A022 [TERBUKTI lewat R-313].** Rumusan yang terbukti: *selisih 516.135 antara Σ
  baris parquet lolos gerbang dan Σ seluruh baris parquet rilis adalah tepat jumlah
  baris pada parquet karantina yang berada di luar penyebut 19.586.* Terukur:
  **516.135** baris pada **12** parquet, dari delapan laporan `pulihkan` yang ditulis
  **dua hari sebelum pertanyaannya dirumuskan**. **Batas tafsir (ADR-A019 kep. 6):**
  yang terbukti **identitas himpunan**, bukan sebab karantina. Identitasnya belum
  didaftar. Turunan cuma-cuma: **`cacah_baris_cacat` = 0 di seluruh semesta**.
- Hipotesis berikutnya **H-A023**.

## Praregistrasi R-312 — TERADJUDIKASI: TIDAK TERADJUDIKASI, SELAMANYA

Disimpan apa adanya sebagai jejak (aturan 29). Poros: selisih antara `cacah_lilin` dan
`cacah_lilin_terbaca` atas 19.586 baris.

- **Butir 1 (BERISIKO).** Cacah baris berselisih, pita **12 .. 120**.
- **Butir 2 (BERISIKO).** Bagian selisih yang ditanggung baris teratas, pita
  **0,50 .. 0,865**.
- **Butir 3 (MUDAH).** Penggugur, kendali, kode 0, CI.

**Terukur: `cacah_berselisih` = 0.** Penyebut butir 2 NOL → aturan 41. **Vonis: TIDAK
TERADJUDIKASI, selamanya** (ADR-A019 kep. 4). Porosnya runtuh sebelum diadjudikasi
karena kedua medan **terikat identitas**; **[v14] lebih keras lagi: arah selisih yang
diramalkan mustahil bertanda positif**, sehingga butir 2 tak dapat dimenangkan secara
struktural sejak sebelum pita dikunci.

**Lima larangan permanen:** (1) pita 12..120 DILARANG disebut "tidak terbantah";
(2) DILARANG mengatakan kalibrasi membaik atau memburuk karenanya; (3) DILARANG
dihitung di pembilang maupun penyebut nisbah kemenangan; (4) DILARANG dihidupkan
kembali dengan alasan penjelasannya kini ditemukan; (5) kesamaan angka **12** dengan
R-313 DILARANG dibaca sebagai konfirmasi — artinya berbeda. **[v14] Atribusi larangan
5 dilengkapi: ia berasal dari PRAREGISTRASI (syarat gugur nomor 3, docstring modul dan
jurnal 136), bukan dari adjudikasi.**

**Aturan 85 dipakai pertama kali di R-312 dan MASIH BELUM PUNYA SATU PUN ADJUDIKASI.**
Ia belum terbukti bekerja maupun gagal; **DILARANG** menyebutnya penangkal yang sudah
teruji.

**[v14] Syarat praregistrasi baru (ADR-A019 kep. 4):** kebebasan tiap medan **WAJIB
diperiksa terhadap kode** sebelum pita dikunci.

## Praregistrasi R-313 — TERADJUDIKASI: TEPAT (2/2)

Disimpan apa adanya sebagai jejak (aturan 29).

- **Butir 1.** Σ `baris_karantina` atas delapan laporan = **516.135**, titik tunggal →
  terukur **516.135** → **MENANG**.
- **Butir 2.** Σ parquet karantina = **12**, titik tunggal → terukur **12** → **MENANG**.

**Cacat prosedural yang diakui:** praregistrasi ditulis **di chat**, bukan di
`journal/**` — **pelanggaran aturan 79**. Satu-satunya saksi bahwa ia ditulis lebih dulu
adalah riwayat percakapan, **bukan git**. **Penolakan pihak ketiga atas R-313 sah.**

**[v14] ATURAN 79 DIRUMUSKAN ULANG, BUKAN DILEMAHKAN** (ADR-A019 kep. 7, STATE v55).
Aturan yang dilanggar lalu disebut "lemah" adalah aturan yang sedang dihapus diam-diam.
Rumusan yang berlaku: aturan 79 **tetap PENUH**; praregistrasi di luar `journal/**`
**tidak sah sebagai praregistrasi**; hasilnya tetap dicatat demi kejujuran riwayat,
**cacatnya melekat permanen**. Yang lemah bukan aturannya, melainkan **kepatuhan kami**
pada satu kejadian. **DILARANG** menyebut aturan 79 lemah, longgar, atau opsional.

**DILARANG** membaca kemenangan ini sebagai bukti kalibrasi membaik: ia menjumlahkan
angka yang **sudah tercatat di repo**, bukan menaksir sebaran yang belum diukur.

## Praregistrasi R-314 — BELUM ADA

Porosnya **wajib ditulis di jurnal lebih dulu** (aturan 79), pada giliran yang BERBEDA
dari adjudikasi (ADR-A016). Urutan resmi poros (ADR-A019 kep. 9):

1. **Lubang tengah gugus `2022-05` dan `2024-05`** — menguji **H-A021 dan H-A020
   sekaligus**: apakah baris berdefisit yang berhimpit bulan itu berbagi satu jendela
   lilin yang sama. **Prioritas tertinggi.**
2. **Identitas dua belas simbol-bulan karantina** — kandidat **termurah**; manifesnya
   sudah ada di repo (`reports/manifes_pecahan_<i>.json`). **Aturan 86 berlaku penuh.**
3. **Irisan 880 lawan 877 lubang funding** — kandidat KC-52 berikutnya.

**[v14] SEMBILAN SYARAT KUMULATIF sebelum pita R-314 dikunci** (STATE v55, ADR-A019
kep. 9): aturan **79** (di `journal/**`, giliran berbeda) · aturan **83** (aritmetika
implikasi tertulis) · aturan **84** (satu klausa per butir) · aturan **85** (tepi
terpusat di lantai aritmetis atau paling banyak satu orde di atasnya, **dengan alasan
tertulis**) · **aturan 86** (`reports/` diperiksa lebih dulu — dua kejadian menunjukkan
jawabannya kadang sudah tersimpan) · **kebebasan tiap medan diperiksa terhadap kode** ·
**KC-50** (tidak ada agregat lewat jalan memutar) · **KC-52** (batas himpunan tiap
penyebut dinyatakan) · aturan **66** (nama modul dicek lewat pencacahan direktori
TANGAN; 49/53/44 sah untuk ref `3196fd98`, **50/54/45 DILARANG dikutip terukur**).

## Utang ukur yang masih hidup

1. **LUNAS [v14]** — aturan 52 atas trio `c1dc0009`: ketiganya dibaca UTUH, blob
   dicatat (lihat bagian modul).
2. **`karantina_semesta.yml`** (`de40fa4e`) belum dibaca utuh; begitu pula
   `test_pulihkan.py` (`11c43533`), `test_rilis_karantina.py` (`739c8da9`),
   `test_karantina_a006.py` (`a5a3d82f`).
3. **Lima ADR belum dibaca utuh:** A002, A004, A006, A007, A008.
4. **Identitas dua belas simbol-bulan karantina** belum didaftar.
5. **Irisan 880 lawan 877 lubang funding** belum diukur.
6. **Perbedaan "bulan pertama di penyebut" lawan "bulan pertama di bursa"** belum
   diukur (ADR-A016 kep. 6).
7. **Sebab kekosongan TLMUSDT 2023-03** belum diukur; tidak ada tafsir yang ditegakkan.
8. **Cacah tangan aturan 66 ulang** — 50/54/45 TURUNAN, DILARANG dikutip terukur;
   ADR-A019 kep. 8 **MENOLAK** menutup utang ini.
9. **`ukur_baris` V6** — `BERKAS_DIUKUR` 21 nama atas ~50 modul dan ~54 uji.
10. **Tiga butir `PETA_MODUL.md` bertanda "memerlukan verifikasi"** (repo WARISAN):
    `enable_hs` tidak ditemukan di `config.py` padahal dipakai `strategy.py`; klaim
    "30 pair dipilih alfabetis"; klaim "kendala mengikat = kapasitas margin".
11. **`PROMPT_KELANJUTAN.md`** belum diberi kepala "ARSIP — BUKAN SUMBER" dan belum
    dihapus; **`PROMPT.md` v55** belum didorong.
12. **LUNAS [v14]** — ADR-A019 ada (blob `9cd7d25e7a61207343e60233887d06b441aa3cbf`,
    commit `e6007ba5`, sepuluh keputusan, dibaca ulang utuh pada giliran yang sama).
13. **LUNAS [v14]** — jurnal 141 ada (blob `bde76db952f587f4df4529e49f0015c13a29919b`,
    commit `1b970da5`, sembilan bagian). **Digantikan:** **jurnal 142 + praregistrasi
    R-314** belum ditulis; itulah pekerjaan ukur berikutnya.
14. **BARU [v14]** — laporan CI atas push berkas ini (**aturan 38 ke-51**) wajib dibaca
    sebelum push akar berikutnya.

## Penomoran berikutnya

Aturan resmi **1–81, 83, 84, 85, 86** · usulan tersisa **77**, **78**, **82** · **aturan
berikutnya yang bebas 87** · KC resmi sampai **KC-52** (KC-16 kosong selamanya; KC-52
ditutup sebagai teka-teki, TETAP HIDUP sebagai pola) · **KC berikutnya KC-53** ·
Hipotesis berikutnya **H-A023** · Jurnal berikutnya **142** · `STATE.md` berikutnya
**v56** · EKOR berikutnya **v15** · UKUR berikutnya **v15** · PROMPT berikutnya **v55
(belum didorong)** · ADR berikutnya **A020** · Ramalan berikutnya **R-314** · papan skor
**313** (TEPAT **218** · MELESET **57** · SEPARUH **22** · TIDAK TERADJUDIKASI **9** ·
MENUNGGU **7**).
