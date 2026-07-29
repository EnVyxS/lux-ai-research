# STATE — versi 37

Diperbarui: 2026-07-29 (sesi 55, lanjutan kelima). Aturan hanya BERTAMBAH; jangan
menulis ulang dari ingatan. v37 disusun di atas teks v36 yang dibaca langsung dari
`main` (blob **`f09497092de107cc08065070eabd71901c70ec8d`**, dibaca **UTUH**
sebelum satu huruf pun ditulis), ditambah jurnal 96–101,
`lux_ai/serapan/semesta_silang.py` (blob `ad72f3f2`, dibaca UTUH),
`lux_ai/serapan/pecahan.py` (blob `f1b49f1b`, UTUH), `lux_ai/serapan/arsip.py`
(blob `0104958b`, UTUH), `lux_ai/serapan/gerbang_1m.py` (blob `c8cc54c8`, UTUH),
**`lux_ai/semesta/taksonomi.py` (blob `b418c7ba`, UTUH — berkas yang belum pernah
dibaca sampai jurnal 100)**, `reports/semesta_kuota_ringkas.json` V2 (blob
`15613b65`, UTUH) dan **V3 (blob `8adae5ee`, UTUH)**, serta
`reports/ci_terakhir.json` (blob `7fa81edb` 598, lalu **`f344b717` 610**).

Run yang dicocokkan commit-nya, semuanya kode 0: **30452311150** (`9d6ce310`, CI
552), **30452448908** (`709b4728`, CI 552), **30454633506** (`f5cebf04`,
`semesta_kuota` V1) dan **30454633453** (CI 584), **30455491987** (`3a3e85e1`,
V2) dan **30455491991** (CI 598), **30456422183** (`db4a192d`, V3) dan
**30456421973** (CI **610**).

Tiga peristiwa terbesar sejak v36:

1. **Semesta riset akhirnya tersurat DAN terbukti.** Penyebut **787** simbol
   bukan sekadar "pasangan berkuota USDT" melainkan **tepat himpunan seluruh nama
   bergolongan `perpetual_usdt`** menurut taksonomi kanonik. Dibuktikan DUA ARAH
   pada run 30456422183: `cacah_perpetual_usdt_luar_penyebut` **0** dan
   `cacah_penyebut_bukan_perpetual_usdt` **0**.
2. **Satu klaim v36 DICABUT.** "150 simbol hanya-arsip hampir seluruhnya
   BUSD/USDC" **SALAH**: hanya **80 dari 147** (54,4%). Klaim itu lahir dari 18
   contoh yang ternyata urut ABJAD. Dari sini lahir aturan 65 dan KC-27.
3. **Taksonomi kanonik ditemukan sudah ada sejak lama, dan saya menuduhnya tidak
   ada sebelum membacanya.** Aturan 66 lahir salah lalu DIREVISI dalam giliran
   yang sama; KC-29 dinamai untuk cacatnya sendiri.

## Aturan bernomor

Aturan 1–36 berlaku tanpa perubahan; teksnya ada di STATE v19 (blob
`e06c486e…`). Ringkas nomornya: 1 satu definisi R · 2 gerbang kandidat ·
3 adjudikasi terkunci · 4-5 modul warisan · 6 hanya arsip publik · 7 sidik wajib ·
8 ≤800 baris · 9 satu jalur eksekusi · 10 diagnostik `bukan_bukti` · 11 biaya
sejak hari pertama · 12 guard struktural · 13-14 tanpa jaringan · 15 kode repo
lain · 16 nama medan jujur · 17 data biaya hilang → keluar · 18 gerbang lolos
wajib bercacah · 19 Decimal · 20 rentang disampel · 21 hitung ulang · 22 cakupan
`sidik_kode` · 23 gerbang merah tak dilonggarkan · 24 medan penggugur ·
25 cakupan dipatok sebelum run · 26 ramalan mutlak butuh besaran · 27 pendamping
tak bersyarat · 28 bulan awal parsial · 29 amandemen tak menghapus · 30 penyebut
eksplisit · 31 `sidik_data` · 32 nama non-ASCII · 33 pemicu sempit · 34 dilarang
add borongan · 35 laporan tanpa sidik hanya petunjuk · 36 dua angka beda →
definisi berdampingan. **[v37] Aturan 16 dan 36 baru saja terbayar besar:** 16
lewat kategori sisa jujur `TAK_DIKENAL` yang mencegah 50 kontrak bertanggal
tercampur diam-diam, dan 36 sebagai penangkal KC-29.

37. **[v20]** Sampel yang dipakai menguji sebuah jalur wajib memuat sedikitnya
    satu kasus dari tiap kelas cacat yang diketahui relevan, dan laporan wajib
    menyebut kelas mana yang tersentuh dan mana yang tidak, walau cacahnya nol.
38. **[v21]** Cacah uji hanya sah dari `reports/ci_terakhir.json` (run id +
    commit + `kode_keluar`). Penjumlahan taksiran dilarang ditulis sebagai angka
    uji. Dilanggar pada R-148, R-211, R-217. **Ditaati pada R-198, R-200, R-204,
    R-205, R-208, R-215, R-220, R-221, R-226–R-228, R-231, R-232, R-250, R-253,
    R-256, R-260, R-264, dan R-267.** Laporan CI dapat TERTIMPA run berikutnya;
    bila demikian baca pada ref commit yang bersangkutan. **Cara menemukan ref:**
    `list_commits` dengan `path="reports/ci_terakhir.json"` mendaftar tiap commit
    runner beserta nomor run di pesannya. **[v37] Perangkap ini menyala DUA KALI
    lagi:** sesudah push V1 dan V2, pembacaan pertama laporan masih memuat commit
    run SEBELUMNYA dengan blob yang tampak wajar. Yang menyelamatkan bukan blob
    melainkan `list_commits`: selama belum ada commit runner baru, laporan yang
    terbaca BUKAN hasil push terakhir.
39. **[v22]** Keseragaman terukur pada sampel DILARANG dipakai sebagai angka
    ramalan bagi anggota di luar sampel; wajib pita atau kemungkinan campuran.
40. **[v22]** Tiap laporan yang mencacah baris sebuah simbol-bulan wajib memuat
    uji silang `baris + hilang_di_tengah + tepi = menit_kalender`.
41. **[v23]** Ramalan bersyarat berpenyebut nol dicatat TIDAK TERADJUDIKASI.
42. **[v23]** Kelas cacat baru DILARANG dinamai atas dasar satu angka yang belum
    diukur langsung. **Ditaati pada KC-18, KC-21–KC-29.**
43. **[v24]** Medan penggugur bertoleransi BERSKALA, bukan margin datar.
44. **[v24]** Ramalan wajib menyebut penyebutnya: pecahan mana, semesta mana,
    medan mana. Pita yang hanya masuk akal di bawah satu tafsir → MELESET.
45. **[v25] Keatomikan push pemicu.** Push yang MENYALAKAN run wajib memuat setiap
    berkas yang run itu bergantung padanya. Ditaati pada `bdcbaebc`, `8466396f`,
    `d95c35a5`, `474fa23c`, `9bdab113`, `404e6f1b`, **`f5cebf04`**,
    **`3a3e85e1`**, dan **`db4a192d`**.
46. **[v26, LUNAS DI KODE v28] Kode dilarang menyimpulkan dari penyebut nol.**
    Medan yang MENYIMPULKAN wajib memeriksa lebih dulu apakah kasusnya mampu
    membedakan. Ditaati oleh `kohort_ekor` V4, `kehidupan`, `kehidupan_arsip`,
    `silang_funding`, `lubang_tengah`, `kebangkitan`, `penyebut_tahun`,
    `semesta_silang`, `bulan_settled` V1, dan **`semesta_kuota` V1–V3**
    (`pemegang_terbanyak.terukur`). **[v36] Aturan ini membuktikan nilainya ke
    arah yang tidak nyaman:** `bulan_settled` menang 6–0 tetapi melaporkan sendiri
    `definisi_dapat_dibedakan` **false**.
47. **[v27]** Sebutkan satuan cacah secara eksplisit — simbol, bulan,
    simbol-bulan, baris, atau butir uji — dan periksa angka rujukannya bersatuan
    itu.
48. **[v27]** Berkas modul yang mendekati pagar 800 baris harus dipecah SEBELUM
    fungsi baru ditambahkan. **Berlaku atas DUA berkas, keduanya 705 baris:**
    `funding.py` dan `silang_funding.py`. Tertinggi berikutnya
    `lubang_tengah.py` V2 **560**.
49. **[v27]** Pemecahan berkas yang mempertahankan nama fungsi lewat re-export
    TETAP dapat mematahkan uji. Telusuri nama yang DITAMBAL (`monkeypatch`,
    `patch`, akses atribut modul).
50. **[v27]** Setiap pengukuran yang menyimpulkan dari KETIADAAN wajib memuat
    kendali positif. **[v37] `semesta_kuota` V1–V3 bersih:** kendali BTCUSDT
    `cacah_bulan` **78** ≥ ambang **60**.
51. **[v27]** Jendela pemindaian mundur wajib adaptif atau dibuktikan mencakup
    peristiwa yang dicari.
