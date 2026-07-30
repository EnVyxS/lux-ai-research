# PROMPT KELANJUTAN — v47

**Operator:** Diva Juan Nur Taqarrub · GitHub: EnVyxS · Zona waktu: Asia/Jakarta ·
Bahasa kerja: Indonesia · Tenggat: 2 Agustus 2026.

**BERKAS DI REPO ADALAH KEBENARAN; prompt ini hanya peta dan boleh saja tertinggal.**

---

## LANGKAH 0 — WAJIB, BERURUTAN, SEBELUM PEKERJAAN APA PUN

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})` dengan
   owner/repo HANYA di dalam `toolArguments`, tidak di tingkat atas.
3. Baca dari repo `EnVyxS/lux-ai-research`, **berurutan**:
   - `STATE.md` v44 (bagian 1: aturan + KC)
   - `STATE_LAMPIRAN_EKOR.md` v4 (bagian 2: papan skor, ADR, catatan)
   - `STATE_LAMPIRAN_UKUR.md` v4 (bagian 3: pengukuran, modul, API, hipotesis)
   - `journal/2026-07-30-125.md` (adjudikasi R-304 + praregistrasi R-305)
4. Baru setelah itu pekerjaan teknis.

---

## BATASAN LINGKUNGAN

- Sandbox agen tidak punya jaringan; semua pengukuran lewat GitHub Actions; hanya
  artefak yang di-commit boleh dipercaya.
- Tidak ada alat membaca status Actions dan tidak ada alat memicu
  `workflow_dispatch`. Satu-satunya cara menyalakan run adalah push ke berkas dalam
  `paths` workflow.
- Tidak ada API patch: `push_files` MENULIS ULANG seluruh isi berkas. Jangan
  menulis ulang berkas panjang sebelum membacanya utuh (KC-42d); sesudah mendorong
  berkas panjang WAJIB baca ulang dari main (aturan 52).
- Batas tulis aman ±25–45 KB; STATE penuh (~55 KB) pernah TERPOTONG SUNYI dua
  kali (KC-42): commit BUKAN bukti keutuhan.
- Batas baca: hasil >±30.000 token DIPOTONG. `reports/funding_semesta.json` hanya
  terbaca 27% → TIDAK terukur utuh. Manifes pecahan mustahil dibaca.
- `search_code` mengembalikan 0 hasil — pakai `get_file_contents`; path berakhiran
  garis miring melisting direktori.
- Runner punya numpy, pandas, pyarrow, pyyaml, pytest; TIDAK ada scipy/requests.
  `data.binance.vision` dapat diakses; `fapi.binance.com` 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`; `lux-research` baca saja.
