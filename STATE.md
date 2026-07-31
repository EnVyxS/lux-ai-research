# STATE — versi 60 (bagian 1 dari tiga)

Diperbarui: 2026-07-31 (UTC). Aturan hanya BERTAMBAH; jangan menulis ulang dari ingatan.
v60 disusun di atas `STATE.md` v59 (blob
**`8f5bc472b81865bdabcb5be7c16bbdbac6505ec1`**, commit `05f6f72e`), yang **DIBACA UTUH
pada giliran ini sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43).

**Apa yang v60 kerjakan, tersurat:** ia menyerap **R-317** — ramalan pertama sejak
R-316 yang diregistrasi dan diadjudikasi dengan tiga belas syarat kumulatif lengkap.
Papan skor **BERGERAK untuk pertama kalinya sejak v57**: **321 → 325**. Dua butir
menang, dua kalah. Ia juga meresmikan **aturan 90**, membuka **kesalahan dokumen butir
18**, dan — yang paling berharga — **melokalisasi dua bulan yang absen dari penyebut
BNXUSDT** ke dalam selang sembilan bulan, tanpa menamainya.

**Kalimat yang wajib dibaca lebih dulu.** v59 mencatat bahwa cacat yang paling awet
adalah tafsir masuk akal atas angka benar. v60 menambahkan bentuk yang lebih memalukan:
**riset ini salah membaca tabel yang ditulisnya sendiri.** Butir 3 R-317 kalah bukan
karena data mengejutkan, melainkan karena kolom tabel H-A010 di lampiran memakai batas
**eksklusif** sementara medan laporan **inklusif**. Sumber kesalahan bukan Binance,
bukan alat, bukan modul — melainkan lampiran kita sendiri.

## KESERASIAN VERSI — TIDAK SERASI; v60 / v18 / v18

1. `STATE.md` **v60** — berkas ini. Aturan 1–81, 83–87, **90**; KC-1..KC-55 resmi,
   **KC-56 dan KC-57 diusulkan**.
2. `STATE_LAMPIRAN_EKOR.md` **v18** — blob
   **`217beaeebd367309ea1a4a4d5ea3234887788b2b`**, commit
   **`bb565f4cb2bc0ef8d7b2c72ece8f835c74613422`**. **TERTINGGAL SATU VERSI** begitu
   berkas ini didorong. Kepalanya berbunyi "milik STATE v59". Ia belum memuat R-317,
   papan skor 325, aturan 90, butir 18, maupun usulan KC-57.
3. `STATE_LAMPIRAN_UKUR.md` **v18** — blob
   **`11b14975a7ee2b00ca5e25ca19fc4e16ad5c1deb`**, commit
   **`51c65e2afea4364a855e68c8f84465d1a2efcac9`**. **TERTINGGAL SATU VERSI**, alasan
   sama; ia juga belum memuat pembacaan `reports/lubang_awal.json`.
4. `STATE_LAMPIRAN_ADR.md` (`a02ef271`) dan **`PROMPT_KELANJUTAN.md`** (`35beed44`) —
   **arsip; BUKAN sumber** (ADR-A018 kep. 9).

**PERINGATAN KESERASIAN.** Keserasian penuh v59 / v18 / v18 **pecah begitu berkas ini
didorong** — harga yang disengaja (satu berkas per push, KC-42). Bila EKOR v18 atau
UKUR v18 bertentangan dengan berkas ini pada **R-317, papan skor 325, aturan 90, butir
18, usulan KC-57, tabel aturan 38 ke-61..ke-63, atau pembacaan
`reports/lubang_awal.json`**, **berkas ini yang menang** — pengecualian tersurat atas
KC-41 yang berlaku HANYA untuk butir yang v60 nyatakan baru. Untuk segala hal lain,
KC-41 tetap penuh: **berkas SUMBER menang**.

Keserasian **wajib dipulihkan** lewat **EKOR v19** dan **UKUR v19**.

**Tentang push berkas ini:** ia di akar repo sehingga menyalakan `ci.yml`. Tidak satu
pun `tests/**` berubah, jadi cacah uji tetap **1377** — ramalan **deterministik**
(aturan 57), **MUDAH**, TIDAK diskor. Laporannya WAJIB dibaca sebelum push akar
berikutnya (aturan 38, pemakaian **ke-64**), dan **wajib lolos aturan 90**.

## STATE DIPECAH TIGA — BACA INI LEBIH DULU

1. **`STATE.md`** (berkas ini) — **bagian 1**: kepala, aturan bernomor 1–87 dan 90
   (plus usulan 77, 78, 82, 88, 89), kelas cacat KC-1..KC-55 (**KC-56, KC-57 usulan**).
2. **`STATE_LAMPIRAN_EKOR.md`** — **bagian 2**: papan skor per ramalan, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** — **bagian 3**: penyebut 787, taksonomi, karantina,
   bulan ABSEN, hipotesis H-A001..H-A023, lubang funding, byte parquet semesta,
   modul/workflow/uji, API terverifikasi, koreksi bernomor.

**Ketiga berkas wajib dibaca bersama.** LANGKAH 0 PROMPT wajib menyebut ketiganya.

## CACAH TANGAN DIREKTORI — UTANG HIDUP

| direktori | cacah TERUKUR (tangan, bernomor) | ref |
| --- | --- | --- |
| `lux_ai/serapan/` (`.py`, termasuk `__init__.py`) | **49** | `3196fd98` / `8a614567` |
| `tests/` | **53** | idem |
| `.github/workflows/` | **44** | idem |
| akar repo | **18** entri (**6** direktori + **12** berkas) | idem |

**[v60] UTANG ATURAN 66 TETAP HIDUP.** Angka harapan **50 / 54 / 45** tetap **TURUNAN**
dan **DILARANG dikutip sebagai terukur** (ADR-A019 kep. 8). Tidak ada modul baru sejak
v56.

**LARANGAN (ADR-A018 kep. 10) — DUA CACAH `tests/` DILARANG DICAMPUR.**
`PETA_MODUL_BERKAS.md` (`3abe95f6`) mencatat **34** berkas uji milik repo **WARISAN
`bot_v8`**; repo riset ini punya **53**. **Menyebut "cacah uji" tanpa menyebut repo-nya
DILARANG.**

## PERINGATAN DINI ATURAN 48 — besar modul

`silang_funding.py` **29.873 B / 705 baris** (pagar 800 → jarak **95**) · `funding.py`
**28.121** · `sisa_defisit.py` **25.949** · `semesta_kuota.py` **24.987** ·
`lubang_tengah.py` **23.745** · `keterisian_lilin.py` **22.291** · `kehidupan_arsip.py`
**19.281** · `pulihkan.py` **14.839**.

