#!/usr/bin/python3
class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """
        Args:
            size: size of square
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
            the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the new value for size
        Args:
            value: new size value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns:
            tha area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
