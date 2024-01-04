#!/usr/bin/python3
"""Defines Function that writes an object to a text file."""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding="utf-8") as f:
        write = f.write(json.dumps(my_obj))
    return (write)
