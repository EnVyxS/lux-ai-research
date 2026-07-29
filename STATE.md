# STATE — versi 30

Diperbarui: 2026-07-29 (sesi 54, lanjutan). Aturan hanya BERTAMBAH; jangan
menulis ulang dari ingatan. v30 disusun di atas teks v29 yang dibaca langsung
dari `main` (blob `f066b6ea`), ditambah jurnal 82 (`e94ed337`), delapan laporan
ringkas `kehidupan_arsip` (run pecahan 0 = **30419770259**, commit `0929643c`),
serta dua run CI yang dicocokkan commit-nya: **30419770312** (`0929643c`, 291
butir, kode **1**) dan **30420236800** (`dceb1009`, 291 butir, kode **0**).

Peristiwa terbesar sejak v29: **kehidupan SELURUH semesta terserap kini
terukur.** 19.586 simbol-bulan lolos gerbang diurai kolom demi kolom: **1.401
MATI, 98 SEPI, 18.087 HIDUP, 0 tak terukur.** Kematian ternyata jauh melampaui
kohort puncak, tetapi semesta tetap 92,35% hidup.

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
    **Ditaati pada R-198, R-200, R-204, R-205, dan R-208.**
39. **[v22]** Keseragaman yang terukur pada sampel DILARANG dipakai sebagai
    angka ramalan untuk anggota di luar sampel; wajib pita atau kemungkinan
    campuran. Lahir dari R-114. **Dibenarkan keras [v30]:** kohort puncak 100%
    mati, semesta 7,15% mati.
40. **[v22]** Tiap laporan yang mencacah baris sebuah simbol-bulan wajib memuat
    uji silang `baris + hilang_di_tengah + tepi = menit_kalender` dan melaporkan
    selisihnya walau nol. Lahir dari 210 menit BNXUSDT 2022-04.
41. **[v23]** Ramalan bersyarat yang penyebutnya nol dicatat TIDAK
    TERADJUDIKASI, bukan TEPAT, dan status itu wajib dipra-registrasikan bersama
    ramalannya. Lahir dari R-120. Aktif pada laporan kehidupan kohort
    (`penyebut_tanpa_mati` = 0). **TIDAK aktif lagi untuk semesta [v30]:**
    `penyebut_tanpa_mati` semesta = **18.185**, jadi rasio di atasnya kini dapat
    diadjudikasi.
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
    `57a04f1e`. Ditaati pada `ab4e0774`, `387037a9`, `796c2fc4`, `5c65adf9`,
    `d4a2f60a`, dan **`0929643c`** (kehidupan_arsip: modul + uji + workflow).
46. **[v26, LUNAS DI KODE v28] Kode dilarang menyimpulkan dari penyebut nol.**
    Medan yang MENYIMPULKAN sebuah definisi atau sebab wajib memeriksa lebih
    dulu apakah kasusnya mampu membedakan. Bila penyebutnya nol, atau bila kedua
    kemungkinan menghasilkan angka yang sama, medan itu wajib berbunyi "tidak
    dapat dibedakan", bukan menyebut salah satu. Aturan 30 dan 41 melarang AGEN
    menyimpulkan dari penyebut nol; aturan ini melarang KODE melakukannya.
    Lahir dari `pulihkan.py` VERSI 1, yang pada pecahan 2 dan 5 (tanpa
    karantina) mencetak `definisi_jumlah_baris` = "baris lolos saja" padahal
    kedua definisi menghasilkan angka identik di sana. **Diperbaiki di
    `pulihkan.py` VERSI 2** (commit `5c65adf9`) lewat fungsi murni
    `putuskan_definisi` dan medan penggugur `definisi_dapat_dibedakan`. Sudah
    lebih dulu DITAATI oleh `kohort_ekor` V4 (`bangkit_dapat_diuji`), lalu oleh
    `kehidupan` V1 dan `kehidupan_arsip` V1 (`penyebut_tanpa_mati_kosong`).
