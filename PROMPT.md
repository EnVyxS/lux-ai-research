# PROMPT v55 - serah terima LUX-AI

Operator: **Diva Juan Nur Taqarrub** (GitHub **EnVyxS**).
Repo tulis: **`EnVyxS/lux-ai-research`**, branch `main`. Tenggat riset: **2026-08-02**.
Bahasa kerja: **Indonesia**.

Ditulis 2026-07-31, pada giliran sesudah **EKOR v23** didorong dan dibaca ulang UTUH.
Menggantikan **PROMPT v54** (blob `e1aecf77fdf8edbbbb3240762fbf1624877107c0`, 30.816 B).

---

## 0. APA YANG BERUBAH DARI v54 - BACA SEBELUM APA PUN

v54 ditulis pada keadaan **STATE v50 / EKOR v10 / UKUR v10**, papan skor **310**, dan
tahap serapan masih terbuka. Seluruh bagian "posisi", "penomoran", "utang", dan "angka
semesta" di v54 kini **KEDALUWARSA**. v54 tetap sah di riwayat git sebagai jejak.

**Tiga hal yang wajib dibawa dari v54 dan masih berlaku penuh:**

1. **KC-50 - agregat semesta lewat jalan memutar.** **839.842.134 BUKAN jumlah lilin.**
   Ia total baris parquet rilis penuh. Jumlah lilin yang dihitung LANGSUNG dari baris
   adalah **839.325.999**. **Selisih 516.135** - kedua besaran itu **BUKAN besaran yang
   sama**. Hitung agregat lewat jalur LANGSUNG; bila dua angka seharusnya setara, **adu
   keduanya dan laporkan selisihnya, termasuk bila nol**. Cacat kelas ini tidak
   menghasilkan galat; ia menghasilkan **kesunyian**.
2. **Aturan 83** - hitung aritmetika implikasi SEBELUM mengunci pita ramalan.
3. **Aturan 84** - butir berklausa ATAU wajib melaporkan sumbangan BEBAS tiap klausa;
   bila tak bisa, klausa ATAU DILARANG dan butir dipecah.

**Yang baru sejak v54:** tahap serapan **TERTUTUP**; **aturan 94** dan penutupan paksa
tiga lapis (ADR-A024); **tiga belas butir ditutup paksa**; **Lapis A KOSONG dan dibayar
dengan pengukuran**; sumber label funding ditemukan; papan skor **350**.

---

## LANGKAH 0 - WAJIB SEBELUM PEKERJAAN APA PUN

Baca UTUH dan berurutan. Jangan mengerjakan apa pun sebelum ketujuhnya selesai.

1. `PROMPT.md` - berkas ini, **v55**.
2. `STATE.md` **v65** blob `308789664f67045bbfb03f8bf823ba252caa7323` (commit `c251d920`).
3. `STATE_LAMPIRAN_UKUR.md` **v23** blob `59326334bd0ca5f6395406e245658d53fb3f66bb`
   (commit `a88a4631`).
4. `STATE_LAMPIRAN_EKOR.md` **v23** blob `569c7c3afce3ea84319a7e49a792a95f151a6ae4`
   (commit `25970a88`, **28.033 B**) - **tidak lagi tertinggal**; ia merujuk STATE v65 dan
   UKUR v23, pencacahnya sampai aturan 38 ke-81.
5. `journal/2026-07-31-165.md` blob `31505537defcab310bfcc559e233843b66396b50`
   (LAPIS B + LAPIS C, tiga belas butir ditutup paksa).
6. `journal/2026-07-31-164.md` blob `cee2a53ecf37ef86a3972b6ee03009577bb6f345`
   (adjudikasi R-323, blokir 4 terpecahkan).
7. `decisions/ADR-A024.md` blob `cb5a07105b594278a73f486c8906ad873358b59e`
   (aturan 94, penutupan paksa tiga lapis, delapan keputusan).

Sesudah itu catat di jawaban pertama: papan skor, penomoran berikutnya, dan utang yang
masih hidup **beserta daftar matinya**.

---

## POSISI SAAT SERAH TERIMA

**Trio akar SERASI - tidak ada berkas trio yang tertinggal:**
STATE **v65** (`c251d920`) - UKUR **v23** (`a88a4631`) - EKOR **v23** (`25970a88`).

Tip `main` saat berkas ini disusun = **`fbdfa43eb519cd2393c41b196f46b9752b5806eb`**
(commit bot CI, laporan run 30628050382). Push berkas ini menambah commit, dan bot CI
menambah satu lagi - **selalu ukur tip yang sebenarnya, jangan mengasumsikan.**

