import pandas as pd

from scipy.stats import chi2_contingency

from .utils import interpret_p_value


def chi_square_test(
    x: pd.Series,
    y: pd.Series,
    alpha: float = 0.05
):
    """
    Perform Chi-Square Test of Independence.

    Parameters
    ----------
    x : pandas.Series

    y : pandas.Series

    alpha : float

    Returns
    -------
    dict
    """

    data = pd.concat(
        [x, y],
        axis=1
    ).dropna()

    if len(data) < 2:

        return {

            "method": "Chi-Square",

            "statistic": None,

            "p_value": None,

            "degrees_of_freedom": None,

            "alpha": alpha,

            **interpret_p_value(None, alpha)
        }

    contingency_table = pd.crosstab(
        data.iloc[:, 0],
        data.iloc[:, 1]
    )

    chi2, p_value, dof, expected = chi2_contingency(
        contingency_table
    )

    return {

        "method": "Chi-Square",

        "statistic": round(
            float(chi2),
            4
        ),

        "p_value": round(
            float(p_value),
            4
        ),

        "degrees_of_freedom": int(dof),

        "alpha": alpha,

        "expected_frequency": expected.tolist(),

        **interpret_p_value(
            p_value,
            alpha
        )
    }