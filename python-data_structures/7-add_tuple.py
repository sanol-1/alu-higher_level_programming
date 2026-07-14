#!/usr/bin/python3
"""Module that adds two tuples"""


def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples

    Args:
        tuple_a: the first tuple
        tuple_b: the second tuple

    Returns:
        A tuple with the element-wise addition of the first 2
        elements of each argument. Missing elements are treated as 0.
    """
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (a1 + b1, a2 + b2)
