from .low_variance import low_variance_filter
from .high_correlation import high_correlation_filter
from .chi_square_filter import chi_square_filter
from .annova_filter import anova_filter
from .mutual_information_filter import (
    mutual_information_filter
)


def select_feature_selection_methods(
    feature_schema,
    target_schema
):
    """
    Select appropriate feature selection methods
    based on feature and target characteristics.
    """

    feature_type = feature_schema["type"].lower()
    target_type = target_schema["type"].lower()

    numeric_types = [
        "integer",
        "float",
        "double",
        "int"
    ]

    categorical_types = [
        "string",
        "category",
        "categorical",
        "object"
    ]

    methods = []

    # --------------------------------------
    # Numeric Features
    # --------------------------------------

    if feature_type in numeric_types:

        methods.append(low_variance_filter)

        methods.append(high_correlation_filter)

        methods.append(mutual_information_filter)

        if target_type in categorical_types:

            methods.append(anova_filter)

    # --------------------------------------
    # Categorical Features
    # --------------------------------------

    elif feature_type in categorical_types:

        methods.append(mutual_information_filter)

        if target_type in categorical_types:

            methods.append(chi_square_filter)

    # --------------------------------------

    return methods