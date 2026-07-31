# STATE LAMPIRAN UKUR - v24

Lampiran ukur bagi `STATE.md` **v66** (commit `95021cda`). Berisi angka terukur **beserta
status utang dan larangan yang melekat padanya**. Indeks, rantai, dan registri ada di
`STATE_LAMPIRAN_EKOR.md` **v23** (commit `25970a88`).

**Ditulis:** 2026-07-31, menggantikan v23 (commit `a88a4631`, blob `59326334`).

> **PERINGATAN KEUTUHAN.** Berkas ini ditulis ulang, bukan ditambal. Butir tertentu dari v23
> mungkin tidak terbawa kata demi kata. **v23 tetap sah di riwayat git pada commit
> `a88a4631`** dan menjadi rujukan bagi apa pun yang tidak muncul di sini.

> ## PERINGATAN TERGANTI ATAS v22 - MASIH BERLAKU
> **v22 (`ae483de8`) memuat dua pernyataan yang SALAH** karena keadaan berubah sesudahnya:
> 1. Bagian 9 menulis **TIDAK TERADJUDIKASI 16**. Nilai sah **21**.
> 2. Bagian 10 menulis **"DAFTAR UTANG DITUTUP PAKSA: masih KOSONG"**. Daftar itu terisi
>    **tiga belas butir**.
>
> **DILARANG mengutip v22 bagian 9 dan 10.** Bagian lain v22 tetap sah.
> Larangan ini **diteruskan**, bukan dicabut, oleh v24.

> **ATURAN PEMAKAIAN BERKAS INI (aturan 94 / ADR-A024 keputusan 5).**
> *Tidak ada angka boleh dikutip di tahap mana pun tanpa status utangnya.*
> Angka tanpa status adalah pelanggaran.

---

## 1. Penyebut - tulang punggung seluruh riset

| angka | arti | status |
| --- | --- | --- |
| **19.586** | penyebut lolos gerbang = `penyebut_kehidupan` | SAH, bersaksi ganda bebas |
| **19.598** | rilis penuh = 19.586 + 12 | SAH |
| **18.999** | lolos dan tidak terhenti | SAH (R-322) |
| **587** | lolos dan terhenti | SAH (R-322) |
| **12** | dikarantina | SAH |

**18.999 + 587 = 19.586** diukur ulang oleh `peta_funding.py`, modul yang tidak mewarisi kode
penghitung penyebut. **Saksi kedua yang bebas** - tetapi modul itu **tak berpasangan uji**
(ditutup paksa B-3). Kekuatan pendamaian ini terletak pada **kebebasan sumbernya**, bukan
pada terverifikasinya kodenya. **DILARANG** menyajikannya sebagai hasil terverifikasi.

**19.586 + 12 = 19.598** dikonfirmasi dua modul atas manifes yang sama.
**Bukan dua saksi bebas** - satu data, dua pembaca.

**Pecahan manifes:** 2.411 - 2.468 - 2.337 - 2.154 - 2.497 - 2.741 - 2.652 - 2.338 = **19.598**.

> **PERINGATAN GERBANG (B-1).** Ke-19.586 simbol-bulan itu lolos lewat gerbang 1m berklausa
> **ENAM**, sedangkan dokumen keputusan yang mengesahkannya hanya menyebut **LIMA**.
> Utang ini **ditutup paksa, bukan dibayar**. Bila satu klausa ternyata tak berdasar,
> penyebut ini ikut tergugat. **Wajib disebut setiap kali 19.586 dikutip di artefak mengikat.**

**DILARANG:** memakai **712.925** sebagai penyebut (KC-50) - mempertukarkan penyebut karantina
dengan penyebut bulan absen (aturan 76, KC-39) - mempertukarkan **937** dengan **787**.

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

Keenam sel ditemukan dengan jalur lengkapnya oleh `sumber_funding.py` - modul yang tidak
membaca kode penulis tabel itu, tetapi **tak berpasangan uji** (ditutup paksa B-4).
`enam_sel_lengkap` true - `jumlah_cocok_19586` true.

**Pendamaian bebas:** panjang larik `.baris_mati` = **1.401** = 559 + 842.
`kardinalitas_maksimum` seluruh berkas juga 1.401.

### 2.2 Kelas positif

