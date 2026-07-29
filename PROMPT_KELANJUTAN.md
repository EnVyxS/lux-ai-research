# PROMPT KELANJUTAN — versi 39

Ditulis 29 Juli 2026, 20:05 WIB (sesi 55). Menggantikan v38 (blob `545b66de`).
Berkas di repo adalah kebenaran; prompt ini hanya peta dan boleh saja tertinggal.

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
   - **`STATE.md` v36 — PALING PENTING dan kini MUTAKHIR.** Ia sudah memuat
     aturan 1–64, KC-1..KC-26, papan skor R-1..R-255, H-A013 MENANG, tabel
     penyebut per tahun, angka semesta arsip, dan tabel `ukur_baris` V5. Baca
     UTUH sebelum menulis ulang sebaris pun.
   - `journal/2026-07-29-95.md` (adjudikasi R-248/R-250/R-251/R-252 dan
     praregistrasi R-253..R-255), lalu `journal/2026-07-29-96.md` bila sudah ada;
   - `journal/2026-07-29-94.md` (blob `fc6fd2e6`) — **wajib**, untuk memeriksa
     teks **R-249** yang masih MENUNGGU atas dasar penalaran, belum atas bacaan;
   - `journal/2026-07-29-92.md` dan `-93.md` bila perlu rincian R-236..R-247
     yang belum disalin ke papan skor STATE;
   - `lux_ai/serapan/ukur_baris.py` V5 bila menyentuh pengukuran baris;
     `lux_ai/serapan/bulan_settled.py` V1 bila menyentuh H-A013/H-A014;
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
percaya keberadaan berkas (aturan 38). `search_code` mengembalikan 0 hasil — pakai
`get_file_contents`; path berakhiran garis miring melisting direktori, dan listing
`reports/` TERPOTONG — pakai path berkas langsung, atau `minimal_output: true`
untuk listing panjang seperti `tests/` dan `lux_ai/serapan/`. Runner punya numpy,
pandas, pyarrow, pyyaml, pytest; TIDAK ada scipy dan requests;
`data.binance.vision` bisa diakses, `fapi.binance.com` memberi 451. Dilarang
menulis apa pun di luar repo `lux-ai-research`; `lux-research` boleh DIBACA saja,
hasil dan angkanya tidak pernah boleh masuk.

## POSISI (29 Juli 2026, 20:05 WIB)

HEAD saat prompt ini ditulis: **`9d6ce31077b1be674c6c9ad242f78cff66d70009`**
(STATE v36); commit berikutnya adalah commit yang memuat berkas ini.

Rantai sesi 55: `9bdab113` (trio `bulan_settled` V1) → **`404e6f1b`**
(`ukur_baris` V5) → **`d3b836ed`** (jurnal 95) → **`9d6ce310`** (STATE v36) →
PROMPT v39.

Run TERVERIFIKASI sesi 55 (commit dicocokkan, aturan 38):

| run | commit | isi | kode |
|---|---|---|---:|
| 30448334675 | `9bdab113` | CI **552** butir | 0 |
| 30448334739 | `9bdab113` | `bulan_settled` V1 | 0 |
| 30451749412 | `404e6f1b` | `ukur_baris` V5 (21 berkas) | 0 |
| 30451749571 | `404e6f1b` | CI **552** butir | 0 |

Riwayat CI: … 450 → 494 → 526 → **552**.

Papan skor R-1..R-255: TEPAT **180** / MELESET **44** / SEPARUH **16** / TIDAK
TERADJUDIKASI **7** / MENUNGGU **8** = **255** (180+44+16+7+8 = 255).
MENUNGGU: R-7, R-19, R-20, R-28, R-36, R-37, R-199, **R-249**.
R-256 SUDAH dipraregistrasi di STATE v36; ramalan berikutnya **R-257**.
Aturan sampai **64**. Kelas cacat sampai **KC-26**. Jurnal berikutnya **96**.
STATE berikutnya **v37**. PROMPT berikutnya **v40**. ADR berikutnya **A009**.

## PEKERJAAN PERTAMA DI SESI BARU — adjudikasi yang MENGGANTUNG

