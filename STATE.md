# STATE — versi 19

Diperbarui: 2026-07-28 (sesi 40). Aturan hanya BERTAMBAH; jangan menulis ulang
dari ingatan. v19 disusun di atas teks v18 (blob
`8b3dd4160ec3e1ffdbda069c77f6ddd04579e951`) yang dibaca ulang dari `main` pada
sesi yang sama, ditambah hasil run taksonomi.

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
30. **[v16]** Setiap laporan diagnostik wajib memuat PENYEBUT-nya secara
    eksplisit, dan bila penyebut itu nol, laporan wajib berstatus
    `TIDAK MENGUKUR`. Ramalan atas medan penggugur DILARANG diadjudikasi TEPAT
    bila penyebutnya nol; status yang benar adalah TIDAK TERADJUDIKASI.
31. **[v16]** Setiap laporan wajib mencatat `sidik_data` sumbernya, dan setiap
    perbandingan antar-run wajib menyebut apakah `sidik_data`-nya sama. Cacah
    byte TIDAK cukup membuktikan dua pengukuran memakai masukan yang sama.
32. **[v16]** Nama pasar TIDAK boleh dianggap ASCII. Setiap penyaring nama wajib
    mencatat CACAH dan CONTOH yang ditolaknya; menolak tanpa mencatat dilarang.
    Pada serapan, nama simbol wajib di-percent-encode saat menyusun URL arsip,
    dan nama berkas keluaran wajib diamankan untuk sistem berkas.
33. **[v17]** Workflow yang menyentuh jaringan wajib dipicu oleh berkas yang
    benar-benar dipakainya, bukan oleh pola direktori. Bila cakupan pemicu
    diperluas, alasannya wajib ditulis di jurnal pada commit yang sama.
34. **[v17]** Dilarang meng-commit direktori laporan secara borongan (`git add
    reports` atau `git add -A reports/`). Setiap workflow hanya boleh meng-add
    berkas yang dinamainya sendiri.
35. **[v18]** Berkas laporan yang TIDAK memuat `sidik_kode` dilarang dikutip
    sebagai sumber angka di STATE maupun di ADR. Ia hanya boleh dikutip sebagai
    petunjuk, dengan penanda "belum bersidik" menempel pada kutipannya.
36. **[v19]** Bila dua laporan memberi angka berbeda untuk besaran yang namanya
    sama, DEFINISI keduanya wajib ditulis berdampingan sebelum salah satunya
    dipakai, dan selisihnya wajib dilacak sampai ke entitas yang berpindah sisi.
    Selisih kecil dilarang dibulatkan hilang.

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
   - Bulan kendali: 1 dari **140.544** = **0,0007%**, 457 kali lebih jarang,
     tetapi tidak nol (LINKUSDT 2023-04).
   - Tidak ada N yang aman untuk "buang N bulan pertama": pada N = 6, DOGEUSDT
     masih 202 dan BTSUSDT masih 8.
   - **Diselesaikan oleh ADR-A004**, ada dalam kode `lux_ai/serapan/gerbang_1m.py`,
     tercatat sebagai Amandemen A-1 di `decisions/ADR-A002.md`.
   - BELUM terjawab: mana yang benar, 1m atau 5m/15m terbitan. Ini memerlukan
     verifikasi dari sumber independen yang tidak kami punya.
7. **KC-7 (repo ini)** — laporan yang tampak BERSIH padahal penyebutnya NOL.
   Penangkalnya aturan 30.
8. **KC-8 (repo ini)** — sumber bergerak, dikira tetap, karena hanya UKURANNYA
   yang dicocokkan. SEBABNYA DIKETAHUI (jurnal 33–34). Penangkalnya aturan 31.
9. **KC-9 (repo ini)** — penyaring ASCII-sentris membuang entitas SAH tanpa
   jejak. Tiga pasar Tionghoa, 19 berkas-bulan. Penangkalnya aturan 32. Titik
   (a) URL arsip AMAN, dijaga enam uji. **Lokasinya pasti**: penyaring hidup di
   `ringkas_semesta`, BUKAN di `survei.py`; ketiga nama hadir utuh di
   `semesta_rentang.json` dan di `taksonomi_semesta.json`.
10. **KC-10 (repo ini)** — pemicu LUAS pada workflow berjaringan. Sensus penuh:
    **1 dari 10** workflow (`probe_serapan.yml`). Penangkalnya aturan 33.
11. **KC-11 (repo ini)** — commit borongan direktori laporan. Sensus:
    **6 dari 10** workflow melanggar; patuh: `ci`, `ringkas_semesta`,
    `bentuk_semesta`, `taksonomi_semesta`. Penangkalnya aturan 34.
12. **KC-12 (repo ini)** — laporan TANPA SIDIK. `reports/semesta_rentang.json`
    hanya punya satu kunci tingkat atas (`rentang`). **Ditutup untuk berkas ini
    lewat turunan bersidik** `reports/taksonomi_semesta.json`; berkas aslinya
    tetap tak bersidik dan dilarang dikutip langsung (aturan 35).

