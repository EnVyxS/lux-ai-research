# STATE lampiran UKUR — bagian 3 dari STATE v46 (v6)

**Kedudukan berkas ini.** STATE dipecah tiga sejak v43 (KC-42). Pembagian berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, KC-1..KC-47.
2. **`STATE_LAMPIRAN_EKOR.md`** — bagian 2: papan skor, ADR, catatan kejujuran.
3. **`STATE_LAMPIRAN_UKUR.md`** (berkas ini, v6) — bagian 3: pengukuran, modul,
   workflow, uji, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip lama; bukan sumber lagi.

Dasar v6: UKUR v5 (blob **`eb8268176d573d88ee48193e9b57338a6aaa7153`**), dibaca UTUH
sebelum berkas ini ditulis. Yang ditambahkan v6: trio `lubang_tebing` V1; sebaran
arah 40/78/0; tebing 39; CI 1044; cacah direktori 44/39/48; **dua koreksi KC-41**;
hipotesis **H-A018**.

**Angka yang TIDAK berubah dari v44/v45** (tidak diulang): taksonomi 9 kelas,
karantina 12, bulan ABSEN 11, H-A013..H-A015, terhenti, SETTLED. Rinciannya di v44
(blob `d302caff`) dan v45 (blob `eb826817`).

## KOREKSI KC-41 — BACA SEBELUM MENGUTIP BERKAS INI

**Koreksi 1 (kesalahan berkas ini pada v5).** UKUR v5 menulis bahwa
`.github/workflows/lubang_awal.yml` ber-`paths` pada `lux_ai/serapan/lubang_awal.py`,
`tests/test_lubang_awal.py`, **dan workflow sendiri**. **ITU SALAH.** Berkas asli
(blob **`3134bc9f6f91c83ed39ff8424506ac253317edee`**, dibaca UTUH) memuat **SATU**
entri `paths`:

```
paths:
  - 'lux_ai/serapan/lubang_awal.py'
```

`STATE.md` v45 menulisnya benar ("sempit pada modulnya"), jadi dua bagian STATE
saling bertentangan selama satu versi. Aturan yang diperkuat: bila bagian STATE
bertentangan, **berkas sumber menang**. `lubang_tebing.yml` (blob `c8ae552a`) sengaja
meniru berkas ASLI ini, bukan rumusan v5.

**Koreksi 2 (kesalahan PROMPT v49).** PROMPT v49 (blob `4dca042c`) menyebut poros
R-307 sebagai "H-A017 byte parquet". **ITU SALAH LABEL.** H-A017 adalah hipotesis
arah sebab (LITUSDT) — lihat § Hipotesis. Byte parquet hanya PENGAMATAN di ekor
H-A017 dan kini dinaikkan menjadi hipotesis tersendiri **H-A018**. **Pita
praregistrasi R-307 TIDAK diubah** (aturan 29 utuh); hanya labelnya dikoreksi.
PROMPT v50 wajib memuat koreksi ini.

## Semesta riset = `perpetual_usdt` = penyebut 787 — tidak berubah

- `cacah_perpetual_usdt` **787** = `cacah_penyebut_simbol` **787**
- `cacah_perpetual_usdt_luar_penyebut` 0, `cacah_penyebut_bukan_perpetual_usdt` 0
- Batas wajib disebut: token saham/ETF/komoditas ikut di dalam 787.

## KC-18 — semesta kehidupan (tidak berubah)

Atas **19.586** simbol-bulan lolos: **1.401 MATI** (7,153%), **98 SEPI**, **18.087
HIDUP**. Dari 1.401 MATI: 842 kehilangan funding, 559 tetap berfunding.
`cacah_simbol_tanpa_hidup` **18**.

## Lubang funding — agregat semesta (tetap dari v5)

Sumber: `lubang_awal.py` V1 run 30522785043 (commit `d304d3eb`, kode 0).

