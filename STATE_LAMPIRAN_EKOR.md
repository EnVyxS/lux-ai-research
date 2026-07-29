# STATE lampiran EKOR — bagian 2 dari STATE (v3, menuju STATE v44)

**Mengapa berkas ini ada, dan mengapa ia MENGIKAT.** Dua push `STATE.md` berturut
terpotong: v41 berhenti di "Utang verifikasi" butir 24, v42 berhenti di tengah
tabel papan skor pada baris **R-287**. Sebabnya bukan data melainkan **batas
panjang satu push** — `STATE.md` sudah melampaui apa yang dapat ditulis utuh dalam
satu kali kirim, dan tidak ada API tambal. Maka STATE dipecah, sebagaimana repo ini
sudah punya presedennya (`STATE_LAMPIRAN.md`, `STATE_LAMPIRAN_ANGKA.md`).

**Pembagian yang berlaku:**

1. **`STATE.md` v43** (blob **`a91a49346a6ebcf1a288b936904a8fe1facc3d7a`**) —
   bagian 1: kepala, aturan bernomor 1–76, kelas cacat KC-1..KC-42. Ia **berhenti
   sesudah kelas cacat** dan menunjuk ke sini.
2. **`STATE_LAMPIRAN_EKOR.md`** (berkas ini) — bagian 2: papan skor, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan,
   penomoran berikutnya.
3. **`STATE_LAMPIRAN_UKUR.md`** (blob **`0e9ec3783d95be522dd4e56221fc7197f89c13c0`**)
   — bagian 3: seluruh tabel pengukuran, modul/workflow/uji, API terverifikasi,
   hipotesis. **Belum memuat H-A017 dan bentangan `anatomi_tengah`; ia wajib
   diperbarui pada giliran berikutnya sesudah dibaca UTUH lebih dulu (KC-42d).**
4. **`STATE_LAMPIRAN_ADR.md`** (blob `a02ef271`) — arsip ekor v41; **bukan sumber
   lagi**.

**Tentang push berkas ini:** ia menyalakan `ci.yml` (akar repo, di luar
`paths-ignore` — KC-41) dan **sengaja TIDAK dipraregistrasi**. Sejak jurnal 118 dan
calon aturan 79, cacah butir uji yang deterministik tidak lagi dijadikan ramalan;
ia tetap diukur dan dicatat, tetapi tidak lagi menambah papan skor. Delapan
kemenangan MUDAH berturut sudah cukup membuktikan bahwa `pytest --collect-only`
berperilaku sama setiap kali.

## KC-42 — kelas cacat [v42, disempurnakan v43]

**KC-42 — menulis ulang berkas yang sudah melampaui batas satu push, lalu
menganggap push itu berhasil karena alat mengembalikan commit.** `push_files`
mengembalikan ref baru dengan gembira meski muatan berhenti di tengah kalimat;
tidak ada galat. Dua kali berturut `STATE.md` didorong cacat (v41, v42), keduanya
hanya tertangkap oleh aturan 52. **Penangkal, mengikat:** (a) berkas yang tidak
dapat ditulis utuh dalam satu kirim WAJIB dipecah lebih dulu; (b) commit yang
dikembalikan alat BUKAN bukti keutuhan; (c) sesudah push berkas panjang, DILARANG
menyusun berkas lain di atasnya sebelum pembacaan ulang; **(d) sebelum menulis
ulang berkas panjang, badan lamanya WAJIB dibaca UTUH** — penangkal (d) dijalankan
lagi sebelum berkas ini ditulis (blob lama `62d4b24f…` dibaca UTUH). Kerabat KC-19
dan aturan 38. **Obatnya TERBUKTI:** sejak STATE dipecah, sembilan push panjang
berturut lolos utuh (v43, kedua lampiran, PROMPT v44, jurnal 117–120, trio
`anatomi_tengah`).

**Calon aturan 78 (DIUSULKAN):** batas panjang alat adalah bagian dari desain repo
— ±2,4 MB untuk membaca (manifes pecahan 2 DITOLAK), ±25–45 KB terbukti aman untuk
menulis.

