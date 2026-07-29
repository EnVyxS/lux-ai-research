# STATE — versi 43 (bagian 1 dari tiga)

Diperbarui: 2026-07-30 (sesi 56, lanjutan). Aturan hanya BERTAMBAH; jangan menulis
ulang dari ingatan. v43 disusun di atas teks **v42 yang dibaca UTUH dari `main`**
(blob **`e29aeb9c32b7fb8499f82e63000096f92d2582d9`**), `STATE_LAMPIRAN_EKOR.md`
(blob **`7480cedd1f9b4bbe1b9d091ac9f8a6c59c95c139`**, UTUH), dan
`STATE_LAMPIRAN_UKUR.md` (blob **`0e9ec3783d95be522dd4e56221fc7197f89c13c0`**,
UTUH).

## STATE SEKARANG DIPECAH TIGA — BACA INI LEBIH DULU

**Sebabnya, terukur.** Dua push `STATE.md` berturut TERPOTONG di tengah kalimat:
v41 berhenti di "Utang verifikasi" butir 24 ("… kini cacahnya diketahui,"), dan
v42 berhenti di tengah tabel papan skor pada baris **R-287** ("… **TEPAT** (MUDAH,
run "). Alat tidak menggerutu sama sekali — `push_files` mengembalikan commit baru
dengan gembira atas muatan yang cacat. Berkas ini sudah melampaui **batas panjang
satu push**, dan tidak ada API tambal. Mengulangi cara yang sama untuk ketiga kali
adalah kekeliruan yang sudah dikenali, jadi STATE dipecah — sebagaimana repo ini
sudah punya presedennya (`STATE_LAMPIRAN.md`, `STATE_LAMPIRAN_ANGKA.md`).

**Pembagian yang MENGIKAT sejak v43:**

1. **`STATE.md`** (berkas ini) — **bagian 1**: kepala, aturan bernomor 1–76, kelas
   cacat KC-1..KC-42. Berkas ini berhenti sesudah kelas cacat; ia TIDAK memuat
   papan skor maupun tabel pengukuran.
2. **`STATE_LAMPIRAN_EKOR.md`** — **bagian 2**: papan skor lengkap R-199..R-296,
   catatan kejujuran, jumlah uji, utang verifikasi 24, Daftar ADR A001–A008, temuan
   sampingan, penomoran berikutnya.
3. **`STATE_LAMPIRAN_UKUR.md`** — **bagian 3**: penyebut 787, taksonomi sembilan
   kelas, daftar dua belas karantina, bulan ABSEN, H-A015, lubang funding 880/877,
   terhenti per jenis, lima belas pasangan SETTLED, penyebut per tahun, cacah baris,
   daftar modul/workflow/uji, API terverifikasi, dan seluruh hipotesis.
4. `STATE_LAMPIRAN_ADR.md` (blob `a02ef271`) — arsip ekor v41; isinya sudah diserap
   ke bagian 2 dan **bukan sumber lagi**.

**Ketiga berkas wajib dibaca bersama.** Membaca hanya `STATE.md` memberi aturan
tanpa angka; membaca hanya lampiran memberi angka tanpa aturan. LANGKAH 0 PROMPT
v44 wajib menyebut ketiganya beserta blobnya.

**Kekeliruan itu milik penulis, bukan data.** Tidak satu pun angka riset berubah
karena pemotongan; aturan 52-lah yang menangkap keduanya sebelum ada angka yang
dipakai. Papan skor terakhir: **296** (lihat bagian 2).

Yang lahir sejak v42: **KC-42**, calon aturan 78, pemecahan STATE, adjudikasi R-295
dan R-296, serta praregistrasi **R-297** di bawah.

**Praregistrasi R-297 (ditulis SEBELUM push ini menyalakan `ci.yml`).** Push
`STATE.md` menyalakan CI (`paths-ignore` tidak memuat akar repo — KC-41). Tidak
satu pun berkas `tests/**` berubah, jadi cacah tetap **722** dan `kode_keluar`
**0**. Ramalan ini **MUDAH** (aturan 57).

Berkas yang TIDAK dibaca ulang pada giliran ini dan karena itu tidak diubah
angkanya: `lux_ai/serapan/lubang_tengah.py` (blob `4d3beaf1`),
`decisions/ADR-A002.md`, `ADR-A004.md`, `ADR-A006.md`, `ADR-A007.md`,
`ADR-A008.md`, `PETA_MODUL.md`, `lux_ai/semesta/taksonomi.py` (blob `b418c7ba`),
`.github/workflows/karantina_semesta.yml` (didorong, belum dibaca ulang).

## Aturan bernomor

Aturan **1–36** berlaku tanpa perubahan; teks di STATE v19 (blob `e06c486e…`),
ringkas nomornya di v37 (blob `f520d5e2`).

Aturan **37, 39–45, 47, 49, 51, 53, 54, 56, 59–62** berlaku tanpa perubahan dan
teks penuhnya ada di v37 (blob `f520d5e2`). Ringkas satu baris: 37 kelas cacat
pada sampel · 39 keseragaman sampel bukan ramalan · 40 uji silang baris ·
41 penyebut nol → TIDAK TERADJUDIKASI · 42 kelas cacat butuh angka terukur ·
43 toleransi berskala · 44 ramalan menyebut penyebut · 45 keatomikan push pemicu ·
47 satuan cacah tersurat · 49 re-export tetap mematahkan uji · 51 jendela mundur
adaptif · 53 ramalan kode keluar butuh pembacaan perilaku · 54 cacah `def test_`
satu per satu · 56 "commit BERIKUTNYA yang menyentuh X" · 59 ketiadaan gejala
butuh penyebut · 60 mekanisme tak dipindah antarkasus · 61 medan tak dipindah
antarjalur · 62 daftar tak diminta dari laporan bercacah.

Yang berikut memuat angka atau daftar kepatuhan, jadi ditulis agak penuh:

38. Cacah uji hanya sah dari `reports/ci_terakhir.json` (run id + commit +
    `kode_keluar`). Laporan dapat TERTIMPA run berikutnya; temukan ref runner
    lewat `list_commits` dengan `path="reports/<berkas>.json"`. **[v41] Ditaati
    empat kali lagi**: R-292 pada ref `aabd2019` (run 30478069419); R-293 pada
    `936d7901` (run 30479093362); R-291 pada **`d9e44119`** (run 30479681799);
    R-294 pada **`e82919f5`** (run 30479681620). **[v42] Ditaati sekali lagi atas
    run yang TIDAK dipraregistrasi** (run **30481231522**, commit `ea2a07e7`, ref
    `b7c030a8`, blob `1b10bd19`, 722, kode 0) — pengukurannya sah, tetapi karena
    tak ada ramalan sebelumnya ia DILARANG dihitung sebagai kemenangan.
    **[v43] Ditaati tiga kali lagi, dan kali ini `list_commits` benar-benar
    diperlukan:** R-295 pada ref `117d8c67` (run **30482205512**, commit
    `35b3d6d8`, blob `a605c94a`, 722, kode 0); run **30482387663** (commit
    `117d8c67`, blob `12083485`) yang TIDAK dipraregistrasi — pengukuran saja; dan
    R-296 pada ref **`ecdaacdb`** (run **30482864644**, commit `58a2f09c`, blob
    `a467ab62`, 722, kode 0), yang hanya ditemukan setelah `list_commits`
    menunjukkan bahwa `main` sudah bergerak dua laporan ke depan. Total pemakaian
    tercatat: **dua puluh dua**. Perangkap ini menyala berulang: sesudah push,
    laporan di `main` sudah memuat commit run BERIKUTNYA.
46. Kode dilarang menyimpulkan dari penyebut nol; medan yang menyimpulkan wajib
    memeriksa lebih dulu apakah kasusnya mampu membedakan. Ditaati `terhenti`
    V2/V4, `silang_settled` V1, `bulan_absen` V1, dan **[v41]
    `karantina_semesta` V1** (`nisbah_lilin` dan `selisih_menit` bernilai **null**
    bila bulannya tak terbaca, bukan nol; `bulan_menit` mengembalikan 0 hanya
    sebagai penanda TAK TERUKUR dan itu disebut tersurat di docstringnya,
    aturan 74).
48. Berkas modul yang mendekati pagar 800 baris dipecah SEBELUM fungsi baru
    ditambahkan. Berlaku atas `funding.py` dan `silang_funding.py` (705 SERI).
    **RENCANANYA DITINJAU [v39], DIPERKUAT [v40, v41]:** preseden MENGIMPOR kini
    empat kali — `lubang_tengah.py`, `silang_settled.py`, `bulan_absen.py`, dan
    **`karantina_semesta.py`** (mengimpor `pulihkan` untuk `nama_manifes` dan
    `TOTAL_PECAHAN`) memakai fungsi modul lain tanpa menyalinnya, sehingga definisi
    tetap SATU (aturan 36). Pemecahan hanya boleh dijalankan bila ada alasan yang
    mengalahkan preseden ini. **[v43] Prinsip yang sama kini terbukti berlaku atas
    berkas CATATAN, bukan hanya kode:** `STATE.md` dipecah tiga karena melampaui
    batas alat tulis, dan pemecahannya memakai penunjuk silang berblob — padanan
    "mengimpor", bukan "menyalin".
50. Setiap pengukuran yang menyimpulkan dari KETIADAAN wajib memuat kendali
    positif. `terhenti` V2..V4 `kendali_sah` true; `silang_settled` V1 true;
    `bulan_absen` V1 true; **[v41] `karantina_semesta` V1 true** — BTCUSDT dan
    ETHUSDT masing-masing **0** kemunculan di daftar karantina, sesuai dengan 78
    bulan lolos tanpa absen yang diukur `bulan_absen`.
52. Laporan yang tidak dapat dibaca utuh setara dengan laporan yang tidak ada.
    Ekor SETIAP berkas kode dan berkas panjang yang didorong wajib dibaca sesudah
    push. **[v41] Ditaati atas jurnal 116, `karantina_semesta.py`,
    `tests/test_karantina_semesta.py`, `.github/workflows/bulan_absen.yml`
    (utang v40 LUNAS), dan STATE v40.** **[v42] DAN AKHIRNYA TERBUKTI PERLU:**
    pembacaan ulang `STATE.md` v41 menemukan bahwa push-nya TERPOTONG di tengah
    kalimat. **[v43] Terbukti perlu untuk KEDUA kali, dan inilah aturan yang
    menyelamatkan riset dari kehilangan naskah aturannya sendiri:** pembacaan
    ulang v42 (blob `e29aeb9c`) menemukan pemotongan kedua di baris R-287,
    sekaligus memulihkan naskah aturan 1–76 dan KC-1..KC-41 yang HANYA hidup di
    badan berkas itu — menulis v43 dari ingatan akan memusnahkannya (KC-19).
    Ditaati juga atas `STATE_LAMPIRAN_EKOR.md` (blob `7480cedd`) dan
    `STATE_LAMPIRAN_UKUR.md` (blob `0e9ec378`), keduanya UTUH.
    **Turunan yang kini mengikat: berkas yang didorong dalam potongan yang sangat
    panjang wajib dibaca ulang SEBELUM berkas lain disusun di atasnya; pemotongan
    wajib ditutup di versi berikutnya, bukan disunting diam-diam (aturan 29); dan
    berkas yang terpotong DUA KALI wajib DIPECAH, bukan didorong ulang (KC-42).**
    Yang tetap tak terbaca utuh: `reports/silang_funding.json` 183.963 B,
    `reports/bulan_absen.json` 249.992 B, dan `reports/manifes_pecahan_2.json`
    2.446.093 B (blob `c0be6ecf1204145f80eec34c4856a6c5363445a8`) yang **DITOLAK
    alat baca agen** — ketiganya dianggap TIDAK ADA; yang berlaku adalah berkas
    ringkasnya atau modul yang membacanya di runner.
55. Sebelum meramalkan hasil workflow, baca `paths`/`paths-ignore` dan sebutkan
    workflow MANA yang menyala. **[v42] DIKOREKSI DARI KODE, bukan dari ingatan
    (`ci.yml` blob `c79497b2`, dibaca UTUH).** Bunyi warisan "push ke `STATE.md`,
    `PROMPT_KELANJUTAN.md`, `lux_ai/**`, `tests/**` menyalakan `ci.yml`" **SALAH
    BENTUK**: `ci.yml` tidak memakai `paths` sama sekali, ia memakai
    **`paths-ignore`** atas `journal/**`, `decisions/**`, `hipotesis/**`,
    `reports/**`. Yang benar: **SETIAP push apa pun di luar keempat direktori itu
    menyalakan CI** — termasuk `README.md`, `requirements.txt`, `PETA_MODUL*.md`,
    `STATE_LAMPIRAN*.md`, dan `.github/workflows/**`. **[v43] Akibatnya kini
    terukur tiga kali:** push `STATE_LAMPIRAN_ADR.md` (run 30481231522), push
    `STATE_LAMPIRAN_EKOR.md` (run 30482387663), dan push `STATE_LAMPIRAN_UKUR.md`
    (run 30482864644) semuanya menyalakan CI — dua yang pertama tanpa
    praregistrasi, yang ketiga sudah dipraregistrasi di dalam berkas yang
    mendorongnya (R-296, TEPAT). Karena laporan CI ditulis ke `reports/**` yang
    ADA di `paths-ignore`, run tidak melahirkan run — tidak ada rantai tak
    berujung. `ci.yml` **juga mendeklarasikan `workflow_dispatch`**, dan memasang
    `concurrency: ci-${{ github.ref }}` dengan **`cancel-in-progress: false`** —
    run mengantre dan tidak saling membatalkan, sehingga penulisan
    `reports/ci_terakhir.json` diserialkan oleh GitHub, bukan oleh disiplin
    peramal. Workflow lain tetap ber-`paths` sempit: `ukur_baris.yml` hanya atas
    `lux_ai/serapan/ukur_baris.py`; `semesta_kuota.yml` hanya atas
    `lux_ai/serapan/semesta_kuota.py`; `terhenti_semesta.yml` hanya atas
    `lux_ai/semesta/terhenti.py` dan dirinya sendiri; `silang_settled.yml` hanya
    atas `lux_ai/serapan/silang_settled.py`; `bulan_absen.yml` hanya atas
    `lux_ai/serapan/bulan_absen.py` — dan ia MENDEKLARASIKAN `workflow_dispatch`.
    **KOREKSI BATASAN WARISAN [v41, dikuatkan v42]:** bunyi "tidak ada
    `workflow_dispatch` di repo" TIDAK tepat — sedikitnya DUA workflow
    mendeklarasikannya; yang benar adalah **tidak ada alat di sisi agen untuk
    memicunya**, sehingga satu-satunya cara menyalakan run tetap push.
57. Sebelum meramalkan cacah butir uji, nama tiap `def test_` WAJIB ditulis
    BERNOMOR dan nomor terakhirnya dipakai sebagai cacahan. **TERBUKTI BEKERJA
    SEMBILAN BELAS DARI SEMBILAN BELAS [v43]:** 382, 396, 450, 494, 526, 552, 584,
    598, 610, 623, 630, 630, 638, 662, 662, 662, 694, 694, 694, **722** — dan 722
    kini terukur lima kali berturut (run 30479681620, 30481231522, 30482205512,
    30482387663, 30482864644). Mekanismenya deterministik — itu sebab
    keberhasilannya, bukan kecakapan meramal, dan setiap kemenangannya wajib
    disebut **MUDAH**.
58. Cacah baris berkas yang versi terkininya belum dibaca ulang UTUH dalam
    giliran yang sama DILARANG diramalkan dengan pita sempit. Pilih: (a) baca
    ulang utuh; (b) pita batas atas ≥1,8× batas bawah; (c) jangan meramal, ukur.
63. **[DIAMANDEMEN v37, DIPERKUAT v38]** Setiap klaim tentang kematian,
    kebangkitan, lubang funding, dan `bagian_mati` WAJIB menyebut batas
    semestanya secara tersurat: penyebut **787** simbol adalah `perpetual_usdt`,
    dan ia PERSIS seluruh perpetual USDT di arsip. Semesta arsip **937** simbol,
    **21.789** bulan; **150** hanya-arsip; **0** hanya-penyebut. Frasa lama
    "hampir seluruhnya BUSD/USDC" **DICABUT** (terukur 80 dari 147). Pada bulan
    tutup semesta **49 nama di luar penyebut masih terbit**. Penyebut 787
    terkonfirmasi dari arah ketiga oleh `bulan_absen` V1
    (`cacah_nama_penyebut` **787**, `selisih_nama_penyebut` **0**).
64. Ramalan tentang nilai EKSTREM wajib menyebut perlakuan atas SERI, dan medan
    yang menamai pemegang ekstrem wajib melaporkan SELURUH pemegangnya bila seri.
    Perbaikan wajib di `ukur_baris` **V6**; `semesta_kuota` sudah benar sejak V1.
65. Setiap daftar contoh WAJIB menyebut CARA pemilihannya, dan kalimat sifat
    tentang KESELURUHAN himpunan DILARANG disusun dari contoh yang bukan
    seluruhnya. Contoh yang benar: sampel `diagnosa_kc15` berlapis atas delapan
    pecahan. **[v41] Contoh ketiga:** dua belas baris `karantina_semesta` adalah
    SELURUH isi daftar karantina kedelapan manifes, dan modul melaporkan
    `daftar_terpotong` 0 untuk membuktikannya.
66. **[lahir salah lalu DIREVISI]** Setiap cacahan semesta wajib menyebut KELAS
    INSTRUMEN yang dicacah. **Sebelum menuduh sebuah batas tidak ada, berkas
    penyaringnya WAJIB dibaca lebih dulu.** Perluasan: sebelum menulis modul baru,
    LISTING direktori paket dan direktori workflow lebih dulu. **[v41] Ditaati
    lagi:** listing sebelum `karantina_semesta` mencatat `lux_ai/serapan/` **38**,
    `.github/workflows/` **32**, dan `tests/` **41**; sesudah push menjadi **39**,
    **33**, dan **42**. **[v42] Kerabatnya kini terbukti berlaku atas WORKFLOW
    juga:** sebelum menyatakan workflow mana yang menyala, berkas workflow-nya
    wajib dibaca — lihat KC-41.
67. **[v38] Keanggotaan semesta dan keberlangsungan hidup adalah DUA SUMBU; satu
    DILARANG disimpulkan dari yang lain.** Terukur pada bulan tutup 2026-06: dari
    937 nama arsip **808 masih terbit** dan **129 terhenti**; dari 787 nama
    penyebut **759 masih terbit** dan **28 terhenti**; **49** nama yang masih
    terbit berada DI LUAR penyebut. Angka **28** DILARANG dicampur dengan **1.401**
    MATI, **98** SEPI, atau `cacah_simbol_tanpa_hidup` **18**. Lihat KC-30.
68. **[v38] Nama turunan dan nama asal dapat terbit BERSAMAAN.** Kehadiran nama
    turunan (`SETTLED`) DILARANG dibaca sebagai berhentinya nama asal; bulan
    terakhir keduanya wajib dilaporkan BERPASANGAN. Dari 15 nama SETTLED hanya
    **dua** yang nama dasarnya berhenti terbit (`SXPUSDT` 2026-05, `BDXNUSDT`
    2026-03). Lihat KC-31.
69. **[v39, jurnal 107] Setiap nama turunan wajib disebut bersama nama asalnya,
    dan setiap kelompok nama wajib punya pemeriksaan silang ke pengukuran lain atas
    besaran yang sama.** Terbayar tiga kali: 36 kolom bulan tabel 15 pasangan =
    `bulan_settled.py` V1; 11 bulan absen + 1 tepi = 12 = 19.598 − 19.586; dan
    **[v41] `byte_parquet_karantina_semesta` 13.247.705 = angka KC-17 di
    `pecahan.py` VERSI 6 (`selisih_byte_tercatat` 0), serta
    `pecahan_tanpa_karantina` [2, 5] persis seperti tersurat di sana.** **[v42]
    Terbayar keempat kali, kecil tetapi sah:** `ci_terakhir.json` mencatat "722
    tests collected" sedangkan `ci_terakhir.txt` mencatat "722 passed" — dua
    keluaran pytest yang berbeda (collect-only lawan eksekusi) pada satu run, dan
    keduanya 722. **Pengukuran yang tak dapat dicocokkan dengan pengukuran lain
    mana pun harus dianggap belum diuji.**
70. **[v39, jurnal 108, lahir dari R-281] Sebelum praregistrasi dikunci, setiap
    butir yang saling menentukan wajib dijumlahkan silang; praregistrasi yang tidak
    konsisten dengan dirinya sendiri adalah ramalan CACAT, dan kecacatannya milik
    peramal, bukan milik data.** Lihat KC-34.
71. **[v39, jurnal 109, lahir dari R-282] Sebelum mempraregistrasi ramalan atas
    laporan yang belum pernah dibaca, modul penghasilnya wajib dibaca lebih dulu.**
    Ramalan atas medan yang tidak pernah diukur laporan itu gugur otomatis dan
    tidak boleh dihitung sebagai kekalahan data. **[v41] Dipakai dengan benar dua
    kali:** `serap.py`, `pecahan.py`, `pulihkan.py`, `rilis.py` dibaca UTUH sebelum
    `karantina_semesta` ditulis, sehingga nama medan `daftar_karantina`,
    `parquet_karantina`, `cacah_karantina`, `daftar_terpotong` dikutip dari kode
    yang menulisnya; dan `gerbang_1m.py` dibaca sebelum arti `pelanggaran`
    ditafsirkan (KC-40).
72. **[v39, jurnal 110] Sebuah laporan hanya membuktikan apa yang benar-benar
    disampelnya.** Setiap adjudikasi wajib menyebut penyebut sampel laporan sebelum
    menyebut putusannya. **Turunan yang mengikat:** angka terbitan wajib disebut
    bersama penyebutnya — 880 lubang funding (seluruhnya) lawan 877 (di dalam
    19.586). **[v41] Ditaati oleh rancangan `karantina_semesta`:** `kode_keluar`
    sengaja TIDAK memeriksa `uji_r291`, `selisih_penyebut`, maupun
    `selisih_byte_tercatat` — ramalan yang kalah tidak boleh membatalkan laporannya
    sendiri (preseden `bulan_absen`, aturan 24). **[v42] `ci.yml` menaati prinsip
    yang sama tanpa direncanakan:** laporan ditulis dan di-commit LEBIH DULU, baru
    `exit ${kode}` dijalankan, sehingga suite yang gagal pun tetap meninggalkan
    pengukurannya.
73. **[v39, jurnal 111, lahir dari R-284] Dilarang mempraregistrasi ramalan atas
    ISI sebuah berkas yang belum pernah dibaca ketika satu-satunya dasar ramalan
    adalah NAMA berkas itu.** Bila sebuah berkas perlu diketahui, bacalah —
    pembacaan tidak butuh run, tidak butuh jaringan, dan tidak berbiaya.
    **[v41] Batasnya kini diketahui:** ada berkas yang TIDAK DAPAT dibaca agen
    (manifes pecahan 2,4 MB). Untuk berkas seperti itu, jalan sahnya adalah modul
    yang berjalan di runner, bukan dugaan dari nama. **[v42] Kerabat terdekatnya
    memakan saya sendiri: `ci.yml` sudah ada sejak awal riset dan tetap tidak
    pernah dibaca, sementara `paths`-nya saya kutip dari ingatan (KC-41).**
74. **[v39, jurnal 112, lahir dari R-285] Setiap nol yang dipakai sebagai dasar
    ramalan wajib disebut bersama PENYEBUT dan DEFINISI ujinya.** Lihat KC-37.
    **[v41] Dipakai dengan benar:** nol `cacah_kunci_ganda`, nol `cacah_dibuang`,
    nol `cacah_ditambal`, dan nol kemunculan kendali BTCUSDT/ETHUSDT disebut
    bersama penyebutnya masing-masing (8 manifes, 12 baris).
75. **[v39, jurnal 113, lahir dari R-286] Setiap cacahan "cocok" wajib disertai
    medan pembeda MEKANISME, dan pita ramalan wajib menyebut mekanisme mana yang
    dihitung.** Lihat KC-38. Ditaati `bulan_absen` V1 lewat `pembeda_absen`
    (gagal_gerbang 11 lawan tak_diterbitkan_arsip 0).
76. **[v40, jurnal 115, lahir dari R-288] Setiap cacah "bulan yang hilang" wajib
    menyebut apakah penyebutnya RENTANG bulan LOLOS atau DAFTAR bulan DIDAFTAR
    arsip (`bulan_didaftar`), dan angka dari kedua penyebut itu DILARANG
    dijumlahkan atau dipertukarkan.** Kasus asalnya: BNXUSDT punya **3** bulan
    gagal gerbang tetapi hanya **2** bulan absen. **[v41] Penyebut KETIGA kini
    terukur dan wajib ikut dibedakan:** menit hilang dapat dihitung atas **rentang
    yang ADA di berkas** (`gerbang_1m.menit_hilang_dalam_rentang`) atau atas
    **panjang bulan KALENDER** (`karantina_semesta.selisih_menit`). Untuk BNXUSDT
    2022-04 keduanya berbeda tepat **210** menit — menit tepi peluncuran. Kedua
    angka benar; penyebutnya berbeda. Lihat KC-39 dan KC-40.

**Calon aturan 77 (DIUSULKAN, belum berlaku):** dua berkas laporan yang berblob
IDENTIK bukan dua pengukuran. Asalnya jurnal 115/116: `reports/bulan_absen.log`
dan `reports/bulan_absen_ringkas.json` berblob sama
(`e450d9f95e9bca0dc28a0e01c6aad6594c4fa3d6`) karena workflow men-`tee` stdout
modul. Belum dijadikan aturan bernomor karena baru satu kasus. **[v42] Sisi
sebaliknya kini punya contoh yang menyehatkan:** `ci_terakhir.json` dan
`ci_terakhir.txt` berblob BERBEDA (`1b10bd19` lawan `0f8626bc`) dan memang berisi
dua keluaran pytest yang berbeda — jadi ujinya bukan "nama berbeda" melainkan
**blob berbeda DAN asal perintah berbeda**.

**Calon aturan 78 (DIUSULKAN [v43], belum berlaku):** batas panjang alat adalah
bagian dari DESAIN repo, bukan kecelakaan. Struktur berkas wajib disesuaikan
dengan batas alat yang TERUKUR — ±2,4 MB sebagai batas baca (manifes pecahan 2
DITOLAK) dan sekitar satu berkas STATE penuh sebagai batas tulis (dua pemotongan
berturut). Belum dijadikan aturan bernomor karena batas tulisnya baru terukur
secara kasar: yang diketahui hanyalah bahwa ±45 KB berhasil dan STATE penuh
gagal dua kali; angka pastinya belum diukur.

## Kelas cacat

KC-1 s.d. KC-12 seperti v19; KC-10 dan KC-11 DITUTUP. KC-13 keterwakilan sampel
(penangkal aturan 37). **KC-16 DITARIK — nomornya TETAP kosong selamanya.**
KC-17 DITUTUP. Teks penuh KC-14, KC-15, KC-19–KC-29 ada di v37 (blob `f520d5e2`);
yang wajib dibawa:

- **KC-14** — menit hilang NYATA di arsip 1m: **9** simbol-bulan, **6.375** menit
  (425×15). Sebab tak diketahui (H-A004 tak dapat diuji). Karantina (ADR-A006).
- **KC-15 [DIKOREKSI v39, DILENGKAPI v41]** — klines BULANAN kehilangan HARI UTC
  penuh: **3** simbol-bulan, semuanya BNXUSDT 2022 (**2022-04, 2022-06, 2022-08**),
  **7.200** menit = **5 hari UTC**. **Hari-hari itu UTUH di arsip HARIAN** —
  jurnal 109 §5.2 DICABUT. Yang benar-benar tak terjelaskan hanyalah **210 menit
  TEPI** pada 2022-04, konsisten dengan peluncuran pukul **03:30 UTC**
  (`stempel_pertama_ms` 1648783800000; berkas harian 2022-04-01 memuat 1.230 =
  1.440 − 210 baris; `menit_tepi_hadir` 0 dari 210). **PEMBAGIAN 5 HARI KE TIGA
  BULAN TERUKUR** (`karantina_semesta` V1, penyebut kalender):

  | bulan | baris | menit kalender | selisih | keterangan |
  |---|---:|---:|---:|---|
  | 2022-04 | 41.550 | 43.200 | **1.650** | 1.440 tengah + 210 tepi |
  | 2022-06 | 41.760 | 43.200 | **1.440** | 1 hari UTC |
  | 2022-08 | 40.320 | 44.640 | **4.320** | 3 hari UTC |

  1.650 + 1.440 + 4.320 = **7.410**; 7.410 − 210 = **7.200** = 5 × 1.440 ✅ Jadi
  lima hari itu terbagi **1 + 3 + 1**, dan 210 menit sisanya adalah TEPI, bukan
  celah. Dua modul berkode berbeda kini sepakat pada satu angka (aturan 69).
  Anatomi 2022-04 selebihnya tetap: `menit_hilang_di_tengah` **1.440**,
  `gerbang_lolos` **false**, `putusan` TEPI_TAK_TERJELASKAN, `checksum_bulanan`
  `14bd6937…`. 9 + 3 = **12** karantina; 6.375 + 7.200 = **13.575** menit;
  **516.135** baris. Kedua belas karantina BERNAMA dan TERUKUR — lihat bagian 3.
  **TANGGAL** hari-hari yang hilang masih belum diukur. Kebijakan ADR-A007 masih
  DIUSULKAN.
- **KC-18** — lilin datar lolos gerbang struktural; gerbang menilai BENTUK, bukan
  kehidupan. Semesta `perpetual_usdt` atas **19.586** simbol-bulan lolos: **1.401
  MATI** (7,153%), **98 SEPI** (0,500%), **18.087 HIDUP** (92,35%); 945 MATI di
  luar kohort puncak. Dari 1.401 MATI, **842** kehilangan funding dan **559**
  tetap berfunding. **Kematian dapat berbalik** — LITUSDT MATI 2025-02..2025-11
  lalu **HIDUP 2026-01..2026-06 terukur**. Kematian permanen tetap punya contoh
  telak: BTCSTUSDT 53 dari 53 MATI. **Kecocokan bulan membuktikan PENAMAAN
  kontrak, bukan perdagangan** — mengikat atas H-A013, H-A014, H-A015, H-A016, dan
  seluruh laporan `silang_settled`, `bulan_absen`, maupun `karantina_semesta`.
  ADR-A008 Keputusan 1–6 DITERIMA; Keputusan 7 DITANGGUHKAN.
- **KC-19** mencacah dari ingatan (aturan 57). **KC-20** taksiran baris bias ke
  BAWAH (58). **KC-21** ketiadaan gejala dari ketiadaan pengukuran (59). **KC-22**
  memindahkan MEKANISME (60). **KC-23** memindahkan MEDAN (61). **KC-24** bertanya
  DAFTAR kepada laporan bercacah (62). **KC-25** batas semesta tak tersurat (63).
  **KC-26** medan ekstrem membisu tentang SERI (64). **KC-27** mengarakterisasi
  himpunan dari contoh BERURUT (65). **KC-28** mencampur kelas instrumen — berlaku
  atas arsip **937**, BUKAN atas penyebut 787 (66). **KC-29** taksonomi PARALEL
  (lubang aturan 22).
- **KC-30** — membaca NAMA KELAS sebagai KEADAAN. Penangkal 67.
- **KC-31** — membaca nama PERISTIWA sebagai MEKANISMENYA. Penangkal 68.
- **KC-32** — mencampur DUA SISTEM PENOMORAN (utang verifikasi nomor 28 lawan
  **ramalan R-28**). **R-28 tetap MENUNGGU**; bunyinya ada di STATE v23 dan belum
  dibaca. Teks jurnal 105 TIDAK disunting (aturan 29).
- **KC-33 [v39] — mengenali satu peristiwa lalu berhenti mencari yang kedua.**
  `SXPUSDTSETTLED` disebut satu-satunya peristiwa penamaan; **`BDXNUSDT`** adalah
  yang kedua dan sudah SELESAI. Pencarian pola WAJIB atas seluruh rentang.
- **KC-34 [v39] — menurunkan cacah subkelompok dengan pengurangan di kepala** lalu
  memakainya tanpa mencocokkannya ke jumlah yang sudah dipegang. Penangkal 70.
- **KC-35 [v39, DIPERSEMPIT] — menyamakan CAKUPAN kode cacat dengan CAKUPAN satu
  laporan yang namanya memuat kode itu.** Penangkal aturan 72.
- **KC-36 [v39] — homonim di dalam kosakata riset sendiri diperlakukan sebagai satu
  konsep** ("tengah", "lubang"). Penangkal aturan 73. `bulan_absen.py` menuliskan
  pembedaan itu tersurat: lubang funding dan lubang tengah ADA di penyebut, bulan
  ABSEN TIDAK ADA di penyebut.
- **KC-37 [v39] — memakai nol dari satu penyebut sebagai bukti ketiadaan gejala di
  penyebut lain.** Penangkal aturan 74.
- **KC-38 [v39] — mencacah "kecocokan" tanpa membedakan MEKANISMENYA.** Penangkal
  aturan 75.
- **KC-39 [v40, lahir dari R-288] — mencampur dua penyebut "bulan yang tidak ada di
  penyebut": bulan absen DI DALAM rentang lawan bulan gagal gerbang di TEPI
  riwayat.** Bulan tepi TIDAK dapat absen menurut definisi rentang. BNXUSDT **3**
  gagal gerbang lawan **2** absen. Kerabat KC-36 dan KC-35. Penangkal aturan 76.
- **KC-40 [v41, jurnal 116] — membaca daftar nama KLAUSA yang gagal sebagai
  pernyataan KEADAAN.** `gerbang_1m.KLAUSA` menamai klausa yang harus BENAR
  (`deret_tidak_kosong`, `tanpa_duplikat`, `tanpa_menit_hilang`, `jarak_60_detik`,
  `selaras_menit`, `satuan_milidetik`), sedangkan medan `pelanggaran` mendaftar
  klausa yang **GAGAL**. Maka `tanpa_menit_hilang` di dalam `pelanggaran` berarti
  menit MEMANG hilang — makna terbalik dari bunyi harfiahnya. Kerabat KC-30
  (nama kelas) dan KC-36 (homonim). **Penangkal: bila sebuah medan berisi daftar
  nama klausa yang gagal, nama-nama itu wajib dibaca sebagai negasi, dan anggota
  `pelanggaran` DILARANG dikutip sebagai pernyataan keadaan.**
- **KC-41 [v42, lahir dari `ci.yml`] — merumuskan pemicu sebuah workflow dari
  INGATAN, dan merumuskannya dalam bentuk yang berlawanan dengan kodenya.**
  Selama puluhan sesi batasan CI ditulis sebagai daftar `paths` yang MENGIZINKAN
  ("STATE.md, PROMPT_KELANJUTAN.md, lux_ai/**, tests/**"), padahal `ci.yml`
  memakai `paths-ignore` yang MELARANG empat direktori dan mengizinkan sisanya.
  Bentuk daftar-izin dan daftar-larangan menghasilkan ramalan yang berbeda pada
  setiap berkas di luar keduanya: push `README.md`, `requirements.txt`,
  `PETA_MODUL.md`, `.github/workflows/**`, dan **seluruh `STATE_LAMPIRAN*.md`**
  menyalakan CI, sedangkan rumusan lama meramalkan tidak. Akibat nyata: **tiga**
  run menyala di luar rencana dan salah satunya menimpa laporan run sebelumnya
  (aturan 38). Kerabat KC-19 (mencacah dari ingatan) dan KC-30 (nama dibaca
  sebagai keadaan). **Penangkal: rumusan pemicu wajib dikutip dari berkas workflow
  beserta blobnya, wajib menyebut apakah ia `paths` atau `paths-ignore`, dan setiap
  push wajib diperiksa terhadap bentuk itu SEBELUM didorong (aturan 45, 55, 66).**
- **KC-42 [v43, lahir dari dua pemotongan `STATE.md`] — menulis ulang berkas yang
  sudah melampaui batas satu push, lalu menganggap push itu berhasil karena alat
  mengembalikan commit.** `push_files` mengembalikan ref baru tanpa galat meski
  muatan yang terkirim berhenti di tengah kalimat: v41 terpotong di utang 24, v42
  di baris papan skor R-287. Keduanya hanya tertangkap oleh aturan 52, dan yang
  kedua nyaris memusnahkan naskah aturan itu sendiri — sebab aturan 1–76 dan
  KC-1..KC-41 hanya hidup di badan `STATE.md`, sehingga menulis v43 dari ingatan
  akan menghapusnya (kerabat KC-19). **Penangkal, mengikat:** (a) berkas yang
  tidak dapat ditulis utuh dalam satu kirim WAJIB DIPECAH, bukan didorong ulang —
  itulah sebab STATE kini tiga berkas; (b) commit yang dikembalikan alat BUKAN
  bukti keutuhan, hanya pembacaan ulang yang membuktikannya; (c) sesudah push
  berkas panjang, DILARANG menyusun berkas lain di atasnya sebelum pembacaan
  ulang; (d) sebelum menulis ulang berkas panjang, badan lamanya WAJIB dibaca utuh
  supaya naskah yang hanya hidup di sana tidak hilang. Kerabat aturan 38 (percaya
  keberadaan berkas) dan calon aturan 78 (batas alat sebagai desain).

## Ke bagian 2 dan 3

Berkas ini berhenti di sini dengan sengaja. Lanjutannya:

- **Papan skor R-199..R-296 (total 296), catatan kejujuran, jumlah uji 722, utang
  verifikasi 24, Daftar ADR A001–A008, temuan sampingan, penomoran berikutnya** →
  `STATE_LAMPIRAN_EKOR.md` (blob `7480cedd1f9b4bbe1b9d091ac9f8a6c59c95c139`).
- **Penyebut 787, taksonomi sembilan kelas, dua belas karantina, bulan ABSEN,
  H-A015, lubang funding 880/877, LITUSDT, BTCSTUSDT 2022-01, terhenti per jenis,
  lima belas pasangan SETTLED, penyebut per tahun, cacah baris, modul/workflow/uji,
  API, hipotesis H-A001..H-A016** → `STATE_LAMPIRAN_UKUR.md` (blob
  `0e9ec3783d95be522dd4e56221fc7197f89c13c0`).

Pekerjaan berikutnya sesudah utang tulis ini bersih: **jurnal 117**, **PROMPT
v44** (LANGKAH 0 wajib menyebut ketiga berkas STATE beserta blobnya), lalu
pekerjaan riset **anatomi BTCSTUSDT 2022-01** — prasyarat tersurat Keputusan 7
ADR-A008.