## Papan skor hipotesis

Hipotesis RISET: kosong. N_percobaan: 0.

Hipotesis INFRASTRUKTUR (tidak masuk N_percobaan): H1 GUGUR; H2 bertahan;
**H-A002a TERBUKTI** (dikuatkan tiga kali: 937−934, 9+6+4 = 19, dan
`non_ascii.jumlah_bulan` = 19); H-A002b GUGUR; H-A003 inti TERBUKTI namun
mekanismenya salah; H-A004 GUGUR; H-A005 GUGUR.

## Papan skor prediksi

R-1..R-55 di STATE v16 (blob `dd997064…`): TEPAT 31, MELESET 15, SEPARUH 2,
TIDAK TERADJUDIKASI 1, MENUNGGU 6.
R-56..R-82 di STATE v17 (blob `1991c374…`): TEPAT 15, MELESET 9, SEPARUH 2,
TIDAK TERADJUDIKASI 1.
R-83..R-85 di STATE v18 (blob `8b3dd416…`): TEPAT 1 (R-84), MELESET 1 (R-85),
TIDAK TERADJUDIKASI 1 (R-83).

Baru pada v19, semuanya dari run taksonomi (laporan blob `42d07af7…`):

| # | Prediksi | Status |
|---|---|---|
| R-86 | `cacah_simbol` = 937 (pita 930..940) | TEPAT |
| R-87 | Jumlah `cacah_bulan` = 21.789 (pita 21.700..21.900) | TEPAT |
| R-88 | Non-ASCII: 3 simbol, 19 bulan | TEPAT |
| R-89 | Futures kedaluwarsa 40..60; SETTLED 12..20 | TEPAT (50; 15) |
| R-90 | CI hijau percobaan pertama, 110 uji | TEPAT |

**Total R-1..R-90** (aturan 21): TEPAT 31+15+1+5 = **52**; MELESET 15+9+1 =
**25**; MELESET SEPARUH **4**; TIDAK TERADJUDIKASI **3**; MENUNGGU **6**
(R-7, R-19, R-20, R-28, R-36, R-37). 52+25+4+3+6 = **90**. ✅

Catatan kejujuran: empat dari lima TEPAT itu meramalkan isi berkas yang sudah
saya lihat 95%-nya. Yang benar-benar berisiko hanya R-89 dan R-90.
Ramalan berikutnya **R-91**.

## Daftar ADR

- ADR-A001 — aturan dasar riset. DITERIMA.
- ADR-A002 — serapan data arsip. DITERIMA; **§3 DIAMANDEMEN oleh ADR-A004**
  (Amandemen A-1, commit `4995940c…`).
- ADR-A003 — taksonomi rezim/klasifikasi. BELUM ADA.
- ADR-A004 — kebijakan KC-6. DITERIMA. 1m satu-satunya sumber kebenaran; tanpa
  toleransi; tanpa pengecualian N bulan pertama. Penerapannya `gerbang_1m.py`.

## Gerbang integritas 1m (ADR-A004 §2 dalam kode)

Enam klausa: `deret_tidak_kosong`, `tanpa_duplikat`, `tanpa_menit_hilang`,
`jarak_60_detik`, `selaras_menit`, `satuan_milidetik`. Ringkasan wajib memuat
`baris_diperiksa`, `slot_diperiksa`, `simbol_bulan_gagal`,
`pelanggaran_per_klausa` walau nol. `ukur_deret` DISALIN dari
`diagnosa_kc6.celah_menit`, bukan diimpor (aturan 10).

**Cacat rumus yang sengaja dibiarkan:** `menit_hilang_dalam_rentang` bisa
NEGATIF bila dua stempel jatuh pada menit yang sama; penangkapnya klausa
`selaras_menit`. Medan itu DILARANG dipakai sendirian.

Modul ini BELUM pernah melihat data arsip sungguhan (utang 24).

## Taksonomi semesta arsip (TERUKUR, bersidik)

Sumber: `reports/taksonomi_semesta.json`, blob `42d07af7…`,
`sidik_kode` `f19e89d2…`, `sidik_data` `6128fbb0…`, `bukan_bukti: true`,
`entri_dibaca` 937, `cacah_entri_cacat` 0, `cacah_tak_tergolong` **0**.

| Jenis | Simbol | Bulan |
|---|---|---|
| perpetual_usdt | 787 | 19.598 |
| futures_kedaluwarsa | 50 | 258 |
| perpetual_busd | 41 | 812 |
| perpetual_usdc | 39 | 893 |
| sisa_settled | 15 | 36 |
| indeks | 3 | 151 |
| basis_non_fiat | 1 | 39 |
| perpetual_usd1 | 1 | 2 |
| tak_tergolong | 0 | 0 |

