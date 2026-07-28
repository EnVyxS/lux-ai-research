# PROMPT KELANJUTAN — versi 6

Ditulis 2026-07-28. Berkas ini untuk sesi/akun Notion BARU yang kehilangan
konteks. Baca berkas ini lebih dulu, lalu ikuti urutan bacaan di §1.

## 1. Urutan bacaan wajib

1. `STATE.md` (versi 6) — aturan 1..20, kelas cacat KC-1..KC-5, papan skor
   prediksi, utang verifikasi 1..14.
2. `decisions/ADR-A001.md` dan `decisions/ADR-A002.md` (keduanya DITERIMA).
3. Jurnal terbaru ke belakang: `journal/2026-07-28-07.md` (adjudikasi survei
   semesta), lalu `-06.md`, `-05.md`, `-04.md`.
4. `PETA_MODUL.md` dan `PETA_MODUL_BERKAS.md` bila perlu konteks modul warisan.

Jangan menulis apa pun sebelum keempatnya dibaca.

## 2. Identitas kerja

- Operator: Diva Juan Nur Taqarrub, zona Asia/Jakarta, bahasa kerja Indonesia.
- GitHub: `EnVyxS`. Repo kerja SATU-SATUNYA: `EnVyxS/lux-ai-research` (publik,
  id 1314330181, cabang `main`).
- Boleh dibaca, HARAM ditulis: `EnVyxS/lux-research`, `EnVyxS/lux-scalp-research`.
  Hasil/angka/putusan dari sana tidak boleh masuk; kode boleh atas izin eksplisit
  operator disertai asal + blob sha.
- "lanjut"/"lanjutkan" dari operator = teruskan pekerjaan tanpa minta konfirmasi.

## 3. Larangan yang paling sering dilanggar

- Jangan memakai `backtest.py` warisan sebagai juri, dan jangan memakai angka
  AUDIT.md/README warisan sebagai bukti.
- Jangan menyentuh bagian live modul warisan (exchange, telegram_bot, dashboard).
- Jangan menulis angka arsip sebelum artefaknya ter-commit (aturan 13). Sandbox
  agen TIDAK punya jaringan.
- Jangan membuat guard berbasis pencarian kata (aturan 12).
- Jangan melaporkan gerbang hijau tanpa cacah yang dibandingkan (aturan 18).
- Jangan memakai float pada perbandingan data arsip (aturan 19).
- Jangan menyimpulkan melampaui rentang yang disampel (aturan 20).
- Berkas 5m/15m ASLI hanya untuk uji integritas, bukan bahan riset; semua bar
  dibentuk dari 1m.

## 4. Fakta operasional GitHub Actions

- Semua operasi lewat `connections.mcpServer_github.runTool({toolName,
  toolArguments})`. `owner`/`repo` HANYA di dalam `toolArguments`.
- Tidak ada alat untuk melihat status Actions. Status hanya dari berkas laporan
  yang di-commit workflow sendiri.
- Setelah mendorong berkas panjang, WAJIB baca ulang dari `main` dan pastikan
  ekornya hadir.
- Menambah berkas apa pun di `lux_ai/serapan/**` memicu ulang `probe-serapan`
  (~10 menit). Itu tidak merusak apa-apa dan berguna sebagai uji keterulangan.
- Waktu jalan terukur: probe semesta ~10 menit; uji resample 71 detik; survei
  semesta ~13 menit. Unduh rerata 1,33 detik per berkas.
- Runner: tanpa scipy dan requests; numpy/pandas/pyarrow/pyyaml/pytest ada.
  `data.binance.vision` tercapai (200); `fapi.binance.com` 451.

## 5. Posisi sekarang

- HEAD: `12c723956b572122ec86d2aa8649ca9253e78008`.
- CI hijau, 38 uji (run 30327685234).
- Survei semesta selesai (run 30327685200, `kode_keluar: 0`): 937 simbol, 128
  terhenti, 809 hidup, peralihan header 2022-01, stempel milidetik pada seluruh
  144 berkas 2020-2023 dan pada 2024-05, tiga simbol mati berhenti 2024-05-28.
- Skor ramalan: tepat 8, meleset 5, meleset separuh 1, tepat sebagian 1, tidak
  teradjudikasi 1.

## 6. Pekerjaan berikutnya, berurut prioritas

1. **Ukur satuan stempel era 2024-06..2026-06** (utang 14, R-18). Cara termurah:
   naikkan `AKHIR_HEADER` di `lux_ai/serapan/survei.py` menjadi `"2026-06"` dan
   jalankan ulang `survei-semesta`. Bila ada bulan mikrodetik, `resample.py`
   wajib diperbaiki sebelum serapan penuh.
2. **Ganti medan `delisting_klaim_terbukti` di `lux_ai/serapan/probe.py`**
   (utang 13, KC-5) dengan ukuran `survei.terhenti`. Perlu emisi ulang penuh
   berkas 6.594 byte.
3. **Perluas gerbang resample ke era tanpa header** (utang 12, R-12): ulangi
   perbandingan pada bulan PERTAMA tiap simbol probe.
