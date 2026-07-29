# STATE — versi 40

Diperbarui: 2026-07-30 (sesi 56, lanjutan). Aturan hanya BERTAMBAH; jangan menulis
ulang dari ingatan. v40 disusun di atas teks v39 yang dibaca langsung dari `main`
(blob **`f8078dd20f0b3fc1bf738f0befdb97cb934f4f16`**, dibaca **UTUH** sebelum satu
huruf pun ditulis), ditambah jurnal **114** (blob `e1413bf2472f82d4db6d84588be8471ba06ba1ff`)
dan **115** (blob `67c21c1776e71681fdefa51c1d214ec4c87ff819`), keduanya UTUH;
`lux_ai/serapan/silang_funding.py` (blob **`42c3aa9dc2c16220b79cf9c9e46979dd000fd393`**,
UTUH), `lux_ai/serapan/kehidupan_arsip.py` (blob **`318a5cb187406d16cfd3385d653bed905f632934`**,
UTUH), `lux_ai/serapan/bulan_absen.py` (blob **`10279d721d66a86b6d265badf81ada3204648f69`**,
UTUH), `tests/test_bulan_absen.py` (blob **`d4f2ee5ae1c7259c929bc707c51794b9b4800046`**,
UTUH), `reports/bulan_absen_ringkas.json` (blob **`e450d9f95e9bca0dc28a0e01c6aad6594c4fa3d6`**,
UTUH, ref runner **`8b0e0182`**), dan `reports/ci_terakhir.json` blob
**`2d8530215e5d548483589d431f69446cd14a0c4c`** (**694**).

**KOREKSI PAPAN SKOR YANG WAJIB DIBACA LEBIH DULU.** v39 mencatat total **287**.
Itu sudah basi sejak jurnal 114. Angka benar sekarang **290** (R-1..R-290,
seluruhnya teradjudikasi atau menunggu). Rinciannya di bagian papan skor.

Yang lahir sejak v39: aturan **76**; KC-**39**; adjudikasi **R-288, R-289,
R-290**; praregistrasi **R-291**; modul `bulan_absen` V1; dan pengukuran pertama
bulan ABSEN atas seluruh 787 nama — yang menutup utang "identitas selisih 12"
yang hidup sejak jurnal 92.

Berkas yang TIDAK dibaca ulang pada sesi 56 dan karena itu tidak diubah angkanya
di sini: `lux_ai/serapan/lubang_tengah.py` (blob `4d3beaf1`, dibaca UTUH di jurnal
111), `decisions/ADR-A002.md`, `ADR-A004.md`, `ADR-A006.md`, `ADR-A007.md`,
`PETA_MODUL.md`, `.github/workflows/bulan_absen.yml` (didorong, belum dibaca ulang).

Lima peristiwa terbesar sejak v39:

1. **Bulan ABSEN TERUKUR atas seluruh 787 nama, bukan lagi dugaan atas 15.**
   **11** bulan absen di dalam rentang, **0** di luar 15 pasangan SETTLED, dan
   kedua belas simbol-bulan karantina akhirnya BERNAMA (11 dalam rentang + 1 tepi).
2. **Mekanisme KEDUA bagi H-A015.** 9 dari 9 pasangan berabsen-satu punya bulan
   absen yang SAMA PERSIS dengan `bulan_settled_terakhir` — kali ini dari gerbang
   KLINES, sumber data yang sama sekali lain daripada arsip funding di jurnal 112.
3. **H-A014 bentuk baru MENANG, bentuk lama salah bentuk.** Bulan SETTLED bukan
   bulan MATI di tengah hidup nama dasarnya, melainkan bulan yang ABSEN dari
   daftar bulan lolos nama dasarnya. LITUSDT 2025-12 terbukti persis begitu.
4. **Aturan 76 dan KC-39** — dua penyebut "bulan yang hilang" (rentang LOLOS lawan
   daftar DIDAFTAR arsip) tidak boleh dipertukarkan. Ini yang mengalahkan R-288.
5. **CI 662 → 694**, terverifikasi pada ref runner.

## Aturan bernomor

Aturan **1–36** berlaku tanpa perubahan; teks di STATE v19 (blob `e06c486e…`),
ringkas nomornya di v37 (blob `f520d5e2`).

Aturan **37, 39–45, 47, 49, 51, 53, 54, 56, 59–62** berlaku tanpa perubahan dan
teks penuhnya ada di v37 (blob `f520d5e2`). Ringkas satu baris: 37 kelas cacat
pada sampel · 39 keseragaman sampel bukan ramalan · 40 uji silang baris ·
41 penyebut nol → TIDAK TERADJUDIKASI · 42 kelas cacat butuh angka terukur ·
43 toleransi berskala · 44 ramalan menyebut penyebut · 45 keatomikan push pemicu ·
47 satuan cacah tersurat · 49 re-export tetap mematahkan uji · 51 jendela mundur
adaptif · 53 ramalan kode keluar butuh pembacaan perilaku · 54 cacah `def test_`
satu per satu · 56 "commit BERIKUTNYA yang menyentuh X" · 59 ketiadaan gejala
butuh penyebut · 60 mekanisme tak dipindah antarkasus · 61 medan tak dipindah
antarjalur · 62 daftar tak diminta dari laporan bercacah.

Yang berikut memuat angka atau daftar kepatuhan, jadi ditulis agak penuh:

38. Cacah uji hanya sah dari `reports/ci_terakhir.json` (run id + commit +
    `kode_keluar`). Laporan dapat TERTIMPA run berikutnya; temukan ref runner
    lewat `list_commits` dengan `path="reports/<berkas>.json"`. **[v40] Ditaati
    empat kali lagi**: R-289 dua cabang pada ref `fda544a0` (run 30475448183) dan
    `c4a60f4f` (run 30475625553); R-290 pada **`9698c36b`** (run 30477143164);
    R-288 pada **`8b0e0182`** (run 30477142893). Total pemakaian tercatat: empat
    belas. Perangkap ini menyala berulang: sesudah push, laporan di `main` sudah
    memuat commit run BERIKUTNYA.
46. Kode dilarang menyimpulkan dari penyebut nol; medan yang menyimpulkan wajib
    memeriksa lebih dulu apakah kasusnya mampu membedakan. Ditaati `terhenti`
    V2/V4, `silang_settled` V1, dan **[v40] `bulan_absen` V1** (`rentang`,
    `selisih_rentang`, dan `konsisten_rentang` bernilai **null** bagi nama tanpa
    bulan sah, bukan nol; `bulan_ke_indeks` mengembalikan None atas bentuk cacat).
48. Berkas modul yang mendekati pagar 800 baris dipecah SEBELUM fungsi baru
    ditambahkan. Berlaku atas `funding.py` dan `silang_funding.py` (705 SERI).
    **RENCANANYA DITINJAU [v39], DIPERKUAT [v40]:** preseden MENGIMPOR kini sudah
    tiga kali — `lubang_tengah.py`, `silang_settled.py`, dan `bulan_absen.py`
    memakai fungsi `silang_funding` tanpa menyalinnya, sehingga definisi tetap SATU
    (aturan 36) dan `sidik_kode` laporan lama tidak batal. Pemecahan hanya boleh
    dijalankan bila ada alasan yang mengalahkan preseden ini.
50. Setiap pengukuran yang menyimpulkan dari KETIADAAN wajib memuat kendali
    positif. `terhenti` V2..V4 `kendali_sah` true; `silang_settled` V1 true;
    **[v40] `bulan_absen` V1 true** — BTCUSDT dan ETHUSDT masing-masing **78**
    bulan lolos dengan **0** bulan absen. Kendali ini penting justru karena seluruh
    kesimpulannya bersandar pada KETIADAAN bulan di penyebut.
52. Laporan yang tidak dapat dibaca utuh setara dengan laporan yang tidak ada.
    Ekor SETIAP berkas kode dan berkas panjang yang didorong wajib dibaca sesudah
    push. **[v40] Ditaati atas jurnal 114, jurnal 115, STATE v39, PROMPT v42,
    `bulan_absen.py`, dan `tests/test_bulan_absen.py`.** Yang tetap tak terbaca
    utuh: `reports/silang_funding.json` 183.963 B dan **[v40]
    `reports/bulan_absen.json` 249.992 B** — keduanya dianggap TIDAK ADA; yang
    berlaku adalah berkas ringkasnya.
55. Sebelum meramalkan hasil workflow, baca `paths`/`paths-ignore` dan sebutkan
    workflow MANA yang menyala. `ci.yml` mengabaikan `journal/**`, `decisions/**`,
    `hipotesis/**`, `reports/**`. `ukur_baris.yml` hanya atas
    `lux_ai/serapan/ukur_baris.py`; `semesta_kuota.yml` hanya atas
    `lux_ai/serapan/semesta_kuota.py`; `terhenti_semesta.yml` hanya atas
    `lux_ai/semesta/terhenti.py` dan dirinya sendiri; `silang_settled.yml` hanya
    atas `lux_ai/serapan/silang_settled.py`; **[v40] `bulan_absen.yml` hanya atas
    `lux_ai/serapan/bulan_absen.py`**.
57. Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB ditulis
    BERNOMOR dan nomor terakhirnya dipakai sebagai cacahan. **TERBUKTI BEKERJA
    ENAM BELAS DARI ENAM BELAS [v40]:** 382, 396, 450, 494, 526, 552, 584, 598,
    610, 623, 630, 630, 638, 662, 662, 662, **694**. Mekanismenya deterministik —
    itu sebab keberhasilannya, bukan kecakapan meramal, dan setiap kemenangannya
    wajib disebut **MUDAH**.
58. Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH dalam
    giliran yang sama DILARANG diramalkan dengan pita sempit. Pilih: (a) baca
    ulang utuh; (b) pita batas atas ≥1,8× batas bawah; (c) jangan meramal, ukur.
63. **[DIAMANDEMEN v37, DIPERKUAT v38]** Setiap klaim tentang kematian,
    kebangkitan, lubang funding, dan `bagian_mati` WAJIB menyebut batas
    semestanya secara tersurat: penyebut **787** simbol adalah `perpetual_usdt`,
    dan ia PERSIS seluruh perpetual USDT di arsip. Semesta arsip **937** simbol,
    **21.789** bulan; **150** hanya-arsip; **0** hanya-penyebut. Frasa lama
    "hampir seluruhnya BUSD/USDC" **DICABUT** (terukur 80 dari 147). Pada bulan
    tutup semesta **49 nama di luar penyebut masih terbit**. **[v40] Penyebut 787
    kini terkonfirmasi dari arah ketiga:** `bulan_absen` V1 melaporkan
    `cacah_nama_penyebut` **787** dan `selisih_nama_penyebut` **0** atas 19.586
    simbol-bulan, serta `cacah_nama_didaftar` **787** dari manifes.
64. Ramalan tentang nilai EKSTREM wajib menyebut perlakuan atas SERI, dan medan
    yang menamai pemegang ekstrem wajib melaporkan SELURUH pemegangnya bila seri.
    Perbaikan wajib di `ukur_baris` **V6**; `semesta_kuota` sudah benar sejak V1.
