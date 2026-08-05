import pandas as pd

from visualization.utils import (
    create_chart_response,
    validate_numeric
)


def scatter(
    x: pd.Series,
    y: pd.Series
):
    """
    Prepare scatter plot visualization data.

    Parameters
    ----------
    x : pandas.Series

    y : pandas.Series

    Returns
    -------
    dict
    """

    validate_numeric(x)
    validate_numeric(y)

    df = pd.concat(
        [x, y],
        axis=1
    ).dropna()

    return create_chart_response(

        chart_type="scatter",

        title=f"{x.name} vs {y.name}",

        x_axis=x.name,

        y_axis=y.name,

        priority=1,

        reason=(
            "Both variables are numeric."
        ),

        recommendation=(
            "Useful for identifying relationships, "
            "correlation, clusters and outliers."
        ),

        data={

            "x": df.iloc[:, 0].tolist(),

            "y": df.iloc[:, 1].tolist()

        }

    )