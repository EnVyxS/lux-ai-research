# STATE — versi 56 (bagian 1 dari tiga)

Diperbarui: 2026-07-31 (sesi 61, giliran lanjutan). Aturan hanya BERTAMBAH; jangan
menulis ulang dari ingatan. v56 disusun di atas `STATE.md` v55 (blob
**`be6bc6524e4209d370a4a5795a00bfe6c561d24d`**), yang **DIBACA UTUH pada giliran ini
sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43).

**Apa yang v56 kerjakan, tersurat:** ia menyerap **ADR-A020** — yang menyatakan
**H-A011 TERBUKTI**, meresmikan **KC-53** dan **aturan 86 butir (b)**, mengusulkan
**aturan 87**, dan **mencabut dua cacat** pada ADR-A019 keputusan 9. Ia mencatat
adjudikasi **R-314 (2 TEPAT / 1 MELESET)**, sehingga papan skor naik dari 313 ke
**316** dan **aturan 85 akhirnya punya adjudikasi pertamanya**. Ia mencatat
**kebangkitan pertama yang terukur** di repo ini. Ia memuat **satu koreksi yang
mempersempit klaim kebaruan jurnal 142** dan **satu konsekuensi pahit**: uji yang
direncanakan bagi H-A020 dan H-A021 ternyata **mustahil**. Ordinal aturan 38 maju ke
**ke-51**.

## KESERASIAN VERSI — TIDAK SERASI; v56 / v14 / v14

1. `STATE.md` **v56** — berkas ini. Aturan 1–81, 83, 84, 85, 86 (+butir b); KC-1..KC-53.
2. `STATE_LAMPIRAN_EKOR.md` **v14** — blob
   **`a722ec632b3ee6f144e6e90c615db2480e946837`** salah; blob yang benar
   **`5d481f9b0fd6adca53e8ba145f3fbd6cfeca20a4`** (commit `a722ec63`). **TERTINGGAL
   SATU VERSI.** Kepalanya berbunyi "milik STATE v55". Ia belum memuat ADR-A020,
   R-314, KC-53, maupun H-A011.
3. `STATE_LAMPIRAN_UKUR.md` **v14** — blob
   **`69d95bc490441ff19f74b4ac5a1b3e8258fdbacb`** (commit `6157586e`). **TERTINGGAL
   SATU VERSI.** Kepalanya berbunyi "milik STATE v55".
4. `STATE_LAMPIRAN_ADR.md` (`a02ef271`) dan **`PROMPT_KELANJUTAN.md`** (`35beed44`) —
   **arsip; BUKAN sumber** (ADR-A018 kep. 9).

**PERINGATAN KESERASIAN.** Sama seperti v55: keserasian pecah begitu berkas ini
didorong, dan itu **harga yang disengaja**. Bila EKOR v14 atau UKUR v14 bertentangan
dengan berkas ini pada **ADR-A020, R-314, KC-53, aturan 86 butir (b), aturan 87,
H-A011, atau papan skor 316**, **berkas ini yang menang** — pengecualian tersurat atas
KC-41 yang berlaku HANYA untuk butir yang v56 nyatakan baru. Untuk segala hal lain,
KC-41 tetap penuh: berkas SUMBER menang.

**Satu berkas per push tetap MENGIKAT** (KC-42, KC-43).

**Tentang push berkas ini:** ia di akar repo sehingga menyalakan `ci.yml`. Tidak satu
pun `tests/**` berubah, jadi cacah uji tetap **1377** — ramalan **deterministik**
(aturan 57), **MUDAH**, TIDAK diskor, TIDAK menambah beruntun. **Laporannya WAJIB
dibaca sebelum push akar berikutnya** (aturan 38).

## STATE DIPECAH TIGA — BACA INI LEBIH DULU

1. **`STATE.md`** (berkas ini) — **bagian 1**: kepala, aturan bernomor 1–**86** (plus
   usulan 77, 78, 82, **87**), kelas cacat KC-1..**KC-53**.
2. **`STATE_LAMPIRAN_EKOR.md`** v14 — **bagian 2**: papan skor per ramalan, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** v14 — **bagian 3**: penyebut 787, taksonomi,
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

**[v56] UTANG ATURAN 66 TETAP HIDUP.** Angka harapan **50 / 54 / 45** tetap **TURUNAN**
dan **DILARANG dikutip sebagai terukur** (ADR-A019 kep. 8).

**LARANGAN (ADR-A018 kep. 10) — DUA CACAH `tests/` DILARANG DICAMPUR.**
`PETA_MODUL_BERKAS.md` (`3abe95f6`) mencatat **34** berkas uji milik repo **WARISAN
`bot_v8`**; repo riset ini punya **53** (menuju 54). **Menyebut "cacah uji" tanpa
menyebut repo-nya DILARANG.**