65. Setiap daftar contoh WAJIB menyebut CARA pemilihannya, dan kalimat sifat
    tentang KESELURUHAN himpunan DILARANG disusun dari contoh yang bukan
    seluruhnya. Contoh yang benar: sampel `diagnosa_kc15` berlapis atas delapan
    pecahan, dan modul itu menyatakannya. **[v40] Contoh kedua:** daftar 12
    karantina di bawah adalah SELURUHNYA, sebab penyebutnya seluruh 787 nama.
66. **[lahir salah lalu DIREVISI]** Setiap cacahan semesta wajib menyebut KELAS
    INSTRUMEN yang dicacah. **Sebelum menuduh sebuah batas tidak ada, berkas
    penyaringnya WAJIB dibaca lebih dulu.** Perluasan: sebelum menulis modul baru,
    LISTING direktori paket dan direktori workflow lebih dulu. **[v40] DITAATI dan
    langsung berbayar:** listing sebelum `bulan_absen` menemukan `lux_ai/serapan/`
    berisi **37** berkas dan `.github/workflows/` berisi **31** — bukan 30 seperti
    tercatat sejak jurnal 107; yang luput adalah `silang_settled.yml` (`78d8051c`).
    Sesudah push `bulan_absen`: paket **38**, workflow **32**.
67. **[v38] Keanggotaan semesta dan keberlangsungan hidup adalah DUA SUMBU; satu
    DILARANG disimpulkan dari yang lain.** Terukur pada bulan tutup 2026-06: dari
    937 nama arsip **808 masih terbit** dan **129 terhenti**; dari 787 nama
    penyebut **759 masih terbit** dan **28 terhenti**; **49** nama yang masih
    terbit berada DI LUAR penyebut. Angka **28** DILARANG dicampur dengan **1.401**
    MATI, **98** SEPI, atau `cacah_simbol_tanpa_hidup` **18**. Lihat KC-30.
68. **[v38] Nama turunan dan nama asal dapat terbit BERSAMAAN.** Kehadiran nama
    turunan (`SETTLED`) DILARANG dibaca sebagai berhentinya nama asal; bulan
    terakhir keduanya wajib dilaporkan BERPASANGAN. Dari 15 nama SETTLED hanya
    **dua** yang nama dasarnya berhenti terbit (`SXPUSDT` 2026-05, `BDXNUSDT`
    2026-03). Lihat KC-31.
69. **[v39, jurnal 107] Setiap nama turunan wajib disebut bersama nama asalnya,
    dan setiap kelompok nama wajib punya pemeriksaan silang ke pengukuran lain atas
    besaran yang sama.** Terbayar dua kali: jumlah kolom bulan tabel 15 pasangan
    `terhenti` V4 = **36** sama dengan `bulan_settled.py` V1; dan **[v40]** 11
    bulan absen + 1 bulan tepi = **12** sama dengan 19.598 − 19.586 yang diukur
    `semesta_kuota` V3 dengan kode lain atas bahan lain. **Pengukuran yang tak
    dapat dicocokkan dengan pengukuran lain mana pun harus dianggap belum diuji.**
70. **[v39, jurnal 108, lahir dari R-281] Sebelum praregistrasi dikunci, setiap
    butir yang saling menentukan wajib dijumlahkan silang; praregistrasi yang tidak
    konsisten dengan dirinya sendiri adalah ramalan CACAT, dan kecacatannya milik
    peramal, bukan milik data.** Lihat KC-34.
71. **[v39, jurnal 109, lahir dari R-282] Sebelum mempraregistrasi ramalan atas
    laporan yang belum pernah dibaca, modul penghasilnya wajib dibaca lebih dulu.**
    Ramalan atas medan yang tidak pernah diukur laporan itu gugur otomatis dan
    tidak boleh dihitung sebagai kekalahan data.
72. **[v39, jurnal 110] Sebuah laporan hanya membuktikan apa yang benar-benar
    disampelnya.** Setiap adjudikasi wajib menyebut penyebut sampel laporan sebelum
    menyebut putusannya. **Turunan yang mengikat:** angka terbitan wajib disebut
    bersama penyebutnya — 880 lubang funding (seluruhnya) lawan 877 (di dalam
    19.586). **[v40] Dilanggar sendiri lagi di R-288**: penyebut BNXUSDT tertukar.
73. **[v39, jurnal 111, lahir dari R-284] Dilarang mempraregistrasi ramalan atas
    ISI sebuah berkas yang belum pernah dibaca ketika satu-satunya dasar ramalan
    adalah NAMA berkas itu.** Bila sebuah berkas perlu diketahui, bacalah —
    pembacaan tidak butuh run, tidak butuh jaringan, dan tidak berbiaya.
74. **[v39, jurnal 112, lahir dari R-285] Setiap nol yang dipakai sebagai dasar
    ramalan wajib disebut bersama PENYEBUT dan DEFINISI ujinya.** Lihat KC-37.
    **[v40] Dipakai dengan benar:** nol `tak_diterbitkan_arsip` (0 dari 11) dan nol
    absen pada lima pasangan disebut bersama penyebutnya masing-masing.
75. **[v39, jurnal 113, lahir dari R-286] Setiap cacahan "cocok" wajib disertai
    medan pembeda MEKANISME, dan pita ramalan wajib menyebut mekanisme mana yang
    dihitung.** Lihat KC-38. **[v40] Ditaati:** `bulan_absen` V1 membawa medan
    `pembeda_absen` yang memisahkan `gagal_gerbang` dari `tak_diterbitkan_arsip`,
    dan hasilnya 11 lawan 0 — satu mekanisme saja yang bekerja.
76. **[v40, jurnal 115, lahir dari R-288] Setiap cacah "bulan yang hilang" wajib
    menyebut apakah penyebutnya RENTANG bulan LOLOS (`bulan_terakhir` −
    `bulan_pertama` + 1 lawan `cacah_bulan_lolos`) atau DAFTAR bulan DIDAFTAR
    arsip (`bulan_didaftar`), dan angka dari kedua penyebut itu DILARANG
    dijumlahkan atau dipertukarkan.** Kasus asalnya: BNXUSDT punya **3** bulan
    gagal gerbang tetapi hanya **2** bulan absen, sebab 2022-04 adalah bulan
    didaftar PERTAMA dan gagal, sehingga ia terlempar ke luar rentang. Menyalin
    angka 3 ke butir yang berpenyebut rentang mengalahkan R-288 butir 1 dan 3.
    Pengetatan aturan 44 dan kerabat langsung KC-36. Lihat KC-39.

## Kelas cacat

KC-1 s.d. KC-12 seperti v19; KC-10 dan KC-11 DITUTUP. KC-13 keterwakilan sampel
(penangkal aturan 37). **KC-16 DITARIK — nomornya TETAP kosong selamanya.**
KC-17 DITUTUP. Teks penuh KC-14, KC-15, KC-19–KC-29 ada di v37 (blob `f520d5e2`);
yang wajib dibawa:

- **KC-14** — menit hilang NYATA di arsip 1m: **9** simbol-bulan, **6.375** menit
  (425×15). Sebab tak diketahui (H-A004 tak dapat diuji). Karantina (ADR-A006).
- **KC-15 [DIKOREKSI v39]** — klines BULANAN kehilangan HARI UTC penuh: **3**
  simbol-bulan, semuanya BNXUSDT 2022 (**2022-04, 2022-06, 2022-08**), **7.200**
  menit = **5 hari UTC**. **Hari-hari itu UTUH di arsip HARIAN** — jurnal 109 §5.2
  DICABUT. Yang benar-benar tak terjelaskan hanyalah **210 menit TEPI** pada
  2022-04, konsisten dengan peluncuran pukul **03:30 UTC**
  (`stempel_pertama_ms` 1648783800000; berkas harian 2022-04-01 memuat 1.230 =
  1.440 − 210 baris; `menit_tepi_hadir` 0 dari 210). Anatomi bulan itu:
  `cacah_baris_1m` 41.550, `menit_kalender` 43.200, `menit_hilang_di_tengah`
  **1.440**, `tepi_awal` 210, `gerbang_lolos` **false**, `putusan`
  TEPI_TAK_TERJELASKAN, `checksum_bulanan` `14bd6937…`. 43.200 − 41.550 = 1.650 =
  1.440 + 210 ✅ Pembagian 5 hari ke tiga bulan BELUM diukur. 9 + 3 = **12**
  karantina; 6.375 + 7.200 = **13.575** menit; **516.135** baris. **[v40] Kedua
  belas karantina itu kini BERNAMA — lihat bagian "Bulan ABSEN"; dan KC-39
  mengikat: hanya 11 dari 12 yang berupa bulan ABSEN, sebab BNXUSDT 2022-04 ada
  di TEPI.** Kebijakan ADR-A007 masih DIUSULKAN.
- **KC-18** — lilin datar lolos gerbang struktural; gerbang menilai BENTUK, bukan
  kehidupan. Semesta `perpetual_usdt` atas **19.586** simbol-bulan lolos: **1.401
  MATI** (7,153%), **98 SEPI** (0,500%), **18.087 HIDUP** (92,35%); 945 MATI di
  luar kohort puncak. Dari 1.401 MATI, **842** kehilangan funding dan **559**
  tetap berfunding. **Kematian dapat berbalik** — LITUSDT MATI 2025-02..2025-11
  lalu **HIDUP 2026-01..2026-06 terukur**. Kematian permanen tetap punya contoh
  telak: BTCSTUSDT 53 dari 53 MATI. **Kecocokan bulan membuktikan PENAMAAN
  kontrak, bukan perdagangan** — mengikat atas H-A013, H-A014, H-A015, dan
  seluruh laporan `silang_settled` maupun **`bulan_absen`**. ADR-A008 Keputusan
  1–6 DITERIMA; Keputusan 7 DITANGGUHKAN.
- **KC-19** mencacah dari ingatan (aturan 57). **KC-20** taksiran baris bias ke
  BAWAH (58). **KC-21** ketiadaan gejala dari ketiadaan pengukuran (59). **KC-22**
  memindahkan MEKANISME (60). **KC-23** memindahkan MEDAN (61). **KC-24** bertanya
  DAFTAR kepada laporan bercacah (62). **KC-25** batas semesta tak tersurat (63).
  **KC-26** medan ekstrem membisu tentang SERI (64). **KC-27** mengarakterisasi
  himpunan dari contoh BERURUT (65). **KC-28** mencampur kelas instrumen — berlaku
  atas arsip **937**, BUKAN atas penyebut 787 (66). **KC-29** taksonomi PARALEL
  (lubang aturan 22).
- **KC-30** — membaca NAMA KELAS sebagai KEADAAN. Penangkal 67.
- **KC-31** — membaca nama PERISTIWA sebagai MEKANISMENYA. Penangkal 68.
- **KC-32** — mencampur DUA SISTEM PENOMORAN (utang verifikasi nomor 28 lawan
  **ramalan R-28**). **R-28 tetap MENUNGGU**; bunyinya ada di STATE v23 dan belum
  dibaca. Teks jurnal 105 TIDAK disunting (aturan 29).
