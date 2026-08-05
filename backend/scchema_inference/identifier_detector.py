import re
import pandas as pd

IDENTIFIER_KEYWORDS = {
    "id",
    "identifier",
    "key",
    "code",
    "uuid",
    "roll",
    "reg",
    "registration"
}


def tokenize_column_name(column_name: str):
    """
    Split a column name into meaningful tokens.

    Examples
    --------
    CustomerID     -> ['customer', 'id']
    Order_No       -> ['order', 'no']
    SepalWidthCm   -> ['sepal', 'width', 'cm']
    PetalLengthCm  -> ['petal', 'length', 'cm']
    """

    column_name = column_name.replace("_", " ")
    column_name = column_name.replace("-", " ")

    tokens = re.findall(
        r"[A-Z]+(?=[A-Z][a-z]|[0-9]|$)|[A-Z]?[a-z]+|[0-9]+",
        column_name
    )

    return [token.lower() for token in tokens]


def detect_identifier(series, is_datetime=False):
    """
    Detect whether a column is likely an identifier.

    Parameters
    ----------
    series : pandas.Series

    is_datetime : bool

    Returns
    -------
    dict
    """

    # -----------------------------------------
    # Datetime columns cannot be identifiers
    # -----------------------------------------
    if is_datetime:

        return {
            "is_identifier": False
        }

    # -----------------------------------------
    # Tokenize column name
    # -----------------------------------------
    column_tokens = tokenize_column_name(
        str(series.name)
    )

    # -----------------------------------------
    # Rule 1 : Identifier keywords
    # -----------------------------------------
    has_identifier_keyword = any(
        token in IDENTIFIER_KEYWORDS
        for token in column_tokens
    )

    # -----------------------------------------
    # Rule 2 : Uniqueness
    # -----------------------------------------
    unique_count = series.nunique(dropna=True)

    total_count = len(series.dropna())

    is_unique = unique_count == total_count

    # -----------------------------------------
    # Rule 3 : Monotonicity
    # -----------------------------------------
    is_monotonic = False

    if pd.api.types.is_numeric_dtype(series):

        is_monotonic = (
            series
            .dropna()
            .is_monotonic_increasing
        )

    # -----------------------------------------
    # Final Decision
    # -----------------------------------------
    is_identifier = (
        has_identifier_keyword or
        (is_unique and is_monotonic)
    )

    return {

        "is_identifier": is_identifier

    }