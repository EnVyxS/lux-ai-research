# STATE lampiran EKOR — bagian 2 dari STATE (v8, milik STATE v48)

**Mengapa berkas ini ada.** Dua push `STATE.md` berturut terpotong (v41, v42);
pemecahan ke tiga berkas berlaku sejak v43 (KC-42). Pembagian yang berlaku:

1. **`STATE.md`** — bagian 1: kepala, aturan 1–81, KC-1..KC-49.
2. **`STATE_LAMPIRAN_EKOR.md`** (berkas ini, v8) — bagian 2: papan skor, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** — bagian 3: pengukuran, modul, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip lama; bukan sumber lagi.

Dasar v8: EKOR v7 (blob **`9e906dfbb630c510d412a0a676ad2125b37b88b4`**), dibaca UTUH
sebelum berkas ini ditulis.

**PERINGATAN KESERASIAN VERSI — dorongan BERTAHAP.** Saat berkas ini didorong,
`STATE.md` masih **v47** (blob `7642b75d0ba7cd8612d83c3a43bff1274d8cac57`) dan
`STATE_LAMPIRAN_UKUR.md` masih **v7** (blob pendek `4e7fb65b`; empat puluh karakter
penuhnya BELUM pernah dicatat — jangan mengarang, baca dari main). Keduanya menyusul
pada giliran berikutnya, dibaca UTUH lebih dahulu. Pemecahan ini SENGAJA: `push_files`
menulis ulang seluruh berkas, sehingga menulis tiga berkas besar dari satu konteks
yang sudah terpakai banyak adalah cara paling pasti merusak aturan 1–81 (KC-42,
KC-43). Yang WAJIB diketahui pembaca sampai keduanya naik: **KC-49, ADR-A015, dan
usulan aturan 83 belum tercantum di `STATE.md` v47**, dan **angka R-308 belum
tercantum di UKUR v7** — sumbernya sementara adalah `journal/2026-07-30-129.md`
(blob `ecb6ac241d84f06767195f931f8418fa1c853ba2`) dan `decisions/ADR-A015.md`
(blob `387d551051da4f0d539f7c9c26e438a9ac84c9a3`).

**Tentang push berkas ini:** berkas ini berada di akar repo sehingga menyalakan
`ci.yml`. Tidak satu pun `tests/**` berubah, jadi cacah uji tetap **1168** — ramalan
deterministik (aturan 57), TIDAK masuk papan skor.

## KC-43..KC-49 (teks lengkap KC-43..KC-47 di STATE.md v47)

- **KC-43** — tanda tangan fungsi dari INGATAN. Penangkal: baca modul yang diimpor
  UTUH pada giliran yang sama.
- **KC-44** — semua laporan di-commit satu langkah. Penangkal: commit tiap berkas
  laporan sendiri-sendiri.
- **KC-45 [RESMI v45]** — satuan "bulan tanpa funding" vs "bulan MATI" dicampur.
- **KC-46 [RESMI v45]** — lubang bentuk AWAL dibaca sebagai "funding berhenti".
- **KC-47 [RESMI v46]** — satu peristiwa menyamar sebagai banyak pengamatan bebas
  (39 dari 40 `mati_dulu` berbagi tebing `2025-07`). Penangkal: aturan 81, ADR-A013.
- **KC-48 [RESMI v7]** — **ambang absolut ditetapkan pada besaran yang sebarannya
  belum pernah diukur.** Sumber terukur: ambang 10.000 byte pada butir 2 R-307,
  sementara berkas TERKECIL di semesta 22.440 byte — butir itu tidak pernah menguji
  alam. Penangkal: ukur min/maks/rata lebih dahulu, atau pakai ambang RELATIF
  (usulan aturan 82). Kerabat KC-20, KC-25, aturan 43.
