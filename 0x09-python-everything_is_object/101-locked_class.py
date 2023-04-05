#!/usr/bin/python3
""" Defining a class """


class LockedClass:
    """ This class prevents a user from creating dynamic attributes unless if it is first_name"""
    __slots__ = ['first_name']
