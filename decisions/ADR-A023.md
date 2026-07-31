# ADR-A023 — Aturan 77 dan 78 diputus; aturan 93 diresmikan pada rumusan kedua; nasib KC-58 dan KC-59; permohonan pencabutan aturan 88/89/91/92 ditolak dengan syarat

Status: **DITERIMA**
Tanggal: 2026-07-31 (UTC)
Penyusun: agen riset LUX-AI, atas perintah operator Diva Juan Nur Taqarrub (`EnVyxS`)
Papan skor saat penyusunan: **339 — SAH** (disahkan `STATE_LAMPIRAN_EKOR.md` v20, blob `957b99e964bd63be567c310c29a62143c5350bf8`)

---

## 0. Keadaan terukur pada saat penyusunan

Semua angka di bawah ini dibaca pada giliran ini juga, bukan dari ingatan.

| hal | nilai |
|---|---|
| trio akar serasi penuh | `STATE.md` **v62** blob `a762c129914b9adfa8175b4746ba219d6e80f775` · `STATE_LAMPIRAN_EKOR.md` **v20** blob `957b99e964bd63be567c310c29a62143c5350bf8` · `STATE_LAMPIRAN_UKUR.md` **v20** blob `56cfded0c4e8711a96d79df28d9bd4b006fc3604` |
| aturan 38 ke-70 | blob `e5e015037d7af172d03e7e532775808672a22165`, run **30616177405**, commit `8e6f583df0816e262b23ad1a0e2c68b41ea4df02`, `waktu_utc` 2026-07-31T08:24:41Z, kode 0, `"1377 tests collected in 0.61s"` |
| aturan 90 | dipakai **sembilan** kali, **nol** nyala — DILARANG disebut teruji |
| tip `main` sebelum ADR ini | `4dc444f0fc57cbfb5425ffcaa23e077bcfa6345b` (commit bot CI di atas `8e6f583d`) |
| sumber teks aturan 77 dan 78 | `STATE.md` **v43**, blob **`a91a49346a6ebcf1a288b936904a8fe1facc3d7a`**, commit **`eea324fd98f76d27c812690eaea54467408508ec`**, dibaca **UTUH** pada giliran ini |

**Catatan prosedur.** Push ini menyentuh `decisions/**`, yang ADA di `paths-ignore` `ci.yml` (blob `c79497b2c812679eaa69aee5b3160eac9f5c5fb7`). Maka push ini **TIDAK menyalakan CI** dan tidak melahirkan commit bot. Tidak ada adjudikasi pada giliran ini (ADR-A016).

---

## 1. Konteks: mengapa dua calon aturan menganggur enam belas versi

Calon aturan 77 lahir di STATE v41/v42 dan calon aturan 78 lahir di STATE v43. Keduanya **DITUNDA oleh ADR-A022 keputusan 6** dengan alasan tersurat: teks penuhnya tidak ada di tangan, dan meresmikan aturan dari ingatan adalah KC-19.

Penundaan itu benar dan biayanya nyata: **enam belas versi STATE** berlalu dengan dua nomor aturan yang berlubang. Yang menutup lubang ini bukan penalaran baru, melainkan satu pembacaan: `STATE.md` v43 pada commit `eea324fd98f76d27c812690eaea54467408508ec`, blob `a91a4934…` — persis blob yang dicatat prompt. Berkas itu ditemukan lewat `search_commits`, bukan `search_code` (yang selalu 0 hasil di repo ini).

**Pelajaran prosedural yang wajib dicatat:** aturan yang teksnya hanya hidup di satu versi berkas lama tidak hilang — ia dapat dipanggil kembali selama blobnya dicatat. Disiplin mencatat blob adalah yang membuat penundaan enam belas versi dapat dipulihkan tanpa mengarang satu kata pun.

---

## 2. Keputusan 1 — Aturan 77 DIRESMIKAN, dengan rumusan yang DIPERTAJAM

### 2.1 Teks calon yang dikutip verbatim dari STATE v43

