# PROMPT KELANJUTAN v29 — LUX-AI

Disusun 2026-07-29 08:15 WIB, sesudah jurnal 75 (`3ef5bfa6`).
Berkas di repo adalah kebenaran. Prompt ini hanya peta.

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`.
   `owner` dan `repo` HANYA di dalam `toolArguments`, tidak di tingkat atas.
   (Kesalahan ini terjadi lagi pada 2026-07-29; jangan ulangi.)
3. Baca dari `main` repo `EnVyxS/lux-ai-research`, berurutan:
   - `PROMPT_KELANJUTAN.md` (v29, berkas ini)
   - `STATE.md` (v26 — aturan, kelas cacat, papan skor, daftar utang; PALING PENTING;
     PERINGATAN: STATE masih v26 dan tertinggal, aturan 51 dan 52 serta KC-18 baru
     ada di jurnal, belum di STATE)
   - `journal/2026-07-29-73.md`, `-74.md`, `-75.md`
   - `decisions/ADR-A006.md`, `ADR-A007.md` (DIUSULKAN, belum diterima)
   - `ADR-A004.md` dan `ADR-A002.md` bila menyentuh serapan
   - `PETA_MODUL.md` bila menyentuh modul warisan
4. Baru setelah itu jalankan pekerjaan teknis.

## BATASAN YANG MAHAL DIPELAJARI ULANG

- Sandbox agen TIDAK punya jaringan. Semua unduhan dan pengukuran arsip dijalankan
  GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- Tidak ada alat membaca status GitHub Actions dan tidak ada alat memicu
  `workflow_dispatch`. Status hanya diketahui dari berkas laporan yang di-commit
  workflow itu sendiri. Satu-satunya cara menyalakan run adalah push ke berkas yang
  tersebut di `paths` workflow.
- Tidak ada API patch. `push_files` menulis ulang seluruh isi berkas. Rancang berkas
  kecil. Sesudah mendorong berkas panjang, BACA ULANG dari `main` dan pastikan
  ekornya hadir.
- Saat memeriksa hasil run, cocokkan `commit` / `run_id` / `sidik_kode`. JANGAN
  percaya keberadaan berkas: laporan run lama sering masih terbaca. Pola ini muncul
  berkali-kali, termasuk hari ini.
- `search_code` mengembalikan 0 hasil (tidak berindeks). Pakai `get_file_contents`.
  Path berakhiran garis miring akan melisting direktori.
- Runner: numpy, pandas, pyarrow, pyyaml, pytest tersedia. TIDAK ada scipy dan
  requests. `data.binance.vision` bisa diakses; `fapi.binance.com` memberi 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. Repo `lux-research` boleh
  DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## POSISI (2026-07-29 08:15 WIB)

HEAD `3ef5bfa677fe99b86d60c8b00c334c5fa563acff` (jurnal 75).
Rantai commit terakhir: `099bcece` (kohort V2) → `1d1cc2c6` (jurnal 73) →
`805a0fdb` (jurnal 74) → `04d37031` (kohort V3) → `11383298` (kohort_ringkas V1) →
`3ef5bfa6` (jurnal 75).

CI terakhir terverifikasi: **239 butir, kode 0, run `30415870832`**, commit
`11383298`. Jurnal 75 belum dikonfirmasi CI — hanya berkas markdown, tetapi tetap
cocokkan commit sebelum percaya.

Papan skor sampai R-193: **TEPAT 134 / MELESET 37 / SEPARUH 9 /
TIDAK TERADJUDIKASI 5 / MENUNGGU 8 = 193**. MENUNGGU = R-7, R-19, R-20, R-28,
R-36, R-37, R-175, R-179. Ramalan berikutnya yang belum terpakai: **R-197**.
Aturan terakhir: **52**. Kelas cacat terakhir: **KC-18**. Jurnal berikutnya: **76**.
STATE berikutnya: **v27**. PROMPT berikutnya: **v30**. ADR berikutnya: **A008**.

## TEMUAN MUTAKHIR YANG MENENTUKAN ARAH

- **KC-18**: arsip menerbitkan klines 1m yang sempurna secara bentuk — 43.200 lilin,
  cap waktu rapat, checksum cocok — untuk pasar yang tidak diperdagangkan, dengan
  `volume` dan `count` nol pada setiap lilin. Gerbang 1m meloloskannya karena menilai
  BENTUK, bukan KEHIDUPAN. Bentangan terukur: 864.000 lilin pada 20 simbol-bulan.
  JANGAN diekstrapolasi ke 456 simbol-bulan kohort.
- **Jendela buta (jurnal 75)**: pemindaian mundur 15 bulan gagal mengukur
  `bulan_hidup_terakhir` pada 9 dari 10 simbol karena mereka sudah sepi sejak bulan
  paling awal jendela. Hanya **ALPACAUSDT** terukur: **2025-04**.
- **Tafsir tebing funding terbalik**: AGIXUSDT 2025-06 nol transaksi sebulan penuh
  padahal berkas funding-nya ada dan berisi 531 byte baris sungguhan. Funding terus
  terbit untuk pasar mati. Ini TIDAK membuktikan arsip funding cacat; penghentian
  penerbitan yang tertunda sama-sama muat. ADR-A002 §10 TIDAK boleh diubah atas
  bukti kohort semata.

## PEKERJAAN BERIKUTNYA (urutan disarankan)

1. **kohort_ekor VERSI 4 — pindaian adaptif.** Baca dulu
   `lux_ai/serapan/kohort_ekor.py` V3 utuh; jangan tulis ulang dari ingatan.
   Ubah pemindaian agar mundur simbol demi simbol sampai bulan ramai pertama
   ditemukan, pagu keras 60 bulan, `batas_tercapai` tetap ada sebagai penggugur.
   Push atomik bersama `tests/test_kohort_ekor.py` (aturan 45), cacah fungsi uji
   dengan MENGHITUNG, bukan menaksir (kegagalan "Tujuh vs Delapan").
   Ramalan sudah terdaftar: **R-194** (`cacah_simbol_batas_tercapai` jadi 0),
   **R-195** (kesepuluh bulan hidup terakhir sebelum 2025-07), **R-196** (CI 241, kode 0).
2. **Jurnal 76** dengan adjudikasi R-194..R-196.
3. **STATE v27 + PROMPT v30**: harus memuat aturan sampai 52, KC-18, papan skor 193+,
   modul `kohort_ekor` (V1→V4) dan `kohort_ringkas`, temuan CDN dan funding V6.
4. **Ukur cacah baris nyata** `funding.py` dan `funding_cdn.py` untuk menutup **R-175**
   dan **R-179**. Jangan menebak, jangan menyetel ulang pita.
5. **Perbaiki aturan 46 di `pulihkan.py`**: label harus "tidak dapat dibedakan" saat
   kedua `selisih` bernilai 0.
6. **Terima atau tolak ADR-A007**; bila diterima, terapkan `sumber_baris`,
   `cacah_baris_dipulihkan`, `cacah_hari_dipulihkan`, `cacah_simbol_bulan_dipulihkan`,
   dan tripwire `cacah_pemulihan_gagal_checksum` = 0. Kendala **R-146**: kurangi baris
   karantina yang digantikan sebelum menambah baris pulihan ke 839.842.134.
7. **Putuskan akibat KC-18 pada riset**: bolehkah lilin nol-volume masuk penyebut.
   Tulis ADR-A008. Jangan diputuskan dari bukti kohort saja.
8. **Terapkan ADR-A006**: medan karantina, persistensi parquet sebagai rilis tar
   terbelah ≤1,8 GB dengan SHA256SUMS. Sampai selesai, TIDAK ADA data serapan yang
   bertahan.
9. `dugaan_pengganti` (ADR-A005); karantina artefak 7 hari; adjudikasi R-7, R-19,
   R-20, R-28, R-36, R-37.
10. Belum diukur: sebab KC-15; apakah lubang funding BNXUSDT (2022-04…2023-01)
    berimpit dengan lubang klines-nya; 15 SETTLED lain; INDEKS 3 nama manual;
    token saham/komoditas; simbol non-ASCII tersisa; `.decode("utf-8","replace")`;
    BUSD/USDC; jurang 38 lawan 41; skew `waktu_utc`; baca
    `reports/funding_selisih_penuh.json` (daftar sebelumnya terpotong, 500 dari 880);
    selisih byte AGIX 531 lawan 529; bentangan penuh KC-18 pada 456 simbol-bulan.
11. Paralel diizinkan (aturan 3): ADR-A003; juri T4 dengan biaya; lapisan validasi
    (Šidák, ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy murni).
    **Adjudikasi riset TETAP TERKUNCI** sampai manifes semesta penuh terverifikasi.

## KEBIASAAN YANG WAJIB DIPERTAHANKAN

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. Ramalan yang hanya dapat diuji
  pada sebagian kecil unitnya dicatat TIDAK TERADJUDIKASI, bukan TEPAT.
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21).
- Setiap pengukuran sebab wajib memuat medan penggugur (aturan 24).
- Aturan 37: sampel wajib memuat ≥1 kasus tiap kelas cacat relevan.
- Aturan 20: dilarang menyimpulkan di luar rentang yang disampel.
- Aturan 50: setiap kesimpulan dari KETIADAAN wajib punya kendali positif yang
  membuktikan alatnya mampu melihat KEHADIRAN.
- Aturan 51: jendela mundur wajib adaptif atau terbukti mencakup peristiwanya.
- Aturan 52: laporan yang tak terbaca utuh setara dengan tak ada; sediakan keluaran
  ringkas bersidik sumber.
- BACA berkas sebelum menuduhnya salah. Pola salah-tuduh sudah tercegah TUJUH kali,
  yang terakhir terhadap berkas milik sendiri (`timeout-minutes: 300` adalah menit,
  bukan detik).
- Pisahkan fakta dari asumsi. Tanpa bukti, tulis "Ini memerlukan verifikasi."
- "lanjut" berarti teruskan tanpa konfirmasi.
- Perbarui STATE.md, jurnal, dan PROMPT_KELANJUTAN.md secara berkala.
- Jangan berhenti dengan alasan konteks Notion; patokannya konteks model.
- Tenggat: riset dipercepat sebelum **3 Agustus 2026**.
