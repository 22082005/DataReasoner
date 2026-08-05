import pandas as pd


def calculate_quartiles(series: pd.Series):
    """
    Calculate quartiles.
    """

    series = series.dropna()

    return {
        "q1": round(float(series.quantile(0.25)), 4),
        "q2": round(float(series.quantile(0.50)), 4),
        "q3": round(float(series.quantile(0.75)), 4)
    }


def calculate_percentiles(series: pd.Series):
    """
    Calculate important percentiles.
    """

    series = series.dropna()

    return {
        "p10": round(float(series.quantile(0.10)), 4),
        "p25": round(float(series.quantile(0.25)), 4),
        "p50": round(float(series.quantile(0.50)), 4),
        "p75": round(float(series.quantile(0.75)), 4),
        "p90": round(float(series.quantile(0.90)), 4)
    }


def calculate_iqr(series: pd.Series):
    """
    Calculate Interquartile Range.
    """

    series = series.dropna()

    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)

    return {
        "iqr": round(float(q3 - q1), 4)
    }


def calculate_percentile_statistics(series: pd.Series):
    """
    Calculate all percentile-based statistics.
    """

    result = {}

    result.update(
        calculate_quartiles(series)
    )

    result.update(
        calculate_percentiles(series)
    )

    result.update(
        calculate_iqr(series)
    )

    return result