> **Calon aturan 77 (DIUSULKAN, belum berlaku):** dua berkas laporan yang berblob IDENTIK bukan dua pengukuran. Asalnya jurnal 115/116: `reports/bulan_absen.log` dan `reports/bulan_absen_ringkas.json` berblob sama (`e450d9f95e9bca0dc28a0e01c6aad6594c4fa3d6`) karena workflow men-`tee` stdout modul. Belum dijadikan aturan bernomor karena baru satu kasus. **[v42] Sisi sebaliknya kini punya contoh yang menyehatkan:** `ci_terakhir.json` dan `ci_terakhir.txt` berblob BERBEDA (`1b10bd19` lawan `0f8626bc`) dan memang berisi dua keluaran pytest yang berbeda — jadi ujinya bukan "nama berbeda" melainkan **blob berbeda DAN asal perintah berbeda**.

### 2.2 Ambang yang berlaku

ADR-A022 keputusan 1 menetapkan dua jenis usulan dengan dua ambang: **kelas cacat (KC) butuh DUA kejadian**; **aturan disiplin pengukuran/praregistrasi cukup SATU manfaat terukur**. Aturan 77 adalah aturan disiplin pengukuran — ia mengatur cara menghitung banyaknya bukti, bukan menamai satu jenis kekeliruan berulang. Maka ambangnya **satu manfaat terukur**.

### 2.3 Manfaat terukur yang sudah ada

1. **Kejadian asal (jurnal 115/116).** `reports/bulan_absen.log` dan `reports/bulan_absen_ringkas.json` berblob **identik** `e450d9f95e9bca0dc28a0e01c6aad6594c4fa3d6`. Tanpa aturan ini keduanya dapat dikutip sebagai dua saksi; nyatanya mereka satu berkas dengan dua nama, hasil `tee` stdout.
2. **Manfaat terukur pada sesi ini.** Bahan jurnal 150/151 adalah `reports/bulan_absen_ringkas.json`, blob **`e450d9f95e9bca0dc28a0e01c6aad6594c4fa3d6`** — **blob yang sama persis**. Empat butir R-318 diadjudikasi dari berkas itu dan **`bulan_absen.log` TIDAK pernah dikutip sebagai saksi kedua**. Angka empat kemenangan itu tetap empat, bukan delapan. Inilah manfaat terukurnya: aturan 77 sudah bekerja sebagai kebiasaan sebelum ia bernomor.
3. **Contoh penyeimbang yang mempertajam ujinya.** `ci_terakhir.json` (`1b10bd19`) lawan `ci_terakhir.txt` (`0f8626bc`): blob berbeda, dan asal perintahnya juga berbeda (`--collect-only` lawan eksekusi). Keduanya sah dihitung sebagai dua pencocokan (aturan 69).

### 2.4 Rumusan RESMI aturan 77 (yang berlaku sejak ADR ini)

> **Aturan 77 (RESMI).** Dua berkas laporan yang **berblob identik bukan dua pengukuran** — ia satu pengukuran dengan dua nama. Sebuah berkas hanya boleh dihitung sebagai saksi tambahan bila **blobnya berbeda DAN asal perintahnya berbeda**; kesamaan blob mengalahkan perbedaan nama, perbedaan ekstensi, dan perbedaan direktori. Setiap klaim "dicocokkan dari dua sumber" (aturan 69) wajib menyebut **kedua blob** secara tersurat, dan bila keduanya sama, klaim itu gugur menjadi satu sumber.

### 2.5 Batas aturan 77 yang wajib disebut

- Aturan 77 hanya menyaring **kelipatan sempurna**. Dua berkas yang berblob berbeda tetapi lahir dari **satu perintah yang sama** (misalnya laporan yang sama ditulis dua kali dengan stempel waktu berbeda) **tidak** tertangkap olehnya. Itu sebab klausa "asal perintah berbeda" ikut mengikat.
- Aturan 77 **tidak** mengatakan apa pun tentang mutu isi. Dua blob berbeda dari dua modul berbeda tetap bisa sama-sama keliru.
- **DILARANG** memakai aturan 77 untuk membatalkan pengukuran mana pun yang sudah masuk papan skor. Ia mengatur **pencacahan saksi**, bukan **vonis**.

