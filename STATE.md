# STATE — versi 38

Diperbarui: 2026-07-29 (sesi 55, lanjutan kesembilan). Aturan hanya BERTAMBAH;
jangan menulis ulang dari ingatan. v38 disusun di atas teks v37 yang dibaca
langsung dari `main` (blob **`f520d5e2a50c17c43f6af73c6b2b5701c59d1f0b`**, dibaca
**UTUH** sebelum satu huruf pun ditulis), ditambah jurnal 102–105,
`reports/taksonomi_semesta.json` (blob `42d07af7`, UTUH),
`reports/terhenti_semesta.json` **V1** (blob `609160a3`, UTUH) dan **V3** (blob
`e4f71ba8`, UTUH, ref runner `9aad0576`), `lux_ai/serapan/survei.py` (blob
`26b14940`, UTUH), `lux_ai/semesta/terhenti.py` V1 (blob `3fa8f697`, UTUH),
`lux_ai/serapan/ringkas_semesta.py` (blob `bc8f7ad7`, UTUH),
`.github/workflows/terhenti_semesta.yml` (blob `baef4f41`, UTUH), listing UTUH
`.github/workflows/` (**30 berkas**) dan `lux_ai/semesta/` (3 berkas), serta
`reports/ci_terakhir.json` blob `2a594f92` (610), `17e905a4` (623) dan
**`bee0342e` (630)**.

Run yang dicocokkan commit-nya, semuanya kode 0: **30459083416** (`5b968b2a`, CI
610), **30459312700** (`10ca9d4c`, CI 610), **30461798702** (`8121739b`, CI
**623**), **30462427226** (`e6b74855`, CI **630**), serta dua run
`terhenti-semesta`: laporan V2 pada ref runner `0e6e51fd` dan **laporan V3 pada
ref runner `9aad0576`**.

Tiga peristiwa terbesar sejak v37:

1. **Dua sumbu dipisahkan: keanggotaan semesta lawan keberlangsungan hidup.**
   Lahir aturan **67** dan KC-**30**. Terukur: **49** nama masih terbit pada bulan
   tutup semesta DI LUAR penyebut riset — lebih dari dua kali taksiran minimum 21.
2. **Tafsir "peralihan nama" DICABUT.** Keenam nama peralihan H-A013
   **seluruhnya masih terbit** pada 2026-06 berdampingan dengan saudara
   SETTLED-nya (`cacah_peralihan_terhenti` **0**). Nama SETTLED **menambah**,
   bukan mengganti. Lahir aturan **68** dan KC-**31**.
3. **Empat berkas yang tak pernah tercatat ditemukan sudah ada**
   (`terhenti.py`, `tests/test_terhenti.py`, `reports/terhenti_semesta.json`,
   `terhenti_semesta.yml`), dan satu angka warisan DICABUT: "16 simbol
   non-ASCII" sebenarnya **3 nama / 19 bulan**. Lahir KC-**32** (mencampur dua
   sistem penomoran).

## Aturan bernomor

Aturan **1–36** berlaku tanpa perubahan; teks di STATE v19 (blob `e06c486e…`),
ringkas nomornya di v37 (blob `f520d5e2`).

Aturan **37, 39–45, 47, 49, 51, 53, 54, 56, 59–62** berlaku tanpa perubahan dan
teks penuhnya ada di v37 (blob `f520d5e2`). Ringkas satu baris: 37 kelas cacat
pada sampel · 39 keseragaman sampel bukan ramalan · 40 uji silang baris ·
41 penyebut nol → TIDAK TERADJUDIKASI · 42 kelas cacat butuh angka terukur ·
43 toleransi berskala · 44 ramalan menyebut penyebut · 45 keatomikan push pemicu ·
47 satuan cacah tersurat · 49 re-export tetap mematahkan uji · 51 jendela mundur
adaptif · 53 ramalan kode keluar butuh pembacaan perilaku · 54 cacah `def test_`
satu per satu · 56 "commit BERIKUTNYA yang menyentuh X" · 59 ketiadaan gejala
butuh penyebut · 60 mekanisme tak dipindah antarkasus · 61 medan tak dipindah
antarjalur · 62 daftar tak diminta dari laporan bercacah.

Yang berikut memuat angka atau daftar kepatuhan, jadi ditulis agak penuh:

38. Cacah uji hanya sah dari `reports/ci_terakhir.json` (run id + commit +
    `kode_keluar`). Laporan dapat TERTIMPA run berikutnya; temukan ref runner
    lewat `list_commits` dengan `path="reports/ci_terakhir.json"`. **[v38]
    Ditaati lima kali lagi:** R-268 (610), R-274 (623), R-277 (630) dan kedua
    laporan `terhenti` V2/V3 dibaca pada ref runner `0e6e51fd` dan `9aad0576`,
    bukan dari `main`. Cara yang sama berlaku bagi laporan NON-CI: `list_commits`
    dengan `path="reports/terhenti_semesta.json"` mendaftar tiap commit runner.
46. Kode dilarang menyimpulkan dari penyebut nol; medan yang menyimpulkan wajib
    memeriksa lebih dulu apakah kasusnya mampu membedakan. **[v38] Ditaati oleh
    `terhenti` V2/V3** (`definisi_dapat_dibedakan`, dan `_laporan_kosong` yang
    tetap memuat SELURUH medan saat penyebut nol).
48. Berkas modul yang mendekati pagar 800 baris dipecah SEBELUM fungsi baru
    ditambahkan. Berlaku atas DUA berkas 705 baris: `funding.py` dan
    `silang_funding.py`. **Masih BELUM dikerjakan; tidak ada lagi alasan
    menundanya.** Tertinggi berikutnya `lubang_tengah.py` V2 **560**.
50. Setiap pengukuran yang menyimpulkan dari KETIADAAN wajib memuat kendali
    positif. **[v38] `terhenti` V2/V3 bersih:** `kendali_sah` true — BTCUSDT ada,
    hidup, dan bergolongan `perpetual_usdt`.
52. Laporan yang tidak dapat dibaca utuh setara dengan laporan yang tidak ada.
    **[v38] Aturan ini menangkap cacat yang paling memalukan sesi ini:** push V3
    membawa **kurung kurawal liar** di baris terakhir `tests/test_terhenti.py`
    (sisa sintaksis JSON yang menyusup ke berkas Python). Yang menemukannya adalah
    pembacaan ulang ekor berkas sesudah push, bukan laporan. **Perluasan tersurat:
    ekor SETIAP berkas kode yang didorong wajib dibaca, bukan hanya berkas
    panjang seperti STATE.** Laporan `silang_funding` penuh 183.963 B tetap tak
    terbaca utuh selamanya.
55. Sebelum meramalkan hasil workflow, baca `paths`/`paths-ignore` dan sebutkan
    workflow MANA yang menyala. `ci.yml` mengabaikan `journal/**`, `decisions/**`,
    `hipotesis/**`, `reports/**`. `ukur_baris.yml` hanya atas
    `lux_ai/serapan/ukur_baris.py`; `semesta_kuota.yml` hanya atas
    `lux_ai/serapan/semesta_kuota.py`; **`terhenti_semesta.yml` hanya atas
    `lux_ai/semesta/terhenti.py` dan dirinya sendiri** — karena itu menyunting
    `taksonomi.py` saja TIDAK menyalakannya, meski isi laporannya bergantung
    padanya.
57. Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB ditulis
    BERNOMOR dan nomor terakhirnya dipakai sebagai cacahan. **TERBUKTI BEKERJA
    DUA BELAS DARI DUA BELAS [v38]:** 382, 396, 450, 494, 526, 552, 584, 598,
    610, **623**, **630**. Mekanismenya deterministik — itu sebab keberhasilannya,
    bukan kecakapan meramal. Fungsi yang hanya BERGANTI NAMA dihitung nol
    tambahan.
58. Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH dalam
    giliran yang sama DILARANG diramalkan dengan pita sempit. Pilih: (a) baca
    ulang utuh; (b) pita batas atas ≥1,8× batas bawah; (c) jangan meramal, ukur.
