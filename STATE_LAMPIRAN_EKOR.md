# STATE lampiran EKOR — bagian 2 dari STATE (v17, milik STATE v58)

**Mengapa berkas ini ada.** Dua push `STATE.md` berturut terpotong (v41, v42);
pemecahan ke tiga berkas berlaku sejak v43 (KC-42). Pembagian yang berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, 83, 84, 85, 86, **87**;
   KC-1..**KC-55**.
2. **`STATE_LAMPIRAN_EKOR.md`** (berkas ini, v17) — bagian 2: papan skor, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** — bagian 3: pengukuran, modul, API, hipotesis, koreksi.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) dan **`PROMPT_KELANJUTAN.md`**
   (blob `35beed44`) — **arsip; BUKAN sumber** (ADR-A018 kep. 9).

Dasar v17: EKOR v16 (blob **`1afefb8f99aeaf5a6529a246cffa354341ee9ec2`**, commit
**`3241393513750ca823d86e86808c88af9132491e`**), **dibaca UTUH pada giliran yang sama
sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43).

## KESERASIAN VERSI — dibaca apa adanya, termasuk yang belum serasi

Saat berkas ini didorong:

- `STATE.md` **v58** — blob **`986b138f400bfcd1fcd9f3592f50bef1b12f867c`**, commit
  **`839a0f17b558a6359c9746944c70bcbf9c33e61e`**, dibaca ulang UTUH pada giliran yang
  sama ia didorong. **SERASI** dengan berkas ini.
- `STATE_LAMPIRAN_EKOR.md` **v17** — berkas ini.
- `STATE_LAMPIRAN_UKUR.md` masih **v16** — blob
  **`510addd24bdd7dc04205b622fdda252e69c284f2`**, commit
  **`9b01c06ec5f2a58e0c083f4a924515c92475356b`**. **TERTINGGAL SATU VERSI.** Kepalanya
  berbunyi "milik STATE v57". Ia **tidak memuat**: R-316, papan skor **321**, **KC-55**,
  usulan **aturan 89**, kesalahan dokumen butir **16**, angka **51** dan **6**, temuan
  `gerbang_1m.py` pustaka murni, **Koreksi 14**, serta aturan 38 ke-57 dan ke-58.
  **Sampai UKUR v17 naik, sumber sah untuk seluruh butir itu adalah `STATE.md` v58,
  berkas ini, dan jurnal 146–147** — bukan UKUR v16.

**Satu berkas per push tetap MENGIKAT** (KC-42, KC-43).

**Tentang push berkas ini:** ia di akar repo sehingga menyalakan `ci.yml`. Tidak satu
pun `tests/**` berubah, jadi cacah uji tetap **1377** — ramalan deterministik, **MUDAH**,
TIDAK diskor, TIDAK menambah beruntun aturan 57. **Laporannya WAJIB dibaca sebelum push
akar berikutnya** (pemakaian aturan 38 **ke-59**).

## KESALAHAN DOKUMEN SENDIRI — kini ENAM BELAS

Daftar ini disalin dari STATE v58 dan berlaku identik di ketiga bagian. Sebab tetap
sama setiap kali: `push_files` menulis ulang SELURUH berkas, sehingga memperbaiki satu
karakter berarti menyusun ulang berkas besar dari konteks terpakai — persis yang
dicatat KC-42 sebagai cara paling pasti merusaknya. Perbaikan selalu menumpang pada
penulisan ulang yang memang sudah dijadwalkan.

| # | berkas | tertulis | seharusnya | status |
| --- | --- | --- | --- | --- |
| 1 | jurnal 132 §3 | "beruntun 2/1" | 2/2 | LUNAS di STATE v50 |
| 2 | EKOR v10 | `terisi ≉ 49,7%` | `≈ 49,7%` | LUNAS di EKOR v11 |
| 3 | jurnal 135 §13.3 | "hendan dirumuskan" | "hendak" | LUNAS di STATE v51 |
| 4 | EKOR v11 kepala | "deretministik" | "deterministik" | LUNAS di EKOR v12 |
| 5 | UKUR v11 kepala | "KESERAIAN VERSI" | "KESERASIAN VERSI" | LUNAS di UKUR v12 |
| 6 | UKUR v11 daftar uji | penanda `**` tak berpasangan | berpasangan | LUNAS di UKUR v12 |
| 7 | STATE v52 | "Empat salah ketik" padahal tabelnya enam | "Enam" | LUNAS di STATE v53 |
| 8 | STATE v53 aturan 45 | "empat push terakhir" lalu mendaftar ENAM | "enam push terakhir" | LUNAS di STATE v54 |
| 9 | STATE v53 aturan 52 | pembacaan ulang "tidak menangkap satu pun" | **satu dari delapan** | LUNAS di STATE v54 |
| 10 | jurnal 138 §5 butir 2 | "maka **839.842.134 yang keliru**" | kesimpulan **tidak sah dari premisnya** | LUNAS di jurnal 140 |
| 11 | jurnal 141 §6 | tuduhan atas EKOR v13 **dan ADR-A019** | tuduhan **terlalu luas** | LUNAS di EKOR v14 |
| 12 | ADR-A019 kep. 9 | poros karantina **"termurah"**; gugus lubang tengah `2022-05`/`2024-05` | manifes **20.533.802 B**; bulan sebenarnya **BTCSTUSDT 2022-01** dan **LITUSDT 2025-07..2025-11** | LUNAS di ADR-A020 kep. 8 |
| 13 | jurnal 142 §4 | **880 / 877 / 3** diumumkan sebagai temuan baru | ketiganya **sudah di STATE v55**; yang baru hanya **letak** selisih 3 | LUNAS di STATE v56 |
| 14 | STATE v56, keserasian nomor 2 | blob EKOR v14 ditulis berbelit, commit dikoreksi di tempat | ditulis bersih pada kolom terpisah | LUNAS di STATE v57 |
| 15 | ringkasan giliran sebelum jurnal 144 | `journal/2026-07-31-144.md` | konvensi **tanggal UTC**: `journal/2026-07-30-144.md` | LUNAS di STATE v57 |
| **16** | **jurnal 146 §5, pita butir 3 R-316** | pita **dua sisi** — `< 50` TEPAT, `= 50` MELESET | ruang nilainya **tiga sisi**; sisi **> 50** tidak tertutup, dan **51** itulah yang terukur | **LUNAS di STATE v58** |

**Kelas butir 16: KC-55**, yang diresmikan justru olehnya. Ia berbeda dari butir 14 dan
15: keduanya cacat **penulisan**, sedangkan butir 16 cacat **rancangan ramalan** — dan
cacat rancangan selalu lebih mahal, sebab ia membuka pintu bagi penulis untuk memilih
vonis sesudah melihat angka.

### Batas kekuatan aturan 52 — rumusan yang berlaku

> Pembacaan ulang **dokumen sendiri** lemah terhadap penalaran cacat: ia membaca
> kalimat yang sudah diyakini benar. Pembacaan **kode** kuat terhadapnya: kode
> menyatakan identitas yang tidak dapat ditawar.

