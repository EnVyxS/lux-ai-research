# PROMPT v50 — serah terima LUX-AI

Operator: **Diva Juan Nur Taqarrub** (GitHub **EnVyxS**).
Repo tulis: **`EnVyxS/lux-ai-research`**. Tenggat proyek: **2026-08-02**.
Ditulis: 2026-07-30 sesudah STATE v46 terbit dan diverifikasi.
Menggantikan PROMPT v49 (blob `4dca042c9bdb9a7b8e664200690ae6217a88dfe0`).

**Mengapa v50 lahir hanya beberapa menit sesudah v49.** v49 memuat tiga pernyataan
yang langsung menjadi salah: ia menulis "STATE v46 BELUM ADA" (kini ada), "penomoran
aturan DITUNDA" (kini selesai: **80** dan **81**), dan melabeli poros R-307 sebagai
"H-A017" (label itu SALAH; yang benar **H-A018**). Membiarkan berkas yang pertama
dibaca LANGKAH 0 dalam keadaan salah sama dengan menanam KC-41 untuk giliran
berikutnya.

---

## LANGKAH 0 — WAJIB SEBELUM PEKERJAAN APA PUN

Jangan menulis kode, jangan mendorong berkas, jangan mengklaim angka sebelum
keempat hal ini selesai:

1. Baca **PROMPT.md** (berkas ini) UTUH dari main.
2. Baca ketiga berkas STATE **v46** UTUH:
   - `STATE.md` — blob **`41b5b585d202a2486ba6f15a0c0100d90e728dea`**
   - `STATE_LAMPIRAN_EKOR.md` v6 — blob **`f3b2f5dd6c2dd58ec4ae438a6af9d3a65a69c5ed`**
   - `STATE_LAMPIRAN_UKUR.md` v6 — blob **`27e59a79dacc9a07091c948c0f955491b1247478`**
3. Baca **jurnal 127** (`journal/2026-07-30-127.md`, blob `9b5015eb`) dan
   **ADR-A013** (`decisions/ADR-A013.md`, blob `3a7f8612`) UTUH.
4. Baca `reports/ci_terakhir.json` untuk cacah uji CI **terukur** — jangan mengarang
   cacah uji. Nilai terakhir yang diketahui: **1044**.

Sesudah itu, catat di jawaban pertama: papan skor, penomoran berikutnya, dan utang
aturan 52 yang masih hidup.

**Peringatan khusus:** `STATE_LAMPIRAN_UKUR.md` v6 dibuka dengan bagian
"KOREKSI KC-41". Baca bagian itu sebelum mengutip apa pun dari lampiran versi lama.

---

## 1. Aturan yang paling sering dilanggar (baca ini dua kali)

- **Aturan 29 — adjudikasi jujur.** Pita praregistrasi TIDAK BOLEH diubah sesudah
  pengukuran. MELESET dicatat MELESET. Kemenangan yang tidak mengajarkan apa pun
  wajib dinyatakan lemah walau menang (contoh: R-306 butir 1).
- **Aturan 52 — baca utuh.** Sesudah `push_files`, baca ulang setiap berkas UTUH dari
  main. `push_files` pernah memotong berkas besar dalam sunyi (KC-42); batas tulis
  aman ±**25–45 KB** per berkas.
- **Aturan 55 / KC-41 — jangan mengutip rumusan dari ingatan.** Kelas cacat paling
  sering berulang di repo ini. Dua kasus baru tertangkap pada sesi 59, **keduanya
  pada dokumen kami sendiri** (lampiran UKUR v5 dan PROMPT v49). Rumusan pemicu
  workflow, label hipotesis, dan nomor aturan WAJIB dikutip dari berkas beserta
  blobnya pada giliran yang sama. Bila dua bagian STATE bertentangan, **berkas sumber
  menang**, bukan yang lebih baru.
- **Aturan 66 — cacah direktori dengan tangan** sebelum menamai modul baru. Pada
  sesi 59 aturan itu mencegah `lubang_tengah.py` tertimpa.
- **Aturan 57 — ramalkan cacah uji SEBELUM push**, lalu ukur. Kini **25/25** tepat.
- **Aturan 79 — praregistrasi lebih dulu**, di `journal/**` (ada di `paths-ignore`),
  SEBELUM modul pengukurnya dibuat.
- **Aturan 80 (BARU, resmi v46) — uji arah waktu wajib STRIKT**, dan kelas
  `serempak` (tanggal SAMA) dilapor tersendiri, **DILARANG masuk numerator**.
