from typing import List

# ----------------------------------------------------------
# Severity Levels
# ----------------------------------------------------------

SEVERITY = {
    "INFO": "Informational",
    "LOW": "Low",
    "MEDIUM": "Medium",
    "HIGH": "High",
    "CRITICAL": "Critical"
}


# ----------------------------------------------------------
# Missing Value Rules
# ----------------------------------------------------------

def evaluate_missing(evidence: dict):
    """
    Evaluate missing value evidence.
    """

    percentage = evidence["metadata"]["missing_percentage"]

    if percentage >= 50:

        return {
            "severity": SEVERITY["CRITICAL"],
            "rule": "Extremely High Missing Values"
        }

    elif percentage >= 30:

        return {
            "severity": SEVERITY["HIGH"],
            "rule": "High Missing Values"
        }

    elif percentage > 0:

        return {
            "severity": SEVERITY["LOW"],
            "rule": "Minor Missing Values"
        }

    return {
        "severity": SEVERITY["INFO"],
        "rule": "No Missing Values"
    }


# ----------------------------------------------------------
# Outlier Rules
# ----------------------------------------------------------

def evaluate_outlier(evidence: dict):
    """
    Evaluate outlier evidence.
    """

    count = evidence["metadata"]["outlier_count"]

    if count == 0:

        return {
            "severity": SEVERITY["INFO"],
            "rule": "No Outliers"
        }

    elif count <= 5:

        return {
            "severity": SEVERITY["LOW"],
            "rule": "Few Outliers"
        }

    elif count <= 20:

        return {
            "severity": SEVERITY["MEDIUM"],
            "rule": "Moderate Outliers"
        }

    return {
        "severity": SEVERITY["HIGH"],
        "rule": "Many Outliers"
    }


# ----------------------------------------------------------
# Correlation Rules
# ----------------------------------------------------------

def evaluate_correlation(evidence: dict):
    """
    Evaluate correlation evidence.
    """

    correlation = abs(
        evidence["metadata"]["correlation"]
    )

    if correlation >= 0.90:

        return {
            "severity": SEVERITY["HIGH"],
            "rule": "Very Strong Correlation"
        }

    elif correlation >= 0.70:

        return {
            "severity": SEVERITY["MEDIUM"],
            "rule": "Strong Correlation"
        }

    elif correlation >= 0.50:

        return {
            "severity": SEVERITY["LOW"],
            "rule": "Moderate Correlation"
        }

    return {
        "severity": SEVERITY["INFO"],
        "rule": "Weak Correlation"
    }


# ----------------------------------------------------------
# Target Detection Rules
# ----------------------------------------------------------

def evaluate_target(evidence: dict):
    """
    Evaluate target detection.
    """

    return {
        "severity": SEVERITY["INFO"],
        "rule": "Target Variable Detected"
    }


# ----------------------------------------------------------
# Generic Rules
# ----------------------------------------------------------

def evaluate_generic(evidence: dict):
    """
    Fallback rule.
    """

    return {
        "severity": SEVERITY["INFO"],
        "rule": "General Information"
    }


# ----------------------------------------------------------
# Rule Dispatcher
# ----------------------------------------------------------

def apply_rules(
    evidence_list: List[dict]
):
    """
    Apply reasoning rules to all evidence.

    Parameters
    ----------
    evidence_list : list

    Returns
    -------
    list
    """

    decisions = []

    for evidence in evidence_list:

        evidence_type = evidence["type"]

        if evidence_type == "missing":

            decision = evaluate_missing(evidence)

        elif evidence_type == "outlier":

            decision = evaluate_outlier(evidence)

        elif evidence_type == "correlation":

            decision = evaluate_correlation(evidence)

        elif evidence_type == "target":

            decision = evaluate_target(evidence)

        else:

            decision = evaluate_generic(evidence)

        decisions.append({

            "evidence": evidence,

            "decision": decision

        })

    return decisions