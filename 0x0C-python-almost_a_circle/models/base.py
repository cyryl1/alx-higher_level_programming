#!/usr/bin/python3
"""Defines a class Base."""


class Base:
    """Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base class.
        Args:
            id(int): instance variable.
        """
        if (id is not None):
            self.id = int(id)
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
