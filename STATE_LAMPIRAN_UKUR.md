# STATE lampiran UKUR — bagian 3 dari STATE (v9, milik STATE v49)

**Kedudukan berkas ini.** STATE dipecah tiga sejak v43 (KC-42). Pembagian berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81 dan 83, KC-1..KC-49.
2. **`STATE_LAMPIRAN_EKOR.md`** v9 — bagian 2: papan skor, ADR, catatan kejujuran.
3. **`STATE_LAMPIRAN_UKUR.md`** (berkas ini, v9) — bagian 3: pengukuran, modul,
   workflow, uji, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip lama; bukan sumber lagi.

Dasar v9: UKUR v8 (blob **`ff19069512bd4604b18cedb896af1d6cf6ba2557`**), dibaca UTUH
sebelum berkas ini ditulis (aturan 52). Yang ditambahkan v9: **irisan bulan pertama**
(pengukuran pertama); API `bulan_pertama` V1; CI **1233**; adjudikasi **R-309 TEPAT**;
cacah tangan tiga direktori LUNAS pada ref `010edff2` (**47 / 51 / 42**); **H-A019
DIUJI dan DITERIMA TERBATAS**; koreksi resmi atas daftar dugaan v8.

**KETIMPANGAN VERSI SELESAI — ketiga bagian kini serasi pada v49 / v9 / v9.**
Peringatan keserasian di kepala v8 (yang menyebut `STATE.md` masih v47) **GUGUR**:
`STATE.md` sudah naik ke v48 lalu **v49** (blob
**`64dc7b3fed15b447f297874e8410c9a6c4b7dd4e`**, commit `8dd0e4a5`), dan EKOR sudah
naik ke **v9** (blob **`beaed54cb93e00c2c56f1aaa8d1c2709c97f08d0`**, commit
`a3830617`). Jejak peringatan lama sengaja tidak dihapus dari riwayat; jangan
memperlakukannya sebagai utang hidup. Pemecahan bertahap tetap SENGAJA: menulis tiga
berkas besar dari satu konteks terpakai adalah cara paling pasti merusak aturan 1–83
(KC-42, KC-43).

**Tentang push berkas ini:** berkas ini di akar repo sehingga menyalakan `ci.yml`.
Tidak satu pun `tests/**` berubah, jadi cacah uji tetap **1233** — ramalan
deterministik (aturan 57), **MUDAH**, TIDAK masuk papan skor.

**Angka yang TIDAK berubah dari v44/v45/v6/v7** (tidak diulang): taksonomi 9 kelas,
karantina 12, bulan ABSEN 11, H-A013..H-A015, terhenti, SETTLED. Rinciannya di v44
(blob `d302caff`), v45 (`eb826817`), v6 (`27e59a79`), v7
(`4e7fb65be81bc5657da94060447075f0f1e2d73c`).

## KOREKSI KC-41 — BACA SEBELUM MENGUTIP BERKAS INI

Ketiga koreksi di bawah **tetap dicantumkan** karena semuanya soal dokumen kami
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
`irisan_byte.yml` (`7d98a267`), dan `bulan_pertama.yml` (`2242e3e4`) meniru berkas
ASLI ini, bukan rumusan v5.

**Koreksi 2 (kesalahan PROMPT v49).** PROMPT v49 menyebut poros R-307 "H-A017";
yang benar **H-A018**. PROMPT v50 sudah memuat koreksi — **utang koreksi LUNAS**.

**Koreksi 3 [BARU v9] (kesalahan v8 dan jurnal 129, dari DUGAAN bukan kutipan).**
v8 menulis bahwa MTLUSDT 2021-03, ENJUSDT 2020-09, SLPUSDT 2023-10, dan TLMUSDT
2023-03 "tampak bulan tengah" sehingga MELAWAN H-A019. **Tiga dari empat SALAH.**
Terukur oleh `bulan_pertama` V1: MTLUSDT 2021-03, ENJUSDT 2020-09, dan SLPUSDT
2023-10 justru bulan **PERTAMA** simbolnya di dalam penyebut. Yang benar-benar
melawan hanya **TLMUSDT 2023-03 (80.394 byte)**. Kalimat v8 itu **DICABUT**
(ADR-A016 kep. 4). Pelajaran: membaca daftar dengan mata lalu menyebutnya "tampak"
adalah tebakan, bukan ukuran.

