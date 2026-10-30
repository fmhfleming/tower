"""functionality for creating blank sheet"""
import pandas as pd

def create_blank_expenses_sheet(sheet_name, type="expenses"):
    """Creates a blank accounts sheet that will be readable by tower."""
    if not isinstance(sheet_name, str) or sheet_name == "":
        raise TypeError("sheet_name must be a string")

    if type == "expenses":
        sheet = pd.DataFrame(
            columns = ["date", "value", "currency", "tag", "description"]
        )
    elif type == "accounts":
        sheet = pd.DataFrame(
            columns = ["name", "currency", "value", "description"]
        )
    else:
        raise ValueError("type must be either 'expenses' or 'accounts'")

    with pd.ExcelWriter(
        f"sheets/{sheet_name}.ods",
        engine="odf"
    ) as writer:
        sheet.to_excel(writer, sheet_name=sheet_name, index=False)

    print(
        "-"*50 +
        f" \nCreated blank sheet {sheet_name}.ods",
        "in sheets/ directory and gitignored by default. \n",
        "-"*50
    )

def check_sheet_exists(sheet_name):
    """Checks if a sheet exists with the same name."""
    pass