# STATE — versi 55 (bagian 1 dari tiga)

Diperbarui: 2026-07-31 (sesi 61, giliran lanjutan). Aturan hanya BERTAMBAH; jangan
menulis ulang dari ingatan. v55 disusun di atas `STATE.md` v54 (blob
**`af10274dc4b75292d56ff15c369f1e08ccfc5dd3`**), yang **DIBACA UTUH pada giliran ini
sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43).

**Apa yang v55 kerjakan, tersurat:** ia menyerap **ADR-A019** — yang meresmikan
**aturan 86**, menutup **KC-52**, mengadjudikasi **R-312** dan **R-313** secara resmi,
dan **merumuskan ulang aturan 79 alih-alih melemahkannya**. Ia mencatat bahwa **utang
aturan 52 atas trio `c1dc0009` LUNAS PENUH** dengan tiga blob yang sebelumnya tidak
pernah tercatat. Ia memuat **satu temuan baru yang memperberat vonis atas R-312**, dan
**satu koreksi diri atas jurnal 141** yang menuduh terlalu jauh. Papan skor tetap
**313**; ordinal aturan 38 maju ke **ke-48**.

## KESERASIAN VERSI — TIDAK SERASI; v55 / v13 / v13

1. `STATE.md` **v55** — berkas ini. Aturan 1–81, 83, 84, 85, **86**; KC-1..KC-52.
2. `STATE_LAMPIRAN_EKOR.md` **v13** — blob
   **`26ba6dc06fcaa358df3d0ac511996a9bb40a864f`** (commit `6642ed68`). **TERTINGGAL
   SATU VERSI.** Kepalanya berbunyi "milik STATE v54". Ia belum memuat aturan 86 resmi,
   ADR-A019, jurnal 141, maupun ketiga blob trio.
3. `STATE_LAMPIRAN_UKUR.md` **v13** — blob
   **`9e71c1ee9667c4b06389c87e0c77d4cefaca5b96`** (commit `2bdd8233`). **TERTINGGAL
   SATU VERSI.** Kepalanya berbunyi "milik STATE v54". Ia belum memuat temuan arah
   selisih (bagian di bawah) maupun blob trio.
4. `STATE_LAMPIRAN_ADR.md` (`a02ef271`) dan **`PROMPT_KELANJUTAN.md`** (`35beed44`) —
   **arsip; BUKAN sumber** (ADR-A018 kep. 9).

**PERINGATAN KESERASIAN.** Keserasian v54/v13/v13 yang baru pulih pada giliran lalu
**pecah lagi** begitu berkas ini didorong. Itu **harga yang disengaja**: menunda v55
berarti menahan aturan 86 resmi dan tiga blob trio di luar STATE. Bila EKOR v13 atau
UKUR v13 bertentangan dengan berkas ini pada aturan 86, adjudikasi R-312/R-313, blob
trio, atau daftar kesalahan dokumen, **berkas ini yang menang** — pengecualian tersurat
atas KC-41 yang berlaku HANYA untuk butir yang v55 nyatakan baru. Untuk segala hal
lain, KC-41 tetap penuh: berkas SUMBER menang.

**Satu berkas per push tetap MENGIKAT** (KC-42, KC-43).

**Tentang push berkas ini:** ia di akar repo sehingga menyalakan `ci.yml`. Tidak satu
pun `tests/**` berubah, jadi cacah uji tetap **1377** — ramalan **deterministik**
(aturan 57), **MUDAH**, TIDAK diskor, TIDAK menambah beruntun. **Laporannya WAJIB
dibaca sebelum push akar berikutnya** (aturan 38).

## STATE DIPECAH TIGA — BACA INI LEBIH DULU

1. **`STATE.md`** (berkas ini) — **bagian 1**: kepala, aturan bernomor 1–**86** (plus
   usulan 77, 78, 82), kelas cacat KC-1..KC-52.
2. **`STATE_LAMPIRAN_EKOR.md`** v13 — **bagian 2**: papan skor per ramalan, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** v13 — **bagian 3**: penyebut 787, taksonomi,
   karantina, bulan ABSEN, hipotesis H-A001..H-A022, lubang funding, byte parquet
   semesta, modul/workflow/uji, API terverifikasi.

**Ketiga berkas wajib dibaca bersama.** LANGKAH 0 PROMPT wajib menyebut ketiganya.

## CACAH TANGAN DIREKTORI — UTANG HIDUP

| direktori | cacah TERUKUR (tangan, bernomor) | ref |
| --- | --- | --- |
| `lux_ai/serapan/` (`.py`, termasuk `__init__.py`) | **49** | `3196fd98` / `8a614567` |
| `tests/` | **53** | idem |
| `.github/workflows/` | **44** | idem |
| akar repo | **18** entri (**6** direktori + **12** berkas) | idem |

**[v55] UTANG ATURAN 66 TETAP HIDUP, dan ADR-A019 kep. 8 MENOLAK menutupnya.** Angka
harapan **50 / 54 / 45** tetap **TURUNAN** dan **DILARANG dikutip sebagai terukur**.
Alasan penolakan dikutip apa adanya: menuliskannya sebagai "cacah baru" berarti
mengarang pengukuran di dalam dokumen yang justru meresmikan larangan mengarang.

**LARANGAN (ADR-A018 kep. 10) — DUA CACAH `tests/` DILARANG DICAMPUR.**
`PETA_MODUL_BERKAS.md` (`3abe95f6`) mencatat **34** berkas uji milik repo **WARISAN
`bot_v8`**; repo riset ini punya **53** (menuju 54). **Menyebut "cacah uji" tanpa
menyebut repo-nya DILARANG.**

## PERINGATAN DINI ATURAN 48 — besar modul

