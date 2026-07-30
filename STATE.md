# STATE — versi 49 (bagian 1 dari tiga)

Diperbarui: 2026-07-30 (sesi 60, giliran lanjutan). Aturan hanya BERTAMBAH; jangan
menulis ulang dari ingatan. v49 disusun di atas `STATE.md` v48 (blob
**`2fd136e404f2085e5b188c896b5499d4f98e1ecc`**), yang **DIBACA UTUH pada giliran ini
sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43).

**KETIMPANGAN VERSI BARU — kali ini TERBALIK dari v48.** Bagian 1 naik lebih dulu;
kedua lampiran masih v8 dan memuat keadaan SEBELUM R-309:

1. `STATE.md` **v49** — berkas ini. Memuat R-309, papan skor **309**, aturan **83
   DIRESMIKAN**, usulan aturan **84**, cacah tangan **47 / 51 / 42**.
2. `STATE_LAMPIRAN_EKOR.md` **v8** — blob `c34c88e27dce4813622c2e3ea71bf4d486ec65d6`.
   **USANG SEBAGIAN:** masih menulis papan skor 308, jumlah uji 1168, dan ADR sampai
   A015.
3. `STATE_LAMPIRAN_UKUR.md` **v8** — blob `ff19069512bd4604b18cedb896af1d6cf6ba2557`.
   **USANG SEBAGIAN:** H-A019 masih tercatat BELUM diuji, dan praregistrasi R-309
   masih tercatat sebagai menunggu.

**Sampai EKOR v9 dan UKUR v9 naik, sumber sah untuk hasil R-309 adalah
`journal/2026-07-30-130.md` (blob `d4c48ae45a6fbeffdf473824f3fa69f6506ed909`),
`decisions/ADR-A016.md` (blob `209802d7b5eeff9a0d66f13d552b83145acb9dd6`), dan
`reports/bulan_pertama.json` (blob `0a2aa6ae15d949b44803dffdc9e97dbd322bbc85`).**
Bila lampiran bertentangan dengan berkas ini soal R-309, berkas SUMBER menang
(KC-41).

Sebab pemecahan tetap sama: `push_files` menulis ulang SELURUH berkas, dan menyusun
tiga berkas besar dari satu konteks yang sudah terpakai banyak adalah cara paling
pasti merusak aturan 1–83 (KC-42, KC-43).

## STATE DIPECAH TIGA — BACA INI LEBIH DULU

Pembagian yang MENGIKAT sejak v43, berlanjut di v49:

1. **`STATE.md`** (berkas ini) — **bagian 1**: kepala, aturan bernomor 1–**83** (plus
   usulan 77, 78, 82, 84), kelas cacat KC-1..**KC-49**. Berkas ini berhenti sesudah
   kelas cacat.
2. **`STATE_LAMPIRAN_EKOR.md`** v8 — **bagian 2**: papan skor R-199..R-308, catatan
   kejujuran, jumlah uji 1168, utang verifikasi, Daftar ADR A001–A015, temuan
   sampingan, penomoran berikutnya. **Angka-angka itu kini tertinggal satu ramalan.**
3. **`STATE_LAMPIRAN_UKUR.md`** v8 — **bagian 3**: penyebut 787, taksonomi, karantina,
   bulan ABSEN, hipotesis, lubang funding, byte parquet semesta, lebar zona irisan
   byte, modul/workflow/uji, API terverifikasi, praregistrasi R-309.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip ekor v41; bukan sumber lagi.

**Ketiga berkas wajib dibaca bersama.** LANGKAH 0 PROMPT wajib menyebut ketiganya.

Yang lahir sejak v48: adjudikasi **R-309 = TEPAT** (tiga butir menang); **ADR-A016**;
**aturan 83 DIRESMIKAN** (syaratnya sendiri terpenuhi — lihat di bawah); **aturan 84
DIUSULKAN** (klausa ATAU wajib melapor sumbangan bebas tiap klausa); CI 1168 →
**1233**; modul **`bulan_pertama` V1** (sidik `0d3530f6…`); pengukuran PERTAMA irisan
bulan pertama (**37 dari 38** baris HIDUP-kecil adalah bulan pertama simbol; nisbah
rata byte pertama : bukan-pertama = **0,527179**); **aturan 57 kembali berjalan,
benar 1 dari 1** sesudah putus di 26/27; cacah tangan tiga direktori LUNAS LAGI pada
ref `010edff2` (**47 / 51 / 42**); tiga dugaan jurnal 129 tentang "bulan tengah"
DICABUT karena SALAH.

