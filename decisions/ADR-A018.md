# ADR-A018 — Bias taksiran pemusatan, dan apa yang boleh dibaca dari R-311

**Tanggal:** 30 Juli 2026 · **Status:** DITERIMA · **Menggantikan:** tidak ada ·
**Mengoreksi:** ADR-A016 keputusan 4 (sebagian), STATE v51 bagian aturan 38 (sebagian).

**Dasar berkas, seluruhnya dibaca UTUH sebelum ADR ini ditulis:**
`journal/2026-07-30-135.md` (`626293c1`), `STATE.md` v51 (`412a5b2d`),
`STATE_LAMPIRAN_EKOR.md` v11 (`3d72a9e7`), `STATE_LAMPIRAN_UKUR.md` v10
(`162c1305`), `decisions/ADR-A017.md` (`1be570f2`),
`reports/sisa_defisit_ringkas.json` (`91a05c05`),
`reports/sisa_defisit_status.json` (`1c9c2c5f`),
`reports/ci_terakhir.json` (`bce1177e`).

Berkas ini berada di `decisions/**` yang masuk `paths-ignore` `ci.yml`, jadi
push-nya TIDAK menyalakan CI dan cacah uji tetap **1341** tanpa pengukuran baru.
Itu dinyatakan supaya tidak ada yang mengira angka 1341 di bawah diukur ulang di
sini.

---

## Konteks

R-311 menguji sisa **712.925** lilin yang ditinggalkan R-310: berapa banyak baris
bukan-pertama bukan-MATI yang berdefisit, dan seberapa terpusat kekosongan itu.
Hasilnya **SEPARUH**: butir 1 kalah telak (**114** lawan pita **200 .. 12.000**),
butir 2 menang menempel tepi atas (**0,4087** lawan pita **0,02 .. 0,45**).

Kekalahan butir 1 adalah kekalahan **ketiga berturut ke arah yang sama**, dan
arahnya tidak pernah berbalik. Itulah pokok ADR ini. Yang diputuskan di sini
bukan "ramalannya meleset", melainkan **cacat sistematis dalam cara pita
disusun**.

---

## Keputusan

### 1. KC-51 DIRESMIKAN — bias taksiran pemusatan

**Rumusan resmi, satu-satunya yang boleh dikutip:**

> Ketika sebuah besaran belum pernah diukur sebarannya, taksiran yang saya buat
> secara sistematis mengandaikan besaran itu **lebih menyebar** daripada
> kenyataannya. Akibatnya tepi pita di sisi "terpusat" diletakkan terlalu jauh
> dari lantai aritmetis, dan pita kalah ke sisi itu.

**Tiga bukti berturut, tanpa satu pun pembalikan arah:**

| ramalan | besaran | taksiran / pita | terukur | arah |
|---|---|---|---|---|
| R-308 butir 2 | cacah MATI ber-byte kecil | 10 .. 300 | **2** | lebih terpusat |
| R-310 butir 2 | bagian defisit bukan-pertama | taksir 0,073 (pita 0,02..0,25) | **0,0445** | lebih terpusat |
| R-311 butir 1 | cacah baris berdefisit | taksir 3.000 (pita 200..12.000) | **114** | lebih terpusat |
| R-311 butir 2 | pemusatan sepuluh teratas | taksir 0,15 (pita 0,02..0,45) | **0,4087** | lebih terpusat |

R-311 butir 1 meleset **26,3 kali** dari taksiran titik dan **1,75 kali** di bawah
tepi bawah. R-311 butir 2 meleset **+172%** dari taksiran titik — dan perhatikan
bahwa **kedua butir meleset ke arah yang sama secara fisik** (kekosongan lebih
terpusat), meskipun satu kalah dan satu menang. Itu justru memperkuat KC-51:
satu-satunya alasan butir 2 menang adalah pitanya kebetulan cukup lebar.

**Yang DILARANG oleh KC-51:** menyebut kemenangan butir 2 sebagai bukti
kalibrasi membaik. Dua ramalan berturut yang menang **menempel tepi berlawanan**
(R-310 menempel tepi BAWAH pada kedua butir, R-311 menempel tepi ATAS dengan
sisa 0,0413) adalah gejala pita yang disusun tanpa gambaran sebaran, bukan
gejala pita yang dirancang baik.

### 2. ATURAN 85 DIRUMUSKAN dan BERLAKU

