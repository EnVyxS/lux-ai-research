# PROMPT KELANJUTAN v23 — LUX-AI

Disusun 2026-07-28 sesi 50. Menggantikan v22 (`6af0b252`).
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
   `STATE.md` (v21 — aturan 1-38, KC-1..KC-14, H-A001..H-A004, papan skor,
   daftar karantina, daftar utang; INI YANG PALING PENTING);
   `journal/2026-07-28-50.md` (semesta penuh + adjudikasi terakhir);
   `journal/2026-07-28-49.md` bila menyentuh KC-14;
   `decisions/ADR-A006.md`; `ADR-A004.md` dan `ADR-A002.md` bila menyentuh
   serapan; `ADR-A005.md` bila menyentuh semesta; `PETA_MODUL.md` bila menyentuh
   modul warisan.
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
- Saat memeriksa hasil run, **cocokkan `run_id` / `sidik_kode` / blob sha**;
  jangan percaya keberadaan berkas — laporan run lama sering masih terbaca.
- Manifes pecahan sangat besar (2,0–2,5 MB). Baca ringkasannya lewat
  `reports/pecahan_<i>.log`, bukan `reports/manifes_pecahan_<i>.json`.
- `search_code` mengembalikan 0 hasil di repo ini. Pakai `get_file_contents`.
- Runner: numpy, pandas, pyarrow, pyyaml, pytest tersedia; TIDAK ada scipy dan
  requests. `data.binance.vision` bisa diakses; `fapi.binance.com` → 451.
- Cacah uji hanya sah dari `reports/ci_terakhir.json` (aturan 38). Taksiran di
  kepala sudah meleset: v22 menulis 135, CI melaporkan **141**.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. `lux-research` boleh
  DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## POSISI (2026-07-28 sesi 50)

Rantai giliran terakhir: `f50b9f40` (diagnosa_kc14b) → `6af0b252` (PROMPT v22)
→ run bot pecahan 1..7 (`30358650719`) → **jurnal 50** → **diagnosa_kc14c +
uji + workflow** → **STATE v21 + PROMPT v23** (commit ini).

Uji **141 TERVERIFIKASI** (run `30359672326`, commit `6af0b252`, kode 0);
setelahnya +8 uji `tests/test_diagnosa_kc14c.py`, menunggu laporan CI.

### SEMESTA `perpetual_usdt` SUDAH TERUKUR PENUH

787 simbol · **19.598 simbol-bulan** · **839.842.134 baris** · 0 gagal unduh ·
0 gagal checksum · 0 baris dibuang · zip 26,53 GB · parquet 32,71 GB ·
nisbah 1,2327 · gerbang lolos 19.586, GAGAL **12**, `persen_lolos` 99,9388 ·
menit hilang 13.575. Rincian per pecahan ada di STATE v21.
**Parquet TIDAK dipersistenkan** — semua ini masih angka tanpa data.

### KC-14 dan sebabnya

12 simbol-bulan dikarantina (daftar lengkap di STATE v21), semuanya pada klausa
`tanpa_menit_hilang` + `jarak_60_detik`. Empat klausa format nol → ADR-A004
berdiri. H-A002b GUGUR. **H-A003 (cacat perakitan bulanan) GUGUR**: berkas
harian ketiga tersangka berisi 1440 − panjang_lubang baris dan mulai tepat saat
lubang berakhir. **H-A004 (cacat di hulu arsip) TIDAK TERUJI** dan tidak dapat
diuji tanpa sumber non-arsip (`fapi` 451). Dilarang menulis "lubang itu jeda
pasar" sebagai fakta. KC-15 masih dicadangkan.

### SATU RUN SEDANG BERJALAN

**Diagnosa KC-14c** (dipicu commit `diagnosa_kc14c.py`) → `reports/diagnosa_kc14c.json`,
`.log`, `_status.json`. Sembilan tersangka baru; lubang ditemukan sendiri dari
berkas bulanan lalu dibanding berkas HARIAN per TANGGAL UTC. Perkiraan beberapa
menit sampai ±20 menit.

## PEKERJAAN BERIKUTNYA, BERURUTAN

1. **Baca `reports/diagnosa_kc14c.json`** (cocokkan `sidik_kode` dan
   `_status.json`) → adjudikasi **R-113, R-114, R-115, R-116**.
   - `menit_hadir_di_harian_saat_bulanan_hilang` > 0 pada tersangka mana pun →
     **namai KC-15**, arsip bulanan cacat, seluruh serapan berbasis berkas
     bulanan wajib ditinjau, amandemen ADR-A002 (pindah ke berkas harian).
   - `cacah_pecahan_tak_cocok` > 0 → aritmetika gerbang dan hitungan lubang
     berselisih; keduanya wajib diperiksa sebelum dipakai (aturan 36).
