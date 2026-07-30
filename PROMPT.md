# PROMPT v52 — serah terima LUX-AI

Operator: **Diva Juan Nur Taqarrub** (GitHub **EnVyxS**).
Repo tulis: **`EnVyxS/lux-ai-research`**. Tenggat proyek: **2026-08-02**.
Ditulis: 2026-07-30 (sesi 60) sesudah **`STATE.md` v48 terbit dan dibaca ulang UTUH**,
sehingga ketiga bagian STATE kini serasi **v48 / v8 / v8**.
Menggantikan PROMPT v51 (blob `dc5ef264d051b5b3a3c7c6fcb29a894981062275`).

**Apa yang berubah dari v51.** v51 ditulis ketika R-308 masih ramalan terkunci yang
belum diukur, dan ketika `STATE.md` masih v47 sementara kedua lampiran sudah v8. Kini
R-308 sudah diukur dan **SEPARUH**, lahir **KC-49**, **ADR-A015**, dan usulan **aturan
83**; usulan aturan 82 DIPERLUAS; CI 1100 → **1168**; **aturan 57 PUTUS** pada giliran
ke-27 (catatan 26/27); dan **ketimpangan versi STATE sudah LUNAS**. Semua angka di
bawah dikutip dari berkas yang dibaca UTUH pada sesi 59–60, bukan dari ingatan.

---

## LANGKAH 0 — WAJIB SEBELUM PEKERJAAN APA PUN

Jangan menulis kode, jangan mendorong berkas, jangan mengklaim angka sebelum keempat
hal ini selesai:

1. Baca **PROMPT.md** (berkas ini) UTUH dari main.
2. Baca ketiga berkas STATE UTUH — **kini serasi pada v48 / v8 / v8**:
   - `STATE.md` **v48** — blob **`2fd136e404f2085e5b188c896b5499d4f98e1ecc`**
     (commit `e7ae0e3af706d47c6c1320dd63a9cb7a2a120038`)
   - `STATE_LAMPIRAN_EKOR.md` **v8** — blob
     **`c34c88e27dce4813622c2e3ea71bf4d486ec65d6`**
   - `STATE_LAMPIRAN_UKUR.md` **v8** — blob
     **`ff19069512bd4604b18cedb896af1d6cf6ba2557`**
3. Baca **jurnal 129** (`journal/2026-07-30-129.md`, blob
   `ecb6ac241d84f06767195f931f8418fa1c853ba2`) dan **ADR-A015**
   (`decisions/ADR-A015.md`, blob `387d551051da4f0d539f7c9c26e438a9ac84c9a3`) UTUH.
4. Baca `reports/ci_terakhir.json` untuk cacah uji CI **terukur** — jangan mengarang
   cacah uji. Nilai terakhir yang diketahui: **1168**. **Blob berkas itu untuk angka
   1168 TIDAK pernah dicatat** — jangan mengarang empat puluh karakternya.

Sesudah itu, catat di jawaban pertama: papan skor, penomoran berikutnya, dan utang
aturan 52 yang masih hidup.

**Peringatan yang SUDAH GUGUR:** kepala EKOR v8 dan UKUR v8 memuat peringatan
ketimpangan versi karena keduanya sempat lebih maju daripada `STATE.md` v47. Dengan
terbitnya `STATE.md` v48, ketiganya serasi. Peringatan itu tetap tertulis sebagai
jejak; **jangan memperlakukannya sebagai utang yang masih hidup.**

---

## 1. Aturan yang paling sering dilanggar (baca ini dua kali)

- **Aturan 29 — adjudikasi jujur.** Pita praregistrasi TIDAK BOLEH diubah sesudah
  pengukuran. **Dua giliran berturut godaannya nyata:** R-307 butir 1 kalah tipis
  (0.017704 lawan ambang bawah 0.02) dan R-308 butir 2 kalah (**2** lawan pita
  **10..300**). Godaan mengubah 10..300 menjadi 1..300 direkam di ADR-A015 kep. 4
  lalu DITOLAK. Kalah ya kalah.