- **KC-33 [v39] — mengenali satu peristiwa lalu berhenti mencari yang kedua.**
  `SXPUSDTSETTLED` disebut satu-satunya peristiwa penamaan; **`BDXNUSDT`** adalah
  yang kedua dan sudah SELESAI. Pencarian pola WAJIB atas seluruh rentang.
- **KC-34 [v39] — menurunkan cacah subkelompok dengan pengurangan di kepala** lalu
  memakainya tanpa mencocokkannya ke jumlah yang sudah dipegang. Penangkal 70.
- **KC-35 [v39, DIPERSEMPIT] — menyamakan CAKUPAN kode cacat dengan CAKUPAN satu
  laporan yang namanya memuat kode itu.** Penangkal aturan 72.
- **KC-36 [v39] — homonim di dalam kosakata riset sendiri diperlakukan sebagai satu
  konsep** ("tengah", "lubang"). Penangkal aturan 73. **[v40] `bulan_absen.py`
  menuliskan pembedaan itu tersurat di docstringnya: lubang funding dan lubang
  tengah ADA di penyebut, bulan ABSEN TIDAK ADA di penyebut.**
- **KC-37 [v39] — memakai nol dari satu penyebut sebagai bukti ketiadaan gejala di
  penyebut lain.** Penangkal aturan 74.
- **KC-38 [v39] — mencacah "kecocokan" tanpa membedakan MEKANISMENYA.** Penangkal
  aturan 75.
- **KC-39 [v40, jurnal 115, lahir dari R-288] — mencampur dua penyebut "bulan yang
  tidak ada di penyebut": bulan absen DI DALAM rentang lawan bulan gagal gerbang
  di TEPI riwayat.** Bulan tepi TIDAK dapat absen menurut definisi rentang, sebab
  bulan pertama yang LOLOS menjadi batas rentang. Maka cacahan yang tampak sama
  menghasilkan dua bilangan yang keduanya benar: BNXUSDT **3** gagal gerbang lawan
  **2** absen. Kerabat KC-36 (homonim) dan KC-35 (cakupan). Penangkal aturan 76.

## Semesta riset = `perpetual_usdt` = penyebut 787 — TERBUKTI TIGA ARAH [v40]

Sumber: `semesta_kuota.py` **V3**, commit `db4a192d`, run 30456422183, laporan
blob `8adae5ee` (UTUH), `sidik_kode` `ef0c4a24…`, `bukan_bukti` false.

- `cacah_perpetual_usdt` **787** = `cacah_penyebut_simbol` **787**
- `cacah_perpetual_usdt_luar_penyebut` **0**; `cacah_penyebut_bukan_perpetual_usdt`
  **0**; `cacah_penyebut_bukan_akhiran_usdt` **0**; `cacah_penyebut_luar_arsip`
  **0**; `penyebut_bagian_arsip` true.
- **[v40] Arah ketiga:** `bulan_absen` V1 atas laporan kehidupan menemukan
  `cacah_nama_penyebut` **787** (`selisih_nama_penyebut` 0) dan dari manifes
  `cacah_nama_didaftar` **787** — kode lain, bahan lain, angka sama (aturan 69).

Karena KEDUA arah nol, ini **kesamaan himpunan**, bukan himpunan bagian.

Batas yang wajib ikut disebut (`taksonomi.CATATAN_BATAS`): token **saham, ETF, dan
komoditas** (mis. `AAPLUSDT`, `XAUUSDT`) tak dapat dibedakan lewat bentuk nama,
jadi mereka **IKUT di dalam 787**. `AAPLUSDT:2026-05` terbukti nyata di dalam
sampel `diagnosa_kc15` dan bulannya lolos gerbang bersih.

### Taksonomi kanonik — sembilan kelas

Berkas `lux_ai/semesta/taksonomi.py` (blob `b418c7ba`). Urutan pemeriksaan
MENGIKAT: pola ekspirasi `_\d{6}$` → akhiran `SETTLED` → daftar `INDEKS` → kutipan
`("USDT","USDC","BUSD","USD1","BTC")` dengan `BTC` sebagai `KUTIPAN_NON_FIAT`.
`INDEKS` = {`DEFIUSDT`, `BTCDOMUSDT`, `BLUEBIRDUSDT`}, manual, tersurat. Maka
**790 nama berakhiran USDT = 787 perpetual + 3 indeks**, tanpa sisa.

| jenis kanonik | nama (arsip 937) | bulan | hanya-arsip (150) | bulan |
|---|---:|---:|---:|---:|
| `perpetual_usdt` | **787** | **19.598** | 0 | 0 |
| `futures_kedaluwarsa` | 50 | 258 | 50 | 258 |
| `perpetual_busd` | 41 | 812 | 41 | 812 |
| `perpetual_usdc` | 39 | 893 | 39 | 893 |
| `sisa_settled` | 15 | 36 | 15 | 36 |
| `indeks` | 3 | **151** | 3 | **151** |
| `perpetual_usd1` | 1 | 2 | 1 | 2 |
| `basis_non_fiat` | 1 | 39 | 1 | 39 |
| `tak_tergolong` | **0** | 0 | 0 | 0 |
| **jumlah** | **937** | **21.789** | **150** | **2.191** |

Dihitung tangan (aturan 21): 787+50+41+39+15+3+1+1 = **937** ✅ ·
19.598+258+812+893+36+151+2+39 = **21.789** ✅ · 21.789 − 2.191 = **19.598** ✅

**ANGKA WARISAN YANG DICABUT.** "16 simbol non-ASCII" adalah HANTU. Terukur
**3 nama / 19 bulan**: 币安人生USDT 9, 我踏马来了USDT 6, 龙虾USDT 4; 9+6+4 = **19** ✅
Ketiganya `perpetual_usdt`, jadi ADA di penyebut. Asal-usul angka 16 tetap belum
diketahui.

### Taksonomi LOKAL modul (kuota) — dipertahankan berdampingan

USDT 805 nama/19.785 bulan (15 SETTLED) · TAK_DIKENAL 51/260 · BUSD 41/812 ·
USDC 39/893 · BTC 1/39. `TAK_DIKENAL` 51 = 50 `futures_kedaluwarsa` + 1
`perpetual_usd1` (`BTCUSD1`); 258 + 2 = 260 ✅ **150 hanya-arsip = 147
bukan-akhiran-USDT + 3 indeks**; dari 147 itu BUSD+USDC = **80** (54,4%).

### Penguraian selisih 163 — identitas utuh, dan kini bernama

`bulan_usdt_bukan_settled` 19.749 · `bulan_arsip_milik_penyebut` **19.598** ·
`bulan_arsip_milik_hanya_arsip` **151** · `bulan_lolos_gerbang` 19.586 ·
`selisih_total` **163** · `selisih_dalam_penyebut` **12** ·
`selisih_dari_hanya_arsip` **151** · `identitas_utuh` true.
19.598 + 151 = 19.749 ✅ · 12 + 151 = 163 ✅ · 19.598 − 19.586 = **12** ✅

**151 bulan itu SELURUHNYA milik ketiga indeks.** Dan **[v40] angka 12 kini bukan
lagi kesamaan angka belaka: kedua belasnya bernama** — lihat bagian berikut.

## Bulan ABSEN — TERUKUR atas seluruh 787 nama [v40, `bulan_absen` V1]

Sumber: `lux_ai/serapan/bulan_absen.py` V1 (blob **`10279d72`**, dibaca UTUH),
laporan `reports/bulan_absen_ringkas.json` blob **`e450d9f9`** pada ref runner
**`8b0e0182`** (run **30477142893**), dibaca UTUH. Laporan penuh
`reports/bulan_absen.json` **249.992 B** dengan `sidik_sumber` `d2fc3bfb…`
BELUM terbaca utuh dan karena itu dianggap TIDAK ADA (aturan 52). `sidik_kode`
**`0294eb3a…`**, `versi_bulan_absen` 1, `bukan_bukti` false.

**Definisi, tersurat (aturan 76, KC-36, KC-39):** bulan ABSEN adalah bulan
kalender di antara `bulan_pertama` dan `bulan_terakhir` sebuah simbol yang TIDAK
ADA di penyebut 19.586. Ia **bukan** lubang funding dan **bukan** lubang tengah —
keduanya ADA di penyebut. Bulan gagal gerbang yang jatuh di TEPI riwayat **bukan**
bulan absen.

Penggugur SELURUHNYA aman (aturan 24): `sidik_seragam` true (satu sidik
`24b6bb26…`) · `cacah_laporan_dibaca` 8/8 · `cacah_kunci_ganda` 0 · `kendali_sah`
true · `selisih_penyebut` **0** · `cacah_pasangan` 15 · `selisih_nama_penyebut`
**0** · `sumber_pembeda_ada` true (`manifes_hilang` []) · kode keluar **0**.
Kendali positif: **BTCUSDT 78 bulan / 0 absen** dan **ETHUSDT 78 bulan / 0 absen**.

### Angka pokok

| medan | nilai |
|---|---:|
| `jumlah_bulan_absen` (787 nama) | **11** |
| `cacah_nama_berabsen` | **10** |
| `jumlah_bulan_absen_pasangan` (15 SETTLED) | **11** |
| `jumlah_bulan_absen_luar_pasangan` | **0** |
| `cacah_nama_tak_konsisten_rentang` | **0** |
| `sebaran_pembeda.gagal_gerbang` | **11** |
| `sebaran_pembeda.tak_diterbitkan_arsip` | **0** |
| `sebaran_pembeda.tak_terukur` | **0** |

Jadi tidak satu pun bulan absen lahir karena arsip tidak menerbitkannya;
kesebelasnya diterbitkan arsip lalu **gagal gerbang 1m**. Nol
`tak_diterbitkan_arsip` hanya boleh diklaim karena pembedanya ADA (aturan 59).

### Dua belas simbol-bulan karantina — SELURUHNYA bernama

19.598 − 19.586 = 12. Kedua belasnya (aturan 65: ini seluruhnya, penyebutnya 787):

| # | simbol | bulan | kedudukan | = bulan SETTLED terakhir? |
|---|---|---|---|---|
| 1 | AERGOUSDT | 2025-04 | dalam rentang | ya |
| 2 | AIAUSDT | 2026-01 | dalam rentang | ya |
| 3 | BNXUSDT | 2022-06 | dalam rentang | tidak |
| 4 | BNXUSDT | 2022-08 | dalam rentang | tidak |
| 5 | CTKUSDT | 2025-04 | dalam rentang | ya |
| 6 | CVCUSDT | 2025-05 | dalam rentang | ya |
| 7 | CVXUSDT | 2025-07 | dalam rentang | ya |
| 8 | LITUSDT | 2025-12 | dalam rentang | ya |
| 9 | MAVIAUSDT | 2025-03 | dalam rentang | ya |
| 10 | PUMPUSDT | 2025-07 | dalam rentang | ya |
| 11 | SLPUSDT | 2025-07 | dalam rentang | ya |
| 12 | BNXUSDT | 2022-04 | **TEPI** (KC-39) | tidak |

