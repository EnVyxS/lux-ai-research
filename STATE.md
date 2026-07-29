# STATE — versi 36

Diperbarui: 2026-07-29 (sesi 55). Aturan hanya BERTAMBAH; jangan menulis ulang
dari ingatan. v36 disusun di atas teks v35 yang dibaca langsung dari `main` (blob
**`6523b84f88caa1c61c82bb6c2d50192b772a0a4d`**, dibaca **UTUH** sebelum satu huruf
pun ditulis), ditambah jurnal 92–95, `lux_ai/serapan/bulan_settled.py` V1 (blob
`80e8d8bb`), `reports/bulan_settled_ringkas.json` (blob `df2d2bfa`, 14.413 B,
dibaca UTUH), `reports/bulan_settled_status.json` (blob `4c46e56d`),
`reports/ukur_baris.json` V5 (blob `c8b988ff`, dibaca UTUH),
`reports/ukur_baris_status.json` (blob `e47efe55`), dan
`reports/ci_terakhir.json` (blob `b0e4e1aa`). Run yang dicocokkan commit-nya:
**30448334675** (`9bdab113`, CI **552**), **30448334739** (`9bdab113`,
`bulan_settled` V1), **30451749412** (`404e6f1b`, `ukur_baris` V5), dan
**30451749571** (`404e6f1b`, CI **552**). Semuanya kode 0.

Dua peristiwa terbesar sejak v35:

1. **H-A013 DIUJI dan MENANG 6 dari 6.** Keenam bulan peralihan kebangkitan SAMA
   dengan satu-satunya bulan saudara SETTLED simbol itu. Tafsir "delapan
   kebangkitan" karena itu DILEMAHKAN menjadi **"dua bersambung dan enam
   peralihan nama"**.
2. **Batas semesta akhirnya tersurat.** Penyebut 787 simbol adalah pasangan
   berkuota **USDT SAJA**; semesta arsip **937** simbol dan **21.789** bulan.
   Dua semesta dilarang disilangkan tanpa bukti kesepadanan. Dari sini lahir
   aturan 62 dan 63 serta KC-24 dan KC-25.

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
    uji. Dilanggar pada R-148, R-211, R-217. **Ditaati pada R-198, R-200, R-204,
    R-205, R-208, R-215, R-220, R-221, R-226–R-228, R-231, R-232, R-250, dan
    R-253.** Laporan CI dapat TERTIMPA run berikutnya; bila demikian baca pada
    ref commit yang bersangkutan. **Cara menemukan ref:** `list_commits` dengan
    `path="reports/ci_terakhir.json"` mendaftar tiap commit runner beserta nomor
    run di pesannya (dipakai untuk R-231 dan R-250).
39. **[v22]** Keseragaman terukur pada sampel DILARANG dipakai sebagai angka
    ramalan bagi anggota di luar sampel; wajib pita atau kemungkinan campuran.
40. **[v22]** Tiap laporan yang mencacah baris sebuah simbol-bulan wajib memuat
    uji silang `baris + hilang_di_tengah + tepi = menit_kalender`.
41. **[v23]** Ramalan bersyarat berpenyebut nol dicatat TIDAK TERADJUDIKASI.
42. **[v23]** Kelas cacat baru DILARANG dinamai atas dasar satu angka yang belum
    diukur langsung. **Ditaati pada KC-18, KC-21–KC-26.**
43. **[v24]** Medan penggugur bertoleransi BERSKALA, bukan margin datar.
44. **[v24]** Ramalan wajib menyebut penyebutnya: pecahan mana, semesta mana,
    medan mana. Pita yang hanya masuk akal di bawah satu tafsir → MELESET.
45. **[v25] Keatomikan push pemicu.** Push yang MENYALAKAN run wajib memuat setiap
    berkas yang run itu bergantung padanya. Ditaati pada `bdcbaebc`, `8466396f`,
    `d95c35a5`, `474fa23c`, `9bdab113`, dan **`404e6f1b`** (`ukur_baris` V5 tidak
    memerlukan berkas baru, dan itu diperiksa sebelum push).
46. **[v26, LUNAS DI KODE v28] Kode dilarang menyimpulkan dari penyebut nol.**
    Medan yang MENYIMPULKAN wajib memeriksa lebih dulu apakah kasusnya mampu
    membedakan. Ditaati oleh `kohort_ekor` V4, `kehidupan`, `kehidupan_arsip`,
    `silang_funding`, `lubang_tengah`, `kebangkitan`, `penyebut_tahun`,
    `semesta_silang`, dan **`bulan_settled` V1** (`terukur`,
    `definisi_dapat_dibedakan`). **[v36] Aturan ini baru saja membuktikan
    nilainya ke arah yang tidak nyaman:** `bulan_settled` menang 6–0 tetapi
    melaporkan sendiri `definisi_dapat_dibedakan` **false** — kemenangan yang
    jujur mengaku sempit.
47. **[v27]** Sebutkan satuan cacah secara eksplisit — simbol, bulan,
    simbol-bulan, baris, atau butir uji — dan periksa angka rujukannya bersatuan
    itu.
48. **[v27]** Berkas modul yang mendekati pagar 800 baris harus dipecah SEBELUM
    fungsi baru ditambahkan. **[v36] Berlaku atas DUA berkas, keduanya 705 baris
    dan terukur ulang oleh `ukur_baris` V5:** `funding.py` dan
    `silang_funding.py`. Tidak ada berkas lain yang melewati pagar; tertinggi
    berikutnya `lubang_tengah.py` V2 **560**.
49. **[v27]** Pemecahan berkas yang mempertahankan nama fungsi lewat re-export
    TETAP dapat mematahkan uji. Telusuri nama yang DITAMBAL (`monkeypatch`,
    `patch`, akses atribut modul).
50. **[v27]** Setiap pengukuran yang menyimpulkan dari KETIADAAN wajib memuat
    kendali positif. **[v36] `bulan_settled` V1 bersih:** kendali BTCUSDT
    `cacah_bulan` **78** ≥ ambang **60**, `kendali_sah` true.
51. **[v27]** Jendela pemindaian mundur wajib adaptif atau dibuktikan mencakup
    peristiwa yang dicari.
52. **[v27]** Laporan yang tidak dapat dibaca utuh setara dengan laporan yang
    tidak ada. Ditaati oleh `kohort_ringkas`, `ukur_baris`, `kehidupan`,
    `kehidupan_arsip`, `silang_funding`, `lubang_tengah`, `kebangkitan`,
    `penyebut_tahun`, `semesta_silang`, dan `bulan_settled`. Laporan
    `silang_funding` penuh 183.963 B tetap tak terbaca utuh selamanya.
