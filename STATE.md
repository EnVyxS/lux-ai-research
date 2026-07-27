# STATE — versi 4

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
16. **[baru v4]** Setiap medan laporan wajib dinamai menurut apa yang benar-benar
    diukurnya. Bila nama menjanjikan lebih daripada pengukurannya, laporan itu
    salah meskipun kodenya berjalan benar. Ramalan yang lulus lewat medan
    semacam itu dihitung TIDAK teradjudikasi.
17. **[baru v4]** Bila data yang dibutuhkan biaya hilang untuk suatu
    simbol-bulan, simbol-bulan itu dikeluarkan dari backtest. Dilarang
    menggantinya dengan nol; ketiadaan data tidak boleh menjadi keuntungan.

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
   sejarah. Berkas klines lama tanpa baris header, yang baru dengan header.
   Satu aturan baca tetap akan menelan header sebagai data atau membuang satu
   baris nyata. Penangkalnya: deteksi header diukur dari ISI baris pertama,
   dengan uji untuk kedua bentuk.
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
| R-5 | Berkas bulanan terbaru punya header, yang lama tidak | 2026-07-28 | **BELUM TERADJUDIKASI**: laporan probe tidak punya medannya. Ditambahkan pada pengukuran berikutnya |
| R-6 | Resample 1m→5m/15m cocok pada OHLC untuk 12 probe; volume beda tipis karena pembulatan | 2026-07-28 | menunggu |
| R-7 | Total parquet semesta penuh jatuh di bawah 25 GB, jauh di bawah batas atas 39,17 GB | 2026-07-28 | menunggu |
| R-8 | Lebih dari 300 dari 937 simbol punya bulan terakhir lebih tua dari 2026-01 | 2026-07-28 | menunggu |

## Daftar ADR

- ADR-A001 — aturan dasar riset. DITERIMA 2026-07-28.
- ADR-A002 — serapan data arsip. **DITERIMA 2026-07-28**; bagian 7 terisi dari
  `reports/probe_serapan.json` (run 30312616216). Ditambah bagian 9 (matriks 8
  pecahan) dan bagian 10 (bulan tanpa funding dikeluarkan). Serapan penuh kini
  diizinkan.
- ADR-A003 — taksonomi rezim/klasifikasi. BELUM ADA.

## Status pipeline

| Tahap | Status |
|---|---|
| T0 Peta modul | SELESAI (`PETA_MODUL.md`, `PETA_MODUL_BERKAS.md`) |
| T1 Serapan | Probe SELESAI dan terverifikasi (937 simbol, 21.789 berkas, 12/12 checksum cocok). Serapan penuh DIIZINKAN tetapi BELUM dibangun; uji integritas resample juga belum |
| T2 Klasifikasi | BELUM MULAI (butuh ADR-A003) |
| T3 Sinyal | BELUM MULAI |
| T4 Juri/backtest | BELUM MULAI |
| T5 Adjudikasi | TERKUNCI sampai semesta penuh + manifes terverifikasi |

## Angka arsip yang sudah terverifikasi

| Besaran | Nilai | Sumber |
|---|---|---|
| Simbol di indeks arsip | 937 | `reports/probe_serapan.json` |
| Berkas bulanan 1m | 21.789 | idem |
| Rerata byte zip per simbol-bulan | 1.186.859 | idem |
| Rerata byte parquet zstd per simbol-bulan | 1.797.488 | idem |
| Batas atas total zip | 25,86 GB | idem |
| Batas atas total parquet | 39,17 GB | idem |
| Rerata detik unduh per berkas | 1,33 (0,60-1,91) | idem |

## Jumlah uji

15 uji, semuanya murni tanpa jaringan.
- `tests/test_kontinuitas.py` (7): 2 menguji CARA MENGUKUR guard antarmuka, 5
  menguji aturan repo (berkas kontinuitas, larangan `__main__` di akar, batas
  800 baris, pemisahan antarmuka langsung, pemisahan transitif).
- `tests/test_serapan.py` (8): bentuk URL arsip, percent-encoding simbol
  non-ASCII, URL funding, deteksi header dari isi, baca zip dengan dan tanpa
  header, perapian urutan dan duplikat, penegakan anti bias keselamatan-hidup.
Belum ada uji numerik.

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
   `.CHECKSUM`, dan listing S3 kini TERBUKTI oleh run probe. Yang MASIH klaim:
   percent-encoding simbol non-ASCII (tidak ada simbol non-ASCII di 12 probe,
   jadi jalur itu belum pernah dijalankan sungguhan) dan 451 dari REST
   `fapi.binance.com` (tidak diuji, dan memang tidak boleh diuji).
8. ~~Klaim warisan "40-60 GB, ~34.000 berkas"~~ DIBAYAR: DIBANTAH; 21.789 berkas,
   batas atas 39,17 GB.
9. Dugaan bahwa SRMUSDT, COCOSUSDT, dan BTSUSDT berhenti pada tanggal yang sama
   (sekitar 27-28 Mei 2024) berasal dari kemiripan cacah baris, belum dari
   stempel waktu bar terakhirnya. Perlu diukur.
10. R-5 (header lama lawan baru) belum teradjudikasi karena medannya tidak ada.
