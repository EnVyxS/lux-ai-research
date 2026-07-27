# PROMPT KELANJUTAN — v1

Ditulis 2026-07-28. Bahasa kerja: Indonesia.

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

## Ambang yang sudah dibekukan

Ekspektasi bersih >= 0,05R; >= 100 transaksi per sel; p <= 0,05 dengan koreksi
Sidak; permutasi >= 300 ulangan per TANGGAL UTC; PBO < 0,50; DSR > 0,95; tidak
ada transaksi rugi melampaui -1,5R. Butir rezim DITANGGUHKAN sampai ADR-A003.

## Sari batas alat (versi panjang: prompt pembuka §0A)

- Seluruh operasi GitHub lewat `runTool({toolName, toolArguments})`.
- TIDAK ADA alat untuk GitHub Actions: tidak bisa memicu, tidak bisa membaca log,
  tidak bisa melihat status. Status hanya lewat artefak yang di-commit workflow.
- Tidak ada API patch. Rancang berkas kecil. `push_files` untuk perubahan berkait.
- Blob sha hanya dari `get_file_contents`, bukan dari `get_commit`.
- `raw.githubusercontent` tidak dapat dipakai verifikasi. Setelah mendorong
  berkas panjang, baca ulang dari main dan pastikan EKORNYA hadir.
- `cache: 'pip'` butuh `requirements.txt` di akar. Sudah ada; jangan dihapus.
- Pola CI: cetak cacah uji sebelum pytest; `set +e`; jalankan; simpan kode;
  tulis laporan; commit `[skip ci]`; `git pull --rebase --autostash`; baru exit.
- Runner: 4 vCPU, ~15 GB RAM, ~14 GB disk, 6 jam per job. Tidak ada scipy, tidak
  ada requests. Arsip `data.binance.vision` bisa; `fapi.binance.com` 451.

## Posisi sekarang (satu paragraf)

Tugas 0 selesai: arsip modul dibongkar dan dibaca, PETA MODUL ditulis, temuan
warisan A-P diverifikasi satu per satu (C, D, E, F, H, I, J, K, L, M, N, P
terverifikasi; O terverifikasi dengan koreksi; G sebagian; A dan B belum bisa
diperiksa tanpa juri sendiri). Tugas 1 selesai: repo publik dibuka, ADR-A001
memaku aturan dasar, enam berkas kontinuitas ada, kerangka CI terpasang, kerangka
paket `lux_ai/` dibuat. Belum ada satu baris pun kode riset, belum ada data,
belum ada hipotesis, N_percobaan masih 0.

## Daftar tugas berprioritas

1. **ADR-A002 (serapan)** — paku sumber arsip, cakupan simbol termasuk yang
   delisting (dari INDEKS ARSIP, bukan daftar pair aktif), rentang waktu,
   karantina N hari pertama sejak listing, format simpan (parquet per
   simbol-bulan), dan estimasi ukuran dari pengukuran 12 simbol probe.
2. **Pengukuran 12 simbol probe** — ukur dulu, ekstrapolasi, catat angkanya di
   ADR-A002 sebelum menjalankan serapan penuh.
3. **Workflow serapan matriks** sebagai proses latar; manifes per pecahan berisi
   nama, jumlah baris, rentang waktu, checksum, sumber arsip.
4. **Uji integritas resample** 1m -> 5m/15m untuk 12 simbol probe melawan berkas
   asli (open, high, low, close, volume). Ketidakcocokan menghentikan pipeline.
5. **Paralel:** ADR-A003 (taksonomi rezim/label) lalu juri T4 di atas 12 simbol.
6. Baru setelah semesta penuh: baseline B0 + buku penyimpangan.

## Nomor bebas berikutnya

- ADR berikutnya: **ADR-A002**.
- Hipotesis pertama: **H-A001** (belum ada).
- Jurnal berikutnya: `journal/2026-07-28-02.md` (bila sesi berlanjut hari yang
  sama), selain itu `journal/<tanggal>-01.md`.

## HEAD saat penyerahan

Commit "Tugas 0+1". Blob sha berkas inti BELUM dicatat di v1 — dicatat di v2
setelah pembacaan ulang dari main. Ini utang verifikasi yang harus dibayar di
sesi ini juga.
