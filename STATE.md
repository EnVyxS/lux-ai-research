# STATE — versi 15

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
    dari barisnya saat berkas diperbarui.
22. **[v8]** `sidik_kode` wajib mencakup SELURUH berkas yang ikut menentukan isi
    laporan, termasuk modul yang dipanggil dari modul lain.
23. **[v9]** Gerbang yang MERAH dilarang dilonggarkan sebelum sebab kegagalannya
    terukur. Toleransi, pengecualian bulan, dan ambang "cukup dekat" hanya boleh
    lahir dari ADR yang memuat angka terukur.
24. **[v10]** Setiap pengukuran sebab wajib memuat medan yang dapat MENGGUGURKAN
    hipotesis yang sedang saya percayai, dan medan itu dilaporkan walau nilainya
    nol.
25. **[v11]** Parameter cakupan sebuah pengukuran (mis. K bulan yang disampel,
    cara memilih bulan kendali) wajib dipatok tertulis SEBELUM run dan tidak
    boleh disetel ulang setelah hasilnya terlihat.
26. **[v12]** Ramalan yang memakai kata mutlak ("nol", "seluruh", "tidak ada")
    wajib disertai ramalan BESARAN pendamping.
27. **[v13]** Ramalan pendamping besaran dilarang BERSYARAT pada hasil ramalan
    lain. Ramalan bersyarat dihitung TIDAK TERADJUDIKASI.
28. **[v14]** Ekstrapolasi cacah dari sampel bulan AWAL ke bulan lain dilarang
    tanpa menyatakan bahwa bulan awal PARSIAL dan mengoreksinya. R-42 meleset
    46% justru karena mengalikan rerata bulan parsial dengan jumlah bulan penuh.
29. **[v15]** Bila sebuah ADR diamandemen, teks lama TIDAK dihapus. Amandemen
    ditulis sebagai bagian terpisah bernomor, dan penunjuk silang dipasang di
    kepala berkas DAN di kepala bagian yang diamandemen.

## Kelas cacat

1. **KC-1 (modul warisan)** — pemilihan default berdasarkan paruh uji.
2. **KC-2 (modul warisan)** — asimetri pencatatan setup diambil vs dilewatkan.
3. **KC-3 (repo ini)** — guard berbasis pencarian kata. Penangkalnya aturan 12.
4. **KC-4 (repo ini)** — format arsip berubah: tanpa header s.d. 2021-12,
   berheader sejak 2022-01. Teruji pada 12 simbol.
5. **KC-5 (repo ini)** — label yang mengukur hal lain daripada namanya.
   DIPERBAIKI lewat `nilai_klaim_delisting`.
6. **KC-6 (arsip)** — berkas 1m dan berkas 5m/15m terbitan Binance TIDAK
   sepakat. Terukur pada 84 simbol-bulan (12 simbol × 6 bulan awal + 1 kendali):
   - Deret 1m UTUH: 0 menit hilang, 0 duplikat, 0 jarak bukan 60 detik pada 84
     dari 84 simbol-bulan. Hipotesis celah menit (H1) mati.
   - Bulan awal: 2.530 dari **790.983** bucket beda = **0,3199%**.
   - Bulan kendali: 1 dari **140.544** = **0,0007%**, yaitu 457 kali lebih
     jarang, tetapi tidak nol (LINKUSDT 2023-04).
   - Gejalanya LANGKA, bukan lazim. Itu tidak mengubah ADR-A004, yang berdiri di
     atas besar beda (~3% pada XRPUSDT 2020-01) dan atas kenyataan bahwa ia tak
     pernah nol — bukan di atas lajunya.
   - Tidak ada N yang aman untuk "buang N bulan pertama": pada N = 6, DOGEUSDT
     masih 202 dan BTSUSDT masih 8.
   - **Diselesaikan oleh ADR-A004**, yang kini ADA DALAM KODE:
     `lux_ai/serapan/gerbang_1m.py`, dan tercatat sebagai Amandemen A-1 di
     `decisions/ADR-A002.md`.
   - BELUM terjawab: mana yang benar, 1m atau 5m/15m terbitan. Ini memerlukan
     verifikasi dari sumber independen yang tidak kami punya.

## Papan skor hipotesis

Kosong. Hipotesis selesai: 0. Kandidat: 0. Ditolak: 0. N_percobaan: 0.

## Papan skor prediksi

