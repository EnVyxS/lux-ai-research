# PROMPT KELANJUTAN — versi 35

Disusun 29 Juli 2026, 15:10 WIB, di atas STATE **v32** (commit `509fd63e`) serta
jurnal 85 dan 86. Berkas di repo adalah kebenaran; prompt ini hanya peta.

Kamu melanjutkan riset LUX-AI. Operator: Diva Juan Nur Taqarrub, GitHub EnVyxS,
zona waktu Asia/Jakarta, bahasa kerja Indonesia. Jangan mulai bekerja sebelum
menyelesaikan LANGKAH 0.

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`, dengan
   `owner` dan `repo` HANYA di dalam `toolArguments`, tidak di tingkat atas.
3. Baca dari `main` repo `EnVyxS/lux-ai-research` berurutan: berkas ini,
   `STATE.md` (**v32** — aturan 1–57, kelas cacat sampai KC-19, papan skor
   R-1..R-219, daftar utang; INI YANG PALING PENTING dan TIDAK tertinggal dari
   jurnal), `journal/2026-07-29-86.md`, lalu `-85.md`; `decisions/ADR-A008.md`
   (DITERIMA 1–6, Keputusan 7 ditangguhkan — syaratnya kini SETENGAH terpenuhi),
   `decisions/ADR-A007.md` (masih DIUSULKAN), lalu `ADR-A004.md` dan
   `ADR-A002.md` bila menyentuh serapan (§10 BELUM disentuh),
   `PETA_MODUL.md` bila menyentuh modul warisan.
4. Baru setelah itu jalankan pekerjaan teknis.

## BATASAN YANG MAHAL DIPELAJARI ULANG

- Sandbox agen TIDAK punya jaringan. Semua unduhan dan pengukuran arsip
  dijalankan GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- Tidak ada alat membaca status GitHub Actions dan tidak ada alat memicu
  `workflow_dispatch`. Status hanya diketahui dari berkas laporan yang
  di-commit workflow itu sendiri, dan satu-satunya cara menyalakan run adalah
  push ke berkas yang tersebut di `paths` workflow. Manfaatkan ini: memperbaiki
  BERKAS UJI tidak menyalakan ulang runner berat, sebab `paths` hanya memuat
  modulnya.
- **Aturan 55:** `.github/workflows/ci.yml` memakai `paths-ignore` untuk
  `journal/**`, `decisions/**`, `hipotesis/**`, dan `reports/**`. Commit yang
  HANYA menyentuh jurnal atau ADR **tidak menyalakan CI sama sekali** (R-209 dan
  R-212 hangus karena ini). `STATE.md` dan `PROMPT_KELANJUTAN.md` ada di AKAR,
  jadi keduanya MENYALAKAN CI.
- **Aturan 56 (BARU):** ramalan wajib menyebut sasaran yang keberadaannya
  dijamin cara kerjamu sendiri — bentuknya "commit BERIKUTNYA yang menyentuh
  `<berkas>`". Menyebut satu commit bermuatan dua berkas DILARANG kecuali
  push-nya dirancang atomik sejak ramalan ditulis. R-216 jatuh ke SEPARUH karena
  ini.
- **Aturan 57 (BARU) dan KC-19:** cacah butir uji hanya sah bila nama setiap
  fungsi `def test_` ditulis BERNOMOR lebih dulu. Tiga ramalan sudah gugur
  dengan sebab yang sama (R-148, R-211, R-217) — semuanya karena mencacah di
  kepala sambil menulis berkasnya. Aturan 54 saja tidak cukup.
- Tidak ada API patch — `push_files` menulis ulang seluruh isi berkas. Rancang
  berkas kecil, dan sesudah mendorong berkas panjang BACA ULANG dari `main`
  untuk memastikan ekornya hadir (aturan 52). Berkas laporan besar wajib
  berpasangan dengan berkas KECIL: pola itu terbukti pada
  `reports/hidup_tanpa_funding.json`, yang terbaca utuh sementara laporan penuh
  183.963 B tidak akan pernah terbaca utuh.
- Saat memeriksa hasil run, cocokkan `commit` / `run_id` / `sidik_kode`. Jangan
  percaya keberadaan berkas: laporan run lama sering masih terbaca.
- Laporan yang belum terbit menjawab "path does not point to a file" — itu bukan
  kegagalan push, melainkan run yang masih berjalan. Melisting `reports/`
  (path berakhiran garis miring) lebih murah daripada menebak nama berkas.
- `search_code` mengembalikan 0 hasil (tidak berindeks) — pakai
  `get_file_contents`.
- Runner punya numpy, pandas, pyarrow, pyyaml, pytest; TIDAK ada scipy dan
  requests. `data.binance.vision` bisa diakses; `fapi.binance.com` memberi 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. Repo `lux-research`
  boleh DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## POSISI (29 Juli 2026, 15:10 WIB)

Rantai commit mutakhir: `9819d76b` (STATE v31) → `dce890eb` (PROMPT v34) →
**`667d8d21`** (jurnal 85) → **`b1816ddf`** (silang_funding **V2**: modul + uji +
workflow, ATOMIK) → `88f0b51a` (commit laporan runner) → **`ad0d8c4e`**
(jurnal 86) → **`509fd63e`** (STATE v32) → berkas ini.

Run terverifikasi (commit dicocokkan):

- **silang_funding V2** — run **30434948267**, commit `b1816ddf`, kode 0,
  `sidik_kode` `8a9b859c…31b1`; `reports/hidup_tanpa_funding.json` blob
  `a7b20503` dibaca UTUH; `selisih_hidup_tanpa_funding` 0,
  `selisih_lubang_tak_dikenal` 0.
- **CI 30434951202** (`b1816ddf`) — **340 butir, kode 0**.
- **CI 30434140732** (`9819d76b`) — 316 butir, kode 0 (dasar R-216).
- ukur_baris V3 pada `67ec2be4` — 12 berkas, 3.885 baris, 0 lewat pagar.

Papan skor sampai R-219: **TEPAT 152 / MELESET 40 / SEPARUH 13 / TIDAK
TERADJUDIKASI 7 / MENUNGGU 7 = 219** (MENUNGGU: R-7, R-19, R-20, R-28, R-36,
R-37, R-199). Ramalan berikutnya **R-221** — R-220 dipraregistrasi di bawah.
Aturan terakhir **57**, kelas cacat terakhir **KC-19**, hipotesis terakhir
**H-A010 (LAHIR, BELUM DIUJI)**, jurnal berikutnya **87**, STATE berikutnya
**v33**, PROMPT berikutnya **v36**, ADR berikutnya **A009**.

**R-220, dipraregistrasi di sini (aturan 26, 38, 55, 56).** Pada commit
BERIKUTNYA yang menyentuh `PROMPT_KELANJUTAN.md` — yakni commit yang memuat
berkas ini — `ci.yml` MENYALA (berkas ada di akar, tidak tersentuh
`paths-ignore`), dan `reports/ci_terakhir.json` akan melaporkan **340 butir**
dengan `kode_keluar` **0**. Dasarnya: tidak ada berkas uji maupun modul yang
berubah pada commit ini, dan 340 sudah terverifikasi pada run 30434951202.
Aturan 57 tidak perlu daftar bernomor di sini sebab angkanya diambil dari
laporan CI terverifikasi, bukan dari cacahan sendiri.

## TEMUAN MUTAKHIR YANG MENENTUKAN ARAH

1. **Ke-33 simbol-bulan HIDUP tanpa funding sudah BERNAMA, dan bentuknya
   seragam.** `sebaran_bentuk_hidup_tanpa_funding` = **awal 33, ekor 0, tengah
   0, seluruh 0**. Lima simbol saja: ICPUSDT 13 (2021-05..2022-05), TLMUSDT 11
   (2021-07..2022-05), BNXUSDT 7 (2022-05, -07, -09, -10, -11, -12, 2023-01),
   JUPUSDT 1 (2024-01), QTUMUSDT 1 (2020-02). 13+11+7+1+1 = 33 ✅
2. **Tafsirnya, dengan batasnya.** Bentuk AWAL sepenuhnya, tanpa satu pun ekor
   atau tengah, adalah bentuk yang diharapkan bila penerbitan funding MENYUSUL
   penerbitan klines — bukan bentuk "funding berhenti". Karena itu kelompok 33
   BUKAN kelas cacat (aturan 42) dan BUKAN alasan mengubah ADR-A002 §10; ia
   justru MENGURANGI alasan itu. Yang belum diukur: tanggal mulai penerbitan
   funding per simbol — lihat **H-A010**.
3. **Ketiga lubang tak dikenal bernama: BNXUSDT 2022-04, 2022-06, 2022-08**,
   ketiganya bersimbol DIKENAL. Ini menutup jurang dua definisi: bentuk lokal
   atas 877 = {awal 45, ekor 826, tengah 6}; terbitan `funding.py` atas 880 =
   {awal 48, ekor 826, tengah 6}; selisih tepat 3 ✅
4. **Sisa yang benar-benar tak terjelaskan tinggal 6 lubang TENGAH.** Itulah
   satu-satunya penghalang Keputusan 7 ADR-A008 sekarang, dan itulah pekerjaan
   nomor satu.
5. **Medan baris laporan kehidupan akhirnya diketahui** (14 medan, termasuk
   `cacah_lilin` yang ADA pada seluruh 19.586 baris). Jangan menebak nama medan;
   `baca_medan_baris` di `silang_funding` V2 mencatat `medan_baris_terlihat` dan
   menghasilkan null tanpa menggugurkan apa pun — pola itu layak dipakai ulang.
6. **Dua arah irisan tetap wajib dipisah:** lubang → mati 96,0% (842/877) KUAT;
   mati → lubang 60,1% (842/1.401) LEMAH. Irisan BUKAN sebab (aturan 10).
7. **Tiga cacat prosedural berturut lahir dari SATU kebiasaan:** R-216 (SEPARUH,
   commit sasaran tak pernah ada → aturan 56) dan R-217 (MELESET, 335 lawan 340
   → aturan 57 + KC-19). Angka ramalan yang sudah didorong TIDAK boleh disunting
   belakangan; kesalahan R-217 saya temukan sendiri sebelum laporan CI terbaca
   dan tetap dicatat MELESET.

## PEKERJAAN BERIKUTNYA

1. **Nama keenam lubang funding TENGAH.** Bahannya sudah ada di repo tanpa
   unduhan baru: `reports/funding_semesta.json` (per simbol
   `klines_tanpa_funding`, `mulai_lubang_ekor`) plus kedelapan
   `reports/kehidupan_arsip_<i>.json`. Cara termurah: perluas `silang_funding`
   menjadi V3 dengan `daftar_lubang_tengah` yang memakai `bentuk_lubang_lokal`
   yang SUDAH ada, dan terbitkan ke berkas KECIL tersendiri. Push atomik modul +
   uji + workflow (aturan 45); cacah butir uji menurut aturan 54 **dan 57**
   (daftar bernomor, jangan mengulang KC-19).
2. **Uji H-A010** — bandingkan bulan funding PERTAMA dengan bulan klines pertama
   bagi ICP, TLM, BNX, JUP, QTUM. MENANG bila kelimanya funding-nya mulai
   SESUDAH klines; GUGUR bila ada satu saja yang mulai lebih dulu lalu bolong.
3. **Cocokkan 3 lubang BNXUSDT (2022-04, -06, -08) dengan 3 simbol-bulan KC-15**
   — keduanya BNXUSDT 2022 dan keduanya bercacah 3. Kebetulan yang mencurigakan;
   wajib dicocokkan, dilarang diasumsikan.
4. **Jalankan ulang `ukur_baris`** — cacah baris `silang_funding.py` V2 BELUM
   diukur; angka 396 (V1) KEDALUWARSA. Dilarang ditaksir (pola R-175/179/203).
5. **Sebaran 1.401 MATI menurut tahun dan simbol** dari `baris_mati` di laporan
   penuh; sekalian `bulan_hidup_terakhir` bagi 28 anggota kohort di luar sampel
   abjad — definisi wajib dicocokkan dengan `kohort_ekor` (aturan 36). Peringatan
   nyata: BNXUSDT muncul di kedua daftar dengan arti berbeda.
6. **R-199** — jalankan ulang `pulihkan` V2 atas kedelapan pecahan
   (`definisi_dapat_dibedakan` diramalkan false pada indeks 2 dan 5). Sampai itu
   `reports/pulihkan_pecahan_<i>.json` dibaca sebagai laporan V1.
7. **Terima atau tolak ADR-A007** dengan kendala R-146 (839.842.134 sudah memuat
   516.135 baris karantina). **Terapkan ADR-A006 sepenuhnya**;
   `dugaan_pengganti` (ADR-A005); karantina artefak 7 hari; adjudikasi R-7,
   R-19, R-20, R-28, R-36, R-37.
8. Kehidupan 12 simbol-bulan karantina (tar terpisah, belum disentuh).
9. `funding.py` **705 baris** — aturan 48 melarang menambah fungsi sebelum
   dipecah.
10. Belum diukur (daftar penuh di bagian terakhir STATE v32): sebab KC-15,
    15 SETTLED lain, INDEKS 3 nama manual, token saham dan komoditas, 16 simbol
    non-ASCII, `.decode("utf-8","replace")`, BUSD/USDC, jurang 38 lawan 41, skew
    `waktu_utc`, `funding_selisih_penuh.json` (`daftar_terpotong` true), selisih
    byte AGIX 531 lawan 529, `tests/test_pulihkan.py` belum dibaca ulang.
11. Paralel (aturan 3): ADR-A003 (berkasnya BELUM ADA), juri T4 dengan biaya,
    lapisan validasi (Šidák, ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy
    murni). **Adjudikasi riset TETAP TERKUNCI.**

## KEBIASAAN

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. Berkepala dua yang separuh
  salah = SEPARUH. Penyebut nol = TIDAK TERADJUDIKASI. Run yang tak akan menyala
  = DILARANG diramalkan (55). Commit yang tak akan ada = DILARANG (56). Cacah
  butir tanpa daftar bernomor = DILARANG (57).
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21). Jangan
  menaksir yang bisa dihitung.
- **Jangan menyunting angka ramalan yang sudah didorong.** Bila kau menemukan
  sendiri bahwa ramalanmu salah sebelum hasilnya terbit, catat temuan itu dan
  biarkan ramalannya kalah. Mencocokkan angka belakangan adalah cara paling
  halus untuk menipu papan skor sendiri.
- Aturan 24 medan penggugur; 37 sampel wajib memuat ≥1 kasus tiap kelas cacat
  relevan; 20 dilarang menyimpulkan di luar rentang disampel; 50 kesimpulan dari
  KETIADAAN wajib kendali positif; 51 jendela mundur adaptif; 52 laporan tak
  terbaca utuh setara tak ada; 53 baca PERILAKU fungsi sebelum meramal kode
  keluar.
- Pisahkan arah sebuah irisan: A→B dan B→A adalah dua angka.
- Bila dua definisi memberi angka berbeda, tulis keduanya berdampingan dengan
  penyebutnya (aturan 36) — kadang keduanya bertemu setelah penyebut disamakan,
  seperti 48 lawan 45 lubang awal.
- Push yang menyalakan run wajib atomik (aturan 45): modul + uji + workflow.
- BACA berkas sebelum menuduhnya salah. Sebaliknya, jangan menuduh modul ketika
  yang salah adalah harapan uji, jangan menuduh laporan tertimpa ketika yang
  salah adalah pemicu workflow, dan jangan menuduh pytest ketika yang salah
  adalah cacahanmu sendiri.
- Pisahkan fakta dari asumsi; tanpa bukti tulis "Ini memerlukan verifikasi."
- "lanjut" berarti teruskan tanpa konfirmasi. Perbarui STATE.md, jurnal, dan
  berkas ini secara berkala. Jangan berhenti dengan alasan konteks Notion;
  patokannya konteks model.
- Tenggat: riset dipercepat sebelum 3 Agustus 2026.
