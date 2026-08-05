import pandas as pd

from visualization.utils import (
    create_chart_response,
    validate_numeric
)


def histogram(
    series: pd.Series,
    bins: int = 20
):
    """
    Prepare histogram visualization data.

    Parameters
    ----------
    series : pandas.Series

    bins : int, default=20

    Returns
    -------
    dict
    """

    validate_numeric(series)

    series = series.dropna()

    return create_chart_response(

        chart_type="histogram",

        title=f"Distribution of {series.name}",

        x_axis=series.name,

        y_axis="Frequency",

        reason="Numeric feature.",

        recommendation=(
            "Useful for understanding the "
            "distribution of the feature."
        ),

        priority=1,

        data={

            "values": series.tolist(),

            "bins": bins
        }
    )