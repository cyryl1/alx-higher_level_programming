#!/usr/bin/python3
"""Add all arguments to a python list and save them to a file."""
import sys
import json


def add_item():
    """Function to add."""
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    args = sys.argv
    filename = "add_item.json"

    try:
        List = load_from_json_file(filename)
    except FileNotFoundError:
        List = []
    List.extend(sys.argv[1:])
    save_to_json_file(List, filename)
