# PROMPT v51 — serah terima LUX-AI

Operator: **Diva Juan Nur Taqarrub** (GitHub **EnVyxS**).
Repo tulis: **`EnVyxS/lux-ai-research`**. Tenggat proyek: **2026-08-02**.
Ditulis: 2026-07-30 sesudah STATE v47/v7/v7 terbit dan **ketiganya diverifikasi utuh**.
Menggantikan PROMPT v50 (blob `08fd3f7609d6fc86d4a7793c35a9dce26a01eab6`).

**Apa yang berubah dari v50.** v50 ditulis ketika R-307 masih ramalan terkunci yang
belum diukur. Kini R-307 sudah diukur dan **MELESET**, ketiga berkas STATE sudah naik
ke v47/v7/v7, CI 1044 → **1100**, lahir **KC-48**, **ADR-A014**, dan usulan **aturan
82**. Semua angka di bawah dikutip dari berkas yang dibaca utuh pada sesi 59, bukan
dari ingatan.

---

## LANGKAH 0 — WAJIB SEBELUM PEKERJAAN APA PUN

Jangan menulis kode, jangan mendorong berkas, jangan mengklaim angka sebelum
keempat hal ini selesai:

1. Baca **PROMPT.md** (berkas ini) UTUH dari main.
2. Baca ketiga berkas STATE UTUH — **kini serasi pada v47 / v7 / v7**:
   - `STATE.md` **v47** — blob **`7642b75d0ba7cd8612d83c3a43bff1274d8cac57`**
   - `STATE_LAMPIRAN_EKOR.md` **v7** — blob **`9e906dfbb630c510d412a0a676ad2125b37b88b4`**
   - `STATE_LAMPIRAN_UKUR.md` **v7** — blob **`4e7fb65b`** (baca dari tip main)
3. Baca **jurnal 128** (`journal/2026-07-30-128.md`, blob `13c06f61`) dan
   **ADR-A014** (`decisions/ADR-A014.md`, blob `6d77c2cd`) UTUH.
4. Baca `reports/ci_terakhir.json` untuk cacah uji CI **terukur** — jangan mengarang
   cacah uji. Nilai terakhir yang diketahui: **1100**.

Sesudah itu, catat di jawaban pertama: papan skor, penomoran berikutnya, dan utang
aturan 52 yang masih hidup.

**Peringatan yang SUDAH GUGUR:** EKOR v7 dan UKUR v7 memuat peringatan keserasian
versi karena sempat lebih maju daripada `STATE.md` v46. Dengan terbitnya `STATE.md`
v47, ketiganya serasi. Peringatan itu tetap tertulis sebagai jejak; **jangan
memperlakukannya sebagai utang yang masih hidup.**

---

## 1. Aturan yang paling sering dilanggar (baca ini dua kali)

- **Aturan 29 — adjudikasi jujur.** Pita praregistrasi TIDAK BOLEH diubah sesudah
  pengukuran. **Diuji paling keras di R-307:** butir 1 terukur **0.017704** lawan
  ambang bawah **0.02** — kalah tipis, sementara arah hipotesisnya justru DIDUKUNG
  kuat oleh data yang sama. Godaan melebarkan pita ditolak; R-307 dicatat MELESET.
  Hipotesis yang benar arahnya tidak menyelamatkan ramalan yang salah angkanya.
- **Aturan 82 (DIUSULKAN, belum berlaku) + KC-48 — ambang absolut pada besaran yang
  sebarannya belum pernah diukur DILARANG jadi butir berisiko.** Butir 2 R-307
  memakai ambang 10.000 byte; berkas terkecil di seluruh semesta ternyata **22.440**
  byte. Butir itu tidak pernah dapat menguji apa pun. Ambang wajib bersandar pada
  sebaran terukur, atau dinyatakan RELATIF terhadap sebaran yang diukur run itu juga.
