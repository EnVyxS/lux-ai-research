# STATE lampiran EKOR — bagian 2 dari STATE (v9, milik STATE v49)

**Mengapa berkas ini ada.** Dua push `STATE.md` berturut terpotong (v41, v42);
pemecahan ke tiga berkas berlaku sejak v43 (KC-42). Pembagian yang berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81 dan 83, KC-1..KC-49.
2. **`STATE_LAMPIRAN_EKOR.md`** (berkas ini, v9) — bagian 2: papan skor, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** — bagian 3: pengukuran, modul, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip lama; bukan sumber lagi.

Dasar v9: EKOR v8 (blob **`c34c88e27dce4813622c2e3ea71bf4d486ec65d6`**), dibaca UTUH
sebelum berkas ini ditulis (aturan 52).

**Peringatan keserasian versi di kepala v8 kini GUGUR** — `STATE.md` v48 dan UKUR v8
sudah naik pada giliran berikutnya seperti dijanjikan, lalu `STATE.md` naik lagi ke
**v49**. Jejaknya sengaja tidak dihapus dari riwayat; jangan memperlakukannya sebagai
utang hidup.

**PERINGATAN KESERASIAN VERSI YANG BERLAKU SEKARANG.** Saat berkas ini didorong:

- `STATE.md` **v49** — blob **`64dc7b3fed15b447f297874e8410c9a6c4b7dd4e`**, commit
  `8dd0e4a5`. SERASI dengan berkas ini.
- `STATE_LAMPIRAN_EKOR.md` **v9** — berkas ini. SERASI.
- `STATE_LAMPIRAN_UKUR.md` masih **v8** — blob
  **`ff19069512bd4604b18cedb896af1d6cf6ba2557`**. **USANG SEBAGIAN:** H-A019 masih
  tercatat BELUM diuji dan praregistrasi R-309 masih tercatat menunggu.

Sampai UKUR v9 naik, sumber sah untuk hasil R-309 adalah
`journal/2026-07-30-130.md` (blob `d4c48ae45a6fbeffdf473824f3fa69f6506ed909`),
`decisions/ADR-A016.md` (blob `209802d7b5eeff9a0d66f13d552b83145acb9dd6`), dan
`reports/bulan_pertama.json` (blob `0a2aa6ae15d949b44803dffdc9e97dbd322bbc85`).
Pemecahan bertahap ini SENGAJA: `push_files` menulis ulang seluruh berkas, sehingga
menulis tiga berkas besar dari satu konteks yang sudah terpakai banyak adalah cara
paling pasti merusak aturan 1–83 (KC-42, KC-43).

**Tentang push berkas ini:** berkas ini berada di akar repo sehingga menyalakan
`ci.yml`. Tidak satu pun `tests/**` berubah, jadi cacah uji tetap **1233** — ramalan
deterministik (aturan 57), **MUDAH**, TIDAK masuk papan skor.

## KC-43..KC-49 (teks lengkap KC-43..KC-47 di STATE.md v47, KC-49 di v48)

- **KC-43** — tanda tangan fungsi dari INGATAN. Penangkal: baca modul yang diimpor
  UTUH pada giliran yang sama.
- **KC-44** — semua laporan di-commit satu langkah. Penangkal: commit tiap berkas
  laporan sendiri-sendiri.
- **KC-45 [RESMI v45]** — satuan "bulan tanpa funding" vs "bulan MATI" dicampur.
- **KC-46 [RESMI v45]** — lubang bentuk AWAL dibaca sebagai "funding berhenti".
- **KC-47 [RESMI v46]** — satu peristiwa menyamar sebagai banyak pengamatan bebas
  (39 dari 40 `mati_dulu` berbagi tebing `2025-07`). Penangkal: aturan 81, ADR-A013.
  **[v9] Kerabat baru:** usulan aturan 84 — klausa ATAU yang tidak bekerja dapat
  bersembunyi di balik klausa yang bekerja (butir 1 R-309).
- **KC-48 [RESMI v7]** — ambang absolut pada besaran yang sebarannya belum pernah
  diukur. Sumber terukur: ambang 10.000 byte pada butir 2 R-307 lawan minimum semesta
  22.440. Penangkal: usulan aturan 82.
