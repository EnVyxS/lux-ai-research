# ADR-A009 — Arah sebab antara kematian perdagangan dan berhentinya funding

- **Status:** DITERIMA, 30 Juli 2026 (jurnal 123).
- **Menggantikan:** Keputusan 7 ADR-A008 yang selama ini DITANGGUHKAN karena
  prasyarat terakhirnya belum lunas.
- **Bahan:** `reports/bentangan_kohort.json` blob
  `6040030d3fad3ab87a89cdabefb53d2f29fe2366`, run **30509071237**, commit
  `703daa900e2aa285dc5b058592457e81fe02643f`, kode keluar 0, penyebut
  **19.586** simbol-bulan, kohort **38** simbol, kendali positif sah.

## 1. Keputusan

Untuk kohort puncak funding **2025-07**, urutan kedua gejala **terukur dan searah**:
**perdagangan berhenti LEBIH DAHULU, penerbitan funding berhenti KEMUDIAN.**

Angkanya: **38 dari 38** anggota memiliki bulan HIDUP terakhir yang lebih awal
daripada tebing 2025-07, dengan jarak **3 sampai 37 bulan** (ALPACAUSDT 3 bulan
yang tercepat, SCUSDT 37 bulan yang terlama). Seluruh 38 anggota punya sedikitnya
**5** bulan HIDUP (STRAXUSDT 5 dari 33; BALUSDT dan OMGUSDT 55), dan seluruh 38
punya bulan terakhir **2026-06**, sehingga nol pada `cacah_simbol_hidup_sesudah_tebing`
lahir dari pengukuran, bukan dari ketiadaan bahan (aturan 74).

Bukti kedua dari semesta lain: kematian **LITUSDT** mendahului berhentinya
funding-nya **5 bulan** (H-A017, jurnal 120).

## 2. Kata yang DITOLAK

Kata **"serentak"** ditolak untuk menyebut hubungan kematian pasar dengan tebing
funding. Yang serentak hanyalah **penerbitan funding antar-simbol** — 38 simbol
berhenti menerbitkan funding pada bulan yang sama. Kematian perdagangan mereka
**tidak** serentak: ia tersebar dari 2022-06 sampai 2025-04, rentang 35 bulan.
Menyebut keduanya "serentak" mencampur dua sumbu yang berbeda dan itulah kekeliruan
yang ADR ini dibuat untuk menutup.

## 3. Yang TIDAK diputuskan

- **Irisan bukan sebab (aturan 10).** ADR ini menetapkan **URUTAN WAKTU**, bukan
  mekanisme. Bahwa mati mendahului funding tidak membuktikan kematian MENYEBABKAN
  penghentian penerbitan; satu delisting yang diproses bertahap muat sama baiknya
  dengan data ini.
- **Rentang (aturan 20).** Keputusan ini berlaku bagi 38 anggota kohort puncak dan
  dua pemilik lubang tengah yang sudah dibentangkan. Ia **tidak** dinyatakan bagi
  787 simbol semesta, dan tidak bagi lubang funding jenis AWAL.
- **Arsip funding tidak dinyatakan cacat.** Penerbitan yang berlanjut selama
  berbulan-bulan sesudah pasar mati (BTCSTUSDT: nol bulan HIDUP dari 64 padahal
  funding-nya terbit) menunjukkan penerbitan funding **bukan tanda kehidupan
  perdagangan** — itu sifat arsip, bukan kerusakannya.

## 4. Akibat mengikat

1. Setiap tafsir yang memakai tebing funding sebagai penanda peristiwa pasar pada
   bulan itu **batal**; tebing funding adalah peristiwa PENERBITAN.
2. `funding_ada` dan turunannya **tidak boleh** dipakai sebagai gerbang kehidupan
   di manifes mana pun.
3. Setiap laporan yang menyebut kohort 2025-07 wajib menyertakan jarak bulan antara
   bulan hidup terakhir dan tebing, bukan hanya keanggotaannya.

## 5. Pembatal (aturan 24) — apa yang membuka kembali ADR ini

- Satu saja anggota kohort puncak terbukti berlabel HIDUP pada 2025-07 atau
  sesudahnya.
- `mati_tersisip` atas seluruh 19.586 (R-303) menemukan kematian yang
  berselang-seling dalam jumlah berarti, sebab kematian yang bolak-balik tidak muat
  dengan urutan sekali-dan-seterusnya yang menjadi dasar ADR ini.
- Ditemukan simbol yang funding-nya berhenti LEBIH DAHULU daripada kematiannya
  dengan selisih di luar galat bulanan.

## 6. Catatan penguat, bukan pembuktian

Seluruh 38 anggota berbentuk **monoton**: satu rentetan HIDUP lalu satu rentetan
MATI, `cacah_mati_tersisip` **0 dari 38**, dan `rentetan_mati_terpanjang` sama
dengan `cacah_mati` pada 38/38. Bentuk monoton itu muat dengan arah sebab di §1,
tetapi ia lahir dari semesta yang sama, jadi ia **bukan** bukti bebas. Ujian bebasnya
adalah R-303 atas 19.586.
