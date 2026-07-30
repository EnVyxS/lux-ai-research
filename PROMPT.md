# PROMPT v54 — serah terima LUX-AI

Operator: **Diva Juan Nur Taqarrub** (GitHub **EnVyxS**).
Repo tulis: **`EnVyxS/lux-ai-research`**. Tenggat proyek: **2026-08-02**.
Ditulis: 2026-07-30 (sesi 61) sesudah **R-310 diukur dan TEPAT**, dan sesudah ketiga
bagian STATE naik serta dibaca ulang UTUH — kini serasi **v50 / v10 / v10**.
Menggantikan PROMPT v53 (blob `fda318b291c0b3fc5c50a75e1821c252e1fab6bd`).

**Apa yang berubah dari v53.** v53 ditulis ketika R-310 belum disusun dan pertanyaan
"apa isi berkas bulan MATI" sudah tiga giliran tak terjawab. Pertanyaan itu kini
**TERJAWAB**: bulan MATI **penuh datanya**; yang nol adalah transaksinya. R-310
**TEPAT (3/3)**; **KC-50 DIRESMIKAN**; **aturan 84 DIRESMIKAN**; **H-A020 DIUSULKAN**;
CI 1233 → **1297**; aturan 57 **beruntun 2/2**. Dan yang paling penting: sebuah angka
yang dipakai berpuluh kali di repo ini ternyata **salah dipakai** — lihat §0.

---

## 0. KOREKSI YANG WAJIB DIBACA SEBELUM MENGUTIP ANGKA APA PUN

**839.842.134 BUKAN jumlah lilin.** Angka itu adalah **total baris parquet semesta**
dari run rilis 30404071324. Ia dipakai berulang di jurnal dan lampiran seolah setara
dengan jumlah lilin 1 menit. `keterisian_lilin` V1 menghitung LANGSUNG dari medan
`cacah_lilin` atas 19.586 baris dan memperoleh **839.325.999**.

> **Selisih 516.135. Kedua besaran itu BUKAN besaran yang sama.**

Seluruh aritmetika implikasi jurnal 131 §6 dibangun di atas penyamaan itu, jadi cacat
di bahan baku — meski R-310 tetap sah karena pitanya dikunci lebih dulu (aturan 29).
Dari sinilah **KC-50** naik menjadi resmi. Dugaan penyebab (19.598 − 19.586 = 12
simbol-bulan karantina; 516.135 / 12 = 43.011 ≈ sebulan penuh) **BELUM DIUJI dan
DILARANG dikutip sebagai penjelasan.**

Pelajaran yang dibawa ke setiap modul baru: **hitung agregat semesta lewat jalur
LANGSUNG dari baris**, jangan menyalin angka yang sudah tercatat, dan bila ada dua
angka yang seharusnya setara, **adu keduanya dan laporkan selisihnya — termasuk bila
nol**. Cacat kelas ini tidak menghasilkan galat; ia menghasilkan kesunyian.

---

## LANGKAH 0 — WAJIB SEBELUM PEKERJAAN APA PUN

Jangan menulis kode, jangan mendorong berkas, jangan mengklaim angka sebelum keempat
hal ini selesai:

1. Baca **PROMPT.md** (berkas ini) UTUH dari main.
2. Baca ketiga berkas STATE UTUH — **kini serasi pada v50 / v10 / v10**:
   - `STATE.md` **v50** — blob **`095a4b2cd8b6b5cadeb3e887ab72fa7dde4c81c3`**
     (commit `0c8ddac8484c2c8c053180c1af15937d339cd306`)
   - `STATE_LAMPIRAN_EKOR.md` **v10** — blob
     **`42fce0212c6f90581c39fc4df939616c479b6920`** (commit `7e7c3a65`)
   - `STATE_LAMPIRAN_UKUR.md` **v10** — blob
     **`162c130592c723f7bde5862546982b8d8a5295af`** (commit `8a2ca90e`)
3. Baca **jurnal 132** (`journal/2026-07-30-132.md`, blob
   `35c5400ea2a6fb6191c26bd5d7f7dbc3f630b2f0`, 15 bagian) UTUH. Jurnal 131
   (`cae9ab53641f7e0b984e6fb1a439f4720ffa5e88`) memuat praregistrasi R-310 apa adanya;
   jurnal 130 (`d4c48ae4…`) dan **ADR-A016** (`209802d7…`) tetap wajib sebagai latar.
   **Peringatan:** jurnal 132 §3 memuat salah ketik "beruntun 2/1" di judulnya — yang
   benar **2/2**, sudah dikoreksi di STATE v50.
4. Baca `reports/ci_terakhir.json` untuk cacah uji CI **terukur** — jangan mengarang.
   Nilai terakhir yang diketahui: **1297**, blob
   **`3c07c9093d5232ce3852b2ac509fd9e9875f0f33`**, run **30535202643**, commit
   `924b0d7afcf1f9e17965dff931d36489ad27f01b`, 2026-07-30T10:35:00Z, kode 0.

