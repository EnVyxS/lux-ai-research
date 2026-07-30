# STATE lampiran EKOR — bagian 2 dari STATE (v5, menuju STATE v46)

**Mengapa berkas ini ada.** Dua push `STATE.md` berturut terpotong (v41, v42);
pemecahan ke tiga berkas berlaku sejak v43 (KC-42). Pembagian yang berlaku:

1. **`STATE.md` v45** (blob `ede3ce3b` = v44; blob v45 terbit setelah push ini) —
   bagian 1: kepala, aturan 1–79, KC-1..KC-46.
2. **`STATE_LAMPIRAN_EKOR.md`** (berkas ini, v5) — bagian 2: papan skor, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan, penomoran.
3. **`STATE_LAMPIRAN_UKUR.md`** v5 — bagian 3: pengukuran, modul, API, hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip lama; bukan sumber lagi.

**Tentang push berkas ini:** berkas ini berada di akar repo sehingga menyalakan
`ci.yml` (KC-41). Tidak satu pun `tests/**` berubah, jadi cacah tetap **984**.
Push ini **tidak dipraregistrasi** karena cacah deterministik tidak lagi ditambahkan
ke papan skor sejak aturan 79.

## KC-43..KC-46 (teks lengkap di STATE.md)

- **KC-43** — tanda tangan fungsi dari INGATAN. Penangkal: baca modul yang diimpor
  UTUH pada giliran yang sama.
- **KC-44** — semua laporan di-commit satu langkah. Penangkal: commit tiap berkas
  laporan sendiri-sendiri.
- **KC-45 [RESMI v45]** — satuan “bulan tanpa funding” vs “bulan MATI” dicampur.
- **KC-46 [RESMI v45]** — lubang bentuk AWAL dibaca sebagai “funding berhenti”.

## Papan skor prediksi — lengkap R-300..R-305 (R-199..R-299 di v4, blob `67dda29e`)

| # | Prediksi | Status |
|---|---|---|
| R-300 | (1) cacah_bulan 64; (2) tetangga BTCST HIDUP; (3) cacah_hidup 8..30 dan MATI>HIDUP | **SEPARUH** |
| R-301 | (1) tebing==0; (2) mati_tersisip ≥1; (3) bangkit==0 | **TIDAK TERADJUDIKASI** |
| R-302 | (1) simbol tersisip 1..10; (2) simbol-bulan 1..50; (3) penyebut 19.586/787 | **SEPARUH** (butir 2 MELESET 88>50) |
| R-303 | (1) simbol tersisip 1..60; (2) simbol-bulan 1..300; (3) penyebut/kendali/kode 0 | **TEPAT (3/3)** |
| R-304 | (1) mati_dulu 5..8; (2) hidup_berlubang 3..8; (3) penyebut/kendali/kode 0 | **MELESET** (1 dan 2 kalah) |
| R-305 | (1) bagian mati-tak-setelah-lubang dari ≥100 dalam 0.55..0.95; (2) cacah lubang-awal 20..120; (3) 19.586/787/1401/877/880/8 + kendali + kode 0 + CI | **MELESET** — butir 1 KALAH (penyebut 118, bagian **1.0** > 0.95, tautologis aturan 10); butir 2 KALAH (cacah **5** < 20, penyebut<20 aturan 41); butir 3 TEPAT (MUDAH) |

**Total R-1..R-305** (dihitung tangan, aturan 21). Dasar v4 (papan skor R-1..R-304):
TEPAT 214 · MELESET 55 · SEPARUH 20 · TIDAK TERADJUDIKASI 8 · MENUNGGU 7 = 304.

Sesudah v4: **R-305 MELESET**.

- TEPAT **214**
- MELESET 55 + 1 = **56**
- SEPARUH **20**
- TIDAK TERADJUDIKASI **8**
- MENUNGGU **7** (R-7, R-19, R-20, R-28, R-36, R-37, R-199)

214 + 56 + 20 + 8 + 7 = **305** ✅ Nomor terpakai R-1..R-305, seluruhnya
teradjudikasi atau menunggu. N_percobaan = 0. **ADJUDIKASI RISET TETAP TERKUNCI.**
Ramalan berikutnya **R-306** (praregistrasi sudah di jurnal 126 §7), lalu **R-307**.

**Utang papan skor:** rincian R-236..R-247 masih di jurnal 92–94; R-229 TEPAT dan
R-230 MELESET (dari docstring) menunggu pemeriksaan R-224..R-235.

## Catatan kejujuran [v5]

