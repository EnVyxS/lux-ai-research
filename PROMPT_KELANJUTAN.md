# PROMPT KELANJUTAN — versi 36

Disusun 29 Juli 2026, 15:45 WIB, di atas STATE **v33** (commit `cd684a8c`) serta
jurnal 87 dan 88. Berkas di repo adalah kebenaran; prompt ini hanya peta.

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
   `STATE.md` (**v33** — aturan 1–58, kelas cacat sampai KC-20, papan skor
   R-1..R-226, daftar utang; INI YANG PALING PENTING dan TIDAK tertinggal dari
   jurnal), `journal/2026-07-29-88.md`, lalu `-87.md`; `decisions/ADR-A008.md`
   (DITERIMA 1–6; **Keputusan 7 kini berprasyarat BENTUK terpenuhi**),
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
- **Aturan 56:** ramalan wajib menyebut sasaran yang keberadaannya dijamin cara
  kerjamu sendiri — bentuknya "commit BERIKUTNYA yang menyentuh `<berkas>`".
  Menyebut satu commit bermuatan dua berkas DILARANG kecuali push-nya dirancang
  atomik sejak ramalan ditulis. R-216 jatuh ke SEPARUH karena ini.
- **Aturan 57 dan KC-19:** cacah butir uji hanya sah bila nama setiap fungsi
  `def test_` ditulis BERNOMOR lebih dulu. Tiga ramalan gugur dengan sebab yang
  sama (R-148, R-211, R-217). **Aturan itu kini TERBUKTI BEKERJA:** R-221
  menulis 42 nama bernomor dan CI mengumpulkan tepat 382.
- **Aturan 58 dan KC-20 (BARU) — pelajaran termahal giliran ini.** Taksiran
  cacah baris atas berkas yang belum kau baca ulang UTUH bias sistematis ke
  BAWAH: R-175 (..680, nyata 705), R-179 (..700, 705), R-203 (..400, 417), R-225
  (..620, **705**). Empat dari empat, semuanya terlalu rendah. Sementara ramalan
  sesudah baca ulang utuh TEPAT tiga dari tiga (R-213, R-214, R-224). Karena itu:
  baca ulang dulu lalu ramalkan, atau pakai pita yang batas atasnya ≥1,8× batas
  bawah, atau jangan meramal dan cukup ukur. Menambah 30 persen tidak cukup.
- Tidak ada API patch — `push_files` menulis ulang seluruh isi berkas. Rancang
  berkas kecil, dan sesudah mendorong berkas panjang BACA ULANG dari `main`
  untuk memastikan ekornya hadir (aturan 52). Berkas laporan besar wajib
  berpasangan dengan berkas KECIL: pola itu terbukti dua kali, pada
  `reports/hidup_tanpa_funding.json` dan `reports/lubang_tengah.json`.
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

## POSISI (29 Juli 2026, 15:45 WIB)

Rantai commit mutakhir: `509fd63e` (STATE v32) → `8b397622` (PROMPT v35) →
**`680d04b4`** (trio `lubang_tengah` V1: modul + uji + workflow, ATOMIK) →
`1fa7aadf` (laporan runner) → **`3ecf08cf`** (jurnal 87) → **`85079ffd`**
(`ukur_baris` V4) → `29c120b2` (laporan runner) → **`0c7c8e39`** (jurnal 88) →
**`cd684a8c`** (STATE v33) → berkas ini.

Run terverifikasi (commit dicocokkan):

- **lubang_tengah V1** — run **30436334434**, commit `680d04b4`, kode 0,
  `sidik_kode` `ebdf0b1c…25e4`; `reports/lubang_tengah.json` blob `247a04cf`
  dibaca UTUH; `selisih_lubang_tengah` **0**, `kendali_sah` true.
- **ukur_baris V4** — run **30436915256**, commit `85079ffd`, kode 0;
  `reports/ukur_baris.json` blob `6f9c5420` dibaca UTUH; 13 berkas, **4.638**
  baris, `melebihi_pagar` **0**.
- **CI 30436915256** (`85079ffd`) — **382 butir, kode 0**.
- **CI 30436334383** (`680d04b4`) — 382 butir, kode 0 (dasar R-221).
- **CI 30435672616** (`8b397622`) — 340 butir, kode 0 (dasar R-220).

Papan skor sampai R-226: **TEPAT 158 / MELESET 41 / SEPARUH 13 / TIDAK
TERADJUDIKASI 7 / MENUNGGU 7 = 226** (MENUNGGU: R-7, R-19, R-20, R-28, R-36,
R-37, R-199). Ramalan berikutnya **R-228** — R-227 dipraregistrasi di bawah.
Aturan terakhir **58**, kelas cacat terakhir **KC-20**, hipotesis terakhir
**H-A011 (LAHIR, BELUM DIUJI)**; **H-A010 MENANG 5–0 dengan batas tersurat**.
Jurnal berikutnya **89**, STATE berikutnya **v34**, PROMPT berikutnya **v37**,
ADR berikutnya **A009**.

