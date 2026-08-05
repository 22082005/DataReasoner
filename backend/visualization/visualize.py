import pandas as pd

from .selector import select_visualizations
from .bivariate.heatmap import heatmap

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

                if method.__name__ in [

                    "histogram",
                    "boxplot",
                    "density",
                    "violin",
                    "bar",
                    "pie"

                ]:

                    chart = method(feature)

                elif method.__name__ in [

                    "scatter",

                    "grouped_boxplot",

                    "grouped_bar"

                ]:

                    chart = method(

                        feature,

                        df[target_schema["column_name"]]

                    )

                else:

                    continue

                visualizations.append(chart)

            except Exception as e:

                visualizations.append({

                    "chart_type": method.__name__,

                    "status": "Failed",

                    "reason": str(e)

                })

        feature_results.append({

            "feature":

                feature_schema["column_name"],

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
    # Dataset Visualization
    # -----------------------------------------

    correlation = analyze_correlation(
        df,
        schema
    )

    dataset_results.append({

        "status": "Dataset Visualization",

        "statistics": {

            "chart_count": 1

        },

        "metadata": {

            "charts": [

                heatmap(

                    correlation

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

            "dataset_visualizations":

                len(dataset_results)

        },

        "results": {

            "feature_visualizations":

                feature_results,

            "dataset_visualizations":

                dataset_results

        },

        "recommendations": [],

        "metadata": {

            "module": "Visualization",

            "version": "1.0"

        }

    }