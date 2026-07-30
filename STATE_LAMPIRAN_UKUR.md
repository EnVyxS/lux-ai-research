# STATE lampiran UKUR — bagian 3 dari STATE (v12, milik STATE v52)

**Kedudukan berkas ini.** STATE dipecah tiga sejak v43 (KC-42). Pembagian berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, 83, 84, dan **85**; KC-1..KC-51.
2. **`STATE_LAMPIRAN_EKOR.md`** v12 (blob **`568dc877f69d6508b1db50a35877d34da76fc21e`**)
   — bagian 2: papan skor, ADR, catatan kejujuran.
3. **`STATE_LAMPIRAN_UKUR.md`** (berkas ini, v12) — bagian 3: pengukuran, modul,
   workflow, uji, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) dan **`PROMPT_KELANJUTAN.md`** (blob
   `35beed44`) — **arsip; BUKAN sumber** (ADR-A018 kep. 9).

Dasar v12: UKUR v11 (blob **`7f0221bfb548d04f464a5b8c67f0579214f97b54`**), dibaca UTUH
pada giliran yang sama sebelum berkas ini ditulis (aturan 52, pencegahan KC-43).
**Yang ditambahkan v12 hanyalah ketertiban dokumen, BUKAN pengukuran baru:** dua salah
ketik milik berkas ini sendiri dilunasi; kepala naik ke v12/STATE v52; ordinal aturan
38 maju ke **ke-42** dengan dua blob CI baru; satu laporan CI yang **hangus** dicatat
terbuka. **Tidak satu angka ukur pun berubah dari v11.**

## KESERASIAN VERSI — ketiga bagian kini serasi pada v52 / v12 / v12

- `STATE.md` **v52** — blob **`635c24952637449d294a0f8035c8ed7e2f4932e4`**, commit
  **`28afc9ae075befe1bc3c1ed474f42d7dae95626e`**.
- `STATE_LAMPIRAN_EKOR.md` **v12** — blob **`568dc877f69d6508b1db50a35877d34da76fc21e`**,
  commit **`e68deab7b9bc2a96b597ba58573aca358c707b21`**.
- `STATE_LAMPIRAN_UKUR.md` **v12** — berkas ini.

Ketimpangan nomor versi yang dicatat EKOR v12 ("UKUR masih v11") **LUNAS oleh berkas
ini**. Jejaknya sengaja tidak dihapus dari riwayat; jangan memperlakukannya sebagai
utang hidup. **Satu berkas per push tetap MENGIKAT** (KC-42, KC-43).

**Tentang push berkas ini:** berkas ini di akar repo sehingga menyalakan `ci.yml`.
Tidak satu pun `tests/**` berubah, jadi cacah uji tetap **1341** — ramalan
**deterministik** (aturan 57), **MUDAH**, TIDAK masuk papan skor, TIDAK menambah
beruntun. **Laporannya WAJIB dibaca sebelum push akar berikutnya**, sebab dua push akar
berturut tanpa pembacaan di antaranya sudah terbukti menghanguskan yang pertama (lihat
bagian ordinal aturan 38).

**Angka yang TIDAK berubah dari v44/v45/v6/v7** (tidak diulang): taksonomi 9 kelas,
karantina 12, bulan ABSEN 11, H-A013..H-A015, terhenti, SETTLED. Rinciannya di v44
(blob `d302caff`), v45 (`eb826817`), v6 (`27e59a79`), v7
(`4e7fb65be81bc5657da94060447075f0f1e2d73c`).

## KOREKSI KC-41 — BACA SEBELUM MENGUTIP BERKAS INI

Kedelapan koreksi di bawah **tetap dicantumkan** karena semuanya soal dokumen kami
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
`irisan_byte.yml` (`7d98a267`), `bulan_pertama.yml` (`2242e3e4`),
`keterisian_lilin.yml` (`d821c63a`), dan **`sisa_defisit.yml`
(`645112075e104a74d43f3e3d2185cfbd48b0b513`)** meniru berkas ASLI ini, bukan rumusan
v5.

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

**Koreksi 4 [v10] — Angka 839.842.134 BUKAN jumlah lilin.** Angka itu adalah **total
baris parquet semesta** dari run rilis 30404071324, dan dipakai berulang di jurnal
serta lampiran seolah setara dengan jumlah lilin 1 menit. `keterisian_lilin` V1
menghitung LANGSUNG dari medan `cacah_lilin` atas 19.586 baris dan memperoleh
**839.325.999**. **Selisih 516.135.** Seluruh aritmetika implikasi jurnal 131 §6
dibangun di atas penyamaan itu, sehingga cacat di bahan baku, meskipun R-310 tetap
sah karena pitanya dikunci lebih dulu (aturan 29). Dari sinilah **KC-50** naik menjadi
resmi di STATE v50. Dugaan penyebab — 19.598 − 19.586 = 12 simbol-bulan karantina,
516.135 / 12 = 43.011 ≈ sebulan penuh — **BELUM DIUJI dan DILARANG dikutip sebagai
penjelasan**. **[v11] Ia kini menjadi poros calon (b) untuk R-312, dengan syarat
porosnya berupa bentuk SEBARAN, bukan rata-rata (ADR-A018 kep. 12).**

**Koreksi 5 [v10, DILUNASI di badan EKOR v11] — salah ketik di EKOR v10.** Bagian
"Temuan sampingan" EKOR v10 (blob `42fce021`) menulis `terisi ≉49,7%`. Karakternya
salah: `≉` berarti "tidak kira-kira sama dengan", kebalikan dari yang dimaksud.
**Bacaan yang benar: ≈49,7%.** EKOR v11 sudah memperbaikinya di badan berkas dengan
jejak koreksi di kepalanya.

**Koreksi 6 [v11, KINI LUNAS DI SUMBERNYA] — salah ketik di kepala EKOR v11.**
Kepala `STATE_LAMPIRAN_EKOR.md` v11 (blob `3d72a9e7`) menulis **"ramalan
deretministik"**; bacaan yang benar **"ramalan deterministik"**. **EKOR v12
(`568dc877`) sudah memperbaikinya di sumbernya** dengan jejak koreksi. Butir ini kini
riwayat, bukan utang.

**Koreksi 7 [BARU v12, LUNAS DI BERKAS INI] — salah ketik di kepala berkas ini
sendiri.** UKUR v11 (blob `7f0221bf`) menulis kepala bagian **"KESERAIAN VERSI"**.
Bacaan yang benar: **"KESERASIAN VERSI"**. Diperbaiki di atas.

**Koreksi 8 [BARU v12, LUNAS DI BERKAS INI] — penanda tebal tak berpasangan.**
Di daftar cacah per berkas uji, UKUR v11 membuka `**` dua kali pada baris
`test_bentangan_kohort.py` tanpa menutupnya berpasangan, sehingga penandaan tebal
bocor ke butir sesudahnya saat dirender. Diperbaiki di bagian "Modul, workflow, dan
berkas uji". **Tidak ada angka yang berubah** — hanya penanda.

