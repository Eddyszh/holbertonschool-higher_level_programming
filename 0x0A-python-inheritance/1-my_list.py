#!/usr/bin/python3
"""My list module
"""


class MyList(list):
    """
    inherits from list
    """
    def print_sorted(self):
        """Prints the list
        """
        print(sorted(self))
