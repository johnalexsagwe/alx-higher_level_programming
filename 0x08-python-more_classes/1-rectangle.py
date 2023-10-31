#!/usr/bin/python3
"""A class Rectangle that defines a rectangle."""


class Rectangle:
    """
    Represents a rectangle


    Attributes: width and height 

    """
    def __init__(self, width=0, height=0):
        """Initializes the rectangle


        Args:
            width (int): width of a rectangle
            height (int): height of a rectangle


        Returns:
            None
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """get rectangle width


        Returns:
            Rectangle Width
        """
        return(self.__width)

    @property
    def height(self):
        """get the height


        Returns:
            Rectangle height
        """
        return(self.__height)

    @width.setter
    def width(self, value):
        """width set


        Args:
            value (int):Represents Rectangle width


        Returns:
            None
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """height set


        Args:
            value (int): Represents Rectangle height


        Returns:
            None
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
