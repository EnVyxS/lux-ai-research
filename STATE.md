# STATE — versi 17

Diperbarui: 2026-07-28 (sesi 36). Aturan hanya BERTAMBAH; jangan menulis ulang
dari ingatan. Versi ini disusun setelah v16 dibaca UTUH dari `main` (blob
`dd9970640fa2a5e2b57d66c410a410c137bab14c`), bukan dari rekonstruksi.

## Aturan bernomor

1. Satu definisi R (ADR-A001 §1). Laporan dengan definisi lain ditolak.
2. Gerbang KANDIDAT ADR-A001 §2 berlaku penuh; butir 7 (rezim) DITANGGUHKAN
   sampai ADR-A003 ada.
3. Adjudikasi hipotesis DILARANG sebelum semesta data lengkap dan manifesnya
   terverifikasi. Pembangunan juri di atas 12 simbol probe boleh jalan paralel.
4. `backtest.py` modul warisan tidak boleh dipakai.
5. Angka mana pun dari modul warisan adalah klaim, bukan bukti.
6. Nol koneksi ke bursa; hanya arsip publik `data.binance.vision`.
7. Setiap laporan memuat `sidik_kode` dan `sidik_data`; laporan dengan
   `sidik_data` berbeda tidak boleh dibandingkan.
8. Tidak ada berkas kode BARU melebihi 800 baris; berkas tier A (angkat
   byte-identik) dikecualikan dan wajib punya catatan pengangkatan.
9. Tidak ada skrip `__main__` di akar repo. Satu jalur eksekusi per fungsi.
10. Keluaran diagnostik selalu ditandai `"bukan_bukti": true` dan tidak boleh
    menyentuh gerbang, ambang, konfigurasi, atau putusan.
11. Biaya (fee taker/maker terpisah, funding bertanda benar, slippage yang selalu
    merugikan) adalah bagian JURI sejak hari pertama, bukan money management.
12. **[v2]** Guard struktural dilarang memakai pencarian kata atas kode atau
    berkas konfigurasi. Guard wajib mengukur strukturnya (mis. AST), dan CARA
    MENGUKUR itu sendiri wajib punya uji dengan kasus positif dan negatif.
13. **[v3]** Sandbox agen TIDAK punya akses jaringan. Setiap pengukuran dan
    unduhan arsip dijalankan runner, dan agen hanya boleh mempercayai artefak
    yang di-commit.
14. **[v3]** Uji di CI dilarang menyentuh jaringan.
15. **[v3]** Kode dari jalur riset lain hanya boleh masuk atas izin eksplisit
    operator, disalin apa adanya, disertai catatan asal dan blob sha. HASIL,
    angka, dan putusan dari repo lain tidak pernah boleh masuk.
16. **[v4]** Setiap medan laporan wajib dinamai menurut apa yang benar-benar
    diukurnya. Ramalan yang lulus lewat medan yang salah ukur dihitung TIDAK
    teradjudikasi.
17. **[v4]** Bila data yang dibutuhkan biaya hilang untuk suatu simbol-bulan,
    simbol-bulan itu dikeluarkan dari backtest. Dilarang menggantinya dengan nol.
18. **[v5]** Gerbang yang LOLOS wajib melaporkan CACAH hal yang benar-benar
    dibandingkan. Gerbang hijau tanpa cacah dianggap belum menguji apa pun.
19. **[v5]** Aritmetika atas harga dan volume arsip memakai Decimal atas teks
    aslinya. Float dilarang di jalur perbandingan data.
20. **[v6]** Setiap pengukuran wajib menyebut RENTANG yang benar-benar disampel,
    dan kesimpulan dilarang melampaui rentang itu.
21. **[v7]** Setiap angka ringkasan yang saya tulis sendiri wajib dihitung ulang
    dari barisnya saat berkas diperbarui.
22. **[v8]** `sidik_kode` wajib mencakup SELURUH berkas yang ikut menentukan isi
    laporan, termasuk modul yang dipanggil dari modul lain.