- **KC-49 [RESMI v8 lampiran ini, teks penuh di jurnal 129 §6 dan ADR-A015 kep. 1]**
  — **pita praregistrasi dikunci tanpa lebih dulu menghitung implikasi aritmetis dari
  momen yang SUDAH terukur** (rata, min, maks, penyebut, nisbah antar kelas). Sumber
  terukur: pita 10..300 pada butir 2 R-308, sementara kelas MATI sudah diketahui
  ber-rata 413.306 dengan maksimum 451.875 — rata yang hanya ~8% di bawah maksimum
  memaksa ekor bawah menjadi tipis, dan terukur hanya **2**. Kejadian kembar: butir 1
  R-307 (7,15% ÷ 4,3 ≈ 1,7% dapat dihitung sebelum run). **Beda dari KC-48:** KC-48
  soal ambang MUSTAHIL sehingga butir tidak menguji alam; KC-49 soal ambang yang
  MUNGKIN dilewati tetapi hasilnya sudah tersirat, sehingga pita dipasang di tempat
  yang salah — butirnya tetap sah, letaknya yang keliru. Penangkal: usulan aturan 83.

## Papan skor prediksi — lengkap R-300..R-308 (R-199..R-299 di v4, blob `67dda29e`)

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

**Total R-1..R-308** (dihitung tangan, aturan 21). Dasar v7 (papan skor R-1..R-307):
TEPAT 215 · MELESET 57 · SEPARUH 20 · TIDAK TERADJUDIKASI 8 · MENUNGGU 7 = 307.

Sesudah v7: **R-308 SEPARUH**.

- TEPAT **215**
- MELESET **57**
- SEPARUH 20 + 1 = **21**
- TIDAK TERADJUDIKASI **8**
- MENUNGGU **7** (R-7, R-19, R-20, R-28, R-36, R-37, R-199)

215 + 57 + 21 + 8 + 7 = **308** ✅ Nomor terpakai R-1..R-308, seluruhnya
teradjudikasi atau menunggu. N_percobaan = 0. **ADJUDIKASI RISET TETAP TERKUNCI.**
Ramalan berikutnya **R-309** (praregistrasi sudah di jurnal 129 §10), lalu **R-310**.

**Utang papan skor:** rincian R-236..R-247 masih di jurnal 92–94; R-229 TEPAT dan
R-230 MELESET (dari docstring) menunggu pemeriksaan R-224..R-235.

## Catatan kejujuran [v8]

**R-308 SEPARUH. Satu butir berisiko menang, satu kalah, dan keduanya mengajarkan
hal yang berbeda.**

1. **Butir 1 MENANG dan ia benar-benar berisiko.** Terukur **38** dalam pita 20..600
   yang lebarnya tiga puluh kali lipat — tetapi pita itu dapat gagal ke DUA arah, dan
   nol adalah hasil yang sangat mungkin bila kedua kelas benar-benar terpisah. Zona
   irisan itu NYATA: 38 baris HIDUP berada di bawah berkas MATI terkecil. Ia juga
   TIPIS: 38 dari 18.087 hanyalah 0,21% kelas HIDUP.
2. **Butir 2 KALAH karena aritmetika saya, bukan karena alam — lagi.** R-307 sudah
   menyerahkan min 97.634, maks 451.875, rata 413.306 untuk kelas MATI. Rata yang
   duduk hanya ~8% di bawah maksimum berarti massanya menumpuk rapat di ujung atas
   dan ekor bawahnya pasti tipis; terukur **2**. Bahan hitungannya ada di tangan saya
   ketika pita 10..300 dikunci, dan saya tidak menghitungnya. Dua giliran berturut
   dengan sebab yang sama — itu pola. **KC-49**, usulan **aturan 83**, ADR-A015.
3. **Kekalahan butir 2 R-308 BUKAN sejenis kekalahan butir 2 R-307.** Ambang 150.000
   DAPAT dilewati dan memang dilewati dua kali, jadi butir ini benar-benar menguji
   alam (beda dari KC-48, yang ambangnya mustahil). Yang salah letak pitanya, bukan
   keberadaan ujinya. Pita TIDAK dilebarkan sesudah melihat hasil; godaan mengubah
   10..300 menjadi 1..300 direkam lalu DITOLAK (aturan 29).
4. **Ramalan cacah uji MELESET — aturan 57 PUTUS di giliran ke-27, catatan 26/27.**
   Diucapkan 67 butir dan CI 1167; sebenarnya 68 dan 1168. Sebab tepat: dalam daftar
   bernomor yang saya ucapkan, kelompok `uji_r308` ditulis "56–62" (tujuh) padahal
   kode berisi delapan — `test_uji_butir2_kalah` hilang dari DAFTAR, bukan dari kode.
   Angka 1168 yang saya perbaiki sesudah membaca berkas TIDAK menghapus kegagalan
   ramalan pertama; perbaikan pasca-melihat bukan ramalan. Hitungan beruntun dimulai
   lagi dari nol.
