# STATE lampiran EKOR — bagian 2 dari STATE (v7, milik STATE v47)

**Mengapa berkas ini ada.** Dua push `STATE.md` berturut terpotong (v41, v42);
pemecahan ke tiga berkas berlaku sejak v43 (KC-42). Pembagian yang berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, KC-1..KC-48.
2. **`STATE_LAMPIRAN_EKOR.md`** (berkas ini, v7) — bagian 2: papan skor, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** — bagian 3: pengukuran, modul, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip lama; bukan sumber lagi.

Dasar v7: EKOR v6 (blob **`f3b2f5dd6c2dd58ec4ae438a6af9d3a65a69c5ed`**), dibaca UTUH
sebelum berkas ini ditulis.

**PERINGATAN KESERASIAN VERSI — dorongan BERTAHAP.** Saat berkas ini didorong,
`STATE.md` masih **v46** (blob `41b5b585`) dan `STATE_LAMPIRAN_UKUR.md` masih **v6**
(blob `27e59a79`). Keduanya menyusul pada giliran berikutnya, dibaca UTUH lebih dahulu.
Pemecahan ini SENGAJA: `push_files` menulis ulang seluruh berkas, sehingga menulis tiga
berkas besar dari satu konteks yang sudah terpakai banyak adalah cara paling pasti
merusak aturan 1–81 (KC-42, KC-43). Yang WAJIB diketahui pembaca sampai keduanya naik:
KC-48 dan aturan 82-yang-diusulkan belum tercantum di `STATE.md` v46, dan angka byte
R-307 belum tercantum di UKUR v6 — sumbernya sementara adalah
`journal/2026-07-30-128.md` dan `decisions/ADR-A014.md`.

**Tentang push berkas ini:** berkas ini berada di akar repo sehingga menyalakan
`ci.yml`. Tidak satu pun `tests/**` berubah, jadi cacah uji tetap **1100** — ramalan
deterministik (aturan 57), TIDAK masuk papan skor.

## KC-43..KC-48 (teks lengkap KC-43..KC-47 di STATE.md v46)

- **KC-43** — tanda tangan fungsi dari INGATAN. Penangkal: baca modul yang diimpor
  UTUH pada giliran yang sama.
- **KC-44** — semua laporan di-commit satu langkah. Penangkal: commit tiap berkas
  laporan sendiri-sendiri.
- **KC-45 [RESMI v45]** — satuan "bulan tanpa funding" vs "bulan MATI" dicampur.
- **KC-46 [RESMI v45]** — lubang bentuk AWAL dibaca sebagai "funding berhenti".
- **KC-47 [RESMI v46]** — satu peristiwa menyamar sebagai banyak pengamatan bebas
  (39 dari 40 `mati_dulu` berbagi tebing `2025-07`). Penangkal: aturan 81, ADR-A013.
- **KC-48 [RESMI v7 lampiran ini, teks penuh di jurnal 128 §6]** — **ambang absolut
  ditetapkan pada besaran yang sebarannya belum pernah diukur.** Sumber terukur:
  ambang 10.000 byte pada butir 2 R-307, sementara berkas TERKECIL di seluruh
  semesta 22.440 byte — tidak ada data yang mungkin lolos, sehingga butir itu tidak
  pernah menguji alam. Penangkal: ukur min/maks/rata (atau kuantil) lebih dahulu,
  atau pakai ambang RELATIF terhadap sebaran terukur (usulan aturan 82). Kerabat
  KC-20, KC-25, aturan 43.

## Papan skor prediksi — lengkap R-300..R-307 (R-199..R-299 di v4, blob `67dda29e`)

