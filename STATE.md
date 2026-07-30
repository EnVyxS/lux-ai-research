# STATE — versi 48 (bagian 1 dari tiga)

Diperbarui: 2026-07-30 (sesi 60). Aturan hanya BERTAMBAH; jangan menulis ulang dari
ingatan. v48 disusun di atas `STATE.md` v47 (blob
**`7642b75d0ba7cd8612d83c3a43bff1274d8cac57`**), yang **DIBACA UTUH pada giliran ini
sebelum berkas ini ditulis** (aturan 52, KC-42d, KC-43).

**Ketimpangan versi yang disengaja kini SELESAI.** Dorongan bertahap giliran lalu
menaikkan lampiran lebih dulu dan meninggalkan bagian 1 tertinggal:

1. `STATE_LAMPIRAN_EKOR.md` **v8** — commit `ea141915`, blob
   **`c34c88e27dce4813622c2e3ea71bf4d486ec65d6`**, dibaca UTUH giliran ini.
2. `STATE_LAMPIRAN_UKUR.md` **v8** — blob
   **`ff19069512bd4604b18cedb896af1d6cf6ba2557`**, dibaca UTUH giliran ini.
3. `STATE.md` **v48** — berkas ini.

Selama keadaan setengah-jalan itu, **KC-49** dan **usulan aturan 83** hanya sah dari
`journal/2026-07-30-129.md` §6 (blob `ecb6ac241d84f06767195f931f8418fa1c853ba2`) dan
`decisions/ADR-A015.md` (blob `387d551051da4f0d539f7c9c26e438a9ac84c9a3`), keduanya
commit `982c2536`. **Dengan naiknya berkas ini, peringatan keserasian di kepala kedua
lampiran GUGUR: ketiga bagian kini serasi pada v48 / v8 / v8.** Peringatan itu tetap
tertulis di lampiran sebagai jejak; jangan memperlakukannya sebagai utang hidup.

Sebab pemecahan tetap sama: `push_files` menulis ulang SELURUH berkas, dan menyusun
tiga berkas besar dari satu konteks yang sudah terpakai banyak adalah cara paling
pasti merusak aturan 1–81 (KC-42, KC-43).

## STATE DIPECAH TIGA — BACA INI LEBIH DULU

Pembagian yang MENGIKAT sejak v43, berlanjut di v48:

1. **`STATE.md`** (berkas ini) — **bagian 1**: kepala, aturan bernomor 1–81 (plus
   usulan 77, 78, 82, 83), kelas cacat KC-1..**KC-49**. Berkas ini berhenti sesudah
   kelas cacat.
2. **`STATE_LAMPIRAN_EKOR.md`** v8 — **bagian 2**: papan skor lengkap
   R-199..**R-308**, catatan kejujuran, jumlah uji **1168**, utang verifikasi 24,
   Daftar ADR A001–**A015**, temuan sampingan, penomoran berikutnya.
3. **`STATE_LAMPIRAN_UKUR.md`** v8 — **bagian 3**: penyebut 787, taksonomi, karantina,
   bulan ABSEN, hipotesis (**H-A018** diukur dua kali, **H-A019** didaftarkan), lubang
   funding, byte parquet semesta, **lebar zona irisan byte**, modul/workflow/uji, API
   terverifikasi (termasuk `irisan_byte` V1), praregistrasi **R-309**.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip ekor v41; bukan sumber lagi.

**Ketiga berkas wajib dibaca bersama.** LANGKAH 0 PROMPT wajib menyebut ketiganya.

Yang lahir sejak v47: adjudikasi **R-308 = SEPARUH**; **ADR-A015** (pita praregistrasi
wajib melewati aritmetika implikasi); **KC-49 RESMI**; **aturan 83 DIUSULKAN**; usulan
aturan 82 DIPERLUAS; CI 1100 → **1168**; modul **`irisan_byte` V1** (sidik
`0e7103ef…`); pengukuran PERTAMA lebar zona irisan byte (**38** HIDUP di bawah
`byte_min` MATI, **0** MATI di zona itu); **H-A019 didaftarkan**; **aturan 57 PUTUS**
pada giliran ke-27 (26/27); cacah tangan tiga direktori LUNAS pada ref `5a777664`
(45 / 49 / 40); praregistrasi **R-309** dikunci di jurnal 129 §10 (aturan 79).

