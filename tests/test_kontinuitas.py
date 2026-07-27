"""Uji struktural: menegakkan aturan repo, bukan menilai strategi."""
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


def test_berkas_kontinuitas_ada_dan_tidak_kosong():
    for nama in BERKAS_KONTINUITAS:
        p = AKAR / nama
        assert p.is_file(), f"hilang: {nama}"
        assert p.stat().st_size > 0, f"kosong: {nama}"


def test_tidak_ada_skrip_main_di_akar():
    for p in AKAR.glob("*.py"):
        isi = p.read_text(encoding="utf-8")
        assert "__main__" not in isi, f"skrip __main__ di akar: {p.name}"


def test_tidak_ada_berkas_kode_baru_melebihi_800_baris():
    for p in (AKAR / "lux_ai").rglob("*.py"):
        n = len(p.read_text(encoding="utf-8").splitlines())
        assert n <= 800, f"{p.relative_to(AKAR)} = {n} baris"


def test_backtest_dan_sinyal_tidak_menyentuh_antarmuka():
    for sub in ("backtest", "sinyal"):
        direktori = AKAR / "lux_ai" / sub
        if not direktori.is_dir():
            continue
        for p in direktori.rglob("*.py"):
            isi = p.read_text(encoding="utf-8")
            assert "antarmuka" not in isi, f"{p.relative_to(AKAR)} menyebut antarmuka"
