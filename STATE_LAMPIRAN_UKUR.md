# STATE lampiran UKUR — bagian 3 dari STATE (v10, milik STATE v50)

**Kedudukan berkas ini.** STATE dipecah tiga sejak v43 (KC-42). Pembagian berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, 83, dan 84; KC-1..KC-50.
2. **`STATE_LAMPIRAN_EKOR.md`** v10 — bagian 2: papan skor, ADR, catatan kejujuran.
3. **`STATE_LAMPIRAN_UKUR.md`** (berkas ini, v10) — bagian 3: pengukuran, modul,
   workflow, uji, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip lama; bukan sumber lagi.

Dasar v10: UKUR v9 (blob **`0b795fb48ababa61b318518ce1196ad90467e077`**), dibaca UTUH
sebelum berkas ini ditulis (aturan 52). Yang ditambahkan v10: **keterisian lilin**
(pengukuran pertama atas ISI bulan MATI); API `keterisian_lilin` V1; CI **1297**;
adjudikasi **R-310 TEPAT**; **koreksi 516.135** yang meresmikan KC-50; kesembilan
baris MATI tak penuh; **H-A020 DIUSULKAN**.

**KESERASIAN VERSI — ketiga bagian kini serasi pada v50 / v10 / v10.**
Peringatan di kepala v9 (yang menyebut ketimpangan sudah selesai pada v49/v9/v9)
**GUGUR**: `STATE.md` sudah naik ke **v50** (blob
**`095a4b2cd8b6b5cadeb3e887ab72fa7dde4c81c3`**, commit `0c8ddac8`) dan EKOR sudah naik
ke **v10** (blob **`42fce0212c6f90581c39fc4df939616c479b6920`**, commit `7e7c3a65`).
Peringatan USANG SEBAGIAN di kepala EKOR v10 — yang menyatakan UKUR masih v9 dan
belum memuat `keterisian_lilin`, kesembilan baris, koreksi 516.135, dan H-A020 —
**DILUNASI oleh berkas ini**. Jejak peringatan lama sengaja tidak dihapus dari
riwayat; jangan memperlakukannya sebagai utang hidup. Pemecahan bertahap tetap
SENGAJA: menulis tiga berkas besar dari satu konteks terpakai adalah cara paling
pasti merusak aturan 1–84 (KC-42, KC-43).

**Tentang push berkas ini:** berkas ini di akar repo sehingga menyalakan `ci.yml`.
Tidak satu pun `tests/**` berubah, jadi cacah uji tetap **1297** — ramalan
deterministik (aturan 57), **MUDAH**, TIDAK masuk papan skor.

**Angka yang TIDAK berubah dari v44/v45/v6/v7** (tidak diulang): taksonomi 9 kelas,
karantina 12, bulan ABSEN 11, H-A013..H-A015, terhenti, SETTLED. Rinciannya di v44
(blob `d302caff`), v45 (`eb826817`), v6 (`27e59a79`), v7
(`4e7fb65be81bc5657da94060447075f0f1e2d73c`).

## KOREKSI KC-41 — BACA SEBELUM MENGUTIP BERKAS INI

Kelima koreksi di bawah **tetap dicantumkan** karena semuanya soal dokumen kami
sendiri, bukan soal data — menghapusnya berarti menghapus jejak cacat.

**Koreksi 1 (kesalahan berkas ini pada v5).** UKUR v5 menulis bahwa
`.github/workflows/lubang_awal.yml` ber-`paths` pada tiga entri. **ITU SALAH.** Berkas
asli (blob **`3134bc9f6f91c83ed39ff8424506ac253317edee`**) memuat **SATU** entri:

```
paths:
  - 'lux_ai/serapan/lubang_awal.py'
```

Aturan yang diperkuat: bila bagian STATE bertentangan, **berkas sumber menang**.
`lubang_tebing.yml` (`c8ae552a`), `byte_semesta.yml` (`45650ff9`),
`irisan_byte.yml` (`7d98a267`), `bulan_pertama.yml` (`2242e3e4`), dan
**`keterisian_lilin.yml` (`d821c63a`)** meniru berkas ASLI ini, bukan rumusan v5.

**Koreksi 2 (kesalahan PROMPT v49).** PROMPT v49 menyebut poros R-307 "H-A017";
yang benar **H-A018**. PROMPT v50 sudah memuat koreksi — **utang koreksi LUNAS**.

**Koreksi 3 [v9] (kesalahan v8 dan jurnal 129, dari DUGAAN bukan kutipan).**
v8 menulis bahwa MTLUSDT 2021-03, ENJUSDT 2020-09, SLPUSDT 2023-10, dan TLMUSDT
2023-03 "tampak bulan tengah" sehingga MELAWAN H-A019. **Tiga dari empat SALAH.**
Terukur oleh `bulan_pertama` V1: MTLUSDT 2021-03, ENJUSDT 2020-09, dan SLPUSDT
2023-10 justru bulan **PERTAMA** simbolnya di dalam penyebut. Yang benar-benar
melawan hanya **TLMUSDT 2023-03 (80.394 byte)**. Kalimat v8 itu **DICABUT**
(ADR-A016 kep. 4). Pelajaran: membaca daftar dengan mata lalu menyebutnya "tampak"
adalah tebakan, bukan ukuran.

**Koreksi 4 [BARU v10] — YANG TERBESAR SEJAUH INI. Angka 839.842.134 BUKAN jumlah
lilin.** Angka itu adalah **total baris parquet semesta** dari run rilis 30404071324,
dan dipakai berulang di jurnal serta lampiran seolah setara dengan jumlah lilin
1 menit. `keterisian_lilin` V1 menghitung LANGSUNG dari medan `cacah_lilin` atas
19.586 baris dan memperoleh **839.325.999**. **Selisih 516.135.** Seluruh aritmetika
implikasi jurnal 131 §6 dibangun di atas penyamaan itu, sehingga cacat di bahan baku,
meskipun R-310 tetap sah karena pitanya dikunci lebih dulu (aturan 29). Dari sinilah
**KC-50 naik menjadi resmi di STATE v50**. Dugaan penyebab — 19.598 − 19.586 = 12
simbol-bulan karantina, 516.135 / 12 = 43.011 ≈ sebulan penuh — **BELUM DIUJI dan
DILARANG dikutip sebagai penjelasan**.

