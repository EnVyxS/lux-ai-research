# STATE lampiran UKUR — bagian 3 dari STATE (v8, milik STATE v48)

**Kedudukan berkas ini.** STATE dipecah tiga sejak v43 (KC-42). Pembagian berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, KC-1..KC-49.
2. **`STATE_LAMPIRAN_EKOR.md`** v8 — bagian 2: papan skor, ADR, catatan kejujuran.
3. **`STATE_LAMPIRAN_UKUR.md`** (berkas ini, v8) — bagian 3: pengukuran, modul,
   workflow, uji, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip lama; bukan sumber lagi.

Dasar v8: UKUR v7 (blob **`4e7fb65be81bc5657da94060447075f0f1e2d73c`** — empat puluh
karakter penuh, akhirnya tercatat; sampai v7 hanya bentuk pendek `4e7fb65b` yang
diketahui dan itu diakui tersurat), dibaca UTUH sebelum berkas ini ditulis. Yang
ditambahkan v8: **lebar zona irisan byte** (pengukuran pertama); API `irisan_byte` V1;
CI 1168; adjudikasi R-308 SEPARUH; cacah tangan tiga direktori LUNAS; H-A019
didaftarkan; praregistrasi **R-309**.

**PERINGATAN KESERASIAN VERSI — dorongan BERTAHAP.** Saat berkas ini didorong,
`STATE_LAMPIRAN_EKOR.md` sudah **v8** (commit `ea141915`, blob
`c34c88e27dce4813622c2e3ea71bf4d486ec65d6`) tetapi `STATE.md` masih **v47** (blob
`7642b75d0ba7cd8612d83c3a43bff1274d8cac57`), sehingga **KC-49** dan **usulan aturan
83** belum tercantum di bagian 1. Sumber sah keduanya sampai `STATE.md` v48 naik:
`journal/2026-07-30-129.md` §6 (blob `ecb6ac241d84f06767195f931f8418fa1c853ba2`) dan
`decisions/ADR-A015.md` (blob `387d551051da4f0d539f7c9c26e438a9ac84c9a3`). Pemecahan
ini SENGAJA: menulis tiga berkas besar dari satu konteks terpakai adalah cara paling
pasti merusak aturan 1–81 (KC-42, KC-43).

**Angka yang TIDAK berubah dari v44/v45/v6/v7** (tidak diulang): taksonomi 9 kelas,
karantina 12, bulan ABSEN 11, H-A013..H-A015, terhenti, SETTLED. Rinciannya di v44
(blob `d302caff`), v45 (`eb826817`), v6 (`27e59a79`), v7 (`4e7fb65b…`).

## KOREKSI KC-41 — BACA SEBELUM MENGUTIP BERKAS INI

Kedua koreksi di bawah LAHIR di v6 dan **tetap dicantumkan** karena keduanya soal
dokumen kami sendiri, bukan soal data — menghapusnya berarti menghapus jejak cacat.

**Koreksi 1 (kesalahan berkas ini pada v5).** UKUR v5 menulis bahwa
`.github/workflows/lubang_awal.yml` ber-`paths` pada tiga entri. **ITU SALAH.** Berkas
asli (blob **`3134bc9f6f91c83ed39ff8424506ac253317edee`**) memuat **SATU** entri:

```
paths:
  - 'lux_ai/serapan/lubang_awal.py'
```

Aturan yang diperkuat: bila bagian STATE bertentangan, **berkas sumber menang**.
`lubang_tebing.yml` (`c8ae552a`), `byte_semesta.yml` (`45650ff9`), dan
`irisan_byte.yml` (`7d98a267`) meniru berkas ASLI ini, bukan rumusan v5.

**Koreksi 2 (kesalahan PROMPT v49).** PROMPT v49 menyebut poros R-307 "H-A017";
yang benar **H-A018**. PROMPT v50 sudah memuat koreksi — **utang koreksi LUNAS**.

## Semesta riset = `perpetual_usdt` = penyebut 787 — tidak berubah

- `cacah_perpetual_usdt` **787** = `cacah_penyebut_simbol` **787**
- `cacah_perpetual_usdt_luar_penyebut` 0, `cacah_penyebut_bukan_perpetual_usdt` 0
- Batas wajib disebut: token saham/ETF/komoditas ikut di dalam 787.

## KC-18 — semesta kehidupan (dikonfirmasi ulang oleh R-307 DAN R-308)