Push `journal/**`, `decisions/**`, `hipotesis/**`, `reports/**` **tidak** menyalakan CI.
Push ke **akar repo** (`STATE.md`, `STATE_LAMPIRAN_*.md`, `PROMPT.md`) **menyalakan CI**.

Papan skor **350 - SAH**: TEPAT 240 - MELESET 68 - SEPARUH 22 -
**TIDAK TERADJUDIKASI 21** - MENUNGGU 1.
**Kenaikan TIDAK TERADJUDIKASI 16 -> 21 wajib disebut setiap kali papan skor dikutip.**

### Pencacah

aturan 38 berikutnya **ke-83** - aturan 52 berikutnya **ke-73**, yaitu pembacaan ulang
UTUH berkas ini pada giliran yang sama (batas rekam-diri; sesudahnya **ke-74**) -
berhenti eksplisit berikutnya **ke-70** - jurnal **166** - STATE **v66** - EKOR **v24** -
UKUR **v24** - PROMPT **v56** - ADR **A025** (dan **A003**) - KC **KC-60** -
aturan **95** - hipotesis **H-A024** - ramalan **R-324** - koreksi **22** -
**kesalahan dokumen 26** - **utang ukur 38** - utang verifikasi **54**.

### Deret aturan 38 - ke-42..ke-82 = **41 pembacaan berturut**

| ke- | blob | run | commit | waktu |
| --- | --- | --- | --- | --- |
| **82** | `1c696ea933a77569a0e896cc61769f36ae99e37d` | 30628050382 | `25970a88` (EKOR v23) | 11:44:11Z |
| 81 | `7d89e919...` | 30626985954 | `a88a4631` (UKUR v23) | 11:26:08Z |
| 80 | `8391c269...` | 30626827028 | `c251d920` (STATE v65) | 11:23:18Z |
| 79 | `b2a8a465...` | 30626303664 | `ae483de8` (UKUR v22) | 11:14:25Z |

Bacaan ke-82 sah karena **ketiga sisinya berganti** dari nilai basi yang diumumkan di
muka (run 30626985954 / commit `a88a4631` / blob `7d89e919...`). Cacah uji **1377**,
kode keluar 0.

**Nilai BASI yang wajib DITOLAK pada bacaan ke-83:** run **30628050382** - commit
`25970a88` - blob `1c696ea9...`. Bila ketiganya yang terbaca, laporan belum berganti dan
bacaan ke-83 **belum sah**.

Aturan 90: **empat belas pemakaian, DUA nyala.**
**DILARANG menjumlahkan aturan 90 dan 77** - alasannya berkorelasi.
**DILARANG** menyebut aturan 77 / 78 / 89 / 90 / 91 / 93 "teruji".

### Cacah tangan sah (aturan 66)

Pada tip `9d30060e`: `lux_ai/serapan/` **51** - `.github/workflows/` **46**.
Pada tip `470acfbb`: `journal/` **165** (penomoran 01..165 utuh tanpa lubang) -
`decisions/` **23** (A001..A024 tanpa A003) - akar **18 entri** = 12 berkas + 6 direktori.

TURUNAN **52 / 48 dilarang dikutip terukur**. **DILARANG** mengutip **44** sebagai cacah
tangan sah. `tests/` **53 tetap KEDALUWARSA**.
**DILARANG** membaca kesamaan angka akar 18 lama dan 18 baru sebagai konfirmasi - angka
sama lewat jalan berbeda bukan saksi.

---

## KEWAJIBAN TERBUKA - KERJAKAN BERURUTAN

1. **STATE v66 dan UKUR v24 - menyerap dua temuan baru.** EKOR v23 melahirkan
   **kesalahan dokumen 25** dan **utang ukur 37**; keduanya **belum masuk** STATE v65
   maupun UKUR v23. Sampai diserap, STATE dan UKUR **tertinggal satu langkah** dari EKOR -
   kebalikan dari keadaan sebelumnya. Katakan itu apa adanya.

2. **Utang ukur 37 - HIDUP, belum digolongkan lapisnya.** Lima blob ADR yang tercatat di
   EKOR v22 bagian 5 **tidak cocok** dengan blob terukur pada tip `470acfbb`:
   A009 `17a594b6` lawan `85796418` - A010 `c4bccf21` lawan `6de941f7` -
   A011 `645fd5df` lawan `312638e9` - A012 `f9f564d1` lawan `0c474067` -
   A013 `8ba4f989` lawan `3a7f8612`. Sembilan belas blob lain cocok persis.
   Dua kemungkinan yang sama-sama **belum diuji**: berkasnya pernah berubah, atau v22
   mencatat keliru sejak awal. **DILARANG menduga yang mana.** Bayar dengan
   `list_commits` berparameter `path` atas kelima berkas itu.
   **DILARANG** memakai jurnal 165 untuk menutupnya - ia lahir sesudah jurnal itu
   (aturan 94, larangan penyerta 4).

