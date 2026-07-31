# STATE — versi 61 (bagian 1 dari tiga)

Diperbarui: 2026-07-31 (UTC). Aturan hanya BERTAMBAH; jangan menulis ulang dari ingatan.
v61 disusun di atas `STATE.md` v60 (blob
**`d3f1448fad4ead804be59b1bbb1562b460f01621`**, commit
**`8345668e9a8f0e01bcbe86fd9d0f60f4709fd834`**), yang **DIBACA UTUH pada giliran ini
sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43).

**BERKAS INI SENGAJA PADAT.** Aturan 1–90 dan KC-1..KC-57 **dirujuk ke blob v60, BUKAN
disalin ulang**. Alasannya bukan kemalasan melainkan **kesalahan dokumen butir 19**
yang lahir pada giliran ini: sebuah berkas akar terdorong dalam keadaan **terpotong**
karena disusun ulang seutuhnya dari konteks terpakai. Penangkalnya ditaati **pada
giliran yang sama ia ditulis**.

**Apa yang v61 kerjakan, tersurat:**

1. **Memulihkan keserasian trio akar** — pecah sejak v57, kini **SERASI PENUH**.
2. **Menyalin papan skor 329** dari EKOR v19, satu-satunya sumber sah.
3. **Membuka kesalahan dokumen butir 19** dan kelas cacat **pemotongan oleh PENYUSUN**.
4. Mencatat **aturan 38 ke-64, ke-65, ke-66** dan satu laporan CI yang **tertimpa**.
5. Mengusulkan **aturan 91 dan 92**; melahirkan **utang ukur 25 dan 26**, **utang
   verifikasi 47**.

**Kalimat yang wajib dibaca lebih dulu.** v60 menulis bahwa bentuk cacat paling
memalukan adalah riset yang salah membaca tabel yang ditulisnya sendiri. v61 menambah
bentuk yang lebih telanjang lagi: **riset yang mendorong separuh berkas dan tidak
diberi tahu oleh apa pun.** Alat melaporkan **berhasil**. SHA sah. Setiap kalimat yang
ada di dalamnya **benar**. Yang salah adalah **yang tidak ada**. Satu-satunya yang
menangkapnya adalah **aturan 52** — pembacaan ulang utuh pada giliran yang sama.

## KESERASIAN VERSI — PULIH PENUH untuk pertama kalinya sejak v56

1. `STATE.md` **v61** — berkas ini. Aturan 1–81, 83–87, 90; KC-1..KC-55 resmi,
   **KC-56, KC-57, KC-58 diusulkan**. Papan skor **329**.
2. `STATE_LAMPIRAN_EKOR.md` **v19** — blob
   **`e19c5573966d835e9d40eadcb55165ab7d79f0de`**, commit
   **`b8877a2710544723ce81fc44ad505fa08fb7828b`**. Kepala "milik STATE v60". Papan skor
   **329 — DISAHKAN DI SANA**.
3. `STATE_LAMPIRAN_UKUR.md` **v19** — blob
   **`47df297d146697749643019d0bda216c5a88059a`**, commit
   **`9d159e1edb6bfff58bb643409c3b86b8a9cd661d`**. Kepala "milik STATE v60". **Dorongan
   KEDUA**; dorongan pertama terpotong (butir 19).
4. `STATE_LAMPIRAN_ADR.md` (`a02ef271`) dan **`PROMPT_KELANJUTAN.md`** (`35beed44`) —
   **arsip; BUKAN sumber** (ADR-A018 kep. 9).

**KETIDAKSERASIAN YANG DITUTUP OLEH BERKAS INI.** Sejak EKOR v19, papan skor sah
adalah **329** sementara `STATE.md` v60 masih memuat **325**. Berkas ini **menyalin
329** dan ketidakserasian itu **LUNAS**.

**Sisa ketidakserasian yang TIDAK material dan TIDAK berpura-pura ditutup:** kepala
EKOR v19 dan UKUR v19 berbunyi **"milik STATE v60"**, bukan v61. Itu **penamaan**, bukan
pertentangan isi. Tidak satu angka, aturan, larangan, atau vonis pun berbeda antara
ketiganya. **Penaikan kepala ke "milik STATE v61" ditunda ke EKOR v20 / UKUR v20** dan
dicatat di sini sebagai **utang penamaan**, bukan sebagai keserasian palsu.

**KC-41 tetap penuh:** berkas SUMBER menang. Untuk **papan skor**, sumbernya **EKOR**.
Berkas ini **menyalin**, tidak mengesahkan.

**Tentang push berkas ini:** ia di akar repo sehingga menyalakan `ci.yml`. Tidak satu
pun `tests/**` berubah → cacah uji tetap **1377**; ramalan **deterministik, MUDAH**,
TIDAK diskor. Laporannya WAJIB dibaca sebelum push akar berikutnya (aturan 38,
pemakaian **ke-67**) dan **WAJIB DITOLAK bila medan `commit` tidak cocok** (aturan 90).

## STATE DIPECAH TIGA — BACA INI LEBIH DULU

1. **`STATE.md`** (berkas ini) — aturan bernomor, kelas cacat, larangan aktif, angka
   semesta, penomoran.
2. **`STATE_LAMPIRAN_EKOR.md`** — papan skor per ramalan, catatan kejujuran, utang
   verifikasi, daftar ADR.
3. **`STATE_LAMPIRAN_UKUR.md`** — pengukuran, modul, workflow, uji, API, hipotesis,
   koreksi bernomor, utang ukur.

**Ketiga berkas wajib dibaca bersama.** LANGKAH 0 PROMPT wajib menyebut ketiganya.

