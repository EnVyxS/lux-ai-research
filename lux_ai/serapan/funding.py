"""Diagnosa ketersediaan funding untuk semesta perpetual_usdt (utang 24).

`funding_ada` bernilai null di seluruh 19.598 baris manifes serapan karena
`serap.py` sengaja tidak mengambil funding. Modul ini mengukur ketersediaannya
lebih dulu, sebelum ada satu pun keputusan menulis medan itu.

Rancangan dan biayanya:

1. **Modul terpisah, bukan perubahan `pecahan.py`.** Menaikkan `VERSI` pecahan
   menyalakan delapan runner yang mengunduh 3-4,6 GB masing-masing, sekitar satu
   jam per job. Pertanyaan funding menyangkut berkas yang seluruh semestanya di
   bawah 25 MB (ADR-A002 bagian 7). Satu job cukup.
2. **Ketersediaan diukur lewat LISTING, bukan 404 per berkas.** Satu permintaan
   per simbol menggantikan 19.598 permintaan.
3. **Unduhan sungguhan hanya untuk SAMPEL berlapis** (aturan 37), agar ada bukti
   berkasnya benar-benar terambil dan cocok checksum, bukan sekadar namanya
   terdaftar di listing.
4. **Hanya pustaka baku.** Modul ini sengaja TIDAK mengimpor `serap`/`klines`,
   supaya tidak menyeret pandas dan pyarrow ke job yang tidak membutuhkannya.
   Harganya: beberapa konstanta batas diulang di sini. Bila `serap.py`
   mengubahnya, keduanya bisa hanyut, dan itu risiko yang dicatat, bukan
   disembunyikan.

Riwayat versi:

- VERSI 1 mengukur ketersediaan; hasilnya 880 bulan klines tanpa funding.
- VERSI 2 menambahkan bukti sampel ke log, daftar penuh, dan klasifikasi lubang;
  hasilnya 826 dari 880 lubang berada di EKOR riwayat simbol.
- VERSI 3 mengukur bentuk kohortnya: 38 simbol memulai lubang ekor tepat di
  2025-07, dan ketiga puluh delapan itu berjarak persis 12 bulan dari bulan
  klines terakhirnya. 456 simbol-bulan, 51,8% dari seluruh lubang.
- VERSI 4 menjawab keberatan yang sejak VERSI 1 tertulis di catatan metode:
  seluruh angka di atas berasal dari LISTING, dan ketiadaan nama di listing
  bukan ketiadaan berkas di CDN. Di sini berkas kohort diminta LANGSUNG.
  Permintaan itu tidak berarti apa-apa tanpa KENDALI: tanpa berkas pembanding
  yang terdaftar dan berhasil diambil, kode 404 tidak dapat dibedakan dari
  jalur unduh yang rusak (aturan 24). Hasilnya: 3 kohort menjawab 404, 3
  kendali menjawab 200 dengan checksum cocok.
- VERSI 5 memperbaiki dua kelemahan VERSI 4. Pertama, angka 38 dan 456 sampai
  kini hanya hidup di jurnal sebagai aritmetika tangan; di sini keduanya
  diterbitkan modul sendiri, dengan satuan yang DIPISAH (aturan 47) dan daftar
  anggotanya. Kedua, tiga pasang uji CDN dipilih dengan tangan karena mudah,
  dan itu bias pilihan. Sekarang pasangan dipilih DARI DATA: sepuluh anggota
  kohort pertama menurut urutan nama, dengan kendali bukan bulan tetangga yang
  ditebak melainkan bulan funding TERAKHIR simbol itu sendiri, yang menurut
  listing pasti ada. Ditambahkan pula bulan klines terakhir tiap anggota,
  karena klaim "kohort berhenti serempak" belum pernah diukur langsung; bila
  tidak seragam, klaim itu harus ditulis ulang.

Laporan ini **diagnostik** (`bukan_bukti: true`, aturan 10). Ia tidak mengubah
satu baris pun manifes serapan.

Aturan yang ditegakkan: 7, 10, 16, 20, 21, 22, 24, 30, 32, 36, 37, 41, 44, 46, 47.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import io
import json
import os
import urllib.error
import urllib.request
import zipfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

from . import arsip

VERSI = 5
SUMBER_RENTANG = "reports/semesta_rentang.json"
KELUARAN = "reports/funding_semesta.json"
KELUARAN_SELISIH = "reports/funding_selisih_penuh.json"
JENIS_DIIZINKAN = "perpetual_usdt"

# Diulang dari serap.py dengan sadar; lihat butir 4 di docstring.
BATAS_HEADER = "2022-01"
BATAS_BARU = "2025-01"
BATAS_HIDUP = "2026-05"
BATAS_DAFTAR = 500

# Banyaknya pasang kohort-kendali yang diminta langsung ke CDN. Tiap pasang
# adalah dua permintaan, jadi sepuluh pasang = dua puluh permintaan; masih jauh
# di bawah biaya listing dan tidak mendekati batas waktu job 300 detik.
BATAS_UJI_CDN = 10

# Kelas yang dapat ditentukan SEBELUM mengunduh. `pra_header` tidak masuk sini:
# ia hanya diketahui setelah berkasnya dibaca, dan menebaknya dari bulan akan
# mencampur dugaan dengan ukuran (aturan 16).
KELAS_PRA_UNDUH = ("bulan_awal_2020_2021", "non_ascii", "terhenti", "kendali_baru")
KELAS_RISIKO = ("pra_header",) + KELAS_PRA_UNDUH

MEDAN_SAMPEL_RINGKAS = (
    "simbol",
    "bulan",
    "kelas_terpilih",
    "berheader",
    "byte_zip",
    "cacah_baris",
    "gagal_unduh",
    "gagal_checksum",
)

# Daftar cadangan, dipakai HANYA bila kohort terukur kosong (mis. saat modul
# dijalankan dengan FUNDING_BATAS_SIMBOL kecil). Ketiga pasang inilah yang
# diuji VERSI 4; dipertahankan supaya hasil lama tetap dapat direproduksi.
UJI_KOHORT: Tuple[Tuple[str, str], ...] = (
    ("FTMUSDT", "2025-07"),
    ("KLAYUSDT", "2025-07"),
    ("LOOMUSDT", "2025-07"),
)
UJI_KENDALI: Tuple[Tuple[str, str], ...] = (
    ("FTMUSDT", "2025-06"),
    ("KLAYUSDT", "2025-06"),
    ("LOOMUSDT", "2025-06"),
)


def nama_keluaran() -> str:
    return KELUARAN


def nama_keluaran_selisih() -> str:
    return KELUARAN_SELISIH


def sidik_kode() -> str:
    """Aturan 22: seluruh berkas yang ikut menentukan isi laporan ini."""
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(["funding.py", "arsip.py"]):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def non_ascii(simbol: str) -> bool:
    return any(ord(ch) > 127 for ch in simbol)


def selisih_bulan(
    bulan_klines: Sequence[str], bulan_funding: Sequence[str]
) -> Dict[str, List[str]]:
    """Selisih dua arah, keduanya dilaporkan walau kosong (aturan 36)."""
    k = {str(b) for b in bulan_klines}
    f = {str(b) for b in bulan_funding}
    return {
        "klines_tanpa_funding": sorted(k - f),
        "funding_tanpa_klines": sorted(f - k),
    }


def _akhiran_hilang(bulan_klines: Sequence[str], hilang: Sequence[str]) -> List[str]:
    """Bulan-bulan akhiran berurutan yang hilang, setelah awalan dikurangi."""
    urut = sorted(str(b) for b in bulan_klines)
    kurang = {str(b) for b in hilang}
    awal = 0
    for b in urut:
        if b in kurang:
            awal += 1
        else:
            break
    ekor: List[str] = []
    for b in reversed(urut[awal:]):
        if b in kurang:
            ekor.append(b)
        else:
            break
    return sorted(ekor)


def klasifikasi_lubang(
    bulan_klines: Sequence[str], hilang: Sequence[str]
) -> Dict[str, int]:
    """Golongkan tiap bulan hilang: awalan, akhiran, atau tengah riwayat simbol.

    Awalan dihitung lebih dulu, akhiran dihitung dari SISA setelah awalan,
    sehingga simbol yang seluruh bulannya hilang tercacah sekali saja sebagai
    `awal` dan tidak pernah ganda. `hilang` yang memuat bulan di luar riwayat
    klines diabaikan; hanya irisannya yang dicacah.
    """
    urut = sorted(str(b) for b in bulan_klines)
    kurang = {str(b) for b in hilang}
    awal = 0
    for b in urut:
        if b in kurang:
            awal += 1
        else:
            break
    ekor = len(_akhiran_hilang(urut, kurang))
    total = sum(1 for b in urut if b in kurang)
    return {"awal": awal, "ekor": ekor, "tengah": total - awal - ekor, "hilang": total}


def mulai_lubang_ekor(
    bulan_klines: Sequence[str], hilang: Sequence[str]
) -> Optional[str]:
    """Bulan PERTAMA dari lubang ekor, atau None bila tidak ada lubang ekor.

    None dan "tidak ada lubang" adalah keadaan yang sama di sini, tetapi None
    tidak boleh diam-diam menjadi nol di histogram; pemanggil wajib menyaringnya
    (aturan 46).
    """
    ekor = _akhiran_hilang(bulan_klines, hilang)
    return ekor[0] if ekor else None


def jarak_bulan(awal: str, akhir: str) -> Optional[int]:
    """Selisih kalender dalam bulan; None bila salah satu tidak berbentuk YYYY-MM."""
    try:
        ta, ba = str(awal).split("-")
        tb, bb = str(akhir).split("-")
        return (int(tb) * 12 + int(bb)) - (int(ta) * 12 + int(ba))
    except (ValueError, AttributeError):
        return None


def histogram(nilai: Sequence[Any]) -> Dict[str, int]:
    """Cacah kemunculan, kunci terurut. None disaring, bukan dijadikan kunci."""
    cacah: Dict[str, int] = {}
    for n in nilai:
        if n is None:
            continue
        kunci = str(n)
        cacah[kunci] = cacah.get(kunci, 0) + 1
    return {k: cacah[k] for k in sorted(cacah)}


def puncak_histogram(h: Dict[str, int]) -> Dict[str, Any]:
    """Kunci dengan cacah terbesar; seri dimenangkan kunci terkecil, dan
    keseriannya DILAPORKAN, bukan disembunyikan."""
    if not h:
        return {"kunci": None, "cacah": 0, "seri": False}
    tertinggi = max(h.values())
    kandidat = sorted(k for k, v in h.items() if v == tertinggi)
    return {"kunci": kandidat[0], "cacah": tertinggi, "seri": len(kandidat) > 1}


def anggota_kohort(per_simbol: List[Dict[str, Any]], kunci: Optional[str]) -> List[Dict[str, Any]]:
    """Baris per-simbol yang lubang ekornya mulai tepat di `kunci`, terurut nama."""
    if kunci is None:
        return []
    pilih = [b for b in per_simbol if b.get("mulai_lubang_ekor") == kunci]
    return sorted(pilih, key=lambda x: str(x.get("simbol") or ""))


def kumpulkan_kohort(
    per_simbol: List[Dict[str, Any]], kunci: Optional[str]
) -> Dict[str, Any]:
    """Terbitkan kohort puncak sebagai angka modul, bukan aritmetika tangan.

    Dua satuan dipisah dengan sengaja: `cacah_simbol` dalam SIMBOL dan
    `cacah_simbol_bulan` dalam SIMBOL-BULAN. Menukar keduanya persis kesalahan
    yang membuat R-163 kalah, dan aturan 47 lahir darinya.

    `cacah_tanpa_bulan_terakhir` adalah medan penggugur bagi keseragaman:
    histogram menyaring None, jadi tanpa medan ini sebuah kohort yang separuh
    anggotanya tak punya bulan terakhir bisa tampak seragam sempurna.
    """
    anggota = anggota_kohort(per_simbol, kunci)
    simbol_bulan = sum(
        int((b.get("bentuk_lubang") or {}).get("ekor") or 0) for b in anggota
    )
    terakhir = [b.get("bulan_klines_terakhir") for b in anggota]
    tanpa = sum(1 for t in terakhir if not t)
    hist = histogram([t for t in terakhir if t])
    return {
        "bulan_mulai": kunci,
        "cacah_simbol": len(anggota),
        "cacah_simbol_bulan": simbol_bulan,
        "cacah_tanpa_bulan_terakhir": tanpa,
        "simbol": [str(b.get("simbol")) for b in anggota],
        "histogram_bulan_klines_terakhir": hist,
        "puncak_bulan_klines_terakhir": puncak_histogram(hist),
        "seragam_bulan_klines_terakhir": bool(anggota) and len(hist) == 1 and tanpa == 0,
        "catatan_satuan": (
            "cacah_simbol bersatuan SIMBOL dan cacah_simbol_bulan bersatuan "
            "SIMBOL-BULAN; keduanya tidak boleh saling menggantikan (aturan 47)"
        ),
        "catatan_seragam": (
            "seragam_bulan_klines_terakhir hanya benar bila SELURUH anggota "
            "punya bulan terakhir yang sama DAN tidak ada anggota tanpa bulan "
            "terakhir; bila cacah_tanpa_bulan_terakhir != 0 keseragaman tidak "
            "dapat disimpulkan (aturan 46)"
        ),
    }


def pasangan_uji(
    per_simbol: List[Dict[str, Any]],
    kunci: Optional[str],
    batas: int = BATAS_UJI_CDN,
) -> List[Tuple[str, str, str]]:
    """Pasangan (simbol, bulan kohort, bulan kendali) yang dipilih DARI DATA.

    Kendali bukan bulan tetangga yang ditebak, melainkan bulan funding TERAKHIR
    simbol itu sendiri: menurut listing ia pasti ada, sehingga kegagalannya
    menunjuk jalur unduh dan bukan arsip. Anggota tanpa bulan funding sama
    sekali dilewati, karena baginya tidak ada kendali yang sah.
    """
    pasang: List[Tuple[str, str, str]] = []
    for b in anggota_kohort(per_simbol, kunci):
        kendali = b.get("bulan_funding_terakhir")
        if not kendali:
            continue
        pasang.append((str(b.get("simbol")), str(kunci), str(kendali)))
        if len(pasang) >= batas:
            break
    return pasang


def periksa_url(url: str, timeout: int = 60) -> Dict[str, Any]:
    """Minta satu URL dan laporkan kode HTTP apa adanya.

    404 (server menjawab: tidak ada) dan galat jaringan (server tidak menjawab)
    adalah dua keadaan yang berbeda. Menyamakan keduanya persis kesalahan yang
    dilarang aturan 46, maka `kode_http` tetap None saat yang terjadi adalah
    galat, dan `galat` tetap None saat yang terjadi adalah 404.
    """
    baris: Dict[str, Any] = {
        "url": url,
        "kode_http": None,
        "byte": None,
        "checksum_sha256": None,
        "teks_awal": None,
        "galat": None,
    }
    try:
        with urllib.request.urlopen(url, timeout=timeout) as jawab:
            data = jawab.read()
            baris["kode_http"] = int(getattr(jawab, "status", 200) or 200)
            baris["byte"] = len(data)
            baris["checksum_sha256"] = hashlib.sha256(data).hexdigest()
            baris["teks_awal"] = data[:200].decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        baris["kode_http"] = int(exc.code)
    except Exception as exc:  # noqa: BLE001
        baris["galat"] = str(exc)[:200]
    return baris


def periksa_berkas_funding(simbol: str, bulan: str, peran: str) -> Dict[str, Any]:
    """Minta satu berkas funding langsung ke CDN, lalu cocokkan checksum resmi.

    `checksum_cocok` bernilai None bila berkas tidak terambil; None berarti
    "tidak dapat diperiksa", bukan "tidak cocok".
    """
    url = arsip.url_funding(simbol, bulan)
    baris = periksa_url(url)
    baris["simbol"] = simbol
    baris["bulan"] = bulan
    baris["peran"] = peran
    baris["checksum_cocok"] = None
    if baris["kode_http"] == 200 and baris["checksum_sha256"]:
        sidik = periksa_url(url + ".CHECKSUM")
        baris["kode_http_checksum"] = sidik["kode_http"]
        teks = sidik.get("teks_awal") or ""
        if sidik["kode_http"] == 200 and teks:
            baris["checksum_cocok"] = baris["checksum_sha256"] in teks.split()
    return baris


def ringkas_uji_cdn(
    kohort: List[Dict[str, Any]], kendali: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """Cacah hasil uji CDN, dengan kendali sebagai medan penggugur.

    Bila kendali tidak seluruhnya 200 dan cocok checksum, jalur unduh sendiri
    yang tidak dapat dipercaya, dan seluruh angka kohort di blok ini batal.
    """
    kendali_200 = sum(1 for b in kendali if b.get("kode_http") == 200)
    kendali_cocok = sum(1 for b in kendali if b.get("checksum_cocok") is True)
    sah = bool(kendali) and kendali_200 == len(kendali) and kendali_cocok == len(kendali)
    return {
        "cacah_kohort_diminta": len(kohort),
        "cacah_kohort_404": sum(1 for b in kohort if b.get("kode_http") == 404),
        "cacah_kohort_200": sum(1 for b in kohort if b.get("kode_http") == 200),
        "cacah_kohort_galat": sum(1 for b in kohort if b.get("galat")),
        "cacah_kendali_diminta": len(kendali),
        "cacah_kendali_200": kendali_200,
        "cacah_kendali_checksum_cocok": kendali_cocok,
        "kendali_sah": sah,
        "catatan": (
            "bila kendali_sah false, jalur unduh tidak terbukti bekerja dan "
            "seluruh cacah kohort di blok ini BATAL (aturan 24); 404 berarti "
            "server menjawab tidak ada, galat berarti server tidak menjawab, "
            "dan keduanya tidak boleh disamakan (aturan 46)"
        ),
    }


def jalankan_uji_cdn(
    pasangan: Optional[Sequence[Tuple[str, str, str]]] = None
) -> Dict[str, Any]:
    """Uji kohort dan kendali berdampingan; keduanya selalu dijalankan.

    Pasangan yang terpilih dari data lebih disukai daripada daftar tetap,
    karena daftar tetap dipilih tangan dan itu bias pilihan yang diakui.
    """
    if pasangan:
        kohort = [periksa_berkas_funding(s, bk, "kohort") for s, bk, _ in pasangan]
        kendali = [periksa_berkas_funding(s, bn, "kendali") for s, _, bn in pasangan]
        sumber = "kohort terukur"
    else:
        kohort = [periksa_berkas_funding(s, b, "kohort") for s, b in UJI_KOHORT]
        kendali = [periksa_berkas_funding(s, b, "kendali") for s, b in UJI_KENDALI]
        sumber = "daftar tetap"
    hasil = ringkas_uji_cdn(kohort, kendali)
    hasil["sumber_pasangan"] = sumber
    hasil["baris"] = [
        {
            m: b.get(m)
            for m in (
                "peran",
                "simbol",
                "bulan",
                "kode_http",
                "byte",
                "checksum_cocok",
                "galat",
            )
        }
        for b in kohort + kendali
    ]
    return hasil


def kelas_bulan(simbol: str, bulan: str, bulan_terakhir: str = "") -> List[str]:
    """Kelas risiko yang sudah pasti sebelum berkasnya diunduh."""
    kelas: List[str] = []
    if bulan and bulan < BATAS_HEADER:
        kelas.append("bulan_awal_2020_2021")
    if non_ascii(simbol):
        kelas.append("non_ascii")
    if bulan_terakhir and bulan_terakhir < BATAS_HIDUP:
        kelas.append("terhenti")
    if bulan and bulan >= BATAS_BARU:
        kelas.append("kendali_baru")
    return kelas


def pilih_sampel(
    kandidat: List[Dict[str, Any]], kelas_wajib: Sequence[str] = KELAS_PRA_UNDUH
) -> List[Dict[str, Any]]:
    """Satu wakil tiap kelas, deterministik menurut (simbol, bulan).

    Kelas yang tidak punya kandidat sama sekali TIDAK menghasilkan wakil, dan
    ketiadaannya dilaporkan sebagai kelas kosong, bukan diam-diam dilewati.
    """
    urut = sorted(
        kandidat, key=lambda x: (str(x.get("simbol") or ""), str(x.get("bulan") or ""))
    )
    dipilih: List[Dict[str, Any]] = []
    terpakai = set()
    for kelas in kelas_wajib:
        for c in urut:
            if kelas not in (c.get("kelas") or []):
                continue
            kunci = (str(c.get("simbol")), str(c.get("bulan")))
            if kunci in terpakai:
                continue
            terpakai.add(kunci)
            salinan = dict(c)
            salinan["kelas_terpilih"] = kelas
            dipilih.append(salinan)
            break
    return dipilih


def _angka(teks: str) -> bool:
    try:
        float(teks.strip())
        return True
    except ValueError:
        return False


def baca_zip_funding(data: bytes) -> Dict[str, Any]:
    """Baca zip fundingRate dengan pustaka baku saja.

    `decode("utf-8", "replace")` dipakai seperti di `klines.py`; ia membungkam
    byte rusak dan sudah terdaftar sebagai temuan yang belum diukur.
    """
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        nama = sorted(z.namelist())
        if not nama:
            return {
                "berkas_dalam_zip": None,
                "berheader": None,
                "cacah_baris": 0,
                "baris_pertama": "",
            }
        isi = z.read(nama[0]).decode("utf-8", "replace")
    garis = [g for g in isi.splitlines() if g.strip()]
    if not garis:
        return {
            "berkas_dalam_zip": nama[0],
            "berheader": None,
            "cacah_baris": 0,
            "baris_pertama": "",
        }
    pertama = garis[0]
    berheader = not _angka(pertama.split(",")[0])
    return {
        "berkas_dalam_zip": nama[0],
        "berheader": berheader,
        "cacah_baris": len(garis) - (1 if berheader else 0),
        "baris_pertama": pertama[:200],
    }


def ukur_satu(simbol: str, bulan: str, kelas_terpilih: Optional[str] = None) -> Dict[str, Any]:
    """Unduh satu berkas funding, cocokkan checksum resmi, lalu baca isinya."""
    url = arsip.url_funding(simbol, bulan)
    baris: Dict[str, Any] = {
        "simbol": simbol,
        "bulan": bulan,
        "kelas_terpilih": kelas_terpilih,
        "sumber_url": url,
        "gagal_unduh": False,
        "gagal_checksum": False,
        "galat": None,
    }
    try:
        data = arsip.unduh_terverifikasi(url)
    except Exception as exc:  # noqa: BLE001
        pesan = str(exc)
        baris["gagal_unduh"] = True
        baris["gagal_checksum"] = "checksum" in pesan.lower() or "sha256" in pesan.lower()
        baris["galat"] = pesan[:300]
        return baris
    baris["byte_zip"] = len(data)
    baris["checksum_zip_sha256"] = hashlib.sha256(data).hexdigest()
    baris.update(baca_zip_funding(data))
    return baris


def ringkas_sampel(sampel: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Baris sampel sekecil mungkin, cukup untuk mengadjudikasi tanpa JSON penuh.

    `berheader` sengaja dipertahankan apa adanya, termasuk `None`: null dan
    false adalah dua keadaan berbeda, dan menyamakannya persis kesalahan yang
    dilarang aturan 46.
    """
    keluar: List[Dict[str, Any]] = []
    for s in sampel:
        keluar.append({medan: s.get(medan) for medan in MEDAN_SAMPEL_RINGKAS})
    return keluar