`silang_funding.py` **29.873** · `funding.py` **28.121** · `sisa_defisit.py` **25.949**
· `semesta_kuota.py` **24.987** · `lubang_tengah.py` **23.745** ·
`keterisian_lilin.py` **22.291** · `kehidupan_arsip.py` **19.281** · `pulihkan.py`
**14.839**. **Bila `sisa_defisit` V2 atau `silang_funding` V3 diperlukan, pecah lebih
dulu.**

## KESALAHAN DOKUMEN SENDIRI — kini SEBELAS

| # | berkas | tertulis | seharusnya | status |
| --- | --- | --- | --- | --- |
| 1 | jurnal 132 §3 | "beruntun 2/1" | 2/2 | dikoreksi di STATE v50 |
| 2 | EKOR v10 | `terisi ≉49,7%` | `≈49,7%` | LUNAS di EKOR v11 |
| 3 | jurnal 135 §13.3 | "hendan dirumuskan" | "hendak" | LUNAS di STATE v51 |
| 4 | EKOR v11 kepala | "deretministik" | "deterministik" | LUNAS di EKOR v12 |
| 5 | UKUR v11 kepala | "KESERAIAN VERSI" | "KESERASIAN VERSI" | LUNAS di UKUR v12 |
| 6 | UKUR v11 daftar uji | penanda `**` tak berpasangan | berpasangan | LUNAS di UKUR v12 |
| 7 | STATE v52 | "Empat salah ketik" | "Enam" | LUNAS di STATE v53 |
| 8 | STATE v53 aturan 45 | "empat push terakhir" lalu mendaftar **ENAM** | "enam push terakhir" | LUNAS di STATE v54 |
| 9 | STATE v53 aturan 52 | pembacaan ulang "tidak menangkap satu pun" | **satu dari delapan** | LUNAS di STATE v54 |
| 10 | jurnal 138 §5 butir 2 | "maka **839.842.134 yang keliru**" | kesimpulan **tidak sah dari premis benar** | LUNAS di jurnal 140 |
| 11 | **jurnal 141 §6** | larangan R-312 nomor 5 "disajikan di EKOR v13 **dan ADR-A019** seolah diresmikan sesudah adjudikasi" | tuduhan itu **terlalu luas**; lihat di bawah | **LUNAS di berkas ini** |

### Butir 11 — koreksi diri, dan ia berpihak melawan tuduhan saya sendiri

Jurnal 141 §6 menuduh EKOR v13 dan ADR-A019 menyajikan larangan permanen R-312 nomor 5
seolah diresmikan **sesudah** adjudikasi, padahal ia sudah dikunci di muka sebagai
syarat gugur 3. Pembacaan utuh STATE v54 pada giliran ini menunjukkan tuduhan itu
**tidak seluruhnya benar**:

- **STATE v54 TIDAK bersalah.** Larangan nomor 5 di v54 ditutup dengan kalimat kurung
  **"(syarat gugur nomor 3, jurnal 136)"** — atribusinya sudah tepat sejak semula.
- **ADR-A019 memang bersalah**, tetapi ringan: ia mendaftar kelima larangan di bawah
  kepala "DIRESMIKAN" tanpa menyebut bahwa nomor 5 berasal dari praregistrasi.
  Kalimatnya tidak keliru; **konteksnya** yang menyesatkan.
- **Tuduhan terhadap EKOR v13 BELUM TERVERIFIKASI.** EKOR v13 **tidak dibaca ulang**
  pada giliran jurnal 141 ditulis maupun pada giliran ini. Menuduh sebuah berkas dari
  ingatan adalah **KC-41 dan KC-19 sekaligus**, dilakukan di dalam jurnal yang sedang
  merayakan pembacaan utuh. Tuduhan itu **DICABUT** sampai EKOR v13 dibaca ulang.

**Yang tetap berdiri dari jurnal 141 §6:** kredit atas larangan nomor 5 memang milik
**praregistrasi**, bukan adjudikasi. Itu benar dan penting.

### Batas kekuatan aturan 52 — DIKOREKSI KE ATAS, dengan pembatasan

ADR-A019 kep. 2 menulis bahwa pembacaan ulang aturan 52 "tidak berdaya terhadap
penalaran cacat" dan **DILARANG** disebut menjaga mutu penalaran. Giliran ini memberi
kejadian tandingan yang harus dicatat jujur: **pembacaan ulang trio `c1dc0009`
menangkap cacat penalaran** — arah selisih yang mustahil (lihat bagian di bawah) —
yang lolos dari seluruh pemeriksaan lain.

**Rumusan yang berlaku sekarang, lebih tepat daripada keduanya:**

> Pembacaan ulang **dokumen sendiri** lemah terhadap penalaran cacat: ia membaca
> kalimat yang sudah diyakini benar. Pembacaan **kode** kuat terhadapnya: kode
> menyatakan identitas yang tidak dapat ditawar, dan ketidakcocokan antara docstring
> dan badan fungsi tampak begitu keduanya dibaca berdampingan.

Larangan ADR-A019 **dipersempit, bukan dicabut**: DILARANG menulis bahwa aturan 52
menjaga mutu penalaran **atas dokumen**; DIIZINKAN mencatat bahwa ia melakukannya
**atas kode**, dengan satu kejadian terukur.

## KC-52 — DIRESMIKAN DAN DITUTUP (ADR-A019 kep. 1)

```
Σ baris_utama     = 839.325.999   (19.586 simbol-bulan LOLOS gerbang)
Σ baris_karantina =     516.135   (12 simbol-bulan KARANTINA)
Σ baris_total     = 839.842.134   (19.598 simbol-bulan SELURUH rilis)
```

> **839.325.999 + 516.135 = 839.842.134** dan **19.586 + 12 = 19.598**

