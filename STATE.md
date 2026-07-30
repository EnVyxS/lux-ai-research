# STATE — versi 46 (bagian 1 dari tiga)

Diperbarui: 2026-07-30 (sesi 59). Aturan hanya BERTAMBAH; jangan menulis ulang dari
ingatan. v46 disusun di atas `STATE.md` v45 (blob
**`e07f2de12adacf5f814639be3988f690d2881fc5`**), `STATE_LAMPIRAN_EKOR.md` v5 (blob
**`fe45f8b483db019873698f605a9aded4f0f229af`**), dan `STATE_LAMPIRAN_UKUR.md` v5
(blob **`eb8268176d573d88ee48193e9b57338a6aaa7153`**) — **ketiganya DIBACA UTUH pada
giliran ini sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43). Pembacaan itu
langsung membayar tiga hal yang tidak boleh diputuskan dari ingatan: penomoran
aturan (§ bawah), koreksi KC-41 pada lampiran UKUR, dan label hipotesis R-307.

## STATE DIPECAH TIGA — BACA INI LEBIH DULU

Pembagian yang MENGIKAT sejak v43, berlanjut di v46:

1. **`STATE.md`** (berkas ini) — **bagian 1**: kepala, aturan bernomor 1–81, kelas
   cacat KC-1..KC-47. Berkas ini berhenti sesudah kelas cacat.
2. **`STATE_LAMPIRAN_EKOR.md`** v6 — **bagian 2**: papan skor lengkap R-199..R-306,
   catatan kejujuran, jumlah uji **1044**, utang verifikasi 24, Daftar ADR
   A001–A013, temuan sampingan, penomoran berikutnya.
3. **`STATE_LAMPIRAN_UKUR.md`** v6 — **bagian 3**: penyebut 787, taksonomi,
   karantina, bulan ABSEN, hipotesis (termasuk **H-A018** baru), lubang funding,
   modul/workflow/uji, API terverifikasi (termasuk `lubang_tebing` V1).
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip ekor v41; bukan sumber lagi.

**Ketiga berkas wajib dibaca bersama.** LANGKAH 0 PROMPT v49 menyebut ketiganya.

Yang lahir sejak v45: adjudikasi **R-306 = TEPAT**; **ADR-A013** (klaim arah waktu
wajib dipilah tebing / bukan-tebing); **aturan 80 dan 81 RESMI**; **KC-47 RESMI**;
CI 984 → **1044**; modul **`lubang_tebing` V1** (sidik `4a5c2e42…`); praregistrasi
**R-307** dikunci di jurnal 127 §7 (aturan 79); cacah direktori 44 / 39 / 48.

## Aturan bernomor

Aturan **1–36** berlaku tanpa perubahan; teks di STATE v19 (blob `e06c486e…`),
ringkas di v37 (blob `f520d5e2`).

**Aturan 10 (irisan/urutan bulan BUKAN sebab) terbukti untuk KETIGA kalinya di
R-306, dalam bentuk yang lebih halus:** perbandingan STRIKT sudah dipakai, penyebut
sudah benar (118), kendali positif sudah ada — dan klaim arah TETAP kosong, karena
39 dari 40 anggota numerator berbagi SATU bulan tebing `2025-07`. Kecocokan urutan
waktu bukan bukti arah sebab, bahkan ketika cacahnya puluhan. Lahirnya aturan 81 dan
KC-47.

Aturan **37, 39–45, 47, 49, 51, 53, 54, 56, 59–62** berlaku tanpa perubahan;
ringkas satu baris: 37 kelas cacat pada sampel · 39 keseragaman sampel bukan ramalan
· 40 uji silang baris · 41 penyebut nol → TIDAK TERADJUDIKASI · 42 kelas cacat butuh
angka terukur · 43 toleransi berskala · 44 ramalan menyebut penyebut · 45 keatomikan
push pemicu · 47 satuan cacah tersurat · 49 re-export mematahkan uji · 51 jendela
mundur adaptif · 53 ramalan kode keluar butuh pembacaan perilaku · 54 cacah
`def test_` satu per satu · 56 commit BERIKUTNYA yang menyentuh X · 59 ketiadaan
gejala butuh penyebut · 60 mekanisme tak dipindah antarkasus · 61 medan tak dipindah
antarjalur · 62 daftar tak diminta dari laporan bercacah.

Yang berikut memuat angka atau daftar kepatuhan, jadi ditulis agak penuh:

