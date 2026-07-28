# STATE — versi 9

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
13. **[v3]** Sandbox agen TIDAK punya akses jaringan. Setiap pengukuran dan
    unduhan arsip dijalankan runner, dan agen hanya boleh mempercayai artefak
    yang di-commit.
14. **[v3]** Uji di CI dilarang menyentuh jaringan.
15. **[v3]** Kode dari jalur riset lain hanya boleh masuk atas izin eksplisit
    operator, disalin apa adanya, disertai catatan asal dan blob sha. HASIL,
    angka, dan putusan dari repo lain tidak pernah boleh masuk.
16. **[v4]** Setiap medan laporan wajib dinamai menurut apa yang benar-benar
    diukurnya. Ramalan yang lulus lewat medan yang salah ukur dihitung TIDAK
    teradjudikasi.
17. **[v4]** Bila data yang dibutuhkan biaya hilang untuk suatu simbol-bulan,
    simbol-bulan itu dikeluarkan dari backtest. Dilarang menggantinya dengan nol.
18. **[v5]** Gerbang yang LOLOS wajib melaporkan CACAH hal yang benar-benar
    dibandingkan. Gerbang hijau tanpa cacah dianggap belum menguji apa pun.
19. **[v5]** Aritmetika atas harga dan volume arsip memakai Decimal atas teks
    aslinya. Float dilarang di jalur perbandingan data.
20. **[v6]** Setiap pengukuran wajib menyebut RENTANG yang benar-benar disampel,
    dan kesimpulan dilarang melampaui rentang itu.
21. **[v7]** Setiap angka ringkasan yang saya tulis sendiri wajib dihitung ulang
    dari barisnya saat berkas diperbarui. Angka ringkasan yang tidak pernah
    dihitung ulang adalah klaim, sama seperti angka warisan.
22. **[v8]** `sidik_kode` wajib mencakup SELURUH berkas yang ikut menentukan isi
    laporan, termasuk modul yang dipanggil dari modul lain.
23. **[v9]** Gerbang yang MERAH dilarang dilonggarkan sebelum sebab kegagalannya
    terukur. Toleransi, pengecualian bulan, dan ambang "cukup dekat" hanya boleh
    lahir dari ADR yang memuat angka terukur — tidak pernah dari keinginan agar
    pipeline berjalan. Melonggarkan gerbang agar hijau adalah KC-1 dalam bentuk
    lain.

## Kelas cacat

1. **KC-1 (modul warisan)** — pemilihan default berdasarkan paruh uji.
   Penangkalnya: pra-registrasi tertulis sebelum run.
2. **KC-2 (modul warisan)** — asimetri pencatatan: alasan setup dilewatkan
   dicatat, alasan setup diambil tidak.
3. **KC-3 (repo ini)** — guard berbasis pencarian kata; menjatuhkan CI run
   30311582627. Penangkalnya: aturan 12.
4. **KC-4 (repo ini)** — format arsip berubah di tengah sejarah: tanpa header
   s.d. 2021-12, berheader sejak 2022-01. Kini teruji pada 12 simbol
   (`tanggal_tak_sepakat_dengan_isi` kosong), bukan lagi 3.
5. **KC-5 (repo ini)** — label yang mengukur hal lain daripada namanya.
   DIPERBAIKI 2026-07-28 lewat `nilai_klaim_delisting`; empat uji menjaganya.