`Σ baris_total` sama persis dengan angka run rilis `30404071324`. **Ketiganya bersatuan
BARIS PARQUET.** Tidak satu pun keliru.

**Sebab strukturalnya terukur:** `kehidupan_arsip.peta_parquet` (blob `318a5cb1`,
dibaca UTUH) **melewatkan baris `parquet_karantina`**. Kedua belas parquet itu karena
itu tidak pernah masuk penyebut mana pun — benar secara kode, dan tidak pernah disebut
di dokumen mana pun sebelum jurnal 140. **Kesunyian itulah isi KC-52.**

**Cacah karantina per pecahan (terukur, bukan turunan):**

| pecahan | `baris_karantina` | parquet |
| --- | --- | --- |
| 0 | 130.605 | 3 |
| 1 | 131.760 | 3 |
| 2 | 0 (`karantina: null`) | 0 |
| 3 | 42.585 | 1 |
| 4 | 43.590 | 1 |
| 5 | 0 (`karantina: null`) | 0 |
| 6 | 123.630 | 3 |
| 7 | 43.965 | 1 |
| **jumlah** | **516.135** | **12** |

**Mutu bukti:** kedelapan laporan `pulih_sah` **true**; `cacah_sha_tak_cocok`,
`cacah_bagian_hilang`, `cacah_anggota_kurang`, `cacah_anggota_tak_aman`, dan
`selisih_baris_total` seluruhnya **0**. Sidik kode seragam
`76c27e3ce5d6edb13bb998b6ec65b538fb3d25205d4469bd4d186a95fa62d700`; sidik kode manifes
seragam `237ccf427faf9d48e9c0904433a56e8902de64de6552daee5d3053093bfba601`; seluruhnya
dari `run_id_sumber` **30396803601**, ditulis 2026-07-29T02:48Z. Penjumlahan lintas
pecahan sah (aturan 22). **KC-47 diperiksa dan TIDAK terpicu:** 12 parquet tersebar di
**enam** pecahan (3/3/1/1/3/1).

**Rata-rata 516.135 / 12 = 43.011** boleh dikutip sebagai **turunan**, bukan bukti;
sebarannya 42.585 sampai 131.760 per tar. Tafsir "tiap karantina kira-kira sebulan
penuh" **TIDAK ditegakkan**.

## TEMUAN v55 — arah selisih R-312 mustahil positif secara struktural

**Ini temuan jurnal 141 §5, dan ia MEMPERBERAT vonis atas R-312.**

Docstring `selisih_lilin.py` (blob **`d19bdb5fe67e0bd9c1b141d7fb7cc6dcd089c5f2`**,
dibaca UTUH) menetapkan sebelum pengukuran:

> `selisih(baris) = cacah_lilin_terbaca - cacah_lilin`, dengan arah dipilih "supaya
> selisih semesta bertanda POSITIF bila jumlah terbaca memang lebih besar".

Tetapi `kehidupan_arsip.ukur_kolom` memaksa:

> **`cacah_lilin` = `cacah_lilin_terbaca` + `cacah_baris_cacat`**, dengan
> `cacah_baris_cacat` ≥ 0

Maka **`cacah_lilin_terbaca` ≤ `cacah_lilin` pada setiap baris, tanpa kecuali**, dan
selisih yang didefinisikan modul **tidak akan pernah positif**.

**Konsekuensi yang wajib dikutip bersama vonis R-312:**

1. Butir 2 menimbang "sepuluh baris berselisih **positif** terbesar". Himpunan itu
   **mustahil tidak kosong**. Butir 2 bukan sekadar tidak teradjudikasi karena
   penyebutnya kebetulan nol — ia **tidak dapat dimenangkan secara struktural**, dan itu
   benar **sejak sebelum pita dikunci**.
2. Butir 1 mencacah selisih bukan nol arah mana pun, jadi secara teknis masih bisa tidak
   nol. Yang membuatnya nol adalah kenyataan terpisah: `cacah_baris_cacat` = 0 di
   seluruh 19.586.
3. Kalimat docstring "sesuai dua angka di atas" adalah **KC-52 yang ditulis ulang ke
   dalam kode**: ia menyamakan 839.842.134 dengan jumlah sebuah medan per baris,
   padahal angka itu mencacah seluruh rilis **termasuk karantina**, yang tidak pernah
   masuk laporan kehidupan.

**KOREKSI atas rumusan v54, UKUR v13, dan ADR-A019.** Ketiganya menulis bahwa R-312
runtuh karena kedua medan "bukan dua pengukuran bebas". Itu benar tetapi **kurang
keras**. Rumusan yang berlaku: **arah ramalannya berlawanan dengan arah yang mungkin
secara matematis**, dan itu dapat diketahui dari **satu pembacaan** `ukur_kolom`
sebelum satu baris modul pun ditulis.

## Aturan bernomor

Aturan **1–36** berlaku tanpa perubahan; teks di STATE v19 (`e06c486e`), ringkas di v37
(`f520d5e2`).

**Aturan 10. [v55] Ditaati.**

**Aturan 21 (total papan skor dihitung tangan). [v55] Ditaati; lajur TIDAK bergerak:**
218 + 57 = 275; 275 + 22 = 297; 297 + 9 = 306; 306 + 7 = **313**. Rincian: TEPAT
**218** · MELESET **57** · SEPARUH **22** · TIDAK TERADJUDIKASI **9** · MENUNGGU **7**.
N_percobaan = 0. **ADJUDIKASI RISET TETAP TERKUNCI.** MENUNGGU: R-7, R-19, R-20,
R-28, R-36, R-37, R-199. Tidak ada ramalan baru diadjudikasi sejak v54.