- **Aturan 52 — baca utuh.** Sesudah `push_files`, baca ulang setiap berkas UTUH dari
  main. `push_files` pernah memotong berkas besar dalam sunyi (KC-42); batas tulis
  aman ±**25–45 KB** per berkas. Bila tiga berkas besar harus naik, **dorong
  BERTAHAP** (satu per satu, masing-masing dibaca ulang) — itu yang dipakai untuk
  STATE v47/v7/v7 dan berhasil.
- **Aturan 55 / KC-41 — jangan mengutip rumusan dari ingatan.** Kelas cacat paling
  sering berulang di repo ini; dua kasus sesi 59 keduanya pada dokumen kami sendiri.
  Rumusan pemicu workflow, label hipotesis, dan nomor aturan WAJIB dikutip dari
  berkas beserta blobnya pada giliran yang sama. Bila dua bagian STATE bertentangan,
  **berkas sumber menang**, bukan yang lebih baru.
- **Aturan 66 — cacah direktori dengan tangan** sebelum menamai modul baru. Pernah
  mencegah `lubang_tengah.py` tertimpa.
- **Aturan 57 — ramalkan cacah uji SEBELUM push**, lalu ukur. Kini **26/26** tepat;
  berikutnya yang ke-27. Kemenangan ini deterministik — wajib disebut **MUDAH**, tidak
  masuk papan skor.
- **Aturan 79 — praregistrasi lebih dulu**, di `journal/**` (ada di `paths-ignore`),
  SEBELUM modul pengukurnya dibuat.
- **Aturan 80 — uji arah waktu wajib STRIKT**, kelas `serempak` dilapor tersendiri dan
  DILARANG masuk numerator.
- **Aturan 81 — bila satu bulan kalender menguasai ≥ 1/4 numerator**, klaim wajib
  dilapor bersama cacah per bulan dan ditandai kemungkinan artefak satu peristiwa.

---

## 2. Posisi sekarang

- Commit terakhir yang ditulis sesi 59: **`8e3bf791a68d80d9fb7c3c34b0606cef4a2d3dda`**
  (`STATE.md` v47), di atas `b5f1cfef` (UKUR v7), `cfc42e70` (EKOR v7), `69bfdd5d`
  (jurnal 128 + ADR-A014), `d3bc2039` (trio `byte_semesta`), `d73b07b9` (PROMPT v50).
  Bot laporan CI menambah commit sesudahnya — **selalu baca tip main yang sebenarnya,
  jangan asumsikan.**
- **Papan skor R-1..R-307 = 307**: TEPAT **215** / MELESET **57** / SEPARUH **20** /
  TIDAK TERADJUDIKASI **8** / MENUNGGU **7**.
  MENUNGGU: R-7, R-19, R-20, R-28, R-36, R-37, R-199. `N_percobaan` = 0.
  **ADJUDIKASI RISET TETAP TERKUNCI.**
- **CI terukur 1100** (run **30526358010**, commit `d3bc2039`, kode 0, blob
  `0765ce7b`). Riwayat: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879
  → 936 → 984 → 1044 → **1100**. Push STATE/PROMPT menyalakan `ci.yml` tetapi tidak
  mengubah `tests/**`, jadi cacah seharusnya TETAP 1100 — **ukur, jangan asumsikan.**
- **Cacah direktori — baca dengan hati-hati.** Dicacah TANGAN pada ref `d73b07b9`:
  `tests/` **48**, `lux_ai/serapan/` **44**, `.github/workflows/` **39**. Sesudah trio
  `byte_semesta` (satu berkas per direktori) angka TURUNAN menjadi **49 / 45 / 40**,
  tetapi **turunan itu BELUM dicacah tangan**. Cacah langsung sebelum dikutip sebagai
  fakta terhitung (aturan 66, KC-33).
- **STATE v47/v7/v7 SUDAH ADA dan ketiganya terverifikasi utuh.** Tidak ada utang
  STATE. STATE berikutnya v48.

---

## 3. Penomoran berikutnya

