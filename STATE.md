# STATE — versi 44 (bagian 1 dari tiga)

Diperbarui: 2026-07-30 (sesi 57). Aturan hanya BERTAMBAH; jangan menulis ulang dari
ingatan. v44 disusun di atas `STATE.md` v43 (blob
**`a91a49346a6ebcf1a288b936904a8fe1facc3d7a`**), `STATE_LAMPIRAN_EKOR.md` v3 (blob
**`89fec9273ab8519c21c0b2a63c958784cead6a87`**), dan `STATE_LAMPIRAN_UKUR.md` (blob
**`0e9ec3783d95be522dd4e56221fc7197f89c13c0`**) — ketiganya DIBACA UTUH sebelum
berkas ini ditulis.

## STATE SEKARANG DIPECAH TIGA — BACA INI LEBIH DULU

Pembagian yang MENGIKAT sejak v43, berlanjut di v44:

1. **`STATE.md`** (berkas ini) — **bagian 1**: kepala, aturan bernomor 1–79, kelas
   cacat KC-1..KC-44. Berkas ini berhenti sesudah kelas cacat.
2. **`STATE_LAMPIRAN_EKOR.md`** — **bagian 2**: papan skor lengkap R-199..R-304,
   catatan kejujuran, jumlah uji, utang verifikasi 24, Daftar ADR A001–A011, temuan
   sampingan, penomoran berikutnya.
3. **`STATE_LAMPIRAN_UKUR.md`** — **bagian 3**: penyebut 787, taksonomi, karantina,
   bulan ABSEN, hipotesis, lubang funding, modul/workflow/uji, API terverifikasi.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip ekor v41; bukan sumber lagi.

**Ketiga berkas wajib dibaca bersama.** LANGKAH 0 PROMPT v47 wajib menyebut
ketiganya beserta blobnya.

Yang lahir sejak v43: **KC-43**, **KC-44**, calon **KC-45**, calon **KC-46**;
**aturan 79 resmi**; adjudikasi R-301..R-304; ADR-A009, A010, A011; CI
769→814→832→879→936; delapan simbol bangkit; PROMPT v45, v46 didorong;
bentangan_kohort V2, tersisip_semesta V1, sebab_bangkit V1.

## Aturan bernomor

Aturan **1–36** berlaku tanpa perubahan; teks di STATE v19 (blob `e06c486e…`),
ringkas di v37 (blob `f520d5e2`).

Aturan **37, 39–45, 47, 49, 51, 53, 54, 56, 59–62** berlaku tanpa perubahan;
ringkas satu baris: 37 kelas cacat pada sampel · 39 keseragaman sampel bukan ramalan
· 40 uji silang baris · 41 penyebut nol → TIDAK TERADJUDIKASI · 42 kelas cacat
butuh angka terukur · 43 toleransi berskala · 44 ramalan menyebut penyebut · 45
keatomikan push pemicu · 47 satuan cacah tersurat · 49 re-export mematahkan uji ·
51 jendela mundur adaptif · 53 ramalan kode keluar butuh pembacaan perilaku · 54
cacah `def test_` satu per satu · 56 commit BERIKUTNYA yang menyentuh X · 59
ketiadaan gejala butuh penyebut · 60 mekanisme tak dipindah antarkasus · 61 medan
tak dipindah antarjalur · 62 daftar tak diminta dari laporan bercacah.

Yang berikut memuat angka atau daftar kepatuhan, jadi ditulis agak penuh:

38. Cacah uji hanya sah dari `reports/ci_terakhir.json` (run id + commit +
    `kode_keluar`). Laporan dapat TERTIMPA run berikutnya. **[v44] Ditaati empat
    kali lagi:** R-301 bentangan V2 run **30509071237** (commit `703daa90`, blob
    `24ecf836`, kode 0); CI **832** run **30509071199**; tersisip_semesta run
    **30514239872** (commit `25106dd5`, blob laporan run `6a7710e3`, kode 0); CI
    **879** run **30514239862**; PROMPT v46 CI **879** run **30514531868** (commit
    `2f240448`); sebab_bangkit run **30517682958** (commit `3913a054`, blob
    `2caf2e59`, kode 0); CI **936** run **30517682951**. Total pemakaian tercatat:
    **dua puluh delapan**.
46. Kode dilarang menyimpulkan dari penyebut nol. **[v44] Ditaati di
    `sebab_bangkit` V1:** `tersisip_sepakat` sengaja TIDAK menjadi penggugur agar
    perbedaan definisi dua alat dilaporkan, bukan dijadikan batalnya riset.
48. Berkas modul mendekati 800 baris dipecah sebelum fungsi baru ditambahkan.
    `funding.py` dan `silang_funding.py` keduanya 705 baris (SERI). **[v44]
    `sebab_bangkit.py` V1 memang lebih pendek dari batas.**
