# STATE LAMPIRAN EKOR - v22

Lampiran ekor bagi `STATE.md` v64 (commit `7c479f1a`). Berisi indeks, rantai, dan registri.
Angka terukur beserta larangannya ada di `STATE_LAMPIRAN_UKUR.md`.

**Ditulis:** 2026-07-31, menggantikan v21 (commit `40448545`).

> **PERINGATAN KEUTUHAN.** Berkas ini **ditulis ulang**, bukan ditambal, dan disusun dari
> catatan kerja sesi 2026-07-31. Butir tertentu dari v21 mungkin tidak terbawa kata demi
> kata. **v21 tetap sah di riwayat git pada commit `40448545`** dan menjadi rujukan bagi apa
> pun yang tidak muncul di sini. Disebut supaya batas keandalan berkas ini diketahui.

---

## 1. Rantai commit sesi 2026-07-31

Terbaru ke lama. Bot CI ditandai `[bot]`.

| commit | isi |
| --- | --- |
| `7c479f1a0362d75eb64e472b9404e9cfdbead474` | **STATE v64** |
| `f0ca69ecfc1f10ede233887e79b4d7a5e1bdfe4b` | jurnal 164 - ADJ R-323 |
| `4f98bef834433e5a3f3e270301ba5ea2f561e29b` | `.github/workflows/sumber_funding.yml` |
| `d0a7c3272500a8d6653be1101464ac62a1565f10` | `lux_ai/serapan/sumber_funding.py` |
| `f1fd5d8d75fddb10843e074e91c3f8247e41f509` | jurnal 163 - PRAREG R-323 |
| `c91d1ac8947beda8e435bfb596a77f86f7bac3ea` | jurnal 162 - ADJ R-322 |
| `41000f5d214109576735aee46f93648806522bee` | `.github/workflows/peta_funding.yml` |
| `386381f692ec3f7109cb2dba81ede76aa05e8cf5` | jurnal 161 - PRAREG R-322 |
| `f0807165280557d102b4e0cd963a44869034de61` | `lux_ai/serapan/peta_funding.py` |
| `20c78e08` | ADR-A024 |
| `5d0a3438` | jurnal 160 |
| `9d30060e` | jurnal 159 - ADJ R-321 |
| `c2fd93f5` | `peta_manifes.yml` v2 |
| `02be565f` | jurnal 158 - PRAREG R-321 |
| `c766852d` | [bot] |
| `3439c2b9` | `peta_manifes.yml` v1 - **kegagalan bisu** |
| `e513d0ec` | `lux_ai/serapan/peta_manifes.py` |
| `884790ce` | [bot] |
| `e86f468f` | UKUR v21 |
| `d2455b83` | [bot] |
| `40448545` | **EKOR v21** |
| `4ec4eed8` | [bot] |
| `3f5ec7e4` | **STATE v63** |
| `a8acbeba` | ADR-A023 |
| `4dc444f0` | [bot] |
| `8e6f583d` | UKUR v20 |
| `713825d6` | [bot] |
| `b1d1ed36` | EKOR v20 |
| `27c7a7eb` | [bot] |
| `f5019bb6` | STATE v62 |

Sebelumnya: `9654890e` (157) - `a5b4ab70` (156) - `65b77d39` (155) - `6326a18d` (154) -
`a90d543a` (153) - `1aa3fe3a` (152) - `f92c0dcf` (ADR-A022) - `72e49824` [bot] -
`bb959b62` (STATE v61) - `2da162ed` [bot] - `9d159e1e` (UKUR v19 PADAT) -
`c28202df` (UKUR v19 CACAT) - `4bf883c4` [bot] - `b8877a27` (EKOR v19) - `06d62085` (151) -
`6894b02f` (150) - `e08a0a2a` [bot] - `8345668e` (STATE v60) - `fccd2e12` (149) -
`1ba0a007` (148) - `8e0b39a5` [bot] - `51c65e2a` (UKUR v18) - `64b03bdb` [bot] -
`bb565f4c` (EKOR v18) - `9e43911b` [bot] - `05f6f72e` (STATE v59) - `24b53ba5` [bot] -
`72fe177c` (UKUR v17) - `14f3316e` [bot] - `c0877746` (EKOR v17) - `e271a711` [bot] -
`839a0f17` (STATE v58) - `e429e4fb` (147) - `440fe8ba` (146) - `9b01c06e` (UKUR v16) -
`47769b18` [bot] - `32413935` (EKOR v16) - `ff89f688` [bot] - `ebe6f373` (STATE v57) -
`2cee14b7` (ADR-A021) - `526e41e8` (145) - `1146b96a` (144) - `c4a7468e` [bot] -
`d551f471` (UKUR v15) - `019d16ea` (STATE v56).

