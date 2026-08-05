import pandas as pd


def calculate_variance(series: pd.Series):
    """
    Calculate variance.
    """

    series = series.dropna()

    return {
        "variance": round(float(series.var()), 4)
    }


def calculate_standard_deviation(series: pd.Series):
    """
    Calculate standard deviation.
    """

    series = series.dropna()

    return {
        "standard_deviation": round(float(series.std()), 4)
    }


def calculate_minimum(series: pd.Series):
    """
    Calculate minimum value.
    """

    series = series.dropna()

    return {
        "minimum": round(float(series.min()), 4)
    }


def calculate_maximum(series: pd.Series):
    """
    Calculate maximum value.
    """

    series = series.dropna()

    return {
        "maximum": round(float(series.max()), 4)
    }


def calculate_range(series: pd.Series):
    """
    Calculate range.
    """

    series = series.dropna()

    value = series.max() - series.min()

    return {
        "range": round(float(value), 4)
    }


def calculate_dispersion(series: pd.Series):
    """
    Calculate all dispersion measures.
    """

    result = {}

    result.update(
        calculate_variance(series)
    )

    result.update(
        calculate_standard_deviation(series)
    )

    result.update(
        calculate_minimum(series)
    )

    result.update(
        calculate_maximum(series)
    )

    result.update(
        calculate_range(series)
    )

    return result