## Semesta riset = `perpetual_usdt` = penyebut 787 — tidak berubah

- `cacah_perpetual_usdt` **787** = `cacah_penyebut_simbol` **787**
- `cacah_perpetual_usdt_luar_penyebut` 0, `cacah_penyebut_bukan_perpetual_usdt` 0
- Batas wajib disebut: token saham/ETF/komoditas ikut di dalam 787.

## KC-18 — semesta kehidupan (dikonfirmasi ulang oleh R-307, R-308, DAN R-309)

Atas **19.586** simbol-bulan lolos: **1.401 MATI** (7,153%), **98 SEPI**, **18.087
HIDUP**. Dari 1.401 MATI: 842 kehilangan funding, 559 tetap berfunding.
`cacah_simbol_tanpa_hidup` **18**.

`cacah_lain` = 0 pada ketiga modul → seluruh 19.586 berstatus MATI/SEPI/HIDUP, tidak
ada TAK_TERUKUR. 18.087 + 98 = 18.185 TERUKUR, + 1.401 = 19.586 ✅

**Pembelahan BARU atas penyebut yang sama [v9]:** **787** baris adalah bulan PERTAMA
simbolnya (tepat satu per simbol — identitas, bukan kebetulan), **18.799** baris
bukan-pertama. 787 + 18.799 = **19.586** ✅

## Lubang funding — agregat semesta (tetap)

- `cacah_simbol_ada_lubang` = **122** (dari 787) · awal **5** · bukan-awal **118**
- BNXUSDT punya lubang AWAL dan bukan-awal sekaligus.
- Lima bentuk AWAL: BNXUSDT, ICPUSDT, JUPUSDT, QTUMUSDT, TLMUSDT. ICP dan TLM lubang
  awalnya melewati kematian (sumber salah-baca R-304, KC-46).
- Lubang funding **880** semesta / **877** dalam penyebut / 3 tak dikenal. Irisan
  880 lawan 877 BELUM diukur.

## IRISAN BULAN PERTAMA [BARU v9 — pengukuran PERTAMA]

Sumber: `bulan_pertama.py` V1 run **30532058657** (commit `09ce9853`, kode 0).
Laporan `reports/bulan_pertama.json` blob
**`0a2aa6ae15d949b44803dffdc9e97dbd322bbc85`** (terbaca **UTUH** —
`BATAS_BARIS_LAPORAN=40` berhasil untuk ketiga kalinya berturut), `_status.json` blob
**`0c8ea41a5a1aea4090d0dd2de65c9652088fc462`**.

**Pertanyaan yang dijawab:** apakah baris HIDUP ber-byte kecil adalah bulan yang
tidak terisi penuh. Definisi "bulan pertama" yang dipakai: bulan TERKECIL milik
simbol itu **di dalam penyebut 19.586** (yaitu yang lolos gerbang 1m) — bukan bulan
pertama simbol itu di bursa. Perbedaan keduanya BELUM diukur dan dicatat sebagai
lubang ukur (ADR-A016 kep. 6).

| besaran | nilai |
| --- | --- |
| `cacah_hidup_kecil_sebagian` (dari 38) | **37** |
| `bagian_hidup_kecil_sebagian` | **0,973684** |
| `cacah_pertama` (baris bulan pertama, dari 19.586) | **787** |
| `cacah_bukan_pertama` | **18.799** |
| `jumlah_byte_pertama` | **706.233.745** |
| `jumlah_byte_bukan_pertama` | **32.000.028.630** |
| `rata_byte_pertama` | **897.374,517** |
| `rata_byte_bukan_pertama` | **1.702.219,726** |
| `nisbah_rata` | **0,527179** |

