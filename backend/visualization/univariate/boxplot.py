import pandas as pd

from visualization.utils import (
    create_chart_response,
    validate_numeric
)


def boxplot(series: pd.Series):
    """
    Prepare box plot visualization data.

    Parameters
    ----------
    series : pandas.Series

    Returns
    -------
    dict
    """

    validate_numeric(series)

    series = series.dropna()

    return create_chart_response(

        chart_type="boxplot",

        title=f"Box Plot of {series.name}",

        x_axis=series.name,

        y_axis="Value",

        priority=1,

        reason=(
            "Numeric feature."
        ),

        recommendation=(
            "Useful for detecting outliers, "
            "spread and quartiles."
        ),

        data={

            "values": series.tolist()

        }

    )