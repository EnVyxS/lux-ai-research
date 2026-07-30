# STATE — versi 57 (bagian 1 dari tiga)

Diperbarui: 2026-07-30 (UTC; jam lokal Asia/Jakarta 2026-07-31 pagi — perbedaan itu
sendiri kini tercatat sebagai kesalahan dokumen butir 15). Aturan hanya BERTAMBAH;
jangan menulis ulang dari ingatan. v57 disusun di atas `STATE.md` v56 (blob
**`3ac9c3698583b2e528015a5d36bfb9aa1cc3bd0c`**, commit `019d16ea`), yang **DIBACA UTUH
pada giliran ini sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43), bersama EKOR
v15, UKUR v15, jurnal 144, jurnal 145, dan ADR-A021.

**Apa yang v57 kerjakan, tersurat:** ia menyerap **ADR-A021** — yang meresmikan hasil
**R-315 (1 TEPAT / 1 MELESET / 1 tidak diskor)**, **mencabut** bacaan lama atas
`lubang_tak_dikenal`, meresmikan **KC-54**, meresmikan **aturan 87**, dan mengusulkan
**aturan 88**. Papan skor naik dari 316 ke **318**. Ia mencatat **`sidik_kode_funding`
baru** yang belum pernah tertulis di dokumen mana pun. Daftar kesalahan dokumen
bertambah dua butir sekaligus, **14** dan **15**, keduanya kesalahan kami sendiri.
Ordinal aturan 38 berdiri di **ke-54**.

**Kalimat yang wajib dibaca lebih dulu:** giliran-giliran terakhir memenangkan butir
bernomor dan mengalahkan butir biner. R-315 kalah pada butir yang **dipercaya dari
gambaran sendiri tentang arti sebuah nama medan**. Tidak ada siapa pun yang bisa
disalahkan untuk kekalahan itu, dan karena itu ia yang paling mahal.

## KESERASIAN VERSI — TIDAK SERASI; v57 / v15 / v15

1. `STATE.md` **v57** — berkas ini. Aturan 1–81, 83, 84, 85, 86 (a dan b), **87**;
   KC-1..**KC-54**.
2. `STATE_LAMPIRAN_EKOR.md` **v15** — blob
   **`e3fd04c267b702b308e50110b5b7f697b6bbf80d`**, commit
   **`94c7d9da8babdf586ae3f821a13781321a7fd40d`**. **TERTINGGAL SATU VERSI** begitu
   berkas ini didorong. Kepalanya berbunyi "milik STATE v56". Ia belum memuat R-315,
   ADR-A021, KC-54, aturan 87 resmi, usulan aturan 88, maupun papan skor 318.
3. `STATE_LAMPIRAN_UKUR.md` **v15** — blob
   **`0768d497812e6e39269ebc74cca75ee0fb89fe25`**, commit
   **`d551f4712aa8719de87188ed4a33dd89914a20cb`**. **TERTINGGAL SATU VERSI** dengan
   alasan yang sama.
4. `STATE_LAMPIRAN_ADR.md` (`a02ef271`) dan **`PROMPT_KELANJUTAN.md`** (`35beed44`) —
   **arsip; BUKAN sumber** (ADR-A018 kep. 9).

**PERINGATAN KESERASIAN.** Keserasian penuh v56 / v15 / v15 yang dicatat jurnal 144 §2
**pecah begitu berkas ini didorong**, dan itu **harga yang disengaja** (satu berkas per
push, KC-42). Bila EKOR v15 atau UKUR v15 bertentangan dengan berkas ini pada **R-315,
ADR-A021, KC-54, aturan 87, usulan aturan 88, pencabutan bacaan `lubang_tak_dikenal`,
`sidik_kode_funding`, atau papan skor 318**, **berkas ini yang menang** — pengecualian
tersurat atas KC-41 yang berlaku HANYA untuk butir yang v57 nyatakan baru. Untuk segala
hal lain, KC-41 tetap penuh: **berkas SUMBER menang**.

Keserasian **wajib dipulihkan** lewat **EKOR v16** dan **UKUR v16** pada giliran-giliran
berikutnya.

**Tentang push berkas ini:** ia di akar repo sehingga menyalakan `ci.yml`. Tidak satu
pun `tests/**` berubah, jadi cacah uji tetap **1377** — ramalan **deterministik**
(aturan 57), **MUDAH**, TIDAK diskor, TIDAK menambah beruntun. **Laporannya WAJIB
dibaca sebelum push akar berikutnya** (aturan 38, pemakaian **ke-55**), atau ia hangus
seperti run `30547842823`. Bot CI akan menambah satu commit di atas push ini —
deterministik dari `ci.yml`, **DILARANG** dihitung sebagai kemenangan ramalan.

## STATE DIPECAH TIGA — BACA INI LEBIH DULU

1. **`STATE.md`** (berkas ini) — **bagian 1**: kepala, aturan bernomor 1–**87** (plus
   usulan 77, 78, 82, **88**), kelas cacat KC-1..**KC-54**.
2. **`STATE_LAMPIRAN_EKOR.md`** — **bagian 2**: papan skor per ramalan, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** — **bagian 3**: penyebut 787, taksonomi, karantina,
   bulan ABSEN, hipotesis H-A001..H-A022, lubang funding, byte parquet semesta,
   modul/workflow/uji, API terverifikasi.

**Ketiga berkas wajib dibaca bersama.** LANGKAH 0 PROMPT wajib menyebut ketiganya.

## CACAH TANGAN DIREKTORI — UTANG HIDUP

| direktori | cacah TERUKUR (tangan, bernomor) | ref |
| --- | --- | --- |
| `lux_ai/serapan/` (`.py`, termasuk `__init__.py`) | **49** | `3196fd98` / `8a614567` |
| `tests/` | **53** | idem |
| `.github/workflows/` | **44** | idem |
| akar repo | **18** entri (**6** direktori + **12** berkas) | idem |

**[v57] UTANG ATURAN 66 TETAP HIDUP.** Angka harapan **50 / 54 / 45** tetap **TURUNAN**
dan **DILARANG dikutip sebagai terukur** (ADR-A019 kep. 8). Tidak ada modul baru yang
dinamai sejak v56, sehingga utang ini tidak bertambah — tetapi juga tidak berkurang.

