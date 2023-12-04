#!/usr/bin/python3
"""Define a MagicClass matching the bytecode given"""

import math
class MagicClass:
    """Class Representation"""

    def __inti__(self, radius=0):
        """initialze

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """

        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return area"""
        return (self.__radius ** 2 * math.pi)

    def circ(self):
        """Retuirn the circumference"""
        return (2 * math.pi * self.__radius)
