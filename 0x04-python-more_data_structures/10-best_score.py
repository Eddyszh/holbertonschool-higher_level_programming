#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    x = None
    for i in a_dictionary:
        if not x or a_dictionary[i] > a_dictionary[x]:
            x = i
    return x
