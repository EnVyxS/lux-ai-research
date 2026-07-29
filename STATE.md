# STATE — versi 32

Diperbarui: 2026-07-29 (sesi 54, lanjutan). Aturan hanya BERTAMBAH; jangan
menulis ulang dari ingatan. v32 disusun di atas teks v31 yang dibaca langsung
dari `main` (blob `2b4c4045`), ditambah jurnal 85 (`667d8d21`, blob `2b9370b6`)
dan jurnal 86 (`ad0d8c4e`, blob `c901fe50`), laporan
`reports/hidup_tanpa_funding.json` (blob **`a7b20503`**, dibaca UTUH), serta tiga
run yang dicocokkan commit-nya: **30434140732** (`9819d76b`, CI 316, kode 0),
**30434948267** (`b1816ddf`, silang_funding V2, kode 0), dan **30434951202**
(`b1816ddf`, CI **340**, kode 0).

Peristiwa terbesar sejak v31: **ke-33 simbol-bulan HIDUP tanpa funding sudah
disebut namanya, dan bentuknya seragam.** Ketiga puluh tiga itu SEMUANYA lubang
berbentuk AWAL — nol berbentuk ekor, nol berbentuk tengah. Kelompok yang selama
tiga versi dicurigai sebagai cacat arsip funding ternyata berperilaku seperti
funding yang MENYUSUL penerbitan klines. Yang tersisa tak terjelaskan hanyalah
**6 lubang TENGAH**.

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
    **Ditaati pada R-198, R-200, R-204, R-205, R-208, dan R-215.** **Dilanggar
    lagi pada R-211 [v31] dan R-217 [v32]** — lihat aturan 54, 57, dan KC-19.
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
    kelas cacat, sebab bentuk lubangnya justru menjelaskannya.
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
    `d4a2f60a`, `0929643c`, `1b0e8d8e`, dan **`b1816ddf`** (silang_funding V2:
    modul + uji + workflow dalam satu commit).
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
    `kehidupan` V1, `kehidupan_arsip` V1 (`penyebut_tanpa_mati_kosong`), dan
    `silang_funding` V1–V2 (`_bagian` mengembalikan null bila penyebut nol).
47. **[v27, lahir di jurnal 69]** Sebelum menulis ramalan berupa cacah,
    sebutkan satuannya secara eksplisit — simbol, bulan, simbol-bulan, baris,
    atau butir uji — dan periksa bahwa angka rujukan yang dipakai memang
    bersatuan itu. Lahir dari R-163.
48. **[v27, lahir di jurnal 71]** Berkas modul yang mendekati pagar 800 baris
    harus dipecah SEBELUM fungsi baru ditambahkan, dan setiap pemecahan wajib
    memperluas daftar berkas yang masuk `sidik_kode`.
49. **[v27, lahir di jurnal 72]** Pemecahan berkas yang mempertahankan seluruh
    nama fungsi lewat re-export TETAP dapat mematahkan uji, karena re-export
    memindahkan fungsi dan bukan modul. Telusuri juga nama yang DITAMBAL
    (`monkeypatch.setattr`, `patch`, akses atribut modul).
50. **[v27, lahir di jurnal 73]** Setiap pengukuran yang menyimpulkan dari
    KETIADAAN — volume nol, berkas hilang, baris kosong, jawaban 404 — wajib
    memuat kendali positif yang membuktikan alat ukurnya mampu mendeteksi
    KEHADIRAN pada kondisi yang sama. Dipakai sebagai klausa gugur ADR-A008 §6;
    pada run kehidupan kohort klausa itu tidak aktif (kendali 4/4), pada run
    semesta juga tidak (**kendali 24/24 hidup**), dan pada run silang funding
    juga tidak (**3/3 BTCUSDT HIDUP dan berfunding**).
51. **[v27, lahir di jurnal 75]** Jendela pemindaian mundur wajib adaptif, atau
    dibuktikan mencakup peristiwa yang dicari. Jendela tetap yang seluruh isinya
    sepi menghasilkan null, bukan jawaban. **Ditaati pada kohort_ekor V4.**
52. **[v27, lahir di jurnal 75]** Laporan yang tidak dapat dibaca utuh setara
    dengan laporan yang tidak ada. Setiap pelapor besar wajib berpasangan dengan
    keluaran ringkas yang memuat sidik berkas sumbernya. Ditaati oleh
    `kohort_ringkas`, `ukur_baris`, `kehidupan`, `kehidupan_arsip`, dan
    `silang_funding`. **Diperkuat [v32]:** V2 menerbitkan berkas ketiga
    `reports/hidup_tanpa_funding.json` yang memuat kedua daftar bernama dan
    memang terbaca utuh, sedangkan laporan penuh 183.963 B tetap tak terbaca
    utuh selamanya.