52. **[v27]** Laporan yang tidak dapat dibaca utuh setara dengan laporan yang
    tidak ada. Ditaati oleh `kohort_ringkas`, `ukur_baris`, `kehidupan`,
    `kehidupan_arsip`, `silang_funding`, `lubang_tengah`, `kebangkitan`,
    `penyebut_tahun`, `semesta_silang`, `bulan_settled`, dan **`semesta_kuota`**
    (berkas ringkas memuat seluruh daftar yang wajib dibaca utuh, `baris` dan
    `nama_hanya_arsip` dibuang). Laporan `silang_funding` penuh 183.963 B tetap
    tak terbaca utuh selamanya.
53. **[v30]** Ramalan kode keluar sebuah run yang gerbangnya berkas uji wajib
    didahului pembacaan PERILAKU setiap fungsi yang diuji.
54. **[v31]** Cacah butir uji dihitung dengan mencacah `def test_` satu per satu
    pada berkas uji yang SUDAH selesai ditulis. TIDAK CUKUP sendiri — lihat 57.
55. **[v31]** Sebelum meramalkan hasil workflow, baca `paths`/`paths-ignore` dan
    sebutkan workflow MANA yang menyala. `ci.yml` mengabaikan `journal/**`,
    `decisions/**`, `hipotesis/**`, `reports/**`. `ukur_baris.yml` menyala HANYA
    atas `lux_ai/serapan/ukur_baris.py`; **`semesta_kuota.yml` HANYA atas
    `lux_ai/serapan/semesta_kuota.py`** — karena itu V3 menyala walau
    `taksonomi.py` tidak disentuh, dan menyunting `taksonomi.py` saja TIDAK akan
    menyalakannya.
56. **[v32]** Ramalan yang menyebut commit sasaran wajib memakai bentuk yang
    dijamin ada: "commit BERIKUTNYA yang menyentuh `<berkas>`".
57. **[v32]** Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB
    ditulis BERNOMOR, dan nomor terakhirnya dipakai sebagai cacahan. **TERBUKTI
    BEKERJA SEMBILAN DARI SEMBILAN [v37]:** R-221 (382), R-228 (396), R-232
    (450), R-241 (494), R-245 (526), R-250 (552), R-260 (584), R-264 (598), R-267
    (**610**). Mekanismenya deterministik — itu sebab keberhasilannya, bukan
    kecakapan meramal. **Fungsi yang hanya BERGANTI NAMA dihitung nol tambahan**
    (`test_versi_dua` → `test_versi_tiga`).
58. **[v33]** Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH
    dalam giliran yang sama DILARANG diramalkan dengan pita sempit. Pilih: (a)
    baca ulang utuh; (b) pita dengan batas atas ≥1,8× batas bawah; (c) jangan
    meramal, cukup ukur.
59. **[v34]** Ramalan yang menegaskan KETIADAAN gejala wajib menyebut penyebut
    yang mampu memuat gejala itu dan cacah kasus yang pernah diperiksa.
60. **[v35]** Tafsir MEKANISME yang menang pada satu kasus dilarang dipakai
    sebagai dasar ramalan atas kasus lain sebelum penyebutnya ≥2 dan variasinya
    terukur. Lahir dari R-234 (LITUSDT → BTCSTUSDT, 0 dari 53).
61. **[v35]** Nilai sebuah medan dilarang dipakai sebagai nilai medan jalur LAIN
    tanpa membaca laporan jalur itu. `funding_sebelum` bukan
    `bulan_hidup_terakhir`. Lihat KC-23.
62. **[v36, lahir dari R-239/R-240] Dua semesta yang berbeda DILARANG
    disilangkan tanpa bukti kesepadanan, dan laporan yang memuat CACAH tidak
    dapat menjawab pertanyaan tentang DAFTAR.** Penangkalnya: sebelum bertanya,
    periksa apakah laporan memuat DAFTAR yang diperlukan; bila hanya cacah, buat
    pengukur baru. Lihat KC-24. **[v37] Aturan ini terbayar penuh:** kesepadanan
    penyebut 787 dengan `perpetual_usdt` diuji dari KEDUA arah, dan hanya karena
    kedua arah nol ia sah disebut kesamaan himpunan, bukan himpunan bagian.
63. **[v36, DIAMANDEMEN v37] Setiap klaim tentang kematian, kebangkitan, lubang
    funding, dan `bagian_mati` WAJIB menyebut batas semestanya secara tersurat:
    penyebut 787 simbol adalah `perpetual_usdt` — pasangan berkuota USDT SAJA,
    dan sejak v37 diketahui pula bahwa ia PERSIS seluruh perpetual USDT di
    arsip.** Semesta arsip **937** simbol dan **21.789** bulan; **150** simbol
    hanya-arsip, **0** simbol hanya-penyebut. **AMANDEMEN [v37]:** frasa lama
    "hampir seluruhnya BUSD/USDC" **DICABUT** — terukur hanya **80 dari 147**
    nama bukan-akhiran-USDT (54,4%). Teks v36 tidak disunting (aturan 29), tetapi
    frasa itu DILARANG diwarisi. Berlaku juga di ADR. Lihat KC-25 dan KC-27.
64. **[v36, lahir dari R-255] Ramalan tentang nilai EKSTREM — terbesar,
    terkecil, terpanjang — wajib menyebut perlakuan atas SERI, dan medan
    laporan yang menamai pemegang ekstrem wajib melaporkan seluruh pemegangnya
    bila terjadi seri.** Lihat KC-26. **[v37] Ditaati sejak lahir oleh
    `semesta_kuota.pemegang_terbanyak`**, yang mengembalikan `pemegang` sebagai
    DAFTAR beserta `seri` dan `cacah_pemegang`; nilainya terbukti pada uji
    sintetis BUSD/USDC seri 7–7.
65. **[v37, lahir dari R-258] Setiap daftar contoh WAJIB menyebut CARA
    pemilihannya — seluruhnya, dua puluh teratas, urut abjad, atau acak — dan
    kalimat sifat tentang KESELURUHAN himpunan DILARANG disusun dari contoh yang
    bukan seluruhnya.** Lahir dari kekalahan yang paling murah dihindari sepanjang
    riset ini: 18 contoh nama hanya-arsip di jurnal 94 adalah **awal daftar urut
    abjad**, sehingga penuh BUSD/USDC hanya karena huruf A dan B; dari situ saya
    menyimpulkan sifat 150 nama. Penangkal praktis: bila cara pemilihan tidak
    diketahui, daftar itu hanya boleh dipakai untuk membuktikan KEBERADAAN, tidak
    pernah untuk membuktikan PROPORSI. Lihat KC-27.
66. **[v37, lahir salah lalu DIREVISI dalam giliran yang sama] Setiap cacahan
    semesta wajib menyebut KELAS INSTRUMEN yang dicacah — perpetual, delivery
    bertanggal, indeks, sisa penyelesaian — dan STATE wajib memuat batas semesta
    yang sudah ditegakkan KODE.** Kelas yang tidak sepadan wajib dikeluarkan atau
    dilaporkan terpisah, dan seluruh klaim kematian serta kebangkitan berlaku bagi
    **perpetual berkuota USDT**.
    **Bentuk PERTAMA aturan ini keliru dan teksnya tidak disunting (aturan 29):**
    jurnal 99 menyatakan kebersihan penyebut dari kontrak bertanggal adalah
    "kebetulan yang menguntungkan, bukan hasil rancangan yang tertulis". Satu
    bacaan berkas membatalkannya — `pecahan.py` menyatakan "Semesta: 787 simbol
    `perpetual_usdt`" di baris pertama docstring-nya dan menyaring lewat
    `taksonomi.jenis_instrumen`. **Karena itu bagian tambahan aturan ini: sebelum
    menuduh sebuah batas tidak ada, berkas penyaringnya WAJIB dibaca lebih dulu;
    ketidaktahuan pembaca bukan cacat rancangan.** Yang benar-benar kurang adalah
    batas itu tertulis di kode tetapi tidak di STATE — dan v37 memperbaikinya.
    Lihat KC-28 dan KC-29.

## Kelas cacat

KC-1 s.d. KC-12 seperti pada v19. KC-10 dan KC-11 DITUTUP (v20). KC-13
(keterwakilan sampel) → penangkalnya aturan 37.

- **KC-14 [v21, dipersempit v22] — menit hilang NYATA di arsip 1m, hadir di
  KEDUA representasi.** **9** simbol-bulan, **6.375 menit** (425×15). Sebab tidak
  diketahui (H-A004, tak dapat diuji). Kebijakan: karantina (ADR-A006).
- **KC-15 [v22] — berkas klines BULANAN dapat kehilangan HARI UTC penuh yang
  datanya utuh di berkas HARIAN.** **3** simbol-bulan, semuanya BNXUSDT 2022,
  **7.200 menit = 5×1440**. Kebijakan: ADR-A007. Sebab masih tidak diketahui.
- 9 + 3 = **12** karantina; 6.375 + 7.200 = **13.575** menit ✅ Keduabelasnya
  memuat **516.135 baris**. **Kehidupan keduabelasnya BELUM diukur.**
