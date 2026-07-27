# STATE LAMPIRAN — keputusan naratif yang sudah selesai

Agar perdebatan yang sama tidak diulang tiap sesi.

## L-1. Mengapa juri ditulis ulang, bukan diangkat dari modul

`backtest.py` modul memodelkan biaya sebagai satu potongan datar `fee_r`
(baris 134, dikurangkan di baris 426) dan menyatakan sendiri di docstring baris
29 bahwa funding tidak dimodelkan. Juri yang tidak bisa membedakan taker dari
maker, tidak menghitung funding, dan tidak membuat slippage bergantung ukuran
stop, tidak dapat menjawab pertanyaan utama riset ini. Selesai; tidak perlu
diperdebatkan lagi.

## L-2. Mengapa detektor tetap diangkat dari modul

Geometri di `patterns.py` dan `strategy.py` adalah objek yang sedang diuji.
Menulis ulang detektor berarti menguji strategi lain dan menyebutnya baseline.
Maka: angkat byte-identik bila memungkinkan (tier A), atau dengan penyimpangan
yang dideklarasikan satu per satu (tier B) plus catatan pengangkatan berisi
sha256 sumber, blob git, jumlah baris, dan daftar diff persis.

## L-3. Mengapa lapisan risiko modul diangkat apa adanya

`risk.py` adalah bagian paling matang di modul (terverifikasi: power-law sizing,
tier 1-3%, taper mega-cap, `qty_for_max_loss`, `clamp_sl_to_valid_side`,
`resolve_milestone_sl`). Merusaknya berarti membuang kerja yang sudah benar.
Catatan penting: dalam backtest bersatuan R, sizing tidak terlihat sama sekali,
jadi menunda pengujian sizing tidak merusak apa pun.

## L-4. Mengapa ukuran model LLM bukan alasan

Aturan sebenarnya: LLM dilarang di jalur keputusan. Ukuran model adalah
KONSEKUENSI, bukan alasan. Modul warisan membuktikannya tanpa sengaja: 8.674
baris subpohon `lux/` menempel di empat titik yang secara efektif tidak memilih
satu pun transaksi pada konfigurasi default.

Koreksi terhadap rumusan lama "keempatnya no-op by design": `is_setup_silenced`
(engine 1761) dan `lux.genome.apply_to_settings` (main 112) BISA mengubah
perilaku bila genom diredam. Yang membuatnya no-op adalah DEFAULT (semua gen
aktif), bukan desain. Perbedaan ini penting karena default bisa berubah diam-diam.

## L-5. Mengapa serapan berjalan paralel dengan pembangunan juri

Serapan semesta penuh memakan waktu dinding berminggu-minggu karena batas 6 jam
per job. Pembangunan juri hanya butuh 12 simbol. Yang dilarang keras bukan
bekerja paralel, melainkan MENGADJUDIKASI di atas subhimpunan.
