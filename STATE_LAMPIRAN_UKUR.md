# STATE lampiran UKUR — bagian 3 dari STATE v42

**Kedudukan berkas ini.** Sejak v42 STATE dipecah karena `STATE.md` melampaui batas
satu push (KC-42). Pembagian yang berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan bernomor 1–76, kelas cacat KC-1..KC-42.
2. **`STATE_LAMPIRAN_UKUR.md`** (berkas ini) — bagian 3: seluruh bagian pengukuran,
   modul, API, dan hipotesis.
3. **`STATE_LAMPIRAN_EKOR.md`** (blob `7480cedd1f9b4bbe1b9d091ac9f8a6c59c95c139`) —
   bagian 2: papan skor, catatan kejujuran, jumlah uji, utang verifikasi, ADR,
   temuan sampingan, penomoran berikutnya.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip ekor v41, sudah diserap;
   bukan sumber lagi.

Seluruh angka di sini disalin dari `STATE.md` **v41** yang dibaca UTUH (blob
**`b02061545da86b371e8f07766673bb5d0893da56`**). Tidak ada angka baru yang lahir di
berkas ini; ia pemindahan, bukan pengukuran. `STATE.md` v43 wajib menunjuk ke sini
dan berhenti sesudah kelas cacat.

**Praregistrasi R-296 (ditulis SEBELUM push ini menyalakan `ci.yml`).** Karena
`ci.yml` memakai `paths-ignore` dan berkas ini berada di akar repo (KC-41), push ini
MENYALAKAN CI. Tidak satu pun berkas `tests/**` berubah, jadi cacah tetap **722**
dan `kode_keluar` **0**. Ramalan ini **MUDAH** — ia hanya menyalin angka
terverifikasi (aturan 57).

## Semesta riset = `perpetual_usdt` = penyebut 787 — TERBUKTI TIGA ARAH

Sumber: `semesta_kuota.py` **V3**, commit `db4a192d`, run 30456422183, laporan blob
`8adae5ee` (UTUH), `sidik_kode` `ef0c4a24…`, `bukan_bukti` false.

- `cacah_perpetual_usdt` **787** = `cacah_penyebut_simbol` **787**
- `cacah_perpetual_usdt_luar_penyebut` **0** · `cacah_penyebut_bukan_perpetual_usdt`
  **0** · `cacah_penyebut_bukan_akhiran_usdt` **0** · `cacah_penyebut_luar_arsip`
  **0** · `penyebut_bagian_arsip` true.
- **Arah ketiga:** `bulan_absen` V1 menemukan `cacah_nama_penyebut` **787**
  (`selisih_nama_penyebut` 0) dan dari manifes `cacah_nama_didaftar` **787** — kode
  lain, bahan lain, angka sama (aturan 69).

Karena KEDUA arah nol, ini **kesamaan himpunan**, bukan himpunan bagian.

Batas yang wajib ikut disebut (`taksonomi.CATATAN_BATAS`): token **saham, ETF, dan
komoditas** (mis. `AAPLUSDT`, `XAUUSDT`) tak dapat dibedakan lewat bentuk nama, jadi
mereka **IKUT di dalam 787**. `AAPLUSDT:2026-05` terbukti nyata di sampel
`diagnosa_kc15` dan bulannya lolos gerbang bersih.

### Taksonomi kanonik — sembilan kelas

`lux_ai/semesta/taksonomi.py` (blob `b418c7ba`, **belum dibaca ulang sejak v37 —
premis "beroperasi atas 937 nama arsip" tetap ASUMSI**). Urutan pemeriksaan
MENGIKAT: pola ekspirasi `_\d{6}$` → akhiran `SETTLED` → daftar `INDEKS` → kutipan
`("USDT","USDC","BUSD","USD1","BTC")` dengan `BTC` sebagai `KUTIPAN_NON_FIAT`.
`INDEKS` = {`DEFIUSDT`, `BTCDOMUSDT`, `BLUEBIRDUSDT`}, manual, tersurat. Maka **790
nama berakhiran USDT = 787 perpetual + 3 indeks**, tanpa sisa.

| jenis kanonik | nama (arsip 937) | bulan | hanya-arsip (150) | bulan |
|---|---:|---:|---:|---:|
| `perpetual_usdt` | **787** | **19.598** | 0 | 0 |
| `futures_kedaluwarsa` | 50 | 258 | 50 | 258 |
| `perpetual_busd` | 41 | 812 | 41 | 812 |
| `perpetual_usdc` | 39 | 893 | 39 | 893 |
| `sisa_settled` | 15 | 36 | 15 | 36 |
| `indeks` | 3 | **151** | 3 | **151** |
| `perpetual_usd1` | 1 | 2 | 1 | 2 |
| `basis_non_fiat` | 1 | 39 | 1 | 39 |
| `tak_tergolong` | **0** | 0 | 0 | 0 |
| **jumlah** | **937** | **21.789** | **150** | **2.191** |

Dihitung tangan (aturan 21): 787+50+41+39+15+3+1+1 = **937** ✅ ·
19.598+258+812+893+36+151+2+39 = **21.789** ✅ · 21.789 − 2.191 = **19.598** ✅

**ANGKA WARISAN YANG DICABUT.** "16 simbol non-ASCII" adalah HANTU. Terukur **3
nama / 19 bulan**: 币安人生USDT 9, 我踏马来了USDT 6, 龙虾USDT 4; 9+6+4 = **19** ✅
Ketiganya `perpetual_usdt`, jadi ADA di penyebut. Asal-usul angka 16 belum diketahui.

### Taksonomi LOKAL modul (kuota) — dipertahankan berdampingan

USDT 805 nama/19.785 bulan (15 SETTLED) · TAK_DIKENAL 51/260 · BUSD 41/812 · USDC
39/893 · BTC 1/39. `TAK_DIKENAL` 51 = 50 `futures_kedaluwarsa` + 1 `perpetual_usd1`
(`BTCUSD1`); 258 + 2 = 260 ✅ **150 hanya-arsip = 147 bukan-akhiran-USDT + 3
indeks**; dari 147 itu BUSD+USDC = **80** (54,4%).

### Penguraian selisih 163 — identitas utuh, bernama, TERUKUR

`bulan_usdt_bukan_settled` 19.749 · `bulan_arsip_milik_penyebut` **19.598** ·
`bulan_arsip_milik_hanya_arsip` **151** · `bulan_lolos_gerbang` 19.586 ·
`selisih_total` **163** · `selisih_dalam_penyebut` **12** ·
`selisih_dari_hanya_arsip` **151** · `identitas_utuh` true.
19.598 + 151 = 19.749 ✅ · 12 + 151 = 163 ✅ · 19.598 − 19.586 = **12** ✅
**151 bulan itu SELURUHNYA milik ketiga indeks.**

## Daftar karantina — TERUKUR [v41, `karantina_semesta` V1]

