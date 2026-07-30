# PROMPT KELANJUTAN v45

Kamu melanjutkan riset LUX-AI. Operator: Diva Juan Nur Taqarrub, GitHub EnVyxS,
zona waktu Asia/Jakarta, bahasa kerja Indonesia. Tenggat: **2 Agustus 2026**.
**BERKAS DI REPO ADALAH KEBENARAN; prompt ini hanya peta dan boleh saja tertinggal.**
v44 memang tertinggal: ia menyuruh membaca laporan `bentangan_kohort` yang TIDAK
PERNAH ADA. Berkas menang atas prompt — itu bukan basa-basi.

## LANGKAH 0 — WAJIB, BERURUTAN, SEBELUM PEKERJAAN APA PUN

1. Baca dokumentasi modul sandbox sebelum memanggil fungsi apa pun. Dilarang
   menebak bentuk masukan alat.
2. Semua operasi GitHub lewat
   `connections.mcpServer_github.runTool({toolName, toolArguments})` dengan
   owner/repo HANYA di dalam `toolArguments`.
3. Baca dari `main` repo `EnVyxS/lux-ai-research`, berurutan:
   - `journal/2026-07-30-123.md` — **adjudikasi R-302 + praregistrasi R-303** (paling penting)
   - `journal/2026-07-30-122.md` — KC-43, KC-44, sebab kegagalan V1
   - `decisions/ADR-A009.md` — arah sebab mati → funding (DITERIMA)
   - `STATE.md` (masih **v43**, blob `a91a4934…`) — belum diperbarui, lihat §UTANG
   - `STATE_LAMPIRAN_EKOR.md` (masih **v3**, blob `89fec927…`) — papan skornya BASI
   - `reports/bentangan_kohort.json` (blob `6040030d…`) bila menyentuh kohort
   - `decisions/ADR-A008.md` (blob `4c3632d6…`) bila menyentuh pembatal §6
4. Baru sesudah itu pekerjaan teknis.

## BATASAN LINGKUNGAN

- Sandbox agen tidak punya jaringan. Semua pengukuran lewat GitHub Actions; agen
  hanya boleh percaya artefak yang DI-COMMIT.
- Tidak ada alat membaca status Actions, tidak ada `workflow_dispatch`. Satu-satunya
  cara menyalakan run adalah push yang MENGUBAH ISI berkas di dalam `paths`
  workflow. Push berisi byte identik tidak melahirkan commit → tidak menyala.
- Tidak ada API patch: `push_files` MENULIS ULANG seluruh berkas. Jangan menulis
  ulang berkas panjang sebelum membacanya utuh (KC-42d); sesudahnya baca ulang dari
  main (aturan 52).
- Batas tulis aman ±25–45 KB. STATE penuh (±55 KB) pernah TERPOTONG SUNYI dua kali
  (KC-42): commit BUKAN bukti keutuhan.
- Batas baca terukur ulang: hasil >±30.000 token DIPOTONG. `reports/funding_semesta.json`
  hanya 27% → TIDAK terukur utuh. Listing `reports/` juga terpotong (89%).
  `reports/bentangan_kohort.json` (38 baris ringkas) **terbaca UTUH** — pola inilah
  yang wajib ditiru: terbitkan ringkasan per SIMBOL, jangan per simbol-bulan.
- `search_code` mengembalikan 0 hasil — pakai `get_file_contents`; path berakhiran
  garis miring melisting direktori.
- Runner punya numpy, pandas, pyarrow, pyyaml, pytest; TIDAK ada scipy/requests.
- Dilarang menulis apa pun di luar repo `lux-ai-research`; `lux-research` baca saja.
- `ci.yml` memakai `paths-ignore` (`journal/**`, `decisions/**`, `hipotesis/**`,
  `reports/**`). Push ke `lux_ai/**`, `tests/**`, `STATE*`, `PROMPT*` MENYALAKAN CI;
  push jurnal/decisions/reports TIDAK.

## POSISI SERAH TERIMA (30 Juli 2026, ±09:55 WIB)