**[v17] Bukti keempat, dan bentuknya baru:** R-316 butir 1 tidak dapat diadili sama
sekali, sebab bahan yang dipilih **tidak memuat jenis informasi yang diramalkan**. Yang
menyelamatkan bukan pembacaan dokumen sendiri melainkan **syarat gugur (c) yang ditulis
sebelum bahan dibuka**. **DILARANG** menulis bahwa aturan 52 menjaga mutu penalaran
**atas dokumen**; yang dijaganya **kesetiaan salinan**.

## KC-43..KC-55

(teks lengkap KC-43..KC-47 di STATE v47, KC-49 di v48, KC-50 di v50, KC-51 di v52,
KC-52 di v54, KC-53 di v56, KC-54 di v57, **KC-55 di v58**)

- **KC-43** — tanda tangan fungsi dari INGATAN.
- **KC-44** — semua laporan di-commit satu langkah.
- **KC-45 [RESMI v45]** — satuan "bulan tanpa funding" vs "bulan MATI" dicampur.
- **KC-46 [RESMI v45]** — lubang bentuk AWAL dibaca sebagai "funding berhenti".
- **KC-47 [RESMI v46]** — satu peristiwa menyamar sebagai banyak pengamatan bebas.
  **[v17] Terpicu lagi:** seluruh isi R-316 bergantung pada **satu simbol** (BNXUSDT).
- **KC-48 [RESMI v47]** — ambang absolut pada sebaran yang belum diukur.
- **KC-49 [RESMI v8 lampiran ini]** — pita dikunci tanpa aritmetika implikasi.
  **[v17] Kerabat terdekat KC-55**, tetapi berbeda: KC-49 tentang **implikasi** pita,
  KC-55 tentang **cakupan** pita.
- **KC-50 [RESMI di STATE v50]** — agregat lewat jalan memutar.
- **KC-51 [RESMI v52]** — bias taksiran pemusatan. Empat kejadian berturut tanpa
  pembalikan arah. **[v17] Kejadian kelima TIDAK dicatat**, tetapi arah R-316 patut
  disebut apa adanya: taksiran **48** dan pita **< 50** keduanya **di bawah** nilai
  terukur **51**. Itu **arah yang sama** dengan keempat kejadian lama — namun karena
  butir 2 bukan pita melainkan titik tunggal, dan butir 3 pitanya cacat, **tidak satu
  pun dari keduanya sah dihitung sebagai kejadian KC-51**. Dicatat sebagai **kecurigaan
  terbuka**, bukan sebagai kejadian.
- **KC-52 [RESMI di STATE v54]** — dua penyebut berbeda diperlakukan sebagai satu.
  **[v17] MENDAPAT KASUS BARU YANG TAJAM:** untuk BNXUSDT kini ada **tiga** angka yang
  semuanya benar dan semuanya berbeda — **48** (`cacah_bulan_klines_simbol`), **50**
  (rentang kalender, TURUNAN), **51** (`bulan_per_simbol` semesta 1m). Mencampur
  ketiganya adalah KC-52 dalam bentuk paling murni.
- **KC-53 [RESMI di ADR-A020 kep. 3]** — nol pada medan dibaca sebagai ketiadaan
  fenomena.
- **KC-54 [RESMI di ADR-A021 kep. 3]** — **nama medan dibaca sebagai definisi medan.**
  **[v17] KINI TIGA KEJADIAN:** (1) label gugus `2022-05`/`2024-05`;
  (2) `lubang_tak_dikenal`; (3) **`bulan_per_simbol`** — dibaca sebagai *daftar* bulan,
  isinya *cacah* bulan. **Tiga kejadian dalam tiga giliran akar berturut: pola, bukan
  kesialan.** Penangkalnya naik status menjadi prasyarat kumulatif, dan bila definisi
  medan **tidak dapat ditemukan**, ramalan atasnya **WAJIB** disertai syarat gugur
  tersurat.
- **KC-55 [RESMI di STATE v58]** — **pita ramalan tidak menutup seluruh ruang nilai.**
  Pita ditulis atas sebagian sisi saja sehingga hasil di sisi yang tak tertutup tidak
  punya vonis yang dikunci di muka; akibatnya penulis dapat memilih vonis **sesudah**
  melihat angka. **Angka terukur kasus asal (aturan 42):** pita `< 50` / `= 50`,
  terukur **51**. **Penangkal:** tulis ketiga sisi, atau nyatakan mengapa satu sisi
  mustahil; bila terlanjur, vonis diambil dari **isi** ramalan, bukan bunyi harfiahnya.
- **KC berikutnya yang bebas: KC-56.**

## Papan skor prediksi — lengkap R-300..R-316 (R-199..R-299 di v4, blob `67dda29e`)

| # | Prediksi | Status |
|---|---|---|
| R-300 | (1) cacah_bulan 64; (2) tetangga BTCST HIDUP; (3) cacah_hidup 8..30 dan MATI>HIDUP | **SEPARUH** |
| R-301 | (1) tebing==0; (2) mati_tersisip ≥1; (3) bangkit==0 | **TIDAK TERADJUDIKASI** |
| R-302 | (1) simbol tersisip 1..10; (2) simbol-bulan 1..50; (3) penyebut 19.586/787 | **SEPARUH** (butir 2 MELESET 88>50) |
| R-303 | (1) simbol tersisip 1..60; (2) simbol-bulan 1..300; (3) penyebut/kendali/kode 0 | **TEPAT (3/3)** |
| R-304 | (1) mati_dulu 5..8; (2) hidup_berlubang 3..8; (3) penyebut/kendali/kode 0 | **MELESET** |
| R-305 | (1) bagian mati-tak-setelah-lubang 0.55..0.95; (2) lubang-awal 20..120; (3) MUDAH | **MELESET** — penyebut 118, bagian **1.0** (tautologis); **5**; butir 3 TEPAT |
| R-306 | (1) bagian arah STRIKT 0.25..0.60; (2) tebing 2025-07 20..90; (3) MUDAH | **TEPAT (3/3)** — **0.339**; **39** |
| R-307 | (1) bagian byte MATI 0.02..0.15; (2) simbol-bulan byte<10.000 20..400; (3) MUDAH | **MELESET** — **0.017704**; **0** (KC-48) |
| R-308 | (1) HIDUP byte<97.634 dalam 20..600; (2) MATI byte<150.000 dalam 10..300; (3) MUDAH | **SEPARUH** — **38** menang; **2** kalah (kasus pertama KC-51) |
| R-309 | (1) HIDUP-kecil bulan pertama 22..38; (2) nisbah rata byte 0.10..0.60; (3) MUDAH | **TEPAT (3/3)** — **37**; **0,527179** |
| R-310 | (1) MATI berdefisit 1..120; (2) bagian defisit bukan-pertama 0.02..0.25; (3) MUDAH | **TEPAT** — **9**; **0,0445** (keduanya tipis ke tepi BAWAH) |
| R-311 | (1) bukan-pertama bukan-MATI berdefisit 200..12.000; (2) bagian sepuluh teratas 0,02..0,45; (3) MUDAH | **SEPARUH** — **114** kalah; **0,4087** menang |
| R-312 | (1) baris berselisih 12..120; (2) bagian baris teratas 0,50..0,865; (3) MUDAH | **TIDAK TERADJUDIKASI** — `cacah_berselisih` **0**, penyebut butir 2 NOL (aturan 41) |
| R-313 | (1) Σ `baris_karantina` = **516.135**; (2) Σ parquet = **12** | **TEPAT (2/2)** — selisih **0**, dengan **cacat aturan 79 melekat permanen** |
| R-314 | (1) `cacah_per_simbol_funding` ∈ [747, 827]; (2) `h_a010_cacah_simbol_berisi` = 0; (3) `h_a011_cacah_hidup` = 0 | **2 TEPAT / 1 MELESET** — **787** · **0** · **6** MELESET. Butir 2 dan 3 TURUNAN. |
| R-315 | (1) pemilik ketiga `lubang_tak_dikenal` = **1**; (2) **ketiga** lubang lebih awal daripada `bulan_klines_pertama`; (3) MUDAH | **1 TEPAT / 1 MELESET** — **1** (BNXUSDT) TEPAT; **1 dari 3** MELESET. **Syarat gugur (e) MENYALA.** |
| **R-316** | (1) 2022-06 dan 2022-08 **tidak hadir** sebagai bulan 1m BNXUSDT; (2) cacah bulan BNXUSDT = **48**; (3) [TURUNAN] cacah **< 50**; (4) MUDAH: berkas terbaca utuh | **0 TEPAT / 2 MELESET / 1 TIDAK TERADJUDIKASI** — butir 1 **GUGUR** lewat syarat (c), berkas tidak memuat satu nama bulan pun; butir 2 **MELESET** (**51**, selisih +3); butir 3 **MELESET** (**51**, pita cacat → KC-55); butir 4 terpenuhi, tidak masuk lajur |

