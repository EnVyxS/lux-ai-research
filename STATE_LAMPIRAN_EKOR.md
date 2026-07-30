# STATE lampiran EKOR — bagian 2 dari STATE (v10, milik STATE v50)

**Mengapa berkas ini ada.** Dua push `STATE.md` berturut terpotong (v41, v42);
pemecahan ke tiga berkas berlaku sejak v43 (KC-42). Pembagian yang berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, 83, dan 84; KC-1..KC-50.
2. **`STATE_LAMPIRAN_EKOR.md`** (berkas ini, v10) — bagian 2: papan skor, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** — bagian 3: pengukuran, modul, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip lama; bukan sumber lagi.

Dasar v10: EKOR v9 (blob **`beaed54cb93e00c2c56f1aaa8d1c2709c97f08d0`**), dibaca UTUH
sebelum berkas ini ditulis (aturan 52).

**Peringatan keserasian versi di kepala v9 kini GUGUR** — UKUR v9 sudah naik seperti
dijanjikan, lalu `STATE.md` naik lagi ke **v50**. Jejaknya sengaja tidak dihapus dari
riwayat; jangan memperlakukannya sebagai utang hidup.

**PERINGATAN KESERASIAN VERSI YANG BERLAKU SEKARANG.** Saat berkas ini didorong:

- `STATE.md` **v50** — blob **`095a4b2cd8b6b5cadeb3e887ab72fa7dde4c81c3`**, commit
  `0c8ddac8484c2c8c053180c1af15937d339cd306`. SERASI dengan berkas ini.
- `STATE_LAMPIRAN_EKOR.md` **v10** — berkas ini. SERASI.
- `STATE_LAMPIRAN_UKUR.md` masih **v9** — blob
  **`0b795fb48ababa61b318518ce1196ad90467e077`**. **USANG SEBAGIAN:** belum memuat API
  `keterisian_lilin` V1, belum memuat kesembilan baris MATI tak penuh, belum memuat
  koreksi 516.135, belum memuat H-A020, dan cacah modul/uji/workflow masih 47/51/42.

Sampai UKUR v10 naik, sumber sah untuk hasil R-310 adalah
`journal/2026-07-30-132.md` (blob `35c5400ea2a6fb6191c26bd5d7f7dbc3f630b2f0`),
`reports/keterisian_lilin.json` (blob `14f1772070789dad603b132ece034ea4c19c6e3d`), dan
`reports/keterisian_lilin_ringkas.json` (blob `f33714eda66e77d37a7024b52c433ead070b16c7`).
Pemecahan bertahap ini SENGAJA (KC-42, KC-43).

**Tentang push berkas ini:** berkas ini berada di akar repo sehingga menyalakan
`ci.yml`. Tidak satu pun `tests/**` berubah, jadi cacah uji tetap **1297** — ramalan
deterministik (aturan 57), **MUDAH**, TIDAK masuk papan skor.

## KC-43..KC-50 (teks lengkap KC-43..KC-47 di STATE v47, KC-49 di v48, KC-50 di v50)

- **KC-43** — tanda tangan fungsi dari INGATAN. Penangkal: baca modul yang diimpor
  UTUH pada giliran yang sama.
- **KC-44** — semua laporan di-commit satu langkah. Penangkal: commit tiap berkas
  laporan sendiri-sendiri.
- **KC-45 [RESMI v45]** — satuan "bulan tanpa funding" vs "bulan MATI" dicampur.
- **KC-46 [RESMI v45]** — lubang bentuk AWAL dibaca sebagai "funding berhenti".
- **KC-47 [RESMI v46]** — satu peristiwa menyamar sebagai banyak pengamatan bebas
  (39 dari 40 `mati_dulu` berbagi tebing `2025-07`). Penangkal: aturan 81, ADR-A013.
  **[v10] KASUS BARU YANG KUAT:** dari sembilan baris MATI tak penuh R-310, **TUJUH**
  berbulan `2024-05` dengan `cacah_lilin` 39.308–39.317 — jendela **9 lilin**. Numerator
  9 karena itu BUKAN sembilan pengamatan bebas; paling banter **tiga** (gugus 2024-05,
  LENDUSDT 2020-11, FRONTUSDT 2024-09).