## PERINGATAN DINI ATURAN 48 — besar modul

`silang_funding.py` **29.873** · `funding.py` **28.121** · `sisa_defisit.py` **25.949**
· `semesta_kuota.py` **24.987** · `lubang_tengah.py` **23.745** ·
`keterisian_lilin.py` **22.291** · `kehidupan_arsip.py` **19.281** · `pulihkan.py`
**14.839**. **Bila `sisa_defisit` V2 atau `silang_funding` V3 diperlukan, pecah lebih
dulu.** **[v56] `lubang_tengah.py` V2 dibaca UTUH** (blob
`4d3beaf18c070d2931044c50dd5a354d75eaceb8`); besarnya terkonfirmasi 23.745 B.

## KESALAHAN DOKUMEN SENDIRI — kini TIGA BELAS

| # | berkas | tertulis | seharusnya | status |
| --- | --- | --- | --- | --- |
| 1 | jurnal 132 §3 | "beruntun 2/1" | 2/2 | dikoreksi di STATE v50 |
| 2 | EKOR v10 | `terisi ≉ 49,7%` | `≈ 49,7%` | LUNAS di EKOR v11 |
| 3 | jurnal 135 §13.3 | "hendan dirumuskan" | "hendak" | LUNAS di STATE v51 |
| 4 | EKOR v11 kepala | "deretministik" | "deterministik" | LUNAS di EKOR v12 |
| 5 | UKUR v11 kepala | "KESERAIAN VERSI" | "KESERASIAN VERSI" | LUNAS di UKUR v12 |
| 6 | UKUR v11 daftar uji | penanda `**` tak berpasangan | berpasangan | LUNAS di UKUR v12 |
| 7 | STATE v52 | "Empat salah ketik" | "Enam" | LUNAS di STATE v53 |
| 8 | STATE v53 aturan 45 | "empat push terakhir" lalu mendaftar ENAM | "enam push terakhir" | LUNAS di STATE v54 |
| 9 | STATE v53 aturan 52 | pembacaan ulang "tidak menangkap satu pun" | satu dari delapan | LUNAS di STATE v54 |
| 10 | jurnal 138 §5 butir 2 | "maka 839.842.134 yang keliru" | kesimpulan tidak sah dari premis benar | LUNAS di jurnal 140 |
| 11 | jurnal 141 §6 | tuduhan terhadap EKOR v13 dan ADR-A019 | terlalu luas; STATE v54 BEBAS | LUNAS di STATE v55 |
| 12 | **ADR-A019 kep. 9** | poros karantina "**termurah**"; poros "**gugus 2022-05/2024-05**" | manifes **20.533.802 B**, menuntut modul CI; bulan sebenarnya **2022-01** dan **2025-07..11** | **LUNAS di ADR-A020 kep. 8 dan berkas ini** |
| 13 | **jurnal 142 §4** | temuan irisan 880/877 disajikan seolah seluruhnya baru | **880 / 877 / 3 sudah tercatat di STATE v55**; yang baru HANYA letak selisihnya di kelas *awal* | **LUNAS di berkas ini** |

### Butir 13 — koreksi yang mempersempit klaim saya sendiri

Jurnal 142 §4 menuliskan "temuan tak terduga" atas irisan 880 lawan 877. Pembacaan
utuh STATE v55 pada giliran ini menunjukkan bahwa bagian "Angka semesta yang mengikat"
**sudah** memuat: *lubang funding 880 semesta / 877 dalam penyebut / 3 tak dikenal*.
Maka **ketiga angka itu bukan temuan baru**. Yang benar-benar baru hanya satu kalimat:
seluruh selisih 3 duduk di kelas **awal** (48 − 45 = 3; 826 − 826 = 0; 6 − 6 = 0),
sebab kelas-kelasnya belum pernah dibandingkan berdampingan. Klaim kebaruan jurnal 142
**dipersempit** ke kalimat itu saja. Ini kelas KC-19 dalam bentuk halus: mengumumkan
sebagai baru apa yang sudah tertulis di dokumen sendiri.

## H-A011 TERBUKTI — kebangkitan pertama yang terukur

Dari `reports/lubang_tengah.json` (blob **`39cd1caacedc4d49ba23c91c80f553bb9fb135a6`**,
11.014 B, dibaca UTUH; `waktu_utc` **2026-07-29T09:38:52Z**), kelima penggugur lolos:
`sidik_seragam` true · `cacah_laporan_dibaca` 8 dari 8 · `cacah_kunci_ganda` 0 ·
`kendali_sah` true · `selisih_lubang_tengah` 0.