- **KC-49 + usulan aturan 83 (BARU) — hitung aritmetika implikasi SEBELUM mengunci
  pita.** Dua kekalahan berturut lahir dari melewatkan langkah ini: R-307 butir 1
  (7,153% baris ÷ nisbah rata 4,3 ≈ 1,7% byte) dan R-308 butir 2 (rata MATI 413.306
  hanya ~8% di bawah maksimum 451.875 → ekor bawah pasti tipis). Setiap praregistrasi
  berikutnya WAJIB memuat satu paragraf aritmetika implikasi di jurnal. Bila
  aritmetika itu sudah menentukan jawabannya dalam satu angka signifikan, butir itu
  **bukan ramalan berisiko** dan porosnya harus dipindah.
- **Usulan aturan 82 (DIPERLUAS) + KC-48 — ambang yang MUSTAHIL dilewati ATAU yang
  hasilnya SUDAH TERSIRAT dilarang jadi butir berisiko.** Butir 2 R-307 memakai ambang
  10.000 byte; berkas terkecil di seluruh semesta ternyata **22.440** byte.
- **Aturan 52 — baca utuh.** Sesudah `push_files`, baca ulang setiap berkas UTUH dari
  main. `push_files` pernah memotong berkas besar dalam sunyi (KC-42); batas tulis
  aman ±**25–45 KB** per berkas. Bila beberapa berkas besar harus naik, **dorong
  BERTAHAP** (satu per satu, masing-masing dibaca ulang) — itu yang dipakai untuk
  EKOR v8, UKUR v8, dan `STATE.md` v48, dan ketiganya berhasil.
- **Aturan 55 / KC-41 — jangan mengutip rumusan dari ingatan.** Rumusan pemicu
  workflow, label hipotesis, dan nomor aturan WAJIB dikutip dari berkas beserta
  blobnya pada giliran yang sama. Bila dua bagian STATE bertentangan, **berkas sumber
  menang**, bukan yang lebih baru.
- **Aturan 66 — cacah direktori dengan tangan** sebelum menamai modul baru. Pernah
  mencegah `lubang_tengah.py` tertimpa. **Cacah tangan terakhir: 45 / 49 / 40 pada ref
  `5a777664`**; angka sesudah trio `irisan_byte` (**46 / 50 / 41**) masih TURUNAN.
- **Aturan 57 — ramalkan cacah uji SEBELUM push**, lalu ukur. **PUTUS di giliran
  ke-27; catatan resmi 26/27; hitungan beruntun mulai lagi dari nol.** Sebab tepat:
  satu butir (`test_uji_butir2_kalah`) tercecer dari DAFTAR bernomor, bukan dari kode.
  Perbaikan pasca-melihat bukan ramalan. Kemenangan di sini deterministik — wajib
  disebut **MUDAH**, tidak masuk papan skor.
- **Aturan 79 — praregistrasi lebih dulu**, di `journal/**` (ada di `paths-ignore`),
  SEBELUM modul pengukurnya dibuat.
- **Aturan 80 — uji arah waktu wajib STRIKT**, kelas `serempak` dilapor tersendiri dan
  DILARANG masuk numerator.
- **Aturan 81 — bila satu bulan kalender menguasai ≥ 1/4 numerator**, klaim wajib
  dilapor bersama cacah per bulan dan ditandai kemungkinan artefak satu peristiwa.
  **Relevan untuk R-309:** tiga dari 38 baris HIDUP-kecil berbulan `2026-06`.

---

## 2. Posisi sekarang

- **Tip main saat berkas ini ditulis: `e7ae0e3af706d47c6c1320dd63a9cb7a2a120038`**
  (`STATE.md` v48), di atas `4dea4346` (UKUR v8), `ea141915` (EKOR v8), `982c2536`
  (jurnal 129 + ADR-A015), `d22364b9` (trio `irisan_byte` V1), `8489f847` (commit bot
  laporan). Push PROMPT ini menambah satu commit lagi. Bot laporan CI juga menambah
  commit — **selalu baca tip main yang sebenarnya, jangan asumsikan.**
