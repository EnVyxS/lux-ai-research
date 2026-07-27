"""Pembacaan CSV klines arsip dan penulisan parquet kanonik.

Jebakan yang ditangani di sini: arsip Binance MENGUBAH formatnya di tengah
sejarah. Berkas lama tidak punya baris header, berkas yang lebih baru punya.
Membaca keduanya dengan satu aturan tetap akan menelan baris header sebagai
data atau membuang satu baris nyata. Deteksi dilakukan atas isi, bukan tanggal.

Mode `teks=True` membaca seluruh sel sebagai string apa adanya. Itu wajib untuk
uji integritas resample: begitu harga menjadi float, penjumlahan volume tidak
lagi eksak dan ketidakcocokan yang muncul tidak bisa dibedakan antara kesalahan
agregasi dan kesalahan pembulatan.
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


def csv_mentah(data: bytes) -> bytes:
    """Ambil satu-satunya CSV di dalam zip arsip."""
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        nama = [n for n in z.namelist() if n.endswith(".csv")]
        if len(nama) != 1:
            raise RuntimeError(f"zip memuat {len(nama)} csv, diharapkan tepat satu")
        return z.read(nama[0])


def baris_pertama(data: bytes) -> str:
    """Baris pertama CSV di dalam zip, untuk mengukur ada tidaknya header."""
    return csv_mentah(data).split(b"\n", 1)[0].decode("utf-8", "replace")


def baca_zip(data: bytes, teks: bool = False) -> pd.DataFrame:
    """Baca satu zip klines arsip menjadi DataFrame berkolom kanonik.

    `teks=True` mempertahankan setiap sel sebagai string apa adanya.
    """
    mentah = csv_mentah(data)
    opsi = {"dtype": str, "keep_default_na": False} if teks else {}

    pertama = mentah.split(b"\n", 1)[0].decode("utf-8", "replace")
    if punya_header(pertama):
        df = pd.read_csv(io.BytesIO(mentah), **opsi)
        df.columns = KOLOM[: len(df.columns)]
    else:
        jumlah = pertama.count(",") + 1
        df = pd.read_csv(io.BytesIO(mentah), header=None, names=KOLOM[:jumlah], **opsi)
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
