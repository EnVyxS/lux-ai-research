# STATE — versi 41

Diperbarui: 2026-07-30 (sesi 56, lanjutan). Aturan hanya BERTAMBAH; jangan menulis
ulang dari ingatan. v41 disusun di atas teks v40 yang dibaca langsung dari `main`
(blob **`86c68a664603c548c39132aaa4d47605f0c84f9b`**, dibaca **UTUH** sebelum satu
huruf pun ditulis), ditambah jurnal **116** (blob
**`1652d12b901f5afacf6ca21873e11f40ebf4fcbf`**, UTUH),
`lux_ai/serapan/karantina_semesta.py` V1 (blob
**`46e7c46be39545ed7a761838a6c95c3526ad25be`**, UTUH),
`tests/test_karantina_semesta.py` (blob
**`d535f6d99762f39acb98e1e4c52b00e2be7c2b3e`**, UTUH),
`lux_ai/serapan/gerbang_1m.py` (blob **`c8cc54c84a57173ef2e426c317d6ac50734e9b4a`**,
UTUH — pembacaan pertama sesi ini),
`reports/karantina_semesta_ringkas.json` (blob
**`a247ee3f7b7f4dc21d12321a64d22d0e84b1a76d`**, UTUH, ref runner **`d9e44119`**),
`reports/karantina_semesta_status.json` (blob **`e99d7225…`**), dan
`reports/ci_terakhir.json` blob **`7db592379db67c54918c9feeb5833918bc050014`**
(**722**).

**KOREKSI PAPAN SKOR YANG WAJIB DIBACA LEBIH DULU.** v40 mencatat total **290**.
Angka benar sekarang **294** (R-1..R-294, seluruhnya teradjudikasi atau menunggu).
**Erratum v40 yang dikoreksi di sini:** v40 menulis "tiga TEPAT" sesudah v39
padahal yang baru hanya **dua** (R-289, R-290); aritmetikanya sendiri benar
(202 + 2 = 204). Kalimat itu diganti di bagian papan skor v41.

Yang lahir sejak v40: **KC-40**; hipotesis baru **H-A016**; adjudikasi **R-291,
R-292, R-293, R-294**; modul `karantina_semesta` V1; pembacaan pertama
`gerbang_1m.py`; dan **pembagian 5 hari KC-15 ke tiga bulan BNXUSDT yang akhirnya
TERUKUR** — utang yang hidup sejak jurnal 109.

Berkas yang TIDAK dibaca ulang pada giliran ini dan karena itu tidak diubah
angkanya di sini: `lux_ai/serapan/lubang_tengah.py` (blob `4d3beaf1`),
`decisions/ADR-A002.md`, `ADR-A004.md`, `ADR-A006.md`, `ADR-A007.md`, `ADR-A008.md`,
`PETA_MODUL.md`, `lux_ai/semesta/taksonomi.py` (blob `b418c7ba`),
`.github/workflows/karantina_semesta.yml` (didorong, belum dibaca ulang).

Lima peristiwa terbesar sejak v40:

1. **Daftar `parquet_karantina` akhirnya DIBACA, dan R-291 MENANG.** Dua belas
   simbol-bulan, himpunannya sama persis dengan yang dipraregistrasi; ini
   kemenangan **BERISIKO** pertama sejak R-288 butir 2.
2. **Lima hari KC-15 TERBAGI:** BNXUSDT 2022-04 kehilangan 1.650 menit, 2022-06
   1.440, 2022-08 4.320; jumlah 7.410 − 210 menit tepi = **7.200** = 5 hari.
3. **Bulan karantina berlilin SEBAGIAN, bukan kosong** — `nisbah_lilin` 0,903
   sampai 0,990; dan kedua belas selisih menitnya habis dibagi **15** (H-A016).
4. **KC-40 dan pembacaan `gerbang_1m.py`:** medan `pelanggaran` memuat nama
   KLAUSA yang gagal, jadi `tanpa_menit_hilang` di dalamnya berarti menit MEMANG
   hilang. Membacanya harfiah membalik maknanya.
5. **CI 694 → 722**, terverifikasi pada ref runner.

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
    lewat `list_commits` dengan `path="reports/<berkas>.json"`. **[v41] Ditaati
    empat kali lagi**: R-292 pada ref `aabd2019` (run 30478069419); R-293 pada
    `936d7901` (run 30479093362); R-291 pada **`d9e44119`** (run 30479681799);
    R-294 pada **`e82919f5`** (run 30479681620). Total pemakaian tercatat:
    **delapan belas**. Perangkap ini menyala berulang: sesudah push, laporan di
    `main` sudah memuat commit run BERIKUTNYA.
46. Kode dilarang menyimpulkan dari penyebut nol; medan yang menyimpulkan wajib
    memeriksa lebih dulu apakah kasusnya mampu membedakan. Ditaati `terhenti`
    V2/V4, `silang_settled` V1, `bulan_absen` V1, dan **[v41]
    `karantina_semesta` V1** (`nisbah_lilin` dan `selisih_menit` bernilai **null**
    bila bulannya tak terbaca, bukan nol; `bulan_menit` mengembalikan 0 hanya
    sebagai penanda TAK TERUKUR dan itu disebut tersurat di docstringnya,
    aturan 74).
48. Berkas modul yang mendekati pagar 800 baris dipecah SEBELUM fungsi baru
    ditambahkan. Berlaku atas `funding.py` dan `silang_funding.py` (705 SERI).
    **RENCANANYA DITINJAU [v39], DIPERKUAT [v40, v41]:** preseden MENGIMPOR kini
    empat kali — `lubang_tengah.py`, `silang_settled.py`, `bulan_absen.py`, dan
    **`karantina_semesta.py`** (mengimpor `pulihkan` untuk `nama_manifes` dan
    `TOTAL_PECAHAN`) memakai fungsi modul lain tanpa menyalinnya, sehingga definisi
    tetap SATU (aturan 36). Pemecahan hanya boleh dijalankan bila ada alasan yang
    mengalahkan preseden ini.
50. Setiap pengukuran yang menyimpulkan dari KETIADAAN wajib memuat kendali
    positif. `terhenti` V2..V4 `kendali_sah` true; `silang_settled` V1 true;
    `bulan_absen` V1 true; **[v41] `karantina_semesta` V1 true** — BTCUSDT dan
    ETHUSDT masing-masing **0** kemunculan di daftar karantina, sesuai dengan 78
    bulan lolos tanpa absen yang diukur `bulan_absen`.
52. Laporan yang tidak dapat dibaca utuh setara dengan laporan yang tidak ada.
    Ekor SETIAP berkas kode dan berkas panjang yang didorong wajib dibaca sesudah
    push. **[v41] Ditaati atas jurnal 116, `karantina_semesta.py`,
    `tests/test_karantina_semesta.py`, `.github/workflows/bulan_absen.yml`
    (utang v40 LUNAS), dan STATE v40.** Yang tetap tak terbaca utuh:
    `reports/silang_funding.json` 183.963 B, `reports/bulan_absen.json` 249.992 B,
    dan **[v41] `reports/manifes_pecahan_2.json` 2.446.093 B (blob
    `c0be6ecf1204145f80eec34c4856a6c5363445a8`) yang DITOLAK alat baca agen** —
    ketiganya dianggap TIDAK ADA; yang berlaku adalah berkas ringkasnya atau
    modul yang membacanya di runner.
