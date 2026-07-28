"""Uji medan karantina ADR-A006 di serap.ringkas. Tanpa jaringan."""

from lux_ai.serapan import serap


def _baris(simbol, bulan, lolos=True, **tambahan):
    baris = {
        "simbol": simbol,
        "bulan": bulan,
        "jenis_instrumen": "perpetual_usdt",
        "gagal_unduh": False,
        "gagal_checksum": False,
        "byte_zip": 1000,
        "baris": 44640,
        "baris_dibuang": 0,
        "gerbang_lolos": lolos,
        "gerbang_pelanggaran": [] if lolos else ["jarak_60_detik", "tanpa_menit_hilang"],
        "byte_parquet": 1200 if lolos else 0,
        "byte_parquet_karantina": 0 if lolos else 900,
        "parquet_karantina": None if lolos else f"data/parquet_karantina/{simbol}/x.parquet",
        "checksum_zip_sha256": "a" * 64,
    }
    baris.update(tambahan)
    return baris


def test_baris_karantina_hanya_yang_jatuh_gerbang():
    manifes = [
        _baris("AUSDT", "2025-01"),
        _baris("BUSDT", "2025-02", lolos=False),
    ]
    daftar = serap.baris_karantina(manifes)
    assert [d["simbol"] for d in daftar] == ["BUSDT"]
    assert daftar[0]["pelanggaran"] == ["jarak_60_detik", "tanpa_menit_hilang"]
    assert daftar[0]["parquet_karantina"].startswith("data/parquet_karantina/")


def test_gagal_unduh_bukan_karantina():
    manifes = [{"simbol": "XUSDT", "bulan": "2025-01", "gagal_unduh": True}]
    assert serap.baris_karantina(manifes) == []
    ringkas = serap.ringkas_karantina(manifes)
    assert ringkas["cacah_karantina"] == 0
    assert ringkas["cacah_tak_terunduh"] == 1


def test_daftar_karantina_urut_simbol_lalu_bulan():
    manifes = [
        _baris("ZUSDT", "2022-06", lolos=False),
        _baris("AUSDT", "2022-08", lolos=False),
        _baris("AUSDT", "2022-04", lolos=False),
    ]
    daftar = serap.baris_karantina(manifes)
    assert [(d["simbol"], d["bulan"]) for d in daftar] == [
        ("AUSDT", "2022-04"),
        ("AUSDT", "2022-08"),
        ("ZUSDT", "2022-06"),
    ]


def test_ringkas_memuat_medan_penggugur_walau_nol():
    hasil = serap.ringkas([_baris("AUSDT", "2025-01")])
    assert hasil["cacah_karantina"] == 0
    assert hasil["daftar_karantina"] == []
    assert hasil["karantina"]["cacah_dibuang"] == 0
    assert hasil["karantina"]["cacah_ditambal"] == 0
    assert hasil["byte_parquet_karantina_total"] == 0


def test_ringkas_kosong_tetap_memuat_karantina():
    hasil = serap.ringkas([])
    assert hasil["status"] == "TIDAK MENGUKUR"
    assert hasil["cacah_karantina"] == 0
    assert hasil["karantina"]["cacah_dibuang"] == 0


def test_nisbah_tidak_tercemar_parquet_karantina():
    manifes = [_baris("AUSDT", "2025-01"), _baris("BUSDT", "2025-02", lolos=False)]
    hasil = serap.ringkas(manifes)
    # byte_parquet_total hanya dari yang lolos: 1200 / 2000 zip
    assert hasil["byte_parquet_total"] == 1200
    assert hasil["byte_parquet_karantina_total"] == 900
    assert hasil["nisbah_parquet_per_zip"] == round(1200 / 2000, 4)
    assert hasil["cacah_karantina"] == 1
