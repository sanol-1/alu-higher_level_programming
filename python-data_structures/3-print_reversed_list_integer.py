#!/usr/bin/python3
"""Module that prints a list of integers in reverse"""


def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list, in reverse order, one per line

    Args:
        my_list: the list of integers to print
    """
    for i in reversed(my_list):
        print("{:d}".format(i))
