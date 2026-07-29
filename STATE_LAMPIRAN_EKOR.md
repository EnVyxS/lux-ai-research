# STATE lampiran EKOR — bagian 2 dari STATE v42

**Mengapa berkas ini ada, dan mengapa ia MENGIKAT.** Dua push `STATE.md` berturut
terpotong: v41 berhenti di "Utang verifikasi" butir 24, v42 berhenti di tengah
tabel papan skor pada baris **R-287**. Sebabnya bukan data melainkan **batas
panjang satu push** — `STATE.md` sudah melampaui apa yang dapat ditulis utuh dalam
satu kali kirim, dan tidak ada API tambal. Maka STATE dipecah, sebagaimana repo ini
sudah punya presedennya (`STATE_LAMPIRAN.md`, `STATE_LAMPIRAN_ANGKA.md`).

**Pembagian yang berlaku sejak v42:**

1. **`STATE.md`** — bagian 1: kepala, aturan bernomor, kelas cacat, semesta,
   karantina, bulan absen, hipotesis, dan tabel-tabel pengukuran. Baris terakhirnya
   saat ini TERPOTONG di tengah tabel papan skor; potongan itu **DIGANTI oleh
   berkas ini**, dan `STATE.md` v43 wajib berhenti sebelum papan skor sambil
   menunjuk ke sini.
2. **`STATE_LAMPIRAN_EKOR.md`** (berkas ini) — bagian 2: papan skor, catatan
   kejujuran, jumlah uji, utang verifikasi, daftar ADR, temuan sampingan,
   penomoran berikutnya.
3. **`STATE_LAMPIRAN_ADR.md`** (blob `a02ef271`) — arsip ekor v41; isinya sudah
   diserap ke sini dan boleh diabaikan sebagai sumber.

Dasar bacaan: `STATE.md` v41 blob **`b02061545da86b371e8f07766673bb5d0893da56`**
(UTUH), `ci.yml` blob **`c79497b2`** (UTUH), `reports/ci_terakhir.json` blob
**`1b10bd19`**, `reports/ci_terakhir.txt` blob **`0f8626bc`** (UTUH).

## KC-42 — kelas cacat baru [v42]

**KC-42 — menulis ulang berkas yang sudah melampaui batas satu push, lalu
menganggap push itu berhasil karena alat mengembalikan commit.** `push_files`
mengembalikan ref baru dengan gembira meski muatan yang dikirim berhenti di tengah
kalimat; tidak ada galat, tidak ada peringatan. Dua kali berturut `STATE.md`
didorong cacat (v41, v42), dan keduanya hanya tertangkap oleh aturan 52.
**Penangkal, mengikat:** (a) berkas yang tidak dapat ditulis utuh dalam satu kirim
WAJIB dipecah lebih dulu, bukan diulang; (b) commit yang dikembalikan alat BUKAN
bukti keutuhan — hanya pembacaan ulang yang membuktikannya; (c) sesudah push
berkas panjang, DILARANG menyusun berkas lain di atasnya sebelum pembacaan ulang.
Kerabat KC-19 (percaya ingatan) dan aturan 38 (percaya keberadaan berkas).

