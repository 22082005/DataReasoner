import pandas as pd

from scipy.stats import mannwhitneyu

from .utils import (
    validate_alpha,
    interpret_p_value
)


def mann_whitney_test(
    feature: pd.Series,
    target: pd.Series,
    alpha: float = 0.05
):
    """
    Perform Mann-Whitney U Test.

    Parameters
    ----------
    feature : pandas.Series
        Numeric feature.

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

            "method": "Mann-Whitney U",

            "statistic": None,

            "p_value": None,

            "alpha": alpha,

            **interpret_p_value(None, alpha)
        }

    groups = data.iloc[:, 1].unique()

    if len(groups) != 2:

        return {

            "method": "Mann-Whitney U",

            "statistic": None,

            "p_value": None,

            "alpha": alpha,

            **interpret_p_value(None, alpha),

            "reason":
                "Target must contain exactly two groups."
        }

    group1 = data[
        data.iloc[:, 1] == groups[0]
    ].iloc[:, 0]

    group2 = data[
        data.iloc[:, 1] == groups[1]
    ].iloc[:, 0]

    statistic, p_value = mannwhitneyu(
        group1,
        group2,
        alternative="two-sided"
    )

    return {

        "method": "Mann-Whitney U",

        "statistic": round(
            float(statistic),
            4
        ),

        "p_value": round(
            float(p_value),
            4
        ),

        "alpha": alpha,

        "group_1": str(groups[0]),

        "group_2": str(groups[1]),

        "group_1_size": len(group1),

        "group_2_size": len(group2),

        **interpret_p_value(
            p_value,
            alpha
        )
    }