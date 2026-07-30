# STATE — versi 52 (bagian 1 dari tiga)

Diperbarui: 2026-07-30 (sesi 61, giliran lanjutan). Aturan hanya BERTAMBAH; jangan
menulis ulang dari ingatan. v52 disusun di atas `STATE.md` v51 (blob
**`412a5b2dc9a05613b5e71f5a987c59687f3382d6`**), yang **DIBACA UTUH pada giliran ini
sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43). Dibaca UTUH pada giliran yang
sama pula: `STATE_LAMPIRAN_UKUR.md` v10 (`162c1305`) dan v11
(`7f0221bfb548d04f464a5b8c67f0579214f97b54`), serta `decisions/ADR-A018.md`
(`3fba599e6498b921e2a5babb915e247a3b1ecac4`).

## KESERASIAN VERSI — KETIGA BAGIAN KINI SERASI

Ketimpangan versi yang diperingatkan v51 **SUDAH DITUTUP**. Keadaan yang benar pada
saat berkas ini ditulis:

1. `STATE.md` **v52** — berkas ini. Aturan 1–81, 83, 84, **85**; KC-1..**KC-51**.
2. `STATE_LAMPIRAN_EKOR.md` **v11** — blob
   **`3d72a9e7aeb5123401065b225168c485d3e37963`** (commit `175c0387`). Memuat papan
   skor 311, R-311 SEPARUH, jumlah uji 1341, ADR sampai A017, rekonsiliasi ordinal
   aturan 38.
3. `STATE_LAMPIRAN_UKUR.md` **v11** — blob
   **`7f0221bfb548d04f464a5b8c67f0579214f97b54`** (commit `f9c5d960`). Memuat API
   `sisa_defisit` V1, 114 baris berdefisit, H-A021, cacah tangan 49/53/44/18.
4. `STATE_LAMPIRAN_ADR.md` (`a02ef271`) dan **`PROMPT_KELANJUTAN.md`** (`35beed44`) —
   **arsip; BUKAN sumber** (ADR-A018 kep. 9).

Perintah v51 bahwa "sumber sah R-311/KC-51/H-A021 adalah jurnal 135" **GUGUR dengan
sendirinya**: ketiga bagian STATE kini memuatnya, dan ADR-A018 meresmikannya. Jurnal
135 tetap sah sebagai jejak, bukan lagi sebagai satu-satunya sumber.

**Satu berkas per push tetap MENGIKAT** (KC-42, KC-43).

## STATE DIPECAH TIGA — BACA INI LEBIH DULU

1. **`STATE.md`** (berkas ini) — **bagian 1**: kepala, aturan bernomor 1–**85** (plus
   usulan 77, 78, 82), kelas cacat KC-1..**KC-51**.
2. **`STATE_LAMPIRAN_EKOR.md`** v11 — **bagian 2**: papan skor per ramalan, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** v11 — **bagian 3**: penyebut 787, taksonomi,
   karantina, bulan ABSEN, hipotesis H-A001..**H-A021**, lubang funding, byte parquet
   semesta, modul/workflow/uji, API terverifikasi.

**Ketiga berkas wajib dibaca bersama.** LANGKAH 0 PROMPT wajib menyebut ketiganya.

Yang lahir sejak v51: **ADR-A018 DITERIMA**; **KC-51 RESMI**; **aturan 85 RESMI**;
ordinal aturan 38 **DIREKONSILIASI** menjadi ke-**40** dengan cacatnya disebut;
koreksi resmi atas klaim v51 bahwa ramalan "CI tetap" tak pernah terukur;
`PROMPT_KELANJUTAN.md` **dinyatakan ARSIP**; larangan mencampur dua cacah `tests/`;
tiga berkas akar terakhir **DIBACA UTUH**; utang baca `test_bentangan_kohort.py` V2
**LUNAS**.

## CACAH TANGAN DIREKTORI — tetap sah pada ref `3196fd98`

| direktori | cacah TERUKUR (tangan, bernomor) |
| --- | --- |
| `lux_ai/serapan/` (berkas `.py`, termasuk `__init__.py`) | **49** |
| `tests/` | **53** |
| `.github/workflows/` | **44** |
| akar repo | **18** entri (**6** direktori + **12** berkas) |

Enam direktori akar: `.github`, `decisions`, `journal`, `lux_ai`, `reports`, `tests`.
Dua belas berkas akar: `PETA_MODUL.md`, `PETA_MODUL_BERKAS.md`, `PROMPT.md`,
`PROMPT_KELANJUTAN.md`, `README.md`, `STATE.md`, `STATE_LAMPIRAN.md`,
`STATE_LAMPIRAN_ADR.md`, `STATE_LAMPIRAN_ANGKA.md`, `STATE_LAMPIRAN_EKOR.md`,
`STATE_LAMPIRAN_UKUR.md`, `requirements.txt`.

Angka 48/52/43 pada ref `5d7d8b96` dan 47/51/42 pada ref `07a69d39` tetap sah untuk
ref masing-masing. **Sesudah trio berikutnya, 50/54/45 menjadi TURUNAN dan DILARANG
dikutip sebagai terukur.**

