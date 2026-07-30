# STATE — versi 54 (bagian 1 dari tiga)

Diperbarui: 2026-07-31 (sesi 61, giliran lanjutan). Aturan hanya BERTAMBAH; jangan
menulis ulang dari ingatan. v54 disusun di atas `STATE.md` v53 (blob
**`a0ea143e1b34b7be512df75853a4a4f2ca79351c`**), yang **DIBACA UTUH pada giliran ini
sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43).

**Apa yang v54 kerjakan, tersurat:** ia memuat **penutupan KC-52**, temuan terbesar
sejak papan skor menembus 300 — dua angka besar yang selama berpuluh giliran
diperlakukan sebagai satu ternyata **keduanya benar**, dan selisihnya terukur persis.
Ia juga mengadjudikasi **R-312 (TIDAK TERADJUDIKASI)** dan **R-313 (TEPAT)**,
menaikkan papan skor ke **313**, memajukan ordinal aturan 38 ke **ke-45**, mencatat
tiga kesalahan dokumen baru sehingga daftarnya menjadi **sepuluh**, dan mengusulkan
**aturan 86**.

## KESERASIAN VERSI — TIDAK SERASI; v54 / v12 / v12

1. `STATE.md` **v54** — berkas ini. Aturan 1–81, 83, 84, 85; KC-1..**KC-52**.
2. `STATE_LAMPIRAN_EKOR.md` **v12** — blob
   **`568dc877f69d6508b1db50a35877d34da76fc21e`**. **TERTINGGAL DUA VERSI.** Ia masih
   memuat papan skor **311** dan ADR sampai A018.
3. `STATE_LAMPIRAN_UKUR.md` **v12** — blob
   **`b8dab926ac3bbf4441339f5856775ef521efdec1`**. **TERTINGGAL DUA VERSI.** Ia belum
   memuat API `selisih_lilin`, `pulihkan`, maupun H-A022.
4. `STATE_LAMPIRAN_ADR.md` (`a02ef271`) dan **`PROMPT_KELANJUTAN.md`** (`35beed44`) —
   **arsip; BUKAN sumber** (ADR-A018 kep. 9).

**PERINGATAN KESERASIAN, tersurat dan tidak dihaluskan:** untuk pertama kalinya sejak
v51, ketiga bagian **tidak serasi**. Bila EKOR v12 atau UKUR v12 bertentangan dengan
berkas ini pada papan skor, KC, atau angka karantina, **berkas ini yang menang** —
pengecualian tersurat atas KC-41 yang berlaku HANYA untuk butir-butir yang v54 nyatakan
baru. Untuk segala hal lain, KC-41 tetap penuh: berkas SUMBER menang.

**Satu berkas per push tetap MENGIKAT** (KC-42, KC-43).

**Tentang push berkas ini:** ia di akar repo sehingga menyalakan `ci.yml`. Tidak satu
pun `tests/**` berubah, jadi cacah uji tetap **1377** — ramalan **deterministik**
(aturan 57), **MUDAH**, TIDAK diskor, TIDAK menambah beruntun. **Laporannya WAJIB
dibaca sebelum push akar berikutnya** (lihat aturan 38).

## STATE DIPECAH TIGA — BACA INI LEBIH DULU

1. **`STATE.md`** (berkas ini) — **bagian 1**: kepala, aturan bernomor 1–**85** (plus
   usulan 77, 78, 82, **86**), kelas cacat KC-1..**KC-52**.
2. **`STATE_LAMPIRAN_EKOR.md`** v12 — **bagian 2**: papan skor per ramalan, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** v12 — **bagian 3**: penyebut 787, taksonomi,
   karantina, bulan ABSEN, hipotesis H-A001..**H-A022**, lubang funding, byte parquet
   semesta, modul/workflow/uji, API terverifikasi.

**Ketiga berkas wajib dibaca bersama.** LANGKAH 0 PROMPT wajib menyebut ketiganya.

## CACAH TANGAN DIREKTORI — UTANG HIDUP

| direktori | cacah TERUKUR (tangan, bernomor) | ref |
| --- | --- | --- |
| `lux_ai/serapan/` (`.py`, termasuk `__init__.py`) | **49** | `3196fd98` / `8a614567` |
| `tests/` | **53** | idem |
| `.github/workflows/` | **44** | idem |
| akar repo | **18** entri (**6** direktori + **12** berkas) | idem |

