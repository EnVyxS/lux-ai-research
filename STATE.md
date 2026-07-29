# STATE — versi 35

Diperbarui: 2026-07-29 (sesi 54, lanjutan). Aturan hanya BERTAMBAH; jangan
menulis ulang dari ingatan. v35 disusun di atas teks v34 yang dibaca langsung dari
`main` (blob `12a25cd1`), ditambah jurnal 90 (`f59b7c82`) dan jurnal 91
(`cbd5e8e6`), laporan `reports/kebangkitan.json` (blob
**`43b70e24dfb0385c0d07ffbd45b368d2c16dea24`**, 17.644 B, dibaca **UTUH**),
`reports/kebangkitan_ringkas.json` (blob `810ee0a4`),
`reports/kebangkitan_status.json` (blob `19304a77`), serta tiga run yang
dicocokkan commit-nya: **30442623074** (`63fc2e8f`, CI **396**), **30443289417**
(`bdcbaebc`, CI **450**), dan **30443289476** (`bdcbaebc`, `kebangkitan` **V1**).
Semuanya kode 0.

Peristiwa terbesar sejak v34: **kebangkitan bukan peristiwa tunggal.** H-A012
MENANG — **delapan** simbol dari 787 punya bulan MATI lalu bulan HIDUP sesudahnya,
kedelapannya `bangkit_penuh`. Sekaligus dua koreksi mahal: kronologi LITUSDT yang
ditulis v34 SALAH (mati 2025-02, bukan 2025-07), dan BTCSTUSDT ternyata kebalikan
LITUSDT — funding pulih tanpa perdagangan, **53 dari 53 bulan MATI**. Dari kedua
kekeliruan itu lahir aturan 60 dan 61 serta KC-22 dan KC-23.

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
    (198 lawan **201**). **Ditaati pada R-198, R-200, R-204, R-205, R-208, R-215,
    R-220, R-221, R-226, R-227, R-228, R-231, dan R-232.** Dilanggar pada R-211
    [v31] dan R-217 [v32] — lihat aturan 54, 57, dan KC-19. **Catatan [v34]:**
    laporan CI dapat TERTIMPA oleh run berikutnya di `main`; bila demikian,
    bacalah pada ref commit yang bersangkutan (R-227 hanya terbaca lewat ref
    `be5cd877`). **Cara menemukan ref-nya [v35]:** `list_commits` dengan
    `path="reports/ci_terakhir.json"` mendaftar setiap commit runner beserta nomor
    run di pesannya; R-231 diadjudikasi lewat ref `acd79d41` dengan cara ini.
39. **[v22]** Keseragaman yang terukur pada sampel DILARANG dipakai sebagai
    angka ramalan untuk anggota di luar sampel; wajib pita atau kemungkinan
    campuran. Lahir dari R-114. **Dibenarkan keras [v30]:** kohort puncak 100%
    mati, semesta 7,15% mati. **Dibenarkan kedua kali [v31]:** kohort puncak
    456/456 berlubang funding, semesta hanya 842 dari 1.401 MATI.
40. **[v22]** Tiap laporan yang mencacah baris sebuah simbol-bulan wajib memuat
    uji silang `baris + hilang_di_tengah + tepi = menit_kalender` dan melaporkan
    selisihnya walau nol. Lahir dari 210 menit BNXUSDT 2022-04.
41. **[v23]** Ramalan bersyarat yang penyebutnya nol dicatat TIDAK
    TERADJUDIKASI, bukan TEPAT, dan status itu wajib dipra-registrasikan bersama
    ramalannya. Lahir dari R-120. **TIDAK aktif lagi untuk semesta [v30]:**
    `penyebut_tanpa_mati` semesta = **18.185**.
42. **[v23]** Kelas cacat baru DILARANG dinamai atas dasar satu angka yang
    belum diukur langsung. Tuduhan ditulis sebagai hipotesis + run, bukan
    sebagai kelas. Lahir dari KC-16 yang ditarik. **Ditaati pada KC-18, KC-21,
    KC-22, dan KC-23** — yang terakhir dinamai hanya sesudah kedua angkanya
    terukur langsung (2025-02 lawan 2025-06).
43. **[v24]** Medan penggugur yang membandingkan taksiran dengan kenyataan wajib
    memakai toleransi yang BERSKALA terhadap cacah item, bukan margin datar.
44. **[v24]** Ramalan wajib menyebut penyebutnya secara eksplisit: pecahan mana,
    semesta mana, medan mana. Bila sebuah pita hanya masuk akal di bawah satu
    tafsir dan meleset di bawah tafsir lain, ia diadjudikasi MELESET. Lahir dari
    R-131.
45. **[v25] Keatomikan push pemicu.** Sebuah push yang MENYALAKAN run wajib
    memuat setiap berkas yang run itu bergantung padanya, dan daftar berkas itu
    wajib dihitung ulang tepat sebelum dikirim. GitHub Actions memakai berkas
    workflow pada commit PEMICU. Lahir dari `57a04f1e`. Ditaati pada `ab4e0774`,
    `387037a9`, `796c2fc4`, `5c65adf9`, `d4a2f60a`, `0929643c`, `1b0e8d8e`,
    `b1816ddf`, `680d04b4`, `be5cd877`, dan **`bdcbaebc`** (`kebangkitan` V1:
    modul + uji + workflow dalam SATU commit).
46. **[v26, LUNAS DI KODE v28] Kode dilarang menyimpulkan dari penyebut nol.**
    Medan yang MENYIMPULKAN sebuah definisi atau sebab wajib memeriksa lebih
    dulu apakah kasusnya mampu membedakan; bila tidak, ia wajib berbunyi "tidak
    dapat dibedakan". Ditaati oleh `kohort_ekor` V4, `kehidupan` V1,
    `kehidupan_arsip` V1, `silang_funding` V1–V2, `lubang_tengah` V1–V2, dan
    **`kebangkitan` V1** (`terukur`, `ada_hidup_sebelum`, `cacah_bulan_antara`).
    **[v34] Sisi lain aturan ini terbukti mahal** — lihat aturan 59.
47. **[v27]** Sebelum menulis ramalan berupa cacah, sebutkan satuannya secara
    eksplisit — simbol, bulan, simbol-bulan, baris, atau butir uji — dan periksa
    bahwa angka rujukan yang dipakai memang bersatuan itu. Lahir dari R-163.
48. **[v27]** Berkas modul yang mendekati pagar 800 baris harus dipecah SEBELUM
    fungsi baru ditambahkan, dan setiap pemecahan wajib memperluas daftar berkas
    `sidik_kode`. **Berlaku atas DUA berkas:** `funding.py` **705** dan
    `silang_funding.py` **705**. **[v35] Kini TIGA berkas belum terukur:**
    `lubang_tengah.py` V2, `kebangkitan.py` V1, dan kedua berkas ujinya.
49. **[v27]** Pemecahan berkas yang mempertahankan seluruh nama fungsi lewat
    re-export TETAP dapat mematahkan uji. Telusuri juga nama yang DITAMBAL
    (`monkeypatch.setattr`, `patch`, akses atribut modul).
50. **[v27]** Setiap pengukuran yang menyimpulkan dari KETIADAAN — volume nol,
    berkas hilang, baris kosong, jawaban 404 — wajib memuat kendali positif yang
    membuktikan alat ukurnya mampu mendeteksi KEHADIRAN pada kondisi yang sama.
    Pada seluruh run klausa gugur ADR-A008 §6 tidak aktif; `kebangkitan` V1 juga
    bersih (`kendali_sah` true, BTCUSDT 2021-05, 2021-08, 2021-01 HIDUP dan
    berfunding).