**[v52] LARANGAN BARU (ADR-A018 kep. 10) — DUA CACAH `tests/` DILARANG DICAMPUR.**
`PETA_MODUL_BERKAS.md` (blob `3abe95f6`) mencatat **34** berkas uji milik repo
**WARISAN `bot_v8`**; repo riset ini punya **53**. Keduanya benar untuk repo
masing-masing. **Menyebut "cacah uji" tanpa menyebut repo-nya DILARANG**, karena
selisih 34 lawan 53 akan tampak seperti pelanggaran aturan 66 padahal bukan.

## PERINGATAN DINI ATURAN 48 — besar modul

Dari daftar direktori pada ref `3196fd98` (byte, bukan baris): `silang_funding.py`
**29.873** · `funding.py` **28.121** · **`sisa_defisit.py` 25.949** ·
`semesta_kuota.py` 24.987 · `lubang_tengah.py` 23.745. **Bila `sisa_defisit` V2
diperlukan, pecah lebih dulu.**

## SALAH KETIK DOKUMEN SENDIRI — daftar yang diakui dan belum diperbaiki di sumbernya

Empat salah ketik kami sendiri kini diakui terbuka. Tidak satu pun berkas didorong
ulang hanya untuk itu, dengan sebab tertulis yang sama setiap kali: `push_files`
menulis ulang SELURUH berkas, sehingga memperbaiki satu karakter berarti menyusun
ulang berkas besar dari konteks yang sudah terpakai — persis yang dicatat KC-42
sebagai cara paling pasti merusak berkas.

| # | berkas | tertulis | seharusnya | status |
| --- | --- | --- | --- | --- |
| 1 | jurnal 132 §3 | "beruntun 2/1" | 2/2 | dikoreksi di STATE v50 |
| 2 | EKOR v10 | `terisi ≉49,7%` | `≈49,7%` | dikoreksi di EKOR v11 |
| 3 | jurnal 135 §13.3 | "hendan dirumuskan" | "hendak" | dikoreksi di STATE v51 |
| 4 | EKOR v11 kepala | "ramalan deretministik" | "deterministik" | **utang EKOR v12** |
| 5 | UKUR v11 kepala | "KESERAIAN VERSI" | "KESERASIAN VERSI" | **utang UKUR v12** |
| 6 | UKUR v11 daftar uji | penanda `**` tak berpasangan pada baris `test_bentangan_kohort.py` | penanda berpasangan | **utang UKUR v12** |

**Bila berkas sumber dan koreksi ini bertentangan pada titik-titik itu, koreksi ini
menang** — pengecualian tersurat atas KC-41 yang HANYA berlaku untuk salah ketik yang
sudah diakui, tidak pernah untuk angka terukur.

**Pembacaan yang jujur atas pola ini:** tiga berkas berturut (EKOR v11, UKUR v11, dan
UKUR v11 lagi) memuat salah ketik yang lolos, padahal masing-masing dibaca ulang UTUH
sesudah push. Itu **tanda ketelitian menurun pada giliran panjang**, bukan kebetulan,
dan wajib dibaca sebagai peringatan operasional — bukan sebagai kelas cacat ilmiah.

## KOREKSI BESAR yang MASIH HIDUP — dua angka yang selama ini disamakan

- **TERUKUR:** `jumlah_lilin_langsung` = **839.325.999** lilin menit, dijumlahkan
  LANGSUNG dari medan `cacah_lilin` atas 19.586 baris.
- **TERCATAT BERULANG:** total baris parquet semesta = **839.842.134** baris parquet,
  dari run rilis 30404071324.
- **SELISIH = 516.135.** Kedua besaran BUKAN besaran yang sama.

Aritmetika implikasi jurnal 131 §6 karena itu **SALAH sebagai turunan**, meski R-310
sendiri tetap sah (pita dikunci lebih dulu, aturan 29). **Dugaan yang BELUM DIUJI dan
DILARANG dikutip sebagai penjelasan:** 19.598 − 19.586 = 12 simbol-bulan karantina,
516.135 / 12 = 43.011 ≈ sebulan penuh. **[v52] Kini resmi menjadi poros calon (b)
R-312 dengan syarat bentuk SEBARAN, bukan rata-rata** (ADR-A018 kep. 12).

## Aturan bernomor

Aturan **1–36** berlaku tanpa perubahan; teks di STATE v19 (blob `e06c486e…`),
ringkas di v37 (blob `f520d5e2`).

**Aturan 10 (irisan/urutan bulan BUKAN sebab). [v52] Ditaati.** Seluruh pernyataan
R-311 tetap pernyataan SEBARAN. Tidak ada kalimat sebab yang ditegakkan untuk TLMUSDT
2023-03 maupun gugus `2022-05`.

**Aturan 21 (total papan skor dihitung tangan). [v52] Ditaati, tanpa perubahan:**
217 + 57 = 274; 274 + 22 = 296; 296 + 8 = 304; 304 + 7 = **311**. Rincian: TEPAT
**217** · MELESET **57** · SEPARUH **22** · TIDAK TERADJUDIKASI **8** · MENUNGGU **7**.
N_percobaan = 0. **ADJUDIKASI RISET TETAP TERKUNCI.** MENUNGGU: R-7, R-19, R-20,
R-28, R-36, R-37, R-199. **Tidak ada ramalan baru yang diadjudikasi sejak v51**, jadi
lajur tidak bergerak; ia DIBACA dari v51, tidak dikarang.