- **Aturan 81 (BARU, resmi v46) — bila satu bulan kalender menguasai ≥ 1/4
  numerator**, klaim wajib dilapor bersama cacah per bulan, ditandai kemungkinan
  artefak satu peristiwa, dan kekuatan bukti yang LEPAS dari bulan itu dinyatakan apa
  adanya.
- **Aturan 10 + KC-47 + ADR-A013 — irisan bukan sebab, dan satu peristiwa bukan
  banyak pengamatan.** Lihat §4.

---

## 2. Posisi sekarang

- Commit terakhir yang ditulis giliran ini: **`ce3e8c033d084ac17c1c63ca2e349ac7e1a0d9b8`**
  (STATE v46 tiga berkas), di atas `b64ce46c` (PROMPT v49), `8ba4f989` (jurnal 127 +
  ADR-A013), `84b11164` (trio `lubang_tebing`). Bot laporan CI menambah commit
  sesudahnya — **selalu baca tip main yang sebenarnya, jangan asumsikan.**
- **Papan skor R-1..R-306 = 306**: TEPAT **215** / MELESET **56** / SEPARUH **20** /
  TIDAK TERADJUDIKASI **8** / MENUNGGU **7**.
  MENUNGGU: R-7, R-19, R-20, R-28, R-36, R-37, R-199. `N_percobaan` = 0.
  **ADJUDIKASI RISET TETAP TERKUNCI.**
- **CI terukur 1044** (run **30524631516**, commit `84b11164`, kode 0). Riwayat:
  630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 → 984 → **1044**.
  Push STATE/PROMPT menyalakan `ci.yml` tetapi tidak mengubah `tests/**`, jadi cacah
  seharusnya TETAP 1044 — **ukur, jangan asumsikan.**
- Cacah direktori: `lux_ai/serapan/` **44** `.py`, `.github/workflows/` **39**,
  `tests/` **48**. Angka 44 dan 39 sahih (43/38 dicacah tangan + 1). **Angka 48
  adalah turunan 47 + 1 dan BELUM dicacah tangan** — cacah langsung sebelum dikutip
  (aturan 66).
- **STATE v46 SUDAH ADA dan terverifikasi utuh** (blob di LANGKAH 0). Tidak ada utang
  STATE. STATE berikutnya v47.

---

## 3. Penomoran berikutnya

| hal | berikutnya |
| --- | --- |
| jurnal | **128** |
| STATE | **v47** |
| PROMPT | **v51** |
| ADR | **A014** |
| aturan resmi | **82** (resmi sampai **81**; **77** dan **78** TETAP usulan) |
| KC resmi | **KC-48** (resmi sampai KC-47; KC-16 kosong selamanya) |
| hipotesis | **H-A019** (terbuka: H-A016, H-A018) |
| ramalan | **R-307** (terkunci, jurnal 127 §7), lalu R-308 |
| papan skor sesudah R-307 | **307** |

**Catatan penomoran aturan (diselesaikan dari berkas, bukan ingatan):** 77 dan 78
memang masih DIUSULKAN dan belum pernah berlaku, sementara 79 sudah BERLAKU — nomor
di repo ini tidak selalu diberikan berurutan. Karena itu aturan baru sesi 59
mengambil 80 dan 81.

---

## 4. Apa yang baru dipelajari (jangan diulang)

R-306 = **TEPAT 3/3**, dan justru kemenangan itulah yang paling wajib dikecilkan.

Penyebut 118 simbol (berlubang funding bukan-awal) terpecah dengan perbandingan
STRIKT: `mati_dulu` **40** / `serempak` **78** / `lubang_dulu` **0**. Bagian strikt
**0.339** (pita 0.25..0.60 → MENANG). Cacah tebing **39** (pita 20..90 → MENANG).

Lalu pemilahan lanjutan: **39 dari 40** simbol `mati_dulu` ber-lubang-bukan-awal
pertama TEPAT `2025-07`. Hanya **BTCSTUSDT** yang lepas (lubang 2022-01, MATI
2021-04). Jadi "arah waktu" bukan 40 pengamatan bebas melainkan **satu peristiwa
penerbitan yang menimpa 39 bangkai**; derajat kebebasan efektif ≈ 1.

→ **KC-47** (satu peristiwa menyamar sebagai banyak pengamatan bebas) dan **aturan
81**. Yang membuat KC-47 berbahaya: ia LOLOS dari penyebut yang benar, dari kendali
positif, DAN dari perbandingan strikt — ketiganya sudah diterapkan di R-306.