Sumber: `karantina_semesta.py` V1 (blob **`46e7c46b`**, UTUH), laporan
`reports/karantina_semesta_ringkas.json` blob **`a247ee3f`** pada ref runner
**`d9e44119`** (run **30479681799**, commit `edea61f7`), UTUH;
`karantina_semesta_status.json` blob `e99d7225` mencatat `kode_keluar` **0**.
`sidik_kode` `ad30150e…`, `versi_karantina_semesta` 1, `bukan_bukti` false. Laporan
penuh `reports/karantina_semesta.json` belum dibaca.

**Mengapa modul ini harus ada:** `reports/manifes_pecahan_2.json` 2.446.093 byte
DITOLAK alat baca agen, sehingga daftar karantina tak mungkin dibaca langsung
(aturan 52, 73).

Penggugur SELURUHNYA aman (aturan 24): `cacah_manifes_dibaca` **8/8** ·
`manifes_hilang` [] · `cacah_kunci_ganda` **0** · `jumlah_selisih_cacah_daftar`
**0** · `cacah_daftar_terpotong` **0** · `jumlah_cacah_dibuang` **0** ·
`jumlah_cacah_ditambal` **0** · `jumlah_karantina_tak_terkemas` **0** ·
`selisih_ditulis_terdaftar` **0** · `sidik_seragam` true (satu sidik `237ccf42…`) ·
`kendali_sah` true (BTCUSDT 0, ETHUSDT 0).

`cacah_karantina_semesta` **12** · `cacah_kunci_unik` **12** · `selisih_penyebut`
**0** · `byte_parquet_karantina_semesta` **13.247.705** (`selisih_byte_tercatat`
**0**, = KC-17) · `cacah_tanpa_parquet_karantina` **0** ·
`cacah_pecahan_berkarantina` **6** · `pecahan_tanpa_karantina` **[2, 5]** ·
`sebaran_pelanggaran` = {`jarak_60_detik` **12**, `tanpa_menit_hilang` **12**}
(baca sebagai negasi, KC-40).

| # | simbol | bulan | pecahan | baris | menit kalender | selisih | `nisbah_lilin` |
|---|---|---|---:|---:|---:|---:|---:|
| 1 | AERGOUSDT | 2025-04 | 0 | 42.540 | 43.200 | 660 | 0,984722 |
| 2 | AIAUSDT | 2026-01 | 7 | 43.965 | 44.640 | 675 | 0,984879 |
| 3 | BNXUSDT | 2022-04 | 6 | 41.550 | 43.200 | 1.650 | 0,961806 |
| 4 | BNXUSDT | 2022-06 | 6 | 41.760 | 43.200 | 1.440 | 0,966667 |
| 5 | BNXUSDT | 2022-08 | 6 | 40.320 | 44.640 | 4.320 | 0,903226 |
| 6 | CTKUSDT | 2025-04 | 3 | 42.585 | 43.200 | 615 | 0,985764 |
| 7 | CVCUSDT | 2025-05 | 0 | 44.130 | 44.640 | 510 | 0,988575 |
| 8 | CVXUSDT | 2025-07 | 1 | 43.950 | 44.640 | 690 | 0,984543 |
| 9 | LITUSDT | 2025-12 | 4 | 43.590 | 44.640 | 1.050 | 0,976478 |
| 10 | MAVIAUSDT | 2025-03 | 1 | 43.620 | 44.640 | 1.020 | 0,977151 |
| 11 | PUMPUSDT | 2025-07 | 1 | 44.190 | 44.640 | 450 | 0,989919 |
| 12 | SLPUSDT | 2025-07 | 0 | 43.935 | 44.640 | 705 | 0,984207 |

Sebaran per pecahan 3, 3, 0, 1, 1, 0, 3, 1 = **12** ✅ Himpunan ini SAMA PERSIS
dengan sebelas bulan ABSEN + BNXUSDT 2022-04 di tepi (aturan 69; KC-39 tetap
mengikat atas cara mencacahnya). **Yang TETAP belum diukur:** kehidupan kedua belas
bulan itu (MATI/SEPI/HIDUP tak dapat ada, sebab di luar penyebut 19.586) dan
**TANGGAL** hari-hari yang hilang.

**Berlilin SEBAGIAN, celah kelipatan 15.** `nisbah_lilin` terendah **0,903226**
(BNX 2022-08), tertinggi **0,989919** (PUMP 2025-07); tak satu pun mendekati nol.
Seluruh dua belas selisih habis dibagi **15**: 660, 675, 1.650, 1.440, 4.320, 615,
510, 690, 1.050, 1.020, 450, 705 → 44, 45, 110, 96, 288, 41, 34, 46, 70, 68, 30,
47. Ini melahirkan **H-A016**. Tak ada bilangan yang dipraregistrasi untuk gejala
ini, jadi ia bukan kemenangan ramalan.

**KC-15 [DIKOREKSI v39, DILENGKAPI v41].** BNXUSDT 2022-04 kehilangan **1.650**
menit (1.440 tengah + 210 tepi), 2022-06 **1.440**, 2022-08 **4.320**; jumlah
**7.410** − 210 = **7.200** = 5 × 1.440 ✅ Lima hari terbagi **1 + 3 + 1**. Hari-hari
itu UTUH di arsip HARIAN (jurnal 109 §5.2 DICABUT); yang tak terjelaskan hanyalah
**210 menit TEPI** 2022-04, konsisten dengan peluncuran **03:30 UTC**
(`stempel_pertama_ms` 1648783800000; berkas harian 2022-04-01 memuat 1.230 = 1.440
− 210 baris; `menit_tepi_hadir` 0 dari 210). Anatomi lain 2022-04:
`menit_hilang_di_tengah` **1.440**, `gerbang_lolos` false, `putusan`
TEPI_TAK_TERJELASKAN, `checksum_bulanan` `14bd6937…`. 9 + 3 = **12** karantina;
6.375 + 7.200 = **13.575** menit; **516.135** baris.

## Bulan ABSEN — TERUKUR atas seluruh 787 nama [v40, `bulan_absen` V1]

Sumber: `bulan_absen.py` V1 (blob **`10279d72`**, UTUH), laporan
`bulan_absen_ringkas.json` blob **`e450d9f9`** pada ref runner **`8b0e0182`** (run
**30477142893**), UTUH. Laporan penuh `bulan_absen.json` **249.992 B**
(`sidik_sumber` `d2fc3bfb…`) BELUM terbaca utuh → dianggap TIDAK ADA (aturan 52).
`sidik_kode` **`0294eb3a…`**, `versi_bulan_absen` 1, `bukan_bukti` false.
`bulan_absen_status.json` (blob `d6ec6ca0`): `kode_keluar` **0**, commit `4fc818f0`,
17:50:29Z. **`bulan_absen.log` berblob IDENTIK dengan ringkasnya** (`e450d9f9`)
karena workflow men-`tee` stdout — SATU pengukuran (calon aturan 77).

