import pandas as pd

from scipy.stats import wilcoxon

from .utils import (
    validate_alpha,
    interpret_p_value
)


def wilcoxon_test(
    before: pd.Series,
    after: pd.Series,
    alpha: float = 0.05
):
    """
    Perform Wilcoxon Signed-Rank Test.

    Parameters
    ----------
    before : pandas.Series
        First measurement.

    after : pandas.Series
        Second measurement.

    alpha : float, default=0.05

    Returns
    -------
    dict
    """

    validate_alpha(alpha)

    data = pd.concat(
        [before, after],
        axis=1
    ).dropna()

    if len(data) < 2:

        return {

            "method": "Wilcoxon Signed-Rank",

            "statistic": None,

            "p_value": None,

            "alpha": alpha,

            **interpret_p_value(None, alpha)
        }

    statistic, p_value = wilcoxon(
        data.iloc[:, 0],
        data.iloc[:, 1]
    )

    return {

        "method": "Wilcoxon Signed-Rank",

        "statistic": round(
            float(statistic),
            4
        ),

        "p_value": round(
            float(p_value),
            4
        ),

        "alpha": alpha,

        "sample_size": len(data),

        **interpret_p_value(
            p_value,
            alpha
        )
    }