51. **[v27]** Jendela pemindaian mundur wajib adaptif, atau dibuktikan mencakup
    peristiwa yang dicari. **[v35] Dibenarkan telak:** `kohort_ekor` V4 memindai
    MUNDUR dari 2025-07 dan karena itu tidak pernah dapat melihat kebangkitan
    2025-08 atau 2026-01; `kebangkitan` V1 memindai SELURUH rentang dan menemukan
    delapan.
52. **[v27]** Laporan yang tidak dapat dibaca utuh setara dengan laporan yang
    tidak ada. Setiap pelapor besar wajib berpasangan dengan keluaran ringkas yang
    memuat sidik berkas sumbernya. Ditaati oleh `kohort_ringkas`, `ukur_baris`,
    `kehidupan`, `kehidupan_arsip`, `silang_funding`, `lubang_tengah` V1–V2, dan
    **`kebangkitan` V1**. **[v35]** `reports/kebangkitan.json` 17.644 B terbaca
    UTUH, jadi seluruh angkanya sah dipakai; laporan `silang_funding` penuh
    183.963 B tetap tak terbaca utuh selamanya.
53. **[v30]** Ramalan kode keluar sebuah run yang gerbangnya adalah berkas uji
    wajib didahului pembacaan PERILAKU setiap fungsi yang diuji, bukan hanya
    namanya. Lahir dari R-205. **Ditaati pada R-211, R-215, R-217, R-221, R-222,
    R-226, R-228, dan R-232** (kode keluar 0 benar pada semuanya).
54. **[v31]** Cacah butir uji dalam sebuah ramalan wajib dihitung dengan mencacah
    definisi `def test_` satu per satu pada berkas uji yang SUDAH selesai ditulis,
    mengalikan setiap fungsi berparameter dengan cacah kasusnya. Lahir dari R-211
    (312 lawan **316**). **TIDAK CUKUP [v32]** — lihat aturan 57.
55. **[v31]** Sebelum meramalkan hasil sebuah workflow, baca `paths`/`paths-ignore`
    workflow itu dan sebutkan di dalam ramalan workflow MANA yang akan menyala
    pada commit yang dimaksud. `ci.yml` memakai `paths-ignore` untuk `journal/**`,
    `decisions/**`, `hipotesis/**`, dan `reports/**`. **Ditaati pada R-217, R-221,
    R-226, R-227, R-228, R-231, dan R-232.**
56. **[v32]** Ramalan yang menyebut sebuah commit sebagai sasaran wajib menyebut
    sasaran yang keberadaannya dijamin oleh cara kerja saya sendiri. Bentuk sah:
    "commit BERIKUTNYA yang menyentuh `<berkas>`". **Ditaati pada R-217, R-220,
    R-221, R-226, R-227, R-228, R-231, dan R-232.**
57. **[v32]** Sebelum meramalkan cacah butir uji, nama setiap fungsi `def test_`
    WAJIB ditulis BERNOMOR di jurnal atau docstring, dan nomor terakhirnya dipakai
    sebagai cacahan. Lahir dari R-217 (42 ditulis, **47** nyata). **TERBUKTI
    BEKERJA TIGA DARI TIGA [v35]:** R-221 (42 nama → **382**), R-228 (56 nama →
    382 − 42 + 56 = **396**), R-232 (54 nama → 396 + 54 = **450**).
58. **[v33]** Cacah baris sebuah berkas yang versi terkininya belum dibaca ulang
    UTUH dalam giliran yang sama DILARANG diramalkan dengan pita sempit. Pilih:
    (a) baca ulang utuh dulu; (b) pita yang batas atasnya ≥**1,8×** batas bawah;
    (c) jangan meramal, cukup ukur. Lahir dari R-225 (pita 470..620, nyata
    **705**). **Pilihan (c) dipakai [v34–v35]** atas `lubang_tengah.py` V2 dan
    `kebangkitan.py` V1.
59. **[v34]** Ramalan yang menegaskan KETIADAAN sebuah gejala wajib menyebut
    penyebut yang mampu memuat gejala itu, beserta cacah kasus yang benar-benar
    pernah diperiksa. Bila cacah itu NOL, ramalan wajib ditulis sebagai kemungkinan
    campuran, bukan penegasan. Lahir dari R-230. Aturan 39 melarang
    mengekstrapolasi KESERAGAMAN sampel; aturan 59 melarang mengekstrapolasi
    KEKOSONGAN sampel. **Ditaati pada R-233 [v35]:** pita 2..80 simbol, bukan
    "hanya satu", dan hasilnya 8 — di dalam pita.
60. **[v35, lahir dari R-234] Tafsir MEKANISME yang menang pada satu kasus
    dilarang dipakai sebagai dasar ramalan atas kasus lain sebelum penyebutnya ≥2
    dan variasinya terukur.** Lahir dari R-234: mekanisme LITUSDT (funding kembali
    → perdagangan pulih) saya pindahkan ke BTCSTUSDT dan meramalkan `cacah_hidup`
    ≥1; hasilnya **0 dari 53**. Aturan 39 melarang memindahkan KESERAGAMAN,
    aturan 59 melarang memindahkan KEKOSONGAN, aturan 60 melarang memindahkan
    MEKANISME. Lihat KC-22.
61. **[v35, lahir dari koreksi jurnal 91] Nilai sebuah medan dilarang dipakai
    sebagai nilai medan jalur LAIN tanpa membaca laporan jalur itu.**
    `funding_sebelum` bukan `bulan_hidup_terakhir`; `bulan_funding_pertama` bukan
    `bulan_klines_pertama`. Bila laporan jalur yang dimaksud belum dibaca, tulis
    "belum diukur", bukan angka tetangga yang kebetulan tersedia. Aturan 36
    mengatur dua definisi atas SATU gejala; aturan 61 mengatur satu nama yang
    dipakai atas DUA gejala. Lihat KC-23.

## Kelas cacat

KC-1 s.d. KC-12 seperti pada v19. KC-10 dan KC-11 DITUTUP (v20). KC-13
(keterwakilan sampel) → penangkalnya aturan 37.

- **KC-14 [v21, dipersempit v22] — menit hilang NYATA di arsip 1m, hadir di
  KEDUA representasi.** **9** simbol-bulan, **6.375 menit** (425×15). Sebab tidak
  diketahui (H-A004, tak dapat diuji). Kebijakan: karantina (ADR-A006).
- **KC-15 [v22] — berkas klines BULANAN dapat kehilangan HARI UTC penuh yang
  datanya utuh di berkas HARIAN.** **3** simbol-bulan, semuanya BNXUSDT 2022,
  **7.200 menit = 5×1440**. Kebijakan: ADR-A007. Sebab masih tidak diketahui.
- 9 + 3 = **12** karantina; 6.375 + 7.200 = **13.575** menit ✅ Keduabelasnya
  memuat **516.135 baris**. **Kehidupan keduabelasnya BELUM diukur.**
