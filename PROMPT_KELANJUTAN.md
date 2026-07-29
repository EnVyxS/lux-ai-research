# PROMPT KELANJUTAN — versi 32

Disusun 29 Juli 2026, 10:05 WIB, di atas STATE v29 (commit yang sama dengan
berkas ini) dan jurnal 79, 80, 81. Berkas di repo adalah kebenaran; prompt ini
hanya peta.

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
   `STATE.md` (v29 — aturan, kelas cacat, papan skor, daftar utang; INI YANG
   PALING PENTING), `journal/2026-07-29-79.md`, `-80.md`, `-81.md`,
   `decisions/ADR-A008.md` (DITERIMA 1–6, Keputusan 7 ditangguhkan),
   `decisions/ADR-A007.md` (masih DIUSULKAN), lalu `ADR-A004.md` dan
   `ADR-A002.md` bila menyentuh serapan, `PETA_MODUL.md` bila menyentuh modul
   warisan.
4. Baru setelah itu jalankan pekerjaan teknis.

## BATASAN YANG MAHAL DIPELAJARI ULANG

- Sandbox agen TIDAK punya jaringan. Semua unduhan dan pengukuran arsip
  dijalankan GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- Tidak ada alat membaca status GitHub Actions dan tidak ada alat memicu
  `workflow_dispatch`. Status hanya diketahui dari berkas laporan yang
  di-commit workflow itu sendiri, dan satu-satunya cara menyalakan run adalah
  push ke berkas yang tersebut di `paths` workflow.
- Tidak ada API patch — `push_files` menulis ulang seluruh isi berkas. Rancang
  berkas kecil, dan sesudah mendorong berkas panjang BACA ULANG dari `main`
  untuk memastikan ekornya hadir (aturan 52).
- Saat memeriksa hasil run, cocokkan `commit` / `run_id` / `sidik_kode`. Jangan
  percaya keberadaan berkas: laporan run lama sering masih terbaca. Ini terjadi
  lagi pada 29 Juli (CI 253 basi terbaca sesudah push `d4a2f60a`).
- Laporan yang belum terbit menjawab "path does not point to a file" — itu bukan
  kegagalan push, melainkan run yang masih berjalan. Melisting `reports/`
  (path berakhiran garis miring) lebih murah daripada menebak nama berkas.
- `search_code` mengembalikan 0 hasil (tidak berindeks) — pakai
  `get_file_contents`.
- Runner punya numpy, pandas, pyarrow, pyyaml, pytest; TIDAK ada scipy dan
  requests. `data.binance.vision` bisa diakses; `fapi.binance.com` memberi 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. Repo `lux-research`
  boleh DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## POSISI (29 Juli 2026, 10:05 WIB)

Rantai commit mutakhir: `d4a2f60a` (kehidupan V1 + uji + workflow) →
`f954c0e4` (jurnal 79) → `12dde093` (ukur_baris V2) → `5f291268` (jurnal 80) →
`d13b7bfe` (jurnal 81) → berkas ini + STATE v29.

Run terverifikasi:

- **kehidupan 30418471430** (`d4a2f60a`, kode 0) — 456/456 simbol-bulan MATI.
- **ukur_baris V2 30418761259** (`12dde093`, kode 0) — total 2.950 baris.
- **CI 30418761270** (`12dde093`, kode 0) — **269 butir**.

Papan skor sampai R-204: **TEPAT 143 / MELESET 38 / SEPARUH 11 / TIDAK
TERADJUDIKASI 5 / MENUNGGU 7 = 204** (MENUNGGU: R-7, R-19, R-20, R-28, R-36,
R-37, R-199). Ramalan berikutnya **R-205**. Aturan terakhir **52**, kelas cacat
terakhir **KC-18**, jurnal berikutnya **82**, STATE berikutnya **v30**, PROMPT
berikutnya **v33**, ADR berikutnya **A009**.

## TEMUAN MUTAKHIR YANG MENENTUKAN ARAH

