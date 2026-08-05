import pandas as pd
from pathlib import Path

from .csv_loader import load_csv
from .excel_loader import load_excel

Loader = {
    ".csv": load_csv,
    "excel": load_excel,
}

def load_data(path):
    extension = Path(path).suffix.lower()
    if extension not in Loader:
        raise ValueError(f"Unsupported file extension: {extension}")
    return Loader[extension](path)
