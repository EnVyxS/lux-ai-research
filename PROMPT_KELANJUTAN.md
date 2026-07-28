# PROMPT KELANJUTAN — versi 7

Ditulis 2026-07-28. Berkas ini untuk sesi berikutnya, atau untuk akun Notion
lain, bila percakapan sebelumnya hilang. Bacalah ini lebih dulu, jangan mulai
bekerja dari ingatan siapa pun.

## Posisi sekarang

- Repo kerja: `EnVyxS/lux-ai-research`, publik, cabang `main`.
- HEAD saat berkas ini ditulis: `db21e68e98923e9d2973aa1008f82848829548c6`.
- Tahap: T1 SERAPAN. Probe selesai, gerbang resample lulus, survei semesta
  selesai untuk rentang penuh. Serapan penuh BELUM dibangun.
- Hipotesis riset: 0. Kandidat: 0. N_percobaan: 0. Belum ada satu pun angka
  strategi. Yang sudah matang barulah infrastrukturnya.

## Urutan baca wajib sebelum menyentuh apa pun

1. `STATE.md` — aturan bernomor 1–21, kelas cacat KC-1..KC-5, papan skor
   prediksi, utang verifikasi. Ini dokumen paling penting.
2. `decisions/ADR-A001.md` dan `decisions/ADR-A002.md`.
3. `journal/2026-07-28-08.md` (adjudikasi R-18, satuan stempel) dan
   `journal/2026-07-28-09.md` (perbaikan KC-5 pada probe, pra-registrasi R-21
   dan R-22).
4. `PETA_MODUL.md` untuk modul warisan; jangan pernah memakai angkanya sebagai
   bukti.

## Batasan yang paling sering membuat celaka

- Semua operasi GitHub lewat
  `connections.mcpServer_github.runTool({toolName, toolArguments})`, dan
  `owner`/`repo` HANYA di dalam `toolArguments`.
- Tidak ada API patch. Setiap penulisan berkas adalah emisi ISI PENUH, jadi
  rancang berkas kecil. Setelah mendorong berkas panjang, BACA ULANG dari
  `main` dan pastikan ekornya hadir.
- Tidak ada alat untuk melihat status GitHub Actions. Status hanya diketahui
  dari artefak yang di-commit workflow ke `reports/`.
- Sandbox agen TIDAK punya jaringan. Semua unduhan arsip dijalankan runner.
- Runner tidak punya `scipy` dan `requests`. Statistik memakai numpy murni.
- Commit ke `journal/**`, `decisions/**`, `hipotesis/**`, `reports/**` tidak
  memicu CI. Berkas `.md` di akar (termasuk berkas ini) MEMICU CI.
- Mendorong `lux_ai/serapan/**` memicu `probe-serapan` (~10 menit) dan, bila
  yang tersentuh `survei.py`, memicu `survei-semesta` (~15 menit).

## Angka yang sudah terverifikasi (jangan dihitung ulang dari ingatan)

| Besaran | Nilai |
|---|---|
| Simbol di indeks arsip | 937, terulang tiga run |
| Berkas bulanan 1m | 21.789, terulang dua run |
| Rentang arsip | 2020-01 s.d. 2026-06 |
| Simbol terhenti (jeda ≥ 2 bulan) | 128 (13,7%); masih terbit 809 |
| Bulan terakhir lebih tua dari 2026-01 | 121 |
| Peralihan header | tanpa header s.d. 2021-12, berheader sejak 2022-01, monoton, 3 simbol × 78 bulan |
| Satuan stempel | milidetik, seragam pada 237 bulan disampel |
| Rerata byte zip / parquet | 1.186.859 / 1.797.488 |
| Batas atas total zip / parquet | 25,86 GB / 39,17 GB |
| Gerbang resample | 12/12 lolos, 8.640 bar 5m dan 2.880 bar 15m per simbol, 0 beda pada 9 kolom |
| Simbol mati SRM/COCOS/BTS | berhenti 2024-05-28, 07:10 / 07:16 / 07:09 UTC |

Klaim warisan 40–60 GB dan ~34.000 berkas TERBANTAH. Estimasi bulan pertama
yang saya tulis sendiri juga meleset; jangan mewarisi angka mana pun tanpa
artefaknya.

## Uji

46 uji tanpa jaringan (CI run 30336075738, commit `7fdc81cc`, `kode_keluar: 0`).
`test_kontinuitas.py` 7, `test_serapan.py` 12, `test_resample.py` 11,
`test_survei.py` 16. Sebagian menguji CARA MENGUKUR, bukan hasil — pertahankan
kebiasaan itu (aturan 12).

## Yang sedang berjalan saat berkas ini ditulis

Run `probe-serapan` yang dipicu commit `7fdc81cc` BELUM selesai.
`reports/probe_status.json` masih memuat run 30334170269. Sesi berikutnya wajib
membaca `reports/probe_serapan.json` yang baru dan mengadjudikasi:

- **R-21**: `klaim_delisting_terhenti` = SRM, COCOS, BTS; `masih_terbit` = FTT;
  `tidak_di_indeks` kosong; acuan `2026-06`. Ini sekaligus adjudikasi ulang R-2.
- **R-22**: 937, 21.789, rerata zip 1.186.859, rerata parquet 1.797.488
  terulang persis.

## Pekerjaan berikutnya, berurutan

1. Adjudikasi R-21 dan R-22 dari artefak, lalu STATE v8 dan jurnal 10.
2. Utang 12 / R-12: perluas gerbang resample ke era TANPA header, yaitu bulan
   PERTAMA tiap simbol probe.
3. Bangun serapan penuh menurut ADR-A002 §9: 8 pecahan, ~2.724 berkas per
   pecahan, parquet per simbol-bulan sebagai aset rilis. Manifes wajib memuat
   `nama, baris, rentang waktu, checksum, sumber, funding_ada, baris_dibuang,
   berheader, awal_sejati, akhir_sejati` DITAMBAH satuan stempel per
   simbol-bulan, karena R-19 dan R-20 diadjudikasi dari situ. Karantina 7 hari.
4. ADR-A003: taksonomi rezim, likuiditas, sesi, struktur, funding, semuanya
   point-in-time. Sebelum ini ada, kriteria lulus butir 7 tetap ditangguhkan.
5. Juri T4 dan lapisan validasi: uji bulanan berpasangan dengan koreksi Sidak,
   permutasi ≥300 per TANGGAL UTC, PBO dan DSR numpy murni. Putuskan lebih dulu
   apakah `lux/validasi/dsr.py` dan `pbo.py` diangkat dari `lux-research` — itu
   butuh izin eksplisit operator, catatan pengangkatan, dan blob sha.
6. Baseline B0, BUKU PENYIMPANGAN, pra-registrasi, baru adjudikasi.

Adjudikasi hipotesis riset tetap TERKUNCI sampai semesta penuh terserap dan
manifesnya terverifikasi (aturan 3). Pembangunan juri di atas 12 simbol probe
boleh jalan paralel.

## Penomoran

ADR berikutnya A003. Hipotesis pertama H-A001 (belum ada). Jurnal berikutnya
`journal/2026-07-28-10.md`. STATE berikutnya v8. PROMPT berikutnya v8. Ramalan
berikutnya R-23.

## Nada kerja yang diminta operator

Bahasa Indonesia. Pisahkan fakta dari asumsi; fakta tanpa artefak ditulis "Ini
memerlukan verifikasi." Yang nyata hanyalah yang tercommit. "lanjut" berarti
teruskan tanpa meminta konfirmasi. Jangan pernah menaruh angka hasil dari
`lux-research` atau `lux-scalp-research` ke dalam repo ini.
