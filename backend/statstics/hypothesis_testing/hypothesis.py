import pandas as pd

from .selector import select_hypothesis_test


def analyze_hypothesis_testing(
    df: pd.DataFrame,
    schema: list,
    target: str
):
    """
    Perform hypothesis testing for all eligible
    features against the user-selected target column.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataset.

    schema : list
        Inferred schema information for the dataset.

    target : str
        Target column explicitly selected by the user.

    Returns
    -------
    dict
        Hypothesis testing analysis results.
    """

    # ---------------------------------------
    # Find user-selected target in schema
    # ---------------------------------------

    target_schema = None

    for column in schema:

        if column["column_name"] == target:

            target_schema = column

            break

    # ---------------------------------------
    # Target not found
    # ---------------------------------------

    if target_schema is None:

        return {

            "summary": {

                "target_detected": False,

                "target": target,

                "analyzed_features": 0,

                "significant_features": 0

            },

            "results": [],

            "recommendations": [],

            "metadata": {

                "module": "Hypothesis Testing",

                "version": "1.0"

            }

        }

    # ---------------------------------------
    # Get target series
    # ---------------------------------------

    target_series = df[target_schema["column_name"]]

    analyzed_features = 0

    significant_features = 0

    results = []

    # ---------------------------------------
    # Analyze each feature
    # ---------------------------------------

    for feature_schema in schema:

        # -----------------------------------
        # Skip Target & Identifier
        # -----------------------------------

        if feature_schema["column_name"] == target:

            continue

        if feature_schema["semantic_role"] == "identifier":

            continue

        # -----------------------------------
        # Skip unsupported columns
        # -----------------------------------

        if not feature_schema["use_for_analysis"]:

            continue

        analyzed_features += 1

        # -----------------------------------
        # Get feature series
        # -----------------------------------

        feature = df[
            feature_schema["column_name"]
        ]

        # -----------------------------------
        # Select appropriate hypothesis test
        # -----------------------------------

        decision = select_hypothesis_test(

            feature,

            target_series,

            feature_schema,

            target_schema

        )

        # -----------------------------------
        # No suitable test
        # -----------------------------------

        if decision["selected_test"] is None:

            continue

        # -----------------------------------
        # Selected test
        # -----------------------------------

        method = decision["selected_test"]

        result = method(

            feature,

            target_series

        )

        # -----------------------------------
        # Statistical significance
        # -----------------------------------

        if result.get("reject_null", False):

            significant_features += 1

        # -----------------------------------
        # Store result
        # -----------------------------------

        results.append({

            "entity_1":
                feature_schema["column_name"],

            "entity_2":
                target_schema["column_name"],

            "status": (

                "Statistically Significant"

                if result.get(
                    "reject_null",
                    False
                )

                else

                "Not Significant"

            ),

            "statistics": result,

            "metadata": {

                "test":
                    method.__name__,

                "reason":
                    decision["reason"],

                "alternatives": [

                    alternative.__name__

                    for alternative
                    in decision["alternatives"]

                ]

            }

        })

    # ---------------------------------------
    # Final response
    # ---------------------------------------

    return {

        "summary": {

            "target_detected": True,

            "target":
                target_schema["column_name"],

            "analyzed_features":
                analyzed_features,

            "significant_features":
                significant_features

        },

        "results": results,

        "recommendations": [],

        "metadata": {

            "module": "Hypothesis Testing",

            "version": "1.0"

        }

    }