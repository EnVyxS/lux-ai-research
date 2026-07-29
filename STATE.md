# STATE — versi 33

Diperbarui: 2026-07-29 (sesi 54, lanjutan). Aturan hanya BERTAMBAH; jangan
menulis ulang dari ingatan. v33 disusun di atas teks v32 yang dibaca langsung
dari `main` (blob `83fc9590`), ditambah jurnal 87 (`3ecf08cf`, blob `33a9a360`)
dan jurnal 88 (`0c7c8e39`, blob `2cfb0a0a`), laporan `reports/lubang_tengah.json`
(blob **`247a04cf`**, dibaca UTUH), `reports/lubang_tengah_status.json` (blob
`70407e91`), `reports/ukur_baris.json` V4 (blob **`6f9c5420`**, dibaca UTUH),
serta empat run yang dicocokkan commit-nya: **30435672616** (`8b397622`, CI 340),
**30436334383** (`680d04b4`, CI **382**), **30436334434** (`680d04b4`,
lubang_tengah V1), dan **30436915256** (`85079ffd`, CI 382 + ukur_baris V4).
Semuanya kode 0.

Peristiwa terbesar sejak v32: **keempat bentuk lubang funding kini punya
penjelasan calon.** Keenam lubang TENGAH disebut namanya, H-A010 diuji dan
MENANG, dan `silang_funding.py` ternyata 705 baris sehingga aturan 48 kini
menyentuh berkas KEDUA.

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
    **Ditaati pada R-198, R-200, R-204, R-205, R-208, R-215, R-220, R-221, dan
    R-226.** Dilanggar pada R-211 [v31] dan R-217 [v32] — lihat aturan 54, 57,
    dan KC-19.
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
    ia dicatat sebagai bentuk terukur beserta pertanyaan yang belum diukur.
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
    `d4a2f60a`, `0929643c`, `1b0e8d8e`, `b1816ddf`, dan **`680d04b4`**
    (lubang_tengah V1: modul + uji + workflow dalam satu commit).
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
    `silang_funding` V1–V2, dan **`lubang_tengah` V1** (`cacah_tak_terukur`
    dipisah dari `cacah_gugur` pada uji H-A010).
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
    jalur V3 sudah menembus pagar sekarang.
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
    juga tidak (**3/3 BTCUSDT HIDUP dan berfunding**, `kendali_sah` true).
51. **[v27, lahir di jurnal 75]** Jendela pemindaian mundur wajib adaptif, atau
    dibuktikan mencakup peristiwa yang dicari. Jendela tetap yang seluruh isinya
    sepi menghasilkan null, bukan jawaban. **Ditaati pada kohort_ekor V4.**
52. **[v27, lahir di jurnal 75]** Laporan yang tidak dapat dibaca utuh setara
    dengan laporan yang tidak ada. Setiap pelapor besar wajib berpasangan dengan
    keluaran ringkas yang memuat sidik berkas sumbernya. Ditaati oleh
    `kohort_ringkas`, `ukur_baris`, `kehidupan`, `kehidupan_arsip`,
    `silang_funding`, dan **`lubang_tengah`** (laporan penuh + berkas status).
    **Diperkuat [v32]:** V2 menerbitkan `reports/hidup_tanpa_funding.json` yang
    memuat kedua daftar bernama dan memang terbaca utuh, sedangkan laporan penuh
    183.963 B tetap tak terbaca utuh selamanya.
53. **[v30, lahir dari R-205] Ramalan kode keluar sebuah run yang gerbangnya
    adalah berkas uji wajib didahului pembacaan PERILAKU setiap fungsi yang
    diuji, bukan hanya namanya.** Lahir dari R-205: uji menuntut
    `bagian_volume_nol` sama dengan 2/3 penuh, sedangkan `kohort_ekor.bagian`
    MEMBULATKAN ke empat desimal dan mengembalikan 0,6667 — CI keluar dengan
    kode 1 karena harapan uji, bukan karena modulnya. Ramalan berkepala dua yang
    separuhnya salah diadjudikasi SEPARUH, bukan MELESET. **Ditaati pada R-211,
    R-215, R-217, R-221, R-222, dan R-226** (kode keluar 0 benar pada semuanya).
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
    menyalakan CI. **Ditaati pada R-217, R-221, dan R-226.**