**Koreksi 5 [BARU v10] — salah ketik di EKOR v10, dokumen kami sendiri.** Bagian
"Temuan sampingan" EKOR v10 (blob `42fce021`) menulis `terisi ≉49,7%`. Karakternya
salah: `≉` berarti "tidak kira-kira sama dengan", kebalikan dari yang dimaksud.
**Bacaan yang benar: ≈49,7%.** EKOR tidak didorong ulang untuk satu karakter
(KC-42), persis seperti perlakuan atas salah ketik jurnal 132 §3; koreksinya resmi di
berkas ini, dan berkas ini menang atas EKOR **pada titik itu saja**.

## Semesta riset = `perpetual_usdt` = penyebut 787 — tidak berubah

- `cacah_perpetual_usdt` **787** = `cacah_penyebut_simbol` **787**
- `cacah_perpetual_usdt_luar_penyebut` 0, `cacah_penyebut_bukan_perpetual_usdt` 0
- Batas wajib disebut: token saham/ETF/komoditas ikut di dalam 787.

## KC-18 — semesta kehidupan (dikonfirmasi ulang oleh R-307..R-310)

Atas **19.586** simbol-bulan lolos: **1.401 MATI** (7,153%), **98 SEPI**, **18.087
HIDUP**. Dari 1.401 MATI: 842 kehilangan funding, 559 tetap berfunding.
`cacah_simbol_tanpa_hidup` **18**.

`cacah_lain` = 0 pada keempat modul → seluruh 19.586 berstatus MATI/SEPI/HIDUP, tidak
ada TAK_TERUKUR. 18.087 + 98 = 18.185 TERUKUR, + 1.401 = 19.586 ✅

**Pembelahan atas penyebut yang sama [v9]:** **787** baris adalah bulan PERTAMA
simbolnya (tepat satu per simbol — identitas, bukan kebetulan), **18.799** baris
bukan-pertama. 787 + 18.799 = **19.586** ✅

**Pembelahan BARU [v10] atas kelas MATI:** dari 1.401 baris MATI, **1.392** berlilin
PENUH dan **9** tidak penuh. 1.392 + 9 = **1.401** ✅

## Lubang funding — agregat semesta (tetap)

- `cacah_simbol_ada_lubang` = **122** (dari 787) · awal **5** · bukan-awal **118**
- BNXUSDT punya lubang AWAL dan bukan-awal sekaligus.
- Lima bentuk AWAL: BNXUSDT, ICPUSDT, JUPUSDT, QTUMUSDT, TLMUSDT. ICP dan TLM lubang
  awalnya melewati kematian (sumber salah-baca R-304, KC-46).
- Lubang funding **880** semesta / **877** dalam penyebut / 3 tak dikenal. Irisan
  880 lawan 877 BELUM diukur.

## KETERISIAN LILIN [BARU v10 — pengukuran PERTAMA atas ISI bulan MATI]

Sumber: `keterisian_lilin.py` V1 run **30535202643** (commit
**`924b0d7afcf1f9e17965dff931d36489ad27f01b`**, kode 0). Laporan
`reports/keterisian_lilin.json` blob **`14f1772070789dad603b132ece034ea4c19c6e3d`**
(6.588 B, terbaca **UTUH** — `BATAS_BARIS_LAPORAN=40` berhasil untuk keempat kalinya
berturut), `reports/keterisian_lilin_ringkas.json` blob **`f33714eda66e77d37a7024b52c433ead070b16c7`**.

**Pertanyaan yang dijawab** — pertanyaan prioritas pertama ADR-A016 kep. 7, yang tiga
giliran berturut tidak terjawab: **apa isi berkas bulan MATI.** Jawabannya tegas.

| besaran | nilai |
| --- | --- |
| `cacah_mati_penuh` (lilin = lilin penuh bulannya) | **1.392** |
| `cacah_mati_tak_penuh` | **9** |
| `jumlah_lilin_langsung` (atas 19.586 baris) | **839.325.999** |
| `defisit_total` | **18.143.601** |
| `defisit_pertama` (bulan pertama simbol) | **17.335.439** (95,5%) |
| `defisit_bukan_pertama` | **808.162** |
| `bagian_defisit_bukan_pertama` | **0,0445** |
| `cacah_baris_dengan_medan` | **19.586** |
| `cacah_baris_tanpa_lilin` | **0** |
| `cacah_defisit_negatif` | **0** |
| `cacah_kunci_ganda` | **0** |
| `cacah_laporan_dibaca` | **8** dari 8 |
| `sidik_seragam` | **true** |

- **BULAN MATI PENUH DATANYA; YANG NOL ADALAH TRANSAKSINYA.** 1.392 dari 1.401
  (**99,4%**) bulan MATI berisi lilin sebanyak-banyaknya bulan itu. Bulan MATI bukan
  bulan yang datanya berhenti; ia bulan yang perdagangannya berhenti sementara
  lilinnya terus dicetak. Ini menutup pertanyaan ADR-A016 kep. 7.
- **DILARANG melanjutkan ke "harga beku" atau "lilin datar".** `medan_baris_terlihat`
  berisi **14** medan — `ada_di_arsip`, `bagian_volume_nol`, `bulan`, `byte_parquet`,
  `cacah_baris_cacat`, `cacah_lilin`, `cacah_lilin_terbaca`, `cacah_volume_nol`,
  `galat`, `gerbang_lolos`, `jalur`, `simbol`, `status`, `transaksi_total` — dan
  **tak satu pun harga**. Bentuk harga di dalam bulan MATI BELUM DIUKUR.
- **`cacah_baris_tanpa_lilin` = 0 sah dibaca** hanya karena kendali negatifnya
  membuktikan modul BISA mendeteksi baris tanpa lilin (aturan 50).
- **Defisit menumpuk di bulan pertama.** 17.335.439 dari 18.143.601 (**95,5%**) ada di
  787 bulan pertama; rata-rata **22.027** lilin hilang per bulan pertama, yaitu
  keterisian **≈49,7%**. Angka ini bersesuaian dengan nisbah byte 0,527179 dari R-309
  — dua jalur ukur berbeda memberi gambaran bulan pertama yang sama: **separuh**.
