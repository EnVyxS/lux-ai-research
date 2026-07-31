"""sumber_funding.py — menyelidiki DARI MANA label funding sesungguhnya berasal.

Latar: R-322 membuktikan medan `funding_ada` pada manifes bernilai `null` pada
SELURUH 19.598 entri. Medan itu mati. Maka kelas positif 33 mustahil diturunkan
dari manifes, dan utang ukur 35 dibuka: dari berkas mana ia berasal, dan seberapa
jauh jangkauannya.

Modul ini TIDAK mengandaikan bentuk berkas mana pun. Ia berjalan menyusuri
struktur apa adanya dan melaporkan apa yang ditemuinya.

Nama medan keluaran di bawah ini TERIKAT oleh praregistrasi R-323 di
`journal/2026-07-31-163.md`, yang didorong SEBELUM berkas ini ditulis:
  - kandidat["hidup_tanpa_funding"].wadah_panjang_33
  - kandidat["hidup_tanpa_funding"].cacah_lima_simbol
  - kandidat["funding_semesta"].wadah_penting / tipe_puncak
  - jangkauan_maksimum_funding
  - silang.jumlah_enam_sel

Disiplin yang diwarisi dari KOREKSI 19 dan KOREKSI 20:
  - TIDAK ADA ambang kardinalitas. Tidak ada sebaran yang disatukan sebagian.
  - Setiap daftar yang dipotong WAJIB mengumumkan `*_dipotong` dan `*_penyebut`
    (aturan 86 (b)).
  - TIDAK memakai pola regex simbol untuk apa pun yang mengikat. KOREKSI 20
    membuktikan pola itu menolak ticker satu huruf yang sah.

Modul ini BUKAN bukti sampai laporannya lahir dari GitHub Actions (aturan 38).
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import sys
from collections import Counter
from datetime import datetime, timezone

VERSI = 1
KELUARAN = "reports/sumber_funding.json"

KANDIDAT = (
    "funding_semesta",
    "silang_funding",
    "hidup_tanpa_funding",
    "kehidupan",
    "semesta_bulan_1m",
)

SIMBOL_LIMA = ("BNXUSDT", "ICPUSDT", "JUPUSDT", "QTUMUSDT", "TLMUSDT")

# Angka tercatat yang WAJIB didamaikan, bukan diandaikan.
CACAH_33 = 33
CACAH_SIMBOL = 787
PENYEBUT_LOLOS = 19586
PENYEBUT_SEMESTA = 19598
ENAM_SEL = (18054, 33, 559, 842, 96, 2)
JUMLAH_ENAM_SEL_TERCATAT = 19586

KARDINALITAS_PENTING = (CACAH_33, CACAH_SIMBOL, PENYEBUT_LOLOS, PENYEBUT_SEMESTA)

BATAS_DAFTAR = 80
BATAS_KEDALAMAN = 7

AKAR = pathlib.Path(__file__).resolve().parents[2]


def sidik_kode() -> str:
    return hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()


def _jalur(nama: str) -> pathlib.Path:
    calon = pathlib.Path("reports/%s.json" % nama)
    if not calon.exists():
        calon = AKAR / "reports" / ("%s.json" % nama)
    return calon


def _potong(barang, batas=BATAS_DAFTAR):
    """Potong SECARA TERBUKA. Kembalikan (daftar, dipotong, penyebut)."""
    barang = list(barang)
    penyebut = len(barang)
    return barang[:batas], bool(penyebut > batas), penyebut


class Jelajah:
    """Menyusuri struktur JSON sekali jalan dan memungut segalanya sekaligus."""

    def __init__(self):
        self.wadah = []            # (jalur, tipe, kardinalitas)
        self.kedalaman_terpotong = 0
        self.cacah_simbol_nilai = Counter()
        self.cacah_simbol_kunci = Counter()
        self.simbol_dalam_wadah_33 = Counter()
        self.bilangan = Counter()  # nilai bulat -> berapa kali muncul
        self.jalur_bilangan = {}   # nilai bulat -> daftar jalur

    def _catat_bilangan(self, nilai, jalur):
        if isinstance(nilai, bool) or not isinstance(nilai, int):
            return
        self.bilangan[nilai] += 1
        if nilai in ENAM_SEL or nilai in KARDINALITAS_PENTING:
            self.jalur_bilangan.setdefault(nilai, [])
            if len(self.jalur_bilangan[nilai]) < BATAS_DAFTAR:
                self.jalur_bilangan[nilai].append(jalur)

    def jalan(self, simpul, jalur="", kedalaman=0, dalam_33=False):
        if kedalaman > BATAS_KEDALAMAN:
            self.kedalaman_terpotong += 1
            return

        if isinstance(simpul, dict):
            n = len(simpul)
            self.wadah.append((jalur or ".", "peta", n))
            di33 = dalam_33 or (n == CACAH_33)
            for kunci, nilai in simpul.items():
                teks = str(kunci)
                if teks in SIMBOL_LIMA:
                    self.cacah_simbol_kunci[teks] += 1
                    if di33:
                        self.simbol_dalam_wadah_33[teks] += 1
                self.jalan(nilai, "%s.%s" % (jalur, teks), kedalaman + 1, di33)
            return

        if isinstance(simpul, list):
            n = len(simpul)
            self.wadah.append((jalur or ".", "larik", n))
            di33 = dalam_33 or (n == CACAH_33)
            for i, nilai in enumerate(simpul):
                self.jalan(nilai, "%s[]" % jalur, kedalaman + 1, di33)
            return

        if isinstance(simpul, str):
            if simpul in SIMBOL_LIMA:
                self.cacah_simbol_nilai[simpul] += 1
                if dalam_33:
                    self.simbol_dalam_wadah_33[simpul] += 1
            return

        self._catat_bilangan(simpul, jalur)


def _periksa(nama: str) -> dict:
    jalur = _jalur(nama)
    if not jalur.exists():
        return {"ada": False, "jalur_dicoba": str(jalur)}

    byte = jalur.stat().st_size
    try:
        muatan = json.loads(jalur.read_text())
    except Exception as galat:  # noqa: BLE001
        return {"ada": True, "byte": byte, "galat": "%s: %s" % (type(galat).__name__, galat)}

    j = Jelajah()
    j.jalan(muatan)

    if isinstance(muatan, dict):
        tipe_puncak = "peta"
        kunci_puncak, kp_dipotong, kp_penyebut = _potong(sorted(str(k) for k in muatan))
    elif isinstance(muatan, list):
        tipe_puncak = "larik"
        kunci_puncak, kp_dipotong, kp_penyebut = [], False, 0
    else:
        tipe_puncak = type(muatan).__name__
        kunci_puncak, kp_dipotong, kp_penyebut = [], False, 0

    w33 = [
        {"jalur": p, "tipe": t, "kardinalitas": n}
        for (p, t, n) in j.wadah
        if n == CACAH_33
    ]
    daftar_33, d33_dipotong, d33_penyebut = _potong(w33)

    penting = [
        {"jalur": p, "tipe": t, "kardinalitas": n}
        for (p, t, n) in j.wadah
        if n in KARDINALITAS_PENTING
    ]
    daftar_penting, dp_dipotong, dp_penyebut = _potong(penting)

    kardinalitas_maks = max((n for (_, _, n) in j.wadah), default=0)
    kardinalitas_funding = [
        n for (p, _, n) in j.wadah if "funding" in p.lower()
    ]

    sebaran_kardinalitas = Counter(n for (_, _, n) in j.wadah)
    teratas, sk_dipotong, sk_penyebut = _potong(
        [
            {"kardinalitas": k, "cacah_wadah": v}
            for k, v in sorted(sebaran_kardinalitas.items(), key=lambda x: (-x[1], -x[0]))
        ],
        40,
    )

    cacah_lima = {
        s: j.cacah_simbol_nilai.get(s, 0) + j.cacah_simbol_kunci.get(s, 0)
        for s in SIMBOL_LIMA
    }

    return {
        "ada": True,
        "byte": byte,
        "tipe_puncak": tipe_puncak,
        "kardinalitas_puncak": len(muatan) if isinstance(muatan, (dict, list)) else None,
        "kunci_puncak": kunci_puncak,
        "kunci_puncak_dipotong": kp_dipotong,
        "kunci_puncak_penyebut": kp_penyebut,
        "cacah_wadah": len(j.wadah),
        "kedalaman_terpotong": j.kedalaman_terpotong,
        "kardinalitas_maksimum": kardinalitas_maks,
        "kardinalitas_maksimum_funding": max(kardinalitas_funding, default=0),
        "wadah_panjang_33": daftar_33,
        "wadah_panjang_33_dipotong": d33_dipotong,
        "wadah_panjang_33_penyebut": d33_penyebut,
        "wadah_penting": daftar_penting,
        "wadah_penting_dipotong": dp_dipotong,
        "wadah_penting_penyebut": dp_penyebut,
        "sebaran_kardinalitas_teratas": teratas,
        "sebaran_kardinalitas_dipotong": sk_dipotong,
        "sebaran_kardinalitas_penyebut": sk_penyebut,
        "cacah_lima_simbol": cacah_lima,
        "cacah_lima_simbol_jumlah": sum(cacah_lima.values()),
        "cacah_lima_simbol_sebagai_kunci": dict(j.cacah_simbol_kunci),
        "cacah_lima_simbol_sebagai_nilai": dict(j.cacah_simbol_nilai),
        "cacah_lima_simbol_dalam_wadah_33": dict(j.simbol_dalam_wadah_33),
        "cacah_enam_sel": {str(v): j.bilangan.get(v, 0) for v in ENAM_SEL},
        "jalur_enam_sel": {
            str(v): j.jalur_bilangan.get(v, []) for v in ENAM_SEL
        },
        "cacah_kardinalitas_penting_sebagai_bilangan": {
            str(v): j.bilangan.get(v, 0) for v in KARDINALITAS_PENTING
        },
    }


def jalankan() -> dict:
    kandidat = {nama: _periksa(nama) for nama in KANDIDAT}

    jangkauan = max(
        (k.get("kardinalitas_maksimum_funding", 0) for k in kandidat.values() if k.get("ada")),
        default=0,
    )

    hilang = sorted(n for n, k in kandidat.items() if not k.get("ada"))
    bergalat = sorted(n for n, k in kandidat.items() if k.get("galat"))

    htf = kandidat.get("hidup_tanpa_funding", {})
    sf = kandidat.get("silang_funding", {})
    fs = kandidat.get("funding_semesta", {})

    enam_ditemukan = {
        str(v): any(
            k.get("cacah_enam_sel", {}).get(str(v), 0) > 0
            for k in kandidat.values()
            if k.get("ada")
        )
        for v in ENAM_SEL
    }

    silang = {
        "enam_sel_tercatat": list(ENAM_SEL),
        "jumlah_enam_sel": sum(ENAM_SEL),
        "jumlah_enam_sel_tercatat": JUMLAH_ENAM_SEL_TERCATAT,
        "jumlah_cocok_19586": sum(ENAM_SEL) == JUMLAH_ENAM_SEL_TERCATAT,
        "enam_sel_ditemukan_di_mana_pun": enam_ditemukan,
        "enam_sel_lengkap": all(enam_ditemukan.values()),
        "cacah_enam_sel_di_silang_funding": sf.get("cacah_enam_sel", {}),
    }

    ringkas = {
        "hidup_tanpa_funding_punya_wadah_33": bool(htf.get("wadah_panjang_33")),
        "hidup_tanpa_funding_cacah_wadah_33": htf.get("wadah_panjang_33_penyebut", 0),
        "funding_semesta_tipe_puncak": fs.get("tipe_puncak"),
        "funding_semesta_punya_wadah_787": any(
            w.get("kardinalitas") == CACAH_SIMBOL for w in fs.get("wadah_penting", [])
        ),
        "jangkauan_kurang_dari_semesta": jangkauan < PENYEBUT_SEMESTA,
        "jangkauan_sama_dengan_lolos": jangkauan == PENYEBUT_LOLOS,
    }

    return {
        "versi_sumber_funding": VERSI,
        "bukan_bukti": False,
        "waktu_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "sidik_kode": sidik_kode(),
        "kandidat_diperiksa": list(KANDIDAT),
        "kandidat_hilang": hilang,
        "kandidat_bergalat": bergalat,
        "jangkauan_maksimum_funding": jangkauan,
        "silang": silang,
        "ringkas": ringkas,
        "kandidat": kandidat,
    }


def kode_keluar(hasil: dict) -> int:
    if hasil.get("kandidat_hilang"):
        return 2
    if hasil.get("kandidat_bergalat"):
        return 3
    return 0


def main() -> int:
    hasil = jalankan()
    keluaran = pathlib.Path(KELUARAN)
    keluaran.parent.mkdir(parents=True, exist_ok=True)
    keluaran.write_text(
        json.dumps(hasil, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    )

    print("kandidat_hilang=%s" % hasil["kandidat_hilang"])
    print("kandidat_bergalat=%s" % hasil["kandidat_bergalat"])
    print("jangkauan_maksimum_funding=%s" % hasil["jangkauan_maksimum_funding"])
    for nama in KANDIDAT:
        k = hasil["kandidat"][nama]
        if not k.get("ada"):
            print("%s: TIDAK ADA" % nama)
            continue
        print(
            "%s: puncak=%s kard_puncak=%s wadah=%s maks=%s maks_funding=%s w33=%s"
            % (
                nama,
                k.get("tipe_puncak"),
                k.get("kardinalitas_puncak"),
                k.get("cacah_wadah"),
                k.get("kardinalitas_maksimum"),
                k.get("kardinalitas_maksimum_funding"),
                k.get("wadah_panjang_33_penyebut"),
            )
        )
    print("lima_simbol_htf=%s" % json.dumps(
        hasil["kandidat"].get("hidup_tanpa_funding", {}).get("cacah_lima_simbol", {}),
        sort_keys=True,
    ))
    print("byte_laporan=%s" % keluaran.stat().st_size)

    kode = kode_keluar(hasil)
    print("kode_keluar=%s" % kode)
    return kode


if __name__ == "__main__":
    sys.exit(main())