63. **[DIAMANDEMEN v37, DIPERKUAT v38]** Setiap klaim tentang kematian,
    kebangkitan, lubang funding, dan `bagian_mati` WAJIB menyebut batas
    semestanya secara tersurat: penyebut **787** simbol adalah `perpetual_usdt`,
    dan ia PERSIS seluruh perpetual USDT di arsip. Semesta arsip **937** simbol,
    **21.789** bulan; **150** hanya-arsip; **0** hanya-penyebut. Frasa lama
    "hampir seluruhnya BUSD/USDC" **DICABUT** (terukur 80 dari 147).
    **[v38] Alasan baru yang membuat aturan ini bukan formalitas:** pada bulan
    tutup semesta, **49 nama di luar penyebut masih terbit**, di antaranya **38
    dari 39** perpetual USDC. Kalimat tentang "pasar" yang disusun dari 787 nama
    wajib berbunyi "di antara perpetual USDT".
64. Ramalan tentang nilai EKSTREM wajib menyebut perlakuan atas SERI, dan medan
    yang menamai pemegang ekstrem wajib melaporkan SELURUH pemegangnya bila seri.
    Perbaikan wajib di `ukur_baris` **V6**; `semesta_kuota` sudah benar sejak V1.
65. Setiap daftar contoh WAJIB menyebut CARA pemilihannya, dan kalimat sifat
    tentang KESELURUHAN himpunan DILARANG disusun dari contoh yang bukan
    seluruhnya. Bila cara pemilihan tak diketahui, daftar hanya boleh membuktikan
    KEBERADAAN, tidak pernah PROPORSI. **[v38] Terbayar langsung:**
    `contoh_hidup_luar_penyebut` V2 memuat 20 nama pertama urut ABJAD dan berhenti
    di `DOGEUSDC`, sehingga nama SETTLED yang hidup **tak terlihat** — itulah sebab
    V3 mendaftar nama penuh dengan medan `daftar_nama_terpotong`.
66. **[lahir salah lalu DIREVISI]** Setiap cacahan semesta wajib menyebut KELAS
    INSTRUMEN yang dicacah, dan STATE wajib memuat batas semesta yang sudah
    ditegakkan KODE. **Sebelum menuduh sebuah batas tidak ada, berkas
    penyaringnya WAJIB dibaca lebih dulu; ketidaktahuan pembaca bukan cacat
    rancangan.** **[v38] Menyelamatkan untuk kali ketiga:** rencana menulis
    pengurai terhenti baru dibatalkan setelah `.github/workflows/` dan
    `lux_ai/semesta/` dilisting — modulnya sudah ada. **Perluasan tersurat:
    sebelum menulis modul baru, LISTING direktori paket dan direktori workflow
    lebih dulu.**

67. **[v38, lahir dari R-271 dan diukur oleh R-272/R-273] Keanggotaan semesta dan
    keberlangsungan hidup adalah DUA SUMBU; satu DILARANG disimpulkan dari yang
    lain.** "Hanya-arsip" tidak berarti "mati", dan "di dalam penyebut" tidak
    berarti "masih terbit". Terukur pada bulan tutup 2026-06: dari 937 nama arsip,
    **808 masih terbit** dan **129 terhenti**; dari 787 nama penyebut, **759 masih
    terbit** dan **28 terhenti**; dan **49** nama yang masih terbit berada DI LUAR
    penyebut. Angka **28** (berhenti terbit) DILARANG dicampur dengan **1.401**
    simbol-bulan MATI, **98** SEPI, atau `cacah_simbol_tanpa_hidup` **18** — yang
    pertama mengukur berhentinya ARSIP, sisanya mengukur kehidupan DI DALAM arsip
    yang tetap terbit. Pasangan 28 lawan 18 paling berbahaya karena keduanya kecil
    dan sama-sama terdengar seperti "simbol mati". Lihat KC-30.
68. **[v38, lahir dari R-276] Nama turunan dan nama asal dapat terbit BERSAMAAN.**
    Kehadiran nama turunan (`SETTLED` atau sejenisnya) DILARANG dibaca sebagai
    berhentinya nama asal; bulan terakhir keduanya wajib diukur terpisah dan
    dilaporkan BERPASANGAN. Terukur: keenam nama peralihan H-A013 masih terbit
    2026-06 bersama saudara SETTLED-nya, dan dari 15 nama SETTLED hanya **dua**
    yang nama dasarnya berhenti terbit (`SXPUSDT`, `BDXNUSDT`). Lihat KC-31.

## Kelas cacat

KC-1 s.d. KC-12 seperti v19; KC-10 dan KC-11 DITUTUP. KC-13 keterwakilan sampel
(penangkal aturan 37). **KC-16 DITARIK — nomornya TETAP kosong selamanya.**
KC-17 DITUTUP. Teks penuh KC-14, KC-15, KC-19–KC-29 ada di v37 (blob
`f520d5e2`); yang wajib dibawa:

- **KC-14** — menit hilang NYATA di arsip 1m: **9** simbol-bulan, **6.375** menit
  (425×15). Sebab tak diketahui (H-A004 tak dapat diuji). Karantina (ADR-A006).
- **KC-15** — klines BULANAN kehilangan HARI UTC penuh yang utuh di berkas
  HARIAN: **3** simbol-bulan, semuanya BNXUSDT 2022, **7.200** menit (5×1440).
  Kebijakan ADR-A007. 9 + 3 = **12** karantina; 6.375 + 7.200 = **13.575** menit;
  **516.135** baris. **Kehidupan keduabelasnya BELUM diukur.**
- **KC-18** — lilin datar lolos gerbang struktural; gerbang menilai BENTUK, bukan
  kehidupan. Semesta `perpetual_usdt` atas **19.586** simbol-bulan lolos: **1.401
  MATI** (7,153%), **98 SEPI** (0,500%), **18.087 HIDUP** (92,35%); 945 MATI di
  luar kohort puncak. Dari 1.401 MATI, **842** kehilangan funding dan **559**
  tetap berfunding — jadi BUKAN cacat arsip funding. **Kematian dapat berbalik**
  (LITUSDT MATI 2025-02..2025-11 lalu HIDUP 2026-01..2026-06), jadi status wajib
  per SIMBOL-BULAN. Kematian permanen punya contoh telak: BTCSTUSDT **53 dari
  53** MATI sesudah funding-nya pulih 2022-02. **[v38] Kecocokan bulan saudara
  SETTLED membuktikan PENAMAAN kontrak, bukan perdagangan — dan kini diperkuat
  dari arah baru: `SXPUSDTSETTLED` adalah nama SETTLED yang AKTIF diterbitkan,
  jadi `SETTLED` bahkan bukan penanda "sudah berakhir".** Kebijakan ADR-A008
  Keputusan 1–6 DITERIMA; Keputusan 7 DITANGGUHKAN.
- **KC-19** mencacah dari ingatan (penangkal aturan 57) — **tidak terulang dua
  belas kali**. **KC-20** taksiran baris bias ke BAWAH (aturan 58). **KC-21**
  ketiadaan gejala dari ketiadaan pengukuran (aturan 59). **KC-22** memindahkan
  MEKANISME (aturan 60). **KC-23** memindahkan MEDAN (aturan 61). **KC-24**
  bertanya DAFTAR kepada laporan bercacah (aturan 62). **KC-25** batas semesta tak
  tersurat (aturan 63). **KC-26** medan ekstrem membisu tentang SERI (aturan 64).
  **KC-27** mengarakterisasi himpunan dari contoh BERURUT (aturan 65). **KC-28**
  mencampur kelas instrumen dalam satu cacahan — berlaku atas arsip **937**, BUKAN
  atas penyebut 787 yang bersih **karena dirancang** (aturan 66). **KC-29**
  taksonomi PARALEL: mengarang klasifikasi padahal `lux_ai/semesta/taksonomi.py`
  sudah ada, dan tidak mencapnya dalam `sidik_kode` (lubang aturan 22).

- **KC-30 [v38, lahir dari R-271, diukur oleh R-272/R-273] — membaca NAMA KELAS
  sebagai KEADAAN.** Saya menyimpulkan `futures_kedaluwarsa` berarti "sudah
  kedaluwarsa" dan `perpetual_usdc` berarti "sudah mati". Terukur sebaliknya:
  `futures_kedaluwarsa` memuat **44 terhenti dan 6 HIDUP** dalam satu kelas —
  keenamnya `BTCUSDT_260626`, `_260925`, `_261225` dan tiga saudara ETH-nya, yakni
  kontrak yang tanggal jatuh temponya belum lewat pada 2026-06 — sementara
  `perpetual_usdc` **38 dari 39 masih hidup**. Nama kelas menamai BENTUK kontrak,
  bukan status. Akar yang sama melahirkan kekalahan R-271, R-272, R-273.
  Penangkalnya aturan 67.