## Aturan bernomor

Aturan **1–36** berlaku tanpa perubahan; teks di STATE v19 (blob `e06c486e…`),
ringkas di v37 (blob `f520d5e2`).

**Aturan 10 (irisan/urutan bulan BUKAN sebab). [v49] DIUJI KERAS dan ditaati.**
R-309 menang bulat, dan justru karena itu ADR-A016 kep. 1 mengunci rumusan yang boleh
dikutip: *hampir setiap baris HIDUP di zona byte kecil adalah bulan pertama simbol itu
di dalam penyebut (37 dari 38), sementara hampir setiap bulan pertama BUKAN berkas
kecil (37 dari 787, ±4,7%).* DILARANG mengubahnya menjadi pernyataan sebab ke arah
mana pun.

**Aturan 21 (total papan skor dihitung tangan). [v49] Ditaati:** 216 + 57 = 273;
273 + 21 = 294; 294 + 8 = 302; 302 + 7 = **309**. Rincian: TEPAT **216** · MELESET 57
· SEPARUH 21 · TIDAK TERADJUDIKASI 8 · MENUNGGU 7. N_percobaan = 0. ADJUDIKASI RISET
TETAP TERKUNCI. MENUNGGU: R-7, R-19, R-20, R-28, R-36, R-37, R-199.

**Aturan 29 (pita praregistrasi TIDAK boleh diubah sesudah pengukuran). [v49]
Ditaati tanpa godaan:** ketiga butir R-309 menang di dalam pitanya sendiri — butir 1
**37** dalam 22..38, butir 2 **0,527179** dalam 0.10..0.60. Pita dikunci di jurnal 129
§10 sebelum modulnya ada dan tidak disentuh. Catatan kejujuran: butir 2 menang dengan
margin tipis ke batas atas (0,527 lawan 0,60), jadi kemenangan itu tidak boleh
dibacakan sebagai konfirmasi kuat.

**Aturan 36 (dua modul berbeda atas semesta sama wajib cocok). [v49] Ditaati untuk
ketiga kalinya:** sebaran byte per kelas dari `bulan_pertama` V1 IDENTIK dengan
`irisan_byte` V1 dan `byte_semesta` V1 — HIDUP 18.087 / min 22.440 / maks 2.770.666 /
rata 1.771.962,899 · SEPI 98 / 259.327 / 1.231.408 / 793.143,102 · MATI 1.401 /
97.634 / 451.875 / 413.305,781 · penyebut 19.586 · simbol 787 · total byte
32.706.262.375 · LAIN 0.

**Aturan 43 (toleransi berskala). [v49]** Tidak mendapat bentuk kegagalan baru. R-309
justru menjadi kasus pertama di mana aritmetika implikasi ditulis LEBIH DULU dan
pitanya tetap menang — dasar peresmian aturan 83 di bawah.

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
    `kode_keluar`). **[v49] Ditaati DUA KALI, dan cacat administratif v48 LUNAS:**
    - pemakaian ke-**34**: blob **`2498e2cf6e6f6c7d0b8807bb5ba923ac1d803b6d`**, run
      **30531387464**, commit `5c8d220a` (PROMPT v52), kode 0, **1168** butir;
    - pemakaian ke-**35**: blob **`0489d71101e451efe73d20fd8fe75ba6d41c5c27`**, run
      **30532058688**, commit `09ce9853`, 2026-07-30T09:47:29Z, kode 0, **1233**
      butir.
    Blob laporan CI kini TERCATAT; v48 mengakui tidak mencatatnya. Total pemakaian
    tercatat: **tiga puluh lima**.
45. Keatomikan push pemicu. **[v49] Ditaati:** trio `bulan_pertama` (modul + uji +
    workflow) didorong dalam SATU `push_files` (**`09ce9853ccf6e077bad1038df35508f59f105a3e`**).
46. Kode dilarang menyimpulkan dari penyebut nol. **[v49] Ditaati di `bulan_pertama`
    V1:** butir 1 menyatakan `teradjudikasi: false` bila penyebut 38 menjadi nol, dan
    `nisbah_pertama` mengembalikan **null**, bukan 0, ketika salah satu penyebutnya
    kosong.
