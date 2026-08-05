from typing import List


def collect_evidence(

    schema,

    missing_values,

    duplicates,

    outliers,

    correlation,

    feature_selection

):
    """
    Collect evidence from analysis modules.

    Returns
    -------
    list
    """

    evidence = []

    # -------------------------------------
    # Schema
    # -------------------------------------

    for column in schema:

        if column["semantic_role"] == "Target":

            evidence.append({

                "module":"Schema",

                "type":"target",

                "feature":column["column_name"],

                "value":True,

                "metadata":{

                    "confidence":1.0

                }

            })

    # Remaining modules
    # (We'll add them gradually)

    return evidence