53. **[v30]** Ramalan kode keluar sebuah run yang gerbangnya berkas uji wajib
    didahului pembacaan PERILAKU setiap fungsi yang diuji.
54. **[v31]** Cacah butir uji dihitung dengan mencacah `def test_` satu per satu
    pada berkas uji yang SUDAH selesai ditulis. TIDAK CUKUP sendiri — lihat 57.
55. **[v31]** Sebelum meramalkan hasil workflow, baca `paths`/`paths-ignore` dan
    sebutkan workflow MANA yang menyala. `ci.yml` mengabaikan `journal/**`,
    `decisions/**`, `hipotesis/**`, `reports/**`. `ukur_baris.yml` menyala HANYA
    atas `lux_ai/serapan/ukur_baris.py`. **Ditaati pada R-253.**
56. **[v32]** Ramalan yang menyebut commit sasaran wajib memakai bentuk yang
    dijamin ada: "commit BERIKUTNYA yang menyentuh `<berkas>`".
57. **[v32]** Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB
    ditulis BERNOMOR, dan nomor terakhirnya dipakai sebagai cacahan. **TERBUKTI
    BEKERJA ENAM DARI ENAM [v36]:** R-221 (382), R-228 (396), R-232 (450),
    R-241 (494), R-245 (526), R-250 (**552**). Mekanismenya deterministik — itu
    sebab keberhasilannya, bukan kecakapan meramal.
58. **[v33]** Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH
    dalam giliran yang sama DILARANG diramalkan dengan pita sempit. Pilih: (a)
    baca ulang utuh; (b) pita dengan batas atas ≥1,8× batas bawah; (c) jangan
    meramal, cukup ukur. **Pilihan (c) dipakai atas seluruh sembilan berkas baru
    di `ukur_baris` V5 [v36]** — dan itu terbukti tepat sebagai kebiasaan:
    taksiran byte akan meleset lagi pada `lubang_tengah.py` V2 (390 → **560**).
59. **[v34]** Ramalan yang menegaskan KETIADAAN gejala wajib menyebut penyebut
    yang mampu memuat gejala itu dan cacah kasus yang pernah diperiksa.
60. **[v35]** Tafsir MEKANISME yang menang pada satu kasus dilarang dipakai
    sebagai dasar ramalan atas kasus lain sebelum penyebutnya ≥2 dan variasinya
    terukur. Lahir dari R-234 (LITUSDT → BTCSTUSDT, 0 dari 53).
61. **[v35]** Nilai sebuah medan dilarang dipakai sebagai nilai medan jalur LAIN
    tanpa membaca laporan jalur itu. `funding_sebelum` bukan
    `bulan_hidup_terakhir`. Lihat KC-23.
62. **[v36, lahir dari R-239/R-240] Dua semesta yang berbeda DILARANG
    disilangkan tanpa bukti kesepadanan, dan laporan yang memuat CACAH tidak
    dapat menjawab pertanyaan tentang DAFTAR.** R-239 dan R-240 MELESET bukan
    karena hipotesisnya salah, melainkan karena saya mengajukan pertanyaan
    tentang keberadaan bulan tertentu kepada laporan yang hanya menerbitkan
    cacah bulan per simbol. Akibatnya H-A013 saat itu berstatus **TAK BERLAKU**,
    bukan kalah. Penangkalnya: sebelum bertanya, periksa apakah laporan memuat
    DAFTAR yang diperlukan; bila hanya cacah, buat pengukur baru. Lihat KC-24.
63. **[v36] Setiap klaim tentang kematian, kebangkitan, lubang funding, dan
    `bagian_mati` WAJIB menyebut batas semestanya secara tersurat: penyebut 787
    simbol adalah pasangan berkuota USDT SAJA.** Semesta arsip **937** simbol
    dan **21.789** bulan; **150** simbol hanya-arsip (hampir seluruhnya
    BUSD/USDC), **0** simbol hanya-penyebut. Berlaku juga di STATE dan di ADR.
    Lihat KC-25.
64. **[v36, lahir dari R-255] Ramalan tentang nilai EKSTREM — terbesar,
    terkecil, terpanjang — wajib menyebut perlakuan atas SERI, dan medan
    laporan yang menamai pemegang ekstrem wajib melaporkan seluruh pemegangnya
    bila terjadi seri.** R-255 meramalkan `silang_funding.py` sebagai berkas
    terpanjang; hasilnya **705 SERI** dengan `funding.py`, dan medan
    `berkas_terpanjang` menamai `funding.py` semata karena urutan daftar. Ramalan
    dinilai **SEPARUH** dan medannya dicatat cacat. Lihat KC-26.

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
  berkas klines 1m lengkap dan sah secara BENTUK untuk pasar yang tidak
  diperdagangkan: stempel waktu rapat, checksum cocok, namun `volume` dan `count`
  nol pada SELURUH lilin. Gerbang 1m menilai bentuk, bukan kehidupan.
  - Bentangan: jurnal 74 864.000 lilin/20 simbol-bulan; jurnal 77 169 dari 179;
    kohort puncak **456 dari 456**.
  - **SEMESTA (USDT saja, aturan 63):** dari **19.586** simbol-bulan lolos
    gerbang — **1.401 MATI** (7,153%), **98 SEPI** (0,500%), **18.087 HIDUP**
    (92,35%). **945** MATI di luar kohort puncak.
  - **BUKAN CACAT ARSIP FUNDING:** dari 1.401 MATI, **842** kehilangan funding,
    **559** tetap berfunding.
  - **KEMATIAN DAPAT BERBALIK.** LITUSDT MATI **2025-02..2025-11** (10 bulan)
    lalu HIDUP 2026-01..2026-06. Status kehidupan WAJIB per SIMBOL-BULAN.
  - **KEBANGKITAN PUNYA DELAPAN CONTOH — DAN KINI TAFSIRNYA DILEMAHKAN [v36]:**
    **dua bersambung** (ICPUSDT 2022-09, TLMUSDT 2023-03) dan **enam peralihan
    nama** (CTK, CVC, CVX, LIT, MAVIA, SLP). Kecocokan bulan saudara SETTLED
    membuktikan **PENAMAAN kontrak**, BUKAN perdagangan — itu bunyi KC-18 sendiri
    dipakai atas temuannya sendiri.
  - **KEMATIAN PERMANEN JUGA PUNYA CONTOH TELAK:** BTCSTUSDT **53 dari 53** bulan
    MATI SESUDAH funding-nya pulih pada 2022-02. Kembalinya funding BUKAN penanda
    kebangkitan.
  - **Kebijakan DIPUTUSKAN [v28] oleh ADR-A008** (Keputusan 1–6 DITERIMA):
    KC-18 bukan gerbang serapan; kehidupan per simbol-bulan; **SEPI** bila
    `bagian_volume_nol` ≥ 0,5 dan **MATI** bila `transaksi_total` = 0; penyebut
    berpasangan; backtest hanya pada simbol-bulan HIDUP; angka 839.842.134 tidak
    ditulis ulang. Keputusan 7 DITANGGUHKAN.