38. Cacah uji hanya sah dari `reports/ci_terakhir.json` (run id + commit +
    `kode_keluar`). **[v46] Ditaati lagi:** CI **1044** run **30524631516** (commit
    `84b11164`, 2026-07-30T07:56:28Z, kode 0, "1044 tests collected in 0.61s").
    Total pemakaian tercatat: **tiga puluh**.
46. Kode dilarang menyimpulkan dari penyebut nol. **[v46] Ditaati di `lubang_tebing`
    V1:** kelas `lubang_dulu` = 0 hanya diklaim TERUKUR karena `kendali_deteksi`
    membuktikan kelas itu terlihat pada bentangan buatan.
48. Berkas modul mendekati 800 baris dipecah sebelum fungsi baru ditambahkan.
    `funding.py` (28.121 B) dan `silang_funding.py` (29.873 B) terbesar; keduanya
    belum melampaui batas baris. `lubang_tebing.py` V1 di bawah batas.
50. Setiap pengukuran yang menyimpulkan dari KETIADAAN wajib memuat kendali
    positif. **[v46] Ditaati di `lubang_tebing` V1 dengan EMPAT bentangan buatan:**
    KENDALI_MATI_DULU → `mati_dulu`, KENDALI_SEREMPAK → `serempak`,
    KENDALI_LUBANG_DULU → `lubang_dulu`, KENDALI_TEBING → `serempak` + `di_tebing`
    true. `kendali_sah` true DAN `kendali_deteksi_sah` true.
52. Laporan yang tidak dapat dibaca utuh setara dengan laporan yang tidak ada. Ekor
    tiap berkas kode dan berkas panjang yang didorong wajib dibaca sesudah push.
    **[v46] Ditaati:** `lubang_tebing.py` V1 (blob `575e777e`),
    `test_lubang_tebing.py` (blob `bf57d69d`, 60 butir), `lubang_tebing.yml` (blob
    `c8ae552a`) dibaca ulang UTUH dari main sesudah push `84b11164`; jurnal 127
    (blob `9b5015eb`), ADR-A013 (blob `3a7f8612`), PROMPT v49 (blob `4dca042c`)
    dibaca ulang UTUH sesudah push. Ketiga berkas STATE v45 dibaca UTUH sebelum v46
    ditulis. Utang yang TETAP hidup: `tests/test_bentangan_kohort.py` V2 (63 butir,
    blob `9f850ecd`) belum dibaca ulang byte demi byte.
55. Rumusan pemicu workflow wajib dikutip dari berkas workflow beserta blobnya.
    **[v46] KOREKSI PENTING — lihat KC-41 di bawah.** Rumusan yang BENAR, dibaca
    dari blob `3134bc9f`: `lubang_awal.yml` ber-`paths` **satu entri saja**,
    `- 'lux_ai/serapan/lubang_awal.py'`. `lubang_tebing.yml` (blob `c8ae552a`) meniru
    berkas ASLI itu, bukan ingatan tentangnya.
57. Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB ditulis
    bernomor. **TERBUKTI DUA PULUH LIMA DARI DUA PULUH LIMA [v46]:**
    936 → 984 → **1044**; `test_lubang_tebing.py` 60 butir; 984 + 60 = **1044** ✅
    Mekanismenya deterministik — tiap kemenangan wajib disebut **MUDAH** dan TIDAK
    masuk papan skor sebagai kemenangan berisiko.
58. Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH DILARANG
    diramalkan dengan pita sempit.
63–76. Berlaku tanpa perubahan dari v43. Teks penuh di v43 (blob `a91a4934`).

**Penomoran aturan — TABRAKAN DISELESAIKAN DARI BERKAS [v46].** Jurnal 127 §9 dengan
sengaja menahan penomoran dua aturan baru karena catatan di ingatan tampak
bertentangan ("calon 77, 78" sementara 79 sudah dipakai). Pembacaan v45 UTUH
menjelaskan sebabnya: **77 dan 78 memang masih DIUSULKAN dan belum pernah berlaku,
sementara 79 sudah BERLAKU** — nomor di repo ini diberikan tidak selalu berurutan.
Karena itu dua aturan baru sah mengambil **80** dan **81**, dan 77/78 TETAP
ditahan sebagai usulan. Tidak ada nomor yang ditulis dari ingatan.

