#!/usr/bin/python3

"""Square class definition."""
class Square:
    """Represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Square Class initialization.

        Args:
            size (int): Size of Square.
            position (tuple): position to fill
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Return area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square to stdout using #."""
        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print("")

        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print("")

    def __str__(self):
        """Define the print() represetation of a sSquare."""
        if self.__size != 0:
            for i in range(self.__position[1]):
                print("")
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")

            if i != self.__size - 1:
                print("")
        return ("")