23. **[v9]** Gerbang yang MERAH dilarang dilonggarkan sebelum sebab kegagalannya
    terukur. Toleransi, pengecualian bulan, dan ambang "cukup dekat" hanya boleh
    lahir dari ADR yang memuat angka terukur.
24. **[v10]** Setiap pengukuran sebab wajib memuat medan yang dapat MENGGUGURKAN
    hipotesis yang sedang saya percayai, dan medan itu dilaporkan walau nilainya
    nol.
25. **[v11]** Parameter cakupan sebuah pengukuran (mis. K bulan yang disampel,
    cara memilih bulan kendali) wajib dipatok tertulis SEBELUM run dan tidak
    boleh disetel ulang setelah hasilnya terlihat.
26. **[v12]** Ramalan yang memakai kata mutlak ("nol", "seluruh", "tidak ada")
    wajib disertai ramalan BESARAN pendamping.
27. **[v13]** Ramalan pendamping besaran dilarang BERSYARAT pada hasil ramalan
    lain. Ramalan bersyarat dihitung TIDAK TERADJUDIKASI.
28. **[v14]** Ekstrapolasi cacah dari sampel bulan AWAL ke bulan lain dilarang
    tanpa menyatakan bahwa bulan awal PARSIAL dan mengoreksinya. R-42 meleset
    46% justru karena mengalikan rerata bulan parsial dengan jumlah bulan penuh.
29. **[v15]** Bila sebuah ADR diamandemen, teks lama TIDAK dihapus. Amandemen
    ditulis sebagai bagian terpisah bernomor, dan penunjuk silang dipasang di
    kepala berkas DAN di kepala bagian yang diamandemen.
30. **[v16]** Setiap laporan diagnostik wajib memuat PENYEBUT-nya secara
    eksplisit, dan bila penyebut itu nol, laporan wajib berstatus
    `TIDAK MENGUKUR`. Ramalan atas medan penggugur DILARANG diadjudikasi TEPAT
    bila penyebutnya nol; status yang benar adalah TIDAK TERADJUDIKASI.
31. **[v16]** Setiap laporan wajib mencatat `sidik_data` sumbernya, dan setiap
    perbandingan antar-run wajib menyebut apakah `sidik_data`-nya sama. Cacah
    byte TIDAK cukup membuktikan dua pengukuran memakai masukan yang sama.
32. **[v16]** Nama pasar TIDAK boleh dianggap ASCII. Setiap penyaring nama wajib
    mencatat CACAH dan CONTOH yang ditolaknya; menolak tanpa mencatat dilarang.
    Pada serapan, nama simbol wajib di-percent-encode saat menyusun URL arsip,
    dan nama berkas keluaran wajib diamankan untuk sistem berkas.
33. **[v17]** Workflow yang menyentuh jaringan wajib dipicu oleh berkas yang
    benar-benar dipakainya, bukan oleh pola direktori. Bila cakupan pemicu
    diperluas, alasannya wajib ditulis di jurnal pada commit yang sama.
34. **[v17]** Dilarang meng-commit direktori laporan secara borongan (`git add
    reports` atau `git add -A reports/`). Setiap workflow hanya boleh meng-add
    berkas yang dinamainya sendiri. Alasannya ketertelusuran: berkas yang
    di-commit oleh job yang bukan pemiliknya membuat pertanyaan "siapa menulis
    angka ini" menjadi mahal — terbukti memakan empat sesi dan dua hipotesis
    gugur (jurnal 30–34).

## Kelas cacat

1. **KC-1 (modul warisan)** — pemilihan default berdasarkan paruh uji.
2. **KC-2 (modul warisan)** — asimetri pencatatan setup diambil vs dilewatkan.
3. **KC-3 (repo ini)** — guard berbasis pencarian kata. Penangkalnya aturan 12.
4. **KC-4 (repo ini)** — format arsip berubah: tanpa header s.d. 2021-12,
   berheader sejak 2022-01. Teruji pada 12 simbol.
