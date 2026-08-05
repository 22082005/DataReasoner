import pandas as pd

from scipy.stats import fisher_exact

from .utils import (
    validate_alpha,
    interpret_p_value
)


def fisher_exact_test(
    feature: pd.Series,
    target: pd.Series,
    alpha: float = 0.05
):
    """
    Perform Fisher's Exact Test.

    Parameters
    ----------
    feature : pandas.Series
        Categorical feature.

    target : pandas.Series
        Binary categorical target.

    alpha : float, default=0.05

    Returns
    -------
    dict
    """

    validate_alpha(alpha)

    data = pd.concat(
        [feature, target],
        axis=1
    ).dropna()

    if len(data) < 2:

        return {

            "method": "Fisher's Exact",

            "statistic": None,

            "p_value": None,

            "alpha": alpha,

            **interpret_p_value(None, alpha)
        }

    contingency = pd.crosstab(
        data.iloc[:, 0],
        data.iloc[:, 1]
    )

    if contingency.shape != (2, 2):

        return {

            "method": "Fisher's Exact",

            "statistic": None,

            "p_value": None,

            "alpha": alpha,

            **interpret_p_value(None, alpha),

            "reason":
                "Fisher's Exact Test requires a 2×2 contingency table."
        }

    odds_ratio, p_value = fisher_exact(
        contingency
    )

    return {

        "method": "Fisher's Exact",

        "statistic": round(
            float(odds_ratio),
            4
        ),

        "p_value": round(
            float(p_value),
            4
        ),

        "alpha": alpha,

        "table_shape": contingency.shape,

        **interpret_p_value(
            p_value,
            alpha
        )
    }