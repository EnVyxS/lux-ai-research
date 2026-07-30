# STATE lampiran EKOR — bagian 2 dari STATE (v12, milik STATE v52)

**Mengapa berkas ini ada.** Dua push `STATE.md` berturut terpotong (v41, v42);
pemecahan ke tiga berkas berlaku sejak v43 (KC-42). Pembagian yang berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, 83, 84, dan **85**; KC-1..**KC-51**.
2. **`STATE_LAMPIRAN_EKOR.md`** (berkas ini, v12) — bagian 2: papan skor, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** — bagian 3: pengukuran, modul, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) dan **`PROMPT_KELANJUTAN.md`**
   (blob `35beed44`) — **arsip; BUKAN sumber** (ADR-A018 kep. 9).

Dasar v12: EKOR v11 (blob **`3d72a9e7aeb5123401065b225168c485d3e37963`**), **dibaca
UTUH pada giliran yang sama sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43).

## KESERASIAN VERSI — dibaca apa adanya, termasuk yang belum serasi

Saat berkas ini didorong:

- `STATE.md` **v52** — blob **`635c24952637449d294a0f8035c8ed7e2f4932e4`**, commit
  **`28afc9ae075befe1bc3c1ed474f42d7dae95626e`**, dibaca ulang UTUH sesudah push.
  **SERASI** dengan berkas ini.
- `STATE_LAMPIRAN_EKOR.md` **v12** — berkas ini.
- `STATE_LAMPIRAN_UKUR.md` masih **v11** — blob
  **`7f0221bfb548d04f464a5b8c67f0579214f97b54`**, commit `f9c5d960`.
  **ISINYA SERASI, NOMORNYA TERTINGGAL.** UKUR v11 sudah memuat API `sisa_defisit` V1,
  114 baris berdefisit, H-A021, aturan 85, dan cacah tangan 49/53/44/18. **Utang UKUR
  v12 hanyalah DUA SALAH KETIK** (lihat tabel di bawah), bukan angka yang hilang.
  **Tidak ada peringatan "USANG SEBAGIAN" yang berlaku terhadap UKUR v11.**

Peringatan keserasian EKOR v11 — bahwa UKUR v10 usang sebagian dan bahwa sumber sah
R-311 adalah jurnal 135 — **GUGUR SELURUHNYA**: UKUR v11 sudah naik dan memuatnya.
Jurnal 135 tetap sah sebagai jejak, bukan lagi sebagai satu-satunya sumber.

**Satu berkas per push tetap MENGIKAT** (KC-42, KC-43).

## SALAH KETIK DOKUMEN SENDIRI — buku besar yang diwarisi dan diperpanjang

Daftar ini disalin dari STATE v52 dan **diperpanjang satu baris**. Sebab tetap sama
setiap kali: `push_files` menulis ulang SELURUH berkas, sehingga memperbaiki satu
karakter berarti menyusun ulang berkas besar dari konteks terpakai — persis yang
dicatat KC-42 sebagai cara paling pasti merusak berkas. Perbaikan karena itu selalu
menumpang pada penulisan ulang yang memang sudah dijadwalkan.

| # | berkas | tertulis | seharusnya | status |
| --- | --- | --- | --- | --- |
| 1 | jurnal 132 §3 | "beruntun 2/1" | 2/2 | dikoreksi di STATE v50 |
| 2 | EKOR v10 | `terisi ≉49,7%` | `≈49,7%` | dikoreksi di EKOR v11 |
| 3 | jurnal 135 §13.3 | "hendan dirumuskan" | "hendak" | dikoreksi di STATE v51 |
| 4 | EKOR v11 kepala | "ramalan deretministik" | "deterministik" | **LUNAS DI BERKAS INI** |
| 5 | UKUR v11 kepala | "KESERAIAN VERSI" | "KESERASIAN VERSI" | **utang UKUR v12** |
| 6 | UKUR v11 daftar uji | penanda `**` tak berpasangan pada baris `test_bentangan_kohort.py` | penanda berpasangan | **utang UKUR v12** |
| 7 | **STATE v52** | kepala tabel salah ketik berbunyi **"Empat salah ketik"** padahal tabelnya memuat **enam** baris, dan paragraf di bawahnya sudah menyebut "keenam" | "Enam salah ketik" | **utang STATE v53** |

**Bila berkas sumber dan tabel ini bertentangan pada titik-titik itu, tabel ini
menang** — pengecualian tersurat atas KC-41, HANYA untuk salah ketik yang sudah
diakui, tidak pernah untuk angka terukur.

**Pembacaan yang jujur, dan kali ini lebih keras daripada di STATE v52:** cacat nomor 7
lahir **di dalam berkas yang memperingatkan pola itu sendiri**, dan lolos meskipun
STATE v52 dibaca ulang UTUH sesudah push. Dengan itu **empat berkas berturut** (EKOR
v11, UKUR v11 dua kali, STATE v52) memuat salah ketik milik kami sendiri. Baca ini
sebagai **tanda ketelitian menurun pada giliran panjang** — peringatan operasional,
bukan kelas cacat ilmiah, dan bukan kebetulan.

## KC-43..KC-51 (teks lengkap KC-43..KC-47 di STATE v47, KC-49 di v48, KC-50 di v50, **KC-51 di v52**)

- **KC-43** — tanda tangan fungsi dari INGATAN. Penangkal: baca modul yang diimpor
  UTUH pada giliran yang sama.
- **KC-44** — semua laporan di-commit satu langkah. Penangkal: commit tiap berkas
  laporan sendiri-sendiri.