**Aturan 29. [v55] Ditaati:** pita R-312 tidak disentuh meskipun kini terbukti mustahil
dimenangkan. Pita yang mustahil tetap dicatat apa adanya, bukan dihapus.

**Aturan 36. [v55] Kasus terkuat sampai kini tetap berdiri:** `selisih_lilin`
(839.325.999 dari medan `cacah_lilin`) dan `pulihkan` (839.325.999 dari kaki parquet,
jalur unduh–bongkar yang sama sekali berbeda, run berbeda, tiga hari lebih awal)
bertemu **sampai satuan terakhir**.

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

38. Cacah uji hanya sah dari `reports/ci_terakhir.json`. **[v55] Ditaati; ordinal maju
    ke ke-48.**

    | ke- | CI | run | commit | blob |
    | --- | --- | --- | --- | --- |
    | 44 | 1341 | 30551789395 | `33a4ab37` | `5b16417b` |
    | 45 | 1377 | 30559145901 | `c1dc0009` | `cdfdee25` |
    | 46 | 1377 | 30575123865 | `8368ca1f` | `effb3a46` |
    | 47 | 1377 | 30576963781 | `6642ed68` | `8cbbd4ce7b85d9e1f217a9cefbdacfb9318dec78` |
    | **48** | **1377** | **30577779309** | **`2bdd8233`** | **`8ec97de5af8b528276174f635e3bda9e6cc2d7ef`** |

    Pemakaian ke-48 dibaca **2026-07-30T20:07:50Z**, kode keluar **0**,
    `1377 tests collected in 0.62s`, atas push UKUR v13.
    **[v55] Tujuh pembacaan berturut (ke-42..ke-48) tanpa satu pun laporan hangus.**
    **Dua cacat lama tetap disebut:** **(a)** ke-**38** (run `30541051907`, CI 1297,
    commit `5d7d8b96`) **tanpa blob**; **(b)** run **30547842823** (bot `de2fc03d`)
    **tidak pernah dibaca**, tertimpa, **DILARANG dihitung**.
    **Calon aturan** — dua push akar berturut tanpa membaca laporan di antaranya pasti
    menghanguskan yang pertama — **tetap DITOLAK diresmikan** (ADR-A019 kep. 3): masih
    **satu** kejadian.
45. Keatomikan push pemicu. **[v55]** Tidak ada push pemicu baru; trio `c1dc0009` tetap
    contoh kepatuhan penuh.
46. Kode dilarang menyimpulkan dari penyebut nol. **[v55] Kasus positif tetap berdiri:**
    `pulihkan` V2 melaporkan `definisi_dapat_dibedakan` **false** pada pecahan 2 dan 5
    dan menolak memilih definisi. **[v55] Kasus kedua terbaca dari kode:**
    `selisih_lilin.bagian_teratas` mengembalikan **null** bila penyebut nol atau baris
    positif kurang dari sepuluh — dan itulah yang terjadi pada alur nyata.
47. Satuan cacah tersurat. **[v55] Ditaati:** "114", "17.398", "18.799", "1.401", "9",
    "53", "49", "44", "34", **"12"** bersatuan **baris atau berkas** — **34 lawan 53
    milik REPO BERBEDA**, dan **12 bersatuan BERKAS PARQUET karantina**; "712.925",
    "291.379", "42.510", "808.162", "95.237", "18.143.601" bersatuan **lilin menit**;
    **"839.325.999", "516.135", "839.842.134" seluruhnya bersatuan BARIS PARQUET**;
    "0,4087" **bagian tanpa satuan**; "29.873", "19.281", "14.839" bersatuan **byte
    berkas sumber**; **"1377"** bersatuan **butir uji terkumpul pytest**; **"48"** pada
    aturan 38 bersatuan **pemakaian berjejak**; **"36"** bersatuan **butir uji**.
48. Berkas modul mendekati 800 baris dipecah. **[v55] PERINGATAN DINI berlanjut.**
50. Pengukuran dari KETIADAAN wajib memuat kendali positif. **[v55] Terverifikasi dari
    kode pada `selisih_lilin`:** empat kendali dibaca utuh — `kendali_deteksi` (jawaban
    dihitung TANGAN, 11 medan), `kendali_nol`, `kendali_negatif` (menuntut bersih
    **−250** agar arah negatif tidak dibulatkan jadi nol), `kendali_teratas` (bagian
    **0,9615** = 7.500/7.800, dihitung TANGAN). Keempatnya lolos pada alur nyata.
52. Laporan yang tidak dapat dibaca utuh setara dengan laporan yang tidak ada.
    **[v55] UTANG TERBESAR LUNAS.** Ketiga berkas trio `c1dc0009` dibaca UTUH pada ref
    `e6007ba5`, **blob dicatat untuk pertama kalinya**:

    | berkas | blob |
    | --- | --- |
    | `.github/workflows/selisih_lilin.yml` | **`de2fd4fd346c9e13213fcc9a410d4aea8460d67a`** |
    | `tests/test_selisih_lilin.py` | **`2d903a4a6f544eacd26b82bdb177680fa78bdffd`** |
    | `lux_ai/serapan/selisih_lilin.py` | **`d19bdb5fe67e0bd9c1b141d7fb7cc6dcd089c5f2`** |

    **Tidak ada pemotongan.** Cacah **36** butir `test_01`..`test_36` **terverifikasi
    dari sumber**; dua helper berawalan garis bawah tidak dikumpulkan pytest. Turunan
    **1341 + 36 = 1377** kini berdiri di atas pembacaan, bukan ingatan.
    **[v55] Ditaati tujuh kali berturut:** jurnal 137, 138, 139, 140, **ADR-A019**
    (`9cd7d25e7a61207343e60233887d06b441aa3cbf`), **jurnal 141**
    (`bde76db952f587f4df4529e49f0015c13a29919b`), dan berkas ini.
    **UTANG BACA yang TETAP hidup:** `decisions/ADR-A002`, **A004**, **A006**, **A007**,
    **A008**; `karantina_semesta.yml` (`de40fa4e`); `tests/test_pulihkan.py`
    (`11c43533`); `test_rilis_karantina.py` (`739c8da9`); `test_karantina_a006.py`
    (`a5a3d82f`). **[v55] BARU:** EKOR v13 dan UKUR v13 belum dibaca ulang sesudah
    ADR-A019, sehingga tuduhan jurnal 141 terhadap EKOR v13 dicabut (butir 11).
