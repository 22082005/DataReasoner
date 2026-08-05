import pandas as pd

from sklearn.feature_selection import (
    mutual_info_classif,
    mutual_info_regression
)


def mutual_information(
    feature: pd.Series,
    target: pd.Series,
    target_type: str
):
    """
    Calculate Mutual Information between a feature
    and the target.

    Parameters
    ----------
    feature : pandas.Series

    target : pandas.Series

    target_type : str
        "categorical" or "continuous"

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

            "method": "Mutual Information",

            "mutual_information": None,

            "reason":
                "No valid observations."
        }

    X = data.iloc[:, [0]]
    y = data.iloc[:, 1]

    try:

        if target_type == "categorical":

            score = mutual_info_classif(
                X,
                y,
                random_state=42
            )[0]

        else:

            score = mutual_info_regression(
                X,
                y,
                random_state=42
            )[0]

    except Exception as e:

        return {

            "method": "Mutual Information",

            "mutual_information": None,

            "reason": str(e)
        }

    return {

        "method": "Mutual Information",

        "mutual_information":
            round(float(score), 4)
    }