Sesudah itu, catat di jawaban pertama: papan skor, penomoran berikutnya, dan utang
aturan 52 serta aturan 66 yang masih hidup.

**Peringatan yang SUDAH GUGUR:** kepala EKOR v9 dan UKUR v9 memuat peringatan
ketimpangan versi; kepala EKOR v10 menyatakan UKUR masih v9. Keduanya **SELESAI** —
ketiga bagian serasi. Peringatan lama tetap tertulis sebagai jejak; **jangan
memperlakukannya sebagai utang yang hidup.**

---

## 1. Aturan yang paling sering dilanggar (baca ini dua kali)

- **Aturan 29 — adjudikasi jujur.** Pita praregistrasi TIDAK BOLEH diubah sesudah
  pengukuran. Berlaku dua arah: jangan melebarkan pita yang kalah, jangan pula
  mempersempit pita yang menang agar kemenangan terlihat lebih hebat.
- **Aturan 83 (RESMI sejak STATE v49) — hitung aritmetika implikasi SEBELUM mengunci
  pita.** **Terbukti bekerja dua kali pada R-310**: tiga calon butir dibuang karena
  jawabannya sudah tertentu. Salah satunya — cacah baris MATI berlilin penuh —
  dihitung ≈1.370–1.401 sebelum mengukur dan **terukur 1.392**. Itu akan menjadi
  kemenangan murahan; membuangnya adalah kerja aturan 83.
- **Aturan 84 (RESMI sejak STATE v50) — butir berklausa ATAU wajib melaporkan
  sumbangan BEBAS tiap klausa; bila tak bisa, klausa ATAU DILARANG dan butir dipecah.**
  Sumbernya kegagalan butir 1 R-309 (klausa `2026-06` menyumbang **NOL**). R-310
  menerapkannya secara preventif: kedua butir berisiko sengaja berklausa TUNGGAL.
- **KC-50 (RESMI sejak STATE v50) — agregat semesta lewat jalan memutar.** Lihat §0.
  Dua kasus: `total_byte` turunan di `irisan_byte`, dan 839.842.134 lawan 839.325.999.
- **Usulan aturan 82 + KC-48 — ambang yang MUSTAHIL dilewati ATAU yang hasilnya SUDAH
  TERSIRAT dilarang jadi butir berisiko.** Butir 2 R-307 memakai ambang 10.000 byte;
  berkas terkecil di semesta ternyata **22.440**.
- **Aturan 52 — baca utuh.** Sesudah `push_files`, baca ulang setiap berkas UTUH dari
  main dan CATAT blobnya. `push_files` pernah memotong berkas besar dalam sunyi
  (KC-42); batas tulis aman ±**25–45 KB**. Bila beberapa berkas besar harus naik,
  **dorong BERTAHAP satu berkas per push** — itu yang dipakai untuk STATE v50,
  EKOR v10, UKUR v10, dan seluruhnya berhasil sekali jalan.
- **Aturan 55 / KC-41 — jangan mengutip dari ingatan, dan jangan menyimpulkan dari
  MATA.** Bila dua bagian STATE bertentangan, **berkas sumber menang**. Pengecualian
  tersurat yang berlaku sekarang: untuk salah ketik yang sudah diakui, dokumen
  pengoreksi menang (STATE v50 atas jurnal 132 §3; UKUR v10 atas EKOR v10 pada satu
  karakter `≉`/`≈`). Pengecualian itu **hanya** untuk salah ketik, tidak pernah untuk
  angka terukur.
- **Aturan 66 — cacah direktori dengan tangan** sebelum menamai modul baru. **Cacah
  tangan sah terakhir: 47 / 51 / 42 pada ref `07a69d39`.** Sesudah trio
  `keterisian_lilin`, angka 48 / 52 / 43 adalah **TURUNAN dan DILARANG dikutip sebagai
  terukur**. **UTANG HIDUP — lunasi sebelum menamai modul R-311.**
- **Aturan 57 — ramalkan cacah uji SEBELUM push**, lalu ukur. **Beruntun kini 2/2**
  sesudah PUTUS di 26/27. Penangkal yang terbukti: tulis DAFTAR bernomor satu nama
  per nomor, **jangan pernah memakai rentang**. Perhatikan helper: pada
  `test_keterisian_lilin.py` dua helper sengaja berawalan garis bawah agar tidak
  dikumpulkan pytest — itulah yang mencegah ramalan meleset ke atas. Kemenangan di
  sini deterministik — wajib disebut **MUDAH**, tidak masuk papan skor.
- **Aturan 50 — nol hanya boleh dibaca bila detektornya terbukti bisa melihat bukan-nol.**
  `cacah_baris_tanpa_lilin = 0` sah dibaca hanya karena `kendali_negatif` membuktikan
  modulnya BISA mendeteksi baris tanpa lilin.
- **Aturan 79 — praregistrasi lebih dulu**, di `journal/**` (ada di `paths-ignore`),
  SEBELUM modul pengukurnya dibuat.
