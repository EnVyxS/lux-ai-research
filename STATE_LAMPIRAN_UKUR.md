# STATE LAMPIRAN UKUR - v22

Lampiran ukur bagi `STATE.md` v64 (commit `7c479f1a`). Berisi angka terukur **beserta status
utang dan larangan yang melekat padanya**. Indeks, rantai, dan registri ada di
`STATE_LAMPIRAN_EKOR.md` v22 (commit `c282a438`).

**Ditulis:** 2026-07-31, menggantikan v21 (commit `e86f468f`).

> **PERINGATAN KEUTUHAN.** Berkas ini **ditulis ulang**, bukan ditambal. Butir tertentu dari
> v21 mungkin tidak terbawa kata demi kata. **v21 tetap sah di riwayat git pada commit
> `e86f468f`** dan menjadi rujukan bagi apa pun yang tidak muncul di sini.

> **ATURAN PEMAKAIAN BERKAS INI (aturan 94 / ADR-A024 keputusan 5).**
> *Tidak ada angka boleh dikutip di tahap mana pun tanpa status utangnya.*
> Setiap angka di bawah ini membawa statusnya sendiri. Angka tanpa status adalah pelanggaran.

---

## 1. Penyebut - tulang punggung seluruh riset

| angka | arti | status |
| --- | --- | --- |
| **19.586** | penyebut lolos gerbang = `penyebut_kehidupan` | SAH, bersaksi ganda bebas |
| **19.598** | rilis penuh = 19.586 + 12 karantina | SAH |
| **18.999** | lolos dan tidak terhenti | SAH (R-322) |
| **587** | lolos dan terhenti | SAH (R-322) |
| **12** | dikarantina | SAH |

**18.999 + 587 = 19.586** - pendamaian ini diukur ulang oleh `peta_funding.py`, modul yang
tidak mewarisi kode penghitung penyebut sebelumnya. **Saksi kedua yang bebas.**

**19.586 + 12 = 19.598** - dikonfirmasi dua modul (`peta_manifes`, `peta_funding`) atas
manifes yang sama. **Bukan dua saksi bebas** - satu data, dua pembaca.

**Pecahan manifes:** 2.411 - 2.468 - 2.337 - 2.154 - 2.497 - 2.741 - 2.652 - 2.338 =
**19.598**. Identik antara kedua modul.

**DILARANG:** memakai **712.925** sebagai penyebut (KC-50) - mempertukarkan penyebut
karantina dengan penyebut bulan absen (aturan 76, KC-39) - mempertukarkan **937** dengan
**787** (utang ukur 36).

---

## 2. LABEL FUNDING - temuan pokok, R-323

### 2.1 Tabel silang - sumber label

Sumber: `reports/silang_funding.json`, jalur `.ringkasan.tabel_silang`.

| | `funding_ada` | `funding_hilang` | baris |
| --- | --- | --- | --- |
| **HIDUP** | **18.054** | **33** | 18.087 |
| **MATI** | **559** | **842** | 1.401 |
| **SEPI** | **96** | **2** | 98 |
| **jumlah** | 18.709 | 877 | **19.586** |

**Status: SAH sebagai pembukuan. BELUM DIUJI ketepatannya terhadap kenyataan funding.**

Keenam sel ditemukan dengan jalur lengkapnya oleh `sumber_funding.py`, modul yang tidak
membaca kode penulis tabel itu. `enam_sel_lengkap` true - `jumlah_cocok_19586` true.

**Pendamaian bebas:** panjang larik `.baris_mati` = **1.401** = 559 + 842.
`kardinalitas_maksimum` seluruh berkas juga 1.401.

### 2.2 Kelas positif

`.baris_hidup_tanpa_funding` - larik **33** baris. Ada identik di `silang_funding.json` dan
`hidup_tanpa_funding.json`; keduanya membawa `versi_silang_funding` 2 dan `sidik_data_funding`
yang sama. **Petikan, bukan saksi kedua.**

Pembagian per simbol, terukur lewat `cacah_lima_simbol_dalam_wadah_33`:
**BNX 7 - ICP 13 - JUP 1 - QTUM 1 - TLM 11 = 33.**

