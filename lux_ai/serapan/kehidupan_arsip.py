"""Kehidupan SELURUH semesta terserap, diukur dari parquet rilis — bukan arsip.

Jurnal 81 menutup kohort puncak: 456 dari 456 simbol-bulan MATI. Aturan 20
melarang menyimpulkan apa pun tentang 19.142 simbol-bulan sisanya, dan itulah
lubang terbesar yang tersisa — sebab bila kematian meluas, semesta yang layak
di-backtest jauh lebih kecil daripada 19.598.

## Mengapa TIDAK mengunduh ulang dari arsip

`kehidupan.py` V1 mengunduh 456 zip dari `data.binance.vision`. Cara yang sama
untuk 19.586 simbol-bulan berarti ±26,5 GB unduhan dan berjam-jam runner, sedang
SELURUH data itu sudah tersimpan sebagai parquet di aset rilis — dan sudah
terbukti dapat diambil kembali oleh proses yang tidak menulisnya (run
`30404071324`, 29/29 aset, sha cocok, 839.842.134 baris terbaca ulang).

Parquet menyimpan kolom `volume` dan `trades` (lihat `klines.KOLOM_SIMPAN`),
tepat dua kolom yang dibutuhkan definisi ADR-A008. Jadi kehidupan dapat diukur
dari artefak yang sudah terverifikasi, tanpa menyentuh jaringan arsip sama
sekali.

Konsekuensi yang WAJIB disebut, bukan disembunyikan:

- Penyebutnya adalah **19.586 simbol-bulan yang LOLOS gerbang**, bukan 19.598.
  Dua belas simbol-bulan karantina ada di tar terpisah dan TIDAK diukur di sini
  (aturan 30, 44).
- Parquet ditulis dengan `teks=True`, sehingga `volume` dan `trades` berupa
  STRING. Ia diurai dengan pengurai sendiri; baris yang tak terurai dicacah
  sebagai `cacah_baris_cacat`, tidak diam-diam dibaca sebagai nol (aturan 16).
- Bila tak satu pun baris terurai, `transaksi_total` dibuat **null**, bukan 0,
  supaya berkas yang tak terbaca tidak menyamar sebagai pasar yang mati
  (aturan 41, 46).

## Kendali positif (aturan 50)

`kehidupan.py` memakai BTCUSDT dan ETHUSDT sebagai kendali. Di sini kendali itu
tidak selalu tersedia: pembagian pecahan bersifat round-robin atas abjad,
sehingga BTCUSDT hanya ada di SATU pecahan. Kendali karena itu dipilih dari
manifes pecahan itu sendiri, SEBELUM satu byte data pun dibaca: **tiga
simbol-bulan dengan `byte_parquet` terbesar**. Pemilihannya deterministik dan
tidak melihat volume maupun transaksi, jadi ia bukan lingkaran; parquet zstd
yang besar berarti banyak nilai berbeda, yang mustahil dihasilkan lilin datar.
Bila salah satu dari ketiganya tidak terbaca HIDUP, `parser_terbukti` false,
kode keluar 2, dan SELURUH klaim kematian pecahan itu batal.

## Praregistrasi ramalan — ditulis SEBELUM run

- **R-205** — CI pada commit ini mengumpulkan **291 butir**, kode keluar 0.
  Dasar: 269 butir terverifikasi pada run `30418761270`, ditambah 22 butir baru
  dari `tests/test_kehidupan_arsip.py` (18 fungsi berbutir tunggal + 1 fungsi
  berparameter empat kasus). Satuan: BUTIR yang dikumpulkan pytest (aturan 38,
  47).
- **R-206** — dijumlahkan atas kedelapan pecahan, simbol-bulan berstatus MATI
  berjumlah dalam pita **456..2.000**. Satuan: SIMBOL-BULAN. Penyebut eksplisit:
  19.586 simbol-bulan yang lolos gerbang dan terkemas di tar utama, BUKAN 19.598
  (aturan 44). Dasar pita: 456 sudah terukur mati di kohort puncak, dan 880
  adalah seluruh bulan klines tanpa funding — himpunan yang paling mungkin
  memuat bulan tak diperdagangkan. Batas atas 2.000 dipasang agar ramalan ini
  benar-benar dapat gugur: bila kematian menembusnya, ia meluas jauh di luar
  himpunan lubang funding, dan itu temuan besar yang harus dicatat sebagai
  MELESET, bukan dibenarkan belakangan.
- **R-207** — `parser_terbukti` bernilai true pada **kedelapan** pecahan, yakni
  ketiga kendali tiap pecahan terbaca HIDUP. Penggugur: bila satu pecahan saja
  gagal, R-206 dicatat TIDAK TERADJUDIKASI, bukan MELESET, sebab penyebutnya
  cacat (aturan 41).

Modul ini DIAGNOSTIK. Ia tidak menjatuhkan satu simbol-bulan pun, tidak menyentuh
manifes, dan tidak menulis ulang 839.842.134 (aturan 29).

Aturan yang mengikat: 10, 16, 20, 21, 22, 24, 29, 30, 41, 44, 45, 46, 47, 48,
50, 52.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import tarfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from . import kehidupan, kohort_ekor, pulihkan, rilis

VERSI = 1
TOTAL_PECAHAN = 8
AKAR_UNDUH = "data/unduh"
AKAR_BONGKAR = "data/kehidupan_arsip"
KENDALI_CACAH = 3
KOLOM_VOLUME = "volume"
KOLOM_TRANSAKSI = "trades"

BERKAS_DICAP = [
    "kehidupan.py",
    "kehidupan_arsip.py",
    "kohort_ekor.py",
    "pulihkan.py",
    "rilis.py",
]


def nama_keluaran(indeks: int) -> str:
    return f"reports/kehidupan_arsip_{indeks}.json"


def nama_ringkas(indeks: int) -> str:
    return f"reports/kehidupan_arsip_{indeks}_ringkas.json"


def sidik_kode() -> str:
    """Aturan 22: cap setiap berkas yang ikut menentukan angka ini."""
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(BERKAS_DICAP):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def peta_parquet(manifes: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """Jalur parquet -> simbol, bulan, byte. Baris tanpa parquet dilewati.

    Baris karantina menaruh jalurnya di `parquet_karantina` dan sengaja TIDAK
    masuk sini: tar karantina tidak diunduh workflow ini, dan mencampurnya akan
    membuat penyebut 19.586 diam-diam berubah (aturan 30).
    """
    hasil: Dict[str, Dict[str, Any]] = {}
    for baris in manifes.get("manifes") or []:
        jalur = baris.get("parquet")
        if not jalur:
            continue
        hasil[str(jalur)] = {
            "simbol": str(baris.get("simbol") or ""),
            "bulan": str(baris.get("bulan") or ""),
            "jalur": str(jalur),
            "byte_parquet": int(baris.get("byte_parquet") or 0),
            "gerbang_lolos": baris.get("gerbang_lolos"),
            "baris_manifes": int(baris.get("baris") or 0),
        }
    return hasil


def _angka(teks: Any) -> Optional[float]:
    if teks is None:
        return None
    s = str(teks).strip()
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def ukur_kolom(volume: List[Any], transaksi: List[Any]) -> Dict[str, Any]:
    """Ukur satu simbol-bulan dari dua kolom mentah berupa string.

    `transaksi_total` sengaja null ketika tak satu baris pun terurai: berkas yang
    tidak terbaca BUKAN pasar yang mati (aturan 41, 46).
    """
    n = max(len(volume), len(transaksi))
    cacat = 0
    terbaca = 0
    total = 0.0
    nol = 0
    for i in range(n):
        v = _angka(volume[i]) if i < len(volume) else None
        t = _angka(transaksi[i]) if i < len(transaksi) else None
        if v is None or t is None:
            cacat += 1
            continue
        terbaca += 1
        total += t
        if v == 0.0:
            nol += 1
    return {
        "cacah_lilin": n,
        "cacah_lilin_terbaca": terbaca,
        "cacah_baris_cacat": cacat,
        "transaksi_total": int(total) if terbaca else None,
        "cacah_volume_nol": nol,
        "bagian_volume_nol": kohort_ekor.bagian(nol, terbaca),
    }


def ukur_parquet(jalur: Path) -> Dict[str, Any]:
    """Baca DUA kolom saja dari satu parquet dan ukur kehidupannya."""
    import pyarrow.parquet as pq

    berkas = pq.ParquetFile(str(jalur))
    nama_kolom = set(berkas.schema_arrow.names)
    kurang = [k for k in (KOLOM_VOLUME, KOLOM_TRANSAKSI) if k not in nama_kolom]
    if kurang:
        return {
            "cacah_lilin": int(berkas.metadata.num_rows),
            "cacah_lilin_terbaca": 0,
            "cacah_baris_cacat": int(berkas.metadata.num_rows),
            "transaksi_total": None,
            "cacah_volume_nol": 0,
            "bagian_volume_nol": None,
            "galat": f"kolom hilang: {','.join(kurang)}",
        }
    tabel = berkas.read(columns=[KOLOM_VOLUME, KOLOM_TRANSAKSI])
    ukuran = ukur_kolom(
        tabel.column(KOLOM_VOLUME).to_pylist(),
        tabel.column(KOLOM_TRANSAKSI).to_pylist(),
    )
    ukuran["galat"] = None
    return ukuran


def baris_kehidupan(info: Dict[str, Any], ukuran: Dict[str, Any]) -> Dict[str, Any]:
    """Satu baris laporan; statusnya dari `kehidupan.klasifikasi`, satu definisi."""
    baris: Dict[str, Any] = {
        "simbol": info.get("simbol"),
        "bulan": info.get("bulan"),
        "jalur": info.get("jalur"),
        "gerbang_lolos": info.get("gerbang_lolos"),
        "byte_parquet": info.get("byte_parquet"),
        "ada_di_arsip": True,
    }
    baris.update(ukuran)
    baris["status"] = kehidupan.klasifikasi(baris)
    return baris


def kendali_pecahan(
    peta: Dict[str, Dict[str, Any]], cacah: int = KENDALI_CACAH
) -> List[Tuple[str, str]]:
    """Kendali positif dipilih dari MANIFES, sebelum data dibaca (aturan 50).

    Kunci urut: byte parquet menurun, lalu simbol dan bulan menaik, supaya
    pilihannya tetap sama persis pada tiap pengulangan.
    """
    urut = sorted(
        peta.values(),
        key=lambda x: (-int(x.get("byte_parquet") or 0), str(x.get("simbol")), str(x.get("bulan"))),
    )
    return [(str(x.get("simbol")), str(x.get("bulan"))) for x in urut[:cacah]]


def ringkas_pecahan(
    baris: List[Dict[str, Any]],
    kendali_kunci: List[Tuple[str, str]],
    angkutan: Dict[str, Any],
) -> Dict[str, Any]:
    """Penyebut ganda ADR-A008 ditambah medan penggugur pengangkutan."""
    angka = kehidupan.penyebut_ganda(baris)
    status_per_kunci = {(str(b.get("simbol")), str(b.get("bulan"))): b.get("status") for b in baris}
    kendali = [
        {"simbol": s, "bulan": b, "status": status_per_kunci.get((s, b))}
        for s, b in kendali_kunci
    ]
    hidup = sum(1 for k in kendali if k["status"] == kehidupan.STATUS_HIDUP)
    ringkasan: Dict[str, Any] = {
        "cacah_parquet_diminta": int(angkutan.get("cacah_parquet_diminta") or 0),
        "cacah_parquet_terbaca": len(baris),
        "cacah_parquet_hilang": int(angkutan.get("cacah_parquet_hilang") or 0),
        "cacah_parquet_tak_dikenal": int(angkutan.get("cacah_parquet_tak_dikenal") or 0),
        "cacah_bagian_hilang": int(angkutan.get("cacah_bagian_hilang") or 0),
        "cacah_sha_tak_cocok": int(angkutan.get("cacah_sha_tak_cocok") or 0),
        "cacah_anggota_tak_aman": int(angkutan.get("cacah_anggota_tak_aman") or 0),
        "cacah_baris_cacat": sum(int(b.get("cacah_baris_cacat") or 0) for b in baris),
        "cacah_tak_terukur": sum(
            1 for b in baris if b.get("status") == kehidupan.STATUS_TAK_TERUKUR
        ),
        "cacah_mati_lolos_gerbang": sum(
            1
            for b in baris
            if b.get("status") == kehidupan.STATUS_MATI and b.get("gerbang_lolos")
        ),
        "kendali": kendali,
        "cacah_kendali": len(kendali),
        "cacah_kendali_hidup": hidup,
        "parser_terbukti": bool(kendali) and hidup == len(kendali),
    }
    ringkasan.update(angka)
    return ringkasan


def kode_keluar(ringkasan: Dict[str, Any]) -> int:
    """Kode 2 bila laporan tidak berhak diklaim sebagai pengukuran."""
    if not ringkasan.get("parser_terbukti"):
        return 2
    for medan in (
        "cacah_sha_tak_cocok",
        "cacah_bagian_hilang",
        "cacah_parquet_hilang",
        "cacah_anggota_tak_aman",
    ):
        if int(ringkasan.get(medan) or 0) > 0:
            return 2
    return 0


def _cocokkan(nama: str, peta: Dict[str, Dict[str, Any]], per_nama: Dict[str, Dict[str, Any]]):
    """Anggota tar dicocokkan ke manifes lewat jalur penuh, lalu nama berkas."""
    if nama in peta:
        return peta[nama]
    return per_nama.get(Path(nama).name)


def periksa_bagian(
    jalur_tar: Path,
    sha_harap: str,
    peta: Dict[str, Dict[str, Any]],
    per_nama: Dict[str, Dict[str, Any]],
    tujuan: Path,
    hapus: bool = True,
) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    """Satu bagian tar: cocokkan sidik, bongkar seanggota demi seanggota, ukur.

    Anggota dihapus segera setelah diukur; puncak cakram tetap satu tar plus satu
    parquet, bukan satu pecahan terbongkar penuh.
    """
    rincian: Dict[str, Any] = {
        "nama": jalur_tar.name,
        "ada": jalur_tar.exists(),
        "sha256": None,
        "sha256_diharap": sha_harap,
        "sha_cocok": False,
        "byte": 0,
        "cacah_anggota": 0,
        "cacah_anggota_tak_aman": 0,
        "cacah_parquet_tak_dikenal": 0,
    }
    baris: List[Dict[str, Any]] = []
    if not rincian["ada"]:
        return rincian, baris

    rincian["byte"] = int(jalur_tar.stat().st_size)
    rincian["sha256"] = rilis.sha256_berkas(jalur_tar)
    rincian["sha_cocok"] = bool(rincian["sha256"] == sha_harap)
    tujuan.mkdir(parents=True, exist_ok=True)

    with tarfile.open(jalur_tar, "r") as tar:
        for anggota in tar.getmembers():
            if not anggota.isfile():
                continue
            if not pulihkan.anggota_aman(anggota.name):
                rincian["cacah_anggota_tak_aman"] += 1
                continue
            info = _cocokkan(anggota.name, peta, per_nama)
            if info is None:
                rincian["cacah_parquet_tak_dikenal"] += 1
                continue
            tar.extract(anggota, path=str(tujuan))
            rincian["cacah_anggota"] += 1
            keluar = tujuan / anggota.name
            try:
                ukuran = ukur_parquet(keluar)
            except Exception as exc:  # noqa: BLE001
                ukuran = {
                    "cacah_lilin": 0,
                    "cacah_lilin_terbaca": 0,
                    "cacah_baris_cacat": 0,
                    "transaksi_total": None,
                    "cacah_volume_nol": 0,
                    "bagian_volume_nol": None,
                    "galat": str(exc)[:300],
                }
            baris.append(baris_kehidupan(info, ukuran))
            if hapus and keluar.exists():
                keluar.unlink()

    if hapus and jalur_tar.exists():
        jalur_tar.unlink()
    return rincian, baris


def jalankan(
    indeks: int,
    akar: str = ".",
    dir_unduh: str = AKAR_UNDUH,
    dir_bongkar: str = AKAR_BONGKAR,
    hapus: bool = True,
) -> Dict[str, Any]:
    basis = Path(akar)
    mentah = (basis / pulihkan.nama_manifes(indeks)).read_bytes()
    manifes = json.loads(mentah.decode("utf-8"))
    peta = peta_parquet(manifes)
    per_nama = {Path(k).name: v for k, v in peta.items()}
    kendali_kunci = kendali_pecahan(peta)

    bagian_harap = ((manifes.get("rilis") or {}).get("bagian")) or []
    rincian: List[Dict[str, Any]] = []
    baris: List[Dict[str, Any]] = []
    for b in bagian_harap:
        r, isi = periksa_bagian(
            basis / dir_unduh / str(b.get("nama")),
            str(b.get("sha256")),
            peta,
            per_nama,
            basis / dir_bongkar,
            hapus=hapus,
        )
        rincian.append(r)
        baris += isi

    terbaca = {(str(x.get("simbol")), str(x.get("bulan"))) for x in baris}
    angkutan = {
        "cacah_parquet_diminta": len(peta),
        "cacah_parquet_hilang": len(
            {(v["simbol"], v["bulan"]) for v in peta.values()} - terbaca
        ),
        "cacah_parquet_tak_dikenal": sum(int(r["cacah_parquet_tak_dikenal"]) for r in rincian),
        "cacah_bagian_hilang": sum(1 for r in rincian if not r["ada"]),
        "cacah_sha_tak_cocok": sum(1 for r in rincian if r["ada"] and not r["sha_cocok"]),
        "cacah_anggota_tak_aman": sum(int(r["cacah_anggota_tak_aman"]) for r in rincian),
    }
    ringkasan = ringkas_pecahan(baris, kendali_kunci, angkutan)

    return {
        "bukan_bukti": False,
        "versi_kehidupan_arsip": VERSI,
        "indeks": indeks,
        "total_pecahan": TOTAL_PECAHAN,
        "run_id_sumber": pulihkan.run_id_sumber(indeks, akar=akar),
        "sumber_manifes": pulihkan.nama_manifes(indeks),
        "sidik_manifes": hashlib.sha256(mentah).hexdigest(),
        "sidik_kode_manifes": manifes.get("sidik_kode"),
        "sidik_kode": sidik_kode(),
        "ambang_sepi": kohort_ekor.AMBANG_SEPI,
        "definisi": {
            "MATI": "transaksi_total == 0",
            "SEPI": "bukan MATI dan bagian_volume_nol >= ambang_sepi",
            "HIDUP": "selain keduanya",
            "TAK_TERUKUR": (
                "parquet tak terbaca, kolom hilang, atau tak satu baris pun "
                "terurai; BUKAN nol dan tidak masuk penyebut mana pun"
            ),
        },
        "kendali_dipilih": [{"simbol": s, "bulan": b} for s, b in kendali_kunci],
        "bagian": rincian,
        "baris": baris,
        "ringkasan": ringkasan,
        "catatan_kendali": (
            "kendali positif dipilih dari manifes SEBELUM data dibaca: tiga "
            "simbol-bulan dengan byte_parquet terbesar. Pemilihan tidak melihat "
            "volume maupun transaksi, jadi bukan lingkaran (aturan 50)"
        ),
        "catatan_penyebut": (
            "penyebut pecahan ini adalah parquet yang LOLOS gerbang dan terkemas "
            "di tar utama; 12 simbol-bulan karantina semesta ada di tar terpisah "
            "dan TIDAK diukur di sini, sehingga jumlah lintas pecahan adalah "
            "19.586, bukan 19.598 (aturan 30, 44)"
        ),
        "catatan_penggugur": (
            "parser_terbukti false berarti seluruh klaim kematian pecahan ini "
            "batal; cacah_sha_tak_cocok, cacah_bagian_hilang, "
            "cacah_parquet_hilang, dan cacah_anggota_tak_aman bukan nol berarti "
            "yang diukur bukan seluruh isi pecahan (aturan 24)"
        ),
        "catatan_rentang": (
            f"hasil berlaku untuk pecahan {indeks} dari {TOTAL_PECAHAN} saja; "
            "penjumlahan lintas pecahan hanya sah bila kedelapan laporan berasal "
            "dari sidik_kode yang sama (aturan 20, 22)"
        ),
        "waktu_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def berkas_ringkas(laporan: Dict[str, Any], teks_sumber: str, indeks: int) -> Dict[str, Any]:
    """Aturan 52: ringkasan yang terbaca utuh dan menyebut sidik laporan penuhnya."""
    byte_sumber = teks_sumber.encode("utf-8")
    return {
        "versi_kehidupan_arsip": laporan.get("versi_kehidupan_arsip"),
        "indeks": indeks,
        "sidik_kode": laporan.get("sidik_kode"),
        "sidik_manifes": laporan.get("sidik_manifes"),
        "run_id_sumber": laporan.get("run_id_sumber"),
        "berkas_sumber": nama_keluaran(indeks),
        "byte_sumber": len(byte_sumber),
        "sidik_sumber": hashlib.sha256(byte_sumber).hexdigest(),
        "definisi": laporan.get("definisi"),
        "kendali_dipilih": laporan.get("kendali_dipilih"),
        "ringkasan": laporan.get("ringkasan"),
    }


def main() -> int:
    indeks = int(os.environ.get("KEHIDUPAN_ARSIP_INDEKS", "0") or 0)
    laporan = jalankan(indeks)
    teks = json.dumps(laporan, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    Path(nama_keluaran(indeks)).parent.mkdir(parents=True, exist_ok=True)
    Path(nama_keluaran(indeks)).write_text(teks, encoding="utf-8")
    ringkas = berkas_ringkas(laporan, teks, indeks)
    Path(nama_ringkas(indeks)).write_text(
        json.dumps(ringkas, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(ringkas, ensure_ascii=False, indent=2, sort_keys=True))
    return kode_keluar(laporan["ringkasan"])


if __name__ == "__main__":
    raise SystemExit(main())
