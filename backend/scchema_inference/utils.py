def get_basic_metadata(series):
    """
    General metadata about a column.
    """

    return {
        "column_name": series.name,
        "total_rows": len(series),
        "missing_values": int(series.isnull().sum()),
        "missing_percentage": round(
            (series.isnull().sum() / len(series)) * 100,
            2
        ),
        "sample_values": series.dropna().head(5).tolist()
    }