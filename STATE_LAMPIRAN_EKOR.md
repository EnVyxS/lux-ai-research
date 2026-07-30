# STATE lampiran EKOR — bagian 2 dari STATE (v13, milik STATE v54)

**Mengapa berkas ini ada.** Dua push `STATE.md` berturut terpotong (v41, v42);
pemecahan ke tiga berkas berlaku sejak v43 (KC-42). Pembagian yang berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, 83, 84, **85**; KC-1..**KC-52**.
2. **`STATE_LAMPIRAN_EKOR.md`** (berkas ini, v13) — bagian 2: papan skor, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** — bagian 3: pengukuran, modul, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) dan **`PROMPT_KELANJUTAN.md`**
   (blob `35beed44`) — **arsip; BUKAN sumber** (ADR-A018 kep. 9).

Dasar v13: EKOR v12 (blob **`568dc877f69d6508b1db50a35877d34da76fc21e`**), **dibaca
UTUH pada giliran yang sama sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43).

## KESERASIAN VERSI — dibaca apa adanya, termasuk yang belum serasi

Saat berkas ini didorong:

- `STATE.md` **v54** — blob **`af10274dc4b75292d56ff15c369f1e08ccfc5dd3`**, commit
  **`8368ca1f296f2e7ad4547ef9f9486e5370d4445a`**, dibaca ulang UTUH sesudah push.
  **SERASI** dengan berkas ini.
- `STATE_LAMPIRAN_EKOR.md` **v13** — berkas ini.
- `STATE_LAMPIRAN_UKUR.md` masih **v12** — blob
  **`b8dab926ac3bbf4441339f5856775ef521efdec1`**, commit `1247a5a3`.
  **USANG SEBAGIAN — dan kali ini bukan sekadar nomor yang tertinggal.** UKUR v12
  ditulis sebelum KC-52 ditutup. Ia **tidak memuat**: penutupan KC-52, **H-A022
  TERBUKTI**, cacah karantina per pecahan, API `pulihkan` V2, API `kehidupan_arsip`,
  API `selisih_lilin`, dan turunan `cacah_baris_cacat` = 0. **Sampai UKUR v13 naik,
  sumber sah untuk seluruh butir itu adalah `STATE.md` v54 dan jurnal 139–140**, bukan
  UKUR v12.

**Satu berkas per push tetap MENGIKAT** (KC-42, KC-43).

**Tentang push berkas ini:** ia di akar repo sehingga menyalakan `ci.yml`. Tidak satu
pun `tests/**` berubah, jadi cacah uji tetap **1377** — ramalan deterministik, **MUDAH**,
TIDAK diskor, TIDAK menambah beruntun aturan 57. **Laporannya WAJIB dibaca sebelum push
akar berikutnya**, atau ia hangus seperti run `30547842823`.

## KESALAHAN DOKUMEN SENDIRI — kini SEPULUH, dan yang kesepuluh bukan salah ketik

Daftar ini disalin dari STATE v54 dan berlaku identik di ketiga bagian. Sebab tetap
sama setiap kali: `push_files` menulis ulang SELURUH berkas, sehingga memperbaiki satu
karakter berarti menyusun ulang berkas besar dari konteks terpakai — persis yang
dicatat KC-42 sebagai cara paling pasti merusaknya. Perbaikan selalu menumpang pada
penulisan ulang yang memang sudah dijadwalkan.

| # | berkas | tertulis | seharusnya | status |
| --- | --- | --- | --- | --- |
| 1 | jurnal 132 §3 | "beruntun 2/1" | 2/2 | LUNAS di STATE v50 |
| 2 | EKOR v10 | `terisi ≉49,7%` | `≈49,7%` | LUNAS di EKOR v11 |
| 3 | jurnal 135 §13.3 | "hendan dirumuskan" | "hendak" | LUNAS di STATE v51 |
| 4 | EKOR v11 kepala | "deretministik" | "deterministik" | LUNAS di EKOR v12 |
| 5 | UKUR v11 kepala | "KESERAIAN VERSI" | "KESERASIAN VERSI" | LUNAS di UKUR v12 |
| 6 | UKUR v11 daftar uji | penanda `**` tak berpasangan | berpasangan | LUNAS di UKUR v12 |
| 7 | STATE v52 | "Empat salah ketik" padahal tabelnya enam | "Enam" | LUNAS di STATE v53 |
| 8 | STATE v53 aturan 45 | "empat push terakhir adalah dokumen tunggal" lalu mendaftar **ENAM** | "enam push terakhir" | **LUNAS di STATE v54** |
| 9 | STATE v53 aturan 52 | pembacaan ulang "tidak menangkap satu pun" | **kadang** menangkap — **satu dari delapan** | **LUNAS di STATE v54** |
| 10 | jurnal 138 §5 butir 2 | "maka **839.842.134 yang keliru**" | kesimpulan **tidak sah dari premisnya**; kedua angka benar | **LUNAS di jurnal 140** |

**Butir 10 memutus pola dan wajib dibaca terpisah.** Butir 1–9 adalah salah ketik atau
salah cacah — kelas kesalahan yang tidak mengancam satu angka pun. Butir 10 adalah
**kesimpulan tidak sah dari premis yang benar**, dan ia sempat menetapkan sebuah angka
terukur sebagai keliru. Ia bertahan **dua giliran penuh**, lolos dari pembacaan ulang
aturan 52, dan runtuh hanya karena data baru dibuka. **Pemeriksaan formal kami tidak
punya satu pun penangkal untuk kelas ini** — itulah yang KC-52 rumuskan.

