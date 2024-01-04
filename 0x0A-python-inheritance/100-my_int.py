#!/usr/bin/python3
"""Defines a class MyInt."""


class MyInt(int):
    """To inverts operators

    Args:
        value(int): if int return false
            and if not int otherwise.
    """

    def __eq__(self, value):
        """return false if == operator."""
        return (self.real != value)
    
    def __ne__(self, value):
        """returns true if != operator."""
        return (self.real == value)
