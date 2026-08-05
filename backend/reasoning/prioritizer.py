from typing import List


# ----------------------------------------------------------
# Priority Mapping
# ----------------------------------------------------------

PRIORITY = {

    "Critical": 1,

    "High": 2,

    "Medium": 3,

    "Low": 4,

    "Informational": 5

}


# ----------------------------------------------------------
# Sort Insights
# ----------------------------------------------------------

def sort_by_priority(
    insights: List[dict]
):
    """
    Sort insights by severity.

    Parameters
    ----------
    insights : list

    Returns
    -------
    list
    """

    return sorted(

        insights,

        key=lambda insight:

        PRIORITY.get(

            insight["severity"],

            99

        )

    )


# ----------------------------------------------------------
# Group Insights
# ----------------------------------------------------------

def group_by_category(
    insights: List[dict]
):
    """
    Group insights by module.

    Parameters
    ----------
    insights : list

    Returns
    -------
    dict
    """

    grouped = {}

    for insight in insights:

        module = insight["module"]

        grouped.setdefault(

            module,

            []

        ).append(insight)

    return grouped


# ----------------------------------------------------------
# Select Top Insights
# ----------------------------------------------------------

def select_top_insights(
    insights: List[dict],
    limit: int = 10
):
    """
    Select highest priority insights.

    Parameters
    ----------
    insights : list

    limit : int

    Returns
    -------
    list
    """

    insights = sort_by_priority(

        insights

    )

    return insights[:limit]


# ----------------------------------------------------------
# Build Dashboard
# ----------------------------------------------------------

def build_dashboard(
    insights: List[dict],
    limit: int = 10
):
    """
    Build dashboard structure.

    Parameters
    ----------
    insights : list

    Returns
    -------
    dict
    """

    top = select_top_insights(

        insights,

        limit

    )

    grouped = group_by_category(

        top

    )

    return {

        "total_insights": len(insights),

        "displayed_insights": len(top),

        "insights": top,

        "groups": grouped

    }