- **KC-48 [RESMI v7]** — ambang absolut pada besaran yang sebarannya belum pernah
  diukur. Penangkal: usulan aturan 82.
- **KC-49 [RESMI v8 lampiran ini]** — pita dikunci tanpa menghitung implikasi
  aritmetis momen yang sudah terukur. Penangkalnya BERLAKU sebagai aturan 83.
- **KC-50 [DIRESMIKAN di STATE v50] — agregat semesta dihitung lewat jalan memutar
  (dijumlahkan dari total per kelas atau disalin dari angka yang sudah tercatat)
  alih-alih LANGSUNG dari baris, sehingga selisih terhadap sumber lain menjadi
  mustahil terlihat.** Dua kasus: (1) `total_byte` di `irisan_byte.ringkaskan` —
  delapan pemeriksaan bebas + satu turunan, menyebut "sembilan pemeriksaan bebas"
  DILARANG; (2) **total baris parquet 839.842.134** dipakai berulang seolah jumlah
  lilin, sampai `keterisian_lilin` V1 menghitung langsung dan memunculkan
  **839.325.999** — **selisih 516.135**. Kasus kedua lebih tajam: yang pertama membuat
  pemeriksaan terhitung berlebih, yang kedua menyembunyikan ketidakcocokan nyata.
  **Cacat kelas ini tidak menghasilkan galat; ia menghasilkan kesunyian.**

## Papan skor prediksi — lengkap R-300..R-310 (R-199..R-299 di v4, blob `67dda29e`)

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
| R-310 | (1) cacah baris MATI ber-`cacah_lilin` kurang dari lilin penuh bulannya, dari 1.401, dalam **1..120**; (2) bagian defisit lilin yang ditanggung baris bukan-pertama dalam **0.02..0.25**; (3) delapan selisih invarian nol + tiga kendali sah + lima penggugur bersih + kode 0 + CI | **TEPAT (2 berisiko menang, 1 mudah cocok)** — butir 1 **MENANG** (**9** dari 1.401); butir 2 **MENANG** (**0,0445**); butir 3 **MENANG** (MUDAH) |

**Total R-1..R-310** (dihitung tangan, aturan 21). Dasar v9 (papan skor R-1..R-309):
TEPAT 216 · MELESET 57 · SEPARUH 21 · TIDAK TERADJUDIKASI 8 · MENUNGGU 7 = 309.

Sesudah v9: **R-310 TEPAT**.

- TEPAT 216 + 1 = **217**
- MELESET **57**
- SEPARUH **21**
- TIDAK TERADJUDIKASI **8**
- MENUNGGU **7** (R-7, R-19, R-20, R-28, R-36, R-37, R-199)

217 + 57 = 274; 274 + 21 = 295; 295 + 8 = 303; 303 + 7 = **310** ✅ Nomor terpakai
R-1..R-310, seluruhnya teradjudikasi atau menunggu. N_percobaan = 0.
**ADJUDIKASI RISET TETAP TERKUNCI.** Ramalan berikutnya **R-311** (poros belum
ditetapkan; ADR-A016 menolak penyusunan percobaan pada giliran yang sama dengan
adjudikasi).

**Utang papan skor:** rincian R-236..R-247 masih di jurnal 92–94; R-229 TEPAT dan
R-230 MELESET (dari docstring) menunggu pemeriksaan R-224..R-235.

## Catatan kejujuran [v10]

**R-310 TEPAT — dan giliran ini menghasilkan sesuatu yang lebih berharga daripada
kemenangannya: sebuah angka yang selama berpuluh berkas salah dipakai.**

1. **KOREKSI TERBESAR: 839.842.134 BUKAN jumlah lilin.** `jumlah_lilin_langsung`
   terukur **839.325.999** — selisih **516.135** terhadap total baris parquet yang
   dikutip berulang di repo. Sepanjang jurnal 131 §6 keduanya diperlakukan sebagai
   besaran yang sama dan SELURUH aritmetika implikasi dibangun di atasnya. Itu salah.
   Ramalan R-310 tetap sah karena pitanya dikunci sebelum pengukuran (aturan 29),
   tetapi taksiran yang mengantarnya cacat di bahan baku. Dari sinilah **KC-50** naik
   menjadi resmi.