2. **Terapkan ADR-A006 ke kode** — ini penghalang terbesar sekarang:
   (a) medan `karantina`, `cacah_karantina`, `daftar_karantina` di
   `serap.ringkas` (baca `lux_ai/serapan/serap.py` UTUH lebih dulu);
   (b) persistensi parquet sebagai rilis tar terbelah ≤1,8 GB + `SHA256SUMS`,
   satu rilis per pecahan, nomor rilis mengikat `sidik_kode` + `sidik_data`.
   Tanpa (b) setiap serapan ulang membakar ±1,5 jam runner untuk angka saja.
3. **Jalur funding**: `funding_ada` masih null di seluruh manifes (ADR-A002 §9).
   Medan `dugaan_pengganti` (ADR-A005) juga belum ada.
4. **Jurnal 51 + STATE v22 + PROMPT v24** setelah adjudikasi 1 dan 2.
5. Sisa utang 24: karantina artefak 7 hari. Mengadjudikasi R-7, R-19, R-20,
   R-36, R-37.
6. Belum diukur: 15 `SETTLED` lain; kelengkapan `INDEKS` (3 nama manual);
   pemisahan saham/komoditas token dari 787 perpetual_usdt; keamanan
   `arsip.bulan_tersedia` untuk simbol Tionghoa; `.decode("utf-8","replace")`;
   apakah BUSD/USDC layak digabung dengan USDT; pola BNXUSDT 2022 (7.200 menit,
   tiga bulan, satu-satunya tersangka pra-2023).
7. Paralel, boleh kapan saja (aturan 3): ADR-A003 taksonomi rezim; juri T4
   dengan biaya sejak hari pertama; lapisan validasi (uji bulanan berpasangan +
   Sidak, ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy murni).
8. Utang lama menunggu tahap lain: 1, 2, 3, 4, 5, 11. **Adjudikasi riset tetap
   TERKUNCI sampai data serapan benar-benar bertahan (butir 2b).** Manifes
   semesta sendiri sudah terverifikasi.

## RAMALAN YANG MENUNGGU ADJUDIKASI

| Ramalan | Isi |
|---|---|
| R-113 | total menit hilang 9 tersangka = **11.700**; per pecahan 2.160 / 615 / 1.050 / 7.200 / 675 untuk pecahan 1 / 3 / 4 / 6 / 7 |
| R-114 | `menit_hadir_di_harian_saat_bulanan_hilang` = **0** untuk kesembilan (H-A003 tetap gugur) |
| R-115 | ≥ **6 dari 9** tersangka: SELURUH bloknya mulai tepat 00:00 UTC; ≥ **8 dari 9**: total menit hilang kelipatan 15 |
| R-116 | `cacah_hari_tidak_tersedia` = **0**, termasuk untuk hari yang lenyap penuh dari berkas bulanan |

Lama menunggu: R-7, R-19, R-20, R-28, R-36, R-37.

**Papan skor R-1..R-112**: TEPAT **73**, MELESET **26**, SEPARUH **4**,
TIDAK TERADJUDIKASI **3**, MENUNGGU **6**. Jumlah 112 ✅.
Ramalan berikutnya **R-117**. N_percobaan = 0.

## PENOMORAN BERIKUTNYA

Jurnal berikutnya `journal/2026-07-28-51.md`. STATE berikutnya **v22**. PROMPT
berikutnya **v24**. ADR berikutnya **A007** (A003 dicadangkan, belum ada).
Aturan terakhir **38**. Kelas cacat terakhir **KC-14**; KC-15 dicadangkan.
Hipotesis: H-A001 belum, H-A002a/b selesai, H-A003 gugur, **H-A004 tak teruji**.

## KEBIASAAN

- Tulis ramalan **sebelum** run, lalu adjudikasi jujur. 26 ramalan sudah
  MELESET; deret TEPAT panjang adalah tanda ramalan terlalu aman. Pada sesi 50
  ada enam TEPAT beruntun, tetapi tiga di antaranya nyaris aritmetika.
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21).
- Setiap pengukuran sebab wajib memuat medan yang bisa MENGGUGURKAN hipotesis
  yang dipercaya (aturan 24). Aturan 37: sampel wajib memuat ≥1 kasus tiap
  kelas cacat relevan, dan kelas yang kosong wajib disebut.
- Aturan 20: dilarang menyimpulkan di luar rentang yang disampel. Kedua belas
  tersangka bukan sampel dari 19.586 yang LOLOS.
- **BACA berkas sebelum menuduhnya salah.** Pola "meramal dari ingatan lalu
  menuduh kode yang ternyata benar" sudah terjadi ENAM kali; penawarnya bekerja
  setiap kali dipakai.
- Pisahkan fakta dari asumsi; tanpa bukti tulis "Ini memerlukan verifikasi."
- "lanjut" berarti teruskan tanpa konfirmasi.
- Perbarui STATE.md, jurnal, dan PROMPT_KELANJUTAN.md secara berkala. Jangan
  berhenti dengan alasan konteks Notion; patokannya konteks model. Ada tenggat:
  riset dipercepat sebelum **3 Agustus 2026**.