3. **ADR-A003 - DITAHAN, bukan ditunda karena konteks.** Isi keputusan yang seharusnya
   direkam A-003 **tidak ada dalam konteks mana pun**. Menulisnya berarti mengarang
   keputusan yang tak pernah diambil. **DILARANG mengarang isinya.** Butuh bahan dari
   operator atau penelusuran jurnal lama lebih dulu.

4. **Klasifikasi boleh dimulai.** Serapan tertutup; pembukuan yang tersisa tidak
   menghalanginya. Bila operator meminta maju, mulai dengan **praregistrasi R-324**
   (aturan 79 dan 89: ruang vonis **empat sisi**, di `journal/**`, sebelum bahan dibuka
   dan sebelum modul pengukurnya dibuat) - **bukan** dengan kode.

5. Bila konteks berat: **BERHENTI ke-70** dengan nomor dan alasan tertulis.

---

## CATATAN ATAS C-6 - PERSELISIHAN YANG SENGAJA TIDAK DIREDAM

Serah terima v54-ke-v55 menyatakan bahwa mendorong PROMPT v55 "melunasi C-6 dengan
pengukuran alih-alih membiarkannya mati". **Rumusan itu tidak dipakai di sini**, dan
sebabnya mengikat:

ADR-A024 keputusan 6 dan jurnal 165 larangan 1 melarang menulis utang yang ditutup paksa
sebagai **lunas, dibayar, atau selesai**, dan melarang **mengurangkannya dari cacah
utang**. Daftar mati **tidak pernah menyusut**.

Yang terukur, dan hanya ini:

> **PROMPT v55 kini ADA** di `main` dan terbaca ulang utuh. **C-6 tetap tercatat
> DITUTUP PAKSA** di daftar mati. Perbuatan mendorong v55 **tidak menghidupkan kembali
> C-6**, **tidak** mengurangi cacah tiga belas butir, dan **tidak** boleh dikutip sebagai
> pelunasan.

Bila operator menghendaki C-6 benar-benar dinyatakan lunas, itu menuntut **ADR baru yang
mengubah keputusan 6 ADR-A024**, bukan sekadar sebuah push. **Jangan memutuskannya
sendiri.**

---

## ANGKA TERUKUR SAH - SELALU DENGAN STATUS UTANGNYA

Penyebut **19.586** = 18.999 + 587 = 18.054+33+559+842+96+2 - rilis penuh **19.598** =
19.586 + 12 karantina - simbol manifes **787** = 769 + 18 - simbol `semesta_bulan_1m`
**937** (selisih **150 TIDAK TERJELASKAN**, B-5) - HIDUP 18.087 - MATI 1.401 - SEPI 98 -
kelas positif **33** (BNX 7 - ICP 13 - JUP 1 - QTUM 1 - TLM 11) - `terhenti` **587** pada
**27** simbol - `berheader` 17.646 = 17.257 + 389 - baris rilis penuh **839.842.134** =
24.801.034 + 815.041.100 - baris parquet lolos 839.325.999 - karantina 516.135 -
byte parquet 32.706.262.375 - jumlah uji **1377** = 1341 + 36.

Tabel silang (`reports/silang_funding.json`, `.ringkasan.tabel_silang`):
HIDUP 18.054 / 33 - MATI 559 / 842 - SEPI 96 / 2.
Kelas positif = `.baris_hidup_tanpa_funding`. Pendamaian bebas: `.baris_mati` = 1.401.

**Aturan pemakaian (aturan 94 / ADR-A024 keputusan 5):**
*Tidak ada angka boleh dikutip di tahap mana pun tanpa status utangnya.*

---

## ENAM SYARAT MENYEBERANG KE KLASIFIKASI - WAJIB IKUT SETIAP KUTIPAN

1. **Ketakseimbangan kelas 33 : 19.553.** DILARANG melaporkan akurasi tanpa ini.
2. Tabel silang **belum diuji ketepatannya** terhadap kenyataan funding.
3. **Dua penyebut simbol** hidup berdampingan: 787 dan 937 (B-5).
4. Delapan belas simbol tak berpola adalah **simbol sah**, bukan anomali (KOREKSI 20).
5. **Ketiga modul penemu tak berpasangan uji** (B-2 `peta_manifes.py`,
   B-3 `peta_funding.py`, B-4 `sumber_funding.py`).
