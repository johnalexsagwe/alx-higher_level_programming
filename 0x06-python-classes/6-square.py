#!/usr/bin/python3

class Square:
    """
    Define a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize an instance of the Square class.

        Args:
            size (int, optional): The size of the square (default is 0).
            position: The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Get the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If the position is not a tuple of two positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Prints a square with the specified size and position.
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()

            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