## Aturan bernomor

Aturan **1–36** berlaku tanpa perubahan; teks di STATE v19 (blob `e06c486e…`),
ringkas di v37 (blob `f520d5e2`).

**Aturan 10 (irisan/urutan bulan BUKAN sebab)** tetap seperti v47. R-308 tidak
menyentuhnya karena porosnya bukan arah waktu.

**Aturan 21 (total papan skor dihitung tangan). [v48] Ditaati:** 215 + 57 + 21 + 8 + 7
= **308**, dijumlah tangan di EKOR v8.

**Aturan 29 (pita praregistrasi TIDAK boleh diubah sesudah pengukuran) diuji lagi di
R-308 [v48].** Butir 2 terukur **2** lawan pita **10..300**. Godaan mengubah pita
menjadi "1..300" — yang akan mengubah kekalahan menjadi kemenangan — direkam di
ADR-A015 keputusan 4 lalu DITOLAK. R-308 dicatat **SEPARUH**. Bersama R-307, aturan
ini kini dua giliran berturut menahan godaan yang nyata, bukan hipotetis.

**Aturan 36 (dua modul berbeda atas semesta sama wajib cocok). [v48] Ditaati:**
sebaran byte per kelas dari `irisan_byte` V1 IDENTIK dengan `byte_semesta` V1
(HIDUP 18.087 / 22.440 / 1.771.962,899 · SEPI 98 · MATI 1.401 / 97.634 / 451.875 /
413.305,781 · total 32.706.262.375), dan keempat sidik data seragam cocok lagi.

**Aturan 43 (toleransi berskala) mendapat bentuk kegagalan KEDUA-nya di R-308 [v48]:**
sesudah R-307 mengajarkan bahwa **letak** ambang bisa mustahil (KC-48), R-308
mengajarkan bahwa letak ambang bisa **sudah tersirat** oleh momen yang telah diukur.
Rata MATI 413.306 yang duduk hanya ~8% di bawah maksimum 451.875 memaksa ekor bawah
tipis; terukur 2. Lahirnya KC-49 dan usulan aturan 83.

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
    `kode_keluar`). **[v48] Ditaati:** CI **1168** run **30529294152** (commit
    **`d22364b9bf680c9e3bbafa0c28672b3b561db702`**, 2026-07-30T09:05:52Z, kode 0,
    1168 butir terkumpul). **Blob berkas laporan itu TIDAK dicatat saat dibaca** —
    cacat administratif yang diakui; jangan mengarang empat puluh karakternya, baca
    ulang dari main bila diperlukan. Total pemakaian tercatat: **tiga puluh tiga**.
45. Keatomikan push pemicu. **[v48] Ditaati:** trio `irisan_byte` (modul + uji +
    workflow) didorong dalam SATU `push_files` (`d22364b9`), sehingga CI dan workflow
    modul menyala atas pohon yang sama.
46. Kode dilarang menyimpulkan dari penyebut nol. **[v48] Ditaati di `irisan_byte`
    V1:** cacah kecil hanya diklaim TERUKUR karena `kendali_deteksi` membuktikan
    kelas itu terlihat pada bentangan buatan.
47. Satuan cacah tersurat. **[v48] Ditaati:** "38" bersatuan **simbol-bulan HIDUP**,
    bukan simbol; "2" bersatuan simbol-bulan MATI.
48. Berkas modul mendekati 800 baris dipecah sebelum fungsi baru ditambahkan.
    `funding.py` (28.121 B) dan `silang_funding.py` (29.873 B) terbesar; keduanya
    belum melampaui batas baris. `irisan_byte.py` V1 di bawah batas.
50. Setiap pengukuran yang menyimpulkan dari KETIADAAN wajib memuat kendali
    positif. **[v48] Ditaati di `irisan_byte` V1:** `kendali_deteksi(ambang=50)` →
    `hidup_kecil` **2** (harap 2), `mati_kecil` **1** (harap 1), `total` **1922**;
    baris tepat DI AMBANG tidak terhitung (perbandingan strikt). `kendali_data_sah`
    true (tiga parquet terbesar seluruhnya BTCUSDT: 2021-05 2.770.666, 2021-08
    2.730.341, 2021-01 2.722.266, ketiganya HIDUP) DAN `kendali_deteksi_sah` true.
    Karena itu "NOL baris MATI di zona 22.440–97.634" sah disebut TERUKUR, bukan buta.
