# STATE lampiran EKOR — bagian 2 dari STATE (v11, milik STATE v51)

**Mengapa berkas ini ada.** Dua push `STATE.md` berturut terpotong (v41, v42);
pemecahan ke tiga berkas berlaku sejak v43 (KC-42). Pembagian yang berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, 83, dan 84; KC-1..KC-50 dan usulan
   KC-51.
2. **`STATE_LAMPIRAN_EKOR.md`** (berkas ini, v11) — bagian 2: papan skor, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** — bagian 3: pengukuran, modul, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip lama; bukan sumber lagi.

Dasar v11: EKOR v10 (blob **`42fce0212c6f90581c39fc4df939616c479b6920`**), dibaca UTUH
sebelum berkas ini ditulis (aturan 52), pada giliran yang sama.

**PERINGATAN KESERASIAN VERSI YANG BERLAKU SEKARANG.** Saat berkas ini didorong:

- `STATE.md` **v51** — blob **`412a5b2dc9a05613b5e71f5a987c59687f3382d6`**, commit
  **`8c30de51cc4d0098d4bd2922966684591bd7ce96`**, dibaca ulang UTUH sesudah push.
  SERASI dengan berkas ini.
- `STATE_LAMPIRAN_EKOR.md` **v11** — berkas ini. SERASI.
- `STATE_LAMPIRAN_UKUR.md` masih **v10** — blob
  **`162c130592c723f7bde5862546982b8d8a5295af`**. **USANG SEBAGIAN:** belum memuat API
  `sisa_defisit` V1, belum memuat 114 baris berdefisit dan sepuluh baris teratasnya,
  belum memuat **H-A021**, dan cacah modul/uji/workflow masih 47/51/42 dengan utang
  cacah tangan yang **kini sudah LUNAS** (49/53/44 pada ref `3196fd98`).

Sampai UKUR v11 naik, sumber sah untuk hasil R-311 adalah
`journal/2026-07-30-135.md` (blob `626293c1ccd61eb8d8d063b48ad51112f5fda476`),
`reports/sisa_defisit_ringkas.json` (blob `91a05c0528050d0d37e4cf7711b6556f13fc8d16`),
dan `reports/sisa_defisit_status.json` (blob `1c9c2c5fc5f14a3f0e5cadcf564e699c92f8cf0e`).
Pemecahan bertahap ini SENGAJA (KC-42, KC-43).

**Nomor versi lampiran kini DIVERIFIKASI dari kepala berkas, bukan dari blob.**
Giliran ini membuka baris pertama kedua lampiran dan membacanya: EKOR **v10** dan UKUR
**v10**, keduanya bertanda "milik STATE v50". Larangan mengutip "v10" yang dibawa
serah terima dengan itu dicabut, dan v11 ini adalah kelanjutannya yang sah.

**KOREKSI SALAH KETIK DI BERKAS INI SENDIRI (LUNAS di sini).** EKOR v10 menulis
"Bulan pertama rata-rata terisi **≉**49,7%". Karakter `≉` berarti "tidak kira-kira sama
dengan" — kebalikan dari yang dimaksud. Bacaan yang benar **≈49,7%**, sebagaimana
sudah dicatat UKUR v10 Koreksi 5. Karena v11 menulis ulang seluruh berkas, karakter itu
**diperbaiki langsung di teks di bawah**; jejak koreksinya ditinggalkan di sini agar
tidak dibaca sebagai perubahan angka.

**Tentang push berkas ini:** berkas ini berada di akar repo sehingga menyalakan
`ci.yml`. Tidak satu pun `tests/**` berubah, jadi cacah uji tetap **1341** — ramalan
deretministik (aturan 57), **MUDAH**, TIDAK masuk papan skor dan TIDAK menambah
beruntun.

## KC-43..KC-51 (teks lengkap KC-43..KC-47 di STATE v47, KC-49 di v48, KC-50 di v50, KC-51 di v51)

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
  **[v11] Diperiksa untuk R-311 dan TIDAK terpicu:** sepuluh baris berdefisit teratas
  tersebar di tujuh bulan berbeda; kelompok terbesar satu bulan hanya dua baris.
- **KC-48 [RESMI v7]** — ambang absolut pada besaran yang sebarannya belum pernah
  diukur. Penangkal: usulan aturan 82.