- **KC-45 [RESMI v45]** — satuan "bulan tanpa funding" vs "bulan MATI" dicampur.
- **KC-46 [RESMI v45]** — lubang bentuk AWAL dibaca sebagai "funding berhenti".
- **KC-47 [RESMI v46]** — satu peristiwa menyamar sebagai banyak pengamatan bebas
  (39 dari 40 `mati_dulu` berbagi tebing `2025-07`). Penangkal: aturan 81, ADR-A013.
  Kasus kuat v10: dari sembilan baris MATI tak penuh R-310, **TUJUH** berbulan
  `2024-05` dengan `cacah_lilin` 39.308–39.317 — jendela **9 lilin**. Numerator 9
  karena itu BUKAN sembilan pengamatan bebas; paling banter **tiga**.
  **Diperiksa untuk R-311 dan TIDAK terpicu** (ADR-A018 kep. 4): sepuluh baris
  berdefisit teratas tersebar di tujuh bulan berbeda; kelompok terbesar satu bulan
  hanya dua baris.
- **KC-48 [RESMI v7]** — ambang absolut pada besaran yang sebarannya belum pernah
  diukur. Penangkal: usulan aturan 82.
- **KC-49 [RESMI v8 lampiran ini]** — pita dikunci tanpa menghitung implikasi
  aritmetis momen yang sudah terukur. Penangkalnya BERLAKU sebagai aturan 83.
- **KC-50 [RESMI di STATE v50]** — agregat semesta dihitung lewat jalan memutar
  alih-alih LANGSUNG dari baris, sehingga selisih terhadap sumber lain mustahil
  terlihat. Dua kasus: `total_byte` `irisan_byte`, dan **839.842.134 dipakai seolah
  jumlah lilin** sampai `keterisian_lilin` V1 menghitung langsung **839.325.999** —
  **selisih 516.135**. **Cacat kelas ini tidak menghasilkan galat; ia menghasilkan
  kesunyian.** Menggigit lagi di R-311: penutupan sisa 712.925 adalah TAUTOLOGI dari
  808.162 − 95.237.
- **KC-51 — [v12] KINI RESMI** (diresmikan ADR-A018 kep. 1, teks penuh di STATE v52).
  **Bias taksiran pemusatan:** besaran yang belum pernah diukur sebarannya secara
  sistematis ditaksir **lebih menyebar** daripada kenyataannya, sehingga tepi pita di
  sisi "terpusat" jatuh terlalu jauh dari lantai aritmetis. **Empat kejadian berturut
  tanpa satu pun pembalikan arah:** R-308 butir 2 (pita 10..300 → **2**); R-310 butir 2
  (taksir 0,073 pita 0,02..0,25 → **0,0445**); R-311 butir 1 (taksir 3.000 pita
  200..12.000 → **114**, faktor **26,3**); R-311 butir 2 (taksir 0,15 pita 0,02..0,45 →
  **0,4087**, **+172%**). **Yang DILARANG:** membaca kemenangan R-311 butir 2 — atau
  kemenangan tipis mana pun yang menempel tepi — sebagai bukti kalibrasi membaik.
  **Penangkalnya adalah aturan 85**, RESMI di STATE v52, berlaku mulai **R-312**,
  **tidak berlaku surut**; **R-311 TIDAK diadjudikasi ulang** (aturan 29).
- **KC berikutnya yang bebas: KC-52.**

## Papan skor prediksi — lengkap R-300..R-311 (R-199..R-299 di v4, blob `67dda29e`)

| # | Prediksi | Status |
|---|---|---|
| R-300 | (1) cacah_bulan 64; (2) tetangga BTCST HIDUP; (3) cacah_hidup 8..30 dan MATI>HIDUP | **SEPARUH** |
| R-301 | (1) tebing==0; (2) mati_tersisip ≥1; (3) bangkit==0 | **TIDAK TERADJUDIKASI** |
| R-302 | (1) simbol tersisip 1..10; (2) simbol-bulan 1..50; (3) penyebut 19.586/787 | **SEPARUH** (butir 2 MELESET 88>50) |
| R-303 | (1) simbol tersisip 1..60; (2) simbol-bulan 1..300; (3) penyebut/kendali/kode 0 | **TEPAT (3/3)** |
| R-304 | (1) mati_dulu 5..8; (2) hidup_berlubang 3..8; (3) penyebut/kendali/kode 0 | **MELESET** (1 dan 2 kalah) |
| R-305 | (1) bagian mati-tak-setelah-lubang dari ≥100 dalam 0.55..0.95; (2) cacah lubang-awal 20..120; (3) invarian + kendali + kode 0 + CI | **MELESET** — butir 1 KALAH (penyebut 118, bagian **1.0**, tautologis aturan 10); butir 2 KALAH (**5** < 20); butir 3 TEPAT (MUDAH) |
| R-306 | (1) bagian arah STRIKT dari penyebut ≥100 dalam 0.25..0.60; (2) cacah tebing 2025-07 dalam 20..90; (3) sembilan invarian + dua kendali + kode 0 + CI | **TEPAT (3/3)** — butir 1 **0.339** (penyebut **118**); butir 2 **39**; butir 3 MENANG (MUDAH) |
| R-307 | (1) bagian byte MATI atas total byte 19.586 dalam 0.02..0.15; (2) cacah simbol-bulan ber-`byte_parquet` < 10.000 dalam 20..400; (3) sembilan invarian nol + dua kendali + kode 0 + CI | **MELESET** — butir 1 KALAH (**0.017704**, tipis di bawah pita); butir 2 KALAH (**0**, ambang MUSTAHIL, KC-48); butir 3 MENANG (MUDAH) |
| R-308 | (1) cacah HIDUP ber-byte < 97.634 dari 18.087 dalam **20..600**; (2) cacah MATI ber-byte < 150.000 dari 1.401 dalam **10..300**; (3) sembilan invarian nol + dua kendali sah + kode 0 + CI | **SEPARUH** — butir 1 **MENANG** (**38**); butir 2 **KALAH** (**2**, KC-49, kini juga kasus pertama KC-51); butir 3 **MENANG** (MUDAH) |
| R-309 | (1) cacah baris HIDUP-kecil yang bulan PERTAMA simbol ATAU bulan tepi `2026-06`, dari 38, dalam **22..38**; (2) nisbah rata byte bulan-pertama atas bukan-pertama dalam **0.10..0.60**; (3) delapan selisih invarian nol + dua kendali sah + kode 0 + CI | **TEPAT (3/3)** — butir 1 **37** (0,973684); butir 2 **0,527179**; butir 3 MENANG (MUDAH) |
| R-310 | (1) cacah baris MATI ber-`cacah_lilin` kurang dari lilin penuh bulannya, dari 1.401, dalam **1..120**; (2) bagian defisit lilin yang ditanggung baris bukan-pertama dalam **0.02..0.25**; (3) delapan selisih invarian nol + tiga kendali sah + lima penggugur bersih + kode 0 + CI | **TEPAT** — butir 1 **MENANG** (**9** dari 1.401, tipis ke tepi BAWAH); butir 2 **MENANG** (**0,0445**, tipis ke tepi BAWAH); butir 3 **MENANG** (MUDAH) |
| R-311 | (1) cacah baris bukan-pertama bukan-MATI yang berdefisit lilin, dari **17.398** calon, dalam **200 .. 12.000**; (2) bagian sisa 712.925 yang ditanggung SEPULUH baris berdefisit teratas, dalam **0,02 .. 0,45**; (3) sepuluh selisih invarian nol + kendali data sah + kendali negatif + kendali nol + penggugur bersih + kode 0 + CI | **SEPARUH** — butir 1 **KALAH** (**114**, jauh di bawah tepi bawah 200; lantai aritmetis 16); butir 2 **MENANG** (**0,4087**, tipis ke tepi ATAS, sisa 0,0413); butir 3 **MENANG** (MUDAH) |