- **KC-16 DITARIK [v23] — nomornya TETAP kosong selamanya.**
- **KC-17 [v24] — parquet karantina tidak dipersistenkan. DITUTUP [v25].**
- **KC-18 [v27] — lilin datar lolos gerbang struktural.** Arsip menerbitkan
  berkas klines 1m lengkap dan sah secara BENTUK untuk pasar yang tidak
  diperdagangkan: stempel waktu rapat, checksum cocok, namun `volume` dan `count`
  nol pada SELURUH lilin. Gerbang 1m menilai bentuk, bukan kehidupan.
  - Bentangan: jurnal 74 864.000 lilin/20 simbol-bulan; jurnal 77 169 dari 179;
    kohort puncak **456 dari 456**.
  - **SEMESTA (`perpetual_usdt` saja, aturan 63):** dari **19.586** simbol-bulan
    lolos gerbang — **1.401 MATI** (7,153%), **98 SEPI** (0,500%), **18.087
    HIDUP** (92,35%). **945** MATI di luar kohort puncak.
  - **BUKAN CACAT ARSIP FUNDING:** dari 1.401 MATI, **842** kehilangan funding,
    **559** tetap berfunding.
  - **KEMATIAN DAPAT BERBALIK.** LITUSDT MATI **2025-02..2025-11** (10 bulan)
    lalu HIDUP 2026-01..2026-06. Status kehidupan WAJIB per SIMBOL-BULAN.
  - **KEBANGKITAN PUNYA DELAPAN CONTOH — TAFSIRNYA DILEMAHKAN [v36]:** **dua
    bersambung** (ICPUSDT 2022-09, TLMUSDT 2023-03) dan **enam peralihan nama**
    (CTK, CVC, CVX, LIT, MAVIA, SLP). Kecocokan bulan saudara SETTLED
    membuktikan **PENAMAAN kontrak**, BUKAN perdagangan.
  - **KEMATIAN PERMANEN JUGA PUNYA CONTOH TELAK:** BTCSTUSDT **53 dari 53** bulan
    MATI SESUDAH funding-nya pulih pada 2022-02. Kembalinya funding BUKAN penanda
    kebangkitan.
  - **Kebijakan DIPUTUSKAN [v28] oleh ADR-A008** (Keputusan 1–6 DITERIMA):
    KC-18 bukan gerbang serapan; kehidupan per simbol-bulan; **SEPI** bila
    `bagian_volume_nol` ≥ 0,5 dan **MATI** bila `transaksi_total` = 0; penyebut
    berpasangan; backtest hanya pada simbol-bulan HIDUP; angka 839.842.134 tidak
    ditulis ulang. Keputusan 7 DITANGGUHKAN.
- **KC-19 [v32] — mencacah dari INGATAN atas berkas yang baru saya tulis
  sendiri.** R-148, R-211, R-217. Penangkalnya aturan 57. **TIDAK TERULANG
  SEMBILAN KALI [v37].**
- **KC-20 [v33] — taksiran cacah baris bias sistematis ke BAWAH.** R-175, R-179,
  R-203, R-225 — empat dari empat searah. Penangkalnya aturan 58. `lubang_tengah.py`
  V1 390 baris, V2 ternyata **560**.
- **KC-21 [v34] — menyimpulkan KETIADAAN gejala dari ketiadaan PENGUKURANNYA.**
  Lahir dari R-230. Penangkalnya aturan 59.
- **KC-22 [v35] — memindahkan MEKANISME dari kasus yang menang ke kasus lain.**
  Lahir dari R-234. Penangkalnya aturan 60. Cacat PENALARAN, bukan kode.
- **KC-23 [v35] — memindahkan MEDAN antarjalur.** `funding_sebelum` dipakai
  sebagai bulan hidup terakhir. Penangkalnya aturan 61. KC-23 memindahkan ANGKA,
  KC-22 memindahkan SEBAB.
- **KC-24 [v36] — mengajukan pertanyaan tentang DAFTAR kepada laporan yang hanya
  memuat CACAH, dan menyilangkan dua semesta tanpa bukti kesepadanan.** Akibat
  nyata: R-239 dan R-240 MELESET, H-A013 sempat berstatus TAK BERLAKU padahal
  belum diuji. Penangkalnya aturan 62.
- **KC-25 [v36, DIAMANDEMEN v37] — batas semesta yang tidak tersurat.** Seluruh
  angka kematian, kebangkitan, dan `bagian_mati` dihitung atas **787 simbol
  `perpetual_usdt`**, sementara arsip memuat **937** simbol dan **21.789** bulan.
  Menulis "semesta" tanpa menyebut batas itu membuat pembaca berikutnya —
  termasuk saya sendiri — memperluas klaimnya tanpa sadar. Penangkalnya aturan 63.
  **AMANDEMEN [v37]:** kalimat lama "selisih 150 simbol hanya-arsip hampir
  seluruhnya BUSD/USDC" DICABUT; angka sebenarnya 80 dari 147. KC-25 tentang
  KUOTA; KC-28 tentang JENIS KONTRAK; keduanya berbeda.
- **KC-26 [v36, lahir dari R-255] — medan yang menamai pemegang nilai EKSTREM
  membisu tentang SERI.** `ringkasan.berkas_terpanjang` pada `ukur_baris` V5
  menamai `funding.py` (705) padahal `silang_funding.py` juga **705**; pemenang
  ditentukan urutan daftar, bukan data. Penangkalnya aturan 64. Perbaikan wajib
  di `ukur_baris` **V6**; `semesta_kuota` sudah benar sejak V1.
- **KC-27 [v37, lahir dari R-258] — mengarakterisasi sebuah himpunan dari contoh
  yang terpilih secara BERURUT.** Delapan belas nama hanya-arsip yang dicatat di
  jurnal 94 adalah awal daftar urut ABJAD; seluruhnya BUSD/USDC hanya karena
  huruf A dan B. Dari situ lahir kalimat "hampir seluruhnya BUSD/USDC" yang masuk
  ke aturan 63, ke KC-25, dan ke STATE v36 — tiga tempat sekaligus — lalu terukur
  salah: **80 dari 147 (54,4%)**, dan pemegang terbanyak justru `TAK_DIKENAL`
  dengan 51 nama. Penangkalnya aturan 65. **Beda dengan KC-24:** KC-24 salah
  BERTANYA (meminta daftar dari laporan bercacah), KC-27 salah MENYIMPULKAN
  (membuat pernyataan proporsi dari daftar sebagian).
- **KC-28 [v37, DIBATASI dalam giliran yang sama] — mencampur KELAS INSTRUMEN di
  dalam satu cacahan semesta.** Semesta arsip **937** mencampur perpetual dengan
  **50 kontrak delivery bertanggal** (`BTCUSDT_210326`…`BTCUSDT_261225` 24 nama;
  `ETHUSDT_210326`…`ETHUSDT_261225` 24; `BTCBUSD_210129`, `BTCBUSD_210226`) dan
  **3 indeks**. Kematian kontrak kuartalan DIJADWALKAN sejak lahir dan tidak
  sepadan dengan delisting perpetual, sehingga mencampurnya akan mengencerkan
  setiap kadar kematian. **BATAS [v37]: KC-28 berlaku atas semesta ARSIP 937,
  BUKAN atas penyebut 787** — penyebut terbukti bersih dari kedua kelas itu, dan
  kebersihan itu **dirancang**, bukan kebetulan. Penangkalnya aturan 66.
- **KC-29 [v37] — taksonomi PARALEL: mengarang klasifikasi sendiri padahal
  taksonomi kanonik sudah ada di repo.** `semesta_kuota` V1 dan V2 memakai
  `kuota_dasar`/`KUOTA_URUT` buatan sendiri, sementara `lux_ai/semesta/taksonomi.py`
  sudah menggolongkan sembilan kelas dan sudah dipakai gerbang serapan lewat
  `pecahan.simbol_pecahan`. Akibatnya terukur: kategori sisa `TAK_DIKENAL` 51 nama
  yang saya perlakukan sebagai misteri ternyata **50 `futures_kedaluwarsa` + 1
  `perpetual_usd1`** (`BTCUSD1`, sebab `taksonomi.KUTIPAN` memuat `USD1`).
  Akibat kedua, lebih halus: sampai V2, `taksonomi.py` TIDAK ikut `sidik_kode`,
  sehingga mengubah taksonomi kanonik tidak akan mengubah sidik laporan mana pun
  — lubang aturan 22 yang tak pernah menyala karena tak pernah diuji. Penangkalnya
  aturan 36 yang sudah lama ada: pakai definisi apa adanya. **Tidak satu pun
  angka V1/V2 batal karena KC-29; yang rusak PENAMAAN dan TAFSIR, bukan
  cacahannya.** Penawarnya `semesta_kuota` V3, yang melaporkan kedua taksonomi
  berdampingan agar penyimpangannya terlihat, bukan tersembunyi.

## Semesta riset = `perpetual_usdt` = penyebut 787 — TERBUKTI DUA ARAH [v37]

Sumber: `lux_ai/serapan/semesta_kuota.py` **V3**, commit **`db4a192d`**, run
**30456422183**, laporan `reports/semesta_kuota_ringkas.json` blob **`8adae5ee`**
(dibaca UTUH), `sidik_kode` **`ef0c4a2429a713f2fd8769bfd8488fc6b4925816875d4e1aaf82623f6dfa7eaa`**,
`sidik_data` `6bb4ec0d…c10e`, `waktu_utc` 2026-07-29T13:31:55Z, `bukan_bukti`
false. `berkas_dicap`: `semesta/taksonomi.py`, `serapan/kehidupan_arsip.py`,
`serapan/semesta_kuota.py`, `serapan/semesta_silang.py`,
`serapan/silang_funding.py`.

- `cacah_perpetual_usdt` **787** = `cacah_penyebut_simbol` **787**
- `cacah_perpetual_usdt_luar_penyebut` **0**, daftarnya `[]`
- `cacah_penyebut_bukan_perpetual_usdt` **0**, daftarnya `[]`
- `cacah_penyebut_bukan_akhiran_usdt` **0**; `cacah_penyebut_luar_arsip` **0**;
  `penyebut_bagian_arsip` **true**

