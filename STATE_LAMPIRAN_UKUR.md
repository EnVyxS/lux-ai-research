# STATE lampiran UKUR — bagian 3 dari STATE (v21, milik STATE v63)

**TRIO AKAR SERASI PENUH KEMBALI — NAMA DAN ISI.** Keserasian yang dicapai v20 pecah
begitu STATE v63 naik, persis seperti yang v20 ramalkan tentang dirinya sendiri. Dengan
berkas ini ia pulih, dan kali ini **utang penamaan nol untuk ketiganya sejak awal**:

| berkas | versi | blob | commit |
| --- | --- | --- | --- |
| `STATE.md` | **v63** | `515abb2981d2c07374e6f5b7ea0a080622049580` | `3f5ec7e4f3a2d555b84a07524abd88f2d3c26083` |
| `STATE_LAMPIRAN_EKOR.md` | **v21** | `9bd48a49af9e95c47d273d396e2dfc6130e11503` | `4044854573888d39920b9da6233d1f326683ec6d` |
| `STATE_LAMPIRAN_UKUR.md` | **v21** | berkas ini | — |

**Papan skor 339 SAH sejak EKOR v20, TIDAK BERGERAK di EKOR v21.** Berkas ini **tidak
memuat dan tidak berwenang mengesahkan** papan skor (aturan 29) — pembagian kewenangan
itu tidak berubah dan tidak akan berubah di sini.

**Keserasian ini akan pecah lagi begitu STATE v64 naik.** Itu bukan cacat; itu bentuk
kerja trio. Yang dilarang adalah **menyatakan trio serasi tanpa memeriksa ketiga blob**.

**Dasar v21:** UKUR v20, blob **`56cfded0c4e8711a96d79df28d9bd4b006fc3604`**, commit
**`8e6f583df0816e262b23ad1a0e2c68b41ea4df02`**, **dibaca UTUH pada giliran yang sama
sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43), berakhir pada penanda
penutupnya — jadi **aturan 92 terpenuhi pada bahan, bukan hanya pada keluaran**.

**BERKAS INI PADAT DENGAN SENGAJA** (aturan 78, aturan 92). Bagian warisan **dirujuk ke
blob, BUKAN disalin ulang**.

### BAGIAN WARISAN YANG DIRUJUK, BUKAN DISALIN

Sah dikutip dari **UKUR v20 `56cfded0c4e8711a96d79df28d9bd4b006fc3604`**, tidak berubah:
rantai serapan `pecahan.jalankan` → parquet · isi `pecahan.py` / `serap.py` /
`klines.py` · tabel **dua belas karantina** lengkap dengan `nisbah_lilin` dan
`selisih_menit` · pendamaian 11 + 1 = 12 beserta larangan menskorkannya · Koreksi 17 ·
tabel ukuran dan blob kedelapan `manifes_pecahan_*.json` · utang ukur 30 · peresmian
aturan 88/89/91/92.
Sah dikutip dari **UKUR v19 `47df297d146697749643019d0bda216c5a88059a`**: `lubang_awal.json` ·
`bulan_absen_ringkas.json` · jembatan 48/50/51 · semesta bulan 1m · lubang tengah dan
H-A010 · silang funding · KC-18 · Koreksi 1–16 · butir 19 · H-A001..H-A023.
Sah dikutip dari **UKUR v18 `11b14975a7ee2b00ca5e25ca19fc4e16ad5c1deb`**: sisa defisit ·
keterisian lilin · irisan bulan pertama · irisan byte · byte parquet semesta · arah
waktu kematian.

**Merujuk BUKAN menghapus.** Bila berkas ini bertentangan dengan yang dirujuk, **yang
dirujuk menang** dan pertentangan itu wajib dicatat sebagai koreksi baru.

**Tentang push berkas ini:** di akar repo → menyalakan `ci.yml`. Tidak satu pun
`tests/**` berubah → cacah uji tetap **1377**; deterministik, **MUDAH**, TIDAK diskor,
TIDAK menambah beruntun aturan 57. Laporannya WAJIB dibaca sebelum push akar berikutnya
(aturan 38 **ke-73**) dan **WAJIB DITOLAK bila medan `commit` tidak cocok** (aturan 90) —
larangan yang sejak giliran lalu **bukan lagi teori**.

## [v21] ATURAN 78 RESMI — DAN INILAH RUMAHNYA