**R-305 MELESET pada dua butir berisiko, meleset DUA ARAH.**
1. Butir 1 diramalkan 0.55..0.95, terukur **1.0** (118/118) — over-shoot. Kemenangan
   arah sebab tampak makin kuat, TETAPI nyaris tautologis: hampir setiap
   `bulan_mati_pertama` == `bulan_lubang_bukan_awal_pertama`, dan banyak lubang
   bukan-awal pertama jatuh di tebing “2025-07”. Itu persis peringatan aturan 10 —
   kecocokan urutan waktu BUKAN bukti arah sebab. Karena itu 100% tidak dihitung
   sebagai kemenangan arah.
2. Butir 2 diramalkan 20..120, terukur hanya **5** simbol berlubang bentuk AWAL
   (≈ 0.6% dari 787) — langka; penyebut < 20 memaksa KALAH (aturan 41/46).
3. ICPUSDT dan TLMUSDT (`lubang_awal_berakhir_sebelum_mati` false) mengukuhkan
   KC-46: lubang AWAL mereka melewati kematian, sumber salah-baca R-304.

**Konsekuensi ADR (ADR-A012):** arah sebab ADR-A009 (“kematian mendahului hilangnya
funding”) DICABUT untuk SELURUH semesta, bukan hanya kelas bangkit. 100% butir 1
dicatat sebagai artefak tautologis (lubang bukan-awal ≈ delisting). Tebing 2025-07
dicurigai memproduksi lubang semu — inti pertanyaan R-306.

**Kesalahan proses giliran ini:**
1. `push_files` trio `lubang_awal` gagal transien sekali + args ter-truncate sekali
   (verifikasi tip masih `0bab4638`; tidak ada commit). Didorong ulang lengkap →
   `d304d3eb` sukses. Konektor MCP GitHub gagal transien beberapa kali; retry sah.
2. Cacah berkas uji drift: v44 mencatat 45, pencacahan langsung memberi **47**.
   R-305 hanya menambah `test_lubang_awal.py` → cacah v44 kurang 1; DIKOREKSI oleh
   pencacahan langsung (aturan 66). Cacah butir uji CI (984) TIDAK terpengaruh.

## Jumlah uji

**984 TERUKUR [v5].** `reports/ci_terakhir.json` (blob `56e411ce`) pada commit
`d304d3eb`: run **30522785099**, commit
**`d304d3eb19a875eab1cbc5dc5cedc81c20fb91f9`**, 2026-07-30T07:23:33Z, `kode_keluar`
0, **“984 tests collected in 0.56s”**. Turunan: 936 + **48** butir
`tests/test_lubang_awal.py` = **984** ✅ (aturan 21).

Riwayat panjang: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 →
**984**.

Cacah per berkas uji (yang diketahui): `test_lubang_awal.py` **48** ·
`test_sebab_bangkit.py` **57** · `test_tersisip_semesta.py` **47** ·
`test_bentangan_kohort.py` V2 **63** · `test_anatomi_tengah.py` 47 ·
`test_terhenti.py` V4 33 · `test_silang_settled.py` 24 · `test_bulan_absen.py` 32 ·
`test_karantina_semesta.py` 28. Aturan 57 kini **dua puluh empat dari dua puluh
empat**.

## Utang verifikasi

1-5, 11 menunggu tahap juri. 6-23, 25-28 LUNAS. **Nomor utang BUKAN nomor
ramalan — KC-32.**

24. **AKTIF.** Lunas lama seperti v4. **LUNAS BARU [v5]:**
    - `kehidupan.py` (`f49abb2b`), `kehidupan_arsip.py` (`318a5cb1`),
      `silang_funding.py` V2 (`42c3aa9d`) dibaca UTUH pada giliran R-305 sebelum
      `lubang_awal.py` ditulis (KC-43 dibayar).
    - `lubang_awal.py` V1 (`8c36943d`) dan `test_lubang_awal.py` (`86c401ee`, 48
      butir) dibaca ulang UTUH sesudah push `d304d3eb` (aturan 52).
    - `lubang_awal.yml` (`3134bc9f`) dibaca ulang UTUH (aturan 55).
    - `reports/lubang_awal.json` (`3da15a11`), `_status.json` (`ce1a9901`),
      `ci_terakhir.json` (`56e411ce`) terbaca UTUH.
    - Listing `lux_ai/serapan/` (**43**), `.github/workflows/` (**38**), `tests/`
      (**47**) dicacah tangan ref `b5442df3` (aturan 66).
    **TETAP BELUM:** `tests/test_bentangan_kohort.py` V2 (63 butir, blob
    `9f850ecd`) belum dibaca ulang byte demi byte; seluruh daftar BELUM dari v4
    masih berlaku.

## Daftar ADR

