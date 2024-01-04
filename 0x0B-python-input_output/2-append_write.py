#!/usr/bin/python3
"""Defines a function that appends a string to the end of textfile."""


def append_write(filename="", text=""):
    """Append a string to the end UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
