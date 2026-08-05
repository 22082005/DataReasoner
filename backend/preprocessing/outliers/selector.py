from statstics.normality.selector import select_normality_test

from statstics.outlier_detection.iqr import iqr_outliers
from statstics.outlier_detection.zscore import zscore_outliers
from statstics.outlier_detection.modified_zscore import modified_zscore_outliers
from statstics.outlier_detection.isolation_forest import isolation_forest_outliers


def select_outlier_method(
    series,
    descriptive_summary
):
    """
    Select the most appropriate outlier detection algorithm.

    Parameters
    ----------
    series : pandas.Series

    descriptive_summary : dict
        Output of descriptive_summary(series)

    Returns
    -------
    dict
    """

    series = series.dropna()

    n = len(series)

    skewness = descriptive_summary["skewness"]
    kurtosis = descriptive_summary["kurtosis"]
    iqr = descriptive_summary["iqr"]
    std = descriptive_summary["standard_deviation"]

    # ----------------------------------------
    # Rule 1 : Insufficient observations
    # ----------------------------------------
    if n < 3:

        return {
            "selected_method": None,
            "reason": "Insufficient observations.",
            "normality_test": None
        }

    # ----------------------------------------
    # Rule 2 : Large Dataset
    # ----------------------------------------
    if n >= 10000:

        return {
            "selected_method": isolation_forest_outliers,
            "reason": (
                "Large dataset. Isolation Forest is suitable "
                "for large datasets."
            ),
            "normality_test": None,
            "alternatives": [
                modified_zscore_outliers,
                iqr_outliers
            ]
        }

    # ----------------------------------------
    # Rule 3 : Highly Skewed Distribution
    # ----------------------------------------
    if abs(skewness) > 1:

        return {
            "selected_method": iqr_outliers,
            "reason": (
                f"Highly skewed distribution "
                f"(skewness={round(skewness,2)})."
            ),
            "normality_test": None,
            "alternatives": [
                modified_zscore_outliers
            ]
        }

    # ----------------------------------------
    # Rule 4 : Heavy Tailed Distribution
    # ----------------------------------------
    if abs(kurtosis) > 3:

        return {
            "selected_method": modified_zscore_outliers,
            "reason": (
                f"Heavy-tailed distribution "
                f"(kurtosis={round(kurtosis,2)})."
            ),
            "normality_test": None,
            "alternatives": [
                iqr_outliers
            ]
        }

    # ----------------------------------------
    # Rule 5 : Constant / Near Constant Feature
    # ----------------------------------------
    if std == 0 or iqr == 0:

        return {
            "selected_method": None,
            "reason": (
                "Feature has no variation. "
                "Outlier detection is unnecessary."
            ),
            "normality_test": None,
            "alternatives": []
        }

    # ----------------------------------------
    # Rule 6 : Normality Test
    # ----------------------------------------
    normality_decision = select_normality_test(series)

    if normality_decision is None:

        return {
            "selected_method": iqr_outliers,
            "reason": "Unable to determine normality.",
            "normality_test": None,
            "alternatives": [
                modified_zscore_outliers
            ]
        }

    normality_result = normality_decision["selected_test"](series)

    # ----------------------------------------
    # Rule 7 : Normal Distribution
    # ----------------------------------------
    if normality_result["is_normal"]:

        return {
            "selected_method": zscore_outliers,
            "reason": (
                "Data appears approximately normally distributed."
            ),
            "normality_test": normality_result["test"],
            "alternatives": [
                modified_zscore_outliers
            ]
        }

    # ----------------------------------------
    # Rule 8 : Non-Normal Distribution
    # ----------------------------------------
    return {

        "selected_method": iqr_outliers,

        "reason": (
            "Data is not normally distributed."
        ),

        "normality_test": normality_result["test"],

        "alternatives": [
            modified_zscore_outliers
        ]
    }