**Total R-1..R-316** (dihitung TANGAN dari rincian v16, aturan 21):

- TEPAT **221**
- MELESET **61**
- SEPARUH **22**
- TIDAK TERADJUDIKASI **10**
- MENUNGGU **7** (R-7, R-19, R-20, R-28, R-36, R-37, R-199)

221 + 61 = 282; 282 + 22 = 304; 304 + 10 = 314; 314 + 7 = **321** ✅ Nomor terpakai
R-1..R-316. N_percobaan = 0. **ADJUDIKASI RISET TETAP TERKUNCI.**
**Pertambahan dari 318:** MELESET **+2**, TIDAK TERADJUDIKASI **+1**, seluruhnya dari
**R-316**. **TEPAT tidak bergerak sama sekali.**

**[v17] Lajur MENUNGGU sengaja TIDAK bergerak.** R-316 **tidak pernah sempat tercatat
menunggu**: praregistrasinya (jurnal 146, commit `440fe8ba`) dan adjudikasinya (jurnal
147, commit `e429e4fb`) berjarak **satu giliran**.

**[v17] PAPAN SKOR 321 KINI SAH.** STATE v58 mencatatnya sebagai penerapan aturan 21;
**pengesahan lajur terjadi di berkas ini**, dan tidak di tempat lain.

**Kolom terpisah — DI LUAR lajur papan skor:** **R-229 TEPAT** dan **R-230 MELESET**
(ADR-A020 kep. 5). **R-228 tetap BELUM diadjudikasi.**

**Nisbah papan skor, dihitung tangan:** dari 304 ramalan yang beradjudikasi penuh
(221 + 61 + 22), TEPAT **72,7%**, MELESET **20,1%**, SEPARUH **7,2%**. Ketiganya turun
atau naik ke arah yang tidak menyenangkan dibandingkan v16 (73,2 / 19,5 / 7,3), dan itu
**disebut apa adanya**. Angka ini tetap **DILARANG dibaca sebagai mutu ramalan**:
sebagian besar butir ketiga tiap ramalan berlabel MUDAH. **R-312 DILARANG masuk
pembilang maupun penyebut.**

**Utang papan skor:** rincian R-236..R-247 masih di jurnal 92–94; pemeriksaan
R-224..R-235 belum dikerjakan.

### [v17] R-316 — kekalahan ganda yang wajib disebut telanjang

**Diramalkan 48; terukur 51. Diramalkan kurang dari 50; terukur lebih dari 50.**
Tidak ada pembungkus untuk itu, dan **tidak ada kemenangan harfiah yang diambil**.

Ramalan ini dirancang untuk menang: bahannya dipilih hati-hati sesudah bahan lama
dibatalkan karena ukuran, dan sebelas syarat kumulatif diperiksa satu per satu di
jurnal 146 §6. Ia tetap kalah dua kali. **Dan justru karena itu ia berguna:** ia
memaksa keluar angka **51**, yang tidak pernah tertulis di dokumen akar mana pun, dan
yang **lebih besar** daripada rentang kalender klines BNXUSDT sendiri.

**Fakta baru itu lahir dari kekalahan, bukan dari kemenangan.** Kalimat itu ditulis di
sini bukan sebagai penghiburan melainkan sebagai catatan metodologis: pada riset ini,
ramalan yang kalah telah **dua kali berturut** (R-315, R-316) menghasilkan lebih banyak
pengetahuan daripada butir MUDAH yang menang.

**Yang DILARANG disimpulkan** — diulang di sini karena godaannya besar:

1. **DILARANG** menyatakan tiga bulan selisih (51 − 48 = 3) **adalah** 2022-04 /
   2022-06 / 2022-08. **Kesamaan cacah bukan kesamaan identitas.**
2. **DILARANG** menyatakan gerbang 1m menjatuhkan bulan mana pun; `gerbang_1m.py`
   **tidak berkeluaran**, dan tidak ada medan yang menamai klausa pelanggaran per
   simbol-bulan.
3. **DILARANG** membandingkan 51 dan 48 tanpa menyebut **selisih 23 jam** antara kedua
   laporan (2026-07-28T09:44:48Z lawan 2026-07-29T08:17:55Z).
4. **DILARANG** menyamakan "tidak ada di penyebut" dengan "dijatuhkan gerbang".
5. **DILARANG** menskor butir 3 sebagai TEPAT atas dasar bunyi harfiah pita.

### [v17] Aturan 88 dan 89 — keduanya TETAP USULAN

> **Usulan aturan 88 (ADR-A021 kep. 5).** Ramalan bahwa **semua** anggota sebuah
> himpunan berbagi satu sifat **WAJIB** disertai **mekanisme tertulis**; bila yang
> tersedia hanya nama medan atau kesan pola, ramalan **WAJIB** ditulis sebagai
> **sebaran**.

