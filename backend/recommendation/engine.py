from .visual_evidence import (
    attach_visualizations
)


def generate_recommendations(
    information=None,
    hypothesis=None,
    feature_selection=None,
    correlation=None,
    visualization=None
):
    """
    Generate data-driven recommendations
    by combining multiple EDA results.
    """

    recommendations = []

    # -----------------------------------------
    # Build hypothesis lookup
    # -----------------------------------------

    hypothesis_lookup = {}

    if hypothesis is not None:

        for result in hypothesis.get(
            "results",
            []
        ):

            feature = result.get(
                "entity_1"
            )

            if feature:

                hypothesis_lookup[feature] = result

    # -----------------------------------------
    # Information Theory
    # -----------------------------------------

    if information is not None:

        for result in information.get(
            "results",
            []
        ):

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

            mi = statistics.get(
                "mutual_information"
            )

            if mi is None:
                continue

            # ---------------------------------
            # Find hypothesis result
            # ---------------------------------

            hypothesis_result = (
                hypothesis_lookup.get(
                    feature
                )
            )

            hypothesis_status = None

            if hypothesis_result is not None:

                hypothesis_status = (
                    hypothesis_result.get(
                        "status"
                    )
                )

            # ---------------------------------
            # Determine evidence strength
            # ---------------------------------

            if (
                mi >= 0.75
                and
                hypothesis_status ==
                "Statistically Significant"
            ):

                assessment = (
                    "Strong evidence"
                )

                priority = 1

                recommendation = (

                    f"{feature} shows strong "
                    f"evidence of being useful "
                    f"for distinguishing {target}. "
                    f"Prioritize it for further "
                    f"model evaluation."

                )

            elif (
                mi >= 0.30
                and
                hypothesis_status ==
                "Statistically Significant"
            ):

                assessment = (
                    "Moderate evidence"
                )

                priority = 2

                recommendation = (

                    f"{feature} shows a meaningful "
                    f"relationship with {target}, "
                    f"but the evidence is weaker "
                    f"than the strongest features. "
                    f"Consider it during model evaluation."

                )

            elif (
                hypothesis_status ==
                "Statistically Significant"
            ):

                assessment = (
                    "Statistically significant "
                    "but weaker information"
                )

                priority = 2

                recommendation = (

                    f"{feature} has a statistically "
                    f"significant relationship with "
                    f"{target}, although its information "
                    f"strength is comparatively lower. "
                    f"Keep it under consideration "
                    f"during model evaluation."

                )

            elif mi >= 0.75:

                assessment = (
                    "Strong information relationship"
                )

                priority = 2

                recommendation = (

                    f"{feature} has a strong "
                    f"information relationship with "
                    f"{target}. Investigate this "
                    f"feature further before modelling."

                )

            else:

                assessment = (
                    "Limited evidence"
                )

                priority = 3

                recommendation = (

                    f"{feature} shows comparatively "
                    f"limited evidence of a strong "
                    f"relationship with {target}. "
                    f"Compare it with other features "
                    f"before making modelling decisions."

                )

            # ---------------------------------
            # Create recommendation
            # ---------------------------------

            recommendations.append({

                "category":
                    "Feature Analysis",

                "title":
                    f"{feature}: {assessment}",
                "feature": feature,

                "target": target,

                "description": (

                    f"{feature} was evaluated against "
                    f"the target {target} using "
                    f"information theory and "
                    f"hypothesis testing."

                ),

                "priority":
                    priority,

                "evidence": {

                    "mutual_information":
                        mi,

                    "hypothesis_test":
                        hypothesis_status

                },

                "recommendation":
                    recommendation,

                "source":
                    "Information Theory + "
                    "Hypothesis Testing"

            })

    # -----------------------------------------
    # Sort by priority
    # -----------------------------------------

    recommendations.sort(
        key=lambda x: x["priority"]
    )

    recommendations = attach_visualizations(
    recommendations,
    visualization
    )
    print("\nAFTER VISUALIZATION ATTACHMENT:")
    print(recommendations)

    return recommendations