- **Kesembilan baris MATI tak penuh, LENGKAP** (semuanya `pertama: false`):

| # | simbol | bulan | `cacah_lilin` | lilin penuh | defisit |
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

  Jumlah defisit kesembilan **95.237** — hanya **0,1178** dari 808.162.
- **DUA ANOMALI LAMA LUNAS, DUA DARI DUA.** Baris 1 dan 2 adalah tepat kedua
  `cacah_mati_byte_kecil` R-308 (LENDUSDT 2020-11 = 97.634 byte, minimum kelas MATI;
  FRONTUSDT 2024-09 = 109.120 byte). Berkas MATI yang kecil itu kecil **karena
  lilinnya memang sedikit**, bukan karena hal lain. Meski begitu **larangan ADR-A015
  kep. 5 TIDAK dibalik**: menjelaskan dua kasus bukan membangun detektor, dan besar
  berkas tetap DILARANG dipakai sebagai penanda status ke arah mana pun.
- **TUJUH dari sembilan berbulan `2024-05` dengan jendela hanya SEMBILAN lilin**
  (39.308..39.317). Numerator 9 karena itu **BUKAN sembilan pengamatan bebas**; paling
  banter **tiga** (gugus 2024-05, LENDUSDT, FRONTUSDT). Ini kasus baru KC-47 dan
  penerapan aturan 81. **Kalimat "tujuh simbol didelisting 28 Mei 2024" DILARANG
  ditulis sebagai temuan** — yang terukur hanya jendela sembilan lilin.
- **SISA 712.925 LILIN BELUM DIJELASKAN.** 808.162 − 95.237 = **712.925** lilin
  defisit di baris bukan-pertama yang BUKAN baris MATI tak penuh. Baris mana yang
  menanggungnya belum diukur; ini pertanyaan terbuka nomor satu.
- **Lima penggugur bersih:** `sidik_seragam` true · 8/8 laporan dibaca ·
  `cacah_kunci_ganda` 0 · `cacah_defisit_negatif` 0 · `cacah_baris_tanpa_lilin` 0.
- **Kendali data sah:** tiga kendali BTCUSDT — 2021-05, 2021-08, 2021-01 — semuanya
  `cacah_lilin` **44.640** (bulan 31 hari penuh) dan berstatus HIDUP.
- **Delapan selisih invarian seluruhnya NOL dan seluruhnya BEBAS.** Seperti
  `bulan_pertama` dan berbeda dari `irisan_byte`, tidak ada medan turunan di dalam
  cacah itu; `jumlah_lilin_langsung` dihitung lewat jalur LANGSUNG dari baris —
  dan justru itulah yang memunculkan selisih 516.135 (Koreksi 4).
- **Adjudikasi R-310:** butir 1 **MENANG** (9 dalam 1..120), butir 2 **MENANG**
  (0,0445 dalam 0,02..0,25), butir 3 **MENANG** (MUDAH) → **TEPAT**. Bacaan jujurnya
  di EKOR v10 § Catatan kejujuran, termasuk peringatan bahwa **kedua kemenangan tipis
  ke tepi BAWAH** pita sehingga lebih murah daripada tampaknya.

**Sidik kode `keterisian_lilin` V1 =**
`1cd98f4fa22c24b30f31f5b36dac0ea0bb3fa9de44e5e15ae73cbf11cdca08bb`
**Sidik kode laporan (`sidik_kode_laporan`) =**
`24b6bb265525e81c2e571b46e401f36903383f1e3738c487850861adc3e8c595`

## IRISAN BULAN PERTAMA [v9, tetap berlaku]

Sumber: `bulan_pertama.py` V1 run **30532058657** (commit `09ce9853`, kode 0).
Laporan `reports/bulan_pertama.json` blob
**`0a2aa6ae15d949b44803dffdc9e97dbd322bbc85`**, `_status.json` blob
**`0c8ea41a5a1aea4090d0dd2de65c9652088fc462`**.

Definisi "bulan pertama" yang dipakai: bulan TERKECIL milik simbol itu **di dalam
penyebut 19.586** (yaitu yang lolos gerbang 1m) — bukan bulan pertama simbol itu di
bursa. Perbedaan keduanya BELUM diukur dan dicatat sebagai lubang ukur
(ADR-A016 kep. 6).

| besaran | nilai |
| --- | --- |
| `cacah_hidup_kecil_sebagian` (dari 38) | **37** |
| `bagian_hidup_kecil_sebagian` | **0,973684** |
| `cacah_pertama` (dari 19.586) | **787** |
| `cacah_bukan_pertama` | **18.799** |
| `jumlah_byte_pertama` | **706.233.745** |
| `jumlah_byte_bukan_pertama` | **32.000.028.630** |
| `rata_byte_pertama` | **897.374,517** |
| `rata_byte_bukan_pertama` | **1.702.219,726** |
| `nisbah_rata` | **0,527179** |

- **Irisan NYATA tetapi ASIMETRIS TAJAM.** 37 dari 38 berkas kecil adalah bulan
  pertama (**97,4%**); tetapi hanya 37 dari 787 bulan pertama yang berkas kecil
  (**±4,7%**). Rumusan resmi satu-satunya ada di **ADR-A016 kep. 1**.
- **Bulan pertama SEPARUH, bukan sepersepuluh** (0,527179) — **[v10] dikuatkan dari
  jalur ukur lain:** keterisian lilin bulan pertama ≈49,7%.
- **Klausa tepi `2026-06` menyumbang NOL secara bebas** (SQQQUSDT, TQQQUSDT,
  MVLLUSDT juga bulan pertama) — **DICABUT** (ADR-A016 kep. 2), melahirkan aturan 84
  yang kini RESMI di STATE v50.
- **Satu lawan tersisa:** **TLMUSDT 2023-03 (80.394 byte)** — bukan pertama, bukan
  tepi, tetap kecil. **[v10] TIDAK terjelaskan oleh R-310** — TLMUSDT 2023-03
  berstatus HIDUP, jadi ia tidak muncul di kesembilan baris MATI tak penuh. Belum
  dijelaskan; DILARANG dibuang sebagai pencilan.
