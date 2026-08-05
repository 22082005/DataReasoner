import pandas as pd

from scipy.stats import entropy as scipy_entropy


def calculate_entropy(series: pd.Series):
    """
    Calculate Shannon Entropy.

    Parameters
    ----------
    series : pandas.Series

    Returns
    -------
    dict
    """

    series = series.dropna()

    if series.empty:

        return {

            "method": "Entropy",

            "entropy": None,

            "reason":
                "Series contains no valid observations."
        }

    probabilities = (
        series
        .value_counts(normalize=True)
        .values
    )

    entropy_value = scipy_entropy(
        probabilities,
        base=2
    )

    return {

        "method": "Entropy",

        "entropy": round(
            float(entropy_value),
            4
        ),

        "unique_values": int(series.nunique()),

        "sample_size": int(len(series))
    }