## BAGIAN YANG DIRUJUK KE v60, BUKAN DISALIN

Sah dikutip dari blob v60 **`d3f1448fad4ead804be59b1bbb1562b460f01621`**, **tidak
berubah isinya**:

- **Teks penuh aturan 1–81, 83, 84, 85, 86 (a/b), 87, 90** dan usulan 77, 78, 82, 88, 89.
- **Teks penuh KC-1..KC-55 resmi** dan usulan **KC-56**, **KC-57** (termasuk tabel lima
  simbol butir 18 dan alasan ia sengaja tidak diresmikan).
- **Kesalahan dokumen butir 1–18** dengan seluruh uraiannya.
- **Tabel aturan 38 ke-59..ke-63** dan dua cacat lama (ke-38 tanpa blob; run
  `30547842823` tertimpa).
- **Pembacaan `reports/lubang_awal.json`** dan baris BNXUSDT verbatim.
- **Adjudikasi R-317** (2 TEPAT / 2 MELESET) dengan tabel lima butirnya.
- **Berkas akar — status hidup/mati, 5 dari 5.**
- **Sidik yang tercatat resmi** dan **peringatan dini aturan 48**.

**Merujuk BUKAN menghapus.** Bila berkas ini bertentangan dengan v60 pada bagian yang
dirujuk, **v60 menang** dan pertentangan itu wajib dicatat sebagai kesalahan dokumen baru.

## KESALAHAN DOKUMEN SENDIRI — kini SEMBILAN BELAS

Butir 1–17 LUNAS (teks di v58/v59). Butir 18 LUNAS di v60, disalin ke UKUR v19 sebagai
Koreksi 16.

| # | berkas | tertulis | seharusnya | status |
| --- | --- | --- | --- | --- |
| 18 | tabel H-A010 di lampiran UKUR | kolom akhir dibaca sebagai `akhir_lubang_awal` | kolom itu batas **EKSKLUSIF** | LUNAS di v60 |
| **19** | **`STATE_LAMPIRAN_UKUR.md` v19, dorongan pertama** | **berkas utuh** | **berkas berhenti di tengah kalimat; separuh ekornya tidak ada** | **LUNAS pada giliran ini** |

### Butir 19 — berkas akar terdorong dalam keadaan TERPOTONG

**Kejadian, angka telanjang.** UKUR v19 didorong sebagai commit
**`c28202df1ad4ec4abb791df37da10c9c41890670`**, blob
**`40e450b65cf9f5f068f3af7380711a0dd214646d`**. Berkas berhenti di tengah kalimat,
verbatim:

> *"Ramalan yang butir-butirnya diturunkan dari **satu arit"*

**Yang hilang:** sisa usulan aturan 91 · catatan kejujuran atas usulan 88/89/91 ·
**seluruh daftar utang ukur** · **bagian penomoran berikutnya** · **syarat kumulatif
praregistrasi R-319**.

**Sebab, disebut telanjang:** **batas panjang penulisan penyusun** — bukan galat alat,
bukan galat modul, bukan galat GitHub. `push_files` menulis ulang **seluruh** berkas,
sehingga berkas yang terpotong di sumbernya terdorong dalam keadaan itu. **Push
dilaporkan BERHASIL tanpa satu pun peringatan.**

**Pemulihan:** UKUR v19 didorong ulang **PADAT** — bagian warisan dirujuk ke blob v18 —
sebagai commit **`9d159e1edb6bfff58bb643409c3b86b8a9cd661d`**, blob
**`47df297d146697749643019d0bda216c5a88059a`**, dan **dibaca ulang UTUH sampai penanda
penutupnya sendiri** (aturan 52 ke-35).

### KELAS CACAT — PEMOTONGAN OLEH PENYUSUN

| kelas | siapa memotong | apakah berteriak | penangkal |
| --- | --- | --- | --- |
| pemotongan ALAT | alat baca | **YA**, verbatim `truncated (showing NN%)` | membaca peringatan |
| pemotongan MODUL | kode penulis laporan | **TIDAK** | aturan 86 (b) — baca kode lebih dulu |
| **pemotongan PENYUSUN [BARU v61]** | **penyusun berkas** | **TIDAK** | **aturan 52 — baca ulang utuh** |

**PENANGKAL WAJIB SEJAK v61.** Berkas akar yang diperkirakan melampaui **~25 KB** WAJIB
disusun dengan **bagian warisan DIRUJUK ke blob versi sebelumnya**, bukan disalin ulang.
Menyalin ulang berkas besar dari konteks terpakai adalah **KC-42 yang dijalankan**, bukan
KC-42 yang dihindari. **Berkas ini adalah penerapan pertama penangkal itu.**

**Bacaan yang membalik catatan v60 sendiri.** v60 melarang menulis bahwa aturan 52
menjaga mutu penalaran atas dokumen; yang dijaganya **kesetiaan salinan**. Butir 19
adalah **pembuktian paling murni** atas kalimat itu: cacat kesetiaan salinan paling
telanjang yang mungkin — separuh berkas hilang — dan aturan 52 menangkapnya pada
percobaan pertama. **Batas aturan 52 dipersempit, dan di dalam batas itu nilainya
terbukti mutlak.**

**UTANG VERIFIKASI 47 LAHIR:** memastikan tidak ada berkas akar **lain** yang pernah
terdorong terpotong tanpa tertangkap. **Sampai diperiksa, DILARANG menyatakan butir 19
sebagai kejadian tunggal.**

### Akibat kedua butir 19 — satu laporan CI TERTIMPA

