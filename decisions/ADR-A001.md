# ADR-A001 — Aturan dasar riset lux-ai-research

Status: DITERIMA. Tanggal: 2026-07-28. Menggantikan: tidak ada.

## Konteks

Dua jalur riset sebelumnya kehilangan waktu karena membangun di atas pemahaman
yang keliru dan mengejar angka yang lahir dari kebocoran seleksi. Modul warisan
adalah contoh hidupnya: `AUDIT.md` memilih default berdasarkan performa di paruh
uji (terverifikasi, lihat `PETA_MODUL.md` §6 butir F).

## Keputusan

### 1. Definisi R (tunggal, mengikat)

Satu R = jarak entry ke stop-loss AWAL dikali qty, dalam USD, diukur SEBELUM
biaya. Fee, funding, dan slippage dikurangkan DARI hasil, tidak pernah dilipat ke
dalam penyebut R. Laporan dengan definisi lain tidak sebanding dan ditolak.

### 2. Gerbang KANDIDAT

Seluruh butir wajib terpenuhi dan dipra-registrasi sebelum run:

1. Ekspektasi bersih >= 0,05R per transaksi setelah fee, funding, dan slippage
   yang selalu merugikan.
2. Minimal 100 transaksi per sel, di seluruh sel yang diuji.
3. p <= 0,05 pada uji bulanan berpasangan (bulan UTC), dengan koreksi Sidak atas
   N_percobaan berjalan.
4. Bertahan terhadap permutasi entri acak >= 300 ulangan, pengacakan PER TANGGAL
   UTC (sebab ada ketergantungan lintas simbol: `risk.btc_correlation_block`,
   terverifikasi).
5. PBO < 0,50 dan DSR > 0,95. PBO memerlukan grid yang seluruh titiknya
   dideklarasikan di muka sebagai satu keluarga percobaan. Grid yang diperluas
   setelah melihat hasil membatalkan seluruh sel.
6. Tidak ada invarian risiko yang jebol: tidak ada transaksi rugi melampaui
   -1,5R, checksum konsisten, tidak ada gerbang pengaman yang mati diam-diam.
7. Lolos di minimal dua rezim yang dideklarasikan di dalam pra-registrasi.
   **DITANGGUHKAN sampai ADR-A003 memaku taksonomi rezim.** Hipotesis mana pun
   yang mengklaim lulus sebelum itu wajib menyebut penangguhan ini di laporannya.

Tidak lulus = DITOLAK. Ditolak adalah keluaran yang sah dan murah.

### 3. Determinisme

- Benih acak dipatok dan dicatat di setiap laporan.
- Urutan simbol selalu terurut; tidak ada iterasi atas himpunan tak terurut.
- Versi pustaka dipatok di `requirements.txt` dan dicatat di setiap laporan.
- Setiap `reports/*.json` wajib memuat `sidik_kode` (hash modul terlibat) dan
  `sidik_data` (hash manifes dataset). Dua laporan dengan `sidik_data` berbeda
  TIDAK SEBANDING dan dilarang dibandingkan.
- DSR dan PBO ditulis dengan numpy murni; runner tidak punya scipy.
- Setiap run berpotensi >30 menit wajib menulis `reports/<nama>_progres.json`
  secara berkala dan meng-commit-nya.

### 4. N_percobaan

Satu sel yang melewati gerbang = 1. Pra-saring = 0. Setiap retrain = 1. Grid
yang dipra-registrasi = jumlah titiknya. Angka berjalan disimpan di
`STATE_LAMPIRAN_ANGKA.md`; ambang Sidak dihitung ulang setiap kali ia naik.

### 5. Batas LLM

LLM dilarang berada di jalur keputusan. Ia tidak memilih entry, tidak menyetel
ambang, tidak memilih strategi, tidak menilai setup, tidak menulis putusan.
Penegakan: uji yang gagal bila `lux_ai/backtest/` atau `lux_ai/sinyal/`
mengimpor `lux_ai/antarmuka/`, langsung maupun transitif.

### 6. Isolasi

Tidak menulis apa pun ke `lux-research` maupun `lux-scalp-research`, dan tidak
mengutip angka dari keduanya sebagai bukti. Papan skor mulai dari nol.

### 7. Larangan atas modul warisan

`backtest.py` modul tidak dipakai. Angka apa pun dari modul adalah klaim, bukan
bukti. Nol koneksi ke bursa.

## Konsekuensi

Riset ini lambat di awal dan mahal dalam disiplin pencatatan. Imbalannya: setiap
angka yang lolos punya asal-usul yang dapat ditelusuri, dan penolakan menjadi
murah.