HEAD terakhir diketahui: **`17a594b69e243a83884862122f01b5e1ade4278a`** (jurnal 123
+ ADR-A009), lalu commit ini sendiri.

Urutan giliran lalu: `47e12611` jurnal 122 → **`703daa90` trio bentangan_kohort V2**
→ `24ecf836` laporan bentangan kohort run 30509071237 → laporan CI run 30509071199
→ `17a594b6` jurnal 123 + ADR-A009.

**Papan skor R-1..R-302 = 302:** TEPAT **213** / MELESET **54** / SEPARUH **20** /
TIDAK TERADJUDIKASI **8** / MENUNGGU **7**. Aritmetika 213+54+20+8+7 = 302 ✅.
MENUNGGU: R-7, R-19, R-20, R-28, R-36, R-37, R-199. N_percobaan = 0.
ADJUDIKASI RISET TETAP TERKUNCI.

- **R-301 = TIDAK TERADJUDIKASI** — laporannya tidak pernah ada (bukan MELESET).
- **R-302 = SEPARUH** — butir 1 dan 3 MENANG, butir 2 KALAH, butir 4 (MUDAH) MENANG.
- **R-303 sudah DIPRAREGISTRASI** di jurnal 123 §5. Modulnya belum dibuat.

Aturan sampai **76** (calon 77, 78, 79 — 79 kini **tiga kali** teruji berhasil).
KC sampai **KC-44**. Hipotesis terbuka: H-A016, H-A017 (H-A015 naik derajat).
Jurnal berikutnya **124**. STATE berikutnya **v44**. PROMPT berikutnya **v46**.
ADR berikutnya **A010**. Ramalan berikutnya **R-304** (R-303 sudah tertulis).

## APA YANG TERUKUR PADA GILIRAN LALU

1. **`tests/test_bentangan_kohort.py` V1 terbaca UTUH** (blob `539336cb…`): 45 butir,
   `test_01`…`test_45`. Utang aturan 52 dari v44 LUNAS.
2. **CI 814** pada `ffa45371` (run 30486876254, kode 0). 769 + 45 = 814 ✅.
3. **Laporan `bentangan_kohort` V1 TIDAK ADA** — tiga berkas gagal dibaca, dan tidak
   ada commit laporan sama sekali. Sebabnya DUA, keduanya milik penulis:
   - **KC-43**: `bentangan_kohort` V1 memakai `silang_funding.lubang_funding` dan
     `baca_medan_baris` yang mengembalikan **PASANGAN** sebagai dict (`tuple` tidak
     punya `.get` → `AttributeError`), dan mengira kunci laporan kehidupan berupa
     STRING padahal `Kunci = Tuple[str, str]`.
   - **KC-44**: `git add -f a b c || true` bersifat semua-atau-tidak-ada, sehingga
     run yang gagal tidak meninggalkan jejak apa pun — bahkan lognya.
4. **Trio V2 didorong** (`703daa90`): modul memperlakukan kunci tuple sebagai kanon,
   membongkar kedua pasangan dengan benar, dan tiga butir uji memanggil
   `silang_funding` ASLI untuk memeriksa bentuk kembaliannya (penangkal KC-43).
   Workflow kini `git add` PER BERKAS + `if: always()` (penangkal KC-44).
5. **Laporan V2 terukur, terbaca UTUH**: run **30509071237**, commit `703daa90`,
   kode **0**, `sidik_kode` `8ca6ebbe…`, blob `6040030d…`, status blob `ccb41854…`.
   Penyebut **19.586** (`selisih_penyebut` 0), kohort **38**, tanpa label **0**,
   `cacah_kunci_gagal_pisah` **0**, `kendali_sah` **true**, `sidik_seragam` **true**.
6. **CI 832** pada `703daa90` (run 30509071199, kode 0). Hitung tangan:
   814 − 45 (butir V1 dihapus) + 63 (butir V2) = **832** ✅. Riwayat CI:
   630→638→662→694→722×8→769→814→**832**. Cacah uji TIDAK diramalkan lagi, hanya diukur.

## HASIL RISET BARU (R-302, penyebut 38 anggota kohort puncak 2025-07)