53. **[v30, lahir dari R-205] Ramalan kode keluar sebuah run yang gerbangnya
    adalah berkas uji wajib didahului pembacaan PERILAKU setiap fungsi yang
    diuji, bukan hanya namanya.** Membaca modul tidak sama dengan mengetahui
    pembulatan, pemotongan, atau normalisasi yang dilakukannya. Lahir dari
    R-205: uji menuntut `bagian_volume_nol` sama dengan 2/3 penuh, sedangkan
    `kohort_ekor.bagian` MEMBULATKAN ke empat desimal dan mengembalikan 0,6667 —
    CI keluar dengan kode 1 karena harapan uji, bukan karena modulnya. Ramalan
    berkepala dua (cacah butir DAN kode keluar) yang separuhnya salah
    diadjudikasi SEPARUH, bukan MELESET. **Ditaati pada R-211, R-215, dan
    R-217** (kode keluar 0 benar pada ketiganya; yang salah cacah butirnya).
54. **[v31, lahir dari R-211] Cacah butir uji dalam sebuah ramalan wajib
    dihitung dengan mencacah definisi `def test_` satu per satu pada berkas uji
    yang SUDAH selesai ditulis, mengalikan setiap fungsi berparameter dengan
    cacah kasusnya.** Dilarang mencacah dari ingatan rancangan. Lahir dari
    R-211: docstring saya menyebut "18 fungsi berbutir tunggal" padahal berkas
    yang saya dorong memuat **22** fungsi berbutir tunggal + 1 fungsi
    berparameter tiga kasus = **25** butir, sehingga CI mengumpulkan 316, bukan
    312. Aturan 38 mengatur SUMBER angka akhir; aturan 54 mengatur cara
    menyusun angka RAMALANNYA. Pendahulu: R-148. **TIDAK CUKUP [v32]:** R-217
    gugur walau aturan 54 saya kira sudah ditaati — lihat aturan 57 dan KC-19.
55. **[v31, lahir dari R-209 dan R-212] Sebelum meramalkan hasil sebuah
    workflow, baca `paths`/`paths-ignore` workflow itu dan sebutkan di dalam
    ramalan workflow MANA yang akan menyala pada commit yang dimaksud. Ramalan
    atas run yang tidak akan pernah menyala DILARANG.** `.github/workflows/ci.yml`
    memakai `paths-ignore` untuk `journal/**`, `decisions/**`, `hipotesis/**`,
    dan `reports/**`; karena itu commit yang hanya menyentuh jurnal TIDAK
    menyalakan CI, dan R-209 serta R-212 mustahil menang maupun kalah. Aturan 52
    menjaga dari laporan yang tak terbaca utuh; aturan 55 menjaga dari laporan
    yang tidak akan pernah ada. **Ditaati pada R-217** (disebut tersurat bahwa
    pemicunya `tests/test_silang_funding.py`).
56. **[v32, lahir dari R-216] Ramalan yang menyebut sebuah commit sebagai
    sasaran wajib menyebut sasaran yang keberadaannya dijamin oleh cara kerja
    saya sendiri.** Bentuk yang sah: "commit BERIKUTNYA yang menyentuh
    `<berkas>`". Bentuk yang dilarang: menyebut satu commit yang memuat DUA
    berkas atau lebih, kecuali push-nya memang atomik dan dirancang atomik sejak
    ramalan ditulis (aturan 45). Lahir dari R-216, yang menyebut "commit yang
    memuat STATE v31 DAN PROMPT v34" padahal keduanya saya dorong terpisah
    (`9819d76b`, `dce890eb`), sehingga commit itu tidak pernah ada. Aturan 55
    melarang meramalkan run yang tak akan menyala; aturan 56 melarang
    meramalkan run atas commit yang tak akan ada.
57. **[v32, lahir dari R-217] Sebelum meramalkan cacah butir uji, nama setiap
    fungsi `def test_` WAJIB ditulis BERNOMOR di jurnal atau docstring, dan
    nomor terakhirnya dipakai sebagai cacahan.** Ramalan cacah butir tanpa
    daftar bernomor yang tersurat DILARANG. Aturan 54 menyuruh mencacah dari
    berkas yang sudah jadi; ternyata itu masih memberi ruang untuk "mencacah di
    kepala sambil menulis", dan itulah yang menjatuhkan R-217 (ditulis 42 fungsi
    / 44 butir, nyatanya **47** fungsi / **49** butir). Daftar yang panjang
    justru pertanda cacahan kepala paling mudah salah. Lihat KC-19.

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
    dalam 1.401, sehingga **945 simbol-bulan MATI berada di luar kohort puncak**
    (angka turunan, bukan medan run). Dua pertiga kematian tak terlihat dari
    kohort funding.
  - **KEMATIAN BUKAN CACAT ARSIP FUNDING [v31].** Dari 1.401 MATI, **842**
    kehilangan funding dan **559 tetap punya funding**. Arsip menerbitkan
    funding bagi pasar yang tidak diperdagangkan sama sekali; jadi ketiadaan
    funding BUKAN penanda kematian yang perlu, hanya yang hampir cukup.
  - Ekstrapolasi dari kohort ke semesta TERBUKTI keliru arah: kohort 100% mati,
    semesta 7,15% mati. Aturan 39 dibenarkan.
  - **Kebijakan DIPUTUSKAN [v28] oleh ADR-A008** (Keputusan 1–6 DITERIMA):
    KC-18 bukan gerbang serapan; kehidupan diukur per simbol-bulan; **SEPI**
    bila `bagian_volume_nol` ≥ 0,5 dan **MATI** bila `transaksi_total` = 0;
    setiap penyebut diterbitkan berpasangan; backtest hanya pada simbol-bulan
    HIDUP; angka 839.842.134 tidak ditulis ulang (aturan 29). Keputusan 7
    DITANGGUHKAN. **Klausa gugur §6 tidak aktif** pada ketiga run.