---

## 3. Keputusan 2 — Aturan 78 DIRESMIKAN, dengan angka yang KINI TERUKUR

### 3.1 Teks calon yang dikutip verbatim dari STATE v43

> **Calon aturan 78 (DIUSULKAN [v43], belum berlaku):** batas panjang alat adalah bagian dari DESAIN repo, bukan kecelakaan. Struktur berkas wajib disesuaikan dengan batas alat yang TERUKUR — ±2,4 MB sebagai batas baca (manifes pecahan 2 DITOLAK) dan sekitar satu berkas STATE penuh sebagai batas tulis (dua pemotongan berturut). Belum dijadikan aturan bernomor karena batas tulisnya baru terukur secara kasar: yang diketahui hanyalah bahwa ±45 KB berhasil dan STATE penuh gagal dua kali; angka pastinya belum diukur.

### 3.2 Alasan penundaan itu KINI GUGUR — batasnya sudah terukur jauh lebih rapat

Calon aturan 78 ditunda karena satu alasan tersurat: **angka pastinya belum diukur**. Sesi ini mengukurnya dari empat arah.

**(a) Batas BACA — penolakan penuh.** Kedelapan `reports/manifes_pecahan_*.json` DITOLAK alat, galat verbatim: `File reports/manifes_pecahan_0.json is too large to display (2530465 bytes).` Ukurannya terukur satu per satu: 2.530.465 · 2.587.577 · 2.446.093 · 2.257.314 · 2.615.515 · 2.865.596 · 2.780.523 · 2.450.719 B, jumlah **20.533.802 B**. **Yang terkecil yang ditolak: 2.257.314 B.** Maka batas tolak berada **di bawah 2.257.314 B**, bukan "±2,4 MB" — taksiran v43 terlalu longgar dan kini diperketat oleh pengukuran.

**(b) Batas BACA — pemotongan yang berteriak.** Terukur tiga titik pada sesi ini dan sesi sebelumnya: `reports/semesta_rentang.json` 110.662 B → **95%**; `reports/silang_funding.json` 194.728 B → **54%**; daftar direktori `reports/` → **76%**. Kesimpulan yang mengikat: **pemotongan mulai jauh di bawah 200 KB**, ratusan kali lipat lebih rendah daripada batas tolak. Dua rezim ini berbeda dan DILARANG dicampur.

**(c) Batas TULIS.** Empat pemotongan terdokumentasi: `STATE.md` v41 (berhenti di utang 24), v42 (berhenti di baris R-287), dan **`STATE_LAMPIRAN_UKUR.md` v19** (`c28202df…`, blob `40e450b65cf9f5f068f3af7380711a0dd214646d`) yang berhenti verbatim di tengah kata: `**[BARU v19] Usulan aturan 91 [BELUM RESMI].** Ramalan yang butir-butirnya diturunkan dari **satu arit`. Lawan itu, **empat berkas akar PADAT berturut berhasil utuh**: STATE v61, STATE v62, EKOR v20, UKUR v20 — semuanya di pita **±25–45 KB** dan semuanya berakhir pada penanda penutupnya sendiri.

**(d) Alat tidak berteriak saat menulis.** `push_files` mengembalikan commit dengan gembira atas muatan cacat — tiga kali. Ini bukan taksiran; ini tiga kejadian bernomor commit.

### 3.3 Rumusan RESMI aturan 78 (yang berlaku sejak ADR ini)

