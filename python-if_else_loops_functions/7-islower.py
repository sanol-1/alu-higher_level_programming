#!/usr/bin/python3
"""Module that checks for a lowercase character"""


def islower(c):
    """Checks if a character is lowercase

    Args:
        c: the character to check

    Returns:
        True if c is lowercase, False otherwise
    """
    return ord(c) >= 97 and ord(c) <= 122
