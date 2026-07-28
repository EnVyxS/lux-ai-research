"""Serapan penuh berpecahan atas semesta tahap pertama (ADR-A005).

Semesta: 787 simbol `perpetual_usdt`, 19.598 simbol-bulan. Dibagi 8 pecahan
per ADR-A002 §9.

**Pembagian round-robin atas DAFTAR SIMBOL urut abjad** (`indeks % total`),
bukan potong blok dan bukan atas simbol-bulan:
- seluruh riwayat satu simbol selalu jatuh di pecahan yang sama, sehingga
  penggabungan tidak perlu melintasi pecahan;
- potong blok akan menumpuk simbol berawalan angka di pecahan 0 dan berawalan
  Z di pecahan 7, membuat umur dan ukuran berkas timpang. Itu pelajaran
  langsung dari KC-13.

**Daftar bulan DITANYAKAN ke arsip** lewat `arsip.bulan_tersedia`, tidak
diturunkan dari `bulan_pertama..bulan_terakhir`: `semesta_rentang.json` hanya
menyimpan ujung dan `cacah_bulan`, sehingga simbol yang pernah jeda akan
menghasilkan bulan hantu bila rentangnya sekadar dibentangkan. Pada pecahan 0
selisihnya nol untuk 99 simbol; itu tetap dilaporkan, tidak diasumsikan
(aturan 36).

**Parquet TIDAK dipersistenkan.** Ia ditulis, diukur, lalu dihapus. Aset rilis
GitHub berbatas 2 GB per berkas sementara satu pecahan ≈ 4,1 GB; bentuk
persistensi diputuskan ADR-A006. Yang di-commit hanya manifesnya.

**VERSI** dinaikkan setiap kali pecahan perlu dijalankan ulang. Pemicu-diri
workflow sudah dicabut (aturan 33), dan modul inilah satu-satunya pemicu run,
sehingga menaikkan VERSI adalah cara sengaja untuk menyalakannya.

Aturan yang ditegakkan: 18, 20, 24, 25, 28, 30, 32, 36, 37.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
from pathlib import Path
from typing import Any, Dict, List

from . import arsip, serap

VERSI = 2
SUMBER_RENTANG = serap.SUMBER_RENTANG
TOTAL_PECAHAN = 8
JENIS_DIIZINKAN = serap.JENIS_DIIZINKAN


def nama_keluaran(indeks: int) -> str:
    return f"reports/manifes_pecahan_{indeks}.json"


def sidik_kode() -> str:
    """Aturan 22: modul ini ditambah seluruh rantai yang dipakainya."""
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(
        ["pecahan.py", "serap.py", "arsip.py", "klines.py", "gerbang_1m.py", "resample.py"]
    ):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def simbol_pecahan(
    rentang: Dict[str, Any], jenis_dari, indeks: int, total: int = TOTAL_PECAHAN
) -> List[str]:
    """Simbol milik satu pecahan, round-robin atas daftar urut abjad."""
    if total <= 0:
        raise ValueError("total pecahan wajib positif")
    if not 0 <= indeks < total:
        raise ValueError(f"indeks pecahan {indeks} di luar 0..{total - 1}")
    layak = [
        s
        for s, isi in sorted(rentang.items())
        if isinstance(isi, dict) and jenis_dari(s) == JENIS_DIIZINKAN
    ]
    return [s for i, s in enumerate(layak) if i % total == indeks]


def jalankan(
    indeks: int, total: int = TOTAL_PECAHAN, akar: str = ".", hapus_parquet: bool = True
) -> Dict[str, Any]:
    from ..semesta import taksonomi

    basis = Path(akar)
    mentah = (basis / SUMBER_RENTANG).read_bytes()
    rentang = json.loads(mentah.decode("utf-8")).get("rentang", {})
    if not isinstance(rentang, dict):
        rentang = {}

    simbol = simbol_pecahan(rentang, taksonomi.jenis_instrumen, indeks, total)
    batas = int(os.environ.get("PECAHAN_BATAS_SIMBOL", "0") or 0)
    if batas > 0:
        simbol = simbol[:batas]

    manifes: List[Dict[str, Any]] = []
    selisih_bulan: List[Dict[str, Any]] = []
    gagal_daftar: List[str] = []

    for nama in simbol:
        isi = rentang.get(nama) or {}
        try:
            bulan = sorted(arsip.bulan_tersedia(nama))
        except Exception as exc:  # noqa: BLE001
            gagal_daftar.append(f"{nama}: {str(exc)[:120]}")
            continue

        diharap = isi.get("cacah_bulan")
        if isinstance(diharap, int) and diharap != len(bulan):
            selisih_bulan.append(
                {
                    "simbol": nama,
                    "cacah_bulan_rentang": diharap,
                    "cacah_bulan_arsip": len(bulan),
                }
            )

        mati = bool(str(isi.get("bulan_terakhir") or "") < serap.BATAS_HIDUP)
        for b in bulan:
            baris = serap.serap_satu(nama, b, akar=akar, terhenti=mati)
            if hapus_parquet and baris.get("parquet"):
                jalur = basis / str(baris["parquet"])
                if jalur.exists():
                    jalur.unlink()
            manifes.append(baris)

    laporan = serap.ringkas(manifes)
    laporan["bukan_bukti"] = False
    laporan["versi_pecahan"] = VERSI
    laporan["pecahan"] = {
        "indeks": indeks,
        "total": total,
        "cacah_simbol": len(simbol),
        "cacah_simbol_gagal_daftar": len(gagal_daftar),
        "contoh_gagal_daftar": gagal_daftar[:10],
    }
    laporan["selisih_cacah_bulan"] = {
        "cacah_simbol_berselisih": len(selisih_bulan),
        "contoh": selisih_bulan[:10],
        "catatan": (
            "daftar bulan diambil dari arsip; cacah_bulan di semesta_rentang.json "
            "berasal dari survei terdahulu. Selisih dicatat, tidak dibulatkan hilang "
            "(aturan 36)."
        ),
    }
    laporan["parquet_dipersistenkan"] = not hapus_parquet
    laporan["catatan_parquet"] = (
        "parquet ditulis, diukur, lalu dihapus; bentuk persistensi menunggu ADR-A006"
    )
    laporan["catatan_rentang"] = (
        f"hasil berlaku untuk pecahan {indeks} dari {total} saja, bukan untuk "
        "19.598 bulan perpetual_usdt (aturan 20)"
    )
    laporan["catatan_bulan_parsial"] = (
        "bulan pertama dan terakhir tiap simbol PARSIAL; rerata baris per bulan "
        "dilarang dikalikan begitu saja (aturan 28)"
    )
    laporan["manifes"] = [
        {k: v for k, v in b.items() if not k.startswith("_")} for b in manifes
    ]
    laporan["sumber_rentang"] = SUMBER_RENTANG
    laporan["sidik_data"] = hashlib.sha256(mentah).hexdigest()
    laporan["sidik_kode"] = sidik_kode()
    laporan["waktu_utc"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    tujuan = basis / nama_keluaran(indeks)
    tujuan.parent.mkdir(parents=True, exist_ok=True)
    tujuan.write_text(
        json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return laporan


def main() -> None:
    indeks = int(os.environ.get("PECAHAN_INDEKS", "0") or 0)
    total = int(os.environ.get("PECAHAN_TOTAL", str(TOTAL_PECAHAN)) or TOTAL_PECAHAN)
    hasil = jalankan(indeks, total)
    print(
        json.dumps(
            {k: v for k, v in hasil.items() if k != "manifes"},
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
