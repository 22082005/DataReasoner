import pandas as pd

from visualization.utils import (
    create_chart_response,
    validate_numeric
)


def density(series: pd.Series):
    """
    Prepare density plot visualization data.

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

        chart_type="density",

        title=f"Density Plot of {series.name}",

        x_axis=series.name,

        y_axis="Density",

        priority=2,

        reason=(
            "Numeric feature."
        ),

        recommendation=(
            "Useful for understanding the "
            "underlying probability distribution "
            "and identifying skewness or multiple peaks."
        ),

        data={

            "values": series.tolist()

        }

    )