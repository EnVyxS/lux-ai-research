# PROMPT KELANJUTAN — versi 42

Ditulis 30 Juli 2026, sesi 56. Menggantikan v41 (blob
`b21811c801637b642107c481aa857c85e9510ce9`).

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
   - **`STATE.md` v39** (blob **`f8078dd20f0b3fc1bf738f0befdb97cb934f4f16`**) —
     kini **TIDAK tertinggal**: memuat aturan 1–75, KC-1..KC-38, papan skor
     R-1..R-287, H-A015, kebangkitan LITUSDT, 880 lawan 877, bulan ABSEN, dan
     kedua ramalan yang masih menggantung. **Bacalah ini lebih dulu, bukan prompt
     ini.**
   - **`journal/2026-07-30-113.md`** (blob
     **`342edcb7e2906d24c1ebbb9fab4c9735f18335a4`**) — adjudikasi R-286/R-287,
     KC-38, aturan 75, dan tabel bulan ABSEN beserta tiga kehati-hatiannya.
   - `journal/2026-07-29-112.md` (blob `a31e7a66…`), `-111.md` (`7521d1af…`),
     `-110.md` (`0784c727…`) bila perlu latar temuan.
   - `lux_ai/serapan/silang_settled.py` (blob `3eea2a80…`) sebelum menyentuh
     serapan SETTLED; `lux_ai/serapan/lubang_tengah.py` (blob `4d3beaf1…`) sebelum
     menyentuh lubang funding; `lux_ai/serapan/silang_funding.py` sebelum menulis
     modul yang MENGIMPORNYA.
   - `decisions/ADR-A006.md`, `ADR-A007.md`, `ADR-A008.md` sebelum menyentuh
     karantina/serapan/Keputusan 7; `ADR-A002.md`/`ADR-A004.md` bila menyentuh
     serapan; `PETA_MODUL.md` bila menyentuh modul warisan.
4. Baru setelah itu pekerjaan teknis.

## Batasan yang mahal dipelajari ulang

Sandbox agen **tidak punya jaringan**; semua unduhan dan pengukuran arsip
dijalankan GitHub Actions, dan agen hanya boleh percaya artefak yang di-commit.
Tidak ada alat membaca status Actions dan tidak ada alat memicu `workflow_dispatch`;
status hanya diketahui dari berkas laporan yang di-commit workflow itu sendiri, dan
satu-satunya cara menyalakan run adalah **push ke berkas yang tersebut di `paths`
workflow**. Tidak ada API patch — `push_files` menulis ulang **seluruh** isi
berkas; jangan menulis ulang `STATE.md` atau berkas panjang sebelum membacanya
utuh, dan sesudah mendorong berkas panjang **baca ulang dari `main`** untuk
memastikan ekornya hadir (aturan 52). Cocokkan commit/run_id/`sidik_kode`; jangan
percaya keberadaan berkas (aturan 38) — sesudah push, laporan di `main` sudah
memuat commit run BERIKUTNYA. `search_code` mengembalikan 0 hasil — pakai
`get_file_contents`; path berakhiran garis miring melisting direktori. Runner punya
numpy, pandas, pyarrow, pyyaml, pytest; **tidak ada** scipy dan requests;
`data.binance.vision` bisa diakses, `fapi.binance.com` memberi 451. Dilarang
menulis apa pun di luar repo `lux-ai-research`; `lux-research` boleh **dibaca
saja**, hasil dan angkanya tidak pernah boleh masuk. Push ke `STATE.md`,
`PROMPT_KELANJUTAN.md`, `lux_ai/**`, atau `tests/**` menyalakan `ci.yml` dan
menimpa `reports/ci_terakhir.json`; push jurnal, `decisions/**`, `hipotesis/**`,
dan `reports/**` TIDAK menyalakan CI.

## Posisi tepat saat serah terima (30 Juli 2026, sesi 56)

Rantai ekor: `de46eebb` (jurnal 112) → `3d113d49` (trio `silang_settled` V1) →
`32088010` (laporan CI 662, run 30469781181) → **`0c001ed5`** (jurnal 113) →
**`9e4226ca`** (STATE v39) → commit prompt ini.