**Aturan 29 (pita praregistrasi TIDAK boleh diubah sesudah pengukuran). [v52]
Dipertegas oleh ADR-A018:** aturan 85 yang baru **TIDAK berlaku surut**, dan **R-311
TIDAK diadjudikasi ulang** meskipun kekalahannya melahirkan aturan itu. Memperbaiki
cara meramal ke depan tidak boleh dipakai untuk memperbaiki nilai ke belakang.

**Aturan 36 (dua modul berbeda atas semesta sama wajib cocok). [v52]** Tidak ada run
baru; kecocokan lima run berturut tetap tercatat di UKUR v11.

Aturan **37, 39–45, 47, 49, 51, 53, 54, 56, 59–62** berlaku tanpa perubahan; ringkas
satu baris: 37 kelas cacat pada sampel · 39 keseragaman sampel bukan ramalan · 40 uji
silang baris · 41 penyebut nol → TIDAK TERADJUDIKASI · 42 kelas cacat butuh angka
terukur · 43 toleransi berskala · 44 ramalan menyebut penyebut · 45 keatomikan push
pemicu · 47 satuan cacah tersurat · 49 re-export mematahkan uji · 51 jendela mundur
adaptif · 53 ramalan kode keluar butuh pembacaan perilaku · 54 cacah `def test_` satu
per satu · 56 commit BERIKUTNYA yang menyentuh X · 59 ketiadaan gejala butuh penyebut
· 60 mekanisme tak dipindah antarkasus · 61 medan tak dipindah antarjalur · 62 daftar
tak diminta dari laporan bercacah.

Yang berikut memuat angka atau daftar kepatuhan:

38. Cacah uji hanya sah dari `reports/ci_terakhir.json` (run id + commit +
    `kode_keluar`). **[v52] Ditaati, dan ORDINALNYA KINI DIREKONSILIASI.**
    **1341** butir, blob **`bce1177ea21d7a4e01b59b2d4f4277a8584b4eed`**, run
    **30545364506**, commit **`8c30de51cc4d0098d4bd2922966684591bd7ce96`**,
    2026-07-30T13:05:55Z, kode 0 (`1341 tests collected in 0.45s`).
    Blob kedua berangka sama: **`2d32f814e5e426e1411559810b55b9f20176a22d`**, run
    **30542217837**, commit `b1c7941d`, 12:22:10Z, 0.62s.
    **Definisi ordinal yang BERLAKU (ADR-A018 kep. 8):** pemakaian aturan 38 dihitung
    **hanya** untuk pembacaan `ci_terakhir.json` yang meninggalkan **jejak tertulis**
    berupa nomor run, commit, dan blob di STATE, lampiran, atau jurnal. Dengan definisi
    itu, pemakaian berjalan adalah yang **ke-40**. Larangan v51 untuk menulis nomor
    pasti **DICABUT** karena definisinya kini tersurat.
    **Cacatnya disebut, bukan disembunyikan:** baris ke-38 (run `30541051907`, CI 1297,
    commit `5d7d8b96`) **tidak memuat blob** — diwarisi dari jurnal 135, blobnya sudah
    tertimpa dan tidak dapat dipulihkan. Ordinal 40 karena itu sah **relatif terhadap
    definisi di atas**, bukan sebagai pencacahan mutlak. **Bila jejak pembacaan lain
    ditemukan di jurnal 133–134, nomor ini WAJIB dikoreksi.**
    **[v52] KOREKSI RESMI atas v51 (ADR-A018 kep. 7).** v51 menulis bahwa ramalan
    "CI tetap" pada push dokumen **tidak pernah terukur**. **Itu terbantah** oleh
    pembacaan langsung run 30545364506 atas commit `8c30de51`, yaitu push STATE v51
    itu sendiri. Rumusan yang benar dan mengikat: ramalan semacam itu **terukur bila
    laporannya dibaca sebelum run berikutnya menimpanya**, dan tetap berlabel **MUDAH**,
    tetap **tidak diskor**, tetap **tidak menambah beruntun aturan 57**, karena tidak
    menyentuh `tests/**`. Yang terukur mengalahkan yang disimpulkan (KC-41).
45. Keatomikan push pemicu. **[v52]** Tidak ada push pemicu giliran ini; ketiga push
    terakhir adalah dokumen tunggal (ADR-A018, UKUR v11, berkas ini).
46. Kode dilarang menyimpulkan dari penyebut nol. **[v52]** Tidak ada kode baru.
47. Satuan cacah tersurat. **[v52] Ditaati:** "114", "17.398", "17.284", "18.799",
    "1.401", "9", "1.392", "53", "49", "44", "34" bersatuan **baris atau berkas**, dan
    **34 lawan 53 milik REPO BERBEDA**; "712.925", "291.379", "42.510", "808.162",
    "95.237", "18.143.601", "839.325.999", "516.135" bersatuan **lilin menit**;
    "839.842.134" bersatuan **baris parquet**; "0,4087" adalah **bagian tanpa satuan**;
    "25.949", "29.873", "28.121" bersatuan **byte berkas sumber**; "1341" bersatuan
    **butir uji terkumpul pytest**.
48. Berkas modul mendekati 800 baris dipecah sebelum fungsi baru ditambahkan.
    **[v52] PERINGATAN DINI berlanjut** — lihat bagian tersendiri di atas.
