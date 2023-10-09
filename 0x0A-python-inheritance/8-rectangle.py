#!/usr/bin/python3
"""Module Rectangle
Creates a Rectangle class
"""


class BaseGeometry:
    def area(self):
        """Raise an exception indicating that the area()
        method is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            """Raise a TypeError if the value is not an integer"""
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            """Raise a ValueError if the value is less than or equal to 0"""
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