- **Papan skor R-1..R-287: TEPAT 202 / MELESET 54 / SEPARUH 17 / TIDAK
  TERADJUDIKASI 7 / MENUNGGU 7 = 287.** MENUNGGU: R-7, R-19, R-20, R-28, R-36,
  R-37, R-199.
- Aturan sampai **75**, KC sampai **KC-38**, jurnal berikutnya **114**, STATE
  berikutnya **v40**, PROMPT berikutnya **v43**, ADR berikutnya **A009**, ramalan
  berikutnya **R-290** (R-288 dan R-289 sudah terpraregistrasi dan **belum
  diadjudikasi**).
- Cacah uji terverifikasi **662** (kode 0, commit `3d113d49`, run 30469781181).

## Pekerjaan pertama — adjudikasi dua ramalan menggantung

Push STATE v39 (`9e4226ca`) dan push prompt ini masing-masing menyalakan `ci.yml`.
Lakukan `list_commits` dengan `path="reports/ci_terakhir.json"` lalu baca laporan
**pada ref runner** (aturan 38):

- **R-289** (jurnal 113 §9, **MUDAH**): pada commit yang menyentuh `STATE.md` dan
  pada commit yang menyentuh `PROMPT_KELANJUTAN.md`, `ci.yml` MENYALA sementara
  `terhenti_semesta.yml`, `semesta_kuota.yml`, `ukur_baris.yml`, dan workflow
  `silang_settled` TIDAK; `reports/ci_terakhir.json` melaporkan **662** butir dengan
  `kode_keluar` **0**. Tidak ada berkas uji atau modul yang berubah, jadi cacahnya
  wajib tetap 662; bila berubah, itu temuan besar dan wajib dicari sebabnya.
- **R-288** (jurnal 113 §8) **belum bisa diadjudikasi** — alat ukurnya belum ada.
  Ia menuntut modul baru; lihat butir 1 di bawah.

## Pekerjaan berikutnya, urut

1. **Modul bulan ABSEN — alat uji R-288, dan pekerjaan paling murah bernilai
   tinggi.** Modul baru di `lux_ai/serapan/` yang **MENGIMPOR** `silang_funding`
   (preseden jurnal 111 §5: impor, jangan pecah, jangan salin) lalu, untuk SETIAP
   dari **787** nama penyebut, menghitung `rentang = bulan_terakhir −
   bulan_pertama + 1`, `cacah_bulan_lolos`, dan **daftar bulan yang absen di dalam
   rentang**; ditambah medan yang membedakan "absen karena tak diterbitkan arsip"
   dari "absen karena gagal gerbang" (bandingkan dengan `bulan_didaftar`
   `kehidupan_arsip`). Medan penggugur wajib: `selisih_penyebut` 0 terhadap 19.586,
   `jumlah_bulan_absen` (ramalan: **12**), kendali positif BTCUSDT (absen 0).
   Ramalan R-288 sudah terkunci — **jangan diubah**: (1) sembilan nama berabsen
   satu, persis AERGO/AIA/CTK/CVC/CVX/LIT/MAVIA/PUMP/SLP, BNXUSDT 3, lima sisanya
   0 (MUDAH); (2) **≥7 dari 9** bulan absen = `bulan_settled_terakhir` (BERISIKO);
   (3) jumlah atas SELURUH 787 = 12 (BERISIKO BESAR). GUGUR bila butir 2 salah.
   Ramalan cacah uji sesudah berkas uji baru wajib dipraregistrasi lebih dulu dari
   **daftar bernomor** `def test_` (aturan 54/56/57), dan dasarnya 662.
2. **Anatomi BTCSTUSDT 2022-01** — satu-satunya lubang funding bentuk tengah yang
   benar-benar tak terjelaskan: `cacah_lilin` **44.640** PENUH, `byte_parquet`
   399.757, klines 2021-03..2026-06 (64 bulan, 1 lubang), status **MATI**. Modul
   baru yang MENGIMPOR, jangan memecah; listing direktori paket dan workflow lebih
   dulu (aturan 66 revisi). **Keputusan 7 ADR-A008 DILARANG diambil sebelum ini.**
