# STATE lampiran EKOR — bagian 2 dari STATE (v21, milik STATE v63)

**UTANG PENAMAAN LUNAS PADA GILIRAN YANG SAMA.** Kepala berkas ini dinaikkan ke
**v63** serentak dengan naiknya STATE v63, sehingga keterlambatan penamaan yang di v20
sempat dua versi kini **nol**. UKUR v21 wajib menyusul; sampai ia naik, keserasian nama
**dua dari tiga**.

Dasar v21: EKOR v20 (blob **`957b99e964bd63be567c310c29a62143c5350bf8`**, commit
**`b1d1ed3651a18884a2e4802be378db4087b2da6a`**), **dibaca UTUH pada giliran yang sama
sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43).

**BERKAS INI SENGAJA PADAT** (aturan 78). Bagian warisan **dirujuk ke blob v20 dan v19,
BUKAN disalin ulang**.

**Apa yang v21 kerjakan:**

1. Mencatat **ADR-A023 DITERIMA** — tiga aturan diresmikan, satu dipertegas, satu usulan
   KC dibuang.
2. Mencatat **papan skor 339 TIDAK BERGERAK** — tidak ada adjudikasi sejak v20.
3. Membukukan **aturan 38 ke-69, ke-70, ke-71**.
4. Membukukan **ATURAN 90 MENYALA UNTUK PERTAMA KALI** — peristiwa terpenting berkas ini.
5. Membukukan **aturan 77 dipakai pertama kali, satu giliran sesudah diresmikan**.
6. Membukukan **kegagalan panggilan alat GitHub PERTAMA sepanjang sesi**.
7. Menaikkan syarat praregistrasi **R-321 menjadi DELAPAN BELAS**.

**Kalimat yang wajib dibaca lebih dulu.** v20 mencatat bahwa lajur yang tumbuh paling
cepat adalah lajur **tidak pernah diuji**. v21 mencatat kebalikannya dalam hal kecil
tetapi nyata: sebuah aturan yang sembilan kali dipatuhi tanpa pernah berguna, pada
pemakaian **kesepuluh** akhirnya menolak sesuatu. **Sembilan kepatuhan yang tampak
sia-sia adalah harga yang dibayar untuk satu penolakan yang benar.** Itu satu-satunya
angka baru berkas ini, dan ia angka tentang **cara kerja**, bukan tentang alam.

## KESERASIAN VERSI

1. `STATE.md` **v63** — blob **`515abb2981d2c07374e6f5b7ea0a080622049580`**, commit
   **`3f5ec7e4f3a2d555b84a07524abd88f2d3c26083`**. Memuat **339 SAH**; aturan resmi
   **1–81, 83–93**; **nol usulan aturan tersisa**.
2. `STATE_LAMPIRAN_EKOR.md` **v21** — berkas ini.
3. `STATE_LAMPIRAN_UKUR.md` masih **v20** — blob
   **`56cfded0c4e8711a96d79df28d9bd4b006fc3604`**, commit
   **`8e6f583df0816e262b23ad1a0e2c68b41ea4df02`**, kepala **"milik STATE v62"**.
   **TERTINGGAL SATU VERSI.** Ia **tidak memuat**: peresmian aturan 77, 78, 93; aturan
   89 dipertegas; uji upacara; utang ukur 31; aturan 38 ke-69..ke-71; nyala pertama
   aturan 90. **Sampai UKUR v21 naik, sumber sah untuk seluruh butir itu adalah STATE
   v63, ADR-A023, dan berkas ini** — bukan UKUR v20.
4. `decisions/ADR-A023.md` — blob **`d2a5302f08442c44176a177baacc2eee0ee5df58`**, commit
   **`a8acbeba4c9999cb4ae4b899f2b70bfa2d7f30c3`**. Dibaca UTUH sebelum diserap.
5. `STATE_LAMPIRAN_ADR.md` (`a02ef271`) dan `PROMPT_KELANJUTAN.md` (`35beed44`) —
   **arsip; BUKAN sumber**.

**Satu berkas per push tetap MENGIKAT.** Push berkas ini menyalakan `ci.yml`; tidak satu
pun `tests/**` berubah → cacah uji tetap **1377**, deterministik, **MUDAH**, TIDAK
diskor. Laporannya WAJIB dibaca sebelum push akar berikutnya (aturan 38 **ke-72**) dan
**WAJIB DITOLAK bila medan `commit` tidak cocok** (aturan 90) — larangan yang sejak
giliran ini **bukan lagi teori**.