**Calon aturan 78 (DIUSULKAN):** batas panjang alat adalah bagian dari desain
repo, bukan kecelakaan; struktur berkas wajib disesuaikan dengan batas alat yang
terukur (baca: ±2,4 MB untuk membaca, dan sekitar satu berkas STATE untuk
menulis).

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
| R-284 | `lubang_tengah.py` memuat tetapan tiga bulan BNXUSDT | **MELESET** (aturan 73) |
| R-285 | 6 lubang tengah, LIT 5 / BTCST 1, `h_a011_menang` false | **SEPARUH** |
| R-286 | H-A015: cocok 3..4; ≥10 dari 12 lebih awal; lubang >10 lawan <10 | **TEPAT** (4, 11 dari 12) |
| R-287 | CI **662**, kode 0, commit `3d113d49` | **TEPAT** (MUDAH, run 30469781181) |
| R-289 | `ci.yml` menyala pada commit STATE **dan** commit PROMPT, 662, kode 0 | **TEPAT** pada KEDUA cabang (MUDAH) |
| R-288 | bulan ABSEN: (1) 9 tunggal + BNX **3** + lima nol; (2) ≥7 dari 9 sama dengan bulan SETTLED; (3) jumlah semesta **12** | **SEPARUH** — butir 2 **TEPAT 9 dari 9**; butir 1 MELESET (BNX **2**); butir 3 MELESET (**11**) |
| R-290 | CI **694**, kode 0, commit `4fc818f0` | **TEPAT** (MUDAH, run 30477143164) |
| R-291 | daftar `parquet_karantina` kedelapan manifes memuat **tepat 12** simbol-bulan, himpunannya sama persis dengan tabel karantina | **TEPAT — BERISIKO** (12/12, `diramalkan_hilang` [], `terukur_tak_diramalkan` [], run 30479681799) |
| R-292 | CI **694**, kode 0, commit `c07cb65f` | **TEPAT** (MUDAH, run 30478069419) |
| R-293 | CI **694**, kode 0, commit `91ce4660` | **TEPAT** (MUDAH, run 30479093362) |
| R-294 | CI **722**, kode 0, commit `edea61f7` | **TEPAT** (MUDAH, run 30479681620) |
| R-295 | commit BERIKUTNYA yang menyalakan `ci.yml` memberi cacah **722** dan `kode_keluar` **0**, sebab tidak ada berkas di `tests/**` yang berubah | **DIPRAREGISTRASI — MUDAH** |

**Total R-1..R-294** (dihitung tangan, aturan 21). Dasar v40: TEPAT 204 · MELESET
54 · SEPARUH 18 · TIDAK TERADJUDIKASI 7 · MENUNGGU 7 = **290**. Sesudah v40:
**empat TEPAT** (R-291, R-292, R-293, R-294), tanpa MELESET maupun SEPARUH baru.

- TEPAT 204 + 4 = **208**
- MELESET **54** · SEPARUH **18** · TIDAK TERADJUDIKASI **7**
- MENUNGGU **7** (R-7, R-19, R-20, **R-28**, R-36, R-37, R-199)

208+54 = 262; +18 = 280; +7 = 287; +7 = **294** ✅ Nomor terpakai R-1..R-294,
seluruhnya teradjudikasi atau menunggu. **R-295 dipraregistrasi tetapi belum
teradjudikasi, jadi ia BELUM masuk total.** N_percobaan = 0; adjudikasi riset
TETAP TERKUNCI. Ramalan berikutnya sesudah R-295 adalah **R-296**.

**Erratum yang dibawa:** v40 menulis total **290** dengan kalimat "tiga TEPAT"
padahal yang baru hanya dua (R-289, R-290); aritmetikanya sendiri benar
(202 + 2 = 204). PROMPT v43 menulis **291**. Angka yang berlaku adalah **294**.

**Utang papan skor:** rincian baris R-236..R-247 masih hanya di jurnal 92–94; dan
ramalan yang dipraregistrasi di dalam **docstring modul** (mis. R-229 TEPAT, R-230
MELESET di `lubang_tengah.py` V2) belum masuk papan — pemeriksaan R-224..R-235
wajib dijalankan lebih dulu agar tidak mengulang KC-32.

## Catatan kejujuran [v42]

Sejak v40 ada empat adjudikasi, semuanya TEPAT, tetapi tiga di antaranya (R-292,
R-293, R-294) hanyalah cacah butir uji dari daftar bernomor — **MUDAH** dan
deterministik. Satu-satunya yang benar-benar berisiko adalah **R-291**, dan ia
menang bersih. Pola lama tetap berlaku: **cabang yang saya sebut BERISIKO menang,
cabang yang saya sebut MUDAH-lah yang dulu kalah** (R-281, R-282, R-284, R-288
butir 1 dan 3).

**Tiga kesalahan proses pada giliran ini, semuanya milik penulis:**