Karena KEDUA arah nol, ini **kesamaan himpunan**, bukan himpunan bagian: tidak ada
perpetual USDT yang arsip terbitkan lalu serapan lewatkan, dan tidak ada anggota
penyebut yang bukan perpetual USDT. **Inilah batas semesta riset, dan sejak v37 ia
tertulis di STATE, bukan hanya di kode.**

Batas yang wajib ikut disebut (`taksonomi.CATATAN_BATAS`): token **saham, ETF, dan
komoditas** (mis. `AAPLUSDT`, `XAUUSDT`) tidak dapat dibedakan dari perpetual koin
lewat bentuk nama, sehingga mereka **IKUT berada di dalam 787**. Memisahkannya
menuntut daftar instrumen dari bursa. Setiap kadar kematian yang ditafsirkan
sebagai sifat "pasar kripto" wajib menyebut batas ini.

### Taksonomi kanonik — sembilan kelas

Berkas: **`lux_ai/semesta/taksonomi.py`** (blob `b418c7ba`). Urutan pemeriksaan
MENGIKAT: pola ekspirasi `_\d{6}$` → akhiran `SETTLED` → daftar `INDEKS` → mata
uang kutipan `("USDT","USDC","BUSD","USD1","BTC")`, dengan `BTC` sebagai
`KUTIPAN_NON_FIAT`. Membalik urutan salah, sebab `BTCUSDT_210326` juga berakhiran
angka dan `ICPUSDT_SETTLED` juga memuat `USDT`.

**`INDEKS` = {`DEFIUSDT`, `BTCDOMUSDT`, `BLUEBIRDUSDT`} — daftar manual, tersurat
di kode.** Utang lama "daftar `INDEKS` hanya tiga nama, disusun manual" **LUNAS
[v37]**: ketiganya persis sama dengan tiga nama berkuota USDT di arsip yang tak
pernah masuk penyebut. Maka **790 nama berakhiran USDT = 787 perpetual + 3
indeks**, tanpa sisa.

| jenis kanonik | nama (arsip 937) | bulan | nama (hanya-arsip 150) | bulan |
|---|---:|---:|---:|---:|
| `perpetual_usdt` | **787** | **19.598** | **0** | 0 |
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
19.598+258+812+893+36+151+2+39 = **21.789** ✅ · hanya-arsip 50+41+39+15+3+1+1 =
**150** ✅ · 258+812+893+36+151+2+39 = **2.191** ✅ · 21.789 − 2.191 = **19.598** ✅

`tak_tergolong` **0** menutup satu kekhawatiran lama: seluruh 937 nama punya kelas
kanonik, termasuk keenam belas nama non-ASCII, sebab semuanya berakhiran `USDT`.

### Taksonomi LOKAL modul (kuota) — dipertahankan berdampingan

| kuota | nama (937) | bulan | SETTLED | nama (hanya-arsip) | bulan |
|---|---:|---:|---:|---:|---:|
| USDT | **805** | 19.785 | 15 | **18** | 187 |
| TAK_DIKENAL | 51 | 260 | 0 | 51 | 260 |
| BUSD | 41 | 812 | 0 | 41 | 812 |
| USDC | 39 | 893 | 0 | 39 | 893 |
| BTC | 1 | 39 | 0 | 1 | 39 |

`TAK_DIKENAL` 51 = 50 `futures_kedaluwarsa` + 1 `perpetual_usd1`; 258 + 2 = 260
bulan ✅ — itulah KC-29 dalam bentuk angka. `terbanyak_bukan_usdt`: medan
`cacah_nama`, nilai **51**, pemegang `["TAK_DIKENAL"]`, `seri` false, `terukur`
true.

**150 hanya-arsip = 147 bukan-akhiran-USDT + 3 berakhiran USDT** (ketiga indeks).
Dari 147 itu, BUSD+USDC = **80** (54,4%) — bukan "hampir seluruhnya" (KC-27).

### Penguraian selisih 163 — identitas utuh

`urai_selisih` pada V2 (`15613b65`) dan V3 (`8adae5ee`), keduanya sama:

| medan | nilai |
|---|---:|
| `bulan_usdt_bukan_settled` | 19.749 |
| `bulan_arsip_milik_penyebut` | **19.598** |
| `bulan_arsip_milik_hanya_arsip` | **151** |
| `bulan_lolos_gerbang` | 19.586 |
| `selisih_total` | **163** |
| `selisih_dalam_penyebut` | **12** |
| `selisih_dari_hanya_arsip` | **151** |
| `identitas_utuh` | true |

19.598 + 151 = 19.749 ✅ · 12 + 151 = 163 ✅ · 19.598 − 19.586 = **12** ✅

**151 bulan itu SELURUHNYA milik ketiga indeks** — `per_jenis.indeks.jumlah_bulan`
juga 151. Bukan campuran, bukan misteri.

**Peringatan yang wajib dibawa:** kesamaan angka **12** dengan 12 simbol-bulan
karantina (KC-14 9 + KC-15 3) **BUKAN bukti identitas himpunan**. Nama dan bulan
keduanya belum dicocokkan. Itu utang terbuka, bukan temuan.

**Koreksi terhadap jurnal 98 sendiri (teks jurnal 98 TIDAK disunting, aturan 29):**
jurnal 98 menuduh alasan R-249 "tidak cukup". Sebenarnya alasan itu — 12
simbol-bulan gagal gerbang, yakni karantina — **TEPAT PERSIS** bagi komponen
dalam-penyebut (19.598 − 19.586 = 12); yang terlewat adalah keberadaan tiga nama
berkuota USDT DI LUAR penyebut yang menyumbang 151. Jadi alasannya benar dan
lengkap bagi satu sumbangan, dan bisu tentang sumbangan lain.

## H-A013 — DIUJI dan MENANG 6–0 [v36]

Sumber: `lux_ai/serapan/bulan_settled.py` **V1** (blob
**`80e8d8bb25cdeff974ef99c5b0e590a87f9bc656`**, `VERSI` 1, `AMBANG_KENDALI` 60,
`SETTLED_TERCATAT` 15), didorong ATOMIK bersama uji dan workflow pada commit
**`9bdab113`** (aturan 45). Run **30448334739**, `kode_keluar` **0**, commit
dicocokkan (aturan 38). Laporan: `reports/bulan_settled_ringkas.json` blob
`df2d2bfa`, 14.413 B, **dibaca UTUH** (aturan 52), `sidik_kode`
`cf96025f…048c`, `sidik_data_silang` `00a95373…a4a1`, `waktu_utc`
2026-07-29T11:38:40Z, `bukan_bukti` false.

| simbol | bulan peralihan | saudara ditemukan | bulan saudara | cocok |
|---|---|---|---|---|
| CTKUSDT | 2025-04 | **CTKUSDTSETTLED** | 2025-04 | ✅ |
| CVCUSDT | 2025-05 | **CVCUSDTSETTLED** | 2025-05 | ✅ |
| CVXUSDT | 2025-07 | **CVXUSDTSETTLED** | 2025-07 | ✅ |
| LITUSDT | 2025-12 | **LITUSDTSETTLED** | 2025-12 | ✅ |
| MAVIAUSDT | 2025-03 | **MAVIAUSDTSETTLED** | 2025-03 | ✅ |
| SLPUSDT | 2025-07 | **SLPUSDTSETTLED** | 2025-07 | ✅ |

`cacah_peralihan` **6** · `cacah_terukur` **6** · `cacah_cocok_bulan` **6** ·
`ambang_menang` **4** · `menang` **true** · `terukur` **true** ·
`sebab_terpakai` hanya `["saudara_settled_memuat_bulan"]` ·
`definisi_dapat_dibedakan` **false**. Tiap saudara punya TEPAT SATU bulan.

**Kelemahan yang diakui terbuka.** Keenam baris jatuh ke satu jalur sebab, jadi
uji ini tidak pernah membedakan dua penjelasan bersaing di dalam sampelnya.
Kemenangannya atas ambang yang saya sendiri tetapkan (4 dari 6), bukan atas
alternatif. Sahih, tetapi sempit — dan laporan mengatakannya sendiri (aturan 46).

**DUA konvensi nama hidup berdampingan di arsip.** Enam saudara di atas TANPA
garis bawah; `ICPUSDT_SETTLED` DENGAN garis bawah; `TLMUSDTSETTLED` tanpa. R-246
SEPARUH karena catatan lama dan docstring `penyebut_tahun.py` menulis
`TLMUSDT_SETTLED`; teks itu TIDAK disunting (aturan 29) dan cukup tidak diwarisi.

**Pelemahan tafsir yang WAJIB dibawa ke mana pun.** "Delapan kebangkitan" diganti
"**dua bersambung dan enam peralihan nama**". Batasnya: (1) KC-18 — kecocokan
bulan membuktikan PENAMAAN kontrak, bukan perdagangan; (2) aturan 63 — seluruh
angka ini berlaku atas semesta `perpetual_usdt`; (3) aturan 62 — laporan ini
memuat DAFTAR bulan sehingga pertanyaan "bulan mana" sah, tetapi "berapa simbol
lain berperilaku sama di seluruh arsip" TIDAK sah dijawab darinya; (4) kedua kasus
bersambung tidak diuji ulang di run itu (aturan 59).

### Silang cacah 24 nama — 24 dari 24 cocok