## PAPAN SKOR — 339, TIDAK BERGERAK

Seluruh baris R-1..R-320 dirujuk ke blob v20 **`957b99e964bd63be567c310c29a62143c5350bf8`**,
tidak berubah. **Tidak ada baris baru di v21.**

TEPAT **229** · MELESET **65** · SEPARUH **22** · TIDAK TERADJUDIKASI **16** ·
MENUNGGU **7** (R-7, R-19, R-20, R-28, R-36, R-37, R-199).

Aritmetika tangan: 229 + 65 = 294; 294 + 22 = **316**; 316 + 16 = 332; 332 + 7 = **339** ✅
Nomor terpakai R-1..R-320. N_percobaan = 0. **ADJUDIKASI RISET TETAP TERKUNCI.**

**Papan skor 339 tetap SAH**; pengesahannya terjadi di v20 dan tidak diulang di sini —
mengulang pengesahan tanpa adjudikasi baru adalah upacara menurut uji ADR-A023 §7.2.

Nisbah atas **316**: **72,5 / 20,6 / 7,0%**. **DIAM DUA VERSI BERTURUT.**

> **PERINGATAN YANG WAJIB MELEKAT, KINI UNTUK KEDUA KALINYA.** Nisbah ini diam bukan
> karena kalibrasi mantap, melainkan karena **tidak ada satu pun ramalan diadjudikasi
> sejak v20**. Dua giliran terakhir seluruhnya tata tertib: satu ADR, satu STATE, satu
> EKOR. **Nisbah yang diam adalah tanda ketiadaan pengukuran, dan sekarang ia diam lebih
> lama.** DILARANG membacanya sebagai kestabilan; DILARANG pula memakainya untuk
> menyatakan riset sedang tertib — tertib dan produktif adalah dua sumbu berbeda.

**R-312 dan R-320 tetap DILARANG masuk pembilang maupun penyebut.**
**Kolom terpisah:** R-229 TEPAT, R-230 MELESET (ADR-A020 kep. 5). **R-228, R-288, R-290,
R-291, R-305 tetap BELUM diadjudikasi tangan** — daftar yang tidak menyusut sejak v19.
**`uji_r291` tetap vonis alat, bukan adjudikasi** (KC-49).

## ADR-A023 — DITERIMA; DELAPAN KEPUTUSAN

Blob **`d2a5302f08442c44176a177baacc2eee0ee5df58`**, commit
**`a8acbeba4c9999cb4ae4b899f2b70bfa2d7f30c3`**. Push `decisions/**` **tidak menyalakan
CI** — terukur dari `paths-ignore` `ci.yml` (`c79497b2`), dan terbukti: tidak ada commit
bot di atasnya.

| kep. | pokok | dampak pada lampiran ini |
|---|---|---|
| 1 | **aturan 77 RESMI** | pencacahan saksi berubah; dipakai hari ini juga |
| 2 | **aturan 78 RESMI** | batas tulis ±25–45 KB kini angka mengikat |
| 3 | **aturan 93 RESMI, rumusan kedua** | syarat R-321 butir 16 naik dari sukarela ke wajib |
| 4 | **KC-58 DITUNDA**, dua syarat pematangan tersurat | usulan KC hidup tinggal satu |
| 5 | **KC-59 DIBUANG** → **utang ukur 31** | KC-59 DILARANG dikutip sebagai usulan hidup |
| 6 | **88/89/91/92 TIDAK DICABUT**; **uji upacara**; **aturan 89 DIPERTEGAS** | syarat R-321 butir 15 naik menjadi **empat sisi wajib** |
| 7 | resmi **1–81, 83–93**; **nol usulan aturan** | penomoran di bawah |
| 8 | trio wajib menyerap | STATE v63 ✅, berkas ini ✅, UKUR v21 belum |

**Yang ADR-A023 TOLAK, dan alasannya wajib diingat:** permohonan pencabutan aturan
88/89/91/92 ditolak dengan **uji upacara** — *aturan yang DILANGGAR bukan aturan
upacara; pelanggaran justru bukti bahwa ia mengikat sesuatu*. Butir kesalahan dokumen 21
karenanya menjadi alasan **mempertegas**, bukan mencabut.

## [v21] ATURAN 90 MENYALA UNTUK PERTAMA KALI — peristiwa terpenting berkas ini

