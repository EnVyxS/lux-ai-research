# STATE — versi 23

Diperbarui: 2026-07-28 (sesi 52). Aturan hanya BERTAMBAH; jangan menulis ulang
dari ingatan. v23 disusun di atas teks v22, ditambah
`reports/diagnosa_kc15.json` (run `30369333069`, commit `a360bf11`).

Satu baris v22 kini SALAH dan diperbaiki di sini: kecurigaan bahwa 210 menit
tepi BNXUSDT 2022-04 adalah cacat. Terbukti sah. **KC-16 DITARIK.**

## Aturan bernomor

Aturan 1–36 berlaku tanpa perubahan; teksnya ada di STATE v19 (blob
`e06c486e…`). Ringkas nomornya: 1 satu definisi R · 2 gerbang kandidat ·
3 adjudikasi terkunci · 4-5 modul warisan · 6 hanya arsip publik · 7 sidik wajib ·
8 ≤800 baris · 9 satu jalur eksekusi · 10 diagnostik `bukan_bukti` · 11 biaya
sejak hari pertama · 12 guard struktural · 13-14 tanpa jaringan · 15 kode repo
lain · 16 nama medan jujur · 17 data biaya hilang → keluar · 18 gerbang lolos
wajib bercacah · 19 Decimal · 20 rentang disampel · 21 hitung ulang · 22 cakupan
`sidik_kode` · 23 gerbang merah tak dilonggarkan · 24 medan penggugur ·
25 cakupan dipatok sebelum run · 26 ramalan mutlak butuh besaran · 27 pendamping
tak bersyarat · 28 bulan awal parsial · 29 amandemen tak menghapus · 30 penyebut
eksplisit · 31 `sidik_data` · 32 nama non-ASCII · 33 pemicu sempit · 34 dilarang
add borongan · 35 laporan tanpa sidik hanya petunjuk · 36 dua angka beda →
definisi berdampingan.

37. **[v20]** Sampel yang dipakai menguji sebuah jalur wajib memuat sedikitnya
    satu kasus dari tiap kelas cacat yang diketahui relevan, dan laporan wajib
    menyebut kelas mana yang tersentuh dan mana yang tidak, walau cacahnya nol.
38. **[v21]** Cacah uji hanya sah dari `reports/ci_terakhir.json` (run id +
    commit + `kode_keluar`). Penjumlahan taksiran dilarang ditulis sebagai angka
    uji. Lahir dari selisih 135 lawan **141**.
39. **[v22]** Keseragaman yang terukur pada sampel DILARANG dipakai sebagai
    angka ramalan untuk anggota di luar sampel; wajib pita atau kemungkinan
    campuran. Lahir dari R-114.
40. **[v22]** Tiap laporan yang mencacah baris sebuah simbol-bulan wajib memuat
    uji silang `baris + hilang_di_tengah + tepi = menit_kalender` dan melaporkan
    selisihnya walau nol. Lahir dari 210 menit BNXUSDT 2022-04. **Sudah terbukti
    berguna:** medan `cacah_selisih_tak_terjelaskan` = 0 pada 38 sampel langsung
    membuktikan tepi = 210 tanpa membaca rincian.
41. **[v23]** Ramalan bersyarat yang penyebutnya nol dicatat TIDAK
    TERADJUDIKASI, bukan TEPAT, dan status itu wajib dipra-registrasikan bersama
    ramalannya. Lahir dari R-120.
42. **[v23]** Kelas cacat baru DILARANG dinamai atas dasar satu angka yang
    belum diukur langsung. Tuduhan ditulis sebagai hipotesis + run, bukan
    sebagai kelas. Lahir dari KC-16 yang ditarik: satu angka (210) hampir
    menjadi salah-tuduh ketujuh.

## Kelas cacat

KC-1 s.d. KC-12 seperti pada v19. KC-10 dan KC-11 DITUTUP (v20). KC-13
(keterwakilan sampel) → penangkalnya aturan 37.

- **KC-14 [v21, dipersempit v22] — menit hilang NYATA di arsip 1m, hadir di
  KEDUA representasi.** **9** simbol-bulan, **6.375 menit** (425×15). Berkas
  HARIAN memuat tepat `1440 − panjang_lubang` baris dan mulai persis saat lubang
  bulanan berakhir. Sebab tidak diketahui (H-A004, tak dapat diuji). Kebijakan:
  karantina (ADR-A006).