- **KC-49 [RESMI v8 lampiran ini; teks penuh STATE v48, jurnal 129 §6, ADR-A015
  kep. 1]** — pita praregistrasi dikunci tanpa lebih dulu menghitung implikasi
  aritmetis dari momen yang SUDAH terukur. Sumber terukur: pita 10..300 pada butir 2
  R-308 sementara kelas MATI sudah diketahui ber-rata 413.306 dengan maksimum 451.875;
  terukur **2**. **Beda dari KC-48:** KC-48 soal ambang MUSTAHIL; KC-49 soal ambang
  yang MUNGKIN dilewati tetapi hasilnya sudah tersirat. **[v9] Penangkalnya kini
  BERLAKU sebagai aturan 83**, dan R-309 adalah bukti pertama penangkal itu bekerja.
- **Calon KC-50 (BELUM RESMI)** — medan invarian turunan dicacah sebagai pemeriksaan
  bebas (`total_byte` di `irisan_byte`). **[v9] Tetap satu kasus:** `bulan_pertama`
  justru memperbaikinya lewat `total_byte_langsung`, jadi tidak ada kasus kedua.

## Papan skor prediksi — lengkap R-300..R-309 (R-199..R-299 di v4, blob `67dda29e`)

| # | Prediksi | Status |
|---|---|---|
| R-300 | (1) cacah_bulan 64; (2) tetangga BTCST HIDUP; (3) cacah_hidup 8..30 dan MATI>HIDUP | **SEPARUH** |
| R-301 | (1) tebing==0; (2) mati_tersisip ≥1; (3) bangkit==0 | **TIDAK TERADJUDIKASI** |
| R-302 | (1) simbol tersisip 1..10; (2) simbol-bulan 1..50; (3) penyebut 19.586/787 | **SEPARUH** (butir 2 MELESET 88>50) |
| R-303 | (1) simbol tersisip 1..60; (2) simbol-bulan 1..300; (3) penyebut/kendali/kode 0 | **TEPAT (3/3)** |
| R-304 | (1) mati_dulu 5..8; (2) hidup_berlubang 3..8; (3) penyebut/kendali/kode 0 | **MELESET** (1 dan 2 kalah) |
| R-305 | (1) bagian mati-tak-setelah-lubang dari ≥100 dalam 0.55..0.95; (2) cacah lubang-awal 20..120; (3) invarian + kendali + kode 0 + CI | **MELESET** — butir 1 KALAH (penyebut 118, bagian **1.0**, tautologis aturan 10); butir 2 KALAH (**5** < 20); butir 3 TEPAT (MUDAH) |
| R-306 | (1) bagian arah STRIKT dari penyebut ≥100 dalam 0.25..0.60; (2) cacah tebing 2025-07 dalam 20..90; (3) sembilan invarian + dua kendali + kode 0 + CI | **TEPAT (3/3)** — butir 1 **0.339** (penyebut **118**); butir 2 **39**; butir 3 MENANG (MUDAH) |
| R-307 | (1) bagian byte MATI atas total byte 19.586 dalam 0.02..0.15; (2) cacah simbol-bulan TERUKUR ber-`byte_parquet` < 10.000 dalam 20..400; (3) sembilan invarian nol + dua kendali + kode 0 + CI | **MELESET** — butir 1 KALAH (**0.017704**, tipis di bawah pita; arah H-A018 justru didukung); butir 2 KALAH (**0**, ambang MUSTAHIL, KC-48); butir 3 MENANG (MUDAH) |
| R-308 | (1) cacah HIDUP ber-byte < 97.634 (byte_min MATI) dari 18.087 dalam **20..600**; (2) cacah MATI ber-byte < 150.000 dari 1.401 dalam **10..300**; (3) sembilan invarian nol + dua kendali sah + kode 0 + CI diukur | **SEPARUH** — butir 1 **MENANG** (**38**, bagian 0.0021009564880853653); butir 2 **KALAH** (**2**, di bawah tepi bawah pita, bagian 0.0014275517487508922, KC-49); butir 3 **MENANG** (MUDAH) |
| R-309 | (1) cacah baris HIDUP-kecil yang bulan PERTAMA simbol ATAU bulan tepi `2026-06`, dari 38, dalam **22..38**; (2) nisbah rata byte bulan-pertama atas rata byte bukan-pertama dalam **0.10..0.60**; (3) delapan selisih invarian nol + dua kendali sah + kode 0 + CI diukur | **TEPAT (3/3)** — butir 1 **MENANG** (**37** dari 38, bagian 0,973684); butir 2 **MENANG** (**0,527179**); butir 3 **MENANG** (MUDAH) |