50. Setiap pengukuran yang menyimpulkan dari KETIADAAN wajib memuat kendali
    positif. **[v44] Ditaati di `sebab_bangkit` V1:** dua lapis — kendali data
    (`silang_funding.kendali_silang`, tiga simbol-bulan berparquet terbesar) DAN
    kendali detektor (dua bentangan buatan, membuktikan detektor arah waktu dapat
    memisahkan `mati_dulu` dari `lubang_dulu`).
52. Laporan yang tidak dapat dibaca utuh setara dengan laporan yang tidak ada. Ekor
    setiap berkas kode dan berkas panjang yang didorong wajib dibaca sesudah push.
    **[v44] Ditaati delapan kali lagi:** `bentangan_kohort.py` V2 (blob
    `f4eae57a`, berakhir utuh), `bentangan_kohort.yml` V2 (`13f21d1d`), jurnal 122
    dibaca ulang, `tersisip_semesta.py` V1 (blob `8a648838`, berakhir
    `raise SystemExit(main())`), `test_tersisip_semesta.py` (blob `61196fd1`, 47
    butir), `.github/workflows/tersisip_semesta.yml` (blob `abdab4af`), dan kini
    `sebab_bangkit.py` (blob `fd5a1dc4`, berakhir `raise SystemExit(main())`),
    `test_sebab_bangkit.py` (blob `3977c11c`, 57 butir). Utang yang TETAP hidup:
    `tests/test_bentangan_kohort.py` V2 (63 butir, commit `703daa90`) belum dibaca
    ulang byte demi byte.
55. Rumusan pemicu workflow wajib dikutip dari berkas workflow beserta blobnya.
    **[v44] Tiga workflow baru menambah preseden:** `bentangan_kohort.yml` V2 (blob
    `13f21d1d`), `tersisip_semesta.yml` (blob `abdab4af`), `sebab_bangkit.yml`
    (didorong commit `3913a054`) — ketiganya ber-`paths` sempit pada modulnya saja.
57. Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB ditulis bernomor
    dan nomor terakhirnya dipakai sebagai cacahan. **TERBUKTI DUA PULUH TIGA DARI
    DUA PULUH TIGA [v44]:** ... 769, 814, 832, **879**, **936** — kali ini aturan
    57 berlaku pada `test_tersisip_semesta.py` 47 butir dan `test_sebab_bangkit.py`
    57 butir. 879 + 57 = **936** ✅ Mekanismenya deterministik — dan setiap
    kemenangan wajib disebut **MUDAH**.
58. Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH DILARANG
    diramalkan dengan pita sempit.
63–76. Berlaku tanpa perubahan dari v43. Teks penuh di v43 (blob `a91a4934`).

**Aturan 77 (DIUSULKAN, belum berlaku):** dua berkas laporan berblob IDENTIK bukan
dua pengukuran. Baru satu kasus (`bulan_absen.log` == `bulan_absen_ringkas.json`).

**Aturan 78 (DIUSULKAN, belum berlaku):** batas panjang alat adalah bagian dari
DESAIN repo. Struktur berkas wajib disesuaikan dengan batas terukur — ±2,4 MB baca,
±25–45 KB tulis. Belum resmi karena batas tulis baru diketahui secara kasar.

**Aturan 79 (BERLAKU mulai v44):** praregistrasi ramalan ditulis lebih dulu di
`journal/**` (yang ada di `paths-ignore`) **sebelum** modul pengukurnya dibuat,
sehingga urutan "ramalan dulu, pengukuran kemudian" dapat ditegakkan dan tidak
mungkin disunting setelah angka terlihat. Ditaati EMPAT kali berturut:
R-300 (jurnal 119), R-302 (jurnal 121), R-303 (jurnal 122), R-304 (jurnal 124).
Pada R-301 urutan masih terbalik; pada R-302 praregistrasi sudah di jurnal.
Mulai R-305 dan seterusnya praregistrasi di jurnal adalah WAJIB.

## Kelas cacat

KC-1 s.d. KC-12 seperti v19; KC-10 dan KC-11 DITUTUP. KC-13 keterwakilan sampel.
**KC-16 DITARIK — nomornya TETAP kosong selamanya.** KC-17 DITUTUP. Teks penuh
KC-14, KC-15, KC-19..KC-29 ada di v37 (blob `f520d5e2`). KC-30..KC-42 ada di v43
(blob `a91a4934`), teks penuhnya tidak diulang di sini.

Ringkas KC-19..KC-42 satu baris: KC-19 mencacah dari ingatan · KC-20 bias ke bawah
· KC-21 ketiadaan gejala dari ketiadaan pengukuran · KC-22 mekanisme dipindah · KC-23
medan dipindah · KC-24 daftar dari laporan bercacah · KC-25 batas semesta tak
tersurat · KC-26 medan ekstrem membisu tentang seri · KC-27 karakterisasi dari
contoh berurut · KC-28 mencampur kelas instrumen · KC-29 taksonomi paralel · KC-30
nama kelas dibaca sebagai keadaan · KC-31 nama peristiwa dibaca sebagai mekanisme ·
KC-32 dua sistem penomoran dicampur · KC-33 mengenali satu peristiwa lalu berhenti
· KC-34 cacah subkelompok dari pengurangan kepala · KC-35 cakupan kode dicampur
dengan cakupan laporan · KC-36 homonim diperlakukan satu konsep · KC-37 nol dari
satu penyebut sebagai bukti di penyebut lain · KC-38 kecocokan tanpa membedakan
mekanisme · KC-39 dua penyebut bulan absen dicampur · KC-40 daftar klausa gagal
dibaca sebagai keadaan · KC-41 pemicu workflow dirumuskan dari ingatan · KC-42
menulis ulang berkas melampaui batas push.

