# ADR-A007 — Serapan hibrida: bulanan sebagai dasar, harian sebagai pemulih

- **Status**: DIUSULKAN (menunggu hasil run diagnosa KC-15 tepi bulan, R-117..R-120)
- **Tanggal**: 2026-07-28
- **Menggantikan sebagian**: ADR-A002 §3 (sumber berkas serapan)
- **Bergantung pada**: ADR-A004 (berkas 1m satu-satunya kebenaran), ADR-A006 (karantina, larangan penambalan sintetis)
- **Bukti pemicu**: jurnal 51; `reports/diagnosa_kc14c.json` run `30367836338`

## 1. Konteks

ADR-A002 §3 memilih berkas klines **bulanan** sebagai sumber serapan, dengan
alasan efisiensi: satu permintaan HTTP per simbol-bulan, bukan tiga puluh.
Alasan itu masih benar. Premis yang menyertainya ternyata tidak.

Premis yang gugur: "berkas bulanan memuat seluruh baris yang ada di berkas
harian bulan itu". Terukur pada tiga simbol-bulan (KC-15, jurnal 51):

| simbol-bulan | hari yang lenyap dari bulanan | baris di harian |
|---|---|---|
| BNXUSDT 2022-04 | 2022-04-17 | 1.440 |
| BNXUSDT 2022-06 | 2022-06-09 | 1.440 |
| BNXUSDT 2022-08 | 2022-08-10, -11, -12 | 1.440 × 3 |

7.200 menit — lima hari UTC penuh — ada, utuh, dan checksum-nya terverifikasi di
arsip publik yang sama, tetapi tidak ada di berkas bulanan. Sembilan
simbol-bulan karantina lain diperiksa dengan cara yang sama dan lubangnya nyata
di kedua representasi (KC-14): di sana harian dan bulanan sepakat.

Gerbang ADR-A004 menangkap kedua belasnya lewat klausa `tanpa_menit_hilang`,
jadi tidak ada data cacat yang lolos diam-diam — sejauh lubangnya di TENGAH
bulan. Apakah pemotongan di TEPI bulan juga tertangkap sedang diukur; bila
tidak, ADR ini bertambah satu klausa gerbang.

## 2. Keputusan

1. Berkas **bulanan** tetap sumber dasar serapan. Tidak ada perubahan pada jalur
   normal, dan tidak ada 30× permintaan HTTP untuk 19.598 simbol-bulan.
2. Bila dan hanya bila gerbang menjatuhkan sebuah simbol-bulan karena
   `tanpa_menit_hilang` atau `jarak_60_detik`, jalankan **pemulihan harian**:
   unduh berkas harian untuk tanggal-tanggal yang terdampak lubang, verifikasi
   checksum-nya, lalu gabungkan barisnya.
3. Simbol-bulan hasil gabungan **dinilai ulang oleh gerbang yang sama, tanpa
   pelunakan ambang**. Bila lolos, ia masuk data utama; bila masih jatuh, ia
   tetap karantina. Ambang gerbang tidak boleh diturunkan untuk
   mengakomodasi pemulihan (ADR-A006, aturan 23).
4. Setiap baris membawa asal-usulnya: medan `sumber_baris` bernilai `bulanan`
   atau `harian`. Manifes memuat `cacah_baris_dipulihkan`,
   `cacah_hari_dipulihkan`, dan `cacah_simbol_bulan_dipulihkan`.
5. Manifes memuat medan penggugur `cacah_pemulihan_gagal_checksum`, yang wajib
   nol. Baris tanpa checksum terverifikasi TIDAK BOLEH masuk, walau itu berarti
   simbol-bulan tetap karantina.

## 3. Mengapa ini bukan pelanggaran ADR-A006

ADR-A006 melarang interpolasi, forward-fill, dan penurunan ambang gerbang.
Pemulihan dari berkas harian bukan salah satunya:

- ia tidak mengarang nilai; barisnya adalah baris arsip asli;
- ia punya checksum sendiri dari penerbit yang sama, diverifikasi sebelum dipakai;
- ia tidak menurunkan ambang; gerbang dijalankan ulang utuh;
- ia dapat diaudit; `sumber_baris` membuat tiap baris pulihan dapat dilacak dan
  dibuang kembali bila kelak terbukti berbeda.

Perbedaan yang menentukan: ADR-A006 melarang **menciptakan** data yang tidak
ada. ADR-A007 mengambil data yang **memang ada** dari representasi lain arsip
yang sama.

## 4. Yang ditolak

- **Pindah seluruhnya ke berkas harian.** ≈30× permintaan dan ≈30× berkas untuk
  19.598 simbol-bulan, demi memperbaiki 3 di antaranya (0,015%). Ditolak
  sebagai harga yang tidak sebanding — dan lubang KC-14 tidak ikut sembuh.
- **Membuang ketiga bulan BNXUSDT.** Ini pembuangan data yang tersedia dan utuh;
  justru yang ADR-A006 lawan.
- **Menambal 7.200 menit dengan interpolasi.** Dilarang ADR-A006, dan tidak ada
  alasan menambal ketika data aslinya bisa diunduh.
- **Menurunkan ambang gerbang agar ketiganya lolos.** Ini akan meloloskan juga
  sembilan lubang KC-14 yang nyata. Dilarang, aturan 23.

## 5. Akibat yang diakui

- Jalur pemulihan hanya berjalan pada simbol-bulan karantina, sehingga biayanya
  terikat pada cacah karantina (12 dari 19.598 sejauh terukur). Bila cacah itu
  meledak pada semesta lain, kebijakan wajib ditinjau ulang, bukan diperbesar
  diam-diam.
- Waktu tempuh serapan bertambah hanya untuk simbol-bulan karantina.
- Kode bertambah satu jalur bercabang, yang berarti bertambah satu tempat cacat
  bisa bersembunyi. Karena itu `sumber_baris` wajib, bukan opsional.

## 6. Yang masih belum diketahui

- Sebab KC-15 tidak diketahui. Ketiga kasusnya BNXUSDT 2022, satu-satunya simbol
  pra-2023 di antara dua belas karantina dan satu-satunya yang berulang. Apakah
  KC-15 khas simbol tertentu, khas tahun 2022, atau tersebar merata: belum
  terukur. Ini memerlukan verifikasi.
- Apakah pemotongan tepi bulan lolos gerbang: sedang diukur (R-117..R-120).
  Bila lolos, ADR ini perlu klausa gerbang ketujuh yang membandingkan tepi bulan
  TENGAH terhadap kalender, dan pemulihan harian ikut berlaku untuk tepi.
- Sebab sembilan lubang KC-14 yang semuanya mulai 00:00 UTC dan semuanya
  kelipatan 15 menit tetap tidak diketahui. ADR ini tidak mengklaim
  menjelaskannya.
