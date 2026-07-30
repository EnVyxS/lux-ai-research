# STATE lampiran UKUR — bagian 3 dari STATE (v7, milik STATE v47)

**Kedudukan berkas ini.** STATE dipecah tiga sejak v43 (KC-42). Pembagian berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, KC-1..KC-48.
2. **`STATE_LAMPIRAN_EKOR.md`** v7 — bagian 2: papan skor, ADR, catatan kejujuran.
3. **`STATE_LAMPIRAN_UKUR.md`** (berkas ini, v7) — bagian 3: pengukuran, modul,
   workflow, uji, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip lama; bukan sumber lagi.

Dasar v7: UKUR v6 (blob **`27e59a79dacc9a07091c948c0f955491b1247478`**), dibaca UTUH
sebelum berkas ini ditulis. Yang ditambahkan v7: **byte parquet atas seluruh semesta**
(pengukuran pertama); API `byte_semesta` V1; CI 1100; adjudikasi R-307 MELESET;
H-A018 dari BELUM DIUKUR menjadi DIUKUR-dan-DIBATASI; praregistrasi **R-308**.

**PERINGATAN KESERASIAN VERSI — dorongan BERTAHAP.** Saat berkas ini didorong,
`STATE_LAMPIRAN_EKOR.md` sudah **v7** (commit `cfc42e70`, blob `9e906dfb`) tetapi
`STATE.md` masih **v46** (blob `41b5b585`), sehingga **KC-48** dan **usulan aturan 82**
belum tercantum di bagian 1. Sumber sah keduanya sampai `STATE.md` v47 naik:
`journal/2026-07-30-128.md` §6–§7 dan `decisions/ADR-A014.md`. Pemecahan ini SENGAJA
(lihat kepala EKOR v7): menulis tiga berkas besar dari satu konteks terpakai adalah
cara paling pasti merusak aturan 1–81.

**Angka yang TIDAK berubah dari v44/v45/v6** (tidak diulang): taksonomi 9 kelas,
karantina 12, bulan ABSEN 11, H-A013..H-A015, terhenti, SETTLED. Rinciannya di v44
(blob `d302caff`), v45 (blob `eb826817`), v6 (blob `27e59a79`).

## KOREKSI KC-41 — BACA SEBELUM MENGUTIP BERKAS INI

Kedua koreksi di bawah LAHIR di v6 dan **tetap dicantumkan** karena keduanya soal
dokumen kami sendiri, bukan soal data — menghapusnya berarti menghapus jejak cacat.

**Koreksi 1 (kesalahan berkas ini pada v5).** UKUR v5 menulis bahwa
`.github/workflows/lubang_awal.yml` ber-`paths` pada tiga entri. **ITU SALAH.** Berkas
asli (blob **`3134bc9f6f91c83ed39ff8424506ac253317edee`**, dibaca UTUH dua kali — di
giliran v6 dan sekali lagi di giliran R-307) memuat **SATU** entri `paths`:

```
paths:
  - 'lux_ai/serapan/lubang_awal.py'
```

Aturan yang diperkuat: bila bagian STATE bertentangan, **berkas sumber menang**.
`lubang_tebing.yml` (`c8ae552a`) dan `byte_semesta.yml` (`45650ff9`) sengaja meniru
berkas ASLI ini, bukan rumusan v5.

**Koreksi 2 (kesalahan PROMPT v49).** PROMPT v49 (blob `4dca042c`) menyebut poros
R-307 sebagai "H-A017 byte parquet". **ITU SALAH LABEL.** H-A017 adalah hipotesis arah
sebab (LITUSDT); byte parquet adalah **H-A018**. Pita praregistrasi R-307 TIDAK diubah
(aturan 29 utuh); hanya labelnya dikoreksi. PROMPT v50 (blob `08fd3f76`) sudah memuat
koreksi ini — **utang koreksi LUNAS**.

## Semesta riset = `perpetual_usdt` = penyebut 787 — tidak berubah

- `cacah_perpetual_usdt` **787** = `cacah_penyebut_simbol` **787**
- `cacah_perpetual_usdt_luar_penyebut` 0, `cacah_penyebut_bukan_perpetual_usdt` 0
- Batas wajib disebut: token saham/ETF/komoditas ikut di dalam 787.

## KC-18 — semesta kehidupan (tidak berubah, dikonfirmasi ulang oleh R-307)

