#!/usr/bin/python3
"""
 A class MyList that inherits from list
"""


class MyList(list):
    """ a method to print lists and  sort them"""
    def print_sorted(self):
        print(sorted(self))