**Bacaan yang jujur atas Koreksi 6–8:** ini **lima berkas berturut** (EKOR v11,
UKUR v11 dua kali, STATE v52, dan cacat "Empat/Enam" yang masih terbuka) yang memuat
salah ketik milik kami sendiri, meskipun setiap berkas dibaca ulang UTUH sesudah push.
Dibaca sebagai **tanda ketelitian menurun pada giliran panjang** — peringatan
operasional, bukan kelas cacat ilmiah. **Utang yang masih hidup: STATE v53 wajib
mengubah "Empat salah ketik" menjadi "Enam".**

## Semesta riset = `perpetual_usdt` = penyebut 787 — tidak berubah

- `cacah_perpetual_usdt` **787** = `cacah_penyebut_simbol` **787**
- `cacah_perpetual_usdt_luar_penyebut` 0, `cacah_penyebut_bukan_perpetual_usdt` 0
- Batas wajib disebut: token saham/ETF/komoditas ikut di dalam 787.

## KC-18 — semesta kehidupan (dikonfirmasi ulang oleh R-307..R-311)

Atas **19.586** simbol-bulan lolos: **1.401 MATI** (7,153%), **98 SEPI**, **18.087
HIDUP**. Dari 1.401 MATI: 842 kehilangan funding, 559 tetap berfunding.
`cacah_simbol_tanpa_hidup` **18**.

`cacah_lain` = 0 pada kelima modul → seluruh 19.586 berstatus MATI/SEPI/HIDUP, tidak
ada TAK_TERUKUR. 18.087 + 98 = 18.185 TERUKUR, + 1.401 = 19.586 ✅

**Pembelahan atas penyebut yang sama [v9]:** **787** baris adalah bulan PERTAMA
simbolnya (tepat satu per simbol — identitas, bukan kebetulan), **18.799** baris
bukan-pertama. 787 + 18.799 = **19.586** ✅

**Pembelahan atas kelas MATI [v10]:** dari 1.401 baris MATI, **1.392** berlilin PENUH
dan **9** tidak penuh. 1.392 + 9 = **1.401** ✅

**Pembelahan [v11] — penyebut kerja R-311.** Dari 18.799 baris bukan-pertama,
yang BUKAN berstatus MATI berjumlah **17.398** (18.799 − 1.401 = 17.398 ✅ — seluruh
1.401 baris MATI ternyata bukan bulan pertama simbolnya). Dari 17.398 itu:
**17.284** berlilin PENUH dan **114** berdefisit. 17.284 + 114 = **17.398** ✅
Rincian kelas 114: **HIDUP 111**, **SEPI 3**, **MATI 0**.

## Lubang funding — agregat semesta (tetap)

- `cacah_simbol_ada_lubang` = **122** (dari 787) · awal **5** · bukan-awal **118**
- BNXUSDT punya lubang AWAL dan bukan-awal sekaligus.
- Lima bentuk AWAL: BNXUSDT, ICPUSDT, JUPUSDT, QTUMUSDT, TLMUSDT. ICP dan TLM lubang
  awalnya melewati kematian (sumber salah-baca R-304, KC-46).
- Lubang funding **880** semesta / **877** dalam penyebut / 3 tak dikenal. Irisan
  880 lawan 877 BELUM diukur.

## SISA DEFISIT [v11 — penutupan sisa 712.925 lilin]

Sumber: `sisa_defisit.py` V1 run modul **30542217951** (commit
**`b1c7941db3e08ae8a6f06864d7f47a571abf5669`**, kode 0). Laporan
`reports/sisa_defisit.json` (11.069 B), ringkas blob
**`91a05c0528050d0d37e4cf7711b6556f13fc8d16`**, status blob
**`1c9c2c5fc5f14a3f0e5cadcf564e699c92f8cf0e`**.

**Pertanyaan yang dijawab** — pertanyaan terbuka nomor satu sejak R-310: **baris mana
yang menanggung 712.925 lilin defisit bukan-pertama di luar kesembilan baris MATI tak
penuh.**

| besaran | nilai |
| --- | --- |
| `cacah_calon` (bukan-pertama, bukan-MATI) | **17.398** |
| `cacah_calon_penuh` | **17.284** |
| **`cacah_berdefisit`** | **114** |
| bagian berdefisit atas calon | **0,006553** (0,66%) |
| `defisit_calon` | **712.925** |
| rata-rata defisit per baris berdefisit | **6.254** |
| `defisit_teratas` (sepuluh baris) | **291.379** |
| **`bagian_teratas`** | **0,4087** (= 291.379 / 712.925) |
| `defisit_terbesar` (satu baris) | **42.510** |
| `selisih_sisa` | **0** |
| `cacah_berdefisit_hidup` | **111** |
| `cacah_berdefisit_sepi` | **3** |
| `cacah_berdefisit_mati` | **0** |

- **KEKOSONGAN ITU LANGKA TETAPI TERPUSAT.** Hanya **114 dari 17.398** baris
  (**0,66%**) yang kurang lilin, dan **dua per lima** dari seluruh kekurangan itu
  ditanggung **sepuluh** baris saja.
- **Baris terbesar: TLMUSDT `2023-03`, berstatus HIDUP, 2.130 dari 44.640 lilin —
  95,2% KOSONG.** Inilah baris yang sejak R-309 menjadi satu-satunya lawan H-A019
  dan yang R-310 gagal jelaskan. Sifatnya kini terukur: bukan bulan tepi, bukan bulan
  pertama, melainkan bulan penuh kalender yang datanya nyaris tidak ada
  (ADR-A018 kep. 6).
- **Sepuluh baris teratas tersebar di TUJUH bulan berbeda**, kelompok terbesar dalam
  satu bulan hanya **dua** baris: `2023-03` (TLMUSDT, puncak), `2022-09`, `2023-02`,
  `2022-04` ×2, `2024-09`, **`2022-05` ×2**, `2022-02` ×2. Berbeda tajam dari R-310
  yang tujuh dari sembilan barisnya berhimpit di `2024-05` dalam jendela sembilan
  lilin. **Aturan 81 diperiksa dan TIDAK terpicu** (ADR-A018 kep. 4), sehingga **114
  sah diperlakukan sebagai cacah baris**, bukan satu peristiwa yang menyamar.
- **Dua baris `2022-05` nyaris kembar:** **ANCUSDT defisit 26.959** lawan **LUNAUSDT
  defisit 26.950** — selisih **sembilan lilin**. Ini dan hanya ini dasar **H-A021**.
  Ia **kebetulan angka, bukan bukti**; **setiap kalimat sebab untuk gugus `2022-05`
  DILARANG** sampai diuji lewat lubang tengah.
- **PENUTUPAN 712.925 DILARANG DISEBUT PENGUKURAN BEBAS.** `defisit_calon` = 712.925
  dan `selisih_sisa` = 0 **terpaksa** muncul dari 808.162 − 95.237 begitu seluruh
  1.401 baris MATI ternyata bukan bulan pertama. Itu tautologi (KC-50, KC-37,
  ADR-A018 kep. 3).
- **Kenyataan bahwa 114 baris seluruhnya HIDUP atau SEPI dan NOL MATI DILARANG
  disebut temuan** — itu dipaksa oleh definisi penyebut kerja, yang memang membuang
  seluruh baris MATI.
