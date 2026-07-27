# STATE LAMPIRAN ANGKA — buku besar

Hanya angka yang punya artefak sumber. Angka tanpa artefak tidak masuk ke sini.

## N_percobaan berjalan

| Tanggal | Peristiwa | Delta | N kumulatif |
|---|---|---|---|
| 2026-07-28 | Repo dibuka | 0 | 0 |

Ambang Sidak berjalan: N = 0, jadi belum ada koreksi. Rumus yang dipakai nanti:
`alpha_sidak = 1 - (1 - 0,05)^(1/N)`.

## Audit gerbang per sel

Kosong.

## Sidik run

Kosong.

## Sidik data

Kosong. Manifes dataset belum ada (butuh ADR-A002 dan T1).

## Angka terukur dari modul warisan (fakta struktural, bukan hasil dagang)

Semua diukur di sandbox atas arsip yang dilampirkan, bukan dikutip dari dokumen
modul.

| Besaran | Nilai | Cara ukur |
|---|---|---|
| Jumlah berkas dalam arsip | 208 | `find -type f \| wc -l` |
| Berkas `.py` | 165 | pemindaian direktori |
| Total baris `.py` | 25.811 | penghitungan baris per berkas |
| `engine.py` | 3.621 baris / 184.993 byte | idem |
| `strategy.py` | 1.598 baris / 70.020 byte | idem |
| Subpohon `lux/` | 8.674 baris | `wc -l` atas `lux/**/*.py` |
| Skrip `__main__` di akar | 17 dari 33 berkas `.py` | grep `__main__` |
| Penanda tambalan bertanda | 697 kemunculan | grep pola `[...]` |
| Titik tempel `lux` di `engine.py` | 4 (baris 1751, 1761, 2385, 3140) | grep `from lux` |

## Angka yang MASIH KLAIM (dilarang dipakai sebagai bukti)

| Klaim | Sumber klaim | Status |
|---|---|---|
| Signals 10.032, Filled 586, +189,41R, PF 1,61 | `AUDIT.md` modul | belum diverifikasi |
| 559 dari 582 transaksi = TRENDLINE_BREAK | `AUDIT.md` bagian v8.3 | belum diverifikasi |
| Ekspektasi 0,3232R per transaksi | turunan klaim di atas | belum diverifikasi |
| Estimasi biaya sebenarnya 0,306R | temuan warisan | belum diverifikasi |
| PF 1,39 / 1,68 / 1,71 dan seluruh tabel tuning | `AUDIT.md` modul | tercemar kebocoran seleksi (terverifikasi) |