> **Aturan 78 (RESMI).** Batas panjang alat adalah **bagian dari desain repo**, bukan kecelakaan yang boleh diulangi. Struktur berkas wajib disesuaikan dengan batas alat yang **terukur**, dan angka-angka berikut mengikat sampai diukur ulang:
> - **Batas tulis aman: ±25–45 KB per push.** Berkas yang tidak muat wajib **DIPECAH**, bukan didorong ulang (KC-42).
> - **Batas baca — penolakan penuh:** terjadi setidaknya pada **2.257.314 B**; tidak ada isi sama sekali yang diperoleh, dan tidak ada jalan pintas lewat `raw.githubusercontent.com` karena repo tertutup.
> - **Batas baca — pemotongan:** sudah terjadi pada **110.662 B (95%)** dan **194.728 B (54%)**; pemotongan **berteriak** lewat `truncated (showing NN%)` dan wajib dibaca.
> - **Keberhasilan panggilan alat BUKAN bukti keutuhan muatan.** Hanya pembacaan ulang yang membuktikannya (aturan 52), dan penanda penutup wajib ada (aturan 92).
> - Sebelum sebuah berkas dijadikan bahan, **ukurannya wajib diketahui lebih dulu lewat daftar direktori** (aturan 93).

### 3.4 Hubungan aturan 78 dengan kelas kegagalan keempat

Aturan 78 kini menjadi rumah resmi bagi tabel empat kelas pemotongan:

| kelas | siapa memotong | berteriak? | isi yang didapat | penangkal |
|---|---|---|---|---|
| ALAT | alat baca | **YA** | sebagian | membaca peringatan |
| MODUL | kode penulis laporan | TIDAK | sebagian | aturan 86 (b) |
| PENYUSUN | penyusun berkas | TIDAK | sebagian | aturan 52 + 92 |
| **PENOLAKAN PENUH** | **alat baca** | **YA** | **NOL** | **aturan 93 + 78** |

---

## 4. Keputusan 3 — Aturan 93 DIRESMIKAN pada RUMUSAN KEDUA

### 4.1 Duduk perkaranya

Usulan aturan 93 lahir di jurnal 156 sebagai buah kekalahan R-320. **Rumusan pertamanya mewajibkan pemeriksaan ukuran bahan tanpa menyebut CARANYA.** Satu giliran kemudian, upaya mematuhinya menyebabkan pelanggaran aturan 21 yang **kedua**: `get_file_contents` atas `reports/karantina_semesta.json` dimaksudkan memeriksa ukuran saja, tetapi alat mengembalikan **seluruh isi** (blob `678b665c1d32d6d5bbda0d9fd93445bcd64b2932`), sehingga berkas itu terbakar sebagai bahan ramalan.

**Ironi yang wajib ditulis:** pelanggaran lahir dari upaya mematuhi aturan yang baru diusulkan penyusun sendiri. **Aturan yang dirumuskan setengah jalan tidak melindungi — ia mengarahkan ke lubang lain.**

### 4.2 Dua manfaat terukur yang BERARAH BERLAWANAN

- **R-320:** ukuran **tidak diperiksa sama sekali** → delapan bahan ditolak alat → lima butir TIDAK TERADJUDIKASI.
- **Jurnal 157:** ukuran **diperiksa dengan cara yang salah** → satu bahan terbakar.

Dua arah kegagalan pada satu sumbu adalah pembenaran terkuat yang tersedia bagi sebuah aturan disiplin. Ambang ADR-A022 keputusan 1 (satu manfaat terukur) terlampaui.

### 4.3 Rumusan RESMI aturan 93

> **Aturan 93 (RESMI, rumusan kedua — satu-satunya yang berlaku).** Ukuran sebuah bahan wajib diperoleh lewat **daftar direktori**, **tidak pernah** lewat panggilan pengambil isi; ukuran itu wajib **dicatat di praregistrasi** bersama nama dan blob bahannya. Bahan yang ukurannya tidak diketahui **DILARANG** didaftarkan sebagai bahan ramalan.

**DILARANG mengutip rumusan pertama aturan 93 dalam artefak mengikat mana pun.** Rumusan pertama tetap boleh disebut sebagai riwayat kekeliruan, dengan penanda tersurat bahwa ia dicabut.

---

## 5. Keputusan 4 — KC-58 DITUNDA (tetap usulan hidup)

**Bunyi usulan:** satu nama gejala dapat menutupi dua mekanisme berbeda. Bahan: **sembilan dari sepuluh** simbol berabsen kehilangan tepat bulan settled terakhirnya; **BNXUSDT tidak**.