**LARANGAN (ADR-A018 kep. 10) — DUA CACAH `tests/` DILARANG DICAMPUR.**
`PETA_MODUL_BERKAS.md` (`3abe95f6`) mencatat **34** berkas uji milik repo **WARISAN
`bot_v8`**; repo riset ini punya **53**. **Menyebut "cacah uji" tanpa menyebut repo-nya
DILARANG.**

## PERINGATAN DINI ATURAN 48 — besar modul

`silang_funding.py` **29.873 B / 705 baris** (pagar 800 → jarak **95**) · `funding.py`
**28.121** · `sisa_defisit.py` **25.949** · `semesta_kuota.py` **24.987** ·
`lubang_tengah.py` **23.745** · `keterisian_lilin.py` **22.291** · `kehidupan_arsip.py`
**19.281** · `pulihkan.py` **14.839**. **Bila `sisa_defisit` V2 atau `silang_funding`
V3 diperlukan, pecah lebih dulu.**

## KESALAHAN DOKUMEN SENDIRI — kini LIMA BELAS

| # | berkas | tertulis | seharusnya | status |
| --- | --- | --- | --- | --- |
| 1 | jurnal 132 §3 | "beruntun 2/1" | 2/2 | LUNAS di STATE v50 |
| 2 | EKOR v10 | `terisi ≉ 49,7%` | `≈ 49,7%` | LUNAS di EKOR v11 |
| 3 | jurnal 135 §13.3 | "hendan dirumuskan" | "hendak" | LUNAS di STATE v51 |
| 4 | EKOR v11 kepala | "deretministik" | "deterministik" | LUNAS di EKOR v12 |
| 5 | UKUR v11 kepala | "KESERAIAN VERSI" | "KESERASIAN VERSI" | LUNAS di UKUR v12 |
| 6 | UKUR v11 daftar uji | penanda `**` tak berpasangan | berpasangan | LUNAS di UKUR v12 |
| 7 | STATE v52 | "Empat salah ketik" | "Enam" | LUNAS di STATE v53 |
| 8 | STATE v53 aturan 45 | "empat push terakhir" lalu mendaftar ENAM | "enam push terakhir" | LUNAS di STATE v54 |
| 9 | STATE v53 aturan 52 | pembacaan ulang "tidak menangkap satu pun" | satu dari delapan | LUNAS di STATE v54 |
| 10 | jurnal 138 §5 butir 2 | "maka 839.842.134 yang keliru" | kesimpulan tidak sah dari premis benar | LUNAS di jurnal 140 |
| 11 | jurnal 141 §6 | tuduhan terhadap EKOR v13 dan ADR-A019 | terlalu luas; STATE v54 BEBAS | LUNAS di STATE v55 |
| 12 | ADR-A019 kep. 9 | poros karantina "termurah"; poros "gugus 2022-05/2024-05" | manifes **20.533.802 B**; bulan sebenarnya **2022-01** dan **2025-07..11** | LUNAS di ADR-A020 kep. 8 dan STATE v56 |
| 13 | jurnal 142 §4 | irisan 880/877 disajikan seolah seluruhnya baru | **880 / 877 / 3 sudah tertulis di STATE v55**; yang baru hanya letak selisih di kelas AWAL | LUNAS di STATE v56 |
| **14** | **STATE v56, keserasian nomor 2** | blob EKOR v14 ditulis berbelit: "blob `a722ec63…` salah; blob yang benar `5d481f9b…` (commit `a722ec63`)" | **commit tertukar dengan blob lalu dikoreksi di tempat**, bukan ditulis bersih sejak awal | **LUNAS di berkas ini** |
| **15** | **ringkasan giliran sebelum jurnal 144** | nama berkas jurnal ditulis `journal/2026-07-31-144.md` | konvensi repo memakai **tanggal UTC**; yang benar **`journal/2026-07-30-144.md`** | **LUNAS di berkas ini** |

### Butir 14 — cara menulis blob yang merusak keterbacaan

STATE v56 menuliskan keserasian EKOR v14 dengan mengoreksi dirinya sendiri di tengah
kalimat: sebuah **commit** disebut lebih dulu sebagai blob, lalu dibantah pada baris
yang sama. Angkanya tidak salah, tetapi pembaca berikutnya dipaksa mengurai koreksi
alih-alih membaca fakta. **Aturan yang dipegang mulai sekarang:** blob dan commit
ditulis pada kolom yang berbeda, dan bila sebuah nilai keliru, ia **ditulis ulang
bersih**, bukan dibantah di tempat.

### Butir 15 — jam lokal dipakai untuk konvensi berbasis UTC

Nama berkas jurnal disusun dari jam lokal **Asia/Jakarta** (31 Juli dini hari) padahal
konvensi repo memakai **tanggal UTC** (saat itu masih 30 Juli; commit terakhir
`c4a7468e` bertanggal 2026-07-30T21:55:58Z). Nama yang benar dan dipakai:
**`journal/2026-07-30-144.md`** dan **`journal/2026-07-30-145.md`**.

Kelasnya sama dengan Koreksi 11 UKUR v15 dan dengan **KC-54** yang diresmikan berkas
ini: **label yang terdengar masuk akal atas medan yang benar**. Zona waktu adalah medan;
namanya bukan definisinya.

## R-315 — ADJUDIKASI RESMI: 1 TEPAT / 1 MELESET / 1 TIDAK DISKOR

Praregistrasi: jurnal 144 (`journal/2026-07-30-144.md`, blob
**`fcc9374529fd91bd1c9a3d43c34b7f24a86d344e`**, commit `1146b96a`), ditulis **sebelum**
bahannya dibuka. Adjudikasi: jurnal 145 (blob
**`d9b63433e6693a5e012ed14eec1ecc8e9b740e21`**, commit `526e41e8`), pada giliran yang
**berbeda** (ADR-A016 TERPENUHI, aturan 79 DITAATI PENUH — kedua kalinya berturut
sesudah R-314).