`silang_cacah.cacah_nama` **24** · `cacah_cocok_cacah` **24** ·
`cacah_tak_ada_di_laporan_lama` **0** · `seluruhnya_cocok` **true**. Penggugur
bersih: `cacah_gagal_daftar` **0**, `cacah_settled_tercatat` **15**,
`jumlah_bulan_didaftar` **518**.

Cacah bulan ARSIP: BNXUSDT **51** · CTKUSDT 68 · CVCUSDT 68 · CVXUSDT 46 ·
ICPUSDT 62 · LITUSDT 65 · MAVIAUSDT 29 · SLPUSDT 33 · TLMUSDT 60 ·
ICPUSDT_SETTLED 9 · TLMUSDTSETTLED 9 · BNXUSDTSETTLED 6 · dan dua belas nama
SETTLED lain bercacah 1 (AERGO, AIA, BDXN, CTK, CVC, CVX, LIT, MAVIA, MINA, PUMP,
SLP, SXP). Cara pemilihan: **SELURUH 24 nama** (aturan 65). Total bulan SETTLED
9+9+6+12 = **36** ✅ — sama dengan `per_jenis.sisa_settled.jumlah_bulan`.

**Peringatan aturan 62/63:** BNXUSDT **51** di sini cacah bulan **ARSIP**,
sedangkan **48** pada H-A010 cacah bulan **PENYEBUT**. Dua semesta, dua angka.
Bahwa selisih 3 itu "persis" tiga lubang tengah BNXUSDT 2022-04/-06/-08 adalah
**dugaan**, bukan fakta terukur.

## Semesta arsip lawan semesta penyebut — TERUKUR [v36, diperkaya v37]

| besaran | nilai |
|---|---:|
| simbol penyebut (`perpetual_usdt`) | **787** |
| simbol arsip | **937** |
| hanya-arsip | **150** (= 147 bukan-akhiran-USDT + 3 indeks) |
| hanya-penyebut | **0** |
| bulan arsip | **21.789** |
| bulan hanya-arsip | **2.191** |
| bulan arsip milik penyebut | **19.598** |
| nama SETTLED di arsip | **15** |
| nama SETTLED di penyebut | **0** |

**Identitas ke-150 nama itu kini terbaca sebagian:** sebarannya per jenis dan per
kuota ada di tabel §"Semesta riset" di atas, ketiga nama USDT-nya bernama
(BLUEBIRDUSDT, BTCDOMUSDT, DEFIUSDT), dan **51 nama `TAK_DIKENAL` terdaftar
SELURUHNYA** di `reports/semesta_kuota_ringkas.json`. Yang masih belum terbaca:
daftar 147 nama bukan-akhiran-USDT satu per satu (`reports/semesta_kuota.json`
penuh, medan `nama_hanya_arsip` dan `nama_bukan_akhiran_usdt`).

## Penyebut simbol-bulan PER TAHUN — TERUKUR [v36]

Semesta `perpetual_usdt` saja (aturan 63). Sumber: `penyebut_tahun` V1.

| tahun | penyebut simbol-bulan | MATI | `bagian_mati` |
|---|---:|---:|---:|
| 2020 | 504 | 1 | 0,001984 |
| 2021 | 1.385 | 9 | 0,006498 |
| 2022 | 1.729 | 34 | 0,019665 |
| 2023 | 2.400 | 103 | 0,042917 |
| 2024 | 3.570 | 192 | 0,053782 |
| 2025 | 5.948 | 506 | 0,085071 |
| 2026 (6 bulan) | 4.050 | 556 | **0,137284** |

Pembilang: 1+9+34+103+192+506+556 = **1.401** ✅ Penyebut:
504+1.385+1.729+2.400+3.570+5.948+4.050 = **19.586** ✅ `bagian_mati` MENANJAK
monoton dari 0,20% (2020) ke **13,73%** (2026). Yang TETAP DILARANG: menyebut ini
laju kematian "pasar kripto"; ia laju atas `perpetual_usdt` di arsip futures, per
simbol-bulan yang lolos gerbang 1m, dan token saham/komoditas ikut di dalamnya.

`cacah_simbol_tanpa_hidup` **18** — identitas kedelapan belas simbol itu belum
dibaca (`reports/penyebut_tahun.json` penuh belum terbaca).

## Cacah baris terukur [v36] — `ukur_baris` V5

Sumber: `reports/ukur_baris.json` **V5** (blob `c8b988ff`, dibaca UTUH), commit
**`404e6f1b`**, run **30451749412**, kode 0. Penggugur bersih:
`cacah_berkas_hilang` **0**, `cacah_berkas_melebihi_pagar` **0**,
`cacah_berkas_ada` **21** dari 21. Definisi `len(teks.splitlines())`, sama dengan
pagar 800 di `tests/test_kontinuitas.py`.

| berkas | baris | byte |
| --- | ---: | ---: |
| `funding.py` | **705** | 28.121 |
| `silang_funding.py` V2 | **705** | 29.873 |
| `lubang_tengah.py` **V2** | **560** | 23.745 |
| `kohort_ekor.py` | 553 | 22.590 |
| `kebangkitan.py` V1 | **552** | 22.603 |
| `penyebut_tahun.py` V1 | **527** | 21.653 |
| `tests/test_kebangkitan.py` | **501** | 15.755 |
| `kehidupan_arsip.py` | 496 | 19.281 |
| `semesta_silang.py` V1 | **423** | 16.126 |
| `kehidupan.py` | 417 | 16.638 |
| `bulan_settled.py` V1 | **386** | 14.776 |
| `pulihkan.py` V2 | 383 | 14.839 |
| `tests/test_penyebut_tahun.py` | **369** | 11.596 |
| `ukur_baris.py` V5 | 352 | 17.442 |
| `tests/test_semesta_silang.py` | **253** | 7.879 |
| `tests/test_bulan_settled.py` | **240** | 7.612 |
| `gerbang_1m.py` | 184 | 6.775 |
| `funding_cdn.py` | 162 | 6.335 |
| `arsip.py` | 154 | 5.231 |
| `resample.py` | 127 | 4.356 |
| `kohort_ringkas.py` | 82 | 2.882 |

Total **8.131** baris ✅ Terbesar **705, SERI** — `funding.py` dan
`silang_funding.py`. **Aturan 48 berlaku atas KEDUANYA dan atas keduanya saja.**
`berkas_terpanjang` melaporkan `funding.py` semata karena urutan daftar — KC-26.

**Angka kedaluwarsa yang MATI:** `ukur_baris.py` 183/226/280 BATAL → **352**;
`silang_funding.py` 396 BATAL → 705; `pulihkan.py` 318 BATAL → 383;
`lubang_tengah.py` 390 hanya untuk V1 → **560**.

**BELUM DIUKUR:** `tests/test_lubang_tengah.py` (56 fungsi, 18.387 B),
`lux_ai/semesta/taksonomi.py`, `lux_ai/serapan/pecahan.py`,
`lux_ai/serapan/semesta_kuota.py` V3, `tests/test_semesta_kuota.py`, dan berkas
uji lain. Tidak diramalkan dengan pita sempit (aturan 58 pilihan c).

## API modul yang sudah terbaca dan boleh dipakai [v37]

Dicatat agar sesi berikutnya tidak perlu membaca ulang berkas besar:

- `semesta_silang`: `SUMBER_ARSIP` (= `reports/semesta_bulan_1m.json`),
  `MEDAN_ARSIP` = `"bulan_per_simbol"`, `TOTAL_PECAHAN`, `SUMBER_FUNDING`,
  `SIMBOL_TERCATAT` 787, `cacah_bulan_arsip(dok)`, `simbol_arsip`,
  `simbol_penyebut(status)`, `berakhiran_settled`, `daftar_settled`,
  `silang_semesta`, `settled_di_penyebut`, `saudara_arsip`, `uji_h_a013_arsip`,
  `rinci_bersambung_arsip`.
- `silang_funding`: **`baca_laporan_kehidupan(akar, total) -> (status, byte_parquet,
  meta)`** dengan `status: Dict[(simbol,bulan), str]` — inilah jalur sah menuju
  daftar penyebut; `lubang_funding`, `kendali_silang`, `kendali_sah`, `sidik_kode`.
- `arsip`: `S3`, `CDN`, `AKAR` = `"data/futures/um"`, `segmen` (percent-encode),
  `ambil` (backoff, gagal → lempar), `daftar_prefix`, `daftar_kunci`,
  `semesta_simbol` (**satu-satunya sumber daftar simbol yang sah** — daftar pair
  aktif akan memasukkan bias keselamatan-hidup), `bulan_tersedia`, `url_klines`,
  `url_funding`, `checksum_arsip`, `unduh_terverifikasi` (checksum tak cocok →
  dianggap TIDAK ADA), `simpan`. Tanpa `requests`; `fapi.binance.com` 451.
- `pecahan`: `VERSI` **6**, `TOTAL_PECAHAN` 8, `JENIS_DIIZINKAN` =
  `serap.JENIS_DIIZINKAN` (= `perpetual_usdt`), `simbol_pecahan` (round-robin
  `indeks % total` atas daftar urut ABJAD — potong blok akan menimpangkan umur,
  pelajaran KC-13), `kemas_diminta` (env `PECAHAN_KEMAS`), `sidik_kode` mencakup
  `pecahan/serap/arsip/klines/gerbang_1m/resample/rilis`, `nama_keluaran(i)`.
  Docstring-nya menyatakan tersurat: **"Semesta: 787 simbol `perpetual_usdt`,
  19.598 simbol-bulan"**.