- **Irisan itu NYATA tetapi ASIMETRIS TAJAM.** 37 dari 38 berkas kecil adalah bulan
  pertama (**97,4%**); tetapi hanya 37 dari 787 bulan pertama yang berkas kecil
  (**±4,7%**). Rumusan resmi satu-satunya yang boleh dikutip ada di **ADR-A016 kep.
  1**. H-A019 menjelaskan ekor bawah; ia TIDAK meramalkan bahwa bulan pertama akan
  kecil.
- **Bulan pertama SEPARUH, bukan sepersepuluh.** Nisbah 0,527179 berarti berkas bulan
  pertama rata-rata setengah ukuran bulan biasa. Bulan pertama bukan bulan kosong.
- **Klausa tepi `2026-06` menyumbang NOL secara bebas.** Ketiga baris tepi
  (SQQQUSDT 72.819, TQQQUSDT 82.330, MVLLUSDT 86.126) **juga** bulan pertama
  simbolnya; menghapus klausa itu tetap menghasilkan 37. Klausa tersebut **DICABUT**
  dari rumusan H-A019 (ADR-A016 kep. 2), dan lahirlah **usulan aturan 84**.
- **Satu lawan yang tersisa:** **TLMUSDT 2023-03 (80.394 byte)** — bukan pertama,
  bukan tepi, tetap kecil. Belum dijelaskan; DILARANG dibuang sebagai pencilan.
- **Delapan medan selisih invarian, seluruhnya BEBAS dan seluruhnya 0.** Berbeda dari
  `irisan_byte`, `total_byte` di sini dihitung lewat **jalur LANGSUNG**
  (`total_byte_langsung`), tidak dijumlahkan dari byte per kelas — perbaikan atas
  calon KC-50 (ADR-A016 kep. 5). Yang tetap dinyatakan apa adanya: `byte_hidup` dan
  `total_byte` berbagi bahan baku yang sama, jadi bebas sebagai JALUR HITUNG, bukan
  sebagai bukti yang saling merdeka.
- **Kendali dua lapis sah.** Data (`kendali_data_sah` true): tiga parquet terbesar
  seluruhnya **BTCUSDT** — 2021-05 2.770.666, 2021-08 2.730.341, 2021-01 2.722.266,
  semuanya HIDUP. Detektor (`kendali_deteksi_sah` true): semesta buatan lima baris
  dua simbol, jawabannya dihitung TANGAN lebih dulu — `DETEKSI_PERTAMA` 2,
  `DETEKSI_HIDUP_KECIL` 2, `DETEKSI_SEBAGIAN` 2, `DETEKSI_NISBAH` 0,75,
  `DETEKSI_TOTAL_BYTE` 1.500 — seluruhnya cocok.
- **Adjudikasi R-309:** butir 1 **MENANG** (37 dalam 22..38), butir 2 **MENANG**
  (0,527179 dalam 0.10..0.60), butir 3 **MENANG** (MUDAH) → **TEPAT**. Bacaan
  jujurnya di EKOR v9 § Catatan kejujuran, termasuk peringatan bahwa butir 2 menang
  tipis ke tepi atas.

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

## LEBAR ZONA IRISAN BYTE [v8, tetap berlaku — dengan Koreksi 3 di atas]

Sumber: `irisan_byte.py` V1 run **30529294165** (commit `d22364b9`, kode 0). Laporan
`reports/irisan_byte.json` blob **`4c13bf6afc36c9afbeb1c662d6098258a6b750dd`**,
`_status.json` blob **`863dc4cb266b2fcee56fb733960722d37bd931e7`**.

| besaran | nilai |
| --- | --- |
| `cacah_hidup_byte_kecil` (HIDUP, byte < **97.634**, STRIKT) | **38** |
| `bagian_hidup_byte_kecil` (penyebut 18.087) | **0.0021009564880853653** |
| `cacah_mati_byte_kecil` (MATI, byte < **150.000**, STRIKT) | **2** |
| `bagian_mati_byte_kecil` (penyebut 1.401) | **0.0014275517487508922** |

