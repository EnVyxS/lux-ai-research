# STATE — versi 8

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
20. **[v6]** Setiap pengukuran wajib menyebut RENTANG yang benar-benar disampel,
    dan kesimpulan dilarang melampaui rentang itu. Bila sebuah sifat diuji pada
    2020-2023, sifat itu TIDAK terbukti untuk 2024-2026. Ramalan yang menyangkut
    seluruh sejarah hanya boleh dihitung tepat bila sampelnya menjangkau seluruh
    sejarah.
21. **[v7]** Setiap angka ringkasan yang saya tulis sendiri (cacah baris tabel,
    total, persentase) wajib dihitung ulang dari barisnya saat berkas diperbarui.
    Papan skor v6 menulis "tepat 8" padahal barisnya 7. Angka ringkasan yang
    tidak pernah dihitung ulang adalah klaim, sama seperti angka warisan.
22. **[v8]** `sidik_kode` wajib mencakup SELURUH berkas yang ikut menentukan isi
    laporan, termasuk modul yang dipanggil dari modul lain. Sidik yang tidak
    mencakup ketergantungannya memberi rasa aman palsu: laporan bisa berubah
    tanpa sidiknya berubah.

## Kelas cacat

1. **KC-1 (modul warisan)** — pemilihan default berdasarkan paruh uji.
   Penangkalnya: pra-registrasi tertulis sebelum run.
2. **KC-2 (modul warisan)** — asimetri pencatatan: alasan setup dilewatkan
   dicatat, alasan setup diambil tidak. Penangkalnya: setiap sinyal membawa
   setup_source, htf_score, regime, pattern, sesi, indeks bar.
3. **KC-3 (repo ini)** — guard berbasis pencarian kata; menjatuhkan CI run
   30311582627. Penangkalnya: aturan 12.
4. **KC-4 (repo ini)** — format arsip berubah di tengah sejarah. TERUKUR:
   tanpa header s.d. 2021-12, berheader sejak 2022-01, monoton sepanjang 78
   bulan untuk tiga simbol. Penangkalnya: deteksi header dari ISI baris pertama.
5. **KC-5 (repo ini)** — label yang mengukur hal lain daripada namanya.
   Medan `delisting_klaim_terbukti` di `probe.py` hanya mengukur kehadiran di
   indeks arsip. DIPERBAIKI 2026-07-28: medan itu dihapus dan diganti
   `nilai_klaim_delisting` yang memakai `survei.terhenti`, dengan empat uji
   termasuk kasus negatif FTTUSDT. Bentuk pikiran yang sama membuat ramalan R-8
   dan R-14 saya meleset jauh; kodenya sembuh, kebiasaannya tetap dijaga.

## Papan skor hipotesis

Kosong. Hipotesis selesai: 0. Kandidat: 0. Ditolak: 0. N_percobaan: 0.

## Papan skor prediksi

