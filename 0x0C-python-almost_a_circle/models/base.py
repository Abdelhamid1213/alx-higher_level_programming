#!/usr/bin/python3
"""Module defining a Base class for other classes"""
import json
import csv


class Base:
    """Base class serving as the foundation for other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor method for the Base class.

        Args:
            id (int): An optional identifier for the object. If not provided,
                      a unique identifier will be assigned.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries to convert.

        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instances to a file in JSON format.

        Args:
            list_objs (list): List of instances to save.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON string representation of a list of
            dictionaries.

        Returns:
            list: List of dictionaries represented by the JSON string.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes already set.

        Args:
            **dictionary: Double pointer to a dictionary.

        Returns:
            Base: Instance with attributes set according to the provided
            dictionary.
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of instances to a CSV file.

        Args:
            list_objs (list): List of instances to save.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_csv())

    @classmethod
    def load_from_file_csv(cls):
        """
        Load a list of instances from a CSV file.

        Returns:
            list: List of instances loaded from the file.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                instances = [cls.create_from_csv(row) for row in reader]
                return instances
        except FileNotFoundError:
            return []

    def to_csv(self):
        """
        Convert instance attributes to a CSV row.

        Returns:
            list: List containing attributes to be written to a CSV file.
        """
        return [str(getattr(self, attr)) for attr in self.__dict__.keys()]

    @classmethod
    def create_from_csv(cls, csv_row):
        """
        Create an instance from a CSV row.

        Args:
            csv_row (list): List containing attributes to create an instance.

        Returns:
            Base: Instance with attributes set according to the provided
            CSV row.
        """
        return cls(*map(int, csv_row))