| # | Prediksi | Status |
|---|---|---|
| R-300 | (1) cacah_bulan 64; (2) tetangga BTCST HIDUP; (3) cacah_hidup 8..30 dan MATI>HIDUP | **SEPARUH** |
| R-301 | (1) tebing==0; (2) mati_tersisip ≥1; (3) bangkit==0 | **TIDAK TERADJUDIKASI** |
| R-302 | (1) simbol tersisip 1..10; (2) simbol-bulan 1..50; (3) penyebut 19.586/787 | **SEPARUH** (butir 2 MELESET 88>50) |
| R-303 | (1) simbol tersisip 1..60; (2) simbol-bulan 1..300; (3) penyebut/kendali/kode 0 | **TEPAT (3/3)** |
| R-304 | (1) mati_dulu 5..8; (2) hidup_berlubang 3..8; (3) penyebut/kendali/kode 0 | **MELESET** (1 dan 2 kalah) |
| R-305 | (1) bagian mati-tak-setelah-lubang dari ≥100 dalam 0.55..0.95; (2) cacah lubang-awal 20..120; (3) invarian + kendali + kode 0 + CI | **MELESET** — butir 1 KALAH (penyebut 118, bagian **1.0** > 0.95, tautologis aturan 10); butir 2 KALAH (cacah **5** < 20, aturan 41); butir 3 TEPAT (MUDAH) |
| R-306 | (1) bagian arah STRIKT dari penyebut ≥100 dalam 0.25..0.60; (2) cacah tebing 2025-07 dalam 20..90; (3) sembilan invarian + dua kendali + kode 0 + CI diukur | **TEPAT (3/3)** — butir 1 **0.339** (penyebut **118**) MENANG; butir 2 **39** MENANG; butir 3 MENANG (MUDAH) |
| R-307 | (1) bagian byte parquet simbol-bulan MATI atas TOTAL byte 19.586 dalam 0.02..0.15; (2) cacah simbol-bulan TERUKUR (HIDUP/SEPI) ber-`byte_parquet` < 10.000 dalam 20..400; (3) sembilan invarian nol + dua kendali sah + kode 0 + CI diukur | **MELESET** — butir 1 KALAH (**0.017704**, di bawah pita 0.02; arah H-A018 justru didukung); butir 2 KALAH (**0**, dan ambangnya mustahil — dasar semesta 22.440 byte, KC-48); butir 3 MENANG (MUDAH) |

**Total R-1..R-307** (dihitung tangan, aturan 21). Dasar v6 (papan skor R-1..R-306):
TEPAT 215 · MELESET 56 · SEPARUH 20 · TIDAK TERADJUDIKASI 8 · MENUNGGU 7 = 306.

Sesudah v6: **R-307 MELESET**.

- TEPAT **215**
- MELESET 56 + 1 = **57**
- SEPARUH **20**
- TIDAK TERADJUDIKASI **8**
- MENUNGGU **7** (R-7, R-19, R-20, R-28, R-36, R-37, R-199)

215 + 57 + 20 + 8 + 7 = **307** ✅ Nomor terpakai R-1..R-307, seluruhnya
teradjudikasi atau menunggu. N_percobaan = 0. **ADJUDIKASI RISET TETAP TERKUNCI.**
Ramalan berikutnya **R-308** (praregistrasi sudah di jurnal 128 §9), lalu **R-309**.

**Utang papan skor:** rincian R-236..R-247 masih di jurnal 92–94; R-229 TEPAT dan
R-230 MELESET (dari docstring) menunggu pemeriksaan R-224..R-235.

## Catatan kejujuran [v7]

**R-307 MELESET — dan kedua kekalahannya BERBEDA JENIS. Menyamakannya menyesatkan.**

1. **Butir 1 kalah karena aritmetika saya, bukan karena alam.** Terukur 0.017704
   lawan pita 0.02–0.15 — gagal tipis di ambang bawah. Tetapi ARAH yang diramalkan
   terbukti kuat: bulan MATI adalah 7,153% BARIS (1.401/19.586) namun hanya **1,77%**
   BYTE, dengan rata 413.306 lawan HIDUP 1.771.963 (≈**4,3×** lebih kecil). Angka
   1,7% itu DAPAT dihitung sebelum run dari dua besaran yang sudah ada di tangan
   (7,15% / 4,3 ≈ 1,7%), dan saya tidak menghitungnya. Pita TIDAK dilebarkan sesudah
   pengukuran (aturan 29); MELESET tetap MELESET.
