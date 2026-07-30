# PROMPT v53 — serah terima LUX-AI

Operator: **Diva Juan Nur Taqarrub** (GitHub **EnVyxS**).
Repo tulis: **`EnVyxS/lux-ai-research`**. Tenggat proyek: **2026-08-02**.
Ditulis: 2026-07-30 (sesi 61) sesudah **R-309 diukur dan TEPAT**, dan sesudah ketiga
bagian STATE naik serta dibaca ulang UTUH — kini serasi **v49 / v9 / v9**.
Menggantikan PROMPT v52 (blob `16eafb156fb2391fe1f0be6c92b5df0609f099d5`).

**Apa yang berubah dari v52.** v52 ditulis ketika R-309 masih ramalan terkunci yang
belum diukur. Kini R-309 sudah diukur dan **TEPAT (3/3)** — kemenangan bulat pertama
sejak R-306. Lahir **ADR-A016**; **aturan 83 DIRESMIKAN**; **usulan aturan 84**
diajukan; **H-A019 DIUJI dan DITERIMA TERBATAS**; tiga dari empat dugaan jurnal 129
terbukti **SALAH** dan dicabut; CI 1168 → **1233**; **aturan 57 kembali berjalan
(1/1)**; cacah tangan direktori LUNAS pada **47 / 51 / 42**; blob
`reports/ci_terakhir.json` akhirnya TERCATAT untuk kedua angka. Semua angka di bawah
dikutip dari berkas yang dibaca UTUH pada sesi 60–61, bukan dari ingatan.

---

## LANGKAH 0 — WAJIB SEBELUM PEKERJAAN APA PUN

Jangan menulis kode, jangan mendorong berkas, jangan mengklaim angka sebelum keempat
hal ini selesai:

1. Baca **PROMPT.md** (berkas ini) UTUH dari main.
2. Baca ketiga berkas STATE UTUH — **kini serasi pada v49 / v9 / v9**:
   - `STATE.md` **v49** — blob **`64dc7b3fed15b447f297874e8410c9a6c4b7dd4e`**
     (commit `8dd0e4a5a045ea01de39a3163ce052b051336cac`)
   - `STATE_LAMPIRAN_EKOR.md` **v9** — blob
     **`beaed54cb93e00c2c56f1aaa8d1c2709c97f08d0`** (commit `a3830617`)
   - `STATE_LAMPIRAN_UKUR.md` **v9** — blob
     **`0b795fb48ababa61b318518ce1196ad90467e077`** (commit `f8098980`)
3. Baca **jurnal 130** (`journal/2026-07-30-130.md`, blob
   `d4c48ae45a6fbeffdf473824f3fa69f6506ed909`) dan **ADR-A016**
   (`decisions/ADR-A016.md`, blob `209802d7b5eeff9a0d66f13d552b83145acb9dd6`) UTUH.
   Jurnal 129 (`ecb6ac24…`) dan ADR-A015 (`387d5510…`) tetap berguna sebagai latar,
   **tetapi § dugaan "bulan tengah" di jurnal 129 SUDAH DICABUT** — lihat §4.
4. Baca `reports/ci_terakhir.json` untuk cacah uji CI **terukur** — jangan mengarang.
   Nilai terakhir yang diketahui: **1233**, blob
   **`0489d71101e451efe73d20fd8fe75ba6d41c5c27`**, run **30532058688**, commit
   `09ce9853`, 2026-07-30T09:47:29Z, kode 0.

Sesudah itu, catat di jawaban pertama: papan skor, penomoran berikutnya, dan utang
aturan 52 yang masih hidup.

**Peringatan yang SUDAH GUGUR:** kepala EKOR v8 dan UKUR v8 memuat peringatan
ketimpangan versi. Ketimpangan itu **SELESAI** — ketiga bagian serasi. Peringatan lama
tetap tertulis sebagai jejak; **jangan memperlakukannya sebagai utang yang hidup.**

---

## 1. Aturan yang paling sering dilanggar (baca ini dua kali)

