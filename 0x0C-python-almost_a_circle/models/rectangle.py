#!/usr/bin/python3
"""Define a Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """Represent a rectangle object.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle.
        y (int): The y-coordinate of the rectangle.
        id (int): The identity of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            id (int): The identity of the rectangle.

        Raises:
            TypeError: If width, height, x, or y is not an int.
            ValueError: If width, height, x, or y is <= 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width value.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

        @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set and check the value of height.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set and check the value of x-coordinate.

        Args:
            value (int): The x-coordinate value to set.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is < 0.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set and check the value of y-coordinate.

        Args:
            value (int): The y-coordinate value to set.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is < 0.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__height * self.__width

    def display(self):
        """Display the rectangle with the '#' character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for row in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for h in range(self.width)]
            print("")

    def __str__(self):
        """Override string representation of the class.

        Returns:
            str: String representation of the class in the format:
                 [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
