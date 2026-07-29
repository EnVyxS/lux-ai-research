# PROMPT KELANJUTAN — v31

Disusun 2026-07-29 (sesi 54, lanjutan). Berkas di repo adalah kebenaran; prompt
ini hanya peta. Bila prompt dan repo berbeda, REPO yang benar.

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`, dengan
   `owner` dan `repo` HANYA di dalam `toolArguments`, tidak di tingkat atas.
3. Baca dari `main` repo `EnVyxS/lux-ai-research` berurutan:
   `STATE.md` (**v28 — MUTAKHIR: aturan 1–52, KC-18 beserta kebijakannya, papan
   skor 199, CI 253, `pulihkan` V2**); lalu `journal/2026-07-29-77.md` dan
   `-78.md`; lalu `decisions/ADR-A008.md` (DITERIMA 1–6) dan `ADR-A007.md`
   (masih DIUSULKAN); `ADR-A004.md` dan `ADR-A002.md` bila menyentuh serapan;
   `PETA_MODUL.md` bila menyentuh modul warisan.
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
  percaya keberadaan berkas: laporan run lama sering masih terbaca. Terjadi lagi
  sesudah push `5c65adf9` — laporan CI commit `789a6adf` (244 butir) masih
  terbaca beberapa menit, dan hanya pencocokan commit yang mencegah salah baca.
- `search_code` mengembalikan 0 hasil (tidak berindeks). Pakai
  `get_file_contents`; path berakhiran garis miring melisting direktori.
- Runner punya numpy, pandas, pyarrow, pyyaml, pytest; TIDAK ada scipy dan
  requests. `data.binance.vision` bisa diakses; `fapi.binance.com` memberi 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. Repo `lux-research`
  boleh DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## POSISI (29 Juli 2026)

Rantai mutakhir: `796c2fc4` (ukur_baris V1) → `458d2618` (jurnal 76) →
`1f189ca9` (jurnal 77) → `789a6adf` (STATE v27 + PROMPT v30) → `9d19140b`
(ADR-A008) → `5c65adf9` (pulihkan V2 + uji) → `805b2461` (jurnal 78) →
STATE v28 + PROMPT v31.

Run terverifikasi terakhir:

- CI **30417800419**, commit `5c65adf9`, kode 0, **253 butir**.
- kohort ekor V4 **30416845475**, commit `387037a9`, kode 0,
  `sidik_kode` `73ca4eb2…`.
- ukur_baris V1 **30416988938**, commit `796c2fc4`, kode 0.

Papan skor R-1..R-199: **TEPAT 139 / MELESET 37 / SEPARUH 11 /
TIDAK TERADJUDIKASI 5 / MENUNGGU 7 = 199.** MENUNGGU = R-7, R-19, R-20, R-28,
R-36, R-37 (ramalan riset lama) dan **R-199** (label
`definisi_dapat_dibedakan` pada delapan pecahan).

Ramalan belum terpakai: **R-200**. Aturan terakhir **52**. Kelas cacat terakhir
**KC-18**. Jurnal berikutnya **79**. STATE berikutnya **v29**. PROMPT berikutnya
**v32**. ADR berikutnya **A009**.

## TEMUAN MUTAKHIR YANG MENENTUKAN ARAH

- **KC-18 kini berkebijakan (ADR-A008, DITERIMA 1–6).** Lilin datar bukan data
  palsu; ia keterangan sah bahwa tidak ada perdagangan. Karena itu ia DILABELI,
  bukan dijatuhkan: **SEPI** bila `bagian_volume_nol` ≥ 0,5, **MATI** bila
  `transaksi_total` = 0. Setiap penyebut diterbitkan berpasangan (penuh dan
  tanpa MATI); backtest hanya pada simbol-bulan HIDUP; angka 839.842.134 TIDAK
  ditulis ulang. KC-18 tidak dijadikan gerbang serapan, sebab gerbang menilai
  BENTUK dan mencampur KEHIDUPAN ke sana membuat satu medan gagal karena dua
  sebab (aturan 24, 46).
- **Keputusan 7 ADR-A008 DITANGGUHKAN.** Nasib ADR-A002 §10 menunggu dua
  pengukuran: sifat 48 lubang funding AWAL dan 6 lubang TENGAH. Bukti kohort
  saja tidak cukup — ia 10 dari 38, dan arah sebabnya masih dua kemungkinan yang
  meramalkan data yang sama.
- **Aturan 46 LUNAS di kode.** `pulihkan.py` V2 menambahkan fungsi murni
  `putuskan_definisi` dan medan penggugur `definisi_dapat_dibedakan`. Utang ini
  ditunda enam jurnal; kode yang melahirkan aturan itu sendiri yang
  melanggarnya.
- **Laporan `reports/pulihkan_pecahan_<i>.json` masih hasil V1.** Label keliru
  pada pecahan 2 dan 5 masih terbaca di git. Cocokkan `versi_pulihkan` dan
  `sidik_kode` sebelum mempercayainya.
- **Kohort mati bertahap, funding berhenti serempak** (2024-06..2025-04 lawan
  2025-07). Tebing funding lebih menyerupai perubahan rezim PENERBITAN daripada
  peristiwa pasar — tetapi ini TIDAK membuktikan arsip funding cacat.
- **`funding.py` 705 baris**, 95 di bawah pagar 800. Aturan 48: pecah lebih dulu
  sebelum menambah fungsi ke sana.

## PEKERJAAN BERIKUTNYA

1. **Terapkan ADR-A008 Keputusan 2–4**: modul pengukur kehidupan per
   simbol-bulan atas SEMESTA (bukan hanya 10 simbol), menerbitkan `cacah_lilin`,
   `cacah_volume_nol`, `bagian_volume_nol`, `transaksi_total`, `volume_total`,
   plus penyebut kedua tanpa simbol-bulan MATI. Ini sekaligus mengukur bentangan
   penuh KC-18 atas 456 simbol-bulan.
2. **Adjudikasi R-199** ketika `pulihkan` V2 dijalankan ulang atas kedelapan
   pecahan. Ingat biayanya: run itu mengunduh puluhan gigabyte aset rilis.
3. **Terima atau tolak ADR-A007**, dengan kendala R-146: baris karantina yang
   digantikan harus dikurangi lebih dulu sebelum baris pulihan ditambahkan ke
   839.842.134. Baca ulang adjudikasi tepi bulan (R-117..R-120) lebih dulu —
   jangan memutuskan dari ingatan.
4. **Terapkan ADR-A006** sepenuhnya.
5. Perluas kohort ekor ke **28 anggota sisanya** bila ingin klaim tingkat
   kohort; ingat aturan 20 dan biaya unduh (179 simbol-bulan untuk 10 simbol).
6. Ukur sifat **48 lubang funding awal dan 6 lubang tengah** — penentu
   Keputusan 7 ADR-A008.
7. `dugaan_pengganti` (ADR-A005); karantina artefak 7 hari; adjudikasi R-7,
   R-19, R-20, R-28, R-36, R-37.
8. Belum diukur: sebab KC-15; lubang funding BNXUSDT; 15 SETTLED lain; INDEKS 3
   nama manual; token saham/komoditas; simbol non-ASCII;
   `.decode("utf-8","replace")`; BUSD/USDC; jurang 38 lawan 41; skew `waktu_utc`;
   `funding_selisih_penuh.json`; selisih byte AGIX 531 lawan 529; cacah baris
   `pulihkan.py` V2.
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
