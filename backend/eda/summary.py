import pandas as pd


def generate_summary(
    df: pd.DataFrame,
    schema: list,
    target:str
):
    """
    Generate a high-level dataset summary.

    Parameters
    ----------
    df : pandas.DataFrame

    schema : list

    Returns
    -------
    dict
    """

    total_rows = len(df)

    total_columns = len(df.columns)

    numeric_columns = 0

    categorical_columns = 0

    datetime_columns = 0

    identifier_columns = 0

    target_column = target

    for column in schema:

        if column["semantic_role"] == "Identifier":

            identifier_columns += 1

        

        dtype = column["type"].lower()

        if dtype in [

            "integer",

            "float",

            "double",

            "int"

        ]:

            numeric_columns += 1

        elif dtype in [

            "string",

            "object",

            "category",

            "categorical"

        ]:

            categorical_columns += 1

        elif column["is_datetime"]:

            datetime_columns += 1

    return {

        "rows": total_rows,

        "columns": total_columns,

        "numeric_columns": numeric_columns,

        "categorical_columns": categorical_columns,

        "datetime_columns": datetime_columns,

        "identifier_columns": identifier_columns,

        "target_column": target_column

    }