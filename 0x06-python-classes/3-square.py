#!/usr/bin/python3
"""Square Class Module"""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Initialize a square with default attributes."""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        
    def area(self):
        """Returns the current square area."""
        return self.size * self.size
