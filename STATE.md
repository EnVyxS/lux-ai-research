# STATE — versi 5

Diperbarui: 2026-07-28. Aturan hanya BERTAMBAH; jangan menulis ulang dari ingatan.

## Aturan bernomor

1. Satu definisi R (ADR-A001 §1). Laporan dengan definisi lain ditolak.
2. Gerbang KANDIDAT ADR-A001 §2 berlaku penuh; butir 7 (rezim) DITANGGUHKAN
   sampai ADR-A003 ada.
3. Adjudikasi hipotesis DILARANG sebelum semesta data lengkap dan manifesnya
   terverifikasi. Pembangunan juri di atas 12 simbol probe boleh jalan paralel.
4. `backtest.py` modul warisan tidak boleh dipakai.
5. Angka mana pun dari modul warisan adalah klaim, bukan bukti.
6. Nol koneksi ke bursa; hanya arsip publik `data.binance.vision`.
7. Setiap laporan memuat `sidik_kode` dan `sidik_data`; laporan dengan
   `sidik_data` berbeda tidak boleh dibandingkan.
8. Tidak ada berkas kode BARU melebihi 800 baris; berkas tier A (angkat
   byte-identik) dikecualikan dan wajib punya catatan pengangkatan.
9. Tidak ada skrip `__main__` di akar repo. Satu jalur eksekusi per fungsi.
10. Keluaran diagnostik selalu ditandai `"bukan_bukti": true` dan tidak boleh
    menyentuh gerbang, ambang, konfigurasi, atau putusan.
11. Biaya (fee taker/maker terpisah, funding bertanda benar, slippage yang selalu
    merugikan) adalah bagian JURI sejak hari pertama, bukan money management.
12. **[v2]** Guard struktural dilarang memakai pencarian kata atas kode atau
    berkas konfigurasi. Guard wajib mengukur strukturnya (mis. AST), dan CARA
    MENGUKUR itu sendiri wajib punya uji dengan kasus positif dan negatif.
13. **[v3]** Sandbox agen TIDAK punya akses jaringan (terverifikasi 2026-07-28:
    DNS gagal). Setiap pengukuran dan unduhan arsip dijalankan runner, dan agen
    hanya boleh mempercayai artefak yang di-commit. Jangan pernah menulis angka
    arsip di dokumen sebelum artefaknya ada.
14. **[v3]** Uji di CI dilarang menyentuh jaringan. Kegagalan jaringan yang
    menyamar sebagai kegagalan logika membuat CI merah berhenti dipercaya.
15. **[v3]** Kode dari jalur riset lain hanya boleh masuk atas izin eksplisit
    operator, disalin apa adanya, disertai catatan asal dan blob sha. HASIL,
    angka, dan putusan dari repo lain tidak pernah boleh masuk.
16. **[v4]** Setiap medan laporan wajib dinamai menurut apa yang benar-benar
    diukurnya. Bila nama menjanjikan lebih daripada pengukurannya, laporan itu
    salah meskipun kodenya berjalan benar. Ramalan yang lulus lewat medan
    semacam itu dihitung TIDAK teradjudikasi.
17. **[v4]** Bila data yang dibutuhkan biaya hilang untuk suatu simbol-bulan,
    simbol-bulan itu dikeluarkan dari backtest. Dilarang menggantinya dengan nol;
    ketiadaan data tidak boleh menjadi keuntungan.
18. **[baru v5]** Gerbang yang LOLOS wajib melaporkan CACAH hal yang benar-benar
    dibandingkan. Gerbang hijau tanpa cacah dianggap belum menguji apa pun, dan
    gerbang yang lolos jauh lebih cepat daripada dugaan wajib diperiksa dulu
    apakah ia mengukur sesuatu sebelum hasilnya dipakai.
19. **[baru v5]** Aritmetika atas harga dan volume arsip memakai Decimal atas
    teks aslinya. Float dilarang di jalur perbandingan data, karena beda
    pembulatan tidak bisa dibedakan dari beda agregasi.

## Kelas cacat

1. **KC-1 (modul warisan)** — pemilihan default berdasarkan paruh uji.
   Penangkalnya: pra-registrasi tertulis sebelum run.
2. **KC-2 (modul warisan)** — asimetri pencatatan: alasan setup dilewatkan
   dicatat, alasan setup diambil tidak. Penangkalnya: setiap sinyal membawa
   setup_source, htf_score, regime, pattern, sesi, indeks bar.
3. **KC-3 (repo ini, 2026-07-28)** — guard berbasis pencarian kata. Uji
   pemisahan antarmuka versi pertama gagal membedakan impor dari docstring yang
   MELARANG impor, lalu menjatuhkan CI run 30311582627. Penangkalnya: aturan 12.
4. **KC-4 (repo ini, 2026-07-28)** — format arsip yang berubah di tengah
   sejarah. **TERBUKTI 2026-07-28** oleh `reports/uji_resample.json`: bulan
   pertama sepuluh simbol probe (2020-01 sampai 2021-02) tanpa header, sedangkan
   FTTUSDT 2022-04, COCOSUSDT 2023-02, dan seluruh bulan yang diuji (2024-05 dan
   2026-06) berheader. Penangkalnya: deteksi header diukur dari ISI baris
   pertama, dengan uji untuk kedua bentuk.