- **KC-15 [v22] — TERBUKTI: berkas klines BULANAN dapat kehilangan HARI UTC
  penuh yang datanya utuh di berkas HARIAN.** **3** simbol-bulan, semuanya
  BNXUSDT 2022 (2022-04, 2022-06, 2022-08), **7.200 menit = 5×1440**, tiap
  berkas harian 1.440 baris penuh dengan checksum terverifikasi. Sumber:
  `reports/diagnosa_kc14c.json` blob `a3e8f675`, run `30367836338`, `sidik_kode`
  `487d93c0…`. Kebijakan: ADR-A007 (pemulihan dari harian).
  **Bentuknya kini lebih sempit:** KC-15 melenyapkan hari penuh di TENGAH bulan
  dan TIDAK pernah memotong tepi bulan pada 37 bulan tengah yang diperiksa.
- 9 + 3 = **12** karantina; 6.375 + 7.200 = **13.575** menit — cocok dengan
  total semesta lewat jalur berbeda ✅.
- **KC-16 DITARIK [v23].** Nomornya dicadangkan dan TIDAK terpakai. Dugaan
  "gerbang buta terhadap tepi bulan" GUGUR: 210 menit BNXUSDT 2022-04 adalah
  awal pengutipan yang sah di bulan PERTAMA simbol itu di arsip (aturan 28), dan
  berkas harian 2022-04-01 sepakat tidak memuat menit sebelum itu.
  `gerbang_1m.py` sudah dibaca dan tidak cacat.

## Hipotesis

- H-A001: belum diuji.
- H-A002a / H-A002b: H-A002b **GUGUR** (`slot_5m_hadir_saat_1m_hilang` = 0).
- **H-A003 (cacat perakitan arsip BULANAN): MENANG pada 3, GUGUR pada 9.**
  `menit_hadir_di_harian_saat_bulanan_hilang` = 7.200 pada BNXUSDT 2022-04/06/08
  (`cacah_mendukung_h_a003` 3, `cacah_h_a003_gugur` 6).
- **H-A004 (cacat di HULU arsip): TIDAK TERUJI dan tidak dapat diuji** dengan
  akses sekarang (`fapi.binance.com` → 451). Berlaku untuk 9 kasus KC-14.
  Dilarang menulis "lubang itu jeda pasar" sebagai fakta.
- **H-A005 (KC-15 juga memotong TEPI bulan dan lolos gerbang): GUGUR pada
  rentang yang disampel [v23].** 37 bulan TENGAH dari kedelapan pecahan,
  `cacah_bulan_tepi_tak_nol` = 0, `total_menit_tepi` = 0,
  `cacah_gerbang_lolos_padahal_tepi_terpotong` = 0 — nol karena pembilangnya
  nol, bukan karena gerbangnya tajam (aturan 30). Tidak dapat diperluas ke
  19.586 (aturan 20).

## Papan skor prediksi

R-1..R-99 dirinci v20. R-100..R-103 di jurnal 47 (R-103 MELESET). R-104..R-112
di jurnal 50 (semuanya TEPAT). R-113..R-116 di jurnal 51 (R-114 MELESET).

| # | Prediksi | Status |
|---|---|---|
| R-117 | BNXUSDT 2022-04 tepi = 210 dan 210 hadir di harian | **MELESET** (tepi 210 ✅, hadir 0 — bulan pertama arsip, sah) |
| R-118 | cacah bulan tengah bertepi tak nol di pita 0..6 | TEPAT (0 dari 37; pita longgar) |
| R-119 | total menit tepi 0..1.200 | TEPAT (0; pita longgar) |
| R-120 | bila R-118 > 0 maka menit tepi hadir di harian > 0 | TIDAK TERADJUDIKASI (penyebut nol) |

**Total R-1..R-120** (aturan 21): TEPAT **78**; MELESET **28**; SEPARUH **4**;
TIDAK TERADJUDIKASI **4**; MENUNGGU **6** (R-7, R-19, R-20, R-28, R-36, R-37).
78+28+4+4+6 = **120** ✅. Ramalan berikutnya **R-121**. N_percobaan = 0.

Catatan kejujuran: dua sesi berturut-turut, ramalan yang benar-benar berisiko
meleset (R-114, R-117) sementara yang berpita longgar tepat. Pita longgar tidak
mengajari apa pun; dua MELESET itu masing-masing menghasilkan satu kelas cacat
baru (KC-15) dan satu pembatalan tuduhan (KC-16).

