# STATE lampiran UKUR — bagian 3 dari STATE v44

**Kedudukan berkas ini.** STATE dipecah tiga sejak v43 (KC-42). Pembagian berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–79, KC-1..KC-44.
2. **`STATE_LAMPIRAN_EKOR.md`** — bagian 2: papan skor, ADR, catatan kejujuran.
3. **`STATE_LAMPIRAN_UKUR.md`** (berkas ini, diperbarui v44) — bagian 3: pengukuran,
   modul, workflow, uji, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip lama; bukan sumber lagi.

Seluruh angka di sini berasal dari pengukuran yang sudah terverifikasi. Yang
ditambahkan pada v44: trio `bentangan_kohort` V2, `tersisip_semesta` V1,
`sebab_bangkit` V1; delapan simbol bangkit; listing serapan 41, workflows 36, tests
45; CI 936; H-A017 dirumuskan ulang.

**Angka yang TIDAK berubah dari v43** (tidak diulang di sini bila sudah tercatat
di tempat lain): penyebut 787, taksonomi 9 kelas, karantina 12, bulan ABSEN 11,
H-A013..H-A015, lubang funding 880/877, LITUSDT, BTCSTUSDT, terhenti, SETTLED.

## Semesta riset = `perpetual_usdt` = penyebut 787 — tidak berubah dari v43

Sumber, angka, dan bukti tiga arah: sama seperti STATE_LAMPIRAN_UKUR versi
sebelumnya (blob `0e9ec378`). Ringkas:
- `cacah_perpetual_usdt` **787** = `cacah_penyebut_simbol` **787**
- `cacah_perpetual_usdt_luar_penyebut` 0, `cacah_penyebut_bukan_perpetual_usdt` 0
- Arah ketiga: `bulan_absen` V1 `cacah_nama_penyebut` **787**, `selisih` 0
- Batas wajib disebut: token saham/ETF/komoditas ikut di dalam 787.

### Taksonomi kanonik — sembilan kelas (tidak berubah)

`lux_ai/semesta/taksonomi.py` (blob `b418c7ba`). Tabel dan silang dari v43 tetap
berlaku: `perpetual_usdt` 787/19.598 · `futures_kedaluwarsa` 50/258 ·
`perpetual_busd` 41/812 · `perpetual_usdc` 39/893 · `sisa_settled` 15/36 ·
`indeks` 3/151 · `perpetual_usd1` 1/2 · `basis_non_fiat` 1/39 · `tak_tergolong` 0/0.
937/21.789 ✅

**Angka warisan yang dicabut:** "16 simbol non-ASCII" adalah HANTU. Terukur **3
nama / 19 bulan**.

## KC-18 — semesta kehidupan (tidak berubah)

Atas **19.586** simbol-bulan lolos: **1.401 MATI** (7,153%), **98 SEPI** (0,500%),
**18.087 HIDUP** (92,35%). Dari 1.401 MATI: 842 kehilangan funding, 559 tetap
berfunding. `cacah_simbol_tanpa_hidup` **18**.

## Delapan simbol bangkit — TERUKUR [v44]

Sumber: `tersisip_semesta.py` V1 run **30514239872** (commit `25106dd5`, kode 0),
laporan blob `911acd1c`, dan `sebab_bangkit.py` V1 run **30517682958** (commit
`3913a054`, kode 0), laporan blob `9d654428`. Keduanya terbaca UTUH.

Delapan simbol dengan `cacah_tersisip` > 0 (seluruhnya `cacah_tersisip ==
cacah_mati == rentetan_mati_terpanjang`):

| simbol | bulan | HIDUP | MATI | tersisip | mati pertama | lubang pertama | selisih | arah |
|---|---:|---:|---:|---:|---|---|---:|---|
| CVCUSDT | 67 | 38 | 29 | 29 | 2022-12 | — | null | tanpa lubang |
| CVXUSDT | 45 | 31 | 13 | 13 | 2024-06 | — | null | tanpa lubang |
| SLPUSDT | 32 | 18 | 13 | 13 | 2024-06 | — | null | tanpa lubang |
| CTKUSDT | 67 | 55 | 11 | 11 | 2024-05 | — | null | tanpa lubang |
| LITUSDT | 64 | 54 | 10 | 10 | 2025-02 | 2025-07 | **+5** | mati dulu |
| TLMUSDT | 60 | 51 | 8 | 8 | 2022-07 | 2021-07 | −12 | lubang dulu (AWAL) |
| ICPUSDT | 62 | 59 | 2 | 2 | 2022-07 | 2021-05 | −14 | lubang dulu (AWAL) |
| MAVIAUSDT | 28 | 25 | 2 | 2 | 2025-01 | — | null | tanpa lubang |

