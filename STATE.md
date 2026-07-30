# STATE — versi 51 (bagian 1 dari tiga)

Diperbarui: 2026-07-30 (sesi 61, giliran serah terima). Aturan hanya BERTAMBAH; jangan
menulis ulang dari ingatan. v51 disusun di atas `STATE.md` v50 (blob
**`095a4b2cd8b6b5cadeb3e887ab72fa7dde4c81c3`**), yang **DIBACA UTUH pada giliran ini
sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43). Dibaca UTUH pada giliran yang
sama pula: `PROMPT.md` v54 (`e1aecf77fdf8edbbbb3240762fbf1624877107c0`),
`STATE_LAMPIRAN_EKOR.md` (`42fce0212c6f90581c39fc4df939616c479b6920`),
`STATE_LAMPIRAN_UKUR.md` (`162c130592c723f7bde5862546982b8d8a5295af`),
`journal/2026-07-30-135.md` (`626293c1ccd61eb8d8d063b48ad51112f5fda476`),
`decisions/ADR-A017.md` (`1be570f29e95227393dfb0989354cbbb5024b46c`).

## KESERASIAN VERSI — nomor lampiran kini DIVERIFIKASI dari KEPALA berkas

Serah terima giliran ini menyatakan nomor versi EKOR dan UKUR **belum diverifikasi**
karena yang ada hanya perbandingan blob, bukan pembacaan kepala berkas. **Utang itu
LUNAS di sini.** Kepala kedua berkas dibaca langsung pada giliran ini:

- `STATE_LAMPIRAN_EKOR.md` — baris pertama berbunyi *"STATE lampiran EKOR — bagian 2
  dari STATE (v10, milik STATE v50)"* → **v10**, blob `42fce0212c6f90581c39fc4df939616c479b6920`.
- `STATE_LAMPIRAN_UKUR.md` — baris pertama berbunyi *"STATE lampiran UKUR — bagian 3
  dari STATE (v10, milik STATE v50)"* → **v10**, blob `162c130592c723f7bde5862546982b8d8a5295af`.

**Koreksi atas jurnal 135 §12.4.** Jurnal 135 menulis ketimpangan versi "masih
terbuka: STATE v50 / EKOR v9 / UKUR v9 menurut kepala STATE v50". Kepala STATE v50
memang menulis v9 untuk kedua lampiran, dan itu sudah USANG saat v50 didorong: EKOR
v10 dan UKUR v10 sudah naik. Keadaan yang benar **pada saat berkas ini ditulis**:

1. `STATE.md` **v51** — berkas ini. Memuat R-311, papan skor **311**, **KC-51
   DIUSULKAN**, **H-A021 DIUSULKAN**, cacah tangan direktori baru.
2. `STATE_LAMPIRAN_EKOR.md` **v10** — **USANG SEBAGIAN:** papan skor masih 310, jumlah
   uji masih 1297, daftar ADR berhenti di A016 (A017 sudah ADA dan DITERIMA).
3. `STATE_LAMPIRAN_UKUR.md` **v10** — **USANG SEBAGIAN:** belum memuat API
   `sisa_defisit` V1, belum memuat 114 baris berdefisit, belum memuat H-A021, dan
   cacah modul/uji/workflow masih 47/51/42 dengan utang cacah tangan yang kini LUNAS.

**Sampai EKOR v11 dan UKUR v11 naik, sumber sah untuk R-311, KC-51, dan H-A021 adalah
`journal/2026-07-30-135.md` (blob `626293c1ccd61eb8d8d063b48ad51112f5fda476`) beserta
`reports/sisa_defisit_ringkas.json` (`91a05c0528050d0d37e4cf7711b6556f13fc8d16`) dan
`reports/sisa_defisit_status.json` (`1c9c2c5fc5f14a3f0e5cadcf564e699c92f8cf0e`).**
Bila lampiran bertentangan dengan berkas ini soal R-311, berkas SUMBER menang (KC-41).

Sebab pemecahan tetap sama: `push_files` menulis ulang SELURUH berkas, dan menyusun
tiga berkas besar dari satu konteks yang sudah terpakai banyak adalah cara paling
pasti merusak aturan 1–84 (KC-42, KC-43). **Satu berkas per push.**

## STATE DIPECAH TIGA — BACA INI LEBIH DULU

Pembagian yang MENGIKAT sejak v43, berlanjut di v51:

1. **`STATE.md`** (berkas ini) — **bagian 1**: kepala, aturan bernomor 1–**84** (plus
   usulan 77, 78, 82), kelas cacat KC-1..**KC-50** dan usulan **KC-51**.
2. **`STATE_LAMPIRAN_EKOR.md`** v10 — **bagian 2**: papan skor per ramalan, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** v10 — **bagian 3**: penyebut 787, taksonomi,
   karantina, bulan ABSEN, hipotesis H-A001..H-A020, lubang funding, byte parquet
   semesta, modul/workflow/uji, API terverifikasi.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip ekor v41; bukan sumber lagi.

**Ketiga berkas wajib dibaca bersama.** LANGKAH 0 PROMPT wajib menyebut ketiganya.

Yang lahir sejak v50: adjudikasi **R-311 = SEPARUH**; modul **`sisa_defisit` V1**
(sidik `6211624ba9514d604d4dc510abca2e40386775c7aaa1279135f0baf666f044b0`); CI 1297 →
**1341**; **aturan 57 beruntun 3 dari 3**; **KC-51 DIUSULKAN**; **H-A021 DIUSULKAN**;
**ADR-A017 DITERIMA**; dan **utang aturan 66 LUNAS** dengan cacah tangan bernomor pada
ref mutakhir.

