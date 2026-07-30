# STATE lampiran EKOR — bagian 2 dari STATE (v4, menuju STATE v45)

**Mengapa berkas ini ada.** Dua push `STATE.md` berturut terpotong (v41, v42);
pemecahan ke tiga berkas berlaku sejak v43 (KC-42). Pembagian yang berlaku:

1. **`STATE.md` v44** (blob terbit setelah push ini) — bagian 1: kepala, aturan 1–79,
   KC-1..KC-44.
2. **`STATE_LAMPIRAN_EKOR.md`** (berkas ini, v4) — bagian 2: papan skor, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** (blob `0e9ec3783d95be522dd4e56221fc7197f89c13c0`
   — berkas ini diperbarui bersama push ini) — bagian 3: pengukuran, modul, API,
   hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip lama; bukan sumber lagi.

**Tentang push berkas ini:** berkas ini berada di akar repo sehingga menyalakan
`ci.yml` (KC-41). Tidak satu pun `tests/**` berubah, jadi cacah tetap **936**
(push `sebab_bangkit` terakhir). Push ini **tidak dipraregistrasi** karena sejak
calon 79 resmi, cacah deterministik tidak lagi ditambahkan ke papan skor.

## KC-43 dan KC-44 (teks lengkap di STATE.md v44)

- **KC-43** — memakai tanda tangan fungsi dari INGATAN. Penangkal: baca modul
  yang diimpor UTUH pada giliran yang sama sebelum menulis modul baru.
- **KC-44** — semua laporan di-commit dalam satu langkah sehingga laporan berikutnya
  menimpa jejak laporan sebelumnya. Penangkal: tiap berkas laporan di-commit
  sendiri-sendiri.

**Calon KC-45:** satuan "bulan tanpa funding" vs "bulan MATI" dicampur.
**Calon KC-46:** lubang bentuk AWAL dibaca sebagai "funding berhenti".

## Papan skor prediksi — lengkap R-199..R-304

| # | Prediksi | Status |
|---|---|---|
| R-199 | `definisi_dapat_dibedakan` false pada TEPAT 2 pecahan | **MENUNGGU** |
| R-275 | SETTLED hidup: bulan tutup DAN cacah_bulan ≤3 | **TEPAT** |
| R-276 | keenam nama peralihan ada di 28 terhenti | **MELESET** |
| R-277 | CI 630, kode 0, commit `e6b74855` | **TEPAT** |
| R-278 | 15 SETTLED: 13 dasar hidup, 2 terhenti, ≥11 mendahului | **TEPAT** |
| R-279 | CI 630, commit `8a0c4bff` | **TEPAT** (MUDAH) |
| R-280 | CI 638 sesudah `test_terhenti` V4 | **TEPAT** (MUDAH) |
| R-281 | bulan SETTLED 36 dan 11 nama bersatu-bulan | **MELESET** (12) |
| R-282 | `diagnosa_kc15.json` menyebut tiga bulan BNXUSDT | **MELESET** (hanya 2022-04) |
| R-283 | modul `diagnosa_kc15` mengukur tepi | **TEPAT** |
| R-284 | `lubang_tengah.py` memuat tetapan tiga bulan BNXUSDT | **MELESET** (aturan 73) |
| R-285 | 6 lubang tengah, LIT 5 / BTCST 1, `h_a011_menang` false | **SEPARUH** |
| R-286 | H-A015: cocok 3..4; ≥10 dari 12 lebih awal; lubang >10 lawan <10 | **TEPAT** |
| R-287 | CI 662, kode 0, commit `3d113d49` | **TEPAT** (MUDAH) |
| R-288 | bulan ABSEN: (1) BNX 3 + 9 tunggal; (2) ≥7 dari 9 sama dengan SETTLED; (3) semesta 12 | **SEPARUH** |
| R-289 | `ci.yml` menyala pada STATE dan PROMPT, 662, kode 0 | **TEPAT** (MUDAH) |
| R-290 | CI 694, kode 0, commit `4fc818f0` | **TEPAT** (MUDAH) |
| R-291 | daftar karantina kedelapan manifes tepat 12, himpunan sama persis | **TEPAT — BERISIKO** |
| R-292 | CI 694, kode 0, commit `c07cb65f` | **TEPAT** (MUDAH) |
| R-293 | CI 694, kode 0, commit `91ce4660` | **TEPAT** (MUDAH) |
| R-294 | CI 722, kode 0, commit `edea61f7` | **TEPAT** (MUDAH) |
| R-295 | commit berikutnya penyala `ci.yml` memberi 722 dan kode 0 | **TEPAT** (MUDAH) |
| R-296 | push `STATE_LAMPIRAN_UKUR.md` memberi 722 dan kode 0 | **TEPAT** (MUDAH) |
| R-297 | push `STATE.md` v43 memberi 722 dan kode 0 | **TEPAT** (MUDAH) |
| R-298 | push PROMPT v44 memberi 722 dan kode 0 | **TEPAT** (MUDAH) |
| R-299 | push lampiran EKOR v2 memberi 722 dan kode 0 | **TEPAT** (MUDAH) |
| R-300 | (1) cacah_bulan 64; (2) tetangga BTCST keduanya HIDUP; (3) cacah_hidup 8..30 dan MATI>HIDUP | **SEPARUH** |
| R-301 | (1) tebing==0 dari 38; (2) mati_tersisip ≥1; (3) bangkit==0 | **TIDAK TERADJUDIKASI** |
| R-302 | (1) simbol tersisip 1..10; (2) simbol-bulan tersisip 1..50; (3) penyebut 19.586 / 787, kode 0 | **SEPARUH** — butir 3 TEPAT; butir 1 TEPAT (8); butir 2 MELESET (88 > 50) |
| R-303 | (1) cacah_simbol_tersisip 1..60; (2) simbol-bulan 1..300; (3) penyebut / simbol / kendali / kode 0 | **TEPAT (3/3)** — run 30514239872, kode 0; 8 simbol (dlm 1..60 ✅); 88 bulan (dlm 1..300 ✅) |
| R-304 | (1) mati_dulu dari 8 dalam pita 5..8; (2) hidup_berlubang dari 8 dalam pita 3..8; (3) penyebut / kendali / kode 0 | **MELESET** — butir 1 kalah (1, bukan 5..8); butir 2 kalah (2, bukan 3..8); butir 3 TEPAT (MUDAH) |

