#!/usr/bin/python3
"""Class Square definition."""

class Square:
    """Class Square representation."""

    def __init__(self, size=0):
        """Class intialization.

        Args:
            size (int): size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