Atas **19.586** simbol-bulan lolos: **1.401 MATI** (7,153%), **98 SEPI**, **18.087
HIDUP**. Dari 1.401 MATI: 842 kehilangan funding, 559 tetap berfunding.
`cacah_simbol_tanpa_hidup` **18**.

`cacah_lain` = 0 pada kedua modul → seluruh 19.586 berstatus MATI/SEPI/HIDUP, tidak
ada TAK_TERUKUR. 18.087 + 98 = 18.185 TERUKUR, + 1.401 = 19.586 ✅

## Lubang funding — agregat semesta (tetap)

- `cacah_simbol_ada_lubang` = **122** (dari 787) · awal **5** · bukan-awal **118**
- BNXUSDT punya lubang AWAL dan bukan-awal sekaligus.
- Lima bentuk AWAL: BNXUSDT, ICPUSDT, JUPUSDT, QTUMUSDT, TLMUSDT. ICP dan TLM lubang
  awalnya melewati kematian (sumber salah-baca R-304, KC-46).
- Lubang funding **880** semesta / **877** dalam penyebut / 3 tak dikenal. Irisan
  880 lawan 877 BELUM diukur.

## LEBAR ZONA IRISAN BYTE [BARU v8 — pengukuran PERTAMA]

Sumber: `irisan_byte.py` V1 run **30529294165** (commit `d22364b9`, kode 0). Laporan
`reports/irisan_byte.json` blob **`4c13bf6afc36c9afbeb1c662d6098258a6b750dd`**
(terbaca **UTUH** — `BATAS_BARIS_LAPORAN=40` berhasil untuk kedua kalinya berturut),
`_status.json` blob **`863dc4cb266b2fcee56fb733960722d37bd931e7`**.

**Pertanyaan yang dijawab:** seberapa lebar zona tempat bulan HIDUP lebih kecil
daripada bulan MATI terkecil. Ambang kedua butir RELATIF terhadap sebaran yang sudah
terukur di R-307, sehingga KC-48 dijawab langsung.

| besaran | nilai |
| --- | --- |
| `cacah_hidup_byte_kecil` (HIDUP, byte < **97.634**, STRIKT) | **38** |
| `bagian_hidup_byte_kecil` (penyebut 18.087) | **0.0021009564880853653** |
| `cacah_mati_byte_kecil` (MATI, byte < **150.000**, STRIKT) | **2** |
| `bagian_mati_byte_kecil` (penyebut 1.401) | **0.0014275517487508922** |

- **Zona 22.440–97.634 byte berisi 38 baris HIDUP dan NOL baris MATI.** Itu bukan
  akibat definisi: berkas MATI terkecil di seluruh semesta memang 97.634. Maka di
  ekor bawah sebaran byte, berkas kecil hampir seluruhnya HIDUP — tafsir "kecil =
  mati" di zona itu **TERBALIK** (ADR-A015 kep. 5).
- **Ekor bawah MATI nyaris kosong.** Hanya **2** baris di bawah 150.000, dan inilah
  keduanya, lengkap: **LENDUSDT 2020-11 = 97.634** (minimum kelas MATI itu sendiri)
  dan **FRONTUSDT 2024-09 = 109.120**. Sebab kekalahan butir 2 R-308 → **KC-49**.
- **Sebaran per kelas IDENTIK dengan R-307 dari modul berbeda** (saling menguatkan,
  aturan 36):

| kelas | cacah | byte | byte_min | byte_maks | byte_rata |
| --- | --- | --- | --- | --- | --- |
| HIDUP | 18.087 | 32.049.492.952 | **22.440** | 2.770.666 | 1.771.962,899 |
| SEPI | 98 | 77.728.024 | 259.327 | 1.231.408 | 793.143,102 |
| MATI | 1.401 | 579.041.399 | **97.634** | 451.875 | 413.305,781 |

  `cacah_lain` 0 · `byte_lain` 0 · `total_byte` **32.706.262.375**.
- **Sembilan medan selisih semuanya 0 — tetapi hanya DELAPAN di antaranya bebas.**
  Di `ringkaskan`, `total_byte` dihitung sebagai jumlah byte keempat kelas, sehingga
  `selisih_total_byte` tersirat secara aritmetis dari tiga selisih byte lain. Cacat
  ini diakui SEBELUM hasil keluar; menyebut "sembilan pemeriksaan bebas" DILARANG
  (ADR-A015 kep. 7, calon KC-50).