Atas **19.586** simbol-bulan lolos: **1.401 MATI** (7,153%), **98 SEPI**, **18.087
HIDUP**. Dari 1.401 MATI: 842 kehilangan funding, 559 tetap berfunding.
`cacah_simbol_tanpa_hidup` **18**.

**[v7] Kelengkapan status kini TERUKUR:** `byte_semesta` melaporkan `cacah_lain` = 0,
jadi seluruh 19.586 berstatus MATI/SEPI/HIDUP dan **tidak ada TAK_TERUKUR**.
18.087 + 98 = 18.185 TERUKUR, + 1.401 = 19.586 ✅

## Lubang funding — agregat semesta (tetap)

- `cacah_simbol_ada_lubang` = **122** (dari 787)
- `cacah_simbol_lubang_awal` = **5** · `cacah_simbol_lubang_bukan_awal` = **118**
- BNXUSDT punya lubang AWAL dan bukan-awal sekaligus.
- Lima bentuk AWAL: BNXUSDT, ICPUSDT, JUPUSDT, QTUMUSDT, TLMUSDT. Tiga (BNX, JUP,
  QTUM) `lubang_awal_berakhir_sebelum_mati` true; dua (ICP, TLM) false — lubang AWAL
  melewati kematian (sumber salah-baca R-304, KC-46).
- Lubang funding **880** semesta / **877** dalam penyebut / 3 tak dikenal. Irisan
  880 lawan 877 BELUM diukur.

## BYTE PARQUET ATAS SELURUH SEMESTA [BARU v7 — pengukuran PERTAMA]

Sumber: `byte_semesta.py` V1 run **30526358811** (commit `d3bc2039`, kode 0,
2026-07-30T08:21:25Z). Laporan `reports/byte_semesta.json` blob **`8b7f2077`**
(terbaca **UTUH**, bukan 99% seperti `lubang_tebing.json` — rancangan ringkas
`BATAS_BARIS_LAPORAN=40` berhasil), `_status.json` blob **`2cbcbc1b`**.

**Total byte parquet seluruh semesta = 32.706.262.375** (≈32,7 GB) atas 19.586
simbol-bulan. Penyebutnya laporan kehidupan itu sendiri; simbol-bulan di luar 19.586
tidak pernah masuk (bukan dibuang diam-diam).

| status | cacah | byte | byte_min | byte_maks | byte_rata |
| --- | --- | --- | --- | --- | --- |
| HIDUP | 18.087 | 32.049.492.952 | **22.440** | 2.770.666 | 1.771.963 |
| SEPI | 98 | 77.728.024 | 259.327 | 1.231.408 | 793.143 |
| MATI | 1.401 | **579.041.399** | **97.634** | **451.875** | **413.306** |

- `bagian_byte_mati` = **0.017704297493883234** · `bagian_byte_terukur` = 0.982296
- `cacah_terukur_byte_kecil` (< 10.000, STRIKT) = **0** · `cacah_mati_byte_kecil` = 0
  · `cacah_lain_byte_kecil` = 0 · `cacah_byte_nol` = **0**
- **Dasar keras ukuran berkas ≈ 22 KB.** Tidak ada satu pun simbol-bulan di bawah
  22.440 byte, dan tidak ada yang berbyte nol → sebab langsung KC-48.
- **IRISAN KELAS — wajib dikutip bersama setiap klaim H-A018:** HIDUP `byte_min`
  **22.440** < MATI `byte_min` **97.634**. Berkas TERKECIL di semesta milik bulan
  **HIDUP** dan lebih kecil daripada SETIAP bulan MATI. Besar berkas karena itu
  **DILARANG** dipakai sebagai detektor status (ADR-A014 keputusan 2, kerabat KC-38).
- **Bulan MATI bukan bulan KOSONG:** `byte_min` 97.634 > 0 dan `cacah_byte_nol` 0.
  Berkasnya ada dan berisi, hanya ≈4,3× lebih ringan daripada HIDUP. **APA ISINYA
  BELUM DIUKUR** (lilin berulang? volume nol?) dan dilarang ditebak (ADR-A014 kep. 4).
- Sembilan selisih invarian = **0** (19.586 / 787 / 1.401 / 8 / 877 / 880 / 122 / 5 /
  118). `sidik_seragam` true, `cacah_laporan_dibaca` 8 = `total_pecahan` 8,
  `cacah_kunci_ganda` 0, `cacah_lubang_ganda` 0, `laporan_hilang` [].