- **KC-16 DITARIK [v23] — nomornya TETAP kosong selamanya.**
- **KC-17 [v24] — parquet karantina tidak dipersistenkan. DITUTUP [v25].**
- **KC-18 [v27] — lilin datar lolos gerbang struktural.** Arsip menerbitkan
  berkas klines 1m lengkap dan sah secara bentuk untuk pasar yang tidak
  diperdagangkan: stempel waktu rapat tanpa menit hilang, checksum cocok, namun
  `volume` dan `count` nol pada SELURUH lilin.
  - Bentangan jurnal 74: 864.000 lilin pada 20 simbol-bulan. Jurnal 77: 169 dari
    179 simbol-bulan sepi pada 10 simbol. Kohort [v29]: **456 dari 456**.
  - **BENTANGAN SEMESTA [v30]:** dari **19.586** simbol-bulan lolos gerbang,
    **1.401 MATI** (7,153%), **98 SEPI** (0,500%), **18.087 HIDUP** (92,35%).
  - **945 simbol-bulan MATI berada di luar kohort puncak.**
  - **BUKAN CACAT ARSIP FUNDING [v31]:** dari 1.401 MATI, **842** kehilangan
    funding dan **559 tetap punya funding**.
  - **KEMATIAN DAPAT BERBALIK [v34, DIKOREKSI v35].** LITUSDT MATI **2025-02**
    sampai 2025-11 (10 bulan) lalu HIDUP kembali 2026-01..2026-06. Status
    kehidupan WAJIB dipakai per SIMBOL-BULAN.
  - **KEBANGKITAN PUNYA DELAPAN CONTOH [v35]:** CTKUSDT, CVCUSDT, CVXUSDT,
    ICPUSDT, LITUSDT, MAVIAUSDT, SLPUSDT, TLMUSDT. H-A012 MENANG.
  - **DAN KEMATIAN PERMANEN JUGA PUNYA CONTOH TELAK [v35]:** BTCSTUSDT **53 dari
    53** bulan MATI sesudah funding-nya PULIH pada 2022-02. Jadi kembalinya
    funding BUKAN penanda kebangkitan.
  - Ekstrapolasi dari kohort ke semesta TERBUKTI keliru arah. Aturan 39 dibenarkan.
  - **Kebijakan DIPUTUSKAN [v28] oleh ADR-A008** (Keputusan 1–6 DITERIMA):
    KC-18 bukan gerbang serapan; kehidupan diukur per simbol-bulan; **SEPI** bila
    `bagian_volume_nol` ≥ 0,5 dan **MATI** bila `transaksi_total` = 0; setiap
    penyebut diterbitkan berpasangan; backtest hanya pada simbol-bulan HIDUP;
    angka 839.842.134 tidak ditulis ulang (aturan 29). Keputusan 7 DITANGGUHKAN.
- **KC-19 [v32] — mencacah dari INGATAN atas berkas yang baru saya tulis
  sendiri.** R-148, R-211, dan R-217 gugur dengan sebab yang persis sama.
  Penangkalnya aturan 57. **TIDAK TERULANG TIGA KALI [v35]:** R-221 (382),
  R-228 (396), R-232 (**450**) tepat pada percobaan pertama.
- **KC-20 [v33] — taksiran cacah baris bias sistematis ke BAWAH.** R-175 (..680
  vs 705), R-179 (..700 vs 705), R-203 (..400 vs 417), R-225 (..620 vs 705) —
  empat dari empat ke arah yang sama. Ramalan atas berkas yang dibaca ulang utuh
  lebih dahulu TEPAT tiga dari tiga (R-213, R-214, R-224). Penangkalnya aturan 58.
- **KC-21 [v34] — menyimpulkan KETIADAAN sebuah gejala dari ketiadaan
  PENGUKURANNYA.** Lahir dari R-230: `cacah_simbol_bangkit_dapat_diuji` = 0
  dipakai sebagai bukti bahwa kebangkitan tidak ada. Nol yang tidak mampu
  membedakan bukan bukti; ia ketidaktahuan yang rapi. Penangkalnya aturan 59.
  **[v35] Bentangannya kini terukur: bukan satu kebangkitan yang terlewat,
  melainkan DELAPAN.**
- **KC-22 [v35, lahir dari R-234] — memindahkan MEKANISME dari satu kasus yang
  menang ke kasus lain.** Praregistrasi R-234 menyebut syarat "bila tafsir
  LITUSDT berlaku umum", tetapi angka yang saya tulis tetap `cacah_hidup` ≥1 —
  syarat bersyarat yang ditulis sebagai ramalan mutlak. BTCSTUSDT menjawab 0 dari
  53. Penangkalnya aturan 60. Cacat PENALARAN, bukan cacat kode.
- **KC-23 [v35, lahir dari koreksi jurnal 91] — memindahkan MEDAN antarjalur.**
  STATE v34 menulis "LITUSDT HIDUP sampai 2025-06" dengan memakai medan
  `funding_sebelum` dari jalur funding sebagai bulan hidup terakhir dari jalur
  kehidupan. Pengukuran langsung: MATI mulai **2025-02**, lima bulan lebih awal.
  Bedanya dengan KC-22: KC-23 memindahkan ANGKA, KC-22 memindahkan SEBAB.
  Penangkalnya aturan 61.

## H-A012 — DIUJI dan MENANG [v35]

Sumber: `lux_ai/serapan/kebangkitan.py` **V1** (blob
**`446321eea09ece50bd0637eb4b0018a4f874ce23`**, `VERSI` 1, `sidik_kode`
**`9d25670cfb7d7ac60a46a8afd22e1eb91caffff919b277d5d26359f386157b48`**), didorong
ATOMIK bersama `tests/test_kebangkitan.py` (blob `1fd006c5`, **54** fungsi
bernomor, nol `parametrize`) dan `.github/workflows/kebangkitan.yml` pada commit
**`bdcbaebc`** (aturan 45). Run **30443289476**, kode 0, `waktu_utc`
2026-07-29T10:20:47Z. Bahan: kedelapan `reports/kehidupan_arsip_<i>.json` +
`reports/funding_semesta.json`; tanpa unduhan.

`cacah_simbol_bangkit` **8**, `cacah_peristiwa` **8**,
`cacah_simbol_bangkit_penuh` **8**, `penyebut_simbol` **787**, `menang` **true**,
`terukur` **true**. 8/787 = **1,02%**; 8/133 simbol bermati = **6,0%**.

| simbol | rentang (bulan) | MATI mulai | MATI terakhir | panjang | HIDUP pertama sesudah | bulan di antara |
|---|---|---|---|---:|---|---|
| CTKUSDT | 2020-11..2026-06 (67) | 2024-05 | 2025-03 | 11 | 2025-05 | **2025-04 tidak ada** |
| CVCUSDT | 2020-11..2026-06 (67) | 2022-12 | 2025-04 | 29 | 2025-06 | **2025-05 tidak ada** |
| CVXUSDT | 2022-09..2026-06 (45) | 2024-06 | 2025-06 | 13 | 2025-08 | **2025-07 tidak ada** |
| ICPUSDT | 2021-05..2026-06 (62) | 2022-07 | 2022-08 | 2 | 2022-09 | — (bersambung) |
| LITUSDT | 2021-02..2026-06 (64) | **2025-02** | 2025-11 | 10 | 2026-01 | **2025-12 tidak ada** |
| MAVIAUSDT | 2024-02..2026-06 (28) | 2025-01 | 2025-02 | 2 | 2025-04 | **2025-03 tidak ada** |
| SLPUSDT | 2023-10..2026-06 (32) | 2024-06 | 2025-06 | 13 | 2025-08 | **2025-07 tidak ada** |
| TLMUSDT | 2021-07..2026-06 (60) | 2022-07 | 2023-02 | 8 | 2023-03 | — (bersambung) |

Kedelapannya `bangkit_penuh` true (ada bulan HIDUP SEBELUM rentetan MATI — tanpa
itu yang terjadi permulaan lambat, bukan kebangkitan), `cacah_peristiwa` **1**
masing-masing, `cacah_bulan_antara` **0**. **Tidak ada simbol yang bangkit dua
kali.** Panjang MATI 2, 2, 8, 10, 11, 13, 13, 29 — jumlah **88** bulan (dihitung
tangan ✅). Jadi **88 dari 1.401** bulan MATI (6,28%) berada dalam rentetan yang
terbukti berakhir; **1.313** sisanya belum terbukti berakhir.

