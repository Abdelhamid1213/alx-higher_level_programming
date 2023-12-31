#!/usr/bin/python3
"""Square Class Module"""


class Square:
    """A class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with default attributes."""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

        if not isinstance(position, tuple) or len(position) != 2 or \
                not isinstance(position[0], int) or not \
                isinstance(position[1], int) or \
                position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

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

    @property
    def position(self):
        """Returns the position of square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of square."""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not isinstance(value[0], int) \
                or not isinstance(value[1], int) or \
                value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """Print a square."""
        if self.__size == 0:
            print('')
        else:
            for _ in range(self.__position[1]):
                print('')
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