## Daftar ADR

- ADR-A001 aturan dasar. DITERIMA.
- ADR-A002 serapan. DITERIMA; §3 DIAMANDEMEN oleh ADR-A004 lalu ADR-A007;
  §9 DIGANTI oleh ADR-A006 Keputusan 3.
- ADR-A003 taksonomi rezim. BELUM ADA (nomor dicadangkan).
- ADR-A004 kebijakan KC-6. DITERIMA; **berdiri dengan enam klausa.** Klausa
  ketujuh soal tepi TIDAK ditambahkan — tidak ada kasus yang menuntutnya
  (aturan 42).
- ADR-A005 jenis instrumen tahap pertama. DITERIMA.
- **ADR-A006** karantina + persistensi. DITERIMA. **SEBAGIAN DITERAPKAN:**
  `rilis.py` (`PengemasBerbelah`, batas 1,8 GB, `SHA256SUMS`, `verifikasi()`)
  dan `serap.py` Versi 3 (medan karantina + parquet karantina). **BELUM:**
  menyambungkan pengemas ke `pecahan.py` dan mengunggah aset rilis.
- **ADR-A007 serapan hibrida. DIUSULKAN**; cakupannya cukup dan TIDAK perlu
  diperluas ke tepi bulan (H-A005 gugur). Gerbang dijalankan ULANG tanpa
  pelunakan ambang; tiap baris membawa `sumber_baris`.
- ADR berikutnya **A008**.

## Serapan semesta `perpetual_usdt` — TERUKUR PENUH

Sumber: `reports/pecahan_serapan.log` blob `1dc3e929` (pecahan 0, run
`30353584831`) dan `reports/pecahan_1..7.log` (run `30358650719`, `sidik_kode`
seragam `059df499…`, `versi_pecahan` 2, kode keluar 0). `sidik_data`
`6128fbb0…` di kedelapan.

| i | simbol | simbol-bulan | baris | menit hilang | gagal | nisbah |
|---|---|---|---|---|---|---|
| 0 | 99 | 2.411 | 103.264.917 | 1.875 | 3 | 1,2295 |
| 1 | 99 | 2.468 | 105.765.980 | 2.160 | 3 | 1,2268 |
| 2 | 99 | 2.337 | 100.058.416 | 0 | 0 | 1,2293 |
| 3 | 98 | 2.154 | 91.884.319 | 615 | 1 | 1,2356 |
| 4 | 98 | 2.497 | 106.865.397 | 1.050 | 1 | 1,2327 |
| 5 | 98 | 2.741 | 117.671.896 | 0 | 0 | 1,2341 |
| 6 | 98 | 2.652 | 114.013.851 | 7.200 | 3 | 1,2399 |
| 7 | 98 | 2.338 | 100.317.358 | 675 | 1 | 1,2334 |

- Simbol **787**; simbol-bulan **19.598**; baris **839.842.134**; slot
  **839.855.709**; menit hilang **13.575** = 6.375 (KC-14) + 7.200 (KC-15).
- Gerbang: lolos **19.586**, gagal **12**, `persen_lolos` **99,9388**.
- 0 gagal unduh, 0 gagal checksum, 0 baris dibuang, 0 simbol gagal didaftar,
  `cacah_simbol_berselisih` = 0, `jenis_instrumen_unik` = `[perpetual_usdt]`.
- Zip **26.532.925.083 B**; parquet **32.706.262.375 B**; nisbah **1,2327**.
- Kelas risiko: pra_header 1.952, bulan_awal_2020_2021 1.889, terhenti 587,
  non_ascii 19, kendali_baru 10.007.
- **Parquet tidak bertahan.** `parquet_dipersistenkan: false` di kedelapan
  laporan. Semesta ini masih ANGKA tanpa data.
- **Batas kesahihan:** hari yang lenyap penuh dari berkas bulanan SELALU
  melanggar `tanpa_menit_hilang`, jadi 19.586 yang lolos tidak dapat
  menyembunyikan hari dalaman yang hilang. Untuk TEPI bulan, 37 sampel bulan
  tengah bersih seluruhnya — tetapi itu 37, bukan 19.586.

## Daftar karantina ADR-A006 — 12 simbol-bulan, dua sebab

