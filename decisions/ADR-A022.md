# ADR-A022 — Menutup tumpukan usulan: empat aturan diresmikan, dua KC dibuang, satu KC dipersempit

**Tanggal:** 2026-07-31 (UTC)
**Status:** DITERIMA
**Konteks berkas:** disusun di atas `STATE.md` **v61** (blob
**`376768322e634b4e79bb416a5c4dbe4d18c0b03e`**, commit
**`bb959b62682347d62f75574b919949fd22222deb`**) dan `STATE_LAMPIRAN_UKUR.md` **v19**
(blob **`47df297d146697749643019d0bda216c5a88059a`**, commit `9d159e1e`), **keduanya
dibaca UTUH pada giliran ini atau giliran ini juga** (aturan 52 ke-35 dan ke-36).

**Aturan 38 dan ADR-A016 dipenuhi:** tidak ada adjudikasi pada giliran ini; laporan CI
ke-67 dibaca dan lolos aturan 90 sebelum berkas ini disusun.

---

## 1. Masalah yang dipaksa diputuskan

STATE v61 mencatat, dengan angka telanjang, bahwa **enam usulan aturan** (77, 78, 88,
89, 91, 92) dan **tiga usulan KC** (56, 57, 58) menganggur bersamaan, dan menuliskan
vonisnya sendiri terhadap keadaan itu:

> *"Menumpuknya usulan BUKAN tanda kedisiplinan otomatis — ia dapat menjadi cara halus
> menunda keputusan sambil tampak berhati-hati."*

ADR ini menutup tumpukan itu **sejauh bahannya dibaca**, dan **menyebut secara tersurat
apa yang tidak ditutup beserta alasannya**. Menutup dengan mengarang teks yang tidak
dibaca ulang adalah **KC-41**, dan itu lebih buruk daripada menunda.

---

## 2. Keputusan pokok yang mendasari semuanya: DUA JENIS USULAN, DUA AMBANG

Selama ini satu ambang dipakai untuk dua jenis barang yang berbeda, dan itulah sebab
tumpukan ini tidak pernah bergerak. ADR-A019 kep. 3 mensyaratkan **dua kejadian cacat
bebas** sebelum sesuatu diresmikan. Syarat itu **benar untuk KC** dan **keliru untuk
sebagian aturan**.

**KEPUTUSAN 1 — pembedaan resmi.**

| jenis | isinya | ambang peresmian |
| --- | --- | --- |
| **KELAS CACAT (KC)** | **klaim empiris**: "cacat berbentuk X betul-betul ada dan berulang" | **TETAP dua kejadian bebas** (ADR-A019 kep. 3), tanpa pelonggaran |
| **ATURAN DISIPLIN PRAREGISTRASI** | **kewajiban menulis** yang berlaku sebelum bahan dibuka | **manfaat terukur sekali pun CUKUP**, bila biayanya nol dan ia tidak mengklaim apa pun tentang dunia |

**Dasarnya.** Sebuah KC menyatakan sesuatu **tentang kenyataan** — meresmikannya dari
satu kejadian adalah menggeneralisasi dari n = 1, yaitu **KC-47**. Sebuah aturan disiplin
praregistrasi tidak menyatakan apa pun tentang kenyataan; ia hanya **memaksa penyusun
menulis lebih banyak sebelum melihat angka**. Bila ia salah, kerugiannya **beberapa baris
teks**; bila ia benar, ia mencegah kemenangan palsu. **Ambang "dua kejadian" untuk barang
bermodal nol adalah kehati-hatian yang salah alamat** — ia menunda manfaat tanpa
mencegah risiko apa pun.

**BATAS PENGECUALIAN, TEGAS.** Pelonggaran ini berlaku **HANYA** untuk aturan yang
memenuhi **ketiganya**: (i) ia kewajiban **menulis**, bukan kewajiban **menyimpulkan**;
(ii) ia berlaku **sebelum** bahan dibuka; (iii) melanggarnya **tidak dapat** mengubah
satu angka terukur pun. **DILARANG** memakai keputusan 1 untuk meresmikan KC mana pun,
atau aturan yang menyentuh **vonis**, **papan skor**, atau **tafsir angka**.

---

## 3. Keputusan atas usulan aturan

### KEPUTUSAN 2 — ATURAN 88 DIRESMIKAN

> **Aturan 88 [RESMI].** Ramalan tentang **keseragaman** yang tidak disertai mekanisme
> tertulis WAJIB ditulis sebagai **sebaran**, bukan sebagai nilai tunggal.

