#!/usr/bin/python3
"""Module that returns multiple values from a sentence"""


def multiple_returns(sentence):
    """Returns the length of a string and its first character

    Args:
        sentence: the string to analyze

    Returns:
        A tuple (length, first character). If sentence is empty,
        the first character is None.
    """
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])
