#!/usr/bin/python
"""Defines a class Rectangle that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """To represent a rectangle using a base geometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """To calculate the area of a rectangle."""
        return (self.__width * self.__height)

    def __str__(self):
        """Return the printable representation of the rectangle."""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