2. **Kedua butir menang DEKAT TEPI BAWAH, dan itu memurahkan kemenangannya.**
   Butir 1 terukur **9** pada pita 1..120; butir 2 **0,0445** pada pita 0,02..0,25.
   Pita yang lebar di sisi atas membuat kemenangan lebih murah daripada yang tampak.
   DILARANG membacakan R-310 sebagai konfirmasi kuat.
3. **Numerator 9 bukan sembilan pengamatan bebas.** Tujuh dari sembilan berbulan
   `2024-05` dalam jendela sembilan lilin (KC-47, aturan 81). Kesimpulan apa pun
   tentang "bentuk kematian sebagian" yang memakai penyebut 9 memakai penyebut palsu.
4. **Dua anomali lama LUNAS, dan itu memang kemenangan.** Baris 1 dan 2 dari sembilan
   — LENDUSDT 2020-11 (97.634 byte) dan FRONTUSDT 2024-09 (109.120 byte) — adalah
   tepat kedua `cacah_mati_byte_kecil` R-308. Dua dari dua. Berkas MATI yang kecil itu
   kecil karena lilinnya memang sedikit, bukan karena hal lain.
5. **Larangan ADR-A015 kep. 5 TIDAK dibalik.** Meski butir 4 menjelaskan dua berkas
   MATI kecil, besar berkas tetap DILARANG dipakai sebagai detektor status ke arah
   mana pun. Menjelaskan dua kasus bukan membangun detektor.
6. **Aturan 83 bekerja sebagai PENCEGAH, dua kali, sebelum pita dikunci.** Tiga calon
   butir dibuang: (a) cacah baris MATI berlilin penuh, sudah tertentu ≈1.370–1.401 —
   **terukur 1.392, tepat di dalam rentang yang dihitung sebelum mengukur; itu akan
   menjadi kemenangan murahan**; (b) cacah MATI ber-`cacah_lilin` < 1.440, hampir
   pasti 0; (c) nisbah byte-per-lilin MATI:HIDUP, tersirat 0,233.
7. **Taksiran diadu dengan kenyataan, termasuk yang meleset.** Defisit semesta taksir
   18.612.246 → terukur **18.143.601** (−2,5%); defisit bulan pertama taksir 17.247.105
   → terukur **17.335.439** (+0,5% — anggapan "bulan pertama terisi separuh" meleset
   hanya setengah persen); bagian bukan-pertama taksir 0,073 → terukur **0,0445**
   (meleset ±64% ke atas, dan justru itu yang menjaga butir 2 tetap berisiko).
8. **Aturan 57 beruntun 2 dari 2.** Daftar 64 butir `test_01`..`test_64` ditulis
   bernomor satu nama per nomor tanpa rentang; ramalan 1233 + 64 = **1297**, kode 0;
   terukur **1297**, kode 0. Dua helper sengaja berawalan garis bawah agar tidak
   dikumpulkan pytest — itulah yang mencegah ramalan meleset ke atas.
9. **SALAH KETIK yang diakui dan dilunasi di tempat lain.** Judul jurnal 132 §3
   berbunyi "beruntun 2/1"; badan teksnya menulis "2/2", dan **2/2 yang benar**.
   Jurnal tidak diperbaiki dengan push ulang (KC-42); koreksinya resmi di STATE v50,
   yang menang atas jurnal pada titik itu saja.
10. **Aturan 66 TIDAK dapat diklaim taat.** Cacah tangan sah terakhir ada pada ref
    `07a69d39`: 47 / 51 / 42. Angka 48 / 52 / 43 sesudah trio R-310 adalah TURUNAN
    pengurangan — persis yang dilarang aturan 66 (KC-33). **Utang hidup.**
