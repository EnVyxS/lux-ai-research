# PROMPT KELANJUTAN — v3

Ditulis 2026-07-28. Repo: `EnVyxS/lux-ai-research` (PUBLIK).
Bila kamu sesi baru: yang tercommit itu nyata, sisanya tidak ada.

## 1. Urutan baca yang mengikat

1. Berkas ini, utuh.
2. `decisions/ADR-A002.md` (ADR terbaru), lalu `decisions/ADR-A001.md`.
3. `STATE.md`.
4. `STATE_LAMPIRAN.md`, lalu `STATE_LAMPIRAN_ANGKA.md`.
5. Dua jurnal terakhir: `journal/2026-07-28-02.md`, `journal/2026-07-28-01.md`.
   Jangan pernah membaca seluruh direktori `journal/`.
6. `PETA_MODUL.md` bila pekerjaanmu menyentuh modul warisan.

Dilarang memulai riset sebelum keenamnya dibaca.

## 2. Larangan

- Jangan menulis apa pun ke `lux-research` atau `lux-scalp-research`. Membaca
  boleh atas izin operator; mengutip HASIL, angka, atau putusan dari sana
  sebagai bukti tidak pernah boleh.
- Jangan memakai `backtest.py` modul warisan sebagai juri.
- Jangan memakai angka modul warisan sebagai bukti; itu klaim yang harus diuji.
- Jangan menyentuh bursa. Hanya arsip publik.
- Jangan mengadjudikasi hipotesis sebelum semesta penuh masuk dan manifesnya
  terverifikasi.
- Jangan mengubah ambang setelah melihat hasil.
- Jangan menulis guard berbasis pencarian kata atas kode atau berkas workflow
  (KC-3).
- Jangan menulis uji yang menyentuh jaringan (aturan 14).
- Jangan menulis angka arsip di dokumen mana pun sebelum artefaknya ada
  (aturan 13).

## 3. Ambang yang sudah dibekukan

- Ekspektasi bersih ≥ 0,05R setelah biaya. Minimal 100 transaksi per sel.
- p ≤ 0,05 uji bulanan berpasangan + koreksi Sidak:
  `alpha_sidak = 1 - (1 - 0,05)^(1/N_percobaan)`.
- Permutasi ≥ 300 ulangan, diacak PER TANGGAL UTC.
- PBO < 0,50 dan DSR > 0,95. Tidak ada rugi melampaui -1,5R.
- Butir rezim DITANGGUHKAN sampai ADR-A003 dan penangguhan wajib disebut.
- N_percobaan berjalan: **0**.
- Karantina listing: **N = 7 hari** (ADR-A002 §4). Dipatok, tidak boleh disetel
  setelah melihat hasil.

## 4. Sari batas alat (§0A), plus yang terbukti di repo ini

- Semua operasi GitHub lewat `runTool({toolName, toolArguments})`. `owner` dan
  `repo` HANYA boleh ada di dalam `toolArguments`; menaruhnya di tingkat atas
  ditolak. Ini kesalahan nyata yang pernah terjadi 2026-07-28.
- TIDAK ADA alat untuk Actions. Status run hanya diketahui dari artefak yang
  di-commit workflow. Pola laporan-sebelum-exit TERBUKTI bekerja di repo ini.
- `push_files` untuk banyak berkas satu commit. Tidak ada API patch.
- Setelah mendorong berkas panjang, baca ulang dari `main` dan pastikan EKORNYA
  hadir. Ukuran bukan bukti isi.
- `cache: 'pip'` butuh `requirements.txt` di akar. Sudah ada.
- Cacah uji dicetak sebelum pytest; laporan di-commit sebelum `exit 1`.
- Sandbox agen TIDAK punya jaringan. Semua unduhan lewat runner.
- Runner: 4 vCPU, ~15 GB RAM, ~14 GB disk bebas, 6 jam per job. Tanpa scipy,
  tanpa requests. Statistik harus numpy murni.
- `data.binance.vision` bisa dari runner; `fapi.binance.com` 451.

## 5. Posisi sekarang, satu paragraf

Tugas 0 dan 1 selesai dan terverifikasi. Peta modul lengkap; temuan warisan A-P
sudah dinilai satu per satu (A dan B belum bisa diperiksa, G sebagian, O
dikoreksi). ADR-A001 mematok aturan dasar; ADR-A002 mematok serapan tetapi
bagian estimasi ukurannya sengaja kosong. Workflow `probe-serapan` sudah
diluncurkan pada commit 55837ea untuk mengukur 12 simbol probe dan mencacah
seluruh indeks arsip; hasilnya belum terlihat saat berkas ini ditulis. CI hijau
dengan 15 uji. Belum ada satu pun angka strategi, belum ada juri, belum ada
baseline B0, N_percobaan masih 0.

## 6. Daftar tugas berprioritas