`.baris_hidup_tanpa_funding` - larik **33**. Ada identik di `silang_funding.json` dan
`hidup_tanpa_funding.json`; keduanya membawa `versi_silang_funding` 2 dan `sidik_data_funding`
yang sama. **Petikan, bukan saksi kedua.**

Pembagian per simbol: **BNX 7 - ICP 13 - JUP 1 - QTUM 1 - TLM 11 = 33.**

**Ketakseimbangan kelas: 33 : 19.553.**
**DILARANG melaporkan angka akurasi apa pun tanpa menyebut nisbah ini.**

### 2.3 `funding_ada` di manifes - MEDAN MATI

`sebaran_nilai` = `{"null": 19598}`, merata di kedelapan pecahan, `cacah_kunci_hilang` **0**.
`cocok_33` false - `cocok_lima_simbol` false.

**DILARANG** memakai manifes sebagai sumber label funding.
**DILARANG** menyimpulkan data funding tidak ada - hanya **manifes** yang tak memuatnya.
**DILARANG** menyatakan tabel silang **benar**; yang terukur hanya **lengkap dan konsisten
dengan dirinya sendiri**.

### 2.4 Sendi medan

`terhenti` bersendi **simbol**. `funding_semesta.json` bersendi **simbol** - `.per_simbol`
kardinalitas **787**, `tipe_puncak` peta, `kardinalitas_puncak` 47.
**DILARANG** menggeneralkan dua kejadian menjadi pola.

---

## 3. Simbol

| angka | arti | status |
| --- | --- | --- |
| **787** | simbol unik di manifes | SAH; `cocok_787` true |
| **769** | lolos `POLA_SIMBOL` | SAH; polanya **cacat** |
| **18** | tidak lolos pola | SAH; **cacat pola, bukan cacat data** |
| **937** | simbol di `semesta_bulan_1m.json` | SAH; selisih 150 **TIDAK TERJELASKAN** (B-5) |
| **122** | simbol berlubang | SAH |
| **27** | simbol terhenti | SAH |

**Delapan belas simbol tak berpola** (daftar UTUH, `dipotong` false, penyebut 18):
TUSDT 41 - WUSDT 27 - GUSDT 23 - DUSDT 18 - SUSDT 18 - AUSDT 14 - BUSDT 14 - FUSDT 13 -
HUSDT 13 - CUSDT 12 - MUSDT 12 - QUSDT 10 - 4USDT 9 - VUSDT 2 - OUSDT 1 - dan tiga simbol
beraksara Tionghoa dengan 9, 6, dan 4 bulan.

Deteksi medan: 769/787 = **97,7%**; (19.598-246)/19.598 = **98,7%**. **Kedua nisbah membawa
cacat pola di pembilangnya** (KOREKSI 20, ditutup paksa lewat B-3).

**DILARANG** membaca ke-18 simbol ini sebagai anomali data.
**DILARANG** memakai 787 dan 937 secara bergantian - **dua penyebut simbol hidup
berdampingan** dan setiap kutipan wajib menyebut yang mana.

---

## 4. Kehidupan dan funding

| angka | arti | status |
| --- | --- | --- |
| **18.087** | HIDUP = 18.054 + 33 | SAH |
| **1.401** | MATI = 559 + 842 = panjang `.baris_mati` | SAH |
| **98** | SEPI = 96 + 2 | SAH |
| **33** | kelas positif | SAH |
| **880** | `cacah_lubang_funding` | SAH |
| **877** | 45/826/0/6 | SAH |
| **880** | 48/826/6 | SAH |

**DILARANG** menyamakan **587** dengan **1.401** atau dengan **33**.

---

## 5. Baris dan byte

| angka | arti |
| --- | --- |
| **839.842.134** | baris rilis penuh = 24.801.034 + 815.041.100 |
| 839.325.999 | baris parquet lolos |
| 516.135 | baris parquet karantina |
| 24.801.034 | baris pada 587 simbol-bulan terhenti (min 3.900, maks 44.640) |
| 815.041.100 | baris tidak terhenti (min 330) |
| 32.706.262.375 | byte parquet |
| 26.532.925.083 | byte zip |
| 13.247.705 | byte parquet karantina |
| 20.533.802 | `byte_manifes_total` |

**KC-50 - jangan lupa.** 839.842.134 **BUKAN** jumlah lilin; ia total baris parquet rilis
penuh. Jumlah lilin yang dihitung LANGSUNG adalah **839.325.999**. **Selisih 516.135.**
Kedua besaran itu bukan besaran yang sama.

