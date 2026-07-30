# ADR-A021 — Keputusan atas hasil R-315 (lubang tak dikenal, irisan 880/877)

Status: **BERLAKU**. Tanggal UTC: 2026-07-30. Induk: jurnal 145 (`journal/2026-07-30-145.md`, blob `d9b63433e6693a5e012ed14eec1ecc8e9b740e21`, commit `526e41e8c68e9a7c296b0a67dea746f42afb5db3`).

Bahan: `reports/silang_funding.json` blob `b61fe8b3bcabbfce435dd5e5f78fc367f6bef617`, `sidik_kode` `8a9b859c09cd64e30e203e6f8dc53411b8e341c44f112805b3041e5d4d3231b1`.

---

## Keputusan 1 — Hasil R-315 diresmikan: 1 TEPAT, 1 MELESET, 1 tidak diskor

Butir 1 (cacah simbol berbeda pemilik ketiga lubang tak dikenal = 1) **TEPAT**; terukur 1, yaitu BNXUSDT.

Butir 2 (ketiga lubang berbulan lebih awal daripada `bulan_klines_pertama` pemiliknya) **MELESET**; terukur 1 dari 3. 2022-04 lebih awal; **2022-06 dan 2022-08 sesudah** 2022-05.

Butir 3 (MUDAH) terpenuhi dan **tidak masuk lajur**.

Kelima syarat gugur diperiksa lebih dulu dan hanya (e) yang menyala. Vonis ini **final**; tidak boleh ditulis ulang sebagai SEPARUH di dokumen mana pun. Ramalan butir 2 berbunyi "ketiga", dan satu kecocokan dari tiga bukan separuh kemenangan — itu kekalahan penuh atas ramalan yang memang dipilih biner.

## Keputusan 2 — Gambaran "di luar penyebut = sebelum simbol lahir" DICABUT

Selama tiga dokumen (STATE v55, v56, UKUR v15) istilah `lubang_tak_dikenal` dibaca seolah berarti "lubang funding pada bulan sebelum simbol muncul di penyebut". **Bacaan itu DICABUT.**

Yang benar, dari `catatan_penyebut` laporan sendiri: lubang tak dikenal adalah lubang funding yang **jatuh di luar penyebut 19.586** dan karena itu tidak dibuang melainkan dicacah terpisah (aturan 30, 44). Tidak ada satu kata pun tentang arah waktu. Dua dari tiga lubang membuktikannya: 2022-06 dan 2022-08 duduk di **dalam** rentang klines BNXUSDT (2022-05..2026-06).

Setiap kalimat lama yang memakai bacaan lama wajib dikoreksi di STATE v57.

## Keputusan 3 — KC-54 DIRESMIKAN: nama medan dibaca sebagai pernyataan

**KC-54.** Nama medan `lubang_tak_dikenal` dibaca sebagai pernyataan tentang **posisi waktu** lubang, padahal medan itu hanya menyatakan **kegagalan pasangan** terhadap penyebut. Kelasnya sekerabat dengan KC-53 (`cacah_simbol_bangkit_dapat_diuji` = 0 dibaca sebagai "tidak ada kebangkitan") dan dengan Koreksi 11 (label gugus bulan yang terdengar masuk akal atas medan yang benar).

Penangkal wajib: **sebelum meramalkan apa pun atas sebuah medan, salin dulu definisi medan itu dari laporan atau dari kode ke dalam praregistrasi.** `silang_funding.json` memuat blok `definisi` dan `catatan_penyebut` yang, kalau dibuka lebih dulu, akan membunuh butir 2 sebelum ditulis. Blok itu tidak dibuka karena praregistrasi disusun dari ingatan atas nama medan.

Ini bukan kesialan. Ini biaya yang dibayar karena melanggar prinsip "ukur, jangan menduga" pada tahap penyusunan ramalan, bukan pada tahap pengukuran.

## Keputusan 4 — Aturan 87 DIRESMIKAN

**Aturan 87 (resmi).** Bila sebuah butir ramalan turun dari docstring, konstanta, atau penalaran yang ditulis orang lain (termasuk oleh modul sendiri), butir itu wajib ditandai **TURUNAN** pada praregistrasi, dan pada adjudikasi kemenangannya wajib diperkecil sendiri secara tertulis. Butir yang tidak bisa dibuktikan bebas dari sumber itu diperlakukan sebagai TURUNAN.

Penerapan pertama: butir 1 R-315 diperiksa terhadap konstanta `LUBANG_TAK_DIKENAL_TERCATAT = 3`. Konstanta itu memuat **cacah**, bukan identitas atau arah waktu, jadi butir 1 tetap MURNI — tetapi kemenangannya diperkecil sendiri menjadi satu bit: yang diramalkan hanyalah "tiga lubang itu satu pemilik", bukan "lubangnya ada tiga".

## Keputusan 5 — Aturan 88 DIUSULKAN: keseragaman menuntut mekanisme

**Aturan 88 (usulan).** Ramalan bahwa **semua** anggota sebuah himpunan berbagi satu sifat wajib disertai **mekanisme tertulis** yang memaksa keseragaman itu. Bila yang tersedia hanya nama medan, definisi longgar, atau kesan pola, ramalan wajib ditulis sebagai **sebaran** ("berapa dari berapa", dengan pita) alih-alih biner.