11 + 1 = **12** ✅ sama dengan 19.598 − 19.586.

**PERINGATAN aturan 71/73 yang WAJIB diwarisi:** tabel ini adalah bulan yang ABSEN
dari penyebut ditambah satu bulan tepi yang sudah teranatomi. Daftar
`parquet_karantina` di manifes **belum pernah dibaca**, jadi kesamaan keduanya
adalah dugaan beraritmetika — itulah isi **R-291**, dan sebelum R-291 diadjudikasi
frasa "inilah kedua belas karantina" DILARANG ditulis tanpa peringatan ini.

### Rentang lawan lolos per pasangan SETTLED — TERUKUR

| simbol | pertama | terakhir | rentang | lolos | absen | bulan absen | bulan SETTLED | cocok |
|---|---|---|---:|---:|---:|---|---|---|
| AERGOUSDT | 2024-09 | 2026-06 | 22 | 21 | 1 | 2025-04 | 2025-04 | **ya** |
| AIAUSDT | 2025-09 | 2026-06 | 10 | 9 | 1 | 2026-01 | 2026-01 | **ya** |
| BDXNUSDT | — | 2026-03 | 10 | 10 | 0 | — | 2026-04 | tidak |
| BNXUSDT | 2022-05 | 2026-06 | 50 | 48 | 2 | 2022-06, 2022-08 | 2023-02 | tidak |
| CTKUSDT | 2020-11 | 2026-06 | 68 | 67 | 1 | 2025-04 | 2025-04 | **ya** |
| CVCUSDT | 2020-11 | 2026-06 | 68 | 67 | 1 | 2025-05 | 2025-05 | **ya** |
| CVXUSDT | 2022-09 | 2026-06 | 46 | 45 | 1 | 2025-07 | 2025-07 | **ya** |
| ICPUSDT | 2021-05 | 2026-06 | 62 | 62 | 0 | — | 2022-09 | tidak |
| LITUSDT | 2021-02 | 2026-06 | 65 | 64 | 1 | **2025-12** | 2025-12 | **ya** |
| MAVIAUSDT | 2024-02 | 2026-06 | 29 | 28 | 1 | 2025-03 | 2025-03 | **ya** |
| MINAUSDT | 2023-02 | 2026-06 | 41 | 41 | 0 | — | 2023-02 | tidak |
| PUMPUSDT | 2025-04 | 2026-06 | 15 | 14 | 1 | 2025-07 | 2025-07 | **ya** |
| SLPUSDT | 2023-10 | 2026-06 | 33 | 32 | 1 | 2025-07 | 2025-07 | **ya** |
| SXPUSDT | 2020-07 | 2026-05 | 71 | 71 | 0 | — | 2026-06 | tidak |
| TLMUSDT | 2021-07 | 2026-06 | 60 | 60 | 0 | — | 2023-03 | tidak |

**9 dari 9** nama berabsen-satu cocok PERSIS dengan bulan SETTLED terakhirnya.
Jumlah absen 9×1 + 2 (BNX) = **11** ✅

### Mekanisme KEDUA bagi H-A015, dan batasnya

Jurnal 112 menemukan kecocokan bulan SETTLED dengan **bulan berfunding pertama**
(arsip funding). Ini kecocokan bulan SETTLED dengan **kegagalan gerbang klines** —
sumber data berbeda, gerbang berbeda, penyebut berbeda. H-A015 kini disokong dua
gejala yang saling bebas.

Yang TETAP dilarang (KC-18 mengikat): ini membuktikan bahwa bulan peralihan
kontrak menghasilkan bulan 1m yang tidak utuh — soal PENAMAAN dan PENERBITAN. Ia
tidak membuktikan bahwa kontrak lama diperdagangkan sampai bulan itu. **ADR-A002
§10 tidak boleh diubah atas dasar ini.**

Penyeimbang (aturan 74): enam pasangan tidak menunjukkan gejala ini — BDXN, ICP,
MINA, SXP, TLM berabsen **0**, dan kedua bulan absen BNX bukan bulan SETTLED-nya.
Nol pada kelima nama itu berlaku atas penyebut rentangnya sendiri.

## H-A015 — MENANG sebagai angka, DIBATASI sebagai tafsir [v39, dikuatkan v40]

Sumber: `silang_settled.py` V1 (blob `3eea2a80`, UTUH), laporan blob **`755bbaef`**
pada ref runner **`12a65cbb`** (run **30469781160**), UTUH. `sidik_kode`
`0d814bc6…`, `sidik_kode_silang_funding` `8a9b859c…` (sama dengan laporan
`lubang_tengah` V2 → definisi bentuk tetap SATU, aturan 36), `sidik_data_funding`
`2c9fbd1b…`, `versi_funding` 6.

Penggugur SELURUHNYA aman: `sidik_seragam` true · 8/8 · `cacah_kunci_ganda` 0 ·
`kendali_sah` true · `selisih_penyebut` **0** ·
**`selisih_kendali_funding_pertama` 0** · `cacah_pasangan` 15 · kode keluar 0.

**Kesetaraan definisi TERUJI (KC-9):** 5 dari 5 cocok — BNXUSDT 2023-02, ICPUSDT
2022-09, JUPUSDT 2024-02, QTUMUSDT 2020-03, TLMUSDT 2023-03.

`sebaran_arah` = {`sama` **4**, `lebih_awal` **11**, `lebih_lambat` **0**,
`tak_terukur` **0**}; 4 + 11 = **15** ✅

- **Yang didukung:** pada ketiga pasangan berkohort banyak, bulan SETTLED terakhir
  = bulan berfunding pertama nama dasar, sesudah **19/16/20** bulan klines tanpa
  funding — fundingnya **milik kontrak lain**. Kohort 3 dari 3 berlubang > 10;
  keduabelas pasangan bersatu-bulan berlubang < 10.
- **Yang DIBANTAH:** bentuk KUAT H-A015. Pada **11 dari 15** pasangan bulan SETTLED
  jatuh **jauh SESUDAH** funding pertama. Bulan SETTLED punya **DUA peran**.
- **Cela KC-38 (aturan 75):** kecocokan keempat `MINAUSDT` bermekanisme lain —
  `bulan_klines_pertama` = `bulan_berfunding_pertama` = `bulan_settled_terakhir` =
  2023-02 dengan `cacah_lubang` **0**.
- `cacah_lubang` bukan nol di luar kohort banyak hanya **LITUSDT 5** dan **SXPUSDT
  5**; sepuluh sisanya **0**.

## Lubang funding — 880 lawan 877, dan keenam lubang TENGAH

Sumber: docstring `lubang_tengah.py` V2 (blob `4d3beaf1`, UTUH di jurnal 111) dan
laporan blob `39cd1caa` pada ref runner **`e2a37ff7`** (run **30440471508**), UTUH:
`sidik_kode` `c9372bd7…`, `sidik_seragam` true, 8/8, `kendali_sah` true,
`selisih_lubang_tengah` **0**.

- **880** = SELURUH lubang funding; **877** = yang jatuh di dalam **19.586**,
  bentuk lokal {awal **45**, ekor **826**, tengah **6**, seluruh **0**};
  45+826+6+0 = **877** ✅ Selisih **3** = tiga bulan BNXUSDT di luar penyebut.
  **[v40] Kedua penyebut itu kini terkonfirmasi dari kode:** docstring
  `silang_funding.py` menyimpan `BENTUK_TERBITAN_FUNDING` = {awal **48**, ekor 826,
  tengah 6} atas 880; 48+826+6 = **880** ✅ dan 45+826+6 = **877** ✅ — dua
  penyebut, dua bentuk, keduanya benar (aturan 72, 76). **Irisan 880 lawan 877
  tetap UTANG.**
- **Keenam lubang TENGAH dimiliki hanya DUA simbol** (`SIMBOL_TENGAH_TERCATAT =
  ["BTCSTUSDT", "LITUSDT"]`): **LITUSDT 2025-07..2025-11 (5)** dan **BTCSTUSDT
  2022-01 (1)**; 5 + 1 = 6 ✅ Keenamnya MATI. **Inilah asal-usul "dua cabang"
  Keputusan 7 ADR-A008.**
- **Pemilik ke-33 lubang pada simbol-bulan HIDUP:** BNXUSDT, ICPUSDT, **JUPUSDT**,
  **QTUMUSDT**, TLMUSDT; ke-33 lubang HIDUP itu SEMUANYA berbentuk awal.
- Bentuk ekor terjelaskan oleh kematian pasar: lubang → mati **96,0%** (842/877);
  mati → lubang **60,1%** (842/1.401). Lubang funding TIDAK sah sebagai penyaring
  kematian.
- `funding.py` V6 mencacah **87** "funding tanpa klines" atas 787 simbol;
  `funding_tanpa_klines` KOSONG pada kelima simbol H-A010 (**R-229 TEPAT**).

### LITUSDT — urutan peristiwa, kini lengkap [v40]

1. MATI **2025-02..2025-11** (10 bulan); kematian MENDAHULUI hilangnya funding.
2. Lubang funding bentuk TENGAH **2025-07..2025-11** (rentetan **5**); berfunding
   terakhir **2025-06**, kembali **2026-01**.
3. **Bulan 2025-12 ABSEN dari penyebut** — terukur [v40], `pembeda_absen`
   **gagal_gerbang**: arsip menerbitkannya, gerbang 1m menolaknya.
4. `LITUSDTSETTLED` bermuatan **2025-12**, bulan yang sama.
5. **HIDUP 2026-01..2026-06 dengan funding kembali** (`h_a011_menang` true,
   `h_a011_cacah_hidup` **6**). **H-A011 MENANG.**

Jadi bulan SETTLED LITUSDT bukan bulan MATI di sela hidup nama dasarnya — ia bulan
yang nama dasarnya **tidak punya sama sekali** di penyebut. Itu mengubah bentuk
H-A014 (lihat Hipotesis).

### BTCSTUSDT 2022-01 — satu-satunya lubang tengah yang benar-benar tak terjelaskan

`cacah_lilin` **44.640** (31 × 1.440, penuh), `byte_parquet` **399.757**, klines
terbit 2021-03..2026-06 (**64 bulan**, hanya **1** lubang funding), status
**MATI**. **[v40] Dan kini diketahui pula bahwa BTCSTUSDT TIDAK punya bulan
absen** — ia tidak ada di antara sepuluh nama berabsen, jadi bulan itu LOLOS
gerbang dan tetap mati. Ada bulan berlilin PENUH yang lolos gerbang dan tetap
MATI. **Keputusan 7 ADR-A008 DILARANG diambil sebelum bulan itu dianatomi seperti
BNXUSDT 2022-04.**

## Terhenti lawan hidup per jenis — TERUKUR [v38, dilengkapi V4 di v39]

