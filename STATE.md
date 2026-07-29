# STATE — versi 27

Diperbarui: 2026-07-29 (sesi 54). Aturan hanya BERTAMBAH; jangan menulis ulang
dari ingatan. v27 disusun di atas teks v26 yang dibaca langsung dari `main`
(blob `c07d5e58`), ditambah teks aturan 47–52 yang dibaca verbatim dari jurnal
69, 71, 72, 73, dan 75, ditambah laporan run `30416845475` (kohort ekor V4),
`30416988938` (ukur_baris V1), dan `30416988936` (CI 244).

Peristiwa terbesar sejak v26: **kohort funding terbukti mati lebih dulu daripada
fundingnya.** Kesepuluh anggota yang disampel berhenti diperdagangkan antara
2024-06 dan 2025-04 — sembilan bulan berbeda, tersebar — sementara penerbitan
funding berhenti serempak pada 2025-07. Bersamaan dengan itu lahir KC-18: arsip
menerbitkan klines yang sempurna secara BENTUK untuk pasar yang tidak
diperdagangkan.

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
    sebagai kelas. Lahir dari KC-16 yang ditarik. **Ditaati pada KC-18**, yang
    baru dinamai di jurnal 74 sesudah kendali positif membuktikan alat ukurnya
    melihat.
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
    `57a04f1e`. Ditaati pada `ab4e0774`, `387037a9`, dan `796c2fc4`.
46. **[v26] Kode dilarang menyimpulkan dari penyebut nol.** Medan yang
    MENYIMPULKAN sebuah definisi atau sebab wajib memeriksa lebih dulu apakah
    kasusnya mampu membedakan. Bila penyebutnya nol, atau bila kedua kemungkinan
    menghasilkan angka yang sama, medan itu wajib berbunyi "tidak dapat
    dibedakan", bukan menyebut salah satu. Aturan 30 dan 41 melarang AGEN
    menyimpulkan dari penyebut nol; aturan ini melarang KODE melakukannya.
    Lahir dari `pulihkan.py` VERSI 1, yang pada pecahan 2 dan 5 (tanpa
    karantina) mencetak `definisi_jumlah_baris` = "baris lolos saja" padahal
    kedua definisi menghasilkan angka identik di sana. **Belum diperbaiki di
    kode**; namun sudah DITAATI di modul baru — `kohort_ekor` V4 menerbitkan
    `bangkit_dapat_diuji` alih-alih membiarkan `bangkit_kembali` false terbaca
    sebagai bukti.
47. **[v27, lahir di jurnal 69]** Sebelum menulis ramalan berupa cacah,
    sebutkan satuannya secara eksplisit — simbol, bulan, simbol-bulan, baris,
    atau butir uji — dan periksa bahwa angka rujukan yang dipakai memang
    bersatuan itu. Lahir dari R-163: saya mencacah baris "2025-07" pada daftar
    terpotong (satuan SIMBOL-BULAN) lalu memakainya sebagai taksiran cacah
    SIMBOL, sehingga pita 100..400 lahir untuk angka yang sebenarnya 38. Ini
    kelas kesalahan yang sama dengan R-148 (fungsi uji lawan butir pytest).
48. **[v27, lahir di jurnal 71]** Berkas modul yang mendekati pagar 800 baris
    harus dipecah SEBELUM fungsi baru ditambahkan, dan setiap pemecahan wajib
    memperluas daftar berkas yang masuk `sidik_kode`. Memindahkan kode ke berkas
    yang tidak ikut dicap membuat sidik kode menyempit diam-diam, sehingga dua
    versi kode yang berbeda dapat memberi sidik yang sama — kebalikan dari
    gunanya.
49. **[v27, lahir di jurnal 72]** Pemecahan berkas yang mempertahankan seluruh
    nama fungsi lewat re-export TETAP dapat mematahkan uji, karena re-export
    memindahkan fungsi dan bukan modul. Sebelum mendorong pemecahan, telusuri
    bukan hanya nama yang DIPANGGIL uji, melainkan juga nama yang DITAMBAL
    (`monkeypatch.setattr`, `patch`, akses atribut modul). Bila sebuah uji
    menambal atribut modul, tambalan harus menunjuk modul pemilik kode yang
    baru, dan panggilannya sebaiknya tetap lewat modul lama agar re-export itu
    sendiri ikut teruji.