50. Setiap pengukuran yang menyimpulkan dari KETIADAAN wajib memuat kendali positif.
    **[v52]** Tidak ada pengukuran baru; kepatuhan `sisa_defisit` V1 tercatat di v51
    dan UKUR v11.
52. Laporan yang tidak dapat dibaca utuh setara dengan laporan yang tidak ada.
    **[v52] DUA UTANG BESAR LUNAS.**
    **(a) `tests/test_bentangan_kohort.py` V2 DIBACA UTUH** — blob
    **`9f850ecdb25466d38c839004b36ff221db2cf7f8`** (13.154 B). Dicacah TANGAN bernomor:
    `test_01`..`test_63` berurut **tanpa lompatan = 63 butir**; helper `peta`,
    `baris_uji`, `laporan_bersih` tidak berawalan `test_` sehingga tidak dikumpulkan.
    **Sembilan versi menunggu → NOL.**
    **(b) TIGA BERKAS AKAR TERAKHIR DIBACA UTUH** — `PETA_MODUL.md` (`9ee33a99`),
    `PETA_MODUL_BERKAS.md` (`3abe95f6`), `PROMPT_KELANJUTAN.md` (`35beed44`). Daftar
    "berkas akar yang belum pernah diperiksa" kini **5 dari 5 LUNAS**.
    **Utang baca yang TETAP hidup:** `decisions/ADR-A002`, **A004**, **A006**, **A007**,
    **A008**; `karantina_semesta.yml` (`de40fa4e`); `tests/test_pulihkan.py`
    (`11c43533`); `test_rilis_karantina.py` (`739c8da9`); `test_karantina_a006.py`
    (`a5a3d82f`).
55. Rumusan pemicu workflow wajib dikutip dari berkas workflow beserta blobnya.
    **[v52]** Tidak ada workflow baru.
57. Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB ditulis bernomor.
    **[v52] BERUNTUN TETAP 3 DARI 3.** Tidak ada push yang menyentuh `tests/**` sejak
    v51, sehingga beruntun **tidak bertambah dan tidak putus**. Push dokumen —
    termasuk berkas ini — meramalkan CI tetap **1341**; ramalan itu **MUDAH**,
    deterministik, TIDAK diskor, dan TIDAK menambah beruntun.
58. Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH DILARANG
    diramalkan dengan pita sempit.
63–76. Berlaku tanpa perubahan dari v43. Teks penuh di v43 (blob `a91a4934`).

**Aturan 66 (cacah direktori dengan TANGAN, bernomor). [v52] Tidak ada utang hidup;**
cacah 49/53/44/18 pada ref `3196fd98` tetap yang terakhir sah. **Utang baru lahir
begitu trio berikutnya didorong.**

**Aturan 77 (TETAP DIUSULKAN):** dua berkas laporan berblob IDENTIK bukan dua
pengukuran. **[v52] Tidak mendapat kasus baru.**

**Aturan 78 (TETAP DIUSULKAN):** `BATAS_BARIS_LAPORAN` sebagai syarat keterbacaan.
**[v52] Tidak mendapat kasus baru.** Belum diresmikan karena ini kasus rancangan,
bukan pengukuran batasnya sendiri.

**Aturan 79 (BERLAKU sejak v44). [v52] Ditegaskan kembali oleh ADR-A018 kep. 12:**
praregistrasi R-312 **DILARANG ditulis di ADR maupun di lampiran**; ia wajib ditulis
di `journal/**` lebih dulu, pada giliran yang berbeda dari adjudikasi.

**Aturan 80 (BERLAKU sejak v46). [v52]** Tidak ada uji arah waktu.

**Aturan 81 (BERLAKU sejak v46). [v52] Hasil pemeriksaan R-311 DIRESMIKAN
(ADR-A018 kep. 4): TIDAK terpicu.** Sepuluh baris berdefisit teratas tersebar di
**tujuh bulan berbeda**; kelompok terbesar dalam satu bulan hanya **dua** baris.
Karena itu **114 sah diperlakukan sebagai cacah baris**, bukan sebagai satu peristiwa
yang menyamar. **Untuk R-310 aturan 81 TETAP terpicu** (tujuh dari sembilan berhimpit
di `2024-05` dalam jendela sembilan lilin) dan tetap mengikat setiap kutipan angka 9.

**Aturan 82 (TETAP DIUSULKAN, nomor dicadangkan).** **[v52] Tidak mendapat kasus baru.**

**Aturan 83 (BERLAKU sejak v49). [v52] Batasnya kini tersurat.** Aturan 83 menuntut
aritmetika implikasi **dihitung**; ia tidak pernah menuntut hasilnya **dipakai**. Di
R-311 ia ditaati penuh — lantai **16** dihitung sendiri di jurnal 134 dan rentang
implikasi (16 .. 18.790) benar — dan pitanya tetap kalah karena tepi bawah diletakkan
di **200** tanpa satu kalimat pun yang membenarkannya. Lubang itu ditutup aturan 85.

**Aturan 84 (RESMI sejak v50). [v52]** Berlaku tanpa perubahan: satu klausa per butir
berisiko.

**ATURAN 85 — RESMI DI SINI (peresmian oleh ADR-A018 kep. 2), BERLAKU MULAI R-312.**