`gerbang_1m.py` (`c8cc54c84a57173ef2e426c317d6ac50734e9b4a`) tetap **pustaka murni** —
tanpa `KELUARAN`, tanpa `jalankan`, **tidak menulis laporan apa pun**. **Pertanyaan
poros tentang gerbang TIDAK dapat dijawab dari keluaran gerbang.** Penulis
`semesta_rentang.json` **masih belum diidentifikasi**.

**[v60] `lubang_awal.py` (`8c36943da222dfa262b3b9f2117bf72dc801681d`) DIBACA UTUH.** Ia
berkeluaran (`KELUARAN = "reports/lubang_awal.json"`, `VERSI = 1`) dan memuat
**`BATAS_BARIS_LAPORAN = 60`** — lihat bagian pembacaan di bawah.

## KESALAHAN DOKUMEN SENDIRI — kini DELAPAN BELAS

Butir 1–15 seperti v58 (teks penuh di v58, blob `986b138f`), seluruhnya LUNAS. Butir 16
dan 17 LUNAS (teks penuh di v58 dan v59).

| # | berkas | tertulis | seharusnya | status |
| --- | --- | --- | --- | --- |
| 16 | jurnal 146 §5 | pita **dua sisi** | ruang nilai **tiga sisi**; terukur 51 di sisi terbuka | LUNAS di v58 |
| 17 | STATE v58, aturan 38 | "tujuh belas" pembacaan (ke-42..ke-57) | 57 − 42 = 15; 15 + 1 = **enam belas** | LUNAS di v59 |
| **18** | **tabel H-A010 di lampiran UKUR** | kolom akhir dibaca sebagai `akhir_lubang_awal` | kolom itu **batas EKSKLUSIF** — bulan pertama yang TIDAK berlubang | **LUNAS di berkas ini** |

### Butir 18 — tabel sendiri salah dibaca, lima baris sekaligus

Diperiksa terhadap `reports/lubang_awal.json` pada seluruh lima simbol berlubang awal:

| simbol | tabel H-A010 (lampiran) | `akhir_lubang_awal` (terukur) | selisih |
| --- | --- | --- | --- |
| BNXUSDT | 2023-02 | **2023-01** | +1 bulan |
| ICPUSDT | 2022-09 | **2022-08** | +1 bulan |
| JUPUSDT | 2024-02 | **2024-01** | +1 bulan |
| QTUMUSDT | 2020-03 | **2020-02** | +1 bulan |
| TLMUSDT | 2023-03 | **2023-02** | +1 bulan |

**Lima dari lima, selisih tepat +1 setiap kali.** Bukan salah ketik, bukan pergeseran
baris: kolom lampiran memuat **bulan pertama yang TIDAK berlubang** (eksklusif), medan
laporan memuat **bulan terakhir yang masih berlubang** (inklusif).

**Akibat langsung:** butir 3 R-317 kalah. **Akibat yang lebih jauh:** setiap kutipan
lama "rentang lubang awal" dari tabel H-A010 wajib dibaca ulang dengan penanda
eksklusif. UKUR v19 **wajib** menambahkan penanda itu ke tabel.

**Penangkal:** sebelum sebuah angka lampiran dijadikan dasar ramalan, kolomnya wajib
dipetakan ke **nama medan laporan** yang tepat.

## PEMBACAAN `reports/lubang_awal.json` — BAHAN R-317

Blob **`3da15a11c3cd949fb2741f919beb2b515a51d70f`**, **42.449 B**, dibaca pada ref
**`1ba0a007421182d22584a1d22fac546ff7951b7d`**, **UTUH tanpa peringatan pemotongan
alat**. `waktu_utc` **2026-07-30T07:23:11Z** · `versi_lubang_awal` **1** · `sidik_kode`
**`156499ce9d6e822bb7f57786e8e308955441996699c1fd53d0e8814e1f8f2362`**.
`sidik_data_funding` dan `sidik_kode_silang_funding` **cocok** dengan yang resmi.

**Penggugur aturan 24 seluruhnya bersih:** keenam `selisih_*` = 0; `kendali_sah` true;
`kendali_deteksi_sah` true; `sidik_seragam` true; `laporan_hilang` kosong;
`cacah_kunci_ganda` 0; `cacah_lubang_ganda` 0.

**Pemeriksa bebas yang lolos:** `penyebut_kehidupan` 19586 · `cacah_simbol` 787 ·
`cacah_mati` 1401 · `cacah_lubang_semesta` 880 · `cacah_lubang_dalam_penyebut` 877 ·
`cacah_simbol_ada_lubang` 122 · `cacah_simbol_lubang_awal` 5 ·
`cacah_simbol_lubang_bukan_awal` 118 — **seluruhnya cocok** dengan angka resmi.

### PEMOTONGAN DI DALAM LAPORAN — kelas baru, bukan batas alat

`BATAS_BARIS_LAPORAN = 60` di dalam kode. Terukur:
`cacah_baris_penyebut_butir_1_dilapor` **60** sementara `penyebut_butir_1` **118**.
118 − 60 = **58 baris tidak pernah ditulis ke berkas**.

**Ini pemotongan yang dilakukan MODUL, bukan alat.** Ia **tidak** memunculkan peringatan
pemotongan, sehingga tidak terdeteksi dengan cara apa pun selain membaca kode. Ia
ditemukan **sebelum** berkas dibuka, karena aturan 86 (b) menuntut modul penulis dibaca
lebih dulu.

**LARANGAN BARU:** **DILARANG** mencacah simbol, menjumlah, merata-rata, atau menarik
sebaran apa pun dari `baris_penyebut_butir_1`. Ia **sampel 60 pertama menurut abjad**,
bukan populasi. Larik `baris_penyebut_butir_2` (**5 dari 5**, cacah tangan cocok dengan
`cacah_simbol_lubang_awal`) **boleh** diperlakukan lengkap.

### Baris BNXUSDT — disalin verbatim

```
akhir_lubang_awal        "2023-01"
bulan_pertama            "2022-05"
bulan_terakhir           "2026-06"
bulan_pertama_berlubang  true
cacah_bulan              48
cacah_lubang             19
cacah_lubang_awal        7
cacah_lubang_bukan_awal  12
cacah_mati               15
```

**Definisi disalin dari KODE, bukan dari bentuk data (KC-54):** `cacah_bulan` =
`len(urut)` dengan `urut` = bulan simbol pada `peta_status(status)`, dan `status`
berasal dari `silang_funding.baca_laporan_kehidupan` — yaitu **penyebut kehidupan
19.586**. Maka **`cacah_bulan` di laporan ini adalah cacah bulan PENYEBUT per simbol.**

### TEMUAN — dua bulan absen BNXUSDT TERLOKALISASI (TIDAK DISKOR)

