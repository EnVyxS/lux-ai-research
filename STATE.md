# STATE — versi 25

Diperbarui: 2026-07-29 (sesi 53). Aturan hanya BERTAMBAH; jangan menulis ulang
dari ingatan. v25 disusun di atas teks v24 yang dibaca langsung dari `main`
(blob `ae5a077f`), ditambah kedelapan log run **`30396803601`**.

Peristiwa terbesar sejak v24: **semesta bertahan UTUH, termasuk yang cacat.**
v24 menutup dengan satu lubang — 12 parquet karantina diukur lalu lenyap. Lubang
itu tertutup. Yang tersisa bukan lagi soal apa yang disimpan, melainkan apakah
yang tersimpan bisa diambil kembali oleh mesin lain.

## Aturan bernomor

Aturan 1–36 berlaku tanpa perubahan; teksnya ada di STATE v19 (blob
`e06c486e…`). Ringkas nomornya: 1 satu definisi R · 2 gerbang kandidat ·
3 adjudikasi terkunci · 4-5 modul warisan · 6 hanya arsip publik · 7 sidik wajib ·
8 ≤800 baris · 9 satu jalur eksekusi · 10 diagnostik `bukan_bukti` · 11 biaya
sejak hari pertama · 12 guard struktural · 13-14 tanpa jaringan · 15 kode repo
lain · 16 nama medan jujur · 17 data biaya hilang → keluar · 18 gerbang lolos
wajib bercacah · 19 Decimal · 20 rentang disampel · 21 hitung ulang · 22 cakupan
`sidik_kode` · 23 gerbang merah tak dilonggarkan · 24 medan penggugur ·
25 cakupan dipatok sebelum run · 26 ramalan mutlak butuh besaran · 27 pendamping
tak bersyarat · 28 bulan awal parsial · 29 amandemen tak menghapus · 30 penyebut
eksplisit · 31 `sidik_data` · 32 nama non-ASCII · 33 pemicu sempit · 34 dilarang
add borongan · 35 laporan tanpa sidik hanya petunjuk · 36 dua angka beda →
definisi berdampingan.

37. **[v20]** Sampel yang dipakai menguji sebuah jalur wajib memuat sedikitnya
    satu kasus dari tiap kelas cacat yang diketahui relevan, dan laporan wajib
    menyebut kelas mana yang tersentuh dan mana yang tidak, walau cacahnya nol.
38. **[v21]** Cacah uji hanya sah dari `reports/ci_terakhir.json` (run id +
    commit + `kode_keluar`). Penjumlahan taksiran dilarang ditulis sebagai angka
    uji. Lahir dari selisih 135 lawan **141**.
39. **[v22]** Keseragaman yang terukur pada sampel DILARANG dipakai sebagai
    angka ramalan untuk anggota di luar sampel; wajib pita atau kemungkinan
    campuran. Lahir dari R-114.
40. **[v22]** Tiap laporan yang mencacah baris sebuah simbol-bulan wajib memuat
    uji silang `baris + hilang_di_tengah + tepi = menit_kalender` dan melaporkan
    selisihnya walau nol. Lahir dari 210 menit BNXUSDT 2022-04.
41. **[v23]** Ramalan bersyarat yang penyebutnya nol dicatat TIDAK
    TERADJUDIKASI, bukan TEPAT, dan status itu wajib dipra-registrasikan bersama
    ramalannya. Lahir dari R-120.
42. **[v23]** Kelas cacat baru DILARANG dinamai atas dasar satu angka yang
    belum diukur langsung. Tuduhan ditulis sebagai hipotesis + run, bukan
    sebagai kelas. Lahir dari KC-16 yang ditarik.