> Untuk tiap butir berisiko yang membatasi sebuah **cacah** atau **bagian**, dan yang
> sebarannya belum pernah diukur, aritmetika implikasi aturan 83 wajib dilanjutkan
> satu langkah: sesudah lantai dan langit-langit aritmetis dihitung, **tepi pita di
> sisi "terpusat" diletakkan pada lantai itu atau paling banyak satu orde besaran di
> atasnya**, dan alasan penempatannya ditulis sebagai kalimat tersendiri di
> praregistrasi. Kelipatan intuitif seperti 100, 200, atau 1.000 di atas lantai
> DILARANG dipakai tanpa alasan tertulis.

**Batas berlakunya:** mulai **R-312**, **TIDAK berlaku surut**, dan **R-311 TIDAK
diadjudikasi ulang** (aturan 29). Kerabat: aturan 83 (yang ia lanjutkan), KC-48,
KC-49, dan KC-51 (yang ia tangkal).

**Penomoran aturan [v52].** Aturan resmi kini: **1–81, 83, 84, dan 85**. Nomor **82**
tetap dicadangkan untuk usulan yang belum berlaku; **77** dan **78** tetap usulan.
**Aturan berikutnya yang bebas: 86.**

## R-311 — ADJUDIKASI RESMI: SEPARUH (tidak berubah, dirumuskan ulang oleh ADR-A018)

| butir | berisiko | pita | terukur | hasil |
| --- | --- | --- | --- | --- |
| 1 — cacah baris berdefisit | ya | 200 .. 12.000 | **114** | **KALAH** |
| 2 — bagian sepuluh teratas | ya | 0,02 .. 0,45 | **0,4087** | **MENANG** |
| 3 — penggugur bersih + invarian nol | tidak (mudah) | — | bersih | menang, tidak diskor |

**Rumusan resmi temuan R-311 (ADR-A018 kep. 3) — satu-satunya yang boleh dikutip:**

> Dari **17.398** baris simbol-bulan yang bukan bulan pertama simbolnya dan bukan
> berstatus MATI, hanya **114** (**0,66%**) yang jumlah lilinnya kurang dari lilin
> penuh bulannya. Keseratus empat belas baris itu menanggung **712.925** lilin yang
> hilang, rata-rata **6.254** lilin per baris. **Sepuluh baris teratas menanggung
> 291.379 lilin, yaitu 0,4087 — dua per lima dari seluruhnya.** Baris terbesar adalah
> **TLMUSDT 2023-03**, berstatus HIDUP, dengan **2.130 dari 44.640** lilin, yakni
> **95,2% kosong**.

**Larangan yang menyertainya, seluruhnya tetap berlaku:**

1. **Penutupan 712.925 DILARANG disebut pengukuran bebas** — tautologi dari
   808.162 − 95.237 (KC-50, KC-37).
2. **Kenyataan bahwa 114 baris seluruhnya HIDUP (111) atau SEPI (3) dan NOL MATI
   DILARANG disebut temuan** — dipaksa definisi penyebut kerja.
3. **Tidak satu kalimat pun boleh menyimpulkan apa pun tentang harga** — keempat belas
   medan `medan_baris_terlihat` tidak memuat harga (ADR-A017 kep. 2).
4. **Butir 2 menang TIPIS ke tepi ATAS** (sisa 0,0413). Dua ramalan berturut yang
   menang menempel tepi BERLAWANAN **DILARANG** dibaca sebagai pita yang dirancang baik.

**[v52] Akibat atas H-A019 diresmikan (ADR-A018 kep. 6):** sifat TLMUSDT 2023-03 kini
terukur, sehingga tafsir "byte parquet kecil = bulan sebagian di tepi rentang"
**MELEMAH** — ada jalan ketiga, yaitu bulan penuh kalender yang datanya nyaris tidak
ada. **Tafsir penggantinya TIDAK ditegakkan** karena sebabnya belum diukur. H-A019
tetap **DITERIMA TERBATAS**; ADR-A015 kep. 5 **TIDAK dibalik**.

## Kelas cacat

KC-1 s.d. KC-12 seperti v19; KC-10 dan KC-11 DITUTUP. KC-13 keterwakilan sampel.
**KC-16 DITARIK — nomornya TETAP kosong selamanya.** KC-17 DITUTUP. Teks penuh
KC-14, KC-15, KC-19..KC-29 di v37 (`f520d5e2`). KC-30..KC-42 di v43 (`a91a4934`).
KC-43, KC-44 di v44 (`ede3ce3b`). KC-45, KC-46 di v45 (`e07f2de1`). KC-47 di v46
(`41b5b585`). KC-48 di v47 (`7642b75d`). KC-49 di v48 (`2fd136e4`). KC-50 di v50
(`095a4b2c`). **KC-51 teks penuh di bawah.**

