# PROMPT KELANJUTAN — versi 43

Ditulis 30 Juli 2026, sesi 57. Menggantikan v42 (blob
`8b19fd49c1b74b605efde1cba8416a8988eb1749`).

Kamu melanjutkan riset LUX-AI. Operator: **Diva Juan Nur Taqarrub**, GitHub
**EnVyxS**, zona waktu **Asia/Jakarta**, bahasa kerja **Indonesia**. Tenggat:
**2 Agustus 2026**. **Berkas di repo adalah kebenaran; prompt ini hanya peta dan
boleh saja tertinggal.** Bila prompt dan `STATE.md` berselisih, `STATE.md` menang;
bila `STATE.md` dan jurnal berselisih, jurnal menang; bila jurnal dan laporan pada
ref runner berselisih, laporan menang.

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`, dengan `owner`
   dan `repo` **hanya di dalam `toolArguments`**, tidak di tingkat atas.
3. Baca dari `main` repo `EnVyxS/lux-ai-research` berurutan:
   - **`STATE.md` v40** (blob **`86c68a664603c548c39132aaa4d47605f0c84f9b`**,
     commit `c07cb65f`) — memuat aturan 1–76, KC-1..KC-39, papan skor R-1..R-290,
     bagian **"Bulan ABSEN — TERUKUR atas seluruh 787 nama"**, H-A014 bentuk baru,
     H-A015 dua mekanisme, dan utang verifikasi 24 butir. **Bacalah ini lebih dulu,
     bukan prompt ini.** Satu **erratum diketahui**: pada bagian papan skor,
     prosanya menulis "tiga TEPAT" padahal yang baru sejak v39 hanya **dua**
     (R-289, R-290); aritmetikanya benar (202 + 2 = 204). Perbaiki di v41, jangan
     mewarisi kalimatnya.
   - **`journal/2026-07-30-115.md`** (blob
     **`67c21c1776e71681fdefa51c1d214ec4c87ff819`**) — adjudikasi R-288 SEPARUH dan
     R-290 TEPAT, aturan 76, KC-39, dua belas karantina bernama, praregistrasi
     R-291.
   - `journal/2026-07-30-114.md` (blob `e1413bf2…`) dan `-113.md`
     (`342edcb7…`) bila perlu latar bulan ABSEN dan R-286/R-287.
   - `lux_ai/serapan/bulan_absen.py` (blob **`10279d721d66a86b6d265badf81ada3204648f69`**)
     sebelum menyentuh bulan absen atau karantina; `silang_funding.py`
     (`42c3aa9d…`) sebelum menulis modul yang MENGIMPORNYA; `kehidupan_arsip.py`
     (`318a5cb1…`) sebelum menyentuh `bulan_didaftar` atau `peta_parquet`;
     `silang_settled.py` (`3eea2a80…`) sebelum menyentuh serapan SETTLED;
     `lubang_tengah.py` (`4d3beaf1…`) sebelum menyentuh lubang funding.
   - `decisions/ADR-A006.md`, `ADR-A007.md`, `ADR-A008.md` sebelum menyentuh
     karantina/serapan/Keputusan 7; `ADR-A002.md`/`ADR-A004.md` bila menyentuh
     serapan; `PETA_MODUL.md` bila menyentuh modul warisan. **Tak satu pun dari
     berkas ini dibaca pada sesi 56–57** — jangan mengutipnya sebagai terverifikasi
     baru.
4. Baru setelah itu pekerjaan teknis.

## Batasan yang mahal dipelajari ulang

Sandbox agen **tidak punya jaringan**; semua unduhan dan pengukuran arsip
dijalankan GitHub Actions, dan agen hanya boleh percaya artefak yang di-commit.
Tidak ada alat membaca status Actions dan tidak ada alat memicu `workflow_dispatch`;
status hanya diketahui dari berkas laporan yang di-commit workflow itu sendiri, dan
satu-satunya cara menyalakan run adalah **push ke berkas yang tersebut di `paths`
workflow**. Tidak ada API patch — `push_files` menulis ulang **seluruh** isi
berkas; jangan menulis ulang `STATE.md` atau berkas panjang sebelum membacanya
utuh, dan sesudah mendorong berkas panjang **baca ulang dari `main`** (aturan 52).
Cocokkan commit/run_id/`sidik_kode`; jangan percaya keberadaan berkas (aturan 38) —
sesudah push, laporan di `main` sudah memuat commit run BERIKUTNYA. `search_code`
mengembalikan 0 hasil — pakai `get_file_contents`; path berakhiran garis miring
melisting direktori. Runner punya numpy, pandas, pyarrow, pyyaml, pytest; **tidak
ada** scipy dan requests; `data.binance.vision` bisa diakses, `fapi.binance.com`
memberi 451. Dilarang menulis apa pun di luar repo `lux-ai-research`;
`lux-research` boleh **dibaca saja**, hasil dan angkanya tidak pernah boleh masuk.
Push ke `STATE.md`, `PROMPT_KELANJUTAN.md`, `lux_ai/**`, atau `tests/**` menyalakan
`ci.yml` dan menimpa `reports/ci_terakhir.json`; push jurnal, `decisions/**`,
`hipotesis/**`, dan `reports/**` TIDAK menyalakan CI.

**Kopling yang membatasi paralelisme (jawaban sesi 56 atas pertanyaan operator).**
Urutan daftar pekerjaan adalah **prioritas, bukan ketergantungan**; aturan 3
mengizinkan kerja paralel. Empat kopling nyata: (1) `reports/ci_terakhir.json`
adalah berkas TUNGGAL — push yang menyalakan CI wajib **serial**, sebab run kedua
menimpa laporan run pertama; (2) karena itu hanya **satu** ramalan cacah uji boleh
menggantung pada satu waktu; (3) tanpa `workflow_dispatch`, satu push bisa
membangunkan beberapa workflow sekaligus — aman selama nama berkas laporannya
berbeda; (4) medan GABUNGAN (559, 842, 33, 877) tetap terkopling sampai irisan 880
lawan 877 tuntas. Kesimpulan: **paralel pada pekerjaan, serial pada push.**

## Posisi tepat saat serah terima (30 Juli 2026, sesi 57)

Rantai ekor: `0c001ed5` (jurnal 113) → `9e4226ca` (STATE v39) → `57bac8ae`
(PROMPT v42) → `a9ee214d` (jurnal 114) → **`4fc818f0`** (trio `bulan_absen` V1) →
`8b0e0182` (laporan `bulan_absen_ringkas`, run 30477142893) → `9698c36b` (laporan
CI 694, run 30477143164) → **`9b5b4441`** (jurnal 115) → **`c07cb65f`** (STATE v40)
→ `aabd2019` (laporan CI 694, run 30478069419) → commit prompt ini.

- **Papan skor R-1..R-291: TEPAT 205 / MELESET 54 / SEPARUH 18 / TIDAK
  TERADJUDIKASI 7 / MENUNGGU 7 = 291.** MENUNGGU: R-7, R-19, R-20, R-28, R-36,
  R-37, R-199. (STATE v40 masih menulis 290; selisihnya adalah R-292 yang
  diadjudikasi sesudah v40 ditulis. Lihat catatan penomoran di bawah.)
- Aturan sampai **76**, KC sampai **KC-39**, jurnal berikutnya **116**, STATE
  berikutnya **v41**, PROMPT berikutnya **v44**, ADR berikutnya **A009**, ramalan
  berikutnya **R-294**. Menggantung: **R-291** (daftar `parquet_karantina`,
  BERISIKO) dan **R-293** (CI dari push prompt ini, MUDAH).
- **Penomoran ramalan — jangan diulang salahnya.** R-292 dipakai untuk CI yang
  dinyalakan push STATE v40 dan sudah **TEPAT (MUDAH)**: `reports/ci_terakhir.json`
  pada ref `aabd2019`, run **30478069419**, commit `c07cb65f`, **694** butir, kode
  keluar **0**, blob `4bac352c9b0888d900383cd8be4df9445e9567a6`. Nomor R-292 dulu
  sengaja dikosongkan di jurnal 115 §7; ia kini TERPAKAI.
- Cacah uji terverifikasi **694** (638 + 24 `test_silang_settled` + 32
  `test_bulan_absen`). 32 workflow, 38 modul di `lux_ai/serapan/`.

## Pekerjaan pertama — dua ramalan menggantung

- **R-293 (MUDAH, dipraregistrasi di sini).** Push prompt ini menyalakan `ci.yml`
  dan TIDAK menyalakan workflow lain. `reports/ci_terakhir.json` pada ref runner
  akan melaporkan **694** butir dengan `kode_keluar` **0** dan `commit` sama dengan
  commit prompt ini. Tidak ada berkas uji atau modul yang berubah, jadi cacahnya
  wajib tetap 694; bila berubah, itu temuan besar dan wajib dicari sebabnya.
  Adjudikasi lewat `list_commits` `path="reports/ci_terakhir.json"` lalu baca pada
  ref runner (aturan 38).
- **R-291 (BERISIKO, jurnal 115 §7).** Belum bisa diadjudikasi — alat ukurnya
  belum ada. Lihat butir 1 di bawah.

## Pekerjaan berikutnya, urut

1. **Modul kecil pembaca `parquet_karantina` — alat uji R-291.** Baca kedelapan
   manifes lewat `pulihkan.nama_manifes(i)` dan `kehidupan_arsip.peta_parquet`,
   tanpa jaringan, lalu daftarkan simbol-bulan yang ada di tar karantina.
   Bunyi R-291 sudah terkunci di jurnal 115 §7 — **jangan diubah**. Medan penggugur
   wajib dan kendali positif (aturan 24/50). Praregistrasikan cacah uji dari
   **daftar bernomor** `def test_` lebih dulu (aturan 54/56/57), dasarnya **694**.
   Ingat kopling: satu ramalan cacah uji pada satu waktu — tuntaskan R-293 dulu
   atau gabungkan pushnya.
2. **STATE v41** — perbaiki erratum "tiga TEPAT", masukkan R-292 (dan R-293/R-291
   bila sudah teradjudikasi), papan skor **291**.
3. **Anatomi BTCSTUSDT 2022-01** — satu-satunya lubang funding bentuk tengah yang
   tak terjelaskan: `cacah_lilin` **44.640** PENUH, `byte_parquet` 399.757, klines
   2021-03..2026-06 (64 bulan, 1 lubang), status **MATI**, dan kini juga diketahui
   **tanpa bulan absen** (`bulan_absen` V1). Modul baru yang MENGIMPOR, jangan
   memecah; listing direktori paket dan workflow lebih dulu (aturan 66 revisi).
   **Keputusan 7 ADR-A008 DILARANG diambil sebelum ini.**
4. **Pertanyaan murah bernilai tinggi:** mengapa gerbang 1m menolak **tepat** bulan
   peralihan kontrak? Sebelas bulan absen DITERBITKAN arsip
   (`tak_diterbitkan_arsip` = 0) tetapi gagal gerbang — dugaan: bulan itu berlilin
   **sebagian** karena perdagangan berhenti di tengah bulan. Ukur `cacah_baris_1m`
   dan `menit_kalender` untuk kedua belas bulan karantina; preseden BNXUSDT 2022-04
   (41.550 dari 43.200).
5. **H-A014 / H-A015.** H-A014 bentuk baru ("bulan SETTLED = bulan ABSEN dari nama
   dasarnya") **MENANG 9 dari 9**, bentuk lama DICABUT. Ujilah dengan modul lain
   memakai medan `definisi_dapat_dibedakan` (aturan 46) dan kendali positif (50).
   H-A015 kini bermekanisme **dua** — funding pertama (3/3 kohort banyak) dan bulan
   absen (9/9) — tetapi **KC-18 tetap mengikat: yang terbukti PENAMAAN, bukan
   perdagangan**, dan aturan 75 menuntut setiap "cocok" disebut bersama
   mekanismenya.
6. Irisan **880 lawan 877** (utang, bukan angka terverifikasi); pembagian **5 hari**
   KC-15 ke tiga bulan BNXUSDT (2022-06 dan 2022-08 kini diketahui ABSEN dalam
   rentang, 2022-04 di TEPI); tanggal hari yang hilang di BNXUSDT 2022-04 (1.440
   menit); selisih **40 − 38** sampel `diagnosa_kc15`.
7. **`ukur_baris` V6** — pemegang ekstrem jadi DAFTAR + `seri` (KC-26/aturan 64);
   **empat belas** berkas belum terukur, termasuk `bulan_absen.py`,
   `tests/test_bulan_absen.py`, `silang_settled.py`, `tests/test_silang_settled.py`,
   `taksonomi.py`, `terhenti.py` V4, `tests/test_terhenti.py` V4, `pecahan.py`,
   `semesta_kuota.py` V3, `tests/test_semesta_kuota.py`, `ringkas_semesta.py`,
   `survei.py`, `diagnosa_kc15.py`, `tests/test_lubang_tengah.py`.
8. **Laporan belum terbaca** (aturan 52 dan 71 mengikat): `reports/bulan_absen.json`
   penuh (249.992 B), `.github/workflows/bulan_absen.yml` (didorong, belum dibaca
   ulang — utang kecil aturan 52), `semesta_rentang.json` (110.662 B, masih
   `sumber_bersidik` false — aturan 22), `ringkas_semesta.json`,
   `survei_semesta.json`, `survei_progres.json`, `rentang_kc6.json`,
   `semesta_kuota.json` penuh (147 nama), `semesta_silang.json`,
   `penyebut_tahun.json`, `kohort_ekor.json`, `funding_semesta.json`,
   `funding_selisih_penuh.json` (`daftar_terpotong` true, 500 dari 880),
   `hidup_tanpa_funding.json`, `tests/test_pulihkan.py`.
9. **ADR:** Keputusan 7 ADR-A008 **dua cabang bernama** (BTCSTUSDT lubang tunggal &
   MATI lawan LITUSDT rentetan 5 & BANGKIT; R-276 mengikat "tidak ada peralihan
   terbukti"; R-278 mengikat 13/2/0; aturan 74 wajib dipakai); ADR-A003 (wajib
   memuat kebangkitan LITUSDT **dan** bulan ABSEN **dan** aturan 76); terima/tolak
   ADR-A007 — **bahan baru: sebelas bulan absen ADA di arsip, jadi pemulihan akan
   MENGUBAH 19.586, dan itu dilarang tanpa ADR**; terapkan ADR-A006;
   `dugaan_pengganti` (ADR-A005); karantina artefak 7 hari.
10. Aturan 46 di `pulihkan.py`; **bunyi R-28 wajib digali dari riwayat `STATE.md`
    v23** (KC-32: dua sistem penomoran) lalu adjudikasi R-7/19/20/28/36/37 dan
    R-199. Salin rincian R-236..R-247 dari jurnal 92–94 ke papan skor STATE; periksa
    R-224..R-235 sebelum memasukkan ramalan docstring (mis. R-229 TEPAT, R-230
    MELESET).
11. Daftar **147/150** nama hanya-arsip; identitas **18** simbol tanpa bulan HIDUP;
    tiga nama ekor 2026-04; keberadaan `POLUSDT` di 787; asal-usul hantu "16
    non-ASCII"; **kehidupan kedua belas simbol-bulan karantina** (namanya sudah
    diketahui, lilinnya belum diukur). Baca `taksonomi.py` (blob `b418c7ba…`) dan
    ADR-A002/A004/A006/A007 sebelum menjadikan keputusan paralelisasi jadi aturan.
12. Paralel (aturan 3): juri T4 dengan biaya; lapisan validasi (Šidák, ≥300
    permutasi per TANGGAL UTC, PBO & DSR numpy murni). **ADJUDIKASI RISET TETAP
    TERKUNCI.**

## Temuan wajib dibawa

- **Bulan ABSEN kini TERUKUR, bukan lagi dugaan — dan selisih 12 tuntas bernama.**
  Atas seluruh **787** nama penyebut: `jumlah_bulan_absen` **11**,
  `cacah_nama_berabsen` **10**, `jumlah_bulan_absen_luar_pasangan` **0**,
  `cacah_nama_tak_konsisten_rentang` **0**. Kedua belas simbol-bulan karantina
  bernama seluruhnya: AERGO 2025-04, AIA 2026-01, BNX 2022-06, BNX 2022-08, CTK
  2025-04, CVC 2025-05, CVX 2025-07, LIT 2025-12, MAVIA 2025-03, PUMP 2025-07, SLP
  2025-07 (sebelas di dalam rentang) **+ BNXUSDT 2022-04 yang di TEPI rentang**,
  karena itu 11 dan bukan 12. `sebaran_pembeda` = {gagal_gerbang **11**,
  tak_diterbitkan_arsip **0**, tak_terukur **0**} dan `cacah_nama_didaftar` **787**:
  **arsip menerbitkan semuanya; gerbang 1m yang menolaknya.** Kendali positif
  BTCUSDT dan ETHUSDT masing-masing 78 bulan lolos, absen 0.
- **Sembilan dari sembilan** nama berabsen tunggal punya bulan absen yang sama
  persis dengan `bulan_settled_terakhir`-nya — mekanisme **kedua** bagi H-A015,
  lahir dari gerbang klines dan bebas dari arsip funding. KC-18 tetap mengikat.
- **Aturan 76 dan KC-39 [BARU]:** rentang bulan LOLOS dan daftar bulan DIDAFTAR
  arsip adalah **dua penyebut berbeda**; angkanya dilarang dipertukarkan. BNXUSDT:
  rentang lolos 50 (absen **2**) tetapi `bulan_didaftar` 51 (selisih **3**).
  Kekalahan R-288 butir 1 dan 3 seluruhnya lahir dari satu pertukaran itu.
- **Kebangkitan terukur pertama di repo ini:** LITUSDT MATI 2025-02..2025-11,
  funding terakhir 2025-06, lubang funding bentuk TENGAH 2025-07..2025-11 (rentetan
  **5**), `LITUSDTSETTLED` bermuatan **2025-12** tepat di sela, lalu **HIDUP
  2026-01..2026-06** dengan funding kembali (H-A011 MENANG). Klaim "tidak ada satu
  pun kebangkitan terukur" (`cacah_simbol_bangkit_dapat_diuji` = 0 pada
  `kohort_ekor` V4) **DICABUT** — nol itu benar untuk kohort ekor saja (aturan 74,
  KC-37).
- **H-A015 sebagai angka menang, sebagai tafsir dibatasi.** Bulan berfunding
  pertama nama dasar = bulan SETTLED terakhir pada **3 dari 3** pasangan berkohort
  banyak (BNX 2023-02 / 19 lubang, ICP 2022-09 / 16, TLM 2023-03 / 20). Tetapi pada
  **11 dari 15** pasangan bulan SETTLED jatuh jauh SESUDAH funding pertama;
  `sebaran_arah` = {sama 4, lebih_awal 11, lebih_lambat 0, tak_terukur 0}. Bulan
  SETTLED punya DUA peran. **KC-38 dan aturan 75:** kecocokan keempat adalah
  MINAUSDT dan mekanismenya lain lagi — klines pertama = funding pertama = bulan
  SETTLED = 2023-02 dengan `cacah_lubang` 0, cocok semata karena lahir pada bulan
  rombak penamaan.
- **880 lawan 877 bukan angka yang sama:** 880 seluruh lubang funding
  (`BENTUK_TERBITAN_FUNDING` {awal 48, ekor 826, tengah 6}); 877 yang jatuh di dalam
  penyebut 19.586 ({awal 45, ekor 826, tengah 6, seluruh 0}); selisih 3 = tiga bulan
  BNXUSDT di luar penyebut. 48 + 826 + 6 = 880 dan 45 + 826 + 6 = 877 — kedua bentuk
  konsisten (silang-periksa sesi 56). **Irisannya tetap UTANG.** Keenam lubang tengah
  dimiliki hanya DUA simbol: LITUSDT 5 dan BTCSTUSDT 1, keenamnya MATI. Ke-33 lubang
  pada simbol-bulan HIDUP milik BNX/ICP/JUP/QTUM/TLM dan SEMUANYA berbentuk awal.
- **Koreksi KC-15:** 7.200 menit BNXUSDT (2022-04/-06/-08) **UTUH di arsip HARIAN**;
  hanya **210 menit tepi** 2022-04 tak terjelaskan, konsisten dengan peluncuran
  03:30 UTC. Jurnal 109 §5.2 DICABUT.
- **"Dua bersambung" DICABUT:** hanya `ICPUSDT_SETTLED` (2022-01..2022-09) yang
  bersambung; TLM dan BNX bercelah dengan jurang sama 2022-09..2023-01. **DUA BELAS**
  nama SETTLED bersatu-bulan (bukan 11 — kekalahan R-281).
- **R-246 SEPARUH:** `TLMUSDTSETTLED` tanpa garis bawah; docstring
  `penyebut_tahun.py` masih salah — jangan disunting, cukup jangan diwarisi. Angka
  warisan "16 simbol non-ASCII" DICABUT → **3 nama / 19 bulan** (币安人生USDT 9,
  我踏马来了USDT 6, 龙虾USDT 4).

## Angka terverifikasi

Penyebut **787** simbol USDT = `perpetual_usdt`, PERSIS, kini terbukti **tiga arah**
(taksonomi, kehidupan, `cacah_nama_didaftar` `bulan_absen`); arsip **937**; **150**
hanya-arsip; **21.789** bulan arsip; 15 nama SETTLED di arsip, 0 di penyebut;
**19.598** simbol-bulan, lolos **19.586**, gagal **12** (karantina bernama
seluruhnya, tar terpisah); MATI **1.401** / SEPI **98** / HIDUP **18.087**;
**839.842.134** baris; funding **880** lubang (877 di dalam penyebut); **33** HIDUP
tanpa funding; `cacah_simbol_tanpa_hidup` **18**; penyebut per tahun
504/1.385/1.729/2.400/3.570/5.948/4.050 dengan `bagian_mati`
0,001984/0,006498/0,019665/0,042917/0,053782/0,085071/**0,137284**; dari 1.401 MATI
**842** kehilangan funding dan **559** tetap berfunding; taksonomi 9 kelas
{basis_non_fiat 1, futures_kedaluwarsa 50, indeks 3, perpetual_busd 41,
perpetual_usd1 1, perpetual_usdc 39, perpetual_usdt 787, sisa_settled 15,
tak_tergolong 0}; ekor 2026-06 = **808** hidup / **129** terhenti, **49** hidup di
luar penyebut, **28** `perpetual_usdt` terhenti; R-278 **13/2/0**; BTCSTUSDT 2022-01
`cacah_lilin` **44.640**, `byte_parquet` 399.757, 64 bulan, MATI, tanpa bulan absen;
BNXUSDT 2022-04 `gerbang_lolos` false, `cacah_baris_1m` **41.550**, `menit_kalender`
43.200; riwayat CI 630 → 630 → 638 → 662 → 662 → 662 → **694**; aturan 57 **enam
belas dari enam belas**.

**15 pasangan SETTLED** (bulan SETTLED terakhir · cacah bulan SETTLED · lubang
funding nama dasar · rentang/lolos/absen): AERGO 2025-04 ·1·0· 22/21/1 · AIA 2026-01
·1·0· 10/9/1 · BDXN 2026-04 ·1·0· 10/10/0 · **BNX 2023-02 ·6·19· 50/48/2** · CTK
2025-04 ·1·0· 68/67/1 · CVC 2025-05 ·1·0· 68/67/1 · CVX 2025-07 ·1·0· 46/45/1 ·
**ICP_SETTLED 2022-09 ·9·16· 62/62/0** · LIT 2025-12 ·1·**5**· 65/64/1 · MAVIA
2025-03 ·1·0· 29/28/1 · MINA 2023-02 ·1·0· 41/41/0 · PUMP 2025-07 ·1·0· 15/14/1 ·
SLP 2025-07 ·1·0· 33/32/1 · SXP 2026-06 ·1·**5**· 71/71/0 · **TLM 2023-03 ·9·20·
60/60/0**. Jumlah bulan SETTLED **36**; jumlah absen **11**. Nama dasar terhenti
hanya dua: SXPUSDT 2026-05, BDXNUSDT 2026-03. Rombak penamaan 2023-02 (BNX/MINA/TLM)
dan 2025-07 (CVX/SLP/PUMP).

## Kebiasaan

Ramalan **sebelum** run lalu adjudikasi jujur; hitung ulang tiap angka (21); medan
penggugur (24); kelas cacat pada sampel (37); dilarang menyimpulkan di luar rentang
(20); ramalan menyebut penyebut (44); kendali positif (50); jendela mundur adaptif
(51); laporan tak terbaca utuh = tidak ada (52); cacah butir uji dari daftar
bernomor (54/56/57); taksiran baris bias ke bawah (58); ketiadaan pengukuran
**bukan** ketiadaan gejala (59); listing direktori paket dan workflow sebelum
menulis modul baru (66 revisi); nama turunan wajib disebut bersama asalnya dan
wajib punya pemeriksaan silang (69); jumlahkan silang butir ramalan sendiri (70);
baca modul penghasil sebelum meramalkan laporannya (71); sebut penyebut sampel
sebelum putusan (72); jangan meramal isi berkas dari NAMA-nya (73); setiap nol
disebut bersama penyebutnya (74); setiap "cocok" disebut bersama mekanismenya (75);
**rentang lolos dan daftar didaftar adalah dua penyebut, jangan dipertukarkan
(76)**.

Ramalan yang hanya menyalin angka terverifikasi adalah **MUDAH** — katakan begitu.
**Baca berkas sebelum menuduhnya salah.** Pisahkan fakta dari asumsi. Tumpuk
pertanyaan dalam satu run atomik; dorong modul pengukur lebih dulu. "lanjut"
berarti teruskan tanpa konfirmasi. Jangan berhenti dengan alasan konteks Notion.

**Catatan kejujuran yang wajib diwarisi.** Sejak STATE v39 ada empat adjudikasi:
R-289 TEPAT (MUDAH), R-290 TEPAT (MUDAH), R-292 TEPAT (MUDAH), dan R-288 SEPARUH.
Satu-satunya cabang **BERISIKO** yang benar-benar menang atas data adalah R-288
butir 2 (9 dari 9) — dan justru dua butir yang disebut MUDAH di ramalan yang sama
yang kalah, karena saya menyalah-salin tabel jurnal saya sendiri. Itu kelas cacat
**keempat** sesudah R-281 (aritmetika sendiri), R-282 (nama laporan), dan R-284
(nama modul); keempatnya dapat dicegah **tanpa jaringan dan tanpa satu pun run**.
Aturan 57 enam belas dari enam belas bukan prestasi meramal — mekanismenya
deterministik. **Yang layak dibanggakan bukan papan skor, melainkan bahwa setiap
kekalahan melahirkan aturan yang menutup lubangnya: R-288 melahirkan aturan 76 dan
KC-39.**
