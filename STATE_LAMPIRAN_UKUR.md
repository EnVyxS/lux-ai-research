# STATE lampiran UKUR — bagian 3 dari STATE (v19, milik STATE v60)

**PERINGATAN DI KEPALA BERKAS — BACA LEBIH DULU.** Berkas ini adalah **dorongan kedua**
v19. Dorongan pertama (commit `c28202df1ad4ec4abb791df37da10c9c41890670`, blob
`40e450b65cf9f5f068f3af7380711a0dd214646d`) **terdorong dalam keadaan TERPOTONG** —
berhenti di tengah kalimat pada usulan aturan 91, kehilangan seluruh daftar utang ukur,
penomoran berikutnya, dan syarat praregistrasi R-319. Itu **kesalahan dokumen butir 19**
(diuraikan di bawah). Versi ini **PADAT dengan sengaja**: bagian warisan yang tidak
berubah **dirujuk ke blob v18**, bukan disalin, agar berkas muat utuh dalam satu tulisan.

## Kedudukan berkas ini

STATE dipecah tiga sejak v43 (KC-42):

1. **`STATE.md`** — aturan 1–81, 83, 84, 85, 86 (a) dan (b), 87, **90**; KC-1..**KC-55**
   resmi; **KC-56 dan KC-57 diusulkan**.
2. **`STATE_LAMPIRAN_EKOR.md`** v19 — blob **`e19c5573966d835e9d40eadcb55165ab7d79f0de`**,
   commit **`b8877a2710544723ce81fc44ad505fa08fb7828b`** — papan skor, ADR, catatan
   kejujuran, utang verifikasi.
3. **`STATE_LAMPIRAN_UKUR.md`** (berkas ini, v19) — pengukuran, modul, workflow, uji,
   API, hipotesis, koreksi bernomor, utang ukur.
4. `STATE_LAMPIRAN_ADR.md` (`a02ef271`) dan **`PROMPT_KELANJUTAN.md`** (`35beed44`) —
   **arsip; BUKAN sumber** (ADR-A018 kep. 9).

**Dasar v19:** UKUR v18, blob **`11b14975a7ee2b00ca5e25ca19fc4e16ad5c1deb`**, commit
**`51c65e2afea4364a855e68c8f84465d1a2efcac9`**, dibaca UTUH pada giliran yang sama
(aturan 52, pencegahan KC-43).

### BAGIAN WARISAN YANG DIRUJUK, BUKAN DISALIN

Agar berkas ini muat utuh, bagian berikut **TIDAK berubah isinya sejak v18** dan
**tetap sah dikutip dari blob v18 `11b14975a7ee2b00ca5e25ca19fc4e16ad5c1deb`**:

- **SISA DEFISIT** (17.398 / 17.284 / **114** berdefisit / 712.925 / bagian_teratas
  0,4087 / TLMUSDT 2023-03 42.510).
- **KETERISIAN LILIN** (1.392 penuh + **9** tak penuh; 839.325.999; defisit_total
  18.143.601; defisit_pertama 17.335.439 = 95,5%; tabel sembilan baris MATI tak penuh;
  **95.237** dan 808.162 − 95.237 = **712.925**).
- **IRISAN BULAN PERTAMA** dan **daftar 38 berkas kecil bertanda** lengkap.
- **LEBAR ZONA IRISAN BYTE** (38 HIDUP / 0 MATI di 22.440–97.634; tabel tiga kelas;
  total 32.706.262.375).
- **BYTE PARQUET SEMESTA** dan **ARAH WAKTU KEMATIAN** (`mati_dulu` 40 = 0,339;
  tebing 2025-07 dengan 39 simbol; BTCSTUSDT satu-satunya bukan-tebing).
- **VONIS `ukur_kolom`** dan **ARAH SELISIH R-312 MUSTAHIL**.
- Blok **API modul lama** (`lubang_tengah` V2, `pulihkan` V2, `kehidupan_arsip`,
  `selisih_lilin`, `silang_funding` V2, `keterisian_lilin`, `sisa_defisit`,
  `bulan_pertama`, `irisan_byte`, `bentangan_kohort` V2, `kohort_ekor` V4,
  `ukur_baris` V5, `kehidupan`) beserta sidik-sidiknya.
- **Koreksi 1–15** dengan seluruh uraiannya, termasuk tabel tiga kejadian KC-54.
- **POLA WORKFLOW TRIO** terverifikasi dari `selisih_lilin.yml`.
- Angka v44/v45/v6/v7 (taksonomi 9 kelas, H-A013..H-A015, terhenti, SETTLED).

**Merujuk BUKAN menghapus.** Bila berkas ini bertentangan dengan v18 pada bagian mana
pun yang dirujuk, **v18 menang** dan pertentangan itu wajib dicatat sebagai koreksi baru.

## KESERASIAN VERSI — PULIH PADA ATURAN, BELUM PADA PAPAN SKOR

- `STATE.md` **v60** — blob **`d3f1448fad4ead804be59b1bbb1562b460f01621`**, commit
  **`8345668e9a8f0e01bcbe86fd9d0f60f4709fd834`**.
- `STATE_LAMPIRAN_EKOR.md` **v19** — blob **`e19c5573966d835e9d40eadcb55165ab7d79f0de`**.
- `STATE_LAMPIRAN_UKUR.md` **v19** — berkas ini.

Ketertinggalan **dua versi isi** yang dicatat EKOR v19 terhadap berkas ini — pembacaan
`lubang_awal.json`, kelas batas pemotongan oleh MODUL, tabel `baris_penyebut_butir_2`,
penanda konvensi pada tabel H-A010, aritmetika 50 − 48 = 2 dan 9 − 7 = 2, pembacaan
`bulan_absen.py`, dan seluruh isi `bulan_absen_ringkas.json` — **LUNAS oleh berkas ini**.

**SATU KETIDAKSERASIAN TETAP TERBUKA:** `STATE.md` v60 memuat papan skor **325**; EKOR
v19 memuat dan **mengesahkan 329**. Sebabnya tersurat: R-318 diadjudikasi di jurnal 151,
**sesudah** STATE v60 didorong. **Sumber sah papan skor adalah EKOR v19** (aturan 29).
Berkas ini **tidak memuat dan tidak berwenang mengesahkan** papan skor.
**Pemulihan penuh menuntut `STATE.md` v61.**

**Satu berkas per push tetap MENGIKAT** (KC-42, KC-43).

**Tentang push berkas ini:** ia di akar repo sehingga menyalakan `ci.yml`. Tidak satu
pun `tests/**` berubah → cacah uji tetap **1377**; ramalan **deterministik, MUDAH**,
TIDAK masuk papan skor, TIDAK menambah beruntun aturan 57. Laporannya **WAJIB dibaca
sebelum push akar berikutnya** (aturan 38 **ke-66**) dan **WAJIB DITOLAK bila medan
`commit` tidak cocok** (**aturan 90**).

## KESALAHAN DOKUMEN BUTIR 19 — BERKAS AKAR TERDORONG DALAM KEADAAN TERPOTONG

**Kejadian.** Pada giliran yang sama dengan berkas ini, UKUR v19 didorong sekali
(commit `c28202df1ad4ec4abb791df37da10c9c41890670`, blob
`40e450b65cf9f5f068f3af7380711a0dd214646d`) dan **berhenti di tengah kalimat**:

> *"Ramalan yang butir-butirnya diturunkan dari **satu arit"*

**Yang hilang:** sisa usulan aturan 91 · catatan kejujuran atas 88/89/91 · **seluruh
daftar utang ukur** · **penomoran berikutnya** · **syarat kumulatif praregistrasi R-319**.

**Sebab, disebut telanjang:** batas panjang penulisan penyusun, **bukan galat alat**.
`push_files` menulis ulang **seluruh** berkas, sehingga berkas yang terpotong di sumber
terdorong utuh-utuhnya dalam keadaan cacat. **Tidak ada peringatan alat sama sekali** —
push dilaporkan **berhasil**.

**Yang menangkapnya:** **aturan 52**, pembacaan ulang utuh pada giliran yang sama.
Tidak ada penangkal lain yang mungkin: alat melaporkan sukses, SHA sah, dan seluruh isi
yang **ada** benar.

**Ini kelas cacat baru, dan ia kerabat dekat pemotongan oleh MODUL:**

