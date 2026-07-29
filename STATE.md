# STATE — versi 34

Diperbarui: 2026-07-29 (sesi 54, lanjutan). Aturan hanya BERTAMBAH; jangan
menulis ulang dari ingatan. v34 disusun di atas teks v33 yang dibaca langsung
dari `main` (blob `8c8caf07`), ditambah jurnal 89 (`f6eb8b78`, blob `ab1c984b`),
laporan `reports/lubang_tengah.json` **V2** (blob **`39cd1caa`**, dibaca UTUH),
`reports/lubang_tengah_status.json` (blob `e7e28495`), serta tiga run yang
dicocokkan commit-nya: **30437620711** (`a9e91bcd`, CI **382**), **30440471598**
(`be5cd877`, CI **396**), dan **30440471508** (`be5cd877`, lubang_tengah **V2**).
Semuanya kode 0.

Peristiwa terbesar sejak v33: **kebangkitan pasar PERTAMA yang terukur di repo
ini.** LITUSDT hidup kembali pada 2026-01..2026-06 — H-A011 MENANG 6–0 — dan
karena itu "nol kebangkitan" pada `kohort_ekor` V4 terbukti batas ALAT UKUR,
bukan sifat pasar. Dari kekalahan ramalan atas fakta itu lahir aturan 59 dan
KC-21.

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
definisi berdampingan.

37. **[v20]** Sampel yang dipakai menguji sebuah jalur wajib memuat sedikitnya
    satu kasus dari tiap kelas cacat yang diketahui relevan, dan laporan wajib
    menyebut kelas mana yang tersentuh dan mana yang tidak, walau cacahnya nol.
38. **[v21]** Cacah uji hanya sah dari `reports/ci_terakhir.json` (run id +
    commit + `kode_keluar`). Penjumlahan taksiran dilarang ditulis sebagai angka
    uji. Lahir dari selisih 135 lawan **141**; dilanggar lagi pada R-148
    (198 lawan **201**) karena saya mencacah FUNGSI uji, bukan butir yang
    dikumpulkan pytest — satu fungsi berparameter empat kasus bernilai 4 butir.
    **Ditaati pada R-198, R-200, R-204, R-205, R-208, R-215, R-220, R-221, R-226,
    R-227, dan R-228.** Dilanggar pada R-211 [v31] dan R-217 [v32] — lihat aturan
    54, 57, dan KC-19. **Catatan baru [v34]:** laporan CI dapat TERTIMPA oleh run
    berikutnya di `main`; bila demikian, bacalah pada ref commit yang bersangkutan
    (R-227 hanya terbaca lewat ref `be5cd877`).
39. **[v22]** Keseragaman yang terukur pada sampel DILARANG dipakai sebagai
    angka ramalan untuk anggota di luar sampel; wajib pita atau kemungkinan
    campuran. Lahir dari R-114. **Dibenarkan keras [v30]:** kohort puncak 100%
    mati, semesta 7,15% mati. **Dibenarkan kedua kali [v31]:** kohort puncak
    456/456 berlubang funding, semesta hanya 842 dari 1.401 MATI.
40. **[v22]** Tiap laporan yang mencacah baris sebuah simbol-bulan wajib memuat
    uji silang `baris + hilang_di_tengah + tepi = menit_kalender` dan melaporkan
    selisihnya walau nol. Lahir dari 210 menit BNXUSDT 2022-04.
41. **[v23]** Ramalan bersyarat yang penyebutnya nol dicatat TIDAK
    TERADJUDIKASI, bukan TEPAT, dan status itu wajib dipra-registrasikan bersama
    ramalannya. Lahir dari R-120. Aktif pada laporan kehidupan kohort
    (`penyebut_tanpa_mati` = 0). **TIDAK aktif lagi untuk semesta [v30]:**
    `penyebut_tanpa_mati` semesta = **18.185**, jadi rasio di atasnya kini dapat
    diadjudikasi.
42. **[v23]** Kelas cacat baru DILARANG dinamai atas dasar satu angka yang
    belum diukur langsung. Tuduhan ditulis sebagai hipotesis + run, bukan
    sebagai kelas. Lahir dari KC-16 yang ditarik. **Ditaati pada KC-18**, yang
    baru dinamai di jurnal 74 sesudah kendali positif membuktikan alat ukurnya
    melihat. **Ditaati lagi [v32]:** ke-33 HIDUP tanpa funding TIDAK dinamai
    kelas cacat, sebab bentuk lubangnya justru menjelaskannya. **Ditaati ketiga
    kali [v33]:** jeda funding LITUSDT 2025-07..-11 TIDAK dinamai kelas cacat;
    ia dicatat sebagai bentuk terukur beserta pertanyaan yang belum diukur —
    dan [v34] pertanyaan itu terjawab MELAWAN dugaan saya, membuktikan
    penundaan penamaan itu benar.
43. **[v24]** Medan penggugur yang membandingkan taksiran dengan kenyataan wajib
    memakai toleransi yang BERSKALA terhadap cacah item, bukan margin datar.
    Margin datar 20.480 byte membuat 16 uji lolos sementara produksi gagal pada
    1.055 anggota, karena cacatnya (header pax 1.024 B per anggota) tumbuh per
    item sedangkan marginnya tidak. Uji wajib memuat kasus bercacah besar.
44. **[v24]** Ramalan wajib menyebut penyebutnya secara eksplisit: pecahan mana,
    semesta mana, medan mana. Bila sebuah pita hanya masuk akal di bawah satu
    tafsir dan meleset di bawah tafsir lain, ia diadjudikasi MELESET. Lahir dari
    R-131.
45. **[v25] Keatomikan push pemicu.** Sebuah push yang MENYALAKAN run wajib
    memuat setiap berkas yang run itu bergantung padanya, dan daftar berkas itu
    wajib dihitung ulang tepat sebelum dikirim. GitHub Actions memakai berkas
    workflow pada commit PEMICU, sehingga perbaikan workflow yang menyusul di
    commit berikutnya TIDAK berlaku untuk run yang sedang berjalan. Lahir dari
    `57a04f1e`. Ditaati pada `ab4e0774`, `387037a9`, `796c2fc4`, `5c65adf9`,
    `d4a2f60a`, `0929643c`, `1b0e8d8e`, `b1816ddf`, `680d04b4`, dan
    **`be5cd877`** (lubang_tengah V2: modul + uji dalam satu commit; workflow
    tidak berubah sehingga tidak perlu disertakan).
46. **[v26, LUNAS DI KODE v28] Kode dilarang menyimpulkan dari penyebut nol.**
    Medan yang MENYIMPULKAN sebuah definisi atau sebab wajib memeriksa lebih
    dulu apakah kasusnya mampu membedakan. Bila penyebutnya nol, atau bila kedua
    kemungkinan menghasilkan angka yang sama, medan itu wajib berbunyi "tidak
    dapat dibedakan", bukan menyebut salah satu. Aturan 30 dan 41 melarang AGEN
    menyimpulkan dari penyebut nol; aturan ini melarang KODE melakukannya.
    Lahir dari `pulihkan.py` VERSI 1, yang pada pecahan 2 dan 5 (tanpa
    karantina) mencetak `definisi_jumlah_baris` = "baris lolos saja" padahal
    kedua definisi menghasilkan angka identik di sana. **Diperbaiki di
    `pulihkan.py` VERSI 2** (commit `5c65adf9`) lewat fungsi murni
    `putuskan_definisi` dan medan penggugur `definisi_dapat_dibedakan`. Sudah
    lebih dulu DITAATI oleh `kohort_ekor` V4 (`bangkit_dapat_diuji`), lalu oleh
    `kehidupan` V1, `kehidupan_arsip` V1 (`penyebut_tanpa_mati_kosong`),
    `silang_funding` V1–V2, dan `lubang_tengah` V1–**V2** (`cacah_tak_terukur`,
    `terukur` pada `uji_h_a011`). **[v34] Sisi lain aturan ini terbukti mahal:**
    `cacah_simbol_bangkit_dapat_diuji` = 0 pada kohort_ekor V4 memang JUJUR, tetapi
    saya sendiri yang lalu membacanya sebagai fakta pasar — lihat aturan 59.
47. **[v27, lahir di jurnal 69]** Sebelum menulis ramalan berupa cacah,
    sebutkan satuannya secara eksplisit — simbol, bulan, simbol-bulan, baris,
    atau butir uji — dan periksa bahwa angka rujukan yang dipakai memang
    bersatuan itu. Lahir dari R-163.
