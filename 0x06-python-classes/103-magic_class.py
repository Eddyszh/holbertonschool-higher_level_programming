#!/usr/bin/python3
"""Magic Class"""
import math


class MagicClass():
    """Defines a circumference
    Public instance attribute: _MagicClass__radius.
    Instantiation with optional radius.
    Public instance method: def area(self).
    Public instance method: def circumference(self).
    """
    def __init__(self, radius=0):
        """Initializing"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """Returns: calculates the area"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Returns: Calculates the circumference"""
        return 2 * math.pi * self._MagicClass__radius
