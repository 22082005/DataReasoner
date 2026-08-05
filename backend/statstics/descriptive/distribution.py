import pandas as pd


def calculate_skewness(series: pd.Series):
    """
    Calculate skewness.
    """

    series = series.dropna()

    return {
        "skewness": round(float(series.skew()), 4)
    }


def calculate_kurtosis(series: pd.Series):
    """
    Calculate kurtosis.
    """

    series = series.dropna()

    return {
        "kurtosis": round(float(series.kurt()), 4)
    }


def calculate_distribution(series: pd.Series):
    """
    Calculate distribution statistics.
    """

    result = {}

    result.update(
        calculate_skewness(series)
    )

    result.update(
        calculate_kurtosis(series)
    )

    return result