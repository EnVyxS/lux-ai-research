# PETA MODUL — bot_v8 (LUX Terminal v9 / v8.7)

Keluaran Tugas 0. Dasar: arsip `LUX_Terminal_v9_web_lux_upgrade.zip` dibongkar di
sandbox, 208 berkas, 165 di antaranya `.py` berjumlah 25.811 baris. Inventaris
lengkap per berkas ada di `PETA_MODUL_BERKAS.md`.

Semua nomor baris di sini dibaca langsung dari berkas versi ini.

## 1. Bentuk umum

- Akar `bot_v8/` berisi 33 berkas `.py`; **17 di antaranya punya blok `__main__`**
  (backtest, combined_tune, compare_strategies, exp_refine_entry, explore,
  export_replay, export_viz, fetch_data, fetch_data_full, inspect_markets,
  lux_start, main, mc_risk_tune, paper_review, research_entry_tf, tune_refine,
  walk_forward). Tidak ada satu jalur eksekusi kanonik.
- `engine.py` = 3.621 baris (sekitar 27% dari seluruh baris di akar).
- Subpohon `lux/` = 8.674 baris (dihitung `wc -l` atas seluruh `lux/**/*.py`).
- Penanda tambalan bertanda versi/fase (`[v8.1]`, `[P1]`, `[ICEBERG v8.7]`, dll.)
  muncul 697 kali di berkas `.py`.

## 2. Jalur keputusan dagang (satu-satunya yang relevan untuk riset)

```
engine.run (605)
  -> _scan_for_entries (1033)
  -> _poll_symbol (1210)            # menyuapi candle ke SweepStrategy.update
     -> strategy.update (1195)      # strategy.py: hasilkan Signal atau None
  -> _validate_and_enter (1537)     # gerbang HTF/DI/regime/BTC
  -> _try_enter (1774) -> _run_entry_bg (1818) -> _try_enter_inner (1836)
     -> _sprof override (1921-1926) -> find_tp_levels (strategy 945)
     -> gerbang rr1 < min_rr efektif (1997)  -> entry refinement (2015+)
     -> sizing (risk.size_position 291) -> penempatan order
  -> _manage_open_positions (2619) -> _check_partial_tp_and_trail (2730)
  -> _determine_exit (3004) -> _finalize_close (3089)
```

Berkas pendukung: `patterns.py` (detektor geometri murni, 728 baris),
`risk.py` (sizing & invarian risiko, 530 baris), `state.py` (slot, breaker,
blacklist), `journal.py` (SQLite), `sessions.py`/`assets.py` (murni).

## 3. Konfigurasi yang benar-benar aktif saat kirim

Dibaca dari `config.py` (default `field(default_factory=...)`) dan disilangkan
dengan `.env.example`. Keduanya konsisten pada butir-butir berikut.

| Kunci | Nilai kirim | Baris config.py |
|---|---|---|
| `enable_smc` | False | 357 |
| `allow_two_layer` | False | 353 |
| `enable_trendline` | True | 499 |
| `enable_trendline_bounce` | False | 501 |
| `enable_double` | False | 503 |
| `enable_flag` | False | 505 |
| `enable_triangle` / `enable_rectangle` / `enable_triple` / `enable_wedge` / `enable_complex_hs` | True | 699-703 |
| `trendline_min_htf_score` | 3 (dari maksimum 3) | 517 |
| `fee_taker` / `fee_maker` | 0,0005 / 0,0002 | 426-427 |
| `sl_slippage_pct` | 0,0005 | 430 |
| `strategy_profiles` | dict override per setup_source | 540 |

Catatan: `enable_hs` (head & shoulders) TIDAK muncul sebagai atribut di daftar
grep `config.py`, sementara `.env.example` baris 243 memuat
`ENABLE_HEAD_SHOULDERS=true` dan `strategy.py` membacanya sebagai `self.enable_hs`.
**Ini memerlukan verifikasi** (kemungkinan atribut bernama lain di `config.py`).

## 4. Titik penimpaan konfigurasi saat berjalan

1. `engine._get_strategy_profile` (engine.py 175) membaca
   `settings.strategy_profiles[setup_source]`.
2. `engine._try_enter_inner` 1921-1926 menimpa enam parameter efektif:
   `sl_atr_multiplier`, `min_rr`, `fallback_rr`, `tp1_close_fraction`,
   `trailing_steps`.
3. `backtest._apply_strategy_profile` (backtest.py 185) melakukan hal setara di
   jalur backtest; dipakai juga oleh `exp_refine_entry.py` 153 dan
   `lux/bridge/signal_export.py` 126.
4. `lux.genome.apply_to_settings` dipanggil di `main.py` 112 — peredaman gen
   dapat mengubah settings sebelum engine berjalan.
5. `config.set_daily_drawdown_override` (config.py 142) mengubah batas harian
   saat berjalan.

Konsekuensi: konfigurasi tertulis bukan konfigurasi efektif. Setiap angka dari
modul tanpa cetakan konfigurasi efektif tidak dapat direproduksi.

## 5. Bagian yang HARUS diabaikan di repo ini

`exchange.py`, `telegram_bot.py`, `web_dashboard/**`, `diagnose.py`,
`inspect_markets.py`, `lux/agent/**` (chat, suara, web, backend LLM),
`lux/market/feed.py`, `lux/paper/**`, `lux/memory/**`, `lux/intel/**` (menarik
data jaringan saat berjalan), dan `backtest.py` (dilarang oleh §2).

## 6. Verifikasi temuan warisan A-P