6. **Gerbang penyaring penyebut punya ENAM klausa dengan dasar keputusan LIMA** (B-1).

---

## UTANG

**LAPIS A: KOSONG.** Blokir 4, utang ukur 32, utang ukur 35, utang verifikasi 50 -
semuanya **dibayar dengan pengukuran**, nol ditutup paksa.
**DILARANG** membaca kekosongan ini sebagai bukti tidak ada utang.

**DITUTUP PAKSA: tiga belas butir** (STATE v65 bagian 6; label penuh di jurnal 165).
LAPIS B: B-1 gerbang enam lawan lima - B-2 `peta_manifes.py` tanpa uji dan terbukti
pernah cacat - B-3 `peta_funding.py` tanpa uji - B-4 `sumber_funding.py` tanpa uji -
B-5 dua penyebut simbol - B-6 `pulihkan.py` tak pernah dibaca.
LAPIS C: C-1 sampai C-7.

Penutupan paksa **BUKAN pelunasan**. DILARANG menulisnya lunas - DILARANG
mengurangkannya dari cacah utang - DILARANG mengutip angka yang bergantung padanya
tanpa menyebut labelnya - DILARANG memakai jurnal 165 untuk menutup utang yang lahir
sesudahnya tanpa penggolongan lapis tersendiri - DILARANG menutup paksa utang Lapis A
dengan alasan tenggat, biaya, atau permintaan operator - DILARANG menggolongkan utang
ke Lapis C karena mahal.

**Utang ukur HIDUP:** 6 - 7 - 17 - 21 - 22 - 26 - 27 - 30 - **37 (baru, belum berlapis)**.
**Utang verifikasi HIDUP:** 24 - 45 - 46 - 49.

**DILARANG** membaca pendeknya daftar utang hidup sebagai kematangan bila daftar matinya
tidak ikut disebut pada napas yang sama.

**Poros riset HIDUP:** rentetan awal BNXUSDT - dua pola bulan absen - TLMUSDT 2023-03
(95,2%) - tebing 2025-07 (39 simbol) - penulis `semesta_rentang.json` - sebab kelipatan
hari penuh BNXUSDT - selisih 937 lawan 787 - sisa **712.925** lilin (**DILARANG jadi
penyebut**, KC-50) - selisih **516.135**.

---

## ALAT

GitHub lewat MCP `mcpServer_github`. Bentuk WAJIB - `owner`/`repo` **hanya** di dalam
`toolArguments`, tidak pernah di tingkat atas `args`:

```
connections.mcpServer_github.runTool({
  toolName: "...",
  toolArguments: { owner: "EnVyxS", repo: "lux-ai-research", ... }
})
```

- `get_file_contents`: `{owner, repo, path, ref?, sha?, fields?}` - `sha` = commit SHA;
  **`fields` HARUS LARIK**, hanya untuk direktori. Akhiran `/` atau nama direktori
  melisting isinya.
- `push_files`: `{owner, repo, branch, files:[{path,content}], message}` -
  **satu berkas per push**.
- `list_commits` dan `search_commits` bekerja. **`search_code` selalu 0 hasil.**
- **Tidak ada alat GitHub Actions.** Status run hanya lewat `reports/*_status.json` dan
  `reports/ci_terakhir.json` (**193 B**, hanya menyimpan run TERAKHIR).
- Batas tulis "aman" +-25-45 KB **BUKAN JAMINAN** - muatan besar pernah memicu
  `JSON parse error` pada posisi 27317. Penangkalnya **memadatkan muatan**, bukan
  mengulang apa adanya. EKOR v23 berhasil pada **28.033 B** sekali jalan; **itu satu
  kejadian, bukan jaminan.**
- Tulisan ke GitHub **tidak** memakai `editDescriptionVariableName` maupun
  `<edit_reference>` - itu hanya untuk halaman Notion.
- Sandbox tanpa jaringan. Pengukuran hanya berjalan lewat GitHub Actions.

---

## DISIPLIN MENGIKAT

Aturan **21 - 29 - 38 - 52 - 55 - 57 - 66 - 79 - 80 - 83 - 84 - 85 - 86 - 87 - 89 - 90 -
93 - 94** dan KC-49. Aturan resmi **1-81, 83-94**.

