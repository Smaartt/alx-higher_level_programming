#!/usr/bin/python3
"""

writes Python obj to file using JSON represenation
"""


def save_to_json_file(my_obj, filename):
    """Writes Python obj to file using JSON represenation
    Args:
        my_obj: python object
        filename: file
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as g:
        json.dump(my_obj, g)
