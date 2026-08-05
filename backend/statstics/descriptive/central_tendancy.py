import pandas as pd


def calculate_mean(series: pd.Series):
    """
    Calculate arithmetic mean.
    """

    series = series.dropna()

    return {
        "mean": round(float(series.mean()), 4)
    }


def calculate_median(series: pd.Series):
    """
    Calculate median.
    """

    series = series.dropna()

    return {
        "median": round(float(series.median()), 4)
    }


def calculate_mode(series: pd.Series):
    """
    Calculate mode.
    """

    series = series.dropna()

    mode = series.mode()

    if mode.empty:
        value = None
    else:
        value = mode.tolist()

    return {
        "mode": value
    }


def calculate_central_tendency(series: pd.Series):
    """
    Calculate all measures of central tendency.
    """

    result = {}

    result.update(
        calculate_mean(series)
    )

    result.update(
        calculate_median(series)
    )

    result.update(
        calculate_mode(series)
    )

    return result