**[v54] UTANG ATURAN 66 HIDUP.** Trio `selisih_lilin` sudah didorong (commit
`c1dc0009`), sehingga angka harapan **50 / 54 / 45** kini **TURUNAN** dan **DILARANG
dikutip sebagai terukur** sampai dicacah dengan tangan, bernomor, pada ref yang
disebutkan.

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

## KESALAHAN DOKUMEN SENDIRI — kini SEPULUH, dan yang kesepuluh berbeda jenis

| # | berkas | tertulis | seharusnya | status |
| --- | --- | --- | --- | --- |
| 1 | jurnal 132 §3 | "beruntun 2/1" | 2/2 | dikoreksi di STATE v50 |
| 2 | EKOR v10 | `terisi ≉49,7%` | `≈49,7%` | LUNAS di EKOR v11 |
| 3 | jurnal 135 §13.3 | "hendan dirumuskan" | "hendak" | LUNAS di STATE v51 |
| 4 | EKOR v11 kepala | "deretministik" | "deterministik" | LUNAS di EKOR v12 |
| 5 | UKUR v11 kepala | "KESERAIAN VERSI" | "KESERASIAN VERSI" | LUNAS di UKUR v12 |
| 6 | UKUR v11 daftar uji | penanda `**` tak berpasangan | berpasangan | LUNAS di UKUR v12 |
| 7 | STATE v52 | "Empat salah ketik" | "Enam" | LUNAS di STATE v53 |
| 8 | STATE v53 aturan 45 | "empat push terakhir adalah dokumen tunggal" lalu mendaftar **ENAM** butir | "enam push terakhir" | **LUNAS di berkas ini** |
| 9 | STATE v53 aturan 52 | pembacaan ulang "tidak menangkap satu pun" salah ketik | **kadang** menangkap — **satu dari delapan** | **LUNAS di berkas ini** |
| 10 | jurnal 138 §5 butir 2 | "maka **839.842.134 yang keliru**" | kesimpulan **tidak sah dari premisnya**; kedua angka benar | **LUNAS di jurnal 140** |

**Butir 10 adalah jenis yang berbeda dan lebih berbahaya.** Butir 1–9 adalah salah
ketik atau salah cacah. Butir 10 adalah **kesimpulan yang tidak sah dari premis yang
benar**: dari "839.325.999 adalah cacah baris parquet" saya melompat ke "maka
839.842.134 keliru", padahal dua angka dapat sama-sama benar bila mencacah **himpunan
berkas yang berbeda** — dan itulah yang terjadi. Ia lolos dari semua pemeriksaan
formal karena tampak beralasan.

**Bila berkas sumber dan koreksi ini bertentangan pada titik-titik itu, koreksi ini
menang** — pengecualian tersurat atas KC-41 yang HANYA berlaku untuk kesalahan yang
sudah diakui, tidak pernah untuk angka terukur.

**Pembacaan jujur atas pola ini, DIKOREKSI dari v53:** v53 menulis bahwa pembacaan
ulang aturan 52 "tidak menangkap satu pun" kesalahan. Itu terlalu keras terhadap
aturan 52 sendiri. Rumusan yang benar: pembacaan ulang **kadang** menangkap — **satu
dari delapan** kasus yang terlacak. Yang tetap benar: pembacaan ulang **kuat** untuk
memastikan berkas tidak terpotong atau tertimpa, dan **lemah** sebagai pemeriksa ejaan
dan penalaran. **Tidak ada berkas yang didorong ulang hanya demi satu karakter** —
`push_files` menulis ulang SELURUH berkas (KC-42). Setiap koreksi menumpang pada versi
berikutnya.

## KC-52 — DITUTUP. Dua angka itu keduanya benar.

**Ini menggantikan seluruh bagian "KOREKSI BESAR yang MASIH HIDUP" di v53.**

Dijumlahkan atas kedelapan laporan `reports/pulihkan_pecahan_<i>.json`:

```
Σ baris_utama     = 839.325.999
Σ baris_karantina =     516.135
Σ baris_total     = 839.842.134
```

> **839.325.999 + 516.135 = 839.842.134**

Dan `Σ baris_total` sama persis dengan angka run rilis `30404071324`.

| angka | apa yang ia cacah | keliru? |
| --- | --- | --- |
| **839.325.999** | baris parquet yang LOLOS gerbang, **19.586** simbol-bulan | **tidak** |
| **839.842.134** | seluruh baris parquet rilis, lolos **dan** karantina, **19.598** | **tidak** |
| **516.135** | **12** parquet karantina, di tar keluarga terpisah | — |