3. **H-A014 — wajib ditulis ulang dalam DUA bentuk berdampingan.** Bentuk lama:
   bulan SETTLED adalah bulan MATI di tengah hidup nama dasarnya (13 kasus).
   Bentuk baru yang kini lebih mungkin: bulan SETTLED adalah bulan yang **ABSEN**
   dari nama dasarnya (9 kasus). Butuh aturan 59, kendali positif (50), dan medan
   `definisi_dapat_dibedakan` (46). Butir 1 di atas sekaligus menjadi separuh
   alat ujinya.
4. Irisan **880 lawan 877** (utang, bukan angka terverifikasi); pembagian **5 hari**
   KC-15 ke tiga bulan BNXUSDT; tanggal hari yang hilang di BNXUSDT 2022-04
   (1.440 menit); selisih **40 − 38** sampel `diagnosa_kc15`.
5. **`ukur_baris` V6** — pemegang ekstrem jadi DAFTAR + `seri` (KC-26/aturan 64);
   tambahkan `silang_settled.py`, `tests/test_silang_settled.py`, `taksonomi.py`,
   `terhenti.py` V4, `tests/test_terhenti.py` V4, `pecahan.py`, `semesta_kuota.py`
   V3, `tests/test_semesta_kuota.py`, `ringkas_semesta.py`, `survei.py`,
   `diagnosa_kc15.py`, `tests/test_lubang_tengah.py`.
6. **Laporan belum terbaca:** `semesta_rentang.json` (110.662 B, masih
   `sumber_bersidik` false — aturan 22), `ringkas_semesta.json`,
   `survei_semesta.json`, `survei_progres.json`, `rentang_kc6.json`,
   `semesta_kuota.json` penuh (147 nama), `semesta_silang.json`,
   `penyebut_tahun.json`, `kohort_ekor.json`, `funding_semesta.json`,
   `funding_selisih_penuh.json` (`daftar_terpotong` true, 500 dari 880),
   `hidup_tanpa_funding.json`, `tests/test_pulihkan.py`. **Aturan 71 mengikat:**
   baca modul penghasilnya lebih dulu bila hendak meramalkan isinya.
7. **ADR:** Keputusan 7 ADR-A008 **dua cabang bernama** (BTCSTUSDT lubang tunggal
   & MATI lawan LITUSDT rentetan 5 & BANGKIT; R-276 mengikat "tidak ada peralihan
   terbukti"; R-278 mengikat 13/2/0; aturan 74 wajib dipakai); ADR-A003 (wajib
   memuat kebangkitan LITUSDT sebagai kasus terukur pertama); terima/tolak
   ADR-A007; terapkan ADR-A006; `dugaan_pengganti` (ADR-A005); karantina 7 hari.
8. Aturan 46 di `pulihkan.py`; **bunyi R-28 wajib digali dari riwayat `STATE.md`
   v23** (KC-32: dua sistem penomoran) lalu adjudikasi R-7/19/20/28/36/37 dan
   R-199.
9. Kehidupan **12** simbol-bulan karantina; bedakan dua tafsir selisih 12 lewat
   NAMA dan BULAN (butir 1 di atas menjawabnya sebagian). Salin rincian
   R-236..R-247 dari jurnal 92–94 ke papan skor STATE. Periksa R-224..R-235 sebelum
   memasukkan ramalan docstring (mis. R-229 TEPAT, R-230 MELESET) ke papan skor.
10. Paralel (aturan 3): juri T4 dengan biaya; lapisan validasi (Šidák, ≥300
    permutasi per TANGGAL UTC, PBO & DSR numpy murni). **ADJUDIKASI RISET TETAP
    TERKUNCI.**

## Temuan wajib dibawa

- **Kebangkitan terukur pertama di repo ini:** LITUSDT MATI 2025-02..2025-11,
  funding terakhir 2025-06, lubang funding bentuk TENGAH 2025-07..2025-11 (rentetan
  **5**), `LITUSDTSETTLED` bermuatan **2025-12** tepat di sela, lalu **HIDUP
  2026-01..2026-06** dengan funding kembali (H-A011 MENANG, `h_a011_cacah_hidup` 6).
  Klaim "tidak ada satu pun kebangkitan terukur"
  (`cacah_simbol_bangkit_dapat_diuji` = 0 pada `kohort_ekor` V4) **DICABUT** — nol
  itu benar untuk kohort ekor saja (aturan 74, KC-37).