**Definisi, tersurat (aturan 76, KC-36, KC-39):** bulan ABSEN adalah bulan kalender
di antara `bulan_pertama` dan `bulan_terakhir` sebuah simbol yang TIDAK ADA di
penyebut 19.586. Ia **bukan** lubang funding dan **bukan** lubang tengah — keduanya
ADA di penyebut. Bulan gagal gerbang di TEPI riwayat **bukan** bulan absen.

Penggugur aman: `sidik_seragam` true (`24b6bb26…`) · 8/8 · `cacah_kunci_ganda` 0 ·
`kendali_sah` true · `selisih_penyebut` **0** · `cacah_pasangan` 15 ·
`selisih_nama_penyebut` **0** · `sumber_pembeda_ada` true · kode keluar **0**.
Kendali positif: **BTCUSDT 78 bulan / 0 absen**, **ETHUSDT 78 / 0**.

| medan | nilai |
|---|---:|
| `jumlah_bulan_absen` (787 nama) | **11** |
| `cacah_nama_berabsen` | **10** |
| `jumlah_bulan_absen_pasangan` (15 SETTLED) | **11** |
| `jumlah_bulan_absen_luar_pasangan` | **0** |
| `cacah_nama_tak_konsisten_rentang` | **0** |
| `sebaran_pembeda.gagal_gerbang` | **11** |
| `sebaran_pembeda.tak_diterbitkan_arsip` | **0** |
| `sebaran_pembeda.tak_terukur` | **0** |

Tidak satu pun bulan absen lahir karena arsip tidak menerbitkannya; kesebelasnya
diterbitkan lalu **gagal gerbang 1m**, pada klausa `jarak_60_detik` dan
`tanpa_menit_hilang`.

| simbol | pertama | terakhir | rentang | lolos | absen | bulan absen | bulan SETTLED | cocok |
|---|---|---|---:|---:|---:|---|---|---|
| AERGOUSDT | 2024-09 | 2026-06 | 22 | 21 | 1 | 2025-04 | 2025-04 | **ya** |
| AIAUSDT | 2025-09 | 2026-06 | 10 | 9 | 1 | 2026-01 | 2026-01 | **ya** |
| BDXNUSDT | — | 2026-03 | 10 | 10 | 0 | — | 2026-04 | tidak |
| BNXUSDT | 2022-05 | 2026-06 | 50 | 48 | 2 | 2022-06, 2022-08 | 2023-02 | tidak |
| CTKUSDT | 2020-11 | 2026-06 | 68 | 67 | 1 | 2025-04 | 2025-04 | **ya** |
| CVCUSDT | 2020-11 | 2026-06 | 68 | 67 | 1 | 2025-05 | 2025-05 | **ya** |
| CVXUSDT | 2022-09 | 2026-06 | 46 | 45 | 1 | 2025-07 | 2025-07 | **ya** |
| ICPUSDT | 2021-05 | 2026-06 | 62 | 62 | 0 | — | 2022-09 | tidak |
| LITUSDT | 2021-02 | 2026-06 | 65 | 64 | 1 | **2025-12** | 2025-12 | **ya** |
| MAVIAUSDT | 2024-02 | 2026-06 | 29 | 28 | 1 | 2025-03 | 2025-03 | **ya** |
| MINAUSDT | 2023-02 | 2026-06 | 41 | 41 | 0 | — | 2023-02 | tidak |
| PUMPUSDT | 2025-04 | 2026-06 | 15 | 14 | 1 | 2025-07 | 2025-07 | **ya** |
| SLPUSDT | 2023-10 | 2026-06 | 33 | 32 | 1 | 2025-07 | 2025-07 | **ya** |
| SXPUSDT | 2020-07 | 2026-05 | 71 | 71 | 0 | — | 2026-06 | tidak |
| TLMUSDT | 2021-07 | 2026-06 | 60 | 60 | 0 | — | 2023-03 | tidak |

**9 dari 9** nama berabsen-satu cocok PERSIS dengan bulan SETTLED terakhirnya.
9×1 + 2 (BNX) = **11** ✅

**Mekanisme KEDUA bagi H-A015, dan batasnya.** Jurnal 112 menemukan kecocokan bulan
SETTLED dengan **bulan berfunding pertama**; ini kecocokan dengan **kegagalan
gerbang klines** — sumber, gerbang, dan penyebut berbeda, jadi dua gejala saling
bebas. Yang TETAP dilarang (KC-18): ini soal PENAMAAN dan PENERBITAN, bukan bukti
bahwa kontrak lama diperdagangkan sampai bulan itu. **ADR-A002 §10 tidak boleh
diubah atas dasar ini.** Penyeimbang (aturan 74): BDXN, ICP, MINA, SXP, TLM
berabsen **0**, dan kedua bulan absen BNX bukan bulan SETTLED-nya.

## H-A015 — MENANG sebagai angka, DIBATASI sebagai tafsir

Sumber: `silang_settled.py` V1 (blob `3eea2a80`, UTUH), laporan blob **`755bbaef`**
pada ref runner **`12a65cbb`** (run **30469781160**), UTUH. `sidik_kode`
`0d814bc6…`, `sidik_kode_silang_funding` `8a9b859c…` (sama dengan laporan
`lubang_tengah` V2 → definisi bentuk tetap SATU, aturan 36), `sidik_data_funding`
`2c9fbd1b…`, `versi_funding` 6. Penggugur aman: `sidik_seragam` true · 8/8 ·
`cacah_kunci_ganda` 0 · `kendali_sah` true · `selisih_penyebut` **0** ·
**`selisih_kendali_funding_pertama` 0** · `cacah_pasangan` 15 · kode keluar 0.

**Kesetaraan definisi TERUJI (KC-9):** 5 dari 5 — BNXUSDT 2023-02, ICPUSDT 2022-09,
JUPUSDT 2024-02, QTUMUSDT 2020-03, TLMUSDT 2023-03. `sebaran_arah` = {`sama` **4**,
`lebih_awal` **11**, `lebih_lambat` **0**, `tak_terukur` **0**}; 4 + 11 = **15** ✅

- **Didukung:** pada ketiga pasangan berkohort banyak, bulan SETTLED terakhir =
  bulan berfunding pertama nama dasar, sesudah **19/16/20** bulan klines tanpa
  funding — fundingnya **milik kontrak lain**. Kohort 3 dari 3 berlubang > 10;
  keduabelas pasangan bersatu-bulan berlubang < 10.
- **DIBANTAH:** bentuk KUAT. Pada **11 dari 15** pasangan bulan SETTLED jatuh jauh
  SESUDAH funding pertama. Bulan SETTLED punya **DUA peran**.
- **Cela KC-38:** kecocokan keempat `MINAUSDT` bermekanisme lain —
  `bulan_klines_pertama` = `bulan_berfunding_pertama` = `bulan_settled_terakhir` =
  2023-02 dengan `cacah_lubang` **0**.
