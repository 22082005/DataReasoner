import pandas as pd

from scipy.stats import kruskal

from .utils import (
    validate_alpha,
    interpret_p_value
)


def kruskal_wallis_test(
    feature: pd.Series,
    target: pd.Series,
    alpha: float = 0.05
):
    """
    Perform Kruskal-Wallis H Test.

    Parameters
    ----------
    feature : pandas.Series
        Numeric feature.

    target : pandas.Series
        Categorical target with three or more groups.

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

            "method": "Kruskal-Wallis",

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

            "method": "Kruskal-Wallis",

            "statistic": None,

            "p_value": None,

            "alpha": alpha,

            **interpret_p_value(None, alpha),

            "reason":
                "Kruskal-Wallis requires at least three groups."
        }

    statistic, p_value = kruskal(*groups)

    return {

        "method": "Kruskal-Wallis",

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