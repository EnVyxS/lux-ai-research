# STATE lampiran EKOR — bagian 2 dari STATE (v20, milik STATE v62)

**UTANG PENAMAAN LUNAS.** Kepala berkas ini berdiri di **v19** selama dua kenaikan
STATE (v61 dan v62) sambil berbunyi "milik STATE v60". Kepala di atas **sudah
dinaikkan**, dan sejak baris ini **trio akar serasi pada NAMA maupun ISI** — pertama
kalinya sejak v56. UKUR v20 wajib menyusul; sampai ia naik, keserasian nama masih
**dua dari tiga**.

Dasar v20: EKOR v19 (blob **`e19c5573966d835e9d40eadcb55165ab7d79f0de`**, commit
**`b8877a2710544723ce81fc44ad505fa08fb7828b`**), **dibaca UTUH pada giliran yang sama
sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43).

**BERKAS INI SENGAJA PADAT** — penangkal butir 19. Bagian warisan **dirujuk ke blob
v19, BUKAN disalin ulang**.

**Apa yang v20 kerjakan:**

1. **Mengesahkan papan skor 339** — naik sepuluh dari 329, dari **dua** ramalan.
2. Membukukan **R-319** (2 TEPAT / 2 MELESET / 1 TIDAK TERADJUDIKASI) dan **R-320**
   (**5 TIDAK TERADJUDIKASI** — pertama kalinya sebuah ramalan gugur **seluruhnya**).
3. Menyerap **ADR-A022**: empat aturan RESMI, dua KC DIBUANG, satu kelas bahan baru.
4. Membukukan **aturan 38 ke-65, ke-66, ke-67, ke-68**.
5. Melahirkan **utang verifikasi 47, 48, 49**; mengusulkan **KC-59**.

**Kalimat yang wajib dibaca lebih dulu.** v19 mencatat kemenangan terbesar sesi ini dan
memperingatkan agar tidak dibaca sebagai mutu. v20 adalah kebalikannya, dan
peringatannya berlaku ke arah sebaliknya: **sepuluh butir masuk papan skor dan hanya
dua yang menang.** Enam belas butir kini berstatus TIDAK TERADJUDIKASI — naik dari
sepuluh. **Lajur yang tumbuh paling cepat di berkas ini bukan lajur kalah, melainkan
lajur tidak pernah diuji.** Itu keterangan tentang **cara kerja**, bukan tentang alam.

## KESERASIAN VERSI

1. `STATE.md` **v62** — blob **`a762c129914b9adfa8175b4746ba219d6e80f775`**, commit
   **`f5019bb6e4839a12521abb182484129519a9a14f`**. Memuat **339**; menyatakan diri
   **belum sah** sampai berkas ini naik. **Kini SAH.**
2. `STATE_LAMPIRAN_EKOR.md` **v20** — berkas ini.
3. `STATE_LAMPIRAN_UKUR.md` masih **v19 PADAT** — blob
   **`47df297d146697749643019d0bda216c5a88059a`**, commit
   **`9d159e1edb6bfff58bb643409c3b86b8a9cd661d`**, kepala "milik STATE v60".
   **TERTINGGAL TIGA VERSI ISI.** Ia **tidak memuat**: rantai `pecahan.jalankan`;
   pembacaan `serap.py`, `klines.py`, `pecahan.py`; tabel dua belas karantina;
   `sebaran_pelanggaran` 12/12; pendamaian 49/50; kelas kegagalan **PENOLAKAN PENUH**.
   **Sampai UKUR v20 naik, sumber sah untuk seluruh butir itu adalah STATE v62,
   jurnal 154–157, dan berkas ini** — bukan UKUR v19.
4. `STATE_LAMPIRAN_ADR.md` (`a02ef271`) dan `PROMPT_KELANJUTAN.md` (`35beed44`) —
   **arsip; BUKAN sumber**.

**Satu berkas per push tetap MENGIKAT.** Push berkas ini menyalakan `ci.yml`; tidak satu
pun `tests/**` berubah → cacah uji tetap **1377**, deterministik, **MUDAH**, TIDAK
diskor. Laporannya WAJIB dibaca sebelum push akar berikutnya (aturan 38 **ke-69**) dan
**WAJIB DITOLAK bila medan `commit` tidak cocok** (aturan 90).

