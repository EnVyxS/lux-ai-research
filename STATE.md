# STATE — versi 39

Diperbarui: 2026-07-30 (sesi 56, pembukaan). Aturan hanya BERTAMBAH; jangan menulis
ulang dari ingatan. v39 disusun di atas teks v38 yang dibaca langsung dari `main`
(blob **`9f8e8606c2ed9514c1642fa3717b6fb2c1ac84ab`**, dibaca **UTUH** sebelum satu
huruf pun ditulis), ditambah jurnal **106, 107, 108, 109, 110, 111, 112, 113**
(seluruhnya dibaca UTUH dari `main`: blob `43d83f79`, `bc880574`, `a30fa4d7`,
`62f15f8c`, `0784c727`, `7521d1af`, `a31e7a66`, `342edcb7`),
`lux_ai/serapan/silang_settled.py` (blob `3eea2a80`, UTUH),
`reports/silang_settled.json` (blob `755bbaef`, UTUH, ref runner `12a65cbb`), dan
`reports/ci_terakhir.json` blob `ca47d961` (638) dan **`8504322b` (662)**.

v38 tertinggal **tiga jurnal**; utang itu lunas di sini. Yang lahir sejak v38:
aturan **69, 70, 71, 72, 73, 74, 75**; KC-**33, 34, 35, 36, 37, 38**; adjudikasi
**R-278..R-287**; hipotesis **H-A015**; dan kebangkitan terukur pertama di repo ini.

Berkas yang TIDAK dibaca ulang pada sesi 56 dan karena itu tidak diubah
angkanya di sini: `lux_ai/serapan/lubang_tengah.py` (blob `4d3beaf1`, dibaca UTUH
di jurnal 111), `decisions/ADR-A002.md`, `ADR-A004.md`, `ADR-A006.md`,
`ADR-A007.md`, `PETA_MODUL.md`.

Lima peristiwa terbesar sejak v38:

1. **Kebangkitan terukur PERTAMA di repo ini.** LITUSDT MATI 2025-02..2025-11 lalu
   **HIDUP 2026-01..2026-06** dengan funding kembali (`sebaran_status` HIDUP 6).
   Klaim lama "tidak ada satu pun kasus kebangkitan terukur"
   (`cacah_simbol_bangkit_dapat_diuji` = 0 pada `kohort_ekor` V4) **DICABUT**: nol
   itu benar untuk kohort EKOR saja. Lahir aturan **74** dan KC-**37**.
2. **Bulan berfunding pertama nama dasar = bulan SETTLED terakhir** pada ketiga
   pasangan berkohort banyak (BNXUSDT 2023-02, ICPUSDT 2022-09, TLMUSDT 2023-03),
   terukur atas seluruh 15 pasangan oleh `silang_settled` V1. Lahir **H-A015**,
   yang MENANG sebagai angka tetapi **DIBATASI** sebagai tafsir.
3. **Selisih 12 (19.598 − 19.586) akhirnya punya calon identitas bernama** —
   sembilan nama berpasangan SETTLED yang kehilangan tepat satu bulan, ditambah
   tiga bulan BNXUSDT. Masih dugaan; dipraregistrasi sebagai **R-288**.
4. **Empat kekalahan yang seluruhnya dapat dicegah tanpa jaringan** (R-281
   aritmetika sendiri, R-282 nama laporan, R-284 nama modul, R-285 butir 3),
   melahirkan aturan **70, 71, 72, 73** dan KC-**34, 35, 36**.
5. **CI 630 → 638 → 662**, ketiganya terverifikasi pada ref runner masing-masing.

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
    lewat `list_commits` dengan `path="reports/<berkas>.json"`. **[v39] Ditaati
    enam kali lagi**: R-279 pada ref `2719e231`, R-280/R-281 pada `f787d70c` dan
    `0aac1dba`, R-282 pada `38bb1628`, R-285 pada `e2a37ff7`, R-286 pada
    **`12a65cbb`**, R-287 pada **`32088010`**. Perangkap ini menyala berulang:
    sesudah push, laporan di `main` sudah memuat commit run BERIKUTNYA.
46. Kode dilarang menyimpulkan dari penyebut nol; medan yang menyimpulkan wajib
    memeriksa lebih dulu apakah kasusnya mampu membedakan. Ditaati `terhenti`
    V2/V3/V4 dan `silang_settled` V1 (`bulan_berfunding_pertama_lokal`
    mengembalikan None, bukan nol).
48. Berkas modul yang mendekati pagar 800 baris dipecah SEBELUM fungsi baru
    ditambahkan. Berlaku atas `funding.py` dan `silang_funding.py` (705 SERI).
    **[v39] RENCANANYA DITINJAU:** jurnal 111 §5 menemukan preseden yang lebih
    baik daripada memecah — `lubang_tengah.py` dan `silang_settled.py` **MENGIMPOR**
    fungsi `silang_funding` tanpa menyalinnya, sehingga definisi tetap SATU
    (aturan 36) dan `sidik_kode` laporan lama tidak batal. Pemecahan hanya boleh
    dijalankan bila ada alasan yang mengalahkan preseden ini.
50. Setiap pengukuran yang menyimpulkan dari KETIADAAN wajib memuat kendali
    positif. `terhenti` V2..V4 `kendali_sah` true; `silang_settled` V1 `kendali_sah`
    true (BTCUSDT 2021-05/-08/-01 HIDUP, berfunding, 2,72–2,77 MB).
52. Laporan yang tidak dapat dibaca utuh setara dengan laporan yang tidak ada.
    Ekor SETIAP berkas kode dan berkas panjang yang didorong wajib dibaca sesudah
    push. **[v39] Ditaati atas jurnal 106–113 satu per satu**, dan atas
    `terhenti.py` V4 (blob `aaceb023`) serta `tests/test_terhenti.py` V4 (blob
    `1c4afa6f`) SEBELUM angka apa pun dibaca — berkas uji itulah yang pernah
    dirusakkan `}` liar di V3. Laporan `silang_funding` penuh 183.963 B tetap tak
    terbaca utuh selamanya.
55. Sebelum meramalkan hasil workflow, baca `paths`/`paths-ignore` dan sebutkan
    workflow MANA yang menyala. `ci.yml` mengabaikan `journal/**`, `decisions/**`,
    `hipotesis/**`, `reports/**`. `ukur_baris.yml` hanya atas
    `lux_ai/serapan/ukur_baris.py`; `semesta_kuota.yml` hanya atas
    `lux_ai/serapan/semesta_kuota.py`; `terhenti_semesta.yml` hanya atas
    `lux_ai/semesta/terhenti.py` dan dirinya sendiri.
57. Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB ditulis
    BERNOMOR dan nomor terakhirnya dipakai sebagai cacahan. **TERBUKTI BEKERJA
    LIMA BELAS DARI LIMA BELAS [v39]:** 382, 396, 450, 494, 526, 552, 584, 598,
    610, 623, 630, 630, **638**, **662** (dan 662 dua kali bila commit PROMPT
    dihitung). Mekanismenya deterministik — itu sebab keberhasilannya, bukan
    kecakapan meramal.
58. Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH dalam
    giliran yang sama DILARANG diramalkan dengan pita sempit. Pilih: (a) baca
    ulang utuh; (b) pita batas atas ≥1,8× batas bawah; (c) jangan meramal, ukur.
63. **[DIAMANDEMEN v37, DIPERKUAT v38]** Setiap klaim tentang kematian,
    kebangkitan, lubang funding, dan `bagian_mati` WAJIB menyebut batas
    semestanya secara tersurat: penyebut **787** simbol adalah `perpetual_usdt`,
    dan ia PERSIS seluruh perpetual USDT di arsip. Semesta arsip **937** simbol,
    **21.789** bulan; **150** hanya-arsip; **0** hanya-penyebut. Frasa lama
    "hampir seluruhnya BUSD/USDC" **DICABUT** (terukur 80 dari 147). Pada bulan
    tutup semesta **49 nama di luar penyebut masih terbit**, di antaranya **38 dari
    39** perpetual USDC.