55. Rumusan pemicu workflow wajib dikutip dari berkas beserta blobnya. **[v55] LUNAS
    untuk `selisih_lilin.yml`:** blob `de2fd4fd…`, `on.push.paths` **satu entri**
    `'lux_ai/serapan/selisih_lilin.py'`, `permissions: contents: write`, job `ukur`,
    checkout@v4 + setup-python@v5 (3.11), `set +e` → `KODE=$?` → `exit 0`, langkah
    `catat status`, `dorong laporan` `[skip ci]` dengan `pull --rebase`, penutup
    `exit ${{ steps.jalan.outputs.kode }}`. **Cocok persis dengan pola trio.**
57. Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB ditulis bernomor.
    **[v55] BERUNTUN 4 DARI 4, tidak bertambah.** Tidak ada berkas uji baru pada
    giliran-giliran ini. Push dokumen — termasuk berkas ini — meramalkan CI tetap
    **1377**; MUDAH, deterministik, TIDAK diskor, TIDAK menambah beruntun.
58. Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH DILARANG
    diramalkan dengan pita sempit.
63–76. Berlaku tanpa perubahan dari v43 (`a91a4934`).

**Aturan 66. [v55] UTANG HIDUP**, ditolak ditutup oleh ADR-A019 kep. 8.

**Aturan 77, 78 (TETAP DIUSULKAN). [v55] Tidak mendapat kasus baru.**

### ATURAN 79 — DIRUMUSKAN ULANG, BUKAN DILEMAHKAN (ADR-A019 kep. 7)

**v54 menulis bahwa R-313 "melemahkan aturan 79". Rumusan itu DICABUT.** Aturan yang
dilanggar lalu disebut "lemah" adalah aturan yang sedang dihapus diam-diam.

> **Aturan 79 tetap PENUH.** Praregistrasi yang tidak ditulis di `journal/**` sebelum
> pengukuran **tidak sah sebagai praregistrasi**. Bila ia terlanjur diadjudikasi,
> hasilnya **tetap dicatat** demi kejujuran riwayat, tetapi **cacatnya melekat
> permanen**, dan **penolakan pihak ketiga atas hasil itu sah**. Aturan 79 **tidak
> boleh** disebut lemah, longgar, atau opsional.

Yang lemah bukan aturannya, melainkan **kepatuhan kami** pada satu kejadian tertentu.
Perbedaan itu wajib dipertahankan dalam bahasa.

**Aturan 80, 82, 83, 84 [v55]** berlaku tanpa perubahan. **[v55]** Aturan 83 tercatat
**ditaati di dalam kode** R-312: lantai aritmetis 12 diturunkan tertulis dari
516.135 / 44.640 = 11,56… dibulatkan ke atas.

**Aturan 81. [v55]** Tidak terpicu oleh perkembangan baru.

**Aturan 85. [v55] MASIH BELUM PUNYA SATU PUN ADJUDIKASI.** Pemakaian pertamanya
(R-312) tidak menghasilkan adjudikasi. Ia **DILARANG** disebut sebagai penangkal yang
sudah teruji.

### ATURAN 86 — RESMI (ADR-A019 kep. 3)

> **Aturan 86.** Sebelum menulis modul baru untuk menjawab sebuah pertanyaan
> kuantitatif, isi direktori `reports/` **WAJIB** diperiksa lebih dulu untuk memastikan
> jawabannya belum tersimpan di sana. Bila sudah tersimpan, modul baru **DILARANG**
> ditulis; angkanya dibaca. Taksiran biaya "menulis modul" **WAJIB** disertai taksiran
> biaya "membaca laporan yang mungkin sudah ada", dan keduanya dibandingkan tertulis.

**Dua kejadian terukur, keduanya kerugian kami sendiri:**

1. **Jurnal 138 §4.** Biaya uji pemisah ditaksir **empat langkah** (tulis → dorong →
   tunggu CI → baca). Nyatanya **satu pembacaan**. Meleset empat kali ke arah yang
   membuat jalan murah tampak mahal.
2. **Jurnal 140 §7.** Modul `selisih_lilin` ditulis lengkap dengan **36** butir uji dan
   satu workflow untuk mencari angka yang **sudah tersimpan** sebagai `baris_karantina`
   di `reports/pulihkan_pecahan_<i>.json` sejak **29 Juli** — dua hari **sebelum**
   pertanyaannya dirumuskan.

**Penomoran aturan [v55].** Aturan resmi: **1–81, 83, 84, 85, 86**. Nomor **82**
dicadangkan; **77**, **78** usulan. **Aturan berikutnya yang bebas: 87.**

## R-312 — ADJUDIKASI RESMI: TIDAK TERADJUDIKASI, selamanya

Laporan `reports/selisih_lilin_ringkas.json` (blob `e5cc6401`, sidik kode
`e6c77965…`): `cacah_berselisih` **0** dari 19.586; `jumlah_klaim_langsung` =
`jumlah_terbaca_langsung` = **839.325.999**; `bagian_teratas` null; `sebaran_kelas`
`{}`; keempat kendali lolos; `dua_jalur_bertemu` true; `selisih_invarian` delapan-
delapannya 0; kode keluar alur modul **2** — **dirancang**, sebab `kode_keluar`
mengembalikan 2 bila `cacah_berselisih <= 0`.

