import pandas as pd

from .entropy import calculate_entropy


def information_gain(
    feature: pd.Series,
    target: pd.Series
):
    """
    Calculate Information Gain between a feature
    and the target.

    Parameters
    ----------
    feature : pandas.Series

    target : pandas.Series

    Returns
    -------
    dict
    """

    data = pd.concat(
        [feature, target],
        axis=1
    ).dropna()

    if len(data) == 0:

        return {

            "method": "Information Gain",

            "information_gain": None,

            "reason":
                "No valid observations."
        }

    feature = data.iloc[:, 0]
    target = data.iloc[:, 1]

    # ------------------------------------
    # Entropy of Target
    # ------------------------------------

    target_entropy = calculate_entropy(
        target
    )["entropy"]

    # ------------------------------------
    # Weighted Conditional Entropy
    # ------------------------------------

    weighted_entropy = 0

    for value in feature.unique():

        subset = target[
            feature == value
        ]

        probability = len(subset) / len(target)

        entropy = calculate_entropy(
            subset
        )["entropy"]

        weighted_entropy += (
            probability * entropy
        )

    information_gain_value = (
        target_entropy
        -
        weighted_entropy
    )

    return {

        "method": "Information Gain",

        "target_entropy":
            round(target_entropy, 4),

        "conditional_entropy":
            round(weighted_entropy, 4),

        "information_gain":
            round(
                information_gain_value,
                4
            )
    }