- **KC-49 [RESMI v8 lampiran ini]** — pita dikunci tanpa menghitung implikasi
  aritmetis momen yang sudah terukur. Penangkalnya BERLAKU sebagai aturan 83.
- **KC-50 [RESMI di STATE v50]** — agregat semesta dihitung lewat jalan memutar
  alih-alih LANGSUNG dari baris, sehingga selisih terhadap sumber lain mustahil
  terlihat. Dua kasus: `total_byte` `irisan_byte` (delapan bebas + satu turunan), dan
  **839.842.134 dipakai seolah jumlah lilin** sampai `keterisian_lilin` V1 menghitung
  langsung **839.325.999** — **selisih 516.135**. **Cacat kelas ini tidak menghasilkan
  galat; ia menghasilkan kesunyian.** **[v11] Menggigit lagi di R-311:** penutupan
  sisa 712.925 adalah TAUTOLOGI dari 808.162 − 95.237, bukan pengukuran bebas.
- **KC-51 [DIUSULKAN di STATE v51, BELUM RESMI] — taksiran pemusatan bias ke arah
  terlalu menyebar.** Tiga kasus berturut tanpa pembalikan arah: R-308 butir 2
  (terukur 2 lawan pita 10..300), R-310 (0,0445 lawan taksir 0,073), R-311 (114 lawan
  taksir 3.000 — faktor 26,3; pemusatan 0,4087 lawan taksir 0,15 — +172%). Penangkal
  yang diusulkan menjadi **aturan 85**: tepi pita di sisi "terpusat" diletakkan pada
  atau dekat lantai aritmetis yang sudah dihitung, bukan pada kelipatan intuitif di
  atasnya. Peresmian adalah tugas **ADR-A018**.

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
| R-307 | (1) bagian byte MATI atas total byte 19.586 dalam 0.02..0.15; (2) cacah simbol-bulan TERUKUR ber-`byte_parquet` < 10.000 dalam 20..400; (3) sembilan invarian nol + dua kendali + kode 0 + CI | **MELESET** — butir 1 KALAH (**0.017704**, tipis di bawah pita); butir 2 KALAH (**0**, ambang MUSTAHIL, KC-48); butir 3 MENANG (MUDAH) |
| R-308 | (1) cacah HIDUP ber-byte < 97.634 dari 18.087 dalam **20..600**; (2) cacah MATI ber-byte < 150.000 dari 1.401 dalam **10..300**; (3) sembilan invarian nol + dua kendali sah + kode 0 + CI | **SEPARUH** — butir 1 **MENANG** (**38**); butir 2 **KALAH** (**2**, KC-49); butir 3 **MENANG** (MUDAH) |
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
**ADJUDIKASI RISET TETAP TERKUNCI.** Ramalan berikutnya **R-312** (poros belum
ditetapkan; ADR-A016 menolak penyusunan percobaan pada giliran yang sama dengan
adjudikasi).

**Nisbah papan skor, dihitung tangan dan disebut apa adanya:** dari 296 ramalan yang
sudah beradjudikasi penuh (217 + 57 + 22), TEPAT **73,3%**, MELESET **19,3%**, SEPARUH
**7,4%**. Angka itu **DILARANG dibaca sebagai mutu ramalan**: sebagian besar butir
ketiga tiap ramalan berlabel MUDAH dan tidak berisiko.

**Utang papan skor:** rincian R-236..R-247 masih di jurnal 92–94; R-229 TEPAT dan
R-230 MELESET (dari docstring) menunggu pemeriksaan R-224..R-235.

## Catatan kejujuran [v11]

**R-311 SEPARUH. Kekalahannya lebih berharga daripada kemenangannya, dan ini
kekalahan ketiga berturut ke arah yang sama.**

1. **Butir 1 KALAH telanjang: 114 lawan pita 200 .. 12.000.** Bukan meleset tipis —
   nyata **1,75× di bawah tepi bawah**, dan **26,3× di bawah taksiran titik 3.000**
   yang dipakai menyusun pita. Lantai aritmetis yang sudah dihitung sendiri di jurnal
   134 adalah **16**; tepi bawah tetap diletakkan di 200, dua belas setengah kali di
   atas lantai itu. **Aturan 83 ditaati, dan tetap kalah** — karena aritmetika
   implikasi hanya menjamin rentang (16 .. 18.790) dan tidak pernah memaksa tepi
   diletakkan dekat lantai. Itu lubang yang KC-51 usulkan untuk ditutup lewat aturan
   85.
