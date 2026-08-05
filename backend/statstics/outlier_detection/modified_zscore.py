import numpy as np
import pandas as pd


def modified_zscore_outliers(
        series: pd.Series,
        threshold: float = 3.5
):
    """
    Detect outliers using the Modified Z-Score method.

    Parameters
    ----------
    series : pandas.Series
    threshold : float
        Default threshold = 3.5

    Returns
    -------
    dict
    """

    series = series.dropna()

    if len(series) < 3:
        return {
            "method": "Modified Z-Score",
            "threshold": threshold,
            "outlier_count": 0,
            "outlier_percentage": 0.0,
            "outlier_indices": [],
            "reason": "Insufficient data"
        }

    median = series.median()

    mad = np.median(
        np.abs(series - median)
    )

    if mad == 0:
        return {
            "method": "Modified Z-Score",
            "threshold": threshold,
            "outlier_count": 0,
            "outlier_percentage": 0.0,
            "outlier_indices": [],
            "reason": "MAD is zero"
        }

    modified_z = (
        0.6745
        * (series - median)
        / mad
    )

    mask = np.abs(modified_z) > threshold

    outlier_indices = series[mask].index.tolist()

    return {
        "method": "Modified Z-Score",
        "threshold": threshold,
        "median": round(float(median), 4),
        "mad": round(float(mad), 4),
        "outlier_count": len(outlier_indices),
        "outlier_percentage": round(
            (len(outlier_indices) / len(series)) * 100,
            2
        ),
        "outlier_indices": outlier_indices
    }