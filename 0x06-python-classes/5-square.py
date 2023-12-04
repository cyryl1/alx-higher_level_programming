#!/usr/bin/python3

"""Square class definition."""
class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Square Class initialization.

        Args:
            size (int): Size of Square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square to stdout using #."""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")

        if self.__size == 0:
            print("")
