import pandas as pd

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


from recommendation.engine import generate_recommendations

def analyze_eda(
    df: pd.DataFrame,
    target: str,
    debug: bool = False
):
    """
    Perform complete Exploratory Data Analysis.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.

    target : str
        Target column explicitly selected by the user.

    debug : bool, default=False
        Print intermediate outputs.

    Returns
    -------
    dict
        Complete EDA results.
    """

    # -------------------------------------------------
    # Schema
    # -------------------------------------------------

    schema = infer_schema(df)

    # -------------------------------------------------
    # Preprocessing
    # -------------------------------------------------

    missing_values = analyze_missing_values(
        df
    )

    duplicates = analyze_duplicates(
        df
    )

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

    # Target-aware hypothesis testing
    hypothesis = analyze_hypothesis_testing(
        df,
        schema,
        target
    )

    # Target-aware information theory
    information = analyze_information(
        df,
        schema,
        target
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
        schema,
        target
    )

    # -------------------------------------------------
    # Debug Mode
    # -------------------------------------------------

    if debug:

        print("Debug Mode")

        print("\nSchema:")
        print(schema)

        print("\nMissing Values:")
        print(missing_values)

        print("\nDuplicates:")
        print(duplicates)

        print("\nOutliers:")
        print(outliers)

        print("\nDescriptive Statistics:")
        print(descriptive)

        print("\nCorrelation:")
        print(correlation)

        print("\nHypothesis Testing:")
        print(hypothesis)

        print("\nInformation Theory:")
        print(information)

        print("\nFeature Selection:")
        print(feature_selection)

        print("\nVisualization:")
        print(visualization)

        print("\nSummary:")
        print(summary)

        return None

    # -------------------------------------------------
    # Insights
    # -------------------------------------------------

    insights = generate_insights(

    missing_values=missing_values,

    duplicates=duplicates,

    outliers=outliers,

    correlation=correlation,

    hypothesis=hypothesis,

    information=information,

    feature_selection=feature_selection,

    visualization=visualization

    )
    insights = select_insights(
        insights
    )

    # -------------------------------------------------
# Recommendations
# -------------------------------------------------

    recommendations = generate_recommendations(

    information=information,

    hypothesis=hypothesis,

    feature_selection=feature_selection,

    correlation=correlation,

    visualization=visualization

)
    print("\nRECOMMENDATIONS:")
    print(recommendations)
    

    # -------------------------------------------------
    # Final Result
    # -------------------------------------------------
 
    return {

        "summary": summary,

        "schema": schema,

        "preprocessing": {

            "missing_values":
                missing_values,

            "duplicates":
                duplicates,

            "outliers":
                outliers

        },

        "statistics": {

            "descriptive":
                descriptive,

            "correlation":
                correlation,

            "hypothesis":
                hypothesis,

            "information_theory":
                information

        },

        "feature_selection":
            feature_selection,

        "visualization":
            visualization,

        "insights":
            insights

    }