#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    aq = 0

    for x in uniq:
        aq += x

    return aq