**Akibat strategis:** poros lubang/funding sudah kehabisan kejutan — R-304, R-305,
dan R-306 semuanya berujung ke peristiwa `2025-07` yang sama. R-307 sengaja pindah
poros.

---

## 5. R-307 — PRAREGISTRASI TERKUNCI (jurnal 127 §7, JANGAN DIUBAH)

Poros: **H-A018** — byte parquet sebagai gejala kehidupan, atas semesta 19.586
simbol-bulan, yang belum pernah dijumlahkan sekali pun.

> **Koreksi label (KC-41).** PROMPT v49 menyebut poros ini "H-A017". **Itu salah:**
> H-A017 adalah hipotesis arah sebab (LITUSDT) yang sudah dicabut sebagai pola. Byte
> parquet dulu hanya PENGAMATAN di ekor H-A017 dan kini dinaikkan menjadi hipotesis
> tersendiri **H-A018** (lampiran UKUR v6). **Pita di bawah TIDAK berubah** — yang
> salah label, bukan angkanya, jadi aturan 29 tetap utuh.

- **Butir 1 (BERISIKO).** Bagian byte parquet milik simbol-bulan berstatus **MATI**
  atas TOTAL byte parquet seluruh 19.586 simbol-bulan. Pita **0.02 .. 0.15**. Bila
  total byte = 0 → TIDAK TERADJUDIKASI (aturan 41).
- **Butir 2 (BERISIKO).** Cacah simbol-bulan berstatus **TERUKUR** (HIDUP atau SEPI)
  yang `byte_parquet` **< 10.000**. Pita **20 .. 400**.
- **Butir 3 (MUDAH).** Sembilan invarian penggugur tetap nol, kedua kendali sah,
  kode keluar 0, cacah uji CI **diukur**.

Sembilan invarian penggugur (aturan 24): penyebut **19.586**, simbol **787**, MATI
**1.401**, bangkit **8**, lubang dalam penyebut **877**, lubang semesta **880**,
ada_lubang **122**, lubang_awal **5**, lubang_bukan_awal **118**.

**Sumber byte sudah tersedia — tidak perlu pembaca baru:**
`silang_funding.baca_laporan_kehidupan(akar, total)` mengembalikan
`(status, byte_parquet, meta)`. Kendali dua lapis WAJIB: kendali data
(`silang_funding.kendali_silang`) + kendali detektor buatan (aturan 50), karena butir
2 dapat berujung pada cacah kecil atau nol.

**Nama modul R-307 WAJIB dicek lewat pencacahan direktori lebih dulu** (aturan 66) —
pelajaran `lubang_tengah`.

---

## 6. Pola trio yang sudah terbukti (ikuti apa adanya)

Satu `push_files` atomik berisi tiga berkas (aturan 45):

1. `lux_ai/serapan/<modul>.py` — tetapan penggugur, `sidik_kode()` atas
   `BERKAS_DICAP` (SERTAKAN setiap modul yang ikut menentukan angka),
   `kendali_deteksi()` buatan, `uji_r<nnn>()` yang mengadjudikasi pitanya sendiri,
   `kode_keluar()` → 2 bila laporan tak berhak diklaim, `main()` menulis
   `reports/<modul>.json`. **Rancang laporan agar RINGKAS** — laporan `lubang_tebing`
   terpotong saat dibaca (batas ±30.000 token) karena daftar barisnya panjang.
2. `tests/test_<modul>.py` — butir dinamai `test_01`..`test_NN` tanpa `parametrize`,
   agar cacah dapat diverifikasi dengan mata (aturan 54, 57).
3. `.github/workflows/<modul>.yml` — tiru berkas ASLI yang sudah ada, mis.
   `lubang_awal.yml` (blob `3134bc9f`), yang `paths`-nya berisi **SATU** entri:
   `- 'lux_ai/serapan/lubang_awal.py'`. Sertakan `permissions: contents: write`,
   langkah jalan + tulis status + commit laporan `[skip ci]` +
   `exit ${{ steps.jalan.outputs.kode }}`.

Push trio menyalakan DUA workflow: `ci` (paths `lux_ai/**`, `tests/**`) dan workflow
modulnya. Ramalkan cacah uji CI sebelum push, lalu ukur dari `ci_terakhir.json`.

---

## 7. Batasan lingkungan (tetap berlaku)