**Total R-1..R-311** (dihitung tangan, aturan 21). Dasar v10 (papan skor R-1..R-310):
TEPAT 217 · MELESET 57 · SEPARUH 21 · TIDAK TERADJUDIKASI 8 · MENUNGGU 7 = 310.
Sesudah v10: **R-311 SEPARUH**.

- TEPAT **217**
- MELESET **57**
- SEPARUH 21 + 1 = **22**
- TIDAK TERADJUDIKASI **8**
- MENUNGGU **7** (R-7, R-19, R-20, R-28, R-36, R-37, R-199)

217 + 57 = 274; 274 + 22 = 296; 296 + 8 = 304; 304 + 7 = **311** ✅ Nomor terpakai
R-1..R-311, seluruhnya teradjudikasi atau menunggu. N_percobaan = 0.
**ADJUDIKASI RISET TETAP TERKUNCI.**

**[v12] Tidak ada ramalan yang diadjudikasi sejak v11.** Giliran-giliran sesudahnya
adalah giliran DOKUMEN (ADR-A018, UKUR v11, STATE v52, berkas ini), bukan giliran
ukur. Papan skor karena itu **tidak bergerak, dan ketidakbergerakannya disengaja**;
ia DIBACA dari v11, tidak dikarang. Ramalan berikutnya **R-312**, poros sudah
ditetapkan ADR-A018 kep. 12 tetapi **pitanya belum boleh dikunci di sini** (aturan 79).

**Nisbah papan skor, dihitung tangan dan disebut apa adanya:** dari 296 ramalan yang
sudah beradjudikasi penuh (217 + 57 + 22), TEPAT **73,3%**, MELESET **19,3%**, SEPARUH
**7,4%**. Angka itu **DILARANG dibaca sebagai mutu ramalan**: sebagian besar butir
ketiga tiap ramalan berlabel MUDAH dan tidak berisiko.

**Utang papan skor:** rincian R-236..R-247 masih di jurnal 92–94; R-229 TEPAT dan
R-230 MELESET (dari docstring) menunggu pemeriksaan R-224..R-235.

## Catatan kejujuran [v12]

Giliran ini **tidak menghasilkan satu pun pengukuran baru**. Yang bertambah hanyalah
ketertiban dokumen. Itu disebut lebih dulu agar tidak ada kalimat di bawah yang
terbaca seolah kemajuan riset.

1. **Ramalan CI untuk push STATE v52 TERUKUR dan TEPAT.** `ci.yml` menyala pada commit
   `28afc9ae` dan menulis `reports/ci_terakhir.json` blob
   **`2c3290cb23097ab93f196f79e61c751221fe4b4d`**: run **30548418622**,
   2026-07-30T13:46:02Z, `kode_keluar` **0**, **1341 butir**
   (`1341 tests collected in 0.60s`). Tetap **MUDAH**, tetap TIDAK diskor, tetap TIDAK
   menambah beruntun aturan 57.
2. **SATU RAMALAN HILANG SEBELUM SEMPAT DIBACA — dilaporkan telanjang.** Push UKUR v11
   (commit `f9c5d960`) juga menyalakan `ci.yml`: run **30547842823**, commit bot
   **`de2fc03d6c7afe5a2d5b19379f722a2d96ea6576`**, 13:38:51Z. Laporannya **TIDAK
   pernah dibaca** dan sudah **DITIMPA** oleh run 30548418622. Angkanya tidak dapat
   dipulihkan dengan alat yang ada. Ramalan "CI tetap 1341" untuk push itu karena itu
   **TIDAK TERUKUR — bukan menang, bukan kalah.** Ini persis batas yang dirumuskan
   ADR-A018 kep. 7: ramalan semacam itu terukur **hanya bila laporannya dibaca sebelum
   run berikutnya menimpanya**. Dua push dokumen berturut dalam satu giliran cukup
   untuk menghanguskan yang pertama.
