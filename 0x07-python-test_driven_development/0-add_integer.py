#!/usr/bin/python3
"""
    Function:
        add_integer : adds 2 integers
"""


def add_integer(a, b=98):
    """
    Args:
        a: integer
        b: integer
    Raise:
        TypeError
    Returns:
        the addition of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    add_integer(3, 5, 6)