43. **[v24]** Medan penggugur yang membandingkan taksiran dengan kenyataan wajib
    memakai toleransi yang BERSKALA terhadap cacah item, bukan margin datar.
    Margin datar 20.480 byte membuat 16 uji lolos sementara produksi gagal pada
    1.055 anggota, karena cacatnya (header pax 1.024 B per anggota) tumbuh per
    item sedangkan marginnya tidak. Uji wajib memuat kasus bercacah besar.
44. **[v24]** Ramalan wajib menyebut penyebutnya secara eksplisit: pecahan mana,
    semesta mana, medan mana. Bila sebuah pita hanya masuk akal di bawah satu
    tafsir dan meleset di bawah tafsir lain, ia diadjudikasi MELESET. Lahir dari
    R-131, yang pitanya disusun untuk delapan pecahan tetapi medannya hanya ada
    pada tujuh.
45. **[v25] Keatomikan push pemicu.** Sebuah push yang MENYALAKAN run wajib
    memuat setiap berkas yang run itu bergantung padanya, dan daftar berkas itu
    wajib dihitung ulang tepat sebelum dikirim. GitHub Actions memakai berkas
    workflow pada commit PEMICU, sehingga perbaikan workflow yang menyusul di
    commit berikutnya TIDAK berlaku untuk run yang sedang berjalan. Lahir dari
    `57a04f1e`: empat berkas direncanakan, tiga terkirim, dan run VERSI 6
    berjalan dengan workflow lama sehingga `SHA256SUMS_KARANTINA` tidak terunggah.

## Kelas cacat

KC-1 s.d. KC-12 seperti pada v19. KC-10 dan KC-11 DITUTUP (v20). KC-13
(keterwakilan sampel) → penangkalnya aturan 37.

- **KC-14 [v21, dipersempit v22] — menit hilang NYATA di arsip 1m, hadir di
  KEDUA representasi.** **9** simbol-bulan, **6.375 menit** (425×15). Sebab
  tidak diketahui (H-A004, tak dapat diuji). Kebijakan: karantina (ADR-A006).
  Kesembilan berkasnya kini TERSIMPAN sebagai aset tar karantina.
- **KC-15 [v22] — berkas klines BULANAN dapat kehilangan HARI UTC penuh yang
  datanya utuh di berkas HARIAN.** **3** simbol-bulan, semuanya BNXUSDT 2022,
  **7.200 menit = 5×1440**. Kebijakan: ADR-A007 (pemulihan dari harian).
  Ketiga berkasnya kini TERSIMPAN — ini bahan baku pemulihannya.
- 9 + 3 = **12** karantina; 6.375 + 7.200 = **13.575** menit ✅
- **KC-16 DITARIK [v23] — nomornya TETAP kosong selamanya.**
- **KC-17 [v24] — parquet karantina tidak dipersistenkan meskipun diukur dan
  didaftar. DITUTUP [v25].** Sebab: pengemas hanya menerima `baris.get("parquet")`,
  sedangkan baris karantina menaruh jalurnya di `parquet_karantina`; 12 berkas,
  13.247.705 B hilang bersama runner. Perbaikan: `pecahan.py` VERSI 6 dengan
  pengemas kedua yang dibuat MALAS, `rilis.PengemasBerbelah(nama_sums=…)`, dan
  medan penggugur `cacah_karantina_tak_terkemas`. Bukti penutupan bukan
  keberadaan tar, melainkan `verifikasi_rilis_karantina` yang membaca ulang tiap
  tar, mencocokkan sha256, dan menemukan cacah anggota sama dengan cacah berkas
  yang dikemas pada keenam pecahan yang punya karantina (run `30396803601`).
  **Koreksi penomoran (aturan 29):** jurnal 59 menamainya KC-16; nomor itu
  terikat permanen pada tuduhan yang ditarik di v23.

## Hipotesis