## CACAH TANGAN DIREKTORI — LUNAS pada ref `3196fd98`

Aturan 66 menuntut cacah TANGAN bernomor, bukan turunan penambahan. Dicacah satu per
satu, bernomor, tanpa rentang, pada ref
**`3196fd9809f23917ba819b4339cdfdd57bb808d1`** (tip main saat berkas ini ditulis):

| direktori | cacah TERUKUR |
| --- | --- |
| `lux_ai/serapan/` (berkas `.py`, termasuk `__init__.py`) | **49** |
| `tests/` | **53** |
| `.github/workflows/` | **44** |
| akar repo | **18** entri (**6** direktori + **12** berkas) |

Enam direktori akar: `.github`, `decisions`, `journal`, `lux_ai`, `reports`, `tests`.
Dua belas berkas akar: `PETA_MODUL.md`, `PETA_MODUL_BERKAS.md`, `PROMPT.md`,
`PROMPT_KELANJUTAN.md`, `README.md`, `STATE.md`, `STATE_LAMPIRAN.md`,
`STATE_LAMPIRAN_ADR.md`, `STATE_LAMPIRAN_ANGKA.md`, `STATE_LAMPIRAN_EKOR.md`,
`STATE_LAMPIRAN_UKUR.md`, `requirements.txt`.

Angka 48 / 52 / 43 pada ref `5d7d8b96` (ADR-A017 kep. 11) TETAP sah untuk ref itu.
Angka 49 / 53 / 44 di atas **bukan turunan penambahan** — ia hasil cacah bernomor
langsung. **Kecocokannya dengan turunan bukan alasan melewatkan pencacahan berikutnya**
(aturan 66, KC-33). Sesudah trio berikutnya, angka 50 / 54 / 45 akan menjadi TURUNAN
dan DILARANG dikutip sebagai terukur.

## PERINGATAN DINI ATURAN 48 — besar modul

Diukur dari daftar direktori pada ref `3196fd98` (byte, bukan baris):
`silang_funding.py` **29.873** · `funding.py` **28.121** · **`sisa_defisit.py`
25.949** · `semesta_kuota.py` 24.987 · `lubang_tengah.py` 23.745. `sisa_defisit.py`
kini modul **terbesar ketiga** di repo. Ini peringatan dini, bukan pelanggaran:
aturan 48 menuntut pemecahan sebelum fungsi baru ditambahkan pada berkas yang
mendekati 800 baris. **Bila `sisa_defisit` V2 diperlukan, pecah lebih dulu.**

## KOREKSI SALAH KETIK — jurnal 135 §13.3 (LUNAS di sini)

§13 butir 3 jurnal 135 berbunyi *"ADR-A018 bila KC-51 hendak diresmikan dan aturan 85
**hendan** dirumuskan"*. Kata **"hendan" adalah SALAH KETIK; yang benar "hendak"**.
Berkas jurnal **TIDAK didorong ulang**, dengan sebab tertulis: `push_files` menulis
ulang seluruh berkas, sehingga memperbaiki satu karakter berarti menyusun ulang
seluruh jurnal dari konteks yang sudah terpakai banyak — persis yang dicatat KC-42
sebagai cara paling pasti merusak berkas. Ini mengikuti preseden STATE v50 atas jurnal
132 §3 ("beruntun 2/1" → 2/2). **Bila jurnal 135 dan berkas ini bertentangan pada
titik itu, berkas ini menang** — pengecualian tersurat atas KC-41 yang HANYA berlaku
untuk salah ketik yang sudah diakui, tidak pernah untuk angka terukur.

## KOREKSI BESAR yang MASIH HIDUP — dua angka yang selama ini disamakan

Tidak berubah dari v50, diulang karena mengubah bacaan kalimat lama:

- **TERUKUR:** `jumlah_lilin_langsung` = **839.325.999** lilin menit, dijumlahkan
  LANGSUNG dari medan `cacah_lilin` atas 19.586 baris laporan kehidupan.
- **TERCATAT BERULANG:** total baris parquet semesta = **839.842.134** baris parquet,
  dari run rilis 30404071324.
- **SELISIH = 516.135.** Kedua besaran BUKAN besaran yang sama.

Seluruh aritmetika implikasi jurnal 131 §6 dibangun di atas penyamaan itu dan karena
itu **SALAH sebagai turunan**, meski R-310 sendiri tetap sah (pita dikunci lebih dulu,
aturan 29). **Dugaan yang BELUM DIUJI dan DILARANG dikutip sebagai penjelasan:**
19.598 − 19.586 = 12 simbol-bulan karantina, dan 516.135 / 12 = 43.011 ≈ sebulan penuh
lilin menit. Masih belum tersentuh sejak diusulkan di v50; calon poros R-312.

## Aturan bernomor

Aturan **1–36** berlaku tanpa perubahan; teks di STATE v19 (blob `e06c486e…`),
ringkas di v37 (blob `f520d5e2`).

**Aturan 10 (irisan/urutan bulan BUKAN sebab). [v51] Ditaati.** R-311 mengukur bahwa
114 baris menanggung seluruh sisa 712.925 lilin, dengan puncaknya TLMUSDT 2023-03
(2.130 dari 44.640 lilin, 95,2% kosong). Itu pernyataan SEBARAN. DILARANG diubah
menjadi sebab, dan DILARANG dilanjutkan ke pernyataan tentang harga atau peristiwa
pasar (lihat larangan aktif di bawah).