1. Baca `reports/probe_status.json` dan `reports/probe_serapan.json`. Bila belum
   ada, baca `reports/probe_serapan_progres.json` untuk tahu tahap terakhir.
   Bila run gagal, `reports/probe_serapan.log` memuat 20 KB terakhir.
2. Nilai ramalan R-1 sampai R-5 di `STATE.md` secara jujur, termasuk yang
   meleset, lalu isi ADR-A002 bagian 7 dengan angka dari artefak.
3. Bangun uji integritas resample: 1m → 5m dan 15m dibandingkan berkas ASLI
   untuk 12 simbol probe, pada open/high/low/close/volume. Ketidakcocokan
   menghentikan pipeline.
4. Bangun matriks serapan penuh sebagai workflow latar + manifes (nama, baris,
   rentang waktu, checksum, sumber). Parquet per simbol-bulan sebagai aset rilis.
5. Paralel, di atas 12 simbol probe: ADR-A003 (taksonomi rezim, likuiditas,
   sesi, struktur, funding; label point-in-time), lalu juri T4, lalu validasi.
6. DSR dan PBO: operator sudah mengizinkan pembacaan `lux-research`. Bila kode
   `lux/validasi/dsr.py` dan `lux/validasi/pbo.py` disalin, salin apa adanya dan
   catat asalnya beserta blob sha (tercatat di `journal/2026-07-28-02.md`).
7. Baru setelah semesta penuh: Baseline B0 + BUKU PENYIMPANGAN + pra-registrasi.

## 7. Penomoran berikutnya

- ADR bebas berikutnya: **ADR-A003**.
- Jurnal berikutnya: **`journal/2026-07-28-03.md`**.
- Hipotesis pertama masih **H-A001** (belum terpakai).

## 8. HEAD saat penyerahan

- `55837eac88bf293933f61c91ec5ab2a54695882d` — Tugas 2 langkah 1.
- `5984212f3a80a3f107163ee0c87d1ebdf8fc831c` — laporan CI run 30312616139,
  `kode_keluar: 0`, 15 uji.
- Sebelumnya: `adec1485759a7334077ad24a31a922f5d94e8fe0` (perbaikan guard),
  `364e578cff911dc8a772051dd30b88da5e3a3b02` (isi pertama).

## 9. Berkas inti — byte dan blob sha pada commit 5984212

| Berkas | Byte | Blob sha |
|---|---|---|
| `README.md` | 1.910 | `d875f3643e274bf6e7b47b84ccfcd8ada016c554` |
| `requirements.txt` | 71 | `b3749ba54f8b27bd9f8bc002f38c11d33f4c1a07` |
| `STATE.md` (v2) | 4.093 | `623b3fdf975dd872f6f6cf29a1e3a2a9895bf01b` |
| `STATE_LAMPIRAN.md` | 2.350 | `f2b907648bb291d5a4e44e5683270d84cf981a6a` |
| `STATE_LAMPIRAN_ANGKA.md` | 1.841 | `f3ebdb02f4e03fea6e45a2fba107a50f69ace7c6` |
| `PROMPT_KELANJUTAN.md` (v2) | 5.923 | `d62067d6ef7e039dac48d7a70c63e4fdcd9ea18d` |
| `PETA_MODUL.md` | 8.691 | `9ee33a991b2ec28405a00550c65f30e419f823cc` |
| `PETA_MODUL_BERKAS.md` | 6.890 | `3abe95f6fdac76fc87259f91b638b0903d67048e` |
| `decisions/ADR-A001.md` | 3.569 | `d5bb2f64862b0e2f4b49a3591b3b65e662469e2f` |
| `decisions/ADR-A002.md` | 3.767 | `3104f949e4c9558a3ca402699396a1c84120670d` |
| `journal/2026-07-28-01.md` | 2.618 | `fc13dc310a3c3eff22df3849799d695f6a8cf3a8` |
| `journal/2026-07-28-02.md` | 1.852 | `44d02d441635345328d81f39d8f017bcdceda3af` |

Baris `STATE.md` dan `PROMPT_KELANJUTAN.md` di tabel ini adalah versi SEBELUM
commit yang membawa v3; perbarui keduanya di pembaruan berikutnya.

## 10. Kode serapan yang sudah ada

| Berkas | Byte | Blob sha | Isi |
|---|---|---|---|
| `lux_ai/serapan/arsip.py` | 5.231 | `0104958bd99772cda8262d5527da52aea9635724` | listing S3, URL, checksum, unduh terverifikasi |
| `lux_ai/serapan/klines.py` | 2.696 | `c308b9676fdb1fe78b1a9d4c7304253975109409` | baca zip, deteksi header, rapikan, parquet zstd |
| `lux_ai/serapan/probe.py` | 6.594 | `df0a2d5da219b953f307e5034f00a7a9ef7495d9` | pengukuran 12 probe + cacah semesta |

Workflow: `.github/workflows/ci.yml` (uji) dan
`.github/workflows/probe_serapan.yml` (probe; terpicu oleh perubahan di
`lux_ai/serapan/**`, menulis progres tiap 10 menit).