**Pola BARU yang belum pernah terlihat [v35].** Enam dari delapan kebangkitan
dipisahkan oleh **tepat satu bulan kalender yang TIDAK ADA di penyebut 19.586**:
CTK 2025-04 · CVC 2025-05 · CVX 2025-07 · LIT 2025-12 · MAVIA 2025-03 · SLP
2025-07. Dua yang bersambung tanpa lubang adalah **ICPUSDT dan TLMUSDT** — persis
dua simbol H-A010, yang bulan kebangkitannya SAMA dengan bulan berfunding
pertamanya (2022-09 dan 2023-03). Dua dari enam bulan hilang itu adalah
**2025-07**, bulan tebing funding dan bulan kohort puncak.

**Yang TIDAK boleh disimpulkan (aturan 10, 46, 59).** `cacah_bulan_antara` 0
berarti tidak ada bulan TERUKUR di antaranya, BUKAN bahwa tidak ada apa-apa di
sana. Belum diukur: apakah keenam bulan itu (a) tidak diterbitkan arsip,
(b) diterbitkan tetapi gagal gerbang 1m, atau (c) masuk 12 simbol-bulan
karantina. Sebab kebangkitan juga tidak terjangkau: pendaftaran ulang, perubahan
rezim penerbitan arsip, dan pemulihan minat pasar sama-sama menghasilkan pola
MATI lalu HIDUP.

## BTCSTUSDT — bentuk TENGAH yang BUKAN kebangkitan [v35]

Diuji lewat `lubang_tengah.uji_h_a011(status, simbol="BTCSTUSDT",
rentang=("2022-02","2026-06"))` — definisi SATU, tidak disalin ulang (aturan 36).

| medan | nilai |
| --- | ---: |
| `btcst_cacah_bulan` | **53** |
| `btcst_cacah_bulan_kalender` | **53** |
| `btcst_cacah_hidup` | **0** |
| `btcst_menang` | **false** |
| `btcst_terukur` | **true** |
| `sebaran_status` | MATI **53** · SEPI 0 · HIDUP 0 · TAK_TERUKUR 0 |

Funding BTCSTUSDT hilang satu bulan (2022-01) lalu **PULIH** pada 2022-02 —
sesudah itu pasarnya MATI 53 bulan berturut tanpa satu pun bulan HIDUP, dan ia
pemegang rekor semesta dengan **63** bulan MATI.

**Kesimpulan yang WAJIB dibawa ke Keputusan 7 ADR-A008: bentuk lubang funding
TENGAH punya DUA sebab yang berlawanan.** LITUSDT — funding kembali, pasar hidup
kembali. BTCSTUSDT — funding kembali, pasar tetap mati. Kembalinya funding BUKAN
penanda kebangkitan; penerbitan funding dapat pulih TANPA perdagangan, yang
persis bunyi KC-18 pada jalur funding. KC-18 menang atas tafsir v34.

**Koreksi tersurat atas v34 (aturan 29, tanpa menghapus jejaknya).** v34 menulis
bahwa pada LITUSDT "funding dan perdagangan berhenti serta pulih BERSAMA".
Separuh kalimat itu BATAL: perdagangan berhenti 2025-02, funding hilang 2025-07 —
selisih **lima bulan**. Hanya ujung kebangkitannya yang bertemu. Lubang funding
tengah MENYUSUL kematian, tidak menandainya.

## Sebaran 1.401 MATI menurut TAHUN dan SIMBOL — TERUKUR [v35]

| tahun | simbol-bulan MATI |
| --- | ---: |
| 2020 | 1 |
| 2021 | 9 |
| 2022 | 34 |
| 2023 | 103 |
| 2024 | 192 |
| 2025 | 506 |
| 2026 | **556** (hanya 6 bulan) |

1+9+34+103+192+506+556 = **1.401** ✅ (`cacah_tahun_bermati` 7). Laju 2026 =
92,7/bulan lawan 42,2/bulan pada 2025. **PENYEBUT PER TAHUN BELUM DIUKUR**, jadi
ketujuh angka ini masih pembilang tanpa penyebut dan DILARANG dibaca sebagai laju
kematian relatif (aturan 30).

**133 simbol** dari 787 (16,9%) punya ≥1 bulan MATI (`cacah_simbol_bermati` 133).
Dua puluh teratas (`cacah_teratas` 20): BTCSTUSDT **63** · SCUSDT 48 · FTTUSDT 43 ·
RAYUSDT 43 · CVCUSDT **29** · STRAXUSDT 27 · DGBUSDT 26 · GLMRUSDT 25 · IDEXUSDT
25 · MDTUSDT 25 · RADUSDT 25 · SNTUSDT 25 · STPTUSDT 25 · AGIXUSDT 24 · OCEANUSDT
24 · WAVESUSDT 24 · BTSUSDT 21 · KLAYUSDT 20 · UNFIUSDT 20 · BLZUSDT 18.

CVCUSDT ada di kedua daftar: 29 bulan MATI **dan** bangkit penuh — dan rentetan
MATI-nya juga 29, jadi seluruh kematiannya bersambung dalam satu rentetan tunggal.
ICPUSDT dan TLMUSDT bangkit sekaligus pemilik lubang AWAL (H-A010).

**Pencocokan `bulan_hidup_terakhir` dengan `kohort_ekor` V4:** `cacah_cocok`
**10 dari 10**, `cacah_beda` **0**, `cacah_hilang` **0**, `seluruhnya_cocok`
true — AGIX 2024-06, ALPACA 2025-04, AMB 2025-02, BADGER 2025-03, BAL 2025-03,
BLZ 2024-12, BNX 2025-03, BOND 2024-11, COMBO 2025-03, DAR 2024-12. Kekhawatiran
bahwa jendela mundur `kohort_ekor` menggeser angka TIDAK terbukti; yang salah pada
V4 hanya klaim "nol kebangkitan", bukan bulan hidup terakhirnya.

Penggugur bersih `kebangkitan` V1: `selisih_penyebut` **0** (19.586),
`selisih_mati` **0** (1.401), `sidik_seragam` **true**, `sidik_kode_laporan`
tunggal `24b6bb26…c595`, `cacah_laporan_dibaca` **8**, `laporan_hilang` **[]**,
`cacah_kunci_ganda` 0, `cacah_lubang_ganda` 0, `cacah_lubang_funding` **880**,
`kendali_sah` **true**, `kode_keluar` **0**.

## H-A011 — DIUJI dan MENANG 6–0 [v34]

Sumber: `lubang_tengah.py` **V2** (blob **`4d3beaf1`**, `sidik_kode`
**`c9372bd763b86cfeb2adcf0a0c0c43dae8d9aa9a6508e9c32f7671d5ec7b3f4e`**), commit
**`be5cd877`**, run **30440471508**, kode 0. LITUSDT 2026-01..2026-06 seluruhnya
**HIDUP**: `cacah_bulan` 6, `cacah_hidup` 6, `terukur` true, `h_a011_menang` true.
Penggugur bersih: `selisih_lubang_tengah` **0**, `cacah_lubang_tengah` **6**,
`sebaran_status_lubang_tengah` {MATI 6, SEPI 0, HIDUP 0, TAK_TERUKUR 0},
`cacah_lubang_funding` 880, `penyebut_kehidupan` 19.586, `kendali_sah` true.

**Batas yang kini terlihat [v35]:** kemenangan ini sah untuk LITUSDT dan HANYA
untuk LITUSDT. Rentetan yang sama pada BTCSTUSDT memberi jawaban berlawanan, dan
kronologi LITUSDT sendiri ternyata lima bulan lebih panjang daripada yang v34
tulis.

## Keenam lubang funding TENGAH — BERNAMA [v33]