- `ci.yml` memakai `paths-ignore` (journal/**, decisions/**, hipotesis/**,
  reports/**), BUKAN `paths`. Push ke `lux_ai/**`, `tests/**`, `STATE*`, `PROMPT*`
  MENYALAKAN CI; push jurnal/decisions/reports TIDAK.

---

## POSISI SERAH TERIMA (30 Juli 2026, ±12:56 WIB)

HEAD main = commit `645fd5df1c973cc5c6336ebc6cee3786a6eb347a` = STATE v44 + LAMPIRAN
v4 + PROMPT v47 (push giliran ini). Sebelumnya: `3913a054` = trio `sebab_bangkit`;
`645fd5df` memuatnya.

Papan skor R-1..R-304: TEPAT **214** / MELESET **55** / SEPARUH **20** /
TIDAK TERADJUDIKASI **8** / MENUNGGU **7** = **304**.
MENUNGGU: R-7, R-19, R-20, R-28, R-36, R-37, R-199.
N_percobaan = 0. ADJUDIKASI RISET TETAP TERKUNCI.
Aturan sampai 79 (resmi). KC sampai KC-44. Hipotesis terbuka H-A016, H-A017.
Jurnal berikutnya 126. STATE v45. ADR A012. Ramalan R-305 sudah dipraregistrasi di
jurnal 125 §7.

---

## PEKERJAAN PERTAMA, BERURUTAN

1. **Utang aturan 52:** baca ulang `tests/test_bentangan_kohort.py` V2 (blob commit
   `703daa90`, 63 butir) — belum dibaca ulang sesudah push.
2. Baca `reports/ci_terakhir.json` untuk memastikan commit HEAD dan cacah CI sesudah
   push STATE v44 ini (harapan 936, wajib DIUKUR bukan diramal).
3. **Praregistrasi R-305 sudah terkunci di jurnal 125 §7.** Sebelum trio penguji
   R-305 dibuat, baca berkas-berkas yang akan diimpor: `silang_funding.py` V2 (blob
   `42c3aa9d`) terutama fungsi `bentuk_lubang_lokal` dan definisi lubang awal,
   BESERTA listing `lux_ai/serapan/` dan `.github/workflows/` yang dicacah tangan.
4. Dorong trio R-305 atomik (satu `push_files`): modul `lubang_awal.py` atau nama
   yang belum dipakai, berkas uji bernomor `test_01`…, workflow yang meniru
   `sebab_bangkit.yml`.
5. Sesudah run: baca status.json, .json, .log; cocokkan run_id/commit/sidik_kode;
   bayar aturan 52 (baca ulang modul + berkas uji dari main).
6. Adjudikasi R-305 JUJUR terhadap praregistrasi jurnal 125 §7; dilarang menawar
   sesudah angka terlihat (aturan 29).
7. Jurnal 126 → ADR A012 bila perlu → PROMPT v48.

---

## TEMUAN WAJIB DIBAWA

**Delapan simbol bangkit (terukur, `sebab_bangkit` V1 run 30517682958):**
CVCUSDT 29 tersisip · CVXUSDT 13 · SLPUSDT 13 · CTKUSDT 11 · LITUSDT 10 ·
TLMUSDT 8 · ICPUSDT 2 · MAVIAUSDT 2. Total 88 ✅

**Lima tanpa lubang funding:** CVCUSDT, CVXUSDT, SLPUSDT, CTKUSDT, MAVIAUSDT.
**LITUSDT satu-satunya `mati_dulu` (+5 bulan).** ICP dan TLM berlubang sejak bulan
klines pertama (calon KC-46 — bukan "berhenti", melainkan "belum mulai").
**ADR-A011 DITERIMA:** arah sebab A009 DICABUT untuk kelas bangkit. H-A017
dirumuskan ulang: berlaku pada LITUSDT saja, penyebut 1 dari 8.

**CI: 936** (run 30517682951, commit `3913a054`, kode 0, 05:49:11Z).
**Sidik kode `sebab_bangkit`:**
`bafe4359e8f36f0402d4be4a4e4aef4a28f224f6419f06f701fb3a5bf696221a`
**Sidik kode `tersisip_semesta`:**
`9618fd19e4ab2e7b5279177db600f6176afd914ab1e94576e54197f70ebc537c`

---

## PRAREGISTRASI R-305 (terkunci di jurnal 125 §7)

- **Butir 1 (BERISIKO):** di antara simbol yang punya ≥1 bulan MATI DAN ≥1 lubang
  **bukan-awal**, yang `bulan_mati_pertama`-nya TIDAK lebih besar dari bulan lubang
  bukan-awal pertamanya berjumlah dalam pita **55%..95%** dari penyebut itu.
  Penyebut wajib ≥ 100; bila <100 → TIDAK TERADJUDIKASI.
- **Butir 2 (BERISIKO):** cacah simbol yang bulan klines PERTAMAnya berlubang
  funding dalam pita **20..120** dari 787; dari simbol itu, yang lubang awalnya
  berakhir SEBELUM bulan MATI pertama (atau tidak pernah MATI) ≥ **80%**.
- **Butir 3 (MUDAH, disebut MUDAH):** penyebut 19.586 / 787, MATI 1.401, lubang
  877/880, bangkit 8, kendali sah, kode 0.

Akibat: lihat jurnal 125 §7 untuk bunyi lengkap.

---

## KEBIASAAN YANG MENGIKAT

Ramalan SEBELUM run lalu adjudikasi jujur; **praregistrasi di jurnal lebih dulu
(aturan 79, RESMI)**; hitung ulang tiap angka (21); medan penggugur (24); kelas
cacat pada sampel (37); dilarang menyimpulkan di luar rentang (20); kendali positif
wajib (50); laporan tak terbaca utuh = tidak ada (52); cacah butir uji dari daftar
bernomor (54/56/57); ketiadaan pengukuran bukan ketiadaan gejala (59); listing
direktori sebelum menulis modul baru (66); nama turunan bersama asalnya (69); baca
modul penghasil sebelum meramalkan laporannya (71); jangan meramal isi berkas dari
NAMA-nya (73); setiap nol bersama penyebutnya (74); **tanda tangan fungsi dikutip
dari kode, bukan dari ingatan (KC-43)**; **tiap laporan di-commit sendiri-sendiri
(KC-44)**; **satuan bulan wajib tersurat (calon KC-45)**; **periksa bentuk lubang
sebelum tafsir arah waktu (calon KC-46)**.

"lanjut"/"lanjutkan" berarti teruskan tanpa konfirmasi. Jangan berhenti dengan
alasan konteks Notion.

---

## PEKERJAAN BERIKUTNYA SESUDAH R-305

H-A017 (byte parquet atas semesta); H-A016 (celah kelipatan 15 menit); STATE v45;
mati_tersisip atas 19.586; `ukur_baris` V6 (KC-26); ADR A003/A007/A005/A006;
adjudikasi R-7/19/20/28/36/37 dan R-199; gali bunyi R-28 dari STATE v23 (KC-32);
R-236..R-247 dari jurnal 92–94 (R-229 TEPAT, R-230 MELESET); TANGGAL hari hilang
BNX 2022-04/06/08; irisan 880 lawan 877; selisih 40−38 `diagnosa_kc15`; bentangan
38 kohort (prasyarat Keputusan 7 ADR-A008).

**Belum dibaca:** `decisions/ADR-A002.md`, A004, A006, A007, A008 (utuh),
`PETA_MODUL.md`, `PETA_MODUL_BERKAS.md`, `STATE_LAMPIRAN.md`,
`STATE_LAMPIRAN_ANGKA.md`, `karantina_semesta.yml` (blob kini `de40fa4e`),
`tests/test_pulihkan.py`, `test_rilis_karantina.py`, `test_karantina_a006.py`,
`tests/test_bentangan_kohort.py` V2 (utang aturan 52).

---

## API TERVERIFIKASI (JANGAN DITEBAK)

`silang_funding` V2 (blob `42c3aa9d`, 29.873 B) · `kehidupan_arsip` V1
(`318a5cb1`, `TOTAL_PECAHAN=8`) · `kohort_ekor` V4 (`c9b63bbe`,
`TEBING="2025-07"`, `BULAN_DIHARAPKAN="2026-06"`, `BATAS_SIMBOL=10`) ·
`tersisip_semesta` V1 (`8a648838`) · `sebab_bangkit` V1 (`fd5a1dc4`) ·
`bentangan_kohort` V2 (`f4eae57a`) · `anatomi_tengah` V1 (`04279335`) ·
`lubang_tengah` V2 (`4d3beaf1`).

Sidik kode laporan kehidupan (seragam):
`24b6bb265525e81c2e571b46e401f36903383f1e3738c487850861adc3e8c595`

---

## COMMIT/REF PENTING (terbaru lebih dulu)

- **`645fd5df`** STATE v44 + LAMPIRAN v4 + PROMPT v47 (giliran ini)
- **`3913a054`** trio `sebab_bangkit` V1
- `c4bccf21` jurnal 124 + ADR-A010
- `6a7710e3` laporan `tersisip_semesta` run 30514239872
- `25106dd5` trio `tersisip_semesta` V1
- `2f240448` PROMPT v46
- `17a594b6` jurnal 123 + ADR-A009
- `703daa90` trio `bentangan_kohort` V2
- `47e12611` jurnal 122
- `ffa45371` trio `bentangan_kohort` V1

**Run id penting:** sebab_bangkit **30517682958** (kode 0) · CI **30517682951**
(936) · tersisip_semesta **30514239872** (kode 0) · CI **30514239862** (879) ·
bentangan V2 30509071237 · CI 30509071199 (832) · CI 30514531868 (879, PROMPT v46)
· CI 30485048845 (769) · CI 30482864644 (722).
