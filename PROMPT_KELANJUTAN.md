# PROMPT KELANJUTAN — v28

Disusun 2026-07-29 dari STATE v26 (blob `c07d5e58`) yang dibaca langsung dari
`main`. Berkas di repo adalah kebenaran; prompt ini hanya PETA. Bila peta dan
berkas berselisih, berkas yang menang.

Operator: Diva Juan Nur Taqarrub · GitHub `EnVyxS` · Asia/Jakarta · bahasa kerja
Indonesia. Tenggat: riset dipercepat sebelum **3 Agustus 2026**.

## LANGKAH 0 — wajib, berurutan, sebelum pekerjaan teknis apa pun

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`. `owner` dan
   `repo` HANYA di dalam `toolArguments`, tidak di tingkat atas.
3. Baca dari `main` repo `EnVyxS/lux-ai-research`, berurutan:
   - `PROMPT_KELANJUTAN.md` (v28, berkas ini)
   - **`STATE.md` (v26) — aturan 1–46, kelas cacat KC-1..KC-17, papan skor,
     daftar utang. INI YANG PALING PENTING.**
   - `journal/2026-07-29-62.md`, `-63.md`, `-64.md`
   - `decisions/ADR-A006.md` dan `ADR-A007.md`
   - `ADR-A004.md` dan `ADR-A002.md` bila menyentuh serapan
   - `PETA_MODUL.md` bila menyentuh modul warisan
4. Baru setelah itu jalankan pekerjaan teknis.

## Batasan yang mahal dipelajari ulang

- Sandbox agen **tidak punya jaringan**. Semua unduhan dan pengukuran arsip
  dijalankan GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- **Tidak ada alat membaca status Actions** dan **tidak ada alat memicu
  `workflow_dispatch`**. Status hanya diketahui dari berkas laporan yang
  di-commit workflow itu sendiri. Satu-satunya cara menyalakan run adalah push
  ke berkas yang tersebut di `paths` workflow.
- **Aturan 45:** push pemicu wajib ATOMIK — modul, workflow, dan uji dalam satu
  commit. Actions memakai workflow pada commit pemicu.
- **Tidak ada API patch.** `push_files` menulis ulang seluruh isi berkas.
  Rancang berkas kecil; setelah mendorong berkas panjang, BACA ULANG dari `main`
  dan pastikan ekornya hadir.
- Saat memeriksa hasil run, cocokkan `run_id` / `sidik_kode` / blob sha. Jangan
  percaya keberadaan berkas — laporan run lama sering masih terbaca.
- Manifes pecahan sangat besar: baca `reports/pecahan_<i>.log`, bukan
  `reports/manifes_pecahan_<i>.json`. Laporan pemulihan
  (`reports/pulihkan_pecahan_<i>.json`) kecil dan aman dibaca utuh.
- `search_code` mengembalikan 0 hasil (tidak berindeks) — pakai
  `get_file_contents`.
- Runner: numpy, pandas, pyarrow, pyyaml, pytest tersedia; TIDAK ada scipy dan
  requests. `data.binance.vision` bisa diakses; `fapi.binance.com` memberi 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. `lux-research` boleh
  DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## Posisi (2026-07-29)

HEAD `fb56f7d8` (STATE v26). **TIDAK ADA RUN YANG SEDANG BERJALAN.**

- Uji **201 TERVERIFIKASI** — run `30404071399`, commit `ab4e0774`, kode 0.
- Serapan semesta: run **`30396803601`**, `versi_pecahan` 6. 787 simbol,
  19.598 simbol-bulan, **839.842.134 baris**, 13.575 menit hilang, 12 karantina,
  parquet 32.706.262.375 B, nisbah 1,2327.
- **Pemulihan di luar runner: LUNAS** — run **`30404071324`**, commit
  `ab4e0774`, `versi_pulihkan` 1. 29/29 aset, 29/29 sha cocok, 0 anggota tak
  aman, 19.598 anggota, 839.842.134 baris terbaca ulang oleh pyarrow.
- **Temuan definisi:** `jumlah_baris` = baris lolos (839.325.999) + baris
  karantina (516.135). ADR-A007 wajib memperhitungkan ini atau semesta
  tercacah ganda.
- Papan skor: TEPAT 100 / MELESET 34 / SEPARUH 5 / TIDAK TERADJUDIKASI 4 /
  MENUNGGU 6 = **149**. Berikutnya **R-150**.

## Pekerjaan berikutnya, menurut urutan utang

1. **Jalur funding** — kini utang tunggal terbesar. `funding_ada` null di
   seluruh manifes; nol kali diuji (ADR-A002 §9).
2. **ADR-A007**: terima atau tolak, lalu implementasikan `sumber_baris`,
   `cacah_baris_dipulihkan`, `cacah_hari_dipulihkan`,
   `cacah_simbol_bulan_dipulihkan`, tripwire `cacah_pemulihan_gagal_checksum`
   = 0. Memulihkan 7.200 menit BNXUSDT. Bahan bakunya sudah tersedia dan
   terbukti dapat diunduh.
3. **Aturan 46 di `pulihkan.py`**: `definisi_jumlah_baris` wajib berbunyi "tidak
   dapat dibedakan" saat tak ada karantina. Gabungkan dengan perubahan lain yang
   memang perlu dijalankan — menaikkan `VERSI` menyalakan delapan runner.
4. `dugaan_pengganti` (ADR-A005); karantina artefak 7 hari.
5. Adjudikasi R-7, R-19, R-20, R-28, R-36, R-37.
6. Belum diukur: sebab KC-15; 15 SETTLED lain; INDEKS 3 nama manual; saham dan
   komoditas token; 16 simbol non-ASCII sisa; `.decode("utf-8","replace")`;
   BUSD/USDC; selisih 38 lawan 41 di diagnosa KC-15; skew `waktu_utc`.
7. Paralel (aturan 3): ADR-A003; juri T4 dengan biaya; lapisan validasi (Šidák,
   ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy murni). **Adjudikasi riset
   TETAP TERKUNCI** sampai lapisan validasi berdiri.

## Kebiasaan yang tidak boleh luntur

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. Sebut sendiri mana yang
  berisiko rendah.
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21).
- Tiap pengukuran sebab wajib memuat medan penggugur (aturan 24); aturan 37
  sampel wajib memuat ≥1 kasus tiap kelas cacat relevan.
- Aturan 20: dilarang menyimpulkan di luar rentang yang disampel. Aturan 30, 41,
  dan **46**: dilarang menyimpulkan dari penyebut nol — termasuk oleh KODE.
- **BACA berkas sebelum menuduhnya salah.** Pola salah-tuduh sudah ENAM kali;
  yang ketujuh nyaris terjadi pada run `30404071324` dan dibatalkan oleh angka.
- Pisahkan fakta dari asumsi; tanpa bukti tulis "Ini memerlukan verifikasi."
- "lanjut" berarti teruskan tanpa konfirmasi.
- Perbarui `STATE.md`, jurnal, dan berkas ini secara berkala. Jangan berhenti
  dengan alasan konteks Notion; patokannya konteks model.

## Penomoran

Jurnal berikutnya **65**. STATE **v26** kini; berikutnya v27. PROMPT **v28**
kini; berikutnya v29. ADR berikutnya **A008** (A003 dicadangkan, A007
DIUSULKAN). Aturan terakhir **46**. Kelas cacat terakhir **KC-17 (DITUTUP)**;
KC-16 kosong selamanya. Ramalan berikutnya **R-150**. Uji **201**.