**Total R-1..R-304** (dihitung tangan, aturan 21). Dasar v43 (papan skor v3):
TEPAT 213 · MELESET 54 · SEPARUH 19 · TIDAK TERADJUDIKASI 7 · MENUNGGU 7 = 300.

Sesudah v3: R-301 TIDAK TERADJUDIKASI; R-302 SEPARUH; R-303 TEPAT; R-304 MELESET.

- TEPAT 213 + 1 = **214**
- MELESET 54 + 1 = **55**
- SEPARUH 19 + 1 = **20**
- TIDAK TERADJUDIKASI 7 + 1 = **8**
- MENUNGGU **7** (R-7, R-19, R-20, R-28, R-36, R-37, R-199)

214 + 55 + 20 + 8 + 7 = **304** ✅ Nomor terpakai R-1..R-304, seluruhnya
teradjudikasi atau menunggu. N_percobaan = 0. **ADJUDIKASI RISET TETAP TERKUNCI.**
Ramalan berikutnya **R-305** (praregistrasi sudah di jurnal 125 §7).

**Utang papan skor:** rincian R-236..R-247 masih di jurnal 92–94; R-229 TEPAT dan
R-230 MELESET (dari docstring); keduanya menunggu pemeriksaan R-224..R-235.

## Catatan kejujuran [v4]

**R-304 MELESET pada dua butir berisiko.** Saya meramalkan pita 5..8 dari 8 simbol
yang kematiannya mendahului hilangnya funding, dan yang terukur adalah **1**. Saya
meramalkan pita 3..8 yang punya bulan HIDUP berlubang, dan yang terukur adalah **2**.
Kekalahan bersih: angka keduanya jauh di bawah batas bawah pita. Tafsir penyebab:
1. Lima dari delapan simbol bangkit tidak punya satu pun lubang funding — kematian
   pasar dan lubang funding adalah DUA GEJALA BERBEDA.
2. Dua yang tampak "lubang dulu" (ICP −14, TLM −12) ternyata berlubang di BULAN
   PERTAMA riwayatnya — bukan funding berhenti, melainkan funding belum mulai
   (calon KC-46).
3. Satuan pada H-A015 dulu dicampur (calon KC-45): 19 dan 20 bulan itu bulan TANPA
   FUNDING, bukan bulan MATI.