**(i)** Bentangan penyebut 2022-05 → 2026-06, cacah tangan: 2022 Mei–Des **8**; 2023
**12**; 2024 **12**; 2025 **12**; 2026 Jan–Jun **6**. 8 + 12 = 20; 20 + 12 = 32;
32 + 12 = 44; 44 + 6 = **50**. Terukur `cacah_bulan` **48**. 50 − 48 = **2**.

**Dua bulan absen dari penyebut, keduanya di DALAM bentangan. Bukan tiga.**

**(ii)** Rentetan lubang awal BNXUSDT 2022-05..2023-01 = 8 + 1 = **9** bulan, sementara
`cacah_lubang_awal` = **7**. 9 − 7 = **2**. Diperiksa pada keempat simbol lain —
ICPUSDT 16 = 16, TLMUSDT 20 = 20, JUPUSDT 1 = 1, QTUMUSDT 1 = 1 — **seluruhnya
kontigu**. **BNXUSDT satu-satunya yang bolong di dalam rentetan awalnya, dan jumlah
bolongnya sama persis dengan jumlah bulan yang absen dari penyebut.**

**(iii)** Maka kedua bulan absen itu **terletak di antara 2022-05 dan 2023-01**. Selang
pencarian menyempit dari **50 bulan menjadi 9**.

**(iv) Tiga angka bersaing 48 / 50 / 51 — aritmetika tutup untuk pertama kalinya.**
`semesta_rentang.json`: BNXUSDT 2022-04..2026-06, `cacah_bulan` 51, bentangan 51, rapat.
Penyebut: 48, tepi mula 2022-05. 51 − 48 = **3** = satu bulan di tepi (**2022-04**, di
luar penyebut) + **dua** bulan di dalam.

**LARANGAN KERAS.** R-315 menetapkan `lubang_tak_dikenal` = 2022-04, 2022-06, 2022-08,
dan ketiganya **cocok** dengan pola di atas. **Kecocokan itu DILARANG ditulis sebagai
identitas terbukti.** Yang terukur hanyalah **cacah** dan **selang**, bukan **nama**.
Laporan ini tidak memuat daftar bulan penyebut. Kedua bulan absen itu dapat saja
2022-07 dan 2022-09 tanpa satu angka pun di atas berubah. **Empat kecocokan aritmetika
bukan bukti nama** — ini persis jenis kesalahan yang melahirkan KC-47 dan Koreksi 15.

**UTANG UKUR 24 LAHIR: daftar nama bulan penyebut untuk BNXUSDT.** Selama ia terbuka,
poros nomor satu tetap terbuka.

### `uji_r305` — dicatat, TIDAK diadjudikasi

Laporan menuliskan vonisnya sendiri: `butir_1` **KALAH** (`bagian` 1.0 di luar pita
0.55–0.95; penyebut 118 ≥ minimal 100), `butir_2` **KALAH** (`bagian` 0.6 < minimal
0.8; `cacah` 5 di bawah pita 20–120), `butir_3` MUDAH.

**Vonis yang ditulis oleh alat yang diuji TIDAK sah menggantikan adjudikasi tangan**
(aturan 29, KC-49). Papan skor tidak disentuh untuk R-305. **Utang baca
`journal/2026-07-30-125.md` naik peringkat.**

Catatan yang wajib ditahan: `bagian_butir_1` = **1.0** berarti **118 dari 118**. Medan
`mati_tidak_setelah_lubang_bukan_awal` memakai `<=`, sehingga **DILARANG dipakai untuk
klaim arah** (aturan 80).

## R-317 — ADJUDIKASI

Praregistrasi `journal/2026-07-31-148.md` (blob `aae8789582b66ce5a63405d15512433156f2b70d`,
commit `1ba0a007`); adjudikasi `journal/2026-07-31-149.md` (blob
`200a0bc18f71f8c86d321c5e3d7f621ed82ad9d9`, commit `fccd2e12`). **Giliran berbeda —
ADR-A016 dan aturan 85 terpenuhi.**

| butir | diramalkan | terukur | vonis |
| --- | --- | --- | --- |
| 1 [UTAMA] `cacah_bulan` | 48 | **48** | **TEPAT** |
| 2 [UTAMA] `bulan_pertama` | "2022-05" | **"2022-05"** | **TEPAT** |
| 3 [UTAMA] `akhir_lubang_awal` | "2023-02" | **"2023-01"** | **MELESET** |
| 4 [TURUNAN] `cacah_lubang_awal` | 19 | **7** | **MELESET** |
| 5 [MUDAH] terbaca utuh | ya | ya | menang, tidak diskor |

**Butir 4 — risiko yang diakui di muka terbukti.** Jurnal 148 menulis sebelum bahan
dibuka bahwa 19 mungkin mencacah **seluruh** lubang. Terukur: 7 + 12 = **19**. Dugaan
itu tepat, dan justru karena itu butir 4 kalah. **Aturan 87 bekerja.**

**Butir 3 — pita tiga sisi mencegah kemenangan palsu.** Sisi "lebih awal" ditutup di
muka. Bila pita ditulis dua sisi seperti jurnal 146, "2023-01" berpeluang diklaim
menang lewat bunyi harfiah. **Ini manfaat terukur pertama dari usulan aturan 89.**

## Aturan bernomor

Aturan **1–36** berlaku tanpa perubahan; teks di STATE v19 (`e06c486e`), ringkas di v37
(`f520d5e2`).

**Aturan 10. [v60] Ditaati** — tidak satu kalimat sebab ditulis atas BNXUSDT.

**Aturan 21 (total papan skor dihitung tangan). [v60] LAJUR BERGERAK.**
TEPAT **223** · MELESET **63** · SEPARUH **22** · TIDAK TERADJUDIKASI **10** ·
MENUNGGU **7**. Aritmetika tangan: 223 + 63 = 286; 286 + 22 = 308; 308 + 10 = 318;
318 + 7 = **325**. Perubahan dari 321: TEPAT **+2**, MELESET **+2**.
Nisbah atas 308: **72,4 / 20,5 / 7,1%**. N_percobaan = 0.
**ADJUDIKASI RISET TETAP TERKUNCI.** MENUNGGU: R-7, R-19, R-20, R-28, R-36, R-37,
R-199 — tidak berubah. **Papan skor 325 belum sah sampai masuk lajur EKOR v19.**

**Aturan 29. [v60] Ditaati keras.** Temuan dua bulan absen **tidak diramalkan**, maka
**tidak diskor** — sekalipun ia temuan paling berharga pada giliran ini. Vonis
`uji_r305` di dalam laporan juga tidak diskor.

