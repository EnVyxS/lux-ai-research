"""Selisih dua definisi "simbol terhenti" (utang 28, aturan 36), dan sejak V2
penguraiannya per KELAS INSTRUMEN (aturan 66, aturan 67).

`survei.py` menghitung terhenti sebagai `selisih_bulan(bulan_terakhir,
bulan_tutup) >= 2`, sedangkan `taksonomi.py` memakai `bulan_terakhir <
"2026-06"`. Keduanya memberi angka berbeda (128 lawan 129), dan aturan 36
melarang selisih itu dibiarkan tanpa nama. V1 sudah menamainya: satu simbol,
`SXPUSDT`, bulan terakhir 2026-05, dengan `hanya_survei` KOSONG.

V2 menjawab pertanyaan yang berbeda dan lebih tajam. Laporan V1 memberi
`cacah_hidup` 808 atas penyebut 937, sedangkan semesta riset hanya 787 nama
`perpetual_usdt`. Karena 808 > 787, sekurangnya 21 nama yang MASIH TERBIT berada
DI LUAR semesta riset. Itu membantah kebiasaan lama saya menyamakan "di luar
penyebut" dengan "sudah mati" (aturan 67), dan V1 tidak dapat menunjukkan nama
maupun kelasnya. V2 menguraikan terhenti dan hidup ke sembilan kelas kanonik,
lalu menyebut nama contoh yang hidup di luar penyebut.

Taksonomi TIDAK diulang di sini. `jenis_instrumen` diimpor dari
`lux_ai/semesta/taksonomi.py`, sebab KC-29 lahir justru karena sebuah modul
mengarang klasifikasinya sendiri padahal taksonomi kanonik sudah ada. Sebagai
akibatnya `sidik_kode` V2 mencap KEDUA berkas (aturan 22): laporan yang isinya
ditentukan dua berkas tetapi hanya mencap satu adalah lubang yang tak akan
menyala sampai seseorang mengubah berkas yang tak tercap.

`selisih_bulan` tetap DISALIN dari `survei.py`, bukan diimpor, agar modul ini
tidak menarik paket serapan. Uji `test_terhenti.py` memaksa kedua salinan
sepakat.

Ramalan yang dipraregistrasi di `journal/2026-07-29-103.md` SEBELUM modul ini
ditulis, dan medannya disediakan di sini agar adjudikasinya mekanis:

- **R-272**: `perpetual_busd` terhenti 41 dari 41, dan `sisa_settled` 15 dari 15.
- **R-273**: `perpetual_usdt` terhenti berada di rentang 40..80.
- **R-274**: cacah butir uji CI menjadi **623** (610 + 13 butir baru), kode 0.

Medan `r_272_menang` dan `r_273_menang` dilaporkan apa adanya dan TIDAK dipakai
sebagai penggugur: laporan yang gugur ketika hipotesisnya kalah akan menolak
melahirkan angka yang membantah peramalnya.

Tidak menyentuh jaringan (aturan 13).
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

from .taksonomi import JENIS, jenis_instrumen

VERSI = 2

SUMBER = "reports/semesta_rentang.json"
KELUARAN = "reports/terhenti_semesta.json"

# Nilai yang dipakai survei.py saat laporan 128/809 dibuat.
JEDA_MATI_BULAN = 2

# Berapa bulan terakhir yang cacahnya dilaporkan walau nol (aturan 24).
EKOR_BULAN = 4

BATAS_CONTOH = 20

# Aturan 22 dan pelajaran KC-29: setiap berkas yang ikut menentukan isi laporan
# wajib dicap, termasuk berkas modul lain dalam paket yang sama.
BERKAS_DICAP = ("taksonomi.py", "terhenti.py")

# Kendali positif (aturan 50). BTCUSDT wajib ada, wajib HIDUP, dan wajib
# tergolong jenis penyebut; bila tidak, pengukurannya tidak boleh dipercaya.
SIMBOL_KENDALI = "BTCUSDT"
JENIS_PENYEBUT = "perpetual_usdt"

# Angka yang sudah terukur pada laporan V1 (blob 609160a3). Dipatok agar
# perubahan senyap pada sumber terdeteksi, bukan untuk dipercaya buta.
CACAH_SIMBOL_TERCATAT = 937
TERHENTI_SURVEI_TERCATAT = 128
TERHENTI_TAKSONOMI_TERCATAT = 129
HIDUP_TERCATAT = 808
PENYEBUT_RISET_TERCATAT = 787

# Batas rentang R-273, dipatok di muka dan dilarang disetel sesudah melihat
# hasil (KC-1).
R273_BAWAH = 40
R273_ATAS = 80


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


def _laporan_kosong(entri_dibaca: int) -> Dict[str, Any]:
    """Bentuk laporan saat tak ada entri sah; medannya HARUS lengkap.

    Laporan yang kehilangan medan ketika penyebutnya nol membuat pembacanya
    menyangka medan itu tak pernah ada (aturan 18, 24).
    """
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
        "identitas_per_jenis_utuh": True,
        "jenis_tanpa_anggota": sorted(JENIS),
        "cacah_hidup": 0,
        "cacah_hidup_luar_penyebut": 0,
        "contoh_hidup_luar_penyebut": [],
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
    }


def bandingkan(rentang: Dict[str, Any]) -> Dict[str, Any]:
    """Bandingkan kedua definisi, lalu urai hasilnya per kelas instrumen."""
    sah = {
        simbol: isi["bulan_terakhir"]
        for simbol, isi in rentang.items()
        if isinstance(isi, dict) and isinstance(isi.get("bulan_terakhir"), str)
    }
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
    hidup_luar: List[str] = []

    for simbol in sorted(sah):
        jenis = jenis_instrumen(simbol)
        cacah_per_jenis[jenis] += 1
        if simbol in set_taksonomi:
            terhenti_per_jenis[jenis] += 1
        else:
            hidup_per_jenis[jenis] += 1
            if jenis != JENIS_PENYEBUT:
                hidup_luar.append(simbol)

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
    r273 = bool(R273_BAWAH <= terhenti_per_jenis[JENIS_PENYEBUT] <= R273_ATAS)

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
        "identitas_per_jenis_utuh": identitas,
        "jenis_tanpa_anggota": sorted(j for j in JENIS if cacah_per_jenis[j] == 0),
        "cacah_hidup": cacah_hidup,
        "cacah_hidup_luar_penyebut": len(hidup_luar),
        "contoh_hidup_luar_penyebut": hidup_luar[:BATAS_CONTOH],
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
