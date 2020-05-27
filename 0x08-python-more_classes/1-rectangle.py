#!/usr/bin/python3
"""Rectangle module
"""


class Rectangle:
    """Defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """Args:
            width: width of a rectangle (int)
            height: height of a rectangle (int)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns:
            The width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets new value for width
        Raises:
            TypeError, ValueError
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns:
            The height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets new value for height
        Raises:
            TypeError, ValueError
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