64. Ramalan tentang nilai EKSTREM wajib menyebut perlakuan atas SERI, dan medan
    yang menamai pemegang ekstrem wajib melaporkan SELURUH pemegangnya bila seri.
    Perbaikan wajib di `ukur_baris` **V6**; `semesta_kuota` sudah benar sejak V1.
65. Setiap daftar contoh WAJIB menyebut CARA pemilihannya, dan kalimat sifat
    tentang KESELURUHAN himpunan DILARANG disusun dari contoh yang bukan
    seluruhnya. **[v39] Contoh yang benar:** sampel `diagnosa_kc15` **bukan** urut
    abjad melainkan berlapis atas delapan pecahan, dan modul itu menyatakannya.
66. **[lahir salah lalu DIREVISI]** Setiap cacahan semesta wajib menyebut KELAS
    INSTRUMEN yang dicacah. **Sebelum menuduh sebuah batas tidak ada, berkas
    penyaringnya WAJIB dibaca lebih dulu.** Perluasan: sebelum menulis modul baru,
    LISTING direktori paket dan direktori workflow lebih dulu. **[v39] Dilanggar
    sendiri di R-283**, yang menyebut jalur `lux_ai/serapan/kc15.py` yang tidak
    ada; nama benarnya `diagnosa_kc15.py` (16.268 B, blob `3642e5b6`).
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
    besaran yang sama.** Terbayar langsung: jumlah kolom bulan tabel 15 pasangan
    `terhenti` V4 = **36**, sama persis dengan "total bulan SETTLED 36" yang diukur
    `bulan_settled.py` V1 dengan kode lain atas bahan lain. **Pengukuran yang tak
    dapat dicocokkan dengan pengukuran lain mana pun harus dianggap belum diuji.**
70. **[v39, jurnal 108, lahir dari R-281] Sebelum praregistrasi dikunci, setiap
    butir yang saling menentukan wajib dijumlahkan silang; praregistrasi yang tidak
    konsisten dengan dirinya sendiri adalah ramalan CACAT, dan kecacatannya milik
    peramal, bukan milik data.** R-281 mematok 36 bulan DAN 11 nama bersatu-bulan,
    padahal 11×1 + (9+9+6) = 35 ≠ 36. Pemeriksaan ini gratis: tanpa jaringan,
    tanpa run. Lihat KC-34.
71. **[v39, jurnal 109, lahir dari R-282] Sebelum mempraregistrasi ramalan atas
    laporan yang belum pernah dibaca, modul penghasilnya wajib dibaca lebih dulu**
    — setidaknya docstring dan tetapannya — untuk mengetahui besaran apa yang
    benar-benar diukur. Ramalan atas medan yang tidak pernah diukur laporan itu
    gugur otomatis dan tidak boleh dihitung sebagai kekalahan data. Saudara aturan
    66 dan 67: *baca berkasnya dulu*, kini juga untuk berkas yang akan DIRAMALKAN.
72. **[v39, jurnal 110] Sebuah laporan hanya membuktikan apa yang benar-benar
    disampelnya; cakupan kode cacat yang dinamai dalam judulnya boleh jauh lebih
    luas.** Maka (a) jangan memakai laporan sempit untuk menilai klaim luas, dan
    (b) jangan memakai luasnya nama untuk meramalkan isi yang sempit. Setiap
    adjudikasi wajib menyebut penyebut sampel laporan sebelum menyebut putusannya.
    **Turunan yang mengikat:** angka terbitan wajib disebut bersama penyebutnya —
    880 lubang funding (seluruhnya) lawan 877 (yang jatuh di dalam 19.586).
73. **[v39, jurnal 111, lahir dari R-284] Dilarang mempraregistrasi ramalan atas
    ISI sebuah berkas yang belum pernah dibaca ketika satu-satunya dasar ramalan
    adalah NAMA berkas itu.** Yang boleh dipraregistrasi adalah artefak yang
    dihasilkan kode yang SUDAH dibaca, atau angka yang dapat diturunkan dari
    pengukuran yang sudah ada. Bila sebuah berkas perlu diketahui, bacalah —
    pembacaan tidak butuh run, tidak butuh jaringan, dan tidak berbiaya.
74. **[v39, jurnal 112, lahir dari R-285] Setiap nol yang dipakai sebagai dasar
    ramalan wajib disebut bersama PENYEBUT dan DEFINISI ujinya; bila penyebut
    ramalan berbeda dari penyebut nol itu, nol itu tidak boleh dipakai.** Pasangan
    aturan 72. Kasus asalnya: `cacah_simbol_bangkit_dapat_diuji` = 0 pada
    `kohort_ekor` V4 dipakai untuk menolak kebangkitan di TENGAH riwayat, dan
    LITUSDT membantahnya. Lihat KC-37.
75. **[v39, jurnal 113, lahir dari R-286] Setiap cacahan "cocok" wajib disertai
    medan pembeda MEKANISME, dan pita ramalan wajib menyebut mekanisme mana yang
    dihitung.** Cacah kecocokan yang mencampur mekanisme DILARANG dipakai untuk
    memperkuat hipotesis sebelum dipisah. Kasus asalnya: kecocokan keempat R-286
    (`MINAUSDT`) berasal dari mekanisme lain — simbol yang LAHIR pada bulan itu
    dengan `cacah_lubang` 0 — bukan funding yang menyusul 16–20 bulan. Lihat KC-38.

## Kelas cacat

KC-1 s.d. KC-12 seperti v19; KC-10 dan KC-11 DITUTUP. KC-13 keterwakilan sampel
(penangkal aturan 37). **KC-16 DITARIK — nomornya TETAP kosong selamanya.**
KC-17 DITUTUP. Teks penuh KC-14, KC-15, KC-19–KC-29 ada di v37 (blob `f520d5e2`);
yang wajib dibawa:

- **KC-14** — menit hilang NYATA di arsip 1m: **9** simbol-bulan, **6.375** menit
  (425×15). Sebab tak diketahui (H-A004 tak dapat diuji). Karantina (ADR-A006).
- **KC-15 [DIKOREKSI v39]** — klines BULANAN kehilangan HARI UTC penuh: **3**
  simbol-bulan, semuanya BNXUSDT 2022 (**2022-04, 2022-06, 2022-08**, disebut
  harfiah di docstring `diagnosa_kc15.py`), **7.200** menit = **5 hari UTC**.
  **Hari-hari itu UTUH di arsip HARIAN** — jurnal 109 §5.2 yang menyebutnya "tidak
  diterbitkan" **DICABUT**. Yang benar-benar tak terjelaskan hanyalah **210 menit
  TEPI** pada 2022-04, dan itu pun konsisten dengan peluncuran pukul **03:30 UTC**
  (`stempel_pertama_ms` 1648783800000; berkas harian 2022-04-01 memuat 1.230 =
  1.440 − 210 baris; `menit_tepi_hadir` 0 dari 210). Anatomi bulan itu:
  `cacah_baris_1m` 41.550, `menit_kalender` 43.200, `menit_hilang_di_tengah`
  **1.440**, `tepi_awal` 210, `gerbang_lolos` **false**, pelanggaran
  `tanpa_menit_hilang` + `jarak_60_detik`, `posisi` pertama (dikecualikan dari
  putusan), `putusan` TEPI_TAK_TERJELASKAN, `checksum_bulanan` `14bd6937…`.
  43.200 − 41.550 = 1.650 = 1.440 + 210 ✅ Pembagian 5 hari ke tiga bulan BELUM
  diukur. 9 + 3 = **12** karantina; 6.375 + 7.200 = **13.575** menit; **516.135**
  baris. Kebijakan ADR-A007 masih DIUSULKAN.
- **KC-18** — lilin datar lolos gerbang struktural; gerbang menilai BENTUK, bukan
  kehidupan. Semesta `perpetual_usdt` atas **19.586** simbol-bulan lolos: **1.401
  MATI** (7,153%), **98 SEPI** (0,500%), **18.087 HIDUP** (92,35%); 945 MATI di
  luar kohort puncak. Dari 1.401 MATI, **842** kehilangan funding dan **559**
  tetap berfunding. **Kematian dapat berbalik** — dan sejak v39 itu bukan lagi
  dugaan: LITUSDT MATI 2025-02..2025-11 lalu **HIDUP 2026-01..2026-06 terukur**.
  Kematian permanen tetap punya contoh telak: BTCSTUSDT 53 dari 53 MATI.
  **Kecocokan bulan membuktikan PENAMAAN kontrak, bukan perdagangan** — mengikat
  atas H-A013, H-A015, dan seluruh laporan `silang_settled`. ADR-A008 Keputusan
  1–6 DITERIMA; Keputusan 7 DITANGGUHKAN.