**[v17] TIDAK mendapat kejadian kedua.** Butir 1 R-316 memang biner tanpa mekanisme,
tetapi ia **gugur karena bahan**, bukan kalah karena keseragaman. Menghitungnya sebagai
kejadian kedua berarti **mengesahkan aturan dengan bukti yang dipaksakan** — persis
yang dilarang ADR-A019 kep. 3. Tetap **satu** kejadian.

> **Usulan aturan 89 (lahir dari butir 16).** Setiap pita ramalan atas sebuah bilangan
> **WAJIB** menutup **ketiga sisi** ruang nilainya — di bawah, tepat, dan di atas —
> atau menyatakan tertulis mengapa satu sisi mustahil.

Baru **satu** kejadian (R-316 butir 3). Diresmikan pada kejadian kedua.

**Catatan kejujuran yang melekat pada keduanya:** aturan 88 dan 89 sama-sama lahir
**sesudah** kekalahan. Keduanya **utang yang dibayar, bukan laba**, dan **DILARANG**
diklaim sebagai kemenangan metodologis.

### [v17] Aturan 85 — TETAP DUA ADJUDIKASI

R-316 butir 3 **bukan** adjudikasi aturan 85: pitanya tidak menutup ruang jawaban,
sehingga tidak ada "tepi" yang sah untuk dinilai. **DILARANG** menyebut aturan 85
**teruji**, **bekerja**, atau **terbukti**.

### Lima larangan permanen yang menempel pada R-312 (tidak berubah)

1. **DILARANG** mengatakan pita butir 1 (12..120) "tidak terbantah". Ia tidak diuji.
2. **DILARANG** mengatakan kalibrasi membaik atau memburuk karena R-312.
3. **DILARANG** menghitungnya di pembilang maupun penyebut nisbah kemenangan.
4. **DILARANG** menghidupkannya kembali dengan alasan penjelasannya kini ditemukan.
5. Angka **12** di R-313 adalah cacah **parquet karantina** — arti berbeda dari 12 di
   R-312 butir 1. **Kesamaan itu DILARANG dibaca sebagai konfirmasi apa pun.**

### Larangan yang lahir bersama STATE v57/ADR-A021, tetap penuh

1. `lubang_tak_dikenal` **bukan** pernyataan arah waktu.
2. Vonis R-315 **DILARANG** ditulis SEPARUH.
3. Kemunculan BNXUSDT **DILARANG** dibaca sebagai konfirmasi fakta lama.
4. Sebab BNXUSDT 2022-06/2022-08 **DILARANG** diklaim.
5. Cacah total `baris_mati` **DILARANG** diklaim terukur (terpotong **54%**); selisih
   TLMUSDT **20** lawan **19** adalah **utang bacaan, bukan cacat laporan**.
6. Empat kecocokan pasca-hoc jurnal 145 §7 **DILARANG** masuk lajur skor.
7. Aturan 88 **— dan kini 89 — DILARANG** diklaim kemenangan metodologis.

**[v17] Larangan baru:** `reports/kehidupan_arsip_*.json` (991.422–1.261.637 B per
berkas) **DILARANG** dibuka dengan harapan dibaca utuh; poros yang menuntutnya
**berhenti**.

## Catatan kejujuran [v17]

1. **Kekalahan disebut telanjang, dengan angka.** Diramalkan **48**, terukur **51**;
   diramalkan **< 50**, terukur **51**. Dua butir berisiko, dua kalah, nol menang.
2. **Kemenangan harfiah ditolak sendiri.** Pita butir 3 secara harfiah tidak dilanggar
   (51 bukan 50), dan menskornya TEPAT akan lolos dari pembaca mana pun. Ia **ditolak
   di jurnal 147**, sebelum papan skor disentuh, dan penolakan itu **FINAL**.
3. **Syarat gugur yang ditulis di muka menyelamatkan giliran ini.** Tanpa syarat (c),
   butir 1 akan disulap menjadi SEPARUH. Ini bukti pertama bahwa **syarat gugur bekerja
   sebagai penjaga**, bukan sekadar hiasan praregistrasi.
4. **Aturan 79 DITAATI SEPENUHNYA untuk KETIGA kalinya berturut.** Praregistrasi commit
   `440fe8ba`, adjudikasi commit `e429e4fb`. Saksinya **git**.
5. **Aturan 88 dan 89 sengaja TIDAK diresmikan.** Keduanya berdiri di satu kejadian.
   Meresmikannya sekarang akan terasa produktif dan **akan salah**.
6. **Aturan 36 sengaja TIDAK diberi kasus keempat.** Kesamaan **3 = 3** lahir dari dua
   laporan berjarak 23 jam yang belum terbukti mengukur himpunan yang sama;
   memasukkannya akan mengulang KC-38.
7. **Aturan 57 beruntun 4 dari 4, tidak bertambah.**
8. **Aturan 52 ditaati dua puluh satu kali berturut** hingga STATE v58, **dua puluh
   dua** dengan berkas ini.
9. **`PROMPT_KELANJUTAN.md` tetap belum diberi kepala "ARSIP — BUKAN SUMBER"** dan
   `PROMPT.md` **v55 belum didorong**. Utang ini kini berumur tujuh versi.
10. **Jebakan laporan CI terbukti nyata dan terhindari.** Sesudah push STATE v58,
    pembacaan pertama `reports/ci_terakhir.json` mengembalikan blob `5b433a93` dengan
    `commit` `9b01c06e` — **laporan ke-57 yang lama**. Mencatatnya sebagai ke-58 akan
    **mengarang jejak**. Ia **tidak dicatat**; laporan ke-58 yang sejati baru terbaca
    pada giliran berikutnya. **Laporan sah hanya bila medan `commit` cocok.**
11. **Pemeriksaan silang yang menutup tanpa sisa** (terbitan, TIDAK diskor):
    18.799 − 1.401 = **17.398**; 98 − 80 = **18**; 769 + 18 = **787**;
    **19.586 + 12 = 19.598**; **839.325.999 + 516.135 = 839.842.134**;
    **880 − 877 = 3**; `tabel_silang` **33 + 842 + 2 + 0 = 877**.
    **[v17] Yang TIDAK menutup, dan itu justru temuannya: 51 − 48 = 3, tanpa satu pun
    nama bulan yang menjelaskannya.**

**Kesalahan proses [v17].** Tidak ada kegagalan panggilan alat baru; seluruh `runTool`
berhasil dengan bungkus `{toolName, toolArguments}`. Yang lama tetap tercatat: push
STATE v55 pernah ditolak karena bungkus itu tidak dipakai — **kesalahan bentuk
panggilan, bukan galat alat**. Kerugian lama: laporan CI run `30547842823` hangus, blob
ke-38 tak dapat dipulihkan. **Batas alat yang tetap terbuka:** `silang_funding.json`
**54%**, daftar `reports/` **76%**, `kehidupan_arsip_*.json` **mustahil**.

## Jumlah uji

**1377 TERUKUR, kini EMPAT BELAS bacaan berjejak (ke-45..ke-58).**

