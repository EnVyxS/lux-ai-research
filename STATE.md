# STATE — versi 45 (bagian 1 dari tiga)

Diperbarui: 2026-07-30 (sesi 58). Aturan hanya BERTAMBAH; jangan menulis ulang dari
ingatan. v45 disusun di atas `STATE.md` v44 (blob
**`ede3ce3b1ac820b108107236062c51afd5266e6f`**), `STATE_LAMPIRAN_EKOR.md` v4 (blob
**`67dda29e0847d81c149407f66b897523075345f3`**), dan `STATE_LAMPIRAN_UKUR.md` v4
(blob **`d302caff3c8d464924b45c84fe7685425989debf`**) — ketiganya DIBACA UTUH pada
giliran ini sebelum berkas ini ditulis (aturan 52, KC-42d, KC-43).

## STATE SEKARANG DIPECAH TIGA — BACA INI LEBIH DULU

Pembagian yang MENGIKAT sejak v43, berlanjut di v45:

1. **`STATE.md`** (berkas ini) — **bagian 1**: kepala, aturan bernomor 1–79, kelas
   cacat KC-1..KC-46. Berkas ini berhenti sesudah kelas cacat.
2. **`STATE_LAMPIRAN_EKOR.md`** v5 — **bagian 2**: papan skor lengkap R-199..R-305,
   catatan kejujuran, jumlah uji 984, utang verifikasi 24, Daftar ADR A001–A012,
   temuan sampingan, penomoran berikutnya.
3. **`STATE_LAMPIRAN_UKUR.md`** v5 — **bagian 3**: penyebut 787, taksonomi,
   karantina, bulan ABSEN, hipotesis, lubang funding, modul/workflow/uji, API
   terverifikasi (termasuk `lubang_awal` V1).
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip ekor v41; bukan sumber lagi.

**Ketiga berkas wajib dibaca bersama.** LANGKAH 0 PROMPT v48 wajib menyebut
ketiganya beserta blobnya.

Yang lahir sejak v44: **KC-45 dan KC-46 kini RESMI**; adjudikasi R-305 = MELESET;
**ADR-A012** (arah sebab A009 dicabut untuk SELURUH semesta); CI 936→**984**; modul
**`lubang_awal` V1** (sidik `156499ce`); praregistrasi R-306 dikunci di jurnal 126
§7 (aturan 79). Cacah direktori dikoreksi lewat pencacahan langsung: serapan 43,
workflows 38, tests 47.

## Aturan bernomor

Aturan **1–36** berlaku tanpa perubahan; teks di STATE v19 (blob `e06c486e…`),
ringkas di v37 (blob `f520d5e2`). **Aturan 10 (irisan/urutan bulan BUKAN sebab)
terbukti lagi di R-305:** butir 1 mencapai 100% justru karena tautologi lubang
bukan-awal ≈ bulan delisting — kecocokan urutan waktu bukan bukti arah sebab.

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
    `kode_keluar`). **[v45] Ditaati lagi:** CI **984** run **30522785099** (commit
    `d304d3eb`, 2026-07-30T07:23:33Z, kode 0, "984 tests collected"). Total
    pemakaian tercatat: **dua puluh sembilan**.
46. Kode dilarang menyimpulkan dari penyebut nol. **[v45] Ditaati di `lubang_awal`
    V1:** butir 2 R-305 penyebut 5 (<20) → KALAH, TIDAK dipaksa jadi kesimpulan.
48. Berkas modul mendekati 800 baris dipecah sebelum fungsi baru ditambahkan.
    `funding.py` (28.121 B) dan `silang_funding.py` (29.873 B) terbesar; keduanya
    belum melampaui batas baris. `lubang_awal.py` V1 (15.801 B) di bawah batas.
50. Setiap pengukuran yang menyimpulkan dari KETIADAAN wajib memuat kendali
    positif. **[v45] Ditaati di `lubang_awal` V1:** dua lapis — kendali data
    (BTCUSDT 2021-05/08/01 HIDUP+funding → `kendali_sah` true) DAN kendali detektor
    (`kendali_deteksi_sah` true).
52. Laporan yang tidak dapat dibaca utuh setara dengan laporan yang tidak ada. Ekor
    tiap berkas kode dan berkas panjang yang didorong wajib dibaca sesudah push.
    **[v45] Ditaati:** `lubang_awal.py` V1 (blob `8c36943d`), `test_lubang_awal.py`
    (blob `86c401ee`, 48 butir), `lubang_awal.yml` (blob `3134bc9f`) ketiganya
    dibaca ulang UTUH dari main sesudah push `d304d3eb`; PROMPT v48 dibaca ulang
    UTUH sesudah push. Utang yang TETAP hidup: `tests/test_bentangan_kohort.py` V2
    (63 butir, blob `9f850ecd`) belum dibaca ulang byte demi byte.
55. Rumusan pemicu workflow wajib dikutip dari berkas workflow beserta blobnya.
    **[v45]** `lubang_awal.yml` (blob `3134bc9f`) ber-`paths` sempit pada modulnya.
57. Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB ditulis
    bernomor. **TERBUKTI DUA PULUH EMPAT DARI DUA PULUH EMPAT [v45]:**
    879 → 936 → **984**; `test_lubang_awal.py` 48 butir; 936 + 48 = **984** ✅
    Mekanismenya deterministik — tiap kemenangan wajib disebut **MUDAH**.
58. Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH DILARANG
    diramalkan dengan pita sempit.
63–76. Berlaku tanpa perubahan dari v43. Teks penuh di v43 (blob `a91a4934`).

**Aturan 77 (DIUSULKAN, belum berlaku):** dua berkas laporan berblob IDENTIK bukan
dua pengukuran. Baru satu kasus (`bulan_absen.log` == `bulan_absen_ringkas.json`).

**Aturan 78 (DIUSULKAN, belum berlaku):** batas panjang alat adalah bagian dari
DESAIN repo. Struktur berkas wajib disesuaikan dengan batas terukur — ±2,4 MB baca,
±25–45 KB tulis. Belum resmi karena batas tulis baru diketahui secara kasar.

**Aturan 79 (BERLAKU sejak v44):** praregistrasi ramalan ditulis lebih dulu di
`journal/**` (yang ada di `paths-ignore`) SEBELUM modul pengukurnya dibuat.
**[v45] Ditaati di R-305** (praregistrasi jurnal 125 §7) dan R-306 (praregistrasi
jurnal 126 §7, dikunci sebelum modul R-306 dibuat).

## Kelas cacat

KC-1 s.d. KC-12 seperti v19; KC-10 dan KC-11 DITUTUP. KC-13 keterwakilan sampel.
**KC-16 DITARIK — nomornya TETAP kosong selamanya.** KC-17 DITUTUP. Teks penuh
KC-14, KC-15, KC-19..KC-29 ada di v37 (blob `f520d5e2`). KC-30..KC-42 ada di v43
(blob `a91a4934`). KC-43, KC-44 teks penuh di v44 (blob `ede3ce3b`).

Ringkas KC-19..KC-44 satu baris: KC-19 mencacah dari ingatan · KC-20 bias ke bawah
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
menulis ulang berkas melampaui batas push · KC-43 tanda tangan fungsi dari ingatan
(penangkal: baca modul yang diimpor UTUH giliran yang sama) · KC-44 semua laporan
di-commit satu langkah (penangkal: tiap berkas laporan commit sendiri-sendiri).

- **KC-45 [RESMI sejak v45; lahir dari R-304, dikukuhkan R-305] — mencampur satuan
  “bulan tanpa funding” dan “bulan MATI” dalam satu klaim kausal.** Sumber: H-A015
  dulu mencatat ICPUSDT 19 dan TLMUSDT 20 sebagai “bulan MATI” padahal satuannya
  “bulan TANPA FUNDING”; salah baca itu menyesatkan arah sebab ADR-A009 dan ramalan
  R-304 (MELESET). **Penangkal: setiap angka bulan yang menyangkut kematian pasar
  WAJIB menyebut satuannya tersurat di tempat ia ditulis.** Diresmikan sesudah
  R-305 mengukuhkan pola: satuan “bulan berlubang funding” dan “bulan MATI” berbeda
  dan tidak boleh dipertukarkan. Kerabat KC-36 (homonim) dan KC-47 satuan.
- **KC-46 [RESMI sejak v45; lahir dari R-304, dikukuhkan R-305] — lubang funding di
  BULAN PERTAMA riwayat simbol dibaca sebagai “funding berhenti”.** Sumber: ICPUSDT
  (bulan pertama 2021-05 = lubang pertama, selisih −14) dan TLMUSDT (2021-07 =
  lubang pertama, selisih −12) berlubang sejak bulan pertama — bukan funding
  berhenti, melainkan funding BELUM MULAI. **[v45] Dikukuhkan `lubang_awal` V1:**
  lubang bentuk AWAL LANGKA — hanya **5 dari 787** simbol (BNXUSDT, ICPUSDT,
  JUPUSDT, QTUMUSDT, TLMUSDT). ICP dan TLM lubang awalnya melewati kematian
  (`lubang_awal_berakhir_sebelum_mati` false) — sumber salah-baca R-304.
  **Penangkal: setiap tafsir arah waktu wajib memeriksa bentuk lubang
  (`bentuk_lubang_lokal` / medan `lubang_awal`) lebih dulu; lubang bentuk AWAL
  DILARANG dibaca sebagai “berhenti”.** Kerabat KC-36 dan KC-40.

## Ke bagian 2 dan 3

Berkas ini berhenti di sini dengan sengaja. Lanjutannya:

- **Papan skor R-199..R-305 (total 305), catatan kejujuran, jumlah uji 984, utang
  verifikasi 24, Daftar ADR A001–A012, temuan sampingan, penomoran berikutnya** →
  `STATE_LAMPIRAN_EKOR.md` v5.
- **Penyebut 787, taksonomi, karantina, bulan ABSEN, hipotesis H-A001..H-A017,
  lubang funding, modul/workflow/uji, API terverifikasi (`lubang_awal` V1)** →
  `STATE_LAMPIRAN_UKUR.md` v5.
