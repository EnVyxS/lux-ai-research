# PROMPT KELANJUTAN — versi 33

Disusun 29 Juli 2026, 14:10 WIB, di atas STATE v30 (commit yang sama dengan
berkas ini) dan jurnal 82. Berkas di repo adalah kebenaran; prompt ini hanya
peta.

Kamu melanjutkan riset LUX-AI. Operator: Diva Juan Nur Taqarrub, GitHub EnVyxS,
zona waktu Asia/Jakarta, bahasa kerja Indonesia. Jangan mulai bekerja sebelum
menyelesaikan LANGKAH 0.

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`, dengan
   `owner` dan `repo` HANYA di dalam `toolArguments`, tidak di tingkat atas.
3. Baca dari `main` repo `EnVyxS/lux-ai-research` berurutan: berkas ini,
   `STATE.md` (v30 — aturan 1–53, kelas cacat, papan skor, daftar utang; INI
   YANG PALING PENTING), `journal/2026-07-29-82.md`, lalu `-81.md` dan `-80.md`
   bila perlu latar, `decisions/ADR-A008.md` (DITERIMA 1–6, Keputusan 7
   ditangguhkan), `decisions/ADR-A007.md` (masih DIUSULKAN), lalu `ADR-A004.md`
   dan `ADR-A002.md` bila menyentuh serapan, `PETA_MODUL.md` bila menyentuh
   modul warisan.
4. Baru setelah itu jalankan pekerjaan teknis.

## BATASAN YANG MAHAL DIPELAJARI ULANG

- Sandbox agen TIDAK punya jaringan. Semua unduhan dan pengukuran arsip
  dijalankan GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- Tidak ada alat membaca status GitHub Actions dan tidak ada alat memicu
  `workflow_dispatch`. Status hanya diketahui dari berkas laporan yang
  di-commit workflow itu sendiri, dan satu-satunya cara menyalakan run adalah
  push ke berkas yang tersebut di `paths` workflow. Manfaatkan ini: memperbaiki
  BERKAS UJI tidak menyalakan ulang runner berat, sebab `paths` hanya memuat
  modulnya.
- Tidak ada API patch — `push_files` menulis ulang seluruh isi berkas. Rancang
  berkas kecil, dan sesudah mendorong berkas panjang BACA ULANG dari `main`
  untuk memastikan ekornya hadir (aturan 52).
- Saat memeriksa hasil run, cocokkan `commit` / `run_id` / `sidik_kode`. Jangan
  percaya keberadaan berkas: laporan run lama sering masih terbaca.
- Laporan yang belum terbit menjawab "path does not point to a file" — itu bukan
  kegagalan push, melainkan run yang masih berjalan. Melisting `reports/`
  (path berakhiran garis miring) lebih murah daripada menebak nama berkas.
- `search_code` mengembalikan 0 hasil (tidak berindeks) — pakai
  `get_file_contents`.
- Runner punya numpy, pandas, pyarrow, pyyaml, pytest; TIDAK ada scipy dan
  requests. `data.binance.vision` bisa diakses; `fapi.binance.com` memberi 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. Repo `lux-research`
  boleh DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## POSISI (29 Juli 2026, 14:10 WIB)

Rantai commit mutakhir: `d13b7bfe` (jurnal 81) → `14e75e7d` (STATE v29 + PROMPT
v32) → `0929643c` (kehidupan_arsip V1 + uji + workflow, atomik) → `dceb1009`
(perbaikan harapan uji) → `e94ed337` (jurnal 82) → berkas ini + STATE v30.

Run terverifikasi:

- **kehidupan_arsip delapan pecahan** pada `0929643c`; pecahan 0 =
  **30419770259**, kode 0 di kedelapan.
- **CI 30419770312** (`0929643c`) — 291 butir, kode **1** (harapan uji salah).
- **CI 30420236800** (`dceb1009`) — **291 butir, kode 0**; teks "291 passed".

Papan skor sampai R-209: **TEPAT 146 / MELESET 38 / SEPARUH 12 / TIDAK
TERADJUDIKASI 5 / MENUNGGU 8 = 209** (MENUNGGU: R-7, R-19, R-20, R-28, R-36,
R-37, R-199, R-209). Ramalan berikutnya **R-210**. Aturan terakhir **53**, kelas
cacat terakhir **KC-18**, jurnal berikutnya **83**, STATE berikutnya **v31**,
PROMPT berikutnya **v34**, ADR berikutnya **A009**.

## TEMUAN MUTAKHIR YANG MENENTUKAN ARAH

1. **Kehidupan SELURUH semesta terserap kini terukur.** Dari 19.586 simbol-bulan
   lolos gerbang: **1.401 MATI (7,153%), 98 SEPI (0,500%), 18.087 HIDUP
   (92,35%), 0 tak terukur.** Penyebut tanpa MATI = **18.185**. Kendali positif
   **24/24 hidup**, `parser_terbukti` true pada kedelapan pecahan, nol baris
   cacat dari 839 juta baris.
2. **Uji silang terkuat sesi ini:** jumlah `lilin_penuh` = **839.325.999**,
   cocok PERSIS dengan baris lolos gerbang yang diukur serapan lewat jalur kode
   berbeda (zip, bukan parquet). Dua pengukuran independen bertemu.
3. **Kematian tidak terkurung di kohort puncak.** 456 MATI kohort termuat dalam
   1.401, jadi **945 simbol-bulan MATI di luar kohort** — dua pertiga kematian
   tak terlihat dari kohort funding. Semesta menyusut 7,65%, tidak runtuh.
4. Sebaran mati per pecahan 4,18%–13,14%: DILARANG memakai 7,153% sebagai laju
   kematian simbol mana pun (aturan 20, 39).
5. **Aturan 53 lahir** dari R-205: meramalkan kode keluar tanpa membaca perilaku
   pembulatan fungsi yang dipanggil sendiri. `kohort_ekor.bagian` membulatkan ke
   empat desimal; pembulatan itu TIDAK diubah (aturan 29).
6. ADR-A002 §10 tetap tidak boleh disentuh atas bukti kohort semata. Pertanyaan
   penentunya sekarang: apakah 945 MATI di luar kohort juga kehilangan funding?

## PEKERJAAN BERIKUTNYA

1. **Funding bagi 945 simbol-bulan MATI di luar kohort puncak.** Bahan bakunya
   sudah ada di repo: `reports/kehidupan_arsip_<i>.json` (status per
   simbol-bulan) dan `reports/funding_semesta.json`. Ini pengukuran SILANG
   tanpa jaringan — kerjakan lebih dulu, sebab paling murah dan paling
   menentukan nasib ADR-A002 §10 serta Keputusan 7 ADR-A008.
2. **Sebaran 1.401 MATI menurut tahun dan simbol** dari laporan penuh; ini juga
   dapat menjawab `bulan_hidup_terakhir` bagi 28 anggota kohort di luar sampel
   abjad — dengan syarat definisinya dicocokkan dengan `kohort_ekor` (aturan 36).
3. **Tambahkan `kehidupan_arsip.py` ke `BERKAS_DIUKUR`** di `ukur_baris.py`;
   jangan menaksir cacah barisnya (aturan 21, dan pola R-175/179/203).
4. **R-199** — jalankan ulang `pulihkan` V2 atas kedelapan pecahan.
5. **Ukur sifat 48 lubang funding AWAL dan 6 lubang TENGAH** — prasyarat
   Keputusan 7 ADR-A008.
6. **Terima atau tolak ADR-A007** dengan kendala R-146 (839.842.134 sudah memuat
   516.135 baris karantina). **Terapkan ADR-A006 sepenuhnya**;
   `dugaan_pengganti` (ADR-A005); karantina artefak 7 hari; adjudikasi R-7,
   R-19, R-20, R-28, R-36, R-37.
7. Kehidupan 12 simbol-bulan karantina (tar terpisah, belum disentuh).
8. Belum diukur (daftar penuh di STATE v30 bagian terakhir): sebab KC-15, lubang
   funding BNXUSDT, 15 SETTLED lain, INDEKS 3 nama manual, token saham dan
   komoditas, 16 simbol non-ASCII, `.decode("utf-8","replace")`, BUSD/USDC,
   jurang 38 lawan 41, skew `waktu_utc`, `funding_selisih_penuh.json`, selisih
   byte AGIX 531 lawan 529, `tests/test_pulihkan.py` belum dibaca ulang.
9. Paralel (aturan 3): ADR-A003, juri T4 dengan biaya, lapisan validasi (Šidák,
   ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy murni). **Adjudikasi riset
   TETAP TERKUNCI.**

## KEBIASAAN

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. Ramalan berkepala dua yang
  separuhnya salah dicatat SEPARUH. Ramalan yang penyebutnya nol dicatat TIDAK
  TERADJUDIKASI, bukan TEPAT.
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21). Jangan
  menaksir yang bisa dihitung — pola menaksir panjang berkas sudah meleset tiga
  kali (R-175, R-179, R-203).
- **Aturan 53:** sebelum meramalkan kode keluar CI, baca PERILAKU tiap fungsi
  yang diuji, bukan hanya namanya.
- Setiap pengukuran sebab wajib memuat medan penggugur (aturan 24); aturan 37
  sampel wajib memuat ≥1 kasus tiap kelas cacat relevan; aturan 20 dilarang
  menyimpulkan di luar rentang disampel; aturan 50 kesimpulan dari KETIADAAN
  wajib kendali positif; aturan 51 jendela mundur wajib adaptif; aturan 52
  laporan yang tak terbaca utuh setara dengan tak ada.
- Push yang menyalakan run wajib atomik (aturan 45): modul + uji + workflow.
- BACA berkas sebelum menuduhnya salah — pola salah-tuduh sudah tercegah TUJUH
  kali. Sebaliknya, jangan menuduh modul ketika yang salah adalah harapan uji.
- Pisahkan fakta dari asumsi; tanpa bukti tulis "Ini memerlukan verifikasi."
- "lanjut" berarti teruskan tanpa konfirmasi. Perbarui STATE.md, jurnal, dan
  berkas ini secara berkala. Jangan berhenti dengan alasan konteks Notion;
  patokannya konteks model.
- Tenggat: riset dipercepat sebelum 3 Agustus 2026.
