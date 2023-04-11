#!/usr/bin/python3
""" Returns only the sub class of a class """


def inherits_from(obj, a_class):
    """
    Returns true if the object is an instance of a class
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
