def analyze_datetime(schema):
    """
    Return all datetime columns from the schema.
    """

    datetime_columns = []

    for column in schema:

        if column["is_datetime"]:

            datetime_columns.append(column["column_name"])

    return datetime_columns



import pandas as pd


def transform_datetime(df, schema):
    """
    Transform datetime columns into useful components.
    """

    df = df.copy()

    datetime_columns = analyze_datetime(schema)

    for column in datetime_columns:

        df[column] = pd.to_datetime(
            df[column],
            errors="coerce"
        )

        df[f"{column}_Year"] = df[column].dt.year
        df[f"{column}_Month"] = df[column].dt.month
        df[f"{column}_Day"] = df[column].dt.day
        df[f"{column}_DayOfWeek"] = df[column].dt.dayofweek
        df[f"{column}_Quarter"] = df[column].dt.quarter

        # Remove original datetime column
        df.drop(columns=[column], inplace=True)

    return df