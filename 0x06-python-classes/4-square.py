#!/usr/bin/python3
"""Square that defines a square"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square."""
        self.size = size

    @property
    def size(self):
        """set the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """put the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """return the size of the square twice"""
        return self.__size ** 2