---

## 2. Registri blob - artefak sesi ini

### Modul dan workflow

| berkas | blob | commit |
| --- | --- | --- |
| `lux_ai/serapan/peta_manifes.py` | `65adcc37...` 15.987 B | `e513d0ec` |
| `.github/workflows/peta_manifes.yml` v1 | `45a34f35...` | `3439c2b9` |
| `.github/workflows/peta_manifes.yml` v2 | `b60b430e...` | `c2fd93f5` |
| `lux_ai/serapan/peta_funding.py` | `05266922d7af456ec8da2af23d7bbefe7d7244ab` | `f0807165` |
| `.github/workflows/peta_funding.yml` | `860d8b8ec006d0ff53a9acf2dfa73fbb34cea690` | `41000f5d` |
| `lux_ai/serapan/sumber_funding.py` | `bc4472a0551ab559f4566580adf024656c9040ba` | `d0a7c327` |
| `.github/workflows/sumber_funding.yml` | `7ce324c16342884f48606e3ed8408d4597f8c4b1` | `4f98bef8` |

### Laporan yang lahir sesi ini

| laporan | blob | byte |
| --- | --- | --- |
| `reports/peta_manifes.json` | `d392201123d26062ad1e40e1787e91d9207c13a0` | 69.736 |
| `reports/peta_manifes.log` | `6fff9609...` | 3.029 |
| `reports/peta_manifes_status.json` | `3ac255c1...` | 195 |
| `reports/peta_funding.json` | `3e5139aafc1ffc366d8ce4e8601ff41808f55d8f` | 8.392 |
| `reports/peta_funding.log` | belum dibaca | 1.031 |
| `reports/peta_funding_status.json` | `4e0bc8f20d67e76e046c5c13864bbb7226599e80` | 216 |
| `reports/sumber_funding.json` | `b62538b54cf43959b2a16c376c9718ccd0533c44` | **24.963** |
| `reports/sumber_funding.log` | belum dibaca | 1.107 |
| `reports/sumber_funding_status.json` | `56032437d98e84aaecbc6b0f6b079151961d59df` | 217 |

### Artefak tulisan

| berkas | blob | commit |
| --- | --- | --- |
| `decisions/ADR-A024.md` | `cb5a07105b594278a73f486c8906ad873358b59e` | `20c78e08` |
| `journal/2026-07-31-161.md` | `f45f53ece21a367e81478eeec8a3916f5429240a` | `386381f6` |
| `journal/2026-07-31-162.md` | `9e69ac56dc0d647f8ebe4a72d95c6b73f7277f22` | `c91d1ac8` |
| `journal/2026-07-31-163.md` | `ce00cfadde06b428f1fcec7bd279191d0cdf2131` | `f1fd5d8d` |
| `journal/2026-07-31-164.md` | `cee2a53ecf37ef86a3972b6ee03009577bb6f345` | `f0ca69ec` |
| `STATE.md` v64 | `75a5d2965a54af83a620fb2bf9a06e388bbf97ae` | `7c479f1a` |

---

## 3. Deret aturan 38 - ke-42 sampai ke-78, 37 pembacaan berturut

| ke- | blob `ci_terakhir.json` | run | commit | waktu UTC |
| --- | --- | --- | --- | --- |
| **78** | `8ad4f4b9a53dc08d7e1a367c833e66d32d73d2d9` | 30625536901 | `7c479f1a` | 11:01:20Z |
| 77 | `edbd1756701d39f635ad05b786884550c027a21b` | 30624776589 | `4f98bef8` | 10:48:10Z |
| 76 | `36ccbdf3bb5e9d29f96902ad616700730c9ce476` | 30623991546 | `41000f5d` | 10:34:30Z |
| 75 | `d76177af2227ef1fedae34fe3b6004fb880a3525` | 30620019935 | `c2fd93f5` | 09:28:21Z |
| 74 | `cb7e8d74...` | 30619655110 | `e513d0ec` | - |
| 73 | `6e87282b...` | 30618758109 | `e86f468f` | 09:07:46Z |
| 72 | `75bee028...` | 30617907684 | `40448545` | - |
| 71 | `a993ff3a...` | 30617261973 | `3f5ec7e4` | - |
| 70 | `e5e01503...` | 30616177405 | `8e6f583d` | - |

