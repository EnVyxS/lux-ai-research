# ADR-A008 — Kebijakan menghadapi KC-18: pasar mati dilabeli, bukan dijatuhkan diam-diam

- **Status**: **DITERIMA** 2026-07-29 untuk Keputusan 1–6. Keputusan 7 (nasib
  ADR-A002 §10) sengaja DITANGGUHKAN dan alasannya ditulis di §5.
- **Tanggal**: 2026-07-29
- **Tidak mengamandemen apa pun.** ADR-A002 §10 tidak disentuh; ADR-A004 §2
  (gerbang struktural 1m) tidak disentuh; ADR-A006 (larangan penambalan) tidak
  disentuh.
- **Bukti pemicu**: jurnal 73, 74, 75, 76, 77;
  `reports/kohort_ekor_ringkas.json` run `30416845475` commit `387037a9`,
  `sidik_kode` `73ca4eb2…`.

## 1. Masalah

**KC-18.** Arsip menerbitkan berkas klines 1m yang lengkap dan sah secara BENTUK
untuk pasar yang tidak diperdagangkan: 43.200 lilin sebulan, stempel waktu rapat
tanpa satu menit pun hilang, checksum resmi cocok — namun `volume` dan `count`
nol pada SELURUH lilin. Gerbang 1m (ADR-A004 §2) meloloskannya karena kelima
klausanya menilai BENTUK deret, bukan KEHIDUPAN pasar.

Yang terukur, dan hanya ini:

| pengukuran | angka | sumber |
| --- | --- | --- |
| lilin kosong yang lolos gerbang | 864.000 pada 20 simbol-bulan | jurnal 74 |
| simbol-bulan sepi pada pindaian adaptif | 169 dari 179 diunduh, 10 simbol | jurnal 77 |
| simbol yang berhenti diperdagangkan sebelum tebing funding | 10 dari 10 terukur | jurnal 77 |
| rentang bulan hidup terakhir | 2024-06 sampai 2025-04, sembilan bulan berbeda | jurnal 77 |

Alat ukurnya terbukti melihat: kendali hidup BTCUSDT dan ETHUSDT ramai pada 4
dari 4 baris, `parser_terbukti` true (aturan 50), dan medan `kepala` yang direkam
modul menunjukkan indeks 5 memang `volume` dan indeks 8 memang `count`.

Bahayanya bukan bahwa lilin datar itu palsu. Ia bukan palsu: ia keterangan sah
bahwa tidak ada perdagangan. Bahayanya ada tiga, dan ketiganya menyerang riset
dari arah yang sama:

1. **Penyebut.** Baris kosong terhitung sebagai baris sah di semesta
   (839.842.134). Ukuran apa pun yang membaginya dengan "cacah baris" atau
   "cacah simbol-bulan" diam-diam memasukkan pasar mati ke penyebut, sehingga
   cakupan tampak lebih besar daripada kenyataannya.
2. **Rezim palsu.** Deret harga yang datar sempurna selama berbulan-bulan adalah
   rezim volatilitas nol yang tidak pernah dialami pedagang mana pun. Strategi
   apa pun yang tidak membuka posisi di sana akan tampak "tidak rugi", dan
   strategi yang membuka posisi akan tampak mengisi pada harga yang tak pernah
   dapat diisi.
3. **N palsu.** Menambah simbol-bulan mati ke dalam sampel menambah panjang
   deret tanpa menambah satu pun pengamatan pasar. Lapisan validasi (Šidák,
   permutasi, PBO, DSR) memperoleh penyebut yang lebih besar dari apa yang
   sesungguhnya diamati, dan itu melonggarkan setiap ambangnya.

## 2. Keputusan

1. **KC-18 TIDAK menjadi gerbang serapan.** Berkas berlilin datar tetap diunduh,
   tetap diverifikasi checksum-nya, tetap disimpan. Menjatuhkannya di tingkat
   serapan berarti membuang keterangan sah tentang kapan sebuah pasar mati —
   keterangan yang justru dibutuhkan untuk mengukur bias bertahan hidup.
2. **Kehidupan diukur dan DILABELI per simbol-bulan**, terpisah dari bentuk.
   Medan wajib: `cacah_lilin`, `cacah_volume_nol`, `bagian_volume_nol`,
   `transaksi_total`, `volume_total`. Definisi tunggal (aturan 1): sebuah
   simbol-bulan disebut **SEPI** bila `bagian_volume_nol` ≥ `AMBANG_SEPI`
   (0,5 sebagaimana dipakai `kohort_ekor`), dan **MATI** bila
   `transaksi_total` = 0. Kedua istilah tidak boleh dipertukarkan.
3. **Larangan penyebut diam-diam.** Setiap laporan riset yang memakai cacah
   baris, cacah simbol-bulan, atau panjang deret sebagai penyebut WAJIB
   menerbitkan pasangan angkanya: penyebut penuh dan penyebut tanpa simbol-bulan
   MATI, berdampingan (aturan 30, aturan 36). Menerbitkan satu saja adalah
   pelanggaran ADR ini.
4. **Backtest berjalan pada simbol-bulan HIDUP saja**, dan pemotongan itu wajib
   dilaporkan sebagai angka, bukan disembunyikan di dalam kode. Alasannya sama
   dengan ADR-A002 §4 tentang karantina 7 hari: bar yang tidak dapat
   diperdagangkan tidak boleh menghasilkan keuntungan di atas kertas.