| # | Status | Bukti |
|---|---|---|
| A | BELUM DIPERIKSA | 586/10.032 adalah angka run, bukan properti kode. Hanya bisa dinilai setelah juri sendiri berjalan. |
| B | BELUM DIPERIKSA | Idem; 559/582 muncul sebagai klaim di `AUDIT.md` bagian v8.3, bukan artefak yang dapat diverifikasi. |
| C | TERVERIFIKASI | `strategy._first_pattern_ctx` 1125-1175: `ctxs` diisi berurutan, `detect_trendline_break` ditambahkan PERTAMA (1135), lalu loop `for ctx in ctxs: if ctx is not None: return ctx`. Prioritas murni urutan penyusunan. |
| D | TERVERIFIKASI | config.py 353/357/501/503/505 = False (lihat tabel §3). Konsisten dengan `.env.example` 118/122/242/244/271. |
| E | TERVERIFIKASI | config.py 517 default 3; ditegakkan di `engine.py` 1601: `if _is_trendline_break and htf_score < settings.trendline_min_htf_score: return`. Uji modul sendiri mematoknya (`tests/test_di_gate.py` 121). Maksimum skor 3 sesuai `HTFBias.htf_score` (strategy.py 178, "1-3"). |
| F | TERVERIFIKASI | `AUDIT.md` bagian v8.3: "OOS test-half: **0.40/fw30 PF 1.632** > 0.40/fw20 (1.603) > baseline (1.571). **Default final v8.3**". Default dipilih dengan melihat paruh uji. Kebocoran seleksi, angka turunannya tidak sah. |
| G | SEBAGIAN TERVERIFIKASI | `AUDIT.md` menyebut "split kronologis per-pair: paruh-1 train, paruh-2 test", tanpa embargo/purging. Klaim "30 pair dipilih alfabetis" belum saya temukan buktinya di berkas. **Ini memerlukan verifikasi.** |
| H | TERVERIFIKASI | `strategy.Signal` 134-152: hanya side, sweep_price, wick_extreme, ob_top, ob_bottom, ifvg_top, ifvg_bottom, candle_index, atr, structure_type, is_eql_sweep, regime, is_two_layer, setup_source, allow_market, pattern_name. Tidak ada entry/sl/tp/probabilitas/alasan. |
| I | TERVERIFIKASI | `_last_miss_reason` hanya ditulis di cabang gagal (strategy.py 1239, 1286, 1340, 1385) dan dibaca sekali di engine 1360. Tidak ada padanan "taken_reason". |
| J | TERVERIFIKASI | SCHEMA `journal.py` 12-38: kolom trades tidak memuat setup_source, htf_score, regime, maupun pattern. |
| K | TERVERIFIKASI | Lihat §4 di atas. |
| L | TERVERIFIKASI | `engine.py` 1997: `if rr1 < _min_rr_eff: return`. Geometri TP menentukan apakah transaksi terjadi. |
| M | TERVERIFIKASI | `risk.btc_correlation_block` 489-505 memblokir LONG saat BTC BEAR dan sebaliknya, plus cap posisi searah saat netral; dipanggil `engine.py` 1626. Keputusan lintas simbol nyata -> permutasi harus per TANGGAL UTC. |
| N | TERVERIFIKASI | `risk.py`: `calculate_dynamic_risk` 36 (power-law, clamp min/max), tier 1-3% (`DEFAULT_RISK_TIERS`), taper mega-cap <1% di atas $100k, `qty_for_max_loss` 226, `size_position` 291, `resolve_milestone_sl` 389, `clamp_sl_to_valid_side` 454. Lapisan ini paling rapi di modul. Klaim "kendala mengikat = kapasitas margin" belum saya uji angkanya; **ini memerlukan verifikasi**. |
| O | TERVERIFIKASI (dengan koreksi) | Subpohon `lux/` = 8.674 baris. Titik tempel ke mesin ada EMPAT: engine 1751 `lux_gate_entry`, 1761 `is_setup_silenced`, 2385 dan 3140 `paper_recorder`. `lux_gate_entry` mengembalikan None kecuali controller='lux' DAN uang asli efektif (default bot) -> no-op. `paper_recorder` hanya merekam. **Koreksi**: `is_setup_silenced` dan `lux.genome.apply_to_settings` (main.py 112) BUKAN no-op struktural — keduanya BISA mengubah perilaku bila genom diredam; yang membuatnya no-op adalah default "semua gen aktif", bukan desain. Jadi "keempatnya no-op by design" terlalu kuat. |
| P | TERVERIFIKASI | 697 kemunculan penanda bertanda di berkas `.py`; `engine.py` 3.621 baris = sekitar 27% baris akar. Angka "187" pada temuan warisan lebih rendah dari cacah saya; perbedaan kemungkinan pola pencocokan. |

## 7. Aritmetika biaya warisan

`backtest.py` modul memodelkan biaya sebagai satu potongan datar `fee_r`
(baris 134, dikurangkan sekali di baris 426: `"r": realized - fee_r`).
**Funding tidak dimodelkan sama sekali** — dinyatakan sendiri di docstring
`backtest.py` baris 29. Slippage juga tidak dimodelkan per-eksekusi; ia dilipat
ke `fee_r` yang sama.

Artinya prediksi warisan ("ekspektasi B0 jatuh di bawah 0,10R setelah biaya
dimodelkan benar") berdiri di atas dasar mekanis yang nyata: model biaya modul
memang tidak memuat funding, tidak memuat asimetri taker/maker per-kaki, dan
tidak memuat slippage yang bergantung ukuran stop. Angka 0,3232R dan 0,306R
sendiri BELUM diverifikasi di sini dan tetap berstatus klaim.