- **Zona 22.440–97.634 byte berisi 38 baris HIDUP dan NOL baris MATI.** Berkas MATI
  terkecil di seluruh semesta memang 97.634. Di ekor bawah sebaran byte, berkas kecil
  hampir seluruhnya HIDUP — tafsir "kecil = mati" di zona itu **TERBALIK**
  (ADR-A015 kep. 5).
- **Ekor bawah MATI nyaris kosong.** Hanya **2** baris di bawah 150.000, lengkap:
  **LENDUSDT 2020-11 = 97.634** (minimum kelas MATI itu sendiri) dan **FRONTUSDT
  2024-09 = 109.120**. Sebab kekalahan butir 2 R-308 → **KC-49**.
- **Sebaran per kelas IDENTIK dari TIGA modul berbeda** (aturan 36, kini tiga kali):

| kelas | cacah | byte | byte_min | byte_maks | byte_rata |
| --- | --- | --- | --- | --- | --- |
| HIDUP | 18.087 | 32.049.492.952 | **22.440** | 2.770.666 | 1.771.962,899 |
| SEPI | 98 | 77.728.024 | 259.327 | 1.231.408 | 793.143,102 |
| MATI | 1.401 | 579.041.399 | **97.634** | 451.875 | 413.305,781 |

  `cacah_lain` 0 · `byte_lain` 0 · `total_byte` **32.706.262.375**.
- **Sembilan medan selisih semuanya 0 — tetapi hanya DELAPAN di antaranya bebas**
  (`total_byte` turunan). Menyebut "sembilan pemeriksaan bebas" DILARANG
  (ADR-A015 kep. 7, calon KC-50).
- `laporan_hilang` [] · `cacah_laporan_hilang` 0.

**`daftar_mati_kecil` (2, LENGKAP):** LENDUSDT 2020-11 97.634 · FRONTUSDT 2024-09
109.120.

**Sidik kode `irisan_byte` V1 =**
`0e7103ef46a37d1e442d8e7fc5b9771b1ef7cdc3956ea57d584d84f6f73ea2c6`

## BYTE PARQUET ATAS SELURUH SEMESTA [v7, tetap berlaku]

Sumber: `byte_semesta.py` V1 run **30526358811** (commit `d3bc2039`, kode 0), laporan
blob `8b7f2077`. **Total byte parquet = 32.706.262.375** (≈32,7 GB) atas 19.586
simbol-bulan. `bagian_byte_mati` = **0.017704297493883234**;
`cacah_terukur_byte_kecil` (< 10.000) = 0; `cacah_byte_nol` = 0 → **dasar keras ≈22
KB**, sebab langsung KC-48. Bulan MATI bukan bulan KOSONG (`byte_min` 97.634 > 0) —
**APA ISINYA BELUM DIUKUR** dan dilarang ditebak (ADR-A014 kep. 4); pertanyaan ini
kini **tiga giliran berturut** tidak terjawab dan menjadi **prioritas pertama**
(ADR-A016 kep. 7). Adjudikasi R-307: **MELESET**.
Sidik `byte_semesta` V1 =
`e02aca2b3967069b500b01d27a1d2d1553f47b912ea41ddbecd9e4e6c33883c7`

## Arah waktu kematian lawan lubang funding [v6, `lubang_tebing` V1 — tetap]

Run **30524631435** (commit `84b11164`, kode 0), laporan blob `7d8883f5` (terbaca
99%; seluruh `ringkasan` dan `uji_r306` terbaca). Penyebut **118**.

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

**1233** — `reports/ci_terakhir.json` blob
**`0489d71101e451efe73d20fd8fe75ba6d41c5c27`**, run **30532058688**, commit
**`09ce9853`**, 2026-07-30T09:47:29Z, kode 0. Riwayat: 814 → 832 → 879 → 936 → 984 →
1044 → 1100 → 1168 → **1233**. Turunan: 1168 + **65** butir
`test_bulan_pertama.py` = 1233 ✅

Cacat administratif v8 (blob CI tidak dicatat) **LUNAS**: CI 1168 =
`2498e2cf6e6f6c7d0b8807bb5ba923ac1d803b6d`, CI 1233 = `0489d711…`.

