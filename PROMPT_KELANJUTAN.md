# PROMPT KELANJUTAN — v5

Ditulis 2026-07-28. Repo: `EnVyxS/lux-ai-research` (PUBLIK).
Bila kamu sesi baru: yang tercommit itu nyata, sisanya tidak ada.

## 1. Urutan baca yang mengikat

1. Berkas ini, utuh.
2. `decisions/ADR-A002.md` (ADR terbaru), lalu `decisions/ADR-A001.md`.
3. `STATE.md` (v5).
4. `STATE_LAMPIRAN.md`, lalu `STATE_LAMPIRAN_ANGKA.md`.
5. Dua jurnal terakhir: `journal/2026-07-28-05.md`, `journal/2026-07-28-04.md`.
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
- Jangan mempercayai gerbang hijau yang tidak melaporkan CACAH yang
  dibandingkan, terutama bila ia lolos jauh lebih cepat daripada dugaan
  (aturan 18).
- Jangan memakai float pada jalur perbandingan data arsip; Decimal atas teks
  asli (aturan 19).
- Berkas 5m/15m ASLI hanya untuk uji integritas. Dilarang masuk backtest.

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
  Pola laporan-sebelum-exit sudah terbukti bekerja pada tiga workflow.
- `push_files` untuk banyak berkas satu commit. Tidak ada API patch.
- Setelah mendorong berkas panjang, baca ulang dari `main` dan pastikan EKORNYA
  hadir. Ukuran bukan bukti isi.
- Menyentuh `lux_ai/serapan/**` memicu ULANG workflow `probe-serapan`. Itu
  disengaja dibiarkan sekali sebagai uji keterulangan; bila tidak diinginkan,
  sempitkan pemicunya lebih dulu.
- Sandbox agen TIDAK punya jaringan. Semua unduhan lewat runner.
- Runner TERUKUR: probe penuh ~10 menit; uji resample 12 simbol ~71 detik;
  unduh rerata 1,33 detik per berkas.
- Runner: 4 vCPU, ~15 GB RAM, ~14 GB disk bebas, 6 jam per job. Tanpa scipy,
  tanpa requests. Statistik harus numpy murni.
- `data.binance.vision` bisa dari runner; `fapi.binance.com` 451 (tak diuji).

## 5. Posisi sekarang, satu paragraf

Tugas 0, 1, dan 2 selesai. ADR-A002 DITERIMA penuh: 937 simbol, 21.789 berkas
bulanan 1m (keduanya TERULANG pada run probe kedua), batas atas 25,86 GB zip /
39,17 GB parquet, 12/12 checksum cocok, 0 celah waktu. Keputusan "unduh 1m saja,
turunkan interval lain" kini TERBUKTI: bar 5m dan 15m turunan cocok dengan
berkas asli arsip pada seluruh sembilan kolom untuk 12 simbol probe, lebih dari
138 ribu bar dibandingkan, nol beda. Format arsip memang berubah di tengah
sejarah (KC-4 terbukti): bulan 2020-01..2021-02 tanpa header, 2022-04 dan
sesudahnya berheader. Dari sebelas ramalan yang sudah jatuh temponya: lima
tepat, tiga meleset, satu meleset separuh, satu tidak teradjudikasi karena label
salah ukur (KC-5). Serapan penuh DIIZINKAN tetapi BELUM dibangun. CI hijau
dengan 26 uji. Belum ada satu pun angka strategi, belum ada juri, belum ada
baseline B0, N_percobaan masih 0.

## 6. Daftar tugas berprioritas

1. **Survei semesta** (satu workflow, membayar banyak utang sekaligus): untuk
   937 simbol catat bulan pertama, bulan terakhir, cacah bulan; untuk itu
   adjudikasi R-8 (berapa simbol yang bulan terakhirnya lebih tua dari 2026-01).
   Ganti medan `delisting_klaim_terbukti` di `probe.py` dengan ukuran yang benar
   (jarak bulan terakhir simbol terhadap bulan tutup terakhir semesta) plus uji
   atas CARA MENGUKUR-nya (utang 13, KC-5). Ukur juga stempel waktu bar terakhir
   SRMUSDT/COCOSUSDT/BTSUSDT (utang 9) dan bulan persis peralihan format header
   untuk beberapa simbol yang hidup melintasi 2021-2022 (utang 11, R-13).
2. **Perluas gerbang resample ke era tanpa header**: ulangi perbandingan pada
   bulan PERTAMA tiap simbol probe, bukan hanya bulan terakhir (utang 12, R-12).
3. **Workflow serapan penuh**: matriks 8 pecahan (ADR-A002 §9), manifes per
   pecahan (nama, baris, rentang waktu, checksum, sumber, `funding_ada`,
   `baris_dibuang`, `berheader`, `awal_sejati`, `akhir_sejati`), parquet per
   simbol-bulan sebagai aset rilis. Ini mengadjudikasi R-7.
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
- Jurnal berikutnya: **`journal/2026-07-28-06.md`**.
- Hipotesis pertama masih **H-A001** (belum terpakai).
- Ramalan berikutnya: **R-14**.

## 8. HEAD saat penyerahan

- `af08e3463fc45e2f3eb5e30997c2d22e535c0d45` — adjudikasi R-5/R-6/R-9/R-10/R-11
  + STATE v5 (commit ini belum menyertakan PROMPT v5; PROMPT v5 adalah commit
  sesudahnya).