| simbol | bulan | funding sebelum | funding sesudah | rentetan | status | cacah_lilin | byte parquet |
|---|---|---|---|---:|---|---:|---:|
| BTCSTUSDT | 2022-01 | 2021-12 | 2022-02 | 1 | MATI | 44.640 | 399.757 |
| LITUSDT | 2025-07 | 2025-06 | 2026-01 | 5 | MATI | 44.640 | 427.922 |
| LITUSDT | 2025-08 | 2025-06 | 2026-01 | 5 | MATI | 44.640 | 427.505 |
| LITUSDT | 2025-09 | 2025-06 | 2026-01 | 5 | MATI | 43.200 | 392.233 |
| LITUSDT | 2025-10 | 2025-06 | 2026-01 | 5 | MATI | 44.640 | 434.201 |
| LITUSDT | 2025-11 | 2025-06 | 2026-01 | 5 | MATI | 43.200 | 389.479 |

**PERINGATAN [v35]:** medan `funding sebelum` di tabel ini adalah medan JALUR
FUNDING. Ia BUKAN bulan hidup terakhir (aturan 61, KC-23) — LITUSDT sudah MATI
sejak 2025-02.

BTCSTUSDT: 64 bulan klines (2021-03..2026-06), 1 lubang. LITUSDT: 64 bulan klines
(2021-02..2026-06), 5 lubang. "Enam lubang tengah" adalah enam SIMBOL-BULAN dalam
**DUA** rentetan; keenamnya MATI dan berklines penuh secara bentuk.

**Ketiga bentuk punya penjelasan calon:** ekor = kematian pasar (lubang → mati
96,0%); awal = funding menyusul klines (H-A010 MENANG, definisi TEPAT); tengah =
**DUA sebab berlawanan** (LITUSDT jeda yang berakhir; BTCSTUSDT penerbitan funding
pulih tanpa perdagangan).

## H-A010 — DIUJI, MENANG, dan definisinya kini TEPAT [v34]

| simbol | klines pertama | berfunding pertama | jarak | bulan klines | lubang |
|---|---|---|---:|---:|---:|
| QTUMUSDT | 2020-02 | 2020-03 | 1 | 77 | 1 |
| ICPUSDT | 2021-05 | 2022-09 | 16 | 62 | 16 |
| TLMUSDT | 2021-07 | 2023-03 | 20 | 60 | 20 |
| BNXUSDT | 2022-05 | 2023-02 | 9 | 48 | 19 |
| JUPUSDT | 2024-01 | 2024-02 | 1 | 30 | 1 |

`cacah_menang` **5**, `cacah_gugur` **0**, `h_a010.menang` **true**.
`funding_tanpa_klines` KOSONG pada kelimanya (`ada_medan` true 5/5, `cacah_bulan`
0, `kosong_seluruhnya` true), jadi definisi turunan "bulan berfunding pertama"
bukan hanya memadai melainkan **TEPAT**. **[v35] Sambungan baru:** bulan
berfunding pertama ICPUSDT (2022-09) dan TLMUSDT (2023-03) SAMA dengan bulan
kebangkitannya — satu-satunya dua kebangkitan yang tidak dipisahkan bulan hilang.

## Daftar 33 HIDUP tanpa funding dan 3 lubang tak dikenal — TERBIT [v32]

**Sebaran bentuk ke-33: awal 33 · ekor 0 · tengah 0 · seluruh 0.**

| simbol | cacah | bulan | lubang simbol | bulan klines simbol |
|---|---:|---|---:|---:|
| ICPUSDT | 13 | 2021-05..2022-05 | 16 | 62 |
| TLMUSDT | 11 | 2021-07..2022-05 | 20 | 60 |
| BNXUSDT | 7 | 2022-05, -07, -09, -10, -11, -12, 2023-01 | 19 | 48 |
| JUPUSDT | 1 | 2024-01 | 1 | 30 |
| QTUMUSDT | 1 | 2020-02 | 1 | 77 |

13+11+7+1+1 = **33** ✅ **Tiga lubang tak dikenal: BNXUSDT 2022-04, 2022-06,
2022-08** — ketiganya `simbol_dikenal` true.

**Definisi `bentuk_lubang_lokal` (aturan 36):** lokal atas 877 lubang di dalam
penyebut = awal **45** + ekor **826** + tengah **6** = **877** ✅ terbitan
`funding.py` atas 880 = awal **48** + ekor 826 + tengah 6; selisih 48 − 45 = **3**
= ketiga lubang BNXUSDT di luar penyebut ✅

**Medan baris laporan kehidupan** (14 medan): `ada_di_arsip`, `bagian_volume_nol`,
`bulan`, `byte_parquet`, `cacah_baris_cacat`, `cacah_lilin`, `cacah_lilin_terbaca`,
`cacah_volume_nol`, `galat`, `gerbang_lolos`, `jalur`, `simbol`, `status`,
`transaksi_total`. `cacah_baris_dengan_medan` = **19.586**.

## Silang funding × kehidupan — TERUKUR [v31]

Penyebut: **19.586** simbol-bulan lolos gerbang (aturan 30, 44).

| status | funding ADA | funding HILANG | jumlah |
|---|---:|---:|---:|
| MATI | 559 | **842** | 1.401 |
| SEPI | 96 | 2 | 98 |
| HIDUP | 18.054 | **33** | 18.087 |
| TAK TERUKUR | 0 | 0 | 0 |
| **jumlah** | **18.709** | **877** | **19.586** |

- 559+96+18.054 = **18.709** ✅ 842+2+33 = **877** ✅ jumlah **19.586** ✅
- 877 + **3** lubang tak dikenal = **880** ✅ (BNXUSDT 2022-04, -06, -08).
- Kohort puncak: **456/456** MATI dan berlubang ✅ Di luar kohort: 945 MATI =
  **386** berlubang + **559** berfunding ✅ `bagian` 386/945 = **0,4085**.

**Dua arah wajib dipisah:** lubang → mati **kuat** (842/877 = **96,0%**); mati →
lubang **lemah** (842/1.401 = **60,1%**). Lubang funding TIDAK sah dipakai sebagai
penyaring kematian. Irisan bukan sebab (aturan 10).

## Kehidupan semesta terserap — TERUKUR [v30]

`kehidupan_arsip.py` V1 (`sidik_kode`
**`24b6bb265525e81c2e571b46e401f36903383f1e3738c487850861adc3e8c595`**), commit
`0929643c`, run pecahan 0 = **30419770259**. Sidik kode SAMA di kedelapan laporan.

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

- 1.401+98+18.087 = **19.586** ✅ 19.586 − 1.401 = **18.185** ✅
- Jumlah `lilin_penuh` **839.325.999** cocok PERSIS dengan baris lolos gerbang
  yang diukur serapan (run `30396803601`) lewat jalur kode berbeda.
- Lilin mati 61.168.123 = **7,29%**; MATI + SEPI = 1.499 = **7,654%**.

Penggugur bersih di kedelapan pecahan: `cacah_tak_terukur` 0, `cacah_baris_cacat`
**0** dari 839 juta baris, `cacah_parquet_hilang` 0, `cacah_sha_tak_cocok` 0,
`kode_keluar` 0. Kendali positif: **24 dari 24 HIDUP**, `parser_terbukti` true.

Yang TIDAK BOLEH: memakai 7,153% sebagai laju kematian simbol mana pun —
sebarannya 4,18% sampai 13,14%, dan pecahan dibagi menurut simbol. **[v34–v35]**
dan tidak boleh dipakai sebagai laju kematian PERMANEN: 88 bulan MATI terbukti
berakhir dengan kebangkitan.

## Kehidupan kohort puncak 2025-07 — TERUKUR [v29]

