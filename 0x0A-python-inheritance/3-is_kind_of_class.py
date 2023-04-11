#!/usr/bin/python3
""" function that returns same class or inherits from a class """


def is_kind_of_class(obj, a_class):
    """ Returns true if the object is an instance of a class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
