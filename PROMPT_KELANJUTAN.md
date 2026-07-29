# PROMPT KELANJUTAN — versi 41

Ditulis 29 Juli 2026, 22:05 WIB (sesi 55, lanjutan kesembilan). Menggantikan v40
(blob `cb04bf8830e73c578c215839c2ae3ef0ccacfa9f`). Berkas di repo adalah kebenaran;
prompt ini hanya peta dan boleh saja tertinggal.

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
   - **`STATE.md` v38 — PALING PENTING dan MUTAKHIR** (blob
     **`9f8e8606c2ed9514c1642fa3717b6fb2c1ac84ab`** pada commit
     **`8a0c4bfff05653b66491b76c11ac1999b0a55b3f`**, sudah diverifikasi utuh
     sesudah push, aturan 52). Ia memuat aturan 1–68, KC-1..KC-32, papan skor
     R-1..R-277, semesta riset `perpetual_usdt`, ketiga tabel taksonomi, tabel
     terhenti-lawan-hidup per jenis dengan identitas penuh, penguraian
     163 = 12 + 151, tabel penyebut per tahun, tabel `ukur_baris` V5, daftar 30
     workflow, ringkasan API modul yang sudah terbaca, dan cacah uji 630. **Baca
     UTUH sebelum menulis ulang sebaris pun.**
   - `journal/2026-07-29-105.md` (R-275 TEPAT, R-276 MELESET BESAR, R-277 TEPAT,
     aturan 68, KC-31, praregistrasi R-278) dan `journal/2026-07-29-104.md`
     (R-272/R-273/R-274, aturan 67 terukur, KC-30);
   - `journal/2026-07-29-103.md` bila menyentuh `survei.py` atau asal aturan 67;
     `-102.md` bila menyentuh taksonomi; `-100.md`/`-101.md` bila perlu asal-usul
     aturan 66 revisi, KC-28, KC-29;
   - `journal/2026-07-29-92.md`, `-93.md`, `-94.md` bila menyalin rincian baris
     **R-236..R-247** ke papan skor — satu-satunya utang papan skor yang tersisa;
   - `lux_ai/semesta/taksonomi.py` bila menyentuh penggolongan instrumen;
     `lux_ai/semesta/terhenti.py` V3 bila menyentuh keberhentian terbit;
     `lux_ai/serapan/survei.py` bila menyentuh `semesta_rentang.json`;
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
percaya keberadaan berkas (aturan 38) — perangkap ini menyala berulang: sesudah
push, laporan yang terbaca masih memuat commit run SEBELUMNYA dengan blob yang
tampak wajar. Yang menyelamatkan bukan blob melainkan `list_commits` dengan
`path="reports/<berkas>.json"` (penulis lux-ci; nomor run ada di pesan commit
"laporan CI \<run_id\> [skip ci]"), lalu baca laporan **pada ref commit runner
itu**. `search_code` mengembalikan 0 hasil — pakai `get_file_contents`; path
berakhiran garis miring melisting direktori, dan listing `reports/` TERPOTONG —
pakai path berkas langsung, atau `minimal_output: true`. Runner punya numpy,
pandas, pyarrow, pyyaml, pytest; TIDAK ada scipy dan requests;
`data.binance.vision` bisa diakses, `fapi.binance.com` memberi 451. Dilarang
menulis apa pun di luar repo `lux-ai-research`; `lux-research` boleh DIBACA saja,
hasil dan angkanya tidak pernah boleh masuk.

**Aturan 52 terbukti sebagai penyelamat, bukan formalitas.** Di sesi 55 ia
menangkap dua kerusakan nyata: ekor `STATE.md` v37 yang hilang, dan `}` liar di
akhir `tests/test_terhenti.py` V3 yang membuat SELURUH berkas uji `SyntaxError`.
Keduanya tak terlihat dari keluaran `push_files` yang melaporkan sukses.

## POSISI (29 Juli 2026, 22:05 WIB)

HEAD saat prompt ini ditulis: **`8a0c4bfff05653b66491b76c11ac1999b0a55b3f`**
(STATE v38); commit berikutnya adalah commit yang memuat berkas ini.