**Total R-1..R-309** (dihitung tangan, aturan 21). Dasar v8 (papan skor R-1..R-308):
TEPAT 215 · MELESET 57 · SEPARUH 21 · TIDAK TERADJUDIKASI 8 · MENUNGGU 7 = 308.

Sesudah v8: **R-309 TEPAT**.

- TEPAT 215 + 1 = **216**
- MELESET **57**
- SEPARUH **21**
- TIDAK TERADJUDIKASI **8**
- MENUNGGU **7** (R-7, R-19, R-20, R-28, R-36, R-37, R-199)

216 + 57 = 273; 273 + 21 = 294; 294 + 8 = 302; 302 + 7 = **309** ✅ Nomor terpakai
R-1..R-309, seluruhnya teradjudikasi atau menunggu. N_percobaan = 0.
**ADJUDIKASI RISET TETAP TERKUNCI.** Ramalan berikutnya **R-310** (poros belum
ditetapkan; ADR-A016 kep. 7 mengarahkan ke isi berkas bulan MATI).

**Utang papan skor:** rincian R-236..R-247 masih di jurnal 92–94; R-229 TEPAT dan
R-230 MELESET (dari docstring) menunggu pemeriksaan R-224..R-235.

## Catatan kejujuran [v9]

**R-309 TEPAT, tiga dari tiga. Kemenangan bulat pertama sejak R-306 — dan justru
karena bulat, ia wajib dibaca dengan paling hati-hati.**

1. **Butir 1 menang besar, tetapi klausa keduanya menyumbang NOL.** Ramalan berbunyi
   "bulan PERTAMA simbol ATAU bulan tepi `2026-06`"; terukur 37 dari 38. Ketiga baris
   `2026-06` (SQQQUSDT, TQQQUSDT, MVLLUSDT) ternyata **juga** bulan pertama simbolnya,
   sehingga menghapus klausa tepi tetap menghasilkan **37**. Kemenangan itu kemenangan
   "bulan pertama", BUKAN kemenangan "bulan sebagian dalam dua rupa". Modul kebetulan
   menyimpan medan `pertama` dan `tepi` per baris sehingga cacat ini terlihat —
   kebetulan bukan penangkal; lahirlah **usulan aturan 84**.
2. **Butir 2 menang dengan margin tipis ke batas atas.** Terukur **0,527179** lawan
   tepi atas 0,60. Kemenangan tipis DILARANG dibacakan sebagai konfirmasi kuat.
   Yang penting justru besarnya: berkas bulan pertama rata-rata **setengah** ukuran
   bulan biasa, bukan sepersepuluh. Bulan pertama tidak "nyaris kosong"; ia separuh.
3. **Tiga dari empat dugaan saya di jurnal 129 SALAH, dan saya mencabutnya.**
   MTLUSDT 2021-03, ENJUSDT 2020-09, dan SLPUSDT 2023-10 saya sebut "tampak bulan
   tengah" sehingga melawan H-A019; terukur, ketiganya justru bulan **PERTAMA**
   simbolnya. Yang benar-benar melawan hanya **TLMUSDT 2023-03 (80.394 byte)**:
   bukan pertama, bukan tepi, tetap kecil. Satu lawan yang tersisa itu belum
   dijelaskan dan DILARANG dibuang sebagai pencilan (ADR-A016 menolak jalan itu).
4. **Asimetri yang wajib disebut lebih keras daripada kemenangannya.** 37 dari 38
   berkas kecil adalah bulan pertama (97,4%), tetapi hanya 37 dari 787 bulan pertama
   yang berkas kecil (**±4,7%**). Irisan ini asimetris tajam, sehingga H-A019 hanya
   DITERIMA TERBATAS: ia menjelaskan ekor bawah, ia TIDAK meramalkan bahwa bulan
   pertama akan kecil. Rumusan resmi satu-satunya yang boleh dikutip ada di ADR-A016
   kep. 1.