**Calon aturan 79 (DIUJI SEKALI, BERHASIL):** praregistrasi ramalan ditulis lebih
dulu di `journal/**` yang ada di `paths-ignore`, sehingga urutan "ramalan dulu,
pengukuran kemudian" dapat ditegakkan tanpa menyalakan run. Ujian pertamanya
adalah **R-300**: jurnal 119 (commit `3b43ee8b`, blob `f7ec9f62`) didorong
**sebelum** modul `anatomi_tengah.py` ada, sehingga pita 8..30 dan ramalan tetangga
HIDUP tidak mungkin disunting sesudah angkanya terlihat. Dan angkanya memang
mengalahkan ramalannya.

## Papan skor prediksi — lengkap

| # | Prediksi | Status |
|---|---|---|
| R-199 | `definisi_dapat_dibedakan` false pada TEPAT 2 pecahan | **MENUNGGU** |
| R-275 | SETTLED hidup: bulan tutup DAN cacah_bulan ≤3 | **TEPAT** |
| R-276 | keenam nama peralihan ada di 28 terhenti | **MELESET** (0 dari 6) |
| R-277 | CI 630, kode 0, commit `e6b74855` | **TEPAT** |
| R-278 | 15 SETTLED: 13 dasar hidup, 2 terhenti, ≥11 mendahului | **TEPAT** (13/2/0, 14) |
| R-279 | CI 630, commit `8a0c4bff` | **TEPAT** (MUDAH) |
| R-280 | CI 638 sesudah `test_terhenti` V4 | **TEPAT** (MUDAH) |
| R-281 | bulan SETTLED 36 **dan** 11 nama bersatu-bulan | **MELESET** (12 — aritmetika sendiri) |
| R-282 | `diagnosa_kc15.json` menyebut tiga bulan BNXUSDT | **MELESET** (hanya 2022-04) |
| R-283 | modul `diagnosa_kc15` mengukur tepi | **TEPAT** (lewat disjungsi — mendekati MUDAH) |
| R-284 | `lubang_tengah.py` memuat tetapan tiga bulan BNXUSDT | **MELESET** (aturan 73; yang ada `SIMBOL_TENGAH_TERCATAT` = dua NAMA SIMBOL) |
| R-285 | 6 lubang tengah, LIT 5 / BTCST 1, `h_a011_menang` false | **SEPARUH** (dua butir pertama tepat; `h_a011_menang` ternyata **true**) |
| R-286 | H-A015: cocok 3..4; ≥10 dari 12 lebih awal; lubang >10 lawan <10 | **TEPAT** (4, 11 dari 12) |
| R-287 | CI **662**, kode 0, commit `3d113d49` | **TEPAT** (MUDAH, run 30469781181) |
| R-289 | `ci.yml` menyala pada commit STATE **dan** commit PROMPT, 662, kode 0 | **TEPAT** pada KEDUA cabang (MUDAH) |
| R-288 | bulan ABSEN: (1) 9 tunggal + BNX **3** + lima nol; (2) ≥7 dari 9 sama dengan bulan SETTLED; (3) jumlah semesta **12** | **SEPARUH** — butir 2 **TEPAT 9 dari 9**; butir 1 MELESET (BNX **2**); butir 3 MELESET (**11**) |
| R-290 | CI **694**, kode 0, commit `4fc818f0` | **TEPAT** (MUDAH, run 30477143164) |
| R-291 | daftar `parquet_karantina` kedelapan manifes memuat **tepat 12** simbol-bulan, himpunannya sama persis dengan tabel karantina | **TEPAT — BERISIKO** (12/12, `diramalkan_hilang` [], `terukur_tak_diramalkan` [], run 30479681799) |
| R-292 | CI **694**, kode 0, commit `c07cb65f` | **TEPAT** (MUDAH, run 30478069419) |
| R-293 | CI **694**, kode 0, commit `91ce4660` | **TEPAT** (MUDAH, run 30479093362) |
| R-294 | CI **722**, kode 0, commit `edea61f7` | **TEPAT** (MUDAH, run 30479681620) |
| R-295 | commit BERIKUTNYA penyala `ci.yml` memberi **722** dan kode **0** | **TEPAT** (MUDAH) — run **30482205512**, ref `117d8c67`, blob `a605c94a` |
| R-296 | push `STATE_LAMPIRAN_UKUR.md` memberi **722** dan kode **0** | **TEPAT** (MUDAH) — run **30482864644**, ref `ecdaacdb`, blob `a467ab62` |
| R-297 | push `STATE.md` v43 memberi **722** dan kode **0** | **TEPAT** (MUDAH) — run **30483341732**, ref `4613a559`, blob `4b5a9c4b` |
| R-298 | push `PROMPT_KELANJUTAN.md` v44 memberi **722** dan kode **0** | **TEPAT** (MUDAH) — run **30483636460**, ref `c620c51a`, blob `9b0f3a09` |
| R-299 | push lampiran EKOR v2 memberi **722** dan kode **0** | **TEPAT** (MUDAH) — run **30483924857**, commit `a2c44177`, ref `ab654c78`, blob `c1d12d53`, 19:20:28Z, "722 tests collected in 0.52s" |
| R-300 | (1) `cacah_bulan` **64** bagi BTCSTUSDT dan LITUSDT; (2) tetangga BTCST 2021-12 dan 2022-02 **keduanya HIDUP**; (3) `cacah_hidup` BTCST di pita **8..30** DAN MATI > HIDUP | **SEPARUH** — butir 1 (satu-satunya yang disebut MUDAH) **TEPAT** 64/64; butir 2 **MELESET** (kedua tetangga **MATI**); butir 3 **MELESET** (`cacah_hidup` **0**, di luar pita; klausa MATI>HIDUP benar tetapi ramalan menuntut keduanya). Run **30485048909**, ref `6366f20b`, blob `403ebdf9` |