- **KC-19** mencacah dari ingatan (aturan 57). **KC-20** taksiran baris bias ke
  BAWAH (58). **KC-21** ketiadaan gejala dari ketiadaan pengukuran (59). **KC-22**
  memindahkan MEKANISME (60). **KC-23** memindahkan MEDAN (61). **KC-24** bertanya
  DAFTAR kepada laporan bercacah (62). **KC-25** batas semesta tak tersurat (63).
  **KC-26** medan ekstrem membisu tentang SERI (64). **KC-27** mengarakterisasi
  himpunan dari contoh BERURUT (65). **KC-28** mencampur kelas instrumen — berlaku
  atas arsip **937**, BUKAN atas penyebut 787 (66). **KC-29** taksonomi PARALEL
  (lubang aturan 22).
- **KC-30** — membaca NAMA KELAS sebagai KEADAAN (`futures_kedaluwarsa` memuat 44
  terhenti dan **6 HIDUP**; `perpetual_usdc` 38 dari 39 hidup). Penangkal 67.
- **KC-31** — membaca nama PERISTIWA sebagai MEKANISMENYA ("peralihan" yang
  ternyata hanya **penambahan**). Penangkal 68.
- **KC-32** — mencampur DUA SISTEM PENOMORAN (utang verifikasi nomor 28 lawan
  **ramalan R-28**). **R-28 tetap MENUNGGU**; bunyinya ada di STATE v23 dan belum
  dibaca. Teks jurnal 105 TIDAK disunting (aturan 29); kalimatnya DILARANG
  diwarisi.

- **KC-33 [v39, jurnal 107] — mengenali satu peristiwa lalu berhenti mencari yang
  kedua.** `SXPUSDTSETTLED` disebut "satu peristiwa penamaan yang sedang
  berlangsung", dan pertanyaan apakah ada peristiwa serupa yang sudah SELESAI tidak
  diajukan. Jawabannya ada di data yang sama: **`BDXNUSDT`** (dasar berhenti
  2026-03, SETTLED terbit 2026-04 lalu berhenti). Sebabnya: peristiwa yang sedang
  berlangsung menyisakan jejak di bulan tutup, yang sudah selesai tidak. Maka
  pencarian pola WAJIB atas seluruh rentang, bukan atas ekor.
- **KC-34 [v39, jurnal 108] — menurunkan cacah subkelompok dengan pengurangan di
  kepala** lalu memakainya sebagai angka terverifikasi tanpa mencocokkannya ke
  jumlah yang sudah dipegang. Sumber datanya benar, totalnya benar; satu langkah
  aritmetika sepele tak pernah diperiksa. Penangkal aturan 70.
- **KC-35 [v39, jurnal 109, DIPERSEMPIT di jurnal 110] — menyamakan CAKUPAN sebuah
  kode cacat dengan CAKUPAN satu laporan yang namanya memuat kode itu.** KC-15
  berlaku atas tiga bulan; `diagnosa_kc15.json` memeriksa **satu** tersangka
  (`TERSANGKA_TEPI = (("BNXUSDT", "2022-04"),)`) plus 37 bulan tengah tersampel.
  Nama berkasnya benar; yang salah adalah anggapan bahwa satu berkas melaporkan
  seluruh cakupan kode cacatnya. Penangkal aturan 72.
- **KC-36 [v39, jurnal 111] — homonim di dalam kosakata riset sendiri diperlakukan
  sebagai satu konsep.** "Tengah" berarti dua hal tak berhubungan: posisi hari di
  dalam bulan klines (KC-15) dan bentuk lokal lubang FUNDING; begitu pula
  "lubang". Setiap istilah yang dipakai di dua modul wajib disebut bersama
  pemiliknya — "lubang funding bentuk tengah" lawan "hari hilang di tengah bulan"
  — dan DILARANG disingkat menjadi "lubang tengah". Penangkal aturan 73.
- **KC-37 [v39, jurnal 112] — memakai nol dari satu penyebut sebagai bukti
  ketiadaan gejala di penyebut lain.** `cacah_simbol_bangkit_dapat_diuji` = 0 benar
  untuk kohort EKOR dan tidak berkata apa pun tentang kebangkitan di tengah
  riwayat. Bedanya dengan aturan 59: di sana pengukurannya tidak ada, di sini
  pengukuran ADA tetapi penyebutnya lain. Penangkal aturan 74.
- **KC-38 [v39, jurnal 113] — mencacah "kecocokan" tanpa membedakan MEKANISMENYA.**
  Empat kecocokan butir 1 R-286 berasal dari dua mekanisme berbeda; pita yang cukup
  lebar dapat dimenangkan oleh kasus yang tidak mendukung tafsirnya. Keluarga
  dengan KC-30/KC-31. Penangkal aturan 75.

## Semesta riset = `perpetual_usdt` = penyebut 787 — TERBUKTI DUA ARAH [v37]

Sumber: `semesta_kuota.py` **V3**, commit `db4a192d`, run 30456422183, laporan
blob `8adae5ee` (UTUH), `sidik_kode` `ef0c4a24…`, `bukan_bukti` false.

- `cacah_perpetual_usdt` **787** = `cacah_penyebut_simbol` **787**
- `cacah_perpetual_usdt_luar_penyebut` **0**; `cacah_penyebut_bukan_perpetual_usdt`
  **0**; `cacah_penyebut_bukan_akhiran_usdt` **0**; `cacah_penyebut_luar_arsip`
  **0**; `penyebut_bagian_arsip` true.

Karena KEDUA arah nol, ini **kesamaan himpunan**, bukan himpunan bagian.

Batas yang wajib ikut disebut (`taksonomi.CATATAN_BATAS`): token **saham, ETF, dan
komoditas** (mis. `AAPLUSDT`, `XAUUSDT`) tak dapat dibedakan lewat bentuk nama,
jadi mereka **IKUT di dalam 787**. **[v39] `AAPLUSDT:2026-05` kini terbukti nyata
di dalam sampel `diagnosa_kc15`, dan bulannya lolos gerbang bersih** — utang
"token saham di 787" punya satu bukti terukur.

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

**ANGKA WARISAN YANG DICABUT [v38, DIKUATKAN v39].** "16 simbol non-ASCII" adalah
HANTU. Terukur **3 nama / 19 bulan**: 币安人生USDT 9, 我踏马来了USDT 6, 龙虾USDT 4;
9+6+4 = **19** ✅ Ketiganya `perpetual_usdt`, jadi ADA di penyebut. **[v39] Angka 3
muncul untuk ketiga kalinya dari pengukuran berbeda** (`kelas_risiko_tersentuh`
di `diagnosa_kc15.json`: `non_ascii` 3), dan ketiganya TEPI_BERSIH dengan URL
ter-persen-enkode. Asal-usul angka 16 tetap belum diketahui.

### Taksonomi LOKAL modul (kuota) — dipertahankan berdampingan

USDT 805 nama/19.785 bulan (15 SETTLED) · TAK_DIKENAL 51/260 · BUSD 41/812 ·
USDC 39/893 · BTC 1/39. `TAK_DIKENAL` 51 = 50 `futures_kedaluwarsa` + 1
`perpetual_usd1` (`BTCUSD1`); 258 + 2 = 260 ✅ **150 hanya-arsip = 147
bukan-akhiran-USDT + 3 indeks**; dari 147 itu BUSD+USDC = **80** (54,4%).

### Penguraian selisih 163 — identitas utuh

`bulan_usdt_bukan_settled` 19.749 · `bulan_arsip_milik_penyebut` **19.598** ·
`bulan_arsip_milik_hanya_arsip` **151** · `bulan_lolos_gerbang` 19.586 ·
`selisih_total` **163** · `selisih_dalam_penyebut` **12** ·
`selisih_dari_hanya_arsip` **151** · `identitas_utuh` true.
19.598 + 151 = 19.749 ✅ · 12 + 151 = 163 ✅ · 19.598 − 19.586 = **12** ✅