50. **[v27, lahir di jurnal 73]** Setiap pengukuran yang menyimpulkan dari
    KETIADAAN — volume nol, berkas hilang, baris kosong, jawaban 404 — wajib
    memuat kendali positif yang membuktikan alat ukurnya mampu mendeteksi
    KEHADIRAN pada kondisi yang sama. Tanpa kendali positif, angka nol tidak
    dapat dibedakan dari alat yang buta, dan laporannya harus dianggap batal,
    bukan sekadar lemah.
51. **[v27, lahir di jurnal 75]** Jendela pemindaian mundur wajib adaptif, atau
    dibuktikan mencakup peristiwa yang dicari. Jendela tetap yang seluruh isinya
    sepi menghasilkan null, bukan jawaban; dan null yang tidak diberi medan
    penggugur akan terbaca sebagai nol. **Ditaati pada kohort_ekor V4**, yang
    mundur sampai bulan ramai pertama dengan pagu keras 60 bulan.
52. **[v27, lahir di jurnal 75]** Laporan yang tidak dapat dibaca utuh setara
    dengan laporan yang tidak ada. Setiap pelapor besar wajib berpasangan dengan
    keluaran ringkas yang memuat sidik berkas sumbernya, supaya ringkasan
    terbukti berasal dari run yang itu juga dan bukan sisa run lama. Ditaati
    oleh `kohort_ringkas` (`sidik_sumber`) dan `ukur_baris`.

## Kelas cacat

KC-1 s.d. KC-12 seperti pada v19. KC-10 dan KC-11 DITUTUP (v20). KC-13
(keterwakilan sampel) → penangkalnya aturan 37.

- **KC-14 [v21, dipersempit v22] — menit hilang NYATA di arsip 1m, hadir di
  KEDUA representasi.** **9** simbol-bulan, **6.375 menit** (425×15). Sebab
  tidak diketahui (H-A004, tak dapat diuji). Kebijakan: karantina (ADR-A006).
- **KC-15 [v22] — berkas klines BULANAN dapat kehilangan HARI UTC penuh yang
  datanya utuh di berkas HARIAN.** **3** simbol-bulan, semuanya BNXUSDT 2022,
  **7.200 menit = 5×1440**. Kebijakan: ADR-A007. Sebab masih tidak diketahui.
- 9 + 3 = **12** karantina; 6.375 + 7.200 = **13.575** menit ✅ Keduabelasnya
  memuat **516.135 baris**, terbaca ulang dari luar runner.
- **KC-16 DITARIK [v23] — nomornya TETAP kosong selamanya.**
- **KC-17 [v24] — parquet karantina tidak dipersistenkan. DITUTUP [v25],
  diperkuat [v26]** oleh pembacaan ulang keenam tar karantina dari luar runner.
- **KC-18 [v27, dinamai di jurnal 74] — lilin datar lolos gerbang struktural.**
  Arsip menerbitkan berkas klines 1m lengkap dan sah secara bentuk untuk pasar
  yang tidak diperdagangkan: 43.200 lilin, stempel waktu rapat tanpa menit
  hilang, checksum cocok, namun `volume` dan `count` nol pada SELURUH lilin.
  Gerbang 1m meloloskannya karena gerbang menilai BENTUK deret, bukan KEHIDUPAN
  pasar. Baris semacam ini terhitung sebagai baris sah di semesta.
  - Bentangan terukur jurnal 74: **864.000 lilin** pada 20 simbol-bulan
    (20 × 43.200), seluruhnya lolos gerbang.
  - Bentangan terukur jurnal 77: **169 simbol-bulan sepi** dari 179 yang
    diunduh pada 10 simbol, seluruhnya lolos gerbang.
  - Aturan 20: JANGAN diekstrapolasi ke 456 simbol-bulan kohort. Bentangan
    penuh belum diukur.
  - Kebijakannya belum diputuskan; ADR-A008 akan menanganinya. Lilin datar bukan
    data palsu, ia keterangan sah bahwa tidak ada perdagangan. Bahayanya adalah
    bila ia diam-diam ikut menjadi PENYEBUT dalam ukuran apa pun.