2. **Butir 2 MENANG, tetapi menempel tepi ATAS:** 0,4087 pada pita 0,02 .. 0,45 —
   sisa hanya **0,0413**, sekitar sembilan persen lebar pita. R-310 menang menempel
   tepi BAWAH pada kedua butirnya. **Dua ramalan berturut yang menang menempel tepi,
   dan pada tepi BERLAWANAN, DILARANG dibacakan sebagai bukti pita yang dirancang
   baik.** Yang ditunjukkannya justru sebaliknya: pita disusun tanpa gambaran sebaran.
3. **Penutupan 712.925 nyaris TAUTOLOGIS.** `defisit_calon` = 712.925 tepat dan
   `selisih_sisa` = 0, tetapi angka itu **terpaksa** muncul dari 808.162 − 95.237
   begitu seluruh 1.401 baris MATI ternyata bukan-pertama. Menyebutnya "pengukuran
   bebas yang mengonfirmasi" DILARANG (KC-50, KC-37).
4. **Temuan yang benar-benar baru dan tidak tautologis:** sisa 712.925 lilin ditanggung
   hanya **114 baris** dari 17.398 calon (**0,66%**), rata-rata **6.254** lilin per
   baris; **sepuluh baris teratas (8,8% dari 114) memikul 40,87%**. Kekosongan itu
   **sangat terpusat**, bukan tersebar tipis — kebalikan dari yang ditaksir.
5. **TLMUSDT 2023-03 muncul lagi, dan gambarannya berubah.** Ia puncak daftar
   berdefisit: status HIDUP, **2.130 dari 44.640 lilin — 95,2% kosong**. Selama ini ia
   "satu-satunya lawan H-A019" yang tak terjelaskan. Kini terlihat bahwa ia bukan
   bulan tepi dan bukan bulan pertama, melainkan **bulan HIDUP yang hampir seluruhnya
   kosong**. Itu **melemahkan** bacaan "byte kecil = bulan sebagian di tepi" **tanpa
   menegakkan penggantinya**. Sebabnya tetap BELUM diukur.
6. **Seluruh 114 baris HIDUP (111) atau SEPI (3), tak satu pun MATI** — itu **dipaksa
   oleh definisi penyebut kerja** (calon = bukan-pertama dan bukan-MATI), jadi BUKAN
   temuan. Menyebutnya "penemuan bahwa kekosongan hanya menimpa yang hidup" adalah
   kesalahan bentuk KC-37.
7. **Pemeriksaan silang yang menutup tanpa sisa** (terbitan, TIDAK diskor):
   18.799 − 17.398 = **1.401** = seluruh baris MATI → tidak satu pun bulan pertama
   simbol berstatus MATI; 18.087 − 17.318 = **769** bulan pertama HIDUP;
   98 − 80 = **18** bulan pertama SEPI; 769 + 18 = **787** = `cacah_simbol`.
8. **Aturan 57 beruntun 3 dari 3.** Daftar **44** butir `test_01`..`test_44` ditulis
   bernomor satu nama per nomor tanpa rentang; ramalan 1297 + 44 = **1341**, kode 0;
   terukur **1341**, kode 0. Dua helper (`_baris`, `_ringkasan_bersih`) sengaja
   berawalan garis bawah agar tidak dikumpulkan pytest.
