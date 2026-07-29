"""Selisih dua definisi "simbol terhenti" (utang 28, aturan 36), penguraiannya
per KELAS INSTRUMEN (V2), dan sejak V3 penyebutan NAMA-nya (aturan 16, 27).

`survei.py` menghitung terhenti sebagai `selisih_bulan(bulan_terakhir,
bulan_tutup) >= 2`, sedangkan `taksonomi.py` memakai `bulan_terakhir <
"2026-06"`. Keduanya memberi 128 lawan 129, dan aturan 36 melarang selisih itu
dibiarkan tanpa nama. V1 sudah menamainya: satu simbol, `SXPUSDT`, bulan terakhir
2026-05, dengan `hanya_survei` KOSONG.

V2 mengurai 129 terhenti dan 808 hidup ke sembilan kelas kanonik. Hasilnya
menggugurkan dua ramalan sekaligus dan melahirkan dua pertanyaan yang hanya bisa
dijawab dengan NAMA, bukan cacah:

1. `sisa_settled` terhenti **14 dari 15**. Satu nama berakhiran SETTLED masih
   terbit pada bulan tutup semesta. V2 tidak dapat menunjukkan namanya, sebab
   `contoh_hidup_luar_penyebut` hanya memuat 20 nama pertama menurut abjad dan
   berhenti di `DOGEUSDC`. Bila nama SETTLED bisa masih terbit, maka `SETTLED`
   bukan penanda "kontrak sudah berakhir" melainkan penanda penamaan — yang
   memperkuat KC-18.
2. Dari 787 nama penyebut, **28** berhenti terbit. Apakah keenam nama peralihan
   H-A013 termasuk di dalamnya? Bila TIDAK, nama lama dan nama SETTLED pernah
   terbit bersamaan, dan gagasan "peralihan nama" wajib dilemahkan.

Maka V3 mendaftar nama, dengan batas yang cukup memuat seluruh kelas kecil
(`futures_kedaluwarsa` terbesar dengan 44 terhenti, dan 49 nama hidup di luar
penyebut; `BATAS_NAMA` 60 memuat keduanya utuh). Daftar yang terpotong WAJIB
menampakkan cacah penuhnya di medan terpisah, sebab daftar terpotong yang
menyamar sebagai daftar utuh adalah cacat yang tak menyala (KC-13).

Taksonomi TIDAK diulang di sini; `jenis_instrumen` diimpor dari `taksonomi.py`
(pelajaran KC-29), dan `sidik_kode` mencap KEDUA berkas (aturan 22).
`selisih_bulan` tetap DISALIN dari `survei.py` agar modul ini tidak menarik paket
serapan; uji memaksa kedua salinan sepakat.

Ramalan yang dipraregistrasi di `journal/2026-07-29-104.md` (commit `9a6b6e65`)
SEBELUM berkas ini ditulis:

- **R-275**: nama `sisa_settled` yang hidup punya `bulan_terakhir` = bulan tutup
  DAN `cacah_bulan` ≤ 3. Gugur bila `cacah_bulan` > 3.
- **R-276**: keenam nama peralihan H-A013 SELURUHNYA ada di dalam 28 nama
  `perpetual_usdt` yang terhenti. Gugur bila satu pun masih terbit.
- **R-277**: cacah butir uji CI menjadi **630** (623 + 7 butir baru), kode 0.

Medan `r_275_menang` dan `r_276_menang` dilaporkan apa adanya dan TIDAK dipakai
sebagai penggugur laporan: laporan yang gugur ketika hipotesisnya kalah akan
menolak melahirkan angka yang membantah peramalnya.

Tidak menyentuh jaringan (aturan 13).
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

from .taksonomi import JENIS, jenis_instrumen

VERSI = 3

SUMBER = "reports/semesta_rentang.json"
KELUARAN = "reports/terhenti_semesta.json"

# Nilai yang dipakai survei.py saat laporan 128/809 dibuat.
JEDA_MATI_BULAN = 2

# Berapa bulan terakhir yang cacahnya dilaporkan walau nol (aturan 24).
EKOR_BULAN = 4

BATAS_CONTOH = 20

# Cukup memuat kelas terbesar secara utuh: 44 terhenti dan 49 hidup luar
# penyebut. Bila kelak sebuah daftar melampauinya, cacah penuh tetap dilaporkan.
BATAS_NAMA = 60

# Aturan 22 dan pelajaran KC-29.
BERKAS_DICAP = ("taksonomi.py", "terhenti.py")

# Kendali positif (aturan 50).
SIMBOL_KENDALI = "BTCUSDT"
JENIS_PENYEBUT = "perpetual_usdt"

# Angka terukur pada laporan V2 (blob d4a6863d), dipatok agar perubahan senyap
# pada sumber terdeteksi, bukan untuk dipercaya buta.
CACAH_SIMBOL_TERCATAT = 937
TERHENTI_SURVEI_TERCATAT = 128
TERHENTI_TAKSONOMI_TERCATAT = 129
HIDUP_TERCATAT = 808
HIDUP_LUAR_PENYEBUT_TERCATAT = 49
PENYEBUT_RISET_TERCATAT = 787
TERHENTI_PENYEBUT_TERCATAT = 28

# Keenam bulan peralihan H-A013 (MENANG 6-0). Nama tanpa akhiran SETTLED.
PERALIHAN_H_A013 = (
    "CTKUSDT",
    "CVCUSDT",
    "CVXUSDT",
    "LITUSDT",
    "MAVIAUSDT",
    "SLPUSDT",
)

# Batas R-275, dipatok di muka dan dilarang disetel sesudah melihat hasil (KC-1).
R275_BATAS_BULAN = 3


def sidik_kode() -> str:
    """sha256 gabungan seluruh berkas yang menentukan isi laporan (aturan 22)."""
    h = hashlib.sha256()
    for nama in sorted(BERKAS_DICAP):
        h.update((Path(__file__).parent / nama).read_bytes())
    return h.hexdigest()


def sidik_data(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _pecah(bulan: str) -> Tuple[int, int]:
    tahun, bln = bulan.split("-")
    return int(tahun), int(bln)


def selisih_bulan(lebih_tua: str, acuan: str) -> int:
    """Berapa bulan `lebih_tua` tertinggal di belakang `acuan`.

    DISALIN dari `lux_ai/serapan/survei.py`. Bila salinan ini menyimpang, uji
    kesepakatan akan pecah.
    """
    ta, ba = _pecah(lebih_tua)
    tb, bb = _pecah(acuan)
    return (tb - ta) * 12 + (bb - ba)


def mundur_bulan(bulan: str, langkah: int) -> str:
    """Bulan YYYY-MM sekian langkah sebelum `bulan`."""
    tahun, bln = _pecah(bulan)
    total = tahun * 12 + (bln - 1) - langkah
    return f"{total // 12:04d}-{total % 12 + 1:02d}"


def terhenti_survei(bulan_terakhir: str, acuan: str, jeda: int = JEDA_MATI_BULAN) -> bool:
    return selisih_bulan(bulan_terakhir, acuan) >= jeda


def terhenti_taksonomi(bulan_terakhir: str, acuan: str) -> bool:
    return bulan_terakhir < acuan


def _kosong_per_jenis() -> Dict[str, int]:
    """Peta kesembilan kelas kanonik bernilai nol (aturan 18: nol dilaporkan)."""
    return {nama: 0 for nama in JENIS}


def _kosong_nama_per_jenis() -> Dict[str, List[str]]:
    return {nama: [] for nama in JENIS}


def _peralihan_kosong() -> Dict[str, Dict[str, Any]]:
    """Keenam nama peralihan selalu dilaporkan, walau tak satu pun hadir.

    Nama yang hilang dari sumber TIDAK boleh terbaca sebagai nama yang terhenti
    (aturan 59: ketiadaan pengukuran bukan ketiadaan gejala).
    """
    return {
        simbol: {"ada": False, "terhenti": False, "bulan_terakhir": None}
        for simbol in PERALIHAN_H_A013
    }


def _laporan_kosong(entri_dibaca: int) -> Dict[str, Any]:
    """Bentuk laporan saat tak ada entri sah; medannya HARUS lengkap."""
    return {
        "versi_terhenti": VERSI,
        "bukan_bukti": True,
        "status": "TIDAK MENGUKUR",
        "penyebut": {"entri_dibaca": entri_dibaca, "cacah_simbol": 0},
        "bulan_tutup_terakhir": None,
        "jeda_mati_bulan": JEDA_MATI_BULAN,
        "ambang_survei": None,
        "ambang_taksonomi": None,
        "cacah_terhenti_survei": 0,
        "cacah_terhenti_taksonomi": 0,
        "cacah_hanya_taksonomi": 0,
        "cacah_hanya_survei": 0,
        "hanya_taksonomi": [],
        "hanya_survei": [],
        "rincian_selisih": [],
        "cacah_per_bulan_terakhir_ekor": {},
        "cacah_per_jenis": _kosong_per_jenis(),
        "terhenti_per_jenis": _kosong_per_jenis(),
        "hidup_per_jenis": _kosong_per_jenis(),
        "nama_terhenti_per_jenis": _kosong_nama_per_jenis(),
        "daftar_nama_terpotong": False,
        "identitas_per_jenis_utuh": True,
        "jenis_tanpa_anggota": sorted(JENIS),
        "cacah_hidup": 0,
        "cacah_hidup_luar_penyebut": 0,
        "contoh_hidup_luar_penyebut": [],
        "nama_hidup_luar_penyebut": [],
        "settled_hidup": [],
        "peralihan_h_a013": _peralihan_kosong(),
        "cacah_peralihan_terhenti": 0,
        "definisi_dapat_dibedakan": False,
        "kendali": {
            "simbol": SIMBOL_KENDALI,
            "ada": False,
            "hidup": False,
            "jenis": None,
        },
        "kendali_sah": False,
        "r_272_menang": False,
        "r_273_menang": False,
        "r_275_menang": False,
        "r_276_menang": False,
    }


def bandingkan(rentang: Dict[str, Any]) -> Dict[str, Any]:
    """Bandingkan kedua definisi, urai per kelas, lalu sebut namanya."""
    sah: Dict[str, str] = {}
    cacah_bulan: Dict[str, Any] = {}
    for simbol, isi in rentang.items():
        if isinstance(isi, dict) and isinstance(isi.get("bulan_terakhir"), str):
            sah[simbol] = isi["bulan_terakhir"]
            nilai = isi.get("cacah_bulan")
            cacah_bulan[simbol] = nilai if isinstance(nilai, int) else None
    if not sah:
        return _laporan_kosong(len(rentang))

    acuan = max(sah.values())

    set_survei = {s for s, b in sah.items() if terhenti_survei(b, acuan)}
    set_taksonomi = {s for s, b in sah.items() if terhenti_taksonomi(b, acuan)}

    hanya_taksonomi = sorted(set_taksonomi - set_survei)
    hanya_survei = sorted(set_survei - set_taksonomi)

    cacah_per_jenis = _kosong_per_jenis()
    terhenti_per_jenis = _kosong_per_jenis()
    hidup_per_jenis = _kosong_per_jenis()
    nama_terhenti: Dict[str, List[str]] = _kosong_nama_per_jenis()
    hidup_luar: List[str] = []
    settled_hidup: List[Dict[str, Any]] = []

    for simbol in sorted(sah):
        jenis = jenis_instrumen(simbol)
        cacah_per_jenis[jenis] += 1
        if simbol in set_taksonomi:
            terhenti_per_jenis[jenis] += 1
            nama_terhenti[jenis].append(simbol)
        else:
            hidup_per_jenis[jenis] += 1
            if jenis != JENIS_PENYEBUT:
                hidup_luar.append(simbol)
            if jenis == "sisa_settled":
                settled_hidup.append(
                    {
                        "simbol": simbol,
                        "bulan_terakhir": sah[simbol],
                        "cacah_bulan": cacah_bulan.get(simbol),
                    }
                )

    terpotong = any(len(v) > BATAS_NAMA for v in nama_terhenti.values()) or len(
        hidup_luar
    ) > BATAS_NAMA
    nama_terhenti_dipotong = {j: v[:BATAS_NAMA] for j, v in nama_terhenti.items()}

    peralihan = _peralihan_kosong()
    for simbol in PERALIHAN_H_A013:
        if simbol in sah:
            peralihan[simbol] = {
                "ada": True,
                "terhenti": simbol in set_taksonomi,
                "bulan_terakhir": sah[simbol],
            }
    cacah_peralihan_terhenti = sum(1 for v in peralihan.values() if v["terhenti"])

    cacah_hidup = len(sah) - len(set_taksonomi)
    identitas = all(
        cacah_per_jenis[j] == terhenti_per_jenis[j] + hidup_per_jenis[j] for j in JENIS
    )

    ekor: Dict[str, int] = {}
    for langkah in range(EKOR_BULAN):
        bulan = mundur_bulan(acuan, langkah)
        ekor[bulan] = sum(1 for b in sah.values() if b == bulan)

    rincian: List[Dict[str, str]] = [
        {"simbol": s, "bulan_terakhir": sah[s]}
        for s in (hanya_taksonomi + hanya_survei)[:BATAS_CONTOH]
    ]

    kendali_ada = SIMBOL_KENDALI in sah
    kendali_hidup = bool(kendali_ada and SIMBOL_KENDALI not in set_taksonomi)
    kendali_jenis = jenis_instrumen(SIMBOL_KENDALI) if kendali_ada else None
    kendali_sah = bool(kendali_ada and kendali_hidup and kendali_jenis == JENIS_PENYEBUT)

    r272 = bool(
        cacah_per_jenis["perpetual_busd"] > 0
        and cacah_per_jenis["sisa_settled"] > 0
        and terhenti_per_jenis["perpetual_busd"] == cacah_per_jenis["perpetual_busd"]
        and terhenti_per_jenis["sisa_settled"] == cacah_per_jenis["sisa_settled"]
    )
    r273 = bool(40 <= terhenti_per_jenis[JENIS_PENYEBUT] <= 80)
    r275 = bool(
        settled_hidup
        and all(
            item["bulan_terakhir"] == acuan
            and isinstance(item["cacah_bulan"], int)
            and item["cacah_bulan"] <= R275_BATAS_BULAN
            for item in settled_hidup
        )
    )
    r276 = bool(
        all(v["ada"] for v in peralihan.values())
        and cacah_peralihan_terhenti == len(PERALIHAN_H_A013)
    )

    return {
        "versi_terhenti": VERSI,
        "bukan_bukti": True,
        "status": "TERUKUR",
        "penyebut": {"entri_dibaca": len(rentang), "cacah_simbol": len(sah)},
        "bulan_tutup_terakhir": acuan,
        "jeda_mati_bulan": JEDA_MATI_BULAN,
        "ambang_survei": mundur_bulan(acuan, JEDA_MATI_BULAN),
        "ambang_taksonomi": mundur_bulan(acuan, 1),
        "cacah_terhenti_survei": len(set_survei),
        "cacah_terhenti_taksonomi": len(set_taksonomi),
        "cacah_hanya_taksonomi": len(hanya_taksonomi),
        "cacah_hanya_survei": len(hanya_survei),
        "hanya_taksonomi": hanya_taksonomi[:BATAS_CONTOH],
        "hanya_survei": hanya_survei[:BATAS_CONTOH],
        "rincian_selisih": rincian,
        "cacah_per_bulan_terakhir_ekor": ekor,
        "cacah_per_jenis": cacah_per_jenis,
        "terhenti_per_jenis": terhenti_per_jenis,
        "hidup_per_jenis": hidup_per_jenis,
        "nama_terhenti_per_jenis": nama_terhenti_dipotong,
        "daftar_nama_terpotong": terpotong,
        "identitas_per_jenis_utuh": identitas,
        "jenis_tanpa_anggota": sorted(j for j in JENIS if cacah_per_jenis[j] == 0),
        "cacah_hidup": cacah_hidup,
        "cacah_hidup_luar_penyebut": len(hidup_luar),
        "contoh_hidup_luar_penyebut": hidup_luar[:BATAS_CONTOH],
        "nama_hidup_luar_penyebut": hidup_luar[:BATAS_NAMA],
        "settled_hidup": settled_hidup,
        "peralihan_h_a013": peralihan,
        "cacah_peralihan_terhenti": cacah_peralihan_terhenti,
        "definisi_dapat_dibedakan": bool(
            len(set_survei) != len(set_taksonomi) or hanya_taksonomi or hanya_survei
        ),
        "kendali": {
            "simbol": SIMBOL_KENDALI,
            "ada": kendali_ada,
            "hidup": kendali_hidup,
            "jenis": kendali_jenis,
        },
        "kendali_sah": kendali_sah,
        "r_272_menang": r272,
        "r_273_menang": r273,
        "r_275_menang": r275,
        "r_276_menang": r276,
    }


def jalankan(akar: str = ".") -> Dict[str, Any]:
    basis = Path(akar)
    mentah = (basis / SUMBER).read_bytes()
    muatan = json.loads(mentah.decode("utf-8"))
    rentang = muatan.get("rentang", {})
    if not isinstance(rentang, dict):
        rentang = {}

    laporan = bandingkan(rentang)
    laporan["sumber"] = SUMBER
    laporan["sumber_byte"] = len(mentah)
    laporan["sumber_bersidik"] = "sidik_kode" in muatan
    laporan["berkas_dicap"] = sorted(BERKAS_DICAP)
    laporan["sidik_data"] = sidik_data(mentah)
    laporan["sidik_kode"] = sidik_kode()

    tujuan = basis / KELUARAN
    tujuan.parent.mkdir(parents=True, exist_ok=True)
    tujuan.write_text(
        json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return laporan


def main() -> None:
    print(json.dumps(jalankan(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
