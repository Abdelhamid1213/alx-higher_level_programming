#!/usr/bin/python3
"""Contain class rectangle"""


class Rectangle():
    """Class Rectangle"""

    def __init__(self, width=0, height=0):
        """default value when init"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Get Area of Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Get perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """Return sting to be printed"""
        buffer = ''
        if self.__width == 0 or self.__height == 0:
            return buffer
        for _ in range(self.__height):
            for _ in range(self.width):
                buffer += '#'
            buffer += '\n'
        return buffer[:-1]