**Total R-1..R-300** (dihitung tangan, aturan 21). Dasar v43: TEPAT 212 · MELESET
54 · SEPARUH 18 · TIDAK TERADJUDIKASI 7 · MENUNGGU 7 = **298**. Sesudahnya: R-299
**TEPAT**, R-300 **SEPARUH**.

- TEPAT 212 + 1 = **213**
- MELESET **54** · SEPARUH 18 + 1 = **19** · TIDAK TERADJUDIKASI **7**
- MENUNGGU **7** (R-7, R-19, R-20, **R-28**, R-36, R-37, R-199)

213+54 = 267; +19 = 286; +7 = 293; +7 = **300** ✅ Nomor terpakai R-1..R-300,
seluruhnya teradjudikasi atau menunggu; tidak ada praregistrasi yang menggantung.
N_percobaan = 0; adjudikasi riset TETAP TERKUNCI. Ramalan berikutnya **R-301**.

**Erratum yang dibawa:** v40 menulis total **290** dengan kalimat "tiga TEPAT"
padahal yang baru hanya dua; aritmetikanya sendiri benar (202+2=204). PROMPT v43
menulis **291**, PROMPT v44 menulis **297**, lampiran EKOR v2 menulis **298** —
semuanya benar pada saatnya. Angka yang berlaku sekarang **300**.

**Utang papan skor:** rincian R-236..R-247 masih hanya di jurnal 92–94. Ramalan
yang dipraregistrasi di dalam **docstring modul** juga belum masuk papan — dan dua
di antaranya kini punya bukti laporannya: **R-229 dikukuhkan TEPAT**
(`funding_tanpa_klines` kosong pada 5 dari 5) dan **R-230 MELESET**
(`h_a011_menang` ternyata **true**, 6 dari 6 HIDUP). Keduanya menunggu pemeriksaan
R-224..R-235 agar tidak mengulang KC-32.

## Catatan kejujuran [v3]

**Pola lama TERBALIK pada R-300, dan itu satu-satunya kabar baik tentang mutu
ramalan pada rangkaian giliran ini.** Sepanjang R-292..R-299 ada delapan kemenangan
berturut, **tujuh di antaranya MUDAH** — cacah butir uji dari daftar bernomor yang
deterministik. Pada R-300 saya memasang dua butir berpita yang benar-benar bisa
kalah, dan **keduanya kalah**; yang menang justru butir yang saya sendiri labeli
MUDAH. Itu bukan kemunduran: itu bukti bahwa pitanya bukan hiasan.

