"""Diagnosa KC-15 tepi bulan — apakah pemotongan tepi LOLOS gerbang tanpa jejak?

KC-15 terbukti pada jurnal 51: berkas klines BULANAN dapat kehilangan hari UTC
penuh yang datanya utuh di berkas HARIAN (BNXUSDT 2022-04, 2022-06, 2022-08;
7.200 menit). Lubang di TENGAH bulan selalu ditangkap gerbang lewat klausa
`tanpa_menit_hilang`.

Yang belum terukur adalah TEPI. `gerbang_1m.ukur_deret` menghitung
`menit_hilang_dalam_rentang` dari stempel pertama sampai terakhir yang
benar-benar ada di berkas. Itu keputusan rancangan yang benar dan tertulis di
docstring-nya: bulan pertama sebuah simbol memang mulai di tengah bulan. Tetapi
untuk bulan TENGAH — bulan yang punya tetangga sebelum dan sesudahnya — gerbang
tidak punya cara membedakan "memang mulai belakangan" dari "dipotong perakit
arsip". Bila KC-15 bisa melenyapkan lima hari di tengah, tidak ada alasan
menganggapnya tidak bisa melenyapkan beberapa jam di tepi.

Modul ini mengukurnya: menit kalender bulan dikurangi rentang yang benar-benar
ada memberi `tepi_awal` dan `tepi_akhir`; lalu berkas HARIAN tanggal pertama dan
terakhir bulan itu diunduh untuk melihat apakah menit tepi itu ADA di harian.

Petunjuk kuat yang memicu run ini: BNXUSDT 2022-04 punya 41.550 baris + 1.440
menit lubang = 42.990, sedangkan April punya 43.200 menit. Selisih 210 menit
(14×15) ada di tepi dan tidak terlihat gerbang maupun penghitung lubang.

Bulan pertama dan terakhir hidup tiap simbol DIKECUALIKAN dari putusan, tetapi
tetap dicacah (aturan 28, 30). Medan penggugur: `menit_tepi_hadir_di_harian`
dilaporkan walau nol, dan `cacah_gerbang_lolos_padahal_tepi_terpotong` adalah
angka yang membatalkan klaim "gerbang cukup" (aturan 24).

Aturan yang ditegakkan: 20, 21, 24, 28, 30, 32, 36, 37.
"""

from __future__ import annotations

import calendar
import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

from . import arsip, gerbang_1m, klines, pecahan, serap
from . import diagnosa_kc14 as k14
from .diagnosa_kc14b import url_harian

KELUARAN = "reports/diagnosa_kc15.json"
MS_MENIT = 60_000
MENIT_SEHARI = 1440
BATAS_CONTOH = 20
# Lima simbol per pecahan, delapan pecahan = 40 bulan tengah (R-118).
SIMBOL_PER_PECAHAN = 5
TOTAL_PECAHAN = pecahan.TOTAL_PECAHAN

# Tersangka tepi yang memicu run ini, diperiksa apa pun hasil pencuplikan.
TERSANGKA_TEPI: Tuple[Tuple[str, str], ...] = (("BNXUSDT", "2022-04"),)


def sidik_kode() -> str:
    h = hashlib.sha256()
    dasar = Path(__file__).parent
    for nama in sorted(
        [
            "diagnosa_kc15.py",
            "diagnosa_kc14.py",
            "diagnosa_kc14b.py",
            "arsip.py",
            "klines.py",
            "gerbang_1m.py",
            "pecahan.py",
            "serap.py",
        ]
    ):
        h.update((dasar / nama).read_bytes())
    return h.hexdigest()


def menit_kalender(bulan: str) -> int:
    """Menit dalam satu bulan kalender UTC, dari calendar.monthrange."""
    tahun, bln = (int(x) for x in bulan.split("-"))
    return calendar.monthrange(tahun, bln)[1] * MENIT_SEHARI


def awal_bulan_ms(bulan: str) -> int:
    tahun, bln = (int(x) for x in bulan.split("-"))
    return int(
        dt.datetime(tahun, bln, 1, tzinfo=dt.timezone.utc).timestamp() * 1000
    )


def tanggal_tepi(bulan: str) -> Tuple[str, str]:
    tahun, bln = (int(x) for x in bulan.split("-"))
    akhir = calendar.monthrange(tahun, bln)[1]
    return f"{bulan}-01", f"{bulan}-{akhir:02d}"