**Tidak pernah ada data yang hilang, tidak pernah ada pembaca yang cacat, tidak pernah
ada angka yang keliru.** Yang ada hanya **dua penyebut berbeda yang diperlakukan
sebagai satu**.

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
pecahan karena itu sah (aturan 22).

**Bonus terukur:** `19.598 = 19.586 + 12` kini bukan aritmetika yang dicocokkan dari
catatan, melainkan terukur dari dua belas parquet yang dibongkar, dicacah kakinya, dan
sidik tarnya dicocokkan terhadap manifes di git. **Dugaan lama "516.135 / 12 = 43.011
≈ sebulan penuh" kini boleh dikutip — tetapi sebagai rata-rata turunan, bukan sebagai
bukti**, sebab sebarannya nyata sangat tidak rata (42.585 sampai 131.760 per tar).

**Asal-usul `cacah_lilin` dan `cacah_lilin_terbaca` (terbaca dari kode, jurnal 139).**
`kehidupan_arsip.ukur_kolom` menulis keduanya dari **dua ekspresi yang berbeda**:
`cacah_lilin` = `n` = cacah baris parquet; `cacah_lilin_terbaca` = baris yang KEDUA
kolomnya berhasil diurai menjadi angka. Identitas yang dipaksakan badan fungsi:

> **`cacah_lilin` = `cacah_lilin_terbaca` + `cacah_baris_cacat`**

Karena `selisih_lilin` mengukur kedua medan identik pada **19.586 dari 19.586** baris,
identitas itu memaksa satu kesimpulan tanpa run tambahan: **`cacah_baris_cacat` = 0
pada seluruh semesta.** Tidak satu pun dari 839.325.999 baris gagal diurai.

`silang_funding.baca_medan_baris` **TIDAK cacat** (jurnal 138): ia memakai parameter
`medan` dua kali di badannya dan tidak memaku satu pun nama medan.

## Aturan bernomor

Aturan **1–36** berlaku tanpa perubahan; teks di STATE v19 (`e06c486e`), ringkas di v37
(`f520d5e2`).

**Aturan 10 (irisan/urutan bulan BUKAN sebab). [v54] Ditaati.**

**Aturan 21 (total papan skor dihitung tangan). [v54] Ditaati, dan lajur BERGERAK:**
218 + 57 = 275; 275 + 22 = 297; 297 + 9 = 306; 306 + 7 = **313**. Rincian: TEPAT
**218** · MELESET **57** · SEPARUH **22** · TIDAK TERADJUDIKASI **9** · MENUNGGU **7**.
N_percobaan = 0. **ADJUDIKASI RISET TETAP TERKUNCI.** MENUNGGU: R-7, R-19, R-20,
R-28, R-36, R-37, R-199. Dua ramalan diadjudikasi sejak v53: **R-312 → TIDAK
TERADJUDIKASI** (8→9), **R-313 → TEPAT** (217→218).

**Aturan 29 (pita praregistrasi TIDAK boleh diubah sesudah pengukuran). [v54] Ditaati
dua kali:** R-312 tidak diselamatkan meski penjelasannya kelak ditemukan; R-313
diregistrasikan lengkap di chat **sebelum** `pulihkan_pecahan_0.json` disentuh.

**Aturan 36 (dua modul berbeda atas semesta sama wajib cocok). [v54] Kasus terkuat
sampai kini:** `selisih_lilin` (839.325.999 dari medan `cacah_lilin`) dan `pulihkan`
(839.325.999 dari kaki parquet, lewat jalur unduhan-bongkar yang sama sekali berbeda)
bertemu **sampai satuan terakhir**. Dua jalur, dua modul, dua run, satu angka.

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

38. Cacah uji hanya sah dari `reports/ci_terakhir.json`. **[v54] Ditaati; ordinal maju
    ke ke-45.**

    | ke- | CI | run | commit | blob | jejak |
    | --- | --- | --- | --- | --- | --- |
    | 41 | 1341 | 30548418622 | `28afc9ae` | `2c3290cb` | EKOR v12, UKUR v12 |
    | 42 | 1341 | 30549286062 | `e68deab7` | `ed743bdf` | UKUR v12 |
    | 43 | 1341 | 30550547017 | `1247a5a3` | `fdb7c668` | STATE v53 |
    | 44 | 1341 | 30551789395 | `33a4ab37` | `5b16417b` | jurnal 136 |
    | **45** | **1377** | **30559145901** | **`c1dc0009`** | **`cdfdee25`** | **jurnal 137, berkas ini** |

    Pemakaian ke-45 dibaca **2026-07-30T15:57:01Z**, kode keluar **0**,
    `1377 tests collected in 0.58s`, atas push trio `selisih_lilin`.
    **Dua cacat tetap disebut:** **(a)** baris ke-**38** (run `30541051907`, CI 1297,
    commit `5d7d8b96`) **tanpa blob**, tidak dapat dipulihkan; **(b)** run
    **30547842823** (bot `de2fc03d`) **tidak pernah dibaca**, tertimpa, dan **DILARANG
    dihitung**. **Aturan kerja calon** — dua push akar berturut tanpa membaca laporan
    di antaranya pasti menghanguskan yang pertama — tetap **belum diangkat**; masih
    satu kejadian.
