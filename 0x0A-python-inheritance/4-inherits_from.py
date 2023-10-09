#!/usr/bin/python3
"""Module inherits_from 
Finds if the object is an instance of a class that inherited
(directly/indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """Checks whether obj is an instance of a class that is derived from a_class.
    """

    return isinstance(obj, a_class) and type(obj) != a_class