- Kendali dua lapis sah: tiga parquet terbesar seluruhnya BTCUSDT (2021-05 2.770.666,
  2021-08 2.730.341, 2021-01 2.722.266, semuanya HIDUP); detektor semesta buatan lima
  baris dua simbol dengan jawaban dihitung TANGAN lebih dulu — `DETEKSI_PERTAMA` 2,
  `DETEKSI_HIDUP_KECIL` 2, `DETEKSI_SEBAGIAN` 2, `DETEKSI_NISBAH` 0,75,
  `DETEKSI_TOTAL_BYTE` 1.500 — seluruhnya cocok.

**`daftar_kecil_bertanda` (38, LENGKAP, urut byte menaik; `pertama` true untuk semua
kecuali TLMUSDT; `tepi` true untuk tiga baris `2026-06`):** JUPUSDT 2024-01 22.440 ·
TIAUSDT 2023-10 24.551 · REZUSDT 2024-04 32.164 · SLPUSDT 2023-10 33.257 ·
PORTALUSDT 2024-02 34.175 · NAORISUSDT 2025-07 34.673 · TROYUSDT 2024-10 35.511 ·
MDTUSDT 2023-06 36.580 · COSUSDT 2024-09 36.742 · GUNUSDT 2025-03 36.768 · CCUSDT
2025-10 37.116 · MAGMAUSDT 2025-12 37.327 · COLLECTUSDT 2025-12 38.486 · CKBUSDT
2023-02 39.079 · EDUUSDT 2023-04 39.749 · AIOTUSDT 2025-04 41.514 · PUNDIXUSDT
2025-04 42.561 · ADAUSDT 2020-01 42.678 · VFYUSDT 2025-09 44.460 · PLAYUSDT 2025-07
44.508 · COMPUSDT 2020-06 44.898 · MLNUSDT 2025-03 45.246 · EDENUSDT 2025-09 45.883 ·
RLCUSDT 2020-07 46.447 · FUNUSDT 2025-03 47.831 · MTLUSDT 2021-03 51.322 · YFIUSDT
2020-08 54.929 · ATAUSDT 2021-08 58.161 · ENSUSDT 2021-11 62.845 · ROSEUSDT 2021-12
63.592 · **SQQQUSDT 2026-06 72.819 (tepi)** · **TLMUSDT 2023-03 80.394
(pertama:false, tepi:false, sebagian:false)** · AMBUSDT 2023-03 81.419 · **TQQQUSDT
2026-06 82.330 (tepi)** · **MVLLUSDT 2026-06 86.126 (tepi)** · LEVERUSDT 2023-03
89.724 · INXUSDT 2026-01 94.575 · ENJUSDT 2020-09 94.658.

**Sidik kode `bulan_pertama` V1 =**
`0d3530f69ad51a22e038c17616411b56e4518698ff14c9b635131ec1e2a66562`

## LEBAR ZONA IRISAN BYTE [v8, tetap berlaku]

Sumber: `irisan_byte.py` V1 run **30529294165** (commit `d22364b9`, kode 0). Laporan
`reports/irisan_byte.json` blob **`4c13bf6afc36c9afbeb1c662d6098258a6b750dd`**,
`_status.json` blob **`863dc4cb266b2fcee56fb733960722d37bd931e7`**.

| besaran | nilai |
| --- | --- |
| `cacah_hidup_byte_kecil` (HIDUP, byte < **97.634**, STRIKT) | **38** |
| `bagian_hidup_byte_kecil` (penyebut 18.087) | **0.0021009564880853653** |
| `cacah_mati_byte_kecil` (MATI, byte < **150.000**, STRIKT) | **2** |
| `bagian_mati_byte_kecil` (penyebut 1.401) | **0.0014275517487508922** |

- **Zona 22.440–97.634 byte berisi 38 baris HIDUP dan NOL baris MATI.** Tafsir
  "kecil = mati" di zona itu **TERBALIK** (ADR-A015 kep. 5).
- **Ekor bawah MATI nyaris kosong.** Hanya **2** baris di bawah 150.000: LENDUSDT
  2020-11 = 97.634 dan FRONTUSDT 2024-09 = 109.120. Sebab kekalahan butir 2 R-308 →
  **KC-49**. **[v10] keduanya kini TERJELASKAN** sebagai dua baris MATI tak penuh
  dengan lilin paling sedikit di seluruh semesta.
- **Sebaran per kelas IDENTIK dari TIGA modul berbeda** (aturan 36):

| kelas | cacah | byte | byte_min | byte_maks | byte_rata |
| --- | --- | --- | --- | --- | --- |
| HIDUP | 18.087 | 32.049.492.952 | **22.440** | 2.770.666 | 1.771.962,899 |
| SEPI | 98 | 77.728.024 | 259.327 | 1.231.408 | 793.143,102 |
| MATI | 1.401 | 579.041.399 | **97.634** | 451.875 | 413.305,781 |

  `cacah_lain` 0 · `byte_lain` 0 · `total_byte` **32.706.262.375**.
- **Sembilan medan selisih semuanya 0 — tetapi hanya DELAPAN di antaranya bebas**
  (`total_byte` turunan). Menyebut "sembilan pemeriksaan bebas" DILARANG; ini kasus
  pertama **KC-50** yang kini resmi.
- `laporan_hilang` [] · `cacah_laporan_hilang` 0.

**Sidik kode `irisan_byte` V1 =**
`0e7103ef46a37d1e442d8e7fc5b9771b1ef7cdc3956ea57d584d84f6f73ea2c6`

## BYTE PARQUET ATAS SELURUH SEMESTA [v7, tetap berlaku]