- **KC-43 [v44, lahir dari giliran R-302] — memakai tanda tangan fungsi dari
  INGATAN alih-alih membacanya dari kode.** Pada giliran R-302 pertama, tanda tangan
  `silang_funding.baca_laporan_kehidupan` dikutip dari ingatan, bukan dari berkas.
  Hasilnya: parameter yang dioper salah dan modus kegagalan yang tidak terduga.
  **Penangkal:** sebelum modul baru yang MENGIMPOR modul lain ditulis, berkas modul
  yang diimpor WAJIB dibaca UTUH pada giliran yang sama — termasuk docstring dan
  nilai balik setiap fungsi yang akan dipanggil. Tanda tangan tidak boleh
  dikutip dari STATE atau PROMPT; hanya kode yang berlaku sebagai kebenaran. Kerabat
  KC-19 (dari ingatan) dan KC-73 (meramal dari nama). Penangkal 71 (baca modul
  sebelum meramalkan laporan) diperluas ke: baca modul sebelum MENGGUNAKANNYA.
- **KC-44 [v44, lahir dari giliran R-302] — workflow mendorong semua laporan dalam
  SATU commit sehingga laporan berikutnya menimpa laporan sebelumnya tanpa jejak.**
  Pada `anatomi_tengah.yml` (blob `49c452a2`) seluruh laporan di-commit bersama;
  bila run gagal di tengah, berkas yang sudah terbuka tertimpa oleh run berikutnya.
  Preseden baru: `tersisip_semesta.yml` dan `sebab_bangkit.yml` masing-masing
  men-commit `<nama>.json`, `<nama>.log`, dan `<nama>_status.json`
  **sendiri-sendiri** dengan retry `git pull --rebase`, sehingga setiap berkas
  punya commit sendiri dan `list_commits` dapat menemukannya. **Penangkal:** setiap
  workflow yang menghasilkan lebih dari satu berkas laporan WAJIB men-commit tiap
  berkas dalam langkah terpisah dengan pesan commit yang berbeda. Commit bersama
  hanya boleh bila laporan itu satu berkas tunggal.

**Calon KC-45 (DIUSULKAN, belum berlaku):** satuan "bulan tanpa funding" dan "bulan
MATI" dicampur dalam satu klaim kausal. Sumber: H-A015 dulu mencatat angka ICPUSDT
19 bulan dan TLMUSDT 20 bulan sebagai "bulan MATI" padahal satuannya "bulan TANPA
FUNDING". Salah baca itu menghasilkan tafsir arah sebab yang salah arah di ADR-A009
dan berlanjut ke ramalan R-304 yang MELESET. **Penangkal: setiap angka bulan yang
menyangkut kematian pasar WAJIB menyebut satuannya tersurat di tempat ia ditulis.**
Baru satu kasus terdokumentasi; menunggu konfirmasi pola sebelum jadi aturan resmi.

**Calon KC-46 (DIUSULKAN, belum berlaku):** lubang funding yang berada di BULAN
PERTAMA riwayat sebuah simbol dibaca sebagai "funding berhenti". Sumber: ICPUSDT
(bulan pertama 2021-05 = bulan berlubang pertama, selisih −14) dan TLMUSDT (bulan
pertama 2021-07 = bulan berlubang pertama, selisih −12) keduanya berlubang tepat
sejak bulan pertama — bukan karena funding berhenti, melainkan karena funding BELUM
MULAI. **Penangkal: setiap tafsir arah waktu wajib memeriksa bentuk lubang
(`bentuk_lubang_lokal`) lebih dulu; lubang bentuk AWAL DILARANG dibaca sebagai
"berhenti".** Kerabat KC-36 (homonim) dan KC-40 (nama yang bermakna terbalik).
Baru satu kasus; menunggu konfirmasi pola.

## Ke bagian 2 dan 3

Berkas ini berhenti di sini dengan sengaja. Lanjutannya:

- **Papan skor R-199..R-304 (total 304), catatan kejujuran, jumlah uji 936, utang
  verifikasi 24, Daftar ADR A001–A011, temuan sampingan, penomoran berikutnya** →
  `STATE_LAMPIRAN_EKOR.md`.
- **Penyebut 787, taksonomi, karantina, bulan ABSEN, hipotesis H-A001..H-A017,
  lubang funding, modul/workflow/uji, API terverifikasi** →
  `STATE_LAMPIRAN_UKUR.md`.
