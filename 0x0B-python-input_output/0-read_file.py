#!/usr/bin/python3
"""Module to define function for reading and printing a text file to stdout"""


def read_file(filename=""):
    """
    Reads text file (UTF-8 encoded) and prints its content to standard output.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
