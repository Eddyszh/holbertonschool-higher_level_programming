#!/usr/bin/python3
"""
    print_square
    Function:
        print_square: prints a square with the character #
"""


def print_square(size):
    """
    Args:
        size: size of the square
    Raise:
        TypeError, ValueError
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("{}".format("#" * size))