**Aturan 57 kembali berjalan: benar 1 dari 1** sesudah PUTUS di 26/27.
Aturan 38 pemakaian ke-**35**.

## Modul, workflow, dan berkas uji [v9]

**UTANG CACAH TANGAN LUNAS LAGI (aturan 66, KC-33).** Pencacahan TANGAN dilakukan
pada ref **`010edff23f7143063fd47a5d3a077ca28c66e859`** — SESUDAH trio
`bulan_pertama` — satu per satu bernomor:

- `lux_ai/serapan/` **47** (`__init__.py` 1 … `bulan_absen.py` 6 ·
  **`bulan_pertama.py` 7** · `bulan_settled.py` 8 … `ukur_baris.py` 47)
- `tests/` **51** (`test_anatomi_tengah.py` 1 … **`test_bulan_pertama.py` 6** …
  `test_ukur_baris.py` 51)
- `.github/workflows/` **42** (`anatomi_tengah.yml` 1 … **`bulan_pertama.yml` 5** ·
  `ci.yml` 8 … `ukur_baris.yml` 42)

Ketiganya COCOK dengan angka turunan v8. Kecocokan itu TIDAK menyahkan kebiasaan
mengutip turunan; turunan benar lagi hanya karena tiap trio menambah tepat satu
berkas per direktori. Angka sesudah trio BERIKUTNYA kembali TURUNAN sampai dicacah.

Blob trio baru:

- `lux_ai/serapan/bulan_pertama.py` V1 blob
  **`b9bd00ac46a2825a8f1b540bbe9207e154f66bf4`** (19.349 B).
- `tests/test_bulan_pertama.py` blob
  **`75d87ba2f9254d362ef36d47637e33bdd2b503b5`** (13.375 B, **65** butir, dicacah
  TANGAN `def test_` satu per satu; daftar bernomor 1–65 utuh di kepala berkas).
- `.github/workflows/bulan_pertama.yml` blob
  **`2242e3e4a819f767c015f87a61bae1f5a2f6e82c`** (`paths` **SATU** entri
  `- 'lux_ai/serapan/bulan_pertama.py'`).

Blob lain identik dengan v8: `irisan_byte.py` `2dbe3d55`, `test_irisan_byte.py`
`b6389051` (68 butir), `irisan_byte.yml` `7d98a267`, `kehidupan.py` `f49abb2b`,
`kehidupan_arsip.py` `318a5cb1`, `silang_funding.py` V2 `42c3aa9d`, `kohort_ekor.py`
`c9b63bbe`, `lubang_awal.py` `8c36943d`, `lubang_tebing.py` `575e777e`,
`lubang_tengah.py` `4d3beaf1`, `sebab_bangkit.py` `fd5a1dc4`, `tersisip_semesta.py`
`8a648838`, `bentangan_kohort.py` V2 `f4eae57a`, `byte_semesta.py` `ff68e4be`,
`funding.py` `8d4b1f82`, `arsip.py` `0104958b`, `gerbang_1m.py` `c8cc54c8`,
`resample.py` `66a4b177`. `ci.yml` = `c79497b2` (paths-ignore
journal/decisions/hipotesis/reports; push ke `lux_ai/**`, `tests/**`, `STATE*`,
`PROMPT*` MENYALAKAN CI). `karantina_semesta.yml` = `de40fa4e` (belum dibaca utuh).

**Pola workflow trio (terbukti lagi pada `bulan_pertama.yml`, dibaca UTUH):** `name`,
`on.push.paths` SATU entri, `permissions: contents: write`, job `ukur` di
`ubuntu-latest`, checkout@v4 + setup-python@v5 (3.11), `pip install numpy pandas
pyarrow pyyaml`, langkah `jalan` id=`jalan` dengan `set +e` → `KODE=$?` →
`echo "kode=$KODE" >> "$GITHUB_OUTPUT"` → `exit 0`, langkah `catat status` (printf
JSON ke `reports/<modul>_status.json`), langkah `dorong laporan` (git config bot,
add, commit `[skip ci]`, pull --rebase, push), langkah akhir
`exit ${{ steps.jalan.outputs.kode }}`.

