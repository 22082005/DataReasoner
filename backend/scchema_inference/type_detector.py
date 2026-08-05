import pandas as pd

def detect_type(data):
    """Detect type metadata for a Series or DataFrame."""
    if isinstance(data, pd.Series):
        if pd.api.types.is_integer_dtype(data):
            return {"type": "integer"}
        if pd.api.types.is_float_dtype(data):
            return {"type": "float"}
        if pd.api.types.is_string_dtype(data):
            return {"type": "string"}
        if pd.api.types.is_bool_dtype(data):
            return {"type": "boolean"}
        if pd.api.types.is_datetime64_any_dtype(data):
            return {"type": "datetime"}
        return {"type": "unknown"}

    column_types = {}
    for column in data.columns:
        series = data[column]
        if pd.api.types.is_integer_dtype(series):
            column_types[column] = "integer"
        elif pd.api.types.is_float_dtype(series):
            column_types[column] = "float"
        elif pd.api.types.is_string_dtype(series):
            column_types[column] = "string"
        elif pd.api.types.is_bool_dtype(series):
            column_types[column] = "boolean"
        elif pd.api.types.is_datetime64_any_dtype(series):
            column_types[column] = "datetime"
        else:
            column_types[column] = "unknown"
    return column_types