5. **KC-5 (repo ini)** — label yang mengukur hal lain daripada namanya.
   DIPERBAIKI lewat `nilai_klaim_delisting`.
6. **KC-6 (arsip)** — berkas 1m dan berkas 5m/15m terbitan Binance TIDAK
   sepakat. Terukur pada 84 simbol-bulan (12 simbol × 6 bulan awal + 1 kendali):
   - Deret 1m UTUH: 0 menit hilang, 0 duplikat, 0 jarak bukan 60 detik pada 84
     dari 84 simbol-bulan. Hipotesis celah menit (H1) mati.
   - Bulan awal: 2.530 dari **790.983** bucket beda = **0,3199%**.
   - Bulan kendali: 1 dari **140.544** = **0,0007%**, yaitu 457 kali lebih
     jarang, tetapi tidak nol (LINKUSDT 2023-04).
   - Gejalanya LANGKA, bukan lazim. Itu tidak mengubah ADR-A004, yang berdiri di
     atas besar beda (~3% pada XRPUSDT 2020-01) dan atas kenyataan bahwa ia tak
     pernah nol — bukan di atas lajunya.
   - Tidak ada N yang aman untuk "buang N bulan pertama": pada N = 6, DOGEUSDT
     masih 202 dan BTSUSDT masih 8.
   - **Diselesaikan oleh ADR-A004**, yang kini ADA DALAM KODE:
     `lux_ai/serapan/gerbang_1m.py`, dan tercatat sebagai Amandemen A-1 di
     `decisions/ADR-A002.md`.
   - BELUM terjawab: mana yang benar, 1m atau 5m/15m terbitan. Ini memerlukan
     verifikasi dari sumber independen yang tidak kami punya.
7. **KC-7 (repo ini)** — laporan yang tampak BERSIH padahal penyebutnya NOL.
   `ringkas_semesta` pertama melaporkan duplikat 0, tidak terurut 0, di luar
   rentang 0 — seluruhnya atas 0 simbol yang diperiksa. Nol pelanggaran atas nol
   pengamatan bukan bukti kebersihan, melainkan bukti pengukuran tidak terjadi.
   Penangkalnya aturan 30.
8. **KC-8 (repo ini)** — sumber bergerak, dikira tetap, karena hanya UKURANNYA
   yang dicocokkan. `reports/semesta_bulan_1m.json` selalu 18.884 B pada empat
   pembacaan, tetapi `sidik_data`-nya berbeda tiap kali (`fae1210f…`,
   `f435f470…`, `7d287ab6…`, `ced89c14…`). **SEBABNYA KINI DIKETAHUI** (jurnal
   33–34): workflow `probe-serapan` menulis ulang laporannya tiap run dan
   meng-commit seluruh direktori. Datanya sendiri tidak berubah: 934 dan 21.770
   terulang persis pada dua run bersidik berbeda. Penangkalnya aturan 31.
9. **KC-9 (repo ini)** — penyaring ASCII-sentris membuang entitas SAH tanpa
   jejak. `POLA_SIMBOL = [A-Z0-9_]{2,20}` membuang tiga pasar bernama huruf
   Tionghoa (币安人生USDT, 我踏马来了USDT, 龙虾USDT) yang memikul 19 berkas-bulan.
   Panjang bukan sebabnya: `panjang_nama_terpanjang` = 16. Penangkalnya
   aturan 32. Titik (a) URL arsip sudah AMAN dan kini dijaga enam uji
   (`tests/test_arsip_kc9.py`); titik (b) nama berkas dan (c) kunci manifes
   menjadi syarat rancangan utang 24.
10. **KC-10 (repo ini)** — pemicu LUAS pada workflow berjaringan.
    `probe_serapan.yml` dipicu oleh `paths: lux_ai/serapan/**`, direktori yang
    menampung setiap modul baru. Akibatnya setiap dorongan modul menyalakan run
    pengunduhan beranggaran 330 menit yang tidak diminta siapa pun. Sensus penuh:
    **1 dari 9** workflow. Penangkalnya aturan 33.