| kelas | siapa memotong | apakah berteriak | penangkal |
| --- | --- | --- | --- |
| pemotongan ALAT | alat baca | **YA**, verbatim `truncated (showing NN%)` | membaca peringatan |
| pemotongan MODUL | kode penulis laporan | **TIDAK** | aturan 86 (b) — baca kode dulu |
| **pemotongan PENYUSUN [BARU]** | **penyusun berkas** | **TIDAK** | **aturan 52 — baca ulang utuh** |

**Bacaan yang wajib melekat, dan ia membalik catatan v19 sendiri.** Bagian "BATAS
KEKUATAN ATURAN 52" di bawah menyimpulkan bahwa aturan 52 menjaga **kesetiaan salinan**,
bukan mutu penalaran. **Butir 19 adalah pembuktian paling murni atas kalimat itu** —
cacat kesetiaan salinan paling telanjang yang mungkin (separuh berkas hilang), dan
aturan 52 menangkapnya pada percobaan pertama. **Batas aturan 52 dipersempit di v19,
dan pada giliran yang sama nilainya di dalam batas itu terbukti mutlak.**

**Penangkal WAJIB sejak v19:** berkas akar yang diperkirakan melampaui ~25 KB **WAJIB
disusun dengan bagian warisan DIRUJUK ke blob versi sebelumnya**, bukan disalin ulang.
Menyalin ulang berkas besar dari konteks terpakai adalah **KC-42 yang dijalankan**, bukan
KC-42 yang dihindari.

**Usulan aturan 92 [BELUM RESMI].** *Setiap push berkas akar wajib diikuti pembacaan
ulang utuh pada giliran yang sama, dan berkas yang terbaca tidak berakhir pada penanda
penutupnya sendiri WAJIB didorong ulang sebelum pekerjaan lain apa pun.* **TIDAK
diresmikan:** satu kejadian (ADR-A019 kep. 3). Bagian pertamanya toh sudah aturan 52.

**Utang verifikasi 47 LAHIR:** memastikan tidak ada berkas akar **lain** yang pernah
terdorong terpotong tanpa tertangkap. Sampai diperiksa, **DILARANG** menyatakan butir 19
kejadian tunggal.

## KOREKSI KC-41 — Koreksi 1–15 dirujuk ke v18; Koreksi 16 baru

Koreksi **1–15** tercatat lengkap di v18 (`11b14975a…`) dan **tetap berlaku penuh**.
Ringkas seperlunya: Koreksi 4 (tiga angka baris parquet, 839.325.999 + 516.135 =
839.842.134 ✅, 19.586 + 12 = 19.598 ✅) · Koreksi 9 (**salah nalar**, bukan salah
ketik; kelas cacat tanpa penangkal) · Koreksi 11, 13, 14 (**tiga kejadian KC-54**) ·
Koreksi 15 (`cacah_bulan` nyaris dibaca sebagai bentangan kalender; dibatalkan oleh
BNXUSDTSETTLED 11 vs **6** dan TLMUSDTSETTLED 15 vs **9**; penangkalnya **periksa simbol
kedua sebelum menulis definisi**).

**[v19] KC-54 TETAP TIGA KEJADIAN**, ditangkal **preventif** untuk kedua kalinya
berturut: definisi `bulan_absen`, `pembeda_absen`, `rentang`, dan `kendali` **disalin
verbatim** sebelum satu pun angkanya ditafsirkan.

**[v19] Koreksi 13 kini berlapis dua.** Tafsir "lubang di luar penyebut = bulan sebelum
simbol lahir" bukan sekadar tak terbukti: **sebab sejatinya kini bernama** — 2022-06 dan
2022-08 terukur **`gagal_gerbang`**, jadi sebabnya **gerbang**, bukan kelahiran simbol.

### Koreksi 16 [BARU v19] — KONVENSI BATAS TABEL SENDIRI BERGESER SATU BULAN

Ini **kesalahan dokumen butir 18**, diresmikan di STATE v60, disalin ke sini karena
tabelnya hidup di lampiran ini.

Tabel H-A010 menulis kolom "rentang lubang awal" dengan batas kanan **EKSKLUSIF**; medan
sumbernya `akhir_lubang_awal` pada `reports/lubang_awal.json` **INKLUSIF**. Selisih tepat
**+1**, **lima dari lima**:

| simbol | tabel lama (EKSKLUSIF) | `akhir_lubang_awal` sejati (INKLUSIF) |
| --- | --- | --- |
| BNXUSDT | 2023-02 | **2023-01** |
| ICPUSDT | 2022-09 | **2022-08** |
| JUPUSDT | 2024-02 | **2024-01** |
| QTUMUSDT | 2020-03 | **2020-02** |
| TLMUSDT | 2023-03 | **2023-02** |

**Akibat terukur:** butir 3 R-317 mengutip **2023-02** dari tabel cacat ini dan **KALAH**
terhadap **2023-01**. **Kekalahan TIDAK dibatalkan** (aturan 29, ADR-A016); yang
ditambahkan hanya sebabnya.

**Mengapa lolos begitu lama:** **setiap angkanya benar**; yang salah hanya **konvensi**,
dan konvensi tidak pernah dibaca ulang. Penangkal butir 17 (aritmetika terbuka) **tidak
dapat menangkapnya sama sekali**.

**DILARANG** mengutip tabel H-A010 di lampiran ini sebagai nilai `akhir_lubang_awal`.
**Sumber sah hanya `reports/lubang_awal.json`.**

**KC-57 [DIUSULKAN, DITAHAN].** *Tabel ringkasan susunan tangan dapat memakai konvensi
batas yang berbeda dari medan sumbernya; kecocokan angka tidak menjamin kecocokan
konvensi.* Penangkal: kepala kolom WAJIB menyebut **nama medan sumber dan konvensinya**.
**TIDAK diresmikan:** lima baris dari **satu kolom pada satu tabel** = satu cacat tampak
lima kali. Meresmikannya adalah **KC-47 persis**.

**Pola koreksi resmi, bertumbuh:** cacat yang bertahan paling lama bukan salah hitung,
melainkan **tafsir masuk akal atas angka yang benar**; sejak v15 bertambah **label masuk
akal atas medan yang benar**; sejak v18 **kecocokan angka pada satu contoh yang terdengar
seperti definisi**; sejak v19 **konvensi batas yang bergeser satu satuan tanpa satu pun
angka salah**; dan **[butir 19] berkas yang setiap kalimatnya benar tetapi separuhnya
tidak ada**.

## BATAS KEKUATAN ATURAN 52 — DIPERSEMPIT, LALU TERBUKTI MUTLAK DI DALAM BATASNYA

> Pembacaan ulang **dokumen sendiri** lemah terhadap penalaran cacat: ia membaca kalimat
> yang sudah diyakini benar. Pembacaan **kode** kuat terhadapnya.

Bukti ketiga [v16], keempat [v17], kelima [v18] tercatat di v18.
**[v19] Bukti keenam, paling tajam:** butir 18 lolos dari **seluruh** pembacaan ulang
sejak tabel H-A010 disusun, karena **setiap angkanya benar**; ia **tidak dapat**
ditangkap aritmetika. Yang menangkapnya **sumber di luar dokumen** — pembacaan
`reports/lubang_awal.json`.
**[v19] Bukti balik, dan ini yang paling berharga.** Pada giliran R-318, aturan 86 (b)
dipakai lebih dulu: `bulan_absen.py` dibaca UTUH **sebelum** laporannya. Satu pembacaan
kode memberi **tiga penangkal sekaligus**: (1) kepastian modul **tanpa pembatas baris**
sehingga `baris_berabsen` lengkap — mustahil diketahui dari laporan; (2) definisi tiap
medan **disalin** sebelum ditafsirkan; (3) pengetahuan bahwa **tepi tidak pernah absen
menurut definisi**, sehingga 2022-04 mustahil muncul — dan pita ramalan dikunci sadar
atas dasar itu.
**[v19, butir 19] Bukti ketujuh, arah berlawanan:** aturan 52 menangkap **separuh berkas
yang hilang** pada percobaan pertama. **DILARANG** menulis bahwa aturan 52 menjaga mutu
penalaran atas dokumen; yang dijaganya **kesetiaan salinan** — dan di dalam wilayah itu
ia **tidak tergantikan**.

