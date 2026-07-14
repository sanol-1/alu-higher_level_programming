#!/usr/bin/python3
"""Module that deletes an item at a specific position in a list"""


def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list

    Args:
        my_list: the list to modify
        idx: the index to delete

    Returns:
        The list with the item removed, or unchanged if idx is
        negative or out of range
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