LITUSDT kehilangan funding pada lima bulan **2025-07..2025-11** dan memperolehnya
kembali **2026-01**. Keenam bulan **2026-01..2026-06** berstatus **HIDUP**
(`sebaran_status` = {HIDUP 6, MATI 0, SEPI 0, TAK_TERUKUR 0}; `terukur` true).

**Batas yang MENGIKAT:** status HIDUP **tidak** membuktikan sebab kembalinya funding;
ia hanya menunjukkan perdagangan dan penerbitan pulih bersama (aturan 10).
**Generalisasi ke simbol lain DILARANG** — yang terukur satu simbol, satu jeda, satu
pemulihan.

**Bacaan lama DICABUT:** `cacah_simbol_bangkit_dapat_diuji` = 0 pada `kohort_ekor` V4
**DILARANG** dikutip sebagai bukti ketiadaan kebangkitan. Yang benar: tidak ada
kebangkitan yang dapat diuji **menurut definisi kohort ekor**.

## KEENAM LUBANG TENGAH — terukur, dan konsekuensinya pahit

| simbol | bulan | status | rentetan | tetangga berfunding | `cacah_lilin` |
| --- | --- | --- | --- | --- | --- |
| BTCSTUSDT | 2022-01 | MATI | 1 | 2021-12 → 2022-02 | 44.640 |
| LITUSDT | 2025-07 | MATI | 5 | 2025-06 → 2026-01 | 44.640 |
| LITUSDT | 2025-08 | MATI | 5 | 2025-06 → 2026-01 | 44.640 |
| LITUSDT | 2025-09 | MATI | 5 | 2025-06 → 2026-01 | 43.200 |
| LITUSDT | 2025-10 | MATI | 5 | 2025-06 → 2026-01 | 44.640 |
| LITUSDT | 2025-11 | MATI | 5 | 2025-06 → 2026-01 | 43.200 |

**KONSEKUENSI YANG WAJIB DITULIS TERANG.** STATE v55 menetapkan bahwa uji yang
menegakkan atau meruntuhkan **H-A020 dan H-A021** adalah "lubang tengah pada gugus
`2022-05` dan `2024-05`". Keenam lubang tengah yang terukur **tidak menyentuh satu pun
dari kedua bulan itu**. Maka:

1. Uji yang direncanakan bagi H-A020 dan H-A021 **MUSTAHIL** — bukan mahal, bukan
   tertunda, melainkan tidak ada bahannya.
2. **H-A020 dan H-A021 tetap DIUSULKAN dan BELUM DIUJI**, dan kini **tanpa jalan uji
   yang diketahui**.
3. Larangan yang menempel pada keduanya berlaku penuh: **DILARANG** menulis "tujuh
   simbol didelisting 28 Mei 2024" atau sebab serupa bagi gugus `2022-05`.

Poros yang dikira menjawab dua hipotesis sekaligus ternyata menjawab **nol**. Ia
menjawab pertanyaan lain yang lebih berharga (H-A011), tetapi bukan yang direncanakan.

## Aturan bernomor

Aturan **1–36** berlaku tanpa perubahan; teks di STATE v19 (`e06c486e`), ringkas di v37
(`f520d5e2`).

**Aturan 10. [v56] Ditaati** — lihat batas tafsir H-A011.

**Aturan 21 (total papan skor dihitung tangan). [v56] LAJUR BERGERAK.** Rincian baru:
TEPAT **220** · MELESET **58** · SEPARUH **22** · TIDAK TERADJUDIKASI **9** · MENUNGGU
**7**. Aritmetika tangan: 220 + 58 = 278; 278 + 22 = 300; 300 + 9 = 309; 309 + 7 =
**316**. Pertambahan dari 313: **TEPAT +2, MELESET +1**, seluruhnya dari R-314.
N_percobaan = 0. **ADJUDIKASI RISET TETAP TERKUNCI.** MENUNGGU: R-7, R-19, R-20,
R-28, R-36, R-37, R-199.

**R-229 dan R-230 TIDAK masuk lajur ini.** Keduanya praregistrasi warisan milik giliran
penulis modul; pencatatannya wajib di kolom terpisah EKOR (ADR-A020 kep. 5).

**Aturan 29. [v56] Ditaati:** pita R-314 tidak disentuh sesudah pengukuran.