**Kejadian terukur: SATU.** ADR-A022 keputusan 1 menetapkan KC butuh **DUA** kejadian, dan keputusan itu tidak boleh dilanggar oleh penyusunnya sendiri satu ADR sesudahnya — presedennya sudah buruk sekali (lihat §7).

**Putusan: KC-58 DITUNDA, tetap usulan hidup.** Syarat pematangannya ditetapkan tersurat supaya penundaan ini tidak menjadi penundaan tanpa ujung:

1. **Utang verifikasi 46 dibayar** — mengapa sembilan dari sepuluh kehilangan tepat bulan settled terakhirnya.
2. **Satu kejadian kedua ditemukan pada gejala yang BERBEDA** — bukan pada sepuluh simbol yang sama. Kejadian kedua atas gejala yang sama hanyalah pengukuran ulang, bukan kelas.

**DILARANG** menulis KC-58 sebagai kelas cacat resmi. **DILARANG** memakai selisih 9 lawan 1 sebagai bukti bahwa mekanismenya sudah diketahui — yang terukur adalah **pola nama**, bukan mekanisme.

---

## 6. Keputusan 5 — KC-59 DIBUANG sebagai kelas cacat; menjelma menjadi UTANG UKUR 31

**Bunyi usulan:** pada 19.598 simbol-bulan, gerbang 1m hanya pernah menjatuhkan lewat **satu pasangan klausa** (`jarak_60_detik` + `tanpa_menit_hilang`, **12 dari 12**); **empat klausa lain nol kejadian**.

Pernyataan itu **benar dan terukur** (`sebaran_pelanggaran` di `reports/karantina_semesta.json`). Tetapi ia bukan **kelas cacat** — ia tidak menamai kekeliruan yang dapat diulangi oleh peneliti; ia menamai **temuan empiris tentang perilaku sebuah gerbang**. Menyimpannya sebagai KC akan mengulangi KC-35 (menyamakan cakupan satu laporan dengan cakupan sebuah kelas).

Ditambah satu hal yang menyempitkan maknanya: dua dari enam klausa terbukti **mustahil menyala** dari pembacaan kode — `tanpa_duplikat` (dijamin `drop_duplicates` di `klines.rapikan`) dan, menurut `tests/test_gerbang_1m.py`, `deret_tidak_kosong` hanya menyala pada deret kosong yang tidak pernah sampai ke gerbang. Maka "empat klausa nol" bukan empat teka-teki setara.

**Putusan: KC-59 DIBUANG sebagai kelas cacat.** Isinya dipindahkan utuh menjadi **utang ukur 31**:

> **Utang ukur 31.** Untuk masing-masing dari empat klausa gerbang 1m yang nol kejadian (`deret_tidak_kosong`, `tanpa_duplikat`, `selaras_menit`, `satuan_milidetik`): tetapkan dari **kode**, bukan dari laporan, apakah nol itu berarti (a) **mustahil menyala** karena dijamin langkah sebelumnya, (b) **mungkin menyala tetapi tidak pernah terjadi** pada 19.598, atau (c) **belum diketahui**. Sertakan penyebut dan definisi uji tiap klausa (aturan 74).

**DILARANG** menyebut KC-59 sebagai usulan hidup sesudah ADR ini. **DILARANG** menyimpulkan bahwa gerbang 1m "pada praktiknya berklausa satu pasang" sebelum utang ukur 31 dibayar.

---

## 7. Keputusan 6 — Permohonan pencabutan aturan 88, 89, 91, 92 DITOLAK; aturan 89 DIPERTEGAS

### 7.1 Alasan permohonan

`STATE_LAMPIRAN_EKOR.md` v20 memberi ADR ini wewenang mencabut aturan 88/89/91/92 **bila terbukti upacara**, dan butir kesalahan dokumen **21** memberi satu alasan konkret: **aturan 89 dilanggar penulisnya sendiri satu giliran sesudah diresmikan ADR-A022.** Ruang vonis butir 2 dan 4 jurnal 155 hanya bersisi tiga; sisi **"bahan tidak terjangkau" tidak ada** — padahal justru sisi itulah yang terjadi. Butir 1, 3, dan 5 menutupnya.

