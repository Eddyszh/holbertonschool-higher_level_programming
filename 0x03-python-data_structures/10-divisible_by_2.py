#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    r_list = []
    for i in my_list:
        if i % 2 == 0:
            r_list.append(True)
        else:
            r_list.append(False)
    return r_list
