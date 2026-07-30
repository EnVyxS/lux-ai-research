# ADR-A016 — Keputusan sesudah R-309 (H-A019)

- Tanggal: 2026-07-30
- Status: DITERIMA
- Sumber ukur: `reports/bulan_pertama.json` blob
  `0a2aa6ae15d949b44803dffdc9e97dbd322bbc85`, run 30532058657, kode 0,
  commit `09ce9853ccf6e077bad1038df35508f59f105a3e`.
  Sidik kode modul `0d3530f69ad51a22e038c17616411b56e4518698ff14c9b635131ec1e2a66562`.
  CI 1233 butir, kode 0, blob `0489d71101e451efe73d20fd8fe75ba6d41c5c27`.
- Jurnal terkait: 130 (blob `d4c48ae45a6fbeffdf473824f3fa69f6506ed909`).
- ADR sebelumnya yang bersambung: A015 (kep. 5 melarang besar berkas dipakai
  sebagai detektor status).

## Konteks

R-308 menemukan zona 22.440–97.634 byte berisi 38 baris HIDUP dan nol baris
MATI. H-A019 mengusulkan bahwa berkas kecil menandai bulan SEBAGIAN — bulan
pertama pencatatan simbol, atau bulan tepi jendela `2026-06`. R-309 mengujinya
dengan praregistrasi terkunci dan menang bulat: butir 1 = 37 dari 38 (pita
22..38), butir 2 nisbah 0,527179 (pita 0.10..0.60), butir 3 seluruh kendali
sah.

Kemenangan bulat itu justru yang menuntut ADR ini, karena tiga hal yang
terbaca dari laporannya tidak boleh larut ke dalam kata "menang".

## Keputusan

**1. H-A019 DITERIMA TERBATAS, sebagai irisan asimetris, bukan sebab.**
Rumusan resmi yang boleh dikutip: *hampir setiap baris HIDUP di zona byte kecil
adalah bulan pertama simbol itu di dalam penyebut (37 dari 38), sementara
hampir setiap bulan pertama BUKAN berkas kecil (37 dari 787, sekitar 4,7%).*
DILARANG mengutipnya sebagai "berkas kecil disebabkan oleh bulan pertama" atau
sebagai "bulan pertama menghasilkan berkas kecil" (aturan 10).

**2. Klausa `2026-06` DICABUT dari rumusan H-A019.** Ketiga baris tepi
(SQQQUSDT, TQQQUSDT, MVLLUSDT) juga bulan pertama simbolnya; menghapus klausa
tepi tidak mengubah cacah 37. Klausa itu menyumbang NOL secara bebas dan
karena itu tidak boleh ikut dipakai sebagai penjelas. Hipotesis turunan mana
pun yang memakai "bulan tepi" harus mengujinya sendiri dari nol.

**3. Usulan aturan 84 DIAJUKAN** (resmi menyusul di STATE v49): butir
praregistrasi yang memakai klausa ATAU wajib melaporkan sumbangan BEBAS setiap
klausa secara terpisah, bukan hanya cacah gabungannya. Tanpa itu, klausa yang
tidak bekerja bersembunyi di balik klausa yang bekerja, dan butir yang menang
menjadi tidak dapat ditafsirkan. R-309 lolos dari cacat ini hanya karena
modulnya kebetulan menyimpan medan `pertama` dan `tepi` per baris.

**4. Koreksi resmi terhadap jurnal 129 §H-A019.** Di sana empat baris disebut
"tampak bulan tengah" dan diperkirakan melawan hipotesis. Terukur: MTLUSDT
2021-03, ENJUSDT 2020-09, dan SLPUSDT 2023-10 justru bulan PERTAMA simbolnya.
Satu-satunya yang benar-benar melawan adalah TLMUSDT 2023-03 (80.394 byte).
Tiga dari empat dugaan itu SALAH dan dicabut.

**5. `total_byte` WAJIB dihitung dari jalur langsung.** Praktik `irisan_byte`,
yang menghitung `total_byte` dari jumlah per kelas sehingga
`selisih_total_byte` menjadi turunan, TIDAK boleh ditiru lagi. Modul baru
mengikuti `bulan_pertama.total_byte_langsung`. Setiap laporan wajib menyebut
cacah pemeriksaan BEBAS apa adanya, dan wajib menyatakan bila dua medan
berbagi bahan baku yang sama meski jalur hitungnya berbeda. Ini menjadi isi
calon KC-50.

**6. Batas tafsir "bulan pertama" dicatat sebagai lubang ukur.** Yang diukur
adalah bulan terkecil DI DALAM penyebut 19.586 yang lolos gerbang 1m, bukan
bulan pertama perdagangan simbol di bursa. Selama keduanya belum dibandingkan,
seluruh tafsir kep. 1 berlaku hanya atas definisi penyebut.

**7. Prioritas riset berpindah ke sisi MATI.** Sisi HIDUP dari teka-teki byte
kecil kini tertutup oleh kep. 1. Pertanyaan terbuka nomor satu menjadi: APA
ISI berkas bulan MATI, yang byte minimumnya 97.634 dan rata-ratanya 413.305,781
tetapi tak satu pun jatuh ke zona kecil. Belum diukur, DILARANG ditebak.

**8. Cacah tangan pasca-trio dicatat sebagai TERHITUNG** pada ref
`010edff23f7143063fd47a5d3a077ca28c66e859`: `lux_ai/serapan/` = 47,
`tests/` = 51, `.github/workflows/` = 42. Ketiganya dicacah satu per satu dan
bernomor, cocok dengan ramalan turunannya.

## Alternatif yang DITOLAK

- **Menyatakan H-A019 "terbukti" tanpa kualifikasi.** Ditolak: nisbah 0,527
  berarti bulan pertama rata-rata hanya setengah, bukan sepersepuluh, dan
  95,3% bulan pertama tidak berada di zona kecil.
- **Melebarkan H-A019 menjadi penjelasan bagi kelas MATI.** Ditolak: tidak ada
  satu pun baris MATI di zona kecil, jadi tidak ada yang bisa dijelaskan di
  sana. Menghubungkan keduanya akan mengulangi kesalahan yang dilarang
  ADR-A015 kep. 5.
- **Membuang TLMUSDT 2023-03 sebagai pencilan.** Ditolak: satu baris yang
  melawan adalah data, bukan gangguan, dan ia menjadi pertanyaan terbuka
  nomor dua.
- **Menyusun R-310 pada giliran yang sama.** Ditolak: KC-49 menuntut hitungan
  aritmetis lebih dulu, dan konteks giliran ini sudah terpakai berat oleh
  bacaan besar. Praregistrasi yang disusun dalam keadaan lelah adalah persis
  cara dua kekalahan sebelumnya lahir.

## Konsekuensi

- STATE v49 wajib memuat: R-309 TEPAT, papan skor 309, usulan aturan 84,
  KC-50, cacah tangan 47/51/42, dan koreksi jurnal 129 di kep. 4.
- Rumusan kep. 1 adalah satu-satunya bentuk H-A019 yang boleh dikutip modul
  atau dokumen berikutnya.
- Aturan 57 kembali berjalan dari 1/1 sesudah putus di 26/27.
