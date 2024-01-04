#!/usr/bin/python3
"""Function to check if an object is sn instance of a class."""


def is_same_class(obj, a_class):
    """Confirms if obj is an instance of a_class."""
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