- **KC-31 [v38, lahir dari R-276] — membaca nama PERISTIWA sebagai MEKANISMENYA.**
  Kata "peralihan" saya pakai untuk sesuatu yang ternyata hanya **penambahan**:
  nama SETTLED terbit di SAMPING nama dasar yang terus hidup, bukan
  menggantikannya. Keluarga sama dengan KC-30. Penangkalnya aturan 68.
- **KC-32 [v38] — mencampur DUA SISTEM PENOMORAN yang berbeda.** Di jurnal 105
  saya menulis "R-28 kini dapat diadjudikasi" atas dasar bahwa **utang verifikasi
  nomor 28** sudah lunas. Keduanya tak berhubungan: utang verifikasi 6–23 dan
  25–28 LUNAS sejak lama, sedangkan **ramalan R-28** bunyinya ada di STATE v23 dan
  **belum saya baca**. Teks jurnal 105 TIDAK disunting (aturan 29); kalimat itu
  DILARANG diwarisi. **R-28 tetap MENUNGGU** dan tidak boleh diadjudikasi sebelum
  bunyinya digali dari riwayat `STATE.md`. Penangkal: sebelum mengadjudikasi
  ramalan bernomor, bunyinya wajib DIBACA dari sumber, bukan disimpulkan dari
  nomor yang mirip.

## Semesta riset = `perpetual_usdt` = penyebut 787 — TERBUKTI DUA ARAH [v37]

Sumber: `semesta_kuota.py` **V3**, commit `db4a192d`, run 30456422183, laporan
blob `8adae5ee` (UTUH), `sidik_kode` `ef0c4a24…`, `bukan_bukti` false.

- `cacah_perpetual_usdt` **787** = `cacah_penyebut_simbol` **787**
- `cacah_perpetual_usdt_luar_penyebut` **0**; `cacah_penyebut_bukan_perpetual_usdt`
  **0**; `cacah_penyebut_bukan_akhiran_usdt` **0**; `cacah_penyebut_luar_arsip`
  **0**; `penyebut_bagian_arsip` true.

Karena KEDUA arah nol, ini **kesamaan himpunan**, bukan himpunan bagian.

Batas yang wajib ikut disebut (`taksonomi.CATATAN_BATAS`): token **saham, ETF,
dan komoditas** (mis. `AAPLUSDT`, `XAUUSDT`) tak dapat dibedakan lewat bentuk
nama, jadi mereka **IKUT di dalam 787**.

### Taksonomi kanonik — sembilan kelas

Berkas `lux_ai/semesta/taksonomi.py` (blob `b418c7ba`). Urutan pemeriksaan
MENGIKAT: pola ekspirasi `_\d{6}$` → akhiran `SETTLED` → daftar `INDEKS` → kutipan
`("USDT","USDC","BUSD","USD1","BTC")` dengan `BTC` sebagai `KUTIPAN_NON_FIAT`.
`INDEKS` = {`DEFIUSDT`, `BTCDOMUSDT`, `BLUEBIRDUSDT`}, manual, tersurat. Maka
**790 nama berakhiran USDT = 787 perpetual + 3 indeks**, tanpa sisa.

| jenis kanonik | nama (arsip 937) | bulan | hanya-arsip (150) | bulan |
|---|---:|---:|---:|---:|
| `perpetual_usdt` | **787** | **19.598** | 0 | 0 |
| `futures_kedaluwarsa` | 50 | 258 | 50 | 258 |
| `perpetual_busd` | 41 | 812 | 41 | 812 |
| `perpetual_usdc` | 39 | 893 | 39 | 893 |
| `sisa_settled` | 15 | 36 | 15 | 36 |
| `indeks` | 3 | **151** | 3 | **151** |
| `perpetual_usd1` | 1 | 2 | 1 | 2 |
| `basis_non_fiat` | 1 | 39 | 1 | 39 |
| `tak_tergolong` | **0** | 0 | 0 | 0 |
| **jumlah** | **937** | **21.789** | **150** | **2.191** |

Dihitung tangan (aturan 21): 787+50+41+39+15+3+1+1 = **937** ✅ ·
19.598+258+812+893+36+151+2+39 = **21.789** ✅ · 21.789 − 2.191 = **19.598** ✅

`tak_tergolong` **0**: seluruh 937 nama punya kelas kanonik.

**ANGKA WARISAN YANG DICABUT [v38].** v37 menulis "keenam belas nama non-ASCII"
dan "sisa 16 simbol non-ASCII". Laporan `taksonomi_semesta.json` (blob
`42d07af7`) memberi `non_ascii.cacah` **3** dan `jumlah_bulan` **19**, dengan
contoh 币安人生USDT (9 bulan), 我踏马来了USDT (6), 龙虾USDT (4) — 9+6+4 = **19** ✅
**Angka 16 adalah HANTU dan DILARANG diwarisi** (contoh lain KC-11). Ketiganya
bergolongan `perpetual_usdt`, jadi ADA di dalam penyebut, dan asal-usul angka 16
belum diketahui.

### Taksonomi LOKAL modul (kuota) — dipertahankan berdampingan

USDT 805 nama/19.785 bulan (15 SETTLED) · TAK_DIKENAL 51/260 · BUSD 41/812 ·
USDC 39/893 · BTC 1/39. `TAK_DIKENAL` 51 = 50 `futures_kedaluwarsa` + 1
`perpetual_usd1` (`BTCUSD1`); 258 + 2 = 260 ✅ — KC-29 dalam bentuk angka.
**150 hanya-arsip = 147 bukan-akhiran-USDT + 3 indeks**; dari 147 itu BUSD+USDC =
**80** (54,4%), bukan "hampir seluruhnya" (KC-27).

### Penguraian selisih 163 — identitas utuh

`bulan_usdt_bukan_settled` 19.749 · `bulan_arsip_milik_penyebut` **19.598** ·
`bulan_arsip_milik_hanya_arsip` **151** · `bulan_lolos_gerbang` 19.586 ·
`selisih_total` **163** · `selisih_dalam_penyebut` **12** ·
`selisih_dari_hanya_arsip` **151** · `identitas_utuh` true.
19.598 + 151 = 19.749 ✅ · 12 + 151 = 163 ✅ · 19.598 − 19.586 = **12** ✅

**151 bulan itu SELURUHNYA milik ketiga indeks.** Kesamaan angka **12** dengan 12
simbol-bulan karantina **BUKAN bukti identitas himpunan** — nama dan bulannya
belum dicocokkan. Utang terbuka, bukan temuan.

## Terhenti lawan hidup per jenis — TERUKUR [v38]

Sumber: **`lux_ai/semesta/terhenti.py` V3**, laporan
`reports/terhenti_semesta.json` blob **`e4f71ba8`** pada ref runner
**`9aad0576`** (dibaca UTUH), `sidik_kode` **`d892391d…`** (V2 `e6b2ad9f…`, V1
`f4fe7675…`), `sidik_data` `6128fbb0…`, `sumber` `reports/semesta_rentang.json`
110.662 B, `sumber_bersidik` **false** (aturan 35: laporan sumber tanpa sidik
hanya petunjuk), `bukan_bukti` true, `status` TERUKUR, `kendali_sah` true,
`identitas_per_jenis_utuh` true, **`daftar_nama_terpotong` false**.

Dua definisi "terhenti" hidup berdampingan (aturan 36): **survei** memakai
`selisih_bulan >= 2` → **128**; **taksonomi** memakai `bulan_terakhir < 2026-06`
→ **129**. `cacah_hanya_taksonomi` **1** = **`SXPUSDT`** (bulan terakhir
2026-05); `cacah_hanya_survei` **0**, jadi selisihnya semata soal ambang, bukan
dua himpunan bersilang. Ekor: 2026-03 **1**, 2026-04 **3**, 2026-05 **1**,
2026-06 **808**.

