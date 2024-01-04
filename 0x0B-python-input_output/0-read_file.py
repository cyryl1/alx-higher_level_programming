#!/usr/bin/python3
"""Defines a function that reads a text file and prints it out to stdout."""


def read_file(filename=""):
    """function to read file."""

    with open(filename, encoding="utf-8") as f:
        read = f.read()
    print(read, end="")
