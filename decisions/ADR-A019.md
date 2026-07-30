# ADR-A019 — Penutupan KC-52, peresmian aturan 86, dan adjudikasi resmi R-312/R-313

- **Status:** DITERIMA
- **Tanggal:** 2026-07-31 (UTC 2026-07-30)
- **Dasar dokumen:** `STATE.md` v54 (blob `af10274dc4b75292d56ff15c369f1e08ccfc5dd3`,
  commit `8368ca1f`) · `STATE_LAMPIRAN_EKOR.md` v13 (blob
  `26ba6dc06fcaa358df3d0ac511996a9bb40a864f`, commit `6642ed68`) ·
  `STATE_LAMPIRAN_UKUR.md` v13 (blob `9e71c1ee9667c4b06389c87e0c77d4cefaca5b96`,
  commit `2bdd8233`) · jurnal 136–140.
- **Syarat ADR-A016 terpenuhi:** keputusan ini diambil pada giliran yang **BERBEDA**
  dari giliran adjudikasi R-312 dan R-313.
- **Ketiga bagian STATE serasi** pada v54 / v13 / v13 saat ADR ini ditulis.

---

## Latar

ADR-A018 meninggalkan dua belas keputusan dan satu poros yang ditetapkan tetapi belum
diuji. Lima giliran sesudahnya menghasilkan: satu poros yang **runtuh sebelum
diadjudikasi** (R-312), satu ramalan yang **menang telak tetapi hampir tidak berisiko**
(R-313), satu identitas besar yang **menutup salah paham berumur berpuluh giliran**
(KC-52), dan satu kelas cacat yang **tidak punya penangkal sama sekali** dalam seluruh
perkakas pemeriksaan kami.

ADR ini memutuskan status resmi kesemuanya. Ia juga **menolak** menutup dua utang yang
secara nomor sudah bisa ditutup, karena menutupnya berarti mengarang.

---

## Keputusan 1 — KC-52 DIRESMIKAN

**Rumusan resmi, satu-satunya yang boleh dikutip:**

> Dua angka yang keduanya benar dapat dijajarkan berpuluh giliran tanpa satu pun
> pemeriksaan formal menyadari bahwa **penyebutnya berbeda**. Selisih di antara
> keduanya lalu dibaca sebagai cacat pengukuran, padahal ia adalah **himpunan yang
> memang tidak dihitung**. Tidak ada invarian, kendali, sidik kode, atau pembacaan
> ulang yang menangkap kelas ini, sebab tak satu pun dari angka itu salah.

**Kejadian yang meresmikannya:**

| angka | himpunan | satuan |
| --- | --- | --- |
| **839.325.999** | 19.586 simbol-bulan **lolos gerbang** | baris parquet |
| **516.135** | **12** simbol-bulan **karantina** | baris parquet |
| **839.842.134** | 19.598 simbol-bulan **seluruh rilis** | baris parquet |

**839.325.999 + 516.135 = 839.842.134** dan **19.586 + 12 = 19.598**.

**Sebab strukturalnya terukur, bukan diduga:** fungsi `peta_parquet` di
`kehidupan_arsip.py` (blob `318a5cb1`, dibaca UTUH) **melewatkan baris
`parquet_karantina`**. Kedua belas parquet itu karena itu tidak pernah masuk penyebut
mana pun — benar secara kode, dan **tidak pernah disebut** di dokumen mana pun sebelum
jurnal 140. Kesunyian itulah isi KC-52.

**Yang DILARANG mulai sekarang:** memakai salah satu dari ketiga angka di atas **tanpa
menyebut penyebutnya**.

**Yang DICABUT:** sirat Koreksi 4 UKUR v10–v12 bahwa 839.842.134 "bermasalah" dan
839.325.999 "yang benar". Ketiganya benar. Yang keliru adalah menyamakan penyebutnya.

**Yang juga DICABUT:** pemisahan satuan pada STATE v53, yang memberi 839.325.999 dan
516.135 satuan "lilin menit" tetapi 839.842.134 satuan "baris parquet". **Ketiganya
bersatuan baris parquet.** Pemisahan satuan itu bukan kesalahan sepele: ia adalah salah
satu **penyangga** yang membuat kekeliruan bertahan, karena ia membuat ketidakcocokan
tampak wajar.

---

## Keputusan 2 — Koreksi 9 diakui sebagai KELAS CACAT TANPA PENANGKAL

Jurnal 138 §5 butir 2 menulis verbatim:

> *"Keduanya ditulis dari dua ekspresi berbeda yang kebetulan selalu bertemu — maka
> 839.325.999 adalah cacah baris parquet yang sebenarnya, dan **839.842.134 yang
> keliru**, bukan sebaliknya."*

**Premisnya benar. Kesimpulannya tidak sah.** Kalimat itu bertahan **dua giliran
penuh**, melewati pembacaan ulang aturan 52 atas berkas yang memuatnya, dan runtuh
bukan karena diperiksa melainkan karena **data baru kebetulan dibuka**.

**Keputusan:** ia dicatat sebagai butir ke-**10** daftar kesalahan dokumen, dan
satu-satunya yang **bukan salah ketik**. Kesembilan butir lain adalah cacat penyalinan;
yang ini cacat penalaran.

**Pengakuan yang wajib disertakan setiap kali daftar itu dikutip:** kesembilan butir
pertama dapat ditangkap oleh pembacaan ulang yang teliti. **Butir kesepuluh tidak.**
Pemeriksaan formal kami — invarian, kendali data, sidik kode, kendali nol, pembacaan
ulang utuh — **tidak punya satu pun penangkal** untuk kesimpulan tidak sah yang ditarik
dari premis benar. Pembacaan ulang aturan 52 terbukti **kuat terhadap pemotongan,
lemah terhadap ejaan, dan tidak berdaya terhadap penalaran cacat**: dari delapan kasus
terlacak, ia menangkap **satu**.

**DILARANG** menulis bahwa aturan 52 "menjaga mutu penalaran". Ia menjaga keutuhan
byte.

---

## Keputusan 3 — Aturan 86 DIRESMIKAN

**Bunyi resmi:**

> **Aturan 86.** Sebelum menulis modul baru untuk menjawab sebuah pertanyaan
> kuantitatif, isi direktori `reports/` **WAJIB** diperiksa lebih dulu untuk memastikan
> jawabannya belum tersimpan di sana. Bila sudah tersimpan, modul baru **DILARANG**
> ditulis; angkanya dibaca. Taksiran biaya "menulis modul" **WAJIB** disertai taksiran
> biaya "membaca laporan yang mungkin sudah ada", dan keduanya dibandingkan tertulis.

**Dua kejadian terukur yang menjadi dasarnya — keduanya kerugian kami sendiri:**

1. **Jurnal 138 bagian 4.** Biaya uji pemisah ditaksir **empat langkah** (tulis → dorong
   → tunggu CI → baca). Nyatanya **satu pembacaan**. Taksiran meleset empat kali ke
   arah yang membuat jalan murah tampak mahal.
2. **Jurnal 140 bagian 7.** Modul `selisih_lilin` ditulis lengkap dengan **36 butir
   uji** dan **satu workflow**, didorong sebagai push pemicu, untuk mencari angka yang
   **sudah tersimpan** sebagai medan `baris_karantina` di
   `reports/pulihkan_pecahan_<i>.json` sejak **29 Juli** — yaitu **dua hari sebelum
   pertanyaannya dirumuskan**.

**Alasan aturan ini boleh diresmikan sekarang padahal KC-48 melarang mengangkat aturan
dari satu kejadian:** kejadiannya **dua**, keduanya terukur, keduanya berarah sama, dan
keduanya merugikan. Itu ambang minimum yang sama yang dipakai untuk aturan 85.

**Yang DITOLAK diresmikan:** calon aturan "dua berkas akar yang didorong berturut tanpa
membaca laporan di antaranya pasti menghanguskan yang pertama". Kejadian terukurnya
masih **satu** (run 30547842823). Meresmikannya sekarang mengulang KC-48 persis pada
giliran yang meresmikan aturan 86 karena menghindari KC-48. Ia **tetap calon**.

**Penomoran:** aturan resmi kini **1–81, 83, 84, 85, 86**. Usulan yang masih
menggantung: **77**, **78**, **82**. Aturan berikutnya yang bebas: **87**.

---

## Keputusan 4 — R-312 resmi TIDAK TERADJUDIKASI, selamanya

**Poros:** selisih antara `cacah_lilin` dan `cacah_lilin_terbaca` atas 19.586 baris.
**Pita terkunci:** butir 1 **12 .. 120**; butir 2 **0,50 .. 0,865**; butir 3 MUDAH.
**Terukur:** `cacah_berselisih` = **0**. Penyebut butir 2 nol → **aturan 41**.