**Penangkal wajib sejak v59:** setiap panjang deret ditulis bersama aritmetika
`akhir − awal + 1` secara terbuka. Diterapkan di seluruh berkas ini.

## KELAS BATAS — PEMOTONGAN OLEH MODUL, BUKAN OLEH ALAT

`reports/lubang_awal.json` terbaca **42.449 byte, UTUH, tanpa satu pun peringatan alat**.
Di dalamnya: `penyebut_butir_1` **118** vs `cacah_baris_penyebut_butir_1_dilapor` **60**
→ **58 baris tidak pernah ditulis**. Sebabnya terukur dari kode:
`lux_ai/serapan/lubang_awal.py` (blob **`8c36943da222dfa262b3b9f2117bf72dc801681d`**,
DIBACA UTUH) memuat **`BATAS_BARIS_LAPORAN = 60`**.

> **Lebih berbahaya daripada pemotongan alat.** Alat berteriak; modul diam. Pendeteksi
> satu-satunya: **membaca kode sebelum laporan** (aturan 86 b).

**LARANGAN PERMANEN.** DILARANG menarik **cacah, sebaran, daftar, minimum, maksimum,
atau kesimpulan apa pun** dari larik `baris_penyebut_butir_1`. Hanya medan agregat yang
dihitung modul atas **seluruh 118** yang boleh dipakai.

**Pemeriksaan preventif atas modul kedua:** `lux_ai/serapan/bulan_absen.py` (blob
**`10279d721d66a86b6d265badf81ada3204648f69`**) dibaca UTUH **sebelum** laporannya
dibuka. **TIDAK memiliki pembatas baris apa pun** → `baris_berabsen` **LENGKAP**, dan itu
**terukur**, bukan diasumsikan.

**Konsekuensi prosedural:** setiap laporan yang dikutip sesudah v19 wajib disertai jawaban
atas: **apakah modul penulisnya sudah dibaca, dan apakah ia punya pembatas baris?**

## `reports/lubang_awal.json` — bahan R-317

Blob **`3da15a11c3cd949fb2741f919beb2b515a51d70f`**, **42.449 B**, ref `1ba0a007…`.
`waktu_utc` **2026-07-30T07:23:11Z** · `sidik_kode`
**`156499ce9d6e822bb7f57786e8e308955441996699c1fd53d0e8814e1f8f2362`**.
**Tanpa pemotongan ALAT; DIPOTONG MODUL.**

`cacah_simbol_ada_lubang` **122** · `cacah_simbol_lubang_awal` **5** ·
`cacah_simbol_lubang_bukan_awal` **118** · `cacah_bangkit` **8** · `penyebut_butir_1`
**118** / `bagian_butir_1` **1.0** · `penyebut_butir_2` **5** / `numerator_butir_2` **3**
/ `bagian_butir_2` **0.6** · semua `selisih_*` **0**.

**`baris_penyebut_butir_2` — 5 dari 5, LENGKAP** (larik ini **tidak** kena batas 60):

| simbol | `bulan_pertama` | `bulan_terakhir` | `cacah_bulan` | `cacah_lubang` | `cacah_lubang_awal` | `cacah_lubang_bukan_awal` | **`akhir_lubang_awal` (INKLUSIF)** | `cacah_mati` | `bangkit` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **BNXUSDT** | **2022-05** | 2026-06 | **48** | 19 | **7** | 12 | **2023-01** | 15 | false |
| ICPUSDT | 2021-05 | 2026-06 | 62 | 16 | 16 | 0 | **2022-08** | 2 | true |
| JUPUSDT | 2024-01 | 2026-06 | 30 | 1 | 1 | 0 | **2024-01** | 0 | false |
| QTUMUSDT | 2020-02 | 2026-06 | 77 | 1 | 1 | 0 | **2020-02** | 0 | false |
| TLMUSDT | 2021-07 | 2026-06 | 60 | 20 | 20 | 0 | **2023-02** | 8 | true |

Baris lain terbaca di `baris_penyebut_butir_1` (**DILARANG dicacah** — 58 hilang):
BTCSTUSDT (2021-03..2026-06, 64, `cacah_mati` **63**) · DARUSDT (2022-04..2026-06, 51) ·
FTTUSDT (2022-04..2026-06, 51, `cacah_mati` 43) · LENDUSDT (2020-07..2020-11, 5).

**Temuan struktural:** **empat dari lima** kontigu sempurna (16=16, 20=20, 1=1, 1=1).
**Hanya BNXUSDT tidak:** 7 dari 19. Rentetan 2022-05..2023-01 = **9**; 9 − 7 = **2** —
**selang yang sama** dengan 50 − 48 = 2, bernama **2022-06** dan **2022-08**. ✅

**Blok `uji_r305` — VONIS ALAT, BUKAN ADJUDIKASI (KC-49).** Ia menyatakan sendiri butir 1
KALAH (`bagian` **1.0** di luar pita 0.55–0.95) dan butir 2 KALAH (**0.6** < 0.80;
cacah **5** di bawah pita 20–120). **Papan skor TIDAK disentuh** (aturan 29). R-305 tetap
menunggu **adjudikasi tangan** atas `journal/2026-07-30-125.md`, **belum dibaca**.

**`bagian_butir_1` = 1.0 TAUTOLOGIS:** modul menghitung `cacah_bulan` sebagai `len(urut)`
atas penyebut 19.586 → pembilang dan penyebut tidak bebas. **DILARANG** dibaca sebagai
temuan empiris.

Tetapan R-305 di modul: `R305_PITA_BUTIR_1=(0.55,0.95)` ·
`R305_MINIMAL_PENYEBUT_BUTIR_1=100` · `R305_PITA_BUTIR_2_CACAH=(20,120)` ·
`R305_MINIMAL_BAGIAN_BUTIR_2=0.80`. Docstring memuat **praregistrasi R-305**.

## `reports/bulan_absen_ringkas.json` — bahan R-318, TERBACA UTUH

Blob **`e450d9f95e9bca0dc28a0e01c6aad6594c4fa3d6`**, ref `6894b02f…`. **TANPA PEMOTONGAN
ALAT, dan modulnya terukur TANPA PEMBATAS BARIS.**

`waktu_utc` **2026-07-29T17:50:29Z** · `versi_bulan_absen` **1** · `sidik_kode`
**`0294eb3a2fca6354b495148fc87d564f649d545a81314f21ef432775cf163088`** · `berkas_sumber`
`reports/bulan_absen.json` · `byte_sumber` **249.992** · `sidik_sumber`
**`d2fc3bfb362f834225faab76d6bf87b8f334d1ee26638a8112fb9b546614a3bd`**.

**Definisi resmi, DISALIN VERBATIM sebelum ditafsirkan (KC-54):**

> `bulan_absen` — *"bulan kalender di antara bulan_pertama dan bulan_terakhir sebuah
> simbol yang TIDAK ada di penyebut 19.586; BUKAN lubang funding dan BUKAN lubang
> tengah"*.

> `pembeda_absen` — *`gagal_gerbang` bila bulan itu ADA di manifes arsip;
> `tak_diterbitkan_arsip` bila tidak ada di manifes; `tak_terukur` bila manifes tidak
> lengkap terbaca*.

**Konsekuensi definisi:** karena batasnya *"di antara"*, **bulan tepi tidak pernah dapat
absen** → **2022-04 mustahil muncul** di medan ini, diketahui **sebelum** pita R-318
dikunci.