| # | Prediksi | Status |
|---|---|---|
| P-1 | Ekspektasi B0 di bawah 0,10R setelah biaya dan GAGAL kriteria 1 | menunggu |
| P-2 | Menyalakan detektor non-trendline tidak memperbaiki ekspektasi | menunggu |
| P-3 | Rasio isi rendah didominasi gerbang `rr1 < min_rr` dan `htf_score = 3` | menunggu |
| R-1 | Indeks arsip memuat lebih dari 450 simbol | TEPAT: 937 |
| R-2 | Minimal 3 dari 4 klaim delisting terbukti | TEPAT: 3 dari 4 |
| R-3 | Simbol-bulan 1m likuid 1,5-4 MB zip; parquet lebih kecil dari zip | MELESET SEPARUH |
| R-4 | Estimasi total lebih besar dari 40-60 GB | MELESET: 25,86 / 39,17 GB |
| R-5 | Berkas terbaru berheader, yang lama tidak | TEPAT |
| R-6 | OHLC cocok; volume beda tipis karena pembulatan | MELESET pada volume |
| R-7 | Total parquet semesta penuh di bawah 25 GB | menunggu |
| R-8 | Lebih dari 300 simbol berbulan terakhir lebih tua dari 2026-01 | MELESET: 121 |
| R-9 | Gerbang OHLC lolos untuk 12 simbol probe (bulan akhir) | TEPAT: 12/12 |
| R-10 | `trades` cocok, `quote_volume` beda sebagian | MELESET: cocok persis |
| R-11 | Run probe kedua mengulang 937 dan 21.789 persis | TEPAT |
| R-12 | Resample pada bulan PERTAMA tiap simbol juga cocok eksak | MELESET: 609 sel beda |
| R-13 | Peralihan format seragam dan jatuh sebelum 2022-04 | TEPAT: 2022-01 |
| R-14 | Lebih dari 300 simbol berstatus terhenti | MELESET: 128 |
| R-15 | Peralihan header monoton dan sama untuk ketiga simbol | TEPAT |
| R-16 | Seluruh bulan yang diperiksa memakai stempel milidetik | TEPAT (237 bulan) |
| R-17 | Tiga simbol mati berhenti pada tanggal UTC yang sama | TEPAT: 2024-05-28 |
| R-18 | Bulan 2024-06..2026-06 juga milidetik 13 digit | TEPAT |
| R-19 | Peralihan header 2022-01 berlaku untuk SELURUH simbol | menunggu |
| R-20 | Serapan penuh: 0 berkas non-milidetik, 0 pelanggaran batas header | menunggu |
| R-21 | Probe baru: terhenti SRM/COCOS/BTS, FTT masih terbit | TEPAT |
| R-22 | Angka infrastruktur terulang ketiga kali persis | TEPAT |
| R-23 | Gerbang dua bulan lolos, `total_beda_kolom_jumlah` = 0 | MELESET pada keduanya |
| R-24 | `tanggal_tak_sepakat_dengan_isi` kosong | TEPAT |
| R-25 | `bulan_era_tanpa_header` = 10 | TEPAT |
| R-26 | ≥ 90% bucket `open` beda DOGE/BTS berimpit dengan celah menit | MELESET: 0% |
| R-27 | ETHUSDT 2020-01 tanpa celah, sehingga H1 gugur untuk ETH | TEPAT |
| R-28 | 12 bulan akhir tetap 0 beda pada run berikutnya | menunggu |
| R-29 | `beda_tak_terjelaskan_h1` positif pada minimal dua simbol | TEPAT: sembilan |
| R-30 | DOGE & BTS: beda menurun dan mencapai nol dalam 6 bulan pertama | MELESET: DOGE naik s.d. 494 lalu 202; BTS bangkit 0 → 8 |
| R-31 | Bulan kendali menunjukkan 0 beda pada SELURUH simbol | MELESET: LINKUSDT 2023-04 = 1 |
| R-32 | ≥ 7 dari 9 simbol: beda bulan ke-6 < bulan ke-1 | TEPAT: 9 dari 9 |
| R-33 | `menit_hilang_total` dan `duplikat_total` tetap 0 di 84 bulan | TEPAT |
| R-34 | Minimal satu simbol masih beda > 0 pada bulan ke-6 | TEPAT: DOGE 202, BTS 8 |
| R-35 | Total beda bulan kendali < 10% total beda bulan pertama | TEPAT: 1 lawan 468 |
| R-36 | Serapan penuh: gerbang integritas 1m lolos ≥ 99% simbol-bulan | menunggu |
| R-37 | Simbol-bulan dengan menit hilang pada serapan penuh: 1..200 | menunggu |
| R-38 | CI commit gerbang: tepat 87 uji, kode keluar 0, percobaan pertama | TEPAT: run 30341471061 |
| R-39 | `ukur_deret` sepakat dengan `celah_menit` pada 4 kasus uji | TEPAT |
| R-40 | Bersyarat: bila R-39 kalah, medan berbeda ≤ 2 dari 36 | TIDAK TERADJUDIKASI (aturan 27) |
| R-41 | CI commit penyebut: tepat 90 uji, kode keluar 0, percobaan pertama | TEPAT: run 30342486568 |
| R-42 | Penyebut total 84 simbol-bulan antara 550.000 dan 750.000 | MELESET: 931.527 |
| R-43 | Laju open beda bulan awal antara 0,2% dan 0,8% | TEPAT: 0,3199% |