- **R-256** (praregistrasi di STATE v36): pada commit **`9d6ce310`** — commit yang
  menyentuh `STATE.md` — `ci.yml` MENYALA dan `reports/ci_terakhir.json` akan
  melaporkan **552 butir**, `kode_keluar` **0**. Ini ramalan **MUDAH** dan sudah
  disebut begitu di muka. **Peringatan:** push PROMPT v39 juga menyalakan `ci.yml`,
  sehingga laporan `9d6ce310` mungkin TERTIMPA. Bila medan `commit` di
  `reports/ci_terakhir.json` bukan `9d6ce310`, cari commit runner lewat
  `list_commits` dengan `path="reports/ci_terakhir.json"` (penulis lux-ci, nomor
  run ada di pesan commit) lalu baca pada ref itu (aturan 38).
- **R-257** wajib dipraregistrasi SEBELUM run berikutnya, bukan sesudahnya.

## ADJUDIKASI SESI 55 — sudah selesai, jangan diulang

- **R-248 TEPAT** — H-A013 MENANG **6 dari 6** (ambang 4), `menang` true,
  `terukur` true, `definisi_dapat_dibedakan` **false**, `sebab_terpakai` hanya
  `["saudara_settled_memuat_bulan"]`. Enam pasangan: CTK 2025-04 · CVC 2025-05 ·
  CVX 2025-07 · LIT 2025-12 · MAVIA 2025-03 · SLP 2025-07.
- **R-250 TEPAT** (552, ramalan MUDAH) · **R-251 TEPAT** (`cacah_cocok_cacah`
  24/24, `cacah_tak_ada_di_laporan_lama` 0) · **R-252 TEPAT** (kendali BTCUSDT
  **78** ≥ 60, `kendali_sah` true).
- **R-253 TEPAT** (CI 552, kode 0, `404e6f1b`; ramalan MUDAH) · **R-254 TEPAT**
  (`cacah_berkas_hilang` 0, `cacah_berkas_melebihi_pagar` 0, 21 dari 21) ·
  **R-255 SEPARUH** — terbesar **705 SERI** antara `funding.py` dan
  `silang_funding.py`; medan `berkas_terpanjang` menamai `funding.py` semata
  karena urutan daftar. Dari situ lahir **aturan 64** dan **KC-26**.

## TEMUAN MUTAKHIR YANG WAJIB DIBAWA

- **Tafsir kebangkitan DILEMAHKAN:** bukan "delapan kebangkitan", melainkan **dua
  bersambung** (ICPUSDT 2022-09, TLMUSDT 2023-03) dan **enam peralihan nama**.
  Kecocokan bulan membuktikan **PENAMAAN kontrak**, bukan perdagangan (KC-18).
- **H-A014 LAHIR, BELUM DIUJI:** keenam peralihan itu pergantian KONTRAK, bukan
  pergantian kehidupan pasar. Uji termurah yang tersisa: ukur kehidupan keenam
  bulan saudara SETTLED dari arsip yang sudah di-commit. Penyebut 6 — kecil, jadi
  aturan 59 wajib ditaati.
- **DUA konvensi nama SETTLED hidup berdampingan:** `ICPUSDT_SETTLED` bergaris
  bawah; `TLMUSDTSETTLED` dan keenam saudara peralihan TANPA garis bawah. R-246
  SEPARUH karena itu. Docstring `penyebut_tahun.py` masih menulis bentuk salah —
  jangan disunting, cukup jangan diwarisi.
- **Aturan 63 dan KC-25:** penyebut **787** simbol adalah pasangan berkuota **USDT
  SAJA**; arsip **937** simbol dan **21.789** bulan; **150** hanya-arsip (hampir
  seluruhnya BUSD/USDC), **0** hanya-penyebut. Setiap klaim kematian,
  kebangkitan, lubang funding, dan `bagian_mati` wajib menyebut batas itu.
- **Aturan 62 dan KC-24:** dua semesta dilarang disilangkan tanpa bukti
  kesepadanan; laporan yang memuat CACAH tidak menjawab pertanyaan tentang
  DAFTAR. Contoh hidup: BNXUSDT **51** bulan ARSIP lawan **48** bulan PENYEBUT —
  dua semesta, bukan kontradiksi; bahwa selisih 3 itu tiga lubang tengah
  2022-04/-06/-08 masih **DUGAAN**.
