#!/usr/bin/python3
""" creates a function that adds new attributes to an object """


def add_attribute(obj, name, value):
    """ An add attributes function """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