- **Papan skor R-1..R-308 = 308** (dihitung tangan, aturan 21): TEPAT **215** /
  MELESET **57** / SEPARUH **21** / TIDAK TERADJUDIKASI **8** / MENUNGGU **7**.
  MENUNGGU: R-7, R-19, R-20, R-28, R-36, R-37, R-199. `N_percobaan` = 0.
  **ADJUDIKASI RISET TETAP TERKUNCI.**
- **CI terukur 1168** (run **30529294152**, commit `d22364b9`, kode 0,
  2026-07-30T09:05:52Z). Turunan: 1100 + **68** butir `test_irisan_byte.py` = 1168 ✅
  Riwayat: 630 → 638 → 662×3 → 694×3 → 722×8 → 769 → 814 → 832 → 879 → 936 → 984
  → 1044 → 1100 → **1168**. Push STATE/PROMPT menyalakan `ci.yml` tetapi tidak mengubah
  `tests/**`, jadi cacah seharusnya TETAP 1168 — **ukur, jangan asumsikan.**
- **Cacah direktori.** Dicacah TANGAN dan bernomor pada ref `5a777664`:
  `lux_ai/serapan/` **45**, `tests/` **49**, `.github/workflows/` **40**. Sesudah trio
  `irisan_byte` angka TURUNAN menjadi **46 / 50 / 41**, dan **turunan itu BELUM
  dicacah tangan**. Cacah langsung sebelum dikutip sebagai fakta terhitung (aturan 66,
  KC-33) — dan wajib dicacah sebelum menamai modul R-309.
- **STATE v48/v8/v8 SUDAH ADA dan ketiganya terverifikasi utuh.** Tidak ada utang
  STATE. STATE berikutnya v49.

---

## 3. Penomoran berikutnya

| hal | berikutnya |
| --- | --- |
| jurnal | **130** |
| STATE | **v49** (lampiran EKOR/UKUR → v9) |
| PROMPT | **v53** |
| ADR | **A016** |
| aturan resmi | **84** (resmi sampai **81**; **77**, **78**, **82**, **83** TETAP usulan) |
| KC resmi | **KC-50** (resmi sampai KC-49; KC-16 kosong selamanya) |
| hipotesis | **H-A020** (terbuka: H-A016; H-A019 didaftarkan, poros R-309) |
| ramalan | **R-309** (terkunci, jurnal 129 §10), lalu R-310 |
| papan skor sesudah R-309 | **309** |

**Catatan penomoran aturan:** nomor di repo ini tidak diberikan berurutan. 77 dan 78
masih usulan sementara 79–81 sudah berlaku; 82 dan 83 dicadangkan untuk usulan dan
belum berlaku. Jangan menomori dari ingatan — baca `STATE.md` v48.

---

## 4. Apa yang baru dipelajari (jangan diulang)

R-308 = **SEPARUH**. Satu butir berisiko menang, satu kalah, dan keduanya mengajarkan
hal yang berbeda (ADR-A015).

**Butir 1 MENANG dan benar-benar berisiko.** Terukur **38** dalam pita 20..600. Pita
itu lebar, tetapi dapat gagal ke DUA arah, dan **nol** adalah hasil yang sangat
mungkin bila kedua kelas benar-benar terpisah. Zona irisannya NYATA sekaligus TIPIS:
38 dari 18.087 hanya **0,21%** kelas HIDUP.

**Butir 2 KALAH karena aritmetika saya, bukan karena alam — lagi.** R-307 sudah
menyerahkan min 97.634, maks 451.875, rata 413.306 untuk kelas MATI. Rata yang duduk
hanya ~8% di bawah maksimum berarti massanya menumpuk rapat di ujung atas dan ekor
bawahnya pasti tipis; terukur **2**. Bahan hitungannya ada di tangan ketika pita
10..300 dikunci. Dua giliran berturut dengan sebab yang sama → **KC-49**, usulan
**aturan 83**.

**Kekalahan butir 2 R-308 BUKAN sejenis kekalahan butir 2 R-307.** Ambang 150.000
DAPAT dilewati dan memang dilewati dua kali, jadi butir ini benar-benar menguji alam
(beda dari KC-48, yang ambangnya mustahil). Yang salah letak pitanya, bukan
keberadaan ujinya.