Push `c28202df` **menyalakan CI**, dan laporannya **tertimpa oleh push `9d159e1e`
sebelum sempat dibaca**. Ini kelas yang sama dengan run **30547842823** (bot
`de2fc03d`). **Laporan itu DILARANG dihitung dalam deret aturan 38.** Ia **tidak**
memutus deret — yang diputus hanyalah bila push akar berikutnya didorong tanpa membaca,
dan itu tidak terjadi.

## PAPAN SKOR — 329, DISALIN DARI EKOR v19

**Aturan 21 (dihitung tangan). LAJUR BERGERAK KEDUA KALINYA BERTURUT.**

TEPAT **227** · MELESET **63** · SEPARUH **22** · TIDAK TERADJUDIKASI **10** ·
MENUNGGU **7**.

Aritmetika tangan, terbuka: 227 + 63 = 290; 290 + 22 = 312; 312 + 10 = 322;
322 + 7 = **329**. Jalur kedua: 325 + 4 = **329** ✅

**Perubahan dari 325:** TEPAT **+4**, seluruh lajur lain **tidak berubah**. Sumbernya
**R-318, empat butir berskor, SEMUANYA TEPAT**.

Nisbah atas **312** ramalan beradjudikasi penuh: **72,8 / 20,2 / 7,1%**
(v18: 72,7 / 20,1 / 7,2). N_percobaan = 0.

**ADJUDIKASI RISET TETAP TERKUNCI.** MENUNGGU: R-7, R-19, R-20, R-28, R-36, R-37,
R-199 — tidak berubah.

**Peringatan yang wajib melekat pada nisbah.** Kenaikan 72,7 → 72,8 **DILARANG dibaca
sebagai kalibrasi membaik** (KC-51). Empat kemenangan R-318 **berkorelasi** — tiga di
antaranya turun dari **satu** aritmetika (bentangan 50; 50 − 48 = 2). Itulah dasar
usulan aturan 91 di bawah.

## R-318 — ADJUDIKASI, EMPAT TEPAT

Praregistrasi `journal/2026-07-31-150.md` (blob
**`2e55ee54e85d556b1a84d328c146f0d446eb87fe`**, commit `6894b02f`); adjudikasi
`journal/2026-07-31-151.md` (blob **`5680804d257bc8ff1f6508a050ba1ae1ba672ea8`**, commit
`06d62085`). **Giliran berbeda — ADR-A016 dan aturan 85 terpenuhi.**

Bahan: `reports/bulan_absen_ringkas.json` (blob
**`e450d9f95e9bca0dc28a0e01c6aad6594c4fa3d6`**), dibuka **sesudah** modul penulisnya
`lux_ai/serapan/bulan_absen.py` (blob **`10279d721d66a86b6d265badf81ada3204648f69`**)
dibaca UTUH (aturan 86 b) dan **sesudah** keenam syarat gugur diperiksa — **tak satu pun
menyala**.

**TEMUAN POKOK, TERUKUR.** Dari **787** simbol hanya **10** punya bulan absen,
berjumlah **11** bulan, **`sebaran_pembeda` = `gagal_gerbang` 11 / `tak_diterbitkan_arsip`
0 / `tak_terukur` 0**. Untuk pertama kalinya sebuah kelas lubang punya **mekanisme
bernama**, bukan sekadar bentuk.

**BNXUSDT: `bulan_absen` = 2022-06 dan 2022-08**, `rentang` **50**,
`cacah_bulan_lolos` **48**. Satu-satunya simbol berbulan-absen lebih dari satu, dan
satu-satunya yang bulan absennya **bukan** bulan settled terakhirnya.

**Jembatan tertutup tanpa sisa:** 51 − 50 = **1** (tepi 2022-04) · 50 − 48 = **2**
(di dalam: 2022-06, 2022-08) · 51 − 48 = **3** ✅, sama dengan
`cacah_lubang_tak_dikenal` **dan bernama sama persis**. Silang mandiri dari laporan
berbeda: rentetan lubang awal 9 − 7 = **2** ✅

**Aturan 29 ditaati keras.** Blok `uji_r288` di dalam laporan menyatakan vonisnya
sendiri (butir 1 dan 3 kalah, butir 2 menang, `r288_menang` false). **Papan skor tidak
disentuh untuk R-288** (KC-49). R-288 dan R-290 tetap **belum diadjudikasi**.

**KOREKSI ATAS PRAREGISTRASI SENDIRI.** Jurnal 150 §4 menduga `cacah_absen_bnx` = 3
akan memberi KC-52 bukti keras. Terukur **2**. Dugaan itu **DIBATALKAN TERTULIS**.
Angka 3 adalah **`R288_BNX_ABSEN`, tetapan ramalan di dalam kode**, bukan pengukuran
laporan kedua. **DILARANG mengutip selisih 3 lawan 2 sebagai bukti KC-52.**

## Aturan bernomor — hanya yang bergerak di v61

Teks penuh seluruh aturan ada di v60 (`d3f1448f…`). Yang dicatat di sini **hanya
perubahan status**.

**Aturan 21.** Papan skor **329**; aritmetika di atas.

**Aturan 29. [v61] Ditaati keras dua kali** — vonis `uji_r288` tidak diskor; kekalahan
butir 3 R-317 **TIDAK dibatalkan** sekalipun sebabnya kini bernama (butir 18).

**Aturan 36. [v61] TIDAK mendapat kasus keempat.** Kecocokan 3 = 3, 6 = 6, 51 = 51
tidak dimasukkan: yang menutup jembatan adalah **aritmetika di dalam satu simbol**,
bukan sebaran lintas simbol.