**Koreksi jujur atas rumusan EKOR v12 sendiri:** v12 menulis bahwa pembacaan ulang
aturan 52 gagal menangkap salah ketik. Rumusan yang tepat, dihitung atas sepuluh butir
di tabel: pembacaan ulang menangkap **satu dari delapan** kasus yang terlacak. Ia kuat
terhadap pemotongan dan penimpaan; lemah terhadap ejaan; **tidak berdaya sama sekali
terhadap penalaran yang cacat**.

## KC-43..KC-52 (teks lengkap KC-43..KC-47 di STATE v47, KC-49 di v48, KC-50 di v50, KC-51 di v52, **KC-52 di v54**)

- **KC-43** — tanda tangan fungsi dari INGATAN. Penangkal: baca modul yang diimpor
  UTUH pada giliran yang sama.
- **KC-44** — semua laporan di-commit satu langkah.
- **KC-45 [RESMI v45]** — satuan "bulan tanpa funding" vs "bulan MATI" dicampur.
- **KC-46 [RESMI v45]** — lubang bentuk AWAL dibaca sebagai "funding berhenti".
- **KC-47 [RESMI v46]** — satu peristiwa menyamar sebagai banyak pengamatan bebas.
  Kasus kuat: TUJUH dari sembilan baris MATI tak penuh R-310 berbulan `2024-05` dalam
  jendela **9 lilin**. **Diperiksa untuk R-311 dan TIDAK terpicu** (ADR-A018 kep. 4).
  **[v13] Diperiksa untuk R-313 dan TIDAK terpicu:** dua belas parquet karantina
  tersebar di **enam pecahan berbeda** dengan cacah 3/3/1/1/3/1, bukan satu peristiwa.
- **KC-48 [RESMI v47]** — ambang absolut pada besaran yang sebarannya belum diukur.
- **KC-49 [RESMI v8 lampiran ini]** — pita dikunci tanpa aritmetika implikasi.
  Penangkalnya berlaku sebagai aturan 83.
- **KC-50 [RESMI di STATE v50]** — agregat lewat jalan memutar, sehingga selisih
  terhadap sumber lain mustahil terlihat. **Cacat kelas ini tidak menghasilkan galat;
  ia menghasilkan kesunyian.** **[v13] Kasus 839.842.134 lawan 839.325.999 kini
  SELESAI — tetapi tidak dengan cara yang KC-50 ramalkan.** Jalur langsung memang
  memperlihatkan selisihnya; yang tidak dilihat siapa pun adalah bahwa selisih itu sah.
  Kasus `total_byte` `irisan_byte` dan tautologi 712.925 tetap berlaku penuh.
- **KC-51 [RESMI v52]** — **bias taksiran pemusatan**: besaran yang belum pernah diukur
  sebarannya secara sistematis ditaksir **lebih menyebar** daripada kenyataannya.
  **Empat kejadian berturut tanpa satu pun pembalikan arah:** R-308 butir 2 (pita
  10..300 → **2**); R-310 butir 2 (0,073; pita 0,02..0,25 → **0,0445**); R-311 butir 1
  (3.000; pita 200..12.000 → **114**, faktor **26,3**); R-311 butir 2 (0,15; pita
  0,02..0,45 → **0,4087**, **+172%**). **[v13] TIDAK mendapat kejadian kelima.** R-312
  tidak teradjudikasi; R-313 bukan taksiran atas sebaran yang belum diukur, melainkan
  penjumlahan angka yang sudah tercatat. **DILARANG:** membaca kemenangan tipis mana
  pun — **termasuk R-313** — sebagai bukti kalibrasi membaik. **Penangkalnya aturan 85**,
  berlaku mulai R-312, dan **masih belum punya satu pun adjudikasi**.
- **KC-52 [RESMI di STATE v54, dan DITUTUP pada giliran yang sama]** — **dua penyebut
  berbeda diperlakukan sebagai satu.** Rumusan resmi: ketika dua angka besar atas
  "semesta yang sama" tidak cocok, kemungkinan pertama yang wajib diperiksa bukanlah
  bahwa salah satunya keliru, melainkan bahwa keduanya **mencacah himpunan yang
  berbeda**. Selisih tak terjelaskan adalah dugaan tentang **batas himpunan**, bukan
  tentang mutu pengukuran. Kasusnya bertahan sejak jurnal 131 dan berturut-turut
  disalahartikan sebagai salah aritmetika, lalu cacat pembaca, lalu satu angka keliru
  — **ketiganya salah**. Kerabat: KC-25, KC-36, KC-39, aturan 44.
- **KC berikutnya yang bebas: KC-53.**

## Papan skor prediksi — lengkap R-300..R-313 (R-199..R-299 di v4, blob `67dda29e`)