6. **KC-6 (arsip, BARU v9)** — berkas 1m dan berkas 5m/15m terbitan Binance
   TIDAK sepakat di bulan-bulan awal simbol. Terukur: 609 sel OHLC berbeda dari
   ~905.872 perbandingan (0,067%), seluruhnya di bulan awal, didominasi `open`,
   `close` hanya beda 2 kali. Bukan cacat kode kami. Bukan pula soal header:
   FTTUSDT 2022-04 berheader dan gagal, COCOSUSDT 2023-02 berheader dan bersih.
   Sebabnya BELUM terukur; dua hipotesis bersaing (H1 celah menit, H2 sumber
   agregasi berbeda) dan ETHUSDT 2020-01 dengan 44.640 baris penuh namun tetap
   berbeda adalah bukti tandingan untuk H1.

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
| R-3 | Simbol-bulan 1m likuid 1,5-4 MB zip; parquet lebih kecil dari zip | MELESET SEPARUH |
| R-4 | Estimasi total lebih besar dari 40-60 GB | MELESET: 25,86 / 39,17 GB |
| R-5 | Berkas terbaru berheader, yang lama tidak | TEPAT |
| R-6 | OHLC cocok; volume beda tipis karena pembulatan | MELESET pada volume |
| R-7 | Total parquet semesta penuh di bawah 25 GB | menunggu |
| R-8 | Lebih dari 300 simbol berbulan terakhir lebih tua dari 2026-01 | MELESET: 121 |
| R-9 | Gerbang OHLC lolos untuk 12 simbol probe (bulan akhir) | TEPAT: 12/12 |
| R-10 | `trades` cocok, `quote_volume` beda sebagian | MELESET: cocok persis |
| R-11 | Run probe kedua mengulang 937 dan 21.789 persis | TEPAT |
| R-12 | Resample pada bulan PERTAMA tiap simbol juga cocok eksak | **MELESET: 609 sel OHLC beda** |
| R-13 | Peralihan format seragam dan jatuh sebelum 2022-04 | TEPAT: 2022-01 |
| R-14 | Lebih dari 300 simbol berstatus terhenti | MELESET: 128 |
| R-15 | Peralihan header monoton dan sama untuk ketiga simbol | TEPAT |
| R-16 | Seluruh bulan yang diperiksa memakai stempel milidetik | TEPAT (237 bulan) |
| R-17 | Tiga simbol mati berhenti pada tanggal UTC yang sama | TEPAT: 2024-05-28 |
| R-18 | Bulan 2024-06..2026-06 juga milidetik 13 digit | TEPAT |
| R-19 | Peralihan header 2022-01 berlaku untuk SELURUH simbol | menunggu (baru 12 simbol) |
| R-20 | Serapan penuh: 0 berkas non-milidetik dan 0 pelanggaran batas header | menunggu |
| R-21 | Probe baru: terhenti SRM/COCOS/BTS, FTT masih terbit | TEPAT |
| R-22 | Angka infrastruktur terulang ketiga kali persis | TEPAT |
| R-23 | Gerbang dua bulan lolos, `total_beda_kolom_jumlah` = 0 | **MELESET pada kedua klausa** |
| R-24 | `tanggal_tak_sepakat_dengan_isi` kosong | TEPAT |
| R-25 | `bulan_era_tanpa_header` = 10 | TEPAT |
| R-26 | ≥ 90% bucket `open` beda pada DOGE/BTS berimpit dengan celah menit | menunggu |
| R-27 | ETHUSDT 2020-01 benar-benar tanpa celah, sehingga H1 gugur untuk ETH | menunggu |
| R-28 | 12 bulan akhir tetap 0 beda pada run berikutnya | menunggu |

Cacah dihitung ulang baris demi baris (aturan 21):

- TEPAT 14: R-1, R-2, R-5, R-9, R-11, R-13, R-15, R-16, R-17, R-18, R-21, R-22,
  R-24, R-25.
- MELESET 7: R-4, R-6, R-8, R-10, R-12, R-14, R-23.
- MELESET SEPARUH 1: R-3.
- TIDAK TERADJUDIKASI 0.
- MENUNGGU 5: R-7, R-19, R-20, R-26, R-27, R-28 — enam baris; MENUNGGU 6.

Jumlah 14+7+1+0+6 = 28, sama dengan cacah baris R-1..R-28. P-1..P-3 dihitung
terpisah dan ketiganya masih menunggu.

## Daftar ADR

- ADR-A001 — aturan dasar riset. DITERIMA.
- ADR-A002 — serapan data arsip. DITERIMA; §3 kini TERBANTAH SEBAGIAN: resample
  eksak terbukti untuk bulan akhir, TIDAK untuk bulan awal (KC-6).
- ADR-A003 — taksonomi rezim/klasifikasi. BELUM ADA.
- ADR-A004 — kebijakan bulan awal simbol menghadapi KC-6. WAJIB ADA sebelum
  serapan penuh; belum ditulis.

## Status pipeline

