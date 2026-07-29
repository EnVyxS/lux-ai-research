# STATE lampiran ADR — ekor v41

**Mengapa berkas ini ada.** Push `STATE.md` v41 TERPOTONG di tengah kalimat pada
bagian "Utang verifikasi" butir 24 ("… kini cacahnya diketahui,"). Tidak ada API
tambal: `push_files` menulis ulang seluruh berkas, jadi memperbaiki `STATE.md`
berarti mengirim ulang seluruh isinya. Agar tidak ada satu pun isi yang hilang
sementara itu, ekor yang terpotong dituliskan di sini UTUH dan diperbarui ke
keadaan v41. Teks v40 yang menjadi dasarnya dapat dibaca pada blob
**`86c68a664603c548c39132aaa4d47605f0c84f9b`**.

**Status:** berlaku bersama `STATE.md` v41 (papan skor **294**, aturan sampai
**76**, KC sampai **KC-40**). `STATE.md` v42 wajib menyerap kembali isi berkas ini
ATAU menyebutnya tersurat sebagai lampiran yang mengikat. Kelalaian ini dicatat
sebagai kesalahan penulis, bukan kesalahan data (aturan 29: teks yang sudah
didorong tidak disunting diam-diam).

## Utang verifikasi 24 — lanjutan daftar BELUM

Sambungan kalimat yang terpotong: **TANGGAL** hari-hari yang hilang pada ketiga
bulan BNXUSDT — kini cacahnya diketahui (1.650 / 1.440 / 4.320 menit) tetapi
tanggal UTC-nya belum; berikutnya:

- selisih 40 − 38 sampel `diagnosa_kc15`
- `ukur_baris` **V6** (KC-26 + enam belas berkas belum terukur)
- peninjauan `funding.py` / `silang_funding.py` (705 baris, SERI)
- daftar **147** nama hanya-arsip
- identitas **18** simbol tanpa bulan HIDUP
- kehidupan kedua belas simbol-bulan karantina — **catatan v41:** status
  MATI/SEPI/HIDUP tidak dapat ada bagi mereka, sebab mereka DI LUAR penyebut
  19.586; yang dapat diukur hanyalah lilin di dalam berkas karantinanya
- `funding_ada` masih null di seluruh manifes
- `dugaan_pengganti` (ADR-A005)
- pemulihan harian ADR-A007; karantina artefak 7 hari
- 28 anggota kohort di luar sampel abjad
- **bunyi ramalan R-28 dari STATE v23 (KC-32)**
- tiga nama ekor 2026-04; keberadaan `POLUSDT` di dalam 787; asal-usul hantu
  "16 non-ASCII"
- **`.github/workflows/karantina_semesta.yml` belum dibaca ulang sesudah push**
- `lux_ai/semesta/taksonomi.py` (blob `b418c7ba`) belum dibaca ulang — premis
  "taksonomi beroperasi atas 937 nama arsip" tetap **ASUMSI**
- `decisions/ADR-A002.md`, `ADR-A004.md`, `ADR-A006.md`, `ADR-A007.md`,
  `ADR-A008.md`, dan `PETA_MODUL.md` belum dibaca ulang pada sesi ini
- **H-A016 belum diuji** atas simbol-bulan yang LOLOS gerbang
- laporan yang belum pernah dibaca utuh: `bulan_absen.json` penuh (249.992 B),
  `karantina_semesta.json` penuh, `semesta_rentang.json` (110.662 B, **tak
  bersidik**), `ringkas_semesta.json`, `survei_semesta.json`,
  `survei_progres.json`, `rentang_kc6.json`, `semesta_kuota.json` penuh,
  `semesta_silang.json` penuh, `penyebut_tahun.json` penuh, `kohort_ekor.json`,
  `funding_semesta.json` penuh, `funding_selisih_penuh.json`
  (`daftar_terpotong` true, 500 dari 880), `hidup_tanpa_funding.json`,
  `tests/test_pulihkan.py`, `tests/test_rilis_karantina.py`,
  `tests/test_karantina_a006.py`
- **MUSTAHIL dibaca agen:** `reports/manifes_pecahan_*.json` (pecahan 2 berukuran
  2.446.093 B, blob `c0be6ecf…`, DITOLAK alat baca) — hanya lewat modul di runner

Cacat penulisan yang dicatat dan TIDAK disunting: docstring R-225 ("tujuh fungsi"
lalu sembilan nama) dan docstring `penyebut_tahun.py` (`TLMUSDT_SETTLED`).
Mengadjudikasi R-7, R-19, R-20, R-28, R-36, R-37.

## Daftar ADR

- **ADR-A001** aturan dasar. DITERIMA.
- **ADR-A002** serapan. DITERIMA; §3 DIAMANDEMEN oleh A004 lalu A007; §9 DIGANTI
  oleh A006 Keputusan 3. **§10 belum disentuh dan tetap tidak boleh disentuh atas
  bukti kohort semata;** bila kelak disunting, WAJIB menyebut batas
  `perpetual_usdt`. Dua gejala bebas yang menyokong H-A015 TIDAK cukup untuk
  menyentuhnya — keduanya soal penamaan dan penerbitan, bukan perdagangan (KC-18).
  **[v41] Bukti bulan karantina berlilin SEBAGIAN (nisbah 0,903–0,990) juga TIDAK
  cukup:** ia menunjukkan berkas tidak utuh, bukan bahwa perdagangan berhenti.
- **ADR-A003** taksonomi rezim. BELUM ADA (nomor dicadangkan). Wajib memisahkan
  "kontrak berganti nama" dari "pasar hidup kembali", wajib memakai taksonomi
  INSTRUMEN kanonik (KC-29), wajib memuat aturan 68, wajib memuat kebangkitan
  LITUSDT beserta aturan 74, wajib memuat bulan ABSEN sebagai kelas gejala
  tersendiri beserta aturan 76, dan **[v41] wajib memuat KC-40** — sebab kelas
  gejala itu dikenali dari medan `pelanggaran` yang bermakna terbalik.