**Boolean manifes:** `berheader` **17.646** = 17.257 + 389 sehingga 1.952 tanpa header -
`dikemas` 19.586 - `gerbang_lolos` 19.586 - `karantina` 12 - `gagal_unduh` 0 -
`gagal_checksum` 0 - `baris_dibuang` 0 - **`terhenti` 587**.

**Silang terhenti:** pada `terhenti=True`, `gerbang_lolos=True` 587 - `karantina=False` 587 -
`dikemas=True` 587. **Ke-587 baris terhenti bersih seluruhnya.**

**DILARANG** menuliskan "27 simbol berhenti diperdagangkan di bursa" sebagai terukur -
riset ini tidak pernah mengukur status pencatatan bursa.
**DILARANG** memakai besar berkas sebagai detektor status.

---

## 6. Nisbah yang mudah disalahbaca

| nisbah | nilai | peringatan |
| --- | --- | --- |
| terhenti pada bulan terakhir | 27 / 587 = **0,0460** | R-322 butir 4 menduga >= 0,50; **MELESET** |
| deteksi simbol | 769 / 787 = 97,7% | pembilang cacat pola |
| deteksi entri | 98,7% | idem |
| defisit terbesar | 2.130 / 44.640 = **95,2%** | TLMUSDT 2023-03 |
| karantina BNX 2022-08 | 40.320 / 44.640 = 0,903226 | - |
| KC-52 | 0,127% | DIPERSEMPIT (ADR-A022) |

**DILARANG** membaca kenaikan nisbah sebagai perbaikan mutu.
**DILARANG** membaca nisbah yang diam sebagai kestabilan.

---

## 7. KOREKSI 18 sampai 21

**18** - pemotongan `76%` daftar `reports/` adalah batas volume teks alat baca, bukan cacah
berkas. Dengan `fields` sebagai larik, daftar utuh.

**19** - cacat penggabung kardinalitas `peta_manifes.py` (`BATAS_KARDINALITAS = 24`).
**DILARANG dikutip sebagai angka semesta:** bulan 77 - simbol 99 - `checksum_zip_sha256`
2.411 - `parquet` 2.408 - `sumber_url` 2.411 - `awal_sejati_utc` 176 - `akhir_sejati_utc` 81.
Hanya blok `sensus` sah. `contoh` bias alfabetis, bukan sampel acak.
Tidak diwariskan ke `peta_funding.py` maupun `sumber_funding.py`.

**20** - `POLA_SIMBOL` `^[A-Z0-9]{2,20}USDT$` menolak ticker beraksara tunggal yang sah.
Dikuatkan R-323: `VUSDT` muncul di berkas 937 dengan 2 bulan.

**21** - `jangkauan_maksimum_funding` ukuran cacat. (a) Hanya memungut wadah yang jalur
kuncinya memuat teks `funding`, sehingga `.ringkasan.tabel_silang` tidak pernah masuk
hitungan. (b) Angka **500** hampir pasti batas pemotongan daftar.
**DILARANG** mengutipnya sebagai ukuran jangkauan. **DILARANG** mengutip
`ringkas.jangkauan_kurang_dari_semesta` sebagai temuan. **DILARANG** memakai butir 3 R-323
sebagai bukti apa pun. Jangkauan sesungguhnya, **19.586**, datang dari butir 5.

**Koreksi berikutnya: 22.**

---

## 8. Kesalahan dokumen 22 sampai 25

**22** - taksiran turunan **45** bagi `.github/workflows/` terbantah; cacah tangan **46**;
selisih +1 tidak terjelaskan (utang ukur 34, ditutup paksa C-1).
**DILARANG** mengutip **44** sebagai cacah tangan sah.

**23** - prosa rusak di jurnal 162 bagian 2. Angkanya benar, kalimatnya rusak.

**24** - celah pencacah aturan 52 di EKOR v22: bagian 6 mencatat ke-66 sementara bagian 14
menyebut berikutnya ke-68, sehingga ke-67 tidak bernama. Sebabnya **batas rekam-diri**,
bukan kelalaian. Penangkalnya kini dipakai tersurat: nomor bacaan-diri **dinamai di muka**.

### 8.1 Butir 25 - PENGENAL TERTUKAR, sebab TERUKUR