**Aturan 36. [v56] Kasus terkuat tetap berdiri** (`selisih_lilin` dan `pulihkan`
bertemu di 839.325.999). **[v56] Kasus kedua tercatat:** `lubang_tengah` **memakai**
`silang_funding.bentuk_lubang_lokal` alih-alih menyalinnya, sehingga definisi bentuk
lubang tetap satu di seluruh repo — terverifikasi dari kode.

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

38. Cacah uji hanya sah dari `reports/ci_terakhir.json`. **[v56] Ditaati; ordinal maju
    ke ke-51.**

    | ke- | CI | run | commit | blob |
    | --- | --- | --- | --- | --- |
    | 47 | 1377 | 30576963781 | `6642ed68` | `8cbbd4ce` |
    | 48 | 1377 | 30577779309 | `2bdd8233` | `8ec97de5` |
    | 49 | 1377 | 30579348728 | `cd209f3e` | `94d270e7065218f87bd5a26c5113ed8346cf6abf` |
    | 50 | 1377 | 30580133552 | `a722ec63` | `04bfa2ed5fb43f128f8ee2351f41722314685a03` |
    | **51** | **1377** | **30581703827** | **`6157586e`** | **`aeb4315ad73806b61f734f9c1d92b27b1ae2727b`** |

    Pemakaian ke-51 dibaca pada ref `4ea6fd2c`, `waktu_utc` **2026-07-30T21:02:01Z**,
    kode keluar **0**, `1377 tests collected in 0.61s`, atas push UKUR v14.
    **[v56] Sepuluh pembacaan berturut (ke-42..ke-51) tanpa satu pun laporan hangus.**
    Ke-50 tercepat: **0.46s**.
    **Dua cacat lama tetap disebut:** **(a)** ke-**38** (run `30541051907`, CI 1297,
    commit `5d7d8b96`) **tanpa blob**; **(b)** run **30547842823** (bot `de2fc03d`)
    **tidak pernah dibaca**, tertimpa, **DILARANG dihitung**.
    **Calon aturan** "dua push akar berturut tanpa membaca laporan" **tetap DITOLAK
    diresmikan**: masih **satu** kejadian.
45. Keatomikan push pemicu. **[v56]** Tidak ada push pemicu baru sejak trio `c1dc0009`.
46. Kode dilarang menyimpulkan dari penyebut nol. **[v56] Kasus ketiga terbaca dari
    kode dan terkonfirmasi dari laporan:** `lubang_tengah.funding_tanpa_klines`
    menolak berbunyi `kosong_seluruhnya` true bila ada baris tanpa medan; pada alur
    nyata `cacah_tak_terukur` = 0 sehingga true itu **sah**.
47. Satuan cacah tersurat. **[v56] Ditaati.** Tambahan v56: **"6"** bersatuan
    **simbol-bulan berlubang bentuk tengah**; **"787"** pada
    `cacah_per_simbol_funding` bersatuan **simbol pada laporan funding**, yang
    **BUKAN** dengan sendirinya himpunan yang sama dengan 787 simbol klines
    (lihat R-314 syarat gugur 5); **"51"** pada aturan 38 bersatuan **pemakaian
    berjejak**; **"316"** bersatuan **butir ramalan teradjudikasi**.
48. Berkas modul mendekati 800 baris dipecah. **[v56] PERINGATAN DINI berlanjut.**
50. Pengukuran dari KETIADAAN wajib memuat kendali positif. **[v56] Ditaati pada
    laporan lubang tengah:** `kendali` memuat tiga simbol-bulan BTCUSDT berparquet
    terbesar, ketiganya HIDUP dan berfunding; `kendali_sah` true.
52. Laporan yang tidak dapat dibaca utuh setara dengan laporan yang tidak ada.
    **[v56] Ditaati sebelas kali berturut:** jurnal 137–141, ADR-A019, STATE v55,
    EKOR v14, UKUR v14, **jurnal 142** (`af11d8a2`), **jurnal 143** (`fb4ec5ad`),
    **ADR-A020** (`200c7e7d737fdfa0b8d689e35482d9ae249b90ee`), dan berkas ini.
    **[v56] Blob baru yang tercatat pertama kali:** `lux_ai/serapan/lubang_tengah.py`
    **`4d3beaf18c070d2931044c50dd5a354d75eaceb8`**; `reports/lubang_tengah.json`
    **`39cd1caacedc4d49ba23c91c80f553bb9fb135a6`**.
    **UTANG BACA yang TETAP hidup:** `decisions/ADR-A002`, **A004**, **A006**, **A007**,
    **A008**; `karantina_semesta.yml` (`de40fa4e`); `tests/test_pulihkan.py`
    (`11c43533`); `test_rilis_karantina.py` (`739c8da9`); `test_karantina_a006.py`
    (`a5a3d82f`); **`tests/test_lubang_tengah.py`** — belum pernah dibaca, padahal
    modulnya sudah.