**Aturan 38. [v61] Ordinal berdiri di ke-66.**

| ke- | CI | run | commit | blob | jejak |
| --- | --- | --- | --- | --- | --- |
| 63 | 1377 | 30593086004 | `51c65e2a` | `a185f32a…` | UKUR v18 |
| **64** | **1377** | **30594157668** | **`8345668e`** | **`b6835432ff25e8482781f13018c17b9f080ad510`** | **STATE v60** |
| **65** | **1377** | **30595169680** | **`b8877a27`** | **`87677ef656439ff30eb0c1a6788a5c324fdca702`** | **EKOR v19** |
| **66** | **1377** | **30607412702** | **`9d159e1e`** | **`d241b08efbc05588d5dd23d85c48415c05b25665`** | **UKUR v19 padat** |

Ke-64 `waktu_utc` **2026-07-31T00:39:46Z**, `0.48s`, bot
**`e08a0a2a12100b6b375fbafce9f7e29d90a7bf45`**; ke-65 **2026-07-31T01:01:01Z**,
`0.47s`, bot **`4bf883c433d492fa76f84707dec6320162ec61c0`**; ke-66
**2026-07-31T05:40:05Z**, `0.57s`, kode keluar **0**, bot
**`2da162ed9fe02cd58cd56cd934949fec110220d2`**.

**Panjang deret, aritmetika terbuka (butir 17):** ke-42..ke-66 → 66 − 42 = 24;
24 + 1 = **25 pembacaan berturut** tanpa laporan hangus.

**[v61] SATU LAPORAN TERTIMPA, DICATAT BUKAN DISEMBUNYIKAN:** push `c28202df` (UKUR v19
cacat) menyalakan CI dan laporannya tertimpa sebelum dibaca. **DILARANG dihitung.**
Deret **tidak** putus.

**Ke-67 lahir pada push berkas ini** dan wajib dibaca sebelum push akar berikutnya.

**Aturan 45. [v61] Ditaati** — berkas ini satu push sendiri.

**Aturan 47 (satuan cacah tersurat). [v61] Tambahan:** **"11"** bersatuan **simbol-bulan
absen di seluruh 787 simbol** · **"10"** bersatuan **simbol yang punya sekurangnya satu
bulan absen** · **"15"** bersatuan **pasangan simbol-settled** · **"50"** bersatuan
**bulan bentangan kalender BNXUSDT** · **"48"** bersatuan **bulan BNXUSDT yang ADA di
penyebut 19.586** · **"25"** pada aturan 38 bersatuan **pemakaian berjejak**.

**Aturan 52. [v61] Ditaati; ordinal berdiri di ke-35**, dan **ke-36** bila pembacaan
ulang berkas ini pada giliran yang sama ikut dihitung.

**[v61] Blob baru yang tercatat pertama kali:** `lux_ai/serapan/bulan_absen.py`
**`10279d721d66a86b6d265badf81ada3204648f69`** · `reports/bulan_absen_ringkas.json`
**`e450d9f95e9bca0dc28a0e01c6aad6594c4fa3d6`** · `journal/2026-07-31-150.md`
**`2e55ee54e85d556b1a84d328c146f0d446eb87fe`** · `journal/2026-07-31-151.md`
**`5680804d257bc8ff1f6508a050ba1ae1ba672ea8`** · `STATE.md` v60
**`d3f1448fad4ead804be59b1bbb1562b460f01621`** · `STATE_LAMPIRAN_EKOR.md` v19
**`e19c5573966d835e9d40eadcb55165ab7d79f0de`** · `STATE_LAMPIRAN_UKUR.md` v19 **cacat**
**`40e450b65cf9f5f068f3af7380711a0dd214646d`** dan v19 **padat**
**`47df297d146697749643019d0bda216c5a88059a`** · `ci_terakhir.json` ke-64
**`b6835432`**, ke-65 **`87677ef6`**, ke-66 **`d241b08e`**.

**BATAS PEMBACAAN yang tetap terbuka:** `semesta_rentang.json` **95%**;
`silang_funding.json` **54%**; daftar `reports/` **76%**; `kehidupan_arsip_0..7.json`
**MUSTAHIL dibaca utuh**; `lubang_awal.json` **dipotong MODUL** (60 dari 118).

**UTANG BACA yang TETAP hidup:** `decisions/ADR-A002`, **A004 (PERINGKAT TERTINGGI)**,
A006, A007, A008; **`tests/test_gerbang_1m.py` (peringkat NAIK)**;
`journal/2026-07-30-125.md` (praregistrasi R-305); `karantina_semesta.yml`
(`de40fa4e`); `tests/test_pulihkan.py` (`11c43533`); `test_rilis_karantina.py`
(`739c8da9`); `test_karantina_a006.py` (`a5a3d82f`); `tests/test_lubang_tengah.py`;
bagian `baris_mati` `silang_funding.json`; modul penulis `semesta_rentang.json`;
`reports/bulan_absen.json` (**249.992 B, belum dibuka**).

**Aturan 57. [v61] BERUNTUN 4 DARI 4, tidak bertambah** — tidak ada `tests/**` yang
berubah.

**Aturan 66. [v61] UTANG HIDUP.** Cacah tangan yang **dilakukan** pada giliran R-318:
`baris_berabsen` = **10** dan `baris_pasangan_settled` = **15**, keduanya cocok dengan
medan ringkasannya. Angka harapan direktori **50 / 54 / 45** tetap **TURUNAN** dan
**DILARANG dikutip terukur**.