| # | Prediksi | Status |
|---|---|---|
| R-300 | (1) cacah_bulan 64; (2) tetangga BTCST HIDUP; (3) cacah_hidup 8..30 dan MATI>HIDUP | **SEPARUH** |
| R-301 | (1) tebing==0; (2) mati_tersisip ≥1; (3) bangkit==0 | **TIDAK TERADJUDIKASI** |
| R-302 | (1) simbol tersisip 1..10; (2) simbol-bulan 1..50; (3) penyebut 19.586/787 | **SEPARUH** (butir 2 MELESET 88>50) |
| R-303 | (1) simbol tersisip 1..60; (2) simbol-bulan 1..300; (3) penyebut/kendali/kode 0 | **TEPAT (3/3)** |
| R-304 | (1) mati_dulu 5..8; (2) hidup_berlubang 3..8; (3) penyebut/kendali/kode 0 | **MELESET** (1 dan 2 kalah) |
| R-305 | (1) bagian mati-tak-setelah-lubang dari ≥100 dalam 0.55..0.95; (2) cacah lubang-awal 20..120; (3) invarian + kendali + kode 0 + CI | **MELESET** — butir 1 KALAH (penyebut 118, bagian **1.0**, tautologis); butir 2 KALAH (**5**); butir 3 TEPAT (MUDAH) |
| R-306 | (1) bagian arah STRIKT dari penyebut ≥100 dalam 0.25..0.60; (2) cacah tebing 2025-07 dalam 20..90; (3) sembilan invarian + dua kendali + kode 0 + CI | **TEPAT (3/3)** — **0.339** (penyebut **118**); **39**; MUDAH |
| R-307 | (1) bagian byte MATI dalam 0.02..0.15; (2) cacah simbol-bulan ber-`byte_parquet` < 10.000 dalam 20..400; (3) sembilan invarian nol + dua kendali + kode 0 + CI | **MELESET** — **0.017704** tipis di bawah pita; **0** (ambang MUSTAHIL, KC-48); butir 3 MUDAH |
| R-308 | (1) cacah HIDUP ber-byte < 97.634 dari 18.087 dalam **20..600**; (2) cacah MATI ber-byte < 150.000 dari 1.401 dalam **10..300**; (3) invarian + kendali + kode 0 + CI | **SEPARUH** — **38** MENANG; **2** KALAH (KC-49, kasus pertama KC-51); butir 3 MUDAH |
| R-309 | (1) cacah baris HIDUP-kecil bulan PERTAMA atau tepi `2026-06`, dari 38, dalam **22..38**; (2) nisbah rata byte dalam **0.10..0.60**; (3) delapan invarian nol + dua kendali + kode 0 + CI | **TEPAT (3/3)** — **37** (0,973684); **0,527179**; MUDAH |
| R-310 | (1) cacah baris MATI berdefisit lilin, dari 1.401, dalam **1..120**; (2) bagian defisit bukan-pertama dalam **0.02..0.25**; (3) delapan invarian nol + tiga kendali + lima penggugur + kode 0 + CI | **TEPAT** — **9** (tipis ke tepi BAWAH); **0,0445** (tipis ke tepi BAWAH); MUDAH |
| R-311 | (1) cacah baris bukan-pertama bukan-MATI berdefisit, dari **17.398**, dalam **200 .. 12.000**; (2) bagian sisa 712.925 yang ditanggung SEPULUH teratas, dalam **0,02 .. 0,45**; (3) sepuluh invarian nol + tiga kendali + penggugur + kode 0 + CI | **SEPARUH** — butir 1 **KALAH** (**114**, lantai aritmetis 16); butir 2 **MENANG** (**0,4087**, tipis ke tepi ATAS, sisa 0,0413); butir 3 MUDAH |
| **R-312** | (1) cacah baris berselisih antara `cacah_lilin` dan `cacah_lilin_terbaca`, dari 19.586, dalam **12 .. 120**; (2) bagian selisih yang ditanggung baris teratas dalam **0,50 .. 0,865**; (3) penggugur + kendali + kode 0 + CI | **TIDAK TERADJUDIKASI** — `cacah_berselisih` **0**, penyebut butir 2 NOL (aturan 41). Porosnya runtuh sebelum diadjudikasi: kedua medan **tidak bebas**. |
| **R-313** | (1) Σ `baris_karantina` atas delapan `reports/pulihkan_pecahan_<i>.json` = **516.135** (titik tunggal, selisih nol); (2) Σ parquet karantina = **12** (titik tunggal) | **TEPAT (2/2)** — **516.135** dan **12**, keduanya selisih **0** |

**Total R-1..R-313** (dihitung tangan, aturan 21). Dasar v12 (R-1..R-311): TEPAT 217 ·
MELESET 57 · SEPARUH 22 · TIDAK TERADJUDIKASI 8 · MENUNGGU 7 = 311. Sesudah v12:
**R-312 TIDAK TERADJUDIKASI** (8→9), **R-313 TEPAT** (217→218).

- TEPAT 217 + 1 = **218**
- MELESET **57**
- SEPARUH **22**
- TIDAK TERADJUDIKASI 8 + 1 = **9**
- MENUNGGU **7** (R-7, R-19, R-20, R-28, R-36, R-37, R-199)

218 + 57 = 275; 275 + 22 = 297; 297 + 9 = 306; 306 + 7 = **313** ✅ Nomor terpakai
R-1..R-313, seluruhnya teradjudikasi atau menunggu. N_percobaan = 0.
**ADJUDIKASI RISET TETAP TERKUNCI.**

**Nisbah papan skor, dihitung tangan dan disebut apa adanya:** dari 297 ramalan yang
beradjudikasi penuh (218 + 57 + 22), TEPAT **73,4%**, MELESET **19,2%**, SEPARUH
**7,4%**. Angka itu **DILARANG dibaca sebagai mutu ramalan**: sebagian besar butir
ketiga tiap ramalan berlabel MUDAH dan tidak berisiko. **R-312 DILARANG masuk pembilang
maupun penyebut nisbah ini.**