1. **Satu run CI menyala tanpa praregistrasi** (run **30481231522**, commit
   `ea2a07e7`) karena push `STATE_LAMPIRAN_ADR.md` ternyata memicu `ci.yml`.
   Pengukurannya sah, kemenangannya TIDAK ADA — tidak ada ramalan sebelumnya.
2. **Batasan CI dirumuskan dari ingatan dan terbalik bentuknya** (KC-41):
   `ci.yml` memakai `paths-ignore`, bukan `paths`.
3. **`STATE.md` didorong terpotong dua kali** (KC-42), dan hanya aturan 52 yang
   menangkapnya.

Yang layak dicatat sebagai kemajuan bukan papan skornya, melainkan bahwa setiap
kekalahan melahirkan aturan atau kelas cacat yang menutup lubangnya: 70, 71, 72,
73, 76, KC-40, dan sekarang **KC-41** serta **KC-42**.

## Jumlah uji

**722 TERVERIFIKASI DUA ARAH [v42].** Arah pertama, cacah kumpul:
`reports/ci_terakhir.json` blob **`1b10bd19d03dab9ebdeeff9d50dd17fdd0890d27`**,
run **30481231522**, commit **`ea2a07e7a43942b9d9413a1d7f537d4149af90b3`**,
2026-07-29T18:44:01Z, `kode_keluar` **0**, "**722 tests collected in 0.51s**", ref
runner **`b7c030a8`**. Arah kedua, hasil eksekusi: `reports/ci_terakhir.txt` blob
**`0f8626bc64b5904fe83b012433219939828359d1`** (pembacaan PERTAMA berkas ini) —
sepuluh baris 72 titik + satu baris 2 titik, lalu "**722 passed in 1.33s**";
10×72 + 2 = **722** ✅ (aturan 21, 69). Kedua angka berasal dari perintah pytest
yang BERBEDA di dalam satu run — `--collect-only` lawan eksekusi penuh — jadi ini
dua pengukuran, bukan satu (bandingkan calon aturan 77).

Sebelum itu **722** juga terukur pada run **30479681620** commit `edea61f7` (blob
`7db59237`, ref `e82919f5`, "722 tests collected in 0.40s") — itulah dasar R-294.
Sebelumnya **694** tiga kali (blob `2d853021` run 30477143164 commit `4fc818f0`;
blob `4bac352c` run 30478069419 commit `c07cb65f`; blob `8027606f` run 30479093362
commit `91ce4660`), **662** tiga kali (blob `8504322b`, `15d14123`, `18cae8e5`),
**638** (blob `ca47d961`), **630** (blob `2d0dfa27`). Riwayat: 231 → … → 610 → 623
→ 630 → 630 → 638 → 662 → 662 → 662 → 694 → 694 → 694 → **722 → 722**.

`tests/test_terhenti.py`: V1 **5** → V2 **18** → V3 **25** → **V4 33**.
`tests/test_silang_settled.py` **24** (638 + 24 = 662).
`tests/test_bulan_absen.py` **32** (662 + 32 = 694).
**`tests/test_karantina_semesta.py` 28** butir tanpa satu pun `parametrize`
(694 + 28 = **722**), daftar bernomor ada di docstringnya. Lainnya:
`test_semesta_kuota` 58 · `test_lubang_tengah` 56 · `test_kebangkitan` 54 ·
`test_silang_funding` 49 · `test_penyebut_tahun` 44 · `test_semesta_silang` 32 ·
`test_bulan_settled` 26. Aturan 57 kini **tujuh belas dari tujuh belas**.

**Kendali negatif yang tercatat:** run 30462286751 atas commit `7b819787` berjalan
ketika `tests/test_terhenti.py` masih memuat kurung kurawal liar; run 30462427226
atas commit perbaikan `e6b74855` memberi 630 dan kode 0.