**Sebab runtuhnya, terukur dari kode dan bukan dari ingatan** (`kehidupan_arsip.py`,
fungsi `ukur_kolom`):

- `cacah_lilin` = `n` = cacah baris parquet, dari `pq.ParquetFile(...).metadata.num_rows`
- `cacah_lilin_terbaca` = baris yang **kedua** kolomnya terurai
- **identitas paksa:** `cacah_lilin` = `cacah_lilin_terbaca` + `cacah_baris_cacat`

Kedua medan **bukan dua pengukuran bebas**; mereka dua sisi satu identitas. Seluruh
poros R-312 berdiri di atas anggapan kebebasan itu, dan anggapan itu **tidak pernah
diperiksa terhadap satu baris kode pun** sebelum pitanya dikunci — meskipun aturan 85
baru saja diresmikan justru untuk memperketat penguncian pita.

**Yang hilang bersamanya:** satu modul, **36 butir uji**, satu workflow, dan satu push
pemicu. Ditulis seluruhnya di atas anggapan yang bisa dibantah oleh **satu pembacaan
berkas**.

**Lima larangan permanen R-312 — DIRESMIKAN:**

1. Pita 12..120 **DILARANG** disebut "tidak terbantah". Ia tidak diuji, bukan lolos.
2. **DILARANG** mengatakan kalibrasi membaik **atau** memburuk karena R-312.
3. **DILARANG** dihitung di pembilang maupun penyebut nisbah kemenangan mana pun.
4. **DILARANG** dihidupkan kembali dengan pita yang sama atau yang diubah.
5. Kesamaan angka **12** antara pita bawah R-312 dan cacah parquet karantina R-313
   **DILARANG** dibaca sebagai konfirmasi apa pun. Artinya berbeda; pertemuannya
   kebetulan.

**Catatan tentang aturan 85:** R-312 adalah pemakaian **pertama**-nya, dan pemakaian
itu **tidak menghasilkan adjudikasi**. Karena itu aturan 85 **sampai detik ini belum
terbukti bekerja maupun gagal**. Ia **DILARANG** disebut sebagai penangkal yang sudah
teruji.

**Pelajaran yang diangkat menjadi syarat praregistrasi** (berlaku mulai R-314):
**kebebasan setiap medan yang dipakai dalam sebuah poros WAJIB diperiksa terhadap kode
sumbernya lebih dulu, tertulis, sebelum pita dikunci.**

---

## Keputusan 5 — R-313 resmi TEPAT (2/2), dengan cacat prosedural yang diakui

**Butir 1.** Σ `baris_karantina` atas delapan `reports/pulihkan_pecahan_<i>.json` =
**516.135**, titik tunggal, selisih nol → terukur **516.135** → **MENANG**.
**Butir 2.** Σ parquet karantina = **12**, titik tunggal → terukur **12** → **MENANG**.

**Mutu bukti:** kedelapan laporan `pulih_sah` **true**; `cacah_sha_tak_cocok`,
`cacah_bagian_hilang`, `cacah_anggota_kurang`, `cacah_anggota_tak_aman`,
`selisih_baris_total` seluruhnya **0**; sidik kode seragam
`76c27e3c…3d25205d4469bd4d186a95fa62d700`; sidik kode manifes seragam
`237ccf42…6552daee5d3053093bfba601` → penjumlahan lintas pecahan sah (aturan 22).
**KC-47 diperiksa dan TIDAK terpicu:** 12 parquet tersebar di **enam** pecahan
(3/3/1/1/3/1).

**Cacat prosedural — PELANGGARAN ATURAN 79, DIAKUI DAN TIDAK DIPUTIHKAN.**
Praregistrasi R-313 ditulis **di chat**, bukan di `journal/**`. Bunyinya dikutip kata
demi kata di jurnal 140 §2, tetapi satu-satunya saksi bahwa ia ditulis **sebelum**
pengukuran adalah riwayat percakapan — **bukan git**.

**Keputusan:** kemenangan ini **tetap dicatat** di papan skor, **dan** cacatnya melekat
padanya secara permanen. **Bila kelak seseorang menolak mengakui R-313, penolakan itu
sah.** Kalimat ini wajib ikut setiap kali R-313 dikutip sebagai kemenangan.

**DILARANG** membaca R-313 sebagai bukti kalibrasi membaik. Ia **menjumlahkan angka
yang sudah tercatat di repo**, bukan menaksir sebaran yang belum diukur. Nilai
ilmiahnya terletak pada identitas yang ditutupnya, **bukan** pada ketepatan ramalannya.