Jumlah tersisip 29+13+13+11+10+8+2+2 = **88** ✅ · `cacah_mati_dulu` **1** ·
`cacah_lubang_dulu` **2** (keduanya bentuk AWAL) · `cacah_tanpa_lubang` **5** ·
`cacah_simbol_hidup_berlubang` **2** (ICPUSDT 13, TLMUSDT 11).

**Catatan tafsir (ADR-A011):** kematian pasar dan lubang funding adalah DUA GEJALA
BERBEDA. Lima dari delapan bangkit tanpa satu pun lubang. LITUSDT satu-satunya
`mati_dulu` (+5 bulan). ICP dan TLM berlubang sejak bulan klines pertama — calon
KC-46.

**Sidik kode `sebab_bangkit` V1 =**
`bafe4359e8f36f0402d4be4a4e4aef4a28f224f6419f06f701fb3a5bf696221a`

## Karantina, bulan ABSEN, H-A015, lubang funding — tidak berubah dari v43

Seluruh angka daftar karantina 12, bulan absen 11, H-A015, lubang 880/877, LITUSDT
urutan peristiwa, BTCSTUSDT 0 HIDUP, H-A013/H-A014, SETTLED 15 pasangan, per-tahun
penyebut, cacah baris V5: sama seperti STATE_LAMPIRAN_UKUR blob `0e9ec378`. Tidak
diulang di sini untuk menghemat ukuran berkas.

## Jumlah uji — terukur

**936** (run 30517682951, commit `3913a054`, kode 0, 2026-07-30T05:49:11Z).
Riwayat: 769 → 814 → 832 → 879 → **936**.

- 769 + 45 (`test_bentangan_kohort.py` V2 63 − V1 45 + 47 `test_anatomi_tengah`) =
  langkah tidak lurus karena V1→V2 mengganti berkas. Yang terukur: trio V2
  menghasilkan **832** (run 30509071199), lalu V2 menggantikan V1 di CI sehingga
  832 − 769 = **63** butir baru dari V2.
- 832 + 47 `test_tersisip_semesta.py` = **879** (run 30514239862, kode 0).
- 879 + 57 `test_sebab_bangkit.py` = **936** ✅

## Modul, workflow, dan berkas uji — diperbarui v44

**`lux_ai/serapan/` — 41 berkas** (dicacah tangan ref `d182de1d`, sebelum push
`sebab_bangkit`):
`__init__.py` `64d85584` · `anatomi_tengah.py` `04279335` · `arsip.py` `0104958b` ·
`bentangan_kohort.py` **`f4eae57a`** V2 · `bentuk_semesta.py` `1f0feb30` ·
`bulan_absen.py` `10279d72` · `bulan_settled.py` `80e8d8bb` · `diagnosa_kc14.py`
`5bd67d15` · `diagnosa_kc14b.py` `bceada11` · `diagnosa_kc14c.py` `ab517db9` ·
`diagnosa_kc15.py` `3642e5b6` · `diagnosa_kc6.py` `0f699854` · `funding.py`
`8d4b1f82` · `funding_cdn.py` `fd624d00` · `gerbang_1m.py` `c8cc54c8` ·
`karantina_semesta.py` `46e7c46b` · `kebangkitan.py` `446321ee` · `kehidupan.py`
`f49abb2b` · `kehidupan_arsip.py` `318a5cb1` · `klines.py` `cc4d9287` ·
`kohort_ekor.py` `c9b63bbe` · `kohort_ringkas.py` `4ae62d5b` · `lubang_tengah.py`
`4d3beaf1` · `pecahan.py` `f1b49f1b` · `penyebut_kc6.py` `7f399244` ·
`penyebut_tahun.py` `265aad00` · `probe.py` `4581639f` · `pulihkan.py` `a9e6eab7` ·
`rentang_kc6.py` `631ec2f3` · `resample.py` `66a4b177` · `rilis.py` `2e44530c` ·
`ringkas_semesta.py` `bc8f7ad7` · `semesta_kuota.py` `7288b030` · `semesta_silang.py`
`ad72f3f2` · `serap.py` `62d4c2c3` · `silang_funding.py` **`42c3aa9d`** V2 ·
`silang_settled.py` `3eea2a80` · `survei.py` `26b14940` · **`tersisip_semesta.py`
`8a648838`** V1 · `uji_resample.py` `f10ec98a` · `ukur_baris.py` `3ebaa9f9`.
Sesudah push `sebab_bangkit`: **42 berkas** (ditambah `sebab_bangkit.py`
**`fd5a1dc4`** V1).