45. Keatomikan push pemicu. **[v54] Ditaati penuh pada trio R-312:**
    `selisih_lilin.py` + `test_selisih_lilin.py` + `selisih_lilin.yml` didorong sebagai
    **satu commit** `c1dc0009`. **KOREKSI atas v53:** v53 menulis "empat push terakhir
    adalah dokumen tunggal" lalu mendaftar **enam**; bacaan yang benar adalah **enam**.
46. Kode dilarang menyimpulkan dari penyebut nol. **[v54] Kasus positif terukur:**
    `pulihkan` VERSI 2 melaporkan `definisi_dapat_dibedakan` **false** pada pecahan 2
    dan 5 (tanpa karantina) dan menolak menyebut salah satu definisi. Perilaku itu
    terbaca apa adanya di laporan; aturan 46 **terbukti bekerja sebagaimana
    dirancang**.
47. Satuan cacah tersurat. **[v54] Ditaati:** "114", "17.398", "18.799", "1.401", "9",
    "53", "49", "44", "34", **"12"** bersatuan **baris atau berkas** — dan **34 lawan
    53 milik REPO BERBEDA**, sedangkan **12 bersatuan BERKAS PARQUET karantina**;
    "712.925", "291.379", "42.510", "808.162", "95.237", "18.143.601" bersatuan **lilin
    menit**; **"839.325.999", "516.135", "839.842.134" seluruhnya bersatuan BARIS
    PARQUET** — **[v54] ini koreksi penting atas v53**, yang menyatukan 839.325.999 dan
    516.135 sebagai "lilin menit" dan 839.842.134 sebagai "baris parquet" seolah
    berbeda satuan; sesudah KC-52 ditutup, ketiganya terbukti satu satuan yang sama
    atas himpunan berkas yang berbeda; "0,4087" **bagian tanpa satuan**; "29.873",
    "19.281", "14.839" bersatuan **byte berkas sumber**; **"1377"** bersatuan **butir
    uji terkumpul pytest**; "45" pada aturan 38 bersatuan **pemakaian berjejak**.
48. Berkas modul mendekati 800 baris dipecah. **[v54] PERINGATAN DINI berlanjut.**
50. Pengukuran yang menyimpulkan dari KETIADAAN wajib memuat kendali positif.
    **[v54]** `kehidupan_arsip.kendali_pecahan` terbaca: tiga simbol-bulan ber-byte
    parquet terbesar, dipilih dari manifes **sebelum** data dibaca, deterministik, dan
    tidak melihat volume maupun transaksi. Kepatuhan **terverifikasi dari kode**, bukan
    dari klaim docstring.
52. Laporan yang tidak dapat dibaca utuh setara dengan laporan yang tidak ada.
    **[v54] Ditaati empat kali berturut:** jurnal 137 (`432d568e`), 138 (`596a3148`),
    139 (`9684bed3`), 140 (`a659206c`) — masing-masing dibaca UTUH dengan blob dicatat.
    **Batas kekuatannya, DIKOREKSI:** ia menangkap **satu dari delapan** kesalahan yang
    terlacak; ia kuat terhadap pemotongan dan penimpaan, lemah terhadap ejaan dan
    penalaran.
    **UTANG BACA yang TETAP hidup:** ketiga berkas trio `c1dc0009` belum dibaca ulang
    utuh; `decisions/ADR-A002`, **A004**, **A006**, **A007**, **A008**;
    `karantina_semesta.yml` (`de40fa4e`); `tests/test_pulihkan.py` (`11c43533`);
    `test_rilis_karantina.py` (`739c8da9`); `test_karantina_a006.py` (`a5a3d82f`).
    **Bukti tak langsung (CI 1377, laporan lengkap) TIDAK diklaim sebagai lunas.**
55. Rumusan pemicu workflow wajib dikutip dari berkas beserta blobnya. **[v54]**
    `selisih_lilin.yml` mengikuti pola trio; blobnya belum dibaca ulang (lihat 52).
57. Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB ditulis bernomor.
    **[v54] BERUNTUN 4 DARI 4.** Kesempatan keempat: 36 butir `test_01`..`test_36`
    ditulis bernomor, ramalan **1341 + 36 = 1377** dinyatakan **sebelum** laporan CI
    dibaca, terukur **1377**. Push dokumen — termasuk berkas ini — meramalkan CI tetap
    **1377**; ramalan itu MUDAH, deterministik, TIDAK diskor, TIDAK menambah beruntun.
58. Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH DILARANG
    diramalkan dengan pita sempit.
63–76. Berlaku tanpa perubahan dari v43 (`a91a4934`).

**Aturan 66 (cacah direktori dengan TANGAN, bernomor). [v54] UTANG HIDUP** — lihat
bagian cacah tangan di atas. Harapan 50/54/45 adalah TURUNAN.

**Aturan 77, 78 (TETAP DIUSULKAN). [v54] Tidak mendapat kasus baru.**

**Aturan 79 (BERLAKU sejak v44). [v54] Ditaati:** praregistrasi R-312 ditulis di jurnal
136, adjudikasinya pada giliran berbeda. **R-313 adalah pengecualian yang wajib
disebut terbuka:** ia diregistrasikan **di chat**, bukan di `journal/**`, karena
pengukurnya bukan modul baru melainkan pembacaan laporan yang sudah ada, dan
menuliskannya ke jurnal lebih dulu berarti satu push tambahan sebelum data dibuka.
Bunyinya dikutip lengkap dan kata demi kata di jurnal 140 §2. **Ini melemahkan aturan
79 dan harus dicatat, bukan dibenarkan** — satu-satunya saksi bahwa ramalan itu
ditulis lebih dulu adalah riwayat percakapan, bukan git.

**Aturan 80, 82, 83, 84 [v54]** berlaku tanpa perubahan.

**Aturan 81 (BERLAKU sejak v46). [v54]** Tidak terpicu oleh R-313: dua belas parquet
karantina tersebar di enam pecahan berbeda dan bukan satu peristiwa tunggal. Untuk
R-310 aturan 81 TETAP terpicu.

**ATURAN 85 (RESMI sejak v52), BERLAKU MULAI R-312. [v54] Dipakai pertama kali di
praregistrasi R-312** (jurnal 136). Hasilnya tidak dapat dinilai: R-312 TIDAK
TERADJUDIKASI, sehingga **aturan 85 masih belum punya satu pun adjudikasi**.

### ATURAN 86 — DIUSULKAN (dua kejadian terukur, layak dinaikkan)

> Sebelum menulis modul pengukur baru, dua hal WAJIB dikerjakan lebih dulu: **(i)**
> badan fungsi atau berkas yang hendak diukur dibaca UTUH; **(ii)** `reports/` diperiksa
> untuk mengetahui apakah jawabannya sudah tersimpan. Menulis pengukur atas sesuatu
> yang sudah tertulis adalah mengukur yang sudah diketahui.

**Kejadian 1 (jurnal 138).** Uji pemisah cabang (a)/(b) ditaksir butuh satu modul,
satu push, satu run CI, dan satu pembacaan laporan. Biaya sebenarnya: **satu
pembacaan** `silang_funding.py`.

**Kejadian 2 (jurnal 140).** Modul `selisih_lilin` ditulis lengkap dengan **36** butir
uji dan satu workflow untuk mencari asal 516.135. Jawabannya sudah tersimpan di
`reports/pulihkan_pecahan_<i>.json` sejak **29 Juli**, **dua hari sebelum**
pertanyaannya dirumuskan.

**Status: DIUSULKAN**, belum resmi. Dua kejadian sudah cukup menurut ambang yang
dipakai untuk aturan sebelumnya, tetapi peresmiannya diserahkan ke ADR-A019 agar tidak
mengulang KC-48 (mengangkat aturan dari kesan, bukan dari cacah).

**Penomoran aturan [v54].** Aturan resmi: **1–81, 83, 84, 85**. Nomor **82**
dicadangkan; **77**, **78**, **86** usulan. **Aturan berikutnya yang bebas: 87.** Satu
calon tanpa nomor tetap menunggu kejadian kedua: larangan dua push akar berturut tanpa
membaca laporan CI di antaranya.

## R-312 — ADJUDIKASI RESMI: TIDAK TERADJUDIKASI

