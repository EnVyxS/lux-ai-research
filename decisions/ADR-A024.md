# ADR-A024 — Penutupan paksa utang: tiga lapis

- **Tanggal:** 2026-07-31
- **Keadaan:** DITERIMA
- **Tip `main` saat ditulis:** `5d0a34382be039f00eba7fe0dd3bde71965809f9`
- **Pemicu:** tenggat riset 2026-08-02. Operator meminta penutupan tahap serapan
  meskipun sebagian utang tidak akan pernah dibayar.

## Konteks

Tahap serapan tidak menuntut **nol utang** untuk ditutup. Yang dituntutnya adalah utang
yang **tercatat, terhitung, dan tidak menyusup ke tahap berikutnya**. Tanpa aturan yang
mengikat, penutupan paksa di bawah tekanan tenggat akan mengambil bentuk terburuk yang
mungkin: utang yang tidak dibayar **dan** tidak tercatat, lalu muncul kembali di tahap
backtest sebagai angka tak bertuan.

Risiko yang mendasari seluruh keputusan di bawah ini **tidak simetris**:

- Kekeliruan pada **pembukuan** berhenti di pembukuan.
- Kekeliruan pada **penyebut** atau **label** merambat ke **setiap** hasil backtest, dan
  **tidak akan tampak keliru** — ia akan tampak seperti hasil.

Seluruh pemilahan di bawah ini adalah penerapan ketaksimetrisan itu, bukan penilaian
tentang seberapa penting suatu utang terasa.

## Keputusan

### (1) Aturan 94 RESMI — penutupan paksa tiga lapis

Suatu utang hanya boleh dinyatakan **DITUTUP PAKSA** setelah digolongkan ke salah satu
dari tiga lapis, dan penggolongannya ditulis bersama alasannya. Menyatakan sebuah utang
mati tanpa lapis adalah **pelanggaran aturan 94**.

### (2) LAPIS A — DILARANG ditutup paksa

Utang yang menyentuh **label** atau **keanggotaan penyebut** yang akan dikonsumsi
klasifikasi. Tenggat **BUKAN** alasan sah untuk menembus lapis ini.

| utang | mengapa Lapis A |
| --- | --- |
| **blokir 4 — `funding_ada`** | kelas positif **33** adalah **label** klasifikasi. Menutupnya paksa berarti melatih di atas label yang asal-usulnya tak diketahui. |
| **utang verifikasi 50** | apakah tiga simbol non-Latin ikut dalam **787**; menyentuh keanggotaan penyebut. |
| **utang ukur 32** | arti `terhenti` = **587**. Bila ia menandai serapan terpotong, maka 587 simbol-bulan di dalam **19.586** cacat, dan backtest rusak tanpa satu pun tanda. |

### (3) LAPIS B — boleh ditutup paksa, WAJIB berlabel mengikat

Menyentuh **definisi**, bukan angka. Label wajib ikut ke setiap tahap berikutnya.

- **Utang ukur 31** dan **utang verifikasi 48** — lima lawan enam klausa gerbang 1m. Kode
  sudah terukur **enam** (`assert len(g.KLAUSA) == 6`); yang belum lunas adalah
  `ADR-A004.md` §2.2 yang mencacah **lima**.
- **Utang verifikasi 51** — `tests/test_peta_manifes.py` tidak ada, padahal modulnya
  menghasilkan angka yang dipakai R-321 dan sudah terbukti mengandung **KOREKSI 19**.
- **Utang bacaan `pulihkan.py`** (14.839 B) — `peta_manifes.py` **meminjam**
  `nama_manifes()` dan `TOTAL_PECAHAN` darinya. Berkas ini berada di dalam rantai
  penghasil angka R-321 tanpa pernah dibaca utuh.

### (4) LAPIS C — boleh ditutup paksa dengan catatan ringkas

Tidak menyentuh satu pun angka yang dikonsumsi tahap berikutnya.

- Utang ukur **33** (ketidakseragaman kunci `dikemas_karantina`) dan **34** (44 lawan 46
  workflow).
- Utang verifikasi **47** (UKUR v19 terdorong terpotong).
- Cacah tangan `tests/` dan akar.
- Adjudikasi tangan **R-305, R-288, R-290, R-228, R-291**.
- Sisa utang bacaan selain `pulihkan.py`.
- **PROMPT v55** dan kepala "ARSIP — BUKAN SUMBER" pada `PROMPT_KELANJUTAN.md`.

### (5) DAFTAR UTANG DITUTUP PAKSA — wajib dan terbawa

STATE v64 wajib memuat bagian **DAFTAR UTANG DITUTUP PAKSA** berisi setiap utang mati,
lapisnya, dan alasannya. Bagian ini **wajib terbawa utuh** ke tahap klasifikasi dan
backtest. Aturannya satu kalimat:

> Tidak ada angka boleh dikutip di tahap mana pun tanpa status utangnya.

### (6) Penutupan paksa BUKAN pelunasan

**DILARANG** menulis utang yang ditutup paksa sebagai lunas, dibayar, atau selesai.
**DILARANG** mengurangkannya dari cacah utang seolah ia terbayar. Ia berpindah dari
daftar hidup ke daftar mati, dan daftar mati tidak pernah menyusut.

### (7) Larangan baru yang menyertai

- **DILARANG** menutup paksa utang Lapis A dengan alasan tenggat, biaya, atau permintaan
  operator.
- **DILARANG** menggolongkan utang ke Lapis C karena ia mahal; lapis ditentukan oleh apa
  yang disentuhnya, bukan oleh ongkosnya.
- **DILARANG** membaca pendeknya daftar utang hidup sebagai kematangan bila daftar matinya
  tidak disebut pada napas yang sama.
- **DILARANG** memakai ADR ini untuk menutup paksa utang yang **lahir sesudahnya** tanpa
  penggolongan lapis tersendiri.

### (8) Catatan atas asumsi operator — "funding sudah sangat matang"

Operator menyatakan sendiri bahwa ini **asumsi, bukan data**, dan meminta diperiksa.
Diperiksa terhadap ukuran yang ada: **asumsi itu belum didukung.**

Blokir 2, 3, dan 5 memang **LUNAS**, dan itu kemajuan besar. Tetapi **blokir 4 baru lunas
sebagian**: `funding_ada` **tidak muncul** pada lajur boolean maupun teks di
`reports/peta_manifes.json`, sehingga kelas positif **33** masih belum lepas dari lima
simbol (BNX 7 · ICP 13 · JUP 1 · QTUM 1 · TLM 11). Selama itu belum terpecahkan, funding
matang sebagai **PEMBUKUAN** namun **belum** sebagai **LANDASAN FITUR**.

Inilah tepatnya sebab `funding_ada` ditempatkan di **Lapis A**: satu-satunya utang yang
paling mudah dikira sudah beres justru yang paling merusak bila dibiarkan mati.

## Akibat

Serapan dapat ditutup hari ini tanpa melunasi semua utang, asalkan Lapis A dibayar dan
Lapis B/C dilabeli. Papan skor **343** tetap sah. Cacah TIDAK TERADJUDIKASI akan naik dari
**16** menjadi **21** bila kelima adjudikasi tangan Lapis C benar-benar ditutup paksa;
kenaikan itu **wajib disebut** setiap kali papan skor dikutip sesudahnya.

## Penomoran sesudah ADR ini

Aturan resmi **1–81, 83–94**; nol usulan hidup selain **KC-58**. Aturan berikutnya **95**.
ADR berikutnya **A025** (dan **A003** yang masih belum ada).

— akhir `decisions/ADR-A024.md` —