| hal | berikutnya |
| --- | --- |
| jurnal | **129** |
| STATE | **v48** (lampiran EKOR/UKUR → v8) |
| PROMPT | **v52** |
| ADR | **A015** |
| aturan resmi | **82** (resmi sampai **81**; **77**, **78**, **82** TETAP usulan) |
| KC resmi | **KC-49** (resmi sampai KC-48; KC-16 kosong selamanya) |
| hipotesis | **H-A019** (terbuka: H-A016; H-A018 sudah diukur dan dibatasi) |
| ramalan | **R-308** (terkunci, jurnal 128 §9), lalu R-309 |
| papan skor sesudah R-308 | **308** |

**Catatan penomoran aturan:** nomor di repo ini tidak selalu diberikan berurutan.
77 dan 78 masih usulan sementara 79–81 sudah berlaku; 82 dicadangkan untuk usulan
KC-48 dan belum berlaku. Jangan menomori dari ingatan — baca `STATE.md` v47.

---

## 4. Apa yang baru dipelajari (jangan diulang)

R-307 = **MELESET**, dan yang penting: **dua butirnya kalah dengan jenis kekalahan
yang BERBEDA.** Menyamakan keduanya akan menghapus pelajarannya (ADR-A014).

**Butir 1 — kekalahan yang SAH dan mengajarkan.** Bagian byte parquet milik bulan
MATI terukur **0.017704297493883234**, pita **0.02..0.15** → kalah di ambang bawah.
Padahal arah H-A018 DIDUKUNG kuat: rata-rata byte bulan MATI **413.305,781** lawan
HIDUP **1.771.962,899** — sekitar **4,3×** lebih kecil. Aritmetika yang saya lalaikan
dan bisa dikerjakan SEBELUM run: bulan MATI hanya **7,153%** baris, dibagi 4,3 ≈
**1,7%** byte. Pita saya bahkan tidak memuat nilai yang tersirat oleh angka yang
sudah saya ketahui sendiri.

**Butir 2 — kekalahan yang KOSONG.** Cacah simbol-bulan TERUKUR ber-`byte_parquet`
< 10.000 terukur **0**, pita 20..400. Sebabnya: berkas TERKECIL di seluruh 19.586
adalah **22.440** byte, dan `cacah_byte_nol` = **0**. Ambang itu mustahil dilewati
semesta apa pun — butir itu tidak menguji alam, hanya menguji kelalaian saya.
→ **KC-48** dan usulan **aturan 82**. Nol itu tetap **TERUKUR bukan buta**:
`kendali_deteksi_sah` true (aturan 50 / KC-21 terpenuhi).

**Temuan yang MELAWAN tafsir mudah — wajib ikut setiap kali H-A018 dikutip:**
HIDUP `byte_min` **22.440** < MATI `byte_min` **97.634**. Berkas TERKECIL di seluruh
semesta justru milik bulan HIDUP, dan bulan MATI berkisar sempit (97.634..451.875).
Maka: **boleh** berbunyi "bulan MATI menyumbang 0,0177 byte semesta dan rata-rata
4,3× lebih kecil"; **DILARANG** berbunyi "berkas kecil = mati". Besar berkas dilarang
dipakai sebagai detektor status (kerabat KC-38). Bulan MATI juga bukan bulan KOSONG
(`byte_min` 97.634 > 0) — ISI berkasnya BELUM diukur, dilarang ditebak.

---

## 5. R-308 — PRAREGISTRASI TERKUNCI (jurnal 128 §9, JANGAN DIUBAH)

Poros tetap **H-A018**, tetapi menyerang **IRISAN kelas**, bukan pusat sebarannya.
Semua ambang RELATIF terhadap sebaran terukur R-307 (menaati usulan aturan 82).

- **Butir 1 (BERISIKO).** Cacah simbol-bulan berstatus **HIDUP** dengan
  `byte_parquet` **< 97.634** (yaitu di bawah `byte_min` bulan MATI). Penyebut
  **18.087**. Pita **20 .. 600**. Bila penyebut 0 → TIDAK TERADJUDIKASI (aturan 41).
