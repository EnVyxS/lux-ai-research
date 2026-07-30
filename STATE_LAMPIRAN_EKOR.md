# STATE lampiran EKOR — bagian 2 dari STATE (v16, milik STATE v57)

**Mengapa berkas ini ada.** Dua push `STATE.md` berturut terpotong (v41, v42);
pemecahan ke tiga berkas berlaku sejak v43 (KC-42). Pembagian yang berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, 83, 84, 85, 86, **87**;
   KC-1..**KC-54**.
2. **`STATE_LAMPIRAN_EKOR.md`** (berkas ini, v16) — bagian 2: papan skor, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** — bagian 3: pengukuran, modul, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) dan **`PROMPT_KELANJUTAN.md`**
   (blob `35beed44`) — **arsip; BUKAN sumber** (ADR-A018 kep. 9).

Dasar v16: EKOR v15 (blob **`e3fd04c267b702b308e50110b5b7f697b6bbf80d`**, commit
**`94c7d9da8babdf586ae3f821a13781321a7fd40d`**), **dibaca UTUH pada giliran yang sama
sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43).

## KESERASIAN VERSI — dibaca apa adanya, termasuk yang belum serasi

Saat berkas ini didorong:

- `STATE.md` **v57** — blob **`a542b4b12c556fa0a0180ccdbc09bc3d620d12a1`**, commit
  **`ebe6f373b585bca00ac68c0f8bde9f32c97938ac`**, dibaca ulang UTUH pada giliran yang
  sama ia didorong. **SERASI** dengan berkas ini.
- `STATE_LAMPIRAN_EKOR.md` **v16** — berkas ini.
- `STATE_LAMPIRAN_UKUR.md` masih **v15** — blob
  **`0768d497812e6e39269ebc74cca75ee0fb89fe25`**, commit
  **`d551f4712aa8719de87188ed4a33dd89914a20cb`**. **TERTINGGAL SATU VERSI.** Kepalanya
  berbunyi "milik STATE v56". Ia **tidak memuat**: R-315, ADR-A021, KC-54, aturan 87
  resmi, usulan aturan 88, pencabutan bacaan `lubang_tak_dikenal`, tabel tiga lubang tak
  dikenal, jembatan 877 + 3 = 880, `sidik_kode_funding` baru, papan skor 318, aturan 38
  ke-54 dan ke-55, serta butir 14 dan 15 daftar kesalahan dokumen. **Sampai UKUR v16
  naik, sumber sah untuk seluruh butir itu adalah `STATE.md` v57, berkas ini, ADR-A021,
  dan jurnal 144–145** — bukan UKUR v15.

**Satu berkas per push tetap MENGIKAT** (KC-42, KC-43).

**Tentang push berkas ini:** ia di akar repo sehingga menyalakan `ci.yml`. Tidak satu
pun `tests/**` berubah, jadi cacah uji tetap **1377** — ramalan deterministik, **MUDAH**,
TIDAK diskor, TIDAK menambah beruntun aturan 57. **Laporannya WAJIB dibaca sebelum push
akar berikutnya** (pemakaian aturan 38 **ke-56**), atau ia hangus seperti run
`30547842823`.

## KESALAHAN DOKUMEN SENDIRI — kini LIMA BELAS, keduanya yang baru LUNAS

Daftar ini disalin dari STATE v57 dan berlaku identik di ketiga bagian. Sebab tetap
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
| 8 | STATE v53 aturan 45 | "empat push terakhir" lalu mendaftar ENAM | "enam push terakhir" | LUNAS di STATE v54 |
| 9 | STATE v53 aturan 52 | pembacaan ulang "tidak menangkap satu pun" | **satu dari delapan** | LUNAS di STATE v54 |
| 10 | jurnal 138 §5 butir 2 | "maka **839.842.134 yang keliru**" | kesimpulan **tidak sah dari premisnya**; kedua angka benar | LUNAS di jurnal 140 |
| 11 | jurnal 141 §6 | tuduhan atas EKOR v13 **dan ADR-A019** | tuduhan **terlalu luas**; diadili dari sumber | LUNAS di EKOR v14 |
| 12 | ADR-A019 kep. 9 | poros identitas 12 karantina disebut **"termurah"**; gugus lubang tengah dilabeli `2022-05`/`2024-05` | manifes **20.533.802 B**; bulan sebenarnya **BTCSTUSDT 2022-01** dan **LITUSDT 2025-07..2025-11** | LUNAS di ADR-A020 kep. 8 |
| 13 | jurnal 142 §4 | angka **880 / 877 / 3** diumumkan sebagai temuan baru | ketiganya **sudah tertulis di STATE v55**; yang baru hanya **letak** selisih 3 di kelas AWAL | LUNAS di STATE v56 |
| **14** | **STATE v56, keserasian nomor 2** | blob EKOR v14 ditulis berbelit: "blob `a722ec63…` salah; blob yang benar `5d481f9b…` (commit `a722ec63`)" | **commit tertukar dengan blob lalu dikoreksi di tempat**, bukan ditulis bersih sejak awal | **LUNAS di STATE v57** |
| **15** | **ringkasan giliran sebelum jurnal 144** | nama berkas jurnal ditulis `journal/2026-07-31-144.md` | konvensi repo memakai **tanggal UTC**; yang benar **`journal/2026-07-30-144.md`** | **LUNAS di STATE v57** |

**Aturan yang dipegang sejak butir 14:** blob dan commit ditulis pada kolom yang
berbeda; nilai keliru **ditulis ulang bersih**, bukan dibantah di tempat.

**Kelas butir 15:** sama dengan **KC-54** — label yang terdengar masuk akal atas medan
yang benar. Zona waktu adalah medan; namanya bukan definisinya.

### Butir 13 — bentuk halus KC-19, dan mengapa ia layak masuk daftar

Jurnal 142 §4 menyajikan irisan **880 lubang funding semesta lawan 877 di dalam
penyebut, selisih 3 tak dikenal** sebagai temuan giliran itu. Pembacaan utuh STATE v55
menunjukkan bagian "Angka semesta yang mengikat" **sudah memuat ketiga angka itu**.
Maka yang benar-benar baru hanya satu hal: **seluruh selisih 3 duduk di kelas AWAL**
(48 − 45 = 3; ekor 826 − 826 = 0; tengah 6 − 6 = 0).

> Ini kelas KC-19 dalam bentuk halus: mengumumkan sebagai baru apa yang sudah tertulis
> di dokumen sendiri.

### Batas kekuatan aturan 52 — rumusan yang berlaku

> Pembacaan ulang **dokumen sendiri** lemah terhadap penalaran cacat: ia membaca
> kalimat yang sudah diyakini benar. Pembacaan **kode** kuat terhadapnya: kode
> menyatakan identitas yang tidak dapat ditawar.

**[v16] Bukti ketiga, dan ia yang paling tajam:** R-315 butir 2 kalah karena
praregistrasinya disusun dari **nama medan**, sementara **blok `definisi` dan
`catatan_penyebut` di laporan itu sendiri** akan membunuhnya sebelum ditulis. Yang
gagal bukan pembacaan dokumen sendiri, melainkan **pembacaan bahan yang sudah tersedia
dan tidak dibuka**. **DILARANG** menulis bahwa aturan 52 menjaga mutu penalaran **atas
dokumen**.

