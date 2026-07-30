# STATE — versi 50 (bagian 1 dari tiga)

Diperbarui: 2026-07-30 (sesi 60, giliran lanjutan). Aturan hanya BERTAMBAH; jangan
menulis ulang dari ingatan. v50 disusun di atas `STATE.md` v49 (blob
**`64dc7b3fed15b447f297874e8410c9a6c4b7dd4e`**), yang **DIBACA UTUH pada giliran ini
sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43).

**KETIMPANGAN VERSI — kembali seperti v49, bagian 1 naik lebih dulu.** Kedua lampiran
baru saja lunas di v9 pada giliran sebelumnya dan kini tertinggal satu ramalan lagi:

1. `STATE.md` **v50** — berkas ini. Memuat R-310, papan skor **310**, aturan **84
   DIRESMIKAN**, **KC-50 DIRESMIKAN**, usulan **H-A020**, koreksi selisih **516.135**.
2. `STATE_LAMPIRAN_EKOR.md` **v9** — blob `beaed54cb93e00c2c56f1aaa8d1c2709c97f08d0`.
   **USANG SEBAGIAN:** papan skor masih 309, jumlah uji masih 1233, ADR sampai A016.
3. `STATE_LAMPIRAN_UKUR.md` **v9** — blob `0b795fb48ababa61b318518ce1196ad90467e077`.
   **USANG SEBAGIAN:** belum memuat API `keterisian_lilin` V1, belum memuat sembilan
   baris MATI tak penuh, dan cacah modul/uji/workflow masih 47 / 51 / 42.

**Sampai EKOR v10 dan UKUR v10 naik, sumber sah untuk hasil R-310 adalah
`journal/2026-07-30-132.md` (blob `35c5400ea2a6fb6191c26bd5d7f7dbc3f630b2f0`),
`reports/keterisian_lilin.json` (blob `14f1772070789dad603b132ece034ea4c19c6e3d`), dan
`reports/keterisian_lilin_ringkas.json` (blob `f33714eda66e77d37a7024b52c433ead070b16c7`).**
Bila lampiran bertentangan dengan berkas ini soal R-310, berkas SUMBER menang (KC-41).

Sebab pemecahan tetap sama: `push_files` menulis ulang SELURUH berkas, dan menyusun
tiga berkas besar dari satu konteks yang sudah terpakai banyak adalah cara paling
pasti merusak aturan 1–84 (KC-42, KC-43).

## STATE DIPECAH TIGA — BACA INI LEBIH DULU

Pembagian yang MENGIKAT sejak v43, berlanjut di v50:

1. **`STATE.md`** (berkas ini) — **bagian 1**: kepala, aturan bernomor 1–**84** (plus
   usulan 77, 78, 82), kelas cacat KC-1..**KC-50**. Berkas ini berhenti sesudah kelas
   cacat.
2. **`STATE_LAMPIRAN_EKOR.md`** v9 — **bagian 2**: papan skor R-199..R-309, catatan
   kejujuran, jumlah uji 1233, utang verifikasi, Daftar ADR A001–A016, temuan
   sampingan, penomoran berikutnya. **Angka-angka itu kini tertinggal satu ramalan.**
3. **`STATE_LAMPIRAN_UKUR.md`** v9 — **bagian 3**: penyebut 787, taksonomi, karantina,
   bulan ABSEN, hipotesis H-A001..H-A019, lubang funding, byte parquet semesta, lebar
   zona irisan byte, modul/workflow/uji, API terverifikasi.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip ekor v41; bukan sumber lagi.

**Ketiga berkas wajib dibaca bersama.** LANGKAH 0 PROMPT wajib menyebut ketiganya.

Yang lahir sejak v49: adjudikasi **R-310 = TEPAT** (dua butir berisiko menang, satu
butir mudah cocok); modul **`keterisian_lilin` V1** (sidik
`1cd98f4fa22c24b30f31f5b36dac0ea0bb3fa9de44e5e15ae73cbf11cdca08bb`); CI 1233 →
**1297**; **aturan 57 beruntun 2 dari 2**; **aturan 84 DIRESMIKAN**; **KC-50
DIRESMIKAN**; **H-A020 DIUSULKAN**; dan satu koreksi aritmetis besar: **jumlah lilin
semesta 839.325.999 BUKAN total baris parquet 839.842.134 — selisih 516.135.**

