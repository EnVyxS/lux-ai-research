# STATE lampiran EKOR — bagian 2 dari STATE (v6, milik STATE v46)

**Mengapa berkas ini ada.** Dua push `STATE.md` berturut terpotong (v41, v42);
pemecahan ke tiga berkas berlaku sejak v43 (KC-42). Pembagian yang berlaku:

1. **`STATE.md` v46** — bagian 1: kepala, aturan 1–81, KC-1..KC-47.
2. **`STATE_LAMPIRAN_EKOR.md`** (berkas ini, v6) — bagian 2: papan skor, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** v6 — bagian 3: pengukuran, modul, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip lama; bukan sumber lagi.

Dasar v6: EKOR v5 (blob **`fe45f8b483db019873698f605a9aded4f0f229af`**), dibaca UTUH
sebelum berkas ini ditulis.

**Tentang push berkas ini:** berkas ini berada di akar repo sehingga menyalakan
`ci.yml`. Tidak satu pun `tests/**` berubah, jadi cacah uji tetap **1044** — ramalan
deterministik (aturan 57), TIDAK masuk papan skor.

## KC-43..KC-47 (teks lengkap di STATE.md v46)

- **KC-43** — tanda tangan fungsi dari INGATAN. Penangkal: baca modul yang diimpor
  UTUH pada giliran yang sama.
- **KC-44** — semua laporan di-commit satu langkah. Penangkal: commit tiap berkas
  laporan sendiri-sendiri.
- **KC-45 [RESMI v45]** — satuan "bulan tanpa funding" vs "bulan MATI" dicampur.
- **KC-46 [RESMI v45]** — lubang bentuk AWAL dibaca sebagai "funding berhenti".
- **KC-47 [RESMI v46]** — satu peristiwa menyamar sebagai banyak pengamatan bebas
  (39 dari 40 `mati_dulu` berbagi tebing `2025-07`). Penangkal: aturan 81, ADR-A013.

## Papan skor prediksi — lengkap R-300..R-306 (R-199..R-299 di v4, blob `67dda29e`)

| # | Prediksi | Status |
|---|---|---|
| R-300 | (1) cacah_bulan 64; (2) tetangga BTCST HIDUP; (3) cacah_hidup 8..30 dan MATI>HIDUP | **SEPARUH** |
| R-301 | (1) tebing==0; (2) mati_tersisip ≥1; (3) bangkit==0 | **TIDAK TERADJUDIKASI** |
| R-302 | (1) simbol tersisip 1..10; (2) simbol-bulan 1..50; (3) penyebut 19.586/787 | **SEPARUH** (butir 2 MELESET 88>50) |
| R-303 | (1) simbol tersisip 1..60; (2) simbol-bulan 1..300; (3) penyebut/kendali/kode 0 | **TEPAT (3/3)** |
| R-304 | (1) mati_dulu 5..8; (2) hidup_berlubang 3..8; (3) penyebut/kendali/kode 0 | **MELESET** (1 dan 2 kalah) |
| R-305 | (1) bagian mati-tak-setelah-lubang dari ≥100 dalam 0.55..0.95; (2) cacah lubang-awal 20..120; (3) invarian + kendali + kode 0 + CI | **MELESET** — butir 1 KALAH (penyebut 118, bagian **1.0** > 0.95, tautologis aturan 10); butir 2 KALAH (cacah **5** < 20, aturan 41); butir 3 TEPAT (MUDAH) |
| R-306 | (1) bagian arah STRIKT dari penyebut ≥100 dalam 0.25..0.60; (2) cacah tebing 2025-07 dalam 20..90; (3) sembilan invarian + dua kendali + kode 0 + CI diukur | **TEPAT (3/3)** — butir 1 **0.339** (penyebut **118**) MENANG; butir 2 **39** MENANG; butir 3 MENANG (MUDAH) |

**Total R-1..R-306** (dihitung tangan, aturan 21). Dasar v5 (papan skor R-1..R-305):
TEPAT 214 · MELESET 56 · SEPARUH 20 · TIDAK TERADJUDIKASI 8 · MENUNGGU 7 = 305.

