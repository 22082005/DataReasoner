import pandas as pd
from scipy.stats import pearsonr


def pearson_correlation(
    x: pd.Series,
    y: pd.Series
):
    """
    Calculate Pearson correlation between two numeric variables.
    """

    data = pd.concat([x, y], axis=1).dropna()

    if len(data) < 2:
        return {
            "method": "Pearson",
            "correlation": None,
            "p_value": None,
            "relationship": None,
            "reason": "Insufficient observations."
        }

    correlation, p_value = pearsonr(
        data.iloc[:, 0],
        data.iloc[:, 1]
    )

    return {
        "method": "Pearson",
        "correlation": round(float(correlation), 4),
        "p_value": round(float(p_value), 4),
        "relationship": interpret_correlation(correlation)
    }


def interpret_correlation(value):
    """
    Interpret correlation strength.
    """

    value = abs(value)

    if value < 0.2:
        return "Very Weak"

    elif value < 0.4:
        return "Weak"

    elif value < 0.6:
        return "Moderate"

    elif value < 0.8:
        return "Strong"

    return "Very Strong"