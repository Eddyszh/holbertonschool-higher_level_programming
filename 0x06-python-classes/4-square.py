#!/usr/bin/python3
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

    @property
    def size(self):
        """
        Returns:
            the value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the new value for size
        Args:
            value: new value for size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns:
            the area of the square
        """
        return self.__size ** 2