3. **Konsekuensi prosedural yang diakui, belum diusulkan sebagai aturan.** Bila dua
   berkas akar didorong berturut tanpa membaca laporan di antaranya, yang pertama
   pasti hangus. Ini **belum** diangkat menjadi aturan bernomor karena baru **satu**
   kejadian terukur; mengangkatnya sekarang berarti mengulang KC-48 dalam bentuk lain,
   yaitu menetapkan aturan dari satu pengamatan. Dicatat sebagai **calon**, menunggu
   kejadian kedua.
4. **KC-51 dan aturan 85 kini RESMI**, keduanya lewat ADR-A018, dan keduanya lahir
   dari **kekalahan** R-311 butir 1, bukan dari kemenangan butir 2. Perlu diulang
   karena godaannya kuat: pada giliran yang sama papan skor bertambah satu SEPARUH,
   dan itu bisa terbaca seolah hasil yang lumayan. **Yang sebenarnya terjadi: taksiran
   meleset 26,3 kali dan kelas cacatnya baru sekarang dinamai, sesudah empat kejadian
   berturut ke arah yang sama.**
5. **Aturan 83 ditaati penuh di R-311 dan tetap kalah.** Lantai aritmetis **16**
   dihitung sendiri di jurnal 134, rentang implikasi (16 .. 18.790) benar, dan tepi
   bawah tetap diletakkan di **200** — dua belas setengah kali di atas lantai — tanpa
   satu kalimat pun yang membenarkannya. Aturan yang ditaati tetapi tidak mengikat
   keputusan **bukan aturan yang bekerja**; itulah lubang yang ditutup aturan 85.
6. **Tiga berkas akar terakhir dibaca UTUH**, sehingga daftar "belum pernah diperiksa"
   kini **5 dari 5 LUNAS**. Yang paling penting bukan isinya melainkan pertentangannya:
   **`PROMPT_KELANJUTAN.md` memerintahkan "jangan berhenti dengan alasan konteks
   Notion"**, berlawanan langsung dengan perintah operator yang berlaku. Berkas usang
   itu kini **ARSIP — BUKAN SUMBER** (ADR-A018 kep. 9). **Perintah yang berlaku menang
   atas berkas yang tertinggal enam versi.**
7. **Utang baca `tests/test_bentangan_kohort.py` V2 LUNAS** sesudah **sembilan versi**
   menunggu: blob **`9f850ecdb25466d38c839004b36ff221db2cf7f8`** (13.154 B), dicacah
   TANGAN bernomor `test_01`..`test_63` tanpa lompatan = **63** butir; helper `peta`,
   `baris_uji`, `laporan_bersih` tidak berawalan `test_`.
8. **Larangan baru yang lahir dari kecelakaan yang nyaris terjadi:** `PETA_MODUL_BERKAS.md`
   mencatat **34** berkas uji milik repo **WARISAN `bot_v8`**, sedangkan repo riset ini
   punya **53**. Keduanya benar untuk repo masing-masing, dan selisihnya sempat tampak
   seperti pelanggaran aturan 66. **Menyebut "cacah uji" tanpa menyebut repo-nya kini
   DILARANG** (ADR-A018 kep. 10).
9. **Pemeriksaan silang yang menutup tanpa sisa** (terbitan, TIDAK diskor, diwarisi
   v11): 18.799 − 1.401 = **17.398**; 18.087 − 17.318 = **769**; 98 − 80 = **18**;
   769 + 18 = **787** = `cacah_simbol`.
10. **Aturan 57 beruntun 3 dari 3, tidak bertambah.** Tidak ada push yang menyentuh
    `tests/**` sejak v11, jadi beruntun **tidak bertambah dan tidak putus**.
11. **Empat berkas berturut memuat salah ketik milik kami sendiri** — lihat tabel di
    atas, termasuk cacat nomor 7 yang lahir di dalam berkas yang memperingatkan pola
    itu. Tidak ada pembelaan yang diajukan untuk itu.

**Kesalahan proses giliran ini:** tidak ada kegagalan konektor — seluruh `push_files`,
`get_file_contents`, dan `list_commits` berhasil sekali jalan, tidak ada pemotongan
terdeteksi. Satu kerugian nyata tetap terjadi tanpa kegagalan alat apa pun: laporan CI
run 30547842823 hangus karena urutan kerja, bukan karena galat (butir 2 di atas).

## Jumlah uji

**1341 TERUKUR, tiga bacaan berjejak sejauh ini pada rangkaian giliran ini.**

1. blob **`2d32f814e5e426e1411559810b55b9f20176a22d`**: run **30542217837**, commit
   **`b1c7941db3e08ae8a6f06864d7f47a571abf5669`** (trio `sisa_defisit`),
   2026-07-30T12:22:10Z, kode 0, **1341** (`1341 tests collected in 0.62s`).
2. blob **`bce1177ea21d7a4e01b59b2d4f4277a8584b4eed`**: run **30545364506**, commit
   **`8c30de51cc4d0098d4bd2922966684591bd7ce96`** (push STATE v51),
   2026-07-30T13:05:55Z, kode 0, **1341** (`1341 tests collected in 0.45s`).
