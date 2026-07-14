#!/usr/bin/python3
"""Module that prints the last digit of a number"""


def print_last_digit(number):
    """Prints the last digit of a number

    Args:
        number: the number to print the last digit of

    Returns:
        The value of the last digit
    """
    last_digit = abs(number) % 10
    print("{:d}".format(last_digit), end="")
    return last_digit
