#!/usr/bin/python3
"""Square Module
    This module contains the methods and attributes
    for a square object
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Creates a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Args:
            size, x, y, id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Returns:
            private value of size (width)
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets new value for size (width, height)
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        String representation of a square
        Returns:
            [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {:d}/{:d} - {:d}".format(self.id,
        self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Assigns values and attributes
        """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                if i == 1:
                    self.size = j
                if i == 2:
                    self.x = j
                if i == 3:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Returns:
            dictionay representation of a square
        """
        sqr_dict = {}
        sqr_dict["id"] = self.id
        sqr_dict["size"] = self.size
        sqr_dict["x"] = self.x
        sqr_dict["y"] = self.y
        return sqr_dict
