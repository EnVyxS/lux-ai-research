# ADR-A015 — Pita praregistrasi wajib melewati aritmetika implikasi

- Status: **DITERIMA**
- Tanggal: 2026-07-30
- Konteks commit: `d22364b9bf680c9e3bbafa0c28672b3b561db702`
- Jurnal terkait: 129
- Menggantikan: tidak ada. Melengkapi ADR-A014 (KC-48, aturan 82).

## Konteks

R-307 kalah pada butir 1 karena pita 0.02..0.15 dipasang tanpa menghitung bahwa
7,15% baris dibagi nisbah rata 4,3 kira-kira menghasilkan 1,7% byte. R-308 kalah
pada butir 2 karena pita 10..300 dipasang tanpa menghitung bahwa kelas MATI
ber-rata 413.306 dengan maksimum 451.875 pasti memiliki ekor bawah yang tipis.

Dua kekalahan berturut-turut dengan sebab yang sama bukan kebetulan. Keduanya
bukan kesalahan pengukuran dan bukan kesalahan alam; keduanya kesalahan LETAK
ambang, yang seluruhnya dapat dihindari dengan aritmetika yang bahannya sudah
tersedia sebelum run.

## Keputusan

1. **KC-49 DITETAPKAN RESMI**: pita praregistrasi dikunci tanpa lebih dulu
   menghitung implikasi aritmetis dari momen yang SUDAH terukur (rata, min, maks,
   penyebut, nisbah antar kelas). Berbeda dari KC-48, yang menyangkut ambang
   MUSTAHIL sehingga butir tidak pernah menguji alam. KC-49 menyangkut ambang yang
   mungkin dilewati tetapi hasilnya sudah tersirat, sehingga pita dipasang di
   tempat yang salah.

2. **Aturan 83 DIUSULKAN**: sebelum mengunci pita praregistrasi, tuliskan di
   jurnal aritmetika implikasi dari setiap momen terukur yang relevan. Bila
   aritmetika itu sudah menentukan jawabannya dalam satu angka signifikan, butir
   tersebut bukan ramalan berisiko dan harus diganti atau dipindah porosnya.

3. **Aturan 82 (usulan, ADR-A014) DIPERLUAS** dari "dilarang mengunci ambang yang
   mustahil dilewati" menjadi "dilarang mengunci ambang yang mustahil dilewati
   ATAU yang hasilnya sudah tersirat oleh ukuran sebelumnya". Nomor 82 tetap
   berstatus DIUSULKAN; aturan resmi tetap sampai 81.

4. **R-308 diadjudikasi SEPARUH**: butir 1 MENANG (38 dalam 20..600), butir 2
   KALAH (2 lawan 10..300), butir 3 MENANG. Papan skor menjadi 308 dengan SEPARUH
   21. Pita tidak diubah sesudah melihat hasil, dan godaan untuk melebarkan
   10..300 menjadi 1..300 direkam di sini lalu DITOLAK (aturan 29).

5. **Tafsir H-A018 dipersempit lebih jauh**: di zona 22.440–97.634 byte terdapat
   38 baris HIDUP dan NOL baris MATI. Karena itu besar berkas DILARANG dipakai
   sebagai detektor status ke arah mana pun — bukan hanya "kecil = mati" yang
   dilarang, tetapi juga kebalikannya sebagai aturan umum. Yang boleh dinyatakan
   hanyalah angka agregat terukur.

6. **H-A019 DIDAFTARKAN** (byte kecil menandai bulan sebagian: bulan pertama
   pencatatan atau bulan tepi jendela), dengan catatan bahwa hipotesis ini lahir
   dari membaca daftar hasil R-308, sehingga WAJIB diuji atas semesta penuh dengan
   pita terkunci lebih dulu. R-309 mempraregistrasikannya.

7. **Cacah invarian wajib menyebut mana yang bebas.** Dalam `irisan_byte`,
   `total_byte` dihitung dari jumlah byte per kelas sehingga `selisih_total_byte`
   adalah turunan: sembilan medan selisih berarti delapan pemeriksaan bebas dan
   satu turunan. Laporan dan jurnal DILARANG menyebut angka mentahnya sebagai
   jumlah pemeriksaan bebas.

8. **Aturan 57 dicatat PUTUS pada giliran ke-27** dengan hasil 26/27; hitungan
   beruntun dimulai kembali dari nol. Ramalan yang diperbaiki setelah membaca
   berkas tidak dihitung sebagai ramalan.

## Akibat

- Setiap praregistrasi berikutnya harus memuat satu paragraf aritmetika implikasi.
  R-309 di jurnal 129 §10 sudah mematuhinya.
- KC berikutnya adalah KC-50; ADR berikutnya A016; aturan berikutnya 84.