9. **KOREKSI ATAS STATE v51 YANG BARU SAJA DITULIS — dilakukan dengan pengukuran,
   bukan dengan pendapat.** STATE v51 menulis bahwa ramalan "CI tetap" pada push
   dokumen **"tidak pernah terukur"** karena `ci_terakhir.json` hanya menyimpan run
   terakhir. **Itu terlalu keras dan kini terbantah oleh bacaan langsung.** Sesudah
   push STATE v51 (commit `8c30de51`), `ci.yml` menyala dan menulis ulang laporan:
   blob **`bce1177ea21d7a4e01b59b2d4f4277a8584b4eed`**, run **30545364506**, commit
   **`8c30de51cc4d0098d4bd2922966684591bd7ce96`**, 2026-07-30T13:05:55Z, kode 0,
   **1341 butir** (`1341 tests collected in 0.45s`). Jadi ramalan "tetap 1341" untuk
   push STATE v51 **TERUKUR dan TEPAT**. Rumusan yang benar: ramalan semacam itu
   terukur **bila dibaca sebelum run berikutnya menimpanya**, dan tetap **MUDAH,
   TIDAK diskor, TIDAK menambah beruntun aturan 57** karena tidak menyentuh
   `tests/**`. Berkas ini menang atas STATE v51 pada titik itu saja (KC-41: yang
   terukur mengalahkan yang disimpulkan).
10. **Aturan 66 LUNAS — utang nomor 29 ditutup.** Cacah TANGAN bernomor pada ref
    **`3196fd9809f23917ba819b4339cdfdd57bb808d1`**: `lux_ai/serapan/` **49** ·
    `tests/` **53** · `.github/workflows/` **44** · akar **18** (6 direktori +
    12 berkas). Angka 48/52/43 pada ref `5d7d8b96` tetap sah untuk ref itu.
    **Kecocokan dengan turunan bukan alasan melewatkan pencacahan berikutnya.**
11. **Dua berkas akar yang tidak pernah diperiksa akhirnya dibuka.**
    `STATE_LAMPIRAN.md` (`f2b90764`, 2.350 B) HIDUP sebagai arsip naratif L-1..L-5,
    tanpa angka semesta. `STATE_LAMPIRAN_ANGKA.md` (`f3ebdb02`, 1.841 B) HIDUP tetapi
    hampir kosong: `N_percobaan` = 0, audit gerbang / sidik run / sidik data kosong,
    isinya angka repo WARISAN dan daftar klaim yang DILARANG dipakai sebagai bukti.
    **Tiga sisanya — `PETA_MODUL.md`, `PETA_MODUL_BERKAS.md`, `PROMPT_KELANJUTAN.md`
    — TIDAK dibaca, dan tidak ada satu kalimat pun tentang isinya di v51 atau di
    berkas ini.**
12. **Giliran ini BERHENTI sebelum UKUR v11**, atas pertimbangan konteks. Itu keputusan
    sadar mengikuti KC-42/KC-43, bukan kelalaian; utangnya dicatat terbuka di bawah.

**Kesalahan proses giliran ini:** tidak ada kegagalan konektor — seluruh `push_files`
dan `get_file_contents` berhasil sekali jalan, tidak ada pemotongan terdeteksi.
`BATAS_BARIS_LAPORAN=40` kembali bekerja pada `sisa_defisit_ringkas.json`; usulan
aturan 78 makin kuat (kali kelima berturut).

## Jumlah uji

**1341 TERUKUR [v11], dua bacaan pada giliran ini.**

1. `reports/ci_terakhir.json` blob **`2d32f814e5e426e1411559810b55b9f20176a22d`**: run
   **30542217837**, commit **`b1c7941db3e08ae8a6f06864d7f47a571abf5669`** (trio
   `sisa_defisit`), 2026-07-30T12:22:10Z, `kode_keluar` 0, **1341 butir**
   (`1341 tests collected in 0.62s`). Dicatat lewat jurnal 135.
2. `reports/ci_terakhir.json` blob **`bce1177ea21d7a4e01b59b2d4f4277a8584b4eed`**: run
   **30545364506**, commit **`8c30de51cc4d0098d4bd2922966684591bd7ce96`** (push STATE
   v51), 2026-07-30T13:05:55Z, `kode_keluar` 0, **1341 butir**
   (`1341 tests collected in 0.45s`). **Dibaca LANGSUNG dari repo pada giliran ini.**

Turunan: 1297 + **44** butir `tests/test_sisa_defisit.py` = **1341** ✅ (aturan 21).

Riwayat panjang: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 →
984 → 1044 → 1100 → 1168 → 1233 → 1297 → **1341**.

