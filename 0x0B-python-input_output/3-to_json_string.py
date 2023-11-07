#!/usr/bin/python3
"""Append text to a text file."""


def append_write(filename="", text=""):
    """Append text to a text file."""
    with open(filename, 'a') as f:
        return f.write(text)