- `taksonomi`: `SUMBER` = `reports/semesta_rentang.json`, `KELUARAN` =
  `reports/taksonomi_semesta.json`, `AKHIR_SEMESTA` = `"2026-06"`,
  `POLA_EKSPIRASI`, `KUTIPAN`, `KUTIPAN_NON_FIAT`, `INDEKS` (3 nama), `JENIS` (9),
  `CATATAN_BATAS`, `jenis_instrumen`, `non_ascii`, `ringkas`, `sidik_kode`.
- `semesta_kuota` V3: `jenis_nama` (delegasi), `ringkas_jenis` (melaporkan kelas
  bernilai nol), `per_jenis_himpunan`, `perpetual_usdt_luar_penyebut`,
  `penyebut_luar_jenis`, `urai_selisih`, `baca_penyebut`, `himpunan_hanya_arsip`,
  `pemegang_terbanyak` (DAFTAR + `seri`), `berkas_dicap_penuh`, `kode_keluar`.
- `penyebut_tahun`: `PERALIHAN`, `BERSAMBUNG`, `AKHIRAN_SETTLED`,
  `nama_settled(simbol)`, `AMBANG_MENANG`. `kehidupan_arsip`: `TOTAL_PECAHAN`,
  `nama_keluaran(i)`. `kebangkitan`: `PENYEBUT_TERCATAT`.

## Yang berlaku tanpa perubahan dari v35 dan v36

Seluruh bagian berikut TIDAK berubah dan angkanya tidak ditulis ulang dari
ingatan; rinciannya ada di STATE v35 (blob `6523b84f`) dan v36 (blob `f0949709`).

- **H-A012 MENANG [v35]** — 8 simbol dari 787 punya bulan MATI lalu HIDUP,
  kedelapannya `bangkit_penuh`, `cacah_bulan_antara` 0. Panjang rentetan MATI
  2, 2, 8, 10, 11, 13, 13, 29 = **88** bulan; 88 dari 1.401 bulan MATI terbukti
  berakhir, **1.313** sisanya belum terbukti berakhir. **[v36] tafsirnya
  dilemahkan** — lihat H-A013.
- **BTCSTUSDT** — 53 bulan, 53 MATI, 0 HIDUP, pemegang rekor **63** bulan MATI
  semesta; funding hilang 2022-01 lalu PULIH 2022-02.
- **Sebaran 1.401 MATI menurut simbol** — **133** simbol dari 787 (16,9%) punya
  ≥1 bulan MATI. Cara pemilihan daftar berikut: **DUA PULUH TERATAS** (aturan
  65): BTCSTUSDT 63 · SCUSDT 48 · FTTUSDT 43 · RAYUSDT 43 · CVCUSDT 29 ·
  STRAXUSDT 27 · DGBUSDT 26 · GLMRUSDT 25 · IDEXUSDT 25 · MDTUSDT 25 · RADUSDT
  25 · SNTUSDT 25 · STPTUSDT 25 · AGIXUSDT 24 · OCEANUSDT 24 · WAVESUSDT 24 ·
  BTSUSDT 21 · KLAYUSDT 20 · UNFIUSDT 20 · BLZUSDT 18.
- **Silang funding × kehidupan [v31]** — penyebut 19.586: MATI 559 berfunding +
  842 berlubang = 1.401; SEPI 96 + 2 = 98; HIDUP 18.054 + **33** = 18.087; jumlah
  18.709 + 877 = **19.586** ✅ 877 + 3 lubang tak dikenal = **880** ✅ Arah wajib
  dipisah: lubang → mati **96,0%** (842/877); mati → lubang **60,1%**
  (842/1.401). Lubang funding TIDAK sah dipakai sebagai penyaring kematian.
- **Bentuk lubang funding** — lokal atas 877 di dalam penyebut: awal **45** +
  ekor **826** + tengah **6** = 877 ✅; terbitan `funding.py` atas 880: awal 48 +
  826 + 6; selisih 3 = tiga lubang BNXUSDT di luar penyebut ✅
- **Keenam lubang funding TENGAH** — BTCSTUSDT 2022-01 dan LITUSDT
  2025-07..2025-11; keenamnya MATI dan berklines penuh secara bentuk. Medan
  `funding sebelum` adalah medan JALUR FUNDING, bukan bulan hidup terakhir
  (aturan 61, KC-23): LITUSDT sudah MATI sejak 2025-02, jadi **kematian
  MENDAHULUI hilangnya funding**.
- **H-A010 MENANG 5–0, definisi TEPAT** — QTUMUSDT 2020-02/2020-03 (1),
  ICPUSDT 2021-05/2022-09 (16), TLMUSDT 2021-07/2023-03 (20), BNXUSDT
  2022-05/2023-02 (9), JUPUSDT 2024-01/2024-02 (1); `funding_tanpa_klines` kosong
  pada kelimanya. BNXUSDT **48** bulan di PENYEBUT dengan 3 lubang tengah
  2022-04/-06/-08 yang bulannya TIDAK ADA.
- **33 HIDUP tanpa funding** — bentuk: awal 33, ekor 0, tengah 0. ICPUSDT 13 ·
  TLMUSDT 11 · BNXUSDT 7 · JUPUSDT 1 · QTUMUSDT 1 = **33** ✅
- **Kehidupan semesta terserap [v30]** — kedelapan pecahan `kehidupan_arsip` V1
  (`sidik_kode` `24b6bb26…c595`), penyebut penuh **19.586**, MATI 1.401, SEPI 98,
  HIDUP 18.087, tanpa MATI **18.185**, lilin penuh **839.325.999**, lilin mati
  61.168.123 (7,29%). `cacah_baris_cacat` **0** dari 839 juta baris. Kendali 24
  dari 24 HIDUP. `bagian_mati` per pecahan 0,0418..0,1314 — karena itu 7,153%
  DILARANG dipakai sebagai laju kematian simbol mana pun.
- **Kohort puncak 2025-07 [v29]** — 38 simbol, 456 simbol-bulan, MATI 456, HIDUP
  0; nol simbol-bulan layak backtest.
- **Serapan semesta `perpetual_usdt`** — run **30396803601**, commit `57a04f1e`,
  `versi_pecahan` 6. Simbol **787**, simbol-bulan **19.598**, baris
  **839.842.134**, slot 839.855.709, menit hilang **13.575**; gerbang lolos
  **19.586**, gagal **12**, `persen_lolos` **99,9388**. Zip 26.532.925.083 B;
  parquet 32.706.262.375 B; nisbah 1,2327; parquet karantina 13.247.705 B.
  Pemulihan run **30404071324** (commit `ab4e0774`): 29/29 aset hadir, 29/29 sha
  cocok. Penyebut ganda: PENUH **19.586**, TANPA MATI **18.185**, LAYAK BACKTEST
  **18.087**.
- **Funding semesta (`funding.py` V6)** — run **30412188715**, commit `ba37c5d5`.
  880 bulan klines tanpa funding; 87 funding tanpa klines; penyebut 19.598.
  Kohort puncak 2025-07 = 38 simbol/456 simbol-bulan = 51,8% dari 880. `uji_cdn`:
  10 kohort 404, 10 kendali 200 dengan checksum cocok.
- **`kohort_ekor` V4** — pindaian ADAPTIF, pagu 60 bulan tak tersentuh; sepuluh
  bulan hidup terakhir (AGIX 2024-06, ALPACA 2025-04, AMB 2025-02, BADGER
  2025-03, BAL 2025-03, BLZ 2024-12, BNX 2025-03, BOND 2024-11, COMBO 2025-03,
  DAR 2024-12; cara pemilihan: **urut ABJAD**, aturan 65) dikuatkan `kebangkitan`
  V1 dengan definisi berbeda: **10 dari 10 sama**. `bangkit_kembali` 0 pada
  laporan itu BUKAN bukti tidak ada kebangkitan
  (`cacah_simbol_bangkit_dapat_diuji` = 0). 28 anggota kohort di luar sampel abjad
  BELUM diperiksa. **ADR-A002 §10 tidak boleh diubah atas bukti kohort semata.**
- **Definisi `jumlah_baris`** — manifes = baris lolos gerbang **839.325.999** +
  baris karantina **516.135** = **839.842.134**.
  `reports/pulihkan_pecahan_<i>.json` di git masih HASIL V1; cocokkan
  `versi_pulihkan` dan `sidik_kode`.

## Hipotesis

- H-A001: belum diuji. H-A002b **GUGUR**. H-A003 MENANG pada 3, GUGUR pada 9.
  H-A004 **tidak dapat diuji** (`fapi.binance.com` → 451). H-A005 GUGUR pada
  rentang yang disampel. H-A006 MENANG pada enam run. H-A008 MENANG dua kali.
- **H-A009 GUGUR** — 559 simbol-bulan MATI tetap berfunding.
- **H-A010 MENANG 5–0**, definisi TEPAT.
- **H-A011 MENANG 6–0 pada LITUSDT, DIBATASI** — BTCSTUSDT memberi 0 HIDUP dari
  53 (aturan 60).
- **H-A012 MENANG** — 8 simbol dari 787, kedelapannya bangkit penuh.
- **H-A013 [v36] MENANG 6–0** — bulan peralihan kebangkitan SAMA dengan bulan
  saudara SETTLED-nya, ambang 4. `definisi_dapat_dibedakan` **false**: kemenangan
  sempit, satu jalur sebab. Statusnya sebelum itu **TAK BERLAKU** karena KC-24 —
  bukan kalah.
