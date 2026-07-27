# PROMPT KELANJUTAN — v2

Ditulis 2026-07-28. Bahasa kerja: Indonesia. Menggantikan v1.

## Urutan baca yang mengikat untuk sesi berikutnya

1. Berkas ini, utuh.
2. ADR terbaru di `decisions/` (sekarang: ADR-A001).
3. `STATE.md`.
4. `STATE_LAMPIRAN.md`, lalu `STATE_LAMPIRAN_ANGKA.md`.
5. Dua jurnal terakhir di `journal/`. JANGAN membaca seluruh direktori.
6. `PETA_MODUL.md` bila pekerjaanmu menyentuh modul warisan.

Apa pun yang tidak tercatat di berkas-berkas itu dianggap BELUM DIKETAHUI.
Jangan merekonstruksinya dari ingatan.

## Larangan

- Jangan menjalankan hipotesis tanpa pra-registrasi tertulis lebih dulu.
- Jangan mengubah ambang setelah melihat hasil.
- Jangan menambah percobaan tanpa membayarnya di N_percobaan.
- Jangan menyentuh `lux-research` maupun `lux-scalp-research`.
- Jangan menyentuh bursa. Nol koneksi.
- Jangan mengadjudikasi sebelum semesta data lengkap dan manifes terverifikasi.
- Jangan memakai `backtest.py` modul warisan.
- Jangan memakai angka dari modul warisan sebagai bukti.
- Jangan menulis guard berbasis pencarian kata atas kode atau berkas workflow.
  Lihat KC-3 di `STATE.md`: guard semacam itu sudah sekali menjatuhkan CI di
  repo ini.

## Ambang yang sudah dibekukan

Ekspektasi bersih >= 0,05R; >= 100 transaksi per sel; p <= 0,05 dengan koreksi
Sidak; permutasi >= 300 ulangan per TANGGAL UTC; PBO < 0,50; DSR > 0,95; tidak
ada transaksi rugi melampaui -1,5R. Butir rezim DITANGGUHKAN sampai ADR-A003.

## Sari batas alat (versi panjang: prompt pembuka §0A)

- Seluruh operasi GitHub lewat `runTool({toolName, toolArguments})`.
- TIDAK ADA alat untuk GitHub Actions: tidak bisa memicu, tidak bisa membaca log,
  tidak bisa melihat status. Status hanya lewat artefak yang di-commit workflow.
  Terbukti bekerja di repo ini: `reports/ci_terakhir.json` dan `.txt` memuat
  kode keluar, cacah uji, dan jejak kegagalan lengkap.
- Tidak ada API patch. Rancang berkas kecil. `push_files` untuk perubahan berkait.
- Blob sha hanya dari `get_file_contents` (termasuk daftar direktori), bukan dari
  `get_commit`.
- `raw.githubusercontent` tidak dapat dipakai verifikasi. Setelah mendorong
  berkas panjang, baca ulang dari main dan pastikan EKORNYA hadir.
- `cache: 'pip'` butuh `requirements.txt` di akar. Sudah ada; jangan dihapus.
- Pola CI yang sudah terpasang dan terbukti: cetak cacah uji sebelum pytest;
  `set +e`; jalankan; simpan kode; tulis laporan; commit `[skip ci]`;
  `git pull --rebase --autostash`; baru `exit`.
- Runner: 4 vCPU, ~15 GB RAM, ~14 GB disk, 6 jam per job. Tidak ada scipy, tidak
  ada requests. Arsip `data.binance.vision` bisa; `fapi.binance.com` 451.

## Posisi sekarang (satu paragraf)

Tugas 0 selesai: arsip modul dibongkar dan dibaca, PETA MODUL ditulis, temuan
warisan A-P diverifikasi satu per satu (C, D, E, F, H, I, J, K, L, M, N, P
terverifikasi; O terverifikasi dengan koreksi; G sebagian; A dan B belum bisa
diperiksa tanpa juri sendiri). Tugas 1 selesai: repo publik dibuka, ADR-A001
memaku aturan dasar, enam berkas kontinuitas ada, CI berjalan dan terbukti
meninggalkan jejak yang bisa dibaca, kerangka paket `lux_ai/` dibuat. Run CI
pertama MERAH karena guard berbasis kata (KC-3) dan sudah diganti pengukur AST
yang cara mengukurnya ikut diuji. Belum ada satu baris pun kode riset, belum ada
data, belum ada hipotesis, N_percobaan masih 0.