**Ketakseimbangan kelas: 33 : 19.553.**
**DILARANG melaporkan angka akurasi apa pun tanpa menyebut nisbah ini.**

### 2.3 `funding_ada` di manifes - MEDAN MATI

`sebaran_nilai` = `{"null": 19598}`. Seluruhnya null, merata di kedelapan pecahan,
`cacah_kunci_hilang` **0**. `cacah_simbol_funding_true` 0 - `cacah_bulan_funding_true` 0 -
`cocok_33` false - `cocok_lima_simbol` false.

**DILARANG** memakai manifes sebagai sumber label funding.
**DILARANG** menyimpulkan bahwa data funding tidak ada - hanya **manifes** yang tak memuatnya.
**DILARANG** menyatakan tabel silang **benar** - yang terukur hanya bahwa ia lengkap dan
konsisten sendiri.

### 2.4 Sendi medan

`terhenti` bersendi **simbol** (R-322). `funding_semesta.json` bersendi **simbol** -
`.per_simbol` kardinalitas **787**, `tipe_puncak` peta, `kardinalitas_puncak` 47 (R-323).
**DILARANG** menggeneralkan dua kejadian menjadi pola.

---

## 3. Simbol

| angka | arti | status |
| --- | --- | --- |
| **787** | simbol unik di manifes | SAH; `cocok_787` true |
| **769** | lolos `POLA_SIMBOL` | SAH |
| **18** | tidak lolos pola | SAH; **cacat pola, bukan cacat data** |
| **937** | simbol di `semesta_bulan_1m.json` | SAH; selisih 150 **TIDAK TERJELASKAN** |
| **122** | simbol berlubang | SAH |
| **27** | simbol terhenti | SAH |

**Delapan belas simbol tak berpola** (daftar UTUH, `dipotong` false, penyebut 18):
TUSDT 41 - WUSDT 27 - GUSDT 23 - DUSDT 18 - SUSDT 18 - AUSDT 14 - BUSDT 14 - FUSDT 13 -
HUSDT 13 - CUSDT 12 - MUSDT 12 - QUSDT 10 - 4USDT 9 - VUSDT 2 - OUSDT 1 - dan tiga simbol
beraksara Tionghoa dengan 9, 6, dan 4 bulan.

Deteksi medan tetap sah: 769/787 = **97,7%**; (19.598-246)/19.598 = **98,7%**; keduanya di
atas ambang 0,9.

**DILARANG** membaca ke-18 simbol ini sebagai anomali data.

---

## 4. Kehidupan dan funding

| angka | arti | status |
| --- | --- | --- |
| **18.087** | HIDUP | SAH; = 18.054 + 33 |
| **1.401** | MATI = `cacah_mati` | SAH; = 559 + 842; panjang larik `.baris_mati` |
| **98** | SEPI | SAH; = 96 + 2 |
| **33** | `cacah_hidup_tanpa_funding` | SAH; kelas positif |
| **880** | `cacah_lubang_funding` | SAH |
| **877** | 45/826/0/6 | SAH |
| **880** | 48/826/6 | SAH |

**DILARANG** menyamakan **587** dengan **1.401** atau dengan **33**. Ketiganya angka berbeda
yang gampang tertukar.

---

## 5. Baris dan byte

| angka | arti |
| --- | --- |
| **839.842.134** | baris rilis penuh = 24.801.034 + 815.041.100 |
| 839.325.999 | baris parquet lolos |
| 516.135 | baris parquet karantina |
| 24.801.034 | baris pada 587 simbol-bulan terhenti (min 3.900, maks 44.640) |
| 815.041.100 | baris pada 19.011 tidak terhenti (min 330) |
| 32.706.262.375 | byte parquet |
| 26.532.925.083 | byte zip |
| 13.247.705 | byte parquet karantina |
| 20.533.802 | `byte_manifes_total` |

**Boolean manifes:** `berheader` **17.646** = 17.257 + 389 (sepakat lintas modul) sehingga
1.952 tanpa header - `dikemas` 19.586 - `gerbang_lolos` 19.586 - `karantina` 12 -
`gagal_unduh` 0 - `gagal_checksum` 0 - `baris_dibuang` 0 - **`terhenti` 587**.