## KC-43..KC-54 (teks lengkap KC-43..KC-47 di STATE v47, KC-49 di v48, KC-50 di v50, KC-51 di v52, KC-52 di v54, KC-53 di v56, **KC-54 di v57**)

- **KC-43** — tanda tangan fungsi dari INGATAN. Penangkal: baca modul yang diimpor
  UTUH pada giliran yang sama.
- **KC-44** — semua laporan di-commit satu langkah.
- **KC-45 [RESMI v45]** — satuan "bulan tanpa funding" vs "bulan MATI" dicampur.
- **KC-46 [RESMI v45]** — lubang bentuk AWAL dibaca sebagai "funding berhenti".
- **KC-47 [RESMI v46]** — satu peristiwa menyamar sebagai banyak pengamatan bebas.
  Kasus kuat: TUJUH dari sembilan baris MATI tak penuh R-310 berbulan `2024-05` dalam
  jendela **9 lilin**. Terpicu KUAT pada H-A011 (LITUSDT 2026-01..2026-06: satu simbol,
  satu rentetan). **[v16] Terpicu lagi pada R-315:** ketiga lubang tak dikenal milik
  **satu simbol** (BNXUSDT) — itulah isi syarat gugur (e).
- **KC-48 [RESMI v47]** — ambang absolut pada besaran yang sebarannya belum diukur.
- **KC-49 [RESMI v8 lampiran ini]** — pita dikunci tanpa aritmetika implikasi.
  Penangkalnya berlaku sebagai aturan 83. **[v16] Ditaati pada R-315 butir 1:** ruang
  jawaban ditulis tersurat sebagai **{1, 2, 3}** sebelum pita dikunci.
- **KC-50 [RESMI di STATE v50]** — agregat lewat jalan memutar. **Cacat kelas ini tidak
  menghasilkan galat; ia menghasilkan kesunyian.**
- **KC-51 [RESMI v52]** — bias taksiran pemusatan. Empat kejadian berturut tanpa
  pembalikan arah: R-308 butir 2 (10..300 → **2**); R-310 butir 2 (0,02..0,25 →
  **0,0445**); R-311 butir 1 (200..12.000 → **114**, faktor **26,3**); R-311 butir 2
  (0,02..0,45 → **0,4087**). **[v16] TIDAK mendapat kejadian kelima.** R-315 butir 1
  memakai titik tunggal **1** pada ruang {1, 2, 3} dan menang di **lantai aritmetis** —
  **DILARANG** dibaca sebagai kalibrasi membaik.
- **KC-52 [RESMI di STATE v54, DITUTUP sebagai teka-teki, TETAP HIDUP sebagai pola]** —
  dua penyebut berbeda diperlakukan sebagai satu: 19.586 lawan 19.598, **880 lawan
  877**, 18.799 lawan 17.398, dan pasangan paling berbahaya **787 simbol klines lawan
  787 simbol funding** (sama besar, tanpa selisih yang menyalakan alarm).
  **[v16] Pola 880/877 kini TUTUP secara pembukuan** — 33 + 842 + 2 = 877, + 3 = 880 —
  tetapi penutupan itu **pasca-hoc** dan **DILARANG** masuk lajur skor (ADR-A021 kep. 8).
- **KC-53 [RESMI di ADR-A020 kep. 3]** — nol pada sebuah medan dibaca sebagai ketiadaan
  fenomena. Kasus asal: `cacah_simbol_bangkit_dapat_diuji` = 0. **Mengutipnya sebagai
  bukti ketiadaan kebangkitan DILARANG.**
- **KC-54 [RESMI di ADR-A021 kep. 3, diserap STATE v57]** — **nama medan dibaca sebagai
  definisi medan.** Kasus asal: `lubang_tak_dikenal` dibaca sebagai pernyataan tentang
  **posisi waktu** lubang, padahal medan itu hanya menyatakan **kegagalan pasangan**
  terhadap penyebut **19.586**. **Penangkal wajib:** sebelum meramalkan apa pun atas
  sebuah medan, **salin dulu definisi medan itu dari laporan atau dari kode ke dalam
  praregistrasi**. Kerabat: KC-53, KC-30, KC-31, KC-36, KC-41, Koreksi 11 UKUR v15,
  butir 15 daftar kesalahan dokumen.
- **KC berikutnya yang bebas: KC-55.**

## Papan skor prediksi — lengkap R-300..R-315 (R-199..R-299 di v4, blob `67dda29e`)

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
| R-311 | (1) cacah baris bukan-pertama bukan-MATI berdefisit, dari **17.398**, dalam **200 .. 12.000**; (2) bagian sisa 712.925 yang ditanggung SEPULUH teratas, dalam **0,02 .. 0,45**; (3) sepuluh invarian nol + tiga kendali + penggugur + kode 0 + CI | **SEPARUH** — butir 1 **KALAH** (**114**, lantai aritmetis 16); butir 2 **MENANG** (**0,4087**, tipis ke tepi ATAS); butir 3 MUDAH |
| R-312 | (1) cacah baris berselisih `cacah_lilin` vs `cacah_lilin_terbaca`, dari 19.586, dalam **12 .. 120**; (2) bagian selisih yang ditanggung baris teratas dalam **0,50 .. 0,865**; (3) penggugur + kendali + kode 0 + CI | **TIDAK TERADJUDIKASI** — `cacah_berselisih` **0**, penyebut butir 2 NOL (aturan 41). Butir 2 **mustahil dimenangkan secara struktural**. |
| R-313 | (1) Σ `baris_karantina` atas delapan `reports/pulihkan_pecahan_<i>.json` = **516.135**; (2) Σ parquet karantina = **12** | **TEPAT (2/2)** — keduanya selisih **0**, dengan **cacat aturan 79 melekat permanen** |
| R-314 | (1) `cacah_per_simbol_funding` ∈ **[747, 827]**; (2) `h_a010_cacah_simbol_berisi` = **0**; (3) `h_a011_cacah_hidup` = **0** | **2 TEPAT / 1 MELESET** — **787** TEPAT · **0** TEPAT · **6** **MELESET**. Butir 2 dan 3 **TURUNAN dari docstring**. |
| **R-315** | (1) cacah simbol berbeda pemilik ketiga `lubang_tak_dikenal` = **1**; (2) **ketiga** lubang berbulan lebih awal daripada `bulan_klines_pertama`; (3) MUDAH: laporan terbaca, `sidik_kode` cocok, penyebut 19.586, lubang semesta 880 | **1 TEPAT / 1 MELESET** — butir 1 **1** (BNXUSDT) **TEPAT**; butir 2 **1 dari 3** **MELESET**; butir 3 terpenuhi, **tidak masuk lajur**. **Syarat gugur (e) MENYALA.** |

**Total R-1..R-315** (dihitung TANGAN dari rincian v15, aturan 21):

- TEPAT **221**
- MELESET **59**
- SEPARUH **22**
- TIDAK TERADJUDIKASI **9**
- MENUNGGU **7** (R-7, R-19, R-20, R-28, R-36, R-37, R-199)

221 + 59 = 280; 280 + 22 = 302; 302 + 9 = 311; 311 + 7 = **318** ✅ Nomor terpakai
R-1..R-315. N_percobaan = 0. **ADJUDIKASI RISET TETAP TERKUNCI.**
**Pertambahan dari 316:** TEPAT **+1**, MELESET **+1**, seluruhnya dari **R-315**;
lajur lain **tidak bergerak**.

