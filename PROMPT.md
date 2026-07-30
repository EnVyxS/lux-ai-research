# PROMPT v49 — serah terima LUX-AI

Operator: **Diva Juan Nur Taqarrub** (GitHub **EnVyxS**).
Repo tulis: **`EnVyxS/lux-ai-research`**. Tenggat proyek: **2026-08-02**.
Ditulis: 2026-07-30 sesudah R-306 diadjudikasi (jurnal 127).
Menggantikan PROMPT v48 (blob `35beed4449d7efe899a44f8456060c2f23323f7e`).

---

## LANGKAH 0 — WAJIB SEBELUM PEKERJAAN APA PUN

Jangan menulis kode, jangan mendorong berkas, jangan mengklaim angka sebelum
keempat hal ini selesai:

1. Baca **PROMPT.md** (berkas ini) UTUH dari main.
2. Baca **STATE.md**, **STATE_LAMPIRAN_EKOR.md**, **STATE_LAMPIRAN_UKUR.md** UTUH.
3. Baca **jurnal terbaru** (`journal/2026-07-30-127.md`) dan ADR terbaru
   (`decisions/ADR-A013.md`) UTUH.
4. Baca `reports/ci_terakhir.json` untuk cacah uji CI **terukur** — jangan
   mengarang cacah uji.

Sesudah itu, catat di jawaban pertama: papan skor, penomoran berikutnya, dan
utang aturan 52 yang masih hidup.

---

## 1. Aturan yang paling sering dilanggar (baca ini dua kali)

- **Aturan 29 — adjudikasi jujur.** Pita praregistrasi TIDAK BOLEH diubah
  sesudah pengukuran. MELESET dicatat MELESET.
- **Aturan 52 — baca utuh.** Sesudah `push_files`, baca ulang setiap berkas UTUH
  dari main. `push_files` pernah memotong berkas besar dalam sunyi (KC-42);
  batas tulis aman ±**25–45 KB** per berkas.
- **Aturan 55 / KC-41 — jangan mengutip rumusan dari ingatan.** Rumusan pemicu
  workflow, definisi medan, nama tetapan: BACA berkasnya. Giliran ini menemukan
  satu kasus lagi (§6).
- **Aturan 66 — cacah direktori dengan tangan** sebelum menamai modul baru.
  Giliran ini aturan itu mencegah `lubang_tengah` ditimpa.
- **Aturan 57 — ramalkan cacah uji SEBELUM push**, lalu ukur. Kini 25/25 tepat.
- **Aturan 79 — praregistrasi lebih dulu.** Pita ditulis di jurnal SEBELUM modul
  pengukurnya ada.
- **Aturan 10 + ADR-A013 — irisan bukan sebab, dan satu peristiwa bukan banyak
  pengamatan.** Lihat §4.

---

## 2. Posisi sekarang

- Tip main sesudah pekerjaan giliran ini: commit **`8ba4f989be545783e885caa21b9834e0456da4b7`**
  (jurnal 127 + ADR-A013), di atas **`84b11164`** (trio `lubang_tebing`).
  Catatan: bot laporan CI menambah commit sesudahnya — selalu baca tip main
  yang sebenarnya, jangan asumsikan.
- **Papan skor R-1..R-306 = 306**: TEPAT **215** / MELESET **56** / SEPARUH **20** /
  TIDAK TERADJUDIKASI **8** / MENUNGGU **7**.
  MENUNGGU: R-7, R-19, R-20, R-28, R-36, R-37, R-199. `N_percobaan` = 0.
- **CI terukur 1044** butir (run **30524631516**, commit `84b11164`, kode 0).
  Riwayat: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 →
  984 → **1044**.
- Cacah direktori sesudah trio giliran ini: `lux_ai/serapan/` **44** `.py`,
  `.github/workflows/` **39**, `tests/` **48**. (Terukur sebelum trio: 43 / 38 / 47.
  Cacah `tests/` wajib dicacah ulang dengan tangan pada giliran berikut.)