- **KC-19 [v32] — mencacah dari INGATAN atas berkas yang baru saya tulis
  sendiri.** R-148, R-211, R-217. Penangkalnya aturan 57. **TIDAK TERULANG ENAM
  KALI [v36]:** R-221, R-228, R-232, R-241, R-245, R-250.
- **KC-20 [v33] — taksiran cacah baris bias sistematis ke BAWAH.** R-175 (..680
  vs 705), R-179 (..700 vs 705), R-203 (..400 vs 417), R-225 (..620 vs 705) —
  empat dari empat searah. Penangkalnya aturan 58. **[v36] Diperkuat tanpa
  ramalan baru:** `lubang_tengah.py` V1 390 baris, V2 ternyata **560**; menaksir
  V2 dari byte V1 akan meleset ke bawah untuk kelima kalinya.
- **KC-21 [v34] — menyimpulkan KETIADAAN gejala dari ketiadaan PENGUKURANNYA.**
  Lahir dari R-230. Penangkalnya aturan 59.
- **KC-22 [v35] — memindahkan MEKANISME dari kasus yang menang ke kasus lain.**
  Lahir dari R-234. Penangkalnya aturan 60. Cacat PENALARAN, bukan kode.
- **KC-23 [v35] — memindahkan MEDAN antarjalur.** `funding_sebelum` dipakai
  sebagai bulan hidup terakhir. Penangkalnya aturan 61. KC-23 memindahkan ANGKA,
  KC-22 memindahkan SEBAB.
- **KC-24 [v36, lahir dari R-239/R-240] — mengajukan pertanyaan tentang DAFTAR
  kepada laporan yang hanya memuat CACAH, dan menyilangkan dua semesta tanpa
  bukti kesepadanan.** Gejalanya halus: laporan menjawab dengan angka yang sah,
  tetapi angka itu menjawab pertanyaan LAIN. Akibat nyata: R-239 dan R-240
  MELESET, dan H-A013 sempat berstatus TAK BERLAKU padahal belum diuji.
  Penangkalnya aturan 62.
- **KC-25 [v36] — batas semesta yang tidak tersurat.** Seluruh angka kematian,
  kebangkitan, dan `bagian_mati` dihitung atas **787 simbol berkuota USDT**,
  sementara arsip memuat **937** simbol dan **21.789** bulan. Selisih **150**
  simbol hanya-arsip hampir seluruhnya BUSD/USDC. Menulis "semesta" tanpa
  menyebut batas itu membuat setiap pembaca berikutnya — termasuk saya sendiri di
  sesi berikutnya — memperluas klaimnya tanpa sadar. Penangkalnya aturan 63.
- **KC-26 [v36, lahir dari R-255] — medan yang menamai pemegang nilai EKSTREM
  membisu tentang SERI.** `ringkasan.berkas_terpanjang` pada `ukur_baris` V5
  menamai `funding.py` (705) padahal `silang_funding.py` juga **705**; pemenang
  ditentukan urutan daftar, bukan data. Ramalan identitas R-255 karena itu
  SEPARUH, dan medannya wajib diperbaiki pada V6 agar melaporkan DAFTAR pemegang.
  Penangkalnya aturan 64.

## H-A013 — DIUJI dan MENANG 6–0 [v36]

Sumber: `lux_ai/serapan/bulan_settled.py` **V1** (blob
**`80e8d8bb25cdeff974ef99c5b0e590a87f9bc656`**, `VERSI` 1, `AMBANG_KENDALI` 60,
`SETTLED_TERCATAT` 15), didorong ATOMIK bersama uji dan workflow pada commit
**`9bdab113`** (aturan 45). Run **30448334739**, `kode_keluar` **0**, commit
dicocokkan (aturan 38). Laporan: `reports/bulan_settled_ringkas.json` blob
`df2d2bfa`, 14.413 B, **dibaca UTUH** (aturan 52), `sidik_kode`
`cf96025f…048c`, `sidik_data_silang` `00a95373…a4a1`, `waktu_utc`
2026-07-29T11:38:40Z, `bukan_bukti` false.

| simbol | bulan peralihan | saudara diperiksa | saudara ditemukan | bulan saudara | cocok |
|---|---|---|---|---|---|
| CTKUSDT | 2025-04 | CTKUSDTSETTLED, CTKUSDT_SETTLED | **CTKUSDTSETTLED** | 2025-04 | ✅ |
| CVCUSDT | 2025-05 | CVCUSDTSETTLED, CVCUSDT_SETTLED | **CVCUSDTSETTLED** | 2025-05 | ✅ |
| CVXUSDT | 2025-07 | CVXUSDTSETTLED, CVXUSDT_SETTLED | **CVXUSDTSETTLED** | 2025-07 | ✅ |
| LITUSDT | 2025-12 | LITUSDTSETTLED, LITUSDT_SETTLED | **LITUSDTSETTLED** | 2025-12 | ✅ |
| MAVIAUSDT | 2025-03 | MAVIAUSDTSETTLED, MAVIAUSDT_SETTLED | **MAVIAUSDTSETTLED** | 2025-03 | ✅ |
| SLPUSDT | 2025-07 | SLPUSDTSETTLED, SLPUSDT_SETTLED | **SLPUSDTSETTLED** | 2025-07 | ✅ |

`cacah_peralihan` **6** · `cacah_terukur` **6** · `cacah_cocok_bulan` **6** ·
`ambang_menang` **4** · `menang` **true** · `terukur` **true** ·
`sebab_terpakai` hanya `["saudara_settled_memuat_bulan"]` ·
`definisi_dapat_dibedakan` **false**. Tiap saudara punya TEPAT SATU bulan
(`cacah_bulan_saudara` 1 pada keenamnya).

**Kelemahan yang diakui terbuka.** Karena keenam baris jatuh ke satu jalur sebab,
uji ini tidak pernah membedakan dua penjelasan bersaing di dalam sampelnya.
Kemenangannya adalah kemenangan atas ambang yang saya sendiri tetapkan (4 dari
6), bukan atas alternatif. Sahih, tetapi sempit — dan laporan mengatakannya
sendiri lewat `definisi_dapat_dibedakan` false (aturan 46).

