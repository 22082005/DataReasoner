from typing import Any


def create_chart_response(
    chart_type: str,
    title: str,
    data: dict,
    x_axis: str = None,
    y_axis: str = None,
    reason: str = "",
    priority: int = 1,
    recommendation: str = ""
):
    """
    Create a standardized visualization response.

    Parameters
    ----------
    chart_type : str

    title : str

    data : dict

    x_axis : str, optional

    y_axis : str, optional

    reason : str

    priority : int

    recommendation : str

    Returns
    -------
    dict
    """

    return {

        "chart_type": chart_type,

        "title": title,

        "x_axis": x_axis,

        "y_axis": y_axis,

        "priority": priority,

        "reason": reason,

        "recommendation": recommendation,

        "data": data
    }


def validate_column_exists(
    df,
    column: str
):
    """
    Validate that a column exists.
    """

    if column not in df.columns:

        raise ValueError(
            f"Column '{column}' not found."
        )


def validate_numeric(series):
    """
    Validate numeric column.
    """

    if not series.dtype.kind in "if":

        raise ValueError(
            "Numeric column required."
        )


def validate_categorical(series):
    """
    Validate categorical column.
    """

    if series.dtype.kind in "if":

        raise ValueError(
            "Categorical column required."
        )