- **STATE v46 BELUM ADA.** STATE terkini masih v45:
  `STATE.md` = `e07f2de12adacf5f814639be3988f690d2881fc5`,
  `STATE_LAMPIRAN_EKOR.md` v5 = `fe45f8b483db019873698f605a9aded4f0f229af`,
  `STATE_LAMPIRAN_UKUR.md` v5 = `eb8268176d573d88ee48193e9b57338a6aaa7153`.
  **STATE v46 adalah utang nomor satu giliran berikut** (isi wajib di §7).

---

## 3. Penomoran berikutnya

| hal | berikutnya |
| --- | --- |
| jurnal | **128** |
| STATE | **v46** |
| PROMPT | **v50** |
| ADR | **A014** |
| KC resmi | **KC-47** (KC-16 kosong selamanya) |
| ramalan | **R-307** (terkunci, jurnal 127 §7), lalu R-308 |
| papan skor sesudah R-307 | **307** |
| aturan resmi | **DITUNDA** — lihat §6 |

---

## 4. Apa yang baru dipelajari (jangan diulang)

R-306 = **TEPAT** (tiga butir menang), tetapi pelajarannya justru pahit:

Penyebut 118 simbol terpecah menjadi `mati_dulu` **40** / `serempak` **78** /
`lubang_dulu` **0**. Bagian strikt **0.339** (dalam pita 0.25..0.60). Cacah
tebing **39** (dalam pita 20..90).

Lalu: **39 dari 40** simbol `mati_dulu` ber-lubang-bukan-awal-pertama TEPAT
`2025-07`. Hanya **BTCSTUSDT** yang lepas dari tebing. Jadi "arah waktu" itu
bukan 40 pengamatan bebas, melainkan **satu peristiwa penerbitan yang menimpa 39
bangkai**. ADR-A013 mewajibkan setiap klaim arah dipilah tebing / bukan-tebing,
dan melarang kelas `serempak` masuk numerator.

**Akibat strategis:** poros lubang/funding sudah kehabisan kejutan (R-304, R-305,
R-306 semuanya berujung ke 2025-07). R-307 sengaja pindah poros.

---

## 5. R-307 — PRAREGISTRASI TERKUNCI (jurnal 127 §7, JANGAN DIUBAH)

Poros: **H-A017**, byte parquet atas semesta 19.586 simbol-bulan (belum pernah
dijumlahkan sekali pun).

- **Butir 1 (BERISIKO).** Bagian byte parquet milik simbol-bulan berstatus **MATI**
  atas TOTAL byte parquet seluruh 19.586 simbol-bulan. Pita **0.02 .. 0.15**.
  Bila total byte = 0 → TIDAK TERADJUDIKASI.
- **Butir 2 (BERISIKO).** Cacah simbol-bulan berstatus **TERUKUR** (HIDUP atau
  SEPI) yang `byte_parquet` **< 10.000**. Pita **20 .. 400**.
- **Butir 3 (MUDAH).** Sembilan invarian penggugur tetap nol, kedua kendali sah,
  kode keluar 0, cacah uji CI **diukur**.

Sembilan invarian penggugur (aturan 24): penyebut **19.586**, simbol **787**,
MATI **1.401**, bangkit **8**, lubang dalam penyebut **877**, lubang semesta
**880**, ada_lubang **122**, lubang_awal **5**, lubang_bukan_awal **118**.

Rencana pelaksanaan: modul baru `lux_ai/serapan/<nama>.py` — **cacah direktori
dulu** (aturan 66) sebelum menamainya. Sumber byte: `byte_parquet` dari
`silang_funding.baca_laporan_kehidupan`, yang sudah mengembalikan
`(status, byte_parquet, meta)`. Kendali dua lapis wajib: kendali data
(`silang_funding.kendali_silang`) + kendali detektor buatan.

---

## 6. Penomoran aturan: DITUNDA dengan sengaja

Dua aturan layak diresmikan (jurnal 127 §9):