Rantai sesi 55, lanjutan terakhir: `620c6101` (jurnal 102) → `ab3ab3b1` (jurnal
103, aturan 67 + KC-30) → **`8121739b`** (`terhenti` V2) → runner `0e6e51fd`
(laporan V2) dan `0fd4d790` (CI 623) → **`9a6b6e65`** (jurnal 104) →
**`7b819787`** (`terhenti` V3, **uji ekor RUSAK**) → runner `9aad0576` (laporan
V3) dan `dfa86186` (CI atas commit rusak) → **`e6b74855`** (perbaikan ekor uji,
lewat `create_or_update_file`) → runner **`e8fb04ab`** (CI **630**) →
**`6c99c350`** (jurnal 105) → **`8a0c4bff`** (STATE v38) → PROMPT v41.

Run TERVERIFIKASI terbaru (commit dicocokkan, aturan 38), semuanya kode 0:

| run | commit | isi |
|---|---|---|
| 30459083416 | `5b968b2a` | CI 610 |
| 30459312700 | `10ca9d4c` | CI 610 |
| 30461798702 | `8121739b` | CI **623** |
| 30462286751 | `7b819787` | CI atas commit RUSAK — **kendali negatif** |
| **30462427226** | **`e6b74855`** | **CI 630**, blob `bee0342e` |

Riwayat CI: … 552 → 584 → 598 → 610 → **623** → **630**.

Papan skor R-1..R-277: TEPAT **196** / MELESET **51** / SEPARUH **16** / TIDAK
TERADJUDIKASI **7** / MENUNGGU **7** = **277** (196+51 = 247; +16 = 263; +7 = 270;
+7 = 277). MENUNGGU: R-7, R-19, R-20, R-28, R-36, R-37, R-199. Terpraregistrasi:
**R-278** (jurnal 105) dan **R-279** (STATE v38). Cacah uji `terhenti` V4 =
**R-280**. Aturan sampai **68**. Kelas cacat sampai **KC-32**. Jurnal berikutnya
**106**. STATE berikutnya **v39**. PROMPT berikutnya **v42**. ADR berikutnya
**A009**.

## PEKERJAAN PERTAMA DI SESI BARU — adjudikasi yang MENGGANTUNG

- **R-279** (praregistrasi di STATE v38): pada commit **`8a0c4bff`** — commit yang
  menyentuh `STATE.md` — `ci.yml` MENYALA sedangkan `terhenti_semesta.yml` TIDAK
  (STATE bukan `lux_ai/semesta/terhenti.py`), dan `reports/ci_terakhir.json` akan
  melaporkan **630** butir dengan `kode_keluar` **0**. Ramalan **MUDAH**, dan
  sudah disebut begitu di muka. **Peringatan:** push PROMPT v41 juga menyalakan
  `ci.yml`, sehingga laporan `8a0c4bff` mungkin TERTIMPA. Bila medan `commit`
  bukan `8a0c4bff`, jangan menyimpulkan apa pun dari berkas itu — cari commit
  runner lewat `list_commits` dengan `path="reports/ci_terakhir.json"` lalu baca
  pada ref itu (aturan 38).
- **R-278** (praregistrasi di jurnal 105): `terhenti` V4 memasangkan kelima belas
  nama SETTLED dengan nama dasarnya (aturan 68). Ramalan: **13 pasangan dengan
  nama dasar masih HIDUP** dan **2 dengan nama dasar TERHENTI** (`SXPUSDT`
  2026-05, `BDXNUSDT`), dan **≥11 dari 13** bulan SETTLED mendahului 2026-06.
  Cacah butir uji V4 = **R-280**, wajib diramalkan dari daftar bernomor sebelum
  run (54/56/57).
- **R-269 dan sesudahnya wajib dipraregistrasi SEBELUM run**, bukan sesudahnya.

## ADJUDIKASI SESI 55 — sudah selesai, jangan diulang

