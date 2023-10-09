#!/usr/bin/python3
"""module 0-lookup
Finding a list of available attributes & methods of an object
"""


def lookup(obj):
    """Returns that list of attributes and methods

    Args:
        - obj: object to look into
    """

    return dir(obj)
