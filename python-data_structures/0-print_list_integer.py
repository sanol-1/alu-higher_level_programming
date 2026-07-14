#!/usr/bin/python3
"""Module that prints a list of integers"""


def print_list_integer(my_list=[]):
    """Prints all integers of a list, one per line

    Args:
        my_list: the list of integers to print
    """
    for i in my_list:
        print("{:d}".format(i))
