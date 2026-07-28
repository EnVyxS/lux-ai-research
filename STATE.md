# STATE — versi 22

Diperbarui: 2026-07-28 (sesi 51). Aturan hanya BERTAMBAH; jangan menulis ulang
dari ingatan. v22 disusun di atas teks v21 (blob
`ad969f7ea7a05fa45578b82d3033be43f3fe5e13`) yang dibaca UTUH dari `main` pada
sesi ini, ditambah `reports/diagnosa_kc14c.json` dan pembacaan
`lux_ai/serapan/gerbang_1m.py`.

Dua baris v21 kini SALAH dan diperbaiki di sini: "KC-15 masih DICADANGKAN" dan
"H-A003 GUGUR". Keduanya benar untuk tiga tersangka pertama dan salah untuk
sembilan berikutnya. Aturan 29: yang lama tidak dihapus, statusnya dipersempit.

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
    satu kasus dari tiap kelas cacat yang diketahui relevan bagi jalur itu, dan
    laporan wajib menyebut kelas mana yang tersentuh dan mana yang tidak, walau
    cacahnya nol. Lahir dari KC-13.

38. **[v21]** Cacah uji hanya sah dari `reports/ci_terakhir.json` (run id +
    commit + `kode_keluar`). Penjumlahan taksiran dilarang ditulis sebagai
    angka uji, bahkan dengan kata "perkiraan". Lahir dari selisih 135 (taksiran
    STATE v20 / PROMPT v22) lawan **141** (run `30359672326`).

39. **[v22]** Keseragaman yang terukur pada sampel DILARANG dipakai sebagai
    angka ramalan untuk anggota di luar sampel. Bila tiga kasus pertama
    seragam, ramalan untuk sembilan berikutnya wajib menyebut pita atau
    kemungkinan campuran, bukan nilai tunggal hasil perluasan. Lahir dari
    R-114: nol pada tiga tersangka KC-14b diperluas menjadi "nol untuk
    kesembilan", padahal tiga di antaranya bernilai 7.200. Ini aturan 20 yang
    dilanggar di dalam angka ramalan, bukan di dalam kesimpulan.

40. **[v22]** Tiap laporan yang mencacah baris sebuah simbol-bulan wajib
    memuat uji silang aritmetika terhadap menit KALENDER bulan itu
    (`baris + hilang_di_tengah + tepi = menit_kalender`) dan melaporkan
    selisihnya walau nol. Lahir dari BNXUSDT 2022-04: 41.550 + 1.440 = 42.990
    sementara April punya 43.200 menit; 210 menit tak terpertanggungjawabkan
    baru terlihat setelah hitung ulang manual, bukan dari medan laporan.

## Kelas cacat

KC-1 s.d. KC-12 seperti pada v19. KC-10 dan KC-11 DITUTUP (v20). KC-9 teruji
pada berkas nyata. KC-13 (keterwakilan sampel) → penangkalnya aturan 37.

- **KC-14 [v21, dipersempit v22] — menit hilang NYATA di arsip 1m, hadir di
  KEDUA representasi.** Terukur pada **9** simbol-bulan; **6.375 menit**
  (6.375 = 425×15). Untuk kesembilan, berkas HARIAN memuat tepat
  `1440 − panjang_lubang` baris dan mulai persis saat lubang bulanan berakhir:
  harian dan bulanan sepakat menit demi menit. Sebab **tidak diketahui**; lihat
  H-A004. Kebijakan: karantina (ADR-A006).
- **KC-15 [v22] — DINAMAI, TERBUKTI: berkas klines BULANAN dapat kehilangan
  hari UTC penuh yang datanya utuh di berkas HARIAN.** Terukur pada **3**
  simbol-bulan, semuanya BNXUSDT 2022: 2022-04 (2022-04-17), 2022-06
  (2022-06-09), 2022-08 (2022-08-10, -11, -12). **7.200 menit = 5×1440**, tiap
  berkas harian memuat 1.440 baris penuh dengan checksum terverifikasi.
  Sumber: `reports/diagnosa_kc14c.json` blob `a3e8f675`, run `30367836338`,
  commit `f3096288`, `sidik_kode` `487d93c0…`, `kode_keluar` 0.
  Kebijakan: ADR-A007 (pemulihan dari berkas harian).