55. Sebelum meramalkan hasil workflow, baca `paths`/`paths-ignore` dan sebutkan
    workflow MANA yang menyala. `ci.yml` mengabaikan `journal/**`, `decisions/**`,
    `hipotesis/**`, `reports/**`. `ukur_baris.yml` hanya atas
    `lux_ai/serapan/ukur_baris.py`; `semesta_kuota.yml` hanya atas
    `lux_ai/serapan/semesta_kuota.py`; `terhenti_semesta.yml` hanya atas
    `lux_ai/semesta/terhenti.py` dan dirinya sendiri; `silang_settled.yml` hanya
    atas `lux_ai/serapan/silang_settled.py`; `bulan_absen.yml` hanya atas
    `lux_ai/serapan/bulan_absen.py` — **dan ia MENDEKLARASIKAN
    `workflow_dispatch`**. **[v41] KOREKSI BATASAN WARISAN:** bunyi "tidak ada
    `workflow_dispatch` di repo" TIDAK tepat; yang benar adalah **tidak ada alat
    di sisi agen untuk memicunya**. Satu-satunya cara menyalakan run tetap push ke
    berkas di dalam `paths`.
57. Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB ditulis
    BERNOMOR dan nomor terakhirnya dipakai sebagai cacahan. **TERBUKTI BEKERJA
    TUJUH BELAS DARI TUJUH BELAS [v41]:** 382, 396, 450, 494, 526, 552, 584, 598,
    610, 623, 630, 630, 638, 662, 662, 662, 694, **722**. Mekanismenya
    deterministik — itu sebab keberhasilannya, bukan kecakapan meramal, dan setiap
    kemenangannya wajib disebut **MUDAH**.
58. Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH dalam
    giliran yang sama DILARANG diramalkan dengan pita sempit. Pilih: (a) baca
    ulang utuh; (b) pita batas atas ≥1,8× batas bawah; (c) jangan meramal, ukur.
63. **[DIAMANDEMEN v37, DIPERKUAT v38]** Setiap klaim tentang kematian,
    kebangkitan, lubang funding, dan `bagian_mati` WAJIB menyebut batas
    semestanya secara tersurat: penyebut **787** simbol adalah `perpetual_usdt`,
    dan ia PERSIS seluruh perpetual USDT di arsip. Semesta arsip **937** simbol,
    **21.789** bulan; **150** hanya-arsip; **0** hanya-penyebut. Frasa lama
    "hampir seluruhnya BUSD/USDC" **DICABUT** (terukur 80 dari 147). Pada bulan
    tutup semesta **49 nama di luar penyebut masih terbit**. Penyebut 787
    terkonfirmasi dari arah ketiga oleh `bulan_absen` V1
    (`cacah_nama_penyebut` **787**, `selisih_nama_penyebut` **0**).
64. Ramalan tentang nilai EKSTREM wajib menyebut perlakuan atas SERI, dan medan
    yang menamai pemegang ekstrem wajib melaporkan SELURUH pemegangnya bila seri.
    Perbaikan wajib di `ukur_baris` **V6**; `semesta_kuota` sudah benar sejak V1.
65. Setiap daftar contoh WAJIB menyebut CARA pemilihannya, dan kalimat sifat
    tentang KESELURUHAN himpunan DILARANG disusun dari contoh yang bukan
    seluruhnya. Contoh yang benar: sampel `diagnosa_kc15` berlapis atas delapan
    pecahan. **[v41] Contoh ketiga:** dua belas baris `karantina_semesta` adalah
    SELURUH isi daftar karantina kedelapan manifes, dan modul melaporkan
    `daftar_terpotong` 0 untuk membuktikannya.
66. **[lahir salah lalu DIREVISI]** Setiap cacahan semesta wajib menyebut KELAS
    INSTRUMEN yang dicacah. **Sebelum menuduh sebuah batas tidak ada, berkas
    penyaringnya WAJIB dibaca lebih dulu.** Perluasan: sebelum menulis modul baru,
    LISTING direktori paket dan direktori workflow lebih dulu. **[v41] Ditaati
    lagi:** listing sebelum `karantina_semesta` mencatat `lux_ai/serapan/` **38**,
    `.github/workflows/` **32**, dan `tests/` **41**; sesudah push menjadi **39**,
    **33**, dan **42**.
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
    besaran yang sama.** Terbayar tiga kali: 36 kolom bulan tabel 15 pasangan =
    `bulan_settled.py` V1; 11 bulan absen + 1 tepi = 12 = 19.598 − 19.586; dan
    **[v41] `byte_parquet_karantina_semesta` 13.247.705 = angka KC-17 di
    `pecahan.py` VERSI 6 (`selisih_byte_tercatat` 0), serta `pecahan_tanpa_karantina`
    [2, 5] persis seperti tersurat di sana.** **Pengukuran yang tak dapat
    dicocokkan dengan pengukuran lain mana pun harus dianggap belum diuji.**
70. **[v39, jurnal 108, lahir dari R-281] Sebelum praregistrasi dikunci, setiap
    butir yang saling menentukan wajib dijumlahkan silang; praregistrasi yang tidak
    konsisten dengan dirinya sendiri adalah ramalan CACAT, dan kecacatannya milik
    peramal, bukan milik data.** Lihat KC-34.
71. **[v39, jurnal 109, lahir dari R-282] Sebelum mempraregistrasi ramalan atas
    laporan yang belum pernah dibaca, modul penghasilnya wajib dibaca lebih dulu.**
    Ramalan atas medan yang tidak pernah diukur laporan itu gugur otomatis dan
    tidak boleh dihitung sebagai kekalahan data. **[v41] Dipakai dengan benar dua
    kali:** `serap.py`, `pecahan.py`, `pulihkan.py`, `rilis.py` dibaca UTUH sebelum
    `karantina_semesta` ditulis, sehingga nama medan `daftar_karantina`,
    `parquet_karantina`, `cacah_karantina`, `daftar_terpotong` dikutip dari kode
    yang menulisnya; dan `gerbang_1m.py` dibaca sebelum arti `pelanggaran`
    ditafsirkan (KC-40).
72. **[v39, jurnal 110] Sebuah laporan hanya membuktikan apa yang benar-benar
    disampelnya.** Setiap adjudikasi wajib menyebut penyebut sampel laporan sebelum
    menyebut putusannya. **Turunan yang mengikat:** angka terbitan wajib disebut
    bersama penyebutnya — 880 lubang funding (seluruhnya) lawan 877 (di dalam
    19.586). **[v41] Ditaati oleh rancangan `karantina_semesta`:** `kode_keluar`
    sengaja TIDAK memeriksa `uji_r291`, `selisih_penyebut`, maupun
    `selisih_byte_tercatat` — ramalan yang kalah tidak boleh membatalkan laporannya
    sendiri (preseden `bulan_absen`, aturan 24).
73. **[v39, jurnal 111, lahir dari R-284] Dilarang mempraregistrasi ramalan atas
    ISI sebuah berkas yang belum pernah dibaca ketika satu-satunya dasar ramalan
    adalah NAMA berkas itu.** Bila sebuah berkas perlu diketahui, bacalah —
    pembacaan tidak butuh run, tidak butuh jaringan, dan tidak berbiaya.
    **[v41] Batasnya kini diketahui:** ada berkas yang TIDAK DAPAT dibaca agen
    (manifes pecahan 2,4 MB). Untuk berkas seperti itu, jalan sahnya adalah modul
    yang berjalan di runner, bukan dugaan dari nama.