52. Laporan yang tidak dapat dibaca utuh setara dengan laporan yang tidak ada. Ekor
    tiap berkas kode dan berkas panjang yang didorong wajib dibaca sesudah push.
    **[v48] Ditaati:** `irisan_byte.py` V1 (`2dbe3d55`), `tests/test_irisan_byte.py`
    (`b6389051`, **68** butir dicacah tangan), `.github/workflows/irisan_byte.yml`
    (`7d98a267`) dibaca ulang UTUH dari main sesudah push `d22364b9`;
    `reports/irisan_byte.json` (`4c13bf6a`) terbaca **UTUH**; `_status.json`
    (`863dc4cb`) terbaca utuh; jurnal 129 (`ecb6ac24`) dan ADR-A015 (`387d5510`)
    dibaca ulang UTUH sesudah push `982c2536`; EKOR v8 (`c34c88e2`) dan UKUR v8
    (`ff190695`) dibaca UTUH sebelum berkas ini ditulis; PROMPT v51 (`dc5ef264`) dan
    `STATE.md` v47 (`7642b75d`) dibaca UTUH pada giliran ini.
    Utang yang TETAP hidup: `tests/test_bentangan_kohort.py` V2 (63 butir, blob
    `9f850ecd`) belum dibaca ulang byte demi byte — **kini enam versi menunggu.**
55. Rumusan pemicu workflow wajib dikutip dari berkas workflow beserta blobnya.
    **[v48] Ditaati:** `irisan_byte.yml` (blob `7d98a267`) dibaca UTUH — `paths`
    **satu entri saja**, `- 'lux_ai/serapan/irisan_byte.py'`, meniru `lubang_awal.yml`
    asli (`3134bc9f`). Koreksi KC-41 kasus 1 tetap berlaku dan tetap tercatat di
    lampiran UKUR v8.
57. Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB ditulis
    bernomor. **[v48] PUTUS pada giliran ke-27; catatan resmi 26 DARI 27.**
    Diucapkan 67 butir dan CI 1167 sebelum push; sebenarnya **68** dan **1168**.
    Sebab tepat: dalam daftar bernomor yang diucapkan, kelompok `uji_r308` ditulis
    "56–62" (tujuh) padahal kode berisi delapan — `test_uji_butir2_kalah` hilang dari
    DAFTAR, bukan dari kode. Angka 1168 yang diperbaiki SESUDAH membaca berkas TIDAK
    menghapus kegagalan ramalan pertama; perbaikan pasca-melihat bukan ramalan.
    **Hitungan beruntun dimulai lagi dari nol.** Mekanismenya tetap deterministik —
    tiap kemenangan wajib disebut **MUDAH** dan TIDAK masuk papan skor.
58. Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH DILARANG
    diramalkan dengan pita sempit.
63–76. Berlaku tanpa perubahan dari v43. Teks penuh di v43 (blob `a91a4934`).

**Aturan 66 (cacah direktori dengan TANGAN, bernomor, bukan pengurangan dari angka
lama). [v48] Ditaati dan utang LUNAS:** pada ref **`5a777664`** ketiga direktori
dicacah satu per satu — `lux_ai/serapan/` **45** (`__init__` 1 … `ukur_baris` 45),
`tests/` **49** (`test_anatomi_tengah` 1 … `test_ukur_baris` 49),
`.github/workflows/` **40** (`anatomi_tengah` 1 … `ukur_baris` 40). Ketiganya cocok
dengan turunan v7. **Kecocokan itu TIDAK menyahkan kebiasaan mengutip turunan**
(KC-33). **Angka SESUDAH trio `irisan_byte` — 46 / 50 / 41 — masih TURUNAN dan belum
dicacah tangan; jangan dikutip sebagai fakta terhitung.**

**Penomoran aturan [v48].** Tidak ada aturan baru yang DIRESMIKAN giliran ini. Aturan
resmi tetap sampai **81**. Nomor **82** dan **83** dicadangkan untuk usulan di bawah,
keduanya belum berlaku. **Aturan berikutnya yang bebas: 84.** Nomor tidak pernah
ditulis dari ingatan; keempatnya dibaca dari v47, EKOR v8, dan ADR-A015.