Sesudah **sembilan** pemakaian tanpa satu pun nyala (ke-62..ke-70), pemakaian
**kesepuluh** menolak sebuah laporan. Rinciannya dicatat telanjang:

- Push **STATE v63** menghasilkan commit **`3f5ec7e4f3a2d555b84a07524abd88f2d3c26083`**.
- Pembacaan pertama `reports/ci_terakhir.json` pada `refs/heads/main` mengembalikan
  `run_id` **30616177405**, `commit` **`8e6f583df0816e262b23ad1a0e2c68b41ea4df02`** —
  yaitu commit **UKUR v20**, laporan **ke-70** yang sudah dibukukan.
- **DITOLAK.** Tidak dihitung sebagai ke-71. CI atas STATE v63 belum selesai; tanpa
  aturan 90, laporan basi itu akan tercatat sebagai bukti CI atas berkas yang **belum
  diuji sama sekali**.

> **Inilah tepat kelas kegagalan yang aturan 90 dirumuskan untuk menangkap**, dan ia
> menangkapnya. **Tetapi DILARANG menyebut aturan 90 "teruji".** Satu nyala dari sepuluh
> pemakaian adalah **satu kejadian**, bukan pengujian. Yang bertambah adalah **cacah
> kejadian**, bukan derajat keyakinan.

**Pelajaran yang wajib melekat:** selama sembilan pemakaian, aturan 90 tampak sebagai
biaya tanpa hasil — persis bentuk yang paling mudah dituduh upacara. Menurut uji upacara
ADR-A023 §7.2 ia **tidak pernah** upacara, sebab kepatuhan padanya selalu berpotensi
mengubah tindakan; giliran ini membuktikan potensi itu **nyata**. **Aturan yang belum
pernah menyala bukan aturan yang sia-sia; ia aturan yang belum diuji keadaan.**

## [v21] ATURAN 77 DIPAKAI PERTAMA KALI, SATU GILIRAN SESUDAH DIRESMIKAN

Laporan yang ditolak di atas berblob **`e5e015037d7af172d03e7e532775808672a22165`** —
**identik** dengan blob bacaan **ke-70**. Menurut aturan 77 ia **bukan pengukuran
kedua**, melainkan pengukuran yang sama dibaca dua kali.

**Dua alasan berdiri sendiri menolak laporan itu, dan keduanya sepakat:** medan `commit`
tidak cocok (aturan 90) **dan** blobnya identik dengan bacaan yang sudah dibukukan
(aturan 77). **DILARANG** menghitung kesepakatan itu sebagai dua bukti bebas — keduanya
membaca **satu berkas yang sama** dan karenanya **berkorelasi sempurna** (aturan 91).
**DILARANG** pula menyebut aturan 77 "teruji": ia dipakai sekali, pada perkara yang
paling mudah bagi dirinya.

## [v21] KEGAGALAN PANGGILAN ALAT GITHUB — YANG PERTAMA SEPANJANG SESI

Selama sepuluh giliran, catatan kejujuran EKOR berbunyi *"tidak ada kegagalan panggilan
alat GitHub sepanjang sesi ini"*. **Kalimat itu berhenti benar pada giliran ini, dan
koreksinya ditulis sebelum berkas ini didorong, bukan sesudahnya.**

Percobaan pertama mendorong berkas ini ditolak dengan galat verbatim:
`payload.owner should be not present, instead was "EnVyxS"` dan
`payload.repo should be not present, instead was "lux-ai-research"`.
Sebabnya: `owner` dan `repo` ikut dituliskan **di luar** `toolArguments`. **Push TIDAK
terjadi**; tidak ada commit, tidak ada berkas separuh, tidak ada laporan CI yang lahir.

**Kelas kegagalan ini BERTERIAK dan GAGAL BERSIH** — berbeda dari keempat kelas
pemotongan (aturan 78). Ia tidak melahirkan artefak cacat, jadi ia **tidak** menambah
kelas kegagalan kelima; ia hanya membuktikan bentuk panggilan yang benar tetap wajib
dijaga: `{toolName, toolArguments:{owner, repo, …}}`. Galat serupa pernah tercatat
sebagai riwayat lama (`Tool '' does not exist on this MCP server`), sehingga ini
**kejadian kedua** dari kelas yang sama sepanjang riset — **tetapi yang pertama dalam
sesi ini**, dan hanya keterangan yang kedua itu yang boleh dipakai.