Ringkas KC-19..KC-50 satu baris: KC-19 mencacah dari ingatan · KC-20 bias ke bawah ·
KC-21 ketiadaan gejala dari ketiadaan pengukuran · KC-22 mekanisme dipindah · KC-23
medan dipindah · KC-24 daftar dari laporan bercacah · KC-25 batas semesta tak tersurat
· KC-26 medan ekstrem membisu tentang seri · KC-27 karakterisasi dari contoh berurut ·
KC-28 mencampur kelas instrumen · KC-29 taksonomi paralel · KC-30 nama kelas dibaca
sebagai keadaan · KC-31 nama peristiwa dibaca sebagai mekanisme · KC-32 dua sistem
penomoran dicampur · KC-33 mengenali satu peristiwa lalu berhenti · KC-34 cacah
subkelompok dari pengurangan kepala · KC-35 cakupan kode dicampur dengan cakupan
laporan · KC-36 homonim diperlakukan satu konsep · KC-37 nol dari satu penyebut
sebagai bukti di penyebut lain · KC-38 kecocokan tanpa membedakan mekanisme · KC-39
dua penyebut bulan absen dicampur · KC-40 daftar klausa gagal dibaca sebagai keadaan ·
KC-41 pemicu/label/nomor dari ingatan · KC-42 menulis ulang berkas melampaui batas push
· KC-43 tanda tangan fungsi dari ingatan · KC-44 semua laporan di-commit satu langkah ·
KC-45 satuan "bulan tanpa funding" dan "bulan MATI" dicampur · KC-46 lubang bentuk AWAL
dibaca sebagai "funding berhenti" · KC-47 satu peristiwa menyamar sebagai banyak
pengamatan bebas · KC-48 ambang absolut pada besaran yang sebarannya belum pernah
diukur · KC-49 pita dikunci tanpa menghitung implikasi aritmetis · KC-50 agregat
dihitung lewat jalan memutar sehingga selisihnya tak terlihat.

**KC-41 — tetap berlaku.** Bila dua bagian STATE bertentangan, berkas SUMBER menang,
bukan yang lebih baru — dengan pengecualian tersurat untuk keenam salah ketik yang
sudah diakui di tabel atas.

**KC-47 — [v52] tidak mendapat kasus baru;** kasus R-310 tetap berlaku penuh dan wajib
ikut setiap kali angka 9 dikutip. R-311 **tidak** menambah kasus (aturan 81 tidak
terpicu).

**KC-48, KC-49, KC-50** berlaku tanpa perubahan.

### KC-51 — RESMI DI SINI (peresmian oleh ADR-A018 kep. 1)

**Bias taksiran pemusatan. Rumusan resmi, satu-satunya yang boleh dikutip:**

> Ketika sebuah besaran belum pernah diukur sebarannya, taksiran yang saya buat secara
> sistematis mengandaikan besaran itu **lebih menyebar** daripada kenyataannya.
> Akibatnya tepi pita di sisi "terpusat" diletakkan terlalu jauh dari lantai
> aritmetis, dan pita kalah ke sisi itu.

**Empat kejadian berturut, tanpa satu pun pembalikan arah:**

| ramalan | besaran | taksiran / pita | terukur | arah |
| --- | --- | --- | --- | --- |
| R-308 butir 2 | cacah MATI ber-byte kecil | 10 .. 300 | **2** | lebih terpusat |
| R-310 butir 2 | bagian defisit bukan-pertama | 0,073 (0,02..0,25) | **0,0445** | lebih terpusat |
| R-311 butir 1 | cacah baris berdefisit | 3.000 (200..12.000) | **114** | lebih terpusat |
| R-311 butir 2 | pemusatan sepuluh teratas | 0,15 (0,02..0,45) | **0,4087** | lebih terpusat |

R-311 butir 1 meleset **26,3 kali** dari taksiran titik dan **1,75 kali** di bawah tepi
bawah. R-311 butir 2 meleset **+172%**. **Kedua butir meleset ke arah fisik yang sama**
meskipun satu kalah dan satu menang; satu-satunya alasan butir 2 menang adalah pitanya
kebetulan cukup lebar.

**Mengapa ini kelas cacat dan bukan empat kesialan:** arahnya **tidak pernah berbalik**.
Kesialan acak akan berganti arah.

**Yang DILARANG oleh KC-51:** menyebut kemenangan R-311 butir 2 — atau kemenangan
tipis mana pun yang menempel tepi — sebagai bukti bahwa kalibrasi membaik.

**Penangkalnya adalah aturan 85**, yang berlaku mulai R-312. Kerabat: KC-20, KC-48,
KC-49; kerabat aturan 83.

**Kelas cacat berikutnya yang bebas: KC-52.**

## Hipotesis yang berstatus DIUSULKAN

**H-A020 (DIUSULKAN, BELUM DIUJI)** — ketujuh baris MATI tak penuh berbulan `2024-05`
adalah SATU peristiwa; jendelanya hanya sembilan lilin (39.308..39.317). **DILARANG**
menulis "tujuh simbol didelisting 28 Mei 2024" sebagai temuan.

**H-A021 (DIUSULKAN, BELUM DIUJI)** — kekosongan **ANCUSDT 2022-05** (defisit
**26.959**) dan **LUNAUSDT 2022-05** (defisit **26.950**) adalah SATU peristiwa yang
sama, bukan dua pengamatan bebas. Dasarnya HANYA selisih **sembilan lilin** pada bulan
yang sama — **kebetulan angka, bukan bukti**.

**Peringatan yang menempel pada keduanya:** bentuk buktinya IDENTIK, dan pengulangan
bentuk itu sendiri patut dicurigai — ia bisa menandakan mekanisme yang sama, atau
menandakan bahwa kita hanya pandai menemukan pola yang sudah kita cari. Uji yang
menegakkan atau meruntuhkan keduanya: **lubang tengah pada gugus `2022-05` dan
`2024-05`**.