| jenis | terhenti | dari | hidup |
|---|---:|---:|---:|
| `futures_kedaluwarsa` | **44** | 50 | 6 |
| `perpetual_busd` | **41** | 41 | **0** |
| `perpetual_usdt` | **28** | 787 | **759** |
| `sisa_settled` | **14** | 15 | **1** |
| `indeks` | 1 | 3 | 2 |
| `perpetual_usdc` | 1 | 39 | **38** |
| `perpetual_usd1` | 0 | 1 | 1 |
| `basis_non_fiat` | 0 | 1 | 1 |
| `tak_tergolong` | 0 | 0 | 0 |

Terhenti 44+41+28+14+1+1 = **129** ✅ Hidup 759+38+6+2+1+1+1 = **808** ✅
129 + 808 = **937** ✅ `cacah_hidup_luar_penyebut` = 808 − 759 = **49** ✅

**28 nama `perpetual_usdt` yang berhenti terbit (SELURUHNYA, aturan 65):**
1000BTTCUSDT, AKROUSDT, ANCUSDT, ANTUSDT, AUDIOUSDT, **BDXNUSDT**, BTSUSDT,
BTTUSDT, BZRXUSDT, COCOSUSDT, DODOUSDT, DOTECOUSDT, EOSUSDT, FOOTBALLUSDT,
FRONTUSDT, GALUSDT, HNTUSDT, KEEPUSDT, LENDUSDT, LUNAUSDT, **MATICUSDT**,
MBLUSDT, NUUSDT, RNDRUSDT, SRMUSDT, **SXPUSDT**, TOMOUSDT, YFIIUSDT.

Yang TIDAK ada di dalamnya, dan karena itu masih terbit: **ICPUSDT, TLMUSDT,
BNXUSDT, CTKUSDT, CVCUSDT, CVXUSDT, LITUSDT, MAVIAUSDT, SLPUSDT** — yakni
kedelapan simbol "kebangkitan" beserta BNXUSDT.

**49 nama HIDUP di luar penyebut (SELURUHNYA, aturan 65):** 1000BONKUSDC,
1000PEPEUSDC, 1000SHIBUSDC, AAVEUSDC, ADAUSDC, ARBUSDC, AVAXUSDC, BCHUSDC,
BIOUSDC, BNBUSDC, BOMEUSDC, BTCDOMUSDT, BTCUSD1, BTCUSDC, BTCUSDT_260626,
BTCUSDT_260925, BTCUSDT_261225, CRVUSDC, DEFIUSDT, DOGEUSDC, ENAUSDC, **ETHBTC**,
ETHFIUSDC, ETHUSDC, ETHUSDT_260626, ETHUSDT_260925, ETHUSDT_261225, FILUSDC,
HBARUSDC, IPUSDC, KAITOUSDC, LINKUSDC, LTCUSDC, NEARUSDC, NEOUSDC, ORDIUSDC,
PENGUUSDC, PNUTUSDC, SOLUSDC, SUIUSDC, **SXPUSDTSETTLED**, TIAUSDC, TRUMPUSDC,
UNIUSDC, WIFUSDC, WLDUSDC, WLFIUSDC, XRPUSDC, ZECUSDC.

**14 nama SETTLED yang terhenti:** AERGOUSDTSETTLED, AIAUSDTSETTLED,
BDXNUSDTSETTLED, BNXUSDTSETTLED, CTKUSDTSETTLED, CVCUSDTSETTLED,
CVXUSDTSETTLED, ICPUSDT_SETTLED, LITUSDTSETTLED, MAVIAUSDTSETTLED,
MINAUSDTSETTLED, PUMPUSDTSETTLED, SLPUSDTSETTLED, TLMUSDTSETTLED.
**Satu yang HIDUP:** `settled_hidup` = [{`SXPUSDTSETTLED`, bulan_terakhir
**2026-06**, cacah_bulan **1**}].

**Peristiwa yang menyatukan dua serpihan lama:** `SXPUSDT` berhenti terbit
2026-05; `SXPUSDTSETTLED` mulai terbit 2026-06 dengan tepat satu bulan. Selisih
128 lawan 129 bukan cacat pembukuan melainkan **satu peristiwa penamaan yang
sedang berlangsung pada bulan tutup semesta**.

`MATICUSDC` satu-satunya USDC terhenti, dan `MATICUSDT` ada di antara 28 — dua
kuota, satu nama dasar, berhenti bersama. Penjelasan penggantian lambang MATIC
menjadi POL adalah **ASUMSI**; yang terukur hanya kedua nama berhenti terbit, dan
keberadaan `POLUSDT` di dalam 787 belum diperiksa.

## H-A013 — MENANG 6–0, tetapi TAFSIRNYA DICABUT [v38]

Sumber: `bulan_settled.py` V1 (blob `80e8d8bb`), commit `9bdab113`, run
30448334739, laporan blob `df2d2bfa` (UTUH).

| simbol | bulan peralihan | saudara SETTLED | bulan saudara | cocok | **bulan terakhir simbol [v38]** |
|---|---|---|---|---|---|
| CTKUSDT | 2025-04 | CTKUSDTSETTLED | 2025-04 | ✅ | **2026-06, masih terbit** |
| CVCUSDT | 2025-05 | CVCUSDTSETTLED | 2025-05 | ✅ | **2026-06, masih terbit** |
| CVXUSDT | 2025-07 | CVXUSDTSETTLED | 2025-07 | ✅ | **2026-06, masih terbit** |
| LITUSDT | 2025-12 | LITUSDTSETTLED | 2025-12 | ✅ | **2026-06, masih terbit** |
| MAVIAUSDT | 2025-03 | MAVIAUSDTSETTLED | 2025-03 | ✅ | **2026-06, masih terbit** |
| SLPUSDT | 2025-07 | SLPUSDTSETTLED | 2025-07 | ✅ | **2026-06, masih terbit** |

`cacah_cocok_bulan` 6 · `ambang_menang` 4 · `menang` true ·
`definisi_dapat_dibedakan` **false** — kemenangan sempit, satu jalur sebab.
**`cacah_peralihan_terhenti` = 0.**

**RANTAI PELEMAHAN TAFSIR, LENGKAP:**

1. semula "delapan kebangkitan" (simbol mati lalu hidup kembali);
2. sesudah R-248 dan KC-18 → "dua bersambung dan enam peralihan nama", kecocokan
   bulan hanya membuktikan PENAMAAN kontrak;
3. **[v38] sesudah R-276 → bukan peralihan sama sekali:** keenam kejadian adalah
   **penambahan nama kontrak selesai sementara nama aslinya terus terbit**. Bukan
   penggantian, bukan kebangkitan. Frasa "enam peralihan nama" DILARANG diwarisi
   tanpa keterangan ini (aturan 68).

DUA konvensi nama hidup berdampingan: enam saudara TANPA garis bawah;
`ICPUSDT_SETTLED` DENGAN; `TLMUSDTSETTLED` tanpa. Docstring `penyebut_tahun.py`
menulis `TLMUSDT_SETTLED` (salah): dicatat, TIDAK disunting, tidak diwarisi
(R-246 SEPARUH).

Silang cacah 24 nama: **24 dari 24** cocok, `cacah_gagal_daftar` 0,
`jumlah_bulan_didaftar` 518, bulan SETTLED **36**. Cacah bulan ARSIP: BNXUSDT 51
(48 di PENYEBUT — dua semesta, dua angka) · CTKUSDT 68 · CVCUSDT 68 · CVXUSDT 46 ·
ICPUSDT 62 · LITUSDT 65 · MAVIAUSDT 29 · SLPUSDT 33 · TLMUSDT 60 ·
ICPUSDT_SETTLED 9 · TLMUSDTSETTLED 9 · BNXUSDTSETTLED 6 · dua belas nama SETTLED
lain bercacah 1 (AERGO, AIA, BDXN, CTK, CVC, CVX, LIT, MAVIA, MINA, PUMP, SLP,
SXP). Cara pemilihan: SELURUH 24 nama.

## Penyebut simbol-bulan PER TAHUN — TERUKUR [v36]

Semesta `perpetual_usdt` saja (aturan 63). Sumber `penyebut_tahun` V1.

| tahun | penyebut | MATI | `bagian_mati` |
|---|---:|---:|---:|
| 2020 | 504 | 1 | 0,001984 |
| 2021 | 1.385 | 9 | 0,006498 |
| 2022 | 1.729 | 34 | 0,019665 |
| 2023 | 2.400 | 103 | 0,042917 |
| 2024 | 3.570 | 192 | 0,053782 |
| 2025 | 5.948 | 506 | 0,085071 |
| 2026 (6 bln) | 4.050 | 556 | **0,137284** |