**Utang papan skor:** rincian R-236..R-247 masih di jurnal 92–94; R-229 TEPAT dan
R-230 MELESET (dari docstring) menunggu pemeriksaan R-224..R-235.

### Lima larangan permanen yang menempel pada R-312

1. **DILARANG** mengatakan pita butir 1 (12..120) "tidak terbantah".
2. **DILARANG** mengatakan kalibrasi membaik atau memburuk karena R-312.
3. **DILARANG** menghitungnya di pembilang maupun penyebut nisbah kemenangan.
4. **DILARANG** menghidupkannya kembali dengan alasan penjelasannya kini ditemukan.
5. Angka **12** di R-313 adalah cacah **parquet karantina** — arti berbeda dari 12 di
   R-312 butir 1. **Kesamaan itu DILARANG dibaca sebagai konfirmasi apa pun.**

## Catatan kejujuran [v13]

1. **Tiga giliran berturut menghasilkan nol baris kode dan tetap menjawab pertanyaan
   terbesar yang terbuka.** Jurnal 138 menjawab satu cabang dengan membaca kode; 139
   menjawab strukturnya dengan membaca kode; 140 menutup KC-52 dengan membaca laporan
   yang sudah ada. Bandingkan dengan giliran sebelumnya, yang menulis satu modul, 36
   butir uji, dan satu workflow untuk mencari angka yang **sudah tersimpan di repo dua
   hari sebelumnya**. Itulah dasar usulan **aturan 86**.
2. **R-313 menang telak dan itu justru harus dikecilkan, bukan dibesarkan.** Kedua
   butirnya titik tunggal dengan selisih nol — tetapi ia menjumlahkan medan yang sudah
   tertulis di delapan berkas laporan. Risikonya nyata (satu berkas hilang atau satu
   medan bernama lain akan menggugurkannya) namun **jauh lebih kecil** daripada
   meramalkan sebaran yang belum pernah diukur. **R-313 bukan bukti bahwa KC-51
   melemah.**
3. **Aturan 79 dilemahkan oleh R-313, dan itu diakui, bukan dibenarkan.** Praregistrasi
   R-313 ditulis **di chat**, bukan di `journal/**`, karena pengukurnya adalah
   pembacaan laporan yang sudah ada dan menuliskannya ke jurnal lebih dulu berarti satu
   push tambahan sebelum data dibuka. Bunyinya dikutip kata demi kata di jurnal 140 §2.
   **Satu-satunya saksi bahwa ramalan itu ditulis lebih dulu adalah riwayat percakapan,
   bukan git.** Bila kelak seseorang menolak mengakui R-313, penolakan itu sah.
4. **Aturan 57 beruntun 4 dari 4.** Kesempatan keempat: 36 butir `test_01`..`test_36`
   ditulis bernomor, ramalan **1341 + 36 = 1377** dinyatakan sebelum laporan dibaca,
   terukur **1377**. Ini satu-satunya lajur kalibrasi yang belum pernah kalah sejak
   putus di 26/27, dan satu-satunya alasan ia tidak dibanggakan adalah ia **mencacah,
   bukan menaksir**.
5. **Aturan 36 mendapat kasus terkuatnya sampai kini.** `selisih_lilin` menjumlahkan
   medan `cacah_lilin` atas 19.586 baris laporan kehidupan; `pulihkan` mencacah kaki
   parquet lewat jalur unduh-bongkar-verifikasi yang sama sekali berbeda. Keduanya
   **839.325.999**, sampai satuan terakhir. Dua jalur, dua modul, dua run, satu angka.
6. **Turunan cuma-cuma yang tidak diramalkan siapa pun:** identitas `cacah_lilin` =
   `cacah_lilin_terbaca` + `cacah_baris_cacat`, digabung dengan `cacah_berselisih` = 0
   pada 19.586 dari 19.586, memaksa **`cacah_baris_cacat` = 0 di seluruh semesta**.
   Tidak satu pun dari 839.325.999 baris gagal diurai. Itu didapat tanpa run tambahan.
7. **Kekalahan poros terbesar sesi ini, disebut telanjang (jurnal 137).** R-312 berdiri
   di atas anggapan **tak terperiksa** bahwa dua medan bernama berbeda adalah dua
   pengukuran bebas. Tidak ada satu pun baris kode yang dibaca sebelum pita dikunci.
   Modul, 36 butir uji, dan satu workflow ditulis di atas anggapan itu.
8. **`PROMPT_KELANJUTAN.md` tetap belum diberi kepala "ARSIP — BUKAN SUMBER"** dan
   `PROMPT.md` **v55 belum didorong**. Sampai itu dikerjakan, satu-satunya penjaga
   adalah larangan tertulis di STATE v52–v54 dan di berkas ini.
9. **Pemeriksaan silang yang menutup tanpa sisa** (terbitan, TIDAK diskor):
   18.799 − 1.401 = **17.398**; 18.087 − 17.318 = **769**; 98 − 80 = **18**;
   769 + 18 = **787** = `cacah_simbol`; **19.586 + 12 = 19.598**;
   **839.325.999 + 516.135 = 839.842.134**.

**Kesalahan proses giliran-giliran ini:** tidak ada satu pun kegagalan konektor —
seluruh `push_files`, `get_file_contents`, dan `list_commits` berhasil sekali jalan,
seluruh SHA dibandingkan dan cocok, tidak ada pemotongan terdeteksi. Kerugian yang
tetap tercatat berasal dari urutan kerja, bukan galat alat: laporan CI run
`30547842823` hangus, dan blob laporan ke-38 tidak dapat dipulihkan.