- `cacah_lubang` bukan nol di luar kohort banyak hanya **LITUSDT 5** dan **SXPUSDT
  5**; sepuluh sisanya **0**.

## Lubang funding — 880 lawan 877, dan keenam lubang TENGAH

Sumber: docstring `lubang_tengah.py` V2 (blob `4d3beaf1`, UTUH di jurnal 111) dan
laporan blob `39cd1caa` pada ref runner **`e2a37ff7`** (run **30440471508**), UTUH:
`sidik_kode` `c9372bd7…`, `sidik_seragam` true, 8/8, `kendali_sah` true,
`selisih_lubang_tengah` **0**.

- **880** = SELURUH lubang funding; **877** = yang jatuh di dalam **19.586**, bentuk
  lokal {awal **45**, ekor **826**, tengah **6**, seluruh **0**}; 45+826+6+0 =
  **877** ✅ Selisih **3** = tiga bulan BNXUSDT di luar penyebut, kini bernama:
  **2022-04, 2022-06, 2022-08** — persis ketiga baris karantina BNX. Docstring
  `silang_funding.py` menyimpan `BENTUK_TERBITAN_FUNDING` = {awal **48**, ekor 826,
  tengah 6} atas 880; 48+826+6 = **880** ✅ — dua penyebut, dua bentuk, keduanya
  benar (aturan 72, 76). **Irisan 880 lawan 877 tetap UTANG.**
- **Keenam lubang TENGAH dimiliki hanya DUA simbol** (`SIMBOL_TENGAH_TERCATAT =
  ["BTCSTUSDT", "LITUSDT"]`): **LITUSDT 2025-07..2025-11 (5)** dan **BTCSTUSDT
  2022-01 (1)**; 5 + 1 = 6 ✅ Keenamnya MATI. **Inilah asal-usul "dua cabang"
  Keputusan 7 ADR-A008.**
- **Pemilik ke-33 lubang pada simbol-bulan HIDUP:** BNXUSDT, ICPUSDT, **JUPUSDT**,
  **QTUMUSDT**, TLMUSDT; ke-33 lubang HIDUP itu SEMUANYA berbentuk awal.
- Bentuk ekor terjelaskan oleh kematian pasar: lubang → mati **96,0%** (842/877);
  mati → lubang **60,1%** (842/1.401). Lubang funding TIDAK sah sebagai penyaring
  kematian.
- `funding.py` V6 mencacah **87** "funding tanpa klines" atas 787 simbol;
  `funding_tanpa_klines` KOSONG pada kelima simbol H-A010 (**R-229 TEPAT**).

### LITUSDT — urutan peristiwa

1. MATI **2025-02..2025-11** (10 bulan); kematian MENDAHULUI hilangnya funding.
2. Lubang funding bentuk TENGAH **2025-07..2025-11** (rentetan **5**); berfunding
   terakhir **2025-06**, kembali **2026-01**.
3. **Bulan 2025-12 ABSEN**, `pembeda_absen` **gagal_gerbang**; terukur **43.590 dari
   44.640** menit — kurang **1.050** (nisbah 0,976478). Hampir penuh, bukan kosong.
4. `LITUSDTSETTLED` bermuatan **2025-12**, bulan yang sama.
5. **HIDUP 2026-01..2026-06 dengan funding kembali** (`h_a011_menang` true,
   `h_a011_cacah_hidup` **6**). **H-A011 MENANG.**

Jadi bulan SETTLED LITUSDT bukan bulan MATI di sela hidup nama dasarnya — ia bulan
yang nama dasarnya **tidak punya sama sekali** di penyebut. Itu mengubah bentuk
H-A014.

### BTCSTUSDT 2022-01 — lubang tengah yang benar-benar tak terjelaskan

`cacah_lilin` **44.640** (31 × 1.440, penuh), `byte_parquet` **399.757**, klines
terbit 2021-03..2026-06 (**64 bulan**, hanya **1** lubang funding), status **MATI**,
53 dari 53 bulan MATI. BTCSTUSDT TIDAK punya bulan absen **dan tidak ada di daftar
karantina**, jadi bulan itu LOLOS gerbang dan tetap mati. **Keputusan 7 ADR-A008
DILARANG diambil sebelum bulan itu dianatomi seperti BNXUSDT 2022-04.**

## Terhenti lawan hidup per jenis — TERUKUR

Sumber V4: `terhenti.py` V4 blob **`aaceb023`** commit **`6cc335e3`**, laporan blob
**`b5a1102c`** ref runner **`4dbf06a7`**, `sidik_kode` **`b8d0571d…`**, `sidik_data`
`6128fbb0…`. Sumber V3: laporan blob `e4f71ba8` ref runner `9aad0576`, `sumber`
`reports/semesta_rentang.json` 110.662 B, `sumber_bersidik` **false** (utang 22).

Dua definisi "terhenti" berdampingan (aturan 36): **survei** `selisih_bulan >= 2` →
**128**; **taksonomi** `bulan_terakhir < 2026-06` → **129**. `cacah_hanya_taksonomi`
**1** = `SXPUSDT` (2026-05); `cacah_hanya_survei` **0**. Ekor: 2026-03 **1**,
2026-04 **3**, 2026-05 **1**, 2026-06 **808**.

| jenis | terhenti | dari | hidup |
|---|---:|---:|---:|
| `futures_kedaluwarsa` | **44** | 50 | 6 |
| `perpetual_busd` | **41** | 41 | **0** |
| `perpetual_usdt` | **28** | 787 | **759** |
| `sisa_settled` | **14** | 15 | **1** |
| `indeks` | 1 | 3 | 2 |
| `perpetual_usdc` | 1 | 39 | **38** |
| `perpetual_usd1` | 0 | 1 | 1 |
| `basis_non_fiat` | 0 | 1 | 1 |
| `tak_tergolong` | 0 | 0 | 0 |

Terhenti 44+41+28+14+1+1 = **129** ✅ Hidup 759+38+6+2+1+1+1 = **808** ✅ 129 + 808 =
**937** ✅ `cacah_hidup_luar_penyebut` = 808 − 759 = **49** ✅

**28 nama `perpetual_usdt` yang berhenti terbit (SELURUHNYA, aturan 65):**
1000BTTCUSDT, AKROUSDT, ANCUSDT, ANTUSDT, AUDIOUSDT, **BDXNUSDT**, BTSUSDT,
BTTUSDT, BZRXUSDT, COCOSUSDT, DODOUSDT, DOTECOUSDT, EOSUSDT, FOOTBALLUSDT,
FRONTUSDT, GALUSDT, HNTUSDT, KEEPUSDT, LENDUSDT, LUNAUSDT, **MATICUSDT**, MBLUSDT,
NUUSDT, RNDRUSDT, SRMUSDT, **SXPUSDT**, TOMOUSDT, YFIIUSDT.