**Aturan 36. [v60] Tidak mendapat kasus keempat.** Kecocokan 2 = 2 antara "bulan absen
dari penyebut" dan "bolong di rentetan awal" **tidak** dimasukkan: keduanya dihitung
dari berkas yang sama, sehingga bukan pemeriksaan bebas.

Aturan **37, 39–44, 47, 49, 51, 53, 54, 56, 59–62** berlaku tanpa perubahan; ringkas
satu baris: 37 kelas cacat pada sampel · 39 keseragaman sampel bukan ramalan · 40 uji
silang baris · 41 penyebut nol → TIDAK TERADJUDIKASI · 42 kelas cacat butuh angka
terukur · 43 toleransi berskala · 44 ramalan menyebut penyebut · 47 satuan cacah
tersurat · 49 re-export mematahkan uji · 51 jendela mundur adaptif · 53 ramalan kode
keluar butuh pembacaan perilaku · 54 cacah `def test_` satu per satu · 56 commit
BERIKUTNYA yang menyentuh X · 59 ketiadaan gejala butuh penyebut · 60 mekanisme tak
dipindah antarkasus · 61 medan tak dipindah antarjalur · 62 daftar tak diminta dari
laporan bercacah.

38. Cacah uji hanya sah dari `reports/ci_terakhir.json`. **[v60] Ditaati; ordinal
    berdiri di ke-63.**

    | ke- | CI | run | commit | blob |
    | --- | --- | --- | --- | --- |
    | 59 | 1377 | 30590948580 | `c0877746` | `5f62452d` |
    | 60 | 1377 | 30591338909 | `72fe177c` | `990502c7` |
    | 61 | 1377 | 30592159959 | `05f6f72e` | `b6d02273aa15ebee7736f79883283f4906c447b7` |
    | 62 | 1377 | 30592559253 | `bb565f4c` | `3f299eaf4383604666f30c3448a32d38e57b1742` |
    | **63** | **1377** | **30593086004** | **`51c65e2a`** | **`a185f32a80471ea9f76c72415cacf3c4f06dfeda`** |

    Ke-61 `waktu_utc` 2026-07-30T23:59:10Z, `0.52s`, bot
    `9e43911b9cab30a2f13fe354f2ed8f6b362a0059`; ke-62 **2026-07-31T00:06:48Z**, `0.62s`,
    bot `64b03bdbdbf07d41f99ada51ced69b2633b4bb34`; ke-63 **2026-07-31T00:17:08Z**,
    `0.57s`, kode keluar **0**, bot `8e0b39a50515c0fdcc04def2cf07543938d74c33`.
    **[v60] Panjang deret, aritmetika terbuka (butir 17):** ke-42..ke-63 →
    63 − 42 = 21; 21 + 1 = **22 pembacaan berturut** tanpa laporan hangus.
    **Ke-64 lahir pada push berkas ini** dan wajib dibaca sebelum push akar berikutnya.
    **Dua cacat lama tetap disebut:** ke-**38** (run `30541051907`, CI 1297, commit
    `5d7d8b96`) **tanpa blob**; run **30547842823** (bot `de2fc03d`) tertimpa,
    **DILARANG dihitung**.
    **Calon aturan** "dua push akar berturut tanpa membaca laporan" **tetap DITOLAK
    diresmikan**: masih **satu** kejadian.
45. Keatomikan push pemicu. **[v60]** Ditaati; berkas ini satu push sendiri.
46. Kode dilarang menyimpulkan dari penyebut nol. **[v60]** Tidak ada kasus baru.
47. Satuan cacah tersurat. **[v60] Ditaati.** Tambahan v60: **"48"** bersatuan **bulan
    milik BNXUSDT yang ADA di penyebut kehidupan 19.586** — bukan bulan kalender, bukan
    bulan di bursa; **"50"** bersatuan **bulan bentangan kalender, TURUNAN**; **"9"**
    bersatuan **bulan bentangan rentetan lubang awal, TURUNAN**; **"2"** bersatuan
    **bulan yang absen, TURUNAN dari pengurangan**; **"60" dan "118"** bersatuan
    **baris laporan** — yang pertama **dilapor**, yang kedua **penyebut sesungguhnya**;
    **"22"** pada aturan 38 bersatuan **pemakaian berjejak**.
48. Berkas modul mendekati 800 baris dipecah. **[v60] PERINGATAN DINI berlanjut.**
50. Pengukuran dari KETIADAAN wajib memuat kendali positif. **[v60] TERPAKAI.** Klaim
    "empat simbol lain kontigu" adalah pengukuran dari ketiadaan bolong; kendali
    positifnya **BNXUSDT sendiri** (9 lawan 7) membuktikan laporan **mampu**
    memperlihatkan ketidak-kontiguan bila ada.
52. Laporan yang tidak dapat dibaca utuh setara dengan laporan yang tidak ada.
    **[v60] Ditaati dua puluh sembilan kali berturut**, dan **tiga puluh kali** bila
    pembacaan ulang berkas ini pada giliran yang sama ikut dihitung.
    **[v60] Blob baru yang tercatat pertama kali:** `lux_ai/serapan/lubang_awal.py`
    **`8c36943da222dfa262b3b9f2117bf72dc801681d`** · `reports/lubang_awal.json`
    **`3da15a11c3cd949fb2741f919beb2b515a51d70f`** · `journal/2026-07-31-148.md`
    **`aae8789582b66ce5a63405d15512433156f2b70d`** · `journal/2026-07-31-149.md`
    **`200a0bc18f71f8c86d321c5e3d7f621ed82ad9d9`** · `STATE.md` v59
    **`8f5bc472b81865bdabcb5be7c16bbdbac6505ec1`** · `STATE_LAMPIRAN_EKOR.md` v18
    **`217beaeebd367309ea1a4a4d5ea3234887788b2b`** · `STATE_LAMPIRAN_UKUR.md` v18
    **`11b14975a7ee2b00ca5e25ca19fc4e16ad5c1deb`** · `ci_terakhir.json` ke-61
    **`b6d02273`**, ke-62 **`3f299eaf`**, ke-63 **`a185f32a`**.
    **BATAS PEMBACAAN yang tetap terbuka:** `semesta_rentang.json` **95%**;
    `silang_funding.json` **54%**; daftar `reports/` **76%**;
    `kehidupan_arsip_0..7.json` **MUSTAHIL dibaca utuh**.
    **[v60] KELAS BATAS BARU — pemotongan oleh MODUL:** `lubang_awal.json` melaporkan
    **60 dari 118** baris butir 1. Ini **bukan** batas alat dan **tidak** memunculkan
    peringatan; ia hanya terdeteksi lewat pembacaan kode.
    **UTANG BACA yang TETAP hidup:** `decisions/ADR-A002`, **A004**, **A006**, **A007**,
    **A008**; `tests/test_gerbang_1m.py`; `karantina_semesta.yml` (`de40fa4e`);
    `tests/test_pulihkan.py` (`11c43533`); `test_rilis_karantina.py` (`739c8da9`);
    `test_karantina_a006.py` (`a5a3d82f`); `tests/test_lubang_tengah.py`; bagian
    `baris_mati` `silang_funding.json`; modul penulis `semesta_rentang.json`;
    **[v60 BARU] `journal/2026-07-30-125.md` (praregistrasi R-305) — peringkat naik**.
