# STATE — versi 21

Diperbarui: 2026-07-28 (sesi 50). Aturan hanya BERTAMBAH; jangan menulis ulang
dari ingatan. v21 disusun di atas teks v20 (blob
`b8a6a6d2d09cee050c6ab89948a31a37f6bcd724`) yang dibaca UTUH dari `main` pada
sesi ini, ditambah kedelapan laporan pecahan, diagnosa KC-14 dan KC-14b.

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

## Kelas cacat

KC-1 s.d. KC-12 seperti pada v19. KC-10 dan KC-11 DITUTUP (v20). KC-9 teruji
pada berkas nyata. KC-13 (keterwakilan sampel) → penangkalnya aturan 37.

- **KC-14 [v21] — menit hilang NYATA di arsip 1m.** Terukur pada seluruh semesta
  `perpetual_usdt`: **12 dari 19.598** simbol-bulan dijatuhkan gerbang pada
  klausa `tanpa_menit_hilang` + `jarak_60_detik`; total **13.575 menit** hilang
  (0,0000162 dari seluruh menit). Empat klausa lain (`deret_tidak_kosong`,
  `satuan_milidetik`, `selaras_menit`, `tanpa_duplikat`) **nol di kedelapan
  pecahan**, jadi KC-14 adalah menit hilang, BUKAN kerusakan format — ADR-A004
  tidak perlu ditinjau ulang. Sebab lubang **tidak diketahui**; lihat H-A003 dan
  H-A004 di bawah. Kebijakannya ADR-A006: karantina.
- **KC-15 masih DICADANGKAN.** Hanya dipakai bila terbukti berkas HARIAN memuat
  menit yang absen dari berkas BULANAN. Pada tiga tersangka pertama itu TIDAK
  terbukti (diagnosa KC-14b), sembilan sisanya sedang diukur (diagnosa KC-14c).

## Hipotesis

- H-A001: belum diuji.
- H-A002a (bursa berhenti mengutip) / H-A002b (kerusakan satu interval):
  H-A002b **GUGUR** (`slot_5m_hadir_saat_1m_hilang` = 0 pada 5m dan 15m).
- **H-A003 (cacat perakitan arsip BULANAN): GUGUR.** Berkas harian ketiga
  tersangka berisi 1440 − panjang_lubang baris, mulai tepat saat lubang bulanan
  berakhir; harian dan bulanan sepakat menit demi menit
  (`reports/diagnosa_kc14b.json` blob `2f2b179c`, `sidik_kode` `e675a617…`).
- **H-A004 [v21] (cacat di HULU arsip, sebelum pemecahan harian maupun bulanan):
  TIDAK TERUJI dan tidak dapat diuji dengan akses sekarang.** Pemisahnya butuh
  sumber non-arsip; `fapi.binance.com` memberi 451 dari runner. Konsekuensi:
  dilarang menulis "lubang itu jeda pasar" sebagai fakta. Status resmi: sebab
  tidak diketahui, simbol-bulannya dikarantina.

## Papan skor prediksi

R-1..R-99 seperti dirinci v20. R-100..R-103 diadjudikasi di jurnal 47
(R-103 MELESET: nisbah 1,2295 lawan ramalan 1,30..1,60). R-107..R-109 TEPAT
(jurnal 49).

| # | Prediksi | Status |
|---|---|---|
| R-104 | simbol-bulan pecahan 1..7 = 17.187 ± 60; total 19.598 | TEPAT (17.187 / 19.598) |
| R-105 | `simbol_bulan_gagal` pecahan 1..7 di pita 5..60 | TEPAT (9) |
| R-106 | hanya 2 klausa dilanggar; baris_dibuang 0..5 | TEPAT (2 klausa; 0) |
| R-110 | `cacah_hari_tersedia` = 3 | TEPAT |
| R-111 | `menit_hadir_di_harian_saat_bulanan_hilang` = 0 | TEPAT (H-A003 gugur) |
| R-112 | baris harian 780 / 930 / 735 | TEPAT (bukan ramalan mandiri) |

**Total R-1..R-112** (aturan 21): TEPAT **73**; MELESET **26**; SEPARUH **4**;
TIDAK TERADJUDIKASI **3**; MENUNGGU **6** (R-7, R-19, R-20, R-28, R-36, R-37).
73+26+4+3+6 = **112** ✅.

MENUNGGU tambahan yang baru dipra-registrasi (jurnal 50): R-113, R-114, R-115,
R-116 — diagnosa KC-14c. Ramalan berikutnya **R-117**. N_percobaan = 0.

Catatan kejujuran: enam TEPAT beruntun pada sesi 50, tetapi R-104 dibatasi angka
19.598 yang sudah dipatok ADR-A005, pita R-105 sangat lebar, dan R-112 hanyalah
aritmetika turunan R-111. Yang benar-benar berisiko hanya R-106 dan R-111.

## Daftar ADR

- ADR-A001 aturan dasar. DITERIMA.
- ADR-A002 serapan. DITERIMA; §3 DIAMANDEMEN oleh ADR-A004; §9 soal persistensi
  DIGANTI oleh ADR-A006 Keputusan 3.
