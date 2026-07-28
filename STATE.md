# STATE — versi 24

Diperbarui: 2026-07-29 (sesi 53). Aturan hanya BERTAMBAH; jangan menulis ulang
dari ingatan. v24 disusun di atas teks v23 yang dibaca langsung dari `main`
(blob `c28a00be`), ditambah kedelapan log run **`30389402113`**.

Peristiwa terbesar sejak v23: **data serapan akhirnya bertahan.** 19.586 parquet
yang lolos gerbang kini tersimpan sebagai aset rilis terverifikasi. Sejak v20
STATE selalu menutup dengan kalimat "semesta ini masih ANGKA tanpa data";
kalimat itu tidak berlaku lagi.

## Aturan bernomor

Aturan 1–36 berlaku tanpa perubahan; teksnya ada di STATE v19 (blob
`e06c486e…`). Ringkas nomornya: 1 satu definisi R · 2 gerbang kandidat ·
3 adjudikasi terkunci · 4-5 modul warisan · 6 hanya arsip publik · 7 sidik wajib ·
8 ≤800 baris · 9 satu jalur eksekusi · 10 diagnostik `bukan_bukti` · 11 biaya
sejak hari pertama · 12 guard struktural · 13-14 tanpa jaringan · 15 kode repo
lain · 16 nama medan jujur · 17 data biaya hilang → keluar · 18 gerbang lolos
wajib bercacah · 19 Decimal · 20 rentang disampel · 21 hitung ulang · 22 cakupan
`sidik_kode` · 23 gerbang merah tak dilonggarkan · 24 medan penggugur ·
25 cakupan dipatok sebelum run · 26 ramalan mutlak butuh besaran · 27 pendamping
tak bersyarat · 28 bulan awal parsial · 29 amandemen tak menghapus · 30 penyebut
eksplisit · 31 `sidik_data` · 32 nama non-ASCII · 33 pemicu sempit · 34 dilarang
add borongan · 35 laporan tanpa sidik hanya petunjuk · 36 dua angka beda →
definisi berdampingan.

37. **[v20]** Sampel yang dipakai menguji sebuah jalur wajib memuat sedikitnya
    satu kasus dari tiap kelas cacat yang diketahui relevan, dan laporan wajib
    menyebut kelas mana yang tersentuh dan mana yang tidak, walau cacahnya nol.
38. **[v21]** Cacah uji hanya sah dari `reports/ci_terakhir.json` (run id +
    commit + `kode_keluar`). Penjumlahan taksiran dilarang ditulis sebagai angka
    uji. Lahir dari selisih 135 lawan **141**.
39. **[v22]** Keseragaman yang terukur pada sampel DILARANG dipakai sebagai
    angka ramalan untuk anggota di luar sampel; wajib pita atau kemungkinan
    campuran. Lahir dari R-114.
40. **[v22]** Tiap laporan yang mencacah baris sebuah simbol-bulan wajib memuat
    uji silang `baris + hilang_di_tengah + tepi = menit_kalender` dan melaporkan
    selisihnya walau nol. Lahir dari 210 menit BNXUSDT 2022-04.
41. **[v23]** Ramalan bersyarat yang penyebutnya nol dicatat TIDAK
    TERADJUDIKASI, bukan TEPAT, dan status itu wajib dipra-registrasikan bersama
    ramalannya. Lahir dari R-120.
42. **[v23]** Kelas cacat baru DILARANG dinamai atas dasar satu angka yang
    belum diukur langsung. Tuduhan ditulis sebagai hipotesis + run, bukan
    sebagai kelas. Lahir dari KC-16 yang ditarik.
43. **[v24]** Medan penggugur yang membandingkan taksiran dengan kenyataan wajib
    memakai toleransi yang BERSKALA terhadap cacah item, bukan margin datar.
    Margin datar 20.480 byte membuat 16 uji lolos sementara produksi gagal pada
    1.055 anggota, karena cacatnya (header pax 1.024 B per anggota) tumbuh per
    item sedangkan marginnya tidak. Uji wajib memuat kasus bercacah besar.
44. **[v24]** Ramalan wajib menyebut penyebutnya secara eksplisit: pecahan mana,
    semesta mana, medan mana. Bila sebuah pita hanya masuk akal di bawah satu
    tafsir dan meleset di bawah tafsir lain, ia diadjudikasi MELESET. Lahir dari
    R-131, yang pitanya disusun untuk delapan pecahan tetapi medannya hanya ada
    pada tujuh.