47. Satuan cacah tersurat. **[v49] Ditaati:** "37" dan "38" bersatuan **simbol-bulan
    HIDUP**; "787" bersatuan **simbol**; "0,527179" adalah **nisbah tanpa satuan**
    antara dua rata byte.
48. Berkas modul mendekati 800 baris dipecah sebelum fungsi baru ditambahkan.
    `funding.py` (28.121 B) dan `silang_funding.py` (29.873 B) terbesar;
    `bulan_pertama.py` 19.349 B, di bawah batas.
50. Setiap pengukuran yang menyimpulkan dari KETIADAAN wajib memuat kendali
    positif. **[v49] Ditaati di `bulan_pertama` V1:** `kendali_deteksi` memakai
    semesta buatan lima baris dua simbol yang jawabannya dihitung tangan lebih dulu
    (cacah simbol 2, hidup kecil 2, sebagian 2, nisbah 0,75, total byte 1.500) —
    seluruhnya cocok. `kendali_data` membaca tiga parquet terbesar (BTCUSDT 2021-05
    2.770.666, 2021-08 2.730.341, 2021-01 2.722.266) dan memastikan ketiganya HIDUP.
52. Laporan yang tidak dapat dibaca utuh setara dengan laporan yang tidak ada.
    **[v49] Ditaati untuk enam berkas:** `STATE.md` v48 (`2fd136e4`) dan PROMPT v52
    (`16eafb15`) dibaca ulang UTUH sesudah pushnya; `lux_ai/serapan/bulan_pertama.py`
    (**`b9bd00ac46a2825a8f1b540bbe9207e154f66bf4`**),
    `tests/test_bulan_pertama.py` (**`75d87ba2f9254d362ef36d47637e33bdd2b503b5`**),
    `.github/workflows/bulan_pertama.yml` (**`2242e3e4a819f767c015f87a61bae1f5a2f6e82c`**)
    dibaca ulang UTUH sesudah push `09ce9853`; `journal/2026-07-30-130.md`
    (**`d4c48ae4`**) dan `decisions/ADR-A016.md` (**`209802d7`**) dibaca ulang UTUH
    sesudah pushnya. `reports/bulan_pertama.json` (**`0a2aa6ae`**) terbaca UTUH dalam
    satu bacaan berkat `BATAS_BARIS_LAPORAN=40`.
    Utang yang TETAP hidup: `tests/test_bentangan_kohort.py` V2 (63 butir, blob
    `9f850ecd`) belum dibaca ulang byte demi byte — **kini TUJUH versi menunggu.**
55. Rumusan pemicu workflow wajib dikutip dari berkas workflow beserta blobnya.
    **[v49] Ditaati:** `bulan_pertama.yml` (blob `2242e3e4`) dibaca UTUH — `paths`
    **satu entri saja**, `- 'lux_ai/serapan/bulan_pertama.py'`.
57. Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB ditulis
    bernomor. **[v49] KEMBALI BERJALAN: benar 1 dari 1.** Daftar 65 butir bernomor
    ditulis lengkap di kepala `tests/test_bulan_pertama.py` SEBELUM ramalan diucapkan;
    ramalan **1168 + 65 = 1233, kode 0**; terukur **1233, kode 0**. Kemenangannya
    **MUDAH** dan TIDAK masuk papan skor. Penangkal kegagalan giliran ke-27 dipakai
    langsung: daftar ditulis satu nama per nomor tanpa rentang "56–62", karena persis
    rentang itulah yang menyembunyikan butir hilang.
58. Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH DILARANG
    diramalkan dengan pita sempit.
63–76. Berlaku tanpa perubahan dari v43. Teks penuh di v43 (blob `a91a4934`).

**Aturan 66 (cacah direktori dengan TANGAN, bernomor, bukan pengurangan dari angka
lama). [v49] Ditaati dan utang v48 LUNAS:** pada ref
**`010edff23f7143063fd47a5d3a077ca28c66e859`** ketiga direktori dicacah satu per satu
dan bernomor — `lux_ai/serapan/` **47** (`__init__.py` 1 … `bulan_pertama.py` 7 …
`ukur_baris.py` 47), `tests/` **51** (`test_anatomi_tengah.py` 1 …
`test_bulan_pertama.py` 6 … `test_ukur_baris.py` 51), `.github/workflows/` **42**
(`anatomi_tengah.yml` 1 … `bulan_pertama.yml` 5 … `ukur_baris.yml` 42). Ketiganya
cocok dengan turunan v48 (47 / 51 / 42), dan **kecocokan itu TIDAK menyahkan
kewajiban mencacah** (KC-33). Angka apa pun sesudah trio berikutnya kembali menjadi
TURUNAN sampai dicacah lagi.