47. **[v27, lahir di jurnal 69]** Sebelum menulis ramalan berupa cacah,
    sebutkan satuannya secara eksplisit — simbol, bulan, simbol-bulan, baris,
    atau butir uji — dan periksa bahwa angka rujukan yang dipakai memang
    bersatuan itu. Lahir dari R-163.
48. **[v27, lahir di jurnal 71]** Berkas modul yang mendekati pagar 800 baris
    harus dipecah SEBELUM fungsi baru ditambahkan, dan setiap pemecahan wajib
    memperluas daftar berkas yang masuk `sidik_kode`.
49. **[v27, lahir di jurnal 72]** Pemecahan berkas yang mempertahankan seluruh
    nama fungsi lewat re-export TETAP dapat mematahkan uji, karena re-export
    memindahkan fungsi dan bukan modul. Telusuri juga nama yang DITAMBAL
    (`monkeypatch.setattr`, `patch`, akses atribut modul).
50. **[v27, lahir di jurnal 73]** Setiap pengukuran yang menyimpulkan dari
    KETIADAAN — volume nol, berkas hilang, baris kosong, jawaban 404 — wajib
    memuat kendali positif yang membuktikan alat ukurnya mampu mendeteksi
    KEHADIRAN pada kondisi yang sama. Dipakai sebagai klausa gugur ADR-A008 §6;
    pada run kehidupan kohort klausa itu tidak aktif (kendali 4/4), dan pada run
    semesta juga tidak aktif (**kendali 24/24 hidup**).
51. **[v27, lahir di jurnal 75]** Jendela pemindaian mundur wajib adaptif, atau
    dibuktikan mencakup peristiwa yang dicari. Jendela tetap yang seluruh isinya
    sepi menghasilkan null, bukan jawaban. **Ditaati pada kohort_ekor V4.**
52. **[v27, lahir di jurnal 75]** Laporan yang tidak dapat dibaca utuh setara
    dengan laporan yang tidak ada. Setiap pelapor besar wajib berpasangan dengan
    keluaran ringkas yang memuat sidik berkas sumbernya. Ditaati oleh
    `kohort_ringkas`, `ukur_baris`, `kehidupan`, dan **`kehidupan_arsip`**
    (delapan laporan penuh 991.422–1.261.637 B, masing-masing berpasangan
    dengan `_ringkas.json` yang terbaca utuh).
53. **[v30, lahir dari R-205] Ramalan kode keluar sebuah run yang gerbangnya
    adalah berkas uji wajib didahului pembacaan PERILAKU setiap fungsi yang
    diuji, bukan hanya namanya.** Membaca modul tidak sama dengan mengetahui
    pembulatan, pemotongan, atau normalisasi yang dilakukannya. Lahir dari
    R-205: uji menuntut `bagian_volume_nol` sama dengan 2/3 penuh, sedangkan
    `kohort_ekor.bagian` MEMBULATKAN ke empat desimal dan mengembalikan 0,6667 —
    CI keluar dengan kode 1 karena harapan uji, bukan karena modulnya. Ramalan
    berkepala dua (cacah butir DAN kode keluar) yang separuhnya salah
    diadjudikasi SEPARUH, bukan MELESET.

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
  memuat **516.135 baris**, terbaca ulang dari luar runner. **Kehidupan
  keduabelasnya BELUM diukur** — tar karantina terpisah dan tidak disentuh run
  `kehidupan_arsip`.
- **KC-16 DITARIK [v23] — nomornya TETAP kosong selamanya.**
- **KC-17 [v24] — parquet karantina tidak dipersistenkan. DITUTUP [v25],
  diperkuat [v26].**