**Aturan 77 (TETAP DIUSULKAN, belum berlaku):** dua berkas laporan berblob IDENTIK
bukan dua pengukuran. Baru satu kasus (`bulan_absen.log` ==
`bulan_absen_ringkas.json`).

**Aturan 78 (TETAP DIUSULKAN, belum berlaku):** batas panjang alat adalah bagian dari
DESAIN repo. Struktur berkas wajib disesuaikan dengan batas terukur — ±2,4 MB baca,
±25–45 KB tulis. Belum resmi karena batas tulis baru diketahui secara kasar.

**Aturan 79 (BERLAKU sejak v44):** praregistrasi ramalan ditulis lebih dulu di
`journal/**` (yang ada di `paths-ignore`) SEBELUM modul pengukurnya dibuat.
**[v46] Ditaati di R-306** (praregistrasi jurnal 126 §7, dikunci sebelum modul ada)
dan **R-307** (praregistrasi jurnal 127 §7, dikunci sebelum modulnya ada).

**Aturan 80 (BERLAKU sejak v46; lahir dari R-306) — uji arah waktu wajib STRIKT dan
kelas `serempak` dilapor tersendiri.** Setiap perbandingan dua tanggal yang dipakai
untuk menyimpulkan ARAH wajib memakai perbandingan STRIKT (`<`, bukan `<=`), dan
kelas kesamaan ("serempak", bulan atau tanggal SAMA) wajib dilapor sebagai kelas
TERSENDIRI. Kelas `serempak` **DILARANG masuk numerator** klaim arah. Dasar
pengukuran: R-305 memakai `<=` dan mendapat 1.0 (118/118); R-306 memakai `<` di atas
penyebut yang sama dan mendapat 40 `mati_dulu` / 78 `serempak` / 0 `lubang_dulu`.
Dua pertiga "kemenangan" R-305 ternyata kelas serempak. Kerabat aturan 10, 44, 47.

**Aturan 81 (BERLAKU sejak v46; lahir dari R-306) — numerator yang dikuasai satu
bulan kalender wajib dilapor sebagai kemungkinan artefak satu peristiwa.** Bila satu
bulan kalender menguasai **≥ 1/4** numerator sebuah klaim, klaim itu WAJIB dilapor
bersama cacah per bulan dan ditandai sebagai kemungkinan artefak satu peristiwa;
dan kekuatan bukti yang LEPAS dari bulan penguasa itu wajib dinyatakan apa adanya.
Dasar pengukuran: 39 dari 40 (0.975) anggota `mati_dulu` berbagi bulan tebing
`2025-07`; bukti yang lepas dari tebing = **satu simbol** (BTCSTUSDT). Kerabat
aturan 10, 59, 74; penangkal KC-47.

## Kelas cacat

KC-1 s.d. KC-12 seperti v19; KC-10 dan KC-11 DITUTUP. KC-13 keterwakilan sampel.
**KC-16 DITARIK — nomornya TETAP kosong selamanya.** KC-17 DITUTUP. Teks penuh
KC-14, KC-15, KC-19..KC-29 ada di v37 (blob `f520d5e2`). KC-30..KC-42 ada di v43
(blob `a91a4934`). KC-43, KC-44 teks penuh di v44 (blob `ede3ce3b`). KC-45, KC-46
teks penuh di v45 (blob `e07f2de1`).

Ringkas KC-19..KC-46 satu baris: KC-19 mencacah dari ingatan · KC-20 bias ke bawah
· KC-21 ketiadaan gejala dari ketiadaan pengukuran · KC-22 mekanisme dipindah ·
KC-23 medan dipindah · KC-24 daftar dari laporan bercacah · KC-25 batas semesta tak
tersurat · KC-26 medan ekstrem membisu tentang seri · KC-27 karakterisasi dari
contoh berurut · KC-28 mencampur kelas instrumen · KC-29 taksonomi paralel · KC-30
nama kelas dibaca sebagai keadaan · KC-31 nama peristiwa dibaca sebagai mekanisme ·
KC-32 dua sistem penomoran dicampur · KC-33 mengenali satu peristiwa lalu berhenti ·
KC-34 cacah subkelompok dari pengurangan kepala · KC-35 cakupan kode dicampur
dengan cakupan laporan · KC-36 homonim diperlakukan satu konsep · KC-37 nol dari
satu penyebut sebagai bukti di penyebut lain · KC-38 kecocokan tanpa membedakan
mekanisme · KC-39 dua penyebut bulan absen dicampur · KC-40 daftar klausa gagal
dibaca sebagai keadaan · KC-41 pemicu workflow dirumuskan dari ingatan · KC-42
menulis ulang berkas melampaui batas push · KC-43 tanda tangan fungsi dari ingatan ·
KC-44 semua laporan di-commit satu langkah · KC-45 satuan "bulan tanpa funding" dan
"bulan MATI" dicampur · KC-46 lubang bentuk AWAL dibaca sebagai "funding berhenti".

