import pandas as pd

from .entropy import calculate_entropy
from .information_gain import information_gain
from .mutual_information import mutual_information


def analyze_information(
    df: pd.DataFrame,
    schema: list
):
    """
    Analyze Information Theory statistics for all
    features against the target.

    Returns
    -------
    dict
    """

    target_schema = None

    for column in schema:

        if column["semantic_role"] == "Target":

            target_schema = column

            break

    # --------------------------------------------------
    # No Target
    # --------------------------------------------------

    if target_schema is None:

        return {

            "summary": {

                "target_detected": False,

                "analyzed_features": 0

            },

            "results": [],

            "recommendations": [],

            "metadata": {

                "module": "Information Theory",

                "version": "1.0"

            }

        }

    target = df[target_schema["column_name"]]

    categorical_types = [

        "string",

        "category",

        "categorical",

        "object"

    ]

    target_type = (

        "categorical"

        if target_schema["type"].lower() in categorical_types

        else "continuous"

    )

    analyzed_features = 0

    informative_features = 0

    results = []

    # --------------------------------------------------
    # Feature Analysis
    # --------------------------------------------------

    for feature_schema in schema:

        if feature_schema["semantic_role"] in [

            "Target",

            "Identifier"

        ]:

            continue

        if not feature_schema["use_for_analysis"]:

            continue

        analyzed_features += 1

        feature = df[feature_schema["column_name"]]

        entropy = None

        information_gain_value = None

        if feature_schema["type"].lower() in categorical_types:

            entropy = calculate_entropy(

                feature

            )

            information_gain_value = information_gain(

                feature,

                target

            )

        mutual_information_value = mutual_information(

            feature,

            target,

            target_type

        )

        if mutual_information_value > 0:

            informative_features += 1

        results.append({

            "entity_1": feature_schema["column_name"],

            "entity_2": target_schema["column_name"],

            "status": (

                "Informative"

                if mutual_information_value > 0

                else

                "Low Information"

            ),

            "statistics": {

                "entropy": entropy,

                "information_gain": information_gain_value,

                "mutual_information": mutual_information_value

            },

            "metadata": {

                "feature_type": feature_schema["type"],

                "target_type": target_type

            }

        })

    return {

        "summary": {

            "target_detected": True,

            "target": target_schema["column_name"],

            "analyzed_features": analyzed_features,

            "informative_features": informative_features

        },

        "results": results,

        "recommendations": [],

        "metadata": {

            "module": "Information Theory",

            "version": "1.0"

        }

    }