import pandas as pd
from sklearn.ensemble import IsolationForest


def isolation_forest_outliers(
        series: pd.Series,
        contamination="auto",
        random_state=42
):
    """
    Detect outliers using Isolation Forest.

    Parameters
    ----------
    series : pandas.Series
    contamination : float or "auto"
    random_state : int

    Returns
    -------
    dict
    """

    series = series.dropna()

    if len(series) < 10:
        return {
            "method": "Isolation Forest",
            "outlier_count": 0,
            "outlier_percentage": 0.0,
            "outlier_indices": [],
            "reason": "Insufficient data"
        }

    model = IsolationForest(
        contamination=contamination,
        random_state=random_state
    )

    predictions = model.fit_predict(
        series.to_frame()
    )

    mask = predictions == -1

    outlier_indices = series[mask].index.tolist()

    return {
        "method": "Isolation Forest",
        "contamination": contamination,
        "outlier_count": len(outlier_indices),
        "outlier_percentage": round(
            (len(outlier_indices) / len(series)) * 100,
            2
        ),
        "outlier_indices": outlier_indices
    }