- **Butir 2 (BERISIKO).** Cacah simbol-bulan berstatus **MATI** dengan
  `byte_parquet` **< 150.000**. Penyebut **1.401**. Pita **10 .. 300**.
- **Butir 3 (MUDAH).** Sembilan invarian penggugur tetap nol, kedua kendali sah,
  kode keluar 0, cacah uji CI **diukur**.

Sembilan invarian penggugur (aturan 24): penyebut **19.586**, simbol **787**, MATI
**1.401**, bangkit **8**, lubang dalam penyebut **877**, lubang semesta **880**,
ada_lubang **122**, lubang_awal **5**, lubang_bukan_awal **118**.

**Sumber byte sudah ada, tidak perlu pembaca baru:** `byte_semesta` V1 sudah
menyediakan `himpun_byte`, `sebaran_byte_per_status`, dan `kendali_deteksi`; atau
langsung `silang_funding.baca_laporan_kehidupan(akar,total)` →
`(status, byte_parquet, meta)`. Kendali dua lapis WAJIB (data + detektor buatan).

**Nama modul R-308 WAJIB dicek lewat pencacahan direktori lebih dulu** (aturan 66).
Laporan WAJIB dirancang RINGKAS (`BATAS_BARIS_LAPORAN` ≤ 60) — `lubang_tebing.json`
dulu terpotong, `byte_semesta.json` dengan batas 40 terbaca utuh.

---

## 6. Pola trio yang sudah terbukti (ikuti apa adanya)

Satu `push_files` atomik berisi tiga berkas (aturan 45):

1. `lux_ai/serapan/<modul>.py` — tetapan penggugur, `sidik_kode()` atas
   `BERKAS_DICAP` (SERTAKAN setiap modul yang ikut menentukan angka),
   `kendali_deteksi()` buatan, `uji_r<nnn>()` yang mengadjudikasi pitanya sendiri,
   `kode_keluar()` → 2 bila laporan tak berhak diklaim, `main()` menulis
   `reports/<modul>.json`. **Rancang laporan agar RINGKAS.**
2. `tests/test_<modul>.py` — butir dinamai `test_01`..`test_NN` tanpa `parametrize`,
   agar cacah dapat diverifikasi dengan mata (aturan 54, 57).
3. `.github/workflows/<modul>.yml` — tiru berkas ASLI yang sudah ada, mis.
   `byte_semesta.yml` (blob `45650ff9`) atau `lubang_awal.yml` (blob `3134bc9f`),
   yang `paths`-nya berisi **SATU** entri: `- 'lux_ai/serapan/<modul>.py'`. Sertakan
   `permissions: contents: write`, langkah jalan + tulis status + commit laporan
   `[skip ci]` + `exit ${{ steps.jalan.outputs.kode }}`.

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

- `byte_semesta` **V1** (`ff68e4be`): `VERSI=1`, `KELUARAN="reports/byte_semesta.json"`,
  `BATAS_BARIS_LAPORAN=40`, `KELAS_MATI/KELAS_TERUKUR/KELAS_LAIN` + `KELAS_UKUR`,
  `R307_PITA_BUTIR_1=(0.02,0.15)`, `R307_AMBANG_BYTE_KECIL=10000`,
  `R307_PITA_BUTIR_2_CACAH=(20,400)`; fungsi `kelas_ukur`,
  `himpun_byte(status,byte_parquet,ambang=10000)`, `daftar_terukur_byte_kecil`,
  `sebaran_byte_per_status`, `kendali_deteksi(ambang=50)`, `dalam_pita`, `uji_r307`,
  `kode_keluar`, `jalankan(akar=".",total=None)`. Sidik
  `e02aca2b3967069b500b01d27a1d2d1553f47b912ea41ddbecd9e4e6c33883c7`.
