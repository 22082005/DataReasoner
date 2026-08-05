import pandas as pd


def iqr_outliers(series: pd.Series):
    """
    Detect outliers using the Interquartile Range (IQR) method.

    Parameters
    ----------
    series : pandas.Series

    Returns
    -------
    dict
    """

    series = series.dropna()

    if len(series) < 4:
        return {
            "method": "IQR",
            "outlier_count": 0,
            "outlier_percentage": 0.0,
            "lower_bound": None,
            "upper_bound": None,
            "outlier_indices": [],
            "reason": "Insufficient data"
        }

    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)

    iqr = q3 - q1

    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    mask = (
        (series < lower_bound)
        | (series > upper_bound)
    )

    outlier_indices = series[mask].index.tolist()

    return {
        "method": "IQR",
        "q1": round(float(q1), 4),
        "q3": round(float(q3), 4),
        "iqr": round(float(iqr), 4),
        "lower_bound": round(float(lower_bound), 4),
        "upper_bound": round(float(upper_bound), 4),
        "outlier_count": len(outlier_indices),
        "outlier_percentage": round(
            (len(outlier_indices) / len(series)) * 100,
            2
        ),
        "outlier_indices": outlier_indices
    }