**Silang terhenti (R-322):** pada `terhenti=True`, `gerbang_lolos=True` 587 -
`karantina=False` 587 - `dikemas=True` 587 - `gagal_unduh=False` 587.
**Ke-587 baris terhenti bersih seluruhnya.**

**DILARANG** menuliskan "27 simbol berhenti diperdagangkan di bursa" sebagai terukur -
riset ini tidak pernah mengukur status pencatatan bursa.
**DILARANG** memakai besar berkas sebagai detektor status.

---

## 6. Nisbah terukur yang mudah disalahbaca

| nisbah | nilai | peringatan |
| --- | --- | --- |
| terhenti pada bulan terakhir | 27 / 587 = **0,0460** | ramalan R-322 butir 4 menduga >= 0,50; **MELESET** |
| deteksi simbol | 769 / 787 = 97,7% | pembilangnya cacat pola |
| deteksi entri | 98,7% | idem |
| defisit terbesar | 2.130 / 44.640 = **95,2%** | TLMUSDT 2023-03 |
| nisbah karantina BNX 2022-08 | 40.320 / 44.640 = 0,903226 | - |
| KC-52 | 0,127% | DIPERSEMPIT oleh ADR-A022 |

**DILARANG** membaca kenaikan nisbah sebagai perbaikan mutu.
**DILARANG** membaca nisbah yang diam sebagai kestabilan.

---

## 7. KOREKSI 18 sampai 21

**KOREKSI 18** - pemotongan `76%` pada daftar `reports/` adalah batas volume teks alat baca,
**bukan** cacah berkas. Dengan `fields` sebagai larik, daftar utuh.

**KOREKSI 19** - cacat penggabung kardinalitas `peta_manifes.py` (`BATAS_KARDINALITAS = 24`;
di atas itu `setdefault` menyimpan nilai pecahan pertama saja).
**DILARANG dikutip sebagai angka semesta:** bulan 77 - simbol 99 - `checksum_zip_sha256`
2.411 - `parquet` 2.408 - `sumber_url` 2.411 - `awal_sejati_utc` 176 - `akhir_sejati_utc` 81.
Hanya blok `sensus` yang sah. `contoh` bias alfabetis, **bukan sampel acak**.
Cacat ini **tidak diwariskan** ke `peta_funding.py` maupun `sumber_funding.py`.

**KOREKSI 20** - `POLA_SIMBOL` `^[A-Z0-9]{2,20}USDT$` menolak ticker beraksara tunggal yang
sah. Cacat pola. Dikuatkan R-323: `VUSDT` muncul di `semesta_bulan_1m.json` dengan 2 bulan.

**KOREKSI 21** - `jangkauan_maksimum_funding` adalah ukuran cacat. (a) Ia hanya memungut
wadah yang **jalur kuncinya memuat teks `funding`**, sehingga `.ringkasan.tabel_silang` -
pengangkut label sesungguhnya - tidak pernah masuk hitungan. (b) Angka **500** yang terpungut
hampir pasti batas pemotongan daftar.
**DILARANG** mengutip `jangkauan_maksimum_funding` sebagai ukuran jangkauan.
**DILARANG** mengutip `ringkas.jangkauan_kurang_dari_semesta` = true sebagai temuan.
**DILARANG** memakai butir 3 R-323 sebagai bukti apa pun - kemenangannya kosong isinya.
Jangkauan sesungguhnya, **19.586**, datang dari butir 5.

**Koreksi UKUR berikutnya: 22.**

---

## 8. Kesalahan dokumen 22, 23, 24

**Butir 22** - taksiran turunan **45** bagi `.github/workflows/` TERBANTAH; cacah tangan **46**.
Selisih +1 TIDAK TERJELASKAN, menjadi **utang ukur 34**.
**DILARANG** mengutip 44 sebagai cacah tangan sah sampai utang ukur 34 lunas.

**Butir 23** - prosa rusak di jurnal 162 bagian 2: "Pada ketiga puluh - tepatnya ketujuh belas
dan seterusnya". Angkanya benar, kalimatnya rusak. Ditemukan oleh bacaan ulang aturan 52
ke-61 itu sendiri.