74. **[v39, jurnal 112, lahir dari R-285] Setiap nol yang dipakai sebagai dasar
    ramalan wajib disebut bersama PENYEBUT dan DEFINISI ujinya.** Lihat KC-37.
    **[v41] Dipakai dengan benar:** nol `cacah_kunci_ganda`, nol `cacah_dibuang`,
    nol `cacah_ditambal`, dan nol kemunculan kendali BTCUSDT/ETHUSDT disebut
    bersama penyebutnya masing-masing (8 manifes, 12 baris).
75. **[v39, jurnal 113, lahir dari R-286] Setiap cacahan "cocok" wajib disertai
    medan pembeda MEKANISME, dan pita ramalan wajib menyebut mekanisme mana yang
    dihitung.** Lihat KC-38. Ditaati `bulan_absen` V1 lewat `pembeda_absen`
    (gagal_gerbang 11 lawan tak_diterbitkan_arsip 0).
76. **[v40, jurnal 115, lahir dari R-288] Setiap cacah "bulan yang hilang" wajib
    menyebut apakah penyebutnya RENTANG bulan LOLOS atau DAFTAR bulan DIDAFTAR
    arsip (`bulan_didaftar`), dan angka dari kedua penyebut itu DILARANG
    dijumlahkan atau dipertukarkan.** Kasus asalnya: BNXUSDT punya **3** bulan
    gagal gerbang tetapi hanya **2** bulan absen. **[v41] Penyebut KETIGA kini
    terukur dan wajib ikut dibedakan:** menit hilang dapat dihitung atas **rentang
    yang ADA di berkas** (`gerbang_1m.menit_hilang_dalam_rentang`) atau atas
    **panjang bulan KALENDER** (`karantina_semesta.selisih_menit`). Untuk BNXUSDT
    2022-04 keduanya berbeda tepat **210** menit — menit tepi peluncuran. Kedua
    angka benar; penyebutnya berbeda. Lihat KC-39 dan KC-40.

**Calon aturan 77 (DIUSULKAN, belum berlaku):** dua berkas laporan yang berblob
IDENTIK bukan dua pengukuran. Asalnya jurnal 115/116: `reports/bulan_absen.log`
dan `reports/bulan_absen_ringkas.json` berblob sama
(`e450d9f95e9bca0dc28a0e01c6aad6594c4fa3d6`) karena workflow men-`tee` stdout
modul. Belum dijadikan aturan bernomor karena baru satu kasus.

## Kelas cacat

KC-1 s.d. KC-12 seperti v19; KC-10 dan KC-11 DITUTUP. KC-13 keterwakilan sampel
(penangkal aturan 37). **KC-16 DITARIK — nomornya TETAP kosong selamanya.**
KC-17 DITUTUP. Teks penuh KC-14, KC-15, KC-19–KC-29 ada di v37 (blob `f520d5e2`);
yang wajib dibawa:

- **KC-14** — menit hilang NYATA di arsip 1m: **9** simbol-bulan, **6.375** menit
  (425×15). Sebab tak diketahui (H-A004 tak dapat diuji). Karantina (ADR-A006).
- **KC-15 [DIKOREKSI v39, DILENGKAPI v41]** — klines BULANAN kehilangan HARI UTC
  penuh: **3** simbol-bulan, semuanya BNXUSDT 2022 (**2022-04, 2022-06, 2022-08**),
  **7.200** menit = **5 hari UTC**. **Hari-hari itu UTUH di arsip HARIAN** —
  jurnal 109 §5.2 DICABUT. Yang benar-benar tak terjelaskan hanyalah **210 menit
  TEPI** pada 2022-04, konsisten dengan peluncuran pukul **03:30 UTC**
  (`stempel_pertama_ms` 1648783800000; berkas harian 2022-04-01 memuat 1.230 =
  1.440 − 210 baris; `menit_tepi_hadir` 0 dari 210). **[v41] PEMBAGIAN 5 HARI KE
  TIGA BULAN AKHIRNYA TERUKUR** (`karantina_semesta` V1, penyebut kalender):

  | bulan | baris | menit kalender | selisih | keterangan |
  |---|---:|---:|---:|---|
  | 2022-04 | 41.550 | 43.200 | **1.650** | 1.440 tengah + 210 tepi |
  | 2022-06 | 41.760 | 43.200 | **1.440** | 1 hari UTC |
  | 2022-08 | 40.320 | 44.640 | **4.320** | 3 hari UTC |

  1.650 + 1.440 + 4.320 = **7.410**; 7.410 − 210 = **7.200** = 5 × 1.440 ✅ Jadi
  lima hari itu terbagi **1 + 3 + 1**, dan 210 menit sisanya adalah TEPI, bukan
  celah. Dua modul berkode berbeda kini sepakat pada satu angka (aturan 69).
  Anatomi 2022-04 selebihnya tetap: `menit_hilang_di_tengah` **1.440**,
  `gerbang_lolos` **false**, `putusan` TEPI_TAK_TERJELASKAN, `checksum_bulanan`
  `14bd6937…`. 9 + 3 = **12** karantina; 6.375 + 7.200 = **13.575** menit;
  **516.135** baris. Kedua belas karantina **BERNAMA dan kini TERUKUR** — lihat
  bagian "Daftar karantina". **TANGGAL** hari-hari yang hilang masih belum diukur.
  Kebijakan ADR-A007 masih DIUSULKAN.
- **KC-18** — lilin datar lolos gerbang struktural; gerbang menilai BENTUK, bukan
  kehidupan. Semesta `perpetual_usdt` atas **19.586** simbol-bulan lolos: **1.401
  MATI** (7,153%), **98 SEPI** (0,500%), **18.087 HIDUP** (92,35%); 945 MATI di
  luar kohort puncak. Dari 1.401 MATI, **842** kehilangan funding dan **559**
  tetap berfunding. **Kematian dapat berbalik** — LITUSDT MATI 2025-02..2025-11
  lalu **HIDUP 2026-01..2026-06 terukur**. Kematian permanen tetap punya contoh
  telak: BTCSTUSDT 53 dari 53 MATI. **Kecocokan bulan membuktikan PENAMAAN
  kontrak, bukan perdagangan** — mengikat atas H-A013, H-A014, H-A015, H-A016, dan
  seluruh laporan `silang_settled`, `bulan_absen`, maupun `karantina_semesta`.
  ADR-A008 Keputusan 1–6 DITERIMA; Keputusan 7 DITANGGUHKAN.
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
  konsep** ("tengah", "lubang"). Penangkal aturan 73. `bulan_absen.py` menuliskan
  pembedaan itu tersurat: lubang funding dan lubang tengah ADA di penyebut, bulan
  ABSEN TIDAK ADA di penyebut.
- **KC-37 [v39] — memakai nol dari satu penyebut sebagai bukti ketiadaan gejala di
  penyebut lain.** Penangkal aturan 74.
- **KC-38 [v39] — mencacah "kecocokan" tanpa membedakan MEKANISMENYA.** Penangkal
  aturan 75.
- **KC-39 [v40, lahir dari R-288] — mencampur dua penyebut "bulan yang tidak ada di
  penyebut": bulan absen DI DALAM rentang lawan bulan gagal gerbang di TEPI
  riwayat.** Bulan tepi TIDAK dapat absen menurut definisi rentang. BNXUSDT **3**
  gagal gerbang lawan **2** absen. Kerabat KC-36 dan KC-35. Penangkal aturan 76.
