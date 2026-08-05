import pandas as pd
from scipy.stats import zscore


def zscore_outliers(series: pd.Series, threshold: float = 3.0):
    """
    Detect outliers using the Z-Score method.

    Parameters
    ----------
    series : pandas.Series
    threshold : float
        Z-score threshold (default = 3)

    Returns
    -------
    dict
    """

    series = series.dropna()

    if len(series) < 3:
        return {
            "method": "Z-Score",
            "threshold": threshold,
            "outlier_count": 0,
            "outlier_percentage": 0.0,
            "outlier_indices": [],
            "reason": "Insufficient data"
        }

    # Calculate Z-Scores
    z_scores = zscore(series)

    # Identify Outliers
    mask = abs(z_scores) > threshold

    outlier_indices = series[mask].index.tolist()

    return {
        "method": "Z-Score",
        "threshold": threshold,
        "mean": round(float(series.mean()), 4),
        "std": round(float(series.std()), 4),
        "outlier_count": len(outlier_indices),
        "outlier_percentage": round(
            (len(outlier_indices) / len(series)) * 100,
            2
        ),
        "outlier_indices": outlier_indices
    }