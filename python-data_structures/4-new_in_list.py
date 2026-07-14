#!/usr/bin/python3
"""Module that replaces an element in a copy of a list"""


def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position,
    without modifying the original list

    Args:
        my_list: the original list
        idx: the index to replace
        element: the new element

    Returns:
        A new list with the element replaced, or a copy of the
        original list if idx is negative or out of range
    """
    new_list = my_list.copy()
    if idx < 0 or idx >= len(new_list):
        return new_list
    new_list[idx] = element
    return new_list