- **KC-40 [v41, jurnal 116] — membaca daftar nama KLAUSA yang gagal sebagai
  pernyataan KEADAAN.** `gerbang_1m.KLAUSA` menamai klausa yang harus BENAR
  (`deret_tidak_kosong`, `tanpa_duplikat`, `tanpa_menit_hilang`, `jarak_60_detik`,
  `selaras_menit`, `satuan_milidetik`), sedangkan medan `pelanggaran` mendaftar
  klausa yang **GAGAL**. Maka `tanpa_menit_hilang` di dalam `pelanggaran` berarti
  menit MEMANG hilang — makna terbalik dari bunyi harfiahnya. Kerabat KC-30
  (nama kelas) dan KC-36 (homonim). **Penangkal: bila sebuah medan berisi daftar
  nama klausa yang gagal, nama-nama itu wajib dibaca sebagai negasi, dan anggota
  `pelanggaran` DILARANG dikutip sebagai pernyataan keadaan.**

## Semesta riset = `perpetual_usdt` = penyebut 787 — TERBUKTI TIGA ARAH

Sumber: `semesta_kuota.py` **V3**, commit `db4a192d`, run 30456422183, laporan
blob `8adae5ee` (UTUH), `sidik_kode` `ef0c4a24…`, `bukan_bukti` false.

- `cacah_perpetual_usdt` **787** = `cacah_penyebut_simbol` **787**
- `cacah_perpetual_usdt_luar_penyebut` **0**; `cacah_penyebut_bukan_perpetual_usdt`
  **0**; `cacah_penyebut_bukan_akhiran_usdt` **0**; `cacah_penyebut_luar_arsip`
  **0**; `penyebut_bagian_arsip` true.
- **Arah ketiga:** `bulan_absen` V1 menemukan `cacah_nama_penyebut` **787**
  (`selisih_nama_penyebut` 0) dan dari manifes `cacah_nama_didaftar` **787** —
  kode lain, bahan lain, angka sama (aturan 69).

Karena KEDUA arah nol, ini **kesamaan himpunan**, bukan himpunan bagian.

Batas yang wajib ikut disebut (`taksonomi.CATATAN_BATAS`): token **saham, ETF, dan
komoditas** (mis. `AAPLUSDT`, `XAUUSDT`) tak dapat dibedakan lewat bentuk nama,
jadi mereka **IKUT di dalam 787**. `AAPLUSDT:2026-05` terbukti nyata di dalam
sampel `diagnosa_kc15` dan bulannya lolos gerbang bersih.

### Taksonomi kanonik — sembilan kelas

Berkas `lux_ai/semesta/taksonomi.py` (blob `b418c7ba`, **belum dibaca ulang sejak
v37 — premis "beroperasi atas 937 nama arsip" tetap ASUMSI**). Urutan pemeriksaan
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

### Penguraian selisih 163 — identitas utuh, dan kini bernama serta TERUKUR

`bulan_usdt_bukan_settled` 19.749 · `bulan_arsip_milik_penyebut` **19.598** ·
`bulan_arsip_milik_hanya_arsip` **151** · `bulan_lolos_gerbang` 19.586 ·
`selisih_total` **163** · `selisih_dalam_penyebut` **12** ·
`selisih_dari_hanya_arsip` **151** · `identitas_utuh` true.
19.598 + 151 = 19.749 ✅ · 12 + 151 = 163 ✅ · 19.598 − 19.586 = **12** ✅

**151 bulan itu SELURUHNYA milik ketiga indeks.** Dan **[v41] angka 12 bukan lagi
aritmetika: kedua belasnya bernama DAN daftar karantinanya sudah dibaca** —
lihat bagian berikut.

## Daftar karantina — TERUKUR [v41, `karantina_semesta` V1]

Sumber: `lux_ai/serapan/karantina_semesta.py` V1 (blob **`46e7c46b`**, UTUH),
laporan `reports/karantina_semesta_ringkas.json` blob **`a247ee3f`** pada ref
runner **`d9e44119`** (run **30479681799**, commit `edea61f7`), dibaca UTUH;
`reports/karantina_semesta_status.json` blob `e99d7225` mencatat `kode_keluar`
**0**. `sidik_kode` `ad30150e…`, `versi_karantina_semesta` 1, `bukan_bukti` false.
Laporan penuh `reports/karantina_semesta.json` belum dibaca (isinya sama dengan
ringkas ditambah `berkas_sumber`).

**Mengapa modul ini harus ada:** `reports/manifes_pecahan_2.json` 2.446.093 byte
DITOLAK alat baca agen, sehingga daftar karantina tak mungkin dibaca langsung
(aturan 52, 73).

Penggugur SELURUHNYA aman (aturan 24): `cacah_manifes_dibaca` **8/8** ·
`manifes_hilang` [] · `cacah_kunci_ganda` **0** · `jumlah_selisih_cacah_daftar`
**0** · `cacah_daftar_terpotong` **0** · `jumlah_cacah_dibuang` **0** ·
`jumlah_cacah_ditambal` **0** · `jumlah_karantina_tak_terkemas` **0** ·
`selisih_ditulis_terdaftar` **0** · `sidik_seragam` true (satu sidik
`237ccf42…`) · `kendali_sah` true (BTCUSDT 0, ETHUSDT 0).

### Kedua belas simbol-bulan, dengan ukuran lilinnya

`cacah_karantina_semesta` **12** · `cacah_kunci_unik` **12** ·
`selisih_penyebut` **0** (12 = 19.598 − 19.586) ·
`byte_parquet_karantina_semesta` **13.247.705** (`selisih_byte_tercatat` **0**,
sama dengan KC-17) · `cacah_tanpa_parquet_karantina` **0** ·
`cacah_pecahan_berkarantina` **6** · `pecahan_tanpa_karantina` **[2, 5]** ·
`sebaran_pelanggaran` = {`jarak_60_detik` **12**, `tanpa_menit_hilang` **12**}.

| # | simbol | bulan | pecahan | baris | menit kalender | selisih | `nisbah_lilin` |
|---|---|---|---:|---:|---:|---:|---:|
| 1 | AERGOUSDT | 2025-04 | 0 | 42.540 | 43.200 | 660 | 0,984722 |
| 2 | AIAUSDT | 2026-01 | 7 | 43.965 | 44.640 | 675 | 0,984879 |
| 3 | BNXUSDT | 2022-04 | 6 | 41.550 | 43.200 | 1.650 | 0,961806 |
| 4 | BNXUSDT | 2022-06 | 6 | 41.760 | 43.200 | 1.440 | 0,966667 |
| 5 | BNXUSDT | 2022-08 | 6 | 40.320 | 44.640 | 4.320 | 0,903226 |
| 6 | CTKUSDT | 2025-04 | 3 | 42.585 | 43.200 | 615 | 0,985764 |
| 7 | CVCUSDT | 2025-05 | 0 | 44.130 | 44.640 | 510 | 0,988575 |
| 8 | CVXUSDT | 2025-07 | 1 | 43.950 | 44.640 | 690 | 0,984543 |
| 9 | LITUSDT | 2025-12 | 4 | 43.590 | 44.640 | 1.050 | 0,976478 |
| 10 | MAVIAUSDT | 2025-03 | 1 | 43.620 | 44.640 | 1.020 | 0,977151 |
| 11 | PUMPUSDT | 2025-07 | 1 | 44.190 | 44.640 | 450 | 0,989919 |
| 12 | SLPUSDT | 2025-07 | 0 | 43.935 | 44.640 | 705 | 0,984207 |

Sebaran per pecahan 3, 3, 0, 1, 1, 0, 3, 1 = **12** ✅ (aturan 21).