Bahan: **`reports/silang_funding.json`**, blob
**`b61fe8b3bcabbfce435dd5e5f78fc367f6bef617`**, `waktu_utc` **2026-07-29T08:17:55Z**.

### Isi larik `lubang_tak_dikenal` — tepat tiga butir, semuanya BNXUSDT

| # | simbol | bulan lubang | `bulan_klines_pertama` | `bulan_klines_terakhir` | `cacah_bulan_klines_simbol` |
| --- | --- | --- | --- | --- | --- |
| 1 | BNXUSDT | **2022-04** | 2022-05 | 2026-06 | 48 |
| 2 | BNXUSDT | **2022-06** | 2022-05 | 2026-06 | 48 |
| 3 | BNXUSDT | **2022-08** | 2022-05 | 2026-06 | 48 |

### Vonis

| butir | sifat | ramalan | terukur | hasil |
| --- | --- | --- | --- | --- |
| 1 | BERISIKO · MURNI · titik tunggal | cacah simbol berbeda pemilik ketiga lubang tak dikenal = **1** | **1** (BNXUSDT) | **TEPAT** |
| 2 | BERISIKO · MURNI · biner | **ketiga** lubang berbulan lebih awal daripada `bulan_klines_pertama` | **1 dari 3** | **MELESET** |
| 3 | MUDAH | laporan terbaca; `sidik_kode` cocok; penyebut 19.586; lubang semesta 880 | keempatnya cocok | terpenuhi, **tidak masuk lajur** |

**Kekalahan butir 2 ditulis telanjang: diramalkan 3 dari 3, terukur 1 dari 3.**
2022-06 dan 2022-08 duduk **sesudah** 2022-05, yakni **di dalam** rentang klines
simbolnya. **Vonis ini FINAL dan DILARANG ditulis ulang sebagai SEPARUH di dokumen mana
pun** (ADR-A021 kep. 1).

**Syarat gugur (e) MENYALA** — ketiganya milik BNXUSDT, simbol yang sudah lebih dulu
dikenal berlubang AWAL dan bukan-AWAL sekaligus. Sesuai yang dikunci di muka,
**kesamaan itu DILARANG dibaca sebagai konfirmasi apa pun**: bahan yang sama sudah
menghasilkan fakta lama itu.

**Pengecilan kemenangan butir 1, ditulis sendiri (aturan 87):** cacah **3** sudah
tercatat pada konstanta `LUBANG_TAK_DIKENAL_TERCATAT`. Yang benar-benar diramalkan
hanyalah "ketiga lubang itu satu pemilik" — **kemenangan sempit, satu bit**.

## PENCABUTAN — "lubang di luar penyebut = bulan sebelum simbol lahir"

Selama tiga dokumen (STATE v55, STATE v56, UKUR v15) istilah `lubang_tak_dikenal`
dibaca seolah berarti "lubang funding pada bulan sebelum simbol muncul". **Bacaan itu
DICABUT** (ADR-A021 kep. 2).

> **Yang benar, dari `catatan_penyebut` laporan sendiri:** lubang tak dikenal adalah
> lubang funding yang **jatuh di luar penyebut 19.586**, sehingga tidak dibuang
> melainkan dicacah terpisah (aturan 30, 44). **Tidak ada satu kata pun tentang arah
> waktu.**

Dua dari tiga lubang membuktikannya. Setiap kalimat lama yang memakai bacaan lama
**wajib diperlakukan sebagai dicabut**, di berkas mana pun ia masih tertulis, termasuk
UKUR v15 sampai UKUR v16 naik.

## Aturan bernomor

Aturan **1–36** berlaku tanpa perubahan; teks di STATE v19 (`e06c486e`), ringkas di v37
(`f520d5e2`).

**Aturan 10. [v57] Ditaati** — tidak ada kalimat sebab yang ditulis atas BNXUSDT.

**Aturan 21 (total papan skor dihitung tangan). [v57] LAJUR BERGERAK.** Rincian baru:
TEPAT **221** · MELESET **59** · SEPARUH **22** · TIDAK TERADJUDIKASI **9** · MENUNGGU
**7**. Aritmetika tangan: 221 + 59 = 280; 280 + 22 = 302; 302 + 9 = 311; 311 + 7 =
**318**. Pertambahan dari 316: **TEPAT +1, MELESET +1**, seluruhnya dari R-315.
N_percobaan = 0. **ADJUDIKASI RISET TETAP TERKUNCI.** MENUNGGU: R-7, R-19, R-20, R-28,
R-36, R-37, R-199 — **tidak berubah**, sebab R-315 tidak pernah sempat tercatat
menunggu (praregistrasi dan adjudikasi berjarak satu giliran).

**Papan skor 318 belum SAH** sampai ia masuk lajur **EKOR v16**. Angka di berkas ini
adalah pencatatan aturan 21, bukan pengesahan lajur.

**R-229 dan R-230 TIDAK masuk lajur ini** (ADR-A020 kep. 5); kolom terpisah di EKOR.

**Aturan 29. [v57] Ditaati:** pita dan bunyi ketiga butir R-315 tidak disentuh sesudah
pengukuran; butir 2 dibiarkan kalah dalam bentuk aslinya yang biner.

**Aturan 30, 44. [v57] Dikutip langsung** sebagai dasar definisi lubang tak dikenal.

**Aturan 36. [v57] Kasus ketiga tercatat, dan ia pembukuan, bukan pengukuran baru:**
dua jalur berbeda dalam satu laporan bertemu di 880 — `tabel_silang` kolom
`funding_hilang` (33 + 842 + 2 + 0 = **877**) + **3** tak dikenal, dan
`bentuk_terbitan_funding` 48 AWAL lawan `sebaran_bentuk_semua_lubang` 45 AWAL. Kasus
terkuat tetap yang pertama (`selisih_lilin` dan `pulihkan` bertemu di 839.325.999).