def ukur_tepi(bulan: str, pertama_ms: int, terakhir_ms: int) -> Dict[str, int]:
    """Menit yang absen SEBELUM stempel pertama dan SESUDAH stempel terakhir."""
    awal = awal_bulan_ms(bulan)
    akhir = awal + menit_kalender(bulan) * MS_MENIT  # eksklusif
    tepi_awal = max(0, (int(pertama_ms) - awal) // MS_MENIT)
    tepi_akhir = max(0, (akhir - MS_MENIT - int(terakhir_ms)) // MS_MENIT)
    return {
        "tepi_awal": tepi_awal,
        "tepi_akhir": tepi_akhir,
        "tepi_total": tepi_awal + tepi_akhir,
    }


def posisi_bulan(bulan: str, daftar: Sequence[str]) -> str:
    urut = sorted(daftar)
    if not urut or bulan not in urut:
        return "tak_dikenal"
    if bulan == urut[0]:
        return "pertama"
    if bulan == urut[-1]:
        return "terakhir"
    return "tengah"


def bulan_tengah_terpilih(daftar: Sequence[str]) -> str:
    """Bulan tengah deterministik: median daftar tanpa ujung-ujungnya."""
    tengah = sorted(daftar)[1:-1]
    if not tengah:
        return ""
    return tengah[len(tengah) // 2]


def kelas_simbol(isi: Dict[str, Any], simbol: str) -> List[str]:
    """Kelas risiko yang melekat pada SIMBOL, belum pada bulannya."""
    kelas: List[str] = []
    pertama = str(isi.get("bulan_pertama") or "")
    terakhir = str(isi.get("bulan_terakhir") or "")
    if pertama and pertama < serap.BATAS_HEADER:
        kelas.append("pra_header")
    if terakhir and terakhir < serap.BATAS_HIDUP:
        kelas.append("terhenti")
    if pertama and pertama >= serap.BATAS_BARU:
        kelas.append("kendali_baru")
    if serap.non_ascii(simbol):
        kelas.append("non_ascii")
    return kelas


def kelas_dengan_bulan(kelas: Sequence[str], bulan: str) -> List[str]:
    """Tambahkan kelas yang hanya bisa ditentukan oleh BULAN yang dipilih.

    Tanpa ini `bulan_awal_2020_2021` akan selalu dilaporkan KOSONG walau bulan
    pra-2022 benar-benar tersampel — laporan kelas kosong yang bohong justru
    yang dilarang aturan 37.
    """
    hasil = list(kelas)
    if bulan and bulan < serap.BATAS_HEADER and "bulan_awal_2020_2021" not in hasil:
        hasil.append("bulan_awal_2020_2021")
    return hasil


def pilih_simbol(
    rentang: Dict[str, Any], simbol: Sequence[str], banyak: int = SIMBOL_PER_PECAHAN
) -> List[str]:
    """Pilih simbol berlapis dari satu pecahan: kelas risiko wajib terwakili.

    Deterministik: di dalam tiap lapis kandidat diurut abjad dan yang pertama
    diambil (aturan 37, penangkal KC-13).
    """
    urut = sorted(simbol)
    kelas_dari = {s: kelas_simbol(rentang.get(s) or {}, s) for s in urut}
    terpilih: List[str] = []

    def tambah(nama: str) -> None:
        if nama and nama not in terpilih and len(terpilih) < banyak:
            terpilih.append(nama)

    for wajib in ("non_ascii", "pra_header", "terhenti", "kendali_baru"):
        for s in urut:
            if wajib in kelas_dari[s]:
                tambah(s)
                break
    for s in urut:
        tambah(s)
    return terpilih


def periksa_hari_tepi(
    simbol: str, tanggal: str, dicari: Sequence[int]
) -> Dict[str, Any]:
    catatan: Dict[str, Any] = {"tanggal": tanggal, "menit_tepi_dicari": len(dicari)}
    url = url_harian(simbol, "1m", tanggal)
    catatan["url"] = url
    try:
        data = arsip.unduh_terverifikasi(url)
    except Exception as exc:  # noqa: BLE001
        catatan["tersedia"] = False
        catatan["sebab"] = str(exc)[:200]
        return catatan
    catatan["tersedia"] = True
    catatan["checksum"] = arsip.sha256_bytes(data)
    df, dibuang = klines.rapikan(klines.baca_zip(data, teks=True))
    stempel = set(int(x) for x in df["open_time"].tolist())
    hadir = sorted(int(t) for t in dicari if int(t) in stempel)
    catatan["cacah_baris_harian"] = len(stempel)
    catatan["baris_dibuang"] = int(dibuang)
    catatan["menit_tepi_hadir"] = len(hadir)
    catatan["contoh_menit_hadir"] = hadir[:BATAS_CONTOH]
    return catatan


def periksa_satu(
    simbol: str, bulan: str, indeks: int, kelas: Sequence[str], bulan_arsip: Sequence[str]
) -> Dict[str, Any]:
    catatan: Dict[str, Any] = {
        "simbol": simbol,
        "bulan": bulan,
        "pecahan": indeks,
        "kelas": kelas_dengan_bulan(kelas, bulan),
        "bulan_pertama_arsip": (sorted(bulan_arsip)[0] if bulan_arsip else ""),
        "bulan_terakhir_arsip": (sorted(bulan_arsip)[-1] if bulan_arsip else ""),
        "posisi": posisi_bulan(bulan, bulan_arsip),
        "menit_kalender": menit_kalender(bulan),
    }
    url = arsip.url_klines(simbol, "1m", bulan)
    catatan["url_bulanan"] = url
    try:
        data = arsip.unduh_terverifikasi(url)
    except Exception as exc:  # noqa: BLE001
        catatan["bulanan_tersedia"] = False
        catatan["sebab"] = str(exc)[:200]
        catatan["putusan"] = "TIDAK MENGUKUR"
        return catatan

    catatan["bulanan_tersedia"] = True
    catatan["checksum_bulanan"] = arsip.sha256_bytes(data)
    stempel = k14.stempel_dari_zip(data)
    if not stempel:
        catatan["putusan"] = "TIDAK MENGUKUR"
        catatan["cacah_baris_1m"] = 0
        return catatan

    urut = sorted(int(t) for t in stempel)
    hilang = k14.menit_hilang(urut)
    putusan_gerbang = gerbang_1m.nilai_deret(urut, simbol, bulan)
    tepi = ukur_tepi(bulan, urut[0], urut[-1])

    catatan["cacah_baris_1m"] = len(urut)
    catatan["menit_hilang_di_tengah"] = len(hilang)
    catatan["gerbang_lolos"] = bool(putusan_gerbang["lolos"])
    catatan["gerbang_pelanggaran"] = list(putusan_gerbang["pelanggaran"])
    catatan["stempel_pertama_ms"] = urut[0]
    catatan["stempel_terakhir_ms"] = urut[-1]
    catatan.update(tepi)
    # Uji silang aritmetika (aturan 21): baris + tengah + tepi wajib = kalender.
    catatan["jumlah_terpertanggungjawabkan"] = (
        len(urut) + len(hilang) + tepi["tepi_total"]
    )
    catatan["selisih_tak_terjelaskan"] = catatan["menit_kalender"] - catatan[
        "jumlah_terpertanggungjawabkan"
    ]

    awal = awal_bulan_ms(bulan)
    akhir_eksklusif = awal + catatan["menit_kalender"] * MS_MENIT
    menit_awal = [awal + i * MS_MENIT for i in range(tepi["tepi_awal"])]
    menit_akhir = [
        urut[-1] + (i + 1) * MS_MENIT
        for i in range(tepi["tepi_akhir"])
        if urut[-1] + (i + 1) * MS_MENIT < akhir_eksklusif
    ]

    tanggal_awal, tanggal_akhir = tanggal_tepi(bulan)
    rincian_hari: List[Dict[str, Any]] = []
    if menit_awal:
        rincian_hari.append(periksa_hari_tepi(simbol, tanggal_awal, menit_awal))
    if menit_akhir:
        rincian_hari.append(periksa_hari_tepi(simbol, tanggal_akhir, menit_akhir))

    catatan["harian"] = rincian_hari
    terukur = [h for h in rincian_hari if h.get("tersedia")]
    catatan["hari_tepi_diperiksa"] = len(terukur)
    catatan["hari_tepi_tidak_tersedia"] = sum(
        1 for h in rincian_hari if h.get("tersedia") is False
    )
    hadir = sum(int(h.get("menit_tepi_hadir", 0)) for h in terukur)
    catatan["menit_tepi_hadir_di_harian"] = hadir
    catatan["putusan"] = putusan_tepi(tepi["tepi_total"], hadir, len(terukur))
    return catatan


def putusan_tepi(tepi_total: int, hadir: int, hari_terukur: int) -> str:
    if tepi_total == 0:
        return "TEPI_BERSIH"
    if hari_terukur == 0:
        return "TIDAK MENGUKUR"
    if hadir > 0:
        return "TEPI_TERPOTONG"
    return "TEPI_TAK_TERJELASKAN"


def ringkas(catatan: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    diperiksa = [c for c in catatan if c.get("bulanan_tersedia") and c.get("cacah_baris_1m")]
    tengah = [c for c in diperiksa if c.get("posisi") == "tengah"]
    putusan = [c.get("putusan") for c in catatan]
    kelas_cacah: Dict[str, int] = {nama: 0 for nama in serap.KELAS_RISIKO}
    for c in diperiksa:
        for nama in c.get("kelas") or []:
            if nama in kelas_cacah:
                kelas_cacah[nama] += 1
    return {
        "status": "TERUKUR" if tengah else "TIDAK MENGUKUR",
        "bulan_diminta": len(catatan),
        "bulan_diperiksa": len(diperiksa),
        "bulan_tengah_diperiksa": len(tengah),
        "cacah_bulan_pertama_dikecualikan": sum(
            1 for c in diperiksa if c.get("posisi") == "pertama"
        ),
        "cacah_bulan_terakhir_dikecualikan": sum(
            1 for c in diperiksa if c.get("posisi") == "terakhir"
        ),
        "cacah_bulan_tepi_tak_nol": sum(1 for c in tengah if int(c.get("tepi_total") or 0)),
        "total_menit_tepi": sum(int(c.get("tepi_total") or 0) for c in tengah),
        "menit_tepi_hadir_di_harian": sum(
            int(c.get("menit_tepi_hadir_di_harian") or 0) for c in tengah
        ),
        "hari_tepi_diperiksa": sum(int(c.get("hari_tepi_diperiksa") or 0) for c in diperiksa),
        "cacah_hari_tepi_tidak_tersedia": sum(
            int(c.get("hari_tepi_tidak_tersedia") or 0) for c in diperiksa
        ),
        "cacah_gerbang_lolos_padahal_tepi_terpotong": sum(
            1
            for c in tengah
            if c.get("gerbang_lolos") and int(c.get("menit_tepi_hadir_di_harian") or 0) > 0
        ),
        "cacah_selisih_tak_terjelaskan": sum(
            1 for c in diperiksa if int(c.get("selisih_tak_terjelaskan") or 0) != 0
        ),
        "cacah_tepi_bersih": putusan.count("TEPI_BERSIH"),
        "cacah_tepi_terpotong": putusan.count("TEPI_TERPOTONG"),
        "cacah_tepi_tak_terjelaskan": putusan.count("TEPI_TAK_TERJELASKAN"),
        "cacah_tidak_mengukur": putusan.count("TIDAK MENGUKUR"),
        "kelas_risiko_tersentuh": kelas_cacah,
        "kelas_risiko_kosong": [n for n, v in kelas_cacah.items() if not v],
        "catatan_penggugur": (
            "cacah_gerbang_lolos_padahal_tepi_terpotong > 0 berarti gerbang "
            "meloloskan simbol-bulan yang datanya benar-benar terpotong di tepi, "
            "dan enam klausa ADR-A004 tidak cukup (aturan 24)"
        ),
        "catatan_pengecualian": (
            "bulan pertama dan terakhir hidup tiap simbol dikecualikan dari putusan "
            "karena parsialnya sah, tetapi tetap dicacah agar tidak hilang dari "
            "penyebut (aturan 28, 30)"
        ),
        "catatan_rentang": (
            "sampel bulan tengah dari kedelapan pecahan; kesimpulan tidak boleh "
            "diperluas ke 19.598 simbol-bulan (aturan 20)"
        ),
    }


def jalankan(akar: str = ".") -> Dict[str, Any]:
    from ..semesta import taksonomi

    basis = Path(akar)
    mentah = (basis / serap.SUMBER_RENTANG).read_bytes()
    rentang = json.loads(mentah.decode("utf-8")).get("rentang", {})
    if not isinstance(rentang, dict):
        rentang = {}

    tugas: List[Tuple[str, str, int, List[str], List[str]]] = []
    singgah: Dict[str, List[str]] = {}

    def bulan_arsip(nama: str) -> List[str]:
        if nama not in singgah:
            try:
                singgah[nama] = sorted(arsip.bulan_tersedia(nama))
            except Exception:  # noqa: BLE001
                singgah[nama] = []
        return singgah[nama]

    for simbol, bulan in TERSANGKA_TEPI:
        tugas.append(
            (simbol, bulan, -1, kelas_simbol(rentang.get(simbol) or {}, simbol), bulan_arsip(simbol))
        )

    for indeks in range(TOTAL_PECAHAN):
        milik = pecahan.simbol_pecahan(
            rentang, taksonomi.jenis_instrumen, indeks, TOTAL_PECAHAN
        )
        for simbol in pilih_simbol(rentang, milik):
            daftar = bulan_arsip(simbol)
            bulan = bulan_tengah_terpilih(daftar)
            if not bulan:
                continue
            if any(t[0] == simbol and t[1] == bulan for t in tugas):
                continue
            tugas.append(
                (simbol, bulan, indeks, kelas_simbol(rentang.get(simbol) or {}, simbol), daftar)
            )

    catatan = [periksa_satu(s, b, i, k, d) for s, b, i, k, d in tugas]
    laporan = ringkas(catatan)
    laporan["bukan_bukti"] = False
    laporan["tersangka_tepi"] = [f"{s} {b}" for s, b in TERSANGKA_TEPI]
    laporan["cakupan_disampel"] = [f"{s}:{b}" for s, b, _, _, _ in tugas]
    laporan["rincian"] = catatan
    laporan["sumber_rentang"] = serap.SUMBER_RENTANG
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
    print(
        json.dumps(
            {k: v for k, v in hasil.items() if k != "rincian"},
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
