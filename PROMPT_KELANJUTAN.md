# PROMPT KELANJUTAN v16

Kamu melanjutkan riset LUX-AI. Operator: Diva Juan Nur Taqarrub, GitHub EnVyxS,
zona waktu Asia/Jakarta, bahasa kerja Indonesia. Jangan mulai bekerja sebelum
menyelesaikan LANGKAH 0. Berkas di repo adalah kebenaran; prompt ini hanya peta.

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`. `owner` dan
   `repo` HANYA di dalam `toolArguments`, tidak di tingkat atas.
3. Baca dari main repo `EnVyxS/lux-ai-research`, berurutan:
   `PROMPT_KELANJUTAN.md` (v16); **`STATE.md` (v16) — kini MUTAKHIR dan sinkron,
   aturan 1-32, KC-1..KC-9, papan skor R-1..R-55, utang 1-26. INI YANG PALING
   PENTING**; `decisions/ADR-A001.md`, `ADR-A002.md` (beserta Amandemen A-1),
   `ADR-A004.md`; `journal/2026-07-28-25.md`; `PETA_MODUL.md` bila menyentuh
   modul warisan.
4. Baru setelah itu jalankan pekerjaan teknis.

## BATASAN YANG MAHAL DIPELAJARI ULANG

- Sandbox agen TIDAK punya jaringan. Semua unduhan dan pengukuran arsip
  dijalankan GitHub Actions; agen hanya boleh percaya artefak yang di-commit.
- Tidak ada alat untuk membaca status GitHub Actions. Status hanya diketahui
  dari berkas laporan yang di-commit workflow itu sendiri.
- Tidak ada API patch. `push_files` menulis ulang seluruh isi berkas. Rancang
  berkas kecil.
- Setelah mendorong berkas panjang, BACA ULANG dari main dan pastikan ekornya
  hadir.
- Runner: numpy, pandas, pyarrow, pyyaml, pytest tersedia; TIDAK ada scipy dan
  requests. data.binance.vision bisa diakses; fapi.binance.com memberi 451.
- Dilarang menulis apa pun di luar repo lux-ai-research. lux-research boleh
  DIBACA saja; hasil dan angkanya tidak pernah boleh masuk.

## POSISI HARI INI (2026-07-28, akhir sesi 25)

- HEAD pekerjaan teknis: `f270354ca8a5c3d585fcdef943123370b7702826`
  (`ringkas_semesta.py` v3). Jurnal terakhir `journal/2026-07-28-25.md`
  (commit `3244550d…`). STATE v16 dan PROMPT v16 didorong sesudahnya.
- CI terakhir: run **30347164329**, commit `f270354c`, `kode_keluar: 0`,
  **96 uji**.
- Semesta sah: **937 simbol, 21.789 berkas-bulan**, 2020-01..2026-06, bulan per
  simbol 1..78. Utang 19 LUNAS.
- **KC-9 baru**: 3 dari 937 pasar bernama huruf Tionghoa (币安人生USDT,
  我踏马来了USDT, 龙虾USDT), memikul 19 berkas-bulan. Aturan 32 lahir dari sini.
- Utang AKTIF: **7** (percent-encoding, penghalang serapan), **24** (serapan
  penuh), **25** (H-A003 belum terbukti), **26** (lima berkas belum dibaca ulang).
- Aturan terakhir **32**. Kelas cacat terakhir **KC-9**. Ramalan berikutnya
  **R-56**. Jurnal berikutnya `journal/2026-07-28-26.md`. STATE berikutnya v17.
  PROMPT berikutnya v17. N_percobaan = 0.

## PAPAN SKOR (R-1..R-55)

TEPAT 31 · MELESET 15 · MELESET SEPARUH 2 (R-3, R-53) · TIDAK TERADJUDIKASI 1
(R-40) · MENUNGGU 6 (R-7, R-19, R-20, R-28, R-36, R-37). Rinciannya di STATE v16.

## PEKERJAAN BERIKUTNYA, BERURUTAN

1. **Utang 7 — periksa `lux_ai/serapan/arsip.py` terhadap KC-9** sebelum serapan
   penuh, pada tiga titik: (a) `url_klines` dan `url_funding` menempelkan nama
   simbol mentah tanpa percent-encoding; (b) nama berkas parquet memakai nama
   simbol apa adanya; (c) kunci manifes berasumsi ASCII. Tulis uji dengan kasus
   POSITIF dan NEGATIF memakai ketiga nama Tionghoa itu (aturan 12).
   Pra-registrasi R-56 dst. sebelum run.
2. **Utang 24 — serapan penuh** per ADR-A002 §9 sebagaimana diamandemen
   ADR-A004: 8 pecahan (~2.724 berkas, ~1,0 jam, ~4,9 GB tiap pecahan), tiap
   simbol-bulan melewati `gerbang_1m.nilai_deret`, manifes per simbol-bulan
   (nama, baris, rentang waktu, checksum, sumber, funding_ada, baris_dibuang,
   berheader, awal_sejati, akhir_sejati, satuan stempel, hasil gerbang), parquet
   sebagai aset rilis, karantina 7 hari. Mengadjudikasi R-7, R-19, R-20, R-36,
   R-37.
3. **Utang 26** — baca ulang dari `main`: `journal/2026-07-28-17.md`, `-19.md`,
   `tests/test_penyebut_kc6.py`, `.github/workflows/penyebut_kc6.yml`,
   `lux_ai/serapan/bentuk_semesta.py`.
4. Paralel, boleh sekarang (aturan 3): ADR-A003 taksonomi rezim; juri T4 dengan
   biaya sejak hari pertama; lapisan validasi (uji bulanan berpasangan + Sidak,
   ≥300 permutasi per TANGGAL UTC, PBO dan DSR numpy murni).
5. Utang lama yang menunggu tahap lain: 1, 2, 3, 4, 5, 11.

Adjudikasi riset tetap TERKUNCI sampai manifes semesta penuh terverifikasi
(aturan 3).

## KEBIASAAN

Tulis ramalan SEBELUM run lalu adjudikasi jujur (15 sudah MELESET, 2 MELESET
SEPARUH). Hitung ulang setiap angka ringkasan baris demi baris (aturan 21).
Setiap pengukuran sebab wajib memuat medan yang bisa MENGGUGURKAN hipotesis yang
dipercaya (aturan 24). Bila ramalan tepat angkanya tetapi salah sebabnya, catat
MELESET SEPARUH dan kejar sebabnya — R-53 nyaris membuat saya memperbaiki batas
panjang padahal cacatnya ASCII. Nol pelanggaran atas nol pengamatan bukan
kebersihan (aturan 30). Ukuran berkas yang sama bukan bukti data yang sama
(aturan 31). Pisahkan fakta dari asumsi; tanpa bukti tulis "Ini memerlukan
verifikasi." Kegagalan yang berbunyi keras lebih murah daripada keberhasilan
yang berbohong: jangan menulis pengumpul "toleran" yang menebak. "lanjut"
berarti teruskan tanpa konfirmasi. Bila konteks hampir penuh, HENTIKAN pekerjaan
teknis dan perbarui berkas kontinuitas dulu.