5. **Cacat konstruksi yang saya akui SEBELUM hasil keluar:** di `ringkaskan`,
   `total_byte` dihitung sebagai jumlah byte keempat kelas, sehingga
   `selisih_total_byte` tersirat secara aritmetis dari tiga selisih byte lain.
   Sembilan medan selisih = **delapan pemeriksaan bebas + satu turunan**. Butir 3
   tetap sah; menyebutnya "sembilan pemeriksaan bebas" DILARANG (ADR-A015 kep. 7).
6. **Temuan yang MELAWAN tafsir mudah, dikuatkan dua kali.** Di zona 22.440–97.634
   byte terdapat **38 baris HIDUP dan NOL baris MATI**. Maka di ekor bawah sebaran,
   berkas kecil hampir seluruhnya HIDUP: tafsir "kecil = mati" bukan sekadar belum
   terbukti, di zona itu ia TERBALIK. Besar berkas DILARANG dipakai sebagai detektor
   status ke arah mana pun (ADR-A015 kep. 5, kerabat KC-38).
7. **Utang cacah tangan LUNAS** (aturan 66): `lux_ai/serapan/` **45**, `tests/` **49**,
   `.github/workflows/` **40**, dinomori satu per satu pada ref `5a777664`. Ketiganya
   cocok dengan turunan — dan kecocokan itu TIDAK menyahkan kebiasaan mengutip
   turunan; KC-33 lahir persis dari kecocokan yang dijadikan alasan berhenti memeriksa.

**Kesalahan proses giliran ini:** tidak ada kegagalan konektor — dua belas giliran
berturut seluruh `push_files` dan `get_file_contents` berhasil sekali jalan. Satu
cacat administratif diakui: **blob `reports/ci_terakhir.json` untuk CI 1168 tidak
dicatat** ketika berkas itu dibaca; jangan mengarang empat puluh karakternya, baca
ulang dari main bila diperlukan. Satu hal yang BERJALAN BENAR: `BATAS_BARIS_LAPORAN`
40 membuat `irisan_byte.json` terbaca UTUH untuk kedua kalinya berturut — usulan
aturan 78 makin kuat. Cacat kecil tanpa akibat: `import pytest` tidak terpakai di
`tests/test_irisan_byte.py`.

## Jumlah uji

**1168 TERUKUR [v8].** `reports/ci_terakhir.json`: run **30529294152**, commit
**`d22364b9bf680c9e3bbafa0c28672b3b561db702`**, 2026-07-30T09:05:52Z, `kode_keluar` 0,
**1168 butir terkumpul**. Turunan: 1100 + **68** butir `tests/test_irisan_byte.py`
= **1168** ✅ (aturan 21). Blob berkas laporan itu TIDAK dicatat — lihat catatan
kejujuran butir kesalahan proses.

Riwayat panjang: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 →
984 → 1044 → 1100 → **1168**.

Cacah per berkas uji (yang diketahui): **`test_irisan_byte.py` 68** (dicacah TANGAN
pada berkas yang sudah di main, `def test_` satu per satu) ·
`test_bentangan_kohort.py` V2 **63** · `test_lubang_tebing.py` **60** ·
`test_sebab_bangkit.py` **57** · `test_byte_semesta.py` **56** ·
`test_lubang_awal.py` **48** · `test_tersisip_semesta.py` **47** ·
`test_anatomi_tengah.py` 47 · `test_terhenti.py` V4 33 · `test_bulan_absen.py` 32 ·
`test_karantina_semesta.py` 28 · `test_silang_settled.py` 24.

**Aturan 57 kini PUTUS: 26 dari 27**, hitungan beruntun mulai lagi dari nol.

Aturan 38 (cacah uji HANYA dari `ci_terakhir.json`): pemakaian ke-**tiga puluh tiga**.

## Utang verifikasi

1-5, 11 menunggu tahap juri. 6-23, 25-28 LUNAS. **Nomor utang BUKAN nomor
ramalan — KC-32.**

