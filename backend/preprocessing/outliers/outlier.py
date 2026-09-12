import pandas as pd

from .selector import select_outlier_method
from statstics.descriptive import descriptive_summary


def analyze_outliers(
    df: pd.DataFrame,
    schema
):
    """
    Analyze outliers for all eligible numeric features.

    Returns
    -------
    dict
    """

    results = []

    total_outliers = 0
    columns_with_outliers = 0
    analyzed_features = 0

    for column in schema:

        # Skip non-analysis columns
        if (
            column["semantic_role"] in ["Target", "Identifier"]
            or column["type"] not in ["integer", "float"]
            or not column["use_for_analysis"]
        ):
            continue

        analyzed_features += 1

        feature = column["column_name"]

        series = df[feature]

        summary = descriptive_summary(series)

        decision = select_outlier_method(
            series,
            summary
        )

        # -----------------------------------
        # No suitable algorithm
        # -----------------------------------

        if decision["selected_method"] is None:

            results.append({

                "feature": feature,

                "status": "Skipped",

                "count": 0,

                "percentage": 0,

                "details": {

                    "method": None,

                    "reason": decision["reason"]

                }

            })

            continue

        # -----------------------------------
        # Execute detector
        # -----------------------------------

        detector = decision["selected_method"]

        result = detector(series)

        outlier_count = result["outlier_count"]

        if outlier_count > 0:

            columns_with_outliers += 1

            total_outliers += outlier_count

        results.append({

            "feature": feature,

            "status": (

                "Outliers Detected"

                if outlier_count > 0

                else

                "No Outliers"

            ),

            "count": outlier_count,

            "percentage": round(

                (outlier_count / len(series)) * 100,

                2

            ),

            "details": {

                "method": detector.__name__,

                "reason": decision["reason"],

                "lower_bound": result.get("lower_bound"),

                "upper_bound": result.get("upper_bound"),

                "outlier_indices": result.get("outlier_indices", []),

                "alternatives": [

                    method.__name__

                    for method in decision.get(

                        "alternatives",

                        []

                    )

                ]

            }

        })

    return {

        "summary": {

            "analyzed_features": analyzed_features,

            "columns_with_outliers": columns_with_outliers,

            "total_outliers": total_outliers,

            "has_outliers": total_outliers > 0

        },

        "results": results,

        "recommendations": [],

        "metadata": {

            "module": "Outlier Detection",

            "version": "1.0"

        }

    }