**[v16] Lajur MENUNGGU sengaja TIDAK bergerak.** R-315 **tidak pernah sempat tercatat
menunggu**: praregistrasinya (jurnal 144, commit `1146b96a`) dan adjudikasinya (jurnal
145, commit `526e41e8`) berjarak **satu giliran**. Ketujuh anggota lajur MENUNGGU tetap
R-7, R-19, R-20, R-28, R-36, R-37, R-199.

**[v16] PAPAN SKOR 318 KINI SAH.** STATE v57 mencatatnya sebagai penerapan aturan 21;
**pengesahan lajur terjadi di berkas ini**, dan tidak di tempat lain.

**Kolom terpisah — DI LUAR lajur papan skor:** **R-229 TEPAT** dan **R-230 MELESET**
(ADR-A020 kep. 5). Keduanya **TIDAK dimasukkan ke lajur** karena pemeriksaan berurutan
R-224..R-235 belum dilakukan. **R-228 tetap BELUM diadjudikasi.**

**Nisbah papan skor, dihitung tangan dan disebut apa adanya:** dari 302 ramalan yang
beradjudikasi penuh (221 + 59 + 22), TEPAT **73,2%**, MELESET **19,5%**, SEPARUH
**7,3%**. Angka itu **DILARANG dibaca sebagai mutu ramalan**: sebagian besar butir
ketiga tiap ramalan berlabel MUDAH dan tidak berisiko. **R-312 DILARANG masuk pembilang
maupun penyebut nisbah ini.**

**Utang papan skor:** rincian R-236..R-247 masih di jurnal 92–94; pemeriksaan
R-224..R-235 belum dikerjakan.

### [v16] R-315 — kekalahan yang wajib disebut telanjang

**Diramalkan 3 dari 3; terukur 1 dari 3.** Tidak ada pembungkus untuk itu.

BNXUSDT **2022-06** dan **2022-08** duduk **sesudah** `bulan_klines_pertama` **2022-05**
— yakni **di dalam** rentang klines simbolnya sendiri. Yang runtuh bukan satu butir
ramalan, melainkan **bacaan yang dipakai tiga dokumen berturut** (STATE v55, STATE v56,
UKUR v15): bahwa lubang tak dikenal berarti "bulan sebelum simbol lahir". Bacaan itu
**DICABUT** (ADR-A021 kep. 2). Definisi yang benar, dari `catatan_penyebut` laporan
sendiri: lubang funding yang **jatuh di luar penyebut 19.586** — **tanpa satu kata pun
tentang arah waktu**.

**Vonis FINAL: 1 TEPAT / 1 MELESET / 1 tidak diskor. DILARANG ditulis ulang sebagai
SEPARUH di dokumen mana pun** (ADR-A021 kep. 1).

**Pengecilan kemenangan butir 1, ditulis sendiri (aturan 87 — kini RESMI):** cacah **3**
sudah tercatat pada konstanta `LUBANG_TAK_DIKENAL_TERCATAT` di kode. Yang benar-benar
diramalkan hanyalah "ketiga lubang itu satu pemilik" — **kemenangan sempit, satu bit**.
Pemeriksaan kebebasan medan yang dijanjikan di jurnal 144 **ditepati** di jurnal 145:
konstanta itu memuat **cacah**, bukan identitas maupun arah waktu, sehingga butir 1
tetap **MURNI**.

**Syarat gugur (e) MENYALA** — ketiganya milik BNXUSDT, simbol yang sudah lebih dulu
dikenal berlubang AWAL dan bukan-AWAL sekaligus. Sesuai yang dikunci **di muka**,
**kesamaan itu DILARANG dibaca sebagai konfirmasi apa pun**.

### [v16] Aturan 87 RESMI, aturan 88 DIUSULKAN

> **Aturan 87 (RESMI, ADR-A021 kep. 4).** Butir ramalan yang turun dari docstring,
> konstanta, atau penalaran pihak lain — termasuk modul repo ini sendiri — **WAJIB**
> ditandai **TURUNAN** pada praregistrasi, dan pada adjudikasi kemenangannya **WAJIB**
> diperkecil sendiri secara tertulis. Butir yang tidak dapat dibuktikan bebas dari
> sumber itu **diperlakukan sebagai TURUNAN**.

Kejadian pertama R-314 (butir 2 dan 3 dari docstring `lubang_tengah.py`); ADR-A020
kep. 7 menolak meresmikannya atas satu kejadian. Kejadian kedua R-315, dan kali ini
janjinya **ditepati di muka**. Diresmikan pada kejadian kedua, sesuai ADR-A019 kep. 3.

> **Usulan aturan 88 (BELUM RESMI, ADR-A021 kep. 5).** Ramalan bahwa **semua** anggota
> sebuah himpunan berbagi satu sifat **WAJIB** disertai **mekanisme tertulis** yang
> memaksa keseragaman itu. Bila yang tersedia hanya nama medan, definisi longgar, atau
> kesan pola, ramalan **WAJIB** ditulis sebagai **sebaran** ("berapa dari berapa",
> dengan pita) alih-alih biner.

Baru **satu** kejadian (R-315 butir 2). **Catatan kejujuran yang melekat:** aturan 88
lahir **sesudah** kekalahan. Ia **utang yang dibayar, bukan laba**, dan **DILARANG**
diklaim sebagai kemenangan metodologis.

### [v16] Aturan 85 mendapat adjudikasi keduanya

Pada R-315 butir 1, ruang jawaban seluruhnya **{1, 2, 3}**, lantai aritmetisnya **1**,
dan **1 itulah yang dipilih** dengan alasan tertulis di muka. Ia mendarat **TEPAT**.
**Yang DIIZINKAN:** aturan 85 kini punya **dua** adjudikasi, keduanya menang. **Yang
DILARANG:** menyebutnya **teruji**, **bekerja**, atau **terbukti** — dua titik data
bukan riwayat, dan kemenangan tepi **DILARANG** dibaca sebagai kalibrasi membaik
(KC-51).

### Lima larangan permanen yang menempel pada R-312 (tidak berubah di v16)

1. **DILARANG** mengatakan pita butir 1 (12..120) "tidak terbantah". Ia tidak diuji.
2. **DILARANG** mengatakan kalibrasi membaik atau memburuk karena R-312.
3. **DILARANG** menghitungnya di pembilang maupun penyebut nisbah kemenangan.
4. **DILARANG** menghidupkannya kembali dengan alasan penjelasannya kini ditemukan.
5. Angka **12** di R-313 adalah cacah **parquet karantina** — arti berbeda dari 12 di
   R-312 butir 1. **Kesamaan itu DILARANG dibaca sebagai konfirmasi apa pun.**

### [v16] Larangan yang lahir bersama STATE v57 dan ADR-A021

1. **DILARANG** membaca `lubang_tak_dikenal` sebagai "bulan sebelum simbol lahir" atau
   sebagai pernyataan arah waktu apa pun.
2. **DILARANG** menulis vonis R-315 sebagai **SEPARUH**.
3. **DILARANG** membaca kemunculan BNXUSDT sebagai konfirmasi fakta lama mana pun
   (syarat gugur (e) menyala).
4. **DILARANG** mengklaim **sebab** mengapa BNXUSDT 2022-06 dan 2022-08 tidak lolos
   gerbang. Belum diukur (aturan 21).
