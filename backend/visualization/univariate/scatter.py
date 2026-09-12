from visualization.utils import create_chart_response


def scatter(
    x_series,
    y_series
):
    """
    Prepare scatter plot visualization data.

    Parameters
    ----------
    x_series : pandas.Series
        Numeric feature for x-axis.

    y_series : pandas.Series
        Numeric feature for y-axis.

    Returns
    -------
    dict
    """

    data = []

    for x, y in zip(
        x_series,
        y_series
    ):

        if (
            x is None
            or y is None
        ):
            continue

        data.append({

            "x": float(x),

            "y": float(y)

        })

    return create_chart_response(

        chart_type="scatter",

        title=(
            f"{x_series.name} vs "
            f"{y_series.name}"
        ),

        x_axis=x_series.name,

        y_axis=y_series.name,

        priority=1,

        reason=(
            "Two numeric features."
        ),

        recommendation=(
            "Useful for identifying relationships, "
            "patterns and potential clusters between "
            "two numeric features."
        ),

        data={

            "points": data

        }

    )