**Penomoran aturan [v49].** Aturan **83 DIRESMIKAN** giliran ini (dasar di bawah).
Aturan resmi kini: **1–81 dan 83**. Nomor **82** tetap dicadangkan untuk usulan yang
belum berlaku. Nomor **84** dicadangkan untuk usulan baru di bawah. **Aturan
berikutnya yang bebas: 85.** Nomor tidak pernah ditulis dari ingatan; seluruhnya
dibaca dari v48 dan ADR-A016.

**Aturan 77 (TETAP DIUSULKAN, belum berlaku):** dua berkas laporan berblob IDENTIK
bukan dua pengukuran. Baru satu kasus (`bulan_absen.log` ==
`bulan_absen_ringkas.json`).

**Aturan 78 (TETAP DIUSULKAN, belum berlaku — MENGUAT LAGI [v49]):** batas panjang
alat adalah bagian dari DESAIN repo. **Bukti pendukung baru:**
`BATAS_BARIS_LAPORAN=40` membuat `bulan_pertama.json` terbaca UTUH dalam satu bacaan
meski memuat daftar 38 baris bertanda — kali ketiga berturut sesudah
`irisan_byte.json` dan `byte_semesta.json`. Belum diresmikan karena ini kasus
rancangan, bukan pengukuran batasnya sendiri.

**Aturan 79 (BERLAKU sejak v44):** praregistrasi ramalan ditulis lebih dulu di
`journal/**` (yang ada di `paths-ignore`) SEBELUM modul pengukurnya dibuat.
**[v49] Ditaati di R-309:** praregistrasi jurnal 129 §10, dikunci sebelum
`bulan_pertama.py` ada, disalin apa adanya ke docstring modul dan tidak diubah.

**Aturan 80 (BERLAKU sejak v46) — uji arah waktu wajib STRIKT dan kelas `serempak`
dilapor tersendiri.** [v49] R-309 tidak menguji arah waktu, tetapi perbandingan
STRIKT `<` dipakai konsisten di `cacah_di_bawah` dan `cacah_sebagian`.

**Aturan 81 (BERLAKU sejak v46) — numerator yang dikuasai satu bulan kalender wajib
dilapor sebagai kemungkinan artefak satu peristiwa.** **[v49] Ditaati dan terpakai
nyata:** dari numerator 37, tiga baris berbulan `2026-06` (SQQQUSDT, TQQQUSDT,
MVLLUSDT) — di bawah ambang 1/4, jadi tidak ada penguasaan satu bulan. Yang justru
muncul adalah temuan lain: ketiga baris itu **juga** bulan pertama simbolnya, sehingga
klausa tepi menyumbang NOL secara bebas (ADR-A016 kep. 2). Kekuatan bukti yang LEPAS
dari klausa tepi: 37 dari 38, tidak berkurang sedikit pun.

**Aturan 82 (TETAP DIUSULKAN, belum berlaku; nomor dicadangkan) — ambang yang MUSTAHIL
dilewati ATAU yang hasilnya SUDAH TERSIRAT oleh ukuran sebelumnya DILARANG dipakai
sebagai butir berisiko.** Teks penuh seperti v48. Dasar tetap: butir 2 R-307 (ambang
10.000 byte lawan minimum semesta 22.440) dan butir 2 R-308 (ambang 150.000).
Belum diresmikan karena bentuk perluasannya masih satu kasus. Kerabat aturan 43, 44,
83; penangkal KC-48 dan KC-49.

**Aturan 83 (DIRESMIKAN [v49]; diusulkan sejak ADR-A015 kep. 2) — sebelum mengunci
pita praregistrasi, tuliskan di jurnal aritmetika implikasi dari setiap momen terukur
yang relevan.** Bila aritmetika itu sudah menentukan jawabannya dalam satu angka
signifikan, butir tersebut **bukan ramalan berisiko** dan harus diganti atau dipindah
porosnya.