48. **[v27, lahir di jurnal 71]** Berkas modul yang mendekati pagar 800 baris
    harus dipecah SEBELUM fungsi baru ditambahkan, dan setiap pemecahan wajib
    memperluas daftar berkas yang masuk `sidik_kode`. **[v33] Kini berlaku atas
    DUA berkas:** `funding.py` **705** dan `silang_funding.py` **705** — seri,
    masing-masing 95 baris di bawah pagar. Keputusan membuat `lubang_tengah.py`
    sebagai modul BARU alih-alih `silang_funding` V3 terbukti benar oleh angka:
    jalur V3 sudah menembus pagar sekarang. **[v34] Peringatan:**
    `lubang_tengah.py` V2 menambah tiga fungsi di atas 390 baris dan CACAHNYA
    BELUM DIUKUR; ukur sebelum V3.
49. **[v27, lahir di jurnal 72]** Pemecahan berkas yang mempertahankan seluruh
    nama fungsi lewat re-export TETAP dapat mematahkan uji, karena re-export
    memindahkan fungsi dan bukan modul. Telusuri juga nama yang DITAMBAL
    (`monkeypatch.setattr`, `patch`, akses atribut modul).
50. **[v27, lahir di jurnal 73]** Setiap pengukuran yang menyimpulkan dari
    KETIADAAN — volume nol, berkas hilang, baris kosong, jawaban 404 — wajib
    memuat kendali positif yang membuktikan alat ukurnya mampu mendeteksi
    KEHADIRAN pada kondisi yang sama. Dipakai sebagai klausa gugur ADR-A008 §6;
    pada run kehidupan kohort klausa itu tidak aktif (kendali 4/4), pada run
    semesta juga tidak (**kendali 24/24 hidup**), pada run silang funding juga
    tidak (**3/3 BTCUSDT HIDUP dan berfunding**), dan pada run **lubang_tengah**
    V1 dan **V2** juga tidak (**3/3 BTCUSDT HIDUP dan berfunding**, `kendali_sah`
    true). **[v34] Aturan 59 memindahkan kewajiban yang sama ke RAMALAN.**
51. **[v27, lahir di jurnal 75]** Jendela pemindaian mundur wajib adaptif, atau
    dibuktikan mencakup peristiwa yang dicari. Jendela tetap yang seluruh isinya
    sepi menghasilkan null, bukan jawaban. **Ditaati pada kohort_ekor V4.**
52. **[v27, lahir di jurnal 75]** Laporan yang tidak dapat dibaca utuh setara
    dengan laporan yang tidak ada. Setiap pelapor besar wajib berpasangan dengan
    keluaran ringkas yang memuat sidik berkas sumbernya. Ditaati oleh
    `kohort_ringkas`, `ukur_baris`, `kehidupan`, `kehidupan_arsip`,
    `silang_funding`, dan `lubang_tengah` V1–V2 (laporan penuh + berkas status).
    **Diperkuat [v32]:** V2 `silang_funding` menerbitkan
    `reports/hidup_tanpa_funding.json` yang memuat kedua daftar bernama dan
    memang terbaca utuh, sedangkan laporan penuh 183.963 B tetap tak terbaca
    utuh selamanya.
53. **[v30, lahir dari R-205] Ramalan kode keluar sebuah run yang gerbangnya
    adalah berkas uji wajib didahului pembacaan PERILAKU setiap fungsi yang
    diuji, bukan hanya namanya.** Lahir dari R-205: uji menuntut
    `bagian_volume_nol` sama dengan 2/3 penuh, sedangkan `kohort_ekor.bagian`
    MEMBULATKAN ke empat desimal dan mengembalikan 0,6667 — CI keluar dengan
    kode 1 karena harapan uji, bukan karena modulnya. Ramalan berkepala dua yang
    separuhnya salah diadjudikasi SEPARUH, bukan MELESET. **Ditaati pada R-211,
    R-215, R-217, R-221, R-222, R-226, dan R-228** (kode keluar 0 benar pada
    semuanya).
54. **[v31, lahir dari R-211] Cacah butir uji dalam sebuah ramalan wajib
    dihitung dengan mencacah definisi `def test_` satu per satu pada berkas uji
    yang SUDAH selesai ditulis, mengalikan setiap fungsi berparameter dengan
    cacah kasusnya.** Dilarang mencacah dari ingatan rancangan. Lahir dari
    R-211 (312 lawan **316**). Aturan 38 mengatur SUMBER angka akhir; aturan 54
    mengatur cara menyusun angka RAMALANNYA. Pendahulu: R-148. **TIDAK CUKUP
    [v32]:** R-217 gugur walau aturan 54 saya kira sudah ditaati — lihat aturan
    57.
55. **[v31, lahir dari R-209 dan R-212] Sebelum meramalkan hasil sebuah
    workflow, baca `paths`/`paths-ignore` workflow itu dan sebutkan di dalam
    ramalan workflow MANA yang akan menyala pada commit yang dimaksud. Ramalan
    atas run yang tidak akan pernah menyala DILARANG.** `.github/workflows/ci.yml`
    memakai `paths-ignore` untuk `journal/**`, `decisions/**`, `hipotesis/**`,
    dan `reports/**`; karena itu commit yang hanya menyentuh jurnal TIDAK
    menyalakan CI. **Ditaati pada R-217, R-221, R-226, R-227, dan R-228.**
56. **[v32, lahir dari R-216] Ramalan yang menyebut sebuah commit sebagai
    sasaran wajib menyebut sasaran yang keberadaannya dijamin oleh cara kerja
    saya sendiri.** Bentuk yang sah: "commit BERIKUTNYA yang menyentuh
    `<berkas>`". Bentuk yang dilarang: menyebut satu commit yang memuat DUA
    berkas atau lebih, kecuali push-nya memang atomik dan dirancang atomik sejak
    ramalan ditulis (aturan 45). Lahir dari R-216. **Ditaati pada R-217, R-220,
    R-221, R-226, R-227, dan R-228.**
57. **[v32, lahir dari R-217] Sebelum meramalkan cacah butir uji, nama setiap
    fungsi `def test_` WAJIB ditulis BERNOMOR di jurnal atau docstring, dan
    nomor terakhirnya dipakai sebagai cacahan.** Ramalan cacah butir tanpa
    daftar bernomor yang tersurat DILARANG. Lahir dari R-217 (ditulis 42 fungsi
    / 44 butir, nyatanya **47** fungsi / **49** butir). **TERBUKTI BEKERJA DUA
    DARI DUA [v34]:** R-221 menulis 42 nama BERNOMOR → 382 tepat; R-228 menulis
    **56** nama BERNOMOR → 382 − 42 + 56 = **396** tepat.
58. **[v33, lahir dari R-225] Cacah baris sebuah berkas yang versi terkininya
    belum dibaca ulang UTUH dalam giliran yang sama DILARANG diramalkan dengan
    pita sempit.** Pilih salah satu: (a) baca ulang utuh dulu, lalu ramalkan;
    (b) pakai pita yang batas atasnya sekurang-kurangnya **1,8 kali** batas
    bawah; atau (c) jangan meramalkan sama sekali dan cukup ukur. Lahir dari
    R-225: pita 470..620 atas `silang_funding.py` V2 yang nyatanya **705**.
    Menambah 30 persen ke taksiran sudah terbukti tidak cukup. Lihat KC-20.
    **Pilihan (c) dipakai [v34]** atas `lubang_tengah.py` V2: tidak diramalkan,
    akan diukur.
59. **[v34, lahir dari R-230] Ramalan yang menegaskan KETIADAAN sebuah gejala
    wajib menyebut penyebut yang mampu memuat gejala itu, beserta cacah kasus
    yang benar-benar pernah diperiksa.** Bila cacah itu NOL, ramalan wajib
    ditulis sebagai kemungkinan campuran, bukan sebagai penegasan — atau tidak
    ditulis sama sekali. Lahir dari R-230: saya meramalkan LITUSDT tetap MATI
    dengan dasar "tidak ada kebangkitan yang pernah terukur", padahal
    `cacah_simbol_bangkit_dapat_diuji` = 0 berarti penyebutnya memang tidak
    pernah mampu membedakan. Aturan 39 melarang mengekstrapolasi KESERAGAMAN
    sampel; aturan 59 melarang mengekstrapolasi KEKOSONGAN sampel. Aturan 50
    mewajibkan kendali positif pada KODE; aturan 59 mewajibkan padanannya pada
    RAMALAN. Lihat KC-21.

## Kelas cacat

KC-1 s.d. KC-12 seperti pada v19. KC-10 dan KC-11 DITUTUP (v20). KC-13
(keterwakilan sampel) → penangkalnya aturan 37.

