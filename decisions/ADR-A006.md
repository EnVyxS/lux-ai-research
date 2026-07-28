# ADR-A006 — Nasib simbol-bulan yang dijatuhkan gerbang, dan persistensi parquet

- Status: **DITERIMA** (2026-07-28)
- Menggantikan: tidak ada. Melengkapi ADR-A002 §9 dan ADR-A004.
- Dipicu oleh: **KC-14**, terukur pada pecahan 0 (run `30353584831`).

## Konteks

Dua hal yang sebelumnya boleh ditunda kini tidak bisa lagi.

**Pertama**, ADR-A004 memutuskan gerbang 1m mengikat, tetapi diam soal apa yang
terjadi pada simbol-bulan yang GAGAL. Selama gerbang selalu 100% lolos,
kediaman itu tidak berbiaya. Pecahan 0 mengakhirinya: 3 dari 2.411 simbol-bulan
dijatuhkan (AERGOUSDT 2025-04, CVCUSDT 2025-05, SLPUSDT 2025-07), seluruhnya
pada klausa `tanpa_menit_hilang` dan `jarak_60_detik`, total **1.875 menit**
hilang.

**Kedua**, parquet pecahan 0 berukuran 4,121 GB sedangkan aset rilis GitHub
berbatas 2 GB per berkas. Sampai keputusan ini, parquet ditulis lalu dihapus:
setiap run mahal menghasilkan angka tetapi tidak menghasilkan data yang
bertahan.

## Keputusan 1 — karantina, bukan buang, bukan tambal

Simbol-bulan yang dijatuhkan gerbang **dikarantina**: tetap diserap dan tetap
dicatat penuh di manifes, tetapi **dikecualikan dari sumber data riset** dan
diberi tanda `karantina: true` beserta daftar klausa yang dilanggarnya.

Yang secara tegas DILARANG:
- **Menambal lubang** dengan interpolasi, forward-fill, atau menyambung ke
  candle berikutnya. Menit yang tidak ada bukan menit berharga terakhir.
- **Menurunkan ambang gerbang** agar simbol-bulan itu lolos. Itu bentuk lain
  dari kebijakan toleransi yang sudah dinyatakan tidak sah pada KC-6.
- **Membuang berkasnya diam-diam.** Penyebut riset wajib tetap memuatnya,
  supaya "berapa banyak data yang kami tolak" selalu bisa dijawab.

## Keputusan 2 — sebab lubang wajib diuji, bukan ditebak

Ada dua penjelasan yang sama masuk akal dan berkonsekuensi sangat berbeda:

- **H-A002a**: bursa memang berhenti mengutip (jeda perdagangan, likuiditas
  nol). Maka arsipnya benar dan lubangnya adalah fakta pasar.
- **H-A002b**: berkas arsipnya cacat atau tidak lengkap. Maka arsipnya salah
  dan premis "arsip 1m adalah kebenaran" — dasar seluruh ADR-A002 — retak.

Uji pemisahnya, wajib dijalankan sebelum serapan dinyatakan sah:
1. Unduh ulang ketiga berkas itu dan bandingkan checksum-nya dengan yang
   tercatat. Checksum sama pada dua unduhan → bukan kerusakan transportasi.
2. Bandingkan dengan berkas **5m dan 15m ASLI** bulan yang sama. Bila 5m juga
   berlubang pada slot yang sama → mendukung H-A002a. Bila 5m penuh sedangkan
   1m berlubang → **H-A002b menang dan ADR-A002 wajib ditinjau ulang seluruhnya**.
3. Periksa apakah lubangnya bersebelahan (satu blok) atau tersebar. Blok
   panjang cocok dengan jeda bursa; sebaran acak cocok dengan berkas cacat.

Medan penggugur (aturan 24): laporan uji wajib memuat panjang blok terpanjang,
cacah blok, dan hasil banding 5m walau ketiganya mendukung hipotesis yang saya
sukai. Sebelum uji ini selesai, dilarang menulis kalimat "lubang itu jeda
pasar". **Ini memerlukan verifikasi.**

## Keputusan 3 — parquet dipersistenkan sebagai aset rilis terbelah

Satu rilis per pecahan, berisi arsip `tar` yang dibelah menjadi potongan
**≤1,8 GB** (margin di bawah batas 2 GB), ditambah berkas `SHA256SUMS` untuk
seluruh potongan dan manifes pecahan yang bersangkutan. Pemulihan dilakukan
dengan menyambung potongan lalu memverifikasi checksum sebelum dibuka.

Alasan menolak alternatif:
- **Artefak run** kedaluwarsa 90 hari dan tidak bisa dirujuk stabil; riset ini
  akan hidup lebih lama dari itu.
- **Commit langsung ke repo** akan menambah puluhan GB ke riwayat git secara
  permanen dan tidak bisa dibatalkan.
- **Penyimpanan luar** memerlukan kredensial dan berada di luar batas "hanya
  menulis di repo lux-ai-research".

Konsekuensi yang diterima sadar: 8 rilis × ≈3 potongan, dan setiap serapan ulang
menghasilkan rilis baru, bukan menimpa. Nomor rilis mengikat `sidik_kode` dan
`sidik_data` agar data selalu bisa dilacak ke kode yang membuatnya.

## Konsekuensi

- `serap.ringkas` bertambah medan `cacah_karantina` dan `daftar_karantina`.
- Setiap laporan riset wajib menyebut cacah karantina; nol pun disebut.
- ADR-A002 §9 tetap berlaku selain soal persistensi, yang kini diatur di sini.
- ADR-A004 tetap berlaku; ADR ini mengisi kediamannya, tidak membatalkannya.
