#!/usr/bin/python3
"""Print the numbers from 1 to 100 separated by a space.

    For multiples of three, print Fizz instead of the number.
    For multiples of five, print Buzz instead of the number.
    For multiples of three and five, print FizzBuzz instead of the number.
    """
def fizzbuzz():
    def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz", end="")
        if i % 5 == 0:
            print("Buzz", end="")
        if (i % 3 != 0) and (i % 5 != 0):
            print(i, end="")
        print(" ", end="")