- **KC-18 [v27, dinamai di jurnal 74] — lilin datar lolos gerbang struktural.**
  Arsip menerbitkan berkas klines 1m lengkap dan sah secara bentuk untuk pasar
  yang tidak diperdagangkan: stempel waktu rapat tanpa menit hilang, checksum
  cocok, namun `volume` dan `count` nol pada SELURUH lilin. Gerbang 1m
  meloloskannya karena menilai BENTUK deret, bukan KEHIDUPAN pasar.
  - Bentangan jurnal 74: 864.000 lilin pada 20 simbol-bulan.
  - Bentangan jurnal 77: 169 dari 179 simbol-bulan sepi pada 10 simbol.
  - Bentangan kohort [v29] — run `30418471430`: **456 dari 456** simbol-bulan
    kohort puncak 2025-07 MATI, 19.972.800 lilin, 456/456 lolos gerbang.
  - **BENTANGAN SEMESTA TERUKUR [v30]** — delapan run pecahan pada commit
    `0929643c`: dari **19.586** simbol-bulan lolos gerbang, **1.401 MATI**
    (7,153%), **98 SEPI** (0,500%), **18.087 HIDUP** (92,35%).
  - **Kematian TIDAK terkurung di kohort puncak.** 456 MATI kohort termuat di
    dalam 1.401, sehingga **945 simbol-bulan MATI berada di luar kohort puncak**
    (angka turunan, bukan medan run). Dua pertiga kematian tak terlihat dari
    kohort funding.
  - Ekstrapolasi dari kohort ke semesta TERBUKTI keliru arah: kohort 100% mati,
    semesta 7,15% mati. Aturan 39 dibenarkan.
  - **Kebijakan DIPUTUSKAN [v28] oleh ADR-A008** (Keputusan 1–6 DITERIMA):
    KC-18 bukan gerbang serapan; kehidupan diukur per simbol-bulan; **SEPI**
    bila `bagian_volume_nol` ≥ 0,5 dan **MATI** bila `transaksi_total` = 0;
    setiap penyebut diterbitkan berpasangan; backtest hanya pada simbol-bulan
    HIDUP; angka 839.842.134 tidak ditulis ulang (aturan 29). Keputusan 7
    DITANGGUHKAN. **Klausa gugur §6 tidak aktif** pada kedua run.

## Kehidupan semesta terserap — TERUKUR [v30]

Modul `lux_ai/serapan/kehidupan_arsip.py` V1 (blob `318a5cb1…`, `sidik_kode`
**`24b6bb265525e81c2e571b46e401f36903383f1e3738c487850861adc3e8c595`**), didorong
atomik bersama uji dan workflow pada commit `0929643c` (aturan 45). Delapan
runner mengunduh tar rilis `serapan-pecahan-<i>-30396803601`, membongkarnya, dan
mengukur kolom `volume` serta `trades` tiap parquet lolos gerbang. Run pecahan
0 = **30419770259**. Sidik kode SAMA di kedelapan laporan, sehingga penjumlahan
lintas pecahan sah (aturan 20, 22).

| pecahan | penyebut penuh | MATI | SEPI | HIDUP | tanpa MATI | bagian_mati | lilin penuh | lilin mati |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 2.408 | 122 | 13 | 2.273 | 2.286 | 0,0507 | 103.134.312 | 5.339.520 |
| 1 | 2.465 | 103 | 11 | 2.351 | 2.362 | 0,0418 | 105.634.220 | 4.468.906 |
| 2 | 2.337 | 204 | 7 | 2.126 | 2.133 | 0,0873 | 100.058.416 | 8.922.240 |
| 3 | 2.153 | 283 | 17 | 1.853 | 1.870 | 0,1314 | 91.841.734 | 12.379.101 |
| 4 | 2.496 | 182 | 15 | 2.299 | 2.314 | 0,0729 | 106.821.807 | 7.924.835 |
| 5 | 2.741 | 165 | 12 | 2.564 | 2.576 | 0,0602 | 117.671.896 | 7.204.748 |
| 6 | 2.649 | 182 | 8 | 2.459 | 2.467 | 0,0687 | 113.890.221 | 7.941.027 |
| 7 | 2.337 | 160 | 15 | 2.162 | 2.177 | 0,0685 | 100.273.393 | 6.987.746 |
| **jumlah** | **19.586** | **1.401** | **98** | **18.087** | **18.185** | — | **839.325.999** | **61.168.123** |