Yang TIDAK ada di dalamnya, dan karena itu masih terbit: **ICPUSDT, TLMUSDT,
BNXUSDT, CTKUSDT, CVCUSDT, CVXUSDT, LITUSDT, MAVIAUSDT, SLPUSDT**, ditambah
**AERGOUSDT, AIAUSDT, MINAUSDT, PUMPUSDT**.

**49 nama HIDUP di luar penyebut (SELURUHNYA, aturan 65):** 1000BONKUSDC,
1000PEPEUSDC, 1000SHIBUSDC, AAVEUSDC, ADAUSDC, ARBUSDC, AVAXUSDC, BCHUSDC,
BIOUSDC, BNBUSDC, BOMEUSDC, BTCDOMUSDT, BTCUSD1, BTCUSDC, BTCUSDT_260626,
BTCUSDT_260925, BTCUSDT_261225, CRVUSDC, DEFIUSDT, DOGEUSDC, ENAUSDC, **ETHBTC**,
ETHFIUSDC, ETHUSDC, ETHUSDT_260626, ETHUSDT_260925, ETHUSDT_261225, FILUSDC,
HBARUSDC, IPUSDC, KAITOUSDC, LINKUSDC, LTCUSDC, NEARUSDC, NEOUSDC, ORDIUSDC,
PENGUUSDC, PNUTUSDC, SOLUSDC, SUIUSDC, **SXPUSDTSETTLED**, TIAUSDC, TRUMPUSDC,
UNIUSDC, WIFUSDC, WLDUSDC, WLFIUSDC, XRPUSDC, ZECUSDC.

`MATICUSDC` satu-satunya USDC terhenti, dan `MATICUSDT` ada di antara 28.
Penjelasan penggantian lambang MATIC → POL tetap **ASUMSI**; keberadaan `POLUSDT`
di dalam 787 belum diperiksa.

## Kelima belas pasangan SETTLED — TERUKUR [R-278 TEPAT]

`cacah_settled` **15** · `cacah_dasar_hidup` **13** · `cacah_dasar_terhenti` **2** ·
`cacah_dasar_tak_ada` **0** · `cacah_settled_mendahului` **14** ·
`identitas_pasangan_utuh` true · `kendali_pasangan_sah` true.

| SETTLED | bulan SETTLED | bulan | nama dasar | bulan dasar | dasar hidup |
|---|---|---:|---|---|---|
| AERGOUSDTSETTLED | 2025-04 | 1 | AERGOUSDT | 2026-06 | ya |
| AIAUSDTSETTLED | 2026-01 | 1 | AIAUSDT | 2026-06 | ya |
| BDXNUSDTSETTLED | 2026-04 | 1 | BDXNUSDT | **2026-03** | **tidak** |
| BNXUSDTSETTLED | 2023-02 | **6** | BNXUSDT | 2026-06 | ya |
| CTKUSDTSETTLED | 2025-04 | 1 | CTKUSDT | 2026-06 | ya |
| CVCUSDTSETTLED | 2025-05 | 1 | CVCUSDT | 2026-06 | ya |
| CVXUSDTSETTLED | 2025-07 | 1 | CVXUSDT | 2026-06 | ya |
| ICPUSDT_SETTLED | 2022-09 | **9** | ICPUSDT | 2026-06 | ya |
| LITUSDTSETTLED | 2025-12 | 1 | LITUSDT | 2026-06 | ya |
| MAVIAUSDTSETTLED | 2025-03 | 1 | MAVIAUSDT | 2026-06 | ya |
| MINAUSDTSETTLED | 2023-02 | 1 | MINAUSDT | 2026-06 | ya |
| PUMPUSDTSETTLED | 2025-07 | 1 | PUMPUSDT | 2026-06 | ya |
| SLPUSDTSETTLED | 2025-07 | 1 | SLPUSDT | 2026-06 | ya |
| SXPUSDTSETTLED | **2026-06** | 1 | SXPUSDT | **2026-05** | **tidak** |
| TLMUSDTSETTLED | 2023-03 | **9** | TLMUSDT | 2026-06 | ya |

Jumlah kolom bulan = 1+1+1+6+1+1+1+9+1+1+1+1+1+1+9 = **36** ✅ sama persis dengan
total bulan SETTLED yang diukur `bulan_settled.py` V1 (aturan 69).

**Dari `reports/bulan_settled.json` (blob `31d3971e`, ref runner `0aac1dba`, UTUH):**

1. **"DUA BERSAMBUNG" DICABUT.** `TLMUSDTSETTLED` sembilan bulannya: 2022-01,
   2022-02, **2022-04**..2022-08, 2023-02, 2023-03. Yang benar: **satu bersambung
   (`ICPUSDT_SETTLED` 2022-01..2022-09) dan dua bercelah (TLM, BNX)**.
2. `BNXUSDTSETTLED` = 2022-04..2022-08 (lima bersambung) + 2023-02.
3. **`bulan_didaftar` BNXUSDT = 2022-04..2026-06 PENUH, 51 bulan tanpa lubang.**
   Maka "3 lubang" adalah lubang **gerbang kehidupan**, bukan berkas tak
   diterbitkan. Aturan 76 lahir dari sini: 51 − 48 = **3**, sedangkan rentang 50 −
   48 = **2**.
4. **Ketiga bulan lubang BNXUSDT ada di dalam `BNXUSDTSETTLED`** — calon penjelasan
   KC-15, diturunkan menjadi **ASUMSI LEMAH** oleh jurnal 110.
5. **Penamaan SETTLED BEROMBAK:** 2023-02 memuat TIGA nama (BNX, MINA, TLM) dan
   2025-07 memuat TIGA (CVX, SLP, PUMP).
6. **DUA BELAS nama bersatu-bulan** (bukan 11 — kekalahan R-281): AERGO, AIA, BDXN,
   CTK, CVC, CVX, LIT, MAVIA, MINA, PUMP, SLP, SXP. Tiga lebih panjang: ICP 9, TLM
   9, BNX 6. 12 + 3 = 15 ✅ 12×1 + 24 = **36** ✅
7. `definisi_dapat_dibedakan` **false** pada H-A013. Kendali BTCUSDT 78 bulan ≥ 60.
8. **`BDXNUSDT` penghuni ekor 2026-03**, satu-satunya. 2026-05 = SXPUSDT; tiga nama
   2026-04 belum bernama, satu di antaranya `BDXNUSDTSETTLED`.

## H-A013 — MENANG 6–0, TAFSIRNYA DICABUT

Enam bulan peralihan cocok dengan bulan saudara SETTLED-nya (CTK 2025-04, CVC
2025-05, CVX 2025-07, LIT 2025-12, MAVIA 2025-03, SLP 2025-07), `cacah_cocok_bulan`
6, `ambang_menang` 4, `cacah_peralihan_terhenti` **0**, keenam nama dasar masih
terbit 2026-06. Rantai pelemahan tafsir: "delapan kebangkitan" → "dua bersambung +
enam peralihan nama" → **PENAMBAHAN nama kontrak selesai** (aturan 68, KC-31).
Keenam bulan itu juga bulan ABSEN, dan keenamnya ada di daftar karantina dengan
`nisbah_lilin` 0,976 sampai 0,986 — kelas gejalanya sama.