11. **KC-11 (repo ini)** — commit borongan direktori laporan. `git add reports`
    atau `git add -A reports/` membuat sebuah job meng-commit berkas yang bukan
    keluarannya. Sensus penuh: **6 dari 9** workflow (`survei_semesta`,
    `penyebut_kc6`, `diagnosa_kc6`, `rentang_kc6`, `uji_resample`,
    `probe_serapan`); tiga yang patuh adalah `ci`, `ringkas_semesta`,
    `bentuk_semesta`. `probe_serapan` memperberatnya dengan gelung latar
    `while true` + `sleep 600` yang meng-commit tiap 10 menit selama job hidup
    (1 dari 9). Diduga inilah sebab **anomali tree** yang tercatat berkali-kali
    — belum dibuktikan langsung, ini memerlukan verifikasi. Penangkalnya
    aturan 34.

## Papan skor hipotesis

Hipotesis RISET: kosong. Selesai: 0. Kandidat: 0. Ditolak: 0. N_percobaan: 0.

Hipotesis INFRASTRUKTUR (bukan hipotesis riset, tidak masuk N_percobaan):

| Kode | Isi | Status |
|---|---|---|
| H1 | Beda KC-6 dijelaskan celah menit | GUGUR (jurnal 14) |
| H2 | Beda KC-6 bukan dari celah menit | bertahan |
| H-A002a | Selisih 937−934 adalah ulah penyaring saya | **TERBUKTI** (934+3=937) |
| H-A002b | Semesta memang kehilangan tiga simbol | **GUGUR** |
| H-A003 | `semesta_bulan_1m.json` ditulis ulang berkala, isi data tetap | **TERBUKTI intinya, mekanismenya salah** |
| H-A004 | CI yang meng-commitnya lewat `git add reports` polos | **GUGUR** (jurnal 32) |
| H-A005 | `probe_serapan.yml` dipicu `push` tanpa `paths:` | **GUGUR** (jurnal 34) |

Catatan kejujuran atas H-A003: jurnal 30 menyatakannya GUGUR karena tidak ada
`schedule:`. Setelah penulisnya ditemukan (jurnal 33–34), inti klaimnya —
ditulis ulang berkala, isi data tetap — ternyata BENAR; yang salah adalah
mekanisme yang saya andaikan. Vonis "gugur" di jurnal 30 terlalu cepat, dan
koreksi ini ditulis terbuka alih-alih menyunting jurnal lama.

## Papan skor prediksi

R-1..R-55 tercatat lengkap di STATE v16 (blob `dd997064…`) dan tidak disalin
ulang di sini agar berkas ini tetap kecil. Rekapitulasinya: TEPAT 31, MELESET
15, MELESET SEPARUH 2, TIDAK TERADJUDIKASI 1, MENUNGGU 6 = 55.