- **Satu berkas per push.**
- **Setiap berkas yang didorong wajib dibaca ulang UTUH pada giliran yang sama**
  (aturan 52), dan blobnya dicatat. Tidak boleh dilewati dengan alasan apa pun.
- **Batas rekam-diri.** Sebuah berkas tidak dapat merekam pembacaan ulang atas dirinya
  sendiri. Penangkalnya: **namai nomornya di muka** di dalam berkas itu. Kelalaian
  melakukan ini melahirkan kesalahan dokumen 24.
- **Ramalan diregistrasi sebelum bahan dibuka**; adjudikasi pada **giliran berbeda**;
  ruang vonis wajib **empat sisi** (aturan 89).
- **Periksa ukuran berkas dari daftar direktori sebelum membukanya** (aturan 93).
- **Umumkan nilai BASI di muka** sebelum menunggu CI, lalu tolak bila ketiga sisinya
  tidak berganti.
- **Jangan mengarang SHA. Jangan mengarang angka. Ukur, jangan menduga.**
- Kalau konteks berat, **berhenti dan katakan berhenti** - sebutkan nomor berhenti dan
  alasannya.

---

## LARANGAN YANG PALING MUDAH DILANGGAR

DILARANG mengutip `jangkauan_maksimum_funding` atau butir 3 R-323 sebagai bukti apa pun
(KOREKSI 21) - DILARANG memakai manifes sebagai sumber label funding (`funding_ada`
adalah medan mati, `{"null": 19598}`) - DILARANG menyimpulkan data funding tidak ada -
DILARANG menyatakan tabel silang **benar** (hanya "lengkap dan konsisten dengan dirinya
sendiri") - DILARANG menghitung `silang_funding.json` dan `hidup_tanpa_funding.json`
sebagai dua saksi bebas - DILARANG mengutip kardinalitas 77/99/2.411/2.408/176/81
sebagai angka semesta (KOREKSI 19) - DILARANG mengutip **44** sebagai cacah tangan sah -
DILARANG menjumlahkan **1377 + 16** - DILARANG memakai **712.925** sebagai penyebut
(KC-50) - DILARANG mempertukarkan **787** dan **937** - DILARANG menyamakan **587**
dengan 1.401 atau dengan 33 - DILARANG menyamakan "nol menang" dengan "nol diuji" -
DILARANG menulis rekor aturan 79 sembilan atau menghidupkannya kembali - DILARANG
mengklaim CI EKOR v22 (`c282a438`) pernah diperiksa (tertimpa) - DILARANG menjumlahkan
aturan 90 dan 77 - DILARANG menyebut jenis instrumen karantina maupun jenis instrumen
bagi ke-150 nama selisih 937 lawan 787 - DILARANG membuka
`reports/kehidupan_arsip_*.json` - DILARANG mengutip UKUR **v22 bagian 9 dan 10**
(TERGANTI oleh v23) - DILARANG membaca pendeknya daftar utang hidup sebagai kematangan
bila daftar matinya tidak ikut disebut - DILARANG menuliskan "27 simbol berhenti
diperdagangkan di bursa" sebagai terukur - DILARANG memperlakukan
`PROMPT_KELANJUTAN.md` sebagai sumber.

---

## NADA KERJA

Ukur, jangan mengarang. Bila angka belum diukur, katakan belum diukur. Bedakan **TERUKUR**
dari **TURUNAN**, dan bedakan pula **MELIHAT** dari **MENGUKUR**. Bila dua angka yang kamu
kira sama ternyata berbeda, **angka itu temuannya**, bukan gangguannya - 516.135 lebih
berharga daripada kemenangan R-310 itu sendiri, dan kelima blob ADR yang tak cocok lebih
berharga daripada registri yang rapi. Bila ramalan meleset, tulis MELESET dan cari
sebabnya. Bila ramalan menang, cari bagian mana dari kemenangan itu yang sebenarnya
kosong. Kemenangan yang tidak mengajarkan apa pun wajib dinyatakan lemah walau menang;
kemenangan tipis ke tepi pita wajib disebut tipis. Bila temuan melawan tafsir yang kamu
sukai, tulis temuan itu **lebih keras**, bukan lebih pelan. Bila permintaan operator
bertabrakan dengan aturan yang mengikat, **katakan tabrakannya** dan jangan meredamnya
diam-diam. Bila dokumen sendiri bertentangan dengan berkas sumber, **berkas sumber
menang** dan dokumen dikoreksi pada giliran itu juga. Tutup setiap giliran dengan jurnal,
dan tinggalkan PROMPT + STATE yang bisa dipakai orang lain tanpa bertanya apa pun.

- akhir PROMPT v55 -