5. **Aturan 57 kembali berjalan: benar 1 dari 1.** Daftar 65 butir ditulis bernomor
   satu nama per nomor — tanpa rentang seperti "56–62" yang persis menyembunyikan
   butir hilang pada giliran ke-27. Ramalan 1168 + 65 = **1233**, kode 0; terukur
   **1233**, kode 0.
6. **Cacat administratif v8 LUNAS.** Blob `reports/ci_terakhir.json` kini dicatat
   untuk kedua pemakaian: CI 1168 = `2498e2cf6e6f6c7d0b8807bb5ba923ac1d803b6d`,
   CI 1233 = `0489d71101e451efe73d20fd8fe75ba6d41c5c27`.
7. **Aturan 83 DIRESMIKAN, dan dasarnya dikutip dari STATE v48 sendiri.** v48
   menuliskan satu-satunya syarat yang kurang — "belum diuji pada praregistrasi yang
   MENANG". R-309 memenuhinya: aritmetika implikasi ditulis lebih dulu, pita tetap
   dapat kalah ke dua arah, hasilnya menang. Tiga kasus kini tercatat: dua kegagalan
   (R-307, R-308) dan satu keberhasilan (R-309).
8. **Utang cacah tangan LUNAS lagi** (aturan 66): pada ref `010edff2`
   `lux_ai/serapan/` **47**, `tests/` **51**, `.github/workflows/` **42**, dinomori
   satu per satu. Cocok dengan turunan — dan kecocokan itu TIDAK menyahkan kewajiban
   mencacah (KC-33).
9. **Ramalan yang BELUM terverifikasi, dinyatakan apa adanya.** Untuk push `STATE.md`
   v49 (commit `8dd0e4a5`) saya meramalkan cacah tetap 1233; ketika
   `reports/ci_terakhir.json` dibaca sesudahnya, isinya masih commit `09ce9853`.
   Run untuk commit itu belum tercatat. Ramalan tersebut **belum diukur** — bukan
   tepat, bukan meleset; jangan mencatatnya sebagai kemenangan beruntun.

**Kesalahan proses giliran ini:** tidak ada kegagalan konektor — seluruh
`push_files` dan `get_file_contents` berhasil sekali jalan, dan tidak ada pemotongan
terdeteksi pada berkas mana pun. Satu hal yang BERJALAN BENAR lagi:
`BATAS_BARIS_LAPORAN=40` membuat `bulan_pertama.json` terbaca UTUH meski memuat
daftar 38 baris bertanda — kali ketiga berturut; usulan aturan 78 makin kuat.

## Jumlah uji

**1233 TERUKUR [v9].** `reports/ci_terakhir.json` blob
**`0489d71101e451efe73d20fd8fe75ba6d41c5c27`**: run **30532058688**, commit
**`09ce9853ccf6e077bad1038df35508f59f105a3e`**, 2026-07-30T09:47:29Z, `kode_keluar` 0,
**1233 butir terkumpul**. Turunan: 1168 + **65** butir `tests/test_bulan_pertama.py`
= **1233** ✅ (aturan 21).

Riwayat panjang: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 →
984 → 1044 → 1100 → 1168 → **1233**.

Cacah per berkas uji (yang diketahui): `test_irisan_byte.py` **68** ·
`test_bulan_pertama.py` **65** (dicacah TANGAN, `def test_` satu per satu, daftar
bernomor 1–65 di kepala berkas) · `test_bentangan_kohort.py` V2 **63** ·
`test_lubang_tebing.py` **60** · `test_sebab_bangkit.py` **57** ·
`test_byte_semesta.py` **56** · `test_lubang_awal.py` **48** ·
`test_tersisip_semesta.py` **47** · `test_anatomi_tengah.py` 47 ·
`test_terhenti.py` V4 33 · `test_bulan_absen.py` 32 ·
`test_karantina_semesta.py` 28 · `test_silang_settled.py` 24.

**Aturan 57 kembali berjalan: benar 1 dari 1** sesudah putus di 26/27.

Aturan 38 (cacah uji HANYA dari `ci_terakhir.json`): pemakaian ke-**tiga puluh lima**
(ke-34 untuk CI 1168 blob `2498e2cf`, ke-35 untuk CI 1233 blob `0489d711`).

## Utang verifikasi

1-5, 11 menunggu tahap juri. 6-23, 25-28 LUNAS. **Nomor utang BUKAN nomor
ramalan — KC-32.**