- **Calon A** — uji arah waktu wajib perbandingan STRIKT, kelas `serempak`
  dilapor tersendiri dan tidak pernah di numerator.
- **Calon B** — bila satu bulan kalender menguasai ≥ 1/4 numerator, klaim wajib
  dilapor bersama cacah per bulan dan ditandai kemungkinan artefak satu peristiwa.

Nomornya TIDAK ditetapkan karena catatan penomoran di ingatan saling
bertentangan ("calon 77, 78" sementara aturan 79 sudah dipakai). **Tetapkan nomor
HANYA sesudah `STATE_LAMPIRAN.md` dibaca UTUH.** Menomori dari ingatan = KC-41.

**KC-41 baru giliran ini:** `STATE_LAMPIRAN_UKUR.md` v5 menulis `lubang_awal.yml`
ber-`paths` pada modul + berkas uji + workflow sendiri. Berkas asli (blob
`3134bc9f`) memuat SATU entri: `- 'lux_ai/serapan/lubang_awal.py'`. Wajib
dikoreksi di STATE v46.

---

## 7. Isi WAJIB STATE v46 (utang nomor satu)

1. Papan skor **306** (TEPAT 215 / MELESET 56 / SEPARUH 20 / TT 8 / MENUNGGU 7).
2. CI **1044**, run 30524631516; aturan 57 kini **25/25**.
3. **ADR-A013 DITERIMA** — pemilahan tebing / bukan-tebing wajib.
4. Modul `lubang_tebing` V1: sidik kode
   `4a5c2e4279eb1554dc119b48d6a8db61f6ea4ee11b7539efd70ee71d1ae18bf3`,
   blob `575e777e`, uji 60 butir blob `bf57d69d`, workflow blob `c8ae552a`.
5. Angka R-306: 118 = 40 `mati_dulu` + 78 `serempak` + 0 `lubang_dulu`;
   bagian 0.339; tebing 39 (bagian 0.3305); BTCSTUSDT satu-satunya bukan-tebing.
6. **Koreksi KC-41** tentang `paths` `lubang_awal.yml` (§6).
7. Cacah direktori: serapan 44, workflows 39, tests 48 — tandai bahwa cacah
   `tests/` belum dicacah tangan sesudah trio.
8. Praregistrasi R-307 disalin apa adanya dari jurnal 127 §7.
9. Dua calon aturan A dan B dengan status "belum bernomor".

Tulis STATE dalam **tiga berkas terpisah** (`STATE.md`,
`STATE_LAMPIRAN_EKOR.md`, `STATE_LAMPIRAN_UKUR.md`) dan JANGAN lampaui ~45 KB
per berkas; STATE ~55 KB pernah terpotong sunyi (KC-42). Baca ulang UTUH
sesudah push.

---

## 8. Batasan lingkungan (tetap berlaku)

- Sandbox **tanpa jaringan**. Pengukuran hanya berjalan lewat GitHub Actions,
  dipicu oleh push ke `paths` workflow yang bersangkutan.
- `push_files` **menulis ulang seluruh berkas** (bukan tambal). Batas aman
  ±25–45 KB. Pernah gagal dengan galat "Failed to connect to MCP server" dan args
  ter-truncate — selalu periksa commit sesudahnya.
- Pembacaan >±30.000 token dipotong. Laporan besar dibaca dengan `ref` tetap.
- Runner punya numpy / pandas / pyarrow / pyyaml / pytest. **Tidak ada** scipy,
  tidak ada requests.
- Alat GitHub: `get_file_contents` (akhiran `/` melisting direktori; tanpa `ref` =
  tip main), `push_files`, `create_or_update_file` (butuh sha), `list_commits`,
  `get_commit`, `search_code` (selalu 0 hasil — jangan bergantung padanya).
  **Tidak ada** alat Actions/workflow-run: status run hanya lewat berkas
  `reports/*_status.json` dan `reports/ci_terakhir.json`.
