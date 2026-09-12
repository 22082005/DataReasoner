import pandas as pd

from .entropy import calculate_entropy
from .information_gain import information_gain
from .mutual_information import mutual_information


def analyze_information(
    df: pd.DataFrame,
    schema: list,
    target: str
):
    """
    Analyze Information Theory statistics for all
    eligible features against the user-selected target.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataset.

    schema : list
        Inferred schema information.

    target : str
        Target column explicitly selected by the user.

    Returns
    -------
    dict
        Information Theory analysis results.
    """

    # --------------------------------------------------
    # Find User-Selected Target
    # --------------------------------------------------

    target_schema = None

    for column in schema:

        if column["column_name"] == target:

            target_schema = column

            break

    # --------------------------------------------------
    # Target Not Found
    # --------------------------------------------------

    if target_schema is None:

        return {

            "summary": {

                "target_detected": False,

                "target": target,

                "analyzed_features": 0,

                "informative_features": 0

            },

            "results": [],

            "recommendations": [],

            "metadata": {

                "module": "Information Theory",

                "version": "1.0"

            }

        }

    # --------------------------------------------------
    # Target Series
    # --------------------------------------------------

    target_series = df[
        target_schema["column_name"]
    ]

    # --------------------------------------------------
    # Categorical Types
    # --------------------------------------------------

    categorical_types = [

        "string",
        "category",
        "categorical",
        "object"

    ]

    # --------------------------------------------------
    # Determine Target Type
    # --------------------------------------------------

    target_type = (

        "categorical"

        if target_schema["type"].lower()
        in categorical_types

        else

        "continuous"

    )

    analyzed_features = 0

    informative_features = 0

    results = []

    # --------------------------------------------------
    # Feature Analysis
    # --------------------------------------------------

    for feature_schema in schema:

        # ----------------------------------------------
        # Skip User-Selected Target
        # ----------------------------------------------

        if feature_schema["column_name"] == target:

            continue

        # ----------------------------------------------
        # Skip Identifier
        # ----------------------------------------------

        if feature_schema["semantic_role"] == "identifier":

            continue

        # ----------------------------------------------
        # Skip Unsupported Columns
        # ----------------------------------------------

        if not feature_schema["use_for_analysis"]:

            continue

        analyzed_features += 1

        # ----------------------------------------------
        # Feature Series
        # ----------------------------------------------

        feature = df[
            feature_schema["column_name"]
        ]

        entropy = None

        information_gain_value = None

        # ----------------------------------------------
        # Entropy & Information Gain
        # Only for categorical features
        # ----------------------------------------------

        if feature_schema["type"].lower() in categorical_types:

            entropy = calculate_entropy(
                feature
            )

            information_gain_value = information_gain(
                feature,
                target_series
            )

        # ----------------------------------------------
        # Mutual Information
        # ----------------------------------------------

        mutual_information_result = mutual_information(

            feature,

            target_series,

            target_type

        )

        mutual_information_value = (
            mutual_information_result["mutual_information"]
        )

        # ----------------------------------------------
        # Check Informativeness
        # ----------------------------------------------

        if mutual_information_value > 0:

            informative_features += 1

        # ----------------------------------------------
        # Store Result
        # ----------------------------------------------

        results.append({

            "entity_1":
                feature_schema["column_name"],

            "entity_2":
                target_schema["column_name"],

            "status": (

                "Informative"

                if mutual_information_value > 0

                else

                "Low Information"

            ),

            "statistics": {

                "entropy":
                    entropy,

                "information_gain":
                    information_gain_value,

                "mutual_information":
                    mutual_information_value

            },

            "metadata": {

                "feature_type":
                    feature_schema["type"],

                "target_type":
                    target_type

            }

        })

    # --------------------------------------------------
    # Final Response
    # --------------------------------------------------

    return {

        "summary": {

            "target_detected": True,

            "target":
                target_schema["column_name"],

            "analyzed_features":
                analyzed_features,

            "informative_features":
                informative_features

        },

        "results": results,

        "recommendations": [],

        "metadata": {

            "module": "Information Theory",

            "version": "1.0"

        }

    }