- **KC-14 [v21, dipersempit v22] — menit hilang NYATA di arsip 1m, hadir di
  KEDUA representasi.** **9** simbol-bulan, **6.375 menit** (425×15). Sebab
  tidak diketahui (H-A004, tak dapat diuji). Kebijakan: karantina (ADR-A006).
- **KC-15 [v22] — berkas klines BULANAN dapat kehilangan HARI UTC penuh yang
  datanya utuh di berkas HARIAN.** **3** simbol-bulan, semuanya BNXUSDT 2022,
  **7.200 menit = 5×1440**. Kebijakan: ADR-A007. Sebab masih tidak diketahui.
- 9 + 3 = **12** karantina; 6.375 + 7.200 = **13.575** menit ✅ Keduabelasnya
  memuat **516.135 baris**, terbaca ulang dari luar runner. **Kehidupan
  keduabelasnya BELUM diukur** — tar karantina terpisah dan tidak disentuh run
  `kehidupan_arsip`.
- **KC-16 DITARIK [v23] — nomornya TETAP kosong selamanya.**
- **KC-17 [v24] — parquet karantina tidak dipersistenkan. DITUTUP [v25],
  diperkuat [v26].**
- **KC-18 [v27, dinamai di jurnal 74] — lilin datar lolos gerbang struktural.**
  Arsip menerbitkan berkas klines 1m lengkap dan sah secara bentuk untuk pasar
  yang tidak diperdagangkan: stempel waktu rapat tanpa menit hilang, checksum
  cocok, namun `volume` dan `count` nol pada SELURUH lilin. Gerbang 1m
  meloloskannya karena menilai BENTUK deret, bukan KEHIDUPAN pasar.
  - Bentangan jurnal 74: 864.000 lilin pada 20 simbol-bulan.
  - Bentangan jurnal 77: 169 dari 179 simbol-bulan sepi pada 10 simbol.
  - Bentangan kohort [v29] — run `30418471430`: **456 dari 456** simbol-bulan
    kohort puncak 2025-07 MATI, 19.972.800 lilin, 456/456 lolos gerbang.
  - **BENTANGAN SEMESTA TERUKUR [v30]** — delapan run pecahan pada commit
    `0929643c`: dari **19.586** simbol-bulan lolos gerbang, **1.401 MATI**
    (7,153%), **98 SEPI** (0,500%), **18.087 HIDUP** (92,35%).
  - **Kematian TIDAK terkurung di kohort puncak.** 456 MATI kohort termuat di
    dalam 1.401, sehingga **945 simbol-bulan MATI berada di luar kohort puncak**.
  - **KEMATIAN BUKAN CACAT ARSIP FUNDING [v31].** Dari 1.401 MATI, **842**
    kehilangan funding dan **559 tetap punya funding**.
  - **SISI KEBALIKANNYA TERUKUR [v33]:** keenam lubang funding TENGAH jatuh pada
    simbol-bulan berstatus **MATI** yang klines-nya justru **sempurna secara
    bentuk** — 44.640 lilin (31×1.440) atau 43.200 lilin (30×1.440), tanpa satu
    menit pun hilang. Gerbang 1m meloloskan keenamnya.
  - **KEMATIAN DAPAT BERBALIK [v34].** LITUSDT HIDUP sampai 2025-06 → MATI
    2025-07..2025-11 (klines penuh secara bentuk, funding hilang) → **HIDUP
    kembali 2026-01..2026-06** dengan funding pulih. Jadi KC-18 tidak selalu
    menandai akhir sebuah pasar; ia dapat menandai JEDA. Konsekuensi langsung:
    status kehidupan WAJIB dipakai per SIMBOL-BULAN, sebab satu simbol dapat
    menyeberang status di dalam dirinya sendiri.
  - Ekstrapolasi dari kohort ke semesta TERBUKTI keliru arah: kohort 100% mati,
    semesta 7,15% mati. Aturan 39 dibenarkan.
  - **Kebijakan DIPUTUSKAN [v28] oleh ADR-A008** (Keputusan 1–6 DITERIMA):
    KC-18 bukan gerbang serapan; kehidupan diukur per simbol-bulan; **SEPI**
    bila `bagian_volume_nol` ≥ 0,5 dan **MATI** bila `transaksi_total` = 0;
    setiap penyebut diterbitkan berpasangan; backtest hanya pada simbol-bulan
    HIDUP; angka 839.842.134 tidak ditulis ulang (aturan 29). Keputusan 7
    DITANGGUHKAN. **Klausa gugur §6 tidak aktif** pada seluruh run.
- **KC-19 [v32, lahir dari R-217] — mencacah dari INGATAN atas berkas yang baru
  saya tulis sendiri.** R-148, R-211, dan R-217 gugur dengan sebab yang persis
  sama. Penangkalnya aturan 57 (daftar bernomor tersurat). **TIDAK TERULANG DUA
  KALI [v34]:** R-221 (382) dan R-228 (396) tepat pada percobaan pertama.
- **KC-20 [v33, lahir dari R-225] — taksiran cacah baris bias sistematis ke
  BAWAH.** Keempat ramalan cacah baris atas berkas yang belum dibaca ulang utuh
  MELESET, dan keempatnya ke arah yang SAMA: R-175 (pita ..680, nyata 705),
  R-179 (..700, 705), R-203 (..400, 417), R-225 (..620, 705). Sementara ramalan
  atas berkas yang dibaca ulang utuh beberapa menit sebelumnya TEPAT tiga dari
  tiga: R-213 (496 dalam 250..500), R-214 (396 dalam 330..430), R-224 (390 dalam
  350..470). Sebabnya dapat disebut: yang saya ingat adalah daftar fungsi,
  sedangkan yang menghabiskan baris adalah docstring praregistrasi, medan
  laporan, dan baris kosong antar-blok — pada `silang_funding.py` V2 ada 99
  baris kosong dan 113 baris bukan-kode. Penangkalnya aturan 58. Kelas ini
  BUKAN tentang kode; ia tentang cara saya menaksir berkas sendiri.
- **KC-21 [v34, lahir dari R-230] — menyimpulkan KETIADAAN sebuah gejala dari
  ketiadaan PENGUKURANNYA.** Aturan 46 sudah menjaga KODE dari penyebut nol dan
  aturan 50 mewajibkan kendali positif; R-230 memperlihatkan lubang yang sama
  pada AGEN. Saya memakai `cacah_simbol_bangkit_dapat_diuji` = 0 — sebuah nol
  yang secara tersurat berarti "tidak dapat diuji" — sebagai dasar meramalkan
  bahwa kebangkitan tidak akan ditemukan. Nol yang tidak mampu membedakan bukan
  bukti; ia ketidaktahuan yang rapi. Penangkalnya aturan 59. Kelas ini, seperti
  KC-19 dan KC-20, adalah cacat PENALARAN saya, bukan cacat kode.

## H-A011 — DIUJI dan MENANG 6–0 [v34]

Sumber: `lux_ai/serapan/lubang_tengah.py` **V2** (blob **`4d3beaf1`**,
`VERSI` 2, `sidik_kode`
**`c9372bd763b86cfeb2adcf0a0c0c43dae8d9aa9a6508e9c32f7671d5ec7b3f4e`**),
didorong ATOMIK bersama berkas ujinya (blob `b5417b27`, **56** fungsi bernomor)
pada commit **`be5cd877`** (aturan 45). Run **30440471508**, kode 0.
`reports/lubang_tengah.json` V2 (blob **`39cd1caa`**) dibaca **UTUH**;
`reports/lubang_tengah_status.json` blob `e7e28495`. Bahan: kedelapan
`reports/kehidupan_arsip_<i>.json` + `reports/funding_semesta.json`; tanpa
unduhan.

| bulan LITUSDT | status |
| --- | --- |
| 2026-01 | **HIDUP** |
| 2026-02 | **HIDUP** |
| 2026-03 | **HIDUP** |
| 2026-04 | **HIDUP** |
| 2026-05 | **HIDUP** |
| 2026-06 | **HIDUP** |

`cacah_bulan` **6**, `cacah_hidup` **6**, `sebaran_status` {HIDUP 6, MATI 0,
SEPI 0, TAK_TERUKUR 0}, `terukur` **true**, **`h_a011_menang` true**.

