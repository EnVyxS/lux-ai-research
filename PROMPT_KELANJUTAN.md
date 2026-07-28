# PROMPT KELANJUTAN v17

Ditulis 2026-07-28 sesi 29. Berkas di repo adalah kebenaran; berkas ini hanya
peta. Bila keduanya berselisih, repo yang menang dan peta ini salah.

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat `connections.mcpServer_github.runTool({toolName,
   toolArguments})`. `owner` dan `repo` HANYA di dalam `toolArguments`.
3. Baca dari `EnVyxS/lux-ai-research`, berurutan: berkas ini; `STATE.md`
   (**v16, TERTINGGAL** — lihat peringatan di bawah); `journal/2026-07-28-29.md`
   (paling mutakhir, memuat status utang); `decisions/ADR-A002.md` beserta
   Amandemen A-1 dan `decisions/ADR-A004.md` sebelum menyentuh serapan.
4. Baru setelah itu jalankan pekerjaan teknis.

## PERINGATAN KONTINUITAS

`STATE.md` masih **v16** dan berhenti di sesi 25. Sesi 26–29 hanya tercatat di
jurnal 26, 27, 28, 29. STATE v17 BELUM ditulis karena isi v16 (≈15 KB) tidak
muat dibaca ulang di akhir sesi, dan `push_files` menulis ulang seluruh berkas —
menyusunnya dari ingatan akan menghapus isi yang benar. **Tugas pertama sesi
berikutnya: baca `STATE.md` v16 utuh saat konteks masih lapang, lalu tulis v17.**
Jangan menulis STATE dari ingatan.

## BATASAN YANG MAHAL DIPELAJARI ULANG

- Sandbox agen TIDAK punya jaringan. Semua unduhan dan pengukuran arsip
  dijalankan GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- Tidak ada alat membaca status Actions. Status hanya diketahui dari berkas
  laporan yang di-commit workflow itu sendiri.
- Tidak ada API patch. `push_files` menulis ulang seluruh isi berkas. Rancang
  berkas kecil. Setelah mendorong, BACA ULANG dari `main` dan pastikan ekornya
  hadir.
- Runner: numpy, pandas, pyarrow, pyyaml, pytest ADA; scipy dan requests TIDAK.
  data.binance.vision bisa diakses; fapi.binance.com memberi 451.
- Dilarang menulis apa pun di luar repo lux-ai-research. lux-research boleh
  DIBACA saja; angkanya tidak pernah boleh masuk.

## POSISI HARI INI

- HEAD sesi 29: `20f383680111c3d9913bef842bcd25ebc9d1674b`.
- Jumlah uji **102**, terverifikasi CI run **30349383760** (commit `65e4f5f9`,
  `kode_keluar: 0`).
- Papan skor **R-1..R-64**: TEPAT 37, MELESET 18, MELESET SEPARUH 2, TIDAK
  TERADJUDIKASI 1, MENUNGGU 6 (R-7, R-19, R-20, R-28, R-36, R-37). Jumlah 64.
  Wajib dihitung ulang baris demi baris saat menulis STATE v17 (aturan 21).
- Ramalan berikutnya **R-65**. Jurnal berikutnya `journal/2026-07-28-30.md`.
  STATE berikutnya v17. PROMPT berikutnya v18. Aturan terakhir **32**. Kelas
  cacat terakhir **KC-9**. Utang terakhir **26**. N_percobaan = 0.

## UTANG AKTIF — tinggal dua

- **24 — serapan penuh.** Satu-satunya pekerjaan besar tersisa. Per ADR-A002 §9
  sebagaimana diamandemen ADR-A004: 8 pecahan (~2.724 berkas, ~1,0 jam, ~4,9 GB
  tiap pecahan), tiap simbol-bulan lewat `gerbang_1m.nilai_deret`, manifes per
  simbol-bulan, parquet sebagai aset rilis, karantina 7 hari. Mengadjudikasi
  R-7, R-19, R-20, R-36, R-37.