Aturan **37, 39–44, 47, 49, 51, 53, 54, 56, 59–62** berlaku tanpa perubahan; ringkas
satu baris: 37 kelas cacat pada sampel · 39 keseragaman sampel bukan ramalan · 40 uji
silang baris · 41 penyebut nol → TIDAK TERADJUDIKASI · 42 kelas cacat butuh angka
terukur · 43 toleransi berskala · 44 ramalan menyebut penyebut · 47 satuan cacah
tersurat · 49 re-export mematahkan uji · 51 jendela mundur adaptif · 53 ramalan kode
keluar butuh pembacaan perilaku · 54 cacah `def test_` satu per satu · 56 commit
BERIKUTNYA yang menyentuh X · 59 ketiadaan gejala butuh penyebut · 60 mekanisme tak
dipindah antarkasus · 61 medan tak dipindah antarjalur · 62 daftar tak diminta dari
laporan bercacah.

Yang berikut memuat angka atau daftar kepatuhan:

38. Cacah uji hanya sah dari `reports/ci_terakhir.json`. **[v57] Ditaati; ordinal
    berdiri di ke-54.**

    | ke- | CI | run | commit | blob |
    | --- | --- | --- | --- | --- |
    | 50 | 1377 | 30580133552 | `a722ec63` | `04bfa2ed` |
    | 51 | 1377 | 30581703827 | `6157586e` | `aeb4315a` |
    | 52 | 1377 | 30583686515 | `019d16ea` | `19785af1` |
    | 53 | 1377 | 30584737431 | `94c7d9da` | `5f4282f6` |
    | **54** | **1377** | **30585269231** | **`d551f471`** | **`340c3c7f425d49859e6ae659cca38d0ee7770aaa`** |

    Pemakaian ke-54 dibaca pada ref pasca-`c4a7468e`, `waktu_utc`
    **2026-07-30T21:55:58Z**, kode keluar **0**, `1377 tests collected in 0.60s`, atas
    push UKUR v15. **[v57] Empat belas pembacaan berturut (ke-42..ke-54) tanpa satu pun
    laporan hangus.**
    **Ke-55 lahir pada push berkas ini** dan **wajib dibaca sebelum push akar
    berikutnya**. Jurnal 144, jurnal 145, dan ADR-A021 **tidak** menyalakan CI
    (`journal/**` dan `decisions/**` ada di `paths-ignore`), sehingga tidak ada utang
    laporan yang lahir dari ketiganya.
    **Dua cacat lama tetap disebut:** **(a)** ke-**38** (run `30541051907`, CI 1297,
    commit `5d7d8b96`) **tanpa blob**; **(b)** run **30547842823** (bot `de2fc03d`)
    **tidak pernah dibaca**, tertimpa, **DILARANG dihitung**.
    **Calon aturan** "dua push akar berturut tanpa membaca laporan" **tetap DITOLAK
    diresmikan**: masih **satu** kejadian.
45. Keatomikan push pemicu. **[v57]** Tidak ada push pemicu baru sejak trio `c1dc0009`.
46. Kode dilarang menyimpulkan dari penyebut nol. **[v57]** Tidak mendapat kasus baru;
    ketiga kasus lama tetap berdiri.
47. Satuan cacah tersurat. **[v57] Ditaati.** Tambahan v57: **"3"** bersatuan
    **simbol-bulan berlubang funding di luar penyebut 19.586** — bukan "bulan sebelum
    lahir", bukan "simbol"; **"1"** pada butir 1 R-315 bersatuan **simbol berbeda
    pemilik ketiga lubang itu**; **"318"** bersatuan **butir ramalan teradjudikasi**;
    **"54"** pada aturan 38 bersatuan **pemakaian berjejak**.
48. Berkas modul mendekati 800 baris dipecah. **[v57] PERINGATAN DINI berlanjut**;
    `silang_funding.py` V2 tinggal berjarak **95** baris dari pagar.
50. Pengukuran dari KETIADAAN wajib memuat kendali positif. **[v57] Ditaati pada
    `silang_funding.json`:** kendali tiga baris BTCUSDT (2021-01, 2021-05, 2021-08)
    semuanya HIDUP dengan `funding_ada` true; `kendali_sah` **true**.
52. Laporan yang tidak dapat dibaca utuh setara dengan laporan yang tidak ada.
    **[v57] Ditaati enam belas kali berturut** hingga ADR-A021, dan **tujuh belas kali**
    bila pembacaan ulang berkas ini pada giliran yang sama ikut dihitung.
    **[v57] Blob baru yang tercatat pertama kali:** `journal/2026-07-30-144.md`
    **`fcc9374529fd91bd1c9a3d43c34b7f24a86d344e`** · `journal/2026-07-30-145.md`
    **`d9b63433e6693a5e012ed14eec1ecc8e9b740e21`** · `decisions/ADR-A021.md`
    **`3e756672ca355ea976bf2931d278e37fe9057d0d`** · `reports/ci_terakhir.json` ke-54
    **`340c3c7f425d49859e6ae659cca38d0ee7770aaa`**.
    **[v57] BATAS BARU YANG WAJIB DIINGAT:** `reports/silang_funding.json` **TIDAK
    terbaca utuh** — hasil alat terpotong pada **54%**, bagian tengah larik `baris_mati`
    tidak terlihat. Adjudikasi R-315 tetap sah karena larik `lubang_tak_dikenal`,
    `ringkasan`, `definisi`, dan `baris_hidup_tanpa_funding` **terlihat utuh**; tetapi
    **cacah total baris `baris_mati` DILARANG diklaim terukur**.
    **UTANG BACA yang TETAP hidup:** `decisions/ADR-A002`, **A004**, **A006**, **A007**,
    **A008**; `karantina_semesta.yml` (`de40fa4e`); `tests/test_pulihkan.py`
    (`11c43533`); `test_rilis_karantina.py` (`739c8da9`); `test_karantina_a006.py`
    (`a5a3d82f`); `tests/test_lubang_tengah.py`; **bagian `baris_mati`
    `silang_funding.json`**.
55. Rumusan pemicu workflow wajib dikutip dari berkas beserta blobnya. **[v57] Tidak
    ada workflow baru.** `ci.yml` = **`c79497b2c812679eaa69aee5b3160eac9f5c5fb7`**,
    `paths-ignore`: `journal/**`, `decisions/**`, `hipotesis/**`, `reports/**`.
57. Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB ditulis bernomor.
    **[v57] BERUNTUN 4 DARI 4, tidak bertambah.** Push berkas ini meramalkan CI tetap
    **1377**; MUDAH, deterministik, TIDAK diskor.
58. Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH DILARANG
    diramalkan dengan pita sempit.
63–76. Berlaku tanpa perubahan dari v43 (`a91a4934`).

**Aturan 66. [v57] UTANG HIDUP**, ditolak ditutup oleh ADR-A019 kep. 8.

**Aturan 77, 78 (TETAP DIUSULKAN). [v57] Tidak mendapat kasus baru.**

**Aturan 79 — tetap PENUH.** **[v57] DITAATI SEPENUHNYA untuk kedua kalinya berturut:**
praregistrasi R-315 ditulis di `journal/2026-07-30-144.md` (commit `1146b96a`) pada
giliran yang **berbeda** dari adjudikasinya (jurnal 145, commit `526e41e8`), dan
**sebelum** `reports/silang_funding.json` dibuka. Saksinya **git**, bukan riwayat
percakapan. **DILARANG menyebut aturan 79 lemah, longgar, atau opsional.**

**Aturan 80. [v57] Tidak perlu dipakai pada R-315:** tidak satu pun lubang berbulan
**sama dengan** `bulan_klines_pertama`; dua pelanggaran sudah tegas berarah **sesudah**.
Kesiapannya tetap dicatat: bulan yang SAMA akan dihitung **MELESET**.

**Aturan 82, 83, 84 [v57]** berlaku tanpa perubahan; 83 dan 84 tercatat ditaati pada
ketiga butir R-315 (satu klausa per butir; aritmetika implikasi ditulis lebih dulu).

**Aturan 81. [v57]** Tidak terpicu — ketiga lubang milik satu simbol, bukan satu bulan
kalender yang menguasai numerator.

**ATURAN 85 — [v57] PUNYA ADJUDIKASI KEDUANYA.** Pada R-315 butir 1, ruang jawaban
seluruhnya **{1, 2, 3}**, lantai aritmetisnya **1**, dan **1 itulah yang dipilih**
dengan alasan tertulis di muka. Ia mendarat **TEPAT**. **Yang DIIZINKAN dikatakan:**
aturan 85 kini punya **dua** adjudikasi, keduanya menang. **Yang tetap DILARANG:**
menyebutnya **teruji**, **bekerja**, atau **terbukti** — dua titik data bukan riwayat,
dan kemenangan tepi **DILARANG** dibaca sebagai kalibrasi membaik (KC-51).

**ATURAN 86 (a dan b). [v57] Tetap resmi; tidak mendapat kejadian kelima.** Poros R-315
justru contoh penerapan yang benar: jawabannya sudah tersimpan di `reports/`, dan yang
dikerjakan hanyalah **membacanya**, bukan menulis modul baru.

### ATURAN 87 — RESMI (ADR-A021 kep. 4)

> **Aturan 87 (resmi).** Bila sebuah butir ramalan turun dari docstring, konstanta, atau
> penalaran yang ditulis pihak lain — termasuk oleh modul repo ini sendiri — butir itu
> **WAJIB** ditandai **TURUNAN** pada praregistrasi, dan pada adjudikasi kemenangannya
> **WAJIB** diperkecil sendiri secara tertulis. Butir yang tidak dapat dibuktikan bebas
> dari sumber itu **diperlakukan sebagai TURUNAN**.

**Riwayat:** diusulkan di STATE v56 atas satu kejadian (R-314 butir 2 dan 3), ditolak
diresmikan oleh ADR-A020 kep. 7 karena kejadiannya baru satu. Kejadian kedua datang
dari R-315: janji penandaan ditulis di muka pada jurnal 144, lalu **ditepati** pada
jurnal 145 — pemeriksaan menunjukkan konstanta `LUBANG_TAK_DIKENAL_TERCATAT = 3` memuat
**cacah**, bukan identitas atau arah waktu, sehingga butir 1 tetap **MURNI** tetapi
kemenangannya diperkecil sendiri menjadi **satu bit**.

### ATURAN 88 — DIUSULKAN, BELUM RESMI (ADR-A021 kep. 5)

> **Usulan aturan 88.** Ramalan bahwa **semua** anggota sebuah himpunan berbagi satu
> sifat **WAJIB** disertai **mekanisme tertulis** yang memaksa keseragaman itu. Bila
> yang tersedia hanya nama medan, definisi longgar, atau kesan pola, ramalan **WAJIB**
> ditulis sebagai **sebaran** ("berapa dari berapa", dengan pita) alih-alih biner.

Baru **satu** kejadian (R-315 butir 2). ADR-A019 kep. 3 melarang meresmikan aturan atas
satu kejadian; diresmikan pada kejadian kedua.

**Catatan kejujuran yang melekat:** aturan 88 lahir **sesudah** kekalahan. Ia **utang
yang dibayar, bukan laba**, dan **DILARANG** diklaim sebagai kemenangan metodologis.

**Penomoran aturan [v57].** Aturan resmi: **1–81, 83, 84, 85, 86 (a dan b), 87**. Nomor
**82** dicadangkan; **77**, **78**, **88** usulan. **Aturan berikutnya yang bebas: 89.**

## Kelas cacat

KC-1 s.d. KC-12 seperti v19; KC-10, KC-11 DITUTUP. KC-13 keterwakilan sampel. **KC-16
DITARIK — nomornya TETAP kosong selamanya.** KC-17 DITUTUP. Teks penuh KC-14, KC-15,
KC-19..KC-29 di v37 (`f520d5e2`). KC-30..KC-42 di v43 (`a91a4934`). KC-43, KC-44 di
v44. KC-45, KC-46 di v45. KC-47 di v46. KC-48 di v47. KC-49 di v48. KC-50 di v50.
KC-51 teks penuh di v52/v53. KC-52 teks penuh di v54. KC-53 teks penuh di v56.

