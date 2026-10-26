"""Profile class for tower"""

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