## Aturan 38 — buku besar, kini sampai ke-71

Baris ke-55..ke-68 dirujuk ke v19 dan v20. Tiga baris baru:

| ke- | CI | run | commit | blob | jejak |
|---|---|---|---|---|---|
| **69** | **1377** | **30615541233** | **`b1d1ed36`** | **`c91cf8c9d3eface1e6bc1c1f81b28ede0ef3d7ca`** | **EKOR v20** |
| **70** | **1377** | **30616177405** | **`8e6f583d`** | **`e5e015037d7af172d03e7e532775808672a22165`** | **UKUR v20** |
| **71** | **1377** | **30617261973** | **`3f5ec7e4`** | **`a993ff3a7a55b3832e978e846892b47ffa968e4e`** | **STATE v63** |

Ke-69: **2026-07-31T08:13:43Z**, `1377 tests collected in 0.64s`, kode 0, bot
**`713825d64a891a38304b5c2682c6bbda846bc4b6`**.
Ke-70: **08:24:41Z**, `0.61s`, kode 0, bot
**`4dc444f0fc57cbfb5425ffcaa23e077bcfa6345b`**.
Ke-71: **08:43:06Z**, `0.64s`, kode 0, bot
**`4ec4eed8dae17cb85801e72fa66ac5dda207fa09`**. **Cocok pada percobaan KEDUA** —
percobaan pertama ditolak aturan 90, lihat di atas.

**Pemakaian berjalan = ke-tujuh puluh satu.**
**Panjang deret berjejak tanpa laporan hangus (butir 17):** ke-42..ke-71 → 71 − 42 = 29;
29 + 1 = **30 pembacaan berturut**.
**Aturan 90 dipakai SEPULUH kali sesudah peresmian** (ke-62..ke-71), **SATU nyala**.

**Bot CI menambah satu commit di atas tiap push pemicu** — kini **dua puluh enam kali
berturut** (terbaru `713825d6`, `4dc444f0`, **`4ec4eed8dae17cb85801e72fa66ac5dda207fa09`**).
Deterministik dari `ci.yml`; **DILARANG dihitung sebagai kemenangan ramalan.**
**Push `decisions/**` TIDAK menyalakan CI** — ADR-A023 tidak melahirkan commit bot,
sesuai ramalan deterministik dan karenanya **TIDAK diskor**.

**Tiga cacat lama tetap disebut apa adanya:** baris ke-**38** (run `30541051907`) tanpa
blob; run **30547842823** (bot `de2fc03d`) tertimpa; laporan push `c28202df` tertimpa
sebelum dibaca. Ketiganya **DILARANG dihitung**; deret **tidak** putus.
**[v21] Cacat keempat TIDAK lahir** — laporan yang ditolak giliran ini bukan laporan
hangus, melainkan laporan **sah milik push lain** yang dibaca terlalu dini.

## Jumlah uji

**1377 TERUKUR, kini DUA PULUH TUJUH bacaan berjejak (ke-45..ke-71).** Aritmetika
tangan: 71 − 45 = 26; 26 + 1 = **27**.

Bacaan ke-45..ke-68 tercatat di v16–v20. Tiga terbaru adalah ke-69, ke-70, ke-71 pada
tabel di atas — ketiganya `1377`, kode keluar 0.

Turunan: 1341 + **36** butir `test_selisih_lilin.py` = **1377** ✅
Cacah per berkas uji dirujuk ke v19, tidak berubah.
**`tests/test_gerbang_1m.py` = 16 butir** (blob `a930af172fa51ca643384c7be30283958a225e46`);
**apakah 16 itu termasuk dalam 1377 BELUM diukur (utang ukur 27); DILARANG menjumlahkan
1377 + 16.** `tests/test_lubang_tengah.py` — 56 butir menurut R-228, **BELUM DIBACA**.

## Aturan 52 — ordinal berdiri di ke-49

Ke-45 EKOR v20 · ke-46 UKUR v20 · **ke-47 ADR-A023** (blob `d2a5302f…`) · **ke-48 STATE
v63** (blob `515abb29…`) · **ke-49 berkas ini**. Ditaati **tanpa satu pun kelalaian**
sejak butir 19; **lima berkas akar PADAT berturut berhasil utuh** — STATE v61, STATE
v62, EKOR v20, UKUR v20, STATE v63 — dan berkas ini yang keenam bila pembacaan ulangnya
bersih.