- **KC-19 [v32, lahir dari R-217] — mencacah dari INGATAN atas berkas yang baru
  saya tulis sendiri.** R-148, R-211, dan R-217 gugur dengan sebab yang persis
  sama: angka cacah butir uji ditulis sebagai fakta padahal ia hasil cacahan di
  kepala sambil menulis berkasnya. Penangkalnya aturan 57 (daftar bernomor
  tersurat). Kelas ini BUKAN tentang pytest dan bukan tentang kode; ia tentang
  kebiasaan saya memercayai ingatan atas berkas yang panjang.

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
seluruh bila keduanya; tengah bila tidak satu pun. Kedua definisi itu BERTEMU
setelah penyebutnya disamakan:

- lokal atas 877 lubang di dalam penyebut = awal **45** + ekor **826** + tengah
  **6** + seluruh 0 = **877** ✅
- terbitan `funding.py` atas 880 = awal **48** + ekor 826 + tengah 6
- selisih 48 − 45 = **3** = ketiga lubang BNXUSDT di luar penyebut ✅

**Yang BOLEH disimpulkan.** Setiap pasar HIDUP tanpa funding kehilangan
funding-nya di AWAL riwayat klines-nya; tak satu pun di tengah, tak satu pun
sampai bulan terakhir. Bentuk itu yang diharapkan bila penerbitan funding
MENYUSUL penerbitan klines bagi simbol tersebut. Karena itu kelompok 33 ini
bukan kelas cacat (aturan 42) dan bukan bantahan bagi KC-18 maupun ADR-A002 §10.

**Yang TIDAK BOLEH disimpulkan (aturan 20).** "Funding menyusul" masih DUGAAN:
laporan ini tidak mengukur tanggal mulai penerbitan funding per simbol. Dan
ketiga lubang BNXUSDT DIDUGA anggota 12 simbol-bulan karantina — belum
dicocokkan dengan daftar karantina, jadi belum fakta.

**Medan baris laporan kehidupan, akhirnya diketahui** (`medan_baris_terlihat`, 14
medan): `ada_di_arsip`, `bagian_volume_nol`, `bulan`, `byte_parquet`,
`cacah_baris_cacat`, `cacah_lilin`, `cacah_lilin_terbaca`, `cacah_volume_nol`,
`galat`, `gerbang_lolos`, `jalur`, `simbol`, `status`, `transaksi_total`.
`cacah_baris_dengan_medan` = **19.586**, jadi `cacah_lilin` ada pada SETIAP baris.

## Silang funding × kehidupan — TERUKUR [v31]

Modul `lux_ai/serapan/silang_funding.py`: V1 (396 baris, `sidik_kode`
`259c069b…8c60`) didorong atomik pada commit **`1b0e8d8e`**; **V2** didorong
atomik pada **`b1816ddf`** (aturan 45). Tidak menyentuh jaringan: bahannya
kedelapan `reports/kehidupan_arsip_<i>.json` (`sidik_kode` seragam
`24b6bb26…c595`) dan `reports/funding_semesta.json`. Laporan penuh 183.963 B;
ringkasnya terbaca utuh dan identik dengan `reports/silang_funding.log`.

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
  semesta `funding.py` V6 ✅ Ketiganya kini BERNAMA: BNXUSDT 2022-04, -06, -08.
- Kohort puncak: **456/456** MATI dan **456/456** berlubang ✅
- Di luar kohort: 945 MATI = **386** berlubang + **559** berfunding ✅
  456 + 386 = 842 ✅ `bagian` 386/945 = **0,4085** (dibulatkan 4 desimal).

Medan penggugur bersih pada kedua versi: `sidik_seragam` true,
`cacah_laporan_dibaca` 8, `laporan_hilang` [], `cacah_kunci_ganda` 0,
`cacah_lubang_ganda` 0, `selisih_penyebut` 0, `selisih_mati` 0,
`selisih_kohort` 0, `kode_keluar` 0; V2 menambah `selisih_hidup_tanpa_funding` 0
dan `selisih_lubang_tak_dikenal` 0. Kendali positif (aturan 50): tiga
simbol-bulan berparquet terbesar — BTCUSDT 2021-05, 2021-08, 2021-01 — ketiganya
HIDUP dan berfunding, `kendali_sah` true.

**Yang BOLEH disimpulkan.** Dua arah wajib dipisah:

- lubang → mati **kuat**: 842 dari 877 lubang di dalam penyebut (**96,0%**)
  berada di bulan MATI;
- mati → lubang **lemah**: hanya 842 dari 1.401 MATI (**60,1%**) kehilangan
  funding.