R-248 TEPAT · R-249 TEPAT · R-250 TEPAT (mudah) · R-251 TEPAT · R-252 TEPAT ·
R-253 TEPAT (mudah) · R-254 TEPAT · R-255 **SEPARUH** (705 SERI → aturan 64,
KC-26) · R-256 TEPAT (mudah) · R-257 **MELESET** (790 ≠ 787) · R-258 **MELESET,
klaim DICABUT** (80 dari 147) · R-259 TEPAT · R-260 TEPAT (584) · R-261 TEPAT ·
R-262 TEPAT (mudah) · R-263 **MELESET dan TERBALIK** (151, bukan ≤60) · R-264
TEPAT (598) · R-265 TEPAT · R-266 TEPAT dari DUA arah · R-267 TEPAT (610) · R-268
TEPAT (610) · R-269 TEPAT · R-270 TEPAT · R-271 **MELESET** (129 terhenti;
tuduhan cacat DIBATALKAN sesudah `survei.py` dibaca → aturan 67, KC-30) · R-272
**MELESET** (`sisa_settled` 14 dari 15) · R-273 **MELESET** (28, bukan 40..80) ·
R-274 TEPAT (623) · R-275 **TEPAT** (`SXPUSDTSETTLED` satu-satunya SETTLED hidup)
· R-276 **MELESET TOTAL** (`cacah_peralihan_terhenti` **0** dari 6) · R-277 TEPAT
(630, mudah).

**Empat ramalan berisiko berturut kalah — R-271, R-272, R-273, R-276 — dengan
SEBAB YANG SAMA: membaca NAMA sebagai KEADAAN.** Ini bukan kebetulan dan bukan
nasib buruk; ia satu cacat berpikir yang muncul empat kali.

## TEMUAN MUTAKHIR YANG WAJIB DIBAWA

- **TAFSIR "PERALIHAN NAMA" DICABUT SELURUHNYA.** Rantai pelemahannya:
  "delapan kebangkitan" → "dua bersambung + enam peralihan nama" → **bukan
  peralihan sama sekali**. Bukti: `cacah_peralihan_terhenti` **0**; keenam nama
  dasar H-A013 (CTKUSDT, CVCUSDT, CVXUSDT, LITUSDT, MAVIAUSDT, SLPUSDT) masih
  terbit 2026-06, begitu pula ICPUSDT, TLMUSDT, dan BNXUSDT. Yang benar hanya:
  **nama SETTLED MENAMBAH, tidak MENGGANTI** (aturan 68, KC-31). Dari kelima
  belas nama SETTLED, hanya `SXPUSDT` dan `BDXNUSDT` yang nama dasarnya berhenti
  terbit.
- **`SXPUSDTSETTLED` adalah satu-satunya nama SETTLED yang masih terbit**
  (bulan_terakhir 2026-06, cacah_bulan 1), dan ia menyatukan dua serpihan:
  `SXPUSDT` berhenti 2026-05, `SXPUSDTSETTLED` mulai 2026-06. Selisih 128 lawan
  129 antara dua definisi keberhentian adalah **satu peristiwa penamaan yang
  sedang berlangsung**, bukan cacat pembukuan.
- **Aturan 67:** keanggotaan semesta dan keberlangsungan hidup adalah DUA SUMBU;
  satu dilarang disimpulkan dari yang lain. Angka **28** (nama penyebut yang
  berhenti terbit) DILARANG dicampur dengan **1.401** MATI, **98** SEPI, atau
  **18** `cacah_simbol_tanpa_hidup`. Pasangan 28 lawan 18 paling berbahaya karena
  keduanya kecil dan sama-sama terdengar seperti "simbol mati".
- **Aturan 68:** nama turunan dan nama asal dapat terbit BERSAMAAN; bulan terakhir
  keduanya wajib dilaporkan BERPASANGAN, tidak sendiri-sendiri.
- **KC-32 — mencampur DUA SISTEM PENOMORAN.** Di jurnal 105 saya menulis "R-28
  kini dapat diadjudikasi" atas dasar bahwa **utang verifikasi nomor 28** lunas.
  Keduanya tak berhubungan. **R-28 tetap MENUNGGU**; bunyinya ada di STATE v23 dan
  belum dibaca. Teks jurnal 105 TIDAK disunting (aturan 29); kalimat itu DILARANG
  diwarisi.
- **ANGKA WARISAN DICABUT: "16 simbol non-ASCII" adalah HANTU.** Laporan
  taksonomi memberi **3 nama / 19 bulan** (币安人生USDT 9, 我踏马来了USDT 6,
  龙虾USDT 4), ketiganya `perpetual_usdt` dan ADA di penyebut. Angka 16 sempat
  ditulis dua kali di STATE v37. Asal-usulnya BELUM diketahui dan masuk daftar
  belum diukur.