**DUA konvensi nama hidup berdampingan di arsip — ini fakta, bukan tipografi.**
Enam saudara di atas TANPA garis bawah; `ICPUSDT_SETTLED` DENGAN garis bawah;
`TLMUSDTSETTLED` tanpa. R-246 SEPARUH karena catatan lama dan docstring
`penyebut_tahun.py` menulis `TLMUSDT_SETTLED`; teks itu TIDAK disunting (aturan
29) dan cukup tidak diwarisi.

**Pelemahan tafsir yang WAJIB dibawa ke mana pun.** "Delapan kebangkitan" diganti
"**dua bersambung dan enam peralihan nama**". Batasnya: (1) KC-18 — kecocokan
bulan membuktikan PENAMAAN kontrak, bukan perdagangan; (2) aturan 63 — seluruh
angka ini berlaku atas semesta USDT; (3) aturan 62 — laporan ini memuat DAFTAR
bulan sehingga pertanyaan "bulan mana" sah, tetapi pertanyaan "berapa simbol lain
berperilaku sama di seluruh arsip" TIDAK sah dijawab darinya; (4) kedua kasus
bersambung tidak diuji ulang di run ini — ketiadaan pengukuran bukan ketiadaan
gejala (aturan 59).

### Silang cacah 24 nama — 24 dari 24 cocok

`silang_cacah.cacah_nama` **24** · `cacah_cocok_cacah` **24** ·
`cacah_tak_ada_di_laporan_lama` **0** · `seluruhnya_cocok` **true**. Penggugur
bersih: `cacah_gagal_daftar` **0**, `cacah_settled_tercatat` **15** (= konstanta),
`jumlah_bulan_didaftar` **518**, `cacah_nama_didaftar` = `cacah_nama_silang` = 24.

Cacah bulan ARSIP: BNXUSDT **51** · CTKUSDT 68 · CVCUSDT 68 · CVXUSDT 46 ·
ICPUSDT 62 · LITUSDT 65 · MAVIAUSDT 29 · SLPUSDT 33 · TLMUSDT 60 ·
ICPUSDT_SETTLED 9 · TLMUSDTSETTLED 9 · BNXUSDTSETTLED 6 · dan dua belas nama
SETTLED lain bercacah 1 (AERGO, AIA, BDXN, CTK, CVC, CVX, LIT, MAVIA, MINA, PUMP,
SLP, SXP).

**Peringatan aturan 62/63 yang tidak boleh hilang:** BNXUSDT **51** di sini adalah
cacah bulan **ARSIP**, sedangkan **48** yang tercatat pada H-A010 adalah cacah
bulan **PENYEBUT** (USDT saja). Dua semesta, dua angka. Bahwa selisih 3 itu
"persis" tiga lubang tengah BNXUSDT 2022-04/-06/-08 adalah **dugaan**, bukan
fakta terukur, sampai ada laporan yang memuat daftar bulan KEDUA semesta.

## Semesta arsip lawan semesta penyebut — TERUKUR [v36]

| besaran | nilai |
|---|---:|
| simbol penyebut (USDT saja) | **787** |
| simbol arsip | **937** |
| hanya-arsip | **150** |
| hanya-penyebut | **0** |
| bulan arsip | **21.789** |
| nama SETTLED di arsip | **15** |
| nama SETTLED di penyebut | **0** |

150 simbol hanya-arsip hampir seluruhnya BUSD/USDC. Karena `hanya_penyebut` = 0,
penyebut adalah HIMPUNAN BAGIAN murni dari arsip — itulah satu-satunya bukti
kesepadanan yang dimiliki, dan ia hanya menyapa keanggotaan simbol, BUKAN
keanggotaan bulan. **Identitas ke-150 nama itu belum pernah dibaca**
(`reports/semesta_silang.json` penuh belum terbaca).

## Penyebut simbol-bulan PER TAHUN — TERUKUR [v36]

Semesta USDT saja (aturan 63). Sumber: `penyebut_tahun` V1.

| tahun | penyebut simbol-bulan | MATI | `bagian_mati` |
|---|---:|---:|---:|
| 2020 | 504 | 1 | 0,001984 |
| 2021 | 1.385 | 9 | 0,006498 |
| 2022 | 1.729 | 34 | 0,019665 |
| 2023 | 2.400 | 103 | 0,042917 |
| 2024 | 3.570 | 192 | 0,053782 |
| 2025 | 5.948 | 506 | 0,085071 |
| 2026 (6 bulan) | 4.050 | 556 | **0,137284** |

Pembilang: 1+9+34+103+192+506+556 = **1.401** ✅ Penyebut:
504+1.385+1.729+2.400+3.570+5.948+4.050 = **19.586** ✅ (dihitung tangan, aturan
21). Ketujuh angka MATI kini punya penyebut, sehingga `bagian_mati` sah dibaca —
dan ia MENANJAK monoton dari 0,20% (2020) ke **13,73%** (2026). Yang TETAP
DILARANG: menyebut ini laju kematian "pasar kripto"; ia laju atas pasangan
berkuota USDT di arsip futures, per simbol-bulan yang lolos gerbang 1m.

`cacah_simbol_tanpa_hidup` **18** — identitas kedelapan belas simbol itu belum
dibaca (`reports/penyebut_tahun.json` penuh belum terbaca).

## Cacah baris terukur [v36] — `ukur_baris` V5

Sumber: `reports/ukur_baris.json` **V5** (blob `c8b988ff`, dibaca UTUH), commit
**`404e6f1b`**, run **30451749412**, kode 0. Penggugur bersih:
`cacah_berkas_hilang` **0**, `cacah_berkas_melebihi_pagar` **0**,
`cacah_berkas_ada` **21** dari 21. Definisi `len(teks.splitlines())`, sama dengan
pagar 800 di `tests/test_kontinuitas.py`.

| berkas | baris | byte |
| --- | ---: | ---: |
| `funding.py` | **705** | 28.121 |
| `silang_funding.py` V2 | **705** | 29.873 |
| `lubang_tengah.py` **V2** | **560** | 23.745 |
| `kohort_ekor.py` | 553 | 22.590 |
| `kebangkitan.py` V1 | **552** | 22.603 |
| `penyebut_tahun.py` V1 | **527** | 21.653 |
| `tests/test_kebangkitan.py` | **501** | 15.755 |
| `kehidupan_arsip.py` | 496 | 19.281 |
| `semesta_silang.py` V1 | **423** | 16.126 |
| `kehidupan.py` | 417 | 16.638 |
| `bulan_settled.py` V1 | **386** | 14.776 |
| `pulihkan.py` V2 | 383 | 14.839 |
| `tests/test_penyebut_tahun.py` | **369** | 11.596 |
| `ukur_baris.py` V5 | 352 | 17.442 |
| `tests/test_semesta_silang.py` | **253** | 7.879 |
| `tests/test_bulan_settled.py` | **240** | 7.612 |
| `gerbang_1m.py` | 184 | 6.775 |
| `funding_cdn.py` | 162 | 6.335 |
| `arsip.py` | 154 | 5.231 |
| `resample.py` | 127 | 4.356 |
| `kohort_ringkas.py` | 82 | 2.882 |

