"""Uji pembagian pecahan. Tidak menyentuh jaringan (aturan 14)."""

import pytest

from lux_ai.serapan import pecahan


def jenis_usdt(simbol):
    return "perpetual_usdt" if simbol.endswith("USDT") else "perpetual_usdc"


RENTANG = {
    f"S{i:03d}USDT": {"bulan_pertama": "2021-01", "bulan_terakhir": "2026-06", "cacah_bulan": 60}
    for i in range(20)
}
RENTANG["ETHUSDC"] = {"bulan_pertama": "2023-01", "bulan_terakhir": "2026-06", "cacah_bulan": 40}


def test_pecahan_menutupi_tiap_simbol_tepat_sekali():
    total = 8
    terkumpul = []
    for i in range(total):
        terkumpul.extend(pecahan.simbol_pecahan(RENTANG, jenis_usdt, i, total))
    assert sorted(terkumpul) == sorted(s for s in RENTANG if s.endswith("USDT"))
    assert len(terkumpul) == len(set(terkumpul))
    assert "ETHUSDC" not in terkumpul  # ADR-A005


def test_pecahan_seimbang_dan_deterministik():
    total = 8
    ukuran = [len(pecahan.simbol_pecahan(RENTANG, jenis_usdt, i, total)) for i in range(total)]
    assert max(ukuran) - min(ukuran) <= 1
    assert pecahan.simbol_pecahan(RENTANG, jenis_usdt, 0, total) == pecahan.simbol_pecahan(
        RENTANG, jenis_usdt, 0, total
    )


def test_indeks_di_luar_rentang_ditolak():
    with pytest.raises(ValueError):
        pecahan.simbol_pecahan(RENTANG, jenis_usdt, 8, 8)
    with pytest.raises(ValueError):
        pecahan.simbol_pecahan(RENTANG, jenis_usdt, -1, 8)
    with pytest.raises(ValueError):
        pecahan.simbol_pecahan(RENTANG, jenis_usdt, 0, 0)


def test_nama_keluaran_menyebut_indeksnya():
    assert pecahan.nama_keluaran(0) == "reports/manifes_pecahan_0.json"
    assert pecahan.nama_keluaran(7) == "reports/manifes_pecahan_7.json"