Penggugur bersih V2: `selisih_lubang_tengah` **0**, `cacah_lubang_tengah` **6**,
`sebaran_status_lubang_tengah` {MATI 6, SEPI 0, HIDUP 0, TAK_TERUKUR 0},
`sidik_seragam` true, `cacah_laporan_dibaca` **8**, `laporan_hilang` [],
`cacah_kunci_ganda` 0, `cacah_lubang_ganda` 0, `cacah_lubang_funding` **880**,
`cacah_per_simbol_funding` **787**, `penyebut_kehidupan` **19.586**,
`cacah_baris_dengan_medan` **19.586**, `kendali_sah` **true** (BTCUSDT 2021-05,
2021-08, 2021-01 — ketiganya HIDUP dan berfunding), `kode_keluar` 0.

**Yang BOLEH disimpulkan.** Rentetan LITUSDT adalah **kebangkitan pasar pertama
yang terukur di repo ini**: HIDUP → MATI lima bulan dengan klines tetap terbit
penuh secara bentuk dan funding HILANG → funding KEMBALI dan pasar HIDUP kembali
enam bulan berturut. Bentuk lubang TENGAH karena itu berpenjelasan jauh lebih
kuat daripada "jeda penerbitan pada pasar mati": pada LITUSDT ia menandai pasar
yang berhenti diperdagangkan lalu diperdagangkan kembali, dengan funding dan
perdagangan berhenti serta pulih BERSAMA.

**Yang TIDAK BOLEH disimpulkan (aturan 10, 20).** Bahwa sebabnya delisting resmi
lalu pendaftaran ulang — itu tetap DUGAAN, tak terjangkau dari arsip. Bahwa
BTCSTUSDT 2022-01 sejenis — rentetannya satu bulan dan statusnya sesudah lubang
BELUM diperiksa. Bahwa kebangkitan lazim: satu kasus bukan laju. ADR-A002 §10
tetap tidak disunting.

**Batas alat ukur yang terbongkar.** `kohort_ekor` V4 melaporkan
`bangkit_kembali` 0 dengan `cacah_simbol_bangkit_dapat_diuji` **0**. Nol pertama
kini terbukti artefak nol kedua. Setiap pernyataan repo ini tentang "tidak ada
kebangkitan" BATAL sebagai fakta dan hanya sah sebagai "belum terukur".

## Keenam lubang funding TENGAH — BERNAMA [v33]

Sumber: `lubang_tengah.py` **V1** (blob `c2046bce`, **390 baris**, `sidik_kode`
**`ebdf0b1c68420662d349d9e03daa750574e327f971bc81551889776c575925e4`**), commit
**`680d04b4`**, run **30436334434**, kode 0; laporan V1 blob **`247a04cf`** dibaca
UTUH. Angka-angka ini TIDAK berubah di V2 (`selisih_lubang_tengah` tetap 0,
`cacah_lubang_tengah` tetap 6). Definisi bentuk lubang TETAP satu, dipakai dari
`silang_funding` (aturan 36).

| simbol | bulan | funding sebelum | funding sesudah | rentetan | status | cacah_lilin | byte parquet |
|---|---|---|---|---:|---|---:|---:|
| BTCSTUSDT | 2022-01 | 2021-12 | 2022-02 | 1 | MATI | 44.640 | 399.757 |
| LITUSDT | 2025-07 | 2025-06 | 2026-01 | 5 | MATI | 44.640 | 427.922 |
| LITUSDT | 2025-08 | 2025-06 | 2026-01 | 5 | MATI | 44.640 | 427.505 |
| LITUSDT | 2025-09 | 2025-06 | 2026-01 | 5 | MATI | 43.200 | 392.233 |
| LITUSDT | 2025-10 | 2025-06 | 2026-01 | 5 | MATI | 44.640 | 434.201 |
| LITUSDT | 2025-11 | 2025-06 | 2026-01 | 5 | MATI | 43.200 | 389.479 |

`sebaran_status_lubang_tengah` = **MATI 6 · SEPI 0 · HIDUP 0 · TAK_TERUKUR 0**.
BTCSTUSDT: 64 bulan klines (2021-03..2026-06), 1 lubang. LITUSDT: 64 bulan
klines (2021-02..2026-06), 5 lubang.

"Enam lubang tengah" adalah enam SIMBOL-BULAN dalam **DUA** rentetan, bukan enam
peristiwa. Keenamnya MATI dan berklines penuh secara bentuk.

**Ketiga bentuk kini punya penjelasan calon:** ekor = kematian pasar (lubang →
mati 96,0%); awal = funding menyusul klines (H-A010 MENANG, definisinya kini
TEPAT); tengah = **jeda perdagangan yang dapat berakhir dengan kebangkitan**
(H-A011 MENANG). Prasyarat BENTUK bagi Keputusan 7 ADR-A008 terpenuhi;
keputusannya sendiri belum diambil.

## H-A010 — DIUJI, MENANG, dan definisinya kini TEPAT [v34]

Uji `uji_h_a010` atas kelima simbol pemilik ke-33 lubang HIDUP tanpa funding.
Definisi LOKAL yang dipakai dan diakui tersurat: "bulan berfunding pertama" =
bulan klines terawal yang TIDAK berlubang.

| simbol | klines pertama | berfunding pertama | jarak | bulan klines | lubang |
|---|---|---|---:|---:|---:|
| QTUMUSDT | 2020-02 | 2020-03 | 1 | 77 | 1 |
| ICPUSDT | 2021-05 | 2022-09 | 16 | 62 | 16 |
| TLMUSDT | 2021-07 | 2023-03 | 20 | 60 | 20 |
| BNXUSDT | 2022-05 | 2023-02 | 9 | 48 | 19 |
| JUPUSDT | 2024-01 | 2024-02 | 1 | 30 | 1 |

`cacah_menang` **5**, `cacah_gugur` **0**, `cacah_tak_terukur` **0**,
`h_a010.menang` **true**. Uji dirancang dapat gugur: satu simbol membangkang
sudah menjatuhkannya.

**BATAS v33 kini DITUTUP [v34].** `funding_semesta.json.per_simbol` memuat
**10 medan** dan TIDAK memuat `bulan_funding_pertama`, sehingga "berfunding
pertama" di atas adalah definisi TURUNAN. V2 memeriksa medan
`funding_tanpa_klines` bagi kelima simbol itu: `ada_medan` **true 5/5**,
`cacah_bulan` **0** pada kelimanya, `bulan` **[]**, `cacah_berisi` **0**,
`cacah_tak_terukur` **0**, `kosong_seluruhnya` **true**. Tidak ada satu pun bulan
funding yang MENDAHULUI klines pada ICP, TLM, BNX, JUP, QTUM. Karena itu definisi
turunan tadi bukan hanya memadai melainkan **TEPAT**, dan kemenangan R-223
DIKUATKAN — tidak perlu ditinjau ulang.

## Daftar 33 HIDUP tanpa funding dan 3 lubang tak dikenal — TERBIT [v32]

Sumber: `silang_funding` **V2**, run **30434948267**, commit **`b1816ddf`**,
kode 0; `sidik_kode`
**`8a9b859c09cd64e30e203e6f8dc53411b8e341c44f112805b3041e5d4d3231b1`**;
`sidik_data_funding` `2c9fbd1b…8c24` (SAMA dengan V1 → bahan baku identik).
Berkas `reports/hidup_tanpa_funding.json` (blob `a7b20503`) dibaca **UTUH**.
Penggugur: `selisih_hidup_tanpa_funding` **0**, `selisih_lubang_tak_dikenal` **0**.

**Sebaran bentuk ke-33: awal 33 · ekor 0 · tengah 0 · seluruh 0.**

| simbol | cacah | bulan | lubang simbol | bulan klines simbol |
|---|---:|---|---:|---:|
| ICPUSDT | 13 | 2021-05..2022-05 | 16 | 62 |
| TLMUSDT | 11 | 2021-07..2022-05 | 20 | 60 |
| BNXUSDT | 7 | 2022-05, -07, -09, -10, -11, -12, 2023-01 | 19 | 48 |
| JUPUSDT | 1 | 2024-01 | 1 | 30 |
| QTUMUSDT | 1 | 2020-02 | 1 | 77 |

13 + 11 + 7 + 1 + 1 = **33** ✅ (dihitung tangan, aturan 21). Lima simbol saja.

**Tiga lubang tak dikenal: BNXUSDT 2022-04, 2022-06, 2022-08** — ketiganya
`simbol_dikenal` true (BNXUSDT punya 48 bulan di penyebut, 2022-05..2026-06).

**Definisi `bentuk_lubang_lokal` (aturan 36).** Dihitung V2 atas penyebut 19.586,
BUKAN definisi `funding.py`: awal bila semua bulan klines simbol yang tidak lebih
besar juga berlubang; ekor bila semua yang tidak lebih kecil juga berlubang;
seluruh bila keduanya; tengah bila tidak satu pun. Kedua definisi BERTEMU setelah
penyebutnya disamakan:

