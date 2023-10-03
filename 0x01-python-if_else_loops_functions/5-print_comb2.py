#!/usr/bin/python3
for two_digit_number in range(100):
    if two_digit_number < 99:
        print("{:02d}, ".format(two_digit_number), end="")
    else:
        print("{:02d}".format(two_digit_number))
