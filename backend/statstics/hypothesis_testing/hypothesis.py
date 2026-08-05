import pandas as pd

from .selector import select_hypothesis_test


def analyze_hypothesis_testing(
    df: pd.DataFrame,
    schema: list
):
    """
    Perform hypothesis testing for all eligible
    features against the target column.

    Returns
    -------
    dict
    """

    target_schema = None

    for column in schema:

        if column["semantic_role"] == "Target":

            target_schema = column

            break

    if target_schema is None:

        return {

            "summary": {

                "target_detected": False,

                "analyzed_features": 0

            },

            "results": [],

            "recommendations": [],

            "metadata": {

                "module": "Hypothesis Testing",

                "version": "1.0"

            }

        }

    target = df[target_schema["column_name"]]

    analyzed_features = 0

    significant_features = 0

    results = []

    for feature_schema in schema:

        # ---------------------------------------
        # Skip Target & Identifier
        # ---------------------------------------

        if feature_schema["semantic_role"] in [

            "Target",

            "Identifier"

        ]:

            continue

        # ---------------------------------------
        # Skip unsupported columns
        # ---------------------------------------

        if not feature_schema["use_for_analysis"]:

            continue

        analyzed_features += 1

        feature = df[feature_schema["column_name"]]

        decision = select_hypothesis_test(

            feature,

            target,

            feature_schema,

            target_schema

        )

        if decision["selected_test"] is None:

            continue

        method = decision["selected_test"]

        result = method(

            feature,

            target

        )

        if result.get("reject_null", False):

            significant_features += 1

        results.append({

            "entity_1": feature_schema["column_name"],

            "entity_2": target_schema["column_name"],

            "status": (

                "Statistically Significant"

                if result.get("reject_null", False)

                else

                "Not Significant"

            ),

            "statistics": result,

            "metadata": {

                "test": method.__name__,

                "reason": decision["reason"],

                "alternatives": [

                    alternative.__name__

                    for alternative in decision["alternatives"]

                ]

            }

        })

    return {

        "summary": {

            "target_detected": True,

            "target": target_schema["column_name"],

            "analyzed_features": analyzed_features,

            "significant_features": significant_features

        },

        "results": results,

        "recommendations": [],

        "metadata": {

            "module": "Hypothesis Testing",

            "version": "1.0"

        }

    }