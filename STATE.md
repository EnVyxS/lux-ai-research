# STATE — versi 20

Diperbarui: 2026-07-28 (sesi 45). Aturan hanya BERTAMBAH; jangan menulis ulang
dari ingatan. v20 disusun di atas teks v19 (blob
`e06c486ecf710929de7e380d9402574dcc7867e2`) yang dibaca ulang UTUH dari `main`
pada sesi ini, ditambah hasil run terhenti, pilot serapan v1, dan pilot v2.

## Aturan bernomor

Aturan 1–36 berlaku tanpa perubahan; teksnya ada di STATE v19 (blob
`e06c486e…`) dan tidak saya salin ulang agar tidak berubah diam-diam saat
disalin. Ringkas nomornya: 1 satu definisi R · 2 gerbang kandidat · 3 adjudikasi
terkunci · 4-5 modul warisan · 6 hanya arsip publik · 7 sidik wajib · 8 ≤800
baris · 9 satu jalur eksekusi · 10 diagnostik `bukan_bukti` · 11 biaya sejak
hari pertama · 12 guard struktural · 13-14 tanpa jaringan · 15 kode repo lain ·
16 nama medan jujur · 17 data biaya hilang → keluar · 18 gerbang lolos wajib
bercacah · 19 Decimal · 20 rentang disampel · 21 hitung ulang · 22 cakupan
`sidik_kode` · 23 gerbang merah tak dilonggarkan · 24 medan penggugur · 25
cakupan dipatok sebelum run · 26 ramalan mutlak butuh besaran · 27 pendamping
tak bersyarat · 28 bulan awal parsial · 29 amandemen tak menghapus · 30 penyebut
eksplisit · 31 `sidik_data` · 32 nama non-ASCII · 33 pemicu sempit · 34 dilarang
add borongan · 35 laporan tanpa sidik hanya petunjuk · 36 dua angka beda →
definisi berdampingan.

37. **[v20]** Sampel yang dipakai menguji sebuah jalur wajib memuat sedikitnya
    satu kasus dari tiap kelas cacat yang diketahui relevan bagi jalur itu, dan
    laporan wajib menyebut kelas mana yang tersentuh dan mana yang tidak, walau
    cacahnya nol. Lahir dari KC-13.

## Kelas cacat

KC-1 s.d. KC-12 seperti pada v19. Perubahan status:

- **KC-10 DITUTUP.** Sensus 12 workflow: pemicu direktori luas = **0**.
  `probe_serapan` dipersempit ke `lux_ai/serapan/probe.py` pada commit
  `4e095921`.
- **KC-11 DITUTUP.** Sensus 12 workflow: pelanggar `git add reports` borongan =
  **0**. Keenam pelanggar ditambal pada commit `4e095921` setelah isinya dibaca
  utuh lebih dulu.
- **KC-9** kini teruji pada berkas NYATA, bukan hanya unit test:
  币安人生USDT 2025-10 terunduh lewat URL ter-percent-encode dan tersimpan
  sebagai `u5E01u5B89u4EBAu751FUSDT-1m-2025-10.parquet`.
- **KC-13 [baru]** — keterwakilan sampel dikorbankan demi keterulangan. Pilot
  serapan v1 memilih tiga simbol pertama menurut abjad; yang terpilih 0GUSDT,
  1000000BOBUSDT, 1000000MOGUSDT — semuanya pasar 2024-2025, sehingga
  pra-header, non-ASCII, dan simbol terhenti tidak tersentuh sama sekali,
  padahal laporannya berbunyi "100% lolos". Penangkalnya aturan 37.

## Papan skor prediksi

R-1..R-85 seperti dirinci v19 (v16 blob `dd997064…`, v17 `1991c374…`,
v18 `8b3dd416…`). R-86..R-90 TEPAT semua (v19).

