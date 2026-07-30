# PROMPT KELANJUTAN — v48

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
   - `STATE.md` v44 (bagian 1: aturan + KC) — STATE v45 masih UTANG, lihat bawah
   - `STATE_LAMPIRAN_EKOR.md` v4 (bagian 2: papan skor, ADR, catatan)
   - `STATE_LAMPIRAN_UKUR.md` v4 (bagian 3: pengukuran, modul, API, hipotesis)
   - `journal/2026-07-30-126.md` (adjudikasi R-305 + praregistrasi R-306)
   - `decisions/ADR-A012.md` (arah sebab A009 dicabut seluruh semesta)
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
  kali (KC-42): commit BUKAN bukti keutuhan. Pecah STATE bila perlu.
- Batas baca: hasil >±30.000 token DIPOTONG. `reports/funding_semesta.json` hanya
  terbaca 27% → TIDAK terukur utuh.
- MCP GitHub kadang gagal "Failed to connect to MCP server"; ULANGI panggilan,
  jangan menyerah. `push_files` yang gagal-koneksi TIDAK menulis apa pun
  (diperiksa lewat `list_commits` giliran ini).
- `search_code` mengembalikan 0 hasil — pakai `get_file_contents`; path berakhiran
  garis miring melisting direktori.
- Runner punya numpy, pandas, pyarrow, pyyaml, pytest; TIDAK ada scipy/requests.
- Dilarang menulis apa pun di luar repo `lux-ai-research`; `lux-research` baca saja.
- `ci.yml` memakai `paths-ignore` (journal/**, decisions/**, hipotesis/**,
  reports/**). Push ke `lux_ai/**`, `tests/**`, `STATE*`, `PROMPT*` MENYALAKAN CI;
  push jurnal/decisions/reports TIDAK. Tiap workflow ukur meng-commit
  json/log/status SENDIRI-SENDIRI (KC-44).

---

## POSISI SERAH TERIMA (30 Juli 2026, ±14:30 WIB)

HEAD main = commit jurnal 126 + ADR-A012 + PROMPT v48 (push giliran ini); CI akan
menambah satu commit `reports/ci_terakhir.json` sesudahnya (tetap 984). Sebelumnya:
`d304d3eb` = trio `lubang_awal` V1; `2888df0c` = CI 984; `0deef07e` = laporan
`lubang_awal` run 30522785043.

Papan skor R-1..R-305: TEPAT **214** / MELESET **56** / SEPARUH **20** /
TIDAK TERADJUDIKASI **8** / MENUNGGU **7** = **305**.
MENUNGGU: R-7, R-19, R-20, R-28, R-36, R-37, R-199.
N_percobaan = 0. ADJUDIKASI RISET TETAP TERKUNCI.
Aturan sampai 79 (resmi). KC sampai KC-44 (KC-45, KC-46 wajib diangkat di STATE
v45). Hipotesis terbuka H-A016, H-A017 (LITUSDT saja).
Jurnal berikutnya 127. STATE v45. ADR A013. Ramalan R-306 sudah dipraregistrasi di
jurnal 126 §7; berikutnya R-307.

---

## PEKERJAAN PERTAMA, BERURUTAN

1. **UTANG TERBESAR — STATE v45 (tiga berkas).** Angkat papan skor ke 305
   (MELESET 56), catat ADR-A012, angkat KC-45 (satuan bulan wajib tersurat) dan
   KC-46 (periksa bentuk lubang sebelum tafsir arah waktu) menjadi KC RESMI,
   catat modul `lubang_awal` V1 + sidik kodenya. Tulis per berkas ≤±45 KB dan
   BACA ULANG tiap berkas dari main sesudahnya (KC-42/aturan 52).
2. Baca `reports/ci_terakhir.json` untuk memastikan cacah CI sesudah push STATE
   v45 (harapan tetap 984 kecuali ada butir uji baru — wajib DIUKUR).
3. **Praregistrasi R-306 sudah terkunci di jurnal 126 §7.** Bangun trio penguji
   R-306 yang HANYA menambah dua agregat di atas medan `lubang_awal` V1
   (`bulan_mati_pertama` vs `bulan_lubang_bukan_awal_pertama`, dan kesamaan dengan
   `kohort_ekor.TEBING`). Impor `TEBING` apa adanya (aturan 36). Listing
   `lux_ai/serapan/` (kini 42) dan `.github/workflows/` (kini 37) dicacah tangan
   sebelum menulis; nama baru wajib bebas.
4. Dorong trio R-306 atomik (satu `push_files`): modul + uji bernomor `test_01`…
   + workflow meniru `lubang_awal.yml`.
5. Sesudah run: baca status.json, .json, .log; cocokkan run_id/commit/sidik_kode;
   bayar aturan 52 (baca ulang modul + berkas uji dari main).
6. Adjudikasi R-306 JUJUR terhadap praregistrasi jurnal 126 §7; dilarang menawar
   sesudah angka terlihat (aturan 29).
7. Jurnal 127 → ADR A013 bila perlu → PROMPT v49.

---

## TEMUAN WAJIB DIBAWA (dari R-305, `lubang_awal` V1 run 30522785043)

- **Butir 1 = 100% (118/118) TAUTOLOGIS.** Tidak ada simbol yang mati SESUDAH
  lubang bukan-awal pertama, tetapi itu karena lubang bukan-awal sering ADALAH
  bulan delisting, atau muncul di tebing 2025-07 lama sesudah kematian. Bukan
  bukti arah sebab (aturan 10).
- **Lubang bentuk AWAL langka: 5 dari 787** — BNXUSDT, ICPUSDT, JUPUSDT,
  QTUMUSDT, TLMUSDT. Dari 5, tiga (BNX, JUP, QTUM) lubang awalnya berakhir
  sebelum mati / tak pernah mati; dua (ICP, TLM) tidak (bentuk AWAL panjang
  melewati kematian — sumber salah-baca R-304).
- **Hanya 122 dari 787 simbol pernah berlubang funding** (`cacah_simbol_ada_lubang`
  122; lubang awal 5; lubang bukan-awal 118; BNX punya keduanya).
- **Tebing 2025-07 memproduksi lubang bukan-awal** (banyak
  `bulan_lubang_bukan_awal_pertama` = "2025-07"). Inti pertanyaan R-306.
- **CI: 984** (run 30522785099, commit `d304d3eb`, kode 0, 07:23:33Z) = 936 + 48.
- **Sidik kode `lubang_awal` V1:**
  `156499ce9d6e822bb7f57786e8e308955441996699c1fd53d0e8814e1f8f2362`

---

## PRAREGISTRASI R-306 (terkunci di jurnal 126 §7)

- **Butir 1 (BERISIKO):** dari simbol dengan ≥1 MATI dan ≥1 lubang bukan-awal
  (penyebut ≥100), yang `bulan_mati_pertama` **lebih kecil** (bukan sama) daripada
  lubang bukan-awal pertama berjumlah dalam pita **25%..60%**. <100 → TIDAK
  TERADJUDIKASI.
- **Butir 2 (BERISIKO):** cacah simbol yang lubang bukan-awal pertamanya TEPAT
  `kohort_ekor.TEBING` ("2025-07") dalam pita **20..90** dari penyebut butir 1.
- **Butir 3 (MUDAH):** 19.586 / 787, MATI 1.401, lubang 877/880, bangkit 8,
  ada-lubang 122, lubang-awal 5, lubang-bukan-awal 118, kendali sah, kode 0, CI
  diukur.

Akibat: lihat jurnal 126 §7 untuk bunyi lengkap.

---

## KEBIASAAN YANG MENGIKAT

Ramalan SEBELUM run lalu adjudikasi jujur; **praregistrasi di jurnal lebih dulu
(aturan 79, RESMI)**; hitung ulang tiap angka (21); medan penggugur (24); kelas
cacat pada sampel (37); **dilarang menyimpulkan di luar rentang sampel (20) —
dilanggar 9 kali, R-305 termasuk**; kendali positif dua lapis wajib (50); laporan
tak terbaca utuh = tidak ada (52); cacah butir uji dari daftar bernomor (54);
ketiadaan pengukuran bukan ketiadaan gejala (59); listing direktori sebelum
menulis modul baru (66); nama turunan bersama asalnya (69); baca modul penghasil
sebelum meramalkan laporannya (71); jangan meramal isi berkas dari NAMA-nya (73);
setiap nol bersama penyebutnya (74); **irisan/urutan bulan BUKAN sebab (10) —
terbukti tautologis di R-305**; **tanda tangan fungsi dikutip dari kode (KC-43)**;
**tiap laporan di-commit sendiri-sendiri (KC-44)**; **satuan bulan wajib tersurat
(KC-45, angkat resmi)**; **periksa bentuk lubang sebelum tafsir arah waktu
(KC-46, angkat resmi)**; **pakai definisi modul lama apa adanya, jangan tulis
ulang (36)**.

"lanjut"/"lanjutkan" berarti teruskan tanpa konfirmasi. Jangan berhenti dengan
alasan konteks Notion.

---

## PEKERJAAN BERIKUTNYA SESUDAH R-306

Taksonomi lubang tiga kelas (awal/delisting/tebing); pangkas tebing sebelum ukur
lubang (calon aturan baru); H-A017 (byte parquet atas semesta); H-A016 (celah
kelipatan 15 menit); mati_tersisip atas 19.586; `ukur_baris` V6 (KC-26); ADR
A003/A007/A005/A006; adjudikasi R-7/19/20/28/36/37 dan R-199; gali bunyi R-28 dari
STATE v23 (KC-32); R-236..R-247 dari jurnal 92–94; TANGGAL hari hilang BNX
2022-04/06/08; irisan 880 lawan 877; selisih 40−38 `diagnosa_kc15`; bentangan 38
kohort (prasyarat Keputusan 7 ADR-A008).

**Belum dibaca:** `decisions/ADR-A002.md`, A004, A006, A007, A008 (utuh),
`PETA_MODUL.md`, `PETA_MODUL_BERKAS.md`, `STATE_LAMPIRAN.md`,
`STATE_LAMPIRAN_ANGKA.md`, `karantina_semesta.yml` (`de40fa4e`),
`tests/test_pulihkan.py`, `test_rilis_karantina.py`, `test_karantina_a006.py`.

---

## API TERVERIFIKASI (JANGAN DITEBAK)

`lubang_awal` V1 (blob `8c36943d`, sidik `156499ce…`) — impor `kehidupan`,
`kehidupan_arsip`, `silang_funding`; medan per simbol: `bulan_mati_pertama`,
`bulan_lubang_bukan_awal_pertama`, `bulan_pertama_berlubang`, `akhir_lubang_awal`,
`cacah_lubang_awal`, `cacah_lubang_bukan_awal`, `masuk_penyebut_butir_1`,
`mati_tidak_setelah_lubang_bukan_awal`, `lubang_awal_berakhir_sebelum_mati`.
`silang_funding` V2 (`42c3aa9d`, 29.873 B) — `bentuk_lubang_lokal(bulan_urut,
bulan_berlubang, bulan)` → bukan_lubang/awal/ekor/seluruh/tengah;
`baca_laporan_kehidupan(akar,total)`→(status,byte_parquet,meta);
`lubang_funding(funding)`→(Set[(simbol,bulan)],meta); `kendali_silang`,
`kendali_sah`, `SUMBER_FUNDING`. `kehidupan_arsip` V1 (`318a5cb1`,
`TOTAL_PECAHAN=8`, `nama_keluaran(i)`). `kehidupan` (`f49abb2b`, `STATUS_MATI`
="MATI", `STATUS_HIDUP`="HIDUP", `STATUS_SEPI`). `kohort_ekor` V4 (`c9b63bbe`,
`TEBING="2025-07"`, `BULAN_DIHARAPKAN="2026-06"`, `BATAS_SIMBOL=10`).
`sebab_bangkit` V1 (`fd5a1dc4`) · `tersisip_semesta` V1 (`8a648838`) ·
`bentangan_kohort` V2 (`f4eae57a`).

Sidik kode laporan kehidupan (seragam):
`24b6bb265525e81c2e571b46e401f36903383f1e3738c487850861adc3e8c595`

---

## COMMIT/REF PENTING (terbaru lebih dulu)

- jurnal 126 + ADR-A012 + PROMPT v48 (giliran ini)
- **`2888df0c`** CI 984 (run 30522785099)
- **`0deef07e`** laporan `lubang_awal` run 30522785043
- **`d304d3eb`** trio `lubang_awal` V1 (blobs py `8c36943d`, uji `86c401ee`, yml `3134bc9f`)
- `0bab4638` laporan CI 30519527929 (936)
- `eb778829` STATE v44 (tiga berkas) + PROMPT v47
- `645fd5df` jurnal 125 + ADR-A011 + praregistrasi R-305
- `3913a054` trio `sebab_bangkit` V1
- `c4bccf21` jurnal 124 + ADR-A010
- `25106dd5` trio `tersisip_semesta` V1
- `703daa90` trio `bentangan_kohort` V2

**Run id penting:** `lubang_awal` **30522785043** (kode 0) · CI **30522785099**
(984) · `sebab_bangkit` 30517682958 (kode 0) · CI 30517682951 (936) ·
`tersisip_semesta` 30514239872 (kode 0) · CI 30514239862 (879).