1+9+34+103+192+506+556 = **1.401** ✅ ·
504+1.385+1.729+2.400+3.570+5.948+4.050 = **19.586** ✅ `bagian_mati` menanjak
monoton 0,20% → **13,73%**. DILARANG disebut laju kematian "pasar kripto".
`cacah_simbol_tanpa_hidup` **18** — identitasnya belum dibaca.

## Cacah baris terukur [v36] — `ukur_baris` V5

Sumber blob `c8b988ff` (UTUH), commit `404e6f1b`, run 30451749412, kode 0;
`cacah_berkas_hilang` 0, `cacah_berkas_melebihi_pagar` 0, 21 dari 21 berkas.
Definisi `len(teks.splitlines())`, pagar 800 di `tests/test_kontinuitas.py`.

`funding.py` **705**/28.121 B · `silang_funding.py` **705**/29.873 B ·
`lubang_tengah.py` V2 560 · `kohort_ekor.py` 553 · `kebangkitan.py` 552 ·
`penyebut_tahun.py` 527 · `tests/test_kebangkitan.py` 501 · `kehidupan_arsip.py`
496 · `semesta_silang.py` 423 · `kehidupan.py` 417 · `bulan_settled.py` 386 ·
`pulihkan.py` 383 · `tests/test_penyebut_tahun.py` 369 · `ukur_baris.py` 352 ·
`tests/test_semesta_silang.py` 253 · `tests/test_bulan_settled.py` 240 ·
`gerbang_1m.py` 184 · `funding_cdn.py` 162 · `arsip.py` 154 · `resample.py` 127 ·
`kohort_ringkas.py` 82. Total **8.131** ✅ Terbesar **705, SERI** — aturan 48
berlaku atas KEDUANYA; `berkas_terpanjang` menamai `funding.py` semata karena
urutan daftar (KC-26).

**Angka MATI:** `ukur_baris.py` 183/226/280 BATAL → 352; `silang_funding.py` 396
BATAL → 705; `pulihkan.py` 318 BATAL → 383; `lubang_tengah.py` 390 hanya V1 → 560.

**BELUM DIUKUR, dan utangnya bertambah [v38]:** `tests/test_lubang_tengah.py`,
`taksonomi.py`, `pecahan.py`, `semesta_kuota.py` V3, `tests/test_semesta_kuota.py`,
**`terhenti.py` V3**, **`tests/test_terhenti.py` V3 (12.202 B)**, **`survei.py`**,
`ringkas_semesta.py`. Tidak diramalkan dengan pita sempit (aturan 58 pilihan c).

## Modul dan workflow yang kini tercatat [v38]

**`lux_ai/semesta/`:** `__init__.py` 273 B (`4c2d1f25`) · `taksonomi.py` 7.086 B
(`b418c7ba`) · **`terhenti.py`** V1 5.300 B (`3fa8f697`), V2 pada commit
`8121739b`, **V3 pada commit `7b819787`**.

**30 berkas di `.github/workflows/`** (blob): bentuk_semesta `dc393dd0` ·
bulan_settled `9e0829f2` · **ci `c79497b2`** · diagnosa_kc14 `6524646a` · kc14b
`a315c25b` · kc14c `82126b60` · kc15 `c5f2ee0f` · kc6 `6bae2b1b` · funding_semesta
`c1ce55f3` · kebangkitan `282b51aa` · kehidupan `3eb10655` · kehidupan_arsip
`8234e5dc` · kohort_ekor `2e747475` · lubang_tengah `557030de` · pecahan_serapan
`cd9e21d1` · penyebut_kc6 `14617b6b` · penyebut_tahun `8f0d5852` · probe_serapan
`9b356e15` · pulihkan_rilis `32bd1099` · rentang_kc6 `db1e77ae` · ringkas_semesta
`d6145d28` · semesta_kuota `b7e5a65a` · semesta_silang `babf08e4` · serap_pilot
`85694e0f` · silang_funding `23f8c870` · survei_semesta `a1fb0192` ·
**taksonomi_semesta `b066b4db`** · **terhenti_semesta `baef4f41`** · uji_resample
`121f3e25` · ukur_baris `f62be605`.

`terhenti_semesta.yml`: `paths` = [`lux_ai/semesta/terhenti.py`, dirinya sendiri],
`workflow_dispatch`, timeout 20 menit, menjalankan `python -m
lux_ai.semesta.terhenti`, lalu commit `reports/terhenti_semesta.json` berpesan
**"laporan selisih definisi terhenti [skip ci]"** dengan `git pull --rebase
--autostash`.

## API modul yang sudah terbaca dan boleh dipakai

Rincian v37 (blob `f520d5e2`) berlaku untuk `semesta_silang`, `silang_funding`
(**`baca_laporan_kehidupan`** — jalur sah menuju daftar penyebut), `arsip`
(`semesta_simbol` satu-satunya sumber daftar simbol yang sah; tanpa `requests`;
`fapi.binance.com` 451), `pecahan` (VERSI 6, `simbol_pecahan` round-robin abjad),
`taksonomi`, `semesta_kuota` V3, `penyebut_tahun`, `kehidupan_arsip`,
`kebangkitan`. Tambahan [v38]:

- **`survei` (blob `26b14940`) — PENGHASIL `reports/semesta_rentang.json`**, lewat
  `jalankan()` yang menulis `_tulis(RENTANG, {"rentang": rentang})` dari
  `survei_rentang()`; `LAPORAN` `survei_semesta.json`, `PROGRES`
  `survei_progres.json`, `JEDA_MATI_BULAN` 2, `BATAS_R8` "2026-01",
  `SIMBOL_AKHIR` [SRMUSDT, COCOSUSDT, BTSUSDT], `SIMBOL_HEADER` [BTCUSDT,
  ETHUSDT, LINKUSDT]; fungsi `bulan_dalam_rentang`, `selisih_bulan`, `terhenti`,
  `cacah_lebih_tua`, `ringkas_header`, **`satuan_stempel`** (mili 10^12..10^13,
  mikro 10^15..10^16, lain `tidak_dikenali`), `iso_dari_stempel`, `survei_rentang`,
  `ukur_bar_terakhir`, `ukur_header`. `sidik_kode` mencap arsip/klines/survei.
  Medannya SAH — tuduhan cacat atas `semesta_rentang.json` DIBATALKAN.
- **`terhenti` V3:** `VERSI` 3, `SUMBER`/`KELUARAN`, `JEDA_MATI_BULAN` 2,
  `EKOR_BULAN` 4, `BATAS_CONTOH` 20, **`BATAS_NAMA` 60**, `BERKAS_DICAP` =
  (`taksonomi.py`, `terhenti.py`), `SIMBOL_KENDALI` BTCUSDT, `JENIS_PENYEBUT`
  `perpetual_usdt`, **`PERALIHAN_H_A013`** enam nama, `R275_BATAS_BULAN` 3;
  fungsi `sidik_kode` (dua berkas), `sidik_data`, `selisih_bulan` (SALINAN survei,
  disepakatkan oleh uji), `mundur_bulan`, `terhenti_survei`, `terhenti_taksonomi`,
  `bandingkan`, `jalankan`. Medan hipotesis `r_272/273/275/276_menang` dilaporkan
  apa adanya dan TIDAK dipakai sebagai penggugur laporan.
- `ringkas_semesta` (blob `bc8f7ad7`) — SUMBER `semesta_bulan_1m.json`, BATAS_BULAN
  78, medan `cacah_kunci_ditolak_pola`; **bukan** penghasil `semesta_rentang.json`.
  `rentang_kc6.py` (blob `631ec2f3`) menulis `reports/rentang_kc6.json`, juga bukan.

## Yang berlaku tanpa perubahan dari v35–v37

Angkanya tidak ditulis ulang dari ingatan; rincian di v35 (`6523b84f`), v36
(`f0949709`), v37 (`f520d5e2`).

- **H-A012 MENANG** — 8 simbol dari 787 punya bulan MATI lalu HIDUP, kedelapannya
  `bangkit_penuh`, `cacah_bulan_antara` 0; rentetan MATI 2,2,8,10,11,13,13,29 =
  **88**; 1.313 bulan MATI sisanya belum terbukti berakhir. **Tafsirnya dicabut
  [v38] — lihat H-A013.**
