from statstics.hypothesis_testing.chi_square import (
    chi_square_test
)


def chi_square_filter(
    feature,
    target,
    alpha=0.05
):
    """
    Select a feature using the Chi-Square Test.

    Parameters
    ----------
    feature : pandas.Series

    target : pandas.Series

    alpha : float

    Returns
    -------
    dict
    """

    result = chi_square_test(
        feature,
        target,
        alpha
    )

    if result["p_value"] is None:

        return {

            "method": "Chi-Square Filter",

            "selected": False,

            "reason":
                "Unable to compute the Chi-Square Test.",

            "recommendation":
                "Review the feature manually.",

            "statistics": result
        }

    if result["reject_null"]:

        return {

            "method": "Chi-Square Filter",

            "selected": True,

            "reason":
                "Feature is significantly associated with the target.",

            "recommendation":
                "Retain the feature.",

            "statistics": result
        }

    return {

        "method": "Chi-Square Filter",

        "selected": False,

        "reason":
            "Feature is not significantly associated with the target.",

        "recommendation":
            "Consider removing the feature.",

        "statistics": result
    }