- **Aturan 29 — adjudikasi jujur.** Pita praregistrasi TIDAK BOLEH diubah sesudah
  pengukuran. R-309 menang tanpa satu pun pita disentuh. Ini berlaku dua arah:
  jangan melebarkan pita yang kalah, jangan pula mempersempit pita yang menang agar
  kemenangan terlihat lebih hebat.
- **Aturan 83 (RESMI sejak STATE v49) — hitung aritmetika implikasi SEBELUM mengunci
  pita.** Lahir dari dua kekalahan berturut (R-307 butir 1, R-308 butir 2, KC-49) dan
  **terbukti bekerja pada R-309**. Setiap praregistrasi WAJIB memuat satu paragraf
  aritmetika implikasi di jurnal. Bila aritmetika itu sudah menentukan jawabannya
  dalam satu angka signifikan, butir itu **bukan ramalan berisiko** — pindahkan
  porosnya.
- **Usulan aturan 84 (BARU, ADR-A016 kep. 3) — butir berklausa ATAU wajib melaporkan
  sumbangan BEBAS tiap klausa, atau dipecah jadi butir terpisah.** Sumbernya butir 1
  R-309: klausa "bulan tepi `2026-06`" menyumbang **NOL** karena ketiga baris tepi
  juga bulan pertama. Kemenangan itu milik satu klausa saja. Kerabat KC-47.
- **Usulan aturan 82 + KC-48 — ambang yang MUSTAHIL dilewati ATAU yang hasilnya SUDAH
  TERSIRAT dilarang jadi butir berisiko.** Butir 2 R-307 memakai ambang 10.000 byte;
  berkas terkecil di semesta ternyata **22.440**.
- **Aturan 52 — baca utuh.** Sesudah `push_files`, baca ulang setiap berkas UTUH dari
  main dan CATAT blobnya. `push_files` pernah memotong berkas besar dalam sunyi
  (KC-42); batas tulis aman ±**25–45 KB**. Bila beberapa berkas besar harus naik,
  **dorong BERTAHAP** — itu yang dipakai untuk STATE v48, v49, EKOR v9, UKUR v9, dan
  seluruhnya berhasil.
- **Aturan 55 / KC-41 — jangan mengutip dari ingatan, dan jangan menyimpulkan dari
  MATA.** Bila dua bagian STATE bertentangan, **berkas sumber menang**. Pelajaran
  terbaru paling mahal: pada jurnal 129 saya melihat daftar 38 baris lalu menulis
  empat simbol "tampak bulan tengah"; **tiga di antaranya SALAH**. Melihat bukan
  mengukur.
- **Aturan 66 — cacah direktori dengan tangan** sebelum menamai modul baru. **Cacah
  tangan terakhir: 47 / 51 / 42 pada ref `010edff2`** (sesudah trio `bulan_pertama`).
  Angka sesudah trio BERIKUTNYA otomatis kembali menjadi TURUNAN sampai dicacah lagi.
- **Aturan 57 — ramalkan cacah uji SEBELUM push**, lalu ukur. **Beruntun kini 1/1**
  sesudah PUTUS di 26/27. Penangkal yang terbukti: tulis DAFTAR bernomor satu nama
  per nomor, **jangan pernah memakai rentang** seperti "56–62" — justru rentang itu
  yang menyembunyikan butir hilang pada giliran ke-27. Kemenangan di sini
  deterministik — wajib disebut **MUDAH**, tidak masuk papan skor.
- **Aturan 79 — praregistrasi lebih dulu**, di `journal/**` (ada di `paths-ignore`),
  SEBELUM modul pengukurnya dibuat.
- **Aturan 80 — uji arah waktu wajib STRIKT**, kelas `serempak` dilapor tersendiri dan
  DILARANG masuk numerator.
- **Aturan 81 — bila satu bulan kalender menguasai ≥ 1/4 numerator**, klaim wajib
  dilapor bersama cacah per bulan dan ditandai kemungkinan artefak satu peristiwa.

---

## 2. Posisi sekarang

