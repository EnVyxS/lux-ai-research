from lux_ai.serapan import bentuk_semesta as bs


def test_kerangka_memapar_bentuk_dan_menandai_penyebut_nol():
    # Kasus positif: akar objek dengan kunci dan cabang bersarang.
    akar = {
        "meta": {"versi": 3},
        "per_simbol": {"BTCUSDT": ["2020-01", "2020-02"]},
        "cacah": 21789,
    }
    hasil = bs.kerangka(akar)
    assert hasil["tipe_akar"] == "objek"
    assert hasil["cacah_kunci_tingkat_atas"] == 3
    assert hasil["kunci_tingkat_atas"] == ["meta", "per_simbol", "cacah"]
    assert hasil["tipe_nilai"] == {
        "meta": "objek",
        "per_simbol": "objek",
        "cacah": "angka",
    }
    assert hasil["cacah_elemen_nilai"] == {"meta": 1, "per_simbol": 1}
    assert hasil["cabang_pertama"]["jejak"] == ["meta", "versi"]
    assert hasil["cabang_pertama"]["tipe"] == "angka"
    assert hasil["kunci_dipotong"] is False
    assert hasil["status"] == bs.MENGUKUR

    # Kasus negatif (aturan 30): penyebut nol wajib berstatus TIDAK MENGUKUR,
    # bukan tampak bersih seperti KC-7.
    for kosong in ({}, [1, 2, 3], "teks"):
        sepi = bs.kerangka(kosong)
        assert sepi["cacah_kunci_tingkat_atas"] == 0
        assert sepi["status"] == bs.TIDAK_MENGUKUR

    # Contoh panjang dipotong, bukan dibuang.
    panjang = bs.potong({"a": "x" * 500})
    assert len(panjang) == bs.BATAS_CONTOH + 3
    assert panjang.endswith("...")