- H-A001: belum diuji.
- H-A002a / H-A002b: H-A002b **GUGUR** (`slot_5m_hadir_saat_1m_hilang` = 0).
- **H-A003: MENANG pada 3, GUGUR pada 9.**
- **H-A004: TIDAK TERUJI dan tidak dapat diuji** (`fapi.binance.com` → 451).
- **H-A005: GUGUR pada rentang yang disampel [v23]** (37 bulan tengah).
- **H-A006 — serapan bersifat deterministik. MENANG, kini pada EMPAT run
  melintasi empat versi kode.** Run `30396803601` (VERSI 6) menghasilkan
  `jumlah_baris`, `byte_parquet_total`, cacah karantina, dan
  `nisbah_parquet_per_zip` yang identik byte demi byte dengan `30389402113`
  (VERSI 5), `30383278359` (VERSI 4, pecahan 1..7), dan `30353584831` (pecahan
  0). `sidik_data` tetap `6128fbb0…` di seluruhnya. Belum diuji pada rentang
  waktu panjang — arsip historis bisa saja direvisi kelak.

## Papan skor prediksi

R-1..R-120 dirinci v23: TEPAT 78, MELESET 28, SEPARUH 4, TIDAK TERADJUDIKASI 4,
MENUNGGU 6 = 120. R-121..R-138 di jurnal 56–58 dan tabel v24.

| # | Prediksi | Status |
|---|---|---|
| R-139 | karantina: nol tak terkemas, 12 anggota, 13.247.705 B, tiap tar < 5 MB | TEPAT (tar terbesar 4.433.920 B) |
| R-140 | 19.586 anggota utama; 19.586+12 = 19.598; `sah` ×8 | TEPAT |
| R-141 | nol perubahan angka serapan vs `30389402113` | TEPAT (baris, zip, parquet, menit hilang identik) |
| R-142 | `rilis_karantina` null tepat di P2 dan P5; `cacah_aset_tar` 4,4,3,3,4,3,4,4 = 29 | TEPAT |
| R-143 | CI 190 uji, kode 0 | TEPAT (run `30396875564`) |

**Total R-1..R-143** (aturan 21): TEPAT **96**; MELESET **32**; SEPARUH **5**;
TIDAK TERADJUDIKASI **4**; MENUNGGU **6** (R-7, R-19, R-20, R-28, R-36, R-37).
96+32+5+4+6 = **143** ✅ Ramalan berikutnya **R-144**. N_percobaan = 0.

Catatan kejujuran yang wajib dibaca bersama angka 96 itu: lima TEPAT terakhir
didaftarkan sebelum run, tetapi hanya R-139 dan R-141 yang benar-benar bisa
gugur oleh satu byte. R-142 dan R-143 berisiko rendah dan disebut begitu sejak
pendaftarannya. Rasio TEPAT yang menanjak di sini BUKAN tanda ramalan yang makin
baik; sebagian besar adalah pengulangan sistem yang sudah stabil.

## Daftar ADR

- ADR-A001 aturan dasar. DITERIMA.
- ADR-A002 serapan. DITERIMA; §3 DIAMANDEMEN oleh ADR-A004 lalu ADR-A007;
  §9 DIGANTI oleh ADR-A006 Keputusan 3.
- ADR-A003 taksonomi rezim. BELUM ADA (nomor dicadangkan).
- ADR-A004 kebijakan KC-6. DITERIMA; berdiri dengan enam klausa.
- ADR-A005 jenis instrumen tahap pertama. DITERIMA.
- **ADR-A006 karantina + persistensi. DITERIMA dan DITERAPKAN SEPENUHNYA** —
  data lolos dan data karantina keduanya bertahan sebagai aset rilis
  terverifikasi (`pecahan.py` VERSI 6, `rilis.py` dengan `nama_sums`, workflow
  v4). Sisa satu-satunya: pemulihan di luar runner belum pernah diuji.
- **ADR-A007 serapan hibrida. DIUSULKAN**, belum diterima, belum
  diimplementasikan. Bahan bakunya kini tersedia (3 tar BNXUSDT).
- ADR berikutnya **A008**.