**Aturan 21 (total papan skor dihitung tangan). [v51] Ditaati:** 217 + 57 = 274;
274 + 22 = 296; 296 + 8 = 304; 304 + 7 = **311**. Rincian: TEPAT **217** · MELESET
**57** · SEPARUH **22** · TIDAK TERADJUDIKASI **8** · MENUNGGU **7**. N_percobaan = 0.
**ADJUDIKASI RISET TETAP TERKUNCI.** MENUNGGU: R-7, R-19, R-20, R-28, R-36, R-37,
R-199. Dasar lajur: STATE v50 (TEPAT 217 · MELESET 57 · SEPARUH 21 · TIDAK
TERADJUDIKASI 8 · MENUNGGU 7 = 310) ditambah R-311 SEPARUH (21 → 22). Lajur DIBACA
dari v50, tidak dikarang.

**Aturan 29 (pita praregistrasi TIDAK boleh diubah sesudah pengukuran). [v51]
Ditaati, dan kali ini pitanya KALAH sebagian.** Pita R-311 dikunci di
`journal/2026-07-30-134.md` (blob `edf62c54f99fc26f43c046472eb1d74989f54c19`) sebelum
`sisa_defisit.py` ada: butir 1 (cacah baris berdefisit) **200 .. 12.000**, butir 2
(bagian sepuluh teratas) **0,02 .. 0,45**. Terukur **114** dan **0,4087**. Pita TIDAK
dilebarkan, TIDAK dipersempit, dan kekalahan butir 1 ditulis telanjang.

**Aturan 36 (dua modul berbeda atas semesta sama wajib cocok). [v51] Ditaati untuk
kelima kalinya:** kesepuluh invarian `sisa_defisit` V1 berselisih NOL terhadap catatan
semesta — penyebut 19.586 · simbol 787 · bukan-pertama 18.799 · HIDUP 18.087 · SEPI 98
· MATI 1.401 · MATI penuh 1.392 · MATI tak penuh 9 · `defisit_bukan_pertama` 808.162 ·
`defisit_sembilan` 95.237.

**Aturan 43 (toleransi berskala). [v51]** Tidak mendapat bentuk kegagalan baru.

Aturan **37, 39–45, 47, 49, 51, 53, 54, 56, 59–62** berlaku tanpa perubahan; ringkas
satu baris: 37 kelas cacat pada sampel · 39 keseragaman sampel bukan ramalan · 40 uji
silang baris · 41 penyebut nol → TIDAK TERADJUDIKASI · 42 kelas cacat butuh angka
terukur · 43 toleransi berskala · 44 ramalan menyebut penyebut · 45 keatomikan push
pemicu · 47 satuan cacah tersurat · 49 re-export mematahkan uji · 51 jendela mundur
adaptif · 53 ramalan kode keluar butuh pembacaan perilaku · 54 cacah `def test_` satu
per satu · 56 commit BERIKUTNYA yang menyentuh X · 59 ketiadaan gejala butuh penyebut
· 60 mekanisme tak dipindah antarkasus · 61 medan tak dipindah antarjalur · 62 daftar
tak diminta dari laporan bercacah.

Yang berikut memuat angka atau daftar kepatuhan, jadi ditulis agak penuh:

38. Cacah uji hanya sah dari `reports/ci_terakhir.json` (run id + commit +
    `kode_keluar`). **[v51] Ditaati:** **1341** butir, blob
    **`2d32f814e5e426e1411559810b55b9f20176a22d`**, run **30542217837**, commit
    **`b1c7941db3e08ae8a6f06864d7f47a571abf5669`**, 2026-07-30T12:22:10Z, kode 0
    (`1341 tests collected in 0.62s`). Turunan: 1297 + **44** butir
    `tests/test_sisa_defisit.py` = 1341 ✅ (aturan 21).
    **ORDINAL PEMAKAIAN BELUM TEREKONSILIASI — DILARANG menulis nomor pasti.**
    STATE v50 mencatat pemakaian ke-**37** (run 30535202643). Sesudah itu ada
    sekurang-kurangnya dua pembacaan lagi: run **30541051907** (CI 1297, commit
    `5d7d8b96`) dan run **30542217837** (CI 1341, commit `b1c7941d`). Karena tidak
    dapat dipastikan tidak ada pembacaan lain di antaranya, nomor pemakaian berjalan
    **tidak boleh ditulis**; **EKOR v11 wajib merekonsiliasinya**.
    **Catatan jujur yang WAJIB ikut:** `ci_terakhir.json` hanya menyimpan run
    TERAKHIR, sehingga ramalan "CI tetap" pada push dokumen yang tidak menyentuh
    `tests/**` tidak pernah terukur. Bukan tepat, bukan meleset; DILARANG dicatat
    sebagai kemenangan. Push berkas ini termasuk kelas itu.
45. Keatomikan push pemicu. **[v51] Ditaati:** trio `sisa_defisit` (modul + uji +
    workflow) didorong dalam SATU `push_files`
    (**`b1c7941db3e08ae8a6f06864d7f47a571abf5669`**).
46. Kode dilarang menyimpulkan dari penyebut nol. **[v51] Ditaati di `sisa_defisit`
    V1:** `bagian_teratas` mengembalikan **null**, bukan 0, bila baris berdefisit
    kurang dari sepuluh atau penyebutnya nol; di adjudikasi null dibaca TIDAK
    TERADJUDIKASI, bukan kekalahan. Tidak terpakai kali ini karena 114 >= 10.
47. Satuan cacah tersurat. **[v51] Ditaati:** "114", "17.398", "17.284", "18.799",
    "1.401", "9", "1.392" bersatuan **baris simbol-bulan**; "712.925", "291.379",
    "42.510", "808.162", "95.237", "18.143.601", "839.325.999", "516.135" bersatuan
    **lilin menit**; "839.842.134" bersatuan **baris parquet** — dan dua satuan
    terakhir itu BERBEDA; "0,4087" adalah **bagian tanpa satuan**, bukan persen;
    "25.949", "29.873", "28.121" bersatuan **byte berkas sumber**.