## KOREKSI BESAR — dua angka yang selama ini disamakan ternyata berbeda

Ditulis lebih dulu karena mengubah bacaan kalimat lama, bukan hanya menambah.

- **TERUKUR:** `jumlah_lilin_langsung` = **839.325.999** lilin, dijumlahkan LANGSUNG
  dari medan `cacah_lilin` pada 19.586 baris laporan kehidupan.
- **TERCATAT BERULANG di repo:** total baris parquet semesta = **839.842.134**, dari
  run rilis 30404071324 (29/29 aset).
- **SELISIH = 516.135.** Kedua besaran BUKAN besaran yang sama.

**Akibat yang mengikat:** setiap kalimat di jurnal 131 §6 dan di berkas mana pun yang
memperlakukan "total baris parquet" sebagai "jumlah lilin di penyebut 19.586" harus
dibaca ulang dengan koreksi ini. Seluruh aritmetika implikasi jurnal 131 §6 dibangun
di atas penyamaan itu dan karenanya SALAH sebagai turunan, meskipun ramalan R-310
sendiri tetap menang di dalam pitanya (pita dikunci sebelum pengukuran, aturan 29).

**Dugaan, BELUM DIUJI, DILARANG dikutip sebagai temuan:** 19.598 − 19.586 = 12
simbol-bulan karantina, dan 516.135 / 12 = 43.011 ≈ satu bulan penuh lilin menit.
Kesesuaian angka itu menarik dan justru karena itu harus diuji, bukan dipercaya. Calon
butir R-311.

## KOREKSI SALAH KETIK — jurnal 132 §3 (utang dari giliran sebelumnya, LUNAS di sini)

Judul `journal/2026-07-30-132.md` §3 berbunyi **"beruntun 2/1"**. Itu SALAH KETIK.
Badan teks di bagian yang sama menulis **"Beruntun 2/2"**, dan **2/2 yang benar**:
aturan 57 tepat pada R-309 (1233) dan tepat lagi pada R-310 (1297). Berkas jurnal
TIDAK diperbaiki dengan push ulang, dengan sebab tertulis: `push_files` menulis ulang
seluruh berkas, sehingga memperbaiki satu karakter berarti menyusun ulang 14 KB dari
konteks yang sudah terpakai banyak — persis cara yang dicatat KC-42 sebagai paling
pasti merusak berkas. **Koreksi ini berlaku dari berkas ini; bila jurnal 132 dan STATE
v50 bertentangan pada titik ini, STATE v50 menang.** Ini pengecualian tersurat atas
KC-41 ("berkas sumber menang") yang hanya berlaku untuk salah ketik yang sudah diakui
dan tidak menyangkut angka terukur.

## Aturan bernomor

Aturan **1–36** berlaku tanpa perubahan; teks di STATE v19 (blob `e06c486e…`),
ringkas di v37 (blob `f520d5e2`).

**Aturan 10 (irisan/urutan bulan BUKAN sebab). [v50] Ditaati.** R-310 mengukur bahwa
**95,5%** defisit lilin semesta (17.335.439 dari 18.143.601) menumpuk di bulan pertama
simbol. Itu pernyataan SEBARAN, bukan sebab. Rumusan yang boleh dikutip: *bulan pertama
simbol rata-rata terisi ±49,7% dari lilin penuhnya (defisit rata 22.027 dari 44.640-an),
sementara bulan bukan-pertama menanggung hanya 0,0445 bagian defisit.* DILARANG
mengubahnya menjadi pernyataan sebab.

**Aturan 21 (total papan skor dihitung tangan). [v50] Ditaati:** 217 + 57 = 274;
274 + 21 = 295; 295 + 8 = 303; 303 + 7 = **310**. Rincian: TEPAT **217** · MELESET 57
· SEPARUH 21 · TIDAK TERADJUDIKASI 8 · MENUNGGU 7. N_percobaan = 0. ADJUDIKASI RISET
TETAP TERKUNCI. MENUNGGU: R-7, R-19, R-20, R-28, R-36, R-37, R-199.