**Riset bergerak lagi.** Sejak R-291 tidak ada pengukuran riset baru; R-300
memecah kebekuan itu dan langsung menghasilkan tiga temuan yang mengubah ADR (lihat
Daftar ADR dan Temuan sampingan).

**Kesalahan dan keterbatasan proses yang tetap dicatat:**

1. **KC-41** — batasan CI pernah dirumuskan dari ingatan dan terbalik bentuknya:
   `ci.yml` memakai `paths-ignore`, bukan `paths`.
2. **KC-42** — `STATE.md` didorong terpotong dua kali; hanya aturan 52 menangkapnya.
3. **Empat run CI menyala tanpa praregistrasi** — 30481231522, 30482387663, run
   push STATE v41 yang laporannya tertimpa sebelum terbaca, dan **30485048845**
   (769, commit `583fcb79`). Yang terakhir **sengaja** demikian dan dicatat sebagai
   pengukuran tanpa kemenangan.
4. **Rantai tulis-CI** (jurnal 118 §4): setiap perbaikan papan skor menyalakan CI
   yang melahirkan peluang ramalan MUDAH baru. Ditutup dengan berhenti meramalkan
   cacah uji.
5. **Selisih listing `lux_ai/serapan/` 38 lawan 39** belum terjelaskan; dicatat
   sebagai selisih terbuka, bukan dikoreksi (aturan 29). Sesudah trio
   `anatomi_tengah` masuk, cacah terukurnya menjadi **39**.

Yang layak dicatat sebagai kemajuan bukan papan skornya, melainkan bahwa setiap
kekalahan melahirkan aturan atau kelas cacat yang menutup lubangnya: 70–74, 76,
KC-40, KC-41, KC-42, dan calon 77, 78, **79**.

## Jumlah uji

**769 TERUKUR [v3].** `reports/ci_terakhir.json` blob
**`d7f2be03fb43f72a4f2d594c3deecacb694b6e97`** pada ref
**`a9bb57e19544f3c1cacf5c07ab97a8817174a7f0`**: run **30485048845**, commit
**`583fcb7974e35161dda28d624cbac735de2e6c11`**, 2026-07-29T19:35:21Z, `kode_keluar`
**0**, "**769 tests collected in 0.52s**". Turunan: 722 + **47** butir
`tests/test_anatomi_tengah.py` = **769** ✅ (aturan 21). Tanpa praregistrasi, dengan
sengaja.

**722 terukur DELAPAN kali berturut** sebelum itu (aturan 38, masing-masing pada ref
runnernya): run 30479681620 (`7db59237`) · 30481231522 (`1b10bd19`) · 30482205512
(`a605c94a`) · 30482387663 (`12083485`) · 30482864644 (`a467ab62`) · 30483341732
(`4b5a9c4b`) · 30483636460 (`9b0f3a09`) · 30483924857 (`c1d12d53`). Sebelumnya
**694** tiga kali (`2d853021`, `4bac352c`, `8027606f`), **662** tiga kali
(`8504322b`, `15d14123`, `18cae8e5`), **638** (`ca47d961`), **630** (`2d0dfa27`).
Riwayat: 231 → … → 610 → 623 → 630 → 630 → 638 → 662 ×3 → 694 ×3 → 722 ×8 →
**769**.

**722 pernah TERVERIFIKASI DUA ARAH [v42]:** arah kumpul lewat
`ci_terakhir.json` blob `1b10bd19` ("722 tests collected"), arah eksekusi lewat
`reports/ci_terakhir.txt` blob **`0f8626bc64b5904fe83b012433219939828359d1`** —
sepuluh baris 72 titik + satu baris 2 titik, lalu "722 passed in 1.33s"; 10×72+2 =
**722** ✅ Dua perintah pytest berbeda dalam satu run, jadi dua pengukuran
(bandingkan calon aturan 77).

