# STATE — versi 26

Diperbarui: 2026-07-29 (sesi 53). Aturan hanya BERTAMBAH; jangan menulis ulang
dari ingatan. v26 disusun di atas teks v25 yang dibaca langsung dari `main`
(blob `73b0cc88`), ditambah kedelapan laporan run pemulihan **`30404071324`**.

Peristiwa terbesar sejak v25: **semesta terbukti bisa DIAMBIL KEMBALI.** v25
ditutup dengan satu batas kesahihan yang besar — seluruh klaim persistensi
berasal dari runner yang menulis tar itu sendiri. Batas itu hilang. 29 aset,
19.598 anggota, 839.842.134 baris diunduh ulang oleh mesin lain, dicocokkan
terhadap sidik di git, dibongkar, dan dibaca. Nol byte berubah.

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
    uji. Lahir dari selisih 135 lawan **141**; dilanggar lagi pada R-148
    (198 lawan **201**) karena saya mencacah FUNGSI uji, bukan butir yang
    dikumpulkan pytest — satu fungsi berparameter empat kasus bernilai 4 butir.
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
    R-131.
45. **[v25] Keatomikan push pemicu.** Sebuah push yang MENYALAKAN run wajib
    memuat setiap berkas yang run itu bergantung padanya, dan daftar berkas itu
    wajib dihitung ulang tepat sebelum dikirim. GitHub Actions memakai berkas
    workflow pada commit PEMICU, sehingga perbaikan workflow yang menyusul di
    commit berikutnya TIDAK berlaku untuk run yang sedang berjalan. Lahir dari
    `57a04f1e`. **Ditaati pada `ab4e0774`** — modul, workflow, dan uji dalam satu
    commit; run pemulihan berjalan dengan workflow yang benar sejak detik nol.
46. **[v26] Kode dilarang menyimpulkan dari penyebut nol.** Medan yang
    MENYIMPULKAN sebuah definisi atau sebab wajib memeriksa lebih dulu apakah
    kasusnya mampu membedakan. Bila penyebutnya nol, atau bila kedua kemungkinan
    menghasilkan angka yang sama, medan itu wajib berbunyi "tidak dapat
    dibedakan", bukan menyebut salah satu. Aturan 30 dan 41 melarang AGEN
    menyimpulkan dari penyebut nol; aturan ini melarang KODE melakukannya.
    Lahir dari `pulihkan.py` VERSI 1, yang pada pecahan 2 dan 5 (tanpa
    karantina) mencetak `definisi_jumlah_baris` = "baris lolos saja" padahal
    kedua definisi menghasilkan angka identik di sana. Belum diperbaiki di kode.

## Kelas cacat

KC-1 s.d. KC-12 seperti pada v19. KC-10 dan KC-11 DITUTUP (v20). KC-13
(keterwakilan sampel) → penangkalnya aturan 37.

- **KC-14 [v21, dipersempit v22] — menit hilang NYATA di arsip 1m, hadir di
  KEDUA representasi.** **9** simbol-bulan, **6.375 menit** (425×15). Sebab
  tidak diketahui (H-A004, tak dapat diuji). Kebijakan: karantina (ADR-A006).
  Kesembilan berkasnya tersimpan sebagai aset tar karantina **dan kini terbukti
  dapat diunduh ulang serta dibaca** (run `30404071324`).
- **KC-15 [v22] — berkas klines BULANAN dapat kehilangan HARI UTC penuh yang
  datanya utuh di berkas HARIAN.** **3** simbol-bulan, semuanya BNXUSDT 2022,
  **7.200 menit = 5×1440**. Kebijakan: ADR-A007. Ketiga berkasnya tersimpan dan
  terbukti dapat dipulihkan — bahan baku ADR-A007 kini ada di tangan.
- 9 + 3 = **12** karantina; 6.375 + 7.200 = **13.575** menit ✅ Keduabelasnya
  memuat **516.135 baris**, terbaca ulang dari luar runner.