- `cacah_simbol_ada_lubang` = **122** (dari 787)
- `cacah_simbol_lubang_awal` = **5** · `cacah_simbol_lubang_bukan_awal` = **118**
- BNXUSDT punya lubang AWAL dan bukan-awal sekaligus.
- Lima bentuk AWAL: BNXUSDT, ICPUSDT, JUPUSDT, QTUMUSDT, TLMUSDT. Tiga (BNX, JUP,
  QTUM) `lubang_awal_berakhir_sebelum_mati` true; dua (ICP, TLM) false — lubang AWAL
  melewati kematian (sumber salah-baca R-304, KC-46).
- Lubang funding **880** semesta / **877** dalam penyebut / 3 tak dikenal. Irisan
  880 lawan 877 BELUM diukur.

## Arah waktu kematian lawan lubang funding [v6, `lubang_tebing` V1]

Sumber: `lubang_tebing.py` V1 run **30524631435** (commit `84b11164`, kode 0,
2026-07-30T07:56:06Z). Laporan `reports/lubang_tebing.json` blob **`7d8883f5`**
(terbaca 99%; seluruh `ringkasan` dan `uji_r306` terbaca), `_status.json` blob
**`685191e1`** (`kode_keluar` 0).

Penyebut = **118** simbol berlubang bukan-awal (`penyebut_butir_1` =
`penyebut_butir_2` = 118).

| kelas arah (perbandingan STRIKT, aturan 80) | cacah | bagian |
| --- | --- | --- |
| `mati_dulu` — MATI pertama **<** lubang bukan-awal pertama | **40** | **0.339** |
| `serempak` — bulan SAMA (DILARANG di numerator) | **78** | 0.661 |
| `lubang_dulu` — MATI pertama **>** lubang pertama | **0** | 0.000 |

- `cacah_tebing_butir_2` = **39**, `bagian_tebing_butir_2` = **0.3305** (simbol
  dengan `bulan_lubang_bukan_awal_pertama` == `kohort_ekor.TEBING` == `2025-07`).
- **39 dari 40** anggota `mati_dulu` ada di tebing (0.975). Satu-satunya bukan-tebing:
  **BTCSTUSDT** (lubang 2022-01, MATI 2021-04, `cacah_mati` 63). → KC-47, aturan 81.
- Sembilan selisih invarian = **0** (19.586 / 787 / 1.401 / 8 / 877 / 880 / 122 / 5 /
  118). `sidik_seragam` true. `cacah_laporan_dibaca` 8 = `total_pecahan` 8.
  `cacah_kunci_ganda` 0, `cacah_lubang_ganda` 0, `laporan_hilang` [].
- Cacah baris dilapor: `mati_dulu` 40, tebing 39, `lubang_dulu` 0,
  penyebut_butir_1 **60** (kena `BATAS_BARIS_LAPORAN` = 60 — daftar TIDAK lengkap,
  aturan 62/KC-24: jangan mengambil daftar penuh dari medan ini).
- **Kendali dua lapis sah:** `kendali_sah` true (data) DAN `kendali_deteksi_sah` true.
  Empat bentangan buatan terpisah benar: KENDALI_MATI_DULU → `mati_dulu`,
  KENDALI_SEREMPAK → `serempak`, KENDALI_LUBANG_DULU → `lubang_dulu`, KENDALI_TEBING
  → `serempak` + `di_tebing` true. Karena itu `lubang_dulu` = 0 sah disebut TERUKUR.
- **Adjudikasi R-306:** butir 1 MENANG (0.339 dalam 0.25..0.60, penyebut 118 ≥ 100),
  butir 2 MENANG (39 dalam 20..90), butir 3 MENANG → **TEPAT 3/3**. Bacaan jujurnya
  di EKOR v6 § Catatan kejujuran: kemenangan sah, klaim ilmiah hampir kosong.