4. **Bangun serapan penuh** per ADR-A002 §9: 8 pecahan berimbang menurut cacah
   bulan (~2.724 berkas, ~1,0 jam, ~4,9 GB per pecahan), manifes per pecahan
   (nama, baris, rentang waktu, checksum, sumber, `funding_ada`, `baris_dibuang`,
   `berheader`, `awal_sejati`, `akhir_sejati` setelah karantina 7 hari), parquet
   per simbol-bulan sebagai aset rilis. Ini mengadjudikasi R-7.
5. **Tugas 3 paralel di 12 simbol probe**: tulis ADR-A003 (taksonomi rezim,
   likuiditas, sesi, struktur, funding; semuanya point-in-time), lalu juri T4
   (fee taker/maker terpisah, funding tiap jadwal, slippage selalu merugikan),
   lalu validasi (uji bulanan berpasangan + Sidak, permutasi ≥300 per TANGGAL
   UTC, PBO & DSR numpy murni). ADJUDIKASI TETAP TERKUNCI sampai manifes semesta
   penuh terverifikasi.
6. Putuskan mengangkat `lux/validasi/dsr.py` + `pbo.py` dari `lux-research`
   (butuh izin operator + catatan pengangkatan + blob sha) atau menulis ulang.
7. Tugas 4: baseline B0, BUKU PENYIMPANGAN, pra-registrasi.
8. `reports/semesta_bulan_1m.json` (18.884 byte) belum pernah dibaca agen.

## 7. Penomoran berikutnya

ADR berikutnya **ADR-A003**. Hipotesis pertama **H-A001** (belum ada). Jurnal
berikutnya **`journal/2026-07-28-08.md`**. STATE berikutnya **v7**. PROMPT
berikutnya **v7**. Ramalan berikutnya **R-20**. N_percobaan = 0. Karantina 7
hari. Serapan 8 pecahan. Jeda mati 2 bulan.

## 8. Berkas repo (blob sha pada HEAD 12c72395 kecuali disebut lain)

| Berkas | Blob sha |
|---|---|
| `STATE.md` v6 | `6028da89053f331f030283e110c23640599855ee` |
| `journal/2026-07-28-07.md` | `1ab7ecf913cb53308062d531f8a460950aeea4ad` |
| `journal/2026-07-28-05.md` | `ccab37c73d8ec5a3a82b092a29092d815c362e86` |
| `decisions/ADR-A002.md` | `5d34225481d206fb4c56d198f29e52b0217a84d7` |
| `decisions/ADR-A001.md` (3.569 B) | `d5bb2f64862b0e2f4b49a3591b3b65e662469e2f` |
| `lux_ai/serapan/arsip.py` (5.231 B) | `0104958bd99772cda8262d5527da52aea9635724` |
| `lux_ai/serapan/klines.py` (3.445 B) | `cc4d9287ccb7a8ea72380399c334b4d19b5301d3` |
| `lux_ai/serapan/probe.py` (6.594 B) | `df0a2d5da219b953f307e5034f00a7a9ef7495d9` |
| `lux_ai/serapan/resample.py` (4.356 B) | `66a4b177fa9d784e1ede92522413595d8a8447fa` |
| `lux_ai/serapan/uji_resample.py` (5.768 B) | `5049dbb0e7b9e24c017ec3ebbde8eb21282a85f9` |
| `lux_ai/serapan/survei.py` | `efe1edba07f9ab33aa5ad8c1a820b6ca75dea2bd` |
| `PETA_MODUL.md` (8.691 B) | `9ee33a991b2ec28405a00550c65f30e419f823cc` |
| `requirements.txt` (71 B) | `b3749ba54f8b27bd9f8bc002f38c11d33f4c1a07` |

Byte yang tidak tertulis memang belum pernah diukur; jangan mengarangnya
(aturan: ukuran berkas bukan bukti isi, dan angka tanpa pengukuran adalah klaim).

## 9. Artefak laporan terakhir

| Berkas | Isi ringkas |
|---|---|
| `reports/ci_terakhir.json` | run 30327685234, commit `e9e891d9`, 38 uji, kode 0 |
| `reports/survei_status.json` | run 30327685200, kode 0, 2026-07-28T04:17:28Z |
| `reports/survei_semesta.json` | 937/128/809/121, header 2022-01, stempel 13 digit |
| `reports/semesta_rentang.json` | rentang bulan per simbol untuk 937 simbol |
| `reports/uji_resample.json` | 12/12 lolos, 0 beda pada 9 kolom |
| `reports/probe_serapan.json` | 937 simbol, 21.789 berkas, estimasi ukuran |
| `reports/semesta_bulan_1m.json` | 18.884 B, BELUM pernah dibaca |

## 10. Empat workflow yang ada

`ci.yml` (uji, abaikan journal/decisions/hipotesis/reports), `probe_serapan.yml`
(`lux_ai/serapan/**`), `uji_resample.yml` (resample/klines), `survei_semesta.yml`
(`lux_ai/serapan/survei.py`). Semuanya commit laporan SEBELUM keluar dengan kode
gagal, dan memakai `[skip ci]` + `git pull --rebase --autostash`.
