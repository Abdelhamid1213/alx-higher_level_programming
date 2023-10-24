#!/usr/bin/python3
"""Square Class Module"""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Initialize a square with default attributes."""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    @property
    def size(self):
        """Returns the size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of square."""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