Laporan `reports/selisih_lilin_ringkas.json` (blob `e5cc6401`, sidik kode
`e6c77965…`): `cacah_berselisih` **0** dari 19.586 baris; `jumlah_klaim_langsung` =
`jumlah_terbaca_langsung` = **839.325.999**; `bagian_teratas` null; `sebaran_kelas`
`{}`; keempat kendali lolos; `dua_jalur_bertemu` true; `selisih_invarian`
delapan-delapannya 0; kode keluar alur modul **2** (dirancang).

**Poros ramalannya runtuh sebelum diadjudikasi:** ia mengandaikan `cacah_lilin_terbaca`
adalah pengukuran kedua yang **bebas** dari `cacah_lilin`. Nama berbeda diperlakukan
sebagai isi berbeda. Sesudah jurnal 139 membaca `ukur_kolom`, terbukti keduanya
berbeda ekspresi tetapi selalu bertemu karena tak satu baris pun cacat.

**Larangan yang menempel pada R-312, seluruhnya tetap berlaku selamanya:**

1. **DILARANG** mengatakan pita R-312 butir 1 (12..120) "tidak terbantah".
2. **DILARANG** mengatakan kalibrasi membaik atau memburuk karena R-312.
3. **DILARANG** menghitung R-312 di pembilang maupun penyebut nisbah kemenangan.
4. **DILARANG** menghidupkannya kembali dengan alasan penjelasannya kini ditemukan.
5. Angka **12** yang muncul di R-313 adalah cacah **parquet karantina** — arti yang
   berbeda dari 12 di R-312 butir 1. **Kesamaan itu DILARANG dibaca sebagai konfirmasi
   apa pun** (syarat gugur nomor 3, jurnal 136).

## R-313 — ADJUDIKASI RESMI: TEPAT (kedua butir)

| butir | berisiko | ramalan | terukur | hasil |
| --- | --- | --- | --- | --- |
| 1 — Σ `baris_karantina` | ya, titik tunggal | **516.135** | **516.135** | **TEPAT** (selisih 0) |
| 2 — Σ parquet karantina | ya, titik tunggal | **12** | **12** | **TEPAT** (selisih 0) |

Diregistrasikan lengkap sesudah `pulihkan.py` dibaca tetapi **sebelum** laporan pertama
dibuka. Penggugur dipasang di muka: satu laporan hilang → TIDAK TERADJUDIKASI.
Kedelapan ada.

**Yang DILARANG diklaim darinya:** bahwa kalibrasi membaik. Satu kemenangan bukan
tren, dan larangan KC-51 berlaku sama ke arah sebaliknya. R-313 juga tidak menyentuh
satu pun besaran yang sebarannya belum diukur — ia menjumlahkan angka yang sudah
tercatat — sehingga **ia bukan bukti bahwa KC-51 melemah**.

## R-311 — ADJUDIKASI RESMI: SEPARUH (tidak berubah)

| butir | berisiko | pita | terukur | hasil |
| --- | --- | --- | --- | --- |
| 1 — cacah baris berdefisit | ya | 200 .. 12.000 | **114** | **KALAH** |
| 2 — bagian sepuluh teratas | ya | 0,02 .. 0,45 | **0,4087** | **MENANG** |
| 3 — penggugur bersih + invarian nol | tidak | — | bersih | menang, tidak diskor |

**Rumusan resmi (ADR-A018 kep. 3) — satu-satunya yang boleh dikutip:** dari **17.398**
baris bukan-pertama dan bukan-MATI, hanya **114** (**0,66%**) berdefisit; keseratus
empat belas menanggung **712.925** lilin, rata-rata **6.254**; sepuluh teratas
menanggung **291.379**, yaitu **0,4087**; terbesar **TLMUSDT 2023-03**, HIDUP,
**2.130 dari 44.640** lilin (**95,2% kosong**).

Larangan penyertanya tetap berlaku seluruhnya: 712.925 bukan pengukuran bebas (KC-50,
KC-37); "114 seluruhnya HIDUP/SEPI, nol MATI" bukan temuan; tidak satu kalimat pun
boleh menyimpulkan tentang harga; butir 2 menang **TIPIS ke tepi ATAS**.

## Kelas cacat

KC-1 s.d. KC-12 seperti v19; KC-10, KC-11 DITUTUP. KC-13 keterwakilan sampel. **KC-16
DITARIK — nomornya TETAP kosong selamanya.** KC-17 DITUTUP. Teks penuh KC-14, KC-15,
KC-19..KC-29 di v37 (`f520d5e2`). KC-30..KC-42 di v43 (`a91a4934`). KC-43, KC-44 di
v44. KC-45, KC-46 di v45. KC-47 di v46. KC-48 di v47. KC-49 di v48. KC-50 di v50.
KC-51 teks penuh di v52/v53. **KC-52 teks penuh di bawah.**

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
**kesepuluh** butir di tabel atas.