Ringkas KC-19..KC-53 satu baris: KC-19 mencacah dari ingatan · KC-20 bias ke bawah ·
KC-21 ketiadaan gejala dari ketiadaan pengukuran · KC-22 mekanisme dipindah · KC-23
medan dipindah · KC-24 daftar dari laporan bercacah · KC-25 batas semesta tak tersurat
· KC-26 medan ekstrem membisu tentang seri · KC-27 karakterisasi dari contoh berurut ·
KC-28 mencampur kelas instrumen · KC-29 taksonomi paralel · KC-30 nama kelas dibaca
sebagai keadaan · KC-31 nama peristiwa sebagai mekanisme · KC-32 dua penomoran
dicampur · KC-33 mengenali satu peristiwa lalu berhenti · KC-34 cacah subkelompok dari
pengurangan kepala · KC-35 cakupan kode dicampur cakupan laporan · KC-36 homonim satu
konsep · KC-37 nol dari satu penyebut sebagai bukti di penyebut lain · KC-38 kecocokan
tanpa membedakan mekanisme · KC-39 dua penyebut bulan absen dicampur · KC-40 daftar
klausa sebagai keadaan · KC-41 pemicu/label/nomor dari ingatan · KC-42 menulis ulang
berkas melampaui batas push · KC-43 tanda tangan fungsi dari ingatan · KC-44 semua
laporan di-commit satu langkah · KC-45 satuan bulan-tanpa-funding dan bulan-MATI
dicampur · KC-46 lubang AWAL sebagai "funding berhenti" · KC-47 satu peristiwa
menyamar sebagai banyak pengamatan bebas · KC-48 ambang absolut pada sebaran yang
belum diukur · KC-49 pita dikunci tanpa aritmetika implikasi · KC-50 agregat lewat
jalan memutar · KC-51 bias taksiran pemusatan · KC-52 dua angka atas "semesta sama"
yang mencacah himpunan berbeda · KC-53 nol pada medan dibaca sebagai ketiadaan
fenomena.

### KC-54 — RESMI (ADR-A021 kep. 3)

> **KC-54 — nama medan dibaca sebagai definisi medan.** Sebuah nama medan yang
> deskriptif dibaca seolah menyatakan lebih daripada yang didefinisikannya. Kasus asal:
> `lubang_tak_dikenal` dibaca sebagai pernyataan tentang **posisi waktu** lubang,
> padahal medan itu hanya menyatakan **kegagalan pasangan** terhadap penyebut 19.586.
>
> **Penangkal wajib:** sebelum meramalkan apa pun atas sebuah medan, **salin dulu
> definisi medan itu dari laporan atau dari kode ke dalam praregistrasi**.

`silang_funding.json` memuat blok `definisi` dan `catatan_penyebut` yang, kalau dibuka
lebih dulu, **akan membunuh butir 2 sebelum ia ditulis**. Blok itu tidak dibuka karena
praregistrasi disusun dari **ingatan atas nama medan**. Ini bukan kesialan; ini biaya
melanggar "ukur, jangan menduga" pada tahap **penyusunan ramalan**, bukan pada tahap
pengukuran.

**Kerabat:** KC-53 (nol dibaca sebagai ketiadaan), Koreksi 11 UKUR v15 (label gugus
bulan), KC-30, KC-31, KC-36, KC-41, butir 15 daftar kesalahan dokumen di atas.
**Kelas cacat berikutnya: KC-55.**

**KC-41 — tetap berlaku.** Berkas SUMBER menang, dengan pengecualian tersurat untuk
kelima belas butir di tabel kesalahan dokumen.

## Hipotesis

**H-A011 — TERBUKTI** (ADR-A020 kep. 1): LITUSDT 2026-01..2026-06 keenamnya HIDUP,
kebangkitan pertama yang terukur. **Generalisasi ke simbol lain DILARANG** (KC-47: satu
simbol, satu rentetan). **Kalimat sebab DILARANG.**

**H-A020 (DIUSULKAN, BELUM DIUJI, TANPA JALAN UJI YANG DIKETAHUI)** — ketujuh baris
MATI tak penuh berbulan `2024-05` adalah SATU peristiwa; jendelanya sembilan lilin
(39.308..39.317). **Uji yang direncanakan MUSTAHIL** — tidak ada lubang tengah di bulan
itu.

**H-A021 (DIUSULKAN, BELUM DIUJI, TANPA JALAN UJI YANG DIKETAHUI)** — **ANCUSDT
2022-05** (defisit 26.959) dan **LUNAUSDT 2022-05** (26.950) adalah SATU peristiwa;
dasarnya HANYA selisih sembilan lilin. **Uji yang direncanakan MUSTAHIL** dengan alasan
yang sama.

**H-A022 — TERBUKTI**, dengan batas: yang terbukti **identitas himpunan**, bukan sebab
karantina; **identitas 12 simbol-bulan BELUM DIDAFTAR**; **DILARANG** menulis apa pun
tentang **jenis** instrumen yang dikarantina.

**[v57] Tidak ada hipotesis baru yang lahir dari R-315.** Pertanyaan yang lahir —
mengapa BNXUSDT 2022-06 dan 2022-08 tidak lolos gerbang — sengaja **tidak** dinaikkan
menjadi hipotesis, sebab belum ada satu pun mekanisme tertulis yang mendasarinya
(semangat usulan aturan 88). Ia poros riset, bukan hipotesis.

Hipotesis berikutnya **H-A023**.

## Berkas akar — status hidup/mati, LENGKAP 5 dari 5

- **`STATE_LAMPIRAN.md`** (`f2b90764`, 2.350 B) — HIDUP sebagai arsip naratif
  (L-1..L-5). Tidak memuat angka semesta.
- **`STATE_LAMPIRAN_ANGKA.md`** (`f3ebdb02`, 1.841 B) — HIDUP tetapi hampir kosong.
  `N_percobaan` = 0. Memuat klaim TERLARANG (Signals 10.032 / +189,41R / PF 1,61).
  **Jangan dicampur dengan penyebut 19.586** (KC-36).
- **`PETA_MODUL.md`** (`9ee33a99`, 8.691 B) — HIDUP, seluruhnya tentang repo WARISAN
  `bot_v8`. **Tiga butir "memerlukan verifikasi" TETAP UTANG TERBUKA:** (a) `enable_hs`
  tidak ada di `config.py` padahal dipakai `strategy.py`; (b) klaim "30 pair alfabetis";
  (c) klaim "kendala mengikat = kapasitas margin".
