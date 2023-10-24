#!/usr/bin/python3

class Square:
    """
    Define a square.
    """

    def __init__(self, size=0):
        """
        Initialize an instance of the Square class.

        Args:
            size (int, optional): The size of the square (default is 0).
        """
        self.size = size

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Get the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is a negative number.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Prints a square of side length `size`.
        If size is 0, print an empty line.
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
