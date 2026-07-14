#!/usr/bin/python3
"""Module that securely retrieves an element from a list"""


def element_at(my_list, idx):
    """Retrieves an element from a list, like in C

    Args:
        my_list: the list to access
        idx: the index to retrieve

    Returns:
        The element at idx, or None if idx is negative or out of range
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
