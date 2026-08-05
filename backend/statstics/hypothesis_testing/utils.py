def validate_alpha(alpha: float):
    """
    Validate the significance level (alpha).

    Parameters
    ----------
    alpha : float
        Significance level.

    Raises
    ------
    TypeError
        If alpha is not numeric.

    ValueError
        If alpha is not between 0 and 1.
    """

    if not isinstance(alpha, (int, float)):
        raise TypeError(
            "alpha must be a numeric value."
        )

    if not 0 < alpha < 1:
        raise ValueError(
            "alpha must be between 0 and 1."
        )


def interpret_p_value(
    p_value: float | None,
    alpha: float = 0.05
) -> dict:
    """
    Interpret the p-value of a hypothesis test.

    Parameters
    ----------
    p_value : float or None
        P-value returned by the statistical test.

    alpha : float, default=0.05
        Significance level.

    Returns
    -------
    dict
        Interpretation of the statistical result.
    """

    validate_alpha(alpha)

    if p_value is None:

        return {

            "reject_null": None,

            "decision": "Unable to determine.",

            "reason":
                "P-value could not be computed.",

            "recommendation":
                "Review the dataset or statistical assumptions."
        }

    p_value = float(p_value)

    if p_value < alpha:

        return {

            "reject_null": True,

            "decision":
                "Reject the null hypothesis.",

            "reason":
                (
                    f"P-value ({round(p_value, 4)}) "
                    f"is less than alpha ({alpha})."
                ),

            "recommendation":
                "The result is statistically significant."
        }

    return {

        "reject_null": False,

        "decision":
            "Fail to reject the null hypothesis.",

        "reason":
            (
                f"P-value ({round(p_value, 4)}) "
                f"is greater than or equal to alpha ({alpha})."
            ),

        "recommendation":
            "The result is not statistically significant."
    }