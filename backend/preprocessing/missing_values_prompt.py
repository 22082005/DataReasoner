def build_missing_value_prompt(columns_info):
    prompt = f"""
    You are an expert data analyst.

    Based on the following column information, recommend the best missing value handling strategy.

    For each column return JSON with:

    - column_name
    - strategy
    - reason

    Possible strategies:
    - Mean
    - Median
    - Mode
    - Drop Rows
    - Drop Column
    - Leave Missing
    - Forward Fill
    - Backward Fill

    Column Information:

    {columns_info}

    Return ONLY valid JSON.
    """
    return prompt