5. **Larangan ekstrapolasi (aturan 20).** Bentangan KC-18 yang boleh dikutip
   hanya yang tercantum di §1. Perkalian 456 × 43.200 DILARANG ditulis sebagai
   angka terukur. Sampel yang ada adalah 10 dari 38 anggota kohort, dipilih
   menurut abjad — sistematis, bukan acak.
6. **Kebangkitan tetap terbuka.** Pindaian adaptif berhenti pada bulan ramai
   pertama, sehingga `bangkit_kembali` tidak dapat digugurkan olehnya
   (`cacah_simbol_bangkit_dapat_diuji` = 0, aturan 46). ADR ini TIDAK menyatakan
   bahwa pasar mati tetap mati. Setiap pemakaian label MATI wajib bersifat per
   simbol-bulan, tidak pernah per simbol.
7. **DITANGGUHKAN**: apakah ADR-A002 §10 diubah. Lihat §5.

## 3. Yang ditolak

- **Menjatuhkan berkas berlilin datar di gerbang 1m.** Ditolak: gerbang menilai
  integritas struktural, dan mencampurkan penilaian kehidupan ke dalamnya
  membuat satu medan gagal karena dua sebab yang berbeda — persis cacat yang
  aturan 24 dan aturan 46 lawan.
- **Membiarkan lilin datar ikut ke backtest apa adanya.** Ditolak, §1 butir 2
  dan 3.
- **Menghapus baris kosong dari cacah semesta 839.842.134.** Ditolak: angka itu
  sudah diterbitkan, diverifikasi ulang dari luar runner, dan dipakai sebagai
  patokan di belasan laporan. Yang benar adalah menerbitkan penyebut KEDUA di
  sampingnya (Keputusan 3), bukan menulis ulang yang pertama (aturan 29).
- **Menyimpulkan bahwa arsip funding cacat.** Ditolak, §5.
- **Menyimpulkan bahwa ke-38 anggota kohort mati.** Ditolak, aturan 20: yang
  terukur sepuluh.

## 4. Akibat yang diakui

- Cacah simbol-bulan yang benar-benar dapat dipakai riset akan LEBIH KECIL
  daripada 19.598, dan besarnya belum diketahui. Ini kabar buruk yang lebih baik
  diketahui sekarang daripada sesudah sebuah hipotesis diadjudikasi.
- Pengukuran kehidupan menuntut membaca kolom `volume` dan `count` pada seluruh
  semesta, bukan hanya pada 10 simbol. Itu run tersendiri dan biayanya nyata.
- Setiap laporan bertambah satu pasang angka penyebut. Itu memang maksudnya.

## 5. Mengapa ADR-A002 §10 TIDAK disentuh

§10 memerintahkan simbol-bulan `funding_ada: false` dikeluarkan dari backtest.
Kekhawatiran yang berdiri sejak jurnal 70: aturan itu memotong 456 simbol-bulan
kohort — 51,8% dari seluruh 880 lubang — tepat di ekor sejarah, yang merupakan
bias bertahan hidup dalam bentuknya yang paling murni.

Temuan jurnal 77 MELEMAHKAN kekhawatiran itu tanpa membatalkannya: pada sepuluh
anggota yang terukur, bulan-bulan yang akan dipotong §10 memang bulan-bulan
ketika pasarnya sudah mati. Memotong bulan mati bukan memotong sejarah yang
berharga.

Tetapi tiga hal melarang saya menutup soal ini sekarang:

1. Sepuluh dari tiga puluh delapan. Aturan 20.
2. Arah sebab masih dua kemungkinan. Perdagangan berhenti bertahap (2024-06
   sampai 2025-04) sementara funding berhenti serempak (2025-07). Itu cocok
   dengan pembersihan administratif, dan sama-sama cocok dengan penghentian
   penerbitan yang tertunda. Keduanya meramalkan data yang sama. Arsip funding
   TIDAK terbukti cacat.
3. §10 tidak hanya menyentuh kohort. Ia menyentuh 880 lubang, termasuk 48 lubang
   awal dan 6 lubang tengah yang sebabnya sama sekali belum diukur — dan lubang
   tengah pada pasar yang HIDUP adalah kasus yang sepenuhnya berbeda.

Karena itu keputusan atas §10 menunggu dua pengukuran: bentangan kehidupan atas
seluruh 38 anggota kohort, dan sifat ke-6 lubang tengah. **Ini memerlukan
verifikasi.**

## 6. Apa yang membatalkan ADR ini

- Bila pengukuran kehidupan atas semesta penuh menemukan bahwa simbol-bulan MATI
  jumlahnya besar dan tersebar di TENGAH sejarah simbol yang aktif — bukan hanya
  di ekor — maka label saja tidak cukup dan kebijakan penyebut harus dinaikkan
  menjadi gerbang riset tersendiri.
- Bila ditemukan simbol-bulan dengan `transaksi_total` = 0 tetapi harga
  BERGERAK, definisi MATI di Keputusan 2 salah dan wajib ditulis ulang, bukan
  ditambal.
- Bila kendali positif gagal pada run kehidupan berikutnya (`parser_terbukti`
  false), seluruh angka di §1 batal dan ADR ini gugur bersamanya (aturan 50).
