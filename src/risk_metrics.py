from __future__ import annotations

import numpy as np
import pandas as pd


TRADING_DAYS_PER_YEAR = 252


def _validate_dataframe(data: pd.DataFrame, name: str) -> None:
    """
    Validate that an input is a non-empty pandas DataFrame.

    Parameters
    ----------
    data : pandas.DataFrame
        DataFrame to validate.
    name : str
        Name of the argument used in error messages.

    Raises
    ------
    TypeError
        If data is not a pandas DataFrame.
    ValueError
        If data is empty or contains no numeric columns.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError(f"{name} must be a pandas DataFrame.")

    if data.empty:
        raise ValueError(f"{name} must not be empty.")

    if data.select_dtypes(include="number").empty:
        raise ValueError(f"{name} must contain numeric columns.")


def calculate_daily_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate simple daily returns from historical prices.

    Parameters
    ----------
    prices : pandas.DataFrame
        Historical adjusted closing prices indexed by date.

    Returns
    -------
    pandas.DataFrame
        Daily percentage returns with the first incomplete row removed.
    """
    _validate_dataframe(prices, "prices")

    returns = prices.pct_change(fill_method=None)
    returns = returns.dropna(how="all")

    return returns


def calculate_cumulative_returns(
    daily_returns: pd.DataFrame,
) -> pd.DataFrame:
    """
    Calculate cumulative growth factors from daily returns.

    Parameters
    ----------
    daily_returns : pandas.DataFrame
        Daily returns expressed as decimals.

    Returns
    -------
    pandas.DataFrame
        Cumulative growth factors, where 1.10 represents a 10% gain.
    """
    _validate_dataframe(daily_returns, "daily_returns")

    cumulative_returns = (1 + daily_returns).cumprod()

    return cumulative_returns


def calculate_annualized_volatility(
    daily_returns: pd.DataFrame,
    trading_days: int = TRADING_DAYS_PER_YEAR,
) -> pd.Series:
    """
    Calculate annualized volatility from daily returns.

    Parameters
    ----------
    daily_returns : pandas.DataFrame
        Daily returns expressed as decimals.
    trading_days : int, default 252
        Number of trading periods used for annualization.

    Returns
    -------
    pandas.Series
        Annualized volatility for each asset.

    Raises
    ------
    ValueError
        If trading_days is not a positive integer.
    """
    _validate_dataframe(daily_returns, "daily_returns")

    if not isinstance(trading_days, int) or trading_days <= 0:
        raise ValueError("trading_days must be a positive integer.")

    volatility = daily_returns.std() * np.sqrt(trading_days)

    return volatility