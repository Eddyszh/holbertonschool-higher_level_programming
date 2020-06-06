#!/usr/bin/python3
"""Square Module
    Contains a claas that creates a square
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Creates a square object
    """
    def __init__(self, size):
        """
        Class constructor
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
