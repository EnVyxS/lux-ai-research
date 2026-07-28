# STATE — versi 10

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
24. **[v10]** Setiap pengukuran sebab wajib memuat medan yang dapat MENGGUGURKAN
    hipotesis yang sedang saya percayai, dan medan itu dilaporkan walau nilainya
    nol. Instrumen yang hanya bisa membenarkan dugaan pembuatnya bukan instrumen.

## Kelas cacat

1. **KC-1 (modul warisan)** — pemilihan default berdasarkan paruh uji.
   Penangkalnya: pra-registrasi tertulis sebelum run.
2. **KC-2 (modul warisan)** — asimetri pencatatan: alasan setup dilewatkan
   dicatat, alasan setup diambil tidak.
3. **KC-3 (repo ini)** — guard berbasis pencarian kata; menjatuhkan CI run
   30311582627. Penangkalnya: aturan 12.
4. **KC-4 (repo ini)** — format arsip berubah di tengah sejarah: tanpa header
   s.d. 2021-12, berheader sejak 2022-01. Teruji pada 12 simbol.
5. **KC-5 (repo ini)** — label yang mengukur hal lain daripada namanya.
   DIPERBAIKI 2026-07-28 lewat `nilai_klaim_delisting`.
6. **KC-6 (arsip)** — berkas 1m dan berkas 5m/15m terbitan Binance TIDAK sepakat
   di bulan awal simbol. **Sebab kini terukur sebagian**: berkas 1m ternyata UTUH
   pada 12 dari 12 bulan awal (0 menit hilang, 0 duplikat, 0 jarak bukan 60
   detik), dan 0 dari 468 bucket ber-`open` beda punya menit pertama yang hilang.
   Hipotesis celah menit (H1) GUGUR. Yang bertahan: kedua berkas dibangun dari
   agregasi yang berbeda di sisi Binance (H2). Sebagian beda mencapai ~3%
   (XRPUSDT 2020-01: 0,1970 lawan 0,2032), jadi kebijakan berbentuk toleransi
   tidak sah. Yang BELUM terukur: berapa lama gejala ini bertahan sepanjang hidup
   simbol (R-30, R-31).

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
| R-12 | Resample pada bulan PERTAMA tiap simbol juga cocok eksak | MELESET: 609 sel OHLC beda |
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
| R-23 | Gerbang dua bulan lolos, `total_beda_kolom_jumlah` = 0 | MELESET pada kedua klausa |
| R-24 | `tanggal_tak_sepakat_dengan_isi` kosong | TEPAT |
| R-25 | `bulan_era_tanpa_header` = 10 | TEPAT |
| R-26 | ≥ 90% bucket `open` beda pada DOGE/BTS berimpit dengan celah menit | **MELESET: 0%** |
| R-27 | ETHUSDT 2020-01 benar-benar tanpa celah, sehingga H1 gugur untuk ETH | **TEPAT** |
| R-28 | 12 bulan akhir tetap 0 beda pada run berikutnya | menunggu |
| R-29 | `beda_tak_terjelaskan_h1` positif pada minimal dua simbol | **TEPAT: sembilan** |
| R-30 | Beda menurun dan mencapai nol dalam enam bulan pertama (DOGE, BTS) | menunggu |
| R-31 | Bulan kendali di tengah hidup simbol menunjukkan 0 beda | menunggu |

Cacah dihitung ulang baris demi baris (aturan 21):

- TEPAT — 16 baris: R-1, R-2, R-5, R-9, R-11, R-13, R-15, R-16, R-17, R-18,
  R-21, R-22, R-24, R-25, R-27, R-29.
- MELESET — 8 baris: R-4, R-6, R-8, R-10, R-12, R-14, R-23, R-26.
- MELESET SEPARUH — 1 baris: R-3.
- TIDAK TERADJUDIKASI — 0 baris.
- MENUNGGU — 6 baris: R-7, R-19, R-20, R-28, R-30, R-31.

