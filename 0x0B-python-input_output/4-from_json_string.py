#!/usr/bin/python3

import json


def from_json_string(my_str):
    """An object represented by a JSON string"""
    return json.loads(my_str)