2. **Butir 2 tidak pernah menguji apa pun.** Ambang 10.000 byte terletak DI BAWAH
   dasar semesta: `byte_min` seluruh 19.586 = **22.440**, `cacah_byte_nol` = 0. Tidak
   ada data yang mungkin lolos, jadi pita 20..400 mustahil terpenuhi. Ini **KC-48**
   dan sebab **usulan aturan 82**. Kegagalan jenis ini tidak mengajarkan apa pun
   tentang alam, hanya tentang kelalaian saya.
3. **Nol pada butir 2 tetap sah disebut TERUKUR, bukan buta.** `kendali_deteksi_sah`
   true: bentangan buatan memisahkan dua baris berbyte kecil (5 dan 10) dari baris
   tepat DI AMBANG (tidak terhitung — perbandingan strikt) dan dari baris kelas LAIN
   berbyte kecil (tidak masuk butir 2). Detektornya MAMPU melihat; semestanya yang
   tidak punya (aturan 50, KC-21). Pelajaran R-305 terpakai.
4. **Temuan yang MELAWAN tafsir mudah, dan wajib dikutip bersama setiap klaim
   H-A018:** HIDUP `byte_min` **22.440** < MATI `byte_min` **97.634**. Berkas
   TERKECIL di semesta milik bulan **HIDUP**, lebih kecil daripada SETIAP bulan MATI.
   Kedua kelas beririsan, dan irisannya di ujung yang berlawanan dengan dugaan.
   H-A018 boleh berbunyi "MATI rata-rata jauh lebih kecil"; DILARANG berbunyi "kecil
   berarti mati". Besar berkas DILARANG dipakai sebagai detektor status (kerabat
   KC-38). Lihat ADR-A014 keputusan 2.
5. **Butir 3 MENANG dan wajib disebut MUDAH** (deterministik): sembilan selisih
   invarian nol, `kendali_sah` true, `kendali_deteksi_sah` true, kode keluar 0, CI
   **1100 diukur** bukan diklaim.
6. **Yang membuat R-307 lebih berharga daripada kemenangan R-306:** tidak satu pun
   angkanya dapat runtuh menjadi artefak tebing `2025-07`. KC-47 tidak berlaku di
   sini karena byte parquet diukur dari berkas data, bukan dari daftar tanggal
   funding. Perpindahan poros itu memang tujuannya, dan ia berhasil.

**Kesalahan proses giliran ini:** tidak ada kegagalan konektor; seluruh `push_files`
dan `get_file_contents` berhasil sekali jalan. Kesalahan substantifnya justru pada
PRAREGISTRASI, bukan pada pelaksanaan — lihat butir 1 dan 2 di atas. Satu hal yang
BERJALAN BENAR dan patut dicatat: laporan `byte_semesta` sengaja dirancang ringkas
(`BATAS_BARIS_LAPORAN` 40) karena `lubang_tebing.json` dulu terpotong, dan kali ini
laporan terbaca **UTUH** — usulan aturan 78 terbukti berguna.

## Jumlah uji

**1100 TERUKUR [v7].** `reports/ci_terakhir.json` (blob
**`0765ce7b7d443be72d34ae24d7f70ef6e8cf6bd7`**): run **30526358010**, commit
**`d3bc20399361058bdcbfd0b2dc33c613717a561f`**, 2026-07-30T08:21:45Z, `kode_keluar` 0,
**"1100 tests collected in 0.56s"**. Turunan: 1044 + **56** butir
`tests/test_byte_semesta.py` = **1100** ✅ (aturan 21).

Riwayat panjang: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 →
984 → 1044 → **1100**.

Cacah per berkas uji (yang diketahui): `test_bentangan_kohort.py` V2 **63** ·
`test_lubang_tebing.py` **60** · `test_sebab_bangkit.py` **57** ·
**`test_byte_semesta.py` 56** (`test_01`..`test_56`, dicacah mata pada berkas yang
sudah di main) · `test_lubang_awal.py` **48** · `test_tersisip_semesta.py` **47** ·
`test_anatomi_tengah.py` 47 · `test_terhenti.py` V4 33 · `test_bulan_absen.py` 32 ·
`test_karantina_semesta.py` 28 · `test_silang_settled.py` 24. Aturan 57 kini **dua
puluh enam dari dua puluh enam**.