**Kesalahan proses tetap dicatat:**
1. KC-43 — tanda tangan dikutip dari ingatan pada giliran R-302 awal.
2. KC-44 — `anatomi_tengah.yml` meng-commit semua laporan bersama; diperbaiki di
   `tersisip_semesta.yml` dan `sebab_bangkit.yml`.
3. R-301 TIDAK TERADJUDIKASI: praregistrasinya di jurnal 121 ternyata menguji
   fungsi yang BELUM ADA di `bentangan_kohort` V1 — `bangkit` dan `mati_tersisip`
   baru muncul di V2.
4. Urutan ramalan R-301: trio V2 baru didorong SETELAH jurnal 121; sejak R-302
   urutan diperbaiki (aturan 79 resmi).
5. **STATE v44 tertunda EMPAT giliran** — utang terbesar sesi ini. Kini dibayar.

## Jumlah uji

**936 TERUKUR [v4].** `reports/ci_terakhir.json` blob
**`10a301c543ff02940b738782defa452fdd641bc1`** pada commit
**`645fd5df1c973cc5c6336ebc6cee3786a6eb347a`**: run **30517682951**, commit
**`3913a0546c8db08b83ec22051459fdb24c4baf2d`**, 2026-07-30T05:49:11Z,
`kode_keluar` 0, **"936 tests collected in 0.55s"**. Turunan: 879 + **57** butir
`tests/test_sebab_bangkit.py` = **936** ✅ (aturan 21).

Riwayat panjang:
630 → 638 → 662×3 → 694×3 → 722×8 → **769** → **814** (commit `583fcb79` → trio
`bentangan_kohort` V1 **769**, lalu commit anatomi V1 = 769 terukur;
`bentangan_kohort` V2 menambah 63 → **832**; tersisip_semesta +47 → **879**;
sebab_bangkit +57 → **936**).

Cacah per berkas uji (yang diketahui): `test_bentangan_kohort.py` V2 **63** ·
`test_tersisip_semesta.py` **47** · `test_sebab_bangkit.py` **57** ·
`test_anatomi_tengah.py` 47 · `test_terhenti.py` V4 33 · `test_silang_settled.py`
24 · `test_bulan_absen.py` 32 · `test_karantina_semesta.py` 28. Aturan 57 kini
**dua puluh tiga dari dua puluh tiga**.

CI terakhir yang ada sebelum giliran ini (PROMPT v46): run **30514531868**,
commit `2f240448`, blob `4dc534a2`, 879, kode 0 — tidak ada perubahan berkas
uji, cacah tetap 879 ✅.

## Utang verifikasi

1-5, 11 menunggu tahap juri. 6-23, 25-28 LUNAS. **Nomor utang BUKAN nomor
ramalan — KC-32.**

24. **AKTIF.** Lunas lama seperti v3. **LUNAS BARU [v4]:**
    - `silang_funding.py` V2 (blob `42c3aa9dc2`, 29.873 B) dibaca UTUH pada giliran
      ini sebelum `sebab_bangkit.py` ditulis (KC-43 dibayar).
    - `tersisip_semesta.py` V1 (blob `8a648838`) dan `test_tersisip_semesta.py`
      (blob `61196fd1`) dibaca ulang UTUH sesudah push (aturan 52).
    - `sebab_bangkit.py` V1 (blob `fd5a1dc4`) dan `test_sebab_bangkit.py`
      (blob `3977c11c`) dibaca ulang UTUH sesudah push (aturan 52).
    - `reports/sebab_bangkit.json` (blob `9d654428`) terbaca UTUH dalam satu bacaan.
    - Listing `lux_ai/serapan/` (41) dan `.github/workflows/` (36) dicacah tangan
      pada ref `d182de1d` sebelum trio `sebab_bangkit` didorong (aturan 66).
    **TETAP BELUM:** `tests/test_bentangan_kohort.py` V2 (63 butir, `703daa90`)
    belum dibaca ulang; seluruh daftar BELUM dari v3 masih berlaku.

## Daftar ADR

- **ADR-A001** aturan dasar. DITERIMA.
- **ADR-A002** serapan. Kondisi v3 berlaku; §10 tetap tidak boleh diubah.
- **ADR-A003** taksonomi rezim. BELUM ADA. Wajib memuat delapan simbol bangkit
  (ADR-A010 §3.4), koreksi ADR-A011 (LITUSDT satu-satunya `mati_dulu` dari 8),
  bentangan LITUSDT, bulan ABSEN, aturan 76, KC-40.