5. **KC-5 (repo ini, 2026-07-28)** — label yang mengukur hal lain daripada
   namanya. `delisting_klaim_terbukti` sebenarnya hanya mengukur kehadiran
   simbol di indeks arsip, padahal arsip menyimpan simbol mati selamanya. Ramalan
   R-2 karenanya "lulus" tanpa menguji apa pun. Penangkalnya: aturan 16, dan
   ukuran delisting yang benar adalah bulan terakhir yang tersedia.

## Papan skor hipotesis

Kosong. Hipotesis selesai: 0. Kandidat: 0. Ditolak: 0. N_percobaan: 0.

## Papan skor prediksi

| # | Prediksi | Ditulis | Status |
|---|---|---|---|
| P-1 | Ekspektasi B0 jatuh di bawah 0,10R setelah funding+slippage dimodelkan benar, dan GAGAL kriteria 1 | 2026-07-28 | menunggu (butuh B0) |
| P-2 | Menyalakan detektor non-trendline tidak memperbaiki ekspektasi; hanya menambah transaksi berkualitas rendah | 2026-07-28 | menunggu |
| P-3 | Rasio isi rendah didominasi gerbang `rr1 < min_rr` dan `htf_score = 3`, bukan kelangkaan sinyal | 2026-07-28 | menunggu |
| R-1 | Indeks arsip memuat lebih dari 450 simbol | 2026-07-28 | **TEPAT**: 937 simbol |
| R-2 | Minimal 3 dari 4 klaim delisting terbukti ada di indeks | 2026-07-28 | **TIDAK TERADJUDIKASI** (KC-5): 4/4 hadir di indeks, tetapi kehadiran bukan ukuran delisting. Menurut bulan terakhir: SRM/COCOS/BTS delisting; FTTUSDT masih hidup sampai 2026-06, klaimnya dibantah |
| R-3 | Satu simbol-bulan 1m likuid 1,5-4 MB zip; parquet zstd lebih kecil dari zip | 2026-07-28 | **MELESET SEPARUH**: zip 1,47-1,88 MB (hampir tepat); parquet justru 1,51x LEBIH BESAR dari zip |
| R-4 | Estimasi total dari probe LEBIH BESAR dari kisaran warisan 40-60 GB | 2026-07-28 | **MELESET**: 25,86 GB zip / 39,17 GB parquet, keduanya di bawah kisaran; klaim warisan 34.000 berkas juga dibantah (21.789) |
| R-5 | Berkas bulanan terbaru punya header, yang lama tidak | 2026-07-28 | **TEPAT**: bulan pertama 2020-01..2021-02 tanpa header; 2022-04 dan sesudahnya berheader. Peralihan antara 2021-02 dan 2022-04 belum diukur persis |
| R-6 | Resample 1m ke 5m/15m cocok pada OHLC; volume beda tipis karena pembulatan | 2026-07-28 | **MELESET pada bagian volume**: OHLC cocok, dan volume juga cocok PERSIS (0 beda dari 9 kolom) |
| R-7 | Total parquet semesta penuh jatuh di bawah 25 GB, jauh di bawah batas atas 39,17 GB | 2026-07-28 | menunggu (butuh serapan penuh) |
| R-8 | Lebih dari 300 dari 937 simbol punya bulan terakhir lebih tua dari 2026-01 | 2026-07-28 | menunggu (butuh pengukuran bulan terakhir per simbol) |
| R-9 | Gerbang OHLC lolos untuk 12 simbol probe | 2026-07-28 | **TEPAT**: 12/12 lolos, 0 beda |
| R-10 | `trades` cocok persis, `quote_volume` beda pada sebagian kecil bar | 2026-07-28 | **MELESET**: `quote_volume` cocok persis juga |
| R-11 | Run probe kedua mengulang 937 simbol dan 21.789 berkas persis | 2026-07-28 | **TEPAT**: run 30314166310 mengulang keduanya |
| R-12 | Resample pada bulan PERTAMA tiap simbol (era tanpa header) juga cocok eksak | 2026-07-28 | menunggu |
| R-13 | Peralihan format arsip seragam antar simbol dan jatuh sebelum 2022-04 | 2026-07-28 | menunggu |

## Daftar ADR

- ADR-A001 — aturan dasar riset. DITERIMA 2026-07-28.
- ADR-A002 — serapan data arsip. **DITERIMA 2026-07-28**; bagian 7 terisi dari
  `reports/probe_serapan.json`. Bagian 3 (unduh 1m saja, turunkan sisanya) kini
  TERBUKTI oleh `reports/uji_resample.json`. Bagian 9 matriks 8 pecahan, bagian
  10 bulan tanpa funding dikeluarkan.
- ADR-A003 — taksonomi rezim/klasifikasi. BELUM ADA.

## Status pipeline