ADR-A023 kep. 2 meresmikan aturan 78 dan menetapkan **lampiran UKUR sebagai rumah
angka-angkanya**. Seluruh batas alat yang pernah **terukur** sepanjang riset dikumpulkan
di satu tempat untuk pertama kalinya. **Setiap baris di bawah ini adalah pengamatan,
bukan spesifikasi alat** — tidak satu pun angka ini diumumkan oleh alatnya sendiri.

### § 3.1 — Batas TULIS

| perkara | angka | dasar |
| --- | --- | --- |
| tulis aman, terbukti berulang | **±25–45 KB** per push | seluruh push akar sesi ini |
| tulis GAGAL DIAM-DIAM | butir 19: UKUR v19 `c28202df` | push dilaporkan **BERHASIL**, isi terpotong |
| satu berkas per push | MENGIKAT | aturan 29 |

**Butir 19 adalah satu-satunya bukti langsung** bahwa keberhasilan panggilan **bukan**
bukti keutuhan tulisan. **DILARANG menyimpulkan ada ambang tulis yang aman secara pasti**
— yang terukur hanya bahwa berkas berukuran wajar pernah berhasil, dan sekali gagal
tanpa peringatan. Penangkalnya bukan angka, melainkan **aturan 52 + aturan 92**:
pembacaan ulang utuh sampai penanda penutup.

### § 3.2 — Batas BACA, empat titik terukur

| # | perkara | byte terukur | perilaku alat |
| --- | --- | --- | --- |
| (a) | `reports/manifes_pecahan_3.json` | **2.257.314** | **PENOLAKAN PENUH**, berteriak, isi NOL |
| (b) | `reports/silang_funding.json` | **194.728** | terpotong, berteriak `showing 54%` |
| (c) | `reports/semesta_rentang.json` | **110.662** | terpotong, berteriak `showing 95%` |
| (d) | daftar direktori `reports/` | — | terpotong, berteriak `showing 76%` |

Galat penolakan penuh, verbatim: `File reports/manifes_pecahan_0.json is too large to
display (2530465 bytes). Use the download URL to fetch the content: …`
Pembaca kedua `connections.web.loadPage` atas URL mentah menjawab verbatim
`{"url":"","title":"Unable to load","text":"Content not available","score":0}` —
**repo tertutup; `raw.githubusercontent.com` tidak dapat dipakai sama sekali.**

> **ZONA YANG BELUM TERUKUR, DAN LARANGAN INTERPOLASI.** Antara **194.728 B** (terpotong
> 54%) dan **2.257.314 B** (ditolak penuh) **tidak ada satu pun pengukuran**. **DILARANG
> menginterpolasi ambang** dan **DILARANG menyatakan berkas 250 KB atau 500 KB "pasti
> terpotong sekian persen"**. Berkas yang belum dibaca dan berada di zona itu —
> khususnya `reports/bulan_absen.json` (**249.992 B**) dan `reports/funding_semesta.json`
> (**394.142 B**) — wajib diperlakukan **mungkin terpotong**, bukan **pasti**.

**Sisi lain yang juga belum terukur:** tidak ada satu pun berkas di bawah 110.662 B yang
pernah terpotong ALAT sepanjang catatan. **Itu bukan jaminan.** Nol kejadian bukan
kemustahilan (KC-53) — aturan yang sama yang melarang kita menyebut `selaras_menit`
mustahil menyala melarang kita menyebut berkas kecil pasti aman.

### § 3.3 — EMPAT KELAS PEMOTONGAN, kini berumah di aturan 78

Tabel ini pindah dari v20 ke sini sebagai lampiran resmi aturan 78. Isinya tidak berubah:

| kelas | siapa memotong | berteriak? | isi yang didapat | penangkal |
| --- | --- | --- | --- | --- |
| ALAT | alat baca | **YA** — `truncated (showing NN%)` | sebagian | membaca peringatan |
| MODUL | kode penulis laporan | TIDAK | sebagian | aturan 86 (b) |
| PENYUSUN | penyusun berkas | TIDAK | sebagian | aturan 52 + 92 |
| PENOLAKAN PENUH | alat baca | **YA** | **NOL** | **aturan 93 + 78** |

**Yang paling berbahaya tetap dua kelas yang TIDAK berteriak**, dan keduanya hanya
tertangkap oleh membaca ulang dan membaca kode — bukan oleh angka.