**151 bulan itu SELURUHNYA milik ketiga indeks.** Kesamaan angka **12** dengan 12
simbol-bulan karantina bukan bukti identitas himpunan — **tetapi [v39] ia kini
punya calon identitas bernama; lihat bagian "Bulan absen" di bawah.**

## Bulan ABSEN — calon identitas selisih 12 [v39, jurnal 113 §6]

Dihitung tangan dari `reports/silang_settled.json` (aturan 21): rentang bulan =
`bulan_klines_terakhir` − `bulan_klines_pertama` + 1, dibandingkan dengan
`cacah_bulan_klines` (bulan LOLOS gerbang).

| simbol | pertama | terakhir | rentang | lolos | **absen** | bulan SETTLED |
|---|---|---|---:|---:|---:|---|
| AERGOUSDT | 2024-09 | 2026-06 | 22 | 21 | **1** | 2025-04 |
| AIAUSDT | 2025-09 | 2026-06 | 10 | 9 | **1** | 2026-01 |
| BDXNUSDT | 2025-06 | 2026-03 | 10 | 10 | 0 | 2026-04 |
| BNXUSDT | 2022-05 | 2026-06 | 50 | 48 | **2** (**3** atas rentang ARSIP 2022-04..2026-06 = 51) | 2023-02 |
| CTKUSDT | 2020-11 | 2026-06 | 68 | 67 | **1** | 2025-04 |
| CVCUSDT | 2020-11 | 2026-06 | 68 | 67 | **1** | 2025-05 |
| CVXUSDT | 2022-09 | 2026-06 | 46 | 45 | **1** | 2025-07 |
| ICPUSDT | 2021-05 | 2026-06 | 62 | 62 | 0 | 2022-09 |
| LITUSDT | 2021-02 | 2026-06 | 65 | 64 | **1** | 2025-12 |
| MAVIAUSDT | 2024-02 | 2026-06 | 29 | 28 | **1** | 2025-03 |
| MINAUSDT | 2023-02 | 2026-06 | 41 | 41 | 0 | 2023-02 |
| PUMPUSDT | 2025-04 | 2026-06 | 15 | 14 | **1** | 2025-07 |
| SLPUSDT | 2023-10 | 2026-06 | 33 | 32 | **1** | 2025-07 |
| SXPUSDT | 2020-07 | 2026-05 | 71 | 71 | 0 | 2026-06 |
| TLMUSDT | 2021-07 | 2026-06 | 60 | 60 | 0 | 2023-03 |

Jumlah: **9 × 1** (AERGO, AIA, CTK, CVC, CVX, LIT, MAVIA, PUMP, SLP) + **3**
(BNXUSDT atas rentang arsip) = **12**, sama dengan 19.598 − 19.586 = **12**; dan
KC-14 mencacah **9** simbol-bulan, KC-15 mencacah **3** (BNXUSDT 2022).

**Tiga kehati-hatian yang WAJIB menyertainya:**

1. Bulan absen bisa berarti **tidak ada di arsip** atau **ada tetapi gagal
   gerbang** (karantina). Laporan ini tidak membedakannya, dan `bulan_didaftar`
   BNXUSDT justru menunjukkan keduanya bisa berbeda (lihat di bawah).
2. **772 nama penyebut lain belum diperiksa.** Satu saja punya bulan absen, dan
   jumlahnya melampaui 12 → tafsirnya gugur. Penyebut yang benar untuk klaim
   "inilah keduabelasnya" adalah **787**, bukan 15.
3. Bulan MANA yang absen belum diukur. Itu isi **R-288**.

**Kasus paling telak:** LITUSDT kehilangan tepat satu bulan dari rentangnya, dan
`LITUSDTSETTLED` bermuatan **2025-12** — bulan di antara bulan MATI terakhir
(2025-11) dan bulan HIDUP pertama (2026-01). Bila bulan absen itu 2025-12, maka
bulan SETTLED **bukan** "bulan di sela hidup nama dasar" melainkan **bulan yang
nama dasarnya tidak punya sama sekali**, dan **H-A014 salah bentuk**.

## H-A015 — MENANG sebagai angka, DIBATASI sebagai tafsir [v39]

Sumber: `lux_ai/serapan/silang_settled.py` V1 (blob `3eea2a80`, dibaca UTUH),
laporan `reports/silang_settled.json` blob **`755bbaef`** pada ref runner
**`12a65cbb`** (run **30469781160**), dibaca UTUH. `sidik_kode` `0d814bc6…`,
`sidik_kode_silang_funding` `8a9b859c…` (sama dengan laporan `lubang_tengah` V2 →
definisi bentuk tetap SATU, aturan 36), `sidik_data_funding` `2c9fbd1b…`,
`versi_funding` 6, `bukan_bukti` false.

Penggugur SELURUHNYA aman (aturan 24): `sidik_seragam` true ·
`cacah_laporan_dibaca` 8/8 · `cacah_kunci_ganda` 0 · `kendali_sah` true ·
`selisih_penyebut` **0** (`penyebut_kehidupan` 19.586) ·
**`selisih_kendali_funding_pertama` 0** · `cacah_pasangan` 15. Kode keluar **0**.

**Kesetaraan definisi TERUJI, bukan diasumsikan (KC-9):** 5 dari 5 cocok antara
definisi LOKAL (`bulan klines pertama yang TIDAK berlubang funding`) dan terbitan
`lubang_tengah` V2 — BNXUSDT 2023-02, ICPUSDT 2022-09, JUPUSDT 2024-02, QTUMUSDT
2020-03, TLMUSDT 2023-03.

`sebaran_arah` = {`sama` **4**, `lebih_awal` **11**, `lebih_lambat` **0**,
`tak_terukur` **0**}; 4 + 11 = **15** ✅ `h_a015_menang` true.

- **Yang didukung:** pada ketiga pasangan berkohort banyak, bulan SETTLED terakhir
  = bulan berfunding pertama nama dasar, sesudah **19/16/20** bulan klines tanpa
  funding. Maka bulan-bulan itu bukan data hilang: fundingnya **milik kontrak
  lain**. Kohort 3 dari 3 berlubang > 10; keduabelas pasangan bersatu-bulan
  berlubang < 10.
