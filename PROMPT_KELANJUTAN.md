# PROMPT KELANJUTAN — v30

Disusun 2026-07-29 (sesi 54). Berkas di repo adalah kebenaran; prompt ini hanya
peta. Bila prompt dan repo berbeda, REPO yang benar.

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`, dengan
   `owner` dan `repo` HANYA di dalam `toolArguments`, tidak di tingkat atas.
3. Baca dari `main` repo `EnVyxS/lux-ai-research` berurutan:
   `STATE.md` (**v27 — sekarang MUTAKHIR: memuat aturan 1–52, KC-18, papan skor
   197, cacah baris terukur, dan hasil kohort ekor V4**); lalu
   `journal/2026-07-29-76.md` dan `-77.md`; lalu `decisions/ADR-A006.md` dan
   `ADR-A007.md` (A007 masih DIUSULKAN); `ADR-A004.md` dan `ADR-A002.md` bila
   menyentuh serapan; `PETA_MODUL.md` bila menyentuh modul warisan.
4. Baru setelah itu jalankan pekerjaan teknis.

## BATASAN YANG MAHAL DIPELAJARI ULANG

- Sandbox agen TIDAK punya jaringan. Semua unduhan dan pengukuran arsip
  dijalankan GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- Tidak ada alat membaca status GitHub Actions dan tidak ada `workflow_dispatch`.
  Status hanya diketahui dari berkas laporan yang di-commit workflow itu sendiri,
  dan satu-satunya cara menyalakan run adalah push ke berkas yang tersebut di
  `paths` workflow.
- Tidak ada API patch — `push_files` menulis ulang seluruh isi berkas. Rancang
  berkas kecil; sesudah mendorong berkas panjang BACA ULANG dari `main` untuk
  memastikan ekornya hadir.
- Saat memeriksa hasil run, cocokkan `commit` / `run_id` / `sidik_kode`. Jangan
  percaya keberadaan berkas: laporan run lama sering masih terbaca. Kohort V4
  membuktikan ini lagi — status V3 masih terbaca sampai puluhan menit sesudah
  push V4.
- `search_code` mengembalikan 0 hasil (tidak berindeks). Pakai
  `get_file_contents`; path berakhiran garis miring melisting direktori.
- Runner punya numpy, pandas, pyarrow, pyyaml, pytest; TIDAK ada scipy dan
  requests. `data.binance.vision` bisa diakses; `fapi.binance.com` memberi 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. Repo `lux-research`
  boleh DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## POSISI (29 Juli 2026)

Rantai mutakhir: `14cbe1e9` (PROMPT v29) → `387037a9` (kohort_ekor V4) →
`796c2fc4` (ukur_baris V1) → jurnal 76 → jurnal 77 → STATE v27 + PROMPT v30.

Run terverifikasi terakhir:

- CI **30416988936**, commit `796c2fc4`, kode 0, **244 butir**.
- kohort ekor V4 **30416845475**, commit `387037a9`, kode 0,
  `sidik_kode` `73ca4eb2…`.
- ukur_baris V1 **30416988938**, commit `796c2fc4`, kode 0.

Papan skor R-1..R-197: **TEPAT 138 / MELESET 37 / SEPARUH 11 /
TIDAK TERADJUDIKASI 5 / MENUNGGU 6 = 197.** MENUNGGU = R-7, R-19, R-20, R-28,
R-36, R-37 (keenamnya ramalan riset lama).

Ramalan belum terpakai: **R-198**. Aturan terakhir **52**. Kelas cacat terakhir
**KC-18**. Jurnal berikutnya **78**. STATE berikutnya **v28**. PROMPT berikutnya
**v31**. ADR berikutnya **A008**.

## TEMUAN MUTAKHIR YANG MENENTUKAN ARAH

- **KC-18** — arsip menerbitkan klines 1m sempurna secara BENTUK (43.200 lilin,
  cap waktu rapat, checksum cocok) untuk pasar yang tidak diperdagangkan, dengan
  `volume` dan `count` nol. Gerbang 1m meloloskannya karena menilai BENTUK, bukan
  KEHIDUPAN. Terukur: 864.000 lilin pada 20 simbol-bulan; 169 simbol-bulan sepi
  pada pindaian adaptif. JANGAN diekstrapolasi ke 456.
- **Kohort mati bertahap, funding berhenti serempak.** Kesepuluh anggota yang
  disampel berhenti diperdagangkan antara 2024-06 dan 2025-04 pada sembilan
  bulan berbeda, sementara funding berhenti serempak 2025-07. Tebing funding
  lebih menyerupai perubahan rezim PENERBITAN daripada peristiwa pasar. Ini
  TIDAK membuktikan arsip funding cacat; ADR-A002 §10 tetap tidak boleh diubah
  atas bukti kohort semata.
- **Pindaian adaptif menutup jendela buta.** Pagu 60 bulan tak pernah tersentuh
  (terpanjang 25 bulan), `pagu_habis` dan `arsip_habis` sama-sama 0. Harganya:
  `bangkit_kembali` tidak lagi dapat digugurkan (`bangkit_dapat_diuji` 0).
- **`funding.py` 705 baris**, 95 di bawah pagar 800. Aturan 48: pecah lebih dulu
  sebelum menambah fungsi ke sana.

## PEKERJAAN BERIKUTNYA

1. **ADR-A008** — putuskan akibat KC-18 pada riset. Bahannya sudah ada. Pokok
   soal: lilin datar bukan data palsu, tetapi ia tidak boleh diam-diam menjadi
   PENYEBUT. Pertimbangkan medan `hidup` per simbol-bulan alih-alih penjatuhan.
2. **Terima atau tolak ADR-A007**, dengan kendala R-146: baris karantina yang
   digantikan harus dikurangi lebih dulu sebelum baris pulihan ditambahkan ke
   839.842.134.
3. **Perbaiki aturan 46 di `pulihkan.py`**: label `definisi_jumlah_baris` wajib
   berbunyi "tidak dapat dibedakan" ketika kedua `selisih` nol. Ini utang paling
   tua yang masih hidup, sudah ditunda lima jurnal berturut-turut.
4. **Terapkan ADR-A006** sepenuhnya.
5. Perluas kohort ekor ke **28 anggota sisanya** bila ingin klaim tingkat kohort;
   ingat aturan 20 dan biaya unduh (179 simbol-bulan untuk 10 simbol).
6. Ukur **bentangan penuh KC-18** atas 456 simbol-bulan.
7. `dugaan_pengganti` (ADR-A005); karantina artefak 7 hari; adjudikasi R-7,
   R-19, R-20, R-28, R-36, R-37.
8. Belum diukur: sebab KC-15; lubang funding BNXUSDT; 15 SETTLED lain; INDEKS 3
   nama manual; token saham/komoditas; simbol non-ASCII;
   `.decode("utf-8","replace")`; BUSD/USDC; jurang 38 lawan 41; skew `waktu_utc`;
   `funding_selisih_penuh.json`; selisih byte AGIX 531 lawan 529.
9. Paralel (aturan 3): ADR-A003; juri T4 dengan biaya; lapisan validasi (Šidák,
   ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy murni). **Adjudikasi riset
   TETAP TERKUNCI** sampai manifes semesta penuh terverifikasi.

## KEBIASAAN

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. Ramalan yang hanya dapat
  diuji pada sebagian kecil unitnya dicatat TIDAK TERADJUDIKASI, bukan TEPAT.
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21). Jangan
  menaksir cacah baris dari byte — dua kali kalah karena itu (R-175, R-179).
- Setiap pengukuran sebab wajib memuat medan penggugur (aturan 24), dibaca dan
  ditulis LEBIH DULU sebelum angka mana pun ditafsirkan.
- Aturan 47 satuan disebut eksplisit · 48 pecah sebelum menabrak pagar 800 ·
  49 re-export memindahkan fungsi bukan modul · 50 kesimpulan dari KETIADAAN
  wajib berkendali positif · 51 jendela mundur wajib adaptif · 52 laporan besar
  wajib berpasangan keluaran ringkas bersidik sumber.
- BACA berkas sebelum menuduhnya salah. Pola salah-tuduh sudah tercegah TUJUH
  kali; yang terakhir terhadap berkas sendiri (`timeout-minutes: 300` adalah
  menit, bukan detik).
- Pisahkan fakta dari asumsi. Tanpa bukti, tulis "Ini memerlukan verifikasi."
- "lanjut" berarti teruskan tanpa konfirmasi.
- Perbarui `STATE.md`, jurnal, dan `PROMPT_KELANJUTAN.md` secara berkala.
- Jangan berhenti dengan alasan konteks Notion; patokannya konteks model.
- Tenggat: riset dipercepat sebelum 3 Agustus 2026.