55. Rumusan pemicu workflow wajib dikutip dari berkas beserta blobnya. **[v60] Tidak
    ada workflow baru.** `ci.yml` = **`c79497b2c812679eaa69aee5b3160eac9f5c5fb7`**,
    `paths-ignore`: `journal/**`, `decisions/**`, `hipotesis/**`, `reports/**`.
57. Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB ditulis bernomor.
    **[v60] BERUNTUN 4 DARI 4, tidak bertambah.**
58. Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH DILARANG
    diramalkan dengan pita sempit.
63–76. Berlaku tanpa perubahan dari v43 (`a91a4934`).

**Aturan 66. [v60] UTANG HIDUP.** Cacah tangan yang **dilakukan** pada giliran ini:
larik `baris_penyebut_butir_2` = **5** (BNXUSDT, ICPUSDT, JUPUSDT, QTUMUSDT, TLMUSDT),
cocok dengan `cacah_simbol_lubang_awal`. Cacah entri `rentang` tetap **tidak dihitung**.

**Aturan 77, 78 (TETAP DIUSULKAN). [v60] Tidak mendapat kasus baru.**

**Aturan 79 — tetap PENUH. [v60] DITAATI, rekor menjadi EMPAT kali berturut** (R-314,
R-315, R-316, R-317). Praregistrasi R-317 didorong sebagai commit `1ba0a007`
**sebelum** `lubang_awal.json` dibuka pada commit yang sama. **DILARANG menyebut aturan
79 lemah, longgar, atau opsional.**

**Aturan 80. [v60] TERPAKAI.** `mati_tidak_setelah_lubang_bukan_awal` memakai `<=`;
angkanya **DILARANG** dipakai untuk klaim arah, termasuk `bagian_butir_1` = 1.0.

**Aturan 81, 82, 83, 84. [v60]** 83 dan 84 ditaati di jurnal 148: tiap butir punya
angka tunggal dan sumber tiap angka dasar disebut.

**ATURAN 85 — [v60] MENJADI TIGA ADJUDIKASI.** R-317 diadjudikasi pada giliran yang
berbeda dari praregistrasinya, dibuktikan oleh dua commit terpisah dan dua giliran
operator terpisah. **Yang tetap DILARANG:** menyebut aturan 85 **teruji**, **bekerja**,
atau **terbukti**. Tiga adjudikasi bukan sebaran.

**ATURAN 86 (a dan b). [v60] KEDUANYA TERPAKAI, dan (b) TERBUKTI MAHAL NILAINYA.**
(a) bahan dipilih dari daftar `reports/` dengan pengakuan batas **76%**. (b) modul
penulis dibaca utuh lebih dulu — dan **hanya karena itu** `BATAS_BARIS_LAPORAN = 60`
ditemukan sebelum berkas dibuka. Tanpa (b), 58 baris yang hilang akan tampak seperti
ketiadaan data.

**ATURAN 87 — RESMI. [v60] TERPAKAI dan TERBUKTI BERGUNA.** Butir 4 R-317 ditandai
TURUNAN di muka beserta alasan risikonya; ia kalah persis pada risiko yang tertulis.
Penandaan di muka membuat kekalahan itu tidak dapat dibantah belakangan.

**ATURAN 88 — TETAP DIUSULKAN.** [v60] Tidak mendapat kejadian kedua.

**ATURAN 89 — TETAP DIUSULKAN, dengan manfaat kini TERUKUR.** Keempat pita R-317
ditutup tiga sisi, dan butir 3 kalah di sisi yang **tidak akan ada** pada pita dua sisi.
**Ia SENGAJA belum diresmikan:** kejadian **cacat**-nya masih **satu** (butir 16), dan
ADR-A019 kep. 3 mensyaratkan dua. Manfaat sekali pakai bukan kejadian cacat.
**Peresmiannya diserahkan ke ADR-A022.**

### ATURAN 90 — DIRESMIKAN PADA BERKAS INI

> **Aturan 90.** Laporan `reports/ci_terakhir.json` **sah dibaca sebagai laporan bagi
> sebuah push hanya bila medan `commit` di dalamnya cocok dengan SHA commit push itu.**
> Bila tidak cocok, laporan itu **milik push sebelumnya** dan **DILARANG** dicatat
> sebagai pemakaian aturan 38 bagi push yang baru; pembacaan wajib diulang.

**Dasar peresmian — TIGA kejadian TERPISAH, di tiga giliran berbeda:**

| # | giliran | blob yang ditolak | `commit` di laporan | commit push yang benar |
| --- | --- | --- | --- | --- |
| 1 | push STATE v58 | `5b433a93` | `9b01c06e` | `839a0f17` |
| 2 | push STATE v59 | `990502c7` | `72fe177c` | `05f6f72e` |
| 3 | push EKOR v18 | `b6d02273` | `05f6f72e` | `bb565f4c` |

Ketiganya lolos syarat ADR-A019 kep. 3: **kejadian terpisah, bukan satu peristiwa yang
menyamar jadi tiga** (KC-47) — masing-masing terjadi pada push berbeda, dengan blob
berbeda, dan masing-masing terdeteksi hanya oleh pemeriksaan medan `commit`.

**Catatan kejujuran:** pada ke-62 dan ke-63 jebakan **tidak** menyala. Itu **tidak**
melemahkan aturan 90 dan juga **tidak** menguatkannya; ia hanya berarti bot kadang
sudah selesai menerbitkan sebelum pembacaan.

**Penomoran aturan [v60].** Aturan resmi: **1–81, 83, 84, 85, 86 (a dan b), 87, 90**.
Nomor **82** dicadangkan; **77**, **78**, **88**, **89** usulan. **Aturan berikutnya
yang bebas: 91.**

## Kelas cacat

KC-1 s.d. KC-12 seperti v19; KC-10, KC-11 DITUTUP. KC-13 keterwakilan sampel. **KC-16
DITARIK — nomornya TETAP kosong selamanya.** KC-17 DITUTUP. Teks penuh KC-14, KC-15,
KC-19..KC-29 di v37 (`f520d5e2`). KC-30..KC-42 di v43 (`a91a4934`). KC-43, KC-44 di
v44. KC-45, KC-46 di v45. KC-47 di v46. KC-48 di v47. KC-49 di v48. KC-50 di v50.
KC-51 di v52/v53. KC-52 di v54. KC-53 di v56. KC-54 di v57. KC-55 di v58.

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