Aturan 38 (cacah uji HANYA dari `ci_terakhir.json`): pemakaian ke-**tiga puluh dua**.

## Utang verifikasi

1-5, 11 menunggu tahap juri. 6-23, 25-28 LUNAS. **Nomor utang BUKAN nomor
ramalan — KC-32.**

24. **AKTIF.** Lunas lama seperti v6. **LUNAS BARU [v7]:**
    - **Trio `byte_semesta` V1 dibaca ulang UTUH dari main** sesudah push `d3bc2039`
      (aturan 52, 55): `lux_ai/serapan/byte_semesta.py` (`ff68e4be`),
      `tests/test_byte_semesta.py` (`0e1e3ab2`, 56 butir dicacah mata),
      `.github/workflows/byte_semesta.yml` (`45650ff9`, `paths` benar-benar SATU entri).
    - `reports/byte_semesta.json` (`8b7f2077`) terbaca **UTUH** — bukan 99% seperti
      `lubang_tebing.json`; rancangan ringkas berhasil. `_status.json` (`2cbcbc1b`)
      dan `ci_terakhir.json` (`0765ce7b`) terbaca utuh.
    - Jurnal 128 (`13c06f61`) dan ADR-A014 (`6d77c2cd`) dibaca ulang UTUH sesudah push.
    - **`silang_funding.py` V2 (`42c3aa9d`) dan `lubang_awal.py` V1 (`8c36943d`)
      dibaca UTUH** sebelum modul R-307 ditulis — KC-43 lunas; tanda tangan tiga-nilai
      `baca_laporan_kehidupan` terverifikasi dari berkas, bukan dari ingatan.
    - `.github/workflows/lubang_awal.yml` (`3134bc9f`) dibaca UTUH (aturan 55).
    - **Cacah tangan tiga direktori** pada ref `d73b07b9` (aturan 66): `tests/` **48**,
      `lux_ai/serapan/` **44**, `.github/workflows/` **39** — dinomori satu per satu.
      Angka turunan 48 TERBUKTI benar; tidak ada drift seperti v44 (45 lawan 47).
    - EKOR v6 (`f3b2f5dd`) dibaca UTUH sebelum berkas ini ditulis.
    **TETAP BELUM:** `tests/test_bentangan_kohort.py` V2 (63 butir, blob
    `9f850ecd`) belum dibaca ulang byte demi byte; seluruh daftar BELUM dari v4/v5
    masih berlaku (`ADR-A002`, A004, A006, A007, A008, `PETA_MODUL.md`,
    `PETA_MODUL_BERKAS.md`, `STATE_LAMPIRAN.md`, `STATE_LAMPIRAN_ANGKA.md`,
    `karantina_semesta.yml`, `test_pulihkan.py`, `test_rilis_karantina.py`,
    `test_karantina_a006.py`).

## Daftar ADR

- **ADR-A001** aturan dasar. DITERIMA.
- **ADR-A002** serapan. Kondisi v3 berlaku; §10 tetap tidak boleh diubah.
- **ADR-A003** taksonomi rezim. BELUM ADA. Wajib memuat delapan simbol bangkit,
  koreksi ADR-A011/A012/A013/A014, bentangan LITUSDT, bulan ABSEN, aturan 76, KC-40.
- **ADR-A004** kebijakan KC-6. DITERIMA.
- **ADR-A005** jenis instrumen. DITERIMA.
- **ADR-A006** karantina + persistensi. DITERIMA, TERVERIFIKASI.
- **ADR-A007** serapan hibrida. DIUSULKAN, belum diterima.
- **ADR-A008** akibat KC-18. Keputusan 1–6 DITERIMA. **Keputusan 7 DITANGGUHKAN.**
  Prasyarat tersisa: bentangan kehidupan 38 kohort puncak.
- **ADR-A009** (commit `17a594b6`) — arah sebab "kematian mendahului hilangnya
  funding". **DICABUT PENUH oleh ADR-A012.**