---

## Keputusan 6 — H-A022 resmi TERBUKTI, dengan batas tafsir yang tegas

**Bunyi resmi yang terbukti:**

> Selisih **516.135** antara Σ baris parquet lolos gerbang dan Σ seluruh baris parquet
> rilis adalah tepat jumlah baris pada parquet **karantina** yang berada di luar
> penyebut 19.586.

**Batas tafsir — MENGIKAT:**

- Yang terbukti adalah **identitas himpunan**. Bukan sebab mengapa kedua belas
  simbol-bulan itu dikarantina.
- **Identitas kedua belas simbol-bulan itu belum didaftar.** Nama simbol dan bulannya
  **tidak diketahui**.
- **DILARANG** menulis kalimat apa pun tentang **jenis** instrumen yang dikarantina.
- Dugaan lama **516.135 / 12 = 43.011 ≈ sebulan penuh**: pembagiannya sah secara
  aritmetis, tetapi sebarannya **sangat tidak rata** (42.585 sampai 131.760 baris per
  tar). Rata-rata 43.011 adalah **turunan yang boleh dikutip, bukan bukti**, dan tafsir
  "tiap karantina kira-kira sebulan penuh" **TIDAK ditegakkan**.

**Turunan cuma-cuma yang ikut resmi:** `selisih_lilin` mengukur `cacah_berselisih` = 0
pada 19.586 dari 19.586; digabung dengan identitas `ukur_kolom`, itu memaksa
**`cacah_baris_cacat` = 0 di seluruh semesta** — tidak satu pun dari 839.325.999 baris
gagal diurai. Didapat **tanpa run tambahan**.

**Aturan 36 — kasus terkuat sampai kini, diresmikan sebagai catatan:** `selisih_lilin`
menjumlahkan medan `cacah_lilin` atas 19.586 baris laporan kehidupan; `pulihkan`
mencacah kaki parquet lewat jalur unduh–bongkar–verifikasi yang sama sekali berbeda,
pada run berbeda, tiga hari lebih awal. Keduanya **839.325.999**, sampai satuan
terakhir.

---

## Keputusan 7 — Aturan 79 DIRUMUSKAN ULANG, bukan dilemahkan

EKOR v13 mencatat aturan 79 sebagai "dilemahkan" karena R-313 melanggarnya dan toh
dicatat menang. **Rumusan itu ditolak.** Aturan yang dilanggar lalu disebut "lemah"
adalah aturan yang sedang dihapus diam-diam.

**Bunyi yang berlaku:**

> **Aturan 79 tetap penuh.** Praregistrasi yang tidak ditulis di `journal/**` sebelum
> pengukuran **tidak sah sebagai praregistrasi**. Bila ia terlanjur diadjudikasi,
> hasilnya **tetap dicatat** demi kejujuran riwayat, tetapi **cacatnya melekat
> permanen**, dan **penolakan pihak ketiga atas hasil itu sah**. Aturan 79 **tidak
> boleh** disebut lemah, longgar, atau opsional.

Dengan kata lain: yang lemah bukan aturannya, melainkan **kepatuhan kami** pada satu
kejadian tertentu. Perbedaan itu penting dan wajib dipertahankan dalam bahasa.

---

## Keputusan 8 — Utang cacah tangan aturan 66 TIDAK ditutup

Calon isi (f) di EKOR v13 adalah "cacah tangan pada ref sesudah trio". **DITOLAK untuk
giliran ini.**

**Yang sah dan boleh dikutip terukur:** **49 / 53 / 44 / 18** — dicacah TANGAN satu per
satu bernomor pada ref `3196fd98`, dikonfirmasi ulang pada ref `8a614567`.

**Yang DILARANG dikutip terukur:** **50 / 54 / 45**. Angka itu **turunan** dari
penambahan trio `selisih_lilin`, bukan hasil pencacahan. Menuliskannya di ADR ini
sebagai "cacah baru" berarti mengarang pengukuran di dalam dokumen yang justru meresmikan
larangan mengarang. Utang tetap **HIDUP** sampai direktori dilisting dan dicacah
bernomor.

Hal yang sama berlaku untuk **`ukur_baris` V6**: `BERKAS_DIUKUR` masih **21 nama**
sementara repo punya sekitar 50 modul dan 54 uji, dan pagar 800 baris belum diuji atas
kira-kira 29 modul yang lebih baru. Utang **HIDUP**.