- **25 — H-A003** belum terbukti: siapa yang menulis ulang
  `reports/semesta_bulan_1m.json` secara berkala (byte tetap 18.884, hanya
  `waktu_utc` berubah).

Utang 7 dan 26 LUNAS. Utang 1, 2, 3, 4, 5, 11 menunggu tahap lain.

## SYARAT RANCANGAN YANG MENGIKAT UTANG 24

Diwariskan dari utang 7 (jurnal 28) dan pembacaan jurnal 17 (jurnal 29):

1. **Nama berkas parquet** wajib diamankan untuk sistem berkas, BUKAN disalin
   mentah dari nama simbol. Tiga pasar bernama huruf Tionghoa itu nyata.
   `klines.tulis_parquet(df, tujuan)` menerima `tujuan` dari pemanggil, jadi
   titik cacatnya akan LAHIR di baris pemanggil, bukan di modul yang ada.
2. **Kunci manifes** wajib sadar non-ASCII sejak baris pertama ditulis, bukan
   ditambal belakangan.
3. Pemanggil wajib mencatat `baris_dibuang` dari `klines.rapikan` ke manifes,
   bukan membuangnya (aturan 18).
4. `gerbang_1m.menit_hilang_dalam_rentang` bisa NEGATIF bila dua stempel jatuh
   di menit yang sama; yang menangkapnya adalah klausa `selaras_menit`. Jangan
   pernah memakai medan itu sendirian.

## KC-9 — status terukur

Tiga pasar non-ASCII: `币安人生USDT`, `我踏马来了USDT`, `龙虾USDT`, memikul 19
berkas-bulan. Semesta = **937 simbol** (934 ASCII + 3), **21.789 berkas 1m**
(21.770 + 19), 2020-01..2026-06 (78 bulan).

- Titik (a) URL arsip: `arsip.segmen()` = `quote(teks, safe="")`, dipakai
  `url_klines` dan `url_funding`. DIJAGA 6 uji di `tests/test_arsip_kc9.py`.
- Titik (b) nama berkas: tidak ada cacat di kode yang ada; jadi syarat
  rancangan utang 24.
- Titik (c) kunci manifes: syarat rancangan utang 24.
- Cacat yang MASIH HIDUP dan sengaja dibiarkan: `ringkas_semesta.POLA_SIMBOL =
  ^[A-Z0-9_]{2,20}$` membuang tiga nama itu — kini dicatat lewat
  `cacah_kunci_ditolak_pola`, bukan dibungkam.

## KEBIASAAN YANG MENGIKAT

- Tulis ramalan SEBELUM run atau SEBELUM membaca berkas, lalu adjudikasi jujur.
- Ramalan dari INGATAN adalah sumber kesalahan yang terbukti: R-56..R-58 ketiganya
  meleset karena saya menuduh `arsip.py` cacat tanpa membacanya. Baca dulu.
- Tiga kali hari ini modul lama ternyata lebih berhati-hati daripada modul baru
  (`arsip.py`, `test_penyebut_kc6.py`, `bentuk_semesta.py`). Kehati-hatian tidak
  menular antar modul; hanya aturan tertulis yang memaksanya.
- Hitung ulang setiap angka ringkasan baris demi baris (aturan 21).
- Setiap pengukuran sebab wajib memuat medan yang bisa MENGGUGURKAN hipotesis
  yang dipercaya (aturan 24).
- Pisahkan fakta dari asumsi; tanpa bukti tulis "Ini memerlukan verifikasi."
- "lanjut" berarti teruskan tanpa konfirmasi.
- Bila konteks hampir penuh, HENTIKAN pekerjaan teknis dan perbarui berkas
  kontinuitas lebih dulu.

## ADJUDIKASI RISET TETAP TERKUNCI

Aturan 3: tidak ada adjudikasi riset sampai manifes semesta penuh terverifikasi.
Boleh paralel sekarang: ADR-A003 taksonomi rezim; juri T4 berbiaya sejak hari
pertama; lapisan validasi (uji bulanan berpasangan + Sidak, ≥300 permutasi per
TANGGAL UTC, PBO dan DSR numpy murni).