Cacah per berkas uji: `test_terhenti` V1 5 → V2 18 → V3 25 → **V4 33** ·
`test_silang_settled` **24** (638+24=662) · `test_bulan_absen` **32** (662+32=694) ·
`test_karantina_semesta` **28** (694+28=722) · **`test_anatomi_tengah` 47**
(722+47=**769**) · `test_semesta_kuota` 58 · `test_lubang_tengah` 56 (V1 42) ·
`test_kebangkitan` 54 · `test_silang_funding` 49 · `test_penyebut_tahun` 44 ·
`test_semesta_silang` 32 · `test_bulan_settled` 26. Aturan 57 kini **dua puluh dari
dua puluh**.

**Kendali negatif yang tercatat:** run 30462286751 atas commit `7b819787` berjalan
ketika `tests/test_terhenti.py` masih memuat kurung kurawal liar; run 30462427226
atas commit perbaikan `e6b74855` memberi 630 dan kode 0.

**Perilaku `ci.yml` dari kode** (blob `c79497b2`): `paths-ignore` atas `journal/**`,
`decisions/**`, `hipotesis/**`, `reports/**`; laporan CI ditulis ke `reports/**`
sehingga **run tidak melahirkan run**; `workflow_dispatch` dideklarasikan;
`concurrency` per ref dengan `cancel-in-progress: false` sehingga run mengantre;
cacah dicetak SEBELUM pytest; laporan di-commit dengan `[skip ci]` SEBELUM
`exit ${kode}`, sehingga suite yang gagal pun meninggalkan pengukuran.

## Utang verifikasi

1-5 dan 11 menunggu tahap juri/klasifikasi. 6-23, 25-28 LUNAS. **Nomor utang ini
BUKAN nomor ramalan — lihat KC-32.**

24. **AKTIF.** LUNAS seperti tercatat v40–v43, ditambah **LUNAS BARU [v3]:**
    **anatomi BTCSTUSDT 2022-01 — LUNAS** lewat `reports/anatomi_tengah.json` (blob
    `403ebdf9`, run 30485048909): bentangan 64 bulan kedua pemilik lubang tengah,
    tetangga lubang, `mati_tersisip`, dan sebaran status · **`lubang_tengah.py` V2
    DIBACA UTUH** (blob `4d3beaf1`) — utang LANGKAH 0 tertua · **`reports/lubang_tengah.json`
    DIBACA UTUH** (blob `39cd1caa`) · **`lux_ai/semesta/taksonomi.py` DIBACA UTUH**
    (blob `b418c7ba`) sehingga premis "taksonomi beroperasi atas 937 nama arsip"
    berhenti menjadi asumsi — dan **bunyinya keliru**: modul menggolongkan setiap
    entri sah `semesta_rentang.json`; 937 adalah HASIL, bukan tetapan (kerabat
    KC-30) · `.github/workflows/lubang_tengah.yml` DIBACA UTUH (blob `557030de`) ·
    modul dan uji `anatomi_tengah` dibaca ulang UTUH sesudah push (blob `04279335`,
    `beca7eea`) · jurnal 118, 119, 120 dibaca ulang UTUH (`4ff5c4bc`, `f7ec9f62`,
    `2472772b`) · listing `lux_ai/serapan/` dan `.github/workflows/` dihitung tangan.
    **BELUM:** **bentangan kehidupan atas seluruh 38 anggota kohort** — kini
    **satu-satunya prasyarat Keputusan 7 yang tersisa** · **`mati_tersisip` atas
    19.586** (penguji langsung pembatal §6 ADR-A008) · **uji H-A017** (byte parquet
    sebagai gejala kehidupan) · **uji H-A016** (celah kelipatan 15 menit) · irisan
    880 lawan 877 · **TANGGAL** hari hilang BNXUSDT 2022-04/06/08 · selisih 40 − 38
    sampel `diagnosa_kc15` · `ukur_baris` **V6** (KC-26 + enam belas berkas belum
    terukur, kini tujuh belas bersama `anatomi_tengah.py`) · peninjauan `funding.py`
    / `silang_funding.py` (705 baris, SERI) · daftar **147** nama hanya-arsip ·
    identitas **18** simbol tanpa bulan HIDUP · kehidupan kedua belas simbol-bulan
    karantina (mustahil berlabel: di luar penyebut) · `funding_ada` masih null di
    seluruh manifes · `dugaan_pengganti` (ADR-A005) · pemulihan harian ADR-A007 ·
    karantina artefak 7 hari · 28 anggota kohort di luar sampel abjad · **bunyi R-28
    dari STATE v23 (KC-32)** · tiga nama ekor 2026-04 · `POLUSDT` di dalam 787 ·
    asal-usul hantu "16 non-ASCII" (terbukti **bukan** dari medan taksonomi, sebab
    `BATAS_CONTOH` 10 membuat daftarnya tak pernah lengkap) · selisih listing 38
    lawan 39 · `.github/workflows/karantina_semesta.yml` belum dibaca ulang sesudah
    push (blob kini `de40fa4e`) · `decisions/ADR-A002.md`, `ADR-A004.md`,
    `ADR-A006.md`, `ADR-A007.md`, `PETA_MODUL.md`, `PETA_MODUL_BERKAS.md`,
    `STATE_LAMPIRAN.md`, `STATE_LAMPIRAN_ANGKA.md` belum dibaca pada sesi ini ·
    laporan yang belum pernah dibaca utuh: `karantina_semesta.json` penuh,
    `bulan_absen.json` (249.992 B), `semesta_rentang.json` (110.662 B,
    `sumber_bersidik` false), `ringkas_semesta.json`, `survei_semesta.json`,
    `survei_progres.json`, `rentang_kc6.json`, `semesta_kuota.json`,
    `semesta_silang.json`, `penyebut_tahun.json`, `kohort_ekor.json`,
    `funding_semesta.json`, `funding_selisih_penuh.json` (500 dari 880),
    `hidup_tanpa_funding.json`, `silang_funding.json` (183.963 B),
    `taksonomi_semesta.json`, `tests/test_pulihkan.py`,
    `tests/test_rilis_karantina.py`, `tests/test_karantina_a006.py` · **MUSTAHIL
    dibaca agen:** `reports/manifes_pecahan_*.json` (pecahan 2 = 2.446.093 B, blob
    `c0be6ecf`, DITOLAK alat baca).

