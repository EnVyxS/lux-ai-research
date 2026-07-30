# STATE — versi 47 (bagian 1 dari tiga)

Diperbarui: 2026-07-30 (sesi 59, lanjutan). Aturan hanya BERTAMBAH; jangan menulis
ulang dari ingatan. v47 disusun di atas `STATE.md` v46 (blob
**`41b5b585d202a2486ba6f15a0c0100d90e728dea`**), yang **DIBACA UTUH pada giliran ini
sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43).

**Catatan cara kerja giliran ini — dorongan BERTAHAP, kini SELESAI.** Ketiga bagian
STATE tidak didorong sekaligus seperti v46, melainkan satu per satu, masing-masing
didahului pembacaan UTUH atas versi sebelumnya dan disusul pembacaan ulang UTUH atas
hasilnya:

1. `STATE_LAMPIRAN_EKOR.md` **v7** — dasar v6 (`f3b2f5dd`) → commit `cfc42e70`, hasil
   dibaca ulang blob **`9e906dfb`**.
2. `STATE_LAMPIRAN_UKUR.md` **v7** — dasar v6 (`27e59a79`) → commit `b5f1cfef`, hasil
   dibaca ulang blob **`4e7fb65b`**.
3. `STATE.md` **v47** — berkas ini.

Sebabnya: `push_files` menulis ulang SELURUH berkas, dan menyusun tiga berkas besar
dari satu konteks yang sudah terpakai banyak adalah cara paling pasti merusak aturan
1–81 (KC-42, KC-43). Selama keadaan setengah-jalan itu, peringatan keserasian versi
ditulis di kepala EKOR v7 dan UKUR v7 agar penerus tidak tertipu. **Dengan naiknya
berkas ini, peringatan itu GUGUR: ketiga bagian kini serasi pada v47/v7/v7.**

## STATE DIPECAH TIGA — BACA INI LEBIH DULU

Pembagian yang MENGIKAT sejak v43, berlanjut di v47:

1. **`STATE.md`** (berkas ini) — **bagian 1**: kepala, aturan bernomor 1–81 (plus
   usulan 77, 78, 82), kelas cacat KC-1..**KC-48**. Berkas ini berhenti sesudah
   kelas cacat.
2. **`STATE_LAMPIRAN_EKOR.md`** v7 — **bagian 2**: papan skor lengkap R-199..**R-307**,
   catatan kejujuran, jumlah uji **1100**, utang verifikasi 24, Daftar ADR
   A001–**A014**, temuan sampingan, penomoran berikutnya.
3. **`STATE_LAMPIRAN_UKUR.md`** v7 — **bagian 3**: penyebut 787, taksonomi, karantina,
   bulan ABSEN, hipotesis (termasuk **H-A018 yang kini SUDAH DIUKUR**), lubang
   funding, **byte parquet atas seluruh semesta**, modul/workflow/uji, API
   terverifikasi (termasuk `byte_semesta` V1), praregistrasi **R-308**.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip ekor v41; bukan sumber lagi.

**Ketiga berkas wajib dibaca bersama.** LANGKAH 0 PROMPT wajib menyebut ketiganya.

Yang lahir sejak v46: adjudikasi **R-307 = MELESET**; **ADR-A014** (byte parquet —
arah H-A018 didukung, pita gugur, "kecil" BUKAN penanda mati); **KC-48 RESMI**;
**aturan 82 DIUSULKAN**; CI 1044 → **1100**; modul **`byte_semesta` V1** (sidik
`e02aca2b…`); pengukuran PERTAMA byte parquet semesta (**32.706.262.375** byte);
praregistrasi **R-308** dikunci di jurnal 128 §9 (aturan 79); cacah direktori tangan
44 / 39 / 48 pada ref `d73b07b9`.

## Aturan bernomor

Aturan **1–36** berlaku tanpa perubahan; teks di STATE v19 (blob `e06c486e…`),
ringkas di v37 (blob `f520d5e2`).

**Aturan 10 (irisan/urutan bulan BUKAN sebab)** tetap seperti v46, terbukti tiga kali;
R-307 tidak menyentuhnya karena porosnya bukan arah waktu.