**Perilaku `ci.yml` yang kini terbaca dari kode** (blob `c79497b2`): `paths-ignore`
atas `journal/**`, `decisions/**`, `hipotesis/**`, `reports/**` — jadi setiap push
di luar keempatnya menyalakan CI; `workflow_dispatch` dideklarasikan;
`concurrency` per ref dengan `cancel-in-progress: false` sehingga run mengantre;
cacah dicetak SEBELUM pytest; laporan ditulis dan di-commit dengan pesan
ber-`[skip ci]` SEBELUM `exit ${kode}`, sehingga suite yang gagal pun tetap
meninggalkan pengukuran.

## Utang verifikasi

1-5 dan 11 menunggu tahap juri/klasifikasi. 6-23, 25-28 LUNAS. **Nomor utang ini
BUKAN nomor ramalan — lihat KC-32.**

24. **AKTIF.** LUNAS seperti tercatat v40, ditambah **LUNAS [v41]:** daftar
    `parquet_karantina` DIBACA (R-291) beserta byte 13.247.705 dan
    `pecahan_tanpa_karantina` [2, 5] · pembagian 5 hari KC-15 ke tiga bulan BNXUSDT
    (1.650 / 1.440 / 4.320) · ukuran lilin kedua belas bulan karantina
    (`nisbah_lilin` 0,903–0,990) · `gerbang_1m.py` UTUH (KC-40) · `pulihkan.py`,
    `rilis.py`, `serap.py`, `pecahan.py` UTUH · `.github/workflows/bulan_absen.yml`
    UTUH · `bulan_absen_status.json` dan `bulan_absen.log` · listing `tests/`
    (41 → 42) · `karantina_semesta.py` dan ujinya sesudah push.
    **LUNAS BARU [v42]:** **`.github/workflows/ci.yml` DIBACA UTUH** (utang tertua
    yang tak pernah disadari — KC-41) · **`reports/ci_terakhir.txt` DIBACA UTUH**
    ("722 passed") · **`STATE.md` v41 dibaca UTUH** sehingga pemotongannya
    tertangkap · listing akar repo dan `journal/`.
    **BELUM:** anatomi **BTCSTUSDT 2022-01** · irisan 880 lawan 877 · **TANGGAL**
    hari-hari yang hilang pada ketiga bulan BNXUSDT (cacahnya diketahui, tanggal
    UTC-nya belum) · selisih 40 − 38 sampel `diagnosa_kc15` · `ukur_baris` **V6**
    (KC-26 + enam belas berkas belum terukur) · peninjauan `funding.py` /
    `silang_funding.py` (705 baris, SERI) · daftar **147** nama hanya-arsip ·
    identitas **18** simbol tanpa bulan HIDUP · kehidupan kedua belas simbol-bulan
    karantina (status MATI/SEPI/HIDUP tidak dapat ada bagi mereka, sebab di luar
    penyebut 19.586) · `funding_ada` masih null di seluruh manifes ·
    `dugaan_pengganti` (ADR-A005) · pemulihan harian ADR-A007 · karantina artefak
    7 hari · 28 anggota kohort di luar sampel abjad · **bunyi R-28 dari STATE v23
    (KC-32)** · tiga nama ekor 2026-04 · keberadaan `POLUSDT` di dalam 787 ·
    asal-usul hantu "16 non-ASCII" ·
    **`.github/workflows/karantina_semesta.yml` belum dibaca ulang sesudah push** ·
    `lux_ai/semesta/taksonomi.py` (blob `b418c7ba`) — premis "taksonomi beroperasi
    atas 937 nama arsip" tetap **ASUMSI** · `decisions/ADR-A002.md`, `ADR-A004.md`,
    `ADR-A006.md`, `ADR-A007.md`, `ADR-A008.md`, `PETA_MODUL.md`,
    `PETA_MODUL_BERKAS.md`, `STATE_LAMPIRAN.md`, `STATE_LAMPIRAN_ANGKA.md` belum
    dibaca pada sesi ini · **H-A016 belum diuji** atas simbol-bulan yang LOLOS
    gerbang · laporan yang belum pernah dibaca utuh: `karantina_semesta.json`
    penuh, `bulan_absen.json` (249.992 B), `semesta_rentang.json` (110.662 B,
    `sumber_bersidik` false), `ringkas_semesta.json`, `survei_semesta.json`,
    `survei_progres.json`, `rentang_kc6.json`, `semesta_kuota.json`,
    `semesta_silang.json`, `penyebut_tahun.json`, `kohort_ekor.json`,
    `funding_semesta.json`, `funding_selisih_penuh.json` (500 dari 880),
    `hidup_tanpa_funding.json`, `tests/test_pulihkan.py`,
    `tests/test_rilis_karantina.py`, `tests/test_karantina_a006.py` ·
    **MUSTAHIL dibaca agen:** `reports/manifes_pecahan_*.json` (pecahan 2 =
    2.446.093 B, blob `c0be6ecf…`, DITOLAK alat baca).

