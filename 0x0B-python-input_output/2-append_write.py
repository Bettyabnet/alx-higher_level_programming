#!/usr/bin/python03
"""
A  function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a text file
    Returns: number of characters written.
    """
    with open(filename, "a", encoding='utf=8') as a_file:
        return a_file.write(text)
