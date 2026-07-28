# PROMPT KELANJUTAN — v21

Kamu melanjutkan riset LUX-AI. Operator: Diva Juan Nur Taqarrub, GitHub EnVyxS,
zona waktu Asia/Jakarta, bahasa kerja Indonesia. Jangan mulai bekerja sebelum
menyelesaikan LANGKAH 0. Berkas di repo adalah kebenaran; prompt ini hanya peta.

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat `connections.mcpServer_github.runTool({toolName,
   toolArguments})`. `owner` dan `repo` HANYA di dalam `toolArguments`.
3. Baca dari main repo `EnVyxS/lux-ai-research`, berurutan: `PROMPT_KELANJUTAN.md`
   (v21); `STATE.md` (v20) — aturan 1-37, KC-1..KC-13, papan skor R-1..R-99,
   utang 1-28, INI YANG PALING PENTING; `decisions/ADR-A001.md`, `ADR-A002.md`
   (beserta Amandemen A-1), `ADR-A004.md`, `ADR-A005.md`;
   `journal/2026-07-28-45.md`; `PETA_MODUL.md` bila menyentuh modul warisan.
4. Baru setelah itu jalankan pekerjaan teknis.

## BATASAN YANG MAHAL DIPELAJARI ULANG

- Sandbox agen TIDAK punya jaringan. Semua unduhan dan pengukuran arsip
  dijalankan GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- Tidak ada alat membaca status GitHub Actions. Status hanya diketahui dari
  berkas laporan yang di-commit workflow itu sendiri.
- Tidak ada API patch. `push_files` menulis ulang seluruh isi berkas. Rancang
  berkas kecil. Setelah mendorong berkas panjang, BACA ULANG dari main dan
  pastikan ekornya hadir.
- Runner: numpy, pandas, pyarrow, pyyaml, pytest tersedia; TIDAK ada scipy dan
  requests. data.binance.vision bisa diakses; fapi.binance.com memberi 451.
- Dilarang menulis apa pun di luar repo lux-ai-research. lux-research boleh
  DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.
- **Pemicu-diri workflow sudah dicabut**: menyunting sebuah `.yml` tidak lagi
  menyalakan run-nya. Untuk menjalankan ulang, pakai `workflow_dispatch`.
  Konsekuensinya salah ketik yml tidak ketahuan otomatis.

## POSISI HARI INI (2026-07-28, sesi 45)

HEAD pekerjaan teknis: jurnal 45 (`322dc256…`) di atas pilot v2 (`ddc47411…`).
Uji 115 terverifikasi; ±123 menunggu laporan CI. Papan skor R-1..R-99: TEPAT 61,
MELESET 25, SEPARUH 4, TIDAK TERADJUDIKASI 3, MENUNGGU 6. Ramalan berikutnya
**R-100**. Aturan terakhir **37**. KC terakhir **KC-13**. ADR berikutnya **A006**
(A003 tetap dicadangkan). Jurnal berikutnya `journal/2026-07-28-46.md`. STATE
berikutnya v21, PROMPT berikutnya v22. N_percobaan = 0.

Semesta: 937 simbol / 21.789 bulan 1m / 2020-01..2026-06. Tahap pertama per
ADR-A005 hanya `perpetual_usdt`: **787 simbol / 19.598 bulan**. Terhenti 129
(ambang ≤2026-05) lawan 128 (≤2026-04); selisihnya SXPUSDT, sudah dinamai.

Jalur serapan sudah terbukti ujung ke ujung pada lima kelas risiko (pra-header,
non-ASCII, terhenti, bulan awal, kendali baru): 5/5 lolos gerbang, 96.375 baris,
0 baris dibuang, nisbah parquet/zip 1,2299.

## PEKERJAAN BERIKUTNYA, BERURUTAN

1. **Utang 24, sisa skala.** Perluas `lux_ai/serapan/serap.py` menjadi serapan
   berpecahan atas 787 simbol perpetual_usdt: indeks pecahan lewat
   `workflow_dispatch`, manifes per pecahan, parquet sebagai artefak/aset rilis
   (JANGAN masuk repo), karantina 7 hari. Pra-registrasi dulu, jangan lupa
   medan penggugur.
2. **Jalur funding** — nol kali diuji. `funding_ada` masih null. ADR-A002 §9
   mewajibkannya di manifes.
3. **Medan `dugaan_pengganti`** (ADR-A005) belum ada di manifes.
4. Paralel, boleh sekarang (aturan 3): ADR-A003 taksonomi rezim; juri T4 dengan
   biaya sejak hari pertama; lapisan validasi (uji bulanan berpasangan + Sidak,
   ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy murni).
5. Belum diukur: 15 SETTLED lain; kelengkapan daftar INDEKS; pemisahan saham
   dan komoditas token dari 787 perpetual_usdt; `.decode("utf-8","replace")`;
   apakah BUSD/USDC layak digabung dengan USDT.

Adjudikasi riset tetap TERKUNCI sampai manifes semesta penuh terverifikasi
(aturan 3).

## KEBIASAAN

Tulis ramalan SEBELUM run lalu adjudikasi jujur. Hitung ulang setiap angka
ringkasan baris demi baris (aturan 21). Setiap pengukuran sebab wajib memuat
medan yang bisa MENGGUGURKAN hipotesis yang dipercaya (aturan 24). Sampel wajib
menyentuh tiap kelas risiko dan menyebut yang kosong (aturan 37). Pisahkan
fakta dari asumsi; tanpa bukti tulis "Ini memerlukan verifikasi." Jangan meramal
isi berkas dari ingatan — tujuh kali pola itu menjerumuskan; baca berkasnya
lebih dulu. "lanjut" berarti teruskan tanpa konfirmasi. Perbarui STATE.md,
jurnal, dan PROMPT_KELANJUTAN.md secara berkala; berkas kontinuitas sudah empat
kali tertinggal di belakang jurnal, jangan biarkan terulang.
