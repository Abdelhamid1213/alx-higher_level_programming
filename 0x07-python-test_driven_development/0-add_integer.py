#!/usr/bin/python3
"""
The 0-add_integer module supplies one function, add_integer().  For example,
>>> add_integer(1, 2)
3
"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the result.
    """

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError('a must be an integer')
    if not isinstance(b, int):
        raise TypeError('b must be an integer')

    return a + b