56. **[v32, lahir dari R-216] Ramalan yang menyebut sebuah commit sebagai
    sasaran wajib menyebut sasaran yang keberadaannya dijamin oleh cara kerja
    saya sendiri.** Bentuk yang sah: "commit BERIKUTNYA yang menyentuh
    `<berkas>`". Bentuk yang dilarang: menyebut satu commit yang memuat DUA
    berkas atau lebih, kecuali push-nya memang atomik dan dirancang atomik sejak
    ramalan ditulis (aturan 45). Lahir dari R-216. **Ditaati pada R-217, R-220,
    R-221, dan R-226.**
57. **[v32, lahir dari R-217] Sebelum meramalkan cacah butir uji, nama setiap
    fungsi `def test_` WAJIB ditulis BERNOMOR di jurnal atau docstring, dan
    nomor terakhirnya dipakai sebagai cacahan.** Ramalan cacah butir tanpa
    daftar bernomor yang tersurat DILARANG. Lahir dari R-217 (ditulis 42 fungsi
    / 44 butir, nyatanya **47** fungsi / **49** butir). **TERBUKTI BEKERJA
    [v33]:** R-221 menulis 42 nama BERNOMOR pada berkas terbitan, meramalkan
    340 + 42 = **382**, dan CI mengumpulkan tepat 382.
58. **[v33, lahir dari R-225] Cacah baris sebuah berkas yang versi terkininya
    belum dibaca ulang UTUH dalam giliran yang sama DILARANG diramalkan dengan
    pita sempit.** Pilih salah satu: (a) baca ulang utuh dulu, lalu ramalkan;
    (b) pakai pita yang batas atasnya sekurang-kurangnya **1,8 kali** batas
    bawah; atau (c) jangan meramalkan sama sekali dan cukup ukur. Lahir dari
    R-225: pita 470..620 atas `silang_funding.py` V2 yang nyatanya **705**.
    Menambah 30 persen ke taksiran sudah terbukti tidak cukup. Lihat KC-20.

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
    menit pun hilang. Gerbang 1m meloloskan keenamnya. Pada rentetan LITUSDT,
    funding berhenti 2025-06 lalu KEMBALI 2026-01 sementara klines tak pernah
    putus.
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
  sama. Penangkalnya aturan 57 (daftar bernomor tersurat). **TIDAK TERULANG
  [v33]:** R-221 tepat pada percobaan pertama sesudah aturan 57 ditaati.
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

## Keenam lubang funding TENGAH — BERNAMA [v33]

Sumber: `lux_ai/serapan/lubang_tengah.py` **V1** (blob `c2046bce`, **390 baris**,
`sidik_kode`
**`ebdf0b1c68420662d349d9e03daa750574e327f971bc81551889776c575925e4`**), didorong
ATOMIK bersama uji dan workflow pada commit **`680d04b4`** (aturan 45). Run
**30436334434**, kode 0. `reports/lubang_tengah.json` (blob **`247a04cf`**)
dibaca **UTUH**. Bahan: kedelapan `reports/kehidupan_arsip_<i>.json` +
`reports/funding_semesta.json`; tanpa jaringan. Definisi bentuk lubang TETAP
satu, dipakai dari `silang_funding` (aturan 36).

Penggugur bersih: `selisih_lubang_tengah` **0**, `sidik_seragam` true,
`cacah_lubang_funding` **880**, `cacah_baris_dengan_medan` **19.586**,
`penyebut_kehidupan` **19.586**, `kendali_sah` **true** (BTCUSDT 2021-05,
2021-08, 2021-01 — ketiganya HIDUP dan berfunding).

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

