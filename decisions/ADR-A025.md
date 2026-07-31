# ADR-A025 — Amandemen ADR-A004 §2: gerbang 1m berklausa ENAM, bukan LIMA

Status: **DITERIMA** 2026-07-31. Mengamandemen ADR-A004 §2.2 dan mengoreksi angka §2.2.

Dasar angka, seluruhnya dibaca utuh pada giliran 20–21:

- `lux_ai/serapan/gerbang_1m.py` blob `c8cc54c84a57173ef2e426c317d6ac50734e9b4a` (6.775 B)
- `tests/test_gerbang_1m.py` blob `a930af172fa51ca643384c7be30283958a225e46` (4.995 B)
- `decisions/ADR-A004.md` blob `ee603a8cbe576684b99985aa605dcc57988e304d` (4.367 B)
- `reports/penyebut_manifes.log` blob `85efd10bb9a6722749e0090b2ee68f2410a2d815`, run `30637911271`, atas kedelapan manifes pecahan (Σ 20.533.802 B)

## 1. Masalah

ADR-A004 §2.2 mendaftar dasar gerbang serapan sebagai **lima** klausa — "0 stempel duplikat; 0 menit hilang di dalam rentang berkas; seluruh jarak antar-baris tepat 60 detik; seluruh stempel selaras batas menit; satuan stempel milidetik" — dan menyebutnya "Kelima klausa ini".

Gerbang yang benar-benar berjalan menjalankan **enam**. Tetapan `KLAUSA` di `gerbang_1m.py`:

`deret_tidak_kosong` · `tanpa_duplikat` · `tanpa_menit_hilang` · `jarak_60_detik` · `selaras_menit` · `satuan_milidetik`

Klausa keenam, **`deret_tidak_kosong`**, tidak pernah diputuskan oleh ADR mana pun. Selama itu berdiri, setiap angka serapan berasal dari gerbang yang sebagian isinya tidak berdasar keputusan tertulis. Itulah penghalang klasifikasi baris 6.

## 2. Yang terukur sebelum diputuskan

1. **Klausa keenam tidak pernah menjatuhkan apa pun.** `gerbang.pelanggaran_per_klausa.deret_tidak_kosong` = 0 pada kedelapan pecahan, atas **19.598** simbol-bulan yang dinilai.
2. **Seluruh kegagalan berasal dari klausa yang berdasar ADR.** `jarak_60_detik` 12 dan `tanpa_menit_hilang` 12, deretnya identik (3,3,0,1,1,0,3,1); `tanpa_duplikat`, `selaras_menit`, `satuan_milidetik` nol. Total gagal 12, lolos 19.586 — tepat cacah yang dikemas.
3. **Nama klausa di kode dan di data cocok satu per satu.** `ringkas_gerbang()` menyemai pencacahnya dari `KLAUSA`, sehingga klausa bernol tetap terbit; tidak ada klausa yang diperiksa diam-diam.
4. **Cacah enam dikunci oleh uji.** `test_klausa_berjumlah_enam_dan_dinilai_semua` menegaskan `len(KLAUSA) == 6` dan `set(hasil["klausa"]) == set(KLAUSA)`. Menurunkan kode menjadi lima akan menggagalkan CI.
5. **Klausa keenam diuji dua arah.** `test_deret_kosong_gagal` membuktikan deret kosong memang ditolak, dan `test_deret_bersih_lolos` membuktikan deret bersih tidak ikut tertolak.

## 3. Keputusan

