# PROMPT KELANJUTAN v22 — LUX-AI

Disusun 2026-07-28 19:34 WIB. Menggantikan v21 (`d415a960`).
Salin seluruh berkas ini sebagai pesan pertama di sesi baru.

---

Kamu melanjutkan riset LUX-AI. Operator: Diva Juan Nur Taqarrub, GitHub
**EnVyxS**, zona waktu Asia/Jakarta, bahasa kerja Indonesia. Jangan mulai
bekerja sebelum menyelesaikan LANGKAH 0. Berkas di repo adalah kebenaran;
prompt ini hanya peta.

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`. `owner`
   dan `repo` HANYA di dalam `toolArguments`, tidak di tingkat atas.
3. Baca dari main repo `EnVyxS/lux-ai-research`, berurutan:
   `STATE.md` (v20 — aturan 1-37, kelas cacat KC-1..KC-14, papan skor, daftar
   utang; INI YANG PALING PENTING); `journal/2026-07-28-47.md`,
   `journal/2026-07-28-48.md`, `journal/2026-07-28-49.md`;
   `decisions/ADR-A006.md`; `decisions/ADR-A004.md` dan `ADR-A002.md` bila
   menyentuh serapan; `PETA_MODUL.md` bila menyentuh modul warisan.
4. Baru setelah itu jalankan pekerjaan teknis.

## BATASAN YANG MAHAL DIPELAJARI ULANG

- Sandbox agen TIDAK punya jaringan. Semua unduhan dan pengukuran arsip
  dijalankan GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- Tidak ada alat untuk membaca status GitHub Actions dan tidak ada alat untuk
  memicu `workflow_dispatch`. Status hanya diketahui dari berkas laporan yang
  di-commit workflow itu sendiri. Satu-satunya cara menyalakan run adalah
  **push ke berkas modul yang tersebut di `paths` workflow**.
- Tidak ada API patch. `push_files` menulis ulang seluruh isi berkas. Rancang
  berkas kecil. Setelah mendorong berkas panjang, BACA ULANG dari main dan
  pastikan ekornya hadir.
- Saat memeriksa hasil run, **cocokkan `run_id` / `sidik_kode` / blob sha**,
  jangan percaya keberadaan berkas: laporan run lama sering masih terbaca.
- Manifes pecahan sangat besar. Baca ringkasannya lewat
  `reports/pecahan_<i>.log` (cetakan laporan **tanpa** larik manifes), bukan
  `reports/manifes_pecahan_<i>.json`, kecuali memang perlu barisnya.
- `search_code` mengembalikan 0 hasil di repo ini (tidak berindeks). Pakai
  `get_file_contents`.
- Runner: numpy, pandas, pyarrow, pyyaml, pytest tersedia; TIDAK ada scipy dan
  requests. `data.binance.vision` bisa diakses; `fapi.binance.com` → 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. `lux-research` boleh
  DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## POSISI HARI INI (2026-07-28 19:34 WIB)

HEAD `f50b9f40b14395853f05898a9b32d5051733a15b`. Rantai giliran terakhir:
`64d6f3c2` → `b66c9bab` (pecahan.py v1) → `4003f9a7` (bot: manifes pecahan 0)
→ `7a0b4034` (jurnal 47) → `8f86d8be` (pecahan.py VERSI=2 + workflow matriks)
→ `2f50cb80` (ADR-A006) → `cacbb8bb` (diagnosa_kc14) → `9cb7f7b7` (jurnal 48)
→ `118cf836` (jurnal 49) → `f50b9f40` (diagnosa_kc14b).

Uji **135** (127 + 8 uji kc14b) — **belum** dikonfirmasi CI; sebelumnya 123
terverifikasi pada run `30353130258`.

### DUA RUN SEDANG BERJALAN saat prompt ini ditulis

1. **Pecahan 1..7** (matriks paralel, dipicu `8f86d8be`). Keluaran per pecahan:
   `reports/manifes_pecahan_<i>.json`, `reports/pecahan_<i>.log`,
   `reports/pecahan_<i>_status.json`. Perkiraan ±1,5 jam.
2. **Diagnosa KC-14b** (dipicu `f50b9f40`), keluaran
   `reports/diagnosa_kc14b.json`. Perkiraan beberapa menit — seharusnya sudah
   ada saat kamu membaca ini.

### Pecahan 0 SUDAH TERUKUR (run `30353584831`, kode 0)

99 simbol, **2.411 simbol-bulan**, **103.264.917 baris**, 0 gagal unduh, 0 gagal
checksum, 0 baris dibuang, `kelas_risiko_kosong` = **[]**, zip 3,351 GB,
parquet 4,121 GB, nisbah **1,2295**, `selisih_cacah_bulan` = 0.
Gerbang: 2.408 lolos, **3 GAGAL**, `persen_lolos` 99,88.

### KC-14 — arsip 1m TIDAK utuh

AERGOUSDT 2025-04, CVCUSDT 2025-05, SLPUSDT 2025-07 dijatuhkan gerbang pada
klausa `tanpa_menit_hilang` + `jarak_60_detik`. Total **1.875 menit** hilang
(660 + 510 + 705), dikonfirmasi dua jalur independen.

`reports/diagnosa_kc14.json` (blob `b8b340dc`): checksum stabil dua unduhan;
`slot_5m_hadir_saat_1m_hilang` = **0** pada 5m dan 15m → H-A002b (kerusakan satu
interval) GUGUR.

**Pola yang belum terjelaskan**: ketiga lubang mulai **tepat 00:00 UTC**
(2025-04-16, 2025-05-16, 2025-07-23), panjangnya kelipatan 15 menit, dan ketiga
bulan utuh sempurna selain lubang tunggal itu (42.540+660 = 43.200 = 30×1440;
44.130+510 = 44.640; 43.935+705 = 44.640). Sepinya pasar tidak tahu jam berapa
tengah malam UTC → **H-A003**: lubang itu cacat perakitan arsip bulanan, bukan
jeda pasar. Itulah yang diuji diagnosa KC-14b lewat berkas HARIAN.

## PEKERJAAN BERIKUTNYA, BERURUTAN

1. **Baca `reports/diagnosa_kc14b.json`** → adjudikasi **R-110, R-111, R-112**.
   Bila `menit_hadir_di_harian_saat_bulanan_hilang` > 0: namai **KC-15**,
   H-A003 MENANG, arsip bulanan cacat, dan **seluruh serapan berbasis berkas
   bulanan wajib ditinjau** — termasuk mempertimbangkan pindah ke berkas harian
   (amandemen ADR-A002). Bila 0: H-A003 gugur, jeda pasar bertahan, karantina
   ADR-A006 berlaku apa adanya.
2. **Baca `reports/pecahan_<i>.log` untuk i = 1..7** (bukan manifesnya) →
   adjudikasi **R-104, R-105, R-106** dengan hitung ulang baris demi baris.
   Periksa `kelas_risiko_kosong`, `pelanggaran_per_klausa`,
   `selisih_cacah_bulan`, dan `cacah_simbol_gagal_daftar` di setiap pecahan.
   Jumlahkan simbol-bulan kedelapan pecahan; wajib **19.598**.
   Setiap simbol-bulan yang GAGAL gerbang wajib masuk daftar karantina dan
   sebaiknya diperiksa dengan `diagnosa_kc14b` (tambahkan ke `TERSANGKA`).
   Bila satu job mati/timeout, jalankan ulang lewat menaikkan `VERSI` di
   `pecahan.py` (menjalankan ulang SEMUA 1..7) atau `workflow_dispatch` job
   `tunggal` bila operator bisa menekannya di UI.
3. **Jurnal 50**: adjudikasi 1 dan 2, pra-registrasi mulai **R-113**.
4. **STATE v21 + PROMPT v23.** STATE v20 memuat satu baris usang: uji "±123
   belum terverifikasi" — sudah terverifikasi (run `30353130258`). Tambahkan
   KC-14 (+KC-15 bila menang), ADR-A006, R-100..R-112, hasil kedelapan pecahan.
5. **Terapkan ADR-A006 ke kode**: medan `karantina`, `cacah_karantina`,
   `daftar_karantina` di `serap.ringkas`; dan persistensi parquet sebagai rilis
   tar terbelah ≤1,8 GB + `SHA256SUMS`. Sampai ini selesai, **tidak ada data
   serapan yang bertahan** — setiap run hanya menghasilkan angka.
6. **Jalur funding**: `funding_ada` masih `null` di seluruh manifes; ADR-A002
   §9 mewajibkannya. Medan `dugaan_pengganti` (ADR-A005) juga belum ada.
7. Sisa utang 24: karantina 7 hari. Mengadjudikasi R-7, R-19, R-20, R-36, R-37.
8. Belum diukur: 15 `SETTLED` lain; kelengkapan `INDEKS` (3 nama manual);
   pemisahan saham/komoditas token dari 787 perpetual_usdt; keamanan
   `arsip.bulan_tersedia` untuk simbol Tionghoa; `.decode("utf-8","replace")`;
   apakah BUSD/USDC layak digabung dengan USDT.
9. Paralel, boleh kapan saja (aturan 3): ADR-A003 taksonomi rezim; juri T4
   dengan biaya sejak hari pertama; lapisan validasi (uji bulanan berpasangan +
   Sidak, ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy murni).
10. Utang lama menunggu tahap lain: 1, 2, 3, 4, 5, 11. **Adjudikasi riset tetap
    TERKUNCI sampai manifes semesta penuh terverifikasi.**

## RAMALAN YANG MENUNGGU ADJUDIKASI

| Ramalan | Isi |
|---|---|
| R-104 | simbol-bulan pecahan 1..7 = **17.187 ± 60**; total kedelapan = 19.598 |
| R-105 | total `simbol_bulan_gagal` pecahan 1..7 di pita **5..60** |
| R-106 | pelanggaran hanya `tanpa_menit_hilang` + `jarak_60_detik`; empat klausa lain nol; `cacah_simbol_bulan_dengan_baris_dibuang` 0..5 |
| R-110 | ketiga berkas harian tersedia (`cacah_hari_tersedia` = 3) |
| R-111 | `menit_hadir_di_harian_saat_bulanan_hilang` = **0** (H-A003 gugur) |
| R-112 | cacah baris harian **780 / 930 / 735** (AERGO / CVC / SLP) |

Lama menunggu: R-7, R-19, R-20, R-28, R-36, R-37.

**Papan skor R-1..R-109**: TEPAT **67**, MELESET **26**, SEPARUH **4**,
TIDAK TERADJUDIKASI **3**, MENUNGGU **9**. Jumlah 109 ✅.
Ramalan berikutnya **R-113**. N_percobaan = 0.

## PENOMORAN BERIKUTNYA

Jurnal berikutnya `journal/2026-07-28-50.md`. STATE berikutnya **v21**. PROMPT
berikutnya **v23**. ADR berikutnya **A007** (A003 masih dicadangkan dan belum
ada). Hipotesis: H-A001 (belum), H-A002a / H-A002b (selesai), **H-A003**
(sedang diuji). Aturan terakhir **37**. Kelas cacat terakhir **KC-14**; KC-15
dicadangkan untuk H-A003 bila menang.

## KEBIASAAN

- Tulis ramalan **sebelum** run, lalu adjudikasi jujur. 26 ramalan sudah
  MELESET; deret TEPAT panjang adalah tanda ramalan terlalu aman, bukan tanda
  makin pandai.
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21).
- Setiap pengukuran sebab wajib memuat medan yang bisa MENGGUGURKAN hipotesis
  yang dipercaya (aturan 24). Aturan 37: sampel wajib memuat ≥1 kasus tiap
  kelas cacat relevan, dan kelas yang kosong wajib disebut.
- Aturan 20: dilarang menyimpulkan di luar rentang yang disampel.
- **BACA berkas sebelum menuduhnya salah.** Pola "meramal dari ingatan lalu
  menuduh kode yang ternyata benar" sudah terjadi ENAM kali; penawarnya
  (membaca utuh dulu) bekerja setiap kali dipakai.
- Pisahkan fakta dari asumsi; tanpa bukti tulis "Ini memerlukan verifikasi."
- "lanjut" berarti teruskan tanpa konfirmasi.
- Perbarui STATE.md, jurnal, dan PROMPT_KELANJUTAN.md secara berkala. Jangan
  berhenti dengan alasan konteks Notion; patokannya konteks model. Ada tenggat:
  riset dipercepat sebelum **3 Agustus 2026**.