**Dua hal yang sekarang boleh ditulis tanpa peringatan:** himpunan ini SAMA PERSIS
dengan sebelas bulan ABSEN ditambah BNXUSDT 2022-04 di tepi (aturan 69, KC-39
tetap mengikat atas cara mencacahnya), dan **frasa "inilah kedua belas karantina"
kini SAH** — peringatan aturan 71/73 di v40 dicabut karena daftarnya sudah dibaca.

**Yang TETAP belum diukur:** kehidupan kedua belas bulan itu (status MATI/SEPI/
HIDUP tidak dapat ada, sebab mereka di luar penyebut 19.586), dan **TANGGAL**
hari-hari yang hilang.

### Bulan karantina berlilin SEBAGIAN — dan celahnya kelipatan 15 menit

`nisbah_lilin` = baris ÷ menit kalender. Terendah **0,903226** (BNX 2022-08),
tertinggi **0,989919** (PUMP 2025-07); tak satu pun mendekati nol. Jadi bulan yang
dikarantina gerbang 1m BUKAN bulan tanpa data, melainkan bulan yang hampir penuh.
Ini menjawab pertanyaan "apakah bulan peralihan kontrak berlilin sebagian" dengan
**ya**, dan tidak ada bilangan yang dipraregistrasi untuknya (jadi bukan
kemenangan ramalan).

Seluruh dua belas selisih menit habis dibagi **15**: 660, 675, 1.650, 1.440,
4.320, 615, 510, 690, 1.050, 1.020, 450, 705 → 44, 45, 110, 96, 288, 41, 34, 46,
70, 68, 30, 47. Dua belas dari dua belas. Ini melahirkan **H-A016**.

## Bulan ABSEN — TERUKUR atas seluruh 787 nama [v40, `bulan_absen` V1]

Sumber: `lux_ai/serapan/bulan_absen.py` V1 (blob **`10279d72`**, dibaca UTUH),
laporan `reports/bulan_absen_ringkas.json` blob **`e450d9f9`** pada ref runner
**`8b0e0182`** (run **30477142893**), dibaca UTUH. Laporan penuh
`reports/bulan_absen.json` **249.992 B** dengan `sidik_sumber` `d2fc3bfb…`
BELUM terbaca utuh dan karena itu dianggap TIDAK ADA (aturan 52). `sidik_kode`
**`0294eb3a…`**, `versi_bulan_absen` 1, `bukan_bukti` false. **[v41]
`reports/bulan_absen_status.json` (blob `d6ec6ca0`) dibaca:** `kode_keluar` **0**,
run 30477142893, commit `4fc818f0`, `waktu_utc` 2026-07-29T17:50:29Z — kode keluar
modul itu kini terverifikasi. **`reports/bulan_absen.log` berblob IDENTIK dengan
`bulan_absen_ringkas.json`** (`e450d9f9`) karena workflow men-`tee` stdout; itu
SATU pengukuran, bukan dua (calon aturan 77).

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
**[v41] Dan sekarang diketahui KLAUSA MANA yang gagal:** `jarak_60_detik` dan
`tanpa_menit_hilang` pada kedua belas baris — dua klausa yang sama pada semuanya
(baca sebagai negasi, KC-40).

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
  Docstring `silang_funding.py` menyimpan `BENTUK_TERBITAN_FUNDING` = {awal **48**,
  ekor 826, tengah 6} atas 880; 48+826+6 = **880** ✅ dan 45+826+6 = **877** ✅ —
  dua penyebut, dua bentuk, keduanya benar (aturan 72, 76). **Irisan 880 lawan 877
  tetap UTANG.** **[v41] Ketiga bulan BNXUSDT di luar penyebut kini bernama dan
  terukur: 2022-04, 2022-06, 2022-08 — persis ketiga baris karantina BNX.**
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

### LITUSDT — urutan peristiwa, kini lengkap dengan ukuran lilin [v41]

1. MATI **2025-02..2025-11** (10 bulan); kematian MENDAHULUI hilangnya funding.
2. Lubang funding bentuk TENGAH **2025-07..2025-11** (rentetan **5**); berfunding
   terakhir **2025-06**, kembali **2026-01**.
3. **Bulan 2025-12 ABSEN dari penyebut**, `pembeda_absen` **gagal_gerbang**: arsip
   menerbitkannya, gerbang 1m menolaknya. **[v41] Dan sekarang terukur berapa yang
   hilang: 43.590 dari 44.640 menit — kurang 1.050 menit (nisbah 0,976478).**
   Bulan itu hampir penuh, bukan kosong.
4. `LITUSDTSETTLED` bermuatan **2025-12**, bulan yang sama.
5. **HIDUP 2026-01..2026-06 dengan funding kembali** (`h_a011_menang` true,
   `h_a011_cacah_hidup` **6**). **H-A011 MENANG.**

Jadi bulan SETTLED LITUSDT bukan bulan MATI di sela hidup nama dasarnya — ia bulan
yang nama dasarnya **tidak punya sama sekali** di penyebut. Itu mengubah bentuk
H-A014 (lihat Hipotesis).

### BTCSTUSDT 2022-01 — satu-satunya lubang tengah yang benar-benar tak terjelaskan

`cacah_lilin` **44.640** (31 × 1.440, penuh), `byte_parquet` **399.757**, klines
terbit 2021-03..2026-06 (**64 bulan**, hanya **1** lubang funding), status
**MATI**. BTCSTUSDT TIDAK punya bulan absen — ia tidak ada di antara sepuluh nama
berabsen, **dan [v41] ia juga TIDAK ada di daftar karantina 12 baris**, jadi bulan
itu LOLOS gerbang dan tetap mati. Ada bulan berlilin PENUH yang lolos gerbang dan
tetap MATI. **Keputusan 7 ADR-A008 DILARANG diambil sebelum bulan itu dianatomi
seperti BNXUSDT 2022-04.**

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
   berkas yang tak diterbitkan. **Aturan 76 lahir tepat dari sini:** 51 didaftar −
   48 lolos = **3**, sedangkan rentang 50 − 48 = **2**. Dua penyebut, dua bilangan,
   keduanya benar. **[v41] Ketiganya kini terukur menit demi menit — lihat KC-15.**
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
Keenam bulan itu juga terbukti bulan ABSEN, dan **[v41] keenamnya ada di daftar
karantina dengan `nisbah_lilin` 0,976 sampai 0,986** — kelas gejalanya sama.

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

**BELUM DIUKUR [v41]:** `tests/test_lubang_tengah.py`, `taksonomi.py`,
`pecahan.py`, `semesta_kuota.py` V3 (24.987 B), `tests/test_semesta_kuota.py`,
`terhenti.py` **V4**, `tests/test_terhenti.py` **V4**, `survei.py`,
`ringkas_semesta.py`, `diagnosa_kc15.py` (16.268 B), `silang_settled.py`,
`tests/test_silang_settled.py`, `bulan_absen.py`, `tests/test_bulan_absen.py`,
**`karantina_semesta.py`**, **`tests/test_karantina_semesta.py`** — enam belas
berkas. Tidak diramalkan dengan pita sempit (aturan 58 pilihan c).

## Modul dan workflow yang tercatat

**`lux_ai/semesta/`:** `__init__.py` 273 B (`4c2d1f25`) · `taksonomi.py` 7.086 B
(`b418c7ba`) · `terhenti.py` V1 `3fa8f697`, V2 `8121739b`, V3 `7b819787`,
**V4 `aaceb023` pada commit `6cc335e3`**.

