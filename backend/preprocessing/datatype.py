import pandas as pd


def apply_datatype_conversion(df: pd.DataFrame, schema):
    """
    Apply datatype conversions based on the schema inference output.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.

    schema : list
        Output from schema inference.

    Returns
    -------
    pd.DataFrame
        DataFrame with converted datatypes.
    """

    df = df.copy()

    for column in schema:

        column_name = column["column_name"]
        datatype = column["recommendation_datatype"]

        # ----------------------------------
        # Integer
        # ----------------------------------
        if datatype == "Integer":

            df[column_name] = pd.to_numeric(
                df[column_name],
                errors="coerce"
            ).astype("Int64")

        # ----------------------------------
        # Float
        # ----------------------------------
        elif datatype == "Float":

            df[column_name] = pd.to_numeric(
                df[column_name],
                errors="coerce"
            )

        # ----------------------------------
        # Datetime
        # ----------------------------------
        elif datatype == "Datetime":

            df[column_name] = pd.to_datetime(
                df[column_name],
                errors="coerce"
            )

        # ----------------------------------
        # Boolean
        # ----------------------------------
        elif datatype == "Boolean":

            df[column_name] = df[column_name].astype("boolean")

        # ----------------------------------
        # Categorical
        # ----------------------------------
        elif datatype == "Categorical":

            df[column_name] = df[column_name].astype("category")

        # ----------------------------------
        # String
        # ----------------------------------
        elif datatype == "String":

            df[column_name] = df[column_name].astype("string")

        # ----------------------------------
        # Leave As Is
        # ----------------------------------
        else:

            continue

    return df