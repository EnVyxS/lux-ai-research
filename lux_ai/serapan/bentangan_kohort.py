"""Bentangan kehidupan 38 anggota kohort ekor funding 2025-07 — penguji R-302.

V1 (blob c0c7e334, commit ffa45371) TIDAK PERNAH menghasilkan laporan. Ia lulus
seluruh 45 butir ujinya dan lulus impor CI (run 30486876254, 814 butir, kode 0),
lalu mati di waktu jalan. Sebabnya dicatat di sini supaya tidak terulang, sebab
inilah KC-43: MENYUSUN MODUL ATAS NAMA FUNGSI TANPA MEMBACA BENTUK KEMBALIANNYA.

Tanda tangan nyata `silang_funding` (blob 42c3aa9d), DIKUTIP, bukan diingat:

    Kunci = Tuple[str, str]                      # (simbol, bulan) — TUPLE, bukan string
    baca_laporan_kehidupan(akar, total)
        -> Tuple[Dict[Kunci, str], Dict[Kunci, int], Dict[str, Any]]
    baca_medan_baris(akar, total, medan)
        -> Tuple[Dict[Kunci, Any], Dict[str, Any]]
    lubang_funding(funding)
        -> Tuple[Set[Kunci], Dict[str, Any]]

V1 menulis `lubang = silang_funding.lubang_funding(funding)` lalu `lubang.get(...)`;
`tuple` tidak punya `.get`, jadi ia gugur dengan `AttributeError` pada anggota
pertama, sebelum satu byte laporan pun ditulis. Cacat kembar yang sama ada pada
`baca_medan_baris`. Dan `POLA_KUNCI` V1 — yang docstringnya berbangga "format kunci
TIDAK diasumsikan" — tetap mengasumsikan bahwa kuncinya STRING; `str(("X","2026-06"))`
berakhir dengan tanda kurung, sehingga regexnya akan menolak seluruh 19.586 kunci.

V2 memperlakukan kunci TUPLE sebagai bentuk kanon dan tetap menerima kunci string
sebagai bentuk sampingan. Butir uji V2 memakai bentuk data yang SAMA dengan bentuk
nyata sumbernya — data sintetis yang bentuknya dikarang sendiri hanya menguji
karangan itu (penangkal KC-43).

## Apa yang diukur

Untuk setiap anggota kohort puncak funding 2025-07 (daftar namanya DIBACA di runner
lewat `kohort_ekor.muat_kohort`, TIDAK pernah menjadi tetapan di sini — aturan 73,
dijaga butir uji terakhir), bentangan status bulanan dari laporan kehidupan
disusun apa adanya lalu diringkas: bulan hidup terakhir, bulan mati pertama, bulan
HIDUP yang jatuh pada atau sesudah tebing, mati tersisip (bulan MATI yang diapit
HIDUP di kedua sisi), kebangkitan, rentetan terpanjang, dan lubang funding.

Modul ini DIAGNOSTIK: ia tidak menjatuhkan satu simbol-bulan pun dan tidak menulis
`funding_ada` di manifes mana pun.

## Penggugur (aturan 24)

`galat_kohort` bukan null, `kendali_sah` false, `penyebut_kehidupan` 0,
`cacah_kunci_gagal_pisah` > 0, `cacah_simbol_kohort` 0, atau `sidik_seragam` false
— masing-masing membatalkan seluruh angka laporan ini, dan masing-masing
menghasilkan kode keluar 2.

Kendali positif (aturan 50): BTCUSDT dan ETHUSDT wajib terbaca HIDUP pada bulan
yang diharapkan. Bila pasar yang pasti diperdagangkan pun terbaca tidak hidup,
yang cacat adalah pembacaan, bukan kohort.

## Praregistrasi R-302 (jurnal 122 §7, ditulis SEBELUM modul ini didorong)

Butir 1 `cacah_simbol_hidup_sesudah_tebing` == 0; butir 2
`cacah_simbol_mati_tersisip` >= 1; butir 3 `cacah_simbol_bangkit` == 0. Ketiganya
dipraregistrasi sebagai R-301 di jurnal 121 dan tidak pernah terlihat angkanya,
sehingga bunyinya dipakai ULANG tanpa perubahan (aturan 29).

Aturan yang mengikat modul ini: 10, 20, 21, 22, 24, 29, 41, 44, 46, 47, 50, 52,
71, 73, 74.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set, Tuple

from . import kehidupan, kehidupan_arsip, kohort_ekor, silang_funding

VERSI = 2
KELUARAN = "reports/bentangan_kohort.json"

# Diwarisi, tidak disalin (aturan 69).
TEBING = kohort_ekor.TEBING
BULAN_DIHARAPKAN = kohort_ekor.BULAN_DIHARAPKAN
KENDALI_HIDUP = kohort_ekor.KENDALI_HIDUP
MEDAN_LILIN = silang_funding.MEDAN_LILIN
SUMBER_FUNDING = silang_funding.SUMBER_FUNDING

# Angka terbitan STATE v30, dipakai sebagai pembanding, BUKAN masukan (aturan 21).
PENYEBUT_TERCATAT = 19586

# Tetapan praregistrasi. Nomor ramalannya berubah (R-301 tidak teradjudikasi karena
# laporannya tidak pernah ada), bunyinya TIDAK.
R301_BUTIR_1_HIDUP_SESUDAH_TEBING = 0
R301_BUTIR_2_MINIMAL_SATU_TERSISIP = 1
R301_BUTIR_3_BANGKIT = 0

BERKAS_DICAP = [
    "bentangan_kohort.py",
    "kehidupan_arsip.py",
    "kohort_ekor.py",
    "silang_funding.py",
]

POLA_BULAN = re.compile(r"^\d{4}-\d{2}$")
POLA_KUNCI = re.compile(r"^(?P<simbol>.+?)[\s|/_:.-]*(?P<bulan>\d{4}-\d{2})$")

Kunci = Tuple[str, str]


def sidik_kode() -> str:
    """Aturan 22: cap setiap berkas yang ikut menentukan angka laporan ini."""
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(BERKAS_DICAP):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def pisah_kunci(kunci: Any) -> Optional[Kunci]:
    """Kunci laporan kehidupan menjadi (simbol, bulan), atau None bila bukan kunci.

    Bentuk KANON adalah tuple `(simbol, bulan)` sebagaimana `silang_funding.Kunci`.
    Bentuk string tetap diterima agar laporan lain yang memakai kunci gabungan
    dapat dibaca, tetapi ia BUKAN bentuk yang diandalkan.
    """
    if isinstance(kunci, (tuple, list)):
        if len(kunci) != 2:
            return None
        simbol = str(kunci[0]).strip()
        bulan = str(kunci[1]).strip()
        if not simbol or not POLA_BULAN.match(bulan):
            return None
        return simbol, bulan
    if isinstance(kunci, str):
        cocok = POLA_KUNCI.match(kunci.strip())
        if not cocok:
            return None
        simbol = cocok.group("simbol").strip(" |/_:.-")
        if not simbol:
            return None
        return simbol, cocok.group("bulan")
    return None


def kelompokkan(status: Dict[Any, Any]) -> Tuple[Dict[str, Dict[str, str]], List[str]]:
    """Peta simbol -> {bulan: status}. Kunci yang gagal dipisah DILAPORKAN, bukan dibuang."""
    peta: Dict[str, Dict[str, str]] = {}
    gagal: List[str] = []
    for kunci, st in dict(status).items():
        pisah = pisah_kunci(kunci)
        if pisah is None:
            gagal.append(str(kunci))
            continue
        simbol, bulan = pisah
        peta.setdefault(simbol, {})[bulan] = str(st)
    return peta, sorted(gagal)


def bulan_berstatus(peta_bulan: Dict[str, str], status: str) -> List[str]:
    """Bulan-bulan bersatuan BULAN yang berstatus `status`, urut menaik."""
    return sorted(b for b, st in dict(peta_bulan).items() if str(st) == str(status))


def mati_tersisip(peta_bulan: Dict[str, str]) -> int:
    """Cacah bulan MATI yang diapit bulan HIDUP di KEDUA sisi.

    Tanpa bulan HIDUP sama sekali, jawabannya 0 dan itu bukan pernyataan tentang
    dunia melainkan tentang ketiadaan pengapit (aturan 74).
    """
    hidup = bulan_berstatus(peta_bulan, kehidupan.STATUS_HIDUP)
    if len(hidup) < 2:
        return 0
    awal, akhir = hidup[0], hidup[-1]
    return sum(
        1
        for b in bulan_berstatus(peta_bulan, kehidupan.STATUS_MATI)
        if awal < b < akhir
    )


def bangkit(peta_bulan: Dict[str, str]) -> bool:
    """Benar bila ada bulan HIDUP yang jatuh SESUDAH bulan MATI paling awal."""
    mati = bulan_berstatus(peta_bulan, kehidupan.STATUS_MATI)
    hidup = bulan_berstatus(peta_bulan, kehidupan.STATUS_HIDUP)
    return bool(mati) and bool(hidup) and hidup[-1] > mati[0]


def rentetan_terpanjang(bulan: Iterable[str]) -> int:
    """Rentetan bulan BERURUTAN KALENDER terpanjang; celah memutus rentetan."""
    urut = sorted({str(b) for b in bulan if b and POLA_BULAN.match(str(b))})
    terbaik = 0
    berjalan = 0
    sebelum: Optional[str] = None
    for b in urut:
        if sebelum is not None and kohort_ekor.mundur_bulan(b, 1) == sebelum:
            berjalan += 1
        else:
            berjalan = 1
        terbaik = max(terbaik, berjalan)
        sebelum = b
    return terbaik


def ringkas_simbol(
    simbol: str,
    peta_bulan: Dict[str, str],
    byte_parquet: Optional[Dict[Any, Any]] = None,
    lilin: Optional[Dict[Any, Any]] = None,
    bulan_berlubang: Optional[Iterable[str]] = None,
) -> Dict[str, Any]:
    """Ringkasan satu simbol. `byte_parquet` dan `lilin` berkunci TUPLE (simbol, bulan)."""
    byte_parquet = dict(byte_parquet or {})
    lilin = dict(lilin or {})
    berlubang = {str(b) for b in (bulan_berlubang or ())}
    bulan = sorted(dict(peta_bulan))
    hidup = bulan_berstatus(peta_bulan, kehidupan.STATUS_HIDUP)
    mati = bulan_berstatus(peta_bulan, kehidupan.STATUS_MATI)
    sepi = bulan_berstatus(peta_bulan, kehidupan.STATUS_SEPI)
    hidup_sesudah = [b for b in hidup if b >= TEBING]
    return {
        "simbol": simbol,
        "cacah_bulan": len(bulan),
        "bulan_pertama": bulan[0] if bulan else None,
        "bulan_terakhir": bulan[-1] if bulan else None,
        "cacah_hidup": len(hidup),
        "cacah_mati": len(mati),
        "cacah_sepi": len(sepi),
        "bulan_hidup_terakhir": hidup[-1] if hidup else None,
        "bulan_mati_pertama": mati[0] if mati else None,
        "cacah_hidup_sesudah_tebing": len(hidup_sesudah),
        "bulan_hidup_sesudah_tebing": hidup_sesudah,
        "cacah_mati_tersisip": mati_tersisip(peta_bulan),
        "bangkit": bangkit(peta_bulan),
        "rentetan_hidup_terpanjang": rentetan_terpanjang(hidup),
        "rentetan_mati_terpanjang": rentetan_terpanjang(mati),
        "cacah_bulan_berlubang_funding": len([b for b in bulan if b in berlubang]),
        "byte_parquet_total": sum(
            int(byte_parquet.get((simbol, b)) or 0) for b in bulan
        ),
        "cacah_lilin_total": sum(int(lilin.get((simbol, b)) or 0) for b in bulan),
        "bulan_terakhir_sama_diharapkan": (
            None if not bulan else bulan[-1] == BULAN_DIHARAPKAN
        ),
    }


def uji_r301(baris: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    """Adjudikasi mesin atas ketiga butir praregistrasi. Satuan tiap cacah: SIMBOL."""
    daftar = list(baris)
    hidup_sesudah = sum(
        1 for r in daftar if int(r.get("cacah_hidup_sesudah_tebing") or 0) > 0
    )
    tersisip = sum(1 for r in daftar if int(r.get("cacah_mati_tersisip") or 0) > 0)
    bangkit_kembali = sum(1 for r in daftar if r.get("bangkit"))
    butir_1 = hidup_sesudah == R301_BUTIR_1_HIDUP_SESUDAH_TEBING
    butir_2 = tersisip >= R301_BUTIR_2_MINIMAL_SATU_TERSISIP
    butir_3 = bangkit_kembali == R301_BUTIR_3_BANGKIT
    return {
        "penyebut_simbol": len(daftar),
        "cacah_simbol_hidup_sesudah_tebing": hidup_sesudah,
        "cacah_simbol_mati_tersisip": tersisip,
        "cacah_simbol_bangkit": bangkit_kembali,
        "butir_1": butir_1,
        "butir_2": butir_2,
        "butir_3": butir_3,
        "cacah_butir_menang": sum((butir_1, butir_2, butir_3)),
        "pembatal_a008_menyala": tersisip > 0,
    }


def kendali_positif(
    status: Dict[Any, Any], bulan: Optional[str] = None
) -> List[Dict[str, Any]]:
    """Aturan 50: simbol yang pasti diperdagangkan wajib terbaca HIDUP."""
    bulan_dipakai = bulan or BULAN_DIHARAPKAN
    peta = dict(status)
    hasil: List[Dict[str, Any]] = []
    for simbol in KENDALI_HIDUP:
        st = peta.get((simbol, bulan_dipakai))
        hasil.append(
            {
                "simbol": simbol,
                "bulan": bulan_dipakai,
                "status": None if st is None else str(st),
                "hidup": str(st) == kehidupan.STATUS_HIDUP,
            }
        )
    return hasil


def kendali_sah(kendali: Sequence[Dict[str, Any]]) -> bool:
    return bool(kendali) and all(bool(k.get("hidup")) for k in kendali)


def kode_keluar(laporan: Dict[str, Any]) -> int:
    """Kode 2 bila laporan ini tidak berhak diklaim sebagai pengukuran."""
    ringkasan = dict(laporan.get("ringkasan") or {})
    if laporan.get("galat_kohort"):
        return 2
    if not ringkasan.get("sidik_seragam"):
        return 2
    if not ringkasan.get("kendali_sah"):
        return 2
    if int(ringkasan.get("penyebut_kehidupan") or 0) <= 0:
        return 2
    if int(ringkasan.get("cacah_kunci_gagal_pisah") or 0) > 0:
        return 2
    if int(ringkasan.get("cacah_simbol_kohort") or 0) <= 0:
        return 2
    return 0


def jalankan(akar: str = ".", total: Optional[int] = None) -> Dict[str, Any]:
    jumlah = kehidupan_arsip.TOTAL_PECAHAN if total is None else int(total)
    status, byte_parquet, meta = silang_funding.baca_laporan_kehidupan(akar, jumlah)
    lilin, meta_lilin = silang_funding.baca_medan_baris(akar, jumlah, MEDAN_LILIN)

    kohort = kohort_ekor.muat_kohort(akar)
    anggota = sorted({str(s) for s in (kohort.get("simbol") or [])})

    lubang: Set[Kunci] = set()
    meta_lubang: Dict[str, Any] = {
        "cacah_lubang_funding": 0,
        "cacah_lubang_ganda": 0,
        "sumber_funding_ada": False,
    }
    jalur_funding = Path(akar) / SUMBER_FUNDING
    if jalur_funding.exists():
        funding = json.loads(jalur_funding.read_text(encoding="utf-8"))
        lubang, hitung = silang_funding.lubang_funding(funding)
        meta_lubang = dict(hitung)
        meta_lubang["sumber_funding_ada"] = True

    peta, gagal = kelompokkan(status)
    berlubang: Dict[str, Set[str]] = {}
    for kunci in lubang:
        pisah = pisah_kunci(kunci)
        if pisah is None:
            continue
        berlubang.setdefault(pisah[0], set()).add(pisah[1])

    baris = [
        ringkas_simbol(
            simbol, peta.get(simbol, {}), byte_parquet, lilin, berlubang.get(simbol, set())
        )
        for simbol in anggota
    ]
    tanpa_label = [r["simbol"] for r in baris if int(r.get("cacah_bulan") or 0) == 0]
    terlabel = [r for r in baris if int(r.get("cacah_bulan") or 0) > 0]

    kendali = kendali_positif(status)
    r301 = uji_r301(terlabel)

    ringkasan: Dict[str, Any] = {
        "versi_bentangan_kohort": VERSI,
        "penyebut_kehidupan": len(status),
        "selisih_penyebut": len(status) - PENYEBUT_TERCATAT,
        "cacah_simbol_kohort": len(anggota),
        "cacah_simbol_kohort_tanpa_label": len(tanpa_label),
        "simbol_kohort_tanpa_label": tanpa_label,
        "cacah_kunci_gagal_pisah": len(gagal),
        "cacah_simbol_dikelompokkan": len(peta),
        "bulan_tebing": TEBING,
        "bulan_diharapkan": BULAN_DIHARAPKAN,
        "kendali": kendali,
        "kendali_sah": kendali_sah(kendali),
        "r301": r301,
    }
    ringkasan.update(meta)
    ringkasan.update(meta_lilin)
    ringkasan.update(meta_lubang)

    return {
        "bukan_bukti": False,
        "versi_bentangan_kohort": VERSI,
        "sidik_kode": sidik_kode(),
        "sidik_kode_kohort_ekor": kohort_ekor.sidik_kode(),
        "sumber_kohort": kohort_ekor.SUMBER,
        "galat_kohort": kohort.get("galat"),
        "bulan_mulai_kohort": kohort.get("bulan_mulai"),
        "kunci_gagal_pisah_contoh": gagal[:10],
        "baris": baris,
        "ringkasan": ringkasan,
        "catatan_bukan_bukti": (
            "laporan ini diagnostik: ia TIDAK menjatuhkan simbol-bulan mana pun dan "
            "TIDAK menulis funding_ada di manifes mana pun"
        ),
        "catatan_kc43": (
            "V1 gugur karena memakai kembalian lubang_funding dan baca_medan_baris "
            "yang berbentuk PASANGAN sebagai dict, dan karena mengira kunci laporan "
            "kehidupan berupa string padahal ia tuple (simbol, bulan); nama fungsi "
            "bukan tanda tangan (KC-43)"
        ),
        "catatan_penggugur": (
            "galat_kohort bukan null, sidik_seragam false, kendali_sah false, "
            "penyebut_kehidupan 0, cacah_kunci_gagal_pisah > 0, atau "
            "cacah_simbol_kohort 0 masing-masing membatalkan SELURUH angka laporan "
            "ini dan menghasilkan kode keluar 2 (aturan 24)"
        ),
        "catatan_satuan": (
            "cacah_simbol_* bersatuan SIMBOL; cacah_bulan, cacah_hidup, cacah_mati, "
            "cacah_sepi, dan cacah_mati_tersisip bersatuan BULAN pada satu simbol; "
            "penyebut_kehidupan bersatuan SIMBOL-BULAN (aturan 47)"
        ),
        "catatan_rentang": (
            "hanya bulan yang ADA di penyebut kehidupan yang diukur; bulan di luar "
            "penyebut tidak diukur, jadi tidak ada pernyataan apa pun tentangnya "
            "(aturan 20), dan simbol tanpa label dicacah tersendiri, tidak dibaca "
            "sebagai nol (aturan 46, 74)"
        ),
        "catatan_nama_kohort": (
            "daftar nama anggota kohort TIDAK pernah menjadi tetapan modul ini; ia "
            "dibaca di runner lewat kohort_ekor.muat_kohort (aturan 73)"
        ),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def main() -> int:
    laporan = jalankan(".")
    Path(KELUARAN).parent.mkdir(parents=True, exist_ok=True)
    with open(KELUARAN, "w", encoding="utf-8") as f:
        json.dump(laporan, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(laporan["ringkasan"], ensure_ascii=False, indent=2, sort_keys=True))
    return kode_keluar(laporan)


if __name__ == "__main__":
    raise SystemExit(main())