- 9 + 3 = **12** simbol-bulan karantina, dan 6.375 + 7.200 = **13.575** menit —
  cocok dengan total semesta yang dihitung lewat jalur berbeda ✅.
- **KC-16 BELUM DINAMAI.** Dicadangkan untuk pemotongan TEPI bulan yang lolos
  gerbang. Petunjuknya satu kasus (BNXUSDT 2022-04, 210 menit) dan sedang
  diukur; jangan dipakai sebelum laporan tepi ada. `gerbang_1m.py` SUDAH dibaca
  dan ia tidak cacat: `ukur_deret` sengaja mengukur dari stempel pertama sampai
  terakhir yang ada, dengan alasan tertulis bahwa bulan pertama sebuah simbol
  memang mulai di tengah bulan (aturan 28). Yang belum diketahui adalah
  akibatnya pada bulan TENGAH.

## Hipotesis

- H-A001: belum diuji.
- H-A002a (bursa berhenti mengutip) / H-A002b (kerusakan satu interval):
  H-A002b **GUGUR** (`slot_5m_hadir_saat_1m_hilang` = 0 pada 5m dan 15m).
- **H-A003 (cacat perakitan arsip BULANAN): MENANG pada 3 simbol-bulan, GUGUR
  pada 9.** v21 mencatatnya GUGUR berdasarkan tiga tersangka pertama saja; itu
  benar untuk ketiganya dan salah sebagai putusan umum. Bukti kemenangan:
  `menit_hadir_di_harian_saat_bulanan_hilang` = **7.200** pada BNXUSDT 2022-04,
  2022-06, 2022-08 (`cacah_mendukung_h_a003` = 3, `cacah_h_a003_gugur` = 6).
- **H-A004 [v21] (cacat di HULU arsip): TIDAK TERUJI dan tidak dapat diuji
  dengan akses sekarang.** Pemisahnya butuh sumber non-arsip;
  `fapi.binance.com` memberi 451 dari runner. Berlaku untuk 9 kasus KC-14 yang
  tersisa. Dilarang menulis "lubang itu jeda pasar" sebagai fakta.
- **H-A005 [v22] (KC-15 juga memotong TEPI bulan, dan pemotongan itu lolos
  gerbang): SEDANG DIUJI** oleh `lux_ai/serapan/diagnosa_kc15.py`, ramalan
  R-117..R-120.

## Papan skor prediksi

R-1..R-99 seperti dirinci v20. R-100..R-103 diadjudikasi di jurnal 47
(R-103 MELESET). R-104..R-112 diadjudikasi di jurnal 50 (semuanya TEPAT).

| # | Prediksi | Status |
|---|---|---|
| R-113 | total menit hilang 9 tersangka = 11.700, rincian per pecahan | TEPAT (11.700; 2.160/615/1.050/7.200/675) |
| R-114 | `menit_hadir_di_harian_saat_bulanan_hilang` = 0 untuk kesembilan | **MELESET (7.200 pada 3 → KC-15)** |
| R-115 | ≥6 dari 9 blok mulai 00:00 UTC; ≥8 dari 9 kelipatan 15 | TEPAT (9 dan 9) |
| R-116 | `cacah_hari_tidak_tersedia` = 0 | TEPAT (0; `hari_diperiksa` 11) |

**Total R-1..R-116** (aturan 21): TEPAT **76**; MELESET **27**; SEPARUH **4**;
TIDAK TERADJUDIKASI **3**; MENUNGGU **6** (R-7, R-19, R-20, R-28, R-36, R-37).
76+27+4+3+6 = **116** ✅.