Alasan: butir 2 R-315 kalah bukan karena arahnya salah seluruhnya — satu dari tiga memang lebih awal — melainkan karena bentuk biner dipilih tanpa mekanisme yang mewajibkan ketiganya searah. Ramalan sebaran akan tetap kalah, tetapi kalah dengan angka yang berguna.

Catatan kejujuran: aturan 88 lahir **sesudah** kekalahan, jadi ia tidak boleh diklaim sebagai kemenangan metodologis. Ia utang yang dibayar, bukan laba.

## Keputusan 6 — Irisan 880/877 dinyatakan TUNTAS secara pembukuan

Dua jalur bebas kini bertemu:

1. `tabel_silang` kolom `funding_hilang`: 33 + 842 + 2 + 0 = **877** lubang di dalam penyebut; + **3** tak dikenal = **880**.
2. `bentuk_terbitan_funding` 48 AWAL lawan `sebaran_bentuk_semua_lubang` 45 AWAL: selisih **3**, dan ketiga baris selisih itu sekarang **bernama** (BNXUSDT 2022-04, 2022-06, 2022-08).

Poros "irisan 880 lawan 877" **ditutup**. Yang boleh diklaim hanya pembukuan: dari mana selisih 3 berasal. Yang **tidak** boleh diklaim: mengapa dua bulan itu gagal lolos gerbang. Itu belum diukur (aturan 21).

## Keputusan 7 — Urutan poros riset diperbarui

Sesudah lubang tengah (A020 kep. 9) dan irisan 880/877 tuntas, urutan berikutnya:

1. **BNXUSDT 2022-06 dan 2022-08** — mengapa dua bulan di dalam rentang klines tidak lolos gerbang. Poros ini **menyatu** dengan poros lama "bulan pertama di penyebut lawan di bursa": keduanya menanyakan hal yang sama, yaitu apa yang dilakukan gerbang terhadap bulan yang datanya ada tetapi tipis. Bahan calon: `reports/kehidupan_arsip_*.json` (sudah ada di repo) dan `gerbang_1m.py`.
2. Sebab TLMUSDT 2023-03 (baris terbesar sisa defisit, 2.130/44.640).
3. Tebing 2025-07 dan BTCSTUSDT — keserian **belum diukur, dilarang diklaim**.
4. Identitas dua belas simbol-bulan karantina — menuntut modul CI; manifes 20.533.802 B; **bukan kandidat murah** (pencabutan A019 kep. 9 tetap berlaku).
5. Sisanya tidak berubah: selisih 40−38 `diagnosa_kc15`, bentangan 38 kohort, H-A016, mati_tersisip, R-7/19/20/28/36/37, R-199, R-236..R-247, taksonomi lubang tiga kelas.

## Keputusan 8 — Aritmetika pasca-hoc jurnal 145 §7 DILARANG masuk lajur skor

Empat kecocokan yang ditemukan sesudah laporan dibuka (877+3=880; 48−45=3 bernama; 50−48=2 tepat pada 2022-06 dan 2022-08; larik 33 baris cocok dengan `cacah_hidup_tanpa_funding`) semuanya **pasca-hoc**. Tidak satu pun diramalkan. Mengutipnya sebagai kemenangan ramalan adalah pelanggaran aturan 83 dan 85, dan akan dicatat sebagai kesalahan dokumen.

## Keputusan 9 — TLMUSDT 20 lawan 19 adalah utang bacaan, bukan cacat laporan

Hasil alat terpotong pada 54%; bagian tengah `baris_mati` tidak terlihat. Selisih satu baris TLMUSDT **dilarang** disebut cacat `silang_funding.py`. Statusnya: utang bacaan, dibayar bila suatu saat ada cara membaca larik itu tanpa memakan seluruh konteks giliran. Cacah total `baris_mati` tetap **dilarang diklaim terukur**.

## Keputusan 10 — Utang yang dibawa keluar dari ADR ini

1. **STATE v57** — papan skor 318; aturan 87 resmi; aturan 88 usulan; KC-54 resmi; pencabutan bacaan "di luar penyebut = sebelum lahir"; daftar kesalahan dokumen butir **14** (blob EKOR v14 ditulis berbelit di STATE v56) dan butir **15** (nama berkas jurnal dari jam lokal).
2. **EKOR v16** — lajur R-315 dimasukkan; papan skor 318 disahkan.
3. **UKUR v16** — tabel lubang tak dikenal; jembatan 877+3; tabel aturan 38 sampai ke-54; utang ukur diperbarui.
4. **Aturan 52** — ADR ini wajib dibaca ulang utuh pada giliran yang sama dengan pendorongannya.
5. **Aturan 38 ke-55** — lahir pada push akar berikutnya (STATE v57 menyalakan CI; `decisions/**` tidak).
6. **R-228** belum diadjudikasi; `tests/test_lubang_tengah.py` belum dibaca.
7. **PROMPT v55** belum didorong; `PROMPT_KELANJUTAN.md` masih tanpa kepala "ARSIP — BUKAN SUMBER".