**Lima larangan permanen, seluruhnya tetap berlaku:**

1. **DILARANG** menyebut pita butir 1 (12..120) "tidak terbantah". Ia tidak diuji.
2. **DILARANG** mengatakan kalibrasi membaik **atau** memburuk karena R-312.
3. **DILARANG** dihitung di pembilang maupun penyebut nisbah kemenangan mana pun.
4. **DILARANG** dihidupkan kembali dengan pita yang sama atau yang diubah.
5. Angka **12** di R-312 butir 1 dan **12** parquet karantina di R-313 berarti berbeda;
   **kesamaan itu DILARANG dibaca sebagai konfirmasi apa pun**. **[v55] Kredit atribusi
   dikoreksi:** larangan ini **berasal dari praregistrasi** — syarat gugur nomor 3 di
   docstring modul dan jurnal 136 — **bukan** dari adjudikasi.

**[v55] Yang harus diakui sebagai kredit, terbaca dari kode:** docstring memuat **empat
syarat gugur yang dikunci di muka**, dan syarat 1 berbunyi bahwa medan identik di
seluruh baris menghasilkan **TIDAK TERADJUDIKASI (aturan 41), bukan MELESET**. Vonis
atas R-312 karena itu **bukan rasionalisasi pasca-hoc**: ia syarat gugur yang terpicu
persis sebagaimana dirumuskan. Disiplin prosedural R-312 hampir seluruhnya benar —
pita terkunci, lantai dihitung, tiga tautologi dibuang tertulis, butir MUDAH ditandai
di muka. **Yang gagal satu hal: tidak ada yang memeriksa apakah besaran yang
diramalkan bisa ada.** Prosedur yang rapi tidak menyelamatkan poros yang mustahil.

**Syarat praregistrasi baru yang lahir darinya (berlaku mulai R-314):** kebebasan
setiap medan yang dipakai dalam sebuah poros **WAJIB diperiksa terhadap kode sumbernya
lebih dulu, tertulis, sebelum pita dikunci.**

## R-313 — ADJUDIKASI RESMI: TEPAT (2/2), dengan cacat yang tidak diputihkan

| butir | berisiko | ramalan | terukur | hasil |
| --- | --- | --- | --- | --- |
| 1 — Σ `baris_karantina` | ya, titik tunggal | **516.135** | **516.135** | **TEPAT** |
| 2 — Σ parquet karantina | ya, titik tunggal | **12** | **12** | **TEPAT** |

**PELANGGARAN ATURAN 79, DIAKUI DAN TIDAK DIPUTIHKAN.** Praregistrasi ditulis **di
chat**, bukan `journal/**`. Dikutip kata demi kata di jurnal 140 §2, tetapi saksinya
**riwayat percakapan, bukan git**. **Bila kelak seseorang menolak mengakui R-313,
penolakan itu sah** — kalimat ini wajib ikut setiap kali R-313 dikutip sebagai
kemenangan.

**DILARANG** membaca R-313 sebagai bukti kalibrasi membaik. Ia menjumlahkan angka yang
sudah tercatat di repo, bukan menaksir sebaran yang belum diukur. Nilai ilmiahnya ada
pada identitas yang ditutupnya, **bukan** pada ketepatan ramalannya.

## R-311 — ADJUDIKASI RESMI: SEPARUH (tidak berubah)

| butir | berisiko | pita | terukur | hasil |
| --- | --- | --- | --- | --- |
| 1 — cacah baris berdefisit | ya | 200 .. 12.000 | **114** | **KALAH** |
| 2 — bagian sepuluh teratas | ya | 0,02 .. 0,45 | **0,4087** | **MENANG** |
| 3 — penggugur bersih + invarian nol | tidak | — | bersih | menang, tidak diskor |

**Rumusan resmi (ADR-A018 kep. 3):** dari **17.398** baris bukan-pertama dan
bukan-MATI, hanya **114** (**0,66%**) berdefisit; keseratus empat belas menanggung
**712.925** lilin, rata-rata **6.254**; sepuluh teratas menanggung **291.379**, yaitu
**0,4087**; terbesar **TLMUSDT 2023-03**, HIDUP, **2.130 dari 44.640** lilin. Larangan
penyertanya berlaku seluruhnya; butir 2 menang **TIPIS ke tepi ATAS**.

## Kelas cacat

KC-1 s.d. KC-12 seperti v19; KC-10, KC-11 DITUTUP. KC-13 keterwakilan sampel. **KC-16
DITARIK — nomornya TETAP kosong selamanya.** KC-17 DITUTUP. Teks penuh KC-14, KC-15,
KC-19..KC-29 di v37 (`f520d5e2`). KC-30..KC-42 di v43 (`a91a4934`). KC-43, KC-44 di
v44. KC-45, KC-46 di v45. KC-47 di v46. KC-48 di v47. KC-49 di v48. KC-50 di v50.
KC-51 teks penuh di v52/v53. **KC-52 teks penuh di v54 dan diringkas di berkas ini.**

Ringkas KC-19..KC-51 satu baris: KC-19 mencacah dari ingatan · KC-20 bias ke bawah ·
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
jalan memutar · KC-51 bias taksiran pemusatan.

**KC-41 — tetap berlaku.** Berkas SUMBER menang, dengan pengecualian tersurat untuk
kesebelas butir di tabel kesalahan dokumen. **[v55] KC-41 dilanggar oleh jurnal 141
sendiri** ketika ia menuduh EKOR v13 tanpa membacanya — dicatat, dicabut, tidak
diputihkan.

