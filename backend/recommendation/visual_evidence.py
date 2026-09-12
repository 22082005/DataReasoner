def attach_visualizations(
    recommendations,
    visualization
):
    """
    Attach relevant visualizations to
    each recommendation.
    """

    if not recommendations:
        return []

    if not visualization:
        return recommendations

    results = visualization.get(
        "results",
        {}
    )

    feature_visualizations = results.get(
        "feature_visualizations",
        []
    )

    dataset_visualizations = results.get(
        "dataset_visualizations",
        []
    )

    # -----------------------------------------
    # Build feature -> charts lookup
    # -----------------------------------------

    feature_charts = {}

    for item in feature_visualizations:

        feature = item.get(
            "feature"
        )

        if not feature:
            continue

        charts = item.get(
            "metadata",
            {}
        ).get(
            "charts",
            []
        )

        feature_charts.setdefault(
            feature,
            []
        ).extend(charts)

    # -----------------------------------------
    # Attach charts to recommendations
    # -----------------------------------------

    for recommendation in recommendations:

        feature = recommendation.get(
            "feature"
        )

        if not feature:
            continue

        relevant_charts = []

        # -------------------------------------
        # Feature-level charts
        # -------------------------------------

        relevant_charts.extend(
            feature_charts.get(
                feature,
                []
            )
        )

        # -------------------------------------
        # Find charts where feature appears
        # in x_axis or y_axis
        # -------------------------------------

        for charts in feature_charts.values():

            for chart in charts:

                x_axis = chart.get(
                    "x_axis"
                )

                y_axis = chart.get(
                    "y_axis"
                )

                if feature in [
                    x_axis,
                    y_axis
                ]:

                    relevant_charts.append(
                        chart
                    )

        # -------------------------------------
        # Remove duplicates
        # -------------------------------------

        unique_charts = []

        seen = set()

        for chart in relevant_charts:

            key = (
                chart.get("chart_type"),
                chart.get("title")
            )

            if key in seen:
                continue

            seen.add(key)

            unique_charts.append(
                chart
            )

        # -------------------------------------
        # Attach
        # -------------------------------------

        recommendation[
            "visualizations"
        ] = unique_charts

    return recommendations