- `cacah_simbol_hidup_sesudah_tebing` = **0 dari 38**, dan nol ini SAH: seluruh 38
  punya ≥5 bulan HIDUP (STRAXUSDT 5/33 terendah; BALUSDT 55/70 dan OMGUSDT 55/72
  tertinggi) serta `bulan_terakhir` = 2026-06 pada 38/38 (aturan 74).
- Bulan hidup terakhir tersebar **2022-06 (SCUSDT) sampai 2025-04 (ALPACAUSDT)**;
  jarak ke tebing **3–37 bulan**, median ±8. Tabel lengkap 38 baris ada di jurnal 123 §2.
- `cacah_simbol_mati_tersisip` = **0 dari 38**. Semua monoton: satu rentetan HIDUP
  lalu satu rentetan MATI. `rentetan_mati_terpanjang` = `cacah_mati` pada 38/38;
  `rentetan_hidup_terpanjang` = `cacah_hidup` pada 37/38 (kecuali **BNXUSDT** 31≠33).
- `cacah_simbol_bangkit` = **0 dari 38**. **LITUSDT bukan anggota kohort** (lubangnya
  TENGAH), jadi kebangkitan masih satu kejadian dari satu simbol.
- **37 anggota ber-`cacah_bulan_berlubang_funding` = 12**; **BNXUSDT = 19**.
  Hitung tangan: 37×12 + 19 = 463; 463 − 7 (lubang BNX bukan ekor) = **456** =
  angka kohort puncak yang sudah diterbitkan ✅. BNX 19 juga persis angka H-A015 —
  dua jalan berbeda bertemu, tapi irisan bukan sebab (aturan 10).
- `cacah_lubang_funding` **880** di laporan ini adalah lubang SEMESTA, bukan 877 di
  dalam penyebut. Jangan disamakan (KC-9, aturan 36).
- **ADR-A009 DITERIMA**: mati dulu, funding kemudian; kata **"serentak" DITOLAK**
  untuk hubungan kematian–tebing (yang serentak hanya penerbitan antar-simbol).
  Pembatalnya tertulis di ADR-A009 §5 — R-303 adalah ujian bebasnya.

## PEKERJAAN PERTAMA, BERURUTAN

1. **UTANG ATURAN 52 (baru):** baca UTUH dari main
   `lux_ai/serapan/bentangan_kohort.py` V2 dan `tests/test_bentangan_kohort.py` V2
   (didorong pada `703daa90`, BELUM dibaca ulang byte demi byte). Bukti tak langsung
   keutuhannya sudah ada — CI 832 kode 0 dan laporan kode 0 — tetapi itu BUKAN
   pembacaan. Cacah butir uji V2 dari daftar bernomor (`test_01`…`test_63`).
2. **Bangun penguji R-303** (praregistrasi sudah tertulis di jurnal 123 §5, JANGAN
   diubah bunyinya): `mati_tersisip` atas seluruh **19.586** simbol-bulan / **787**
   simbol. Wajib: kendali positif, penggugur `selisih_penyebut`/`kendali_sah`,
   keluaran RINGKAS per simbol agar terbaca utuh, dan listing direktori lebih dulu
   (aturan 66). Tiru anatomi trio V2 dan workflow-nya yang sudah terbukti.
3. **STATE v44** — lihat §UTANG di bawah; ini utang terbesar.
4. `STATE_LAMPIRAN_EKOR.md` v4: papan skor 302, KC-43, KC-44, putusan calon aturan.
5. Cacah tangan listing `lux_ai/serapan/` dan `.github/workflows/` (aturan 66).
   Menurut isi commit: `ffa45371` menambah satu berkas di masing-masing (harusnya
   **40** dan **35**), `703daa90` tidak menambah apa pun — tetapi CACAH SENDIRI.

## UTANG YANG WAJIB DISEBUT APA ADANYA