Sebelumnya: ke-69 `c91cf8c9` - ke-68 `939d08dd` - ke-67 `2ba9b4eb` - ke-66 `d241b08e` -
ke-65 `87677ef6` - ke-64 `b6835432` - ke-63 `a185f32a` - ke-62 `3f299eaf` - ke-61 `b6d02273` -
ke-60 `990502c7` - ke-59 `5f62452d` - ke-58 `9718bf98` - ke-57 `5b433a93` - ke-56 `34f88b37` -
ke-55 `8ea8cc46` - ke-54 `340c3c7f` - ke-53 `5f4282f6` - ke-52 `19785af1` - ke-51 `aeb4315a` -
ke-50 `04bfa2ed` - ke-49 `94d270e7` - ke-48 `8ec97de5` - ke-47 `8cbbd4ce` - ke-46 `effb3a46` -
ke-45 `cdfdee25`.

**Cacah uji tetap `1377` pada ke-73 sampai ke-78** meski tiga modul baru ditambahkan.

**Cacat deret yang dibukukan:** ke-38 tanpa blob - run `30547842823` tertimpa - laporan
`c28202df` tertimpa. **DILARANG** menghitung laporan CI `c28202df`.

**Pasangan run yang DILARANG dihitung sebagai dua saksi bebas** (lahir dari commit yang sama):
30620019935 / 30620019905 - 30623991546 / 30623991561 - 30624776589 / 30624776552.

---

## 4. Indeks jurnal 144 sampai 164

| no | blob | commit | isi |
| --- | --- | --- | --- |
| 144 | `fcc9374529fd91bd1c9a3d43c34b7f24a86d344e` | `1146b96a` | LANGKAH 0 |
| 145 | `d9b63433e6693a5e012ed14eec1ecc8e9b740e21` | `526e41e8` | LANGKAH 0 |
| 146 | `1992c8ef...` | `440fe8ba` | - |
| 147 | `eaf941f6...` | `e429e4fb` | - |
| 148 | `aae87895...` | `1ba0a007` | `lubang_awal.py` |
| 149 | `200a0bc1...` | `fccd2e12` | papan 325 |
| 150 | `2e55ee54...` | `6894b02f` | `bulan_absen.py` |
| 151 | `5680804d...` | `06d62085` | papan 329 |
| 152 | `ddc3f0c0...` | `1aa3fe3a` | PRAREG R-319 |
| 153 | `b0a009aa...` | `a90d543a` | ADJ R-319, papan 334 |
| 154 | `db255fc5...` | `6326a18d` | `klines.py`, `serap.py` |
| 155 | `02bab071...` | `65b77d39` | PRAREG R-320 |
| 156 | `c81f6e7f...` | `a5b4ab70` | ADJ R-320, papan 339 |
| 157 | `d9a5ec97...` | `9654890e` | `karantina_semesta.json` |
| 158 | `1a8d9ba8...` | `02be565f` | PRAREG R-321 |
| 159 | `ebece3c7...` | `9d30060e` | ADJ R-321 |
| 160 | `39e8f27d...` | `5d0a3438` | cacah tangan 46 dan 51 |
| 161 | `f45f53ec...` | `386381f6` | PRAREG R-322 |
| 162 | `9e69ac56...` | `c91d1ac8` | ADJ R-322, papan 346, KOREKSI 20, butir 23 |
| **163** | `ce00cfad...` | `f1fd5d8d` | **PRAREG R-323** - lima butir, empat sisi |
| **164** | `cee2a53e...` | `f0ca69ec` | **ADJ R-323, papan 350, KOREKSI 21, utang ukur 36** |

**BELUM DIBACA:** `journal/2026-07-30-125.md` (R-305).

---

## 5. Indeks ADR

| ADR | blob | commit | pokok |
| --- | --- | --- | --- |
| **A024** | `cb5a0710...` | `20c78e08` | aturan 94, penutupan paksa tiga lapis, delapan keputusan |
| A023 | `d2a5302f08442c44176a177baacc2eee0ee5df58` | `a8acbeba` | aturan 77, 78, 93 RESMI; 89 DIPERTEGAS empat sisi |
| A022 | `fd24bb5b...` | `f92c0dcf` | 88/89/91 RESMI; 92 DIPERSEMPIT; KC-56/57 DIBUANG |
| A021 | `3e756672ca355ea976bf2931d278e37fe9057d0d` | `2cee14b7` | LANGKAH 0 |
| A020 | `200c7e7d...` | - | - |
| A019 | `9cd7d25e...` | - | - |
| A018 | `3fba599e` | - | - |
| A017 | `1be570f2` | - | - |
| A016 | `209802d7` | - | - |
| A015 | `387d5510` | - | - |
| A014 | `6d77c2cd` | - | - |
| A013 | `8ba4f989` | - | - |
| A012 | `f9f564d1` | - | - |
| A011 | `645fd5df` | - | - |
| A010 | `c4bccf21` | - | - |
| A009 | `17a594b6` | - | **DICABUT** |
| A004 | `ee603a8c...` | - | 2.2 mencacah LIMA klausa (KOREKSI 17) |

