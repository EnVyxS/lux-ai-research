# STATE — versi 6

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
18. **[v5]** Gerbang yang LOLOS wajib melaporkan CACAH hal yang benar-benar
    dibandingkan. Gerbang hijau tanpa cacah dianggap belum menguji apa pun, dan
    gerbang yang lolos jauh lebih cepat daripada dugaan wajib diperiksa dulu
    apakah ia mengukur sesuatu sebelum hasilnya dipakai.
19. **[v5]** Aritmetika atas harga dan volume arsip memakai Decimal atas teks
    aslinya. Float dilarang di jalur perbandingan data, karena beda pembulatan
    tidak bisa dibedakan dari beda agregasi.
20. **[baru v6]** Setiap pengukuran wajib menyebut RENTANG yang benar-benar
    disampel, dan kesimpulan dilarang melampaui rentang itu. Bila sebuah sifat
    diuji pada 2020-2023, sifat itu TIDAK terbukti untuk 2024-2026. Ramalan yang
    menyangkut seluruh sejarah hanya boleh dihitung tepat bila sampelnya
    menjangkau seluruh sejarah.

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
   sejarah. **TERUKUR PERSIS**: bulan tanpa header terakhir 2021-12, bulan
   berheader pertama 2022-01, monoton untuk tiga simbol yang disampel bulan demi
   bulan sepanjang 48 bulan. Penangkalnya: deteksi header dari ISI baris pertama.
5. **KC-5 (repo ini, 2026-07-28)** — label yang mengukur hal lain daripada
   namanya. `delisting_klaim_terbukti` di `probe.py` hanya mengukur kehadiran di
   indeks arsip. Ukuran yang benar kini ada di `survei.terhenti`, tetapi medan
   lama di `probe.py` MASIH belum diganti. Bentuk pikirannya juga muncul di
   kepala saya sendiri: ramalan R-8 dan R-14 meleset karena saya menyamakan
   "pernah ada di arsip" dengan "sudah mati".

## Papan skor hipotesis

Kosong. Hipotesis selesai: 0. Kandidat: 0. Ditolak: 0. N_percobaan: 0.

## Papan skor prediksi

| # | Prediksi | Status |
|---|---|---|
| P-1 | Ekspektasi B0 di bawah 0,10R setelah biaya dan GAGAL kriteria 1 | menunggu (butuh B0) |
| P-2 | Menyalakan detektor non-trendline tidak memperbaiki ekspektasi | menunggu |
| P-3 | Rasio isi rendah didominasi gerbang `rr1 < min_rr` dan `htf_score = 3` | menunggu |
| R-1 | Indeks arsip memuat lebih dari 450 simbol | **TEPAT**: 937 |
| R-2 | Minimal 3 dari 4 klaim delisting terbukti ada di indeks | **TIDAK TERADJUDIKASI** (KC-5): kehadiran bukan ukuran delisting |
| R-3 | Simbol-bulan 1m likuid 1,5-4 MB zip; parquet lebih kecil dari zip | **MELESET SEPARUH**: zip 1,47-1,88 MB; parquet 1,51x LEBIH BESAR |
| R-4 | Estimasi total lebih besar dari kisaran warisan 40-60 GB | **MELESET**: 25,86 GB zip / 39,17 GB parquet |
| R-5 | Berkas terbaru berheader, yang lama tidak | **TEPAT** |
| R-6 | OHLC cocok; volume beda tipis karena pembulatan | **MELESET pada volume**: 0 beda dari 9 kolom |
| R-7 | Total parquet semesta penuh di bawah 25 GB | menunggu (butuh serapan penuh) |
| R-8 | Lebih dari 300 simbol punya bulan terakhir lebih tua dari 2026-01 | **MELESET**: 121 |
| R-9 | Gerbang OHLC lolos untuk 12 simbol probe | **TEPAT**: 12/12, 0 beda |
| R-10 | `trades` cocok, `quote_volume` beda pada sebagian bar | **MELESET**: cocok persis |
| R-11 | Run probe kedua mengulang 937 dan 21.789 persis | **TEPAT** |
| R-12 | Resample pada bulan PERTAMA tiap simbol juga cocok eksak | menunggu |
| R-13 | Peralihan format seragam dan jatuh sebelum 2022-04 | **TEPAT**: 2022-01, monoton |
| R-14 | Lebih dari 300 simbol berstatus terhenti (jeda 2 bulan) | **MELESET**: 128 |
| R-15 | Peralihan header monoton dan sama untuk ketiga simbol | **TEPAT** |
| R-16 | Seluruh bulan yang diperiksa memakai stempel milidetik | **TEPAT SEBAGIAN**: benar untuk 2020-01..2023-12 dan 2024-05; rentang 2024-06..2026-06 BELUM disampel (aturan 20) |
| R-17 | Tiga simbol mati berhenti pada tanggal UTC yang sama, ≥ 2024-05-28 | **TEPAT**: 2024-05-28, 07:09/07:10/07:16 UTC |
| R-18 | Bulan 2024-06..2026-06 juga milidetik 13 digit | menunggu |
| R-19 | Peralihan header 2022-01 berlaku untuk SELURUH simbol lintas batas | menunggu |

Skor sampai kini: tepat 8, meleset 5, meleset separuh 1, tepat sebagian 1,
tidak teradjudikasi 1.

