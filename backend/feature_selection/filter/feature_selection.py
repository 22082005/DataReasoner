import pandas as pd

from .selector import select_feature_selection_methods


def analyze_feature_selection(
    df: pd.DataFrame,
    schema: list
):
    """
    Perform feature selection for all eligible features.
    """

    # --------------------------------------
    # Find Target
    # --------------------------------------

    target_schema = None

    for column in schema:

        if column["semantic_role"] == "Target":

            target_schema = column

            break

    if target_schema is None:

        return []

    target = df[target_schema["column_name"]]

    results = []

    # --------------------------------------
    # Process Each Feature
    # --------------------------------------

    for feature_schema in schema:

        if feature_schema["semantic_role"] in [
            "Target",
            "Identifier"
        ]:
            continue

        if not feature_schema["use_for_analysis"]:
            continue

        feature = df[
            feature_schema["column_name"]
        ]

        feature_result = {

            "feature": feature_schema["column_name"],

            "target": target_schema["column_name"],

            "methods": []
        }

        methods = select_feature_selection_methods(

            feature_schema,

            target_schema

        )

        for method in methods:

            try:

                # -----------------------------
                # High Correlation
                # -----------------------------

                if method.__name__ == "high_correlation_filter":

                    result = method(
                        df,
                        schema
                    )

                # -----------------------------
                # Mutual Information
                # -----------------------------

                elif method.__name__ == "mutual_information_filter":

                    result = method(
                        feature,
                        target,
                        target_schema
                    )

                # -----------------------------
                # Chi-Square / ANOVA
                # -----------------------------

                elif method.__name__ in [

                    "chi_square_filter",

                    "anova_filter"

                ]:

                    result = method(
                        feature,
                        target
                    )

                # -----------------------------
                # Low Variance
                # -----------------------------

                else:

                    result = method(
                        feature
                    )

                feature_result["methods"].append(result)

            except Exception as e:

                feature_result["methods"].append(

                    {

                        "method": method.__name__,

                        "selected": False,

                        "reason": str(e)
                    }

                )

        results.append(feature_result)

    return results