**Aturan 79. [v61] REKOR MENJADI LIMA KALI BERTURUT** (R-314, R-315, R-316, R-317,
R-318). Aritmetika terbuka: 318 − 314 = 4; 4 + 1 = **5**. **DILARANG menyebut aturan 79
lemah, longgar, atau opsional.** **DILARANG pula** membaca rekor itu sebagai bukti mutu
**isi** ramalan — ia mencacah **ketertiban prosedur**, bukan kebenaran.

**Aturan 85. [v61] TIDAK dinaikkan cacahnya di berkas ini.** EKOR v19 mencatat **tiga**
adjudikasi; menaikkannya menjadi empat tanpa membaca ulang EKOR v19 adalah **KC-41
persis** (lajur dari ingatan). **Cacah resmi dipegang EKOR; penyesuaian ke EKOR v20.**
Yang tetap DILARANG: menyebut aturan 85 **teruji**, **bekerja**, atau **terbukti**.

**Aturan 86 (a dan b). [v61] KEDUANYA TERPAKAI, dan (b) TERBUKTI MAHAL UNTUK KEDUA
KALINYA.** `bulan_absen.py` dibaca UTUH sebelum laporannya. Satu pembacaan kode memberi
**tiga penangkal sekaligus**: (1) kepastian modul **tanpa pembatas baris** sehingga
`baris_berabsen` **lengkap** — mustahil diketahui dari laporan; (2) definisi tiap medan
**disalin verbatim** sebelum ditafsirkan; (3) pengetahuan bahwa **bulan tepi tidak
pernah dapat absen menurut definisi**, sehingga **2022-04 mustahil muncul** — dan pita
ramalan dikunci **sadar** atas dasar itu.

**Aturan 87. [v61] TERPAKAI.** Butir 4 R-318 (`rentang` = 50) ditandai **TURUNAN** di
praregistrasi dan kemenangannya **diperkecil sendiri**.

**Aturan 90. [v61] DIPAKAI EMPAT KALI SESUDAH PERESMIAN** (ke-63, ke-64, ke-65, ke-66)
dan **tidak sekali pun menangkap laporan salah**; keempatnya cocok pada percobaan
pertama. **DILARANG menyebut aturan 90 "teruji"** — aturan yang belum pernah menyala
bukan aturan yang terbukti, hanya aturan yang belum diuji.

### USULAN ATURAN 91 — DITAHAN

> **Usulan aturan 91.** Ramalan yang butir-butirnya diturunkan dari **satu aritmetika
> yang sama** wajib menyatakan hal itu di praregistrasi, dan kemenangan butir-butir itu
> **DILARANG dijumlahkan sebagai bukti bebas**.

**Dasar terukur (aturan 42):** butir 1, 3, dan 4 R-318 semuanya turun dari bentangan
**50** dan **50 − 48 = 2**. Bila aritmetika itu salah, **ketiganya jatuh bersama**. Ini
**KC-47 dalam bentuk paling menggoda: satu perhitungan menyamar sebagai banyak ramalan**.

**TIDAK diresmikan:** **satu** kejadian (ADR-A019 kep. 3).

### USULAN ATURAN 92 — DITAHAN

> **Usulan aturan 92.** Setiap push berkas akar wajib diikuti pembacaan ulang utuh pada
> giliran yang sama, dan berkas yang terbaca **tidak berakhir pada penanda penutupnya
> sendiri** WAJIB didorong ulang sebelum pekerjaan lain apa pun.

**Dasar:** butir 19. **TIDAK diresmikan:** **satu** kejadian; dan bagian pertamanya toh
sudah dijamin aturan 52. Yang benar-benar baru hanyalah **penanda penutup wajib** —
berkas ini memakainya.

**Penomoran aturan [v61].** Aturan resmi: **1–81, 83, 84, 85, 86 (a dan b), 87, 90**.
Nomor **82** dicadangkan; **77, 78, 88, 89, 91, 92** usulan. **Aturan berikutnya yang
bebas: 93.**

### CATATAN KEJUJURAN ATAS USULAN YANG MENUMPUK

**Enam usulan aturan menganggur bersamaan** (77, 78, 88, 89, 91, 92) ditambah **tiga
usulan KC** (56, 57, 58). **Menumpuknya usulan BUKAN tanda kedisiplinan otomatis** — ia
dapat menjadi cara halus menunda keputusan sambil tampak berhati-hati. **ADR-A022 WAJIB
memutuskan seluruhnya**, meresmikan atau membuang. Membiarkannya menggantung satu ADR
lagi **wajib dicatat sebagai cacat proses**.

## Kelas cacat — hanya yang bergerak

KC-1..KC-55 resmi; teks penuh di v60 dan berkas rujukannya. **KC-16 tetap kosong
selamanya.**

**KC-47. [v61] Menjadi kerabat butir 19 dan usulan 91.** Bentuk barunya: **satu
perhitungan menyamar sebagai banyak ramalan**.

**KC-49. [v61] TERPAKAI** — `uji_r288` tidak diperlakukan sebagai adjudikasi.

**KC-51. [v61] TERBALIK UNTUK PERTAMA KALINYA.** Sepanjang riwayat, taksiran pemusatan
cenderung **bias ke bawah**. Pada R-318 sebaliknya: satu pita meramalkan **7** sementara
terukur **19** — dicatat di EKOR v19. **Satu pembalikan bukan sebaran; DILARANG dibaca
sebagai kalibrasi membaik.**

**KC-52. [v61] SEBAGIAN TERDAMAIKAN, TIDAK DICABUT.** Untuk **BNXUSDT** ketiga angka
48 / 50 / 51 konsisten dan ketiga bulannya **bernama**. Untuk **786 simbol lain**
keanggotaan penyebut **belum diukur**. **Kesamaan cacah bukan kesamaan identitas.**