- **Tip main saat berkas ini ditulis: `f80989805b60d05e4baafaecbb11070e833cb3b7`**
  (UKUR v9), di atas `a3830617` (EKOR v9), `8dd0e4a5` (STATE v49), `8fad9091`
  (ADR-A016), `010edff2` (jurnal 130), `09ce9853` (trio `bulan_pertama` V1),
  `5c8d220a` (PROMPT v52), `e7ae0e3a` (STATE v48). Push PROMPT ini menambah satu
  commit lagi; bot laporan CI juga menambah commit — **selalu baca tip main yang
  sebenarnya, jangan asumsikan.**
- **Papan skor R-1..R-309 = 309** (dihitung tangan, aturan 21): TEPAT **216** /
  MELESET **57** / SEPARUH **21** / TIDAK TERADJUDIKASI **8** / MENUNGGU **7**.
  MENUNGGU: R-7, R-19, R-20, R-28, R-36, R-37, R-199. `N_percobaan` = 0.
  **ADJUDIKASI RISET TETAP TERKUNCI.**
- **CI terukur 1233** (run **30532058688**, commit `09ce9853`, kode 0,
  2026-07-30T09:47:29Z, blob `0489d711…`). Turunan: 1168 + **65** butir
  `test_bulan_pertama.py` = 1233 ✅ Riwayat: 630 → 638 → 662×3 → 694×3 → 722×8 → 769
  → 814 → 832 → 879 → 936 → 984 → 1044 → 1100 → 1168 → **1233**. Push STATE/PROMPT
  menyalakan `ci.yml` tetapi tidak mengubah `tests/**`, jadi cacah seharusnya TETAP
  1233 — **ukur, jangan asumsikan.**
- **Cacah direktori.** Dicacah TANGAN dan bernomor pada ref `010edff2`:
  `lux_ai/serapan/` **47**, `tests/` **51**, `.github/workflows/` **42**. Wajib
  dicacah ulang sebelum menamai modul R-310 (aturan 66, KC-33).
- **STATE v49 / v9 / v9 SUDAH ADA dan ketiganya terverifikasi utuh.** Tidak ada utang
  STATE. STATE berikutnya v50.

---

## 3. Penomoran berikutnya

| hal | berikutnya |
| --- | --- |
| jurnal | **131** |
| STATE | **v50** (lampiran EKOR/UKUR → v10) |
| PROMPT | **v54** |
| ADR | **A017** |
| aturan resmi | **85** (resmi: **1–81 dan 83**; **77**, **78**, **82**, **84** TETAP usulan) |
| KC resmi | **KC-50** (resmi sampai KC-49; KC-16 kosong selamanya) |
| hipotesis | **H-A020** (terbuka: H-A016; H-A019 DIUJI, diterima terbatas) |
| ramalan | **R-310** (BELUM disusun) |
| papan skor sesudah R-310 | **310** |

**Catatan penomoran aturan:** nomor di repo ini tidak berurutan. 77 dan 78 masih
usulan sementara 79–81 dan 83 sudah berlaku; 82 dan 84 dicadangkan untuk usulan dan
belum berlaku. Jangan menomori dari ingatan — baca `STATE.md` v49.

---

## 4. Apa yang baru dipelajari (jangan diulang)

R-309 = **TEPAT (3/3)**. Justru karena bulat, ia wajib dibaca paling hati-hati.

**Butir 1 menang besar — tetapi separuh ramalannya kosong.** Terukur **37 dari 38**
(bagian 0,973684) dalam pita 22..38. Ramalannya berbunyi "bulan PERTAMA simbol ATAU
bulan tepi `2026-06`"; ternyata ketiga baris tepi (SQQQUSDT, TQQQUSDT, MVLLUSDT)
**juga** bulan pertama simbolnya, sehingga menghapus klausa tepi tetap menghasilkan
37. Klausa itu **DICABUT** (ADR-A016 kep. 2) dan lahirlah usulan **aturan 84**.