Cacat penulisan yang dicatat dan TIDAK disunting (aturan 29): docstring R-225
("tujuh fungsi" lalu sembilan nama) dan docstring `penyebut_tahun.py`
(`TLMUSDT_SETTLED`). Mengadjudikasi R-7, R-19, R-20, R-28, R-36, R-37, R-199.

## Daftar ADR

- **ADR-A001** aturan dasar. DITERIMA.
- **ADR-A002** serapan. DITERIMA; §3 DIAMANDEMEN oleh A004 lalu A007; §9 DIGANTI
  oleh A006 Keputusan 3. **§10 belum disentuh dan tetap tidak boleh disentuh atas
  bukti kohort semata;** bila kelak disunting, WAJIB menyebut batas
  `perpetual_usdt`. Dua gejala bebas yang menyokong H-A015 TIDAK cukup — keduanya
  soal penamaan dan penerbitan, bukan perdagangan (KC-18). Bukti bulan karantina
  berlilin SEBAGIAN (0,903–0,990) juga TIDAK cukup. §10 menyentuh 880 lubang —
  termasuk 48 lubang AWAL dan 6 lubang TENGAH — jadi ia bukan soal kohort saja.
  **[v3] Sebab kedua lubang TENGAH kini terukur letaknya:** keduanya jatuh di
  wilayah yang sudah MATI, jadi §10 tidak dapat bersandar pada tafsir "funding
  berhenti mendahului perdagangan" pada kedua kasus itu.