Memenuhi ketiga syarat keputusan 1. Kejadian cacatnya tetap **satu**; yang berubah
adalah ambangnya, bukan buktinya. **DILARANG menulis bahwa aturan 88 punya dua
kejadian.**

### KEPUTUSAN 3 — ATURAN 89 DIRESMIKAN

> **Aturan 89 [RESMI].** Setiap pita ramalan WAJIB menutup **seluruh sisi ruang
> nilainya**, atau menyatakan tersurat mengapa sebuah sisi mustahil.

**Manfaatnya terukur dua kali, dan keduanya dicatat sebelum ADR ini:**

1. **R-317 butir 3** kalah di sisi "lebih awal". Bila pitanya dua sisi seperti jurnal
   146, "2023-01" berpeluang diklaim menang lewat bunyi harfiah. **Aturan 89 mencegah
   kemenangan palsu.**
2. **R-318 butir 1** ditulis tiga sisi padahal sisi "lebih" tampak mustahil — dan sisi
   itu **nyaris terpakai**, sebab tetapan kode `R288_BNX_ABSEN` meramalkan **3**
   sementara terukur **2**.

STATE v60 menahan peresmian ini dengan alasan "manfaat sekali pakai bukan kejadian
cacat". **Alasan itu kini digugurkan oleh keputusan 1**, bukan diabaikan.

### KEPUTUSAN 4 — ATURAN 91 DIRESMIKAN

> **Aturan 91 [RESMI].** Ramalan yang butir-butirnya diturunkan dari **satu aritmetika
> yang sama** WAJIB menyatakan hal itu di praregistrasi, dan kemenangan butir-butir itu
> **DILARANG dijumlahkan sebagai bukti bebas**.

**Ini yang paling mendesak dari keempatnya.** R-318 mencetak **empat TEPAT** dan
menaikkan papan skor **+4**, padahal **tiga** di antaranya turun dari bentangan **50**
dan **50 − 48 = 2**. Bila aritmetika itu salah, ketiganya jatuh bersama. **Papan skor
sudah terlanjur mencatat empat**, dan aturan 29 melarang membatalkannya — maka
satu-satunya penangkal yang tersisa adalah **mencegah pengulangannya**.

**Catatan kejujuran yang melekat permanen:** kenaikan nisbah 72,7 → 72,8 pada EKOR v19
**sebagian besar dibiayai oleh empat kemenangan berkorelasi**. **DILARANG dibaca sebagai
kalibrasi membaik** (KC-51).

### KEPUTUSAN 5 — ATURAN 92 DIRESMIKAN, DALAM BENTUK YANG DIPERSEMPIT

> **Aturan 92 [RESMI].** Setiap berkas akar WAJIB berakhir pada **penanda penutupnya
> sendiri** yang menyebut nama dan versinya. Pembacaan ulang yang **tidak** sampai pada
> penanda itu WAJIB diperlakukan sebagai **berkas cacat** dan didorong ulang **sebelum
> pekerjaan lain apa pun**.

**Dipersempit dengan sengaja.** Rumusan usulan di UKUR v19 memuat dua bagian; bagian
pertama ("wajib dibaca ulang utuh pada giliran yang sama") **sudah dijamin aturan 52**
dan **tidak diulang** — mengulangnya akan menciptakan dua nomor untuk satu kewajiban,
yaitu **KC-32**. Yang benar-benar baru adalah **penanda penutup**, dan itulah isi
aturan 92.

**Dasar terukur:** kesalahan dokumen **butir 19**. UKUR v19 dorongan pertama
(`40e450b6…`) berhenti di tengah kalimat; `push_files` melaporkan **berhasil**; SHA sah;
setiap kalimat yang ada di dalamnya benar. **Tanpa penanda penutup, "berkas ini utuh"
tidak dapat diperiksa — hanya dapat dirasakan.** Aturan 92 mengubahnya menjadi
pemeriksaan **mekanis**.

**Sudah dipakai dua kali sebelum diresmikan:** UKUR v19 padat dan STATE v61, keduanya
berakhir pada penandanya dan keduanya terverifikasi.

### KEPUTUSAN 6 — ATURAN 77 dan 78 DITUNDA, DENGAN ALASAN TERSURAT

