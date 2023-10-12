#!/usr/bin/python3

"""
module for to_json_string.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    define a function by using JSON
    """

    with open(filename, mode="w") as J:
        json.dump(my_obj, J)