**[v52] Akibat aritmetis bila H-A021 kelak DITERIMA** (ADR-A018 kep. 5): cacah
pengamatan bebas dalam sepuluh baris teratas turun dari 10 menjadi 9, dan
`bagian_teratas` **TIDAK berubah**, karena ia dihitung atas lilin, bukan atas baris.

**Yang DILARANG sampai diuji:** kalimat apa pun yang menyebut sebab, nama peristiwa
pasar, keruntuhan ekosistem, atau tanggal penghentian untuk gugus `2022-05` maupun
`2024-05`. Laporan kehidupan **tidak menyimpan harga**.

Hipotesis berikutnya **H-A022**.

## Berkas akar — status hidup/mati, kini LENGKAP 5 dari 5

- **`STATE_LAMPIRAN.md`** (`f2b90764`, 2.350 B) — **HIDUP sebagai arsip naratif**
  (L-1..L-5). Tidak memuat angka semesta.
- **`STATE_LAMPIRAN_ANGKA.md`** (`f3ebdb02`, 1.841 B) — **HIDUP tetapi hampir kosong.**
  `N_percobaan` = 0. Memuat angka struktural repo WARISAN dan daftar klaim TERLARANG
  (Signals 10.032 / +189,41R / PF 1,61 dan seluruh tabel tuning `AUDIT.md`, tercemar
  kebocoran seleksi). **Jangan dicampur dengan penyebut 19.586** (KC-36).
- **[v52] `PETA_MODUL.md`** (`9ee33a99`, 8.691 B) — **HIDUP, seluruhnya tentang repo
  WARISAN `bot_v8`.** Memetakan jalur `engine.run (605)` → `_scan_for_entries (1033)`
  → `_validate_and_enter (1537)` → `_try_enter_inner (1836)` → gerbang `rr1 < min_rr`
  (1997) → `_determine_exit (3004)`, dengan verifikasi A–P. Dua hal wajib ikut dikutip:
  **(i) `backtest.py` TIDAK memodelkan funding sama sekali** (docstring baris 29) dan
  slippage dilipat ke `fee_r` datar; **(ii) temuan F = kebocoran seleksi harfiah** —
  `AUDIT.md` v8.3 memilih default dari paruh UJI (`0.40/fw30 PF 1.632`).
  **Tiga butir bertanda "memerlukan verifikasi" DIDAFTARKAN SEBAGAI UTANG TERBUKA,
  bukan fakta** (ADR-A018 kep. 10): atribut `enable_hs` yang tidak ditemukan di
  `config.py` padahal dipakai `strategy.py`; klaim "30 pair dipilih alfabetis" tanpa
  bukti; klaim "kendala mengikat = kapasitas margin" yang belum diuji angkanya.
- **[v52] `PETA_MODUL_BERKAS.md`** (`3abe95f6`, 6.890 B) — **HIDUP sebagai inventaris
  208 berkas repo WARISAN.** Cacah tangan yang cocok: **33** `.py` akar, **17**
  ber-`__main__`, **34** berkas uji warisan. `engine.py` 184.993 B / 3.621 baris;
  `strategy.py` 70.020 B / 1.598; `config.py` 46.688 B / 798; `backtest.py` 45.159 B /
  1.008. **Sumber bahaya dua cacah `tests/` — lihat larangan di bagian cacah tangan.**
- **[v52] `PROMPT_KELANJUTAN.md`** (`35beed44`, 10.777 B) — **ARSIP, BUKAN SUMBER**
  (ADR-A018 kep. 9). Isinya **PROMPT v48**, tertinggal enam versi dari `PROMPT.md`
  v54, dan **setiap angka posisinya salah**: menyuruh membaca STATE v44 / EKOR v4 /
  UKUR v4, papan skor **305**, aturan sampai **79**, KC sampai **KC-44**, CI **984**,
  cacah direktori 42/37, dan mempraregistrasi **R-306** yang sudah lama diadjudikasi
  TEPAT. **DILARANG dipakai sebagai sumber posisi, aturan, atau praregistrasi oleh
  siapa pun, termasuk penerus giliran.**
  **Sebab keputusan ini keras:** namanya justru yang paling mengundang dibaca lebih
  dulu oleh penerus, dan satu perintahnya — *"Jangan berhenti dengan alasan konteks
  Notion"* — **bertabrakan langsung dengan perintah operator yang berlaku sekarang**,
  yang justru memerintahkan berhenti dan mengatakan berhenti bila konteks berat.
  **Perintah operator menang; berkas usang tidak boleh mengalahkan perintah yang
  berlaku.** Pekerjaan tersisa: memberinya kepala "ARSIP — BUKAN SUMBER" atau
  menghapusnya.
- `STATE_LAMPIRAN_ADR.md` (`a02ef271`) tetap **arsip, bukan sumber**.

## Larangan aktif — jangan dilanggar

- Besar berkas **DILARANG** jadi detektor status ke arah mana pun (ADR-A015 kep. 5,
  ditegaskan ADR-A017 kep. 8, **tidak dibalik oleh R-311**). Di zona 22.440–97.634 byte
  ada **38 HIDUP dan 0 MATI**, dan baris paling kosong di seluruh semesta (TLMUSDT
  2023-03, 95,2% kosong) berstatus **HIDUP**.
- Laporan kehidupan TIDAK menyimpan harga (**14** medan, tak satu pun harga) → "harga
  beku", "lilin datar", "jeda pemeliharaan bursa" **DILARANG** disimpulkan.