## Hipotesis

- H-A001: belum diuji.
- H-A002a / H-A002b: H-A002b **GUGUR** (`slot_5m_hadir_saat_1m_hilang` = 0).
- **H-A003: MENANG pada 3, GUGUR pada 9.**
- **H-A004: TIDAK TERUJI dan tidak dapat diuji** (`fapi.binance.com` → 451).
- **H-A005: GUGUR pada rentang yang disampel [v23]** (37 bulan tengah).
- **H-A006 — serapan bersifat deterministik. MENANG pada ENAM run melintasi enam
  versi kode** (`sidik_data` `6128fbb0…` tak bergeser). Ia hanya menyatakan angka
  stabil terhadap penataan ulang kode; ia tidak mengatakan apa pun tentang
  kebenaran angka itu terhadap dunia.
- **H-A008 [v26] — aset rilis GitHub mengembalikan byte yang sama persis.
  MENANG pada satu kali pengambilan**, 29 aset, 32.754.749.440 byte tar. Rentang
  sempit: satu pengambilan, umur aset kurang dari sehari.

## Papan skor prediksi

R-1..R-120 dirinci v23. R-121..R-149 di v26 dan jurnal 56–63. R-150..R-193 di
jurnal 64–75. R-194..R-197 di jurnal 76 dan 77.

| # | Prediksi | Status |
|---|---|---|
| R-175 | kedua berkas ≤800 baris DAN `funding.py` pita 500..680 | **SEPARUH** |
| R-179 | `funding.py` 640..700 DAN `funding_cdn.py` 140..200 | **SEPARUH** |
| R-194 | `cacah_simbol_batas_tercapai` jadi 0 | TEPAT |
| R-195 | kesepuluh `bulan_hidup_terakhir` sebelum 2025-07 | TEPAT |
| R-196 | CI 241 butir, kode 0 | TEPAT |
| R-197 | CI 244 butir, kode 0 | TEPAT |

**Total R-1..R-197** (aturan 21): TEPAT **138**; MELESET **37**; SEPARUH **11**;
TIDAK TERADJUDIKASI **5**; MENUNGGU **6** (R-7, R-19, R-20, R-28, R-36, R-37).
138+37+11+5+6 = **197** ✅ Ramalan berikutnya **R-198**. N_percobaan = 0.

Catatan kejujuran: R-175 dan R-179 sama-sama SEPARUH karena saya dua kali
menaksir panjang `funding.py` terlalu pendek dari ukuran byte (28.121 B / 705
baris = 39,9 B per baris, sedangkan taksiran saya memakai sekitar 43). Pita
kedua justru dinaikkan untuk memperbaiki yang pertama, dan MASIH terlalu rendah.
Tidak ada pita yang disetel ulang sesudah angkanya terlihat.

## Cacah baris terukur — TERSELESAIKAN [v27]

Sumber: `reports/ukur_baris.json`, run **30416988938**, commit `796c2fc4`,
kode 0. Penggugur bersih: `cacah_berkas_hilang` 0,
`cacah_berkas_melebihi_pagar` 0, `cacah_berkas_ada` 8 dari 8.
Definisi: `len(teks.splitlines())`, PERSIS definisi pagar 800 di
`tests/test_kontinuitas.py`.

| berkas | baris | byte |
| --- | --- | --- |
| `funding.py` | **705** | 28.121 |
| `funding_cdn.py` | **162** | 6.335 |
| `arsip.py` | 154 | 5.231 |
| `gerbang_1m.py` | 184 | 6.775 |
| `kohort_ekor.py` | 553 | 22.590 |
| `kohort_ringkas.py` | 82 | 2.882 |
| `pulihkan.py` | 318 | 11.801 |
| `resample.py` | 127 | 4.356 |

Total 2.285 baris; terbesar `funding.py` 705 — 95 baris di bawah pagar 800.
Aturan 48 berlaku: ia sudah dekat, dan fungsi baru DILARANG ditambahkan ke sana
sebelum dipecah.

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
  non_ascii **19**, kendali_baru 10.007.