11. **Ramalan yang BELUM terukur, dinyatakan apa adanya.** `ci_terakhir.json` hanya
    menyimpan run TERAKHIR. Ramalan "CI tetap 1233" untuk push STATE v49
    (`8dd0e4a5`), EKOR v9 (`a3830617`), dan PROMPT v53 (`ec885f7e`) tidak pernah
    terukur. Ditambah satu lagi: **push STATE v50 (`0c8ddac8`) tidak didahului ramalan
    sama sekali** — bukan tepat, bukan meleset, dan jangan dihitung sebagai beruntun.
12. **Aturan 84 DIRESMIKAN dengan dua kasus berbentuk berbeda:** kegagalan terukur
    R-309 (klausa `2026-06` menyumbang NOL) dan penerapan preventif R-310 (kedua butir
    sengaja berklausa tunggal, pelaporan per baris membuat tiap angka dapat dibongkar).

**Kesalahan proses giliran ini:** tidak ada kegagalan konektor — seluruh `push_files`
dan `get_file_contents` berhasil sekali jalan, tidak ada pemotongan terdeteksi.
`BATAS_BARIS_LAPORAN=40` kembali bekerja: `keterisian_lilin.json` (6.588 B) terbaca
UTUH dalam satu bacaan — kali keempat berturut; usulan aturan 78 makin kuat.

## Jumlah uji

**1297 TERUKUR [v10].** `reports/ci_terakhir.json` blob
**`3c07c9093d5232ce3852b2ac509fd9e9875f0f33`**: run **30535202643**, commit
**`924b0d7afcf1f9e17965dff931d36489ad27f01b`**, 2026-07-30T10:35:00Z, `kode_keluar` 0,
**1297 butir terkumpul** (`1297 tests collected in 0.60s`). Turunan: 1233 + **64**
butir `tests/test_keterisian_lilin.py` = **1297** ✅ (aturan 21).

Riwayat panjang: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 →
984 → 1044 → 1100 → 1168 → 1233 → **1297**.

Cacah per berkas uji (yang diketahui): `test_irisan_byte.py` **68** ·
`test_bulan_pertama.py` **65** · `test_keterisian_lilin.py` **64** (dicacah TANGAN,
`test_01`..`test_64`, daftar bernomor sebelum ramalan) ·
`test_bentangan_kohort.py` V2 **63** · `test_lubang_tebing.py` **60** ·
`test_sebab_bangkit.py` **57** · `test_byte_semesta.py` **56** ·
`test_lubang_awal.py` **48** · `test_tersisip_semesta.py` **47** ·
`test_anatomi_tengah.py` 47 · `test_terhenti.py` V4 33 · `test_bulan_absen.py` 32 ·
`test_karantina_semesta.py` 28 · `test_silang_settled.py` 24.

**Aturan 57: beruntun 2 dari 2** sesudah putus di 26/27.

Aturan 38 (cacah uji HANYA dari `ci_terakhir.json`): pemakaian ke-**tiga puluh tujuh**
(ke-36 untuk CI 1233 blob `016fb234`, run 30533500210, commit `f8098980`; ke-37 untuk
CI 1297 blob `3c07c909`, run 30535202643, commit `924b0d7a`).

## Utang verifikasi

1-5, 11 menunggu tahap juri. 6-23, 25-28 LUNAS. **Nomor utang BUKAN nomor
ramalan — KC-32.**