**Yang BOLEH disimpulkan.** "Enam lubang tengah" adalah enam SIMBOL-BULAN dalam
**DUA** rentetan, bukan enam peristiwa — satu bulan yatim pada BTCSTUSDT dan satu
rentetan lima bulan pada LITUSDT. Keenamnya MATI, dan keenamnya berklines penuh
secara bentuk. Jadi bentuk TENGAH = jeda penerbitan funding pada pasar mati yang
klines-nya tetap terbit.

**Yang TIDAK BOLEH disimpulkan (aturan 10, 20).** Ini tidak membuktikan Binance
menghentikan funding karena pasarnya mati, dan TIDAK membuktikan pasar LITUSDT
hidup kembali pada 2026-01. Sebab kembalinya funding LITUSDT **belum diukur sama
sekali**; dugaan delisting-lalu-relisting tetap DUGAAN. ADR-A002 §10 tetap tidak
disunting.

**Ketiga bentuk kini punya penjelasan calon:** ekor = kematian pasar (lubang →
mati 96,0%); awal = funding menyusul klines (H-A010 MENANG); tengah = jeda
penerbitan pada pasar mati. Prasyarat BENTUK bagi Keputusan 7 ADR-A008 terpenuhi;
keputusannya sendiri belum diambil.

## H-A010 — DIUJI dan MENANG [v33]

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

**BATAS yang diakui tersurat.** `funding_semesta.json.per_simbol` memuat
**10 medan** dan TIDAK memuat `bulan_funding_pertama`:
`bentuk_lubang`, `bulan_funding_terakhir`, `bulan_klines_terakhir`,
`cacah_bulan_funding`, `cacah_bulan_klines`, `funding_tanpa_klines`,
`jarak_bulan_terakhir`, `klines_tanpa_funding`, `mulai_lubang_ekor`, `simbol`
(787 baris). Karena itu "berfunding pertama" di atas adalah definisi TURUNAN,
bukan medan terbitan.

**Jalan menguatkan atau MENGGUGURKAN tanpa unduhan [utang baru]:** medan
`funding_tanpa_klines` ADA dan belum dipakai. Bila kelima simbol itu
`funding_tanpa_klines`-nya kosong, tidak ada bulan funding sebelum klines dan
definisi lokal tadi TEPAT, bukan hanya memadai. Bila salah satunya berisi,
kemenangan R-223 wajib ditinjau ulang.

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
- **H-A010 [v32 lahir, v33 DIUJI] — penerbitan funding MENYUSUL penerbitan
  klines bagi sebagian simbol. MENANG 5–0** dengan batas tersurat (definisi
  "berfunding pertama" turunan, sebab `bulan_funding_pertama` tidak diterbitkan).
  Peninjauan wajib bila `funding_tanpa_klines` salah satu dari kelima simbol itu
  ternyata berisi.
- **H-A011 [v33, LAHIR, BELUM DIUJI] — jeda funding TENGAH menandai pasar yang
  berhenti diperdagangkan lalu terdaftar ulang.** Dasar: LITUSDT kehilangan
  funding 2025-07..2025-11 lalu memperolehnya kembali 2026-01, sementara klines
  terbit penuh sepanjang jeda dan status kehidupannya MATI. Uji yang diperlukan:
  status kehidupan LITUSDT pada 2026-01..2026-06 — bila HIDUP kembali, hipotesis
  menguat; bila tetap MATI padahal funding terbit, ia GUGUR dan yang tersisa
  hanya pernyataan tentang penerbitan, bukan tentang perdagangan. Bahan sudah
  ada di `reports/kehidupan_arsip_<i>.json`; tanpa unduhan.

## Papan skor prediksi

R-1..R-120 dirinci v23. R-121..R-149 di v26 dan jurnal 56–63. R-150..R-193 di
jurnal 64–75. R-194..R-199 di jurnal 76–78. R-200..R-204 di jurnal 79–81.
R-205..R-208 di docstring `0929643c` dan `dceb1009`. R-209 di jurnal 82.
R-210..R-211 di docstring `1b0e8d8e`. R-212 di jurnal 83. R-213..R-215 di
docstring `67ec2be4`. R-216 di jurnal 84. R-217..R-219 di docstring `b1816ddf`.
R-220 di jurnal 86. **R-221..R-223 di docstring commit `680d04b4`.**
**R-224..R-226 di docstring commit `85079ffd`.**

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