**Aturan 77 (TETAP DIUSULKAN, belum berlaku):** dua berkas laporan berblob IDENTIK
bukan dua pengukuran. Baru satu kasus (`bulan_absen.log` ==
`bulan_absen_ringkas.json`).

**Aturan 78 (TETAP DIUSULKAN, belum berlaku — MENGUAT LAGI [v48]):** batas panjang
alat adalah bagian dari DESAIN repo. Struktur berkas wajib disesuaikan dengan batas
terukur — ±2,4 MB baca, ±25–45 KB tulis. **Bukti pendukung baru:**
`BATAS_BARIS_LAPORAN=40` membuat `irisan_byte.json` terbaca UTUH — kedua kalinya
berturut sesudah `byte_semesta.json`, sementara `lubang_tebing.json` berbatas 60 dulu
terpotong. Belum diresmikan karena ini kasus rancangan, bukan pengukuran batasnya
sendiri; batas tulis masih diketahui kasar.

**Aturan 79 (BERLAKU sejak v44):** praregistrasi ramalan ditulis lebih dulu di
`journal/**` (yang ada di `paths-ignore`) SEBELUM modul pengukurnya dibuat.
**[v48] Ditaati di R-308** (praregistrasi jurnal 128 §9, tidak disentuh sampai
adjudikasi) **dan R-309** (praregistrasi jurnal 129 §10, dikunci sebelum modulnya
ada, disalin apa adanya ke lampiran UKUR v8).

**Aturan 80 (BERLAKU sejak v46; lahir dari R-306) — uji arah waktu wajib STRIKT dan
kelas `serempak` dilapor tersendiri.** Teks penuh seperti v46. Kelas `serempak`
DILARANG masuk numerator klaim arah. Kerabat aturan 10, 44, 47. R-308 tidak
menyentuhnya, tetapi perbandingan STRIKT `<` dipakai konsisten di `cacah_di_bawah`.

**Aturan 81 (BERLAKU sejak v46; lahir dari R-306) — numerator yang dikuasai satu
bulan kalender wajib dilapor sebagai kemungkinan artefak satu peristiwa.** Teks penuh
seperti v46: ambang **≥ 1/4** numerator, wajib disertai cacah per bulan, dan kekuatan
bukti yang LEPAS dari bulan penguasa wajib dinyatakan apa adanya. Kerabat aturan 10,
59, 74; penangkal KC-47. **[v48] Relevan untuk R-309:** dari 38 baris HIDUP-kecil,
tiga di antaranya berbulan `2026-06` — bila numerator butir 1 R-309 nanti dikuasai
satu bulan, aturan ini wajib dipakai saat melaporkannya.

**Aturan 82 (DIUSULKAN sejak jurnal 128 §7, DIPERLUAS oleh ADR-A015 kep. 3 — BELUM
BERLAKU; nomor dicadangkan) — ambang yang MUSTAHIL dilewati ATAU yang hasilnya SUDAH
TERSIRAT oleh ukuran sebelumnya DILARANG dipakai sebagai butir berisiko.**
Praregistrasi wajib memuat salah satu: (a) sebaran terukur besaran itu (min/maks/rata
atau kuantil) yang dikutip beserta sumbernya, atau (b) ambang yang dinyatakan RELATIF
terhadap sebaran yang akan diukur pada run yang sama. Dasar pengukuran: butir 2 R-307
memakai ambang absolut 10.000 byte sementara nilai terkecil di seluruh 19.586
simbol-bulan adalah 22.440 byte. Perluasan v48: ambang 150.000 pada butir 2 R-308
DAPAT dilewati dan memang dilewati dua kali — jadi ia lolos bentuk lama aturan ini,
tetapi tetap salah letak. Belum diresmikan karena bentuk perluasannya baru satu
kasus. Kerabat aturan 43, 44, 83; penangkal KC-48 dan KC-49.

