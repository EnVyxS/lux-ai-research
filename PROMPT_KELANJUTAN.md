# PROMPT KELANJUTAN — v25

Kamu melanjutkan riset LUX-AI. Operator: Diva Juan Nur Taqarrub, GitHub EnVyxS,
zona waktu Asia/Jakarta, bahasa kerja Indonesia. Jangan mulai bekerja sebelum
menyelesaikan LANGKAH 0. **Berkas di repo adalah kebenaran; prompt ini hanya
peta.**

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`. `owner` dan
   `repo` HANYA di dalam `toolArguments`, tidak di tingkat atas.
3. Baca dari `main` repo `EnVyxS/lux-ai-research`, berurutan:
   - `PROMPT_KELANJUTAN.md` (v25)
   - **`STATE.md` (v23 — aturan 1-42, kelas cacat KC-1..KC-15, papan skor,
     daftar utang; INI YANG PALING PENTING)**
   - `journal/2026-07-28-51.md` dan `-52.md`
   - `decisions/ADR-A007.md`, lalu `ADR-A006.md`
   - `ADR-A004.md` dan `ADR-A002.md` bila menyentuh serapan
   - `PETA_MODUL.md` bila menyentuh modul warisan
4. Baru setelah itu jalankan pekerjaan teknis.

## Batasan yang mahal dipelajari ulang

- Sandbox agen **tidak punya jaringan**. Semua unduhan dan pengukuran arsip
  dijalankan GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- **Tidak ada alat untuk membaca status GitHub Actions** dan tidak ada alat untuk
  memicu `workflow_dispatch`. Status hanya dari berkas laporan yang di-commit
  workflow itu sendiri. Satu-satunya cara menyalakan run adalah **push ke berkas
  modul yang tersebut di `paths` workflow**.
- **Tidak ada API patch.** `push_files` menulis ulang seluruh isi berkas.
  Rancang berkas kecil; setelah mendorong berkas panjang, BACA ULANG dari `main`
  dan pastikan ekornya hadir.
- Saat memeriksa hasil run, cocokkan `run_id` / `commit` / `sidik_kode` / blob
  sha. **Jangan percaya keberadaan berkas.** Sesi 52 membuktikan gunanya: dua
  commit bisa memicu run yang sama, satu di antaranya cacat.
- Manifes pecahan sangat besar: baca `reports/pecahan_<i>.log`, bukan
  `reports/manifes_pecahan_<i>.json`. Untuk diagnosa, `*.log` memuat ringkasan
  tanpa rincian — jauh lebih murah daripada `*.json`.
- `search_code` mengembalikan 0 hasil di repo ini — pakai `get_file_contents`.
- Runner: numpy, pandas, pyarrow, pyyaml, pytest tersedia; **tidak ada** scipy
  dan requests. `data.binance.vision` bisa diakses; `fapi.binance.com` → 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. `lux-research` boleh
  DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## Posisi (2026-07-28, akhir sesi 52)

Rantai commit dua sesi terakhir: `38e36c2b` → `56b28db8` (jurnal 50) →
`f3096288` (diagnosa kc14c) → `9bd95187` (STATE v21 + PROMPT v23) → `0702d9c1`
(rilis.py + serap.py v3 + 2 berkas uji) → `5950152e` (jurnal 51) → `ed203678`
(diagnosa_kc15 v1, cacat) → `a360bf11` (perbaikan kc15) → `4aea79ce` (ADR-A007)
→ `5732730e` (STATE v22 + PROMPT v24) → `abab482e` (jurnal 52) → STATE v23 +
PROMPT v25.

**TIDAK ADA RUN YANG SEDANG BERJALAN.** Semua laporan sudah diadjudikasi.

Dua temuan besar yang sudah selesai:
- **KC-15 TERBUKTI** (sesi 51): berkas BULANAN kehilangan 5 hari UTC penuh yang
  utuh di berkas HARIAN — BNXUSDT 2022-04/06/08, 7.200 menit, dapat dipulihkan.
  12 karantina terpisah: KC-14 9 kasus / 6.375 menit, KC-15 3 kasus / 7.200.
- **H-A005 GUGUR dan KC-16 DITARIK** (sesi 52): 37 bulan TENGAH dari kedelapan
  pecahan, `total_menit_tepi` = 0, seluruh lima kelas risiko tersentuh
  (`kelas_risiko_kosong` = []). 210 menit BNXUSDT 2022-04 terbukti SAH — itu
  bulan pertama simbol itu di arsip (run `30369333069`, commit `a360bf11`).

Uji **141** terverifikasi (run `30359672326`); empat berkas uji ditambahkan
sesudahnya dan cacah barunya belum sah sampai CI melaporkannya (aturan 38).

## Pekerjaan berikutnya, berurutan

1. **ADR-A006 bagian 2/2 — SATU-SATUNYA penghalang agar data serapan bertahan.**
   Sambungkan `rilis.PengemasBerbelah` ke `pecahan.py`: naikkan `VERSI` ke 3,
   tambahkan `rilis.py` ke `sidik_kode`, gerbangi dengan env `PECAHAN_KEMAS`,
   dan perluas `.github/workflows/pecahan_serapan.yml` agar mengunggah tar
   terbelah ≤1,8 GB + `SHA256SUMS` sebagai aset rilis lewat `gh release`.
   **Menaikkan `VERSI` menyalakan matriks 8 job ±1,5 jam** — lakukan hanya
   setelah CI membuktikan `rilis.py`, dan tulis ramalan R-121.. LEBIH DULU.
   Sampai ini selesai, 32,71 GB parquet tetap ditulis, diukur, dihapus, dan
   adjudikasi riset TETAP TERKUNCI.
2. Periksa `reports/ci_terakhir.json` untuk cacah uji baru (aturan 38).
3. **Terima atau tolak ADR-A007**, lalu terapkan: `sumber_baris`
   (`bulanan`/`harian`), `cacah_baris_dipulihkan`, `cacah_hari_dipulihkan`,
   `cacah_simbol_bulan_dipulihkan`, tripwire `cacah_pemulihan_gagal_checksum`
   = 0, gerbang dijalankan ULANG tanpa pelunakan ambang. Memulihkan 7.200 menit
   BNXUSDT. Cakupannya TIDAK perlu diperluas ke tepi bulan (H-A005 gugur).
4. Jalur **funding**: `funding_ada` masih null di seluruh manifes (ADR-A002 §9);
   medan `dugaan_pengganti` (ADR-A005) juga belum ada.
5. Sisa utang 24: karantina artefak 7 hari; mengadjudikasi R-7, R-19, R-20,
   R-36, R-37.
6. Belum diukur: sebab KC-15 (khas simbol? khas 2022? tersebar?); 15 `SETTLED`
   lain; kelengkapan `INDEKS` (3 nama manual); pemisahan saham/komoditas token
   dari 787 `perpetual_usdt`; 16 simbol non-ASCII sisa; `.decode("utf-8",
   "replace")`; apakah BUSD/USDC layak digabung; selisih penyebut 38 lawan 41
   di diagnosa KC-15.
7. Paralel, boleh kapan saja (aturan 3): ADR-A003 taksonomi rezim; juri T4
   dengan biaya sejak hari pertama; lapisan validasi (uji bulanan berpasangan +
   Šidák, ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy murni).
8. Utang lama menunggu tahap lain: 1, 2, 3, 4, 5, 11.

## Ramalan

- Tidak ada ramalan yang menunggu run. Yang masih MENUNGGU tahap lain: R-7,
  R-19, R-20, R-28, R-36, R-37.
- Papan skor R-1..R-120: TEPAT **78**, MELESET **28**, SEPARUH **4**, TIDAK
  TERADJUDIKASI **4**, MENUNGGU **6** (jumlah 120 ✅). Ramalan berikutnya
  **R-121**, ditulis SEBELUM matriks pengemas dinyalakan. N_percobaan = 0.

## Penomoran berikutnya

Jurnal `journal/2026-07-28-53.md`. STATE v24. PROMPT v26. ADR berikutnya
**A008** (A003 dicadangkan, belum ada). Hipotesis: H-A001 (belum), H-A002a/b
(selesai), H-A003 (selesai: menang 3, gugur 9), H-A004 (tak dapat diuji),
H-A005 (gugur pada 37 sampel). Aturan terakhir **42**. Kelas cacat terakhir
**KC-15**; **KC-16 DITARIK dan nomornya bebas**.

## Kebiasaan

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. 28 MELESET; deret TEPAT
  panjang = ramalan terlalu aman. Dua sesi terakhir: ramalan berisiko meleset,
  ramalan berpita longgar tepat — pita longgar tidak mengajari apa pun.
- Aturan 41: ramalan bersyarat berpenyebut nol = TIDAK TERADJUDIKASI, bukan
  TEPAT.
- Aturan 42: kelas cacat dilarang dinamai atas dasar satu angka yang belum
  diukur langsung. KC-16 hampir menjadi salah-tuduh KETUJUH; yang menahannya
  adalah membaca `gerbang_1m.py` lebih dulu lalu menjadikan kecurigaan itu run.
- Aturan 40: `baris + hilang_di_tengah + tepi = menit_kalender`, laporkan
  selisihnya walau nol.
- Aturan 39: keseragaman pada sampel dilarang jadi angka ramalan bagi anggota di
  luar sampel.
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21). Aturan 24
  medan penggugur; aturan 37 tiap kelas cacat relevan terwakili dan kelas kosong
  wajib disebut; aturan 30 penyebut eksplisit; aturan 20 dilarang menyimpulkan
  di luar rentang disampel.
- **BACA berkas sebelum menuduhnya salah** (pola salah-tuduh ENAM kali).
- Pisahkan fakta dari asumsi; tanpa bukti tulis "Ini memerlukan verifikasi."
- "lanjut" berarti teruskan tanpa konfirmasi.
- Perbarui `STATE.md`, jurnal, dan `PROMPT_KELANJUTAN.md` secara berkala.
- Jangan berhenti dengan alasan konteks Notion; patokannya konteks model.
- Ada tenggat: riset dipercepat sebelum **3 Agustus 2026**.