- **KC-16 DITARIK [v23] — nomornya TETAP kosong selamanya.**
- **KC-17 [v24] — parquet karantina tidak dipersistenkan meskipun diukur dan
  didaftar. DITUTUP [v25], dan penutupannya diperkuat [v26]** oleh pembacaan
  ulang keenam tar karantina dari luar runner: sha256 cocok, 12 anggota,
  516.135 baris.

## Hipotesis

- H-A001: belum diuji.
- H-A002a / H-A002b: H-A002b **GUGUR** (`slot_5m_hadir_saat_1m_hilang` = 0).
- **H-A003: MENANG pada 3, GUGUR pada 9.**
- **H-A004: TIDAK TERUJI dan tidak dapat diuji** (`fapi.binance.com` → 451).
- **H-A005: GUGUR pada rentang yang disampel [v23]** (37 bulan tengah).
- **H-A006 — serapan bersifat deterministik. MENANG pada EMPAT run melintasi
  empat versi kode.** Belum diuji pada rentang waktu panjang.
- **H-A008 [v26] — aset rilis GitHub mengembalikan byte yang sama persis dengan
  yang diunggah. MENANG pada satu kali pengambilan**, 29 aset, 32.754.749.440
  byte tar, nol sha tak cocok. Rentangnya sempit dan wajib disebut: satu
  pengambilan, satu waktu, umur aset kurang dari sehari. Ia tidak mengatakan
  apa pun tentang ketahanan berbulan-bulan.

## Papan skor prediksi

R-1..R-120 dirinci v23. R-121..R-143 di jurnal 56–61 dan tabel v25.

| # | Prediksi | Status |
|---|---|---|
| R-144 | `pulih_sah` ×8; nol sha tak cocok dan nol bagian hilang atas 29 aset | TEPAT |
| R-145 | anggota utama 19.586 dan karantina 12, terpecah persis per pecahan | TEPAT |
| R-146 | `jumlah_baris` mencacah baris lolos gerbang saja | **MELESET** |
| R-147 | ketiadaan `SHA256SUMS_KARANTINA` tidak mempengaruhi putusan | TEPAT (risiko rendah, disebut sejak pendaftaran) |
| R-148 | CI melaporkan 198 uji | **MELESET** (dikoreksi di jurnal 63 sebelum laporannya mendarat) |
| R-149 | CI melaporkan 201 uji, kode 0 | TEPAT (run `30404071399`) |

**Total R-1..R-149** (aturan 21): TEPAT **100**; MELESET **34**; SEPARUH **5**;
TIDAK TERADJUDIKASI **4**; MENUNGGU **6** (R-7, R-19, R-20, R-28, R-36, R-37).
100+34+5+4+6 = **149** ✅ Ramalan berikutnya **R-150**. N_percobaan = 0.

Catatan kejujuran: kedua MELESET hari ini adalah kesalahan aritmetika saya atas
hal yang bisa saya BACA — skema manifes dan cara pytest mencacah butir — bukan
kejutan dari dunia. R-144 adalah satu-satunya TEPAT hari ini yang benar-benar
bisa digugurkan oleh satu byte.

## Definisi `jumlah_baris` — TERSELESAIKAN [v26]

**`jumlah_baris` di manifes = baris lolos gerbang + baris karantina.** Terbukti
pada keenam pecahan yang punya karantina: `selisih_baris_total` = 0 dan
`selisih_baris_utama` = −(baris karantina). Pecahan 2 dan 5 tidak dapat
membedakan (aturan 46).

- Baris lolos gerbang saja: **839.325.999**
- Baris karantina: **516.135**
- Jumlah: **839.842.134** = angka semesta.

Konsekuensi untuk ADR-A007: 839.842.134 SUDAH memuat 516.135 baris cacat. Baris
hasil pemulihan harian tidak boleh dijumlahkan ke angka itu tanpa lebih dulu
mengurangi baris karantina yang digantikannya, atau semesta akan tercacah ganda.

## Serapan semesta `perpetual_usdt` — TERUKUR, TERPERSISTENSI, TERPULIHKAN