| # | Prediksi | Status |
|---|---|---|
| R-56 | `arsip.py` tidak percent-encode nama simbol di URL | MELESET: `segmen()` ada, 5 titik pakai |
| R-57 | `arsip.py` menyusun nama berkas dari nama simbol | MELESET: 0 pembentuk nama berkas |
| R-58 | 0 pemanggilan `quote`/`encode` di `arsip.py` | MELESET: ≥ 2 |
| R-59 | CI uji KC-9: 102 uji, kode keluar 0 | TEPAT: run 30349383760 |
| R-60 | Enam uji baru lulus tanpa mengubah `arsip.py` | TEPAT |
| R-61 | Uji gagal 0..1 | TEPAT: 0 |
| R-62 | Nama simbol muncul 0..1 kali di `klines.py` | TEPAT: 0 |
| R-63 | 0 `.upper()` / `encode("ascii")` di `klines.py` | TEPAT |
| R-64 | Titik (b) KC-9 menjadi syarat rancangan utang 24 | TEPAT |
| R-65 | `survei_semesta.yml` punya `schedule:`, 1..2 baris `cron:` | MELESET: 0 |
| R-66 | Workflow itu menulis `semesta_bulan_1m.json` dan commit `[skip ci]` | MELESET SEPARUH: `[skip ci]` benar, penulisnya bukan |
| R-67 | Workflow yang sama menulis `semesta_rentang.json` | TIDAK TERADJUDIKASI: penyebut salah pilih |
| R-68 | `survei.py` menulis hanya di dalam fungsi; 0 penulisan tingkat modul | TEPAT |
| R-69 | Dua workflow tersangka memakai `git add reports` (2 dari 2) | MELESET: 0 dari 2 |
| R-70 | Kata `survei` muncul 0 kali di kedua yml | TEPAT |
| R-71 | `ci.yml` memakai `git add reports` polos (1) | MELESET: 0 |
| R-72 | `ci.yml` menjalankan pytest atas seluruh `tests/` | TEPAT |
| R-73 | Berkas `reports/` bernama di `ci.yml`: 0..2 | TEPAT: 2 |
| R-74 | Riwayat berkas: 3..6 commit pada 08:50Z–09:40Z | TEPAT: 3 |
| R-75 | Pengarangnya bot CI, bukan `push_files` saya | TEPAT: `lux-ci` |
| R-76 | Pesan commit menyebut survei atau penyebut KC-6 | MELESET: probe serapan |
| R-77 | `probe_serapan.yml` tanpa `paths:` (cacah 0) | MELESET: ada, cacah 1 |
| R-78 | Berkas itu commit borongan, cacah 1 | MELESET SEPARUH: borongan benar, cacah 2, bentuk `-A` |
| R-79 | Kata `journal` muncul 0 kali di berkas itu | TEPAT |
| R-80 | Tiga workflow terakhir memakai `paths:` sempit; 0 memakai `serapan/**` | TEPAT |
| R-81 | 1..2 dari ketiganya commit borongan | MELESET: 3 dari 3 |
| R-82 | `while true` muncul 0 kali di ketiganya | TEPAT |

Cacah dihitung ulang baris demi baris (aturan 21), R-56..R-82:

- TEPAT — 15: R-59, R-60, R-61, R-62, R-63, R-64, R-68, R-70, R-72, R-73, R-74,
  R-75, R-79, R-80, R-82.
- MELESET — 9: R-56, R-57, R-58, R-65, R-69, R-71, R-76, R-77, R-81.
- MELESET SEPARUH — 2: R-66, R-78.
- TIDAK TERADJUDIKASI — 1: R-67.

15 + 9 + 2 + 1 = 27, sama dengan cacah baris R-56 sampai R-82.

**Total R-1..R-82:** TEPAT 31+15 = **46**; MELESET 15+9 = **24**; MELESET
SEPARUH 2+2 = **4**; TIDAK TERADJUDIKASI 1+1 = **2**; MENUNGGU **6** (R-7, R-19,
R-20, R-28, R-36, R-37). 46+24+4+2+6 = **82**. ✅

P-1..P-3 dihitung terpisah dan ketiganya masih menunggu. Ramalan berikutnya
**R-83**.

## Daftar ADR

- ADR-A001 — aturan dasar riset. DITERIMA.
- ADR-A002 — serapan data arsip. DITERIMA; **§3 DIAMANDEMEN oleh ADR-A004**,
  tercatat sebagai bagian "Amandemen A-1" di dalam berkasnya sendiri (commit
  `4995940c7aeccf303900c19afb3320029b04b113`, blob
  `3017056456087297e0a83bacbc0d12e7d8e66d36`).
- ADR-A003 — taksonomi rezim/klasifikasi. BELUM ADA.
- ADR-A004 — kebijakan KC-6. **DITERIMA 2026-07-28.** 1m satu-satunya sumber
  kebenaran; gerbang mengikat = integritas struktural deret 1m; 5m/15m terbitan
  tidak diserap; tanpa toleransi; tanpa pengecualian N bulan pertama.
  Penerapannya: `lux_ai/serapan/gerbang_1m.py`.

## Gerbang integritas 1m (ADR-A004 §2 dalam kode)