5. **DILARANG** mengklaim cacah total baris `baris_mati` `silang_funding.json` sebagai
   terukur — hasil alat terpotong pada **54%**. Selisih TLMUSDT `cacah_lubang_simbol`
   **20** lawan **19** baris terlihat adalah **utang bacaan, bukan cacat laporan**
   (ADR-A021 kep. 9).
6. **DILARANG** memasukkan keempat kecocokan pasca-hoc jurnal 145 §7 ke lajur skor
   (877 + 3 = 880; 48 − 45 = 3 bernama; 50 − 48 = 2; larik 33 baris) — ADR-A021 kep. 8.
7. **DILARANG** mengklaim aturan 88 sebagai kemenangan metodologis.

Enam larangan yang lahir bersama STATE v56 tetap berlaku penuh: KC-53 atas
`cacah_simbol_bangkit_dapat_diuji`; "termurah" atas poros karantina; lubang tengah di
`2022-05`/`2024-05`; 787 funding lawan 787 klines; aturan 85 "teruji"; generalisasi
kebangkitan LITUSDT.

## Catatan kejujuran [v16]

1. **Kekalahan disebut telanjang, dengan angka.** R-315 butir 2: **diramalkan 3 dari 3,
   terukur 1 dari 3**. Kekalahan itu **paling mahal** dari semua yang tercatat belakangan,
   bukan karena bobot lajurnya (satu butir), melainkan karena ia membatalkan **bacaan
   yang sudah dipakai tiga dokumen**.
2. **Bahan penangkalnya ada di dalam berkas yang sama dan tidak dibuka.**
   `silang_funding.json` memuat blok `definisi` dan `catatan_penyebut`. Praregistrasi
   disusun dari **ingatan atas nama medan**. Ini biaya melanggar "ukur, jangan menduga"
   pada tahap **penyusunan ramalan**, bukan pada tahap pengukuran. **KC-54 lahir dari
   sini.**
3. **Aturan 79 DITAATI SEPENUHNYA untuk kedua kalinya berturut.** Praregistrasi R-315
   ditulis di `journal/2026-07-30-144.md` (commit `1146b96a`) pada giliran yang berbeda
   dari adjudikasinya (jurnal 145, commit `526e41e8`), dan **sebelum** laporan dibuka.
   Saksinya **git**, bukan riwayat percakapan. **DILARANG** menyebut aturan 79 lemah,
   longgar, atau opsional.
4. **Kemenangan yang diperkecil sendiri, bukan dibesarkan.** Butir 1 menang di **lantai
   aritmetis** ruang {1, 2, 3} — peluang telanjangnya besar, dan itu ditulis di sini,
   bukan disembunyikan.
5. **Empat kecocokan pasca-hoc TIDAK diskor.** 33 + 842 + 2 = 877, + 3 = 880; 48 − 45 = 3
   kini bernama; rentang 2022-05..2026-06 = 50 bulan lawan `cacah_bulan_klines_simbol`
   **48**, selisih **2** tepat pada 2022-06 dan 2022-08; larik `baris_hidup_tanpa_funding`
   33 baris. Keempatnya **ditemukan sesudah** bahan dibuka. **Sebabnya belum diukur,
   dilarang diklaim** (aturan 21).
6. **Aturan 57 beruntun 4 dari 4, dan tidak bertambah.** Tidak ada berkas uji baru sejak
   trio `c1dc0009`.
7. **Aturan 36 mendapat kasus ketiga, dan ia pembukuan, bukan pengukuran baru:** dua
   jalur dalam satu laporan bertemu di **880**. Kasus terkuat tetap yang pertama
   (`selisih_lilin` dan `pulihkan` bertemu di **839.325.999**).
8. **Aturan 52 ditaati enam belas kali berturut hingga ADR-A021**, **tujuh belas** dengan
   STATE v57, **delapan belas** dengan berkas ini. Utang bacanya bertambah satu yang
   tegas: **bagian tengah larik `baris_mati` `silang_funding.json`** — laporan yang
   **tidak terbaca utuh** (terpotong 54%).
9. **`PROMPT_KELANJUTAN.md` tetap belum diberi kepala "ARSIP — BUKAN SUMBER"** dan
   `PROMPT.md` **v55 belum didorong**. Sampai itu dikerjakan, satu-satunya penjaga adalah
   larangan tertulis di STATE v52–v57 dan di berkas ini.
10. **Pemeriksaan silang yang menutup tanpa sisa** (terbitan, TIDAK diskor):
    18.799 − 1.401 = **17.398**; 98 − 80 = **18**; 769 + 18 = **787**;
    **19.586 + 12 = 19.598**; **839.325.999 + 516.135 = 839.842.134**;
    **880 − 877 = 3**, seluruhnya di kelas AWAL (48 − 45); **6 − 6 = 0** untuk kelas
    tengah; `selisih_lubang_tengah` **0**; **[v16]** `tabel_silang` kolom kehilangan
    funding **33 + 842 + 2 + 0 = 877**.

**Kesalahan proses [v16].** Tidak ada kegagalan panggilan alat baru. Yang lama tetap
tercatat: pada giliran push STATE v55, `push_files` **ditolak** karena bungkus
`toolName`/`toolArguments` tidak dipakai — **bukan galat alat, melainkan kesalahan
bentuk panggilan**; tidak ada yang tertulis dan tip tidak bergerak. Kerugian lain tetap
berasal dari urutan kerja: laporan CI run `30547842823` hangus, dan blob laporan ke-38
tidak dapat dipulihkan. **[v16] Kerugian baru berbentuk lain:** `silang_funding.json`
terlalu besar untuk satu pembacaan alat — **54%** yang terbaca cukup untuk mengadili
R-315, tetapi cacah `baris_mati` tetap **di luar jangkauan**.

## Jumlah uji

**1377 TERUKUR, kini SEBELAS bacaan berjejak (ke-45..ke-55).**

1. blob **`cdfdee2559201306a49bc9b01f1185d7aa36eebe`**: run **30559145901**, commit
   **`c1dc0009`** (trio `selisih_lilin`), 15:57:01Z, kode 0, `1377 tests collected in 0.58s`.
2. blob **`effb3a46bc20cda5c6c5910ee926aa16c195bb68`**: run **30575123865**, commit
   **`8368ca1f`** (STATE v54), 19:30:52Z, kode 0, `… in 0.54s`.
3. blob **`8cbbd4ce7b85d9e1f217a9cefbdacfb9318dec78`**: run **30576963781**, commit
   **`6642ed68`** (EKOR v13), 19:56:30Z, kode 0, `… in 0.67s`.
4. blob **`8ec97de5af8b528276174f635e3bda9e6cc2d7ef`**: run **30577779309**, commit
   **`2bdd8233`** (UKUR v13), 20:07:50Z, kode 0, `… in 0.62s`.
5. blob **`94d270e7065218f87bd5a26c5113ed8346cf6abf`**: run **30579348728**, commit
   **`cd209f3e`** (STATE v55), 20:29:25Z, kode 0, `… in 0.61s`.
6. blob **`04bfa2ed5fb43f128f8ee2351f41722314685a03`**: run **30580133552**, commit
   **`a722ec63`** (EKOR v14), kode 0, `… in 0.46s` — **tercepat yang pernah tercatat**.
7. blob **`aeb4315ad73806b61f734f9c1d92b27b1ae2727b`**: run **30581703827**, commit
   **`6157586e`** (UKUR v14), 21:02:01Z, kode 0, `… in 0.61s`.
