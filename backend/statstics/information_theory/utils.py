import pandas as pd


def prepare_feature_target(
    feature: pd.Series,
    target: pd.Series
):
    """
    Remove missing values from
    feature and target simultaneously.
    """

    data = pd.concat(
        [feature, target],
        axis=1
    ).dropna()

    return (
        data.iloc[:, 0],
        data.iloc[:, 1]
    )