MENUNGGU tambahan yang dipra-registrasi di jurnal 51: R-117 (BNXUSDT 2022-04
tepi = 210 dan hadir di harian), R-118 (cacah bulan tengah bertepi tak nol di
pita 0..6 dari 40 sampel), R-119 (total menit tepi 0..1.200), R-120 (gerbang
meloloskan bulan bertepi terpotong bila R-118 > 0; bila R-118 = 0 maka TIDAK
TERADJUDIKASI, bukan TEPAT). Ramalan berikutnya **R-121**. N_percobaan = 0.

Catatan kejujuran: deret enam TEPAT beruntun putus pada R-114, satu-satunya
ramalan sesi 51 yang benar-benar berisiko. R-113 hanya penjumlahan angka
gerbang yang sudah dibaca, dan pita R-115/R-116 longgar. Lahir aturan 39.

## Daftar ADR

- ADR-A001 aturan dasar. DITERIMA.
- ADR-A002 serapan. DITERIMA; §3 DIAMANDEMEN oleh ADR-A004, lalu DIAMANDEMEN
  LAGI oleh ADR-A007 (sumber berkas); §9 soal persistensi DIGANTI oleh ADR-A006
  Keputusan 3.
- ADR-A003 taksonomi rezim. BELUM ADA (nomor dicadangkan).
- ADR-A004 kebijakan KC-6. DITERIMA; berdiri (klausa format nol pelanggaran).
  Kemungkinan bertambah klausa ketujuh bila R-118/R-120 menang.
- ADR-A005 jenis instrumen tahap pertama. DITERIMA. 787 simbol, 19.598 bulan,
  terverifikasi dari arsip.
- **ADR-A006** karantina + persistensi parquet. DITERIMA (sesi 48).
  **SEBAGIAN DITERAPKAN (sesi 51):** `lux_ai/serapan/rilis.py`
  (`PengemasBerbelah`, batas 1,8 GB, `SHA256SUMS`, `verifikasi()`) dan
  `serap.py` Versi 3 (`karantina`, `parquet_karantina`, `cacah_karantina`,
  `daftar_karantina`, `cacah_dibuang`/`cacah_ditambal` sebagai medan penggugur,
  pohon `data/parquet_karantina/`). **BELUM:** menyambungkan pengemas ke
  `pecahan.py` dan mengunggah tar sebagai aset rilis.
- **ADR-A007 [v22] serapan hibrida: bulanan sebagai dasar, harian sebagai
  pemulih terverifikasi checksum. DIUSULKAN**, menunggu R-117..R-120. Gerbang
  dijalankan ULANG tanpa pelunakan ambang; tiap baris membawa `sumber_baris`.
- ADR berikutnya **A008**.

## Serapan semesta `perpetual_usdt` — TERUKUR PENUH

Sumber: `reports/pecahan_serapan.log` blob `1dc3e929` (pecahan 0, run
`30353584831`) dan `reports/pecahan_1..7.log` (run `30358650719`, `sidik_kode`
seragam `059df499…`, `versi_pecahan` 2, kode keluar 0 semuanya). `sidik_data`
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
- Gerbang: lolos **19.586**, gagal **12**, `persen_lolos` semesta **99,9388**.
- 0 gagal unduh, 0 gagal checksum, 0 baris dibuang, 0 simbol gagal didaftar,
  `selisih_cacah_bulan.cacah_simbol_berselisih` = 0, `jenis_instrumen_unik` =
  `[perpetual_usdt]` — di kedelapan pecahan.
- Ukuran: zip **26.532.925.083 B** (26,53 GB); parquet **32.706.262.375 B**
  (32,71 GB); nisbah semesta **1,2327**.
- Kelas risiko gabungan (aturan 37): pra_header 1.952, bulan_awal_2020_2021
  1.889, terhenti 587, non_ascii 19, kendali_baru 10.007.
- **Parquet tidak bertahan.** `parquet_dipersistenkan: false` di kedelapan
  laporan. Sampai pengemas tersambung ke `pecahan.py`, semesta ini adalah ANGKA
  tanpa data.
- **Batas kesahihan yang perlu diingat:** hari yang lenyap penuh dari berkas
  bulanan SELALU melanggar `tanpa_menit_hilang`, jadi 19.586 yang lolos tidak
  dapat menyembunyikan hari dalaman yang hilang. Yang belum terjamin adalah
  TEPI bulan; itu yang diukur diagnosa KC-15.

