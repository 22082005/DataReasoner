
from typing import List


# ----------------------------------------------------------
# Missing Values
# ----------------------------------------------------------

def describe_missing(
    evidence: dict,
    decision: dict
):
    """
    Generate explanation for missing values.
    """

    percentage = evidence["metadata"]["missing_percentage"]

    feature = evidence["feature"]

    rule = decision["rule"]

    if rule == "No Missing Values":

        return {

            "title": "No Missing Values",

            "description": (
                "No missing values were detected "
                f"in '{feature}'."
            ),

            "recommendation": (
                "No action is required."
            )

        }

    elif rule == "Minor Missing Values":

        return {

            "title": "Minor Missing Values",

            "description": (
                f"{feature} contains "
                f"{percentage:.2f}% missing values."
            ),

            "recommendation": (
                "Consider imputing the missing values."
            )

        }

    elif rule == "High Missing Values":

        return {

            "title": "High Missing Values",

            "description": (
                f"{feature} contains "
                f"{percentage:.2f}% missing values."
            ),

            "recommendation": (
                "Review the feature before modelling."
            )

        }

    return {

        "title": "Critical Missing Values",

        "description": (
            f"{feature} contains "
            f"{percentage:.2f}% missing values."
        ),

        "recommendation": (
            "Consider removing the feature or "
            "using an advanced imputation strategy."
        )

    }


# ----------------------------------------------------------
# Correlation
# ----------------------------------------------------------

def describe_correlation(
    evidence: dict,
    decision: dict
):
    """
    Generate explanation for correlation.
    """

    correlation = evidence["metadata"]["correlation"]

    feature_1 = evidence["feature"]

    feature_2 = evidence["metadata"]["related_feature"]

    return {

        "title": decision["rule"],

        "description": (

            f"{feature_1} and "

            f"{feature_2} "

            "have a correlation of "

            f"{correlation:.3f}."

        ),

        "recommendation": (

            "Review both features if using "

            "models sensitive to multicollinearity."

        )

    }


# ----------------------------------------------------------
# Outliers
# ----------------------------------------------------------

def describe_outlier(
    evidence: dict,
    decision: dict
):
    """
    Generate explanation for outliers.
    """

    feature = evidence["feature"]

    count = evidence["metadata"]["outlier_count"]

    return {

        "title": decision["rule"],

        "description": (

            f"{feature} contains "

            f"{count} potential outliers."

        ),

        "recommendation": (

            "Inspect the observations before "

            "removing or transforming them."

        )

    }


# ----------------------------------------------------------
# Target Detection
# ----------------------------------------------------------

def describe_target(
    evidence: dict,
    decision: dict
):
    """
    Generate explanation for target detection.
    """

    return {

        "title": "Target Variable Detected",

        "description": (

            f"{evidence['feature']} "

            "has been identified as the target."

        ),

        "recommendation": (

            "Use this feature as the prediction target."

        )

    }


# ----------------------------------------------------------
# Dispatcher
# ----------------------------------------------------------

def generate_story(
    decisions: List[dict]
):
    """
    Convert reasoning decisions into
    human-readable insights.
    """

    stories = []

    for item in decisions:

        evidence = item["evidence"]

        decision = item["decision"]

        evidence_type = evidence["type"]

        if evidence_type == "missing":

            story = describe_missing(
                evidence,
                decision
            )

        elif evidence_type == "correlation":

            story = describe_correlation(
                evidence,
                decision
            )

        elif evidence_type == "outlier":

            story = describe_outlier(
                evidence,
                decision
            )

        elif evidence_type == "target":

            story = describe_target(
                evidence,
                decision
            )

        else:

            continue

        stories.append({

            "severity": decision["severity"],

            "module": evidence["module"],

            **story

        })

    return stories