- **Tidak satu kalimat pun boleh menyimpulkan apa pun tentang harga.** Keempat belas
  medan `medan_baris_terlihat` tidak memuat harga (ADR-A017 kep. 2 berlaku penuh).
- **Kendali:** `kendali_nol` membuktikan modul BISA mengembalikan nol pada semesta
  buatan tanpa defisit (aturan 50); `JAWABAN_KENDALI` **17 medan** dengan
  `bagian_teratas` **0,9677** = 600/620 dihitung TANGAN lebih dulu dan cocok;
  `bagian_teratas` dikembalikan **null** bila baris berdefisit kurang dari 10.

**Adjudikasi R-311: SEPARUH.**

| butir | pita | terukur | hasil |
| --- | --- | --- | --- |
| 1 (BERISIKO) cacah baris berdefisit | 200 .. 12.000 | **114** | **KALAH** |
| 2 (BERISIKO) `bagian_teratas` | 0,02 .. 0,45 | **0,4087** | MENANG (sisa 0,0413 ke tepi ATAS) |
| 3 (MUDAH) invarian, kendali, kode 0, CI | — | — | MENANG |

Butir 1 meleset **26,3 kali** dari taksiran titik 3.000 dan **1,75 kali** di bawah
tepi bawah. **Kedua butir meleset ke arah fisik yang SAMA** (kekosongan lebih
terpusat daripada dugaan); satu-satunya alasan butir 2 menang adalah pitanya kebetulan
cukup lebar. Itu dasar **KC-51**.

**Sidik kode `sisa_defisit` V1 =**
`6211624ba9514d604d4dc510abca2e40386775c7aaa1279135f0baf666f044b0`

## KETERISIAN LILIN [v10, tetap berlaku]

Sumber: `keterisian_lilin.py` V1 run **30535202643** (commit
**`924b0d7afcf1f9e17965dff931d36489ad27f01b`**, kode 0). Laporan
`reports/keterisian_lilin.json` blob **`14f1772070789dad603b132ece034ea4c19c6e3d`**,
ringkas blob **`f33714eda66e77d37a7024b52c433ead070b16c7`**.

| besaran | nilai |
| --- | --- |
| `cacah_mati_penuh` | **1.392** |
| `cacah_mati_tak_penuh` | **9** |
| `jumlah_lilin_langsung` (19.586 baris) | **839.325.999** |
| `defisit_total` | **18.143.601** |
| `defisit_pertama` | **17.335.439** (95,5%) |
| `defisit_bukan_pertama` | **808.162** |
| `bagian_defisit_bukan_pertama` | **0,0445** |
| `cacah_baris_tanpa_lilin` / `defisit_negatif` / `kunci_ganda` | **0** / **0** / **0** |
| `cacah_laporan_dibaca` | **8** dari 8 · `sidik_seragam` **true** |

- **BULAN MATI PENUH DATANYA; YANG NOL ADALAH TRANSAKSINYA.** 1.392 dari 1.401
  (**99,4%**) bulan MATI berisi lilin sebanyak-banyaknya bulan itu.
- **DILARANG melanjutkan ke "harga beku" atau "lilin datar".** `medan_baris_terlihat`
  berisi **14** medan — `ada_di_arsip`, `bagian_volume_nol`, `bulan`, `byte_parquet`,
  `cacah_baris_cacat`, `cacah_lilin`, `cacah_lilin_terbaca`, `cacah_volume_nol`,
  `galat`, `gerbang_lolos`, `jalur`, `simbol`, `status`, `transaksi_total` — dan
  **tak satu pun harga**.
- **Defisit menumpuk di bulan pertama:** 17.335.439 dari 18.143.601 (**95,5%**) ada di
  787 bulan pertama; rata-rata **22.027** lilin hilang per bulan pertama, yaitu
  keterisian **≈49,7%** — bersesuaian dengan nisbah byte 0,527179 dari R-309.
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
  808.162 − 95.237 = **712.925**, yang kini ditanggung 114 baris di atas.
- **DUA ANOMALI LAMA LUNAS.** Baris 1 dan 2 adalah tepat kedua `cacah_mati_byte_kecil`
  R-308 (LENDUSDT 2020-11 = 97.634 byte; FRONTUSDT 2024-09 = 109.120 byte). Meski
  begitu **larangan ADR-A015 kep. 5 TIDAK dibalik**: besar berkas tetap DILARANG
  dipakai sebagai penanda status ke arah mana pun. **[v11] R-311 tidak membaliknya.**
- **TUJUH dari sembilan berbulan `2024-05` dengan jendela hanya SEMBILAN lilin**
  (39.308..39.317) → KC-47, aturan 81, **H-A020**. **Kalimat "tujuh simbol didelisting
  28 Mei 2024" DILARANG ditulis sebagai temuan.**
- **Kendali data sah:** tiga kendali BTCUSDT — 2021-05, 2021-08, 2021-01 — semuanya
  `cacah_lilin` **44.640** dan berstatus HIDUP.
- **Adjudikasi R-310: TEPAT** (9 dalam 1..120; 0,0445 dalam 0,02..0,25; MUDAH menang)
  — **kedua kemenangan tipis ke tepi BAWAH**, dan itu kini terbaca sebagai gejala
  KC-51, bukan sebagai kalibrasi baik.

**Sidik `keterisian_lilin` V1 =**
`1cd98f4fa22c24b30f31f5b36dac0ea0bb3fa9de44e5e15ae73cbf11cdca08bb`
**Sidik laporan (`sidik_kode_laporan`) =**
`24b6bb265525e81c2e571b46e401f36903383f1e3738c487850861adc3e8c595`

## IRISAN BULAN PERTAMA [v9, tetap berlaku]

Sumber: `bulan_pertama.py` V1 run **30532058657** (commit `09ce9853`, kode 0).
Laporan blob **`0a2aa6ae15d949b44803dffdc9e97dbd322bbc85`**, status blob
**`0c8ea41a5a1aea4090d0dd2de65c9652088fc462`**.

Definisi "bulan pertama": bulan TERKECIL milik simbol itu **di dalam penyebut
19.586** — bukan bulan pertama simbol itu di bursa. Perbedaan keduanya BELUM diukur
(ADR-A016 kep. 6).

| besaran | nilai |
| --- | --- |
| `cacah_hidup_kecil_sebagian` (dari 38) | **37** |
| `bagian_hidup_kecil_sebagian` | **0,973684** |
| `cacah_pertama` | **787** · `cacah_bukan_pertama` **18.799** |
| `jumlah_byte_pertama` | **706.233.745** |
| `jumlah_byte_bukan_pertama` | **32.000.028.630** |
| `rata_byte_pertama` | **897.374,517** |
| `rata_byte_bukan_pertama` | **1.702.219,726** |
| `nisbah_rata` | **0,527179** |

- **Irisan NYATA tetapi ASIMETRIS TAJAM.** 37 dari 38 berkas kecil adalah bulan
  pertama (**97,4%**); hanya 37 dari 787 bulan pertama yang berkas kecil (**±4,7%**).
  Rumusan resmi satu-satunya di **ADR-A016 kep. 1**.