- **STATE v44 BELUM DITULIS.** STATE penuh ±55 KB dan pernah terpotong sunyi dua
  kali; ia tidak boleh ditulis ulang tanpa dibaca UTUH pada giliran yang sama, dan
  giliran lalu memilih menghabiskan anggarannya untuk MENGUKUR alih-alih menulis
  ulang. Papan skor terbaru karena itu hidup di jurnal 123 §8 dan di prompt ini.
  Cara aman: baca STATE utuh, lalu tulis dalam dua berkas (bagian 1 + lampiran),
  masing-masing di bawah 45 KB, lalu BACA ULANG keduanya.
- `STATE_LAMPIRAN_UKUR.md` (blob `0e9ec378…`, baca UTUH lebih dulu) belum memuat:
  814/832, H-A017, bentangan 38 anggota, API `bentangan_kohort` V2, premis taksonomi.
- `STATE_LAMPIRAN_EKOR.md` v3 papan skornya masih 300.
- Belum dibaca sesi lalu: `decisions/ADR-A002.md`, A004, A006, A007, `PETA_MODUL.md`,
  `PETA_MODUL_BERKAS.md`, `STATE_LAMPIRAN.md`, `STATE_LAMPIRAN_ANGKA.md`,
  `karantina_semesta.yml`, `tests/test_pulihkan.py`, `test_rilis_karantina.py`,
  `test_karantina_a006.py`.

## PEKERJAAN BERIKUTNYA SESUDAH R-303

1. Uji **H-A017** (byte parquet: MATI < ±500 ribu, HIDUP > ±1,4 juta) atas semesta
   dengan pita yang bisa kalah + kendali positif. Bahan baru: `byte_parquet_total`
   dan `cacah_lilin_total` per anggota kohort sudah ada di laporan bentangan.
2. Uji **H-A016** (celah kelipatan 15 menit) atas simbol-bulan lolos gerbang.
3. Putuskan calon aturan **77** (dua berkas berblob identik bukan dua pengukuran),
   **78** (batas alat sebagai bagian desain), **79** (praregistrasi di jurnal — kini
   tiga kali berhasil, layak diterima), dan pertimbangkan calon baru dari KC-43:
   **tanda tangan fungsi yang dipakai wajib dikutip di pemakainya**.
4. TANGGAL hari hilang BNX 2022-04/06/08; irisan 880 lawan 877; selisih 40−38 sampel
   `diagnosa_kc15`; `ukur_baris` V6 (KC-26).
5. ADR: A003 (LITUSDT + bulan absen + aturan 76 + KC-40), terima/tolak A007,
   terapkan A006, `dugaan_pengganti` (A005).
6. Adjudikasi R-7/19/20/28/36/37 dan R-199; gali bunyi R-28 dari STATE v23 (KC-32);
   salin R-236..R-247 dari jurnal 92–94; masukkan R-229 TEPAT dan R-230 MELESET.

## API TERVERIFIKASI (JANGAN DITEBAK — INI PELAJARAN KC-43)

```
silang_funding (blob 42c3aa9d, VERSI 2):
  Kunci = Tuple[str, str]                       # (simbol, bulan) — TUPLE
  baca_laporan_kehidupan(akar, total) -> (Dict[Kunci,str], Dict[Kunci,int], meta)
  baca_medan_baris(akar, total, medan)  -> (Dict[Kunci,Any], meta)
  lubang_funding(funding)               -> (Set[Kunci], meta)
  bulan_per_simbol, bentuk_lubang_lokal, kendali_silang, kendali_sah, sidik_kode,
  SUMBER_FUNDING, MEDAN_LILIN "cacah_lilin", KENDALI_CACAH 3, TOTAL_PECAHAN 8
kehidupan: STATUS_MATI/SEPI/HIDUP/TAK_TERUKUR (nilainya "MATI"/"SEPI"/"HIDUP"/…)
kehidupan_arsip: TOTAL_PECAHAN = 8, nama_keluaran(i)
  medan baris nyata: ada_di_arsip, bagian_volume_nol, bulan, byte_parquet,
  cacah_baris_cacat, cacah_lilin, cacah_lilin_terbaca, cacah_volume_nol, galat,
  gerbang_lolos, jalur, simbol, status, transaksi_total
kohort_ekor V4 (blob c9b63bbe): muat_kohort(akar) -> {simbol, bulan_mulai,
  cacah_simbol_kohort, galat}; mundur_bulan(bulan, langkah); bagian(a,b);
  sepi(baris); ramai(baris); TEBING "2025-07"; BULAN_DIHARAPKAN "2026-06";
  KENDALI_HIDUP ("BTCUSDT","ETHUSDT"); BATAS_SIMBOL 10; PAGU_MUNDUR 60;
  SUMBER "reports/funding_semesta.json"
bentangan_kohort V2: sidik_kode, pisah_kunci(kunci)->Optional[(simbol,bulan)],
  kelompokkan(status)->(peta, gagal), bulan_berstatus, mati_tersisip, bangkit,
  rentetan_terpanjang, ringkas_simbol, uji_r301, kendali_positif, kendali_sah,
  kode_keluar(laporan), jalankan(akar, total=None), main
anatomi_tengah V1: bentangan, status_bulan, mati_tersisip, ringkas_simbol,
  rentetan_terpanjang, bulan_berstatus, uji_r300, kode_keluar, jalankan
lubang_tengah V2: TENGAH_TERCATAT 6, SIMBOL_TENGAH_TERCATAT ["BTCSTUSDT","LITUSDT"],
  SIMBOL_H_A011 "LITUSDT"
```

