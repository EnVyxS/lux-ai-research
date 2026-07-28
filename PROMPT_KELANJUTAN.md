# PROMPT KELANJUTAN v15

Kamu melanjutkan riset LUX-AI. Operator: Diva Juan Nur Taqarrub, GitHub EnVyxS,
zona waktu Asia/Jakarta, bahasa kerja Indonesia. Jangan mulai bekerja sebelum
menyelesaikan LANGKAH 0. Berkas di repo adalah kebenaran; prompt ini hanya peta.

## LANGKAH 0 — wajib, berurutan

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})`. `owner` dan
   `repo` HANYA di dalam `toolArguments`, tidak di tingkat atas.
3. Baca dari main repo `EnVyxS/lux-ai-research`, berurutan: `PROMPT_KELANJUTAN.md`
   (v15); `STATE.md` — **PERINGATAN: STATE masih v15 dan TERTINGGAL tujuh sesi**
   (belum memuat aturan 30–32, KC-7..KC-9, papan skor R-44..R-55, utang 19 lunas);
   `journal/2026-07-28-{22,23,24,25}.md` yang memuat keadaan mutakhir sebenarnya;
   `decisions/ADR-A002.md` (beserta Amandemen A-1) dan `decisions/ADR-A004.md`;
   `PETA_MODUL.md` bila menyentuh modul warisan.
4. **Pekerjaan pertama sesi berikutnya adalah menulis STATE v16**, sebelum
   pekerjaan teknis baru.

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

## POSISI HARI INI (2026-07-28, sesi 25)

- HEAD: `3244550d62bb39137dc4f80df6bce1bc465a4c3f` (jurnal 25).
- CI terakhir: run **30347164329**, commit `f270354c`, 09:34:55Z, `kode_keluar: 0`,
  **96 uji**.
- **Utang 19 LUNAS.** Semesta sah: **937 simbol, 21.789 berkas-bulan**,
  2020-01..2026-06. `reports/ringkas_semesta.json` melaporkan 934 diterima + 3
  ditolak = 937; tiga yang ditolak bernama huruf Tionghoa (币安人生USDT,
  我踏马来了USDT, 龙虾USDT) dan memikul tepat 19 berkas-bulan.
- Utang AKTIF tinggal **24** (serapan penuh).
- Aturan terakhir **32**. Kelas cacat terakhir **KC-9**. Ramalan berikutnya
  **R-56**. Jurnal berikutnya `journal/2026-07-28-26.md`. STATE berikutnya v16.
  PROMPT berikutnya v16.

## PAPAN SKOR (sesudah R-55)

TEPAT 31 · MELESET 15 · MELESET SEPARUH 2 (R-3, R-53) · TIDAK TERADJUDIKASI 1
(R-40) · MENUNGGU 6 (R-7, R-19, R-20, R-28, R-36, R-37). Total 55.
Adjudikasi sesi 22–25: R-44 R-45 R-46 MELESET; R-47 R-48 R-49 R-51 R-52 R-54
R-55 TEPAT; R-50 MELESET; R-53 MELESET SEPARUH.

## ATURAN BARU YANG BELUM MASUK STATE

- **30.** Setiap laporan diagnostik wajib memuat penyebutnya eksplisit; bila
  penyebut nol, status `TIDAK MENGUKUR`. Ramalan atas medan penggugur tidak
  boleh TEPAT bila penyebutnya nol. (KC-7: bersih palsu karena penyebut nol.)
- **31.** Setiap laporan wajib mencatat `sidik_data` sumber; perbandingan
  antar-run wajib menyebut apakah `sidik_data`-nya sama. (KC-8: sumber bergerak,
  dikira tetap karena hanya ukurannya dicocokkan — `byte_sumber` 18.884 tetap
  sama sementara sidik berubah tiga kali.)
- **32.** Nama pasar TIDAK boleh dianggap ASCII. Setiap penyaring nama wajib
  mencatat cacah dan contoh yang DITOLAK. Pada serapan, nama simbol wajib
  di-percent-encode di URL dan diamankan untuk nama berkas. (KC-9.)

## PEKERJAAN BERIKUTNYA, BERURUTAN

1. **STATE v16** (paling mendesak): aturan 30–32, KC-7..KC-9, papan skor di atas,
   utang 19 lunas, hipotesis H-A002a TERBUKTI / H-A002b GUGUR / H-A003 bertahan.
2. **Periksa `lux_ai/serapan/arsip.py` terhadap KC-9** sebelum serapan penuh:
   percent-encoding URL, keamanan nama berkas keluaran, kunci manifes non-ASCII.
   Tiga simbol dan 19 berkas-bulan akan hilang tanpa suara bila ini dilewatkan.
3. **Serapan penuh** (utang 24) per ADR-A002 §9 sebagaimana diamandemen ADR-A004:
   8 pecahan (~2.724 berkas, ~1,0 jam, ~4,9 GB tiap pecahan), tiap simbol-bulan
   melewati `gerbang_1m.nilai_deret`, manifes per simbol-bulan, parquet sebagai
   aset rilis, karantina 7 hari. Mengadjudikasi R-7, R-19, R-20, R-36, R-37.
   Pra-registrasi R-56 dst. SEBELUM run; patuhi aturan 25–32.
4. Paralel (aturan 3): ADR-A003 taksonomi rezim; juri T4 berbiaya sejak hari
   pertama; lapisan validasi (uji bulanan berpasangan + Sidak, ≥300 permutasi per
   TANGGAL UTC, PBO dan DSR numpy murni).
5. Baca ulang yang tertunggak: `journal/2026-07-28-17.md`, `-19.md`,
   `tests/test_penyebut_kc6.py`, `.github/workflows/penyebut_kc6.yml`,
   `lux_ai/serapan/bentuk_semesta.py`.
6. Utang lama yang masih berdiri: 1, 2, 3, 4, 5, 7, 11.

Adjudikasi riset tetap TERKUNCI sampai manifes semesta penuh terverifikasi
(aturan 3).

## KEBIASAAN

Tulis ramalan SEBELUM run lalu adjudikasi jujur (15 ramalan sudah MELESET).
Hitung ulang setiap angka ringkasan baris demi baris (aturan 21). Setiap
pengukuran sebab wajib memuat medan yang bisa MENGGUGURKAN hipotesis yang
dipercaya (aturan 24). Bila sebuah ramalan tepat angkanya tetapi salah sebabnya,
catat MELESET SEPARUH dan kejar sebabnya — R-53 nyaris membuat saya memperbaiki
batas panjang padahal cacatnya ASCII. Pisahkan fakta dari asumsi; tanpa bukti
tulis "Ini memerlukan verifikasi." Bila dua berkas kontinuitas sempat tidak
sinkron, catat ketidakcocokannya terbuka di jurnal alih-alih membiarkannya
diam-diam. "lanjut" berarti teruskan tanpa konfirmasi. Bila konteks hampir penuh,
HENTIKAN pekerjaan teknis dan perbarui berkas kontinuitas dulu.