Total **8.131** baris ✅ (dihitung tangan; laporan setuju). Terbesar **705,
SERI** — `funding.py` dan `silang_funding.py`. **Aturan 48 berlaku atas KEDUANYA
dan atas keduanya saja.** `berkas_terpanjang` melaporkan `funding.py` semata
karena urutan daftar — itu KC-26.

**Utang cacah baris LUNAS [v36]:** `funding.py` **705**, `funding_cdn.py` 162,
`lubang_tengah.py` V2 **560**, `kebangkitan.py` **552**, `penyebut_tahun.py`
**527**, `semesta_silang.py` **423**, `bulan_settled.py` **386**, dan keempat
berkas uji. **Angka kedaluwarsa yang MATI:** `ukur_baris.py` 183/226/280 BATAL →
**352**; `silang_funding.py` 396 BATAL → 705; `pulihkan.py` 318 BATAL → 383;
`lubang_tengah.py` 390 berlaku hanya untuk V1 → **560**.

**BELUM DIUKUR:** `tests/test_lubang_tengah.py` (56 fungsi, 18.387 B) dan berkas
uji lain di luar keempat pasangan baru. Tidak diramalkan dengan pita sempit
(aturan 58 pilihan c).

## Yang berlaku tanpa perubahan dari v35

Seluruh bagian berikut TIDAK berubah dan angkanya tidak ditulis ulang dari
ingatan; rinciannya ada di STATE v35 (blob `6523b84f`) dan jurnal yang disebut di
sana. Ringkasannya dipertahankan di sini agar sesi berikutnya tidak perlu menebak.

- **H-A012 MENANG [v35]** — 8 simbol dari 787 punya bulan MATI lalu HIDUP,
  kedelapannya `bangkit_penuh`, `cacah_peristiwa` 8, `cacah_bulan_antara` 0.
  Panjang rentetan MATI 2, 2, 8, 10, 11, 13, 13, 29 = **88** bulan; jadi 88 dari
  1.401 bulan MATI terbukti berakhir dan **1.313** sisanya belum terbukti
  berakhir. Rentang tiap simbol, bulan MATI pertama/terakhir, dan bulan HIDUP
  pertama sesudahnya ada pada tabel v35. **[v36] tafsirnya dilemahkan** — lihat
  H-A013 di atas.
- **BTCSTUSDT** — 53 bulan, 53 MATI, 0 HIDUP, pemegang rekor **63** bulan MATI
  semesta; funding hilang 2022-01 lalu PULIH 2022-02.
- **Sebaran 1.401 MATI menurut simbol** — **133** simbol dari 787 (16,9%) punya
  ≥1 bulan MATI. Dua puluh teratas: BTCSTUSDT 63 · SCUSDT 48 · FTTUSDT 43 ·
  RAYUSDT 43 · CVCUSDT 29 · STRAXUSDT 27 · DGBUSDT 26 · GLMRUSDT 25 · IDEXUSDT
  25 · MDTUSDT 25 · RADUSDT 25 · SNTUSDT 25 · STPTUSDT 25 · AGIXUSDT 24 ·
  OCEANUSDT 24 · WAVESUSDT 24 · BTSUSDT 21 · KLAYUSDT 20 · UNFIUSDT 20 ·
  BLZUSDT 18.
- **Silang funding × kehidupan [v31]** — penyebut 19.586: MATI 559 berfunding +
  842 berlubang = 1.401; SEPI 96 + 2 = 98; HIDUP 18.054 + **33** = 18.087; jumlah
  18.709 + 877 = **19.586** ✅ 877 + 3 lubang tak dikenal = **880** ✅ Arah wajib
  dipisah: lubang → mati **96,0%** (842/877); mati → lubang **60,1%**
  (842/1.401). Lubang funding TIDAK sah dipakai sebagai penyaring kematian.
- **Bentuk lubang funding** — lokal atas 877 di dalam penyebut: awal **45** +
  ekor **826** + tengah **6** = 877 ✅; terbitan `funding.py` atas 880: awal 48 +
  826 + 6; selisih 3 = tiga lubang BNXUSDT di luar penyebut ✅
- **Keenam lubang funding TENGAH** — BTCSTUSDT 2022-01 dan LITUSDT
  2025-07..2025-11; keenamnya MATI dan berklines penuh secara bentuk. Medan
  `funding sebelum` di tabel v35 adalah medan JALUR FUNDING, bukan bulan hidup
  terakhir (aturan 61, KC-23): LITUSDT sudah MATI sejak 2025-02, jadi kematian
  MENDAHULUI hilangnya funding.
- **H-A010 MENANG 5–0, definisi TEPAT** — QTUMUSDT 2020-02/2020-03 (1),
  ICPUSDT 2021-05/2022-09 (16), TLMUSDT 2021-07/2023-03 (20), BNXUSDT
  2022-05/2023-02 (9), JUPUSDT 2024-01/2024-02 (1); `funding_tanpa_klines` kosong
  pada kelimanya. BNXUSDT **48** bulan di PENYEBUT dengan 3 lubang tengah
  2022-04/-06/-08 yang bulannya TIDAK ADA.
- **33 HIDUP tanpa funding** — sebaran bentuk: awal 33, ekor 0, tengah 0.
  ICPUSDT 13 · TLMUSDT 11 · BNXUSDT 7 · JUPUSDT 1 · QTUMUSDT 1 = **33** ✅
- **Kehidupan semesta terserap [v30]** — kedelapan pecahan `kehidupan_arsip` V1
  (`sidik_kode` `24b6bb26…c595`), penyebut penuh **19.586**, MATI 1.401, SEPI 98,
  HIDUP 18.087, tanpa MATI **18.185**, lilin penuh **839.325.999**, lilin mati
  61.168.123 (7,29%). `cacah_baris_cacat` **0** dari 839 juta baris. Kendali 24
  dari 24 HIDUP. `bagian_mati` per pecahan 0,0418..0,1314 — karena itu 7,153%
  DILARANG dipakai sebagai laju kematian simbol mana pun.