## PAPAN SKOR — R-319 dan R-320 dibukukan

Baris R-199..R-318 dirujuk ke blob v19 **`e19c5573966d835e9d40eadcb55165ab7d79f0de`**,
tidak berubah. Dua baris baru:

| # | Prediksi | Status |
|---|---|---|
| **R-319** | (1) `test_gerbang_1m.py` **nol** penyebutan BNXUSDT; (2) ADR-A004 memuat **sekurangnya satu** nama pemanggil gerbang; (3) cacah uji berkas itu di pita **35–70**; (4) klausa penjatuh BNXUSDT dinamai oleh salah satu bahan; (5) utang ukur 25 tetap hidup sesudah giliran itu | **2 TEPAT / 2 MELESET / 1 TIDAK TERADJUDIKASI** — nol penyebutan **TEPAT** · **NOL** nama pemanggil **MELESET** · **16** uji, di bawah tepi bawah sejauh **19**, **MELESET** · butir 4 **TIDAK TERADJUDIKASI** · butir 5 **TEPAT** |
| **R-320** | (1) `daftar_karantina` hadir di manifes; (2) medan cacah karantina per pecahan terisi; (3) sebaran karantina antarpecahan; (4) `selisih_cacah_bulan` = 0; (5) pecahan ber-BNXUSDT memuat `cacah_karantina` ≥ 3 | **5 TIDAK TERADJUDIKASI dari 5** — kedelapan `reports/manifes_pecahan_*.json` **DITOLAK ALAT**; tidak satu butir pun pernah diuji |

**Total R-1..R-320** (dihitung TANGAN, aturan 21):

- TEPAT **229**
- MELESET **65**
- SEPARUH **22**
- TIDAK TERADJUDIKASI **16**
- MENUNGGU **7** (R-7, R-19, R-20, R-28, R-36, R-37, R-199)

Aritmetika terbuka, dua jalur:
- Jalur penjumlahan: 229 + 65 = 294; 294 + 22 = **316**; 316 + 16 = 332; 332 + 7 = **339** ✅
- Jalur pertambahan: papan v19 **329** + R-319 **5** + R-320 **5** = **339** ✅
- Rincian TEPAT: 227 + 2 (R-319) + 0 (R-320) = **229** ✅
- Rincian MELESET: 63 + 2 (R-319) + 0 (R-320) = **65** ✅
- Rincian TIDAK TERADJUDIKASI: 10 + 1 (R-319 butir 4) + 5 (R-320) = **16** ✅
- SEPARUH **tidak bergerak**: 22 → 22 ✅

Nomor terpakai R-1..R-320. N_percobaan = 0. **ADJUDIKASI RISET TETAP TERKUNCI.**

**PAPAN SKOR 339 DISAHKAN DI SINI** (aturan 29).

**Nisbah, dihitung tangan:** dari **316** ramalan beradjudikasi penuh (229 + 65 + 22),
TEPAT **72,5%**, MELESET **20,6%**, SEPARUH **7,0%** (pembulatan berjumlah 100,1%).
v19: 72,8 / 20,2 / 7,1. **TURUN 0,3 poin.**

**TIGA PERINGATAN YANG WAJIB MELEKAT.**
1. Penurunan itu **DILARANG dibaca sebagai kalibrasi memburuk**, persis seperti kenaikan
   dilarang dibaca membaik (KC-51).
2. **R-320 tidak menggerakkan nisbah sama sekali** — nol butirnya masuk pembilang
   maupun penyebut. **Nisbah yang diam bukan tanda kestabilan; ia tanda ketiadaan
   pengukuran.** Membaca 72,5 sebagai "bertahan di tengah dua ramalan" adalah salah:
   ia bertahan karena **satu dari dua ramalan itu tidak pernah terjadi**.
3. **R-312 dan R-320 DILARANG masuk pembilang maupun penyebut.**

**Kolom terpisah — DI LUAR lajur papan skor:** R-229 TEPAT, R-230 MELESET (ADR-A020
kep. 5). **R-228, R-288, R-290, R-291, R-305 tetap BELUM diadjudikasi tangan.**
**[v20] Bertambah:** blok `uji_r291` di `karantina_semesta.json` melaporkan `menang`
**true** (terukur 12 = diramalkan 12, `terukur_tak_diramalkan` kosong) **dan menandai
R-291 BERISIKO sendiri**. **Itu vonis alat, bukan adjudikasi** — sejajar `uji_r305` dan
`uji_r288`. **R-291 tidak masuk lajur mana pun di sini** (KC-49).