### § 3.4 [BARU] — KEGAGALAN PANGGILAN: kelas kelima yang BUKAN pemotongan

Giliran lalu, percobaan pertama mendorong EKOR v21 **ditolak** dengan galat verbatim:
`payload.owner should be not present, instead was "EnVyxS"` dan
`payload.repo should be not present, instead was "lux-ai-research"`.
Sebabnya `owner` dan `repo` dituliskan **di luar** `toolArguments`.

**Ia BERTERIAK dan GAGAL BERSIH:** tidak ada commit, tidak ada berkas separuh, tidak ada
laporan CI yang lahir. Karena tidak melahirkan artefak cacat, ia **BUKAN kelas
pemotongan kelima** dan **DILARANG dimasukkan ke tabel § 3.3**. Ia dicatat di sini hanya
karena ia batas alat.

**Bentuk panggilan yang benar, satu-satunya yang berlaku:**
`{toolName, toolArguments:{owner, repo, …}}`.

**Ini kegagalan panggilan alat GitHub PERTAMA sepanjang sesi ini**, dan kalimat
*"tidak ada kegagalan panggilan alat GitHub sepanjang sesi ini"* yang berdiri di catatan
kejujuran sejak v16 **DICABUT**. **DILARANG mengutipnya dari versi mana pun sesudah v20.**

## [v21] UTANG UKUR 31 DIBUKA — EMPAT KLAUSA NOL KEJADIAN

Lahir dari ADR-A023 kep. 5, menggantikan **KC-59 yang DIBUANG**. **KC-59 DILARANG
dikutip sebagai usulan hidup.**

Empat dari enam klausa gerbang 1m mencatat **nol kejadian pada 19.598** —
`deret_tidak_kosong`, `tanpa_duplikat`, `selaras_menit`, `satuan_milidetik` — sementara
`jarak_60_detik` dan `tanpa_menit_hilang` menyala **12 kali, selalu berpasangan**.

> **UTANG UKUR 31.** Untuk **masing-masing** dari keempat klausa itu, tetapkan **dari
> kode, bukan dari laporan**, apakah nol itu berarti:
> **(a)** mustahil menyala secara struktural · **(b)** mungkin menyala tetapi tak pernah
> terjadi · **(c)** belum diketahui.
> Sertakan **penyebut** dan **definisi uji** tiap klausa (aturan 74).

**Yang sudah terukur hari ini, dan hanya ini:**

| klausa | status | dasar |
| --- | --- | --- |
| `tanpa_duplikat` | **(a) mustahil** | `klines.rapikan` membuang duplikat **sebelum** gerbang dipanggil — terbaca dari `klines.py` `cc4d9287…` |
| `deret_tidak_kosong` | **(c) belum diketahui** | asal-usulnya sendiri belum jelas (utang verifikasi 48) |
| `selaras_menit` | **(c) belum diketahui** | **DILARANG disebut mustahil** |
| `satuan_milidetik` | **(c) belum diketahui** | **DILARANG disebut mustahil** |

**Utang ukur 31 dan utang verifikasi 48 BERSINGGUNGAN, TIDAK SAMA.** 48 menanyakan
**asal-usul** `deret_tidak_kosong`; 31 menanyakan **mengapa nol kejadian**. **DILARANG
menganggap satu membayar yang lain.**

**Akibat yang sudah boleh ditulis sekarang:** dalam praktik semesta, gerbang 1m adalah
penyaring **satu perkara** — menit hilang, yang menyalakan dua klausa sekaligus.
**DILARANG menyebut gerbang "berlapis enam" di artefak mengikat**, dan **DILARANG pula**
menyimpulkan gerbang "berklausa satu pasang" sebelum utang ukur 31 dibayar dari kode.

## Jumlah uji — terukur

**1377, kini DUA PULUH DELAPAN bacaan berjejak di berkas ini.** Bacaan 1–25 tercatat di
v16–v20. Tiga yang baru:

26. blob **`e5e015037d7af172d03e7e532775808672a22165`**, run **30616177405**, commit
    **`8e6f583d`** (UKUR v20), **08:24:41Z**, kode 0, `1377 in 0.61s`.
27. blob **`a993ff3a7a55b3832e978e846892b47ffa968e4e`**, run **30617261973**, commit
    **`3f5ec7e4`** (STATE v63), **08:43:06Z**, kode 0, `1377 in 0.64s`.