- **Kendali dua lapis sah.** Data (`kendali_data_sah` true): tiga simbol-bulan
  berparquet terbesar seluruhnya **BTCUSDT** — 2021-05 2.770.666, 2021-08 2.730.341,
  2021-01 2.722.266 — semuanya HIDUP. Detektor (`kendali_deteksi_sah` true): bentangan
  buatan berambang 50 → `hidup_kecil` **2** (harap 2), `mati_kecil` **1** (harap 1),
  `total` **1922**; baris tepat DI AMBANG tidak terhitung (perbandingan strikt).
- `laporan_hilang` [] · `cacah_laporan_hilang` 0.
- **Adjudikasi R-308:** butir 1 **MENANG** (38 dalam 20..600), butir 2 **KALAH**
  (2 lawan 10..300), butir 3 **MENANG** (MUDAH) → **SEPARUH**. Bacaan jujurnya di
  EKOR v8 § Catatan kejujuran.

**`daftar_mati_kecil` (2, LENGKAP):** LENDUSDT 2020-11 97.634 · FRONTUSDT 2024-09
109.120.

**`daftar_hidup_kecil` (38, LENGKAP, urut byte menaik):** JUPUSDT 2024-01 22.440 ·
TIAUSDT 2023-10 24.551 · REZUSDT 2024-04 32.164 · SLPUSDT 2023-10 33.257 ·
PORTALUSDT 2024-02 34.175 · NAORISUSDT 2025-07 34.673 · TROYUSDT 2024-10 35.511 ·
MDTUSDT 2023-06 36.580 · COSUSDT 2024-09 36.742 · GUNUSDT 2025-03 36.768 · CCUSDT
2025-10 37.116 · MAGMAUSDT 2025-12 37.327 · COLLECTUSDT 2025-12 38.486 · CKBUSDT
2023-02 39.079 · EDUUSDT 2023-04 39.749 · AIOTUSDT 2025-04 41.514 · PUNDIXUSDT
2025-04 42.561 · ADAUSDT 2020-01 42.678 · VFYUSDT 2025-09 44.460 · PLAYUSDT 2025-07
44.508 · COMPUSDT 2020-06 44.898 · MLNUSDT 2025-03 45.246 · EDENUSDT 2025-09 45.883 ·
RLCUSDT 2020-07 46.447 · FUNUSDT 2025-03 47.831 · MTLUSDT 2021-03 51.322 · YFIUSDT
2020-08 54.929 · ATAUSDT 2021-08 58.161 · ENSUSDT 2021-11 62.845 · ROSEUSDT 2021-12
63.592 · SQQQUSDT 2026-06 72.819 · TLMUSDT 2023-03 80.394 · AMBUSDT 2023-03 81.419 ·
TQQQUSDT 2026-06 82.330 · MVLLUSDT 2026-06 86.126 · LEVERUSDT 2023-03 89.724 ·
INXUSDT 2026-01 94.575 · ENJUSDT 2020-09 94.658.

**Sidik kode `irisan_byte` V1 =**
`0e7103ef46a37d1e442d8e7fc5b9771b1ef7cdc3956ea57d584d84f6f73ea2c6`

## BYTE PARQUET ATAS SELURUH SEMESTA [v7, tetap berlaku]

Sumber: `byte_semesta.py` V1 run **30526358811** (commit `d3bc2039`, kode 0), laporan
blob `8b7f2077`. **Total byte parquet = 32.706.262.375** (≈32,7 GB) atas 19.586
simbol-bulan. `bagian_byte_mati` = **0.017704297493883234**;
`cacah_terukur_byte_kecil` (< 10.000) = 0; `cacah_byte_nol` = 0 → **dasar keras ≈22
KB**, sebab langsung KC-48. Bulan MATI bukan bulan KOSONG (`byte_min` 97.634 > 0) —
**APA ISINYA BELUM DIUKUR** dan dilarang ditebak (ADR-A014 kep. 4); pertanyaan ini
kini sudah dua giliran berturut tidak terjawab dan naik prioritas. Adjudikasi R-307:
**MELESET** (butir 1 kalah tipis, butir 2 ambang mustahil, butir 3 menang).
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