**ADR-A003 BELUM ADA** - blokir 1, murni tulisan. Berikutnya **A025**.
**BELUM DIBACA:** A002, A005, A006, A007, A008.

---

## 6. Pemakaian aturan - pencacah

| aturan | pemakaian | nyala |
| --- | --- | --- |
| 38 | **ke-78** | deret ke-42..ke-78 = 37 berturut |
| 52 | **ke-66** | tiap berkas didorong dibaca ulang segiliran |
| 77 | dua | nol nyala sejak |
| 79 | rekor delapan (R-314..R-321) | **BERAKHIR** di R-322; tidak ada rekor berjalan |
| 85 | empat | - |
| 90 | dua belas | **satu** |
| 91 | dua pemakaian + satu penyebutan | - |
| 93 | dipakai pada R-322 dan R-323 | mencegah pelanggaran aturan 21 dua kali |

**DILARANG** menyebut aturan 77 / 78 / 89 / 90 / 91 / 93 sebagai "teruji".
**DILARANG** menjumlahkan aturan 90 dan 77 - kedua alasan berkorelasi.
**DILARANG** menulis aturan 88 punya dua kejadian.

---

## 7. Kegagalan panggilan alat - TIGA kejadian sesi ini

1. `payload.owner should be not present, instead was "EnVyxS"` dan padanan `payload.repo`.
   Sebab: `owner` / `repo` di tingkat atas `args`, bukan di dalam `toolArguments`.
   Galat sekerabat: `Tool '' does not exist on this MCP server`.
2. `parameter fields could not be coerced to []string, is string`.
   Sebab: `fields` dikirim sebagai teks `"name,size"`; menuntut **larik**.
3. **BARU** - `JSON parse error ... Expected ',' or '}' after property value at position 27317`.
   Terjadi pada percobaan mendorong EKOR v22 rumusan pertama. Sebab: muatan tulis terlalu
   besar untuk satu panggilan. **Penangkal: memadatkan muatan, bukan mengulang apa adanya.**

**DILARANG** mengutip "tidak ada kegagalan panggilan alat GitHub sepanjang sesi ini" dari
versi mana pun sesudah v20.
**DILARANG** membaca batas tulis aman 25-45 KB sebagai jaminan - kejadian 3 membuktikannya
bukan jaminan.

---

## 8. Nama workflow - 46, cacah tangan pada tip `9d30060e`

anatomi_tengah - bentangan_kohort - bentuk_semesta - bulan_absen - bulan_pertama -
bulan_settled - byte_semesta - **ci (1.923 B)** - diagnosa_kc14 - diagnosa_kc14b -
diagnosa_kc14c - diagnosa_kc15 - diagnosa_kc6 - funding_semesta - irisan_byte -
**karantina_semesta (2.107 B)** - kebangkitan - kehidupan - kehidupan_arsip (5.802 B) -
keterisian_lilin - kohort_ekor - lubang_awal - lubang_tebing - lubang_tengah -
**pecahan_serapan (7.715 B)** - penyebut_kc6 - penyebut_tahun - **peta_manifes (3.188 B)** -
probe_serapan - **pulihkan_rilis (5.556 B)** - rentang_kc6 - ringkas_semesta - sebab_bangkit -
selisih_lilin - semesta_kuota - semesta_silang - **serap_pilot (2.168 B)** - silang_funding -
silang_settled - sisa_defisit - survei_semesta - taksonomi_semesta - terhenti_semesta -
tersisip_semesta - uji_resample - ukur_baris.

Kini turunan **48** dengan `peta_funding.yml` dan `sumber_funding.yml`.
**DILARANG** mengutip 48 sebagai cacah tangan sah.

**`karantina_semesta.yml`** blob `de40fa4e68dc2e8dd76fd6700a4deed60f147cc2` -
**masih memakai `git add -f` gabungan yang cacat**. Satu-satunya pewaris cacat yang tersisa.