24. **AKTIF.** Lunas lama seperti v7. **LUNAS BARU [v8]:**
    - **Trio `irisan_byte` V1 dibaca ulang UTUH dari main** sesudah push `d22364b9`
      (aturan 52, 55): `lux_ai/serapan/irisan_byte.py` (`2dbe3d55`),
      `tests/test_irisan_byte.py` (`b6389051`, 68 butir dicacah tangan),
      `.github/workflows/irisan_byte.yml` (`7d98a267`, `paths` SATU entri).
    - `reports/irisan_byte.json` (`4c13bf6a`) terbaca **UTUH**; `_status.json`
      (`863dc4cb`) dan `ci_terakhir.json` terbaca utuh.
    - **Cacah tangan tiga direktori** pada ref `5a777664` (aturan 66): 45 / 49 / 40,
      dinomori satu per satu — utang tiga direktori LUNAS.
    - Jurnal 129 (`ecb6ac24`) dan ADR-A015 (`387d5510`) dibaca ulang UTUH sesudah
      push `982c2536`.
    - EKOR v7 (`9e906dfb`) dibaca UTUH sebelum berkas ini ditulis.
    - `get_commit` atas `69bfdd5d` dipakai untuk memastikan POLA NAMA berkas jurnal
      dan ADR (`journal/2026-07-30-128.md`, `decisions/ADR-A014.md`) — nama tidak
      ditebak.
    **TETAP BELUM:** `tests/test_bentangan_kohort.py` V2 (63 butir, blob
    `9f850ecd`) belum dibaca ulang byte demi byte — kini sudah **enam versi**
    menunggu; seluruh daftar BELUM dari v4/v5 masih berlaku (`ADR-A002`, A004, A006,
    A007, A008, `PETA_MODUL.md`, `PETA_MODUL_BERKAS.md`, `STATE_LAMPIRAN.md`,
    `STATE_LAMPIRAN_ANGKA.md`, `karantina_semesta.yml`, `test_pulihkan.py`,
    `test_rilis_karantina.py`, `test_karantina_a006.py`).

## Daftar ADR

- **ADR-A001** aturan dasar. DITERIMA.
- **ADR-A002** serapan. Kondisi v3 berlaku; §10 tetap tidak boleh diubah.
- **ADR-A003** taksonomi rezim. BELUM ADA. Wajib memuat delapan simbol bangkit,
  koreksi ADR-A011/A012/A013/A014/A015, bentangan LITUSDT, bulan ABSEN, aturan 76,
  KC-40.
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
  Delapan keputusan: (1) **KC-49 resmi**; (2) **aturan 83 diusulkan** — tulis
  aritmetika implikasi di jurnal sebelum mengunci pita, dan bila aritmetika itu sudah
  menentukan jawabannya dalam satu angka signifikan, butir itu bukan ramalan berisiko
  dan harus dipindah porosnya; (3) usulan aturan 82 DIPERLUAS mencakup ambang yang
  hasilnya sudah tersirat; (4) R-308 SEPARUH, godaan melebarkan pita direkam lalu
  ditolak; (5) tafsir H-A018 dipersempit — besar berkas bukan detektor status ke arah
  mana pun; (6) **H-A019 didaftarkan** dengan catatan ia lahir dari membaca hasil
  R-308 sehingga wajib diuji atas semesta penuh; (7) cacah invarian wajib menyebut
  mana yang bebas; (8) aturan 57 dicatat PUTUS 26/27. **DITERIMA.**
- **ADR berikutnya A016.**

## Temuan sampingan

**BARU [v8], terukur (`irisan_byte` V1 run 30529294165, commit `d22364b9`, kode 0,
laporan blob `4c13bf6a`, sidik kode
`0e7103ef46a37d1e442d8e7fc5b9771b1ef7cdc3956ea57d584d84f6f73ea2c6`):**

- **Lebar zona irisan terukur:** **38** baris HIDUP ber-byte < 97.634 (byte_min MATI),
  yaitu **0,21%** kelas HIDUP. Di zona 22.440–97.634 byte: 38 HIDUP, **0 MATI**.
- **Ekor bawah MATI nyaris kosong:** hanya **2** baris di bawah 150.000, dan
  seluruhnya — **LENDUSDT 2020-11 = 97.634** (minimum kelas MATI itu sendiri) dan
  **FRONTUSDT 2024-09 = 109.120**.