*Dasar peresmian, dikutip dari v48 sendiri:* v48 menuliskan satu-satunya syarat yang
kurang — “bentuk pelaksanaannya (‘satu angka signifikan’) belum diuji pada
praregistrasi yang MENANG”. R-309 memenuhinya. Aritmetika implikasinya ditulis sebelum
pita dikunci dan menghasilkan pita yang tetap dapat kalah ke dua arah: butir 2
menuntut rata byte bulan pertama antara ±174 ribu dan ±1,018 juta, sementara rata
semesta 1.669.858 dan minimum semesta 22.440; terukur **897.374,517**, di dalam pita
tetapi jauh dari kedua tepinya. Butir 1 menuntut ≥19 dari 35 baris non-tepi; terukur
34 dari 35. Tiga kasus kini tercatat: dua kegagalan (R-307, R-308) dan satu
keberhasilan (R-309). Kerabat aturan 29, 43, 44, 82; penangkal KC-49.

**Aturan 84 (DIUSULKAN sejak ADR-A016 kep. 3 — BELUM BERLAKU; nomor dicadangkan) —
butir praregistrasi yang memakai klausa ATAU wajib melaporkan sumbangan BEBAS setiap
klausa secara terpisah, bukan hanya cacah gabungannya.** Dasar pengukuran: butir 1
R-309 berbunyi “bulan PERTAMA simbol ATAU bulan `2026-06`” dan menang dengan 37 dari
38 — tetapi ketiga baris `2026-06` juga bulan pertama, sehingga menghapus klausa kedua
tidak mengubah cacah sama sekali. Satu klausa yang tidak bekerja bersembunyi di balik
klausa yang bekerja, dan tanpa pelaporan terpisah kemenangan itu tidak dapat
ditafsirkan. Belum diresmikan karena baru satu kasus. R-309 lolos dari akibat
terburuknya hanya karena modulnya kebetulan menyimpan medan `pertama` dan `tepi` per
baris — kebetulan bukan penangkal. Kerabat aturan 44, 47, 59, 81; kerabat KC-47.

## Kelas cacat

KC-1 s.d. KC-12 seperti v19; KC-10 dan KC-11 DITUTUP. KC-13 keterwakilan sampel.
**KC-16 DITARIK — nomornya TETAP kosong selamanya.** KC-17 DITUTUP. Teks penuh
KC-14, KC-15, KC-19..KC-29 ada di v37 (blob `f520d5e2`). KC-30..KC-42 ada di v43
(blob `a91a4934`). KC-43, KC-44 teks penuh di v44 (blob `ede3ce3b`). KC-45, KC-46
teks penuh di v45 (blob `e07f2de1`). KC-47 teks penuh di v46 (blob `41b5b585`).
KC-48 teks penuh di v47 (blob `7642b75d`). KC-49 teks penuh di v48 (blob
`2fd136e4`).

Ringkas KC-19..KC-49 satu baris: KC-19 mencacah dari ingatan · KC-20 bias ke bawah
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
KC-44 semua laporan di-commit satu langkah · KC-45 satuan “bulan tanpa funding” dan
“bulan MATI” dicampur · KC-46 lubang bentuk AWAL dibaca sebagai “funding berhenti” ·
KC-47 satu peristiwa menyamar sebagai banyak pengamatan bebas · KC-48 ambang absolut
pada besaran yang sebarannya belum pernah diukur · KC-49 pita dikunci tanpa
menghitung implikasi aritmetis momen yang sudah terukur.

**KC-41 — dua kasus v46 tetap tercatat** (lampiran UKUR v5 salah mengutip `paths`
`lubang_awal.yml`; PROMPT v49 salah melabeli poros R-307 sebagai H-A017). Keduanya
sudah DIKOREKSI dan koreksinya sengaja TIDAK dihapus. **Penangkal yang berlaku:**
rumusan pemicu, label hipotesis, dan nomor aturan WAJIB dikutip dari berkas beserta
blobnya pada giliran yang sama. Bila dua bagian STATE bertentangan, berkas SUMBER
menang, bukan yang lebih baru. **[v49] Kasus ketiga yang berkerabat, dari dugaan
bukan dari kutipan:** jurnal 129 menyebut empat baris “tampak bulan tengah” sebagai
lawan H-A019; terukur, tiga di antaranya (MTLUSDT 2021-03, ENJUSDT 2020-09, SLPUSDT
2023-10) justru bulan PERTAMA simbolnya. Dugaan itu DICABUT (ADR-A016 kep. 4). Yang
benar-benar melawan hanya **TLMUSDT 2023-03** (80.394 byte).

- **KC-48 [RESMI sejak v47] — ambang absolut pada besaran yang sebarannya belum
  pernah diukur.** Teks penuh di v47. Penangkal: usulan aturan 82.

