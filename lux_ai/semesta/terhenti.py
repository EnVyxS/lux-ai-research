"""Selisih dua definisi "simbol terhenti" (utang 28, aturan 36), penguraiannya
per KELAS INSTRUMEN (V2), penyebutan NAMA-nya (V3), dan sejak V4 PEMASANGAN nama
SETTLED dengan nama dasarnya (aturan 68).

`survei.py` menghitung terhenti sebagai `selisih_bulan(bulan_terakhir,
bulan_tutup) >= 2`, sedangkan `taksonomi.py` memakai `bulan_terakhir <
"2026-06"`. Keduanya memberi 128 lawan 129, dan aturan 36 melarang selisih itu
dibiarkan tanpa nama. V1 sudah menamainya: satu simbol, `SXPUSDT`, bulan terakhir
2026-05, dengan `hanya_survei` KOSONG.

V2 mengurai 129 terhenti dan 808 hidup ke sembilan kelas kanonik. V3 mendaftar
namanya, dan hasilnya menjatuhkan tafsir yang sudah dua kali dilemahkan:

- **R-275 MENANG.** `SXPUSDTSETTLED` adalah satu-satunya nama `sisa_settled` yang
  masih terbit, dengan `cacah_bulan` 1 dan bulan terakhir 2026-06. Ia menyatukan
  dua serpihan: `SXPUSDT` berhenti 2026-05, penggantinya mulai 2026-06. Maka
  selisih 128 lawan 129 bukan cacat pembukuan melainkan satu peristiwa penamaan
  yang sedang berlangsung.
- **R-276 MELESET TOTAL.** `cacah_peralihan_terhenti` = **0** dari 6. Keenam nama
  dasar H-A013 masih terbit pada bulan tutup, begitu pula `ICPUSDT`, `TLMUSDT`,
  dan `BNXUSDT`. Gagasan "peralihan nama" GUGUR seluruhnya; yang benar hanya
  bahwa nama SETTLED **MENAMBAH**, tidak **MENGGANTI** (aturan 68, KC-31).

V4 menguji sisa gagasan itu pada seluruh kelima belas nama SETTLED sekaligus,
bukan pada enam nama pilihan. Untuk setiap nama SETTLED ia mencari nama dasarnya
dan melaporkan bulan terakhir KEDUA nama berpasangan. Dua konvensi penamaan hidup
berdampingan — `ICPUSDT_SETTLED` bergaris bawah, empat belas lainnya tanpa — maka
kedua akhiran dibuang, yang terpanjang lebih dulu. Nama yang gagal dipasangkan
TIDAK dibuang diam-diam; ia dicacah di `cacah_dasar_tak_ada` dan tampak di
`pasangan_settled` dengan `dasar_ada` false (KC-13, aturan 59).

Taksonomi TIDAK diulang di sini; `jenis_instrumen` diimpor dari `taksonomi.py`
(pelajaran KC-29), dan `sidik_kode` mencap KEDUA berkas (aturan 22).
`selisih_bulan` tetap DISALIN dari `survei.py` agar modul ini tidak menarik paket
serapan; uji memaksa kedua salinan sepakat.

Ramalan yang dipraregistrasi SEBELUM run V4 — di `journal/2026-07-29-105.md`
(commit `6c99c350`) untuk R-278, dan di berkas ini untuk R-280:

- **R-278**: dari kelima belas nama `sisa_settled`, **13** punya nama dasar yang
  MASIH TERBIT dan **2** punya nama dasar yang sudah TERHENTI (`SXPUSDT`,
  `BDXNUSDT`); dan **≥11** nama SETTLED punya bulan terakhir yang MENDAHULUI bulan
  tutup. Gugur bila `cacah_dasar_tak_ada` > 0, sebab pemasangan yang gagal berarti
  konvensi nama yang belum saya pahami.
- **R-280**: cacah butir uji CI menjadi **638** (630 + 8 butir baru), kode 0.

Medan `r_275_menang`, `r_276_menang`, dan `r_278_menang` dilaporkan apa adanya dan
TIDAK dipakai sebagai penggugur laporan: laporan yang gugur ketika hipotesisnya
kalah akan menolak melahirkan angka yang membantah peramalnya.

Tidak menyentuh jaringan (aturan 13).
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from .taksonomi import JENIS, jenis_instrumen

VERSI = 4

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

# Angka terukur pada laporan V3 (blob e4f71ba8), dipatok agar perubahan senyap
# pada sumber terdeteksi, bukan untuk dipercaya buta.
CACAH_SIMBOL_TERCATAT = 937
TERHENTI_SURVEI_TERCATAT = 128
TERHENTI_TAKSONOMI_TERCATAT = 129
HIDUP_TERCATAT = 808
HIDUP_LUAR_PENYEBUT_TERCATAT = 49
PENYEBUT_RISET_TERCATAT = 787
TERHENTI_PENYEBUT_TERCATAT = 28
SETTLED_TERCATAT = 15
SETTLED_TERHENTI_TERCATAT = 14

# Keenam bulan peralihan H-A013. Tafsir "peralihan" sudah DICABUT oleh R-276;
# daftar ini tetap dilaporkan sebagai catatan sejarah, bukan sebagai dugaan.
PERALIHAN_H_A013 = (
    "CTKUSDT",
    "CVCUSDT",
    "CVXUSDT",
    "LITUSDT",
    "MAVIAUSDT",
    "SLPUSDT",
)

# Dua konvensi hidup berdampingan; yang TERPANJANG wajib diuji lebih dulu.
AKHIRAN_SETTLED = ("_SETTLED", "SETTLED")

# Batas R-275, dipatok di muka dan dilarang disetel sesudah melihat hasil (KC-1).
R275_BATAS_BULAN = 3

# Batas R-278, dipatok di muka pada jurnal 105.
R278_DASAR_HIDUP = 13
R278_DASAR_TERHENTI = 2
R278_MENDAHULUI_MIN = 11


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


def nama_dasar(simbol: str) -> Optional[str]:
    """Nama dasar sebuah nama SETTLED, atau None bila bukan nama SETTLED.

    Akhiran terpanjang diuji lebih dulu, sebab `ICPUSDT_SETTLED` juga berakhiran
    `SETTLED`. Sisa yang kosong dianggap GAGAL, bukan nama dasar kosong.
    """
    for akhiran in AKHIRAN_SETTLED:
        if simbol.endswith(akhiran):
            dasar = simbol[: -len(akhiran)]
            return dasar or None
    return None


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


def _kendali_pasangan_sah() -> bool:
    """Kendali positif bagi pemasangan (aturan 50), murni atas kode.

    Nama buatan wajib terpasang, dan nama biasa wajib TIDAK terpasang. Bila salah
    satu gagal, seluruh angka pemasangan tak boleh dipercaya.
    """
    return (
        nama_dasar(SIMBOL_KENDALI + "SETTLED") == SIMBOL_KENDALI
        and nama_dasar(SIMBOL_KENDALI + "_SETTLED") == SIMBOL_KENDALI
        and nama_dasar(SIMBOL_KENDALI) is None
    )


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
        "pasangan_settled": [],
        "cacah_settled": 0,
        "cacah_dasar_hidup": 0,
        "cacah_dasar_terhenti": 0,
        "cacah_dasar_tak_ada": 0,
        "cacah_settled_mendahului": 0,
        "identitas_pasangan_utuh": True,
        "definisi_dapat_dibedakan": False,
        "kendali": {
            "simbol": SIMBOL_KENDALI,
            "ada": False,
            "hidup": False,
            "jenis": None,
        },
        "kendali_sah": False,
        "kendali_pasangan_sah": _kendali_pasangan_sah(),
        "r_272_menang": False,
        "r_273_menang": False,
        "r_275_menang": False,
        "r_276_menang": False,
        "r_278_menang": False,
    }


def bandingkan(rentang: Dict[str, Any]) -> Dict[str, Any]:
    """Bandingkan kedua definisi, urai per kelas, sebut namanya, pasangkan SETTLED."""
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
    settled_semua: List[str] = []

    for simbol in sorted(sah):
        jenis = jenis_instrumen(simbol)
        cacah_per_jenis[jenis] += 1
        if jenis == "sisa_settled":
            settled_semua.append(simbol)
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

    # Aturan 68: bulan terakhir nama turunan dan nama asal WAJIB berpasangan.
    pasangan: List[Dict[str, Any]] = []
    dasar_hidup = 0
    dasar_terhenti = 0
    dasar_tak_ada = 0
    settled_mendahului = 0
    for simbol in settled_semua:
        dasar = nama_dasar(simbol)
        ada = bool(dasar is not None and dasar in sah)
        hidup = bool(ada and dasar not in set_taksonomi)
        if not ada:
            dasar_tak_ada += 1
        elif hidup:
            dasar_hidup += 1
        else:
            dasar_terhenti += 1
        mendahului = sah[simbol] < acuan
        if mendahului:
            settled_mendahului += 1
        pasangan.append(
            {
                "settled": simbol,
                "dasar": dasar,
                "dasar_ada": ada,
                "dasar_hidup": hidup,
                "bulan_terakhir_settled": sah[simbol],
                "bulan_terakhir_dasar": sah[dasar] if ada and dasar else None,
                "cacah_bulan_settled": cacah_bulan.get(simbol),
                "settled_mendahului_tutup": mendahului,
            }
        )

    identitas_pasangan = len(settled_semua) == dasar_hidup + dasar_terhenti + dasar_tak_ada

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
    r278 = bool(
        dasar_tak_ada == 0
        and dasar_hidup == R278_DASAR_HIDUP
        and dasar_terhenti == R278_DASAR_TERHENTI
        and settled_mendahului >= R278_MENDAHULUI_MIN
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
        "pasangan_settled": pasangan[:BATAS_NAMA],
        "cacah_settled": len(settled_semua),
        "cacah_dasar_hidup": dasar_hidup,
        "cacah_dasar_terhenti": dasar_terhenti,
        "cacah_dasar_tak_ada": dasar_tak_ada,
        "cacah_settled_mendahului": settled_mendahului,
        "identitas_pasangan_utuh": identitas_pasangan,
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
        "kendali_pasangan_sah": _kendali_pasangan_sah(),
        "r_272_menang": r272,
        "r_273_menang": r273,
        "r_275_menang": r275,
        "r_276_menang": r276,
        "r_278_menang": r278,
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
