#!/usr/bin/python3
"""
contains a function to check if an object is an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if the given object is an instance of the specified class.

    Parameters:
    - obj: The object to be checked.
    - a_class: The class to check against.

    Returns:
    - True if obj is an instance of a_class, otherwise False.
    """
    return type(obj) == a_class