- **KC-49 [RESMI sejak v48] — pita praregistrasi dikunci tanpa lebih dulu menghitung
  implikasi aritmetis dari momen yang SUDAH terukur.** Teks penuh di v48 (blob
  `2fd136e4`), jurnal 129 §6, ADR-A015 kep. 1. **[v49] Penangkalnya kini BERLAKU
  sebagai aturan 83**, dan R-309 adalah kasus pertama yang menunjukkan penangkal itu
  bekerja: aritmetika ditulis lebih dulu, pita tetap berisiko, hasilnya menang.

**Calon KC-50 (BELUM RESMI, dari ADR-A015 kep. 7; DIPERKUAT ADR-A016 kep. 5) — medan
invarian turunan dicacah sebagai pemeriksaan bebas.** Sumber terukur: di
`irisan_byte.ringkaskan`, `total_byte` dihitung sebagai jumlah byte keempat kelas,
sehingga `selisih_total_byte` tersirat secara aritmetis — sembilan medan selisih =
**delapan pemeriksaan bebas + satu turunan**; menyebut “sembilan pemeriksaan bebas”
DILARANG. **[v49] Belum naik menjadi resmi karena belum ada kasus KEDUA — dan memang
tidak ada, sebab `bulan_pertama` justru memperbaikinya:** `total_byte` dihitung
langsung oleh `total_byte_langsung` tanpa melewati pengelompokan kelas, dan kedelapan
medan invariannya tidak ada yang dihitung dari medan lain. Yang tetap dinyatakan apa
adanya di modul itu: `byte_hidup` dan `total_byte` berbagi bahan baku yang sama, jadi
bebas sebagai JALUR HITUNG, bukan sebagai bukti yang saling merdeka. Praktik jalur
langsung kini WAJIB bagi modul baru (ADR-A016 kep. 5). Nomor **KC-50** tetap
dicadangkan.

## Ke bagian 2 dan 3

Berkas ini berhenti di sini dengan sengaja. Lanjutannya:

- **Papan skor.** Keadaan MUTAKHIR ada di berkas ini (aturan 21 di atas): total
  **309** — TEPAT 216 · MELESET 57 · SEPARUH 21 · TIDAK TERADJUDIKASI 8 · MENUNGGU 7.
  Rincian per ramalan R-199..R-308 masih di `STATE_LAMPIRAN_EKOR.md` v8 (blob
  `c34c88e2`), yang totalnya masih 308 dan jumlah ujinya masih 1168. **EKOR v9 wajib
  menambahkan baris R-309 = TEPAT, jumlah uji 1233, dan ADR A016.**
- **Penyebut 787, taksonomi, karantina, bulan ABSEN, hipotesis H-A001..H-A019, byte
  parquet semesta, lebar zona irisan byte, lubang funding, modul/workflow/uji, API
  terverifikasi** → `STATE_LAMPIRAN_UKUR.md` v8 (blob `ff190695`). **UKUR v9 wajib
  menandai H-A019 sebagai DIUJI dengan rumusan terbatas ADR-A016 kep. 1, menambahkan
  API `bulan_pertama` V1, dan mengganti cacah modul/uji/workflow menjadi 47 / 51 /
  42.**

**Hasil R-309 secara ringkas (sumber: jurnal 130, ADR-A016,
`reports/bulan_pertama.json`):** butir 1 BERISIKO **37** dari 38, pita 22..38 —
MENANG; butir 2 BERISIKO nisbah **0,527179** (rata pertama 897.374,517 atas 787 baris;
rata bukan-pertama 1.702.219,726 atas 18.799 baris), pita 0.10..0.60 — MENANG;
butir 3 MUDAH — delapan selisih invarian nol, dua kendali sah, kode 0, CI 1233 —
MENANG. Adjudikasi **TEPAT**.

Ramalan berikutnya **R-310** (poros BELUM ditetapkan; ADR-A016 kep. 7 memindahkan
prioritas ke pertanyaan **apa ISI berkas bulan MATI**, yang belum diukur dan DILARANG
ditebak; aturan 83 kini WAJIB dipenuhi sebelum pitanya dikunci). Jurnal berikutnya
**131**, PROMPT berikutnya **v53**, ADR berikutnya **A017**, KC berikutnya **KC-50**,
aturan berikutnya **85**, hipotesis berikutnya **H-A020**. Papan skor sesudah R-310 =
**310**.