Registri EKOR v22 bagian 5 mencatat, bagi **lima ADR berurutan**, nilai yang tidak cocok
dengan blob terukur pada tip `470acfbb`. Sembilan belas entri lain cocok persis.

Dibayar dengan `list_commits` berparameter `path` atas kelima berkas:

| ADR | tercatat EKOR v22 | commit **tunggal** penyentuh berkas | blob SAH pada `470acfbb` |
| --- | --- | --- | --- |
| A009 | `17a594b6` | `17a594b69e243a83884862122f01b5e1ade4278a` | `85796418` |
| A010 | `c4bccf21` | `c4bccf219ddcc3495265331b4cbce9a3ea806eb5` | `6de941f7` |
| A011 | `645fd5df` | `645fd5df1c973cc5c6336ebc6cee3786a6eb347a` | `312638e9` |
| A012 | `f9f564d1` | `f9f564d17d7ec688b613679e77f67d7974d0091f` | `0c474067` |
| A013 | `8ba4f989` | `8ba4f989be545783e885caa21b9834e0456da4b7` | `3a7f8612` |

**SEBAB TERUKUR: keliru JENIS pengenal, bukan keliru nilai.** Kolom berjudul blob memuat
**SHA commit**. Kelima nilai cocok sempurna sebagai commit dan **nol** sebagai blob.

**Kemungkinan tandingan TERBANTAH:** tiap berkas disentuh **tepat satu commit**, jadi tidak
pernah diubah sesudah dibuat, jadi blobnya tidak mungkin pernah berganti.

**Kelas cacat: PENGENAL TERTUKAR - sekerabat KC-50, kesunyian bukan galat.** Dua jenis
pengenal sama panjang dan sama bentuk dalam satu kolom; tidak ada alat yang berteriak.
Penangkalnya: **adu registri dengan daftar direktori**, bukan membaca registri sendirian.
**Registri yang rapi bukan registri yang benar.**

**Berikutnya: butir 26.**

Cacat lama yang tetap berlaku:
**19** - UKUR v19 (`c28202df`) terdorong terpotong tanpa peringatan (utang verifikasi 47,
ditutup paksa C-2). **DILARANG** menyatakan butir 19 kejadian tunggal.
**20 / KOREKSI 17** - `ADR-A004.md` bagian 2.2 mencacah LIMA klausa, `gerbang_1m.py` ENAM
(utang verifikasi 48, ditutup paksa B-1).
**21** - ruang vonis jurnal 155 hanya tiga sisi; aturan 89 dipertegas menjadi empat sisi.

---

## 9. Papan skor

**350 - SAH.** Tidak berubah sejak v23.

| vonis | cacah |
| --- | --- |
| TEPAT | **240** |
| MELESET | **68** |
| SEPARUH | **22** |
| **TIDAK TERADJUDIKASI** | **21** |
| MENUNGGU | **1** |

**TIDAK TERADJUDIKASI naik 16 -> 21** oleh penutupan paksa C-4: R-305, R-288, R-290, R-228,
R-291. **Kenaikan ini wajib disebut.** Nilai **16** di UKUR v22 **TIDAK BERLAKU**.

| ramalan | vonis |
| --- | --- |
| R-319 | 2 TEPAT / 2 MELESET / 1 TIDAK TERADJUDIKASI |
| R-320 | **5 TIDAK TERADJUDIKASI dari 5** |
| R-321 | 4 TEPAT diskor + 1 MUDAH tidak diskor |
| R-322 | **3 TEPAT / 2 MELESET** |
| R-323 | **4 TEPAT / 1 MELESET** |

**R-323 rinci:** butir 1 wadah 33 TEPAT - butir 2 `cacah_lima_simbol` **MELESET** (terukur 36;
selisihnya 10 = 7 + 3 BNXUSDT di `lubang_tak_dikenal`) - butir 3 TEPAT pada huruf, **kosong
isinya** - butir 4 787 peta TEPAT - butir 5 enam sel TEPAT.

**Aturan 79:** rekor delapan **BERAKHIR** di R-322. Tidak ada rekor berjalan.
**DILARANG** menulis rekor sembilan atau menghidupkannya kembali.
**DILARANG** membaca putusnya rekor sebagai kemunduran mutu.

