# PROMPT KELANJUTAN — versi 10

Salin isi berkas ini sebagai prompt pembuka sesi berikutnya.

---

Kamu melanjutkan riset LUX-AI. Operator: Diva Juan Nur Taqarrub, GitHub EnVyxS,
zona waktu Asia/Jakarta, bahasa kerja Indonesia. Jangan mulai bekerja sebelum
menyelesaikan LANGKAH 0. Berkas di repo adalah kebenaran; prompt ini hanya peta.

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`. `owner` dan
   `repo` HANYA di dalam `toolArguments`, tidak di tingkat atas.
3. Baca dari `main` repo `EnVyxS/lux-ai-research`, berurutan:
   - `PROMPT_KELANJUTAN.md` (versi 10) — berkas ini
   - `STATE.md` (versi 11) — aturan 1-25, kelas cacat KC-1..KC-6, papan skor
     R-1..R-35, daftar utang 1-20. INI YANG PALING PENTING.
   - `decisions/ADR-A001.md` dan `decisions/ADR-A002.md`
   - `journal/2026-07-28-15.md` — pra-registrasi terakhir; lalu `-14.md` bila
     perlu latar KC-6
   - `PETA_MODUL.md` bila menyentuh modul warisan
4. Baru setelah itu jalankan pekerjaan teknis.

## BATASAN YANG MAHAL DIPELAJARI ULANG

- Sandbox agen TIDAK punya jaringan. Semua unduhan dan pengukuran arsip
  dijalankan GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- Tidak ada alat untuk membaca status GitHub Actions. Status hanya diketahui
  dari berkas laporan yang di-commit workflow itu sendiri.
- Tidak ada API patch. `push_files` menulis ulang seluruh isi berkas. Rancang
  berkas kecil.
- Setelah mendorong berkas panjang, BACA ULANG dari `main` dan pastikan ekornya
  hadir.
- Runner: numpy, pandas, pyarrow, pyyaml, pytest tersedia; TIDAK ada scipy dan
  requests. `data.binance.vision` bisa diakses; `fapi.binance.com` memberi 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. `lux-research` boleh
  DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## POSISI HARI INI (2026-07-28, sesi 15)

- HEAD kontinuitas: STATE v11 + PROMPT v10. Commit kode terakhir `daed2cf7`
  (`rentang_kc6.py`, workflow `rentang-kc6`, `tests/test_rentang_kc6.py`);
  commit pra-registrasi `219756d9` (`journal/2026-07-28-15.md`).
- Jumlah uji: **71, KLAIM**. Yang terverifikasi masih 61 (CI run 30338666532).
  Angka 71 baru sah setelah `reports/ci_terakhir.json` berikutnya dibaca.
- T1 serapan: probe 12 simbol SELESAI (937 simbol, 21.789 berkas 1m). Survei
  semesta SELESAI (2020-01..2026-06; 128 terhenti, 809 hidup; milidetik seragam
  pada 237 bulan; batas header 2022-01).
- Gerbang resample: bulan AKHIR 12/12 bersih; bulan AWAL MERAH, 9 dari 12 gagal.
  Serapan penuh TERKUNCI sampai ADR-A004 (aturan 23).

## KC-6 — apa yang sudah terukur

Run 30338666516, `reports/diagnosa_kc6.json` (`"bukan_bukti": true`), 91.335
bucket pada 12 bulan AWAL: 468 bucket `open` beda, 470 OHLC beda, 0 di antaranya
punya menit pertama hilang, `persen_terjelaskan_h1` = 0,0, dan 12/12 bulan awal
bersih sempurna. Simbol beda: DOGE 223, BTS 118, FTT 53, XRP 38, SRM 16, LINK
12, ETH 5, BNB 3, SOL 2. Bersih: BTC, ADA, COCOS. **H1 (celah menit) GUGUR**;
H2 (agregasi berbeda di sisi Binance) bertahan. Beda mencapai ~3% (XRPUSDT
2020-01: 0,1970 lawan 0,2032) → kebijakan berbentuk toleransi TIDAK SAH.

## YANG SEDANG BERJALAN — baca ini lebih dulu

Workflow `rentang-kc6` didorong pada commit `daed2cf7` dan mengukur K = 6 bulan
awal tiap simbol probe ditambah satu bulan KENDALI di tengah hidup simbol
(≈ 12 × 7 × 3 unduhan). K dan cara memilih bulan kendali sudah dipatok di muka
(aturan 25 baru).

Langkah pertama sesi berikutnya:

1. Baca `reports/rentang_kc6_status.json` (`run_id`, `kode_keluar`) dan
   `reports/rentang_kc6.json` dari `main`. Bila belum ada, run belum selesai
   atau gagal sebelum sempat menulis — periksa juga
   `reports/rentang_kc6_progres.json` dan `reports/rentang_kc6.log`.
2. Adjudikasi JUJUR R-30, R-31, R-32, R-33, R-34, R-35 dari medan
   `ringkas`: `total_bucket_beda_awal`, `total_bucket_beda_kendali`,
   `persen_kendali_atas_awal`, `menit_hilang_total`, `duplikat_total`,
   `simbol_kendali_beda`, `simbol_masih_beda_di_bulan_terakhir_awal`,
   `simbol_reda_di_dalam_k`, `simbol_menurun`.
   - `menit_hilang_total` atau `duplikat_total` positif = H1 HIDUP KEMBALI dan
     jurnal 14 harus dibaca ulang (aturan 24).
   - `simbol_kendali_beda` tidak kosong = gejala TIDAK terbatas pada bulan awal,
     dan ADR-A004 tidak boleh berbentuk "buang N bulan pertama".
3. Hitung ulang papan skor baris demi baris (aturan 21) dan baca
   `reports/ci_terakhir.json` untuk mengganti jumlah uji KLAIM menjadi
   terverifikasi.

## PEKERJAAN BERIKUTNYA, BERURUTAN

1. Adjudikasi R-30..R-35 seperti di atas; lunasi utang 20.
2. Tulis `decisions/ADR-A004.md` (utang 16) setelah angka nomor 1 ada. Pilihan:
   mengecualikan bulan awal, mengkarantinanya, atau memakai berkas 5m/15m ASLI
   untuk bulan itu (bertentangan ADR-A002 §3, butuh amandemen tertulis). Bukan
   toleransi. Jumlah bulan yang dikecualikan wajib berasal dari angka terukur,
   bukan dari angka bulat yang enak dipandang.
3. Serapan penuh per ADR-A002 §9: 8 pecahan (~2.724 berkas, ~1,0 jam, ~4,9 GB
   tiap pecahan), manifes per simbol-bulan (nama, baris, rentang waktu,
   checksum, sumber, funding_ada, baris_dibuang, berheader, awal_sejati,
   akhir_sejati, satuan stempel), parquet sebagai aset rilis, karantina 7 hari.
   Mengadjudikasi R-7, R-19, R-20.
4. Paralel, boleh sekarang (aturan 3): ADR-A003 taksonomi rezim; juri T4 dengan
   biaya sejak hari pertama (fee taker/maker terpisah, funding tiap jadwal,
   slippage selalu merugikan); lapisan validasi (uji bulanan berpasangan +
   Sidak, ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy murni).
5. Utang kecil: baca ulang jurnal 08 dan 09 dari `main` (utang 18); baca
   `reports/semesta_bulan_1m.json` (utang 19).

Adjudikasi riset tetap TERKUNCI sampai manifes semesta penuh terverifikasi.

## PENOMORAN BERIKUTNYA

ADR-A003 (dicadangkan) dan ADR-A004 (wajib). Hipotesis pertama H-A001 (belum
ada). Jurnal berikutnya `journal/2026-07-28-16.md`. STATE berikutnya v12. PROMPT
berikutnya v11. Ramalan berikutnya R-36. N_percobaan = 0. Aturan terakhir 25.
Kelas cacat terakhir KC-6.

## KEBIASAAN YANG MENYELAMATKAN RISET INI

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. Sudah 8 ramalan MELESET,
  termasuk beberapa yang paling diyakini; itu tandanya papan skor bekerja.
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21).
- Setiap pengukuran sebab wajib memuat medan yang bisa MENGGUGURKAN hipotesis
  yang sedang dipercaya (aturan 24), dan parameter cakupannya dipatok di muka
  (aturan 25).
- Pisahkan fakta dari asumsi. Tanpa bukti berkas atau alat, tulis "Ini
  memerlukan verifikasi."
- "lanjut" dari operator berarti teruskan tanpa konfirmasi.
- Perbarui `STATE.md`, jurnal, dan `PROMPT_KELANJUTAN.md` secara berkala. Bila
  konteks hampir penuh, HENTIKAN pekerjaan teknis dan perbarui berkas
  kontinuitas dulu.
