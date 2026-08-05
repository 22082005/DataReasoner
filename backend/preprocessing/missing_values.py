import json
import pandas as pd

from llm.gemini import llm
from .missing_values_prompt import build_missing_value_prompt


def analyze_missing_values(df: pd.DataFrame):
    """
    Analyze missing values in the dataset.

    Returns
    -------
    dict
    """

    total_rows = len(df)

    results = []

    total_missing = 0

    columns_with_missing = 0

    for column in df.columns:

        missing_count = int(df[column].isna().sum())

        missing_percentage = round(

            (missing_count / total_rows) * 100,

            2

        )

        if missing_count > 0:

            columns_with_missing += 1

            total_missing += missing_count

        results.append({

            "column_name": column,

            "missing_count": missing_count,

            "missing_percentage": missing_percentage

        })

    return {

        "summary": {

            "total_missing": total_missing,

            "columns_with_missing": columns_with_missing,

            "has_missing": total_missing > 0

        },

        "results": results

    }


def recommend_missing_values(context):
    """
    Uses the LLM to recommend missing value handling strategies.
    """

    # -------------------------------------
    # Step 1 : Keep only columns having missing values
    # -------------------------------------
    filtered_context = [
        column
        for column in context
        if column["missing_count"] > 0
    ]

    # -------------------------------------
    # Step 2 : No missing values
    # -------------------------------------
    if not filtered_context:
        return []

    # -------------------------------------
    # Step 3 : Build Prompt
    # -------------------------------------
    prompt = build_missing_value_prompt(filtered_context)

    # -------------------------------------
    # Step 4 : Call Gemini
    # -------------------------------------
    response = llm.invoke(prompt)

    # -------------------------------------
    # Step 5 : Convert JSON -> Python
    # -------------------------------------
    response_text = response.content.strip()

    if response_text.startswith("```json"):
        response_text = response_text.replace("```json", "", 1)

    if response_text.endswith("```"):
        response_text = response_text[:-3]

    response_text = response_text.strip()

    recommendations = json.loads(response_text)

    return recommendations


import pandas as pd


def apply_missing_value_strategy(df: pd.DataFrame, recommendations):
    """
    Apply the missing value strategies recommended by the LLM.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.

    recommendations : list
        LLM recommendations.

    Returns
    -------
    pd.DataFrame
        DataFrame after applying missing value handling.
    """

    df = df.copy()

    for recommendation in recommendations:

        column = recommendation["column_name"]
        strategy = recommendation["strategy"]

        # -------------------------------
        # Mean
        # -------------------------------
        if strategy == "Mean":

            df[column] = df[column].fillna(
                df[column].mean()
            )

        # -------------------------------
        # Median
        # -------------------------------
        elif strategy == "Median":

            df[column] = df[column].fillna(
                df[column].median()
            )

        # -------------------------------
        # Mode
        # -------------------------------
        elif strategy == "Mode":

            df[column] = df[column].fillna(
                df[column].mode()[0]
            )

        # -------------------------------
        # Drop Rows
        # -------------------------------
        elif strategy == "Drop Rows":

            df = df.dropna(subset=[column])

        # -------------------------------
        # Drop Column
        # -------------------------------
        elif strategy == "Drop Column":

            df = df.drop(columns=[column])

        # -------------------------------
        # Forward Fill
        # -------------------------------
        elif strategy == "Forward Fill":

            df[column] = df[column].ffill()

        # -------------------------------
        # Backward Fill
        # -------------------------------
        elif strategy == "Backward Fill":

            df[column] = df[column].bfill()

        # -------------------------------
        # Leave Missing
        # -------------------------------
        elif strategy == "Leave Missing":

            continue

    return df