Sepuluh bacaan pertama (ke-45..ke-54) tercatat di v16 dan tidak diulang di sini kecuali
blob penuhnya sudah tercatat; tiga yang terbaru:

12. **[v16]** blob **`8ea8cc463ff58246b363e47458e9355d26a5ea79`**: run **30587658376**,
    commit **`ebe6f373`** (STATE v57), **22:36:15Z**, kode 0, `1377 in 0.40s` —
    **tercepat yang pernah tercatat**.
13. **[v17]** blob **`34f88b3744e4d9733a731f3f97056584344ddc33`**: run **30588460935**,
    commit **`32413935`** (EKOR v16), **22:49:39Z**, kode 0, `1377 in 0.61s`.
14. **[v17]** blob **`5b433a93a3f0d3bb2cded75a5c0379c4a557ae3d`**: run **30589452976**,
    commit **`9b01c06e`** (UKUR v16), **23:07:02Z**, kode 0, `1377 in 0.55s`.
15. **[v17]** blob **`9718bf98caafc59349465ff55b9755e4ea309ac3`**: run **30590593816**,
    commit **`839a0f17b558a6359c9746944c70bcbf9c33e61e`** (STATE v58),
    **2026-07-30T23:28:30Z**, kode 0, `1377 tests collected in 0.61s`.

Turunan: 1341 + **36** butir `tests/test_selisih_lilin.py` = **1377** ✅ (aturan 21),
terverifikasi dari sumber, bukan dari ingatan.

Riwayat panjang: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 →
984 → 1044 → 1100 → 1168 → 1233 → 1297 → 1341 (enam run) → **1377** (empat belas run
berjejak).

Cacah per berkas uji (**milik repo riset ini — bukan repo warisan**):
`test_irisan_byte.py` **68** · `test_bulan_pertama.py` **65** ·
`test_keterisian_lilin.py` **64** · `test_bentangan_kohort.py` V2 **63** ·
`test_lubang_tebing.py` **60** · `test_sebab_bangkit.py` **57** ·
`test_byte_semesta.py` **56** · `test_lubang_awal.py` **48** ·
`test_tersisip_semesta.py` **47** · `test_anatomi_tengah.py` **47** ·
`test_sisa_defisit.py` **44** · `test_selisih_lilin.py` **36** · `test_terhenti.py` V4
**33** · `test_bulan_absen.py` **32** · `test_karantina_semesta.py` **28** ·
`test_silang_settled.py` **24** · `test_ukur_baris.py` **3**.
**`tests/test_lubang_tengah.py` — 56 butir menurut R-228, BELUM DIBACA, DILARANG
dikutip sebagai cacah terukur.**
**[v17] `tests/test_gerbang_1m.py` — disebut docstring `gerbang_1m.py` sebagai penjaga
penyimpangan salinan rumus `menit_hilang_dalam_rentang`. BELUM DIBACA; cacah butirnya
TIDAK DIKETAHUI.**

**Aturan 57: beruntun 4 dari 4.** Hanya push yang menyentuh `tests/**` yang dihitung.

### ORDINAL ATURAN 38 — buku besar, kini sampai ke-58

**Definisi yang berlaku (ADR-A018 kep. 8):** pemakaian dihitung **hanya** untuk
pembacaan `reports/ci_terakhir.json` yang meninggalkan **jejak tertulis** berupa nomor
run + commit + blob di STATE, lampiran, atau jurnal.

| ke- | CI | run | commit | blob | jejak |
|---|---|---|---|---|---|
| 49 | 1377 | 30579348728 | `cd209f3e` | `94d270e7` | EKOR v14, STATE v56 |
| 50 | 1377 | 30580133552 | `a722ec63` | `04bfa2ed` | jurnal 142, STATE v56 |
| 51 | 1377 | 30581703827 | `6157586e` | `aeb4315a` | jurnal 142, STATE v56 |
| 52 | 1377 | 30583686515 | `019d16ea` | `19785af1` | EKOR v15 |
| 53 | 1377 | 30584737431 | `94c7d9da` | `5f4282f6` | UKUR v15, STATE v57 |
| 54 | 1377 | 30585269231 | `d551f471` | `340c3c7f` | STATE v57 |
| 55 | 1377 | 30587658376 | `ebe6f373` | `8ea8cc46` | EKOR v16 |
| 56 | 1377 | 30588460935 | `32413935` | `34f88b37` | UKUR v16 |
| 57 | 1377 | 30589452976 | `9b01c06e` | `5b433a93` | jurnal 146, STATE v58 |
| **58** | **1377** | **30590593816** | **`839a0f17`** | **`9718bf98caafc59349465ff55b9755e4ea309ac3`** | **berkas ini** |

**Pemakaian berjalan = ke-lima puluh delapan.** Pemakaian ke-58 dibaca
**2026-07-30T23:28:30Z**, kode keluar **0**, atas push **STATE v58** — dibaca **sebelum
tertimpa**, sehingga ramalan "CI tetap 1377" untuk push itu **TERUKUR dan TEPAT**, tetap
**MUDAH**, tetap tidak diskor.

**[v17] Delapan belas pembacaan berturut (ke-42..ke-58) tanpa satu pun laporan hangus.**

**Bot CI menambah satu commit di atas tiap push pemicu** — kini **sepuluh kali
berturut** (`0fa2b867`, `c139f16a`, `c4a7468e`, `ff89f688`, `47769b18`, `e271a711`, dan
pendahulunya). **Deterministik dari `ci.yml`; DILARANG dihitung sebagai kemenangan
ramalan.**

**Dua cacat tetap disebut apa adanya:** baris ke-**38** (run `30541051907`, CI 1297,
commit `5d7d8b96`) **tanpa blob**; dan run **30547842823** (bot `de2fc03d`) **tidak
pernah dibaca**, tertimpa, **DILARANG dihitung**. Bila jejak lain ditemukan di jurnal
133–134, nomor ini **WAJIB dikoreksi, bukan dipertahankan**.

**Calon aturan** — dua push akar berturut tanpa membaca laporan di antaranya — **tetap
DITOLAK diresmikan**: masih **satu** kejadian.

## Utang verifikasi

1-5, 11 menunggu tahap juri. 6-23, 25-29, 31 LUNAS. **Nomor utang BUKAN nomor ramalan
— KC-32.**