**KC-53. [v61] DITANGKAL PREVENTIF.** Nol pada `tak_diterbitkan_arsip` dan `tak_terukur`
**TIDAK** dibaca sebagai "arsip selalu menerbitkan". Yang terukur: **dari 11 bulan
absen, tak satu pun bersebab itu.**

**KC-54. [v61] TETAP TIGA KEJADIAN**, ditangkal **preventif** untuk kedua kalinya
berturut.

**KC-55. [v61] Tidak bertambah** — pita R-318 menutup tiga sisi.

**KC-56, KC-57 — TETAP DIUSULKAN, tidak bertambah.** Kedua laporan baru **bertanggal**,
sehingga KC-56 tidak terpicu. Teks penuh di v59 dan v60.

**KC-58 — DIUSULKAN, DITAHAN.** Rumusan penuhnya hidup di **EKOR v19**
(`e19c5573…`) dan **SENGAJA tidak disalin ke sini** — menyalinnya dari ingatan adalah
KC-41. Yang dicatat di berkas ini hanya statusnya: **satu kejadian, TIDAK diresmikan**,
dan bahannya adalah **utang verifikasi 46**.

**Kelas cacat berikutnya: KC-59.**

## Larangan aktif — jangan dilanggar

**[v61] SATU LARANGAN DICABUT SEBAGIAN.** Larangan v60 **"DILARANG menamai kedua bulan
absen BNXUSDT"** — **DICABUT**. Keduanya kini **terukur dan sah disebut: 2022-06 dan
2022-08**. **YANG TIDAK DICABUT:** larangan mengklaim **SEBABNYA** di luar apa yang
ditulis medan `pembeda_absen`.

- **[v61] DILARANG menyatakan klausa mana** dari enam klausa `gerbang_1m.py` yang
  menjatuhkan BNXUSDT 2022-06 dan 2022-08 (**utang ukur 25**).
- **[v61] DILARANG menyatakan butir 19 sebagai kejadian tunggal** sebelum utang
  verifikasi 47 dibayar.
- **[v61] DILARANG menyatakan trio akar serasi pada KEPALA berkas** — EKOR v19 dan
  UKUR v19 masih berkepala "milik STATE v60". Serasi pada **isi**, belum pada **nama**.
- **[v61] DILARANG mengutip selisih 3 lawan 2 sebagai bukti KC-52** — 3 adalah tetapan
  ramalan `R288_BNX_ABSEN` di dalam kode.
- **[v61] DILARANG menyimpulkan bahwa hanya simbol berpasangan settled yang berabsen**
  — **5 dari 15** pasangan berabsen **nol**.
- **[v61] DILARANG menjumlahkan kemenangan butir 1, 3, 4 R-318 sebagai tiga bukti
  bebas** (usulan 91).
- **[v61] DILARANG menghitung laporan CI push `c28202df`** — tertimpa sebelum dibaca.
- **[v61] DILARANG menyebut aturan 90 "teruji"** — empat pemakaian, nol nyala.
- **[v61] DILARANG meresmikan KC-56, KC-57, KC-58, atau aturan 88, 89, 91, 92** sebelum
  kejadian kedua yang bebas.
- DILARANG menarik cacah, sebaran, atau daftar apa pun dari `baris_penyebut_butir_1`
  — 60 dari 118, sampel abjad, bukan populasi.
- DILARANG mengutip tabel H-A010 di lampiran sebagai `akhir_lubang_awal` (butir 18).
- DILARANG memakai vonis `uji_r305` atau `uji_r288` sebagai adjudikasi (KC-49).
- DILARANG menulis **H-A023 sebagai TERBUKTI**.
- DILARANG memperlakukan `semesta_rentang.json` sebagai terbaca utuh (95%) dan DILARANG
  membandingkan angkanya tanpa menyebut ia **TAK BERTANGGAL** (KC-56).
- DILARANG memindahkan sifat medan `cacah_bulan` ↔ `bulan_per_simbol` (KC-23, KC-52).
- DILARANG menyamakan "tidak ada di penyebut" dengan "dijatuhkan gerbang" **di luar**
  medan `pembeda_absen` untuk sebelas bulan itu.
- DILARANG menulis panjang deret tanpa aritmetika `akhir − awal + 1` (butir 17).
- DILARANG menulis vonis R-315 butir 2, atau R-317 butir 3 dan 4, sebagai SEPARUH.
  Ketiganya **kalah penuh**.
- DILARANG mengklaim cacah total baris `baris_mati` sebagai terukur (terpotong 54%).
- DILARANG membuka `reports/kehidupan_arsip_*.json` dengan harapan membacanya utuh.
- DILARANG membaca `lubang_tak_dikenal` sebagai "bulan sebelum simbol lahir"
  (ADR-A021 kep. 2).
- DILARANG menggeneralisasi pola BNXUSDT ke 786 simbol lain (**utang ukur 26**, KC-47).
- DILARANG menyebut lubang tengah berada pada gugus `2022-05` atau `2024-05`.
- DILARANG menyamakan 787 simbol funding dengan 787 simbol klines.
- DILARANG menyebut aturan 85 "teruji"; DILARANG menyebut aturan 79 lemah; DILARANG
  membaca rekor aturan 79 sebagai bukti mutu isi.
- DILARANG menuduh isi sebuah berkas tanpa membacanya ulang.
- DILARANG menulis bahwa aturan 52 menjaga mutu penalaran ATAS DOKUMEN; yang dijaganya
  **kesetiaan salinan** — dan **[v61]** di dalam wilayah itu ia **tidak tergantikan**.
