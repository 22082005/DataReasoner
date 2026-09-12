from visualization.utils import create_chart_response


def heatmap(correlation_results):
    """
    Prepare heatmap visualization data.

    Parameters
    ----------
    correlation_results : list
        Correlation result records.

    Returns
    -------
    dict
    """

    matrix = {}

    labels = set()

    for result in correlation_results:

        x = result["feature"]

        statistics = result["statistics"]

        y = statistics["related_feature"]

        value = statistics["correlation"]

        labels.add(x)
        labels.add(y)

        matrix.setdefault(x, {})[y] = value

        matrix.setdefault(y, {})[x] = value

    labels = sorted(labels)

    # ---------------------------------------------
    # Diagonal = perfect self-correlation
    # ---------------------------------------------

    for label in labels:

        matrix.setdefault(label, {})[label] = 1.0

    return create_chart_response(

        chart_type="heatmap",

        title="Correlation Heatmap",

        x_axis="Features",

        y_axis="Features",

        priority=1,

        reason=(
            "Multiple numeric features."
        ),

        recommendation=(
            "Useful for identifying relationships "
            "between all numeric features."
        ),

        data={

            "labels": labels,

            "matrix": matrix

        }

    )