- **Aturan 80 — uji arah waktu wajib STRIKT**, kelas `serempak` dilapor tersendiri dan
  DILARANG masuk numerator.
- **Aturan 81 — bila satu bulan kalender menguasai ≥ 1/4 numerator**, klaim wajib
  dilapor bersama cacah per bulan dan ditandai kemungkinan artefak satu peristiwa.
  **Dipakai lagi pada R-310:** tujuh dari sembilan baris berbulan `2024-05`.

---

## 2. Posisi sekarang

- **Tip main saat berkas ini ditulis: `8a2ca90e3b3e26202a533e673149e4ed775e2e7b`**
  (UKUR v10), di atas `7e7c3a65` (EKOR v10), `0c8ddac8` (STATE v50), `e6ce61f1`
  (jurnal 132), `8976c8a7` (bot laporan R-310), `924b0d7a` (trio `keterisian_lilin`),
  `07a69d39` (jurnal 131), `ec885f7e` (PROMPT v53). Push PROMPT ini menambah satu
  commit lagi; bot laporan CI juga menambah commit — **selalu baca tip main yang
  sebenarnya, jangan asumsikan.**
- **Papan skor R-1..R-310 = 310** (dihitung tangan, aturan 21): TEPAT **217** /
  MELESET **57** / SEPARUH **21** / TIDAK TERADJUDIKASI **8** / MENUNGGU **7**.
  217 + 57 = 274; 274 + 21 = 295; 295 + 8 = 303; 303 + 7 = **310** ✅
  MENUNGGU: R-7, R-19, R-20, R-28, R-36, R-37, R-199. `N_percobaan` = 0.
  **ADJUDIKASI RISET TETAP TERKUNCI.**
- **CI terukur 1297** (run **30535202643**, commit `924b0d7a`, kode 0,
  2026-07-30T10:35:00Z, blob `3c07c909…`). Turunan: 1233 + **64** butir
  `test_keterisian_lilin.py` = 1297 ✅ Riwayat: 630 → 638 → 662×3 → 694×3 → 722×8 →
  769 → 814 → 832 → 879 → 936 → 984 → 1044 → 1100 → 1168 → 1233 → **1297**. Push
  STATE/PROMPT menyalakan `ci.yml` tetapi tidak mengubah `tests/**`, jadi cacah
  seharusnya TETAP 1297 — **ukur, jangan asumsikan.**
- **Cacah direktori.** Dicacah TANGAN dan bernomor pada ref `07a69d39`:
  `lux_ai/serapan/` **47**, `tests/` **51**, `.github/workflows/` **42**. Sesudah trio
  R-310 angka turunannya 48 / 52 / 43 — **TURUNAN**. Wajib dicacah ulang sebelum
  menamai modul R-311 (aturan 66, KC-33).
- **STATE v50 / v10 / v10 SUDAH ADA dan ketiganya terverifikasi utuh.** Tidak ada
  utang STATE. STATE berikutnya v51.

---

## 3. Penomoran berikutnya

| hal | berikutnya |
| --- | --- |
| jurnal | **133** |
| STATE | **v51** (lampiran EKOR/UKUR → v11) |
| PROMPT | **v55** |
| ADR | **A017** |
| aturan resmi | **85** (resmi: **1–81, 83, 84**; **77**, **78**, **82** TETAP usulan) |
| KC resmi | **KC-51** (resmi sampai KC-50; KC-16 kosong selamanya) |
| hipotesis | **H-A021** (terbuka: H-A016; H-A019 diterima terbatas; **H-A020 DIUSULKAN, belum diuji**) |
| ramalan | **R-311** (BELUM disusun) |
| papan skor sesudah R-311 | **311** |

**Catatan penomoran aturan:** nomor di repo ini tidak berurutan. 77 dan 78 masih
usulan sementara 79–81, 83, dan 84 sudah berlaku; 82 dicadangkan untuk usulan dan
belum berlaku. Jangan menomori dari ingatan — baca `STATE.md` v50.

---

## 4. Apa yang baru dipelajari (jangan diulang)

R-310 = **TEPAT (3/3)**. Ia menjawab pertanyaan prioritas pertama, dan tetap wajib
dibaca dengan curiga.

**TEMUAN POKOK — bulan MATI penuh datanya; yang nol adalah transaksinya.**
Dari 1.401 baris MATI, **1.392 (99,4%)** berlilin PENUH sebanyak-banyaknya bulan itu;
hanya **9** yang tidak penuh. Bulan MATI bukan bulan yang datanya berhenti; ia bulan
yang perdagangannya berhenti sementara lilinnya terus dicetak. Ini menutup ADR-A016
kep. 7 yang tiga giliran tak terjawab.

**DILARANG melanjutkan ke "harga beku" atau "lilin datar".** `medan_baris_terlihat`
berisi **14** medan — `ada_di_arsip`, `bagian_volume_nol`, `bulan`, `byte_parquet`,
`cacah_baris_cacat`, `cacah_lilin`, `cacah_lilin_terbaca`, `cacah_volume_nol`,
`galat`, `gerbang_lolos`, `jalur`, `simbol`, `status`, `transaksi_total` — dan **tak
satu pun harga**. Bentuk harga di dalam bulan MATI BELUM DIUKUR.