**Penggugur dan kendali, diperiksa LEBIH DULU:** `kendali_sah` **true** (BTCUSDT **78**/0
· ETHUSDT **78**/0, ambang 60) · `penggugur_menyala` **false** · `sidik_seragam` **true**
· laporan/manifes/pecahan dibaca **8**/**8**/**8** · `cacah_kunci_ganda` **0** ·
`laporan_hilang` [] · `manifes_hilang` [] · `selisih_penyebut` **0** ·
`selisih_nama_penyebut` **0** · `cacah_nama_tak_konsisten_rentang` **0** ·
`penyebut_kehidupan` **19.586** · `cacah_nama_penyebut` / `cacah_nama_didaftar`
**787**/**787** · `sidik_kode_laporan` [`24b6bb26…c8595`].

**Besaran pokok:** `cacah_nama_berabsen` **10** dari 787 · `jumlah_bulan_absen` **11** ·
`jumlah_bulan_absen_pasangan` **11** · `jumlah_bulan_absen_luar_pasangan` **0** ·
`cacah_pasangan` **15** · **`sebaran_pembeda` = `gagal_gerbang` 11 / `tak_diterbitkan_arsip`
0 / `tak_terukur` 0** · `selisih_absen_pasangan_jurnal_113` **−1** (12 tercatat vs **11**
terukur).

**`baris_berabsen` — sepuluh nama, LENGKAP:**

| simbol | `bulan_absen` | `bulan_pertama` | `bulan_terakhir` | `rentang` | `cacah_bulan_lolos` | pembeda |
| --- | --- | --- | --- | --- | --- | --- |
| AERGOUSDT | 2025-04 | 2024-09 | 2026-06 | 22 | 21 | gagal_gerbang |
| AIAUSDT | 2026-01 | 2025-09 | 2026-06 | 10 | 9 | gagal_gerbang |
| **BNXUSDT** | **2022-06, 2022-08** | **2022-05** | 2026-06 | **50** | **48** | gagal_gerbang ×2 |
| CTKUSDT | 2025-04 | 2020-11 | 2026-06 | 68 | 67 | gagal_gerbang |
| CVCUSDT | 2025-05 | 2020-11 | 2026-06 | 68 | 67 | gagal_gerbang |
| CVXUSDT | 2025-07 | 2022-09 | 2026-06 | 46 | 45 | gagal_gerbang |
| LITUSDT | 2025-12 | 2021-02 | 2026-06 | 65 | 64 | gagal_gerbang |
| MAVIAUSDT | 2025-03 | 2024-02 | 2026-06 | 29 | 28 | gagal_gerbang |
| PUMPUSDT | 2025-07 | 2025-04 | 2026-06 | 15 | 14 | gagal_gerbang |
| SLPUSDT | 2025-07 | 2023-10 | 2026-06 | 33 | 32 | gagal_gerbang |

**`baris_pasangan_settled` (15).** `absen_sama_dengan_settled` **true** untuk kesembilan
simbol berabsen tunggal; **false** untuk **BNXUSDT** (`bulan_settled_terakhir`
**2023-02**, `settled_ada_di_absen` false). Lima pasangan berabsen **nol**: BDXNUSDT
(2026-04, 10/10) · ICPUSDT (2022-09, 62/62) · MINAUSDT (2023-02, 41/41) · SXPUSDT
(2026-06, 71/71) · TLMUSDT (2023-03, 60/60).

**Ketertutupan diperiksa tangan:** 9 + 2 = **11** = `jumlah_bulan_absen` ✅ ·
11 + 0 + 0 = **11** ✅ · 10 + 5 = **15** pasangan ✅

### Tiga kesimpulan TERUKUR

1. **Bulan absen adalah gejala GERBANG, bukan gejala PENERBITAN.** Sebelas dari sebelas
   **ADA di manifes arsip** lalu **ditolak gerbang**. Pertama kalinya sebuah kelas lubang
   disertai **mekanisme bernama**, bukan sekadar bentuk.
2. **BNXUSDT satu-satunya simbol dengan lebih dari satu bulan absen** di seluruh 787.
3. **BNXUSDT satu-satunya yang bulan absennya BUKAN bulan settled terakhirnya.**

**KC-53 ditangkal preventif:** nol pada dua pembeda lain **TIDAK** dibaca sebagai "arsip
selalu menerbitkan". Yang terukur: **dari 11 bulan absen, tak satu pun bersebab itu.**

### Yang DILARANG disimpulkan

1. **DILARANG** menyebut **klausa mana** dari `gerbang_1m.py` yang menjatuhkan
   bulan-bulan itu → **utang ukur 25**.
2. **DILARANG** menyamakan "tidak ada di penyebut" dengan "dijatuhkan gerbang" **secara
   umum**, di luar medan `pembeda_absen` untuk 11 bulan itu.
3. **DILARANG** menyimpulkan hanya simbol berpasangan settled yang berabsen: **5 dari 15**
   pasangan berabsen nol → "berpasangan settled" **bukan syarat cukup**.
4. **DILARANG** memakai blok `uji_r288` sebagai adjudikasi (KC-49).
5. **DILARANG** mengutip selisih **3 lawan 2** sebagai bukti KC-52. Angka 3 adalah
   `R288_BNX_ABSEN`, **tetapan ramalan di dalam kode**, bukan pengukuran laporan kedua.
   **Ramalan yang kalah bukan dua penyebut yang berselisih.**

## JEMBATAN 48 / 50 / 51 — TERTUTUP TANPA SISA

| angka | medan / asal | arti terukur |
| --- | --- | --- |
| **48** | `cacah_bulan_lolos`; `cacah_bulan` (`lubang_awal`); `cacah_bulan_klines_simbol` | bulan BNXUSDT yang **ADA di penyebut 19.586** |
| **50** | `rentang` (`bulan_absen_ringkas`) | **bentangan kalender** 2022-05..2026-06 |
| **51** | `cacah_bulan` (`semesta_rentang`); `bulan_per_simbol` (`semesta_bulan_1m`) | bulan berberkas, bentangan 2022-04..2026-06 |

- **51 − 50 = 1** → satu bulan **di tepi**: **2022-04**.
- **50 − 48 = 2** → dua bulan **di dalam**: **2022-06**, **2022-08**, keduanya
  **`gagal_gerbang`**.
- **51 − 48 = 3** = 2 + 1 ✅ — dan `cacah_lubang_tak_dikenal` juga **3**, dengan **nama
  yang sama persis**.

**Silang kedua yang menutup mandiri:** 9 − 7 = **2**, dari laporan **berbeda**.

**TERBUKTI:** untuk BNXUSDT ketiga angka konsisten dan ketiga bulan **bernama**;
**KC-52 SEBAGIAN TERDAMAIKAN** untuk pertama kalinya sejak lahir.
**TIDAK TERBUKTI:** apakah himpunan **787** pada kedua laporan sama → **KC-52 TIDAK
DICABUT**. Keanggotaan penyebut **786 simbol lain** belum diukur → **DILARANG**
digeneralkan (KC-47).

## SEMESTA BULAN 1M dan SEMESTA RENTANG

`semesta_bulan_1m.json` blob **`a1a6d3f0f13dd7100a91853cadfcaa9a5620fee3`**, **18.884 B**,
`waktu_utc` **2026-07-28T09:44:48Z**, UTUH. Dua kunci; **tidak ada nama bulan**; cacah
entri **DILARANG dikutip terukur** (aturan 66). `bulan_per_simbol["BNXUSDT"]` **51** ·
`["BNXUSDTSETTLED"]` **6**.

`semesta_rentang.json` blob **`8d5bd06ca4073dac8a8ef7841d81824427cc8e63`**, **110.662 B**.
**BATAS ALAT WAJIB DISEBUT SETIAP KALI:** `This result has been truncated (showing 95% of
full).` Potongan hilang di **tengah**, abjad **P–R** (antara `PLTRUSDT` dan `ROBOUSDT`).
**TANPA `waktu_utc`, TANPA sidik** (ekor berkas terbaca). Entri terakhir `"龙虾USDT"`.

| simbol | `bulan_pertama` | `bulan_terakhir` | `cacah_bulan` | bentangan (TURUNAN) | lubang |
| --- | --- | --- | --- | --- | --- |
| **BNXUSDT** | **2022-04** | **2026-06** | **51** | **51** | **0** |
| BNXUSDTSETTLED | 2022-04 | 2023-02 | **6** | 11 | **5** |
| TLMUSDT | 2021-07 | 2026-06 | **60** | 60 | **0** |
| TLMUSDTSETTLED | 2022-01 | 2023-03 | **9** | 15 | **6** |
| MATICUSDT | 2020-10 | 2024-09 | 48 | 48 | 0 |
| BTCSTUSDT | 2021-03 | 2026-06 | 64 | 64 | 0 |
| SXPUSDT | 2020-07 | 2026-05 | 71 | 71 | 0 |
| FTTUSDT | 2022-04 | 2026-06 | 51 | 51 | 0 |
| 1000LUNCBUSD | 2022-05 | 2023-12 | 20 | 20 | 0 |
| ICPUSDT_SETTLED | 2022-01 | 2022-09 | 9 | 9 | 0 |

**Larangan penuh:** (1) bukan pengukuran "semesta 1m"; (2) DILARANG menyimpulkan hanya
SETTLED yang berlubang; (3) DILARANG mengklaim berapa simbol berlubang; (4) DILARANG
dibandingkan secara keserempakan — tak bertanggal (**KC-56**); (5) DILARANG memindahkan
sifat `cacah_bulan` ↔ `bulan_per_simbol`; (6) DILARANG menyatakan gerbang menjatuhkan
bulan mana pun atas dasar berkas ini; (7) DILARANG menyamakan "ada di semesta rentang"
dengan "ada di penyebut 19.586".

**Pencabutan sebagian (v18) tetap:** larangan "51 mencakup 2022-04" **DICABUT** untuk
`cacah_bulan`, **TETAP PENUH** untuk `bulan_per_simbol`. **Kesamaan angka DILARANG
memindahkan pencabutan.**

**KESERAMPAKAN:** 1m 2026-07-28T09:44:48Z · silang_funding 2026-07-29T08:17:55Z ·
bulan_absen_ringkas 2026-07-29T17:50:29Z · lubang_awal 2026-07-30T07:23:11Z · semesta
rentang **tak bertanggal**. **Bukan pengukuran serempak.**

**KC-56 [DIUSULKAN] TIDAK bertambah:** kedua laporan baru **bertanggal**. **KC berikutnya
KC-59.**

**Aturan 36 TETAP TIDAK diberi kasus keempat** oleh 3=3, 6=6, maupun 51=51. Yang menutup
jembatan adalah **aritmetika di dalam satu simbol**, bukan sebaran lintas simbol.

## `gerbang_1m.py` — DIBACA UTUH; POROS PERINGKAT PERTAMA

Blob **`c8cc54c84a57173ef2e426c317d6ac50734e9b4a`**; penerapan **ADR-A004 §2**.

**Enam klausa:** `deret_tidak_kosong` · `tanpa_duplikat` · `tanpa_menit_hilang` ·
`jarak_60_detik` · `selaras_menit` · `satuan_milidetik`. `nilai_deret` →
`lolos = not pelanggaran` — **satu klausa gagal cukup menjatuhkan**.
`MS_BAWAH=1_000_000_000_000`, `MS_ATAS=100_000_000_000_000`. `sidik_kode()` mencap **dua**
berkas: `gerbang_1m.py` + `resample.py` (`66a4b177`).

Rumus wajib dikutip persis:
`rentang = (unik[-1] - unik[0]) // MS_MENIT + 1`;
`menit_hilang_dalam_rentang = rentang - len(unik)`
— dari rentang **yang ada di berkas**, bukan panjang bulan kalender. **DISALIN**, bukan
diimpor dari `diagnosa_kc6.celah_menit` (aturan 10); penjaganya `tests/test_gerbang_1m.py`.
Docstring mengaku nilainya **dapat negatif**. Fungsi lain: `persen` ·
`satuan_stempel_dari_besaran` · `ukur_deret` · `nilai_klausa` · `ringkas_gerbang`.

**TEMUAN STRUKTURAL MENGIKAT.** **PUSTAKA MURNI** — tanpa `KELUARAN`, tanpa
`jalankan`/`main`, **tidak menulis laporan apa pun**.

> **Pertanyaan poros tentang gerbang TIDAK dapat dijawab dari keluaran gerbang, sebab
> tidak ada keluaran.** Ia harus lewat laporan **modul pemanggil**.

**Inilah yang membuat utang ukur 25 mahal:** terukur bahwa **11 bulan absen dijatuhkan
gerbang**, tetapi **tidak ada satu medan pun di repo yang menamai klausa pelanggaran per
simbol-bulan**. **ADR-A004 §2 naik menjadi utang bacaan berperingkat tertinggi.**

## SILANG FUNDING — tiga lubang tak dikenal, kini BERNAMA dan TERJELASKAN POSISINYA

Blob **`b61fe8b3bcabbfce435dd5e5f78fc367f6bef617`**, `waktu_utc` **2026-07-29T08:17:55Z**.
**BATAS ALAT WAJIB DISEBUT:** `This result has been truncated (showing 54% of full).`
Tengah larik **`baris_mati`** TIDAK TERLIHAT → **cacah total `baris_mati` DILARANG
diklaim terukur** (utang verifikasi 39, utang ukur 17).

| # | simbol | bulan | dalam rentang klines? | ada di semesta rentang? | posisi thd penyebut | pembeda |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | BNXUSDT | **2022-04** | **TIDAK** | YA | **tepi** | — |
| 2 | BNXUSDT | **2022-06** | YA | YA | **di dalam** | **`gagal_gerbang`** |
| 3 | BNXUSDT | **2022-08** | YA | YA | **di dalam** | **`gagal_gerbang`** |

`bulan_klines_pertama` **2022-05** · `bulan_klines_terakhir` **2026-06** ·
`cacah_bulan_klines_simbol` **48**.
**Ketiganya kini terjelaskan POSISINYA tanpa sisa. SEBAB KLAUSANYA tetap BELUM DIUKUR.**

| jalur | susunan | jumlah |
| --- | --- | --- |
| bentuk | 45 awal + 826 ekor + 0 seluruh + 6 tengah | **877** |
| tabel silang | 33 HIDUP + 842 MATI + 2 SEPI + 0 TAK_TERUKUR | **877** |
| terbitan funding | 48 awal + 826 ekor + 6 tengah | **880** |

**877 + 3 = 880** ✅ Kedua jalur menuju 877 lahir dari laporan yang sama — **aturan 36,
bukan dua pengukuran bebas**.

`penyebut_kehidupan` **19.586** · `bulan_klines_funding` **19.598** ·
`cacah_lubang_funding` **880** · `cacah_lubang_tak_dikenal` **3** · `cacah_mati` **1.401**
(kohort 456 + luar kohort 945) · luar kohort berlubang **386** / berfunding **559** ·
`bagian_mati_luar_kohort_dengan_lubang_funding` **0,4085** · `cacah_hidup_tanpa_funding`
**33** · `tabel_silang` HIDUP 18.054/33, MATI 559/842, SEPI 96/2, TAK_TERUKUR 0/0 · semua
`selisih_*` **0** · `kendali_sah` true · `sidik_seragam` true · `laporan_hilang` [].

**Kelima simbol 33, semuanya kelas AWAL:** BNXUSDT **7** · ICPUSDT **13** · JUPUSDT **1**
· QTUMUSDT **1** · TLMUSDT **11** → 7+13+1+1+11 = **33** ✅
**Ketertutupan:** 18.054+33 = **18.087** ✅ · 559+842 = **1.401** ✅ · 96+2 = **98** ✅ ·
jumlah **19.586** ✅

Sidik: `8a9b859c…3231b1` · `sidik_data_funding` `2c9fbd1b…608d24` ·
**`sidik_kode_funding` `d38548236f03314eaa648f64f73be5af2f682207be750a2c2fa413fad581513a`**
· `sidik_kode_laporan` `24b6bb26…c8595`.

**Adjudikasi R-315 — FINAL, DILARANG DIADILI ULANG.** Butir 1 **TEPAT** · butir 2
**MELESET** (1 dari 3) · butir 3 MUDAH. **DILARANG ditulis ulang sebagai SEPARUH.**
**[v19]** Kekalahan butir 2 kini **dijelaskan sepenuhnya** — dua lubang lain duduk di
dalam rentang dan gugur karena **gerbang**. **Vonisnya tidak berubah.**

## KC-18 — semesta kehidupan

Atas **19.586**: **1.401 MATI** (7,153%) · **98 SEPI** · **18.087 HIDUP**.
`cacah_simbol_tanpa_hidup` **18**. 18.087 + 98 + 1.401 = **19.586** ✅
**787** bulan PERTAMA + **18.799** bukan-pertama = 19.586 ✅ · 1.392 + **9** = 1.401 ✅ ·
18.799 − 1.401 = **17.398**; 17.284 + **114** ✅ · **19.598** = 19.586 + **12** karantina.

| kelas bentuk | semesta | dalam penyebut | selisih |
| --- | --- | --- | --- |
| awal | **48** | **45** | **3** |
| ekor | **826** | **826** | 0 |
| tengah | **6** | **6** | 0 |
| **jumlah** | **880** | **877** | **3** |

**[v19] PERINGATAN YANG BERUBAH BENTUK.** Untuk BNXUSDT selisih itu kini **terukur dan
bernama**. Untuk **786 simbol lain BELUM DIUKUR dan DILARANG DITAKSIR**. Pertanyaannya
bukan lagi "apakah dapat didamaikan" melainkan "apakah pola satu simbol ini berlaku umum".

**[v19] Yang kini terukur secara semesta, dan ini besar:** dari **787** simbol hanya
**10** punya bulan absen, berjumlah **11** bulan, **seluruhnya `gagal_gerbang`**. Jarak
antara "bulan berberkas" dan "bulan di penyebut" **bukan fenomena luas** — terpusat pada
sepuluh simbol.

## LUBANG TENGAH — POROS TUNTAS

Blob **`39cd1caacedc4d49ba23c91c80f553bb9fb135a6`**, **11.014 B**, UTUH. `waktu_utc`
**2026-07-29T09:38:52Z**. `versi_lubang_tengah` **2** · `versi_funding` **6** ·
`cacah_lubang_tengah` **6** · `selisih_lubang_tengah` **0** · ganda **0**/**0** ·
`cacah_laporan_dibaca` **8** · `cacah_per_simbol_funding` **787** · sebaran {HIDUP 0 ·
MATI **6** · SEPI 0} · `h_a010_menang` true (5–0) · `h_a011_menang` true. Sidik
`c9372bd7…b3f4e`.