Sumber: `byte_semesta.py` V1 run **30526358811** (commit `d3bc2039`, kode 0), laporan
blob `8b7f2077`. **Total byte parquet = 32.706.262.375** (≈32,7 GB) atas 19.586
simbol-bulan. `bagian_byte_mati` = **0.017704297493883234**;
`cacah_terukur_byte_kecil` (< 10.000) = 0; `cacah_byte_nol` = 0 → **dasar keras ≈22
KB**, sebab langsung KC-48. Kalimat v9 "bulan MATI bukan bulan KOSONG — APA ISINYA
BELUM DIUKUR" **kini DIJAWAB oleh R-310**: isinya lilin penuh dengan transaksi nol.
Adjudikasi R-307: **MELESET**.
Sidik `byte_semesta` V1 =
`e02aca2b3967069b500b01d27a1d2d1553f47b912ea41ddbecd9e4e6c33883c7`

## Arah waktu kematian lawan lubang funding [v6, `lubang_tebing` V1 — tetap]

Run **30524631435** (commit `84b11164`, kode 0), laporan blob `7d8883f5`. Penyebut
**118**.

| kelas arah (STRIKT, aturan 80) | cacah | bagian |
| --- | --- | --- |
| `mati_dulu` | **40** | **0.339** |
| `serempak` (DILARANG di numerator) | **78** | 0.661 |
| `lubang_dulu` | **0** | 0.000 |

`cacah_tebing_butir_2` **39**, bagian **0.3305** (`2025-07`); **39 dari 40**
`mati_dulu` ada di tebing (0.975); satu-satunya bukan-tebing **BTCSTUSDT** (lubang
2022-01, MATI 2021-04, `cacah_mati` 63) → KC-47, aturan 81. Adjudikasi R-306: TEPAT
3/3 — kemenangan sah, klaim ilmiah hampir kosong. Sidik `lubang_tebing` V1 =
`4a5c2e4279eb1554dc119b48d6a8db61f6ea4ee11b7539efd70ee71d1ae18bf3`

## Jumlah uji — terukur

**1297** — `reports/ci_terakhir.json` blob
**`3c07c9093d5232ce3852b2ac509fd9e9875f0f33`**, run **30535202643**, commit
**`924b0d7afcf1f9e17965dff931d36489ad27f01b`**, 2026-07-30T10:35:00Z, kode 0,
`1297 tests collected in 0.60s`. Riwayat: 814 → 832 → 879 → 936 → 984 → 1044 → 1100 →
1168 → 1233 → **1297**. Turunan: 1233 + **64** butir `tests/test_keterisian_lilin.py`
= **1297** ✅ (aturan 21).

Blob CI yang dicatat: 1168 = `2498e2cf6e6f6c7d0b8807bb5ba923ac1d803b6d` · 1233 =
`0489d71101e451efe73d20fd8fe75ba6d41c5c27` (run 30532058688, commit `09ce9853`) ·
1233 = `016fb2349a960100d270bec926e73d5b2c85e9cc` (run 30533500210, commit
`f8098980`) · **1297 = `3c07c909…`**.

**Aturan 57: beruntun 2 dari 2** sesudah PUTUS di 26/27. Ramalan kedua dibuat dengan
daftar bernomor `test_01`..`test_64` tanpa rentang; dua helper sengaja berawalan garis
bawah agar tidak dikumpulkan pytest.
Aturan 38 pemakaian ke-**tiga puluh tujuh** (ke-36 untuk CI 1233 blob `016fb234`,
ke-37 untuk CI 1297 blob `3c07c909`).

## Modul, workflow, dan berkas uji [v10]

**UTANG CACAH TANGAN HIDUP LAGI (aturan 66, KC-33).** Pencacahan TANGAN sah terakhir
ada pada ref **`07a69d395ea7cbc07bda506b59f3e97b4574a11f`**: `lux_ai/serapan/` **47**,
`tests/` **51**, `.github/workflows/` **42**. Sesudah trio `keterisian_lilin`, angka
turunan menjadi 48 / 52 / 43 — **TURUNAN, DILARANG dikutip sebagai terukur** sampai
dicacah satu per satu bernomor pada ref pasca-R-310. Ini utang verifikasi nomor 29 di
EKOR v10.

Blob trio R-310 (ketiganya dibaca ulang UTUH dari main sesudah push `924b0d7a`,
aturan 52 dan 55):

- `lux_ai/serapan/keterisian_lilin.py` V1 blob
  **`3f80ffa72008008d567ef32f9f278b8931e91ac3`**.
- `tests/test_keterisian_lilin.py` blob
  **`f58912d0b1531dbf537de4c0b4f0a803a3ad1f69`** (**64** butir, dicacah TANGAN
  `test_01`..`test_64`; daftar bernomor utuh di kepala berkas; dua helper
  `_ringkasan_sehat` dan `_selisih_nol` berawalan garis bawah).
- `.github/workflows/keterisian_lilin.yml` blob
  **`d821c63a462a8338ccd63f8014f7c8847602fdff`** (`paths` **SATU** entri).

Blob trio v9 tetap: `bulan_pertama.py` `b9bd00ac` (19.349 B) ·
`test_bulan_pertama.py` `75d87ba2` (13.375 B, 65 butir) · `bulan_pertama.yml`
`2242e3e4`. Blob lain identik dengan v8/v9: `irisan_byte.py` `2dbe3d55`,
`test_irisan_byte.py` `b6389051` (68 butir), `irisan_byte.yml` `7d98a267`,
`kehidupan.py` `f49abb2b`, `kehidupan_arsip.py` `318a5cb1`, `silang_funding.py` V2
`42c3aa9d`, `kohort_ekor.py` `c9b63bbe`, `lubang_awal.py` `8c36943d`,
`lubang_tebing.py` `575e777e`, `lubang_tengah.py` `4d3beaf1`, `sebab_bangkit.py`
`fd5a1dc4`, `tersisip_semesta.py` `8a648838`, `bentangan_kohort.py` V2 `f4eae57a`,
`byte_semesta.py` `ff68e4be`, `funding.py` `8d4b1f82`, `arsip.py` `0104958b`,
`gerbang_1m.py` `c8cc54c8`, `resample.py` `66a4b177`. `ci.yml` = `c79497b2`
(paths-ignore journal/decisions/hipotesis/reports; push ke `lux_ai/**`, `tests/**`,
`STATE*`, `PROMPT*` MENYALAKAN CI). `karantina_semesta.yml` = `de40fa4e` (belum
dibaca utuh).

