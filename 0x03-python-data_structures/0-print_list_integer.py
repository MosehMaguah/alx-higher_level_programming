#!/usr/bin/python3
# prints  all integers in my_list

def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