**1168** (run **30529294152**, commit **`d22364b9`**, kode 0, 2026-07-30T09:05:52Z).
Riwayat: 814 → 832 → 879 → 936 → 984 → 1044 → 1100 → **1168**. Turunan: 1100 + **68**
butir `test_irisan_byte.py` = 1168 ✅ Blob `reports/ci_terakhir.json` untuk angka ini
**TIDAK dicatat** saat dibaca — cacat administratif yang diakui; jangan mengarang,
baca ulang dari main bila perlu.

**Aturan 57 PUTUS: 26 dari 27** (ramalan 67/1167 lawan kenyataan 68/1168; sebabnya
satu butir tercecer dari DAFTAR, bukan dari kode). Hitungan beruntun mulai dari nol.
Aturan 38 pemakaian ke-**33**.

## Modul, workflow, dan berkas uji [v8]

**UTANG CACAH TANGAN LUNAS (aturan 66, KC-33).** Pencacahan TANGAN dilakukan pada ref
**`5a777664`** — yaitu SESUDAH trio `byte_semesta` dan SEBELUM trio `irisan_byte` —
satu per satu bernomor: `lux_ai/serapan/` **45**, `tests/` **49**,
`.github/workflows/` **40**. Ketiganya COCOK dengan angka turunan v7. Kecocokan itu
TIDAK menyahkan kebiasaan mengutip turunan; turunan benar kali ini hanya karena tiap
trio menambah tepat satu berkas per direktori.

Angka SESUDAH trio `irisan_byte` di bawah ini **turunan, belum dicacah tangan**:

- **`lux_ai/serapan/` — 46 (turunan)** = 45 tangan + `irisan_byte.py` V1 blob
  **`2dbe3d5505ac8188a9e212d73db0ce8ba0b2782f`**.
- **`tests/` — 50 (turunan)** = 49 tangan + `test_irisan_byte.py` blob
  **`b6389051ccd01150f4e61d0200567895a7cc1534`** (**68** butir, dicacah TANGAN
  `def test_` satu per satu pada berkas yang sudah di main; cacat kecil tanpa akibat:
  `import pytest` tidak terpakai).
- **`.github/workflows/` — 41 (turunan)** = 40 tangan + `irisan_byte.yml` blob
  **`7d98a267d48282bf6001e1c60a8dc50025751a4b`** (`paths` **SATU** entri
  `- 'lux_ai/serapan/irisan_byte.py'`).

Blob lain identik dengan v7: `kehidupan.py` `f49abb2b`, `kehidupan_arsip.py`
`318a5cb1`, `silang_funding.py` V2 `42c3aa9d`, `kohort_ekor.py` `c9b63bbe`,
`lubang_awal.py` `8c36943d`, `lubang_tebing.py` `575e777e`, `lubang_tengah.py`
`4d3beaf1`, `sebab_bangkit.py` `fd5a1dc4`, `tersisip_semesta.py` `8a648838`,
`bentangan_kohort.py` V2 `f4eae57a`, `byte_semesta.py` `ff68e4be`, `funding.py`
`8d4b1f82`, `arsip.py` `0104958b`, `gerbang_1m.py` `c8cc54c8`, `resample.py`
`66a4b177`. `ci.yml` = `c79497b2` (paths-ignore journal/decisions/hipotesis/reports;
push ke `lux_ai/**`, `tests/**`, `STATE*`, `PROMPT*` MENYALAKAN CI).
`karantina_semesta.yml` = `de40fa4e` (belum dibaca utuh).

**Pola workflow trio (terbukti pada `irisan_byte.yml`, dibaca UTUH):** `name`,
`on.push.paths` SATU entri, `permissions: contents: write`, job `ukur` di
`ubuntu-latest`, checkout@v4 + setup-python@v5 (3.11), `pip install numpy pandas
pyarrow pyyaml`, langkah `jalan` id=`jalan` dengan `set +e` → `KODE=$?` →
`echo "kode=$KODE" >> "$GITHUB_OUTPUT"` → `exit 0`, langkah `catat status` (printf
JSON ke `reports/<modul>_status.json`), langkah `dorong laporan` (git config bot,
add, commit `[skip ci]`, pull --rebase, push), langkah akhir
`exit ${{ steps.jalan.outputs.kode }}`.

## API terverifikasi — tambahan v8

API lama (v37–v7) tetap berlaku. Tambahan:

