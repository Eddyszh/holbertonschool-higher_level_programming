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
