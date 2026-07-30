# PROMPT KELANJUTAN v46 — riset LUX-AI

Operator: Diva Juan Nur Taqarrub, GitHub EnVyxS, zona waktu Asia/Jakarta, bahasa
kerja Indonesia. Tenggat: **2 Agustus 2026**.

**BERKAS DI REPO ADALAH KEBENARAN; prompt ini hanya peta dan boleh saja
tertinggal.** v44 pernah menyuruh membaca laporan yang tidak pernah ada; bila
prompt dan berkas bertengkar, berkas menang, dan pertengkarannya dicatat.

---

## LANGKAH 0 — WAJIB, BERURUTAN, SEBELUM PEKERJAAN APA PUN

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})` dengan
   `owner`/`repo` HANYA di dalam `toolArguments`, tidak di tingkat atas.
3. Baca dari main repo `EnVyxS/lux-ai-research`, berurutan:
   - `PROMPT_KELANJUTAN.md` (berkas ini, v46)
   - `journal/2026-07-30-124.md` — **paling penting**: adjudikasi R-303,
     temuan baru, praregistrasi R-304, papan skor 303
   - `decisions/ADR-A010.md` — keputusan yang baru diambil
   - `journal/2026-07-30-123.md` — bunyi praregistrasi R-303 dan ADR-A009
   - `STATE.md` (v43, blob `a91a4934…`) — masih v43; **v44 belum ada**
   - `STATE_LAMPIRAN_EKOR.md` (v3, blob `89fec927…`) — papan skornya masih 300
   - `decisions/ADR-A008.md` bila menyentuh §6 atau Keputusan 7
4. Baru setelah itu pekerjaan teknis. Jangan mengukur apa pun sebelum
   praregistrasi ramalan berikutnya ditulis di jurnal (aturan 79).

---

## BATASAN LINGKUNGAN

- Sandbox agen tidak punya jaringan; semua pengukuran lewat GitHub Actions; hanya
  artefak YANG DI-COMMIT boleh dipercaya.
- Tidak ada alat membaca status Actions dan tidak ada alat memicu
  `workflow_dispatch`. Satu-satunya cara menyalakan run adalah push ke berkas di
  dalam `paths` workflow.
- Tidak ada API patch: `push_files` MENULIS ULANG seluruh isi berkas. Jangan
  menulis ulang berkas panjang sebelum membacanya utuh (KC-42d); sesudah
  mendorong berkas panjang WAJIB baca ulang dari main (aturan 52).
- Batas tulis aman ±25–45 KB. STATE penuh (~55 KB) pernah TERPOTONG SUNYI dua
  kali (KC-42): commit BUKAN bukti keutuhan.
- Batas baca: hasil >±30.000 token DIPOTONG. `reports/funding_semesta.json` hanya
  terbaca 27% → TIDAK terukur utuh. Manifes pecahan mustahil dibaca. Karena itu
  laporan modul baru WAJIB dirancang ringkas (lihat `tersisip_semesta`: agregat +
  baris hanya bagi simbol yang menyala).
- `search_code` mengembalikan 0 hasil — pakai `get_file_contents`; path
  berakhiran garis miring melisting direktori.
- Runner punya numpy, pandas, pyarrow, pyyaml, pytest; TIDAK ada scipy/requests.
  `data.binance.vision` dapat diakses, `fapi.binance.com` 451.
- Dilarang menulis apa pun di luar repo `lux-ai-research`; `lux-research` baca
  saja.
- `ci.yml` memakai `paths-ignore` (`journal/**`, `decisions/**`, `hipotesis/**`,
  `reports/**`). Push ke `lux_ai/**`, `tests/**`, `STATE*`, `PROMPT*`
  MENYALAKAN CI; push jurnal/decisions/reports TIDAK.

---

## POSISI SERAH TERIMA (30 Juli 2026, ±11:40 WIB)

| commit | isi |
| --- | --- |
| **HEAD saat prompt ini ditulis** | `c4bccf219ddcc3495265331b4cbce9a3ea806eb5` (jurnal 124 + ADR-A010) |
| `6a7710e3a4dc2581b5808bca5e6417c78d4edd69` | laporan `tersisip_semesta` run 30514239872 |
| `25106dd51ed8295b58d3d63c93dc0b78cad00428` | trio `tersisip_semesta` V1 (modul + 47 uji + workflow) |
| `ae435d9abde01ab85e1181c5d8a1ac013ef3e1db` | laporan CI 30509339065 (cacahnya TIDAK terbaca, hilang) |
| `34f4c0265a4ced53eac67f0a21cef58f799f386d` | PROMPT v45 |
| `17a594b69e243a83884862122f01b5e1ade4278a` | jurnal 123 + ADR-A009 |
| `703daa900e2aa285dc5b058592457e81fe02643f` | trio `bentangan_kohort` V2 (63 uji) |
| `47e1261108d4ee4bfc5b7c98fb864f37d89d13e9` | jurnal 122 |

Push PROMPT ini menyalakan CI sekali lagi; hasilnya BELUM dibaca.

**Papan skor R-1 … R-303:** TEPAT **214** / MELESET **54** / SEPARUH **20** /
TIDAK TERADJUDIKASI **8** / MENUNGGU **7** = **303**.
MENUNGGU: R-7, R-19, R-20, R-28, R-36, R-37, R-199. N_percobaan = 0.
**ADJUDIKASI RISET TETAP TERKUNCI.**

Aturan sampai **76** (calon 77, 78, 79 + calon dari KC-43 + calon baru:
penyebut kehidupan tidak seragam berakhir pada bulan ekor).
KC sampai **KC-44**. Hipotesis terbuka: **H-A016**, **H-A017**.

Penomoran berikutnya: jurnal **125** · STATE **v44** (utang) · PROMPT **v47** ·
ADR **A011** · ramalan **R-305** (R-304 SUDAH dipraregistrasi di jurnal 124 §8,
boleh langsung dibangun dan diukur).

---

## PEKERJAAN PERTAMA, BERURUTAN

1. **Bangun penguji R-304** sesuai praregistrasi jurnal 124 §8 — bunyinya TIDAK
   boleh diubah, pitanya TIDAK boleh dilebarkan. Sasaran: memasangkan bentangan
   kematian delapan simbol bangkit dengan lubang funding mereka.
   - Ikuti anatomi yang sudah dua kali berhasil: modul di `lux_ai/serapan/`,
     tests bernomor `test_01`…, workflow meniru
     `.github/workflows/tersisip_semesta.yml` (blob dari main, `git add` PER
     BERKAS + `if: always()`).
   - Listing direktori dan cacah TANGAN lebih dulu (aturan 66). Sesudah trio
     `tersisip_semesta`: `lux_ai/serapan/` = 40, `.github/workflows/` = 35 —
     dicacah tangan pada `ae435d9a`; sesudah trio R-304 seharusnya 41 dan 36,
     WAJIB dicacah ulang.
   - Keluaran WAJIB ringkas (8 baris simbol saja) supaya terbaca utuh.
   - Kendali positif dua lapis dan penggugur wajib ada.
2. **Baca `reports/ci_terakhir.json`** sesudah push mana pun. Cacah uji DIUKUR,
   tidak diramalkan.
3. **STATE v44** — utang terbesar, sudah TIGA giliran tertunda. Baca STATE v43
   UTUH, tulis dalam dua berkas < 45 KB, lalu BACA ULANG keduanya. Wajib memuat:
   KC-43, KC-44, R-301 TIDAK TERADJUDIKASI, R-302 SEPARUH, R-303 TEPAT,
   ADR-A009, ADR-A010, papan skor 303, CI 879, delapan simbol bangkit.
4. `STATE_LAMPIRAN_EKOR.md` v4 (papan skor masih 300).
5. `STATE_LAMPIRAN_UKUR.md` (blob `0e9ec378…`, baca UTUH lebih dulu).

---

## APA YANG BARU DIUKUR (R-303, jangan diukur ulang tanpa alasan)

Run **30514239872**, commit `25106dd5`, kode 0. Laporan
`reports/tersisip_semesta.json` blob
**`911acd1c730a677dd8c7100655313f5bf3d1f6e3`** — TERBACA UTUH.
Sidik kode `tersisip_semesta` =
`9618fd19e4ab2e7b5279177db600f6176afd914ab1e94576e54197f70ebc537c`.

Penyebut: **19.586 simbol-bulan / 787 simbol**; MATI 1.401, SEPI 98, HIDUP
18.087. Kelima selisih terhadap STATE = **0**. Penggugur semua diam; kendali
pasar sah; kendali detektor sah.

**R-303 = TEPAT (3/3):** butir 1 = 8 simbol (pita 1..60), butir 2 = 88
simbol-bulan (pita 1..300), butir 3 MUDAH cocok. Kejujuran: pitanya LEBAR, angka
jatuh di bagian bawah pita, jadi R-303 lebih mudah daripada bunyinya — sudah
ditulis begitu di jurnal 124 §4.

### Delapan simbol bangkit — SELURUH yang ada di semesta

| simbol | bulan | HIDUP | MATI | tersisip | mati pertama |
| --- | --- | --- | --- | --- | --- |
| CVCUSDT | 67 | 38 | 29 | 29 | 2022-12 |
| CVXUSDT | 45 | 31 | 13 | 13 | 2024-06 |
| SLPUSDT | 32 | 18 | 13 | 13 | 2024-06 |
| CTKUSDT | 67 | 55 | 11 | 11 | 2024-05 |
| LITUSDT | 64 | 54 | 10 | 10 | 2025-02 |
| TLMUSDT | 60 | 51 | 8 | 8 | 2022-07 |
| ICPUSDT | 62 | 59 | 2 | 2 | 2022-07 |
| MAVIAUSDT | 28 | 25 | 2 | 2 | 2025-01 |

Hitung tangan: 29+13+13+11+10+8+2+2 = **88** ✅ Distribusi 779 nol + 8 = 787 ✅

### Yang berubah karena pengukuran ini

1. **Pembatal pertama §6 ADR-A008 MENYALA.** Ia tidak boleh lagi disebut belum
   pernah menyala, dan tidak boleh dicabut sebagai pembatal mustahil.
2. **ADR-A009 DIBUKA KEMBALI** (ADR-A010 §3.2). Arah sebab "mati dulu, funding
   kemudian" belum dicabut, tetapi turun derajat menjadi MENUNGGU pengukuran
   berpasangan. R-304 pengujinya. Kata "serentak" tetap DITOLAK.
3. **"Kebangkitan adalah kejadian tunggal satu simbol" DICABUT.** Delapan, bukan
   satu. LITUSDT hanya yang pertama TERLIHAT.
4. **Bentuk kebangkitan = BLOK MATI TUNGGAL.** Pada 8/8, `cacah_tersisip` =
   `cacah_mati` = `rentetan_mati_terpanjang`. Panjang blok: 2, 2, 8, 10, 11, 13,
   13, 29 bulan. Tidak ada kematian kedua pada satu pun simbol.
5. **`tersisip_rapat` = 0 dari 88** pada 0 dari 8 simbol — tidak ada satu pun
   lubang MATI satu bulan yang diapit HIDUP bertetangga langsung. Nol ini
   bermakna HANYA karena detektor rapatnya terbukti menyala 1 dari 1 pada kendali
   positif. Kata "kedip" / "berselang-seling" WAJIB ditulis TIDAK TERUKUR.
6. **BNXUSDT TIDAK bangkit** — 19 bulan lubang funding BNX bukan kebangkitan.
7. **BTSUSDT `bulan_terakhir` = 2024-05**, bukan 2026-06. Penyebut kehidupan
   TIDAK seragam berakhir pada bulan ekor; keseragaman 2026-06 hanya terukur pada
   38 anggota kohort. Calon KC.
8. **H-A015 harus dibaca hati-hati:** ICP MATI 2 bulan (bukan 16), TLM MATI 8
   bulan (bukan 20). Angka 16/19/20 bersatuan BULAN TANPA FUNDING, bukan bulan
   MATI. Tidak bertabrakan, tetapi selisihnya besar dan searah ADR-A009.
9. Simbol MATI terbanyak yang TIDAK bangkit: BTCSTUSDT 63 (0 HIDUP dari 64),
   SCUSDT 48, FTTUSDT 43, RAYUSDT 43, STRAXUSDT 27, DGBUSDT 26.

---

## PRAREGISTRASI R-304 (jurnal 124 §8 — KUTIP, jangan susun ulang)

Penyebut: 8 simbol bangkit dari 787; funding dari
`reports/funding_semesta.json` lewat `silang_funding.lubang_funding`.

- **Butir 1 (BERISIKO):** cacah SIMBOL, dari 8, yang `bulan_mati_pertama`-nya
  jatuh SEBELUM bulan berlubang funding pertamanya → pita **5..8**. Nol kalah.
- **Butir 2 (BERISIKO):** cacah SIMBOL, dari 8, yang punya ≥1 bulan HIDUP yang
  berlubang funding → pita **3..8**.
- **Butir 3 (MUDAH, sebut MUDAH):** penyebut 19.586 / 787 simbol;
  `cacah_simbol_bangkit` 8; `cacah_simbol_bulan_tersisip` 88; kedua kendali sah;
  kode 0.

Akibat sudah dinyatakan: butir 1 menang → ADR-A009 boleh ditutup kembali dengan
bunyi diperluas ke delapan simbol; butir 1 kalah → arah sebab A009 DICABUT dan
pertanyaannya dinyatakan BELUM TERJAWAB (bukan terjawab ke arah lain); butir 2
menang → "33 HIDUP tanpa funding" adalah ciri kebangkitan dan taksonomi wajib
memuat kelasnya; butir 2 kalah → H-A017 dirumuskan ulang.

---

## UTANG ATURAN 52

LUNAS giliran ini:
- `lux_ai/serapan/bentangan_kohort.py` V2 — blob `f4eae57ab59e6e1b8fe584027f2529f19dd736a6` (16.925 B)
- `.github/workflows/bentangan_kohort.yml` V2 — blob `13f21d1df77bbd336c1373e0b4ef2d707810f3aa`
- `lux_ai/serapan/tersisip_semesta.py` V1 — blob `8a648838963e2e08a08089abc08fcc538e1adfc1`
- `tests/test_tersisip_semesta.py` — blob `61196fd1e3c01acecf5a5788ec66fa70b7c84148`, **47 butir** dicacah dari `test_01`…`test_47`

MASIH TERBUKA: `tests/test_bentangan_kohort.py` V2 (63 butir, didorong
`703daa90`) belum dibaca ulang byte demi byte.

---

## RIWAYAT CI (diukur, tidak diramalkan)

630 → 638 → 662 → 694 → 722×8 → 769 → 814 → 832 → **879**.
Terakhir: run **30514239862**, commit `25106dd5`, kode 0,
"879 tests collected in 0.50s", blob `a57e8f1da882310f8424034591f0727e57246514`.
Hitung tangan 832 + 47 = 879 ✅

---

## PEKERJAAN BERIKUTNYA SESUDAH R-304

1. Uji **H-A017** (byte parquet: MATI < ~500 ribu, HIDUP > ~1,4 juta) atas
   semesta, pita yang bisa kalah + kendali positif. Bahan sudah ada:
   `silang_funding.baca_laporan_kehidupan` mengembalikan `byte_parquet` berkunci
   tuple, dan `baca_medan_baris(akar, total, "cacah_lilin")`.
2. Mengapa `tersisip_rapat` nol — ciri pasar atau ciri gerbang bulanan? Belum
   diukur.
3. Uji **H-A016** (celah kelipatan 15 menit).
4. Putuskan calon aturan **77** (dua berkas berblob identik bukan dua
   pengukuran), **78** (batas alat sebagai bagian desain — sudah tiga kali
   dipakai sadar), **79** (praregistrasi di jurnal — kini EMPAT kali berhasil,
   layak diterima), calon dari KC-43 (tanda tangan fungsi yang dipakai wajib
   dikutip di pemakainya — sudah dua kali menyelamatkan modul), dan calon baru
   dari BTSUSDT.
5. TANGGAL hari hilang BNX 2022-04/06/08; irisan 880 lawan 877; selisih 40−38
   `diagnosa_kc15`; `ukur_baris` V6 (KC-26).
6. ADR: A003 wajib memuat delapan simbol bangkit (ADR-A010 §3.4);
   terima/tolak A007; terapkan A006; `dugaan_pengganti` (A005).
7. Adjudikasi R-7/19/20/28/36/37 dan R-199; gali bunyi R-28 dari STATE v23
   (KC-32); salin R-236..R-247 dari jurnal 92–94; masukkan R-229 TEPAT dan
   R-230 MELESET.
8. Belum dibaca: `decisions/ADR-A002.md`, A004, A006, A007, A008 (utuh),
   `PETA_MODUL.md`, `PETA_MODUL_BERKAS.md`, `STATE_LAMPIRAN.md`,
   `STATE_LAMPIRAN_ANGKA.md`, `karantina_semesta.yml`, `tests/test_pulihkan.py`,
   `test_rilis_karantina.py`, `test_karantina_a006.py`.

---

## KEBIASAAN YANG MENGIKAT

Ramalan SEBELUM run lalu adjudikasi jujur; praregistrasi di jurnal lebih dulu
(79); hitung ulang tiap angka dengan tangan (21); sediakan medan penggugur (24);
kelas cacat pada sampel (37); dilarang menyimpulkan di luar rentang (20) — dua
nol pada 38 dan pada 2 baru saja terbukti bukan nol semesta; kendali positif
wajib (50), dan bila yang diukur bisa bernilai nol maka DETEKTORNYA juga wajib
dikendalikan; laporan tak terbaca utuh = tidak ada (52); cacah butir uji dari
daftar bernomor (54/56/57); ketiadaan pengukuran bukan ketiadaan gejala (59);
listing direktori sebelum menulis modul baru (66); nama turunan bersama asalnya
(69); baca modul penghasil sebelum meramalkan laporannya (71); jangan meramal
isi berkas dari NAMA-nya (73); setiap nol bersama penyebutnya (74).

Ramalan yang hanya menyalin angka terverifikasi adalah MUDAH — katakan begitu.
Pita lebar juga membuat butir "berisiko" lebih mudah daripada bunyinya — katakan
begitu juga. "lanjut"/"lanjutkan" berarti teruskan tanpa konfirmasi. Jangan
berhenti dengan alasan konteks Notion.

---

## CATATAN KEJUJURAN

R-300 SEPARUH, R-301 TIDAK TERADJUDIKASI (modulnya mati di waktu jalan, KC-43),
R-302 SEPARUH, R-303 TEPAT. Dari empat ramalan terakhir, hanya satu yang penuh,
dan yang penuh itu dibantu pita lebar. Tiga butir MUDAH dari sembilan butir
terakhir. Praregistrasi R-303 disusun ketika saya menduga jawabannya NOL; ia
ternyata 8. Dugaan saya salah dan pitanya yang menyelamatkan — bukan
ketajaman ramalan.

---

## API TERVERIFIKASI (JANGAN DITEBAK — pelajaran KC-43)

- `silang_funding` V2 (blob `42c3aa9d`): `Kunci = Tuple[str, str]`;
  `baca_laporan_kehidupan(akar, total) -> (Dict[Kunci,str], Dict[Kunci,int], meta)`
  (meta: `total_pecahan, cacah_laporan_dibaca, laporan_hilang,
  sidik_kode_laporan, sidik_seragam, cacah_kunci_ganda`);
  `baca_medan_baris(akar, total, medan) -> (Dict[Kunci,Any], meta)`;
  `lubang_funding(funding) -> (Set[Kunci], {cacah_lubang_funding,
  cacah_lubang_ganda})`; `SUMBER_FUNDING = "reports/funding_semesta.json"`;
  `MEDAN_LILIN = "cacah_lilin"`; `PENYEBUT_TERCATAT 19586`, `MATI_TERCATAT 1401`,
  `KOHORT_TERCATAT 456`, `HIDUP_TANPA_FUNDING_TERCATAT 33`,
  `LUBANG_TAK_DIKENAL_TERCATAT 3`, `BENTUK_TERBITAN_FUNDING {awal 48, ekor 826,
  tengah 6}`, `KENDALI_CACAH 3`, `TOTAL_PECAHAN 8`; `bentuk_lubang_lokal`,
  `bulan_per_simbol`, `kendali_silang`, `kendali_sah`, `sidik_kode`, `kode_keluar`,
  `jalankan`.
- `kehidupan`: `STATUS_MATI`/`STATUS_SEPI`/`STATUS_HIDUP`/`STATUS_TAK_TERUKUR`
  (nilai "MATI"/"SEPI"/"HIDUP").
- `kehidupan_arsip`: `TOTAL_PECAHAN = 8`, `nama_keluaran(i)`. Medan baris nyata:
  `ada_di_arsip, bagian_volume_nol, bulan, byte_parquet, cacah_baris_cacat,
  cacah_lilin, cacah_lilin_terbaca, cacah_volume_nol, galat, gerbang_lolos,
  jalur, simbol, status, transaksi_total`.
- `kohort_ekor` V4 (blob `c9b63bbe`): `muat_kohort(akar) -> {simbol, bulan_mulai,
  cacah_simbol_kohort, galat}`; `mundur_bulan(bulan, langkah=1)` (langkah negatif
  BELUM diukur — jangan dipakai); `TEBING "2025-07"`,
  `BULAN_DIHARAPKAN "2026-06"`, `KENDALI_HIDUP ("BTCUSDT","ETHUSDT")`,
  `BATAS_SIMBOL 10`, `PAGU_MUNDUR 60`, `SUMBER`, `sidik_kode`.
- `bentangan_kohort` V2 (blob `f4eae57a`): `VERSI 2`,
  `KELUARAN "reports/bentangan_kohort.json"`; `sidik_kode`, `pisah_kunci`
  (menerima kunci TUPLE kanon dan string sampingan), `kelompokkan(status) ->
  (peta, gagal)`, `bulan_berstatus`, `mati_tersisip` (int), `bangkit` (bool),
  `rentetan_terpanjang`, `ringkas_simbol`, `uji_r301`, `kendali_positif(status,
  bulan=None)`, `kendali_sah`, `kode_keluar`, `jalankan(akar, total=None)`, `main`.
- `tersisip_semesta` V1 (blob `8a648838`): `VERSI 1`,
  `KELUARAN "reports/tersisip_semesta.json"`, `PENYEBUT_TERCATAT 19586`,
  `SIMBOL_TERCATAT 787`, `MATI_TERCATAT 1401`, `SEPI_TERCATAT 98`,
  `HIDUP_TERCATAT 18087`, `R303_PITA_SIMBOL (1,60)`,
  `R303_PITA_SIMBOL_BULAN (1,300)`, `BATAS_BARIS_LAPORAN 200`,
  `BATAS_BULAN_DICATAT 12`, `BERKAS_DICAP` 5 nama; `sidik_kode`,
  `bulan_tersisip -> List[str]`, `tetangga_maju`, `bulan_tersisip_rapat`,
  `ringkas_simbol(simbol, peta_bulan)`, `ember`, `himpun`, `kendali_deteksi`,
  `dalam_pita`, `uji_r303`, `kode_keluar`, `jalankan(akar, total=None)`, `main`.
- `anatomi_tengah` V1: `bentangan`, `status_bulan`, `mati_tersisip`,
  `ringkas_simbol`, `rentetan_terpanjang`, `bulan_berstatus`, `uji_r300`,
  `kode_keluar`, `jalankan`.
- `lubang_tengah` V2: `TENGAH_TERCATAT 6`,
  `SIMBOL_TENGAH_TERCATAT ["BTCSTUSDT","LITUSDT"]`, `SIMBOL_H_A011 "LITUSDT"`.

---

## ANGKA TERVERIFIKASI

787 penyebut (arsip 937, 150 hanya-arsip) · 21.789 bulan arsip · 15 nama SETTLED
(36 bulan) · 19.598 simbol-bulan (lolos 19.586, gagal 12 karantina) · MATI 1.401 /
SEPI 98 / HIDUP 18.087 · 839.842.134 baris · funding 880 lubang semesta (877 dalam
penyebut: awal 45/48, ekor 826, tengah 6; 3 tak dikenal) · 33 HIDUP tanpa funding ·
taksonomi 9 kelas · ekor 2026-06 = 808 hidup · kohort puncak 2025-07 = 38 simbol /
456 simbol-bulan (37×12 + 19 − 7 = 456) · **8 simbol bangkit / 88 simbol-bulan
tersisip / 0 tersisip rapat** · BTCSTUSDT 64 bulan 0 HIDUP · LITUSDT 64 bulan 54
HIDUP · CI 879.

Sidik laporan kehidupan seragam:
`24b6bb265525e81c2e571b46e401f36903383f1e3738c487850861adc3e8c595`.
