# PROMPT KELANJUTAN — v8

Ditulis 2026-07-28. Berkas ini untuk sesi baru atau akun Notion baru: bacalah
ini lebih dulu, lalu `STATE.md`, lalu dua jurnal terakhir. Jangan mengandalkan
ingatan percakapan.

## Posisi sekarang

- Repo tunggal yang boleh ditulis: **`EnVyxS/lux-ai-research`** (publik, cabang
  `main`). `lux-research` dan `lux-scalp-research` boleh DIBACA, tidak boleh
  ditulis, dan HASIL/angkanya tidak boleh masuk ke sini.
- HEAD saat berkas ini ditulis: commit STATE v9 koreksi 1 + PROMPT v8. HEAD
  sebelumnya `5d27ce7c135ea2d668d62f7c7920d5f077601148`.
- Aturan bernomor: **23**. Kelas cacat: **6**. Uji: **53 terverifikasi**
  (CI run 30338089143, `kode_keluar: 0`).
- Penomoran berikutnya: jurnal `journal/2026-07-28-13.md`, STATE v10, PROMPT v9,
  ramalan **R-29**, ADR **A003** (taksonomi) dan **A004** (kebijakan bulan awal),
  hipotesis pertama masih **H-A001** (belum ada). N_percobaan = 0.

## Keadaan pipeline dalam satu paragraf

T0 dan survei arsip selesai. Semesta arsip terukur: 937 simbol, 21.789 berkas
1m, 2020-01 s.d. 2026-06, batas atas 25,86 GB zip / 39,17 GB parquet. Gerbang
integritas resample HIJAU untuk bulan terakhir tiap simbol probe (tiga kali
berturut-turut) tetapi **MERAH untuk bulan awal**: 609 sel OHLC berbeda dari
~905.872 perbandingan pada 24 bulan (KC-6). Karena itu **serapan penuh
TERKUNCI** sampai ADR-A004 memutuskan perlakuan bulan awal, dan aturan 23
melarang melonggarkan gerbang sebelum sebab kegagalannya terukur.

## Tiga langkah berikutnya, berurutan

1. **Ukur sebab KC-6.** Tambahkan pengukuran per-bucket di
   `lux_ai/serapan/uji_resample.py` (atau modul diagnostik terpisah bertanda
   `"bukan_bukti": true` bila ia tidak menyentuh gerbang): untuk tiap bucket yang
   `open`-nya berbeda, catat apakah menit pertama bucket itu ADA di berkas 1m,
   dan cacah celah menit per bulan. Ini mengadjudikasi **R-26** dan **R-27**.
   Uji cara mengukurnya lebih dulu (aturan 12).
2. **Tulis ADR-A004** setelah sebabnya terukur, bukan sebelumnya. Pilihannya
   antara: mengecualikan bulan pertama tiap simbol dari backtest (sejalan dengan
   aturan 17), atau memakai berkas 5m/15m ASLI untuk bulan-bulan itu (melanggar
   ADR-A002 §3, jadi butuh amandemen tertulis). Angka pendukung wajib ada di ADR.
3. **Serapan penuh** 8 pecahan (~2.724 berkas / ~4,9 GB / ~1 jam per pecahan)
   dengan manifes per simbol-bulan: `nama, baris, rentang waktu, checksum,
   sumber, funding_ada, baris_dibuang, berheader, awal_sejati, akhir_sejati,
   satuan stempel`. Ini mengadjudikasi **R-7**, **R-19**, **R-20**. Parquet per
   simbol-bulan sebagai aset rilis; karantina 7 hari.

Paralel yang diizinkan (aturan 3): membangun juri T4 dan lapisan validasi (uji
bulanan berpasangan + Sidak, permutasi ≥300 per TANGGAL UTC, PBO dan DSR numpy
murni) di atas 12 simbol probe. Adjudikasi riset tetap terkunci sampai manifes
semesta terverifikasi.

## Cara kerja yang tidak boleh dilupakan

- Seluruh operasi GitHub lewat
  `connections.mcpServer_github.runTool({toolName, toolArguments})`, dengan
  `owner`/`repo` HANYA di dalam `toolArguments`.
- Sandbox agen TIDAK punya jaringan. Semua pengukuran arsip dijalankan runner;
  agen hanya boleh percaya artefak yang di-commit.
- Tidak ada API patch: setiap penulisan mengganti seluruh isi berkas. Setelah
  mendorong berkas panjang, BACA ULANG dari `main` dan pastikan ekornya hadir.
- Tidak ada alat untuk membaca status GitHub Actions. Status hanya diketahui
  dari `reports/*_status.json` yang di-commit workflow.
- Commit ke `journal/`, `decisions/`, `hipotesis/`, `reports/` sengaja tidak
  memicu CI; berkas `.md` di akar memicu.
- Ramalan ditulis SEBELUM run, di commit yang sama dengan kodenya.
- Setiap angka ringkasan dihitung ulang baris demi baris saat berkas diperbarui
  (aturan 21). Ini sudah tiga kali saya langgar; periksa cacah papan skor tiap
  kali menyentuhnya.

## Berkas yang wajib dibaca di sesi baru

`STATE.md`, `journal/2026-07-28-12.md` (adjudikasi KC-6),
`journal/2026-07-28-11.md` (pra-registrasi R-23..R-25), `decisions/ADR-A001.md`,
`decisions/ADR-A002.md`, `PETA_MODUL.md`.