### [v20] R-320 — kegagalan yang paling banyak mengajar sesi ini

Tidak satu butir pun pernah diuji. Kedelapan manifes **ditolak alat**, bukan dipotong:
`too large to display`. Terkecil **2.257.314 B**, terbesar **2.865.596 B**, jumlah
tangan **20.533.802 B**. Pembaca kedua atas URL mentah menjawab `Content not available`
— repo tertutup, jalur itu **mati sama sekali**.

**Sebab, telanjang:** delapan berkas didaftarkan sebagai bahan **tanpa satu pun
ukurannya diperiksa**, padahal ukuran tersedia murah lewat daftar direktori. Penyusun
bahkan menyiapkan penangkal — mengurutkan `daftar_karantina` sebelum `manifes` menurut
abjad — **untuk kelas kegagalan yang salah**. Yang disiapkan penangkal **pemotongan**;
yang datang **penolakan**.

**Aturan 91 dikutip pada ramalan yang gagal, bukan yang menang:** cacah bukti bebas
maksimum **TIGA**; yang diuji **NOL dari tiga**. **DILARANG menyamakan "nol menang"
dengan "nol diuji".**

**Yang DILARANG disimpulkan:**
1. **DILARANG** menyatakan `manifes_pecahan_*` tak memuat jawabannya. Ia memuatnya;
   yang terbukti hanyalah **alat ini tak sanggup membacanya**.
2. **DILARANG** menghitung R-320 sebagai bukti aturan 88/89/91 bekerja **maupun** gagal.
   Aturan-aturan itu mengatur **isi** praregistrasi; yang runtuh adalah **jangkauan
   bahan**.
3. **DILARANG** mengubah vonis butir mana pun sesudah `karantina_semesta.json` dibaca.
   Lihat larangan terpenting di bawah.

### [v20] LARANGAN TERPENTING — empat butir R-320 yang "akan menang"

Sesudah adjudikasi selesai, `reports/karantina_semesta.json` dibuka — **melanggar aturan
21**, diakui di STATE v62 dan jurnal 157. Isinya menunjukkan butir **1, 2, 3, dan 5**
akan **TEPAT** seandainya bahannya terjangkau; butir 3 bahkan menyebut pasangan klausa
**tepat sasaran**, dan butir 5 meminta `cacah_karantina` ≥ 3 pada pecahan ber-BNXUSDT —
pecahan **6**, terukur **3**.

> **Fakta itu dicatat sebagai kejujuran dan DILARANG DIHITUNG.** DILARANG masuk papan
> skor · DILARANG dihitung sebagai bukti bebas · DILARANG dipakai memperbaiki nisbah ·
> DILARANG dipakai menyebut R-320 "sebenarnya benar". Vonis tetap **lima dari lima
> TIDAK TERADJUDIKASI, permanen**. **Ramalan yang bahannya tak terbaca pada waktunya
> bukan ramalan yang menang terlambat; ia ramalan yang tak pernah diuji.** Menskorkannya
> sesudah melihat jawabannya adalah persis kecurangan yang aturan 21 ada untuk
> mencegahnya.

Presedennya sudah ada dan diikuti: butir 3 R-317 **tetap kalah** sekalipun butir 18
menjelaskan sebabnya (v19, catatan kejujuran 3). **Sebab boleh dicatat; vonis tidak
boleh disentuh.**

### [v20] R-319 — aturan 91 dipakai pertama kali, dan hasilnya menghukum penulisnya

Butir 4 dan 5 dinyatakan **berkorelasi** di praregistrasi; keduanya bergerak bersama.
Butir 2 dan 3 **bebas — dan KEDUANYA KALAH**. **Dari dua butir yang benar-benar bebas,
NOL menang.** Satu-satunya TEPAT tak berkorelasi adalah butir 1, butir termudah.

**Sebab kekalahan butir 3, telanjang:** penyusun menyamakan **jumlah klausa yang diuji**
dengan **jumlah uji**, lalu menyandarkannya pada kebiasaan modul berat 44–68. **Modul
berat di repo ini berat karena banyak MEDAN LAPORAN, bukan banyak klausa.** Terukur
**16** lawan tepi bawah **35**; selisih **19**.