## Kelas cacat

KC-1 s.d. KC-12 seperti pada v19. KC-10 dan KC-11 DITUTUP (v20). KC-13
(keterwakilan sampel) → penangkalnya aturan 37.

- **KC-14 [v21, dipersempit v22] — menit hilang NYATA di arsip 1m, hadir di
  KEDUA representasi.** **9** simbol-bulan, **6.375 menit** (425×15). Sebab
  tidak diketahui (H-A004, tak dapat diuji). Kebijakan: karantina (ADR-A006).
- **KC-15 [v22] — berkas klines BULANAN dapat kehilangan HARI UTC penuh yang
  datanya utuh di berkas HARIAN.** **3** simbol-bulan, semuanya BNXUSDT 2022,
  **7.200 menit = 5×1440**. Kebijakan: ADR-A007 (pemulihan dari harian).
- 9 + 3 = **12** karantina; 6.375 + 7.200 = **13.575** menit ✅
- **KC-16 DITARIK [v23] — nomornya TETAP kosong selamanya.** Dugaan "gerbang
  buta terhadap tepi bulan" GUGUR; 210 menit BNXUSDT 2022-04 adalah awal
  pengutipan yang sah.
- **KC-17 [v24] — parquet karantina tidak dipersistenkan meskipun diukur dan
  didaftar.** Pengemas di `pecahan.py` hanya menerima `baris.get("parquet")`,
  sedangkan baris karantina menaruh jalurnya di `parquet_karantina`. Akibatnya
  **12 berkas, 13.247.705 B** hilang bersama runner, padahal ADR-A006 berbunyi
  "disisihkan, bukan dibuang". Bukti dua arah: kode, dan selisih
  `simbol_bulan_dinilai` − `cacah_berkas` = cacah karantina di tiap pecahan.
  **Koreksi penomoran (aturan 29):** jurnal 59 menamainya KC-16. Nomor itu sudah
  terikat permanen pada tuduhan yang ditarik di v23, jadi kelas ini bernomor
  **KC-17**; jurnal 59 dibiarkan apa adanya dan koreksinya dicatat di sini.

## Hipotesis

- H-A001: belum diuji.
- H-A002a / H-A002b: H-A002b **GUGUR** (`slot_5m_hadir_saat_1m_hilang` = 0).
- **H-A003: MENANG pada 3, GUGUR pada 9.**
- **H-A004: TIDAK TERUJI dan tidak dapat diuji** (`fapi.binance.com` → 451).
- **H-A005: GUGUR pada rentang yang disampel [v23]** (37 bulan tengah).
- **H-A006 [v24] — serapan bersifat deterministik.** MENANG pada rentang luas:
  kedelapan pecahan pada run `30389402113` menghasilkan `jumlah_baris`,
  `byte_parquet_total`, cacah karantina, dan `nisbah_parquet_per_zip` yang
  identik dengan run `30383278359` (pecahan 1..7) dan `30353584831` (pecahan 0),
  melintasi tiga versi kode. Belum diuji pada rentang waktu panjang — arsip
  historis bisa saja direvisi kelak.

## Papan skor prediksi

R-1..R-120 dirinci v23: TEPAT 78, MELESET 28, SEPARUH 4, TIDAK TERADJUDIKASI 4,
MENUNGGU 6 = 120. R-121..R-131 di jurnal 56. R-132..R-138 di jurnal 56–58.

| # | Prediksi | Status |
|---|---|---|
| R-129 | nisbah bagian per anggota 1,0000..1,0100 | TEPAT (1,00103..1,00114) |
| R-130 | `cacah_berkas` = `cacah_parquet_ditulis` | TEPAT |
| R-131 | total `byte_anggota_total` 31,4..34,0 GB | **MELESET** (28,59 GB pada tujuh pecahan; aturan 44) |
| R-132 | perbaikan pax lolos CI | TEPAT (187 uji, kode 0) |
| R-133 | uji 120 anggota menangkap cacat lama | TEPAT |
| R-134 | `sah` = true di ketujuh pecahan VERSI 4 | TEPAT |
| R-135 | 3 bagian tiap pecahan; total 21 ± 2 | **SEPARUH** (total 20 ✓; pecahan 3 tetap 2) |
| R-136 | kedelapan `sah`; pecahan 0: 2.408 anggota, 3 bagian, 4,10..4,14 GB | TEPAT |
| R-137 | 19.586 anggota; 32,69..32,72 GB | TEPAT (19.586; 32.706.262.375 B) |
| R-138 | 23 ± 2 bagian; nol taksiran terlampaui | TEPAT (23; 0) |