## Serapan semesta `perpetual_usdt` — TERUKUR DAN TERPERSISTENSI UTUH

Sumber tunggal: run **`30396803601`**, commit `57a04f1e`, `versi_pecahan` **6**,
`sidik_kode` **`237ccf427faf9d48e9c0904433a56e8902de64de6552daee5d3053093bfba601`**,
`sidik_data` `6128fbb0…`, kode keluar 0 dan kode unggah 0 di kedelapan job.

| i | simbol | simbol-bulan | baris | menit hilang | karantina | nisbah | anggota utama | bagian utama | byte anggota | tar karantina | byte karantina |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 99 | 2.411 | 103.264.917 | 1.875 | 3 | 1,2295 | 2.408 | 3 | 4.120.562.805 | 1 | 3.286.672 |
| 1 | 99 | 2.468 | 105.765.980 | 2.160 | 3 | 1,2268 | 2.465 | 3 | 4.269.971.639 | 1 | 3.167.212 |
| 2 | 99 | 2.337 | 100.058.416 | 0 | 0 | 1,2293 | 2.337 | 3 | 3.834.773.373 | — | 0 |
| 3 | 98 | 2.154 | 91.884.319 | 615 | 1 | 1,2356 | 2.153 | 2 | 3.382.222.173 | 1 | 442.398 |
| 4 | 98 | 2.497 | 106.865.397 | 1.050 | 1 | 1,2327 | 2.496 | 3 | 4.199.469.659 | 1 | 837.910 |
| 5 | 98 | 2.741 | 117.671.896 | 0 | 0 | 1,2341 | 2.741 | 3 | 4.574.062.521 | — | 0 |
| 6 | 98 | 2.652 | 114.013.851 | 7.200 | 3 | 1,2399 | 2.649 | 3 | 4.449.859.316 | 1 | 4.420.728 |
| 7 | 98 | 2.338 | 100.317.358 | 675 | 1 | 1,2334 | 2.337 | 3 | 3.875.340.889 | 1 | 1.092.785 |

- Simbol **787**; simbol-bulan **19.598**; baris **839.842.134**; slot
  **839.855.709**; menit hilang **13.575**.
- Gerbang: lolos **19.586**, gagal **12**, `persen_lolos` **99,9388**.
- Zip **26.532.925.083 B**; parquet **32.706.262.375 B**; nisbah **1,2327**;
  parquet karantina **13.247.705 B**. Semuanya dijumlahkan ulang dari kedelapan
  log dan cocok sampai byte terakhir.
- Kelas risiko: pra_header 1.952, bulan_awal_2020_2021 1.889, terhenti 587,
  non_ascii **19** (9 di P0, 6 di P1, 4 di P2; kosong dan dinyatakan kosong di
  P3..P7 — aturan 37), kendali_baru 10.007.
- **`parquet_dipersistenkan: true` dan `karantina_dipersistenkan: true` di
  kedelapan laporan.** 19.586 anggota utama dalam **23** bagian tar; 12 anggota
  karantina dalam **6** bagian tar; total **29** aset tar. Tiap bagian dibaca
  ulang dengan sha256 cocok; `cacah_bagian_taksiran_terlampaui` 0,
  `cacah_berkas_hilang` 0, `cacah_parquet_tak_terkemas` 0,
  `cacah_karantina_tak_terkemas` 0.
- P2 dan P5 melaporkan `rilis_karantina: null` dan `karantina_dipersistenkan:
  true` dengan **penyebut nol** — itu bukan bukti pengemas karantina bekerja
  (aturan 30, 41). Buktinya ada pada enam pecahan lain.
- Tag rilis: `serapan-pecahan-<i>-30396803601`, aset `pecahan_<i>.partNN.tar`,
  `pecahan_<i>_karantina.part01.tar`, dan `SHA256SUMS`. Tag lama
  `…-30376241019` (tak sah), `…-30383278359` (tanpa P0), `…-30389402113` (sah,
  tanpa karantina) masih ada.