- ADR-A003 taksonomi rezim. BELUM ADA (nomor dicadangkan).
- ADR-A004 kebijakan KC-6. DITERIMA; berdiri (klausa format nol pelanggaran).
- ADR-A005 jenis instrumen tahap pertama. DITERIMA. 787 simbol, 19.598 bulan —
  **kini terverifikasi dari arsip, bukan dari survei saja**.
- **ADR-A006 nasib simbol-bulan yang dijatuhkan gerbang + persistensi parquet.
  DITERIMA (sesi 48).** Karantina, bukan buang dan bukan tambal; interpolasi,
  forward-fill, dan penurunan ambang DILARANG; parquet dipersistenkan sebagai
  rilis tar terbelah ≤1,8 GB + `SHA256SUMS`. **Belum diterapkan ke kode.**
- ADR berikutnya **A007**.

## Serapan semesta `perpetual_usdt` — TERUKUR PENUH

Sumber: `reports/pecahan_serapan.log` blob `1dc3e929` (pecahan 0, run
`30353584831`, `sidik_kode` `22c17f4f…`) dan `reports/pecahan_1..7.log`
(run `30358650719`, `sidik_kode` seragam `059df499…`, `versi_pecahan` 2,
kode keluar 0 semuanya). `sidik_data` `6128fbb0…` di kedelapan.

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
  **839.855.709**; menit hilang **13.575**.
- Gerbang: lolos **19.586**, gagal **12**, `persen_lolos` semesta **99,9388**.
- 0 gagal unduh, 0 gagal checksum, 0 baris dibuang, 0 simbol gagal didaftar,
  `selisih_cacah_bulan.cacah_simbol_berselisih` = 0, `jenis_instrumen_unik` =
  `[perpetual_usdt]` — di kedelapan pecahan.
- Ukuran: zip **26.532.925.083 B** (26,53 GB); parquet **32.706.262.375 B**
  (32,71 GB); nisbah semesta **1,2327**. Ramalan probe lama (1,51 → 39,17 GB)
  meleset ≈6,5 GB ke atas.
- Kelas risiko gabungan (aturan 37): pra_header 1.952, bulan_awal_2020_2021
  1.889, terhenti 587, non_ascii 19, kendali_baru 10.007. non_ascii KOSONG di
  pecahan 3,4,5,6,7 dan dinyatakan terbuka di `kelas_risiko_kosong`.
- **Parquet tidak bertahan.** `parquet_dipersistenkan: false` di kedelapan
  laporan: ditulis, diukur, dihapus. Sampai ADR-A006 Keputusan 3 diterapkan,
  semesta ini adalah ANGKA tanpa data.

## Daftar karantina ADR-A006 — 12 simbol-bulan (lengkap, bukan sampel)

AERGOUSDT 2025-04 · CVCUSDT 2025-05 · SLPUSDT 2025-07 (pecahan 0) ·
CVXUSDT 2025-07 · MAVIAUSDT 2025-03 · PUMPUSDT 2025-07 (pecahan 1) ·
CTKUSDT 2025-04 (3) · LITUSDT 2025-12 (4) · BNXUSDT 2022-04, 2022-06, 2022-08
(6) · AIAUSDT 2026-01 (7). Semua pada dua klausa yang sama.

Pada tiap pecahan panjang `contoh_gagal` = `simbol_bulan_gagal`, jadi daftar ini
tidak terpotong batas contoh. Menit hilang per pecahan seluruhnya kelipatan 15;
BNXUSDT menyumbang 7.200 menit (5 hari) di tiga bulan 2022 — satu-satunya
tersangka pra-2023 dan satu-satunya yang berulang. **Ini memerlukan verifikasi.**

## Jumlah uji

**141 TERVERIFIKASI** — `reports/ci_terakhir.json` run `30359672326`, commit
`6af0b252`, `kode_keluar: 0`, `"141 tests collected in 0.38s"`. Setelah itu
ditambah `tests/test_diagnosa_kc14c.py` (8 uji) — cacah barunya hanya sah dari
laporan CI berikutnya (aturan 38).

## Utang verifikasi

1-5 dan 11 menunggu tahap juri/klasifikasi. 6-23, 25-28 LUNAS.

24. **AKTIF — sisa pekerjaan bukan pengukuran lagi.** Pengukuran semesta SELESAI
    (787 / 19.598 / 839.842.134). Yang belum:
    - **persistensi** parquet sebagai rilis tar terbelah ≤1,8 GB + `SHA256SUMS`
      (ADR-A006 Keputusan 3) — tanpa ini tiap run mahal hanya menghasilkan angka;
    - medan `karantina`, `cacah_karantina`, `daftar_karantina` di `serap.ringkas`;
    - jalur **funding** (`funding_ada` masih null di seluruh manifes);
    - medan `dugaan_pengganti` (ADR-A005);
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
- Sebab KC-14 (H-A004) — tidak dapat diuji dengan akses sekarang.
- Nisbah parquet/zip: kini 1,2327 atas 19.598 berkas, jadi taksiran probe 1,51
  resmi ditolak; ini bukan lagi keterbatasan sampel (aturan 20 terpenuhi).