**Total R-1..R-226** (aturan 21): TEPAT **158**; MELESET **41**; SEPARUH **13**;
TIDAK TERADJUDIKASI **7**; MENUNGGU **7** (R-7, R-19, R-20, R-28, R-36, R-37,
R-199). 158+41 = 199; +13 = 212; +7 = 219; +7 = **226** ✅ Ramalan berikutnya
**R-227**. N_percobaan = 0.

Catatan kejujuran: R-175, R-179, R-203, dan R-225 adalah SATU pola yang kini
bernama KC-20 — keempatnya meleset ke bawah. Pola itu berhenti hanya ketika
berkasnya dibaca ulang utuh lebih dahulu (R-213, R-214, R-224). R-205
melahirkan aturan 53; R-211 aturan 54; R-209/R-212 aturan 55; R-216 aturan 56;
R-217 aturan 57 dan KC-19; **R-225 aturan 58 dan KC-20**. R-206, R-210, R-218,
dan R-224 TEPAT atas pita LEBAR; ketepatan semacam itu bukan kecakapan meramal.
R-221 adalah kemenangan yang PANTAS dicatat: aturan 57 ditaati, 42 nama bernomor,
cacahnya tepat pada percobaan pertama.

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

**Angka kedaluwarsa yang kini MATI:** `ukur_baris.py` 183 (v29) dan 226 (v31)
BATAL → **280**. `silang_funding.py` **396 BATAL** → **705**. `pulihkan.py` 318
BATAL → 383. Semuanya digantikan oleh laporan V4, bukan oleh taksiran.

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
- **Ketiga bentuk kini terjelaskan calon [v33]:** 33 dari 48 lubang AWAL = pasar
  HIDUP yang funding-nya menyusul (H-A010 MENANG); 826 EKOR = kematian pasar;
  6 TENGAH = dua rentetan pada BTCSTUSDT dan LITUSDT, keduanya MATI berklines
  penuh. Sisa 15 lubang awal jatuh pada bulan MATI atau SEPI.
- **`per_simbol` memuat 10 medan** dan TIDAK memuat `bulan_funding_pertama`;
  `funding_tanpa_klines` ADA dan belum dipakai.

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
Yang TIDAK dibuktikan: (a) 28 anggota sisanya (aturan 20); (b)
`cacah_simbol_bangkit_dapat_diuji` 0; (c) arsip funding TIDAK terbukti cacat —
**ADR-A002 §10 tidak boleh diubah atas bukti kohort semata.** Catatan [v32]:
BNXUSDT ada di kedua daftar; definisi wajib dicocokkan sebelum dijumlahkan
(aturan 36).

## Jumlah uji

