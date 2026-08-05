import pandas as pd

from .selector import select_correlation_method

def analyze_correlation(
    df: pd.DataFrame,
    schema: list
):
    """
    Analyze correlations between all eligible feature pairs.

    Returns
    -------
    dict
    """

    results = []

    eligible_columns = []

    highly_correlated_pairs = 0

    analyzed_pairs = 0

    for column in schema:

        if (
            column["semantic_role"] in ["Identifier", "Target"]
            or
            not column["use_for_analysis"]
        ):
            continue

        eligible_columns.append(column)

    # -----------------------------------------
    # Pairwise Analysis
    # -----------------------------------------

    for i in range(len(eligible_columns)):

        for j in range(i + 1, len(eligible_columns)):

            analyzed_pairs += 1

            x_schema = eligible_columns[i]
            y_schema = eligible_columns[j]

            x = df[x_schema["column_name"]]
            y = df[y_schema["column_name"]]

            decision = select_correlation_method(
                x,
                y,
                x_schema,
                y_schema
            )

            method = decision["selected_method"]

            if method.__name__ == "point_biserial_correlation":

                if x.nunique(dropna=True) == 2:

                    result = method(x, y)

                else:

                    result = method(y, x)

            else:

                result = method(x, y)

            coefficient = result["correlation"]

            if abs(coefficient) >= 0.90:

                highly_correlated_pairs += 1

            results.append({

                "feature": x_schema["column_name"],

                "status": (

                    "Highly Correlated"

                    if abs(coefficient) >= 0.90

                    else

                    "Correlation Computed"

                ),

                "count": None,

                "percentage": None,

                "statistics": {

                    "related_feature":
                        y_schema["column_name"],

                    "correlation":
                        coefficient,

                    "p_value":
                        result.get("p_value"),

                    "method":
                        method.__name__

                },

                "metadata": {

                    "reason":
                        decision["reason"],

                    "alternatives": [

                        alt.__name__

                        for alt in decision["alternatives"]

                    ]

                }

            })

    return {

        "summary": {

            "analyzed_pairs":
                analyzed_pairs,

            "highly_correlated_pairs":
                highly_correlated_pairs,

            "has_high_correlation":
                highly_correlated_pairs > 0

        },

        "results": results,

        "recommendations": [],

        "metadata": {

            "module": "Correlation",

            "version": "1.0"

        }

    }