48. Berkas modul mendekati 800 baris dipecah sebelum fungsi baru ditambahkan.
    **[v51] PERINGATAN DINI** — lihat bagian tersendiri di atas: `silang_funding.py`
    29.873 B · `funding.py` 28.121 B · `sisa_defisit.py` **25.949 B** (terbesar ketiga).
50. Setiap pengukuran yang menyimpulkan dari KETIADAAN wajib memuat kendali positif.
    **[v51] Ditaati di `sisa_defisit` V1:** `kendali_negatif` memakai semesta buatan
    yang jawabannya dihitung TANGAN lebih dulu (`JAWABAN_KENDALI`, tujuh belas medan,
    termasuk `bagian_teratas` 0,9677 = 600/620) dan seluruhnya cocok; **kendali nol**
    membuktikan modul sanggup menjawab **nol baris berdefisit** dan `bagian_teratas`
    **null** alih-alih mengarang angka; `kendali_data` memastikan tiga bulan BTCUSDT
    HIDUP dengan `cacah_lilin` 44.640 penuh.
52. Laporan yang tidak dapat dibaca utuh setara dengan laporan yang tidak ada.
    **[v51] Ditaati untuk trio `sisa_defisit`,** ketiganya dibaca ulang UTUH sesudah
    push `b1c7941d` dan blobnya dicatat di jurnal 135 §1:
    `lux_ai/serapan/sisa_defisit.py` (**`7aa0e6d7003902e50806570ad112aae7f0345b07`**),
    `tests/test_sisa_defisit.py` (**`7004115acffd9c03c9ba4f9873bef40cb6b1375f`**),
    `.github/workflows/sisa_defisit.yml`
    (**`645112075e104a74d43f3e3d2185cfbd48b0b513`**).
    **[v51] Dibaca UTUH pada giliran ini:** PROMPT v54, STATE v50, EKOR v10, UKUR v10,
    jurnal 135, ADR-A017, dan dua berkas akar yang belum pernah diperiksa —
    `STATE_LAMPIRAN.md` (**`f2b907648bb291d5a4e44e5683270d84cf981a6a`**, 2.350 B) dan
    `STATE_LAMPIRAN_ANGKA.md` (**`f3ebdb02f4e03fea6e45a2fba107a50f69ace7c6`**, 1.841 B).
    Utang yang TETAP hidup: `tests/test_bentangan_kohort.py` V2 (63 butir, blob
    `9f850ecdb25466d38c839004b36ff221db2cf7f8`, 13.154 B) belum dibaca ulang byte demi
    byte — **kini SEMBILAN versi menunggu.** Juga belum dibaca utuh: `PETA_MODUL.md`
    (`9ee33a99`, 8.691 B), `PETA_MODUL_BERKAS.md` (`3abe95f6`, 6.890 B),
    `PROMPT_KELANJUTAN.md` (`35beed44`, 10.777 B), `decisions/ADR-A002`, A004, A006,
    A007, A008, `karantina_semesta.yml` (`de40fa4e`), `tests/test_pulihkan.py`
    (`11c43533`), `test_rilis_karantina.py` (`739c8da9`), `test_karantina_a006.py`
    (`a5a3d82f`).
55. Rumusan pemicu workflow wajib dikutip dari berkas workflow beserta blobnya.
    **[v51] Ditaati lewat jurnal 135 §1:** `sisa_defisit.yml` (blob `64511207`) —
    `paths` **satu entri saja**, `- lux_ai/serapan/sisa_defisit.py`.
57. Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB ditulis bernomor.
    **[v51] BERUNTUN 3 DARI 3** sesudah putus di giliran ke-27. Daftar **44** butir
    (`test_01`..`test_44`) ditulis bernomor satu nama per nomor, **tanpa rentang**, di
    kepala berkas uji dan diucapkan SEBELUM push; ramalan **1297 + 44 = 1341, kode 0**;
    terukur **1341, kode 0**. Dua helper (`_baris`, `_ringkasan_bersih`) sengaja
    berawalan garis bawah agar tidak dikumpulkan pytest — itu lagi yang menahan ramalan
    dari meleset ke atas. Kemenangannya **MUDAH** dan TIDAK masuk papan skor.
    **Batas beruntun yang WAJIB ikut:** hanya push yang MENYENTUH `tests/**` yang
    dihitung. Push dokumen (STATE/EKOR/UKUR/PROMPT) tidak pernah terukur dan tidak
    boleh menambah beruntun.
58. Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH DILARANG
    diramalkan dengan pita sempit.
63–76. Berlaku tanpa perubahan dari v43. Teks penuh di v43 (blob `a91a4934`).

**Aturan 66 (cacah direktori dengan TANGAN, bernomor). [v51] LUNAS** — lihat bagian
"CACAH TANGAN DIREKTORI" di atas: 49 / 53 / 44 pada ref `3196fd98`, ditambah 18 entri
akar. Utang yang hidup sejak v50 dengan ini ditutup. **Utang baru akan lahir begitu
trio berikutnya didorong.**

**Penomoran aturan [v51].** Tidak ada aturan baru yang diresmikan giliran ini. Aturan
resmi tetap: **1–81, 83, dan 84**. Nomor **82** tetap dicadangkan untuk usulan yang
belum berlaku. **Aturan berikutnya yang bebas: 85** — calon isinya adalah penangkal
KC-51 (lihat di bawah), dan peresmiannya adalah keputusan **ADR-A018**, yang DILARANG
disusun pada giliran yang sama dengan adjudikasi (ADR-A016).