- lokal atas 877 lubang di dalam penyebut = awal **45** + ekor **826** + tengah
  **6** + seluruh 0 = **877** ✅
- terbitan `funding.py` atas 880 = awal **48** + ekor 826 + tengah 6
- selisih 48 − 45 = **3** = ketiga lubang BNXUSDT di luar penyebut ✅

**Medan baris laporan kehidupan** (`medan_baris_terlihat`, 14 medan):
`ada_di_arsip`, `bagian_volume_nol`, `bulan`, `byte_parquet`,
`cacah_baris_cacat`, `cacah_lilin`, `cacah_lilin_terbaca`, `cacah_volume_nol`,
`galat`, `gerbang_lolos`, `jalur`, `simbol`, `status`, `transaksi_total`.
`cacah_baris_dengan_medan` = **19.586**, jadi `cacah_lilin` ada pada SETIAP baris.

## Silang funding × kehidupan — TERUKUR [v31]

Penyebut: **19.586** simbol-bulan lolos gerbang (aturan 30, 44).

| status | funding ADA | funding HILANG | jumlah |
|---|---:|---:|---:|
| MATI | 559 | **842** | 1.401 |
| SEPI | 96 | 2 | 98 |
| HIDUP | 18.054 | **33** | 18.087 |
| TAK TERUKUR | 0 | 0 | 0 |
| **jumlah** | **18.709** | **877** | **19.586** |

Uji silang (aturan 21):

- 559 + 96 + 18.054 = **18.709** ✅ 842 + 2 + 33 = **877** ✅ jumlah **19.586** ✅
- 877 + **3** `cacah_lubang_tak_dikenal` = **880**, persis cacah lubang funding
  semesta `funding.py` V6 ✅ Ketiganya BERNAMA: BNXUSDT 2022-04, -06, -08.
- Kohort puncak: **456/456** MATI dan **456/456** berlubang ✅
- Di luar kohort: 945 MATI = **386** berlubang + **559** berfunding ✅
  456 + 386 = 842 ✅ `bagian` 386/945 = **0,4085** (dibulatkan 4 desimal).

**Yang BOLEH disimpulkan.** Dua arah wajib dipisah: lubang → mati **kuat**
(842/877 = **96,0%**); mati → lubang **lemah** (842/1.401 = **60,1%**). Lubang
funding TIDAK sah dipakai sebagai penyaring kematian — memakainya melewatkan 559
bulan mati. Irisan bukan sebab (aturan 10).

## Kehidupan semesta terserap — TERUKUR [v30]

Modul `kehidupan_arsip.py` V1 (`sidik_kode`
**`24b6bb265525e81c2e571b46e401f36903383f1e3738c487850861adc3e8c595`**), commit
`0929643c`, run pecahan 0 = **30419770259**. Sidik kode SAMA di kedelapan
laporan, sehingga penjumlahan lintas pecahan sah (aturan 20, 22).

| pecahan | penyebut penuh | MATI | SEPI | HIDUP | tanpa MATI | bagian_mati | lilin penuh | lilin mati |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 2.408 | 122 | 13 | 2.273 | 2.286 | 0,0507 | 103.134.312 | 5.339.520 |
| 1 | 2.465 | 103 | 11 | 2.351 | 2.362 | 0,0418 | 105.634.220 | 4.468.906 |
| 2 | 2.337 | 204 | 7 | 2.126 | 2.133 | 0,0873 | 100.058.416 | 8.922.240 |
| 3 | 2.153 | 283 | 17 | 1.853 | 1.870 | 0,1314 | 91.841.734 | 12.379.101 |
| 4 | 2.496 | 182 | 15 | 2.299 | 2.314 | 0,0729 | 106.821.807 | 7.924.835 |
| 5 | 2.741 | 165 | 12 | 2.564 | 2.576 | 0,0602 | 117.671.896 | 7.204.748 |
| 6 | 2.649 | 182 | 8 | 2.459 | 2.467 | 0,0687 | 113.890.221 | 7.941.027 |
| 7 | 2.337 | 160 | 15 | 2.162 | 2.177 | 0,0685 | 100.273.393 | 6.987.746 |
| **jumlah** | **19.586** | **1.401** | **98** | **18.087** | **18.185** | — | **839.325.999** | **61.168.123** |

- 1.401 + 98 + 18.087 = **19.586** ✅ penyebut yang dipraregistrasi — BUKAN
  19.598 (dua belas karantina tak ada di tar ini).
- 19.586 − 1.401 = **18.185** = jumlah `penyebut_tanpa_mati` ✅
- Jumlah `lilin_penuh` **839.325.999** cocok PERSIS dengan baris lolos gerbang
  yang diukur serapan (run `30396803601`) lewat jalur kode yang berbeda — dari
  zip, bukan dari parquet. Dua pengukuran independen bertemu di satu angka.
- Lilin mati 61.168.123 = **7,29%**; MATI + SEPI = 1.499 = **7,654%** dari 19.586.

Medan penggugur bersih di kedelapan pecahan: `cacah_tak_terukur` 0,
`cacah_baris_cacat` **0** dari 839 juta baris, `cacah_parquet_hilang` 0,
`cacah_parquet_tak_dikenal` 0, `cacah_bagian_hilang` 0, `cacah_sha_tak_cocok` 0,
`cacah_anggota_tak_aman` 0, `kode_keluar` 0. Kendali positif: **24 dari 24
HIDUP**, `parser_terbukti` true.

Yang TIDAK BOLEH: memakai 7,153% sebagai laju kematian simbol mana pun —
sebarannya 4,18% (pecahan 1) sampai 13,14% (pecahan 3), dan pecahan dibagi
menurut simbol sehingga ketidakseragaman ini sifat pasar, bukan derau.
**Tambahan [v34]:** dan tidak boleh dipakai sebagai laju kematian PERMANEN,
sebab sebagian kematian terbukti dapat berbalik (LITUSDT).

## Kehidupan kohort puncak 2025-07 — TERUKUR [v29]

`kehidupan.py` V1 (417 baris, `sidik_kode` `c1aaf852…b4cc`). Run **30418471430**,
commit `d4a2f60a`, kode 0.

| medan | nilai |
| --- | ---: |
| simbol diukur | 38 |
| simbol-bulan diminta / terukur / tak terukur | 456 / 456 / 0 |
| MATI / SEPI / HIDUP | **456** / 0 / **0** |
| lilin penuh = lilin mati | **19.972.800** |
| penyebut penuh / tanpa MATI | 456 / **0** (kosong) |
| kendali diminta / terambil / hidup | 4 / 4 / **4** |

38 × 525.600 = 19.972.800 ✅ dan 38 × 12 = 456 ✅ Kohort puncak menyumbang **nol**
simbol-bulan layak backtest. Yang TIDAK terbukti: bahwa 38 simbol ini tak pernah
diperdagangkan — kohort V4 menunjukkan sebagian hidup pada 2024–2025.

## Hipotesis

- H-A001: belum diuji.
- H-A002a / H-A002b: H-A002b **GUGUR** (`slot_5m_hadir_saat_1m_hilang` = 0).
- **H-A003: MENANG pada 3, GUGUR pada 9.**
- **H-A004: TIDAK TERUJI dan tidak dapat diuji** (`fapi.binance.com` → 451).
- **H-A005: GUGUR pada rentang yang disampel [v23]** (37 bulan tengah).
- **H-A006 — serapan deterministik. MENANG pada ENAM run.**
- **H-A008 — aset rilis GitHub mengembalikan byte yang sama persis. MENANG pada
  DUA kali pengambilan penuh.**
- **H-A009 [v31] — lubang funding dan kematian pasar satu gejala. GUGUR:** 559
  simbol-bulan MATI tetap berfunding.
- **H-A010 [v32 lahir, v33 DIUJI, v34 DIKUATKAN] — penerbitan funding MENYUSUL
  penerbitan klines bagi sebagian simbol. MENANG 5–0**, dan batas v33 kini
  ditutup: `funding_tanpa_klines` kosong pada kelima simbol, jadi definisi
  turunan "berfunding pertama" TEPAT.
- **H-A011 [v33 lahir, v34 DIUJI] — jeda funding TENGAH menandai pasar yang
  berhenti diperdagangkan lalu terdaftar ulang. MENANG 6–0:** LITUSDT
  2026-01..2026-06 seluruhnya HIDUP. Uji dirancang dapat gugur — satu bulan MATI
  padahal funding terbit sudah menjatuhkannya. Batas tersurat: satu simbol, satu
  rentetan; sebab (delisting resmi) tidak terjangkau; BTCSTUSDT belum diperiksa.