**Bunyi resmi aturan 85:**

> Untuk tiap butir berisiko yang membatasi sebuah **cacah** atau **bagian**, dan
> yang sebarannya belum pernah diukur, aritmetika implikasi aturan 83 wajib
> dilanjutkan satu langkah: sesudah lantai dan langit-langit aritmetis dihitung,
> **tepi pita di sisi "terpusat" diletakkan pada lantai itu atau paling banyak
> satu orde besaran di atasnya**, dan alasan penempatannya ditulis sebagai
> kalimat tersendiri di praregistrasi. Kelipatan intuitif seperti 100, 200, atau
> 1.000 di atas lantai DILARANG dipakai tanpa alasan tertulis.

**Mengapa aturan 83 saja tidak cukup, dinyatakan telanjang:** aturan 83 **ditaati
penuh** di R-311. Lantai aritmetis **16** memang dihitung sendiri di jurnal 134,
dan rentang implikasinya (16 .. 18.790) memang benar. Tepi bawah tetap
diletakkan di **200** — dua belas setengah kali lantai — tanpa satu kalimat pun
yang membenarkannya. Aturan 83 menuntut aritmetikanya dihitung; ia tidak pernah
menuntut hasilnya **dipakai**. Aturan 85 menutup lubang itu.

Aturan 85 berlaku mulai **R-312**. Ia TIDAK berlaku surut, dan R-311 TIDAK
diadjudikasi ulang (aturan 29).

### 3. Rumusan resmi temuan R-311

Yang boleh dikutip sebagai terukur, tidak lebih:

> Dari **17.398** baris simbol-bulan yang bukan bulan pertama simbolnya dan bukan
> berstatus MATI, hanya **114** (**0,66%**) yang jumlah lilinnya kurang dari lilin
> penuh bulannya. Keseratus empat belas baris itu menanggung **712.925** lilin
> yang hilang, rata-rata **6.254** lilin per baris. **Sepuluh baris teratas
> menanggung 291.379 lilin, yaitu 0,4087 — dua per lima dari seluruhnya.**
> Baris terbesar adalah **TLMUSDT 2023-03**, berstatus HIDUP, dengan **2.130 dari
> 44.640** lilin, yakni **95,2% kosong**.

**Larangan yang menyertainya:**

- **Penutupan 712.925 DILARANG disebut pengukuran bebas.** `defisit_calon` =
  712.925 dan `selisih_sisa` = 0 **terpaksa** muncul dari 808.162 − 95.237 begitu
  seluruh 1.401 baris MATI ternyata bukan bulan pertama. Itu tautologi (KC-50,
  KC-37).
- **Kenyataan bahwa 114 baris seluruhnya HIDUP (111) atau SEPI (3) dan nol MATI
  DILARANG disebut temuan.** Itu dipaksa oleh definisi penyebut kerja.
- **Tidak satu kalimat pun boleh menyimpulkan apa pun tentang harga.** Keempat
  belas medan `medan_baris_terlihat` tidak memuat harga (ADR-A017 keputusan 2
  tetap berlaku penuh).

### 4. Aturan 81 diperiksa untuk R-311 dan TIDAK terpicu

Sepuluh baris berdefisit teratas tersebar di **tujuh bulan berbeda**; kelompok
terbesar dalam satu bulan hanya **dua** baris. Berbeda dari R-310, yang tujuh
dari sembilan barisnya berhimpit di `2024-05` dalam jendela sembilan lilin
(KC-47). Karena itu **114 boleh diperlakukan sebagai cacah baris**, bukan sebagai
satu peristiwa yang menyamar.

### 5. H-A021 didaftarkan sebagai DIUSULKAN, dan sebabnya DILARANG

> **H-A021:** kekosongan **ANCUSDT `2022-05`** (defisit **26.959**) dan
> **LUNAUSDT `2022-05`** (defisit **26.950**) adalah **satu peristiwa yang sama**,
> bukan dua pengamatan bebas.

Dasarnya hanya selisih **sembilan lilin** antara dua defisit di bulan yang sama.
Itu **kebetulan angka**, bukan bukti. Sampai diuji lewat lubang tengah,
**setiap kalimat sebab untuk gugus `2022-05` DILARANG**, termasuk yang paling
menggoda. Bila H-A021 kelak diterima, cacah pengamatan bebas dalam sepuluh baris
teratas turun dari 10 menjadi 9, dan `bagian_teratas` **tidak** berubah karena ia
dihitung atas lilin, bukan atas baris.