## API terverifikasi — tambahan v9

API lama (v37–v8) tetap berlaku. Tambahan:

**`bulan_pertama` V1** (blob `b9bd00ac`, dibaca UTUH dari `09ce9853` sesudah push):
mengimpor `kehidupan`, `kehidupan_arsip`, `lubang_awal`, `silang_funding`.
Tetapan: `VERSI=1`, `KELUARAN="reports/bulan_pertama.json"`,
`BATAS_BARIS_LAPORAN=40`, **`AMBANG_HIDUP_KECIL=97634`**, **`BULAN_TEPI="2026-06"`**,
`R309_PITA_BUTIR_1=(22,38)`, `R309_PITA_BUTIR_2=(0.10,0.60)`,
`INVARIAN` **delapan** kunci (penyebut 19586, simbol 787, cacah_hidup 18087,
cacah_sepi 98, cacah_mati 1401, total_byte 32706262375, byte_hidup 32049492952,
cacah_hidup_byte_kecil 38), `MEDAN_SELISIH` **8** (seluruhnya BEBAS),
`KENDALI_DATA` 3 baris BTCUSDT (2021-05 2770666, 2021-08 2730341, 2021-01 2722266),
`DETEKSI_AMBANG=250`, `DETEKSI_PERTAMA=2`, `DETEKSI_HIDUP_KECIL=2`,
`DETEKSI_SEBAGIAN=2`, `DETEKSI_NISBAH=0.75`, `DETEKSI_TOTAL_BYTE=1500`.
Fungsi: `nama_keluaran`, `sidik_kode`, `_bagian`, `kelas_status`,
`peta_bulan_pertama`, `penanda_baris`, `sebaran_per_kelas`, **`total_byte_langsung`**,
`cacah_di_bawah`, `cacah_sebagian`, `daftar_kecil_bertanda`, `nisbah_pertama`
(penyebut kosong → **None**, bukan 0), `selisih_invarian`, `dalam_pita`,
`dalam_pita_pecahan`, `kendali_data`, `kendali_deteksi`, `ringkaskan`, `uji_r309`,
`kode_keluar`, `jalankan(akar=".", total=None)`, `main`.
**Perbaikan yang wajib disebut:** `total_byte` dihitung lewat jalur LANGSUNG, bukan
turunan penjumlahan kelas — kebalikan cacat `irisan_byte` (ADR-A016 kep. 5).

**`irisan_byte` V1** (blob `2dbe3d55`): `AMBANG_HIDUP_KECIL=97634`,
`AMBANG_MATI_KECIL=150000`, `R308_PITA_BUTIR_1=(20,600)`,
`R308_PITA_BUTIR_2=(10,300)`, `INVARIAN` 9 kunci, `MEDAN_SELISIH` **9** (delapan
bebas + satu turunan), `DETEKSI_TOTAL=1922`. Rincian penuh di v8.

**`silang_funding` V2** (blob `42c3aa9d`, 29.873 B): `baca_laporan_kehidupan(akar,
total)` → **TIGA** nilai `(status, byte_parquet, meta)`, kunci tuple
`(simbol, bulan)` — terbukti sekali lagi lewat pemakaian di `bulan_pertama` (KC-43
tetap terjaga); `bulan_per_simbol(status)` → `Dict[str, List[str]]` terurut;
`lubang_funding(funding)` → `(Set[(simbol,bulan)], meta)`; `kendali_silang`;
`kendali_sah`; `bentuk_lubang_lokal`; `baca_medan_baris(akar,total,
medan="cacah_lilin")`; `SUMBER_FUNDING="reports/funding_semesta.json"`,
`KENDALI_CACAH=3`, `PENYEBUT_TERCATAT=19586`, `MATI_TERCATAT=1401`,
`KOHORT_TERCATAT=456`, `HIDUP_TANPA_FUNDING_TERCATAT=33`,
`LUBANG_TAK_DIKENAL_TERCATAT=3`,
`BENTUK_TERBITAN_FUNDING={"awal":48,"ekor":826,"tengah":6}`,
`BERKAS_DICAP=["kehidupan.py","kehidupan_arsip.py","silang_funding.py"]`.