- **H-A012 [v34, LAHIR, BELUM DIUJI] — kebangkitan bukan peristiwa tunggal:
  semesta memuat lebih dari satu simbol yang punya bulan MATI lalu bulan HIDUP
  sesudahnya.** Uji: pindai kedelapan `kehidupan_arsip_<i>.json` untuk pola
  MATI→HIDUP per simbol; penyebutnya seluruh 787 simbol, dan kini terbukti tidak
  kosong (LITUSDT ada di dalamnya). Tanpa unduhan. Aturan 59 wajib ditaati saat
  meramalkan cacahnya.

## Papan skor prediksi

R-1..R-120 dirinci v23. R-121..R-149 di v26 dan jurnal 56–63. R-150..R-193 di
jurnal 64–75. R-194..R-199 di jurnal 76–78. R-200..R-204 di jurnal 79–81.
R-205..R-208 di docstring `0929643c` dan `dceb1009`. R-209 di jurnal 82.
R-210..R-211 di docstring `1b0e8d8e`. R-212 di jurnal 83. R-213..R-215 di
docstring `67ec2be4`. R-216 di jurnal 84. R-217..R-219 di docstring `b1816ddf`.
R-220 di jurnal 86. R-221..R-223 di docstring commit `680d04b4`.
R-224..R-226 di docstring commit `85079ffd`. **R-227 di PROMPT v36 (`a9e91bcd`).**
**R-228..R-230 di docstring commit `be5cd877`.** Adjudikasi R-227..R-230 di
jurnal **89** (`f6eb8b78`, blob `ab1c984b`).

| # | Prediksi | Status |
|---|---|---|
| R-175 | kedua berkas ≤800 baris DAN `funding.py` pita 500..680 | **SEPARUH** |
| R-179 | `funding.py` 640..700 DAN `funding_cdn.py` 140..200 | **SEPARUH** |
| R-199 | `definisi_dapat_dibedakan` false pada TEPAT 2 pecahan (2 dan 5) | **MENUNGGU** |
| R-203 | `kehidupan.py` pita 300..400 BARIS DAN 0 berkas lewat pagar | **MELESET** (417) |
| R-211 | CI **312 butir** (291+21), kode 0 | **MELESET** (316; aturan 54) |
| R-213 | `kehidupan_arsip.py` pita 250..500 BARIS | **TEPAT** (496) |
| R-214 | `silang_funding.py` pita 330..430 BARIS | **TEPAT** (396, V1) |
| R-215 | CI 316 butir, kode 0, pada `67ec2be4` | **TEPAT** (`30433635955`) |
| R-216 | CI 316 butir, kode 0, pada commit STATE v31 + PROMPT v34 | **SEPARUH** (aturan 56) |
| R-217 | CI **335 butir**, kode 0 | **MELESET** (340; aturan 57, KC-19) |
| R-218 | `cacah_hidup_tanpa_funding` 33 DAN awal 20..33 DAN ekor 0..3 | **TEPAT** |
| R-219 | ketiga lubang tak dikenal bersimbol dikenal, 3 dari 3 | **TEPAT** (BNXUSDT ×3) |
| R-220 | CI **340 butir**, kode 0, pada commit PROMPT v35 | **TEPAT** (`30435672616`) |
| R-221 | CI **382 butir** (340 + 42), kode 0, pada commit trio `lubang_tengah` | **TEPAT** (`30436334383`) |
| R-222 | `cacah_lubang_tengah` **6** DAN `selisih_lubang_tengah` 0 | **TEPAT** (MATI 6/6) |
| R-223 | H-A010 MENANG: kelima simbol funding pertama SESUDAH klines pertama | **TEPAT** (5–0) |
| R-224 | `lubang_tengah.py` pita **350..470** BARIS | **TEPAT** (390) |
| R-225 | `silang_funding.py` V2 pita **470..620** BARIS DAN 0 lewat pagar | **MELESET** (705; aturan 58, KC-20) |
| R-226 | CI tetap **382 butir**, kode 0, pada commit `ukur_baris` V4 | **TEPAT** (`30436915256`) |
| R-227 | CI **382 butir**, kode 0, pada commit PROMPT v36 | **TEPAT** (`30437620711`) |
| R-228 | CI **396 butir** (382 − 42 + 56), kode 0, pada commit `lubang_tengah` V2 | **TEPAT** (`30440471598`) |
| R-229 | `funding_tanpa_klines` KOSONG pada kelima simbol H-A010 | **TEPAT** (`kosong_seluruhnya` true) |
| R-230 | H-A011 GUGUR: keenam bulan LITUSDT 2026 tetap MATI | **MELESET** (6/6 HIDUP; aturan 59, KC-21) |

**Total R-1..R-230** (aturan 21): TEPAT **161**; MELESET **42**; SEPARUH **13**;
TIDAK TERADJUDIKASI **7**; MENUNGGU **7** (R-7, R-19, R-20, R-28, R-36, R-37,
R-199). 161+42 = 203; +13 = 216; +7 = 223; +7 = **230** ✅ Ramalan berikutnya
**R-231**. N_percobaan = 0.

Catatan kejujuran: R-230 adalah kekalahan yang PALING berharga sejauh ini. Uji
itu dirancang supaya dapat menjatuhkan hipotesisnya sendiri, dan justru
hipotesisnya yang menang; bila saya meramalkan H-A011 menang, saya akan menang
dua-duanya dan tidak belajar apa pun. Angka ramalan tidak disunting. R-175,
R-179, R-203, dan R-225 adalah SATU pola bernama KC-20 — keempatnya meleset ke
bawah; pola itu berhenti hanya ketika berkasnya dibaca ulang utuh lebih dahulu
(R-213, R-214, R-224). R-205 melahirkan aturan 53; R-211 aturan 54; R-209/R-212
aturan 55; R-216 aturan 56; R-217 aturan 57 dan KC-19; R-225 aturan 58 dan
KC-20; **R-230 aturan 59 dan KC-21**. R-206, R-210, R-218, dan R-224 TEPAT atas
pita LEBAR; ketepatan semacam itu bukan kecakapan meramal.

## Cacah baris terukur [v33] — `ukur_baris` V4

Sumber: `reports/ukur_baris.json` **V4** (blob `6f9c5420`), commit **`85079ffd`**,
run **30436915256**, kode 0. Penggugur bersih: `cacah_berkas_hilang` **0**,
`cacah_berkas_melebihi_pagar` **0**, `cacah_berkas_ada` **13 dari 13**. Definisi
`len(teks.splitlines())`, PERSIS definisi pagar 800 di `tests/test_kontinuitas.py`.

| berkas | baris | byte |
| --- | ---: | ---: |
| `funding.py` | **705** | 28.121 |
| `silang_funding.py` V2 | **705** | 29.873 |
| `kohort_ekor.py` | 553 | 22.590 |
| `kehidupan_arsip.py` | 496 | 19.281 |
| `kehidupan.py` | 417 | 16.638 |
| `lubang_tengah.py` V1 | **390** | 15.883 |
| `pulihkan.py` V2 | 383 | 14.839 |
| `ukur_baris.py` V4 | **280** | 13.354 |
| `gerbang_1m.py` | 184 | 6.775 |
| `funding_cdn.py` | 162 | 6.335 |
| `arsip.py` | 154 | 5.231 |
| `resample.py` | 127 | 4.356 |
| `kohort_ringkas.py` | 82 | 2.882 |

Total **4.638** baris (dihitung ulang tangan ✅); terbesar **705, SERI** antara
`funding.py` dan `silang_funding.py` — masing-masing 95 baris di bawah pagar.
**Aturan 48 berlaku atas KEDUANYA:** tidak ada fungsi baru yang boleh
ditambahkan sebelum dipecah.

**BELUM DIUKUR [v34]:** `lubang_tengah.py` **V2** (tiga fungsi lebih banyak
daripada 390 baris V1) dan berkas ujinya (56 fungsi). Tidak diramalkan dengan
pita sempit — aturan 58 pilihan (c).

**Angka kedaluwarsa yang kini MATI:** `ukur_baris.py` 183 (v29) dan 226 (v31)
BATAL → **280**. `silang_funding.py` **396 BATAL** → **705**. `pulihkan.py` 318
BATAL → 383. `lubang_tengah.py` 390 berlaku hanya untuk **V1**.