**KC-54 (RESMI, tiga kejadian)** — nama medan dibaca sebagai definisi medan. Penangkal:
salin definisi medan ke praregistrasi; bila definisi tak ditemukan, **syarat gugur
tersurat WAJIB**. **[v60] Tidak bertambah** — definisi `cacah_bulan` disalin dari kode
sebelum pita dikunci, dan syarat gugur (c) ditulis di muka.

**KC-55 (RESMI)** — pita ramalan tidak menutup seluruh ruang nilai. **[v60] Tidak
bertambah**; keempat pita R-317 menutup tiga sisi.

**KC-56 — TETAP DIUSULKAN.** Laporan tanpa `waktu_utc` diperlakukan seolah serempak
dengan laporan lain. **[v60] Tidak mendapat kejadian kedua** — `lubang_awal.json`
**punya** `waktu_utc` (2026-07-30T07:23:11Z), sehingga bahan giliran ini tidak
memicunya. Teks penuh di v59.

### KC-57 — DIUSULKAN, BELUM RESMI (lahir dari butir 18)

> **KC-57 — kolom tabel ringkasan buatan sendiri diperlakukan sebagai medan laporan.**
> Tabel yang disusun di lampiran memakai nama kolom pilihan penulisnya. Batasnya dapat
> **eksklusif** sementara medan sumbernya **inklusif**, atau satuannya dapat bergeser,
> tanpa satu pun tanda di dalam tabel. Mengutip angka lampiran sebagai jika ia medan
> laporan menghasilkan ramalan yang salah bukan karena datanya, melainkan karena
> pembukuannya.
>
> **Angka terukur kasus asal (aturan 42):** lima simbol, selisih **+1 bulan** pada
> kelimanya — BNXUSDT 2023-02/2023-01, ICPUSDT 2022-09/2022-08, JUPUSDT
> 2024-02/2024-01, QTUMUSDT 2020-03/2020-02, TLMUSDT 2023-03/2023-02.
>
> **Penangkal wajib:** sebelum angka lampiran dijadikan dasar ramalan, petakan kolomnya
> ke nama medan laporan dan sebutkan pemetaan itu di praregistrasi.

**MENGAPA IA TIDAK DIRESMIKAN SEKARANG, walau lima baris cocok.** Kelima baris berasal
dari **satu kolom pada satu tabel** — **satu** cacat pembukuan yang tampak lima kali,
bukan lima cacat bebas. Meresmikannya atas dasar lima "kejadian" adalah **KC-47 persis**:
satu peristiwa menyamar sebagai banyak pengamatan bebas. **Satu kejadian.** Diresmikan
pada kejadian kedua yang berasal dari **tabel lain**. **Kerabat:** KC-54 (nama medan
laporan), KC-23 (medan dipindah).

**Kelas cacat berikutnya: KC-58.**

**KC-41 — tetap berlaku.** Berkas SUMBER menang, dengan pengecualian tersurat untuk
kedelapan belas butir di tabel kesalahan dokumen.

## Hipotesis

**H-A011 — TERBUKTI** (ADR-A020 kep. 1). **Generalisasi DILARANG** (KC-47).

**H-A020, H-A021 (DIUSULKAN)** — uji yang direncanakan **MUSTAHIL**, keduanya.

**H-A022 — TERBUKTI**, dengan batas: identitas himpunan, bukan sebab; **identitas 12
simbol-bulan BELUM DIDAFTAR**.

**H-A023 — BERSYARAT DENGAN ARITMETIKA TERTUTUP.** Status naik dari "bersyarat":
51 − 48 = 3 kini **terurai** menjadi 1 di tepi + 2 di dalam, dan angka 2 itu **terukur
dua kali dari dua arah** (50 − 48 dan 9 − 7). **Yang TETAP tidak terukur:** nama kedua
bulan itu. **DILARANG ditulis sebagai TERBUKTI. TIDAK DISKOR.**

Hipotesis berikutnya **H-A024**.

## Berkas akar — status hidup/mati, LENGKAP 5 dari 5

- **`STATE_LAMPIRAN.md`** (`f2b90764`, 2.350 B) — HIDUP sebagai arsip naratif (L-1..L-5).
- **`STATE_LAMPIRAN_ANGKA.md`** (`f3ebdb02`, 1.841 B) — HIDUP tetapi hampir kosong.
  `N_percobaan` = 0. Memuat klaim TERLARANG (Signals 10.032 / +189,41R / PF 1,61).
  **Jangan dicampur dengan penyebut 19.586** (KC-36).
- **`PETA_MODUL.md`** (`9ee33a99`, 8.691 B) — HIDUP, seluruhnya tentang repo WARISAN
  `bot_v8`. **Tiga butir "memerlukan verifikasi" TETAP UTANG TERBUKA.**
- **`PETA_MODUL_BERKAS.md`** (`3abe95f6`, 6.890 B) — HIDUP; 208 berkas warisan; **34**
  berkas uji warisan.
- **`PROMPT_KELANJUTAN.md`** (`35beed4449d7efe899a44f8456060c2f23323f7e`, 10.777 B) —
  **ARSIP, BUKAN SUMBER**; ADR-A018 kep. 9. **[v60] Masih belum diberi kepala "ARSIP"
  — utang berumur SEPULUH versi.**
- `STATE_LAMPIRAN_ADR.md` (`a02ef271`) tetap **arsip, bukan sumber**.

## Larangan aktif — jangan dilanggar

- **[v60] DILARANG menarik cacah, sebaran, atau daftar apa pun dari
  `baris_penyebut_butir_1`** — ia 60 dari 118, sampel abjad, bukan populasi.
- **[v60] DILARANG menamai kedua bulan absen BNXUSDT.** Yang terukur cacah dan selang,
  bukan nama. Kecocokan dengan 2022-06 dan 2022-08 **bukan** identitas.
- **[v60] DILARANG mengutip tabel H-A010 sebagai `akhir_lubang_awal`** — kolomnya
  **eksklusif** (butir 18).
- **[v60] DILARANG memakai vonis `uji_r305` di dalam laporan sebagai adjudikasi.**
- **[v60] DILARANG meresmikan KC-57 atau aturan 89 sebelum kejadian kedua yang bebas.**
- **[v60] DILARANG menyebut aturan 90 "teruji"** — ia baru diresmikan; ia punya tiga
  kejadian cacat, nol pemakaian pencegahan yang tercatat sesudah peresmian.
