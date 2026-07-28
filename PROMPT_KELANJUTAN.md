# PROMPT KELANJUTAN — versi 11

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
   - `PROMPT_KELANJUTAN.md` (versi 11) — berkas ini
   - `STATE.md` (versi 12) — aturan 1-26, kelas cacat KC-1..KC-6, papan skor
     R-1..R-37, daftar utang 1-23. INI YANG PALING PENTING.
   - `decisions/ADR-A001.md`, `decisions/ADR-A002.md`, `decisions/ADR-A004.md`
   - `journal/2026-07-28-16.md` — adjudikasi terakhir
   - `PETA_MODUL.md` bila menyentuh modul warisan
4. Baru setelah itu jalankan pekerjaan teknis.

## BATASAN YANG MAHAL DIPELAJARI ULANG

- Sandbox agen TIDAK punya jaringan. Semua unduhan dan pengukuran arsip
  dijalankan GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- Tidak ada alat untuk membaca status GitHub Actions. Status hanya diketahui
  dari berkas laporan yang di-commit workflow itu sendiri
  (`reports/*_status.json`).
- Tidak ada API patch. `push_files` menulis ulang seluruh isi berkas. Rancang
  berkas kecil.
- Setelah mendorong berkas panjang, BACA ULANG dari `main` dan pastikan ekornya
  hadir.
- Laporan besar (mis. `rentang_kc6.json` 177 KB) jangan dibaca utuh; baca
  `reports/<nama>.log` yang memuat ringkasannya, atau baca berkas statusnya.
- Runner: numpy, pandas, pyarrow, pyyaml, pytest tersedia; TIDAK ada scipy dan
  requests. `data.binance.vision` bisa diakses; `fapi.binance.com` memberi 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. `lux-research` boleh
  DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## POSISI HARI INI (2026-07-28, akhir sesi 16)

- HEAD kontinuitas: STATE v12 + PROMPT v11. Commit kode `daed2cf7`
  (`rentang_kc6.py` + workflow + 10 uji); commit putusan `119a4f87`
  (`journal/2026-07-28-16.md`, `decisions/ADR-A004.md`).
- Jumlah uji **71, terverifikasi** (CI run 30340153062, `kode_keluar: 0`).
- T1: probe SELESAI (937 simbol, 21.789 berkas 1m). Survei semesta SELESAI
  (2020-01..2026-06; 128 terhenti, 809 hidup; milidetik seragam; batas header
  2022-01).
- **KC-6 sudah diputus.** ADR-A004 DITERIMA: berkas 1m satu-satunya sumber
  kebenaran; seluruh kerangka waktu lebih besar diturunkan dengan resample;
  berkas 5m/15m terbitan Binance TIDAK diserap; gerbang mengikat berpindah ke
  **integritas struktural deret 1m** (0 duplikat, 0 menit hilang, jarak 60 detik,
  stempel selaras menit, milidetik); perbandingan dengan 5m/15m tinggal
  diagnostik. ADR-A002 §3 diamandemen.
- Angka yang mendasarinya (run 30339979270, 84 simbol-bulan): 2.530 bucket beda
  di bulan awal, **1** di seluruh bulan kendali (LINKUSDT 2023-04),
  `menit_hilang_total` = 0, `duplikat_total` = 0, DOGE masih 202 dan BTS masih 8
  di bulan ke-6.
- Papan skor: 20 TEPAT, 10 MELESET, 1 MELESET SEPARUH, 6 MENUNGGU (R-7, R-19,
  R-20, R-28, R-36, R-37). R-30 dan R-31 baru saja meleset — keduanya keyakinan
  yang saya bawa masuk, dan keduanya digugurkan oleh medan yang saya pasang
  sendiri untuk menggugurkannya.

## PEKERJAAN BERIKUTNYA, BERURUTAN

1. **Utang 23 — gerbang integritas 1m dalam kode.** Modul baru (mis.
   `lux_ai/serapan/gerbang_1m.py`) yang menerapkan ADR-A004 §2 per simbol-bulan,
   plus uji dengan kasus positif DAN negatif (aturan 12 berlaku untuk cara
   mengukurnya). Serapan penuh tidak boleh jalan sebelum ini ada.
2. **Serapan penuh** per ADR-A002 §9 sebagaimana diamandemen: 8 pecahan (~2.724
   berkas, ~1,0 jam, ~4,9 GB tiap pecahan), manifes per simbol-bulan (nama,
   baris, rentang waktu, checksum, sumber, funding_ada, baris_dibuang,
   berheader, awal_sejati, akhir_sejati, satuan stempel, plus hasil gerbang
   integritas), parquet sebagai aset rilis, karantina 7 hari. Mengadjudikasi
   R-7, R-19, R-20, R-36, R-37.
3. **Utang 21 dan 22** (murah, kerjakan sambil menunggu run): baca medan
   `pengukuran` `rentang_kc6.json` untuk mendapat penyebutnya; beri catatan
   silang amandemen di `decisions/ADR-A002.md`.
4. **Paralel, boleh sekarang (aturan 3)**: ADR-A003 taksonomi rezim; juri T4
   dengan biaya sejak hari pertama (fee taker/maker terpisah, funding tiap
   jadwal, slippage selalu merugikan); lapisan validasi (uji bulanan berpasangan
   + Sidak, ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy murni).
5. Utang kecil: baca `reports/semesta_bulan_1m.json` (utang 19).

Adjudikasi riset tetap TERKUNCI sampai manifes semesta penuh terverifikasi.

## PENOMORAN BERIKUTNYA

ADR-A003 (dicadangkan) dan ADR-A005 (bila perlu). Hipotesis pertama H-A001
(belum ada). Jurnal berikutnya `journal/2026-07-28-17.md`. STATE berikutnya v13.
PROMPT berikutnya v12. Ramalan berikutnya R-38. N_percobaan = 0. Aturan terakhir
26. Kelas cacat terakhir KC-6. Utang terakhir 23.

## KEBIASAAN YANG MENYELAMATKAN RISET INI

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. Sudah 10 ramalan MELESET.
- Ramalan mutlak wajib berpasangan dengan ramalan besaran (aturan 26).
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21).
- Setiap pengukuran sebab wajib memuat medan yang bisa MENGGUGURKAN hipotesis
  yang dipercaya (aturan 24); parameter cakupannya dipatok di muka (aturan 25).
- Pisahkan fakta dari asumsi. Tanpa bukti berkas atau alat, tulis "Ini
  memerlukan verifikasi."
- "lanjut" dari operator berarti teruskan tanpa konfirmasi.
- Bila konteks hampir penuh, HENTIKAN pekerjaan teknis dan perbarui berkas
  kontinuitas dulu.