DUA konvensi nama berdampingan: `ICPUSDT_SETTLED` bergaris bawah, empat belas
lainnya TANPA. Docstring `penyebut_tahun.py` menulis `TLMUSDT_SETTLED` (salah):
dicatat, TIDAK disunting, tidak diwarisi (R-246 SEPARUH).

Cacah bulan ARSIP 24 nama, 24 dari 24 cocok, `jumlah_bulan_didaftar` **518**:
BNXUSDT 51 (48 di PENYEBUT) · CTKUSDT 68 · CVCUSDT 68 · CVXUSDT 46 · ICPUSDT 62 ·
LITUSDT 65 · MAVIAUSDT 29 · SLPUSDT 33 · TLMUSDT 60 · ICPUSDT_SETTLED 9 ·
TLMUSDTSETTLED 9 · BNXUSDTSETTLED 6 · dua belas nama SETTLED lain bercacah 1.

## Penyebut simbol-bulan PER TAHUN — TERUKUR

Semesta `perpetual_usdt` saja (aturan 63). Sumber `penyebut_tahun` V1.

| tahun | penyebut | MATI | `bagian_mati` |
|---|---:|---:|---:|
| 2020 | 504 | 1 | 0,001984 |
| 2021 | 1.385 | 9 | 0,006498 |
| 2022 | 1.729 | 34 | 0,019665 |
| 2023 | 2.400 | 103 | 0,042917 |
| 2024 | 3.570 | 192 | 0,053782 |
| 2025 | 5.948 | 506 | 0,085071 |
| 2026 (6 bln) | 4.050 | 556 | **0,137284** |

1+9+34+103+192+506+556 = **1.401** ✅ ·
504+1.385+1.729+2.400+3.570+5.948+4.050 = **19.586** ✅ `bagian_mati` menanjak
monoton 0,20% → **13,73%**. DILARANG disebut laju kematian "pasar kripto".
`cacah_simbol_tanpa_hidup` **18** — identitasnya belum dibaca.

**KC-18 (semesta kehidupan).** Atas **19.586** simbol-bulan lolos: **1.401 MATI**
(7,153%), **98 SEPI** (0,500%), **18.087 HIDUP** (92,35%); 945 MATI di luar kohort
puncak. Dari 1.401 MATI, **842** kehilangan funding dan **559** tetap berfunding.

## Cacah baris terukur — `ukur_baris` V5

Sumber blob `c8b988ff` (UTUH), commit `404e6f1b`, run 30451749412, kode 0;
`cacah_berkas_hilang` 0, `cacah_berkas_melebihi_pagar` 0, 21 dari 21 berkas.
Definisi `len(teks.splitlines())`, pagar 800 di `tests/test_kontinuitas.py`.

`funding.py` **705**/28.121 B · `silang_funding.py` **705**/29.873 B ·
`lubang_tengah.py` V2 560 · `kohort_ekor.py` 553 · `kebangkitan.py` 552 ·
`penyebut_tahun.py` 527 · `tests/test_kebangkitan.py` 501 · `kehidupan_arsip.py`
496 · `semesta_silang.py` 423 · `kehidupan.py` 417 · `bulan_settled.py` 386 ·
`pulihkan.py` 383 · `tests/test_penyebut_tahun.py` 369 · `ukur_baris.py` 352 ·
`tests/test_semesta_silang.py` 253 · `tests/test_bulan_settled.py` 240 ·
`gerbang_1m.py` 184 · `funding_cdn.py` 162 · `arsip.py` 154 · `resample.py` 127 ·
`kohort_ringkas.py` 82. Total **8.131** ✅ Terbesar **705, SERI** (KC-26).

**Angka MATI:** `ukur_baris.py` 183/226/280 BATAL → 352; `silang_funding.py` 396
BATAL → 705; `pulihkan.py` 318 BATAL → 383; `lubang_tengah.py` 390 hanya V1 → 560.

**BELUM DIUKUR:** `tests/test_lubang_tengah.py`, `taksonomi.py`, `pecahan.py`,
`semesta_kuota.py` V3 (24.987 B), `tests/test_semesta_kuota.py`, `terhenti.py`
**V4**, `tests/test_terhenti.py` **V4**, `survei.py`, `ringkas_semesta.py`,
`diagnosa_kc15.py` (16.268 B), `silang_settled.py`, `tests/test_silang_settled.py`,
`bulan_absen.py`, `tests/test_bulan_absen.py`, **`karantina_semesta.py`**,
**`tests/test_karantina_semesta.py`** — enam belas berkas. Tidak diramalkan dengan
pita sempit (aturan 58 pilihan c).

## Modul, workflow, dan berkas akar

**`lux_ai/semesta/`:** `__init__.py` 273 B (`4c2d1f25`) · `taksonomi.py` 7.086 B
(`b418c7ba`) · `terhenti.py` V1 `3fa8f697`, V2 `8121739b`, V3 `7b819787`, **V4
`aaceb023` pada commit `6cc335e3`**.

**`lux_ai/serapan/` — 39 berkas:** `__init__.py` (`64d85584`) · `arsip.py`
(`0104958b`) · `bentuk_semesta.py` (`1f0feb30`) · `bulan_absen.py` (`10279d72`) ·
`bulan_settled.py` (`80e8d8bb`) · `diagnosa_kc14.py` (`5bd67d15`) · `kc14b`
(`bceada11`) · `kc14c` (`ab517db9`) · `diagnosa_kc15.py` (`3642e5b6`) ·
`diagnosa_kc6.py` (`0f699854`) · `funding.py` (`8d4b1f82`) · `funding_cdn.py`
(`fd624d00`) · **`gerbang_1m.py` (`c8cc54c8`, UTUH)** · **`karantina_semesta.py`
(`46e7c46b`)** · `kebangkitan.py` (`446321ee`) · `kehidupan.py` (`f49abb2b`) ·
`kehidupan_arsip.py` (`318a5cb1`) · `klines.py` (`cc4d9287`) · `kohort_ekor.py`
(`c9b63bbe`) · `kohort_ringkas.py` (`4ae62d5b`) · `lubang_tengah.py` (`4d3beaf1`) ·
`pecahan.py` (`f1b49f1b`) · `penyebut_kc6.py` (`7f399244`) · `penyebut_tahun.py`
(`265aad00`) · `probe.py` (`4581639f`) · `pulihkan.py` (`a9e6eab7`) ·
`rentang_kc6.py` (`631ec2f3`) · `resample.py` (`66a4b177`) · `rilis.py`
(`2e44530c`) · `ringkas_semesta.py` (`bc8f7ad7`) · `semesta_kuota.py`
(`7288b030`) · `semesta_silang.py` (`ad72f3f2`) · `serap.py` (`62d4c2c3`) ·
`silang_funding.py` (`42c3aa9d`) · `silang_settled.py` (`3eea2a80`) · `survei.py`
(`26b14940`) · `uji_resample.py` (`f10ec98a`) · `ukur_baris.py` (`3ebaa9f9`).