## Jumlah uji

**1377 TERUKUR, dua bacaan berjejak.**

1. blob **`cdfdee2559201306a49bc9b01f1185d7aa36eebe`**: run **30559145901**, commit
   **`c1dc00092c404c2c8633a3bfe92d4fa4d2fc5c29`** (trio `selisih_lilin`),
   2026-07-30T15:57:01Z, kode 0, **1377** (`1377 tests collected in 0.58s`).
2. **[v13]** blob **`effb3a46bc20cda5c6c5910ee926aa16c195bb68`**: run **30575123865**,
   commit **`8368ca1f296f2e7ad4547ef9f9486e5370d4445a`** (push STATE v54),
   2026-07-30T19:30:52Z, kode 0, **1377** (`1377 tests collected in 0.54s`).

Turunan: 1341 + **36** butir `tests/test_selisih_lilin.py` = **1377** ✅ (aturan 21).

Riwayat panjang: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 →
984 → 1044 → 1100 → 1168 → 1233 → 1297 → 1341 (enam run) → **1377**.

Cacah per berkas uji (**milik repo riset ini — bukan repo warisan**):
`test_irisan_byte.py` **68** · `test_bulan_pertama.py` **65** ·
`test_keterisian_lilin.py` **64** · `test_bentangan_kohort.py` V2 **63** (dicacah
TANGAN, `test_01`..`test_63`) · `test_lubang_tebing.py` **60** ·
`test_sebab_bangkit.py` **57** · `test_byte_semesta.py` **56** ·
`test_lubang_awal.py` **48** · `test_tersisip_semesta.py` **47** ·
`test_anatomi_tengah.py` **47** · `test_sisa_defisit.py` **44** (dicacah TANGAN) ·
**`test_selisih_lilin.py` 36** (dicacah TANGAN, `test_01`..`test_36`) ·
`test_terhenti.py` V4 **33** · `test_bulan_absen.py` **32** ·
`test_karantina_semesta.py` **28** · `test_silang_settled.py` **24** ·
`test_ukur_baris.py` **3**.

**Aturan 57: beruntun 4 dari 4** sesudah putus di 26/27. Hanya push yang menyentuh
`tests/**` yang dihitung.

### ORDINAL ATURAN 38 — buku besar, kini sampai ke-46

**Definisi yang berlaku (ADR-A018 kep. 8):** pemakaian dihitung **hanya** untuk
pembacaan `reports/ci_terakhir.json` yang meninggalkan **jejak tertulis** berupa nomor
run + commit + blob di STATE, lampiran, atau jurnal. Pembacaan tanpa jejak tidak masuk
buku besar dan karena itu tidak boleh dihitung.

| ke- | CI | run | commit | blob | jejak |
|---|---|---|---|---|---|
| 39 | 1341 | 30542217837 | `b1c7941d` | `2d32f814` | jurnal 135, STATE v51 |
| 40 | 1341 | 30545364506 | `8c30de51` | `bce1177e` | EKOR v11, STATE v52 |
| 41 | 1341 | 30548418622 | `28afc9ae` | `2c3290cb` | EKOR v12, UKUR v12 |
| 42 | 1341 | 30549286062 | `e68deab7` | `ed743bdf` | UKUR v12 |
| 43 | 1341 | 30550547017 | `1247a5a3` | `fdb7c668` | STATE v53 |
| 44 | 1341 | 30551789395 | `33a4ab37` | `5b16417b` | jurnal 136 |
| 45 | **1377** | 30559145901 | `c1dc0009` | `cdfdee25` | jurnal 137, STATE v54 |
| **46** | **1377** | **30575123865** | **`8368ca1f`** | **`effb3a46`** | **berkas ini** |

**Pemakaian berjalan = ke-empat puluh enam.** Pemakaian ke-46 dibaca
**2026-07-30T19:30:52Z**, kode keluar **0**, atas push STATE v54 — **dibaca sebelum
tertimpa**, sehingga ramalan "CI tetap 1377" untuk push itu **TERUKUR dan TEPAT**,
tetap **MUDAH**, tetap tidak diskor.

**Dua cacat tetap disebut apa adanya:** baris ke-**38** (run `30541051907`, CI 1297,
commit `5d7d8b96`) **tanpa blob**, tidak dapat dipulihkan — ordinal ini karena itu sah
**relatif terhadap definisi di atas**, bukan sebagai pencacahan mutlak; dan run
**30547842823** (bot `de2fc03d`) **tidak pernah dibaca**, sudah tertimpa, **DILARANG
dihitung**, ramalannya **DILARANG diklaim menang**. Bila jejak pembacaan lain ditemukan
di jurnal 133–134, nomor ini **WAJIB dikoreksi, bukan dipertahankan**.

## Utang verifikasi

1-5, 11 menunggu tahap juri. 6-23, 25-29, 31 LUNAS. **Nomor utang BUKAN nomor ramalan
— KC-32.**