- Panggilan: `connections.mcpServer_github.runTool({toolName, toolArguments})`;
  `owner`/`repo` HANYA di dalam `toolArguments`.

---

## 9. Pola trio yang sudah terbukti (ikuti apa adanya)

Satu `push_files` atomik berisi tiga berkas:

1. `lux_ai/serapan/<modul>.py` — tetapan penggugur, `sidik_kode()` atas
   `BERKAS_DICAP` (SERTAKAN setiap modul yang ikut menentukan angka),
   `kendali_deteksi()` buatan, `uji_r<nnn>()` yang mengadjudikasi pita sendiri,
   `kode_keluar()` → 2 bila laporan tak berhak diklaim, `main()` menulis
   `reports/<modul>.json`.
2. `tests/test_<modul>.py` — butir dinamai `test_01`..`test_NN` tanpa
   `parametrize`, agar cacah dapat diverifikasi dengan mata.
3. `.github/workflows/<modul>.yml` — tiru berkas ASLI yang sudah ada (mis.
   `lubang_awal.yml`, blob `3134bc9f`), `paths` hanya modulnya,
   `permissions: contents: write`, langkah jalan + tulis status + commit laporan
   `[skip ci]` + `exit ${{ steps.jalan.outputs.kode }}`.

Push trio menyalakan DUA workflow: `ci` (paths `lux_ai/**`, `tests/**`) dan
workflow modulnya.

---

## 10. API terverifikasi (dibaca utuh, aman dipakai)

- `kehidupan`: `STATUS_MATI="MATI"`, `STATUS_SEPI="SEPI"`, `STATUS_HIDUP="HIDUP"`,
  `STATUS_TAK_TERUKUR`, `STATUS_TERUKUR`, `BULAN_MULAI="2025-07"`,
  `BULAN_AKHIR="2026-06"`, `deret_bulan`, `klasifikasi`, `penyebut_ganda`.
- `kohort_ekor` V4: `TEBING="2025-07"`, `BULAN_DIHARAPKAN="2026-06"`,
  `BATAS_SIMBOL=10`, `PAGU_MUNDUR=60`, `AMBANG_SEPI=0.5`,
  `bagian(pembilang, penyebut)` (4 desimal, None bila penyebut 0), `mundur_bulan`,
  `baca_zip_klines`, `ringkas_lilin`, `muat_kohort`,
  `KENDALI_HIDUP=("BTCUSDT","ETHUSDT")`.
- `silang_funding` V2: `baca_laporan_kehidupan(akar,total) → (status, byte_parquet, meta)`,
  `lubang_funding(funding) → (Set[(simbol,bulan)], meta)`,
  `bentuk_lubang_lokal(...) → bukan_lubang|awal|ekor|seluruh|tengah`,
  `kendali_silang`, `kendali_sah`, `bulan_per_simbol`,
  `SUMBER_FUNDING="reports/funding_semesta.json"`, `TOTAL_PECAHAN`,
  `BENTUK_TERBITAN_FUNDING={"awal":48,"ekor":826,"tengah":6}`.
- `lubang_awal` V1: `peta_status`, `bulan_urut`, `ringkas(simbol,peta,berlubang)`,
  `himpun`, `kendali_deteksi`, `bangkit_lokal`, `BATAS_BARIS_LAPORAN=60`.
  Medan: `bulan_mati_pertama`, `bulan_lubang_bukan_awal_pertama`,
  `bulan_pertama_berlubang`, `akhir_lubang_awal`, `cacah_lubang_awal`,
  `cacah_lubang_bukan_awal`, `masuk_penyebut_butir_1`,
  `mati_tidak_setelah_lubang_bukan_awal` (`<=`, JANGAN dipakai untuk klaim arah),
  `lubang_awal_berakhir_sebelum_mati`, `bangkit`, `cacah_bulan`, `bulan_pertama`,
  `bulan_terakhir`, `cacah_mati`, `cacah_lubang`.
