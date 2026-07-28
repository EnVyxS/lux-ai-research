# PROMPT KELANJUTAN — v18

Untuk sesi berikutnya riset LUX-AI. Operator: Diva Juan Nur Taqarrub, GitHub
EnVyxS, zona waktu Asia/Jakarta, bahasa kerja Indonesia. **Berkas di repo adalah
kebenaran; prompt ini hanya peta.**

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`. `owner` dan
   `repo` HANYA di dalam `toolArguments`, tidak di tingkat atas.
3. Baca dari main repo `EnVyxS/lux-ai-research`, berurutan:
   - `STATE.md` (**v17**) — aturan 1-34, kelas cacat KC-1..KC-11, papan skor
     R-1..R-82, sensus 9 workflow, daftar utang. **INI YANG PALING PENTING.**
   - `decisions/ADR-A001.md`, `decisions/ADR-A002.md` (termasuk Amandemen A-1),
     `decisions/ADR-A004.md`.
   - `journal/2026-07-28-36.md`, lalu mundur ke 35, 34, 33 bila perlu konteks.
   - `PETA_MODUL.md` bila menyentuh modul warisan.
4. Baru setelah itu jalankan pekerjaan teknis.

Catatan: STATE v17 sengaja TIDAK menyalin ulang tabel R-1..R-55; tabel itu ada
lengkap di STATE v16, blob `dd9970640fa2a5e2b57d66c410a410c137bab14c`.

## BATASAN YANG MAHAL DIPELAJARI ULANG

- Sandbox agen TIDAK punya jaringan. Semua unduhan dan pengukuran arsip
  dijalankan GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- Tidak ada alat untuk membaca status GitHub Actions. Status hanya diketahui
  dari berkas laporan yang di-commit workflow itu sendiri.
- Tidak ada API patch. `push_files` menulis ulang SELURUH isi berkas. Rancang
  berkas kecil.
- Setelah mendorong berkas panjang, BACA ULANG dari main dan pastikan ekornya
  hadir.
- Runner: numpy, pandas, pyarrow, pyyaml, pytest tersedia; TIDAK ada scipy dan
  requests. `data.binance.vision` bisa diakses; `fapi.binance.com` memberi 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. `lux-research` boleh
  DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.
- **BARU (KC-10):** mendorong berkas apa pun ke `lux_ai/serapan/` MENYALAKAN
  workflow `probe-serapan` beranggaran 330 menit. Sampai `probe_serapan.yml`
  ditambal, setiap dorongan modul serapan berbiaya satu run berjaringan.

## POSISI HARI INI (2026-07-28, akhir sesi 36)

- STATE **v17**. Jurnal terakhir **36**. Aturan terakhir **34**. Kelas cacat
  terakhir **KC-11**. Ramalan berikutnya **R-83**. N_percobaan = 0.
- Jumlah uji **102**, terverifikasi CI run 30349383760.
- Papan skor R-1..R-82: TEPAT 46, MELESET 24, MELESET SEPARUH 4, TIDAK
  TERADJUDIKASI 2, MENUNGGU 6.
- **Utang AKTIF tinggal SATU: utang 24 (serapan penuh).** Utang 7, 25, 26 LUNAS
  di sesi ini. Utang 1-5 dan 11 menunggu tahap lain.
- T1 serapan: probe SELESAI, survei semesta SELESAI dan teringkas, KC-6 terukur
  dan diputus (ADR-A004), gerbang integritas 1m ADA dalam kode dan teruji.

## PEKERJAAN BERIKUTNYA, BERURUTAN

1. **Utang 24 — jalur serapan penuh.** Per ADR-A002 §9 + Amandemen A-1 +
   ADR-A004: 8 pecahan (~2.724 berkas, ~1,0 jam, ~4,9 GB tiap pecahan), tiap
   simbol-bulan lewat `gerbang_1m.nilai_deret`, manifes per simbol-bulan (nama,
   baris, rentang waktu, checksum, sumber, funding_ada, baris_dibuang,
   berheader, awal_sejati, akhir_sejati, satuan stempel, hasil gerbang), parquet
   sebagai aset rilis, karantina 7 hari. Mengadjudikasi R-7, R-19, R-20, R-36,
   R-37.
   **Tujuh syarat rancangan mengikat** ada di STATE v17 utang 24, butir (a)–(g).
   Syarat (g) penting: tambalan enam workflow pelanggar aturan 34 dan tiga cacat
   `probe_serapan.yml` (persempit `paths:`, hapus gelung latar, ganti `-A`)
   DIGABUNG ke commit yang sama supaya hanya satu run menyala.
   Pra-registrasi R-83 dst. ditulis LEBIH DULU.
2. **Paralel, boleh sekarang (aturan 3):** ADR-A003 taksonomi rezim; juri T4
   dengan biaya sejak hari pertama (fee taker/maker terpisah, funding tiap
   jadwal, slippage selalu merugikan); lapisan validasi (uji bulanan berpasangan
   + Sidak, ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy murni).
3. **Kecil, murah:** baca `reports/semesta_rentang.json` (terbukti ada, ditulis
   `survei.py`) untuk menjawab bulan awal/akhir, keterurutan, duplikat, dan
   simbol berhenti 2024-05 tanpa survei ulang.
4. Belum diperiksa: apakah `arsip.bulan_tersedia` aman untuk simbol Tionghoa;
   besar dampak `.decode("utf-8","replace")`; bukti langsung bahwa gelung latar
   `probe_serapan` menyebabkan anomali tree.

Adjudikasi riset tetap TERKUNCI sampai manifes semesta penuh terverifikasi.

## PENOMORAN BERIKUTNYA

ADR-A003 (dicadangkan). Hipotesis riset pertama H-A001 (belum ada; H-A002..A005
adalah hipotesis INFRASTRUKTUR dan tidak masuk N_percobaan). Jurnal berikutnya
`journal/2026-07-28-37.md`. STATE berikutnya v18. PROMPT berikutnya v19.
Ramalan berikutnya R-83.

## KEBIASAAN

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. 24 ramalan sudah MELESET;
  itu bukan aib, itu satu-satunya bukti bahwa ramalannya bukan hiasan.
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21).
- Setiap pengukuran sebab wajib memuat medan yang bisa MENGGUGURKAN hipotesis
  yang dipercaya (aturan 24).
- **Jangan meramal dari ingatan tentang isi berkas.** Enam kali saya menuduh
  kode yang ternyata benar (R-56..R-58, R-69, R-71, R-77). Baca dulu, ramal
  kemudian — atau ramalkan dengan sadar bahwa itu tebakan buta.
- Pisahkan fakta dari asumsi; tanpa bukti tulis "Ini memerlukan verifikasi."
- "lanjut" berarti teruskan tanpa konfirmasi.
- Perbarui STATE.md, jurnal, dan PROMPT_KELANJUTAN.md secara berkala. Berkas
  kontinuitas yang USANG lebih berbahaya daripada yang tidak ada: begitu STATE
  naik versi, PROMPT wajib menyusul pada sesi yang sama.
