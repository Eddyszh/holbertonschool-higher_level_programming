#!/usr/bin/python3
"""Rectangle Module
    Contains a rectangle class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class that creates a rectangle
    """
    def __init__(self, width, height):
        """
        Class constructor
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Returns:
            Area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        String representation of rectangle
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
