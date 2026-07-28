# PROMPT KELANJUTAN — versi 14

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
   - `PROMPT_KELANJUTAN.md` (versi 14) — berkas ini
   - `STATE.md` (versi 15) — aturan 1-29, kelas cacat KC-1..KC-6, papan skor
     R-1..R-43, daftar utang 1-24. INI YANG PALING PENTING.
   - `decisions/ADR-A004.md` dan bagian "Amandemen A-1" di
     `decisions/ADR-A002.md`; `decisions/ADR-A001.md` bila perlu
   - `journal/2026-07-28-20.md` (adjudikasi terakhir); jurnal 16-19 bila perlu
     latar
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
- Laporan besar jangan dibaca utuh. Polanya sudah terbukti: tulis modul kecil
  yang meringkasnya di runner (lihat `penyebut_kc6.py`), lalu baca ringkasannya.
- Runner: numpy, pandas, pyarrow, pyyaml, pytest tersedia; TIDAK ada scipy dan
  requests. `data.binance.vision` bisa diakses; `fapi.binance.com` memberi 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. `lux-research` boleh
  DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## POSISI HARI INI (2026-07-28, akhir sesi 20)

- Kontinuitas: STATE v15 + PROMPT v14. Commit kode terakhir `ac342940`.
- Jumlah uji **90, terverifikasi** (CI run 30342486568, `kode_keluar: 0`).
- KC-6 diputus (ADR-A004), diterapkan dalam kode (`gerbang_1m.py`, enam klausa,
  teruji positif dan negatif), lajunya diketahui (0,3199% bulan awal, 0,0007%
  bulan kendali, dari 931.527 bucket), dan amandemennya sudah tercatat di
  `decisions/ADR-A002.md`.
- Papan skor: 24 TEPAT, 11 MELESET, 1 MELESET SEPARUH, 1 TIDAK TERADJUDIKASI,
  6 MENUNGGU (R-7, R-19, R-20, R-28, R-36, R-37).
- Utang aktif tinggal **19** (`semesta_bulan_1m.json` belum dibaca) dan **24**
  (gerbang belum melihat data sungguhan).

## PEKERJAAN BERIKUTNYA, BERURUTAN

1. **Serapan penuh** per ADR-A002 §9 sebagaimana diamandemen ADR-A004: 8 pecahan
   (~2.724 berkas, ~1,0 jam, ~4,9 GB tiap pecahan), setiap simbol-bulan melewati
   `gerbang_1m.nilai_deret`, manifes per simbol-bulan (nama, baris, rentang
   waktu, checksum, sumber, funding_ada, baris_dibuang, berheader, awal_sejati,
   akhir_sejati, satuan stempel, hasil gerbang), parquet sebagai aset rilis,
   karantina 7 hari. Mengadjudikasi R-7, R-19, R-20, R-36, R-37 dan melunasi
   utang 24. Tulis ramalan SEBELUM run; patuhi aturan 26, 27, dan 28.
2. **Utang 19 sambil menunggu run**: ringkas `reports/semesta_bulan_1m.json` di
   runner, jangan dibaca utuh.
3. **Paralel, boleh sekarang (aturan 3)**: ADR-A003 taksonomi rezim; juri T4
   dengan biaya sejak hari pertama (fee taker/maker terpisah, funding tiap
   jadwal, slippage selalu merugikan); lapisan validasi (uji bulanan berpasangan
   + Sidak, ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy murni).

Adjudikasi riset tetap TERKUNCI sampai manifes semesta penuh terverifikasi.

## PENOMORAN BERIKUTNYA

ADR-A003 (dicadangkan) dan ADR-A005 (bila perlu). Hipotesis pertama H-A001
(belum ada). Jurnal berikutnya `journal/2026-07-28-21.md`. STATE berikutnya v16.
PROMPT berikutnya v15. Ramalan berikutnya R-44. N_percobaan = 0. Aturan terakhir
29. Kelas cacat terakhir KC-6. Utang terakhir 24.

## KEBIASAAN YANG MENYELAMATKAN RISET INI

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. Sudah 11 ramalan MELESET dan
  1 tidak teradjudikasi karena ditulis bersyarat.
- Ramalan mutlak wajib berpasangan dengan ramalan besaran (aturan 26),
  pendampingnya dilarang bersyarat (aturan 27), dan ekstrapolasi dari bulan awal
  wajib dikoreksi untuk bulan parsial (aturan 28).
- Cacah mutlak tanpa penyebut hampir selalu menyesatkan; cari penyebutnya.
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21).
- Setiap pengukuran sebab wajib memuat medan yang bisa MENGGUGURKAN hipotesis
  yang dipercaya (aturan 24); parameter cakupannya dipatok di muka (aturan 25).
- Amandemen ADR ditulis sebagai bagian terpisah, teks lama tidak dihapus
  (aturan 29).
- Bila dua berkas kontinuitas sempat tidak sinkron, catat ketidakcocokannya
  terbuka di jurnal alih-alih membiarkannya diam-diam.
- Pisahkan fakta dari asumsi. Tanpa bukti berkas atau alat, tulis "Ini
  memerlukan verifikasi."
- "lanjut" dari operator berarti teruskan tanpa konfirmasi.
- Bila konteks hampir penuh, HENTIKAN pekerjaan teknis dan perbarui berkas
  kontinuitas dulu.