24. **AKTIF. LUNAS BARU [v13]:**
    - **`lux_ai/serapan/pulihkan.py` V2 dibaca UTUH** (`a9e6eab7cc47555dfed919ac63044ff2eadc4893`, 14.839 B).
    - **`lux_ai/serapan/kehidupan_arsip.py` V1 dibaca UTUH** (`318a5cb187406d16cfd3385d653bed905f632934`, 19.281 B) — dasar vonis `ukur_kolom`.
    - **`lux_ai/serapan/silang_funding.py` V2 dibaca UTUH** (`42c3aa9dc2c16220b79cf9c9e46979dd000fd393`, 29.873 B) — membuktikan `baca_medan_baris` TIDAK cacat.
    - **Kedelapan `reports/pulihkan_pecahan_0..7.json` dibaca UTUH**, blob tercatat di
      jurnal 140 §3.
    - `reports/ci_terakhir.json` (`cdfdee25`, `effb3a46`) dibaca utuh, blob DICATAT.
    - `STATE.md` v53 (`a0ea143e`) dan v54 (`af10274d`), EKOR v12 (`568dc877`), jurnal
      136–140 dibaca UTUH sesudah masing-masing push.
    **TETAP BELUM — dan satu di antaranya BARU:**
    **(a) ketiga berkas trio `c1dc0009`** (`selisih_lilin.py`, `test_selisih_lilin.py`,
    `selisih_lilin.yml`) **belum dibaca ulang utuh sesudah push** — aturan 52 belum
    lunas atasnya, dan CI 1377 **bukan pengganti**; `decisions/ADR-A002`, **A004**,
    **A006**, **A007**, **A008**; `.github/workflows/karantina_semesta.yml`
    (`de40fa4e`); `tests/test_pulihkan.py` (`11c43533`);
    `tests/test_rilis_karantina.py` (`739c8da9`); `tests/test_karantina_a006.py`
    (`a5a3d82f`).
30. **AKTIF — UTANG HIDUP.** Trio `selisih_lilin` sudah didorong, sehingga angka
    **50 / 54 / 45** kini **TURUNAN** dan **DILARANG dikutip sebagai terukur** sampai
    dicacah satu per satu bernomor (aturan 66, KC-33). Yang sah sekarang tetap
    **49 / 53 / 44 / 18** pada ref `3196fd98` dan `8a614567`.
32. **AKTIF — tiga butir "memerlukan verifikasi" `PETA_MODUL.md`** (repo **WARISAN**),
    utang terbuka, bukan fakta: (a) `enable_hs` tidak ditemukan di `config.py` padahal
    dipakai `strategy.py`; (b) klaim "30 pair dipilih alfabetis"; (c) klaim "kendala
    mengikat = kapasitas margin".
33. **LUNAS [v13]** — kesepuluh butir daftar kesalahan kini lunas di sumbernya
    masing-masing.
34. **AKTIF — `PROMPT_KELANJUTAN.md` belum diberi kepala "ARSIP — BUKAN SUMBER"**, dan
    **`PROMPT.md` v55 belum didorong**.
35. **BARU [v13] — UKUR v13 belum naik.** Sampai ia naik, UKUR v12 **usang sebagian**;
    lihat bagian keserasian di kepala berkas ini.
36. **BARU [v13] — identitas dua belas simbol-bulan karantina belum pernah didaftar.**
    Cacah dan barisnya terukur (12 parquet, 516.135 baris), tetapi **nama simbol dan
    bulannya tidak diketahui**. Selama itu, kalimat apa pun tentang *jenis* instrumen
    yang dikarantina **DILARANG**.

## Daftar ADR

- **ADR-A001** aturan dasar. DITERIMA.
- **ADR-A002** serapan. Kondisi v3 berlaku; §10 tetap tidak boleh diubah.
- **ADR-A003** taksonomi rezim. BELUM ADA.
- **ADR-A004** kebijakan KC-6. DITERIMA.
- **ADR-A005** jenis instrumen. DITERIMA.
- **ADR-A006** karantina + persistensi. DITERIMA, TERVERIFIKASI.
- **ADR-A007** serapan hibrida. DIUSULKAN, belum diterima.
- **ADR-A008** akibat KC-18. Keputusan 1–6 DITERIMA. **Keputusan 7 DITANGGUHKAN.**
- **ADR-A009** (`17a594b6`). **DICABUT PENUH oleh ADR-A012.**
- **ADR-A010** (`c4bccf21`) — klaim "kebangkitan tunggal" DICABUT. DITERIMA.
- **ADR-A011** (`645fd5df`) — arah sebab A009 dicabut untuk kelas bangkit. DITERIMA.
- **ADR-A012** (`f9f564d1`) — arah sebab dicabut untuk SELURUH semesta. DITERIMA.
- **ADR-A013** (`8ba4f989`) — klaim arah waktu wajib dipilah tebing lawan bukan-tebing;
  (2) dan (4) kini aturan **80** dan **81**. DITERIMA.
- **ADR-A014** (blob `6d77c2cd`) — byte parquet; (5) melahirkan KC-48. DITERIMA.
- **ADR-A015** (blob `387d5510`) — delapan keputusan; (5) besar berkas bukan detektor
  status ke arah mana pun — **TIDAK dibalik oleh R-310, R-311, R-313, maupun A018**.
  DITERIMA.
- **ADR-A016** (blob `209802d7`) — H-A019 diterima TERBATAS; delapan keputusan; kep. 4
  **DIKOREKSI oleh A018 kep. 6**. DITERIMA.
