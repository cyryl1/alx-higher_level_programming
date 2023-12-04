#!/usr/bin/python3

"""Square class definition."""
class Square:
    """Represent a class."""
    def __init__(self, size=0):
        """Class initialization.

        Arguments:
            size (int): Size of Square.
        """
        self.size = size

        """Get/set the size of the square."""
    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Return area"""
    def area(self):
        return (self.__size * self.__size)
