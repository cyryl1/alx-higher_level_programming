#!/usr/bin/python3
"""Definition of an inherited list class MyList."""


class MyList(list):
    """To implement sorted printing for the built-in list class"""

    def print_sorted(self):
        """print a list in sorted ascending order."""
        print(sorted(self))
