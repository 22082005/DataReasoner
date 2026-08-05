import pandas as pd

from scipy.stats import f_oneway

from .utils import (
    validate_alpha,
    interpret_p_value
)


def anova_test(
    feature: pd.Series,
    target: pd.Series,
    alpha: float = 0.05
):
    """
    Perform One-Way ANOVA.

    Parameters
    ----------
    feature : pandas.Series
        Numeric feature.

    target : pandas.Series
        Categorical target with more than two groups.

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

            "method": "One-Way ANOVA",

            "statistic": None,

            "p_value": None,

            "alpha": alpha,

            **interpret_p_value(None, alpha)
        }

    groups = []

    group_names = []

    for value in data.iloc[:, 1].unique():

        subset = data[
            data.iloc[:, 1] == value
        ].iloc[:, 0]

        groups.append(subset)

        group_names.append(str(value))

    if len(groups) < 3:

        return {

            "method": "One-Way ANOVA",

            "statistic": None,

            "p_value": None,

            "alpha": alpha,

            **interpret_p_value(None, alpha),

            "reason":
                "ANOVA requires at least three groups."
        }

    statistic, p_value = f_oneway(*groups)

    return {

        "method": "One-Way ANOVA",

        "statistic": round(
            float(statistic),
            4
        ),

        "p_value": round(
            float(p_value),
            4
        ),

        "alpha": alpha,

        "number_of_groups": len(groups),

        "groups": group_names,

        "group_sizes": [
            len(group)
            for group in groups
        ],

        **interpret_p_value(
            p_value,
            alpha
        )
    }