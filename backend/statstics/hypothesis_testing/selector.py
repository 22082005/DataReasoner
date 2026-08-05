from statstics.normality.selector import select_normality_test

from .chi_square import chi_square_test
from .t_test import independent_t_test
from .anova import anova_test
from .mann_whitney import mann_whitney_test
from .kruskals_wallis import kruskal_wallis_test


def select_hypothesis_test(
    feature,
    target,
    feature_schema,
    target_schema
):
    """
    Select the appropriate hypothesis test.
    """

    feature_type = feature_schema["type"].lower()
    target_type = target_schema["type"].lower()

    target_groups = target.dropna().nunique()

    # ---------------------------------------------
    # Numeric & Categorical Types
    # ---------------------------------------------
    numeric_types = ["integer", "float", "int", "double"]
    categorical_types = [
        "string",
        "category",
        "categorical",
        "object"
    ]

    # ---------------------------------------------
    # Rule 1
    # Categorical vs Categorical
    # ---------------------------------------------
    if (
        feature_type in categorical_types
        and
        target_type in categorical_types
    ):

        return {

            "selected_test": chi_square_test,

            "reason":
                "Categorical feature and categorical target.",

            "alternatives": []
        }

    # ---------------------------------------------
    # Rule 2
    # Numeric vs Binary Target
    # ---------------------------------------------
    if (
        feature_type in numeric_types
        and
        target_groups == 2
    ):

        normality = select_normality_test(feature)

        normality_result = normality["selected_test"](feature)

        if normality_result["is_normal"]:

            return {

                "selected_test": independent_t_test,

                "reason":
                    "Binary target with normally distributed feature.",

                "alternatives": [
                    mann_whitney_test
                ]
            }

        return {

            "selected_test": mann_whitney_test,

            "reason":
                "Binary target with non-normal feature.",

            "alternatives": [
                independent_t_test
            ]
        }

    # ---------------------------------------------
    # Rule 3
    # Numeric vs Multi-Class Target
    # ---------------------------------------------
    if (
        feature_type in numeric_types
        and
        target_groups > 2
    ):

        normality = select_normality_test(feature)

        normality_result = normality["selected_test"](feature)

        if normality_result["is_normal"]:

            return {

                "selected_test": anova_test,

                "reason":
                    "Multi-class target with normally distributed feature.",

                "alternatives": [
                    kruskal_wallis_test
                ]
            }

        return {

            "selected_test": kruskal_wallis_test,

            "reason":
                "Multi-class target with non-normal feature.",

                "alternatives": [
                    anova_test
                ]
        }

    # ---------------------------------------------
    # No Suitable Test
    # ---------------------------------------------
    return {

        "selected_test": None,

        "reason":
            (
                f"No hypothesis test available "
                f"(feature_type={feature_type}, "
                f"target_type={target_type}, "
                f"groups={target_groups})"
            ),

        "alternatives": []
    }