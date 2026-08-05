from eda.utils import create_insight


def generate_insights(

    missing_values=None,

    duplicates=None,

    outliers=None,

    correlation=None,

    hypothesis=None,

    feature_selection=None

):
    """
    Generate EDA insights from analysis modules.

    Parameters
    ----------
    missing_values : dict

    duplicates : dict

    outliers : list

    correlation : list

    hypothesis : list

    feature_selection : list

    Returns
    -------
    list
    """

    insights = []

    # ----------------------------------
    # Missing Values
    # ----------------------------------

    if missing_values is not None:

     summary = missing_values["summary"]

     if summary["has_missing"]:

        insights.append(

            create_insight(

                category="Missing Values",

                title="Missing values detected",

                description=(
                    f"{summary['total_missing']} "
                    "missing values were found across "
                    f"{summary['columns_with_missing']} columns."
                ),

                priority=1,

                recommendation=(
                    "Consider an imputation strategy."
                ),

                source="Missing Values"

            )

        )

    # ----------------------------------
    # Duplicate Records
    # ----------------------------------

    if duplicates is not None:
        summary = duplicates["summary"]

        if summary["duplicate_rows"] > 0:

            insights.append(

                create_insight(

                    category="Duplicates",

                    title="Duplicate rows detected",

                    description=(
                        f"{summary['duplicate_rows']} "
                        "duplicate records were found."
                    ),

                    priority=1,

                    recommendation=(
                        "Review duplicate records before modelling."
                    ),

                    source="Duplicates"

                )

            )

    # ----------------------------------
    # Outliers
    # ----------------------------------

    if outliers is not None:

        for result in outliers:

            if result["outlier_count"] > 0:

                insights.append(

                    create_insight(

                        category="Outliers",

                        title=(
                            f"Outliers detected in "
                            f"{result['column_name']}"
                        ),

                        description=(

                            f"{result['outlier_count']} "

                            "outliers were detected."

                        ),

                        priority=2,

                        recommendation=(

                            "Inspect the distribution "

                            "before training."

                        ),

                        source="Outlier Detection"

                    )

                )

    # ----------------------------------
    # Correlation
    # ----------------------------------

    if correlation is not None:

        for result in correlation:

            if abs(result["correlation"]) >= 0.90:

                insights.append(

                    create_insight(

                        category="Correlation",

                        title="Strong relationship",

                        description=(

                            f"{result['column_1']} "

                            f"and "

                            f"{result['column_2']} "

                            "are highly correlated."

                        ),

                        priority=2,

                        recommendation=(

                            "Review whether both "

                            "features are required."

                        ),

                        source="Correlation"

                    )

                )

    return insights