**Kedua kemenangan tipis ke tepi BAWAH.** Butir 1 terukur **9** pada pita 1..120;
butir 2 **0,0445** pada pita 0,02..0,25. Pita yang lebar di sisi atas membuat
kemenangan lebih murah daripada tampaknya. **DILARANG membacakan R-310 sebagai
konfirmasi kuat.**

**Numerator 9 bukan sembilan pengamatan bebas.** Tujuh dari sembilan berbulan
`2024-05` dalam jendela hanya **sembilan lilin** (39.308..39.317) — kasus baru KC-47,
aturan 81. Paling banter **tiga** pengamatan bebas. Dari sini lahir **H-A020**.
**Kalimat "tujuh simbol didelisting 28 Mei 2024" DILARANG ditulis sebagai temuan** —
tanggal itu tidak terukur; yang terukur hanya lebar jendela.

**Dua anomali lama LUNAS, dua dari dua.** LENDUSDT 2020-11 (97.634 byte) dan
FRONTUSDT 2024-09 (109.120 byte) — tepat kedua `cacah_mati_byte_kecil` R-308 — adalah
dua baris MATI dengan lilin paling sedikit (13.475 dan 14.986 dari 43.200). Berkas
MATI yang kecil itu kecil **karena lilinnya memang sedikit**. Meski begitu **larangan
ADR-A015 kep. 5 TIDAK dibalik**: menjelaskan dua kasus bukan membangun detektor.

**Taksiran diadu dengan kenyataan, termasuk yang meleset.** Defisit semesta taksir
18.612.246 → terukur **18.143.601** (−2,5%); defisit bulan pertama taksir 17.247.105 →
**17.335.439** (+0,5%); bagian bukan-pertama taksir 0,073 → **0,0445** (meleset ±64%
ke atas — dan justru itu yang menjaga butir 2 tetap berisiko).

**Dua jalur ukur bertemu pada bulan pertama.** R-309 memberi nisbah byte **0,527179**;
R-310 memberi keterisian lilin bulan pertama **≈49,7%** (defisit rata 22.027 dari
43.500-an). Bulan pertama adalah bulan **separuh**, dari dua arah pengukuran berbeda.

**SISA 712.925 LILIN BELUM DIJELASKAN.** 808.162 − 95.237 = 712.925 lilin defisit di
baris bukan-pertama yang BUKAN baris MATI tak penuh. **Pertanyaan terbuka nomor satu.**

**Yang tetap berlaku dan wajib ikut setiap kali H-A018/H-A019 dikutip:** di zona
**22.440–97.634 byte** ada **38 baris HIDUP dan NOL baris MATI**; besar berkas
DILARANG dipakai sebagai detektor status ke arah mana pun. Lawan H-A019 yang tersisa
tetap **TLMUSDT 2023-03 (80.394 byte)** — **R-310 tidak menjelaskannya**, sebab
TLMUSDT 2023-03 berstatus HIDUP sehingga mustahil muncul di daftar MATI tak penuh.

---

## 5. R-311 — BELUM DISUSUN (pekerjaan berikutnya)

Tidak ada praregistrasi terkunci saat ini. ADR-A016 menolak penyusunan percobaan pada
giliran yang sama dengan adjudikasi. Calon poros urut kekuatan:

1. **Sisa 712.925 lilin** — baris mana yang menanggung defisit bukan-pertama di luar
   kesembilan baris MATI tak penuh. Poros paling bersih karena angkanya sama sekali
   belum tersirat.
2. **Selisih 516.135** lawan dugaan 12 simbol-bulan karantina (516.135 / 12 = 43.011).
   **Peringatan aturan 83:** dugaan itu sudah menghasilkan satu angka; bila pita
   disusun di sekitar 43.011 maka butirnya hampir tidak berisiko — porosnya harus
   dipindahkan ke bentuk sebaran, bukan ke rata-rata.
3. **Lubang tengah gugus `2024-05`** untuk menegakkan atau meruntuhkan **H-A020**:
   apakah lilin yang hilang berada di posisi yang sama pada ketujuh simbol.

Syarat wajib sebelum pita R-311 dikunci:

1. **Aturan 83** — tulis satu paragraf aritmetika implikasi di jurnal 133 lebih dulu.
   Bila jawabannya sudah tertentu dalam satu angka signifikan, pindahkan poros.
2. **Aturan 84 (RESMI)** — hindari klausa ATAU; bila terpaksa, laporkan sumbangan
   BEBAS tiap cabang secara terpisah di dalam laporan modul.
3. **KC-50** — hitung agregat lewat jalur LANGSUNG; adu angka setara dan laporkan
   selisihnya termasuk bila nol.
