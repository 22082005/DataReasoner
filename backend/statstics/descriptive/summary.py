import pandas as pd

from .central_tendancy import calculate_central_tendency
from .dispersion import calculate_dispersion
from .distribution import calculate_distribution
from .percentiles import calculate_percentile_statistics


# ==========================================================
# Single Column Summary
# ==========================================================

def descriptive_summary(series: pd.Series):
    """
    Generate descriptive statistics for a single column.

    Parameters
    ----------
    series : pandas.Series

    Returns
    -------
    dict
    """

    series = series.dropna()

    result = {
        "count": int(series.count())
    }

    # ---------------------------------------------
    # Numeric Columns
    # ---------------------------------------------

    if pd.api.types.is_numeric_dtype(series):

        result.update(
            calculate_central_tendency(series)
        )

        result.update(
            calculate_dispersion(series)
        )

        result.update(
            calculate_distribution(series)
        )

        result.update(
            calculate_percentile_statistics(series)
        )

    # ---------------------------------------------
    # Categorical Columns
    # ---------------------------------------------

    else:

        mode = series.mode()

        result.update({

            "unique_values":
                int(series.nunique()),

            "most_frequent":
                None if mode.empty else mode.iloc[0],

            "frequency":
                0 if mode.empty else int(
                    series.value_counts().iloc[0]
                )

        })

    return result


# ==========================================================
# Dataset Summary (Orchestrator)
# ==========================================================
import pandas as pd




def analyze_descriptive(
    df: pd.DataFrame,
    schema: list
):
    """
    Generate descriptive statistics for all eligible
    columns in the dataset.

    Parameters
    ----------
    df : pandas.DataFrame

    schema : list

    Returns
    -------
    dict
    """

    results = []

    analyzed_features = 0

    numeric_features = 0

    categorical_features = 0

    datetime_features = 0

    for column in schema:

        # -----------------------------------------
        # Skip Identifier
        # -----------------------------------------

        if column["semantic_role"] == "Identifier":
            continue

        # -----------------------------------------
        # Skip unwanted columns
        # -----------------------------------------

        if not column["use_for_analysis"]:
            continue

        analyzed_features += 1

        feature = column["column_name"]

        dtype = column["type"]

        if dtype in ["integer", "float"]:

            numeric_features += 1

        elif dtype == "string":

            categorical_features += 1

        elif dtype == "datetime":

            datetime_features += 1

        results.append({

            "feature": feature,

            "status": "Analyzed",

            "statistics": descriptive_summary(
                df[feature]
            ),

            "metadata": {

                "type": dtype,

                "semantic_role":
                    column["semantic_role"]

            }

        })

    return {

        "summary": {

            "analyzed_features":
                analyzed_features,

            "numeric_features":
                numeric_features,

            "categorical_features":
                categorical_features,

            "datetime_features":
                datetime_features

        },

        "results": results,

        "recommendations": [],

        "metadata": {

            "module": "Descriptive Statistics",

            "version": "1.0"

        }

    }