- **Pemulihan (run `30404071324`):** 29/29 aset hadir, 29/29 sha cocok, 0 bagian
  hilang, 0 anggota tak aman, 839.842.134 baris terbaca ulang oleh pyarrow.
- Sidik pembanding diambil dari `reports/manifes_pecahan_<i>.json` **di git**,
  BUKAN dari `SHA256SUMS` di rilis.
- Tag rilis: `serapan-pecahan-<i>-30396803601`.

## Funding semesta — TERUKUR (`funding.py` V6)

Run FUNDING 6 `30412188715`, commit `ba37c5d5`, kode 0.
`sidik_kode` `d3854823…`, `sidik_data` `6128fbb0…` (tak berubah sejak V1).

- 880 bulan klines tanpa funding; 87 funding tanpa klines; penyebut 19.598.
- Bentuk lubang: {awal 48, ekor 826, tengah 6, hilang 880}. 116 simbol berlubang
  ekor (14,74% dari 787).
- **Kohort puncak 2025-07: 38 simbol, 456 simbol-bulan**, `seri` false; 456 =
  51,8% dari seluruh 880 lubang. Ke-38 anggota punya bulan klines terakhir
  2026-06 (`seragam_bulan_klines_terakhir` true, `cacah_tanpa_bulan_terakhir` 0).
- `uji_cdn`: 10 kohort menjawab **404**, 10 kendali menjawab **200** dengan
  checksum cocok, byte kendali 529–1.939. Listing tidak berbohong: berkasnya
  memang tidak diterbitkan.

## Kohort ekor — kematian bertahap lawan tebing serempak [v27]

Modul `lux_ai/serapan/kohort_ekor.py`, VERSI 1→4, dan pelapor ringkas
`lux_ai/serapan/kohort_ringkas.py` V1 (aturan 52).

- V1 (`cba838ee…`): 20 simbol-bulan seluruhnya bervolume nol — tetapi tanpa
  kendali positif, jadi tak dapat ditafsirkan (aturan 50 lahir di sini).
- V2 (`35cddef9…`): kendali hidup BTCUSDT dan ETHUSDT ramai pada 4 dari 4 baris,
  `parser_terbukti` true. KC-18 dinamai sesudah ini.
- V3 (`9ca1464f…`): jendela TETAP 15 bulan; `batas_tercapai` menyala pada 9 dari
  10 simbol — jendela buta (aturan 51 lahir di sini).
- **V4 (`73ca4eb2a4473a8bc52da5fb7d0cb2c1aa96b726d8878d0512efc4f0980fcdca`),
  run `30416845475`, commit `387037a9`, kode 0**: pindaian ADAPTIF, pagu keras
  60 bulan. `cacah_simbol_batas_tercapai` 0, `cacah_simbol_pagu_habis` 0,
  `cacah_simbol_arsip_habis` 0 — pagu tak pernah tersentuh (pindaian terpanjang
  25 bulan). 179 simbol-bulan diunduh + 4 kendali hidup = 183 baris.

| simbol | bulan hidup terakhir | simbol | bulan hidup terakhir |
| --- | --- | --- | --- |
| AGIXUSDT | 2024-06 | BLZUSDT | 2024-12 |
| ALPACAUSDT | 2025-04 | BNXUSDT | 2025-03 |
| AMBUSDT | 2025-02 | BONDUSDT | 2024-11 |
| BADGERUSDT | 2025-03 | COMBOUSDT | 2025-03 |
| BALUSDT | 2025-03 | DARUSDT | 2024-12 |

Kesepuluhnya berhenti SEBELUM tebing funding 2025-07, tersebar pada sembilan
bulan berbeda. Tebing funding karena itu lebih menyerupai perubahan rezim
PENERBITAN ketimbang peristiwa pasar.

Yang TIDAK dibuktikan: (a) ini 10 dari 38 anggota, sampel SISTEMATIS menurut
abjad, aturan 20 melarang menyimpulkan tentang 28 sisanya; (b)
`cacah_simbol_bangkit_dapat_diuji` **0**, jadi `bangkit_kembali` 0 bukan bukti
(aturan 46); (c) arsip funding TIDAK terbukti cacat — penghentian penerbitan
yang tertunda sama-sama muat, dan **ADR-A002 §10 tidak boleh diubah atas bukti
kohort semata**.

