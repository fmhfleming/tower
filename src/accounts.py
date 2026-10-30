"""accounts class"""
from src.add_rm_expenses import load_sheet

class Accounts:
    """
    Accounts class.
    """
    def __init__(self, sheet_path):
        """
        Starts up from the sheet path. Define all attributes here.
        :param sheet_path: Path to sheet file. *.ods to be supported for now.
        """
        # --- load sheet in ---
        self.sheet = load_sheet(sheet_path)
        # --- define attributes from the sheet ---
        # totals
        totals_dict = {}
        for curr in self.sheet["currency"].unique():
            totals_dict[curr] = sum(self.sheet["value"])
        self.totals = totals_dict