28. blob **`75bee028a26483391e825d13307dc9eccda45169`**, run **30617907684**, commit
    **`4044854573888d39920b9da6233d1f326683ec6d`** (EKOR v21), **08:54:05Z**, kode 0,
    `1377 tests collected in 0.65s`.

Turunan: 1341 + **36** butir `test_selisih_lilin.py` = **1377** ✅
**Rentang waktu kutip 0,40s–0,67s DILARANG dibaca sebagai pengukuran apa pun tentang
repo** — ia keadaan mesin CI.

**Utang ukur 27 tidak bergerak:** apakah **16** butir `tests/test_gerbang_1m.py`
termasuk dalam 1377 **belum diukur**. **DILARANG menjumlahkan 1377 + 16.**

**Aturan 57: beruntun 4 dari 4**, tidak bertambah.

### Aturan 38 — ordinal, kini sampai ke-72

Ordinal 42–69 tercatat di v16–v20. Tiga baris baru:

| ke- | CI | run | commit | blob | jejak |
| --- | --- | --- | --- | --- | --- |
| **70** | **1377** | **30616177405** | **`8e6f583d`** | **`e5e015037d7af172d03e7e532775808672a22165`** | **UKUR v20** |
| **71** | **1377** | **30617261973** | **`3f5ec7e4`** | **`a993ff3a7a55b3832e978e846892b47ffa968e4e`** | **STATE v63** |
| **72** | **1377** | **30617907684** | **`40448545`** | **`75bee028a26483391e825d13307dc9eccda45169`** | **EKOR v21** |

Ke-72 **COCOK pada percobaan pertama**; ke-71 cocok pada percobaan **kedua** (lihat § di
bawah). **Pemakaian berjalan = ke-tujuh puluh dua.**
**Panjang deret berjejak, aritmetika terbuka (butir 17):** ke-42..ke-72 → 72 − 42 = 30;
30 + 1 = **31 pembacaan berturut**.

**Bot CI** menambah satu commit di atas tiap push pemicu — kini **dua puluh tujuh kali
berturut**, terbaru **`d2455b832944f0966c49f3c2fe6a6f4d4a99d99a`** (di atas EKOR v21).
Deterministik dari `ci.yml` (`c79497b2`); **DILARANG dihitung kemenangan ramalan.**
Push `journal/**` dan `decisions/**` tidak menyalakan CI — ADR-A023 tanpa commit bot.

**Tiga cacat lama tetap disebut apa adanya:** ke-**38** tanpa blob · run **30547842823**
tertimpa · laporan push **`c28202df`** tertimpa sebelum dibaca. **Ketiganya DILARANG
dihitung; deret tidak putus. Cacat keempat TIDAK lahir** — laporan yang ditolak pada
ke-71 bukan laporan hangus, melainkan laporan **sah milik push lain** yang dibaca terlalu
dini.

### [v21] ATURAN 90 MENYALA PERTAMA KALI — dan aturan 77 dipakai pertama kali

Sesudah **sembilan** pemakaian tanpa nyala (ke-62..ke-70), pemakaian **kesepuluh**
menolak sebuah laporan: pembacaan pertama sesudah push STATE v63 (`3f5ec7e4…`)
mengembalikan `run_id` **30616177405**, `commit` **`8e6f583d`** — laporan **ke-70** milik
UKUR v20, yang sudah dibukukan. **DITOLAK; tidak dihitung sebagai ke-71.**

Blob laporan basi itu, **`e5e01503…`**, **identik** dengan blob bacaan ke-70 → menurut
**aturan 77** ia **bukan pengukuran kedua**. Inilah pemakaian pertama aturan 77, satu
giliran sesudah ia diresmikan.

> **DILARANG** menghitung kesepakatan aturan 90 dan aturan 77 sebagai **dua bukti
> bebas** — keduanya membaca **satu berkas yang sama**, karenanya **berkorelasi
> sempurna** (aturan 91). **DILARANG** menyebut aturan 90 maupun aturan 77 "teruji":
> satu nyala dari **sebelas** pemakaian (ke-62..ke-72) adalah **satu kejadian**, bukan
> pengujian.

**Aturan 90 dipakai SEBELAS kali sejak diresmikan, SATU nyala.**

## Modul dan berkas — yang bergerak di v21

