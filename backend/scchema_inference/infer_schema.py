import json

from .type_detector import detect_type
from .datetime_detector import detect_datetime
from .identifier_detector import detect_identifier
from .schema_prompt import get_schema_prompt

from llm.gemini import llm


def infer_schema(df):
    """
    Performs schema inference using both rule-based detection
    and LLM-based semantic understanding.
    """

    schema_context = []

    # -------------------------------------
    # Step 1 : Rule-Based Schema Detection
    # -------------------------------------
    for column in df.columns:

        series = df[column]

        type_info = detect_type(series)
        datetime_info = detect_datetime(series)
        identifier_info = detect_identifier(
            series,
            datetime_info["is_datetime"]
        )

        schema_context.append({
            "column_name": column,
            **type_info,
            **datetime_info,
            **identifier_info
        })

    # -------------------------------------
    # Step 2 : Build Prompt
    # -------------------------------------
    prompt = get_schema_prompt(schema_context)

    # -------------------------------------
    # Step 3 : Call Gemini
    # -------------------------------------
    response = llm.invoke(prompt)

    print("\n========== LLM RESPONSE ==========\n")
    print(response.content)
    print("\n==================================\n")

    # -------------------------------------
    # Step 4 : Convert JSON String -> Python
    # -------------------------------------
    if isinstance(response.content, str):

        response_text = response.content

    elif isinstance(response.content, list):

        response_text = ""

    for block in response.content:

        if isinstance(block, dict) and block.get("type") == "text":

            response_text += block.get("text", "")
  
        else:

          raise ValueError(
            f"Unexpected response type: {type(response.content)}"
          )

    response_text = response_text.strip()

    if response_text.startswith("```json"):
        response_text = response_text.replace("```json", "", 1)

    if response_text.endswith("```"):
        response_text = response_text[:-3]

    response_text = response_text.strip()

    semantic_schema = json.loads(response_text)

    # -------------------------------------
    # Step 5 : Merge Rule-Based + LLM Output
    # -------------------------------------
    final_schema = []

    for basic, semantic in zip(schema_context, semantic_schema):

        final_schema.append({
            **basic,
            **semantic
        })

       

    return final_schema