- **Kendali dua lapis sah.** Data (`kendali_sah` true): tiga simbol-bulan berparquet
  terbesar seluruhnya **BTCUSDT** — 2021-05 **2.770.666**, 2021-08 2.730.341, 2021-01
  2.722.266 — semuanya HIDUP dan berfunding. Detektor (`kendali_deteksi_sah` true):
  bentangan buatan berambang 50 menghasilkan `total_byte` **1068** (= 1018 + ambang),
  `cacah_terukur_byte_kecil` **2** (KENDALI_SEPI 5, KENDALI_KECIL 10), sementara baris
  tepat DI AMBANG tidak terhitung dan baris kelas LAIN berbyte kecil tidak masuk
  butir 2. **Karena itu nol pada butir 2 sah disebut TERUKUR, bukan buta** (aturan 50,
  KC-21).
- **Adjudikasi R-307:** butir 1 **KALAH** (0.017704 di bawah pita 0.02–0.15), butir 2
  **KALAH** (0, ambang mustahil — KC-48), butir 3 MENANG (MUDAH) → **MELESET**.
  Bacaan jujurnya di EKOR v7 § Catatan kejujuran: kedua kekalahan BERBEDA JENIS.
- Pengamatan LITUSDT lama (MATI ~390–434 ribu lawan HIDUP ~1,6–1,9 juta) ternyata
  **mewakili semesta dengan baik** (rata MATI 413.306, rata HIDUP 1.771.963).
- Sidik COCOK dengan run sebelumnya (aturan 36) → semesta SAMA: laporan kehidupan
  `24b6bb26…`, `sidik_data_funding` `2c9fbd1b…`, `silang_funding` `8a9b859c…`,
  `lubang_awal` `156499ce…`.

**Sidik kode `byte_semesta` V1 =**
`e02aca2b3967069b500b01d27a1d2d1553f47b912ea41ddbecd9e4e6c33883c7`

## Arah waktu kematian lawan lubang funding [v6, `lubang_tebing` V1 — tetap berlaku]

Sumber: run **30524631435** (commit `84b11164`, kode 0). Laporan blob **`7d8883f5`**
(terbaca 99%; seluruh `ringkasan` dan `uji_r306` terbaca), `_status.json` `685191e1`.
Penyebut = **118** simbol berlubang bukan-awal.

| kelas arah (perbandingan STRIKT, aturan 80) | cacah | bagian |
| --- | --- | --- |
| `mati_dulu` — MATI pertama **<** lubang bukan-awal pertama | **40** | **0.339** |
| `serempak` — bulan SAMA (DILARANG di numerator) | **78** | 0.661 |
| `lubang_dulu` — MATI pertama **>** lubang pertama | **0** | 0.000 |

- `cacah_tebing_butir_2` = **39**, `bagian_tebing_butir_2` = **0.3305** (`2025-07`).
- **39 dari 40** anggota `mati_dulu` ada di tebing (0.975). Satu-satunya bukan-tebing:
  **BTCSTUSDT** (lubang 2022-01, MATI 2021-04, `cacah_mati` 63). → KC-47, aturan 81.
- `penyebut_butir_1` dilapor 60 baris (kena `BATAS_BARIS_LAPORAN` 60 — daftar TIDAK
  lengkap, aturan 62/KC-24).
- **Adjudikasi R-306:** TEPAT 3/3; kemenangan sah, klaim ilmiah hampir kosong.
- Sidik `lubang_tebing` V1 =
  `4a5c2e4279eb1554dc119b48d6a8db61f6ea4ee11b7539efd70ee71d1ae18bf3`

## Jumlah uji — terukur

**1100** (run **30526358010**, commit **`d3bc2039`**, kode 0, 2026-07-30T08:21:45Z,
blob **`0765ce7b`**, "1100 tests collected in 0.56s"). Riwayat: 814 → 832 → 879 → 936
→ 984 → 1044 → **1100**. Turunan: 1044 + 56 `test_byte_semesta.py` = 1100 ✅
Aturan 57 kini **26 dari 26**. Aturan 38 pemakaian ke-**32**.

## Modul, workflow, dan berkas uji [v7]

**PEMBEDAAN YANG WAJIB DIJAGA (aturan 66, KC-33):** cacah TANGAN dilakukan pada ref
**`d73b07b9`** — yaitu SEBELUM trio `byte_semesta` didorong — dan hasilnya
`lux_ai/serapan/` **44**, `.github/workflows/` **39**, `tests/` **48**, ketiganya
dinomori satu per satu. Angka di bawah adalah cacah tangan itu **+1 secara turunan**
karena trio menambah tepat satu berkas per direktori. **Pencacahan tangan sesudah
trio BELUM dilakukan** dan wajib dilakukan sebelum angka 45/40/49 dikutip sebagai
fakta terhitung.