24. **AKTIF. LUNAS BARU [v17]:**
    - **`lux_ai/serapan/gerbang_1m.py` DIBACA UTUH** — blob
      **`c8cc54c84a57173ef2e426c317d6ac50734e9b4a`**. Penerapan **ADR-A004 §2**; enam
      klausa; **pustaka murni tanpa keluaran**.
    - **`reports/semesta_bulan_1m.json` DIBACA UTUH** — blob
      **`a1a6d3f0f13dd7100a91853cadfcaa9a5620fee3`**, 18.884 B.
    - **`journal/2026-07-30-146.md`** — blob `1992c8ef15ea0e243ddf0707ace661cb5a574383`,
      commit `440fe8ba`.
    - **`journal/2026-07-30-147.md`** — blob `eaf941f6a871083f8dcc857e310c1658cab59b84`,
      commit `e429e4fb`.
    - **`STATE.md` v58** — blob `986b138f400bfcd1fcd9f3592f50bef1b12f867c`, commit
      `839a0f17`.
    - **EKOR v16 dibaca UTUH** pada giliran ini — blob
      `1afefb8f99aeaf5a6529a246cffa354341ee9ec2`.
    - `reports/ci_terakhir.json` ke-55..ke-58 dibaca utuh, blob DICATAT.
    **TETAP BELUM:** `decisions/ADR-A002`, **A004 (NAIK PERINGKAT — sumber keenam
    klausa gerbang)**, **A006**, **A007**, **A008**; **`tests/test_gerbang_1m.py`**;
    `.github/workflows/karantina_semesta.yml` (`de40fa4e`); `tests/test_pulihkan.py`
    (`11c43533`); `tests/test_rilis_karantina.py` (`739c8da9`);
    `tests/test_karantina_a006.py` (`a5a3d82f`); `tests/test_lubang_tengah.py`;
    **bagian `baris_mati` `silang_funding.json`**.
30. **AKTIF — UTANG HIDUP**, ADR-A019 kep. 8 MENOLAK menutupnya. Angka **50 / 54 / 45**
    tetap **TURUNAN**. Yang sah tetap **49 / 53 / 44 / 18** pada ref `3196fd98` dan
    `8a614567`. **[v17] Tidak ada modul baru — utang tidak bertambah, juga tidak
    berkurang.** Cacah entri `bulan_per_simbol` **tidak dihitung** dan tidak dikutip.
32. **AKTIF — tiga butir "memerlukan verifikasi" `PETA_MODUL.md`** (repo **WARISAN**):
    (a) `enable_hs`; (b) "30 pair alfabetis"; (c) "kendala mengikat = kapasitas margin".
33. **[v17] LUNAS untuk butir 16** — ditulis resmi di STATE v58 dan disalin ke berkas
    ini. Daftar berdiri di **enam belas** butir, **tanpa calon baru**.
34. **AKTIF — `PROMPT_KELANJUTAN.md` belum berkepala "ARSIP — BUKAN SUMBER"**, dan
    **`PROMPT.md` v55 belum didorong.**
35. **[v17] LUNAS sebagian** — UKUR v16 sudah naik. **Digantikan utang baru:** UKUR
    **v17** belum naik; sampai itu, UKUR v16 tertinggal satu versi.
36. **AKTIF — identitas dua belas simbol-bulan karantina belum pernah didaftar.**
    Manifes **20.533.802 B** — jalan satu-satunya **modul CI**.
37. **AKTIF — `ukur_baris.py` V6 belum ditulis.** `BERKAS_DIUKUR` masih **21** nama.
38. **AKTIF — R-228 belum diadjudikasi.** Cacah 56 butir `test_lubang_tengah.py`
    **DILARANG** dikutip sebagai terukur.
39. **AKTIF — bagian `baris_mati` `silang_funding.json` belum terbaca** (54%). Jalannya
    **modul CI** atau **pembacaan berpotong yang dirancang**.
40. **BARU [v17] — identitas 51 bulan 1m BNXUSDT belum diketahui.** Cacahnya terukur
    (**51**), nama bulannya **tidak**. Ini utang yang **memblokir H-A023** dan poros
    peringkat pertama sekaligus. Bahan calon: `reports/semesta_rentang.json`
    (`8d5bd06ca4073dac8a8ef7841d81824427cc8e63`, 110.662 B), **belum dibuka**.
41. **BARU [v17] — daftar `reports/` belum terbaca utuh** (terpotong **76%** pada ref
    `8364ad92f0a52015f9285ed5f2a9c8eaff33f732`). Keputusan bahan sejauh ini diambil
    **hanya dari bagian yang terlihat**; mungkin ada laporan yang belum diketahui
    keberadaannya. Ini melemahkan penerapan **aturan 86 (a)** dan wajib disebut setiap
    kali (a) dipakai.

## Daftar ADR

- **ADR-A001** aturan dasar. DITERIMA.
- **ADR-A002** serapan. Kondisi v3 berlaku; §10 tetap tidak boleh diubah. **BELUM DIBACA UTUH.**
- **ADR-A003** taksonomi rezim. **BELUM ADA — blokir pertama klasifikasi.**
- **ADR-A004** kebijakan KC-6. DITERIMA. **BELUM DIBACA UTUH — [v17] NAIK PERINGKAT**,
  sebab `gerbang_1m.py` menyatakan dirinya penerapan **§2** ADR ini; keenam klausa
  gerbang bersumber di sana.
- **ADR-A005** jenis instrumen. DITERIMA.
- **ADR-A006** karantina + persistensi. DITERIMA, TERVERIFIKASI. **BELUM DIBACA UTUH.**
- **ADR-A007** serapan hibrida. DIUSULKAN. **BELUM DIBACA UTUH.**
- **ADR-A008** akibat KC-18. Kep. 1–6 DITERIMA; **kep. 7 DITANGGUHKAN.** **BELUM DIBACA UTUH.**
- **ADR-A009** (`17a594b6`). **DICABUT PENUH oleh ADR-A012.**
- **ADR-A010** (`c4bccf21`) — klaim "kebangkitan tunggal" DICABUT. DITERIMA.
- **ADR-A011** (`645fd5df`) — arah sebab A009 dicabut untuk kelas bangkit. DITERIMA.
- **ADR-A012** (`f9f564d1`) — arah sebab dicabut untuk SELURUH semesta. DITERIMA.
- **ADR-A013** (`8ba4f989`) — (2) dan (4) kini aturan **80** dan **81**. DITERIMA.
- **ADR-A014** (`6d77c2cd`) — byte parquet; (5) melahirkan KC-48. DITERIMA.
- **ADR-A015** (`387d5510`) — (5) besar berkas bukan detektor status ke arah mana pun —
  **TIDAK dibalik oleh R-310..R-316**. DITERIMA.
- **ADR-A016** (`209802d7`) — **kewajiban adjudikasi pada giliran berbeda** berasal dari
  sini; kep. 4 DIKOREKSI oleh A018 kep. 6. DITERIMA. **[v17] Ditaati ketiga kalinya
  berturut.**
- **ADR-A017** (`1be570f2`) — kep. 4 TERJAWAB PENUH oleh R-313. DITERIMA.
- **ADR-A018** (`3fba599e`) — (8) definisi ordinal aturan 38; (9) `PROMPT_KELANJUTAN.md`
  arsip, **perintah operator menang**; (10) dua cacah `tests/`; (11) cacah tangan
  49/53/44/18. DITERIMA.
- **ADR-A019** (`9cd7d25e…`, commit `e6007ba5`) — (3) **aturan tidak diresmikan atas
  satu kejadian**; (8) utang cacah tangan ditolak ditutup. **DITERIMA — kep. 9
  DIKOREKSI oleh A020 kep. 8.** **[v17] Kep. 3 dipegang dua kali pada giliran ini**
  (aturan 88 dan 89 keduanya ditahan).