- **Cacat unggah run ini (aturan 45):** `SHA256SUMS_KARANTINA` TIDAK terunggah
  karena workflow v4 baru mendarat setelah run menyala. Sidik keenam tar
  karantina tercatat di `journal/2026-07-29-61.md` dan di
  `reports/manifes_pecahan_<i>.json`, jadi dapat diverifikasi dari git. Berlaku
  otomatis mulai run berikutnya.
- **Batas kesahihan yang tersisa — satu-satunya, dan besar:** aset rilis belum
  pernah diunduh dan dibongkar di luar runner yang menulisnya. `kode_unggah` 0
  hanya berarti perintah `gh` pulang tanpa galat.

## Model ukuran tar — tiga ronde, satu sebab

`rilis.py` menaksir tiap anggota sebagai `KEPALA_ANGGOTA + blok_isi×512`.
Ronde 1 dan 2 memakai kepala 512 B dan gagal di produksi; sebabnya **header pax
1.024 B per anggota** yang ditulis `tarfile` Python ≥3.8 ketika sebuah medan
(misalnya `mtime` pecahan) tidak muat di header ustar. Dengan
`KEPALA_ANGGOTA = 1536` sisa taksiran runtuh ke nol atau tepat ke margin pada
seluruh 29 bagian, termasuk keenam tar karantina yang bercacah anggota sangat
kecil (1 atau 3) — di sana `nisbah_bagian_per_anggota` naik sampai 1,0184 dan
tetap tidak melampaui taksiran. Konstanta: `BATAS_BAGIAN` 1.800.000.000,
`BLOK_TAR` 512, `BLOK_PAX` 1024, `REKAM_TAR` 10240, `MARGIN_REKAM` 20480.

## Jumlah uji

**190 TERVERIFIKASI** — `reports/ci_terakhir.json` run `30396875564`, commit
`5de57a2b`, `kode_keluar` 0. Termasuk 17 uji `tests/test_rilis.py` dan 3 uji
`tests/test_rilis_karantina.py`.

## Utang verifikasi

1-5 dan 11 menunggu tahap juri/klasifikasi. 6-23, 25-28 LUNAS.

24. **AKTIF, sebagian besar LUNAS.**
    - **persistensi data lolos: LUNAS** (run `30389402113`, diulang `30396803601`);
    - **persistensi karantina: LUNAS** (run `30396803601`, KC-17 ditutup);
    - **pemulihan aset di luar runner: BELUM — kini utang tunggal terbesar;**
    - jalur **funding** (`funding_ada` null di seluruh manifes);
    - medan `dugaan_pengganti` (ADR-A005);
    - pemulihan harian ADR-A007 (`sumber_baris`, `cacah_baris_dipulihkan`);
    - karantina artefak 7 hari.
    Mengadjudikasi R-7, R-19, R-20, R-28, R-36, R-37.

## Temuan sampingan yang belum diukur

- Jalur funding: nol kali diuji.
- 15 `SETTLED` lain: apakah punya pendahulu seperti SXPUSDT?
- Daftar `INDEKS` hanya tiga nama, disusun manual.
- Saham dan komoditas token masih terhitung `perpetual_usdt`.
- `.decode("utf-8","replace")` di `klines` membungkam byte rusak.
- Apakah BUSD/USDC layak digabung dengan USDT.
- Sisa 16 simbol non-ASCII belum diuji langsung (3 sudah).
- Sebab KC-14 (H-A004) — tidak dapat diuji. **Sebab KC-15 tidak diketahui.**
- Selisih penyebut diagnosa KC-15: 38 diperiksa, 41 dirancang. Cacat pelaporan.
- `waktu_utc` pada laporan runner berjalan lebih dulu daripada jam sesi; belum
  diselidiki, belum layak disebut cacat.