- **`lux_ai/serapan/` — 45 berkas (turunan)** = 44 tangan + `byte_semesta.py` V1 blob
  **`ff68e4be2282470aa79c5be89152f6991ca9bfa6`**.
- **`.github/workflows/` — 40 berkas (turunan)** = 39 tangan + `byte_semesta.yml` blob
  **`45650ff95c62d6ee33c2dda04393580250dbe73f`** (2.240-an B; `paths` **SATU** entri
  `- 'lux_ai/serapan/byte_semesta.py'`, meniru `lubang_awal.yml` asli).
- **`tests/` — 49 berkas (turunan)** = 48 tangan + `test_byte_semesta.py` blob
  **`0e1e3ab201cb4b625e921a020b0cfa5fc453120d`** (**56** butir, `test_01`..`test_56`,
  dicacah mata pada berkas yang sudah di main; tanpa `parametrize`).

Blob lain identik dengan v6: `kehidupan.py` `f49abb2b`, `kehidupan_arsip.py`
`318a5cb1`, `silang_funding.py` V2 `42c3aa9d`, `kohort_ekor.py` `c9b63bbe`,
`lubang_awal.py` `8c36943d`, `lubang_tebing.py` `575e777e`, `lubang_tengah.py`
`4d3beaf1`, `sebab_bangkit.py` `fd5a1dc4`, `tersisip_semesta.py` `8a648838`,
`bentangan_kohort.py` V2 `f4eae57a`, `funding.py` `8d4b1f82`, `arsip.py` `0104958b`,
`gerbang_1m.py` `c8cc54c8`, `resample.py` `66a4b177`. `ci.yml` = `c79497b2`
(paths-ignore journal/decisions/hipotesis/reports; push ke `lux_ai/**`, `tests/**`,
`STATE*`, `PROMPT*` MENYALAKAN CI). `karantina_semesta.yml` = `de40fa4e` (belum
dibaca utuh).

## API terverifikasi — tambahan v7

API lama (v37–v6) tetap berlaku. Tambahan:

**`byte_semesta` V1** (blob `ff68e4be`, dibaca UTUH dari `d3bc2039` sesudah push):
mengimpor `kehidupan`, `kehidupan_arsip`, `lubang_awal`, `silang_funding`.
Tetapan: `VERSI=1`, `KELUARAN="reports/byte_semesta.json"`,
`TOTAL_PECAHAN=kehidupan_arsip.TOTAL_PECAHAN` (=8),
`PENYEBUT_TERCATAT=19586`, `SIMBOL_TERCATAT=787`, `MATI_TERCATAT=1401`,
`BANGKIT_TERCATAT=8`, `LUBANG_DALAM_PENYEBUT_TERCATAT=877`,
`LUBANG_SEMESTA_TERCATAT=880`, `ADA_LUBANG_TERCATAT=122`, `LUBANG_AWAL_TERCATAT=5`,
`LUBANG_BUKAN_AWAL_TERCATAT=118`, `R307_PITA_BUTIR_1=(0.02,0.15)`,
`R307_AMBANG_BYTE_KECIL=10000`, `R307_PITA_BUTIR_2_CACAH=(20,400)`,
`KELAS_MATI="MATI"`, `KELAS_TERUKUR="TERUKUR"`, `KELAS_LAIN="LAIN"`, `KELAS_UKUR`
(3 kelas), `BATAS_BARIS_LAPORAN=40`, `MEDAN_SELISIH` (**9** nama selisih),
`BERKAS_DICAP` **5** berkas (`byte_semesta.py`, `kehidupan.py`, `kehidupan_arsip.py`,
`lubang_awal.py`, `silang_funding.py`).
Fungsi: `nama_keluaran`, `sidik_kode`, `_bagian` (penyebut 0 → None),
`kelas_ukur` (MATI→MATI; HIDUP/SEPI→TERUKUR; sisanya→LAIN),
`himpun_byte(status, byte_parquet, ambang=10000)`, `daftar_terukur_byte_kecil`
(urut byte menaik lalu simbol-bulan), `sebaran_byte_per_status`,
`kendali_deteksi(ambang=50)`, `dalam_pita`, `uji_r307`, `kode_keluar`, `jalankan`,
`main`. Medan `himpun_byte`: `total_byte`, `byte_mati`, `byte_terukur`, `byte_lain`,
`bagian_byte_mati`, `bagian_byte_terukur`, `cacah_mati`, `cacah_terukur`,
`cacah_lain`, `cacah_terukur_byte_kecil`, `cacah_mati_byte_kecil`,
`cacah_lain_byte_kecil`, `ambang_byte_kecil`, `cacah_byte_nol`, `cacah_baris`.
`kode_keluar` → 2 bila `sidik_seragam` false, `cacah_laporan_dibaca` ≠ `total_pecahan`,
`cacah_kunci_ganda` > 0, `kendali_sah` false, `kendali_deteksi_sah` false, atau salah
satu dari sembilan selisih bukan nol.