**KC-14 (9, lubang nyata di kedua representasi, 6.375 menit):**
AERGOUSDT 2025-04 (660) · CVCUSDT 2025-05 (510) · SLPUSDT 2025-07 (705) [P0] ·
CVXUSDT 2025-07 (690) · MAVIAUSDT 2025-03 (1.020) · PUMPUSDT 2025-07 (450) [P1] ·
CTKUSDT 2025-04 (615) [P3] · LITUSDT 2025-12 (1.050) [P4] ·
AIAUSDT 2026-01 (675) [P7]. Jumlah = **6.375** ✅

**KC-15 (3, hari penuh hilang hanya di bulanan, 7.200 menit, DAPAT DIPULIHKAN):**
BNXUSDT 2022-04 (1.440) · 2022-06 (1.440) · 2022-08 (4.320) [P6].

Kedua belas melanggar dua klausa yang sama (`tanpa_menit_hilang` +
`jarak_60_detik`), satu blok tunggal, semua mulai tepat 00:00 UTC, semua
kelipatan 15 menit — 12 dari 12. `contoh_gagal` = `simbol_bulan_gagal` di tiap
pecahan, jadi daftar ini tidak terpotong batas contoh.

**Selisih 210 menit BNXUSDT 2022-04: TERJELASKAN dan SAH.** 41.550 + 1.440 +
210 = 43.200 ✅. 2022-04 adalah bulan PERTAMA BNXUSDT di arsip; pengutipan mulai
3,5 jam setelah tengah malam 1 April 2022, dan berkas harian 2022-04-01 sepakat
(`menit_tepi_hadir_di_harian` = 0). Bukan cacat (aturan 28).

## Jumlah uji

**141 TERVERIFIKASI** — `reports/ci_terakhir.json` run `30359672326`, commit
`6af0b252`, `kode_keluar` 0, `"141 tests collected in 0.38s"`. Sesudah itu
ditambahkan `tests/test_diagnosa_kc14c.py`, `tests/test_rilis.py`,
`tests/test_karantina_a006.py`, `tests/test_diagnosa_kc15.py`. Cacah barunya
hanya sah dari laporan CI berikutnya (aturan 38).

## Utang verifikasi

1-5 dan 11 menunggu tahap juri/klasifikasi. 6-23, 25-28 LUNAS.

24. **AKTIF.** Pengukuran semesta SELESAI. Yang belum:
    - **persistensi**: `rilis.py` ada dan berpengujian, belum tersambung ke
      `pecahan.py`, belum mengunggah aset rilis — **satu-satunya penghalang
      agar data serapan bertahan**;
    - medan karantina di `serap.py` — **SUDAH ADA** (Versi 3);
    - jalur **funding** (`funding_ada` null di seluruh manifes);
    - medan `dugaan_pengganti` (ADR-A005);
    - pemulihan harian ADR-A007 (`sumber_baris`, `cacah_baris_dipulihkan`);
    - karantina artefak 7 hari.
    Mengadjudikasi R-7, R-19, R-20, R-36, R-37.

## Temuan sampingan yang belum diukur

- Jalur funding: nol kali diuji.
- 15 `SETTLED` lain: apakah punya pendahulu seperti SXPUSDT?
- Daftar `INDEKS` hanya tiga nama, disusun manual.
- Saham dan komoditas token masih terhitung `perpetual_usdt`.
- `.decode("utf-8","replace")` di `klines` membungkam byte rusak.
- Apakah BUSD/USDC layak digabung dengan USDT.
- **Keamanan `arsip.bulan_tersedia` untuk simbol Tionghoa: TERUKUR pada tiga
  simbol** (`币安人生USDT` 2026-02, `我踏马来了USDT` 2026-04, `龙虾USDT` 2026-05) —
  pendaftaran, unduhan, checksum, pembacaan zip lolos semua. Sisa 16 simbol
  non-ASCII belum.
- Sebab KC-14 pada 9 kasus (H-A004) — tidak dapat diuji.
- **Sebab KC-15 tidak diketahui.** Ketiganya BNXUSDT 2022, satu-satunya simbol
  pra-2023 di antara dua belas karantina dan satu-satunya yang berulang. Khas
  simbol, khas 2022, atau tersebar: belum terukur.
- **Selisih penyebut diagnosa KC-15: 38 diperiksa, 41 dirancang.** Tiga simbol
  hilang tanpa medan yang mencatat sebabnya (dugaan: daftar bulan ≤2 sehingga
  tak ada bulan tengah). Ini memerlukan verifikasi; cacat pelaporan, bukan
  cacat data.
