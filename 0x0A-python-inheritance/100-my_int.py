#!/usr/bin/python3
"""Myint module
    Contains a class that inherits from int
"""


class MyInt(int):
    """
     is a rebel. MyInt has == and != operators inverted
    """
    def __eq__(self, other):
        """
         Returns:
            The opposite of equal
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """
        Returns:
            The opposite to not equal
        """
        return not super().__ne__(other)