Cacah per berkas uji yang diketahui: `test_irisan_byte.py` **68** ·
`test_bulan_pertama.py` **65** · `test_keterisian_lilin.py` **64** ·
`test_bentangan_kohort.py` V2 **63** · `test_lubang_tebing.py` **60** ·
`test_sebab_bangkit.py` **57** · `test_byte_semesta.py` **56** ·
`test_lubang_awal.py` **48** · `test_tersisip_semesta.py` **47** ·
`test_anatomi_tengah.py` **47** · `test_terhenti.py` V4 **33** ·
`test_bulan_absen.py` **32** · `test_karantina_semesta.py` **28** ·
`test_silang_settled.py` **24**.

**Pola workflow trio (terbukti lagi pada `keterisian_lilin.yml`, dibaca UTUH):**
`name`, `on.push.paths` SATU entri, `permissions: contents: write`, job `ukur` di
`ubuntu-latest`, checkout@v4 + setup-python@v5 (3.11), `pip install numpy pandas
pyarrow pyyaml`, langkah `jalan` id=`jalan` dengan `set +e` → `KODE=$?` →
`echo "kode=$KODE" >> "$GITHUB_OUTPUT"` → `exit 0`, langkah `catat status` (printf
JSON ke `reports/<modul>_status.json`), langkah `dorong laporan` (git config bot,
add, commit `[skip ci]`, pull --rebase, push), langkah akhir
`exit ${{ steps.jalan.outputs.kode }}`.

## API terverifikasi — tambahan v10

API lama (v37–v9) tetap berlaku. Tambahan:

**`keterisian_lilin` V1** (blob `3f80ffa7`, dibaca UTUH dari `924b0d7a` sesudah push):
mengimpor `kehidupan`, `kehidupan_arsip`, `silang_funding`.
Tetapan: `VERSI=1`, `TOTAL_PECAHAN=kehidupan_arsip.TOTAL_PECAHAN`,
`KELUARAN="reports/keterisian_lilin.json"`,
`KELUARAN_RINGKAS="reports/keterisian_lilin_ringkas.json"`,
`BATAS_BARIS_LAPORAN=40`, **`MENIT_PER_HARI=1440`**, **`MEDAN_LILIN="cacah_lilin"`**,
`KENDALI_SIMBOL="BTCUSDT"`, `KENDALI_CACAH=3`, `AMBANG_HIDUP_KECIL=97634`,
**`R310_PITA_BUTIR_1=(1,120)`**, **`R310_PITA_BUTIR_2=(0.02,0.25)`**,
`BERKAS_DICAP=["kehidupan.py","kehidupan_arsip.py","keterisian_lilin.py",
"silang_funding.py"]`, `INVARIAN` **delapan** kunci (19586, 787, 18087, 98, 1401,
32706262375, 32049492952, 38) — **seluruhnya BEBAS**, `JAWABAN_KENDALI`
(3, 1, 1160, 520, 640, 213400, 0, 0.5517).
Fungsi: `nama_keluaran`, `nama_ringkas`, `daftar_sumber`, `sidik_kode`,
**`hari_dalam_bulan`**, **`lilin_penuh`**, **`defisit`**, `peta_bulan_pertama`,
`kumpulkan`, `ringkas_defisit`, **`baris_mati_tak_penuh`**, `cacah_mati_tak_penuh`,
`cacah_mati_penuh`, `bagian_defisit_bukan_pertama`, `potong`, `dalam_pita`,
`dalam_pita_pecahan`, `invarian_terukur`, `selisih_invarian`, `kendali_data`,
`kendali_data_sah`, `semesta_kendali`, `kendali_deteksi`, **`kendali_negatif`**,
`uji_r310`, `kode_keluar`, `jalankan(akar=".", total=None)`, `berkas_ringkas`, `main`.
**Yang wajib disebut:** `jumlah_lilin_langsung` dihitung LANGSUNG dari baris, bukan
disalin dari angka tercatat — penerapan wajib KC-50 (ADR-A016 kep. 5), dan justru itu
yang memunculkan selisih 516.135. `kendali_negatif` membuktikan modul BISA melihat
baris tanpa lilin, sehingga `cacah_baris_tanpa_lilin = 0` boleh dibaca (aturan 50).

**`bulan_pertama` V1** (blob `b9bd00ac`): `VERSI=1`,
`KELUARAN="reports/bulan_pertama.json"`, `BATAS_BARIS_LAPORAN=40`,
`AMBANG_HIDUP_KECIL=97634`, `BULAN_TEPI="2026-06"`, `R309_PITA_BUTIR_1=(22,38)`,
`R309_PITA_BUTIR_2=(0.10,0.60)`, `INVARIAN` delapan kunci, `MEDAN_SELISIH` 8
(seluruhnya BEBAS), `KENDALI_DATA` 3 baris BTCUSDT, `DETEKSI_AMBANG=250`,
`DETEKSI_PERTAMA=2`, `DETEKSI_HIDUP_KECIL=2`, `DETEKSI_SEBAGIAN=2`,
`DETEKSI_NISBAH=0.75`, `DETEKSI_TOTAL_BYTE=1500`. Fungsi: `nama_keluaran`,
`sidik_kode`, `_bagian`, `kelas_status`, `peta_bulan_pertama`, `penanda_baris`,
`sebaran_per_kelas`, **`total_byte_langsung`**, `cacah_di_bawah`, `cacah_sebagian`,
`daftar_kecil_bertanda`, `nisbah_pertama` (penyebut kosong → **None**),
`selisih_invarian`, `dalam_pita`, `dalam_pita_pecahan`, `kendali_data`,
`kendali_deteksi`, `ringkaskan`, `uji_r309`, `kode_keluar`,
`jalankan(akar=".", total=None)`, `main`.

**`irisan_byte` V1** (blob `2dbe3d55`): `AMBANG_HIDUP_KECIL=97634`,
`AMBANG_MATI_KECIL=150000`, `R308_PITA_BUTIR_1=(20,600)`,
`R308_PITA_BUTIR_2=(10,300)`, `INVARIAN` 9 kunci, `MEDAN_SELISIH` **9** (delapan
bebas + satu turunan), `DETEKSI_TOTAL=1922`. Rincian penuh di v8.