4. **Aturan 79** — praregistrasi masuk `journal/**` sebelum modul dibuat.
5. **Aturan 66** — cacah tiga direktori dengan TANGAN sebelum menamai modul (utang
   48/52/43 masih hidup); hindari nama yang mengandung tafsir yang sedang diuji.
6. Laporan WAJIB dirancang RINGKAS (`BATAS_BARIS_LAPORAN=40` — terbukti **EMPAT** kali
   berturut menyelamatkan laporan dari pemotongan; dasar usulan aturan 78).

---

## 6. Pola trio yang sudah terbukti (ikuti apa adanya)

Satu `push_files` atomik berisi tiga berkas (aturan 45):

1. `lux_ai/serapan/<modul>.py` — tetapan penggugur, `sidik_kode()` atas
   `BERKAS_DICAP` (SERTAKAN setiap modul yang ikut menentukan angka),
   `kendali_deteksi()` buatan yang jawabannya dihitung TANGAN lebih dulu,
   **`kendali_negatif()`** bila ada medan yang mungkin bernilai nol (aturan 50),
   `uji_r<nnn>()` yang mengadjudikasi pitanya sendiri, `kode_keluar()` → 2 bila
   laporan tak berhak diklaim, `main()` menulis `reports/<modul>.json`. **Hitung
   besaran invarian lewat jalur LANGSUNG** agar medan selisih benar-benar bebas
   (KC-50; pelajaran `total_byte_langsung` dan `jumlah_lilin_langsung`).
2. `tests/test_<modul>.py` — butir dinamai `test_01`..`test_NN` tanpa `parametrize`,
   agar cacah dapat diverifikasi dengan mata (aturan 54, 57). **Tulis DAFTAR bernomor
   lengkap, satu nama per nomor, tanpa rentang, sebelum meramal.** Helper wajib
   berawalan garis bawah agar tidak ikut terkumpul.
3. `.github/workflows/<modul>.yml` — tiru berkas ASLI yang sudah ada, mis.
   `keterisian_lilin.yml` (blob `d821c63a`) atau `bulan_pertama.yml` (`2242e3e4`),
   yang `paths`-nya berisi **SATU** entri: `- 'lux_ai/serapan/<modul>.py'`. Sertakan
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
  main; mendukung `minimal_output`), `push_files`, `create_or_update_file` (butuh
  sha), `list_commits`, `get_commit`, `search_code` (**selalu 0 hasil — jangan
  dipakai**). **Tidak ada** alat Actions/workflow-run: status run hanya lewat
  `reports/*_status.json` dan `reports/ci_terakhir.json`. **`ci_terakhir.json` hanya
  menyimpan run TERAKHIR** — ramalan untuk push yang tersusul push lain tidak pernah
  terukur, dan DILARANG dicatat sebagai kemenangan.
- Panggilan: `connections.mcpServer_github.runTool({toolName, toolArguments})`;
  `owner`/`repo` HANYA di dalam `toolArguments`.
- `ci.yml` (blob `c79497b2`) ber-`paths-ignore` journal / decisions / hipotesis /
  reports; push ke `lux_ai/**`, `tests/**`, `STATE*`, `PROMPT*` MENYALAKAN CI.
- Tulisan ke GitHub TIDAK memakai `editDescriptionVariableName` maupun blok
  `<edit_reference>` — itu hanya untuk halaman Notion.

---

## 8. API terverifikasi (dibaca utuh, aman dipakai)

- `keterisian_lilin` **V1** (blob `3f80ffa72008008d567ef32f9f278b8931e91ac3`):
  `VERSI=1`, `TOTAL_PECAHAN=kehidupan_arsip.TOTAL_PECAHAN`,
  `KELUARAN="reports/keterisian_lilin.json"`,
  `KELUARAN_RINGKAS="reports/keterisian_lilin_ringkas.json"`,
  `BATAS_BARIS_LAPORAN=40`, `MENIT_PER_HARI=1440`, `MEDAN_LILIN="cacah_lilin"`,
  `KENDALI_SIMBOL="BTCUSDT"`, `KENDALI_CACAH=3`, `AMBANG_HIDUP_KECIL=97634`,
  `R310_PITA_BUTIR_1=(1,120)`, `R310_PITA_BUTIR_2=(0.02,0.25)`,
  `BERKAS_DICAP=["kehidupan.py","kehidupan_arsip.py","keterisian_lilin.py",
  "silang_funding.py"]`, `INVARIAN` **8** kunci (seluruhnya BEBAS),
  `JAWABAN_KENDALI=(3, 1, 1160, 520, 640, 213400, 0, 0.5517)`. Fungsi:
  `nama_keluaran`, `nama_ringkas`, `daftar_sumber`, `sidik_kode`, `hari_dalam_bulan`,
  `lilin_penuh`, `defisit`, `peta_bulan_pertama`, `kumpulkan`, `ringkas_defisit`,
  `baris_mati_tak_penuh`, `cacah_mati_tak_penuh`, `cacah_mati_penuh`,
  `bagian_defisit_bukan_pertama`, `potong`, `dalam_pita`, `dalam_pita_pecahan`,
  `invarian_terukur`, `selisih_invarian`, `kendali_data`, `kendali_data_sah`,
  `semesta_kendali`, `kendali_deteksi`, **`kendali_negatif`**, `uji_r310`,
  `kode_keluar`, `jalankan(akar=".", total=None)`, `berkas_ringkas`, `main`. Sidik
  `1cd98f4fa22c24b30f31f5b36dac0ea0bb3fa9de44e5e15ae73cbf11cdca08bb`.
