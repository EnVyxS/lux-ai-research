# PROMPT KELANJUTAN — versi 38

Disusun 29 Juli 2026, 17:20 WIB, di atas STATE **v35** (commit `34ff496b`) serta
jurnal 90 dan 91. Berkas di repo adalah kebenaran; prompt ini hanya peta.

Kamu melanjutkan riset LUX-AI. Operator: Diva Juan Nur Taqarrub, GitHub EnVyxS,
zona waktu Asia/Jakarta, bahasa kerja Indonesia. Jangan mulai bekerja sebelum
menyelesaikan LANGKAH 0.

**TENGGAT: 2 Agustus 2026.** Percepatan yang SAH hanya satu bentuk: menumpuk lebih
banyak pertanyaan ke dalam SATU run atomik atas bahan yang sudah di-commit. Pola
itu kini terbukti DUA kali (`lubang_tengah` V2 menjawab dua pertanyaan,
`kebangkitan` V1 menjawab empat). Aturan 45, 52, 54, 57, 58, 59, 60, dan 61 TIDAK
boleh dilewati untuk menghemat waktu — setiap kali salah satunya dilewati, satu
giliran penuh terbuang untuk memperbaikinya.

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`, dengan
   `owner` dan `repo` HANYA di dalam `toolArguments`, tidak di tingkat atas.
3. Baca dari `main` repo `EnVyxS/lux-ai-research` berurutan: berkas ini,
   `STATE.md` (**v35** — aturan 1–61, kelas cacat sampai KC-23, papan skor
   R-1..R-235, daftar utang; INI YANG PALING PENTING dan TIDAK tertinggal dari
   jurnal), `journal/2026-07-29-91.md`, lalu `-90.md`; `decisions/ADR-A008.md`
   (DITERIMA 1–6; **Keputusan 7 berbahan LENGKAP dan BERCABANG DUA**),
   `decisions/ADR-A007.md` (masih DIUSULKAN), lalu `ADR-A004.md` dan `ADR-A002.md`
   bila menyentuh serapan (§10 BELUM disentuh dan tetap tidak boleh disentuh),
   `PETA_MODUL.md` bila menyentuh modul warisan.
4. Baru setelah itu jalankan pekerjaan teknis.

## BATASAN YANG MAHAL DIPELAJARI ULANG

- Sandbox agen TIDAK punya jaringan. Semua unduhan dan pengukuran arsip dijalankan
  GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- Tidak ada alat membaca status GitHub Actions dan tidak ada alat memicu
  `workflow_dispatch`. Status hanya diketahui dari berkas laporan yang di-commit
  workflow itu sendiri, dan satu-satunya cara menyalakan run adalah push ke berkas
  yang tersebut di `paths` workflow. Manfaatkan ini: memperbaiki BERKAS UJI tidak
  menyalakan ulang runner berat, sebab `paths` hanya memuat modulnya.
- **Aturan 55:** `ci.yml` memakai `paths-ignore` untuk `journal/**`, `decisions/**`,
  `hipotesis/**`, dan `reports/**`. Commit yang HANYA menyentuh jurnal atau ADR
  **tidak menyalakan CI sama sekali**. `STATE.md` dan `PROMPT_KELANJUTAN.md` ada di
  AKAR, jadi keduanya MENYALAKAN CI.
- **Laporan CI dapat TERTIMPA.** `reports/ci_terakhir.json` ditulis ulang oleh
  setiap run. **Cara menemukan ref yang benar [v38]:** `list_commits` dengan
  `path="reports/ci_terakhir.json"` — pesan tiap commit runner memuat nomor run,
  jadi ref-nya dapat dipilih tanpa menebak. R-231 diadjudikasi dengan cara ini
  lewat ref `acd79d41`.
- **Praregistrasi di PROMPT mudah TERLEWAT.** R-231 ditulis di PROMPT v37 dan tidak
  masuk daftar papan skor jurnal 90, sehingga totalnya keliru 234 padahal 235.
  Setiap praregistrasi di PROMPT wajib disalin ke papan skor STATE berikutnya.
- **Aturan 56:** ramalan wajib menyebut sasaran yang keberadaannya dijamin cara
  kerjamu sendiri — "commit BERIKUTNYA yang menyentuh `<berkas>`".
- **Aturan 57 dan KC-19:** cacah butir uji hanya sah bila nama setiap fungsi
  `def test_` ditulis BERNOMOR lebih dulu. **TERBUKTI BEKERJA TIGA DARI TIGA:**
  R-221 (42 → 382), R-228 (56 → 396), R-232 (54 → **450**).
- **Aturan 58 dan KC-20:** taksiran cacah baris atas berkas yang belum dibaca ulang
  UTUH bias sistematis ke BAWAH — empat dari empat terlalu rendah. Baca ulang dulu,
  atau pita ≥1,8×, atau jangan meramal dan cukup ukur.
- **Aturan 59 dan KC-21:** penegasan KETIADAAN wajib menyebut penyebut yang mampu
  memuat gejalanya. R-230 gugur karena memakai nol yang berarti "tidak dapat
  diuji" sebagai bukti. Bentangan kekeliruan itu kini terukur: bukan satu
  kebangkitan yang terlewat, melainkan **delapan**.
- **Aturan 60 dan KC-22 (BARU) — pelajaran termahal giliran ini.** Tafsir MEKANISME
  yang menang pada satu kasus dilarang dipakai meramal kasus lain sebelum
  penyebutnya ≥2 dan variasinya terukur. R-234 gugur separuh karena saya memindahkan
  mekanisme LITUSDT (funding kembali → perdagangan pulih) ke BTCSTUSDT; hasilnya
  **0 HIDUP dari 53**.
- **Aturan 61 dan KC-23 (BARU).** Nilai sebuah medan dilarang dipakai sebagai nilai
  medan jalur LAIN tanpa membaca laporan jalur itu. STATE v34 menulis "LITUSDT HIDUP
  sampai 2025-06" dengan memakai `funding_sebelum` sebagai bulan hidup terakhir;
  kenyataannya LITUSDT MATI sejak **2025-02**, lima bulan lebih awal.
- Tidak ada API patch — `push_files` menulis ulang seluruh isi berkas. Rancang
  berkas kecil, dan sesudah mendorong berkas panjang BACA ULANG dari ref commit-nya
  untuk memastikan ekornya hadir (aturan 52). Berkas laporan besar wajib
  berpasangan dengan berkas KECIL.
- Saat memeriksa hasil run, cocokkan `commit` / `run_id` / `sidik_kode`. Jangan
  percaya keberadaan berkas: laporan run lama sering masih terbaca.
- Laporan yang belum terbit menjawab "path does not point to a file" — itu bukan
  kegagalan push, melainkan run yang masih berjalan. Melisting `reports/` (path
  berakhiran garis miring) lebih murah daripada menebak nama berkas.
- `search_code` mengembalikan 0 hasil (tidak berindeks) — pakai `get_file_contents`.
- Runner punya numpy, pandas, pyarrow, pyyaml, pytest; TIDAK ada scipy dan
  requests. `data.binance.vision` bisa diakses; `fapi.binance.com` memberi 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. Repo `lux-research`
  boleh DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## POSISI (29 Juli 2026, 17:20 WIB)

Rantai commit mutakhir: `be5cd877` (`lubang_tengah` V2) → `f6eb8b78` (jurnal 89)
→ `e11750cb` (STATE v34) → `63fc2e8f` (PROMPT v37) → **`bdcbaebc`** (trio
`kebangkitan` V1: modul + uji + workflow, ATOMIK) → `e4ead175` (laporan runner) →
`f59b7c82` (jurnal 90) → **`cbd5e8e6`** (jurnal 91) → **`34ff496b`** (STATE v35) →
berkas ini.

Run terverifikasi (commit dicocokkan):

- **kebangkitan V1** — run **30443289476**, commit `bdcbaebc`, kode 0, `sidik_kode`
  `9d25670c…57b48`; `reports/kebangkitan.json` (blob `43b70e24`, 17.644 B) dibaca
  **UTUH**; `selisih_penyebut` 0, `selisih_mati` 0, `sidik_seragam` true,
  `kendali_sah` true, `cacah_laporan_dibaca` 8.
- **CI 30443289417** (`bdcbaebc`) — **450 butir, kode 0** (dasar R-232).
- **CI 30442623074** (`63fc2e8f`) — 396 butir, kode 0 (dasar R-231; hanya terbaca
  lewat ref `acd79d41`).
- **lubang_tengah V2** — run 30440471508 (`be5cd877`), kode 0.
- **ukur_baris V4** — run 30436915256, 13 berkas, **4.638** baris, melebihi pagar 0.

Papan skor sampai R-235: **TEPAT 165 / MELESET 42 / SEPARUH 14 / TIDAK
TERADJUDIKASI 7 / MENUNGGU 7 = 235** (MENUNGGU: R-7, R-19, R-20, R-28, R-36, R-37,
R-199). **R-236 dipraregistrasi di STATE v35** (CI 450 pada commit `34ff496b`) dan
BELUM diadjudikasi — baca `reports/ci_terakhir.json` pada ref commit itu. **R-237
dipraregistrasi di bawah.** Aturan terakhir **61**, kelas cacat terakhir **KC-23**,
hipotesis terakhir **H-A013 (LAHIR, BELUM DIUJI)**; **H-A010 MENANG 5–0**,
**H-A011 MENANG 6–0 tetapi DIBATASI pada LITUSDT**, **H-A012 MENANG (8 simbol)**.
Riwayat CI: … 382 → 396 → 396 → 396 → **450**. Jurnal berikutnya **92**, STATE
berikutnya **v36**, PROMPT berikutnya **v39**, ADR berikutnya **A009**.

**R-237, dipraregistrasi di sini (aturan 26, 38, 55, 56).** Pada commit BERIKUTNYA
yang menyentuh `PROMPT_KELANJUTAN.md` — yakni commit yang memuat berkas ini —
`ci.yml` MENYALA (berkas di akar, tidak tersentuh `paths-ignore`), dan
`reports/ci_terakhir.json` akan melaporkan **450 butir** dengan `kode_keluar` **0**.
Dasarnya: tidak ada modul maupun berkas uji yang berubah pada commit ini, dan 450
sudah terverifikasi pada run 30443289417. Aturan 57 tidak perlu daftar bernomor
sebab angkanya dari laporan CI terverifikasi.

## TEMUAN MUTAKHIR YANG MENENTUKAN ARAH

1. **KEBANGKITAN BUKAN PERISTIWA TUNGGAL — H-A012 MENANG.** Delapan simbol dari
   787 (1,02%) punya bulan MATI lalu bulan HIDUP sesudahnya, kedelapannya
   `bangkit_penuh` (ada HIDUP sebelum rentetan MATI): **CTKUSDT, CVCUSDT, CVXUSDT,
   ICPUSDT, LITUSDT, MAVIAUSDT, SLPUSDT, TLMUSDT**. Masing-masing tepat SATU
   peristiwa — tak ada yang bangkit dua kali. Panjang MATI 2, 2, 8, 10, 11, 13, 13,
   29 = **88** bulan, yakni 6,28% dari 1.401 bulan MATI; **1.313 sisanya belum
   terbukti berakhir.**
2. **BENTUK LUBANG TENGAH PUNYA DUA SEBAB BERLAWANAN.** LITUSDT: funding kembali
   2026-01, pasar HIDUP 6/6. BTCSTUSDT: funding kembali 2022-02, pasar **MATI
   53/53** dan ia pemegang rekor semesta 63 bulan MATI. **Kembalinya funding BUKAN
   penanda kebangkitan** — penerbitan funding dapat pulih TANPA perdagangan, persis
   bunyi KC-18 di jalur funding. KC-18 menang atas tafsir v34; Keputusan 7 ADR-A008
   WAJIB bercabang dua dan DILARANG menyebut "serentak".
3. **Kronologi LITUSDT DIKOREKSI.** Perdagangan berhenti **2025-02**; funding baru
   hilang **2025-07** — selisih lima bulan. Lubang funding tengah MENYUSUL
   kematian, tidak menandainya (arah yang sama dengan bentuk EKOR: lubang → mati
   96,0%).
4. **POLA BARU BELUM DIUKUR — H-A013.** Enam dari delapan kebangkitan dipisahkan
   oleh **tepat satu bulan kalender yang TIDAK ADA di penyebut 19.586**: CTK
   2025-04, CVC 2025-05, CVX **2025-07**, LIT 2025-12, MAVIA 2025-03, SLP
   **2025-07**. Dua pengecualiannya ICPUSDT dan TLMUSDT — persis simbol H-A010,
   yang bulan kebangkitannya SAMA dengan bulan berfunding pertamanya. Dua bulan
   hilang jatuh pada **2025-07**, bulan tebing funding dan kohort puncak.
   `cacah_bulan_antara` 0 berarti tidak ada bulan TERUKUR di sana, BUKAN tidak ada
   apa-apa (aturan 46, 59).
5. **SEBARAN 1.401 MATI PER TAHUN:** 2020 **1** · 2021 **9** · 2022 **34** · 2023
   **103** · 2024 **192** · 2025 **506** · 2026 **556** (jumlah 1.401 ✅). 2026 hanya
   enam bulan → 92,7/bulan lawan 42,2/bulan pada 2025. **PENYEBUT PER TAHUN BELUM
   DIUKUR**, jadi ketujuh angka ini pembilang tanpa penyebut dan DILARANG dibaca
   sebagai laju (aturan 30). **133 simbol** dari 787 punya ≥1 bulan MATI; teratas
   BTCSTUSDT 63, SCUSDT 48, FTTUSDT 43, RAYUSDT 43, CVCUSDT 29.
6. **`kohort_ekor` V4 DIKUATKAN pada satu hal dan DIBATALKAN pada hal lain.**
   Kesepuluh `bulan_hidup_terakhir`-nya dihitung ulang dengan definisi BERBEDA dan
   cocok **10 dari 10**; tetapi klaim "nol kebangkitan" tetap BATAL, dan tak satu
   pun dari kesepuluh simbol itu ada di daftar delapan yang bangkit.
7. **`silang_funding.py` dan `funding.py` sama-sama 705 baris** (aturan 48 melarang
   menambah fungsi sebelum dipecah). BELUM diukur: `lubang_tengah.py` V2,
   `kebangkitan.py` V1, `tests/test_lubang_tengah.py`, `tests/test_kebangkitan.py`.
8. **Utang penulisan yang sengaja TIDAK disunting:** docstring R-225 menulis "tujuh
   fungsi" lalu menyebut sembilan nama (yang benar sembilan); papan skor jurnal 90
   menulis 234 (yang benar 235, dikoreksi di STATE v35).

## PEKERJAAN BERIKUTNYA — diurut untuk tenggat 2 Agustus

1. **Adjudikasi R-236** dari `reports/ci_terakhir.json` pada ref `34ff496b` — murah,
   dan jangan sampai terlewat seperti R-231.
2. **Satu run atomik yang menjawab EMPAT pertanyaan sekaligus** (modul baru; jangan
   tambahkan ke berkas 705 baris; bahan sudah di-commit, tanpa unduhan):
   a. **Penyebut simbol-bulan PER TAHUN** bagi ketujuh angka MATI — tanpa ini
      sebaran tahun tidak dapat ditafsirkan sama sekali.
   b. **H-A013:** keberadaan keenam bulan peralihan (CTK 2025-04, CVC 2025-05, CVX
      2025-07, LIT 2025-12, MAVIA 2025-03, SLP 2025-07) — tidak diterbitkan arsip,
      gagal gerbang 1m, atau masuk 12 simbol-bulan karantina? Ketiganya
      menghasilkan "tidak ada di penyebut" yang sama, jadi medan wajib membedakan
      (aturan 46).
   c. **Cocokkan 3 lubang BNXUSDT (2022-04, -06, -08) dengan 3 simbol-bulan KC-15**
      — keduanya BNXUSDT 2022 dan bercacah 3. Kebetulan yang mencurigakan; wajib
      dicocokkan, dilarang diasumsikan.
   d. **`bulan_hidup_terakhir` bagi 28 anggota kohort di luar sampel abjad**, dengan
      definisi `kebangkitan` V1 yang sudah terbukti cocok 10/10 (aturan 36).
   Push ATOMIK modul + uji + workflow; daftar `def test_` BERNOMOR sebelum meramal
   cacah butir (450 + n); jangan meramalkan cacah baris tanpa membaca ulang utuh.
3. **`ukur_baris` V5** memuat `lubang_tengah.py` V2, `kebangkitan.py` V1, dan modul
   baru — menutup satu utang tiap kali, murah.
4. **Keputusan 7 ADR-A008** — bahannya LENGKAP dan BERCABANG DUA. Wajib: bentuk
   TENGAH dapat menandai jeda yang berakhir (LITUSDT) ATAU penerbitan funding yang
   pulih tanpa perdagangan (BTCSTUSDT 53/53 MATI); penyaringan per simbol-bulan;
   tanpa kata "serentak".
5. **ADR-A003 taksonomi rezim** — berkasnya BELUM ADA, dan delapan kebangkitan
   menyentuhnya langsung: rezim sebuah simbol tidak monoton dan dapat kembali.
6. **Pecah `silang_funding.py`** (705 baris) sebelum satu pun fungsi baru masuk;
   setiap pemecahan wajib memperluas daftar berkas `sidik_kode` (aturan 48) dan
   waspadai aturan 49.
7. **R-199** — jalankan ulang `pulihkan` V2 atas kedelapan pecahan
   (`definisi_dapat_dibedakan` diramalkan false pada indeks 2 dan 5). Sampai itu
   `reports/pulihkan_pecahan_<i>.json` dibaca sebagai laporan V1.
8. **Terima atau tolak ADR-A007** dengan kendala R-146 (839.842.134 sudah memuat
   516.135 baris karantina). Terapkan ADR-A006 sepenuhnya; `dugaan_pengganti`
   (ADR-A005); karantina artefak 7 hari; adjudikasi R-7, R-19, R-20, R-28, R-36,
   R-37.
9. Kehidupan 12 simbol-bulan karantina (tar terpisah, belum disentuh).
10. Belum diukur (daftar penuh di bagian terakhir STATE v35): sebab kebangkitan
    kedelapan simbol, sebab KC-15, 15 SETTLED lain, INDEKS 3 nama manual, token
    saham dan komoditas, 16 simbol non-ASCII, `.decode("utf-8","replace")`,
    BUSD/USDC, jurang 38 lawan 41, skew `waktu_utc`,
    `funding_selisih_penuh.json` (`daftar_terpotong` true), selisih byte AGIX 531
    lawan 529, `tests/test_pulihkan.py` belum dibaca ulang.
11. Paralel (aturan 3): juri T4 dengan biaya, lapisan validasi (Šidák, ≥300
    permutasi per TANGGAL UTC, PBO dan DSR numpy murni). **Adjudikasi riset TETAP
    TERKUNCI.**

## KEBIASAAN

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. Berkepala dua yang separuh
  salah = SEPARUH. Penyebut nol = TIDAK TERADJUDIKASI. Run yang tak akan menyala =
  DILARANG diramalkan (55). Commit yang tak akan ada = DILARANG (56). Cacah butir
  tanpa daftar bernomor = DILARANG (57). Cacah baris berkas yang belum dibaca ulang
  utuh = pita lebar atau tidak meramal (58). Penegasan KETIADAAN tanpa penyebut
  yang mampu memuat gejalanya = DILARANG (59). **Memindahkan MEKANISME dari satu
  kasus yang menang = DILARANG (60). Memakai medan satu jalur sebagai medan jalur
  lain = DILARANG (61).**
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21). Jangan menaksir
  yang bisa dihitung. Jumlahkan tabel dengan tangan sebelum mendorongnya.
- **Jangan menyunting angka ramalan yang sudah didorong.** R-230 dan R-234 adalah
  dua kekalahan paling berharga justru karena angkanya dibiarkan, dan keduanya
  berlawanan arah: satu menegaskan ketiadaan, satu memindahkan sebab.
- Rancang uji yang BISA gugur. `uji_h_a012` menuntut LEBIH DARI SATU simbol;
  satu simbol saja berarti LITUSDT tetap tunggal.
- Aturan 24 medan penggugur; 37 sampel wajib memuat ≥1 kasus tiap kelas cacat
  relevan; 20 dilarang menyimpulkan di luar rentang disampel; 46 kode dilarang
  menyimpulkan dari penyebut nol; 50 kesimpulan dari KETIADAAN wajib kendali
  positif; 51 jendela mundur adaptif — **dibenarkan telak oleh delapan kebangkitan
  yang tak terlihat dari jendela mundur 2025-07**; 52 laporan tak terbaca utuh
  setara tak ada; 53 baca PERILAKU fungsi sebelum meramal kode keluar.
- Pisahkan arah sebuah irisan: A→B dan B→A adalah dua angka.
- Bila dua definisi memberi angka berbeda, tulis keduanya berdampingan dengan
  penyebutnya (aturan 36). Bila dua kasus memberi mekanisme berbeda, tulis KEDUA
  cabangnya (aturan 60).
- Push yang menyalakan run wajib atomik (aturan 45): modul + uji + workflow.
- BACA berkas sebelum menuduhnya salah. Sebaliknya, jangan menuduh modul ketika
  yang salah adalah harapan uji, jangan menuduh laporan tertimpa ketika yang salah
  adalah pemicu workflow, jangan menuduh pytest ketika yang salah adalah cacahanmu
  sendiri, jangan menuduh arsip cacat ketika bentuk datanya justru menjelaskan
  dirinya, jangan menuduh sebuah gejala tidak ada ketika yang belum ada adalah
  pengukurannya, dan **jangan menuduh dua kasus sejenis hanya karena bentuk
  datanya sama.**
- Pisahkan fakta dari asumsi; tanpa bukti tulis "Ini memerlukan verifikasi."
- "lanjut" berarti teruskan tanpa konfirmasi. Perbarui STATE.md, jurnal, dan berkas
  ini secara berkala. Jangan berhenti dengan alasan konteks Notion; patokannya
  konteks model.
- **Tenggat: 2 Agustus 2026.** Percepat dengan menumpuk pertanyaan per run, bukan
  dengan melewatkan verifikasi.