Enam lubang: **BTCSTUSDT 2022-01** (399.757 B, 44.640) · **LITUSDT 2025-07** (427.922,
44.640) · **2025-08** (427.505, 44.640) · **2025-09** (392.233, 43.200) · **2025-10**
(434.201, 44.640) · **2025-11** (389.479, 43.200) — semuanya MATI.
**TIDAK SATU PUN berbulan `2022-05` atau `2024-05`.** BTCSTUSDT rentetan **1**, LITUSDT
rentetan **5**; keduanya klines **64** bulan. BTCSTUSDT terukur **KONTIGU 64**;
**keserian dengan tebing BELUM diukur dan DILARANG diklaim.**

### H-A010 MENANG 5–0 — TABEL DIPERBAIKI, KONVENSI DINYATAKAN (butir 18)

| simbol | awal lubang awal | **`akhir_lubang_awal` (medan sumber, INKLUSIF)** | `cacah_bulan_klines` | `cacah_lubang` |
| --- | --- | --- | --- | --- |
| BNXUSDT | 2022-05 | **2023-01** | 48 | 19 |
| ICPUSDT | 2021-05 | **2022-08** | 62 | 16 |
| JUPUSDT | 2024-01 | **2024-01** | 30 | 1 |
| QTUMUSDT | 2020-02 | **2020-02** | 77 | 1 |
| TLMUSDT | 2021-07 | **2023-02** | 60 | 20 |

