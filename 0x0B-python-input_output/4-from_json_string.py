#!/usr/bin/python3
"""Decode a JSON string to an object."""
import json


def from_json_string(my_str):
    """Decode a JSON string to an object."""
    return json.loads(my_str)
