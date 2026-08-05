import pandas as pd

from visualization.utils import (
    create_chart_response,
    validate_categorical
)


def pie(series: pd.Series):
    """
    Prepare pie chart visualization data.

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

    total = int(counts.sum())

    percentages = (
        (counts / total) * 100
    ).round(2)

    return create_chart_response(

        chart_type="pie",

        title=f"Composition of {series.name}",

        x_axis=series.name,

        y_axis="Percentage",

        priority=2,

        reason=(
            "Categorical feature."
        ),

        recommendation=(
            "Useful for showing the proportion "
            "of each category when the number "
            "of categories is small."
        ),

        data={

            "categories": counts.index.astype(str).tolist(),

            "counts": counts.values.tolist(),

            "percentages": percentages.tolist()

        }

    )