Sesudah v5: **R-306 TEPAT**.

- TEPAT 214 + 1 = **215**
- MELESET **56**
- SEPARUH **20**
- TIDAK TERADJUDIKASI **8**
- MENUNGGU **7** (R-7, R-19, R-20, R-28, R-36, R-37, R-199)

215 + 56 + 20 + 8 + 7 = **306** ✅ Nomor terpakai R-1..R-306, seluruhnya
teradjudikasi atau menunggu. N_percobaan = 0. **ADJUDIKASI RISET TETAP TERKUNCI.**
Ramalan berikutnya **R-307** (praregistrasi sudah di jurnal 127 §7), lalu **R-308**.

**Utang papan skor:** rincian R-236..R-247 masih di jurnal 92–94; R-229 TEPAT dan
R-230 MELESET (dari docstring) menunggu pemeriksaan R-224..R-235.

## Catatan kejujuran [v6]

**R-306 TEPAT 3/3 — dan justru kemenangan inilah yang paling wajib dikecilkan.**

1. Butir 1 MENANG dengan bagian **0.339** di dalam pita 0.25..0.60, penyebut 118
   (≥100). Pitanya jujur, ditulis sebelum modulnya ada (aturan 79). Tetapi klaim
   ilmiah yang boleh ditarik darinya **hampir kosong**: 39 dari 40 anggota numerator
   berbagi satu bulan tebing `2025-07`. Bukti arah yang lepas dari tebing = **satu
   simbol** (BTCSTUSDT, lubang bukan-awal pertama 2022-01, MATI pertama 2021-04).
   Ini kelas cacat baru **KC-47** dan sebab lahirnya **aturan 81**.
2. Butir 2 MENANG (cacah tebing **39**, pita 20..90). Kemenangan ini sah, dan ia
   justru yang menelanjangi butir 1.
3. Butir 3 MENANG dan wajib disebut **MUDAH** (deterministik): sembilan selisih
   invarian nol, `kendali_sah` true, `kendali_deteksi_sah` true, kode keluar 0, CI
   1044 **diukur** bukan diklaim.
4. **Yang membuat R-306 lebih layak dipercaya daripada R-305:** `lubang_dulu` = 0
   kini nol yang TERUKUR, bukan nol yang buta — `kendali_deteksi` membuktikan kelas
   itu terlihat pada bentangan buatan (aturan 50, KC-21). Dan angka 1.0 milik R-305
   kini terurai tersurat: 118 = 40 + 78, dua pertiganya kelas `serempak`. ADR-A012
   terbukti benar secara aritmetika, bukan hanya secara tafsir.

**Kesalahan proses giliran ini:**
1. **KC-41 dua kali, keduanya pada dokumen kami sendiri** (rincian di STATE.md v46):
   lampiran UKUR v5 salah mengutip `paths` `lubang_awal.yml` (tiga entri, seharusnya
   satu); PROMPT v49 salah melabeli poros R-307 sebagai H-A017 (seharusnya hipotesis
   baru **H-A018**). Keduanya tertangkap HANYA karena berkas sumber dibaca utuh.
2. Penomoran aturan hampir ditetapkan dari ingatan. Jurnal 127 §9 sengaja menahannya;
   pembacaan v45 utuh menunjukkan 77/78 masih USULAN dan 79 sudah BERLAKU, sehingga
   aturan baru sah bernomor **80** dan **81**. Penahanan itu terbukti benar.
3. Nama modul R-306 harus dipindah dari `lubang_tengah` ke `lubang_tebing` karena
   pencacahan tangan (aturan 66) mengungkap `lubang_tengah.py` (`4d3beaf1`) dan
   `lubang_tengah.yml` (`557030de`) SUDAH ADA. Tanpa aturan 66, satu modul akan
   tertimpa dalam sunyi.
