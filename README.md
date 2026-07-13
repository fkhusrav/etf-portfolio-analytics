# etf-portfolio-analytics
Python-based ETF portfolio analytics project covering performance, risk metrics, drawdowns, correlations and portfolio comparison.

# ETF Portfolio Analytics

A Python-based portfolio analytics project for comparing exchange-traded funds (ETFs) by performance, risk, drawdowns, correlations, and portfolio allocation.

The project is designed as a practical introduction to quantitative investment analysis and ETF-based portfolio management. It focuses on building reusable analytical tools with Python, pandas, NumPy, and Jupyter Notebook.

## Project Objectives

The main objective is to create a transparent and reproducible workflow for analysing ETF portfolios.

The project will answer questions such as:

* How have different ETFs performed over time?
* What are their annualised returns and volatility?
* How large were their historical drawdowns?
* How strongly are the ETFs correlated?
* How does combining several ETFs affect portfolio risk?
* How does portfolio rebalancing influence performance?

## Planned Features

### Phase 1: Data Collection and Basic Analysis

* Download historical ETF market data
* Clean and validate price data
* Calculate daily returns
* Calculate cumulative returns
* Compare historical price development
* Visualise ETF performance

### Phase 2: Performance and Risk Metrics

* Annualised return
* Annualised volatility
* Sharpe ratio
* Maximum drawdown
* Rolling volatility
* Risk-adjusted performance comparison

### Phase 3: Portfolio Analytics

* Portfolio allocation
* Portfolio return calculation
* Portfolio volatility
* Correlation matrix
* Diversification analysis
* Contribution of individual assets to portfolio risk

### Phase 4: Backtesting and Rebalancing

* Buy-and-hold portfolio backtest
* Periodic portfolio rebalancing
* Comparison of monthly, quarterly, and annual rebalancing
* Transaction cost assumptions
* Portfolio weight drift analysis

### Phase 5: Reporting and Visualisation

* Interactive charts
* Portfolio analytics dashboard
* Automated analytical report
* Summary of key portfolio insights

## Technologies

* Python
* pandas
* NumPy
* Jupyter Notebook
* matplotlib
* yfinance
* Git
* GitHub

Additional technologies may be introduced as the project develops:

* Plotly
* Dash
* SciPy
* pytest

## Project Structure

```text
etf-portfolio-analytics/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── notebooks/
│   └── 01_etf_portfolio_analysis.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── portfolio_analysis.py
│   ├── risk_metrics.py
│   └── visualization.py
│
├── data/
├── images/
└── reports/
```

## Module Responsibilities

### `data_loader.py`

Responsible for:

* downloading market data;
* validating ticker symbols;
* cleaning missing observations;
* preparing price data for analysis.

### `risk_metrics.py`

Responsible for calculating:

* returns;
* volatility;
* Sharpe ratio;
* maximum drawdown;
* other portfolio risk metrics.

### `portfolio_analysis.py`

Responsible for:

* portfolio weights;
* portfolio-level returns;
* portfolio volatility;
* asset allocation analysis;
* rebalancing logic.

### `visualization.py`

Responsible for:

* price charts;
* cumulative return charts;
* drawdown charts;
* risk and return comparisons;
* correlation visualisations.

## Initial ETF Universe

The first version of the project may use highly liquid US-listed ETFs for technical development and data validation, for example:

* SPY — SPDR S&P 500 ETF Trust
* VOO — Vanguard S&P 500 ETF
* QQQ — Invesco QQQ Trust
* AGG — iShares Core U.S. Aggregate Bond ETF
* GLD — SPDR Gold Shares

Later versions will also include European UCITS ETFs available to investors in Germany.

## Installation

Clone the repository:

```bash
git clone https://github.com/fkhusrav/etf-portfolio-analytics.git
cd etf-portfolio-analytics
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
source .venv/Scripts/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Start Jupyter Notebook:

```bash
jupyter notebook
```

## Current Status

The project structure and development roadmap have been defined.

The next implementation step is to build the market data loading module and create the first ETF comparison notebook.

## Disclaimer

This project is intended for educational and portfolio demonstration purposes only.

It does not constitute investment advice, financial advice, or a recommendation to buy or sell any financial instrument. Historical performance does not guarantee future results.

## Author

Khusrav Fayzulloev

* GitHub: [fkhusrav](https://github.com/fkhusrav)
* LinkedIn: [Khusrav Fayzulloev](https://www.linkedin.com/in/khusrav-fayzulloev-52316a25b/)