- Sebelumnya: `84009e8dcdbf0a6277cecefda6b472fd4e8e78b5` (laporan probe run
  kedua 30314166310), `429037e7cc65a4536922b91c48303126b1e20d32` (laporan uji
  resample run 30314166289, `kode_keluar: 0`),
  `922fe507ceb8f51bdfe9421892ce548f2530ad33` (laporan CI 30314166290, 26 uji),
  `6639bbe5b0bd95e4925ff8e581594bc4912f5b9a` (resample + uji integritas),
  `96e2387effceee506218d7b9969022880ebc9632` (ADR-A002 §7 terisi, STATE v4),
  `3ea77dc1b6553275221b3d8358de5ef4ba5312b1` (laporan probe run pertama).

## 9. Berkas inti — byte dan blob sha

Byte diukur pada commit `96e2387` untuk berkas yang tidak berubah sesudahnya;
blob sha berkas yang berubah diambil pada `af08e346`. Tanda — berarti byte-nya
belum diukur, jangan mengarangnya.

| Berkas | Byte | Blob sha |
|---|---|---|
| `README.md` | 1.910 | `d875f3643e274bf6e7b47b84ccfcd8ada016c554` |
| `requirements.txt` | 71 | `b3749ba54f8b27bd9f8bc002f38c11d33f4c1a07` |
| `STATE.md` (v5) | — | `4128c1b59615453490e5cd2b41759925d100d7c9` |
| `STATE_LAMPIRAN.md` | 2.350 | `f2b907648bb291d5a4e44e5683270d84cf981a6a` |
| `STATE_LAMPIRAN_ANGKA.md` | 1.841 | `f3ebdb02f4e03fea6e45a2fba107a50f69ace7c6` |
| `PROMPT_KELANJUTAN.md` (v4, versi SEBELUM berkas ini) | 8.146 | `de8a3ad3d6db286524ad3e65f32a2535e3ee9e1c` |
| `PETA_MODUL.md` | 8.691 | `9ee33a991b2ec28405a00550c65f30e419f823cc` |
| `PETA_MODUL_BERKAS.md` | 6.890 | `3abe95f6fdac76fc87259f91b638b0903d67048e` |
| `decisions/ADR-A001.md` | 3.569 | `d5bb2f64862b0e2f4b49a3591b3b65e662469e2f` |
| `decisions/ADR-A002.md` (DITERIMA, §7 terisi) | — | `5d34225481d206fb4c56d198f29e52b0217a84d7` |
| `journal/2026-07-28-05.md` | — | `ccab37c73d8ec5a3a82b092a29092d815c362e86` |
| `journal/2026-07-28-03.md` | — | `2e088c99a5f3eac5ef9cde5d7525df2d9d9e3d02` |

## 10. Artefak yang sudah ada di `main`

| Berkas | Isi |
|---|---|
| `reports/probe_serapan.json` | pengukuran 12 simbol + cacah semesta + estimasi (run kedua) |
| `reports/semesta_bulan_1m.json` | cacah bulan 1m untuk 937 simbol; BELUM pernah dibaca agen |
| `reports/probe_status.json` | run_id, commit, kode_keluar, waktu |
| `reports/probe_serapan_progres.json` | progres ditulis tiap 25 simbol |
| `reports/uji_resample.json` | perbandingan per simbol per interval + medan header |
| `reports/uji_resample_status.json` | run 30314166289, `kode_keluar: 0` |
| `reports/uji_resample.log` / `_progres.json` | ringkasan dan tahap |
| `reports/ci_terakhir.json` / `.txt` | CI 30314166290, 26 uji lulus |

## 11. Kode yang sudah ada (byte dan blob sha pada `6639bbe`)

| Berkas | Byte | Blob sha | Isi |
|---|---|---|---|
| `lux_ai/serapan/arsip.py` | 5.231 | `0104958bd99772cda8262d5527da52aea9635724` | listing S3, URL, checksum, unduh terverifikasi |
| `lux_ai/serapan/klines.py` | 3.445 | `cc4d9287ccb7a8ea72380399c334b4d19b5301d3` | baca zip (mode teks), deteksi header, rapikan, parquet |
| `lux_ai/serapan/probe.py` | 6.594 | `df0a2d5da219b953f307e5034f00a7a9ef7495d9` | pengukuran 12 probe + cacah semesta (medan delisting MASIH salah ukur) |
| `lux_ai/serapan/resample.py` | 4.356 | `66a4b177fa9d784e1ede92522413595d8a8447fa` | turunkan bar N menit dengan Decimal + pembanding |
| `lux_ai/serapan/uji_resample.py` | 5.768 | `5049dbb0e7b9e24c017ec3ebbde8eb21282a85f9` | gerbang integritas resample + pengukuran header |
| `tests/test_kontinuitas.py` | 5.714 | `b377271f02564b647baec46fd6ef3984a4855a3a` | 7 uji |
| `tests/test_serapan.py` | 3.211 | `e787fec59ade70790b4b87bc0ddedbbc7757e77a` | 8 uji |
| `tests/test_resample.py` | 5.613 | `f7c003d702d1aa9e8f02c9eb97ebf6eeecd23e45` | 11 uji |

Workflow: `.github/workflows/ci.yml` (uji), `probe_serapan.yml` (probe),
`uji_resample.yml` (gerbang integritas resample). Ketiganya menulis laporan
SEBELUM keluar dengan kode gagal, dan memakai `[skip ci]`.
