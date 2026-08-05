from scipy.stats import kstest


def kolmogorov_test(series):
    """
    Perform the Kolmogorov-Smirnov normality test.

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
            "test": "Kolmogorov-Smirnov",
            "statistic": None,
            "p_value": None,
            "is_normal": False,
            "reason": "Insufficient data"
        }

    # Standardize the data
    standardized = (series - series.mean()) / series.std(ddof=1)

    statistic, p_value = kstest(
        standardized,
        "norm"
    )

    return {
        "test": "Kolmogorov-Smirnov",
        "statistic": round(float(statistic), 4),
        "p_value": round(float(p_value), 4),
        "is_normal": p_value > 0.05
    }