- **SEMESTA RISET = `perpetual_usdt` = penyebut 787, TERBUKTI DUA ARAH** (kedua
  arah selisih nol, berdaftar kosong → kesamaan himpunan). Kebersihannya
  DIRANCANG: `pecahan.py` menyatakannya di baris pertama docstring dan menyaring
  lewat `taksonomi.jenis_instrumen`.
- **Sembilan kelas kanonik** (`lux_ai/semesta/taksonomi.py`), urutan pemeriksaan
  MENGIKAT: ekspirasi `_\d{6}$` → `SETTLED` → `INDEKS` → kutipan
  `("USDT","USDC","BUSD","USD1","BTC")`. `INDEKS` = {`DEFIUSDT`, `BTCDOMUSDT`,
  `BLUEBIRDUSDT`}; 790 = 787 + 3.
- **Batas yang wajib ikut disebut:** token saham, ETF, dan komoditas (`AAPLUSDT`,
  `XAUUSDT`) tidak dapat dibedakan lewat bentuk nama, jadi mereka **IKUT di dalam
  787** (`taksonomi.CATATAN_BATAS`). Kadar kematian DILARANG ditafsirkan sebagai
  sifat "pasar kripto".
- **Aturan 66 [REVISI]:** setiap cacahan semesta wajib menyebut KELAS INSTRUMEN.
  Sebelum menuduh sebuah batas tidak ada, berkas penyaringnya WAJIB dibaca —
  ketidaktahuan pembaca bukan cacat rancangan. Perluasan v38: **sebelum menulis
  modul baru, LISTING direktori paket dan direktori workflow lebih dulu.**
- **Aturan 65/KC-27:** setiap daftar contoh wajib menyebut CARA pemilihannya;
  daftar yang bukan seluruhnya hanya membuktikan KEBERADAAN, tidak pernah
  PROPORSI.
- **KC-28 DIBATASI** ke arsip 937, bukan penyebut 787. **KC-29** taksonomi
  paralel: `TAK_DIKENAL` 51 = 50 `futures_kedaluwarsa` + 1 `perpetual_usd1`.
- **Penguraian selisih 163 = 12 + 151, `identitas_utuh` true.** Kesamaan angka 12
  dengan 12 simbol-bulan karantina **BUKAN bukti identitas himpunan**.
- **DUA konvensi nama SETTLED hidup berdampingan:** `ICPUSDT_SETTLED` bergaris
  bawah; `TLMUSDTSETTLED` dan yang lain TANPA. Docstring `penyebut_tahun.py`
  masih salah — jangan disunting, cukup jangan diwarisi.
- **KC-23/aturan 61:** LITUSDT MATI 2025-02..2025-11; kematian MENDAHULUI
  hilangnya funding (2025-07). Tafsir tebing funding TERBALIK. ADR-A002 §10 tidak
  boleh diubah atas bukti kohort semata.
- **KC-18:** kecocokan bulan membuktikan PENAMAAN kontrak, bukan perdagangan.
  **H-A014 masih BELUM DIUJI.**

## ANGKA TERVERIFIKASI (kutip dari laporan, jangan hitung dari udara)

**Semesta:** 787 penyebut = seluruh `perpetual_usdt` / 937 arsip / 150 hanya-arsip
(= 147 bukan-akhiran-USDT + 3 indeks) / 0 hanya-penyebut / 21.789 bulan arsip /
19.598 bulan milik penyebut / 15 nama SETTLED di arsip dan 0 di penyebut / 790
nama berakhiran USDT.

**Per jenis kanonik (nama / bulan / terhenti / hidup):** `perpetual_usdt`
787/19.598/**28**/759 · `futures_kedaluwarsa` 50/258/**44**/6 · `perpetual_busd`
41/812/**41**/0 · `perpetual_usdc` 39/893/**1**/38 · `sisa_settled`
15/36/**14**/1 · `indeks` 3/151/**1**/2 · `perpetual_usd1` 1/2/0/1 ·
`basis_non_fiat` 1/39/0/1 · `tak_tergolong` 0/0/0/0. Jumlah 937 / 21.789 /
**129** / **808** ✅. Hidup di luar penyebut = **49**.