- **ADR-A020** (`200c7e7d…`, commit `d8335be1`) — sepuluh keputusan. DITERIMA.
- **ADR-A021** (`3e756672…`, commit `2cee14b7`) — sepuluh keputusan: (1) R-315 final;
  (2) bacaan `lubang_tak_dikenal` DICABUT; (3) KC-54; (4) aturan 87 RESMI; (5) aturan 88
  DIUSULKAN; (6) poros irisan 880/877 TUNTAS pembukuan; (7) urutan poros; (8) kecocokan
  pasca-hoc dilarang diskor; (9) cacah `baris_mati` dilarang diklaim; (10) papan skor
  318 dan penomoran A022. DITERIMA.
- **ADR-A022 [BELUM ADA]** — **[v17] calon isinya berubah oleh R-316:** bukan lagi
  "sebab dua bulan hilang", melainkan **status tiga angka bersaing untuk BNXUSDT (48 /
  50 / 51)** dan apakah KC-52 perlu diperluas. **DILARANG disusun pada giliran yang sama
  dengan adjudikasi** (ADR-A016).

## Temuan sampingan

### [v17] `semesta_bulan_1m.json` — bahan R-316

Blob **`a1a6d3f0f13dd7100a91853cadfcaa9a5620fee3`**, **18.884 B**, `waktu_utc`
**2026-07-28T09:44:48Z**. **Terbaca UTUH.**

**Struktur:** dua kunci tingkat atas — `bulan_per_simbol` (peta simbol → **bilangan
bulat**) dan `waktu_utc`. **Tidak ada nama bulan di berkas ini, untuk simbol mana pun.**

| medan | nilai |
| --- | --- |
| `bulan_per_simbol["BNXUSDT"]` | **51** |
| `bulan_per_simbol["BNXUSDTSETTLED"]` | **6** |

**Tiga angka bersaing untuk satu simbol, semuanya benar:** **48**
(`cacah_bulan_klines_simbol`, `silang_funding.json`), **50** (rentang kalender
2022-05..2026-06, TURUNAN), **51** (`bulan_per_simbol`). **51 − 48 = 3**, dan
`cacah_lubang_tak_dikenal` juga **3** — **kesamaan cacah, bukan identitas.**

### [v17] `lux_ai/serapan/gerbang_1m.py` — dibaca utuh

Blob **`c8cc54c84a57173ef2e426c317d6ac50734e9b4a`**. Penerapan **ADR-A004 §2**.

**Enam klausa `KLAUSA`:** `deret_tidak_kosong` · `tanpa_duplikat` ·
`tanpa_menit_hilang` · `jarak_60_detik` · `selaras_menit` · `satuan_milidetik`.
`nilai_deret` → `lolos = not pelanggaran`; **satu klausa gagal cukup menjatuhkan**.
`MS_BAWAH=1_000_000_000_000`, `MS_ATAS=100_000_000_000_000`. `sidik_kode()` mencap dua
berkas: `gerbang_1m.py` + `resample.py` (`66a4b177`).
`rentang = (unik[-1]-unik[0]) // MS_MENIT + 1`;
`menit_hilang_dalam_rentang = rentang - len(unik)` — dihitung **dari rentang yang ada di
berkas**, bukan dari panjang bulan kalender. Rumus itu **DISALIN**, bukan diimpor dari
`diagnosa_kc6.celah_menit` (aturan 10); penjaganya `tests/test_gerbang_1m.py`. Docstring
mengaku nilainya **dapat negatif** dan sengaja tidak ditambal.

**TEMUAN STRUKTURAL YANG MENGIKAT:** modul ini **pustaka murni** — tanpa `KELUARAN`,
tanpa `jalankan`/`main`, **tidak menulis laporan apa pun**, tidak menyentuh jaringan.
**Maka pertanyaan poros tidak dapat dijawab dari keluaran gerbang; ia harus lewat
laporan modul pemanggil.** Ditemukan **sebelum** ramalan R-316 dikunci.

### `silang_funding` V2 (tidak berubah dari v16)

Blob **`b61fe8b3bcabbfce435dd5e5f78fc367f6bef617`**, `waktu_utc`
**2026-07-29T08:17:55Z**, **dibaca 54%**.

`penyebut_kehidupan` **19.586** · `cacah_baris_dengan_medan` **19.586** ·
`bulan_klines_funding` **19.598** · `cacah_lubang_funding` **880** ·
`cacah_lubang_tak_dikenal` **3** · `cacah_mati` **1.401** (kohort **456** + luar kohort
**945**; luar kohort berlubang **386**, berfunding **559**; bagian **0,4085**) ·
`cacah_hidup_tanpa_funding` **33** · `sebaran_bentuk_semua_lubang` 45/826/0/6 = **877** ·
`bentuk_terbitan_funding` 48/826/6 = **880** · seluruh `selisih_*` **0** · `kendali_sah`
**true** · `sidik_seragam` **true** · `laporan_hilang` **[]** · `cacah_simbol_ada_lubang`
**122**.

**`tabel_silang`:** HIDUP **18.054 / 33** · MATI **559 / 842** · SEPI **96 / 2** ·
TAK_TERUKUR **0 / 0**; jembatan 33 + 842 + 2 + 0 = **877**, + **3** = **880**.

**Ketiga lubang tak dikenal, semuanya BNXUSDT:** **2022-04**, **2022-06**, **2022-08**;
`bulan_klines_pertama` **2022-05**, terakhir **2026-06**, `cacah_bulan_klines_simbol`
**48**. **Sebabnya BELUM DIUKUR dan DILARANG DIKLAIM.**

`cacah_hidup_tanpa_funding` **33**, seluruhnya kelas AWAL: BNXUSDT **7** · ICPUSDT
**13** · JUPUSDT **1** · QTUMUSDT **1** · TLMUSDT **11**.

**Sidik:** `sidik_kode` **`8a9b859c…3231b1`** · `sidik_data_funding` **`2c9fbd1b…608d24`** ·
**`sidik_kode_funding`** **`d38548236f03314eaa648f64f73be5af2f682207be750a2c2fa413fad581513a`** ·
`sidik_kode_laporan` **`24b6bb26…c3e8c595`**.

### Lubang tengah — poros TUNTAS (tidak berubah)

Blob **`39cd1caacedc4d49ba23c91c80f553bb9fb135a6`**, 11.014 B, `versi_lubang_tengah`
**2**, `versi_funding` **6**. `cacah_lubang_tengah` **6** · seluruh selisih **0** ·
sebaran {HIDUP 0, MATI 6}. **BTCSTUSDT 2022-01** (rentetan 1) dan **LITUSDT
2025-07..2025-11** (rentetan 5). Keduanya berklines **64 bulan**. **Tidak satu pun
berbulan `2022-05` atau `2024-05`.** H-A011 MENANG (LITUSDT 2026-01..2026-06 keenamnya
HIDUP); H-A010 MENANG 5–0.

