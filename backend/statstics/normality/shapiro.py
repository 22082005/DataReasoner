from scipy.stats import shapiro


def shapiro_test(series):
    """
    Perform the Shapiro-Wilk normality test.

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
            "test": "Shapiro-Wilk",
            "statistic": None,
            "p_value": None,
            "is_normal": False,
            "reason": "Insufficient data"
        }

    statistic, p_value = shapiro(series)

    return {
        "test": "Shapiro-Wilk",
        "statistic": round(float(statistic), 4),
        "p_value": round(float(p_value), 4),
        "is_normal": p_value > 0.05
    }