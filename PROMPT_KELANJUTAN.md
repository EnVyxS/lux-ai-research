# PROMPT KELANJUTAN — v19

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
   - `STATE.md` (**v18**) — aturan 1-35, KC-1..KC-12, papan skor R-1..R-85,
     sensus 9 workflow, bentuk semesta arsip, daftar utang. **PALING PENTING.**
   - `decisions/ADR-A001.md`, `decisions/ADR-A002.md` (termasuk Amandemen A-1),
     `decisions/ADR-A004.md`.
   - `journal/2026-07-28-38.md`, lalu mundur ke 37, 36, 34 bila perlu konteks.
   - `PETA_MODUL.md` bila menyentuh modul warisan.
4. Baru setelah itu jalankan pekerjaan teknis.

Tabel ramalan lama tidak disalin ulang tiap versi: R-1..R-55 ada di STATE v16
(blob `dd9970640fa2a5e2b57d66c410a410c137bab14c`), R-56..R-82 di STATE v17
(blob `1991c3744b292a2f1a4be04a06de3113022e2921`).

## BATASAN YANG MAHAL DIPELAJARI ULANG

- Sandbox agen TIDAK punya jaringan. Semua unduhan dan pengukuran arsip
  dijalankan GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- Tidak ada alat untuk membaca status GitHub Actions. Status hanya diketahui
  dari berkas laporan yang di-commit workflow itu sendiri.
- Tidak ada API patch. `push_files` menulis ulang SELURUH isi berkas. Rancang
  berkas kecil.
- Setelah mendorong berkas panjang, BACA ULANG dari main dan pastikan ekornya
  hadir.
- **Pembacaan berkas besar bisa TERPOTONG.** `reports/semesta_rentang.json`
  hanya tampil ~95%. Bila terpotong, cacah apa pun dari berkas itu dilarang
  diklaim; hitung di runner.
- Runner: numpy, pandas, pyarrow, pyyaml, pytest tersedia; TIDAK ada scipy dan
  requests. `data.binance.vision` bisa diakses; `fapi.binance.com` memberi 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. `lux-research` boleh
  DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.
- **KC-10:** mendorong berkas apa pun ke `lux_ai/serapan/` MENYALAKAN workflow
  `probe-serapan` beranggaran 330 menit. Sampai `probe_serapan.yml` ditambal,
  setiap dorongan modul serapan berbiaya satu run berjaringan.

## POSISI HARI INI (2026-07-28, akhir sesi 38)

- STATE **v18**. Jurnal terakhir **38**. Aturan terakhir **35**. Kelas cacat
  terakhir **KC-12**. Ramalan berikutnya **R-86**. N_percobaan = 0.
- Jumlah uji **102**, terverifikasi CI run 30349383760.
- Papan skor R-1..R-85: TEPAT 47, MELESET 25, MELESET SEPARUH 4, TIDAK
  TERADJUDIKASI 3, MENUNGGU 6.
- **Utang AKTIF: 24 (serapan penuh) dan 27 (sidik + cacah `semesta_rentang`).**
  Utang 7, 25, 26 LUNAS. Utang 1-5 dan 11 menunggu tahap lain.
- Temuan besar sesi 36–38: sensus sembilan workflow lengkap (6 dari 9 melanggar
  aturan 34); semesta arsip BUKAN kumpulan perpetual setara — ada futures
  kedaluwarsa, sisa SETTLED dua ejaan, BUSD/USDC, indeks, dan saham token.

## PEKERJAAN BERIKUTNYA, BERURUTAN

1. **Utang 27 — murah, kerjakan lebih dulu.** Modul kecil yang membaca
   `reports/semesta_rentang.json` di runner, lalu menuliskan laporan BERSIDIK
   berisi: cacah simbol; cacah per `jenis_instrumen`; bulan awal/akhir global;
   cacah simbol yang berhenti sebelum 2026-06; cacah nama non-ASCII beserta
   contohnya (aturan 32); `sidik_kode` dan `sidik_data` (aturan 7, 31, 35).
   Ini sekaligus menyiapkan syarat (h) utang 24. Taruh modulnya DI LUAR
   `lux_ai/serapan/` atau tambal `probe_serapan.yml` lebih dulu, agar tidak
   menyalakan run berjaringan 330 menit (KC-10).
2. **Utang 24 — jalur serapan penuh.** Per ADR-A002 §9 + Amandemen A-1 +
   ADR-A004: 8 pecahan (~2.724 berkas, ~1,0 jam, ~4,9 GB tiap pecahan), tiap
   simbol-bulan lewat `gerbang_1m.nilai_deret`, manifes per simbol-bulan,
   parquet sebagai aset rilis, karantina 7 hari. Mengadjudikasi R-7, R-19,
   R-20, R-36, R-37. **Delapan syarat rancangan** ada di STATE v18 utang 24,
   butir (a)–(h). Syarat (g): tambalan enam workflow pelanggar aturan 34 dan
   tiga cacat `probe_serapan.yml` DIGABUNG ke commit yang sama.
   Pra-registrasi R-86 dst. ditulis LEBIH DULU.
3. **Paralel, boleh sekarang (aturan 3):** ADR-A003 taksonomi rezim; juri T4
   dengan biaya sejak hari pertama; lapisan validasi (uji bulanan berpasangan +
   Sidak, ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy murni).
4. Belum diperiksa: apakah `arsip.bulan_tersedia` aman untuk simbol Tionghoa;
   besar dampak `.decode("utf-8","replace")`; bukti langsung bahwa gelung latar
   `probe_serapan` menyebabkan anomali tree.

Adjudikasi riset tetap TERKUNCI sampai manifes semesta penuh terverifikasi.

## PENOMORAN BERIKUTNYA

ADR-A003 (dicadangkan). Hipotesis riset pertama H-A001 (belum ada; H-A002..A005
adalah hipotesis INFRASTRUKTUR, tidak masuk N_percobaan). Jurnal berikutnya
`journal/2026-07-28-39.md`. STATE berikutnya v19. PROMPT berikutnya v20.
Ramalan berikutnya R-86.

## KEBIASAAN

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. 25 ramalan sudah MELESET;
  itu bukan aib, itu satu-satunya bukti bahwa ramalannya bukan hiasan.
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21).
- Setiap pengukuran sebab wajib memuat medan yang bisa MENGGUGURKAN hipotesis
  yang dipercaya (aturan 24).
- **Jangan meramal dari ingatan tentang isi berkas.** Enam kali saya menuduh
  kode yang ternyata benar (R-56..R-58, R-69, R-71, R-77).
- **Jangan mengaku TEPAT atas angka yang tidak benar-benar dilihat.** R-83
  dinyatakan TIDAK TERADJUDIKASI karena pembacaannya terpotong, walau tebakan
  saya mungkin benar. Tebakan yang kebetulan benar bukan pengukuran.
- Pisahkan fakta dari asumsi; tanpa bukti tulis "Ini memerlukan verifikasi."
- "lanjut" berarti teruskan tanpa konfirmasi.
- Begitu STATE naik versi, PROMPT wajib menyusul pada sesi yang sama. Berkas
  kontinuitas yang USANG lebih berbahaya daripada yang tidak ada.