Uji silang (aturan 21):

- 1.401 + 98 + 18.087 = **19.586** ✅ dan jumlah penyebut = 19.586, penyebut yang
  dipraregistrasi — BUKAN 19.598 (dua belas karantina tak ada di tar ini).
- 19.586 − 1.401 = **18.185** = jumlah `penyebut_tanpa_mati` ✅
- Jumlah `lilin_penuh` **839.325.999** cocok PERSIS dengan baris lolos gerbang
  yang diukur serapan (run `30396803601`) lewat jalur kode yang sepenuhnya
  berbeda — dari zip, bukan dari parquet. Dua pengukuran independen bertemu di
  satu angka; bukti kuat bahwa seluruh isi arsip terbaca.
- Lilin mati 61.168.123 = **7,29%** dari seluruh baris; MATI + SEPI = 1.499 =
  **7,654%** dari 19.586.

Medan penggugur (aturan 24) bersih di kedelapan pecahan: `cacah_tak_terukur` 0,
`cacah_baris_cacat` **0** dari 839 juta baris teks yang diurai,
`cacah_parquet_hilang` 0, `cacah_parquet_tak_dikenal` 0, `cacah_bagian_hilang`
0, `cacah_sha_tak_cocok` 0, `cacah_anggota_tak_aman` 0, `kode_keluar` 0.
Kendali positif (aturan 50): **24 dari 24 HIDUP**, `parser_terbukti` **true**
pada kedelapan pecahan.

Yang BOLEH disimpulkan: 7,654% simbol-bulan lolos gerbang tidak layak
di-backtest tanpa penyaringan tambahan; semesta yang layak = **18.087**
simbol-bulan.
Yang TIDAK BOLEH: memakai 7,153% sebagai laju kematian simbol mana pun —
sebarannya 4,18% (pecahan 1) sampai 13,14% (pecahan 3), jarak lebih dari tiga
kali, dan pecahan dibagi menurut simbol sehingga ketidakseragaman ini sifat
pasar, bukan derau.

## Kehidupan kohort puncak 2025-07 — TERUKUR [v29]

Modul `lux_ai/serapan/kehidupan.py` V1 (blob `f49abb2b…`, 417 baris,
`sidik_kode` `c1aaf852…b4cc`). Run **30418471430**, commit `d4a2f60a`, kode 0.
Ringkasan `reports/kehidupan_ringkas.json` (1.406 B) terbaca UTUH.

| medan | nilai |
| --- | ---: |
| simbol diukur | 38 |
| simbol-bulan diminta / terukur / tak terukur | 456 / 456 / 0 |
| MATI / SEPI / HIDUP | **456** / 0 / **0** |
| MATI yang lolos gerbang | **456** |
| lilin penuh = lilin mati | **19.972.800** |
| penyebut penuh / tanpa MATI | 456 / **0** (kosong) |
| kendali diminta / terambil / hidup | 4 / 4 / **4** |

Uji silang: 38 × 525.600 = 19.972.800 ✅ dan 38 × 12 = 456 ✅
Konsekuensi: kohort puncak menyumbang **nol** simbol-bulan layak backtest.
Yang TIDAK terbukti: bahwa 38 simbol ini tak pernah diperdagangkan — kohort V4
menunjukkan sebagian hidup pada 2024–2025.

## Hipotesis

- H-A001: belum diuji.
- H-A002a / H-A002b: H-A002b **GUGUR** (`slot_5m_hadir_saat_1m_hilang` = 0).
- **H-A003: MENANG pada 3, GUGUR pada 9.**
- **H-A004: TIDAK TERUJI dan tidak dapat diuji** (`fapi.binance.com` → 451).
- **H-A005: GUGUR pada rentang yang disampel [v23]** (37 bulan tengah).
- **H-A006 — serapan bersifat deterministik. MENANG pada ENAM run.**
- **H-A008 [v26] — aset rilis GitHub mengembalikan byte yang sama persis.
  MENANG pada DUA kali pengambilan penuh** — 29 aset / 32.754.749.440 byte pada
  run pemulihan, lalu kedelapan tar diunduh ulang oleh `kehidupan_arsip` dengan
  `cacah_sha_tak_cocok` 0 dan cacah baris yang kembali persis 839.325.999.