### 7.2 Uji upacara yang ditetapkan ADR ini

> Sebuah aturan disebut **UPACARA** bila kepatuhan penuh terhadapnya **tidak mengubah satu pun angka, vonis, atau tindakan** yang akan diambil tanpanya. Aturan yang **DILANGGAR** bukan aturan upacara — pelanggaran justru bukti bahwa ia mengikat sesuatu.

Dengan uji itu, keempat aturan diperiksa:

| aturan | isi ringkas | terpakai? | upacara? |
|---|---|---|---|
| 88 | ramalan atas bahan yang belum pernah dibaca wajib menyebut sisi "medan tidak ada" | ya, satu kejadian | **TIDAK** — R-320 menunjukkan akibat langsung ketiadaannya |
| 89 | ruang vonis praregistrasi wajib menutup **semua** sisi | dilanggar sekali | **TIDAK** — pelanggarannya berakibat pada bentuk vonis lima butir |
| 91 | butir yang saling berkorelasi wajib dinyatakan berkorelasi sebelum diadili | dipakai **dua** kali (R-319, R-320) | **TIDAK** — ia mencegah 4 kemenangan semu dihitung |
| 92 | berkas panjang wajib berakhir pada penanda penutup | dipatuhi **empat** kali berturut | **TIDAK** — ia yang menangkap pemotongan UKUR v19 |

**Putusan: keempatnya TIDAK DICABUT.**

### 7.3 Aturan 89 DIPERTEGAS (amandemen, bukan pencabutan)

> **Aturan 89 (RESMI, DIPERTEGAS oleh ADR-A023).** Ruang vonis setiap butir praregistrasi wajib menutup **semua** sisi yang mungkin, dan sejak ADR ini sisi **"bahan tidak terjangkau"** wajib **ditulis tersurat pada setiap butir tanpa kecuali** — bukan hanya pada butir yang penyusunnya anggap berisiko. Butir yang ruang vonisnya kurang dari empat sisi (menang / kalah / bahan ada tetapi medan tak ada / bahan tidak terjangkau) adalah **praregistrasi CACAT**, dan kecacatannya milik peramal.

### 7.4 Larangan yang menyertai

- **DILARANG** menyebut satu pun dari aturan **85, 88, 89, 90, 91, 92, 93** sebagai "teruji". Kepatuhan berulang bukan pengujian.
- **DILARANG** memakai kenyataan bahwa akibat butir 21 pada angka adalah **nihil** untuk menyatakan cacatnya tak berakibat. Hasil yang kebetulan sama bukan pembenaran prosedur.
- **DILARANG** menghitung R-320 sebagai bukti bahwa aturan 88/89/91 bekerja **maupun** gagal.

---

## 8. Keputusan 7 — Penomoran dan status sesudah ADR ini

| hal | sebelum | sesudah |
|---|---|---|
| aturan RESMI | 1–81, 83–92 | **1–81, 83–93** (82 tetap dicadangkan) |
| usulan aturan hidup | 77, 78, 93 | **tidak ada** |
| aturan berikutnya | 94 | **94** |
| usulan KC hidup | KC-58, KC-59 | **KC-58 saja** |
| KC berikutnya | KC-60 | **KC-60** |
| utang ukur hidup | 6, 7, 17, 21, 22, 26, 27, 30 | **6, 7, 17, 21, 22, 26, 27, 30, 31** |
| utang ukur berikutnya | 31 | **32** |
| utang verifikasi hidup | 45, 46, 47, 48, 49 | tidak berubah |

**KC-16 tetap kosong selamanya.** ADR berikutnya: **A024**. ADR-A003 masih **BELUM ADA** dan tetap menjadi blokir pertama klasifikasi.

---

## 9. Keputusan 8 — Yang WAJIB diserap ke trio akar berikutnya