**Butir 24 - BARU** - celah pencacah aturan 52 di EKOR v22: bagian 6 mencatat "ke-66"
sementara bagian 14 menyebut berikutnya "ke-68", sehingga **ke-67 tidak bernama**. Sebabnya
bukan kelalaian melainkan **batas rekam-diri**: ke-67 adalah bacaan ulang EKOR v22 itu
sendiri, yang mustahil dicatat di dalam dirinya sebelum ia ada. Dibukukan supaya pembaca
tidak menyangka satu pemakaian hilang.

**Kesalahan dokumen berikutnya: butir 25.**

Cacat dokumen lama yang tetap berlaku:
**Butir 19** - UKUR v19 (`c28202df`) terdorong terpotong tanpa peringatan; utang verifikasi 47.
**Butir 20 / KOREKSI 17** - `ADR-A004.md` bagian 2.2 mencacah **LIMA** klausa sedangkan
`gerbang_1m.py` **ENAM**; utang verifikasi 48.
**Butir 21** - ruang vonis butir 2 dan 4 jurnal 155 hanya tiga sisi; ADR-A023 mempertegas
aturan 89 menjadi **empat sisi wajib**.

---

## 9. Papan skor

**350 - SAH.** TEPAT **240** - MELESET **68** - SEPARUH **22** - TIDAK TERADJUDIKASI **16** -
MENUNGGU **1**.

| ramalan | vonis |
| --- | --- |
| R-319 | 2 TEPAT / 2 MELESET / 1 TIDAK TERADJUDIKASI |
| R-320 | **5 TIDAK TERADJUDIKASI dari 5** |
| R-321 | 4 TEPAT diskor + 1 MUDAH tidak diskor |
| R-322 | **3 TEPAT / 2 MELESET** |
| R-323 | **4 TEPAT / 1 MELESET** |

**R-323 rinci:** butir 1 wadah 33 TEPAT - butir 2 `cacah_lima_simbol` **MELESET** (terukur 36,
bukan 33; selisihnya 10 = 7 + 3 BNXUSDT di `lubang_tak_dikenal`) - butir 3 TEPAT pada huruf,
kosong isinya - butir 4 787 peta TEPAT - butir 5 enam sel TEPAT.

**Aturan 79:** rekor delapan (R-314..R-321) **BERAKHIR** di R-322. Tidak ada rekor berjalan.
**DILARANG** menulis rekor sembilan. **DILARANG** menghidupkan rekor yang sudah berakhir.
**DILARANG** membaca putusnya rekor sebagai kemunduran mutu.

**Vonis yang DILARANG diubah:** R-315 butir 2, R-317 butir 3 dan 4, R-319, R-320 -
tidak satu pun boleh ditulis SEPARUH. Kelima butir R-320 TIDAK TERADJUDIKASI **permanen**.
**DILARANG** menyamakan "nol menang" dengan "nol diuji".
**DILARANG** memasukkan butir 3 R-321 ke papan skor.
**DILARANG** menskorkan konfirmasi "12 = 11 + 1".

---

## 10. Utang - ringkas dengan lapis

**LAPIS A: KOSONG.** Blokir 4 TERPECAHKAN - utang ukur 32 LUNAS - utang ukur 35 LUNAS -
utang verifikasi 50 LUNAS. **Keempatnya dibayar dengan pengukuran, nol ditutup paksa.**

**Utang ukur HIDUP:** 6 - 7 - 17 - 21 - 22 - 26 - 27 - 30 - 31 - 33 - 34 - **36**.
Berikutnya 37.

**UTANG UKUR 36 (Lapis B):** `semesta_bulan_1m.json` mencacah **937** simbol; manifes **787**.
Selisih **150 TIDAK TERJELASKAN**. Nama-namanya tercatat verbatim di STATE v64 bagian 7.2.
**DILARANG menyebut jenis instrumen apa pun bagi nama-nama itu** - riset ini tidak pernah
mengukur kelas aset. **DILARANG menduga sebabnya.**

**Utang verifikasi HIDUP:** 24 - 45 - 46 - 47 - 48 - 49 - 51 - **52** - **53**. Berikutnya 54.
Utang 51, 52, 53 = tiga modul baru tanpa pasangan uji (`peta_manifes`, `peta_funding`,
`sumber_funding`). Jumlah uji tetap **1377**.
**DILARANG** membaca ketiadaan uji baru sebagai mutu.