**KC-51 — [v54] tidak mendapat kejadian kelima.** Keempat kejadiannya tetap berdiri
tanpa pembalikan arah. R-312 tidak menambah kejadian (tidak teradjudikasi); R-313 tidak
menambah pembalikan (ia bukan taksiran atas sebaran yang belum diukur).

### KC-52 (RESMI sejak berkas ini) — dan langsung DITUTUP

**Dua penyebut berbeda diperlakukan sebagai satu. Rumusan resmi:**

> Ketika dua angka besar atas "semesta yang sama" tidak cocok, kemungkinan pertama yang
> wajib diperiksa bukanlah bahwa salah satunya keliru, melainkan bahwa keduanya
> **mencacah himpunan yang berbeda**. Selisih yang tak terjelaskan adalah dugaan tentang
> **batas himpunan**, bukan tentang mutu pengukuran.

**Kejadiannya:** 839.325.999 lawan 839.842.134, selisih 516.135, hidup sejak jurnal
131 dan bertahan berpuluh giliran. Sepanjang itu ia diperlakukan berturut-turut sebagai
salah aritmetika, lalu sebagai kemungkinan cacat pembaca, lalu sebagai kemungkinan
salah satu angka keliru. **Ketiganya salah.** Batas himpunannya berbeda: satu
mengecualikan 12 simbol-bulan karantina, satu tidak.

**Ia DITUTUP pada giliran yang sama ia diresmikan**, sebab jawabannya terukur penuh
(lihat bagian KC-52 di atas). Ia tetap dicatat sebagai kelas cacat karena bentuk
kesalahannya akan berulang: repo ini punya **beberapa** penyebut yang mirip — 19.586
lawan 19.598, 880 lawan 877 lubang funding, 18.799 lawan 17.398 — dan tiap pasang itu
adalah undangan bagi kesalahan yang sama.

**Kerabat:** KC-25 (batas semesta tak tersurat), KC-36 (homonim), KC-39 (dua penyebut
bulan absen dicampur), aturan 44 (ramalan wajib menyebut penyebut).

**Kelas cacat berikutnya yang bebas: KC-53.**

## Hipotesis

**H-A020 (DIUSULKAN, BELUM DIUJI)** — ketujuh baris MATI tak penuh berbulan `2024-05`
adalah SATU peristiwa; jendelanya sembilan lilin (39.308..39.317). **DILARANG** menulis
"tujuh simbol didelisting 28 Mei 2024".

**H-A021 (DIUSULKAN, BELUM DIUJI)** — **ANCUSDT 2022-05** (defisit 26.959) dan
**LUNAUSDT 2022-05** (26.950) adalah SATU peristiwa. Dasarnya HANYA selisih sembilan
lilin — **kebetulan angka, bukan bukti**. Bila kelak DITERIMA: cacah pengamatan bebas
sepuluh teratas turun 10→9, dan `bagian_teratas` **TIDAK berubah**.

**H-A022 — TERBUKTI (berkas ini).** Selisih 516.135 adalah cacah baris parquet dari 12
simbol-bulan karantina yang berada di luar penyebut 19.586. Terbukti pada rumusannya
yang tepat, lewat R-313, dengan selisih nol pada dua butir.

**Peringatan yang menempel pada H-A020 dan H-A021:** bentuk buktinya IDENTIK, dan
pengulangan bentuk itu patut dicurigai. Uji yang menegakkan atau meruntuhkan keduanya:
**lubang tengah pada gugus `2022-05` dan `2024-05`**. **DILARANG** menyebut sebab, nama
peristiwa pasar, atau tanggal penghentian sampai diuji.

Hipotesis berikutnya **H-A023**.

## Berkas akar — status hidup/mati, LENGKAP 5 dari 5

- **`STATE_LAMPIRAN.md`** (`f2b90764`, 2.350 B) — HIDUP sebagai arsip naratif
  (L-1..L-5). Tidak memuat angka semesta.
- **`STATE_LAMPIRAN_ANGKA.md`** (`f3ebdb02`, 1.841 B) — HIDUP tetapi hampir kosong.
  `N_percobaan` = 0. Memuat klaim TERLARANG (Signals 10.032 / +189,41R / PF 1,61 dan
  seluruh tabel tuning `AUDIT.md`). **Jangan dicampur dengan penyebut 19.586** (KC-36).
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
  **[v54] Masih belum dikerjakan.**
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
  (KC-51) — **dan [v54] R-313 pun DILARANG dibaca demikian**.