- `silang_funding` **V2** (`42c3aa9d`): `baca_laporan_kehidupan(akar,total)` →
  **tiga** nilai `(status, byte_parquet, meta)`; `lubang_funding(funding)` →
  `(Set[(simbol,bulan)], meta)`; `bentuk_lubang_lokal`, `kendali_silang`,
  `kendali_sah`, `baca_medan_baris(akar,total,medan="cacah_lilin")`,
  `SUMBER_FUNDING="reports/funding_semesta.json"`,
  `BENTUK_TERBITAN_FUNDING={"awal":48,"ekor":826,"tengah":6}`.
- `kehidupan` (`f49abb2b`): `STATUS_MATI/SEPI/HIDUP/TAK_TERUKUR`,
  `BULAN_MULAI="2025-07"`, `BULAN_AKHIR="2026-06"`, `deret_bulan`, `klasifikasi`,
  `penyebut_ganda`. `kehidupan_arsip` (`318a5cb1`): `TOTAL_PECAHAN=8`.
- `kohort_ekor` V4 (`c9b63bbe`): `TEBING="2025-07"`, `BULAN_DIHARAPKAN="2026-06"`,
  `AMBANG_SEPI=0.5`, `KENDALI_HIDUP=("BTCUSDT","ETHUSDT")`.
- `lubang_awal` V1 (`8c36943d`): `peta_status`, `bulan_urut`, `ringkas`, `himpun`,
  `kendali_deteksi`, `bangkit_lokal`, `BATAS_BARIS_LAPORAN=60`. Medan
  `mati_tidak_setelah_lubang_bukan_awal` memakai `<=` — **DILARANG untuk klaim arah**
  (aturan 80).
- `lubang_tebing` V1 (`575e777e`): `kelas_arah`, `di_tebing`, `perkaya`,
  `sebaran_arah`, `kendali_deteksi`, `uji_r306`, `BATAS_BARIS_LAPORAN=60`.

---

## 9. Angka semesta (terkunci, jangan hitung ulang dari ingatan)

Penyebut **19.586** simbol-bulan; **787** simbol; **1.401** MATI (842 kehilangan
funding, 559 berfunding); **98** SEPI; **18.087** HIDUP; `cacah_simbol_tanpa_hidup`
18; lubang funding **880** semesta / **877** dalam penyebut / 3 tak dikenal; 33 HIDUP
tanpa funding; `cacah_simbol_ada_lubang` **122** (lubang_awal **5**, bukan_awal
**118**, BNXUSDT keduanya). Lima bentuk AWAL: BNXUSDT, ICPUSDT, JUPUSDT, QTUMUSDT,
TLMUSDT.

**BYTE PARQUET SEMESTA — diukur PERTAMA kali di R-307 (`reports/byte_semesta.json`,
blob `8b7f2077`, dibaca UTUH):** total **32.706.262.375** byte (≈32,7 GB);
`byte_mati` **579.041.399**; `bagian_byte_mati` **0.017704297493883234**;
`byte_terukur` **32.127.220.976**; `byte_lain` **0**; `cacah_terukur` **18.185**;
`cacah_lain` **0**; `cacah_byte_nol` **0**; `cacah_baris` **19.586**; sembilan selisih
invarian semua **0**; `kendali_sah` true; `kendali_deteksi_sah` true; `sidik_seragam`
true.

Sebaran per status (cacah / total byte / min / maks / rata):
- **HIDUP** 18.087 / 32.049.492.952 / **22.440** / 2.770.666 / 1.771.962,899
- **SEPI** 98 / 77.728.024 / 259.327 / 1.231.408 / 793.143,102
- **MATI** 1.401 / 579.041.399 / **97.634** / **451.875** / **413.305,781**

R-306: penyebut 118 = `mati_dulu` **40** + `serempak` **78** + `lubang_dulu` **0**;
bagian 0.339; tebing **39** (0.3305); satu-satunya bukan-tebing **BTCSTUSDT**.