**Aturan 77 (TETAP DIUSULKAN):** dua berkas laporan berblob IDENTIK bukan dua
pengukuran. **[v51] Tidak menguat:** `sisa_defisit.json` dan `_ringkas.json` berblob
BERBEDA, seperti seharusnya.

**Aturan 78 (TETAP DIUSULKAN — MENGUAT LAGI [v51], kali kelima berturut):**
`BATAS_BARIS_LAPORAN=40` membuat `sisa_defisit_ringkas.json` terbaca UTUH dalam satu
bacaan, sementara `sisa_defisit.json` sendiri **11.069 B**. Belum diresmikan karena ini
kasus rancangan, bukan pengukuran batasnya sendiri.

**Aturan 79 (BERLAKU sejak v44). [v51] Ditaati di R-311:** praregistrasi ditulis di
`journal/2026-07-30-134.md` (ada di `paths-ignore`) SEBELUM `sisa_defisit.py` ada, lalu
disalin apa adanya ke tetapan modul dan tidak diubah.

**Aturan 80 (BERLAKU sejak v46). [v51]** R-311 tidak menguji arah waktu.

**Aturan 81 (BERLAKU sejak v46). [v51] Diperiksa dan TIDAK terpicu untuk butir 2:**
sepuluh baris teratas tersebar di tujuh bulan berbeda (2023-03, 2022-09, 2023-02,
2022-04 dua baris, 2024-09, 2022-05 dua baris, 2022-02 dua baris). Pasangan terbesar
satu bulan hanya dua baris — jauh di bawah ambang 1/4. **Untuk R-310 aturan 81 TETAP
terpicu** dan tetap mengikat setiap kutipan angka 9.

**Aturan 82 (TETAP DIUSULKAN, nomor dicadangkan) — ambang yang MUSTAHIL dilewati ATAU
yang hasilnya SUDAH TERSIRAT DILARANG jadi butir berisiko. [v51] Tidak mendapat kasus
baru;** tidak dilanggar oleh R-311, sebab kedua butirnya benar-benar bisa kalah — dan
butir 1 memang kalah.

**Aturan 83 (BERLAKU sejak v49). [v51] Ditaati untuk KETIGA kalinya — dan kali ini ia
menunjuk pada kegagalan pemakainya, bukan pada dirinya.** Aritmetika implikasi ditulis
di jurnal 134 sebelum pita dikunci: cacah baris berdefisit dijamin berada di **16 ..
18.790**. Terukur **114** — di dalam jaminan. Aritmetikanya benar dan **tidak berguna**:
rentangnya tiga tingkat besaran. Tepi bawah pita justru diletakkan di **200**, dua
belas setengah kali di atas lantai aritmetis **16** yang sudah dihitung sendiri.
Lantai bukan sebab kekalahan; **pilihan menaruh tepi jauh di atas lantai** yang jadi
sebab. Dari sinilah KC-51 lahir.

**Aturan 84 (RESMI sejak v50). [v51] Ditaati untuk kedua kalinya secara preventif:**
ketiga butir R-311 berklausa TUNGGAL; tidak ada satu pun angka yang bergantung pada
klausa gabungan.

## R-311 — ADJUDIKASI RESMI: SEPARUH

Sumber: jurnal 135 (`626293c1…`), `reports/sisa_defisit_ringkas.json` (`91a05c05…`),
`reports/sisa_defisit_status.json` (`1c9c2c5f…`), run modul **30542217951** pada commit
`b1c7941d`, kode keluar **0**.

| butir | berisiko | pita | terukur | hasil |
| --- | --- | --- | --- | --- |
| 1 — cacah baris berdefisit | ya | 200 .. 12.000 | **114** | **KALAH** |
| 2 — bagian sepuluh teratas | ya | 0,02 .. 0,45 | **0,4087** | **MENANG** |
| 3 — penggugur bersih + invarian nol | tidak (mudah) | — | bersih | menang, tidak diskor |

Satu menang, satu kalah dari dua butir berisiko → **SEPARUH**.

**Angka terukur:** `cacah_calon` (bukan-pertama, bukan MATI) **17.398** ·
`cacah_berdefisit` **114** · `cacah_calon_penuh` **17.284** · `defisit_calon`
**712.925** · `defisit_teratas` **291.379** · `bagian_teratas` **0,4087** ·
`defisit_terbesar` **42.510** · `sebaran_status_berdefisit` HIDUP **111** / SEPI **3** /
MATI 0 / TAK_TERUKUR 0 · `sebaran_status_calon` HIDUP **17.318** / SEPI **80**.

**Penggugur seluruhnya bersih:** `sidik_seragam` true · `cacah_laporan_dibaca` 8 dari 8
· `laporan_hilang` kosong · `cacah_kunci_ganda` 0 · `cacah_defisit_negatif` 0 ·
`cacah_baris_tanpa_lilin` 0 · kesepuluh `selisih_invarian` NOL · `kendali_data_sah`
true · `kendali_negatif_lolos` true · `kendali_nol_lolos` true.

**Catatan kejujuran yang WAJIB ikut dikutip:**

1. **Butir 2 menang TIPIS ke tepi ATAS:** sisa pita di atas hanya 0,45 − 0,4087 =
   **0,0413**, sekitar sembilan persen lebar pita. R-310 menang tipis ke tepi BAWAH
   pada kedua butirnya. **Dua ramalan berturut yang menang menempel tepi, dan pada
   tepi BERLAWANAN, DILARANG dibacakan sebagai bukti pita yang dirancang baik.**