- **ADR-A003** taksonomi rezim. BELUM ADA (nomor dicadangkan). Wajib memisahkan
  "kontrak berganti nama" dari "pasar hidup kembali", memakai taksonomi INSTRUMEN
  kanonik (KC-29), memuat aturan 68, kebangkitan LITUSDT beserta aturan 74, bulan
  ABSEN sebagai kelas gejala tersendiri beserta aturan 76, dan **KC-40**.
  **[v3] Wajib memuat bentangan LITUSDT yang kini terukur:** HIDUP 2021-02..2025-01
  (rentetan hidup **48**), MATI 2025-02..2025-11 (**10** bulan), bulan 2025-12
  DIKARANTINA sehingga di luar penyebut, lalu HIDUP kembali 2026-01..2026-06 —
  yakni kebangkitan yang terukur pada tingkat simbol-bulan, bukan disimpulkan.
- **ADR-A004** kebijakan KC-6. DITERIMA. Penggugurnya tetap tidak menyala:
  `cacah_gerbang_lolos_padahal_tepi_terpotong` = 0 atas 37 bulan tengah. Gerbang
  §2 terbaca dari kode (`gerbang_1m.py` blob `c8cc54c8`): enam klausa, dan
  `menit_hilang_dalam_rentang` dihitung atas rentang yang ADA di berkas.
- **ADR-A005** jenis instrumen tahap pertama. DITERIMA.
- **ADR-A006** karantina + persistensi. DITERIMA, DITERAPKAN, TERVERIFIKASI DARI
  LUAR: kedua belas berkas karantina ADA, `cacah_tanpa_parquet_karantina` **0**,
  `cacah_dibuang` **0**, `cacah_ditambal` **0**, byte total **13.247.705**.
- **ADR-A007** serapan hibrida. **DIUSULKAN**, belum diterima. Penguatnya: 7.200
  menit KC-15 UTUH di arsip HARIAN; kesebelas bulan absen ADA di arsip; bulan
  karantina hanya kehilangan 1–10% menitnya sehingga pemulihan berpeluang
  **MENGUBAH 19.586**. Perubahan penyebut DILARANG tanpa ADR (aturan 30, 44).
- **ADR-A008** akibat KC-18. Keputusan 1–6 DITERIMA; Keputusan 5 bersemesta 18.087.
  Definisi mengikat (Keputusan 2): **SEPI** = `bagian_volume_nol` ≥ 0,5; **MATI** =
  `transaksi_total` 0 — dua istilah, tidak boleh dipertukarkan. Keputusan 3
  mengikat semua laporan: penyebut penuh dan penyebut tanpa MATI berdampingan.
  Keputusan 5 melarang perkalian 456 × 43.200 dan mencatat sampel 10 dari 38
  dipilih menurut ABJAD. Keputusan 6: label MATI tidak pernah per simbol.
  **Keputusan 7 tetap DITANGGUHKAN**, dengan dua perubahan besar [v3]:
  1. **Pembatal pertama §6 TIDAK menyala pada kedua lubang tengah.**
     `cacah_mati_tersisip` **0 pada BTCSTUSDT dan 0 pada LITUSDT**,
     `pembatal_a008_menyala` **false**. Lubang 2022-01 BTCST diapit dua bulan
     **MATI**, bukan dua bulan hidup. Ini TIDAK berarti pembatal itu mati di
     semesta: `mati_tersisip` belum diukur atas 19.586 (aturan 20).
  2. **KOREKSI rumusan lama (aturan 29, bukan suntingan diam-diam):** STATE v43
     memasang LITUSDT dan BTCSTUSDT sebagai dua cabang **berlawanan**. Pada sumbu
     letak lubang, keduanya ternyata **KEMBAR** — sama-sama lubang funding di
     wilayah mati. Yang membedakan keduanya adalah **apa yang terjadi sesudahnya**:
     LIT bangkit (6 dari 6 HIDUP 2026-01..2026-06, `h_a011_menang` **true**), BTCST
     tidak pernah hidup sekali pun.
  **Prasyarat yang tersisa tinggal SATU:** bentangan kehidupan atas seluruh **38**
  anggota kohort (§5). Keputusan 7 tetap WAJIB memuat kedua cabang, WAJIB per
  simbol-bulan, DILARANG menyebut funding dan perdagangan berhenti "serentak" — dan
  bentangan LITUSDT kini memberi alasan tambahan yang kuat untuk larangan itu:
  perdagangan berhenti **lima bulan sebelum** funding. Pembatal lain §6 tetap
  berlaku: `transaksi_total` 0 tetapi harga BERGERAK menuntut definisi MATI ditulis
  ulang; `parser_terbukti` false membatalkan seluruh angka §1.