- **Yang DIBANTAH:** bentuk KUAT H-A015 ("bulan SETTLED jatuh pada atau tepat
  sebelum bulan berfunding pertama"). Pada **11 dari 15** pasangan bulan SETTLED
  jatuh **jauh SESUDAH** funding pertama (CTKUSDT 2020-11 lawan 2025-04; SXPUSDT
  2020-07 lawan 2026-06). Maka bulan SETTLED punya **DUA peran**: batas awal
  kontrak berikutnya (3 pasangan berkohort banyak) dan bulan penutupan kontrak
  berjalan (12 pasangan bersatu-bulan). Aturan 20 mengikat: jangan menyimpulkan di
  luar rentang.
- **Cela yang wajib diwarisi (KC-38, aturan 75):** kecocokan keempat adalah
  `MINAUSDT`, dan mekanismenya lain — `bulan_klines_pertama` =
  `bulan_berfunding_pertama` = `bulan_settled_terakhir` = 2023-02 dengan
  `cacah_lubang` **0**; ia cocok semata karena nama dasarnya MULAI terbit pada
  bulan rombak penamaan 2023-02.
- `cacah_lubang` bukan nol di luar kohort banyak hanya **LITUSDT 5** dan **SXPUSDT
  5**; sepuluh sisanya **0**.
- KC-18 tetap mengikat: yang terbukti adalah PENAMAAN dan penerbitan funding,
  bukan perdagangan.

## Lubang funding — 880 lawan 877, dan keenam lubang TENGAH [v39]

Sumber: docstring `lux_ai/serapan/lubang_tengah.py` V2 (blob `4d3beaf1`, dibaca
UTUH di jurnal 111) dan laporan `reports/lubang_tengah.json` V2 blob `39cd1caa`
pada ref runner **`e2a37ff7`** (run **30440471508**), dibaca UTUH:
`versi_lubang_tengah` 2, `sidik_kode` `c9372bd7…`, `sidik_seragam` true,
`cacah_laporan_dibaca` 8/8, `kendali_sah` true, `selisih_lubang_tengah` **0**.

- **880** = SELURUH lubang funding; **877** = yang jatuh di dalam penyebut
  **19.586**, dengan bentuk lokal {awal **45**, ekor **826**, tengah **6**,
  seluruh **0**}; 45+826+6+0 = **877** ✅ Selisih **3** = lubang di luar penyebut
  (tiga bulan BNXUSDT). **Irisan 880 lawan 877 tetap UTANG**, bukan angka
  terverifikasi — tak satu pun laporan menerbitkannya (aturan 72).
- **Keenam lubang TENGAH dimiliki hanya DUA simbol** (`SIMBOL_TENGAH_TERCATAT =
  ["BTCSTUSDT", "LITUSDT"]`): **LITUSDT 2025-07..2025-11 (5)** dan **BTCSTUSDT
  2022-01 (1)**; 5 + 1 = 6 ✅ Keenamnya MATI (`sebaran_status` MATI 6, SEPI 0,
  HIDUP 0, TAK_TERUKUR 0). **Inilah asal-usul "dua cabang" Keputusan 7 ADR-A008.**
- **Pemilik ke-33 lubang pada simbol-bulan HIDUP:** BNXUSDT, ICPUSDT, **JUPUSDT**,
  **QTUMUSDT**, TLMUSDT; ke-33 lubang HIDUP itu SEMUANYA berbentuk awal.
- Bentuk ekor terjelaskan oleh kematian pasar: lubang → mati **96,0%** (842/877);
  mati → lubang **60,1%** (842/1.401). Lubang funding TIDAK sah sebagai penyaring
  kematian.
- `funding.py` V6 mencacah **87** "funding tanpa klines" atas 787 simbol;
  `funding_tanpa_klines` KOSONG pada kelima simbol H-A010 (**R-229 TEPAT**).

### LITUSDT — urutan peristiwa, dan kebangkitan terukur pertama

1. MATI **2025-02..2025-11** (10 bulan); kematian MENDAHULUI hilangnya funding
   (aturan 61, KC-23).
2. Lubang funding bentuk TENGAH **2025-07..2025-11** (rentetan **5**); berfunding
   terakhir **2025-06**, kembali **2026-01**. Ketidakcocokan docstring 2025-06
   lawan 2025-07 **LUNAS**: funding terakhir 2025-06, lubang mulai 2025-07 — beda
   rujukan, keduanya benar.
3. `LITUSDTSETTLED` bermuatan **2025-12**, tepat di sela.
4. **HIDUP 2026-01..2026-06 dengan funding kembali** (`h_a011_menang` true,
   `h_a011_cacah_hidup` **6**, `terukur` true). **H-A011 MENANG.**

### BTCSTUSDT 2022-01 — satu-satunya lubang tengah yang benar-benar tak terjelaskan

`cacah_lilin` **44.640** (31 × 1.440, penuh), `byte_parquet` **399.757**, klines
terbit 2021-03..2026-06 (**64 bulan**, hanya **1** lubang funding), status
**MATI**. Jadi ada bulan berlilin PENUH yang tetap MATI — bukti langsung bahwa
"berkas ada" ≠ "pasar hidup". **Keputusan 7 ADR-A008 DILARANG diambil sebelum
bulan itu dianatomi seperti BNXUSDT 2022-04.**

## Terhenti lawan hidup per jenis — TERUKUR [v38, dilengkapi V4 di v39]

Sumber V3: laporan blob **`e4f71ba8`** ref runner **`9aad0576`**, `sidik_kode`
`d892391d…`, `sidik_data` `6128fbb0…`, `sumber` `reports/semesta_rentang.json`
110.662 B, `sumber_bersidik` **false** (utang aturan 22), `bukan_bukti` true,
`kendali_sah` true, `identitas_per_jenis_utuh` true, `daftar_nama_terpotong` false.
Sumber V4: `terhenti.py` V4 blob **`aaceb023`** commit **`6cc335e3`**, laporan blob
**`b5a1102c`** ref runner **`4dbf06a7`**, `sidik_kode` **`b8d0571d…`**,
`sidik_data` `6128fbb0…` (tak berubah — masukan sama, kode lain).

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
**AERGOUSDT, AIAUSDT, MINAUSDT, PUMPUSDT** [v39].

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
total bulan SETTLED yang diukur `bulan_settled.py` V1 dari laporan lain dengan kode
lain (aturan 69).

**Yang wajib dibawa dari `reports/bulan_settled.json` (blob `31d3971e`, ref runner
`0aac1dba`, dibaca UTUH):**

1. **"DUA BERSAMBUNG" DICABUT.** `TLMUSDTSETTLED` sembilan bulannya adalah 2022-01,
   2022-02, **2022-04**..2022-08, 2023-02, 2023-03 — lubang 2022-03 dan jurang
   lima bulan 2022-09..2023-01; rentang kalender 15 bulan, terbit 9. Yang benar:
   **satu bersambung (`ICPUSDT_SETTLED` 2022-01..2022-09) dan dua bercelah (TLM,
   BNX)**.
2. `BNXUSDTSETTLED` = 2022-04..2022-08 (lima bersambung) + 2023-02; jurangnya sama
   persis dengan jurang TLM.
3. **`bulan_didaftar` BNXUSDT = 2022-04..2026-06 PENUH, 51 bulan tanpa lubang.**
   Maka "3 lubang tengah 2022-04/-06/-08" adalah lubang **gerbang kehidupan**,
   bukan berkas yang tak diterbitkan. `bulan_didaftar` ≠ bulan lolos gerbang.
4. **Ketiga bulan lubang BNXUSDT ada di dalam `BNXUSDTSETTLED`** — calon penjelasan
   KC-15, tetapi jurnal 110 menurunkannya menjadi **ASUMSI LEMAH**: penjelasan
   terukur yang lebih sederhana adalah perakit arsip BULANAN kehilangan hari
   sementara arsip HARIAN utuh.
5. **Penamaan SETTLED datang BEROMBAK:** 2023-02 memuat TIGA nama (BNX, MINA, TLM)
   dan 2025-07 memuat TIGA (CVX, SLP, PUMP).
6. **DUA BELAS nama bersatu-bulan** (bukan 11 — itu kekalahan R-281): AERGO, AIA,
   BDXN, CTK, CVC, CVX, LIT, MAVIA, MINA, PUMP, SLP, SXP. Tiga lebih panjang: ICP
   9, TLM 9, BNX 6. 12 + 3 = 15 ✅ 12×1 + 24 = **36** ✅
7. `definisi_dapat_dibedakan` **false** pada H-A013 (menang 6/6): kemenangan itu
   tetap tak dapat membedakan hipotesis (aturan 46). Kendali BTCUSDT 78 bulan ≥ 60.
8. **`BDXNUSDT` adalah penghuni ekor 2026-03**, satu-satunya. Ekor kini bernama
   sebagian: 2026-03 = BDXNUSDT, 2026-05 = SXPUSDT; tiga nama 2026-04 belum
   bernama, satu di antaranya `BDXNUSDTSETTLED`.

## H-A013 — MENANG 6–0, TAFSIRNYA DICABUT [v38]

Enam bulan peralihan cocok dengan bulan saudara SETTLED-nya (CTK 2025-04, CVC
2025-05, CVX 2025-07, LIT 2025-12, MAVIA 2025-03, SLP 2025-07), `cacah_cocok_bulan`
6, `ambang_menang` 4, `cacah_peralihan_terhenti` **0**, dan **keenam nama dasar
masih terbit 2026-06**. Rantai pelemahan tafsir, lengkap: "delapan kebangkitan" →
"dua bersambung + enam peralihan nama" → **bukan peralihan sama sekali, melainkan
PENAMBAHAN nama kontrak selesai** (aturan 68, KC-31).

DUA konvensi nama hidup berdampingan: `ICPUSDT_SETTLED` bergaris bawah, empat
belas lainnya TANPA. Docstring `penyebut_tahun.py` menulis `TLMUSDT_SETTLED`
(salah): dicatat, TIDAK disunting, tidak diwarisi (R-246 SEPARUH).

Cacah bulan ARSIP 24 nama, 24 dari 24 cocok, `cacah_gagal_daftar` 0,
`jumlah_bulan_didaftar` **518**: BNXUSDT 51 (48 di PENYEBUT) · CTKUSDT 68 ·
CVCUSDT 68 · CVXUSDT 46 · ICPUSDT 62 · LITUSDT 65 · MAVIAUSDT 29 · SLPUSDT 33 ·
TLMUSDT 60 · ICPUSDT_SETTLED 9 · TLMUSDTSETTLED 9 · BNXUSDTSETTLED 6 · dua belas
nama SETTLED lain bercacah 1.

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

**BELUM DIUKUR [v39]:** `tests/test_lubang_tengah.py`, `taksonomi.py`,
`pecahan.py`, `semesta_kuota.py` V3 (blob `7288b030`, 24.987 B),
`tests/test_semesta_kuota.py`, `terhenti.py` **V4**, `tests/test_terhenti.py`
**V4**, `survei.py`, `ringkas_semesta.py`, **`diagnosa_kc15.py`** (16.268 B, blob
`3642e5b6`), **`silang_settled.py`**, **`tests/test_silang_settled.py`**. Tidak
diramalkan dengan pita sempit (aturan 58 pilihan c). `ukur_baris.py` kini blob
`3ebaa9f9` (V5, 17.442 B).

## Modul dan workflow yang tercatat

**`lux_ai/semesta/`:** `__init__.py` 273 B (`4c2d1f25`) · `taksonomi.py` 7.086 B
(`b418c7ba`) · `terhenti.py` V1 5.300 B (`3fa8f697`), V2 `8121739b`, V3
`7b819787`, **V4 blob `aaceb023` pada commit `6cc335e3`**.

**`lux_ai/serapan/` [v39, dari listing]:** `diagnosa_kc15.py` (`3642e5b6`),
`lubang_tengah.py` V2 (`4d3beaf1`, 23.745 B), `semesta_kuota.py` (`7288b030`),
`ukur_baris.py` V5 (`3ebaa9f9`), **`silang_settled.py`** V1 (`3eea2a80`), dan modul
lain seperti tercatat v38.

**30 berkas di `.github/workflows/`** (blob): bentuk_semesta `dc393dd0` ·
bulan_settled `9e0829f2` · **ci `c79497b2`** · diagnosa_kc14 `6524646a` · kc14b
`a315c25b` · kc14c `82126b60` · kc15 `c5f2ee0f` · kc6 `6bae2b1b` · funding_semesta
`c1ce55f3` · kebangkitan `282b51aa` · kehidupan `3eb10655` · kehidupan_arsip
`8234e5dc` · kohort_ekor `2e747475` · lubang_tengah `557030de` · pecahan_serapan
`cd9e21d1` · penyebut_kc6 `14617b6b` · penyebut_tahun `8f0d5852` · probe_serapan
`9b356e15` · pulihkan_rilis `32bd1099` · rentang_kc6 `db1e77ae` · ringkas_semesta
`d6145d28` · semesta_kuota `b7e5a65a` · semesta_silang `babf08e4` · serap_pilot
`85694e0f` · silang_funding `23f8c870` · survei_semesta `a1fb0192` ·
taksonomi_semesta `b066b4db` · terhenti_semesta `baef4f41` · uji_resample
`121f3e25` · ukur_baris `f62be605`. **[v39] Ditambah workflow penghasil
`reports/silang_settled.json`** (pesan commit runner "laporan silang settled run
<run_id> [skip ci]"); listing ulang direktori workflow BELUM dijalankan pada sesi
56, jadi cacah 30 belum diperbarui — sebutkan sebagai belum terukur (aturan 66).

## API modul yang sudah terbaca dan boleh dipakai

Rincian v37 berlaku untuk `semesta_silang`, `silang_funding`
(`baca_laporan_kehidupan` — jalur sah menuju daftar penyebut), `arsip`
(`semesta_simbol`; tanpa `requests`; `fapi.binance.com` 451), `pecahan` (VERSI 6),
`taksonomi`, `semesta_kuota` V3, `penyebut_tahun`, `kehidupan_arsip`,
`kebangkitan`; tambahan v38 untuk `survei` (penghasil `semesta_rentang.json`),
`terhenti` V3, `ringkas_semesta`, `rentang_kc6`. Tambahan [v39]:

- **`silang_settled` V1** — `VERSI` 1, `KELUARAN` `reports/silang_settled.json`,
  `PENYEBUT_TERCATAT` 19586, `PASANGAN_SETTLED` (15 tetapan),
  `KOHORT_BANYAK` = (BNXUSDT, ICPUSDT, TLMUSDT), `FUNDING_PERTAMA_TERBITAN` (5
  tetapan kendali), tetapan pita `R286_*`, `ARAH` = (sama, lebih_awal,
  lebih_lambat, tak_terukur), `BERKAS_DICAP` = (kehidupan, kehidupan_arsip,
  silang_funding, silang_settled); fungsi `sidik_kode`,
  `bulan_berfunding_pertama_lokal`, `arah`, `baris_pasangan`, `sebaran_arah`,
  `kendali_funding_pertama`, `uji_h_a015`, `kode_keluar`, `jalankan`, `main`.
  **Ia MENGIMPOR `silang_funding` dan `kehidupan_arsip`, tidak menyalinnya.**
- **`diagnosa_kc15`** — `TERSANGKA_TEPI = (("BNXUSDT", "2022-04"),)`,
  `TOTAL_PECAHAN` diimpor dari `pecahan`, `serap.KELAS_RISIKO` berisi **5** kelas
  (`pra_header`, `terhenti`, `kendali_baru`, `non_ascii`, `bulan_awal_2020_2021`);
  `pilih_simbol` sampel BERLAPIS (bukan abjad) lima simbol per pecahan × delapan =
  40 diharapkan, **38** benar-benar dijalankan (1 tersangka + 37); selisih 40 − 38
  **belum dijelaskan**. Bulan tengah deterministik: median daftar bulan arsip
  sesudah kedua ujungnya dibuang. Uji silang aritmetika tertanam:
  `baris + tengah + tepi` wajib = `menit_kalender`.
- **`terhenti` V4** — menambah `pasangan_settled` (nama dasar diperoleh dengan
  membuang akhiran `SETTLED` **dan** `_SETTLED`; gagal → `tak_terpasangkan`,
  DILAPORKAN), `cacah_dasar_hidup`/`_terhenti`/`_tak_ada`,
  `cacah_settled_mendahului`, `identitas_pasangan_utuh`, `kendali_pasangan_sah`.

## Hipotesis

- H-A001 belum diuji · H-A002b GUGUR · H-A003 MENANG pada 3, GUGUR pada 9 ·
  H-A004 tak dapat diuji (451) · H-A005 GUGUR pada rentang tersampel · H-A006
  MENANG enam run · H-A008 MENANG dua kali · H-A009 GUGUR · H-A010 **MENANG 5–0**
  (`funding_tanpa_klines` kosong pada kelimanya) · **H-A011 MENANG [v39]** —
  LITUSDT HIDUP 6 dari 6 bulan 2026; batasan BTCSTUSDT 0 dari 53 tetap berlaku
  (aturan 60) · H-A012 MENANG · **H-A013 MENANG 6–0, TAFSIR DICABUT**.
- **H-A014 [BELUM DIUJI, WAJIB DITULIS ULANG v39].** Bentuk lama: "apakah bulan
  SETTLED adalah bulan tanpa perdagangan (MATI) di TENGAH hidup nama dasarnya"
  (13 kasus). **Bentuk baru yang kini lebih mungkin:** apakah bulan SETTLED adalah
  bulan yang **ABSEN** dari daftar bulan nama dasarnya. Bukti pendorong: sembilan
  nama berpasangan kehilangan tepat satu bulan dari rentangnya (lihat "Bulan
  absen"). Kedua bentuk wajib diuji berdampingan; penyebut 13 atau 9 → aturan 59;
  kendali positif (50); medan `definisi_dapat_dibedakan` (46).
- **H-A015 [v39] MENANG sebagai angka, DIBATASI sebagai tafsir.** Bunyi asal:
  bulan `…SETTLED` menandai batas antara dua kontrak pada nama dasar yang sama; ia
  jatuh pada atau tepat sebelum bulan berfunding pertama kontrak berikutnya.
  Terukur: benar pada **3 pasangan berkohort banyak**; **dibantah** pada 11
  pasangan bersatu-bulan, di mana bulan SETTLED jatuh jauh SESUDAH funding pertama.
  Warisi hanya dalam bentuk terbatas (aturan 20), dan ingat KC-38 tentang
  `MINAUSDT`.

## Papan skor prediksi

R-1..R-120 dirinci v23 · R-121..R-149 v26 dan jurnal 56–63 · R-150..R-193 jurnal
64–75 · R-194..R-199 jurnal 76–78 · R-200..R-235 seperti v37 · **R-236..R-247 di
jurnal 92–94** (rincian barisnya ADA DI SANA, belum disalin; R-239/R-240 MELESET
sebab KC-24, R-246 SEPARUH) · R-248..R-252 jurnal 95 · R-253..R-255 jurnal 96 ·
R-256 jurnal 97 · R-257..R-260 jurnal 98 · R-261..R-264 jurnal 99 · R-265..R-267
jurnal 101 · R-268 jurnal 102 · R-269..R-271 jurnal 103 · R-272..R-274 jurnal 104 ·
R-275..R-277 jurnal 105 · **R-279 jurnal 106** · **R-278 dan R-280 jurnal 107** ·
**R-281 jurnal 108** · **R-282 jurnal 109** · **R-283 jurnal 110** · **R-284 jurnal
111** · **R-285 jurnal 112** · **R-286 dan R-287 jurnal 113**.

| # | Prediksi | Status |
|---|---|---|
| R-199 | `definisi_dapat_dibedakan` false pada TEPAT 2 pecahan | **MENUNGGU** |
| R-275 | SETTLED hidup: bulan tutup DAN cacah_bulan ≤3 | **TEPAT** |
| R-276 | keenam nama peralihan ada di 28 terhenti | **MELESET** (0 dari 6) |
| R-277 | CI 630, kode 0, commit `e6b74855` | **TEPAT** |
| R-278 | 15 SETTLED: 13 dasar hidup, 2 terhenti (SXP, BDXN), ≥11 mendahului | **TEPAT** (13/2/0, mendahului 14) |
| R-279 | CI 630, kode 0, commit `8a0c4bff` (STATE v38) | **TEPAT** (MUDAH, run 30463521368) |
| R-280 | cacah uji 638 sesudah `test_terhenti` V4, kode 0 | **TEPAT** (MUDAH, run 30465456232) |
| R-281 | bulan SETTLED 36 **dan** 11 nama bersatu-bulan | **MELESET** (12, bukan 11 — aritmetika sendiri) |
| R-282 | `diagnosa_kc15.json` menyebut tiga bulan BNXUSDT | **MELESET** (hanya 2022-04; laporan TEPI) |
| R-283 | modul `diagnosa_kc15` mengukur tepi, bukan lubang tengah per nama | **TEPAT** (butir 2 lolos lewat disjungsi — mendekati MUDAH) |
| R-284 | `lubang_tengah.py` memuat tetapan tiga bulan BNXUSDT | **MELESET** (nama modul dibaca sebagai isi → aturan 73) |
| R-285 | 6 lubang tengah, 2 simbol (LIT 5 / BTCST 1), `h_a011_menang` **false** | **SEPARUH** (pembagian 5–1 TEPAT; H-A011 justru MENANG) |
| R-286 | H-A015: cocok 3..4 (wajib BNX/ICP/TLM); ≥10 dari 12 lebih awal; lubang >10 lawan <10 | **TEPAT** (4 cocok, 11 dari 12, 3/3 lawan 12/12) |
| R-287 | CI **662** butir, kode 0, commit `3d113d49` | **TEPAT** (MUDAH, run 30469781181) |

**Total R-1..R-287** (dihitung tangan, aturan 21). Dasar v38: TEPAT 196 · MELESET
51 · SEPARUH 16 · TIDAK TERADJUDIKASI 7 · MENUNGGU 7 = **277**. Sesudah v38: enam
TEPAT (R-278, R-279, R-280, R-283, R-286, R-287), tiga MELESET (R-281, R-282,
R-284), satu SEPARUH (R-285):

- TEPAT 196 + 6 = **202**
- MELESET 51 + 3 = **54**
- SEPARUH 16 + 1 = **17**
- TIDAK TERADJUDIKASI **7**
- MENUNGGU **7** (R-7, R-19, R-20, **R-28**, R-36, R-37, R-199)

202+54 = 256; +17 = 273; +7 = 280; +7 = **287** ✅ N_percobaan = 0; adjudikasi
riset TETAP TERKUNCI.

**Terpraregistrasi, belum teradjudikasi [v39]:**

- **R-288** (jurnal 113 §8) — identitas bulan ABSEN. (1) tepat **9** dari 15
  pasangan berbulan-absen satu, persis AERGO/AIA/CTK/CVC/CVX/LIT/MAVIA/PUMP/SLP;
  BNXUSDT 3; lima sisanya 0 — **MUDAH**. (2) bagi **≥7 dari 9**, bulan absen SAMA
  PERSIS dengan `bulan_settled_terakhir` — **BERISIKO**. (3) jumlah bulan absen
  atas SELURUH **787** nama penyebut = **12** — **BERISIKO BESAR**. GUGUR bila
  butir 2 salah (≤6 dari 9). Alat uji: modul baru yang MENGIMPOR
  `silang_funding.bulan_per_simbol`, tanpa jaringan.
- **R-289** (jurnal 113 §9) — pada commit BERIKUTNYA yang menyentuh `STATE.md`
  (yakni commit yang memuat berkas ini) dan begitu pula pada commit yang menyentuh
  `PROMPT_KELANJUTAN.md`: `ci.yml` MENYALA sementara `terhenti_semesta.yml`,
  `semesta_kuota.yml`, `ukur_baris.yml`, dan workflow `silang_settled` TIDAK, dan
  `reports/ci_terakhir.json` melaporkan **662** butir dengan `kode_keluar` **0**.
  **Ramalan MUDAH**, disebut begitu di muka. Ramalan berikutnya sesudah R-289
  adalah **R-290**.

**Utang papan skor:** rincian baris R-236..R-247 masih hanya di jurnal 92–94; dan
ramalan yang dipraregistrasi di dalam **docstring modul** (mis. R-229 TEPAT, R-230
MELESET di `lubang_tengah.py` V2) belum masuk papan skor — pemeriksaan R-224..R-235
wajib dijalankan lebih dulu agar tidak mengulang KC-32.

**Catatan kejujuran [v39].** Dari sepuluh ramalan sejak v38, empat kalah (R-281,
R-282, R-284, R-285) dan **hanya R-285 butir 3 yang benar-benar dikalahkan DATA**;
tiga lainnya dapat dicegah tanpa jaringan dan tanpa satu pun run — aritmetika
sendiri, nama laporan, nama modul. Dari enam yang menang, **empat MUDAH** (R-279,
R-280, R-287, dan R-283 yang lolos lewat disjungsi) dan hanya **R-278** serta
**R-286** yang berisiko; R-286 pun menang di butir 1 dengan bantuan kasus
bermekanisme lain (KC-38). Yang layak dicatat sebagai kemajuan bukan papan skornya
melainkan bahwa keempat kekalahan melahirkan aturan yang menutup lubangnya.

## Jumlah uji

**662 TERVERIFIKASI [v39]** — `reports/ci_terakhir.json` blob **`8504322b`**, run
**30469781181**, commit **`3d113d49`**, `kode_keluar` **0**, "662 tests collected in
0.45s", ref runner `32088010`. Sebelumnya **638** (blob `ca47d961`, run
30465456232, commit `6cc335e3`) dan **630** (blob `2d0dfa27`, run 30463521368,
commit `8a0c4bff`). Riwayat: 231 → … → 552 → 584 → 598 → 610 → 623 → 630 → 630 →
**638** → **662**.

`tests/test_terhenti.py`: V1 **5** → V2 **18** → V3 **25** → **V4 33** (630 + 8 =
638). **`tests/test_silang_settled.py` 24** butir (638 + 24 = **662**), tanpa satu
pun `parametrize`. Lainnya: `test_semesta_kuota` 58 · `test_lubang_tengah` 56 ·
`test_kebangkitan` 54 · `test_silang_funding` 49 · `test_penyebut_tahun` 44 ·
`test_semesta_silang` 32 · `test_bulan_settled` 26.

**Kendali negatif yang tercatat:** run 30462286751 atas commit `7b819787` berjalan
ketika `tests/test_terhenti.py` masih memuat kurung kurawal liar; run 30462427226
atas commit perbaikan `e6b74855` memberi 630 dan kode 0. Kedua commit ada di
riwayat (aturan 29).

## Utang verifikasi

1-5 dan 11 menunggu tahap juri/klasifikasi. 6-23, 25-28 LUNAS. **Nomor utang ini
BUKAN nomor ramalan — lihat KC-32.**

24. **AKTIF.** LUNAS seperti tercatat v38, ditambah **LUNAS BARU [v39]:**
    `reports/bulan_settled.json` dibaca UTUH · `reports/diagnosa_kc15.json` dibaca
    UTUH · `reports/lubang_tengah.json` V2 dibaca UTUH · `reports/silang_settled.json`
    dibaca UTUH · `lux_ai/serapan/lubang_tengah.py` dan `silang_settled.py` dibaca
    UTUH · `terhenti.py` V4 dan ujinya dibaca UTUH · **pemasangan 15 nama SETTLED
    dengan nama dasarnya** · **identitas empat nama dasar baru** (AERGO, AIA, MINA,
    PUMP) · **anatomi BNXUSDT 2022-04** · **pembedaan `bulan_didaftar` lawan lolos
    gerbang** · **880 lawan 877 dibedakan** · **pemilik keenam lubang tengah** ·
    **kebangkitan LITUSDT terukur** · **kecocokan funding–SETTLED atas 15
    pasangan** · **selisih 12 punya calon identitas bernama**.
    **BELUM:** anatomi **BTCSTUSDT 2022-01** · irisan 880 lawan 877 · pembagian 5
    hari KC-15 ke tiga bulan BNXUSDT · tanggal hari yang hilang di BNXUSDT 2022-04
    · selisih 40 − 38 sampel `diagnosa_kc15` · `ukur_baris` V6 (KC-26 + dua belas
    berkas) · pemecahan/peninjauan `funding.py` dan `silang_funding.py` (705) ·
    daftar 147 nama hanya-arsip · identitas 18 simbol tanpa bulan HIDUP ·
    kehidupan 12 simbol-bulan karantina · `funding_ada` masih null di seluruh
    manifes · `dugaan_pengganti` (ADR-A005) · pemulihan harian ADR-A007 ·
    karantina artefak 7 hari · 28 anggota kohort di luar sampel abjad · **bunyi
    ramalan R-28 dari STATE v23 (KC-32)** · tiga nama ekor 2026-04 · keberadaan
    `POLUSDT` di 787 · asal-usul hantu "16 non-ASCII" · listing ulang direktori
    workflow sesudah workflow `silang_settled` lahir · laporan yang belum pernah
    dibaca: `semesta_rentang.json` (110.662 B, **tak bersidik**),
    `ringkas_semesta.json`, `survei_semesta.json`, `survei_progres.json`,
    `rentang_kc6.json`, `semesta_kuota.json` penuh, `semesta_silang.json` penuh,
    `penyebut_tahun.json` penuh, `kohort_ekor.json`, `funding_semesta.json` penuh,
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
- ADR-A003 taksonomi rezim. BELUM ADA (nomor dicadangkan). Wajib memisahkan
  "kontrak berganti nama" dari "pasar hidup kembali", wajib memakai taksonomi
  INSTRUMEN kanonik (KC-29), wajib memuat aturan 68, dan **[v39] wajib memuat
  kebangkitan LITUSDT sebagai kasus terukur pertama beserta aturan 74**.
- ADR-A004 kebijakan KC-6. DITERIMA. ADR-A005 jenis instrumen tahap pertama.
  DITERIMA. ADR-A006 karantina + persistensi. DITERIMA, DITERAPKAN, TERVERIFIKASI
  DARI LUAR. **[v39] Penggugur ADR-A004 tetap tidak menyala:**
  `cacah_gerbang_lolos_padahal_tepi_terpotong` = 0 atas 37 bulan tengah.
- **ADR-A007 serapan hibrida. DIUSULKAN**, belum diterima; wajib memperhitungkan
  temuan `jumlah_baris` dan kendala R-146. **[v39] Bahan baru yang menguatkannya:**
  7.200 menit KC-15 UTUH di arsip HARIAN.
- **ADR-A008 akibat KC-18. Keputusan 1–6 DITERIMA [v28]**; Keputusan 5 bersemesta
  18.087. **Keputusan 7 BERCABANG DUA, dan kedua cabangnya kini bernama [v39]:**
  **LITUSDT** (lubang tengah berentetan **5**, MATI seluruhnya, lalu **BANGKIT**
  terukur) lawan **BTCSTUSDT** (lubang tengah **TUNGGAL** 2022-01, `cacah_lilin`
  44.640 PENUH, tetap MATI, 53 dari 53). Keputusannya WAJIB memuat kedua cabang,
  WAJIB per simbol-bulan, DILARANG menyebut funding dan perdagangan berhenti
  "serentak", WAJIB menyebut batas `perpetual_usdt`, WAJIB memakai aturan 66
  revisi, 67, 68, dan **74**, dan **DILARANG diambil sebelum BTCSTUSDT 2022-01
  dianatomi seperti BNXUSDT 2022-04**. R-276 mengikat: tak ada peralihan yang
  terbukti. R-278 mengikat: 13 / 2 / 0.
- ADR berikutnya **A009**.

## Temuan sampingan yang belum diukur

- **Anatomi BTCSTUSDT 2022-01** — pekerjaan teknis paling berharga yang tersisa.
- **Bulan MANA yang absen** pada kesembilan nama berpasangan (R-288), dan apakah
  absen itu berarti tak diterbitkan atau gagal gerbang.
- Tanggal hari yang hilang di BNXUSDT 2022-04 (1.440 menit) dan pembagian 5 hari
  KC-15 ke tiga bulan.
- Irisan 880 lawan 877; selisih 40 − 38 sampel `diagnosa_kc15`.
- Tiga nama ekor 2026-04; mengapa `SXPUSDT` berhenti 2026-05; apakah `POLUSDT` ada
  di 787; asal-usul hantu "16 non-ASCII".
- Daftar 147 nama hanya-arsip; 18 simbol tanpa bulan HIDUP; kehidupan 12
  simbol-bulan karantina.
- Apakah 50 kontrak delivery bertanggal pernah masuk perhitungan mana pun (44
  terhenti, 6 hidup).
- Mengapa penamaan SETTLED datang berombak pada 2023-02 dan 2025-07 (tiga nama
  masing-masing), dan mengapa 2025-07 juga bulan tebing funding dan kohort puncak.
- Sebab kebangkitan/peralihan kedelapan simbol (di luar jangkauan arsip).
- Saham, ETF, dan komoditas token masih terhitung `perpetual_usdt`
  (`AAPLUSDT:2026-05` terbukti ada dan lolos gerbang).
- `.decode("utf-8","replace")` di `klines` membungkam byte rusak.
- Apakah BUSD/USDC layak digabung dengan USDT (80 nama, 1.705 bulan; 38 dari 39
  USDC masih HIDUP).
- Sebab KC-14 (H-A004) tak dapat diuji; sebab KC-15 tidak diketahui.
- Selisih byte funding AGIXUSDT 531 lawan 529; `waktu_utc` runner berjalan lebih
  dulu daripada jam sesi; satuan stempel mikro lawan mili (`survei.satuan_stempel`).
- `tests/test_pulihkan.py` belum pernah dibaca ulang sesudah push.
