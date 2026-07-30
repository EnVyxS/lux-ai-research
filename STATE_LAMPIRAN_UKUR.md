# STATE lampiran UKUR — bagian 3 dari STATE v45

**Kedudukan berkas ini.** STATE dipecah tiga sejak v43 (KC-42). Pembagian berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–79, KC-1..KC-46.
2. **`STATE_LAMPIRAN_EKOR.md`** — bagian 2: papan skor, ADR, catatan kejujuran.
3. **`STATE_LAMPIRAN_UKUR.md`** (berkas ini, v5) — bagian 3: pengukuran, modul,
   workflow, uji, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip lama; bukan sumber lagi.

Seluruh angka di sini berasal dari pengukuran terverifikasi. Yang ditambahkan v5:
trio `lubang_awal` V1; agregat lubang funding 122/5/118; CI 984; cacah direktori
dikoreksi (serapan 43, workflows 38, tests 47).

**Angka yang TIDAK berubah dari v44** (tidak diulang): penyebut 787, taksonomi 9
kelas, karantina 12, bulan ABSEN 11, H-A013..H-A015, delapan simbol bangkit, lubang
funding 880/877, LITUSDT, BTCSTUSDT, terhenti, SETTLED. Rinciannya di v44 (blob
`d302caff`).

## Semesta riset = `perpetual_usdt` = penyebut 787 — tidak berubah

- `cacah_perpetual_usdt` **787** = `cacah_penyebut_simbol` **787**
- `cacah_perpetual_usdt_luar_penyebut` 0, `cacah_penyebut_bukan_perpetual_usdt` 0
- Batas wajib disebut: token saham/ETF/komoditas ikut di dalam 787.

## KC-18 — semesta kehidupan (tidak berubah)

Atas **19.586** simbol-bulan lolos: **1.401 MATI** (7,153%), **98 SEPI**, **18.087
HIDUP**. Dari 1.401 MATI: 842 kehilangan funding, 559 tetap berfunding.
`cacah_simbol_tanpa_hidup` **18**.

## Lubang funding — agregat semesta [v5, `lubang_awal` V1]

Sumber: `lubang_awal.py` V1 run **30522785043** (commit `d304d3eb`, kode 0),
laporan `reports/lubang_awal.json` blob `3da15a11`, `_status.json` blob `ce1a9901`.
Keduanya terbaca UTUH.

- `cacah_simbol_ada_lubang` = **122** (dari 787)
- `cacah_simbol_lubang_awal` = **5** (bentuk AWAL, lubang sejak bulan pertama)
- `cacah_simbol_lubang_bukan_awal` = **118**
- BNXUSDT punya lubang AWAL dan bukan-awal sekaligus.

**Lima simbol lubang bentuk AWAL:** BNXUSDT, ICPUSDT, JUPUSDT, QTUMUSDT, TLMUSDT.
Dari 5, tiga (BNX, JUP, QTUM) `lubang_awal_berakhir_sebelum_mati` true (atau tak
pernah mati); dua (ICP, TLM) false — lubang AWAL melewati kematian (sumber
salah-baca R-304, KC-46).

**Butir 1 R-305 (adjudikasi):** penyebut = **118** (≥100, teradjudikasi); bagian
`mati_tidak_setelah_lubang_bukan_awal` = **1.0** (118/118) — di ATAS pita 0.55..0.95
→ KALAH. Bacaan: tautologis (lubang bukan-awal ≈ delisting; banyak lubang
bukan-awal pertama = tebing “2025-07”). Aturan 10.

**Butir 2 R-305:** penyebut = 5 (<20) → KALAH (aturan 41/46). Numerator lubang-awal
bulan-pertama = 3 (BNX, JUP, QTUM true), bagian 0.6 (<0.80).

**Kendali `lubang_awal` V1:** data BTCUSDT 2021-05/08/01 HIDUP+funding →
`kendali_sah` true; `kendali_deteksi_sah` true. Enam selisih invarian = 0
(19.586/787/1.401/8/877/880).

**Sidik kode `lubang_awal` V1 =**
`156499ce9d6e822bb7f57786e8e308955441996699c1fd53d0e8814e1f8f2362`

## Jumlah uji — terukur

**984** (run 30522785099, commit `d304d3eb`, kode 0, 2026-07-30T07:23:33Z).
Riwayat: 769 → 814 → 832 → 879 → 936 → **984**. Turunan: 936 + 48
`test_lubang_awal.py` = 984 ✅

## Modul, workflow, dan berkas uji — dicacah tangan ref `b5442df3` [v5]

**`lux_ai/serapan/` — 43 berkas** (v44: 42 + `lubang_awal.py`). Blob baru:
`lubang_awal.py` V1 **`8c36943d`** (15.801 B). Blob lain identik dengan v44
(`d302caff`): `kehidupan.py` `f49abb2b`, `kehidupan_arsip.py` `318a5cb1`,
`silang_funding.py` V2 `42c3aa9d`, `kohort_ekor.py` `c9b63bbe`, `sebab_bangkit.py`
`fd5a1dc4`, `tersisip_semesta.py` `8a648838`, `bentangan_kohort.py` V2 `f4eae57a`,
dst.

