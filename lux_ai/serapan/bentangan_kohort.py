"""bentangan_kohort — V1.

Membentangkan status kehidupan per bulan untuk SELURUH anggota kohort ekor
(bukan sampel abjad 10 seperti `kohort_ekor` dengan BATAS_SIMBOL=10).

Aturan yang mengikat modul ini:

1.  Daftar anggota kohort TIDAK ditulis sebagai tetapan. Ia dibaca di runner
    lewat `kohort_ekor.muat_kohort(akar)`, yang mengambil `kohort_puncak.simbol`
    dari `reports/funding_semesta.json`. Agen tidak pernah membaca laporan itu
    secara utuh (terpotong 27%), sehingga menyalin namanya akan melanggar
    aturan 73.
2.  Penyebutnya adalah label kehidupan per simbol-bulan (19.586 yang lolos
    gerbang), BUKAN arsip. Simbol-bulan tanpa label dihitung sebagai
    TAK_TERUKUR, bukan nol (aturan 74).
3.  Format kunci laporan kehidupan tidak diasumsikan. Ia dideteksi dengan
    `pisah_kunci`, dan bila deteksi gagal untuk seluruh kunci modul keluar
    dengan kode 2 alih-alih melaporkan nol (aturan 46).
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

from lux_ai.serapan import kehidupan, kehidupan_arsip, kohort_ekor, silang_funding

VERSI = 1
KELUARAN = "reports/bentangan_kohort.json"
TEBING = kohort_ekor.TEBING
BULAN_DIHARAPKAN = kohort_ekor.BULAN_DIHARAPKAN
KENDALI_HIDUP = tuple(kohort_ekor.KENDALI_HIDUP)
MEDAN_LILIN = silang_funding.MEDAN_LILIN
BERKAS_DICAP = [
    "bentangan_kohort.py",
    "kohort_ekor.py",
    "kehidupan_arsip.py",
    "silang_funding.py",
]

# Praregistrasi R-301 (jurnal 121), ditulis sebelum modul ini ada.
R301_BUTIR_1_HIDUP_SESUDAH_TEBING = 0
R301_BUTIR_2_MINIMAL_SATU_TERSISIP = 1
R301_BUTIR_3_BANGKIT = 0

POLA_KUNCI = re.compile(r"^(?P<simbol>.+?)[\s|/_:.-]*(?P<bulan>\d{4}-\d{2})$")


def sidik_kode(akar: Path) -> str:
    """Sidik gabungan berkas kode yang membentuk laporan ini."""
    cerna = hashlib.sha256()
    for nama in sorted(BERKAS_DICAP):
        jalan = Path(akar) / "lux_ai" / "serapan" / nama
        cerna.update(nama.encode("utf-8"))
        cerna.update(jalan.read_bytes() if jalan.exists() else b"")
    return cerna.hexdigest()


def pisah_kunci(kunci: str):
    """Pisahkan kunci laporan kehidupan menjadi (simbol, bulan).

    Mengembalikan None bila kunci tidak berakhiran bulan YYYY-MM.
    """
    cocok = POLA_KUNCI.match(str(kunci))
    if not cocok:
        return None
    simbol = cocok.group("simbol").strip(" |/_:.-")
    if not simbol:
        return None
    return simbol, cocok.group("bulan")


def kelompokkan(status: dict):
    """Kelompokkan {kunci: status} menjadi {simbol: {bulan: status}}."""
    per_simbol: dict = {}
    gagal = 0
    for kunci, nilai in status.items():
        pecah = pisah_kunci(kunci)
        if pecah is None:
            gagal += 1
            continue
        simbol, bulan = pecah
        per_simbol.setdefault(simbol, {})[bulan] = nilai
    return per_simbol, gagal


def bulan_berstatus(peta: dict, dicari: str):
    """Daftar bulan terurut yang berstatus `dicari`."""
    return sorted(b for b, s in peta.items() if s == dicari)


def mati_tersisip(peta: dict) -> int:
    """Cacah bulan MATI yang diapit bulan HIDUP di kedua sisi.

    Sisipan dihitung atas urutan bulan yang ADA labelnya; bulan tanpa label
    memutus pengapitan karena ia TAK_TERUKUR, bukan MATI.
    """
    bulan = sorted(peta)
    cacah = 0
    for i in range(1, len(bulan) - 1):
        if peta[bulan[i]] != kehidupan.STATUS_MATI:
            continue
        sebelum = peta[bulan[i - 1]] == kehidupan.STATUS_HIDUP
        sesudah = peta[bulan[i + 1]] == kehidupan.STATUS_HIDUP
        if sebelum and sesudah:
            cacah += 1
    return cacah


def bangkit(peta: dict) -> bool:
    """True bila ada bulan HIDUP sesudah bulan MATI yang didahului HIDUP."""
    bulan = sorted(peta)
    pernah_hidup = False
    mati_sesudah_hidup = False
    for b in bulan:
        s = peta[b]
        if s == kehidupan.STATUS_HIDUP:
            if mati_sesudah_hidup:
                return True
            pernah_hidup = True
        elif s == kehidupan.STATUS_MATI and pernah_hidup:
            mati_sesudah_hidup = True
    return False


def rentetan_terpanjang(peta: dict, dicari: str) -> int:
    """Rentetan terpanjang bulan berurutan berstatus `dicari`."""
    terpanjang = 0
    berjalan = 0
    for b in sorted(peta):
        if peta[b] == dicari:
            berjalan += 1
            terpanjang = max(terpanjang, berjalan)
        else:
            berjalan = 0
    return terpanjang


def ringkas_simbol(simbol: str, peta: dict, byte_parquet: dict, lilin: dict, lubang: dict):
    """Bentangan satu simbol. `peta` boleh kosong (seluruhnya TAK_TERUKUR)."""
    bulan = sorted(peta)
    hidup = bulan_berstatus(peta, kehidupan.STATUS_HIDUP)
    mati = bulan_berstatus(peta, kehidupan.STATUS_MATI)
    sepi = bulan_berstatus(peta, kehidupan.STATUS_SEPI)
    tak = bulan_berstatus(peta, kehidupan.STATUS_TAK_TERUKUR)
    hidup_sesudah_tebing = [b for b in hidup if b >= TEBING]
    total_byte = 0
    for b in bulan:
        nilai = byte_parquet.get(f"{simbol}{b}") if byte_parquet else None
        if isinstance(nilai, (int, float)):
            total_byte += int(nilai)
    return {
        "simbol": simbol,
        "cacah_bulan_berlabel": len(bulan),
        "bulan_pertama": bulan[0] if bulan else None,
        "bulan_terakhir": bulan[-1] if bulan else None,
        "cacah_hidup": len(hidup),
        "cacah_mati": len(mati),
        "cacah_sepi": len(sepi),
        "cacah_tak_terukur": len(tak),
        "bulan_hidup_pertama": hidup[0] if hidup else None,
        "bulan_hidup_terakhir": hidup[-1] if hidup else None,
        "cacah_hidup_sesudah_tebing": len(hidup_sesudah_tebing),
        "bulan_hidup_sesudah_tebing": hidup_sesudah_tebing,
        "cacah_mati_tersisip": mati_tersisip(peta),
        "bangkit": bangkit(peta),
        "rentetan_hidup_terpanjang": rentetan_terpanjang(peta, kehidupan.STATUS_HIDUP),
        "rentetan_mati_terpanjang": rentetan_terpanjang(peta, kehidupan.STATUS_MATI),
        "byte_parquet_total": total_byte,
        "lubang_funding": sorted(lubang.get(simbol, [])) if lubang else [],
        "cacah_lilin_terukur": sum(
            1 for b in bulan if isinstance(lilin.get(f"{simbol}{b}"), (int, float))
        )
        if lilin
        else 0,
    }


def uji_r301(bentangan: list):
    """Adjudikasi ketiga butir R-301 atas seluruh anggota kohort."""
    hidup_sesudah = [b["simbol"] for b in bentangan if b["cacah_hidup_sesudah_tebing"] > 0]
    tersisip = [b["simbol"] for b in bentangan if b["cacah_mati_tersisip"] > 0]
    bangkit_nama = [b["simbol"] for b in bentangan if b["bangkit"]]
    butir_1 = len(hidup_sesudah) == R301_BUTIR_1_HIDUP_SESUDAH_TEBING
    butir_2 = len(tersisip) >= R301_BUTIR_2_MINIMAL_SATU_TERSISIP
    butir_3 = len(bangkit_nama) == R301_BUTIR_3_BANGKIT
    return {
        "butir_1": butir_1,
        "butir_2": butir_2,
        "butir_3": butir_3,
        "cacah_butir_menang": sum([butir_1, butir_2, butir_3]),
        "cacah_simbol_hidup_sesudah_tebing": len(hidup_sesudah),
        "simbol_hidup_sesudah_tebing": hidup_sesudah,
        "cacah_simbol_mati_tersisip": len(tersisip),
        "simbol_mati_tersisip": tersisip,
        "cacah_simbol_bangkit": len(bangkit_nama),
        "simbol_bangkit": bangkit_nama,
        "pembatal_a008_menyala": len(tersisip) > 0,
    }


def kendali_positif(per_simbol: dict):
    """Kendali positif: simbol kendali wajib HIDUP pada bulan ekor."""
    rinci = {}
    for simbol in KENDALI_HIDUP:
        peta = per_simbol.get(simbol, {})
        rinci[simbol] = peta.get(BULAN_DIHARAPKAN)
    sah = all(nilai == kehidupan.STATUS_HIDUP for nilai in rinci.values())
    return {"rinci": rinci, "kendali_sah": sah}


def kode_keluar(ringkasan: dict) -> int:
    """2 bila pengukuran tidak sah; 0 bila sah (menang atau kalah)."""
    if ringkasan.get("galat_kohort"):
        return 2
    if not ringkasan.get("kendali_sah"):
        return 2
    if ringkasan.get("penyebut_kehidupan", 0) <= 0:
        return 2
    if ringkasan.get("cacah_kunci_gagal_pisah", 0) > 0:
        return 2
    if ringkasan.get("cacah_simbol_kohort", 0) <= 0:
        return 2
    return 0


def jalankan(akar, total: int = None) -> dict:
    akar = Path(akar)
    total = kehidupan_arsip.TOTAL_PECAHAN if total is None else total

    kohort = kohort_ekor.muat_kohort(akar)
    galat_kohort = kohort.get("galat")
    simbol_kohort = list(kohort.get("simbol") or [])

    status, byte_parquet, meta = silang_funding.baca_laporan_kehidupan(akar, total)
    lilin = silang_funding.baca_medan_baris(akar, total, MEDAN_LILIN)

    sumber_funding = akar / silang_funding.SUMBER_FUNDING
    lubang = {}
    funding_ada = sumber_funding.exists()
    if funding_ada:
        with open(sumber_funding, encoding="utf-8") as f:
            lubang = silang_funding.lubang_funding(json.load(f))

    per_simbol, gagal_pisah = kelompokkan(status)
    bentangan = [
        ringkas_simbol(s, per_simbol.get(s, {}), byte_parquet, lilin, lubang)
        for s in sorted(simbol_kohort)
    ]
    kendali = kendali_positif(per_simbol)
    r301 = uji_r301(bentangan)

    ringkasan = {
        "penyebut_kehidupan": len(status),
        "cacah_simbol_kohort": len(simbol_kohort),
        "cacah_simbol_kohort_dilaporkan": kohort.get("cacah_simbol_kohort"),
        "bulan_mulai_kohort": kohort.get("bulan_mulai"),
        "galat_kohort": galat_kohort,
        "cacah_kunci_gagal_pisah": gagal_pisah,
        "cacah_simbol_semesta": len(per_simbol),
        "cacah_simbol_kohort_tanpa_label": sum(
            1 for b in bentangan if b["cacah_bulan_berlabel"] == 0
        ),
        "cacah_simbol_bulan_kohort": sum(b["cacah_bulan_berlabel"] for b in bentangan),
        "funding_ada": funding_ada,
        "kendali_sah": kendali["kendali_sah"],
        "kendali": kendali["rinci"],
        "sumber_kehidupan": meta if isinstance(meta, dict) else {},
    }

    laporan = {
        "versi_bentangan_kohort": VERSI,
        "tebing": TEBING,
        "ramalan": "R-301",
        "praregistrasi": "journal/2026-07-30-121.md",
        "ringkasan": ringkasan,
        "bentangan": bentangan,
        "r301": r301,
        "sidik_kode": sidik_kode(akar),
        "sidik_kode_silang_funding": silang_funding.sidik_kode(akar),
    }
    laporan["kode_keluar"] = kode_keluar(ringkasan)
    return laporan


def main() -> int:
    akar = Path(__file__).resolve().parents[2]
    laporan = jalankan(akar)
    keluaran = akar / KELUARAN
    keluaran.parent.mkdir(parents=True, exist_ok=True)
    with open(keluaran, "w", encoding="utf-8") as f:
        json.dump(laporan, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    r = laporan["r301"]
    print(
        "bentangan_kohort V{v}: {n} anggota kohort, {p} penyebut, "
        "butir menang {m}/3 (hidup sesudah tebing {h}, tersisip {t}, bangkit {b})".format(
            v=VERSI,
            n=laporan["ringkasan"]["cacah_simbol_kohort"],
            p=laporan["ringkasan"]["penyebut_kehidupan"],
            m=r["cacah_butir_menang"],
            h=r["cacah_simbol_hidup_sesudah_tebing"],
            t=r["cacah_simbol_mati_tersisip"],
            b=r["cacah_simbol_bangkit"],
        )
    )
    return laporan["kode_keluar"]


if __name__ == "__main__":
    sys.exit(main())