**Cacat konstruksi yang diakui SEBELUM hasil keluar:** di `irisan_byte.ringkaskan`,
`total_byte` dihitung sebagai jumlah byte per kelas, sehingga `selisih_total_byte`
TURUNAN. Sembilan medan selisih = **delapan pemeriksaan bebas + satu turunan**.
Menyebut "sembilan pemeriksaan bebas" DILARANG (ADR-A015 kep. 7, calon KC-50).

**Temuan yang MELAWAN tafsir mudah — wajib ikut setiap kali H-A018 dikutip:**
di zona **22.440–97.634 byte** ada **38 baris HIDUP dan NOL baris MATI**. Itu bukan
akibat definisi: berkas MATI terkecil di seluruh semesta memang 97.634. Naik sampai
150.000, MATI hanya menyumbang 2 baris — **LENDUSDT 2020-11 = 97.634** dan
**FRONTUSDT 2024-09 = 109.120** (daftar LENGKAP). Maka: **boleh** berbunyi "bulan MATI
menyumbang 0,0177 byte semesta dan rata-rata 4,3× lebih kecil"; **DILARANG** berbunyi
"berkas kecil = mati" — di zona itu tafsirnya TERBALIK. **Besar berkas DILARANG
dipakai sebagai detektor status ke arah mana pun** (ADR-A015 kep. 5, kerabat KC-38).
Bulan MATI juga bukan bulan KOSONG — **ISI berkasnya BELUM diukur, dilarang ditebak.**

---

## 5. R-309 — PRAREGISTRASI TERKUNCI (jurnal 129 §10 dan UKUR v8, JANGAN DIUBAH)

Poros **H-A019**. Aritmetika implikasi sudah ditulis sebelum pita dikunci (menaati
usulan aturan 83): dari 38 baris yang terlihat, sekitar dua pertiga sampai seluruhnya
tampak bulan pertama atau bulan tepi; sisanya (MTLUSDT 2021-03, ENJUSDT 2020-09,
SLPUSDT 2023-10, TLMUSDT 2023-03) tampak bulan tengah. Pita disusun agar KEDUA arah
dapat kalah.

- **Butir 1 (BERISIKO).** Dari 38 baris HIDUP ber-byte < 97.634, cacah yang merupakan
  bulan **PERTAMA** simbol **ATAU** bulan **`2026-06`**. Penyebut **38**.
  Pita **22 .. 38**. Bila penyebut 0 → TIDAK TERADJUDIKASI (aturan 41).
- **Butir 2 (BERISIKO).** **Nisbah** rata byte bulan PERTAMA simbol terhadap rata byte
  bulan BUKAN-pertama, atas seluruh **19.586** baris. Pita **0.10 .. 0.60**.
- **Butir 3 (MUDAH).** Invarian penyebut/simbol/kelas nol, kedua kendali sah, kode
  keluar 0, cacah uji CI **diukur**. **Cacah invarian BEBAS wajib disebut apa adanya**
  — bila ada medan turunan, sebut turunan (pelajaran ADR-A015 kep. 7).

Invarian semesta yang tersedia: penyebut **19.586**, simbol **787**, HIDUP **18.087**,
SEPI **98**, MATI **1.401**, LAIN **0**, total byte **32.706.262.375**.

**Sumber byte sudah ada, tidak perlu pembaca baru:**
`silang_funding.baca_laporan_kehidupan(akar, total)` → **TIGA** nilai
`(status, byte_parquet, meta)`. **Jangan mengingat tanda tangan dari hafalan — baca
modulnya UTUH di giliran yang sama (KC-43).** `kehidupan.BULAN_AKHIR = "2026-06"`;
bulan pertama tiap simbol dapat dihitung dari peta status. Kendali dua lapis WAJIB
(data + detektor buatan).

**Nama modul R-309 WAJIB dicek lewat pencacahan direktori lebih dulu** (aturan 66;
pelajaran `lubang_tengah` yang bertabrakan). Hindari nama yang mengandung tafsir yang
sedang diuji. Laporan WAJIB dirancang RINGKAS (`BATAS_BARIS_LAPORAN=40` — terbukti
DUA kali berturut menyelamatkan laporan dari pemotongan).

