# ADR-A010 — Membuka kembali ADR-A009 dan mencabut "kebangkitan tunggal"

- **Tanggal:** 30 Juli 2026
- **Status:** **DITERIMA**
- **Bergantung pada:** ADR-A008 (§6 pembatal pertama), ADR-A009 (arah sebab),
  ADR-A003 (kelas kebangkitan)
- **Bukti:** `reports/tersisip_semesta.json` blob
  `911acd1c730a677dd8c7100655313f5bf3d1f6e3`, run 30514239872, commit
  `25106dd51ed8295b58d3d63c93dc0b78cad00428`, kode keluar 0, terbaca UTUH
- **Adjudikasi:** jurnal 124 §4 (R-303 TEPAT), praregistrasi jurnal 123 §5

---

## 1. Konteks

ADR-A009 diterima satu giliran lalu atas dasar SATU kebangkitan terukur
(LITUSDT) ditambah dua nol `mati_tersisip` pada dua penyebut kecil: dua lubang
funding tengah, dan 38 anggota kohort puncak 2025-07. Pada saat itu §6 ADR-A008
mencatat pembatal pertama yang "belum pernah menyala", dan jurnal 123 §5
mempraregistrasi bahwa bila pembatal itu menyala pada semesta, A009 WAJIB dibuka
kembali.

## 2. Pengukuran yang memaksa keputusan ini

Atas seluruh 19.586 simbol-bulan pada 787 simbol:

- **8 simbol** punya bulan MATI yang terapit HIDUP di kedua sisi;
- **88 simbol-bulan** tersisip, dari 1.401 MATI;
- **0 dari 88** sisipan berbentuk lubang satu bulan berselang-seling
  (`tersisip_rapat` = 0), dengan detektor rapat terbukti menyala pada kendali
  positif;
- pada **8 dari 8**, seluruh bulan MATI membentuk SATU blok berurutan yang
  seluruhnya terapit HIDUP: bentuknya HIDUP → blok MATI → HIDUP, sekali saja;
- panjang blok: 2, 2, 8, 10, 11, 13, 13, 29 bulan.

## 3. Keputusan

1. **Pembatal pertama §6 ADR-A008 dinyatakan MENYALA.** Ia tidak lagi boleh
   disebut "pembatal yang belum pernah menyala", dan tidak boleh dicabut sebagai
   pembatal yang mustahil menyala.
2. **ADR-A009 DIBUKA KEMBALI.** Arah sebab "mati dulu, funding kemudian" tidak
   dicabut, tetapi statusnya turun dari keputusan yang berlaku menjadi keputusan
   yang MENUNGGU pengukuran berpasangan. R-304 adalah pengujinya.
3. **Klaim "kebangkitan adalah kejadian tunggal pada satu simbol" DICABUT.**
   Kebangkitan terukur pada 8 simbol dari 787. LITUSDT bukan satu-satunya; ia
   hanya yang pertama terlihat, karena alat sebelumnya hanya mampu melihatnya.
4. **ADR-A003 (kelas kebangkitan) wajib memuat delapan simbol**, dengan panjang
   blok mati sebagai medan kelas, bukan satu contoh.
5. **Kata "serentak" tetap DITOLAK.** Tidak ada pengukuran yang mendukungnya, dan
   penolakan itu tidak bergantung pada pembatal yang baru menyala ini.
6. **Bentuk kebangkitan yang terukur adalah BLOK TUNGGAL, bukan kedip.** Tidak
   ada satu pun simbol yang mati-hidup-mati-hidup berselang bulanan. Setiap
   pernyataan yang menyebut "kedipan" atau "berselang-seling" harus ditulis
   sebagai TIDAK TERUKUR.

## 4. Yang TIDAK diputuskan

- Apakah kematian mendahului berhentinya funding pada kedelapan simbol. Baru satu
  simbol (LITUSDT, 5 bulan) yang terukur berpasangan. Sisanya belum, dan aturan
  20 melarang saya menyamaratakan dari satu.
- Mengapa `tersisip_rapat` nol. Bisa jadi ciri pasar, bisa jadi ciri gerbang
  bulanan yang tidak mampu memuat kedip sependek satu bulan. Belum diukur.
- Apakah delapan adalah cacah akhir. Ia cacah pada penyebut 19.586 simbol-bulan
  yang LOLOS gerbang; 12 simbol-bulan karantina dan 150 nama hanya-arsip tidak
  ikut diukur, dan ketiadaan pengukuran bukan ketiadaan gejala (aturan 59).

## 5. Pembatal keputusan ini

ADR-A010 batal bila salah satu terjadi:

1. Terukur ada simbol dengan DUA blok mati terapit HIDUP terpisah (kematian
   berulang) — maka "blok tunggal" pada §3.6 salah.
2. Terukur ada `tersisip_rapat` > 0 pada penyebut mana pun dengan detektor sah —
   maka "bukan kedip" pada §3.6 salah.
3. `cacah_simbol_bangkit` berubah dari 8 pada penyebut 19.586 yang sama dengan
   sidik laporan kehidupan `24b6bb26…` — maka salah satu dari dua pengukuran
   cacat dan keduanya harus diulang.
4. R-304 butir 1 KALAH — maka §3.2 tidak cukup dan arah sebab ADR-A009 dicabut,
   bukan hanya dibuka.
