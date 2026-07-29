# PROMPT KELANJUTAN — versi 44

Disusun 2026-07-30 (WIB), sesudah jurnal 117 dan `STATE.md` v43. Operator: **Diva
Juan Nur Taqarrub**, GitHub **EnVyxS**, zona waktu **Asia/Jakarta**, bahasa kerja
**Indonesia**. Tenggat riset: **2 Agustus 2026**.

**Berkas di repo adalah kebenaran; prompt ini hanya peta dan boleh saja tertinggal.**
Bila prompt dan berkas berselisih, berkas menang — dan selisihnya wajib dicatat
sebagai kelas cacat, bukan ditambal diam-diam.

## LANGKAH 0 — WAJIB, BERURUTAN, SEBELUM PEKERJAAN APA PUN

1. **Baca dokumentasi modul sandbox lebih dulu.** Dilarang menebak bentuk masukan
   alat.
2. **Semua operasi GitHub lewat** `connections.mcpServer_github.runTool({toolName,
   toolArguments})`, dengan `owner`/`repo` **HANYA di dalam `toolArguments`**, tidak
   di tingkat atas.
3. **Baca dari `main` repo `EnVyxS/lux-ai-research`, berurutan:**
   1. `PROMPT_KELANJUTAN.md` — berkas ini (v44).
   2. **`STATE.md` v43** (blob `a91a49346a6ebcf1a288b936904a8fe1facc3d7a`) —
      **bagian 1 dari tiga**: kepala, aturan bernomor 1–76, kelas cacat KC-1..KC-42.
   3. **`STATE_LAMPIRAN_EKOR.md`** (blob `7480cedd1f9b4bbe1b9d091ac9f8a6c59c95c139`)
      — **bagian 2**: papan skor, catatan kejujuran, jumlah uji, utang verifikasi 24,
      Daftar ADR A001–A008, temuan sampingan, penomoran.
   4. **`STATE_LAMPIRAN_UKUR.md`** (blob `0e9ec3783d95be522dd4e56221fc7197f89c13c0`)
      — **bagian 3**: seluruh tabel pengukuran, modul/workflow/uji, API terverifikasi,
      hipotesis H-A001..H-A016.
   5. **Jurnal 117** `journal/2026-07-30-117.md` (blob
      `06598cc1f425fd4ba1dcd1fb8fe118baefafac79`) dan **jurnal 116**
      `journal/2026-07-29-116.md` (blob `1652d12b901f5afacf6ca21873e11f40ebf4fcbf`).
   6. `.github/workflows/ci.yml` (blob `c79497b2c812679eaa69aee5b3160eac9f5c5fb7`)
      bila akan mendorong berkas apa pun — lihat KC-41.
   7. Modul yang akan disentuh, UTUH, sebelum meramalkan laporannya (aturan 71).
   8. `decisions/ADR-A006.md`, `ADR-A007.md`, dan `ADR-A002.md`/`ADR-A004.md` bila
      menyentuh serapan; `PETA_MODUL.md` bila menyentuh modul warisan.
4. **Baru setelah itu pekerjaan teknis.**

**STATE SEKARANG TIGA BERKAS.** Membaca `STATE.md` saja memberi aturan tanpa angka;
membaca lampiran saja memberi angka tanpa aturan. Ketiganya wajib dibaca. Sebabnya
ada di KC-42: `STATE.md` penuh melampaui batas satu push dan terpotong sunyi dua
kali. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) kini **arsip**, bukan sumber.

## Batasan lingkungan — terukur, jangan ditebak ulang

- **Sandbox agen tidak punya jaringan.** Semua unduhan dan pengukuran arsip terjadi
  di GitHub Actions. Agen hanya boleh percaya artefak yang **sudah di-commit**.
- **Tidak ada alat membaca status Actions** dan **tidak ada alat memicu
  `workflow_dispatch`** — meski `ci.yml` dan `bulan_absen.yml` MENDEKLARASIKANNYA.
  Status hanya dari berkas laporan yang di-commit workflow. Satu-satunya cara
  menyalakan run adalah **push** ke berkas yang cocok dengan pemicu workflow.