- **Bulan pertama SEPARUH, bukan sepersepuluh** (0,527179), dikuatkan keterisian
  lilin ≈49,7%.
- **Klausa tepi `2026-06` menyumbang NOL secara bebas** — DICABUT (ADR-A016 kep. 2),
  melahirkan aturan 84.
- **Satu lawan tersisa: TLMUSDT 2023-03 (80.394 byte).** **[v11] KINI TERJELASKAN
  SIFATNYA oleh R-311** — ia baris berdefisit terbesar di seluruh semesta, HIDUP,
  2.130/44.640 lilin, 95,2% kosong. Tafsir "byte kecil = bulan sebagian di tepi
  rentang" karena itu **MELEMAH**: ada jalan ketiga. **Tafsir penggantinya TIDAK
  ditegakkan** karena sebab kekosongannya belum diukur (ADR-A018 kep. 6).
- Kendali dua lapis sah: tiga parquet terbesar seluruhnya BTCUSDT (2021-05 2.770.666,
  2021-08 2.730.341, 2021-01 2.722.266, semuanya HIDUP); detektor semesta buatan
  dengan jawaban dihitung TANGAN — `DETEKSI_PERTAMA` 2, `DETEKSI_HIDUP_KECIL` 2,
  `DETEKSI_SEBAGIAN` 2, `DETEKSI_NISBAH` 0,75, `DETEKSI_TOTAL_BYTE` 1.500 — cocok.

**`daftar_kecil_bertanda` (38, LENGKAP, urut byte menaik):** JUPUSDT 2024-01 22.440 ·
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

**Sidik `bulan_pertama` V1 =**
`0d3530f69ad51a22e038c17616411b56e4518698ff14c9b635131ec1e2a66562`

## LEBAR ZONA IRISAN BYTE [v8, tetap berlaku]

Sumber: `irisan_byte.py` V1 run **30529294165** (commit `d22364b9`, kode 0). Laporan
blob **`4c13bf6afc36c9afbeb1c662d6098258a6b750dd`**, status blob
**`863dc4cb266b2fcee56fb733960722d37bd931e7`**.

| besaran | nilai |
| --- | --- |
| `cacah_hidup_byte_kecil` (< **97.634**, STRIKT) | **38** |
| `bagian_hidup_byte_kecil` | **0.0021009564880853653** |
| `cacah_mati_byte_kecil` (< **150.000**, STRIKT) | **2** |
| `bagian_mati_byte_kecil` | **0.0014275517487508922** |

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
  turunan). Menyebut "sembilan pemeriksaan bebas" DILARANG (KC-50).

**Sidik `irisan_byte` V1 =**
`0e7103ef46a37d1e442d8e7fc5b9771b1ef7cdc3956ea57d584d84f6f73ea2c6`

## BYTE PARQUET ATAS SELURUH SEMESTA [v7, tetap berlaku]

Sumber: `byte_semesta.py` V1 run **30526358811** (commit `d3bc2039`, kode 0), laporan
blob `8b7f2077`. **Total byte parquet = 32.706.262.375** (≈32,7 GB) atas 19.586
simbol-bulan. `bagian_byte_mati` = **0.017704297493883234**;
`cacah_terukur_byte_kecil` (< 10.000) = 0; `cacah_byte_nol` = 0 → **dasar keras ≈22
KB**, sebab langsung KC-48. Adjudikasi R-307: **MELESET**.
Sidik = `e02aca2b3967069b500b01d27a1d2d1553f47b912ea41ddbecd9e4e6c33883c7`

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
3/3 — kemenangan sah, klaim ilmiah hampir kosong. Sidik =
`4a5c2e4279eb1554dc119b48d6a8db61f6ea4ee11b7539efd70ee71d1ae18bf3`

## Jumlah uji — terukur

**1341**, kini dengan **EMPAT** bacaan berjejak berturut-turut:

1. blob **`2d32f814e5e426e1411559810b55b9f20176a22d`**, run **30542217837**, commit
   `b1c7941d` (push trio `sisa_defisit`), 12:22:10Z, kode 0, 0.62s.
2. blob **`bce1177ea21d7a4e01b59b2d4f4277a8584b4eed`**, run **30545364506**, commit
   **`8c30de51cc4d0098d4bd2922966684591bd7ce96`** (push STATE v51), 13:05:55Z, kode 0,
   0.45s.
3. blob **`2c3290cb23097ab93f196f79e61c751221fe4b4d`**, run **30548418622**, commit
   **`28afc9ae075befe1bc3c1ed474f42d7dae95626e`** (push STATE v52), 13:46:02Z, kode 0,
   0.60s.
4. **[BARU v12]** blob **`ed743bdf367d41ee0dcbd3d7b6cfc56244eeb662`**, run
   **30549286062**, commit **`e68deab7b9bc2a96b597ba58573aca358c707b21`** (push EKOR
   v12), **2026-07-30T13:57:06Z**, kode 0, `1341 tests collected in 0.64s`.

Riwayat: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 → 984 →
1044 → 1100 → 1168 → 1233 → 1297 → **1341**.
Turunan: 1297 + **44** butir `tests/test_sisa_defisit.py` = **1341** ✅ (aturan 21).

Blob CI yang dicatat: 1168 = `2498e2cf6e6f6c7d0b8807bb5ba923ac1d803b6d` · 1233 =
`0489d71101e451efe73d20fd8fe75ba6d41c5c27` (run 30532058688) · 1233 =
`016fb2349a960100d270bec926e73d5b2c85e9cc` (run 30533500210) · 1297 =
`3c07c9093d5232ce3852b2ac509fd9e9875f0f33` (run 30535202643) · 1341 = keempat blob di
atas. Run **30541051907** (1297, commit `5d7d8b96`) tercatat **TANPA blob** — diwarisi
dari jurnal 135, blobnya sudah tertimpa dan tidak dapat dipulihkan.

**Aturan 57: beruntun 3 dari 3** sesudah PUTUS di 26/27. Tidak bertambah sejak v11:
tidak ada push yang menyentuh `tests/**`. Ramalan ketiga dibuat dengan daftar bernomor
`test_01`..`test_44` tanpa rentang; dua helper `_baris` dan `_ringkasan_bersih` sengaja
berawalan garis bawah agar tidak dikumpulkan pytest.

### Aturan 38 — ordinal, kini sampai ke-42

Definisi yang berlaku (ADR-A018 kep. 8): pemakaian dihitung **hanya** untuk pembacaan
`reports/ci_terakhir.json` yang meninggalkan **jejak tertulis** berupa nomor run,
commit, dan blob.

| ke- | CI | run | commit | blob | jejak |
| --- | --- | --- | --- | --- | --- |
| 39 | 1341 | 30542217837 | `b1c7941d` | `2d32f814` | jurnal 135, STATE v51 |
| 40 | 1341 | 30545364506 | `8c30de51` | `bce1177e` | EKOR v11, STATE v52 |
| 41 | 1341 | 30548418622 | `28afc9ae` | `2c3290cb` | EKOR v12 |
| **42** | **1341** | **30549286062** | **`e68deab7`** | **`ed743bdf`** | **berkas ini** |