Cacah dihitung ulang baris demi baris (aturan 21):

- TEPAT — 24 baris: R-1, R-2, R-5, R-9, R-11, R-13, R-15, R-16, R-17, R-18,
  R-21, R-22, R-24, R-25, R-27, R-29, R-32, R-33, R-34, R-35, R-38, R-39, R-41,
  R-43.
- MELESET — 11 baris: R-4, R-6, R-8, R-10, R-12, R-14, R-23, R-26, R-30, R-31,
  R-42.
- MELESET SEPARUH — 1 baris: R-3.
- TIDAK TERADJUDIKASI — 1 baris: R-40.
- MENUNGGU — 6 baris: R-7, R-19, R-20, R-28, R-36, R-37.

24 + 11 + 1 + 1 + 6 = 43, sama dengan cacah baris R-1 sampai R-43. P-1..P-3
dihitung terpisah dan ketiganya masih menunggu.

## Daftar ADR

- ADR-A001 — aturan dasar riset. DITERIMA.
- ADR-A002 — serapan data arsip. DITERIMA; **§3 DIAMANDEMEN oleh ADR-A004**,
  tercatat sebagai bagian "Amandemen A-1" di dalam berkasnya sendiri (commit
  `4995940c7aeccf303900c19afb3320029b04b113`, blob
  `3017056456087297e0a83bacbc0d12e7d8e66d36`): kesamaan dengan 5m/15m terbitan
  bukan lagi gerbang, melainkan diagnostik.
- ADR-A003 — taksonomi rezim/klasifikasi. BELUM ADA.
- ADR-A004 — kebijakan KC-6. **DITERIMA 2026-07-28.** 1m satu-satunya sumber
  kebenaran; gerbang mengikat = integritas struktural deret 1m; 5m/15m terbitan
  tidak diserap; tanpa toleransi; tanpa pengecualian N bulan pertama.
  Penerapannya: `lux_ai/serapan/gerbang_1m.py`.

## Gerbang integritas 1m (ADR-A004 §2 dalam kode)

`lux_ai/serapan/gerbang_1m.py`, enam klausa per simbol-bulan:
`deret_tidak_kosong`, `tanpa_duplikat`, `tanpa_menit_hilang`, `jarak_60_detik`,
`selaras_menit`, `satuan_milidetik`. Klausa pertama tambahan operasional (berkas
kosong akan lolos kelima klausa lain secara hampa). Ringkasannya wajib memuat
`baris_diperiksa` dan `slot_diperiksa` (aturan 18) serta `simbol_bulan_gagal`
dan `pelanggaran_per_klausa` walau nol (aturan 24). Rumus `ukur_deret` DISALIN
dari `diagnosa_kc6.celah_menit`, bukan diimpor (aturan 10); uji perbandingan
medan bersama menjaga keduanya tidak menyimpang. Modul ini BELUM pernah melihat
data arsip sungguhan (utang 24).

## Status pipeline

| Tahap | Status |
|---|---|
| T0 Peta modul | SELESAI |
| T1 Serapan | Probe SELESAI. Survei semesta SELESAI. KC-6 terukur, diputus (ADR-A004), lajunya diketahui, dan amandemennya tercatat di ADR-A002. Gerbang integritas 1m ADA dalam kode dan teruji. Yang kurang: jalur serapan penuh + manifes per simbol-bulan |
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
| Gerbang resample bulan AKHIR | 12/12 bersih | `uji_resample.json` |
| Integritas 1m | 84 dari 84 simbol-bulan bersih sempurna | `rentang_kc6.json` |