Keserasian trio pecah begitu **STATE v63** naik, dan wajib dipulihkan lewat **EKOR v21** dan **UKUR v21**. Yang wajib masuk:

1. **STATE v63** — aturan 77 dan 78 pindah dari "calon" ke daftar aturan RESMI dengan teks §2.4 dan §3.3; aturan 93 RESMI dengan teks §4.3; aturan 89 versi dipertegas §7.3; KC-59 dihapus dari daftar usulan; KC-58 tetap usulan dengan dua syarat §5; uji upacara §7.2 dicatat; larangan-larangan §7.4.
2. **EKOR v21** — mencatat ADR-A023 DITERIMA; papan skor tetap **339** (ADR tidak mengubah skor); praregistrasi **R-321** bila bahannya sudah memenuhi enam belas syarat kumulatif, kini ditambah kepatuhan aturan 93 rumusan kedua dan aturan 89 empat sisi.
3. **UKUR v21** — tabel batas alat §3.2 (a)–(d) sebagai pengukuran resmi; tabel empat kelas pemotongan §3.4 dipindah ke rumah aturan 78; **utang ukur 31** dibuka.

---

## 10. Yang TIDAK diputus di sini

- **Nasib `reports/karantina_semesta.json` sebagai bahan.** Ia sudah dibuka tanpa praregistrasi dan **tidak dapat dipakai sebagai bahan R-321** — larangan ini tidak dapat ditawar dan tidak dibuka kembali oleh ADR ini.
- **Utang verifikasi 49** (perlukah kelas BAHAN TAK BERSAKSI dilarang menjadi masukan artefak mengikat) tetap **DITUNDA**; bahannya baru satu berkas (`semesta_rentang.json`).
- **Sebab kelipatan hari penuh BNXUSDT** (utang ukur 30) tidak disentuh. **DILARANG** menyimpulkan sebabnya dari ADR ini.
- **Vonis R-319 dan R-320** tidak disentuh sama sekali. R-320 tetap **lima dari lima TIDAK TERADJUDIKASI, permanen**; empat butir yang "akan menang" tetap **DILARANG** masuk papan skor, dihitung bukti bebas, atau dipakai memperbaiki nisbah.

---

## 11. Ringkasan keputusan

1. **Aturan 77 DIRESMIKAN** — blob identik bukan dua pengukuran; saksi tambahan butuh **blob berbeda DAN asal perintah berbeda**.
2. **Aturan 78 DIRESMIKAN** dengan angka terukur — tulis aman ±25–45 KB; tolak baca setidaknya pada 2.257.314 B; pemotongan sudah pada 110.662 B.
3. **Aturan 93 DIRESMIKAN pada rumusan kedua** — ukuran lewat daftar direktori, tidak pernah lewat pengambil isi; rumusan pertama DILARANG dikutip.
4. **KC-58 DITUNDA** dengan dua syarat pematangan tersurat.
5. **KC-59 DIBUANG** sebagai kelas cacat; menjelma menjadi **utang ukur 31**.
6. **Aturan 88, 89, 91, 92 TIDAK DICABUT**; ditetapkan **uji upacara**; **aturan 89 DIPERTEGAS** menjadi empat sisi wajib.
7. Penomoran dimutakhirkan: aturan RESMI **1–81, 83–93**; tidak ada usulan aturan yang tersisa.
8. STATE v63 / EKOR v21 / UKUR v21 wajib menyerap ADR ini; keserasian trio pecah dan wajib dipulihkan.

**Catatan penutup yang jujur.** ADR ini tidak menambah satu angka riset pun. Ia menutup tiga lubang tata tertib yang sudah menganggur enam belas versi dan satu yang lahir dua giliran lalu. Nilainya baru akan terukur pada R-321: bila praregistrasi berikutnya mencatat ukuran tiap bahan dari daftar direktori dan menutup empat sisi vonis, aturan 93 dan aturan 89 terbayar; bila tidak, ADR ini adalah upacara menurut ujinya sendiri.

— akhir decisions/ADR-A023.md —