**Total R-1..R-141** (aturan 21): TEPAT **91**; MELESET **32**; SEPARUH **5**;
TIDAK TERADJUDIKASI **4**; MENUNGGU **9** (R-7, R-19, R-20, R-28, R-36, R-37,
R-139, R-140, R-141). 91+32+5+4+9 = **141** ✅ Ramalan berikutnya **R-142**.
N_percobaan = 0.

Catatan kejujuran: jurnal 57 mengadjudikasi ulang R-104..R-106 yang sebenarnya
sudah TEPAT sejak jurnal 50. Pengukuran ulangnya sah, tetapi tidak dihitung dua
kali di sini. Dan tujuh TEPAT terakhir sebagian besar berpita longgar atau
disusun setelah sebagian besar buktinya terlihat — satu-satunya yang benar-benar
berisiko adalah R-131 dan R-135, dan keduanya jatuh.

## Daftar ADR

- ADR-A001 aturan dasar. DITERIMA.
- ADR-A002 serapan. DITERIMA; §3 DIAMANDEMEN oleh ADR-A004 lalu ADR-A007;
  §9 DIGANTI oleh ADR-A006 Keputusan 3.
- ADR-A003 taksonomi rezim. BELUM ADA (nomor dicadangkan).
- ADR-A004 kebijakan KC-6. DITERIMA; berdiri dengan enam klausa.
- ADR-A005 jenis instrumen tahap pertama. DITERIMA.
- **ADR-A006 karantina + persistensi. DITERIMA dan DITERAPKAN untuk data yang
  LOLOS gerbang** (`rilis.py` VERSI pax, `pecahan.py` VERSI 5, workflow dengan
  `gh release create/upload`). **BELUM LENGKAP:** parquet karantina (KC-17).
- **ADR-A007 serapan hibrida. DIUSULKAN**, belum diterima, belum
  diimplementasikan.
- ADR berikutnya **A008**.

## Serapan semesta `perpetual_usdt` — TERUKUR DAN TERPERSISTENSI

Sumber tunggal: run **`30389402113`**, commit `6ee68891`, `versi_pecahan` **5**,
`sidik_kode` **`dff5d33d98abc65d0fac9ebd55393c235358ed34e03a51dddeb6ea8d93bd7a63`**,
`sidik_data` `6128fbb0…`, kode keluar 0 dan kode unggah 0 di kedelapan job.

| i | simbol | simbol-bulan | baris | menit hilang | gagal | nisbah | anggota tar | bagian | byte anggota |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 99 | 2.411 | 103.264.917 | 1.875 | 3 | 1,2295 | 2.408 | 3 | 4.120.562.805 |
| 1 | 99 | 2.468 | 105.765.980 | 2.160 | 3 | 1,2268 | 2.465 | 3 | 4.269.971.639 |
| 2 | 99 | 2.337 | 100.058.416 | 0 | 0 | 1,2293 | 2.337 | 3 | 3.834.773.373 |
| 3 | 98 | 2.154 | 91.884.319 | 615 | 1 | 1,2356 | 2.153 | 2 | 3.382.222.173 |
| 4 | 98 | 2.497 | 106.865.397 | 1.050 | 1 | 1,2327 | 2.496 | 3 | 4.199.469.659 |
| 5 | 98 | 2.741 | 117.671.896 | 0 | 0 | 1,2341 | 2.741 | 3 | 4.574.062.521 |
| 6 | 98 | 2.652 | 114.013.851 | 7.200 | 3 | 1,2399 | 2.649 | 3 | 4.449.859.316 |
| 7 | 98 | 2.338 | 100.317.358 | 675 | 1 | 1,2334 | 2.337 | 3 | 3.875.340.889 |

- Simbol **787**; simbol-bulan **19.598**; baris **839.842.134**; slot
  **839.855.709**; menit hilang **13.575**.
