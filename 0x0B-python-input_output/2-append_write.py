#!/usr/bin/python3
"""It Appends a string of a text file"""


def append_write(filename="", text=""):
    """It Appends a string of a text file"""
    with open(filename, 'a') as f:
        return f.write(text)