Cacat penulisan yang dicatat dan TIDAK disunting (aturan 29): docstring R-225
("tujuh fungsi" lalu sembilan nama) dan docstring `penyebut_tahun.py`
(`TLMUSDT_SETTLED`). Mengadjudikasi R-7, R-19, R-20, R-28, R-36, R-37, R-199.

## Daftar ADR

- **ADR-A001** aturan dasar. DITERIMA.
- **ADR-A002** serapan. DITERIMA; §3 DIAMANDEMEN oleh A004 lalu A007; §9 DIGANTI
  oleh A006 Keputusan 3. **§10 belum disentuh dan tetap tidak boleh disentuh atas
  bukti kohort semata;** bila kelak disunting, WAJIB menyebut batas
  `perpetual_usdt`. Dua gejala bebas yang menyokong H-A015 TIDAK cukup — keduanya
  soal penamaan dan penerbitan, bukan perdagangan (KC-18). **Bukti bulan karantina
  berlilin SEBAGIAN (0,903–0,990) juga TIDAK cukup:** ia menunjukkan berkas tidak
  utuh, bukan bahwa perdagangan berhenti.
- **ADR-A003** taksonomi rezim. BELUM ADA (nomor dicadangkan). Wajib memisahkan
  "kontrak berganti nama" dari "pasar hidup kembali", memakai taksonomi INSTRUMEN
  kanonik (KC-29), memuat aturan 68, kebangkitan LITUSDT beserta aturan 74, bulan
  ABSEN sebagai kelas gejala tersendiri beserta aturan 76, dan **KC-40** — sebab
  kelas gejala itu dikenali dari medan `pelanggaran` yang bermakna terbalik.
- **ADR-A004** kebijakan KC-6. DITERIMA. Penggugurnya tetap tidak menyala:
  `cacah_gerbang_lolos_padahal_tepi_terpotong` = 0 atas 37 bulan tengah. Gerbang
  §2 kini terbaca dari kode (`gerbang_1m.py` blob `c8cc54c8`): enam klausa, dan
  `menit_hilang_dalam_rentang` dihitung atas rentang yang ADA di berkas, sengaja
  bukan atas bulan kalender.
- **ADR-A005** jenis instrumen tahap pertama. DITERIMA.
- **ADR-A006** karantina + persistensi. DITERIMA, DITERAPKAN, TERVERIFIKASI DARI
  LUAR. Verifikasi terkuat: kedua belas berkas karantina ADA,
  `cacah_tanpa_parquet_karantina` **0**, `cacah_dibuang` **0**, `cacah_ditambal`
  **0**, `jumlah_karantina_tak_terkemas` **0**, byte total **13.247.705** = angka
  KC-17.
- **ADR-A007** serapan hibrida. **DIUSULKAN**, belum diterima; wajib
  memperhitungkan temuan `jumlah_baris` dan kendala R-146. Bahan yang
  menguatkannya: 7.200 menit KC-15 UTUH di arsip HARIAN; kesebelas bulan absen ADA
  di arsip (`tak_diterbitkan_arsip` 0); dan bulan karantina rata-rata hanya
  kehilangan 1–10% menitnya, jadi pemulihan berpeluang besar mengembalikannya ke
  penyebut — yang akan **MENGUBAH 19.586**. Perubahan penyebut DILARANG tanpa ADR
  (aturan 30, 44).
