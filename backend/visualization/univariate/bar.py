import pandas as pd

from visualization.utils import (
    create_chart_response,
    validate_categorical
)


def bar(series: pd.Series):
    """
    Prepare bar chart visualization data.

    Parameters
    ----------
    series : pandas.Series

    Returns
    -------
    dict
    """

    validate_categorical(series)

    series = series.dropna()

    counts = (
        series
        .value_counts(dropna=False)
        .sort_index()
    )

    return create_chart_response(

        chart_type="bar",

        title=f"Distribution of {series.name}",

        x_axis=series.name,

        y_axis="Count",

        priority=1,

        reason=(
            "Categorical feature."
        ),

        recommendation=(
            "Useful for comparing category frequencies."
        ),

        data={

            "categories": counts.index.astype(str).tolist(),

            "counts": counts.values.tolist()

        }

    )