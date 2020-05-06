#!/usr/bin/python3
def multiple_returns(sentence):
    len_c = len(sentence)
    c = sentence[0] if len_c > 0 else "None"
    tuple_r = (len_c, c)
    return tuple_r
