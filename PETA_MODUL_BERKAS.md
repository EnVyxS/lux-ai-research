# Inventaris berkas modul warisan

208 berkas. Format: `bytes  baris  path` (relatif terhadap akar arsip).
Berkas biner ditandai `-` pada kolom baris. Dihasilkan dari pembongkaran arsip
di sandbox, bukan dari nama berkas.

## Akar bot_v8 (33 berkas .py + dokumen)

```
   18022     420  bot_v8/.env.example
     277      23  bot_v8/.gitignore
   12440     238  bot_v8/AUDIT.md
   32886     475  bot_v8/KNOWN_ISSUES.md
    3894      89  bot_v8/PAPER_TRADING.md
   17703     283  bot_v8/README.md
    6583     157  bot_v8/assets.py
   45159    1008  bot_v8/backtest.py
    2134      55  bot_v8/combined_tune.py
    5879     156  bot_v8/compare_strategies.py
   46688     798  bot_v8/config.py
    2948      97  bot_v8/diagnose.py
  184993    3621  bot_v8/engine.py
   39105     838  bot_v8/exchange.py
    5414     138  bot_v8/execution_slicing.py
   13876     282  bot_v8/exp_refine_entry.py
    3975      81  bot_v8/explore.py
    5361     109  bot_v8/export_replay.py
    5351     128  bot_v8/export_viz.py
    7094     179  bot_v8/fetch_data.py
    7950     179  bot_v8/fetch_data_full.py
    5366     135  bot_v8/inspect_markets.py
   10359     246  bot_v8/journal.py
    4610     130  bot_v8/lux_start.py
    8485     215  bot_v8/main.py
    4381     126  bot_v8/mc_risk_tune.py
    6995     174  bot_v8/paper_review.py
   31887     727  bot_v8/patterns.py
     811      19  bot_v8/prep_bundles95.py
     253       7  bot_v8/requirements.txt
    3738      89  bot_v8/research_entry_tf.py
   23901     529  bot_v8/risk.py
    1498      45  bot_v8/run_tests.py
    6901     168  bot_v8/sessions.py
     656      14  bot_v8/split_wf.py
   12922     302  bot_v8/state.py
   70020    1598  bot_v8/strategy.py
   29037     721  bot_v8/telegram_bot.py
    2788      66  bot_v8/tune_refine.py
    2503      67  bot_v8/walk_forward.py
```

## Subpohon lux/ (8.674 baris total)