- **Aturan 64 dan KC-26:** ramalan tentang nilai ekstrem wajib menyebut perlakuan
  atas SERI; medan penamai ekstrem wajib melaporkan seluruh pemegangnya.
- **KC-23/aturan 61:** LITUSDT MATI **2025-02..2025-11**; kematian MENDAHULUI
  hilangnya funding (2025-07). Tafsir tebing funding TERBALIK. ADR-A002 §10 tidak
  boleh diubah atas bukti kohort semata.

## ANGKA TERVERIFIKASI (kutip dari laporan, jangan hitung dari udara)

787 penyebut / 937 arsip / 150 hanya-arsip / 0 hanya-penyebut / 21.789 bulan
arsip / 15 nama SETTLED di arsip dan 0 di penyebut; 19.598 simbol-bulan, lolos
19.586, gagal 12 (karantina, tar terpisah); MATI **1.401** / SEPI **98** / HIDUP
**18.087**; 839.842.134 baris (lolos gerbang 839.325.999 + karantina 516.135);
funding **880** lubang, bentuk lokal {awal 45, ekor 826, tengah 6}; 33 HIDUP tanpa
funding; `cacah_simbol_tanpa_hidup` **18**; penyebut per tahun
504/1.385/1.729/2.400/3.570/5.948/4.050 dengan `bagian_mati`
0,001984/0,006498/0,019665/0,042917/0,053782/0,085071/**0,137284** (tertinggi
2026, menanjak monoton); bulan ARSIP CTK 68, CVC 68, CVX 46, LIT 65, MAVIA 29,
SLP 33, ICP 62 (`ICPUSDT_SETTLED` 9), TLM 60 (`TLMUSDTSETTLED` 9), BNX **51**;
BNX **48** di PENYEBUT; `jumlah_bulan_didaftar` 518 atas 24 nama.

**Cacah baris `ukur_baris` V5 (21 berkas, total 8.131):** `funding.py` **705** ·
`silang_funding.py` **705** · `lubang_tengah.py` V2 **560** · `kohort_ekor.py`
553 · `kebangkitan.py` **552** · `penyebut_tahun.py` **527** ·
`tests/test_kebangkitan.py` **501** · `kehidupan_arsip.py` 496 ·
`semesta_silang.py` **423** · `kehidupan.py` 417 · `bulan_settled.py` **386** ·
`pulihkan.py` 383 · `tests/test_penyebut_tahun.py` **369** · `ukur_baris.py` V5
**352** · `tests/test_semesta_silang.py` **253** · `tests/test_bulan_settled.py`
**240** · `gerbang_1m.py` 184 · `funding_cdn.py` **162** · `arsip.py` 154 ·
`resample.py` 127 · `kohort_ringkas.py` 82.

## PEKERJAAN BERIKUTNYA, berurutan

1. **Jurnal 96** — adjudikasi R-253/R-254/R-255 (sudah tercatat di STATE v36,
   tetapi jurnalnya belum ditulis), aturan 64, KC-26, kelahiran H-A014, dan
   praregistrasi R-257 dst.
2. **Baca ulang R-249 di jurnal 94** sebelum papan skor v37 dibekukan; rincian
   baris R-236..R-247 juga masih perlu disalin dari jurnal 92–94 ke papan skor.
3. **Uji H-A014** — kehidupan keenam bulan saudara SETTLED. Bahan sudah di-commit,
   tanpa unduhan. Praregistrasikan ramalannya lebih dulu; ingat penyebut 6 dan
   aturan 59; sertakan kendali positif (aturan 50) dan medan
   `definisi_dapat_dibedakan` (aturan 46).
4. **Pecah `silang_funding.py` dan `funding.py`** (keduanya **705** baris, aturan
   48) — tidak ada lagi alasan menunda: angka barisnya kini terukur, bukan
   taksiran. Waspadai aturan 49 (nama yang DITAMBAL oleh uji). Perbarui daftar
   berkas `sidik_kode`.
5. **`ukur_baris` V6** — perbaiki KC-26 (medan pemegang ekstrem wajib berupa
   DAFTAR) dan masukkan berkas uji yang belum diukur, mulai
   `tests/test_lubang_tengah.py` (56 fungsi, 18.387 B). Satu langkah per versi.
6. **Laporan yang BELUM pernah dibaca:** `reports/semesta_silang.json` penuh
   (identitas 150 simbol hanya-arsip), `reports/penyebut_tahun.json` penuh
   (identitas 18 simbol tanpa bulan HIDUP), `reports/bulan_settled.json`
   (29.820 B), `reports/diagnosa_kc15.json` (42.916 B),
   `reports/kohort_ekor.json` (112.687 B, 28 anggota di luar sampel abjad),
   `reports/funding_selisih_penuh.json` (`daftar_terpotong` true, 500 dari 880),
   `tests/test_pulihkan.py`.
7. **Keputusan 7 ADR-A008** dengan DUA cabang (LITUSDT lawan BTCSTUSDT), per
   simbol-bulan, TANPA kata "serentak", dengan batas USDT tersurat, dan membedakan
   peralihan KONTRAK dari kebangkitan PASAR; **ADR-A003** (taksonomi rezim, kini
   wajib memisahkan kedua hal itu); terima/tolak **ADR-A007**; terapkan ADR-A006;
   medan `dugaan_pengganti` (ADR-A005); karantina artefak 7 hari.
8. Aturan 46 di `pulihkan.py` (LUNAS di kode V2, laporan pecahan di git masih
   V1); adjudikasi **R-199** (`definisi_dapat_dibedakan` diramalkan false pada
   indeks 2 dan 5); adjudikasi R-7, R-19, R-20, R-28, R-36, R-37, dan R-249.
9. Kehidupan **12 simbol-bulan karantina** (tar terpisah); pencocokan 3 lubang
   BNXUSDT dengan 3 simbol-bulan KC-15.
10. Belum diukur: sebab peralihan/kebangkitan kedelapan simbol; sebab KC-15;
    mengapa dua dari enam bulan peralihan jatuh pada 2025-07; `INDEKS` 3 nama
    manual; token saham/komoditas; 16 simbol non-ASCII sisa (币安人生USDT 9,
    我踏马来了USDT 6, 龙虾USDT 4); `.decode("utf-8","replace")`; jurang 38 lawan
    41; skew `waktu_utc`; selisih byte AGIX 531 lawan 529; apakah BUSD/USDC layak
    digabung dengan USDT (kini berangka: 150 simbol, 21.789 lawan 19.598 bulan).
11. Paralel (aturan 3): juri T4 dengan biaya; lapisan validasi (Šidák, ≥300
    permutasi per TANGGAL UTC, PBO dan DSR numpy murni).
    **ADJUDIKASI RISET TETAP TERKUNCI.**

## KEBIASAAN

Ramalan SEBELUM run lalu adjudikasi jujur; hitung ulang tiap angka (aturan 21);
medan penggugur (24); kelas cacat pada sampel (37); dilarang menyimpulkan di luar
rentang (20); kendali positif (50); jendela mundur adaptif (51); laporan tak
terbaca utuh = tak ada (52); cacah butir uji diramalkan dari daftar bernomor
(54/56/57 — kini enam dari enam, karena mekanis, bukan karena cakap); taksiran
cacah baris bias ke BAWAH, jadi lebih baik tidak ditaksir (58); ketiadaan
pengukuran BUKAN ketiadaan gejala (59); ekstrem wajib memikirkan SERI (64).
Ramalan yang hanya menyalin angka terverifikasi adalah ramalan MUDAH — katakan
begitu, jangan membanggakannya. BACA berkas sebelum menuduhnya salah. Pisahkan
fakta dari asumsi. Percepat dengan menumpuk beberapa pertanyaan dalam SATU run
atomik atas bahan yang sudah di-commit, dan dorong modul pengukur lebih dulu agar
runner bekerja sementara jurnal dan STATE ditulis. "lanjut" berarti teruskan tanpa
konfirmasi. Jangan berhenti dengan alasan konteks Notion.