- `bulan_pertama` **V1** (blob `b9bd00ac46a2825a8f1b540bbe9207e154f66bf4`, 19.349 B):
  `VERSI=1`, `KELUARAN="reports/bulan_pertama.json"`, `BATAS_BARIS_LAPORAN=40`,
  `AMBANG_HIDUP_KECIL=97634`, `BULAN_TEPI="2026-06"`, `R309_PITA_BUTIR_1=(22,38)`,
  `R309_PITA_BUTIR_2=(0.10,0.60)`, `INVARIAN` **8** kunci, `MEDAN_SELISIH` **8**
  (seluruhnya BEBAS), `KENDALI_DATA` 3 baris BTCUSDT, `DETEKSI_AMBANG=250`,
  `DETEKSI_PERTAMA=2`, `DETEKSI_HIDUP_KECIL=2`, `DETEKSI_SEBAGIAN=2`,
  `DETEKSI_NISBAH=0.75`, `DETEKSI_TOTAL_BYTE=1500`. Fungsi: `nama_keluaran`,
  `sidik_kode`, `_bagian`, `kelas_status`, `peta_bulan_pertama`, `penanda_baris`,
  `sebaran_per_kelas`, **`total_byte_langsung`**, `cacah_di_bawah`, `cacah_sebagian`,
  `daftar_kecil_bertanda`, `nisbah_pertama` (penyebut kosong → **None**),
  `selisih_invarian`, `dalam_pita`, `dalam_pita_pecahan`, `kendali_data`,
  `kendali_deteksi`, `ringkaskan`, `uji_r309`, `kode_keluar`, `jalankan(akar=".",
  total=None)`, `main`. Sidik `0d3530f6…`.
- `irisan_byte` **V1** (blob `2dbe3d5505ac8188a9e212d73db0ce8ba0b2782f`):
  `AMBANG_HIDUP_KECIL=97634`, `AMBANG_MATI_KECIL=150000`,
  `R308_PITA_BUTIR_1=(20,600)`, `R308_PITA_BUTIR_2=(10,300)`, `INVARIAN` 9 kunci,
  `MEDAN_SELISIH` 9, `DETEKSI_TOTAL=1922`; `cacah_di_bawah` STRIKT `<`. Sidik
  `0e7103ef…`. **Cacat (kasus pertama KC-50):** `total_byte` dijumlahkan dari byte per
  kelas → `selisih_total_byte` TURUNAN; delapan bebas + satu turunan.
- `byte_semesta` **V1** (`ff68e4be`): `R307_PITA_BUTIR_1=(0.02,0.15)`,
  `R307_AMBANG_BYTE_KECIL=10000`, `R307_PITA_BUTIR_2_CACAH=(20,400)`,
  `BATAS_BARIS_LAPORAN=40`. Sidik `e02aca2b…`.
- `silang_funding` **V2** (`42c3aa9d`, 29.873 B): `baca_laporan_kehidupan(akar,total)`
  → **TIGA** nilai `(status, byte_parquet, meta)`, kunci tuple `(simbol,bulan)`;
  **`baca_medan_baris(akar, total, medan)`** → `(nilai, meta)`, MELEWATI baris
  ber-medan `None` — dipakai `keterisian_lilin` dengan `medan="cacah_lilin"`;
  `bulan_per_simbol(status)` → `Dict[str,List[str]]` terurut;
  `lubang_funding(funding)` → `(Set[(simbol,bulan)], meta)`; `bentuk_lubang_lokal`,
  `kendali_silang`, `kendali_sah`; `PENYEBUT_TERCATAT=19586`, `MATI_TERCATAT=1401`,
  `KOHORT_TERCATAT=456`, `HIDUP_TANPA_FUNDING_TERCATAT=33`,
  `LUBANG_TAK_DIKENAL_TERCATAT=3`,
  `BENTUK_TERBITAN_FUNDING={"awal":48,"ekor":826,"tengah":6}`.
  **Jangan mengingat tanda tangan dari hafalan — baca modulnya UTUH di giliran yang
  sama (KC-43).**
- `kehidupan` (`f49abb2b`): `AMBANG_SEPI=0.5`, `STATUS_MATI/SEPI/HIDUP/TAK_TERUKUR`,
  `BULAN_MULAI="2025-07"`, `BULAN_AKHIR="2026-06"`, `deret_bulan`, `klasifikasi`,
  `penyebut_ganda`. `kehidupan_arsip` (`318a5cb1`): `TOTAL_PECAHAN=8`,
  `AKAR_UNDUH="data/unduh"`, `AKAR_BONGKAR="data/kehidupan_arsip"`,
  `KOLOM_VOLUME="volume"`, `KOLOM_TRANSAKSI="trades"`.
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