**Dua cacat tetap disebut, tidak dihaluskan:**

- Baris ke-**38** (run `30541051907`, commit `5d7d8b96`) **tanpa blob**. Ordinal ini
  karena itu sah **relatif terhadap definisi di atas**, bukan sebagai pencacahan
  mutlak.
- Run **30547842823** (commit bot `de2fc03d`, atas push UKUR v11 `f9c5d960`) **tidak
  pernah dibaca** dan sudah **tertimpa**. Ramalan "CI tetap 1341" untuk push itu
  **TIDAK TERUKUR — bukan menang, bukan kalah**, dan blobnya hilang permanen. Ia
  **DILARANG dihitung** sebagai pemakaian aturan 38.

**Aturan kerja yang lahir dari kerugian itu, dicatat sebagai calon, bukan aturan
bernomor:** dua berkas akar yang didorong berturut tanpa membaca laporan di antaranya
pasti menghanguskan yang pertama. Belum diangkat menjadi aturan karena baru **satu**
kejadian terukur — mengangkatnya sekarang mengulang KC-48.

**Koreksi resmi atas STATE v51** (ADR-A018 kep. 7): STATE v51 menulis bahwa ramalan
"CI tetap" pada push dokumen **tidak pernah terukur**. Itu terbantah oleh run
30545364506. Rumusan yang benar: ramalan semacam itu **terukur bila laporannya dibaca
sebelum run berikutnya menimpanya**, tetap berlabel MUDAH, tetap tidak diskor, tetap
tidak menambah beruntun aturan 57.

## Modul, workflow, dan berkas uji [v11, tidak berubah di v12]

**UTANG CACAH TANGAN LUNAS.** Pencacahan TANGAN satu per satu bernomor (aturan 66)
dilakukan pada ref **`3196fd9809f23917ba819b4339cdfdd57bb808d1`**:

| direktori | cacah TANGAN |
| --- | --- |
| `lux_ai/serapan/` (berkas `.py`) | **49** |
| `tests/` | **53** |
| `.github/workflows/` | **44** |
| akar repo | **18** entri (6 direktori + 12 berkas) |

Ini menggantikan angka sah lama 47/51/42 pada ref `07a69d39` dan angka 48/52/43 pada
ref `5d7d8b96`. Keduanya tetap sah **untuk ref masing-masing**. Begitu trio ukur
berikutnya didorong, 50/54/45 menjadi **TURUNAN dan DILARANG dikutip sebagai terukur**
sampai dicacah tangan ulang.

**PERINGATAN DUA CACAH `tests/` (ADR-A018 kep. 10).** `PETA_MODUL_BERKAS.md`
(blob `3abe95f6`) mencatat **34** berkas uji milik repo **WARISAN `bot_v8`**. Repo
riset ini punya **53**. Keduanya benar untuk repo masing-masing; **menyebut "cacah
uji" tanpa menyebut repo-nya DILARANG**, karena selisihnya akan tampak seperti
pelanggaran aturan 66 padahal bukan.

**Peringatan dini aturan 48:** tiga modul terbesar `lux_ai/serapan/` menurut byte
listing — `silang_funding.py` **29.873** · `funding.py` **28.121** ·
`sisa_defisit.py` **25.949**.

Blob trio R-311 (ketiganya dibaca ulang UTUH dari main sesudah push `b1c7941d`,
aturan 52 dan 55):

- `lux_ai/serapan/sisa_defisit.py` V1 blob
  **`7aa0e6d7003902e50806570ad112aae7f0345b07`** (25.949 B).
- `tests/test_sisa_defisit.py` blob **`7004115acffd9c03c9ba4f9873bef40cb6b1375f`**
  (12.640 B, **44** butir, dicacah TANGAN `test_01`..`test_44`; helper `_baris` dan
  `_ringkasan_bersih` berawalan garis bawah).
- `.github/workflows/sisa_defisit.yml` blob
  **`645112075e104a74d43f3e3d2185cfbd48b0b513`** (`paths` **SATU** entri).

Blob trio R-310 tetap: `keterisian_lilin.py` **`3f80ffa72008008d567ef32f9f278b8931e91ac3`** ·
`test_keterisian_lilin.py` **`f58912d0b1531dbf537de4c0b4f0a803a3ad1f69`** (64 butir) ·
`keterisian_lilin.yml` **`d821c63a462a8338ccd63f8014f7c8847602fdff`**.
Blob trio v9 tetap: `bulan_pertama.py` `b9bd00ac` (19.349 B) ·
`test_bulan_pertama.py` `75d87ba2` (13.375 B, 65 butir) · `bulan_pertama.yml`
`2242e3e4`. Lainnya identik: `irisan_byte.py` `2dbe3d55`, `test_irisan_byte.py`
`b6389051` (68 butir), `irisan_byte.yml` `7d98a267`, `kehidupan.py` `f49abb2b`,
`kehidupan_arsip.py` `318a5cb1`, `silang_funding.py` V2 `42c3aa9d`, `kohort_ekor.py`
`c9b63bbe`, `lubang_awal.py` `8c36943d`, `lubang_tebing.py` `575e777e`,
`lubang_tengah.py` `4d3beaf1`, `sebab_bangkit.py` `fd5a1dc4`, `tersisip_semesta.py`
`8a648838`, `bentangan_kohort.py` V2 `f4eae57a`, `byte_semesta.py` `ff68e4be`,
`funding.py` `8d4b1f82`, `arsip.py` `0104958b`, `gerbang_1m.py` `c8cc54c8`,
`resample.py` `66a4b177`, `semesta_kuota.py` `7288b030`, `bulan_absen.py` `10279d72`,
`kebangkitan.py` `446321ee`, `penyebut_tahun.py` `265aad00`, `anatomi_tengah.py`
`04279335`, `__init__.py` `64d85584`. `ci.yml` = `c79497b2` (paths-ignore
journal/decisions/hipotesis/reports; push ke `lux_ai/**`, `tests/**`, `STATE*`,
`PROMPT*` MENYALAKAN CI). `karantina_semesta.yml` = `de40fa4e` (**belum dibaca utuh**).

Cacah per berkas uji yang diketahui — **milik repo riset ini, bukan repo warisan**
(penanda tebal diperbaiki di v12, Koreksi 8; angkanya tidak berubah):
`test_irisan_byte.py` **68** · `test_bulan_pertama.py` **65** ·
`test_keterisian_lilin.py` **64** · `test_bentangan_kohort.py` V2 **63** (blob
`9f850ecdb25466d38c839004b36ff221db2cf7f8`, 13.154 B — dibaca UTUH, dicacah TANGAN
`test_01`..`test_63`, utang verifikasi LUNAS) · `test_lubang_tebing.py` **60** ·
`test_sebab_bangkit.py` **57** · `test_byte_semesta.py` **56** ·
`test_lubang_awal.py` **48** · `test_tersisip_semesta.py` **47** ·
`test_anatomi_tengah.py` **47** · `test_sisa_defisit.py` **44** ·
`test_terhenti.py` V4 **33** · `test_bulan_absen.py` **32** ·
`test_karantina_semesta.py` **28** · `test_silang_settled.py` **24**.