**Butir 2 menang tipis ke tepi atas.** Nisbah rata byte bulan pertama terhadap
bukan-pertama = **0,527179** lawan tepi atas **0,60**. Kemenangan tipis DILARANG
dibacakan sebagai konfirmasi kuat. Yang penting justru besarnya: berkas bulan pertama
rata-rata **setengah** ukuran bulan biasa — bukan sepersepuluh, bukan nyaris kosong.

**Tiga dari empat dugaan jurnal 129 SALAH dan sudah DICABUT.** MTLUSDT 2021-03,
ENJUSDT 2020-09, dan SLPUSDT 2023-10 saya sebut "tampak bulan tengah"; terukur,
ketiganya justru bulan **PERTAMA**. Satu-satunya yang benar-benar melawan H-A019:
**TLMUSDT 2023-03 (80.394 byte)** — bukan pertama, bukan tepi, tetap kecil. Belum
dijelaskan; **DILARANG dibuang sebagai pencilan** (ADR-A016 menolak jalan itu).

**Asimetri yang wajib disebut lebih keras daripada kemenangannya.** 37 dari 38 berkas
kecil adalah bulan pertama (97,4%), tetapi hanya **37 dari 787** bulan pertama yang
berkas kecil (**±4,7%**). H-A019 menjelaskan ekor bawah; ia TIDAK meramalkan bahwa
bulan pertama akan kecil.

**Perbaikan konstruksi yang berhasil:** `bulan_pertama` menghitung `total_byte` lewat
jalur **LANGSUNG** (`total_byte_langsung`), bukan menjumlahkan byte per kelas seperti
`irisan_byte`. Karena itu kedelapan medan selisihnya BEBAS — kebalikan cacat R-308.
Calon KC-50 tetap CALON: cacatnya diperbaiki, bukan diulang.

**Lubang ukur yang diakui:** "bulan pertama" di sini berarti bulan terkecil yang lolos
gerbang 1m dan masuk penyebut 19.586 — **bukan** bulan pertama simbol itu di bursa.
Perbedaan keduanya BELUM diukur (ADR-A016 kep. 6).

**Yang tetap berlaku dari R-307/R-308 dan wajib ikut setiap kali H-A018 dikutip:**
di zona **22.440–97.634 byte** ada **38 baris HIDUP dan NOL baris MATI**. **Besar
berkas DILARANG dipakai sebagai detektor status ke arah mana pun.** Bulan MATI juga
bukan bulan KOSONG — **ISI berkasnya BELUM diukur, dilarang ditebak.**

---

## 5. R-310 — BELUM DISUSUN (pekerjaan berikutnya)

Tidak ada praregistrasi terkunci saat ini. Poros yang direkomendasikan **ADR-A016
kep. 7**: **APA ISI berkas bulan MATI.** Pertanyaan ini sudah **tiga giliran berturut**
tidak terjawab dan kini prioritas pertama. Yang diketahui: bulan MATI berukuran
97.634–451.875 byte, rata 413.306 — jelas tidak kosong, tetapi isinya belum pernah
dilihat. Dugaan yang DILARANG dipakai sebagai kesimpulan tanpa ukuran: lilin berulang,
volume nol, harga beku.

Syarat wajib sebelum pita R-310 dikunci:

1. **Aturan 83 (RESMI)** — tulis satu paragraf aritmetika implikasi di jurnal 131
   lebih dulu. Bila jawabannya sudah tertentu dalam satu angka signifikan, pindahkan
   poros butir itu.
2. **Usulan aturan 84** — hindari klausa ATAU; bila terpaksa, laporkan sumbangan
   BEBAS tiap cabang secara terpisah di dalam laporan modul.
3. **Aturan 79** — praregistrasi masuk `journal/**` sebelum modul dibuat.
4. **Aturan 66** — cacah tiga direktori dengan tangan sebelum menamai modul; hindari
   nama yang mengandung tafsir yang sedang diuji (pelajaran `byte_kecil` dan
   `lubang_tengah`).
5. Laporan WAJIB dirancang RINGKAS (`BATAS_BARIS_LAPORAN=40` — terbukti **TIGA** kali
   berturut menyelamatkan laporan dari pemotongan; dasar usulan aturan 78).

