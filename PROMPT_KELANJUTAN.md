# PROMPT KELANJUTAN — versi 37

Disusun 29 Juli 2026, 17:05 WIB, di atas STATE **v34** (commit `e11750cb`) serta
jurnal 88 dan 89. Berkas di repo adalah kebenaran; prompt ini hanya peta.

Kamu melanjutkan riset LUX-AI. Operator: Diva Juan Nur Taqarrub, GitHub EnVyxS,
zona waktu Asia/Jakarta, bahasa kerja Indonesia. Jangan mulai bekerja sebelum
menyelesaikan LANGKAH 0.

**TENGGAT MAJU: 2 Agustus 2026** (sebelumnya 3 Agustus). Operator meminta riset
dipercepat. Percepatan yang SAH hanya satu bentuk: menumpuk lebih banyak
pertanyaan ke dalam SATU run atomik atas bahan yang sudah di-commit. Aturan 45,
52, 54, 57, 58, dan 59 TIDAK boleh dilewati untuk menghemat waktu — setiap kali
salah satunya dilewati, satu giliran penuh terbuang untuk memperbaikinya.

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`, dengan
   `owner` dan `repo` HANYA di dalam `toolArguments`, tidak di tingkat atas.
3. Baca dari `main` repo `EnVyxS/lux-ai-research` berurutan: berkas ini,
   `STATE.md` (**v34** — aturan 1–59, kelas cacat sampai KC-21, papan skor
   R-1..R-230, daftar utang; INI YANG PALING PENTING dan TIDAK tertinggal dari
   jurnal), `journal/2026-07-29-89.md`, lalu `-88.md`; `decisions/ADR-A008.md`
   (DITERIMA 1–6; **Keputusan 7 kini berbahan LENGKAP**),
   `decisions/ADR-A007.md` (masih DIUSULKAN), lalu `ADR-A004.md` dan
   `ADR-A002.md` bila menyentuh serapan (§10 BELUM disentuh dan tetap tidak boleh
   disentuh), `PETA_MODUL.md` bila menyentuh modul warisan.
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
- **Laporan CI dapat TERTIMPA.** `reports/ci_terakhir.json` ditulis ulang oleh
  setiap run; bila dua run berdekatan, laporan yang lebih tua hanya terbaca
  dengan `get_file_contents` pada **ref commit** yang bersangkutan. R-227 nyaris
  hangus karena ini — baca pada ref, jangan pada `main`.
- **Aturan 56:** ramalan wajib menyebut sasaran yang keberadaannya dijamin cara
  kerjamu sendiri — bentuknya "commit BERIKUTNYA yang menyentuh `<berkas>`".
- **Aturan 57 dan KC-19:** cacah butir uji hanya sah bila nama setiap fungsi
  `def test_` ditulis BERNOMOR lebih dulu. **Kini TERBUKTI BEKERJA DUA DARI
  DUA:** R-221 (42 nama → 382) dan R-228 (56 nama → 382 − 42 + 56 = **396**).
- **Aturan 58 dan KC-20:** taksiran cacah baris atas berkas yang belum dibaca
  ulang UTUH bias sistematis ke BAWAH — R-175, R-179, R-203, R-225, empat dari
  empat terlalu rendah. Baca ulang dulu lalu ramalkan, atau pakai pita yang batas
  atasnya ≥1,8× batas bawah, atau jangan meramal dan cukup ukur.
- **Aturan 59 dan KC-21 (BARU) — pelajaran termahal giliran ini.** Ramalan yang
  menegaskan KETIADAAN sebuah gejala wajib menyebut penyebut yang mampu memuat
  gejala itu beserta cacah kasus yang pernah benar-benar diperiksa. Bila cacah
  itu NOL, tulis sebagai kemungkinan campuran atau jangan meramal. R-230 gugur
  karena saya memakai `cacah_simbol_bangkit_dapat_diuji` = 0 — sebuah nol yang
  secara tersurat berarti "tidak dapat diuji" — sebagai bukti bahwa kebangkitan
  tidak ada. Nol yang tidak mampu membedakan bukan bukti.
- Tidak ada API patch — `push_files` menulis ulang seluruh isi berkas. Rancang
  berkas kecil, dan sesudah mendorong berkas panjang BACA ULANG dari `main`
  untuk memastikan ekornya hadir (aturan 52). Berkas laporan besar wajib
  berpasangan dengan berkas KECIL: pola itu terbukti tiga kali.
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

## POSISI (29 Juli 2026, 17:05 WIB)

Rantai commit mutakhir: `85079ffd` (`ukur_baris` V4) → **`0c7c8e39`** (jurnal 88)
→ **`cd684a8c`** (STATE v33) → **`a9e91bcd`** (PROMPT v36) → **`be5cd877`**
(`lubang_tengah` V2: modul + uji, ATOMIK) → `3b769380` dan `f6eb8b78` (laporan
runner + jurnal 89) → **`e11750cb`** (STATE v34) → berkas ini.

Run terverifikasi (commit dicocokkan):

- **lubang_tengah V2** — run **30440471508**, commit `be5cd877`, kode 0,
  `sidik_kode` `c9372bd7…b3f4e`; `reports/lubang_tengah.json` blob `39cd1caa`
  dibaca UTUH; `selisih_lubang_tengah` **0**, `kendali_sah` true,
  `cacah_laporan_dibaca` 8.
- **CI 30440471598** (`be5cd877`) — **396 butir, kode 0** (dasar R-228).
- **CI 30437620711** (`a9e91bcd`) — 382 butir, kode 0 (dasar R-227; hanya
  terbaca lewat ref `be5cd877`).
- **CI 30436915256** (`85079ffd`) — 382 butir, kode 0.
- **ukur_baris V4** — run 30436915256, 13 berkas, **4.638** baris,
  `melebihi_pagar` 0.

Papan skor sampai R-230: **TEPAT 161 / MELESET 42 / SEPARUH 13 / TIDAK
TERADJUDIKASI 7 / MENUNGGU 7 = 230** (MENUNGGU: R-7, R-19, R-20, R-28, R-36,
R-37, R-199). Ramalan berikutnya **R-232** — R-231 dipraregistrasi di bawah.
Aturan terakhir **59**, kelas cacat terakhir **KC-21**, hipotesis terakhir
**H-A012 (LAHIR, BELUM DIUJI)**; **H-A010 MENANG 5–0 dengan definisi kini TEPAT**,
**H-A011 MENANG 6–0**. Riwayat CI: … 340 → 382 → 382 → **396**. Jurnal berikutnya
**90**, STATE berikutnya **v35**, PROMPT berikutnya **v38**, ADR berikutnya
**A009**.

**R-231, dipraregistrasi di sini (aturan 26, 38, 55, 56).** Pada commit
BERIKUTNYA yang menyentuh `PROMPT_KELANJUTAN.md` — yakni commit yang memuat
berkas ini — `ci.yml` MENYALA (berkas ada di akar, tidak tersentuh
`paths-ignore`), dan `reports/ci_terakhir.json` akan melaporkan **396 butir**
dengan `kode_keluar` **0**. Dasarnya: tidak ada berkas uji maupun modul yang
berubah pada commit ini, dan 396 sudah terverifikasi pada run 30440471598.
Aturan 57 tidak perlu daftar bernomor di sini sebab angkanya diambil dari laporan
CI terverifikasi, bukan dari cacahan sendiri.

## TEMUAN MUTAKHIR YANG MENENTUKAN ARAH

1. **KEBANGKITAN PASAR PERTAMA YANG TERUKUR.** LITUSDT: HIDUP sampai 2025-06 →
   MATI 2025-07..2025-11 (klines terbit PENUH secara bentuk, 44.640/43.200 lilin,
   nol menit hilang, lolos gerbang 1m, funding HILANG) → funding KEMBALI 2026-01
   dan keenam bulan 2026-01..2026-06 **HIDUP**. `cacah_hidup` 6 dari 6,
   `h_a011_menang` true. **H-A011 MENANG 6–0.**
2. **"Nol kebangkitan" pada `kohort_ekor` V4 adalah batas ALAT UKUR, bukan fakta
   pasar.** `bangkit_kembali` 0 datang bersama
   `cacah_simbol_bangkit_dapat_diuji` **0**. Setiap pernyataan repo tentang
   "tidak ada kebangkitan" BATAL sebagai fakta; ia hanya sah sebagai "belum
   terukur". Dari kesalahan memakainya sebagai fakta lahir **aturan 59** dan
   **KC-21**.
3. **Bentuk lubang TENGAH bukan sekadar "jeda penerbitan pada pasar mati".** Pada
   LITUSDT ia menandai pasar yang berhenti diperdagangkan lalu diperdagangkan
   kembali, dengan funding dan perdagangan berhenti serta pulih BERSAMA — persis
   perilaku arsip yang JUJUR, sehingga alasan menuduh arsip funding cacat makin
   lemah (ADR-A002 §10 tetap tidak disentuh).
4. **R-229 TEPAT menutup batas R-223.** `funding_tanpa_klines` KOSONG pada
   kelima simbol H-A010 (`ada_medan` true 5/5, `cacah_bulan` 0, `cacah_berisi` 0,
   `cacah_tak_terukur` 0, `kosong_seluruhnya` true). Definisi turunan
   "bulan berfunding pertama" bukan hanya memadai melainkan **TEPAT**; kemenangan
   H-A010 DIKUATKAN.
5. **Satu simbol dapat MENYEBERANG status.** Semesta layak backtest 18.087 memuat
   keenam bulan 2026 LITUSDT dan MENOLAK kelima bulan 2025-07..-11 nya. Penyaringan
   per SIMBOL-BULAN (ADR-A008 Keputusan 2–5) kini benar oleh CONTOH, bukan hanya
   oleh selera. Konsekuensi lanjutan: `bulan_hidup_terakhir` bagi 10 anggota
   kohort bisa keliru dibaca sebagai "akhir" — periksa apa yang terjadi SESUDAHnya.
6. **`silang_funding.py` dan `funding.py` sama-sama 705 baris.** Aturan 48
   melarang menambah fungsi ke keduanya sebelum dipecah. `lubang_tengah.py` V2
   belum diukur cacah barisnya — ukur sebelum V3.
7. **Utang penulisan yang sengaja TIDAK disunting:** docstring R-225 menulis
   "tujuh fungsi" lalu menyebut sembilan nama (jumlah yang benar sembilan).
   Salah tulis "simbal" sudah LUNAS di V2 dan dijaga uji.

## PEKERJAAN BERIKUTNYA — diurut untuk tenggat 2 Agustus

1. **Satu run atomik yang menjawab TIGA pertanyaan sekaligus** (pola yang sudah
   terbukti pada `lubang_tengah` V2, bahan sudah di-commit, tanpa unduhan):
   a. **H-A012 — pindaian kebangkitan SELURUH semesta:** simbol mana saja yang
      punya bulan MATI lalu bulan HIDUP sesudahnya, atas kedelapan
      `reports/kehidupan_arsip_<i>.json`; penyebutnya 787 simbol dan kini terbukti
      tidak kosong. Aturan 59 wajib ditaati saat meramalkan cacahnya — jangan
      meramalkan "hanya satu".
   b. **BTCSTUSDT 2022-02..2026-06** lewat `status_rentang`: apakah lubang
      tengahnya juga kebangkitan atau bentuk lain sama sekali.
   c. **Sebaran 1.401 MATI menurut TAHUN dan menurut SIMBOL** dari `baris_mati`,
      plus `bulan_hidup_terakhir` bagi 28 anggota kohort di luar sampel abjad
      (definisi wajib dicocokkan dengan `kohort_ekor`, aturan 36; BNXUSDT muncul
      di dua daftar dengan arti berbeda).
   Modul baru (jangan tambahkan ke berkas 705 baris). Push atomik modul + uji +
   workflow; daftar `def test_` BERNOMOR sebelum meramal cacah butir; jangan
   meramalkan cacah baris tanpa membaca ulang utuh.
2. **Ukur cacah baris `lubang_tengah.py` V2 dan modul baru** lewat `ukur_baris`
   V5 — murah, dan menutup satu utang tiap kali.
3. **Pecah `silang_funding.py`** (705 baris) sebelum satu pun fungsi baru masuk
   ke sana; setiap pemecahan wajib memperluas daftar berkas `sidik_kode`
   (aturan 48) dan waspadai aturan 49 (nama yang DITAMBAL oleh uji).
4. **Keputusan 7 ADR-A008** — bahannya kini LENGKAP: keempat bentuk lubang
   bernama, H-A010 MENANG dengan definisi TEPAT, H-A011 MENANG 6–0. Keputusannya
   wajib menyebut bahwa bentuk TENGAH dapat menandai jeda yang BERAKHIR, bukan
   hanya akhir, dan bahwa penyaringan wajib per simbol-bulan.
5. **Cocokkan 3 lubang BNXUSDT (2022-04, -06, -08) dengan 3 simbol-bulan KC-15**
   — keduanya BNXUSDT 2022 dan keduanya bercacah 3. Kebetulan yang mencurigakan;
   wajib dicocokkan, dilarang diasumsikan.
6. **R-199** — jalankan ulang `pulihkan` V2 atas kedelapan pecahan
   (`definisi_dapat_dibedakan` diramalkan false pada indeks 2 dan 5). Sampai itu
   `reports/pulihkan_pecahan_<i>.json` dibaca sebagai laporan V1.
7. **Terima atau tolak ADR-A007** dengan kendala R-146 (839.842.134 sudah memuat
   516.135 baris karantina). Terapkan ADR-A006 sepenuhnya; `dugaan_pengganti`
   (ADR-A005); karantina artefak 7 hari; adjudikasi R-7, R-19, R-20, R-28, R-36,
   R-37.
8. **ADR-A003 taksonomi rezim** — berkasnya BELUM ADA, dan kebangkitan terukur
   menyentuhnya langsung: rezim sebuah simbol tidak monoton.
9. Kehidupan 12 simbol-bulan karantina (tar terpisah, belum disentuh).
10. Belum diukur (daftar penuh di bagian terakhir STATE v34): sebab KC-15,
    15 SETTLED lain, INDEKS 3 nama manual, token saham dan komoditas, 16 simbol
    non-ASCII, `.decode("utf-8","replace")`, BUSD/USDC, jurang 38 lawan 41, skew
    `waktu_utc`, `funding_selisih_penuh.json` (`daftar_terpotong` true), selisih
    byte AGIX 531 lawan 529, `tests/test_pulihkan.py` belum dibaca ulang.
11. Paralel (aturan 3): juri T4 dengan biaya, lapisan validasi (Šidák, ≥300
    permutasi per TANGGAL UTC, PBO dan DSR numpy murni). **Adjudikasi riset TETAP
    TERKUNCI.**

## KEBIASAAN

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. Berkepala dua yang separuh
  salah = SEPARUH. Penyebut nol = TIDAK TERADJUDIKASI. Run yang tak akan menyala
  = DILARANG diramalkan (55). Commit yang tak akan ada = DILARANG (56). Cacah
  butir tanpa daftar bernomor = DILARANG (57). Cacah baris berkas yang belum
  dibaca ulang utuh = pita lebar atau tidak meramal (58). **Penegasan KETIADAAN
  tanpa penyebut yang mampu memuat gejalanya = DILARANG (59).**
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21). Jangan
  menaksir yang bisa dihitung.
- **Jangan menyunting angka ramalan yang sudah didorong.** Bila kau menemukan
  sendiri bahwa ramalanmu salah sebelum hasilnya terbit, catat temuan itu dan
  biarkan ramalannya kalah. R-230 adalah kekalahan yang PALING berharga sejauh
  ini justru karena angkanya dibiarkan.
- Rancang uji yang BISA gugur. `uji_h_a011` menuntut LITUSDT hidup kembali; satu
  bulan MATI padahal funding terbit sudah menjatuhkannya — karena itu
  kemenangannya berarti, walau ramalan saya kalah.
- Aturan 24 medan penggugur; 37 sampel wajib memuat ≥1 kasus tiap kelas cacat
  relevan; 20 dilarang menyimpulkan di luar rentang disampel; 46 kode dilarang
  menyimpulkan dari penyebut nol; 50 kesimpulan dari KETIADAAN wajib kendali
  positif; 51 jendela mundur adaptif; 52 laporan tak terbaca utuh setara tak ada;
  53 baca PERILAKU fungsi sebelum meramal kode keluar.
- Pisahkan arah sebuah irisan: A→B dan B→A adalah dua angka.
- Bila dua definisi memberi angka berbeda, tulis keduanya berdampingan dengan
  penyebutnya (aturan 36).
- Push yang menyalakan run wajib atomik (aturan 45): modul + uji + workflow.
- BACA berkas sebelum menuduhnya salah. Sebaliknya, jangan menuduh modul ketika
  yang salah adalah harapan uji, jangan menuduh laporan tertimpa ketika yang
  salah adalah pemicu workflow, jangan menuduh pytest ketika yang salah adalah
  cacahanmu sendiri, jangan menuduh arsip cacat ketika bentuk datanya justru
  menjelaskan dirinya, dan **jangan menuduh sebuah gejala tidak ada ketika yang
  sebenarnya belum ada adalah pengukurannya.**
- Pisahkan fakta dari asumsi; tanpa bukti tulis "Ini memerlukan verifikasi."
- "lanjut" berarti teruskan tanpa konfirmasi. Perbarui STATE.md, jurnal, dan
  berkas ini secara berkala. Jangan berhenti dengan alasan konteks Notion;
  patokannya konteks model.
- **Tenggat: 2 Agustus 2026.** Percepat dengan menumpuk pertanyaan per run, bukan
  dengan melewatkan verifikasi.