```
     684      15  lux/__init__.py         1366  32  lux/PERSONA.md
    6456     137  lux/README.md           6968 177  lux/cli.py
     610      13  lux/agent/__init__.py   2962  66  lux/agent/autopilot.py
    2397      67  lux/agent/backends/__init__.py
    2722      62  lux/agent/backends/anthropic_backend.py
    1307      42  lux/agent/backends/base.py
   16470     312  lux/agent/backends/local_brain.py
   10670     225  lux/agent/backends/local_llm_backend.py
    2688      64  lux/agent/backends/openai_backend.py
   11491     274  lux/agent/backends/router_backend.py
    9769     251  lux/agent/chart_analysis.py
    3193      81  lux/agent/chat.py
    4516      92  lux/agent/engine.py
    2381      80  lux/agent/exchange_bridge.py
    2403      68  lux/agent/hwinfo.py
    4811     122  lux/agent/initiative.py
    2329      71  lux/agent/intent.py
    4905     131  lux/agent/knowledge.py
    4026     119  lux/agent/media.py
    2523      70  lux/agent/memory.py
    5408     131  lux/agent/model_advisor.py
    1824      48  lux/agent/registry.py
    3118      90  lux/agent/requests.py
   16860     387  lux/agent/server.py
    1497      51  lux/agent/skills/loader.py
    2174      67  lux/agent/tool.py
    6533     144  lux/agent/tools/__init__.py
   13486     280  lux/agent/tools/live_tools.py
   16290     334  lux/agent/tools/market_tools.py
    8271     208  lux/agent/tools/media_tools.py
     830      22  lux/agent/tools/sys_tools.py
    4572     103  lux/agent/tools/web_tools.py
    4697     130  lux/agent/voice/speech.py
    2895      79  lux/agent/voice/style.py
    2097      68  lux/agent/web/fetch.py
    2411      56  lux/agent/web/learn.py
    5430     159  lux/agent/web/search.py
     914      30  lux/bridge/batch_export.py
    4883     118  lux/bridge/engine_gate.py
    1189      44  lux/bridge/intel_feed.py
    2652      68  lux/bridge/live_hook.py
    2477      81  lux/bridge/paper_recorder.py
    9131     213  lux/bridge/signal_export.py
     483       8  lux/control/__init__.py
    4455     132  lux/control/switch.py
    1859      58  lux/core/metalabel.py
    1716      57  lux/core/model_io.py
    1292      40  lux/data/loader.py
    1164      49  lux/eval/metrics.py
    1535      43  lux/eval/montecarlo.py
    1696      42  lux/eval/pbo.py
     670      21  lux/eval/walkforward.py
    1695      54  lux/evaluate.py
    2716      71  lux/features/builder.py
     496      10  lux/genome/__init__.py
    4351      79  lux/genome/genes.py
    3421     111  lux/genome/genome.py
    9469     259  lux/genome/lab.py
     818      24  lux/intel/__init__.py
    1231      34  lux/intel/_net.py
    1503      38  lux/intel/analytics.py
    2668      91  lux/intel/base.py
    2698      67  lux/intel/catalyst.py
    2594      74  lux/intel/dataset.py
    1800      46  lux/intel/geopolitics.py
    2658      57  lux/intel/institutional.py
    2359      63  lux/intel/macro_regime.py
    2675      64  lux/intel/orderflow.py
    1208      35  lux/intel/registry.py
    2034      44  lux/intel/retail.py
    1963      43  lux/intel/smart_money.py
    1485      47  lux/intel/store.py
    1341      30  lux/llm/persona.py
    9015     275  lux/market/feed.py
    6799     187  lux/memory/chain.py
   15881     436  lux/memory/vault.py
    4613     111  lux/paper/account.py
    2069      54  lux/paper/harness.py
    7899     208  lux/paper/live_paper.py
    5379     132  lux/paper_retrain.py
    1033      34  lux/risk/sizing.py
    3615     109  lux/train.py
```

## tests/ (34 berkas)

```
test_asset_class 81, test_backtest 183, test_confluence 70,
test_daily_and_slippage 162, test_di_gate 127, test_entry_fill 50,
test_execution_slicing 104, test_guardrails 98, test_manage_order_zombie 65,
test_memory_chain 81, test_metadata_and_sl 132, test_milestone_trailing 88,
test_observability 62, test_order_lifecycle 44, test_paper_account 84,
test_paper_review 76, test_patterns 120, test_patterns2 91,
test_pnl_reconcile 152, test_recovery_order_matching 94, test_risk 154,
test_risk_tiered 133, test_sessions 94, test_setup_quality 117,
test_stock_failsafe 36, test_stock_session 45, test_strategy 349,
test_stray_orders 108, test_tp_levels 135, test_universe_filters 36,
test_v81_features 91, test_v82_features 50, test_v83_features 112,
test_vault_reason 26   (angka = jumlah baris)
```

## web_dashboard/ dan lain-lain (diabaikan untuk riset)

```
assets/chart.js 587, assets/dash.js 299, assets/style.css 280,
assets/terminal.js 383, backtest.html 82, backtest_bot.html 49,
backtest_data.js 1 baris/27.795 byte, backtest_lux_paper.html 47,
backtest_lux_real.html 46, export_dashboard.py 240, index.html 195,
live.html 112, live_data.js 1/17.723, live_state.js 2/75.130, lux.html 120,
lux_backtest_data.js 4, lux_bt.js 161, lux_chat.html 84,
lux_data.js 1/24.571, make_live_state.py 36, pairs_data.js 1/1.897.461,
status.html 128, searxng/{README.md,docker-compose.yml,settings.yml},
lux/agent/voice/web/lux_voice.html 110, lux/intel/data/events.json 64
```
