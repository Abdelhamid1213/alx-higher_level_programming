#!/usr/bin/python3
"""Contain BaseGeometry Class"""


class BaseGeometry:
    """BaseGeometry Class"""
    def area(self):
        """Area method"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        self.name = name
        if type(value) is not int:
            raise TypeError(f'{self.name} must be an integer')
        if value <= 0:
            raise ValueError(f'{self.name} must be greater than 0')