**`byte_semesta` V1** (blob `ff68e4be`): rincian penuh di v7. Tetapan pokok
`R307_PITA_BUTIR_1=(0.02,0.15)`, `R307_AMBANG_BYTE_KECIL=10000`,
`R307_PITA_BUTIR_2_CACAH=(20,400)`, `BATAS_BARIS_LAPORAN=40`, `MEDAN_SELISIH` 9.

**`lubang_awal` V1** (`8c36943d`): `peta_status`, `ringkas`, `himpun`, `bulan_urut`,
`bangkit_lokal`, `kendali_deteksi`, `dalam_pita`, `uji_r305`, `kode_keluar`;
`POLA_BULAN=re.compile(r"^\d{4}-\d{2}$")`; `BATAS_BARIS_LAPORAN=60`. Medan
`mati_tidak_setelah_lubang_bukan_awal` memakai `<=` — **DILARANG dipakai untuk klaim
arah** (aturan 80). Sidik `156499ce…`.
`lubang_tebing` V1 (`575e777e`): rincian di v6; `BATAS_BARIS_LAPORAN=60`.
`kohort_ekor` V4 (`c9b63bbe`): `TEBING="2025-07"`, `BULAN_DIHARAPKAN="2026-06"`,
`BATAS_SIMBOL=10`, `PAGU_MUNDUR=60`, `AMBANG_SEPI=0.5`,
`KENDALI_HIDUP=("BTCUSDT","ETHUSDT")`.
`kehidupan_arsip` (`318a5cb1`): `TOTAL_PECAHAN=8`, `nama_keluaran(i)`.
`kehidupan` (`f49abb2b`): `STATUS_MATI/SEPI/HIDUP/TAK_TERUKUR`,
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
Keempatnya COCOK lagi pada run `bulan_pertama` (aturan 36) → semesta SAMA.

## Hipotesis

- H-A001 belum diuji · H-A002b GUGUR · H-A003 MENANG pada 3, GUGUR pada 9 · H-A004
  tak dapat diuji · H-A005 GUGUR · H-A006 MENANG enam run · H-A008 MENANG dua kali ·
  H-A009 GUGUR · H-A010 MENANG 5–0 · H-A011 MENANG · H-A012 MENANG · H-A013 MENANG
  6–0, TAFSIR DICABUT · H-A014 BENTUK BARU MENANG 9 dari 9 · H-A015 MENANG sebagai
  angka, DIBATASI sebagai tafsir (KC-45) · H-A016 PENGAMATAN, BELUM DIUJI.
- **H-A017** DICABUT sebagai pola semesta (ADR-A011/A012, dilemahkan R-306): bukti
  lepas-tebing tinggal **1** simbol. TIDAK dipulihkan oleh R-307, R-308, maupun
  R-309 — ketiganya tidak menyentuh arah sebab.
- **H-A018 — byte parquet sebagai gejala kehidupan. DIUKUR DUA KALI (R-307, R-308).**
  **Bunyi yang BOLEH dipakai:** "bulan MATI menempati bagian KECIL dari byte semesta
  (**0,0177** dari 32,7 GB) dan rata-rata sekitar **4,3×** lebih kecil daripada bulan
  HIDUP (413.306 lawan 1.771.963 byte)".
  **Bunyi yang DILARANG:** "berkas kecil berarti pasar mati" — di zona 22.440–97.634
  byte ada **38 HIDUP dan 0 MATI**. Besar berkas DILARANG dipakai sebagai detektor
  status ke arah mana pun (ADR-A014 kep. 2, ADR-A015 kep. 5).