**`silang_funding` V2** (blob `42c3aa9d`, 29.873 B, dibaca UTUH ulang di giliran
R-307): `baca_laporan_kehidupan(akar,total)` → **TIGA** nilai `(status, byte_parquet,
meta)` dengan `byte_parquet[k] = int(baris.get("byte_parquet") or 0)`;
`lubang_funding(funding)` → `(Set[(simbol,bulan)], meta)`;
`kendali_silang(byte_parquet, status, lubang, cacah=KENDALI_CACAH)`; `kendali_sah`;
`bentuk_lubang_lokal`; `baca_medan_baris(akar,total,medan="cacah_lilin")`;
`SUMBER_FUNDING="reports/funding_semesta.json"`, `KENDALI_CACAH=3`,
`BENTUK_TERBITAN_FUNDING={"awal":48,"ekor":826,"tengah":6}`, `BERKAS_DICAP` 3 berkas.

**`lubang_awal` V1** (blob `8c36943d`, dibaca UTUH ulang di giliran R-307):
`peta_status(status)` → `{simbol:{bulan:status}}`; `ringkas(simbol, peta_bulan,
berlubang)`; `himpun(baris)` → `cacah_simbol`, `cacah_bangkit`,
`cacah_simbol_ada_lubang`, `cacah_simbol_lubang_awal`,
`cacah_simbol_lubang_bukan_awal`, `penyebut_butir_1`, `numerator_butir_1`,
`bagian_butir_1`, `penyebut_butir_2`; `bulan_urut`, `bangkit_lokal`,
`kendali_deteksi`, `dalam_pita`, `uji_r305`, `kode_keluar`;
`POLA_BULAN=re.compile(r"^\d{4}-\d{2}$")`; `BATAS_BARIS_LAPORAN=60`; `BERKAS_DICAP`
4 berkas. Medan `mati_tidak_setelah_lubang_bukan_awal` memakai `<=` — **DILARANG
dipakai untuk klaim arah** (aturan 80). Sidik `156499ce…`.

`lubang_tebing` V1 (`575e777e`): rincian di v6; `BATAS_BARIS_LAPORAN=60`,
`KELAS_ARAH` 3 kelas, `BERKAS_DICAP` 6 berkas.
`kohort_ekor` V4 (`c9b63bbe`): `TEBING="2025-07"`, `BULAN_DIHARAPKAN="2026-06"`,
`BATAS_SIMBOL=10`, `PAGU_MUNDUR=60`, `AMBANG_SEPI=0.5`, `bagian` (4 desimal, None
bila penyebut 0), `KENDALI_HIDUP=("BTCUSDT","ETHUSDT")`.
`kehidupan_arsip` (`318a5cb1`): `TOTAL_PECAHAN=8`, `nama_keluaran(i)`.
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
- **H-A017 [ADR-A011, dipertegas ADR-A012, dibatasi ADR-A013]:** arah sebab "kematian
  mendahului hilangnya funding" DICABUT sebagai pola untuk seluruh semesta. Bunyi
  tersisa: "pada LITUSDT, dan sejauh ini HANYA LITUSDT dari delapan bangkit, bulan
  MATI pertama mendahului bulan berlubang pertama sebanyak 5 bulan"; penyebut 1 dari 8
  (aturan 74). R-306 melemahkannya lebih jauh: `mati_dulu` 40 dari 118 tetapi 39
  artefak tebing; bukti lepas-tebing = 1 simbol. **TIDAK dipulihkan oleh R-307** —
  R-307 tidak menyentuh soal arah sebab sama sekali (ADR-A014 keputusan 6).
