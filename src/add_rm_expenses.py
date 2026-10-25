"""Functionality for adding and removing expenses from basic tower sheets."""

import pandas as pd
import os
from pathlib import Path

def load_sheet(sheet_path):
    """Load a basic tower sheet from file."""
    if not isinstance(sheet_path, str):
        raise TypeError(f"Path not a string: {sheet_path}")
    elif not os.path.exists(sheet_path):
        raise ValueError(f"Path nonexistent: {sheet_path}")
    elif not sheet_path.endswith(".ods"):
        raise ValueError(f"Path must end with .ods (for now).")

    sheet = pd.read_excel(sheet_path, engine = "odf")

    if not sheet.columns.tolist() == ["date", "value", "currency", "tag"]:
        raise ValueError("Expected columns: ['date', 'value', 'currency', 'tag']",
                         f" \ngot: {sheet.columns}")
    print(
        "-"*50 +
        f" \nLoaded sheet at {sheet_path},",
        f" \nwith {sheet.shape[0]} rows. \n",
        "-"*50
    )
    return sheet

def add_row(sheet, row):
    """Add a row to the tower sheet."""
    if not isinstance(row, dict):
        raise TypeError(f"Row not a dictionary: {row}")
    elif not sheet.columns.tolist() == ["date", "value", "currency", "tag"]:
        raise ValueError("Expected columns: ['date', 'value', 'currency', 'tag'] in sheet")
    elif set(row.keys()) != {"date", "value", "currency", "tag"}:
        raise ValueError("Expected keys: ['date', 'value', 'currency', 'tag'] in row")

    sheet.loc[len(sheet)] = row

    print(
        "-"*50,
        " \nAdded a row to a tower sheet. \n",
        "-"*50

    )