## Papan skor prediksi

R-1..R-120 dirinci v23. R-121..R-149 di v26 dan jurnal 56–63. R-150..R-193 di
jurnal 64–75. R-194..R-197 di jurnal 76 dan 77. R-198..R-199 di jurnal 78.
R-200 di jurnal 79. R-201 di jurnal 81. R-202..R-204 di jurnal 80.
R-205..R-207 dipraregistrasi di docstring commit `0929643c`; R-208 di docstring
commit `dceb1009`; R-209 di jurnal 82.

| # | Prediksi | Status |
|---|---|---|
| R-175 | kedua berkas ≤800 baris DAN `funding.py` pita 500..680 | **SEPARUH** |
| R-179 | `funding.py` 640..700 DAN `funding_cdn.py` 140..200 | **SEPARUH** |
| R-198 | CI 253 butir, kode 0 | TEPAT |
| R-199 | `definisi_dapat_dibedakan` false pada TEPAT 2 pecahan (2 dan 5) | **MENUNGGU** |
| R-200 | CI **269 butir**, kode 0 (253 + 16) | **TEPAT** |
| R-201 | MATI pita 350..456 SIMBOL-BULAN DAN `cacah_hidup` 0 | **TEPAT** |
| R-202 | `pulihkan.py` V2 pita 340..420 BARIS | **TEPAT** (383) |
| R-203 | `kehidupan.py` pita 300..400 BARIS DAN 0 berkas lewat pagar | **MELESET** (417) |
| R-204 | CI tetap 269 butir, kode 0, pada `12dde093` | **TEPAT** |
| R-205 | CI **291 butir** (269+22) DAN kode 0 | **SEPARUH** (291 tepat, kode 1) |
| R-206 | MATI semesta pita 456..2.000 atas penyebut 19.586 | **TEPAT** (1.401) |
| R-207 | `parser_terbukti` true pada kedelapan pecahan | **TEPAT** (8/8) |
| R-208 | CI 291 butir, kode 0, pada commit perbaikan uji | **TEPAT** (`30420236800`) |
| R-209 | CI 291 butir, kode 0, pada commit jurnal 82 | **MENUNGGU** |

**Total R-1..R-209** (aturan 21): TEPAT **146**; MELESET **38**; SEPARUH **12**;
TIDAK TERADJUDIKASI **5**; MENUNGGU **8** (R-7, R-19, R-20, R-28, R-36, R-37,
R-199, R-209). 146+38+12+5+8 = **209** ✅ Ramalan berikutnya **R-210**.
N_percobaan = 0.

Catatan kejujuran: R-175, R-179, dan R-203 adalah satu pola — menaksir panjang
berkas ketika ia dapat dihitung; pola itu TIDAK terulang giliran ini sebab saya
sengaja tidak meramalkan cacah baris `kehidupan_arsip.py`. R-205 adalah pola
BARU dan lebih dalam: meramalkan kode keluar tanpa membaca perilaku pembulatan
fungsi yang saya panggil sendiri. Pola itu kini menjadi **aturan 53**. R-206
TEPAT atas pita 456..2.000 yang lebar; ketepatannya tidak layak dibanggakan.

## Cacah baris terukur [v29]

Sumber: `reports/ukur_baris.json` V2, run **30418761259**, commit `12dde093`,
kode 0. Penggugur bersih: `cacah_berkas_hilang` 0, `cacah_berkas_melebihi_pagar`
0, `cacah_berkas_ada` 10 dari 10. Definisi `len(teks.splitlines())`, PERSIS
definisi pagar 800 di `tests/test_kontinuitas.py`.

