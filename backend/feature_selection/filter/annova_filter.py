from statstics.hypothesis_testing.anova import (
    anova_test
)


def anova_filter(
    feature,
    target,
    alpha=0.05
):
    """
    Select a feature using One-Way ANOVA.

    Parameters
    ----------
    feature : pandas.Series

    target : pandas.Series

    alpha : float

    Returns
    -------
    dict
    """

    result = anova_test(
        feature,
        target,
        alpha
    )

    if result["p_value"] is None:

        return {

            "method": "ANOVA Filter",

            "selected": False,

            "reason":
                "Unable to compute One-Way ANOVA.",

            "recommendation":
                "Review the feature manually.",

            "statistics": result
        }

    if result["reject_null"]:

        return {

            "method": "ANOVA Filter",

            "selected": True,

            "reason":
                "The feature shows statistically significant differences among target groups.",

            "recommendation":
                "Retain the feature.",

            "statistics": result
        }

    return {

        "method": "ANOVA Filter",

        "selected": False,

        "reason":
            "The feature does not show statistically significant differences among target groups.",

        "recommendation":
            "Consider removing the feature.",

        "statistics": result
    }