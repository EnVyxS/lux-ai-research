"""Uji struktural: menegakkan aturan repo, bukan menilai strategi.

Catatan cacat KC-3: versi pertama uji pemisahan antarmuka memakai pencarian
kata (`"antarmuka" in isi`). Guard itu tidak bisa membedakan IMPOR dari
KALIMAT TENTANG impor, dan ia menjatuhkan CI pada run pertama (run 30311582627)
karena docstring `lux_ai/backtest/__init__.py` menyebut kata itu. Penggantinya
mengukur impor lewat AST, dan cara pengukurannya sendiri diuji di bawah.
"""
import ast
import pathlib

AKAR = pathlib.Path(__file__).resolve().parents[1]

BERKAS_KONTINUITAS = [
    "PROMPT_KELANJUTAN.md",
    "README.md",
    "STATE.md",
    "STATE_LAMPIRAN.md",
    "STATE_LAMPIRAN_ANGKA.md",
    "requirements.txt",
]

PAKET = "lux_ai"
TERLARANG = "antarmuka"


def modul_yang_diimpor(sumber: str) -> set:
    """Himpunan nama modul yang benar-benar DIIMPOR oleh sebuah sumber Python.

    Hanya simpul Import dan ImportFrom yang dihitung. Komentar, docstring, dan
    string biasa tidak dihitung. Impor relatif (level > 0) diselesaikan oleh
    pemanggil; di sini nama relatif dikembalikan apa adanya dengan awalan titik.
    """
    nama = set()
    for simpul in ast.walk(ast.parse(sumber)):
        if isinstance(simpul, ast.Import):
            for alias in simpul.names:
                nama.add(alias.name)
        elif isinstance(simpul, ast.ImportFrom):
            dasar = simpul.module or ""
            if simpul.level:
                dasar = "." * simpul.level + dasar
            nama.add(dasar)
            for alias in simpul.names:
                nama.add((dasar + "." + alias.name) if dasar else alias.name)
    return nama


def menyentuh_antarmuka(sumber: str) -> bool:
    """True bila sumber mengimpor paket antarmuka, betapa pun ia menuliskannya."""
    for nama in modul_yang_diimpor(sumber):
        if TERLARANG in nama.strip(".").split("."):
            return True
    return False


# --------------------------------------------------------------------------
# Uji atas CARA MENGUKUR (bukan hanya atas niat guard). Lihat KC-3.
# --------------------------------------------------------------------------

def test_pengukur_membedakan_impor_dari_kalimat_tentang_impor():
    docstring_saja = '"""Dilarang mengimpor lux_ai.antarmuka, langsung maupun transitif."""\n'
    komentar_saja = "# jangan pernah import lux_ai.antarmuka di sini\nx = 1\n"
    string_biasa = 'pesan = "lux_ai.antarmuka"\n'
    assert not menyentuh_antarmuka(docstring_saja)
    assert not menyentuh_antarmuka(komentar_saja)
    assert not menyentuh_antarmuka(string_biasa)


def test_pengukur_menangkap_impor_sungguhan_dalam_berbagai_bentuk():
    assert menyentuh_antarmuka("import lux_ai.antarmuka\n")
    assert menyentuh_antarmuka("from lux_ai.antarmuka import apa_saja\n")
    assert menyentuh_antarmuka("from lux_ai import antarmuka\n")
    assert menyentuh_antarmuka("from . import antarmuka\n")
    assert menyentuh_antarmuka("import lux_ai.antarmuka as a\n")
    assert menyentuh_antarmuka("def f():\n    import lux_ai.antarmuka\n")
    assert not menyentuh_antarmuka("import numpy as np\nfrom lux_ai import serapan\n")


# --------------------------------------------------------------------------
# Uji aturan repo
# --------------------------------------------------------------------------

def test_berkas_kontinuitas_ada_dan_tidak_kosong():
    for nama in BERKAS_KONTINUITAS:
        p = AKAR / nama
        assert p.is_file(), f"hilang: {nama}"
        assert p.stat().st_size > 0, f"kosong: {nama}"


def test_tidak_ada_skrip_main_di_akar():
    for p in AKAR.glob("*.py"):
        assert "__main__" not in p.read_text(encoding="utf-8"), (
            f"skrip __main__ di akar: {p.name}"
        )


def test_tidak_ada_berkas_kode_baru_melebihi_800_baris():
    for p in (AKAR / PAKET).rglob("*.py"):
        n = len(p.read_text(encoding="utf-8").splitlines())
        assert n <= 800, f"{p.relative_to(AKAR)} = {n} baris"


def test_backtest_dan_sinyal_tidak_mengimpor_antarmuka():
    for sub in ("backtest", "sinyal"):
        direktori = AKAR / PAKET / sub
        if not direktori.is_dir():
            continue
        for p in direktori.rglob("*.py"):
            sumber = p.read_text(encoding="utf-8")
            assert not menyentuh_antarmuka(sumber), (
                f"{p.relative_to(AKAR)} mengimpor {TERLARANG}"
            )


def test_tak_ada_modul_lux_ai_yang_mengimpor_antarmuka_secara_transitif():
    """Penegakan transitif: bangun graf impor internal, lalu telusuri tutupannya.

    Selama paket masih kerangka, graf ini kosong dan uji lolos secara trivial.
    Ia menjadi bergigi begitu modul nyata masuk.
    """
    graf = {}
    for p in (AKAR / PAKET).rglob("*.py"):
        modul = ".".join(p.relative_to(AKAR).with_suffix("").parts)
        if modul.endswith(".__init__"):
            modul = modul[: -len(".__init__")]
        tetangga = set()
        for nama in modul_yang_diimpor(p.read_text(encoding="utf-8")):
            if nama.startswith(PAKET + ".") or nama == PAKET:
                tetangga.add(nama)
        graf[modul] = tetangga

    def tercemar(awal):
        dilihat, tumpukan = set(), [awal]
        while tumpukan:
            m = tumpukan.pop()
            if m in dilihat:
                continue
            dilihat.add(m)
            for t in graf.get(m, ()):
                if TERLARANG in t.split("."):
                    return True
                tumpukan.append(t)
        return False

    for sub in ("backtest", "sinyal"):
        akar_sub = f"{PAKET}.{sub}"
        for modul in graf:
            if modul == akar_sub or modul.startswith(akar_sub + "."):
                assert not tercemar(modul), f"{modul} mencapai {TERLARANG} secara transitif"
