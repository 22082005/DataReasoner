from statstics.descriptive.dispersion import calculate_variance


def low_variance_filter(
    series,
    threshold=0.01
):
    """
    Determine whether a feature should be removed
    based on its variance.

    Parameters
    ----------
    series : pandas.Series

    threshold : float, default=0.01

    Returns
    -------
    dict
    """

    result = calculate_variance(series)

    feature_variance = result["variance"]

    if feature_variance is None:

        return {

            "method": "Low Variance",

            "variance": None,

            "selected": False,

            "reason": "Unable to calculate variance.",

            "recommendation":
                "Review feature manually."
        }

    if feature_variance < threshold:

        return {

            "method": "Low Variance",

            "variance": feature_variance,

            "selected": False,

            "reason":
                f"Variance ({feature_variance}) is below the threshold ({threshold}).",

            "recommendation":
                "Remove feature because it contains very little information."
        }

    return {

        "method": "Low Variance",

        "variance": feature_variance,

        "selected": True,

        "reason":
            f"Variance ({feature_variance}) is above the threshold ({threshold}).",

        "recommendation":
            "Retain feature."
    }