**Aturan 29 (pita praregistrasi TIDAK boleh diubah sesudah pengukuran) diuji paling
keras sejauh ini di R-307 [v47].** Butir 1 kalah dengan selisih tipis — terukur
**0.017704** lawan ambang bawah **0.02** — dan arah hipotesisnya justru DIDUKUNG kuat
oleh data yang sama. Godaan melebarkan pita menjadi "0.015..0.15" nyata dan ditolak.
R-307 dicatat **MELESET**. Hipotesis yang benar arahnya TIDAK menyelamatkan ramalan
yang salah angkanya (ADR-A014 keputusan 1).

**Aturan 43 (toleransi berskala) mendapat bentuk kegagalan barunya di R-307 [v47]:**
yang salah bukan lebar pita melainkan **letak** ambang — 10.000 byte pada semesta yang
dasarnya 22.440 byte. Toleransi berskala tidak menolong bila skalanya sendiri belum
pernah diukur. Lahirnya KC-48 dan usulan aturan 82.

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
    `kode_keluar`). **[v47] Ditaati lagi:** CI **1100** run **30526358010** (commit
    `d3bc2039`, 2026-07-30T08:21:45Z, kode 0, "1100 tests collected in 0.56s", blob
    `0765ce7b`). Total pemakaian tercatat: **tiga puluh dua**.
45. Keatomikan push pemicu. **[v47] Ditaati:** trio `byte_semesta` (modul + uji +
    workflow) didorong dalam SATU `push_files` (`d3bc2039`), sehingga CI dan workflow
    modul menyala atas pohon yang sama.
46. Kode dilarang menyimpulkan dari penyebut nol. **[v47] Ditaati di `byte_semesta`
    V1:** `cacah_terukur_byte_kecil` = 0 hanya diklaim TERUKUR karena
    `kendali_deteksi` membuktikan kelas itu terlihat pada bentangan buatan.
48. Berkas modul mendekati 800 baris dipecah sebelum fungsi baru ditambahkan.
    `funding.py` (28.121 B) dan `silang_funding.py` (29.873 B) terbesar; keduanya
    belum melampaui batas baris. `byte_semesta.py` V1 di bawah batas.
50. Setiap pengukuran yang menyimpulkan dari KETIADAAN wajib memuat kendali
    positif. **[v47] Ditaati di `byte_semesta` V1:** `kendali_deteksi(ambang=50)`
    memisahkan dua baris berbyte kecil (5 dan 10) dari baris tepat DI AMBANG (tidak
    terhitung — perbandingan strikt) dan dari baris kelas LAIN berbyte kecil.
    `kendali_sah` true (tiga parquet terbesar seluruhnya BTCUSDT, HIDUP, berfunding)
    DAN `kendali_deteksi_sah` true. Karena itu nol pada butir 2 R-307 sah disebut
    TERUKUR, bukan buta.
52. Laporan yang tidak dapat dibaca utuh setara dengan laporan yang tidak ada. Ekor
    tiap berkas kode dan berkas panjang yang didorong wajib dibaca sesudah push.
    **[v47] Ditaati:** `byte_semesta.py` V1 (`ff68e4be`), `test_byte_semesta.py`
    (`0e1e3ab2`, 56 butir), `byte_semesta.yml` (`45650ff9`) dibaca ulang UTUH dari
    main sesudah push `d3bc2039`; `reports/byte_semesta.json` (`8b7f2077`) terbaca
    **UTUH**; jurnal 128 (`13c06f61`) dan ADR-A014 (`6d77c2cd`) dibaca ulang UTUH
    sesudah push `69bfdd5d`; EKOR v7 (`9e906dfb`) dan UKUR v7 (`4e7fb65b`) dibaca
    ulang UTUH sesudah pushnya masing-masing; `silang_funding.py` V2 (`42c3aa9d`) dan
    `lubang_awal.py` V1 (`8c36943d`) dibaca UTUH SEBELUM modul R-307 ditulis.
    Utang yang TETAP hidup: `tests/test_bentangan_kohort.py` V2 (63 butir, blob
    `9f850ecd`) belum dibaca ulang byte demi byte.
55. Rumusan pemicu workflow wajib dikutip dari berkas workflow beserta blobnya.
    **[v47] Ditaati:** `byte_semesta.yml` (blob `45650ff9`) dibaca UTUH — `paths`
    **satu entri saja**, `- 'lux_ai/serapan/byte_semesta.py'`, meniru `lubang_awal.yml`
    asli (`3134bc9f`) yang juga dibaca ulang giliran ini. Koreksi KC-41 kasus 1 tetap
    berlaku dan tetap tercatat di lampiran UKUR v7.
57. Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB ditulis
    bernomor. **TERBUKTI DUA PULUH ENAM DARI DUA PULUH ENAM [v47]:**
    984 → 1044 → **1100**; `test_byte_semesta.py` 56 butir; 1044 + 56 = **1100** ✅
    Ramalan 56 diucapkan di chat SEBELUM push. Mekanismenya deterministik — tiap
    kemenangan wajib disebut **MUDAH** dan TIDAK masuk papan skor sebagai kemenangan
    berisiko.
58. Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH DILARANG
    diramalkan dengan pita sempit.
63–76. Berlaku tanpa perubahan dari v43. Teks penuh di v43 (blob `a91a4934`).

**Penomoran aturan [v47].** Tidak ada aturan baru yang DIRESMIKAN giliran ini. Aturan
resmi tetap sampai **81**. Nomor **82** dicadangkan untuk usulan di bawah, belum
berlaku. Nomor tidak pernah ditulis dari ingatan; ketiganya dibaca dari v46.

**Aturan 77 (TETAP DIUSULKAN, belum berlaku):** dua berkas laporan berblob IDENTIK
bukan dua pengukuran. Baru satu kasus (`bulan_absen.log` ==
`bulan_absen_ringkas.json`).

**Aturan 78 (TETAP DIUSULKAN, belum berlaku — tetapi MENGUAT [v47]):** batas panjang
alat adalah bagian dari DESAIN repo. Struktur berkas wajib disesuaikan dengan batas
terukur — ±2,4 MB baca, ±25–45 KB tulis. **Bukti pendukung baru:** `lubang_tebing.json`
dulu terpotong pada 99%, maka `byte_semesta` V1 sengaja dirancang ringkas
(`BATAS_BARIS_LAPORAN=40`) dan laporannya terbaca **UTUH**. Rancangan yang tunduk pada
batas alat terbukti menyelamatkan adjudikasi. Belum diresmikan karena ini kasus
rancangan, bukan pengukuran batasnya sendiri; batas tulis masih diketahui kasar.

**Aturan 79 (BERLAKU sejak v44):** praregistrasi ramalan ditulis lebih dulu di
`journal/**` (yang ada di `paths-ignore`) SEBELUM modul pengukurnya dibuat.
**[v47] Ditaati di R-307** (praregistrasi jurnal 127 §7) **dan R-308** (praregistrasi
jurnal 128 §9, dikunci sebelum modulnya ada, disalin apa adanya ke lampiran UKUR v7).

**Aturan 80 (BERLAKU sejak v46; lahir dari R-306) — uji arah waktu wajib STRIKT dan
kelas `serempak` dilapor tersendiri.** Teks penuh seperti v46. Kelas `serempak`
DILARANG masuk numerator klaim arah. Kerabat aturan 10, 44, 47.

**Aturan 81 (BERLAKU sejak v46; lahir dari R-306) — numerator yang dikuasai satu
bulan kalender wajib dilapor sebagai kemungkinan artefak satu peristiwa.** Teks penuh
seperti v46: ambang **≥ 1/4** numerator, wajib disertai cacah per bulan, dan kekuatan
bukti yang LEPAS dari bulan penguasa wajib dinyatakan apa adanya. Kerabat aturan 10,
59, 74; penangkal KC-47.

**Aturan 82 (DIUSULKAN sejak jurnal 128 §7 — BELUM BERLAKU; nomor dicadangkan) —
ambang absolut pada besaran yang belum pernah disebar-ukur DILARANG dipakai sebagai
butir berisiko.** Praregistrasi wajib memuat salah satu: (a) sebaran terukur besaran
itu (min/maks/rata atau kuantil) yang dikutip beserta sumbernya, atau (b) ambang yang
dinyatakan RELATIF terhadap sebaran yang akan diukur pada run yang sama. Dasar
pengukuran: butir 2 R-307 memakai ambang absolut **10.000** byte sementara nilai
terkecil di seluruh 19.586 simbol-bulan adalah **22.440** byte — butir itu tidak
pernah dapat menguji apa pun. Belum diresmikan karena **baru satu kasus**. Kerabat
aturan 43, 44; penangkal KC-48. Praregistrasi R-308 sudah menaatinya lebih dulu
(ambang 97.634 dan 150.000 keduanya diambil dari sebaran terukur R-307).

## Kelas cacat