- **`PETA_MODUL_BERKAS.md`** (`3abe95f6`, 6.890 B) — HIDUP; inventaris 208 berkas repo
  WARISAN; **34** berkas uji warisan.
- **`PROMPT_KELANJUTAN.md`** (`35beed4449d7efe899a44f8456060c2f23323f7e`, 10.777 B) —
  **ARSIP, BUKAN SUMBER**. Ia memuat perintah lama "jangan berhenti dengan alasan
  konteks" yang **berlawanan** dengan cara kerja sekarang; ADR-A018 kep. 9 memutuskan
  **perintah operator menang**. **[v57] Masih belum diberi kepala "ARSIP".**
- `STATE_LAMPIRAN_ADR.md` (`a02ef271`) tetap **arsip, bukan sumber**.

## Larangan aktif — jangan dilanggar

- **[v57] DILARANG membaca `lubang_tak_dikenal` sebagai "bulan sebelum simbol lahir"**
  atau sebagai pernyataan arah waktu apa pun (ADR-A021 kep. 2).
- **[v57] DILARANG menulis vonis R-315 sebagai SEPARUH.** Butir 2 kalah penuh.
- **[v57] DILARANG membaca kemunculan BNXUSDT sebagai konfirmasi** fakta lama mana pun
  (syarat gugur (e) menyala).
- **[v57] DILARANG mengklaim sebab** mengapa BNXUSDT 2022-06 dan 2022-08 tidak lolos
  gerbang. Belum diukur (aturan 21).
- **[v57] DILARANG mengklaim cacah total baris `baris_mati`** dari
  `silang_funding.json` sebagai terukur; hasil alat terpotong pada **54%**. Selisih
  TLMUSDT `cacah_lubang_simbol` **20** lawan **19** baris terlihat adalah **utang
  bacaan, bukan cacat laporan** (ADR-A021 kep. 9).
- **[v57] DILARANG memasukkan keempat kecocokan pasca-hoc jurnal 145 §7 ke lajur skor**
  (877+3=880; 48−45=3 bernama; 50−48=2; larik 33 baris) — ADR-A021 kep. 8.
- **[v57] DILARANG mengklaim aturan 88 sebagai kemenangan metodologis.**
- Besar berkas **DILARANG** jadi detektor status.
- Laporan kehidupan TIDAK menyimpan harga (**14** medan) → "harga beku", "lilin datar",
  "jeda pemeliharaan bursa" **DILARANG**.
- **DILARANG** menulis "delisting 28 Mei 2024" dan sebab serupa untuk gugus `2022-05`.
- **712.925 DILARANG jadi penyebut** (KC-50).
- Frasa "sembilan pemeriksaan bebas" **DILARANG**.
- Lajur papan skor **DILARANG dikarang** tanpa membaca STATE.
- Cacah direktori **turunan DILARANG** dikutip sebagai terukur — termasuk 50/54/45.
- **Menyebut "cacah uji" tanpa menyebut repo-nya DILARANG.**
- **`PROMPT_KELANJUTAN.md` DILARANG dipakai sebagai sumber.**
- Kemenangan pita yang menempel tepi **DILARANG** dibaca sebagai kalibrasi membaik
  (KC-51) — termasuk kemenangan butir 1 R-315 di lantai aritmetis.
- Ramalan CI yang laporannya sudah tertimpa **DILARANG diklaim menang**; bot CI yang
  menambah satu commit di atas tiap push pemicu (kini **enam kali berturut**) adalah
  **deterministik** dan **DILARANG** dihitung sebagai kemenangan ramalan.
- **Kelima larangan R-312** berlaku penuh.
- **DILARANG memakai 839.325.999 / 516.135 / 839.842.134 tanpa menyebut penyebutnya.**
- **DILARANG menyebut *jenis* instrumen yang dikarantina**, dan **DILARANG menyebut
  poros identitas 12 karantina "termurah"** (manifes 20.533.802 B).
- **DILARANG menulis bahwa aturan 52 menjaga mutu penalaran ATAS DOKUMEN**; diizinkan
  atas **kode**.
- **DILARANG menyebut aturan 79 lemah, longgar, atau opsional.**
- **DILARANG menuduh isi sebuah berkas tanpa membacanya ulang.**
- **DILARANG mengutip `cacah_simbol_bangkit_dapat_diuji` = 0 sebagai bukti ketiadaan
  kebangkitan** (KC-53).
- **DILARANG menyebut lubang tengah berada pada gugus `2022-05` atau `2024-05`.**
- **DILARANG menyamakan 787 simbol funding dengan 787 simbol klines.**
- **DILARANG menyebut aturan 85 "teruji"** — ia baru punya dua adjudikasi.
- **DILARANG menggeneralisasi kebangkitan LITUSDT ke simbol lain.**

## Angka semesta yang mengikat