**Pola workflow trio (terbukti lagi pada `sisa_defisit.yml`):** `name`,
`on.push.paths` SATU entri, `permissions: contents: write`, job `ukur` di
`ubuntu-latest`, checkout@v4 + setup-python@v5 (3.11), `pip install numpy pandas
pyarrow pyyaml`, langkah `jalan` id=`jalan` dengan `set +e` → `KODE=$?` →
`echo "kode=$KODE" >> "$GITHUB_OUTPUT"` → `exit 0`, langkah `catat status` (printf
JSON ke `reports/<modul>_status.json`), langkah `dorong laporan` (git config bot,
add, commit `[skip ci]`, pull --rebase, push), langkah akhir
`exit ${{ steps.jalan.outputs.kode }}`.

## API terverifikasi — tambahan v11 (tidak berubah di v12)

API lama (v37–v10) tetap berlaku. Tambahan:

**`sisa_defisit` V1** (blob `7aa0e6d7`, dibaca UTUH dari `b1c7941d` sesudah push):
mengimpor `kehidupan`, `kehidupan_arsip`, `silang_funding`, dan **menurunkan
`lilin_penuh`/`hari_dalam_bulan` dari `keterisian_lilin`** (pemakaian ulang, bukan
salinan — KC-43 terjaga untuk kelima kalinya).
Tetapan: `VERSI=1`, `KELUARAN="reports/sisa_defisit.json"`,
`KELUARAN_RINGKAS="reports/sisa_defisit_ringkas.json"`, `BATAS_BARIS_LAPORAN=40`,
`MENIT_PER_HARI=1440`, `MEDAN_LILIN="cacah_lilin"`, `CACAH_TERATAS=10`,
`R311_PITA_BUTIR_1=(200,12000)`, `R311_PITA_BUTIR_2=(0.02,0.45)`,
`DEFISIT_SEMBILAN_TERCATAT=95237`, `DEFISIT_BUKAN_PERTAMA_TERCATAT=808162`,
`SISA_TERCATAT=712925`, `BERKAS_DICAP` 4 nama, `INVARIAN` delapan kunci seluruhnya
BEBAS, **`JAWABAN_KENDALI` 17 medan** (dengan `bagian_teratas` **0,9677** = 600/620,
dihitung TANGAN lebih dulu).
Fungsi: `nama_keluaran`, `nama_ringkas`, `daftar_sumber`, `sidik_kode`,
`peta_bulan_pertama`, `kumpulkan`, **`baris_calon`**, **`baris_berdefisit`**,
**`teratas`** (mengembalikan **None** untuk `bagian_teratas` bila baris berdefisit
< 10 — bukan 0, bukan galat), `ringkas`, `selisih_sisa`, `sebaran_kelas`,
`invarian_terukur`, `selisih_invarian`, `kendali_data`, `kendali_data_sah`,
`semesta_kendali`, `kendali_deteksi`, **`kendali_nol`**, `dalam_pita`,
`dalam_pita_pecahan`, `uji_r311`, `kode_keluar`, `jalankan(akar=".", total=None)`,
`berkas_ringkas`, `main`.
**Yang wajib disebut:** penyebut kerja **17.398** dihitung LANGSUNG dari baris, bukan
disalin; `selisih_sisa` = 0 **tautologis** dan DILARANG disebut pengukuran bebas
(KC-50); `kendali_nol` yang membuat `cacah_berdefisit` bermakna (aturan 50).

**`keterisian_lilin` V1** (blob `3f80ffa7`): `VERSI=1`,
`TOTAL_PECAHAN=kehidupan_arsip.TOTAL_PECAHAN`, `BATAS_BARIS_LAPORAN=40`,
`MENIT_PER_HARI=1440`, `MEDAN_LILIN="cacah_lilin"`, `KENDALI_SIMBOL="BTCUSDT"`,
`KENDALI_CACAH=3`, `AMBANG_HIDUP_KECIL=97634`, `R310_PITA_BUTIR_1=(1,120)`,
`R310_PITA_BUTIR_2=(0.02,0.25)`, `INVARIAN` delapan kunci BEBAS, `JAWABAN_KENDALI`
(3, 1, 1160, 520, 640, 213400, 0, 0.5517). Fungsi kunci: `hari_dalam_bulan`,
`lilin_penuh`, `defisit`, `baris_mati_tak_penuh`, `kendali_negatif`, `uji_r310`,
`jalankan(akar=".", total=None)`.

**`bulan_pertama` V1** (blob `b9bd00ac`): `R309_PITA_BUTIR_1=(22,38)`,
`R309_PITA_BUTIR_2=(0.10,0.60)`, `BULAN_TEPI="2026-06"`, `AMBANG_HIDUP_KECIL=97634`,
`DETEKSI_PERTAMA=2`, `DETEKSI_HIDUP_KECIL=2`, `DETEKSI_SEBAGIAN=2`,
`DETEKSI_NISBAH=0.75`, `DETEKSI_TOTAL_BYTE=1500`, `nisbah_pertama` (penyebut kosong →
**None**), `total_byte_langsung`.

**`irisan_byte` V1** (blob `2dbe3d55`): `AMBANG_HIDUP_KECIL=97634`,
`AMBANG_MATI_KECIL=150000`, `R308_PITA_BUTIR_1=(20,600)`,
`R308_PITA_BUTIR_2=(10,300)`, `MEDAN_SELISIH` **9** (delapan bebas + satu turunan),
`DETEKSI_TOTAL=1922`.

**`silang_funding` V2** (blob `42c3aa9d`, 29.873 B): `baca_laporan_kehidupan(akar,
total)` → **TIGA** nilai `(status, byte_parquet, meta)`, kunci tuple
`(simbol, bulan)`; `baca_medan_baris(akar, total, medan)` → `(nilai, meta)`, MELEWATI
baris ber-medan `None` — dipakai `keterisian_lilin` dan **`sisa_defisit`** dengan
`medan="cacah_lilin"`; `bulan_per_simbol(status)`; `lubang_funding(funding)`;
`bentuk_lubang_lokal(bulan_urut, bulan_berlubang, bulan)` →
bukan_lubang/awal/ekor/seluruh/tengah; `kendali_silang`; `kendali_sah`;
`SUMBER_FUNDING="reports/funding_semesta.json"`, `KENDALI_CACAH=3`,
`PENYEBUT_TERCATAT=19586`, `MATI_TERCATAT=1401`, `KOHORT_TERCATAT=456`,
`HIDUP_TANPA_FUNDING_TERCATAT=33`, `LUBANG_TAK_DIKENAL_TERCATAT=3`,
`BENTUK_TERBITAN_FUNDING={"awal":48,"ekor":826,"tengah":6}`.