**DAFTAR UTANG DITUTUP PAKSA: masih KOSONG.** Lapis B dan C sudah resmi tetapi belum
dijalankan. **DILARANG** menulis utang yang ditutup paksa sebagai lunas.
**DILARANG** mengurangkannya dari cacah utang.
**DILARANG** membaca pendeknya daftar utang hidup sebagai kematangan bila daftar matinya
tidak disebut.

---

## 11. Angka lain yang mengikat

**R-315 FINAL:** `lubang_tak_dikenal` tiga butir, seluruhnya BNXUSDT - 2022-04, 2022-06,
2022-08. `bulan_klines_pertama` 2022-05, `cacah_bulan_klines_simbol` 48.
**Dikuatkan saksi bebas R-323:** BNXUSDT muncul 10 kali di `hidup_tanpa_funding.json`;
10 = 7 (dalam larik 33) + 3 (`lubang_tak_dikenal`).
**DILARANG** membaca `lubang_tak_dikenal` sebagai "bulan sebelum simbol lahir".
**DILARANG** menggeneralisasi pola BNXUSDT ke 786 simbol lain.
**DILARANG** menyimpulkan sebab hilangnya hari bulat BNXUSDT.

**KC-15:** 1.650 + 1.440 + 4.320 = **7.410**; 7.410 - 210 = **7.200** = 5 x 1.440; pembagian
**1 + 3 + 1** hari; 210 menit TEPI (peluncuran 03:30 UTC, `stempel_pertama_ms`
1648783800000); KC-14 **9** simbol-bulan / **6.375** menit; 9 + 3 = **12**;
6.375 + 7.200 = **13.575**.

**Defisit:** total 18.143.601 - pertama 17.335.439 - bukan pertama 808.162 - sembilan 95.237 -
sisa 712.925 (**DILARANG jadi penyebut**, KC-50) - calon 17.398 = 17.284 + 114.

**Tebing:** `cacah_tebing_butir_2` **39** pada 2025-07.

**Bulan absen:** `cacah_nama_berabsen` 10 - `jumlah_bulan_absen` 11 - `cacah_pasangan` 15 -
`sebaran_pembeda` `{gagal_gerbang: 11}`. Berabsen nol: BDXNUSDT, ICPUSDT, MINAUSDT, SXPUSDT,
TLMUSDT. **KOREKSI 14/15:** `bulan_per_simbol` berarti "berapa bulan"; `cacah_bulan` bukan
bentangan kalender.
**DILARANG** menyimpulkan hanya simbol berpasangan settled yang berabsen.

**Lubang awal:** `cacah_baris_penyebut_butir_1_dilapor` **60** vs penyebut **118** -
**PEMOTONGAN OLEH MODUL** (`BATAS_BARIS_LAPORAN = 60`), tidak berteriak.
**DILARANG** menarik cacah dari `baris_penyebut_butir_1`.

**Gerbang 1m:** **ENAM** klausa; `tests/test_gerbang_1m.py` menegaskan
`assert len(g.KLAUSA) == 6`, 16 uji.
**DILARANG** menyebut gerbang 1m "berlapis enam" di artefak mengikat sebelum utang ukur 31
lunas dari kode. **DILARANG** mengutip "100% bersih 84 simbol-bulan" sebagai bukti enam
klausa bersih. **DILARANG** menjumlahkan 1377 + 16.
**DILARANG** menyebut `selaras_menit` / `satuan_milidetik` mustahil menyala.
**DILARANG** menyimpulkan `deret_tidak_kosong` diselundupkan.

**Karantina:** dua belas, `pelanggaran` SERAGAM `["jarak_60_detik","tanpa_menit_hilang"]`.
**DILARANG menyebut jenis instrumen karantina.**

---

## 12. Penomoran

UKUR berikutnya **v23**. Koreksi UKUR berikutnya **22**. Kesalahan dokumen berikutnya **25**.
Utang ukur berikutnya **37**. Utang verifikasi berikutnya **54**. Papan skor **350 - SAH**.
Aturan 38 berikutnya **ke-79**. Aturan 52 berikutnya **ke-69**.
Penomoran lengkap ada di `STATE.md` v64 bagian 15.

- akhir UKUR v22 -