- **ADR-A001** aturan dasar. DITERIMA.
- **ADR-A002** serapan. Kondisi v3 berlaku; §10 tetap tidak boleh diubah.
- **ADR-A003** taksonomi rezim. BELUM ADA. Wajib memuat delapan simbol bangkit,
  koreksi ADR-A011/A012, bentangan LITUSDT, bulan ABSEN, aturan 76, KC-40.
- **ADR-A004** kebijakan KC-6. DITERIMA.
- **ADR-A005** jenis instrumen. DITERIMA.
- **ADR-A006** karantina + persistensi. DITERIMA, TERVERIFIKASI.
- **ADR-A007** serapan hibrida. DIUSULKAN, belum diterima.
- **ADR-A008** akibat KC-18. Keputusan 1–6 DITERIMA. **Keputusan 7 DITANGGUHKAN.**
  Prasyarat tersisa: bentangan kehidupan 38 kohort puncak.
- **ADR-A009** (commit `17a594b6`) — arah sebab “kematian mendahului hilangnya
  funding”. **DICABUT PENUH oleh ADR-A012.**
- **ADR-A010** (commit `c4bccf21`) — klaim “kebangkitan tunggal” DICABUT. DITERIMA.
- **ADR-A011** (commit `645fd5df`) — arah sebab ADR-A009 DICABUT untuk kelas
  bangkit; kematian dan lubang funding DUA GEJALA BERBEDA. DITERIMA.
- **ADR-A012** (commit `f9f564d1`, giliran R-305) — arah sebab A009 DICABUT untuk
  SELURUH semesta. Butir 1 R-305 = 100% (118/118) dinyatakan ARTEFAK TAUTOLOGIS
  (lubang bukan-awal ≈ bulan delisting), bukan bukti arah (aturan 10). Ukur ulang
  arah waktu tanpa praduga; tebing 2025-07 tersangka artefak. Lubang bentuk AWAL
  langka (5/787). DITERIMA.
- **ADR berikutnya A013.**

## Temuan sampingan

**BARU [v5], terukur (`lubang_awal` V1 run 30522785043, commit `d304d3eb`, kode 0):**

- **Hanya 122 dari 787 simbol pernah berlubang funding** (`cacah_simbol_ada_lubang`
  122; `cacah_simbol_lubang_awal` **5**; `cacah_simbol_lubang_bukan_awal` **118**;
  BNXUSDT punya keduanya).
- **Lubang bentuk AWAL langka: 5 simbol** — BNXUSDT, ICPUSDT, JUPUSDT, QTUMUSDT,
  TLMUSDT. Dari 5: tiga (BNX, JUP, QTUM) lubang awalnya berakhir sebelum mati / tak
  pernah mati; dua (ICP, TLM) melewati kematian (`lubang_awal_berakhir_sebelum_mati`
  false) — mengukuhkan KC-46.
- **Butir 1 = 100% (118/118) tautologis:** tidak ada simbol yang mati SESUDAH lubang
  bukan-awal pertama, karena lubang bukan-awal sering ADALAH bulan delisting atau
  muncul di tebing 2025-07 lama sesudah kematian.
- **Tebing 2025-07** memproduksi banyak `bulan_lubang_bukan_awal_pertama` = “2025-07”
  — inti pertanyaan R-306.
- `sidik_kode` `lubang_awal` V1 = `156499ce9d6e822bb7f57786e8e308955441996699c1fd53d0e8814e1f8f2362`;
  sidik silang_funding & data_funding COCOK dengan laporan sebelumnya (aturan 36).

**Delapan simbol bangkit (v4, tetap):** CVCUSDT 29 · CVXUSDT 13 · SLPUSDT 13 ·
CTKUSDT 11 · LITUSDT 10 · TLMUSDT 8 · ICPUSDT 2 · MAVIAUSDT 2 = 88. Lima tanpa
lubang; LITUSDT satu-satunya `mati_dulu` (+5).

**Lama, belum diukur:** irisan 880 lawan 877; TANGGAL hari hilang BNX 2022-04/06/08;
selisih 40−38 `diagnosa_kc15`; H-A016 (celah kelipatan 15); mati_tersisip atas
19.586; bentangan 38 kohort; `ukur_baris` V6; R-7/19/20/28/36/37 dan R-199;
R-236..R-247 dari jurnal 92–94.

## Penomoran berikutnya

Aturan sampai **79** (resmi) · calon **77**, **78** (belum resmi) · KC sampai
**KC-46** (KC-45, KC-46 kini RESMI) · Hipotesis terbuka H-A016, H-A017 (LITUSDT
saja) · Jurnal berikutnya **127** · STATE berikutnya **v46** · PROMPT berikutnya
**v49** · ADR berikutnya **A013** · Ramalan berikutnya **R-306** (praregistrasi
sudah di jurnal 126 §7), lalu **R-307** · papan skor **305**.