**Vonis MENANG 5–0 TIDAK BERUBAH** — yang cacat konvensi kolom ringkasan, bukan hasil uji.

**CATATAN SILANG YANG WAJIB DITAHAN, kini BERLIPAT ENAM.** Baris BNXUSDT —
`cacah_bulan_klines` **48**, mulai **2022-05** — medan yang sama yang: (a) di v15 berpindah
menjadi nama poros "gugus 2022-05"; (b) di v16 menutup jembatan 50 lawan 48; (c) di v17
dibantah oleh **51**; (d) di v18 dibantah lagi oleh semesta rentang yang mulai **2022-04**;
**(e) di v19 TERDAMAIKAN** — 2022-04 bulan tepi, selisihnya terukur bukan cacat;
**(f) di v19 pula kolom tetangganya terbukti bergeser satu bulan.**
**Satu medan, enam pemakaian, dua di antaranya keliru sebelum diukur.**

Kendali: tiga baris **BTCUSDT** semuanya HIDUP dengan `funding_ada` true.
**Uji H-A020 dan H-A021 MUSTAHIL** — bukan mahal, **tidak ada bahannya**.

**[v19] Catatan silang baru yang WAJIB ditahan:** **LITUSDT** muncul di **tiga** tempat —
lima lubang tengah 2025-07..2025-11, tebing funding 2025-07, dan **bulan absen 2025-12**
(`gagal_gerbang`). **Keseriannya DILARANG diklaim:** tiga kemunculan satu simbol pada tiga
laporan **bukan** tiga pengamatan bebas (KC-47), dan tak satu pun diregistrasi lebih dulu
(aturan 29).

**[v19] TLMUSDT 2023-03** (defisit terbesar **42.510**; 2.130/44.640 = **95,2% kosong**)
terukur **ADA** pada semesta rentang **dan** TLMUSDT **berabsen NOL**. **Maka kekosongan
itu DIPASTIKAN soal ISI, dari dua sumber bebas.** Utang ukur 7 menyempit; tetap hidup.

## Lubang funding — agregat semesta

`cacah_simbol_ada_lubang` **122** dari 787 · awal **5** · bukan-awal **118**. BNXUSDT punya
lubang AWAL dan bukan-awal sekaligus. Lima bentuk AWAL: BNXUSDT, ICPUSDT, JUPUSDT,
QTUMUSDT, TLMUSDT. **880** semesta / **877** dalam penyebut / **3** tak dikenal. Dari 945
MATI di luar kohort: **386** kehilangan funding, **559** berfunding.

## Jumlah uji — terukur

**1377, kini DUA PULUH SATU bacaan berjejak di berkas ini.** Bacaan 1–18 tercatat di
v16–v18 dan tidak diulang. Yang baru:

19. blob **`a185f32a80471ea9f76c72415cacf3c4f06dfeda`**, run **30593086004**, commit
    **`51c65e2a`** (UKUR v18), **00:17:08Z**, kode 0, `… in 0.57s`.
20. blob **`b6835432ff25e8482781f13018c17b9f080ad510`**, run **30594157668**, commit
    **`8345668e9a8f0e01bcbe86fd9d0f60f4709fd834`** (STATE v60), **00:39:46Z**, kode 0,
    `1377 tests collected in 0.48s`.
21. blob **`87677ef656439ff30eb0c1a6788a5c324fdca702`**, run **30595169680**, commit
    **`b8877a2710544723ce81fc44ad505fa08fb7828b`** (EKOR v19), **2026-07-31T01:01:01Z**,
    kode 0, `1377 tests collected in 0.47s`.

Turunan: 1341 + **36** butir `tests/test_selisih_lilin.py` = **1377** ✅
**Rentang waktu kutip 0,40s–0,67s DILARANG dibaca sebagai pengukuran apa pun tentang
repo** — ia keadaan mesin CI, bukan besaran riset.

Riwayat: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 → 984 →
1044 → 1100 → 1168 → 1233 → 1297 → 1341 (enam run) → **1377**.
**Aturan 57: beruntun 4 dari 4** sesudah PUTUS di 26/27. Ia **mencacah, bukan menaksir**.

### Aturan 38 — ordinal, kini sampai ke-65

| ke- | CI | run | commit | blob | jejak |
| --- | --- | --- | --- | --- | --- |
| 62 | 1377 | 30592559253 | `bb565f4c` | `3f299eaf` | UKUR v18 |
| **63** | **1377** | **30593086004** | **`51c65e2a`** | **`a185f32a…`** | **STATE v60, EKOR v19** |
| **64** | **1377** | **30594157668** | **`8345668e`** | **`b6835432…`** | **EKOR v19** |
| **65** | **1377** | **30595169680** | **`b8877a27…`** | **`87677ef6…`** | **berkas ini** |

Ordinal 42–61 tercatat di v16–v18.
**Pemakaian berjalan = ke-enam puluh lima**, `commit` **COCOK pada percobaan pertama**.
**Panjang deret berjejak, aritmetika terbuka (butir 17):** ke-42..ke-65 → 65 − 42 = 23;
23 + 1 = **24 pembacaan berturut**.

### ATURAN 90 — RESMI (diresmikan di STATE v60)

> Laporan `reports/ci_terakhir.json` sah bagi sebuah push **hanya bila** medan `commit`
> cocok dengan SHA push itu. Bila tidak, laporan itu milik push sebelumnya; pembacaan
> **WAJIB diulang** dan laporan tak cocok **DILARANG dicatat**.