`lux_ai/serapan/gerbang_1m.py`, enam klausa per simbol-bulan:
`deret_tidak_kosong`, `tanpa_duplikat`, `tanpa_menit_hilang`, `jarak_60_detik`,
`selaras_menit`, `satuan_milidetik`. Ringkasannya wajib memuat `baris_diperiksa`
dan `slot_diperiksa` (aturan 18) serta `simbol_bulan_gagal` dan
`pelanggaran_per_klausa` walau nol (aturan 24). Rumus `ukur_deret` DISALIN dari
`diagnosa_kc6.celah_menit`, bukan diimpor (aturan 10).

**Cacat rumus yang sengaja dibiarkan:** `menit_hilang_dalam_rentang` bisa
NEGATIF bila dua stempel jatuh pada menit yang sama, sebab rumusnya dijaga
identik dengan `celah_menit`. Yang menangkapnya adalah klausa `selaras_menit`,
bukan rumusnya sendiri. Medan itu DILARANG dipakai sendirian (syarat rancangan
utang 24).

Modul ini BELUM pernah melihat data arsip sungguhan (utang 24).

## Sensus workflow (9 dari 9 terbaca, sesi 36)

| Workflow | Pemicu | Commit | Anggaran |
|---|---|---|---|
| `ci` | push (paths-ignore journal/decisions/reports) | 2 berkas bernama | bawaan |
| `ringkas_semesta` | `ringkas_semesta.py` | 3 berkas bernama | 20 mnt |
| `bentuk_semesta` | `bentuk_semesta.py` | 3 berkas bernama | 20 mnt |
| `survei_semesta` | `survei.py` | `git add reports` | 330 mnt |
| `penyebut_kc6` | modulnya | `git add reports` | 20 mnt |
| `diagnosa_kc6` | `diagnosa_kc6.py` | `git add reports` | 120 mnt |
| `rentang_kc6` | `rentang_kc6.py` | `git add reports` | 300 mnt |
| `uji_resample` | `resample.py`, `uji_resample.py`, `klines.py` | `git add reports` | 120 mnt |
| `probe_serapan` | **`lux_ai/serapan/**`** | `git add -A reports/` ×2 + gelung latar | 330 mnt |

Patuh aturan 34: 3. Melanggar: 6. 3 + 6 = 9. ✅

## Status pipeline

| Tahap | Status |
|---|---|
| T0 Peta modul | SELESAI |
| T1 Serapan | Probe SELESAI. Survei semesta SELESAI dan TERINGKAS. KC-6 terukur dan diputus (ADR-A004). Gerbang integritas 1m ADA dalam kode dan teruji. KC-9 titik (a) aman dan dijaga uji. Yang kurang: jalur serapan penuh + manifes per simbol-bulan |
| T2 Klasifikasi | BELUM MULAI (butuh ADR-A003) |
| T3 Sinyal | BELUM MULAI |
| T4 Juri/backtest | BELUM MULAI |
| T5 Adjudikasi | TERKUNCI sampai semesta penuh + manifes terverifikasi |

## Angka arsip yang sudah terverifikasi

| Besaran | Nilai | Sumber |
|---|---|---|
| Simbol di indeks arsip | 937 (empat run) | `probe_serapan.json`, `ringkas_semesta.json` |
| — di antaranya bernama non-ASCII | 3 (币安人生USDT, 我踏马来了USDT, 龙虾USDT) | `ringkas_semesta.json` |
| Berkas bulanan 1m | 21.789 (= 21.770 ASCII + 19 non-ASCII) | idem |
| Rentang arsip | 2020-01 s.d. 2026-06 | `survei_semesta.json` |
| Bulan per simbol: terkecil / terbesar | 1 / 78 | `ringkas_semesta.json` |
| Simbol terhenti / masih terbit | 128 / 809 | `survei_semesta.json` |
| Peralihan format | tanpa header s.d. 2021-12; teruji 12 simbol | `uji_resample.json` |
| Satuan stempel | milidetik, 237 bulan disampel, seragam | `survei_semesta.json` |
| Batas atas total zip / parquet | 25,86 GB / 39,17 GB | `probe_serapan.json` |
| Gerbang resample bulan AKHIR | 12/12 bersih | `uji_resample.json` |
| Integritas 1m | 84 dari 84 simbol-bulan bersih sempurna | `rentang_kc6.json` |