- **H-A018 [BARU v46, DIUKUR v7 oleh R-307] — byte parquet sebagai gejala kehidupan.**
  **Bunyi yang BOLEH dipakai (ADR-A014 keputusan 2):** "bulan MATI menempati bagian
  KECIL dari byte semesta (**0,0177** dari 32,7 GB) dan rata-rata sekitar **4,3×**
  lebih kecil daripada bulan HIDUP (**413.306** lawan **1.771.963** byte)". Arah ini
  DIDUKUNG kuat oleh pengukuran atas 19.586 simbol-bulan.
  **Bunyi yang DILARANG:** "berkas kecil berarti pasar mati". Kedua kelas beririsan
  dan irisannya BERLAWANAN dengan dugaan — HIDUP `byte_min` 22.440 < MATI `byte_min`
  97.634. Besar berkas DILARANG dipakai sebagai detektor status (kerabat KC-38).
  **Catatan:** R-307 MELESET meski arahnya didukung, karena PITA-nya keliru; hipotesis
  yang benar arahnya tidak menyelamatkan ramalan yang salah angkanya (aturan 29).
- Hipotesis berikutnya **H-A019**.

## Praregistrasi R-307 — SUDAH TERADJUDIKASI: MELESET

Disimpan apa adanya sebagai jejak (aturan 29 — pita tidak boleh diubah sesudah
pengukuran). Poros H-A018.

- Butir 1 (BERISIKO): bagian byte MATI atas total 19.586, pita **0.02 .. 0.15** →
  terukur **0.017704** → **KALAH**.
- Butir 2 (BERISIKO): cacah TERUKUR ber-`byte_parquet` **< 10.000**, pita **20 .. 400**
  → terukur **0** → **KALAH** (ambang mustahil; dasar semesta 22.440 — **KC-48**).
- Butir 3 (MUDAH): sembilan invarian nol + dua kendali sah + kode 0 + CI diukur →
  **MENANG**.

## Praregistrasi R-308 — DISALIN APA ADANYA dari jurnal 128 §9 (JANGAN DIUBAH)

Poros tetap **H-A018**, kini menyerang **IRISAN** kedua kelas — pertanyaan yang baru
lahir dari pengukuran R-307 dan belum pernah diukur. Kedua butir berisiko memakai
ambang **RELATIF terhadap sebaran yang SUDAH terukur**, sehingga KC-48 dijawab
langsung, bukan hanya dicatat.

- **Butir 1 (BERISIKO).** Cacah simbol-bulan **HIDUP** yang `byte_parquet` lebih kecil
  daripada `byte_min` MATI terukur (**97.634**), atas penyebut **18.087**. Pita
  **20 .. 600**. Dasar: HIDUP `byte_min` 22.440 membuktikan zona itu TIDAK kosong,
  tetapi berapa lebarnya sama sekali belum diukur. Bila cacahnya di bawah 20, irisan
  kedua kelas nyaris tidak ada dan besar berkas hampir memisahkan status; bila di atas
  600, tafsir "MATI lebih kecil" jauh lebih lemah. Penyebut 0 → TIDAK TERADJUDIKASI
  (aturan 41).
- **Butir 2 (BERISIKO).** Cacah simbol-bulan **MATI** yang `byte_parquet` < **150.000**,
  atas penyebut **1.401**. Pita **10 .. 300**. Dasar: MATI min 97.634, rata 413.306,
  maks 451.875 — sebarannya menumpuk tinggi, jadi ekor bawahnya diduga tipis. Ambang
  150.000 dipilih dari sebaran TERUKUR, bukan dari angka bulat yang enak dibaca.
- **Butir 3 (MUDAH).** Sembilan invarian penggugur tetap nol, kedua kendali sah, kode
  keluar 0, dan cacah uji CI **diukur** bukan diklaim.

Sembilan invarian penggugur tetap: 19.586 · 787 · 1.401 MATI · 8 bangkit · 877 lubang
dalam penyebut · 880 lubang semesta · 122 ada_lubang · 5 lubang_awal · 118
lubang_bukan_awal. Sumber byte: `silang_funding.baca_laporan_kehidupan` (TIGA nilai).
Nama modul R-308 WAJIB dicek lewat pencacahan direktori lebih dulu (aturan 66) —
pelajaran `lubang_tengah`. Laporan WAJIB ringkas (`BATAS_BARIS_LAPORAN`) — pelajaran
`lubang_tebing.json` yang terpotong.