**`.github/workflows/` — 38 berkas** (v44: 37 + `lubang_awal.yml` **`3134bc9f`**,
2.240 B, `paths` sempit pada `lux_ai/serapan/lubang_awal.py`,
`tests/test_lubang_awal.py`, dan workflow sendiri). `ci.yml` = `c79497b2`
(paths-ignore journal/decisions/hipotesis/reports; push ke `lux_ai/**`, `tests/**`,
`STATE*`, `PROMPT*` MENYALAKAN CI).

**`tests/` — 47 berkas** (v44 mencatat 45; DIKOREKSI oleh pencacahan langsung —
lihat catatan kejujuran EKOR v5). Blob baru: `test_lubang_awal.py` **`86c401ee`**
(48 butir, `test_01`..`test_48`).

## API terverifikasi — tambahan v5

API lama (v37–v44) tetap berlaku. Tambahan:

**`lubang_awal` V1** (blob `8c36943d`, UTUH): mengimpor `kehidupan`,
`kehidupan_arsip`, `silang_funding`. Medan per simbol: `bulan_mati_pertama`,
`bulan_lubang_bukan_awal_pertama`, `bulan_pertama_berlubang`, `akhir_lubang_awal`,
`cacah_lubang_awal`, `cacah_lubang_bukan_awal`, `masuk_penyebut_butir_1`,
`mati_tidak_setelah_lubang_bukan_awal`, `lubang_awal_berakhir_sebelum_mati`.
Agregat: `cacah_simbol_ada_lubang`, `cacah_simbol_lubang_awal`,
`cacah_simbol_lubang_bukan_awal`. Kendali: `kendali_sah`, `kendali_deteksi_sah`.
Sidik kode `156499ce9d6e822bb7f57786e8e308955441996699c1fd53d0e8814e1f8f2362`.

**`silang_funding` V2** (blob `42c3aa9d`, 29.873 B): `bentuk_lubang_lokal(bulan_urut,
bulan_berlubang, bulan)` → bukan_lubang/awal/ekor/seluruh/tengah;
`baca_laporan_kehidupan(akar,total)`→(status,byte_parquet,meta);
`lubang_funding(funding)`→(Set[(simbol,bulan)],meta); `kendali_silang`,
`kendali_sah`, `SUMBER_FUNDING="reports/funding_semesta.json"`, `TOTAL_PECAHAN`.
`kohort_ekor` V4 (`c9b63bbe`): `TEBING="2025-07"`, `BULAN_DIHARAPKAN="2026-06"`,
`BATAS_SIMBOL=10`. `kehidupan_arsip` (`318a5cb1`): `TOTAL_PECAHAN=8`.
`kehidupan` (`f49abb2b`): `STATUS_MATI="MATI"`, `STATUS_HIDUP="HIDUP"`, `STATUS_SEPI`.

`sebab_bangkit` V1 sidik = `bafe4359e8f36f0402d4be4a4e4aef4a28f224f6419f06f701fb3a5bf696221a`.
`tersisip_semesta` V1 sidik = `9618fd19e4ab2e7b5279177db600f6176afd914ab1e94576e54197f70ebc537c`.
`bentangan_kohort` V2 sidik = `8ca6ebbefc3606464ebd7f94c6b51b1fdf500c62779cdcb5700ec2ee4ea9f32c`.
`sidik_data_funding` = `2c9fbd1b04f74c9c844bc223a99a103d12220b88d08667b3792720e5b9608d24`.
`sidik_kode_silang_funding` seragam = `8a9b859c09cd64e30e203e6f8dc53411b8e341c44f112805b3041e5d4d3231b1`.
Sidik kode laporan kehidupan seragam =
`24b6bb265525e81c2e571b46e401f36903383f1e3738c487850861adc3e8c595`.

## Hipotesis

- H-A001 belum diuji · H-A002b GUGUR · H-A003 MENANG pada 3, GUGUR pada 9 · H-A004
  tak dapat diuji · H-A005 GUGUR · H-A006 MENANG enam run · H-A008 MENANG dua kali ·
  H-A009 GUGUR · H-A010 MENANG 5–0 · H-A011 MENANG · H-A012 MENANG · H-A013 MENANG
  6–0, TAFSIR DICABUT · H-A014 BENTUK BARU MENANG 9 dari 9 · H-A015 MENANG sebagai
  angka, DIBATASI sebagai tafsir (KC-45) · H-A016 PENGAMATAN, BELUM DIUJI.
- **H-A017 [ADR-A011, dipertegas ADR-A012]:** arah sebab “kematian mendahului
  hilangnya funding” DICABUT sebagai pola untuk seluruh semesta. Bunyi tersisa:
  “pada LITUSDT, dan sejauh ini HANYA LITUSDT dari delapan bangkit, bulan MATI
  pertama mendahului bulan berlubang pertama sebanyak 5 bulan”; penyebut 1 dari 8,
  wajib disebut (aturan 74). Belum diuji atas semesta. Dugaan byte_parquet sebagai
  gejala kehidupan tetap PENGAMATAN (LITUSDT byte mati ~390–434 ribu lawan hidup
  ~1,6–1,9 juta).
