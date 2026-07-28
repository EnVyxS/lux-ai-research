# ADR-A005 — Jenis instrumen mana yang masuk serapan dan backtest tahap pertama

Status: **DITERIMA** 2026-07-28 (sesi 42).
Menutup syarat (h) utang 24. Tidak mengamandemen ADR mana pun.

## Konteks terukur

`reports/taksonomi_semesta.json` (blob `42d07af7…`, `sidik_kode` `f19e89d2…`,
`sidik_data` `6128fbb0…`) menghitung 937 simbol dan 21.789 berkas-bulan:

| Jenis | Simbol | Bulan |
|---|---|---|
| perpetual_usdt | 787 | 19.598 |
| futures_kedaluwarsa | 50 | 258 |
| perpetual_busd | 41 | 812 |
| perpetual_usdc | 39 | 893 |
| sisa_settled | 15 | 36 |
| indeks | 3 | 151 |
| basis_non_fiat | 1 | 39 |
| perpetual_usd1 | 1 | 2 |
| tak_tergolong | 0 | 0 |

150 simbol (16,0%) dan 2.191 bulan (10,1%) BUKAN perpetual USDT. Sebelum
pengukuran ini, seluruh dokumen riset memperlakukan "937 simbol" seolah setara.
Itu keliru dan kini tidak bisa lagi keliru diam-diam.

## Keputusan

1. **Tahap pertama serapan dan backtest hanya memuat `perpetual_usdt`**:
   787 simbol, 19.598 berkas-bulan.
2. Jenis lain **DISERAP BELAKANGAN, bukan dibuang**. Arsipnya tidak ke mana-mana;
   yang dibatasi adalah cakupan tahap pertama, supaya satu semesta backtest
   hanya memuat instrumen dengan mekanisme funding, jam dagang, dan cara
   penyelesaian yang sebanding.
3. **Futures kedaluwarsa dan sisa `SETTLED` tidak akan pernah masuk semesta yang
   sama dengan perpetual** tanpa ADR baru. Keduanya punya tanggal mati yang
   diketahui di muka; strategi yang diuji atasnya tanpa memodelkan hal itu
   menghasilkan angka yang menyesatkan.
4. **Simbol yang berganti nama saat penyelesaian wajib ditandai, bukan dianggap
   delisting.** Preseden terukur: SXPUSDT berhenti 2026-05 dan SXPUSDTSETTLED
   mulai 2026-06 (`reports/terhenti_semesta.json`, blob `609160a3…`). Manifes
   wajib memuat medan `dugaan_pengganti` yang diisi bila ada simbol lain
   berawalan sama yang mulai dalam dua bulan setelah simbol ini berhenti, dan
   medan itu dilaporkan walau kosong.
5. **Karantina kontaminasi saham token.** Bentuk nama TIDAK dapat memisahkan
   AAPLUSDT atau XAUUSDT dari perpetual koin, sehingga mereka masih terhitung
   `perpetual_usdt`. Sampai ada daftar instrumen dari sumber yang sah, simbol
   yang dicurigai demikian dimasukkan daftar karantina tertulis dan dikeluarkan
   dari adjudikasi riset, bukan dari serapan. Dasarnya: **ini memerlukan
   verifikasi** — kecurigaan bukan pengukuran, jadi ia tidak boleh menghapus
   data, hanya menunda pemakaiannya.
6. Setiap laporan tahap serapan wajib menyebut cacah simbol dan bulan per jenis
   yang benar-benar diserap, walau nol (aturan 18, 24, 30).

## Yang secara sadar TIDAK diputuskan

- Apakah BUSD dan USDC layak digabung dengan USDT sebagai "perpetual dolar".
  Mereka berbeda dalam likuiditas dan umur; menggabungkannya butuh pengukuran,
  bukan selera. Belum diukur.
- Apakah kelima belas `SETTLED` lain punya pendahulu seperti SXPUSDT. Belum
  diukur.
- Kelengkapan daftar indeks. Hanya tiga nama disusun manual. **Ini memerlukan
  verifikasi.**

## Akibat langsung

- Beban serapan tahap pertama turun dari 21.789 menjadi **19.598** berkas-bulan,
  yaitu 10,1% lebih ringan, tanpa mengorbankan satu pun pasar yang relevan bagi
  hipotesis pertama.
- Syarat (h) utang 24 dinyatakan **terpenuhi**: aturan penggolongan tertulis,
  diuji delapan uji, dan cacahnya terukur.
