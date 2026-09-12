import pandas as pd

from .selector import select_visualizations
from .bivariate.heatmap import heatmap
from .bivariate.scatter import scatter

from statstics.correlation.corr import (
    analyze_correlation
)


def analyze_visualization(
    df: pd.DataFrame,
    schema: list
):
    """
    Generate visualization recommendations.

    Returns
    -------
    dict
    """

    feature_results = []

    bivariate_results = []

    dataset_results = []

    target_schema = None

    # -----------------------------------------
    # Target
    # -----------------------------------------

    for column in schema:

        if column["semantic_role"] == "Target":

            target_schema = column

            break

    # -----------------------------------------
    # Feature Visualizations
    # -----------------------------------------

    analyzed_features = 0

    for feature_schema in schema:

        if feature_schema["semantic_role"] == "Identifier":

            continue

        if not feature_schema["use_for_analysis"]:

            continue

        analyzed_features += 1

        feature = df[
            feature_schema["column_name"]
        ]

        visualizations = []

        methods = select_visualizations(

            feature_schema,

            target_schema

        )

        for method in methods:

            try:

                # ---------------------------------
                # Univariate visualizations
                # ---------------------------------

                if method.__name__ in [

                    "histogram",
                    "boxplot",
                    "density",
                    "violin",
                    "bar",
                    "pie"

                ]:

                    chart = method(
                        feature
                    )

                    visualizations.append(
                        chart
                    )

                # ---------------------------------
                # Feature + Target visualizations
                # ---------------------------------

                elif method.__name__ in [

                    "grouped_boxplot",
                    "grouped_bar"

                ]:

                    if target_schema is None:
                        continue

                    chart = method(

                        feature,

                        df[
                            target_schema[
                                "column_name"
                            ]
                        ]

                    )

                    visualizations.append(
                        chart
                    )

            except Exception as e:

                visualizations.append({

                    "chart_type":
                        method.__name__,

                    "status":
                        "Failed",

                    "reason":
                        str(e)

                })

        feature_results.append({

            "feature":
                feature_schema[
                    "column_name"
                ],

            "status":
                "Visualizations Generated",

            "statistics": {

                "recommended_charts":
                    len(visualizations)

            },

            "metadata": {

                "charts":
                    visualizations

            }

        })

    # -----------------------------------------
    # Bivariate Scatter Visualizations
    # -----------------------------------------

    numeric_features = []

    for feature_schema in schema:

        if feature_schema[
            "semantic_role"
        ] == "Identifier":

            continue

        if not feature_schema[
            "use_for_analysis"
        ]:

            continue

        if feature_schema[
            "type"
        ].lower() in [

            "integer",
            "int",
            "float",
            "double"

        ]:

            numeric_features.append(
                feature_schema
            )

    # -----------------------------------------
    # Generate scatter plots for every
    # pair of numeric features
    # -----------------------------------------

    for i in range(
        len(numeric_features)
    ):

        for j in range(
            i + 1,
            len(numeric_features)
        ):

            x_schema = numeric_features[i]

            y_schema = numeric_features[j]

            x = df[
                x_schema[
                    "column_name"
                ]
            ]

            y = df[
                y_schema[
                    "column_name"
                ]
            ]

            try:

                target = None

                if target_schema is not None:

                 target = df[
                 target_schema["column_name"]
              ]


                chart = scatter(

                x,

                y,

                target

)

                bivariate_results.append(
                    chart
                )

            except Exception as e:

                bivariate_results.append({

                    "chart_type":
                        "scatter",

                    "status":
                        "Failed",

                    "reason":
                        str(e)

                })

    # -----------------------------------------
    # Dataset Visualization
    # -----------------------------------------

    correlation = analyze_correlation(
        df,
        schema
    )

    dataset_results.append({

        "status":
            "Dataset Visualization",

        "statistics": {

            "chart_count":
                1

        },

        "metadata": {

            "charts": [

                heatmap(

                    correlation[
                        "results"
                    ]

                )

            ]

        }

    })

    # -----------------------------------------
    # Final Response
    # -----------------------------------------

    return {

        "summary": {

            "analyzed_features":
                analyzed_features,

            "feature_visualizations":
                len(feature_results),

            "bivariate_visualizations":
                len(bivariate_results),

            "dataset_visualizations":
                len(dataset_results)

        },

        "results": {

            "feature_visualizations":
                feature_results,

            "bivariate_visualizations":
                bivariate_results,

            "dataset_visualizations":
                dataset_results

        },

        "recommendations": [],

        "metadata": {

            "module":
                "Visualization",

            "version":
                "1.0"

        }

    }