def daftar_penuh(per_simbol: List[Dict[str, Any]]) -> Dict[str, List[str]]:
    """Kedua daftar selisih TANPA dipotong, untuk berkas terpisah."""
    ktf: List[str] = []
    ftk: List[str] = []
    for baris in per_simbol:
        simbol = str(baris.get("simbol") or "")
        for b in baris.get("klines_tanpa_funding") or []:
            ktf.append(f"{simbol}:{b}")
        for b in baris.get("funding_tanpa_klines") or []:
            ftk.append(f"{simbol}:{b}")
    return {
        "klines_tanpa_funding": sorted(ktf),
        "funding_tanpa_klines": sorted(ftk),
    }


def ringkas_selisih(
    per_simbol: List[Dict[str, Any]], batas: int = BATAS_DAFTAR
) -> Dict[str, Any]:
    """Cacah kedua arah selisih; daftarnya dipotong dan pemotongannya dilapor."""
    penuh = daftar_penuh(per_simbol)
    ktf = penuh["klines_tanpa_funding"]
    ftk = penuh["funding_tanpa_klines"]
    return {
        "cacah_bulan_klines_tanpa_funding": len(ktf),
        "cacah_bulan_funding_tanpa_klines": len(ftk),
        "daftar_klines_tanpa_funding": ktf[:batas],
        "daftar_funding_tanpa_klines": ftk[:batas],
        "daftar_terpotong": len(ktf) > batas or len(ftk) > batas,
        "batas_daftar": batas,
        "berkas_daftar_penuh": KELUARAN_SELISIH,
    }