- **ADR berikutnya A009.**

## Temuan sampingan

**BARU [v3], terukur:**

- **BTCSTUSDT tidak pernah HIDUP satu bulan pun.** 64 bulan di penyebut: HIDUP
  **0**, MATI **63** berentetan 2021-04..2026-06, SEPI **1** (2021-03, bulan
  pertama, `cacah_lilin` 39.900 — bulan sebagian). Klines terus diterbitkan penuh
  selama 63 bulan tanpa satu transaksi: **KC-18 dalam bentuk paling ekstrem yang
  pernah terukur di repo ini.** 0+63+1+0 = 64 ✅
- **Kematian LITUSDT mendahului lubang funding lima bulan.** MATI mulai 2025-02;
  lubang funding mulai 2025-07; keduanya pulih bersama 2026-01. Ini pengukuran
  pertama yang menunjukkan **arah waktu**, bukan hanya keberadaan irisan. Satu
  simbol bukan bukti (aturan 20, 10).
- **H-A017 (BARU):** ukuran `byte_parquet` adalah gejala kehidupan yang terbaca
  tanpa membuka kolom volume. LITUSDT: ~1,63 juta (2025-01 HIDUP) → **394.147**
  (2025-02 MATI) → ~390–434 ribu selama sepuluh bulan mati → **1.939.126** (2026-01
  HIDUP). BTCSTUSDT sepanjang riwayat matinya **369.967–451.805** — pita yang sama.
  Pita dugaan: bulan MATI < ~500 ribu byte, bulan HIDUP simbol yang sama > ~1,4
  juta. **Belum diuji atas semesta; dilarang digeneralkan.**
- `byte_parquet_total`: BTCSTUSDT **26.811.584**, LITUSDT **95.777.311**.

**Lama, belum diukur:** irisan 880 lawan 877; selisih 40 − 38 sampel
`diagnosa_kc15`; TANGGAL hari hilang BNXUSDT 2022-04/06/08; tiga nama ekor 2026-04;
mengapa `SXPUSDT` berhenti 2026-05; `POLUSDT` di dalam 787; asal hantu "16
non-ASCII"; daftar 147 nama hanya-arsip; 18 simbol tanpa bulan HIDUP; apakah 50
kontrak delivery bertanggal pernah masuk perhitungan; mengapa penamaan SETTLED
datang berombak pada 2023-02 dan 2025-07, dan mengapa 2025-07 juga bulan tebing
funding dan kohort puncak; sebab kebangkitan/peralihan kedelapan simbol; saham,
ETF, komoditas token masih terhitung `perpetual_usdt`;
`.decode("utf-8","replace")` di `klines` membungkam byte rusak; apakah BUSD/USDC
layak digabung dengan USDT (80 nama, 1.705 bulan); sebab KC-14 (H-A004) tak dapat
diuji; sebab KC-15 tidak diketahui meski pembagiannya terukur; selisih byte funding
AGIXUSDT 531 lawan 529; `waktu_utc` runner mendahului jam sesi; satuan stempel
mikro lawan mili; `AKHIR_SEMESTA` "2026-06" DIASUMSIKAN di `taksonomi.py` dan
diterbitkan sebagai `akhir_semesta_diasumsikan` (sumber selisih 129 lawan 128).

## Penomoran berikutnya

Aturan sampai **76** (calon **77** dua berkas berblob sama, calon **78** batas alat
sebagai bagian desain, calon **79** praregistrasi di jurnal — **79 sudah diuji
sekali dan berhasil**, ketiganya belum berlaku). Kelas cacat sampai **KC-42**.
Hipotesis baru **H-A017**. Jurnal berikutnya **121**. STATE berikutnya **v44**
(bagian 1 wajib tetap berhenti sesudah kelas cacat dan menunjuk kedua lampiran).
PROMPT berikutnya **v45**. ADR berikutnya **A009**. Ramalan berikutnya **R-301**.
Papan skor **300**.