2. **Penutupan 712.925 nyaris TAUTOLOGIS.** `defisit_calon` = 712.925 tepat dan
   `selisih_sisa` = 0, tetapi menurut definisi 808.162 − 95.237 = 712.925 **terpaksa**
   muncul begitu seluruh 1.401 baris MATI ternyata bukan-pertama. Muatan sejatinya
   hanya itu. Menyebutnya "pengukuran bebas yang mengonfirmasi" **DILARANG** (KC-50,
   KC-37).
3. **Pemeriksaan silang yang menutup tanpa sisa** (terbitan, TIDAK diskor):
   18.799 − 17.398 = **1.401** = seluruh baris MATI → **tidak satu pun bulan pertama
   simbol berstatus MATI**; 18.087 − 17.318 = **769** bulan pertama HIDUP;
   98 − 80 = **18** bulan pertama SEPI; 769 + 18 = **787** = `cacah_simbol`.
4. **Temuan yang benar-benar baru:** sisa 712.925 ditanggung **114 baris** dari 17.398
   calon (**0,66%**, 114/17.398 = 0,006553), rata-rata **6.254** lilin per baris;
   sepuluh baris teratas (8,8% dari 114) memikul **40,87%**. Puncaknya **TLMUSDT
   2023-03**: HIDUP, 2.130 dari 44.640 lilin, **95,2% kosong** — satu-satunya baris
   yang tercatat MELAWAN H-A019, kini terlihat bukan bulan tepi dan bukan bulan
   pertama, melainkan bulan HIDUP yang hampir seluruhnya kosong. Itu **melemahkan**
   bacaan "byte kecil selalu berarti bulan sebagian di tepi" **tanpa menegakkan
   penggantinya**.
5. Seluruh 114 baris berstatus HIDUP (111) atau SEPI (3); tak satu pun MATI — itu
   **dipaksa definisi penyebut kerja**, jadi BUKAN temuan.

## Kelas cacat

KC-1 s.d. KC-12 seperti v19; KC-10 dan KC-11 DITUTUP. KC-13 keterwakilan sampel.
**KC-16 DITARIK — nomornya TETAP kosong selamanya.** KC-17 DITUTUP. Teks penuh
KC-14, KC-15, KC-19..KC-29 ada di v37 (blob `f520d5e2`). KC-30..KC-42 ada di v43
(blob `a91a4934`). KC-43, KC-44 di v44 (`ede3ce3b`). KC-45, KC-46 di v45 (`e07f2de1`).
KC-47 di v46 (`41b5b585`). KC-48 di v47 (`7642b75d`). KC-49 di v48 (`2fd136e4`).
KC-50 teks penuh di v50 (`095a4b2c`).

Ringkas KC-19..KC-50 satu baris: KC-19 mencacah dari ingatan · KC-20 bias ke bawah ·
KC-21 ketiadaan gejala dari ketiadaan pengukuran · KC-22 mekanisme dipindah · KC-23
medan dipindah · KC-24 daftar dari laporan bercacah · KC-25 batas semesta tak tersurat
· KC-26 medan ekstrem membisu tentang seri · KC-27 karakterisasi dari contoh berurut ·
KC-28 mencampur kelas instrumen · KC-29 taksonomi paralel · KC-30 nama kelas dibaca
sebagai keadaan · KC-31 nama peristiwa dibaca sebagai mekanisme · KC-32 dua sistem
penomoran dicampur · KC-33 mengenali satu peristiwa lalu berhenti · KC-34 cacah
subkelompok dari pengurangan kepala · KC-35 cakupan kode dicampur dengan cakupan
laporan · KC-36 homonim diperlakukan satu konsep · KC-37 nol dari satu penyebut
sebagai bukti di penyebut lain · KC-38 kecocokan tanpa membedakan mekanisme · KC-39
dua penyebut bulan absen dicampur · KC-40 daftar klausa gagal dibaca sebagai keadaan ·
KC-41 pemicu/label/nomor dari ingatan · KC-42 menulis ulang berkas melampaui batas push
· KC-43 tanda tangan fungsi dari ingatan · KC-44 semua laporan di-commit satu langkah ·
KC-45 satuan "bulan tanpa funding" dan "bulan MATI" dicampur · KC-46 lubang bentuk AWAL
dibaca sebagai "funding berhenti" · KC-47 satu peristiwa menyamar sebagai banyak
pengamatan bebas · KC-48 ambang absolut pada besaran yang sebarannya belum pernah
diukur · KC-49 pita dikunci tanpa menghitung implikasi aritmetis · KC-50 agregat
dihitung lewat jalan memutar sehingga selisihnya tak terlihat.

**KC-41 — tetap berlaku.** Bila dua bagian STATE bertentangan, berkas SUMBER menang,
bukan yang lebih baru — dengan pengecualian tersurat untuk salah ketik yang sudah
diakui: jurnal 132 §3 (dikoreksi v50), EKOR v10 karakter `≉`/`≈` (dikoreksi UKUR v10),
dan **jurnal 135 §13.3 "hendan" (dikoreksi berkas ini)**.

**KC-47 — [v51] tidak mendapat kasus baru;** kasus R-310 (tujuh dari sembilan berbulan
`2024-05`) tetap berlaku penuh dan wajib ikut setiap kali angka 9 dikutip.

- **KC-48 [RESMI sejak v47]**, **KC-49 [RESMI sejak v48]**, **KC-50 [RESMI sejak v50]**
  berlaku tanpa perubahan. KC-50 kembali menggigit di R-311 lewat penutupan 712.925
  yang tautologis (lihat catatan kejujuran butir 2).