24. **AKTIF.** Lunas lama seperti v9. **LUNAS BARU [v10]:**
    - **Trio `keterisian_lilin` V1 dibaca ulang UTUH dari main** sesudah push
      `924b0d7a` (aturan 52, 55): `lux_ai/serapan/keterisian_lilin.py`
      (**`3f80ffa72008008d567ef32f9f278b8931e91ac3`**),
      `tests/test_keterisian_lilin.py`
      (**`f58912d0b1531dbf537de4c0b4f0a803a3ad1f69`**, 64 butir dicacah tangan),
      `.github/workflows/keterisian_lilin.yml`
      (**`d821c63a462a8338ccd63f8014f7c8847602fdff`**, `paths` SATU entri).
    - `reports/keterisian_lilin.json` (**`14f1772070789dad603b132ece034ea4c19c6e3d`**,
      6.588 B) dan `reports/keterisian_lilin_ringkas.json` (**`f33714ed`**) terbaca
      **UTUH**; `ci_terakhir.json` (**`3c07c909`**) terbaca utuh dan blobnya DICATAT.
    - `journal/2026-07-30-131.md` (`cae9ab53`), `journal/2026-07-30-132.md`
      (`35c5400e`), `STATE.md` v49 (`64dc7b3f`) dan v50 (`095a4b2c`) dibaca UTUH.
    - EKOR v9 (`beaed54c`) dibaca UTUH sebelum berkas ini ditulis.
    **TETAP BELUM:** `tests/test_bentangan_kohort.py` V2 (63 butir, blob `9f850ecd`)
    belum dibaca ulang byte demi byte — kini **DELAPAN versi** menunggu; seluruh
    daftar BELUM dari v4/v5 masih berlaku (`ADR-A002`, A004, A006, A007, A008,
    `PETA_MODUL.md`, `PETA_MODUL_BERKAS.md`, `STATE_LAMPIRAN.md`,
    `STATE_LAMPIRAN_ANGKA.md`, `karantina_semesta.yml`, `test_pulihkan.py`,
    `test_rilis_karantina.py`, `test_karantina_a006.py`).
29. **BARU [v10] — cacah tangan tiga direktori pada ref pasca-R-310.** Angka
    48 / 52 / 43 adalah TURUNAN dan DILARANG dikutip sebagai terukur sampai dicacah
    satu per satu bernomor (aturan 66, KC-33).

## Daftar ADR