Sumber V4: `terhenti.py` V4 blob **`aaceb023`** commit **`6cc335e3`**, laporan blob
**`b5a1102c`** ref runner **`4dbf06a7`**, `sidik_kode` **`b8d0571d…`**,
`sidik_data` `6128fbb0…`. Sumber V3: laporan blob `e4f71ba8` ref runner `9aad0576`,
`sumber` `reports/semesta_rentang.json` 110.662 B, `sumber_bersidik` **false**
(utang aturan 22).

Dua definisi "terhenti" hidup berdampingan (aturan 36): **survei**
`selisih_bulan >= 2` → **128**; **taksonomi** `bulan_terakhir < 2026-06` → **129**.
`cacah_hanya_taksonomi` **1** = `SXPUSDT` (2026-05); `cacah_hanya_survei` **0**.
Ekor: 2026-03 **1**, 2026-04 **3**, 2026-05 **1**, 2026-06 **808**.

| jenis | terhenti | dari | hidup |
|---|---:|---:|---:|
| `futures_kedaluwarsa` | **44** | 50 | 6 |
| `perpetual_busd` | **41** | 41 | **0** |
| `perpetual_usdt` | **28** | 787 | **759** |
| `sisa_settled` | **14** | 15 | **1** |
| `indeks` | 1 | 3 | 2 |
| `perpetual_usdc` | 1 | 39 | **38** |
| `perpetual_usd1` | 0 | 1 | 1 |
| `basis_non_fiat` | 0 | 1 | 1 |
| `tak_tergolong` | 0 | 0 | 0 |

Terhenti 44+41+28+14+1+1 = **129** ✅ Hidup 759+38+6+2+1+1+1 = **808** ✅
129 + 808 = **937** ✅ `cacah_hidup_luar_penyebut` = 808 − 759 = **49** ✅

**28 nama `perpetual_usdt` yang berhenti terbit (SELURUHNYA, aturan 65):**
1000BTTCUSDT, AKROUSDT, ANCUSDT, ANTUSDT, AUDIOUSDT, **BDXNUSDT**, BTSUSDT,
BTTUSDT, BZRXUSDT, COCOSUSDT, DODOUSDT, DOTECOUSDT, EOSUSDT, FOOTBALLUSDT,
FRONTUSDT, GALUSDT, HNTUSDT, KEEPUSDT, LENDUSDT, LUNAUSDT, **MATICUSDT**,
MBLUSDT, NUUSDT, RNDRUSDT, SRMUSDT, **SXPUSDT**, TOMOUSDT, YFIIUSDT.

Yang TIDAK ada di dalamnya, dan karena itu masih terbit: **ICPUSDT, TLMUSDT,
BNXUSDT, CTKUSDT, CVCUSDT, CVXUSDT, LITUSDT, MAVIAUSDT, SLPUSDT**, ditambah
**AERGOUSDT, AIAUSDT, MINAUSDT, PUMPUSDT**.

**49 nama HIDUP di luar penyebut (SELURUHNYA, aturan 65):** 1000BONKUSDC,
1000PEPEUSDC, 1000SHIBUSDC, AAVEUSDC, ADAUSDC, ARBUSDC, AVAXUSDC, BCHUSDC,
BIOUSDC, BNBUSDC, BOMEUSDC, BTCDOMUSDT, BTCUSD1, BTCUSDC, BTCUSDT_260626,
BTCUSDT_260925, BTCUSDT_261225, CRVUSDC, DEFIUSDT, DOGEUSDC, ENAUSDC, **ETHBTC**,
ETHFIUSDC, ETHUSDC, ETHUSDT_260626, ETHUSDT_260925, ETHUSDT_261225, FILUSDC,
HBARUSDC, IPUSDC, KAITOUSDC, LINKUSDC, LTCUSDC, NEARUSDC, NEOUSDC, ORDIUSDC,
PENGUUSDC, PNUTUSDC, SOLUSDC, SUIUSDC, **SXPUSDTSETTLED**, TIAUSDC, TRUMPUSDC,
UNIUSDC, WIFUSDC, WLDUSDC, WLFIUSDC, XRPUSDC, ZECUSDC.

`MATICUSDC` satu-satunya USDC terhenti, dan `MATICUSDT` ada di antara 28.
Penjelasan penggantian lambang MATIC → POL tetap **ASUMSI**; keberadaan `POLUSDT`
di dalam 787 belum diperiksa.

## Kelima belas pasangan SETTLED — TERUKUR [v39, `terhenti` V4, R-278 TEPAT]

`cacah_settled` **15** · `cacah_dasar_hidup` **13** · `cacah_dasar_terhenti` **2**
· `cacah_dasar_tak_ada` **0** · `cacah_settled_mendahului` **14** ·
`identitas_pasangan_utuh` true · `kendali_pasangan_sah` true.

| SETTLED | bulan SETTLED | bulan | nama dasar | bulan dasar | dasar hidup |
|---|---|---:|---|---|---|
| AERGOUSDTSETTLED | 2025-04 | 1 | AERGOUSDT | 2026-06 | ya |
| AIAUSDTSETTLED | 2026-01 | 1 | AIAUSDT | 2026-06 | ya |
| BDXNUSDTSETTLED | 2026-04 | 1 | BDXNUSDT | **2026-03** | **tidak** |
| BNXUSDTSETTLED | 2023-02 | **6** | BNXUSDT | 2026-06 | ya |
| CTKUSDTSETTLED | 2025-04 | 1 | CTKUSDT | 2026-06 | ya |
| CVCUSDTSETTLED | 2025-05 | 1 | CVCUSDT | 2026-06 | ya |
| CVXUSDTSETTLED | 2025-07 | 1 | CVXUSDT | 2026-06 | ya |
| ICPUSDT_SETTLED | 2022-09 | **9** | ICPUSDT | 2026-06 | ya |
| LITUSDTSETTLED | 2025-12 | 1 | LITUSDT | 2026-06 | ya |
| MAVIAUSDTSETTLED | 2025-03 | 1 | MAVIAUSDT | 2026-06 | ya |
| MINAUSDTSETTLED | 2023-02 | 1 | MINAUSDT | 2026-06 | ya |
| PUMPUSDTSETTLED | 2025-07 | 1 | PUMPUSDT | 2026-06 | ya |
| SLPUSDTSETTLED | 2025-07 | 1 | SLPUSDT | 2026-06 | ya |
| SXPUSDTSETTLED | **2026-06** | 1 | SXPUSDT | **2026-05** | **tidak** |
| TLMUSDTSETTLED | 2023-03 | **9** | TLMUSDT | 2026-06 | ya |

Jumlah kolom bulan = 1+1+1+6+1+1+1+9+1+1+1+1+1+1+9 = **36** ✅ sama persis dengan
total bulan SETTLED yang diukur `bulan_settled.py` V1 (aturan 69).

**Yang wajib dibawa dari `reports/bulan_settled.json` (blob `31d3971e`, ref runner
`0aac1dba`, UTUH):**

1. **"DUA BERSAMBUNG" DICABUT.** `TLMUSDTSETTLED` sembilan bulannya adalah 2022-01,
   2022-02, **2022-04**..2022-08, 2023-02, 2023-03. Yang benar: **satu bersambung
   (`ICPUSDT_SETTLED` 2022-01..2022-09) dan dua bercelah (TLM, BNX)**.
2. `BNXUSDTSETTLED` = 2022-04..2022-08 (lima bersambung) + 2023-02.
3. **`bulan_didaftar` BNXUSDT = 2022-04..2026-06 PENUH, 51 bulan tanpa lubang.**
   Maka "3 lubang 2022-04/-06/-08" adalah lubang **gerbang kehidupan**, bukan
   berkas yang tak diterbitkan. **[v40] Dan aturan 76 lahir tepat dari sini:**
   51 didaftar − 48 lolos = **3**, sedangkan rentang 50 − 48 = **2**. Dua penyebut,
   dua bilangan, keduanya benar.
4. **Ketiga bulan lubang BNXUSDT ada di dalam `BNXUSDTSETTLED`** — calon penjelasan
   KC-15, diturunkan menjadi **ASUMSI LEMAH** oleh jurnal 110.
5. **Penamaan SETTLED datang BEROMBAK:** 2023-02 memuat TIGA nama (BNX, MINA, TLM)
   dan 2025-07 memuat TIGA (CVX, SLP, PUMP).
6. **DUA BELAS nama bersatu-bulan** (bukan 11 — kekalahan R-281): AERGO, AIA,
   BDXN, CTK, CVC, CVX, LIT, MAVIA, MINA, PUMP, SLP, SXP. Tiga lebih panjang: ICP
   9, TLM 9, BNX 6. 12 + 3 = 15 ✅ 12×1 + 24 = **36** ✅
7. `definisi_dapat_dibedakan` **false** pada H-A013. Kendali BTCUSDT 78 bulan ≥ 60.
8. **`BDXNUSDT` adalah penghuni ekor 2026-03**, satu-satunya. 2026-05 = SXPUSDT;
   tiga nama 2026-04 belum bernama, satu di antaranya `BDXNUSDTSETTLED`.

## H-A013 — MENANG 6–0, TAFSIRNYA DICABUT [v38]

Enam bulan peralihan cocok dengan bulan saudara SETTLED-nya (CTK 2025-04, CVC
2025-05, CVX 2025-07, LIT 2025-12, MAVIA 2025-03, SLP 2025-07), `cacah_cocok_bulan`
6, `ambang_menang` 4, `cacah_peralihan_terhenti` **0**, keenam nama dasar masih
terbit 2026-06. Rantai pelemahan tafsir: "delapan kebangkitan" → "dua bersambung +
enam peralihan nama" → **PENAMBAHAN nama kontrak selesai** (aturan 68, KC-31).
**[v40] Keenam bulan itu kini juga terbukti bulan ABSEN** — kelas gejalanya sama.

DUA konvensi nama hidup berdampingan: `ICPUSDT_SETTLED` bergaris bawah, empat
belas lainnya TANPA. Docstring `penyebut_tahun.py` menulis `TLMUSDT_SETTLED`
(salah): dicatat, TIDAK disunting, tidak diwarisi (R-246 SEPARUH).

Cacah bulan ARSIP 24 nama, 24 dari 24 cocok, `jumlah_bulan_didaftar` **518**:
BNXUSDT 51 (48 di PENYEBUT) · CTKUSDT 68 · CVCUSDT 68 · CVXUSDT 46 · ICPUSDT 62 ·
LITUSDT 65 · MAVIAUSDT 29 · SLPUSDT 33 · TLMUSDT 60 · ICPUSDT_SETTLED 9 ·
TLMUSDTSETTLED 9 · BNXUSDTSETTLED 6 · dua belas nama SETTLED lain bercacah 1.

## Penyebut simbol-bulan PER TAHUN — TERUKUR [v36]

Semesta `perpetual_usdt` saja (aturan 63). Sumber `penyebut_tahun` V1.