Jumlah: 937 simbol ✅, 21.789 bulan ✅. **150 simbol (16,0%) dan 2.191 bulan
(10,1%) BUKAN perpetual USDT.**

Batas yang diakui laporan itu sendiri: saham, ETF, dan komoditas token
(AAPLUSDT, XAUUSDT, …) tidak dapat dipisahkan dari perpetual koin lewat bentuk
nama; mereka masih terhitung `perpetual_usdt`. Memisahkannya menuntut daftar
instrumen dari bursa. **Ini memerlukan verifikasi.**

## Sensus workflow (10 workflow)

Patuh aturan 34: `ci`, `ringkas_semesta`, `bentuk_semesta`,
`taksonomi_semesta` = **4**. Melanggar (`git add reports` borongan):
`survei_semesta`, `penyebut_kc6`, `diagnosa_kc6`, `rentang_kc6`, `uji_resample`,
`probe_serapan` = **6**. 4 + 6 = **10**. ✅ Pemicu luas: hanya `probe_serapan`
(330 mnt, `lux_ai/serapan/**`, plus gelung latar `while true`).

## Angka arsip terverifikasi

| Besaran | Nilai | Sumber |
|---|---|---|
| Simbol di indeks arsip | 937 | `probe_serapan.json`, `taksonomi_semesta.json` |
| — bernama non-ASCII | 3 (19 bulan) | `taksonomi_semesta.json` |
| Berkas bulanan 1m | 21.789 | probe; dikonfirmasi silang oleh jumlah `cacah_bulan` |
| Rentang arsip | 2020-01 s.d. 2026-06 | `survei_semesta.json`, taksonomi |
| Simbol terhenti / hidup | **128/809 (survei) vs 129/808 (taksonomi)** | utang 28 |
| Peralihan format | tanpa header s.d. 2021-12; teruji 12 simbol | `uji_resample.json` |
| Satuan stempel | milidetik, 237 bulan disampel, seragam | `survei_semesta.json` |
| Batas atas zip / parquet | 25,86 GB / 39,17 GB | `probe_serapan.json` |
| Integritas 1m | 84 dari 84 simbol-bulan bersih | `rentang_kc6.json` |

## Jumlah uji

**110, TERVERIFIKASI** — `reports/ci_terakhir.json`, run **30351993293**,
commit `86af7163…`, 2026-07-28T10:45:22Z, `kode_keluar: 0`,
`"110 tests collected in 0.39s"`.

## Utang verifikasi

1-5. Menunggu tahap juri/klasifikasi (rincian di v16). 6-23 DIBAYAR.
24. **AKTIF — serapan penuh.** `gerbang_1m` belum pernah melihat data arsip
    sungguhan. Sampai itu terjadi, kalimat "gerbang integritas berlaku atas
    21.789 simbol-bulan" dilarang ditulis. Delapan syarat rancangan:
    (a) nama berkas parquet diamankan untuk sistem berkas;
    (b) kunci manifes sadar non-ASCII sejak baris pertama;
    (c) `baris_dibuang` wajib masuk manifes (aturan 18);
    (d) `menit_hilang_dalam_rentang` dilarang tanpa `selaras_menit`;
    (e) commit hanya berkas bernama (aturan 34);
    (f) pemicu workflow sempit (aturan 33);
    (g) tambalan enam workflow pelanggar aturan 34 + tiga cacat `probe_serapan`
        digabung ke commit yang sama;
    (h) `jenis_instrumen` per simbol — **separuh terbayar**: aturannya sudah
        tertulis dan diuji di `lux_ai/semesta/taksonomi.py` (8 uji), cacah per
        jenis sudah ada. Sisanya: memutuskan jenis mana yang MASUK backtest.
        Rekomendasi awal, belum diputuskan: perpetual USDT saja pada tahap
        pertama.
25-27. LUNAS. Utang 27 dibayar sesi 40 lewat `taksonomi_semesta.json`.
28. **[v19, baru]** Selisih **129 vs 128** simbol terhenti antara taksonomi dan
    survei. Diduga perbedaan definisi (`bulan_terakhir < 2026-06` lawan
    `JEDA_MATI_BULAN=2` terhadap `BATAS_R8`), tetapi simbol yang berpindah sisi
    BELUM diidentifikasi. Aturan 36 melarang membiarkannya.

Utang AKTIF: **24 dan 28**. Utang 1-5 dan 11 menunggu tahap lain.

## Temuan sampingan yang belum diukur

- `.decode("utf-8", "replace")` di `klines` membungkam byte rusak. **Perlu
  verifikasi.**
- `arsip.bulan_tersedia` untuk simbol Tionghoa: belum diperiksa.
- Anomali tree: calon penjelasannya gelung latar `probe_serapan` (KC-11).
  **Belum dibuktikan langsung.**
- Daftar `INDEKS` di taksonomi hanya tiga nama dan disusun manual. Bila ada
  indeks lain di semesta, ia kini terhitung sebagai perpetual. **Perlu
  verifikasi.**
