#!/usr/bin/python3
"""Defines a Square class, inheriting from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the class square.
        Args:
            size: The width and height of the square.
            x: The x coordinate of the square.
            y: The y coordinate of the square.
            id: Represents the identity of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square."""
        return self.height

    @size.setter
    def size(self, value):
        """Sets the size, assigning the same value to width and height."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns formatted string representation of a square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height
        )

    def update(self, *args, **kwargs):
        """Assigns attributes to the square.
        Args:
            *args: Representing positional arguments.
            **kwargs: Representing attribute key-value pairs.
        """
        if args or len(args) != 0:
            g = 0
            for arg in args:
                if g == 0:
                    self.id = arg if arg is not None else self.id
                elif g == 1:
                    self.size = arg
                elif g == 2:
                    self.x = arg
                elif g == 3:
                    self.y = arg
                g += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value if value is not None else self.id
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of the square.
        Returns:
            dict: The dictionary representing the square.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