| Tahap | Status |
|---|---|
| T0 Peta modul | SELESAI (`PETA_MODUL.md`, `PETA_MODUL_BERKAS.md`) |
| T1 Serapan | Probe SELESAI dan terulang. Uji integritas resample LULUS untuk 12 simbol (satu bulan per simbol). Serapan penuh DIIZINKAN tetapi BELUM dibangun: matriks 8 pecahan + manifes masih harus ditulis |
| T2 Klasifikasi | BELUM MULAI (butuh ADR-A003) |
| T3 Sinyal | BELUM MULAI |
| T4 Juri/backtest | BELUM MULAI |
| T5 Adjudikasi | TERKUNCI sampai semesta penuh + manifes terverifikasi |

## Angka arsip yang sudah terverifikasi

| Besaran | Nilai | Sumber |
|---|---|---|
| Simbol di indeks arsip | 937 (terulang di dua run) | `reports/probe_serapan.json` |
| Berkas bulanan 1m | 21.789 (terulang di dua run) | idem |
| Rerata byte zip per simbol-bulan | 1.186.859 | idem |
| Rerata byte parquet zstd per simbol-bulan | 1.797.488 | idem |
| Batas atas total zip | 25,86 GB | idem |
| Batas atas total parquet | 39,17 GB | idem |
| Rerata detik unduh per berkas | 1,33 (0,60-1,91) | idem |
| Bar 5m dibandingkan dengan arsip | 8.640 per simbol likuid; 7.862-7.864 simbol mati | `reports/uji_resample.json` |
| Bar 15m dibandingkan dengan arsip | 2.880 per simbol likuid; 2.621-2.622 simbol mati | idem |
| Beda resample lawan arsip, 9 kolom | 0 | idem |

## Jumlah uji

26 uji, semuanya murni tanpa jaringan (CI run 30314166290, `kode_keluar: 0`).
- `tests/test_kontinuitas.py` (7): 2 menguji CARA MENGUKUR guard antarmuka, 5
  menguji aturan repo.
- `tests/test_serapan.py` (8): bentuk URL arsip, percent-encoding simbol
  non-ASCII, URL funding, deteksi header dari isi, baca zip dengan dan tanpa
  header, perapian urutan dan duplikat, penegakan anti bias keselamatan-hidup.
- `tests/test_resample.py` (11): agregasi 5m, keselarasan ember, menit hilang
  tercatat, penjumlahan Decimal eksak, ketaktergantungan urutan masukan, dua uji
  atas pembanding, pembacaan teks tanpa kehilangan desimal, deteksi header dari
  zip, dan dua uji atas CARA MENGUKUR impor jaringan.
Belum ada uji numerik atas strategi.

## Utang verifikasi yang belum dibayar

1. Temuan A dan B (rasio isi 5,84%; 96% trendline break) hanya bisa dinilai
   setelah juri sendiri berjalan.
2. Temuan G: klaim "30 pair dipilih alfabetis" belum ditemukan buktinya di berkas.
3. Atribut `enable_hs` dipakai `strategy.py` dan ada di `.env.example`, tetapi
   tidak muncul di grep `config.py`. Perlu dilacak.
4. Klaim temuan N bahwa kendala mengikat pada modal kecil adalah kapasitas
   margin, bukan notional minimum — belum diuji angkanya.
5. Angka 0,3232R dan 0,306R pada aritmetika biaya warisan belum diverifikasi.
6. ~~Ukuran byte `decisions/ADR-A001.md`~~ DIBAYAR: 3.569 byte.
7. Sifat arsip di `lux_ai/serapan/arsip.py`: prefix `data/`, keaslian nama demi
   `.CHECKSUM`, dan listing S3 TERBUKTI. Yang MASIH klaim: percent-encoding
   simbol non-ASCII (tidak ada simbol non-ASCII di 12 probe) dan 451 dari REST
   `fapi.binance.com` (tidak diuji, dan memang tidak boleh diuji).
8. ~~Klaim warisan "40-60 GB, ~34.000 berkas"~~ DIBAYAR: DIBANTAH; 21.789 berkas,
   batas atas 39,17 GB.
9. Dugaan bahwa SRMUSDT, COCOSUSDT, dan BTSUSDT berhenti pada tanggal yang sama
   (sekitar 27-28 Mei 2024) berasal dari kemiripan cacah baris, belum dari
   stempel waktu bar terakhirnya. Perlu diukur.
10. ~~R-5 belum teradjudikasi~~ DIBAYAR: terukur lewat `berheader_bulan_pertama`
    dan `berheader_bulan_diuji`.
11. Bulan persis peralihan format arsip (antara 2021-02 dan 2022-04) belum
    diukur, dan keseragamannya antar simbol belum diperiksa.
12. Gerbang resample baru menguji SATU bulan per simbol, semuanya bulan
    berheader. Kecocokan resample pada era TANPA header belum diuji.
13. `delisting_klaim_terbukti` di `probe.py` masih memakai ukuran yang salah
    (KC-5); medannya belum diganti dan belum ada uji atas cara mengukurnya.
