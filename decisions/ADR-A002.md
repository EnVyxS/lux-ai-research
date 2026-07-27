# ADR-A002 — Serapan data arsip Binance USDS-M

Status: DITERIMA. Tanggal keputusan: 2026-07-28.
Bagian 7 diisi pada 2026-07-28 dari `reports/probe_serapan.json`
(run 30312616216, commit `55837eac88bf293933f61c91ec5ab2a54695882d`,
`kode_keluar: 0`, `sidik_kode`
`3198f33836635821a1470399e141b0039a5b6eff2977dd686107031fb74b6e01`).
Serapan penuh kini DIIZINKAN, dengan syarat pemecahan pada bagian 9.

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

TERVERIFIKASI oleh run probe: listing dari endpoint itu berhasil untuk 937
simbol tanpa satu pun kegagalan (`simbol_gagal_listing: []`).

### 2. Cakupan simbol

Daftar simbol diambil dari INDEKS ARSIP (`monthly/klines/` common prefixes),
bukan dari daftar pair yang masih aktif. Simbol delisting WAJIB ikut. Kode
dilarang menyaring berdasarkan status pair; ada uji yang menegakkannya
(`tests/test_serapan.py::test_semesta_simbol_tidak_menyaring_pair_aktif`).

TERVERIFIKASI: 937 simbol di indeks, jauh di atas jumlah pair aktif; simbol
dengan data berhenti di 2024-05 ikut terbawa.

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

Catatan pengukuran: parquet zstd ternyata LEBIH BESAR daripada zip CSV aslinya
(rerata 1.797.488 byte lawan 1.186.859 byte, sekitar 1,51 kali). Format tetap
dipertahankan karena yang dibeli adalah kecepatan baca berkolom dan tipe data
yang pasti, bukan penghematan ruang. Keputusan ini kini sadar-biaya, bukan
asumsi.

### 6. Verifikasi

Setiap berkas arsip dicocokkan dengan berkas `.CHECKSUM` resminya sebelum
dipakai. Pecahan yang checksum-nya tidak cocok DIANGGAP TIDAK ADA. Manifes per
pecahan memuat nama, jumlah baris, rentang waktu, checksum, dan sumber arsip.

TERVERIFIKASI: 12 dari 12 unduhan probe cocok checksum-nya
(`checksum_cocok: true`), termasuk simbol yang datanya berhenti 2024.

### 7. Estimasi ukuran — TERISI DARI PENGUKURAN

Sumber: `reports/probe_serapan.json`, run 30312616216, 2026-07-27T23:09:15Z.

| Besaran | Nilai terukur |
|---|---|
| Simbol di indeks arsip | 937 |
| Simbol gagal listing | 0 |
| Total berkas bulanan 1m | 21.789 |
| Rerata bulan per simbol | 23,3 |
| Rerata byte zip per simbol-bulan | 1.186.859 |
| Rerata byte parquet zstd per simbol-bulan | 1.797.488 |
| Estimasi total zip | 25,86 GB |
| Estimasi total parquet zstd | 39,17 GB |

Kedua estimasi adalah BATAS ATAS kasar: rerata diambil dari probe yang condong
likuid, sedangkan semesta penuh banyak memuat simbol tipis yang berkasnya jauh
lebih kecil (bandingkan BTCUSDT 1.838.455 byte dengan BTSUSDT 208.201 byte pada
bulan penuh).

Klaim warisan "40-60 GB, sekitar 34.000 berkas" DIBANTAH pada cacah berkas:
yang ada 21.789 berkas bulanan 1m, sekitar 36 persen lebih sedikit. Pada ukuran,
bahkan batas atas parquet (39,17 GB) jatuh di bawah pangkal kisaran warisan.

Biaya funding dapat diabaikan: berkas `fundingRate` bulanan berkisar 620-987
byte, jadi seluruh semesta di bawah 25 MB.

### 8. Simbol probe (dipilih di muka)

Likuid: BTCUSDT, ETHUSDT, BNBUSDT, SOLUSDT, XRPUSDT, ADAUSDT, DOGEUSDT, LINKUSDT.
Klaim delisting yang diuji: FTTUSDT, SRMUSDT, COCOSUSDT, BTSUSDT. Simbol yang
ternyata tidak ada di indeks arsip dicatat sebagai klaim yang dibantah, bukan
dihapus diam-diam.

Probe condong likuid, jadi ekstrapolasi ukuran darinya adalah BATAS ATAS kasar,
bukan taksiran tengah. Laporan probe menyatakan ini sendiri.

KOREKSI 2026-07-28: medan `delisting_klaim_terbukti` mengukur KEHADIRAN simbol
di indeks arsip, bukan status delisting. Ukuran yang benar adalah bulan terakhir
yang tersedia. Menurut ukuran itu: SRMUSDT, COCOSUSDT, dan BTSUSDT berhenti di
2024-05 (delisting terdukung), sedangkan FTTUSDT punya data sampai 2026-06,
jadi klaim delisting FTTUSDT DIBANTAH oleh data. Medan itu akan diganti nama
dan diukur ulang; lihat KC-5 di `STATE.md`.

### 9. Pemecahan serapan penuh (baru, dipatok di muka)

Dua kendala runner mengikat sekaligus:

- Ruang: batas atas 39,17 GB parquet melampaui ~14 GB disk bebas satu runner.
- Waktu: rerata unduh terukur 1,33 detik per berkas (rentang 0,60-1,91). Untuk
  21.789 berkas itu sekitar 8,1 jam berturut, melampaui batas 6 jam per job.

Keputusan: serapan penuh dijalankan sebagai **matriks 8 pecahan**. Simbol
diurutkan naik menurut nama, lalu dibagi ke 8 keranjang dengan cara memasukkan
simbol berikutnya ke keranjang yang total bulannya paling kecil, sehingga beban
berimbang menurut CACAH BULAN, bukan menurut cacah simbol. Pembagian ini
deterministik dan dicatat di manifes. Perkiraan per pecahan: sekitar 2.724
berkas, sekitar 1,0 jam unduh, sekitar 4,9 GB parquet. Tiap pecahan mengunggah
aset rilisnya sendiri dan menulis manifes pecahannya sendiri.

### 10. Bulan tanpa data funding (baru, dipatok di muka)

Run probe menemukan FTTUSDT punya klines 2026-06 tetapi TIDAK punya berkas
`fundingRate` 2026-06 (HTTP 404). Jadi ketiadaan funding itu nyata, bukan
teoretis.

Keputusan: simbol-bulan yang klines-nya ada tetapi funding-nya tidak ada DITANDAI
`funding_ada: false` di manifes, dan **dikeluarkan dari backtest**. Alasannya
asimetri arah kesalahan: menganggap funding nol pada bulan yang datanya hilang
adalah memberi makan siang gratis kepada strategi, dan itu persis jenis kesalahan
yang riset ini dibangun untuk mencegah.

## Konsekuensi

Serapan berjalan sebagai matriks job per pecahan bulan di latar, sementara juri
dibangun di atas 12 simbol probe. Tidak ada hipotesis yang boleh diadjudikasi
sebelum semesta penuh selesai dan manifesnya terverifikasi.