**R-227, dipraregistrasi di sini (aturan 26, 38, 55, 56).** Pada commit
BERIKUTNYA yang menyentuh `PROMPT_KELANJUTAN.md` — yakni commit yang memuat
berkas ini — `ci.yml` MENYALA (berkas ada di akar, tidak tersentuh
`paths-ignore`), dan `reports/ci_terakhir.json` akan melaporkan **382 butir**
dengan `kode_keluar` **0**. Dasarnya: tidak ada berkas uji maupun modul yang
berubah pada commit ini, dan 382 sudah terverifikasi dua kali (run 30436334383
dan 30436915256). Aturan 57 tidak perlu daftar bernomor di sini sebab angkanya
diambil dari laporan CI terverifikasi, bukan dari cacahan sendiri.

## TEMUAN MUTAKHIR YANG MENENTUKAN ARAH

1. **Keenam lubang funding TENGAH akhirnya BERNAMA, dan ternyata DUA peristiwa,
   bukan enam.** BTCSTUSDT 2022-01 (rentetan 1; funding 2021-12 → 2022-02) dan
   LITUSDT 2025-07..2025-11 (rentetan 5; funding 2025-06 → **2026-01**).
   `sebaran_status_lubang_tengah` = MATI **6**, SEPI 0, HIDUP 0, TAK_TERUKUR 0.
2. **Keenamnya MATI dengan klines PENUH secara bentuk** — 44.640 lilin
   (31×1.440) atau 43.200 (30×1.440), tanpa satu menit hilang, dan semuanya
   lolos gerbang 1m. Ini KC-18 dari sisi lain: gerbang menilai BENTUK, bukan
   KEHIDUPAN, dan lubang funding tengah justru satu-satunya penanda yang
   memisahkan keduanya.
3. **H-A010 DIUJI dan MENANG 5–0** (QTUM +1 bulan, JUP +1, BNX +9, ICP +16,
   TLM +20). BATASNYA tersurat: `funding_semesta.json.per_simbol` punya **10
   medan** dan TIDAK memuat `bulan_funding_pertama`, jadi "berfunding pertama"
   adalah definisi TURUNAN (bulan klines terawal yang tidak berlubang).
4. **Jalan sah menguatkan atau MENGGUGURKAN R-223 tanpa unduhan:** medan
   `funding_tanpa_klines` ADA dan belum dipakai. Kosong pada kelima simbol →
   definisi turunan itu TEPAT; berisi pada salah satunya → kemenangan R-223
   wajib ditinjau ulang. Ini utang, bukan kesimpulan.
5. **Ketiga bentuk lubang kini punya penjelasan calon:** ekor = kematian pasar
   (lubang → mati 96,0%); awal = funding menyusul klines (H-A010); tengah = jeda
   penerbitan pada pasar mati yang klines-nya tetap terbit. Prasyarat BENTUK bagi
   Keputusan 7 ADR-A008 TERPENUHI — keputusannya sendiri belum diambil, dan
   ADR-A002 §10 tetap TIDAK boleh disunting.
6. **`silang_funding.py` ternyata 705 baris**, seri dengan `funding.py` 705.
   Aturan 48 kini menyentuh DUA berkas: dilarang menambah fungsi ke keduanya
   sebelum dipecah. Keputusan membuat `lubang_tengah.py` sebagai modul BARU
   alih-alih `silang_funding` V3 terbukti benar oleh angka.
7. **Dua utang penulisan dicatat terbuka, sengaja TIDAK disunting:** salah tulis
   "simbal" di `lubang_tengah.py` (menunggu V2 modul itu supaya `sidik_kode`
   tidak berubah di atas laporan yang sudah diadjudikasi), dan docstring R-225
   yang menulis "tujuh fungsi" lalu menyebut sembilan nama (jumlah yang benar
   sembilan; teks praregistrasi yang sudah didorong tidak dirapikan belakangan).

## PEKERJAAN BERIKUTNYA

1. **`lubang_tengah` V2** — uji `funding_tanpa_klines` bagi ICP, TLM, BNX, JUP,
   QTUM (penguat atau penggugur R-223), sekaligus perbaiki salah tulis "simbal".
   Push atomik modul + uji + workflow (aturan 45); cacah butir uji dengan daftar
   BERNOMOR (aturan 54 dan 57); jangan meramalkan cacah barisnya tanpa membaca
   ulang utuh (aturan 58).
2. **Uji H-A011** — status kehidupan LITUSDT pada 2026-01..2026-06 dari
   `reports/kehidupan_arsip_<i>.json`. HIDUP kembali → hipotesis menguat; tetap
   MATI padahal funding terbit → GUGUR, dan yang tersisa hanya pernyataan tentang
   PENERBITAN, bukan tentang perdagangan. Periksa juga apakah BTCSTUSDT 2022-01
   sejenis atau lain sama sekali.