**Sidik kode `lubang_tebing` V1 =**
`4a5c2e4279eb1554dc119b48d6a8db61f6ea4ee11b7539efd70ee71d1ae18bf3`

## Jumlah uji — terukur

**1044** (run 30524631516, commit `84b11164`, kode 0, 2026-07-30T07:56:28Z, blob
`0c104b18`). Riwayat: 814 → 832 → 879 → 936 → 984 → **1044**. Turunan: 984 + 60
`test_lubang_tebing.py` = 1044 ✅

## Modul, workflow, dan berkas uji [v6]

**`lux_ai/serapan/` — 44 berkas** (v5: 43 + `lubang_tebing.py`). Blob baru:
`lubang_tebing.py` V1 **`575e777e5b97479a836a6864410da83941138d32`**. Blob lain
identik dengan v5: `kehidupan.py` `f49abb2b`, `kehidupan_arsip.py` `318a5cb1`,
`silang_funding.py` V2 `42c3aa9d`, `kohort_ekor.py` `c9b63bbe`, `lubang_awal.py`
`8c36943d`, `lubang_tengah.py` **`4d3beaf1`** (23.745 B — SUDAH ADA sejak lama;
sebab nama R-306 dipindah ke `lubang_tebing`), `sebab_bangkit.py` `fd5a1dc4`,
`tersisip_semesta.py` `8a648838`, `bentangan_kohort.py` V2 `f4eae57a`, `funding.py`
`8d4b1f82`, `arsip.py` `0104958b`, `gerbang_1m.py` `c8cc54c8`, `resample.py`
`66a4b177`.

**`.github/workflows/` — 39 berkas** (v5: 38 + `lubang_tebing.yml` **`c8ae552a`**).
`ci.yml` = `c79497b2` (paths-ignore journal/decisions/hipotesis/reports; push ke
`lux_ai/**`, `tests/**`, `STATE*`, `PROMPT*` MENYALAKAN CI). `lubang_awal.yml` =
`3134bc9f` (**`paths` SATU entri** — lihat § KOREKSI KC-41). `lubang_tengah.yml` =
`557030de`. `karantina_semesta.yml` = `de40fa4e` (belum dibaca utuh).
`sebab_bangkit.yml` = `b8227cca`.

**`tests/` — 48 berkas** (47 dicacah tangan ref `b5442df3` + `test_lubang_tebing.py`
**`bf57d69d`**, 60 butir `test_01`..`test_60` dicacah mata). **Peringatan:** angka 48
adalah 47 + 1 secara turunan; pencacahan TANGAN sesudah trio BELUM dilakukan
(aturan 66). Wajib dicacah langsung pada giliran berikut sebelum dikutip.

## API terverifikasi — tambahan v6

API lama (v37–v45) tetap berlaku. Tambahan:

**`lubang_tebing` V1** (blob `575e777e`, dibaca UTUH dari `84b11164`): mengimpor
`kehidupan`, `kehidupan_arsip`, `silang_funding`, `lubang_awal`, `kohort_ekor`.
Tetapan: `VERSI=1`, `KELUARAN="reports/lubang_tebing.json"`,
`TEBING=kohort_ekor.TEBING` (="2025-07"),
`TOTAL_PECAHAN=lubang_awal.TOTAL_PECAHAN` (=8), `KELAS_MATI_DULU="mati_dulu"`,
`KELAS_SEREMPAK="serempak"`, `KELAS_LUBANG_DULU="lubang_dulu"`,
`KELAS_ARAH` (3 kelas), `BATAS_BARIS_LAPORAN=60`,
`R306_PITA_BUTIR_1=(0.25,0.60)`, `R306_MINIMAL_PENYEBUT_BUTIR_1=100`,
`R306_PITA_BUTIR_2_CACAH=(20,90)`, `BERKAS_DICAP` 6 berkas.
Fungsi: `nama_keluaran`, `sidik_kode`, `_bagian`, `kelas_arah`, `di_tebing`,
`perkaya`, `sebaran_arah`, `himpun`, `kendali_deteksi`, `dalam_pita`, `uji_r306`,
`kode_keluar`, `jalankan`, `main`. Medan tambahan per baris: `kelas_arah`,
`mati_sebelum_lubang_strikt`, `lubang_bukan_awal_pertama_di_tebing`, `bulan_tebing`.

