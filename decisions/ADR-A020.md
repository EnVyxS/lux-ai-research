# ADR-A020 — Kebangkitan yang terukur, dan dua cacat pada satu keputusan

Tanggal: 2026-07-31 (UTC)
Tip saat ditulis: `d92ba0f16024d1728265267b21322c36fbc1426e` (jurnal 143),
terverifikasi lewat `list_commits` sebelum push ini.
Sumber: jurnal 142 (`af11d8a2`, commit `ae867f2e`), jurnal 143 (`fb4ec5ad`,
commit `d92ba0f1`), `reports/lubang_tengah.json` (`39cd1caa`),
`lux_ai/serapan/lubang_tengah.py` V2 (`4d3beaf1`).
Pendahulu: ADR-A019 (`9cd7d25e`, commit `e6007ba5`).

---

## Keputusan 1 — H-A011 **TERBUKTI**

LITUSDT kehilangan funding pada lima bulan 2025-07..2025-11 dan memperolehnya
kembali pada 2026-01. Enam bulan 2026-01..2026-06 seluruhnya berstatus **HIDUP**
(`sebaran_status` = {HIDUP 6, MATI 0, SEPI 0, TAK_TERUKUR 0}; `terukur` true;
`menang` true). Maka kembalinya funding pada pasar itu **disertai perdagangan**,
bukan sekadar terbitnya ulang arsip.

Batas yang melekat pada keputusan ini, dikutip dari laporan sendiri: status
HIDUP **tidak** membuktikan sebab kembalinya funding; ia hanya menunjukkan
perdagangan dan penerbitan pulih bersama (aturan 10). Generalisasi ke simbol
lain **DILARANG**: yang terukur satu simbol, satu jeda, satu pemulihan.

## Keputusan 2 — kebangkitan PERTAMA yang terukur; nol lama dicabut maknanya

`kohort_ekor` V4 menerbitkan `cacah_simbol_bangkit_dapat_diuji` = 0. Angka itu
dipakai sebagai dasar R-230 dengan bacaan "tidak ada kebangkitan di repo ini".
Bacaan itu **KELIRU** dan dengan ini dicabut. Yang benar: tidak ada kebangkitan
yang dapat diuji **menurut definisi kohort ekor**. Kebangkitan itu sendiri ADA,
dan LITUSDT adalah kejadian terukur pertamanya.

Mulai sekarang, mengutip `cacah_simbol_bangkit_dapat_diuji` = 0 sebagai bukti
ketiadaan kebangkitan **DILARANG**.

## Keputusan 3 — KC-53 DIRESMIKAN

**KC-53 — nol pada sebuah medan dibaca sebagai ketiadaan fenomena.** Nol pada
sebuah medan hanya berarti nol *menurut penyebut dan definisi medan itu*.
Membacanya sebagai ketiadaan fenomena di dunia adalah kesalahan penyebut.

Dua kejadian terukur:
1. Koreksi 10 (UKUR v14) — kesunyian sebuah dokumen dibaca sebagai klaim.
2. R-230 (jurnal 143) — `cacah_simbol_bangkit_dapat_diuji` = 0 dibaca sebagai
   ketiadaan kebangkitan.

Penangkalnya: setiap kali sebuah nol dipakai sebagai premis, penyebut dan
definisi medannya wajib ditulis pada kalimat yang sama.

## Keputusan 4 — R-314 diadjudikasi 2 TEPAT / 1 MELESET

| butir | ramalan | terukur | vonis |
| --- | --- | --- | --- |
| 1 | `cacah_per_simbol_funding` ∈ [747, 827] | 787 | TEPAT |
| 2 | `h_a010_cacah_simbol_berisi` = 0 | 0 | TEPAT |
| 3 | `h_a011_cacah_hidup` = 0 | 6 | MELESET |

Syarat gugur 5 menyala: kesamaan 787 dengan `cacah_simbol` klines **DILARANG**
dibaca sebagai bukti kedua himpunan simbol itu sama. Yang terukur hanya kedua
cacahnya sama besar.

Papan skor: 313 + 3 = **316**, TEPAT +2, MELESET +1. Angka ini wajib
diverifikasi ulang komposisinya saat STATE v56 ditulis.

R-314 adalah praregistrasi **pertama** yang memenuhi kesembilan syarat kumulatif
ADR-A019 kep. 9 sekaligus (aturan 79, 83, 84, 85, 86, kebebasan medan, KC-50,
KC-52, aturan 66). Aturan 85 dengan ini punya **adjudikasi pertamanya** sejak
dirumuskan.

## Keputusan 5 — praregistrasi warisan ikut diadjudikasi

Docstring `lubang_tengah.py` memuat enam praregistrasi. R-221, R-222, R-223
sudah beranotasi TEPAT di dalam kode. Dua sisanya diadjudikasi pada pembacaan
jurnal 143:

- **R-229 TEPAT** — `kosong_seluruhnya` true, `cacah_berisi` 0,
  `cacah_tak_terukur` 0. Konsekuensinya: definisi turunan
  `bulan_berfunding_pertama` bukan hanya memadai melainkan **TEPAT**, dan
  kemenangan R-223 **tidak** perlu ditinjau ulang.
