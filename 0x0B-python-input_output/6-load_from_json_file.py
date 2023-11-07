#!/usr/bin/python3
"""Reads a JSON file and creates a Python object."""
import json


def load_from_json_file(filename):
    """Reads a JSON file and creates a Python object."""
    with open(filename) as f:
        return json.load(f)