**33 berkas di `.github/workflows/`:** bentuk_semesta `dc393dd0` · bulan_settled
`9e0829f2` · **bulan_absen `71f76a0f`** (UTUH; `paths` hanya modulnya; meng-commit
empat berkas laporan; **mendeklarasikan `workflow_dispatch`**) · **ci `c79497b2`**
(UTUH; **`paths-ignore`** journal/decisions/hipotesis/reports → setiap push di luar
keempatnya menyalakan CI, KC-41; `workflow_dispatch`; `concurrency` per ref tanpa
pembatalan; meng-commit `ci_terakhir.json` DAN `ci_terakhir.txt` ber-`[skip ci]`;
`exit ${kode}` paling akhir) · diagnosa_kc14 `6524646a` · kc14b `a315c25b` · kc14c
`82126b60` · kc15 `c5f2ee0f` · kc6 `6bae2b1b` · funding_semesta `c1ce55f3` ·
**karantina_semesta (blob belum dicatat — didorong pada `edea61f7`, belum dibaca
ulang)** · kebangkitan `282b51aa` · kehidupan `3eb10655` · kehidupan_arsip
`8234e5dc` · kohort_ekor `2e747475` · lubang_tengah `557030de` · pecahan_serapan
`cd9e21d1` · penyebut_kc6 `14617b6b` · penyebut_tahun `8f0d5852` · probe_serapan
`9b356e15` · pulihkan_rilis `32bd1099` · rentang_kc6 `db1e77ae` · ringkas_semesta
`d6145d28` · semesta_kuota `b7e5a65a` · semesta_silang `babf08e4` · serap_pilot
`85694e0f` · silang_funding `23f8c870` · silang_settled `78d8051c` · survei_semesta
`a1fb0192` · taksonomi_semesta `b066b4db` · terhenti_semesta `baef4f41` ·
uji_resample `121f3e25` · ukur_baris `f62be605`.

**`tests/` — 42 berkas**; sebelum push `karantina_semesta` terukur **41** (aturan
66). Blob yang tercatat: `test_karantina_semesta.py` (`d535f6d9`) ·
`test_bulan_absen.py` (`d4f2ee5a`) · `test_pulihkan.py` (`11c43533`) ·
`test_rilis.py` (`be0aa219`) · `test_rilis_karantina.py` (`739c8da9`) ·
`test_karantina_a006.py` (`a5a3d82f`) · `test_silang_funding.py` (`92258b1d`) ·
`test_silang_settled.py` (`dae60732`) · `test_lubang_tengah.py` (`b5417b27`) ·
`test_terhenti.py` (`1c4afa6f`) · `test_semesta_kuota.py` (`170320ab`) ·
`test_kebangkitan.py` (`1fd006c5`) · `test_kohort_ekor.py` (`ec9b5774`) ·
`test_penyebut_tahun.py` (`99e42567`) · `test_kehidupan_arsip.py` (`470a2cd8`) ·
`test_gerbang_1m.py` (`a930af17`) · `test_serap.py` (`adde4013`) ·
`test_serapan.py` (`050a7e0a`) · `test_pecahan.py` (`b4e634c9`) ·
`test_taksonomi.py` (`2f73ec83`) · `test_arsip_kc9.py` (`3d8af70c`) ·
`test_kontinuitas.py` (`b377271f`) · `test_resample.py` (`f7c003d7`) ·
`test_ukur_baris.py` (`7975bf88`).

**Berkas akar repo:** `STATE.md`, `PROMPT_KELANJUTAN.md` (v43 blob `e392c9a1`),
`STATE_LAMPIRAN_EKOR.md` (`7480cedd`), `STATE_LAMPIRAN_UKUR.md` (berkas ini),
`STATE_LAMPIRAN_ADR.md` (`a02ef271`), `STATE_LAMPIRAN.md` (`f2b90764`),
`STATE_LAMPIRAN_ANGKA.md` (`f3ebdb02`), `PETA_MODUL.md` (`9ee33a99`),
`PETA_MODUL_BERKAS.md` (`3abe95f6`), `README.md` (`d875f364`), `requirements.txt`
(`b3749ba5`). Direktori jurnal bernama **`journal/`** (Inggris), berkasnya
`journal/YYYY-MM-DD-NNN.md`.

## API modul yang sudah terbaca dan boleh dipakai

Rincian v37 berlaku untuk `semesta_silang`, `arsip` (tanpa `requests`;
`fapi.binance.com` 451), `pecahan` (VERSI 6), `taksonomi`, `semesta_kuota` V3,
`penyebut_tahun`, `kebangkitan`; v38 untuk `survei`, `terhenti` V3,
`ringkas_semesta`, `rentang_kc6`; v39 untuk `silang_settled` V1, `diagnosa_kc15`,
`terhenti` V4; v40 untuk `silang_funding` V2 (`42c3aa9d`), `kehidupan_arsip` V1
(`318a5cb1`), `bulan_absen` V1 (`10279d72`). Tambahan v41:

- **`pulihkan`** (`a9e6eab7`, UTUH): `VERSI` **2**, `TOTAL_PECAHAN` **8**,
  `AKAR_UNDUH` "data/unduh", `AKAR_PULIH` "data/pulih", `nama_manifes(i)` →
  `reports/manifes_pecahan_{i}.json`, `nama_status_serapan(i)`, `nama_keluaran(i)`,
  `nama_tag(i, run_id)`, `sidik_kode()`, `run_id_sumber(i, akar)`,
  `putuskan_definisi(selisih_utama, selisih_total, baris_karantina)`,
  `anggota_aman`, `cacah_baris_parquet`, `periksa_bagian`, `periksa_keluarga`,
  `jalankan(indeks, akar, dir_unduh, dir_pulih, hapus)`; tetapan
  `DEF_TAK_ADA_MANIFES`, `DEF_TAK_TERBEDAKAN`, `DEF_LOLOS_SAJA`,
  `DEF_LOLOS_PLUS_KARANTINA`, `DEF_TAK_COCOK`; env `PULIH_INDEKS`.
- **`rilis`** (`2e44530c`, UTUH): `BATAS_BAGIAN` 1_800_000_000, `BLOK_TAR` 512,
  `BLOK_PAX` 1024, `KEPALA_ANGGOTA` 1536, `BYTE_AKHIR_TAR` 1024, `REKAM_TAR` 10240,
  `MARGIN_REKAM` 20480, `NAMA_SUMS`, `NAMA_SUMS_KARANTINA`, `AKAR_RILIS`
  "data/rilis", `perkiraan_byte_anggota`, `bulatkan_rekam`, `taksir_bagian`,
  `rencana_belah`, `sha256_berkas`, `baris_sums`,
  `PengemasBerbelah(akar, nama_dasar, tujuan, batas, nama_sums)` dengan
  `tambah`/`tutup`/`laporan`, `verifikasi(akar, laporan)`. **Laporan pengemas hanya
  memuat bagian tar — ia tahu BERAPA berkas karantina, TIDAK tahu SIAPA.**
