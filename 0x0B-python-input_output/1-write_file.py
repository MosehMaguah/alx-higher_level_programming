#!/usr/bin/python3
"""this Defines a file-writing function."""


def write_file(filename="", text=""):
    """Writes a string to a UTF"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