**Aturan 29 (pita praregistrasi TIDAK boleh diubah sesudah pengukuran). [v50]
Ditaati, dan kali ini godaannya nyata.** Pita R-310 dikunci di jurnal 131 sebelum
`keterisian_lilin.py` ada: butir 1 (cacah baris MATI tak penuh) 1..120, butir 2
(bagian defisit bukan-pertama) 0,02..0,25. Terukur **9** dan **0,0445** — keduanya
di dalam pita tetapi dekat tepi BAWAH. Catatan kejujuran yang WAJIB ikut dikutip:
kedua kemenangan itu tipis ke arah bawah, sehingga tidak boleh dibacakan sebagai
konfirmasi kuat; pita yang lebar di sisi atas membuat kemenangan lebih murah daripada
yang tampak.

**Aturan 36 (dua modul berbeda atas semesta sama wajib cocok). [v50] Ditaati untuk
keempat kalinya:** kedelapan invarian `keterisian_lilin` V1 berselisih NOL terhadap
catatan semesta — penyebut 19.586 · simbol 787 · HIDUP 18.087 · SEPI 98 · MATI 1.401 ·
total byte 32.706.262.375 · byte HIDUP 32.049.492.952 · `cacah_hidup_byte_kecil` 38.

**Aturan 43 (toleransi berskala). [v50]** Tidak mendapat bentuk kegagalan baru.

Aturan **37, 39–45, 47, 49, 51, 53, 54, 56, 59–62** berlaku tanpa perubahan;
ringkas satu baris: 37 kelas cacat pada sampel · 39 keseragaman sampel bukan ramalan
· 40 uji silang baris · 41 penyebut nol → TIDAK TERADJUDIKASI · 42 kelas cacat butuh
angka terukur · 43 toleransi berskala · 44 ramalan menyebut penyebut · 45 keatomikan
push pemicu · 47 satuan cacah tersurat · 49 re-export mematahkan uji · 51 jendela
mundur adaptif · 53 ramalan kode keluar butuh pembacaan perilaku · 54 cacah
`def test_` satu per satu · 56 commit BERIKUTNYA yang menyentuh X · 59 ketiadaan
gejala butuh penyebut · 60 mekanisme tak dipindah antarkasus · 61 medan tak dipindah
antarjalur · 62 daftar tak diminta dari laporan bercacah.

Yang berikut memuat angka atau daftar kepatuhan, jadi ditulis agak penuh:

38. Cacah uji hanya sah dari `reports/ci_terakhir.json` (run id + commit +
    `kode_keluar`). **[v50] Ditaati DUA KALI:**
    - pemakaian ke-**36**: blob **`016fb2349a960100d270bec926e73d5b2c85e9cc`**, run
      **30533500210**, commit `f8098980` (UKUR v9), kode 0, **1233** butir;
    - pemakaian ke-**37**: blob **`3c07c9093d5232ce3852b2ac509fd9e9875f0f33`**, run
      **30535202643**, commit `924b0d7afcf1f9e17965dff931d36489ad27f01b`,
      2026-07-30T10:35:00Z, kode 0, **1297** butir (`1297 tests collected in 0.60s`).
    Total pemakaian tercatat: **tiga puluh tujuh**.
    **Catatan jujur yang WAJIB ikut:** `ci_terakhir.json` hanya menyimpan run TERAKHIR,
    sehingga ramalan "CI tetap 1233" untuk push STATE v49 (`8dd0e4a5`), EKOR v9
    (`a3830617`), dan PROMPT v53 (`ec885f7e`) TIDAK PERNAH TERUKUR. Bukan tepat, bukan
    meleset; DILARANG dicatat sebagai kemenangan.
45. Keatomikan push pemicu. **[v50] Ditaati:** trio `keterisian_lilin` (modul + uji +
    workflow) didorong dalam SATU `push_files`
    (**`924b0d7afcf1f9e17965dff931d36489ad27f01b`**).
46. Kode dilarang menyimpulkan dari penyebut nol. **[v50] Ditaati di
    `keterisian_lilin` V1:** `bagian_defisit_bukan_pertama` mengembalikan **null**,
    bukan 0, bila `defisit_total` nol.
47. Satuan cacah tersurat. **[v50] Ditaati:** "9" dan "1.392" bersatuan **simbol-bulan
    MATI**; "18.143.601", "17.335.439", "808.162", "95.237", "712.925", "516.135"
    bersatuan **lilin menit**; "839.325.999" bersatuan **lilin menit**; "839.842.134"
    bersatuan **baris parquet** — dan kedua satuan terakhir itu BERBEDA (lihat koreksi
    di atas); "0,0445" adalah **bagian tanpa satuan**.