| kejadian | push | blob salah | `commit` terbawa | milik ke- |
| --- | --- | --- | --- | --- |
| 1 | STATE v58 | `5b433a93` | `9b01c06e` | ke-57 |
| 2 | STATE v59 | `990502c7` | `72fe177c` | ke-60 |
| 3 | EKOR v18 | `b6d02273` | `05f6f72e` | ke-61 |

**Sejak diresmikan dipakai EMPAT kali** (ke-62..ke-65) dan **tidak sekali pun menangkap
laporan salah**. **DILARANG menyebut aturan 90 "teruji"** — aturan yang belum pernah
menyala bukan aturan yang terbukti, hanya aturan yang belum diuji.

**Bot CI** menambah satu commit di atas tiap push pemicu — deterministik, **DILARANG
dihitung kemenangan**. Terbaru `4bf883c433d492fa76f84707dec6320162ec61c0` (EKOR v19).
**Push `journal/**` dan `decisions/**` TIDAK menyalakan CI** — jurnal 148–151 tanpa commit
bot, terukur dari `paths-ignore`.

**Dua cacat tetap disebut:** ke-**38** (run `30541051907`, commit `5d7d8b96`) **tanpa
blob**; run **30547842823** (bot `de2fc03d`) tertimpa, **DILARANG dihitung**.

## Modul, workflow, dan berkas uji

**CACAH TANGAN sah** (aturan 66), ref `3196fd98` / `8a614567`: `lux_ai/serapan/` **49** ·
`tests/` **53** · `.github/workflows/` **44** · akar **18**. **50 / 54 / 45 TURUNAN dan
DILARANG dikutip terukur.**
**PERINGATAN DUA CACAH `tests/`:** repo WARISAN **34**, repo riset ini **53**. Menyebut
"cacah uji" tanpa menyebut repo-nya **DILARANG**.

**Peringatan dini aturan 48:** `silang_funding.py` **29.873 B / 705 baris** (sisa **95**)
· `funding.py` **28.121** · `sisa_defisit.py` **25.949** · `semesta_kuota.py` **24.987** ·
`lubang_tengah.py` V2 **23.745**.

**Blob modul yang berubah status di v19:**
**`lubang_awal.py` `8c36943da222dfa262b3b9f2117bf72dc801681d` (DIBACA UTUH —
`BATAS_BARIS_LAPORAN = 60`)** · **`bulan_absen.py` `10279d721d66a86b6d265badf81ada3204648f69`
(DIBACA UTUH — TANPA pembatas baris)** · `gerbang_1m.py`
`c8cc54c84a57173ef2e426c317d6ac50734e9b4a` (DIBACA UTUH, pustaka murni).
Blob modul lainnya **tidak berubah** — dirujuk ke v18.

**TIDAK ADA modul yang diketahui menulis `reports/semesta_rentang.json`** (utang ukur 22).

`ci.yml` = **`c79497b2c812679eaa69aee5b3160eac9f5c5fb7`** (paths-ignore `journal/**`,
`decisions/**`, `hipotesis/**`, `reports/**`). `karantina_semesta.yml` = `de40fa4e`
(**belum dibaca utuh**).

Cacah per berkas uji — **repo riset ini**: `test_irisan_byte.py` **68** ·
`test_bulan_pertama.py` **65** · `test_keterisian_lilin.py` **64** ·
`test_bentangan_kohort.py` V2 **63** · `test_lubang_tebing.py` **60** ·
`test_sebab_bangkit.py` **57** · `test_byte_semesta.py` **56** · `test_lubang_awal.py`
**48** · `test_tersisip_semesta.py` **47** · `test_anatomi_tengah.py` **47** ·
`test_sisa_defisit.py` **44** · `test_selisih_lilin.py` **36** · `test_terhenti.py` V4
**33** · `test_bulan_absen.py` **32** · `test_karantina_semesta.py` **28** ·
`test_silang_settled.py` **24** · `test_ukur_baris.py` **3**.
**`test_lubang_tengah.py` — 56 menurut R-228, BELUM DIBACA, DILARANG dikutip terukur.**
**`test_gerbang_1m.py` — BELUM DIBACA; cacah TIDAK DIKETAHUI. [v19] PERINGKATNYA NAIK KE
ATAS:** ia penjaga salinan rumus gerbang, dan utang ukur 25 tak dapat dibayar tanpanya.

## API — dua modul baru di v19

**`bulan_absen` V1** (`10279d72…`, DIBACA UTUH): `VERSI = 1` ·
`KELUARAN="reports/bulan_absen.json"` ·
`KELUARAN_RINGKAS="reports/bulan_absen_ringkas.json"` · `PENYEBUT_TERCATAT=19586` ·
`NAMA_PENYEBUT_TERCATAT=787` · `KENDALI_NAMA=("BTCUSDT","ETHUSDT")` ·
`KENDALI_BULAN_MIN=60` · `ABSEN_PASANGAN_JURNAL_113=12` · **`R288_BNX_ABSEN=3`** ·
`R288_SAMA_MIN=7` · `R288_JUMLAH_SEMESTA=12` ·
`PEMBEDA=("gagal_gerbang","tak_diterbitkan_arsip","tak_terukur")`.
**TIDAK ADA pembatas baris.** Docstring memuat praregistrasi **R-288**, menyebut **R-290**;
keduanya **belum diadjudikasi**. **`R288_BNX_ABSEN = 3` adalah tetapan ramalan, bukan
pengukuran.**

**`lubang_awal` V1** (`8c36943d…`, DIBACA UTUH): **`BATAS_BARIS_LAPORAN = 60`** ·
`R305_PITA_BUTIR_1=(0.55,0.95)` · `R305_MINIMAL_PENYEBUT_BUTIR_1=100` ·
`R305_PITA_BUTIR_2_CACAH=(20,120)` · `R305_MINIMAL_BAGIAN_BUTIR_2=0.80`. `cacah_bulan` =
`len(urut)` atas penyebut 19.586 → **sebab `bagian_butir_1` tautologis 1.0**. Medan
`mati_tidak_setelah_lubang_bukan_awal` memakai `<=` → **DILARANG untuk klaim arah**
(aturan 80). Docstring memuat **praregistrasi R-305**.

API modul lain **tidak berubah** — dirujuk ke v18 (`11b14975a…`).

## Hipotesis

H-A001 belum diuji · H-A002b GUGUR · H-A003 MENANG pada 3, GUGUR pada 9 · H-A004 tak
dapat diuji · H-A005 GUGUR · H-A006 MENANG enam run · H-A008 MENANG dua kali · H-A009
GUGUR · **H-A010 MENANG 5–0** (tabel pendukung dikoreksi konvensinya, vonis tetap) ·
**H-A011 TERBUKTI** · H-A012 MENANG · H-A013 MENANG 6–0 TAFSIR DICABUT · H-A014 MENANG
9 dari 9 · H-A015 DIBATASI sebagai tafsir (KC-45) · H-A016 PENGAMATAN, BELUM DIUJI ·
**H-A017** DICABUT sebagai pola semesta (tinggal 1 simbol) · **H-A018** BOLEH: "bulan MATI
menempati bagian KECIL byte semesta (**0,0177**) dan rata ≈4,3× lebih kecil"; DILARANG:
"berkas kecil berarti pasar mati" · **H-A019** DITERIMA TERBATAS, dilemahkan ADR-A018
kep. 6 · **H-A020, H-A021** uji **MUSTAHIL** · **H-A022 TERBUKTI** lewat R-313 (identitas
himpunan, bukan sebab).

**H-A023 [DIUSULKAN — BERSYARAT dengan ARITMETIKA TERTUTUP].** *Selisih 51 − 48 = 3 pada
BNXUSDT dan `cacah_lubang_tak_dikenal` = 3 menunjuk himpunan simbol-bulan yang sama.*
**TERUKUR dan menutup:** ketiga bulan **BERNAMA** — 2022-04 (tepi), 2022-06 dan 2022-08
(di dalam, `gagal_gerbang`); 51−50 = 1, 50−48 = 2, 1+2 = 3 ✅; nama itu **sama persis**
dengan ketiga `lubang_tak_dikenal`.
**TETAP BERSYARAT:** keanggotaan penyebut diukur untuk **SATU** simbol; untuk 786 lainnya
kesamaan cacah **belum** terbukti kesamaan identitas.
**DILARANG ditulis TERBUKTI.** Kenaikan v18→v19 adalah dari "arah konsisten" menjadi
"aritmetika tertutup pada satu simbol" — **bukan** menjadi terbukti.