- **[v60] DILARANG menskor temuan dua bulan absen** — tidak diramalkan (aturan 29).
- DILARANG memperlakukan `semesta_rentang.json` sebagai terbaca utuh — 95%.
- DILARANG membandingkan angka `semesta_rentang.json` tanpa menyebut ia TAK BERTANGGAL.
- DILARANG memindahkan sifat medan `cacah_bulan` ↔ `bulan_per_simbol` (KC-23, KC-52).
- DILARANG mengklaim berapa banyak simbol berlubang pada semesta rentang.
- DILARANG menulis panjang deret tanpa aritmetika `akhir − awal + 1` (butir 17).
- DILARANG menulis H-A023 sebagai TERBUKTI.
- DILARANG menskor R-316 butir 3 sebagai TEPAT atas dasar bunyi harfiah pita.
- DILARANG menyebut salah satu dari enam klausa `gerbang_1m.py` sebagai penyebab
  hilangnya bulan mana pun tanpa medan yang menamainya (pola KC-54).
- DILARANG menyamakan "tidak ada di penyebut" dengan "dijatuhkan gerbang".
- DILARANG membuka `reports/kehidupan_arsip_*.json` dengan harapan membacanya utuh.
- DILARANG membaca `lubang_tak_dikenal` sebagai "bulan sebelum simbol lahir"
  (ADR-A021 kep. 2).
- DILARANG menulis vonis R-315 sebagai SEPARUH. Butir 2 kalah penuh.
- DILARANG menulis vonis R-317 butir 3 atau 4 sebagai SEPARUH. Keduanya kalah penuh.
- DILARANG mengklaim sebab mengapa bulan mana pun tidak sampai ke penyebut.
- DILARANG mengklaim cacah total baris `baris_mati` sebagai terukur (terpotong 54%).
- DILARANG mengklaim aturan 88, 89, KC-56, atau KC-57 sebagai kemenangan metodologis;
  seluruhnya **utang yang dibayar, bukan laba**.
- Besar berkas DILARANG jadi detektor status.
- Laporan kehidupan TIDAK menyimpan harga (**14** medan) → "harga beku", "lilin datar",
  "jeda pemeliharaan bursa" DILARANG.
- DILARANG menulis "delisting 28 Mei 2024" dan sebab serupa untuk gugus `2022-05`.
- **712.925 DILARANG jadi penyebut** (KC-50).
- Frasa "sembilan pemeriksaan bebas" DILARANG.
- Lajur papan skor DILARANG dikarang tanpa membaca STATE.
- Cacah direktori turunan DILARANG dikutip terukur — termasuk 50/54/45.
- Menyebut "cacah uji" tanpa menyebut repo-nya DILARANG.
- `PROMPT_KELANJUTAN.md` DILARANG dipakai sebagai sumber.
- Kemenangan pita yang menempel tepi DILARANG dibaca sebagai kalibrasi membaik (KC-51).
- Ramalan CI yang laporannya sudah tertimpa DILARANG diklaim menang; bot CI
  deterministik dan DILARANG dihitung sebagai kemenangan.
- Kelima larangan R-312 berlaku penuh.
- DILARANG memakai 839.325.999 / 516.135 / 839.842.134 tanpa menyebut penyebutnya.
- DILARANG menyebut *jenis* instrumen yang dikarantina.
- DILARANG menulis bahwa aturan 52 menjaga mutu penalaran ATAS DOKUMEN; yang dijaganya
  **kesetiaan salinan**. Diizinkan atas **kode**.
- DILARANG menyebut aturan 79 lemah, longgar, atau opsional.
- DILARANG menuduh isi sebuah berkas tanpa membacanya ulang.
- DILARANG mengutip `cacah_simbol_bangkit_dapat_diuji` = 0 sebagai bukti ketiadaan
  kebangkitan (KC-53).
- DILARANG menyebut lubang tengah berada pada gugus `2022-05` atau `2024-05`.
- DILARANG menyamakan 787 simbol funding dengan 787 simbol klines.
- DILARANG menyebut aturan 85 "teruji" — ia kini punya **tiga** adjudikasi; tiga bukan
  sebaran.
- DILARANG menggeneralisasi kebangkitan LITUSDT ke simbol lain.

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
gerbang 839.325.999** · **karantina 516.135** · **rilis penuh 839.842.134** ·
`cacah_baris_cacat` **0** · total byte parquet **32.706.262.375** · `byte_mati`
**579.041.399** · `cacah_hidup_byte_kecil` **38** · `cacah_mati_byte_kecil` **2** ·
bulan pertama HIDUP **769** + SEPI **18** = 787 ✅ · lubang funding **880** semesta /
**877** dalam penyebut / **3** tak dikenal · `sebaran_bentuk_semua_lubang` 45 / 826 / 0
/ 6 = **877** · `bentuk_terbitan_funding` 48 / 826 / 6 = **880** · `tabel_silang`
(berfunding / kehilangan funding): HIDUP 18.054 / 33 · MATI 559 / 842 · SEPI 96 / 2 ·
TAK_TERUKUR 0 / 0; jembatan 33 + 842 + 2 = **877**, + 3 = **880** ·
`cacah_hidup_tanpa_funding` **33**, seluruhnya kelas AWAL (**BNXUSDT 7 · ICPUSDT 13 ·
JUPUSDT 1 · QTUMUSDT 1 · TLMUSDT 11**) · `cacah_simbol_ada_lubang` **122** ·
`cacah_per_simbol_funding` **787** · jumlah uji **1377** (repo riset ini).

**[v60] Kecocokan yang wajib dicatat.** `cacah_hidup_tanpa_funding["BNXUSDT"]` = **7**
dan `cacah_lubang_awal` BNXUSDT = **7**. Angkanya sama. **DILARANG disimpulkan bahwa
kedua medan itu mencacah himpunan yang sama** tanpa pengukuran — satu kecocokan bukan
identitas (KC-52, Koreksi 15). Dicatat sebagai **calon utang ukur**, bukan temuan.

### [v60] Angka BARU dari `reports/lubang_awal.json` (bertanggal 2026-07-30T07:23:11Z)

| simbol | `bulan_pertama` | `akhir_lubang_awal` | `cacah_bulan` (penyebut) | `cacah_lubang_awal` | bentangan rentetan (TURUNAN) | bolong |
| --- | --- | --- | --- | --- | --- | --- |
| **BNXUSDT** | **2022-05** | **2023-01** | **48** | **7** | **9** | **2** |
| ICPUSDT | 2021-05 | 2022-08 | 62 | 16 | 16 | 0 |
| JUPUSDT | 2024-01 | 2024-01 | 30 | 1 | 1 | 0 |
| QTUMUSDT | 2020-02 | 2020-02 | 77 | 1 | 1 | 0 |
| TLMUSDT | 2021-07 | 2023-02 | 60 | 20 | 20 | 0 |