---

## 6. Pola trio yang sudah terbukti (ikuti apa adanya)

Satu `push_files` atomik berisi tiga berkas (aturan 45):

1. `lux_ai/serapan/<modul>.py` — tetapan penggugur, `sidik_kode()` atas
   `BERKAS_DICAP` (SERTAKAN setiap modul yang ikut menentukan angka),
   `kendali_deteksi()` buatan, `uji_r<nnn>()` yang mengadjudikasi pitanya sendiri,
   `kode_keluar()` → 2 bila laporan tak berhak diklaim, `main()` menulis
   `reports/<modul>.json`. **Rancang laporan agar RINGKAS.**
2. `tests/test_<modul>.py` — butir dinamai `test_01`..`test_NN` tanpa `parametrize`,
   agar cacah dapat diverifikasi dengan mata (aturan 54, 57). **Tulis DAFTAR bernomor
   lengkap sebelum meramal** — itulah yang gagal di giliran ke-27.
3. `.github/workflows/<modul>.yml` — tiru berkas ASLI yang sudah ada, mis.
   `irisan_byte.yml` (blob `7d98a267`) atau `lubang_awal.yml` (blob `3134bc9f`), yang
   `paths`-nya berisi **SATU** entri: `- 'lux_ai/serapan/<modul>.py'`. Sertakan
   `permissions: contents: write`, job `ukur` di `ubuntu-latest`, checkout@v4 +
   setup-python@v5 (3.11), `pip install numpy pandas pyarrow pyyaml`, langkah `jalan`
   id=`jalan` dengan `set +e` → `KODE=$?` → `echo "kode=$KODE" >> "$GITHUB_OUTPUT"` →
   `exit 0`, langkah catat status (printf JSON ke `reports/<modul>_status.json`),
   langkah dorong laporan (git config bot, add, commit `[skip ci]`, pull --rebase,
   push), langkah akhir `exit ${{ steps.jalan.outputs.kode }}`.

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
  `get_commit` (berguna memastikan POLA NAMA berkas tanpa melisting direktori besar),
  `search_code` (selalu 0 hasil — jangan bergantung padanya). **Tidak ada** alat
  Actions/workflow-run: status run hanya lewat `reports/*_status.json` dan
  `reports/ci_terakhir.json`.
- Panggilan: `connections.mcpServer_github.runTool({toolName, toolArguments})`;
  `owner`/`repo` HANYA di dalam `toolArguments`.
- `ci.yml` (blob `c79497b2`) ber-`paths-ignore` journal / decisions / hipotesis /
  reports; push ke `lux_ai/**`, `tests/**`, `STATE*`, `PROMPT*` MENYALAKAN CI.
- Tulisan ke GitHub TIDAK memakai `editDescriptionVariableName` maupun blok
  `<edit_reference>` — itu hanya untuk halaman Notion.

---

## 8. API terverifikasi (dibaca utuh, aman dipakai)

- `irisan_byte` **V1** (blob `2dbe3d5505ac8188a9e212d73db0ce8ba0b2782f`): `VERSI=1`,
  `KELUARAN="reports/irisan_byte.json"`, `BATAS_BARIS_LAPORAN=40`,
  `KELAS_HIDUP/SEPI/MATI/LAIN`, `KELAS_URUT=("HIDUP","SEPI","MATI")`,
  `AMBANG_HIDUP_KECIL=97634`, `AMBANG_MATI_KECIL=150000`,
  `R308_PITA_BUTIR_1=(20,600)`, `R308_PITA_BUTIR_2=(10,300)`,
  `PENYEBUT_HIDUP_TERCATAT=18087`, `PENYEBUT_MATI_TERCATAT=1401`, `INVARIAN` 9 kunci,
  `MEDAN_SELISIH` 9, `KENDALI_DATA` 3 baris BTCUSDT, `DETEKSI_HIDUP=(5,10,1000)`,
  `DETEKSI_MATI=(7,900)`, `DETEKSI_TOTAL=1922`. Fungsi: `nama_keluaran`, `sidik_kode`,
  `_bagian`, `kelas_status`, `sebaran_per_kelas`, `cacah_di_bawah` (STRIKT `<`),
  `daftar_kecil`, `kendali_data`, `kendali_deteksi(ambang=50)`, `selisih_invarian`,
  `dalam_pita`, `ringkaskan`, `uji_r308`, `kode_keluar`, `jalankan(akar=".",
  total=None)`, `main`. Sidik
  `0e7103ef46a37d1e442d8e7fc5b9771b1ef7cdc3956ea57d584d84f6f73ea2c6`.
  **Cacat:** `total_byte` dihitung dari jumlah byte per kelas → `selisih_total_byte`
  TURUNAN.