4. `reports/lubang_tebing.json` **terpotong** saat dibaca (batas ±30.000 token,
   "showing 99%"). Yang hilang hanya sebagian daftar `baris_tebing`/`baris_mati_dulu`;
   seluruh `ringkasan` dan `uji_r306` terbaca, jadi adjudikasi tetap sah (aturan 52
   terpenuhi untuk bagian yang diklaim). Dicatat agar laporan berikutnya dirancang
   lebih ringkas — dasar usulan aturan 78.

## Jumlah uji

**1044 TERUKUR [v6].** `reports/ci_terakhir.json` (blob `0c104b18`) pada commit
`84b11164`: run **30524631516**, commit
**`84b111647449d44af519c54f170a2de59c2bf904`**, 2026-07-30T07:56:28Z, `kode_keluar`
0, **"1044 tests collected in 0.61s"**. Turunan: 984 + **60** butir
`tests/test_lubang_tebing.py` = **1044** ✅ (aturan 21).

Riwayat panjang: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 →
984 → **1044**.

Cacah per berkas uji (yang diketahui): `test_lubang_tebing.py` **60** ·
`test_lubang_awal.py` **48** · `test_sebab_bangkit.py` **57** ·
`test_tersisip_semesta.py` **47** · `test_bentangan_kohort.py` V2 **63** ·
`test_anatomi_tengah.py` 47 · `test_terhenti.py` V4 33 · `test_silang_settled.py` 24 ·
`test_bulan_absen.py` 32 · `test_karantina_semesta.py` 28. Aturan 57 kini **dua puluh
lima dari dua puluh lima**.

## Utang verifikasi

1-5, 11 menunggu tahap juri. 6-23, 25-28 LUNAS. **Nomor utang BUKAN nomor
ramalan — KC-32.**

24. **AKTIF.** Lunas lama seperti v5. **LUNAS BARU [v6]:**
    - `lubang_tebing.py` V1 (`575e777e`), `test_lubang_tebing.py` (`bf57d69d`, 60
      butir, `test_01`..`test_60` dicacah mata), `lubang_tebing.yml` (`c8ae552a`)
      dibaca ulang UTUH dari main sesudah push `84b11164` (aturan 52, 55).
    - `reports/lubang_tebing_status.json` (`685191e1`) dan `reports/ci_terakhir.json`
      (`0c104b18`) terbaca UTUH. `reports/lubang_tebing.json` (`7d8883f5`) terbaca
      99% — seluruh `ringkasan` dan `uji_r306` terbaca, ekor daftar terpotong.
    - Jurnal 127 (`9b5015eb`), ADR-A013 (`3a7f8612`), PROMPT v49 (`4dca042c`) dibaca
      ulang UTUH sesudah push.
    - **Ketiga berkas STATE v45 dibaca UTUH** (`e07f2de1`, `fe45f8b4`, `eb826817`)
      sebelum v46 ditulis — dan pembacaan itu menangkap dua kasus KC-41.
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
  koreksi ADR-A011/A012/A013, bentangan LITUSDT, bulan ABSEN, aturan 76, KC-40.
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
  tebing lawan bukan-tebing.** Keputusan: (1) setiap klaim arah dilapor dua kolom
  di-tebing / bukan-tebing, angka gabungan tidak boleh dikutip sendirian; (2) kelas
  `serempak` tidak pernah masuk numerator, perbandingan wajib STRIKT; (3) kekuatan
  bukti lepas-tebing dinyatakan apa adanya = **satu simbol** atas 118; (4) numerator
  yang dikuasai satu bulan ≥1/4 wajib dilapor per bulan; (5) ADR-A012 TETAP berlaku,
  R-306 tidak memulihkan A009. **DITERIMA.** Keputusan (2) dan (4) kini diresmikan
  sebagai **aturan 80 dan 81**.
- **ADR berikutnya A014.**

## Temuan sampingan

**BARU [v6], terukur (`lubang_tebing` V1 run 30524631435, commit `84b11164`, kode 0):**

- **Sebaran arah atas 118 simbol** (penyebut = simbol berlubang bukan-awal):
  `mati_dulu` **40** (bagian **0.339**) · `serempak` **78** (0.661) ·
  `lubang_dulu` **0** (0.000, TERUKUR karena kendali detektor sah).