| # | Prediksi | Status |
|---|---|---|
| R-91 | Terhenti taksonomi 129 vs survei 128, selisih 1 | TEPAT |
| R-92 | Simbol yang berpindah sisi bernama SXPUSDT | TEPAT |
| R-93 | `hanya_survei` kosong (arah selisih satu sisi) | TEPAT |
| R-94 | Pilot: gagal unduh 0, gagal checksum 0 | TEPAT |
| R-95 | Pilot: gerbang gagal 0; nisbah parquet/zip di 1,2..1,9 | TEPAT (1,2151) |
| R-96 | Manifes `jenis_instrumen` = perpetual_usdt 100% | TEPAT |
| R-97 | Pilot v2 memuat 1..4 berkas tanpa header | TEPAT (1) |
| R-98 | Simbol non-ASCII terserap, nama parquet ter-escape | TEPAT |
| R-99 | Gerbang gagal 0 DAN nisbah naik di atas 1,2151 | TEPAT (1,2299) |

**Total R-1..R-99** (aturan 21): TEPAT 52+9 = **61**; MELESET **25**; SEPARUH
**4**; TIDAK TERADJUDIKASI **3**; MENUNGGU **6** (R-7, R-19, R-20, R-28, R-36,
R-37). 61+25+4+3+6 = **99**. ✅

Catatan kejujuran: sembilan TEPAT berturut-turut. Sebagian besar meramalkan
jalur yang saya rancang sendiri dan karenanya berisiko rendah; yang benar-benar
berisiko hanya R-92, R-97, dan klausa nisbah pada R-99. Deret TEPAT panjang
adalah tanda ramalan terlalu aman, bukan tanda saya makin pandai.

Ramalan berikutnya **R-100**.

## Daftar ADR

- ADR-A001 aturan dasar. DITERIMA.
- ADR-A002 serapan. DITERIMA; §3 DIAMANDEMEN oleh ADR-A004 (Amandemen A-1).
- ADR-A003 taksonomi rezim. BELUM ADA (nomor dicadangkan).
- ADR-A004 kebijakan KC-6. DITERIMA.
- **ADR-A005 pemilihan jenis instrumen tahap pertama. DITERIMA (sesi 42).**
  Tahap pertama serapan dan backtest hanya `perpetual_usdt`: 787 simbol,
  19.598 bulan, 10,1% lebih ringan. Jenis lain diserap belakangan, bukan
  dibuang. Futures kedaluwarsa dan SETTLED tidak pernah satu semesta dengan
  perpetual tanpa ADR baru. Manifes wajib bermedan `dugaan_pengganti`. Saham
  dan komoditas token dikarantina.
- ADR berikutnya **A006**.

## Serapan: jalur terbukti ujung ke ujung (pilot)

Sumber: `reports/manifes_pilot.json` blob **`619f16cd28ed23dada3e689536407a16f3838eca`**,
`sidik_kode` `7996d518…`, `sidik_data` `6128fbb0…`, run `30353129569`,
`status: TERUKUR`, `bukan_bukti: false`.

Lima simbol-bulan: ADAUSDT 2020-01 dan 2023-03, 币安人生USDT 2025-10,
1000BTTCUSDT 2022-04, 0GUSDT 2025-09. `kelas_risiko_kosong` = **[]**;
pra_header 1, non_ascii 1, terhenti 1, bulan_awal_2020_2021 1, kendali_baru 2.

Hasil: gagal unduh 0, gagal checksum 0, `baris_dibuang` 0, gerbang lolos 5/5,
`baris_diperiksa` = `slot_diperiksa` = **96.375** (nol menit hilang),
nisbah parquet/zip **1,2299**.

Dua fakta yang mengikat rancangan serapan penuh:
- ADAUSDT 2020-01 hanya **959 baris**, mulai 2020-01-31T08:01Z (hari
  pencatatan).
- 1000BTTCUSDT 2022-04 berakhir 2022-04-11T09:00Z, **14.941 baris**.
→ "44.640 baris" DILARANG dipakai sebagai syarat kelengkapan; ia akan
menjatuhkan bulan pertama dan bulan terakhir setiap simbol.