**KC-41 — DUA KASUS BARU TERTANGKAP [v46]. Kelas ini ternyata yang paling sering
berulang, dan dua kali giliran ini korbannya adalah dokumen kami sendiri:**

1. **`STATE_LAMPIRAN_UKUR.md` v5** (blob `eb826817`) menulis bahwa `lubang_awal.yml`
   ber-`paths` pada `lux_ai/serapan/lubang_awal.py`, `tests/test_lubang_awal.py`,
   **dan workflow sendiri** — TIGA entri. Berkas asli (blob `3134bc9f`, dibaca UTUH)
   memuat **SATU** entri: `- 'lux_ai/serapan/lubang_awal.py'`. `STATE.md` v45
   menulisnya benar ("sempit pada modulnya"), jadi kedua bagian STATE saling
   bertentangan selama satu versi. DIKOREKSI di lampiran UKUR v6.
2. **PROMPT v49** (blob `4dca042c`, ditulis giliran ini) menyebut poros R-307 sebagai
   "H-A017 byte parquet". Pembacaan lampiran UKUR v5 menunjukkan **H-A017 adalah
   hipotesis arah sebab LITUSDT**; byte parquet hanya PENGAMATAN di ekornya. Label
   itu ditulis dari ingatan = KC-41. DIKOREKSI: poros R-307 adalah hipotesis baru
   **H-A018** (lihat lampiran UKUR v6). **Pita praregistrasi R-307 TIDAK berubah**
   — yang salah label, bukan angkanya (aturan 29 tetap utuh).

**Penangkal KC-41 yang diperkuat:** rumusan pemicu, label hipotesis, dan nomor
aturan WAJIB dikutip dari berkas beserta blobnya pada giliran yang sama. Bila
dua bagian STATE bertentangan, berkas SUMBER menang, bukan yang lebih baru.

- **KC-47 [RESMI sejak v46; lahir dari R-306] — satu peristiwa yang menyamar sebagai
  banyak pengamatan bebas.** Sumber terukur: dari **40** simbol `mati_dulu`, **39**
  ber-`bulan_lubang_bukan_awal_pertama` TEPAT `2025-07` (bulan tebing). Bagian 0.339
  itu benar sebagai cacah, tetapi derajat kebebasan efektifnya mendekati **1**, bukan
  40; bukti arah yang lepas dari tebing hanya **BTCSTUSDT**. Yang membuat kelas ini
  berbahaya: ia LOLOS dari penyebut yang benar, dari kendali positif, DAN dari
  perbandingan strikt — ketiganya sudah diterapkan di R-306. **Penangkal: aturan 81**
  (cacah per bulan wajib dilapor bila satu bulan menguasai ≥ 1/4 numerator) dan
  ADR-A013 (pemilahan tebing / bukan-tebing wajib). Kerabat KC-33 (mengenali satu
  peristiwa lalu berhenti) dan KC-38 (kecocokan tanpa mekanisme). Catatan
  bookkeeping: nomor KC-47 sudah pernah DIRUJUK MAJU secara salah di teks KC-45 v45
  ("kerabat KC-36 dan KC-47 satuan") ketika KC-47 belum ada; rujukan itu BATAL, dan
  KC-47 kini berarti kelas cacat di paragraf ini.

## Ke bagian 2 dan 3

Berkas ini berhenti di sini dengan sengaja. Lanjutannya:

- **Papan skor R-199..R-306 (total 306), catatan kejujuran, jumlah uji 1044, utang
  verifikasi 24, Daftar ADR A001–A013, temuan sampingan, penomoran berikutnya** →
  `STATE_LAMPIRAN_EKOR.md` v6.
- **Penyebut 787, taksonomi, karantina, bulan ABSEN, hipotesis H-A001..H-A018,
  lubang funding, modul/workflow/uji, API terverifikasi (`lubang_tebing` V1)** →
  `STATE_LAMPIRAN_UKUR.md` v6.