**TIDAK diputuskan pada ADR ini.** Alasannya tunggal dan tidak boleh dihaluskan:
**teks penuh keduanya tidak dibaca ulang pada giliran ini** — ia hidup di STATE v43
(`a91a4934`) dan berkas turunannya. Memutuskan nasib aturan yang rumusannya diambil dari
ingatan adalah **KC-41**, dan KC-41 lebih mahal daripada satu ADR penundaan.

**MENGIKAT:** **ADR-A023 WAJIB memutuskan keduanya**, dan **prasyaratnya tersurat** —
teks penuh aturan 77 dan 78 dibaca utuh lebih dulu.

---

## 4. Keputusan atas usulan kelas cacat

### KEPUTUSAN 7 — KC-56 DIBUANG SEBAGAI KC, ISINYA DIANGKAT JADI KEWAJIBAN

**KC-56** ("laporan tanpa `waktu_utc` diperlakukan seolah serempak dengan laporan lain")
**TIDAK diresmikan sebagai kelas cacat**, dan **TIDAK dibiarkan menggantung**. Ia
**DIBUANG dari daftar usulan KC** dan isinya diangkat menjadi kewajiban di keputusan 8.

**Sebabnya:** ia tidak pernah mendapat kejadian kedua — setiap laporan baru sejak ia
lahir **bertanggal**. Sebuah kelas cacat yang **satu-satunya kejadiannya adalah satu
berkas** bukan kelas cacat; ia **masalah berkas itu**. Menyimpannya sebagai "usulan"
selamanya adalah persis kepura-puraan kehati-hatian yang STATE v61 peringatkan.

### KEPUTUSAN 8 — `semesta_rentang.json` TURUN KE "BAHAN TAK BERSAKSI"

Berkas **`8d5bd06ca4073dac8a8ef7841d81824427cc8e63`**, 110.662 B, punya **tiga** cacat
sekaligus: terbaca **95%** (potongan hilang di tengah, abjad **P–R**), **tanpa
`waktu_utc`**, dan **tanpa sidik apa pun**. Tidak ada modul yang diketahui menulisnya
(utang ukur 22).

> **Kelas resmi baru — BAHAN TAK BERSAKSI.** Berkas yang tidak memuat `waktu_utc`
> **atau** tidak memuat sidik kode/data **DILARANG** dipakai sebagai bahan ramalan
> berskor, **DILARANG** dibandingkan keserempakannya dengan laporan lain, dan **WAJIB**
> disebut statusnya setiap kali angkanya dikutip. Ia **BOLEH** dipakai sebagai
> **petunjuk arah** dan sebagai **pembanding yang membantah**, tidak pernah sebagai
> **pembanding yang mengukuhkan**.

**Pembedaan terakhir itu bukan hiasan.** `semesta_rentang.json` **sudah** membuktikan
nilainya sebagai pembantah: ia yang membatalkan pembacaan `cacah_bulan` sebagai
bentangan kalender (Koreksi 15, lewat BNXUSDTSETTLED 11 lawan 6). Sebuah berkas tak
bersaksi **boleh menjatuhkan** sebuah tafsir; ia **tidak boleh menegakkan** satu pun.

**Utang ukur 21 dan 22 TETAP HIDUP.** Bila penulisnya ditemukan dan berkas diterbitkan
ulang dengan tanggal dan sidik, statusnya naik kembali.

### KEPUTUSAN 9 — KC-57 DIBUANG SEBAGAI KC, ISINYA SUDAH JADI KEWAJIBAN

**KC-57** ("kolom tabel ringkasan buatan sendiri diperlakukan sebagai medan laporan")
**TIDAK diresmikan** dan **DIBUANG dari daftar usulan KC**.

**Sebabnya, tidak berubah sejak v60 dan tetap benar:** kelima barisnya berasal dari
**satu kolom pada satu tabel** — **satu** cacat pembukuan yang tampak lima kali.
Meresmikannya atas dasar lima "kejadian" adalah **KC-47 persis**.

**Tetapi isinya TIDAK hilang:** ia sudah hidup sebagai **syarat praregistrasi butir 13**
(setiap kolom tabel susunan tangan WAJIB menyebut **nama medan sumber dan konvensinya**),
dan syarat itu **DIKUKUHKAN PERMANEN** oleh ADR ini. **Yang dibuang nomornya, bukan
disiplinnya.**

**Preseden yang ditetapkan:** sebuah cacat yang penangkalnya sudah menjadi kewajiban
tertulis **tidak memerlukan nomor KC**. Nomor KC dicadangkan untuk cacat yang
**berulang** dan **belum tertangkal**.