## Daftar karantina ADR-A006 — 12 simbol-bulan, kini terpisah dua sebab

**KC-14 (9, lubang nyata di kedua representasi, 6.375 menit):**
AERGOUSDT 2025-04 (660) · CVCUSDT 2025-05 (510) · SLPUSDT 2025-07 (705)
[pecahan 0] · CVXUSDT 2025-07 (690) · MAVIAUSDT 2025-03 (1.020) ·
PUMPUSDT 2025-07 (450) [1] · CTKUSDT 2025-04 (615) [3] ·
LITUSDT 2025-12 (1.050) [4] · AIAUSDT 2026-01 (675) [7].
660+510+705+690+1.020+450+615+1.050+675 = **6.375** ✅

**KC-15 (3, hari penuh hilang hanya di bulanan, 7.200 menit, DAPAT DIPULIHKAN):**
BNXUSDT 2022-04 (1.440) · 2022-06 (1.440) · 2022-08 (4.320) [pecahan 6].

Seluruh dua belas melanggar dua klausa yang sama (`tanpa_menit_hilang` +
`jarak_60_detik`), tiap kasus satu blok tunggal, semua blok mulai tepat 00:00
UTC, semua panjang kelipatan 15 menit — 12 dari 12. Pada tiap pecahan panjang
`contoh_gagal` = `simbol_bulan_gagal`, jadi daftar ini tidak terpotong batas
contoh.

**Selisih yang belum terjelaskan:** BNXUSDT 2022-04 punya 41.550 baris +
1.440 menit lubang = 42.990, sedangkan April punya 43.200 menit → **210 menit**
(14×15) di tepi bulan, tak terlihat gerbang maupun penghitung lubang. Delapan
simbol-bulan karantina lain pas tanpa sisa. **Ini memerlukan verifikasi**
(diagnosa KC-15, R-117).

## Jumlah uji

**141 TERVERIFIKASI** — `reports/ci_terakhir.json` run `30359672326`, commit
`6af0b252`, `kode_keluar: 0`, `"141 tests collected in 0.38s"`. Sesudah itu
ditambahkan `tests/test_diagnosa_kc14c.py`, `tests/test_rilis.py`,
`tests/test_karantina_a006.py`, `tests/test_diagnosa_kc15.py`. Cacah barunya
hanya sah dari laporan CI berikutnya (aturan 38) — jangan tulis jumlahnya di
sini sebelum itu.

## Utang verifikasi

1-5 dan 11 menunggu tahap juri/klasifikasi. 6-23, 25-28 LUNAS.

24. **AKTIF.** Pengukuran semesta SELESAI (787 / 19.598 / 839.842.134). Yang
    belum:
    - **persistensi**: pengemas `rilis.py` sudah ada dan berpengujian, tetapi
      belum tersambung ke `pecahan.py` dan belum mengunggah aset rilis;
    - medan `karantina`, `cacah_karantina`, `daftar_karantina` — **SUDAH ADA**
      di `serap.py` Versi 3;
    - jalur **funding** (`funding_ada` masih null di seluruh manifes);
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
- Keamanan `arsip.bulan_tersedia` untuk simbol Tionghoa.
- Sebab KC-14 pada 9 kasus (H-A004) — tidak dapat diuji dengan akses sekarang.
- **Sebab KC-15 tidak diketahui.** Ketiganya BNXUSDT 2022, satu-satunya simbol
  pra-2023 di antara dua belas karantina dan satu-satunya yang berulang. Apakah
  KC-15 khas simbol, khas tahun 2022, atau tersebar: belum terukur.
- Apakah KC-15 juga memotong tepi bulan (H-A005) — sedang diukur.
- Berapa banyak bulan TENGAH di antara 19.586 yang lolos punya tepi tak nol —
  sedang diukur atas 40 sampel; kesimpulan tidak boleh diperluas (aturan 20).