- **712.925 DILARANG jadi penyebut** (KC-50). Frasa "sembilan pemeriksaan bebas"
  DILARANG. Cacah direktori turunan **50/54/45** DILARANG dikutip terukur. Menyebut
  "cacah uji" tanpa menyebut repo-nya DILARANG. `PROMPT_KELANJUTAN.md` DILARANG dipakai
  sebagai sumber. Kelima larangan permanen R-312 berlaku penuh. Bot CI deterministik
  dan DILARANG dihitung sebagai kemenangan. Lajur papan skor DILARANG dikarang tanpa
  membaca STATE. Besar berkas DILARANG jadi detektor status. DILARANG menyebut *jenis*
  instrumen yang dikarantina.

## Angka semesta yang mengikat

Penyebut **19.586** · rilis penuh **19.598** = 19.586 + **12** karantina ·
`cacah_simbol` **787** · bukan-pertama **18.799** · HIDUP **18.087** · SEPI **98** ·
MATI **1.401** (penuh 1.392 / tak penuh 9; kohort 456 + luar kohort 945; luar kohort
berlubang 386, berfunding 559; `bagian_mati_luar_kohort_dengan_lubang_funding` 0,4085) ·
`defisit_total` **18.143.601** · `defisit_pertama` **17.335.439** (95,5%) ·
`defisit_bukan_pertama` **808.162** · `defisit_sembilan` **95.237** · sisa **712.925** ·
calon **17.398** = 17.284 penuh + **114** berdefisit · `defisit_terbesar` **42.510**
(TLMUSDT 2023-03; 2.130/44.640 = **95,2% kosong**) · baris parquet lolos gerbang
**839.325.999** · karantina **516.135** · rilis penuh **839.842.134** · total byte
**32.706.262.375** · `byte_mati` **579.041.399** · bulan pertama HIDUP 769 + SEPI 18 =
**787** ✅ · lubang funding **880** semesta / **877** dalam penyebut / **3** tak dikenal ·
`sebaran_bentuk_semua_lubang` 45/826/0/6 = **877** · `bentuk_terbitan_funding` 48/826/6 =
**880** · `tabel_silang` HIDUP 18.054/33, MATI 559/842, SEPI 96/2, TAK_TERUKUR 0/0 ·
`cacah_hidup_tanpa_funding` **33** (BNXUSDT 7 · ICPUSDT 13 · JUPUSDT 1 · QTUMUSDT 1 ·
TLMUSDT 11) · `cacah_simbol_ada_lubang` **122** · jumlah uji **1377** (repo riset ini).

Silang yang menutup: 18.087 + 98 + 1.401 = **19.586** ✅ · 18.799 − 1.401 = **17.398** ✅ ·
33 + 842 + 2 = **877**, + 3 = **880** ✅ · 839.325.999 + 516.135 = **839.842.134** ✅ ·
19.586 + 12 = **19.598** ✅ · 95.237 + 712.925 = **808.162** ✅

### [v61] Angka BARU dari `reports/bulan_absen_ringkas.json` (2026-07-29T17:50:29Z)

`cacah_nama_berabsen` **10** dari 787 · `jumlah_bulan_absen` **11** ·
`jumlah_bulan_absen_pasangan` **11** · `jumlah_bulan_absen_luar_pasangan` **0** ·
`cacah_pasangan` **15** · `sebaran_pembeda` **11 / 0 / 0** ·
`selisih_absen_pasangan_jurnal_113` **−1** (12 tercatat vs 11 terukur) ·
`penyebut_kehidupan` **19.586** · `cacah_nama_penyebut` / `cacah_nama_didaftar`
**787 / 787** · `kendali_sah` **true** (BTCUSDT 78/0, ETHUSDT 78/0; ambang 60) ·
`penggugur_menyala` **false** · `sidik_seragam` **true** · `cacah_kunci_ganda` **0**.

Sepuluh simbol berabsen: AERGOUSDT 2025-04 · AIAUSDT 2026-01 · **BNXUSDT 2022-06 dan
2022-08** · CTKUSDT 2025-04 · CVCUSDT 2025-05 · CVXUSDT 2025-07 · LITUSDT 2025-12 ·
MAVIAUSDT 2025-03 · PUMPUSDT 2025-07 · SLPUSDT 2025-07. **Seluruhnya `gagal_gerbang`.**
Ketertutupan: 9 + 2 = **11** ✅ · 11 + 0 + 0 = **11** ✅ · 10 + 5 = **15** pasangan ✅

`absen_sama_dengan_settled` **true** untuk kesembilan simbol berabsen tunggal; **false**
untuk BNXUSDT (`bulan_settled_terakhir` **2023-02**, `settled_ada_di_absen` false).

Sidik: `bulan_absen` kode **`0294eb3a…163088`**, sumber **`d2fc3bfb…14a3bd`**,
`byte_sumber` **249.992**.

## Hipotesis — hanya yang bergerak

**H-A023 — TETAP BERSYARAT, dengan ARITMETIKA TERTUTUP.** Ketiga bulan kini **BERNAMA**:
2022-04 (tepi), 2022-06 dan 2022-08 (di dalam, `gagal_gerbang`); 51−50 = 1, 50−48 = 2,
1 + 2 = **3** ✅, dan nama itu **sama persis** dengan ketiga `lubang_tak_dikenal`.
**TETAP BERSYARAT:** keanggotaan penyebut diukur untuk **SATU** simbol. Kenaikan
v60→v61 adalah dari "aritmetika tertutup tanpa nama" menjadi "aritmetika tertutup
**dengan** nama" — **bukan** menjadi terbukti. **DILARANG ditulis TERBUKTI. TIDAK DISKOR.**