**`.github/workflows/` — 36 berkas** (dicacah tangan ref `d182de1d`):
`anatomi_tengah` `49c452a2` · **`bentangan_kohort` `13f21d1d`** V2 · `bentuk_semesta`
`dc393dd0` · `bulan_absen` `71f76a0f` · `bulan_settled` `9e0829f2` · `ci` `c79497b2` ·
`diagnosa_kc14` `6524646a` · `diagnosa_kc14b` `a315c25b` · `diagnosa_kc14c`
`82126b60` · `diagnosa_kc15` `c5f2ee0f` · `diagnosa_kc6` `6bae2b1b` ·
`funding_semesta` `c1ce55f3` · `karantina_semesta` `de40fa4e` · `kebangkitan`
`282b51aa` · `kehidupan` `3eb10655` · `kehidupan_arsip` `8234e5dc` · `kohort_ekor`
`2e747475` · `lubang_tengah` `557030de` · `pecahan_serapan` `cd9e21d1` ·
`penyebut_kc6` `14617b6b` · `penyebut_tahun` `8f0d5852` · `probe_serapan` `9b356e15` ·
`pulihkan_rilis` `32bd1099` · `rentang_kc6` `db1e77ae` · `ringkas_semesta` `d6145d28` ·
`semesta_kuota` `b7e5a65a` · `semesta_silang` `babf08e4` · `serap_pilot` `85694e0f` ·
`silang_funding` `23f8c870` · `silang_settled` `78d8051c` · `survei_semesta`
`a1fb0192` · `taksonomi_semesta` `b066b4db` · `terhenti_semesta` `baef4f41` ·
**`tersisip_semesta` `abdab4af`** V1 · `uji_resample` `121f3e25` · `ukur_baris`
`f62be605`. Sesudah push `sebab_bangkit`: **37 berkas** (ditambah
`sebab_bangkit.yml`).

**`tests/` — 45 berkas** sesudah push `sebab_bangkit` (dari 42 di v43 + 3 baru:
`test_bentangan_kohort.py` **63** butir blob `(V2, commit 703daa90)` · `test_tersisip_semesta.py` **`61196fd1`** 47 butir · `test_sebab_bangkit.py`
**`3977c11c`** 57 butir). Blob berkas lain sama seperti STATE_LAMPIRAN_UKUR
blob `0e9ec378`.

## API terverifikasi — tambahan v44

API lama (v37–v43) tetap berlaku. Tambahan:

**`bentangan_kohort` V2** (blob `f4eae57a`, 16.925 B, UTUH): `VERSI 2`;
`POLA_BULAN ^\d{4}-\d{2}$`; `POLA_KUNCI ^(?P<simbol>.+?)[\s|/_:.-]*(?P<bulan>\d{4}-\d{2})$`;
fungsi: `pisah_kunci`, `kelompokkan`, `bulan_berstatus`, `mati_tersisip`, `bangkit`,
`rentetan_terpanjang`, `ringkas_simbol`, `uji_r301`, `kendali_positif`, `kendali_sah`,
`kode_keluar`, `jalankan`, `main`. Sidik kode
`8ca6ebbefc3606464ebd7f94c6b51b1fdf500c62779cdcb5700ec2ee4ea9f32c`.