`kehidupan.py` V1 (417 baris). Run **30418471430**, commit `d4a2f60a`, kode 0.
38 simbol · 456/456 simbol-bulan terukur · MATI **456** · HIDUP **0** · lilin
19.972.800 (38 × 525.600 ✅) · penyebut tanpa MATI **0** · kendali 4/4 HIDUP.
Kohort puncak menyumbang **nol** simbol-bulan layak backtest.

## Hipotesis

- H-A001: belum diuji.
- H-A002a / H-A002b: H-A002b **GUGUR**.
- **H-A003: MENANG pada 3, GUGUR pada 9.**
- **H-A004: TIDAK TERUJI dan tidak dapat diuji** (`fapi.binance.com` → 451).
- **H-A005: GUGUR pada rentang yang disampel [v23].**
- **H-A006 — serapan deterministik. MENANG pada ENAM run.**
- **H-A008 — aset rilis GitHub mengembalikan byte sama persis. MENANG dua kali.**
- **H-A009 — lubang funding dan kematian pasar satu gejala. GUGUR:** 559
  simbol-bulan MATI tetap berfunding.
- **H-A010 — penerbitan funding MENYUSUL klines bagi sebagian simbol. MENANG
  5–0**, definisi kini TEPAT.
- **H-A011 — jeda funding TENGAH menandai pasar yang berhenti diperdagangkan lalu
  terdaftar ulang. MENANG 6–0 pada LITUSDT**, dan **DIBATASI [v35]:** rentetan
  serupa pada BTCSTUSDT memberi 0 HIDUP dari 53, jadi kemenangan ini tidak boleh
  digeneralisasi (aturan 60).
- **H-A012 [v34 lahir, v35 DIUJI] — kebangkitan bukan peristiwa tunggal. MENANG:**
  **8** simbol dari 787, kedelapannya `bangkit_penuh`, `cacah_peristiwa` 8. Uji
  dirancang dapat gugur: satu simbol saja berarti LITUSDT tetap tunggal.
- **H-A013 [v35, LAHIR, BELUM DIUJI] — bulan peralihan sebuah kebangkitan
  cenderung TIDAK ADA di penyebut.** Terlihat pada 6 dari 8; dua pengecualiannya
  simbol H-A010. Uji: periksa keenam bulan itu di manifes serapan dan daftar
  karantina — ada dan gagal gerbang, atau memang tidak diterbitkan arsip? Tanpa
  unduhan. Aturan 59 wajib ditaati: penyebutnya 8, kecil.

## Papan skor prediksi

R-1..R-120 dirinci v23. R-121..R-149 di v26 dan jurnal 56–63. R-150..R-193 di
jurnal 64–75. R-194..R-199 di jurnal 76–78. R-200..R-204 di jurnal 79–81.
R-205..R-208 di docstring `0929643c` dan `dceb1009`. R-209 di jurnal 82.
R-210..R-211 di docstring `1b0e8d8e`. R-212 di jurnal 83. R-213..R-215 di
docstring `67ec2be4`. R-216 di jurnal 84. R-217..R-219 di docstring `b1816ddf`.
R-220 di jurnal 86. R-221..R-223 di docstring `680d04b4`. R-224..R-226 di
docstring `85079ffd`. R-227 di PROMPT v36 (`a9e91bcd`). R-228..R-230 di docstring
`be5cd877`; adjudikasinya di jurnal 89. **R-231 di PROMPT v37 (`63fc2e8f`).**
**R-232..R-235 di docstring `bdcbaebc`; adjudikasinya di jurnal 90.**

| # | Prediksi | Status |
|---|---|---|
| R-199 | `definisi_dapat_dibedakan` false pada TEPAT 2 pecahan (2 dan 5) | **MENUNGGU** |
| R-225 | `silang_funding.py` V2 pita 470..620 BARIS | **MELESET** (705) |
| R-226 | CI tetap 382 butir, kode 0, pada commit `ukur_baris` V4 | **TEPAT** |
| R-227 | CI 382 butir, kode 0, pada commit PROMPT v36 | **TEPAT** (`30437620711`) |
| R-228 | CI **396 butir** (382 − 42 + 56), kode 0 | **TEPAT** (`30440471598`) |
| R-229 | `funding_tanpa_klines` KOSONG pada kelima simbol H-A010 | **TEPAT** |
| R-230 | H-A011 GUGUR: keenam bulan LITUSDT 2026 tetap MATI | **MELESET** (6/6 HIDUP) |
| R-231 | CI **396 butir**, kode 0, pada commit PROMPT v37 | **TEPAT** (`30442623074`, `63fc2e8f`) |
| R-232 | CI **450 butir** (396 + 54), kode 0, pada commit trio `kebangkitan` | **TEPAT** (`30443289417`) |
| R-233 | H-A012 MENANG, `cacah_simbol_bangkit` pada pita **2..80** dari 787 | **TEPAT** (8) |
| R-234 | BTCSTUSDT 53 bulan DAN `btcst_cacah_hidup` ≥ 1 | **SEPARUH** (53 ✅, 0 HIDUP ❌) |
| R-235 | cocok `kohort_ekor` pita 6..10 DAN `cacah_hilang` 0 | **TEPAT** (10/10) |

**Total R-1..R-235** (aturan 21): TEPAT **165**; MELESET **42**; SEPARUH **14**;
TIDAK TERADJUDIKASI **7**; MENUNGGU **7** (R-7, R-19, R-20, R-28, R-36, R-37,
R-199). 165+42 = 207; +14 = 221; +7 = 228; +7 = **235** ✅ Ramalan berikutnya
**R-236**. N_percobaan = 0.

**KOREKSI CACAH [v35].** Jurnal 90 menulis total **234** dengan TEPAT 164, karena
R-231 (dipraregistrasi di PROMPT v37, bukan di docstring) terlewat dari daftar.
R-231 kini diadjudikasi **TEPAT** lewat ref `acd79d41`, sehingga total yang benar
**235** dan TEPAT **165**. Angka jurnal 90 tidak disunting; koreksinya ditulis di
sini (aturan 29). Pelajaran: ramalan yang dipraregistrasi di PROMPT mudah
terlewat — setiap praregistrasi wajib disalin ke papan skor pada pembaruan STATE
berikutnya.

Catatan kejujuran: R-234 adalah kekalahan kedua yang berharga setelah R-230, dan
keduanya berlawanan arah — R-230 menegaskan KETIADAAN gejala, R-234 memindahkan
SEBAB dari kasus yang menang. Angka keduanya tidak disunting. R-235 TEPAT atas
pita LEBAR (6..10 dari 10) sehingga bukan kecakapan meramal. R-175, R-179, R-203,
dan R-225 adalah SATU pola bernama KC-20. R-205 melahirkan aturan 53; R-211
aturan 54; R-209/R-212 aturan 55; R-216 aturan 56; R-217 aturan 57 dan KC-19;
R-225 aturan 58 dan KC-20; R-230 aturan 59 dan KC-21; **R-234 aturan 60 dan
KC-22**; koreksi kronologi LITUSDT melahirkan **aturan 61 dan KC-23**.

**R-236, dipraregistrasi di sini (aturan 26, 38, 55, 56).** Pada commit BERIKUTNYA
yang menyentuh `STATE.md` — yakni commit yang memuat berkas ini — `ci.yml` MENYALA
(berkas ada di akar, tidak tersentuh `paths-ignore`), dan `reports/ci_terakhir.json`
akan melaporkan **450 butir** dengan `kode_keluar` **0**. Dasarnya: tidak ada
berkas uji maupun modul yang berubah pada commit ini, dan 450 sudah terverifikasi
pada run 30443289417. Aturan 57 tidak perlu daftar bernomor sebab angkanya diambil
dari laporan CI terverifikasi, bukan dari cacahan sendiri.

## Cacah baris terukur [v33] — `ukur_baris` V4