**H-A010 — MENANG 5–0**, tabel pendukungnya cacat konvensi (butir 18); **vonis tidak
berubah**. **H-A011, H-A022 — TERBUKTI**, generalisasi DILARANG. **H-A020, H-A021 —
uji MUSTAHIL.** Sisanya tanpa perubahan; teks di UKUR v19.

Hipotesis berikutnya **H-A024**.

## Penomoran berikutnya

Jurnal **152** · STATE **v62** · EKOR **v20** · UKUR **v20** · PROMPT **v55 (belum
didorong, utang SEBELAS versi)** · ADR **A022** · KC **KC-59** (KC-56, KC-57, KC-58
usulan) · aturan **93** (usulan 77, 78, 82, 88, 89, 91, 92) · hipotesis **H-A024** ·
ramalan **R-319** · **papan skor 329** · aturan 38 **ke-67** · aturan 52 **ke-36** ·
kesalahan dokumen berikutnya butir **20** · utang ukur berikutnya **27** · utang
verifikasi berikutnya **48** · berhenti eksplisit berikutnya **ke-50**.

## Utang yang lahir dari berkas ini

- **UTANG UKUR 25 [POROS PERINGKAT SATU].** Klausa mana dari enam klausa `gerbang_1m.py`
  yang menolak **BNXUSDT 2022-06** dan **2022-08**? Karena `gerbang_1m.py` **pustaka
  murni** tanpa keluaran, utang ini **TIDAK dapat dibayar dengan membaca laporan mana
  pun** — ia **menuntut pemanggilnya ditelusuri**. Bahan: **ADR-A004 §2**,
  `tests/test_gerbang_1m.py`.
- **UTANG UKUR 26.** Apakah pola BNXUSDT (bulan berberkas → gugur gerbang → keluar
  penyebut) berlaku bagi **786 simbol lain**?
- **UTANG VERIFIKASI 47.** Apakah ada berkas akar **lain** yang pernah terdorong
  terpotong tanpa tertangkap?
- **UTANG PENAMAAN.** Kepala EKOR v19 dan UKUR v19 dinaikkan ke "milik STATE v61" pada
  EKOR v20 / UKUR v20.

## ADR-A022 — WAJIB, TUJUH BUTIR

(a) peresmian **aturan 90** beserta tabel tiga kejadian dan catatan "belum pernah
menyala"; (b) **48 / 50 / 51 terdamaikan** — KC-52 diperluas atau dipersempit;
(c) status `semesta_rentang.json` yang **tak bertanggal dan tak bersidik**; (d) apakah
**KC-56 / KC-57 / KC-58** diresmikan; (e) apakah **aturan 89** diresmikan atas **manfaat
terukur** alih-alih cacat berulang — **perubahan kebijakan**; (f) apakah **aturan 91**
diresmikan; (g) **[BARU]** apakah **aturan 92** diresmikan, dan apakah **penanda penutup
wajib** pada berkas akar menjadi aturan tersendiri.

**DILARANG disusun pada giliran yang sama dengan adjudikasi mana pun** (ADR-A016).

## Prasyarat klasifikasi — SATU BLOKIR MENYEMPIT LAGI, tidak ada yang lunas

Serapan funding **matang sebagai PEMBUKUAN, belum matang sebagai LANDASAN FITUR**.

1. **ADR-A003 taksonomi rezim belum ada.**
2. **Keanggotaan penyebut — MENYEMPIT TAJAM.** 48 / 50 / 51 terdamaikan **dan ketiga
   bulan BERNAMA** untuk BNXUSDT; **786 simbol lain belum diperiksa** (utang ukur 26).
3. **`baris_mati` terpotong 54%.**
4. **Kelas positif tipis** — 33 dari lima simbol (KC-47).
5. **Irisan 787 lawan 787 belum didamaikan** (KC-52).
6. **Taksonomi lubang MULAI BERGERAK dari BENTUK ke MEKANISME** — sebelas bulan absen
   kini punya mekanisme bernama (`gagal_gerbang`). **Belum lunas:** mekanisme itu baru
   **nama pembeda**, bukan **klausa** (utang ukur 25).

## Syarat praregistrasi R-319 — LIMA BELAS SYARAT KUMULATIF

Seluruhnya WAJIB; daftar penuh dengan uraian ada di **UKUR v19** (`47df297d…`). Ringkas:
aturan **79** · **83** · **84** · **85** · **86 (a) dan (b)** · **87** · **90** (bila
push akar terlibat) · **66** · pemeriksaan kebebasan medan terhadap kode sumbernya ·
**KC-50, KC-52, KC-53, KC-54, KC-55, KC-56, KC-57** · **batas laporan** (bila modul
penulis memuat pembatas baris, syarat gugur tersurat WAJIB) · **[BARU v61]** bila
beberapa butir turun dari **satu aritmetika yang sama**, hal itu **dinyatakan di
praregistrasi** dan kemenangannya **DILARANG dijumlahkan sebagai bukti bebas** (usulan
aturan 91).

**Bahan R-319 DILARANG** berupa berkas yang sudah dibuka pada sesi ini:
`semesta_rentang.json`, `semesta_bulan_1m.json`, `gerbang_1m.py`, `silang_funding.json`,
`lubang_awal.json`, `bulan_absen_ringkas.json`, `lubang_awal.py`, `bulan_absen.py`.

— akhir `STATE.md` v61 —
