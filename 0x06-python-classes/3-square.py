#!/usr/bin/python3
"""
Creates a square class
"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """
        Args:
            size: size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns:
            the area of the square
        """
        return self.__size ** 2
