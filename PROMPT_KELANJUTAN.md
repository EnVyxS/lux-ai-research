# PROMPT KELANJUTAN — v4

Ditulis 2026-07-28. Repo: `EnVyxS/lux-ai-research` (PUBLIK).
Bila kamu sesi baru: yang tercommit itu nyata, sisanya tidak ada.

## 1. Urutan baca yang mengikat

1. Berkas ini, utuh.
2. `decisions/ADR-A002.md` (ADR terbaru), lalu `decisions/ADR-A001.md`.
3. `STATE.md`.
4. `STATE_LAMPIRAN.md`, lalu `STATE_LAMPIRAN_ANGKA.md`.
5. Dua jurnal terakhir: `journal/2026-07-28-03.md`, `journal/2026-07-28-02.md`.
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
- Jangan menulis guard berbasis pencarian kata (KC-3).
- Jangan menulis uji yang menyentuh jaringan (aturan 14).
- Jangan menulis angka arsip sebelum artefaknya ada (aturan 13).
- Jangan menamai medan laporan lebih besar daripada yang diukurnya (aturan 16,
  KC-5). Sebelum menghitung sebuah ramalan lulus, tanyakan medan itu MENGUKUR
  apa.
- Jangan mengganti data biaya yang hilang dengan nol (aturan 17).

## 3. Ambang yang sudah dibekukan

- Ekspektasi bersih ≥ 0,05R setelah biaya. Minimal 100 transaksi per sel.
- p ≤ 0,05 uji bulanan berpasangan + koreksi Sidak:
  `alpha_sidak = 1 - (1 - 0,05)^(1/N_percobaan)`.
- Permutasi ≥ 300 ulangan, diacak PER TANGGAL UTC.
- PBO < 0,50 dan DSR > 0,95. Tidak ada rugi melampaui -1,5R.
- Butir rezim DITANGGUHKAN sampai ADR-A003 dan penangguhan wajib disebut.
- N_percobaan berjalan: **0**.
- Karantina listing: **N = 7 hari** (ADR-A002 §4).
- Pemecahan serapan: **8 pecahan**, berimbang menurut cacah bulan (ADR-A002 §9).

## 4. Sari batas alat (§0A), plus yang terbukti di repo ini

- Semua operasi GitHub lewat `runTool({toolName, toolArguments})`. `owner` dan
  `repo` HANYA boleh ada di dalam `toolArguments`; menaruhnya di tingkat atas
  ditolak. Kesalahan nyata, 2026-07-28.
- TIDAK ADA alat untuk Actions. Status run hanya dari artefak yang di-commit.
  Pola laporan-sebelum-exit TERBUKTI bekerja dua kali di repo ini.
- `push_files` untuk banyak berkas satu commit. Tidak ada API patch.
- Setelah mendorong berkas panjang, baca ulang dari `main` dan pastikan EKORNYA
  hadir. Ukuran bukan bukti isi.
- `cache: 'pip'` butuh `requirements.txt` di akar. Sudah ada.
- Sandbox agen TIDAK punya jaringan. Semua unduhan lewat runner.
- Runner TERUKUR di repo ini: listing 937 simbol + 12 unduhan + cacah 937 simbol
  selesai dalam ~10 menit. Unduh rerata 1,33 detik per berkas.
- Runner: 4 vCPU, ~15 GB RAM, ~14 GB disk bebas, 6 jam per job. Tanpa scipy,
  tanpa requests. Statistik harus numpy murni.
- `data.binance.vision` bisa dari runner; `fapi.binance.com` 451 (tak diuji).

## 5. Posisi sekarang, satu paragraf

Tugas 0, 1, dan 2 selesai. Peta modul lengkap; temuan warisan A-P dinilai satu
per satu. ADR-A001 mematok aturan dasar; ADR-A002 kini DITERIMA penuh dengan
angka arsip terukur: 937 simbol, 21.789 berkas bulanan 1m, batas atas 25,86 GB
zip / 39,17 GB parquet, 12/12 checksum cocok, 0 celah waktu. Dari lima ramalan
arsip, satu tepat, satu meleset separuh, satu meleset penuh, satu tidak
teradjudikasi karena label salah ukur (KC-5), satu tanpa medan pengukuran. Klaim
warisan "34.000 berkas, 40-60 GB" dibantah. Serapan penuh sudah DIIZINKAN tetapi
BELUM dibangun. CI hijau dengan 15 uji. Belum ada satu pun angka strategi, belum
ada juri, belum ada baseline B0, N_percobaan masih 0.

## 6. Daftar tugas berprioritas

1. Bangun uji integritas resample: 1m → 5m dan 15m dibandingkan berkas ASLI
   untuk 12 simbol probe, pada open/high/low/close/volume. Ketidakcocokan
   menghentikan pipeline. Ini menjaga keputusan ADR-A002 §3.
2. Bangun workflow serapan penuh: matriks 8 pecahan (ADR-A002 §9), manifes per
   pecahan (nama, baris, rentang waktu, checksum, sumber, `funding_ada`,
   `baris_dibuang`, `berheader`), parquet per simbol-bulan sebagai aset rilis.
   Tambahkan medan `berheader` supaya R-5 akhirnya bisa diadjudikasi.