**Tidak satu pun modul baru dibaca pada giliran ini.** Dua giliran berturut tanpa satu
pun berkas kode dibuka. Itu dicatat sebagai kekurangan, bukan sebagai kenetralan.

**CACAH TANGAN sah** (aturan 66), ref `3196fd98` / `8a614567`: `lux_ai/serapan/` **50**
(termasuk `__init__.py`; **49** tanpanya — keduanya sah asal disebut) · `tests/` **53** ·
`.github/workflows/` **44** · akar **18**. Angka **54** dan **45** tetap **TURUNAN** dan
**DILARANG dikutip terukur**.

**`karantina_semesta.py` (14.948 B, `46e7c46b…`) masih belum dibaca — versi keempat
berturut.** Selama itu, tabel dua belas karantina dan `sebaran_pelanggaran` 12/12
dikutip **tanpa aturan 86 (b) terpenuhi**, dan `cacah_daftar_terpotong` **0** tetap
**kesaksian laporan tentang dirinya sendiri**. Ia berada di **peringkat satu utang
bacaan**, dan ukurannya berada jauh di bawah setiap batas terukur § 3.2 — artinya
**tidak ada alasan teknis** ia belum dibaca, hanya alasan urutan kerja.

**Peringatan dini aturan 48** tidak berubah — dirujuk ke v19.

## KOREKSI — tidak ada yang baru di v21

Koreksi 1–17 dirujuk ke v19 dan v20. **Koreksi berikutnya tetap 18.** Nol koreksi baru
bukan tanda ketelitian; giliran ini tidak membuka bahan baru yang dapat menyalahkan
siapa pun. **DILARANG membaca nol koreksi sebagai mutu.**

## UTANG UKUR — daftar penuh

**HIDUP:** **6** · **7** · **17** (cacah total `baris_mati`, terpotong 54%) · **21** (5%
`semesta_rentang.json`) · **22** (penulis `semesta_rentang.json`; pembacanya kini bernama
`serap.py`, penulisnya tidak) · **26** (apakah pola BNXUSDT berlaku bagi **786 simbol
lain**) · **27** (apakah 16 uji termasuk 1377) · **30** (kelipatan hari penuh BNXUSDT) ·
**31 [BARU]** (empat klausa nol kejadian, ditetapkan dari kode).

**LUNAS:** 19, 25, 28, 29 (v20) dan yang lebih lama, dirujuk ke v18/v19.
**Utang ukur berikutnya: 32.**

**Utang verifikasi (penomoran terpisah, milik EKOR):** hidup **24, 45, 46, 47, 48, 49** —
dirujuk ke EKOR v21 blob `9bd48a49af9e95c47d273d396e2dfc6130e11503`.

## PRASYARAT KLASIFIKASI — LIMA BLOKIR, dan ONGKOSNYA KINI DITAKSIR

Serapan funding tetap **matang sebagai PEMBUKUAN, belum matang sebagai LANDASAN FITUR**.
Blokir keenam LUNAS di v20 (taksonomi lubang kini mekanisme sampai tingkat klausa).

Operator bertanya **berapa lama lagi**. Jawaban yang jujur menuntut memisahkan **apa yang
menghalangi** dari **berapa mahal menyingkirkannya**. Kolom ongkos di bawah adalah
**taksiran, bukan pengukuran**, dan ditandai demikian.

| # | blokir | keadaan | ongkos (TAKSIRAN) |
| --- | --- | --- | --- |
| 1 | **ADR-A003 belum ada** | tidak bergerak sejak v14 | **satu giliran**; murni tulisan, bahannya sudah di tangan |
| 2 | **786 simbol lain belum diperiksa** | menyempit, tidak lunas | **mahal**; bahannya `manifes_pecahan_*` yang **DI LUAR JANGKAUAN ALAT** |
| 3 | **`baris_mati` terpotong 54%** | tidak bergerak | **terhalang alat**, bukan terhalang waktu |
| 4 | **kelas positif 33 dari lima simbol** (KC-47) | tidak bergerak | terikat blokir 2 |
| 5 | **787 lawan 787** (KC-52 dipersempit, **0,127%**) | tidak bergerak | terikat blokir 2 |

