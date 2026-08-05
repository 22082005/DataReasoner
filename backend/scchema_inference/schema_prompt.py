def get_schema_prompt(schema_context):

    return f"""
You are an expert data analyst.

You are given metadata about a dataset.

Your task is to infer the semantic meaning of every column.

For each column determine:

1. semantic_role
2. description
3. use_for_analysis (true/false)
4. recommendation_datatype
5. column_tokens

column_tokens should be a list of meaningful words extracted from the column name.

Examples:

CustomerID
→ ["customer", "id"]

Order_No
→ ["order", "number"]

DOB
→ ["date", "of", "birth"]

TxnAmtRs
→ ["transaction", "amount", "rupees"]

SepalWidthCm
→ ["sepal", "width", "cm"]

PetalLengthCm
→ ["petal", "length", "cm"]

Schema Context:

{schema_context}

Return ONLY valid JSON.

Each object should follow this format:

[
  {{
    "semantic_role": "...",
    "description": "...",
    "use_for_analysis": true,
    "recommendation_datatype": "...",
    "column_tokens": ["..."]
  }}
]
"""