8. blob **`19785af1d96fdc1fabec2dfa9f7c3dbaf60b3708`**: run **30583686515**, commit
   **`019d16ea`** (STATE v56), 21:31:10Z, kode 0, `… in 0.61s`.
9. blob **`5f4282f6`**: run **30584737431**, commit **`94c7d9da`** (EKOR v15), kode 0.
10. blob **`340c3c7f425d49859e6ae659cca38d0ee7770aaa`**: run **30585269231**, commit
    **`d551f471`** (UKUR v15), 21:55:58Z, kode 0, `… in 0.60s`.
11. **[v16]** blob **`8ea8cc463ff58246b363e47458e9355d26a5ea79`**: run **30587658376**,
    commit **`ebe6f373b585bca00ac68c0f8bde9f32c97938ac`** (STATE v57),
    **2026-07-30T22:36:15Z**, kode 0, `1377 tests collected in 0.40s` — **tercepat yang
    pernah tercatat**, menggantikan 0.46s.

Turunan: 1341 + **36** butir `tests/test_selisih_lilin.py` = **1377** ✅ (aturan 21),
terverifikasi dari sumber, bukan dari ingatan.

Riwayat panjang: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 →
984 → 1044 → 1100 → 1168 → 1233 → 1297 → 1341 (enam run) → **1377** (sebelas run berjejak).

Cacah per berkas uji (**milik repo riset ini — bukan repo warisan**):
`test_irisan_byte.py` **68** · `test_bulan_pertama.py` **65** ·
`test_keterisian_lilin.py` **64** · `test_bentangan_kohort.py` V2 **63** (dicacah
TANGAN, `test_01`..`test_63`) · `test_lubang_tebing.py` **60** ·
`test_sebab_bangkit.py` **57** · `test_byte_semesta.py` **56** ·
`test_lubang_awal.py` **48** · `test_tersisip_semesta.py` **47** ·
`test_anatomi_tengah.py` **47** · `test_sisa_defisit.py` **44** (dicacah TANGAN) ·
`test_selisih_lilin.py` **36** (dicacah TANGAN dari sumber) · `test_terhenti.py` V4
**33** · `test_bulan_absen.py` **32** · `test_karantina_semesta.py` **28** ·
`test_silang_settled.py` **24** · `test_ukur_baris.py` **3**.
**`tests/test_lubang_tengah.py` — 56 butir menurut R-228, BELUM DIBACA, karena itu
DILARANG dikutip sebagai cacah terukur.**

**Aturan 57: beruntun 4 dari 4** sesudah putus di 26/27. Hanya push yang menyentuh
`tests/**` yang dihitung.

### ORDINAL ATURAN 38 — buku besar, kini sampai ke-55

**Definisi yang berlaku (ADR-A018 kep. 8):** pemakaian dihitung **hanya** untuk
pembacaan `reports/ci_terakhir.json` yang meninggalkan **jejak tertulis** berupa nomor
run + commit + blob di STATE, lampiran, atau jurnal.

| ke- | CI | run | commit | blob | jejak |
|---|---|---|---|---|---|
| 43 | 1341 | 30550547017 | `1247a5a3` | `fdb7c668` | STATE v53 |
| 44 | 1341 | 30551789395 | `33a4ab37` | `5b16417b` | jurnal 136 |
| 45 | 1377 | 30559145901 | `c1dc0009` | `cdfdee25` | jurnal 137, STATE v54 |
| 46 | 1377 | 30575123865 | `8368ca1f` | `effb3a46` | EKOR v13 |
| 47 | 1377 | 30576963781 | `6642ed68` | `8cbbd4ce` | jurnal 141, STATE v55 |
| 48 | 1377 | 30577779309 | `2bdd8233` | `8ec97de5` | jurnal 141, STATE v55 |
| 49 | 1377 | 30579348728 | `cd209f3e` | `94d270e7` | EKOR v14, STATE v56 |
| 50 | 1377 | 30580133552 | `a722ec63` | `04bfa2ed` | jurnal 142, STATE v56 |
| 51 | 1377 | 30581703827 | `6157586e` | `aeb4315a` | jurnal 142, STATE v56 |
| 52 | 1377 | 30583686515 | `019d16ea` | `19785af1` | EKOR v15 |
| 53 | 1377 | 30584737431 | `94c7d9da` | `5f4282f6` | UKUR v15, STATE v57 |
| 54 | 1377 | 30585269231 | `d551f471` | `340c3c7f425d49859e6ae659cca38d0ee7770aaa` | STATE v57 |
| **55** | **1377** | **30587658376** | **`ebe6f373`** | **`8ea8cc463ff58246b363e47458e9355d26a5ea79`** | **berkas ini** |

**Pemakaian berjalan = ke-lima puluh lima.** Pemakaian ke-55 dibaca
**2026-07-30T22:36:15Z**, kode keluar **0**, atas push **STATE v57** — dibaca **sebelum
tertimpa**, sehingga ramalan "CI tetap 1377" untuk push itu **TERUKUR dan TEPAT**, tetap
**MUDAH**, tetap tidak diskor, tetap tidak menambah beruntun aturan 57.

**[v16] Lima belas pembacaan berturut (ke-42..ke-55) tanpa satu pun laporan hangus** —
sebutan ini dihitung tangan dari tabel di atas ditambah ke-42 yang tercatat di v13.

**Bot CI menambah satu commit di atas tiap push pemicu** — kini **tujuh kali berturut**
(`0fa2b867`, `c139f16a`, `c4a7468e`, `ff89f688`, dan pendahulunya). **Deterministik dari
`ci.yml`; DILARANG dihitung sebagai kemenangan ramalan.**

**Dua cacat tetap disebut apa adanya:** baris ke-**38** (run `30541051907`, CI 1297,
commit `5d7d8b96`) **tanpa blob**, tidak dapat dipulihkan — ordinal ini karena itu sah
**relatif terhadap definisi di atas**, bukan sebagai pencacahan mutlak; dan run
**30547842823** (bot `de2fc03d`) **tidak pernah dibaca**, sudah tertimpa, **DILARANG
dihitung**. Bila jejak pembacaan lain ditemukan di jurnal 133–134, nomor ini **WAJIB
dikoreksi, bukan dipertahankan**.

**Calon aturan** — dua push akar berturut tanpa membaca laporan di antaranya pasti
menghanguskan yang pertama — **tetap DITOLAK diresmikan**: masih **satu** kejadian.

## Utang verifikasi

1-5, 11 menunggu tahap juri. 6-23, 25-29, 31 LUNAS. **Nomor utang BUKAN nomor ramalan
— KC-32.**

