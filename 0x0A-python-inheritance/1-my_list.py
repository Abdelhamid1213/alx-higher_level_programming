#!/usr/bin/python3
"""class MyList"""


class MyList(list):
    """MyList a class that inherits from list"""

    def __init__(self):
        """Initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
