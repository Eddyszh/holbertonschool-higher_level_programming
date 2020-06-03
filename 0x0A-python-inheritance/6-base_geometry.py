#!/usr/bin/python3
"""Base geometry module
    Contains a class with a raise exception
"""


class BaseGeometry:
    """
    Class with public method
    """
    def area(self):
        """
        Raises:
            Exception
        """
        raise Exception("area() is not implemented")
