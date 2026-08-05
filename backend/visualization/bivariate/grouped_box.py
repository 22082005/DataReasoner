import pandas as pd

from visualization.utils import (
    create_chart_response,
    validate_numeric,
    validate_categorical
)


def grouped_boxplot(
    numeric: pd.Series,
    categorical: pd.Series
):
    """
    Prepare grouped box plot data.

    Parameters
    ----------
    numeric : pandas.Series

    categorical : pandas.Series

    Returns
    -------
    dict
    """

    validate_numeric(numeric)
    validate_categorical(categorical)

    df = pd.DataFrame({

        "numeric": numeric,

        "category": categorical

    }).dropna()

    grouped = {}

    for category, values in df.groupby("category"):

        grouped[str(category)] = (

            values["numeric"]

            .tolist()

        )

    return create_chart_response(

        chart_type="grouped_boxplot",

        title=f"{numeric.name} by {categorical.name}",

        x_axis=categorical.name,

        y_axis=numeric.name,

        priority=1,

        reason=(
            "Numeric feature grouped by a categorical feature."
        ),

        recommendation=(
            "Useful for comparing distributions "
            "across categories."
        ),

        data={

            "groups": grouped

        }

    )