Pertanyaan cadangan bila poros isi-MATI ternyata tak terjangkau alat: **TLMUSDT
2023-03** (satu-satunya kecil yang bukan pertama dan bukan tepi); apakah "bulan pertama
di penyebut" sama dengan "bulan pertama di bursa"; tebing funding `2025-07`.

---

## 6. Pola trio yang sudah terbukti (ikuti apa adanya)

Satu `push_files` atomik berisi tiga berkas (aturan 45):

1. `lux_ai/serapan/<modul>.py` — tetapan penggugur, `sidik_kode()` atas
   `BERKAS_DICAP` (SERTAKAN setiap modul yang ikut menentukan angka),
   `kendali_deteksi()` buatan yang jawabannya dihitung TANGAN lebih dulu,
   `uji_r<nnn>()` yang mengadjudikasi pitanya sendiri, `kode_keluar()` → 2 bila
   laporan tak berhak diklaim, `main()` menulis `reports/<modul>.json`. **Hitung
   besaran invarian lewat jalur LANGSUNG bila mungkin**, agar medan selisih benar-benar
   bebas (pelajaran `total_byte_langsung`).
2. `tests/test_<modul>.py` — butir dinamai `test_01`..`test_NN` tanpa `parametrize`,
   agar cacah dapat diverifikasi dengan mata (aturan 54, 57). **Tulis DAFTAR bernomor
   lengkap, satu nama per nomor, tanpa rentang, sebelum meramal.**
3. `.github/workflows/<modul>.yml` — tiru berkas ASLI yang sudah ada, mis.
   `bulan_pertama.yml` (blob `2242e3e4`) atau `lubang_awal.yml` (blob `3134bc9f`),
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
  `reports/*_status.json` dan `reports/ci_terakhir.json`.
- Panggilan: `connections.mcpServer_github.runTool({toolName, toolArguments})`;
  `owner`/`repo` HANYA di dalam `toolArguments`.
- `ci.yml` (blob `c79497b2`) ber-`paths-ignore` journal / decisions / hipotesis /
  reports; push ke `lux_ai/**`, `tests/**`, `STATE*`, `PROMPT*` MENYALAKAN CI.
- Tulisan ke GitHub TIDAK memakai `editDescriptionVariableName` maupun blok
  `<edit_reference>` — itu hanya untuk halaman Notion.

---

