# PROMPT KELANJUTAN — versi 9

Ditulis 2026-07-28 15.00 WIB. Menggantikan v8 (blob `3f94b82335dfbad038ae35be79ec9b87b79f6135`).
Tempel SELURUH berkas ini sebagai pesan pertama di sesi atau akun Notion baru.

---

## Kepada asisten yang membaca ini

Kamu melanjutkan riset LUX-AI. Operator: Diva Juan Nur Taqarrub, GitHub `EnVyxS`,
zona waktu Asia/Jakarta, bahasa kerja Indonesia. Jangan mulai bekerja sebelum
menyelesaikan LANGKAH 0 di bawah. Berkas di repo adalah kebenaran; prompt ini
hanya peta menuju berkas itu.

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox (`connections.fs.readFiles`) sebelum memanggil
   fungsi apa pun. Dilarang menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`.
   `owner` dan `repo` HANYA di dalam `toolArguments`, tidak di tingkat atas.
3. Baca dari `main` repo `EnVyxS/lux-ai-research`, berurutan:
   - `STATE.md` (versi 10) — aturan 1-24, kelas cacat KC-1..KC-6, papan skor
     R-1..R-31, daftar utang 1-20. INI YANG PALING PENTING.
   - `decisions/ADR-A001.md` dan `decisions/ADR-A002.md`.
   - `journal/2026-07-28-14.md` — putusan terakhir.
   - `PETA_MODUL.md` bila menyentuh modul warisan.
4. Baru setelah itu jalankan pekerjaan teknis.

## Batasan yang mahal dipelajari ulang

- Sandbox agen TIDAK punya jaringan. Semua unduhan dan pengukuran arsip
  dijalankan GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- Tidak ada alat untuk membaca status GitHub Actions. Status hanya diketahui dari
  berkas laporan yang di-commit workflow itu sendiri.
- Tidak ada API patch. `push_files` menulis ulang seluruh isi berkas. Rancang
  berkas kecil.
- Setelah mendorong berkas panjang, BACA ULANG dari `main` dan pastikan ekornya
  hadir (aturan tak bernomor tapi mengikat).
- Runner: numpy, pandas, pyarrow, pyyaml, pytest tersedia; TIDAK ada scipy dan
  requests. `data.binance.vision` bisa diakses; `fapi.binance.com` memberi 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. `lux-research` boleh
  DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## Posisi hari ini

HEAD `979d0fee3cd8df75a9a2c0ca0f0ec4fcd0573abe` (di atasnya ada pohon laporan
yang di-commit runner). Jumlah uji **61, terverifikasi** lewat CI run 30338666532.

T1 serapan: probe 12 simbol SELESAI (tiga run konsisten: 937 simbol, 21.789
berkas 1m). Survei semesta SELESAI (2020-01..2026-06; 128 terhenti, 809 hidup;
stempel milidetik seragam pada 237 bulan disampel; batas header 2022-01).

Gerbang resample: bulan AKHIR 12/12 bersih. Bulan AWAL **MERAH**, 9 dari 12
simbol gagal. Serapan penuh TERKUNCI sampai ADR-A004 ada (aturan 23).

## KC-6 — apa yang sudah terukur

Berkas 1m dan berkas 5m/15m terbitan Binance tidak sepakat pada bulan awal hidup
simbol. Diagnostik run 30338666516 (`reports/diagnosa_kc6.json`, bertanda
`"bukan_bukti": true`) mengukur 91.335 bucket pada 12 bulan awal:

- 468 bucket ber-`open` beda, 470 bucket ber-OHLC beda.
- **0** di antaranya punya menit pertama yang hilang; `persen_terjelaskan_h1` = 0,0.
- **12 dari 12** bulan awal bersih sempurna: 0 duplikat, 0 menit hilang, 0 jarak
  bukan 60 detik.
- Simbol beda: DOGE 223, BTS 118, FTT 53, XRP 38, SRM 16, LINK 12, ETH 5, BNB 3,
  SOL 2. Bersih: BTC, ADA, COCOS.

**H1 (celah menit) GUGUR.** Arsip 1m utuh; kekurangan data kami bukan sebabnya.
Yang bertahan **H2**: kedua produk dibangun dari agregasi berbeda di sisi Binance.
Sebagian beda ~3% (XRPUSDT 2020-01: `open` 0,1970 lawan 0,2032), jadi kebijakan
berbentuk toleransi TIDAK SAH — ambang yang menampung 3% akan menampung
pergerakan harga sungguhan dan gerbang berhenti mengukur apa pun.

## Pekerjaan berikutnya, berurutan

1. **Ukur SEJAUH MANA KC-6 bertahan** (utang 20). Perluas
   `lux_ai/serapan/diagnosa_kc6.py` ke K bulan pertama tiap simbol ditambah satu
   bulan kendali di tengah hidup simbol. Ini mengadjudikasi R-30 dan R-31.
   Aturan 20 melarang menyimpulkan di luar rentang yang disampel, dan sejauh ini
   HANYA bulan pertama yang disampel.
2. **Tulis ADR-A004** (utang 16) setelah angka nomor 1 ada. Pilihannya:
   mengecualikan bulan awal, mengkarantinanya, atau memakai berkas 5m/15m ASLI
   untuk bulan itu (bertentangan dengan ADR-A002 §3, butuh amandemen tertulis).
   Bukan toleransi.
3. **Serapan penuh** per ADR-A002 §9: 8 pecahan (~2.724 berkas, ~1,0 jam, ~4,9 GB
   tiap pecahan), manifes per simbol-bulan (nama, baris, rentang waktu, checksum,
   sumber, funding_ada, baris_dibuang, berheader, awal_sejati, akhir_sejati,
   satuan stempel), parquet sebagai aset rilis, karantina 7 hari. Mengadjudikasi
   R-7, R-19, R-20.
4. **Paralel, boleh sekarang** (aturan 3 mengizinkan pembangunan juri di atas 12
   simbol probe): ADR-A003 taksonomi rezim; juri T4 dengan biaya sejak hari
   pertama (fee taker/maker terpisah, funding tiap jadwal, slippage selalu
   merugikan); lapisan validasi (uji bulanan berpasangan + Sidak, ≥300 permutasi
   per TANGGAL UTC, PBO dan DSR numpy murni).
5. Utang kecil: baca ulang jurnal 08 dan 09 dari `main` (utang 18); baca
   `reports/semesta_bulan_1m.json` (utang 19).

Adjudikasi riset tetap TERKUNCI sampai manifes semesta penuh terverifikasi.

## Penomoran berikutnya

ADR berikutnya **ADR-A003** (dicadangkan) dan **ADR-A004** (wajib). Hipotesis
pertama **H-A001** (belum ada). Jurnal berikutnya `journal/2026-07-28-15.md`.
STATE berikutnya **v11**. PROMPT berikutnya **v10**. Ramalan berikutnya **R-32**.
N_percobaan = 0. Aturan terakhir **24**. Kelas cacat terakhir **KC-6**.

## Kebiasaan yang menyelamatkan riset ini

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. Sudah 8 ramalan MELESET,
  termasuk beberapa yang paling saya yakini; itu tandanya papan skor bekerja.
- Hitung ulang setiap angka ringkasan baris demi baris saat berkas diperbarui
  (aturan 21 lahir dari tiga kali salah hitung).
- Setiap pengukuran sebab wajib memuat medan yang bisa MENGGUGURKAN hipotesis
  yang sedang dipercaya (aturan 24).
- Pisahkan fakta dari asumsi. Tanpa bukti berkas atau alat, tulis "Ini memerlukan
  verifikasi."
- "lanjut" dari operator berarti teruskan tanpa konfirmasi.
- Perbarui STATE.md, jurnal, dan berkas ini secara berkala. Bila konteks hampir
  penuh, HENTIKAN pekerjaan teknis dan perbarui berkas kontinuitas dulu.