**Pembelahan bulan pertama (R-309):** **787** baris bulan pertama (tepat satu per
simbol) + **18.799** bukan-pertama = 19.586 ✅
**Pembelahan kelas MATI (R-310):** **1.392** berlilin penuh + **9** tak penuh =
1.401 ✅

**LILIN (R-310, diukur LANGSUNG):** `jumlah_lilin_langsung` **839.325.999** — lawan
total baris parquet **839.842.134**, **selisih 516.135** (lihat §0; keduanya BUKAN
besaran yang sama). `defisit_total` **18.143.601**; `defisit_pertama` **17.335.439**
(95,5%); `defisit_bukan_pertama` **808.162**; `bagian_defisit_bukan_pertama`
**0,0445**; `cacah_baris_tanpa_lilin` **0**; `cacah_defisit_negatif` **0**;
`cacah_kunci_ganda` **0**; `cacah_laporan_dibaca` **8**; `sidik_seragam` true.
Kendali BTCUSDT 2021-05 / 2021-08 / 2021-01 semuanya `cacah_lilin` **44.640**, HIDUP.

**Kesembilan baris MATI tak penuh (LENGKAP, semuanya `pertama:false`):** LENDUSDT
2020-11 13.475/43.200 · FRONTUSDT 2024-09 14.986/43.200 · FOOTBALLUSDT 2024-05
39.308/44.640 · ANTUSDT 2024-05 39.309 · BTSUSDT 2024-05 39.310 · SRMUSDT 2024-05
39.311 · HNTUSDT 2024-05 39.312 · TOMOUSDT 2024-05 39.315 · COCOSUSDT 2024-05 39.317.
Jumlah defisitnya **95.237** (0,1178 dari 808.162) → **sisa 712.925 belum dijelaskan**.

**BYTE PARQUET SEMESTA** (R-307, dikuatkan IDENTIK oleh R-308, R-309, R-310 dari modul
berbeda — aturan 36, kini EMPAT kali): total **32.706.262.375** byte (≈32,7 GB);
`byte_mati` **579.041.399**; `bagian_byte_mati` **0.017704297493883234**; `byte_lain`
**0**; `cacah_byte_nol` **0**.

Sebaran per status (cacah / total byte / min / maks / rata):
- **HIDUP** 18.087 / 32.049.492.952 / **22.440** / 2.770.666 / 1.771.962,899
- **SEPI** 98 / 77.728.024 / 259.327 / 1.231.408 / 793.143,102
- **MATI** 1.401 / 579.041.399 / **97.634** / **451.875** / **413.305,781**

**LEBAR ZONA IRISAN BYTE (R-308):** `cacah_hidup_byte_kecil` (< 97.634) = **38**,
bagian **0.0021009564880853653** · `cacah_mati_byte_kecil` (< 150.000) = **2**, bagian
**0.0014275517487508922**. Daftar 2 MATI-kecil LENGKAP: LENDUSDT 2020-11 97.634 ·
FRONTUSDT 2024-09 109.120 — **keduanya kini terjelaskan oleh R-310.**

**IRISAN BULAN PERTAMA (R-309):** `cacah_hidup_kecil_sebagian` **37** dari 38, bagian
**0,973684**; `jumlah_byte_pertama` **706.233.745**; `jumlah_byte_bukan_pertama`
**32.000.028.630**; `rata_byte_pertama` **897.374,517**; `rata_byte_bukan_pertama`
**1.702.219,726**; `nisbah_rata` **0,527179**. Satu-satunya baris kecil yang bukan
bulan pertama: **TLMUSDT 2023-03 (80.394)**. Daftar 38 HIDUP-kecil bertanda LENGKAP
ada di UKUR v10 — **jangan tulis ulang dari ingatan.**

R-306: penyebut 118 = `mati_dulu` **40** + `serempak` **78** + `lubang_dulu` **0**;
bagian 0.339; tebing **39** (0.3305); satu-satunya bukan-tebing **BTCSTUSDT**.

Delapan simbol bangkit: CVCUSDT 29, CVXUSDT 13, SLPUSDT 13, CTKUSDT 11, LITUSDT 10,
TLMUSDT 8, ICPUSDT 2, MAVIAUSDT 2 = 88.

Sidik kode: `keterisian_lilin` V1 `1cd98f4f…`, `bulan_pertama` V1 `0d3530f6…`,
`irisan_byte` V1 `0e7103ef…`, `byte_semesta` V1 `e02aca2b…`, `lubang_tebing` V1
`4a5c2e42…`, `lubang_awal` V1 `156499ce…`, `silang_funding` V2 `8a9b859c…`,
`sebab_bangkit` V1 `bafe4359…`, `tersisip_semesta` V1 `9618fd19…`, `bentangan_kohort`
V2 `8ca6ebbe…`, laporan kehidupan seragam `24b6bb26…`, `sidik_data_funding`
`2c9fbd1b…`.