## ANGKA TERVERIFIKASI

787 penyebut (arsip 937, 150 hanya-arsip), 21.789 bulan arsip, 15 nama SETTLED
(36 bulan), 19.598 simbol-bulan (lolos **19.586**, gagal 12 karantina),
MATI **1.401** / SEPI 98 / HIDUP 18.087, 839.842.134 baris, funding **880** lubang
(877 dalam penyebut: awal 45/48, ekor 826, tengah 6), 33 HIDUP tanpa funding,
taksonomi 9 kelas, ekor 2026-06 = 808 hidup, kohort puncak 2025-07 = **38** simbol /
**456** simbol-bulan / seragam 2026-06, riwayat CI 630→638→662→694→722×8→769→814→**832**.

## KEBIASAAN YANG MENGIKAT

Ramalan SEBELUM run lalu adjudikasi jujur; praregistrasi ditulis di jurnal lebih
dahulu (aturan 79); hitung ulang tiap angka (21); sediakan medan penggugur (24);
kelas cacat pada sampel (37); dilarang menyimpulkan di luar rentang (20); kendali
positif wajib (50); laporan tak terbaca utuh = tidak ada (52); cacah butir uji dari
daftar bernomor (54/56/57); ketiadaan pengukuran bukan ketiadaan gejala (59);
listing direktori sebelum menulis modul baru (66); nama turunan bersama asalnya (69);
baca modul penghasil sebelum meramalkan laporannya (71) — **dan sesudah KC-43: baca
TANDA TANGAN-nya, bukan hanya namanya**; jangan meramal isi berkas dari NAMA-nya (73);
setiap nol bersama penyebutnya (74).
Ramalan yang hanya menyalin angka terverifikasi adalah MUDAH — katakan begitu.
"lanjut"/"lanjutkan" berarti teruskan tanpa konfirmasi. Jangan berhenti dengan
alasan konteks Notion.

## CATATAN KEJUJURAN

Giliran lalu tidak mengadjudikasi apa pun sampai ia lebih dulu mengakui bahwa
laporan yang dijanjikan v44 tidak ada, dan bahwa kedua sebabnya adalah cacat
kode dan cacat workflow buatan sendiri, bukan cacat arsip. R-302 keluar SEPARUH
karena butir yang paling diinginkan — adanya kematian yang berselang-seling —
KALAH 0 dari 38. Butir MUDAH-nya disebut MUDAH di muka. ADR-A009 diambil karena
prasyaratnya lunas, bukan karena ia enak dibaca, dan pembatalnya ditulis di ADR
itu sendiri agar bisa dibunuh oleh R-303.

Mulai dari LANGKAH 0. Jangan mengukur apa pun sebelum praregistrasi ramalan
berikutnya ditulis di jurnal — R-303 sudah tertulis, jadi ia boleh langsung diukur.