Sumber serapan: run **`30396803601`**, commit `57a04f1e`, `versi_pecahan` **6**,
`sidik_kode` **`237ccf42…`**, `sidik_data` `6128fbb0…`.
Sumber pemulihan: run **`30404071324`**, commit `ab4e0774`, `versi_pulihkan` 1,
`sidik_kode` **`c76ff896f39c9d979ac875fe2e7b54b050911f49bd361150f3826a99ea272b38`**.

| i | simbol | simbol-bulan | baris (total) | baris lolos | baris karantina | menit hilang | anggota utama | bagian | tar kar | byte terunduh |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 99 | 2.411 | 103.264.917 | 103.134.312 | 130.605 | 1.875 | 2.408 | 3 | 1 | 4.128.204.800 |
| 1 | 99 | 2.468 | 105.765.980 | 105.634.220 | 131.760 | 2.160 | 2.465 | 3 | 1 | 4.277.565.440 |
| 2 | 99 | 2.337 | 100.058.416 | 100.058.416 | 0 | 0 | 2.337 | 3 | — | 3.838.976.000 |
| 3 | 98 | 2.154 | 91.884.319 | 91.841.734 | 42.585 | 615 | 2.153 | 2 | 1 | 3.386.542.080 |
| 4 | 98 | 2.497 | 106.865.397 | 106.821.807 | 43.590 | 1.050 | 2.496 | 3 | 1 | 4.204.800.000 |
| 5 | 98 | 2.741 | 117.671.896 | 117.671.896 | 0 | 0 | 2.741 | 3 | — | 4.578.979.840 |
| 6 | 98 | 2.652 | 114.013.851 | 113.890.221 | 123.630 | 7.200 | 2.649 | 3 | 1 | 4.459.048.960 |
| 7 | 98 | 2.338 | 100.317.358 | 100.273.393 | 43.965 | 675 | 2.337 | 3 | 1 | 3.880.632.320 |

- Simbol **787**; simbol-bulan **19.598**; baris **839.842.134**; slot
  **839.855.709**; menit hilang **13.575**.
- Gerbang: lolos **19.586**, gagal **12**, `persen_lolos` **99,9388**.
- Zip **26.532.925.083 B**; parquet **32.706.262.375 B**; nisbah **1,2327**;
  parquet karantina **13.247.705 B**.
- Kelas risiko: pra_header 1.952, bulan_awal_2020_2021 1.889, terhenti 587,
  non_ascii **19** (9 di P0, 6 di P1, 4 di P2; kosong dan dinyatakan kosong di
  P3..P7 — aturan 37), kendali_baru 10.007.
- **Pemulihan (run `30404071324`):** 29/29 aset hadir, 29/29 sha cocok, 0 bagian
  hilang, 0 anggota kurang, **0 anggota tak aman** (tak ada jalur mutlak atau
  `..`), 19.586+12 anggota terbaca, 839.842.134 baris terbaca ulang oleh pyarrow.
  Byte tar terunduh **32.754.749.440**; selisihnya terhadap muatan parquet
  (35.185.305 utama, 54.055 karantina) adalah kepala tar dan bantalan, sesuai
  model `KEPALA_ANGGOTA` 1.536.
- Sidik pembanding diambil dari `reports/manifes_pecahan_<i>.json` **di git**,
  BUKAN dari `SHA256SUMS` di rilis. Memeriksa aset rilis dengan berkas sidik
  yang diunggah proses yang sama hanya membuktikan rilis konsisten dengan
  dirinya sendiri.
- Tag rilis: `serapan-pecahan-<i>-30396803601`. Tag lama `…-30376241019` (tak
  sah), `…-30383278359` (tanpa P0), `…-30389402113` (tanpa karantina) masih ada.
- `SHA256SUMS_KARANTINA` tetap tidak ada pada tag `…-30396803601` (aturan 45);
  terbukti tidak mempengaruhi putusan apa pun karena pemulihan tidak memakainya.

## Model ukuran tar — tiga ronde, satu sebab