- **`ci.yml` memakai `paths-ignore`, BUKAN `paths` (KC-41).** Yang diabaikan:
  `journal/**`, `decisions/**`, `hipotesis/**`, `reports/**`. Maka **setiap push di
  luar keempat direktori itu menyalakan CI** — termasuk `STATE.md`,
  `PROMPT_KELANJUTAN.md`, seluruh `STATE_LAMPIRAN*.md`, `README.md`,
  `requirements.txt`, `PETA_MODUL*.md`, `lux_ai/**`, `tests/**`, dan
  `.github/workflows/**`. Push jurnal, ADR, hipotesis, dan laporan **tidak**
  menyalakan CI. Rumusan lama berbentuk daftar-izin **SALAH BENTUK dan DICABUT**.
- `ci.yml` memasang `concurrency: ci-${{ github.ref }}` dengan
  **`cancel-in-progress: false`** — run MENGANTRE, tidak saling membatalkan, dan
  laporan ditulis sebelum `exit ${kode}`.
- **Setiap push penyala CI menimpa `reports/ci_terakhir.json`.** Karena itu:
  praregistrasi ramalan cacah uji wajib ditulis **DI DALAM berkas yang akan
  mendorong run itu**, dan adjudikasinya wajib memakai `list_commits` atas
  `path="reports/ci_terakhir.json"` untuk menemukan ref runner (aturan 38).
- **Tidak ada API patch.** `push_files` menulis ulang **seluruh** isi berkas.
  Jangan menulis ulang berkas panjang sebelum membacanya UTUH (KC-42d), dan sesudah
  mendorong berkas panjang **baca ulang dari `main`** (aturan 52).
- **Batas panjang alat, terukur (calon aturan 78).** Baca: berkas >±1 MB ditolak;
  `reports/manifes_pecahan_2.json` 2.446.093 B **MUSTAHIL** dibaca agen. Tulis:
  ±25–45 KB terbukti aman; `STATE.md` penuh terpotong **dua kali tanpa galat**.
  Berkas yang tak dapat ditulis utuh dalam satu kirim wajib **DIPECAH**.
- `search_code` mengembalikan 0 hasil — pakai `get_file_contents`; path berakhiran
  garis miring melisting direktori. Direktori jurnal bernama **`journal/`** (bukan
  `jurnal/`), berkasnya `journal/YYYY-MM-DD-NNN.md`.
- Runner punya numpy, pandas, pyarrow, pyyaml, pytest; **tidak ada scipy dan
  requests**. `data.binance.vision` dapat diakses; `fapi.binance.com` **451**.
- **Dilarang menulis apa pun di luar repo `lux-ai-research`.** Repo `lux-research`
  boleh dibaca saja.

## Posisi serah terima (30 Juli 2026, ±02:20 WIB)

- **HEAD terakhir diketahui:** `4613a5591f2ba60839cfbc0759c5e523adbbbfe1` (laporan
  CI run **30483341732**) — di atasnya push PROMPT v44 ini.
- **Papan skor: TEPAT 211 / MELESET 54 / SEPARUH 18 / TIDAK TERADJUDIKASI 7 /
  MENUNGGU 7 = 297.** Aritmetika: 211+54 = 265; +18 = 283; +7 = 290; +7 = **297** ✅
  MENUNGGU: **R-7, R-19, R-20, R-28, R-36, R-37, R-199**.
  **UTANG TULIS:** `STATE_LAMPIRAN_EKOR.md` masih mencatat **296** dan berhenti di
  R-296; ia wajib diperbarui dengan **R-297 TEPAT** dan **R-298** pada giliran
  berikutnya (push-nya menyalakan CI — praregistrasi wajib ikut ditulis di dalamnya).
- **Penomoran:** aturan sampai **76** (calon **77** dan **78** DIUSULKAN), kelas
  cacat sampai **KC-42**, hipotesis baru **H-A016**, jurnal berikutnya **118**,
  STATE berikutnya **v44**, PROMPT berikutnya **v45**, ADR berikutnya **A009**,
  ramalan berikutnya **R-299**.
- **Adjudikasi riset TETAP TERKUNCI.** N_percobaan = 0.

