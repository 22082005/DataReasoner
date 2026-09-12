import pandas as pd

from visualization.utils import (
    create_chart_response,
    validate_numeric
)


def scatter(
    x: pd.Series,
    y: pd.Series,
    target: pd.Series = None
):
    """
    Prepare target-aware scatter plot data.

    Parameters
    ----------
    x : pandas.Series
        Numeric feature for x-axis.

    y : pandas.Series
        Numeric feature for y-axis.

    target : pandas.Series, optional
        Target variable used for grouping points.

    Returns
    -------
    dict
    """

    # -----------------------------------------
    # Validate numeric features
    # -----------------------------------------

    validate_numeric(x)
    validate_numeric(y)

    # -----------------------------------------
    # Combine features
    # -----------------------------------------

    data = [
        x.rename("_x"),
        y.rename("_y")
    ]

    if target is not None:

        data.append(
            target.rename("_target")
        )

    df = pd.concat(
        data,
        axis=1
    ).dropna()

    # -----------------------------------------
    # Prepare response data
    # -----------------------------------------

    chart_data = {

        "x": df["_x"].tolist(),

        "y": df["_y"].tolist()

    }

    # -----------------------------------------
    # Add target information
    # -----------------------------------------

    if target is not None:

        chart_data["target"] = (
            df["_target"]
            .astype(str)
            .tolist()
        )

    # -----------------------------------------
    # Chart Response
    # -----------------------------------------

    return create_chart_response(

        chart_type="scatter",

        title=(
            f"{x.name} vs {y.name}"
        ),

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

        data=chart_data

    )