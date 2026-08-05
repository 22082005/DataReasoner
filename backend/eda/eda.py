import pandas as pd
from pprint import pprint

from scchema_inference.infer_schema import infer_schema

from preprocessing.missing_values import analyze_missing_values
from preprocessing.duplicates import analyze_duplicates
from preprocessing.outliers.outlier import analyze_outliers

from statstics.descriptive.summary import analyze_descriptive
from statstics.correlation.corr import analyze_correlation
from statstics.hypothesis_testing.hypothesis import (
    analyze_hypothesis_testing
)
from statstics.information_theory.information import (
    analyze_information
)

from feature_selection.filter.feature_selection import (
    analyze_feature_selection
)

from visualization.visualize import analyze_visualization

from eda.summary import generate_summary
from eda.insights import generate_insights
from eda.selector import select_insights


def analyze_eda(
    df: pd.DataFrame,
    debug: bool = False
):
    """
    Perform complete Exploratory Data Analysis.

    Parameters
    ----------
    df : pandas.DataFrame

    debug : bool, default=False
        Print intermediate outputs.

    Returns
    -------
    dict
    """

    # -------------------------------------------------
    # Schema
    # -------------------------------------------------

    schema = infer_schema(df)

    # -------------------------------------------------
    # Preprocessing
    # -------------------------------------------------

    missing_values = analyze_missing_values(df)

    duplicates = analyze_duplicates(df)

    outliers = analyze_outliers(
        df,
        schema
    )

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    descriptive = analyze_descriptive(
        df,
        schema
    )

    correlation = analyze_correlation(
        df,
        schema
    )

    hypothesis = analyze_hypothesis_testing(
        df,
        schema
    )

    information = analyze_information(
        df,
        schema
    )

    # -------------------------------------------------
    # Feature Selection
    # -------------------------------------------------

    feature_selection = analyze_feature_selection(
        df,
        schema
    )

    # -------------------------------------------------
    # Visualization
    # -------------------------------------------------

    visualization = analyze_visualization(
        df,
        schema
    )

    # -------------------------------------------------
    # Summary
    # -------------------------------------------------

    summary = generate_summary(
        df,
        schema
    )

    # -------------------------------------------------
    # Debug Mode
    # -------------------------------------------------

    if debug:

        print("Debug Mode")

        return

    # -------------------------------------------------
    # Insights
    # -------------------------------------------------

    insights = generate_insights(

        missing_values=missing_values,

        duplicates=duplicates,

        outliers=outliers,

        correlation=correlation,

        hypothesis=hypothesis,

        feature_selection=feature_selection

    )

    insights = select_insights(
        insights
    )

    # -------------------------------------------------
    # Final Result
    # -------------------------------------------------

    return {

        "summary": summary,

        "schema": schema,

        "preprocessing": {

            "missing_values": missing_values,

            "duplicates": duplicates,

            "outliers": outliers

        },

        "statistics": {

            "descriptive": descriptive,

            "correlation": correlation,

            "hypothesis": hypothesis,

            "information_theory": information

        },

        "feature_selection": feature_selection,

        "visualization": visualization,

        "insights": insights

    }