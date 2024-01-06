#!/usr/bin/python3
"""Defines a class Rectangle."""
Base = __import__("base.py").Base


class Rectangle(Base):
    """Class Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__(id=None)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
#        if not isinstance(value, int):
#            raise TypeError("width must be an integer")
#        elif value < 0:
#            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Get/set the x of the Rectangle."""
        return (self.__x)

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Get/set the y of the Rectangle."""
        return (self.__y)

    @height.setter
    def height(self, value):
        self.__y = value
