#!/usr/bin/python3
"""Module that prints the FizzBuzz sequence"""


def fizzbuzz():
    """Prints the numbers from 1 to 100, separated by a space.

    Multiples of 3 print Fizz, multiples of 5 print Buzz,
    multiples of both print FizzBuzz.
    """
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{:d}".format(i), end=" ")