- **BTCSTUSDT** — 53 bulan, 53 MATI, pemegang rekor **63** bulan MATI semesta;
  funding hilang 2022-01 lalu PULIH 2022-02.
- **133 simbol dari 787 (16,9%) punya ≥1 bulan MATI.** DUA PULUH TERATAS (aturan
  65): BTCSTUSDT 63 · SCUSDT 48 · FTTUSDT 43 · RAYUSDT 43 · CVCUSDT 29 ·
  STRAXUSDT 27 · DGBUSDT 26 · GLMRUSDT 25 · IDEXUSDT 25 · MDTUSDT 25 · RADUSDT 25 ·
  SNTUSDT 25 · STPTUSDT 25 · AGIXUSDT 24 · OCEANUSDT 24 · WAVESUSDT 24 · BTSUSDT 21 ·
  KLAYUSDT 20 · UNFIUSDT 20 · BLZUSDT 18.
- **Silang funding × kehidupan** — MATI 559 berfunding + 842 berlubang = 1.401;
  SEPI 96 + 2 = 98; HIDUP 18.054 + **33** = 18.087; 18.709 + 877 = **19.586** ✅
  877 + 3 = **880** ✅ Arah wajib dipisah: lubang→mati **96,0%** (842/877);
  mati→lubang **60,1%** (842/1.401). Lubang funding TIDAK sah sebagai penyaring
  kematian.
- **Bentuk lubang funding** — lokal atas 877: awal **45** + ekor **826** + tengah
  **6** = 877 ✅; atas 880: awal 48 + 826 + 6; selisih 3 = tiga lubang BNXUSDT di
  luar penyebut ✅ Keenam lubang TENGAH: BTCSTUSDT 2022-01 dan LITUSDT
  2025-07..2025-11; keenamnya MATI dan berklines penuh secara bentuk. **Kematian
  LITUSDT (sejak 2025-02) MENDAHULUI hilangnya funding** (aturan 61, KC-23).
- **H-A010 MENANG 5–0, definisi TEPAT** — QTUMUSDT 1, ICPUSDT 16, TLMUSDT 20,
  BNXUSDT 9, JUPUSDT 1; `funding_tanpa_klines` kosong pada kelimanya. BNXUSDT 48
  bulan di PENYEBUT dengan 3 lubang tengah 2022-04/-06/-08 yang bulannya TIDAK ADA.
- **33 HIDUP tanpa funding** — awal 33, ekor 0, tengah 0: ICPUSDT 13 · TLMUSDT 11 ·
  BNXUSDT 7 · JUPUSDT 1 · QTUMUSDT 1 = **33** ✅
- **Kehidupan semesta terserap** — `kehidupan_arsip` V1, penyebut **19.586**, MATI
  1.401, SEPI 98, HIDUP 18.087, tanpa MATI 18.185, lilin penuh **839.325.999**,
  lilin mati 61.168.123 (7,29%), `cacah_baris_cacat` **0**. Kendali 24 dari 24
  HIDUP. `bagian_mati` per pecahan 0,0418..0,1314 — karena itu 7,153% DILARANG
  dipakai sebagai laju kematian simbol mana pun.
- **Kohort puncak 2025-07** — 38 simbol, 456 simbol-bulan, MATI 456, HIDUP 0.
- **Serapan semesta** — run 30396803601, commit `57a04f1e`, `versi_pecahan` 6:
  787 simbol, **19.598** simbol-bulan, **839.842.134** baris, slot 839.855.709,
  menit hilang 13.575; lolos **19.586**, gagal **12**, 99,9388%. Zip
  26.532.925.083 B; parquet 32.706.262.375 B; nisbah 1,2327; parquet karantina
  13.247.705 B. Pemulihan run 30404071324: 29/29 aset, 29/29 sha cocok. Penyebut
  ganda: PENUH 19.586, TANPA MATI 18.185, LAYAK BACKTEST **18.087**.
- **Funding semesta (`funding.py` V6)** — run 30412188715: 880 bulan klines tanpa
  funding; 87 funding tanpa klines; penyebut 19.598; kohort puncak 51,8% dari 880;
  `uji_cdn` 10 kohort 404, 10 kendali 200 checksum cocok.
- **`kohort_ekor` V4** — pindaian ADAPTIF, pagu 60 bulan tak tersentuh; sepuluh
  bulan hidup terakhir (AGIX 2024-06, ALPACA 2025-04, AMB 2025-02, BADGER 2025-03,
  BAL 2025-03, BLZ 2024-12, BNX 2025-03, BOND 2024-11, COMBO 2025-03, DAR
  2024-12; urut ABJAD) dikuatkan `kebangkitan` V1 dengan definisi berbeda: 10 dari
  10 sama. `bangkit_kembali` 0 BUKAN bukti tak ada kebangkitan
  (`cacah_simbol_bangkit_dapat_diuji` = 0). 28 anggota kohort di luar sampel abjad
  BELUM diperiksa. **ADR-A002 §10 tidak boleh diubah atas bukti kohort semata.**
- **Definisi `jumlah_baris`** — 839.325.999 + 516.135 = **839.842.134**.
  `reports/pulihkan_pecahan_<i>.json` di git masih HASIL V1.

## Hipotesis

- H-A001 belum diuji · H-A002b GUGUR · H-A003 MENANG pada 3, GUGUR pada 9 ·
  H-A004 tak dapat diuji (451) · H-A005 GUGUR pada rentang tersampel · H-A006
  MENANG enam run · H-A008 MENANG dua kali · **H-A009 GUGUR** (559 MATI tetap
  berfunding) · **H-A010 MENANG 5–0** · **H-A011 MENANG 6–0 pada LITUSDT,
  DIBATASI** (BTCSTUSDT 0 dari 53, aturan 60) · **H-A012 MENANG** · **H-A013
  MENANG 6–0, TAFSIR DICABUT [v38]**.
- **H-A014 [BELUM DIUJI] — keenam peralihan nama adalah pergantian KONTRAK, bukan
  pergantian kehidupan pasar.** Uji tanpa unduhan: ukur kehidupan keenam bulan
  saudara SETTLED (CTKUSDTSETTLED 2025-04, CVCUSDTSETTLED 2025-05,
  CVXUSDTSETTLED 2025-07, LITUSDTSETTLED 2025-12, MAVIAUSDTSETTLED 2025-03,
  SLPUSDTSETTLED 2025-07); penyebut 6 — kecil, jadi aturan 59 wajib ditaati dan
  hasilnya ditulis sebagai kemungkinan campuran. Kelima belas nama SETTLED
  bergolongan `sisa_settled` dengan 36 bulan dan **0** di penyebut, jadi uji ini
  harus menembus semesta ARSIP. **[v38] Bahan baru yang memperkuat pertanyaannya:**
  nama dasar keenamnya TERBUKTI masih terbit, jadi H-A014 kini menguji apakah
  bulan SETTLED itu bulan tanpa perdagangan di TENGAH hidup nama dasarnya.

## Papan skor prediksi

R-1..R-120 dirinci v23 · R-121..R-149 v26 dan jurnal 56–63 · R-150..R-193 jurnal
64–75 · R-194..R-199 jurnal 76–78 · R-200..R-235 seperti dirinci v37 ·
**R-236..R-247 di jurnal 92–94** (rincian barisnya ADA DI SANA, belum disalin;
yang wajib dibawa: R-239 dan R-240 MELESET sebab KC-24, R-246 SEPARUH) ·
R-248..R-252 jurnal 95 · R-253..R-255 jurnal 96 · R-256 jurnal 97 · R-257..R-260
jurnal 98 · R-261..R-264 jurnal 99 · R-265..R-267 jurnal 101 · **R-268 jurnal 102**
· **R-269..R-271 jurnal 103** · **R-272..R-274 jurnal 104** · **R-275..R-277 jurnal
105**.

