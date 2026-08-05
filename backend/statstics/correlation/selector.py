from statstics.normality.selector import select_normality_test

from .pearson import pearson_correlation
from .spearman import spearman_correlation
from .kendall import kendall_correlation
from .cramers_v import cramers_v
from .point_biserial import point_biserial_correlation


def select_correlation_method(
    x,
    y,
    x_schema,
    y_schema
):
    """
    Select the most appropriate correlation method.

    Parameters
    ----------
    x : pandas.Series
    y : pandas.Series
    x_schema : dict
    y_schema : dict

    Returns
    -------
    dict
    """

    x_type = x_schema["type"]
    y_type = y_schema["type"]

    x_unique = x.nunique(dropna=True)
    y_unique = y.nunique(dropna=True)

    # ----------------------------------------
    # Rule 1
    # Numeric + Numeric
    # ----------------------------------------

    if (
        x_type in ["integer", "float"]
        and
        y_type in ["integer", "float"]
    ):

        x_normality = select_normality_test(x)
        y_normality = select_normality_test(y)

        if (
            x_normality is not None
            and
            y_normality is not None
        ):

            x_result = x_normality["selected_test"](x)
            y_result = y_normality["selected_test"](y)

            if (
                x_result["is_normal"]
                and
                y_result["is_normal"]
            ):

                return {

                    "selected_method": pearson_correlation,

                    "reason":
                        "Both variables are numeric and approximately normally distributed.",

                    "alternatives": [
                        spearman_correlation
                    ]
                }

        return {

            "selected_method": spearman_correlation,

            "reason":
                "Numeric variables but at least one is not normally distributed.",

            "alternatives": [
                pearson_correlation,
                kendall_correlation
            ]
        }

    # ----------------------------------------
    # Rule 2
    # Binary + Numeric
    # ----------------------------------------

    if (
        x_unique == 2
        and
        y_type in ["integer", "float"]
    ):

        return {

            "selected_method": point_biserial_correlation,

            "reason":
                "Binary variable and numeric variable.",

            "alternatives": []
        }

    if (
        y_unique == 2
        and
        x_type in ["integer", "float"]
    ):

        return {

            "selected_method": point_biserial_correlation,

            "reason":
                "Binary variable and numeric variable.",

            "alternatives": []
        }

    # ----------------------------------------
    # Rule 3
    # Categorical + Categorical
    # ----------------------------------------

    if (
        x_type == "categorical"
        and
        y_type == "categorical"
    ):

        return {

            "selected_method": cramers_v,

            "reason":
                "Both variables are categorical.",

            "alternatives": []
        }

    # ----------------------------------------
    # Rule 4
    # Ordinal
    # ----------------------------------------

    if (
        x_schema.get("semantic_role") == "Ordinal"
        or
        y_schema.get("semantic_role") == "Ordinal"
    ):

        return {

            "selected_method": kendall_correlation,

            "reason":
                "Ordinal variables detected.",

            "alternatives": [
                spearman_correlation
            ]
        }

    # ----------------------------------------
    # Default
    # ----------------------------------------

    return {

        "selected_method": spearman_correlation,

        "reason":
            "Fallback correlation method.",

        "alternatives": []
    }