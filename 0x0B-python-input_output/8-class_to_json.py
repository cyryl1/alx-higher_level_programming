#!/usr/bin/python3
"""To return a dictionary description."""


def class_to_json(obj):
    """Function that returns the dictionary description
    for JSON serialization of an object.
    """

    return obj.__dict__