| # | Prediksi | Status |
|---|---|---|
| P-1 | Ekspektasi B0 di bawah 0,10R setelah biaya dan GAGAL kriteria 1 | menunggu |
| P-2 | Menyalakan detektor non-trendline tidak memperbaiki ekspektasi | menunggu |
| P-3 | Rasio isi rendah didominasi gerbang `rr1 < min_rr` dan `htf_score = 3` | menunggu |
| R-1 | Indeks arsip memuat lebih dari 450 simbol | TEPAT: 937 |
| R-2 | Minimal 3 dari 4 klaim delisting terbukti | TEPAT: 3 dari 4; FTTUSDT terbantah |
| R-3 | Simbol-bulan 1m likuid 1,5-4 MB zip; parquet lebih kecil dari zip | MELESET SEPARUH: parquet 1,51x lebih besar |
| R-4 | Estimasi total lebih besar dari 40-60 GB | MELESET: 25,86 GB zip / 39,17 GB parquet |
| R-5 | Berkas terbaru berheader, yang lama tidak | TEPAT |
| R-6 | OHLC cocok; volume beda tipis karena pembulatan | MELESET pada volume: 0 beda |
| R-7 | Total parquet semesta penuh di bawah 25 GB | menunggu |
| R-8 | Lebih dari 300 simbol berbulan terakhir lebih tua dari 2026-01 | MELESET: 121 |
| R-9 | Gerbang OHLC lolos untuk 12 simbol probe | TEPAT: 12/12, 0 beda |
| R-10 | `trades` cocok, `quote_volume` beda sebagian | MELESET: cocok persis |
| R-11 | Run probe kedua mengulang 937 dan 21.789 persis | TEPAT |
| R-12 | Resample pada bulan PERTAMA tiap simbol juga cocok eksak | menunggu |
| R-13 | Peralihan format seragam dan jatuh sebelum 2022-04 | TEPAT: 2022-01 |
| R-14 | Lebih dari 300 simbol berstatus terhenti | MELESET: 128 |
| R-15 | Peralihan header monoton dan sama untuk ketiga simbol | TEPAT |
| R-16 | Seluruh bulan yang diperiksa memakai stempel milidetik | TEPAT (2020-01..2026-06, 237 bulan) |
| R-17 | Tiga simbol mati berhenti pada tanggal UTC yang sama | TEPAT: 2024-05-28 |
| R-18 | Bulan 2024-06..2026-06 juga milidetik 13 digit | TEPAT: seragam, `bulan_satuan_berubah` null |
| R-19 | Peralihan header 2022-01 berlaku untuk SELURUH simbol | menunggu (baru 3 simbol) |
| R-20 | Serapan penuh: 0 berkas non-milidetik dan 0 pelanggaran batas header | menunggu |
| R-21 | Probe baru: terhenti SRM/COCOS/BTS, FTT masih terbit, acuan 2026-06 | TEPAT: keempat medan cocok |
| R-22 | Angka infrastruktur terulang ketiga kali persis | TEPAT: 937, 21.789, 1.186.859, 1.797.488 |

Cacah dihitung ulang baris demi baris (aturan 21):

- TEPAT 12: R-1, R-2, R-5, R-9, R-11, R-13, R-15, R-16, R-17, R-18, R-21, R-22.
- MELESET 5: R-4, R-6, R-8, R-10, R-14.
- MELESET SEPARUH 1: R-3.
- TIDAK TERADJUDIKASI 0.
- MENUNGGU 4: R-7, R-12, R-19, R-20.

Jumlah 12+5+1+0+4 = 22, sama dengan cacah baris R-1..R-22. P-1..P-3 dihitung
terpisah dan ketiganya masih menunggu. Tidak ada lagi baris TIDAK
TERADJUDIKASI: R-2 lunas setelah alat ukurnya dibetulkan.

## Daftar ADR

- ADR-A001 — aturan dasar riset. DITERIMA.
- ADR-A002 — serapan data arsip. DITERIMA; §3 TERBUKTI oleh `uji_resample.json`;
  §9 matriks 8 pecahan; §10 bulan tanpa funding dikeluarkan.
- ADR-A003 — taksonomi rezim/klasifikasi. BELUM ADA.

## Status pipeline

| Tahap | Status |
|---|---|
| T0 Peta modul | SELESAI |
| T1 Serapan | Probe SELESAI (tiga run). Gerbang resample LULUS. Survei semesta SELESAI dua kali, rentang penuh 2020-01..2026-06. Serapan penuh BELUM dibangun |
| T2 Klasifikasi | BELUM MULAI (butuh ADR-A003) |
| T3 Sinyal | BELUM MULAI |
| T4 Juri/backtest | BELUM MULAI |
| T5 Adjudikasi | TERKUNCI sampai semesta penuh + manifes terverifikasi |

## Angka arsip yang sudah terverifikasi

