import pandas as pd

from scipy.stats import chi2_contingency

from .utils import interpret_correlation


def cramers_v(
    x: pd.Series,
    y: pd.Series
):
    """
    Calculate Cramer's V association
    between two categorical variables.
    """

    data = pd.concat([x, y], axis=1).dropna()

    if len(data) < 2:

        return {
            "method": "Cramer's V",
            "correlation": None,
            "p_value": None,
            "relationship": None,
            "direction": "Not Applicable",
            "significant": None,
            "reason": "Insufficient observations."
        }

    contingency_table = pd.crosstab(
        data.iloc[:, 0],
        data.iloc[:, 1]
    )

    chi2, p_value, _, _ = chi2_contingency(
        contingency_table
    )

    n = contingency_table.values.sum()

    rows, cols = contingency_table.shape

    denominator = min(rows - 1, cols - 1)

    if denominator == 0:

        correlation = 0.0

    else:

        correlation = (
            (chi2 / (n * denominator))
            ** 0.5
        )

    return {

        "method": "Cramer's V",

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

        "direction": "Not Applicable",

        "significant": p_value < 0.05
    }