## Daftar tugas berprioritas

1. **Pastikan CI hijau** — baca `reports/ci_terakhir.json`; bila `kode_keluar`
   bukan 0, baca `reports/ci_terakhir.txt` sebelum menyentuh apa pun.
2. **ADR-A002 (serapan)** — paku sumber arsip, cakupan simbol termasuk yang
   delisting (dari INDEKS ARSIP, bukan daftar pair aktif), rentang waktu,
   karantina N hari pertama sejak listing, format simpan (parquet per
   simbol-bulan), dan estimasi ukuran dari pengukuran 12 simbol probe.
3. **Pengukuran 12 simbol probe** — ukur dulu, ekstrapolasi, catat angkanya di
   ADR-A002 sebelum menjalankan serapan penuh.
4. **Workflow serapan matriks** sebagai proses latar; manifes per pecahan berisi
   nama, jumlah baris, rentang waktu, checksum, sumber arsip.
5. **Uji integritas resample** 1m -> 5m/15m untuk 12 simbol probe melawan berkas
   asli. Ketidakcocokan menghentikan pipeline.
6. **Paralel:** ADR-A003 (taksonomi rezim/label) lalu juri T4 di atas 12 simbol.
7. Baru setelah semesta penuh: baseline B0 + buku penyimpangan.

## Nomor bebas berikutnya

- ADR berikutnya: **ADR-A002**.
- Hipotesis pertama: **H-A001** (belum ada).
- Jurnal berikutnya: `journal/2026-07-28-02.md`.

## HEAD saat penyerahan

Commit isi pertama: `364e578cff911dc8a772051dd30b88da5e3a3b02`.
Commit laporan CI otomatis: `8e1ee938890661980439b0a83f1232a0513a1b45`.
Commit ini (perbaikan guard + v2) lebih baru dari keduanya.

## Berkas inti — byte dan blob sha (dibaca ulang dari main, bukan dari ingatan)

Diambil pada commit `364e578`. Berkas yang diubah commit ini otomatis punya sha
baru; yang tidak diubah tetap sah.

| Berkas | Byte | Blob sha |
|---|---|---|
| `PETA_MODUL.md` | 8691 | `9ee33a991b2ec28405a00550c65f30e419f823cc` |
| `PETA_MODUL_BERKAS.md` | 6890 | `3abe95f6fdac76fc87259f91b638b0903d67048e` |
| `README.md` | 1910 | `d875f3643e274bf6e7b47b84ccfcd8ada016c554` |
| `STATE_LAMPIRAN.md` | 2350 | `f2b907648bb291d5a4e44e5683270d84cf981a6a` |
| `STATE_LAMPIRAN_ANGKA.md` | 1841 | `f3ebdb02f4e03fea6e45a2fba107a50f69ace7c6` |
| `requirements.txt` | 71 | `b3749ba54f8b27bd9f8bc002f38c11d33f4c1a07` |
| `decisions/ADR-A001.md` | belum dicatat | `d5bb2f64862b0e2f4b49a3591b3b65e662469e2f` |
| `journal/2026-07-28-01.md` | 2618 | `fc13dc310a3c3eff22df3849799d695f6a8cf3a8` |
| `PROMPT_KELANJUTAN.md` (v1, digantikan) | 4120 | `42b5210d284fcf00afe39d6284090dd594ff0aae` |
| `STATE.md` (v1, digantikan) | 3126 | `f28dfb1f99d1063df2ebb400aeb0085efe578ce4` |

Ekor `PETA_MODUL.md` dan `decisions/ADR-A001.md` sudah dibaca ulang dari main dan
utuh. Byte `ADR-A001.md` belum dicatat: utang kecil, bayar di v3.