3. **Pecah `silang_funding.py`** (705 baris) sebelum satu pun fungsi baru masuk
   ke sana; setiap pemecahan wajib memperluas daftar berkas `sidik_kode`
   (aturan 48) dan waspadai aturan 49 (nama yang DITAMBAL oleh uji).
4. **Cocokkan 3 lubang BNXUSDT (2022-04, -06, -08) dengan 3 simbol-bulan KC-15**
   — keduanya BNXUSDT 2022 dan keduanya bercacah 3. Kebetulan yang mencurigakan;
   wajib dicocokkan, dilarang diasumsikan.
5. **Sebaran 1.401 MATI menurut tahun dan simbol** dari `baris_mati` di laporan
   penuh; sekalian `bulan_hidup_terakhir` bagi 28 anggota kohort di luar sampel
   abjad — definisi wajib dicocokkan dengan `kohort_ekor` (aturan 36). Peringatan
   nyata: BNXUSDT muncul di kedua daftar dengan arti berbeda.
6. **R-199** — jalankan ulang `pulihkan` V2 atas kedelapan pecahan
   (`definisi_dapat_dibedakan` diramalkan false pada indeks 2 dan 5). Sampai itu
   `reports/pulihkan_pecahan_<i>.json` dibaca sebagai laporan V1.
7. **Keputusan 7 ADR-A008** kini boleh dipertimbangkan, dengan syarat memuat
   batas H-A010 dan status H-A011 yang belum diuji. **Terima atau tolak
   ADR-A007** dengan kendala R-146 (839.842.134 sudah memuat 516.135 baris
   karantina). Terapkan ADR-A006 sepenuhnya; `dugaan_pengganti` (ADR-A005);
   karantina artefak 7 hari; adjudikasi R-7, R-19, R-20, R-28, R-36, R-37.
8. Kehidupan 12 simbol-bulan karantina (tar terpisah, belum disentuh).
9. `funding.py` **705 baris** — aturan 48 melarang menambah fungsi sebelum
   dipecah.
10. Belum diukur (daftar penuh di bagian terakhir STATE v33): sebab KC-15,
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
  butir tanpa daftar bernomor = DILARANG (57). Cacah baris berkas yang belum
  dibaca ulang utuh = pita lebar atau tidak meramal sama sekali (58).
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21). Jangan
  menaksir yang bisa dihitung — KC-20 lahir justru dari menaksir berkas yang
  KAU SENDIRI tulis.
- **Jangan menyunting angka ramalan yang sudah didorong.** Bila kau menemukan
  sendiri bahwa ramalanmu salah sebelum hasilnya terbit, catat temuan itu dan
  biarkan ramalannya kalah. Mencocokkan angka belakangan adalah cara paling
  halus untuk menipu papan skor sendiri. Berlaku juga untuk kalimat yang
  bertentangan di dalam docstring praregistrasi: catat, jangan rapikan.
- Aturan 24 medan penggugur; 37 sampel wajib memuat ≥1 kasus tiap kelas cacat
  relevan; 20 dilarang menyimpulkan di luar rentang disampel; 50 kesimpulan dari
  KETIADAAN wajib kendali positif; 51 jendela mundur adaptif; 52 laporan tak
  terbaca utuh setara tak ada; 53 baca PERILAKU fungsi sebelum meramal kode
  keluar.
- Rancang uji yang BISA gugur. `uji_h_a010` menuntut kelima simbol setuju; satu
  membangkang sudah menjatuhkannya — karena itu kemenangannya berarti.
- Pisahkan arah sebuah irisan: A→B dan B→A adalah dua angka.
- Bila dua definisi memberi angka berbeda, tulis keduanya berdampingan dengan
  penyebutnya (aturan 36) — kadang keduanya bertemu setelah penyebut disamakan,
  seperti 48 lawan 45 lubang awal.
- Push yang menyalakan run wajib atomik (aturan 45): modul + uji + workflow.
- BACA berkas sebelum menuduhnya salah. Sebaliknya, jangan menuduh modul ketika
  yang salah adalah harapan uji, jangan menuduh laporan tertimpa ketika yang
  salah adalah pemicu workflow, jangan menuduh pytest ketika yang salah adalah
  cacahanmu sendiri, dan jangan menuduh arsip cacat ketika bentuk datanya justru
  menjelaskan dirinya.
- Pisahkan fakta dari asumsi; tanpa bukti tulis "Ini memerlukan verifikasi."
- "lanjut" berarti teruskan tanpa konfirmasi. Perbarui STATE.md, jurnal, dan
  berkas ini secara berkala. Jangan berhenti dengan alasan konteks Notion;
  patokannya konteks model.
- Tenggat: riset dipercepat sebelum 3 Agustus 2026.