24. **AKTIF.** Lunas lama seperti v8. **LUNAS BARU [v9]:**
    - **Trio `bulan_pertama` V1 dibaca ulang UTUH dari main** sesudah push
      `09ce9853` (aturan 52, 55): `lux_ai/serapan/bulan_pertama.py`
      (**`b9bd00ac46a2825a8f1b540bbe9207e154f66bf4`**, 19.349 B),
      `tests/test_bulan_pertama.py`
      (**`75d87ba2f9254d362ef36d47637e33bdd2b503b5`**, 13.375 B, 65 butir dicacah
      tangan), `.github/workflows/bulan_pertama.yml`
      (**`2242e3e4a819f767c015f87a61bae1f5a2f6e82c`**, `paths` SATU entri).
    - `reports/bulan_pertama.json` (**`0a2aa6ae`**) terbaca **UTUH**; `_status.json`
      (`0c8ea41a`) terbaca utuh; `ci_terakhir.json` (**`0489d711`**) terbaca utuh dan
      blobnya DICATAT.
    - **Cacah tangan tiga direktori** pada ref `010edff2` (aturan 66): 47 / 51 / 42,
      dinomori satu per satu — utang tiga direktori LUNAS lagi.
    - `STATE.md` v48 (`2fd136e4`) dan v49 (`64dc7b3f`), PROMPT v52 (`16eafb15`),
      jurnal 130 (`d4c48ae4`), ADR-A016 (`209802d7`) dibaca ulang UTUH sesudah
      pushnya masing-masing.
    - EKOR v8 (`c34c88e2`) dibaca UTUH sebelum berkas ini ditulis.
    **TETAP BELUM:** `tests/test_bentangan_kohort.py` V2 (63 butir, blob
    `9f850ecd`) belum dibaca ulang byte demi byte — kini sudah **tujuh versi**
    menunggu; seluruh daftar BELUM dari v4/v5 masih berlaku (`ADR-A002`, A004, A006,
    A007, A008, `PETA_MODUL.md`, `PETA_MODUL_BERKAS.md`, `STATE_LAMPIRAN.md`,
    `STATE_LAMPIRAN_ANGKA.md`, `karantina_semesta.yml`, `test_pulihkan.py`,
    `test_rilis_karantina.py`, `test_karantina_a006.py`).

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
- **ADR-A015** (commit `982c2536`, blob **`387d551051da4f0d539f7c9c26e438a9ac84c9a3`**,
  giliran R-308) — **pita praregistrasi wajib melewati aritmetika implikasi.**
  Delapan keputusan: (1) **KC-49 resmi**; (2) **aturan 83 diusulkan** — **kini
  DIRESMIKAN di STATE v49**; (3) usulan aturan 82 DIPERLUAS; (4) R-308 SEPARUH,
  godaan melebarkan pita direkam lalu ditolak; (5) besar berkas bukan detektor status
  ke arah mana pun; (6) **H-A019 didaftarkan**; (7) cacah invarian wajib menyebut
  mana yang bebas; (8) aturan 57 dicatat PUTUS 26/27. **DITERIMA.**
- **ADR-A016** (commit `8fad90910cff2cc94ff117cb4f5d9f50788aaae3`, blob
  **`209802d7b5eeff9a0d66f13d552b83145acb9dd6`**, giliran R-309) — **H-A019 diterima
  TERBATAS sebagai irisan asimetris, bukan sebab.** Delapan keputusan:
  (1) rumusan resmi satu-satunya yang boleh dikutip — *hampir setiap baris HIDUP di
  zona byte kecil adalah bulan pertama simbol di dalam penyebut (37 dari 38),
  sementara hampir setiap bulan pertama BUKAN berkas kecil (37 dari 787, ±4,7%)*;
  (2) **klausa `2026-06` DICABUT** dari rumusan H-A019 — sumbangan bebasnya NOL;
  (3) **usulan aturan 84 diajukan** — butir berklausa ATAU wajib melaporkan sumbangan
  BEBAS tiap klausa terpisah; (4) **koreksi resmi jurnal 129** — tiga dari empat
  dugaan "bulan tengah" SALAH dan dicabut, hanya TLMUSDT 2023-03 yang melawan;
  (5) `total_byte` WAJIB dihitung dari jalur langsung, mengisi calon KC-50;
  (6) batas tafsir "bulan pertama" = bulan terkecil DI DALAM penyebut 19.586, bukan
  bulan pertama di bursa — dicatat sebagai lubang ukur; (7) prioritas riset berpindah
  ke sisi MATI — **APA ISI berkas bulan MATI**; (8) cacah tangan pasca-trio 47/51/42
  pada ref `010edff2`. Alternatif yang DITOLAK: menyatakan H-A019 terbukti tanpa
  kualifikasi; melebarkan ke kelas MATI; membuang TLMUSDT sebagai pencilan; menyusun
  R-310 pada giliran yang sama. **DITERIMA.**