**Batasnya tetap:** aturan 52 menjaga **kesetiaan salinan**, bukan mutu penalaran.

## Aturan 79, 85, 91 — cacah berjalan, TIDAK BERGERAK

**Aturan 79 — tetap TUJUH berturut** (R-314..R-320). Tidak bertambah sebab tidak ada
ramalan baru. **DILARANG** menyebutnya lemah; **DILARANG** membacanya sebagai bukti mutu
isi.
**Aturan 85 — tetap EMPAT adjudikasi yang menguji tepi.** Tidak bertambah.
**Aturan 91 — tetap DUA pemakaian** (R-319, R-320), ditambah **satu penyebutan** giliran
ini untuk menolak penjumlahan dua alasan berkorelasi. **DILARANG disebut "teruji".**
**Aturan 77, 78, 89 (dipertegas), 93 — baru diresmikan; DILARANG disebut "teruji".**

## Catatan kejujuran [v21]

1. **Dua giliran tanpa satu pun angka riset baru.** ADR-A023, STATE v63, dan berkas ini
   seluruhnya tata tertib. Yang bertambah: tiga aturan resmi, satu utang ukur, satu
   nyala aturan 90. Yang **tidak** bertambah: pengetahuan tentang BNXUSDT, tentang 786
   simbol lain, tentang sebab hari bulat hilang. **Tenggat riset 2 Agustus 2026 tidak
   mengenal perbedaan antara tertib dan produktif.**
2. **Aturan 90 menyala, dan itu satu-satunya peristiwa terukur berkas ini.** Ia dicatat
   sebagai kejujuran, bukan kemenangan — tidak ada ramalan yang meramalkannya.
3. **Usulan aturan habis untuk pertama kalinya sejak v41.** Tidak ada satu pun nomor
   aturan menggantung. Itu keadaan bersih, dan **DILARANG dibaca sebagai kematangan
   tata tertib** — habisnya usulan berarti tidak ada yang sedang dipertimbangkan, bukan
   berarti aturan yang ada sudah cukup.
4. **`PROMPT_KELANJUTAN.md` tetap belum berkepala "ARSIP — BUKAN SUMBER"** dan
   `PROMPT.md` **v55 belum didorong**. Umur utang kini **TIGA BELAS versi**, naik satu
   sejak v20. Disebut setiap kali, tidak dikerjakan setiap kali — **cacat proses, dan
   menyebutnya berulang tanpa mengerjakannya adalah cacat kedua** yang kini berumur
   sama panjangnya.
5. **`karantina_semesta.py` masih belum dibaca.** Selama itu, tabel dua belas karantina
   dan `sebaran_pelanggaran` 12/12 dikutip **tanpa aturan 86 (b) terpenuhi**, dan
   `cacah_daftar_terpotong` **0** tetap **kesaksian laporan tentang dirinya sendiri**.
   Ia berdiri di peringkat atas utang bacaan selama tiga versi.
6. **Pemeriksaan silang yang menutup [v21]:** 71 − 42 + 1 = **30** ✅ ·
   71 − 45 + 1 = **27** ✅ · ke-62..ke-71 = **10** pemakaian aturan 90 ✅ ·
   229 + 65 + 22 + 16 + 7 = **339** ✅
   **Yang TETAP TIDAK menutup:** `selisih_absen_pasangan_jurnal_113` = **−1**; utang ukur
   **30**; utang ukur **27**; utang ukur **31**.
7. **KLAIM LAMA DICABUT.** Kalimat *"tidak ada kegagalan panggilan alat GitHub sepanjang
   sesi ini"* yang berdiri sejak v16 **BERHENTI BENAR** pada giliran ini — satu
   `push_files` ditolak sebab bentuk panggilannya salah. **DILARANG mengutip kalimat itu
   dari versi mana pun sesudah v20.** Kegagalan itu **bersih**: tidak ada commit, tidak
   ada artefak separuh. Satu-satunya kegagalan pembacaan tetap `web.loadPage` atas URL
   mentah — repo tertutup.

## Utang verifikasi

1–5, 11 menunggu tahap juri. 6–23, 25–29, 31, 36 LUNAS. **Nomor utang BUKAN nomor
ramalan — KC-32.** Butir 24, 30, 32–44 dirujuk ke v20; yang bergerak:

24. **AKTIF. LUNAS BARU [v21]:** `STATE.md` **v43** (blob
    **`a91a49346a6ebcf1a288b936904a8fe1facc3d7a`**, commit
    **`eea324fd98f76d27c812690eaea54467408508ec`**) — rumah teks calon aturan 77 dan 78,
    ditemukan lewat `search_commits`; `decisions/ADR-A023.md`; STATE v62 dan v63 dibaca
    ulang utuh; EKOR v20 dibaca ulang utuh; `ci_terakhir.json` ke-69..ke-71.
    **TETAP BELUM:** ADR **A002, A005, A006, A007, A008**; **`karantina_semesta.py`**
    (14.948 B, `46e7c46b…`); `reports/manifes_pilot.json`; `diagnosa_kc6.py` dan
    laporannya; `rentang_kc6.py` dan laporannya; `rilis.py`; `arsip.py`; `ukur_baris.py`;
    `tests/test_lubang_tengah.py`; `test_pulihkan.py`; `test_rilis_karantina.py`;
    `test_karantina_a006.py`; `karantina_semesta.yml`; **`journal/2026-07-30-125.md`**;
    bagian `baris_mati` (54%); 5% `semesta_rentang.json`; 58 baris
    `baris_penyebut_butir_1`; **kedelapan `manifes_pecahan_*.json` — DI LUAR JANGKAUAN
    ALAT**; `reports/bulan_absen.json` (249.992 B); lima belas modul serapan.
45. **AKTIF** — `selisih_absen_pasangan_jurnal_113` = **−1**; jurnal 113 belum dibaca.
46. **AKTIF, kini BERSYARAT TERSURAT** — mengapa sembilan dari sepuluh simbol berabsen
    kehilangan tepat bulan settled terakhirnya. ADR-A023 kep. 4 menjadikannya **syarat
    pertama** pematangan KC-58; syarat kedua adalah **kejadian pada gejala BERBEDA**.
47. **AKTIF** — adakah berkas akar lain yang pernah terdorong terpotong tanpa
    tertangkap? **DILARANG menyatakan butir 19 kejadian tunggal.**
48. **AKTIF** — asal-usul klausa `deret_tidak_kosong`. Kini bersinggungan dengan **utang
    ukur 31**, tetapi **tidak sama**: 48 menanyakan **asal-usul**, 31 menanyakan
    **mengapa nol kejadian**. **DILARANG menganggap satu membayar yang lain.**
49. **AKTIF, TETAP DITUNDA** — perluasan kelas BAHAN TAK BERSAKSI. ADR-A023 §10
    menegaskan penundaannya; bahannya baru satu berkas.

**Utang ukur (penomoran terpisah, milik UKUR):** **hidup 6, 7, 17, 21, 22, 26, 27, 30,
dan 31 [BARU]**. **LUNAS: 19, 25, 28, 29.** **Berikutnya 32.**

> **Utang ukur 31 (lahir ADR-A023 kep. 5, menggantikan KC-59).** Untuk masing-masing
> dari empat klausa gerbang 1m yang nol kejadian pada 19.598 — `deret_tidak_kosong`,
> `tanpa_duplikat`, `selaras_menit`, `satuan_milidetik` — tetapkan **dari kode, bukan
> dari laporan**, apakah nol itu berarti (a) mustahil menyala, (b) mungkin tetapi tak
> pernah terjadi, atau (c) belum diketahui. Sertakan penyebut dan definisi uji tiap
> klausa (aturan 74).

## Daftar ADR

A001–A022 dirujuk ke v19 dan v20, tidak berubah. Satu baris bergerak:

- **ADR-A023** (`d2a5302f08442c44176a177baacc2eee0ee5df58`, commit `a8acbeba…`) —
  **DELAPAN keputusan. DITERIMA.** Ia menutup **seluruh** usulan aturan yang menggantung
  (77, 78, 93), memutuskan kedua usulan KC (58 ditunda bersyarat, 59 dibuang), dan
  **menolak** permohonan pencabutan yang EKOR v20 sendiri buka. Kelemahannya diakui
  sendiri di catatan penutupnya: **ia tidak menambah satu angka riset pun**, dan
  nilainya baru terukur pada R-321.
- **ADR-A024 [BELUM ADA]** — belum terikat butir apa pun. **ADR-A003 masih BELUM ADA**
  dan tetap blokir pertama klasifikasi.

## Penomoran berikutnya

