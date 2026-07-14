#!/usr/bin/python3
"""Module that finds the max integer of a list"""


def max_integer(my_list=[]):
    """Finds the biggest integer of a list

    Args:
        my_list: the list of integers to search

    Returns:
        The biggest integer, or None if the list is empty
    """
    if len(my_list) == 0:
        return None
    max_value = my_list[0]
    for n in my_list:
        if n > max_value:
            max_value = n
    return max_value