- **H-A014 [v36, BELUM DIUJI] — keenam peralihan nama adalah pergantian KONTRAK,
  bukan pergantian kehidupan pasar.** Bila benar, bulan saudara SETTLED itu MATI
  atau tidak diperdagangkan meski bentuk klines-nya sempurna. Uji tanpa unduhan:
  ukur kehidupan keenam bulan saudara SETTLED dari arsip yang sudah di-commit;
  penyebutnya 6 — kecil, jadi aturan 59 wajib ditaati dan hasilnya ditulis sebagai
  kemungkinan campuran. **[v37] Bahan tambahan:** kelima belas nama SETTLED
  bergolongan `sisa_settled` dengan **36** bulan seluruhnya, dan **0** di antaranya
  ada di penyebut — jadi uji ini memang harus menembus semesta arsip, bukan
  penyebut.

## Papan skor prediksi

R-1..R-120 dirinci v23. R-121..R-149 di v26 dan jurnal 56–63. R-150..R-193 di
jurnal 64–75. R-194..R-199 di jurnal 76–78. R-200..R-204 di jurnal 79–81.
R-205..R-208 di docstring `0929643c`/`dceb1009`. R-209 jurnal 82. R-210..R-211
docstring `1b0e8d8e`. R-212 jurnal 83. R-213..R-215 docstring `67ec2be4`. R-216
jurnal 84. R-217..R-219 docstring `b1816ddf`. R-220 jurnal 86. R-221..R-223
docstring `680d04b4`. R-224..R-226 docstring `85079ffd`. R-227 PROMPT v36. R-228..
R-230 docstring `be5cd877`. R-231 PROMPT v37. R-232..R-235 docstring `bdcbaebc`.
**R-236..R-247 dipraregistrasi dan diadjudikasi di jurnal 92, 93, dan 94** —
rincian barisnya ADA DI SANA dan belum disalin ke tabel ini; yang wajib dibawa:
**R-239 dan R-240 MELESET** (sebabnya KC-24) dan **R-246 SEPARUH**
(`TLMUSDTSETTLED`). R-248..R-252 docstring `bulan_settled.py` (`9bdab113`),
adjudikasi jurnal 95. R-253..R-255 docstring `ukur_baris.py` V5 (`404e6f1b`),
adjudikasi jurnal 96. R-256 STATE v36, adjudikasi jurnal 97. **R-257..R-260
docstring `semesta_kuota.py` V1 (`f5cebf04`), adjudikasi jurnal 98. R-261..R-264
docstring V2 (`3a3e85e1`), adjudikasi jurnal 99. R-265..R-267 dipraregistrasi di
jurnal 100, adjudikasi jurnal 101.**

| # | Prediksi | Status |
|---|---|---|
| R-199 | `definisi_dapat_dibedakan` false pada TEPAT 2 pecahan (2 dan 5) | **MENUNGGU** |
| R-248 | H-A013: 4..6 dari 6 bulan peralihan cocok | **TEPAT** (**6**) |
| R-249 | bulan USDT bukan-SETTLED di arsip > 19.586 | **TEPAT** (**19.749**) |
| R-250 | CI **552**, kode 0, commit `9bdab113` | **TEPAT** (`30448334675`) |
| R-251 | `cacah_cocok_cacah` 24 dari 24 | **TEPAT** |
| R-252 | kendali BTCUSDT ≥ 60 bulan | **TEPAT** (**78**) |
| R-253 | CI tetap **552**, kode 0, commit `ukur_baris` V5 | **TEPAT** (`30451749571`) |
| R-254 | `cacah_berkas_hilang` 0 DAN `melebihi_pagar` 0 atas 21 berkas | **TEPAT** |
| R-255 | berkas terpanjang = `silang_funding.py` | **SEPARUH** (705 **SERI**) |
| R-256 | CI **552**, kode 0, commit STATE v36 | **TEPAT** (`30452311150`) |
| R-257 | himpunan berakhiran-USDT = penyebut 787 | **MELESET** (**790**) |
| R-258 | 150 hanya-arsip hampir seluruhnya BUSD/USDC | **MELESET** (**80 dari 147**) |
| R-259 | kendali BTCUSDT sah pada `semesta_kuota` V1 | **TEPAT** (78) |
| R-260 | CI **584** butir, kode 0 | **TEPAT** (`30454633453`) |
| R-261 | penyebut bersih; hanya-arsip 150; nama USDT hanya-arsip **3** | **TEPAT** |
| R-262 | `per_kuota_hanya_arsip` 18/41/39/51/1 | **TEPAT** (MUDAH) |
| R-263 | sumbangan nama USDT hanya-arsip ≤ 60 bulan | **MELESET** (**151**; terbalik) |
| R-264 | CI **598** butir, kode 0 | **TEPAT** (`30455491991`) |
| R-265 | `per_jenis_hanya_arsip` kesembilan angka | **TEPAT** (50/15/3/41/39/1/1/0/0) |
| R-266 | `perpetual_usdt` 787 DAN luar penyebut 0 | **TEPAT** (dua arah nol) |
| R-267 | CI **610** butir, kode 0 | **TEPAT** (`30456421973`) |

**Total R-1..R-267** (dihitung tangan, aturan 21). Dasar v36: TEPAT 180 · MELESET
44 · SEPARUH 16 · TIDAK TERADJUDIKASI 7 · MENUNGGU 8 = **255**. Sesudah v36:
sepuluh TEPAT baru (R-256, R-259, R-260, R-261, R-262, R-264, R-265, R-266,
R-267) ditambah **R-249 yang pindah dari MENUNGGU ke TEPAT**, dan tiga MELESET
(R-257, R-258, R-263):

- TEPAT 180 + 9 + 1 = **190**
- MELESET 44 + 3 = **47**
- SEPARUH **16**
- TIDAK TERADJUDIKASI **7**
- MENUNGGU 8 − 1 = **7** (R-7, R-19, R-20, R-28, R-36, R-37, R-199)

190+47 = 237; +16 = 253; +7 = 260; +7 = **267** ✅ Ramalan berikutnya **R-268**.
N_percobaan = 0; adjudikasi riset TETAP TERKUNCI.

**Utang papan skor yang dinyatakan terbuka:** rincian baris R-236..R-247 masih
hanya ada di jurnal 92–94; agregatnya sudah masuk hitungan, barisnya belum
disalin. Menyalinnya menuntut ketiga jurnal itu dibaca ulang UTUH dalam satu
giliran.

**Catatan kejujuran.** Ramalan **MUDAH** di sesi 55: R-250, R-253, R-254, R-256,
R-259, R-260, R-262, R-264, R-267 — kesembilannya menyalin angka yang sudah
terverifikasi atau memakai mekanisme deterministik (aturan 57). Ramalan
**BERISIKO**: R-248 (bisa gugur pada ≤3), R-255 (SEPARUH — lupa SERI), R-257,
R-258, R-261, R-263, R-265, R-266. Empat di antaranya kalah, **dan kekalahan
itulah yang menghasilkan aturan 64, 65, 66 serta KC-26, KC-27, KC-28, KC-29.**
R-266 adalah satu-satunya kemenangan berisiko yang berdiri sendiri.

**R-268, dipraregistrasi di sini (aturan 26, 38, 55, 56).** Pada commit BERIKUTNYA
yang menyentuh `STATE.md` — yakni commit yang memuat berkas ini — `ci.yml`
MENYALA (berkas di akar, tidak tersentuh `paths-ignore`) sedangkan
`semesta_kuota.yml` dan `ukur_baris.yml` TIDAK, dan `reports/ci_terakhir.json`
akan melaporkan **610 butir** dengan `kode_keluar` **0**. Dasarnya: tidak ada
berkas uji maupun modul yang berubah, dan 610 sudah terverifikasi pada run
30456421973. **Ini ramalan MUDAH** dan disebut begitu di muka.

## Jumlah uji

**610 TERVERIFIKASI [v37]** — `reports/ci_terakhir.json` blob **`f344b717`**, run
**30456421973**, commit **`db4a192d`**, `kode_keluar` **0**, "610 tests collected
in 0.36s". Riwayat: 231 → 234 → 236 → 239 → 241 → 244 → 253 → 269 → 291 → 316 →
340 → 382 → 382 → 396 → 396 → 396 → 450 → 494 → 526 → 552 → **584** → **598** →
**610**.

`tests/test_semesta_kuota.py` menyumbang **58** butir dan tumbuh dalam tiga
langkah yang seluruhnya dicacah BERNOMOR sebelum push: 552 + **32** = 584 (V1);
584 + **14** = 598 (V2, fungsi 33..46); 598 + **12** = **610** (V3, fungsi
47..58, dengan `test_versi_dua` → `test_versi_tiga` dihitung nol tambahan).
Berkas uji lain: `tests/test_lubang_tengah.py` 56 · `tests/test_kebangkitan.py`
54 · `tests/test_silang_funding.py` 49 · `tests/test_penyebut_tahun.py` 44 ·
`tests/test_semesta_silang.py` 32 · `tests/test_bulan_settled.py` 26.

## Utang verifikasi

1-5 dan 11 menunggu tahap juri/klasifikasi. 6-23, 25-28 LUNAS.