- **ADR berikutnya A017.**

## Temuan sampingan

**BARU [v9], terukur (`bulan_pertama` V1 run **30532058657**, commit `09ce9853`,
kode 0, laporan blob `0a2aa6ae`, sidik kode
`0d3530f69ad51a22e038c17616411b56e4518698ff14c9b635131ec1e2a66562`):**

- **Irisan bulan pertama terukur:** dari **38** baris HIDUP ber-byte < 97.634,
  sebanyak **37** adalah bulan PERTAMA simbolnya di dalam penyebut 19.586
  (bagian **0,973684**). Satu-satunya yang bukan: **TLMUSDT 2023-03 (80.394 byte)**.
- **Asimetri arah balik:** hanya **37 dari 787** bulan pertama yang berkas kecil
  (±**4,7%**). Irisan ini DILARANG dibaca sebagai ramalan bahwa bulan pertama akan
  kecil (ADR-A016 kep. 1).
- **Nisbah rata byte:** rata bulan pertama **897.374,517** (jumlah 706.233.745 atas
  787 baris); rata bukan-pertama **1.702.219,726** (jumlah 32.000.028.630 atas 18.799
  baris); nisbah **0,527179**. Bulan pertama rata-rata **setengah** ukuran bulan
  biasa — bukan sepersepuluh.
- **Klausa tepi menyumbang NOL:** ketiga baris `2026-06` (SQQQUSDT 72.819,
  TQQQUSDT 82.330, MVLLUSDT 86.126) juga bulan pertama simbolnya, sehingga menghapus
  klausa tepi tetap menghasilkan 37 (usulan aturan 84).
- Delapan selisih invarian bebas seluruhnya **0** (`total_byte` dihitung lewat jalur
  LANGSUNG, bukan turunan penjumlahan kelas); `kendali_data_sah` true (tiga BTCUSDT
  terbesar); `kendali_deteksi_sah` true (semesta buatan lima baris dua simbol:
  hidup kecil 2, sebagian 2, nisbah 0,75, total byte 1.500 — seluruhnya cocok dengan
  hitungan tangan).
- **Lubang ukur yang diakui:** "bulan pertama" berarti bulan terkecil yang LOLOS
  gerbang 1m dan masuk penyebut 19.586, bukan bulan pertama simbol itu di bursa.
  Perbedaan keduanya belum diukur (ADR-A016 kep. 6).

**LAMA [v8], tetap berlaku (`irisan_byte` V1 run 30529294165, laporan `4c13bf6a`,
sidik `0e7103ef…`), DENGAN SATU KOREKSI:**

- **Lebar zona irisan terukur:** **38** baris HIDUP ber-byte < 97.634 (byte_min MATI),
  yaitu **0,21%** kelas HIDUP. Di zona 22.440–97.634 byte: 38 HIDUP, **0 MATI**.
- **Ekor bawah MATI nyaris kosong:** hanya **2** baris di bawah 150.000 —
  **LENDUSDT 2020-11 = 97.634** dan **FRONTUSDT 2024-09 = 109.120**.
- Sebaran per kelas IDENTIK dari tiga modul berbeda (aturan 36): HIDUP 18.087 /
  32.049.492.952 / 22.440 / 2.770.666 / 1.771.962,899 · SEPI 98 / 77.728.024 /
  259.327 / 1.231.408 / 793.143,102 · MATI 1.401 / 579.041.399 / 97.634 / 451.875 /
  413.305,781 · `cacah_lain` 0 · `total_byte` 32.706.262.375.
- Delapan selisih invarian bebas + satu turunan; menyebut "sembilan pemeriksaan
  bebas" DILARANG (calon KC-50).