3. **[v12]** blob **`2c3290cb23097ab93f196f79e61c751221fe4b4d`**: run **30548418622**,
   commit **`28afc9ae075befe1bc3c1ed474f42d7dae95626e`** (push STATE v52),
   2026-07-30T13:46:02Z, kode 0, **1341** (`1341 tests collected in 0.60s`).

Turunan: 1297 + **44** butir `tests/test_sisa_defisit.py` = **1341** ✅ (aturan 21).

Riwayat panjang: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 →
984 → 1044 → 1100 → 1168 → 1233 → 1297 → **1341**.

Cacah per berkas uji (yang diketahui, **milik repo riset ini — bukan repo warisan**):
`test_irisan_byte.py` **68** · `test_bulan_pertama.py` **65** ·
`test_keterisian_lilin.py` **64** · `test_bentangan_kohort.py` V2 **63** (dicacah
TANGAN, `test_01`..`test_63`) · `test_lubang_tebing.py` **60** ·
`test_sebab_bangkit.py` **57** · `test_byte_semesta.py` **56** ·
`test_lubang_awal.py` **48** · `test_tersisip_semesta.py` **47** ·
`test_anatomi_tengah.py` **47** · `test_sisa_defisit.py` **44** (dicacah TANGAN,
`test_01`..`test_44`) · `test_terhenti.py` V4 **33** · `test_bulan_absen.py` **32** ·
`test_karantina_semesta.py` **28** · `test_silang_settled.py` **24**.

**Aturan 57: beruntun 3 dari 3** sesudah putus di 26/27. Hanya push yang menyentuh
`tests/**` yang dihitung.

### ORDINAL ATURAN 38 — buku besar, kini sampai ke-41

**Definisi yang berlaku (ADR-A018 kep. 8), ditulis tersurat agar dapat diperiksa:**
pemakaian aturan 38 dihitung **hanya** untuk pembacaan `reports/ci_terakhir.json` yang
meninggalkan **jejak tertulis** berupa nomor run + commit + blob di STATE, lampiran,
atau jurnal. Pembacaan tanpa jejak tidak pernah masuk buku besar dan karena itu tidak
dapat, dan tidak boleh, dihitung.

| ke- | CI | run | commit | blob | jejak |
|---|---|---|---|---|---|
| 36 | 1233 | 30533500210 | `f8098980` | `016fb234` | STATE v50 |
| 37 | 1297 | 30535202643 | `924b0d7a` | `3c07c909` | STATE v50, EKOR v10 |
| 38 | 1297 | 30541051907 | `5d7d8b96` | — | jurnal 135 (blob tidak dicatat di sana) |
| 39 | 1341 | 30542217837 | `b1c7941d` | `2d32f814` | jurnal 135, STATE v51 |
| 40 | 1341 | 30545364506 | `8c30de51` | `bce1177e` | EKOR v11, STATE v52 |
| **41** | **1341** | **30548418622** | **`28afc9ae`** | **`2c3290cb`** | **berkas ini** |

**Pemakaian berjalan = ke-empat puluh satu.** Dua cacat tetap disebut apa adanya, bukan
dihaluskan:

- Baris ke-**38** **tidak memuat blob** — diwarisi jurnal 135, blobnya tertimpa dan
  tidak dapat dipulihkan. Ordinal ini karena itu sah **relatif terhadap definisi di
  atas**, bukan sebagai pencacahan mutlak.
- Run **30547842823** (commit bot `de2fc03d`, atas push UKUR v11) **tidak pernah
  dibaca** dan **tidak masuk buku besar** — bukan karena diabaikan, melainkan karena
  sudah tertimpa saat hendak dibaca. Ia **DILARANG dihitung** sebagai pemakaian, dan
  ramalannya DILARANG diklaim menang.

Bila kemudian ditemukan jejak pembacaan lain di jurnal 133–134, nomor ini **WAJIB
dikoreksi, bukan dipertahankan**.

## Utang verifikasi

1-5, 11 menunggu tahap juri. 6-23, 25-29, **31** LUNAS. **Nomor utang BUKAN nomor
ramalan — KC-32.**

24. **AKTIF, tetapi jauh lebih pendek.** **LUNAS BARU [v12]:**
    - **`tests/test_bentangan_kohort.py` V2 dibaca UTUH** (`9f850ecd`, 13.154 B, 63
      butir dicacah tangan) — sembilan versi menunggu, kini NOL.
    - **`PETA_MODUL.md`** (`9ee33a99`), **`PETA_MODUL_BERKAS.md`** (`3abe95f6`),
      **`PROMPT_KELANJUTAN.md`** (`35beed44`) dibaca UTUH untuk PERTAMA kalinya →
      daftar berkas akar **5 dari 5 LUNAS**.
    - `decisions/ADR-A018.md` (`3fba599e`), `STATE_LAMPIRAN_UKUR.md` v10 (`162c1305`)
      dan v11 (`7f0221bf`), `STATE.md` v51 (`412a5b2d`) dan v52 (`635c2495`), serta
      EKOR v11 (`3d72a9e7`) dibaca UTUH sesudah masing-masing push.
    - `reports/ci_terakhir.json` (`2c3290cb`) dibaca utuh dan blobnya DICATAT.
    **TETAP BELUM:** `decisions/ADR-A002`, **A004**, **A006**, **A007**, **A008**;
    `.github/workflows/karantina_semesta.yml` (`de40fa4e`); `tests/test_pulihkan.py`
    (`11c43533`); `tests/test_rilis_karantina.py` (`739c8da9`);
    `tests/test_karantina_a006.py` (`a5a3d82f`).