| Besaran | Nilai | Sumber |
|---|---|---|
| Simbol di indeks arsip | 937 (tiga run) | `probe_serapan.json`, `survei_semesta.json` |
| Simbol punya bulan 1m | 937, gagal listing 0 | `survei_semesta.json` |
| Berkas bulanan 1m | 21.789 (tiga run) | `probe_serapan.json` |
| Rentang arsip | 2020-01 s.d. 2026-06 | `survei_semesta.json` |
| Simbol terhenti (jeda ≥ 2 bulan) | 128 dari 937 (13,7%) | idem |
| Simbol masih terbit | 809 | idem |
| Bulan terakhir lebih tua dari 2026-01 | 121 | idem |
| Klaim delisting operator | 3 dari 4 terhenti (SRM, COCOS, BTS); FTTUSDT masih terbit sampai 2026-06 | `probe_serapan.json` run 30336009153 |
| Peralihan format | tanpa header s.d. 2021-12, berheader sejak 2022-01, monoton, 3 simbol × 78 bulan | `survei_semesta.json` |
| Satuan stempel | milidetik pada 237 bulan yang disampel 2020-01..2026-06, seragam | idem |
| Bar terakhir SRM / COCOS / BTS | 2024-05-28 07:10 / 07:16 / 07:09 UTC | idem |
| Rerata byte zip / parquet | 1.186.859 / 1.797.488 (tiga run) | `probe_serapan.json` |
| Batas atas total zip / parquet | 25,86 GB / 39,17 GB | idem |
| Baris bulan penuh likuid | 43.200; `baris_dibuang` 0 dan `celah_bukan_60_detik` 0 untuk 12 simbol | idem |
| Bar 5m / 15m dibandingkan | 8.640 / 2.880 per simbol likuid, 0 beda pada 9 kolom | `uji_resample.json` |

## Jumlah uji

46 uji tanpa jaringan (CI run 30336075738, commit `7fdc81cc`, `kode_keluar: 0`).
`test_kontinuitas.py` 7, `test_serapan.py` 12, `test_resample.py` 11,
`test_survei.py` 16. Empat belas di antaranya menguji CARA MENGUKUR, bukan
hasilnya. Belum ada uji numerik atas strategi.

## Utang verifikasi yang belum dibayar

1. Temuan A dan B (rasio isi 5,84%; 96% trendline break) menunggu juri.
2. Temuan G: klaim "30 pair dipilih alfabetis" belum ditemukan buktinya.
3. Atribut `enable_hs` dipakai `strategy.py` tetapi tidak ada di `config.py`.
4. Klaim temuan N (kendala mengikat = kapasitas margin) belum diuji angkanya.
5. Angka 0,3232R dan 0,306R warisan belum diverifikasi.
6. ~~Ukuran ADR-A001~~ DIBAYAR: 3.569 byte.
7. Percent-encoding simbol non-ASCII belum teruji; 451 dari `fapi.binance.com`
   tidak diuji dan memang tidak boleh.
8. ~~Klaim warisan 40-60 GB / 34.000 berkas~~ DIBAYAR: dibantah.
9. ~~Tanggal berhenti SRM/COCOS/BTS~~ DIBAYAR: 2024-05-28 UTC.
10. ~~R-5~~ DIBAYAR.
11. Bulan peralihan format DIBAYAR untuk 3 simbol (2022-01, 78 bulan); untuk
    seluruh semesta masih klaim (R-19).
12. Gerbang resample baru menguji satu bulan berheader per simbol. Era tanpa
    header belum diuji resample-nya (R-12).
13. ~~Medan `delisting_klaim_terbukti` yang salah ukur~~ DIBAYAR: dihapus,
    diganti pengukuran jarak bulan; run 30336009153 membuktikannya bekerja.
14. ~~Satuan stempel 2024-06..2026-06~~ DIBAYAR: milidetik, 237 bulan disampel,
    `seragam: true`. Untuk 937 simbol penuh masih klaim (R-20).