55. Rumusan pemicu workflow wajib dikutip dari berkas beserta blobnya. **[v56] Tidak
    ada workflow baru; status `selisih_lilin.yml` (`de2fd4fd`) tetap LUNAS.**
57. Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB ditulis bernomor.
    **[v56] BERUNTUN 4 DARI 4, tidak bertambah.** Push dokumen — termasuk berkas ini —
    meramalkan CI tetap **1377**; MUDAH, deterministik, TIDAK diskor.
58. Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH DILARANG
    diramalkan dengan pita sempit.
63–76. Berlaku tanpa perubahan dari v43 (`a91a4934`).

**Aturan 66. [v56] UTANG HIDUP**, ditolak ditutup oleh ADR-A019 kep. 8. **[v56]
Ditaati** saat menamai `lubang_tengah.py`: nama itu ada pada cacah tangan 49 modul
serapan.

**Aturan 77, 78 (TETAP DIUSULKAN). [v56] Tidak mendapat kasus baru.**

**Aturan 79 — tetap PENUH** (rumusan v55 berlaku tanpa perubahan). **[v56] DITAATI
SEPENUHNYA untuk pertama kalinya sejak R-313:** praregistrasi R-314 ditulis di
`journal/**` (jurnal 142, commit `ae867f2e`) pada giliran yang **berbeda** dari
adjudikasinya (jurnal 143, commit `d92ba0f1`). Saksinya **git**, bukan riwayat
percakapan.

**Aturan 80, 82, 83, 84 [v56]** berlaku tanpa perubahan. **[v56]** Aturan 83 dan 84
tercatat ditaati pada ketiga butir R-314.

**Aturan 81. [v56]** Tidak terpicu.

**ATURAN 85 — [v56] PUNYA ADJUDIKASI PERTAMANYA.** Pemakaian keduanya (R-314 butir 1)
menghasilkan adjudikasi: pita **[747, 827]** dipusatkan tepat pada jangkar 787 dengan
alasan tertulis, dan mendarat **TEPAT**. Larangan lama dicabut sebagian: aturan 85 kini
boleh disebut **sudah pernah teruji satu kali**, tetapi **DILARANG** disebut teruji
secara umum — satu adjudikasi bukan riwayat.

### ATURAN 86 — RESMI, dan [v56] DIPERLUAS DENGAN BUTIR (b)

> **Aturan 86 (a).** Sebelum menulis modul baru untuk menjawab sebuah pertanyaan
> kuantitatif, isi direktori `reports/` **WAJIB** diperiksa lebih dulu. Bila jawabannya
> sudah tersimpan, modul baru **DILARANG** ditulis; angkanya dibaca. Taksiran biaya
> "menulis modul" **WAJIB** disertai taksiran biaya "membaca laporan yang mungkin sudah
> ada", dan keduanya dibandingkan tertulis.
>
> **Aturan 86 (b) — RESMI sejak ADR-A020 kep. 6.** Sebelum meramalkan isi sebuah
> laporan, **docstring modul penghasilnya WAJIB dibaca** untuk memeriksa apakah ramalan
> atas medan yang sama sudah tertulis di sana. Ramalan yang mengulanginya tanpa
> menyebutnya adalah pengambilan kredit atas penalaran orang lain.

**Tiga kejadian terukur, seluruhnya kerugian kami sendiri:**

1. **Jurnal 138 §4.** Biaya uji pemisah ditaksir empat langkah; nyatanya satu
   pembacaan. Meleset ke arah **terlalu mahal**.
2. **Jurnal 140 §7.** `selisih_lilin` + 36 uji + satu workflow ditulis untuk angka yang
   sudah tersimpan sejak 29 Juli.
3. **Jurnal 143 §5.** Poros berprioritas tertinggi terjawab oleh
   `reports/lubang_tengah.json` yang tersimpan sejak 2026-07-29, **dua hari sebelum**
   pertanyaannya dirumuskan. Yang terhindar: satu modul, satu berkas uji, satu workflow.

**Kejadian keempat dengan arah berlawanan (ADR-A020 kep. 8):** poros identitas 12
karantina ditaksir "termurah" padahal manifesnya **20.533.802 byte** — taksiran keliru
ke arah **terlalu murah**.

### ATURAN 87 — DIUSULKAN, BELUM RESMI

> **Usulan aturan 87.** Butir ramalan yang hanya menegaskan ulang praregistrasi pihak
> lain **WAJIB** ditandai **TURUNAN** di tempat ia ditulis, dan hasilnya — menang maupun
> kalah — dicatat pada kolom terpisah dari papan skor.

