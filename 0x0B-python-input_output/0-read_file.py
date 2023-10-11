#!/usr/bin/python3
"""
A function that reads a text file
"""


def read_file(filename=""):
    """
    Defining a function that reads a text file
    """

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