**Keberhentian dua definisi:** survei **128**, taksonomi **129**, hanya-taksonomi
**1** (`SXPUSDT` 2026-05), hanya-survei **0**. Ekor: {2026-03: 1, 2026-04: 3,
2026-05: 1, 2026-06: 808}.

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

**Sidik terbaru:** `terhenti` V3 `sidik_kode` `d892391d…`, `sidik_data`
`6128fbb0…`, laporan blob `e4f71ba8` pada ref runner `9aad0576`;
`terhenti_semesta.json` sumber_byte 110.662, `sumber_bersidik` **false** (sumber
`semesta_rentang.json` belum bersidik — utang aturan 22).

**Cacah baris `ukur_baris` V5 (21 berkas, total 8.131):** tabel lengkap di STATE
v38; terbesar **705 SERI** (`funding.py`, `silang_funding.py`), berikutnya
`lubang_tengah.py` V2 **560**. BELUM diukur: `taksonomi.py`, `terhenti.py` V3,
`tests/test_terhenti.py` V3, `pecahan.py`, `semesta_kuota.py` V3,
`ringkas_semesta.py`, `survei.py`, `tests/test_semesta_kuota.py`,
`tests/test_lubang_tengah.py`.

**Cacah uji 630** — `tests/test_terhenti.py` 25 butir (5 → 18 → 25);
`test_semesta_kuota` 58 · `test_lubang_tengah` 56 · `test_kebangkitan` 54 ·
`test_silang_funding` 49 · `test_penyebut_tahun` 44 · `test_semesta_silang` 32 ·
`test_bulan_settled` 26. Aturan 57 kini **dua belas dari dua belas** — karena
mekanis, bukan karena cakap.

## PEKERJAAN BERIKUTNYA, berurutan

1. **Adjudikasi R-279** (630 pada commit `8a0c4bff`) — jurnal **106**.
2. **`terhenti` V4 untuk R-278** — pemasangan 15 nama SETTLED dengan nama
   dasarnya (aturan 68), medan `pasangan_settled` dengan bulan terakhir KEDUA
   nama, `dasar_hidup`/`dasar_terhenti`, dan kendali positif (50). Ramalkan cacah
   butir uji V4 = **R-280** dari daftar bernomor lebih dulu. Dorong modul lebih
   dulu agar runner bekerja sementara jurnal ditulis.
3. **Uji H-A014** — kehidupan keenam bulan saudara SETTLED (CTKUSDTSETTLED
   2025-04, CVCUSDTSETTLED 2025-05, CVXUSDTSETTLED 2025-07, LITUSDTSETTLED
   2025-12, MAVIAUSDTSETTLED 2025-03, SLPUSDTSETTLED 2025-07). Sesudah R-276,
   pertanyaannya BERUBAH: bukan lagi "apakah nama dasar berhenti", melainkan
   **apakah bulan SETTLED itu bulan tanpa perdagangan di TENGAH hidup nama
   dasarnya**. Bahan sudah di-commit, tanpa unduhan. Penyebut 6 → aturan 59;
   kendali positif (50); medan `definisi_dapat_dibedakan` (46).
4. **Pecah `funding.py` dan `silang_funding.py`** (keduanya **705**, aturan 48).
   Waspadai aturan 49 (`monkeypatch`, `patch`, akses atribut modul). Perbarui
   cakupan `sidik_kode` (aturan 22), termasuk berkas di paket lain (KC-29).
5. **`ukur_baris` V6** — perbaiki KC-26 (pemegang ekstrem jadi DAFTAR + `seri`)
   dan tambahkan sembilan berkas yang belum terukur di atas. Satu langkah per
   versi.
6. **Laporan yang BELUM pernah dibaca:** `reports/semesta_rentang.json`
   (110.662 B, **TIDAK bersidik** — sumber `terhenti` dan `survei`),
   `ringkas_semesta.json`, `survei_semesta.json`, `survei_progres.json`,
   `rentang_kc6.json`, `semesta_kuota.json` penuh (147 nama),
   `semesta_silang.json`, `penyebut_tahun.json` (18 simbol tanpa HIDUP),
   `bulan_settled.json` (29.820 B), `diagnosa_kc15.json` (42.916 B),
   `kohort_ekor.json` (112.687 B), `funding_selisih_penuh.json`
   (`daftar_terpotong` true, 500 dari 880), `tests/test_pulihkan.py`. **LUNAS:**
   `taksonomi_semesta.json`, `terhenti_semesta.json` V1/V2/V3, `ci_terakhir.json`.
