#!/usr/bin/python3

"""
module for to_json_string.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Return the JSON representation
    """
    return json.dumps(my_obj)