- **Tebing `2025-07` menguasai kelas arah:** `bulan_lubang_bukan_awal_pertama` ==
  `2025-07` untuk **39** dari 118 simbol (bagian 0.3305), dan untuk **39 dari 40**
  anggota `mati_dulu` (0.975). Satu-satunya `mati_dulu` bukan-tebing: **BTCSTUSDT**
  (lubang bukan-awal pertama 2022-01, MATI pertama 2021-04, `cacah_mati` 63).
- Contoh anggota tebing (dari daftar laporan, dibatasi `BATAS_BARIS_LAPORAN` 60):
  AGIX, ALPACA, AMB, BADGER, BAL, BLZ, BNX, COMBO, DAR, DGB, FTM, FTT, GLMR, IDEX,
  KEY, KLAY, LINA, LIT, LOOM, MDT, NULS, OCEAN, OMG, ORBS, RAD, RAY, REEF, REN, SC,
  SNT, STMX, STPT, STRAX, TROY, UNFI, VIDT, WAVES, XEM (semua bersufiks USDT).
- **Pertanyaan baru yang lahir dan BELUM diukur:** mengapa 39 simbol berhenti
  berfunding tepat `2025-07` padahal bulan MATI mereka tersebar 2022-12..2025-05
  (banyak ber-`cacah_lubang` tepat 12 = 2025-07..2026-06)? Dan mengapa BTCSTUSDT
  satu-satunya yang lepas dari tebing? Dugaan yang BELUM diuji: `2025-07` adalah
  batas penerbitan/arsip data funding, bukan peristiwa pasar.
- `sidik_kode` `lubang_tebing` V1 =
  `4a5c2e4279eb1554dc119b48d6a8db61f6ea4ee11b7539efd70ee71d1ae18bf3`; sidik
  `lubang_awal` (`156499ce…`), `silang_funding` (`8a9b859c…`) dan `sidik_data_funding`
  (`2c9fbd1b…`) COCOK dengan laporan sebelumnya (aturan 36) → semesta sama.

**Lama, tetap berlaku:** 122 dari 787 simbol pernah berlubang funding (awal **5**,
bukan-awal **118**, BNXUSDT keduanya). Lima bentuk AWAL: BNXUSDT, ICPUSDT, JUPUSDT,
QTUMUSDT, TLMUSDT; ICP dan TLM lubang awalnya melewati kematian (KC-46).

**Delapan simbol bangkit (tetap):** CVCUSDT 29 · CVXUSDT 13 · SLPUSDT 13 ·
CTKUSDT 11 · LITUSDT 10 · TLMUSDT 8 · ICPUSDT 2 · MAVIAUSDT 2 = 88. Lima tanpa
lubang; LITUSDT satu-satunya `mati_dulu` (+5).

**Lama, belum diukur:** irisan 880 lawan 877; TANGGAL hari hilang BNX 2022-04/06/08;
selisih 40−38 `diagnosa_kc15`; H-A016 (celah kelipatan 15); mati_tersisip atas
19.586; bentangan 38 kohort; `ukur_baris` V6; R-7/19/20/28/36/37 dan R-199;
R-236..R-247 dari jurnal 92–94; **taksonomi lubang tiga kelas (awal / delisting /
tebing)** — naik prioritas karena ADR-A013.

## Penomoran berikutnya

Aturan sampai **81** (resmi; **80** dan **81** lahir di v46) · calon **77**, **78**
(TETAP belum resmi) · KC sampai **KC-47** (KC-47 kini RESMI; KC-16 kosong selamanya)
· Hipotesis terbuka H-A016 (belum diuji), H-A017 (arah sebab, dicabut sebagai pola),
**H-A018** (byte parquet, BARU — poros R-307) · Jurnal berikutnya **128** · STATE
berikutnya **v47** · PROMPT berikutnya **v50** · ADR berikutnya **A014** · Ramalan
berikutnya **R-307** (praregistrasi sudah di jurnal 127 §7), lalu **R-308** · papan
skor **306**.
