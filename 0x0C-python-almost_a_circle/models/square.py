#!/usr/bin/python3
"""Square Module - Defines the Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class - Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor method for the Square class.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square (default is 0).
            y (int): The y-coordinate of the square (default is 0).
            id (int): The unique identifier of the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the size attribute.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """Update the attributes of the square based on arguments and keyword
        arguments."""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
