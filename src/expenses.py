"""expenses class"""

class Expenses:
    """
    Expenses class for tower repo. Acts as a wrapper/editor that clamps onto an expenses sheet as a source of truth.
    On init, checks path and tries to load it, error out if not. Only gets initialised
    on intentionally existing sheets, process for new account should make blank sheets and then boot up the classes.
    """