24. **AKTIF. LUNAS BARU [v16]:**
    - **`reports/silang_funding.json` dibaca** — blob
      **`b61fe8b3bcabbfce435dd5e5f78fc367f6bef617`**. **TIDAK UTUH:** hasil alat
      terpotong pada **54%**; larik `lubang_tak_dikenal`, `ringkasan`, `definisi`, dan
      `baris_hidup_tanpa_funding` terlihat utuh, **bagian tengah `baris_mati` tidak**.
    - **`journal/2026-07-30-144.md`** — blob `fcc9374529fd91bd1c9a3d43c34b7f24a86d344e`,
      commit `1146b96a`.
    - **`journal/2026-07-30-145.md`** — blob `d9b63433e6693a5e012ed14eec1ecc8e9b740e21`,
      commit `526e41e8`.
    - **`decisions/ADR-A021.md`** — blob `3e756672ca355ea976bf2931d278e37fe9057d0d`,
      commit `2cee14b7`.
    - **`STATE.md` v57** — blob `a542b4b12c556fa0a0180ccdbc09bc3d620d12a1`, commit
      `ebe6f373`.
    - **EKOR v15 dibaca UTUH** pada giliran ini — blob `e3fd04c267b702b308e50110b5b7f697b6bbf80d`.
    - `reports/ci_terakhir.json` (`340c3c7f…`, `8ea8cc46…`) dibaca utuh, blob DICATAT.
    **TETAP BELUM:** `decisions/ADR-A002`, **A004**, **A006**, **A007**, **A008**;
    `.github/workflows/karantina_semesta.yml` (`de40fa4e`); `tests/test_pulihkan.py`
    (`11c43533`); `tests/test_rilis_karantina.py` (`739c8da9`);
    `tests/test_karantina_a006.py` (`a5a3d82f`); `tests/test_lubang_tengah.py`;
    **bagian `baris_mati` `silang_funding.json`**.
30. **AKTIF — UTANG HIDUP**, ADR-A019 kep. 8 MENOLAK menutupnya. Angka **50 / 54 / 45**
    tetap **TURUNAN** dan **DILARANG dikutip sebagai terukur**. Yang sah tetap
    **49 / 53 / 44 / 18** pada ref `3196fd98` dan `8a614567`. **[v16] Tidak ada modul
    baru sejak v15 — utang tidak bertambah, juga tidak berkurang.**
32. **AKTIF — tiga butir "memerlukan verifikasi" `PETA_MODUL.md`** (repo **WARISAN**):
    (a) `enable_hs` tidak ditemukan di `config.py` padahal dipakai `strategy.py`;
    (b) klaim "30 pair dipilih alfabetis"; (c) klaim "kendala mengikat = kapasitas
    margin".
33. **[v16] LUNAS untuk butir 14 dan 15** — keduanya ditulis resmi di STATE v57 dan
    disalin ke berkas ini. Daftar berdiri di **lima belas** butir, **tanpa calon baru**.
34. **AKTIF — `PROMPT_KELANJUTAN.md` belum diberi kepala "ARSIP — BUKAN SUMBER"**, dan
    **`PROMPT.md` v55 belum didorong.**
35. **[v16] LUNAS sebagian** — UKUR v15 sudah naik (commit `d551f471`, blob
    `0768d497…`). **Digantikan utang baru:** UKUR **v16** belum naik; sampai itu, UKUR
    v15 tertinggal satu versi (lihat keserasian di kepala).
36. **AKTIF — identitas dua belas simbol-bulan karantina belum pernah didaftar.**
    Cacah dan barisnya terukur (12 parquet, 516.135 baris), tetapi **nama simbol dan
    bulannya tidak diketahui**. Kalimat apa pun tentang *jenis* instrumen yang
    dikarantina **DILARANG**. Manifes **20.533.802 B** — jalan satu-satunya **modul CI**.
37. **AKTIF — `ukur_baris.py` V6 belum ditulis.** `BERKAS_DIUKUR` masih **21** nama;
    `silang_funding.py` V2 **705 baris**, jarak ke pagar **95**.
38. **AKTIF — R-228 belum diadjudikasi.** Menuntut laporan CI run **30436915256** atau
    berikutnya yang belum pernah dibuka. Cacah 56 butir `test_lubang_tengah.py`
    **DILARANG** dikutip sebagai terukur.
39. **BARU [v16] — bagian `baris_mati` `silang_funding.json` belum terbaca.** Ia bukan
    utang yang dapat dilunasi dengan satu panggilan alat: berkasnya terlalu besar.
    Jalannya **modul yang berjalan di CI** atau **pembacaan berpotong yang dirancang**.
    Sampai itu, **cacah total baris `baris_mati` DILARANG diklaim terukur**.

## Daftar ADR

- **ADR-A001** aturan dasar. DITERIMA.
- **ADR-A002** serapan. Kondisi v3 berlaku; §10 tetap tidak boleh diubah. **BELUM DIBACA UTUH.**
- **ADR-A003** taksonomi rezim. BELUM ADA.
- **ADR-A004** kebijakan KC-6. DITERIMA. **BELUM DIBACA UTUH.**
- **ADR-A005** jenis instrumen. DITERIMA.
- **ADR-A006** karantina + persistensi. DITERIMA, TERVERIFIKASI. **BELUM DIBACA UTUH.**
- **ADR-A007** serapan hibrida. DIUSULKAN, belum diterima. **BELUM DIBACA UTUH.**
- **ADR-A008** akibat KC-18. Keputusan 1–6 DITERIMA. **Keputusan 7 DITANGGUHKAN.**
  **BELUM DIBACA UTUH.**
- **ADR-A009** (`17a594b6`). **DICABUT PENUH oleh ADR-A012.**
- **ADR-A010** (`c4bccf21`) — klaim "kebangkitan tunggal" DICABUT. DITERIMA.
- **ADR-A011** (`645fd5df`) — arah sebab A009 dicabut untuk kelas bangkit. DITERIMA.
- **ADR-A012** (`f9f564d1`) — arah sebab dicabut untuk SELURUH semesta. DITERIMA.
- **ADR-A013** (`8ba4f989`) — (2) dan (4) kini aturan **80** dan **81**. DITERIMA.
- **ADR-A014** (`6d77c2cd`) — byte parquet; (5) melahirkan KC-48. DITERIMA.
- **ADR-A015** (`387d5510`) — delapan keputusan; (5) besar berkas bukan detektor status
  ke arah mana pun — **TIDAK dibalik oleh R-310..R-315 maupun A018–A021**. DITERIMA.
- **ADR-A016** (`209802d7`) — H-A019 diterima TERBATAS; kep. 4 **DIKOREKSI oleh A018
  kep. 6**; **kewajiban adjudikasi pada giliran berbeda** berasal dari sini. DITERIMA.
- **ADR-A017** (`1be570f2`) — sebelas keputusan; kep. 4 TERJAWAB PENUH oleh R-313.
  DITERIMA.
- **ADR-A018** (`3fba599e`) — dua belas keputusan; (8) definisi ordinal aturan 38;
  (9) `PROMPT_KELANJUTAN.md` arsip, **perintah operator menang**; (10) dua cacah
  `tests/`; (11) cacah tangan 49/53/44/18. DITERIMA.
- **ADR-A019** (`9cd7d25e7a61207343e60233887d06b441aa3cbf`, commit `e6007ba5`) —
  sepuluh keputusan; (3) **aturan tidak diresmikan atas satu kejadian**; (8) utang cacah
  tangan aturan 66 ditolak ditutup. **DITERIMA — kep. 9 DIKOREKSI DUA KALI oleh A020
  kep. 8.**
- **ADR-A020** (`200c7e7d737fdfa0b8d689e35482d9ae249b90ee`, commit `d8335be1`) —
  sepuluh keputusan: (1) H-A011 TERBUKTI dengan larangan generalisasi; (2) bacaan nol
  kebangkitan DICABUT; (3) KC-53 DIRESMIKAN; (4) R-314 2 TEPAT / 1 MELESET, papan skor
  **316**, aturan 85 beradjudikasi pertama; (5) R-229/R-230 di kolom terpisah;
  (6) aturan 86 butir (b); (7) aturan 87 **ditolak diresmikan** (satu kejadian);
  (8) dua pencabutan atas A019 kep. 9; (9) urutan poros; (10) penomoran A021. DITERIMA.