---

## Keputusan 9 — Urutan poros resmi sesudah ADR ini

1. **Lubang tengah gugus `2022-05` dan `2024-05`** — poros tunggal berprioritas
   tertinggi; menguji **H-A020 dan H-A021 sekaligus**: apakah baris berdefisit yang
   berhimpit bulan itu berbagi satu jendela lilin yang sama.
2. **Identitas dua belas simbol-bulan karantina** — kandidat **termurah**; manifesnya
   sudah ada di repo (`reports/manifes_pecahan_<i>.json`). **Aturan 86 berlaku penuh di
   sini**: laporan dibaca lebih dulu, modul baru hanya bila terbukti perlu.
3. **Irisan 880 lawan 877 lubang funding** — dua penyebut mirip yang belum pernah
   dijajarkan; kandidat KC-52 berikutnya.
4. Sebab kekosongan TLMUSDT `2023-03`.
5. "Bulan pertama di penyebut" lawan "bulan pertama di bursa" (ADR-A016 kep. 6).
6. Tebing `2025-07` dan BTCSTUSDT.

**Syarat praregistrasi R-314 — kumulatif, seluruhnya WAJIB:** aturan 79 (di
`journal/**`, giliran berbeda dari adjudikasi) · aturan 83 (lantai aritmetis dihitung
tertulis) · aturan 84 (satu klausa per butir) · **aturan 85** (tepi "terpusat" di lantai
aritmetis atau paling banyak satu orde di atasnya, **dengan alasan tertulis**) ·
**aturan 86** (`reports/` diperiksa lebih dulu) · **pemeriksaan kebebasan medan terhadap
kode** (keputusan 4) · aturan 66 (nama modul dicek lewat pencacahan direktori TANGAN).

---

## Keputusan 10 — Utang aturan 52 atas trio `c1dc0009` berstatus UTAMA

`lux_ai/serapan/selisih_lilin.py`, `tests/test_selisih_lilin.py`, dan
`.github/workflows/selisih_lilin.yml` **belum dibaca ulang utuh sesudah push**.

**Ditegaskan:** CI hijau dengan 1377 uji terkumpul **BUKAN pengganti** pembacaan ulang.
CI membuktikan berkas dapat diimpor dan uji dapat dikumpulkan; ia **tidak** membuktikan
berkas tidak terpotong di bagian yang tidak diimpor. `push_files` **menulis ulang
seluruh berkas**, sehingga pemotongan senyap adalah risiko nyata, dan itulah sebabnya
aturan 52 ada.

Utang ini menempati **peringkat pertama** dalam daftar utang ukur.

---

## Konsekuensi penomoran

- KC resmi sampai **KC-52** (KC-16 kosong selamanya) · berikutnya **KC-53**
- Aturan resmi **1–81, 83, 84, 85, 86** · usulan tersisa **77**, **78**, **82** ·
  berikutnya **87**
- Hipotesis: **H-A022 TERBUKTI** · berikutnya **H-A023**
- Ramalan: R-312 **TIDAK TERADJUDIKASI**, R-313 **TEPAT** · berikutnya **R-314**
- Papan skor **313** (TEPAT 218 · MELESET 57 · SEPARUH 22 · TIDAK TERADJUDIKASI 9 ·
  MENUNGGU 7)
- Jurnal berikutnya **141** · `STATE.md` **v55** · EKOR **v14** · UKUR **v14** ·
  PROMPT **v55** · ADR berikutnya **A020**

## Jejak CI pada giliran ini

Aturan 38 pemakaian ke-**48**: `reports/ci_terakhir.json` blob
**`8ec97de5af8b528276174f635e3bda9e6cc2d7ef`**, run **30577779309**, commit
**`2bdd82336dd8424fbc45a0a80e267cd7f76ac20b`** (push UKUR v13),
**2026-07-30T20:07:50Z**, `kode_keluar` **0**, `cacah_uji` **1377 tests collected in
0.62s**. Ramalan "CI tetap 1377" **TERUKUR dan TEPAT**; tetap **MUDAH**, tetap tidak
diskor, tetap tidak menambah beruntun aturan 57 (yang tetap **4/4**).

Berkas ini berada di `decisions/**`, yang termasuk `paths-ignore` pada `ci.yml`
(blob `c79497b2`). Push ini karena itu **TIDAK menyalakan CI** dan **tidak menghanguskan**
laporan mana pun.
