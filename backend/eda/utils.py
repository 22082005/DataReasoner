from typing import List


def create_insight(
    category: str,
    title: str,
    description: str,
    priority: int,
    recommendation: str,
    source: str
) -> dict:
    """
    Create a standardized EDA insight.

    Parameters
    ----------
    category : str
        Insight category.

    title : str
        Short title.

    description : str
        Explanation of the insight.

    priority : int
        Priority level (1 = Highest).

    recommendation : str
        Suggested action.

    source : str
        Module that generated the insight.

    Returns
    -------
    dict
    """

    return {

        "category": category,

        "title": title,

        "description": description,

        "priority": priority,

        "recommendation": recommendation,

        "source": source

    }


def sort_insights(
    insights: List[dict]
) -> List[dict]:
    """
    Sort insights by priority.

    Parameters
    ----------
    insights : list

    Returns
    -------
    list
    """

    return sorted(

        insights,

        key=lambda x: x["priority"]

    )


def merge_insights(
    *insight_groups
) -> List[dict]:
    """
    Merge multiple insight lists.

    Parameters
    ----------
    *insight_groups

    Returns
    -------
    list
    """

    merged = []

    for group in insight_groups:

        merged.extend(group)

    return merged