- **H-A015 MENANG sebagai angka, DIBATASI sebagai tafsir.** Bulan berfunding
  pertama nama dasar = bulan SETTLED terakhir pada **3 dari 3** pasangan berkohort
  banyak (BNXUSDT 2023-02 / 19 lubang, ICPUSDT 2022-09 / 16, TLMUSDT 2023-03 / 20)
  — maka bulan klines tanpa funding itu bukan data hilang, fundingnya **milik
  kontrak lain**. Tetapi pada **11 dari 15** pasangan bulan SETTLED jatuh **jauh
  SESUDAH** funding pertama: bulan SETTLED punya DUA peran (batas awal kontrak
  berikutnya lawan bulan penutupan kontrak berjalan). `sebaran_arah` = {sama 4,
  lebih_awal 11, lebih_lambat 0, tak_terukur 0}. **KC-18 mengikat: yang terbukti
  adalah PENAMAAN, bukan perdagangan.**
- **KC-38 dan aturan 75 [BARU]:** kecocokan keempat R-286 adalah **MINAUSDT**, dan
  mekanismenya lain — klines pertama = funding pertama = bulan SETTLED = 2023-02
  dengan `cacah_lubang` **0**; ia cocok semata karena lahir pada bulan rombak
  penamaan. Cacah "cocok" DILARANG dipakai memperkuat hipotesis sebelum mekanismenya
  dipisah.
- **Bulan ABSEN — selisih 12 punya calon identitas bernama.** Sembilan nama
  berpasangan SETTLED kehilangan **tepat satu** bulan dari rentangnya (AERGO, AIA,
  CTK, CVC, CVX, LIT, MAVIA, PUMP, SLP) dan BNXUSDT kehilangan **3** (atas rentang
  arsip 51); 9 + 3 = **12** = 19.598 − 19.586, dengan KC-14 mencacah 9 dan KC-15
  mencacah 3. **Tiga kehati-hatian:** absen bisa berarti tak diterbitkan ATAU gagal
  gerbang; 772 nama lain belum diperiksa; bulan MANA yang absen belum diukur.
  Jangan menulisnya sebagai terverifikasi — ia ramalan R-288.
- **880 lawan 877 bukan angka yang sama:** 880 seluruh lubang funding; 877 yang
  jatuh di dalam penyebut 19.586, bentuk {awal 45, ekor 826, tengah 6, seluruh 0};
  selisih 3 = tiga bulan BNXUSDT di luar penyebut. **Irisannya UTANG.** Keenam
  lubang tengah dimiliki hanya DUA simbol: LITUSDT 5 dan BTCSTUSDT 1, keenamnya
  MATI. Ke-33 lubang pada simbol-bulan HIDUP milik BNX/ICP/JUP/QTUM/TLM dan
  SEMUANYA berbentuk awal.
- **Koreksi KC-15:** 7.200 menit BNXUSDT (2022-04/-06/-08) **UTUH di arsip
  HARIAN**; hanya **210 menit tepi** 2022-04 tak terjelaskan, dan itu konsisten
  dengan peluncuran 03:30 UTC. Jurnal 109 §5.2 DICABUT.
- **"Dua bersambung" DICABUT:** hanya `ICPUSDT_SETTLED` (2022-01..2022-09) yang
  bersambung; TLM dan BNX bercelah, dengan jurang yang sama 2022-09..2023-01.
  **DUA BELAS** nama SETTLED bersatu-bulan (bukan 11 — kekalahan R-281).
- **R-246 SEPARUH:** `TLMUSDTSETTLED` tanpa garis bawah; docstring
  `penyebut_tahun.py` masih salah — jangan disunting, cukup jangan diwarisi. Angka
  warisan "16 simbol non-ASCII" DICABUT → **3 nama / 19 bulan** (kini terukur tiga
  kali dari tiga pengukuran berbeda).