### 6. ADR-A016 keputusan 4 DIKOREKSI sebagian

A016 mencatat **TLMUSDT 2023-03** sebagai satu-satunya baris yang melawan H-A019,
dengan sifat yang belum diketahui. Kini sifatnya terukur: ia bukan bulan tepi dan
bukan bulan pertama, melainkan **bulan HIDUP yang 95,2% kosong**.

Akibatnya: tafsir "byte parquet kecil = bulan sebagian di tepi rentang"
**MELEMAH** — ada jalan ketiga, yaitu bulan penuh kalender yang datanya memang
nyaris tidak ada. **Tafsir penggantinya TIDAK ditegakkan** karena sebabnya belum
diukur. H-A019 tetap DITERIMA TERBATAS sebagaimana A016 keputusan 1; yang dicabut
hanyalah anggapan bahwa perlawanan TLMUSDT 2023-03 tak terjelaskan.

ADR-A015 keputusan 5 (**besar berkas bukan detektor status ke arah mana pun**)
**TIDAK dibalik** oleh R-311.

### 7. Koreksi atas STATE v51 diresmikan

STATE v51 menulis bahwa ramalan "CI tetap" pada push dokumen **tidak pernah
terukur**. Itu terbantah oleh pembacaan langsung: run **30545364506** atas commit
**`8c30de51`** (push STATE v51) menghasilkan **1341**, kode **0**,
`1341 tests collected in 0.45s`, blob **`bce1177e`**.

Rumusan yang benar dan mengikat: ramalan semacam itu **terukur bila laporannya
dibaca sebelum run berikutnya menimpanya**, dan tetap berlabel **MUDAH**, tetap
**tidak diskor**, tetap **tidak menambah beruntun aturan 57**, karena tidak
menyentuh `tests/**`. Yang terukur mengalahkan yang disimpulkan (KC-41).

### 8. Rekonsiliasi ordinal aturan 38 DITERIMA, dengan cacatnya

Definisi yang berlaku: **pemakaian aturan 38 dihitung hanya untuk pembacaan
`reports/ci_terakhir.json` yang meninggalkan jejak tertulis** berupa nomor run,
commit, dan blob di STATE, lampiran, atau jurnal. Dengan definisi itu, pemakaian
berjalan adalah **ke-40** (run `30545364506`).

**Cacatnya disebut, bukan disembunyikan:** baris ke-38 (run `30541051907`) tidak
memuat blob, diwarisi dari jurnal 135, dan blob itu sudah tertimpa sehingga tidak
dapat dipulihkan. Ordinal 40 karena itu sah **relatif terhadap definisi di atas**,
bukan sebagai pencacahan mutlak. Bila jejak pembacaan lain ditemukan di jurnal
133–134, nomor ini WAJIB dikoreksi.

### 9. `PROMPT_KELANJUTAN.md` DINYATAKAN ARSIP — BUKAN SUMBER

Berkas `PROMPT_KELANJUTAN.md` (blob `35beed44`, 10.777 B) dibaca utuh untuk
pertama kalinya hari ini. Isinya adalah **PROMPT v48**, tertinggal enam versi dari
`PROMPT.md` v54, dan **setiap angka posisinya salah**: ia menyuruh membaca STATE
v44 / EKOR v4 / UKUR v4, menyebut papan skor **305**, aturan sampai **79**, KC
sampai **KC-44**, CI **984**, cacah direktori 42/37, dan mempraregistrasi
**R-306** yang sudah lama diadjudikasi TEPAT.

**Keputusan:** berkas itu **DILARANG dipakai sebagai sumber posisi, aturan, atau
praregistrasi oleh siapa pun**, termasuk penerus giliran. Ia berstatus arsip
setara `STATE_LAMPIRAN_ADR.md`. Pekerjaan tersisa: memberinya kepala
"ARSIP — BUKAN SUMBER" atau menghapusnya.

**Sebab keputusan ini keras:** namanya justru yang paling mengundang dibaca lebih
dulu oleh penerus, dan satu di antara perintahnya bertabrakan langsung dengan
perintah operator yang berlaku sekarang. Perintah operator v54 menang; berkas
usang tidak boleh mengalahkan perintah yang berlaku.