- **ADR-A017** (blob `1be570f2`) — sebelas keputusan; kep. 4 mencatat selisih
  **516.135** sebagai koreksi resmi. **[v13] Kep. 4 kini TERJAWAB PENUH oleh R-313:**
  selisih itu bukan cacat, melainkan batas himpunan. Rumusan A017 kep. 4 tetap benar
  sebagai peringatan; tafsirnya yang menyiratkan salah satu angka bermasalah **gugur**.
  DITERIMA.
- **ADR-A018** (blob `3fba599e`) — dua belas keputusan; (1) KC-51 diresmikan;
  (2) aturan 85 berlaku mulai R-312; (3) rumusan resmi R-311; (4) aturan 81 tidak
  terpicu; (5) H-A021 diusulkan; (6) A016 kep. 4 dikoreksi; (7) koreksi aturan 38;
  (8) definisi ordinal; (9) `PROMPT_KELANJUTAN.md` arsip; (10) dua cacah `tests/`;
  (11) cacah tangan 49/53/44/18; (12) poros R-312 ditetapkan. DITERIMA.
  **[v13] Kep. 12 kini SELESAI:** poros (b) dijawab tuntas lewat R-313; poros (a)
  — lubang tengah `2022-05`/`2024-05` — menjadi poros tunggal yang tersisa.
- **ADR-A019 [BELUM ADA]** — calon isinya sudah pasti dan lebih padat daripada
  sebelumnya: (a) **peresmian KC-52** beserta rumusan dan kerabatnya; (b) **peresmian
  aturan 86** atas dua kejadian terukur; (c) adjudikasi resmi **R-312** dan **R-313**
  berikut kelima larangan; (d) **H-A022 TERBUKTI**; (e) catatan bahwa **aturan 79
  dilemahkan** oleh praregistrasi R-313 di chat, dan apakah pengecualian itu hendak
  ditutup atau dirumuskan; (f) cacah tangan pada ref sesudah trio. **DILARANG disusun
  pada giliran yang sama dengan adjudikasi** (ADR-A016) — syarat itu kini **terpenuhi**,
  sebab adjudikasi R-313 sudah lewat dua giliran.

## Temuan sampingan

**[v13 — BARU] Karantina, terukur penuh** (kedelapan `reports/pulihkan_pecahan_<i>.json`,
ref `a2c4b83c`; `pulihkan` VERSI 2, `run_id_sumber` **30396803601**, ditulis
2026-07-29T02:48Z):

| pecahan | `baris_karantina` | parquet | blob laporan |
| --- | --- | --- | --- |
| 0 | 130.605 | 3 | `2e738ea33cf6b00544e685ca8137b215b2f301ae` |
| 1 | 131.760 | 3 | `9ddfb994eee11a81024dca97a4a0b0ab6785b098` |
| 2 | **0** (`karantina: null`) | 0 | `6f83de7e0f0b9e455cb5d66692074dcb9d2cd1a4` |
| 3 | 42.585 | 1 | `ce5d47b5ca99d56b5758a7f18cb64836221e0947` |
| 4 | 43.590 | 1 | `6b50a6571b560d2c96338898a8e859d01fc48e81` |
| 5 | **0** (`karantina: null`) | 0 | `b09913fd73e07ee293927b82a621b12589cce8e5` |
| 6 | 123.630 | 3 | `5d3f29ccb8181028030bed9e2fcc6f0d789a4150` |
| 7 | 43.965 | 1 | `dcd891af10b782c7c9fa2787403865097abc8856` |
| **jumlah** | **516.135** | **12** | — |

- **Mutu bukti:** kedelapan `pulih_sah` **true**; `cacah_sha_tak_cocok`,
  `cacah_bagian_hilang`, `cacah_anggota_kurang`, `cacah_anggota_tak_aman`,
  `selisih_baris_total` seluruhnya **0**; `baris_terverifikasi` true.
- **Sidik kode seragam** `76c27e3ce5d6edb13bb998b6ec65b538fb3d25205d4469bd4d186a95fa62d700`;
  **sidik kode manifes seragam** `237ccf427faf9d48e9c0904433a56e8902de64de6552daee5d3053093bfba601`
  → penjumlahan lintas pecahan **sah** (aturan 22).
- **Aturan 46 terbukti bekerja:** pecahan 2 dan 5 melaporkan
  `definisi_dapat_dibedakan` **false** dan menolak memilih definisi, alih-alih
  mengarang. Enam pecahan lain melaporkan `definisi_jumlah_baris` = "baris lolos +
  baris karantina".
- **Sebaran sangat tidak rata** — 42.585 sampai 131.760 baris per tar. Rata-rata
  **43.011** karena itu boleh dikutip sebagai turunan, **bukan sebagai bukti**.
- **Nama tar karantina:** `pecahan_<i>_karantina.part01.tar`.

**[v13 — BARU] `selisih_lilin` V1** (commit `c1dc0009`, laporan ringkas blob
`e5cc64011030cfb8e1a8edf3699dd01b3caafab7`, sidik kode `e6c77965…257e7`,
`byte_sumber` 6.834): `cacah_baris` **19586** · `cacah_berselisih` **0** ·
`jumlah_klaim_langsung` = `jumlah_terbaca_langsung` = **839325999** ·
`dua_jalur_bertemu` **true** · `selisih_terhadap_warisan` = {klaim 0, terbaca
−516135, bersih −516135} · `uji_r312.teradjudikasi` **false** · kode keluar alur
modul **2** (dirancang).