- **DILARANG** menulis "delisting 28 Mei 2024", dan kalimat sebab serupa untuk gugus
  `2022-05`.
- **712.925 DILARANG jadi penyebut pemeriksaan** (KC-50).
- Frasa "sembilan pemeriksaan bebas" **DILARANG**; numerator 9 R-310 bukan sembilan
  pengamatan bebas.
- Lajur papan skor **DILARANG dikarang** tanpa membaca STATE.
- Cacah direktori **turunan penambahan DILARANG** dikutip sebagai terukur.
- **[v52] Menyebut "cacah uji" tanpa menyebut repo-nya DILARANG** (34 warisan lawan
  53 riset).
- **[v52] `PROMPT_KELANJUTAN.md` DILARANG dipakai sebagai sumber.**
- **[v52] Kemenangan pita yang menempel tepi DILARANG dibaca sebagai kalibrasi
  membaik** (KC-51).

## Angka semesta yang mengikat (dibaca dari v51/UKUR v11, tidak dihitung ulang dari ingatan)

Penyebut **19.586** (LOLOS gerbang, bukan 19.598) · `cacah_simbol` **787** ·
bukan-pertama **18.799** · HIDUP **18.087** · SEPI **98** · MATI **1.401** (seluruhnya
bukan-pertama) · MATI penuh **1.392** · MATI tak penuh **9** · `cacah_lain` **0** ·
`defisit_total` **18.143.601** · `defisit_pertama` **17.335.439** (95,5%; rata 22.027;
keterisian ≈49,7%) · `defisit_bukan_pertama` **808.162** (0,0445) · `defisit_sembilan`
**95.237** (0,1178) · sisa **712.925** · calon **17.398** (HIDUP 17.318 + SEPI 80) ·
calon penuh **17.284** · calon berdefisit **114** (HIDUP 111 + SEPI 3; 0,66%) ·
`defisit_teratas` **291.379** · `bagian_teratas` **0,4087** · `defisit_terbesar`
**42.510** · rata **6.254** lilin per baris berdefisit · `jumlah_lilin_langsung`
**839.325.999** · total baris parquet **839.842.134** · **selisih 516.135** · total
byte parquet **32.706.262.375** · `byte_mati` **579.041.399** · `bagian_byte_mati`
**0,017704297493883234** · nisbah rata byte **0,527179** · `cacah_hidup_byte_kecil`
**38** · `cacah_mati_byte_kecil` **2** · bulan pertama HIDUP **769** · bulan pertama
SEPI **18** (769 + 18 = 787 ✅) · lubang funding **880** semesta / **877** dalam
penyebut / 3 tak dikenal · `cacah_simbol_ada_lubang` **122** (awal 5, bukan-awal 118) ·
jumlah uji **1341**.

## Ke bagian 2 dan 3

Berkas ini berhenti di sini dengan sengaja.

- **Papan skor per ramalan** → `STATE_LAMPIRAN_EKOR.md` **v11** (`3d72a9e7`), total
  **311**, jumlah uji **1341**, ADR sampai A017. **EKOR v12 wajib menambahkan ADR-A018
  dan memperbaiki salah ketik "deretministik".**
- **Penyebut 787, taksonomi, karantina, bulan ABSEN, hipotesis, byte parquet semesta,
  modul/workflow/uji, API terverifikasi** → `STATE_LAMPIRAN_UKUR.md` **v11**
  (`7f0221bf`). **UKUR v12 wajib memperbaiki dua salah ketik di kepalanya dan di daftar
  uji.**

## Penomoran berikutnya

Jurnal **136** · STATE **v53** · EKOR **v12** · UKUR **v12** · PROMPT **v55** · ADR
**A019** · KC **KC-52** · aturan **86** · hipotesis **H-A022** · ramalan **R-312** ·
papan skor sesudah R-312 = **312**.

**R-312 DILARANG disusun pada giliran adjudikasi** (ADR-A016) dan **DILARANG ditulis
di ADR atau lampiran** (aturan 79) — jurnal lebih dulu. Poros yang sudah DITETAPKAN
(ADR-A018 kep. 12), urut prioritas:

- **(a) Lubang tengah gugus `2022-05` dan `2024-05`** — menguji H-A021 dan H-A020
  sekaligus: apakah baris berdefisit yang berhimpit bulan itu berbagi satu jendela
  lilin yang sama.
- **(b) Selisih 516.135** lawan dugaan 12 simbol-bulan karantina (516.135 / 12 =
  43.011 — **DUGAAN, BELUM DIUJI**). Porosnya **wajib berupa bentuk SEBARAN, bukan
  rata-rata**, sebab rata-rata akan selalu benar secara aritmetis dan karena itu tidak
  berisiko.

Sebelum pita dikunci, seluruhnya WAJIB: aturan **79** (praregistrasi di `journal/**`),
aturan **83** (aritmetika implikasi lebih dulu), **aturan 85** (tepi "terpusat" di
lantai aritmetis atau paling banyak satu orde di atasnya, dengan alasan tertulis),
aturan **84** (klausa tunggal), **KC-50** (agregat lewat jalur LANGSUNG), aturan **66**
(cacah tangan sebelum menamai modul), dan `BATAS_BARIS_LAPORAN` ringkas.