3. Ukur stempel waktu bar terakhir SRMUSDT/COCOSUSDT/BTSUSDT untuk membayar
   utang verifikasi 9, dan cacah simbol yang bulan terakhirnya lebih tua dari
   2026-01 untuk mengadjudikasi R-8.
4. Paralel, di atas 12 simbol probe: ADR-A003 (taksonomi rezim, likuiditas,
   sesi, struktur, funding; label point-in-time), lalu juri T4, lalu validasi.
5. DSR dan PBO: operator sudah mengizinkan pembacaan `lux-research`. Bila
   `lux/validasi/dsr.py` (8.328 byte, blob
   `d87924b6e6b3f54dbbe4959260dc22c501b9c997`) dan `pbo.py` (10.097 byte, blob
   `630898cf933cb626fa4ee4a634adb56d91956a2b`) disalin, salin apa adanya dengan
   catatan pengangkatan.
6. Baru setelah semesta penuh + manifes terverifikasi: Baseline B0 + BUKU
   PENYIMPANGAN + pra-registrasi, lalu adjudikasi pertama.

## 7. Penomoran berikutnya

- ADR bebas berikutnya: **ADR-A003**.
- Jurnal berikutnya: **`journal/2026-07-28-04.md`**.
- Hipotesis pertama masih **H-A001** (belum terpakai).
- Ramalan berikutnya: **R-9**.

## 8. HEAD saat penyerahan

- `3ea77dc1b6553275221b3d8358de5ef4ba5312b1` — laporan probe run 30312616216,
  `kode_keluar: 0`.
- Sebelumnya: `4e6b6f4e419449fe894d07eb1ff51b04c2e0532f` (laporan CI 30312819816),
  `716bc22db8b916e729f101f636662c2513352e42` (STATE v3 + PROMPT v3),
  `55837eac88bf293933f61c91ec5ab2a54695882d` (klien arsip + workflow probe),
  `364e578cff911dc8a772051dd30b88da5e3a3b02` (isi pertama).

## 9. Berkas inti — byte dan blob sha pada commit 3ea77dc

| Berkas | Byte | Blob sha |
|---|---|---|
| `README.md` | 1.910 | `d875f3643e274bf6e7b47b84ccfcd8ada016c554` |
| `requirements.txt` | 71 | `b3749ba54f8b27bd9f8bc002f38c11d33f4c1a07` |
| `STATE.md` (v3) | — | `a322232b517921307c00329de42f68a02a162fc3` |
| `STATE_LAMPIRAN.md` | 2.350 | `f2b907648bb291d5a4e44e5683270d84cf981a6a` |
| `STATE_LAMPIRAN_ANGKA.md` | 1.841 | `f3ebdb02f4e03fea6e45a2fba107a50f69ace7c6` |
| `PROMPT_KELANJUTAN.md` (v3) | — | `ecafec54d7fa97c5bf2a9bb6fa6bd1e9f23043ec` |
| `PETA_MODUL.md` | 8.691 | `9ee33a991b2ec28405a00550c65f30e419f823cc` |
| `PETA_MODUL_BERKAS.md` | 6.890 | `3abe95f6fdac76fc87259f91b638b0903d67048e` |
| `decisions/ADR-A001.md` | 3.569 | `d5bb2f64862b0e2f4b49a3591b3b65e662469e2f` |
| `decisions/ADR-A002.md` (sebelum §7 terisi) | 3.767 | `3104f949e4c9558a3ca402699396a1c84120670d` |
| `journal/2026-07-28-01.md` | 2.618 | `fc13dc310a3c3eff22df3849799d695f6a8cf3a8` |
| `journal/2026-07-28-02.md` | 1.852 | `44d02d441635345328d81f39d8f017bcdceda3af` |

Baris `STATE.md`, `PROMPT_KELANJUTAN.md`, dan `decisions/ADR-A002.md` adalah
versi SEBELUM commit v4; perbarui ketiganya di pembaruan berikutnya.

## 10. Artefak probe yang sudah ada di `main`

| Berkas | Isi |
|---|---|
| `reports/probe_serapan.json` | pengukuran 12 simbol + cacah semesta + estimasi |
| `reports/semesta_bulan_1m.json` | cacah bulan 1m untuk 937 simbol |
| `reports/probe_status.json` | run_id, commit, kode_keluar, waktu |
| `reports/probe_serapan_progres.json` | tahap terakhir; ditulis tiap 25 simbol |
| `reports/ci_terakhir.json` / `.txt` | status CI terakhir |

## 11. Kode serapan yang sudah ada

| Berkas | Byte | Blob sha | Isi |
|---|---|---|---|
| `lux_ai/serapan/arsip.py` | 5.231 | `0104958bd99772cda8262d5527da52aea9635724` | listing S3, URL, checksum, unduh terverifikasi |
| `lux_ai/serapan/klines.py` | 2.696 | `c308b9676fdb1fe78b1a9d4c7304253975109409` | baca zip, deteksi header, rapikan, parquet zstd |
| `lux_ai/serapan/probe.py` | 6.594 | `df0a2d5da219b953f307e5034f00a7a9ef7495d9` | pengukuran 12 probe + cacah semesta |

Workflow: `.github/workflows/ci.yml` (uji) dan
`.github/workflows/probe_serapan.yml` (probe; terpicu oleh perubahan di
`lux_ai/serapan/**`, menulis progres tiap 10 menit).