- **ADR-A010** (commit `c4bccf21`) — klaim "kebangkitan tunggal" DICABUT. DITERIMA.
- **ADR-A011** (commit `645fd5df`) — arah sebab A009 DICABUT untuk kelas bangkit.
  DITERIMA.
- **ADR-A012** (commit `f9f564d1`) — arah sebab A009 DICABUT untuk SELURUH semesta;
  butir 1 R-305 (1.0) ARTEFAK TAUTOLOGIS. DITERIMA.
- **ADR-A013** (commit `8ba4f989`, giliran R-306) — **klaim arah waktu wajib dipilah
  tebing lawan bukan-tebing.** Lima keputusan; (2) dan (4) kini aturan **80** dan
  **81**. **DITERIMA.**
- **ADR-A014** (commit `69bfdd5d`, blob `6d77c2cd`, giliran R-307) — **byte parquet:
  arah H-A018 didukung, pita gugur, dan "kecil" BUKAN penanda mati.** Enam keputusan:
  (1) R-307 dicatat MELESET, dilarang diselamatkan dengan melebarkan pita; (2) H-A018
  TIDAK dicabut tetapi dibatasi — boleh berbunyi soal RATA-RATA (413.306 lawan
  1.771.963), dilarang dipakai sebagai detektor status karena HIDUP `byte_min` 22.440
  < MATI `byte_min` 97.634; (3) nol butir 2 sah disebut TERUKUR karena kendali
  detektor sah; (4) bulan MATI bukan bulan KOSONG (`byte_min` 97.634, `cacah_byte_nol`
  0) — ISI berkasnya belum diukur dan dilarang ditebak; (5) ambang absolut wajib
  bersandar pada sebaran terukur → KC-48 resmi, aturan 82 diusulkan; (6) ADR-A012 dan
  A013 TETAP berlaku, R-307 tidak menyentuh soal arah sebab. **DITERIMA.**
- **ADR berikutnya A015.**

## Temuan sampingan

**BARU [v7], terukur (`byte_semesta` V1 run 30526358811, commit `d3bc2039`, kode 0,
laporan blob `8b7f2077`, sidik kode `e02aca2b…`):**

- **Total byte parquet seluruh semesta = 32.706.262.375** (~32,7 GB) atas 19.586
  simbol-bulan. Ini penjumlahan PERTAMA besaran itu atas semesta penuh.
- Sebaran per status (byte_min / byte_maks / byte_rata):
  - **HIDUP** cacah 18.087 · byte 32.049.492.952 · **22.440** / 2.770.666 / 1.771.963
  - **SEPI** cacah 98 · byte 77.728.024 · 259.327 / 1.231.408 / 793.143
  - **MATI** cacah 1.401 · byte **579.041.399** · **97.634** / **451.875** / **413.306**
- **Bagian byte MATI = 0.017704** (butir 1 R-307, KALAH tipis di bawah 0.02).
- **`cacah_terukur_byte_kecil` (< 10.000) = 0**, dan `cacah_byte_nol` = **0** atas
  seluruh semesta → ada **dasar keras** ukuran berkas ≈ 22 KB. KC-48.
- **`cacah_lain` = 0:** seluruh 19.586 berstatus MATI/SEPI/HIDUP, tidak ada
  TAK_TERUKUR. 18.087 + 98 = 18.185 TERUKUR, + 1.401 = 19.586 ✅
- Kendali data (aturan 50): tiga simbol-bulan berparquet terbesar seluruhnya
  **BTCUSDT** (2021-05 2.770.666 · 2021-08 2.730.341 · 2021-01 2.722.266), semuanya
  HIDUP dan berfunding — `kendali_sah` true.
- Pengamatan LITUSDT lama (MATI ~390–434 ribu lawan HIDUP ~1,6–1,9 juta) ternyata
  **mewakili semesta dengan baik** (rata MATI 413.306, rata HIDUP 1.771.963).
- Sidik COCOK dengan run sebelumnya (aturan 36) → semesta sama: laporan kehidupan
  `24b6bb26…`, `sidik_data_funding` `2c9fbd1b…`, `silang_funding` `8a9b859c…`,
  `lubang_awal` `156499ce…`.
