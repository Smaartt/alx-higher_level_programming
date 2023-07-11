#!/usr/bin/python3
"""

returns JSON representation of obj (string)
"""


def to_json_string(f_obj):
    """Returns JSON representation of obj (string)
    Args:
        f_obj: python object
    Return:
        json string representation
    """
    import json

    return json.dumps(f_obj)