1. **`deret_tidak_kosong` DISAHKAN sebagai klausa keenam** gerbang integritas 1m. Alasannya bukan kenyamanan: tanpa klausa itu, deret kosong akan melewati kelima klausa lain secara vakum — nol duplikat, nol menit hilang, nol jarak salah, nol stempel tak selaras — dan sebuah berkas kosong akan LOLOS gerbang. Gerbang yang meloloskan ketiadaan bukan gerbang.
2. **ADR-A004 §2.2 dibaca sebagai enam klausa** sejak ADR ini. Frasa "Kelima klausa ini" pada ADR-A004 **kedaluwarsa**; ia tidak dihapus dari berkasnya agar jejak kesalahan tetap terbaca (aturan 36), melainkan dikoreksi di sini.
3. **Angka "100% bersih pada 84 simbol-bulan" pada ADR-A004 §2.2 DINYATAKAN KEDALUWARSA terhadap semesta penuh.** Angka yang sah kini: **12 gagal dari 19.598 = 0,061%**, `persen_lolos` per pecahan 99,88 · 99,88 · 100,0 · 99,95 · 99,96 · 100,0 · 99,89 · 99,96. Sampel 84 tidak dicabut; ia hanya bukan lagi angka semesta.
4. **Premis "arsip 1m utuh" TETAP BERDIRI.** ADR-A004 §5 menetapkan pembatalnya adalah pelanggaran "dalam jumlah besar". 0,061% tidak memenuhi itu. Yang berubah hanyalah bahwa premis itu kini punya angka semesta, bukan angka sampel.
5. **Kedua belas simbol-bulan yang gagal tetap dikarantina**, tidak dipulihkan dan tidak ditambal. Tidak ada toleransi yang ditambahkan (ADR-A004 §2.4 tetap berlaku penuh).

## 4. Alternatif yang ditolak

- **Mencabut `deret_tidak_kosong` dari kode agar cocok dengan ADR.** Ditolak: itu akan membuat berkas kosong lolos gerbang, dan itu memperburuk mutu demi kerapian dokumen.
- **Membiarkan selisihnya dan mencatatnya sebagai catatan kaki.** Ditolak: gerbang yang mengikat harus punya dasar keputusan penuh, bukan sebagian. Selama tidak disahkan, setiap angka serapan dapat digugat pada titik itu.
- **Menulis ulang ADR-A004 seluruhnya.** Ditolak: ADR-A004 tidak salah pada keputusan pokoknya (1m sebagai satu-satunya sumber). Yang salah hanya cacah klausa dan angka sampel; menulis ulang akan mengaburkan jejak kesalahan itu.
- **Menyatakan penghalang baris 6 jatuh tanpa ADR.** Ditolak: penghalang itu lahir dari ketiadaan keputusan tertulis, dan hanya keputusan tertulis yang menutupnya.

## 5. Akibat yang wajib diakui

- Penghalang klasifikasi baris 6 **JATUH**. Berdiri kini **sembilan** dari dua belas baris. Baris 1 — **ketakseimbangan 33 : 19.553** — tetap yang paling menentukan.
- **ADR ini TIDAK menyentuh baris 1.** Ia tidak menambah satu pun kelas positif, tidak menguji tabel silang, tidak menjelaskan 18 simbol tak berpola, dan tidak menguji B-2/B-3/B-4. **DILARANG mengutipnya sebagai kemajuan menuju klasifikasi maupun backtest.**
- Yang bertambah hanyalah ini: angka serapan 19.586 kini berdiri di atas gerbang yang seluruh klausanya berdasar keputusan tertulis dan berdasar uji dua arah.

## 6. Apa yang membatalkan ADR ini

- Bila ditemukan simbol-bulan yang dijatuhkan HANYA oleh `deret_tidak_kosong`, dasar §2.1 (klausa itu tidak pernah menjatuhkan apa pun) gugur dan pengesahannya harus dinilai ulang, bukan dipertahankan karena sudah tertulis.
- Bila `tests/test_gerbang_1m.py` ternyata tidak benar-benar menjaga kesamaan `ukur_deret` dengan `diagnosa_kc6.celah_menit` untuk seluruh medan, dasar §2.4 melemah. Yang terukur hari ini: uji itu membandingkan seluruh medan keluaran `celah_menit`; medan yang hanya ada di sisi gerbang TIDAK dijaga olehnya. Batas ini ditulis di muka, bukan ditemukan belakangan.
