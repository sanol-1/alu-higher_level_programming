#!/usr/bin/python3
"""Module that prints a matrix of integers"""


def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers

    Args:
        matrix: the matrix (list of lists) of integers to print
    """
    for row in matrix:
        line = ""
        for i in range(len(row)):
            if i > 0:
                line += " "
            line += "{:d}".format(row[i])
        print(line)
