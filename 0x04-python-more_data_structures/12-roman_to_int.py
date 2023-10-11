#!/usr/bin/python3

def roman_to_int(roman):
    if not roman or not isinstance(roman, str):
        return 0

    r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    s = roman
    l = [r[i[0]] if r[i[0]] >= r[i[1]] else (-1 * r[i[0]))
         for i in zip(s, s[1:] + s[-1])]
    v = sum(l)

    return v
