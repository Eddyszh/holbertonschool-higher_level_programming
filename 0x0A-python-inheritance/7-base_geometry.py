#!/usr/bin/python3
"""Base geometry module
    Contains a class with a raise exception
"""


class BaseGeometry:
    """
    Class with 2 public method
    """
    def area(self):
        """
        Raises:
            Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value
        Raises:
            TypeError, ValueError
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