**`bentangan_kohort` V2** (blob `f4eae57a`, uji `9f850ecd`): `VERSI==2`; `TEBING`,
`BULAN_DIHARAPKAN`, `KENDALI_HIDUP` diwarisi `kohort_ekor`; `MEDAN_LILIN` dan
`SUMBER_FUNDING` diwarisi `silang_funding`; `R301_BUTIR_1_HIDUP_SESUDAH_TEBING=0`,
`R301_BUTIR_2_MINIMAL_SATU_TERSISIP=1`, `R301_BUTIR_3_BANGKIT=0`; `BERKAS_DICAP` 4
nama. Butir uji 09 menolak `str(tuple)` sebagai kunci (penangkal cacat V1); butir
59–61 memanggil `silang_funding` asli untuk memeriksa BENTUK kembalian; butir 63
melarang nama kohort tertulis di dalam modul (aturan 73); butir 37 menuntut `None`,
bukan nol.

**`byte_semesta` V1** (`ff68e4be`): `R307_PITA_BUTIR_1=(0.02,0.15)`,
`R307_AMBANG_BYTE_KECIL=10000`, `R307_PITA_BUTIR_2_CACAH=(20,400)`.
**`lubang_awal` V1** (`8c36943d`): medan `mati_tidak_setelah_lubang_bukan_awal`
memakai `<=` — **DILARANG dipakai untuk klaim arah** (aturan 80). Sidik `156499ce…`.
**`kohort_ekor` V4** (`c9b63bbe`): `TEBING="2025-07"`, `BULAN_DIHARAPKAN="2026-06"`,
`BATAS_SIMBOL=10`, `PAGU_MUNDUR=60`, `AMBANG_SEPI=0.5`,
`KENDALI_HIDUP=("BTCUSDT","ETHUSDT")`.
**`kehidupan_arsip`** (`318a5cb1`): `TOTAL_PECAHAN=8`, `AKAR_UNDUH="data/unduh"`,
`AKAR_BONGKAR="data/kehidupan_arsip"`, `KOLOM_VOLUME="volume"`,
`KOLOM_TRANSAKSI="trades"`.
**`kehidupan`** (`f49abb2b`): `AMBANG_SEPI=0.5`, `STATUS_MATI/SEPI/HIDUP/TAK_TERUKUR`,
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
Keempatnya COCOK lagi pada run `sisa_defisit` (aturan 36, kini **lima** run berturut)
→ semesta SAMA.

## Hipotesis

- H-A001 belum diuji · H-A002b GUGUR · H-A003 MENANG pada 3, GUGUR pada 9 · H-A004
  tak dapat diuji · H-A005 GUGUR · H-A006 MENANG enam run · H-A008 MENANG dua kali ·
  H-A009 GUGUR · H-A010 MENANG 5–0 · H-A011 MENANG · H-A012 MENANG · H-A013 MENANG
  6–0, TAFSIR DICABUT · H-A014 BENTUK BARU MENANG 9 dari 9 · H-A015 MENANG sebagai
  angka, DIBATASI sebagai tafsir (KC-45) · H-A016 PENGAMATAN, BELUM DIUJI.
- **H-A017** DICABUT sebagai pola semesta (ADR-A011/A012, dilemahkan R-306): bukti
  lepas-tebing tinggal **1** simbol. TIDAK dipulihkan oleh R-307..R-311.
- **H-A018 — byte parquet sebagai gejala kehidupan. DIUKUR DUA KALI (R-307, R-308).**
  **Bunyi yang BOLEH dipakai:** "bulan MATI menempati bagian KECIL dari byte semesta
  (**0,0177** dari 32,7 GB) dan rata-rata sekitar **4,3×** lebih kecil daripada bulan
  HIDUP (413.306 lawan 1.771.963 byte)".
  **Bunyi yang DILARANG:** "berkas kecil berarti pasar mati" — di zona 22.440–97.634
  byte ada **38 HIDUP dan 0 MATI**. **[v11] R-311 justru memperkuat larangan itu:**
  baris paling kosong di seluruh semesta (TLMUSDT 2023-03, 95,2% kosong) berstatus
  **HIDUP**.
- **H-A019 [DIUJI R-309 — DITERIMA TERBATAS oleh ADR-A016 kep. 1].**
  **Rumusan resmi satu-satunya:** *hampir setiap baris HIDUP di zona byte kecil adalah
  bulan pertama simbol itu di dalam penyebut (**37 dari 38**), sementara hampir setiap
  bulan pertama BUKAN berkas kecil (**37 dari 787, ±4,7%**).* Irisan asimetris, bukan
  sebab. Klausa `2026-06` DICABUT. Batas tafsir: "bulan pertama" = di dalam penyebut,
  bukan di bursa.
  **[v11] Perlawanan TLMUSDT 2023-03 TIDAK LAGI tak terjelaskan** — sifatnya terukur
  (baris berdefisit terbesar semesta). Tafsir "byte kecil = bulan sebagian di tepi"
  **MELEMAH**; tafsir pengganti **TIDAK ditegakkan** (ADR-A018 kep. 6). H-A019 tetap
  DITERIMA TERBATAS.
- **H-A020 [DIUSULKAN, BELUM DIUJI].** *Ketujuh baris MATI tak penuh berbulan
  `2024-05` adalah SATU peristiwa, bukan tujuh pengamatan bebas: jendelanya hanya
  sembilan lilin (39.308..39.317).* DILARANG menulis "tujuh simbol didelisting 28 Mei
  2024" sebagai temuan. Cara mengujinya: `lubang_tengah` atas gugus 2024-05.
- **H-A021 [v11, DIUSULKAN, BELUM DIUJI].** *Kekosongan **ANCUSDT `2022-05`**
  (defisit **26.959**) dan **LUNAUSDT `2022-05`** (defisit **26.950**) adalah SATU
  peristiwa yang sama, bukan dua pengamatan bebas.* Dasarnya hanya selisih **sembilan
  lilin** di bulan yang sama — **kebetulan angka, bukan bukti**. Sampai diuji, **setiap
  kalimat sebab untuk gugus `2022-05` DILARANG.** Bila kelak DITERIMA, cacah pengamatan
  bebas dalam sepuluh baris teratas turun dari 10 menjadi 9, dan `bagian_teratas`
  **tidak berubah** karena ia dihitung atas lilin, bukan atas baris.
- Hipotesis berikutnya **H-A022**.

## Praregistrasi R-310 — SUDAH TERADJUDIKASI: TEPAT

Disimpan apa adanya sebagai jejak (aturan 29). Poros: isi berkas bulan MATI.

- **Butir 1 (BERISIKO).** Cacah baris MATI berlilin kurang dari penuh, dari 1.401.
  Pita **1 .. 120** → **9** → **MENANG** (tipis ke tepi BAWAH).
- **Butir 2 (BERISIKO).** Bagian defisit yang ditanggung baris BUKAN-pertama.
  Pita **0.02 .. 0.25** → **0,0445** → **MENANG** (tipis ke tepi BAWAH).
- **Butir 3 (MUDAH).** → **MENANG**.

**Tiga calon butir yang DIBUANG sebelum pita dikunci** (jejak aturan 83 bekerja):
(a) cacah baris MATI berlilin PENUH — tersirat ≈1.370–1.401, terukur 1.392;
(b) cacah MATI ber-`cacah_lilin` < 1.440 — hampir pasti 0; (c) nisbah byte-per-lilin
MATI:HIDUP — tersirat 0,233.