def kelas_tersentuh(sampel: List[Dict[str, Any]]) -> Dict[str, int]:
    """Cacah kelas risiko yang benar-benar tersentuh sampel, dilapor walau nol."""
    cacah = {nama: 0 for nama in KELAS_RISIKO}
    for s in sampel:
        for k in s.get("kelas") or []:
            if k in cacah:
                cacah[k] += 1
        if s.get("berheader") is False:
            cacah["pra_header"] += 1
    return cacah


def jalankan(akar: str = ".") -> Dict[str, Any]:
    from ..semesta import taksonomi

    basis = Path(akar)
    mentah = (basis / SUMBER_RENTANG).read_bytes()
    rentang = json.loads(mentah.decode("utf-8")).get("rentang", {})
    if not isinstance(rentang, dict):
        rentang = {}

    simbol = [
        s
        for s, isi in sorted(rentang.items())
        if isinstance(isi, dict) and taksonomi.jenis_instrumen(s) == JENIS_DIIZINKAN
    ]
    batas_simbol = int(os.environ.get("FUNDING_BATAS_SIMBOL", "0") or 0)
    if batas_simbol > 0:
        simbol = simbol[:batas_simbol]

    per_simbol: List[Dict[str, Any]] = []
    kandidat: List[Dict[str, Any]] = []
    gagal_daftar: List[str] = []
    cacah_bulan_klines = 0
    cacah_bulan_funding = 0
    lubang = {"awal": 0, "ekor": 0, "tengah": 0, "hilang": 0}
    tanpa_funding_sama_sekali = 0
    mulai_ekor: List[str] = []
    jarak_terakhir: List[int] = []
    cacah_simbol_ekor = 0

    for nama in simbol:
        isi = rentang.get(nama) or {}
        terakhir = str(isi.get("bulan_terakhir") or "")
        try:
            bulan_k = sorted(arsip.bulan_tersedia(nama))
            bulan_f = sorted(arsip.bulan_tersedia(nama, jenis="fundingRate"))
        except Exception as exc:  # noqa: BLE001
            gagal_daftar.append(f"{nama}: {str(exc)[:120]}")
            continue
        cacah_bulan_klines += len(bulan_k)
        cacah_bulan_funding += len(bulan_f)
        if bulan_k and not bulan_f:
            tanpa_funding_sama_sekali += 1
        beda = selisih_bulan(bulan_k, bulan_f)
        bentuk = klasifikasi_lubang(bulan_k, beda["klines_tanpa_funding"])
        for kunci in lubang:
            lubang[kunci] += bentuk[kunci]
        mulai = mulai_lubang_ekor(bulan_k, beda["klines_tanpa_funding"])
        jarak = None
        if mulai is not None:
            cacah_simbol_ekor += 1
            mulai_ekor.append(mulai)
            if bulan_k and bulan_f:
                jarak = jarak_bulan(bulan_f[-1], bulan_k[-1])
                if jarak is not None:
                    jarak_terakhir.append(jarak)
        per_simbol.append(
            {
                "simbol": nama,
                "cacah_bulan_klines": len(bulan_k),
                "cacah_bulan_funding": len(bulan_f),
                "bulan_klines_terakhir": bulan_k[-1] if bulan_k else None,
                "bulan_funding_terakhir": bulan_f[-1] if bulan_f else None,
                "bentuk_lubang": bentuk,
                "mulai_lubang_ekor": mulai,
                "jarak_bulan_terakhir": jarak,
                "klines_tanpa_funding": beda["klines_tanpa_funding"],
                "funding_tanpa_klines": beda["funding_tanpa_klines"],
            }
        )
        for b in bulan_f:
            kelas = kelas_bulan(nama, b, terakhir)
            if kelas:
                kandidat.append({"simbol": nama, "bulan": b, "kelas": kelas})

    terpilih = pilih_sampel(kandidat)
    sampel: List[Dict[str, Any]] = []
    for c in terpilih:
        hasil = ukur_satu(str(c["simbol"]), str(c["bulan"]), str(c.get("kelas_terpilih")))
        hasil["kelas"] = list(c.get("kelas") or [])
        sampel.append(hasil)

    ringkas = ringkas_selisih(per_simbol)
    kelas = kelas_tersentuh(sampel)
    byte_sampel = [int(s.get("byte_zip") or 0) for s in sampel if not s.get("gagal_unduh")]
    hist_mulai = histogram(mulai_ekor)
    hist_jarak = histogram(jarak_terakhir)
    puncak = puncak_histogram(hist_mulai)
    kohort = kumpulkan_kohort(per_simbol, puncak.get("kunci"))
    pasangan = pasangan_uji(per_simbol, puncak.get("kunci"))

    laporan: Dict[str, Any] = {
        "status": "TERUKUR" if simbol else "TIDAK MENGUKUR",
        "versi_funding": VERSI,
        "bukan_bukti": True,
        "penyebut": {
            "simbol_diminta": len(simbol),
            "simbol_terdaftar": len(per_simbol),
            "bulan_klines": cacah_bulan_klines,
            "bulan_funding": cacah_bulan_funding,
            "simbol_dengan_lubang_ekor": cacah_simbol_ekor,
        },
        "cacah_simbol_gagal_daftar": len(gagal_daftar),
        "contoh_gagal_daftar": gagal_daftar[:10],
        "cacah_simbol_tanpa_funding_sama_sekali": tanpa_funding_sama_sekali,
        "bentuk_lubang": {
            "awal": lubang["awal"],
            "ekor": lubang["ekor"],
            "tengah": lubang["tengah"],
            "hilang": lubang["hilang"],
        },
        "histogram_mulai_lubang_ekor": hist_mulai,
        "puncak_mulai_lubang_ekor": puncak,
        "kohort_puncak": kohort,
        "histogram_jarak_bulan_terakhir": hist_jarak,
        "uji_cdn": jalankan_uji_cdn(pasangan),
        "cacah_sampel": len(sampel),
        "cacah_sampel_gagal_unduh": sum(1 for s in sampel if s.get("gagal_unduh")),
        "cacah_sampel_gagal_checksum": sum(1 for s in sampel if s.get("gagal_checksum")),
        "byte_zip_sampel_min": min(byte_sampel) if byte_sampel else None,
        "byte_zip_sampel_maks": max(byte_sampel) if byte_sampel else None,
        "kelas_risiko_tersentuh": kelas,
        "kelas_risiko_kosong": [n for n, v in kelas.items() if not v],
        "sampel_ringkas": ringkas_sampel(sampel),
        "sampel": sampel,
        "per_simbol": per_simbol,
    }
    laporan.update(ringkas)
    laporan["selisih_klasifikasi"] = (
        laporan["cacah_bulan_klines_tanpa_funding"]
        - (lubang["awal"] + lubang["ekor"] + lubang["tengah"])
    )
    laporan["selisih_histogram"] = cacah_simbol_ekor - sum(hist_mulai.values())
    laporan["selisih_kohort"] = int(puncak.get("cacah") or 0) - int(kohort["cacah_simbol"])
    laporan["catatan_bukan_bukti"] = (
        "laporan ini diagnostik: ia mengukur ketersediaan funding dan TIDAK "
        "menulis funding_ada di manifes mana pun"
    )
    laporan["catatan_penggugur"] = (
        "cacah_simbol_gagal_daftar != 0 berarti listing tidak lengkap dan seluruh "
        "cacah di laporan ini batal sebagai angka semesta; bulan_klines != 19.598 "
        "berarti semesta yang dilihat modul ini bukan semesta manifes serapan, "
        "sehingga perbandingannya tidak sah; selisih_klasifikasi != 0 berarti "
        "cacah bentuk_lubang bocor; selisih_histogram != 0 berarti histogram "
        "bulan-mulai bocor dan seluruh angka kohort batal; selisih_kohort != 0 "
        "berarti daftar anggota kohort tidak sepadan dengan puncak histogram "
        "dan cacah_simbol di kohort_puncak tidak boleh dipakai; "
        "uji_cdn.kendali_sah == false berarti jalur unduh tidak terbukti dan "
        "seluruh cacah uji_cdn batal (aturan 24)"
    )
    laporan["catatan_metode"] = (
        "ketersediaan diukur dari listing S3, bukan dari 404 per berkas; unduhan "
        "sungguhan hanya untuk sampel berlapis (aturan 37). Ketiadaan nama di "
        "listing dan ketiadaan berkas di CDN adalah dua hal berbeda; blok "
        "uji_cdn memeriksa perbedaan itu pada sejumlah kecil pasang berkas "
        "saja, bukan pada 880"
    )
    laporan["catatan_bentuk_lubang"] = (
        "awal dihitung lebih dulu, ekor dari sisa setelah awal; simbol yang "
        "seluruh bulannya tanpa funding masuk awal saja, jadi angka ekor adalah "
        "batas BAWAH bagi gejala hilang-di-akhir, bukan taksiran tengahnya"
    )
    laporan["catatan_kohort"] = (
        "histogram_mulai_lubang_ekor mencacah SIMBOL, bukan bulan; satu simbol "
        "menyumbang tepat satu bulan-mulai. Puncak yang tinggi menunjukkan "
        "banyak simbol berhenti serempak, tetapi TIDAK dengan sendirinya "
        "membuktikan sebabnya ada di sisi arsip: bulan yang sama juga bisa "
        "lahir dari satu gelombang delisting. Membedakan keduanya memerlukan "
        "sumber di luar arsip dan BELUM dilakukan"
    )
    laporan["catatan_uji_cdn"] = (
        "pasangan uji dipilih dari kohort terukur, sepuluh anggota pertama "
        "menurut urutan nama; urutan nama bukan pengacakan, jadi ini sampel "
        "sistematis dan bukan sampel acak. Hasilnya berlaku untuk berkas yang "
        "benar-benar diminta saja dan tidak boleh digeneralkan ke seluruh "
        "simbol-bulan kohort tanpa pengukuran lanjutan (aturan 20)"
    )
    laporan["catatan_jarak"] = (
        "jarak_bulan_terakhir = bulan klines terakhir dikurangi bulan funding "
        "terakhir, dihitung hanya untuk simbol yang punya lubang ekor; simbol "
        "tanpa lubang ekor tidak menyumbang nol, ia tidak menyumbang apa pun"
    )
    laporan["catatan_rentang"] = (
        "kesimpulan berlaku untuk semesta perpetual_usdt pada semesta_rentang.json "
        "saja, bukan untuk 937 simbol arsip (aturan 20)"
    )
    laporan["catatan_kelas_kosong"] = (
        "kelas risiko tanpa kandidat tidak menghasilkan wakil sampel; klaim "
        "apa pun tentang kelas itu berpenyebut nol dan TIDAK dapat dibedakan "
        "dari kasus lain (aturan 41, 46)"
    )
    laporan["sumber_rentang"] = SUMBER_RENTANG
    laporan["sidik_data"] = hashlib.sha256(mentah).hexdigest()
    laporan["sidik_kode"] = sidik_kode()
    laporan["waktu_utc"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    penuh = daftar_penuh(per_simbol)
    penuh["cacah_klines_tanpa_funding"] = len(penuh["klines_tanpa_funding"])
    penuh["cacah_funding_tanpa_klines"] = len(penuh["funding_tanpa_klines"])
    penuh["kohort_puncak"] = kohort
    penuh["versi_funding"] = VERSI
    penuh["sidik_kode"] = laporan["sidik_kode"]
    penuh["sidik_data"] = laporan["sidik_data"]
    penuh["waktu_utc"] = laporan["waktu_utc"]

    for nama_berkas, isi_berkas in ((KELUARAN, laporan), (KELUARAN_SELISIH, penuh)):
        tujuan = basis / nama_berkas
        tujuan.parent.mkdir(parents=True, exist_ok=True)
        tujuan.write_text(
            json.dumps(isi_berkas, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    return laporan


def main() -> None:
    hasil = jalankan()
    ringkas = {k: v for k, v in hasil.items() if k not in ("per_simbol", "sampel")}
    print(json.dumps(ringkas, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