**`silang_funding` V2** (blob `42c3aa9d`, 29.873 B): `baca_laporan_kehidupan(akar,
total)` → **TIGA** nilai `(status, byte_parquet, meta)`, kunci tuple
`(simbol, bulan)`; **`baca_medan_baris(akar, total, medan)`** → `(nilai, meta)`,
MELEWATI baris ber-medan `None` — dipakai `keterisian_lilin` dengan
`medan="cacah_lilin"`, terbukti lagi (KC-43 terjaga); `bulan_per_simbol(status)`;
`lubang_funding(funding)`; `kendali_silang`; `kendali_sah`; `bentuk_lubang_lokal`;
`SUMBER_FUNDING="reports/funding_semesta.json"`, `KENDALI_CACAH=3`,
`PENYEBUT_TERCATAT=19586`, `MATI_TERCATAT=1401`, `KOHORT_TERCATAT=456`,
`HIDUP_TANPA_FUNDING_TERCATAT=33`, `LUBANG_TAK_DIKENAL_TERCATAT=3`,
`BENTUK_TERBITAN_FUNDING={"awal":48,"ekor":826,"tengah":6}`.

**`byte_semesta` V1** (blob `ff68e4be`): `R307_PITA_BUTIR_1=(0.02,0.15)`,
`R307_AMBANG_BYTE_KECIL=10000`, `R307_PITA_BUTIR_2_CACAH=(20,400)`,
`BATAS_BARIS_LAPORAN=40`, `MEDAN_SELISIH` 9. Rincian penuh di v7.

**`lubang_awal` V1** (`8c36943d`): `peta_status`, `ringkas`, `himpun`, `bulan_urut`,
`bangkit_lokal`, `kendali_deteksi`, `dalam_pita`, `uji_r305`, `kode_keluar`;
`POLA_BULAN=re.compile(r"^\d{4}-\d{2}$")`; `BATAS_BARIS_LAPORAN=60`. Medan
`mati_tidak_setelah_lubang_bukan_awal` memakai `<=` — **DILARANG dipakai untuk klaim
arah** (aturan 80). Sidik `156499ce…`.
`lubang_tebing` V1 (`575e777e`): rincian di v6; `BATAS_BARIS_LAPORAN=60`.
`kohort_ekor` V4 (`c9b63bbe`): `TEBING="2025-07"`, `BULAN_DIHARAPKAN="2026-06"`,
`BATAS_SIMBOL=10`, `PAGU_MUNDUR=60`, `AMBANG_SEPI=0.5`,
`KENDALI_HIDUP=("BTCUSDT","ETHUSDT")`.
`kehidupan_arsip` (`318a5cb1`): `TOTAL_PECAHAN=8`, `AKAR_UNDUH="data/unduh"`,
`AKAR_BONGKAR="data/kehidupan_arsip"`, `KOLOM_VOLUME="volume"`,
`KOLOM_TRANSAKSI="trades"`, `nama_keluaran(i)`.
`kehidupan` (`f49abb2b`): `AMBANG_SEPI=0.5`, `STATUS_MATI/SEPI/HIDUP/TAK_TERUKUR`,
`BULAN_MULAI="2025-07"`, `BULAN_AKHIR="2026-06"`, `deret_bulan`, `klasifikasi`,
`penyebut_ganda`.

Sidik lain: `sebab_bangkit` V1 `bafe4359e8f36f0402d4be4a4e4aef4a28f224f6419f06f701fb3a5bf696221a` ·
`tersisip_semesta` V1 `9618fd19e4ab2e7b5279177db600f6176afd914ab1e94576e54197f70ebc537c` ·
`bentangan_kohort` V2 `8ca6ebbefc3606464ebd7f94c6b51b1fdf500c62779cdcb5700ec2ee4ea9f32c` ·
`sidik_data_funding` `2c9fbd1b04f74c9c844bc223a99a103d12220b88d08667b3792720e5b9608d24` ·
`sidik_kode_silang_funding` seragam
`8a9b859c09cd64e30e203e6f8dc53411b8e341c44f112805b3041e5d4d3231b1` ·
laporan kehidupan seragam
`24b6bb265525e81c2e571b46e401f36903383f1e3738c487850861adc3e8c595`.
Keempatnya COCOK lagi pada run `keterisian_lilin` (aturan 36, kini empat run
berturut) → semesta SAMA.

## Hipotesis

- H-A001 belum diuji · H-A002b GUGUR · H-A003 MENANG pada 3, GUGUR pada 9 · H-A004
  tak dapat diuji · H-A005 GUGUR · H-A006 MENANG enam run · H-A008 MENANG dua kali ·
  H-A009 GUGUR · H-A010 MENANG 5–0 · H-A011 MENANG · H-A012 MENANG · H-A013 MENANG
  6–0, TAFSIR DICABUT · H-A014 BENTUK BARU MENANG 9 dari 9 · H-A015 MENANG sebagai
  angka, DIBATASI sebagai tafsir (KC-45) · H-A016 PENGAMATAN, BELUM DIUJI.
- **H-A017** DICABUT sebagai pola semesta (ADR-A011/A012, dilemahkan R-306): bukti
  lepas-tebing tinggal **1** simbol. TIDAK dipulihkan oleh R-307..R-310 — keempatnya
  tidak menyentuh arah sebab.
- **H-A018 — byte parquet sebagai gejala kehidupan. DIUKUR DUA KALI (R-307, R-308).**
  **Bunyi yang BOLEH dipakai:** "bulan MATI menempati bagian KECIL dari byte semesta
  (**0,0177** dari 32,7 GB) dan rata-rata sekitar **4,3×** lebih kecil daripada bulan
  HIDUP (413.306 lawan 1.771.963 byte)".
  **Bunyi yang DILARANG:** "berkas kecil berarti pasar mati" — di zona 22.440–97.634
  byte ada **38 HIDUP dan 0 MATI**. **[v10] R-310 TIDAK membalik larangan ini**,
  meski ia menjelaskan kedua berkas MATI terkecil lewat cacah lilinnya.
