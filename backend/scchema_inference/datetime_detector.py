import pandas as pd
from pandas.api.types import is_datetime64_any_dtype

DATE_KEYWORDS = {
    "date",
    "time",
    "timestamp",
    "dob",
    "birth",
    "joined",
    "joining",
    "created",
    "updated",
    "start",
    "end"
}


def detect_datetime(series):
    """
    Detect whether a column represents datetime information.
    """

    # Rule 1: Already datetime dtype
    if is_datetime64_any_dtype(series):
        return {
            "is_datetime": True
        }

    # Rule 2: Column name contains datetime keywords
    column_name = series.name.lower()

    if any(keyword in column_name for keyword in DATE_KEYWORDS):
        return {
            "is_datetime": True
        }

    # Rule 3: Check only string/object columns
    if series.dtype == "object":

        sample = series.dropna().head(10)

        try:
            pd.to_datetime(sample, errors="raise")

            return {
                "is_datetime": True
            }

        except Exception:
            pass

    return {
        "is_datetime": False
    }