- **Kohort puncak 2025-07 [v29]** — 38 simbol, 456 simbol-bulan, MATI 456, HIDUP
  0; nol simbol-bulan layak backtest.
- **Serapan semesta `perpetual_usdt`** — run **30396803601**, commit `57a04f1e`,
  `versi_pecahan` 6. Simbol **787**, simbol-bulan **19.598**, baris
  **839.842.134**, slot 839.855.709, menit hilang **13.575**; gerbang lolos
  **19.586**, gagal **12**, `persen_lolos` **99,9388**. Zip 26.532.925.083 B;
  parquet 32.706.262.375 B; nisbah 1,2327; parquet karantina 13.247.705 B.
  Pemulihan run **30404071324** (commit `ab4e0774`): 29/29 aset hadir, 29/29 sha
  cocok. Penyebut ganda: PENUH **19.586**, TANPA MATI **18.185**, LAYAK BACKTEST
  **18.087**.
- **Funding semesta (`funding.py` V6)** — run **30412188715**, commit `ba37c5d5`.
  880 bulan klines tanpa funding; 87 funding tanpa klines; penyebut 19.598.
  Kohort puncak 2025-07 = 38 simbol/456 simbol-bulan = 51,8% dari 880. `uji_cdn`:
  10 kohort 404, 10 kendali 200 dengan checksum cocok.
- **`kohort_ekor` V4** — pindaian ADAPTIF, pagu 60 bulan tak tersentuh; sepuluh
  bulan hidup terakhir (AGIX 2024-06, ALPACA 2025-04, AMB 2025-02, BADGER
  2025-03, BAL 2025-03, BLZ 2024-12, BNX 2025-03, BOND 2024-11, COMBO 2025-03,
  DAR 2024-12) dikuatkan `kebangkitan` V1 dengan definisi berbeda: **10 dari 10
  sama**. `bangkit_kembali` 0 pada laporan itu BUKAN bukti tidak ada kebangkitan
  (`cacah_simbol_bangkit_dapat_diuji` = 0). 28 anggota kohort di luar sampel abjad
  BELUM diperiksa. **ADR-A002 §10 tidak boleh diubah atas bukti kohort semata.**
- **Definisi `jumlah_baris`** — manifes = baris lolos gerbang **839.325.999** +
  baris karantina **516.135** = **839.842.134**. `reports/pulihkan_pecahan_<i>.json`
  di git masih HASIL V1; cocokkan `versi_pulihkan` dan `sidik_kode`.

## Hipotesis

- H-A001: belum diuji. H-A002b **GUGUR**. H-A003 MENANG pada 3, GUGUR pada 9.
  H-A004 **tidak dapat diuji** (`fapi.binance.com` → 451). H-A005 GUGUR pada
  rentang yang disampel. H-A006 MENANG pada enam run. H-A008 MENANG dua kali.
- **H-A009 GUGUR** — 559 simbol-bulan MATI tetap berfunding.
- **H-A010 MENANG 5–0**, definisi TEPAT.
- **H-A011 MENANG 6–0 pada LITUSDT, DIBATASI** — BTCSTUSDT memberi 0 HIDUP dari
  53 (aturan 60).
- **H-A012 MENANG** — 8 simbol dari 787 (USDT saja), kedelapannya bangkit penuh.
- **H-A013 [v36] MENANG 6–0** — bulan peralihan kebangkitan SAMA dengan bulan
  saudara SETTLED-nya, 6 dari 6, ambang 4. `definisi_dapat_dibedakan` **false**:
  kemenangan sempit, satu jalur sebab. Statusnya sebelum ini adalah **TAK
  BERLAKU** karena KC-24 — bukan kalah; itu dicatat supaya tidak terbaca sebagai
  hipotesis yang "akhirnya" menang setelah gagal.
- **H-A014 [v36, LAHIR, BELUM DIUJI] — keenam peralihan nama adalah pergantian
  KONTRAK, bukan pergantian kehidupan pasar.** Bila benar, bulan saudara SETTLED
  itu MATI atau tidak diperdagangkan meski bentuk klines-nya sempurna (KC-18
  pada jalur penamaan). Uji yang mungkin tanpa unduhan: ukur kehidupan keenam
  bulan saudara SETTLED itu dari arsip yang sudah di-commit; penyebutnya 6 —
  kecil, jadi aturan 59 wajib ditaati dan hasilnya ditulis sebagai kemungkinan
  campuran, bukan penegasan.

## Papan skor prediksi

R-1..R-120 dirinci v23. R-121..R-149 di v26 dan jurnal 56–63. R-150..R-193 di
jurnal 64–75. R-194..R-199 di jurnal 76–78. R-200..R-204 di jurnal 79–81.
R-205..R-208 di docstring `0929643c`/`dceb1009`. R-209 jurnal 82. R-210..R-211
docstring `1b0e8d8e`. R-212 jurnal 83. R-213..R-215 docstring `67ec2be4`. R-216
jurnal 84. R-217..R-219 docstring `b1816ddf`. R-220 jurnal 86. R-221..R-223
docstring `680d04b4`. R-224..R-226 docstring `85079ffd`. R-227 PROMPT v36. R-228..
R-230 docstring `be5cd877`. R-231 PROMPT v37. R-232..R-235 docstring `bdcbaebc`.
**R-236..R-247 dipraregistrasi dan diadjudikasi di jurnal 92, 93, dan 94** —
rincian barisnya ADA DI SANA dan belum disalin ke tabel ini; yang sudah pasti dan
wajib dibawa: **R-239 dan R-240 MELESET** (sebabnya KC-24, bukan hipotesis yang
salah) dan **R-246 SEPARUH** (`TLMUSDTSETTLED`, bukan `TLMUSDT_SETTLED`).
**R-248..R-252 dipraregistrasi di docstring `bulan_settled.py` (`9bdab113`);
adjudikasinya di jurnal 95. R-253..R-255 dipraregistrasi di docstring
`ukur_baris.py` V5 (`404e6f1b`); adjudikasinya di sini dan di jurnal 96.**