**`lubang_awal` V1** (blob `8c36943d`): `peta_status`, `bulan_urut`, `ringkas`,
`himpun`, `kendali_deteksi`, `bangkit_lokal`, `BATAS_BARIS_LAPORAN=60`. Medan:
`bulan_mati_pertama`, `bulan_lubang_bukan_awal_pertama`, `bulan_pertama_berlubang`,
`akhir_lubang_awal`, `cacah_lubang_awal`, `cacah_lubang_bukan_awal`,
`masuk_penyebut_butir_1`, `mati_tidak_setelah_lubang_bukan_awal` (memakai `<=` —
**DILARANG dipakai untuk klaim arah**, aturan 80),
`lubang_awal_berakhir_sebelum_mati`, `bangkit`, `cacah_bulan`, `bulan_pertama`,
`bulan_terakhir`, `cacah_mati`, `cacah_lubang`. Sidik `156499ce…`.

**`silang_funding` V2** (blob `42c3aa9d`, 29.873 B): `bentuk_lubang_lokal(bulan_urut,
bulan_berlubang, bulan)` → bukan_lubang/awal/ekor/seluruh/tengah;
`baca_laporan_kehidupan(akar,total)` → (status, byte_parquet, meta);
`lubang_funding(funding)` → (Set[(simbol,bulan)], meta); `kendali_silang`,
`kendali_sah`, `bulan_per_simbol`, `SUMBER_FUNDING="reports/funding_semesta.json"`,
`TOTAL_PECAHAN`, `BENTUK_TERBITAN_FUNDING={"awal":48,"ekor":826,"tengah":6}`.
**Catatan untuk R-307:** `baca_laporan_kehidupan` sudah mengembalikan
`byte_parquet` — inilah sumber angka H-A018, tidak perlu pembaca baru.

`kohort_ekor` V4 (`c9b63bbe`): `TEBING="2025-07"`, `BULAN_DIHARAPKAN="2026-06"`,
`BATAS_SIMBOL=10`, `PAGU_MUNDUR=60`, `AMBANG_SEPI=0.5`, `bagian` (4 desimal, None
bila penyebut 0), `KENDALI_HIDUP=("BTCUSDT","ETHUSDT")`.
`kehidupan_arsip` (`318a5cb1`): `TOTAL_PECAHAN=8`.
`kehidupan` (`f49abb2b`): `STATUS_MATI="MATI"`, `STATUS_SEPI="SEPI"`,
`STATUS_HIDUP="HIDUP"`, `STATUS_TAK_TERUKUR`, `BULAN_MULAI="2025-07"`,
`BULAN_AKHIR="2026-06"`, `deret_bulan`, `klasifikasi`, `penyebut_ganda`.

Sidik lain: `sebab_bangkit` V1 `bafe4359e8f36f0402d4be4a4e4aef4a28f224f6419f06f701fb3a5bf696221a` ·
`tersisip_semesta` V1 `9618fd19e4ab2e7b5279177db600f6176afd914ab1e94576e54197f70ebc537c` ·
`bentangan_kohort` V2 `8ca6ebbefc3606464ebd7f94c6b51b1fdf500c62779cdcb5700ec2ee4ea9f32c` ·
`sidik_data_funding` `2c9fbd1b04f74c9c844bc223a99a103d12220b88d08667b3792720e5b9608d24` ·
`sidik_kode_silang_funding` seragam
`8a9b859c09cd64e30e203e6f8dc53411b8e341c44f112805b3041e5d4d3231b1` ·
laporan kehidupan seragam
`24b6bb265525e81c2e571b46e401f36903383f1e3738c487850861adc3e8c595`.

