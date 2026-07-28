# PROMPT KELANJUTAN — v24

Kamu melanjutkan riset LUX-AI. Operator: Diva Juan Nur Taqarrub, GitHub EnVyxS,
zona waktu Asia/Jakarta, bahasa kerja Indonesia. Jangan mulai bekerja sebelum
menyelesaikan LANGKAH 0. **Berkas di repo adalah kebenaran; prompt ini hanya
peta.**

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`. `owner` dan
   `repo` HANYA di dalam `toolArguments`, tidak di tingkat atas.
3. Baca dari `main` repo `EnVyxS/lux-ai-research`, berurutan:
   - `PROMPT_KELANJUTAN.md` (v24)
   - **`STATE.md` (v22 — aturan 1-40, kelas cacat KC-1..KC-15, papan skor,
     daftar utang; INI YANG PALING PENTING)**
   - `journal/2026-07-28-50.md` dan `-51.md`
   - `decisions/ADR-A007.md`, lalu `ADR-A006.md`
   - `ADR-A004.md` dan `ADR-A002.md` bila menyentuh serapan
   - `PETA_MODUL.md` bila menyentuh modul warisan
4. Baru setelah itu jalankan pekerjaan teknis.

## Batasan yang mahal dipelajari ulang

- Sandbox agen **tidak punya jaringan**. Semua unduhan dan pengukuran arsip
  dijalankan GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- **Tidak ada alat untuk membaca status GitHub Actions** dan tidak ada alat untuk
  memicu `workflow_dispatch`. Status hanya dari berkas laporan yang di-commit
  workflow itu sendiri. Satu-satunya cara menyalakan run adalah **push ke berkas
  modul yang tersebut di `paths` workflow**.
- **Tidak ada API patch.** `push_files` menulis ulang seluruh isi berkas.
  Rancang berkas kecil; setelah mendorong berkas panjang, BACA ULANG dari `main`
  dan pastikan ekornya hadir.
- Saat memeriksa hasil run, cocokkan `run_id` / `sidik_kode` / blob sha. **Jangan
  percaya keberadaan berkas** — laporan run lama sering masih terbaca.
- Manifes pecahan sangat besar: baca `reports/pecahan_<i>.log`, bukan
  `reports/manifes_pecahan_<i>.json`.
- `search_code` mengembalikan 0 hasil di repo ini (tidak berindeks) — pakai
  `get_file_contents`.
- Runner: numpy, pandas, pyarrow, pyyaml, pytest tersedia; **tidak ada** scipy
  dan requests. `data.binance.vision` bisa diakses; `fapi.binance.com` → 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. `lux-research` boleh
  DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## Posisi (2026-07-28, sesi 51)

Rantai commit sesi ini: `38e36c2b` → `56b28db8` (jurnal 50) → `f3096288`
(diagnosa kc14c) → `9bd95187` (STATE v21 + PROMPT v23) → `0702d9c1`
(rilis.py + serap.py v3 + 2 berkas uji) → `5950152e` (jurnal 51) → `ed203678`
(diagnosa_kc15 + uji + workflow) → `a360bf11` (perbaikan kelas risiko kc15 +
`baca_zip(teks=True)`) → `4aea79ce` (ADR-A007) → STATE v22 + PROMPT v24.

**SATU RUN SEDANG BERJALAN:** diagnosa KC-15 tepi bulan, dipicu `a360bf11`.
Laporannya `reports/diagnosa_kc15.json` + `_status.json` + `.log`. Beban ≈41
berkas bulanan dan ≤2 berkas harian per bulan bertepi tak nol.

**Temuan terbesar sesi 51: KC-15 TERBUKTI.** `menit_hadir_di_harian_saat_`
`bulanan_hilang` = **7.200** pada BNXUSDT 2022-04, 2022-06, 2022-08. Berkas
BULANAN kehilangan lima hari UTC penuh yang ada dan utuh di berkas HARIAN.
H-A003 MENANG pada 3, GUGUR pada 9. Kedua belas simbol-bulan karantina terpisah
menjadi KC-14 (9 kasus, 6.375 menit, lubang nyata di kedua representasi) dan
KC-15 (3 kasus, 7.200 menit, dapat dipulihkan). 6.375 + 7.200 = 13.575 ✅.

Uji **141** terverifikasi (run `30359672326`). Sesudahnya ditambah empat berkas
uji; cacah barunya hanya sah dari `reports/ci_terakhir.json` (aturan 38).

## Pekerjaan berikutnya, berurutan

1. **Baca `reports/diagnosa_kc15_status.json` lalu `reports/diagnosa_kc15.json`**
   (cocokkan `run_id` dan `sidik_kode`) → adjudikasi **R-117, R-118, R-119,
   R-120**. Bila `cacah_gerbang_lolos_padahal_tepi_terpotong` > 0: namai
   **KC-16**, ADR-A004 perlu klausa gerbang ketujuh (bandingkan tepi bulan
   TENGAH terhadap kalender), dan ADR-A007 diperluas ke tepi. Bila
   `bulan_tengah_diperiksa` = 0 → TIDAK MENGUKUR, keempatnya TIDAK
   TERADJUDIKASI (aturan 30).
2. **Jurnal 52**: adjudikasi butir 1, pra-registrasi mulai **R-121**.
3. **Setujui atau tolak ADR-A007** berdasarkan hasil tepi, lalu terapkan ke
   kode: `sumber_baris`, `cacah_baris_dipulihkan`, `cacah_hari_dipulihkan`,
   `cacah_pemulihan_gagal_checksum` (wajib nol), gerbang dijalankan ULANG tanpa
   pelunakan ambang. Memulihkan 7.200 menit BNXUSDT.
4. **ADR-A006 bagian 2/2** — satu-satunya yang menghalangi data bertahan:
   sambungkan `rilis.PengemasBerbelah` ke `pecahan.py` (naikkan `VERSI` ke 3,
   tambahkan `rilis.py` ke `sidik_kode`, gerbangi dengan env `PECAHAN_KEMAS`)
   dan perluas `.github/workflows/pecahan_serapan.yml` agar mengunggah tar
   terbelah + `SHA256SUMS` sebagai aset rilis lewat `gh release`. **Menaikkan
   VERSI di `pecahan.py` menyalakan matriks 8 job ±1,5 jam** — lakukan hanya
   setelah CI membuktikan pengemas. Sampai ini selesai, parquet 32,71 GB tetap
   ditulis, diukur, dihapus.
5. Verifikasi `reports/ci_terakhir.json` untuk cacah uji baru (aturan 38).
6. Jalur **funding**: `funding_ada` masih null di seluruh manifes (ADR-A002 §9);
   medan `dugaan_pengganti` (ADR-A005) juga belum ada.
7. Sisa utang 24: karantina artefak 7 hari; mengadjudikasi R-7, R-19, R-20,
   R-36, R-37.
8. Belum diukur: sebab KC-15 (khas simbol? khas 2022? tersebar?); 15 `SETTLED`
   lain; kelengkapan `INDEKS` (3 nama manual); pemisahan saham/komoditas token
   dari 787 `perpetual_usdt`; keamanan `arsip.bulan_tersedia` untuk simbol
   Tionghoa; `.decode("utf-8","replace")`; apakah BUSD/USDC layak digabung.
9. Paralel, boleh kapan saja (aturan 3): ADR-A003 taksonomi rezim; juri T4
   dengan biaya sejak hari pertama; lapisan validasi (uji bulanan berpasangan +
   Šidák, ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy murni).
10. Utang lama menunggu tahap lain: 1, 2, 3, 4, 5, 11. **Adjudikasi riset TETAP
    TERKUNCI sampai data serapan benar-benar bertahan** — bukan lagi sampai
    manifes terverifikasi, karena manifesnya sudah terverifikasi penuh.

## Ramalan yang menunggu adjudikasi

- **R-117**: BNXUSDT 2022-04 `tepi_awal + tepi_akhir` = 210 dan
  `menit_tepi_hadir_di_harian` = 210. Bila 2022-04 ternyata bulan pertama
  BNXUSDT di arsip, ramalan MELESET dan 210 menit itu sah.
- **R-118**: dari 40 bulan TENGAH yang lolos gerbang, cacah bulan bertepi tak
  nol di pita **0..6**.
- **R-119**: total menit tepi atas 40 sampel di pita **0..1.200**.
- **R-120**: bila R-118 > 0 maka `menit_tepi_hadir_di_harian` > 0 pada ≥1 bulan.
  Bila R-118 = 0 → TIDAK TERADJUDIKASI, bukan TEPAT.
- Lama menunggu: R-7, R-19, R-20, R-28, R-36, R-37.
- Papan skor R-1..R-116: TEPAT **76**, MELESET **27**, SEPARUH **4**, TIDAK
  TERADJUDIKASI **3**, MENUNGGU **6** (jumlah 116 ✅). Ramalan berikutnya
  **R-121**. N_percobaan = 0.

## Penomoran berikutnya

Jurnal `journal/2026-07-28-52.md`. STATE v23. PROMPT v25. ADR berikutnya
**A008** (A003 dicadangkan, belum ada). Hipotesis: H-A001 (belum), H-A002a/b
(selesai), H-A003 (selesai: menang 3, gugur 9), H-A004 (tak dapat diuji),
H-A005 (sedang diuji). Aturan terakhir **40**. Kelas cacat terakhir **KC-15**;
**KC-16 dicadangkan** untuk pemotongan tepi yang lolos gerbang — jangan dinamai
sebelum laporan tepi ada.

## Kebiasaan

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. 27 MELESET; deret TEPAT
  panjang = ramalan terlalu aman.
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21). Aturan 40:
  `baris + hilang_di_tengah + tepi = menit_kalender`, laporkan selisihnya walau
  nol — 210 menit BNXUSDT hanya muncul karena hitung ulang manual.
- Aturan 39: keseragaman pada sampel dilarang jadi angka ramalan bagi anggota di
  luar sampel. Itulah yang membuat R-114 meleset.
- Setiap pengukuran sebab wajib memuat medan penggugur (aturan 24); aturan 37
  sampel wajib memuat ≥1 kasus tiap kelas cacat relevan dan kelas kosong wajib
  disebut — dan jangan melaporkan kelas KOSONG yang sebenarnya tersentuh.
- Aturan 20: dilarang menyimpulkan di luar rentang yang disampel.
- **BACA berkas sebelum menuduhnya salah** (pola salah-tuduh sudah ENAM kali;
  sesi 51 hampir menjadi ketujuh — `gerbang_1m.py` dibaca dan ternyata benar).
- Pisahkan fakta dari asumsi; tanpa bukti tulis "Ini memerlukan verifikasi."
- "lanjut" berarti teruskan tanpa konfirmasi.
- Perbarui `STATE.md`, jurnal, dan `PROMPT_KELANJUTAN.md` secara berkala.
- Jangan berhenti dengan alasan konteks Notion; patokannya konteks model.
- Ada tenggat: riset dipercepat sebelum **3 Agustus 2026**.