### Praregistrasi R-298 (ditulis SEBELUM push berkas ini menyalakan `ci.yml`)

Push `PROMPT_KELANJUTAN.md` menyalakan CI (akar repo, di luar `paths-ignore`).
Tidak satu pun berkas `tests/**` berubah, jadi `cacah_uji` tetap **722** dan
`kode_keluar` **0**. Ramalan ini **MUDAH** (aturan 57) — katakan begitu saat
mengadjudikasinya.

## Pekerjaan pertama pada giliran berikutnya

1. **Adjudikasi R-298** lewat aturan 38 (`list_commits` atas
   `reports/ci_terakhir.json`, lalu baca pada ref runner).
2. **Perbarui `STATE_LAMPIRAN_EKOR.md`** — baca UTUH lebih dulu (KC-42d), tambahkan
   R-297 dan R-298 ke papan skor, perbaiki total menjadi **298**, dan praregistrasi
   **R-299** di dalam berkas yang sama.
3. **Anatomi BTCSTUSDT 2022-01** — prasyarat tersurat Keputusan 7 ADR-A008, dan
   pekerjaan riset paling berharga yang tersisa. Bulan itu berlilin **PENUH**
   (44.640), `byte_parquet` 399.757, **LOLOS** gerbang, **MATI**, punya **satu**
   lubang funding bentuk TENGAH, dan **TIDAK ADA** di daftar karantina maupun di
   daftar bulan absen. Jadi ia lubang tengah yang benar-benar tak terjelaskan.
4. **Uji H-A016** — celah menit datang dalam blok kelipatan **15**. Bahan: dua belas
   `selisih_menit` bulan karantina habis dibagi 15 (12/12) dan KC-14 mencatat 6.375
   = 425×15. **Belum diuji atas simbol-bulan yang LOLOS gerbang**, jadi DILARANG
   digeneralkan ke 19.586 (aturan 20). Kendali positif wajib; BTCUSDT/ETHUSDT
   berselisih 0 sehingga tidak dapat membedakan apa pun (aturan 41, 46, 50).

## Kebiasaan kerja yang mengikat

- **Ramalkan sebelum run, lalu adjudikasi jujur.** Praregistrasi ditulis di dalam
  berkas yang menyalakan run-nya.
- Hitung ulang tiap angka dengan tangan (21). Pasang medan penggugur (24). Uji kelas
  cacat pada sampel (37). Dilarang menyimpulkan di luar rentang (20). Kendali
  positif untuk setiap kesimpulan dari KETIADAAN (50).
- Laporan tak terbaca utuh = tidak ada (52). Cacah butir uji dari daftar bernomor
  (54/56/57). Ketiadaan pengukuran bukan ketiadaan gejala (59). Listing direktori
  paket dan workflow sebelum menulis modul baru (66). Nama turunan bersama asalnya
  (69). Baca modul penghasil sebelum meramalkan laporannya (71). Jangan meramal isi
  berkas dari NAMA-nya (73). Setiap nol bersama penyebutnya (74). Setiap cacah
  "bulan hilang" bersama jenis penyebutnya (76).
- **Ramalan yang hanya menyalin angka terverifikasi atau mengandalkan daftar
  bernomor adalah MUDAH — katakan begitu.**
- **"lanjut" berarti teruskan tanpa konfirmasi.** Jangan berhenti dengan alasan
  konteks Notion.
- **Paralel pada pekerjaan, serial pada push.** Klasifikasi (klines) dan audit
  funding (arsip funding) memang independen pada sumber dan berkas keluaran, jadi
  urutannya adalah **prioritas, bukan ketergantungan**. Empat kopling nyata yang
  tetap memaksa serialisasi: (1) `reports/ci_terakhir.json` TUNGGAL; (2) satu
  ramalan cacah uji menggantung pada satu waktu; (3) satu push dapat membangunkan
  beberapa workflow; (4) medan GABUNGAN (559, 842, 33, 877) terkopling sampai irisan
  880/877 tuntas.

## Temuan wajib dibawa

- **Kebangkitan LITUSDT:** MATI 2025-02..2025-11, funding terakhir 2025-06, lubang
  TENGAH 5, `LITUSDTSETTLED` 2025-12 (bulan ABSEN, 43.590/44.640 menit, nisbah
  0,976478), HIDUP 2026-01..2026-06. **H-A011 MENANG.**