| berkas | baris | byte |
| --- | ---: | ---: |
| `funding.py` | **705** | 28.121 |
| `kohort_ekor.py` | 553 | 22.590 |
| `kehidupan.py` | **417** | 16.638 |
| `pulihkan.py` V2 | **383** | 14.839 |
| `gerbang_1m.py` | 184 | 6.775 |
| `ukur_baris.py` V2 | 183 | 7.623 |
| `funding_cdn.py` | 162 | 6.335 |
| `arsip.py` | 154 | 5.231 |
| `resample.py` | 127 | 4.356 |
| `kohort_ringkas.py` | 82 | 2.882 |

Total **2.950** baris; terbesar `funding.py` 705 — 95 baris di bawah pagar 800.
Aturan 48 berlaku padanya: fungsi baru DILARANG ditambahkan sebelum dipecah.

**UTANG [v30]:** `kehidupan_arsip.py` BELUM masuk `BERKAS_DIUKUR` di
`ukur_baris.py`, jadi cacah barisnya belum terukur dan DILARANG ditaksir dari
byte (aturan 21). Berkas ke-11 ini harus ditambahkan pada push berikutnya yang
menyentuh `ukur_baris.py`.

## Definisi `jumlah_baris` — TERSELESAIKAN [v26], DITEGAKKAN DI KODE [v28]

**`jumlah_baris` di manifes = baris lolos gerbang + baris karantina.** Terbukti
pada keenam pecahan yang punya karantina: `selisih_baris_total` = 0 dan
`selisih_baris_utama` = −(baris karantina). Pecahan 2 dan 5 tidak dapat
membedakan (aturan 46).

- Baris lolos gerbang saja: **839.325.999** — kini DIKUATKAN oleh pengukuran
  kedua yang berdiri sendiri (jumlah `lilin_penuh` kedelapan pecahan).
- Baris karantina: **516.135**
- Jumlah: **839.842.134** = angka semesta.

Konsekuensi untuk ADR-A007: 839.842.134 SUDAH memuat 516.135 baris cacat. Baris
hasil pemulihan harian tidak boleh dijumlahkan tanpa lebih dulu mengurangi baris
karantina yang digantikannya.

**`pulihkan.py` VERSI 2** (commit `5c65adf9`, 383 baris) menegakkan ini lewat
fungsi murni `putuskan_definisi` dan medan `definisi_dapat_dibedakan`.

**Peringatan membaca laporan:** `reports/pulihkan_pecahan_<i>.json` di git masih
HASIL V1; label keliru pada pecahan 2 dan 5 masih terbaca di sana. Cocokkan
`versi_pulihkan` dan `sidik_kode` sebelum mempercayainya.

## Serapan semesta `perpetual_usdt` — TERUKUR, TERPERSISTENSI, TERPULIHKAN

Sumber serapan: run **`30396803601`**, commit `57a04f1e`, `versi_pecahan` **6**,
`sidik_kode` **`237ccf42…`**, `sidik_data` `6128fbb0…`.
Sumber pemulihan: run **`30404071324`**, commit `ab4e0774`, `versi_pulihkan` 1,
`sidik_kode` **`c76ff896…b38`**.

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
- **Pemulihan (run `30404071324`):** 29/29 aset hadir, 29/29 sha cocok,
  839.842.134 baris terbaca ulang oleh pyarrow.
- Tag rilis: `serapan-pecahan-<i>-30396803601`.
- **Penyebut ganda kini LENGKAP [v30]:** penyebut PENUH 19.586 simbol-bulan
  lolos gerbang (19.598 termasuk karantina); penyebut TANPA MATI **18.185**;
  penyebut LAYAK BACKTEST (HIDUP saja) **18.087**.

## Funding semesta — TERUKUR (`funding.py` V6)

Run FUNDING 6 `30412188715`, commit `ba37c5d5`, kode 0.
`sidik_kode` `d3854823…`, `sidik_data` `6128fbb0…` (tak berubah sejak V1).

