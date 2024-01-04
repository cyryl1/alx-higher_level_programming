#!/usr/bin/python3
"""Defines class BaseGeometry."""


class BaseGeometry:
    """To calculate the base geometry of a circle."""
    def area(self):
        """Function to raise an Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """To validate the parameter value."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