- **R-230 MELESET** — diramalkan `cacah_hidup` = 0, terukur 6.

Keduanya **tidak** ditambahkan ke papan skor giliran ini: keduanya milik
giliran penulis modul, bukan milik giliran yang membacanya. Pencatatannya di
STATE v56 wajib memakai kolom terpisah.

## Keputusan 6 — aturan 86 diperluas dengan butir (b)

Aturan 86 sudah resmi sejak ADR-A019. Kejadian ketiga (jurnal 143) menunjukkan
lubang yang tersisa: bukan hanya *laporan* yang bisa sudah ada, melainkan juga
*praregistrasi*.

**Aturan 86 butir (b) — DIRESMIKAN.** Sebelum meramalkan isi sebuah laporan,
docstring modul penghasilnya wajib dibaca untuk memeriksa apakah ramalan atas
medan yang sama sudah tertulis di sana. Ramalan yang mengulangnya tanpa
menyebutnya adalah pengambilan kredit atas penalaran orang lain.

Tiga kejadian yang mendasari aturan 86 secara keseluruhan: taksiran uji
pemisah (jurnal 138 §4), `selisih_lilin` atas angka yang sudah tersimpan
(jurnal 140 §7), dan poros lubang tengah (jurnal 143 §5).

## Keputusan 7 — aturan 87 DIUSULKAN (belum resmi)

**Usulan aturan 87 — ramalan turunan wajib ditandai.** Sebuah butir ramalan
yang hanya menegaskan ulang praregistrasi pihak lain wajib ditandai
**TURUNAN** di tempat ia ditulis, dan hasilnya — menang maupun kalah — dicatat
pada kolom terpisah dari papan skor.

Status: **USULAN**, bukan resmi. Baru satu kejadian (butir 2 dan 3 R-314), dan
ADR-A019 kep. 3 sudah menetapkan bahwa satu kejadian tidak cukup untuk
meresmikan aturan. Diresmikan pada kejadian kedua.

Catatan yang memberatkan giliran penulis: penandaan itu **sudah dilakukan** di
jurnal 142 sebelum hasilnya diketahui. Yang belum ada hanyalah kewajibannya.

## Keputusan 8 — dua pencabutan atas ADR-A019 keputusan 9

1. Sebutan **"termurah"** bagi poros identitas dua belas simbol-bulan karantina
   **DICABUT**. Manifes berjumlah 20.533.802 byte atas delapan berkas; batas
   baca alat ±30.000 token; poros itu menuntut modul yang berjalan di CI.
   Kejadian ketiga taksiran biaya keliru, dan yang pertama ke arah terlalu
   murah.
2. Label **"lubang tengah gugus `2022-05`/`2024-05`"** **DICABUT**. Bulan yang
   terukur: BTCSTUSDT **2022-01** (rentetan 1) dan LITUSDT **2025-07..2025-11**
   (rentetan 5). Tidak ada `2022-05` maupun `2024-05` di antara keenamnya.

Keputusan 9 ADR-A019 dengan demikian mengandung **dua** cacat pada satu
rumusan. Urutan porosnya tetap berlaku setelah dikoreksi (keputusan 9 di bawah);
kesembilan syarat kumulatifnya tidak tersentuh dan tetap berlaku penuh.

## Keputusan 9 — urutan poros diperbarui

1. **Irisan 880 lawan 877** — naik ke peringkat pertama. Satu pembacaan
   `reports/silang_funding.json` (`b61fe8b3`). Dasar: jurnal 142 §4 menunjukkan
   seluruh selisih 3 duduk di kelas *awal* (48 − 45 = 3; 826 − 826 = 0;
   6 − 6 = 0), tinggal dikonfirmasi dari laporan.
2. **Sebab TLMUSDT 2023-03** — tetap.
3. **"Bulan pertama di penyebut" lawan "di bursa"** — tetap.
4. **Tebing `2025-07` dan BTCSTUSDT** — naik nilainya: kedua nama itu kini
   muncul pada tabel lubang tengah, dan `2025-07` adalah bulan pertama rentetan
   LITUSDT sekaligus tebing yang sudah dikenal. Keseriannya **belum** diukur.
5. **Identitas 12 simbol-bulan karantina** — turun ke peringkat kelima;
   menuntut modul CI.
6. Sisanya tetap seperti ADR-A019 kep. 9.

Poros **lubang tengah** dinyatakan **TUNTAS** dan dikeluarkan dari daftar.

## Keputusan 10 — utang aturan 52 dan penomoran

Berkas ini wajib dibaca ulang UTUH pada giliran yang sama dan blob-nya dicatat.
ADR berikutnya: **A021**. Berkas akar yang menunggu: **STATE v56** (papan skor
316, dua pencabutan, KC-53, aturan 86 butir b, usulan 87) dan **UKUR v15**
(aturan 38 ke-51, blob `39cd1caa`, temuan jurnal 142 §4, adjudikasi pertama
aturan 85).
