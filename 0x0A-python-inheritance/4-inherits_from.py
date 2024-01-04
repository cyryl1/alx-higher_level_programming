#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited from the specific class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    else:
        return (False)