- **H-A019 [DIUJI R-309 — DITERIMA TERBATAS oleh ADR-A016 kep. 1].**
  **Rumusan resmi satu-satunya yang boleh dikutip:** *hampir setiap baris HIDUP di
  zona byte kecil adalah bulan pertama simbol itu di dalam penyebut (**37 dari 38**),
  sementara hampir setiap bulan pertama BUKAN berkas kecil (**37 dari 787, ±4,7%**).*
  Ia adalah **irisan asimetris, bukan sebab**, dan bukan detektor ke arah mana pun.
  **Klausa `2026-06` DICABUT** dari rumusan — sumbangan bebasnya NOL (ADR-A016 kep.
  2). Batas tafsir: "bulan pertama" = bulan terkecil DI DALAM penyebut 19.586, bukan
  bulan pertama di bursa (kep. 6). Lawan yang tersisa: **TLMUSDT 2023-03**.
  Catatan asal-usul tetap berlaku: hipotesis ini lahir dari MEMBACA hasil R-308,
  dan karena itu diuji atas semesta penuh dengan pita terkunci lebih dulu — syarat
  ADR-A015 kep. 6 TERPENUHI.
- Hipotesis berikutnya **H-A020**.

## Praregistrasi R-308 — SUDAH TERADJUDIKASI: SEPARUH

Disimpan apa adanya sebagai jejak (aturan 29). Poros H-A018, menyerang IRISAN.

- Butir 1 (BERISIKO): cacah HIDUP ber-byte < 97.634 dari 18.087, pita **20 .. 600**
  → terukur **38** → **MENANG**.
- Butir 2 (BERISIKO): cacah MATI ber-byte < 150.000 dari 1.401, pita **10 .. 300**
  → terukur **2** → **KALAH** (KC-49).
- Butir 3 (MUDAH): invarian nol + dua kendali sah + kode 0 + CI diukur → **MENANG**.

## Praregistrasi R-309 — SUDAH TERADJUDIKASI: TEPAT

Disimpan apa adanya sebagai jejak (aturan 29); teks di bawah disalin dari jurnal 129
§10 dan TIDAK diubah sesudah pengukuran. Poros **H-A019**. Aritmetika implikasi
dihitung lebih dulu (KC-49, kini **aturan 83**), dan pita disusun agar KEDUA arah
dapat kalah.

- **Butir 1 (BERISIKO).** Dari 38 baris HIDUP ber-byte < 97.634, cacah yang merupakan
  bulan PERTAMA simbol ATAU bulan `2026-06`. Penyebut **38**. Pita **22 .. 38**.
  Penyebut 0 → TIDAK TERADJUDIKASI (aturan 41). → terukur **37** → **MENANG**.
- **Butir 2 (BERISIKO).** Nisbah rata byte bulan PERTAMA simbol terhadap rata byte
  bulan BUKAN-pertama, atas seluruh 19.586 baris. Pita **0.10 .. 0.60**. → terukur
  **0,527179** → **MENANG** (tipis ke tepi atas — jangan dibaca sebagai konfirmasi
  kuat).
- **Butir 3 (MUDAH).** Invarian penyebut/simbol/kelas nol, kedua kendali sah, kode
  keluar 0, CI diukur. Cacah invarian BEBAS disebut apa adanya: **delapan, seluruhnya
  bebas**. → **MENANG**.

**Cacat praregistrasi yang ditemukan SESUDAH menang:** butir 1 memakai klausa ATAU
yang salah satu cabangnya menyumbang NOL secara bebas — dasar **usulan aturan 84**.

## Praregistrasi R-310 — BELUM ADA

Poros belum ditetapkan. Arah yang direkomendasikan ADR-A016 kep. 7: **APA ISI berkas
bulan MATI** — belum diukur, DILARANG ditebak. Sebelum pita dikunci, **aturan 83
(kini RESMI) WAJIB dipenuhi**: tulis aritmetika implikasi di jurnal lebih dulu; bila
jawabannya sudah tertentu dalam satu angka signifikan, pindahkan poros butir itu.
Usulan **aturan 84** wajib diperhatikan bila ada butir berklausa ATAU. Nama modul
R-310 WAJIB dicek lewat pencacahan direktori lebih dulu (aturan 66); laporan WAJIB
ringkas (`BATAS_BARIS_LAPORAN`).