48. Berkas modul mendekati 800 baris dipecah sebelum fungsi baru ditambahkan.
    `silang_funding.py` (29.873 B) dan `funding.py` (28.121 B) terbesar;
    `keterisian_lilin.py` di bawah batas.
50. Setiap pengukuran yang menyimpulkan dari KETIADAAN wajib memuat kendali positif.
    **[v50] Ditaati di `keterisian_lilin` V1:** `kendali_deteksi` memakai semesta
    buatan yang jawabannya dihitung tangan lebih dulu (`JAWABAN_KENDALI`: mati tak
    penuh 3, mati penuh 1, defisit total 1.160, pertama 520, bukan-pertama 640,
    jumlah lilin 213.400, defisit negatif 0, bagian 0,5517) — seluruhnya cocok.
    `kendali_data` membaca tiga bulan BTCUSDT (2021-05, 2021-08, 2021-01) dan
    memastikan ketiganya HIDUP dengan `cacah_lilin` **44.640** penuh.
    **Ini penting:** temuan "0 dari 19.586 baris tanpa lilin" hanya boleh dibaca karena
    kendali negatifnya membuktikan modul BISA mendeteksi baris tanpa lilin.
52. Laporan yang tidak dapat dibaca utuh setara dengan laporan yang tidak ada.
    **[v50] Ditaati untuk tujuh berkas:** `lux_ai/serapan/keterisian_lilin.py`
    (**`3f80ffa72008008d567ef32f9f278b8931e91ac3`**), `tests/test_keterisian_lilin.py`
    (**`f58912d0b1531dbf537de4c0b4f0a803a3ad1f69`**),
    `.github/workflows/keterisian_lilin.yml`
    (**`d821c63a462a8338ccd63f8014f7c8847602fdff`**) dibaca ulang UTUH sesudah push
    `924b0d7a`; `reports/keterisian_lilin_ringkas.json` (**`f33714ed`**) dan
    `reports/keterisian_lilin.json` (**`14f1772070789dad603b132ece034ea4c19c6e3d`**,
    6.588 B) dibaca UTUH; `journal/2026-07-30-131.md` (**`cae9ab53`**) dan
    `journal/2026-07-30-132.md` (**`35c5400e`**) dibaca ulang UTUH sesudah pushnya.
    Utang yang TETAP hidup: `tests/test_bentangan_kohort.py` V2 (63 butir, blob
    `9f850ecd`) belum dibaca ulang byte demi byte — **kini DELAPAN versi menunggu.**
55. Rumusan pemicu workflow wajib dikutip dari berkas workflow beserta blobnya.
    **[v50] Ditaati:** `keterisian_lilin.yml` (blob `d821c63a`) dibaca UTUH — `paths`
    **satu entri saja**, `- 'lux_ai/serapan/keterisian_lilin.py'`.
57. Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB ditulis bernomor.
    **[v50] BERUNTUN 2 DARI 2** sesudah putus di giliran ke-27. Daftar **64** butir
    (`test_01`..`test_64`) ditulis bernomor satu nama per nomor, **tanpa rentang**,
    SEBELUM ramalan diucapkan; ramalan **1233 + 64 = 1297, kode 0**; terukur **1297,
    kode 0**. Dua helper (`_ringkasan_sehat`, `_selisih_nol`) sengaja berawalan garis
    bawah agar tidak dikumpulkan pytest — itulah yang membuat ramalan tidak meleset
    ke atas. Kemenangannya **MUDAH** dan TIDAK masuk papan skor.
58. Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH DILARANG
    diramalkan dengan pita sempit.
63–76. Berlaku tanpa perubahan dari v43. Teks penuh di v43 (blob `a91a4934`).

**Aturan 66 (cacah direktori dengan TANGAN, bernomor). [v50] TIDAK dapat diklaim
taat pada ref mutakhir — ini UTANG, bukan kepatuhan.** Cacah tangan terakhir yang sah
ada pada ref **`07a69d395ea7cbc07bda506b59f3e97b4574a11f`**: `lux_ai/serapan/` **47**,
`tests/` **51**, `.github/workflows/` **42**. Sesudah trio R-310 angka yang beredar
(48 / 52 / 43) adalah **TURUNAN dari pengurangan**, persis yang dilarang aturan 66 dan
dicatat KC-33. **Angka 48 / 52 / 43 DILARANG dikutip sebagai terukur sampai dicacah
satu per satu bernomor pada ref mutakhir.**