Jadi kedua gejala beririsan tetapi bukan satu hal, dan lubang funding TIDAK sah
dipakai sebagai penyaring kematian — memakainya melewatkan 559 bulan mati.

**Yang TIDAK BOLEH disimpulkan.** Irisan bukan sebab (aturan 10); keduanya masih
dapat lahir dari satu delisting. Yang terukur hanya BENTUK irisannya.

**Sisa yang benar-benar mencurigakan kini tinggal 6 lubang TENGAH [v32].**
Kelompok 33 sudah terjelaskan bentuknya (semua AWAL); ketiga lubang tak dikenal
sudah bernama. Keenam lubang tengah BELUM disebut namanya dan itulah prasyarat
Keputusan 7 ADR-A008.

## Kehidupan semesta terserap — TERUKUR [v30]

Modul `lux_ai/serapan/kehidupan_arsip.py` V1 (blob `318a5cb1…`, `sidik_kode`
**`24b6bb265525e81c2e571b46e401f36903383f1e3738c487850861adc3e8c595`**), didorong
atomik bersama uji dan workflow pada commit `0929643c` (aturan 45). Delapan
runner mengunduh tar rilis `serapan-pecahan-<i>-30396803601`, membongkarnya, dan
mengukur kolom `volume` serta `trades` tiap parquet lolos gerbang. Run pecahan
0 = **30419770259**. Sidik kode SAMA di kedelapan laporan, sehingga penjumlahan
lintas pecahan sah (aturan 20, 22).

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

Uji silang (aturan 21):

- 1.401 + 98 + 18.087 = **19.586** ✅ dan jumlah penyebut = 19.586, penyebut yang
  dipraregistrasi — BUKAN 19.598 (dua belas karantina tak ada di tar ini).
- 19.586 − 1.401 = **18.185** = jumlah `penyebut_tanpa_mati` ✅
- Jumlah `lilin_penuh` **839.325.999** cocok PERSIS dengan baris lolos gerbang
  yang diukur serapan (run `30396803601`) lewat jalur kode yang sepenuhnya
  berbeda — dari zip, bukan dari parquet. Dua pengukuran independen bertemu di
  satu angka; bukti kuat bahwa seluruh isi arsip terbaca.
- Lilin mati 61.168.123 = **7,29%** dari seluruh baris; MATI + SEPI = 1.499 =
  **7,654%** dari 19.586.

Medan penggugur (aturan 24) bersih di kedelapan pecahan: `cacah_tak_terukur` 0,
`cacah_baris_cacat` **0** dari 839 juta baris teks yang diurai,
`cacah_parquet_hilang` 0, `cacah_parquet_tak_dikenal` 0, `cacah_bagian_hilang`
0, `cacah_sha_tak_cocok` 0, `cacah_anggota_tak_aman` 0, `kode_keluar` 0.
Kendali positif (aturan 50): **24 dari 24 HIDUP**, `parser_terbukti` **true**
pada kedelapan pecahan.

Yang BOLEH disimpulkan: 7,654% simbol-bulan lolos gerbang tidak layak
di-backtest tanpa penyaringan tambahan; semesta yang layak = **18.087**
simbol-bulan.
Yang TIDAK BOLEH: memakai 7,153% sebagai laju kematian simbol mana pun —
sebarannya 4,18% (pecahan 1) sampai 13,14% (pecahan 3), jarak lebih dari tiga
kali, dan pecahan dibagi menurut simbol sehingga ketidakseragaman ini sifat
pasar, bukan derau.

## Kehidupan kohort puncak 2025-07 — TERUKUR [v29]

Modul `lux_ai/serapan/kehidupan.py` V1 (blob `f49abb2b…`, 417 baris,
`sidik_kode` `c1aaf852…b4cc`). Run **30418471430**, commit `d4a2f60a`, kode 0.
Ringkasan `reports/kehidupan_ringkas.json` (1.406 B) terbaca UTUH.

| medan | nilai |
| --- | ---: |
| simbol diukur | 38 |
| simbol-bulan diminta / terukur / tak terukur | 456 / 456 / 0 |
| MATI / SEPI / HIDUP | **456** / 0 / **0** |
| MATI yang lolos gerbang | **456** |
| lilin penuh = lilin mati | **19.972.800** |
| penyebut penuh / tanpa MATI | 456 / **0** (kosong) |
| kendali diminta / terambil / hidup | 4 / 4 / **4** |

Uji silang: 38 × 525.600 = 19.972.800 ✅ dan 38 × 12 = 456 ✅
Konsekuensi: kohort puncak menyumbang **nol** simbol-bulan layak backtest.
Yang TIDAK terbukti: bahwa 38 simbol ini tak pernah diperdagangkan — kohort V4
menunjukkan sebagian hidup pada 2024–2025.

## Hipotesis