## Angka diagnostik (bukan bukti)

`reports/rentang_kc6.json` (run 30339979270) dan `reports/penyebut_kc6.json`
(run 30342486655, `sidik_data` `7f389bed…a994c`), 84 simbol-bulan × 2 interval
= 168 simpul:

| Kelompok | simpul | bucket dibandingkan | open beda | laju |
|---|---|---|---|---|
| awal | 144 | 790.983 | 2.530 | 0,3199% |
| kendali | 24 | 140.544 | 1 | 0,0007% |
| total | 168 | 931.527 | 2.531 | 0,2717% |

Catatan: `bucket_ohlc_beda` awal = 2.532, dua lebih banyak daripada `open` beda.
Bulan ke-6 masih beda pada DOGEUSDT (202) dan BTSUSDT (8). Simbol bersih
sepenuhnya: BTCUSDT. `menit_hilang_total` dan `duplikat_total` = 0.

## Jumlah uji

**90, TERVERIFIKASI** — `reports/ci_terakhir.json`, run 30342486568, commit
`ac342940`, `kode_keluar: 0`, `"90 tests collected in 0.37s"`.

## Utang verifikasi yang belum dibayar

1. Temuan A dan B (rasio isi 5,84%; 96% trendline break) menunggu juri.
2. Temuan G: klaim "30 pair dipilih alfabetis" belum ditemukan buktinya.
3. Atribut `enable_hs` dipakai `strategy.py` tetapi tidak ada di `config.py`.
4. Klaim temuan N (kendala mengikat = kapasitas margin) belum diuji angkanya.
5. Angka 0,3232R dan 0,306R warisan belum diverifikasi.
6. ~~Ukuran ADR-A001~~ DIBAYAR.
7. Percent-encoding simbol non-ASCII belum teruji.
8. ~~Klaim warisan 40-60 GB / 34.000 berkas~~ DIBAYAR: dibantah.
9. ~~Tanggal berhenti SRM/COCOS/BTS~~ DIBAYAR: 2024-05-28 UTC.
10. ~~R-5~~ DIBAYAR.
11. Peralihan format teruji 12 simbol; untuk 937 simbol masih klaim (R-19).
12. ~~Era tanpa header belum diuji resample~~ DIBAYAR.
13. ~~Medan `delisting_klaim_terbukti`~~ DIBAYAR.
14. ~~Satuan stempel 2024-06..2026-06~~ DIBAYAR.
15. ~~Sebab KC-6~~ DIBAYAR: H1 gugur, arsip 1m utuh.
16. ~~ADR-A004~~ DIBAYAR: diterima 2026-07-28.
17. ~~Jumlah uji berstatus klaim~~ DIBAYAR: kini 90 terverifikasi.
18. ~~Jurnal 08 dan 09 belum dibaca ulang dari `main`~~ DIBAYAR.
19. `reports/semesta_bulan_1m.json` (18.884 B) belum pernah dibaca. Jangan
    dibaca utuh; ringkas di runner seperti pola `penyebut_kc6.py`.
20. ~~Sejauh mana KC-6 bertahan~~ DIBAYAR: 84 simbol-bulan (jurnal 16).
21. ~~Penyebut `rentang_kc6.json`~~ DIBAYAR: 790.983 awal, 140.544 kendali,
    931.527 total (jurnal 20).
22. ~~Catatan silang amandemen §3 di `decisions/ADR-A002.md`~~ DIBAYAR: commit
    `4995940c`, bagian Amandemen A-1 + penunjuk di kepala berkas dan kepala §3;
    berkas sudah dibaca ulang dari `main` dan ekornya hadir.
23. ~~Gerbang integritas 1m belum ada dalam kode~~ DIBAYAR: `gerbang_1m.py`.
24. `gerbang_1m` belum pernah melihat data arsip sungguhan dan belum dipanggil
    jalur serapan mana pun. Sampai itu terjadi, kalimat "gerbang integritas
    berlaku atas 21.789 simbol-bulan" dilarang ditulis.

Utang AKTIF yang tersisa dan bisa dikerjakan sekarang: **19** dan **24**.
Utang 1-5, 7, dan 11 menunggu tahap lain.