- **ADR-A004** kebijakan KC-6. DITERIMA. Penggugurnya tetap tidak menyala:
  `cacah_gerbang_lolos_padahal_tepi_terpotong` = 0 atas 37 bulan tengah.
  **[v41] Gerbang §2 kini terbaca dari kode** (`gerbang_1m.py` blob `c8cc54c8`):
  enam klausa, dan `menit_hilang_dalam_rentang` dihitung atas rentang yang ADA di
  berkas, sengaja bukan atas bulan kalender.
- **ADR-A005** jenis instrumen tahap pertama. DITERIMA.
- **ADR-A006** karantina + persistensi. DITERIMA, DITERAPKAN, TERVERIFIKASI DARI
  LUAR. **[v41] Verifikasi terkuat sampai kini:** kedua belas berkas karantina ADA,
  `cacah_tanpa_parquet_karantina` **0**, `cacah_dibuang` **0**, `cacah_ditambal`
  **0**, `jumlah_karantina_tak_terkemas` **0**, dan byte totalnya **13.247.705**
  sama dengan angka KC-17 — jadi karantina yang dulu lenyap sebelum `pecahan.py`
  VERSI 6 kini terbukti dipersistenkan.
- **ADR-A007** serapan hibrida. **DIUSULKAN**, belum diterima; wajib
  memperhitungkan temuan `jumlah_baris` dan kendala R-146. Bahan yang
  menguatkannya: 7.200 menit KC-15 UTUH di arsip HARIAN; kesebelas bulan absen ADA
  di arsip (`tak_diterbitkan_arsip` 0). **[v41] Bahan baru yang MEMPERKUAT lagi:**
  bulan karantina rata-rata hanya kehilangan 1–10% menitnya, jadi pemulihan dari
  arsip harian berpeluang besar mengembalikannya ke penyebut — dan itu akan
  MENGUBAH 19.586. Perubahan penyebut DILARANG dilakukan tanpa ADR (aturan 30, 44).
- **ADR-A008** akibat KC-18. **Keputusan 1–6 DITERIMA [v28]**; Keputusan 5
  bersemesta 18.087. **Keputusan 7 BERCABANG DUA, kedua cabangnya bernama:**
  **LITUSDT** (lubang tengah berentetan **5**, MATI seluruhnya, bulan **2025-12
  ABSEN** dengan 43.590 dari 44.640 menit, lalu **BANGKIT** terukur) lawan
  **BTCSTUSDT** (lubang tengah **TUNGGAL** 2022-01, `cacah_lilin` 44.640 PENUH,
  **tanpa bulan absen**, **tidak ada di daftar karantina**, tetap MATI, 53 dari 53).
  Keputusannya WAJIB memuat kedua cabang, WAJIB per simbol-bulan, DILARANG
  menyebut funding dan perdagangan berhenti "serentak", WAJIB menyebut batas
  `perpetual_usdt`, WAJIB memakai aturan 66 revisi, 67, 68, 74, 76, dan **DILARANG
  diambil sebelum BTCSTUSDT 2022-01 dianatomi seperti BNXUSDT 2022-04**. R-276
  mengikat: tak ada peralihan yang terbukti. R-278 mengikat: 13 / 2 / 0.
- **ADR berikutnya A009.**

## Temuan sampingan yang belum diukur

- **Anatomi BTCSTUSDT 2022-01** — pekerjaan teknis paling berharga yang tersisa,
  dan satu-satunya prasyarat tersurat Keputusan 7 ADR-A008.
- **Uji H-A016** (celah kelipatan 15 menit) atas simbol-bulan yang LOLOS gerbang;
  penyebutnya harus dipilih hati-hati sebab gerbang menolak bulan bercelah.
- **TANGGAL** hari-hari yang hilang pada BNXUSDT 2022-04 / 2022-06 / 2022-08 —
  cacahnya sudah terukur, tanggalnya belum.
- Irisan **880 lawan 877**; selisih 40 − 38 sampel `diagnosa_kc15`.
- Tiga nama ekor 2026-04; mengapa `SXPUSDT` berhenti 2026-05; apakah `POLUSDT` ada
  di 787; asal-usul hantu "16 non-ASCII".
- Daftar 147 nama hanya-arsip; 18 simbol tanpa bulan HIDUP.
- Apakah 50 kontrak delivery bertanggal pernah masuk perhitungan mana pun.
- Mengapa penamaan SETTLED datang berombak pada 2023-02 dan 2025-07, dan mengapa
  2025-07 juga bulan tebing funding dan kohort puncak.
- Sebab kebangkitan/peralihan kedelapan simbol (di luar jangkauan arsip).
- Saham, ETF, dan komoditas token masih terhitung `perpetual_usdt`.
- `.decode("utf-8","replace")` di `klines` membungkam byte rusak.
- Apakah BUSD/USDC layak digabung dengan USDT (80 nama, 1.705 bulan).
- Sebab KC-14 (H-A004) tak dapat diuji; sebab KC-15 tidak diketahui — **[v41]
  meski pembagiannya kini terukur, SEBABNYA tetap tidak diketahui.**
- Selisih byte funding AGIXUSDT 531 lawan 529; `waktu_utc` runner berjalan lebih
  dulu daripada jam sesi; satuan stempel mikro lawan mili.
- `tests/test_pulihkan.py`, `tests/test_rilis_karantina.py`, dan
  `tests/test_karantina_a006.py` belum pernah dibaca.
