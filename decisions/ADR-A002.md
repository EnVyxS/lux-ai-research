# ADR-A002 — Serapan data arsip Binance USDS-M

Status: DITERIMA SEBAGIAN. Tanggal: 2026-07-28.
Bagian 7 (estimasi ukuran) sengaja kosong sampai run probe mengisinya. Serapan
penuh DILARANG dijalankan sebelum bagian itu terisi dari artefak.

## Konteks

Sandbox agen tidak punya akses jaringan (terverifikasi: penyelesaian DNS ke host
arsip gagal). Maka setiap pengukuran dan setiap unduhan wajib dijalankan oleh
runner GitHub, dan satu-satunya cara agen mengetahui hasilnya adalah artefak
yang di-commit workflow. Ini memperkuat kewajiban pelaporan bertahap.

## Keputusan

### 1. Sumber

Satu-satunya sumber: arsip publik `data.binance.vision`, listing lewat
`https://s3-ap-northeast-1.amazonaws.com/data.binance.vision`, akar prefix
`data/futures/um`. REST `fapi.binance.com` tidak dipakai di jalur mana pun.
Nol koneksi ke bursa.

### 2. Cakupan simbol

Daftar simbol diambil dari INDEKS ARSIP (`monthly/klines/` common prefixes),
bukan dari daftar pair yang masih aktif. Simbol delisting WAJIB ikut. Kode
dilarang menyaring berdasarkan status pair; ada uji yang menegakkannya
(`tests/test_serapan.py::test_semesta_simbol_tidak_menyaring_pair_aktif`).

### 3. Rentang waktu dan interval

- Yang DIUNDUH: `1m` saja, ditambah `fundingRate`.
- Interval lain diturunkan lewat resample dari 1m.
- Pengecualian tunggal: `5m` dan `15m` ASLI untuk 12 simbol probe, semata untuk
  uji integritas resample. Berkas itu DILARANG dipakai backtest mana pun.
- Rentang: seluruh bulan yang tersedia, dari bulan pertama tiap simbol sampai
  bulan terakhir yang sudah tutup. Bulan berjalan tidak diambil.

### 4. Karantina (dipatok SEBELUM serapan)

**N = 7 hari kalender pertama sejak bar sah pertama tiap simbol** dibuang dari
seluruh backtest. Alasan: hari-hari awal listing punya spread lebar, kedalaman
tipis, dan lonjakan ekstrem yang menghasilkan breakout palsu murah. Angka ini
dipatok di muka dan tidak boleh disetel ulang setelah melihat hasil; mengubahnya
memerlukan ADR baru dan membayar N_percobaan.

Dicatat per simbol: `awal_sejati` (bar pertama setelah karantina) dan
`akhir_sejati` (bar sah terakhir).

### 5. Format simpan

Parquet terkompresi zstd, satu berkas per simbol-bulan, kolom kanonik
`open_time, open, high, low, close, volume, close_time, quote_volume, trades,
taker_buy_base, taker_buy_quote`. Baris diurutkan menaik menurut `open_time`;
duplikat dibuang dengan aturan simpan-yang-pertama, dan jumlah yang dibuang
WAJIB tercatat di manifes. Berkas disimpan sebagai aset rilis, bukan di git.

### 6. Verifikasi

Setiap berkas arsip dicocokkan dengan berkas `.CHECKSUM` resminya sebelum
dipakai. Pecahan yang checksum-nya tidak cocok DIANGGAP TIDAK ADA. Manifes per
pecahan memuat nama, jumlah baris, rentang waktu, checksum, dan sumber arsip.

### 7. Estimasi ukuran — MENUNGGU PENGUKURAN

Angka warisan "40-60 GB, sekitar 34.000 berkas" adalah KLAIM yang belum
diverifikasi. Diisi dari `reports/probe_serapan.json`: jumlah simbol semesta,
total berkas bulanan 1m, rerata byte per simbol-bulan (zip dan parquet), serta
estimasi total. Sampai terisi, serapan penuh dilarang.

### 8. Simbol probe (dipilih di muka)

Likuid: BTCUSDT, ETHUSDT, BNBUSDT, SOLUSDT, XRPUSDT, ADAUSDT, DOGEUSDT, LINKUSDT.
Klaim delisting yang diuji: FTTUSDT, SRMUSDT, COCOSUSDT, BTSUSDT. Simbol yang
ternyata tidak ada di indeks arsip dicatat sebagai klaim yang dibantah, bukan
dihapus diam-diam.

Probe condong likuid, jadi ekstrapolasi ukuran darinya adalah BATAS ATAS kasar,
bukan taksiran tengah. Laporan probe menyatakan ini sendiri.

## Konsekuensi

Serapan berjalan sebagai matriks job per pecahan bulan di latar, sementara juri
dibangun di atas 12 simbol probe. Tidak ada hipotesis yang boleh diadjudikasi
sebelum semesta penuh selesai dan manifesnya terverifikasi.