24. **AKTIF.**
    - persistensi data lolos dan karantina: **LUNAS**;
    - pemulihan aset di luar runner: **LUNAS**;
    - perbaikan aturan 46 di `pulihkan.py`: **LUNAS DI KODE** (V2) — laporan
      pecahan di git masih hasil V1;
    - bentangan penuh KC-18 atas kohort dan atas SEMESTA: **LUNAS**;
    - penyebut kedua atas semesta: **LUNAS**;
    - daftar 33 HIDUP tanpa funding dan 3 lubang di luar penyebut: **LUNAS**;
    - nama keenam lubang TENGAH: **LUNAS**;
    - uji H-A010 dan `funding_tanpa_klines`: **LUNAS**;
    - status LITUSDT 2026 (H-A011): **LUNAS**;
    - status BTCSTUSDT 2022-02..2026-06: **LUNAS** — 53/53 MATI;
    - pindaian kebangkitan seluruh semesta (H-A012): **LUNAS** — 8 simbol;
    - sebaran 1.401 MATI menurut TAHUN dan SIMBOL: **LUNAS**;
    - pencocokan `bulan_hidup_terakhir` dengan `kohort_ekor`: **LUNAS** — 10/10;
    - penyebut simbol-bulan PER TAHUN: **LUNAS [v36]**;
    - semesta arsip lawan penyebut (937/787/150/0, 21.789 bulan): **LUNAS [v36]**;
    - keberadaan keenam bulan peralihan (H-A013): **LUNAS [v36]**;
    - cacah baris sembilan berkas dan empat berkas uji: **LUNAS [v36]**;
    - **kuota dan JENIS seluruh 937 nama arsip: LUNAS [v37]** — dua tabel di atas;
    - **identitas tiga nama USDT hanya-arsip: LUNAS [v37]** — ketiga `INDEKS`;
    - **daftar `INDEKS` tiga nama manual: LUNAS [v37]** — terbaca di
      `taksonomi.py`;
    - **penguraian selisih 163 = 12 + 151: LUNAS [v37]**, `identitas_utuh` true;
    - **kesepadanan penyebut 787 dengan `perpetual_usdt`, DUA ARAH: LUNAS [v37]**;
    - **daftar 51 nama `TAK_DIKENAL`, SELURUHNYA: LUNAS [v37]** — 50 kontrak
      bertanggal + `BTCUSD1`;
    - **pemecahan `silang_funding.py` (705) dan `funding.py` (705), aturan 48:
      BELUM** — keduanya terukur ulang, tidak ada lagi alasan menundanya;
    - **medan `berkas_terpanjang` yang membisu tentang SERI (KC-26): BELUM** —
      perbaikan wajib di `ukur_baris` V6, bersama cacah baris
      `taksonomi.py`/`pecahan.py`/`semesta_kuota.py` V3 dan berkas uji;
    - **daftar 147 nama hanya-arsip bukan-akhiran-USDT satu per satu: BELUM** —
      `reports/semesta_kuota.json` penuh belum terbaca;
    - **identitas 18 simbol tanpa bulan HIDUP: BELUM** —
      `reports/penyebut_tahun.json` penuh belum terbaca;
    - **kehidupan keenam bulan saudara SETTLED (H-A014): BELUM**;
    - **pencocokan selisih 12 dengan 12 simbol-bulan karantina: BELUM** —
      kesamaan angka BUKAN bukti identitas himpunan; periksa nama dan bulannya;
    - **apakah 50 kontrak bertanggal pernah masuk perhitungan mana pun: BELUM**;
    - cacat penulisan docstring R-225 ("tujuh fungsi" lalu sembilan nama):
      dicatat, TIDAK disunting; jumlah yang benar sembilan;
    - docstring `penyebut_tahun.py` menulis `TLMUSDT_SETTLED` (salah): dicatat,
      TIDAK disunting, tidak diwarisi;
    - pencocokan 3 lubang BNXUSDT dengan 12 simbol-bulan karantina: BELUM;
    - kehidupan 12 simbol-bulan karantina: BELUM (tar terpisah);
    - jalur **funding**: `funding_ada` masih null di seluruh manifes — BELUM;
    - medan `dugaan_pengganti` (ADR-A005) — BELUM;
    - pemulihan harian ADR-A007 — BELUM, bahan baku sudah ada;
    - karantina artefak 7 hari — BELUM;
    - 28 anggota kohort di luar sampel abjad — BELUM;
    - `reports/diagnosa_kc15.json` (42.916 B), `reports/kohort_ekor.json`
      (112.687 B), `reports/semesta_silang.json` penuh,
      `reports/funding_selisih_penuh.json`, `tests/test_pulihkan.py` — BELUM
      pernah dibaca.
    Mengadjudikasi R-7, R-19, R-20, R-28, R-36, R-37.

## Daftar ADR

- ADR-A001 aturan dasar. DITERIMA.
- ADR-A002 serapan. DITERIMA; §3 DIAMANDEMEN oleh ADR-A004 lalu ADR-A007; §9
  DIGANTI oleh ADR-A006 Keputusan 3. **§10 belum disentuh dan tetap tidak boleh
  disentuh:** ketiga bentuk lubang punya penjelasan calon yang TIDAK menuduh arsip
  funding cacat — pada BTCSTUSDT funding terus terbit sepanjang 53 bulan kematian.
  Bila §10 kelak disunting, ia WAJIB menyebut batas `perpetual_usdt` (aturan 63).
- ADR-A003 taksonomi rezim. BELUM ADA (nomor dicadangkan). Delapan kebangkitan
  menyentuh langsung nomor ini: rezim sebuah simbol tidak monoton dan dapat
  kembali — dan enam dari delapan ternyata peralihan KONTRAK, sehingga taksonomi
  rezim wajib memisahkan "kontrak berganti nama" dari "pasar hidup kembali".
  **[v37] Ia juga wajib memakai taksonomi INSTRUMEN kanonik yang sudah ada
  (`lux_ai/semesta/taksonomi.py`) alih-alih membuat yang baru — pelajaran KC-29.**
- ADR-A004 kebijakan KC-6. DITERIMA.
- ADR-A005 jenis instrumen tahap pertama. DITERIMA.
- ADR-A006 karantina + persistensi. DITERIMA, DITERAPKAN, TERVERIFIKASI DARI LUAR.
- **ADR-A007 serapan hibrida. DIUSULKAN**, belum diterima. Wajib memperhitungkan
  temuan `jumlah_baris` dan kendala R-146.
- **ADR-A008 akibat KC-18. DITERIMA [v28] untuk Keputusan 1–6**; Keputusan 2–4
  TERTERAP atas seluruh semesta; Keputusan 5 bersemesta **18.087**.
  **Keputusan 7: bahannya LENGKAP dan BERCABANG DUA** — bentuk TENGAH dapat
  menandai jeda yang berakhir (LITUSDT) ATAU penerbitan funding yang pulih tanpa
  perdagangan (BTCSTUSDT, 53/53 MATI). Keputusannya WAJIB memuat kedua cabang,
  WAJIB per simbol-bulan, DILARANG menyebut funding dan perdagangan berhenti
  "serentak", dan WAJIB menyebut batas `perpetual_usdt` serta membedakan peralihan
  kontrak dari kebangkitan pasar (aturan 66 bentuk revisi).
- ADR berikutnya **A009**.

## Temuan sampingan yang belum diukur

- **Kehidupan keenam bulan saudara SETTLED (H-A014)** — pertanyaan paling murah
  yang tersisa; bahannya sudah di-commit.
- **Daftar 147 nama hanya-arsip bukan-akhiran-USDT** dan **18 simbol tanpa bulan
  HIDUP**.
- Apakah selisih **12** benar-benar himpunan 12 simbol-bulan karantina.
- Apakah **50 kontrak delivery bertanggal** pernah masuk perhitungan mana pun.
- Mengapa dua dari enam bulan peralihan jatuh pada **2025-07**, bulan tebing
  funding dan bulan kohort puncak.
- Sebab kebangkitan/peralihan kedelapan simbol (di luar jangkauan arsip).
- Apakah 3 lubang BNXUSDT (2022-04, -06, -08) sama dengan 3 simbol-bulan KC-15.
- Kehidupan 12 simbol-bulan karantina.
- `bulan_hidup_terakhir` bagi 28 anggota kohort di luar sampel abjad.
- 15 nama SETTLED: apakah punya pendahulu seperti SXPUSDT; dua belas di antaranya
  bercacah satu bulan saja.
- **Saham, ETF, dan komoditas token masih terhitung `perpetual_usdt`** — diakui
  tersurat oleh `taksonomi.CATATAN_BATAS`; memisahkannya menuntut daftar
  instrumen dari bursa, yang tidak dapat diambil dari runner.
- `.decode("utf-8","replace")` di `klines` membungkam byte rusak.
- Apakah BUSD/USDC layak digabung dengan USDT — kini pertanyaan berangka: 80
  nama, 1.705 bulan (812 + 893).
- Sisa 16 simbol non-ASCII belum diuji langsung (币安人生USDT 9, 我踏马来了USDT 6,
  龙虾USDT 4); ketiganya tergolong `perpetual_usdt`, jadi ADA di dalam penyebut.
- Sebab KC-14 (H-A004) tidak dapat diuji. Sebab KC-15 tidak diketahui.
- Selisih penyebut diagnosa KC-15: 38 diperiksa, 41 dirancang.
- `reports/funding_selisih_penuh.json` belum pernah dibaca; `daftar_terpotong`
  masih true (500 dari 880).
- Selisih byte funding AGIXUSDT 531 lawan 529.
- `waktu_utc` runner berjalan lebih dulu daripada jam sesi.
- `tests/test_pulihkan.py` belum pernah dibaca ulang sesudah push.