- 880 bulan klines tanpa funding; 87 funding tanpa klines; penyebut 19.598.
- Bentuk lubang: {awal 48, ekor 826, tengah 6, hilang 880}. 116 simbol berlubang
  ekor (14,74% dari 787).
- **Kohort puncak 2025-07: 38 simbol, 456 simbol-bulan**, `seri` false; 456 =
  51,8% dari seluruh 880 lubang. Ke-38 anggota punya bulan klines terakhir
  2026-06 — dan terbukti ke-456 simbol-bulan itu MATI.
- `uji_cdn`: 10 kohort menjawab **404**, 10 kendali menjawab **200** dengan
  checksum cocok, byte kendali 529–1.939.
- **Pertanyaan yang kini terbuka [v30]:** 945 simbol-bulan MATI di luar kohort
  puncak — apakah funding-nya juga hilang? Bila mati tanpa lubang funding, maka
  tebing funding dan kematian pasar adalah dua peristiwa berbeda, dan tafsir
  ADR-A002 §10 harus disusun ulang atas dasar itu, bukan atas kohort.

## Kohort ekor — kematian bertahap lawan tebing serempak [v27]

Modul `kohort_ekor.py` V1→4 dan pelapor ringkas `kohort_ringkas.py` V1.
**V4** (`73ca4eb2…0fcda`, run `30416845475`, commit `387037a9`, kode 0):
pindaian ADAPTIF, pagu keras 60 bulan, pagu tak pernah tersentuh.
**Catatan [v30]:** `kohort_ekor.bagian` MEMBULATKAN ke empat desimal — sifat
yang melahirkan aturan 53. Pembulatan itu TIDAK diubah (aturan 29).

| simbol | bulan hidup terakhir | simbol | bulan hidup terakhir |
| --- | --- | --- | --- |
| AGIXUSDT | 2024-06 | BLZUSDT | 2024-12 |
| ALPACAUSDT | 2025-04 | BNXUSDT | 2025-03 |
| AMBUSDT | 2025-02 | BONDUSDT | 2024-11 |
| BADGERUSDT | 2025-03 | COMBOUSDT | 2025-03 |
| BALUSDT | 2025-03 | DARUSDT | 2024-12 |

Kesepuluhnya berhenti SEBELUM tebing funding 2025-07, tersebar pada sembilan
bulan berbeda — tebing funding lebih menyerupai perubahan rezim PENERBITAN.
Yang TIDAK dibuktikan: (a) 28 anggota sisanya (aturan 20); (b)
`cacah_simbol_bangkit_dapat_diuji` 0, jadi `bangkit_kembali` 0 bukan bukti;
(c) arsip funding TIDAK terbukti cacat — **ADR-A002 §10 tidak boleh diubah atas
bukti kohort semata.**

**Jalan pintas yang kini tersedia [v30]:** `reports/kehidupan_arsip_<i>.json`
memuat status per simbol-bulan bagi SELURUH semesta, sehingga
`bulan_hidup_terakhir` bagi 28 anggota sisanya mungkin dijawab tanpa unduhan
baru — dengan syarat definisi "hidup terakhir" dicocokkan lebih dulu dengan
definisi `kohort_ekor` (aturan 36).

## Jumlah uji

**291 TERVERIFIKASI** — `reports/ci_terakhir.json` run **30420236800**, commit
`dceb1009`, `kode_keluar` **0**, "291 tests collected in 0.43s";
`reports/ci_terakhir.txt` terbaca utuh "291 passed in 0.95s" (aturan 52).
Riwayat: 231 → 234 → 236 → 239 → 241 → 244 → 253 → 269 → **291**
(`test_kehidupan_arsip.py` menambah 22 butir). Run CI `30419770312` pada
`0929643c` mengumpulkan 291 butir yang sama tetapi keluar dengan kode 1 — satu
harapan uji yang salah, bukan modul yang salah.

## Utang verifikasi

1-5 dan 11 menunggu tahap juri/klasifikasi. 6-23, 25-28 LUNAS.