---

## 9. Cacah uji per berkas - `tests/` = 53, KEDALUWARSA, 18 nama diketahui

`test_irisan_byte.py` 68 - `test_bulan_pertama.py` 65 - `test_keterisian_lilin.py` 64 -
`test_bentangan_kohort.py` V2 63 - `test_lubang_tebing.py` 60 - `test_sebab_bangkit.py` 57 -
`test_byte_semesta.py` 56 - `test_lubang_awal.py` 48 - `test_tersisip_semesta.py` 47 -
`test_anatomi_tengah.py` 47 - `test_sisa_defisit.py` 44 - `test_selisih_lilin.py` 36 -
`test_terhenti.py` V4 33 - `test_bulan_absen.py` 32 - `test_karantina_semesta.py` 28 -
`test_silang_settled.py` 24 - `test_gerbang_1m.py` **16** - `test_ukur_baris.py` 3.

`test_lubang_tengah.py` 56 menurut R-228, **BELUM DIBACA**. Repo WARISAN `tests/` = 34.

Jumlah uji semesta **1377** = 1341 + 36. **DILARANG** menjumlahkan 1377 + 16.

**Tiga modul tanpa pasangan uji:** `peta_manifes.py` (utang verifikasi 51) -
`peta_funding.py` (52) - `sumber_funding.py` (53). Ketiganya **Lapis B**.

---

## 10. Ukuran berkas `reports/` - daftar utuh ber-`fields`

Delapan manifes pecahan: 2.530.465 - 2.587.577 - 2.446.093 - **2.257.314** - 2.615.515 -
2.865.596 - 2.780.523 - 2.450.719. Jumlah **20.533.802**.

Delapan `kehidupan_arsip_*`: 1.111.114 - 1.136.038 - 1.076.855 - 991.422 - 1.149.519 -
1.261.637 - 1.221.113 - 1.077.396. **DILARANG dibuka.**

Besar ke kecil (pilihan): `funding_semesta.json` **394.142** - `kehidupan.json` 280.587 -
`bulan_absen.json` 249.992 - `semesta_kuota.json` 200.533 - `silang_funding.json` **194.728** -
`rentang_kc6.json` 177.608 - `kohort_ekor.json` 112.687 - `semesta_rentang.json` **110.662** -
`lubang_tebing.json` 110.120 - `peta_manifes.json` 69.736 - `uji_resample.json` 51.921 -
`diagnosa_kc15.json` 42.916 - `lubang_awal.json` 42.449 - `diagnosa_kc6.json` 32.526 -
`anatomi_tengah.json` 32.028 - `penyebut_tahun.json` 30.385 - `bulan_settled.json` 29.820 -
`bentangan_kohort.json` 28.542 - `funding_semesta.log` 25.896 -
**`sumber_funding.json` 24.963** - `survei_semesta.json` 22.731 -
`diagnosa_kc14c.json` 21.104 - `tersisip_semesta.json` 19.330 -
**`semesta_bulan_1m.json` 18.884** - `kebangkitan.json` 17.644 -
`bulan_settled_ringkas.json` 14.413 - `bulan_absen_ringkas.json` 13.729 -
`terhenti_semesta.json` 11.697 - `sisa_defisit.json` 11.069 - `lubang_tengah.json` 11.014 -
`sebab_bangkit.json` 10.862 - **`hidup_tanpa_funding.json` 10.843** -
`ukur_baris.json` 9.748 - `karantina_semesta_ringkas.json` 9.662 -
`karantina_semesta.json` 9.609 - `karantina_semesta.log` 9.430 -
`silang_settled.json` 9.160 - `bulan_pertama.json` 8.888 - `peta_funding.json` 8.392 -
`semesta_silang.json` 7.936 - `probe_serapan.json` 7.586 - `manifes_pilot.json` 6.698 -
`selisih_lilin.json` 6.834 - `keterisian_lilin.json` 6.588 - `irisan_byte.json` 6.150 -
`byte_semesta.json` 6.136 - delapan `pulihkan_pecahan_*` 4.410 / 4.410 / 3.528 / 3.949 /
4.404 / 3.529 / 4.410 / 4.405 - `diagnosa_kc14.json` 4.358 - `peta_manifes.log` 3.029 -
`diagnosa_kc14b.json` 2.844 - `taksonomi_semesta.json` 1.777 - `ci_terakhir.txt` 1.621 -
`ringkas_semesta.json` 1.490 - `penyebut_kc6.json` 1.321 - `sumber_funding.log` 1.107 -
`bentuk_semesta.json` 1.064 - `peta_funding.log` 1.031 - `peta_funding_status.json` 216 -
`sumber_funding_status.json` 217 - `peta_manifes_status.json` 195 -
`ci_terakhir.json` **193**.

