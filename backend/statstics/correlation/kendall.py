import pandas as pd
from scipy.stats import kendalltau

from .utils import interpret_correlation


def kendall_correlation(
    x: pd.Series,
    y: pd.Series
):
    """
    Calculate Kendall's Tau correlation.

    Parameters
    ----------
    x : pandas.Series
    y : pandas.Series

    Returns
    -------
    dict
    """

    data = pd.concat([x, y], axis=1).dropna()

    if len(data) < 2:
        return {
            "method": "Kendall",
            "correlation": None,
            "p_value": None,
            "relationship": None,
            "reason": "Insufficient observations."
        }

    correlation, p_value = kendalltau(
        data.iloc[:, 0],
        data.iloc[:, 1]
    )

    return {
        "method": "Kendall",
        "correlation": round(float(correlation), 4),
        "p_value": round(float(p_value), 4),
        "relationship": interpret_correlation(correlation)
    }