Aturan resmi **1–81, 83–93** · nomor **82** dicadangkan · **usulan aturan tersisa: TIDAK
ADA** · **aturan berikutnya yang bebas 94** · KC resmi sampai **KC-55** (KC-16 kosong
selamanya; **KC-56, KC-57, KC-59 DIBUANG**), usulan hidup **KC-58 saja** · **KC
berikutnya KC-60** · hipotesis berikutnya **H-A024** · jurnal berikutnya **158** ·
`STATE.md` berikutnya **v64** · EKOR berikutnya **v22** · **UKUR berikutnya v21 (utang
hidup; keserasian nama dua dari tiga sampai ia naik)** · PROMPT berikutnya **v55 (belum
didorong, umur tiga belas versi)** · ADR berikutnya **A024** · ramalan berikutnya
**R-321** · **papan skor 339 — SAH** · aturan 38 **ke-72** · aturan 52 **ke-50** ·
kesalahan dokumen berikutnya butir **22** · utang ukur berikutnya **32** · utang
verifikasi berikutnya **50** · berhenti eksplisit berikutnya **ke-58**.

## Syarat praregistrasi R-321 — kini DELAPAN BELAS syarat kumulatif

Enam belas syarat v20 tetap berlaku (dirujuk ke blob v20), dengan **dua kenaikan derajat
dan dua tambahan**:

- **[15 NAIK DERAJAT] Aturan 89 kini DIPERTEGAS, bukan sekadar resmi.** Ruang vonis tiap
  butir wajib **EMPAT SISI tanpa kecuali**: menang · kalah · **bahan ada tetapi medan
  tak ada** · **bahan tidak terjangkau**. Butir bersisi kurang dari empat adalah
  **praregistrasi CACAT**, dan kecacatannya milik peramal.
- **[16 NAIK DERAJAT] Aturan 93 kini RESMI, bukan sukarela.** Ukuran tiap bahan wajib
  diperoleh lewat **daftar direktori** — alat sahnya ada dan murah: `get_file_contents`
  atas sebuah **direktori** dengan `fields` memuat `name`, `size`, `sha`. **DILARANG**
  memakai panggilan pengambil isi untuk memeriksa ukuran; itu persis yang memecahkan
  aturan 21 pada jurnal 157. Ukuran wajib **dicatat di praregistrasi** bersama nama dan
  blob.
- **[17 BARU] Aturan 77 berlaku atas pencacahan saksi.** Bila dua bahan dipakai untuk
  saling mencocokkan (aturan 69), praregistrasi wajib menyebut **kedua blob**; bila
  ternyata sama, klaim dua sumber **gugur menjadi satu** dan cacah bukti bebas turun.
- **[18 BARU] Aturan 78 berlaku atas pemilihan bahan.** Bahan berukuran mendekati batas
  tolak **DILARANG** didaftarkan tanpa rencana pecahan; berkas ≥ 2,25 MB dianggap **tak
  terjangkau** sampai terbukti sebaliknya, dan berkas ratusan KB wajib diperlakukan
  sebagai **mungkin terpotong** sejak praregistrasi.

**Syarat bahan R-321 — daftar terlarang bertambah.** Bahan **DILARANG** berupa berkas
yang sudah dibuka pada sesi ini: `semesta_rentang.json` · `semesta_bulan_1m.json` ·
`gerbang_1m.py` · `silang_funding.json` · `lubang_awal.json` ·
`bulan_absen_ringkas.json` · `lubang_awal.py` · `bulan_absen.py` · `serap.py` ·
`klines.py` · `pecahan.py` · `test_gerbang_1m.py` · `ADR-A004.md` ·
**`karantina_semesta.json`** (dibuka melanggar aturan 21 — **tidak dapat ditawar**) ·
**[v21] `STATE.md` v43** · kedelapan `manifes_pecahan_*.json` selama alat belum sanggup
membacanya.

**Poros yang disarankan bagi R-321:** **utang ukur 30** — mengapa BNXUSDT 2022-06
(1.440 menit = tepat 1 hari) dan 2022-08 (4.320 menit = tepat 3 hari) kehilangan hari
bulat penuh sementara 2022-04 (1.650 menit) tidak. Bahannya **wajib** berkas yang belum
dibuka, ukurannya **wajib** dibaca dari daftar direktori lebih dulu, dan tiap butirnya
**wajib** bersisi empat.

— akhir `STATE_LAMPIRAN_EKOR.md` v21 —