Belum diuji sama sekali: jalur **funding** (`funding_ada` masih null di kelima
baris) dan medan **`dugaan_pengganti`** yang diwajibkan ADR-A005.

## Simbol terhenti — selisih 129 vs 128 SELESAI (utang 28 LUNAS)

Sumber: `reports/terhenti_semesta.json` blob `609160a326c4156ce629e1b5d42707f354646abe`,
`sidik_kode` `f4fe7675…`, `sidik_data` `6128fbb0…`, penyebut 937/937.
Taksonomi 129 (ambang `bulan_terakhir` ≤ 2026-05) lawan survei 128 (ambang
≤ 2026-04, dari `JEDA_MATI_BULAN=2` terhadap acuan 2026-06). Yang berpindah:
**SXPUSDT** (`bulan_terakhir` 2026-05); `hanya_survei` kosong. `BATAS_R8` TIDAK
terlibat — dugaan lama itu salah. SXPUSDT bukan delisting melainkan ganti nama
(SXPUSDTSETTLED mulai 2026-06).

## Sensus workflow (12 workflow)

`ci`, `ringkas_semesta`, `bentuk_semesta`, `taksonomi_semesta`,
`terhenti_semesta`, `serap_pilot`, `survei_semesta`, `penyebut_kc6`,
`diagnosa_kc6`, `rentang_kc6`, `uji_resample`, `probe_serapan`.
Patuh aturan 34: **12 dari 12**. Pemicu direktori luas: **0**.

Perubahan rancangan sadar risiko: seluruh **pemicu-diri dicabut** — menyunting
sebuah yml tidak lagi menyalakan run-nya. Harganya: salah ketik yml baru
ketahuan saat `workflow_dispatch`. Untuk run 120-330 menit itu tukar yang
benar; keenam yml tertambal **belum pernah benar-benar dijalankan**
(`serap_pilot` sudah, dua kali, kode keluar 0).

## Jumlah uji

**115 TERVERIFIKASI** — `reports/ci_terakhir.json` run `30352684074`, commit
`4e095921`, `kode_keluar: 0`, `"115 tests collected in 0.32s"`.
Setelah itu ditambah `tests/test_serap.py` (8 uji): perkiraan **123**, **belum
terverifikasi laporan CI**. Ini memerlukan verifikasi.

## Utang verifikasi

1-5 dan 11 menunggu tahap juri/klasifikasi. 6-23, 25-28 LUNAS.

24. **AKTIF — serapan penuh.** Syarat (a) s.d. (h) semuanya kini TERPENUHI:
    (a)(b) `nama_aman` teruji pada berkas nyata; (c) `baris_dibuang` ada di tiap
    baris manifes; (d) klausa `selaras_menit` menemani; (e)(f)(g) sensus
    workflow bersih; (h) ADR-A005. Sisa pekerjaan bukan lagi rancangan
    melainkan skala:
    - pecahan (ADR-A002 §9) atas 787 simbol / 19.598 bulan;
    - jalur funding (belum pernah dijalankan sekali pun);
    - medan `dugaan_pengganti`;
    - parquet sebagai aset rilis, bukan isi repo (pilot sudah memakai artefak
      dengan retensi 7 hari);
    - karantina 7 hari.
    Mengadjudikasi R-7, R-19, R-20, R-36, R-37.

## Temuan sampingan yang belum diukur

- Jalur funding: nol kali diuji.
- 15 `SETTLED` lain: apakah punya pendahulu seperti SXPUSDT?
- Daftar `INDEKS` hanya tiga nama, disusun manual.
- Saham dan komoditas token masih terhitung `perpetual_usdt`.
- `.decode("utf-8","replace")` di `klines` membungkam byte rusak.
- Nisbah parquet/zip 1,2299 pada 5 berkas lawan 1,51 ramalan probe atas semesta
  penuh. Dengan 5 berkas saya tidak berhak menyimpulkan (aturan 20).
- Anomali tree: sumber dugaannya (gelung latar `probe_serapan`) sudah dihapus.
  Bila anomali berhenti, itu bukti TIDAK LANGSUNG.