24. **AKTIF.**
    - persistensi data lolos dan karantina: **LUNAS**;
    - pemulihan aset di luar runner: **LUNAS** (run `30404071324`);
    - perbaikan aturan 46 di `pulihkan.py`: **LUNAS DI KODE** (V2) — laporan
      pecahan di git masih hasil V1;
    - cacah baris `pulihkan.py` V2: **LUNAS** (383);
    - bentangan penuh KC-18 atas 456 simbol-bulan kohort: **LUNAS**;
    - **pengukur kehidupan atas SEMESTA: LUNAS [v30]** — 19.586 simbol-bulan
      terukur, 0 tak terukur, kendali 24/24 (run pecahan `30419770259` dst.);
    - **penyebut kedua atas semesta: LUNAS [v30]** — 18.185 tanpa MATI, 18.087
      HIDUP;
    - cacah baris `kehidupan_arsip.py` (masuk `BERKAS_DIUKUR`): BELUM;
    - kehidupan 12 simbol-bulan karantina: BELUM (tar terpisah);
    - jalur **funding**: `funding_ada` masih null di seluruh manifes — BELUM;
    - medan `dugaan_pengganti` (ADR-A005) — BELUM;
    - pemulihan harian ADR-A007 — BELUM, bahan baku sudah ada;
    - karantina artefak 7 hari — BELUM;
    - 28 anggota kohort yang belum disampel `kohort_ekor` — BELUM (kini mungkin
      dijawab dari laporan kehidupan semesta);
    - funding bagi 945 MATI di luar kohort puncak — BELUM.
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
- **ADR-A008 akibat KC-18. DITERIMA [v28] untuk Keputusan 1–6**; Keputusan 2–4
  TERTERAP dan TERJALANKAN atas SELURUH semesta [v30]. Keputusan 5 (backtest
  hanya pada HIDUP) kini punya semesta bernama: **18.087** simbol-bulan.
  Keputusan 7 DITANGGUHKAN sampai sifat 48 lubang awal dan 6 lubang tengah
  terukur. Klausa gugur §6 diperiksa dan **tidak aktif** pada kedua run.
- ADR berikutnya **A009**.

## Temuan sampingan yang belum diukur

- **Funding bagi 945 simbol-bulan MATI di luar kohort puncak** — penentu apakah
  tebing funding dan kematian pasar peristiwa yang sama atau bukan.
- Sebaran 1.401 MATI menurut TAHUN dan menurut SIMBOL (laporan penuh memuatnya;
  belum dibaca).
- Kehidupan 12 simbol-bulan karantina.
- Pindaian `bulan_hidup_terakhir` bagi 28 anggota kohort di luar sampel abjad.
- Sifat 48 lubang funding AWAL dan 6 lubang TENGAH — penentu Keputusan 7
  ADR-A008.
- 15 `SETTLED` lain: apakah punya pendahulu seperti SXPUSDT?
- Daftar `INDEKS` hanya tiga nama, disusun manual.
- Saham dan komoditas token masih terhitung `perpetual_usdt`.
- `.decode("utf-8","replace")` di `klines` membungkam byte rusak.
- Apakah BUSD/USDC layak digabung dengan USDT.
- Sisa 16 simbol non-ASCII belum diuji langsung (3 sudah).
- Sebab KC-14 (H-A004) tidak dapat diuji. Sebab KC-15 tidak diketahui.
- Apakah lubang funding BNXUSDT 2022-04..2023-01 berimpit dengan lubang
  klines-nya.
- Selisih penyebut diagnosa KC-15: 38 diperiksa, 41 dirancang.
- `reports/funding_selisih_penuh.json` belum pernah dibaca; `daftar_terpotong`
  masih true (500 dari 880).
- Selisih byte funding AGIXUSDT 531 lawan 529.
- `waktu_utc` runner berjalan lebih dulu daripada jam sesi.
- `tests/test_pulihkan.py` belum pernah dibaca ulang sesudah push.