## Aturan 87 dan 90 RESMI; usulan 88, 89, 91, 92

**Aturan 87 [RESMI].** Butir ramalan **turunan** wajib ditandai TURUNAN; kemenangannya
wajib diperkecil sendiri; kekalahannya dihitung penuh. **[v19] Ditaati:** butir 4 R-318
(`rentang` = 50) ditandai TURUNAN di praregistrasi dan kemenangannya diperkecil sendiri.

**Aturan 90 [RESMI].** Diuraikan penuh di atas.

**Usulan aturan 88 [DITAHAN].** Ramalan keseragaman tanpa mekanisme tertulis wajib ditulis
sebagai **sebaran**. **TIDAK bertambah** — tetap satu kejadian.

**Usulan aturan 89 [DITAHAN].** Setiap pita ramalan wajib menutup **ketiga sisi** ruang
nilainya, atau menyatakan mengapa satu sisi mustahil. **[v19] MANFAATNYA kini TERUKUR** —
pita butir 1 R-318 ditulis tiga sisi padahal sisi "lebih" tampak mustahil, dan sisi itu
**nyaris terpakai** (tetapan kode meramalkan 3). **Tetapi CACAT yang melahirkannya masih
SATU.** Meresmikan atas dasar **manfaat** alih-alih **cacat berulang** adalah **perubahan
kebijakan** — **wewenang ADR-A022**, bukan wewenang lampiran ini.

**Usulan aturan 91 [BARU v19, DITAHAN].** *Ramalan yang butir-butirnya diturunkan dari
**satu aritmetika yang sama** wajib menyatakannya di praregistrasi, dan kemenangan
butir-butir itu DILARANG dijumlahkan sebagai bukti bebas.*
**Dasar:** butir 1, 3, dan 4 R-318 semuanya turun dari bentangan 50 dan 50 − 48 = 2 —
**berkorelasi kuat, bukan tiga bukti bebas**; bila aritmetika itu salah, ketiganya jatuh
bersama. Ini **KC-47 dalam bentuk paling menggoda: satu perhitungan menyamar sebagai
banyak ramalan**. **TIDAK diresmikan** — satu kejadian (ADR-A019 kep. 3).

**Usulan aturan 92 [BARU v19, DITAHAN].** Diuraikan pada kesalahan dokumen butir 19.

**Catatan kejujuran atas keempat usulan.** Empat usulan aturan menganggur bersamaan
(88, 89, 91, 92) ditambah tiga usulan KC (56, 57, 58). **Menumpuknya usulan bukan tanda
kedisiplinan otomatis** — ia dapat menjadi cara halus menunda keputusan. **ADR-A022
WAJIB memutuskan seluruhnya**, meresmikan atau membuang; membiarkannya menggantung satu
ADR lagi wajib dicatat sebagai **cacat proses**.

## UTANG UKUR — daftar penuh

**LUNAS di v19:**

- **Utang ukur 18 LUNAS** — `gerbang_1m.py` dibaca UTUH; enam klausa bernama; terbukti
  **pustaka murni**.
- **Utang ukur 20 LUNAS** — jembatan 51 lawan 48 tertutup: 51−50 = 1 (tepi 2022-04),
  50−48 = 2 (2022-06 dan 2022-08), jumlah **3**.
- **Utang ukur 23 LUNAS** — ketiga bulan `lubang_tak_dikenal` **bernama** dan posisinya
  terhadap penyebut terjelaskan tanpa sisa.
- **Utang ukur 24 LUNAS** — apakah bulan-bulan di luar penyebut punya sebab terukur:
  **YA**, `pembeda_absen` = **`gagal_gerbang`** untuk sebelas dari sebelas.

**MENYEMPIT tetapi HIDUP:** utang ukur **6** (definisi bulan pertama lawan kelahiran
bursa — terukur untuk satu simbol) · **7** (sebab kekosongan TLMUSDT 2023-03 — kini
dipastikan soal **ISI**, sebab isinya belum diukur).

**HIDUP, tidak bergerak:** **17** (cacah total `baris_mati`, terpotong 54%) · **19**
(identitas 12 karantina) · **21** (5% `semesta_rentang.json` yang hilang) · **22** (modul
penulis `semesta_rentang.json`) · utang lama **1–5**, **8–16** sebagaimana tercatat di v18.

**LAHIR di v19:**

- **UTANG UKUR 25 [POROS PERINGKAT SATU].** *Klausa mana dari enam klausa `gerbang_1m.py`
  yang menolak **BNXUSDT 2022-06** dan **BNXUSDT 2022-08**?* Terukur hanya **bahwa**
  pembedanya `gagal_gerbang`. Karena `gerbang_1m.py` **pustaka murni**, utang ini
  **TIDAK dapat dibayar dengan membaca laporan mana pun** — ia **menuntut pemanggilnya
  ditelusuri**. Bahan: **ADR-A004 §2** (peringkat bacaan tertinggi),
  `tests/test_gerbang_1m.py` (peringkat NAIK).
  **LARANGAN AKTIF sampai lunas:** DILARANG menyatakan klausa mana pun yang menjatuhkan
  kedua bulan itu.
- **UTANG UKUR 26.** *Apakah pola BNXUSDT (bulan berberkas → gugur gerbang → keluar
  penyebut) berlaku bagi 786 simbol lain?* Sampai diukur, **DILARANG** digeneralkan.

## Penomoran berikutnya

jurnal **152** · STATE **v61** · EKOR **v20** · UKUR **v20** · PROMPT **v55** · ADR
**A022** · KC **KC-59** (KC-56, KC-57, KC-58 usulan; KC-16 kosong selamanya) · aturan
**93** (usulan 77, 78, 82, 88, 89, 91, 92; resmi 1–81, 83, 84, 85, 86 a/b, 87, 90) ·
hipotesis **H-A024** · ramalan **R-319** · **papan skor 329 — SAH sejak EKOR v19, wajib
disalin ke STATE v61** · aturan 52 berikutnya **ke-35** · aturan 38 berikutnya **ke-66** ·
kesalahan dokumen berikutnya butir **20** · koreksi UKUR berikutnya **17** · utang ukur
berikutnya **27** · utang verifikasi berikutnya **48**.

## Syarat praregistrasi R-319 — LIMA BELAS SYARAT KUMULATIF

1. Diregistrasi di jurnal **sebelum** bahan dibuka (aturan 29).
2. Adjudikasi pada **giliran berbeda** dari praregistrasi.
3. Bahan **DILARANG** berupa berkas yang sudah dibuka pada sesi ini:
   `semesta_rentang.json`, `semesta_bulan_1m.json`, `gerbang_1m.py`,
   `silang_funding.json`, `lubang_awal.json`, `bulan_absen_ringkas.json`,
   `lubang_awal.py`, `bulan_absen.py`.
4. Setiap butir **MUDAH** ditandai MUDAH dan **tidak masuk papan skor**.
5. Setiap butir **TURUNAN** ditandai TURUNAN (aturan 87); kemenangannya diperkecil sendiri.
6. Pita ditulis **tiga sisi** bila ruang nilainya tiga sisi (KC-55; usulan aturan 89).
7. Syarat gugur ditulis **eksplisit dan bernomor**, diperiksa **sebelum** angka apa pun
   dibaca.
8. Ramalan keseragaman ditulis sebagai **sebaran** (usulan aturan 88).
9. Kendali positif disebut namanya.
10. **Modul penulis laporan dibaca lebih dulu** (aturan 86 b) — dan **keberadaan pembatas
    baris dinyatakan tersurat**.
11. Definisi tiap medan **disalin verbatim** sebelum ditafsirkan (KC-54).
12. Simbol **kedua** diperiksa sebelum definisi medan ditulis (Koreksi 15).
13. Setiap kolom tabel susunan tangan menyebut **medan sumber dan konvensinya**
    (butir 18; usulan KC-57).
14. Setiap panjang deret ditulis dengan aritmetika **`akhir − awal + 1`** terbuka
    (butir 17).
15. **[BARU v19]** Bila beberapa butir turun dari **satu aritmetika yang sama**, hal itu
    **dinyatakan di praregistrasi** dan kemenangannya **DILARANG dijumlahkan sebagai bukti
    bebas** (usulan aturan 91).

— akhir `STATE_LAMPIRAN_UKUR.md` v19 —
