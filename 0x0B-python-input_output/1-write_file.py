#!/usr/bin/python3
""" 
    A function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    Define the function that write a string
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