| tahun | penyebut | MATI | `bagian_mati` |
|---|---:|---:|---:|
| 2020 | 504 | 1 | 0,001984 |
| 2021 | 1.385 | 9 | 0,006498 |
| 2022 | 1.729 | 34 | 0,019665 |
| 2023 | 2.400 | 103 | 0,042917 |
| 2024 | 3.570 | 192 | 0,053782 |
| 2025 | 5.948 | 506 | 0,085071 |
| 2026 (6 bln) | 4.050 | 556 | **0,137284** |

1+9+34+103+192+506+556 = **1.401** ✅ ·
504+1.385+1.729+2.400+3.570+5.948+4.050 = **19.586** ✅ `bagian_mati` menanjak
monoton 0,20% → **13,73%**. DILARANG disebut laju kematian "pasar kripto".
`cacah_simbol_tanpa_hidup` **18** — identitasnya belum dibaca.

## Cacah baris terukur [v36] — `ukur_baris` V5

Sumber blob `c8b988ff` (UTUH), commit `404e6f1b`, run 30451749412, kode 0;
`cacah_berkas_hilang` 0, `cacah_berkas_melebihi_pagar` 0, 21 dari 21 berkas.
Definisi `len(teks.splitlines())`, pagar 800 di `tests/test_kontinuitas.py`.

`funding.py` **705**/28.121 B · `silang_funding.py` **705**/29.873 B ·
`lubang_tengah.py` V2 560 · `kohort_ekor.py` 553 · `kebangkitan.py` 552 ·
`penyebut_tahun.py` 527 · `tests/test_kebangkitan.py` 501 · `kehidupan_arsip.py`
496 · `semesta_silang.py` 423 · `kehidupan.py` 417 · `bulan_settled.py` 386 ·
`pulihkan.py` 383 · `tests/test_penyebut_tahun.py` 369 · `ukur_baris.py` 352 ·
`tests/test_semesta_silang.py` 253 · `tests/test_bulan_settled.py` 240 ·
`gerbang_1m.py` 184 · `funding_cdn.py` 162 · `arsip.py` 154 · `resample.py` 127 ·
`kohort_ringkas.py` 82. Total **8.131** ✅ Terbesar **705, SERI** (KC-26).

**Angka MATI:** `ukur_baris.py` 183/226/280 BATAL → 352; `silang_funding.py` 396
BATAL → 705; `pulihkan.py` 318 BATAL → 383; `lubang_tengah.py` 390 hanya V1 → 560.

**BELUM DIUKUR [v40]:** `tests/test_lubang_tengah.py`, `taksonomi.py`,
`pecahan.py`, `semesta_kuota.py` V3 (24.987 B), `tests/test_semesta_kuota.py`,
`terhenti.py` **V4**, `tests/test_terhenti.py` **V4**, `survei.py`,
`ringkas_semesta.py`, `diagnosa_kc15.py` (16.268 B), `silang_settled.py`,
`tests/test_silang_settled.py`, **`bulan_absen.py`**, **`tests/test_bulan_absen.py`**
— empat belas berkas. Tidak diramalkan dengan pita sempit (aturan 58 pilihan c).

## Modul dan workflow yang tercatat

**`lux_ai/semesta/`:** `__init__.py` 273 B (`4c2d1f25`) · `taksonomi.py` 7.086 B
(`b418c7ba`) · `terhenti.py` V1 `3fa8f697`, V2 `8121739b`, V3 `7b819787`,
**V4 `aaceb023` pada commit `6cc335e3`**.

**`lux_ai/serapan/` — 38 berkas [v40, dari listing ref `a9ee214d` + push
`4fc818f0`]:** `__init__.py` (`64d85584`) · `arsip.py` (`0104958b`) ·
`bentuk_semesta.py` (`1f0feb30`) · **`bulan_absen.py` (`10279d72`)** ·
`bulan_settled.py` (`80e8d8bb`) · `diagnosa_kc14.py` (`5bd67d15`) · `kc14b`
(`bceada11`) · `kc14c` (`ab517db9`) · `diagnosa_kc15.py` (`3642e5b6`) ·
`diagnosa_kc6.py` (`0f699854`) · `funding.py` (`8d4b1f82`) · `funding_cdn.py`
(`fd624d00`) · `gerbang_1m.py` (`c8cc54c8`) · `kebangkitan.py` (`446321ee`) ·
`kehidupan.py` (`f49abb2b`) · `kehidupan_arsip.py` (`318a5cb1`) · `klines.py`
(`cc4d9287`) · `kohort_ekor.py` (`c9b63bbe`) · `kohort_ringkas.py` (`4ae62d5b`) ·
`lubang_tengah.py` (`4d3beaf1`) · `pecahan.py` (`f1b49f1b`) · `penyebut_kc6.py`
(`7f399244`) · `penyebut_tahun.py` (`265aad00`) · `probe.py` (`4581639f`) ·
`pulihkan.py` (`a9e6eab7`) · `rentang_kc6.py` (`631ec2f3`) · `resample.py`
(`66a4b177`) · `rilis.py` (`2e44530c`) · `ringkas_semesta.py` (`bc8f7ad7`) ·
`semesta_kuota.py` (`7288b030`) · `semesta_silang.py` (`ad72f3f2`) · `serap.py`
(`62d4c2c3`) · **`silang_funding.py` (`42c3aa9d`)** · `silang_settled.py`
(`3eea2a80`) · `survei.py` (`26b14940`) · `uji_resample.py` (`f10ec98a`) ·
`ukur_baris.py` (`3ebaa9f9`).

**32 berkas di `.github/workflows/` [v40, listing dijalankan]** (blob):
bentuk_semesta `dc393dd0` · bulan_settled `9e0829f2` · **`bulan_absen` (blob belum
dicatat — didorong pada `4fc818f0`, belum dibaca ulang)** · **ci `c79497b2`** ·
diagnosa_kc14 `6524646a` · kc14b `a315c25b` · kc14c `82126b60` · kc15 `c5f2ee0f` ·
kc6 `6bae2b1b` · funding_semesta `c1ce55f3` · kebangkitan `282b51aa` · kehidupan
`3eb10655` · kehidupan_arsip `8234e5dc` · kohort_ekor `2e747475` · lubang_tengah
`557030de` · pecahan_serapan `cd9e21d1` · penyebut_kc6 `14617b6b` · penyebut_tahun
`8f0d5852` · probe_serapan `9b356e15` · pulihkan_rilis `32bd1099` · rentang_kc6
`db1e77ae` · ringkas_semesta `d6145d28` · semesta_kuota `b7e5a65a` · semesta_silang
`babf08e4` · serap_pilot `85694e0f` · silang_funding `23f8c870` ·
**silang_settled `78d8051c`** · survei_semesta `a1fb0192` · taksonomi_semesta
`b066b4db` · terhenti_semesta `baef4f41` · uji_resample `121f3e25` · ukur_baris
`f62be605`. Cacah 30 yang tercatat sejak jurnal 107 **SALAH sejak `silang_settled`
lahir**; angka benar 31 sebelum push ini, **32** sesudahnya.

## API modul yang sudah terbaca dan boleh dipakai

Rincian v37 berlaku untuk `semesta_silang`, `arsip` (tanpa `requests`;
`fapi.binance.com` 451), `pecahan` (VERSI 6), `taksonomi`, `semesta_kuota` V3,
`penyebut_tahun`, `kebangkitan`; v38 untuk `survei`, `terhenti` V3,
`ringkas_semesta`, `rentang_kc6`; v39 untuk `silang_settled` V1, `diagnosa_kc15`,
`terhenti` V4. Tambahan dan pembetulan [v40]:

- **`silang_funding` V2** (blob `42c3aa9d`, dibaca UTUH — blob ini yang benar;
  `3eea2a80` adalah `silang_settled.py`). `VERSI` 2, `TOTAL_PECAHAN` dari
  `kehidupan_arsip` = **8**, `SUMBER_FUNDING` `reports/funding_semesta.json`,
  keluaran `silang_funding.json` / `_ringkas.json` / `hidup_tanpa_funding.json`,
  `PENYEBUT_TERCATAT` 19586, `MATI_TERCATAT` 1401, `KOHORT_TERCATAT` 456,
  `HIDUP_TANPA_FUNDING_TERCATAT` 33, `LUBANG_TAK_DIKENAL_TERCATAT` 3,
  `BENTUK_TERBITAN_FUNDING` {awal 48, ekor 826, tengah 6}. Fungsi:
  `baca_laporan_kehidupan` → (status, byte_parquet, meta) dengan meta
  {`total_pecahan`, `cacah_laporan_dibaca`, `laporan_hilang`, `sidik_kode_laporan`,
  `sidik_seragam`, `cacah_kunci_ganda`}; `baca_medan_baris`; `lubang_funding`;
  `kohort_simbol_bulan`; `silang`; **`bulan_per_simbol`**; `bentuk_lubang_lokal`;
  `_berlubang_per_simbol`; `daftar_hidup_tanpa_funding`;
  `daftar_lubang_tak_dikenal`; `sebaran_bentuk`; `sebaran_bentuk_semua`;
  `rincian_mati`; `kendali_silang`; `kendali_sah`; `kode_keluar`; `jalankan`.
- **`kehidupan_arsip` V1** (blob `318a5cb1`, dibaca UTUH). `TOTAL_PECAHAN` **8**,
  `nama_keluaran(i)` = `reports/kehidupan_arsip_<i>.json`, `nama_ringkas(i)`,
  `peta_parquet(manifes)` membaca `manifes[]` dengan medan `parquet`, `simbol`,
  `bulan`, `byte_parquet`, `gerbang_lolos`, `baris` — baris karantina menaruh
  jalurnya di `parquet_karantina` dan sengaja TIDAK masuk peta; `ukur_kolom`,
  `ukur_parquet` (pyarrow, dua kolom `volume`/`trades`), `baris_kehidupan`
  (medan baris: simbol, bulan, jalur, gerbang_lolos, byte_parquet, ada_di_arsip,
  cacah_lilin, cacah_lilin_terbaca, cacah_baris_cacat, transaksi_total,
  cacah_volume_nol, bagian_volume_nol, galat, status), `kendali_pecahan`,
  `ringkas_pecahan`, `kode_keluar`, `jalankan(indeks)`.
