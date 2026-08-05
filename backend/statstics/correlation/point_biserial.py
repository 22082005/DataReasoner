import pandas as pd

from scipy.stats import pointbiserialr

from .utils import interpret_correlation


def point_biserial_correlation(
    binary: pd.Series,
    numeric: pd.Series
):
    """
    Calculate Point-Biserial Correlation.

    Parameters
    ----------
    binary : pandas.Series
        Binary categorical variable.

    numeric : pandas.Series
        Continuous numeric variable.

    Returns
    -------
    dict
    """

    data = pd.concat(
        [binary, numeric],
        axis=1
    ).dropna()

    if len(data) < 2:

        return {
            "method": "Point-Biserial",
            "correlation": None,
            "p_value": None,
            "relationship": None,
            "direction": None,
            "significant": None,
            "reason": "Insufficient observations."
        }

    binary_encoded = (
        data.iloc[:, 0]
        .astype("category")
        .cat.codes
    )

    correlation, p_value = pointbiserialr(
        binary_encoded,
        data.iloc[:, 1]
    )

    direction = (
        "Positive"
        if correlation > 0
        else "Negative"
        if correlation < 0
        else "No Correlation"
    )

    return {

        "method": "Point-Biserial",

        "correlation": round(
            float(correlation),
            4
        ),

        "p_value": round(
            float(p_value),
            4
        ),

        "relationship": interpret_correlation(
            correlation
        ),

        "direction": direction,

        "significant": p_value < 0.05
    }