**Penomoran aturan [v50].** Aturan **84 DIRESMIKAN** giliran ini. Aturan resmi kini:
**1–81, 83, dan 84**. Nomor **82** tetap dicadangkan untuk usulan yang belum berlaku.
**Aturan berikutnya yang bebas: 85.** Nomor tidak ditulis dari ingatan; seluruhnya
dibaca dari v49.

**Aturan 77 (TETAP DIUSULKAN, belum berlaku):** dua berkas laporan berblob IDENTIK
bukan dua pengukuran. Baru satu kasus. **[v50] Tidak menguat:**
`keterisian_lilin.json` dan `_ringkas.json` berblob BERBEDA, seperti seharusnya.

**Aturan 78 (TETAP DIUSULKAN, belum berlaku — MENGUAT LAGI [v50]):** batas panjang
alat adalah bagian dari DESAIN repo. Bukti pendukung baru: `BATAS_BARIS_LAPORAN=40`
membuat `keterisian_lilin.json` (6.588 B) terbaca UTUH dalam satu bacaan meski memuat
daftar baris bertanda — kali keempat berturut. Belum diresmikan karena ini kasus
rancangan, bukan pengukuran batasnya sendiri.

**Aturan 79 (BERLAKU sejak v44). [v50] Ditaati di R-310:** praregistrasi ditulis di
`journal/2026-07-30-131.md` (yang ada di `paths-ignore`) SEBELUM
`keterisian_lilin.py` ada, lalu disalin apa adanya ke tetapan modul
(`R310_PITA_BUTIR_1=(1,120)`, `R310_PITA_BUTIR_2=(0.02,0.25)`) dan tidak diubah.

**Aturan 80 (BERLAKU sejak v46). [v50]** R-310 tidak menguji arah waktu.

**Aturan 81 (BERLAKU sejak v46) — numerator yang dikuasai satu bulan kalender wajib
dilapor sebagai kemungkinan artefak satu peristiwa. [v50] Ditaati, dan kali ini
mengubah bacaan hasil secara serius:** dari sembilan baris MATI tak penuh, **TUJUH
berbulan `2024-05`** (FOOTBALLUSDT, ANTUSDT, BTSUSDT, SRMUSDT, HNTUSDT, TOMOUSDT,
COCOSUSDT), dengan `cacah_lilin` 39.308–39.317 — rentang selebar **9 lilin**. Itu jauh
di atas ambang 1/4. Maka numerator 9 **BUKAN sembilan pengamatan bebas**; paling banter
tiga: satu peristiwa 2024-05, LENDUSDT 2020-11, dan FRONTUSDT 2024-09.

**Aturan 82 (TETAP DIUSULKAN, belum berlaku; nomor dicadangkan) — ambang yang MUSTAHIL
dilewati ATAU yang hasilnya SUDAH TERSIRAT oleh ukuran sebelumnya DILARANG dipakai
sebagai butir berisiko.** Teks penuh seperti v48. Dasar tetap: butir 2 R-307 dan butir
2 R-308. **[v50] MENGUAT tanpa kasus kegagalan baru, karena bekerja sebagai PENCEGAH:**
tiga calon butir R-310 dibuang SEBELUM dikunci — (a) cacah baris MATI berlilin penuh,
yang sudah tertentu di ≈1.370–1.401 dan **terukur 1.392, tepat di dalam rentang yang
sudah dihitung sebelum mengukur**; (b) cacah baris MATI dengan `cacah_lilin` < 1.440,
hampir pasti 0; (c) nisbah byte-per-lilin MATI:HIDUP, tersirat 0,233. Pencegahan bukan
pengukuran, jadi aturan 82 TETAP usulan.

