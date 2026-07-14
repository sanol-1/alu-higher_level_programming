#!/usr/bin/python3
"""Module that checks which elements of a list are divisible by 2"""


def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list

    Args:
        my_list: the list of integers to check

    Returns:
        A new list of the same size, with True/False depending on
        whether the integer at the same position is a multiple of 2
    """
    result = []
    for n in my_list:
        result.append(n % 2 == 0)
    return result
