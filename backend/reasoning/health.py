from typing import List


def calculate_health(
    insights: List[dict]
):
    """
    Calculate dataset health score.

    Parameters
    ----------
    insights : list

    Returns
    -------
    dict
    """

    score = 100

    deductions = []

    for insight in insights:

        severity = insight["severity"]

        title = insight["title"]

        if severity == "Critical":

            score -= 20

            deductions.append({

                "reason": title,

                "points": 20

            })

        elif severity == "High":

            score -= 10

            deductions.append({

                "reason": title,

                "points": 10

            })

        elif severity == "Medium":

            score -= 5

            deductions.append({

                "reason": title,

                "points": 5

            })

        elif severity == "Low":

            score -= 2

            deductions.append({

                "reason": title,

                "points": 2

            })

    score = max(

        score,

        0

    )

    # ------------------------
    # Grade
    # ------------------------

    if score >= 95:

        grade = "A+"

    elif score >= 90:

        grade = "A"

    elif score >= 80:

        grade = "B"

    elif score >= 70:

        grade = "C"

    elif score >= 60:

        grade = "D"

    else:

        grade = "F"

    return {

        "health_score": score,

        "grade": grade,

        "deductions": deductions

    }