Sumber: `reports/ukur_baris.json` V4 (blob `6f9c5420`), commit `85079ffd`, run
**30436915256**, kode 0. Penggugur bersih: `cacah_berkas_hilang` 0,
`cacah_berkas_melebihi_pagar` **0**, `cacah_berkas_ada` 13 dari 13. Definisi
`len(teks.splitlines())`.

| berkas | baris | byte |
| --- | ---: | ---: |
| `funding.py` | **705** | 28.121 |
| `silang_funding.py` V2 | **705** | 29.873 |
| `kohort_ekor.py` | 553 | 22.590 |
| `kehidupan_arsip.py` | 496 | 19.281 |
| `kehidupan.py` | 417 | 16.638 |
| `lubang_tengah.py` V1 | **390** | 15.883 |
| `pulihkan.py` V2 | 383 | 14.839 |
| `ukur_baris.py` V4 | 280 | 13.354 |
| `gerbang_1m.py` | 184 | 6.775 |
| `funding_cdn.py` | 162 | 6.335 |
| `arsip.py` | 154 | 5.231 |
| `resample.py` | 127 | 4.356 |
| `kohort_ringkas.py` | 82 | 2.882 |

Total **4.638** baris ✅ terbesar **705, SERI**. **Aturan 48 berlaku atas
KEDUANYA.**

**BELUM DIUKUR [v35]:** `lubang_tengah.py` **V2**, `kebangkitan.py` **V1**,
`tests/test_lubang_tengah.py` (56 fungsi), `tests/test_kebangkitan.py` (54
fungsi). Tidak diramalkan dengan pita sempit — aturan 58 pilihan (c). `ukur_baris`
V5 wajib memuat kedua modul baru.

**Angka kedaluwarsa yang MATI:** `ukur_baris.py` 183 dan 226 BATAL → **280**;
`silang_funding.py` 396 BATAL → **705**; `pulihkan.py` 318 BATAL → 383;
`lubang_tengah.py` 390 berlaku hanya untuk **V1**.

## Definisi `jumlah_baris` — TERSELESAIKAN [v26], DITEGAKKAN DI KODE [v28]

**`jumlah_baris` di manifes = baris lolos gerbang + baris karantina.**
Baris lolos gerbang saja **839.325.999**; baris karantina **516.135**; jumlah
**839.842.134** = angka semesta. Konsekuensi ADR-A007: baris hasil pemulihan
harian tidak boleh dijumlahkan tanpa lebih dulu mengurangi baris karantina yang
digantikannya (kendala R-146).

**Peringatan membaca laporan:** `reports/pulihkan_pecahan_<i>.json` di git masih
HASIL V1; label keliru pada pecahan 2 dan 5 masih terbaca di sana. Cocokkan
`versi_pulihkan` dan `sidik_kode`.

## Serapan semesta `perpetual_usdt` — TERUKUR, TERPERSISTENSI, TERPULIHKAN

Sumber serapan: run **`30396803601`**, commit `57a04f1e`, `versi_pecahan` **6**,
`sidik_kode` `237ccf42…`, `sidik_data` `6128fbb0…`. Pemulihan: run
**`30404071324`**, commit `ab4e0774`.

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
- **Pemulihan:** 29/29 aset hadir, 29/29 sha cocok, 839.842.134 baris terbaca
  ulang oleh pyarrow. Tag rilis: `serapan-pecahan-<i>-30396803601`.
- **Penyebut ganda LENGKAP:** PENUH **19.586** lolos gerbang (19.598 termasuk
  karantina); TANPA MATI **18.185**; LAYAK BACKTEST (HIDUP saja) **18.087**.
  Ke-18.087 memuat keenam bulan 2026 LITUSDT dan MENOLAK bulan-bulan MATI-nya —
  penyaringan per SIMBOL-BULAN benar oleh contoh. **[v35] Kini ada delapan
  contoh, bukan satu.**

## Funding semesta — TERUKUR (`funding.py` V6)

Run FUNDING 6 `30412188715`, commit `ba37c5d5`, kode 0. `sidik_kode`
`d3854823…`, `sidik_data` `6128fbb0…`.

- 880 bulan klines tanpa funding; 87 funding tanpa klines; penyebut 19.598.
- Bentuk lubang: {awal 48, ekor 826, tengah 6, hilang 880}. 116 simbol berlubang
  ekor (14,74% dari 787).
- **Kohort puncak 2025-07: 38 simbol, 456 simbol-bulan**, `seri` false; 456 =
  51,8% dari 880. Ke-456 simbol-bulan itu MATI.
- `uji_cdn`: 10 kohort menjawab **404**, 10 kendali menjawab **200** dengan
  checksum cocok.
- Pembagian 880 menurut status: 842 MATI + 2 SEPI + 33 HIDUP + 3 di luar penyebut
  = 880 ✅
- **Ketiga bentuk terjelaskan calon [v33–v35]:** 33 dari 48 lubang AWAL = pasar
  HIDUP yang funding-nya menyusul; 826 EKOR = kematian pasar; 6 TENGAH = dua
  rentetan dengan **dua sebab berlawanan**. Sisa 15 lubang awal jatuh pada bulan
  MATI atau SEPI.
- `per_simbol` memuat **10 medan**, tanpa `bulan_funding_pertama`;
  `funding_tanpa_klines` ADA dan sudah dipakai.

## Kohort ekor — kematian bertahap lawan tebing serempak [v27]

`kohort_ekor.py` V4 (`73ca4eb2…0fcda`, run `30416845475`, commit `387037a9`,
kode 0): pindaian ADAPTIF, pagu keras 60 bulan, pagu tak pernah tersentuh.
`kohort_ekor.bagian` MEMBULATKAN ke empat desimal (aturan 53); TIDAK diubah.

| simbol | bulan hidup terakhir | simbol | bulan hidup terakhir |
| --- | --- | --- | --- |
| AGIXUSDT | 2024-06 | BLZUSDT | 2024-12 |
| ALPACAUSDT | 2025-04 | BNXUSDT | 2025-03 |
| AMBUSDT | 2025-02 | BONDUSDT | 2024-11 |
| BADGERUSDT | 2025-03 | COMBOUSDT | 2025-03 |
| BALUSDT | 2025-03 | DARUSDT | 2024-12 |

Kesepuluhnya berhenti SEBELUM tebing funding 2025-07, tersebar pada sembilan bulan
berbeda. **DIKUATKAN [v35]:** `kebangkitan` V1 menghitung ulang kesepuluh angka ini
dengan definisi BERBEDA (bulan HIDUP terbesar di dalam penyebut, bukan pindaian
mundur) dan mendapat **10 dari 10 sama**.

**DIKOREKSI [v34]:** `bangkit_kembali` 0 pada laporan ini TIDAK berarti tidak ada
kebangkitan; `cacah_simbol_bangkit_dapat_diuji` = **0**. **[v35] Bentangannya
terukur: delapan kebangkitan terlewat, dan tak satu pun di antara kesepuluh simbol
ini.** Yang TIDAK dibuktikan: 28 anggota sisanya (aturan 20). ADR-A002 §10 tidak
boleh diubah atas bukti kohort semata.

## Jumlah uji

**450 TERVERIFIKASI [v35]** — `reports/ci_terakhir.json` (blob `116ff302`) run
**30443289417**, commit `bdcbaebc`, `kode_keluar` **0**, "450 tests collected in
0.44s". Sebelumnya 396 pada run **30442623074** (commit `63fc2e8f`, blob
`3e3d127d`), 396 pada run 30442464855 (`e11750cb`), dan 396 pada run 30440471598
(`be5cd877`). Riwayat: 231 → 234 → 236 → 239 → 241 → 244 → 253 → 269 → 291 → 316 →
340 → 382 → 382 → 396 → 396 → 396 → **450**.
`tests/test_kebangkitan.py` menyumbang **54 butir** (54 fungsi `def test_`, nol
`parametrize`, dicacah BERNOMOR sebelum push): 396 + 54 = **450** ✅
`tests/test_lubang_tengah.py` V2 menyumbang 56; `tests/test_silang_funding.py` 49.