30. **AKTIF — cacah tangan pada ref sesudah trio BERIKUTNYA.** Begitu modul ukur baru
    didorong, angka 50 / 54 / 45 menjadi TURUNAN dan **DILARANG dikutip sebagai
    terukur** sampai dicacah satu per satu bernomor (aturan 66, KC-33). Yang sah
    sekarang: **49 / 53 / 44 / 18** pada ref `3196fd98`.
31. **LUNAS [v12]** — UKUR v11 sudah naik (`7f0221bf`).
32. **BARU [v12] — tiga butir "memerlukan verifikasi" `PETA_MODUL.md`** (repo
    **WARISAN**, ADR-A018 kep. 10), didaftarkan sebagai **utang terbuka, bukan fakta**:
    (a) atribut `enable_hs` tidak ditemukan di `config.py` padahal dipakai
    `strategy.py`; (b) klaim "30 pair dipilih alfabetis" tanpa bukti; (c) klaim
    "kendala mengikat = kapasitas margin" yang belum diuji angkanya.
33. **BARU [v12] — salah ketik yang belum diperbaiki di sumbernya:** dua di UKUR v11
    (utang **UKUR v12**) dan satu di STATE v52 (utang **STATE v53**). Lihat tabel
    salah ketik di kepala berkas ini.
34. **BARU [v12] — `PROMPT_KELANJUTAN.md` belum diberi kepala "ARSIP — BUKAN SUMBER"**
    di dalam berkasnya sendiri, dan **`PROMPT.md` v55 belum didorong**. Sampai itu
    dikerjakan, satu-satunya penjaga adalah larangan tertulis di STATE v52 dan di
    berkas ini.

## Daftar ADR

