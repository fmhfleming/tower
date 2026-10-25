"""functionality for creating blank sheet"""
import pandas as pd

def create_blank_sheet(sheet_name):
    """Creates a blank sheet that will be readable by tower."""
    if not isinstance(sheet_name, str) or sheet_name == "":
        raise TypeError("sheet_name must be a string")

    sheet = pd.DataFrame(
        columns=["data", "value", "currency", "tag"]
    )
    with pd.ExcelWriter(
        f"sheets/{sheet_name}.ods",
        engine="odf"
    ) as writer:
        sheet.to_excel(writer, sheet_name=sheet_name)

def check_sheet_exists(sheet_name):
    """Checks if a sheet exists with the same name."""
    pass