- `byte_semesta` **V1** (`ff68e4be`): `R307_PITA_BUTIR_1=(0.02,0.15)`,
  `R307_AMBANG_BYTE_KECIL=10000`, `R307_PITA_BUTIR_2_CACAH=(20,400)`,
  `BATAS_BARIS_LAPORAN=40`; `himpun_byte`, `sebaran_byte_per_status`,
  `kendali_deteksi(ambang=50)`, `uji_r307`, `jalankan`. Sidik `e02aca2b…`.
- `silang_funding` **V2** (`42c3aa9d`, 29.873 B): `baca_laporan_kehidupan(akar,total)`
  → **tiga** nilai `(status, byte_parquet, meta)`; `lubang_funding(funding)` →
  `(Set[(simbol,bulan)], meta)`; `bentuk_lubang_lokal`, `kendali_silang`,
  `kendali_sah`, `baca_medan_baris(akar,total,medan="cacah_lilin")`,
  `SUMBER_FUNDING="reports/funding_semesta.json"`, `KENDALI_CACAH=3`,
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
funding, 559 berfunding); **98** SEPI; **18.087** HIDUP; `cacah_lain` **0**;
`cacah_simbol_tanpa_hidup` 18; lubang funding **880** semesta / **877** dalam penyebut
/ 3 tak dikenal; 33 HIDUP tanpa funding; `cacah_simbol_ada_lubang` **122**
(lubang_awal **5**, bukan_awal **118**, BNXUSDT keduanya). Lima bentuk AWAL: BNXUSDT,
ICPUSDT, JUPUSDT, QTUMUSDT, TLMUSDT.

**BYTE PARQUET SEMESTA** (diukur di R-307, dikuatkan IDENTIK oleh R-308 dari modul
berbeda — aturan 36): total **32.706.262.375** byte (≈32,7 GB); `byte_mati`
**579.041.399**; `bagian_byte_mati` **0.017704297493883234**; `byte_lain` **0**;
`cacah_byte_nol` **0**.

Sebaran per status (cacah / total byte / min / maks / rata):
- **HIDUP** 18.087 / 32.049.492.952 / **22.440** / 2.770.666 / 1.771.962,899
- **SEPI** 98 / 77.728.024 / 259.327 / 1.231.408 / 793.143,102
- **MATI** 1.401 / 579.041.399 / **97.634** / **451.875** / **413.305,781**

**LEBAR ZONA IRISAN BYTE (R-308, pengukuran PERTAMA):**
`cacah_hidup_byte_kecil` (< 97.634) = **38**, bagian **0.0021009564880853653** ·
`cacah_mati_byte_kecil` (< 150.000) = **2**, bagian **0.0014275517487508922**.
Daftar 2 MATI-kecil LENGKAP: LENDUSDT 2020-11 97.634 · FRONTUSDT 2024-09 109.120.
Daftar 38 HIDUP-kecil LENGKAP ada di UKUR v8 — **jangan tulis ulang dari ingatan.**

R-306: penyebut 118 = `mati_dulu` **40** + `serempak` **78** + `lubang_dulu` **0**;
bagian 0.339; tebing **39** (0.3305); satu-satunya bukan-tebing **BTCSTUSDT**.

Delapan simbol bangkit: CVCUSDT 29, CVXUSDT 13, SLPUSDT 13, CTKUSDT 11, LITUSDT 10,
TLMUSDT 8, ICPUSDT 2, MAVIAUSDT 2 = 88.