**[v11–v12, tetap berlaku] `sisa_defisit` V1** (run 30542217951, laporan ringkas blob
`91a05c05`, sidik kode `6211624b…f044b0`): penyebut kerja **17.398** (HIDUP 17.318 +
SEPI 80) · `cacah_berdefisit` **114** (HIDUP 111, SEPI 3, MATI 0; **0,66%**) ·
`cacah_calon_penuh` **17.284** · `defisit_calon` **712.925** (tautologis, KC-50) ·
`defisit_teratas` **291.379**, `bagian_teratas` **0,4087** · `defisit_terbesar`
**42.510** = **TLMUSDT 2023-03**, HIDUP, 2.130 dari 44.640 lilin (**95,2% kosong**) ·
sepuluh teratas tersebar di **tujuh bulan** → aturan 81 TIDAK terpicu · pasangan
`2022-05`: ANCUSDT **26.959** dan LUNAUSDT **26.950**, berselisih **sembilan lilin**
(dasar **H-A021**; kalimat sebab apa pun **DILARANG**) · sepuluh selisih invarian NOL,
ketiga kendali lolos.

**[v10] `keterisian_lilin` V1:** jumlah lilin semesta LANGSUNG **839.325.999** ·
`cacah_baris_tanpa_lilin` 0 dari 19.586 · MATI penuh **1.392**, tak penuh **9** ·
defisit semesta **18.143.601** dengan **17.335.439 (95,5%)** di bulan pertama dan
**808.162** di bukan-pertama (bagian **0,0445**) · bulan pertama rata terisi
**≈49,7%** · kesembilan baris MATI tak penuh (LENDUSDT 2020-11 13.475 · FRONTUSDT
2024-09 14.986 · FOOTBALLUSDT 2024-05 39.308 · ANTUSDT 39.309 · BTSUSDT 39.310 ·
SRMUSDT 39.311 · HNTUSDT 39.312 · TOMOUSDT 39.315 · COCOSUSDT 39.317; jumlah
**95.237** = 0,1178 dari 808.162) · harga TIDAK tersimpan (**14** medan).

**[v9] `bulan_pertama` V1:** 37 dari 38 baris HIDUP-kecil adalah bulan pertama
(0,973684); satu-satunya yang bukan **TLMUSDT 2023-03**; nisbah rata byte **0,527179**.

**[v8] `irisan_byte` V1:** di zona 22.440–97.634 byte ada **38 HIDUP dan 0 MATI**;
total byte **32.706.262.375**; HIDUP 32.049.492.952 · SEPI 77.728.024 · MATI
579.041.399 · `cacah_lain` 0.

**[v6] `lubang_tebing` V1:** `mati_dulu` **40** (0.339) · `serempak` **78** (0.661) ·
`lubang_dulu` **0**; tebing `2025-07` menguasai 39 dari 40 `mati_dulu`, satu-satunya
bukan-tebing **BTCSTUSDT** (KC-47); **122** dari 787 simbol pernah berlubang funding;
delapan simbol bangkit berjumlah 88.

**Belum diukur, urut prioritas [DIPERBARUI v13 — poros lama nomor 2 SELESAI]:**
(1) **lubang tengah gugus `2022-05` dan `2024-05`** untuk menegakkan atau meruntuhkan
**H-A021 dan H-A020 sekaligus** — kini poros tunggal berprioritas tertinggi;
(2) **identitas dua belas simbol-bulan karantina** (nama dan bulannya belum pernah
didaftar) — kandidat termurah, sebab manifesnya sudah ada di repo;
(3) **irisan 880 lawan 877 lubang funding** — kandidat KC-52 berikutnya: dua penyebut
mirip yang belum pernah dijajarkan; (4) **sebab kekosongan TLMUSDT 2023-03** (95,2%
kosong, HIDUP); (5) apakah "bulan pertama di penyebut" = "bulan pertama di bursa";
(6) tebing funding `2025-07` (39 simbol) dan BTCSTUSDT; (7) selisih 40−38
`diagnosa_kc15`; hari hilang BNXUSDT 2022-04/06/08; bentangan 38 kohort; H-A016;
mati_tersisip atas 19.586; **`ukur_baris` V6** (`BERKAS_DIUKUR` masih 21 nama atas
50 modul); R-7/19/20/28/36/37 dan R-199; R-236..R-247 dari jurnal 92–94; taksonomi
lubang tiga kelas.

## Penomoran berikutnya

Aturan resmi **1–81, 83, 84, 85** · usulan **77**, **78**, **82**, **86** (keempatnya
belum resmi) · **aturan berikutnya yang bebas 87** · KC resmi sampai **KC-52** (KC-16
kosong selamanya; KC-52 ditutup pada giliran ia diresmikan) · **KC berikutnya KC-53** ·
Hipotesis terbuka H-A016 (belum diuji), H-A017 (dilemahkan R-306), H-A018 (tafsir
dibatasi A014/A015), H-A019 (DITERIMA TERBATAS, DILEMAHKAN A018 kep. 6 tanpa
pengganti), **H-A020 (DIUSULKAN, belum diuji)**, **H-A021 (DIUSULKAN, belum diuji)**,
**H-A022 (TERBUKTI lewat R-313)** · Hipotesis berikutnya **H-A023** · Jurnal berikutnya
**141** · `STATE.md` berikutnya **v55** · EKOR berikutnya **v14** · **UKUR berikutnya
v13 (utang besar, usang sebagian)** · PROMPT berikutnya **v55 (belum didorong)** · ADR
berikutnya **A019** · Ramalan berikutnya **R-314** · papan skor **313**.
