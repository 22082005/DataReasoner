from .shapiro import shapiro_test
from .dagostino import dagostino_test
from .anderson import anderson_test
from .kolmogorov import kolmogorov_test


def select_normality_test(series):
    """
    Select the most appropriate normality test
    based on dataset characteristics.
    """

    n = len(series.dropna())

    # ----------------------------------------
    # Rule 1 : Insufficient observations
    # ----------------------------------------
    if n < 3:
        return None

    # ----------------------------------------
    # Rule 2 : Very Small Dataset
    # ----------------------------------------
    if 3 <= n < 8:

        return {
            "selected_test": shapiro_test,
            "reason": (
                "Shapiro-Wilk supports very small datasets. "
                "D'Agostino requires at least 8 observations."
            ),
            "alternatives": [
                anderson_test,
                kolmogorov_test
            ]
        }

    # ----------------------------------------
    # Rule 3 : Small / Medium Dataset
    # ----------------------------------------
    if 8 <= n <= 5000:

        return {
            "selected_test": shapiro_test,
            "reason": (
                "Shapiro-Wilk generally provides strong power "
                "for small and medium datasets."
            ),
            "alternatives": [
                dagostino_test,
                anderson_test,
                kolmogorov_test
            ]
        }

    # ----------------------------------------
    # Rule 4 : Large Dataset
    # ----------------------------------------
    return {
        "selected_test": dagostino_test,
        "reason": (
            "Large dataset. D'Agostino's K² is computationally "
            "more suitable than Shapiro-Wilk."
        ),
        "alternatives": [
            anderson_test,
            kolmogorov_test
        ]
    }