Sidik kode: `irisan_byte` V1 `0e7103ef…`, `byte_semesta` V1 `e02aca2b…`,
`lubang_tebing` V1 `4a5c2e42…`, `lubang_awal` V1 `156499ce…`, `silang_funding` V2
`8a9b859c…`, `sebab_bangkit` V1 `bafe4359…`, `tersisip_semesta` V1 `9618fd19…`,
`bentangan_kohort` V2 `8ca6ebbe…`, laporan kehidupan seragam `24b6bb26…`,
`sidik_data_funding` `2c9fbd1b…`.

---

## 10. Utang yang masih hidup (urut prioritas)

1. **Bangun trio R-309** — praregistrasi sudah terkunci (§5), jadi pekerjaan
   berikutnya adalah mengukurnya. Cacah direktori dengan tangan dulu (aturan 66),
   tulis DAFTAR butir uji bernomor lengkap, ramalkan cacah uji sebelum push (aturan
   57, hitungan beruntun dari nol).
2. **Cacah tangan `lux_ai/serapan/`, `tests/`, `.github/workflows/`** untuk
   mengesahkan angka turunan 46 / 50 / 41.
3. Aturan 52: `tests/test_bentangan_kohort.py` V2 (63 butir, blob `9f850ecd`) belum
   dibaca byte demi byte. **Utang ini sudah ENAM versi berturut-turut — jangan
   diam-diam dihapus.**
4. Belum dibaca utuh: `decisions/ADR-A002.md`, A004, A006, A007, A008,
   `PETA_MODUL.md`, `PETA_MODUL_BERKAS.md`, `STATE_LAMPIRAN.md`,
   `STATE_LAMPIRAN_ANGKA.md`, `karantina_semesta.yml` (`de40fa4e`),
   `tests/test_pulihkan.py` (`11c43533`), `test_rilis_karantina.py` (`739c8da9`),
   `test_karantina_a006.py` (`a5a3d82f`).
5. Adjudikasi tertunda: R-7, R-19, R-20, R-28, R-36, R-37, R-199; gali R-28 dari
   STATE v23 (KC-32); salin R-236..R-247 dari jurnal 92–94; periksa R-224..R-235.
6. ADR A003 / A005 / A006 / A007 belum diputuskan; **A003 wajib memuat koreksi
   A011/A012/A013/A014/A015**.
7. Blob `reports/ci_terakhir.json` untuk CI 1168 tidak tercatat — jangan mengarang.
8. Pertanyaan terbuka: **apa ISI berkas bulan MATI** (97.634..451.875 byte tetapi
   ringan — lilin berulang? volume nol? BELUM diukur, DILARANG ditebak; naik
   prioritas, sudah dua giliran tak terjawab); mengapa 39 simbol berhenti berfunding
   tepat `2025-07` dan mengapa BTCSTUSDT satu-satunya yang lepas; irisan **880 lawan
   877**; selisih **40−38** `diagnosa_kc15`; tanggal hari hilang BNXUSDT
   2022-04/06/08; bentangan 38 kohort puncak; `mati_tersisip` atas 19.586; H-A016
   (celah kelipatan 15 menit); `ukur_baris` V6 (KC-26); **taksonomi lubang tiga
   kelas** (ADR-A013).

---

## 11. Nada kerja

Ukur, jangan mengarang. Bila angka belum diukur, katakan belum diukur. Bedakan angka
TERUKUR dari angka TURUNAN dan katakan mana yang mana. Bila ramalan meleset, tulis
MELESET dan cari sebabnya — dan bedakan kekalahan yang mengajarkan sesuatu dari
kekalahan yang kosong. Kemenangan yang tidak mengajarkan apa pun wajib dinyatakan
lemah walau menang. Bila temuan melawan tafsir yang kamu sukai, tulis temuan itu lebih
keras, bukan lebih pelan. Bila dokumen sendiri bertentangan dengan berkas sumber,
berkas sumber menang dan dokumen dikoreksi pada giliran itu juga. Tutup setiap giliran
dengan jurnal, dan tinggalkan PROMPT + STATE yang bisa dipakai orang lain tanpa
bertanya apa pun.