16 + 8 + 1 + 0 + 6 = 31, sama dengan cacah baris R-1 sampai R-31. P-1 sampai P-3
dihitung terpisah dan ketiganya masih menunggu.

## Daftar ADR

- ADR-A001 — aturan dasar riset. DITERIMA.
- ADR-A002 — serapan data arsip. DITERIMA; §3 TERBANTAH SEBAGIAN: resample eksak
  terbukti untuk bulan akhir, TIDAK untuk bulan awal (KC-6).
- ADR-A003 — taksonomi rezim/klasifikasi. BELUM ADA.
- ADR-A004 — kebijakan bulan awal simbol menghadapi KC-6. WAJIB ADA sebelum
  serapan penuh. Dasar sebagian sudah terukur (H1 gugur, toleransi tidak sah);
  masih menunggu pengukuran SEJAUH MANA gejala bertahan (R-30, R-31).

## Status pipeline

| Tahap | Status |
|---|---|
| T0 Peta modul | SELESAI |
| T1 Serapan | Probe SELESAI (tiga run). Survei semesta SELESAI. Gerbang resample MERAH pada bulan awal; sebab terukur sebagian (H1 gugur); serapan penuh TERKUNCI sampai ADR-A004 |
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
| Peralihan format | tanpa header s.d. 2021-12; teruji 12 simbol | `uji_resample.json` |
| Satuan stempel | milidetik, 237 bulan disampel, seragam | `survei_semesta.json` |
| Rerata byte zip / parquet | 1.186.859 / 1.797.488 | `probe_serapan.json` |
| Batas atas total zip / parquet | 25,86 GB / 39,17 GB | idem |
| Gerbang resample bulan AKHIR | 12/12 bersih, 0 beda pada 9 kolom | `uji_resample.json` |
| Gerbang resample bulan AWAL | 9 dari 12 gagal; 609 sel OHLC beda dari ~905.872 | idem |
| Bar asli dibandingkan | 226.468 pada 24 bulan | idem |
| Beda kolom non-OHLC | 20 sel, seluruhnya XRPUSDT 2020-01 | idem |

## Angka diagnostik (bukan bukti, tidak menyentuh gerbang)

Sumber `reports/diagnosa_kc6.json`, run 30338666516, bertanda
`"bukan_bukti": true`:

| Besaran | Nilai |
|---|---|
| Bucket dibandingkan | 91.335 (68.501 pada 5m, 22.834 pada 15m) |
| Bucket `open` beda | 468 |
| Di antaranya menit pertama hilang | 0 |
| Bucket beda yang H1 tak bisa jelaskan | 470 |
| Bulan awal tanpa celah menit sama sekali | 12 dari 12 |
| Simbol dengan beda positif | 9 (DOGE 223, BTS 118, FTT 53, XRP 38, SRM 16, LINK 12, ETH 5, BNB 3, SOL 2) |

## Jumlah uji

**61, TERVERIFIKASI** — `reports/ci_terakhir.json`, run **30338666532**, commit
`1a5e0666`, `kode_keluar: 0`, `cacah_uji: "61 tests collected in 0.37s"`.

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
12. ~~Era tanpa header belum diuji resample~~ DIBAYAR: hasilnya MERAH.
13. ~~Medan `delisting_klaim_terbukti`~~ DIBAYAR.
14. ~~Satuan stempel 2024-06..2026-06~~ DIBAYAR.
15. ~~Sebab KC-6 belum terukur~~ DIBAYAR SEBAGIAN: H1 gugur, arsip 1m utuh.
    Sisanya menjadi utang 20.
16. ADR-A004 belum ditulis; serapan penuh terkunci sampai ada.
17. ~~Jumlah uji~~ DIBAYAR: 61 terverifikasi.
18. Jurnal 08 dan 09 belum pernah dibaca ulang dari `main`.
19. `reports/semesta_bulan_1m.json` (18.884 B) belum pernah dibaca.
20. **BARU**: sejauh mana KC-6 bertahan sepanjang hidup simbol belum terukur.
    Baru bulan pertama yang disampel (aturan 20). R-30 dan R-31 menunggu.
