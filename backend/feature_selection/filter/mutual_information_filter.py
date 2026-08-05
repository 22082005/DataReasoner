from statstics.information_theory.mutual_information import (
    mutual_information
)


def mutual_information_filter(
    feature,
    target,
    target_schema,
    threshold=0.01
):
    """
    Select a feature using Mutual Information.

    Parameters
    ----------
    feature : pandas.Series

    target : pandas.Series

    target_schema : dict

    threshold : float, default=0.01

    Returns
    -------
    dict
    """

    categorical_types = [
        "string",
        "category",
        "categorical",
        "object"
    ]

    target_type = (
        "categorical"
        if target_schema["type"].lower() in categorical_types
        else "continuous"
    )

    result = mutual_information(
        feature,
        target,
        target_type
    )

    score = result["mutual_information"]

    if score is None:

        return {

            "method": "Mutual Information Filter",

            "selected": False,

            "reason":
                "Unable to compute Mutual Information.",

            "recommendation":
                "Review the feature manually.",

            "statistics": result
        }

    if score >= threshold:

        return {

            "method": "Mutual Information Filter",

            "selected": True,

            "reason":
                (
                    f"Mutual Information ({score}) "
                    f"is greater than or equal to "
                    f"the threshold ({threshold})."
                ),

            "recommendation":
                "Retain the feature.",

            "statistics": result
        }

    return {

        "method": "Mutual Information Filter",

        "selected": False,

        "reason":
            (
                f"Mutual Information ({score}) "
                f"is below the threshold ({threshold})."
            ),

        "recommendation":
            "Consider removing the feature.",

        "statistics": result
    }