**Zona ambang alat baca:** **DILARANG** menginterpolasi pada 194.728 B sampai 2.257.314 B.
**DILARANG** menyatakan berkas di bawah 110.662 B pasti aman.

---

## 11. Blob laporan lama

`semesta_rentang.json` `8d5bd06c...` - `semesta_bulan_1m.json` `a1a6d3f0...` -
`silang_funding.json` `b61fe8b3...` - `lubang_tengah.json` `39cd1caa...` -
`hidup_tanpa_funding.json` `a7b20503...` - `taksonomi_semesta.json` `42d07af7...` -
`karantina_semesta.json` `678b665c1d32d6d5bbda0d9fd93445bcd64b2932` -
`lubang_awal.json` `3da15a11...` - `bulan_absen_ringkas.json` `e450d9f95e9bca0dc28a0e01c6aad6594c4fa3d6` -
`ci_terakhir.txt` `0f8626bc`.

**Blob manifes pecahan 0-7:** `5a118e57` - `89bb9ba1` - `c0be6ecf` - `f6329944` -
`13e4bf9f` - `c51e7e91` - `b73daf25` - `a6fa1673`.

**Blob modul serapan:** `pecahan.py` `f1b49f1b...` - `serap.py` `62d4c2c3...` -
`klines.py` `cc4d9287...` - `gerbang_1m.py` `c8cc54c8...` -
`karantina_semesta.py` `46e7c46be39545ed7a761838a6c95c3526ad25be` -
`bulan_absen.py` `10279d72...` - `lubang_awal.py` `8c36943d...` -
`tests/test_gerbang_1m.py` `a930af17...`.

---

## 12. Sidik kode resmi

| modul | sidik |
| --- | --- |
| **`sumber_funding`** | `ef5be4edd8b980efe461828137f0ff80161235134c53bc62f62bb0deab76af29` |
| **`peta_funding`** | `ed9c3c4e985dc4320011cb47cd0ae2cb68b0209505ac27559396748d3c7cbdfc` |
| `peta_manifes` | `1a5ef37dd6acbf5f298daa1fbdb3dcbe508cce5619daf2616f281a7ff3e64c22` |
| manifes (data) | `237ccf42...ba601` |
| `karantina_semesta` | `ad30150e...913e44c` |
| `silang_funding` V2 | `8a9b859c...3231b1` |
| `sidik_data_funding` | `2c9fbd1b...9608d24` |
| `sidik_kode_funding` | `d3854823...581513a` |
| `sidik_kode_laporan` | `24b6bb26...c8595` |
| `lubang_awal` | `156499ce...f2362` |
| `bulan_absen` | `0294eb3a...163088` |
| `lubang_tengah` V2 | `c9372bd7...b3f4e` |
| `sisa_defisit` | `6211624b...f044b0` |
| `keterisian` | `1cd98f4f...ca08bb` |
| `bulan_pertama` | `0d3530f6...a66562` |
| `irisan_byte` | `0e7103ef...3ea0c6` |
| `byte_semesta` | `e02aca2b...883c7` |
| `lubang_tebing` | `4a5c2e42...18bf3` |

---

## 13. Bahan yang hangus dan terlarang

- `karantina_semesta.py` dan `karantina_semesta.yml` - **TERLARANG sebagai bahan ramalan**
  (sudah dibaca sebelum praregistrasi R-321).
- `semesta_rentang.json` - **BAHAN TAK BERSAKSI** (ADR-A022). Dilarang dikutip tanpa
  menyebut status itu. 5% terakhir belum terbaca.
- Delapan `kehidupan_arsip_*.json` - **DILARANG dibuka**.
- `PROMPT_KELANJUTAN.md` - **bukan sumber**.
- `uji_r305`, `uji_r288`, `uji_r291` - **vonis alat BUKAN adjudikasi**.

---

## 14. Penomoran

EKOR berikutnya **v23**. Lihat `STATE.md` v64 bagian 15 untuk penomoran lengkap.
Papan skor **350 - SAH**. Aturan 38 berikutnya **ke-79**. Aturan 52 berikutnya **ke-68**.

- akhir EKOR v22 -