7. **Keputusan 7 ADR-A008** dengan DUA cabang (LITUSDT lawan BTCSTUSDT), per
   simbol-bulan, TANPA kata "serentak", wajib menyebut batas `perpetual_usdt` dan
   membedakan peralihan KONTRAK dari kebangkitan PASAR — **hasil R-276 MENGIKAT:
   tak ada peralihan yang terbukti**. **ADR-A003** (taksonomi kanonik + aturan
   68); terima/tolak **ADR-A007**; terapkan ADR-A006; medan `dugaan_pengganti`
   (ADR-A005); karantina artefak 7 hari.
8. Aturan 46 di `pulihkan.py` (LUNAS di kode V2, laporan pecahan di git masih V1);
   **gali bunyi R-28 dari riwayat `STATE.md` v23 sebelum mengadjudikasinya**
   (KC-32), begitu pula R-7, R-19, R-20, R-36, R-37, R-199.
9. **Salin rincian baris R-236..R-247** dari jurnal 92–94 ke papan skor STATE —
   satu-satunya utang papan skor yang tersisa; agregatnya sudah masuk hitungan.
10. **Bedakan dua tafsir selisih 12** lewat NAMA dan BULAN, bukan cacah; kehidupan
    12 simbol-bulan karantina (`SHA256SUMS_KARANTINA`, `nama_dasar_karantina(i)`);
    pencocokan 3 lubang BNXUSDT dengan 3 simbol-bulan KC-15.
11. Belum diukur: asal-usul "16 non-ASCII"; mengapa `SXPUSDT` berhenti 2026-05 dan
    siapa 4 nama ekor 2026-03 (1) dan 2026-04 (3); apakah `POLUSDT` ada di 787
    (dugaan MATIC→POL masih ASUMSI, MATICUSDT dan MATICUSDC berhenti bersama);
    daftar 147 nama hanya-arsip; 18 simbol tanpa bulan HIDUP; sebab KC-15; mengapa
    dua dari enam bulan SETTLED jatuh pada 2025-07; apakah **50 kontrak
    bertanggal** pernah masuk perhitungan mana pun (44 terhenti, 6 hidup: tiga
    BTCUSDT_2606/2609/2612 dan tiga saudara ETH); token saham/komoditas di dalam
    787; `.decode("utf-8","replace")`; jurang 38 lawan 41; skew `waktu_utc`;
    selisih byte AGIX 531 lawan 529; apakah BUSD/USDC layak digabung (80 nama,
    1.705 bulan; 38 dari 39 USDC HIDUP); **satuan stempel mikro lawan mili**
    (`survei.satuan_stempel`); 28 anggota kohort di luar sampel abjad.
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
(54/56/57); taksiran cacah baris bias ke BAWAH, jadi lebih baik tidak ditaksir
(58); ketiadaan pengukuran BUKAN ketiadaan gejala (59); ekstrem wajib memikirkan
SERI (64); daftar contoh wajib menyebut cara pemilihannya (65); cacahan semesta
wajib menyebut kelas instrumen (66); keanggotaan bukan kehidupan (67); nama
turunan tidak menggantikan nama asal (68). Ramalan yang hanya menyalin angka
terverifikasi adalah ramalan MUDAH — katakan begitu, jangan membanggakannya.
**BACA berkas sebelum menuduhnya salah.** **JANGAN membaca NAMA sebagai
KEADAAN** — empat ramalan berisiko berturut kalah karena itu. Pisahkan fakta dari
asumsi. Percepat dengan menumpuk beberapa pertanyaan dalam SATU run atomik atas
bahan yang sudah di-commit, dan dorong modul pengukur lebih dulu agar runner
bekerja sementara jurnal dan STATE ditulis. "lanjut" berarti teruskan tanpa
konfirmasi. Jangan berhenti dengan alasan konteks Notion.