Cacah per berkas uji (yang diketahui): `test_irisan_byte.py` **68** ·
`test_bulan_pertama.py` **65** · `test_keterisian_lilin.py` **64** ·
`test_bentangan_kohort.py` V2 **63** · `test_lubang_tebing.py` **60** ·
`test_sebab_bangkit.py` **57** · `test_byte_semesta.py` **56** ·
`test_lubang_awal.py` **48** · `test_tersisip_semesta.py` **47** ·
`test_anatomi_tengah.py` 47 · **`test_sisa_defisit.py` 44 (dicacah TANGAN,
`test_01`..`test_44`, daftar bernomor ditulis sebelum push)** · `test_terhenti.py` V4
33 · `test_bulan_absen.py` 32 · `test_karantina_semesta.py` 28 ·
`test_silang_settled.py` 24.

**Aturan 57: beruntun 3 dari 3** sesudah putus di 26/27. Hanya push yang menyentuh
`tests/**` yang dihitung.

### REKONSILIASI ORDINAL ATURAN 38 — utang dari STATE v51 (LUNAS di sini, dengan definisi tersurat)

Masalahnya: STATE v50 mencatat pemakaian ke-**37**, lalu terjadi beberapa pembacaan
sebelum berkas ini, dan nomor berjalannya jadi kabur. **Definisi yang dipakai untuk
merekonsiliasi, ditulis tersurat agar dapat diperiksa:** *pemakaian aturan 38 dihitung
hanya untuk pembacaan `reports/ci_terakhir.json` yang meninggalkan JEJAK TERTULIS
(nomor run + commit + blob) di STATE, lampiran, atau jurnal.* Pembacaan tanpa jejak
tidak pernah masuk buku besar dan karena itu tidak dapat, dan tidak boleh, dihitung.

| ke- | CI | run | commit | blob | jejak |
|---|---|---|---|---|---|
| 36 | 1233 | 30533500210 | `f8098980` | `016fb234` | STATE v50 |
| 37 | 1297 | 30535202643 | `924b0d7a` | `3c07c909` | STATE v50, EKOR v10 |
| 38 | 1297 | 30541051907 | `5d7d8b96` | — | jurnal 135 (blob tidak dicatat di sana) |
| 39 | 1341 | 30542217837 | `b1c7941d` | `2d32f814` | jurnal 135, STATE v51 |
| 40 | 1341 | 30545364506 | `8c30de51` | `bce1177e` | berkas ini |

**Pemakaian berjalan = ke-empat puluh.** Cacat yang tersisa dan disebut apa adanya:
baris ke-38 **tidak memuat blob** — ia diwarisi dari jurnal 135, bukan dibaca ulang
pada giliran ini, dan blob itu sudah tertimpa sehingga tidak dapat dipulihkan.
Karena itu ordinal 40 sah **relatif terhadap definisi di atas**, bukan sebagai
pencacahan mutlak. Bila kemudian ditemukan jejak pembacaan lain di jurnal 133–134,
nomor ini WAJIB dikoreksi, bukan dipertahankan.

## Utang verifikasi

1-5, 11 menunggu tahap juri. 6-23, 25-28 LUNAS. **Nomor utang BUKAN nomor
ramalan — KC-32.**

24. **AKTIF.** Lunas lama seperti v10. **LUNAS BARU [v11]:**
    - **Trio `sisa_defisit` V1 dibaca ulang UTUH dari main** sesudah push `b1c7941d`
      (aturan 52, 55): `lux_ai/serapan/sisa_defisit.py`
      (**`7aa0e6d7003902e50806570ad112aae7f0345b07`**, 25.949 B),
      `tests/test_sisa_defisit.py`
      (**`7004115acffd9c03c9ba4f9873bef40cb6b1375f`**, 44 butir dicacah tangan),
      `.github/workflows/sisa_defisit.yml`
      (**`645112075e104a74d43f3e3d2185cfbd48b0b513`**, `paths` SATU entri).
    - `PROMPT.md` v54 (`e1aecf77`), `STATE.md` v50 (`095a4b2c`), EKOR v10
      (`42fce021`), UKUR v10 (`162c1305`), `journal/2026-07-30-135.md` (`626293c1`),
      `decisions/ADR-A017.md` (`1be570f2`) dibaca UTUH pada giliran ini.
    - **`STATE_LAMPIRAN.md` (`f2b907648bb291d5a4e44e5683270d84cf981a6a`) dan
      `STATE_LAMPIRAN_ANGKA.md` (`f3ebdb02f4e03fea6e45a2fba107a50f69ace7c6`) dibaca
      UTUH untuk PERTAMA kalinya** — keduanya keluar dari daftar BELUM.
    - `STATE.md` v51 (`412a5b2d`) dibaca ulang UTUH sesudah push.
    - `reports/ci_terakhir.json` (`bce1177e`) dibaca utuh dan blobnya DICATAT.
    **TETAP BELUM:** `tests/test_bentangan_kohort.py` V2 (63 butir, blob `9f850ecd`,
    13.154 B) belum dibaca ulang byte demi byte — kini **SEMBILAN versi** menunggu;
    sisa daftar BELUM: `ADR-A002`, A004, A006, A007, A008, **`PETA_MODUL.md`**
    (`9ee33a99`, 8.691 B), **`PETA_MODUL_BERKAS.md`** (`3abe95f6`, 6.890 B),
    **`PROMPT_KELANJUTAN.md`** (`35beed44`, 10.777 B), `karantina_semesta.yml`
    (`de40fa4e`), `test_pulihkan.py`, `test_rilis_karantina.py`,
    `test_karantina_a006.py`.
