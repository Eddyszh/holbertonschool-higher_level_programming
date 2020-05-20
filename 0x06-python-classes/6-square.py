#!/usr/bin/python3
"""
Creates a square class
"""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size: size of square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Returns:
            the position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the new value for position
        Args:
            value: new position value
        """
        if self._istuple_(value):
            self.__position = value
        elif not self._istuple_(value):
            raise TypeError("position must be a tuple of 2 positive integers")

    def _istuple_(self, position):
        """
        Verifies if is a tuple
        """
        if type(position) is not tuple or len(position) != 2:
            return False
        elif type(position[0]) is not int or position[0] < 0:
            return False
        elif type(position[1]) is not int or position[1] < 0:
            return False
        else:
            return True

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
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
                print("{}{}".format(' ' * self.__position[0], '#' * self.__size))