**Vonis yang DILARANG diubah:** R-315 butir 2 - R-317 butir 3 dan 4 - R-319 - R-320.
Kelima butir R-320 TIDAK TERADJUDIKASI **permanen**.
**DILARANG** menyamakan "nol menang" dengan "nol diuji".
**DILARANG** memasukkan butir 3 R-321 ke papan skor.
**DILARANG** menskorkan konfirmasi "12 = 11 + 1".
**DILARANG** memakai `uji_r305`, `uji_r288`, atau `uji_r291` sebagai adjudikasi.

---

## 10. Utang

### 10.1 LAPIS A - KOSONG

Blokir 4 **TERPECAHKAN** - utang ukur 32 **LUNAS** - utang ukur 35 **LUNAS** -
utang verifikasi 50 **LUNAS** - **utang ukur 37 LUNAS** (bagian 8.1).
Seluruhnya **dibayar dengan pengukuran**, nol ditutup paksa.

Utang ukur **37** lahir di EKOR v23 dan dibayar pada giliran berikutnya. Ia **tidak pernah
digolongkan lapis** dan **tidak pernah ditutup paksa**, sehingga menyebutnya lunas sah dan
tidak melanggar larangan atas daftar mati.

### 10.2 DAFTAR UTANG DITUTUP PAKSA - TIGA BELAS BUTIR

Pernyataan "masih KOSONG" di UKUR v22 **TIDAK BERLAKU**. Cacah **tidak berubah** di v24.

**LAPIS B (berlabel mengikat):** B-1 ukur 31 + verifikasi 48 - B-2 verifikasi 51 -
B-3 verifikasi 52 - B-4 verifikasi 53 - B-5 ukur 36 - B-6 bacaan `pulihkan.py`.

**LAPIS C (catatan ringkas):** C-1 ukur 33 dan 34 - C-2 verifikasi 47 - C-3 cacah tangan
`tests/` dan akar - C-4 lima adjudikasi tangan - C-5 sisa bacaan - C-6 PROMPT v55 -
C-7 manifes pecahan dan `kehidupan_arsip_*`.

Label penuh ada di **jurnal 165** (`e915041e`, blob `31505537`) dan ringkasnya di
**STATE v66 bagian 6**.

**Penutupan paksa BUKAN pelunasan.** DILARANG menulisnya lunas - DILARANG mengurangkannya
dari cacah utang - DILARANG mengutip angka yang bergantung padanya tanpa labelnya -
DILARANG memakai jurnal 165 untuk menutup utang yang lahir sesudahnya.

**Catatan C-6.** `PROMPT.md` v55 kini **ADA** (`91d90c3f`, blob `5fd36c6f`, 16.780 B).
**C-6 tetap DITUTUP PAKSA**; keberadaan v55 tidak menjadikannya lunas dan tidak mengurangi
cacah tiga belas butir.

### 10.3 Utang HIDUP

**Utang ukur hidup:** 6 - 7 - 17 - 21 - 22 - 26 - 27 - 30. Berikutnya **38**.
(31, 33, 34, 36 ditutup paksa; 32, 35, **37** lunas.)
**Utang verifikasi hidup:** 24 - 45 - 46 - 49. Berikutnya **54**.
(47, 48, 51, 52, 53 ditutup paksa; 50 lunas.)

**DILARANG** membaca pendeknya daftar ini sebagai kematangan bila tiga belas butir yang
ditutup paksa tidak ikut disebut pada napas yang sama.

---

## 11. Cacah tangan - angka terukur beserta tipnya

| cacah | nilai | tip | status |
| --- | --- | --- | --- |
| `lux_ai/serapan/` | **51** (50 tanpa `__init__.py`) | `9d30060e` | SAH |
| `.github/workflows/` | **46** | `9d30060e` | SAH |
| `journal/` | **165** | `470acfbb` | SAH, baru di v24 |
| `decisions/` | **23** | `470acfbb` | SAH, baru di v24 |
| akar repo | **18** = 12 berkas + 6 direktori | `470acfbb` | SAH, baru di v24 |
| `tests/` | 53 | lama | **KEDALUWARSA** |

- `journal/` 165: penomoran 01..165 **utuh tanpa lubang** (59+40+13+28+3+4+18 = 165).
  Cacah berkas dan nomor terakhir bersepakat, tetapi lahir dari **satu daftar** -
  **bukan dua saksi bebas**.
- `decisions/` 23: A001..A024 **tanpa A003**. Menguatkan secara terukur bahwa
  **ADR-A003 belum ada**, bukan sekadar belum ditemukan.