**`tersisip_semesta` V1** (blob `8a648838`, 16.905 B, UTUH): `VERSI 1`;
`KELUARAN "reports/tersisip_semesta.json"`; `PENYEBUT_TERCATAT 19586`;
`SIMBOL_TERCATAT 787`; `MATI_TERCATAT 1401`; `SEPI_TERCATAT 98`;
`HIDUP_TERCATAT 18087`; `R303_PITA_SIMBOL (1,60)`; `R303_PITA_SIMBOL_BULAN (1,300)`;
fungsi: `sidik_kode`, `bulan_tersisip(peta_bulan) -> List[str]`, `tetangga_maju`,
`bulan_tersisip_rapat`, `ringkas_simbol`, `ember`, `himpun`, `kendali_deteksi`,
`dalam_pita`, `uji_r303`, `kode_keluar`, `jalankan`, `main`. Modul TIDAK memuat
kata "USDT". Sidik kode
`9618fd19e4ab2e7b5279177db600f6176afd914ab1e94576e54197f70ebc537c`.

**`sebab_bangkit` V1** (blob `fd5a1dc4`, UTUH): `VERSI 1`;
`KELUARAN "reports/sebab_bangkit.json"`; `TOTAL_PECAHAN = kehidupan_arsip.TOTAL_PECAHAN`;
`PENYEBUT_TERCATAT 19586`; `SIMBOL_TERCATAT 787`; `MATI_TERCATAT 1401`;
`BANGKIT_TERCATAT 8`; `TERSISIP_TERCATAT 88`; `LUBANG_DALAM_PENYEBUT_TERCATAT 877`;
`R304_PITA_MATI_DULU (5,8)`; `R304_PITA_HIDUP_BERLUBANG (3,8)`;
`BERKAS_DICAP` 5 nama (kehidupan, kehidupan_arsip, sebab_bangkit, silang_funding,
tersisip_semesta); fungsi: `sidik_kode`, `indeks_bulan`, `jarak_bulan`, `peta_status`,
`bulan_urut`, `bangkit_lokal`, `tersisip_lokal`, `ringkas`, `ember`, `himpun`,
`kendali_deteksi`, `dalam_pita`, `uji_r304`, `kode_keluar`, `jalankan`, `main`.
Modul TIDAK memuat kata "USDT". Sidik kode
`bafe4359e8f36f0402d4be4a4e4aef4a28f224f6419f06f701fb3a5bf696221a`.

`sidik_data_funding` (funding_semesta.json) =
`2c9fbd1b04f74c9c844bc223a99a103d12220b88d08667b3792720e5b9608d24`.
`sidik_kode_silang_funding` yang seragam di tiga laporan =
`8a9b859c09cd64e30e203e6f8dc53411b8e341c44f112805b3041e5d4d3231b1`.

## Hipotesis

- H-A001 belum diuji · H-A002b GUGUR · H-A003 MENANG pada 3, GUGUR pada 9 ·
  H-A004 tak dapat diuji · H-A005 GUGUR · H-A006 MENANG enam run · H-A008 MENANG
  dua kali · H-A009 GUGUR · H-A010 MENANG 5–0 · **H-A011 MENANG** · H-A012 MENANG
  · **H-A013 MENANG 6–0, TAFSIR DICABUT** · **H-A014 BENTUK BARU MENANG 9 dari 9**
  · **H-A015 MENANG sebagai angka, DIBATASI sebagai tafsir** · H-A016 PENGAMATAN,
  BELUM DIUJI.
- **H-A017 [DIRUMUSKAN ULANG, ADR-A011]:** bunyi lama "kematian pasar mendahului
  berhentinya funding" pada kelas bangkit DICABUT sebagai pola. Bunyi baru: "pada
  LITUSDT, dan sejauh ini HANYA pada LITUSDT di antara delapan simbol bangkit, bulan
  MATI pertama mendahului bulan berlubang funding pertama sebanyak **5 bulan**".
  Penyebutnya **1 dari 8** dan wajib ikut disebut setiap kali angka itu dipakai
  (aturan 74). Belum diuji atas semesta. **Dugaan awal H-A017 tentang ukuran
  byte_parquet sebagai gejala kehidupan (dari jurnal 120)** tetap sebagai
  PENGAMATAN: LITUSDT byte mati ~390–434 ribu lawan hidup ~1,6–1,9 juta; belum
  diuji atas semesta.
