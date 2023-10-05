#!/usr/bin/python3
""" Defining  a function that prints a square with the character '#'."""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    """size must be greater than zero"""

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
