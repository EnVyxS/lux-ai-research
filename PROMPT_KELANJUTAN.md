# PROMPT KELANJUTAN — versi 40

Ditulis 29 Juli 2026, 21:10 WIB (sesi 55, lanjutan kelima). Menggantikan v39 (blob
`cddded62`). Berkas di repo adalah kebenaran; prompt ini hanya peta dan boleh saja
tertinggal.

Kamu melanjutkan riset LUX-AI. Operator: Diva Juan Nur Taqarrub, GitHub EnVyxS,
zona waktu Asia/Jakarta, bahasa kerja Indonesia. Tenggat: **2 Agustus 2026**.
Jangan mulai bekerja sebelum menyelesaikan LANGKAH 0.

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun; dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`, dengan
   `owner` dan `repo` HANYA di dalam `toolArguments`, tidak di tingkat atas.
3. Baca dari `main` repo `EnVyxS/lux-ai-research`, berurutan:
   - berkas ini;
   - **`STATE.md` v37 — PALING PENTING dan MUTAKHIR** (blob
     **`f520d5e2a50c17c43f6af73c6b2b5701c59d1f0b`**, sudah diverifikasi utuh
     sesudah push, aturan 52). Ia memuat aturan 1–66, KC-1..KC-29, papan skor
     R-1..R-267, semesta riset `perpetual_usdt`, kedua tabel taksonomi,
     penguraian 163 = 12 + 151, tabel penyebut per tahun, tabel `ukur_baris` V5,
     ringkasan API modul yang sudah terbaca, dan cacah uji 610. **Baca UTUH
     sebelum menulis ulang sebaris pun.**
   - `journal/2026-07-29-100.md` (utang `INDEKS` LUNAS, aturan 66 dikoreksi,
     KC-28 disempitkan, KC-29 lahir, praregistrasi R-265..R-267) dan
     `journal/2026-07-29-101.md` (adjudikasi R-265/R-266/R-267);
   - `journal/2026-07-29-98.md` dan `-99.md` bila perlu asal-usul aturan 65,
     KC-27, KC-28, dan daftar 51 nama `TAK_DIKENAL`;
   - `journal/2026-07-29-92.md`, `-93.md`, `-94.md` bila menyalin rincian baris
     **R-236..R-247** ke papan skor — satu-satunya utang papan skor yang tersisa;
   - `lux_ai/semesta/taksonomi.py` bila menyentuh penggolongan instrumen;
     `lux_ai/serapan/semesta_kuota.py` V3 bila menyentuh cacahan semesta;
     `lux_ai/serapan/bulan_settled.py` V1 bila menyentuh H-A013/H-A014;
     `lux_ai/serapan/ukur_baris.py` V5 bila menyentuh pengukuran baris;
   - `decisions/ADR-A006.md` (DITERIMA), `ADR-A007.md` (masih DIUSULKAN);
     `ADR-A002.md`/`ADR-A004.md` bila menyentuh serapan; `PETA_MODUL.md` bila
     menyentuh modul warisan.
4. Baru setelah itu jalankan pekerjaan teknis.

## BATASAN YANG MAHAL DIPELAJARI ULANG

Sandbox agen TIDAK punya jaringan; semua unduhan dan pengukuran arsip dijalankan
GitHub Actions, dan agen hanya boleh percaya artefak yang di-commit. Tidak ada
alat membaca status Actions dan tidak ada alat memicu `workflow_dispatch`; status
hanya diketahui dari berkas laporan yang di-commit workflow itu sendiri, dan
satu-satunya cara menyalakan run adalah push ke berkas yang tersebut di `paths`
workflow. Tidak ada API patch — `push_files` menulis ulang SELURUH isi berkas;
karena itu jangan pernah menulis ulang `STATE.md` atau berkas panjang lain sebelum
membacanya utuh, dan sesudah mendorong berkas panjang BACA ULANG dari `main`
(aturan 52). Saat memeriksa hasil run, cocokkan commit/run_id/sidik_kode; jangan
percaya keberadaan berkas (aturan 38) — **perangkap ini menyala dua kali lagi di
sesi 55**: sesudah push, laporan yang terbaca masih memuat commit run SEBELUMNYA
dengan blob yang tampak wajar. Yang menyelamatkan bukan blob melainkan
`list_commits` dengan `path="reports/ci_terakhir.json"` (penulis lux-ci, nomor run
ada di pesan commit "laporan CI \<run_id\> [skip ci]"). `search_code` mengembalikan
0 hasil — pakai `get_file_contents`; path berakhiran garis miring melisting
direktori, dan listing `reports/` TERPOTONG — pakai path berkas langsung, atau
`minimal_output: true` untuk listing panjang. Runner punya numpy, pandas, pyarrow,
pyyaml, pytest; TIDAK ada scipy dan requests; `data.binance.vision` bisa diakses,
`fapi.binance.com` memberi 451. Dilarang menulis apa pun di luar repo
`lux-ai-research`; `lux-research` boleh DIBACA saja, hasil dan angkanya tidak
pernah boleh masuk.

## POSISI (29 Juli 2026, 21:10 WIB)

HEAD saat prompt ini ditulis: **`5b968b2a7c5987d4ff4ce3ac58f10e2a420e57a6`**
(STATE v37); commit berikutnya adalah commit yang memuat berkas ini.

Rantai sesi 55, lanjutan: `2aafc561` (jurnal 98) → **`3a3e85e1`**
(`semesta_kuota` V2) → **`e4276b71`** (jurnal 99) → **`2b247d61`** (jurnal 100) →
**`db4a192d`** (`semesta_kuota` V3) → runner `100fdffa` dan `267396a0` → jurnal
101 → **`5b968b2a`** (STATE v37) → PROMPT v40.

Run TERVERIFIKASI (commit dicocokkan, aturan 38), semuanya kode 0:

| run | commit | isi |
|---|---|---|
| 30452311150 | `9d6ce310` | CI 552 butir |
| 30452448908 | `709b4728` | CI 552 butir |
| 30454633506 | `f5cebf04` | `semesta_kuota` V1 |
| 30454633453 | `f5cebf04` | CI **584** butir |
| 30455491987 | `3a3e85e1` | `semesta_kuota` V2 |
| 30455491991 | `3a3e85e1` | CI **598** butir |
| **30456422183** | **`db4a192d`** | **`semesta_kuota` V3** |
| **30456421973** | **`db4a192d`** | **CI 610 butir** |

Riwayat CI: … 526 → 552 → **584** → **598** → **610**.

Papan skor R-1..R-267: TEPAT **190** / MELESET **47** / SEPARUH **16** / TIDAK
TERADJUDIKASI **7** / MENUNGGU **7** = **267** (190+47 = 237; +16 = 253; +7 = 260;
+7 = 267). MENUNGGU: R-7, R-19, R-20, R-28, R-36, R-37, R-199 — **R-249 sudah
keluar dari MENUNGGU menjadi TEPAT** (19.749). R-268 SUDAH dipraregistrasi di
STATE v37; ramalan berikutnya **R-269**. Aturan sampai **66**. Kelas cacat sampai
**KC-29**. Jurnal berikutnya **102**. STATE berikutnya **v38**. PROMPT berikutnya
**v41**. ADR berikutnya **A009**.

## PEKERJAAN PERTAMA DI SESI BARU — adjudikasi yang MENGGANTUNG

- **R-268** (praregistrasi di STATE v37): pada commit **`5b968b2a`** — commit yang
  menyentuh `STATE.md` — `ci.yml` MENYALA sedangkan `semesta_kuota.yml` dan
  `ukur_baris.yml` TIDAK, dan `reports/ci_terakhir.json` akan melaporkan **610
  butir** dengan `kode_keluar` **0**. Ini ramalan **MUDAH** dan sudah disebut
  begitu di muka. **Peringatan:** push PROMPT v40 juga menyalakan `ci.yml`,
  sehingga laporan `5b968b2a` mungkin TERTIMPA. Bila medan `commit` bukan
  `5b968b2a`, cari commit runner lewat `list_commits` dengan
  `path="reports/ci_terakhir.json"` lalu baca pada ref itu (aturan 38).
- **R-269 wajib dipraregistrasi SEBELUM run berikutnya**, bukan sesudahnya.

## ADJUDIKASI SESI 55 — sudah selesai, jangan diulang

- **R-248 TEPAT** (H-A013 menang 6/6) · **R-250 TEPAT** (552, mudah) · **R-251
  TEPAT** (24/24) · **R-252 TEPAT** (kendali 78) · **R-253 TEPAT** (552, mudah) ·
  **R-254 TEPAT** · **R-255 SEPARUH** (705 SERI → aturan 64, KC-26) · **R-256
  TEPAT** (552, mudah).
- **R-249 TEPAT** — bulan USDT bukan-SETTLED di arsip **19.749** > 19.586.
- **R-257 MELESET** — himpunan berakhiran-USDT **790**, bukan 787; selisihnya
  ketiga `INDEKS`.
- **R-258 MELESET, dan klaimnya DICABUT** — "150 hanya-arsip hampir seluruhnya
  BUSD/USDC" salah: **80 dari 147** (54,4%). → aturan 65, KC-27.
- **R-259 TEPAT** (kendali 78) · **R-260 TEPAT** (584) · **R-261 TEPAT** (penyebut
  bersih; 3 nama USDT hanya-arsip) · **R-262 TEPAT** (mudah).
- **R-263 MELESET dan TERBALIK** — sumbangan ketiga nama USDT hanya-arsip
  **151** bulan, bukan ≤60. Dua kali salah pada himpunan yang sama (R-257, R-263)
  dengan sebab identik: saya membayangkan hanya-arsip sebagai banyak nama berumur
  pendek, padahal ia memuat sedikit nama berumur sangat panjang. **Yang salah
  berulang adalah dugaan BENTUK SEBARAN, bukan angkanya.**
- **R-264 TEPAT** (598, mudah) · **R-265 TEPAT** (kesembilan angka
  `per_jenis_hanya_arsip`) · **R-266 TEPAT dari DUA arah** · **R-267 TEPAT** (610,
  mudah).

## TEMUAN MUTAKHIR YANG WAJIB DIBAWA

- **SEMESTA RISET = `perpetual_usdt` = penyebut 787, TERBUKTI DUA ARAH.**
  `cacah_perpetual_usdt_luar_penyebut` **0** dan
  `cacah_penyebut_bukan_perpetual_usdt` **0**, keduanya berdaftar kosong. Karena
  kedua arah nol, ini **kesamaan himpunan**, bukan himpunan bagian. Kebersihan
  penyebut dari kontrak bertanggal dan indeks **DIRANCANG** — `pecahan.py`
  menyatakannya di baris pertama docstring dan menyaring lewat
  `taksonomi.jenis_instrumen`.
- **Sembilan kelas kanonik** (`lux_ai/semesta/taksonomi.py`, blob `b418c7ba`),
  urutan pemeriksaan MENGIKAT: ekspirasi `_\d{6}$` → `SETTLED` → `INDEKS` →
  kutipan `("USDT","USDC","BUSD","USD1","BTC")`. `INDEKS` = {`DEFIUSDT`,
  `BTCDOMUSDT`, `BLUEBIRDUSDT`} — utang "3 nama manual" **LUNAS**; 790 = 787 + 3.
- **Batas yang wajib ikut disebut:** token saham, ETF, dan komoditas
  (`AAPLUSDT`, `XAUUSDT`) tidak dapat dibedakan lewat bentuk nama, jadi mereka
  **IKUT di dalam 787** (`taksonomi.CATATAN_BATAS`). Kadar kematian DILARANG
  ditafsirkan sebagai sifat "pasar kripto".
- **Aturan 66 [bentuk REVISI]:** setiap cacahan semesta wajib menyebut KELAS
  INSTRUMEN, dan STATE wajib memuat batas semesta yang sudah ditegakkan KODE.
  Bagian tambahan yang lahir dari kesalahan saya sendiri: **sebelum menuduh
  sebuah batas tidak ada, berkas penyaringnya WAJIB dibaca lebih dulu —
  ketidaktahuan pembaca bukan cacat rancangan.**
- **Aturan 65 dan KC-27:** setiap daftar contoh wajib menyebut CARA pemilihannya;
  daftar yang bukan seluruhnya hanya boleh membuktikan KEBERADAAN, tidak pernah
  PROPORSI. Kalimat "hampir seluruhnya BUSD/USDC" lahir dari 18 contoh urut abjad
  dan sempat masuk ke aturan 63, KC-25, dan STATE v36 sekaligus.
- **KC-28 DIBATASI:** pencampuran kelas instrumen berlaku atas arsip **937**,
  BUKAN atas penyebut 787.
- **KC-29 — taksonomi PARALEL:** `semesta_kuota` V1/V2 mengarang klasifikasi
  sendiri padahal taksonomi kanonik sudah dipakai gerbang serapan. Akibatnya
  `TAK_DIKENAL` 51 nama yang saya perlakukan sebagai misteri ternyata **50
  `futures_kedaluwarsa` + 1 `perpetual_usd1`** (`BTCUSD1`, 2 bulan). Akibat kedua,
  lebih halus: sampai V2 `taksonomi.py` TIDAK ikut `sidik_kode` — lubang aturan 22
  yang tak pernah menyala karena tak pernah diuji. Tidak satu pun angka V1/V2
  batal; yang rusak PENAMAAN dan TAFSIR.
- **Penguraian selisih 163 = 12 + 151, `identitas_utuh` true.** 151 bulan
  SELURUHNYA milik ketiga indeks. **Kesamaan angka 12 dengan 12 simbol-bulan
  karantina BUKAN bukti identitas himpunan** — nama dan bulannya belum dicocokkan.
- **Tafsir kebangkitan tetap DILEMAHKAN:** dua bersambung (ICPUSDT 2022-09,
  TLMUSDT 2023-03) dan enam peralihan nama; kecocokan bulan membuktikan PENAMAAN
  kontrak, bukan perdagangan (KC-18). **H-A014 masih BELUM DIUJI.**
- **DUA konvensi nama SETTLED hidup berdampingan:** `ICPUSDT_SETTLED` bergaris
  bawah; `TLMUSDTSETTLED` dan keenam saudara peralihan TANPA. Docstring
  `penyebut_tahun.py` masih salah — jangan disunting, cukup jangan diwarisi.
- **KC-23/aturan 61:** LITUSDT MATI 2025-02..2025-11; kematian MENDAHULUI
  hilangnya funding (2025-07). Tafsir tebing funding TERBALIK. ADR-A002 §10 tidak
  boleh diubah atas bukti kohort semata.

## ANGKA TERVERIFIKASI (kutip dari laporan, jangan hitung dari udara)

**Semesta:** 787 penyebut = seluruh `perpetual_usdt` / 937 arsip / 150 hanya-arsip
(= 147 bukan-akhiran-USDT + 3 indeks) / 0 hanya-penyebut / 21.789 bulan arsip /
2.191 bulan hanya-arsip / 19.598 bulan milik penyebut / 15 nama SETTLED di arsip
dan 0 di penyebut / 790 nama berakhiran USDT.

**Per jenis kanonik (nama, bulan):** `perpetual_usdt` 787/19.598 ·
`futures_kedaluwarsa` 50/258 · `perpetual_busd` 41/812 · `perpetual_usdc` 39/893 ·
`sisa_settled` 15/36 · `indeks` 3/**151** · `perpetual_usd1` 1/2 ·
`basis_non_fiat` 1/39 · `tak_tergolong` **0/0**. Jumlah 937 dan 21.789 ✅

**Per kuota lokal (nama arsip / hanya-arsip):** USDT 805/18 · TAK_DIKENAL 51/51 ·
BUSD 41/41 · USDC 39/39 · BTC 1/1. BUSD+USDC di antara 147 = **80** (54,4%).

**Kehidupan:** 19.598 simbol-bulan, lolos 19.586, gagal 12 (karantina, tar
terpisah); MATI **1.401** / SEPI **98** / HIDUP **18.087**; 839.842.134 baris
(lolos 839.325.999 + karantina 516.135); funding **880** lubang, bentuk lokal
{awal 45, ekor 826, tengah 6}; 33 HIDUP tanpa funding; `cacah_simbol_tanpa_hidup`
**18**; penyebut per tahun 504/1.385/1.729/2.400/3.570/5.948/4.050 dengan
`bagian_mati` 0,001984/0,006498/0,019665/0,042917/0,053782/0,085071/**0,137284**
(menanjak monoton).

**Bulan ARSIP:** CTK 68, CVC 68, CVX 46, LIT 65, MAVIA 29, SLP 33, ICP 62
(`ICPUSDT_SETTLED` 9), TLM 60 (`TLMUSDTSETTLED` 9), BNX **51** (48 di PENYEBUT,
3 lubang tengah 2022-04/-06/-08); `jumlah_bulan_didaftar` 518 atas 24 nama; total
bulan SETTLED 36.

**Sidik terbaru:** `semesta_kuota` V3 `sidik_kode`
`ef0c4a2429a713f2fd8769bfd8488fc6b4925816875d4e1aaf82623f6dfa7eaa`, `sidik_data`
`6bb4ec0d…c10e` (tak berubah sejak V1 — masukan sama, kode lain).

**Cacah baris `ukur_baris` V5 (21 berkas, total 8.131):** tabelnya lengkap di STATE
v37; terbesar **705 SERI** (`funding.py`, `silang_funding.py`), berikutnya
`lubang_tengah.py` V2 **560**. BELUM diukur: `taksonomi.py`, `pecahan.py`,
`semesta_kuota.py` V3, `tests/test_semesta_kuota.py`,
`tests/test_lubang_tengah.py`.

**Cacah uji 610** — `tests/test_semesta_kuota.py` 58 butir (32 → 46 → 58);
`test_lubang_tengah` 56 · `test_kebangkitan` 54 · `test_silang_funding` 49 ·
`test_penyebut_tahun` 44 · `test_semesta_silang` 32 · `test_bulan_settled` 26.

## PEKERJAAN BERIKUTNYA, berurutan

1. **Adjudikasi R-268** (610 pada commit `5b968b2a`) lalu praregistrasi R-269 —
   jurnal **102**.
2. **Uji H-A014** — kehidupan keenam bulan saudara SETTLED (CTKUSDTSETTLED
   2025-04, CVCUSDTSETTLED 2025-05, CVXUSDTSETTLED 2025-07, LITUSDTSETTLED
   2025-12, MAVIAUSDTSETTLED 2025-03, SLPUSDTSETTLED 2025-07). Bahan sudah
   di-commit, tanpa unduhan. Praregistrasikan ramalannya lebih dulu; penyebut 6 →
   aturan 59; sertakan kendali positif (50) dan medan `definisi_dapat_dibedakan`
   (46). Ingat: kelima belas nama SETTLED ada di ARSIP dan **0** di penyebut, jadi
   uji ini harus menembus semesta arsip.
3. **Bedakan dua tafsir selisih 12** — apakah ia benar himpunan 12 simbol-bulan
   karantina, dengan memeriksa NAMA dan BULANnya, bukan cacahnya.
4. **Pecah `funding.py` dan `silang_funding.py`** (keduanya **705**, aturan 48).
   Waspadai aturan 49 (nama yang DITAMBAL oleh uji: `monkeypatch`, `patch`, akses
   atribut modul). Perbarui cakupan `sidik_kode` (aturan 22) — dan ingat pelajaran
   KC-29: berkas yang dipakai wajib dicap, termasuk yang berada di paket lain.
5. **`ukur_baris` V6** — perbaiki KC-26 (pemegang ekstrem jadi DAFTAR + `seri`)
   dan tambahkan `taksonomi.py`, `pecahan.py`, `semesta_kuota.py` V3,
   `tests/test_semesta_kuota.py`, `tests/test_lubang_tengah.py`. Satu langkah per
   versi.
6. **Laporan yang BELUM pernah dibaca:** `reports/taksonomi_semesta.json`
   (keluaran `taksonomi.jalankan`: `cacah_per_jenis`, `bulan_per_jenis`,
   `non_ascii`, `cacah_terhenti`, `AKHIR_SEMESTA="2026-06"` — **pembanding
   independen bagi kedua tabel jenis, dan wajib dicocokkan**),
   `reports/semesta_kuota.json` penuh (147 nama), `reports/semesta_silang.json`,
   `reports/penyebut_tahun.json` (18 simbol tanpa HIDUP),
   `reports/bulan_settled.json` (29.820 B), `reports/diagnosa_kc15.json`
   (42.916 B), `reports/kohort_ekor.json` (112.687 B),
   `reports/funding_selisih_penuh.json` (`daftar_terpotong` true, 500 dari 880),
   `tests/test_pulihkan.py`.
7. **Keputusan 7 ADR-A008** dengan DUA cabang (LITUSDT lawan BTCSTUSDT), per
   simbol-bulan, TANPA kata "serentak", wajib menyebut batas `perpetual_usdt` dan
   membedakan peralihan KONTRAK dari kebangkitan PASAR (aturan 66 revisi);
   **ADR-A003** (taksonomi rezim — wajib memakai `lux_ai/semesta/taksonomi.py`,
   bukan membuat taksonomi baru, pelajaran KC-29); terima/tolak **ADR-A007**;
   terapkan ADR-A006; medan `dugaan_pengganti` (ADR-A005); karantina artefak 7
   hari.
8. Aturan 46 di `pulihkan.py` (LUNAS di kode V2, laporan pecahan di git masih
   V1); adjudikasi **R-199** dan R-7, R-19, R-20, R-28, R-36, R-37.
9. **Salin rincian baris R-236..R-247** dari jurnal 92–94 ke papan skor STATE —
   satu-satunya utang papan skor yang tersisa; agregatnya sudah masuk hitungan.
10. Kehidupan **12 simbol-bulan karantina** (tar terpisah,
    `SHA256SUMS_KARANTINA`, `nama_dasar_karantina(i)`); pencocokan 3 lubang
    BNXUSDT dengan 3 simbol-bulan KC-15.
11. Belum diukur: sebab peralihan/kebangkitan kedelapan simbol; sebab KC-15;
    mengapa dua dari enam bulan peralihan jatuh pada 2025-07; apakah **50 kontrak
    bertanggal** pernah masuk perhitungan mana pun; token saham/komoditas di dalam
    787; 16 simbol non-ASCII (币安人生USDT 9, 我踏马来了USDT 6, 龙虾USDT 4 —
    ketiganya `perpetual_usdt`, jadi ADA di penyebut; `tak_tergolong` terukur 0);
    `.decode("utf-8","replace")`; jurang 38 lawan 41; skew `waktu_utc`; selisih
    byte AGIX 531 lawan 529; apakah BUSD/USDC layak digabung dengan USDT (kini
    berangka: 80 nama, 1.705 bulan).
12. Paralel (aturan 3): juri T4 dengan biaya; lapisan validasi (Šidák, ≥300
    permutasi per TANGGAL UTC, PBO dan DSR numpy murni).
    **ADJUDIKASI RISET TETAP TERKUNCI.**

## KEBIASAAN

Ramalan SEBELUM run lalu adjudikasi jujur; hitung ulang tiap angka (21); medan
penggugur (24) — **tetapi hipotesis milik sendiri DILARANG dijadikan penggugur,
sebab laporan yang gugur saat hipotesisnya kalah akan menolak melahirkan angka
yang membantah peramalnya**; kelas cacat pada sampel (37); dilarang menyimpulkan
di luar rentang (20); kendali positif (50); jendela mundur adaptif (51); laporan
tak terbaca utuh = tak ada (52); cacah butir uji diramalkan dari daftar bernomor
(54/56/57 — kini sembilan dari sembilan, karena mekanis, bukan karena cakap);
taksiran cacah baris bias ke BAWAH, jadi lebih baik tidak ditaksir (58); ketiadaan
pengukuran BUKAN ketiadaan gejala (59); ekstrem wajib memikirkan SERI (64); daftar
contoh wajib menyebut cara pemilihannya (65); cacahan semesta wajib menyebut kelas
instrumen (66). Ramalan yang hanya menyalin angka terverifikasi adalah ramalan
MUDAH — katakan begitu, jangan membanggakannya. **BACA berkas sebelum menuduhnya
salah** — pelanggaran terbesar sesi 55 justru di sini. Pisahkan fakta dari asumsi.
Percepat dengan menumpuk beberapa pertanyaan dalam SATU run atomik atas bahan yang
sudah di-commit, dan dorong modul pengukur lebih dulu agar runner bekerja sementara
jurnal dan STATE ditulis. "lanjut" berarti teruskan tanpa konfirmasi. Jangan
berhenti dengan alasan konteks Notion.