**`lux_ai/serapan/` — 39 berkas [v41, dari listing ref `a9ee214d` + push
`4fc818f0` + push `edea61f7`]:** `__init__.py` (`64d85584`) · `arsip.py`
(`0104958b`) · `bentuk_semesta.py` (`1f0feb30`) · `bulan_absen.py` (`10279d72`) ·
`bulan_settled.py` (`80e8d8bb`) · `diagnosa_kc14.py` (`5bd67d15`) · `kc14b`
(`bceada11`) · `kc14c` (`ab517db9`) · `diagnosa_kc15.py` (`3642e5b6`) ·
`diagnosa_kc6.py` (`0f699854`) · `funding.py` (`8d4b1f82`) · `funding_cdn.py`
(`fd624d00`) · **`gerbang_1m.py` (`c8cc54c8`, dibaca UTUH di v41)** ·
**`karantina_semesta.py` (`46e7c46b`)** · `kebangkitan.py` (`446321ee`) ·
`kehidupan.py` (`f49abb2b`) · `kehidupan_arsip.py` (`318a5cb1`) · `klines.py`
(`cc4d9287`) · `kohort_ekor.py` (`c9b63bbe`) · `kohort_ringkas.py` (`4ae62d5b`) ·
`lubang_tengah.py` (`4d3beaf1`) · `pecahan.py` (`f1b49f1b`) · `penyebut_kc6.py`
(`7f399244`) · `penyebut_tahun.py` (`265aad00`) · `probe.py` (`4581639f`) ·
`pulihkan.py` (`a9e6eab7`) · `rentang_kc6.py` (`631ec2f3`) · `resample.py`
(`66a4b177`) · `rilis.py` (`2e44530c`) · `ringkas_semesta.py` (`bc8f7ad7`) ·
`semesta_kuota.py` (`7288b030`) · `semesta_silang.py` (`ad72f3f2`) · `serap.py`
(`62d4c2c3`) · `silang_funding.py` (`42c3aa9d`) · `silang_settled.py`
(`3eea2a80`) · `survei.py` (`26b14940`) · `uji_resample.py` (`f10ec98a`) ·
`ukur_baris.py` (`3ebaa9f9`).

**33 berkas di `.github/workflows/` [v41]** (blob): bentuk_semesta `dc393dd0` ·
bulan_settled `9e0829f2` · **bulan_absen `71f76a0f` (dibaca UTUH di v41;
`paths` hanya `lux_ai/serapan/bulan_absen.py`, meng-commit `bulan_absen.json`,
`bulan_absen_ringkas.json`, `bulan_absen.log`, `bulan_absen_status.json`, dan
MENDEKLARASIKAN `workflow_dispatch`)** · **ci `c79497b2`** · diagnosa_kc14
`6524646a` · kc14b `a315c25b` · kc14c `82126b60` · kc15 `c5f2ee0f` · kc6
`6bae2b1b` · funding_semesta `c1ce55f3` · **`karantina_semesta` (blob belum
dicatat — didorong pada `edea61f7`, belum dibaca ulang)** · kebangkitan `282b51aa`
· kehidupan `3eb10655` · kehidupan_arsip `8234e5dc` · kohort_ekor `2e747475` ·
lubang_tengah `557030de` · pecahan_serapan `cd9e21d1` · penyebut_kc6 `14617b6b` ·
penyebut_tahun `8f0d5852` · probe_serapan `9b356e15` · pulihkan_rilis `32bd1099` ·
rentang_kc6 `db1e77ae` · ringkas_semesta `d6145d28` · semesta_kuota `b7e5a65a` ·
semesta_silang `babf08e4` · serap_pilot `85694e0f` · silang_funding `23f8c870` ·
silang_settled `78d8051c` · survei_semesta `a1fb0192` · taksonomi_semesta
`b066b4db` · terhenti_semesta `baef4f41` · uji_resample `121f3e25` · ukur_baris
`f62be605`.

**`tests/` — 42 berkas [v41]**; sebelum push `karantina_semesta` terukur **41**
(listing dijalankan, aturan 66). Yang blobnya tercatat: `test_karantina_semesta.py`
(`d535f6d9`) · `test_bulan_absen.py` (`d4f2ee5a`) · `test_pulihkan.py`
(`11c43533`) · `test_rilis.py` (`be0aa219`) · `test_rilis_karantina.py`
(`739c8da9`) · `test_karantina_a006.py` (`a5a3d82f`) · `test_silang_funding.py`
(`92258b1d`) · `test_silang_settled.py` (`dae60732`) · `test_lubang_tengah.py`
(`b5417b27`) · `test_terhenti.py` (`1c4afa6f`) · `test_semesta_kuota.py`
(`170320ab`) · `test_kebangkitan.py` (`1fd006c5`) · `test_kohort_ekor.py`
(`ec9b5774`) · `test_penyebut_tahun.py` (`99e42567`) · `test_kehidupan_arsip.py`
(`470a2cd8`) · `test_gerbang_1m.py` (`a930af17`) · `test_serap.py` (`adde4013`) ·
`test_serapan.py` (`050a7e0a`) · `test_pecahan.py` (`b4e634c9`) ·
`test_taksonomi.py` (`2f73ec83`) · `test_arsip_kc9.py` (`3d8af70c`) ·
`test_kontinuitas.py` (`b377271f`) · `test_resample.py` (`f7c003d7`) ·
`test_ukur_baris.py` (`7975bf88`).

## API modul yang sudah terbaca dan boleh dipakai

Rincian v37 berlaku untuk `semesta_silang`, `arsip` (tanpa `requests`;
`fapi.binance.com` 451), `pecahan` (VERSI 6), `taksonomi`, `semesta_kuota` V3,
`penyebut_tahun`, `kebangkitan`; v38 untuk `survei`, `terhenti` V3,
`ringkas_semesta`, `rentang_kc6`; v39 untuk `silang_settled` V1, `diagnosa_kc15`,
`terhenti` V4; v40 untuk `silang_funding` V2 (blob `42c3aa9d`), `kehidupan_arsip`
V1 (blob `318a5cb1`), `bulan_absen` V1 (blob `10279d72`). Tambahan [v41]:

- **`pulihkan`** (blob `a9e6eab7`, UTUH): `VERSI` **2**, `TOTAL_PECAHAN` **8**,
  `AKAR_UNDUH` "data/unduh", `AKAR_PULIH` "data/pulih",
  `nama_manifes(i)` → `reports/manifes_pecahan_{i}.json`, `nama_status_serapan(i)`,
  `nama_keluaran(i)`, `nama_tag(i, run_id)`, `sidik_kode()`,
  `run_id_sumber(i, akar)`, `putuskan_definisi(selisih_utama, selisih_total,
  baris_karantina)`, `anggota_aman`, `cacah_baris_parquet`, `periksa_bagian`,
  `periksa_keluarga`, `jalankan(indeks, akar, dir_unduh, dir_pulih, hapus)`;
  tetapan `DEF_TAK_ADA_MANIFES`, `DEF_TAK_TERBEDAKAN`, `DEF_LOLOS_SAJA`,
  `DEF_LOLOS_PLUS_KARANTINA`, `DEF_TAK_COCOK`; env `PULIH_INDEKS`.