### KEPUTUSAN 10 — KC-58 DITUNDA, DENGAN ALASAN TERSURAT

**TIDAK diputuskan.** Rumusan penuhnya hidup di **EKOR v19**
(`e19c5573966d835e9d40eadcb55165ab7d79f0de`) dan **tidak dibaca ulang pada giliran ini**.
Memutuskannya dari ingatan adalah KC-41.

Yang **sah dicatat** tanpa membaca ulang: statusnya **satu kejadian**, dan bahan yang
akan menentukannya adalah **utang verifikasi 46** — mengapa sembilan dari sepuluh simbol
berabsen kehilangan **tepat** bulan settled terakhirnya sementara **BNXUSDT tidak**.

**MENGIKAT:** ADR-A023 wajib memutuskannya, dengan prasyarat **EKOR dibaca utuh**.

---

## 5. KEPUTUSAN 11 — KC-52 DIPERSEMPIT, TIDAK DICABUT

**KC-52** lahir sebagai: *dua angka yang mengaku tentang "semesta yang sama" ternyata
mencacah himpunan yang berbeda.*

**Yang terukur sejak ia lahir, dan itu banyak:** untuk **BNXUSDT** ketiga angka bersaing
tertutup tanpa sisa — 51 − 50 = **1** (tepi **2022-04**), 50 − 48 = **2** (di dalam:
**2022-06**, **2022-08**), 1 + 2 = **3** ✅ — dan ketiga nama itu **sama persis** dengan
ketiga `lubang_tak_dikenal`. Silang mandiri dari laporan berbeda menutupnya lagi:
9 − 7 = **2** ✅

> **Rumusan KC-52 yang dipersempit [RESMI].** Dua angka atas "semesta yang sama"
> **DILARANG** diperlakukan sebagai mencacah himpunan yang sama **selama keanggotaan
> himpunan itu belum diukur per simbol**. Untuk simbol yang keanggotaannya **sudah**
> diukur dan tertutup secara aritmetika, KC-52 **tidak berlaku**.

**Terukur lunas untuk: BNXUSDT, satu simbol.**
**Tetap berlaku penuh untuk: 786 simbol lain** — **utang ukur 26**.

**DILARANG** menulis bahwa KC-52 dicabut, terselesaikan, atau terbukti sempit. **Satu
simbol dari 787 adalah 0,127% dari semesta**, dan menyebut itu "terdamaikan" tanpa
penyebut adalah **KC-47**.

---

## 6. KEPUTUSAN 12 — ATURAN 90 DIKUKUHKAN, BESERTA KELEMAHANNYA

Aturan 90 diresmikan di STATE v60 atas **tiga kejadian terpisah** (push STATE v58,
STATE v59, EKOR v18), masing-masing pada giliran berbeda dengan blob berbeda. **Ia lolos
ADR-A019 kep. 3 tanpa perlu keputusan 1.** ADR ini **mengukuhkannya**.

**Yang dikukuhkan bersamanya adalah kelemahannya, dan ia wajib ikut tertulis:** sejak
diresmikan, aturan 90 dipakai **lima kali** (ke-63 sampai ke-67) dan **tidak sekali pun
menangkap laporan salah**; kelimanya cocok pada percobaan pertama.

> **DILARANG menyebut aturan 90 "teruji".** Aturan yang belum pernah menyala bukan
> aturan yang terbukti, hanya aturan yang belum diuji. **Nol nyala dari lima pemakaian
> juga DILARANG dibaca sebagai bukti bahwa jebakannya sudah hilang** — tiga kejadian
> aslinya nyata, dan tidak ada satu pun pengukuran yang menyatakan sebabnya lenyap.

**Satu kejadian baru dicatat, dan ia bukan kegagalan aturan 90:** push `c28202df`
(UKUR v19 cacat) menyalakan CI dan laporannya **tertimpa sebelum sempat dibaca**.
Aturan 90 memeriksa **kecocokan**, bukan **keberadaan**. **DILARANG dihitung dalam deret
aturan 38.**

---

## 7. Akibat langsung pada penomoran

**Aturan RESMI sesudah ADR ini:** **1–81, 83, 84, 85, 86 (a dan b), 87, 88, 89, 90, 91,
92.**
Nomor **82** tetap dicadangkan. **Usulan yang tersisa: 77 dan 78 saja.**
**Aturan berikutnya yang bebas: 93.**