| # | Prediksi | Status |
|---|---|---|
| R-199 | `definisi_dapat_dibedakan` false pada TEPAT 2 pecahan | **MENUNGGU** |
| R-248 | H-A013: 4..6 dari 6 bulan peralihan cocok | **TEPAT** (6) |
| R-249 | bulan USDT bukan-SETTLED di arsip > 19.586 | **TEPAT** (19.749) |
| R-250 | CI 552, kode 0, commit `9bdab113` | **TEPAT** |
| R-251 | `cacah_cocok_cacah` 24 dari 24 | **TEPAT** |
| R-252 | kendali BTCUSDT ≥ 60 bulan | **TEPAT** (78) |
| R-253 | CI tetap 552 | **TEPAT** |
| R-254 | `cacah_berkas_hilang` 0 DAN melebihi_pagar 0 | **TEPAT** |
| R-255 | berkas terpanjang = `silang_funding.py` | **SEPARUH** (705 SERI) |
| R-256 | CI 552, commit STATE v36 | **TEPAT** |
| R-257 | himpunan berakhiran-USDT = penyebut 787 | **MELESET** (790) |
| R-258 | 150 hanya-arsip hampir seluruhnya BUSD/USDC | **MELESET** (80/147) |
| R-259 | kendali BTCUSDT sah pada `semesta_kuota` V1 | **TEPAT** (78) |
| R-260 | CI 584, kode 0 | **TEPAT** |
| R-261 | penyebut bersih; hanya-arsip 150; nama USDT 3 | **TEPAT** |
| R-262 | `per_kuota_hanya_arsip` 18/41/39/51/1 | **TEPAT** (MUDAH) |
| R-263 | sumbangan nama USDT hanya-arsip ≤ 60 bulan | **MELESET** (151, terbalik) |
| R-264 | CI 598, kode 0 | **TEPAT** |
| R-265 | `per_jenis_hanya_arsip` kesembilan angka | **TEPAT** |
| R-266 | `perpetual_usdt` 787 DAN luar penyebut 0 | **TEPAT** (dua arah nol) |
| R-267 | CI 610, kode 0 | **TEPAT** |
| R-268 | CI 610, kode 0, commit STATE v37 | **TEPAT** (`30459083416`) |
| R-269 | 18 angka taksonomi cocok lewat jalur berbeda | **TEPAT** |
| R-270 | non-ASCII 3 nama / 19 bulan | **TEPAT** |
| R-271 | `cacah_terhenti` taksonomi ≈ 145 | **MELESET** (**129**) |
| R-272 | BUSD 41/41 DAN SETTLED 15/15 terhenti | **MELESET** (SETTLED **14/15**) |
| R-273 | `perpetual_usdt` terhenti 40..80 | **MELESET** (**28**) |
| R-274 | CI 623, kode 0, commit `8121739b` | **TEPAT** (`30461798702`) |
| R-275 | SETTLED hidup: bulan tutup DAN cacah_bulan ≤3 | **TEPAT** (SXPUSDTSETTLED, 1) |
| R-276 | keenam nama peralihan ada di 28 terhenti | **MELESET** (**0 dari 6**) |
| R-277 | CI 630, kode 0, commit `e6b74855` | **TEPAT** (`30462427226`) |

**Total R-1..R-277** (dihitung tangan, aturan 21). Dasar v37: TEPAT 190 · MELESET
47 · SEPARUH 16 · TIDAK TERADJUDIKASI 7 · MENUNGGU 7 = **267**. Sesudah v37: enam
TEPAT baru (R-268, R-269, R-270, R-274, R-275, R-277) dan empat MELESET (R-271,
R-272, R-273, R-276):

- TEPAT 190 + 6 = **196**
- MELESET 47 + 4 = **51**
- SEPARUH **16**
- TIDAK TERADJUDIKASI **7**
- MENUNGGU **7** (R-7, R-19, R-20, **R-28**, R-36, R-37, R-199)

196+51 = 247; +16 = 263; +7 = 270; +7 = **277** ✅ N_percobaan = 0; adjudikasi
riset TETAP TERKUNCI.

**Terpraregistrasi, belum teradjudikasi: R-278** (jurnal 105) — dari 15 nama
SETTLED, **13** berpasangan dengan nama dasar yang masih terbit 2026-06 dan **2**
dengan nama dasar terhenti (`SXPUSDT`, `BDXNUSDT`); dan untuk sekurangnya 11 dari
13, bulan SETTLED-nya MENDAHULUI 2026-06. Bagian pertama MUDAH (menyalin daftar
28 yang sudah terbaca), bagian kedua BERISIKO.

**Penomoran diperjelas [v38]:** jurnal 105 menyebut R-279 untuk cacah uji V4.
Karena STATE ini memakai R-279, **cacah uji V4 menjadi R-280**. Ramalan
berikutnya sesudah R-279 adalah **R-280**.

**R-279, dipraregistrasi di sini (aturan 26, 38, 55, 56).** Pada commit BERIKUTNYA
yang menyentuh `STATE.md` — yakni commit yang memuat berkas ini — `ci.yml`
MENYALA (berkas akar, tak tersentuh `paths-ignore`) sedangkan `terhenti_semesta.yml`,
`semesta_kuota.yml`, dan `ukur_baris.yml` TIDAK, dan `reports/ci_terakhir.json`
akan melaporkan **630 butir** dengan `kode_keluar` **0**. Dasarnya: tidak ada modul
maupun berkas uji yang berubah, dan 630 sudah terverifikasi pada run 30462427226.
**Ramalan MUDAH**, disebut begitu di muka.

**Utang papan skor:** rincian baris R-236..R-247 masih hanya di jurnal 92–94.

**Catatan kejujuran [v38].** MUDAH: R-250, R-253, R-254, R-256, R-259, R-260,
R-262, R-264, R-267, R-268, R-274, R-277 — seluruhnya menyalin angka terverifikasi
atau memakai mekanisme deterministik (aturan 57). BERISIKO: R-248, R-255, R-257,
R-258, R-261, R-263, R-265, R-266, R-269, R-270, R-271, R-272, R-273, R-275,
R-276. **Empat ramalan berisiko terakhir atas himpunan yang sama kalah berturut
(R-271, R-272, R-273, R-276), dan keempatnya kalah karena SEBAB YANG SAMA:
membaca nama sebagai keadaan.** Itu bukan nasib buruk melainkan satu cacat
berulang yang kini bernama dua kali (KC-30, KC-31). R-275 adalah kemenangan
berisiko yang berdiri sendiri, dan hasilnya menamai `SXPUSDTSETTLED`.

## Jumlah uji

**630 TERVERIFIKASI [v38]** — `reports/ci_terakhir.json` blob **`bee0342e`**, run
**30462427226**, commit **`e6b74855`**, `kode_keluar` **0**, "630 tests collected
in 0.47s", ref runner `e8fb04ab`. Riwayat: 231 → … → 450 → 494 → 526 → 552 → 584
→ 598 → 610 → **623** → **630**.

`tests/test_terhenti.py`: V1 **5** butir (sudah termasuk dalam 610) → V2 **18**
(610 + 13 = 623) → V3 **25** (623 + 7 = 630), seluruhnya dicacah BERNOMOR di
docstring sebelum push. `tests/test_semesta_kuota.py` **58**;
`tests/test_lubang_tengah.py` 56 · `test_kebangkitan.py` 54 ·
`test_silang_funding.py` 49 · `test_penyebut_tahun.py` 44 ·
`test_semesta_silang.py` 32 · `test_bulan_settled.py` 26.

**Kendali negatif yang tercatat [v38]:** run **30462286751** atas commit
`7b819787` berjalan ketika `tests/test_terhenti.py` masih memuat kurung kurawal
liar; run **30462427226** atas commit perbaikan `e6b74855` memberi 630 dan kode 0.
Kedua commit ada di riwayat (aturan 29). **Catatan urutan yang wajib jujur:**
laporan `terhenti` V3 dihasilkan run atas `7b819787`, yakni SEBELUM uji V3 pernah
lulus sekali pun; modulnya sendiri sehat dan `sidik_kode` tidak berubah di antara
keduanya.

## Utang verifikasi

1-5 dan 11 menunggu tahap juri/klasifikasi. 6-23, 25-28 LUNAS. **Nomor utang ini
BUKAN nomor ramalan — lihat KC-32.**