- **KC-51 [DIUSULKAN di sini, BELUM RESMI] — taksiran pemusatan bias ke arah terlalu
  menyebar.**

  *Bentuk:* ketika meramalkan seberapa terpusat sebuah besaran semesta, taksiran titik
  yang ditulis secara sistematis **lebih menyebar** daripada kenyataan, sehingga pita
  yang dikunci meleset ke sisi "menyebar".

  *Tiga kasus terukur, berturut-turut:*
  1. **R-308 butir 2** — KALAH; zona byte ternyata jauh lebih bersih daripada dugaan
     (terukur **2**, pita 10..300).
  2. **R-310** — bagian defisit bukan-pertama ditaksir 0,073, terukur **0,0445**;
     meleset ±64% ke arah terlalu menyebar.
  3. **R-311** — cacah ditaksir ~3.000, terukur **114** (meleset faktor **26,3**,
     −96,2%); pemusatan ditaksir ~0,15, terukur **0,4087** (+172%). Dua-duanya ke arah
     yang sama.

  *Mengapa ini kelas cacat dan bukan tiga kesialan:* **arahnya tidak pernah berbalik.**
  Tiga kali berturut, kenyataannya lebih terpusat. Kesialan acak akan berganti arah.

  *Penangkal yang diusulkan (calon aturan 85):* bila sebuah butir berisiko meramalkan
  cacah atau pemusatan pada besaran yang sebarannya belum pernah diukur di semesta ini,
  taksiran titik WAJIB ditulis bersama arah bias yang tercatat, dan tepi pita di sisi
  "terpusat" WAJIB diletakkan **pada atau dekat lantai aritmetis** yang sudah dihitung,
  bukan pada kelipatan intuitif di atasnya. Kerabat KC-20, KC-48, KC-49; kerabat
  aturan 83.

  *Mengapa belum resmi:* peresmian kelas cacat adalah keputusan ADR, dan ADR-A016
  melarang menyusun keputusan pada giliran yang sama dengan adjudikasi. **ADR-A018**
  adalah tempatnya, bersama perumusan aturan 85.

## Hipotesis yang DIUSULKAN di giliran ini

**H-A021 (DIUSULKAN, BELUM DIUJI) — ANCUSDT 2022-05 (defisit 26.959) dan LUNAUSDT
2022-05 (defisit 26.950) adalah SATU peristiwa bersama, bukan dua kekosongan yang
kebetulan berdekatan.** Dasar terukur, dan HANYA ini: kedua simbol berbulan sama dan
defisitnya berselisih **sembilan lilin** pada penuh 44.640.

**Peringatan yang menempel:** bentuk buktinya IDENTIK dengan H-A020 (jendela sembilan
lilin pada gugus `2024-05`), dan **pengulangan bentuk itu sendiri patut dicurigai** —
ia bisa menandakan mekanisme yang sama, atau menandakan bahwa kita hanya pandai
menemukan pola yang sudah kita cari. Uji yang menegakkan atau meruntuhkannya: **lubang
tengah pada gugus `2022-05`**, sejajar dengan uji yang sudah diusulkan untuk `2024-05`.

**Yang DILARANG ditulis sebagai temuan sampai diuji:** kalimat apa pun yang menyebut
sebab, nama peristiwa pasar, keruntuhan ekosistem, atau tanggal penghentian untuk
gugus `2022-05`. Laporan kehidupan **tidak menyimpan harga**. Larangan menulis
"delisting 28 Mei 2024" untuk H-A020 tetap berlaku dan kini berlaku pula bagi bentuk
kalimat serupa untuk `2022-05` (aturan 10, KC-30, KC-31).

**H-A020** tetap **DIUSULKAN dan BELUM DIUJI**. Hipotesis berikutnya **H-A022**.

## Berkas akar yang baru diperiksa — status hidup/mati

- **`STATE_LAMPIRAN.md`** (`f2b90764`, 2.350 B) — **HIDUP sebagai arsip naratif.**
  Berisi L-1..L-5: mengapa juri ditulis ulang alih-alih diangkat dari modul warisan,
  mengapa detektor tetap diangkat, mengapa lapisan risiko diangkat apa adanya, mengapa
  ukuran model LLM bukan alasan (aturan sebenarnya: LLM dilarang di jalur keputusan),
  dan mengapa serapan berjalan paralel dengan pembangunan juri. **Tidak memuat angka
  semesta**; tidak bertentangan dengan STATE. Fungsinya mencegah perdebatan yang sama
  diulang.
- **`STATE_LAMPIRAN_ANGKA.md`** (`f3ebdb02`, 1.841 B) — **HIDUP tetapi hampir kosong.**
  `N_percobaan` = 0 (satu baris, 2026-07-28 "Repo dibuka"); bagian audit gerbang, sidik
  run, dan sidik data **kosong**; memuat angka struktural modul WARISAN (208 berkas,
  165 `.py`, 25.811 baris, `engine.py` 3.621 baris, subpohon `lux/` 8.674 baris) dan
  daftar **klaim yang DILARANG dipakai sebagai bukti** (Signals 10.032 / +189,41R /
  PF 1,61 dan seluruh tabel tuning `AUDIT.md`, tercemar kebocoran seleksi).
  **Peringatan:** angka di berkas itu tentang repo warisan, **bukan** tentang penyebut
  19.586 — jangan dicampur (KC-36).
