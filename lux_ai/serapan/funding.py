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

Laporan ini **diagnostik** (`bukan_bukti: true`, aturan 10). Ia tidak mengubah
satu baris pun manifes serapan.

Aturan yang ditegakkan: 7, 10, 16, 20, 22, 24, 30, 32, 36, 37, 41, 44, 46.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import io
import json
import os
import zipfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

from . import arsip

VERSI = 1
SUMBER_RENTANG = "reports/semesta_rentang.json"
KELUARAN = "reports/funding_semesta.json"
JENIS_DIIZINKAN = "perpetual_usdt"

# Diulang dari serap.py dengan sadar; lihat butir 4 di docstring.
BATAS_HEADER = "2022-01"
BATAS_BARU = "2025-01"
BATAS_HIDUP = "2026-05"
BATAS_DAFTAR = 500

# Kelas yang dapat ditentukan SEBELUM mengunduh. `pra_header` tidak masuk sini:
# ia hanya diketahui setelah berkasnya dibaca, dan menebaknya dari bulan akan
# mencampur dugaan dengan ukuran (aturan 16).
KELAS_PRA_UNDUH = ("bulan_awal_2020_2021", "non_ascii", "terhenti", "kendali_baru")
KELAS_RISIKO = ("pra_header",) + KELAS_PRA_UNDUH


def nama_keluaran() -> str:
    return KELUARAN


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


def ringkas_selisih(
    per_simbol: List[Dict[str, Any]], batas: int = BATAS_DAFTAR
) -> Dict[str, Any]:
    """Cacah kedua arah selisih; daftarnya dipotong dan pemotongannya dilapor."""
    ktf: List[str] = []
    ftk: List[str] = []
    for baris in per_simbol:
        simbol = str(baris.get("simbol") or "")
        for b in baris.get("klines_tanpa_funding") or []:
            ktf.append(f"{simbol}:{b}")
        for b in baris.get("funding_tanpa_klines") or []:
            ftk.append(f"{simbol}:{b}")
    ktf.sort()
    ftk.sort()
    return {
        "cacah_bulan_klines_tanpa_funding": len(ktf),
        "cacah_bulan_funding_tanpa_klines": len(ftk),
        "daftar_klines_tanpa_funding": ktf[:batas],
        "daftar_funding_tanpa_klines": ftk[:batas],
        "daftar_terpotong": len(ktf) > batas or len(ftk) > batas,
        "batas_daftar": batas,
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
        beda = selisih_bulan(bulan_k, bulan_f)
        per_simbol.append(
            {
                "simbol": nama,
                "cacah_bulan_klines": len(bulan_k),
                "cacah_bulan_funding": len(bulan_f),
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

    laporan: Dict[str, Any] = {
        "status": "TERUKUR" if simbol else "TIDAK MENGUKUR",
        "versi_funding": VERSI,
        "bukan_bukti": True,
        "penyebut": {
            "simbol_diminta": len(simbol),
            "simbol_terdaftar": len(per_simbol),
            "bulan_klines": cacah_bulan_klines,
            "bulan_funding": cacah_bulan_funding,
        },
        "cacah_simbol_gagal_daftar": len(gagal_daftar),
        "contoh_gagal_daftar": gagal_daftar[:10],
        "cacah_sampel": len(sampel),
        "cacah_sampel_gagal_unduh": sum(1 for s in sampel if s.get("gagal_unduh")),
        "cacah_sampel_gagal_checksum": sum(1 for s in sampel if s.get("gagal_checksum")),
        "byte_zip_sampel_min": min(byte_sampel) if byte_sampel else None,
        "byte_zip_sampel_maks": max(byte_sampel) if byte_sampel else None,
        "kelas_risiko_tersentuh": kelas,
        "kelas_risiko_kosong": [n for n, v in kelas.items() if not v],
        "sampel": sampel,
        "per_simbol": per_simbol,
    }
    laporan.update(ringkas)
    laporan["catatan_bukan_bukti"] = (
        "laporan ini diagnostik: ia mengukur ketersediaan funding dan TIDAK "
        "menulis funding_ada di manifes mana pun"
    )
    laporan["catatan_penggugur"] = (
        "cacah_simbol_gagal_daftar != 0 berarti listing tidak lengkap dan seluruh "
        "cacah di laporan ini batal sebagai angka semesta; bulan_klines != 19.598 "
        "berarti semesta yang dilihat modul ini bukan semesta manifes serapan, "
        "sehingga perbandingannya tidak sah (aturan 24)"
    )
    laporan["catatan_metode"] = (
        "ketersediaan diukur dari listing S3, bukan dari 404 per berkas; unduhan "
        "sungguhan hanya untuk sampel berlapis (aturan 37). Ketiadaan nama di "
        "listing dan ketiadaan berkas di CDN adalah dua hal berbeda, dan hanya "
        "yang pertama yang diukur di sini"
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

    tujuan = basis / KELUARAN
    tujuan.parent.mkdir(parents=True, exist_ok=True)
    tujuan.write_text(
        json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return laporan


def main() -> None:
    hasil = jalankan()
    ringkas = {k: v for k, v in hasil.items() if k not in ("per_simbol", "sampel")}
    print(json.dumps(ringkas, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