- **`serap`** (`62d4c2c3`, UTUH): `SUMBER_RENTANG`
  "reports/semesta_rentang.json", `MANIFES` "reports/manifes_pilot.json",
  `AKAR_PARQUET` "data/parquet", `AKAR_KARANTINA` "data/parquet_karantina",
  `JENIS_DIIZINKAN` "perpetual_usdt", `BATAS_HEADER` "2022-01", `BATAS_BARU`
  "2025-01", `BATAS_HIDUP` "2026-05", `KELAS_RISIKO` (pra_header, non_ascii,
  terhenti, bulan_awal_2020_2021, kendali_baru), `BATAS_DAFTAR_KARANTINA` **500**,
  `nama_aman`, `non_ascii`, `pilih_berlapis`, `baris_karantina(manifes)`,
  `ringkas_karantina(manifes)` → `daftar_karantina` berisi {`simbol`, `bulan`,
  `pelanggaran`, `baris`, `parquet_karantina`, `checksum_zip_sha256`} plus
  `cacah_karantina`, `cacah_tak_terunduh`, `cacah_dibuang`, `cacah_ditambal`,
  `byte_parquet_karantina`, `daftar_terpotong`, `batas_daftar`;
  `serap_satu(simbol, bulan, akar, terhenti)`, `ringkas(manifes)`.
- **`gerbang_1m`** (`c8cc54c8`, UTUH): `MS_BAWAH` 1e12, `MS_ATAS` 1e14, `KLAUSA` =
  (`deret_tidak_kosong`, `tanpa_duplikat`, `tanpa_menit_hilang`, `jarak_60_detik`,
  `selaras_menit`, `satuan_milidetik`), `sidik_kode` (mencakup `resample.py`),
  `persen`, `satuan_stempel_dari_besaran`, `ukur_deret`, `nilai_klausa`,
  `nilai_deret`, `ringkas_gerbang`. **`menit_hilang_dalam_rentang` = slot dalam
  rentang − cap unik, dihitung atas rentang yang ADA di berkas dan sengaja BUKAN
  atas bulan kalender; rumusnya SALINAN sengaja dari `diagnosa_kc6.celah_menit`
  (aturan 10), dan `tests/test_gerbang_1m.py` membandingkan keduanya.** Medan
  `pelanggaran` = klausa yang GAGAL (KC-40).
- **`karantina_semesta` V1** (`46e7c46b`, UTUH): `VERSI` 1, `KELUARAN`
  `reports/karantina_semesta.json`, `KELUARAN_RINGKAS` `…_ringkas.json`,
  `R291_HIMPUNAN` (12 pasang), `R291_CACAH` 12, `PENYEBUT_SEMESTA` 19598,
  `PENYEBUT_LOLOS` 19586, `BYTE_KARANTINA_TERCATAT` 13247705, `KENDALI_NAMA`
  (BTCUSDT, ETHUSDT), `MENIT_PER_HARI` 1440. Fungsi: `sidik_kode` (mencakup
  `pulihkan.py`), `bulan_menit`, `kunci`, `entri_karantina`, `_medan`, `perkaya`,
  `baca_manifes`, `jalankan(akar, total)`, `kode_keluar`, `main`. **Mengimpor
  `pulihkan` saja.** `kode_keluar` sengaja TIDAK memeriksa `uji_r291` (aturan 24, 72).

## Hipotesis

- H-A001 belum diuji · H-A002b GUGUR · H-A003 MENANG pada 3, GUGUR pada 9 · H-A004
  tak dapat diuji (451) · H-A005 GUGUR pada rentang tersampel · H-A006 MENANG enam
  run · H-A008 MENANG dua kali · H-A009 GUGUR · H-A010 **MENANG 5–0** · **H-A011
  MENANG** (LITUSDT HIDUP 6 dari 6 bulan 2026; batasan BTCSTUSDT 0 dari 53 tetap
  berlaku, aturan 60) · H-A012 MENANG · **H-A013 MENANG 6–0, TAFSIR DICABUT**.
- **H-A014 — BENTUK LAMA SALAH, BENTUK BARU MENANG 9 dari 9.** Bentuk lama ("bulan
  SETTLED adalah bulan MATI di TENGAH hidup nama dasarnya") **DICABUT**: bulan itu
  bahkan tidak ada di penyebut, jadi ia tak dapat berstatus MATI maupun HIDUP.
  **Bentuk baru TERUKUR:** bulan SETTLED terakhir adalah bulan yang **ABSEN** dari
  daftar bulan LOLOS nama dasarnya — terbukti pada **9 dari 9** nama berabsen-satu
  (AERGO, AIA, CTK, CVC, CVX, LIT, MAVIA, PUMP, SLP), `pembeda_absen`
  **gagal_gerbang** pada kesebelas bulan absen. **Batas (aturan 74):** BDXN, ICP,
  MINA, SXP, TLM berabsen 0 dan BNX berabsen 2 pada bulan yang bukan bulan
  SETTLED-nya. Penyebut wajib disebut **9 dari 15**. `definisi_dapat_dibedakan`
  wajib dipasang bila diuji lagi (aturan 46).
- **H-A015 MENANG sebagai angka, DIBATASI sebagai tafsir; disokong mekanisme
  KEDUA.** Benar pada **3 pasangan berkohort banyak** lewat funding dan **9 dari 9
  pasangan berabsen-satu** lewat gerbang klines; tetap **dibantah** dalam bentuk
  KUAT pada 11 pasangan bersatu-bulan. Warisi hanya dalam bentuk terbatas (aturan
  20); ingat KC-38 (`MINAUSDT`) dan KC-18 (penamaan, bukan perdagangan).
- **H-A016 [v41, PENGAMATAN, BELUM DIUJI] — celah menit di arsip 1m datang dalam
  blok kelipatan 15 menit.** Bahan: kedua belas `selisih_menit` bulan karantina
  habis dibagi 15 (12 dari 12, penyebut 12), dan KC-14 mencatat 6.375 = 425 × 15
  atas 9 simbol-bulan lain. **Belum diuji atas simbol-bulan yang LOLOS gerbang**,
  jadi DILARANG digeneralkan ke 19.586 (aturan 20). Uji yang sah menuntut ukuran
  celah pada bulan yang lolos — dan karena gerbang menolak bulan bercelah,
  penyebutnya harus dipilih hati-hati (kemungkinan besar hanya menit TEPI yang
  tersisa). Kendali positif wajib: BTCUSDT/ETHUSDT dengan selisih 0 tidak dapat
  membedakan apa pun (aturan 41, 46, 50).