- **`bulan_absen` V1** (blob `10279d72`, dibaca UTUH). `VERSI` 1, keluaran
  `reports/bulan_absen.json` + `_ringkas.json`, `PENYEBUT_TERCATAT` 19586,
  `ABSEN_PASANGAN_JURNAL_113` 12 (**keterangan saja, BUKAN penggugur**),
  `NAMA_PENYEBUT_TERCATAT` 787, `PEMBEDA` = (`gagal_gerbang`,
  `tak_diterbitkan_arsip`, `tak_terukur`), `KENDALI_NAMA` = (BTCUSDT, ETHUSDT),
  `KENDALI_BULAN_MIN` 60, tetapan `R288_*`. Fungsi: `bulan_ke_indeks`,
  `indeks_ke_bulan`, `rentang_bulan`, `bulan_sah`, `bulan_absen`, `pembeda_absen`,
  `baris_simbol`, `jumlah_absen`, `sebaran_pembeda`, `peta_didaftar` (memakai
  `pulihkan.nama_manifes(i)`), `baris_pasangan_settled` (memakai
  `silang_settled.PASANGAN_SETTLED`), `uji_r288`, `kendali_absen`, `kendali_sah`,
  `kode_keluar`, `jalankan`, `berkas_ringkas`, `main`. **Ia MENGIMPOR
  `kehidupan_arsip`, `pulihkan`, `silang_funding`, `silang_settled`.**
  **Perancangan yang wajib diwarisi:** `kode_keluar` sengaja TIDAK memeriksa satu
  pun medan `uji_r288` — ramalan yang kalah tidak boleh membatalkan laporannya
  sendiri (aturan 24, 72).

## Hipotesis

- H-A001 belum diuji · H-A002b GUGUR · H-A003 MENANG pada 3, GUGUR pada 9 ·
  H-A004 tak dapat diuji (451) · H-A005 GUGUR pada rentang tersampel · H-A006
  MENANG enam run · H-A008 MENANG dua kali · H-A009 GUGUR · H-A010 **MENANG 5–0**
  · **H-A011 MENANG** — LITUSDT HIDUP 6 dari 6 bulan 2026; batasan BTCSTUSDT 0
  dari 53 tetap berlaku (aturan 60) · H-A012 MENANG · **H-A013 MENANG 6–0, TAFSIR
  DICABUT**.
- **H-A014 [v40] — BENTUK LAMA SALAH, BENTUK BARU MENANG 9 dari 9.** Bentuk lama:
  "bulan SETTLED adalah bulan tanpa perdagangan (MATI) di TENGAH hidup nama
  dasarnya" — **DICABUT sebagai bentuk utama**: bulan itu bahkan tidak ada di
  penyebut, jadi ia tidak dapat berstatus MATI maupun HIDUP. **Bentuk baru yang
  TERUKUR:** bulan SETTLED terakhir adalah bulan yang **ABSEN** dari daftar bulan
  LOLOS nama dasarnya. Terbukti pada **9 dari 9** nama berabsen-satu (AERGO, AIA,
  CTK, CVC, CVX, LIT, MAVIA, PUMP, SLP), dengan `pembeda_absen` **gagal_gerbang**
  pada kesebelas bulan absen. **Batas (aturan 74):** enam pasangan lain tidak
  menunjukkannya — BDXN, ICP, MINA, SXP, TLM berabsen 0 dan BNX berabsen 2 pada
  bulan yang bukan bulan SETTLED-nya. Jadi bentuk barunya berlaku atas SEBAGIAN,
  dan penyebutnya wajib disebut 9 dari 15. Kendali positif terpenuhi (50);
  `definisi_dapat_dibedakan` masih harus dipasang bila hipotesis ini diuji lagi
  dengan modul lain (46).
- **H-A015 MENANG sebagai angka, DIBATASI sebagai tafsir; [v40] disokong mekanisme
  KEDUA.** Bunyi asal: bulan `…SETTLED` menandai batas antara dua kontrak pada
  nama dasar yang sama. Terukur benar pada **3 pasangan berkohort banyak** lewat
  funding, dan sekarang **9 dari 9 pasangan berabsen-satu** lewat gerbang klines —
  dua gejala bebas. Tetap **dibantah** dalam bentuk KUAT pada 11 pasangan
  bersatu-bulan. Warisi hanya dalam bentuk terbatas (aturan 20); ingat KC-38
  (`MINAUSDT`) dan KC-18 (penamaan, bukan perdagangan).

## Papan skor prediksi

R-1..R-120 dirinci v23 · R-121..R-149 v26 dan jurnal 56–63 · R-150..R-193 jurnal
64–75 · R-194..R-199 jurnal 76–78 · R-200..R-235 seperti v37 · **R-236..R-247 di
jurnal 92–94** (rincian barisnya ADA DI SANA, belum disalin) · R-248..R-252 jurnal
95 · R-253..R-255 jurnal 96 · R-256 jurnal 97 · R-257..R-260 jurnal 98 ·
R-261..R-264 jurnal 99 · R-265..R-267 jurnal 101 · R-268 jurnal 102 ·
R-269..R-271 jurnal 103 · R-272..R-274 jurnal 104 · R-275..R-277 jurnal 105 ·
R-279 jurnal 106 · R-278 dan R-280 jurnal 107 · R-281 jurnal 108 · R-282 jurnal
109 · R-283 jurnal 110 · R-284 jurnal 111 · R-285 jurnal 112 · R-286 dan R-287
jurnal 113 · **R-289 jurnal 114** · **R-288 dan R-290 jurnal 115**.

| # | Prediksi | Status |
|---|---|---|
| R-199 | `definisi_dapat_dibedakan` false pada TEPAT 2 pecahan | **MENUNGGU** |
| R-275 | SETTLED hidup: bulan tutup DAN cacah_bulan ≤3 | **TEPAT** |
| R-276 | keenam nama peralihan ada di 28 terhenti | **MELESET** (0 dari 6) |
| R-277 | CI 630, kode 0, commit `e6b74855` | **TEPAT** |
| R-278 | 15 SETTLED: 13 dasar hidup, 2 terhenti, ≥11 mendahului | **TEPAT** (13/2/0, 14) |
| R-279 | CI 630, commit `8a0c4bff` | **TEPAT** (MUDAH) |
| R-280 | CI 638 sesudah `test_terhenti` V4 | **TEPAT** (MUDAH) |
| R-281 | bulan SETTLED 36 **dan** 11 nama bersatu-bulan | **MELESET** (12 — aritmetika sendiri) |
| R-282 | `diagnosa_kc15.json` menyebut tiga bulan BNXUSDT | **MELESET** (hanya 2022-04) |
| R-283 | modul `diagnosa_kc15` mengukur tepi | **TEPAT** (lewat disjungsi — mendekati MUDAH) |
| R-284 | `lubang_tengah.py` memuat tetapan tiga bulan BNXUSDT | **MELESET** (aturan 73) |
| R-285 | 6 lubang tengah, LIT 5 / BTCST 1, `h_a011_menang` false | **SEPARUH** (pembagian TEPAT; H-A011 MENANG) |
| R-286 | H-A015: cocok 3..4; ≥10 dari 12 lebih awal; lubang >10 lawan <10 | **TEPAT** (4, 11 dari 12, 3/3 lawan 12/12) |
| R-287 | CI **662**, kode 0, commit `3d113d49` | **TEPAT** (MUDAH, run 30469781181) |
| R-289 | `ci.yml` menyala pada commit STATE **dan** commit PROMPT, 662 butir, kode 0 | **TEPAT** pada KEDUA cabang (MUDAH; run 30475448183 dan 30475625553) |
| R-288 | bulan ABSEN: (1) 9 tunggal + BNX **3** + lima nol; (2) ≥7 dari 9 sama dengan bulan SETTLED; (3) jumlah semesta **12** | **SEPARUH** — butir 2 **TEPAT 9 dari 9**; butir 1 MELESET (BNX **2**); butir 3 MELESET (**11**) |
| R-290 | CI **694**, kode 0, commit `4fc818f0` | **TEPAT** (MUDAH, run 30477143164) |

**Total R-1..R-290** (dihitung tangan, aturan 21). Dasar v39 yang tercatat: TEPAT
202 · MELESET 54 · SEPARUH 17 · TIDAK TERADJUDIKASI 7 · MENUNGGU 7 = **287**.
Sesudah v39: **tiga TEPAT** (R-289, R-290, dan — sudah masuk sejak jurnal 114 —
R-289 dihitung sekali saja) dan **satu SEPARUH** (R-288). Rinciannya:

- TEPAT 202 + R-289 + R-290 = **204**
- MELESET **54** (tak berubah)
- SEPARUH 17 + R-288 = **18**
- TIDAK TERADJUDIKASI **7**
- MENUNGGU **7** (R-7, R-19, R-20, **R-28**, R-36, R-37, R-199)

204+54 = 258; +18 = 276; +7 = 283; +7 = **290** ✅ Nomor terpakai R-1..R-290,
seluruhnya teradjudikasi atau menunggu. N_percobaan = 0; adjudikasi riset TETAP
TERKUNCI. Ramalan berikutnya **R-292**.

**Terpraregistrasi, belum teradjudikasi [v40]:**

- **R-291** (jurnal 115 §7) — daftar `parquet_karantina` di kedelapan manifes
  memuat **tepat 12** simbol-bulan, dan himpunannya SAMA PERSIS dengan dua belas
  baris tabel karantina di atas (AERGO 2025-04, AIA 2026-01, BNX 2022-04, BNX
  2022-06, BNX 2022-08, CTK 2025-04, CVC 2025-05, CVX 2025-07, LIT 2025-12, MAVIA
  2025-03, PUMP 2025-07, SLP 2025-07). **GUGUR bila ada satu nama-bulan lain, atau
  bila cacahnya bukan 12.** Dasar: (a) 19.598 − 19.586 = 12; (b) 11 bulan absen
  terukur dengan `gagal_gerbang` 11 dan `tak_diterbitkan_arsip` 0; (c) BNXUSDT
  2022-04 sudah teranatomi `gerbang_lolos` false. Yang BERISIKO: apakah tepat itu
  yang masuk `parquet_karantina`. Satuan SIMBOL-BULAN, penyebut **19.598**
  (aturan 44). Daftar itu belum pernah dibaca (aturan 73 ditaati tersurat).
- **R-292 sengaja dikosongkan** sampai daftar bernomor `def test_` berkas uji
  berikutnya selesai ditulis (aturan 54/56/57; preseden jurnal 106 §5, 114 §4).

**Utang papan skor:** rincian baris R-236..R-247 masih hanya di jurnal 92–94; dan
ramalan yang dipraregistrasi di dalam **docstring modul** (mis. R-229 TEPAT, R-230
MELESET di `lubang_tengah.py` V2) belum masuk papan — pemeriksaan R-224..R-235
wajib dijalankan lebih dulu agar tidak mengulang KC-32.

**Catatan kejujuran [v40].** Sejak v39 ada tiga adjudikasi: R-289 TEPAT (MUDAH),
R-290 TEPAT (MUDAH), R-288 SEPARUH. Kedua kemenangan itu deterministik — cacah
butir uji dari daftar bernomor — dan tidak menambah satu pun bukti bahwa mutu
ramalan membaik. Yang benar-benar berisiko adalah R-288, dan di sana pola lama
berulang: **butir yang saya sebut MUDAH justru kalah** karena satu angka disalin
dari penyebut yang salah (BNX 3 lawan 2), sedangkan **butir yang saya sebut
BERISIKO menang 9 dari 9**. Kelas cacat ini sekarang empat kali: R-281 (aritmetika
sendiri), R-282 (nama laporan), R-284 (nama modul), R-288 (penyebut tertukar) —
seluruhnya dapat dicegah tanpa jaringan dan tanpa satu pun run. Yang layak
dicatat sebagai kemajuan bukan papan skornya, melainkan bahwa setiap kekalahan
melahirkan aturan yang menutup lubangnya: 70, 71, 72, 73, dan sekarang **76**.

