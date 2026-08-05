from scipy.stats import normaltest


def dagostino_test(series):
    """
    Perform D'Agostino's K² normality test.

    Parameters
    ----------
    series : pandas.Series

    Returns
    -------
    dict
        Test result.
    """

    series = series.dropna()

    # D'Agostino requires at least 8 observations
    if len(series) < 8:
        return {
            "test": "D'Agostino K²",
            "statistic": None,
            "p_value": None,
            "is_normal": False,
            "reason": "Insufficient data (minimum 8 observations required)"
        }

    statistic, p_value = normaltest(series)

    return {
        "test": "D'Agostino K²",
        "statistic": round(float(statistic), 4),
        "p_value": round(float(p_value), 4),
        "is_normal": p_value > 0.05
    }