- **KOREKSI [v9]:** kalimat v8 yang menyebut MTLUSDT 2021-03, ENJUSDT 2020-09, dan
  SLPUSDT 2023-10 "tampak bulan tengah dan karena itu melawan H-A019" **DICABUT** —
  ketiganya terukur bulan PERTAMA. Yang melawan hanya TLMUSDT 2023-03 (ADR-A016
  kep. 4).

**LAMA [v7], tetap berlaku (`byte_semesta` V1 run 30526358811):** total byte semesta
32.706.262.375 atas 19.586 simbol-bulan; bagian byte MATI **0.017704**;
`cacah_byte_nol` 0 dan dasar keras ≈22 KB (KC-48); `cacah_lain` 0; kendali data tiga
BTCUSDT terbesar.

**LAMA [v6], tetap berlaku (`lubang_tebing` V1 run 30524631435):**

- Sebaran arah atas 118 simbol berlubang bukan-awal: `mati_dulu` **40** (0.339) ·
  `serempak` **78** (0.661) · `lubang_dulu` **0** (TERUKUR, kendali detektor sah).
- Tebing `2025-07` menguasai: 39 dari 118 (0.3305) dan **39 dari 40** `mati_dulu`
  (0.975). Satu-satunya `mati_dulu` bukan-tebing: **BTCSTUSDT**. KC-47.
- Pertanyaan terbuka: mengapa 39 simbol berhenti berfunding tepat `2025-07` padahal
  bulan MATI mereka tersebar 2022-12..2025-05? Dugaan BELUM diuji: `2025-07` batas
  penerbitan/arsip funding, bukan peristiwa pasar.
- 122 dari 787 simbol pernah berlubang funding (awal **5**, bukan-awal **118**,
  BNXUSDT keduanya). Lima bentuk AWAL: BNXUSDT, ICPUSDT, JUPUSDT, QTUMUSDT, TLMUSDT.
- **Delapan simbol bangkit (tetap):** CVCUSDT 29 · CVXUSDT 13 · SLPUSDT 13 ·
  CTKUSDT 11 · LITUSDT 10 · TLMUSDT 8 · ICPUSDT 2 · MAVIAUSDT 2 = 88.

**Lama, belum diukur (urut prioritas jurnal 130 §13):** (1) **APA ISI berkas bulan
MATI** — naik ke prioritas pertama, ditanyakan tiga giliran berturut, DILARANG
ditebak; (2) **TLMUSDT 2023-03**, satu-satunya kecil yang bukan pertama dan bukan
tepi; (3) apakah "bulan pertama di penyebut" sama dengan "bulan pertama di bursa";
(4) tebing funding `2025-07` (39 simbol) dan BTCSTUSDT; (5) irisan 880 lawan 877;
selisih 40−38 `diagnosa_kc15`; TANGGAL hari hilang BNX 2022-04/06/08; bentangan 38
kohort; H-A016 (celah kelipatan 15); mati_tersisip atas 19.586; `ukur_baris` V6;
R-7/19/20/28/36/37 dan R-199; R-236..R-247 dari jurnal 92–94; taksonomi lubang tiga
kelas.

## Penomoran berikutnya

Aturan resmi **1–81 dan 83** (aturan **83 DIRESMIKAN di STATE v49**) · calon **77**,
**78**, **82**, **84** (keempatnya belum resmi; **84** lahir sebagai usulan di
ADR-A016 kep. 3) · aturan berikutnya yang bebas **85** · KC sampai **KC-49**
(KC-16 kosong selamanya) · KC berikutnya **KC-50** (calon sudah ada: medan invarian
turunan) · Hipotesis terbuka H-A016 (belum diuji), H-A017 (dilemahkan R-306),
**H-A018** (DIUKUR dua kali, tafsir dibatasi ADR-A014 dan A015), **H-A019** (DIUJI
R-309, DITERIMA TERBATAS oleh ADR-A016 kep. 1) · Hipotesis berikutnya **H-A020** ·
Jurnal berikutnya **131** · STATE: `STATE.md` **v49** dan EKOR **v9** sudah didorong,
**UKUR v9 BELUM** (lihat peringatan keserasian versi di kepala berkas ini) · PROMPT
berikutnya **v53** · ADR berikutnya **A017** · Ramalan berikutnya **R-310** · papan
skor **309**.