## Jumlah uji

**694 TERVERIFIKASI [v40]** — `reports/ci_terakhir.json` blob
**`2d8530215e5d548483589d431f69446cd14a0c4c`**, run **30477143164**, commit
**`4fc818f09f9a684570f99ffdb6cd20162816fc54`**, `kode_keluar` **0**, "694 tests
collected in 0.48s", ref runner `9698c36b`. Sebelumnya **662** tiga kali (blob
`8504322b` run 30469781181 commit `3d113d49`; blob `15d14123` run 30475448183
commit `9e4226ca`; blob `18cae8e5` run 30475625553 commit `57bac8ae`), **638**
(blob `ca47d961`), **630** (blob `2d0dfa27`). Riwayat: 231 → … → 610 → 623 → 630
→ 630 → 638 → 662 → 662 → 662 → **694**.

`tests/test_terhenti.py`: V1 **5** → V2 **18** → V3 **25** → **V4 33**.
`tests/test_silang_settled.py` **24** (638 + 24 = 662).
**`tests/test_bulan_absen.py` 32** butir tanpa satu pun `parametrize`
(662 + 32 = **694**), daftar bernomor ada di docstringnya. Lainnya:
`test_semesta_kuota` 58 · `test_lubang_tengah` 56 · `test_kebangkitan` 54 ·
`test_silang_funding` 49 · `test_penyebut_tahun` 44 · `test_semesta_silang` 32 ·
`test_bulan_settled` 26.

**Kendali negatif yang tercatat:** run 30462286751 atas commit `7b819787` berjalan
ketika `tests/test_terhenti.py` masih memuat kurung kurawal liar; run 30462427226
atas commit perbaikan `e6b74855` memberi 630 dan kode 0.

## Utang verifikasi

1-5 dan 11 menunggu tahap juri/klasifikasi. 6-23, 25-28 LUNAS. **Nomor utang ini
BUKAN nomor ramalan — lihat KC-32.**

24. **AKTIF.** LUNAS seperti tercatat v39, ditambah **LUNAS BARU [v40]:**
    `lux_ai/serapan/silang_funding.py` dibaca UTUH (blob benar `42c3aa9d`) ·
    `kehidupan_arsip.py` dibaca UTUH · `bulan_absen.py` dan ujinya dibaca UTUH ·
    `reports/bulan_absen_ringkas.json` dibaca UTUH · **listing ulang direktori
    paket (38) dan workflow (32)** · **identitas kedua belas simbol-bulan
    karantina (11 absen + 1 tepi)** · **pembedaan sebab bulan absen: gagal gerbang
    11 lawan tak diterbitkan 0** · **bulan MANA yang absen pada kesembilan nama
    berpasangan** · **kecocokan bulan absen dengan bulan SETTLED 9 dari 9** ·
    **konfirmasi ketiga penyebut 787** · **bentuk 48/45 dua penyebut lubang
    funding**.
    **BELUM:** anatomi **BTCSTUSDT 2022-01** · irisan 880 lawan 877 · pembagian 5
    hari KC-15 ke tiga bulan BNXUSDT · tanggal 1.440 menit hilang di BNXUSDT
    2022-04 · selisih 40 − 38 sampel `diagnosa_kc15` · `ukur_baris` V6 (KC-26 +
    empat belas berkas) · peninjauan `funding.py`/`silang_funding.py` (705) ·
    daftar 147 nama hanya-arsip · identitas 18 simbol tanpa bulan HIDUP ·
    **daftar `parquet_karantina` (R-291)** · kehidupan 12 simbol-bulan karantina ·
    `funding_ada` masih null di seluruh manifes · `dugaan_pengganti` (ADR-A005) ·
    pemulihan harian ADR-A007 · karantina artefak 7 hari · 28 anggota kohort di
    luar sampel abjad · **bunyi ramalan R-28 dari STATE v23 (KC-32)** · tiga nama
    ekor 2026-04 · keberadaan `POLUSDT` di 787 · asal-usul hantu "16 non-ASCII" ·
    `.github/workflows/bulan_absen.yml` belum dibaca ulang sesudah push · laporan
    yang belum pernah dibaca: **`bulan_absen.json` penuh (249.992 B)**,
    `semesta_rentang.json` (110.662 B, **tak bersidik**), `ringkas_semesta.json`,
    `survei_semesta.json`, `survei_progres.json`, `rentang_kc6.json`,
    `semesta_kuota.json` penuh, `semesta_silang.json` penuh, `penyebut_tahun.json`
    penuh, `kohort_ekor.json`, `funding_semesta.json` penuh,
    `funding_selisih_penuh.json` (`daftar_terpotong` true, 500 dari 880),
    `hidup_tanpa_funding.json`, `tests/test_pulihkan.py`.
    Cacat penulisan yang dicatat dan TIDAK disunting: docstring R-225 ("tujuh
    fungsi" lalu sembilan nama) dan docstring `penyebut_tahun.py`
    (`TLMUSDT_SETTLED`). Mengadjudikasi R-7, R-19, R-20, R-28, R-36, R-37.

## Daftar ADR

- ADR-A001 aturan dasar. DITERIMA.
- ADR-A002 serapan. DITERIMA; §3 DIAMANDEMEN oleh A004 lalu A007; §9 DIGANTI oleh
  A006 Keputusan 3. **§10 belum disentuh dan tetap tidak boleh disentuh atas bukti
  kohort semata;** bila kelak disunting, WAJIB menyebut batas `perpetual_usdt`.
  **[v40] Dua gejala bebas yang menyokong H-A015 TIDAK cukup untuk menyentuhnya —
  keduanya soal penamaan dan penerbitan, bukan perdagangan (KC-18).**
- ADR-A003 taksonomi rezim. BELUM ADA (nomor dicadangkan). Wajib memisahkan
  "kontrak berganti nama" dari "pasar hidup kembali", wajib memakai taksonomi
  INSTRUMEN kanonik (KC-29), wajib memuat aturan 68, wajib memuat kebangkitan
  LITUSDT beserta aturan 74, dan **[v40] wajib memuat bulan ABSEN sebagai kelas
  gejala tersendiri beserta aturan 76** — sebab bulan peralihan kontrak ternyata
  bukan bulan MATI melainkan bulan yang TIDAK ADA di penyebut.
- ADR-A004 kebijakan KC-6. DITERIMA. ADR-A005 jenis instrumen tahap pertama.
  DITERIMA. ADR-A006 karantina + persistensi. DITERIMA, DITERAPKAN, TERVERIFIKASI
  DARI LUAR. Penggugur ADR-A004 tetap tidak menyala:
  `cacah_gerbang_lolos_padahal_tepi_terpotong` = 0 atas 37 bulan tengah.
- **ADR-A007 serapan hibrida. DIUSULKAN**, belum diterima; wajib memperhitungkan
  temuan `jumlah_baris` dan kendala R-146. Bahan yang menguatkannya: 7.200 menit
  KC-15 UTUH di arsip HARIAN. **[v40] Bahan baru:** kesebelas bulan absen ADA di
  arsip (`tak_diterbitkan_arsip` 0) — jadi pemulihan dari arsip HARIAN berpeluang
  mengembalikan bulan-bulan itu ke penyebut, dan itu akan MENGUBAH 19.586.
  Perubahan penyebut DILARANG dilakukan tanpa ADR (aturan 30, 44).
- **ADR-A008 akibat KC-18. Keputusan 1–6 DITERIMA [v28]**; Keputusan 5 bersemesta
  18.087. **Keputusan 7 BERCABANG DUA, kedua cabangnya bernama:** **LITUSDT**
  (lubang tengah berentetan **5**, MATI seluruhnya, bulan **2025-12 ABSEN**, lalu
  **BANGKIT** terukur) lawan **BTCSTUSDT** (lubang tengah **TUNGGAL** 2022-01,
  `cacah_lilin` 44.640 PENUH, **tanpa bulan absen**, tetap MATI, 53 dari 53).
  Keputusannya WAJIB memuat kedua cabang, WAJIB per simbol-bulan, DILARANG
  menyebut funding dan perdagangan berhenti "serentak", WAJIB menyebut batas
  `perpetual_usdt`, WAJIB memakai aturan 66 revisi, 67, 68, 74, dan **76**, dan
  **DILARANG diambil sebelum BTCSTUSDT 2022-01 dianatomi seperti BNXUSDT 2022-04**.
  R-276 mengikat: tak ada peralihan yang terbukti. R-278 mengikat: 13 / 2 / 0.
- ADR berikutnya **A009**.

## Temuan sampingan yang belum diukur

- **Anatomi BTCSTUSDT 2022-01** — pekerjaan teknis paling berharga yang tersisa.
- **Daftar `parquet_karantina`** (R-291) — alat ukurnya belum ada; modul kecil yang
  membaca kedelapan manifes sudah cukup, tanpa jaringan.
- Mengapa gerbang 1m menolak tepat bulan peralihan kontrak: apakah bulan itu
  berlilin sebagian karena kontrak lama berhenti di tengah bulan. Ini pertanyaan
  BERIKUTNYA yang paling murah bernilai tinggi sesudah R-291.
- Tanggal hari yang hilang di BNXUSDT 2022-04 (1.440 menit) dan pembagian 5 hari
  KC-15 ke tiga bulan.
- Irisan 880 lawan 877; selisih 40 − 38 sampel `diagnosa_kc15`.
- Tiga nama ekor 2026-04; mengapa `SXPUSDT` berhenti 2026-05; apakah `POLUSDT` ada
  di 787; asal-usul hantu "16 non-ASCII".
- Daftar 147 nama hanya-arsip; 18 simbol tanpa bulan HIDUP; kehidupan 12
  simbol-bulan karantina (kini bernama, tetapi lilinnya belum diukur).
- Apakah 50 kontrak delivery bertanggal pernah masuk perhitungan mana pun.
- Mengapa penamaan SETTLED datang berombak pada 2023-02 dan 2025-07, dan mengapa
  2025-07 juga bulan tebing funding dan kohort puncak.
- Sebab kebangkitan/peralihan kedelapan simbol (di luar jangkauan arsip).
- Saham, ETF, dan komoditas token masih terhitung `perpetual_usdt`.
- `.decode("utf-8","replace")` di `klines` membungkam byte rusak.
- Apakah BUSD/USDC layak digabung dengan USDT (80 nama, 1.705 bulan).
- Sebab KC-14 (H-A004) tak dapat diuji; sebab KC-15 tidak diketahui.
- Selisih byte funding AGIXUSDT 531 lawan 529; `waktu_utc` runner berjalan lebih
  dulu daripada jam sesi; satuan stempel mikro lawan mili.
- `tests/test_pulihkan.py` belum pernah dibaca ulang sesudah push.