- Sandbox **tanpa jaringan**. Pengukuran hanya berjalan lewat GitHub Actions, dipicu
  oleh push ke `paths` workflow yang bersangkutan.
- `push_files` **menulis ulang seluruh berkas** (bukan tambal). Batas aman ±25–45 KB.
  Pernah gagal dengan galat "Failed to connect to MCP server" dan args ter-truncate —
  selalu periksa commit sesudahnya sebelum mendorong ulang.
- Pembacaan >±30.000 token dipotong (terjadi pada `reports/lubang_tebing.json`).
  Laporan besar dibaca dengan `ref` tetap.
- Runner punya numpy / pandas / pyarrow / pyyaml / pytest. **Tidak ada** scipy, tidak
  ada requests.
- Alat GitHub: `get_file_contents` (akhiran `/` melisting direktori; tanpa `ref` = tip
  main), `push_files`, `create_or_update_file` (butuh sha), `list_commits`,
  `get_commit`, `search_code` (selalu 0 hasil — jangan bergantung padanya).
  **Tidak ada** alat Actions/workflow-run: status run hanya lewat berkas
  `reports/*_status.json` dan `reports/ci_terakhir.json`.
- Panggilan: `connections.mcpServer_github.runTool({toolName, toolArguments})`;
  `owner`/`repo` HANYA di dalam `toolArguments`.
- `ci.yml` (blob `c79497b2`) ber-`paths-ignore` journal / decisions / hipotesis /
  reports; push ke `lux_ai/**`, `tests/**`, `STATE*`, `PROMPT*` MENYALAKAN CI.

---

## 8. API terverifikasi (dibaca utuh, aman dipakai)

- `kehidupan` (`f49abb2b`): `STATUS_MATI="MATI"`, `STATUS_SEPI="SEPI"`,
  `STATUS_HIDUP="HIDUP"`, `STATUS_TAK_TERUKUR`, `BULAN_MULAI="2025-07"`,
  `BULAN_AKHIR="2026-06"`, `deret_bulan`, `klasifikasi`, `penyebut_ganda`.
- `kohort_ekor` V4 (`c9b63bbe`): `TEBING="2025-07"`, `BULAN_DIHARAPKAN="2026-06"`,
  `BATAS_SIMBOL=10`, `PAGU_MUNDUR=60`, `AMBANG_SEPI=0.5`, `bagian` (4 desimal, None
  bila penyebut 0), `KENDALI_HIDUP=("BTCUSDT","ETHUSDT")`.
- `silang_funding` V2 (`42c3aa9d`): `baca_laporan_kehidupan(akar,total)` →
  `(status, byte_parquet, meta)`; `lubang_funding(funding)` →
  `(Set[(simbol,bulan)], meta)`; `bentuk_lubang_lokal(...)` →
  bukan_lubang|awal|ekor|seluruh|tengah; `kendali_silang`, `kendali_sah`,
  `bulan_per_simbol`, `SUMBER_FUNDING="reports/funding_semesta.json"`,
  `BENTUK_TERBITAN_FUNDING={"awal":48,"ekor":826,"tengah":6}`.
- `kehidupan_arsip` (`318a5cb1`): `TOTAL_PECAHAN=8`.
- `lubang_awal` V1 (`8c36943d`): `peta_status`, `bulan_urut`, `ringkas`, `himpun`,
  `kendali_deteksi`, `bangkit_lokal`, `BATAS_BARIS_LAPORAN=60`. Medan
  `mati_tidak_setelah_lubang_bukan_awal` memakai `<=` — **DILARANG untuk klaim arah**
  (aturan 80).
- `lubang_tebing` V1 (`575e777e`): `kelas_arah`, `di_tebing`, `perkaya`,
  `sebaran_arah`, `himpun`, `kendali_deteksi`, `dalam_pita`, `uji_r306`,
  `kode_keluar`, `KELAS_ARAH=("mati_dulu","serempak","lubang_dulu")`,
  `BATAS_BARIS_LAPORAN=60`. Sidik
  `4a5c2e4279eb1554dc119b48d6a8db61f6ea4ee11b7539efd70ee71d1ae18bf3`.

---

## 9. Angka semesta (terkunci, jangan hitung ulang dari ingatan)

