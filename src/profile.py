"""Profile class for tower"""
from src.expenses import Expenses
from src.accounts import Accounts

class Profile:
    """
    Profile class for tower. Represents a user's full HUD. Wakes up and sleeps as solely one instance of Expenses and
    one instance of Accounts. Note that these in turn wake up and sleep from individual .ods (and in future, equivalent
    .xlsx etc) files so it's essentially a describer/editor that clamps onto those two files.

    Some kind of password protection would be good to have here on boot up, as well as ability to change passwords and
    usernames. Maybe would be fun to write a password recovery thing that spits out an email to your recovery email if
    you forget it.

    Initialises by init of the two class instances. Class methods for these two get called through profile. Also
    suppose that  the View will be init through here too. So I guess in this way, Profile is our Controller class. Or
    at least the intended main one.
    """

    def __init__(self, expenses_path, accounts_path):
        """
        Initialises class instances. Every attribute should be set within __init__.
        :param expenses_path: filepath to expenses sheet.
        :param accounts_path: filepath to accounts sheet.
        """
        # --- core child classes ---
        self.expenses = Expenses(sheet_path=expenses_path)
        self.accounts = Accounts(sheet_path=accounts_path)
        # --- add these onto the class too --
        self.expenses_path = expenses_path
        self.accounts_path = accounts_path

    def save_out(self):
        """
        To be performed when something like a 'confirm' or 'accept changes' button is pressed. Saves out to both
        sheets and then refreshes the child classes from them.
        :return: Nothing aside from a confirmation that these operations have been performed.
        """
        pass

    def increment_backup(self):
        """
        Looks for a backup file and overwrites it with a snapshot of the user's two files. If none found, creates a new
        one.
        """

    def build_view(self):
        """
        Calculates what it needs for the view. Windows will be a main landing window, manage expenses, manage accounts,
        dashboard, goals, backup.
        :return:
        """
        pass

