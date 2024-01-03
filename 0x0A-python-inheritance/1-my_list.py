#!/usr/bin/python3
"""Definition of MyList that inherits from list."""


class MyList(list):
    """To implement sorted printing for the built-in class"""

    def print_sorted(self):
        """print a list in sorted ascending order."""
        print(sorted(self))