- **`rilis`** (blob `2e44530c`, UTUH): `BATAS_BAGIAN` 1_800_000_000, `BLOK_TAR` 512,
  `BLOK_PAX` 1024, `KEPALA_ANGGOTA` 1536, `BYTE_AKHIR_TAR` 1024, `REKAM_TAR` 10240,
  `MARGIN_REKAM` 20480, `NAMA_SUMS`, `NAMA_SUMS_KARANTINA`, `AKAR_RILIS`
  "data/rilis", `perkiraan_byte_anggota`, `bulatkan_rekam`, `taksir_bagian`,
  `rencana_belah`, `sha256_berkas`, `baris_sums`,
  `PengemasBerbelah(akar, nama_dasar, tujuan, batas, nama_sums)` dengan
  `tambah`/`tutup`/`laporan`, `verifikasi(akar, laporan)`. **Laporan pengemas hanya
  memuat bagian tar (`nama`, `jalur`, `byte`, `sha256`, `cacah_berkas`) — ia tahu
  BERAPA berkas karantina, TIDAK tahu SIAPA.**
- **`serap`** (blob `62d4c2c3`, UTUH): `SUMBER_RENTANG`
  "reports/semesta_rentang.json", `MANIFES` "reports/manifes_pilot.json",
  `AKAR_PARQUET` "data/parquet", `AKAR_KARANTINA` "data/parquet_karantina",
  `JENIS_DIIZINKAN` "perpetual_usdt", `BATAS_HEADER` "2022-01", `BATAS_BARU`
  "2025-01", `BATAS_HIDUP` "2026-05", `KELAS_RISIKO` (pra_header, non_ascii,
  terhenti, bulan_awal_2020_2021, kendali_baru), `BATAS_DAFTAR_KARANTINA` **500**,
  `nama_aman`, `non_ascii`, `pilih_berlapis`, `baris_karantina(manifes)`,
  `ringkas_karantina(manifes)` → `daftar_karantina` berisi {`simbol`, `bulan`,
  `pelanggaran`, `baris`, `parquet_karantina`, `checksum_zip_sha256`} plus
  `cacah_karantina`, `cacah_tak_terunduh`, `cacah_dibuang`, `cacah_ditambal`,
  `byte_parquet_karantina`, `daftar_terpotong`, `batas_daftar`;
  `serap_satu(simbol, bulan, akar, terhenti)`, `ringkas(manifes)`.
- **`gerbang_1m`** (blob `c8cc54c8`, UTUH): `MS_BAWAH` 1e12, `MS_ATAS` 1e14,
  `KLAUSA` = (`deret_tidak_kosong`, `tanpa_duplikat`, `tanpa_menit_hilang`,
  `jarak_60_detik`, `selaras_menit`, `satuan_milidetik`), `sidik_kode` (mencakup
  `resample.py`), `persen`, `satuan_stempel_dari_besaran`, `ukur_deret`,
  `nilai_klausa`, `nilai_deret`, `ringkas_gerbang`. **`menit_hilang_dalam_rentang`
  = slot dalam rentang − cap unik, dihitung atas rentang yang ADA di berkas dan
  sengaja BUKAN atas bulan kalender; rumusnya SALINAN sengaja dari
  `diagnosa_kc6.celah_menit` (aturan 10), dan `tests/test_gerbang_1m.py`
  membandingkan keduanya.** Medan `pelanggaran` = klausa yang GAGAL (KC-40).
- **`karantina_semesta` V1** (blob `46e7c46b`, UTUH): `VERSI` 1, `KELUARAN`
  `reports/karantina_semesta.json`, `KELUARAN_RINGKAS` `…_ringkas.json`,
  `R291_HIMPUNAN` (12 pasang), `R291_CACAH` 12, `PENYEBUT_SEMESTA` 19598,
  `PENYEBUT_LOLOS` 19586, `BYTE_KARANTINA_TERCATAT` 13247705, `KENDALI_NAMA`
  (BTCUSDT, ETHUSDT), `MENIT_PER_HARI` 1440. Fungsi: `sidik_kode` (mencakup
  `pulihkan.py`), `bulan_menit`, `kunci`, `entri_karantina` (blok `karantina`
  lalu kunci atas), `_medan`, `perkaya`, `baca_manifes`, `jalankan(akar, total)`,
  `kode_keluar`, `main`. **Ia MENGIMPOR `pulihkan` saja.** `kode_keluar` sengaja
  TIDAK memeriksa `uji_r291` (aturan 24, 72).

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
  bulan yang bukan bulan SETTLED-nya. Penyebutnya wajib disebut 9 dari 15.
  `definisi_dapat_dibedakan` masih harus dipasang bila diuji lagi (46).
- **H-A015 MENANG sebagai angka, DIBATASI sebagai tafsir; disokong mekanisme
  KEDUA.** Terukur benar pada **3 pasangan berkohort banyak** lewat funding, dan
  **9 dari 9 pasangan berabsen-satu** lewat gerbang klines. Tetap **dibantah**
  dalam bentuk KUAT pada 11 pasangan bersatu-bulan. Warisi hanya dalam bentuk
  terbatas (aturan 20); ingat KC-38 (`MINAUSDT`) dan KC-18 (penamaan, bukan
  perdagangan).
- **H-A016 [v41, LAHIR SEBAGAI PENGAMATAN, BELUM DIUJI] — celah menit di arsip 1m
  datang dalam blok kelipatan 15 menit.** Bahan: kedua belas `selisih_menit`
  bulan karantina habis dibagi 15 (12 dari 12, penyebut 12), dan KC-14 sudah
  mencatat 6.375 = 425 × 15 atas 9 simbol-bulan lain. **Belum diuji atas
  simbol-bulan yang LOLOS gerbang**, jadi DILARANG digeneralkan ke 19.586 (aturan
  20). Uji yang sah menuntut ukuran celah pada bulan yang lolos — dan karena
  gerbang menolak bulan bercelah, penyebutnya harus dipilih dengan hati-hati
  (kemungkinan besar hanya menit TEPI yang tersisa untuk diukur). Kendali positif
  wajib: BTCUSDT/ETHUSDT dengan selisih 0 tidak dapat membedakan apa pun
  (aturan 41, 46, 50).

## Papan skor prediksi