## Definisi `jumlah_baris` — TERSELESAIKAN [v26], DITEGAKKAN DI KODE [v28]

**`jumlah_baris` di manifes = baris lolos gerbang + baris karantina.** Terbukti
pada keenam pecahan yang punya karantina: `selisih_baris_total` = 0 dan
`selisih_baris_utama` = −(baris karantina). Pecahan 2 dan 5 tidak dapat
membedakan (aturan 46).

- Baris lolos gerbang saja: **839.325.999** — DIKUATKAN oleh pengukuran kedua
  yang berdiri sendiri (jumlah `lilin_penuh` kedelapan pecahan).
- Baris karantina: **516.135** · Jumlah: **839.842.134** = angka semesta.

Konsekuensi untuk ADR-A007: 839.842.134 SUDAH memuat 516.135 baris cacat. Baris
hasil pemulihan harian tidak boleh dijumlahkan tanpa lebih dulu mengurangi baris
karantina yang digantikannya.

**Peringatan membaca laporan:** `reports/pulihkan_pecahan_<i>.json` di git masih
HASIL V1; label keliru pada pecahan 2 dan 5 masih terbaca di sana. Cocokkan
`versi_pulihkan` dan `sidik_kode` sebelum mempercayainya.

## Serapan semesta `perpetual_usdt` — TERUKUR, TERPERSISTENSI, TERPULIHKAN

Sumber serapan: run **`30396803601`**, commit `57a04f1e`, `versi_pecahan` **6**,
`sidik_kode` **`237ccf42…`**, `sidik_data` `6128fbb0…`.
Sumber pemulihan: run **`30404071324`**, commit `ab4e0774`, `versi_pulihkan` 1.

| i | simbol | simbol-bulan | baris (total) | baris lolos | baris karantina | menit hilang | anggota utama | bagian | tar kar | byte terunduh |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 99 | 2.411 | 103.264.917 | 103.134.312 | 130.605 | 1.875 | 2.408 | 3 | 1 | 4.128.204.800 |
| 1 | 99 | 2.468 | 105.765.980 | 105.634.220 | 131.760 | 2.160 | 2.465 | 3 | 1 | 4.277.565.440 |
| 2 | 99 | 2.337 | 100.058.416 | 100.058.416 | 0 | 0 | 2.337 | 3 | — | 3.838.976.000 |
| 3 | 98 | 2.154 | 91.884.319 | 91.841.734 | 42.585 | 615 | 2.153 | 2 | 1 | 3.386.542.080 |
| 4 | 98 | 2.497 | 106.865.397 | 106.821.807 | 43.590 | 1.050 | 2.496 | 3 | 1 | 4.204.800.000 |
| 5 | 98 | 2.741 | 117.671.896 | 117.671.896 | 0 | 0 | 2.741 | 3 | — | 4.578.979.840 |
| 6 | 98 | 2.652 | 114.013.851 | 113.890.221 | 123.630 | 7.200 | 2.649 | 3 | 1 | 4.459.048.960 |
| 7 | 98 | 2.338 | 100.317.358 | 100.273.393 | 43.965 | 675 | 2.337 | 3 | 1 | 3.880.632.320 |

- Simbol **787**; simbol-bulan **19.598**; baris **839.842.134**; slot
  **839.855.709**; menit hilang **13.575**.
- Gerbang: lolos **19.586**, gagal **12**, `persen_lolos` **99,9388**.
- Zip **26.532.925.083 B**; parquet **32.706.262.375 B**; nisbah **1,2327**;
  parquet karantina **13.247.705 B**.
- Kelas risiko: pra_header 1.952, bulan_awal_2020_2021 1.889, terhenti 587,
  non_ascii **19**, kendali_baru 10.007.
- **Pemulihan:** 29/29 aset hadir, 29/29 sha cocok, 839.842.134 baris terbaca
  ulang oleh pyarrow. Tag rilis: `serapan-pecahan-<i>-30396803601`.
- **Penyebut ganda LENGKAP [v30]:** PENUH 19.586 lolos gerbang (19.598 termasuk
  karantina); TANPA MATI **18.185**; LAYAK BACKTEST (HIDUP saja) **18.087**.
  **[v34] Catatan tajam:** ke-18.087 itu memuat keenam bulan 2026 LITUSDT dan
  MENOLAK kelima bulan 2025-07..-11 nya — bukti bahwa penyaringan per
  SIMBOL-BULAN (ADR-A008 Keputusan 2–5) benar oleh contoh, bukan hanya oleh
  selera.

## Funding semesta — TERUKUR (`funding.py` V6)

Run FUNDING 6 `30412188715`, commit `ba37c5d5`, kode 0.
`sidik_kode` `d3854823…`, `sidik_data` `6128fbb0…` (tak berubah sejak V1).

- 880 bulan klines tanpa funding; 87 funding tanpa klines; penyebut 19.598.
- Bentuk lubang: {awal 48, ekor 826, tengah 6, hilang 880}. 116 simbol berlubang
  ekor (14,74% dari 787).
- **Kohort puncak 2025-07: 38 simbol, 456 simbol-bulan**, `seri` false; 456 =
  51,8% dari seluruh 880 lubang. Ke-456 simbol-bulan itu MATI.
- `uji_cdn`: 10 kohort menjawab **404**, 10 kendali menjawab **200** dengan
  checksum cocok, byte kendali 529–1.939.
- Pembagian 880 menurut status [v31]: 842 MATI + 2 SEPI + 33 HIDUP + 3 di luar
  penyebut = 880 ✅
- Pembagian 880 menurut BENTUK, dua definisi berdampingan [v32]: terbitan
  `funding.py` {awal 48, ekor 826, tengah 6}; `bentuk_lubang_lokal` atas 877
  {awal 45, ekor 826, tengah 6}; selisih 3 = BNXUSDT 2022-04, -06, -08 ✅
- **Ketiga bentuk terjelaskan calon [v33–v34]:** 33 dari 48 lubang AWAL = pasar
  HIDUP yang funding-nya menyusul (H-A010 MENANG, definisi TEPAT); 826 EKOR =
  kematian pasar; 6 TENGAH = dua rentetan pada BTCSTUSDT dan LITUSDT, dan pada
  LITUSDT terbukti **jeda yang berakhir dengan kebangkitan** (H-A011 MENANG).
  Sisa 15 lubang awal jatuh pada bulan MATI atau SEPI.
- **`per_simbol` memuat 10 medan** dan TIDAK memuat `bulan_funding_pertama`;
  `funding_tanpa_klines` ADA dan **sudah dipakai [v34]** — kosong pada kelima
  simbol H-A010.

## Kohort ekor — kematian bertahap lawan tebing serempak [v27]

`kohort_ekor.py` V4 (`73ca4eb2…0fcda`, run `30416845475`, commit `387037a9`,
kode 0): pindaian ADAPTIF, pagu keras 60 bulan, pagu tak pernah tersentuh.
`kohort_ekor.bagian` MEMBULATKAN ke empat desimal — sifat yang melahirkan aturan
53; TIDAK diubah (aturan 29).

| simbol | bulan hidup terakhir | simbol | bulan hidup terakhir |
| --- | --- | --- | --- |
| AGIXUSDT | 2024-06 | BLZUSDT | 2024-12 |
| ALPACAUSDT | 2025-04 | BNXUSDT | 2025-03 |
| AMBUSDT | 2025-02 | BONDUSDT | 2024-11 |
| BADGERUSDT | 2025-03 | COMBOUSDT | 2025-03 |
| BALUSDT | 2025-03 | DARUSDT | 2024-12 |

Kesepuluhnya berhenti SEBELUM tebing funding 2025-07, tersebar pada sembilan
bulan berbeda — tebing funding lebih menyerupai perubahan rezim PENERBITAN.
Yang TIDAK dibuktikan: (a) 28 anggota sisanya (aturan 20); (b) arsip funding
TIDAK terbukti cacat — **ADR-A002 §10 tidak boleh diubah atas bukti kohort
semata.** Catatan [v32]: BNXUSDT ada di kedua daftar; definisi wajib dicocokkan
sebelum dijumlahkan (aturan 36).

**DIKOREKSI [v34]:** `bangkit_kembali` 0 pada laporan ini TIDAK berarti tidak ada
kebangkitan. `cacah_simbol_bangkit_dapat_diuji` = **0**, jadi nol itu batas alat
ukur; LITUSDT membuktikan gejalanya ADA. Setiap pemakaian angka "nol
kebangkitan" di dokumen mana pun BATAL (aturan 46, 51, 59).

## Jumlah uji

