from .univariate.histogram import histogram
from .univariate.boxplot import boxplot
from .univariate.density import density
from .univariate.violin import violin
from .univariate.bar import bar
from .univariate.pie import pie

from .bivariate.scatter import scatter
from .bivariate.grouped_box import grouped_boxplot
from .bivariate.grouped_bar import grouped_bar
from .bivariate.heatmap import heatmap


def select_visualizations(
    feature_schema,
    target_schema=None
):
    """
    Select appropriate visualizations based on
    feature and target characteristics.

    Parameters
    ----------
    feature_schema : dict

    target_schema : dict, optional

    Returns
    -------
    list
    """

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

    feature_type = feature_schema["type"].lower()

    target_type = None

    if target_schema is not None:

        target_type = target_schema["type"].lower()

    methods = []

    # --------------------------------------
    # Univariate
    # --------------------------------------

    if feature_type in numeric_types:

        methods.extend([

            histogram,

            boxplot,

            density,

            violin

        ])

    elif feature_type in categorical_types:

        methods.extend([

            bar,

            pie

        ])

    # --------------------------------------
    # Bivariate
    # --------------------------------------

    if target_schema is not None:

        if (

            feature_type in numeric_types

            and

            target_type in numeric_types

        ):

            methods.append(scatter)

        elif (

            feature_type in numeric_types

            and

            target_type in categorical_types

        ):

            methods.append(grouped_boxplot)

        elif (

            feature_type in categorical_types

            and

            target_type in categorical_types

        ):

            methods.append(grouped_bar)

    return methods