**Cacat yang ditemukan SESUDAH menang:** numerator 9 bukan sembilan pengamatan bebas
(KC-47), dan bahan baku taksirannya memakai 839.842.134 yang ternyata bukan jumlah
lilin (Koreksi 4, KC-50).

## Praregistrasi R-311 — SUDAH TERADJUDIKASI: SEPARUH

Disimpan apa adanya sebagai jejak (aturan 29); teks disalin dari jurnal 134 dan TIDAK
diubah sesudah pengukuran. Poros: **sisa 712.925 lilin**.

- **Butir 1 (BERISIKO).** Cacah baris bukan-pertama bukan-MATI yang `cacah_lilin`-nya
  kurang dari lilin penuh bulannya. Pita **200 .. 12.000**, taksiran titik 3.000.
  → terukur **114** → **KALAH**, meleset **26,3 kali** dari taksiran dan **1,75 kali**
  di bawah tepi bawah.
- **Butir 2 (BERISIKO).** Bagian defisit sisa yang ditanggung **sepuluh** baris
  teratas. Pita **0,02 .. 0,45**, taksiran titik 0,15. → terukur **0,4087** →
  **MENANG**, sisa hanya **0,0413** ke tepi ATAS; meleset **+172%** dari taksiran.
- **Butir 3 (MUDAH).** Delapan invarian nol, kendali sah, `kendali_nol` bekerja, kode
  keluar 0, CI diukur. → **MENANG**.

**Aturan 83 DITAATI PENUH dan TETAP KALAH.** Lantai aritmetis **16** dihitung sendiri
di jurnal 134 dan rentang implikasinya (16 .. 18.790) benar. Tepi bawah tetap
diletakkan di **200** — dua belas setengah kali lantai — **tanpa satu kalimat pun yang
membenarkannya**. Aturan 83 menuntut aritmetikanya dihitung; ia tidak pernah menuntut
hasilnya **dipakai**. Lubang itu ditutup **aturan 85** (ADR-A018 kep. 2), yang berlaku
mulai **R-312** dan **tidak berlaku surut**; R-311 **tidak** diadjudikasi ulang
(aturan 29).

**KC-51 — bias taksiran pemusatan. Rumusan resmi:**

> Ketika sebuah besaran belum pernah diukur sebarannya, taksiran yang saya buat secara
> sistematis mengandaikan besaran itu **lebih menyebar** daripada kenyataannya.
> Akibatnya tepi pita di sisi "terpusat" diletakkan terlalu jauh dari lantai
> aritmetis, dan pita kalah ke sisi itu.

Empat kejadian berturut tanpa satu pun pembalikan arah:

| ramalan | besaran | taksiran / pita | terukur |
| --- | --- | --- | --- |
| R-308 butir 2 | cacah MATI ber-byte kecil | 10 .. 300 | **2** |
| R-310 butir 2 | bagian defisit bukan-pertama | 0,073 (0,02..0,25) | **0,0445** |
| R-311 butir 1 | cacah baris berdefisit | 3.000 (200..12.000) | **114** |
| R-311 butir 2 | pemusatan sepuluh teratas | 0,15 (0,02..0,45) | **0,4087** |

**DILARANG oleh KC-51:** menyebut kemenangan butir 2 sebagai bukti kalibrasi membaik.
**KC-51 kini RESMI** (ADR-A018 kep. 1, teks penuh di STATE v52), dan penangkalnya —
**aturan 85** — RESMI berlaku mulai **R-312**.

## Praregistrasi R-312 — BELUM ADA

Poros sudah **ditetapkan** di ADR-A018 kep. 12, tetapi **praregistrasinya DILARANG
ditulis di lampiran ini**; ia wajib ditulis di **jurnal** lebih dulu (aturan 79), pada
giliran yang BERBEDA dari adjudikasi (ADR-A016).

1. **(a) Lubang tengah gugus `2022-05` dan `2024-05`** — menguji **H-A021 dan H-A020
   sekaligus**: apakah baris berdefisit yang berhimpit bulan itu berbagi satu jendela
   lilin yang sama.
2. **(b) Selisih 516.135** lawan dugaan 12 simbol-bulan karantina
   (516.135 / 12 = 43.011 — **DUGAAN, BELUM DIUJI**). Porosnya **wajib berupa bentuk
   SEBARAN, bukan rata-rata**, sebab rata-rata 43.011 akan selalu benar secara
   aritmetis dan karena itu tidak berisiko.

Sebelum pita dikunci: aturan 83 WAJIB dipenuhi di jurnal lebih dulu; **aturan 85 WAJIB
diterapkan pada tiap butir cacah/bagian yang sebarannya belum diukur — tepi "terpusat"
di lantai aritmetis atau paling banyak satu orde di atasnya, dengan alasan tertulis**;
aturan 84 WAJIB (satu klausa per butir); nama modul WAJIB dicek lewat pencacahan
direktori TANGAN lebih dulu (aturan 66 — 49/53/44 sah untuk ref `3196fd98`, dan
angka turunan sesudah trio berikutnya DILARANG dikutip); laporan WAJIB ringkas
(`BATAS_BARIS_LAPORAN`).

## Utang ukur yang masih hidup

1. **`karantina_semesta.yml`** (`de40fa4e`) belum dibaca utuh; begitu pula
   `test_pulihkan.py` (`11c43533`), `test_rilis_karantina.py` (`739c8da9`),
   `test_karantina_a006.py` (`a5a3d82f`).
2. **Lima ADR belum dibaca utuh:** A002, A004, A006, A007, A008.
3. **Irisan 880 lawan 877 lubang funding** belum diukur.
4. **Perbedaan "bulan pertama di penyebut" lawan "bulan pertama di bursa"** belum
   diukur (ADR-A016 kep. 6).
5. **Sebab kekosongan TLMUSDT 2023-03** belum diukur; tidak ada tafsir yang ditegakkan.
6. **Tiga butir `PETA_MODUL.md` bertanda "memerlukan verifikasi"** (repo WARISAN,
   bukan repo ini): atribut `enable_hs` yang tidak ditemukan di `config.py` padahal
   dipakai `strategy.py`; klaim "30 pair dipilih alfabetis" tanpa bukti; klaim
   "kendala mengikat = kapasitas margin" yang belum diuji angkanya.
7. **`PROMPT_KELANJUTAN.md`** belum diberi kepala "ARSIP — BUKAN SUMBER" dan belum
   dihapus (ADR-A018 kep. 9).
8. **[BARU v12] `STATE.md` v53** wajib mengubah "Empat salah ketik kami sendiri"
   menjadi **"Enam"** — tabelnya memuat enam baris dan paragraf di bawahnya sudah
   menyebut "keenam".
9. **[BARU v12] `PROMPT.md` v55** belum didorong ke repo.
10. **[BARU v12] Jurnal 136 + praregistrasi R-312** belum ditulis; itulah pekerjaan
    ukur berikutnya, dan pemakaian pertama **aturan 85**.