- Ramalan CI yang laporannya sudah tertimpa **DILARANG diklaim menang**.
- **[v54] Kelima larangan R-312** di bagian adjudikasinya berlaku penuh.
- **[v54] DICABUT:** larangan memperlakukan 839.842.134 dan 839.325.999 sebagai
  berbeda keterpercayaan. Keduanya kini terbukti benar atas himpunan masing-masing;
  yang DILARANG sekarang adalah **memakai salah satunya tanpa menyebut penyebutnya**.

## Angka semesta yang mengikat

Penyebut **19.586** (LOLOS gerbang) · semesta rilis penuh **19.598** = 19.586 + **12**
karantina (**terukur**, bukan turunan) · `cacah_simbol` **787** · bukan-pertama
**18.799** · HIDUP **18.087** · SEPI **98** · MATI **1.401** (penuh 1.392 / tak penuh
9) · `cacah_lain` **0** · `defisit_total` **18.143.601** · `defisit_pertama`
**17.335.439** (95,5%; rata 22.027; keterisian ≈49,7%) · `defisit_bukan_pertama`
**808.162** (0,0445) · `defisit_sembilan` **95.237** (0,1178) · sisa **712.925** · calon
**17.398** · calon penuh **17.284** · calon berdefisit **114** (0,66%) ·
`defisit_teratas` **291.379** · `bagian_teratas` **0,4087** · `defisit_terbesar`
**42.510** · rata **6.254** · **baris parquet lolos gerbang 839.325.999** · **baris
parquet karantina 516.135** · **baris parquet rilis penuh 839.842.134** ·
`cacah_baris_cacat` **0** di seluruh semesta · total byte parquet **32.706.262.375** ·
`byte_mati` **579.041.399** · `cacah_hidup_byte_kecil` **38** · `cacah_mati_byte_kecil`
**2** · bulan pertama HIDUP **769** + SEPI **18** = 787 ✅ · lubang funding **880**
semesta / **877** dalam penyebut / 3 tak dikenal · `cacah_simbol_ada_lubang` **122** ·
jumlah uji **1377** (repo riset ini).

## Ke bagian 2 dan 3

**Utang lampiran yang lahir dari berkas ini — besar:** EKOR **v13** dan UKUR **v13**
wajib menaikkan kepala ke "milik STATE v54" dan memasukkan: papan skor **313**, R-312
TIDAK TERADJUDIKASI, R-313 TEPAT, pemakaian aturan 38 **ke-43/44/45**, jumlah uji
**1377**, aturan 57 beruntun **4/4**, jurnal 136–140, trio `selisih_lilin`, **KC-52**,
**H-A022 TERBUKTI**, usulan **aturan 86**, API `pulihkan` V2 dan `kehidupan_arsip`, dan
daftar kesalahan dokumen yang kini **sepuluh**.

## Penomoran berikutnya

Jurnal **141** · STATE **v55** · EKOR **v13** · UKUR **v13** · PROMPT **v55** · ADR
**A019** · KC **KC-53** · aturan **87** (86 diusulkan) · hipotesis **H-A023** · ramalan
**R-314** · papan skor **313**.

**Poros yang tersisa, urut prioritas:**

- **(a) Lubang tengah gugus `2022-05` dan `2024-05`** — menguji H-A021 dan H-A020
  sekaligus. **Kini poros tunggal dengan prioritas tertinggi**, sebab poros (b) selesai.
- **(b) Irisan 880 lawan 877 lubang funding** — kandidat KC-52 berikutnya: dua penyebut
  mirip yang belum pernah dijajarkan.
- **(c) Sebab kekosongan TLMUSDT 2023-03** — baris paling kosong di semesta, berstatus
  HIDUP.

Sebelum pita dikunci, seluruhnya WAJIB: aturan **79** (praregistrasi di `journal/**`),
**83** (aritmetika implikasi lebih dulu), **85** (tepi "terpusat" di lantai aritmetis
atau paling banyak satu orde di atasnya, dengan alasan tertulis), **84** (klausa
tunggal), **KC-50** (agregat lewat jalur LANGSUNG), **KC-52** (batas himpunan tiap
angka disebut tersurat), aturan **66** (cacah tangan sebelum menamai modul), dan
`BATAS_BARIS_LAPORAN` ringkas. **Usulan aturan 86 berlaku sebagai kebiasaan kerja
sejak sekarang meski belum resmi:** baca berkasnya, periksa `reports/`, baru tulis
pengukur.