### Karantina, terukur penuh (tidak berubah)

Σ `baris_karantina` **516.135** atas **12** parquet, dari delapan
`reports/pulihkan_pecahan_<i>.json` (ref `a2c4b83c`, `pulihkan` VERSI 2, `run_id_sumber`
**30396803601**). Pecahan 2 dan 5 `karantina: null` dan melaporkan
`definisi_dapat_dibedakan` **false** — **aturan 46 terbukti bekerja**. Sidik kode
seragam `76c27e3c…62d700`; manifes seragam `237ccf42…ba601`. Sebaran 42.585–131.760 per
tar; rata **43.011** boleh dikutip sebagai turunan, **bukan bukti**. Manifes
**20.533.802 B**.

### Modul dan laporan lain (tetap berlaku)

- **`selisih_lilin` V1:** `cacah_baris` **19586** · `cacah_berselisih` **0** · dua jalur
  bertemu di **839.325.999** · `selisih_terhadap_warisan` **−516135** · kode keluar alur
  modul **2** (dirancang).
- **`sisa_defisit` V1:** penyebut kerja **17.398** · `cacah_berdefisit` **114** (0,66%) ·
  `bagian_teratas` **0,4087** · `defisit_terbesar` **42.510** = **TLMUSDT 2023-03**,
  HIDUP, 2.130 dari 44.640 lilin (**95,2% kosong**) · pasangan `2022-05`: ANCUSDT
  **26.959** dan LUNAUSDT **26.950** (dasar H-A021; kalimat sebab **DILARANG**).
- **`keterisian_lilin` V1:** lilin LANGSUNG **839.325.999** · MATI penuh **1.392**, tak
  penuh **9** · defisit semesta **18.143.601** (**17.335.439** = 95,5% di bulan pertama;
  **808.162** bukan-pertama, bagian **0,0445**) · bulan pertama rata terisi **≈49,7%** ·
  harga TIDAK tersimpan (**14** medan).
- **`bulan_pertama` V1:** 37 dari 38 baris HIDUP-kecil adalah bulan pertama (0,973684);
  satu-satunya yang bukan **TLMUSDT 2023-03**; nisbah rata byte **0,527179**.
- **`irisan_byte` V1:** zona 22.440–97.634 byte berisi **38 HIDUP dan 0 MATI**; total
  byte **32.706.262.375**.
- **`lubang_tebing` V1:** `mati_dulu` **40** (0.339) · `serempak` **78** · `lubang_dulu`
  **0**; tebing `2025-07` menguasai **39** dari 40, satu-satunya bukan-tebing
  **BTCSTUSDT** (KC-47); **122** dari 787 simbol pernah berlubang funding.
- **`funding.py` V6** mencacah **87** simbol "funding tanpa klines" atas **787** simbol
  (**11,05%** TURUNAN; KC-52 belum didamaikan).

### Belum diukur, urut prioritas resmi

1. **BNXUSDT — identitas bulan.** **[v17] Pertanyaannya BERUBAH BENTUK oleh R-316:**
   bukan lagi "mengapa dua bulan hilang", melainkan **"bulan mana saja yang dimiliki
   BNXUSDT pada semesta 1m (51), dan mana yang tidak sampai ke penyebut (48)"**. Bahan
   calon: `reports/semesta_rentang.json` (110.662 B). **`kehidupan_arsip_*.json` DICORET
   dari daftar bahan** — mustahil dibaca utuh.
2. **Sebab kekosongan TLMUSDT 2023-03** (2.130 dari 44.640 lilin, 95,2% kosong, HIDUP).
3. **Tebing funding `2025-07`** (39 simbol) dan **BTCSTUSDT** — keserian dengan LITUSDT
   **BELUM diukur** dan **DILARANG diklaim**.
4. **Identitas dua belas simbol-bulan karantina** — menuntut **modul CI**. **Bukan
   kandidat murah.**
5. Sisanya: selisih 40−38 `diagnosa_kc15`; bentangan 38 kohort; H-A016; `mati_tersisip`
   atas 19.586; **`ukur_baris` V6**; R-7/19/20/28/36/37 dan R-199; R-236..R-247;
   taksonomi lubang tiga kelas; **bagian `baris_mati` yang belum terbaca**.

**Prasyarat klasifikasi — BELUM SATU PUN DIBAYAR.** Serapan funding **matang sebagai
pembukuan, belum matang sebagai landasan fitur**: (1) ADR-A003 belum ada; (2) keanggotaan
penyebut belum dipahami — **R-316 memperburuknya** dengan angka ketiga (**51**);
(3) `baris_mati` terpotong 54%; (4) kelas positif **33** dari lima simbol (KC-47);
(5) 787 lawan 787 belum didamaikan (KC-52); (6) taksonomi lubang masih **BENTUK, bukan
MEKANISME**.

## Penomoran berikutnya

Aturan resmi **1–81, 83, 84, 85, 86 (a) dan (b), 87** · usulan **77**, **78**, **82**,
**88**, **89** · **aturan berikutnya yang bebas 90** · KC resmi sampai **KC-55** (KC-16
kosong selamanya) · **KC berikutnya KC-56** · Hipotesis: H-A016 (belum diuji), H-A017
(dilemahkan R-306), H-A018 (tafsir dibatasi), H-A019 (DITERIMA TERBATAS), **H-A020 dan
H-A021 (uji MUSTAHIL)**, H-A022 (TERBUKTI), H-A011 (TERBUKTI, larangan generalisasi),
**H-A023 (DIUSULKAN — 51 − 48 = 3 dan `cacah_lubang_tak_dikenal` = 3 menunjuk himpunan
yang sama; BELUM diregistrasi, TIDAK diskor)** · Hipotesis berikutnya **H-A024** ·
Jurnal berikutnya **148** · `STATE.md` berikutnya **v59** · EKOR berikutnya **v18** ·
**UKUR berikutnya v17 (utang hidup, tertinggal satu versi)** · PROMPT berikutnya **v55
(belum didorong)** · ADR berikutnya **A022** · Ramalan berikutnya **R-317** · papan skor
**321**.

**Syarat praregistrasi R-317 — DUA BELAS syarat kumulatif** (naik dari sebelas): aturan
**79** (di `journal/**`, sebelum bahan dibuka) · **83** · **84** · **85** · **86 (a) dan
(b)**, dengan penyebutan bahwa daftar `reports/` baru terbaca **76%** · **87** ·
pemeriksaan **kebebasan medan terhadap kode**, tertulis, sebelum pita dikunci ·
**KC-50** · **KC-52** · **KC-53** · **KC-54** (definisi tiap medan **disalin** ke
praregistrasi; bila definisi tak ditemukan, **syarat gugur tersurat WAJIB**) · **KC-55**
(pita menutup **ketiga sisi**, atau alasan tertulis mengapa satu sisi mustahil) · aturan
**66**. Semangat **usulan 88** dan **usulan 89** ditaati sukarela.