**`irisan_byte` V1** (blob `2dbe3d55`, dibaca UTUH dari `d22364b9` sesudah push):
mengimpor `kehidupan`, `kehidupan_arsip`, `lubang_awal`, `silang_funding`.
Tetapan: `VERSI=1`, `KELUARAN="reports/irisan_byte.json"`, `BATAS_BARIS_LAPORAN=40`,
`KELAS_HIDUP="HIDUP"`, `KELAS_SEPI="SEPI"`, `KELAS_MATI="MATI"`, `KELAS_LAIN="LAIN"`,
`KELAS_URUT=("HIDUP","SEPI","MATI")`, **`AMBANG_HIDUP_KECIL=97634`**,
**`AMBANG_MATI_KECIL=150000`**, `R308_PITA_BUTIR_1=(20,600)`,
`R308_PITA_BUTIR_2=(10,300)`, `PENYEBUT_HIDUP_TERCATAT=18087`,
`PENYEBUT_MATI_TERCATAT=1401`, `INVARIAN` **9** kunci (19586, 787, 18087, 98, 1401,
32706262375, 32049492952, 77728024, 579041399), `MEDAN_SELISIH` **9**,
`KENDALI_DATA` 3 baris BTCUSDT, `DETEKSI_HIDUP=(5,10,1000)`, `DETEKSI_MATI=(7,900)`,
`DETEKSI_TOTAL=1922`.
Fungsi: `nama_keluaran`, `sidik_kode`, `_bagian` (penyebut 0 → None), `kelas_status`,
`sebaran_per_kelas`, `cacah_di_bawah(status, byte_parquet, kelas, ambang)`
(perbandingan **strikt** `<`), `daftar_kecil`, `kendali_data(byte_parquet,
status=None, harapan=None)`, `kendali_deteksi(ambang=50)`, `selisih_invarian`,
`dalam_pita`, `ringkaskan`, `uji_r308`, `kode_keluar`, `jalankan(akar=".",
total=None)`, `main`.
**Cacat yang wajib disebut:** `ringkaskan` menghitung `total_byte` dari jumlah byte
per kelas, sehingga `selisih_total_byte` adalah TURUNAN — sembilan medan selisih =
delapan bebas + satu turunan.

**`silang_funding` V2** (blob `42c3aa9d`, 29.873 B): `baca_laporan_kehidupan(akar,
total)` → **TIGA** nilai `(status, byte_parquet, meta)` — terbukti sekali lagi lewat
pemakaian di `irisan_byte` (KC-43 tetap terjaga); `lubang_funding(funding)` →
`(Set[(simbol,bulan)], meta)`; `kendali_silang`; `kendali_sah`; `bentuk_lubang_lokal`;
`baca_medan_baris(akar,total,medan="cacah_lilin")`;
`SUMBER_FUNDING="reports/funding_semesta.json"`, `KENDALI_CACAH=3`,
`BENTUK_TERBITAN_FUNDING={"awal":48,"ekor":826,"tengah":6}`.

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
`BATAS_SIMBOL=10`, `PAGU_MUNDUR=60`, `AMBANG_SEPI=0.5`.
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
Keempatnya COCOK lagi pada run `irisan_byte` (aturan 36) → semesta SAMA.

## Hipotesis

- H-A001 belum diuji · H-A002b GUGUR · H-A003 MENANG pada 3, GUGUR pada 9 · H-A004
  tak dapat diuji · H-A005 GUGUR · H-A006 MENANG enam run · H-A008 MENANG dua kali ·
  H-A009 GUGUR · H-A010 MENANG 5–0 · H-A011 MENANG · H-A012 MENANG · H-A013 MENANG
  6–0, TAFSIR DICABUT · H-A014 BENTUK BARU MENANG 9 dari 9 · H-A015 MENANG sebagai
  angka, DIBATASI sebagai tafsir (KC-45) · H-A016 PENGAMATAN, BELUM DIUJI.
- **H-A017** DICABUT sebagai pola semesta (ADR-A011/A012, dilemahkan R-306): bukti
  lepas-tebing tinggal **1** simbol. TIDAK dipulihkan oleh R-307 maupun R-308 —
  keduanya tidak menyentuh arah sebab.
- **H-A018 — byte parquet sebagai gejala kehidupan. DIUKUR DUA KALI (R-307, R-308).**
  **Bunyi yang BOLEH dipakai:** "bulan MATI menempati bagian KECIL dari byte semesta
  (**0,0177** dari 32,7 GB) dan rata-rata sekitar **4,3×** lebih kecil daripada bulan
  HIDUP (413.306 lawan 1.771.963 byte)".
  **Bunyi yang DILARANG:** "berkas kecil berarti pasar mati" — dan sesudah R-308
  larangan itu bukan lagi soal kehati-hatian melainkan soal fakta: di zona
  22.440–97.634 byte ada **38 HIDUP dan 0 MATI**. Besar berkas DILARANG dipakai
  sebagai detektor status ke arah mana pun (ADR-A014 kep. 2, ADR-A015 kep. 5).