- **ADR-A004** kebijakan KC-6. DITERIMA.
- **ADR-A005** jenis instrumen. DITERIMA.
- **ADR-A006** karantina + persistensi. DITERIMA, TERVERIFIKASI.
- **ADR-A007** serapan hibrida. DIUSULKAN, belum diterima.
- **ADR-A008** akibat KC-18. Keputusan 1–6 DITERIMA. **Keputusan 7 DITANGGUHKAN.**
  Pembatal pertama §6 TIDAK menyala pada dua lubang tengah (`mati_tersisip` 0 pada
  BTCST dan LIT); tetapi `mati_tersisip` atas seluruh 19.586 belum diukur (aturan
  20). Prasyarat tersisa: bentangan kehidupan **38** kohort puncak.
- **ADR-A009** (commit `17a594b6`) — arah sebab "kematian mendahului hilangnya
  funding" pada kelas bangkit. Dibuka kembali: pembatal pertama §6 ADR-A008 MENYALA
  pada semesta (8 simbol / 88 bulan tersisip semesta — bukan hanya 2 lubang tengah).
  **Wajib ditutup ulang oleh ADR-A011 sesudah R-304 MELESET.**
- **ADR-A010** (commit `c4bccf21`) — pembatal §6 ADR-A008 menyala, klaim
  "kebangkitan tunggal" DICABUT. DITERIMA.
- **ADR-A011** (commit `645fd5df`) — arah sebab ADR-A009 DICABUT untuk kelas
  bangkit. DITERIMA. R-304 butir 1 terukur 1 dari 8 (pita 5..8 kalah). Lima dari
  delapan bangkit tanpa satu pun lubang funding. H-A017 diturunkan: berlaku pada
  LITUSDT saja, bukan pola. Kematian pasar dan lubang funding dinyatakan DUA GEJALA
  BERBEDA. Lubang di bulan pertama DILARANG dibaca sebagai "berhenti".
- **ADR berikutnya A012.**

## Temuan sampingan

**BARU [v4], terukur:**

- **Delapan simbol bangkit (dari tersisip_semesta V1):** CVCUSDT 29 tersisip ·
  CVXUSDT 13 · SLPUSDT 13 · CTKUSDT 11 · LITUSDT 10 · TLMUSDT 8 · ICPUSDT 2 ·
  MAVIAUSDT 2. Total 29+13+13+11+10+8+2+2 = **88** ✅
- **Lima dari delapan tidak punya satu pun lubang funding** (CVCUSDT, CVXUSDT,
  SLPUSDT, CTKUSDT, MAVIAUSDT): kematian dan lubang adalah dua gejala berbeda.
- **LITUSDT satu-satunya dengan `mati_dulu` true** (selisih +5 bulan): bukan pola.
- **ICP dan TLM berlubang sejak bulan klines pertama** (selisih −14 dan −12): bukan
  "berhenti", melainkan "belum mulai" (calon KC-46).
- **`sidik_kode_silang_funding` terukur** dari `sebab_bangkit.json` =
  `8a9b859c09cd64e30e203e6f8dc53411b8e341c44f112805b3041e5d4d3231b1` — cocok
  dengan `sidik_kode` yang ada di laporan `lubang_tengah` V2 dan `silang_settled`
  V1 (aturan 36: definisi tetap satu).

**Lama, belum diukur:** irisan 880 lawan 877; TANGGAL hari hilang BNX 2022-04/06/08;
selisih 40−38 `diagnosa_kc15`; H-A016 (celah kelipatan 15); H-A017 dirumuskan ulang;
mati_tersisip atas 19.586; bentangan 38 kohort; `ukur_baris` V6; R-7/19/20/28/36/37
dan R-199; R-236..R-247 dari jurnal 92–94.

## Penomoran berikutnya

Aturan sampai **79** (resmi) · calon **77**, **78** (belum resmi) · calon KC-45,
KC-46 (belum berlaku) · KC sampai **KC-44** · Hipotesis terbuka H-A016, H-A017
(dirumuskan ulang) · Jurnal berikutnya **126** · STATE berikutnya **v45** · PROMPT
berikutnya **v47** · ADR berikutnya **A012** · Ramalan berikutnya **R-305**
(praregistrasi sudah di jurnal 125 §7) · papan skor **304**.
