# ADR-A004 — Kebijakan menghadapi KC-6: berkas 1m sebagai satu-satunya sumber

Status: **DITERIMA** 2026-07-28. Mengamandemen ADR-A002 §3.
Dasar angka: `reports/diagnosa_kc6.json` (run 30338666516) dan
`reports/rentang_kc6.json` (run 30339979270), keduanya bertanda
`"bukan_bukti": true` — dipakai di sini sebagai dasar KEPUTUSAN, bukan sebagai
bukti hipotesis riset.

## 1. Masalah

Berkas 1m dan berkas 5m/15m terbitan Binance tidak sepakat. Yang terukur:

| Fakta | Angka | Sumber |
|---|---|---|
| Bucket `open` beda, 12 bulan pertama | 468 dari 91.335 | diagnosa_kc6 |
| Bucket `open` beda, 84 simbol-bulan (6 awal + kendali) | 2.530 | rentang_kc6 |
| Bucket beda di bulan kendali (tengah hidup simbol) | 1 (LINKUSDT 2023-04) | rentang_kc6 |
| Bucket beda yang punya menit 1m hilang | 0 | keduanya |
| Simbol-bulan dengan menit hilang atau duplikat | 0 dari 84 | rentang_kc6 |
| Beda terbesar yang tercatat | ~3% (XRPUSDT 2020-01: 0,1970 lawan 0,2032) | uji_resample |

H1 (deret 1m berlubang) GUGUR. Yang tersisa: kedua produk dibangun dari agregasi
yang berbeda di sisi Binance, dan kami tidak punya cara mengukur mana yang
benar. `fapi.binance.com` memberi 451, jadi tidak ada wasit independen.

## 2. Keputusan

1. **Berkas 1m adalah satu-satunya sumber kebenaran.** Seluruh kerangka waktu
   yang lebih besar diturunkan dengan resample dari 1m. Berkas 5m/15m terbitan
   Binance TIDAK diserap dan tidak boleh masuk jalur riset mana pun.
2. **Gerbang serapan yang MENGIKAT berpindah** dari "hasil resample sama dengan
   5m/15m terbitan" menjadi **integritas struktural deret 1m** per simbol-bulan:
   0 stempel duplikat; 0 menit hilang di dalam rentang berkas; seluruh jarak
   antar-baris tepat 60 detik; seluruh stempel selaras batas menit; satuan
   stempel milidetik. Kelima klausa ini terukur 100% bersih pada 84 simbol-bulan
   yang disampel.
3. **Perbandingan dengan 5m/15m terbitan tetap dijalankan, sebagai DIAGNOSTIK**
   bertanda `"bukan_bukti": true`. Ia dilaporkan, tidak pernah meloloskan dan
   tidak pernah menjatuhkan serapan.
4. **Tidak ada toleransi numerik.** Ambang yang menampung beda 3% akan menampung
   pergerakan harga sungguhan; gerbang seperti itu berhenti mengukur apa pun.
5. **Tidak ada pengecualian "N bulan pertama".** Tidak ada N yang aman: pada
   N = 6 DOGEUSDT masih 202 dan BTSUSDT masih 8, dan bulan kendali LINKUSDT
   2023-04 — jauh di luar masa awal — masih 1.
6. **Kewajiban pelaporan.** Setiap hasil riset yang memakai bar 5m/15m wajib
   menyatakan bahwa barnya DITURUNKAN dari 1m. Membandingkan angka kami dengan
   angka pihak lain yang memakai berkas 5m/15m terbitan adalah membandingkan dua
   semesta yang berbeda, dan perbandingan seperti itu dilarang dipakai sebagai
   pembenaran.

## 3. Amandemen ADR-A002 §3

ADR-A002 §3 menetapkan kesamaan eksak dengan berkas 5m/15m terbitan sebagai
syarat serapan. Klausa itu **dicabut sebagai gerbang** dan diturunkan menjadi
diagnostik (§2 dan §3 di atas). Alasannya terukur, bukan demi kenyamanan:
syarat lama menuntut kesamaan dengan produk yang dibangun dari agregasi lain,
sehingga ia mengukur kesepakatan antar-produk Binance, bukan mutu data kami.
Berkas `decisions/ADR-A002.md` belum diberi catatan silang; itu utang 22.

## 4. Alternatif yang ditolak

- **Toleransi harga** — ditolak, lihat §2.4.
- **Mengecualikan N bulan pertama** — ditolak, lihat §2.5. Ini pilihan yang
  paling saya harapkan sebelum run, dan ia gugur oleh datanya sendiri.
- **Mengkarantina bulan bermasalah lalu memutuskan belakangan** — ditolak:
  daftar karantina yang tidak punya kriteria selesai akan berubah menjadi
  daftar pengecualian permanen yang tidak pernah diaudit.
- **Memakai 5m/15m ASLI untuk bulan awal** — ditolak: mencampur dua agregasi
  yang berbeda di dalam satu deret waktu menciptakan diskontinuitas buatan tepat
  di titik sambungnya, dan diskontinuitas itu akan tampak seperti sinyal.

## 5. Apa yang membatalkan ADR ini

- Bila serapan penuh menemukan simbol-bulan 1m yang melanggar §2 dalam jumlah
  besar (lihat R-36 dan R-37), premis "arsip 1m utuh" runtuh dan ADR ini harus
  ditulis ulang, bukan ditambal.
- Bila kelak ada sumber independen yang menunjukkan 5m/15m terbitan lebih benar
  daripada 1m, seluruh pilihan §2.1 harus dinilai ulang. Saat ini pertanyaan itu
  **memerlukan verifikasi** dan tidak dijawab oleh ADR ini.