| # | Prediksi | Status |
|---|---|---|
| R-199 | `definisi_dapat_dibedakan` false pada TEPAT 2 pecahan (2 dan 5) | **MENUNGGU** |
| R-248 | H-A013: 4..6 dari 6 bulan peralihan cocok dengan bulan saudara SETTLED | **TEPAT** (**6**) |
| R-249 | dipraregistrasi jurnal 94; tidak diukur oleh `bulan_settled` V1 | **MENUNGGU** |
| R-250 | CI **552 butir** (526 + 26), kode 0, pada commit `9bdab113` | **TEPAT** (`30448334675`) |
| R-251 | `cacah_cocok_cacah` = 24 dari 24 | **TEPAT** (24/24) |
| R-252 | kendali BTCUSDT ≥ 60 bulan 1m | **TEPAT** (**78**) |
| R-253 | CI tetap **552 butir**, kode 0, pada commit `ukur_baris` V5 | **TEPAT** (`30451749571`) |
| R-254 | `cacah_berkas_hilang` 0 DAN `cacah_berkas_melebihi_pagar` 0 atas 21 berkas | **TEPAT** |
| R-255 | berkas terpanjang = `silang_funding.py` | **SEPARUH** (705 **SERI** dengan `funding.py`; medan menamai `funding.py`) |

**Total R-1..R-255** (dihitung tangan, aturan 21). Dasar R-1..R-247 seperti
tercatat pada PROMPT v38 dan jurnal 94: TEPAT **174** · MELESET **44** · SEPARUH
**15** · TIDAK TERADJUDIKASI **7** · MENUNGGU **7**; 174+44+15+7+7 = **247** ✅
Sesi 55 menambah enam TEPAT (R-248, R-250, R-251, R-252, R-253, R-254), satu
SEPARUH (R-255), dan satu MENUNGGU (R-249):

- TEPAT 174 + 6 = **180**
- MELESET **44**
- SEPARUH 15 + 1 = **16**
- TIDAK TERADJUDIKASI **7**
- MENUNGGU 7 + 1 = **8** (R-7, R-19, R-20, R-28, R-36, R-37, R-199, **R-249**)

180+44 = 224; +16 = 240; +7 = 247; +8 = **255** ✅ Ramalan berikutnya **R-256**.
N_percobaan = 0.

**Utang yang dinyatakan terbuka, bukan disembunyikan.** R-249 dimasukkan MENUNGGU
atas dasar penalaran (`bulan_settled` V1 tidak mengukurnya), bukan atas dasar
bacaan ulang jurnal 94. Sebelum papan skor v37 dibekukan, teks R-249 di jurnal 94
WAJIB dibaca ulang; bila ternyata ia punya sumber terukur, angka MENUNGGU berubah
dan jumlahnya tetap 255. Hal yang sama berlaku bagi rincian R-236..R-247 yang
belum disalin ke tabel ini — agregatnya sudah masuk hitungan, barisnya belum.

Catatan kejujuran: **R-250 dan R-253 adalah ramalan MUDAH.** Keduanya hanya
menyalin cacah uji yang sudah terverifikasi (552) dengan alasan mekanis — satu
karena 26 fungsi baru dicacah bernomor, satu karena tidak ada fungsi uji yang
berubah. Aturan 57 kini enam dari enam karena mekanismenya deterministik, bukan
karena kecakapan meramal; membanggakannya akan mengaburkan papan skor.
**R-254 juga mudah** (pagar 800 masih jauh). Ramalan yang benar-benar berisiko di
sesi ini hanya **R-248** (bisa gugur pada ≤3) dan **R-255** (dan ia SEPARUH,
karena saya lupa memikirkan SERI — aturan 64 dan KC-26 lahir dari situ).

**R-256, dipraregistrasi di sini (aturan 26, 38, 55, 56).** Pada commit BERIKUTNYA
yang menyentuh `STATE.md` — yakni commit yang memuat berkas ini — `ci.yml`
MENYALA (berkas di akar, tidak tersentuh `paths-ignore`) sedangkan
`ukur_baris.yml` TIDAK (pemicunya hanya `lux_ai/serapan/ukur_baris.py`), dan
`reports/ci_terakhir.json` akan melaporkan **552 butir** dengan `kode_keluar`
**0**. Dasarnya: tidak ada berkas uji maupun modul yang berubah pada commit ini,
dan 552 sudah terverifikasi pada run 30451749571. **Ini ramalan MUDAH** dan
disebut begitu di muka.

## Jumlah uji

**552 TERVERIFIKASI [v36]** — `reports/ci_terakhir.json` blob `b0e4e1aa`, run
**30451749571**, commit **`404e6f1b`**, `kode_keluar` **0**, "552 tests collected
in 0.47s". Sebelumnya 552 pada run **30448334675** (commit `9bdab113`, blob
`ca196c5a`) dan 526 pada run 30447917282 (commit `474fa23c`). Riwayat: 231 → 234
→ 236 → 239 → 241 → 244 → 253 → 269 → 291 → 316 → 340 → 382 → 382 → 396 → 396
→ 396 → 450 → 494 → 526 → **552**. `tests/test_bulan_settled.py` menyumbang
**26** butir (26 fungsi `def test_`, nol `parametrize`, dicacah BERNOMOR sebelum
push): 526 + 26 = **552** ✅ `tests/test_kebangkitan.py` 54 ·
`tests/test_lubang_tengah.py` 56 · `tests/test_silang_funding.py` 49 ·
`tests/test_penyebut_tahun.py` 44 · `tests/test_semesta_silang.py` 32.

## Utang verifikasi

1-5 dan 11 menunggu tahap juri/klasifikasi. 6-23, 25-28 LUNAS.