**Sebab kekalahan butir 2:** ADR-A004 memuat **NOL** nama pemanggil gerbang. Dokumen
keputusan di repo ini menetapkan **kebijakan**, bukan **rantai panggilan**. Praduga
bahwa ADR memuat rantai panggilan **tidak berdasar** dan tidak pernah diperiksa.

**KC-51 tidak terpicu:** kekalahan butir 3 adalah taksiran **terlalu tinggi** (35–70
lawan 16), searah dengan pembalikan yang dicatat v19. **Dua titik berlawanan arah bukan
sebaran; DILARANG menyebut arah bias berubah.**

## ADR-A022 — DITERIMA; dampaknya pada berkas ini

Blob **`fd24bb5bbbba24e7e01bcb3d0b9050f83147d017`**, commit **`f92c0dcf…`**, dua belas
keputusan. Teks penuh dirujuk ke blobnya. Yang mengubah lampiran ini:

- **Aturan 88, 89, 91 RESMI; aturan 92 RESMI DIPERSEMPIT** (hanya penanda penutup
  wajib). Ketiga usulan yang v19 tahan di satu kejadian **kini diresmikan atas dasar
  MANFAAT TERUKUR** — kebijakan baru, kep. 1. **Ambang KC tidak berubah: dua kejadian.**
  **DILARANG memakai kep. 1 untuk meresmikan KC mana pun.**
- **KC-56 DIBUANG** (kep. 7) — tak pernah terpicu. **KC-57 DIBUANG** (kep. 9) — menjelma
  syarat praregistrasi butir 13. **Keduanya DILARANG dikutip sebagai usulan hidup.**
- **KC-58 DITUNDA** ke ADR-A023 (kep. 10). Rumusan penuhnya tetap di v19; bahannya
  utang verifikasi 46.
- **KC-52 DIPERSEMPIT, bukan dicabut** (kep. 11) — lunas untuk BNXUSDT saja = **0,127%**
  dari 787. **DILARANG menulis KC-52 dicabut atau terselesaikan.**
- **`semesta_rentang.json` → kelas resmi BAHAN TAK BERSAKSI** (kep. 8). Wajib disebut
  demikian **setiap** dikutip. **DILARANG memperluas kelas ini sekarang** — utang
  verifikasi 49.
- **Aturan 90 DIKUKUHKAN beserta kelemahannya** (kep. 12). **DILARANG disebut "teruji".**
- **Aturan 77 dan 78 DITUNDA** ke ADR-A023 (kep. 6).

### [v20] USULAN KC-59 — satu kejadian, DITAHAN

> **KC-59 (usulan).** Pada seluruh semesta **19.598** simbol-bulan, gerbang 1m hanya
> pernah menjatuhkan lewat **satu pasangan klausa**. Empat klausa lain —
> `deret_tidak_kosong`, `tanpa_duplikat`, `selaras_menit`, `satuan_milidetik` —
> **nol kejadian**.

Bukti: `sebaran_pelanggaran` hanya memuat dua kunci, **`jarak_60_detik` 12** dan
**`tanpa_menit_hilang` 12**; klausa lain **tidak muncul sama sekali**. Dua punya sebab
struktural terukur (`tanpa_duplikat` mustahil sebab `klines.rapikan` membuang duplikat
lebih dulu; `deret_tidak_kosong` mustahil pada kedua belas ini sebab `nisbah_lilin`
terendah **0,903226**). Dua sisanya **belum bersebab terukur** dan **DILARANG disebut
mustahil**. **Akibat:** gerbang berklausa enam itu, dalam praktik, **penyaring satu
perkara**. **DILARANG menyebutnya "gerbang enam lapis" di artefak mengikat.**
**Satu kejadian; DILARANG diresmikan** (ADR-A022 kep. 1). **KC berikutnya: KC-60.**

## Catatan kejujuran [v20]

1. **Sepuluh butir masuk papan skor; dua menang.** Dan enam dari sepuluh **tidak pernah
   diuji**. Lajur TIDAK TERADJUDIKASI naik **10 → 16**, kenaikan terbesar yang pernah
   tercatat dalam satu kenaikan versi. Itu keterangan tentang **cara kerja riset ini**,
   bukan tentang alam yang ditelitinya.
