# PROMPT KELANJUTAN — v27

Kamu melanjutkan riset LUX-AI. Operator: Diva Juan Nur Taqarrub, GitHub EnVyxS,
zona waktu Asia/Jakarta, bahasa kerja Indonesia. Berkas di repo adalah kebenaran;
prompt ini hanya peta.

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`. `owner` dan
   `repo` HANYA di dalam `toolArguments`.
3. Baca dari `main` repo `EnVyxS/lux-ai-research`, berurutan:
   `PROMPT_KELANJUTAN.md` (v27) → **`STATE.md` (v25 — aturan 1-45, kelas cacat
   KC-1..KC-17, papan skor, daftar utang; INI YANG PALING PENTING)** →
   `journal/2026-07-29-60.md` dan `-61.md` → `decisions/ADR-A006.md` dan
   `ADR-A007.md`. Baca `ADR-A004.md` / `ADR-A002.md` bila menyentuh serapan,
   `PETA_MODUL.md` bila menyentuh modul warisan.
4. Baru setelah itu jalankan pekerjaan teknis.

## Batasan yang mahal dipelajari ulang

- Sandbox agen TIDAK punya jaringan. Semua unduhan dan pengukuran arsip
  dijalankan GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- Tidak ada alat membaca status GitHub Actions dan tidak ada alat memicu
  `workflow_dispatch`. Status hanya diketahui dari berkas laporan yang di-commit
  workflow itu sendiri. **Satu-satunya cara menyalakan run serapan adalah push ke
  `lux_ai/serapan/pecahan.py`** (satu-satunya berkas di `paths`), biasanya dengan
  menaikkan `VERSI`. Matriksnya `[0..7]`, ±1,5 jam per pecahan.
  **Konsekuensinya:** workflow BARU (misalnya uji pemulihan) sebaiknya diberi
  `paths` sendiri yang sempit ke berkas modulnya sendiri, supaya bisa dinyalakan
  tanpa membakar delapan runner serapan.
- **Aturan 45:** push yang MENYALAKAN run wajib memuat semua berkas yang run itu
  butuhkan. Actions memakai workflow pada commit PEMICU; perbaikan workflow di
  commit berikutnya tidak berlaku untuk run yang sedang berjalan. Ini sudah
  terjadi sekali dan memakan satu berkas sidik.
- Tidak ada API patch: `push_files` menulis ulang seluruh isi berkas. Rancang
  berkas kecil. Setelah mendorong berkas panjang, BACA ULANG dari `main` dan
  pastikan ekornya hadir.
- Saat memeriksa hasil run, cocokkan `run_id` / `sidik_kode` / blob sha. Jangan
  percaya keberadaan berkas — laporan run lama sering masih terbaca.
  **`kode_keluar` 0 TIDAK berarti hasilnya sah**: run `30376241019` hijau di
  ketujuh job sementara `verifikasi_rilis.sah` = false. Begitu pula
  `kode_unggah` 0 hanya berarti perintah `gh` pulang tanpa galat.
- Manifes pecahan sangat besar: baca `reports/pecahan_<i>.log`, bukan
  `reports/manifes_pecahan_<i>.json`.
- `search_code` mengembalikan 0 hasil (tidak berindeks) — pakai
  `get_file_contents`.
- Runner: numpy, pandas, pyarrow, pyyaml, pytest tersedia; TIDAK ada scipy dan
  requests. `data.binance.vision` bisa diakses; `fapi.binance.com` memberi 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. `lux-research` boleh
  DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## Posisi (2026-07-29 04:10 WIB)

Rantai sesi ini sesudah PROMPT v26: `57a04f1e` (VERSI 6 + `nama_sums` + 3 uji;
menyalakan matriks) → `5de57a2b` (workflow v4) → `75e7b568` (jurnal 60) →
`f38cd545` (jurnal 61) → STATE v25 + PROMPT v27.

**SEMESTA TERPERSISTENSI UTUH, TERMASUK YANG CACAT.** Run **`30396803601`**,
commit `57a04f1e`, `versi_pecahan` **6**, `sidik_kode` `237ccf42…`, `sidik_data`
`6128fbb0…`: kedelapan pecahan `kode_keluar` 0, `verifikasi_rilis.sah` true ×8,
**19.586 anggota utama dalam 23 bagian** (32.706.262.375 B) dan **12 anggota
karantina dalam 6 bagian** (13.247.705 B) = **29 aset tar**. 19.586 + 12 =
19.598 = semesta. Tag `serapan-pecahan-<i>-30396803601`. **KC-17 DITUTUP.**
Uji **190** (run `30396875564`). R-139..R-143 lima-lima TEPAT.

Satu cacat unggah yang sudah tercatat: `SHA256SUMS_KARANTINA` tidak ikut
terunggah pada run ini (aturan 45); sidik keenam tar karantina ada di
`journal/2026-07-29-61.md` dan di manifes. Berlaku otomatis mulai run berikutnya.

TIDAK ADA RUN YANG SEDANG BERJALAN.

## Pekerjaan berikutnya

1. **UTANG TUNGGAL TERBESAR — uji pemulihan dari luar runner.** Aset rilis belum
   pernah diunduh dan dibongkar oleh proses selain yang menulisnya. Perlu
   workflow tersendiri: `gh release download <tag>` → `sha256sum -c SHA256SUMS`
   → bongkar satu bagian → baca satu parquet dengan pyarrow → cocokkan cacah
   baris terhadap manifes → commit laporan ber-`run_id`. Medan penggugurnya:
   `cacah_sha_tak_cocok`, `cacah_anggota_kurang`, `cacah_baris_tak_cocok`,
   semuanya wajib nol. Daftarkan ramalan SEBELUM menjalankannya.
2. **ADR-A007** (serapan hibrida harian/bulanan) — terima atau tolak, lalu
   implementasikan `sumber_baris`, `cacah_baris_dipulihkan`,
   `cacah_hari_dipulihkan`, `cacah_simbol_bulan_dipulihkan`, tripwire
   `cacah_pemulihan_gagal_checksum` = 0, untuk memulihkan 7.200 menit BNXUSDT.
   Bahan bakunya kini tersimpan (3 tar karantina pecahan 6).
3. Jalur **funding** (`funding_ada` null, ADR-A002 §9) dan `dugaan_pengganti`
   (ADR-A005).
4. Karantina artefak 7 hari; adjudikasi R-7, R-19, R-20, R-28, R-36, R-37.
5. Belum diukur: sebab KC-15; 15 SETTLED lain; INDEKS 3 nama manual;
   saham/komoditas token; 16 simbol non-ASCII sisa;
   `.decode('utf-8','replace')`; BUSD/USDC; selisih 38-vs-41; skew `waktu_utc`.
6. Paralel (aturan 3): ADR-A003 taksonomi rezim; juri T4 dengan biaya; lapisan
   validasi (Šidák, ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy murni).
   **Adjudikasi riset TETAP TERKUNCI** sampai lapisan validasi berdiri.

## Penomoran

Jurnal berikutnya `journal/2026-07-29-62.md`. STATE **v26**. PROMPT **v28**.
ADR berikutnya **A008**. Aturan terakhir **45**. Kelas cacat terakhir **KC-17**
(DITUTUP; KC-16 kosong selamanya — tuduhan yang ditarik). Ramalan berikutnya
**R-144**; papan skor 96/32/5/4/6 = **143**. Uji **190**. N_percobaan = 0.

## Kebiasaan

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. 32 MELESET. Deret TEPAT
  panjang berarti ramalannya terlalu aman — sebutkan itu, jangan rayakan. Lima
  TEPAT terakhir sebagian besar pengulangan sistem yang sudah stabil.
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21).
- Tiap pengukuran sebab wajib memuat medan penggugur (aturan 24); aturan 37
  sampel wajib memuat ≥1 kasus tiap kelas cacat relevan; aturan 43 toleransi
  wajib berskala; aturan 44 ramalan wajib menyebut penyebutnya; aturan 30 dan 41
  penyebut nol bukan bukti.
- Aturan 20: dilarang menyimpulkan di luar rentang yang disampel.
- **BACA berkas sebelum menuduhnya salah.** Pola salah-tuduh sudah ENAM kali;
  yang ketujuh nyaris terjadi dan menghasilkan aturan 42. Dua tabrakan pengemas
  pada VERSI 6 tertangkap justru karena `rilis.py` dibaca lebih dulu.
- Pisahkan fakta dari asumsi. Tanpa bukti, tulis "Ini memerlukan verifikasi."
- "lanjut" berarti teruskan tanpa konfirmasi.
- Perbarui STATE, jurnal, dan prompt ini secara berkala. Jangan berhenti dengan
  alasan konteks Notion; patokannya konteks model.
- Ada tenggat: riset dipercepat sebelum **3 Agustus 2026**.
