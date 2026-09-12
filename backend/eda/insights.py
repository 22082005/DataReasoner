from eda.utils import create_insight


def generate_insights(

    missing_values=None,
    duplicates=None,
    outliers=None,
    correlation=None,
    hypothesis=None,
    information=None,
    feature_selection=None,
    visualization=None

):
    """
    Generate EDA insights from analysis modules.

    Parameters
    ----------
    missing_values : dict
        Missing value analysis results.

    duplicates : dict
        Duplicate analysis results.

    outliers : dict
        Outlier detection results.

    correlation : dict
        Correlation analysis results.

    hypothesis : dict
        Hypothesis testing results.

    information : dict
        Information Theory analysis results.

    feature_selection : dict
        Feature selection results.

    visualization : dict
        Visualization analysis results.

    Returns
    -------
    list
        Generated EDA insights.
    """

    insights = []

    # ----------------------------------
    # Missing Values
    # ----------------------------------

    if missing_values is not None:

        summary = missing_values.get(
            "summary",
            {}
        )

        if summary.get(
            "has_missing",
            False
        ):

            insights.append(

                create_insight(

                    category="Missing Values",

                    title="Missing values detected",

                    description=(

                        f"{summary.get('total_missing', 0)} "
                        "missing values were found across "
                        f"{summary.get('columns_with_missing', 0)} "
                        "columns."

                    ),

                    priority=1,

                    recommendation=(

                        "Consider an appropriate imputation "
                        "strategy before modelling."

                    ),

                    source="Missing Values"

                )

            )

    # ----------------------------------
    # Duplicate Records
    # ----------------------------------

    if duplicates is not None:

        summary = duplicates.get(
            "summary",
            {}
        )

        if summary.get(
            "duplicate_rows",
            0
        ) > 0:

            insights.append(

                create_insight(

                    category="Duplicates",

                    title="Duplicate rows detected",

                    description=(

                        f"{summary.get('duplicate_rows', 0)} "
                        "duplicate records were found."

                    ),

                    priority=1,

                    recommendation=(

                        "Review duplicate records before "
                        "modelling."

                    ),

                    source="Duplicates"

                )

            )

    # ----------------------------------
    # Outliers
    # ----------------------------------

    if outliers is not None:

        results = outliers.get(
            "results",
            []
        )

        for result in results:

            outlier_count = result.get(
                "count",
                0
            )

            if outlier_count > 0:

                feature = result.get(
                    "feature",
                    "Unknown feature"
                )

                percentage = result.get(
                    "percentage",
                    0
                )

                insights.append(

                    create_insight(

                        category="Outliers",

                        title=(

                            f"Outliers detected in "
                            f"{feature}"

                        ),

                        description=(

                            f"{outlier_count} outliers "
                            f"({percentage}%) were detected."

                        ),

                        priority=2,

                        recommendation=(

                            "Inspect the distribution and "
                            "determine whether the observations "
                            "are genuine or anomalous."

                        ),

                        source="Outlier Detection"

                    )

                )

    # ----------------------------------
    # Correlation
    # ----------------------------------

    if correlation is not None:

        results = correlation.get(
            "results",
            []
        )

        for result in results:

            statistics = result.get(
                "statistics",
                {}
            )

            correlation_value = statistics.get(
                "correlation"
            )

            if (

                correlation_value is not None

                and

                abs(correlation_value) >= 0.90

            ):

                feature = result.get(
                    "feature",
                    "Unknown feature"
                )

                related_feature = statistics.get(
                    "related_feature",
                    "Unknown feature"
                )

                insights.append(

                    create_insight(

                        category="Correlation",

                        title="Strong relationship",

                        description=(

                            f"{feature} and "
                            f"{related_feature} "
                            "show a very strong "
                            "correlation."

                        ),

                        priority=2,

                        recommendation=(

                            "Review whether both features "
                            "are required, particularly when "
                            "building predictive models."

                        ),

                        source="Correlation"

                    )

                )

    # ----------------------------------
    # Hypothesis Testing
    # ----------------------------------

    if hypothesis is not None:

        results = hypothesis.get(
            "results",
            []
        )

        for result in results:

            if result.get(
                "status"
            ) == "Statistically Significant":

                feature = result.get(
                    "entity_1",
                    "Unknown feature"
                )

                target = result.get(
                    "entity_2",
                    "target"
                )

                insights.append(

                    create_insight(

                        category="Hypothesis Testing",

                        title=(
                            "Statistically significant feature"
                        ),

                        description=(

                            f"{feature} shows a statistically "
                            f"significant relationship with "
                            f"the target {target}."

                        ),

                        priority=2,

                        recommendation=(

                            "Consider this feature as a "
                            "potentially useful predictor."

                        ),

                        source="Hypothesis Testing"

                    )

                )

    # ----------------------------------
    # Information Theory
    # ----------------------------------

    if information is not None:

        results = information.get(
            "results",
            []
        )

        for result in results:

            if result.get(
                "status"
            ) == "Informative":

                feature = result.get(
                    "entity_1",
                    "Unknown feature"
                )

                target = result.get(
                    "entity_2",
                    "target"
                )

                statistics = result.get(
                    "statistics",
                    {}
                )

                mutual_information_value = (
                    statistics.get(
                        "mutual_information"
                    )
                )

                insights.append(

                    create_insight(

                        category="Information Theory",

                        title="Informative feature",

                        description=(

                            f"{feature} contains information "
                            f"about the target {target}. "

                            f"Mutual information: "
                            f"{mutual_information_value}."

                        ),

                        priority=2,

                        recommendation=(

                            "Consider this feature during "
                            "feature selection and modelling."

                        ),

                        source="Information Theory"

                    )

                )

    # ----------------------------------
    # Final Insights
    # ----------------------------------

    return insights