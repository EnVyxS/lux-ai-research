# PROMPT KELANJUTAN — versi 12

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
   - `PROMPT_KELANJUTAN.md` (versi 12) — berkas ini
   - `STATE.md` (versi 13) — aturan 1-27, kelas cacat KC-1..KC-6, papan skor
     R-1..R-40, daftar utang 1-24. INI YANG PALING PENTING.
   - `decisions/ADR-A001.md`, `decisions/ADR-A002.md`, `decisions/ADR-A004.md`
   - `journal/2026-07-28-17.md` dan `journal/2026-07-28-18.md`
   - `lux_ai/serapan/gerbang_1m.py` sebelum menyentuh serapan
   - `PETA_MODUL.md` bila menyentuh modul warisan
4. Baru setelah itu jalankan pekerjaan teknis.

## BATASAN YANG MAHAL DIPELAJARI ULANG

- Sandbox agen TIDAK punya jaringan. Semua unduhan dan pengukuran arsip
  dijalankan GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- Tidak ada alat untuk membaca status GitHub Actions. Status hanya diketahui
  dari berkas laporan yang di-commit workflow itu sendiri
  (`reports/*_status.json`, `reports/ci_terakhir.json`).
- Tidak ada API patch. `push_files` menulis ulang seluruh isi berkas. Rancang
  berkas kecil.
- Setelah mendorong berkas panjang, BACA ULANG dari `main` dan pastikan ekornya
  hadir.
- Laporan besar (mis. `rentang_kc6.json` 177 KB) jangan dibaca utuh; baca
  `reports/<nama>.log` atau berkas statusnya.
- Runner: numpy, pandas, pyarrow, pyyaml, pytest tersedia; TIDAK ada scipy dan
  requests. `data.binance.vision` bisa diakses; `fapi.binance.com` memberi 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. `lux-research` boleh
  DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## POSISI HARI INI (2026-07-28, akhir sesi 18)

- Kontinuitas: STATE v13 + PROMPT v12. Commit terakhir kode `5e24f6b0`
  (`gerbang_1m.py` + 16 uji + jurnal 17).
- Jumlah uji **87, terverifikasi** (CI run 30341471061, `kode_keluar: 0`).
- KC-6 sudah diputus (ADR-A004) DAN penerapannya sudah ada dalam kode:
  `lux_ai/serapan/gerbang_1m.py`, enam klausa, teruji positif dan negatif.
- Papan skor: 22 TEPAT, 10 MELESET, 1 MELESET SEPARUH, 1 TIDAK TERADJUDIKASI,
  6 MENUNGGU (R-7, R-19, R-20, R-28, R-36, R-37).
- Yang BELUM: gerbang itu belum pernah melihat data arsip sungguhan (utang 24).

## PEKERJAAN BERIKUTNYA, BERURUTAN

1. **Serapan penuh** per ADR-A002 §9 sebagaimana diamandemen ADR-A004: 8 pecahan
   (~2.724 berkas, ~1,0 jam, ~4,9 GB tiap pecahan), setiap simbol-bulan melewati
   `gerbang_1m.nilai_deret`, manifes per simbol-bulan (nama, baris, rentang
   waktu, checksum, sumber, funding_ada, baris_dibuang, berheader, awal_sejati,
   akhir_sejati, satuan stempel, hasil gerbang), parquet sebagai aset rilis,
   karantina 7 hari. Mengadjudikasi R-7, R-19, R-20, R-36, R-37 dan melunasi
   utang 24. Tulis ramalannya SEBELUM run, dan patuhi aturan 26 dan 27.
2. **Utang murah sambil menunggu run**: utang 21 (penyebut `rentang_kc6.json`),
   utang 22 (catatan silang di `ADR-A002.md`), utang 19
   (`reports/semesta_bulan_1m.json`).
3. **Paralel, boleh sekarang (aturan 3)**: ADR-A003 taksonomi rezim; juri T4
   dengan biaya sejak hari pertama (fee taker/maker terpisah, funding tiap
   jadwal, slippage selalu merugikan); lapisan validasi (uji bulanan berpasangan
   + Sidak, ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy murni).

Adjudikasi riset tetap TERKUNCI sampai manifes semesta penuh terverifikasi.

## PENOMORAN BERIKUTNYA

ADR-A003 (dicadangkan) dan ADR-A005 (bila perlu). Hipotesis pertama H-A001
(belum ada). Jurnal berikutnya `journal/2026-07-28-19.md`. STATE berikutnya v14.
PROMPT berikutnya v13. Ramalan berikutnya R-41. N_percobaan = 0. Aturan terakhir
27. Kelas cacat terakhir KC-6. Utang terakhir 24.

## KEBIASAAN YANG MENYELAMATKAN RISET INI

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. Sudah 10 ramalan MELESET dan
  1 tidak teradjudikasi karena ditulis bersyarat.
- Ramalan mutlak wajib berpasangan dengan ramalan besaran (aturan 26), dan
  pendampingnya dilarang bersyarat (aturan 27).
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21).
- Setiap pengukuran sebab wajib memuat medan yang bisa MENGGUGURKAN hipotesis
  yang dipercaya (aturan 24); parameter cakupannya dipatok di muka (aturan 25).
- Pisahkan fakta dari asumsi. Tanpa bukti berkas atau alat, tulis "Ini
  memerlukan verifikasi."
- "lanjut" dari operator berarti teruskan tanpa konfirmasi.
- Bila konteks hampir penuh, HENTIKAN pekerjaan teknis dan perbarui berkas
  kontinuitas dulu.
