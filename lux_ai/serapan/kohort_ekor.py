"""Kapan perdagangan kohort ekor benar-benar berhenti.

Latar: 38 simbol berhenti menerbitkan funding serempak pada 2025-07 (456
simbol-bulan) sementara klines mereka terus terbit sampai 2026-06.

VERSI 1 (run 30414969064) menemukan bulan uji 2026-06 kosong total pada sepuluh
anggota. VERSI 2 (run 30415247380) memasang kendali positif BTCUSDT dan ETHUSDT
dan membuktikan pembaca CSV modul ini tidak buta: keempat baris kendali hidup
ramai, dan medan `kepala` menunjukkan indeks 5 memang `volume` serta indeks 8
memang `count`. Karena itu kekosongan kohort adalah sifat arsip, bukan cacat kode
(KC-18).

VERSI 2 juga menemukan bulan kendali 2025-06 IKUT kosong, padahal berkas funding
bulan itu terbukti ada dan berisi baris sungguhan. Funding terus terbit untuk
pasar yang sudah mati, sehingga tebing 2025-07 tidak dapat dijelaskan oleh
perdagangan yang berhenti pada tanggal itu.

VERSI 3 mengukur yang masih hilang: KAPAN perdagangan berhenti. Modul memindai
mundur `BATAS_MUNDUR` bulan bagi tiap simbol, mengukur seluruh jendela tanpa
berhenti lebih awal, lalu melaporkan `bulan_hidup_terakhir`. Jendela dipindai
utuh dengan sengaja: berhenti pada bulan ramai pertama akan MENGANDAIKAN
keruntuhan itu satu arah, padahal justru keandaian itu yang hendak diuji lewat
`bangkit_kembali`.

Penggugur baru: `batas_tercapai` menyala bila tak ada satu pun bulan ramai di
dalam jendela, artinya perdagangan berhenti SEBELUM jendela dan
`bulan_hidup_terakhir` tidak diketahui — bukan nol, melainkan tak terukur
(aturan 41).

DIAGNOSTIK, bukan gerbang: modul ini tidak menjatuhkan satu simbol-bulan pun dan
tidak menulis `funding_ada` di manifes mana pun.

Aturan yang mengikat modul ini: 10, 16, 20, 21, 22, 24, 37, 41, 46, 47, 48, 49, 50.
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

VERSI = 3
SUMBER = "reports/funding_semesta.json"
KELUARAN = "reports/kohort_ekor.json"
INTERVAL = "1m"
BATAS_SIMBOL = 10
BATAS_MUNDUR = 15
BULAN_DIHARAPKAN = "2026-06"

# Bulan tebing funding: seluruh kohort berhenti menerbitkan funding mulai bulan
# ini. Dipakai HANYA sebagai patokan pembanding, tidak untuk menyaring apa pun.
TEBING = "2025-07"

# Kendali positif: simbol yang tidak mungkin sepi sebulan penuh. Perannya bukan
# membandingkan pasar, melainkan MENGUJI PEMBACA CSV modul ini sendiri (aturan 50).
KENDALI_HIDUP = ("BTCUSDT", "ETHUSDT")

# Tata letak CSV klines arsip Binance USDS-M, terkonfirmasi dari medan `kepala`
# pada run 30415247380.
IDX_WAKTU = 0
IDX_VOLUME = 5
IDX_TRANSAKSI = 8
KOLOM_MINIMAL = 9

# Ambang sepi. Sebuah bulan disebut sepi bila bagian lilin bervolume nol
# MELEBIHI ambang ini, dan ramai bila di bawahnya DAN ada transaksi.
AMBANG_SEPI = 0.5

BERKAS_DICAP = ["arsip.py", "gerbang_1m.py", "kohort_ekor.py", "resample.py"]


def sidik_kode() -> str:
    """Aturan 22 dan 48: cakup seluruh berkas yang ikut menentukan angka ini."""
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


def sepi(baris) -> bool:
    """Benar bila bagian lilin bervolume nol MELEBIHI ambang."""
    nilai = baris.get("bagian_volume_nol")
    return nilai is not None and nilai > AMBANG_SEPI


def ramai(baris) -> bool:
    """Benar bila pasar jelas diperdagangkan pada bulan itu."""
    nilai = baris.get("bagian_volume_nol")
    return (
        nilai is not None
        and nilai < AMBANG_SEPI
        and int(baris.get("transaksi_total") or 0) > 0
    )


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


def jendela_bulan(tersedia, batas: int) -> list:
    """`batas` bulan terakhir yang tersedia, urut menaik."""
    bersih = sorted(b for b in (tersedia or []) if b)
    if batas and batas > 0:
        return bersih[-batas:]
    return bersih


def peran_bulan(bulan, bulan_terakhir, bulan_kendali) -> str:
    """Nama peran satu bulan di dalam jendela pindai."""
    if bulan == bulan_terakhir:
        return "uji"
    if bulan_kendali and bulan == bulan_kendali:
        return "kendali"
    return "pindai"


def muat_kohort(akar: str = ".") -> dict:
    """Baca daftar anggota kohort dari laporan funding yang sudah di-commit."""
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
    """Urai satu zip klines 1m menjadi cap waktu, volume, dan cacah transaksi."""
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        nama = z.namelist()[0]
        mentah = z.read(nama).decode("utf-8", "replace")
    baris = [b for b in csv.reader(io.StringIO(mentah)) if b and any(k.strip() for k in b)]
    berheader = bool(baris) and _angka(baris[0][IDX_WAKTU]) is None
    kepala = list(baris[0]) if berheader else None
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
        "kepala": kepala,
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


def baris_kendali_hidup(bulan_uji, bulan_kendali, ukur=None) -> list:
    """Ukur simbol yang pasti hidup pada bulan yang sama dengan kohort."""
    jalan = ukur or ukur_satu
    bulan_dipakai = [b for b in (bulan_uji, bulan_kendali) if b]
    hasil = []
    for simbol in KENDALI_HIDUP:
        for bulan in bulan_dipakai:
            hasil.append(jalan(simbol, bulan, "kendali_hidup"))
    return hasil


def nilai_riwayat(simbol: str, baris_simbol) -> dict:
    """Kapan simbol ini terakhir diperdagangkan, di dalam jendela yang dipindai.

    `batas_tercapai` menyala bila tak satu pun bulan di jendela ramai. Dalam hal
    itu `bulan_hidup_terakhir` bernilai None dan TIDAK boleh dibaca sebagai
    "tidak pernah hidup": ia berarti tak terukur di jendela ini (aturan 41).
    """
    urut = sorted(
        (b for b in baris_simbol if b.get("bulan") and not b.get("galat")),
        key=lambda b: b["bulan"],
    )
    bulan_ramai = [b["bulan"] for b in urut if ramai(b)]
    bulan_sepi = [b["bulan"] for b in urut if sepi(b)]
    hidup_terakhir = bulan_ramai[-1] if bulan_ramai else None
    bangkit = bool(bulan_sepi) and any(m > bulan_sepi[0] for m in bulan_ramai)
    return {
        "simbol": simbol,
        "cacah_bulan_dipindai": len(urut),
        "cacah_bulan_ramai": len(bulan_ramai),
        "cacah_bulan_sepi": len(bulan_sepi),
        "bulan_paling_awal_dipindai": urut[0]["bulan"] if urut else None,
        "bulan_hidup_terakhir": hidup_terakhir,
        "bulan_sepi_paling_awal": bulan_sepi[0] if bulan_sepi else None,
        "bangkit_kembali": bangkit,
        "batas_tercapai": not bulan_ramai,
        "hidup_terakhir_sebelum_tebing": (
            None if hidup_terakhir is None else hidup_terakhir < TEBING
        ),
    }


def ringkas(baris_semua, riwayat=None) -> dict:
    """Cacah lintas simbol beserta medan penggugurnya (aturan 24)."""
    daftar = list(baris_semua)
    daftar_riwayat = list(riwayat or [])
    uji = [b for b in daftar if b.get("peran") == "uji"]
    kendali = [b for b in daftar if b.get("peran") == "kendali"]
    pindai = [b for b in daftar if b.get("peran") == "pindai"]
    hidup = [b for b in daftar if b.get("peran") == "kendali_hidup"]

    kendali_terambil = [b for b in kendali if not b.get("galat")]
    hidup_terambil = [b for b in hidup if not b.get("galat")]
    terukur = [r for r in daftar_riwayat if not r.get("batas_tercapai")]
    return {
        "cacah_uji_diminta": len(uji),
        "cacah_kendali_diminta": len(kendali),
        "cacah_pindai_diminta": len(pindai),
        "cacah_kendali_hidup_diminta": len(hidup),
        "cacah_uji_terambil": len([b for b in uji if not b.get("galat")]),
        "cacah_kendali_terambil": len(kendali_terambil),
        "cacah_kendali_hidup_terambil": len(hidup_terambil),
        "cacah_gagal_unduh": sum(1 for b in daftar if b.get("gagal_unduh")),
        "cacah_gagal_checksum": sum(1 for b in daftar if b.get("gagal_checksum")),
        "cacah_baris_cacat": sum(int(b.get("cacah_baris_cacat") or 0) for b in daftar),
        "cacah_uji_sepi": sum(1 for b in uji if sepi(b)),
        "cacah_kendali_sepi": sum(1 for b in kendali if sepi(b)),
        "cacah_simbol_bulan_sepi": sum(1 for b in daftar if sepi(b)),
        "cacah_kendali_hidup_ramai": sum(1 for b in hidup if ramai(b)),
        "cacah_uji_lolos_gerbang": sum(1 for b in uji if b.get("lolos_gerbang")),
        "cacah_kendali_lolos_gerbang": sum(1 for b in kendali if b.get("lolos_gerbang")),
        "cacah_uji_bulan_bukan_diharapkan": sum(
            1 for b in uji if b.get("bulan") != BULAN_DIHARAPKAN
        ),
        "cacah_simbol_riwayat": len(daftar_riwayat),
        "cacah_simbol_hidup_terakhir_terukur": len(terukur),
        "cacah_simbol_batas_tercapai": sum(
            1 for r in daftar_riwayat if r.get("batas_tercapai")
        ),
        "cacah_simbol_bangkit_kembali": sum(
            1 for r in daftar_riwayat if r.get("bangkit_kembali")
        ),
        "cacah_simbol_hidup_terakhir_sebelum_tebing": sum(
            1 for r in terukur if r.get("hidup_terakhir_sebelum_tebing")
        ),
        "kendali_sah": bool(kendali_terambil) and len(kendali_terambil) == len(kendali),
        "parser_terbukti": bool(hidup) and all(ramai(b) for b in hidup),
    }


def jalankan(akar: str = ".") -> dict:
    kohort = muat_kohort(akar)
    batas = int(os.environ.get("KOHORT_BATAS_SIMBOL", BATAS_SIMBOL) or BATAS_SIMBOL)
    mundur = int(os.environ.get("KOHORT_BATAS_MUNDUR", BATAS_MUNDUR) or BATAS_MUNDUR)
    dipilih = kohort["simbol"][:batas]
    bulan_kendali = mundur_bulan(kohort.get("bulan_mulai") or "", 1)

    baris_semua = []
    riwayat = []
    catatan_bulan = []
    bulan_uji_terakhir = None
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
        jendela = jendela_bulan(tersedia, mundur)
        bulan_terakhir = jendela[-1] if jendela else None
        catatan_bulan.append({"simbol": simbol, "bulan_klines_terakhir": bulan_terakhir})
        if bulan_terakhir:
            bulan_uji_terakhir = bulan_terakhir
        baris_simbol = [
            ukur_satu(simbol, bulan, peran_bulan(bulan, bulan_terakhir, bulan_kendali))
            for bulan in jendela
        ]
        baris_semua += baris_simbol
        riwayat.append(nilai_riwayat(simbol, baris_simbol))

    baris_semua += baris_kendali_hidup(
        bulan_uji_terakhir or BULAN_DIHARAPKAN, bulan_kendali
    )

    laporan = {
        "versi_kohort_ekor": VERSI,
        "sidik_kode": sidik_kode(),
        "sumber_kohort": SUMBER,
        "galat_kohort": kohort.get("galat"),
        "cacah_simbol_kohort": kohort.get("cacah_simbol_kohort"),
        "bulan_mulai_kohort": kohort.get("bulan_mulai"),
        "bulan_kendali": bulan_kendali,
        "bulan_tebing": TEBING,
        "batas_simbol": batas,
        "batas_mundur": mundur,
        "ambang_sepi": AMBANG_SEPI,
        "simbol_disampel": dipilih,
        "simbol_kendali_hidup": list(KENDALI_HIDUP),
        "bulan_klines_terakhir": catatan_bulan,
        "riwayat": riwayat,
        "baris": baris_semua,
        "ringkasan": ringkas(baris_semua, riwayat),
        "catatan_bukan_bukti": (
            "laporan ini diagnostik: ia TIDAK menjatuhkan simbol-bulan mana pun dan "
            "TIDAK menulis funding_ada di manifes mana pun"
        ),
        "catatan_penggugur": (
            "parser_terbukti == false berarti pembaca CSV modul ini tidak terbukti "
            "membaca kolom volume dan transaksi dengan benar, sehingga SELURUH klaim "
            "kekosongan di laporan ini batal (aturan 50); batas_tercapai == true pada "
            "sebuah simbol berarti tak ada bulan ramai di dalam jendela, sehingga "
            "bulan_hidup_terakhir simbol itu TAK TERUKUR dan bukan bernilai nol; "
            "galat_kohort != null berarti daftar anggota tidak terbaca; kendali_sah "
            "== false berarti pembanding tidak lengkap; cacah_gagal_checksum != 0 "
            "berarti berkas yang diukur tidak terbukti asli (aturan 24)"
        ),
        "catatan_kendali_hidup": (
            "KENDALI_HIDUP bukan pembanding pasar melainkan penguji pembaca CSV modul "
            "ini sendiri: bila simbol yang pasti diperdagangkan pun terbaca kosong, "
            "yang cacat adalah kode, bukan arsip"
        ),
        "catatan_satuan": (
            "cacah_simbol_* bersatuan SIMBOL; cacah_uji_*, cacah_kendali_*, "
            "cacah_pindai_*, dan cacah_simbol_bulan_sepi bersatuan SIMBOL-BULAN; "
            "cacah_lilin bersatuan LILIN; bagian_* adalah BAGIAN antara 0 dan 1, "
            "bukan persen (aturan 47)"
        ),
        "catatan_rentang": (
            "hasil berlaku untuk simbol dan bulan yang benar-benar disampel saja; "
            "jendela dibatasi batas_mundur bulan terakhir, jadi tidak ada pernyataan "
            "apa pun tentang bulan di luar jendela (aturan 20)"
        ),
        "catatan_tafsir": (
            "bulan_hidup_terakhir yang lebih awal daripada bulan_tebing menunjukkan "
            "perdagangan berhenti SEBELUM funding berhenti terbit, sehingga tebing "
            "funding bukan cerminan peristiwa pasar pada bulan itu. Ia TIDAK "
            "membuktikan arsip funding cacat: penghentian penerbitan yang tertunda "
            "sama-sama muat dengan data ini"
        ),
    }
    return laporan


def main() -> int:
    laporan = jalankan(".")
    Path(KELUARAN).parent.mkdir(parents=True, exist_ok=True)
    with open(KELUARAN, "w", encoding="utf-8") as f:
        json.dump(laporan, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True))
    ringkasan = laporan["ringkasan"]
    # Kode keluar bukan hiasan: penggugur yang menyala harus terlihat dari luar.
    if laporan["galat_kohort"] or not ringkasan["parser_terbukti"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