| Tahap | Status |
|---|---|
| T0 Peta modul | SELESAI |
| T1 Serapan | Probe SELESAI (tiga run). Survei semesta SELESAI. Gerbang resample **MERAH** pada bulan awal (KC-6); serapan penuh TERKUNCI sampai ADR-A004 |
| T2 Klasifikasi | BELUM MULAI (butuh ADR-A003) |
| T3 Sinyal | BELUM MULAI |
| T4 Juri/backtest | BELUM MULAI |
| T5 Adjudikasi | TERKUNCI sampai semesta penuh + manifes terverifikasi |

## Angka arsip yang sudah terverifikasi

| Besaran | Nilai | Sumber |
|---|---|---|
| Simbol di indeks arsip | 937 (tiga run) | `probe_serapan.json` |
| Berkas bulanan 1m | 21.789 (tiga run) | idem |
| Rentang arsip | 2020-01 s.d. 2026-06 | `survei_semesta.json` |
| Simbol terhenti / masih terbit | 128 / 809 | idem |
| Klaim delisting operator | 3 dari 4 terhenti; FTTUSDT masih terbit | `probe_serapan.json` |
| Peralihan format | tanpa header s.d. 2021-12; teruji 12 simbol, 0 tak sepakat | `uji_resample.json` |
| Satuan stempel | milidetik, 237 bulan disampel, seragam | `survei_semesta.json` |
| Rerata byte zip / parquet | 1.186.859 / 1.797.488 | `probe_serapan.json` |
| Batas atas total zip / parquet | 25,86 GB / 39,17 GB | idem |
| Gerbang resample bulan AKHIR | 12/12 bersih, 0 beda pada 9 kolom | `uji_resample.json` |
| Gerbang resample bulan AWAL | 9 dari 12 gagal; 609 sel OHLC beda dari ~905.872 (0,067%) | idem |
| Bar asli dibandingkan | 226.468 pada 24 bulan | idem |
| Beda kolom non-OHLC | 20 sel, seluruhnya XRPUSDT 2020-01 | idem |

## Jumlah uji

53 menurut hitungan berkas (7 + 12 + 11 + 16 + 7 baru di
`tests/test_uji_resample.py`). Laporan CI untuk commit `aaf0f679` BELUM dibaca,
jadi angka 53 masih klaim, bukan angka terverifikasi. Angka terakhir yang
terverifikasi adalah 46 (run 30336075738).

## Utang verifikasi yang belum dibayar

1. Temuan A dan B (rasio isi 5,84%; 96% trendline break) menunggu juri.
2. Temuan G: klaim "30 pair dipilih alfabetis" belum ditemukan buktinya.
3. Atribut `enable_hs` dipakai `strategy.py` tetapi tidak ada di `config.py`.
4. Klaim temuan N (kendala mengikat = kapasitas margin) belum diuji angkanya.
5. Angka 0,3232R dan 0,306R warisan belum diverifikasi.
6. ~~Ukuran ADR-A001~~ DIBAYAR: 3.569 byte.
7. Percent-encoding simbol non-ASCII belum teruji.
8. ~~Klaim warisan 40-60 GB / 34.000 berkas~~ DIBAYAR: dibantah.
9. ~~Tanggal berhenti SRM/COCOS/BTS~~ DIBAYAR: 2024-05-28 UTC.
10. ~~R-5~~ DIBAYAR.
11. Peralihan format kini teruji 12 simbol; untuk 937 simbol masih klaim (R-19).
12. ~~Era tanpa header belum diuji resample~~ DIBAYAR: sudah diuji, dan hasilnya
    MERAH. Utangnya lunas; masalahnya baru dimulai.
13. ~~Medan `delisting_klaim_terbukti`~~ DIBAYAR.
14. ~~Satuan stempel 2024-06..2026-06~~ DIBAYAR.
15. **BARU**: sebab KC-6 belum terukur. Butuh pengukuran per-bucket: apakah bar
    yang `open`-nya beda berimpit dengan celah menit (R-26, R-27).
16. **BARU**: ADR-A004 (kebijakan bulan awal) belum ditulis; serapan penuh
    terkunci sampai ada.
17. **BARU**: laporan CI commit `aaf0f679` belum dibaca; jumlah uji 53 belum
    terverifikasi.