**Aturan 83 (BERLAKU sejak v49). [v50] Ditaati untuk kedua kalinya:** aritmetika
implikasi R-310 ditulis di jurnal 131 §6 sebelum pita dikunci. Hasil adunya dengan
kenyataan, ditulis apa adanya termasuk yang meleset: defisit semesta taksir 18.612.246
→ terukur **18.143.601** (−2,5%); defisit bulan pertama taksir 17.247.105 → terukur
**17.335.439** (+0,5%); bagian bukan-pertama taksir 0,073 → terukur **0,0445**
(taksiran meleset ±64% ke atas, dan justru itu yang membuat butir 2 tetap berisiko).
**Peringatan yang menempel pada catatan ini:** taksiran itu dibangun di atas penyamaan
839.842.134 dengan jumlah lilin, yang kini terbukti salah sebesar 516.135. Aturan 83
dipenuhi secara bentuk, tetapi bahan bakunya cacat — dan cacat itulah yang melahirkan
KC-50 di bawah.

**Aturan 84 (DIRESMIKAN [v50]; diusulkan sejak ADR-A016 kep. 3) — butir praregistrasi
yang memakai klausa ATAU wajib melaporkan sumbangan BEBAS setiap klausa secara
terpisah, bukan hanya cacah gabungannya. Bila sumbangan bebas itu tidak dapat dilapor
terpisah, klausa ATAU DILARANG dipakai; pecah menjadi butir tersendiri.**

*Dasar peresmian, dua kasus dengan bentuk berbeda:*
1. **Kegagalan terukur (R-309):** butir 1 berbunyi "bulan PERTAMA simbol ATAU bulan
   `2026-06`" dan menang 37 dari 38 — tetapi ketiga baris `2026-06` **juga** bulan
   pertama, sehingga klausa kedua menyumbang **NOL** secara bebas. Klausa yang tidak
   bekerja bersembunyi di balik klausa yang bekerja. R-309 lolos dari akibat
   terburuknya hanya karena modulnya kebetulan menyimpan medan `pertama` dan `tepi`
   per baris — kebetulan bukan penangkal.