Baru **satu** kejadian (R-314 butir 2 dan 3). ADR-A019 kep. 3 melarang meresmikan
aturan atas satu kejadian. Diresmikan pada kejadian kedua.

**Penomoran aturan [v56].** Aturan resmi: **1–81, 83, 84, 85, 86 (a dan b)**. Nomor
**82** dicadangkan; **77**, **78**, **87** usulan. **Aturan berikutnya yang bebas: 88.**

## R-314 — ADJUDIKASI RESMI: 2 TEPAT / 1 MELESET

Praregistrasi: jurnal 142 (`af11d8a2`). Adjudikasi: jurnal 143 (`fb4ec5ad`).

| butir | berisiko | ramalan | terukur | hasil |
| --- | --- | --- | --- | --- |
| 1 | ya | `cacah_per_simbol_funding` ∈ **[747, 827]** | **787** | **TEPAT** |
| 2 | ya (TURUNAN) | `h_a010_cacah_simbol_berisi` = **0** | **0** | **TEPAT** |
| 3 | ya (TURUNAN) | `h_a011_cacah_hidup` = **0** | **6** | **MELESET** |

**Syarat gugur 5 MENYALA dan mengikat:** kesamaan 787 dengan `cacah_simbol` klines
**DILARANG** dibaca sebagai bukti kedua himpunan simbol itu sama. Yang terukur hanya
kedua cacahnya sama besar.

**R-314 adalah praregistrasi pertama yang memenuhi kesembilan syarat kumulatif
sekaligus.** Butir 2 dan 3 ditandai TURUNAN **di muka**, sebelum hasilnya diketahui;
kredit dan kekalahannya karena itu sama-sama bukan milik penalaran baru.

**Praregistrasi warisan yang ikut teradjudikasi (di luar lajur):** **R-229 TEPAT**
(`kosong_seluruhnya` true, `cacah_berisi` 0, `cacah_tak_terukur` 0 — sehingga definisi
turunan `bulan_berfunding_pertama` **TEPAT** dan kemenangan R-223 **tidak** perlu
ditinjau ulang); **R-230 MELESET** (diramalkan 0, terukur 6).

## R-312, R-313, R-311 — tidak berubah

**R-312 — TIDAK TERADJUDIKASI selamanya.** Kelima larangan permanen berlaku penuh;
temuan v55 tetap berdiri: arah selisih **mustahil positif secara struktural**, sebab
`ukur_kolom` memaksa `cacah_lilin` = `cacah_lilin_terbaca` + `cacah_baris_cacat` dengan
`cacah_baris_cacat` ≥ 0. Kalimat penutupnya tetap berlaku: **yang gagal satu hal —
tidak ada yang memeriksa apakah besaran yang diramalkan bisa ada.**

**R-313 — TEPAT (2/2)** atas 516.135 dan 12, **dengan pelanggaran aturan 79 yang tidak
diputihkan**: praregistrasinya di chat, bukan `journal/**`. **Bila kelak seseorang
menolak mengakui R-313, penolakan itu sah.**

**R-311 — SEPARUH.** Butir 1 KALAH (pita 200..12.000, terukur **114**); butir 2 MENANG
tipis ke tepi atas (pita 0,02..0,45, terukur **0,4087**); butir 3 tidak diskor.

## KC-52 — tetap DITUTUP sebagai teka-teki, HIDUP sebagai pola

```
Σ baris_utama     = 839.325.999   (19.586 simbol-bulan LOLOS gerbang)
Σ baris_karantina =     516.135   (12 simbol-bulan KARANTINA)
Σ baris_total     = 839.842.134   (19.598 simbol-bulan SELURUH rilis)
```

> **839.325.999 + 516.135 = 839.842.134** dan **19.586 + 12 = 19.598**

Sebab strukturalnya: `kehidupan_arsip.peta_parquet` melewatkan `parquet_karantina`.
Cacah karantina per pecahan (terukur): 130.605 · 131.760 · **0** · 42.585 · 43.590 ·
**0** · 123.630 · 43.965 = **516.135** atas **12** parquet di **enam** pecahan.
Rata-rata **43.011** hanya **turunan**; tafsir "tiap karantina kira-kira sebulan penuh"
**TIDAK ditegakkan**.

**[v56] Pasangan penyebut mirip yang tetap mengundang KC-52:** 19.586 lawan 19.598 ·
**880 lawan 877** · 18.799 lawan 17.398 · **787 simbol klines lawan 787 simbol
funding** — pasangan terakhir ini **baru**, dan justru berbahaya karena kedua cacahnya
**sama besar**.