- **Pertanyaan baru yang lahir dan BELUM diukur:** (a) berapa lebar zona irisan —
  cacah bulan HIDUP yang lebih kecil daripada bulan MATI terkecil (butir 1 R-308);
  (b) APA ISI berkas bulan MATI, karena ia berisi (97.634 byte) tetapi ringan — lilin
  berulang? volume nol? Dilarang ditebak.

**LAMA [v6], tetap berlaku (`lubang_tebing` V1 run 30524631435):**

- Sebaran arah atas 118 simbol berlubang bukan-awal: `mati_dulu` **40** (0.339) ·
  `serempak` **78** (0.661) · `lubang_dulu` **0** (TERUKUR, kendali detektor sah).
- Tebing `2025-07` menguasai: 39 dari 118 (0.3305) dan **39 dari 40** `mati_dulu`
  (0.975). Satu-satunya `mati_dulu` bukan-tebing: **BTCSTUSDT** (lubang bukan-awal
  pertama 2022-01, MATI pertama 2021-04, `cacah_mati` 63). KC-47.
- Contoh anggota tebing: AGIX, ALPACA, AMB, BADGER, BAL, BLZ, BNX, COMBO, DAR, DGB,
  FTM, FTT, GLMR, IDEX, KEY, KLAY, LINA, LIT, LOOM, MDT, NULS, OCEAN, OMG, ORBS, RAD,
  RAY, REEF, REN, SC, SNT, STMX, STPT, STRAX, TROY, UNFI, VIDT, WAVES, XEM.
- Pertanyaan terbuka: mengapa 39 simbol berhenti berfunding tepat `2025-07` padahal
  bulan MATI mereka tersebar 2022-12..2025-05? Dugaan BELUM diuji: `2025-07` batas
  penerbitan/arsip funding, bukan peristiwa pasar.
- 122 dari 787 simbol pernah berlubang funding (awal **5**, bukan-awal **118**,
  BNXUSDT keduanya). Lima bentuk AWAL: BNXUSDT, ICPUSDT, JUPUSDT, QTUMUSDT, TLMUSDT;
  ICP dan TLM lubang awalnya melewati kematian (KC-46).
- **Delapan simbol bangkit (tetap):** CVCUSDT 29 · CVXUSDT 13 · SLPUSDT 13 ·
  CTKUSDT 11 · LITUSDT 10 · TLMUSDT 8 · ICPUSDT 2 · MAVIAUSDT 2 = 88. Lima tanpa
  lubang; LITUSDT satu-satunya `mati_dulu` (+5).

**Lama, belum diukur:** irisan 880 lawan 877; TANGGAL hari hilang BNX 2022-04/06/08;
selisih 40−38 `diagnosa_kc15`; H-A016 (celah kelipatan 15); mati_tersisip atas
19.586; bentangan 38 kohort; `ukur_baris` V6; R-7/19/20/28/36/37 dan R-199;
R-236..R-247 dari jurnal 92–94; **taksonomi lubang tiga kelas (awal / delisting /
tebing)** — naik prioritas karena ADR-A013.

## Penomoran berikutnya

Aturan sampai **81** (resmi) · calon **77**, **78**, **82** (ketiganya TETAP belum
resmi; 82 lahir sebagai usulan di jurnal 128 §7) · KC sampai **KC-48** (KC-48 kini
RESMI; KC-16 kosong selamanya) · Hipotesis terbuka H-A016 (belum diuji), H-A017
(arah sebab, dicabut sebagai pola), **H-A018** (byte parquet — DIUKUR, arah didukung,
tafsir dibatasi ADR-A014) · Hipotesis berikutnya **H-A019** · Jurnal berikutnya
**129** · STATE: `STATE.md` **v47** dan UKUR **v7** BELUM didorong (lihat peringatan
keserasian versi di kepala berkas ini) · PROMPT berikutnya **v51** · ADR berikutnya
**A015** · Ramalan berikutnya **R-308** (praregistrasi sudah di jurnal 128 §9), lalu
**R-309** · papan skor **307**.
