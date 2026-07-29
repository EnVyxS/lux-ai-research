"""Apakah klines ekor kohort berisi perdagangan sungguhan atau lilin kosong.

Latar: 38 simbol berhenti menerbitkan funding serempak pada 2025-07 (456
simbol-bulan), sementara klines mereka terus terbit sampai 2026-06. Uji CDN pada
VERSI 5 membuktikan servernya menjawab 404 untuk berkas funding kohort sedangkan
kendali bulan sebelumnya terambil utuh. Yang TIDAK dapat dibedakan oleh 404 itu
adalah dua penjelasan yang sama-sama muat: (a) simbolnya berhenti diperdagangkan
sehingga funding memang tidak pernah ada, atau (b) arsip funding cacat sementara
pasarnya tetap hidup.

Modul ini mengukur pembeda itu. Bila lilin 1m pada bulan ekor berisi volume dan
transaksi sungguhan, penjelasan (a) melemah tajam. Bila lilin ekor kosong,
penjelasan (a) menguat.

DIAGNOSTIK, bukan gerbang: modul ini tidak menjatuhkan satu simbol-bulan pun dan
tidak menulis `funding_ada` di manifes mana pun. Ia mengimpor `gerbang_1m` hanya
untuk MEMBACA putusan gerbang atas deret yang sama, bukan untuk mengubahnya.

Rancangan pengukuran:

- Setiap simbol diukur BERPASANGAN. Bulan uji adalah bulan klines terakhir yang
  benar-benar tersedia di arsip; bulan kendali adalah bulan tepat sebelum lubang
  funding kohort dimulai. Simbolnya sama, jadi hanya satu variabel yang berubah.
  Tanpa kendali, bagian lilin kosong pada bulan ekor tidak punya pembanding dan
  tidak berarti apa-apa (aturan 24).
- Daftar anggota kohort DIBACA dari laporan funding, tidak disalin tangan. Salinan
  tangan di jurnal 70 meleset 16 nama karena daftarnya terpotong.
- Dua ukuran kekosongan dilaporkan terpisah: volume nol dan cacah transaksi nol.
  Keduanya tidak identik dan tidak boleh saling menggantikan (aturan 46).
- Kesimpulan hanya berlaku untuk simbol yang benar-benar disampel, bukan untuk
  seluruh kohort (aturan 20).

Aturan yang mengikat modul ini: 10, 16, 20, 21, 22, 24, 37, 41, 46, 47, 48, 49.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import zipfile
from pathlib import Path

from . import arsip, gerbang_1m

VERSI = 1
SUMBER = "reports/funding_semesta.json"
KELUARAN = "reports/kohort_ekor.json"
INTERVAL = "1m"
BATAS_SIMBOL = 10
BULAN_DIHARAPKAN = "2026-06"

# Tata letak CSV klines arsip Binance USDS-M.
IDX_WAKTU = 0
IDX_VOLUME = 5
IDX_TRANSAKSI = 8
KOLOM_MINIMAL = 9

BERKAS_DICAP = ["arsip.py", "gerbang_1m.py", "kohort_ekor.py", "resample.py"]


def sidik_kode() -> str:
    """Aturan 22 dan 48: cakup seluruh berkas yang ikut menentukan angka ini.

    `gerbang_1m.py` dan `resample.py` ikut dicap karena putusan gerbang yang
    dilaporkan modul ini lahir dari keduanya. Bila salah satu berubah tanpa
    sidik ikut berubah, dua versi kode berbeda akan berbagi satu sidik.
    """
    h = hashlib.sha256()
    for nama in sorted(BERKAS_DICAP):
        h.update((Path(__file__).parent / nama).read_bytes())
    return h.hexdigest()


def bagian(pembilang: int, penyebut: int):
    """Bagian yang menolak berbohong saat penyebutnya nol (aturan 41)."""
    if not penyebut:
        return None
    return round(pembilang / penyebut, 4)


def _angka(teks):
    try:
        return float(str(teks).strip())
    except (TypeError, ValueError):
        return None


def mundur_bulan(bulan: str, langkah: int = 1):
    """Bulan sebelum `bulan`, format YYYY-MM; None bila bentuknya bukan bulan."""
    bagian_bulan = str(bulan).split("-")
    if len(bagian_bulan) != 2:
        return None
    try:
        tahun = int(bagian_bulan[0])
        bln = int(bagian_bulan[1])
    except ValueError:
        return None
    if not 1 <= bln <= 12:
        return None
    total = tahun * 12 + (bln - 1) - langkah
    if total < 0:
        return None
    return f"{total // 12:04d}-{total % 12 + 1:02d}"


def muat_kohort(akar: str = ".") -> dict:
    """Baca daftar anggota kohort dari laporan funding yang sudah di-commit.

    Mengembalikan medan `galat` alih-alih melempar, supaya laporan tetap terbit
    dengan penggugur yang menyala dan bukan berhenti tanpa jejak.
    """
    jalur = Path(akar) / SUMBER
    if not jalur.exists():
        return {"simbol": [], "bulan_mulai": None, "galat": f"{SUMBER} tidak ada"}
    try:
        isi = json.loads(jalur.read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        return {"simbol": [], "bulan_mulai": None, "galat": f"{SUMBER} tidak terbaca: {exc}"}
    puncak = isi.get("kohort_puncak") or {}
    simbol = list(puncak.get("simbol") or [])
    if not simbol:
        return {"simbol": [], "bulan_mulai": None, "galat": "kohort_puncak.simbol kosong"}
    return {
        "simbol": sorted(simbol),
        "bulan_mulai": puncak.get("bulan_mulai"),
        "cacah_simbol_kohort": len(simbol),
        "galat": None,
    }


def baca_zip_klines(data: bytes) -> dict:
    """Urai satu zip klines 1m menjadi cap waktu, volume, dan cacah transaksi.

    Header hanya muncul pada berkas arsip yang lebih baru, jadi keberadaannya
    dinilai dari isi kolom pertama, bukan diasumsikan.
    """
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        nama = z.namelist()[0]
        mentah = z.read(nama).decode("utf-8", "replace")
    baris = [b for b in csv.reader(io.StringIO(mentah)) if b and any(k.strip() for k in b)]
    berheader = bool(baris) and _angka(baris[0][IDX_WAKTU]) is None
    if berheader:
        baris = baris[1:]
    cap = []
    volume = []
    transaksi = []
    cacat = 0
    for b in baris:
        if len(b) < KOLOM_MINIMAL:
            cacat += 1
            continue
        w = _angka(b[IDX_WAKTU])
        v = _angka(b[IDX_VOLUME])
        t = _angka(b[IDX_TRANSAKSI])
        if w is None or v is None or t is None:
            cacat += 1
            continue
        cap.append(int(w))
        volume.append(v)
        transaksi.append(int(t))
    return {
        "berheader": berheader,
        "cap_waktu": cap,
        "volume": volume,
        "transaksi": transaksi,
        "cacah_baris": len(cap),
        "cacah_baris_cacat": cacat,
    }


def ringkas_lilin(terurai: dict) -> dict:
    """Cacah kekosongan lilin. Volume nol dan transaksi nol dilaporkan terpisah."""
    volume = list(terurai.get("volume") or [])
    transaksi = list(terurai.get("transaksi") or [])
    n = len(volume)
    volume_nol = sum(1 for v in volume if v == 0)
    transaksi_nol = sum(1 for t in transaksi if t == 0)
    return {
        "cacah_lilin": n,
        "cacah_volume_nol": volume_nol,
        "cacah_transaksi_nol": transaksi_nol,
        "bagian_volume_nol": bagian(volume_nol, n),
        "bagian_transaksi_nol": bagian(transaksi_nol, n),
        "volume_total": round(sum(volume), 8),
        "transaksi_total": sum(transaksi),
    }


def ukur_satu(simbol: str, bulan: str, peran: str) -> dict:
    """Unduh satu simbol-bulan dan ukur isinya. Kegagalan dilaporkan, bukan ditelan."""
    baris = {
        "simbol": simbol,
        "bulan": bulan,
        "peran": peran,
        "gagal_unduh": False,
        "gagal_checksum": False,
        "galat": None,
        "berheader": None,
        "byte_zip": None,
        "lolos_gerbang": None,
        "pelanggaran": None,
    }
    try:
        data = arsip.unduh_terverifikasi(arsip.url_klines(simbol, INTERVAL, bulan))
    except Exception as exc:  # noqa: BLE001
        pesan = str(exc)
        baris["galat"] = pesan
        baris["gagal_checksum"] = "checksum tidak cocok" in pesan
        baris["gagal_unduh"] = not baris["gagal_checksum"]
        return baris
    terurai = baca_zip_klines(data)
    putusan = gerbang_1m.nilai_deret(terurai["cap_waktu"], simbol, bulan)
    baris.update(ringkas_lilin(terurai))
    baris["berheader"] = terurai["berheader"]
    baris["byte_zip"] = len(data)
    baris["cacah_baris_cacat"] = terurai["cacah_baris_cacat"]
    baris["lolos_gerbang"] = putusan["lolos"]
    baris["pelanggaran"] = putusan["pelanggaran"]
    baris["menit_hilang"] = putusan["ukuran"]["menit_hilang_dalam_rentang"]
    return baris


def ringkas(baris_semua) -> dict:
    """Cacah lintas simbol beserta medan penggugurnya (aturan 24)."""
    daftar = list(baris_semua)
    uji = [b for b in daftar if b.get("peran") == "uji"]
    kendali = [b for b in daftar if b.get("peran") == "kendali"]

    def hidup(b):
        return bool(b.get("bagian_volume_nol") is not None and b["bagian_volume_nol"] <= 0.5)

    kendali_terambil = [b for b in kendali if not b.get("galat")]
    return {
        "cacah_uji_diminta": len(uji),
        "cacah_kendali_diminta": len(kendali),
        "cacah_uji_terambil": len([b for b in uji if not b.get("galat")]),
        "cacah_kendali_terambil": len(kendali_terambil),
        "cacah_gagal_unduh": sum(1 for b in daftar if b.get("gagal_unduh")),
        "cacah_gagal_checksum": sum(1 for b in daftar if b.get("gagal_checksum")),
        "cacah_baris_cacat": sum(int(b.get("cacah_baris_cacat") or 0) for b in daftar),
        "cacah_uji_bagian_volume_nol_di_bawah_setengah": sum(1 for b in uji if hidup(b)),
        "cacah_kendali_bagian_volume_nol_di_bawah_setengah": sum(
            1 for b in kendali if hidup(b)
        ),
        "cacah_uji_lolos_gerbang": sum(1 for b in uji if b.get("lolos_gerbang")),
        "cacah_kendali_lolos_gerbang": sum(1 for b in kendali if b.get("lolos_gerbang")),
        "cacah_uji_bulan_bukan_diharapkan": sum(
            1 for b in uji if b.get("bulan") != BULAN_DIHARAPKAN
        ),
        "kendali_sah": bool(kendali_terambil) and len(kendali_terambil) == len(kendali),
    }


def jalankan(akar: str = ".") -> dict:
    kohort = muat_kohort(akar)
    batas = int(os.environ.get("KOHORT_BATAS_SIMBOL", BATAS_SIMBOL) or BATAS_SIMBOL)
    dipilih = kohort["simbol"][:batas]
    bulan_kendali = mundur_bulan(kohort.get("bulan_mulai") or "", 1)

    baris_semua = []
    catatan_bulan = []
    for simbol in dipilih:
        try:
            tersedia = arsip.bulan_tersedia(simbol, INTERVAL, "klines")
        except Exception as exc:  # noqa: BLE001
            baris_semua.append(
                {
                    "simbol": simbol,
                    "bulan": None,
                    "peran": "uji",
                    "gagal_unduh": True,
                    "gagal_checksum": False,
                    "galat": f"gagal mendaftar bulan: {exc}",
                }
            )
            continue
        bulan_uji = tersedia[-1] if tersedia else None
        catatan_bulan.append({"simbol": simbol, "bulan_klines_terakhir": bulan_uji})
        if bulan_uji:
            baris_semua.append(ukur_satu(simbol, bulan_uji, "uji"))
        if bulan_kendali and bulan_kendali in set(tersedia):
            baris_semua.append(ukur_satu(simbol, bulan_kendali, "kendali"))

    laporan = {
        "versi_kohort_ekor": VERSI,
        "sidik_kode": sidik_kode(),
        "sumber_kohort": SUMBER,
        "galat_kohort": kohort.get("galat"),
        "cacah_simbol_kohort": kohort.get("cacah_simbol_kohort"),
        "bulan_mulai_kohort": kohort.get("bulan_mulai"),
        "bulan_kendali": bulan_kendali,
        "batas_simbol": batas,
        "simbol_disampel": dipilih,
        "bulan_klines_terakhir": catatan_bulan,
        "baris": baris_semua,
        "ringkasan": ringkas(baris_semua),
        "catatan_bukan_bukti": (
            "laporan ini diagnostik: ia TIDAK menjatuhkan simbol-bulan mana pun dan "
            "TIDAK menulis funding_ada di manifes mana pun"
        ),
        "catatan_penggugur": (
            "galat_kohort != null berarti daftar anggota tidak terbaca dan seluruh "
            "laporan batal; kendali_sah == false berarti pembanding tidak lengkap "
            "sehingga angka bulan uji tidak boleh ditafsirkan; cacah_gagal_checksum "
            "!= 0 berarti berkas yang diukur tidak terbukti asli; "
            "cacah_uji_bulan_bukan_diharapkan != 0 berarti bulan ekor bukan "
            f"{BULAN_DIHARAPKAN} dan perbandingannya dengan jurnal terdahulu tidak sah "
            "(aturan 24)"
        ),
        "catatan_satuan": (
            "cacah_* bersatuan SIMBOL-BULAN kecuali cacah_lilin yang bersatuan LILIN; "
            "bagian_* adalah BAGIAN antara 0 dan 1, bukan persen (aturan 47)"
        ),
        "catatan_rentang": (
            "hasil berlaku untuk simbol yang benar-benar disampel saja dan tidak boleh "
            "digeneralkan ke seluruh kohort tanpa pengukuran lanjutan (aturan 20)"
        ),
        "catatan_tafsir": (
            "bagian volume nol yang rendah pada bulan ekor menunjukkan pasar masih "
            "diperdagangkan sesudah funding berhenti terbit, sehingga penjelasan "
            "delisting melemah; ia TIDAK membuktikan arsip funding cacat, karena "
            "pasar yang hidup di klines masih mungkin berpindah rezim funding"
        ),
    }
    return laporan


def main() -> int:
    laporan = jalankan(".")
    Path(KELUARAN).parent.mkdir(parents=True, exist_ok=True)
    with open(KELUARAN, "w", encoding="utf-8") as f:
        json.dump(laporan, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    ringkasan = dict(laporan["ringkasan"])
    ringkasan["sidik_kode"] = laporan["sidik_kode"]
    ringkasan["bulan_kendali"] = laporan["bulan_kendali"]
    ringkasan["galat_kohort"] = laporan["galat_kohort"]
    print(json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