## 8. API terverifikasi (dibaca utuh, aman dipakai)

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
  total=None)`, `main`. Sidik
  `0d3530f69ad51a22e038c17616411b56e4518698ff14c9b635131ec1e2a66562`.
- `irisan_byte` **V1** (blob `2dbe3d5505ac8188a9e212d73db0ce8ba0b2782f`):
  `AMBANG_HIDUP_KECIL=97634`, `AMBANG_MATI_KECIL=150000`,
  `R308_PITA_BUTIR_1=(20,600)`, `R308_PITA_BUTIR_2=(10,300)`, `INVARIAN` 9 kunci,
  `MEDAN_SELISIH` 9, `DETEKSI_TOTAL=1922`; `cacah_di_bawah` STRIKT `<`. Sidik
  `0e7103ef…`. **Cacat:** `total_byte` dijumlahkan dari byte per kelas →
  `selisih_total_byte` TURUNAN; delapan bebas + satu turunan.
- `byte_semesta` **V1** (`ff68e4be`): `R307_PITA_BUTIR_1=(0.02,0.15)`,
  `R307_AMBANG_BYTE_KECIL=10000`, `R307_PITA_BUTIR_2_CACAH=(20,400)`,
  `BATAS_BARIS_LAPORAN=40`. Sidik `e02aca2b…`.
- `silang_funding` **V2** (`42c3aa9d`, 29.873 B): `baca_laporan_kehidupan(akar,total)`
  → **TIGA** nilai `(status, byte_parquet, meta)`, kunci tuple `(simbol,bulan)`;
  `bulan_per_simbol(status)` → `Dict[str,List[str]]` terurut;
  `lubang_funding(funding)` → `(Set[(simbol,bulan)], meta)`; `bentuk_lubang_lokal`,
  `kendali_silang`, `kendali_sah`, `baca_medan_baris(akar,total,
  medan="cacah_lilin")`; `PENYEBUT_TERCATAT=19586`, `MATI_TERCATAT=1401`,
  `KOHORT_TERCATAT=456`, `HIDUP_TANPA_FUNDING_TERCATAT=33`,
  `LUBANG_TAK_DIKENAL_TERCATAT=3`,
  `BENTUK_TERBITAN_FUNDING={"awal":48,"ekor":826,"tengah":6}`.
  **Jangan mengingat tanda tangan dari hafalan — baca modulnya UTUH di giliran yang
  sama (KC-43).**
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

**Pembelahan bulan pertama (R-309):** **787** baris bulan pertama (tepat satu per
simbol) + **18.799** bukan-pertama = 19.586 ✅

**BYTE PARQUET SEMESTA** (diukur di R-307, dikuatkan IDENTIK oleh R-308 dan R-309 dari
modul berbeda — aturan 36, kini TIGA kali): total **32.706.262.375** byte (≈32,7 GB);
`byte_mati` **579.041.399**; `bagian_byte_mati` **0.017704297493883234**; `byte_lain`
**0**; `cacah_byte_nol` **0**.

Sebaran per status (cacah / total byte / min / maks / rata):
- **HIDUP** 18.087 / 32.049.492.952 / **22.440** / 2.770.666 / 1.771.962,899
- **SEPI** 98 / 77.728.024 / 259.327 / 1.231.408 / 793.143,102
- **MATI** 1.401 / 579.041.399 / **97.634** / **451.875** / **413.305,781**

**LEBAR ZONA IRISAN BYTE (R-308):** `cacah_hidup_byte_kecil` (< 97.634) = **38**,
bagian **0.0021009564880853653** · `cacah_mati_byte_kecil` (< 150.000) = **2**, bagian
**0.0014275517487508922**. Daftar 2 MATI-kecil LENGKAP: LENDUSDT 2020-11 97.634 ·
FRONTUSDT 2024-09 109.120.

**IRISAN BULAN PERTAMA (R-309):** `cacah_hidup_kecil_sebagian` **37** dari 38, bagian
**0,973684**; `cacah_pertama` **787**; `cacah_bukan_pertama` **18.799**;
`jumlah_byte_pertama` **706.233.745**; `jumlah_byte_bukan_pertama` **32.000.028.630**;
`rata_byte_pertama` **897.374,517**; `rata_byte_bukan_pertama` **1.702.219,726**;
`nisbah_rata` **0,527179**. Satu-satunya baris kecil yang bukan bulan pertama:
**TLMUSDT 2023-03 (80.394)**. Daftar 38 HIDUP-kecil bertanda LENGKAP ada di UKUR v9 —
**jangan tulis ulang dari ingatan.**

R-306: penyebut 118 = `mati_dulu` **40** + `serempak` **78** + `lubang_dulu` **0**;
bagian 0.339; tebing **39** (0.3305); satu-satunya bukan-tebing **BTCSTUSDT**.

Delapan simbol bangkit: CVCUSDT 29, CVXUSDT 13, SLPUSDT 13, CTKUSDT 11, LITUSDT 10,
TLMUSDT 8, ICPUSDT 2, MAVIAUSDT 2 = 88.

Sidik kode: `bulan_pertama` V1 `0d3530f6…`, `irisan_byte` V1 `0e7103ef…`,
`byte_semesta` V1 `e02aca2b…`, `lubang_tebing` V1 `4a5c2e42…`, `lubang_awal` V1
`156499ce…`, `silang_funding` V2 `8a9b859c…`, `sebab_bangkit` V1 `bafe4359…`,
`tersisip_semesta` V1 `9618fd19…`, `bentangan_kohort` V2 `8ca6ebbe…`, laporan
kehidupan seragam `24b6bb26…`, `sidik_data_funding` `2c9fbd1b…`.

---

## 10. Utang yang masih hidup (urut prioritas)

1. **Susun praregistrasi R-310** di jurnal 131 (aturan 79), dengan aritmetika
   implikasi ditulis lebih dulu (aturan 83) dan tanpa klausa ATAU yang tak terukur
   terpisah (usulan aturan 84). Poros yang direkomendasikan: **isi berkas bulan
   MATI** (ADR-A016 kep. 7). Lalu bangun trionya.
2. **Cacah tangan tiga direktori lagi** sesudah trio berikutnya — angka 47 / 51 / 42
   hanya sah untuk ref `010edff2`.
3. Aturan 52: `tests/test_bentangan_kohort.py` V2 (63 butir, blob `9f850ecd`) belum
   dibaca byte demi byte. **Utang ini sudah TUJUH versi berturut-turut — jangan
   diam-diam dihapus.**
4. Belum dibaca utuh: `decisions/ADR-A002.md`, A004, A006, A007, A008,
   `PETA_MODUL.md`, `PETA_MODUL_BERKAS.md`, `STATE_LAMPIRAN.md`,
   `STATE_LAMPIRAN_ANGKA.md`, `karantina_semesta.yml` (`de40fa4e`),
   `tests/test_pulihkan.py` (`11c43533`), `test_rilis_karantina.py` (`739c8da9`),
   `test_karantina_a006.py` (`a5a3d82f`).
5. Adjudikasi tertunda: R-7, R-19, R-20, R-28, R-36, R-37, R-199; gali R-28 dari
   STATE v23 (KC-32); salin R-236..R-247 dari jurnal 92–94; periksa R-224..R-235.
6. ADR A003 / A005 / A006 / A007 belum diputuskan; **A003 wajib memuat koreksi
   A011/A012/A013/A014/A015/A016**.
7. **Ramalan yang belum terukur:** sesudah push STATE v49 (`8dd0e4a5`) ramalan "CI
   tetap 1233" belum sempat diverifikasi — run untuk commit itu belum tercatat saat
   `ci_terakhir.json` dibaca. Bukan tepat, bukan meleset. **Jangan mencatatnya sebagai
   kemenangan beruntun.**
8. Pertanyaan terbuka urut prioritas: **apa ISI berkas bulan MATI** (97.634..451.875
   byte tetapi ringan — BELUM diukur, DILARANG ditebak; tiga giliran tak terjawab);
   **TLMUSDT 2023-03**; apakah "bulan pertama di penyebut" = "bulan pertama di bursa";
   mengapa 39 simbol berhenti berfunding tepat `2025-07` dan mengapa BTCSTUSDT
   satu-satunya yang lepas; irisan **880 lawan 877**; selisih **40−38**
   `diagnosa_kc15`; tanggal hari hilang BNXUSDT 2022-04/06/08; bentangan 38 kohort
   puncak; `mati_tersisip` atas 19.586; H-A016 (celah kelipatan 15 menit);
   `ukur_baris` V6 (KC-26); **taksonomi lubang tiga kelas** (ADR-A013).

---

## 11. Nada kerja

Ukur, jangan mengarang. Bila angka belum diukur, katakan belum diukur. Bedakan angka
TERUKUR dari angka TURUNAN dan katakan mana yang mana — dan bedakan pula MELIHAT dari
MENGUKUR: tiga dugaan yang lahir dari memandang daftar ternyata salah semua. Bila
ramalan meleset, tulis MELESET dan cari sebabnya. Bila ramalan MENANG, cari bagian
mana dari kemenangan itu yang sebenarnya kosong — R-309 menang 3/3 dan tetap
melahirkan satu usulan aturan baru dari cacatnya sendiri. Kemenangan yang tidak
mengajarkan apa pun wajib dinyatakan lemah walau menang. Bila temuan melawan tafsir
yang kamu sukai, tulis temuan itu lebih keras, bukan lebih pelan. Bila dokumen sendiri
bertentangan dengan berkas sumber, berkas sumber menang dan dokumen dikoreksi pada
giliran itu juga. Tutup setiap giliran dengan jurnal, dan tinggalkan PROMPT + STATE
yang bisa dipakai orang lain tanpa bertanya apa pun.
