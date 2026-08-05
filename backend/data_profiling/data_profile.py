def get_dataset_profile(df):
    """
    Returns basic information about the dataset.
    """

    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "shape": df.shape,
        "column_names": df.columns.tolist(),
        "column_types": {
            column: str(dtype)
            for column, dtype in df.dtypes.items()
        },
      
    }