### 10. Dua cacah `tests/` DILARANG dicampur

`PETA_MODUL_BERKAS.md` mencatat **34** berkas uji milik repo WARISAN `bot_v8`.
Repo riset ini punya **53** berkas uji (cacah tangan ref `3196fd98`). Keduanya
benar untuk repo masing-masing. **Menyebut "cacah uji" tanpa menyebut repo-nya
DILARANG**, karena selisih 34 lawan 53 akan tampak seperti pelanggaran aturan 66
padahal bukan.

Selain itu, tiga butir `PETA_MODUL.md` yang bertanda "memerlukan verifikasi"
didaftarkan sebagai utang terbuka, bukan sebagai fakta: atribut `enable_hs` yang
tidak ditemukan di `config.py`; klaim "30 pair dipilih alfabetis" yang tak ada
buktinya; klaim "kendala mengikat = kapasitas margin" yang belum diuji angkanya.

### 11. Cacah tangan direktori dicatat resmi

Pada ref **`3196fd9809f23917ba819b4339cdfdd57bb808d1`**, dicacah satu per satu
bernomor (aturan 66): `lux_ai/serapan/` **49** berkas `.py` · `tests/` **53** ·
`.github/workflows/` **44** · akar repo **18** entri (6 direktori + 12 berkas).
Angka 48/52/43 pada ref `5d7d8b96` (A017 keputusan 11) tetap sah untuk ref itu.

Begitu trio ukur berikutnya didorong, angka 50/54/45 menjadi **turunan** dan
DILARANG dikutip sebagai terukur sampai dicacah ulang dengan tangan.

### 12. Poros R-312 ditetapkan; praregistrasinya BUKAN di sini

Dua poros yang boleh dipakai, urut prioritas:

- **(a) Lubang tengah gugus `2022-05` dan `2024-05`.** Menguji **H-A021 dan
  H-A020 sekaligus**: apakah baris-baris berdefisit yang berhimpit bulan itu
  berbagi satu jendela lilin yang sama, sebagaimana tujuh baris `2024-05` di
  R-310.
- **(b) Selisih 516.135** antara 839.842.134 dan jumlah lilin langsung
  839.325.999, dihadapkan pada dugaan 12 simbol-bulan karantina
  (516.135 / 12 = 43.011 — **DUGAAN, belum diuji**). Porosnya wajib berupa
  **bentuk sebaran**, bukan rata-rata, sebab rata-rata 43.011 akan selalu benar
  secara aritmetis dan karena itu tidak berisiko.

**Praregistrasi R-312 DILARANG ditulis di ADR ini.** Ia wajib ditulis di jurnal
lebih dulu (aturan 79), pada giliran yang berbeda dari adjudikasi (ADR-A016), dan
wajib melewati aturan 83 **dan aturan 85 yang baru berlaku di atas**, serta
aturan 84 (satu klausa per butir).

---

## Akibat langsung

- **KC-51 RESMI.** KC berikutnya yang bebas: **KC-52**.
- **Aturan 85 RESMI dan berlaku mulai R-312.** Aturan berikutnya yang bebas: **86**.
  Usulan **77**, **78**, dan **82** tetap belum resmi.
- **H-A021 DIUSULKAN**, belum diuji. Hipotesis berikutnya: **H-A022**.
- **STATE v52 wajib menyerap ADR ini**: KC-51 dari DIUSULKAN menjadi RESMI, aturan
  85 masuk daftar aturan, koreksi aturan 38, status arsip `PROMPT_KELANJUTAN.md`.
- **UKUR v11 masih UTANG** dan belum memuat API `sisa_defisit` V1, 114 baris
  berdefisit, H-A021, maupun cacah 49/53/44.
- Papan skor tidak berubah: **311**. CI tidak berubah dan tidak diukur ulang di
  sini: **1341**.

## Yang TIDAK diputuskan

- Sebab kekosongan **TLMUSDT 2023-03** — belum diukur, dan tidak ada tafsir yang
  ditegakkan menggantikan yang melemah.
- Apakah gugus `2022-05` satu peristiwa — itu isi R-312 poros (a).
- Apakah 516.135 berasal dari karantina — itu isi R-312 poros (b).
- Apakah "bulan pertama di penyebut" sama dengan "bulan pertama di bursa".
- Nasib akhir `PROMPT_KELANJUTAN.md` (diberi kepala arsip atau dihapus).