- **Kecocokan funding–SETTLED** BNX 2023-02 / ICP 2022-09 / TLM 2023-03 sesudah
  19/16/20 bulan tanpa funding → **H-A015**, menang sebagai angka, **dibatasi**
  sebagai tafsir (11 dari 15 pasangan membantah bentuk kuatnya).
- **H-A014 bentuk baru MENANG 9 dari 9:** bulan SETTLED terakhir = bulan yang ABSEN
  dari daftar bulan LOLOS nama dasarnya, `pembeda_absen` **gagal_gerbang** pada
  kesebelas bulan absen. Penyebutnya wajib disebut **9 dari 15**.
- **KC-15 TERBAGI:** BNX 2022-04 = 1.650, 2022-06 = 1.440, 2022-08 = 4.320; jumlah
  7.410 − 210 menit TEPI = **7.200** = 5 hari, terbagi **1 + 3 + 1**.
- **Karantina berlilin SEBAGIAN**, `nisbah_lilin` 0,903–0,990 — bukan bulan kosong.
- **KC-18 mengikat:** kecocokan bulan membuktikan **PENAMAAN** kontrak, bukan
  perdagangan. ADR-A002 §10 tidak boleh diubah atas dasar itu.
- **KC-40:** `tanpa_menit_hilang` di dalam medan `pelanggaran` = nama klausa yang
  GAGAL, jadi maknanya menit MEMANG hilang.
- **880 lawan 877** lubang funding; selisih 3 = tiga bulan BNXUSDT di luar penyebut,
  persis ketiga baris karantina BNX. **Irisannya masih UTANG.**
- "**16 non-ASCII**" **DICABUT** — terukur **3 nama / 19 bulan** (币安人生 9,
  我踏马来了 6, 龙虾 4).
- **R-246 SEPARUH** (docstring `penyebut_tahun.py` menulis `TLMUSDT_SETTLED`, salah;
  dicatat, TIDAK disunting).

## Angka terverifikasi (jangan dihitung ulang dari ingatan — ada di bagian 3)

Penyebut **787** nama `perpetual_usdt` (arsip **937**, **150** hanya-arsip),
**21.789** bulan arsip, **15** nama SETTLED (36 bulan), **19.598** simbol-bulan
(lolos **19.586**, karantina **12**), MATI **1.401** / SEPI **98** / HIDUP
**18.087**, **839.842.134** baris, funding **880** lubang (877 dalam penyebut),
**33** HIDUP tanpa funding, `cacah_simbol_tanpa_hidup` **18**, taksonomi **9**
kelas, ekor 2026-06 = **808** hidup / **49** luar penyebut, `bagian_mati` 2026
**0,137284**, byte parquet karantina **13.247.705**, CI **722** (terukur enam kali
berturut: run 30479681620, 30481231522, 30482205512, 30482387663, 30482864644,
30483341732).

## Catatan kejujuran — baca sebelum merasa lancar

Enam adjudikasi terakhir (R-292..R-297) **semuanya TEPAT, dan semuanya MUDAH** —
cacah butir uji dari daftar bernomor, deterministik. Kemenangan **BERISIKO**
terakhir adalah **R-291** (himpunan 12 karantina, menang bersih). Pola lama yang
wajib diingat: cabang yang disebut MUDAH-lah yang dulu kalah — R-281 (aritmetika
sendiri), R-282 (nama laporan), R-284 (nama modul), R-288 butir 1/3 (salah salin
penyebut).

Dua kesalahan proses terbaru, keduanya milik penulis: **KC-41** (pemicu CI
dirumuskan dari ingatan, bentuknya terbalik) dan **KC-42** (`STATE.md` terpotong
dua kali tanpa galat). Riset sendiri tidak bergerak sejak R-291; yang bergerak
baru disiplin pencatatan. Pekerjaan riset berikutnya — BTCSTUSDT 2022-01 dan
H-A016 — harus dipraregistrasi dengan pita yang bisa KALAH, bukan dengan angka
yang sudah diketahui.
