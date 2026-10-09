# Master's Thesis — Code and Data

**Stress Testing Automated Trading Systems using a Quantitative Framework for Financial Regulatory Systems**


This repository contains all data and executable scripts needed to reproduce every result, table, and figure in the thesis. The written thesis is included as `MASTER_THESIS-BIDISA_BISWAS.pdf`.

---

## Environment / Setup

1. Python 3.11 is recommended.
2. Install dependencies:
```bash
   pip install -r code/requirements.txt
```
3. Open the notebooks in `code/notebooks/` with Jupyter and run them top to bottom in the order given below.

> All randomness is seeded (random seed = 42) for reproducibility.

---

## Folder Structure

```text
Biswas_Bidisa_1165004_Master_Thesis/
│
├── MASTER_THESIS-BIDISA_BISWAS.pdf     Final thesis (print version)
│
├── code/
│   ├── requirements.txt                Python package list
│   ├── config.py                       Shared paths / settings
│   │
│   ├── data/
│   │   ├── raw/
│   │   │   ├── GSPC_1997_2022.csv       S&P 500 daily prices (readable copy)
│   │   │   └── Data_to_CSV.py           Converts cached Parquet -> CSV
│   │   ├── processed/                   Cleaned / return series
│   │   └── simulated/                   Monte Carlo paths (mc_returns_*.npy)
│   │
│   ├── notebooks/                       All analysis notebooks (run here)
│   ├── src/                             Reusable Python modules
│   ├── models/                          Saved / trained LSTM model
│   └── results/                         Output tables and figures
│
└── sources/                            PDFs of online sources (working
                                        papers, reports, standards)
```

---

## Data

- **Source:** S&P 500 index (ticker `^GSPC`), daily adjusted close, Yahoo Finance, January 1997 – December 2022, downloaded via the `yfinance` library.
- **Ranges:**
  - **2008 analysis** → 1997–2009 (calm 1997–2007, crisis 2007–2009)
  - **COVID analysis** → 2005–2022 (warm-up 2005–2009, LSTM training 2010–2019, crisis 2020–2021)

The raw data is cached as Parquet; `GSPC_1997_2022.csv` is a plain-text copy of the same series for convenience (produced by `Data_to_CSV.py`).

---

## Run Order

Run the notebooks in this order. Each one produces the outputs noted.

| # | Notebook | Produces |
|---|----------|----------|
| 1 | `Data_collection.ipynb` | Downloads and caches the S&P 500 price data; computes log returns |
| 2 | `GARCH Modelling 2008 crisis.ipynb`<br>`GARCH Modelling COVID Crisis.ipynb` | GJR-GARCH(1,1) parameters for the four market periods → **Table 1**, **Figure 2** |
| 3 | `monte_carlo_simulation.ipynb` | 10,000 paths × 252 days for the six stress scenarios; saves to `data/simulated/` → **Figure 4** |
| 4 | `ROBUST_LSTM_Volatility.ipynb` *(main analysis)* | Trains the regularised LSTM, runs the stress test and the lookback contamination test with the path-level bootstrap → **Figure 5**, **Table 5**, **Table 6**, **Table 7**, **Figure 3**, **Figure 6** |

Tables 2, 3, 4 and 8 and the appendix derivations are documented in the thesis text; Table 8 (long-run volatilities) follows directly from the GJR-GARCH parameters in Table 1.

---

## Notes

- Run notebooks from inside `code/notebooks/` so relative paths resolve.
- Figures are written to `results/` (and some alongside the notebooks).
- Seeds are fixed throughout; re-running reproduces the reported figures.