Penyebut **19.586** simbol-bulan; **787** simbol; **1.401** MATI (842 kehilangan
funding, 559 berfunding); **98** SEPI; **18.087** HIDUP; `cacah_simbol_tanpa_hidup`
18; lubang funding **880** semesta / **877** dalam penyebut / 3 tak dikenal; 33 HIDUP
tanpa funding; `cacah_simbol_ada_lubang` **122** (lubang_awal **5**, bukan_awal
**118**, BNXUSDT keduanya). Lima bentuk AWAL: BNXUSDT, ICPUSDT, JUPUSDT, QTUMUSDT,
TLMUSDT (BNX/JUP/QTUM berakhir sebelum mati; ICP/TLM melewati kematian — KC-46).

R-306: penyebut 118 = `mati_dulu` **40** + `serempak` **78** + `lubang_dulu` **0**;
bagian 0.339; tebing **39** (bagian 0.3305); satu-satunya bukan-tebing **BTCSTUSDT**.

Delapan simbol bangkit: CVCUSDT 29, CVXUSDT 13, SLPUSDT 13, CTKUSDT 11, LITUSDT 10,
TLMUSDT 8, ICPUSDT 2, MAVIAUSDT 2 = 88. Lima tanpa lubang: CVC, CVX, SLP, CTK,
MAVIA. LITUSDT satu-satunya `mati_dulu` di antara yang bangkit.

Sidik kode: `lubang_tebing` V1 `4a5c2e42…`, `lubang_awal` V1 `156499ce…`,
`sebab_bangkit` V1 `bafe4359…`, `silang_funding` V2 `8a9b859c…`, `tersisip_semesta`
V1 `9618fd19…`, `bentangan_kohort` V2 `8ca6ebbe…`, laporan kehidupan seragam
`24b6bb26…`, `sidik_data_funding` `2c9fbd1b…`.

---

## 10. Utang yang masih hidup (urut prioritas)

1. **Bangun trio R-307** (modul H-A018 byte parquet) — praregistrasi sudah terkunci,
   jadi pekerjaan berikutnya adalah mengukurnya. Cacah direktori dulu (aturan 66).
2. **Cacah tangan `tests/`** untuk menggantikan angka turunan 48.
3. Aturan 52: `tests/test_bentangan_kohort.py` V2 (63 butir, blob `9f850ecd`) belum
   dibaca byte demi byte.
4. Belum dibaca utuh: `decisions/ADR-A002.md`, A004, A006, A007, A008,
   `PETA_MODUL.md`, `PETA_MODUL_BERKAS.md`, `STATE_LAMPIRAN.md`,
   `STATE_LAMPIRAN_ANGKA.md`, `karantina_semesta.yml` (`de40fa4e`),
   `tests/test_pulihkan.py` (`11c43533`), `test_rilis_karantina.py` (`739c8da9`),
   `test_karantina_a006.py` (`a5a3d82f`).
5. Adjudikasi tertunda: R-7, R-19, R-20, R-28, R-36, R-37, R-199; gali R-28 dari
   STATE v23 (KC-32); salin R-236..R-247 dari jurnal 92–94.
6. ADR A003 / A005 / A006 / A007 belum diputuskan; **A003 wajib memuat koreksi
   A011/A012/A013**.
7. Pertanyaan terbuka: mengapa 39 simbol berhenti berfunding tepat `2025-07` padahal
   bulan MATI mereka tersebar 2022-12..2025-05 (dugaan BELUM diuji: `2025-07` adalah
   batas penerbitan/arsip data funding, bukan peristiwa pasar)? Mengapa BTCSTUSDT
   satu-satunya yang lepas? Lalu: irisan **880 lawan 877**; selisih **40−38**
   `diagnosa_kc15`; tanggal hari hilang BNXUSDT 2022-04/06/08; bentangan 38 kohort
   puncak; `mati_tersisip` atas 19.586; H-A016 (celah kelipatan 15 menit);
   `ukur_baris` V6 (KC-26); **taksonomi lubang tiga kelas** (awal / delisting /
   tebing) — naik prioritas karena ADR-A013.

---

## 11. Nada kerja

Ukur, jangan mengarang. Bila angka belum diukur, katakan belum diukur. Bila ramalan
meleset, tulis MELESET dan cari sebabnya. Kemenangan yang tidak mengajarkan apa pun
wajib dinyatakan lemah walau menang. Bila dokumen sendiri bertentangan dengan berkas
sumber, berkas sumber menang dan dokumen dikoreksi pada giliran itu juga. Tutup
setiap giliran dengan jurnal, dan tinggalkan PROMPT + STATE yang bisa dipakai orang
lain tanpa bertanya apa pun.
