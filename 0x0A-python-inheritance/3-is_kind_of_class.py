#!/usr/bin/python
"""Function to check if an object is sn instance of a class."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
