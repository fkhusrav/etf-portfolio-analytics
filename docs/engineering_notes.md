# Engineering Notes

This document records the key engineering decisions made during the development of the ETF Portfolio Analytics project.

The goal is to document not only *what* was implemented, but also *why* certain technical decisions were made.

---

## EN-001 — Project Architecture

Decision

The project is divided into independent modules instead of implementing all functionality in a single notebook.

Modules:

- data_loader.py
- risk_metrics.py
- portfolio_analysis.py
- visualization.py

Reason

Each module has a single responsibility.

Benefits

- easier maintenance;
- easier testing;
- cleaner code;
- reusable components.

---

## EN-002 — Development Environment

Decision

Each project uses its own Python virtual environment (.venv).

Reason

Different projects often require different library versions.

Benefits

- reproducible environment;
- dependency isolation;
- easier collaboration;
- no conflicts between projects.

---

## EN-003 — Historical Market Data

Decision

Historical market data is downloaded using the yfinance library.

Reason

For an educational and portfolio project, yfinance provides:

- free access;
- reliable historical data;
- simple Python interface.

Future

The data source can later be replaced with professional APIs such as Bloomberg, Polygon, Refinitiv or Alpha Vantage.

---

## EN-004 — Single Responsibility Principle

Decision

Ticker validation, date validation and market data retrieval are implemented as separate functions.

Reason

Each function performs one clearly defined task.

Benefits

- simpler debugging;
- easier unit testing;
- better readability;
- easier future extensions.

---

## EN-005 — Why Adjusted Close?

Decision

Historical return calculations use Adjusted Close instead of Close.

Reason

Adjusted Close includes:

- dividend payments;
- stock splits;
- other corporate actions.

This provides a more accurate representation of an investor's total return.

---

## EN-006 — Trading Calendar

Observation

Financial markets follow trading days rather than calendar days.

Important

A typical trading year contains approximately 252 trading days rather than 365 calendar days.

This value will later be used when calculating:

- annual returns;
- annual volatility;
- Sharpe ratio.

---

## EN-007 — Why pandas DataFrame?

Decision

The project uses pandas DataFrames as the standard data structure.

Reason

A DataFrame provides built-in support for:

- time series;
- multiple assets;
- statistical analysis;
- visualization;
- vectorized calculations.

This makes it the standard structure for quantitative finance projects.