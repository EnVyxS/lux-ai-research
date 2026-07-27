# STATE — versi 1

Diperbarui: 2026-07-28. Aturan hanya BERTAMBAH; jangan menulis ulang dari ingatan.

## Aturan bernomor

1. Satu definisi R (ADR-A001 §1). Laporan dengan definisi lain ditolak.
2. Gerbang KANDIDAT ADR-A001 §2 berlaku penuh; butir 7 (rezim) DITANGGUHKAN
   sampai ADR-A003 ada.
3. Adjudikasi hipotesis DILARANG sebelum semesta data lengkap dan manifesnya
   terverifikasi. Pembangunan juri di atas 12 simbol probe boleh jalan paralel.
4. `backtest.py` modul warisan tidak boleh dipakai.
5. Angka mana pun dari modul warisan adalah klaim, bukan bukti.
6. Nol koneksi ke bursa; hanya arsip publik `data.binance.vision`.
7. Setiap laporan memuat `sidik_kode` dan `sidik_data`; laporan dengan
   `sidik_data` berbeda tidak boleh dibandingkan.
8. Tidak ada berkas kode BARU melebihi 800 baris; berkas tier A (angkat
   byte-identik) dikecualikan dan wajib punya catatan pengangkatan.
9. Tidak ada skrip `__main__` di akar repo. Satu jalur eksekusi per fungsi.
10. Keluaran diagnostik selalu ditandai `"bukan_bukti": true` dan tidak boleh
    menyentuh gerbang, ambang, konfigurasi, atau putusan.
11. Biaya (fee taker/maker terpisah, funding bertanda benar, slippage yang selalu
    merugikan) adalah bagian JURI sejak hari pertama, bukan money management.

## Kelas cacat

1. **KC-1 (dari modul warisan, belum berlaku di repo ini)** — pemilihan default
   berdasarkan paruh uji. Penangkalnya: pra-registrasi tertulis sebelum run.
2. **KC-2 (dari modul warisan)** — asimetri pencatatan: alasan setup dilewatkan
   dicatat, alasan setup diambil tidak. Penangkalnya: setiap sinyal membawa
   setup_source, htf_score, regime, pattern, sesi, indeks bar.

## Papan skor hipotesis

Kosong. Hipotesis selesai: 0. Kandidat: 0. Ditolak: 0.

## Papan skor prediksi

| # | Prediksi | Ditulis | Status |
|---|---|---|---|
| P-1 | Ekspektasi B0 jatuh di bawah 0,10R setelah funding+slippage dimodelkan benar, dan GAGAL kriteria 1 | 2026-07-28 | menunggu (butuh B0) |

## Daftar ADR

- ADR-A001 — aturan dasar riset. DITERIMA 2026-07-28.
- ADR-A002 — serapan data. BELUM ADA.
- ADR-A003 — taksonomi rezim/klasifikasi. BELUM ADA.

## Status pipeline

| Tahap | Status |
|---|---|
| T0 Peta modul | SELESAI (`PETA_MODUL.md`, `PETA_MODUL_BERKAS.md`) |
| T1 Serapan | BELUM MULAI (butuh ADR-A002) |
| T2 Klasifikasi | BELUM MULAI (butuh ADR-A003) |
| T3 Sinyal | BELUM MULAI |
| T4 Juri/backtest | BELUM MULAI |
| T5 Adjudikasi | TERKUNCI sampai T1 tuntas |

## Jumlah uji

4 uji struktural (`tests/test_kontinuitas.py`). Belum ada uji numerik.

## Utang verifikasi yang belum dibayar

1. Temuan A dan B (rasio isi 5,84%; 96% trendline break) hanya bisa dinilai
   setelah juri sendiri berjalan.
2. Temuan G: klaim "30 pair dipilih alfabetis" belum ditemukan buktinya di berkas.
3. Atribut `enable_hs` tidak ditemukan di `config.py` walau dipakai `strategy.py`
   dan ada di `.env.example`. Perlu dilacak.
4. Klaim temuan N bahwa kendala mengikat pada modal kecil adalah kapasitas
   margin, bukan notional minimum — belum diuji angkanya.
5. Angka 0,3232R dan 0,306R pada aritmetika biaya warisan belum diverifikasi.