`penyebut_butir_1` **118** · `numerator_butir_1` **118** · `bagian_butir_1` **1.0** ·
`penyebut_butir_2` **5** · `numerator_butir_2` **3** · `bagian_butir_2` **0.6** ·
`cacah_bangkit` **8** · `cacah_laporan_dibaca` **8** · `total_pecahan` **8**.

### Angka dari semesta rentang (v59, tak bertanggal, 95%)

BNXUSDT 2022-04 / 2026-06 / **51** / bentangan 51 / **0 lubang** · BNXUSDTSETTLED
2022-04 / 2023-02 / **6** / 11 / **5** · TLMUSDT 2021-07 / 2026-06 / **60** / 60 /
**0** · TLMUSDTSETTLED 2022-01 / 2023-03 / **9** / 15 / **6**.

### Sidik yang tercatat resmi

- `sidik_kode` `silang_funding` V2
  **`8a9b859c09cd64e30e203e6f8dc53411b8e341c44f112805b3041e5d4d3231b1`**
- `sidik_data_funding`
  **`2c9fbd1b04f74c9c844bc223a99a103d12220b88d08667b3792720e5b9608d24`**
- `sidik_kode_funding`
  **`d38548236f03314eaa648f64f73be5af2f682207be750a2c2fa413fad581513a`**
- `sidik_kode_laporan`
  **`24b6bb265525e81c2e571b46e401f36903383f1e3738c487850861adc3e8c595`**
- `lubang_tengah` V2
  **`c9372bd763b86cfeb2adcf0a0c0c43dae8d9aa9a6508e9c32f7671d5ec7b3f4e`**
- **[v60] `lubang_awal` `sidik_kode`
  `156499ce9d6e822bb7f57786e8e308955441996699c1fd53d0e8814e1f8f2362`**

`semesta_rentang.json` TIDAK memuat medan sidik apa pun dan TIDAK memuat `waktu_utc`.

## Ke bagian 2 dan 3

**Utang lampiran yang lahir dari berkas ini:** EKOR **v19** dan UKUR **v19** wajib
menaikkan kepala ke "milik STATE v60" dan memasukkan: **lajur R-317 dan pengesahan
papan skor 325**; **aturan 90 beserta tabel tiga kejadian**; **kesalahan dokumen butir
18** dan **penanda EKSKLUSIF pada tabel H-A010**; **usulan KC-57 beserta alasan ia
SENGAJA tidak diresmikan**; tabel `lubang_awal.json`; **kelas batas baru "pemotongan
oleh modul"**; **utang ukur 24**; tabel aturan 38 **ke-61, ke-62, ke-63** (dan ke-64
bila sudah lahir) beserta aritmetika panjang deret; status baru **H-A023**.

## Penomoran berikutnya

Jurnal **150** · STATE **v61** · EKOR **v19** · UKUR **v19** · PROMPT **v55 (belum
didorong, utang sepuluh versi)** · ADR **A022** · KC **KC-58** · aturan **91** ·
hipotesis **H-A024** · ramalan **R-318** · papan skor **325** · aturan 38 **ke-64** ·
aturan 52 **ke-31**.

**Poros yang tersisa, urut prioritas:**

1. **BNXUSDT — NAMA kedua bulan absen.** Bentuknya menyempit tajam: bukan lagi "bulan
   mana di antara 50", melainkan **"dua bulan mana di antara sembilan, 2022-05..2023-01"**.
   Bahan yang menamai bulan per simbol **masih belum ditemukan**. Calon berikutnya:
   **`reports/bulan_absen.json`** (249.992 B — besar, berisiko terpotong) dan modul
   penulisnya `bulan_absen.py` (`10279d72`), yang **wajib dibaca lebih dulu** (aturan
   86 b). `kehidupan_arsip_*.json` tetap **DICORET**.
2. **R-305 — periksa apakah sudah pernah diadjudikasi** (`journal/2026-07-30-125.md`).
   Bila belum, ia MENUNGGU dan papan skor kurang lengkap.
3. **Sebab kekosongan TLMUSDT 2023-03** — bulannya terukur ADA; yang kosong isinya.
4. **Tebing `2025-07` dan BTCSTUSDT** — terukur 2021-03..2026-06, 64 bulan, tanpa
   lubang; keserian dengan LITUSDT BELUM diukur. **[v60] Catatan baru:** BTCSTUSDT
   muncul di `lubang_awal.json` dengan `cacah_mati` **63** dari `cacah_bulan` **64**.
5. **Identitas dua belas simbol-bulan karantina** — manifes 20.533.802 B. Bukan murah.
6. **Penulis `semesta_rentang.json`** — belum diidentifikasi.
7. Sisanya tidak berubah: selisih 40−38 `diagnosa_kc15`; bentangan 38 kohort; H-A016;
   `mati_tersisip` atas 19.586; R-7/19/20/28/36/37; R-199; R-236..R-247; taksonomi
   lubang tiga kelas; bagian `baris_mati`.

**Prasyarat klasifikasi — SATU BLOKIR MENYEMPIT, tidak ada yang lunas.** Serapan
funding **matang sebagai pembukuan, belum matang sebagai landasan fitur**. Enam blokir:
(1) ADR-A003 taksonomi rezim **belum ada**; (2) keanggotaan penyebut — **48 kini
TERUKUR sebagai cacah bulan penyebut BNXUSDT**, dan 48 / 50 / 51 **terdamaikan secara
aritmetika**, tetapi **nama** bulan tetap tidak diketahui, jadi blokir **menyempit,
bukan lunas**; (3) `baris_mati` terpotong 54%; (4) kelas positif tipis 33 dari lima
simbol (KC-47); (5) irisan 787 lawan 787 belum didamaikan (KC-52); (6) taksonomi lubang
masih **BENTUK, bukan MEKANISME** (KC-54, usulan 88).

**Syarat praregistrasi R-318 — kumulatif, seluruhnya WAJIB, kini EMPAT BELAS:** aturan
**79** · **83** · **84** · **85** · **86 (a) dan (b)** · **87** · **90** (bila push akar
terlibat) · **pemeriksaan kebebasan medan terhadap kode sumbernya, tertulis, sebelum
pita dikunci** · **KC-50** · **KC-52** · **KC-53** · **KC-54** · **KC-55** · **KC-56** ·
**[BARU] KC-57** (bila angka dasar diambil dari tabel lampiran, pemetaan kolom → medan
laporan WAJIB ditulis) · **[BARU] batas laporan** (bila modul penulis memuat batas
baris, syarat gugur tersurat WAJIB) · aturan **66**. Semangat **usulan 88** dan
**usulan 89** ditaati sukarela.