- **ADR-A008** akibat KC-18. **Keputusan 1–6 DITERIMA [v28]**; Keputusan 5
  bersemesta 18.087. **Keputusan 7 BERCABANG DUA, kedua cabangnya bernama:**
  **LITUSDT** (lubang tengah berentetan **5**, MATI seluruhnya, bulan **2025-12
  ABSEN** dengan 43.590 dari 44.640 menit, lalu **BANGKIT** terukur) lawan
  **BTCSTUSDT** (lubang tengah **TUNGGAL** 2022-01, `cacah_lilin` 44.640 PENUH,
  **tanpa bulan absen**, **tidak ada di daftar karantina**, tetap MATI, 53 dari 53).
  Keputusannya WAJIB memuat kedua cabang, WAJIB per simbol-bulan, DILARANG
  menyebut funding dan perdagangan berhenti "serentak", WAJIB menyebut batas
  `perpetual_usdt`, WAJIB memakai aturan 66 revisi, 67, 68, 74, 76, dan **DILARANG
  diambil sebelum BTCSTUSDT 2022-01 dianatomi seperti BNXUSDT 2022-04**. R-276
  mengikat: tak ada peralihan yang terbukti. R-278 mengikat: 13 / 2 / 0.
- **ADR berikutnya A009.**

## Temuan sampingan yang belum diukur

- **Anatomi BTCSTUSDT 2022-01** — pekerjaan teknis paling berharga yang tersisa,
  dan satu-satunya prasyarat tersurat Keputusan 7 ADR-A008.
- **Uji H-A016** (celah kelipatan 15 menit) atas simbol-bulan yang LOLOS gerbang;
  penyebutnya harus dipilih hati-hati sebab gerbang menolak bulan bercelah.
- **TANGGAL** hari-hari yang hilang pada BNXUSDT 2022-04 / 2022-06 / 2022-08.
- Irisan **880 lawan 877**; selisih 40 − 38 sampel `diagnosa_kc15`.
- Tiga nama ekor 2026-04; mengapa `SXPUSDT` berhenti 2026-05; apakah `POLUSDT` ada
  di 787; asal-usul hantu "16 non-ASCII".
- Daftar 147 nama hanya-arsip; 18 simbol tanpa bulan HIDUP.
- Apakah 50 kontrak delivery bertanggal pernah masuk perhitungan mana pun.
- Mengapa penamaan SETTLED datang berombak pada 2023-02 dan 2025-07, dan mengapa
  2025-07 juga bulan tebing funding dan kohort puncak.
- Sebab kebangkitan/peralihan kedelapan simbol (di luar jangkauan arsip).
- Saham, ETF, dan komoditas token masih terhitung `perpetual_usdt`.
- `.decode("utf-8","replace")` di `klines` membungkam byte rusak.
- Apakah BUSD/USDC layak digabung dengan USDT (80 nama, 1.705 bulan).
- Sebab KC-14 (H-A004) tak dapat diuji; sebab KC-15 tidak diketahui — meski
  pembagiannya kini terukur, SEBABNYA tetap tidak diketahui.
- Selisih byte funding AGIXUSDT 531 lawan 529; `waktu_utc` runner berjalan lebih
  dulu daripada jam sesi; satuan stempel mikro lawan mili.
- `tests/test_pulihkan.py`, `tests/test_rilis_karantina.py`, dan
  `tests/test_karantina_a006.py` belum pernah dibaca.

## Penomoran berikutnya

Aturan sampai **76** (calon **77** dua berkas berblob sama, calon **78** batas alat
sebagai bagian desain — keduanya belum berlaku). Kelas cacat sampai **KC-42**.
Jurnal berikutnya **117**. STATE berikutnya **v43** (wajib berhenti sebelum papan
skor dan menunjuk berkas ini; wajib menutup baris R-287 yang terpotong). PROMPT
berikutnya **v44**. ADR berikutnya **A009**. Ramalan: **R-295 dipraregistrasi**,
berikutnya **R-296**. Papan skor **294**.