R-1..R-120 dirinci v23 · R-121..R-149 v26 dan jurnal 56–63 · R-150..R-193 jurnal
64–75 · R-194..R-199 jurnal 76–78 · R-200..R-235 seperti v37 · **R-236..R-247 di
jurnal 92–94** (rincian barisnya ADA DI SANA, belum disalin) · R-248..R-252 jurnal
95 · R-253..R-255 jurnal 96 · R-256 jurnal 97 · R-257..R-260 jurnal 98 ·
R-261..R-264 jurnal 99 · R-265..R-267 jurnal 101 · R-268 jurnal 102 ·
R-269..R-271 jurnal 103 · R-272..R-274 jurnal 104 · R-275..R-277 jurnal 105 ·
R-279 jurnal 106 · R-278 dan R-280 jurnal 107 · R-281 jurnal 108 · R-282 jurnal
109 · R-283 jurnal 110 · R-284 jurnal 111 · R-285 jurnal 112 · R-286 dan R-287
jurnal 113 · R-289 jurnal 114 · R-288 dan R-290 jurnal 115 · **R-291, R-292,
R-293, R-294 jurnal 116**.

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
| R-285 | 6 lubang tengah, LIT 5 / BTCST 1, `h_a011_menang` false | **SEPARUH** |
| R-286 | H-A015: cocok 3..4; ≥10 dari 12 lebih awal; lubang >10 lawan <10 | **TEPAT** (4, 11 dari 12) |
| R-287 | CI **662**, kode 0, commit `3d113d49` | **TEPAT** (MUDAH, run 30469781181) |
| R-289 | `ci.yml` menyala pada commit STATE **dan** commit PROMPT, 662, kode 0 | **TEPAT** pada KEDUA cabang (MUDAH) |
| R-288 | bulan ABSEN: (1) 9 tunggal + BNX **3** + lima nol; (2) ≥7 dari 9 sama dengan bulan SETTLED; (3) jumlah semesta **12** | **SEPARUH** — butir 2 **TEPAT 9 dari 9**; butir 1 MELESET (BNX **2**); butir 3 MELESET (**11**) |
| R-290 | CI **694**, kode 0, commit `4fc818f0` | **TEPAT** (MUDAH, run 30477143164) |
| R-291 | daftar `parquet_karantina` kedelapan manifes memuat **tepat 12** simbol-bulan, himpunannya sama persis dengan tabel karantina | **TEPAT — BERISIKO** (12/12, `diramalkan_hilang` [], `terukur_tak_diramalkan` [], run 30479681799) |
| R-292 | CI **694**, kode 0, commit `c07cb65f` | **TEPAT** (MUDAH, run 30478069419) |
| R-293 | CI **694**, kode 0, commit `91ce4660` | **TEPAT** (MUDAH, run 30479093362) |
| R-294 | CI **722**, kode 0, commit `edea61f7` | **TEPAT** (MUDAH, run 30479681620) |

**Total R-1..R-294** (dihitung tangan, aturan 21). Dasar v40: TEPAT 204 · MELESET
54 · SEPARUH 18 · TIDAK TERADJUDIKASI 7 · MENUNGGU 7 = **290**. Sesudah v40:
**empat TEPAT** (R-291, R-292, R-293, R-294) dan tidak ada MELESET maupun SEPARUH
baru. Rinciannya:

- TEPAT 204 + R-291 + R-292 + R-293 + R-294 = **208**
- MELESET **54** (tak berubah)
- SEPARUH **18** (tak berubah)
- TIDAK TERADJUDIKASI **7**
- MENUNGGU **7** (R-7, R-19, R-20, **R-28**, R-36, R-37, R-199)

208+54 = 262; +18 = 280; +7 = 287; +7 = **294** ✅ Nomor terpakai R-1..R-294,
seluruhnya teradjudikasi atau menunggu. N_percobaan = 0; adjudikasi riset TETAP
TERKUNCI. Ramalan berikutnya **R-295**. **Tidak ada ramalan yang menggantung —
slot CI bebas.**

**Utang papan skor:** rincian baris R-236..R-247 masih hanya di jurnal 92–94; dan
ramalan yang dipraregistrasi di dalam **docstring modul** (mis. R-229 TEPAT, R-230
MELESET di `lubang_tengah.py` V2) belum masuk papan — pemeriksaan R-224..R-235
wajib dijalankan lebih dulu agar tidak mengulang KC-32.

**Catatan kejujuran [v41].** Sejak v40 ada empat adjudikasi, semuanya TEPAT,
tetapi tiga di antaranya (R-292, R-293, R-294) hanyalah cacah butir uji dari
daftar bernomor — **MUDAH** dan deterministik, tidak menambah satu pun bukti bahwa
mutu ramalan membaik. Satu-satunya yang benar-benar berisiko adalah **R-291**, dan
ia menang bersih: himpunan dua belas nama-bulan yang disusun dari aritmetika
penyebut dan bulan ABSEN ternyata sama persis dengan daftar yang belum pernah
dibaca. Itu kemenangan berisiko KEDUA berturut sesudah R-288 butir 2, dan pola
lama tetap berlaku: **cabang yang saya sebut BERISIKO menang, cabang yang saya
sebut MUDAH-lah yang dulu kalah** (R-281, R-282, R-284, R-288 butir 1 dan 3 —
empat kelas cacat yang seluruhnya dapat dicegah tanpa jaringan dan tanpa satu pun
run). Yang layak dicatat sebagai kemajuan bukan papan skornya, melainkan bahwa
setiap kekalahan melahirkan aturan atau kelas cacat yang menutup lubangnya: 70,
71, 72, 73, 76, dan sekarang **KC-40**.

## Jumlah uji

**722 TERVERIFIKASI [v41]** — `reports/ci_terakhir.json` blob
**`7db592379db67c54918c9feeb5833918bc050014`**, run **30479681620**, commit
**`edea61f772abed1628a42b42710a60cd54ef2b3e`**, `kode_keluar` **0**, "722 tests
collected in 0.40s", ref runner **`e82919f5`**. Sebelumnya **694** tiga kali
(blob `2d853021` run 30477143164 commit `4fc818f0`; blob `4bac352c` run
30478069419 commit `c07cb65f`; blob `8027606f` run 30479093362 commit `91ce4660`),
**662** tiga kali (blob `8504322b`, `15d14123`, `18cae8e5`), **638** (blob
`ca47d961`), **630** (blob `2d0dfa27`). Riwayat: 231 → … → 610 → 623 → 630 → 630
→ 638 → 662 → 662 → 662 → 694 → 694 → 694 → **722**.

`tests/test_terhenti.py`: V1 **5** → V2 **18** → V3 **25** → **V4 33**.
`tests/test_silang_settled.py` **24** (638 + 24 = 662).
`tests/test_bulan_absen.py` **32** (662 + 32 = 694).
**`tests/test_karantina_semesta.py` 28** butir tanpa satu pun `parametrize`
(694 + 28 = **722**), daftar bernomor ada di docstringnya. Lainnya:
`test_semesta_kuota` 58 · `test_lubang_tengah` 56 · `test_kebangkitan` 54 ·
`test_silang_funding` 49 · `test_penyebut_tahun` 44 · `test_semesta_silang` 32 ·
`test_bulan_settled` 26.

**Kendali negatif yang tercatat:** run 30462286751 atas commit `7b819787` berjalan
ketika `tests/test_terhenti.py` masih memuat kurung kurawal liar; run 30462427226
atas commit perbaikan `e6b74855` memberi 630 dan kode 0.

## Utang verifikasi

1-5 dan 11 menunggu tahap juri/klasifikasi. 6-23, 25-28 LUNAS. **Nomor utang ini
BUKAN nomor ramalan — lihat KC-32.**

24. **AKTIF.** LUNAS seperti tercatat v40, ditambah **LUNAS BARU [v41]:**
    **daftar `parquet_karantina` DIBACA (R-291) beserta byte 13.247.705 dan
    pecahan tanpa karantina [2, 5]** · **pembagian 5 hari KC-15 ke tiga bulan
    BNXUSDT (1.650 / 1.440 / 4.320)** · **ukuran lilin kedua belas bulan karantina
    (`nisbah_lilin` 0,903–0,990)** · `gerbang_1m.py` dibaca UTUH (KC-40) ·
    `pulihkan.py`, `rilis.py`, `serap.py`, `pecahan.py` dibaca UTUH ·
    `.github/workflows/bulan_absen.yml` dibaca UTUH · `bulan_absen_status.json`
    dan `bulan_absen.log` dibaca · listing `tests/` (41 → 42) ·
    `karantina_semesta.py` dan ujinya dibaca UTUH sesudah push.
    **BELUM:** anatomi **BTCSTUSDT 2022-01** · irisan 880 lawan 877 · **TANGGAL**
    hari-hari yang hilang pada ketiga bulan BNXUSDT (kini cacahnya diketahui,
