#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """To represent a square using a rectangle."""

    def __init__(self, size):
        """Intialize a new Square.

        Args:
            size (int): The size of the new Square.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """To calculate the area of a rectangle."""
        return (self.__size * self.__size)

    def __str__(self):
        """Return the printable representation of the rectangle."""
        return ("[Square] {}/{}".format(self.__size, self.__size))