- H-A001: belum diuji.
- H-A002a / H-A002b: H-A002b **GUGUR** (`slot_5m_hadir_saat_1m_hilang` = 0).
- **H-A003: MENANG pada 3, GUGUR pada 9.**
- **H-A004: TIDAK TERUJI dan tidak dapat diuji** (`fapi.binance.com` → 451).
- **H-A005: GUGUR pada rentang yang disampel [v23]** (37 bulan tengah).
- **H-A006 — serapan bersifat deterministik. MENANG pada ENAM run.**
- **H-A008 [v26] — aset rilis GitHub mengembalikan byte yang sama persis.
  MENANG pada DUA kali pengambilan penuh** — 29 aset / 32.754.749.440 byte pada
  run pemulihan, lalu kedelapan tar diunduh ulang oleh `kehidupan_arsip` dengan
  `cacah_sha_tak_cocok` 0 dan cacah baris yang kembali persis 839.325.999.
- **H-A009 [v31, LAHIR DAN LANGSUNG DIUJI] — lubang funding dan kematian pasar
  adalah satu gejala. GUGUR:** 559 simbol-bulan MATI tetap berfunding.
- **H-A010 [v32, LAHIR, BELUM DIUJI] — penerbitan funding MENYUSUL penerbitan
  klines bagi sebagian simbol.** Dasar: ke-33 simbol-bulan HIDUP tanpa funding
  semuanya berbentuk AWAL, nol berbentuk ekor maupun tengah. Uji yang
  diperlukan: bandingkan bulan funding PERTAMA tiap simbol dengan bulan klines
  pertamanya; hipotesis MENANG bila bagi kelima simbol (ICP, TLM, BNX, JUP,
  QTUM) funding pertama datang SESUDAH klines pertama, dan GUGUR bila ada satu
  saja yang funding-nya mulai lebih dulu lalu bolong.

## Papan skor prediksi

R-1..R-120 dirinci v23. R-121..R-149 di v26 dan jurnal 56–63. R-150..R-193 di
jurnal 64–75. R-194..R-197 di jurnal 76 dan 77. R-198..R-199 di jurnal 78.
R-200 di jurnal 79. R-201 di jurnal 81. R-202..R-204 di jurnal 80.
R-205..R-207 dipraregistrasi di docstring commit `0929643c`; R-208 di docstring
commit `dceb1009`; R-209 di jurnal 82; R-210..R-211 di docstring commit
`1b0e8d8e`; R-212 di jurnal 83; R-213..R-215 di docstring commit `67ec2be4`;
R-216 di jurnal 84; **R-217..R-219 di docstring commit `b1816ddf`**.

| # | Prediksi | Status |
|---|---|---|
| R-175 | kedua berkas ≤800 baris DAN `funding.py` pita 500..680 | **SEPARUH** |
| R-179 | `funding.py` 640..700 DAN `funding_cdn.py` 140..200 | **SEPARUH** |
| R-198 | CI 253 butir, kode 0 | TEPAT |
| R-199 | `definisi_dapat_dibedakan` false pada TEPAT 2 pecahan (2 dan 5) | **MENUNGGU** |
| R-200 | CI **269 butir**, kode 0 (253 + 16) | **TEPAT** |
| R-201 | MATI pita 350..456 SIMBOL-BULAN DAN `cacah_hidup` 0 | **TEPAT** |
| R-202 | `pulihkan.py` V2 pita 340..420 BARIS | **TEPAT** (383) |
| R-203 | `kehidupan.py` pita 300..400 BARIS DAN 0 berkas lewat pagar | **MELESET** (417) |
| R-204 | CI tetap 269 butir, kode 0, pada `12dde093` | **TEPAT** |
| R-205 | CI **291 butir** (269+22) DAN kode 0 | **SEPARUH** (291 tepat, kode 1) |
| R-206 | MATI semesta pita 456..2.000 atas penyebut 19.586 | **TEPAT** (1.401) |
| R-207 | `parser_terbukti` true pada kedelapan pecahan | **TEPAT** (8/8) |
| R-208 | CI 291 butir, kode 0, pada commit perbaikan uji | **TEPAT** (`30420236800`) |
| R-209 | CI 291 butir, kode 0, pada commit jurnal 82 | **TIDAK TERADJUDIKASI** (aturan 55: CI tak menyala) |
| R-210 | MATI luar kohort berlubang funding pita 150..400 atas 945 | **TEPAT** (386) |
| R-211 | CI **312 butir** (291+21), kode 0 | **MELESET** (316; aturan 54) |
| R-212 | CI 316 butir, kode 0, pada commit jurnal 83 | **TIDAK TERADJUDIKASI** (aturan 55) |
| R-213 | `kehidupan_arsip.py` pita 250..500 BARIS | **TEPAT** (496) |
| R-214 | `silang_funding.py` pita 330..430 BARIS | **TEPAT** (396) |
| R-215 | CI 316 butir, kode 0, pada `67ec2be4` | **TEPAT** (`30433635955`) |
| R-216 | CI 316 butir, kode 0, pada commit STATE v31 + PROMPT v34 | **SEPARUH** (316/kode 0 tepat pada `9819d76b`, tetapi commit yang disebut tak pernah ada; aturan 56) |
| R-217 | CI **335 butir**, kode 0, pada commit pemicu `tests/test_silang_funding.py` | **MELESET** (340; aturan 57, KC-19) |
| R-218 | `cacah_hidup_tanpa_funding` 33 DAN bentuk awal 20..33 DAN ekor 0..3 | **TEPAT** (33; awal 33, ekor 0) |
| R-219 | ketiga lubang tak dikenal bersimbol dikenal, 3 dari 3 | **TEPAT** (BNXUSDT ×3) |

