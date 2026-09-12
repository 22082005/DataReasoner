"""import pandas as pd
from pathlib import Path
import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from scchema_inference.infer_schema import infer_schema


# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

file_path = (
    Path(__file__).resolve().parent.parent
    / "upload"
    / "Iris (3).csv"
)

df = pd.read_csv(file_path)

# --------------------------------------------------
# Run Schema Inference
# --------------------------------------------------

schema = infer_schema(df)

# --------------------------------------------------
# Basic Tests
# --------------------------------------------------

print("=" * 70)
print("SCHEMA TEST")
print("=" * 70)

assert isinstance(schema, list), \
    "Schema should return a list."

assert len(schema) == len(df.columns), \
    "Schema length does not match dataset columns."

print("✓ Schema returned successfully.")

# --------------------------------------------------
# Validate Each Column
# --------------------------------------------------

REQUIRED_KEYS = {

    "column_name",

    "type",

    "semantic_role",

    "use_for_analysis"

}

for column in schema:

    missing = REQUIRED_KEYS - set(column.keys())

    assert not missing, \
        f"{column['column_name']} missing keys: {missing}"

print("✓ Required keys present.")

# --------------------------------------------------
# Validate Target
# --------------------------------------------------

targets = [

    column

    for column in schema

    if column["semantic_role"] == "Target"

]
print("\nDetected Targets:")

targets = [
    column
    for column in schema
    if column["semantic_role"] == "Target"
]

print(targets)
print(f"Target Count: {len(targets)}")

assert len(targets) == 1, \
    "Exactly one target should exist."

print(f"✓ Target detected : {targets[0]['column_name']}")

# --------------------------------------------------
# Validate Identifier
# --------------------------------------------------

identifiers = [

    column

    for column in schema

    if column["semantic_role"] == "Identifier"

]

print(f"✓ Identifier columns : {len(identifiers)}")

# --------------------------------------------------
# Print Schema
# --------------------------------------------------

print()

for column in schema:

    print(column)

print()

print("=" * 70)
print("SCHEMA TEST PASSED")
print("=" * 70)"""