KC-1 s.d. KC-12 seperti v19; KC-10 dan KC-11 DITUTUP. KC-13 keterwakilan sampel.
**KC-16 DITARIK — nomornya TETAP kosong selamanya.** KC-17 DITUTUP. Teks penuh
KC-14, KC-15, KC-19..KC-29 ada di v37 (blob `f520d5e2`). KC-30..KC-42 ada di v43
(blob `a91a4934`). KC-43, KC-44 teks penuh di v44 (blob `ede3ce3b`). KC-45, KC-46
teks penuh di v45 (blob `e07f2de1`). KC-47 teks penuh di v46 (blob `41b5b585`).

Ringkas KC-19..KC-47 satu baris: KC-19 mencacah dari ingatan · KC-20 bias ke bawah
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
"bulan MATI" dicampur · KC-46 lubang bentuk AWAL dibaca sebagai "funding berhenti" ·
KC-47 satu peristiwa menyamar sebagai banyak pengamatan bebas.

**KC-41 — dua kasus v46 tetap tercatat** (lampiran UKUR v5 salah mengutip `paths`
`lubang_awal.yml`; PROMPT v49 salah melabeli poros R-307 sebagai H-A017). Keduanya
sudah DIKOREKSI di UKUR v6/v7 dan PROMPT v50, dan koreksinya sengaja TIDAK dihapus —
menghapus jejak cacat sama dengan menghapus buktinya. **Penangkal yang berlaku:**
rumusan pemicu, label hipotesis, dan nomor aturan WAJIB dikutip dari berkas beserta
blobnya pada giliran yang sama. Bila dua bagian STATE bertentangan, berkas SUMBER
menang, bukan yang lebih baru.

- **KC-48 [RESMI sejak v47; lahir dari R-307] — ambang absolut ditetapkan pada
  besaran yang sebarannya belum pernah diukur.** Sumber terukur: butir 2 R-307
  memakai ambang **10.000 byte**, sementara pengukuran pada run yang sama menunjukkan
  berkas TERKECIL di seluruh 19.586 simbol-bulan adalah **22.440 byte** dan
  `cacah_byte_nol` = **0**. Tidak ada satu pun data yang mungkin lolos ambang itu,
  sehingga pita 20..400 mustahil terpenuhi oleh semesta apa pun — butir itu **tidak
  pernah menguji alam**, hanya menguji kelalaian saya. Yang membuat kelas ini
  berbahaya: ia LOLOS dari praregistrasi yang jujur (aturan 79), dari kendali positif
  (aturan 50), dan dari penyebut yang benar (aturan 44) — ketiganya sudah diterapkan
  di R-307, dan tetap menghasilkan butir kosong. Kegagalan semacam ini **tidak
  mengajarkan apa pun tentang alam**, dan karena itu lebih buruk daripada kekalahan
  biasa. **Penangkal: usulan aturan 82** (ambang wajib bersandar sebaran terukur atau
  dinyatakan relatif). Kerabat KC-20 (bias ke bawah), KC-25 (batas semesta tak
  tersurat), dan aturan 43 (toleransi berskala). Catatan pembeda: KC-48 BUKAN soal
  pita yang terlalu sempit — butir 1 R-307 kalah tipis karena aritmetika yang tidak
  saya kerjakan, dan itu kekalahan yang SAH serta mengajarkan sesuatu. Kedua
  kekalahan R-307 berbeda jenis dan dilarang disamakan (ADR-A014).

## Ke bagian 2 dan 3

Berkas ini berhenti di sini dengan sengaja. Lanjutannya:

- **Papan skor R-199..R-307 (total 307: TEPAT 215 · MELESET 57 · SEPARUH 20 · TIDAK
  TERADJUDIKASI 8 · MENUNGGU 7), catatan kejujuran, jumlah uji 1100, utang
  verifikasi 24, Daftar ADR A001–A014, temuan sampingan, penomoran berikutnya** →
  `STATE_LAMPIRAN_EKOR.md` v7 (blob `9e906dfb`).
- **Penyebut 787, taksonomi, karantina, bulan ABSEN, hipotesis H-A001..H-A018, byte
  parquet semesta (32.706.262.375), lubang funding, modul/workflow/uji, API
  terverifikasi (`byte_semesta` V1), praregistrasi R-308** →
  `STATE_LAMPIRAN_UKUR.md` v7 (blob `4e7fb65b`).