## Daftar ADR

- ADR-A001 — aturan dasar riset. DITERIMA.
- ADR-A002 — serapan data arsip. DITERIMA; §3 (unduh 1m saja) TERBUKTI oleh
  `reports/uji_resample.json`; §9 matriks 8 pecahan; §10 bulan tanpa funding
  dikeluarkan.
- ADR-A003 — taksonomi rezim/klasifikasi. BELUM ADA.

## Status pipeline

| Tahap | Status |
|---|---|
| T0 Peta modul | SELESAI |
| T1 Serapan | Probe SELESAI (terulang 2x). Uji integritas resample LULUS. Survei semesta SELESAI: rentang hidup 937 simbol terukur. Serapan penuh BELUM dibangun: matriks 8 pecahan + manifes |
| T2 Klasifikasi | BELUM MULAI (butuh ADR-A003) |
| T3 Sinyal | BELUM MULAI |
| T4 Juri/backtest | BELUM MULAI |
| T5 Adjudikasi | TERKUNCI sampai semesta penuh + manifes terverifikasi |

## Angka arsip yang sudah terverifikasi

| Besaran | Nilai | Sumber |
|---|---|---|
| Simbol di indeks arsip | 937 (terulang) | `reports/probe_serapan.json`, `reports/survei_semesta.json` |
| Simbol yang punya bulan 1m | 937, gagal listing 0 | `reports/survei_semesta.json` |
| Berkas bulanan 1m | 21.789 (terulang) | `reports/probe_serapan.json` |
| Bulan paling awal / bulan tutup terakhir | 2020-01 / 2026-06 | `reports/survei_semesta.json` |
| Simbol terhenti (jeda ≥ 2 bulan) | 128 dari 937, yaitu 13,7% | idem |
| Simbol masih terbit | 809 | idem |
| Simbol dengan bulan terakhir < 2026-01 | 121 | idem |
| Peralihan format arsip | tanpa header s.d. 2021-12, berheader sejak 2022-01, monoton, 3 simbol × 48 bulan | idem |
| Satuan stempel waktu | milidetik (13 digit) pada 144 berkas 2020-01..2023-12 dan pada 2024-05 | idem |
| Bar terakhir SRM / COCOS / BTS | 2024-05-28 07:10 / 07:16 / 07:09 UTC | idem |
| Rerata byte zip / parquet per simbol-bulan | 1.186.859 / 1.797.488 | `reports/probe_serapan.json` |
| Batas atas total zip / parquet | 25,86 GB / 39,17 GB | idem |
| Bar 5m dan 15m dibandingkan dengan arsip | 8.640 dan 2.880 per simbol likuid | `reports/uji_resample.json` |
| Beda resample lawan arsip, 9 kolom | 0 | idem |

## Jumlah uji

38 uji, semuanya tanpa jaringan (CI run 30327685234, `kode_keluar: 0`).
- `tests/test_kontinuitas.py` (7), `tests/test_serapan.py` (8),
  `tests/test_resample.py` (11), `tests/test_survei.py` (12).
- Enam di antaranya menguji CARA MENGUKUR, bukan hasilnya: dua atas guard
  antarmuka, dua atas pembanding resample, satu atas pemisahan mati/hidup yang
  tidak boleh bergantung pada kehadiran di indeks, satu atas penolakan peralihan
  header yang tidak monoton.
Belum ada uji numerik atas strategi.

## Utang verifikasi yang belum dibayar

1. Temuan A dan B (rasio isi 5,84%; 96% trendline break) baru bisa dinilai
   setelah juri berjalan.
2. Temuan G: klaim "30 pair dipilih alfabetis" belum ditemukan buktinya.
3. Atribut `enable_hs` dipakai `strategy.py` tetapi tidak muncul di `config.py`.
4. Klaim temuan N (kendala mengikat = kapasitas margin) belum diuji angkanya.
5. Angka 0,3232R dan 0,306R warisan belum diverifikasi.
6. ~~Ukuran `decisions/ADR-A001.md`~~ DIBAYAR: 3.569 byte.
7. Percent-encoding simbol non-ASCII belum teruji (tidak ada simbol non-ASCII di
   sampel); 451 dari `fapi.binance.com` tidak diuji dan memang tidak boleh.
8. ~~Klaim warisan "40-60 GB, ~34.000 berkas"~~ DIBAYAR: dibantah.
9. ~~Tanggal berhenti SRM/COCOS/BTS~~ DIBAYAR: 2024-05-28 UTC, dari stempel bar
   terakhir.
10. ~~R-5~~ DIBAYAR.
11. ~~Bulan peralihan format arsip~~ DIBAYAR untuk tiga simbol: 2022-01. Untuk
    seluruh semesta masih klaim (R-19).
12. Gerbang resample baru menguji satu bulan per simbol, semuanya berheader. Era
    tanpa header belum diuji resample-nya (R-12).
13. `probe.py` masih memakai medan `delisting_klaim_terbukti` yang salah ukur.
    Ukuran benar sudah ada di `survei.py`; penggantian medan lama belum dilakukan.
14. **[baru]** Satuan stempel waktu untuk 2024-06..2026-06 belum diukur sama
    sekali. `resample.py` mengandaikan milidetik lewat `MS_MENIT` (R-18).
