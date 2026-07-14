#!/usr/bin/python3
"""Module that replaces an element in a list"""


def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position

    Args:
        my_list: the list to modify
        idx: the index to replace
        element: the new element

    Returns:
        The list with the element replaced, or the original list
        if idx is negative or out of range
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