**Kelas cacat:** KC-1..KC-55 resmi (KC-16 kosong selamanya). **KC-56 dan KC-57 DIBUANG**
sebagai usulan. **KC-58 satu-satunya usulan KC yang tersisa.**
**KC berikutnya yang bebas: KC-59.**

**Tumpukan sebelum ADR ini:** enam usulan aturan + tiga usulan KC = **sembilan**.
**Sesudahnya:** dua usulan aturan + satu usulan KC = **tiga**. Aritmetika terbuka:
9 − 6 = **3**. **Keenam yang ditutup: aturan 88, 89, 91, 92 (diresmikan); KC-56, KC-57
(dibuang).**

---

## 8. Catatan kejujuran atas ADR ini sendiri

1. **ADR ini melonggarkan sebuah ambang, dan pelonggaran ambang selalu mencurigakan
   ketika dilakukan oleh pihak yang diuntungkan olehnya.** Penangkal yang dipasang:
   pelonggaran dibatasi pada barang bermodal nol (keputusan 1, syarat i–iii), dan
   **KC secara tegas dikecualikan**. Bila kelak sebuah **KC** diresmikan dengan menyebut
   ADR-A022, itu **pelanggaran**, bukan penerapan.

2. **Empat aturan diresmikan sekaligus pada satu giliran.** Itu **banyak**, dan
   patut dicurigai sebagai ledakan aturan. Yang meredakannya: keempatnya **kewajiban
   menulis di praregistrasi**, tidak satu pun menyentuh vonis atau papan skor, dan
   **tidak satu pun dapat mengubah angka terukur mana pun**. Bila kelak terbukti
   keempatnya hanya menambah upacara tanpa mencegah satu cacat pun, **ADR-A023 atau
   sesudahnya WAJIB mencabutnya** — dan pencabutan itu **tidak** boleh disebut kekalahan
   metodologis, melainkan pengukuran yang bekerja.

3. **Tiga barang ditunda** (aturan 77, 78, KC-58). STATE v61 menulis bahwa membiarkan
   usulan menggantung satu ADR lagi "wajib dicatat sebagai cacat proses". **Dicatat di
   sini, tanpa pembelaan:** ketiganya menggantung satu ADR lagi. Yang membedakannya dari
   penundaan sebelumnya hanyalah bahwa **alasannya kini tunggal, terukur, dan dapat
   dihapus** — tiga berkas dibaca utuh, selesai.

4. **Tidak satu pun keputusan di ADR ini menyentuh papan skor 329.** Tidak ada vonis
   yang diubah, dibatalkan, atau ditafsir ulang (aturan 29).

---

## 9. Yang WAJIB dikerjakan berikutnya

1. **STATE v62** — menyerap ADR ini: aturan 88, 89, 91, 92 masuk daftar RESMI; KC-56 dan
   KC-57 dihapus dari usulan; rumusan KC-52 yang dipersempit; kelas **BAHAN TAK
   BERSAKSI**; daftar larangan disesuaikan.
2. **EKOR v20 dan UKUR v20** — menaikkan kepala ke "milik STATE v62" (**utang penamaan**
   dari v61) dan menyerap keputusan yang menyentuh lajurnya.
3. **Syarat praregistrasi R-319 naik dari lima belas** — butir yang dulu ditulis sebagai
   "semangat usulan 88/89" dan "usulan 91" kini **kewajiban aturan resmi**, dan
   **aturan 92** menambah kewajiban penanda penutup bagi setiap berkas akar.
4. **ADR-A023 — MENGIKAT, tiga butir:** (a) aturan **77**; (b) aturan **78**; (c)
   **KC-58**. **Prasyarat tersurat:** teks penuh aturan 77 dan 78 dan `STATE_LAMPIRAN_EKOR.md`
   dibaca UTUH lebih dulu.
5. **Poros riset tetap tidak berubah peringkatnya: utang ukur 25** — klausa mana dari
   enam klausa `gerbang_1m.py` yang menjatuhkan **BNXUSDT 2022-06 dan 2022-08**. Karena
   `gerbang_1m.py` **pustaka murni tanpa keluaran**, ia **menuntut pemanggilnya
   ditelusuri**. Bahan berperingkat tertinggi: **`decisions/ADR-A004` §2** dan
   **`tests/test_gerbang_1m.py`**.

— akhir `decisions/ADR-A022.md` —