**Total R-1..R-219** (aturan 21): TEPAT **152**; MELESET **40**; SEPARUH **13**;
TIDAK TERADJUDIKASI **7**; MENUNGGU **7** (R-7, R-19, R-20, R-28, R-36, R-37,
R-199). 152+40 = 192; +13 = 205; +7 = 212; +7 = **219** ✅ Ramalan berikutnya
**R-220**. N_percobaan = 0.

Catatan kejujuran: R-175, R-179, dan R-203 adalah satu pola — menaksir panjang
berkas ketika ia dapat dihitung; pola itu berhenti pada R-213 dan R-214 karena
keduanya diukur, bukan ditaksir, dan pitanya diakui lebar (496 hanya 4 baris di
bawah batas atas — kemenangan yang tidak layak dibanggakan). R-205 melahirkan
aturan 53. R-211 melahirkan aturan 54 dan mengulang kelas kesalahan R-148;
**R-217 mengulangnya untuk KETIGA kali dan melahirkan aturan 57 serta KC-19** —
kesalahannya saya temukan sendiri sesudah push dan sebelum laporan CI terbaca,
dan angka ramalannya TIDAK disunting. R-209 dan R-212 melahirkan aturan 55;
R-216 melahirkan aturan 56. R-206, R-210, dan R-218 TEPAT atas pita LEBAR;
ketepatan semacam itu tidak boleh dibaca sebagai kecakapan meramal.

## Cacah baris terukur [v31] — SEBAGIAN KEDALUWARSA [v32]

Sumber: `reports/ukur_baris.json` **V3**, commit `67ec2be4`. Penggugur bersih:
`cacah_berkas_hilang` 0, `cacah_berkas_melebihi_pagar` 0, `cacah_berkas_ada`
**12 dari 12**. Definisi `len(teks.splitlines())`, PERSIS definisi pagar 800 di
`tests/test_kontinuitas.py`.

| berkas | baris | byte |
| --- | ---: | ---: |
| `funding.py` | **705** | 28.121 |
| `kohort_ekor.py` | 553 | 22.590 |
| `kehidupan_arsip.py` | **496** | 19.281 |
| `kehidupan.py` | **417** | 16.638 |
| `silang_funding.py` V1 | **396** (KEDALUWARSA) | 15.908 |
| `pulihkan.py` V2 | **383** | 14.839 |
| `ukur_baris.py` V3 | **226** | 10.212 |
| `gerbang_1m.py` | 184 | 6.775 |
| `funding_cdn.py` | 162 | 6.335 |
| `arsip.py` | 154 | 5.231 |
| `resample.py` | 127 | 4.356 |
| `kohort_ringkas.py` | 82 | 2.882 |

Total **3.885** baris (dihitung ulang tangan ✅); terbesar `funding.py` 705 — 95
baris di bawah pagar 800. Aturan 48 berlaku padanya: fungsi baru DILARANG
ditambahkan sebelum dipecah.

**Angka kedaluwarsa:** `ukur_baris.py` 183 baris (v29) BATAL — kini 226.
**`silang_funding.py` 396 BATAL [v32]** — V2 menambah docstring dan tujuh fungsi
baru; panjangnya BELUM diukur, dan dilarang ditaksir (pola R-175/R-179/R-203).
Jalankan `ukur_baris` lagi; bila V2 melewati 800, aturan 48 berlaku padanya.

## Definisi `jumlah_baris` — TERSELESAIKAN [v26], DITEGAKKAN DI KODE [v28]

**`jumlah_baris` di manifes = baris lolos gerbang + baris karantina.** Terbukti
pada keenam pecahan yang punya karantina: `selisih_baris_total` = 0 dan
`selisih_baris_utama` = −(baris karantina). Pecahan 2 dan 5 tidak dapat
membedakan (aturan 46).

- Baris lolos gerbang saja: **839.325.999** — kini DIKUATKAN oleh pengukuran
  kedua yang berdiri sendiri (jumlah `lilin_penuh` kedelapan pecahan).
- Baris karantina: **516.135**
- Jumlah: **839.842.134** = angka semesta.

Konsekuensi untuk ADR-A007: 839.842.134 SUDAH memuat 516.135 baris cacat. Baris
hasil pemulihan harian tidak boleh dijumlahkan tanpa lebih dulu mengurangi baris
karantina yang digantikannya.

**`pulihkan.py` VERSI 2** (commit `5c65adf9`, 383 baris) menegakkan ini lewat
fungsi murni `putuskan_definisi` dan medan `definisi_dapat_dibedakan`.

**Peringatan membaca laporan:** `reports/pulihkan_pecahan_<i>.json` di git masih
HASIL V1; label keliru pada pecahan 2 dan 5 masih terbaca di sana. Cocokkan
`versi_pulihkan` dan `sidik_kode` sebelum mempercayainya.