**KC-51 — [v55] tidak mendapat kejadian kelima.**

**KC-52 (RESMI sejak v54, DITUTUP).** Rumusan resmi:

> Ketika dua angka besar atas "semesta yang sama" tidak cocok, kemungkinan pertama yang
> wajib diperiksa bukanlah bahwa salah satunya keliru, melainkan bahwa keduanya
> **mencacah himpunan yang berbeda**. Selisih yang tak terjelaskan adalah dugaan tentang
> **batas himpunan**, bukan tentang mutu pengukuran.

**[v55] Kemunculan kedua KC-52 tercatat:** ia hidup **di dalam kode**, pada docstring
`selisih_lilin.py`, bukan hanya di dokumen. Kelas cacat ini karena itu **DITUTUP
sebagai teka-teki, tetapi TETAP HIDUP sebagai pola**: repo ini punya beberapa penyebut
mirip — 19.586 lawan 19.598, **880 lawan 877**, 18.799 lawan 17.398 — dan tiap pasang
adalah undangan bagi kesalahan yang sama.

**Kerabat:** KC-25, KC-36, KC-39, aturan 44. **Kelas cacat berikutnya: KC-53.**

## Hipotesis

**H-A020 (DIUSULKAN, BELUM DIUJI)** — ketujuh baris MATI tak penuh berbulan `2024-05`
adalah SATU peristiwa; jendelanya sembilan lilin (39.308..39.317). **DILARANG** menulis
"tujuh simbol didelisting 28 Mei 2024".

**H-A021 (DIUSULKAN, BELUM DIUJI)** — **ANCUSDT 2022-05** (defisit 26.959) dan
**LUNAUSDT 2022-05** (26.950) adalah SATU peristiwa. Dasarnya HANYA selisih sembilan
lilin — **kebetulan angka, bukan bukti**. Bila DITERIMA: cacah pengamatan bebas sepuluh
teratas turun 10→9, dan `bagian_teratas` **TIDAK berubah**.

**H-A022 — TERBUKTI (ADR-A019 kep. 6), dengan batas tafsir MENGIKAT:**

- Yang terbukti adalah **identitas himpunan**, **bukan** sebab kedua belas simbol-bulan
  itu dikarantina.
- **Identitas kedua belas simbol-bulan BELUM DIDAFTAR.** Nama simbol dan bulannya tidak
  diketahui.
- **DILARANG** menulis kalimat apa pun tentang **jenis** instrumen yang dikarantina.

**Turunan cuma-cuma yang ikut resmi:** `cacah_baris_cacat` = **0 di seluruh semesta** —
tidak satu pun dari 839.325.999 baris gagal diurai. Didapat **tanpa run tambahan**.

**Peringatan yang menempel pada H-A020 dan H-A021:** bentuk buktinya IDENTIK, dan
pengulangan bentuk itu patut dicurigai. Uji yang menegakkan atau meruntuhkan keduanya:
**lubang tengah pada gugus `2022-05` dan `2024-05`**. **DILARANG** menyebut sebab, nama
peristiwa pasar, atau tanggal penghentian sampai diuji.

Hipotesis berikutnya **H-A023**.

## Berkas akar — status hidup/mati, LENGKAP 5 dari 5

- **`STATE_LAMPIRAN.md`** (`f2b90764`, 2.350 B) — HIDUP sebagai arsip naratif
  (L-1..L-5). Tidak memuat angka semesta.
- **`STATE_LAMPIRAN_ANGKA.md`** (`f3ebdb02`, 1.841 B) — HIDUP tetapi hampir kosong.
  `N_percobaan` = 0. Memuat klaim TERLARANG (Signals 10.032 / +189,41R / PF 1,61).
  **Jangan dicampur dengan penyebut 19.586** (KC-36).
- **`PETA_MODUL.md`** (`9ee33a99`, 8.691 B) — HIDUP, seluruhnya tentang repo WARISAN
  `bot_v8`. **(i) `backtest.py` TIDAK memodelkan funding sama sekali**; **(ii) temuan F
  = kebocoran seleksi harfiah**. **Tiga butir "memerlukan verifikasi" TETAP UTANG
  TERBUKA:** `enable_hs` tak ditemukan di `config.py` padahal dipakai `strategy.py`;
  klaim "30 pair alfabetis"; klaim "kendala mengikat = kapasitas margin".
- **`PETA_MODUL_BERKAS.md`** (`3abe95f6`, 6.890 B) — HIDUP sebagai inventaris 208
  berkas repo WARISAN. **34** berkas uji warisan. **Sumber bahaya dua cacah `tests/`.**
- **`PROMPT_KELANJUTAN.md`** (`35beed44`, 10.777 B) — **ARSIP, BUKAN SUMBER**. Isinya
  PROMPT v48 dan **setiap angka posisinya salah**. Perintahnya *"Jangan berhenti dengan
  alasan konteks Notion"* **bertabrakan langsung dengan perintah operator**; **perintah
  operator menang**. Pekerjaan tersisa: beri kepala "ARSIP — BUKAN SUMBER" atau hapus.
  **[v55] Masih belum dikerjakan.**
- `STATE_LAMPIRAN_ADR.md` (`a02ef271`) tetap **arsip, bukan sumber**.

## Larangan aktif — jangan dilanggar

- Besar berkas **DILARANG** jadi detektor status (ADR-A015 kep. 5, ADR-A017 kep. 8).
- Laporan kehidupan TIDAK menyimpan harga (**14** medan) → "harga beku", "lilin datar",
  "jeda pemeliharaan bursa" **DILARANG**.
