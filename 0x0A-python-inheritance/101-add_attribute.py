#!/usr/bin/python3
"""
Contains a module to add attribute to an object
"""


def add_attribute(obj, attr, value):
    """
    Adds an attribute
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
