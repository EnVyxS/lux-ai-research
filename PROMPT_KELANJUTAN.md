# PROMPT KELANJUTAN — v26

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
   `PROMPT_KELANJUTAN.md` (v26) → **`STATE.md` (v24 — aturan 1-44, kelas cacat
   KC-1..KC-17, papan skor, daftar utang; INI YANG PALING PENTING)** →
   `journal/2026-07-28-57.md`, `-58.md`, `-59.md` → `decisions/ADR-A006.md` dan
   `ADR-A007.md`. Baca `ADR-A004.md` / `ADR-A002.md` bila menyentuh serapan,
   `PETA_MODUL.md` bila menyentuh modul warisan.
4. Baru setelah itu jalankan pekerjaan teknis.

## Batasan yang mahal dipelajari ulang

- Sandbox agen TIDAK punya jaringan. Semua unduhan dan pengukuran arsip
  dijalankan GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- Tidak ada alat membaca status GitHub Actions dan tidak ada alat memicu
  `workflow_dispatch`. Status hanya diketahui dari berkas laporan yang di-commit
  workflow itu sendiri. **Satu-satunya cara menyalakan run adalah push ke
  `lux_ai/serapan/pecahan.py`** (satu-satunya berkas di `paths`), biasanya dengan
  menaikkan `VERSI`. Matriksnya kini `[0..7]`; untuk satu pecahan saja perlu
  `workflow_dispatch` yang tidak dapat dipicu agen.
- Tidak ada API patch: `push_files` menulis ulang seluruh isi berkas. Rancang
  berkas kecil. Setelah mendorong berkas panjang, BACA ULANG dari `main` dan
  pastikan ekornya hadir.
- Saat memeriksa hasil run, cocokkan `run_id` / `sidik_kode` / blob sha. Jangan
  percaya keberadaan berkas — laporan run lama sering masih terbaca.
  **`kode_keluar` 0 TIDAK berarti hasilnya sah**: run `30376241019` hijau di
  ketujuh job sementara `verifikasi_rilis.sah` = false.
- Manifes pecahan sangat besar: baca `reports/pecahan_<i>.log`, bukan
  `reports/manifes_pecahan_<i>.json`.
- `search_code` mengembalikan 0 hasil (tidak berindeks) — pakai
  `get_file_contents`.
- Runner: numpy, pandas, pyarrow, pyyaml, pytest tersedia; TIDAK ada scipy dan
  requests. `data.binance.vision` bisa diakses; `fapi.binance.com` memberi 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. `lux-research` boleh
  DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## Posisi (2026-07-29 02:20 WIB)

HEAD sesudah STATE v24. Rantai sesi ini: `485138ea` → `b71a8c29` (jurnal 57) →
`6ee68891` (pecahan VERSI 5 + matriks 0..7) → `dc702b7a` (jurnal 58) →
`dcf73f4b` (jurnal 59) → STATE v24 + PROMPT v26.

**SEMESTA SUDAH TERPERSISTENSI.** Run `30389402113`, commit `6ee68891`,
`versi_pecahan` 5, `sidik_kode` `dff5d33d…`: kedelapan pecahan `sah` = true,
**19.586 anggota**, **23 bagian tar**, **32.706.262.375 B**, tag
`serapan-pecahan-<i>-30389402113`. Uji **187** (run `30383126672`).

TIDAK ADA RUN YANG SEDANG BERJALAN.

## Pekerjaan berikutnya

1. **KC-17 — karantina belum tersimpan.** Tambahkan pengemas kedua
   (`pecahan_<i>_karantina`, satu tar, 13,2 MB total untuk 12 berkas) dengan
   medan penggugur `cacah_karantina_tak_terkemas` yang wajib nol sebelum
   `parquet_dipersistenkan` boleh true. Naikkan `pecahan.py` ke VERSI 6 — itu
   sekaligus memicu run. Ramalan R-139..R-141 sudah terdaftar untuk run ini.
2. **Uji pemulihan dari luar runner.** Aset rilis belum pernah diunduh dan
   dibongkar oleh proses lain; klaim "dapat dipulihkan" belum lengkap. Perlu
   langkah CI tersendiri (`gh release download` + `sha256sum -c` + baca parquet).
3. **ADR-A007** (serapan hibrida harian/bulanan) — terima atau tolak, lalu
   implementasikan `sumber_baris`, `cacah_baris_dipulihkan`,
   `cacah_hari_dipulihkan`, `cacah_simbol_bulan_dipulihkan`, tripwire
   `cacah_pemulihan_gagal_checksum` = 0, untuk memulihkan 7.200 menit BNXUSDT.
4. Jalur **funding** (`funding_ada` null, ADR-A002 §9) dan `dugaan_pengganti`
   (ADR-A005).
5. Karantina artefak 7 hari; adjudikasi R-7, R-19, R-20, R-28, R-36, R-37.
6. Belum diukur: sebab KC-15; 15 SETTLED lain; INDEKS 3 nama manual;
   saham/komoditas token; 16 simbol non-ASCII sisa;
   `.decode('utf-8','replace')`; BUSD/USDC; selisih 38-vs-41; skew `waktu_utc`.
7. Paralel (aturan 3): ADR-A003 taksonomi rezim; juri T4 dengan biaya; lapisan
   validasi (Šidák, ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy murni).
   **Adjudikasi riset TETAP TERKUNCI** sampai lapisan validasi berdiri.

## Penomoran

Jurnal berikutnya `journal/2026-07-29-60.md`. STATE **v25**. PROMPT **v27**.
ADR berikutnya **A008**. Aturan terakhir **44**. Kelas cacat terakhir **KC-17**
(KC-16 kosong selamanya — tuduhan yang ditarik). Ramalan berikutnya **R-142**;
papan skor 91/32/5/4/9 = 141. N_percobaan = 0.

## Kebiasaan

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. 32 MELESET. Deret TEPAT
  panjang berarti ramalannya terlalu aman — sebutkan itu, jangan rayakan.
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21).
- Tiap pengukuran sebab wajib memuat medan penggugur (aturan 24); aturan 37
  sampel wajib memuat ≥1 kasus tiap kelas cacat relevan; aturan 43 toleransi
  wajib berskala; aturan 44 ramalan wajib menyebut penyebutnya.
- Aturan 20: dilarang menyimpulkan di luar rentang yang disampel.
- **BACA berkas sebelum menuduhnya salah.** Pola salah-tuduh sudah ENAM kali;
  yang ketujuh nyaris terjadi dan menghasilkan aturan 42.
- Pisahkan fakta dari asumsi. Tanpa bukti, tulis "Ini memerlukan verifikasi."
- "lanjut" berarti teruskan tanpa konfirmasi.
- Perbarui STATE, jurnal, dan prompt ini secara berkala. Jangan berhenti dengan
  alasan konteks Notion; patokannya konteks model.
- Ada tenggat: riset dipercepat sebelum **3 Agustus 2026**.