## Jumlah uji

**244 TERVERIFIKASI** — `reports/ci_terakhir.json` run `30416988936`, commit
`796c2fc4`, `kode_keluar` 0, "244 tests collected in 0.39s". Riwayat mutakhir:
231 (V1) → 234 (V2) → 236 (V3) → 239 (ringkas) → 241 (V4) → **244**
(`tests/test_ukur_baris.py`, 3 fungsi).

## Utang verifikasi

1-5 dan 11 menunggu tahap juri/klasifikasi. 6-23, 25-28 LUNAS.

24. **AKTIF.**
    - persistensi data lolos dan karantina: **LUNAS**;
    - pemulihan aset di luar runner: **LUNAS** (run `30404071324`);
    - jalur **funding**: TERUKUR di tingkat listing dan CDN, tetapi
      `funding_ada` masih null di seluruh manifes — BELUM;
    - medan `dugaan_pengganti` (ADR-A005) — BELUM;
    - pemulihan harian ADR-A007 — BELUM, bahan baku sudah ada;
    - karantina artefak 7 hari — BELUM;
    - perbaikan aturan 46 di `pulihkan.py` — BELUM;
    - bentangan penuh KC-18 atas 456 simbol-bulan — BELUM;
    - 28 anggota kohort yang belum disampel — BELUM.
    Mengadjudikasi R-7, R-19, R-20, R-28, R-36, R-37.

## Daftar ADR

- ADR-A001 aturan dasar. DITERIMA.
- ADR-A002 serapan. DITERIMA; §3 DIAMANDEMEN oleh ADR-A004 lalu ADR-A007;
  §9 DIGANTI oleh ADR-A006 Keputusan 3. **§10 belum disentuh dan tidak boleh
  disentuh atas bukti kohort semata.**
- ADR-A003 taksonomi rezim. BELUM ADA (nomor dicadangkan).
- ADR-A004 kebijakan KC-6. DITERIMA.
- ADR-A005 jenis instrumen tahap pertama. DITERIMA.
- ADR-A006 karantina + persistensi. DITERIMA, DITERAPKAN, TERVERIFIKASI DARI
  LUAR.
- **ADR-A007 serapan hibrida. DIUSULKAN**, belum diterima. Wajib memperhitungkan
  temuan `jumlah_baris` dan kendala R-146.
- **ADR-A008 akibat KC-18. BELUM DITULIS**, tetapi bahannya kini ada: kematian
  bertahap (2024-06..2025-04) lawan tebing penerbitan serempak (2025-07).
- ADR berikutnya **A009** setelah A008 ditulis.

## Temuan sampingan yang belum diukur

- Bentangan penuh KC-18 atas 456 simbol-bulan kohort.
- 28 anggota kohort di luar sampel abjad.
- 15 `SETTLED` lain: apakah punya pendahulu seperti SXPUSDT?
- Daftar `INDEKS` hanya tiga nama, disusun manual.
- Saham dan komoditas token masih terhitung `perpetual_usdt`.
- `.decode("utf-8","replace")` di `klines` membungkam byte rusak.
- Apakah BUSD/USDC layak digabung dengan USDT.
- Sisa 16 simbol non-ASCII belum diuji langsung (3 sudah).
- Sebab KC-14 (H-A004) tidak dapat diuji. Sebab KC-15 tidak diketahui.
- Apakah lubang funding BNXUSDT 2022-04..2023-01 berimpit dengan lubang
  klines-nya. BNXUSDT ada di kohort DAN punya lubang tengah; jangan
  memperlakukan keanggotaan kohort sebagai penjelasan tunggal untuknya.
- Selisih penyebut diagnosa KC-15: 38 diperiksa, 41 dirancang.
- `reports/funding_selisih_penuh.json` belum pernah dibaca; `daftar_terpotong`
  masih true (500 dari 880).
- Selisih byte funding AGIXUSDT 531 lawan 529.
- `waktu_utc` runner berjalan lebih dulu daripada jam sesi; belum diselidiki,
  belum layak disebut cacat.