## Serapan semesta `perpetual_usdt` — TERUKUR, TERPERSISTENSI, TERPULIHKAN

Sumber serapan: run **`30396803601`**, commit `57a04f1e`, `versi_pecahan` **6**,
`sidik_kode` **`237ccf42…`**, `sidik_data` `6128fbb0…`.
Sumber pemulihan: run **`30404071324`**, commit `ab4e0774`, `versi_pulihkan` 1,
`sidik_kode` **`c76ff896…b38`**.

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
- **Pemulihan (run `30404071324`):** 29/29 aset hadir, 29/29 sha cocok,
  839.842.134 baris terbaca ulang oleh pyarrow.
- Tag rilis: `serapan-pecahan-<i>-30396803601`.
- **Penyebut ganda kini LENGKAP [v30]:** penyebut PENUH 19.586 simbol-bulan
  lolos gerbang (19.598 termasuk karantina); penyebut TANPA MATI **18.185**;
  penyebut LAYAK BACKTEST (HIDUP saja) **18.087**.

## Funding semesta — TERUKUR (`funding.py` V6)

Run FUNDING 6 `30412188715`, commit `ba37c5d5`, kode 0.
`sidik_kode` `d3854823…`, `sidik_data` `6128fbb0…` (tak berubah sejak V1).

- 880 bulan klines tanpa funding; 87 funding tanpa klines; penyebut 19.598.
- Bentuk lubang: {awal 48, ekor 826, tengah 6, hilang 880}. 116 simbol berlubang
  ekor (14,74% dari 787).
- **Kohort puncak 2025-07: 38 simbol, 456 simbol-bulan**, `seri` false; 456 =
  51,8% dari seluruh 880 lubang. Ke-38 anggota punya bulan klines terakhir
  2026-06 — dan terbukti ke-456 simbol-bulan itu MATI.
- `uji_cdn`: 10 kohort menjawab **404**, 10 kendali menjawab **200** dengan
  checksum cocok, byte kendali 529–1.939.
- **Pertanyaan v30 TERJAWAB [v31]:** dari 945 simbol-bulan MATI di luar kohort
  puncak, **386** juga kehilangan funding dan **559** tetap berfunding. Tebing
  funding dan kematian pasar karena itu DUA peristiwa yang beririsan, bukan
  satu. Tafsir ADR-A002 §10 tetap TIDAK diubah.
- Pembagian 880 lubang menurut status [v31]: 842 MATI + 2 SEPI + 33 HIDUP + 3 di
  luar penyebut = 880 ✅
- **Pembagian 880 menurut BENTUK, dua definisi berdampingan [v32]:** terbitan
  `funding.py` {awal 48, ekor 826, tengah 6}; `bentuk_lubang_lokal` atas 877 di
  dalam penyebut {awal 45, ekor 826, tengah 6}; selisih 3 = BNXUSDT 2022-04,
  -06, -08 ✅ Ke-33 HIDUP tanpa funding SEMUANYA berbentuk awal, sehingga 33
  dari 48 lubang awal kini terjelaskan; sisa 15 lubang awal jatuh pada bulan
  MATI atau SEPI.

## Kohort ekor — kematian bertahap lawan tebing serempak [v27]

Modul `kohort_ekor.py` V1→4 dan pelapor ringkas `kohort_ringkas.py` V1.
**V4** (`73ca4eb2…0fcda`, run `30416845475`, commit `387037a9`, kode 0):
pindaian ADAPTIF, pagu keras 60 bulan, pagu tak pernah tersentuh.
**Catatan [v30]:** `kohort_ekor.bagian` MEMBULATKAN ke empat desimal — sifat
yang melahirkan aturan 53. Pembulatan itu TIDAK diubah (aturan 29), dan
`silang_funding` V1–V2 memakainya apa adanya dengan uji tersurat 0,6667.

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
`cacah_simbol_bangkit_dapat_diuji` 0, jadi `bangkit_kembali` 0 bukan bukti;
(c) arsip funding TIDAK terbukti cacat — **ADR-A002 §10 tidak boleh diubah atas
bukti kohort semata.**

**Jalan pintas yang kini tersedia [v30]:** `reports/kehidupan_arsip_<i>.json`
memuat status per simbol-bulan bagi SELURUH semesta, sehingga
`bulan_hidup_terakhir` bagi 28 anggota sisanya mungkin dijawab tanpa unduhan
baru — dengan syarat definisi "hidup terakhir" dicocokkan lebih dulu dengan
definisi `kohort_ekor` (aturan 36). **Catatan [v32]:** BNXUSDT ada di kedua
daftar — "bulan hidup terakhir 2025-03" menurut kohort_ekor, dan 7 bulan HIDUP
tanpa funding pada 2022–2023 menurut V2. Keduanya tidak bertentangan, tetapi
itulah contoh pertama mengapa definisi wajib dicocokkan sebelum dijumlahkan.

## Jumlah uji