## Utang verifikasi

1-5 dan 11 menunggu tahap juri/klasifikasi. 6-23, 25-28 LUNAS.

24. **AKTIF.**
    - persistensi data lolos dan karantina: **LUNAS**;
    - pemulihan aset di luar runner: **LUNAS**;
    - perbaikan aturan 46 di `pulihkan.py`: **LUNAS DI KODE** (V2) — laporan
      pecahan di git masih hasil V1;
    - bentangan penuh KC-18 atas kohort dan atas SEMESTA: **LUNAS**;
    - penyebut kedua atas semesta: **LUNAS**;
    - daftar 33 HIDUP tanpa funding dan 3 lubang di luar penyebut: **LUNAS [v32]**;
    - nama keenam lubang TENGAH: **LUNAS [v33]**;
    - uji H-A010 dan `funding_tanpa_klines`: **LUNAS [v33–v34]**;
    - status LITUSDT 2026 (H-A011): **LUNAS [v34]**;
    - salah tulis "simbal": **LUNAS [v34]**;
    - **status BTCSTUSDT 2022-02..2026-06: LUNAS [v35]** — 53/53 MATI, bukan
      kebangkitan;
    - **pindaian kebangkitan SELURUH semesta (H-A012): LUNAS [v35]** — 8 simbol;
    - **sebaran 1.401 MATI menurut TAHUN dan SIMBOL: LUNAS [v35]** — 7 tahun,
      133 simbol, 20 teratas;
    - **pencocokan `bulan_hidup_terakhir` dengan `kohort_ekor`: LUNAS [v35]** —
      10/10;
    - **penyebut simbol-bulan PER TAHUN: BELUM [v35]** — tanpa itu ketujuh angka
      MATI per tahun hanya pembilang;
    - **keberadaan keenam bulan peralihan (H-A013): BELUM [v35]**;
    - **cacah baris `lubang_tengah.py` V2, `kebangkitan.py` V1, dan kedua berkas
      ujinya: BELUM**;
    - **pemecahan `silang_funding.py` (705 baris, aturan 48): BELUM**;
    - cacat penulisan docstring R-225 ("tujuh fungsi" lalu sembilan nama):
      dicatat, TIDAK disunting; jumlah yang benar sembilan;
    - pencocokan 3 lubang BNXUSDT dengan 12 simbol-bulan karantina: BELUM;
    - kehidupan 12 simbol-bulan karantina: BELUM (tar terpisah);
    - jalur **funding**: `funding_ada` masih null di seluruh manifes — BELUM;
    - medan `dugaan_pengganti` (ADR-A005) — BELUM;
    - pemulihan harian ADR-A007 — BELUM, bahan baku sudah ada;
    - karantina artefak 7 hari — BELUM;
    - 28 anggota kohort yang belum disampel `kohort_ekor` — BELUM (dan kini
      diketahui tak satu pun dari 10 yang disampel pernah bangkit).
    Mengadjudikasi R-7, R-19, R-20, R-28, R-36, R-37.

## Daftar ADR

- ADR-A001 aturan dasar. DITERIMA.
- ADR-A002 serapan. DITERIMA; §3 DIAMANDEMEN oleh ADR-A004 lalu ADR-A007; §9
  DIGANTI oleh ADR-A006 Keputusan 3. **§10 belum disentuh dan tetap tidak boleh
  disentuh:** ketiga bentuk lubang punya penjelasan calon yang TIDAK menuduh arsip
  funding cacat — pada BTCSTUSDT funding bahkan terus terbit sepanjang 53 bulan
  kematian, perilaku arsip yang jujur sampai membosankan.
- ADR-A003 taksonomi rezim. BELUM ADA (nomor dicadangkan). **[v35] Delapan
  kebangkitan menyentuh langsung nomor ini: rezim sebuah simbol tidak monoton dan
  dapat kembali.**
- ADR-A004 kebijakan KC-6. DITERIMA.
- ADR-A005 jenis instrumen tahap pertama. DITERIMA.
- ADR-A006 karantina + persistensi. DITERIMA, DITERAPKAN, TERVERIFIKASI DARI LUAR.
- **ADR-A007 serapan hibrida. DIUSULKAN**, belum diterima. Wajib memperhitungkan
  temuan `jumlah_baris` dan kendala R-146.
- **ADR-A008 akibat KC-18. DITERIMA [v28] untuk Keputusan 1–6**; Keputusan 2–4
  TERTERAP atas SELURUH semesta; Keputusan 5 bersemesta **18.087** dan terbukti
  benar oleh delapan contoh. **Keputusan 7: bahannya LENGKAP dan BERCABANG DUA
  [v35]** — bentuk TENGAH dapat menandai jeda yang berakhir (LITUSDT) ATAU
  penerbitan funding yang pulih tanpa perdagangan (BTCSTUSDT, 53/53 MATI).
  Keputusannya WAJIB memuat kedua cabang, WAJIB per simbol-bulan, dan DILARANG
  menyebut funding dan perdagangan berhenti "serentak" (koreksi jurnal 91).
  Klausa gugur §6 diperiksa dan tidak aktif pada seluruh run.
- ADR berikutnya **A009**.

## Temuan sampingan yang belum diukur

- **Penyebut simbol-bulan per TAHUN** — tanpa itu 1 · 9 · 34 · 103 · 192 · 506 ·
  556 hanya pembilang. Murah: kedelapan laporan kehidupan sudah di-commit.
- **Keenam bulan peralihan (H-A013):** CTK 2025-04, CVC 2025-05, CVX 2025-07,
  LIT 2025-12, MAVIA 2025-03, SLP 2025-07 — ada di arsip dan gagal gerbang, masuk
  karantina, atau memang tidak diterbitkan?
- Mengapa dua dari enam bulan peralihan itu jatuh pada **2025-07**, bulan tebing
  funding dan kohort puncak.
- Sebab kebangkitan kedelapan simbol (di luar jangkauan arsip).
- **Apakah 3 lubang BNXUSDT (2022-04, -06, -08) sama dengan 3 simbol-bulan
  KC-15** — keduanya BNXUSDT 2022 dan bercacah 3; wajib dicocokkan.
- Kehidupan 12 simbol-bulan karantina.
- `bulan_hidup_terakhir` bagi 28 anggota kohort di luar sampel abjad.
- 15 `SETTLED` lain: apakah punya pendahulu seperti SXPUSDT?
- Daftar `INDEKS` hanya tiga nama, disusun manual.
- Saham dan komoditas token masih terhitung `perpetual_usdt`.
- `.decode("utf-8","replace")` di `klines` membungkam byte rusak.
- Apakah BUSD/USDC layak digabung dengan USDT.
- Sisa 16 simbol non-ASCII belum diuji langsung (3 sudah).
- Sebab KC-14 (H-A004) tidak dapat diuji. Sebab KC-15 tidak diketahui.
- Selisih penyebut diagnosa KC-15: 38 diperiksa, 41 dirancang.
- `reports/funding_selisih_penuh.json` belum pernah dibaca; `daftar_terpotong`
  masih true (500 dari 880).
- Selisih byte funding AGIXUSDT 531 lawan 529.
- `waktu_utc` runner berjalan lebih dulu daripada jam sesi.
- `tests/test_pulihkan.py` belum pernah dibaca ulang sesudah push.
