#!/usr/bin/python3
"""Student Class module"""


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        """Initialaze an instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is not None:
            new_dict = {}
            for attr in attrs:
                try:
                    new_dict[attr] = self.__dict__[attr]
                except Exception as e:
                    pass
            return new_dict
        return self.__dict__