2. **Empat aturan diresmikan pada giliran yang sama ketika dua di antaranya dilanggar
   penulisnya sendiri.** Aturan 89 diresmikan ADR-A022, lalu **dilanggar satu giliran
   sesudahnya** (butir 21: pita R-320 butir 2 dan 4 tak menutup sisi "bahan tak
   terjangkau"). **Meresmikan aturan bukan menaatinya.**
3. **Aturan 21 dilanggar, dan pelanggarannya lahir dari upaya mematuhi aturan 93.**
   Usulan aturan 93 rumusan pertama menyuruh memeriksa ukuran **tanpa menyebut caranya**;
   panggilan yang dipakai justru membuka isi. **Aturan yang dirumuskan setengah jalan
   tidak melindungi — ia mengarahkan ke lubang lain.** Rumusan kedua menutupnya.
4. **Tiga utang ukur tertua lunas sekaligus (25, 28, 29) — dan seluruhnya dibayar dengan
   bahan yang dibuka melanggar aturan 21.** Keuntungan pengetahuan itu nyata; ongkos
   proseduralnya juga nyata. **DILARANG menghitung yang pertama tanpa menyebut yang
   kedua.**
5. **Dugaan A4 terkonfirmasi nama demi nama** (12 = 11 bulan absen + 1 tepi BNXUSDT
   2022-04) **dan DILARANG diskorkan** — tidak diregistrasi, dan bahannya dibuka sesudah
   adjudikasi.
6. **Aturan 52 ditaati empat puluh empat kali berturut**, empat puluh lima dengan berkas
   ini. Sejak butir 19 **tanpa satu pun kelalaian**.
7. **Aturan 57 beruntun 4 dari 4, tidak bertambah** — tidak ada `tests/**` yang berubah.
8. **`PROMPT_KELANJUTAN.md` tetap belum berkepala "ARSIP — BUKAN SUMBER"** dan
   `PROMPT.md` **v55 belum didorong**. Umur utang kini **dua belas versi**, naik satu
   sejak v19. Disebut setiap kali, tidak dikerjakan setiap kali — **cacat proses, dan
   menyebutnya berulang tanpa mengerjakannya adalah cacat kedua.**
9. **Pemeriksaan silang yang menutup tanpa sisa [v20]:**
   3+3+0+1+1+0+3+1 = **12** karantina ✅ · **19.586 + 12 = 19.598** ✅ ·
   11 bulan absen + 1 tepi = **12** ✅ · 43.200 − 41.760 = **1.440** ✅ ·
   44.640 − 40.320 = **4.320** ✅ · jumlah delapan manifes = **20.533.802 B** ✅
   **Yang TETAP TIDAK menutup:** `selisih_absen_pasangan_jurnal_113` = **−1**;
   mengapa dua dari tiga bulan BNXUSDT kehilangan **hari bulat penuh** (utang ukur 30);
   apakah 16 uji `test_gerbang_1m.py` termasuk dalam **1377** (utang ukur 27).
10. **Tidak ada kegagalan panggilan alat GitHub sepanjang sesi ini.** Satu-satunya
    kegagalan pembacaan: `web.loadPage` atas URL mentah — repo tertutup.

## Jumlah uji

**1377 TERUKUR, kini DUA PULUH EMPAT bacaan berjejak (ke-45..ke-68).** Aritmetika
tangan: 68 − 45 = 23; 23 + 1 = **24**.

Bacaan ke-45..ke-64 tercatat di v16–v19. Empat yang terbaru:

22. blob **`87677ef656439ff30eb0c1a6788a5c324fdca702`**: run **30595169680**, commit
    **`b8877a27`** (EKOR v19), **2026-07-31T01:01:01Z**, kode 0, `1377 in 0.47s`.
23. blob **`d241b08efbc05588d5dd23d85c48415c05b25665`**: run **30607412702**, commit
    **`9d159e1e`** (UKUR v19 padat), **05:40:05Z**, kode 0, `1377 in 0.57s`.
24. blob **`2ba9b4eb125b36f576c4da075e5da09f229f9336`**: run **30608117432**, commit
    **`bb959b62`** (STATE v61), **05:55:30Z**, kode 0, `1377 in 0.61s`.
25. blob **`939d08dd55fe5b93415c006f205476a8a091bcb4`**: run **30615282607**, commit
    **`f5019bb6e4839a12521abb182484129519a9a14f`** (STATE v62), **08:09:20Z**, kode 0,
    `1377 tests collected in 0.65s`.

Turunan: 1341 + **36** butir `test_selisih_lilin.py` = **1377** ✅

Cacah per berkas uji dirujuk ke v19 — tidak berubah.
**[v20] `tests/test_gerbang_1m.py` DIBACA UTUH**, blob
**`a930af172fa51ca643384c7be30283958a225e46`**, **16 butir**. **Apakah 16 itu termasuk
dalam 1377 BELUM diukur (utang ukur 27); DILARANG menjumlahkan 1377 + 16.**
**`tests/test_lubang_tengah.py`** — 56 butir menurut R-228, **BELUM DIBACA**, dilarang
dikutip terukur.

### ORDINAL ATURAN 38 — buku besar, kini sampai ke-68

Baris ke-55..ke-64 dirujuk ke v19. Empat baris baru:

| ke- | CI | run | commit | blob | jejak |
|---|---|---|---|---|---|
| **65** | **1377** | **30595169680** | **`b8877a27`** | **`87677ef656439ff30eb0c1a6788a5c324fdca702`** | **EKOR v19** |
| **66** | **1377** | **30607412702** | **`9d159e1e`** | **`d241b08efbc05588d5dd23d85c48415c05b25665`** | **UKUR v19 padat** |
| **67** | **1377** | **30608117432** | **`bb959b62`** | **`2ba9b4eb125b36f576c4da075e5da09f229f9336`** | **STATE v61, v62** |
| **68** | **1377** | **30615282607** | **`f5019bb6`** | **`939d08dd55fe5b93415c006f205476a8a091bcb4`** | **berkas ini** |

**Pemakaian berjalan = ke-enam puluh delapan.** Ke-68 dibaca atas push **STATE v62**,
`commit` **COCOK pada percobaan pertama**, kode keluar **0**.

**Panjang deret berjejak tanpa laporan hangus (butir 17):** ke-42..ke-68 → 68 − 42 = 26;
26 + 1 = **27 pembacaan berturut**.

**Aturan 90 kini dipakai TUJUH kali sesudah peresmian** (ke-62..ke-68), **nol nyala**.
ADR-A022 kep. 12 mengukuhkannya beserta kelemahannya. **DILARANG disebut "teruji".**

**Bot CI menambah satu commit di atas tiap push pemicu** — kini **dua puluh dua kali
berturut** (terbaru `2da162ed`, `72e49824`, **`27c7a7eb1b8759af094f21be4b22715c9d9b9139`**).
Deterministik dari `ci.yml`; **DILARANG dihitung sebagai kemenangan ramalan.**
**Push `journal/**` dan `decisions/**` TIDAK menyalakan CI** — jurnal 152–157 dan
ADR-A022 tidak menghasilkan commit bot, terukur dari `paths-ignore`.

**Tiga cacat tetap disebut apa adanya:** baris ke-**38** (run `30541051907`) **tanpa
blob**; run **30547842823** (bot `de2fc03d`) tertimpa; **laporan push `c28202df`
tertimpa sebelum dibaca** — ketiganya **DILARANG dihitung**. Deret **tidak** putus.

## Aturan 79, 85, 91 — cacah berjalan

**Aturan 79 — rekor TUJUH berturut.** R-314..R-320 seluruhnya diregistrasi di
`journal/**` **sebelum** bahan dibuka. Aritmetika: 320 − 314 = 6; 6 + 1 = **7**.
**DILARANG** menyebut aturan 79 lemah; **DILARANG** pula membacanya sebagai bukti mutu
**isi** — R-320 tertib sempurna dan gagal seluruhnya.

**Aturan 85 — EMPAT adjudikasi yang menguji tepi**, naik satu dari v19 (R-317, R-318,
**R-319**). **R-320 TIDAK dihitung** — tepinya tak pernah diuji sebab bahannya tak
terjangkau. **DILARANG** menyebut aturan 85 teruji, bekerja, atau terbukti.

**Aturan 91 — dipakai DUA kali sejak diresmikan** (R-319, R-320). Pada R-319 ia
**menyala dan menahan klaim**: kemenangan butir 4–5 tak boleh dijumlahkan. Pada R-320 ia
tak sempat berguna. **DILARANG disebut "teruji".**

## Utang verifikasi

1–5, 11 menunggu tahap juri. 6–23, 25–29, 31 LUNAS. **Nomor utang BUKAN nomor ramalan
— KC-32.** Butir 24, 30, 32–46 dirujuk ke v19; yang bergerak:

24. **AKTIF. LUNAS BARU [v20]:** `decisions/ADR-A004.md` (**`ee603a8cbe576684b99985aa605dcc57988e304d`**)
    · `tests/test_gerbang_1m.py` (**`a930af172fa51ca643384c7be30283958a225e46`**) ·
    `lux_ai/serapan/serap.py` (**`62d4c2c3ac25c4e26e242347df514055d1bbdce6`**) ·
    `klines.py` (**`cc4d9287ccb7a8ea72380399c334b4d19b5301d3`**) · `pecahan.py`
    (**`f1b49f1b8796886ddb8e0a7f30beeb07d0ed8183`**) · `reports/karantina_semesta.json`
    (**`678b665c1d32d6d5bbda0d9fd93445bcd64b2932`** — **dibuka melanggar aturan 21**) ·
    daftar `lux_ai/serapan/` UTUH · EKOR v19 dan STATE v61/v62 dibaca ulang utuh ·
    `ci_terakhir.json` ke-65..ke-68.
    **TETAP BELUM:** ADR **A002, A006, A007, A008**; `karantina_semesta.py` (14.948 B);
    `reports/manifes_pilot.json`; `diagnosa_kc6.py` dan laporannya; `rentang_kc6.py` dan
    laporannya; `rilis.py`; `arsip.py`; `ukur_baris.py`; `tests/test_lubang_tengah.py`;
    `test_pulihkan.py`; `test_rilis_karantina.py`; `test_karantina_a006.py`;
    `karantina_semesta.yml`; **`journal/2026-07-30-125.md`**; bagian `baris_mati`
    (54%); 5% `semesta_rentang.json`; 58 baris `baris_penyebut_butir_1`;
    **kedelapan `manifes_pecahan_*.json` — DI LUAR JANGKAUAN ALAT, bukan sekadar belum
    dibaca**; `reports/bulan_absen.json` (249.992 B); lima belas modul serapan.
36. **✅ LUNAS [v20] — identitas dua belas simbol-bulan karantina.** Utang ini berdiri
    sejak v14 dan diperkirakan menuntut **modul CI**; ternyata terbayar oleh laporan
    ringkas `karantina_semesta.json` yang **selama ini ada di repo**. **Pelajaran yang
    wajib dicatat: jalan memutar dicari sesudah jalan lurus dinyatakan buntu, padahal
    jalan memutar itu lebih pendek.**
45. **AKTIF** — `selisih_absen_pasangan_jurnal_113` = **−1**; jurnal 113 belum dibaca.
46. **AKTIF** — mengapa sembilan dari sepuluh simbol berabsen kehilangan tepat bulan
    settled terakhirnya (bahan KC-58, ditunda ke ADR-A023).
47. **BARU [v20]** — adakah berkas akar **lain** yang pernah terdorong terpotong tanpa
    tertangkap? **Sampai dibayar, DILARANG menyatakan butir 19 kejadian tunggal.**
48. **BARU [v20]** — asal-usul klausa `deret_tidak_kosong`, yang ada di kode tetapi
    **tidak** di ADR-A004 §2.2 (butir 20). Diperkuat oleh KC-59: nol kejadian pada
    19.598. **DILARANG menyimpulkan ia diselundupkan** sebelum dibayar.
49. **BARU [v20]** — perlukah kelas **BAHAN TAK BERSAKSI** melarang bahan itu menjadi
    masukan artefak mengikat, bukan sekadar mewajibkan label? Ditunda; **DILARANG
    memutuskan sekarang**.

**Utang ukur (penomoran terpisah, milik UKUR):** **25 LUNAS**, **28 LUNAS**,
**29 LUNAS** — tiga sekaligus pada sesi ini. **Hidup: 22** (penulis
`semesta_rentang.json`) · **26** (pola BNXUSDT bagi 786 simbol lain) · **27** (apakah
16 uji termasuk 1377) · **30 BARU** (mengapa dua dari tiga bulan BNXUSDT kehilangan
hari bulat penuh; **DILARANG menyimpulkan sebabnya**). **Berikutnya 31.**

## Daftar ADR

A001–A021 dirujuk ke v19, tidak berubah. Dua baris bergerak:

- **ADR-A022** (`fd24bb5bbbba24e7e01bcb3d0b9050f83147d017`, commit `f92c0dcf…`) —
  **DUA BELAS keputusan. DITERIMA.** Ia memutuskan **seluruh** usulan yang menggantung,
  persis seperti STATE v61 mewajibkan; tak satu pun ditunda tanpa alasan tertulis.
  Kelemahannya diakui sendiri: kep. 1 **mengubah kebijakan peresmian** di tengah sesi,
  dan empat aturan diresmikan sekaligus tanpa satu pun teruji.
- **ADR-A023 [BELUM ADA] — TERIKAT, LIMA BUTIR:** (a) aturan **77**; (b) aturan **78**;
  (c) **aturan 93 rumusan kedua**; (d) **KC-58**; (e) **KC-59**. Berwenang pula
  **mencabut** aturan 88/89/91/92 bila terbukti upacara — dan butir 21 sudah memberinya
  satu alasan untuk mempertimbangkannya. **DILARANG disusun pada giliran yang sama
  dengan adjudikasi mana pun** (ADR-A016).

## Penomoran berikutnya

Aturan resmi **1–81, 83–92** · nomor **82** dicadangkan · usulan tersisa **77, 78, 93** ·
**aturan berikutnya yang bebas 94** · KC resmi sampai **KC-55** (KC-16 kosong selamanya;
**KC-56 dan KC-57 DIBUANG**), usulan **KC-58** dan **KC-59** · **KC berikutnya KC-60** ·
hipotesis berikutnya **H-A024** · jurnal berikutnya **158** · `STATE.md` berikutnya
**v63** · EKOR berikutnya **v21** · **UKUR berikutnya v20 (utang hidup; keserasian nama
baru dua dari tiga sampai ia naik)** · PROMPT berikutnya **v55 (belum didorong, umur
dua belas versi)** · ADR berikutnya **A023** · ramalan berikutnya **R-321** ·
**papan skor 339 — SAH sejak berkas ini** · aturan 38 **ke-69** · aturan 52 **ke-45** ·
berhenti eksplisit berikutnya **ke-54**.

**Syarat praregistrasi R-321 — ENAM BELAS syarat kumulatif.** Empat belas syarat R-319
tetap berlaku (dirujuk ke v19), dengan tiga perubahan: **KC-56 DICORET** (dibuang);
**KC-57 menjadi butir 13 tersurat** (setiap kolom tabel buatan sendiri menyebut nama
medan sumber dan konvensinya); dan **DUA BARU**:

- **[15] Aturan 88, 89, 91 kini RESMI**, bukan lagi ditaati sukarela. Aturan 89 menuntut
  pita menutup **seluruh** sisi ruang — **termasuk sisi "bahan tidak terjangkau"**,
  yang butir 21 tunjukkan pernah terlewat.
- **[16] Usulan aturan 93 rumusan kedua ditaati sukarela:** ukuran tiap bahan wajib
  diketahui lebih dulu **lewat daftar direktori**, tidak pernah lewat panggilan
  pengambil isi, dan ukuran itu dicatat di praregistrasi.

**Syarat bahan R-321.** Bahan **DILARANG** berupa berkas yang sudah dibuka pada sesi
ini: `semesta_rentang.json` · `semesta_bulan_1m.json` · `gerbang_1m.py` ·
`silang_funding.json` · `lubang_awal.json` · `bulan_absen_ringkas.json` ·
`lubang_awal.py` · `bulan_absen.py` · `serap.py` · `klines.py` · `pecahan.py` ·
`test_gerbang_1m.py` · `ADR-A004.md` · **`karantina_semesta.json`** (dibuka melanggar
aturan 21 — larangan ini **tidak dapat ditawar**). Bahan **DILARANG** pula berupa
kedelapan `manifes_pecahan_*.json` selama alat belum sanggup membacanya.

— akhir `STATE_LAMPIRAN_EKOR.md` v20 —