- **ADR-A021 — ADA [v16]** (blob **`3e756672ca355ea976bf2931d278e37fe9057d0d`**, commit
  **`2cee14b797ea33d5a4794bba165f159f5ba1efa2`**, dibaca UTUH). **Sepuluh keputusan:**
  (1) **R-315 = 1 TEPAT / 1 MELESET / 1 tidak diskor**, dilarang ditulis SEPARUH;
  (2) **bacaan "lubang tak dikenal = bulan sebelum simbol lahir" DICABUT**;
  (3) **KC-54 DIRESMIKAN**;
  (4) **aturan 87 DIRESMIKAN** atas kejadian kedua;
  (5) **aturan 88 DIUSULKAN**, belum resmi, dengan catatan kejujuran melekat;
  (6) **poros "irisan 880 lawan 877" TUNTAS secara pembukuan** dan dikeluarkan dari
  daftar — yang boleh diklaim hanya **dari mana** selisih 3 berasal, bukan **mengapa**;
  (7) **urutan poros diperbarui** — BNXUSDT 2022-06/2022-08 naik ke peringkat pertama;
  (8) **empat kecocokan pasca-hoc DILARANG masuk lajur skor**;
  (9) **cacah `baris_mati` DILARANG diklaim terukur**; selisih TLMUSDT 20 lawan 19
  adalah **utang bacaan**;
  (10) papan skor **318** dan penomoran **A022** ditetapkan. DITERIMA.
- **ADR-A022 [BELUM ADA]** — calon isinya: hasil poros **BNXUSDT 2022-06 dan 2022-08**
  terhadap gerbang, atau sebab kekosongan **TLMUSDT 2023-03**. **DILARANG disusun pada
  giliran yang sama dengan adjudikasi** (ADR-A016).

## Temuan sampingan

### [v16] `silang_funding` V2 — irisan 880 lawan 877 tertutup secara pembukuan

Sumber: `reports/silang_funding.json`, blob
**`b61fe8b3bcabbfce435dd5e5f78fc367f6bef617`**, `waktu_utc`
**2026-07-29T08:17:55Z**. **Dibaca 54%, bukan utuh.**

**Ringkasan terukur:** `penyebut_kehidupan` **19.586** · `cacah_baris_dengan_medan`
**19.586** · `bulan_klines_funding` **19.598** · `cacah_lubang_funding` **880** ·
`cacah_lubang_tak_dikenal` **3** · `cacah_mati` **1.401** (kohort **456** + luar kohort
**945**; luar kohort berlubang **386**, berfunding **559**;
`bagian_mati_luar_kohort_dengan_lubang_funding` **0,4085**) ·
`cacah_hidup_tanpa_funding` **33** · `sebaran_bentuk_semua_lubang` 45/826/0/6 = **877** ·
`bentuk_terbitan_funding` 48/826/6 = **880** · seluruh medan `selisih_*` **0** ·
`kendali_sah` **true** · `sidik_seragam` **true** · `laporan_hilang` **[]** ·
`cacah_simbol_ada_lubang` **122**.

**`tabel_silang` (berfunding / kehilangan funding):** HIDUP **18.054 / 33** · MATI
**559 / 842** · SEPI **96 / 2** · TAK_TERUKUR **0 / 0**. Jembatan: 33 + 842 + 2 + 0 =
**877**, + **3** tak dikenal = **880**.

**Ketiga lubang tak dikenal, disebut dengan nama — semuanya BNXUSDT:**

| # | simbol | bulan lubang | `bulan_klines_pertama` | `bulan_klines_terakhir` | `cacah_bulan_klines_simbol` |
| --- | --- | --- | --- | --- | --- |
| 1 | BNXUSDT | **2022-04** | 2022-05 | 2026-06 | 48 |
| 2 | BNXUSDT | **2022-06** | 2022-05 | 2026-06 | 48 |
| 3 | BNXUSDT | **2022-08** | 2022-05 | 2026-06 | 48 |

**Butir 2 dan 3 duduk DI DALAM rentang klines simbolnya.** Rentang 2022-05..2026-06
adalah **50 bulan kalender** lawan `cacah_bulan_klines_simbol` **48** — selisih **2**,
tepat pada 2022-06 dan 2022-08. **Sebabnya BELUM DIUKUR dan DILARANG DIKLAIM**
(aturan 21). Inilah **poros peringkat pertama** sekarang.

**`cacah_hidup_tanpa_funding` 33, seluruhnya kelas AWAL:** BNXUSDT **7** · ICPUSDT
**13** · JUPUSDT **1** · QTUMUSDT **1** · TLMUSDT **11**.

**Kendali:** tiga baris BTCUSDT (2021-01, 2021-05, 2021-08) semuanya HIDUP dengan
`funding_ada` true; `kendali_sah` **true**.

**Sidik:** `sidik_kode` **`8a9b859c09cd64e30e203e6f8dc53411b8e341c44f112805b3041e5d4d3231b1`** ·
`sidik_data_funding` **`2c9fbd1b04f74c9c844bc223a99a103d12220b88d08667b3792720e5b9608d24`** ·
**`sidik_kode_funding`** **`d38548236f03314eaa648f64f73be5af2f682207be750a2c2fa413fad581513a`**
(tercatat pertama kali di STATE v57) ·
`sidik_kode_laporan` **`24b6bb265525e81c2e571b46e401f36903383f1e3738c487850861adc3e8c595`**.

### Lubang tengah — poros TUNTAS (tidak berubah dari v15)

Sumber: `reports/lubang_tengah.json`, blob
**`39cd1caacedc4d49ba23c91c80f553bb9fb135a6`**, 11.014 B, ditulis
**2026-07-29T09:38:52Z**, `versi_lubang_tengah` **2**, `versi_funding` **6**.

`cacah_lubang_tengah` **6** · `selisih_lubang_tengah` **0** · `cacah_lubang_ganda`
**0** · `cacah_kunci_ganda` **0** · `cacah_laporan_dibaca` **8** = `total_pecahan` **8** ·
`sebaran_status_lubang_tengah` {HIDUP **0**, MATI **6**, SEPI 0, TAK_TERUKUR 0}.

| simbol | bulan | status | rentetan | tetangga |
| --- | --- | --- | --- | --- |
| **BTCSTUSDT** | **2022-01** | MATI | 1 | 2021-12 → 2022-02 |
| **LITUSDT** | **2025-07 .. 2025-11** | MATI (kelimanya) | 5 | 2025-06 → 2026-01 |

Klines pertama BTCSTUSDT **2021-03**, LITUSDT **2021-02**; terakhir keduanya **2026-06**;
keduanya **64 bulan**. **Tidak satu pun berbulan `2022-05` atau `2024-05`.**

**H-A011 — MENANG:** LITUSDT **2026-01..2026-06**, keenam bulan **HIDUP**;
`h_a011_cacah_hidup` **6**. **Generalisasi DILARANG** (KC-47).
**H-A010 — MENANG 5–0:** kelima simbol `ada_medan` true, `bulan` [], `cacah_bulan` 0;
`h_a010_cacah_simbol_berisi` **0**; `kosong_seluruhnya` **true**.

### Karantina, terukur penuh