- **ADR-A001** aturan dasar. DITERIMA.
- **ADR-A002** serapan. Kondisi v3 berlaku; §10 tetap tidak boleh diubah.
- **ADR-A003** taksonomi rezim. BELUM ADA. Wajib memuat delapan simbol bangkit,
  koreksi ADR-A011/A012/A013/A014/A015/**A016**, bentangan LITUSDT, bulan ABSEN,
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
- **ADR-A015** (commit `982c2536`, blob `387d551051da4f0d539f7c9c26e438a9ac84c9a3`) —
  pita praregistrasi wajib melewati aritmetika implikasi. Delapan keputusan:
  (1) KC-49 resmi; (2) aturan 83 diusulkan — **DIRESMIKAN di STATE v49**; (3) usulan
  aturan 82 diperluas; (4) R-308 SEPARUH; (5) besar berkas bukan detektor status ke
  arah mana pun — **[v10] TIDAK dibalik oleh R-310**; (6) H-A019 didaftarkan;
  (7) cacah invarian wajib menyebut mana yang bebas — **[v10] kini KC-50 resmi**;
  (8) aturan 57 dicatat PUTUS 26/27 — **[v10] kini beruntun 2/2**. **DITERIMA.**
- **ADR-A016** (commit `8fad90910cff2cc94ff117cb4f5d9f50788aaae3`, blob
  `209802d7b5eeff9a0d66f13d552b83145acb9dd6`) — H-A019 diterima TERBATAS sebagai
  irisan asimetris, bukan sebab. Delapan keputusan: (1) rumusan resmi satu-satunya
  yang boleh dikutip; (2) klausa `2026-06` DICABUT; (3) usulan aturan 84 — **kini
  DIRESMIKAN di STATE v50**; (4) koreksi resmi jurnal 129, hanya TLMUSDT 2023-03 yang
  melawan; (5) `total_byte` wajib jalur langsung — **kini berstatus KC-50 resmi dan
  WAJIB bagi modul baru**; (6) batas tafsir "bulan pertama" = di dalam penyebut
  19.586, bukan di bursa; (7) prioritas riset berpindah ke isi berkas bulan MATI —
  **[v10] DIJAWAB oleh R-310**; (8) cacah tangan 47/51/42 pada ref `010edff2`.
  **DITERIMA.**
- **ADR berikutnya A017** — calon isinya: formalisasi keputusan jurnal 132 §13
  (KC-50, aturan 84, koreksi 516.135, H-A020, larangan menulis "delisting 28 Mei
  2024").

## Temuan sampingan

**BARU [v10], terukur (`keterisian_lilin` V1, commit `924b0d7a`, laporan blob
`14f17720` dan `f33714ed`, sidik kode
`1cd98f4fa22c24b30f31f5b36dac0ea0bb3fa9de44e5e15ae73cbf11cdca08bb`):**

- **Jumlah lilin semesta dihitung LANGSUNG: 839.325.999** atas 19.586 baris — selisih
  **516.135** terhadap total baris parquet 839.842.134. Kedua besaran BUKAN besaran
  yang sama (KC-50).
- **`cacah_baris_tanpa_lilin` = 0 dari 19.586.** Sah dibaca hanya karena kendali
  negatifnya membuktikan modul BISA mendeteksi baris tanpa lilin (aturan 50).
- **Baris MATI berlilin PENUH: 1.392. Baris MATI TAK penuh: 9.** Jadi 99,4% bulan
  MATI berisi lilin sebanyak-banyaknya bulan itu — **bulan MATI penuh datanya, yang
  nol adalah transaksinya.**
- **Defisit lilin semesta 18.143.601**, dengan **17.335.439 (95,5%)** di bulan pertama
  simbol dan **808.162** di bulan bukan-pertama (bagian **0,0445**).
- **Bulan pertama rata-rata terisi ≉49,7%**: defisit rata 17.335.439 / 787 =
  **22.027** lilin per bulan pertama.
- **Kesembilan baris MATI tak penuh, lengkap** (semuanya `pertama: false`):
  1 LENDUSDT 2020-11 lilin 13.475 / penuh 43.200 / defisit 29.725 ·
  2 FRONTUSDT 2024-09 lilin 14.986 / 43.200 / 28.214 ·
  3 FOOTBALLUSDT 2024-05 lilin 39.308 / 44.640 / 5.332 ·
  4 ANTUSDT 2024-05 lilin 39.309 / defisit 5.331 ·
  5 BTSUSDT 2024-05 lilin 39.310 / 5.330 ·
  6 SRMUSDT 2024-05 lilin 39.311 / 5.329 ·
  7 HNTUSDT 2024-05 lilin 39.312 / 5.328 ·
  8 TOMOUSDT 2024-05 lilin 39.315 / 5.325 ·
  9 COCOSUSDT 2024-05 lilin 39.317 / 5.323.
  Jumlah defisit kesembilan: **95.237** — hanya **0,1178** dari 808.162.
- **Dua anomali R-308 LUNAS, dua dari dua:** baris 1 dan 2 adalah tepat kedua
  `cacah_mati_byte_kecil` (97.634 dan 109.120 byte).
- **SISA 712.925 lilin BELUM DIJELASKAN** — defisit bukan-pertama yang tidak
  ditanggung kesembilan baris MATI itu. Pertanyaan terbuka nomor satu.
- Lima penggugur bersih: `sidik_seragam` true · 8/8 laporan dibaca ·
  `cacah_kunci_ganda` 0 · `cacah_defisit_negatif` 0 · `cacah_baris_tanpa_lilin` 0.
  Tiga kendali BTCUSDT (2021-05, 2021-08, 2021-01) semuanya `cacah_lilin` **44.640**
  dan HIDUP. Kedelapan selisih invarian **nol**.
- **Yang DILARANG disimpulkan:** harga TIDAK tersimpan di laporan kehidupan —
  `medan_baris_terlihat` hanya 14 medan dan tak satu pun harga; "harga beku" atau
  "lilin datar" DILARANG disimpulkan. Kalimat "tujuh simbol didelisting 28 Mei 2024"
  DILARANG ditulis sebagai temuan; yang terukur hanya jendela sembilan lilin.

**LAMA [v9], tetap berlaku (`bulan_pertama` V1 run 30532058657):** 37 dari 38 baris
HIDUP-kecil adalah bulan pertama (0,973684); satu-satunya yang bukan **TLMUSDT
2023-03 (80.394 byte)**; hanya 37 dari 787 bulan pertama yang kecil (±4,7%); nisbah
rata byte **0,527179** (897.374,517 lawan 1.702.219,726); klausa `2026-06` menyumbang
NOL; lubang ukur "bulan pertama di penyebut" ≠ "bulan pertama di bursa".

**LAMA [v8], tetap berlaku (`irisan_byte` V1 run 30529294165):** 38 baris HIDUP
ber-byte < 97.634 (0,21% kelas HIDUP); di zona 22.440–97.634 byte ada 38 HIDUP dan
**0 MATI**; ekor bawah MATI hanya 2 baris di bawah 150.000; sebaran per kelas IDENTIK
dari tiga modul (aturan 36) — HIDUP 18.087 / 32.049.492.952 / 22.440 / 2.770.666 /
1.771.962,899 · SEPI 98 / 77.728.024 / 259.327 / 1.231.408 / 793.143,102 · MATI 1.401
/ 579.041.399 / 97.634 / 451.875 / 413.305,781 · `cacah_lain` 0 · total byte
32.706.262.375.

**LAMA [v7]:** bagian byte MATI **0.017704**; `cacah_byte_nol` 0; dasar keras ≈22 KB.

**LAMA [v6] (`lubang_tebing` V1 run 30524631435):** `mati_dulu` **40** (0.339) ·
`serempak` **78** (0.661) · `lubang_dulu` **0**; tebing `2025-07` menguasai 39 dari 40
`mati_dulu` (0.975), satu-satunya bukan-tebing **BTCSTUSDT** (KC-47); 122 dari 787
simbol pernah berlubang funding (awal 5, bukan-awal 118, BNXUSDT keduanya); delapan
simbol bangkit CVCUSDT 29 · CVXUSDT 13 · SLPUSDT 13 · CTKUSDT 11 · LITUSDT 10 ·
TLMUSDT 8 · ICPUSDT 2 · MAVIAUSDT 2 = 88.

**Belum diukur, urut prioritas (jurnal 132 §14):** (1) **sisa 712.925 lilin** — baris
mana yang menanggungnya; (2) **selisih 516.135** lawan dugaan 12 simbol-bulan
karantina (516.135 / 12 = 43.011 ≈ sebulan penuh — DUGAAN, belum diuji); (3) **lubang
tengah gugus `2024-05`** untuk menegakkan atau meruntuhkan **H-A020**; (4) **TLMUSDT
2023-03**; (5) apakah "bulan pertama di penyebut" = "bulan pertama di bursa";
(6) tebing funding `2025-07` (39 simbol) dan BTCSTUSDT; (7) irisan 880 lawan 877;
selisih 40−38 `diagnosa_kc15`; hari hilang BNXUSDT 2022-04/06/08; bentangan 38 kohort;
H-A016; mati_tersisip atas 19.586; `ukur_baris` V6; R-7/19/20/28/36/37 dan R-199;
R-236..R-247 dari jurnal 92–94; taksonomi lubang tiga kelas.

## Penomoran berikutnya

Aturan resmi **1–81, 83, dan 84** (aturan **84 DIRESMIKAN di STATE v50**) · calon
**77**, **78**, **82** (ketiganya belum resmi) · aturan berikutnya yang bebas **85** ·
KC sampai **KC-50** (KC-16 kosong selamanya; **KC-50 DIRESMIKAN di STATE v50**) · KC
berikutnya **KC-51** · Hipotesis terbuka H-A016 (belum diuji), H-A017 (dilemahkan
R-306), **H-A018** (tafsir dibatasi ADR-A014 dan A015), **H-A019** (DITERIMA TERBATAS
oleh ADR-A016 kep. 1), **H-A020 (DIUSULKAN di STATE v50, BELUM diuji — tujuh baris
`2024-05` sebagai SATU peristiwa)** · Hipotesis berikutnya **H-A021** · Jurnal
berikutnya **133** · STATE: `STATE.md` **v50** dan EKOR **v10** sudah didorong,
**UKUR v10 BELUM** (lihat peringatan keserasian versi di kepala berkas ini) · PROMPT
berikutnya **v54** · ADR berikutnya **A017** · Ramalan berikutnya **R-311** · papan
skor **310**.