**340 TERVERIFIKASI [v32]** — `reports/ci_terakhir.json` run **30434951202**,
commit `b1816ddf`, `kode_keluar` **0**, "340 tests collected in 0.35s".
Riwayat: 231 → 234 → 236 → 239 → 241 → 244 → 253 → 269 → 291 → 316 → **340**.
`tests/test_silang_funding.py` kini menyumbang **49** butir (**47** fungsi
`def test_`, satu di antaranya `parametrize` tiga kasus): 316 − 25 + 49 = 340 ✅
Angka 25 butir (v31) berlaku untuk berkas uji V1 dan tidak dihapus (aturan 29).

## Utang verifikasi

1-5 dan 11 menunggu tahap juri/klasifikasi. 6-23, 25-28 LUNAS.

24. **AKTIF.**
    - persistensi data lolos dan karantina: **LUNAS**;
    - pemulihan aset di luar runner: **LUNAS** (run `30404071324`);
    - perbaikan aturan 46 di `pulihkan.py`: **LUNAS DI KODE** (V2) — laporan
      pecahan di git masih hasil V1;
    - cacah baris `pulihkan.py` V2: **LUNAS** (383);
    - bentangan penuh KC-18 atas 456 simbol-bulan kohort: **LUNAS**;
    - pengukur kehidupan atas SEMESTA: **LUNAS [v30]** — 19.586 simbol-bulan
      terukur, 0 tak terukur, kendali 24/24;
    - penyebut kedua atas semesta: **LUNAS [v30]** — 18.185 tanpa MATI, 18.087
      HIDUP;
    - cacah baris `kehidupan_arsip.py` dan `silang_funding.py` V1: **LUNAS
      [v31]** (496 dan 396);
    - funding bagi 945 MATI di luar kohort puncak: **LUNAS [v31]** — 386
      berlubang, 559 berfunding;
    - **daftar 33 simbol-bulan HIDUP tanpa funding: LUNAS [v32]** — 5 simbol,
      semuanya bentuk AWAL;
    - **daftar 3 lubang funding di luar penyebut: LUNAS [v32]** — BNXUSDT
      2022-04, -06, -08;
    - **medan baris laporan kehidupan: LUNAS [v32]** — 14 medan, `cacah_lilin`
      ada pada 19.586 baris;
    - **cacah baris `silang_funding.py` V2: BELUM [v32]** — jalankan ulang
      `ukur_baris`;
    - **nama keenam lubang TENGAH: BELUM [v32]** — prasyarat Keputusan 7;
    - **pencocokan 3 lubang BNXUSDT dengan 12 simbol-bulan karantina: BELUM
      [v32]**;
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
  §9 DIGANTI oleh ADR-A006 Keputusan 3. **§10 belum disentuh.** Bukti [v32]
  menyempitkan pertanyaannya dari 880 lubang menjadi **6 lubang TENGAH** — ke-33
  HIDUP tanpa funding sudah terjelaskan bentuknya, dan itu MENGURANGI alasan
  mengubah §10, bukan menambahnya.
- ADR-A003 taksonomi rezim. BELUM ADA (nomor dicadangkan).
- ADR-A004 kebijakan KC-6. DITERIMA.
- ADR-A005 jenis instrumen tahap pertama. DITERIMA.
- ADR-A006 karantina + persistensi. DITERIMA, DITERAPKAN, TERVERIFIKASI DARI
  LUAR.
- **ADR-A007 serapan hibrida. DIUSULKAN**, belum diterima. Wajib memperhitungkan
  temuan `jumlah_baris` dan kendala R-146.
- **ADR-A008 akibat KC-18. DITERIMA [v28] untuk Keputusan 1–6**; Keputusan 2–4
  TERTERAP dan TERJALANKAN atas SELURUH semesta [v30]. Keputusan 5 (backtest
  hanya pada HIDUP) kini punya semesta bernama: **18.087** simbol-bulan.
  Keputusan 7 DITANGGUHKAN; syaratnya kini SETENGAH terpenuhi [v32] — sifat 48
  lubang AWAL sudah terang (33 di antaranya bulan HIDUP berbentuk awal), tinggal
  **6 lubang TENGAH** yang belum disebut namanya. Klausa gugur §6 diperiksa dan
  **tidak aktif** pada seluruh run.
- ADR berikutnya **A009**.

## Temuan sampingan yang belum diukur

- **Nama keenam lubang funding TENGAH** — satu-satunya bentuk lubang yang belum
  terjelaskan; penentu Keputusan 7 ADR-A008.
- **Uji H-A010** — bulan funding pertama lawan bulan klines pertama bagi ICP,
  TLM, BNX, JUP, QTUM.
- **Apakah 3 lubang BNXUSDT (2022-04, -06, -08) sama dengan 3 simbol-bulan
  KC-15** — keduanya BNXUSDT 2022 dan keduanya bercacah 3; kebetulan yang
  mencurigakan dan wajib dicocokkan, bukan diasumsikan.
- Sebaran 1.401 MATI menurut TAHUN dan menurut SIMBOL (laporan penuh memuat
  `baris_mati` lengkap; belum dibaca).
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