(kedelapan `reports/pulihkan_pecahan_<i>.json`, ref `a2c4b83c`; `pulihkan` VERSI 2,
`run_id_sumber` **30396803601**, ditulis 2026-07-29T02:48Z)

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

- Kedelapan `pulih_sah` **true**; `cacah_sha_tak_cocok`, `cacah_bagian_hilang`,
  `cacah_anggota_kurang`, `cacah_anggota_tak_aman`, `selisih_baris_total` seluruhnya
  **0**; `baris_terverifikasi` true.
- **Sidik kode seragam** `76c27e3c…62d700`; **sidik manifes seragam** `237ccf42…ba601`
  → penjumlahan lintas pecahan **sah** (aturan 22).
- **Aturan 46 terbukti bekerja:** pecahan 2 dan 5 melaporkan
  `definisi_dapat_dibedakan` **false** dan menolak memilih definisi.
- Sebaran sangat tidak rata — 42.585 sampai 131.760 baris per tar. Rata **43.011** boleh
  dikutip sebagai turunan, **bukan sebagai bukti**.
- Nama tar: `pecahan_<i>_karantina.part01.tar`. Manifes delapan berkas,
  jumlah **20.533.802 B**.

### `selisih_lilin` V1 — dibaca dari sumber

(blob `d19bdb5f…`, commit `c1dc0009`): `cacah_baris` **19586** · `cacah_berselisih`
**0** · `jumlah_klaim_langsung` = `jumlah_terbaca_langsung` = **839325999** ·
`dua_jalur_bertemu` **true** · `selisih_terhadap_warisan` bersih **−516135** ·
`uji_r312.teradjudikasi` **false** · kode keluar alur modul **2** (**dirancang**).
Empat kendali lolos; `kendali_deteksi` 11 medan; `kendali_teratas` **0,9615**.

### Modul dan laporan lain (tetap berlaku)

- **`sisa_defisit` V1:** penyebut kerja **17.398** · `cacah_berdefisit` **114** (0,66%) ·
  `defisit_calon` **712.925** (tautologis, KC-50) · `bagian_teratas` **0,4087** ·
  `defisit_terbesar` **42.510** = **TLMUSDT 2023-03**, HIDUP, 2.130 dari 44.640 lilin
  (**95,2% kosong**) · pasangan `2022-05`: ANCUSDT **26.959** dan LUNAUSDT **26.950**,
  berselisih **sembilan lilin** (dasar **H-A021**; kalimat sebab **DILARANG**).
- **`keterisian_lilin` V1:** lilin semesta LANGSUNG **839.325.999** · MATI penuh
  **1.392**, tak penuh **9** · defisit semesta **18.143.601**, **17.335.439 (95,5%)** di
  bulan pertama dan **808.162** di bukan-pertama (bagian **0,0445**) · bulan pertama rata
  terisi **≈49,7%** · harga TIDAK tersimpan (**14** medan).
- **`bulan_pertama` V1:** 37 dari 38 baris HIDUP-kecil adalah bulan pertama (0,973684);
  satu-satunya yang bukan **TLMUSDT 2023-03**; nisbah rata byte **0,527179**.
- **`irisan_byte` V1:** zona 22.440–97.634 byte berisi **38 HIDUP dan 0 MATI**; total
  byte **32.706.262.375**; HIDUP 32.049.492.952 · SEPI 77.728.024 · MATI 579.041.399.
- **`lubang_tebing` V1:** `mati_dulu` **40** (0.339) · `serempak` **78** (0.661) ·
  `lubang_dulu` **0**; tebing `2025-07` menguasai 39 dari 40 `mati_dulu`, satu-satunya
  bukan-tebing **BTCSTUSDT** (KC-47); **122** dari 787 simbol pernah berlubang funding.
- **`funding.py` V6** mencacah **87** simbol "funding tanpa klines" atas **787** simbol.

### Belum diukur, urut prioritas resmi (ADR-A021 kep. 7)

**Poros irisan 880 lawan 877 DIKELUARKAN — TUNTAS secara pembukuan.**

1. **BNXUSDT 2022-06 dan 2022-08** — mengapa dua bulan **di dalam** rentang klines
   (2022-05..2026-06) tidak lolos gerbang. **Menyatu** dengan poros lama "bulan pertama
   di penyebut lawan bulan pertama di bursa". Bahan calon: `reports/kehidupan_arsip_*.json`
   (sudah ada — aturan 86 (a)) dan `lux_ai/serapan/gerbang_1m.py` (`c8cc54c8`).
   **PERINGKAT PERTAMA.**
2. **Sebab kekosongan TLMUSDT 2023-03** (2.130 dari 44.640 lilin, 95,2% kosong, HIDUP).
3. **Tebing funding `2025-07`** (39 simbol) dan **BTCSTUSDT** — keserian dengan LITUSDT
   2025-07 **BELUM diukur** dan **DILARANG diklaim**.
4. **Identitas dua belas simbol-bulan karantina** — menuntut **modul CI**; manifes
   **20.533.802 B**. **Bukan kandidat murah.**
5. Sisanya: selisih 40−38 `diagnosa_kc15`; bentangan 38 kohort; H-A016; `mati_tersisip`
   atas 19.586; **`ukur_baris` V6**; R-7/19/20/28/36/37 dan R-199; R-236..R-247 dari
   jurnal 92–94; taksonomi lubang tiga kelas; **bagian `baris_mati` yang belum terbaca**.

## Penomoran berikutnya

Aturan resmi **1–81, 83, 84, 85, 86 (a) dan (b), 87** · usulan **77**, **78**, **82**,
**88** · **aturan berikutnya yang bebas 89** · KC resmi sampai **KC-54** (KC-16 kosong
selamanya) · **KC berikutnya KC-55** · Hipotesis: H-A016 (belum diuji), H-A017
(dilemahkan R-306), H-A018 (tafsir dibatasi A014/A015), H-A019 (DITERIMA TERBATAS),
**H-A020 dan H-A021 (DIUSULKAN, BELUM DIUJI, TANPA JALAN UJI YANG DIKETAHUI)**, H-A022
(TERBUKTI lewat R-313), H-A011 (TERBUKTI lewat R-314, dengan larangan generalisasi) ·
Hipotesis berikutnya **H-A023** · Jurnal berikutnya **146** · `STATE.md` berikutnya
**v58** · EKOR berikutnya **v17** · **UKUR berikutnya v16 (utang hidup, tertinggal satu
versi)** · PROMPT berikutnya **v55 (belum didorong)** · ADR berikutnya **A022** ·
Ramalan berikutnya **R-316** · papan skor **318**.

**Syarat praregistrasi R-316 — SEBELAS syarat kumulatif** (naik dari sepuluh): aturan
**79** (di `journal/**`, sebelum bahan dibuka) · aturan **83** · aturan **84** · aturan
**85** · aturan **86 (a) dan (b)** · **aturan 87** (penandaan TURUNAN di muka) ·
pemeriksaan **kebebasan medan terhadap kode**, tertulis, sebelum pita dikunci ·
**KC-50** · **KC-52** · **KC-53** · **KC-54** (definisi tiap medan yang diramalkan
**disalin** dari laporan atau kode ke dalam praregistrasi) · aturan **66**. Semangat
**usulan aturan 88** ditaati sukarela: ramalan keseragaman tanpa mekanisme ditulis
sebagai **sebaran**, bukan biner.