- **`bulan_didaftar` ≠ bulan lolos gerbang.** `bulan_didaftar` BNXUSDT penuh 51
  bulan tanpa lubang, tetapi 3 bulannya gagal gerbang. Perbedaan ini yang membuat
  butir 1 di atas menuntut medan pembeda.

## Angka terverifikasi

Penyebut **787** simbol USDT = `perpetual_usdt`, PERSIS (kedua arah nol; arsip
**937**; **150** hanya-arsip; 21.789 bulan arsip); 15 nama SETTLED di arsip, 0 di
penyebut; **19.598** simbol-bulan, lolos **19.586**, gagal **12** (karantina, tar
terpisah); MATI **1.401** / SEPI **98** / HIDUP **18.087**; **839.842.134** baris;
funding **880** lubang (877 di dalam penyebut); **33** HIDUP tanpa funding;
`cacah_simbol_tanpa_hidup` **18**; penyebut per tahun
504/1.385/1.729/2.400/3.570/5.948/4.050 dengan `bagian_mati`
0,001984/0,006498/0,019665/0,042917/0,053782/0,085071/**0,137284**; dari 1.401 MATI
**842** kehilangan funding dan **559** tetap berfunding; taksonomi 9 kelas
{basis_non_fiat 1, futures_kedaluwarsa 50, indeks 3, perpetual_busd 41,
perpetual_usd1 1, perpetual_usdc 39, perpetual_usdt 787, sisa_settled 15,
tak_tergolong 0}; ekor 2026-06 = **808** hidup / **129** terhenti, **49** hidup di
luar penyebut, **28** `perpetual_usdt` terhenti; R-278 **13/2/0**; **CI 662** butir
(sebelumnya 638, 630).

**15 pasangan SETTLED** (bulan SETTLED terakhir · cacah bulan SETTLED · lubang
funding nama dasar): AERGO 2025-04 ·1·0 · AIA 2026-01 ·1·0 · BDXN 2026-04 ·1·0 ·
**BNX 2023-02 ·6·19** · CTK 2025-04 ·1·0 · CVC 2025-05 ·1·0 · CVX 2025-07 ·1·0 ·
**ICP_SETTLED 2022-09 ·9·16** · LIT 2025-12 ·1·**5** · MAVIA 2025-03 ·1·0 · MINA
2023-02 ·1·0 · PUMP 2025-07 ·1·0 · SLP 2025-07 ·1·0 · SXP 2026-06 ·1·**5** · **TLM
2023-03 ·9·20**. Jumlah bulan SETTLED **36** (dua pengukuran berkode berbeda
sepakat). Nama dasar terhenti hanya dua: SXPUSDT 2026-05, BDXNUSDT 2026-03. Rombak
penamaan 2023-02 (BNX/MINA/TLM) dan 2025-07 (CVX/SLP/PUMP).

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
disebut bersama penyebutnya (74); setiap "cocok" disebut bersama mekanismenya (75).

Ramalan yang hanya menyalin angka terverifikasi adalah **MUDAH** — katakan begitu.
**Baca berkas sebelum menuduhnya salah.** Pisahkan fakta dari asumsi. Tumpuk
pertanyaan dalam satu run atomik; dorong modul pengukur lebih dulu. "lanjut"
berarti teruskan tanpa konfirmasi. Jangan berhenti dengan alasan konteks Notion.

**Catatan kejujuran yang wajib diwarisi.** Dari sepuluh ramalan sejak STATE v38,
empat kalah (R-281 aritmetika sendiri, R-282 nama laporan, R-284 nama modul, R-285
butir 3) dan **hanya R-285 butir 3 yang benar-benar dikalahkan DATA**; tiga lainnya
dapat dicegah tanpa jaringan dan tanpa satu pun run. Dari enam yang menang, **empat
MUDAH** (R-279, R-280, R-287, dan R-283 yang lolos lewat disjungsi); hanya R-278 dan
R-286 berisiko, dan R-286 pun menang di butir 1 dengan bantuan kasus bermekanisme
lain. Aturan 57 tiga belas dari tiga belas bukan prestasi meramal — mekanismenya
deterministik. **Yang layak dibanggakan bukan papan skor, melainkan bahwa setiap
kekalahan melahirkan aturan yang menutup lubangnya.**