## Hipotesis

- H-A001 belum diuji · H-A002b GUGUR · H-A003 MENANG pada 3, GUGUR pada 9 · H-A004
  tak dapat diuji · H-A005 GUGUR · H-A006 MENANG enam run · H-A008 MENANG dua kali ·
  H-A009 GUGUR · H-A010 MENANG 5–0 · H-A011 MENANG · H-A012 MENANG · H-A013 MENANG
  6–0, TAFSIR DICABUT · H-A014 BENTUK BARU MENANG 9 dari 9 · H-A015 MENANG sebagai
  angka, DIBATASI sebagai tafsir (KC-45) · H-A016 PENGAMATAN, BELUM DIUJI (celah
  kelipatan 15 menit).
- **H-A017 [ADR-A011, dipertegas ADR-A012, dibatasi ADR-A013]:** arah sebab
  "kematian mendahului hilangnya funding" DICABUT sebagai pola untuk seluruh semesta.
  Bunyi tersisa: "pada LITUSDT, dan sejauh ini HANYA LITUSDT dari delapan bangkit,
  bulan MATI pertama mendahului bulan berlubang pertama sebanyak 5 bulan"; penyebut 1
  dari 8, wajib disebut (aturan 74). **[v46] Diukur atas semesta oleh R-306 dan
  hasilnya melemahkan H-A017 lebih jauh:** cacah `mati_dulu` = 40 dari 118, tetapi 39
  di antaranya artefak tebing `2025-07`; bukti lepas-tebing = 1 simbol (BTCSTUSDT).
  H-A017 TIDAK dipulihkan.
- **H-A018 [BARU v46; poros R-307] — byte parquet sebagai gejala kehidupan.** Dulu
  hanya PENGAMATAN di ekor H-A017 (LITUSDT: byte bulan MATI ~390–434 ribu lawan bulan
  HIDUP ~1,6–1,9 juta), kini dinaikkan menjadi hipotesis tersendiri agar tidak
  tercampur dengan klaim arah sebab (KC-36, KC-41 koreksi 2). Bunyi: "besar
  `byte_parquet` per simbol-bulan berkorelasi dengan status kehidupan; bulan MATI
  menempati bagian kecil dari total byte semesta". **BELUM DIUKUR atas 19.586
  simbol-bulan** — itulah pekerjaan R-307.

## Praregistrasi R-307 — DISALIN APA ADANYA dari jurnal 127 §7 (JANGAN DIUBAH)

Poros: **H-A018** (label dikoreksi dari "H-A017" di PROMPT v49; pita TIDAK berubah).

- **Butir 1 (BERISIKO).** Bagian byte parquet milik simbol-bulan berstatus **MATI**
  atas TOTAL byte parquet seluruh 19.586 simbol-bulan. Pita **0.02 .. 0.15**. Bila
  total byte = 0, butir ini TIDAK TERADJUDIKASI (aturan 41).
- **Butir 2 (BERISIKO).** Cacah simbol-bulan berstatus **TERUKUR** (HIDUP atau SEPI)
  yang `byte_parquet` **< 10.000**. Pita **20 .. 400**.
- **Butir 3 (MUDAH).** Sembilan invarian penggugur tetap nol, kedua kendali sah,
  kode keluar 0, dan cacah uji CI **diukur** (bukan diklaim).

Sembilan invarian penggugur: 19.586 · 787 · 1.401 MATI · 8 bangkit · 877 lubang
dalam penyebut · 880 lubang semesta · 122 ada_lubang · 5 lubang_awal · 118
lubang_bukan_awal. Sumber byte: `silang_funding.baca_laporan_kehidupan`. Nama modul
R-307 WAJIB dicek lewat pencacahan direktori lebih dulu (aturan 66) — pelajaran
`lubang_tengah`.
