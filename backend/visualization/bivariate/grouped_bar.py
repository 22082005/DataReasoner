import pandas as pd

from visualization.utils import (
    create_chart_response,
    validate_categorical
)


def grouped_bar(
    feature: pd.Series,
    target: pd.Series
):
    """
    Prepare grouped bar chart data.

    Parameters
    ----------
    feature : pandas.Series

    target : pandas.Series

    Returns
    -------
    dict
    """

    validate_categorical(feature)
    validate_categorical(target)

    df = pd.DataFrame({

        "feature": feature,

        "target": target

    }).dropna()

    grouped = (
        df
        .groupby(["feature", "target"])
        .size()
        .unstack(fill_value=0)
    )

    return create_chart_response(

        chart_type="grouped_bar",

        title=f"{feature.name} vs {target.name}",

        x_axis=feature.name,

        y_axis="Count",

        priority=1,

        reason=(
            "Both variables are categorical."
        ),

        recommendation=(
            "Useful for comparing category frequencies "
            "across multiple groups."
        ),

        data={

            "categories":
                grouped.index.astype(str).tolist(),

            "series":[

                {

                    "name": str(column),

                    "values":
                        grouped[column].tolist()

                }

                for column in grouped.columns

            ]

        }

    )