Delapan simbol bangkit: CVCUSDT 29, CVXUSDT 13, SLPUSDT 13, CTKUSDT 11, LITUSDT 10,
TLMUSDT 8, ICPUSDT 2, MAVIAUSDT 2 = 88.

Sidik kode: `byte_semesta` V1 `e02aca2b…`, `lubang_tebing` V1 `4a5c2e42…`,
`lubang_awal` V1 `156499ce…`, `silang_funding` V2 `8a9b859c…`, `sebab_bangkit` V1
`bafe4359…`, `tersisip_semesta` V1 `9618fd19…`, `bentangan_kohort` V2 `8ca6ebbe…`,
laporan kehidupan seragam `24b6bb26…`, `sidik_data_funding` `2c9fbd1b…`.

---

## 10. Utang yang masih hidup (urut prioritas)

1. **Bangun trio R-308** — praregistrasi sudah terkunci (§5), jadi pekerjaan
   berikutnya adalah mengukurnya. Cacah direktori dengan tangan dulu (aturan 66),
   ramalkan cacah uji sebelum push (aturan 57, berikutnya 27/27).
2. **Cacah tangan `tests/`, `lux_ai/serapan/`, `.github/workflows/`** untuk
   mengesahkan angka turunan 49 / 45 / 40.
3. Aturan 52: `tests/test_bentangan_kohort.py` V2 (63 butir, blob `9f850ecd`) belum
   dibaca byte demi byte. **Utang ini sudah lima versi berturut-turut — jangan
   diam-diam dihapus.**
4. Belum dibaca utuh: `decisions/ADR-A002.md`, A004, A006, A007, A008,
   `PETA_MODUL.md`, `PETA_MODUL_BERKAS.md`, `STATE_LAMPIRAN.md`,
   `STATE_LAMPIRAN_ANGKA.md`, `karantina_semesta.yml` (`de40fa4e`),
   `tests/test_pulihkan.py` (`11c43533`), `test_rilis_karantina.py` (`739c8da9`),
   `test_karantina_a006.py` (`a5a3d82f`).
5. Adjudikasi tertunda: R-7, R-19, R-20, R-28, R-36, R-37, R-199; gali R-28 dari
   STATE v23 (KC-32); salin R-236..R-247 dari jurnal 92–94; periksa R-224..R-235.
6. ADR A003 / A005 / A006 / A007 belum diputuskan; **A003 wajib memuat koreksi
   A011/A012/A013**.
7. Pertanyaan terbuka: **apa ISI berkas bulan MATI** (byte-nya besar, 97.634..451.875
   — belum diukur, DILARANG ditebak); berapa lebar zona irisan HIDUP-berbyte-kecil
   (butir 1 R-308); mengapa 39 simbol berhenti berfunding tepat `2025-07` dan mengapa
   BTCSTUSDT satu-satunya yang lepas; irisan **880 lawan 877**; selisih **40−38**
   `diagnosa_kc15`; tanggal hari hilang BNXUSDT 2022-04/06/08; bentangan 38 kohort
   puncak; `mati_tersisip` atas 19.586; H-A016 (celah kelipatan 15 menit);
   `ukur_baris` V6 (KC-26); **taksonomi lubang tiga kelas** (ADR-A013).

---

## 11. Nada kerja

Ukur, jangan mengarang. Bila angka belum diukur, katakan belum diukur. Bila ramalan
meleset, tulis MELESET dan cari sebabnya — dan bedakan kekalahan yang mengajarkan
sesuatu dari kekalahan yang kosong. Kemenangan yang tidak mengajarkan apa pun wajib
dinyatakan lemah walau menang. Bila dokumen sendiri bertentangan dengan berkas
sumber, berkas sumber menang dan dokumen dikoreksi pada giliran itu juga. Tutup
setiap giliran dengan jurnal, dan tinggalkan PROMPT + STATE yang bisa dipakai orang
lain tanpa bertanya apa pun.
