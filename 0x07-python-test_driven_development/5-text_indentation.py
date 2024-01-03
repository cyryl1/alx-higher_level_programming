#!/usr/bin/python3
"""Define function to indent"""


def text_indentation(text):
    """
    Print a modified version of the provided text.
    Inserts 2 new lines after each occurrence of
    '.', '?', and ':'.

    Args:
        text (str): The input text.

    Returns:
        None

    Raises:
        TypeError: If the provided text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")

    for char in ['.', '?', ':']:
        text = text.replace(char, f"{char}\n\n")
    print(text)
