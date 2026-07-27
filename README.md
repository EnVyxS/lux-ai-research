# lux-ai-research

Repo riset LUX-AI. Tujuan: membuat klaim tentang LUX **bisa dibuktikan atau
ditolak dengan murah**, bukan membuat LUX terlihat menguntungkan.

## Orientasi lima menit

1. Modul warisan (`LUX_Terminal_v9_web_lux_upgrade.zip`, 208 berkas, bot_v8 v8.7)
   adalah BAHAN, bukan sumber kebenaran. Angka apa pun dari `AUDIT.md` modul
   diperlakukan sebagai KLAIM YANG HARUS DIUJI. Lihat `PETA_MODUL.md`.
2. Juri backtest ditulis ulang di repo ini. `backtest.py` modul DILARANG dipakai.
3. Sumber data tunggal: arsip publik `data.binance.vision` (USDS-M futures),
   klines 1m + funding; interval lain diturunkan lewat resample.
4. Sebuah strategi hanya disebut KANDIDAT bila lolos SELURUH gerbang di
   `decisions/ADR-A001.md`, dan gerbang itu dipra-registrasi sebelum run.
5. Nol koneksi ke bursa. Riset ini murni arsip.

## Urutan baca untuk sesi baru (mengikat)

`PROMPT_KELANJUTAN.md` -> ADR terbaru di `decisions/` -> `STATE.md` ->
`STATE_LAMPIRAN.md` -> `STATE_LAMPIRAN_ANGKA.md` -> dua jurnal terakhir di
`journal/`. Jangan membaca seluruh direktori `journal/`.

## Struktur

```
lux_ai/serapan       unduh, verifikasi, resample, manifes
lux_ai/klasifikasi   label rezim, likuiditas, sesi, struktur, funding
lux_ai/sinyal        detektor hasil angkat + catatan pengangkatan
lux_ai/posisi        entry, SL, TP, trailing, sizing
lux_ai/backtest      juri tunggal, gerbang, putusan
lux_ai/validasi      permutasi, PBO, DSR, koreksi banyak-pembandingan
lux_ai/diagnostik    hanya-baca, seluruh keluaran "bukan_bukti": true
lux_ai/antarmuka     LLM & obrolan; TIDAK PERNAH diimpor backtest/ maupun sinyal/
decisions/           ADR-A001 dan seterusnya
hipotesis/           satu berkas pra-registrasi per hipotesis
journal/             satu berkas per sesi
reports/             artefak hasil run
```

Status sekarang: hipotesis selesai 0, kandidat 0, N_percobaan 0, baseline B0
belum punya angka.
