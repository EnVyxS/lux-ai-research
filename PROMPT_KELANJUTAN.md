# PROMPT KELANJUTAN — versi 34

Disusun 29 Juli 2026, 14:55 WIB, di atas STATE v31 (commit `9819d76b`) serta
jurnal 83 dan 84. Berkas di repo adalah kebenaran; prompt ini hanya peta.

Kamu melanjutkan riset LUX-AI. Operator: Diva Juan Nur Taqarrub, GitHub EnVyxS,
zona waktu Asia/Jakarta, bahasa kerja Indonesia. Jangan mulai bekerja sebelum
menyelesaikan LANGKAH 0.

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`, dengan
   `owner` dan `repo` HANYA di dalam `toolArguments`, tidak di tingkat atas.
3. Baca dari `main` repo `EnVyxS/lux-ai-research` berurutan: berkas ini,
   `STATE.md` (v31 — aturan 1–55, kelas cacat, papan skor, daftar utang; INI
   YANG PALING PENTING dan kini TIDAK tertinggal dari jurnal),
   `journal/2026-07-29-84.md`, lalu `-83.md` untuk tabel silang funding penuh,
   `decisions/ADR-A008.md` (DITERIMA 1–6, Keputusan 7 ditangguhkan),
   `decisions/ADR-A007.md` (masih DIUSULKAN), lalu `ADR-A004.md` dan
   `ADR-A002.md` bila menyentuh serapan (§10 BELUM disentuh),
   `PETA_MODUL.md` bila menyentuh modul warisan.
4. Baru setelah itu jalankan pekerjaan teknis.

## BATASAN YANG MAHAL DIPELAJARI ULANG

- Sandbox agen TIDAK punya jaringan. Semua unduhan dan pengukuran arsip
  dijalankan GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- Tidak ada alat membaca status GitHub Actions dan tidak ada alat memicu
  `workflow_dispatch`. Status hanya diketahui dari berkas laporan yang
  di-commit workflow itu sendiri, dan satu-satunya cara menyalakan run adalah
  push ke berkas yang tersebut di `paths` workflow. Manfaatkan ini: memperbaiki
  BERKAS UJI tidak menyalakan ulang runner berat, sebab `paths` hanya memuat
  modulnya.
- **BARU DAN MAHAL (aturan 55):** `.github/workflows/ci.yml` memakai
  `paths-ignore` untuk `journal/**`, `decisions/**`, `hipotesis/**`, dan
  `reports/**`. Commit yang HANYA menyentuh jurnal atau ADR **tidak menyalakan
  CI sama sekali**. Dua ramalan (R-209, R-212) hangus karena ini. Sebelum
  meramalkan hasil workflow, baca pemicunya dan sebutkan workflow mana yang akan
  menyala. `STATE.md` dan `PROMPT_KELANJUTAN.md` ada di AKAR, jadi keduanya
  MENYALAKAN CI.
- Tidak ada API patch — `push_files` menulis ulang seluruh isi berkas. Rancang
  berkas kecil, dan sesudah mendorong berkas panjang BACA ULANG dari `main`
  untuk memastikan ekornya hadir (aturan 52).
- Saat memeriksa hasil run, cocokkan `commit` / `run_id` / `sidik_kode`. Jangan
  percaya keberadaan berkas: laporan run lama sering masih terbaca.
- Laporan yang belum terbit menjawab "path does not point to a file" — itu bukan
  kegagalan push, melainkan run yang masih berjalan. Melisting `reports/`
  (path berakhiran garis miring) lebih murah daripada menebak nama berkas.
- `search_code` mengembalikan 0 hasil (tidak berindeks) — pakai
  `get_file_contents`.
- Runner punya numpy, pandas, pyarrow, pyyaml, pytest; TIDAK ada scipy dan
  requests. `data.binance.vision` bisa diakses; `fapi.binance.com` memberi 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`. Repo `lux-research`
  boleh DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## POSISI (29 Juli 2026, 14:55 WIB)

Rantai commit mutakhir: `e94ed337` (jurnal 82) → `7f659544` (STATE v30 + PROMPT
v33) → **`1b0e8d8e`** (silang_funding V1 + uji + workflow, atomik) → `fbbb61c2`
(commit laporan runner) → **`5f2b7046`** (jurnal 83) → **`67ec2be4`**
(`ukur_baris` V3) → **`d4451a60`** (jurnal 84) → **`9819d76b`** (STATE v31) →
berkas ini.

Run terverifikasi (commit dicocokkan):

- **silang_funding** pada `1b0e8d8e` — laporan penuh 183.963 B, ringkas blob
  `8c63ada6…`, `kendali_sah` true, seluruh medan penggugur nol.
- **ukur_baris V3** pada `67ec2be4` — 12 berkas, 3.885 baris, 0 lewat pagar.
- **CI 30431610324** (`1b0e8d8e`) — **316 butir, kode 0**.
- **CI 30433635955** (`67ec2be4`) — **316 butir, kode 0**.

Papan skor sampai R-216: **TEPAT 150 / MELESET 39 / SEPARUH 12 / TIDAK
TERADJUDIKASI 7 / MENUNGGU 8 = 216** (MENUNGGU: R-7, R-19, R-20, R-28, R-36,
R-37, R-199, R-216). Ramalan berikutnya **R-217**. Aturan terakhir **55**, kelas
cacat terakhir **KC-18**, hipotesis terakhir **H-A009 (GUGUR)**, jurnal
berikutnya **85**, STATE berikutnya **v32**, PROMPT berikutnya **v35**, ADR
berikutnya **A009**.

**Cacat prosedural yang harus diadjudikasi jujur:** R-216 ditulis di jurnal 84
sebagai "CI 316 butir kode 0 pada commit berikutnya, yang memuat STATE v31 DAN
PROMPT v34". Kedua berkas itu ternyata didorong pada DUA commit terpisah
(`9819d76b` lalu commit berkas ini), sehingga commit yang dimaksud ramalan itu
tidak pernah ada dalam bentuk persis. Keduanya menyalakan CI. Adjudikasi yang
jujur: catat R-216 atas commit PERTAMA yang memuat salah satu berkas
(`9819d76b`) dan tulis tersurat bahwa kata-katanya tidak cocok penuh — jangan
mengaku TEPAT tanpa catatan itu. Ini kerabat aturan 45 dan 55: ramalan wajib
menyebut commit yang benar-benar akan ada.

## TEMUAN MUTAKHIR YANG MENENTUKAN ARAH

1. **Pertanyaan 945 TERJAWAB — dan jawabannya membelah dua gejala.** Atas
   penyebut 19.586: MATI 842 berlubang funding / 559 berfunding; SEPI 2 / 96;
   HIDUP **33** / 18.054. Uji silang: 877 lubang dalam penyebut + 3 lubang tak
   dikenal = **880**, persis angka `funding.py` V6.
2. **Dua arah wajib dipisah.** lubang → mati **96,0%** (842/877) KUAT;
   mati → lubang **60,1%** (842/1.401) LEMAH. Lubang funding karena itu TIDAK
   sah dipakai sebagai penyaring kematian — memakainya melewatkan 559 bulan
   mati. Irisan BUKAN sebab (aturan 10).
3. **H-A009 GUGUR:** "lubang funding dan kematian pasar adalah satu gejala"
   dipatahkan oleh 559 simbol-bulan MATI yang tetap berfunding.
4. **Sisa yang benar-benar mencurigakan: 33 simbol-bulan HIDUP tanpa funding.**
   Daftarnya BELUM ADA di laporan mana pun — `silang_funding` V1 hanya
   menerbitkan `baris_mati`. Ini pekerjaan nomor satu.
5. **Aturan 54** lahir dari R-211 (cacah butir uji dicacah dari berkas jadi,
   bukan dari ingatan rancangan; 316 lawan ramalan 312). **Aturan 55** lahir dari
   R-209 dan R-212 (jangan meramalkan run yang tak akan menyala).
6. ADR-A002 §10 tetap TIDAK disentuh. Pertanyaan penentunya kini: apakah ke-33
   bulan HIDUP tanpa funding itu bulan AWAL (48 lubang `awal` sudah terukur),
   ataukah cacat penerbitan yang sesungguhnya.

## PEKERJAAN BERIKUTNYA

1. **`silang_funding` V2** — terbitkan `baris_hidup_tanpa_funding` (33 baris
   diharap) dan daftar **3 lubang tak dikenal**, ditambah `bentuk_lubang` per
   baris (awal/ekor/tengah) supaya dugaan "bulan awal" dapat diadjudikasi tanpa
   pengukuran ketiga. Push atomik modul + uji + workflow (aturan 45); cacah butir
   uji dihitung menurut aturan 54.
2. **Sebaran 1.401 MATI menurut tahun dan simbol** dari `reports/silang_funding.json`
   (183.963 B, memuat `baris_mati` lengkap: simbol, bulan, `di_kohort_puncak`,
   `lubang_funding`); sekalian `bulan_hidup_terakhir` bagi 28 anggota kohort di
   luar sampel abjad — definisi wajib dicocokkan dengan `kohort_ekor` (aturan 36).
3. **Sifat 48 lubang funding AWAL dan 6 lubang TENGAH** — prasyarat Keputusan 7
   ADR-A008, dan kini bertaut langsung dengan ke-33 bulan HIDUP tanpa funding.
4. **R-199** — jalankan ulang `pulihkan` V2 atas kedelapan pecahan
   (`definisi_dapat_dibedakan` diramalkan false pada indeks 2 dan 5). Sampai itu
   `reports/pulihkan_pecahan_<i>.json` dibaca sebagai laporan V1.
5. **Terima atau tolak ADR-A007** dengan kendala R-146 (839.842.134 sudah memuat
   516.135 baris karantina). **Terapkan ADR-A006 sepenuhnya**;
   `dugaan_pengganti` (ADR-A005); karantina artefak 7 hari; adjudikasi R-7,
   R-19, R-20, R-28, R-36, R-37.
6. Kehidupan 12 simbol-bulan karantina (tar terpisah, belum disentuh).
7. `funding.py` 705 baris — aturan 48 melarang menambah fungsi sebelum dipecah.
8. Belum diukur (daftar penuh di STATE v31 bagian terakhir): sebab KC-15, lubang
   funding BNXUSDT, 15 SETTLED lain, INDEKS 3 nama manual, token saham dan
   komoditas, 16 simbol non-ASCII, `.decode("utf-8","replace")`, BUSD/USDC,
   jurang 38 lawan 41, skew `waktu_utc`, `funding_selisih_penuh.json`, selisih
   byte AGIX 531 lawan 529, `tests/test_pulihkan.py` belum dibaca ulang.
9. Paralel (aturan 3): ADR-A003 (berkasnya BELUM ADA), juri T4 dengan biaya,
   lapisan validasi (Šidák, ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy
   murni). **Adjudikasi riset TETAP TERKUNCI.**

## KEBIASAAN

- Tulis ramalan SEBELUM run, lalu adjudikasi jujur. Ramalan berkepala dua yang
  separuhnya salah dicatat SEPARUH. Ramalan yang penyebutnya nol dicatat TIDAK
  TERADJUDIKASI, bukan TEPAT. Ramalan atas run yang tak akan menyala DILARANG
  (aturan 55).
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21). Jangan
  menaksir yang bisa dihitung — pola menaksir panjang berkas sudah meleset tiga
  kali (R-175, R-179, R-203) dan baru berhenti pada R-213/R-214.
- **Aturan 53:** sebelum meramalkan kode keluar CI, baca PERILAKU tiap fungsi
  yang diuji. **Aturan 54:** cacah butir uji dengan mencacah `def test_` pada
  berkas uji yang SUDAH selesai ditulis, kalikan fungsi berparameter dengan
  cacah kasusnya.
- Setiap pengukuran sebab wajib memuat medan penggugur (aturan 24); aturan 37
  sampel wajib memuat ≥1 kasus tiap kelas cacat relevan; aturan 20 dilarang
  menyimpulkan di luar rentang disampel; aturan 50 kesimpulan dari KETIADAAN
  wajib kendali positif; aturan 51 jendela mundur wajib adaptif; aturan 52
  laporan yang tak terbaca utuh setara dengan tak ada.
- Pisahkan arah sebuah irisan: A→B dan B→A adalah dua angka, dan mencampurnya
  melahirkan tafsir terbalik (pelajaran KC-18 lawan funding).
- Push yang menyalakan run wajib atomik (aturan 45): modul + uji + workflow.
- BACA berkas sebelum menuduhnya salah — pola salah-tuduh sudah tercegah TUJUH
  kali. Sebaliknya, jangan menuduh modul ketika yang salah adalah harapan uji,
  dan jangan menuduh laporan tertimpa ketika yang salah adalah pemicu workflow.
- Pisahkan fakta dari asumsi; tanpa bukti tulis "Ini memerlukan verifikasi."
- "lanjut" berarti teruskan tanpa konfirmasi. Perbarui STATE.md, jurnal, dan
  berkas ini secara berkala. Jangan berhenti dengan alasan konteks Notion;
  patokannya konteks model.
- Tenggat: riset dipercepat sebelum 3 Agustus 2026.