**382 TERVERIFIKASI [v33]** — `reports/ci_terakhir.json` (blob `1c313a8d`) run
**30436915256**, commit `85079ffd`, `kode_keluar` **0**, "382 tests collected in
0.33s". Sebelumnya 382 juga pada run **30436334383** (commit `680d04b4`, blob
`9abff629`).
Riwayat: 231 → 234 → 236 → 239 → 241 → 244 → 253 → 269 → 291 → 316 → 340 →
**382**.
`tests/test_lubang_tengah.py` menyumbang **42** butir (42 fungsi `def test_`, nol
`parametrize`, dicacah BERNOMOR sebelum push — aturan 57): 340 + 42 = 382 ✅
`tests/test_silang_funding.py` menyumbang 49 butir (v32).

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
    - **nama keenam lubang TENGAH: LUNAS [v33]** — BTCSTUSDT 2022-01 dan LITUSDT
      2025-07..-11, dua rentetan, keenamnya MATI berklines penuh;
    - **uji H-A010: LUNAS [v33]** — MENANG 5–0, dengan batas tersurat;
    - **cacah baris `silang_funding.py` V2 dan `lubang_tengah.py`: LUNAS [v33]**
      — 705 dan 390, terukur `ukur_baris` V4;
    - **medan `per_simbol` funding: LUNAS [v33]** — 10 medan, tanpa
      `bulan_funding_pertama`;
    - **`funding_tanpa_klines` bagi kelima simbol H-A010: BELUM [v33]** — jalan
      sah menguatkan atau MENGGUGURKAN R-223, tanpa unduhan;
    - **status kehidupan LITUSDT 2026-01..2026-06 (H-A011): BELUM [v33]**;
    - **pemecahan `silang_funding.py` (705 baris, aturan 48): BELUM [v33]**;
    - **salah tulis "simbal" pada `lubang_tengah.py`: BELUM [v33]** — sengaja
      ditunda ke V2 modul itu supaya `sidik_kode` tidak berubah di atas laporan
      yang sudah diadjudikasi;
    - **cacat penulisan docstring R-225** ("tujuh fungsi" lalu menyebut sembilan
      nama): dicatat, TIDAK disunting — teks praregistrasi yang sudah didorong
      tidak dirapikan belakangan; jumlah yang benar sembilan;
    - pencocokan 3 lubang BNXUSDT dengan 12 simbol-bulan karantina: BELUM;
    - kehidupan 12 simbol-bulan karantina: BELUM (tar terpisah);
    - jalur **funding**: `funding_ada` masih null di seluruh manifes — BELUM;
    - medan `dugaan_pengganti` (ADR-A005) — BELUM;
    - pemulihan harian ADR-A007 — BELUM, bahan baku sudah ada;
    - karantina artefak 7 hari — BELUM;
    - 28 anggota kohort yang belum disampel `kohort_ekor` — BELUM (kini mungkin
      dijawab dari laporan kehidupan semesta).
    Mengadjudikasi R-7, R-19, R-20, R-28, R-36, R-37.

## Daftar ADR

- ADR-A001 aturan dasar. DITERIMA.
- ADR-A002 serapan. DITERIMA; §3 DIAMANDEMEN oleh ADR-A004 lalu ADR-A007;
  §9 DIGANTI oleh ADR-A006 Keputusan 3. **§10 belum disentuh dan [v33] tetap
  tidak boleh disentuh:** ketiga bentuk lubang kini punya penjelasan calon yang
  TIDAK menuduh arsip funding cacat — itu MENGURANGI alasan mengubah §10.
- ADR-A003 taksonomi rezim. BELUM ADA (nomor dicadangkan).
- ADR-A004 kebijakan KC-6. DITERIMA.
- ADR-A005 jenis instrumen tahap pertama. DITERIMA.
- ADR-A006 karantina + persistensi. DITERIMA, DITERAPKAN, TERVERIFIKASI DARI
  LUAR.
- **ADR-A007 serapan hibrida. DIUSULKAN**, belum diterima. Wajib memperhitungkan
  temuan `jumlah_baris` dan kendala R-146.
- **ADR-A008 akibat KC-18. DITERIMA [v28] untuk Keputusan 1–6**; Keputusan 2–4
  TERTERAP atas SELURUH semesta [v30]; Keputusan 5 bersemesta bernama **18.087**.
  **Keputusan 7 [v33]: prasyarat BENTUK kini TERPENUHI** — keempat bentuk lubang
  (awal, ekor, tengah, seluruh=0) sudah bernama dan berpenjelasan calon.
  Keputusannya sendiri BELUM diambil dan wajib memuat batas H-A010 serta status
  H-A011 yang belum diuji. Klausa gugur §6 diperiksa dan **tidak aktif** pada
  seluruh run, termasuk run `lubang_tengah`.
- ADR berikutnya **A009**.

## Temuan sampingan yang belum diukur

- **`funding_tanpa_klines` bagi ICP, TLM, BNX, JUP, QTUM** — penguat atau
  penggugur R-223; bahan sudah ada di `funding_semesta.json`.
- **Sebab kembalinya funding LITUSDT pada 2026-01** (H-A011) — dan apakah
  BTCSTUSDT 2022-01 sejenis atau lain sama sekali.
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