Penyebut **19.586** (LOLOS gerbang) · semesta rilis penuh **19.598** = 19.586 + **12**
karantina (**terukur**) · `cacah_baris_dengan_medan` **19.586** · `bulan_klines_funding`
**19.598** · `cacah_simbol` **787** · bukan-pertama **18.799** · HIDUP **18.087** · SEPI
**98** · MATI **1.401** (penuh 1.392 / tak penuh 9; **kohort 456 + luar kohort 945**;
luar kohort berlubang **386**, berfunding **559**;
`bagian_mati_luar_kohort_dengan_lubang_funding` **0,4085**) · `cacah_lain` **0** ·
`defisit_total` **18.143.601** · `defisit_pertama` **17.335.439** (95,5%; rata 22.027;
keterisian ≈49,7%) · `defisit_bukan_pertama` **808.162** (0,0445) · `defisit_sembilan`
**95.237** (0,1178) · sisa **712.925** · calon **17.398** · calon penuh **17.284** ·
calon berdefisit **114** (0,66%) · `defisit_teratas` **291.379** · `bagian_teratas`
**0,4087** · `defisit_terbesar` **42.510** · rata **6.254** · **baris parquet lolos
gerbang 839.325.999** · **baris parquet karantina 516.135** · **baris parquet rilis
penuh 839.842.134** · `cacah_baris_cacat` **0** di seluruh semesta · total byte parquet
**32.706.262.375** · `byte_mati` **579.041.399** · `cacah_hidup_byte_kecil` **38** ·
`cacah_mati_byte_kecil` **2** · bulan pertama HIDUP **769** + SEPI **18** = 787 ✅ ·
lubang funding **880** semesta / **877** dalam penyebut / **3** tak dikenal ·
**[v57] `sebaran_bentuk_semua_lubang` awal 45 / ekor 826 / seluruh 0 / tengah 6 = 877
(TERKONFIRMASI dari `reports/silang_funding.json`)** · **`bentuk_terbitan_funding` awal
48 / ekor 826 / tengah 6 = 880** · **[v57] `tabel_silang` (berfunding/kehilangan
funding): HIDUP 18.054 / 33 · MATI 559 / 842 · SEPI 96 / 2 · TAK_TERUKUR 0 / 0;
jembatan 33 + 842 + 2 = 877, + 3 = 880** · `cacah_hidup_tanpa_funding` **33**, seluruhnya
kelas AWAL (**BNXUSDT 7 · ICPUSDT 13 · JUPUSDT 1 · QTUMUSDT 1 · TLMUSDT 11**) ·
`cacah_simbol_ada_lubang` **122** · `cacah_per_simbol_funding` **787** (himpunan
funding, BUKAN dijamin sama dengan 787 klines) · jumlah uji **1377** (repo riset ini).

### Sidik yang tercatat resmi

- `sidik_kode` `silang_funding` V2
  **`8a9b859c09cd64e30e203e6f8dc53411b8e341c44f112805b3041e5d4d3231b1`**
- `sidik_data_funding`
  **`2c9fbd1b04f74c9c844bc223a99a103d12220b88d08667b3792720e5b9608d24`**
- **[v57, BARU — belum pernah tercatat di dokumen mana pun sebelum ini]**
  `sidik_kode_funding`
  **`d38548236f03314eaa648f64f73be5af2f682207be750a2c2fa413fad581513a`**
- `sidik_kode_laporan`
  **`24b6bb265525e81c2e571b46e401f36903383f1e3738c487850861adc3e8c595`**
- `lubang_tengah` V2
  **`c9372bd763b86cfeb2adcf0a0c0c43dae8d9aa9a6508e9c32f7671d5ec7b3f4e`**

## Ke bagian 2 dan 3

**Utang lampiran yang lahir dari berkas ini:** EKOR **v16** dan UKUR **v16** wajib
menaikkan kepala ke "milik STATE v57" dan memasukkan: **R-315** (lajur: butir 1 TEPAT,
butir 2 MELESET, butir 3 tidak diskor) dan **pengesahan papan skor 318** dengan lajur
MENUNGGU **tidak berubah**; **ADR-A021** (sepuluh keputusan); **KC-54**; **aturan 87
RESMI**; **usulan aturan 88**; **pencabutan bacaan `lubang_tak_dikenal`**; **tabel tiga
lubang tak dikenal**; **jembatan 877 + 3 = 880**; **`sidik_kode_funding` baru**; tabel
aturan 38 **ke-54** (dan **ke-55** bila sudah lahir); butir **14** dan **15** daftar
kesalahan dokumen; **batas pembacaan 54% atas `silang_funding.json`**; utang ukur
diperbarui.

## Penomoran berikutnya

Jurnal **146** · STATE **v58** · EKOR **v16** · UKUR **v16** · PROMPT **v55 (belum
didorong)** · ADR **A022** · KC **KC-55** · aturan **89** · hipotesis **H-A023** ·
ramalan **R-316** · papan skor **318**.

**Poros yang tersisa, urut prioritas (ADR-A021 kep. 7):**

1. **BNXUSDT 2022-06 dan 2022-08** — mengapa dua bulan yang berada **di dalam** rentang
   klines (2022-05..2026-06) tidak lolos gerbang. Poros ini **menyatu** dengan poros
   lama "bulan pertama di penyebut lawan bulan pertama di bursa": keduanya menanyakan
   apa yang dilakukan gerbang terhadap bulan yang datanya ada tetapi tipis. Bahan calon:
   `reports/kehidupan_arsip_*.json` (sudah ada di repo — aturan 86 (a)) dan
   `lux_ai/serapan/gerbang_1m.py` (`c8cc54c8`).
2. **Sebab kekosongan TLMUSDT 2023-03** (2.130 dari 44.640 lilin, 95,2% kosong, HIDUP).
3. **Tebing `2025-07` dan BTCSTUSDT** — keserian dengan lubang LITUSDT yang juga mulai
   `2025-07` **BELUM diukur dan DILARANG diklaim**.
4. **Identitas dua belas simbol-bulan karantina** — menuntut **modul yang berjalan di
   CI**; manifes **20.533.802 byte**. **Bukan kandidat murah.**
5. Sisanya tidak berubah: selisih 40−38 `diagnosa_kc15`; bentangan 38 kohort; H-A016;
   `mati_tersisip` atas 19.586; R-7/19/20/28/36/37; R-199; R-236..R-247; taksonomi
   lubang tiga kelas.

**Poros "irisan 880 lawan 877" dinyatakan TUNTAS secara pembukuan** (ADR-A021 kep. 6)
dan dikeluarkan dari daftar. Yang boleh diklaim hanya **dari mana** selisih 3 berasal;
yang **tidak** boleh diklaim adalah **mengapa** dua bulan itu gagal lolos gerbang.

**Syarat praregistrasi R-316 — kumulatif, seluruhnya WAJIB, kini SEBELAS:** aturan
**79** · **83** · **84** · **85** · **86 (a) dan (b)** · **87** (penandaan TURUNAN di
muka) · **pemeriksaan kebebasan medan terhadap kode sumbernya, tertulis, sebelum pita
dikunci** · **KC-50** · **KC-52** · **KC-53** · **KC-54** (definisi tiap medan yang
diramalkan disalin dari laporan atau kode ke dalam praregistrasi) · aturan **66**.
Semangat **usulan aturan 88** ditaati sukarela: ramalan keseragaman tanpa mekanisme
ditulis sebagai sebaran, bukan biner.
