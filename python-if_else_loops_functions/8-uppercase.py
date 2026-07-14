#!/usr/bin/python3
"""Module that prints a string in uppercase"""


def uppercase(str):
    """Prints a string in uppercase followed by a new line

    Args:
        str: the string to print in uppercase
    """
    for c in "{}".format(str):
        if 97 <= ord(c) <= 122:
            print("{:c}".format(ord(c) - 32), end="")
        else:
            print("{:c}".format(ord(c)), end="")
    print("")