- **BELUM diperiksa:** `PETA_MODUL.md` (`9ee33a99`, 8.691 B), `PETA_MODUL_BERKAS.md`
  (`3abe95f6`, 6.890 B), `PROMPT_KELANJUTAN.md` (`35beed44`, 10.777 B).
  `STATE_LAMPIRAN_ADR.md` (`a02ef271`) tetap **arsip, bukan sumber**.

## Larangan aktif — tidak berubah, jangan dilanggar

- Besar berkas **DILARANG** jadi detektor status ke arah mana pun (ADR-A015 kep. 5,
  ditegaskan ADR-A017 kep. 8). Di zona 22.440–97.634 byte ada **38 HIDUP dan 0 MATI**.
- Laporan kehidupan TIDAK menyimpan harga (`medan_baris_terlihat` **14** medan, tak
  satu pun harga) → "harga beku", "lilin datar", "jeda pemeliharaan bursa" **DILARANG**
  disimpulkan.
- **DILARANG** menulis "delisting 28 Mei 2024", dan kalimat sebab serupa untuk gugus
  `2022-05`.
- **712.925 DILARANG jadi penyebut pemeriksaan** (KC-50): ia muncul terpaksa dari
  808.162 − 95.237.
- Sembilan medan selisih `irisan_byte` = **delapan bebas + satu turunan**; frasa
  "sembilan pemeriksaan bebas" **DILARANG**.
- Numerator 9 pada R-310 **bukan sembilan pengamatan bebas**; paling banter tiga.
- Lajur papan skor **DILARANG dikarang** tanpa membaca STATE.
- Cacah direktori **turunan penambahan DILARANG** dikutip sebagai terukur.

## Angka semesta yang mengikat (dibaca dari v50/UKUR v10, tidak dihitung ulang dari ingatan)

Penyebut **19.586** (LOLOS gerbang, bukan 19.598) · `cacah_simbol` **787** ·
bukan-pertama **18.799** · HIDUP **18.087** · SEPI **98** · MATI **1.401** (seluruhnya
bukan-pertama) · MATI penuh **1.392** · MATI tak penuh **9** · `cacah_lain` **0** ·
`defisit_total` **18.143.601** · `defisit_pertama` **17.335.439** (95,5%) ·
`defisit_bukan_pertama` **808.162** · `defisit_sembilan` **95.237** · sisa **712.925** ·
calon **17.398** (HIDUP 17.318 + SEPI 80) · calon berdefisit **114** (HIDUP 111 +
SEPI 3) · `defisit_teratas` **291.379** · `bagian_teratas` **0,4087** ·
`defisit_terbesar` **42.510** · `jumlah_lilin_langsung` **839.325.999** · total baris
parquet **839.842.134** · **selisih 516.135** · total byte parquet **32.706.262.375** ·
`byte_mati` **579.041.399** · `bagian_byte_mati` **0,017704297493883234** ·
`cacah_hidup_byte_kecil` **38** · `cacah_mati_byte_kecil` **2** · bulan pertama HIDUP
**769** · bulan pertama SEPI **18** · lubang funding **880** semesta / **877** dalam
penyebut / 3 tak dikenal · `cacah_simbol_ada_lubang` **122** (awal 5, bukan-awal 118).

## Ke bagian 2 dan 3

Berkas ini berhenti di sini dengan sengaja. Lanjutannya:

- **Papan skor.** Keadaan MUTAKHIR ada di berkas ini (aturan 21): total **311** —
  TEPAT 217 · MELESET 57 · SEPARUH 22 · TIDAK TERADJUDIKASI 8 · MENUNGGU 7. Rincian per
  ramalan masih di `STATE_LAMPIRAN_EKOR.md` v10 (blob `42fce021`), yang totalnya masih
  310 dan jumlah ujinya masih 1297. **EKOR v11 wajib menambahkan baris R-311 = SEPARUH,
  jumlah uji 1341, ADR sampai A017, dan REKONSILIASI ordinal `ci_terakhir.json`.**
- **Penyebut 787, taksonomi, karantina, bulan ABSEN, hipotesis, byte parquet semesta,
  modul/workflow/uji, API terverifikasi** → `STATE_LAMPIRAN_UKUR.md` v10 (blob
  `162c1305`). **UKUR v11 wajib menambahkan API `sisa_defisit` V1, 114 baris
  berdefisit beserta sepuluh baris teratas, H-A021, dan cacah direktori 49/53/44.**

## Penomoran berikutnya

Jurnal **136** · STATE **v52** (lampiran EKOR/UKUR → **v11**) · PROMPT **v55** · ADR
**A018** · KC **KC-51** (masih usulan) · aturan **85** · hipotesis **H-A022** · ramalan
**R-312** · papan skor sesudah R-312 = **312**.

**R-312 DILARANG disusun pada giliran adjudikasi** (ADR-A016). Poros urut kekuatan:
(a) **lubang tengah pada gugus `2022-05` dan `2024-05`** untuk menegakkan atau
meruntuhkan H-A021 dan H-A020 sekaligus; (b) **selisih 516.135** lawan dugaan 12
simbol-bulan karantina — dengan peringatan aturan 83 bahwa dugaan itu sudah
menghasilkan satu angka (43.011), sehingga porosnya harus dipindahkan ke bentuk
sebaran, bukan ke rata-rata. Sebelum pita dikunci: aturan **83** (aritmetika implikasi
di jurnal lebih dulu, dan **tepi "terpusat" diletakkan dekat lantai** — KC-51), aturan
**84** (klausa tunggal), **KC-50** (agregat lewat jalur LANGSUNG dan diadu dengan angka
setara), aturan **79** (praregistrasi di `journal/**`), aturan **66** (cacah tangan
sebelum menamai modul), dan `BATAS_BARIS_LAPORAN` ringkas.