24. **AKTIF.** LUNAS: persistensi lolos+karantina · pemulihan aset di luar runner ·
    aturan 46 di `pulihkan.py` (LUNAS DI KODE V2; laporan pecahan di git masih
    V1) · bentangan KC-18 atas kohort dan SEMESTA · penyebut kedua · daftar 33
    HIDUP tanpa funding dan 3 lubang luar penyebut · nama keenam lubang TENGAH ·
    H-A010 dan `funding_tanpa_klines` · LITUSDT 2026 · BTCSTUSDT 53/53 · H-A012 ·
    sebaran 1.401 menurut TAHUN dan SIMBOL · pencocokan `kohort_ekor` 10/10 ·
    penyebut per TAHUN · semesta arsip lawan penyebut · keberadaan keenam bulan
    peralihan · cacah baris 21 berkas · kuota dan JENIS 937 nama · identitas 3 nama
    USDT hanya-arsip · daftar `INDEKS` · penguraian 163 = 12 + 151 · kesepadanan
    787 dua arah · daftar 51 `TAK_DIKENAL`.
    **LUNAS BARU [v38]:** `reports/taksonomi_semesta.json` dibaca UTUH ·
    `reports/terhenti_semesta.json` V1 dan V3 dibaca UTUH · **penghasil
    `semesta_rentang.json` ditemukan** (`survei.py`) · **penguraian 129 terhenti dan
    808 hidup per jenis** · **daftar 28 nama penyebut yang berhenti terbit** ·
    **daftar 49 nama hidup di luar penyebut** · **identitas nama SETTLED yang masih
    terbit (`SXPUSDTSETTLED`)** · **status terbit keenam nama peralihan H-A013** ·
    **listing 30 workflow dan paket `lux_ai/semesta/`**.
    **BELUM:** pemecahan `silang_funding.py` dan `funding.py` (705, aturan 48) ·
    `ukur_baris` V6 (KC-26 + sembilan berkas belum terukur) · daftar 147 nama
    hanya-arsip · identitas 18 simbol tanpa bulan HIDUP · kehidupan keenam bulan
    saudara SETTLED (H-A014) · pencocokan selisih 12 dengan 12 simbol-bulan
    karantina (periksa NAMA dan BULAN) · apakah 50 kontrak bertanggal pernah masuk
    perhitungan mana pun · pencocokan 3 lubang BNXUSDT dengan KC-15 · kehidupan 12
    simbol-bulan karantina · `funding_ada` masih null di seluruh manifes ·
    `dugaan_pengganti` (ADR-A005) · pemulihan harian ADR-A007 · karantina artefak
    7 hari · 28 anggota kohort di luar sampel abjad · **bunyi ramalan R-28 dari
    STATE v23 (KC-32)** · `reports/semesta_rentang.json`, `ringkas_semesta.json`,
    `survei_semesta.json`, `survei_progres.json`, `rentang_kc6.json`,
    `semesta_kuota.json` penuh, `semesta_silang.json` penuh, `penyebut_tahun.json`
    penuh, `bulan_settled.json`, `diagnosa_kc15.json`, `kohort_ekor.json`,
    `funding_selisih_penuh.json`, `tests/test_pulihkan.py` — belum pernah dibaca.
    Cacat penulisan yang dicatat dan TIDAK disunting: docstring R-225 ("tujuh
    fungsi" lalu sembilan nama; yang benar sembilan) dan docstring
    `penyebut_tahun.py` (`TLMUSDT_SETTLED`).
    Mengadjudikasi R-7, R-19, R-20, R-28, R-36, R-37.

## Daftar ADR

- ADR-A001 aturan dasar. DITERIMA.
- ADR-A002 serapan. DITERIMA; §3 DIAMANDEMEN oleh A004 lalu A007; §9 DIGANTI oleh
  A006 Keputusan 3. **§10 belum disentuh dan tetap tidak boleh disentuh atas bukti
  kohort semata;** bila kelak disunting, WAJIB menyebut batas `perpetual_usdt`.
- ADR-A003 taksonomi rezim. BELUM ADA (nomor dicadangkan). Wajib memisahkan
  "kontrak berganti nama" dari "pasar hidup kembali", wajib memakai taksonomi
  INSTRUMEN kanonik yang sudah ada (KC-29), dan **[v38] wajib memuat aturan 68:
  nama turunan dapat terbit BERSAMAAN dengan nama asal, sehingga "berganti nama"
  sendiri ternyata bukan gambaran yang benar bagi keenam kasus H-A013.**
- ADR-A004 kebijakan KC-6. DITERIMA. ADR-A005 jenis instrumen tahap pertama.
  DITERIMA. ADR-A006 karantina + persistensi. DITERIMA, DITERAPKAN, TERVERIFIKASI
  DARI LUAR.
- **ADR-A007 serapan hibrida. DIUSULKAN**, belum diterima; wajib memperhitungkan
  temuan `jumlah_baris` dan kendala R-146.
- **ADR-A008 akibat KC-18. Keputusan 1–6 DITERIMA [v28]**; Keputusan 5 bersemesta
  18.087. **Keputusan 7 BERCABANG DUA** — bentuk TENGAH dapat menandai jeda yang
  berakhir (LITUSDT) ATAU funding yang pulih tanpa perdagangan (BTCSTUSDT 53/53).
  Keputusannya WAJIB memuat kedua cabang, WAJIB per simbol-bulan, DILARANG
  menyebut funding dan perdagangan berhenti "serentak", WAJIB menyebut batas
  `perpetual_usdt`, WAJIB memakai aturan 66 bentuk revisi, dan **[v38] WAJIB
  memakai aturan 67 dan 68: LITUSDT masih terbit pada 2026-06 meski MATI
  2025-02..2025-11, jadi "berhenti terbit" dan "mati" tidak boleh dipertukarkan.**
- ADR berikutnya **A009**.

## Temuan sampingan yang belum diukur

- **Kehidupan keenam bulan saudara SETTLED (H-A014)** — pertanyaan paling murah
  yang tersisa; bahannya sudah di-commit.
- **[v38] Mengapa `SXPUSDT` berhenti pada 2026-05, dan siapa 4 nama pada ekor
  2026-03 (1) dan 2026-04 (3)** — keempatnya belum bernama.
- **[v38] Apakah `POLUSDT` ada di dalam 787**, yang akan menguji dugaan
  penggantian lambang MATIC (MATICUSDT dan MATICUSDC berhenti bersama).
- **[v38] Asal-usul angka "16 simbol non-ASCII"** yang kini DICABUT menjadi 3
  nama / 19 bulan.
- Daftar 147 nama hanya-arsip bukan-akhiran-USDT; 18 simbol tanpa bulan HIDUP.
- Apakah selisih **12** benar-benar himpunan 12 simbol-bulan karantina.
- Apakah 50 kontrak delivery bertanggal pernah masuk perhitungan mana pun.
- Mengapa dua dari enam bulan peralihan jatuh pada **2025-07**, bulan tebing
  funding dan bulan kohort puncak.
- Sebab kebangkitan/peralihan kedelapan simbol (di luar jangkauan arsip).
- Apakah 3 lubang BNXUSDT (2022-04, -06, -08) sama dengan 3 simbol-bulan KC-15.
- Kehidupan 12 simbol-bulan karantina; `bulan_hidup_terakhir` 28 anggota kohort di
  luar sampel abjad.
- 15 nama SETTLED: dua belas bercacah satu bulan; **dua di antaranya kini
  diketahui berpasangan dengan nama dasar yang terhenti** (SXPUSDT, BDXNUSDT).
- **Saham, ETF, dan komoditas token masih terhitung `perpetual_usdt`**
  (`taksonomi.CATATAN_BATAS`); memisahkannya menuntut daftar instrumen dari bursa.
- `.decode("utf-8","replace")` di `klines` membungkam byte rusak.
- Apakah BUSD/USDC layak digabung dengan USDT — kini berangka: 80 nama, 1.705
  bulan (812 + 893); **dan 38 dari 39 USDC masih HIDUP**, jadi pertanyaannya bukan
  lagi tentang pasar mati.
- Sebab KC-14 (H-A004) tak dapat diuji; sebab KC-15 tidak diketahui.
- Selisih penyebut diagnosa KC-15: 38 diperiksa, 41 dirancang.
- `funding_selisih_penuh.json` belum dibaca; `daftar_terpotong` true (500 dari 880).
- Selisih byte funding AGIXUSDT 531 lawan 529.
- `waktu_utc` runner berjalan lebih dulu daripada jam sesi.
- **[v38] Satuan stempel mikrodetik lawan milidetik** (`survei.satuan_stempel`;
  `reports/survei_semesta.json` belum dibaca).
- `tests/test_pulihkan.py` belum pernah dibaca ulang sesudah push.
