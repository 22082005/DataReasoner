from statstics.correlation.corr import analyze_correlation


def high_correlation_filter(
    df,
    schema,
    threshold=0.90
):
    """
    Identify highly correlated features.

    Parameters
    ----------
    df : pandas.DataFrame

    schema : list

    threshold : float

    Returns
    -------
    list
    """

    correlation_results = analyze_correlation(
        df,
        schema
    )

    selected_features = set(df.columns)

    recommendations = []

    for result in correlation_results:

        correlation = result["correlation"]

        if correlation is None:
            continue

        if abs(correlation) >= threshold:

            feature_to_remove = result["column_2"]

            if feature_to_remove in selected_features:
                selected_features.remove(feature_to_remove)

            recommendations.append({

                "method": "High Correlation",

                "feature_1": result["column_1"],

                "feature_2": result["column_2"],

                "correlation": correlation,

                "selected": False,

                "reason":
                    f"Correlation ({correlation}) exceeds threshold ({threshold}).",

                "recommendation":
                    f"Consider removing '{feature_to_remove}' because it provides similar information."
            })

    return {

        "selected_features": list(selected_features),

        "recommendations": recommendations
    }