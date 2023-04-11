#!/usr/bin/python3
""" Creates a Mylist class """


class MyList(list):
    """
    MyList class inherits from list
    """
    def print_sorted(self):
        """ Prints the list in sorted order """
        print(sorted(self))