> **PENGAMATAN YANG MENGIKAT, DAN INILAH JAWABAN SEBENARNYA.** Empat dari lima blokir
> (2, 3, 4, 5) bermuara pada **satu sebab tunggal**: bahan yang dibutuhkan berada di
> berkas yang **alat baca tidak sanggup ambil** — kedelapan `manifes_pecahan_*.json`
> (20.533.802 B) dan bagian `baris_mati` yang terpotong 54%. **Bukan waktu yang kurang;
> jangkauan alat yang kurang.** Menambah giliran tidak memindahkan satu pun dari keempat
> blokir itu selama jalur bacanya tetap sama.
>
> **Akibat langsung:** satu-satunya blokir yang dapat ditutup dengan kerja tulis murni
> adalah **blokir 1 (ADR-A003)**. Empat sisanya menunggu **jalan baca baru** — modul
> peringkas yang berjalan di CI dan menulis laporan kecil, atau pemecahan manifes menjadi
> potongan di bawah 110.662 B. **Selama jalan itu belum ada, klasifikasi TIDAK dapat
> dimulai atas dasar terukur, berapa pun giliran ditambahkan.**
>
> **DILARANG** menerjemahkan taksiran di atas menjadi tanggal. **DILARANG** menyatakan
> klasifikasi "tinggal sedikit lagi". **DILARANG** pula memakai kolom ongkos sebagai
> alasan melewati blokir mana pun — taksiran biaya bukan izin.

## Syarat praregistrasi R-321 — DELAPAN BELAS syarat kumulatif

Enam belas syarat v20 tetap berlaku (dirujuk ke blob v20), dengan **dua kenaikan derajat**
yang dicatat penuh di EKOR v21 dan **dua tambahan**. Yang menyentuh lampiran ini:

- **[16] Aturan 93 RESMI, rumusan kedua.** Ukuran tiap bahan wajib diperoleh lewat
  **daftar direktori** — `get_file_contents` atas sebuah **direktori** dengan `fields`
  memuat `name`, `size`, `sha` — **tidak pernah** lewat panggilan pengambil isi, dan
  dicatat di praregistrasi bersama nama dan blob. **DILARANG mengutip rumusan pertama.**
- **[18] Aturan 78 berlaku atas pemilihan bahan.** Bahan **≥ 2,25 MB dianggap tak
  terjangkau** sampai terbukti sebaliknya; bahan **ratusan KB** wajib diperlakukan
  **mungkin terpotong** sejak praregistrasi — dan menurut § 3.2 zona 194.728 B ..
  2.257.314 B **belum terukur sama sekali**, jadi perlakuan itu bukan kehati-hatian
  berlebih melainkan satu-satunya sikap yang jujur.

**Daftar bahan terlarang** (berkas yang sudah dibuka pada sesi ini) dirujuk ke EKOR v21;
termasuk `karantina_semesta.json` (dibuka melanggar aturan 21 — **tidak dapat ditawar**)
dan **`STATE.md` v43**.

**Poros yang disarankan bagi R-321: utang ukur 30** — mengapa BNXUSDT 2022-06 (1.440
menit = tepat 1 hari) dan 2022-08 (4.320 = tepat 3 hari) kehilangan hari bulat penuh
sementara 2022-04 (1.650) tidak. **Bahan wajib berkas yang belum pernah dibuka**, dan
calon terkuatnya adalah **`karantina_semesta.py`** (14.948 B) — jauh di bawah setiap
batas terukur, sekaligus membayar aturan 86 (b) yang menggantung empat versi.

## Penomoran berikutnya

jurnal **158** · STATE **v64** · EKOR **v22** · UKUR **v22** · PROMPT **v55 (belum
didorong, umur TIGA BELAS versi)** · ADR **A024 (belum terikat butir apa pun; A003 masih
BELUM ADA)** · KC **KC-60** (usulan hidup **KC-58 saja**; KC-56, KC-57, KC-59 DIBUANG;
KC-16 kosong selamanya) · aturan **94** (**resmi 1–81, 83–93**; 82 dicadangkan; **nol
usulan tersisa**) · hipotesis **H-A024** · ramalan **R-321** · **papan skor 339 — SAH,
tidak disentuh berkas ini** · aturan 52 berikutnya **ke-51** (ke-50 = pembacaan ulang
berkas ini) · aturan 38 berikutnya **ke-73** · kesalahan dokumen berikutnya butir **22** ·
koreksi UKUR berikutnya **18** · utang ukur berikutnya **32** · utang verifikasi
berikutnya **50** · berhenti eksplisit berikutnya **ke-58**.

— akhir `STATE_LAMPIRAN_UKUR.md` v21 —
