"""Pembacaan CSV klines arsip dan penulisan parquet kanonik.

Jebakan yang ditangani di sini: arsip Binance MENGUBAH formatnya di tengah
sejarah. Berkas lama tidak punya baris header, berkas yang lebih baru punya.
Membaca keduanya dengan satu aturan tetap akan menelan baris header sebagai
data atau membuang satu baris nyata. Deteksi dilakukan atas isi, bukan tanggal.
"""
from __future__ import annotations

import io
import zipfile
from pathlib import Path

import pandas as pd

KOLOM = [
    "open_time",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "close_time",
    "quote_volume",
    "trades",
    "taker_buy_base",
    "taker_buy_quote",
    "ignore",
]

KOLOM_SIMPAN = KOLOM[:-1]


def punya_header(baris_pertama: str) -> bool:
    """True bila baris pertama adalah header, bukan data.

    Diukur dari isi: sel pertama data selalu stempel waktu berupa angka.
    """
    sel = baris_pertama.split(",")[0].strip().strip('"')
    if not sel:
        return True
    try:
        float(sel)
    except ValueError:
        return True
    return False


def baca_zip(data: bytes) -> pd.DataFrame:
    """Baca satu zip klines arsip menjadi DataFrame berkolom kanonik."""
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        nama = [n for n in z.namelist() if n.endswith(".csv")]
        if len(nama) != 1:
            raise RuntimeError(f"zip memuat {len(nama)} csv, diharapkan tepat satu")
        mentah = z.read(nama[0])

    baris_pertama = mentah.split(b"\n", 1)[0].decode("utf-8", "replace")
    if punya_header(baris_pertama):
        df = pd.read_csv(io.BytesIO(mentah))
        df.columns = KOLOM[: len(df.columns)]
    else:
        jumlah = baris_pertama.count(",") + 1
        df = pd.read_csv(io.BytesIO(mentah), header=None, names=KOLOM[:jumlah])
    return df


def rapikan(df: pd.DataFrame):
    """Urutkan menaik, buang duplikat open_time, kembalikan cacah yang dibuang.

    Urutan waktu tidak boleh bergantung pada urutan baris di berkas.
    """
    sebelum = len(df)
    df = df.loc[:, [k for k in KOLOM_SIMPAN if k in df.columns]].copy()
    df["open_time"] = pd.to_numeric(df["open_time"], errors="coerce").astype("Int64")
    df = df.dropna(subset=["open_time"])
    df = df.sort_values("open_time", kind="mergesort")
    df = df.drop_duplicates(subset=["open_time"], keep="first").reset_index(drop=True)
    return df, sebelum - len(df)


def tulis_parquet(df: pd.DataFrame, tujuan: str) -> int:
    """Tulis parquet terkompresi zstd; kembalikan ukuran byte hasilnya."""
    p = Path(tujuan)
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(p, engine="pyarrow", compression="zstd", index=False)
    return p.stat().st_size
