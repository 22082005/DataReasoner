import pandas as pd


def analyze_duplicates(df: pd.DataFrame):
    """
    Analyze duplicate rows in the dataset.

    Returns
    -------
    dict
        Duplicate statistics.
    """
    results=[]
    duplicate_mask = df.duplicated()

    duplicate_indices = df.index[duplicate_mask].tolist()

    duplicate_count = len(duplicate_indices)

    duplicate_percentage = round(
        (duplicate_count / len(df)) * 100,
        2
    )

    results.append( {
        "duplicate_count": duplicate_count,
        "duplicate_percentage": duplicate_percentage,
        "duplicate_indices": duplicate_indices
    })
    return {
        "summary": {
            "duplicate_rows": duplicate_count,
            "duplicate_percentage": duplicate_percentage,
            "has_duplicates": duplicate_count > 0
        },
        "results": results
    }


def remove_duplicates(df: pd.DataFrame):
    """
    Remove duplicate rows from the dataset.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    tuple
        (
            cleaned_dataframe,
            preprocessing_summary
        )
    """

    rows_before = len(df)

    cleaned_df = df.drop_duplicates().reset_index(drop=True)

    rows_after = len(cleaned_df)

    summary = {
        "rows_before": rows_before,
        "rows_after": rows_after,
        "removed_rows": rows_before - rows_after
    }

    return cleaned_df, summary