2. **Penerapan preventif yang berhasil (R-310):** kedua butir berisiko sengaja
   dirumuskan dengan klausa TUNGGAL ("cacah baris MATI ber-`cacah_lilin` kurang dari
   lilin penuh bulannya"; "bagian defisit yang ditanggung baris bukan-pertama"), dan
   pelaporan per baris membuat setiap angka dapat dibongkar sampai ke barisnya. Tidak
   ada satu pun angka R-310 yang bergantung pada klausa gabungan.

Bentuk pelaksanaannya karena itu sudah diuji ke dua arah: sekali sebagai kegagalan
yang terdeteksi, sekali sebagai rancangan yang mencegahnya. Kerabat aturan 44, 47, 59,
81; kerabat KC-47.

## Kelas cacat

KC-1 s.d. KC-12 seperti v19; KC-10 dan KC-11 DITUTUP. KC-13 keterwakilan sampel.
**KC-16 DITARIK — nomornya TETAP kosong selamanya.** KC-17 DITUTUP. Teks penuh
KC-14, KC-15, KC-19..KC-29 ada di v37 (blob `f520d5e2`). KC-30..KC-42 ada di v43
(blob `a91a4934`). KC-43, KC-44 teks penuh di v44 (blob `ede3ce3b`). KC-45, KC-46
teks penuh di v45 (blob `e07f2de1`). KC-47 teks penuh di v46 (blob `41b5b585`).
KC-48 teks penuh di v47 (blob `7642b75d`). KC-49 teks penuh di v48 (blob
`2fd136e4`).

Ringkas KC-19..KC-50 satu baris: KC-19 mencacah dari ingatan · KC-20 bias ke bawah
· KC-21 ketiadaan gejala dari ketiadaan pengukuran · KC-22 mekanisme dipindah ·
KC-23 medan dipindah · KC-24 daftar dari laporan bercacah · KC-25 batas semesta tak
tersurat · KC-26 medan ekstrem membisu tentang seri · KC-27 karakterisasi dari
contoh berurut · KC-28 mencampur kelas instrumen · KC-29 taksonomi paralel · KC-30
nama kelas dibaca sebagai keadaan · KC-31 nama peristiwa dibaca sebagai mekanisme ·
KC-32 dua sistem penomoran dicampur · KC-33 mengenali satu peristiwa lalu berhenti ·
KC-34 cacah subkelompok dari pengurangan kepala · KC-35 cakupan kode dicampur
dengan cakupan laporan · KC-36 homonim diperlakukan satu konsep · KC-37 nol dari
satu penyebut sebagai bukti di penyebut lain · KC-38 kecocokan tanpa membedakan
mekanisme · KC-39 dua penyebut bulan absen dicampur · KC-40 daftar klausa gagal
dibaca sebagai keadaan · KC-41 pemicu workflow dirumuskan dari ingatan · KC-42
menulis ulang berkas melampaui batas push · KC-43 tanda tangan fungsi dari ingatan ·
KC-44 semua laporan di-commit satu langkah · KC-45 satuan "bulan tanpa funding" dan
"bulan MATI" dicampur · KC-46 lubang bentuk AWAL dibaca sebagai "funding berhenti" ·
KC-47 satu peristiwa menyamar sebagai banyak pengamatan bebas · KC-48 ambang absolut
pada besaran yang sebarannya belum pernah diukur · KC-49 pita dikunci tanpa
menghitung implikasi aritmetis momen yang sudah terukur · **KC-50 agregat dihitung
lewat jalan memutar sehingga selisihnya tak terlihat.**

**KC-41 — tetap berlaku, kasus lama tidak dihapus.** Penangkal: rumusan pemicu, label
hipotesis, dan nomor aturan WAJIB dikutip dari berkas beserta blobnya pada giliran
yang sama. Bila dua bagian STATE bertentangan, berkas SUMBER menang, bukan yang lebih
baru — dengan satu pengecualian tersurat untuk salah ketik jurnal 132 §3 di atas.

**KC-47 — [v50] KASUS BARU yang KUAT.** Tujuh dari sembilan baris MATI tak penuh
berbagi bulan `2024-05` dan berjendela sembilan lilin. Bila kesembilan baris itu
dibaca sebagai sembilan pengamatan bebas, kesimpulan apa pun tentang "bentuk kematian
sebagian" akan dihitung dari penyebut palsu. Penangkal yang dipakai: aturan 81, dan
pelaporan per baris di `keterisian_lilin.json`.

- **KC-48 [RESMI sejak v47]** — ambang absolut pada besaran yang sebarannya belum
  pernah diukur. Teks penuh di v47. Penangkal: usulan aturan 82.

- **KC-49 [RESMI sejak v48]** — pita praregistrasi dikunci tanpa lebih dulu menghitung
  implikasi aritmetis dari momen yang SUDAH terukur. Penangkalnya BERLAKU sebagai
  aturan 83.

- **KC-50 [DIRESMIKAN v50; diusulkan sejak ADR-A015 kep. 7, diperkuat ADR-A016 kep. 5]
  — agregat semesta dihitung lewat jalan memutar (dijumlahkan dari total per kelas
  atau dari angka yang sudah tercatat) alih-alih LANGSUNG dari baris, sehingga selisih
  terhadap sumber lain menjadi mustahil terlihat.**

  *Bentuknya:* sebuah angka besar dipakai berulang di banyak berkas. Karena tidak
  pernah dihitung ulang dari baris, tidak ada satu pun momen di mana ia dapat
  bertabrakan dengan angka lain. Cacatnya tidak menghasilkan galat; ia menghasilkan
  KESUNYIAN.

  *Dua kasus terukur:*
  1. **`irisan_byte.ringkaskan`** — `total_byte` dihitung sebagai jumlah byte keempat
     kelas, sehingga `selisih_total_byte` tersirat secara aritmetis. Sembilan medan
     selisih di sana = **delapan pemeriksaan bebas + satu turunan**; menyebut
     "sembilan pemeriksaan bebas" DILARANG.
  2. **Total baris parquet 839.842.134** — dipakai berulang sebagai kalau-kalau ia
     jumlah lilin, tanpa pernah dijumlahkan dari medan `cacah_lilin`. Begitu
     `keterisian_lilin` V1 menghitungnya LANGSUNG, muncul **839.325.999**, dan selisih
     **516.135** yang selama ini tidak terlihat langsung tampak. Ini kasus kedua yang
     ditunggu v49, dan bentuknya lebih tajam daripada kasus pertama: yang pertama
     hanya membuat pemeriksaan terhitung berlebih, yang kedua menyembunyikan
     ketidakcocokan nyata antardua sumber.

  *Penangkal, WAJIB bagi modul baru (ADR-A016 kep. 5, kini berstatus kelas cacat
  resmi):* setiap agregat semesta dihitung LANGSUNG dari baris dalam jalur hitung
  tersendiri, dan bila ada angka setara yang sudah tercatat di repo, keduanya WAJIB
  diadu dan selisihnya dilaporkan — termasuk ketika selisihnya nol. `keterisian_lilin`
  V1 sudah memenuhi ini lewat `jumlah_lilin_langsung`. Kerabat KC-34, KC-35; kerabat
  aturan 36, 40, 83.

## Hipotesis baru yang DIUSULKAN di giliran ini

**H-A020 (DIUSULKAN, BELUM DIUJI) — tujuh baris MATI tak penuh berbulan `2024-05`
adalah SATU peristiwa penghentian bersama, bukan tujuh penghentian yang kebetulan
berdekatan.** Dasar terukur: `cacah_lilin` ketujuhnya 39.308, 39.309, 39.310, 39.311,
39.312, 39.315, 39.317 — jendela **9 lilin** pada penuh 44.640.

**Yang DILARANG ditulis sebagai temuan sampai diuji** (jurnal 132 §8): kalimat "tujuh
simbol didelisting 28 Mei 2024". Yang terukur HANYA jendela sembilan lilin. Mengubah
cacah lilin menjadi titik waktu mengandaikan tidak ada lubang di tengah bulan itu, dan
andaian tersebut BELUM diuji. Uji yang menegakkan atau meruntuhkannya: lubang tengah
pada gugus `2024-05`.

## Ke bagian 2 dan 3

Berkas ini berhenti di sini dengan sengaja. Lanjutannya:

- **Papan skor.** Keadaan MUTAKHIR ada di berkas ini (aturan 21 di atas): total
  **310** — TEPAT 217 · MELESET 57 · SEPARUH 21 · TIDAK TERADJUDIKASI 8 · MENUNGGU 7.
  Rincian per ramalan masih di `STATE_LAMPIRAN_EKOR.md` v9 (blob `beaed54c`), yang
  totalnya masih 309 dan jumlah ujinya masih 1233. **EKOR v10 wajib menambahkan baris
  R-310 = TEPAT dan jumlah uji 1297.**
- **Penyebut 787, taksonomi, karantina, bulan ABSEN, hipotesis H-A001..H-A020, byte
  parquet semesta, lubang funding, modul/workflow/uji, API terverifikasi** →
  `STATE_LAMPIRAN_UKUR.md` v9 (blob `0b795fb4`). **UKUR v10 wajib menambahkan API
  `keterisian_lilin` V1, kesembilan baris MATI tak penuh, angka defisit, koreksi
  516.135, dan H-A020 sebagai usulan.**

**Hasil R-310 secara ringkas (sumber: jurnal 132, `reports/keterisian_lilin.json`,
`reports/keterisian_lilin_ringkas.json`):** lima penggugur bersih — `sidik_seragam`
true, 8/8 laporan terbaca, `cacah_kunci_ganda` 0, `cacah_defisit_negatif` 0,
`cacah_baris_tanpa_lilin` **0 dari 19.586**; ketiga kendali data lolos; kedelapan
selisih invarian nol. Butir 1 BERISIKO **9**, pita 1..120 — MENANG. Butir 2 BERISIKO
**0,0445**, pita 0,02..0,25 — MENANG. Butir 3 MUDAH — cocok, tidak diskor. Adjudikasi
**TEPAT**. Angka pendamping: `cacah_mati_penuh` 1.392 · `defisit_total` 18.143.601 ·
`defisit_pertama` 17.335.439 (95,5%) · `defisit_bukan_pertama` 808.162 · jumlah defisit
sembilan baris 95.237 (0,1178 dari 808.162) · **sisa 712.925 lilin BELUM dijelaskan.**

Ramalan berikutnya **R-311** (poros BELUM ditetapkan; ADR-A016 menolak penyusunan
percobaan pada giliran yang sama dengan adjudikasi. Calon urut kekuatan: (1) selisih
**516.135** lawan dugaan 12 simbol-bulan karantina; (2) berapa baris menanggung sisa
**712.925** lilin bukan-pertama non-MATI; (3) lubang tengah pada gugus `2024-05` untuk
menegakkan atau meruntuhkan H-A020). Jurnal berikutnya **133**, PROMPT berikutnya
**v54**, ADR berikutnya **A017**, KC berikutnya **KC-51**, aturan berikutnya **85**,
hipotesis berikutnya **H-A021**. Papan skor sesudah R-311 = **311**.