- **H-A019 [BARU v8, DIDAFTARKAN, BELUM DIUJI] — byte kecil menandai BULAN SEBAGIAN,
  bukan kematian.** Bunyi: simbol-bulan ber-byte kecil sebagian besar adalah bulan
  PERTAMA pencatatan sebuah simbol atau bulan tepi jendela (`BULAN_AKHIR` = 2026-06),
  yaitu bulan yang tidak terisi penuh. Asal: daftar 38 HIDUP-kecil didominasi
  JUPUSDT 2024-01, TIAUSDT 2023-10, REZUSDT 2024-04, PORTALUSDT 2024-02, NAORISUSDT
  2025-07, ADAUSDT 2020-01, COMPUSDT 2020-06, RLCUSDT 2020-07, YFIUSDT 2020-08, serta
  SQQQUSDT/TQQQUSDT/MVLLUSDT yang ketiganya 2026-06. Yang MELAWAN dan wajib disebut:
  MTLUSDT 2021-03, ENJUSDT 2020-09, SLPUSDT 2023-10, TLMUSDT 2023-03 tampak bulan
  tengah. **Catatan kejujuran:** hipotesis ini lahir dari MEMBACA hasil R-308, jadi ia
  wajib diuji atas semesta penuh dengan pita terkunci lebih dulu, dan DILARANG
  diklaim menang dari 38 baris yang melahirkannya (ADR-A015 kep. 6).
- Hipotesis berikutnya **H-A020**.

## Praregistrasi R-308 — SUDAH TERADJUDIKASI: SEPARUH

Disimpan apa adanya sebagai jejak (aturan 29). Poros H-A018, menyerang IRISAN.

- Butir 1 (BERISIKO): cacah HIDUP ber-byte < 97.634 dari 18.087, pita **20 .. 600**
  → terukur **38** → **MENANG**.
- Butir 2 (BERISIKO): cacah MATI ber-byte < 150.000 dari 1.401, pita **10 .. 300**
  → terukur **2** → **KALAH** (di bawah tepi bawah; hasilnya sudah tersirat oleh rata
  413.306 lawan maks 451.875 — **KC-49**).
- Butir 3 (MUDAH): invarian nol + dua kendali sah + kode 0 + CI diukur → **MENANG**.

## Praregistrasi R-309 — DISALIN APA ADANYA dari jurnal 129 §10 (JANGAN DIUBAH)

Poros **H-A019**. Sebelum mengunci pita, aritmetika implikasi dihitung lebih dulu
(KC-49, usulan aturan 83): dari 38 baris yang terlihat, sekitar dua pertiga sampai
seluruhnya tampak bulan pertama atau bulan tepi; sisanya (MTLUSDT 2021-03, ENJUSDT
2020-09, SLPUSDT 2023-10, TLMUSDT 2023-03) tampak bulan tengah. Pita disusun agar
KEDUA arah dapat kalah.

- **Butir 1 (BERISIKO).** Dari 38 baris HIDUP ber-byte < 97.634, cacah yang merupakan
  bulan PERTAMA simbol ATAU bulan `2026-06`. Penyebut **38**. Pita **22 .. 38**.
  Penyebut 0 → TIDAK TERADJUDIKASI (aturan 41).
- **Butir 2 (BERISIKO).** Nisbah rata byte bulan PERTAMA simbol terhadap rata byte
  bulan BUKAN-pertama, atas seluruh 19.586 baris. Pita **0.10 .. 0.60**.
- **Butir 3 (MUDAH).** Invarian penyebut/simbol/kelas nol, kedua kendali sah, kode
  keluar 0, CI diukur. Cacah invarian BEBAS harus disebut apa adanya — bila ada medan
  turunan, sebut turunan.

Sumber byte tetap `silang_funding.baca_laporan_kehidupan` (TIGA nilai). Nama modul
R-309 WAJIB dicek lewat pencacahan direktori lebih dulu (aturan 66). Laporan WAJIB
ringkas (`BATAS_BARIS_LAPORAN`).