- Gerbang: lolos **19.586**, gagal **12**, `persen_lolos` **99,9388**.
- Zip **26.532.925.083 B**; parquet **32.706.262.375 B**; nisbah **1,2327**.
  Ketiganya dijumlahkan ulang dari kedelapan log dan cocok sampai byte terakhir.
- Kelas risiko: pra_header 1.952, bulan_awal_2020_2021 1.889, terhenti 587,
  non_ascii **19** (9 di P0, 6 di P1, 4 di P2; kosong dan dinyatakan kosong di
  P3..P7 — aturan 37), kendali_baru 10.007.
- **`parquet_dipersistenkan: true` di kedelapan laporan.** 19.586 anggota, 23
  bagian tar ≤1,8 GB, tiap bagian dibaca ulang dengan sha256 cocok,
  `cacah_bagian_taksiran_terlampaui` 0, `cacah_berkas_hilang` 0.
- Tag rilis: `serapan-pecahan-<i>-30389402113`, aset `pecahan_<i>.partNN.tar` +
  `SHA256SUMS`. Tag lama `…-30376241019` (tak sah, taksiran terlampaui) dan
  `…-30383278359` (sah, tanpa pecahan 0) masih ada.
- **Batas kesahihan yang tersisa:** aset rilis belum pernah diunduh dan dibongkar
  di luar runner yang menulisnya, jadi klaim "dapat dipulihkan" belum lengkap.
  Dan parquet karantina tidak ikut tersimpan (KC-17).

## Model ukuran tar — tiga ronde, satu sebab

`rilis.py` menaksir tiap anggota sebagai `KEPALA_ANGGOTA + blok_isi×512`.
Ronde 1 dan 2 memakai kepala 512 B dan gagal di produksi; sebabnya **header pax
1.024 B per anggota** yang ditulis `tarfile` Python ≥3.8 ketika sebuah medan
(misalnya `mtime` pecahan) tidak muat di header ustar. Dengan
`KEPALA_ANGGOTA = 1536` sisa taksiran runtuh ke nol atau tepat ke margin pada
seluruh 23 bagian. Konstanta: `BATAS_BAGIAN` 1.800.000.000, `BLOK_TAR` 512,
`BLOK_PAX` 1024, `REKAM_TAR` 10240, `MARGIN_REKAM` 20480.

## Jumlah uji

**187 TERVERIFIKASI** — `reports/ci_terakhir.json` run `30383126672`, commit
`4b02bb74`, `kode_keluar` 0. Termasuk 17 uji `tests/test_rilis.py`.

## Utang verifikasi

1-5 dan 11 menunggu tahap juri/klasifikasi. 6-23, 25-28 LUNAS.

24. **AKTIF, sebagian LUNAS.**
    - **persistensi data lolos: LUNAS** (run `30389402113`);
    - **persistensi karantina: BELUM** — KC-17, perbaikan direncanakan VERSI 6;
    - pemulihan aset di luar runner: belum pernah diuji;
    - jalur **funding** (`funding_ada` null di seluruh manifes);
    - medan `dugaan_pengganti` (ADR-A005);
    - pemulihan harian ADR-A007 (`sumber_baris`, `cacah_baris_dipulihkan`);
    - karantina artefak 7 hari.
    Mengadjudikasi R-7, R-19, R-20, R-28, R-36, R-37.

## Temuan sampingan yang belum diukur

- Jalur funding: nol kali diuji.
- 15 `SETTLED` lain: apakah punya pendahulu seperti SXPUSDT?
- Daftar `INDEKS` hanya tiga nama, disusun manual.
- Saham dan komoditas token masih terhitung `perpetual_usdt`.
- `.decode("utf-8","replace")` di `klines` membungkam byte rusak.
- Apakah BUSD/USDC layak digabung dengan USDT.
- Sisa 16 simbol non-ASCII belum diuji langsung (3 sudah).
- Sebab KC-14 (H-A004) — tidak dapat diuji. **Sebab KC-15 tidak diketahui.**
- Selisih penyebut diagnosa KC-15: 38 diperiksa, 41 dirancang. Cacat pelaporan.
- `waktu_utc` pada laporan runner berjalan lebih dulu daripada jam sesi; belum
  diselidiki, belum layak disebut cacat.