29. **LUNAS [v11].** Cacah tangan tiga direktori pada ref pasca-R-311 sudah dilakukan
    bernomor: 49 / 53 / 44 pada ref `3196fd98`, ditambah 18 entri akar.
30. **BARU [v11] — cacah tangan pada ref sesudah trio BERIKUTNYA.** Begitu modul ukur
    baru didorong, angka 50 / 54 / 45 menjadi TURUNAN dan DILARANG dikutip sebagai
    terukur sampai dicacah satu per satu bernomor (aturan 66, KC-33).
31. **BARU [v11] — UKUR v11 belum naik.** Selama itu, UKUR v10 USANG SEBAGIAN dan
    tidak boleh dikutip untuk `sisa_defisit`, 114 baris berdefisit, H-A021, atau cacah
    direktori.

## Daftar ADR

- **ADR-A001** aturan dasar. DITERIMA.
- **ADR-A002** serapan. Kondisi v3 berlaku; §10 tetap tidak boleh diubah.
- **ADR-A003** taksonomi rezim. BELUM ADA. Wajib memuat delapan simbol bangkit,
  koreksi ADR-A011/A012/A013/A014/A015/A016/**A017**, bentangan LITUSDT, bulan ABSEN,
  aturan 76, KC-40.
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
  (5) besar berkas bukan detektor status ke arah mana pun — **[v11] TIDAK dibalik oleh
  R-310 maupun R-311**; (6) H-A019 didaftarkan; (7) cacah invarian wajib menyebut mana
  yang bebas — kini KC-50 resmi; (8) aturan 57 dicatat PUTUS 26/27 — **[v11] kini
  beruntun 3/3**. **DITERIMA.**
- **ADR-A016** (commit `8fad9091`, blob `209802d7`) — H-A019 diterima TERBATAS sebagai
  irisan asimetris, bukan sebab. Delapan keputusan: (1) rumusan resmi satu-satunya;
  (2) klausa `2026-06` DICABUT; (3) usulan aturan 84 — DIRESMIKAN di STATE v50;
  (4) koreksi jurnal 129, hanya TLMUSDT 2023-03 yang melawan — **[v11] TLMUSDT 2023-03
  kini terukur 95,2% kosong, dan itu melemahkan tafsir lama tanpa menegakkan
  penggantinya**; (5) `total_byte` wajib jalur langsung — kini KC-50 resmi;
  (6) batas tafsir "bulan pertama" = di dalam penyebut 19.586; (7) prioritas riset ke
  isi bulan MATI — DIJAWAB R-310; (8) cacah tangan 47/51/42 pada ref `010edff2`.
  **DITERIMA.**
- **ADR-A017** (blob **`1be570f29e95227393dfb0989354cbbb5024b46c`**) — **DITERIMA**,
  dibaca UTUH pada giliran ini. Sebelas keputusan: (1) rumusan resmi temuan R-310
  (bulan MATI penuh datanya, yang nol transaksinya); (2) larangan menyimpulkan apa pun
  tentang harga; (3) **KC-50 diresmikan**; (4) koreksi resmi 839.842.134 lawan
  839.325.999, selisih 516.135; (5) **aturan 84 diresmikan**; (6) numerator 9 bukan
  sembilan pengamatan bebas; (7) **H-A020 diusulkan** + larangan menulis "delisting
  28 Mei 2024"; (8) A015 kep. 5 TIDAK dibalik; (9) H-A019 dikuatkan lewat jalur ukur
  kedua, TLMUSDT 2023-03 tetap melawan; (10) pertanyaan terbuka berpindah ke sisa
  712.925 — **[v11] DIJAWAB sebagian oleh R-311: 114 baris, sangat terpusat**;
  (11) cacah tangan 48/52/43 pada ref `5d7d8b96`.
- **ADR berikutnya A018** — calon isinya: peresmian **KC-51**, perumusan **aturan 85**,
  rumusan resmi temuan R-311 (114 baris, 0,4087, TLMUSDT 2023-03), status **H-A021**,
  dan penetapan poros R-312. **DILARANG disusun pada giliran yang sama dengan
  adjudikasi** (ADR-A016).

## Temuan sampingan

**BARU [v11], terukur (`sisa_defisit` V1, run modul 30542217951 pada commit
`b1c7941d`, kode 0; laporan ringkas blob `91a05c05`, status blob `1c9c2c5f`; sidik kode
`6211624ba9514d604d4dc510abca2e40386775c7aaa1279135f0baf666f044b0`):**

- **Penyebut kerja `cacah_calon` = 17.398** baris bukan-pertama dan bukan-MATI
  (HIDUP 17.318 + SEPI 80). Terbitan yang menutup: 18.799 − 1.401 = 17.398.
- **`cacah_berdefisit` = 114** (HIDUP 111, SEPI 3, MATI 0) — **0,66% dari 17.398**.
  `cacah_calon_penuh` = **17.284**.
- **`defisit_calon` = 712.925** lilin, tepat menutup sisa — **tautologis** (KC-50).
- **`defisit_teratas` (sepuluh baris) = 291.379**, `bagian_teratas` = **0,4087**.
  Sepuluh baris memikul dua per lima seluruh kekosongan bukan-pertama non-MATI.
- **`defisit_terbesar` = 42.510** — **TLMUSDT 2023-03**, HIDUP, 2.130 dari 44.640
  lilin (**95,2% kosong**).
- **Sepuluh teratas tersebar di tujuh bulan** (2023-03, 2022-09, 2023-02, 2022-04 ×2,
  2024-09, 2022-05 ×2, 2022-02 ×2) → aturan 81 TIDAK terpicu.
- **Pasangan `2022-05`:** ANCUSDT defisit **26.959** dan LUNAUSDT defisit **26.950** —
  berselisih **sembilan lilin**. Dasar **H-A021** (diusulkan, belum diuji).
  **Kalimat sebab apa pun untuk gugus itu DILARANG.**
- **Penggugur bersih:** `sidik_seragam` true · 8/8 laporan dibaca · `laporan_hilang`
  kosong · `cacah_kunci_ganda` 0 · `cacah_defisit_negatif` 0 · `cacah_baris_tanpa_lilin`
  0 · **sepuluh** selisih invarian NOL · `kendali_data_sah` true · `kendali_negatif_lolos`
  true · `kendali_nol_lolos` true.
- **Kendali nol** membuktikan modul sanggup menjawab **nol baris berdefisit** dan
  `bagian_teratas` **null** alih-alih mengarang angka (aturan 46, 50).

**LAMA [v10], tetap berlaku (`keterisian_lilin` V1, commit `924b0d7a`):** jumlah lilin
semesta LANGSUNG **839.325.999** (selisih **516.135** terhadap 839.842.134);
`cacah_baris_tanpa_lilin` 0 dari 19.586; MATI penuh **1.392**, MATI tak penuh **9**;
defisit semesta **18.143.601** dengan **17.335.439 (95,5%)** di bulan pertama dan
**808.162** di bukan-pertama (bagian **0,0445**); **bulan pertama rata-rata terisi
≈49,7%** (22.027 lilin hilang per bulan pertama) — *karakter `≉` pada v10 adalah salah
ketik, lihat kepala berkas*; kesembilan baris MATI tak penuh lengkap (LENDUSDT 2020-11
13.475/43.200/29.725 · FRONTUSDT 2024-09 14.986/43.200/28.214 · FOOTBALLUSDT 2024-05
39.308/44.640/5.332 · ANTUSDT 39.309/5.331 · BTSUSDT 39.310/5.330 · SRMUSDT
39.311/5.329 · HNTUSDT 39.312/5.328 · TOMOUSDT 39.315/5.325 · COCOSUSDT 39.317/5.323;
jumlah **95.237** = 0,1178 dari 808.162); dua anomali R-308 LUNAS dua dari dua; tiga
kendali BTCUSDT `cacah_lilin` 44.640 dan HIDUP; harga TIDAK tersimpan
(`medan_baris_terlihat` 14 medan, tak satu pun harga).

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
97.634 / 451.875 / 413.305,781 · `cacah_lain` 0 · total byte 32.706.262.375.

**LAMA [v7]:** bagian byte MATI **0.017704**; `cacah_byte_nol` 0; dasar keras ≈22 KB.

**LAMA [v6] (`lubang_tebing` V1 run 30524631435):** `mati_dulu` **40** (0.339) ·
`serempak` **78** (0.661) · `lubang_dulu` **0**; tebing `2025-07` menguasai 39 dari 40
`mati_dulu` (0.975), satu-satunya bukan-tebing **BTCSTUSDT** (KC-47); 122 dari 787
simbol pernah berlubang funding (awal 5, bukan-awal 118, BNXUSDT keduanya); delapan
simbol bangkit CVCUSDT 29 · CVXUSDT 13 · SLPUSDT 13 · CTKUSDT 11 · LITUSDT 10 ·
TLMUSDT 8 · ICPUSDT 2 · MAVIAUSDT 2 = 88.

**Belum diukur, urut prioritas [diperbarui v11]:** (1) **lubang tengah gugus `2022-05`
dan `2024-05`** untuk menegakkan atau meruntuhkan **H-A021 dan H-A020 sekaligus**;
(2) **selisih 516.135** lawan dugaan 12 simbol-bulan karantina (516.135 / 12 = 43.011
— DUGAAN, belum diuji; porosnya harus sebaran, bukan rata-rata, aturan 83);
(3) **sebab kekosongan TLMUSDT 2023-03** (95,2% kosong, HIDUP); (4) apakah "bulan
pertama di penyebut" = "bulan pertama di bursa"; (5) tebing funding `2025-07`
(39 simbol) dan BTCSTUSDT; (6) irisan 880 lawan 877; selisih 40−38 `diagnosa_kc15`;
hari hilang BNXUSDT 2022-04/06/08; bentangan 38 kohort; H-A016; mati_tersisip atas
19.586; `ukur_baris` V6; R-7/19/20/28/36/37 dan R-199; R-236..R-247 dari jurnal 92–94;
taksonomi lubang tiga kelas.

## Penomoran berikutnya

Aturan resmi **1–81, 83, dan 84** · calon **77**, **78**, **82** (ketiganya belum
resmi) · aturan berikutnya yang bebas **85** (calon isinya penangkal KC-51) · KC sampai
**KC-50** resmi (KC-16 kosong selamanya) · **KC-51 DIUSULKAN di STATE v51, belum
resmi** · KC berikutnya sesudahnya **KC-52** · Hipotesis terbuka H-A016 (belum diuji),
H-A017 (dilemahkan R-306), H-A018 (tafsir dibatasi ADR-A014 dan A015), H-A019
(DITERIMA TERBATAS oleh ADR-A016 kep. 1), **H-A020 (DIUSULKAN, BELUM diuji)**,
**H-A021 (DIUSULKAN di STATE v51, BELUM diuji — ANCUSDT dan LUNAUSDT `2022-05` sebagai
SATU peristiwa)** · Hipotesis berikutnya **H-A022** · Jurnal berikutnya **136** ·
STATE: `STATE.md` **v51** dan EKOR **v11** sudah didorong, **UKUR v11 BELUM** (lihat
peringatan keserasian versi di kepala berkas ini) · PROMPT berikutnya **v55** · ADR
berikutnya **A018** · Ramalan berikutnya **R-312** · papan skor **311**.
