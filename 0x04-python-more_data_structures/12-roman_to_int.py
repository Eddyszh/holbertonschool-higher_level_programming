#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) is str:
        new_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        value = 0
        for i, j in zip(roman_string, roman_string[1:]):
            if new_dict[i] < new_dict[j]:
                value -= new_dict[i]
            else:
                value += new_dict[i]
        value += new_dict[roman_string[-1]]
        return value
    else:
        return 0