`rilis.py` menaksir tiap anggota sebagai `KEPALA_ANGGOTA + blok_isi×512`.
Ronde 1 dan 2 memakai kepala 512 B dan gagal di produksi; sebabnya **header pax
1.024 B per anggota**. Dengan `KEPALA_ANGGOTA = 1536` sisa taksiran runtuh ke
nol atau tepat ke margin pada seluruh 29 bagian. Konstanta: `BATAS_BAGIAN`
1.800.000.000, `BLOK_TAR` 512, `BLOK_PAX` 1024, `REKAM_TAR` 10240,
`MARGIN_REKAM` 20480. Bagian terbesar yang benar-benar terunduh: 1.799.792.640 B
— di bawah batas.

## Jumlah uji

**201 TERVERIFIKASI** — `reports/ci_terakhir.json` run `30404071399`, commit
`ab4e0774`, `kode_keluar` 0. Termasuk 17 uji `tests/test_rilis.py`, 3 uji
`tests/test_rilis_karantina.py`, dan 11 butir `tests/test_pulihkan.py`
(8 fungsi, satu di antaranya berparameter empat kasus).

## Utang verifikasi

1-5 dan 11 menunggu tahap juri/klasifikasi. 6-23, 25-28 LUNAS.

24. **AKTIF, menyusut tajam.**
    - persistensi data lolos: **LUNAS**;
    - persistensi karantina: **LUNAS** (KC-17 ditutup);
    - **pemulihan aset di luar runner: LUNAS** (run `30404071324`) — batas
      kesahihannya: satu pengambilan, aset berumur kurang dari sehari;
    - jalur **funding** (`funding_ada` null di seluruh manifes) — BELUM, kini
      utang tunggal terbesar;
    - medan `dugaan_pengganti` (ADR-A005) — BELUM;
    - pemulihan harian ADR-A007 (`sumber_baris`, `cacah_baris_dipulihkan`,
      `cacah_hari_dipulihkan`, `cacah_simbol_bulan_dipulihkan`, tripwire
      `cacah_pemulihan_gagal_checksum` = 0) — BELUM, bahan baku sudah ada;
    - karantina artefak 7 hari — BELUM;
    - perbaikan aturan 46 di `pulihkan.py` — BELUM.
    Mengadjudikasi R-7, R-19, R-20, R-28, R-36, R-37.

## Daftar ADR

- ADR-A001 aturan dasar. DITERIMA.
- ADR-A002 serapan. DITERIMA; §3 DIAMANDEMEN oleh ADR-A004 lalu ADR-A007;
  §9 DIGANTI oleh ADR-A006 Keputusan 3.
- ADR-A003 taksonomi rezim. BELUM ADA (nomor dicadangkan).
- ADR-A004 kebijakan KC-6. DITERIMA.
- ADR-A005 jenis instrumen tahap pertama. DITERIMA.
- **ADR-A006 karantina + persistensi. DITERIMA, DITERAPKAN, dan kini
  TERVERIFIKASI DARI LUAR.** Tidak ada sisa terbuka.
- **ADR-A007 serapan hibrida. DIUSULKAN**, belum diterima, belum
  diimplementasikan. Wajib memperhitungkan temuan `jumlah_baris` di atas.
- ADR berikutnya **A008**.

## Temuan sampingan yang belum diukur

- Jalur funding: nol kali diuji.
- 15 `SETTLED` lain: apakah punya pendahulu seperti SXPUSDT?
- Daftar `INDEKS` hanya tiga nama, disusun manual.
- Saham dan komoditas token masih terhitung `perpetual_usdt`.
- `.decode("utf-8","replace")` di `klines` membungkam byte rusak.
- Apakah BUSD/USDC layak digabung dengan USDT.
- Sisa 16 simbol non-ASCII belum diuji langsung (3 sudah).
- Sebab KC-14 (H-A004) tidak dapat diuji. **Sebab KC-15 tidak diketahui.**
- Selisih penyebut diagnosa KC-15: 38 diperiksa, 41 dirancang. Cacat pelaporan.
- `waktu_utc` runner berjalan lebih dulu daripada jam sesi; masih belum
  diselidiki, masih belum layak disebut cacat.
