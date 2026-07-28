# PROMPT KELANJUTAN — v20

Untuk sesi berikutnya riset LUX-AI. Operator: Diva Juan Nur Taqarrub, GitHub
EnVyxS, zona waktu Asia/Jakarta, bahasa kerja Indonesia. **Berkas di repo adalah
kebenaran; prompt ini hanya peta.**

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`. `owner` dan
   `repo` HANYA di dalam `toolArguments`.
3. Baca dari main repo `EnVyxS/lux-ai-research`, berurutan:
   - `STATE.md` (**v19**) — aturan 1-36, KC-1..KC-12, papan skor R-1..R-90,
     taksonomi semesta, sensus 10 workflow, daftar utang. **PALING PENTING.**
   - `decisions/ADR-A001.md`, `ADR-A002.md` (+ Amandemen A-1), `ADR-A004.md`.
   - `journal/2026-07-28-40.md`, mundur ke 39 dan 38 bila perlu konteks.
   - `PETA_MODUL.md` bila menyentuh modul warisan.
4. Baru setelah itu jalankan pekerjaan teknis.

Tabel ramalan lama: R-1..R-55 di STATE v16 (`dd997064…`), R-56..R-82 di v17
(`1991c374…`), R-83..R-85 di v18 (`8b3dd416…`).

## BATASAN YANG MAHAL DIPELAJARI ULANG

- Sandbox agen TIDAK punya jaringan. Semua pengukuran arsip dijalankan GitHub
  Actions; agen hanya boleh percaya artefak yang di-commit.
- Tidak ada alat untuk membaca status Actions. Status hanya diketahui dari
  berkas laporan yang di-commit workflow itu sendiri.
- Tidak ada API patch. `push_files` menulis ulang SELURUH isi berkas.
- Setelah mendorong berkas panjang, BACA ULANG dari main dan pastikan ekornya
  hadir.
- Pembacaan berkas besar bisa TERPOTONG (`semesta_rentang.json` hanya tampil
  ~95%). Bila terpotong, cacah apa pun dilarang diklaim; hitung di runner.
  Pola yang terbukti bekerja: modul kecil + workflow sempit + laporan bersidik.
- Runner: numpy, pandas, pyarrow, pyyaml, pytest ada; scipy dan requests TIDAK.
  `data.binance.vision` bisa diakses; `fapi.binance.com` memberi 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. `lux-research` boleh
  DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.
- **KC-10:** mendorong berkas apa pun ke `lux_ai/serapan/` MENYALAKAN
  `probe-serapan` beranggaran 330 menit. Modul non-serapan taruh di paket lain
  (`lux_ai/semesta/` sudah terbukti aman).

## POSISI HARI INI (2026-07-28, akhir sesi 40)

- STATE **v19**. Jurnal terakhir **40**. Aturan terakhir **36**. KC terakhir
  **KC-12**. Ramalan berikutnya **R-91**. N_percobaan = 0.
- Uji **110**, hijau, run 30351993293, commit `86af7163`.
- Papan skor R-1..R-90: TEPAT 52, MELESET 25, SEPARUH 4, TIDAK TERADJUDIKASI 3,
  MENUNGGU 6.
- **Utang AKTIF: 24 (serapan penuh) dan 28 (selisih 129 vs 128 terhenti).**
- Semesta arsip sudah bertaksonomi dan bersidik: 937 simbol, 21.789 bulan,
  **150 simbol (16,0%) bukan perpetual USDT**.

## PEKERJAAN BERIKUTNYA, BERURUTAN

1. **Utang 28 — murah.** Perluas `lux_ai/semesta/taksonomi.py` (atau modul
   saudaranya) untuk menuliskan DAFTAR simbol terhenti menurut kedua definisi
   dan selisih himpunannya, sehingga satu simbol yang berpindah sisi bernama.
   Aturan 36 mewajibkannya. Pra-registrasi R-91 dst. lebih dulu.
2. **Utang 24 — serapan penuh, pekerjaan besar terakhir sebelum riset.**
   Per ADR-A002 §9 + Amandemen A-1 + ADR-A004: 8 pecahan (~2.724 berkas, ~1,0
   jam, ~4,9 GB tiap pecahan), tiap simbol-bulan lewat `gerbang_1m.nilai_deret`,
   manifes per simbol-bulan, parquet sebagai aset rilis, karantina 7 hari.
   Mengadjudikasi R-7, R-19, R-20, R-36, R-37. Delapan syarat (a)–(h) di STATE
   v19; (h) separuh terbayar — yang tersisa adalah KEPUTUSAN jenis mana yang
   masuk backtest. Rekomendasi awal: perpetual USDT saja pada tahap pertama,
   ditulis sebagai ADR, bukan sebagai kebiasaan diam-diam.
   Syarat (g): tambalan enam workflow pelanggar aturan 34 dan tiga cacat
   `probe_serapan.yml` DIGABUNG ke commit yang sama.
3. **Paralel, boleh sekarang (aturan 3):** ADR-A003 taksonomi rezim; juri T4
   dengan biaya sejak hari pertama; lapisan validasi (uji bulanan berpasangan +
   Sidak, ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy murni).
4. Belum diperiksa: `arsip.bulan_tersedia` untuk simbol Tionghoa; dampak
   `.decode("utf-8","replace")`; bukti langsung gelung latar menyebabkan anomali
   tree; kelengkapan daftar `INDEKS`.

Adjudikasi riset tetap TERKUNCI sampai manifes semesta penuh terverifikasi.

## PENOMORAN BERIKUTNYA

ADR-A003 dicadangkan; ADR untuk pemilihan jenis instrumen akan menjadi A005.
Jurnal berikutnya `journal/2026-07-28-41.md`. STATE berikutnya v20. PROMPT
berikutnya v21. Ramalan berikutnya R-91.

## KEBIASAAN

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. 25 ramalan sudah MELESET;
  itu satu-satunya bukti bahwa ramalannya bukan hiasan.
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21).
- Setiap pengukuran sebab wajib memuat medan yang bisa MENGGUGURKAN hipotesis
  yang dipercaya (aturan 24).
- **Jangan meramal dari ingatan tentang isi berkas.** Enam preseden: R-56..R-58,
  R-69, R-71, R-77.
- **Jangan mengaku TEPAT atas angka yang tidak benar-benar dilihat** (R-83).
  Tebakan yang kebetulan benar bukan pengukuran.
- **Ramalan yang meramalkan berkas yang sudah dilihat itu murah.** Catat
  kemurahannya, jangan menghitungnya sebagai bukti kemampuan.
- Pisahkan fakta dari asumsi; tanpa bukti tulis "Ini memerlukan verifikasi."
- "lanjut" berarti teruskan tanpa konfirmasi.
- Begitu STATE naik versi, PROMPT wajib menyusul pada sesi yang sama.