**Aturan 83 (DIUSULKAN sejak ADR-A015 kep. 2 — BELUM BERLAKU; nomor dicadangkan) —
sebelum mengunci pita praregistrasi, tuliskan di jurnal aritmetika implikasi dari
setiap momen terukur yang relevan.** Bila aritmetika itu sudah menentukan jawabannya
dalam satu angka signifikan, butir tersebut **bukan ramalan berisiko** dan harus
diganti atau dipindah porosnya. Dasar pengukuran: dua kekalahan berturut yang sebabnya
sama — R-307 butir 1 (7,153% baris ÷ nisbah rata 4,3 ≈ 1,7% byte, dapat dihitung
sebelum run; pita 0.02..0.15 tidak memuatnya) dan R-308 butir 2 (rata MATI 413.306
hanya ~8% di bawah maksimum 451.875 → ekor bawah pasti tipis; terukur 2 lawan pita
10..300). Belum diresmikan karena baru dua kasus dan bentuk pelaksanaannya ("satu
angka signifikan") belum diuji pada praregistrasi yang MENANG. **Praregistrasi R-309
sudah menaatinya lebih dulu** (aritmetika implikasi ditulis di jurnal 129 §10 sebelum
pita 22..38 dan 0.10..0.60 dikunci). Kerabat aturan 29, 43, 44, 82; penangkal KC-49.

## Kelas cacat

KC-1 s.d. KC-12 seperti v19; KC-10 dan KC-11 DITUTUP. KC-13 keterwakilan sampel.
**KC-16 DITARIK — nomornya TETAP kosong selamanya.** KC-17 DITUTUP. Teks penuh
KC-14, KC-15, KC-19..KC-29 ada di v37 (blob `f520d5e2`). KC-30..KC-42 ada di v43
(blob `a91a4934`). KC-43, KC-44 teks penuh di v44 (blob `ede3ce3b`). KC-45, KC-46
teks penuh di v45 (blob `e07f2de1`). KC-47 teks penuh di v46 (blob `41b5b585`).
KC-48 teks penuh di v47 (blob `7642b75d`).

Ringkas KC-19..KC-48 satu baris: KC-19 mencacah dari ingatan · KC-20 bias ke bawah
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
KC-47 satu peristiwa menyamar sebagai banyak pengamatan bebas · KC-48 ambang absolut
pada besaran yang sebarannya belum pernah diukur.

**KC-41 — dua kasus v46 tetap tercatat** (lampiran UKUR v5 salah mengutip `paths`
`lubang_awal.yml`; PROMPT v49 salah melabeli poros R-307 sebagai H-A017). Keduanya
sudah DIKOREKSI di UKUR v6/v7/v8 dan PROMPT v50, dan koreksinya sengaja TIDAK dihapus
— menghapus jejak cacat sama dengan menghapus buktinya. **Penangkal yang berlaku:**
rumusan pemicu, label hipotesis, dan nomor aturan WAJIB dikutip dari berkas beserta
blobnya pada giliran yang sama. Bila dua bagian STATE bertentangan, berkas SUMBER
menang, bukan yang lebih baru.

- **KC-48 [RESMI sejak v47; lahir dari R-307] — ambang absolut ditetapkan pada
  besaran yang sebarannya belum pernah diukur.** Sumber terukur: butir 2 R-307
  memakai ambang **10.000 byte**, sementara pengukuran pada run yang sama menunjukkan
  berkas TERKECIL di seluruh 19.586 simbol-bulan adalah **22.440 byte** dan
  `cacah_byte_nol` = **0**. Tidak ada satu pun data yang mungkin lolos ambang itu,
  sehingga pita 20..400 mustahil terpenuhi oleh semesta apa pun — butir itu **tidak
  pernah menguji alam**. Yang membuat kelas ini berbahaya: ia LOLOS dari praregistrasi
  yang jujur (aturan 79), dari kendali positif (aturan 50), dan dari penyebut yang
  benar (aturan 44). **Penangkal: usulan aturan 82.** Kerabat KC-20, KC-25, aturan 43.

- **KC-49 [RESMI sejak v48; lahir dari R-308; teks penuh jurnal 129 §6 dan ADR-A015
  keputusan 1] — pita praregistrasi dikunci tanpa lebih dulu menghitung implikasi
  aritmetis dari momen yang SUDAH terukur** (rata, min, maks, penyebut, nisbah
  antar kelas). Sumber terukur: butir 2 R-308 memasang pita **10..300** pada cacah
  MATI ber-byte < 150.000, sementara R-307 sudah menyerahkan tiga momen kelas MATI —
  min **97.634**, maks **451.875**, rata **413.305,781**. Rata yang duduk hanya ~8%
  di bawah maksimum berarti massa sebaran menumpuk rapat di ujung atas dan ekor
  bawahnya pasti tipis; terukur **2** (LENDUSDT 2020-11 = 97.634 dan FRONTUSDT
  2024-09 = 109.120, daftar LENGKAP). Bahan hitungannya ada di tangan ketika pita
  dikunci, dan tidak dihitung. **Kejadian kembar:** butir 1 R-307 (7,153% baris ÷ 4,3
  ≈ 1,7% byte). Dua giliran berturut dengan sebab yang sama adalah POLA, bukan
  kebetulan — itulah yang membuatnya naik menjadi kelas cacat resmi.
  **Beda dari KC-48:** KC-48 menyangkut ambang MUSTAHIL sehingga butirnya tidak
  pernah menguji alam; KC-49 menyangkut ambang yang MUNGKIN dilewati — dan memang
  dilewati dua kali — tetapi hasilnya sudah tersirat oleh ukuran sebelumnya, sehingga
  pita dipasang di tempat yang salah. **Butirnya tetap SAH dan tetap mengajarkan**
  (ia mengukur bahwa ekor bawah MATI nyaris kosong); yang keliru letak pitanya, bukan
  keberadaan ujinya. Kedua kekalahan R-307/R-308 berbeda jenis dan DILARANG
  disamakan. **Penangkal: usulan aturan 83** (tulis aritmetika implikasi di jurnal
  sebelum mengunci pita; bila jawabannya sudah tertentu dalam satu angka signifikan,
  pindahkan poros butir itu). Kerabat KC-48, KC-20, aturan 29, 43, 82.

**Calon KC-50 (BELUM RESMI, dari ADR-A015 kep. 7) — medan invarian turunan dicacah
sebagai pemeriksaan bebas.** Sumber terukur: di `irisan_byte.ringkaskan`, `total_byte`
dihitung sebagai jumlah byte keempat kelas, sehingga `selisih_total_byte` tersirat
secara aritmetis dari tiga selisih byte lainnya. Sembilan medan selisih =
**delapan pemeriksaan bebas + satu turunan**. Cacat ini diakui SEBELUM hasil keluar.
Butir 3 R-308 tetap sah; menyebut "sembilan pemeriksaan bebas" DILARANG. Belum
diresmikan karena baru satu kasus. Nomor **KC-50** dicadangkan untuknya.

## Ke bagian 2 dan 3

Berkas ini berhenti di sini dengan sengaja. Lanjutannya:

- **Papan skor R-199..R-308 (total 308: TEPAT 215 · MELESET 57 · SEPARUH 21 · TIDAK
  TERADJUDIKASI 8 · MENUNGGU 7 — MENUNGGU: R-7, R-19, R-20, R-28, R-36, R-37, R-199;
  N_percobaan = 0; ADJUDIKASI RISET TETAP TERKUNCI), catatan kejujuran, jumlah uji
  1168, utang verifikasi 24, Daftar ADR A001–A015, temuan sampingan, penomoran
  berikutnya** → `STATE_LAMPIRAN_EKOR.md` v8 (blob
  `c34c88e27dce4813622c2e3ea71bf4d486ec65d6`).
- **Penyebut 787, taksonomi, karantina, bulan ABSEN, hipotesis H-A001..H-A019, byte
  parquet semesta (32.706.262.375), lebar zona irisan byte (38 / 2, daftar LENGKAP
  keduanya), lubang funding, modul/workflow/uji, API terverifikasi (`irisan_byte` V1),
  praregistrasi R-309** → `STATE_LAMPIRAN_UKUR.md` v8 (blob
  `ff19069512bd4604b18cedb896af1d6cf6ba2557`).

Ramalan berikutnya **R-309** (poros H-A019, praregistrasi TERKUNCI di jurnal 129 §10
dan disalin apa adanya ke UKUR v8 — JANGAN DIUBAH). Jurnal berikutnya **130**, PROMPT
berikutnya **v52**, ADR berikutnya **A016**, KC berikutnya **KC-50**, aturan
berikutnya **84**, hipotesis berikutnya **H-A020**.