## Jumlah uji

**102, TERVERIFIKASI** — `reports/ci_terakhir.json` (blob
`21001dc2876f24e0dcfb06fbefaed7e4d43da4e5`), run **30349383760**, commit
`65e4f5f9ff657cca66712823739d402cabecb545`, 2026-07-28T10:06:20Z,
`kode_keluar: 0`, `"102 tests collected in 0.36s"`.

## Utang verifikasi

1. Temuan A dan B (rasio isi 5,84%; 96% trendline break) menunggu juri.
2. Temuan G: klaim "30 pair dipilih alfabetis" belum ditemukan buktinya.
3. Atribut `enable_hs` dipakai `strategy.py` tetapi tidak ada di `config.py`.
4. Klaim temuan N (kendala mengikat = kapasitas margin) belum diuji angkanya.
5. Angka 0,3232R dan 0,306R warisan belum diverifikasi.
6. ~~Ukuran ADR-A001~~ DIBAYAR.
7. ~~Percent-encoding simbol non-ASCII~~ **LUNAS** (jurnal 26–28): titik (a)
   sudah aman lewat `arsip.segmen()` dan dijaga `tests/test_arsip_kc9.py`;
   titik (b) dan (c) melebur menjadi syarat rancangan utang 24.
8-23. DIBAYAR (rincian di STATE v16).
24. **AKTIF — satu-satunya pekerjaan besar tersisa.** `gerbang_1m` belum pernah
    melihat data arsip sungguhan dan belum dipanggil jalur serapan mana pun.
    Sampai itu terjadi, kalimat "gerbang integritas berlaku atas 21.789
    simbol-bulan" dilarang ditulis. **Tujuh syarat rancangan mengikat:**
    (a) nama berkas parquet diamankan untuk sistem berkas, bukan disalin mentah;
    (b) kunci manifes sadar non-ASCII sejak baris pertama;
    (c) `baris_dibuang` dari `klines.rapikan` wajib masuk manifes (aturan 18);
    (d) `menit_hilang_dalam_rentang` dilarang dipakai tanpa `selaras_menit`;
    (e) commit hanya berkas bernama (aturan 34);
    (f) pemicu workflow sempit (aturan 33);
    (g) tambalan enam workflow pelanggar aturan 34 + tiga cacat `probe_serapan`
        digabung ke commit yang sama, supaya hanya satu run menyala.
25. ~~Siapa menulis ulang `semesta_bulan_1m.json`~~ **LUNAS** (jurnal 33–34):
    workflow `probe-serapan` lewat bot `lux-ci`; irama 13–25 menit berasal dari
    gelung latar 10 menit dan dari dorongan saya sendiri ke `lux_ai/serapan/**`.
26. ~~Lima berkas belum dibaca ulang dari `main`~~ **LUNAS** (jurnal 29): kelima
    berkas dibaca ulang, nol terpotong.

Utang AKTIF: **24 saja**. Utang 1-5 dan 11 menunggu tahap lain.

## Temuan sampingan yang belum diukur

- `klines.baris_pertama`/`baca_zip` memakai `.decode("utf-8", "replace")`,
  mengganti byte rusak dengan U+FFFD tanpa bersuara — kerabat KC-9. Dampaknya
  *diduga* kecil karena hanya untuk deteksi header. **Ini memerlukan verifikasi.**
- Apakah `arsip.bulan_tersedia` (prefix mentah → `urlencode`) aman untuk simbol
  Tionghoa: belum diperiksa.
- Anomali tree (pembacaan setelah push dilayani dari tree berbeda, blob sha
  selalu cocok): calon penjelasannya gelung latar `probe_serapan` (KC-11).
  **Belum dibuktikan langsung.**