- **ADR-A001** aturan dasar. DITERIMA.
- **ADR-A002** serapan. Kondisi v3 berlaku; §10 tetap tidak boleh diubah.
- **ADR-A003** taksonomi rezim. BELUM ADA. Wajib memuat delapan simbol bangkit,
  koreksi ADR-A011/A012/A013/A014/A015/A016/A017/**A018**, bentangan LITUSDT, bulan
  ABSEN, aturan 76, KC-40.
- **ADR-A004** kebijakan KC-6. DITERIMA.
- **ADR-A005** jenis instrumen. DITERIMA.
- **ADR-A006** karantina + persistensi. DITERIMA, TERVERIFIKASI.
- **ADR-A007** serapan hibrida. DIUSULKAN, belum diterima.
- **ADR-A008** akibat KC-18. Keputusan 1–6 DITERIMA. **Keputusan 7 DITANGGUHKAN.**
  Prasyarat tersisa: bentangan kehidupan 38 kohort puncak.
- **ADR-A009** (commit `17a594b6`). **DICABUT PENUH oleh ADR-A012.**
- **ADR-A010** (commit `c4bccf21`) — klaim "kebangkitan tunggal" DICABUT. DITERIMA.
- **ADR-A011** (commit `645fd5df`) — arah sebab A009 dicabut untuk kelas bangkit.
  DITERIMA.
- **ADR-A012** (commit `f9f564d1`) — arah sebab A009 dicabut untuk SELURUH semesta;
  butir 1 R-305 (1.0) ARTEFAK TAUTOLOGIS. DITERIMA.
- **ADR-A013** (commit `8ba4f989`) — klaim arah waktu wajib dipilah tebing lawan
  bukan-tebing. Lima keputusan; (2) dan (4) kini aturan **80** dan **81**. DITERIMA.
- **ADR-A014** (commit `69bfdd5d`, blob `6d77c2cd`) — byte parquet: arah H-A018
  didukung, pita gugur, "kecil" BUKAN penanda mati. Enam keputusan; (5) melahirkan
  KC-48 dan usulan aturan 82. DITERIMA.
- **ADR-A015** (commit `982c2536`, blob `387d5510`) — pita praregistrasi wajib melewati
  aritmetika implikasi. Delapan keputusan: (1) KC-49 resmi; (2) aturan 83 diusulkan —
  DIRESMIKAN di STATE v49; (3) usulan aturan 82 diperluas; (4) R-308 SEPARUH;
  (5) besar berkas bukan detektor status ke arah mana pun — **TIDAK dibalik oleh R-310,
  R-311, maupun ADR-A018**; (6) H-A019 didaftarkan; (7) cacah invarian wajib menyebut
  mana yang bebas — kini KC-50 resmi; (8) aturan 57 dicatat PUTUS 26/27 — kini beruntun
  3/3. **DITERIMA.**
- **ADR-A016** (commit `8fad9091`, blob `209802d7`) — H-A019 diterima TERBATAS sebagai
  irisan asimetris, bukan sebab. Delapan keputusan: (1) rumusan resmi satu-satunya;
  (2) klausa `2026-06` DICABUT; (3) usulan aturan 84 — DIRESMIKAN di STATE v50;
  (4) koreksi jurnal 129, hanya TLMUSDT 2023-03 yang melawan — **DIKOREKSI oleh
  ADR-A018 kep. 6**; (5) `total_byte` wajib jalur langsung — kini KC-50 resmi;
  (6) batas tafsir "bulan pertama" = di dalam penyebut 19.586; (7) prioritas riset ke
  isi bulan MATI — DIJAWAB R-310; (8) cacah tangan 47/51/42 pada ref `010edff2`.
  **DITERIMA.**
- **ADR-A017** (blob `1be570f29e95227393dfb0989354cbbb5024b46c`) — **DITERIMA**.
  Sebelas keputusan: (1) rumusan resmi temuan R-310; (2) larangan menyimpulkan apa pun
  tentang harga; (3) KC-50 diresmikan; (4) koreksi resmi 839.842.134 lawan 839.325.999,
  selisih **516.135**; (5) aturan 84 diresmikan; (6) numerator 9 bukan sembilan
  pengamatan bebas; (7) H-A020 diusulkan + larangan menulis "delisting 28 Mei 2024";
  (8) A015 kep. 5 TIDAK dibalik; (9) H-A019 dikuatkan lewat jalur ukur kedua, TLMUSDT
  2023-03 tetap melawan; (10) pertanyaan terbuka berpindah ke sisa 712.925 — DIJAWAB
  sebagian oleh R-311; (11) cacah tangan 48/52/43 pada ref `5d7d8b96`.
- **ADR-A018 [BARU v12]** (commit **`2ac752b55b228e3b3f8b2428a16cd07c67f513dd`**, blob
  **`3fba599e6498b921e2a5babb915e247a3b1ecac4`**) — **DITERIMA**, ditulis ke
  `decisions/**` (paths-ignore, CI tidak menyala), dibaca ulang UTUH sesudah push.
  **Dua belas keputusan:** (1) **KC-51 DIRESMIKAN** dengan tabel empat bukti;
  (2) **aturan 85 DIRUMUSKAN dan BERLAKU** mulai R-312, tidak berlaku surut, dengan
  pengakuan bahwa aturan 83 ditaati penuh dan tetap kalah; (3) rumusan resmi temuan
  R-311 + empat larangan yang menyertainya; (4) aturan 81 diperiksa untuk R-311 dan
  **TIDAK terpicu** (sepuluh teratas di tujuh bulan, kelompok terbesar dua);
  (5) **H-A021 DIUSULKAN**, kalimat sebab untuk gugus `2022-05` DILARANG, dan bila
  kelak diterima `bagian_teratas` **tidak berubah** karena dihitung atas lilin;
  (6) ADR-A016 kep. 4 **DIKOREKSI** — TLMUSDT 2023-03 kini terukur 95,2% kosong dan
  berstatus HIDUP, sehingga tafsir "byte kecil = bulan tepi" **MELEMAH tanpa
  pengganti**; (7) koreksi STATE v51 soal aturan 38; (8) ordinal ke-40 diterima dengan
  cacat baris ke-38 disebut; (9) **`PROMPT_KELANJUTAN.md` ARSIP — BUKAN SUMBER**;
  (10) dua cacah `tests/` (34 warisan lawan 53 riset) DILARANG dicampur, dan tiga butir
  `PETA_MODUL.md` didaftarkan sebagai utang; (11) cacah tangan **49/53/44/18** dicatat
  resmi pada ref `3196fd98`; (12) poros R-312 ditetapkan, praregistrasinya DILARANG
  ditulis di ADR (aturan 79).
- **ADR berikutnya A019** — calon isinya: adjudikasi **R-312**, status **H-A020** dan
  **H-A021** sesudah uji lubang tengah, dan pemeriksaan pertama apakah **aturan 85**
  benar-benar mengubah letak tepi pita. **DILARANG disusun pada giliran yang sama
  dengan adjudikasi** (ADR-A016).

## Temuan sampingan

**[v11, tetap berlaku] `sisa_defisit` V1** (run modul 30542217951 pada commit
`b1c7941d`, kode 0; laporan ringkas blob `91a05c05`, status blob `1c9c2c5f`; sidik kode
`6211624ba9514d604d4dc510abca2e40386775c7aaa1279135f0baf666f044b0`):

- **Penyebut kerja `cacah_calon` = 17.398** baris bukan-pertama dan bukan-MATI
  (HIDUP 17.318 + SEPI 80). Terbitan yang menutup: 18.799 − 1.401 = 17.398.
- **`cacah_berdefisit` = 114** (HIDUP 111, SEPI 3, MATI 0) — **0,66% dari 17.398**.
  `cacah_calon_penuh` = **17.284**.
- **`defisit_calon` = 712.925** lilin, tepat menutup sisa — **tautologis** (KC-50).
- **`defisit_teratas` (sepuluh baris) = 291.379**, `bagian_teratas` = **0,4087**.
- **`defisit_terbesar` = 42.510** — **TLMUSDT 2023-03**, HIDUP, 2.130 dari 44.640
  lilin (**95,2% kosong**).
- **Sepuluh teratas tersebar di tujuh bulan** (2023-03, 2022-09, 2023-02, 2022-04 ×2,
  2024-09, 2022-05 ×2, 2022-02 ×2) → aturan 81 TIDAK terpicu.
- **Pasangan `2022-05`:** ANCUSDT defisit **26.959** dan LUNAUSDT defisit **26.950** —
  berselisih **sembilan lilin**. Dasar **H-A021** (diusulkan, belum diuji).
  **Kalimat sebab apa pun untuk gugus itu DILARANG.**
- **Penggugur bersih:** `sidik_seragam` true · 8/8 laporan dibaca · `laporan_hilang`
  kosong · `cacah_kunci_ganda` 0 · `cacah_defisit_negatif` 0 ·
  `cacah_baris_tanpa_lilin` 0 · **sepuluh** selisih invarian NOL · `kendali_data_sah`
  true · `kendali_negatif_lolos` true · `kendali_nol_lolos` true.
- **Kendali nol** membuktikan modul sanggup menjawab **nol baris berdefisit** dan
  `bagian_teratas` **null** alih-alih mengarang angka (aturan 46, 50).

**LAMA [v10] (`keterisian_lilin` V1, commit `924b0d7a`):** jumlah lilin semesta LANGSUNG
**839.325.999** (selisih **516.135** terhadap 839.842.134); `cacah_baris_tanpa_lilin` 0
dari 19.586; MATI penuh **1.392**, MATI tak penuh **9**; defisit semesta **18.143.601**
dengan **17.335.439 (95,5%)** di bulan pertama dan **808.162** di bukan-pertama (bagian
**0,0445**); **bulan pertama rata-rata terisi ≈49,7%** (22.027 lilin hilang per bulan
pertama); kesembilan baris MATI tak penuh lengkap (LENDUSDT 2020-11 13.475/43.200/29.725
· FRONTUSDT 2024-09 14.986/43.200/28.214 · FOOTBALLUSDT 2024-05 39.308/44.640/5.332 ·
ANTUSDT 39.309/5.331 · BTSUSDT 39.310/5.330 · SRMUSDT 39.311/5.329 · HNTUSDT
39.312/5.328 · TOMOUSDT 39.315/5.325 · COCOSUSDT 39.317/5.323; jumlah **95.237** =
0,1178 dari 808.162); dua anomali R-308 LUNAS dua dari dua; tiga kendali BTCUSDT
`cacah_lilin` 44.640 dan HIDUP; harga TIDAK tersimpan (`medan_baris_terlihat` **14**
medan, tak satu pun harga).

**LAMA [v9] (`bulan_pertama` V1 run 30532058657):** 37 dari 38 baris HIDUP-kecil adalah
bulan pertama (0,973684); satu-satunya yang bukan **TLMUSDT 2023-03 (80.394 byte)**;
hanya 37 dari 787 bulan pertama yang kecil (±4,7%); nisbah rata byte **0,527179**
(897.374,517 lawan 1.702.219,726); klausa `2026-06` menyumbang NOL; lubang ukur
"bulan pertama di penyebut" ≠ "bulan pertama di bursa".

**LAMA [v8] (`irisan_byte` V1 run 30529294165):** 38 baris HIDUP ber-byte < 97.634
(0,21% kelas HIDUP); di zona 22.440–97.634 byte ada 38 HIDUP dan **0 MATI**; ekor bawah
MATI hanya 2 baris di bawah 150.000; sebaran per kelas IDENTIK dari tiga modul
(aturan 36) — HIDUP 18.087 / 32.049.492.952 / 22.440 / 2.770.666 / 1.771.962,899 ·
SEPI 98 / 77.728.024 / 259.327 / 1.231.408 / 793.143,102 · MATI 1.401 / 579.041.399 /
97.634 / 451.875 / 413.305,781 · `cacah_lain` 0 · total byte **32.706.262.375**.

**LAMA [v7]:** bagian byte MATI **0.017704**; `cacah_byte_nol` 0; dasar keras ≈22 KB.

**LAMA [v6] (`lubang_tebing` V1 run 30524631435):** `mati_dulu` **40** (0.339) ·
`serempak` **78** (0.661) · `lubang_dulu` **0**; tebing `2025-07` menguasai 39 dari 40
`mati_dulu` (0.975), satu-satunya bukan-tebing **BTCSTUSDT** (KC-47); 122 dari 787
simbol pernah berlubang funding (awal 5, bukan-awal 118, BNXUSDT keduanya); delapan
simbol bangkit CVCUSDT 29 · CVXUSDT 13 · SLPUSDT 13 · CTKUSDT 11 · LITUSDT 10 ·
TLMUSDT 8 · ICPUSDT 2 · MAVIAUSDT 2 = 88.

**Belum diukur, urut prioritas [tidak berubah sejak v11 — tidak ada pengukuran baru]:**
(1) **lubang tengah gugus `2022-05` dan `2024-05`** untuk menegakkan atau meruntuhkan
**H-A021 dan H-A020 sekaligus**; (2) **selisih 516.135** lawan dugaan 12 simbol-bulan
karantina (516.135 / 12 = 43.011 — DUGAAN, belum diuji; porosnya **wajib berupa bentuk
SEBARAN, bukan rata-rata**, sebab rata-rata selalu benar secara aritmetis dan karena
itu tidak berisiko); (3) **sebab kekosongan TLMUSDT 2023-03** (95,2% kosong, HIDUP);
(4) apakah "bulan pertama di penyebut" = "bulan pertama di bursa"; (5) tebing funding
`2025-07` (39 simbol) dan BTCSTUSDT; (6) irisan 880 lawan 877; selisih 40−38
`diagnosa_kc15`; hari hilang BNXUSDT 2022-04/06/08; bentangan 38 kohort; H-A016;
mati_tersisip atas 19.586; `ukur_baris` V6; R-7/19/20/28/36/37 dan R-199;
R-236..R-247 dari jurnal 92–94; taksonomi lubang tiga kelas.

## Penomoran berikutnya

Aturan resmi **1–81, 83, 84, dan 85** · calon **77**, **78**, **82** (ketiganya belum
resmi) · **aturan berikutnya yang bebas 86** · KC resmi sampai **KC-51** (KC-16 kosong
selamanya) · **KC berikutnya KC-52** · Hipotesis terbuka H-A016 (belum diuji), H-A017
(dilemahkan R-306), H-A018 (tafsir dibatasi ADR-A014 dan A015), H-A019 (DITERIMA
TERBATAS oleh ADR-A016 kep. 1, **DILEMAHKAN oleh ADR-A018 kep. 6 tanpa pengganti**),
**H-A020 (DIUSULKAN, BELUM diuji)**, **H-A021 (DIUSULKAN, BELUM diuji)** · Hipotesis
berikutnya **H-A022** · Jurnal berikutnya **136** · `STATE.md` berikutnya **v53** ·
EKOR berikutnya **v13** · **UKUR berikutnya v12 (utang salah ketik)** · PROMPT
berikutnya **v55 (belum didorong)** · ADR berikutnya **A019** · Ramalan berikutnya
**R-312** · papan skor **311**, dan sesudah R-312 diadjudikasi **312**.