---

## 10. Utang yang masih hidup (urut prioritas)

1. **Cacah tangan tiga direktori** pada ref pasca-R-310 — angka 47 / 51 / 42 hanya sah
   untuk ref `07a69d39`; 48 / 52 / 43 adalah TURUNAN dan DILARANG dikutip sebagai
   terukur (aturan 66, KC-33). **Lunasi sebelum menamai modul R-311.**
2. **Susun praregistrasi R-311** di jurnal 133 (aturan 79), dengan aritmetika
   implikasi lebih dulu (aturan 83), tanpa klausa ATAU yang tak terukur terpisah
   (aturan 84), dan agregat lewat jalur LANGSUNG (KC-50). Calon poros di §5.
3. **ADR A017** — formalisasi keputusan jurnal 132 §13: KC-50, aturan 84, koreksi
   516.135, H-A020, larangan menulis "delisting 28 Mei 2024".
4. Aturan 52: `tests/test_bentangan_kohort.py` V2 (63 butir, blob `9f850ecd`) belum
   dibaca byte demi byte. **Utang ini sudah DELAPAN versi berturut-turut — jangan
   diam-diam dihapus.**
5. Belum dibaca utuh: `decisions/ADR-A002.md`, A004, A006, A007, A008,
   `PETA_MODUL.md`, `PETA_MODUL_BERKAS.md`, `STATE_LAMPIRAN.md`,
   `STATE_LAMPIRAN_ANGKA.md`, `karantina_semesta.yml` (`de40fa4e`),
   `tests/test_pulihkan.py` (`11c43533`), `test_rilis_karantina.py` (`739c8da9`),
   `test_karantina_a006.py` (`a5a3d82f`).
6. Adjudikasi tertunda: R-7, R-19, R-20, R-28, R-36, R-37, R-199; gali R-28 dari
   STATE v23 (KC-32); salin R-236..R-247 dari jurnal 92–94; periksa R-224..R-235.
7. ADR A003 / A005 / A006 / A007 belum diputuskan; **A003 wajib memuat koreksi
   A011/A012/A013/A014/A015/A016**.
8. **Ramalan yang belum/tidak terukur — jangan dicatat sebagai kemenangan.**
   `ci_terakhir.json` hanya menyimpan run TERAKHIR. Ramalan "CI tetap 1233" untuk push
   STATE v49 (`8dd0e4a5`), EKOR v9 (`a3830617`), PROMPT v53 (`ec885f7e`) tidak pernah
   terukur; **push STATE v50 (`0c8ddac8`) bahkan tidak didahului ramalan sama sekali**.
   Ramalan "CI tetap 1297" untuk EKOR v10, UKUR v10, dan PROMPT ini menunggu
   pengukuran. Bukan tepat, bukan meleset.
9. Pertanyaan terbuka urut prioritas: **sisa 712.925 lilin**; **selisih 516.135**;
   **gugus 2024-05 / H-A020**; **TLMUSDT 2023-03**; apakah "bulan pertama di penyebut"
   = "bulan pertama di bursa"; bentuk **harga** di dalam bulan MATI (belum terlihat
   sama sekali); mengapa 39 simbol berhenti berfunding tepat `2025-07` dan mengapa
   BTCSTUSDT satu-satunya yang lepas; irisan **880 lawan 877**; selisih **40−38**
   `diagnosa_kc15`; tanggal hari hilang BNXUSDT 2022-04/06/08; bentangan 38 kohort
   puncak; `mati_tersisip` atas 19.586; H-A016; `ukur_baris` V6 (KC-26); **taksonomi
   lubang tiga kelas** (ADR-A013).

---

## 11. Nada kerja

Ukur, jangan mengarang. Bila angka belum diukur, katakan belum diukur. Bedakan angka
TERUKUR dari angka TURUNAN dan katakan mana yang mana — dan bedakan pula MELIHAT dari
MENGUKUR. Bila dua angka yang kamu kira sama ternyata berbeda, **angka itu temuannya**,
bukan gangguannya: 516.135 lebih berharga daripada kemenangan R-310 itu sendiri. Bila
ramalan meleset, tulis MELESET dan cari sebabnya. Bila ramalan MENANG, cari bagian
mana dari kemenangan itu yang sebenarnya kosong — R-309 dan R-310 sama-sama menang
3/3 dan sama-sama melahirkan aturan baru dari cacatnya sendiri. Kemenangan yang tidak
mengajarkan apa pun wajib dinyatakan lemah walau menang; kemenangan tipis ke tepi
pita wajib disebut tipis. Bila temuan melawan tafsir yang kamu sukai, tulis temuan itu
lebih keras, bukan lebih pelan. Bila dokumen sendiri bertentangan dengan berkas
sumber, berkas sumber menang dan dokumen dikoreksi pada giliran itu juga. Tutup setiap
giliran dengan jurnal, dan tinggalkan PROMPT + STATE yang bisa dipakai orang lain
tanpa bertanya apa pun.