- Sebaran per kelas IDENTIK dengan R-307 dari modul berbeda (saling menguatkan,
  aturan 36): HIDUP 18.087 / 32.049.492.952 / 22.440 / 2.770.666 / 1.771.962,899 ·
  SEPI 98 / 77.728.024 / 259.327 / 1.231.408 / 793.143,102 · MATI 1.401 /
  579.041.399 / 97.634 / 451.875 / 413.305,781. `cacah_lain` 0, `total_byte`
  32.706.262.375.
- Delapan selisih invarian bebas + satu turunan, seluruhnya **0**;
  `kendali_data_sah` true (tiga BTCUSDT terbesar); `kendali_deteksi_sah` true
  (ambang 50: hidup_kecil 2 = harap 2, mati_kecil 1 = harap 1, total 1922);
  `laporan_hilang` [] · `cacah_laporan_hilang` 0.
- **Bentuk daftar 38 HIDUP-kecil (asal H-A019, BELUM diuji):** didominasi bulan
  pertama pencatatan (JUPUSDT 2024-01 22.440 · TIAUSDT 2023-10 24.551 · REZUSDT
  2024-04 32.164 · PORTALUSDT 2024-02 34.175 · NAORISUSDT 2025-07 34.673 · ADAUSDT
  2020-01 42.678 · COMPUSDT 2020-06 44.898 · RLCUSDT 2020-07 46.447 · YFIUSDT
  2020-08 54.929) dan bulan tepi jendela (SQQQUSDT 72.819 · TQQQUSDT 82.330 ·
  MVLLUSDT 86.126 — ketiganya **2026-06**). Yang tampak bulan tengah dan karena itu
  melawan H-A019: MTLUSDT 2021-03 51.322 · ENJUSDT 2020-09 94.658 · SLPUSDT 2023-10
  33.257 · TLMUSDT 2023-03 80.394.
- **`silang_funding.baca_laporan_kehidupan` bertanda tangan TIGA nilai** — terbukti
  sekali lagi lewat pemakaian di `irisan_byte` (KC-43 tetap terjaga).

**LAMA [v7], tetap berlaku (`byte_semesta` V1 run 30526358811):** total byte semesta
32.706.262.375 atas 19.586 simbol-bulan; bagian byte MATI **0.017704**;
`cacah_byte_nol` 0 dan dasar keras ≈22 KB (KC-48); `cacah_lain` 0; kendali data tiga
BTCUSDT terbesar; pengamatan LITUSDT lama ternyata mewakili semesta dengan baik.

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

**Lama, belum diukur:** APA ISI berkas bulan MATI (naik prioritas — ditanyakan dua
giliran berturut, dilarang ditebak); irisan 880 lawan 877; TANGGAL hari hilang BNX
2022-04/06/08; selisih 40−38 `diagnosa_kc15`; H-A016 (celah kelipatan 15);
mati_tersisip atas 19.586; bentangan 38 kohort; `ukur_baris` V6; R-7/19/20/28/36/37
dan R-199; R-236..R-247 dari jurnal 92–94; taksonomi lubang tiga kelas.

## Penomoran berikutnya

Aturan sampai **81** (resmi) · calon **77**, **78**, **82**, **83** (keempatnya TETAP
belum resmi; 83 lahir sebagai usulan di ADR-A015 kep. 2) · KC sampai **KC-49**
(KC-49 kini RESMI; KC-16 kosong selamanya) · KC berikutnya **KC-50** · Hipotesis
terbuka H-A016 (belum diuji), H-A017 (dilemahkan R-306), **H-A018** (DIUKUR dua kali,
tafsir dibatasi ADR-A014 dan A015), **H-A019** (DIDAFTARKAN, belum diuji — poros
R-309) · Hipotesis berikutnya **H-A020** · Jurnal berikutnya **130** · STATE:
`STATE.md` **v48** dan UKUR **v8** BELUM didorong (lihat peringatan keserasian versi
di kepala berkas ini) · PROMPT berikutnya **v52** · ADR berikutnya **A016** · Ramalan
berikutnya **R-309** (praregistrasi terkunci di jurnal 129 §10), lalu **R-310** ·
papan skor **308**.