24. **AKTIF.**
    - persistensi data lolos dan karantina: **LUNAS**;
    - pemulihan aset di luar runner: **LUNAS**;
    - perbaikan aturan 46 di `pulihkan.py`: **LUNAS DI KODE** (V2) — laporan
      pecahan di git masih hasil V1;
    - bentangan penuh KC-18 atas kohort dan atas SEMESTA: **LUNAS**;
    - penyebut kedua atas semesta: **LUNAS**;
    - daftar 33 HIDUP tanpa funding dan 3 lubang di luar penyebut: **LUNAS**;
    - nama keenam lubang TENGAH: **LUNAS**;
    - uji H-A010 dan `funding_tanpa_klines`: **LUNAS**;
    - status LITUSDT 2026 (H-A011): **LUNAS**;
    - status BTCSTUSDT 2022-02..2026-06: **LUNAS** — 53/53 MATI;
    - pindaian kebangkitan seluruh semesta USDT (H-A012): **LUNAS** — 8 simbol;
    - sebaran 1.401 MATI menurut TAHUN dan SIMBOL: **LUNAS**;
    - pencocokan `bulan_hidup_terakhir` dengan `kohort_ekor`: **LUNAS** — 10/10;
    - **penyebut simbol-bulan PER TAHUN: LUNAS [v36]** — tabel di atas;
    - **semesta arsip lawan penyebut (937/787/150/0, 21.789 bulan): LUNAS [v36]**;
    - **keberadaan keenam bulan peralihan (H-A013): LUNAS [v36]** — keenamnya
      cocok dengan bulan saudara SETTLED-nya;
    - **cacah baris `lubang_tengah.py` V2, `kebangkitan.py`, `penyebut_tahun.py`,
      `semesta_silang.py`, `bulan_settled.py`, `funding.py`, `funding_cdn.py`,
      dan empat berkas uji: LUNAS [v36]**;
    - **pemecahan `silang_funding.py` (705 baris) dan `funding.py` (705 baris),
      aturan 48: BELUM** — keduanya kini terukur ulang, jadi tidak ada lagi
      alasan menundanya;
    - **medan `berkas_terpanjang` yang membisu tentang SERI (KC-26): BELUM** —
      perbaikan wajib di `ukur_baris` V6;
    - **identitas 150 simbol hanya-arsip: BELUM** — `reports/semesta_silang.json`
      penuh belum terbaca;
    - **identitas 18 simbol tanpa bulan HIDUP: BELUM** —
      `reports/penyebut_tahun.json` penuh belum terbaca;
    - **kehidupan keenam bulan saudara SETTLED (H-A014): BELUM**;
    - cacat penulisan docstring R-225 ("tujuh fungsi" lalu sembilan nama):
      dicatat, TIDAK disunting; jumlah yang benar sembilan;
    - docstring `penyebut_tahun.py` menulis `TLMUSDT_SETTLED` (salah): dicatat,
      TIDAK disunting, tidak diwarisi;
    - pencocokan 3 lubang BNXUSDT dengan 12 simbol-bulan karantina: BELUM;
    - kehidupan 12 simbol-bulan karantina: BELUM (tar terpisah);
    - jalur **funding**: `funding_ada` masih null di seluruh manifes — BELUM;
    - medan `dugaan_pengganti` (ADR-A005) — BELUM;
    - pemulihan harian ADR-A007 — BELUM, bahan baku sudah ada;
    - karantina artefak 7 hari — BELUM;
    - 28 anggota kohort di luar sampel abjad — BELUM;
    - `reports/diagnosa_kc15.json` (42.916 B), `reports/kohort_ekor.json`
      (112.687 B), `tests/test_pulihkan.py` — BELUM pernah dibaca.
    Mengadjudikasi R-7, R-19, R-20, R-28, R-36, R-37.

## Daftar ADR

- ADR-A001 aturan dasar. DITERIMA.
- ADR-A002 serapan. DITERIMA; §3 DIAMANDEMEN oleh ADR-A004 lalu ADR-A007; §9
  DIGANTI oleh ADR-A006 Keputusan 3. **§10 belum disentuh dan tetap tidak boleh
  disentuh:** ketiga bentuk lubang punya penjelasan calon yang TIDAK menuduh arsip
  funding cacat — pada BTCSTUSDT funding terus terbit sepanjang 53 bulan kematian.
  **[v36] Bila §10 kelak disunting, ia WAJIB menyebut batas USDT (aturan 63).**
- ADR-A003 taksonomi rezim. BELUM ADA (nomor dicadangkan). Delapan kebangkitan
  menyentuh langsung nomor ini: rezim sebuah simbol tidak monoton dan dapat
  kembali — **dan [v36] enam dari delapan ternyata peralihan KONTRAK, sehingga
  taksonomi rezim wajib memisahkan "kontrak berganti nama" dari "pasar hidup
  kembali".**
- ADR-A004 kebijakan KC-6. DITERIMA.
- ADR-A005 jenis instrumen tahap pertama. DITERIMA.
- ADR-A006 karantina + persistensi. DITERIMA, DITERAPKAN, TERVERIFIKASI DARI LUAR.
- **ADR-A007 serapan hibrida. DIUSULKAN**, belum diterima. Wajib memperhitungkan
  temuan `jumlah_baris` dan kendala R-146.
- **ADR-A008 akibat KC-18. DITERIMA [v28] untuk Keputusan 1–6**; Keputusan 2–4
  TERTERAP atas seluruh semesta USDT; Keputusan 5 bersemesta **18.087**.
  **Keputusan 7: bahannya LENGKAP dan BERCABANG DUA** — bentuk TENGAH dapat
  menandai jeda yang berakhir (LITUSDT) ATAU penerbitan funding yang pulih tanpa
  perdagangan (BTCSTUSDT, 53/53 MATI). Keputusannya WAJIB memuat kedua cabang,
  WAJIB per simbol-bulan, DILARANG menyebut funding dan perdagangan berhenti
  "serentak", dan **[v36] WAJIB menyebut batas USDT serta membedakan peralihan
  kontrak dari kebangkitan pasar.**
- ADR berikutnya **A009**.

## Temuan sampingan yang belum diukur

- **Kehidupan keenam bulan saudara SETTLED (H-A014)** — pertanyaan paling murah
  yang tersisa; bahannya sudah di-commit.
- **Identitas 150 simbol hanya-arsip** dan **18 simbol tanpa bulan HIDUP**.
- Mengapa dua dari enam bulan peralihan jatuh pada **2025-07**, bulan tebing
  funding dan bulan kohort puncak.
- Sebab kebangkitan/peralihan kedelapan simbol (di luar jangkauan arsip).
- Apakah 3 lubang BNXUSDT (2022-04, -06, -08) sama dengan 3 simbol-bulan KC-15.
- Kehidupan 12 simbol-bulan karantina.
- `bulan_hidup_terakhir` bagi 28 anggota kohort di luar sampel abjad.
- 15 nama SETTLED: apakah punya pendahulu seperti SXPUSDT; dua belas di antaranya
  bercacah satu bulan saja.
- Daftar `INDEKS` hanya tiga nama, disusun manual.
- Saham dan komoditas token masih terhitung `perpetual_usdt`.
- `.decode("utf-8","replace")` di `klines` membungkam byte rusak.
- Apakah BUSD/USDC layak digabung dengan USDT — kini pertanyaan berangka: 150
  simbol dan selisih 21.789 lawan 19.598 bulan.
- Sisa 16 simbol non-ASCII belum diuji langsung (币安人生USDT 9, 我踏马来了USDT 6,
  龙虾USDT 4).
- Sebab KC-14 (H-A004) tidak dapat diuji. Sebab KC-15 tidak diketahui.
- Selisih penyebut diagnosa KC-15: 38 diperiksa, 41 dirancang.
- `reports/funding_selisih_penuh.json` belum pernah dibaca; `daftar_terpotong`
  masih true (500 dari 880).
- Selisih byte funding AGIXUSDT 531 lawan 529.
- `waktu_utc` runner berjalan lebih dulu daripada jam sesi.
- `tests/test_pulihkan.py` belum pernah dibaca ulang sesudah push.