- **H-A019 [DIUJI R-309 — DITERIMA TERBATAS oleh ADR-A016 kep. 1].**
  **Rumusan resmi satu-satunya yang boleh dikutip:** *hampir setiap baris HIDUP di
  zona byte kecil adalah bulan pertama simbol itu di dalam penyebut (**37 dari 38**),
  sementara hampir setiap bulan pertama BUKAN berkas kecil (**37 dari 787, ±4,7%**).*
  Irisan asimetris, bukan sebab. Klausa `2026-06` DICABUT (kep. 2). Batas tafsir:
  "bulan pertama" = di dalam penyebut 19.586, bukan di bursa (kep. 6). Lawan yang
  tersisa: **TLMUSDT 2023-03**, dan R-310 tidak menjelaskannya.
  **[v10] DIKUATKAN dari jalur ukur kedua:** bulan pertama menanggung **95,5%**
  defisit lilin semesta dan terisi **≈49,7%** — sebangun dengan nisbah byte 0,527179.
- **H-A020 [DIUSULKAN di STATE v50, BELUM DIUJI].** *Ketujuh baris MATI tak penuh
  berbulan `2024-05` adalah SATU peristiwa, bukan tujuh pengamatan bebas: jendelanya
  hanya sembilan lilin (39.308..39.317).* Larangan yang menyertainya: DILARANG
  menulis "tujuh simbol didelisting 28 Mei 2024" sebagai temuan — tanggal itu TIDAK
  terukur, yang terukur hanya lebar jendela. Cara mengujinya: `lubang_tengah` atas
  gugus 2024-05 untuk melihat apakah lilin yang hilang berada di posisi yang sama.
- Hipotesis berikutnya **H-A021**.

## Praregistrasi R-309 — SUDAH TERADJUDIKASI: TEPAT

Disimpan apa adanya sebagai jejak (aturan 29). Poros **H-A019**.

- **Butir 1 (BERISIKO).** Dari 38 baris HIDUP ber-byte < 97.634, cacah yang merupakan
  bulan PERTAMA simbol ATAU bulan `2026-06`. Pita **22 .. 38** → **37** → **MENANG**.
- **Butir 2 (BERISIKO).** Nisbah rata byte bulan PERTAMA terhadap bulan BUKAN-pertama
  atas 19.586 baris. Pita **0.10 .. 0.60** → **0,527179** → **MENANG** (tipis ke tepi
  atas).
- **Butir 3 (MUDAH).** Delapan invarian nol, dua kendali sah, kode 0, CI → **MENANG**.

**Cacat praregistrasi yang ditemukan SESUDAH menang:** butir 1 memakai klausa ATAU
yang salah satu cabangnya menyumbang NOL secara bebas — dasar **aturan 84**, kini
RESMI di STATE v50.

## Praregistrasi R-310 — SUDAH TERADJUDIKASI: TEPAT

Disimpan apa adanya sebagai jejak (aturan 29); teks disalin dari jurnal 131 §7 dan
TIDAK diubah sesudah pengukuran. Poros: **isi berkas bulan MATI** (ADR-A016 kep. 7).
Aritmetika implikasi ditulis lebih dulu (aturan 83) dan **tiga calon butir dibuang
karena jawabannya sudah tertentu**; kedua butir berisiko sengaja berklausa TUNGGAL
(aturan 84).

- **Butir 1 (BERISIKO).** Cacah baris MATI ber-`cacah_lilin` KURANG dari lilin penuh
  bulannya, dari penyebut **1.401**. Pita **1 .. 120**. Penyebut 0 → TIDAK
  TERADJUDIKASI (aturan 41). → terukur **9** → **MENANG** (tipis ke tepi BAWAH).
- **Butir 2 (BERISIKO).** Bagian defisit lilin semesta yang ditanggung baris
  BUKAN-pertama. Pita **0.02 .. 0.25**. → terukur **0,0445** → **MENANG** (tipis ke
  tepi BAWAH).
- **Butir 3 (MUDAH).** Delapan selisih invarian nol, TIGA kendali sah, lima penggugur
  bersih, kode keluar 0, CI diukur. → **MENANG**.

**Tiga calon butir yang DIBUANG sebelum pita dikunci** (jejak aturan 83 bekerja
sebagai pencegah): (a) cacah baris MATI berlilin PENUH — dihitung ≈1.370–1.401
sebelum mengukur, **terukur 1.392**, akan menjadi kemenangan murahan; (b) cacah MATI
ber-`cacah_lilin` < 1.440 — hampir pasti 0; (c) nisbah byte-per-lilin MATI:HIDUP —
tersirat 0,233.

**Cacat yang ditemukan SESUDAH menang:** numerator 9 bukan sembilan pengamatan bebas
(KC-47, tujuh di antaranya gugus `2024-05`), dan bahan baku taksirannya memakai
839.842.134 yang ternyata bukan jumlah lilin (Koreksi 4, KC-50).

## Praregistrasi R-311 — BELUM ADA

Poros belum ditetapkan; ADR-A016 menolak penyusunan percobaan pada giliran yang sama
dengan adjudikasi. Calon urut kekuatan, dari jurnal 132 §14:

1. **Sisa 712.925 lilin** — baris mana yang menanggung defisit bukan-pertama di luar
   kesembilan baris MATI tak penuh. Ini pertanyaan terbuka nomor satu dan porosnya
   paling bersih karena angkanya sama sekali belum tersirat.
2. **Selisih 516.135** lawan dugaan 12 simbol-bulan karantina (516.135 / 12 = 43.011).
   Peringatan aturan 83: dugaan itu sudah menghasilkan satu angka; bila pita disusun
   di sekitar 43.011 maka butirnya hampir tidak berisiko — porosnya harus dipindahkan
   ke bentuk sebaran, bukan ke rata-rata.
3. **Lubang tengah gugus `2024-05`** untuk menegakkan atau meruntuhkan **H-A020**.

Sebelum pita dikunci: aturan 83 WAJIB dipenuhi di jurnal lebih dulu; aturan 84 WAJIB
diperhatikan bila ada butir berklausa ATAU; nama modul WAJIB dicek lewat pencacahan
direktori TANGAN lebih dulu (aturan 66 — utang 48/52/43 masih hidup); laporan WAJIB
ringkas (`BATAS_BARIS_LAPORAN`).