- `lubang_tebing` V1 (baru): `kelas_arah`, `di_tebing`, `perkaya`, `sebaran_arah`,
  `himpun`, `kendali_deteksi`, `dalam_pita`, `uji_r306`, `kode_keluar`,
  `KELAS_ARAH=("mati_dulu","serempak","lubang_dulu")`.

---

## 11. Angka semesta (terkunci, jangan hitung ulang dari ingatan)

Penyebut **19.586** simbol-bulan; **787** simbol; **1.401** MATI (842 kehilangan
funding, 559 berfunding); **98** SEPI; **18.087** HIDUP;
`cacah_simbol_tanpa_hidup` 18; lubang funding **880** semesta / **877** dalam
penyebut / 3 tak dikenal; 33 HIDUP tanpa funding;
`cacah_simbol_ada_lubang` **122** (lubang_awal **5**, bukan_awal **118**, BNXUSDT
keduanya). Lima bentuk AWAL: BNXUSDT, ICPUSDT, JUPUSDT, QTUMUSDT, TLMUSDT
(BNX/JUP/QTUM berakhir sebelum mati; ICP/TLM tidak).

Delapan simbol bangkit: CVCUSDT 29, CVXUSDT 13, SLPUSDT 13, CTKUSDT 11,
LITUSDT 10, TLMUSDT 8, ICPUSDT 2, MAVIAUSDT 2 = 88. Lima tanpa lubang: CVC, CVX,
SLP, CTK, MAVIA. LITUSDT satu-satunya `mati_dulu` di antara yang bangkit.

Sidik kode: `lubang_tebing` V1 `4a5c2e42…`, `lubang_awal` V1 `156499ce…`,
`sebab_bangkit` V1 `bafe4359…`, `silang_funding` V2 `8a9b859c…`,
`tersisip_semesta` V1 `9618fd19…`, `bentangan_kohort` V2 `8ca6ebbe…`,
laporan kehidupan seragam `24b6bb26…`, `sidik_data_funding` `2c9fbd1b…`.

---

## 12. Utang yang masih hidup

1. **STATE v46** (§7) — nomor satu.
2. Aturan 52: `tests/test_bentangan_kohort.py` V2 (63 butir, blob `9f850ecd`)
   belum dibaca byte demi byte.
3. Belum dibaca utuh: `decisions/ADR-A002.md`, A004, A006, A007, A008,
   `PETA_MODUL.md`, `PETA_MODUL_BERKAS.md`, `STATE_LAMPIRAN.md`,
   `STATE_LAMPIRAN_ANGKA.md`, `karantina_semesta.yml` (`de40fa4e`),
   `tests/test_pulihkan.py` (`11c43533`), `test_rilis_karantina.py` (`739c8da9`),
   `test_karantina_a006.py` (`a5a3d82f`).
4. Adjudikasi tertunda: R-7, R-19, R-20, R-28, R-36, R-37, R-199; gali R-28 dari
   STATE v23 (KC-32); salin R-236..R-247 dari jurnal 92–94.
5. ADR A003 / A005 / A006 / A007 belum diputuskan.
6. Pertanyaan terbuka: irisan **880 lawan 877**; selisih **40−38** `diagnosa_kc15`;
   tanggal hari hilang BNXUSDT 2022-04 / 06 / 08; bentangan 38 kohort puncak;
   `mati_tersisip` atas 19.586; celah kelipatan 15 menit (H-A016);
   `ukur_baris` V6 (KC-26); **taksonomi lubang tiga kelas** (awal / delisting /
   tebing) — naik prioritas karena ADR-A013.

---

## 13. Nada kerja

Ukur, jangan mengarang. Bila angka belum diukur, katakan belum diukur. Bila
ramalan meleset, tulis MELESET dan cari sebabnya. Kemenangan yang tidak
mengajarkan apa pun (seperti R-306 butir 1) wajib dinyatakan lemah walau menang.
Tutup setiap giliran dengan jurnal, dan tinggalkan PROMPT + STATE yang bisa
dipakai orang lain tanpa bertanya apa pun.
