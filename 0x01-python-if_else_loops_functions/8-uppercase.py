#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            n = chr(ord(c) - 32)
        else:
            n = c
        print("{}".format(n), end='')
    print('')