1. **Kohort puncak 2025-07 mati seluruhnya.** 456 dari 456 simbol-bulan
   `transaksi_total` = 0; 19.972.800 lilin; 456 dari 456 lolos gerbang 1m; nol
   berstatus SEPI. Kendali positif hidup 4 dari 4 dan `parser_terbukti` true,
   jadi ini bukan alat yang buta. Penyebut tanpa MATI = 0, sehingga setiap rasio
   di atasnya TIDAK TERADJUDIKASI (aturan 41).
2. Akibatnya kohort ini menyumbang **nol** simbol-bulan yang layak di-backtest.
   Semesta yang dapat dipakai harus dicari di luar 456 unit ini — dan itu belum
   diukur. 456 hanyalah 2,33% dari 19.598; aturan 20 melarang menyimpulkan
   tentang sisanya.
3. Tafsir tebing funding tetap terbalik: kematian klines TIDAK membuktikan arsip
   funding cacat, dan **ADR-A002 §10 tidak boleh diubah atas bukti kohort
   semata**.
4. Pola taksiran panjang berkas meleset untuk ketiga kalinya (R-175, R-179,
   R-203). Bila terulang sekali lagi, jadikan aturan 53.

## PEKERJAAN BERIKUTNYA

1. **Perluas pengukuran kehidupan ke luar kohort puncak.** Butuh sumber daftar
   simbol-bulan selain `kohort_puncak` (mis. `reports/semesta_bulan_1m.json`)
   dan pemecahan, sebab 19.598 unduhan tak muat dalam satu run. Rancang V2
   `kehidupan.py` dengan pemecahan + `KEHIDUPAN_BATAS_SIMBOL`, dan
   praregistrasikan pitanya SEBELUM run.
2. **R-199** — jalankan ulang `pulihkan` V2 atas kedelapan pecahan.
3. **Ukur sifat 48 lubang funding AWAL dan 6 lubang TENGAH** — prasyarat
   Keputusan 7 ADR-A008.
4. **Terima atau tolak ADR-A007** dengan kendala R-146 (839.842.134 sudah memuat
   516.135 baris karantina).
5. **Terapkan ADR-A006 sepenuhnya**; `dugaan_pengganti` (ADR-A005); karantina
   artefak 7 hari; adjudikasi R-7, R-19, R-20, R-28, R-36, R-37.
6. Pindaian `bulan_hidup_terakhir` bagi 28 anggota kohort di luar sampel abjad.
7. Belum diukur (daftar penuh di STATE v29 bagian terakhir): sebab KC-15, lubang
   funding BNXUSDT, 15 SETTLED lain, INDEKS 3 nama manual, token saham dan
   komoditas, 16 simbol non-ASCII, `.decode("utf-8","replace")`, BUSD/USDC,
   jurang 38 lawan 41, skew `waktu_utc`, `funding_selisih_penuh.json`, selisih
   byte AGIX 531 lawan 529.
8. Paralel (aturan 3): ADR-A003, juri T4 dengan biaya, lapisan validasi (Šidák,
   ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy murni). **Adjudikasi riset
   TETAP TERKUNCI sampai manifes semesta penuh terverifikasi.**

## KEBIASAAN

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. Ramalan yang hanya dapat
  diuji pada sebagian kecil unitnya dicatat TIDAK TERADJUDIKASI, bukan TEPAT.
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21). Jangan
  menaksir yang bisa dihitung.
- Setiap pengukuran sebab wajib memuat medan penggugur (aturan 24); aturan 37
  sampel wajib memuat ≥1 kasus tiap kelas cacat relevan; aturan 20 dilarang
  menyimpulkan di luar rentang disampel; aturan 50 kesimpulan dari KETIADAAN
  wajib kendali positif; aturan 51 jendela mundur wajib adaptif; aturan 52
  laporan yang tak terbaca utuh setara dengan tak ada.
- BACA berkas sebelum menuduhnya salah — pola salah-tuduh sudah tercegah TUJUH
  kali (`timeout-minutes: 300` adalah menit, bukan detik).
- Pisahkan fakta dari asumsi; tanpa bukti tulis "Ini memerlukan verifikasi."
- "lanjut" berarti teruskan tanpa konfirmasi. Perbarui STATE.md, jurnal, dan
  berkas ini secara berkala. Jangan berhenti dengan alasan konteks Notion;
  patokannya konteks model.
- Tenggat: riset dipercepat sebelum 3 Agustus 2026.