## Kelas cacat

KC-1 s.d. KC-12 seperti v19; KC-10, KC-11 DITUTUP. KC-13 keterwakilan sampel. **KC-16
DITARIK — nomornya TETAP kosong selamanya.** KC-17 DITUTUP. Teks penuh KC-14, KC-15,
KC-19..KC-29 di v37 (`f520d5e2`). KC-30..KC-42 di v43 (`a91a4934`). KC-43, KC-44 di
v44. KC-45, KC-46 di v45. KC-47 di v46. KC-48 di v47. KC-49 di v48. KC-50 di v50.
KC-51 teks penuh di v52/v53. KC-52 teks penuh di v54.

Ringkas KC-19..KC-52 satu baris: KC-19 mencacah dari ingatan · KC-20 bias ke bawah ·
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
yang mencacah himpunan berbeda.

### KC-53 — RESMI (ADR-A020 kep. 3)

> **KC-53 — nol pada sebuah medan dibaca sebagai ketiadaan fenomena.** Nol pada sebuah
> medan hanya berarti nol **menurut penyebut dan definisi medan itu**. Membacanya
> sebagai ketiadaan fenomena di dunia adalah kesalahan penyebut.

**Dua kejadian terukur:** (1) Koreksi 10 (UKUR v14) — kesunyian dokumen dibaca sebagai
klaim; (2) R-230 — `cacah_simbol_bangkit_dapat_diuji` = 0 dibaca sebagai ketiadaan
kebangkitan, padahal LITUSDT bangkit.

**Penangkal:** setiap kali sebuah nol dipakai sebagai premis, **penyebut dan definisi
medannya wajib ditulis pada kalimat yang sama**.

**Kerabat:** KC-21, KC-37, KC-41, aturan 46, aturan 59. **Kelas cacat berikutnya:
KC-54.**

**KC-41 — tetap berlaku.** Berkas SUMBER menang, dengan pengecualian tersurat untuk
ketiga belas butir di tabel kesalahan dokumen.

## Hipotesis

**H-A011 — TERBUKTI** (ADR-A020 kep. 1), dengan batas tafsir mengikat di atas.

**H-A020 (DIUSULKAN, BELUM DIUJI, TANPA JALAN UJI YANG DIKETAHUI)** — ketujuh baris
MATI tak penuh berbulan `2024-05` adalah SATU peristiwa; jendelanya sembilan lilin
(39.308..39.317).

**H-A021 (DIUSULKAN, BELUM DIUJI, TANPA JALAN UJI YANG DIKETAHUI)** — **ANCUSDT
2022-05** (defisit 26.959) dan **LUNAUSDT 2022-05** (26.950) adalah SATU peristiwa;
dasarnya HANYA selisih sembilan lilin — kebetulan angka, bukan bukti.

**H-A022 — TERBUKTI**, dengan batas: yang terbukti **identitas himpunan**, bukan sebab
karantina; **identitas 12 simbol-bulan BELUM DIDAFTAR**; **DILARANG** menulis apa pun
tentang **jenis** instrumen yang dikarantina.

Hipotesis berikutnya **H-A023**.

## Berkas akar — status hidup/mati, LENGKAP 5 dari 5

- **`STATE_LAMPIRAN.md`** (`f2b90764`, 2.350 B) — HIDUP sebagai arsip naratif
  (L-1..L-5). Tidak memuat angka semesta.
- **`STATE_LAMPIRAN_ANGKA.md`** (`f3ebdb02`, 1.841 B) — HIDUP tetapi hampir kosong.
  `N_percobaan` = 0. Memuat klaim TERLARANG (Signals 10.032 / +189,41R / PF 1,61).
  **Jangan dicampur dengan penyebut 19.586** (KC-36).
- **`PETA_MODUL.md`** (`9ee33a99`, 8.691 B) — HIDUP, seluruhnya tentang repo WARISAN
  `bot_v8`. **Tiga butir "memerlukan verifikasi" TETAP UTANG TERBUKA.**
- **`PETA_MODUL_BERKAS.md`** (`3abe95f6`, 6.890 B) — HIDUP; inventaris 208 berkas repo
  WARISAN; **34** berkas uji warisan.
- **`PROMPT_KELANJUTAN.md`** (`35beed44`, 10.777 B) — **ARSIP, BUKAN SUMBER**;
  perintahnya bertabrakan dengan perintah operator, **perintah operator menang**.
  **[v56] Masih belum diberi kepala "ARSIP".**
- `STATE_LAMPIRAN_ADR.md` (`a02ef271`) tetap **arsip, bukan sumber**.

