from scipy.stats import anderson


def anderson_test(series):
    """
    Perform Anderson-Darling normality test.

    Parameters
    ----------
    series : pandas.Series

    Returns
    -------
    dict
        Test result.
    """

    series = series.dropna()

    if len(series) < 3:
        return {
            "test": "Anderson-Darling",
            "statistic": None,
            "critical_value": None,
            "significance_level": None,
            "is_normal": False,
            "reason": "Insufficient data"
        }

    result = anderson(series)

    # Use the 5% significance level
    idx = list(result.significance_level).index(5.0)

    critical_value = result.critical_values[idx]

    is_normal = result.statistic < critical_value

    return {
        "test": "Anderson-Darling",
        "statistic": round(float(result.statistic), 4),
        "critical_value": round(float(critical_value), 4),
        "significance_level": "5%",
        "is_normal": is_normal
    }