from eda.utils import sort_insights


def select_insights(
    insights: list,
    max_insights: int = 10
):
    """
    Select the most important EDA insights.

    Parameters
    ----------
    insights : list

    max_insights : int, default=10

    Returns
    -------
    list
    """

    if not insights:

        return []

    insights = sort_insights(insights)

    selected = []

    seen_titles = set()

    for insight in insights:

        title = insight["title"]

        if title in seen_titles:

            continue

        seen_titles.add(title)

        selected.append(insight)

        if len(selected) >= max_insights:

            break

    return selected