import pandas as pd

from visualization.utils import (
    create_chart_response,
    validate_numeric
)


def violin(series: pd.Series):
    """
    Prepare violin plot visualization data.

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

        chart_type="violin",

        title=f"Violin Plot of {series.name}",

        x_axis=series.name,

        y_axis="Density",

        priority=2,

        reason=(
            "Numeric feature."
        ),

        recommendation=(
            "Useful for visualizing the distribution, "
            "density, median, quartiles, and possible "
            "multi-modal patterns."
        ),

        data={

            "values": series.tolist()

        }

    )