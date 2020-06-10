#!/usr/bin/python3
"""Base Module
    This module contains the base modules and attributes
    for other classes
"""


class Base():
    """
    Attributes:
        __nb_objects = 0
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Checks id
        Args:
            id = None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