- **DILARANG** menulis "delisting 28 Mei 2024" dan sebab serupa untuk gugus `2022-05`.
- **712.925 DILARANG jadi penyebut** (KC-50).
- Frasa "sembilan pemeriksaan bebas" **DILARANG**.
- Lajur papan skor **DILARANG dikarang** tanpa membaca STATE.
- Cacah direktori **turunan DILARANG** dikutip sebagai terukur — termasuk 50/54/45.
- **Menyebut "cacah uji" tanpa menyebut repo-nya DILARANG.**
- **`PROMPT_KELANJUTAN.md` DILARANG dipakai sebagai sumber.**
- **Kemenangan pita yang menempel tepi DILARANG dibaca sebagai kalibrasi membaik**
  (KC-51) — **dan R-313 pun DILARANG dibaca demikian**.
- Ramalan CI yang laporannya sudah tertimpa **DILARANG diklaim menang**.
- **Kelima larangan R-312** berlaku penuh.
- **DILARANG memakai 839.325.999 / 516.135 / 839.842.134 tanpa menyebut penyebutnya.**
- **DILARANG menyebut *jenis* instrumen yang dikarantina** sampai 12 simbol-bulan
  didaftar; tafsir "tiap karantina kira-kira sebulan penuh" **TIDAK ditegakkan**.
- **[v55] DILARANG menulis bahwa aturan 52 menjaga mutu penalaran ATAS DOKUMEN.**
  Diizinkan mencatat bahwa ia melakukannya **atas kode**, dengan satu kejadian terukur.
- **[v55] DILARANG menyebut aturan 79 lemah, longgar, atau opsional.**
- **[v55] DILARANG menuduh isi sebuah berkas tanpa membacanya ulang** — pelajaran dari
  butir 11.

## Angka semesta yang mengikat

Penyebut **19.586** (LOLOS gerbang) · semesta rilis penuh **19.598** = 19.586 + **12**
karantina (**terukur**) · `cacah_simbol` **787** · bukan-pertama **18.799** · HIDUP
**18.087** · SEPI **98** · MATI **1.401** (penuh 1.392 / tak penuh 9) · `cacah_lain`
**0** · `defisit_total` **18.143.601** · `defisit_pertama` **17.335.439** (95,5%; rata
22.027; keterisian ≈49,7%) · `defisit_bukan_pertama` **808.162** (0,0445) ·
`defisit_sembilan` **95.237** (0,1178) · sisa **712.925** · calon **17.398** · calon
penuh **17.284** · calon berdefisit **114** (0,66%) · `defisit_teratas` **291.379** ·
`bagian_teratas` **0,4087** · `defisit_terbesar` **42.510** · rata **6.254** · **baris
parquet lolos gerbang 839.325.999** · **baris parquet karantina 516.135** · **baris
parquet rilis penuh 839.842.134** · `cacah_baris_cacat` **0** di seluruh semesta ·
total byte parquet **32.706.262.375** · `byte_mati` **579.041.399** ·
`cacah_hidup_byte_kecil` **38** · `cacah_mati_byte_kecil` **2** · bulan pertama HIDUP
**769** + SEPI **18** = 787 ✅ · lubang funding **880** semesta / **877** dalam penyebut
/ 3 tak dikenal · `cacah_simbol_ada_lubang` **122** · jumlah uji **1377** (repo riset
ini).

## Ke bagian 2 dan 3

**Utang lampiran yang lahir dari berkas ini:** EKOR **v14** dan UKUR **v14** wajib
menaikkan kepala ke "milik STATE v55" dan memasukkan: **aturan 86 RESMI**, ADR-A019
(sepuluh keputusan), **aturan 79 dirumuskan ulang bukan dilemahkan**, **tiga blob
trio** dan lunasnya utang aturan 52, **temuan arah selisih R-312**, **butir 11 daftar
kesalahan dokumen** berikut pencabutan tuduhan terhadap EKOR v13, aturan 38 **ke-46,
ke-47, ke-48**, jurnal **141**, dan penyempitan larangan tentang aturan 52.

## Penomoran berikutnya

Jurnal **142** · STATE **v56** · EKOR **v14** · UKUR **v14** · PROMPT **v55** · ADR
**A020** · KC **KC-53** · aturan **87** · hipotesis **H-A023** · ramalan **R-314** ·
papan skor **313**.

**Poros yang tersisa, urut prioritas (ADR-A019 kep. 9):**

1. **Lubang tengah gugus `2022-05` dan `2024-05`** — poros tunggal berprioritas
   tertinggi; menguji **H-A020 dan H-A021 sekaligus**.
2. **Identitas dua belas simbol-bulan karantina** — kandidat **termurah**; manifesnya
   sudah ada di `reports/manifes_pecahan_<i>.json`. **Aturan 86 berlaku penuh di sini.**
3. **Irisan 880 lawan 877 lubang funding** — kandidat KC-52 berikutnya.
4. Sebab kekosongan TLMUSDT `2023-03`.
5. "Bulan pertama di penyebut" lawan "bulan pertama di bursa" (ADR-A016 kep. 6).
6. Tebing `2025-07` dan BTCSTUSDT.

**Syarat praregistrasi R-314 — kumulatif, seluruhnya WAJIB:** aturan **79** (di
`journal/**`, giliran berbeda dari adjudikasi) · **83** (lantai aritmetis dihitung
tertulis) · **84** (satu klausa per butir) · **85** (tepi "terpusat" di lantai
aritmetis atau paling banyak satu orde di atasnya, dengan alasan tertulis) · **86**
(`reports/` diperiksa lebih dulu) · **pemeriksaan kebebasan medan terhadap kode
sumbernya, tertulis, sebelum pita dikunci** · **KC-50** (agregat lewat jalur LANGSUNG)
· **KC-52** (batas himpunan tiap angka disebut tersurat) · aturan **66** (cacah tangan
sebelum menamai modul).