## Larangan aktif — jangan dilanggar

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
  (KC-51) — dan R-313 pun demikian.
- Ramalan CI yang laporannya sudah tertimpa **DILARANG diklaim menang**.
- **Kelima larangan R-312** berlaku penuh.
- **DILARANG memakai 839.325.999 / 516.135 / 839.842.134 tanpa menyebut penyebutnya.**
- **DILARANG menyebut *jenis* instrumen yang dikarantina.**
- **DILARANG menulis bahwa aturan 52 menjaga mutu penalaran ATAS DOKUMEN**; diizinkan
  atas **kode**.
- **DILARANG menyebut aturan 79 lemah, longgar, atau opsional.**
- **DILARANG menuduh isi sebuah berkas tanpa membacanya ulang.**
- **[v56] DILARANG mengutip `cacah_simbol_bangkit_dapat_diuji` = 0 sebagai bukti
  ketiadaan kebangkitan.**
- **[v56] DILARANG menyebut poros identitas 12 karantina "termurah".**
- **[v56] DILARANG menyebut lubang tengah berada pada gugus `2022-05` atau `2024-05`.**
- **[v56] DILARANG menyamakan 787 simbol funding dengan 787 simbol klines.**
- **[v56] DILARANG menyebut aturan 85 "teruji"** — ia baru punya satu adjudikasi.
- **[v56] DILARANG menggeneralisasi kebangkitan LITUSDT ke simbol lain.**

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
/ **3** tak dikenal · **[v56] sebaran bentuk: seluruh semesta awal 48 / ekor 826 /
tengah 6; dalam penyebut awal 45 / ekor 826 / tengah 6 — seluruh selisih 3 di kelas
AWAL, belum dikonfirmasi dari `reports/silang_funding.json`** ·
`cacah_simbol_ada_lubang` **122** · **[v56] `cacah_per_simbol_funding` 787 (himpunan
funding, BUKAN dijamin sama dengan 787 klines)** · jumlah uji **1377** (repo riset ini).

## Ke bagian 2 dan 3

**Utang lampiran yang lahir dari berkas ini:** EKOR **v15** dan UKUR **v15** wajib
menaikkan kepala ke "milik STATE v56" dan memasukkan: **ADR-A020** (sepuluh keputusan),
**R-314** berikut kolom terpisah untuk R-229/R-230, **KC-53**, **aturan 86 butir (b)**,
**usulan aturan 87**, **H-A011 TERBUKTI**, **adjudikasi pertama aturan 85**, aturan 38
**ke-49, ke-50, ke-51**, jurnal **142** dan **143**, butir **12** dan **13** daftar
kesalahan dokumen, serta **mustahilnya uji lubang tengah bagi H-A020/H-A021**.

## Penomoran berikutnya

Jurnal **144** · STATE **v57** · EKOR **v15** · UKUR **v15** · PROMPT **v55** · ADR
**A021** · KC **KC-54** · aturan **88** · hipotesis **H-A023** · ramalan **R-315** ·
papan skor **316**.

**Poros yang tersisa, urut prioritas (ADR-A020 kep. 9):**

1. **Irisan 880 lawan 877 lubang funding** — satu pembacaan
   `reports/silang_funding.json` (`b61fe8b3`) untuk mengonfirmasi bahwa seluruh
   selisih 3 duduk di kelas *awal*.
2. Sebab kekosongan TLMUSDT `2023-03`.
3. "Bulan pertama di penyebut" lawan "bulan pertama di bursa" (ADR-A016 kep. 6).
4. **Tebing `2025-07` dan BTCSTUSDT** — nilainya naik: kedua nama itu muncul pada tabel
   lubang tengah, dan `2025-07` adalah bulan pertama rentetan LITUSDT sekaligus tebing
   yang sudah dikenal. **Keseriannya BELUM diukur.**
5. **Identitas dua belas simbol-bulan karantina** — turun ke peringkat kelima; menuntut
   **modul yang berjalan di CI**, sebab manifes berjumlah **20.533.802 byte**.
6. Sisanya seperti ADR-A019 kep. 9.

**Poros lubang tengah dinyatakan TUNTAS** dan dikeluarkan dari daftar.

**Syarat praregistrasi R-315 — kumulatif, seluruhnya WAJIB:** aturan **79** · **83** ·
**84** · **85** · **86 (a) dan (b)** · **pemeriksaan kebebasan medan terhadap kode
sumbernya, tertulis, sebelum pita dikunci** · **KC-50** · **KC-52** · **KC-53**
(penyebut tiap nol disebut) · aturan **66**. Sepuluh syarat, naik dari sembilan.