- akar 18: angka lamanya juga 18 dan **KEDALUWARSA** (C-3). **Kesamaan itu BUKAN
  konfirmasi** - angka sama lewat jalan berbeda bukan saksi. C-3 tetap ditutup paksa.

**TURUNAN, DILARANG dikutip sebagai cacah tangan:** serapan **52** - workflows **48**.
**DILARANG** mengutip **44** sebagai cacah tangan sah.

---

## 12. Angka lain yang mengikat

**R-315 FINAL:** `lubang_tak_dikenal` tiga butir, seluruhnya BNXUSDT - 2022-04, 2022-06,
2022-08. `bulan_klines_pertama` 2022-05, `cacah_bulan_klines_simbol` 48.
Dikuatkan saksi bebas R-323: BNXUSDT muncul 10 kali di `hidup_tanpa_funding.json`;
10 = 7 (dalam larik 33) + 3 (`lubang_tak_dikenal`).
**DILARANG** membaca `lubang_tak_dikenal` sebagai "bulan sebelum simbol lahir".
**DILARANG** menggeneralisasi pola BNXUSDT ke 786 simbol lain.
**DILARANG** menyimpulkan sebab hilangnya hari bulat BNXUSDT.

**KC-15:** 1.650 + 1.440 + 4.320 = **7.410**; 7.410 - 210 = **7.200** = 5 x 1.440;
pembagian **1 + 3 + 1** hari; 210 menit TEPI (peluncuran 03:30 UTC, `stempel_pertama_ms`
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
PEMOTONGAN OLEH MODUL (`BATAS_BARIS_LAPORAN = 60`), tidak berteriak.
**DILARANG** menarik cacah dari `baris_penyebut_butir_1`.

**Gerbang 1m:** **ENAM** klausa; `tests/test_gerbang_1m.py` menegaskan
`assert len(g.KLAUSA) == 6`, 16 uji. Jumlah uji semesta **1377** = 1341 + 36.
Cacah uji **1377** dikonfirmasi ulang oleh CI pada bacaan aturan 38 ke-82, ke-83, dan ke-84;
ketiganya **satu pengukur yang sama**, bukan tiga saksi bebas.
**DILARANG** menjumlahkan 1377 + 16.
**DILARANG** menyebut gerbang 1m "berlapis enam" di artefak mengikat seolah keenamnya punya
dasar keputusan - lihat B-1.
**DILARANG** mengutip "100% bersih 84 simbol-bulan" sebagai bukti enam klausa bersih.
**DILARANG** menyebut `selaras_menit` / `satuan_milidetik` mustahil menyala.
**DILARANG** menyimpulkan `deret_tidak_kosong` diselundupkan.

**Karantina:** dua belas, `pelanggaran` SERAGAM `["jarak_60_detik","tanpa_menit_hilang"]`.
**DILARANG menyebut jenis instrumen karantina.**

---

## 13. Enam syarat penyeberangan ke klasifikasi

Wajib ikut setiap kali angka serapan dikutip di tahap mana pun:

1. **Ketakseimbangan kelas 33 : 19.553.**
2. Tabel silang **belum diuji ketepatannya** terhadap kenyataan funding.
3. **Dua penyebut simbol** hidup berdampingan: 787 dan 937 (B-5).
4. Delapan belas simbol tak berpola adalah **simbol sah** (KOREKSI 20).
5. **Ketiga modul penemu tak berpasangan uji** (B-2, B-3, B-4).
6. **Gerbang penyaring penyebut punya ENAM klausa dengan dasar keputusan LIMA** (B-1).

---

## 14. Penomoran

UKUR berikutnya **v25**. Koreksi berikutnya **22**. Kesalahan dokumen berikutnya **26**.
Utang ukur berikutnya **38**. Utang verifikasi berikutnya **54**. Papan skor **350 - SAH**.

Aturan 38 berikutnya **ke-85** (deret ke-42..ke-84 = **43 berturut**).
**Nilai BASI yang wajib DITOLAK pada bacaan ke-85:** run **30628719235** - commit
`95021cda` - blob `fedd1e89...`.

Aturan 52 berikutnya **ke-76**, yaitu pembacaan ulang UTUH berkas ini pada giliran yang sama
(batas rekam-diri; sesudahnya **ke-77**).

Penomoran lengkap ada di `STATE.md` **v66** bagian 16.

- akhir UKUR v24 -