**396 TERVERIFIKASI [v34]** — `reports/ci_terakhir.json` (blob `50a145de`) run
**30440471598**, commit `be5cd877`, `kode_keluar` **0**, "396 tests collected in
0.45s". Sebelumnya 382 pada run **30437620711** (commit `a9e91bcd`, blob
`3a1cdcdc`) dan pada run **30436915256** (commit `85079ffd`, blob `1c313a8d`).
Riwayat: 231 → 234 → 236 → 239 → 241 → 244 → 253 → 269 → 291 → 316 → 340 →
382 → 382 → **396**.
`tests/test_lubang_tengah.py` **V2 menyumbang 56 butir** (56 fungsi `def test_`,
nol `parametrize`, dicacah BERNOMOR sebelum push — aturan 57): 382 − 42 + 56 =
**396** ✅ `tests/test_silang_funding.py` menyumbang 49 butir (v32).

## Utang verifikasi

1-5 dan 11 menunggu tahap juri/klasifikasi. 6-23, 25-28 LUNAS.

24. **AKTIF.**
    - persistensi data lolos dan karantina: **LUNAS**;
    - pemulihan aset di luar runner: **LUNAS** (run `30404071324`);
    - perbaikan aturan 46 di `pulihkan.py`: **LUNAS DI KODE** (V2) — laporan
      pecahan di git masih hasil V1;
    - cacah baris `pulihkan.py` V2: **LUNAS** (383);
    - bentangan penuh KC-18 atas 456 simbol-bulan kohort: **LUNAS**;
    - pengukur kehidupan atas SEMESTA: **LUNAS [v30]**;
    - penyebut kedua atas semesta: **LUNAS [v30]**;
    - cacah baris `kehidupan_arsip.py` dan `silang_funding.py` V1: **LUNAS [v31]**;
    - daftar 33 HIDUP tanpa funding: **LUNAS [v32]**;
    - daftar 3 lubang funding di luar penyebut: **LUNAS [v32]**;
    - medan baris laporan kehidupan: **LUNAS [v32]** (14 medan);
    - nama keenam lubang TENGAH: **LUNAS [v33]**;
    - uji H-A010: **LUNAS [v33]** — MENANG 5–0;
    - cacah baris `silang_funding.py` V2 dan `lubang_tengah.py` V1: **LUNAS [v33]**;
    - medan `per_simbol` funding: **LUNAS [v33]** — 10 medan;
    - **`funding_tanpa_klines` bagi kelima simbol H-A010: LUNAS [v34]** — kosong
      5/5, definisi turunan R-223 TEPAT;
    - **status kehidupan LITUSDT 2026-01..2026-06 (H-A011): LUNAS [v34]** —
      keenamnya HIDUP, MENANG 6–0;
    - **salah tulis "simbal" pada `lubang_tengah.py`: LUNAS [v34]** — diperbaiki
      di V2 dan dijaga oleh uji yang menuntut "simbal" tidak ada di `definisi`;
    - **cacah baris `lubang_tengah.py` V2 dan berkas ujinya: BELUM [v34]**;
    - **status BTCSTUSDT 2022-02..2026-06: BELUM [v34]** — apakah lubang
      tengahnya juga kebangkitan; murah, tanpa unduhan;
    - **pindaian kebangkitan SELURUH semesta (H-A012): BELUM [v34]**;
    - **pemecahan `silang_funding.py` (705 baris, aturan 48): BELUM [v33]**;
    - cacat penulisan docstring R-225 ("tujuh fungsi" lalu menyebut sembilan
      nama): dicatat, TIDAK disunting; jumlah yang benar sembilan;
    - pencocokan 3 lubang BNXUSDT dengan 12 simbol-bulan karantina: BELUM;
    - kehidupan 12 simbol-bulan karantina: BELUM (tar terpisah);
    - jalur **funding**: `funding_ada` masih null di seluruh manifes — BELUM;
    - medan `dugaan_pengganti` (ADR-A005) — BELUM;
    - pemulihan harian ADR-A007 — BELUM, bahan baku sudah ada;
    - karantina artefak 7 hari — BELUM;
    - 28 anggota kohort yang belum disampel `kohort_ekor` — BELUM (kini lebih
      penting: kebangkitan terbukti ada, jadi `bulan_hidup_terakhir` mereka bisa
      keliru sebagai "akhir").
    Mengadjudikasi R-7, R-19, R-20, R-28, R-36, R-37.

## Daftar ADR

- ADR-A001 aturan dasar. DITERIMA.
- ADR-A002 serapan. DITERIMA; §3 DIAMANDEMEN oleh ADR-A004 lalu ADR-A007;
  §9 DIGANTI oleh ADR-A006 Keputusan 3. **§10 belum disentuh dan [v34] makin
  kuat alasannya untuk tidak disentuh:** ketiga bentuk lubang kini punya
  penjelasan calon yang TIDAK menuduh arsip funding cacat — pada LITUSDT funding
  hilang lalu pulih BERSAMA perdagangannya, persis seperti arsip yang jujur.
- ADR-A003 taksonomi rezim. BELUM ADA (nomor dicadangkan). **[v34] Kebangkitan
  terukur menyentuh langsung nomor ini.**
- ADR-A004 kebijakan KC-6. DITERIMA.
- ADR-A005 jenis instrumen tahap pertama. DITERIMA.
- ADR-A006 karantina + persistensi. DITERIMA, DITERAPKAN, TERVERIFIKASI DARI
  LUAR.
- **ADR-A007 serapan hibrida. DIUSULKAN**, belum diterima. Wajib memperhitungkan
  temuan `jumlah_baris` dan kendala R-146.
- **ADR-A008 akibat KC-18. DITERIMA [v28] untuk Keputusan 1–6**; Keputusan 2–4
  TERTERAP atas SELURUH semesta [v30]; Keputusan 5 bersemesta bernama **18.087**
  dan kini **terbukti benar oleh contoh [v34]** (LITUSDT menyeberang status di
  dalam satu simbol). **Keputusan 7: prasyarat BENTUK TERPENUHI [v33] dan
  bahannya lengkap [v34]** — H-A010 MENANG dengan definisi TEPAT, H-A011 MENANG
  6–0. Keputusannya sendiri BELUM diambil; wajib menyebut bahwa bentuk TENGAH
  dapat menandai jeda yang berakhir, bukan hanya akhir. Klausa gugur §6 diperiksa
  dan **tidak aktif** pada seluruh run, termasuk `lubang_tengah` V2.
- ADR berikutnya **A009**.

## Temuan sampingan yang belum diukur

- **Apakah BTCSTUSDT 2022-01 sejenis LITUSDT** — status 2022-02..2026-06 lewat
  `status_rentang`; satu pemanggilan, tanpa unduhan.
- **Berapa banyak kebangkitan di seluruh semesta (H-A012)** — pola MATI→HIDUP
  per simbol atas kedelapan laporan kehidupan.
- Sebab kembalinya funding LITUSDT pada 2026-01 (di luar jangkauan arsip).
- **Apakah 3 lubang BNXUSDT (2022-04, -06, -08) sama dengan 3 simbol-bulan
  KC-15** — keduanya BNXUSDT 2022 dan keduanya bercacah 3; kebetulan yang
  mencurigakan dan wajib dicocokkan, bukan diasumsikan.
- Sebaran 1.401 MATI menurut TAHUN dan menurut SIMBOL (`baris_mati` lengkap;
  belum dibaca).
- Kehidupan 12 simbol-bulan karantina.
- Pindaian `bulan_hidup_terakhir` bagi 28 anggota kohort di luar sampel abjad.
- 15 `SETTLED` lain: apakah punya pendahulu seperti SXPUSDT?
- Daftar `INDEKS` hanya tiga nama, disusun manual.
- Saham dan komoditas token masih terhitung `perpetual_usdt`.
- `.decode("utf-8","replace")` di `klines` membungkam byte rusak.
- Apakah BUSD/USDC layak digabung dengan USDT.
- Sisa 16 simbol non-ASCII belum diuji langsung (3 sudah).
- Sebab KC-14 (H-A004) tidak dapat diuji. Sebab KC-15 tidak diketahui.
- Selisih penyebut diagnosa KC-15: 38 diperiksa, 41 dirancang.
- `reports/funding_selisih_penuh.json` belum pernah dibaca; `daftar_terpotong`
  masih true (500 dari 880).
- Selisih byte funding AGIXUSDT 531 lawan 529.
- `waktu_utc` runner berjalan lebih dulu daripada jam sesi.
- `tests/test_pulihkan.py` belum pernah dibaca ulang sesudah push.
